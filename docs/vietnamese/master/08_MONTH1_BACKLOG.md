# 08 — Month-1 Backlog theo gate

**PROPOSED execution plan**, deadline **17/10/2026** và hướng detection đã được chấp thuận ở D03. Đây là backlog tài liệu M1 đang review, không phải GitHub issue graph đã được kích hoạt. WIP ≤ 2: tối đa hai work items thực sự đang làm, không tính các stage tương lai là đang active.

```text
define-ready → research-ready → preimplementation-ready → feature-ready → product-ready v1
```

Không stage nào được đánh dấu hoàn thành chỉ vì đến ngày. Chủ dự án chấp thuận user/scope/stack; reviewer kiểm tra evidence; Control Tower giữ merge gate PR. Trạng thái gate hiện tại nằm ở [Current State](09_CURRENT_STATE.md).

| Ngày 2026 / gate | Objective | Artifacts cần có | Exit gate | Blocker | Explicitly deferred |
| --- | --- | --- | --- | --- | --- |
| 17–18/09 — Define Gate, define-ready | Dọn repo; định nghĩa problem và hợp đồng M1 | Charter, contract, decision log, verified current state | M0 không còn BLOCKER/MAJOR; chủ dự án duyệt primary user/task và hướng scope D05/D06; đề xuất còn lại có owner/gate | User/task chưa được xác nhận | Implementation và lựa chọn stack |
| 19–20/09 — Research entry, research-ready | Biến RQs thành khảo sát có thể trả lời | Research checklist, source audit plan, candidate case, tiêu chí lựa chọn | Reviewer xác nhận câu hỏi, evidence cần lấy, protocol và bounded research scope | Không tiếp cận được sample hoặc thiếu quyền dùng dữ liệu | Survey toàn bộ literature và nhiều nguồn |
| 21–27/09 — Research Gate | Chọn signal/corpus trên evidence | Reading notes, sample/coverage/temporal audit, case rubric, signal comparison; decisions D07/D08 | Chốt domain/provider/window, đơn vị đếm, formula, cutoff rules, minimum support và quality threshold trước holdout; trả lời hoặc bác bỏ R1–R7 đủ cho slice | Không có temporal evidence, field cần thiết hoặc plausible signal | Signal thứ hai nếu không có giá trị đo được |
| 28/09–01/10 — Preimplementation Gate, preimplementation-ready | Thiết kế nhỏ nhất đáp ứng evaluation | Accepted minimal contracts, test fixtures/expected values, runtime budget, design decisions D09 | Human acceptance cho lựa chọn cần triển khai; E1–E8 khả thi; chưa dùng holdout để tuning | Architecture/data semantics chưa rõ hoặc scope vượt thời gian | Full schema, global resolution, network API riêng nếu chưa cần |
| 02–07/10 — Feature Gate, feature-ready | Implement một luồng xuyên hệ thống | Acquisition tới evidence bundle/query/dashboard; tests và frozen sample | Luồng thật chạy được; correctness/trace/replay checks cốt lõi pass; không claim product-ready từ demo happy path | Input/contract thay đổi hoặc tests fail | Multi-source và feature mới |
| 08–13/10 — Evaluation/Demo Gate | Kiểm tra historical case, controls và usability | E1–E8 reports, disagreement/limitation log, reviewer replay | Criteria đã chốt được đáp ứng; không có BLOCKER/MAJOR correctness/temporal/evidence | E3 thiếu availability hoặc E2 không đạt quality threshold | Tuning hậu nghiệm để che failure |
| 14–16/10 — Packaging Gate | Làm demo tái lập được trên môi trường đã chọn | Hướng dẫn replay, dữ liệu được phép chia sẻ, environment record, demo package; docs/log hoàn thiện 16/10 | Reviewer khác replay thành công, lỗi và giới hạn được ghi; hosting chỉ nếu D09 chấp thuận và cần cho task | Demo phụ thuộc môi trường tác giả/live API không ổn định | Public deployment mặc định, production operation |
| 17/10 — Final Gate, product-ready v1 trong phạm vi M1 | Review demo và trả lời primary RQ bằng evidence | Gate checklist, demo, research result, current state cập nhật | Chủ dự án/reviewer xác nhận contract và E1–E8; mọi scope change đã được duyệt | Criterion áp dụng chưa pass hoặc claim vượt evidence | Mở rộng capability chain |

So với lịch draft, design được timebox tới 01/10 để implementation có 02–07/10 thay vì ba ngày. “Deploy” 14–16/10 chuyển thành packaging/replay, không mặc định public hosting. Đây là đề xuất cần duyệt, không thay deadline và không khẳng định đã hoàn thành setup.

## Quy tắc khi trượt gate

Dừng phần việc phụ thuộc gate bị fail; tiếp tục documentation/analysis không phụ thuộc. Đề xuất bỏ signal thứ hai, giảm domain/window/corpus hoặc hoãn hosting, kèm thay đổi claim và đánh giá bias. Không tự bỏ E3/E5 để cứu demo. Nếu scope tối thiểu vẫn không khả thi, báo M1 NOT PASSED với evidence trước final gate; không dời deadline hoặc gọi negative result là demo thành công.
