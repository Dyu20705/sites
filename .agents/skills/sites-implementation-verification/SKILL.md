---
name: sites-implementation-verification
description: Verify bounded SITES implementation, test and performance claims against fixed contracts; invoke for product code, data pipeline, test and runtime review.
---

# Implementation verification

1. State accepted interfaces, frozen inputs, invariants, expected output and no-go scope before code changes.
2. Distinguish source byte identity, scientific measurement identity, exact artifact hashes and semantic replay equality. Do not treat them as interchangeable.
3. Review negative tests: malformed records, duplicate keys/IDs, unsafe paths, missing data, incomplete outputs, tampering and resource-limit failure.
4. Run the narrowest meaningful test and the full relevant suite on the final SHA; record OS, Python version, exact command, status and missing checks.
5. For benchmark or E8 claims, measure on the accepted target with the accepted method. Linux smoke tests and simulated reviewers never establish Windows human E7/E8.
6. Report observed findings separately from speculative risks and required owner decisions. Stop at a failed contract or unaccepted architecture/release gate.

Do not add framework, database, queue or distributed orchestration without a measured requirement and accepted design decision.
