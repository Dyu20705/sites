# 08 — Kế hoạch Month 1 theo điểm kiểm soát

**Deadline:** 17/10/2026.  
**WIP limit:** tối đa 2 work item đang thực hiện.

~~~text
define-ready → Research Entry → research phase → research-ready → preimplementation-ready
→ feature-ready → product-ready v1
~~~

Không giai đoạn nào được đánh dấu hoàn thành chỉ vì đã đến ngày. Mỗi trạng thái phải có artifact và bằng chứng tương ứng.

## Kế hoạch

| Thời gian | Mục tiêu | Artifact chính | Điều kiện qua gate |
| --- | --- | --- | --- |
| 17–18/09 — Define | Dọn repo và chốt bài toán M1 | Charter, M1 definition, decision log, current state | Không còn BLOCKER/MAJOR trong M0; chấp thuận user/task và các nguyên tắc cần thiết |
| 19–20/09 — Research entry | Biến RQ thành kế hoạch khảo sát hữu hạn | Research checklist, source-audit plan, candidate case, selection criteria | Reviewer xác nhận câu hỏi, bằng chứng cần thu và phạm vi research |
| 21–27/09 — Research Gate | Chọn corpus và chỉ báo dựa trên bằng chứng | Reading notes, sample audit, coverage/temporal audit, signal comparison | Chốt domain/provider/window, đơn vị, công thức, cutoff, minimum support và quality threshold trước holdout |
| 28/09–01/10 — Preimplementation | Thiết kế phương án nhỏ nhất đáp ứng evaluation | Contract tối thiểu, fixtures, expected values, runtime budget, D09 | Các lựa chọn cần cho code đã được chấp thuận; E1–E8 khả thi |
| 02–07/10 — Feature | Xây một luồng end-to-end | Acquisition → evidence bundle/query/dashboard + tests | Luồng thật chạy được; các kiểm tra correctness/trace/replay cốt lõi đạt |
| 08–13/10 — Evaluation/Demo | Kiểm tra case, control và usability | E1–E8 reports, limitation/disagreement log, reviewer replay | Đạt tiêu chí đã freeze; không tuning hậu nghiệm để che failure |
| 14–16/10 — Packaging | Làm demo có thể chạy lại | Replay guide, shareable data, environment record, demo package | Reviewer khác replay thành công |
| 17/10 — Final | Review M1 và trả lời RQ chính | Gate checklist, demo, research result, current state cập nhật | Contract và E1–E8 được xác nhận trong phạm vi M1 |

## Hàng đợi nghiên cứu

Chuẩn bị entry là một work item. Hoàn tất review của nó trước khi kích hoạt research execution. Hai issues mới dưới đây là toàn bộ hàng đợi ban đầu; #36–#61 tiếp tục là tư liệu tham khảo.

| Package | Issue | Deliverables và ranh giới hoàn thành |
| --- | --- | --- |
| A — Bằng chứng và chỉ báo ứng viên | Chờ đăng | R1/R2/R6 ledger, định nghĩa và counterevidence, so sánh chỉ báo, case/control và freeze proposal, limitations, đề xuất D08 có căn cứ hoặc báo rõ thiếu bằng chứng |
| B — Khả thi nguồn và corpus | Chờ đăng | R3/R4/R7 provider screening, sample/query/snapshot record giới hạn, field mapping, missingness/coverage, temporal và access/replay evidence, đề xuất D07 có căn cứ hoặc báo rõ thiếu bằng chứng |

A gửi trước field requirements từ [signal candidates](../research/04_SIGNAL_CANDIDATES.md); B trả field khả thi, giới hạn denominator và time semantics theo [audit plan](../research/02_SOURCE_AUDIT_PLAN.md). A không hoàn tất D08 khi chưa có findings từ B. R5 lineage bắt buộc trong cả hai packages. R8 là walkthrough khi có prototype cùng misunderstanding log; chấp thuận D06 chưa kiểm chứng R8 và đây không phải active item thứ ba.

Theo [research protocol](../research/00_RESEARCH_PROTOCOL.md) và [entry checklist](../research/05_RESEARCH_ENTRY_CHECKLIST.md). Mỗi issue hoàn thành khi bằng chứng hoặc negative findings có thể review, limitations và next action rõ ràng, đề xuất sẵn sàng để chủ dự án xem xét. Đóng khảo sát không accept D07/D08 hoặc làm research-ready đạt. Gate đó còn cần empirical artifacts, freeze proposal và chủ dự án chấp thuận D07/D08 rõ ràng. D09 là quyết định sau đó.

## Nếu trượt gate

Khi một gate fail:

1. dừng công việc phụ thuộc gate đó;
2. vẫn có thể tiếp tục documentation hoặc analysis không phụ thuộc;
3. ưu tiên bỏ chỉ báo thứ hai, giảm domain/window/corpus hoặc hoãn hosting;
4. ghi rõ ảnh hưởng của việc giảm scope tới phạm vi kết luận và bias;
5. không tự bỏ các yêu cầu về temporal isolation hoặc traceability chỉ để cứu demo.

Nếu slice tối thiểu vẫn không khả thi, kết luận phải là **M1 NOT PASSED** kèm bằng chứng. Deadline không được “cứu” bằng cách đổi nghĩa của product-ready.
