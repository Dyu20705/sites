# 17 — Research Exit đã chấp thuận và bàn giao kỹ thuật

**12/10/2026: RESEARCH-READY PASSED — RETROSPECTIVE DESCRIPTIVE SCOPE ONLY.** Đây là kết luận đã kiểm chứng theo quyền chấp thuận có điều kiện của owner, ghi tại [G70](https://github.com/Dyu20705/sites/issues/70). D09 vẫn PROPOSED; bước tiếp là đề xuất thiết kế ở #71, #72/#73 chưa đạt. Deadline demo: **15/10/2026**.

[Quyết định owner](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874), Dyu20705 lúc `2026-10-12T07:10:14Z`, chấp thuận A1/A2/A3/D07/D08 và hợp đồng F1 của **M1-R-20261010-v1**. [Packet](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) giữ nguyên chữ PROPOSED và byte lịch sử; acceptance được ghi bên ngoài. SHA-256 EN `da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122`; VI `164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0`. Source commit nghiên cứu: `97bf499718c13166667a8e5da09b201065d9e117`; commit bàn giao được ghim ngoài tài liệu tại G70 để tránh tự tham chiếu.

[Manifest F1-M1-R-20261012-v1 mới](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json) có SHA-256 **`bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`**. Manifest ghi 122 artifact chính xác, identity source/code/config/output, inventory runtime, tiêu chí accepted, ngữ nghĩa thời gian và mẫu số, toàn bộ 598 version ID đã xem, 27 pilot ID chưa gán nhãn, chín late-ID, nhiệm vụ reviewer tương lai và lệnh cấm holdout. Hash development cũ vẫn là bằng chứng development; freeze mới chỉ áp dụng prospectively cho replay/task sau exposure, không phải preregistration độc lập. Source commit ghim artifact cũ; manifest ghim tệp hỗ trợ freeze mới; commit bàn giao ghim toàn bộ gói.

| Tiêu chí research đã chấp thuận | Kết quả / bằng chứng kiểm chứng |
| --- | --- |
| Hợp đồng owner chọn | A1/A2/A3/D07/D08/F1 được chấp thuận rõ; chọn route mô tả giới hạn, không giữ yêu cầu independent scientific reference tại G70 |
| Corpus, field/time và mẫu số | 598 công trình v1 riêng biệt; 100% lineage raw current/v1; bảy field audit đều hợp lệ; chọn current cs.SE, chia tháng theo v1 event UTC tháng 1–6/2019; availability chưa biết |
| Số học và replay | n=0/1/2/1/4/1, N=91/79/97/103/122/106; tổng 9/598; 13 output mới khớp byte với kết quả frozen cũ |
| Phần research E2-R | Case fuzzing cố định, control share không đổi, mười controlled scenarios, năm sensitivity variants và ratio-of-sums hai tháng kề nhau tái lập; không suy ra scientific efficacy |
| Phần research E3-R | Đúng population/version/event/window/config; fixture cutoff/future-event và identity đạt; E3 lịch sử gốc **NOT PASSED** |
| Simulation / pilot thật | SYN-001…027: 54 judgments, 18 agreements, 9 adjudications, nhãn cuối 9/9/9; cưỡng chế fictional roles/IDs; real annotations=0 |
| Giới hạn / abstention | Title unknown ở lại N, n/share null và giữ bounds; N rỗng cho share null; event không hợp lệ làm mẫu số unresolved; không có directional labels ở mọi support |
| F1 | 122 hash khớp artifact; tệp cũ khớp Git blob tại source commit chính xác; runtime inventory tác giả khớp; kiểm tra thư mục mới + tiến trình riêng PASS |
| Regression / bảo toàn source | 56 unit tests PASS (50 cũ + sáu freeze regressions); bao gồm và giữ nguyên 112 artifact đã frozen; không live acquisition hoặc exposure holdout mới |

Bằng chứng: [execution mới](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/execution.json), [kiểm tra integrity trong thư mục sạch](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/clean-freeze-verification.json), [đếm lại XML bằng cách độc lập](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/independent-verification.json), [regression/replay theo trạng thái cũ](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/baseline-regressions.json). “Cách độc lập” là implementation XML/token riêng trên cùng máy tác giả, không phải người hoặc máy khác. Hai status validator cũ cố ý đòi PROPOSED, đã PASS trên tài liệu chưa cập nhật acceptance trước reconciliation; giữ chúng như lịch sử. [Accepted-state checks](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/accepted-state-validation.json) kiểm tra riêng trạng thái quyết định canonical mới.

Runtime inventory ghi Python 3.14.7, hash standard-library/native files và root binaries đã cài. Đây không phải Windows image hermetic: system DLLs và caches nằm ngoài inventory. Không tuyên bố có kết quả runtime, memory hoặc product task của reviewer độc lập. Budget offline ≤60 giây/≤256 MiB/≤598 công trình là prospective; phải ghi identity, exposure và môi trường reviewer trước task sau này.

## Reconciliation investigation #64

Decision packet giới hạn và bàn giao insufficient-evidence đã hoàn thành. #64 giữ mở cho administrative closure, không còn research execution active. Giữ wording checklist gốc và negative evidence; không bulk-close hay đánh dấu ngược phần nghiên cứu còn thiếu thành hoàn thành.

| Yêu cầu lịch sử | Kết luận sau acceptance |
| --- | --- |
| Exact query/service/date của literature search execution | INCOMPLETE; không dựng lại metadata chưa biết; không có claim systematic review hay novelty |
| Chọn historical case/control độc lập trước output | INCOMPLETE; exposure không cho phép claim đó. Demo thay bằng case fuzzing đã exposed và synthetic control cố định; không coi yêu cầu cũ đã đạt |
| Full pre-holdout confirmatory freeze | INCOMPLETE cho scientific confirmation; F1 thay bằng freeze replay development đã exposed và reviewer task prospective. Tháng 7–12 vẫn bị cấm |
| Scientific quality/support threshold và independent reference | NOT MEASURED / không có scientific threshold đủ cơ sở. A3 chọn route mô tả giới hạn; definability/null policy được accepted, không phải bằng chứng chất lượng khoa học |
| Điều khoản kiểm tra confounders | Đã chạy computational controls và development sensitivities; coverage/history của provider và tác động confounder khoa học thật chưa đo |
| Điều khoản reference uncertainty | Có protocol và SYN preservation checks; 27 pilot thật vẫn null judgments; chưa làm thí nghiệm bất đồng giữa người |

Các giới hạn này đáp ứng outcome insufficient-evidence có thể review và gate allocation hẹp đã accepted. Acceptance sửa nghĩa vụ demo, không biến negative findings thành bằng chứng khoa học tích cực. Gap search-provenance ở #69 vẫn mở.

## Quyền kỹ thuật và điều kiện mở lại

**Được làm ngay:** chuẩn bị đề xuất D09 nhỏ nhất ở #71. **Chỉ triển khai sau D09 acceptance riêng:** giữ chính xác population frozen, source refs, title rule, mẫu số, time semantics, null behavior, mọi sensitivity, claim limits và replay identity. Import projection mới phải kiểm tra nghiêm, từ chối current-category membership unknown; lỗi missing-category của helper nghiên cứu chỉ được cô lập nhờ corpus đóng này có field đầy đủ, không được âm thầm tổng quát hóa.

Product E1/E3-R/E5/E6 integration, E2-R interpretation, E4 reviewer replay độc lập, E7 task năm câu/navigation và E8 đo thực tế vẫn pending sau D09. Independent scientific quality **NOT MEASURED**; E3 gốc **NOT PASSED**. Chưa có product display, human validation, as-of completeness, validated trends, precision/recall hay suy rộng population. Bảy checkbox independent demo đều chưa đạt.

Mở lại hoặc tạo version mới khi hash/identity xung đột, mẫu số không reconcile được, thay corpus/rule/window/runtime, reviewer hiểu sai, hoặc cần historical completeness/scientific detection quality. Không sửa evidence cũ hay đổi exposed data thành holdout. Không cho phép acquisition tháng 7–12, merge, release hoặc deployment trong task này.

[Bản tiếng Anh](../../english/research/17_RESEARCH_EXIT_20261012.md).
