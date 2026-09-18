# 01 — Scope and Non-goals

[M1 contract](../baseline/M1.md) là contract phạm vi; tài liệu này diễn giải ranh giới, không mở rộng nó.

## Ba mức phạm vi

| Mức | Nội dung | Trạng thái |
| --- | --- | --- |
| Dài hạn | Toàn chuỗi từ evidence acquisition tới automation/optimization trong charter | Định hướng, chưa có cam kết triển khai |
| M1 | Acquisition corpus giới hạn, provenance, normalization tối thiểu, 1–2 signal giải thích được, query và dashboard demo | Hướng M1 được giao; giới hạn cụ thể là PROPOSED D06–D09 |
| Sau M1 | Forecasting, recommendation, optimization, tự động hóa và mở rộng miền dữ liệu | DEFERRED D10 |

## Scope M1 đề xuất

**PROPOSED — HUMAN DECISION REQUIRED (D06–D09):** một researcher đang khảo sát một chủ đề kỹ thuật; một technical domain; một nguồn; một corpus tối đa 5.000 records trong 24 tháng lịch sử đã kết thúc; một signal chính, signal thứ hai chỉ khi đủ evidence; một historical evaluation case. Đây là trần thử nghiệm để kiểm tra khả thi, không phải benchmark hay workload đã được xác nhận.

Mức nhỏ nhất vẫn đi xuyên hệ thống: acquisition/export có nguồn gốc → observation → normalization → signal → evidence bundle → query → dashboard. Query có thể là chức năng đọc bundle trong cùng ứng dụng; network API riêng không phải điều kiện bắt buộc. Dashboard tối thiểu là một bảng/biểu đồ và khả năng xem signal cùng evidence của một kết quả.

Một corpus giới hạn phải có query/domain definition, ngày cắt dữ liệu, chính sách chọn record và độ đầy đủ. Nếu nguồn trả quá trần, thu hẹp query/window hoặc công bố sampling; không dùng 5.000 record đầu làm đại diện cho toàn miền mà không kiểm tra bias. Khoảng thời gian và thuật ngữ sẽ được chốt ở Research Gate.

## Non-goals M1

**ACCEPTED DECISION D03:** không forecasting, recommendation, optimization, autonomous agents, hạ tầng phân tán lớn, multi-source không cần thiết hoặc opaque LLM-based trend scoring. Không suy ra công nghệ “tốt hơn”, không tư vấn đổi stack từ số bài báo. Không hứa general-purpose platform, real-time monitoring hay production operation.

**DEFERRED D10:** global entity resolution, ontology đầy đủ, graph enrichment rộng, full-text mining quy mô lớn, composite ranking, public deployment và benchmark quy mô lớn. Việc hoãn triển khai không miễn kiểm tra semantics tối thiểu của corpus.

## Chống scope creep

Trước khi thêm nguồn, signal hoặc capability: ghi nhu cầu bị bỏ sót, evidence cho thấy slice hiện tại không đủ, chi phí và phần việc sẽ bỏ; cập nhật D06–D09; chỉ thực hiện sau human acceptance. WIP tối đa 2 theo [backlog](08_MONTH1_BACKLOG.md).

Nếu acquisition hoặc temporal evidence không khả thi, ưu tiên corpus nhỏ hơn và một signal. Không bỏ traceability/reproducibility để giữ số tính năng. Nếu chỉ còn retrospective analysis, phải ghi đúng giới hạn; không tuyên bố đã pass historical as-of evaluation.
