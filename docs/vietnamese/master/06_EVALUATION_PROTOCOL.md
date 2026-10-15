# 06 — Quy trình đánh giá

**Thẩm quyền hiện tại — 12/10/2026:** [owner approval](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874) chấp thuận A1/A2/A3/D07/D08/F1 của [M1-R-20261010-v1](../research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md). D05/D06 giữ ACCEPTED; chỉ sửa ứng dụng temporal M1/D05 và nghĩa vụ demo E2/E3 được nêu rõ. Output accepted là lexical n/N/share retrospective của corpus frozen 598 công trình; không có trend labels hoặc historical-as-of claim. E3 gốc giữ **NOT PASSED**; independent scientific quality **NOT MEASURED**.

[Research Exit đã kiểm chứng](../research/17_RESEARCH_EXIT_20261012.md): **RESEARCH-READY PASSED — RETROSPECTIVE DESCRIPTIVE SCOPE ONLY**. [D09-M1-20261012-v1](https://github.com/Dyu20705/sites/issues/71#issuecomment-6123995295) đã được **ACCEPTED** riêng và PREIMPLEMENTATION-READY đã đạt; #72 là implementation candidate đang hoạt động, #73 chưa đạt. Deadline: **15/10/2026**.

**Gate allocation đã accepted:** G70 gồm quyết định owner, F1, corpus/số học/lineage frozen, synthetic workflow, controls và research E2-R/E3-R. Product E1/E3-R/E5/E6 integration, E2-R interpretation, E4 independent replay, E7 task năm/năm câu đúng và navigation, E8 đo thực tế vẫn là nghĩa vụ demo sau D09. Budget: ≤598 công trình, ≤60 giây, ≤256 MiB peak process memory, không live corpus request. Phải ghi identity/exposure/runtime reviewer trước task mới; chưa có reviewer result hoặc E8 đo thực tế.

## Baseline lịch sử — giữ để đối chiếu

Phần dưới ghi quyết định/kế hoạch trước đây. Exact amendment đã accepted và mục hiện tại phía trên thay các scope, trạng thái, lịch thực hiện mâu thuẫn; nghĩa vụ được giữ lại vẫn áp dụng.

**Amendment đang chờ, 10/10:** owner chọn hướng retrospective-only và cho phép chuẩn bị [M1-R-20261010-v1](../research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md). E2-R/E3-R và quality/support/budget choices vẫn PROPOSED; không tự thay matrix gốc phía dưới. SIMULATED workflow checks không đáp ứng independent scientific-reference quality. E3 gốc vẫn NOT PASSED; accepted retrospective contract cũng không biến nó thành E3 gốc PASS.

**Nguyên tắc D05 ACCEPTED; lựa chọn đánh giá D08 PROPOSED.** Đây là kế hoạch kiểm chứng, chưa phải kết quả test. E1–E8 vẫn bắt buộc; công thức, reference labels, ngưỡng và sensitivity settings còn cần D08 acceptance. Gọi phân tích là retrospective không làm E3 hoặc M1 đạt.

Protocol phải được chốt **trước khi triển khai và trước khi xem kết quả holdout**.

## 1. Điều M1 cần kiểm tra

M1 chỉ kiểm tra khả năng mô tả thay đổi trong corpus đã định nghĩa.

M1 **không** kiểm tra:

- dự báo tương lai;
- công nghệ nào tốt hơn;
- mức độ thành công ngoài thị trường;
- khả năng scale ở production.

Kết quả đánh giá phải tách bốn vấn đề:

1. phép tính có đúng không;
2. bằng chứng có đầy đủ và phù hợp không;
3. kết quả có giải thích được không;
4. detection có phù hợp với trường hợp đánh giá đã xác định không.

Demo chạy được không đồng nghĩa detection có giá trị.

## 2. Thiết kế đánh giá

1. Chốt user task, domain/query, corpus/window, đơn vị đếm, chỉ báo, ngưỡng và minimum support; freeze trước holdout.
2. Tạo synthetic examples có kết quả mong đợi được tính độc lập: tăng, giảm, không đổi, zero/missing, duplicate/revision và future-dated observation.
3. Chọn một trường hợp lịch sử và một control case; ghi tiêu chí chọn trước khi xem system output.
4. Với **as-of evaluation**, mọi field dùng tại cutoff T phải có bằng chứng cho thấy field đó đã available không muộn hơn T.
5. Nếu không có availability evidence, chỉ được gọi là **retrospective case analysis**; không gọi là backtest.
6. Chạy sensitivity analysis khi thay đổi window/threshold trong phạm vi hợp lý và khi loại record thiếu field; giữ cả negative results.
7. Replay phải dùng frozen input, không phụ thuộc live API.

## 3. Ma trận chấp nhận

| ID | Kiểm tra | Bằng chứng cần lưu | Điều kiện đạt |
| --- | --- | --- | --- |
| E1 | Deterministic correctness | Fixture nhỏ, expected value độc lập, actual value và diff | 100% case đã định nghĩa đúng; tolerance số thực chốt trước |
| E2 | Historical case + explainability | Case protocol, control, components, annotation, disagreement, sensitivity | Có ≥1 case và ≥1 control; reviewer giải thích được mọi label; quality threshold được chốt trước |
| E3 | Temporal isolation | Availability audit, cutoff/config/vocabulary record, injected future records | Không có input trái cutoff; future records không làm đổi output trước T; thiếu availability evidence ⇒ NOT PASSED |
| E4 | Reproducibility | Snapshot identity, config, code version, metric definition, environment, output | Hai lần chạy độc lập cho cùng semantic output |
| E5 | Traceability | Full lineage + evidence bundle | 100% assessment demo truy được tới signal và toàn bộ observations đóng góp |
| E6 | Idempotency | Replay cùng input và so sánh count/signal | Không có đóng góp bị nhân đôi; semantic output không đổi |
| E7 | Usability | Task-based walkthrough | Reviewer chọn concept/window, xem kết quả, hiểu chỉ báo và mở bằng chứng mà không sửa code |
| E8 | Bounded operation | Corpus size, coverage, missingness, runtime, resource usage nếu đo được | Đạt budget được chốt trước; không suy diễn scalability |

## 4. Lưu ý về E2

Hoàn thành một report **không đồng nghĩa** detection quality đạt yêu cầu.

Research Gate phải chốt trước:

- metric hoặc rubric;
- cách tạo reference label;
- limitation;
- pass/fail threshold.

Precision/recall chỉ có ý nghĩa nếu reference label đủ độc lập và phù hợp. Không tự gọi annotation là “trend truth”.

## 5. Điều kiện demo được chấp nhận

Một reviewer khác người viết phải:

- chạy lại từ snapshot được phép sử dụng;
- kiểm tra ít nhất một evidence bundle;
- hoàn thành E7;
- ghi lại environment và kết quả.

M1 đạt khi:

- các gate cần thiết đã được chấp thuận;
- các tiêu chí E1–E8 áp dụng đều đạt;
- có demo trước 17/10/2026;
- không còn BLOCKER/MAJOR về correctness, temporal semantics hoặc traceability.

Nếu dữ liệu không đủ hoặc chỉ báo không qua tiêu chí đã chốt, phải ghi **M1 NOT PASSED / scope review required**. Không thay threshold sau đánh giá để cứu demo.
