"""
Unit and Extensibility Tests for Observation Event Contract (Issue #57: Architecture A1).
Tests BaseObservation, typed observation events (Work, Citation, Relation, Metric),
SourceCapabilities, backward-compatibility bridge, and Level 2/3 extensibility.
"""

from datetime import date, datetime, timezone
import pytest

from scholarly_platform.models import (
    BaseObservation,
    WorkObservation,
    AuthorObservation,
    InstitutionObservation,
    VenueObservation,
    CitationObservation,
    RelationObservation,
    MetricObservation,
    SourceCapabilities,
    ObservationBundle,
    ParsedWork,
    ParsedAuthor,
    ParsedCitation,
)


def test_base_observation_initialization():
    """Verifies baseline observation metadata and timestamp defaults."""
    obs = BaseObservation(
        observation_id="obs_test_001",
        source_name="arxiv",
        run_id="run_2026_01",
        source_record_id="2301.00001",
        raw_payload={"sample_key": "sample_val"},
    )
    assert obs.observation_id == "obs_test_001"
    assert obs.source_name == "arxiv"
    assert obs.run_id == "run_2026_01"
    assert obs.schema_version == "1.0.0"
    assert obs.raw_payload == {"sample_key": "sample_val"}
    assert isinstance(obs.observed_at, datetime)
    assert obs.observed_at.tzinfo is not None  # UTC aware


def test_work_observation_attributes():
    """Verifies WorkObservation retains bibliographical metadata and identifier tuples."""
    work_obs = WorkObservation(
        observation_id="work_001",
        source_name="crossref",
        run_id="run_crossref_01",
        title="Attention Is All You Need",
        abstract="The dominant sequence transduction models...",
        publication_year=2017,
        publication_date=date(2017, 12, 6),
        raw_venue_name="NeurIPS 2017",
        venue_type="CONFERENCE",
        identifiers=[("DOI", "10.5555/3295222.3295349"), ("ARXIV", "1706.03762")],
    )
    assert work_obs.title == "Attention Is All You Need"
    assert work_obs.publication_year == 2017
    assert len(work_obs.identifiers) == 2
    assert work_obs.identifiers[0] == ("DOI", "10.5555/3295222.3295349")


def test_citation_observation_tuple_identifiers():
    """
    Verifies CitationObservation models directed citation edges via generic identifier tuples,
    free from provider-specific conditionals or schema restrictions.
    """
    cite_obs = CitationObservation(
        observation_id="cite_001",
        source_name="semantic_scholar",
        run_id="run_s2_01",
        citing_identifiers=[("DOI", "10.1145/330534.330536")],
        cited_identifiers=[
            ("PMID", "12345678"),
            ("DBLP", "conf/nips/VaswaniSPUJGKP17"),
            ("ARXIV", "1706.03762"),
        ],
        is_influential=True,
        citation_intents=["METHODOLOGY", "BACKGROUND"],
    )
    assert cite_obs.is_influential is True
    assert "METHODOLOGY" in cite_obs.citation_intents
    assert len(cite_obs.cited_identifiers) == 3
    assert cite_obs.cited_identifiers[0] == ("PMID", "12345678")
    assert cite_obs.cited_identifiers[1] == ("DBLP", "conf/nips/VaswaniSPUJGKP17")


def test_relation_observation_domain_semantics():
    """
    Verifies RelationObservation models typed scholarly relationships (FRBR/ontology level)
    such as PREPRINT_OF, PUBLISHED_AS, EXTENDED_VERSION_OF, SUPPLEMENTED_BY.
    """
    rel_obs = RelationObservation(
        observation_id="rel_001",
        source_name="datacite",
        run_id="run_datacite_01",
        subject_identifiers=[("DOI", "10.5061/dryad.pk045")],
        predicate_relation="SUPPLEMENTED_BY",
        object_identifiers=[("DOI", "10.1093/nar/gkx1234")],
        subject_type="DATASET",
        object_type="WORK",
    )
    assert rel_obs.predicate_relation == "SUPPLEMENTED_BY"
    assert rel_obs.subject_type == "DATASET"
    assert rel_obs.object_type == "WORK"
    assert rel_obs.subject_identifiers == [("DOI", "10.5061/dryad.pk045")]


def test_metric_observation_properties():
    """Verifies MetricObservation models point-in-time quantitative indicators."""
    metric_obs = MetricObservation(
        observation_id="met_001",
        source_name="openalex",
        run_id="run_oa_01",
        entity_type="WORK",
        entity_identifiers=[("DOI", "10.1000/182")],
        metric_name="citation_count",
        metric_value=1542.0,
    )
    assert metric_obs.metric_name == "citation_count"
    assert metric_obs.metric_value == 1542.0
    assert metric_obs.entity_type == "WORK"


def test_source_capabilities_profile():
    """Verifies declarative SourceCapabilities profiles for heterogeneous source archetypes."""
    # Archetype A: Traditional metadata provider (arXiv)
    arxiv_caps = SourceCapabilities(
        source_name="arxiv",
        provides_works=True,
        provides_authors=True,
        provides_citations=False,
        supported_formats=("xml", "jsonl"),
    )
    assert arxiv_caps.provides_works is True
    assert arxiv_caps.provides_citations is False
    assert "xml" in arxiv_caps.supported_formats

    # Archetype B: Pure citation provider (OpenCitations)
    opencitations_caps = SourceCapabilities(
        source_name="opencitations",
        provides_works=False,
        provides_authors=False,
        provides_citations=True,
        provides_citation_intents=False,
        supported_formats=("csv", "jsonl"),
    )
    assert opencitations_caps.provides_works is False
    assert opencitations_caps.provides_citations is True

    # Archetype C: Dataset & Relation provider (DataCite)
    datacite_caps = SourceCapabilities(
        source_name="datacite",
        provides_works=True,
        provides_relations=True,
        provides_citations=False,
        supported_formats=("jsonl",),
    )
    assert datacite_caps.provides_relations is True


def test_level_2_semantic_extensibility_citation_only():
    """
    Level 2 Semantic Extensibility Test:
    Proves that a source providing ONLY citations (e.g. OpenCitations) can emit
    CitationObservation events without needing dummy titles, fake authors, or a ParsedWork object.
    """
    raw_opencitations_record = {
        "citing": "10.1109/5.771073",
        "cited": "10.1145/330534.330536",
        "creation": "1999-06-01",
        "timespan": "P1Y",
    }

    # Adapter extracts observation event directly
    citation_event = CitationObservation(
        observation_id="oc_obs_001",
        source_name="opencitations",
        run_id="run_oc_2026",
        citing_identifiers=[("DOI", raw_opencitations_record["citing"])],
        cited_identifiers=[("DOI", raw_opencitations_record["cited"])],
        raw_payload=raw_opencitations_record,
    )

    bundle = ObservationBundle(
        source_name="opencitations",
        run_id="run_oc_2026",
        citations=[citation_event],
    )

    assert len(bundle.works) == 0  # Zero dummy works required!
    assert len(bundle.authors) == 0  # Zero dummy authors required!
    assert len(bundle.citations) == 1
    assert bundle.citations[0].citing_identifiers == [("DOI", "10.1109/5.771073")]
    assert bundle.citations[0].cited_identifiers == [("DOI", "10.1145/330534.330536")]


def test_level_3_domain_extensibility_relation_observation():
    """
    Level 3 Domain Extensibility Test:
    Proves that a source providing dataset/software linkages (e.g. DataCite) can emit
    RelationObservation events without falsely coercing them into bibliographical citation edges.
    """
    raw_datacite_relation = {
        "dataset_doi": "10.5061/dryad.pk045",
        "relation": "isSupplementTo",
        "article_doi": "10.1093/nar/gkx1234",
    }

    relation_event = RelationObservation(
        observation_id="dc_obs_001",
        source_name="datacite",
        run_id="run_dc_2026",
        subject_identifiers=[("DOI", raw_datacite_relation["dataset_doi"])],
        predicate_relation="SUPPLEMENTED_BY",
        object_identifiers=[("DOI", raw_datacite_relation["article_doi"])],
        subject_type="DATASET",
        object_type="WORK",
        raw_payload=raw_datacite_relation,
    )

    bundle = ObservationBundle(
        source_name="datacite",
        run_id="run_dc_2026",
        relations=[relation_event],
    )

    assert len(bundle.citations) == 0  # Not falsely coerced to citation edge!
    assert len(bundle.relations) == 1
    assert bundle.relations[0].predicate_relation == "SUPPLEMENTED_BY"


def test_parsed_work_to_observation_bundle_bridge():
    """
    Verifies backward compatibility bridge:
    Existing ParsedWork objects produced by current parsers can be converted
    losslessly into an ObservationBundle with discrete observation events.
    """
    parsed = ParsedWork(
        source_name="arxiv",
        source_work_id="1706.03762",
        title="Attention Is All You Need",
        abstract="The dominant sequence transduction models...",
        publication_year=2017,
        publication_date=date(2017, 6, 12),
        normalized_arxiv_id="1706.03762",
        normalized_doi="10.5555/3295222.3295349",
        raw_venue_name="arXiv",
        citation_count=45000,
        influential_citation_count=12000,
        authors=[
            ParsedAuthor(raw_name="Ashish Vaswani", position=1, orcid="0000-0001-0000-0001"),
            ParsedAuthor(raw_name="Noam Shazeer", position=2),
        ],
        citations=[
            ParsedCitation(cited_doi="10.1145/330534.330536", is_influential=True, citation_intents=["BACKGROUND"]),
        ],
        external_ids={"mag": "2963403868"},
    )

    bundle = parsed.to_observation_bundle(run_id="run_test_bridge")
    assert bundle.source_name == "arxiv"
    assert bundle.run_id == "run_test_bridge"

    # Work verification
    assert len(bundle.works) == 1
    work_obs = bundle.works[0]
    assert work_obs.title == "Attention Is All You Need"
    assert work_obs.publication_year == 2017
    # Identifiers extracted into tuples
    id_dict = dict(work_obs.identifiers)
    assert id_dict["DOI"] == "10.5555/3295222.3295349"
    assert id_dict["ARXIV"] == "1706.03762"
    assert id_dict["MAG"] == "2963403868"

    # Authors verification
    assert len(bundle.authors) == 2
    assert bundle.authors[0].raw_name == "Ashish Vaswani"
    assert bundle.authors[0].position == 1
    assert bundle.authors[0].orcid == "0000-0001-0000-0001"

    # Citations verification
    assert len(bundle.citations) == 1
    cite_obs = bundle.citations[0]
    assert cite_obs.is_influential is True
    assert cite_obs.citation_intents == ["BACKGROUND"]
    assert ("DOI", "10.1145/330534.330536") in cite_obs.cited_identifiers

    # Metrics verification
    assert len(bundle.metrics) == 2
    metric_map = {m.metric_name: m.metric_value for m in bundle.metrics}
    assert metric_map["citation_count"] == 45000.0
    assert metric_map["influential_citation_count"] == 12000.0
