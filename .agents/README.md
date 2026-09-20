# SITES agent skills

Project-local skills are intentionally small and task-scoped. They preserve SITES research and engineering invariants without turning every agent response into one giant system prompt.

## Active skills

| Skill | Role | Activation |
| --- | --- | --- |
| `sites-research-evidence` | Prior art, evidence synthesis, research-method critique | Research/literature/methodology/novelty tasks |
| `sites-source-audit` | Provider/corpus feasibility and temporal/data-quality audit | Data-source or corpus decisions |
| `sites-decision-gate` | Decision record + human acceptance boundary | High-impact design/product/research choices |
| `sites-review` | Evidence-first review across docs, research, code and data | PR/diff/gate/review tasks |
| `sites-security-review` | Defensive security review and escalation contract | Explicit security tasks |

A skill is justified here only when it adds a repeatable procedure, evidence contract, or safety boundary that generic prompting does not reliably preserve. More skills increase trigger ambiguity and context cost, so project-wide installation is deliberately conservative.

## External skills/tools reviewed on 2026-09-19

### Alibaba OpenCodeReview

Reviewed upstream: `alibaba/open-code-review@a003b9341a65130b024829101ea35494b56569e1`.

OpenCodeReview is a code-review harness rather than a passive style prompt. It supplies deterministic diff/rule handling and can either call its own configured LLM or delegate review reasoning to the host agent.

**SITES policy:** do not install it during M0. Re-evaluate at the Feature gate when there is a meaningful implementation diff. Prefer testing delegation mode first so SITES does not add a second LLM-provider configuration by default. Adoption requires a small SITES-specific benchmark covering precision, missed defects/coverage, token/runtime cost, and false-positive review burden.

### Cloudflare security-audit-skill

Reviewed upstream: `cloudflare/security-audit-skill@c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`.

Its strongest ideas are incorporated into `sites-security-review`: source-first findings, explicit trust boundaries, confirmed/needs-validation separation, independent verification for serious findings, and refusal to execute target-controlled code without appropriate isolation.

**SITES policy:** keep the full upstream audit harness external and opt-in. It requires capabilities such as parallel agents and an OS-enforced sandbox that are not M0 project dependencies. Do not auto-install Node packages or run a full audit merely because the security skill exists.

### i-have-adhd

Reviewed upstream: `ayghri/i-have-adhd@ef1a07df87cefee1195397d197815813941caa2f`; its published eval artifact predates this commit.

The skill is primarily output shaping. Its own evaluation reports improved actionability/concision, but also a failed release gate and one meaningful regression where a response asserted a cause without enough evidence.

**SITES policy:** user/session-level opt-in only, not a project invariant. Useful ideas such as bounded steps and visible task state may be used, but research and debugging must preserve uncertainty instead of forcing a “cause -> fix” narrative.

## Deferred skill categories

Do not install skills merely because they may be useful later.

- Browser/UI testing: re-evaluate once a concrete dashboard exists.
- Deployment/MLOps/Kubernetes: re-evaluate only after D09 and deployment scope are accepted.
- Multi-agent orchestration: outside committed M1 product scope.
- Forecasting/optimization: research-ready at most unless a later accepted decision changes M1.

## Updating this catalog

For any new project-wide skill:

1. identify the repeated failure mode it addresses;
2. inspect provenance, license, dependencies, permissions, executable content, and maintenance;
3. compare it with a small local skill or no skill;
4. define trigger and non-trigger cases;
5. benchmark material behavior where outputs are objectively testable;
6. require human acceptance before adding a dependency or broad always-on behavior.

Do not auto-update external skills. Review upstream diffs before changing a recorded revision.
