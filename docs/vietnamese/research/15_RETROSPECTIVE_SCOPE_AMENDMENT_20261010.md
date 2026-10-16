# 15 — Scope amendment hồi cứu và decision packet D07/D08

**Packet ID: M1-R-20261010-v1. Trạng thái: PROPOSED.** Cần owner review và chấp thuận đúng packet này. [Quyết định owner ngày 10/10](https://github.com/Dyu20705/sites/issues/70#issuecomment-6097713689) nghiệm thu investigation/bằng chứng development-only và chọn hướng retrospective-only. Quyết định cho phép chuẩn bị, chưa chấp thuận contract này, D07/D08, thresholds, freeze hoặc Research Exit. Revision bằng chứng: `64da78be17f0b89bbd008f5033192742fd663046`, PR #75 OPEN/Draft; #65 CLOSED/completed; #64/#70 OPEN, đã kiểm tra qua GitHub ngày 10/10. Hạn demo-ready: **15/10/2026**.

Chỉ dẫn tiếp theo của owner trong phiên này cho phép **SIMULATED A/B/C và kiểm thử workflow synthetic trên 27 works hư cấu**. Owner giữ independent scientific quality ở NOT MEASURED và yêu cầu #70 đáp ứng đúng bộ tiêu chí đã được chấp thuận. Chưa có người đánh giá thật được chỉ định. Đây không phải chấp thuận D08 hoặc bỏ một yêu cầu hiện hành.

## 1. Quyết định và estimand — PROPOSED

Đề xuất sửa M1 thành demo mô tả có thể tái lập về **lexical prevalence trong tiêu đề v1 trên tập kết quả arXiv cs.SE đã quan sát và đóng băng năm 2026**, nhóm hồi cứu theo tháng submission v1 UTC từ tháng 01–06/2019.

Câu hỏi chính đề xuất: *Nhà nghiên cứu có thể kiểm tra và tái lập số lượng, tỷ lệ distinct works đã quan sát có tiêu đề v1 khớp rule fuzzing được đánh version, hiểu tác động của denominator/corpus selection và truy ngược mọi đóng góp tới bằng chứng nguồn đã đóng băng hay không?*

Estimand là đại lượng mô tả một corpus hữu hạn, không phải ước lượng toàn bộ hoạt động cs.SE lịch sử. Báo cáo n, N, n/N và evidence/uncertainty. Không suy diễn historical public availability, emergence, tăng/giảm của lĩnh vực khoa học, tầm quan trọng, adoption, nhân quả, topic recall hoặc trend detection đã được kiểm định. Lexical count bằng 0 không có nghĩa không có nghiên cứu fuzzing. Semantic relevance là construct khác, chất lượng độc lập vẫn chưa đo. Không tuyên bố scientific novelty.

| Authority / yêu cầu | Trạng thái hiện tại | Tác động của packet |
| --- | --- | --- |
| Hướng M1 retrospective-only | ACCEPTED theo comment owner | Estimand chính xác và đường nghiệm thu bên dưới vẫn PROPOSED |
| D05 / D06 | ACCEPTED | Giữ D06; chỉ sửa cách áp dụng temporal isolation của D05 sau chấp thuận rõ ràng |
| D07 / D08 / D09 | PROPOSED | Các quyết định owner riêng biệt; không chấp thuận architecture |
| E3 gốc / Research Exit #70 | NOT PASSED | Không đổi nhãn E3 gốc thành PASS; E3-R là yêu cầu mới được đề xuất riêng |
| Independent scientific quality | NOT MEASURED | Kết quả SIMULATED không đáp ứng yêu cầu independent reference |

## 2. Tác động amendment theo từng điều khoản

[M1](../baseline/M1.md), [D05](../master/07_DECISION_LOG.md) và [evaluation protocol](../master/06_EVALUATION_PROTOCOL.md) gốc còn hiệu lực đến khi amendment được chấp thuận. Các dòng dưới là đề xuất thay thế/làm rõ, không phải sửa để tự kích hoạt gate mới.

| Điều khoản gốc | Thay đổi chính xác được đề xuất | Nghĩa vụ giữ lại / năng lực mất đi |
| --- | --- | --- |
| D05: temporal isolation và E3 hiện hành | Áp dụng contract hồi cứu được chấp thuận qua E3-R; giữ E3 lịch sử NOT PASSED, ngoài claim của demo đã sửa | Vẫn bắt buộc ranh giới version/event/snapshot; mất historical availability validity |
| D05: lineage, tách observation/derivation, replay, idempotency, explainability | Không giảm yêu cầu | Mọi đóng góp numerator/denominator vẫn kiểm tra được; conflict phải fail closed |
| D06 / M1 §2: researcher và task | Giữ user; chỉ cho chọn rule fuzzing đã chấp thuận và các khoảng con trong sáu tháng quan sát | Giá trị với user thật vẫn cần E7; không thêm nhóm người dùng |
| M1 §1 / §3 và các RQ hỗ trợ | Thay câu hỏi concept-change detection rộng bằng §1 ở trên | Không có đáp án trend detection được kiểm định; RQ rộng được defer, không coi là đã giải quyết |
| M1 §4 input | Thay corpus candidate chưa chốt bằng D07-R tại §3 | Một nguồn, 598 works quan sát, sáu tháng; không acquisition mới hoặc claim population lịch sử |
| M1 §5 output | D08-R tại §4: lexical n/N/share, support, lineage, missingness và giới hạn claim rõ ràng | Không nhãn emerging/growing/stable/declining, composite score hoặc independent quality claim |
| M1 §6–§8 flow, non-goals và D09 | Giữ flow và exclusions; D09 vẫn riêng | Packet không chọn database/framework/API/dashboard/deployment |
| M1 §9 giả thuyết historical state | Giữ negative finding insufficient evidence của #65 | Historical reconstruction rời critical path trước mắt; mở lại cần proposal hữu hạn được chấp thuận riêng |
| M1 §9 giả thuyết giá trị signal | Kiểm tra arithmetic, denominator effects và reviewer hiểu lexical prevalence | Không chứng minh semantic relevance, trend validity hoặc tính hữu ích tổng quát |
| M1 §10 freeze / holdout | Với demo giới hạn này, thay bằng replay contract trên development đã exposure và freeze trước task reviewer mới | Không claim confirmatory detector; tháng 07–12/2019 vẫn không được truy cập theo authorization hiện tại |
| M1 §10 toàn bộ E1–E8 và xử lý failure | Chỉ áp dụng matrix dưới nếu owner chấp thuận rõ | Failure phải hiển thị; không tune threshold để cứu demo |
| M1 §10–§11 deadline / phases | Dùng mốc demo-ready 15/10 đã được chấp thuận; chuyển bước theo gate | Ngày đến không tự làm gate PASS |

| ID | Tiêu chí áp dụng được đề xuất | Evidence hiện có / còn thiếu |
| --- | --- | --- |
| E1 (giữ) | Không sai lệch ở deterministic fixtures cố định và arithmetic cross-check riêng; tolerance được chốt | Có development checks trong [report 14](14_D08_DEVELOPMENT_EVALUATION_20261010.md); chưa kiểm thử product integration |
| E2-R (thay thế, cần acceptance) | Case fuzzing cố định, synthetic constant-share control, toàn bộ sensitivities đã khai báo, synthetic annotation workflow checks; reviewer độc lập giải thích đúng lexical/semantic và retrospective/as-of | Workflow đã kiểm tra tại §5; real semantic/trend reference NOT MEASURED. Chỉ thay yêu cầu scientific detection-quality gốc nếu được chấp thuận rõ |
| E3-R (thay thế, cần acceptance) | Population offline đã freeze; đúng identity v1/event/window/config; loại event ngoài window; không claim availability/vocabulary lịch sử; future-event fixture không đổi bin trước đó | Boundary fixtures và provenance hỗ trợ development checks. E3 gốc vẫn NOT PASSED; product replay vẫn phải đạt E3-R |
| E4 (giữ) | Tác giả và reviewer khác replay độc lập input/config/code/environment đã chấp thuận, semantic output giống nhau | Có các process cùng host do agent tạo; còn thiếu independent reviewer replay |
| E5 (giữ) | 100% lineage từ assessment hiển thị tới rule, toàn bộ eligible IDs, numerator/nonmatches và raw source refs | Có development XML/ID check; còn thiếu navigation bằng dashboard |
| E6 (giữ) | Không duplicate contribution; replay lặp lại giữ nguyên semantic result | Có tool checks; còn thiếu integrated demo check |
| E7 (giữ, làm rõ rubric) | Reviewer độc lập hoàn thành chọn concept/window, diễn giải, mở evidence không sửa code; đúng cả năm interpretation checks tại §6 | NOT MEASURED; chưa có dashboard dùng được |
| E8 (giữ, đề xuất budget) | Demo offline đúng corpus đã chấp thuận ≤598 works; replay ≤60 giây wall time, peak process memory ≤256 MiB trên environment reviewer được ghi nhận; không live corpus request | Engineering budget PROPOSED sau development exposure; memory và reviewer runtime NOT MEASURED. Không suy diễn scalability |

E2-R thay điều demo phải chứng minh, không đổi nghĩa scientific quality. Nếu owner giữ điều kiện independent reference tại #70 thì SIMULATED test vẫn để điều kiện đó chưa đạt và **#70 tiếp tục NOT PASSED**. Không tự bỏ qua tiêu chí nào.

**Phân bổ gate — PROPOSED:** trước #70, cần quyết định rõ A1/A2/A3/D07/D08/F1, immutable research contract đã accepted, frozen corpus/arithmetic/lineage đã validate và synthetic workflow evidence; mọi independent scientific-reference criterion owner giữ lại cũng phải đạt lúc đó. Product E1–E8, gồm E2-R interpretation, E4 independent demo replay, E7 và E8 được đo, là demo gates sau D09. #70 PASS sẽ chấp thuận contract cụ thể có thể kiểm thử, không claim các product checks đã PASS. Owner có thể yêu cầu thêm research evidence; chưa cung cấp thì vẫn chặn #70.

## 3. D07-R — đề xuất corpus đã quan sát

Provider arXiv, query kỹ thuật `cat:cs.SE AND submittedDate:[201901010000 TO 201906302359]`. Counting unit là distinct work; title và submission event được pin v1. Toàn bộ current-query result đã quan sát có 598 works, không phải sample chọn theo concept. Không loại records để cải thiện biểu đồ; nonmatches vẫn ở N. Acquisition bound là 2.000 works, page size 500, ascending submission order; current pages 500/98, v1 batches 100/100/100/100/100/98, reported_total=598. Freeze tập quan sát này, không query lại.

Retrieval: **10/10/2026, 11:27:47–11:28:24 UTC**; event bins: tháng 01–06/2019 UTC; upper event boundary `2019-06-30T23:59:59Z`. Retrieval time, v1 submission, update và public availability có nghĩa khác nhau. `available_at=null`; chưa có completeness của historical membership/category/vocabulary. Chín late-ID works vẫn thuộc population quan sát chia bin theo event và exposure register. Corpus đề xuất không đại diện toàn bộ software engineering hoặc nghiên cứu fuzzing.

Denominator đã đo: **91/79/97/103/122/106**. Bảy field đã audit có 0 missing/invalid trên 598; đây là syntactic field fitness, không phải semantic correctness. Mutation quan sát: 161 revisions, 55 title changes, bốn category-set changes. Current-category selection, removed/unindexed members, title-only aliases và submission/publication delay tạo bias. Pin version hạn chế title mutation khi replay, không loại current-index selection bias. Evidence: [audit](11_REAL_CORPUS_AUDIT_20261010.md), [historical screen](12_HISTORICAL_AVAILABILITY_SCREEN_20261010.md), [acquisition](../../../experiments/research_exit_20260927/runs/20261010-development-01/acquisition.json).

Retention/sharing: giữ metadata/raw Atom được phép và checksums; [provider screen đã kiểm tra](07_PROVIDER_AUDIT_RESULTS.md) ghi descriptive metadata CC0 và serial requests cách nhau ≥3 giây. Lượt này không acquisition. Quyền PDF/full text là riêng; không bundle paper PDFs hoặc suy ra metadata terms cho phép redistribute chúng. Mọi evidence retrieval sau này phải ghi riêng source/version, access và permitted retention.

Alternatives: provider mới thêm coverage/replay chưa đo mà không giải quyết nhu cầu đã nêu; historical-as-of reconstruction đầy đủ thiếu ledger/capture cần thiết; defer M1 nếu owner không chấp nhận giá trị mô tả giới hạn. Khuyến nghị corpus quan sát hiện có cho contract hẹp này. Đảo chiều nếu frozen input checks fail, denominator không reconcile được hoặc owner đòi historical completeness; historical capture hợp lệ mở một proposal nghiên cứu riêng, không tự đổi corpus này.

## 4. D08-R — đề xuất chỉ báo lexical mô tả

Rule `RE-20260927-01-documented-word-boundary-v1`, case-insensitive `\bfuzz(?:ing|er|ers)?\b` trên tiêu đề v1. Với eligible distinct works C_b: `N(b)=|C_b|`, `n(b)=Σ match(w)`, `p(b)=n(b)/N(b)` khi xác định được. Đề xuất hiển thị share là chỉ báo chính, **n và N bắt buộc đi kèm**. Count đơn lẻ là alternative đơn giản đáng cân nhắc; nó che khác biệt denominator, còn share vẫn chịu selection/alias drift. Cả hai không hỗ trợ nhãn tăng trưởng khoa học.

n đã đo **0/1/2/1/4/1**, tổng **9/598 = 1,5050%**, support chỉ 0–4/tháng. Bốn matches tháng 05 không chứng minh scientific growth. Toàn bộ values, raw refs, sensitivities, controls, prior art và correction history giữ ở [report 14](14_D08_DEVELOPMENT_EVALUATION_20261010.md); packet không đổi rule hoặc measurements.

Support policy: công bố n≥0 khi mọi field liên quan đã biết; share cần N≥1 và event/title fields hợp lệ. Missing/invalid title vẫn ở N, làm n/p null, cho phép báo bounds rõ ràng từ known matches. Missing/invalid event làm monthly denominators unresolved; N rỗng cho undefined share. Conflicting v1 rows phải fail closed; revisions không đóng góp lần nữa. Đây là điều kiện xác định phép tính, không phải threshold bảo đảm statistical support. **Vô hiệu hóa directional trend labels với mọi support value**; không đề xuất finite n threshold bảo đảm trend validity.

Sensitivity set giữ cố định: exact fuzzing, current title, v1 category subset, loại chín late IDs chỉ như perturbation, adjacent two-month ratio of sums và decoded-pattern equality diagnostic. Báo mọi kết quả, kể cả exact-fuzzing chỉ năm matches. Không đổi concept/window để làm biểu đồ đẹp. Đảo chiều khuyến nghị signal nếu reviewer hiểu sai, denominator invalid hoặc semantic checks sau này cho thấy cách dùng gây hiểu lầm; đề xuất thay đổi prospectively, không sửa evidence development này.

## 5. Reference workflow: simulation đã chạy và scientific pilot chưa chạy

**Đã thực hiện:** [simulation source](../../../experiments/research_exit_20260927/simulate_reference_workflow.py), [bảy tests](../../../experiments/research_exit_20260927/test_reference_workflow.py), [synthetic output](../../../experiments/research_exit_20260927/runs/20261010-amendment-01/simulated-workflow.json). SIMULATED_A/B/C xử lý **SYN-001…SYN-027**, không liên quan corpus thật. Kết quả thiết kế sẵn: 54 A/B judgments, 18 agreements, chín disagreements, chín C adjudications; final POSITIVE/NEGATIVE/UNCERTAIN là 9/9/9. Các tỷ lệ là fixture choices, không phải annotator agreement hoặc semantic accuracy quan sát được. Bảy workflow tests và tool suite 35 tests PASS. Chỉ hỗ trợ **synthetic workflow correctness**, không phải end-to-end product correctness hoặc independent scientific quality.

Checks giữ raw A/B labels, cho phép C giữ UNCERTAIN, yêu cầu evidence/rationale với nhãn xác định, reject missing adjudication, duplicate IDs, vai trò không simulated và real-paper IDs/URLs. Output không ghi đè file đã tồn tại. Real corpus works được annotate: **0**. [Manifest 27 works thật hiện có](../../../experiments/research_exit_20260927/runs/20261010-signal-01/reference-pilot-plan.json) vẫn PROPOSED/NOT EXECUTED, annotations null; không phải synthetic fixture này.

Independent pilot thật nếu sau này được yêu cầu/cho phép: hai nhà nghiên cứu thật do owner chỉ định và người phân xử thứ ba. Organizer-only selection giữ chín matches cộng 18 nonmatches (ba/tháng, SHA256 order với seed `D08-REF-20261010-01`), được chọn **sau** output exposure. First-pass dùng opaque IDs/random order và evidence v1 được phép, bỏ dates/arXiv IDs hiển thị, selection strata và signal metadata; tiêu đề vẫn lộ từ vựng, nên không thể blind rule hoàn hảo. Khóa A/B judgments trước khi mở verification links; links làm lộ dates, mọi blinding breach phải được ghi. Reviewers khai báo exposure trước đó, không được coi independent chỉ vì tên vai trò khác nhau.

Rubric: POSITIVE khi abstract/method evidence xác lập fuzzing là research subject/method có nội dung; NEGATIVE khi sufficient evidence xác lập chủ đề khác và chỉ dùng từ không liên quan/ngẫu nhiên; UNCERTAIN với ambiguous, inaccessible hoặc conflicting evidence. Ghi reviewer, source/version/section, rationale và evidence date. Không dùng regex, plot hoặc AI-generated labels làm reference. Giữ cả hai original judgments và rationale của C; unresolved cases vẫn uncertain/pending, không ép consensus hoặc negative.

Reporting khai báo trước cho pilot thật: toàn bộ 54 initial judgments, chín-match/18-nonmatch strata, label totals và uncertainty; raw agreement numerator/denominator gồm uncertain, cùng agreement giữa determinate pairs với denominator riêng; mọi disagreement/adjudication. TP/FP/FN/TN chỉ mô tả selected determinate records, báo stratum counts không weighted; không ước lượng population recall, monthly semantic prevalence hoặc trend accuracy. Chín matched titles và 18 sampled negatives không chứng minh complete semantic coverage. Lượt này không tạo independent labels hoặc các metrics đó.

## 6. Quality/support criteria đề xuất owner chấp thuận

| Tiêu chí đề xuất | Threshold / xử lý quyết định | Lý do / evidence hiện tại |
| --- | --- | --- |
| Deterministic arithmetic, replay, idempotency | 0 fixture/arithmetic mismatches; 0 semantic byte differences; 0 duplicate contributions | Logical correctness, không statistical accuracy; có development evidence |
| Lineage và field accounting | 100% eligible IDs/outputs hiển thị được liên kết; unknowns không tự thành negative hoặc bị loại | Traceability/denominator invariant; còn thiếu product navigation |
| Synthetic annotation workflow | 27 fictional records, 54 A/B judgments hợp lệ; mọi disagreement adjudicated hoặc pending rõ ràng; giữ raw judgments; cả bảy rejection/preservation tests PASS | Simulation đã PASS; 0 independent real judgments |
| Independent reviewer interpretation | 5/5: xác định n/N; giải thích share; phân biệt observed-2026 population với 2019 event; phân biệt lexical với semantic relevance; không suy diễn trend/as-of. Reviewer còn phải mở evidence và replay không sửa code | Prospective task rubric, NOT MEASURED. Sai câu cần fix/retest và khai báo exposure |
| Independent semantic/trend quality | NOT MEASURED; không precision/recall hoặc trend threshold nào accepted/được đề xuất như đã validated | Owner phải chấp thuận rõ boundary demo giới hạn này hoặc giữ yêu cầu và #70 NOT PASSED |
| Support/uncertainty | n≥0; share chỉ khi N≥1 và required fields đã biết; ngược lại null/bounds; không directional labels với mọi n | Báo sparse support trung thực; không bịa “adequate support” threshold |
| Bounded operation | ≤598 works; replay ≤60 giây; peak process memory ≤256 MiB; không live corpus request | Engineering budget PROPOSED; đo trên environment được ghi trước khi claim E8 |

Nếu sau này chọn pilot thật, completeness rule là accounting 100% raw judgments, mọi disagreement adjudicated hoặc unresolved rõ lý do; báo uncertainty, không xóa để đạt pass rate. Simulation **không biện minh được** minimum agreement hoặc precision target cho scientific quality. Chốt target và căn cứ trong prospective protocol được chấp thuận riêng trước untouched confirmatory reference/evaluation.

## 7. Exposure, immutable freeze và holdout sau này

Toàn bộ 598 development records/metadata, sáu counts/shares, sensitivities và chín late-ID anomalies đã exposure. Giữ original local declaration và metadata correction; correction sau signal exposure đầu tiên, không đổi rule/value. Đây không phải independent preregistration. Amendment và engineering budget cũng là proposal sau development output; freeze chỉ có hiệu lực prospective với replay không thay đổi và reviewer tasks mới.

Trước evaluation mới được chấp thuận, ghi owner/time/accepted packet hash, đúng input/config/code/runtime hashes, outputs, toàn bộ applicable criteria, case/control, sensitivities, personnel/exposure và budget trong immutable release manifest. Document hash phải định danh bytes được duyệt, không phải file sẽ sửa sau; ghi acceptance bên ngoài để tránh self-hash cycle. Version mới phải supersede rõ và dùng output directory mới. Không thay frozen artifacts hiện có.

Evidence pin tại source revision: normalized corpus SHA-256 `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1`; config `f4ed7d7bca9c9665a9cb03437c79306f282e15ebb5ad9520bf6126deff61f1f7`; measurements `214c103f82784665907f76925ea56763fd2e46644ce52ccf6950b08e807cc818`. [Corrected declaration](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json) liệt kê 14 frozen input hashes; [execution](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/execution.json) pin evaluator/runtime. Chúng định danh development evidence hiện có, không phải new freeze đã accepted.

Không query/read/write tháng 07–12/2019. ID-month khác event-month, nên calendar split không tự chứng nhận disjointness. Trước confirmatory acquisition được authorize riêng: predeclare population/query, event semantics, semantic reference, thresholds, vocabulary, personnel/exposure và budgets; reconcile exact work/version identity với toàn bộ 598 exposed works, selection 27 works thật và chín late-ID works; quarantine overlap; ghi source evidence đã từng được xem hay chưa. Nếu không xác lập untouched set được, gọi là development, không holdout. Packet không cho phép acquisition đó.

## 8. Alternatives, risks và phép thử tiếp theo hữu hạn

Khuyến nghị route mô tả giới hạn với E2-R/E3-R **để owner duyệt rõ**, vì đã có arithmetic/lineage evidence và hướng retrospective được chọn tránh claim as-of thiếu căn cứ. Giá trị là corpus comparison kiểm tra được và abstention có kỷ luật, không phải trend intelligence đã chứng minh. Alternatives thực chất: giữ independent semantic-quality acceptance và chờ người/reference criteria phù hợp; hoặc defer M1 ở NOT PASSED theo contract gốc. Historical-as-of là nghiên cứu tương lai được gate riêng, không tiếp tục tìm kiếm vô hạn trước mắt. Historical capture verified hoặc yêu cầu validated detection sẽ đảo chiều khuyến nghị route giới hạn.

Risks: sparse support, alias/selection bias; reviewer nhầm lexical với scientific prevalence; simulation bị coi là reference quality; contract sau exposure bị coi là preregistration; trễ 15/10 nếu gate/reviewer resources chưa có. Mitigations: claim labels chính xác, bắt buộc n/N, giữ uncertainty/exposure, E3 IDs riêng và owner choices rõ ràng. Không thêm infrastructure hoặc hạ criteria để bù. Sharing paper content cần kiểm tra quyền riêng.

**Một phép thử phân biệt tiếp theo, sau các gate áp dụng:** reviewer độc lập làm task năm câu, mở một match và một nonmatch evidence bundle, replay fixed demo độc lập trong budget đề xuất. Giữ answers, navigation failures, environment, timing/memory và semantic comparison. Phép thử xác định demo mô tả hẹp có thể hiểu/replay không; không xác lập scientific trend quality. Không có reviewer độc lập thì các tiêu chí này vẫn NOT MEASURED. D09/product work chờ Research Exit rõ ràng và acceptance D09 sau đó.

Critical path: owner review exact amendment + D07/D08/criteria → accepted prospective freeze + disposition #70 rõ ràng → D09 → vertical slice nhỏ nhất → independent replay/task + E1/E3-R/E5/E6/E8 → demo review trước 15/10. WIP vẫn #64 execution, #70 là gate; không tạo execution issue mới.

## 9. Owner acceptance/rejection record — chưa điền

Mỗi dòng ghi ACCEPT / REJECT / REVISE, owner, UTC date và immutable packet/version/hash. Chấp thuận một phần không chấp thuận các dòng khác.

| Item | Quyết định chính xác còn chờ owner | Disposition hiện tại |
| --- | --- | --- |
| A1 | Estimand/claims tại §1 và tác động M1/D05 tại §2 | PROPOSED |
| A2 | Thay nghĩa vụ demo E2/E3 gốc bằng E2-R/E3-R, giữ rõ E3 gốc NOT PASSED | PROPOSED |
| A3 | Chọn limited descriptive acceptance với independent scientific quality NOT MEASURED, **hoặc** giữ independent-reference criterion và chờ pilot thật | PROPOSED; không implicit waiver |
| D07 | Observed population, timestamps, versions, inclusion/denominator, bias, sharing boundary chính xác tại §3 | PROPOSED |
| D08 | Rule/formula chính xác, không directional labels, null/support, sensitivities, phân biệt simulated/real reference và criteria tại §4–§6 | PROPOSED |
| F1 | Prospective freeze manifest, exposure register, reviewer/budget protocol tại §7; không holdout access hiện tại | PROPOSED; chưa accepted freeze |
| G70 | Chỉ ghi RESEARCH-READY PASSED khi mọi research criteria owner chọn đã có evidence và D07/D08 được accepted rõ; nếu chưa, NOT PASSED kèm hạng mục thiếu | NOT PASSED |
| D09 / product gates | Architecture/preimplementation review riêng ở bước sau | PROPOSED; không quyết định ở đây |

GO hiện tại: review proposal cụ thể này và kiểm tra synthetic checks. Direction selection hoặc workflow PASS riêng lẻ không cho phép dependent implementation. Xem [packet English](../../english/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md).
