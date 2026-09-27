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
| 19–20/09 — Research entry | Biến RQ thành kế hoạch khảo sát hữu hạn | Research checklist, research protocol, source-audit plan, case-selection protocol, signal-candidate protocol | [#68](https://github.com/Dyu20705/sites/issues/68) có thẩm quyền ghi **RESEARCH ENTRY PASSED** sau khi documentation merge được chấp thuận |
| 21–27/09 — Research Gate | Chọn corpus và chỉ báo dựa trên bằng chứng | D07/D08 decision packets, literature/evidence ledger, measured source audit, case/control + experiment-freeze proposal | [#70](https://github.com/Dyu20705/sites/issues/70) có thẩm quyền chấp thuận D07/D08 và ghi **RESEARCH-READY PASSED** trước holdout evaluation hoặc implementation |
| 28/09–01/10 — Preimplementation | Thiết kế phương án nhỏ nhất đáp ứng evaluation | Contract tối thiểu, fixtures, expected values, runtime budget, D09 | Các lựa chọn cần cho code đã được chấp thuận; E1–E8 khả thi |
| 02–07/10 — Feature | Xây một luồng end-to-end | Acquisition → evidence bundle/query/dashboard + tests | Luồng thật chạy được; các kiểm tra correctness/trace/replay cốt lõi đạt |
| 08–13/10 — Evaluation/Demo | Kiểm tra case, control và usability | E1–E8 reports, limitation/disagreement log, reviewer replay | Đạt tiêu chí đã freeze; không tuning hậu nghiệm để che failure |
| 14–16/10 — Packaging | Làm demo có thể chạy lại | Replay guide, shareable data, environment record, demo package | Reviewer khác replay thành công |
| 17/10 — Final | Review M1 và trả lời RQ chính | Gate checklist, demo, research result, current state cập nhật | Contract và E1–E8 được xác nhận trong phạm vi M1 |

## Hàng đợi nghiên cứu

Research Entry đã đạt qua #68 ngày 23/09 sau khi PR #74 merge. Hai issues dưới đây là hàng đợi nghiên cứu active; #36–#61 tiếp tục là tư liệu tham khảo.

| Package | Issue | Deliverables và ranh giới hoàn thành |
| --- | --- | --- |
| A — Bằng chứng và chỉ báo ứng viên | [#64](https://github.com/Dyu20705/sites/issues/64) — OPEN, ACTIVE | R1/R2/R6 ledger, định nghĩa và counterevidence, so sánh chỉ báo, case/control và freeze proposal, limitations, đề xuất D08 có căn cứ hoặc báo rõ thiếu bằng chứng |
| B — Khả thi nguồn và corpus | [#65](https://github.com/Dyu20705/sites/issues/65) — OPEN, ACTIVE | R3/R4/R7 provider screening, sample/query/snapshot record giới hạn, field mapping, missingness/coverage, temporal và access/replay evidence, đề xuất D07 có căn cứ hoặc báo rõ thiếu bằng chứng |

[Quyết định #68 có thẩm quyền](https://github.com/Dyu20705/sites/issues/68#issuecomment-5795799412) xác lập WIP thực thi đúng #64 + #65. [Gói bằng chứng 27/09](../research/08_D07_D08_EXIT_PACKET.md) ghi thiếu bằng chứng: acquisition bị chặn, chưa freeze được experiment. #70 giữ NOT PASSED. #69 chỉ tracking; không tạo execution item thứ ba.

**Mục tiêu tăng tốc được yêu cầu ngày 27/09:** hoàn tất Research Exit cùng ngày nếu đủ evidence; sau đó D09 ngày 28/09, build 29/09–02/10, evaluation/demo đầu 03–05/10, sửa lỗi/replay/packaging 06–16/10. Đây là lịch có điều kiện, không phải bằng chứng hoàn thành. Deadline 17/10 và E1–E8 giữ nguyên. Giữ phase allocation ban đầu phía trên để đối chiếu; lịch tăng tốc chưa mở khóa công việc phụ thuộc.

A gửi trước field requirements từ [signal candidates](../research/04_SIGNAL_CANDIDATES.md); B trả field khả thi, giới hạn denominator và time semantics theo [audit plan](../research/02_SOURCE_AUDIT_PLAN.md). A không hoàn tất D08 khi chưa có findings từ B. R5 lineage bắt buộc trong cả hai packages. R8 là walkthrough khi có prototype cùng misunderstanding log; chấp thuận D06 chưa kiểm chứng R8 và đây không phải active item thứ ba.

Theo [research protocol](../research/00_RESEARCH_PROTOCOL.md) và [entry checklist](../research/05_RESEARCH_ENTRY_CHECKLIST.md). Mỗi issue hoàn thành khi bằng chứng hoặc negative findings có thể review, limitations và next action rõ ràng, đề xuất sẵn sàng để chủ dự án xem xét. Đóng khảo sát không accept D07/D08 hoặc làm research-ready đạt. Gate đó còn cần empirical artifacts, freeze proposal và chủ dự án chấp thuận D07/D08 rõ ràng thông qua #70. D09 là quyết định sau đó.

## Nếu trượt gate

Khi một gate fail:

1. dừng công việc phụ thuộc gate đó;
2. vẫn có thể tiếp tục documentation hoặc analysis không phụ thuộc;
3. ưu tiên bỏ chỉ báo thứ hai, giảm domain/window/corpus hoặc hoãn hosting;
4. ghi rõ ảnh hưởng của việc giảm scope tới phạm vi kết luận và bias;
5. không tự bỏ các yêu cầu về temporal isolation hoặc traceability chỉ để cứu demo.

Nếu slice tối thiểu vẫn không khả thi, kết luận phải là **M1 NOT PASSED** kèm bằng chứng. Deadline không được “cứu” bằng cách đổi nghĩa của product-ready.
