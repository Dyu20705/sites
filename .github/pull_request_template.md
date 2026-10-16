## Problem and scope

What outcome does this change deliver? Link the issue, accepted contract/decision, and exact baseline SHA. State **non-goals** and implementation boundaries.

## Change summary

Describe behavior and relevant files, without agent logs or promotional language.

## Evidence and verification

| Requirement / check | Exact command or evidence | Result | Environment / limitations |
| --- | --- | --- | --- |
| Repository policy | `python tools/check_repository.py` | PENDING | |
| Unit/integration tests | | PENDING | |
| Research freeze / regression (if relevant) | | PENDING | |
| Documentation and security review | | PENDING | |
| Human evaluation / E7 / E8 (if relevant) | | NOT MEASURED | |

Only mark PASS for an executed test on the stated commit. A simulated reviewer, synthetic fixture or same-host replay is not an independent evaluation.

## Risks, scientific claims and compatibility

Include source/temporal semantics, hashes and frozen artifacts affected; security impact; migrations/rollback; correctness or resource limitations; and any unmatched baseline. Clearly separate VERIFIED, PROPOSED, UNKNOWN, NOT PASSED and NOT MEASURED.

## Review decision gates

- [ ] I inspected the complete final diff and confirmed the selected baseline.
- [ ] The change does not silently alter accepted D05–D09/F1 contracts or evidence bytes.
- [ ] Canonical user-facing documentation is in English; special immutable evidence exceptions are explicit.
- [ ] Required checks have run on the final commit; failing/missing checks are disclosed.
- [ ] No secrets, personal reviewer material, temporary outputs or unsupported capability claims are published.
- [ ] Any major product/research/security decision has explicit owner approval.
- [ ] No BLOCKER or MAJOR correctness/evidence finding remains unresolved.

## Review and delivery

Explain reviewer focus, how to reproduce results, what remains blocked, and whether this is a **draft**, merge candidate or release candidate. Do not auto-merge, force-push or close a gate merely because the PR template was completed.
