# Amendment and exposure log

- **AM-01, 2026-09-27, Codex:** Initial `RE-20260927-01` count request returned HTTP 406 before any records or signal outputs were received. A single separate diagnostic run explicitly requests `Accept: application/atom+xml` (the documented response format), keeps the same declared identity/query/rate limits, and preserves the original manifest. This tests content negotiation only; no proxy, alternate identity, credentials, or access-control bypass. Stop if it fails. No holdout exposure or concept-selection change.
- The same count URL was opened through the web research tool after the initial failure; that tool reported it inaccessible. It supplied no count or records and is not a raw provider snapshot.
