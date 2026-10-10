# 14 — Thực nghiệm development D08 và gói quyết định cho owner

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
