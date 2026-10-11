# 14 — Thực nghiệm development D08 và gói quyết định cho owner

**Audit mới nhất, 11/10/2026:** phần [Final #64 DoD audit](#final-64-dod-audit--11102026) bên dưới xác minh frozen result, ghi owner decisions còn thiếu và giới hạn của standalone helper. Giữ nguyên báo cáo development có ngày phía dưới.

**Disposition owner tiếp theo:** [#70](https://github.com/Dyu20705/sites/issues/70#issuecomment-6097713689) nghiệm thu development-only evidence này và chọn hướng retrospective-only. [Packet 15](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) chứa exact amendment và D07/D08/quality decisions còn PROPOSED; phần chọn A/B phía dưới là lịch sử. Independent scientific quality giữ NOT MEASURED, kể cả sau synthetic workflow test được cho phép riêng. Không đổi measurement/configuration/declaration ở đây.

**VERIFIED, 10/10/2026:** #65 đã đóng `completed` sau [owner acceptance](https://github.com/Dyu20705/sites/issues/65#issuecomment-6097421846), [A acknowledgment](https://github.com/Dyu20705/sites/issues/64#issuecomment-6097520949) và [completion record](https://github.com/Dyu20705/sites/issues/65#issuecomment-6097523060). #64 đã có count/share thực đo trong phạm vi exploratory. **D07/D08/D09 PROPOSED; E3/#70 NOT PASSED.** Packet phục vụ owner quyết định, chưa phải confirmatory contract đã freeze hoặc quyền triển khai D09. Deadline demo-ready: **15/10/2026**.

## Declaration, đơn vị và ranh giới kết luận

Trạng thái bắt đầu: branch `research/exit-evidence-20260927`, working tree sạch và khớp origin tại `53a50ec806b2d6d5fee4112554a6826aeaea852b`; PR #75 OPEN/Draft; #64/#65/#70 OPEN. Owner chỉ chấp thuận negative investigation outcome của #65, với điều kiện A acknowledgment. A chạy lại 17 tests hiện hữu và tái tạo audit/normalized/crosscheck khớp bytes; đây là same-host agent verification, không phải independent human approval.

Câu hỏi: count và normalized share mô tả gì theo lexical rule fuzzing hiện hữu, và artifact nào làm sai diễn giải? Construct: **tần suất lexical trong title v1 của frozen retrospective development query**. Đơn vị = distinct scholarly work. Query `cat:cs.SE AND submittedDate:[201901010000 TO 201906302359]`, tháng 01–06/2019, UTC monthly bins theo v1 submission. Cả 598 observed current-category works, gồm nonmatches, đủ điều kiện; run thực không có exclusions hoặc title/date unknown. Không đo complete historical cs.SE, toàn bộ nghiên cứu software testing, emergence, importance, adoption, causality hoặc independent detection quality.

[Declaration local](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration.json) được ghi trước real signal execution; [corrected declaration](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json) giữ điều kiện đó và công khai lỗi metadata. Agent đọc nhầm escaping trong JSON lồng của tool output, ban đầu suy ra regex transport mismatch. Đối chiếu trực tiếp disproved nhận định này: root/frozen config và `checks.PATTERN` giống nhau. Không đổi lexical rule. Declaration và outputs đầu được giữ; corrected reports chỉ sửa provenance text. Literal-config diagnostic cũng có chín matches. Correction diễn ra sau khi xem initial output và được ghi đúng là post-exposure.

Rule version `RE-20260927-01-documented-word-boundary-v1`: `\bfuzz(?:ing|er|ers)?\b`, case-insensitive, title v1. Fuzzing đã được chọn trong proposal gốc từ context độc lập năm 2018, không giả định hướng biến động. Prior exposure gồm corpus metadata, synthetic outputs và chín late-ID development works. Declaration local hoặc push sau execution không chứng minh independent preregistration timing. Không query, xem hoặc ghi holdout 07–12/2019; candidate split chưa được chấp thuận.

## Công thức và quan sát development thực

Với eligible distinct works C_b: `N(b)=|C_b|`, `n(c,b)=sum(match(c,w) for w in C_b)` và `p(c,b)=n(c,b)/N(b)` khi `N(b)>0`. Title missing/invalid vẫn trong N nhưng n/p null; giữ known matches và [lower, upper] share bounds. Event time missing/invalid làm monthly denominators unresolved, không âm thầm loại works chưa biết bin. Collapse duplicate v1; conflicting v1 fail; revised observations không đóng góp lần nữa. N=0 thì share undefined. Đây là research interfaces, chưa phải product schema.

| Tháng UTC | Eligible N | Matches n | Share (%) | Title missing / invalid |
| --- | ---: | ---: | ---: | ---: |
| 2019-01 | 91 | 0 | 0.0000 | 0 / 0 |
| 2019-02 | 79 | 1 | 1.2658 | 0 / 0 |
| 2019-03 | 97 | 2 | 2.0619 | 0 / 0 |
| 2019-04 | 103 | 1 | 0.9709 | 0 / 0 |
| 2019-05 | 122 | 4 | 3.2787 | 0 / 0 |
| 2019-06 | 106 | 1 | 0.9434 | 0 / 0 |

Tổng **9/598 = 1.5050%**; support chỉ 0–4 works/tháng. Tháng 02, 04, 06 cùng count=1 nhưng share khác vì N khác. Share bổ sung denominator context, chưa chứng minh substantive trend mạnh hơn. Một title đổi trạng thái match làm share đổi khoảng 0.82–1.27 percentage points tùy N. Tháng 01 có zero rule matches trong observed titles, không có nghĩa không có nghiên cứu fuzzing.

Matched works: `1902.09334`, `1903.02981`, `1903.08483`, `1904.07280`, `1905.01405`, `1905.06944`, `1905.07147`, `1905.10499`, `1906.00621`. [Measurements](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/measurements.json) lưu title và raw file/entry index/entry ID/SHA-256; 598 denominator IDs truy qua [normalized corpus frozen](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-1/normalized-records.json). Không tạo AI relevance labels.

Sensitivities đã khai báo trước execution, báo cáo đầy đủ: exact `fuzzing` cho **0/0/1/1/2/1 = 5 matches**; current-title và v1-category-subset giữ chín matches và sáu denominators. Đây là local stability, không chứng minh historical categories hoặc vocabulary completeness. Loại chín late IDs giữ n nhưng N thành **91/79/96/103/122/98**; March/June share thành **2.0833%/1.0204%**. Đây là perturbation trên observed real records, **không sửa được as-of membership**. Gộp hai tháng liền nhau cho **1/170, 3/200, 5/228** (0.5882%, 1.5000%, 2.1930%); hình thức mượt hơn không phải growth label hoặc lý do chọn window này. As-of n/N/p vẫn null.

## Controlled failure modes và prior art

[Mười controlled checks](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/controlled-checks.json) dùng synthetic data với expected values xác định bằng tay; không đo provider behavior.

| Controlled check | Kết quả đã chạy / ý nghĩa |
| --- | --- |
| Corpus growth | 10/100 → 20/200: count gấp đôi, share vẫn 0.1 |
| Denominator drift | 10/100 → 10/200: share giảm nửa dù matching count giữ nguyên |
| Duplicates/revisions | Lặp v1 và thêm v2 giữ 1/10 |
| Title missing/invalid | Hai unknowns trong ba: n/p null, known match=1, bounds 1/3..1 |
| Sparse/small/empty | 1/1 so với 1/2 thiếu ổn định; share 0/0 null |
| Alias drift | Stipulated same topic đổi “Fuzzing” thành “AFL software testing”: lexical count 1→0 |
| Delayed availability | Retrospective bin vẫn chứa synthetic late-public item; as-of fixture hiện hữu loại stipulated late availability |
| Query selection | Concept-selected subset đổi 10/100 thành 10/10 |
| Category mutation | Current cs.SE so với v1 ngoài cs.SE đổi inclusion 1→0 |
| Cutoff leakage | Future event bị loại; fixture hiện hữu từ chối future vocabulary và loại late membership/availability |

Tách riêng real-data evidence: [B audit](11_REAL_CORPUS_AUDIT_20261010.md) ghi 161 revised works, 55 title differences, bốn category differences và chín late-ID anomalies. Synthetic leakage checks và exact-v1 replay không cung cấp real historical availability còn thiếu.

Prior-art checks ngày 10/10: [Manès et al. (2018), v1](https://arxiv.org/abs/1812.00140v1), abstract/history, cung cấp pre-cutoff topic context, không reference trend label hoặc complete dictionary. [Štimec et al. (2026)](https://link.springer.com/article/10.1007/s11192-026-05744-5), abstract/introduction, trình bày title/abstract n-grams, normalization, burst models và plot-based human evaluation; lexical methods tự nó không đủ novelty claim. Plot judgments của họ không cung cấp independent evidence-based reference cho corpus SITES này. Kleinberg burst là alternative từ EL-002 đã kiểm tra trước; PDF fetch trong execution này thất bại nên không claim mới xác minh full text. Chưa có observed requirement biện minh thêm burst, persistence hoặc citations. Read depth và access failures trong [source log](../../../experiments/research_exit_20260927/runs/20261010-signal-01/source-inspection.json).

## Independent reference protocol — PROPOSED, CHƯA CHẠY

Detection quality, independent annotations và researcher agreement đều **NOT MEASURED**. Survey 2018, regex và plots của chính output không phải trend ground truth. Finite frozen corpus không phải independent random sample của một field.

[Pilot manifest 27 works](../../../experiments/research_exit_20260927/runs/20261010-signal-01/reference-pilot-plan.json) là PROPOSED/NOT EXECUTED, annotations null; selection strata chỉ dành cho organizer và phải bỏ khỏi blinded review view.

1. Giữ fuzzing là development case và synthetic constant-share corpus growth là computational control. Ghi exposure trước lựa chọn case/control mới; không thay concept để tăng support. Control không chứng minh real-world trend validity.
2. Smallest discriminating pilot: hai researchers do owner chỉ định đọc chín matched works và 18 nonmatches, ba mỗi tháng theo fixed hash order, seed `D08-REF-20261010-01`. Selection **sau** khi xem signal, phải công khai. Che month, match status, counts, plots và quyết định của rater khác; producing agent không là independent rater. Pilot cân bằng có thể phát hiện false positives và một số misses, không ước lượng population recall từ 18 negatives hoặc chứng minh trend quality.
3. Rubric: positive = permitted paper evidence xác nhận fuzzing là substantive method/research subject; negative = evidence xác nhận subject khác với terminology incidental/irrelevant; uncertain = inaccessible, ambiguous hoặc conflicting. Ghi exact version/source/section, evidence date, annotator, rationale. Dùng paper abstracts/method sections và independent context, không dựa vào sự xuất hiện candidate token. Không automatic/LLM labels. Historical reference cần cutoff-valid evidence, nếu thiếu thì retrospective-only.
4. Giữ cả hai raw judgments. Researcher thứ ba được chỉ định adjudicate bất đồng, vẫn giữ uncertainty gốc; missing evidence không là negative. Báo pairwise agreement, positive/negative/uncertain và TP/FP/FN chỉ đối chiếu adjudicated independent semantic relevance; giải thích stratification/uncertainty. Muốn claim complete topic recall hoặc reference monthly prevalence cần independent relevance census cả 598 works; semantic relevance vẫn khác lexical prevalence.
5. Reference trend directions cần independent time-indexed substantive evidence, construct/population/interval khớp rõ; hai researchers có thể gán positive change / negative change / uncertain kèm citations. Nếu evidence chỉ cho topic context thì mọi direction labels vẫn uncertain. Không lấy count/share hoặc cảm nhận từ plots của chúng tạo reference này.
6. Chống leakage: chưa xem 07–12; giữ pilot/rubric development-only, ghi source versions, che signal metadata và đối soát chín exposed IDs trước accepted split tương lai. Freeze case/control/rubric/sensitivity/support/quality protocol đầy đủ với owner acceptance trước genuinely unexposed holdout.

**Proposed numeric computational criteria:** zero mismatches ở các hand-calculated cases đã định nghĩa; 100% contributing-ID/source lineage; zero replay byte differences trong semantic artifacts; zero duplicate contributions. Căn cứ = deterministic correctness, không statistical quality target. Có thể báo count khi n=0, share chỉ khi N>0 và fields known; không claim finite minimum support hoặc precision threshold đủ cho trend label. **Independent semantic/trend quality threshold và minimum support vẫn UNRESOLVED; cần pilot evidence và owner acceptance.** Chín matches chưa biện minh confident performance target. Pilot phát hiện misses/ambiguity hoặc thiếu aligned independent temporal evidence → INSUFFICIENT EVIDENCE; không sửa regex/threshold sau exposure để che kết quả.

## D08 recommendation và alternatives tại #70

**PROPOSED D08:** normalized lexical share, bắt buộc kèm count và N; raw count là serious simpler alternative. Evidence: real equal-count/different-N months và controlled growth null. Reversal conditions: denominator không đầy đủ, material vocabulary/selection sensitivity, independent relevance disagreement hoặc reviewer không hiểu construct hẹp này. Có thể cần abstention, prospective development proposal mới hoặc rejection; không tự cấp quyền burst/LLM scoring. Chưa chọn directional labels hoặc product stack.

| Option #70 | Evidence thiếu / smallest test | Deadline và hệ quả claim |
| --- | --- | --- |
| A — historical as-of | Một dated category/announcement capture cụ thể có provenance, coverage gồm removals/additions, cutoff-valid field/vocabulary và đủ lịch sử cho monthly cutoffs; preregister request/byte budget trước acquisition; đối soát chín anomalies và enumerate membership độc lập current positives | B bounded screen chưa xác minh qualifying capture. Test cost chưa biết khi chưa tìm ra source; thêm abstract pages không giải quyết completeness. Rủi ro cao cho 15/10; giữ E3 hiện hữu và dừng dependent work nếu thiếu |
| B — retrospective-only scope proposal | Owner sửa target/estimand và affected D05/E3/M1/E2 requirements rõ ràng; duyệt frozen observed 2026-query population, v1-submission bins, lexical rule, reference/support/quality behavior, exposure/freeze contract mới | Khả thi nhất cho narrow evidence-backed demonstration vì đã có frozen data và descriptive evaluation. Bỏ claim historical public availability, complete historical membership và cutoff-valid vocabulary. E3 gốc vẫn NOT PASSED; requirement hồi cứu mới có thể kiểm tra development boundaries/version/lineage nhưng không được gọi original E3 PASS |

**Recommendation: trình Option B cho owner review ngay**, dựa trên evidence gap đã xác minh và năm ngày tới demo deadline. Đây là value/feasibility judgment, chưa acceptance hoặc chứng minh demo sẽ pass. Nếu owner giữ A, phải tìm capture nói trên trước; nếu không có thì giữ M1 NOT PASSED theo contract hiện hữu. Complete cutoff-valid capture được chứng minh sẽ đảo recommendation này. B giữ giá trị descriptive corpus comparison, abstention, lineage và replay; mất historical-as-of validity, chưa validate user value. Không tự chọn provider/corpus mới, physical model, dependency, dashboard hoặc deployment.

Owner cần quyết định: A hay B và scope amendment cụ thể; D07 population/time semantics; D08 rule/formula, no-label claim boundary, pilot/rubric và quality criteria có căn cứ; experiment freeze/split an toàn exposure mới; disposition #70 rõ ràng. D09 là quyết định sau accepted Research Exit. GO: owner review và development-only independent pilot sau khi thống nhất personnel/protocol. STOP: holdout, #71/#72 dependent implementation, E3/#70 pass, merge, release và deploy.

## Validation và artifacts có thể kiểm tra

Source: [evaluator](../../../experiments/research_exit_20260927/signal_evaluator.py), [11 new unit tests](../../../experiments/research_exit_20260927/test_signal_evaluator.py), [read-only verifier](../../../experiments/research_exit_20260927/validate_signal.py). **28/28 tool tests + 15/15 legacy synthetic tests + 10/10 controlled cases PASS**. Fixture ID conflict ban đầu được sửa trước real measurement. Hai corrected processes tái tạo semantic artifacts; timestamps/environment ở execution manifests riêng. Direct-XML arithmetic riêng kiểm tra cả 598 inputs và chín matching source refs. [Verification](../../../experiments/research_exit_20260927/runs/20261010-signal-01/verification.json) ghi input/output hashes, parsing/link checks và D05–D09 không đổi; [execution manifest](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/execution.json) ghi runtime 3.14.7, code/config SHA-256, UTC timestamps. Frozen config SHA-256: `f4ed7d7bca9c9665a9cb03437c79306f282e15ebb5ad9520bf6126deff61f1f7`.

Lệnh chính xác từ repository root, dùng Python sẵn có; host này cần escalation vì sandbox không thấy runtime:

```powershell
python -m unittest discover -s experiments/research_exit_20260927 -p "test_*.py" -v
python experiments/research_exit_20260927/checks.py --output <new-directory>/legacy-checks.json
python experiments/research_exit_20260927/signal_evaluator.py --declaration experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json --output <new-directory>/replay-1
python experiments/research_exit_20260927/signal_evaluator.py --declaration experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json --output <new-directory>/replay-2
python experiments/research_exit_20260927/validate_signal.py --run experiments/research_exit_20260927/runs/20261010-signal-01 --output <new-directory>/verification.json
git diff --check
```

Evaluator/tests/replay đều offline; literature-page inspection tách khỏi corpus measurement. Same-host agent verification và bilingual self-review không phải independent scientific validation, user validation, product benchmark hoặc E1–E8 acceptance. Relative links/parsing được tự động kiểm tra; external freshness, anchors và translation meaning có giới hạn riêng. Xem [bản tiếng Anh](../../english/research/14_D08_DEVELOPMENT_EVALUATION_20261010.md).

## Final #64 DoD audit — 11/10/2026

**Verdict: #64 READY FOR OWNER REVIEW**, theo outcome proposal mô tả hữu hạn kèm các kết luận thiếu bằng chứng rõ ràng. Không phải đóng issue, nghiệm thu scientific quality hoặc Research Exit. **E3 gốc và #70 vẫn NOT PASSED.** Không đổi threshold, formula, case, corpus, holdout hoặc trạng thái quyết định.

Baseline sạch: `research/exit-evidence-20260927@ed2a21f36b8b0b05efd889279717b61dbe777eda`, upstream bằng nhau (0 ahead/0 behind), live PR head và `git ls-remote` cùng SHA. Checkout ban đầu là `dev@0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`, sạch; chỉ sửa trong worktree research hiện hữu. PR #75 OPEN/Draft, không có submitted review hoặc inline review thread; #65 CLOSED/completed; #64/#69/#70 OPEN. [State/source record](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/context.json). Direction ngày 10/10 chỉ cho phép proposal hồi cứu, chưa accept exact clauses. WIP: #64; #70 là gate.

### Findings và correction hữu hạn

- **P0 scientific blockers giữ nguyên:** chưa xác lập population/public availability/vocabulary lịch sử; independent semantic/trend quality NOT MEASURED. Chưa có human raters, zero real annotations. SIMULATED_A/B/C trên SYN-001…027 không giải quyết các gaps này.
- **P1 đã sửa — validator ghi đè:** `validate.py` trước đây ghi trực tiếp vào historical `results/validation.json`; nay bắt buộc `--output` mới và exclusive creation. Hai subprocess regressions chứng minh giữ bytes có sẵn và thiếu path trả exit 2. README dùng đường dẫn mới. Không sửa historical validation/checks/evaluator/config/raw/results.
- **P1 khi tái sử dụng cho input khác — membership boundary đã xác nhận:** standalone `evaluate()` gặp thiếu `categories_current` thì loại work và trả empty bin n=0, N=0, p=null thay vì unknown membership. [Reproducer/output](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary-probe.json). Đây không phải general fail-closed ingestion interface. Frozen CLI kiểm đúng hashes; cả 598 records thật có valid cs.SE membership, không exclusions, nên arithmetic đã công bố không bị ảnh hưởng. Giữ pinned evaluator. Trước broader reuse phải có membership guard/correction được version riêng và regression, hoặc giữ đúng fixed-input boundary. Không âm thầm đổi experiment contract.
- **P2 làm rõ scope:** phương pháp tính riêng trên cùng host không phải independent scientist/machine. Bảy owner rows của packet vẫn chưa điền; giữ nguyên version/bytes của packet.

### Ma trận DoD

VERIFIED chỉ xác nhận quan sát ghi trong dòng; PARTIAL/UNKNOWN/BLOCKED không tự thành PASS qua amendment còn đề xuất.

| Requirement | Evidence path | Verification method | Status | Finding | Smallest corrective action |
| --- | --- | --- | --- | --- | --- |
| A1 construct/claims | [14](14_D08_DEVELOPMENT_EVALUATION_20261010.md), [15 §1](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Đối chiếu EN/VI với n/N thực | VERIFIED | Lexical prevalence của title v1 trong 598 observed works do frozen query cs.SE năm 2026 trả về, bin hồi cứu theo submission tháng 2019; không emergence/causality/semantic recall | Owner quyết exact estimand |
| A1 prior art/alternatives/gap | [ledger](01_EVIDENCE_LEDGER.md), [EL-001–005](06_RESEARCH_EXIT_EVIDENCE.md), [09](09_RESEARCH_MASTER_20261010.md), [source review](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/context.json) | Đọc lại primary abstract/introduction/manual, kiểm provenance cũ | PARTIAL | Có main lexical method, serious count comparator và burst alternative; fetch PDF Kleinberg mới thất bại; search metadata lịch sử chưa đủ; chưa novelty | Giữ read-depth limits; chỉ tìm novelty riêng nếu có claim mới |
| A2 arithmetic/unit/denominator | [recount](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/independent-verification.json) | Raw XML + token scanner riêng, không import project | VERIFIED | 598 distinct works gồm mọi nonmatches; N=91/79/97/103/122/106, n=0/1/2/1/4/1; 598 source refs, 9 match refs | Không cần sửa fixed experiment |
| A2 confounders/sensitivity/negative results | [measurements](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/measurements.json), [11](11_REAL_CORPUS_AUDIT_20261010.md), [execution](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/execution.json) | Tính lại năm variants, two-month sums; replay mười controls | VERIFIED | Growth/denominator/query/alias/revisions/delay/cutoff được thử; loại late IDs cho N=91/79/96/103/122/98, exact fuzzing=5; không loại selection bias | Giữ mọi kết quả; chưa căn cứ thêm signal |
| A2 uncertain input/missing bins | [tests](../../../experiments/research_exit_20260927/test_signal_evaluator.py), [boundary](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary-probe.json) | Missing/invalid title/date, zero/empty, conflicts/duplicates/partial acquisition và missing category | PARTIAL | n=0 khác unknown và empty N; complete input có sáu bins rõ; partial acquisition bị reject; helper còn giới hạn membership | Guard trước broader reuse; missing retrieval bin không là empty bin |
| A3 case/control/exposure | [03](03_CASE_SELECTION_PROTOCOL.md), [preregistration](../../../experiments/research_exit_20260927/preregistration.json), [15 §7](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Context 2018, candidate/exclusion log, chronology | PARTIAL | Context fuzzing độc lập plot; synthetic null chỉ computational; chưa independently proven timing; 598 works đã exposure, pilot chọn sau output | Prospective immutable freeze; không gọi development là holdout |
| A3 annotation/roles/uncertainty | [pilot](../../../experiments/research_exit_20260927/runs/20261010-signal-01/reference-pilot-plan.json), [15 §5–6](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Tái tạo 27 IDs theo seed, kiểm null fields/simulation | BLOCKED | 9 matches + 18 nonmatches chưa real labels/personnel; 54 synthetic judgments là fixture; quality/recall/agreement NOT MEASURED | Owner chỉ định người đủ chuyên môn/rubric nếu giữ route này, hoặc chọn rõ limited route |
| A4 exact D08 | [declaration](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json), [15 §4–6](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Decode config, 18 lexical cases gồm Unicode/underscore, recount | VERIFIED | Python Unicode IGNORECASE word boundaries, distinct v1 work, UTC month, n/N; share luôn kèm n/N, không directional labels | Accept exact rule/contract; hiện chưa approval |
| A4 support/quality/alternatives | [14](14_D08_DEVELOPMENT_EVALUATION_20261010.md), [15 §6/8](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Tách mathematical criteria khỏi scientific evidence | UNKNOWN | N≥1 chỉ định nghĩa share; support 0–4/tháng; scientific precision/agreement/min-support targets UNRESOLVED; count là alternative thực chất | Không chọn số tùy ý; pilot và prospective justified criteria nếu giữ yêu cầu |
| A4 decision/freeze | [15 §2/7/9](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md), [#70](https://github.com/Dyu20705/sites/issues/70) | Đối chiếu D05/D06, M1/E1–E8 gốc, owner direction | BLOCKED cho acceptance; VERIFIED có proposal | Nghĩa vụ gốc còn hiệu lực; E2-R/E3-R chưa accepted; product E4/E7/E8 còn thiếu; chưa freeze | Owner ghi từng lựa chọn theo immutable bytes và limitation audit |

**Science thực đo:** exact lexical counts/proportions, field/identity checks, sensitivity perturbations. Chưa đo scientific field growth, semantic coverage, independent detector accuracy, user value, effect size hoặc human agreement. Tests chỉ chứng minh arithmetic/workflow đã kiểm. E2-R chỉ hoãn original independent scientific-reference acceptance nếu owner chọn rõ; E3-R thay nghĩa vụ temporal của demo nhưng không sửa historical E3. Hiện chưa kích hoạt deferral nào.

### Scientific/reference integrity

Reports 14/15 giới hạn substantive conclusions trong finite observed population. Equal-count/different-N chỉ chứng minh tác dụng arithmetic của normalization; denominator có selection bias vẫn biased. Năm exact-fuzzing so với chín broad-rule matches là vocabulary sensitivity, không semantic recall. Current-title stability theo rule không xóa 55 title changes. Chín late IDs vẫn trong corpus theo v1 event; trừ chúng không tìm lại members đã bị loại/chưa index. Support nhỏ và sáu bins không đủ trend label hoặc causal interpretation.

Đọc lại ngày 11/10: [Manès v1 abstract/history](https://arxiv.org/abs/1812.00140v1) chỉ cho context trước 2019; [Štimec abstract/introduction](https://link.springer.com/article/10.1007/s11192-026-05744-5) hỗ trợ đối chiếu lexical/normalization/burst/plot evaluation, không SITES accuracy. [arXiv manual](https://info.arxiv.org/help/api/user-manual.html), [availability](https://info.arxiv.org/help/availability.html), [terms](https://info.arxiv.org/help/api/tou.html) hỗ trợ version/time semantics và phân biệt quyền metadata/paper. Không dataset API hoặc holdout. Kleinberg giữ historical EL-002 inspection, không new full-text verification. Không novelty, exhaustive review hoặc claim không tồn tại historical archive.

Human follow-up nhỏ nhất, có điều kiện: hai researchers đủ chuyên môn do owner chỉ định, người thứ ba phân xử; giữ 27 IDs, công khai post-output selection; opaque IDs/random order, giấu strata/month/plots. Title lộ từ nên không blind rule hoàn hảo. Khóa judgments trước mở source links, ghi exposure; giữ raw labels và uncertain/pending. Rubric dùng substantive-topic evidence, không regex/plot làm truth. Báo từng stratum/uncertainty; không suy ra population recall/trend accuracy. Không bịa personnel/labels/scientific thresholds.

### Owner choices — PROPOSED, riêng G70 NOT PASSED

| Row / exact choice | Alternative | Lợi ích / chi phí, scientific limit | Verified evidence / reversal |
| --- | --- | --- | --- | --- |
| A1 — §1/2 finite observed-2026 v1-title estimand | Giữ broad question và defer | Bounded description tái lập; bỏ historical/semantic/detector claims | Recount + negative #65; đảo khi owner cần broader validity hoặc có historical evidence phù hợp |
| A2 — §2 thay E2/E3 bằng E2-R/E3-R | Giữ original obligations | Descriptive demo kiểm được; không đáp ứng original reference/availability | E3 unresolved, controls/replay có; đảo nếu không đáp ứng research objective |
| A3 — §5/6 limited acceptance, quality NOT MEASURED | Giữ independent-reference tại #70 | Quyết định hẹp sớm hơn; mất scientific accuracy acceptance | Zero real labels; đảo nếu reviewer hiểu sai hoặc cần validated quality |
| D07 — §3 đúng 598 works/query/v1 UTC/frozen provenance/bias | Defer hoặc historical capture riêng | Denominator quan sát có sẵn; không historical completeness/representativeness | 14 hashes/598 refs; đảo khi identity/completeness fail |
| D08 — §4–6 fixed lexical n/N/share, no labels/null/support/sensitivity/reference | Count alone hoặc defer | Share thêm denominator context; còn selection/alias/sparse limits | 9/598, sensitivities; đảo khi denominator invalid/hiểu sai; broader reuse cần guard |
| F1 — §7 prospective immutable manifest/exposure | Không confirmatory evaluation | Exact replay/reviewer protocol; không xóa exposure cũ | Có artifact identities, chưa acceptance/personnel/task freeze; sửa nếu approved bytes đổi/overlap |
| G70 — §9 disposition sau accepted criteria có evidence | Giữ NOT PASSED | Tách research contract khỏi product readiness | Rows chưa điền; chỉ đổi sau explicit D07/D08/amendment/freeze và mọi retained research criterion |

Packet `M1-R-20261010-v1` không sửa/activate qua audit. Git-blob SHA-256 vẫn EN `da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122`, VI `164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0`. Acceptance phải định danh version/hash, mọi revision ghi rõ. Rubric 5/5 và budget 60 giây/256 MiB chưa accepted/measured, là engineering/task criteria, không scientifically calibrated thresholds. D09 riêng.

### Validation thực chạy và coverage

[Execution record](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/execution.json) giữ exact argv/environment/stdout/stderr/exit codes và 13 byte comparisons. Python 3.14.7, Windows, stdlib. **37/37 unit tests PASS** (35 cũ + hai preservation regressions); **15/15 legacy checks mỗi hai process**; **10/10 controls mỗi signal replay**; hai workflow processes, hai audit processes, crosscheck và cả hai validators. Successful commands exit 0; deliberate existing-output call exit 2, giữ bytes. Lần đầu default temp chạy 35 tests với 27 setup/cleanup PermissionErrors, exit 1; đặt TEMP/TMP trong workspace sửa giới hạn môi trường. Không che failing assertion.

Từ repository root, mỗi runner tạo scratch directory mới được ignore; không corpus network:

```powershell
python experiments/research_exit_20260927/runs/20261011-final-audit-01/run_checks.py
python experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py --output <new-directory>/independent.json
python experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary_probe.py --output <new-directory>/boundary.json
git diff --check
```

| Frozen artifact tái tạo | SHA-256 |
| --- | --- |
| audit.json | `53a5aff1d8ea577e5789c7dc96a784f9f3c46339495e38ea78d266b41158dbd8` |
| normalized-records.json | `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1` |
| measurements.json | `214c103f82784665907f76925ea56763fd2e46644ce52ccf6950b08e807cc818` |
| crosscheck.json | `0664d7dcd1ad3d1fd570696b47b254ce54329ffcc56c9b6416482830379c6591` |

[Recount script](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py) không import evaluator/parser project; kiểm v1/current refs với XML, 14 inputs với committed bytes, flags/escaping/boundaries, toàn bộ sensitivities và pilot selection. Chỉ chạy process riêng không được gọi independent verification. Frozen/history inputs không đổi. Review gồm 00/01/03/04, D05/D06/M1/evaluation, paired 11–15, declarations/source logs/pilot/measurements, evaluator/audit/crosscheck/simulator/tests/validators, live issues/comments/PR. Các file PR #75 khác chỉ inventory/hash/context review, không exhaustive security/provider-capability review; giữ negative history. Links/parsing/numeric pairing kiểm tự động; EN/VI meaning tự review, không independent translation validation.

**Next action nhỏ nhất:** owner review exact packet không đổi cùng audit này; chọn A1/A2/A3/D07/D08/F1 riêng, ghi G70 có căn cứ. Nếu giữ independent-reference acceptance, chỉ định humans và biện minh/freeze prospective criteria trước evaluation đó. #64 vẫn open, #70 NOT PASSED; chưa product/holdout/merge.
