"""
Domain Models and Typed Data Structures for Canonical Scholarly Platform.
Represents Bronze runs/manifest/quarantine, Silver observations, and Gold canonical entities.
"""

from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import List, Optional, Dict, Any, Tuple
import uuid


def utc_now() -> datetime:
    """Returns current UTC datetime."""
    return datetime.now(timezone.utc)



@dataclass
class IngestionRun:
    """Represents a discrete pipeline execution batch and run-level lineage."""
    run_id: str
    source_name: str
    input_uri: Optional[str] = None
    input_hash: str = ""
    record_count: int = 0
    accepted_count: int = 0
    rejected_count: int = 0
    error_count: int = 0
    pipeline_version: str = "0.1.0"
    parser_version: str = "0.1.0"
    schema_version: str = "1.0.0"
    started_at: datetime = field(default_factory=utc_now)
    completed_at: Optional[datetime] = None
    status: str = "IN_PROGRESS"


@dataclass
class IngestionWatermark:
    """Represents an incremental harvesting checkpoint/watermark."""
    source_name: str
    watermark_type: str
    last_success_datestamp: Optional[str] = None
    last_run_id: Optional[str] = None
    updated_at: datetime = field(default_factory=utc_now)


@dataclass
class RawManifestRecord:
    """Represents an immutable record in the Bronze landing manifest."""
    raw_record_id: str
    run_id: str
    source_name: str
    payload_hash: str
    payload: Dict[str, Any]
    source_record_id: Optional[str] = None
    raw_path: Optional[str] = None
    source_datestamp: Optional[str] = None
    retrieved_at: datetime = field(default_factory=utc_now)
    ingested_at: datetime = field(default_factory=utc_now)


@dataclass
class QuarantineRecord:
    """Represents a rejected or malformed record in Bronze quarantine."""
    quarantine_id: str
    run_id: str
    source_name: str
    raw_payload: Dict[str, Any]
    error_type: str
    error_message: str
    quarantined_at: datetime = field(default_factory=utc_now)


@dataclass
class ParsedAuthor:
    """Represents an author mention extracted from a source record."""
    raw_name: str
    position: int
    orcid: Optional[str] = None
    source_author_id: Optional[str] = None
    raw_affiliation: Optional[str] = None
    institution_name: Optional[str] = None
    institution_ror: Optional[str] = None
    institution_country: Optional[str] = None
    is_corresponding: bool = False


@dataclass
class ParsedCitation:
    """Represents a citation reference extracted from a source record."""
    cited_doi: Optional[str] = None
    cited_arxiv_id: Optional[str] = None
    cited_source_id: Optional[str] = None
    raw_citation_string: Optional[str] = None
    is_influential: bool = False
    citation_intents: List[str] = field(default_factory=list)


@dataclass
class ParsedWork:
    """Represents a parsed, normalized work observation before database staging."""
    source_name: str
    source_work_id: str
    title: str
    abstract: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[date] = None
    normalized_doi: Optional[str] = None
    normalized_arxiv_id: Optional[str] = None
    source_version: Optional[str] = None
    raw_venue_name: Optional[str] = None
    venue_issn: Optional[str] = None
    venue_type: Optional[str] = None
    raw_categories: List[str] = field(default_factory=list)
    raw_comments: Optional[str] = None
    license: Optional[str] = None
    is_withdrawn: bool = False
    is_deleted: bool = False
    source_datestamp: Optional[str] = None
    citation_count: int = 0
    influential_citation_count: int = 0
    authors: List[ParsedAuthor] = field(default_factory=list)
    citations: List[ParsedCitation] = field(default_factory=list)
    external_ids: Dict[str, str] = field(default_factory=dict)
    observed_at: datetime = field(default_factory=utc_now)
    raw_payload: Dict[str, Any] = field(default_factory=dict)

    def to_observation_bundle(self, run_id: str = "default_run") -> "ObservationBundle":
        """Converts monolithic ParsedWork into an ObservationBundle for backward compatibility."""
        base_id = f"obs_{self.source_name}_{uuid.uuid4().hex[:12]}"

        ids = []
        if self.normalized_doi:
            ids.append(("DOI", self.normalized_doi))
        if self.normalized_arxiv_id:
            ids.append(("ARXIV", self.normalized_arxiv_id))
        for k, v in self.external_ids.items():
            ids.append((k.upper(), str(v)))

        work_obs = WorkObservation(
            observation_id=base_id,
            source_name=self.source_name,
            run_id=run_id,
            observed_at=self.observed_at,
            source_record_id=self.source_work_id,
            raw_payload=self.raw_payload,
            title=self.title,
            abstract=self.abstract,
            publication_year=self.publication_year,
            publication_date=self.publication_date,
            source_version=self.source_version,
            raw_venue_name=self.raw_venue_name,
            venue_issn=self.venue_issn,
            venue_type=self.venue_type,
            raw_categories=list(self.raw_categories),
            raw_comments=self.raw_comments,
            license=self.license,
            is_withdrawn=self.is_withdrawn,
            is_deleted=self.is_deleted,
            source_datestamp=self.source_datestamp,
            identifiers=ids,
        )

        author_obs = [
            AuthorObservation(
                raw_name=a.raw_name,
                position=a.position,
                orcid=a.orcid,
                source_author_id=a.source_author_id,
                raw_affiliation=a.raw_affiliation,
                institution_name=a.institution_name,
                institution_ror=a.institution_ror,
                institution_country=a.institution_country,
                is_corresponding=a.is_corresponding,
            )
            for a in self.authors
        ]

        citation_obs = []
        for c in self.citations:
            citing_ids = list(ids)
            cited_ids = []
            if c.cited_doi:
                cited_ids.append(("DOI", c.cited_doi))
            if c.cited_arxiv_id:
                cited_ids.append(("ARXIV", c.cited_arxiv_id))
            if c.cited_source_id:
                cited_ids.append(("SOURCE_ID", c.cited_source_id))

            citation_obs.append(
                CitationObservation(
                    observation_id=f"cite_obs_{uuid.uuid4().hex[:12]}",
                    source_name=self.source_name,
                    run_id=run_id,
                    observed_at=self.observed_at,
                    source_record_id=self.source_work_id,
                    raw_payload={},
                    citing_identifiers=citing_ids,
                    cited_identifiers=cited_ids,
                    is_influential=c.is_influential,
                    citation_intents=list(c.citation_intents),
                    raw_citation_string=c.raw_citation_string,
                    citing_source_id=self.source_work_id,
                    cited_source_id=c.cited_source_id,
                )
            )

        metric_obs = []
        if self.citation_count > 0:
            metric_obs.append(
                MetricObservation(
                    observation_id=f"metric_obs_{uuid.uuid4().hex[:12]}",
                    source_name=self.source_name,
                    run_id=run_id,
                    observed_at=self.observed_at,
                    source_record_id=self.source_work_id,
                    raw_payload={},
                    entity_type="WORK",
                    entity_identifiers=list(ids),
                    metric_name="citation_count",
                    metric_value=float(self.citation_count),
                )
            )
        if self.influential_citation_count > 0:
            metric_obs.append(
                MetricObservation(
                    observation_id=f"metric_obs_{uuid.uuid4().hex[:12]}",
                    source_name=self.source_name,
                    run_id=run_id,
                    observed_at=self.observed_at,
                    source_record_id=self.source_work_id,
                    raw_payload={},
                    entity_type="WORK",
                    entity_identifiers=list(ids),
                    metric_name="influential_citation_count",
                    metric_value=float(self.influential_citation_count),
                )
            )

        return ObservationBundle(
            source_name=self.source_name,
            run_id=run_id,
            works=[work_obs],
            authors=author_obs,
            citations=citation_obs,
            metrics=metric_obs,
        )


@dataclass(frozen=True)
class SourceCapabilities:
    """Declares the capability profile of a scholarly data provider."""
    source_name: str
    provides_works: bool = True
    provides_authors: bool = True
    provides_citations: bool = False
    provides_citation_intents: bool = False
    provides_relations: bool = False
    provides_metrics: bool = False
    provides_institutions: bool = False
    supported_formats: Tuple[str, ...] = ("jsonl",)


@dataclass(kw_only=True)
class BaseObservation:
    """Foundational contract for all source-specific observation events."""
    observation_id: str
    source_name: str
    run_id: str
    observed_at: datetime = field(default_factory=utc_now)
    source_record_id: Optional[str] = None
    raw_record_id: Optional[str] = None
    schema_version: str = "1.0.0"
    raw_payload: Dict[str, Any] = field(default_factory=dict)


@dataclass(kw_only=True)
class WorkObservation(BaseObservation):
    """Observation of a scholarly work's bibliographical attributes."""
    title: str = ""
    abstract: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[date] = None
    source_version: Optional[str] = None
    raw_venue_name: Optional[str] = None
    venue_issn: Optional[str] = None
    venue_type: Optional[str] = None
    raw_categories: List[str] = field(default_factory=list)
    raw_comments: Optional[str] = None
    license: Optional[str] = None
    language: Optional[str] = None
    is_withdrawn: bool = False
    is_deleted: bool = False
    source_datestamp: Optional[str] = None
    identifiers: List[Tuple[str, str]] = field(default_factory=list)


@dataclass
class AuthorObservation:
    """Observation of an author mention associated with a work."""
    raw_name: str
    position: int
    orcid: Optional[str] = None
    source_author_id: Optional[str] = None
    raw_affiliation: Optional[str] = None
    institution_name: Optional[str] = None
    institution_ror: Optional[str] = None
    institution_country: Optional[str] = None
    is_corresponding: bool = False


@dataclass(kw_only=True)
class InstitutionObservation(BaseObservation):
    """Observation of an academic or research institution."""
    name: str = ""
    ror_id: Optional[str] = None
    country_code: Optional[str] = None
    homepage_url: Optional[str] = None


@dataclass(kw_only=True)
class VenueObservation(BaseObservation):
    """Observation of a publication venue (journal, conference, repository)."""
    name: str = ""
    issn: Optional[str] = None
    venue_type: Optional[str] = None


@dataclass(kw_only=True)
class CitationObservation(BaseObservation):
    """Observation of a directed citation edge between two scholarly works."""
    citing_identifiers: List[Tuple[str, str]] = field(default_factory=list)
    cited_identifiers: List[Tuple[str, str]] = field(default_factory=list)
    is_influential: bool = False
    citation_intents: List[str] = field(default_factory=list)
    raw_citation_string: Optional[str] = None
    citing_source_id: Optional[str] = None
    cited_source_id: Optional[str] = None


@dataclass(kw_only=True)
class RelationObservation(BaseObservation):
    """Observation of a typed semantic relationship between scholarly entities."""
    subject_identifiers: List[Tuple[str, str]] = field(default_factory=list)
    predicate_relation: str = "RELATED_TO"
    object_identifiers: List[Tuple[str, str]] = field(default_factory=list)
    subject_type: str = "WORK"
    object_type: str = "WORK"


@dataclass(kw_only=True)
class MetricObservation(BaseObservation):
    """Observation of an entity-level metric (e.g. citation count, download count)."""
    entity_type: str = "WORK"
    entity_identifiers: List[Tuple[str, str]] = field(default_factory=list)
    metric_name: str = ""
    metric_value: float = 0.0


@dataclass
class ObservationBundle:
    """A container of discrete observation events produced during record parsing."""
    source_name: str
    run_id: str
    works: List[WorkObservation] = field(default_factory=list)
    authors: List[AuthorObservation] = field(default_factory=list)
    citations: List[CitationObservation] = field(default_factory=list)
    relations: List[RelationObservation] = field(default_factory=list)
    metrics: List[MetricObservation] = field(default_factory=list)
    institutions: List[InstitutionObservation] = field(default_factory=list)
    venues: List[VenueObservation] = field(default_factory=list)


@dataclass
class SourceWorkObservation:
    """Represents an immutable record-level observation in the Silver layer."""
    observation_id: str
    run_id: str
    source_name: str
    source_work_id: str
    title: str
    observed_at: datetime
    raw_record_id: Optional[str] = None
    source_version: Optional[str] = None
    normalized_doi: Optional[str] = None
    normalized_arxiv_id: Optional[str] = None
    abstract: Optional[str] = None
    publication_date: Optional[date] = None
    publication_year: Optional[int] = None
    raw_venue_name: Optional[str] = None
    raw_categories: List[str] = field(default_factory=list)
    raw_comments: Optional[str] = None
    license: Optional[str] = None
    is_withdrawn: bool = False
    is_deleted: bool = False
    citation_count: int = 0
    influential_citation_count: int = 0
    raw_authors: List[Dict[str, Any]] = field(default_factory=list)
    raw_citations: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class CanonicalWork:
    """Represents an authoritative canonical work entity in the Gold layer."""
    canonical_work_id: str
    title: str
    abstract: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[date] = None
    canonical_doi: Optional[str] = None
    canonical_arxiv_id: Optional[str] = None
    canonical_venue_id: Optional[str] = None
    is_stub: bool = False
    stub_reason: Optional[str] = None
    created_from_source: Optional[str] = None
    citation_count: int = 0
    influential_citation_count: int = 0
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)


@dataclass
class CanonicalVenue:
    """Represents an authoritative venue in the Gold layer."""
    canonical_venue_id: str
    name: str
    normalized_name: str
    venue_type: Optional[str] = "UNSPECIFIED"
    tier: Optional[str] = "UNRANKED"
    issn: Optional[str] = None


@dataclass
class CanonicalInstitution:
    """Represents an authoritative institution in the Gold layer."""
    canonical_inst_id: str
    name: str
    ror_id: Optional[str] = None
    country_code: Optional[str] = None
    homepage_url: Optional[str] = None


@dataclass
class CanonicalAuthor:
    """Represents an authoritative researcher in the Gold layer."""
    canonical_author_id: str
    display_name: str
    orcid: Optional[str] = None
    aliases: List[str] = field(default_factory=list)


@dataclass
class CanonicalWorkIdentifier:
    """Represents an identifier mapping in the Gold layer."""
    identifier_type: str
    normalized_value: str
    canonical_work_id: str
    raw_value: str


@dataclass
class CanonicalWorkAuthor:
    """Represents a work-author junction row in the Gold layer."""
    canonical_work_id: str
    canonical_author_id: str
    author_position: int
    canonical_inst_id: Optional[str] = None
    raw_author_name: Optional[str] = None
    raw_affiliation_string: Optional[str] = None
    is_corresponding: bool = False


@dataclass
class CanonicalCitation:
    """Represents a directed citation edge in the Gold layer."""
    citing_work_id: str
    cited_work_id: str
    is_influential: bool = False
    citation_intents: List[str] = field(default_factory=list)
    source_provider: str = ""


@dataclass
class CanonicalWorkProvenance:
    """Represents attribute-level lineage pointing to the winning source observation."""
    canonical_work_id: str
    attribute_name: str
    winning_source: str
    source_observation_id: str
    resolution_rule: str
    selected_at: datetime = field(default_factory=utc_now)


@dataclass
class MetricsProvenance:
    """Represents a time-series metric snapshot."""
    canonical_work_id: str
    metric_name: str
    metric_value: float
    source_provider: str
    run_id: str
    observed_at: datetime
    source_observation_id: Optional[str] = None
