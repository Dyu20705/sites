---
name: sites-security-review
description: Defensive security guidance and review for SITES code, data pipelines, APIs, dashboard, deployment, dependencies, and future LLM/tool integrations. Use for threat modeling, focused security questions, or explicit security review. Do not turn ordinary code review into a full vulnerability audit automatically.
---

# SITES Security Review

Use a source-first, boundary-first security workflow. This local skill adapts the high-value control ideas reviewed from Cloudflare's `security-audit-skill` at commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`; it is not a vendored copy of the full upstream audit harness.

## Operating modes

**Guidance mode is the default.** Answer focused security questions, inspect relevant source, and propose bounded validation.

**Full audit is explicit opt-in.** If the user requests comprehensive vulnerability hunting/report artifacts, use a dedicated audited security harness only when its execution isolation requirements can actually be enforced.

## Boundary map

For the relevant SITES component, identify:

- untrusted input/source;
- security principal or resource;
- trust boundary crossed;
- validation/transformation;
- side effect or sensitive sink;
- expected security property.

Likely future boundaries include scholarly-provider responses, imported files, dashboard inputs, local paths, credentials/config, dependency/CI/release inputs, and any LLM/tool output if such components are later accepted.

## Finding states

Use:

- **confirmed**: source trace and bounded evidence establish a real boundary failure;
- **needs_validation**: source suggests a credible issue but a decisive fact is missing;
- **rejected**: the candidate was disproved.

Do not assign vulnerability severity to `needs_validation`. Severity requires demonstrated impact, not just deviation from a checklist.

For material findings, prefer an independent second verification before calling them confirmed.

## Execution safety

Source inspection is read-only.

Do not execute target-controlled builds, tests, processes, fuzzers, browsers, or fixtures for security validation unless an OS-enforced sandbox can provide, at minimum:

- no external network except isolated loopback when essential;
- sanitized allowlisted environment with no real credentials;
- read-only target/toolchain with writes limited to dedicated scratch space;
- explicit CPU, memory, process, file, disk, and wall-clock limits.

If these controls are unavailable, keep runtime-dependent leads as `needs_validation` and provide a safe validation plan.

Never probe production/shared endpoints, other users' data, live control planes, real identities, or paid external quota merely to validate a finding.

## SITES-specific priority

Prioritize security work that protects the current slice:

1. secrets and provider authentication;
2. input/path handling and unsafe parsing;
3. provenance/integrity of evidence and generated artifacts;
4. dependency/CI/release supply-chain risk once those systems exist;
5. data lifecycle and access boundaries;
6. LLM prompt/tool/output boundaries only if LLM features are accepted.

Do not manufacture production threat models for components that do not exist.

## Output

For each candidate: boundary, source evidence, observed/expected security outcome, state, impact if confirmed, and smallest safe fix/validation.

End with audited scope, unaudited scope, execution limitations, and any upstream full-audit capability that would be required for stronger evidence.
