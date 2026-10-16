# Offline code delivery

This branch contains the implementation and tests at product commit 6c08a95614c275c70287aca0d2d2e1e29ced9cb4, plus the Windows PowerShell runner and byte-preserving Git attributes. It depends on accepted frozen research commit 0673903c7cf8e4c6725af8a13f2ca4e40a1457a9.

The runner is for the owner's registered Windows machine and existing reviewer ZIP. It uses UTF-8 BOM for Windows PowerShell 5.1 and a fresh timestamped extraction directory. See evaluation/REPLAY.md for the CLI protocol. A fresh source checkout alone does not include the external ZIP or prospective machine-specific evaluation/profile records; these remain in the local delivery package.

The reviewer reported 27/27 tests PASS and two builds/compare PASS on 16 October 2026. Current code bytes were checked against that package, and the runner passed Windows PowerShell syntax parsing. This branch contains no new reviewer response files, runtime profiles or machine execution records. Those are preserved separately in the local evidence commit 525eb3f.

Remote codex/m1-offline-slice at 95d1ecf6eb55bedb26d8a21a85d69d9c7e5f3a96 contains a different implementation. This code is delivered separately on codex/m1-offline-code; neither history is overwritten or merged. Scientific quality remains NOT MEASURED and original E3 NOT PASSED. This delivery does not close #73 or declare full M1 readiness.
