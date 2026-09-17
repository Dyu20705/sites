# sites - Scholar intelligant & tech evolution system

(English)[/README.md] | (Tiếng Việt)[/docs/vietnamese/README.md]

This repository implements an automated data mining pipeline designed to extract, analyze, and forecast **technology development trends** from large-scale bibliographic and scholarly databases. 

Rather than a generic literature search, this pipeline is highly opinionated. It filters for **high-impact, authoritative research** and dynamically aligns the knowledge discovery process with specific, user-defined research vectors (e.g., Multi-Agent Systems, MLOps, Distributed Architecture).

## Core Objectives

* **Targeted Trend Analysis:** Mine citation graphs and textual metadata to identify rising technologies, paradigm shifts, and decaying methodologies over time.
* **Impact & Authority Filtering:** Cut through the noise by prioritizing literature based on "citation velocity," influential citation metrics, and the historical authority of authors/venues.
* **Strict Semantic Alignment:** Ensure the mined trends are deeply relevant to specific technical directions by utilizing vector embeddings and semantic similarity scores against target prompts.
* **Insight Synthesis:** Automatically generate temporal trend reports, concept heatmaps, and highlight the "frontier" papers driving current technological shifts.

## Data Sources

| Source | Role in Pipeline |
| :--- | :--- |
| **Semantic Scholar (S2AG)** | High-signal filtering using "influential citation" flags and citation intent. |
| **OpenAlex** | Comprehensive graph for tracking the temporal growth of specific tech concepts. |
| **arXiv (OAI-PMH)** | The primary source for bleeding-edge preprints in CS, AI, and Systems. |
| **DBLP** | Verified metadata for top-tier computer science conferences and journals. |

## Pipeline Architecture (Canonical Scholarly Data Platform)

```text
[1. arXiv OAI-PMH Harvester]
      │ Incremental harvesting (Watermark + lookback window, bounded retries, resumptionToken)
      ▼
[2. Bronze Layer: Raw Landing & Manifest]
      │ ├── Immutable Raw Storage: data/raw/arxiv/YYYY/MM/...
      │ ├── raw_source_manifest: SHA-256 payload deduplication & audit trail
      │ └── ingestion_quarantine: Malformed XML & DQ-02 isolated routing
      ▼
[3. Silver Layer: Source Work Observations]
      │ ├── High-fidelity XML parser: arXiv, arXivRaw, oai_dc
      │ ├── Preserves LaTeX/TeX equations non-destructively ($\mathcal{O}(n \log n)$)
      │ └── Captures preprints, revisions (v1, v2), withdrawals, categories, licenses
      ▼
[4. Gold Layer: Canonical Entity Resolution]
      │ ├── Deterministic UUIDv5 Work Identity (Work != Version)
      │ ├── In-place revision updates with Source Authority Priority Matrix
      │ └── Lossless lineage tracking in canonical_work_provenance
```

## Quick Start & Verification

### Run End-to-End Pipeline Verification
Execute the automated 7-step verification suite (XML parsing, manifest calculation, Medallion ingestion, idempotent replay, watermark safety, quarantine isolation, layer summary):
```bash
uv run python scripts/verify_arxiv_pipeline.py
```

### Run Test Suite
Execute the full test suite (57 tests covering Harvester, Parser, Watermark, Idempotency, Schema, Resolution):
```bash
uv run pytest -v
```