# 08 — Kế hoạch Month 1 theo điểm kiểm soát

**Deadline:** 17/10/2026.  
**WIP limit:** tối đa 2 work item đang thực hiện.

~~~text
define-ready → research-ready → preimplementation-ready
→ feature-ready → product-ready v1
~~~

Không giai đoạn nào được đánh dấu hoàn thành chỉ vì đã đến ngày. Mỗi trạng thái phải có artifact và evidence tương ứng.

## Kế hoạch

| Thời gian | Mục tiêu | Artifact chính | Điều kiện qua gate |
| --- | --- | --- | --- |
| 17–18/09 — Define | Dọn repo và chốt bài toán M1 | Charter, M1 definition, decision log, current state | Không còn BLOCKER/MAJOR trong M0; chấp thuận user/task và các nguyên tắc cần thiết |
| 19–20/09 — Research entry | Biến RQ thành kế hoạch khảo sát hữu hạn | Research checklist, source-audit plan, candidate case, selection criteria | Reviewer xác nhận câu hỏi, evidence cần thu và phạm vi research |
| 21–27/09 — Research Gate | Chọn corpus và chỉ báo bằng evidence | Reading notes, sample audit, coverage/temporal audit, signal comparison | Chốt domain/provider/window, unit, formula, cutoff, minimum support và quality threshold trước holdout |
| 28/09–01/10 — Preimplementation | Thiết kế phương án nhỏ nhất đáp ứng evaluation | Contracts tối thiểu, fixtures, expected values, runtime budget, D09 | Các lựa chọn cần cho code đã được chấp thuận; E1–E8 khả thi |
| 02–07/10 — Feature | Xây một luồng end-to-end | Acquisition → evidence bundle/query/dashboard + tests | Luồng thật chạy được; correctness/trace/replay cốt lõi đạt |
| 08–13/10 — Evaluation/Demo | Kiểm tra case, control và usability | E1–E8 reports, limitation/disagreement log, reviewer replay | Đạt tiêu chí đã freeze; không tuning hậu nghiệm để che failure |
| 14–16/10 — Packaging | Làm demo có thể chạy lại | Replay guide, shareable data, environment record, demo package | Reviewer khác replay thành công |
| 17/10 — Final | Review M1 và trả lời RQ chính | Gate checklist, demo, research result, current state cập nhật | Contract và E1–E8 được xác nhận trong phạm vi M1 |

## Nếu trượt gate

Khi một gate fail:

1. dừng công việc phụ thuộc gate đó;
2. vẫn có thể tiếp tục documentation hoặc analysis không phụ thuộc;
3. ưu tiên bỏ chỉ báo thứ hai, giảm domain/window/corpus hoặc hoãn hosting;
4. ghi rõ ảnh hưởng của việc giảm scope tới claim và bias;
5. không tự bỏ các yêu cầu về temporal isolation hoặc traceability chỉ để cứu demo.

Nếu slice tối thiểu vẫn không khả thi, kết luận phải là **M1 NOT PASSED** kèm evidence. Deadline không được “cứu” bằng cách đổi nghĩa của product-ready.
