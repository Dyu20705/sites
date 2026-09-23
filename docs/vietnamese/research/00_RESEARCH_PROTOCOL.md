# 00 — Quy trình nghiên cứu

**Protocol đầu vào:** chủ dự án chấp thuận chuẩn bị ngày 20/09/2026. D05/D06 là ACCEPTED; D07–D09 vẫn PROPOSED. Protocol này tổ chức khảo sát, chưa freeze corpus, chỉ báo hay ngưỡng đánh giá.

## Câu hỏi và ranh giới

Khảo sát [P0 và R1–R8](../master/02_RESEARCH_QUESTIONS.md) cho researcher xem thay đổi mô tả trong corpus học thuật giới hạn. Tạo bằng chứng cho D07 (nguồn/corpus) và D08 (chỉ báo/đánh giá), trong [định nghĩa M1](../baseline/M1.md). Dùng một nguồn, tối đa 5.000 bản ghi và 24 tháng đã kết thúc làm giới hạn audit, chưa coi là định nghĩa corpus đã chấp thuận. Công việc này không chấp thuận forecasting, recommendation, chọn kiến trúc hoặc claim novelty.

## Tìm kiếm và sàng lọc

Dùng Google Scholar và Semantic Scholar để tìm nguồn, sau đó đọc paper gốc qua publisher, trang tác giả hoặc repository. Với claim về provider, kiểm tra tài liệu API/dataset và điều khoản chính thức hiện hành. Ghi dịch vụ thực dùng, query chính xác, ngày tìm, bộ lọc, trang/kết quả đã sàng lọc và giới hạn truy cập. Cú pháp phải phù hợp dịch vụ; các ví dụ dưới đây là nhóm truy vấn, không phải biểu thức API được bảo đảm chạy được.

| Luồng | Nhóm truy vấn ban đầu và từ gần nghĩa | Bằng chứng cần tìm | Work package |
| --- | --- | --- | --- |
| Construct | `"emerging technology" bibliometric`, `"technology emergence" scientometric`, scientific activity / publication frequency / corpus share | Định nghĩa, cách đo, sự khác nhau giữa activity và emergence | A: R1 |
| Chỉ báo | `"burst detection" "scientific literature"`, `"publication growth" normalization`, field normalization / denominator / persistence | Phương pháp chính, alternative nghiêm túc, giả định và failure modes | A: R2/R6 |
| Định nghĩa concept | `"concept evolution" "scientific literature"`, terminology change / alias drift / vocabulary cutoff | Cách gọi, cách đếm và tính hợp lệ theo thời gian | A+B: R2/R3/R4 |
| Provider/thời gian | Tên provider + historical snapshot / version / publication date / metadata update / coverage bias | Availability từng field, độ phủ, sampling và replay | B: R3/R4/R7 |
| Tái lập | computational research reproducibility / provenance / idempotency | Yêu cầu truy nguyên, replay và nguy cơ sai lệch | A+B: R5/R6 |

Mỗi luồng phải tìm limitations, bias, counterexamples và phương pháp cạnh tranh bên cạnh bằng chứng hỗ trợ. Theo các tài liệu được trích dẫn và nghiên cứu trích dẫn lại khi phù hợp; ghi nguồn đã theo. Science mapping và knowledge graph chỉ được đọc để trả lời một RQ còn thiếu cụ thể. Forecasting giữ DEFERRED.

Nhận nguồn định nghĩa construct liên quan, so sánh phương pháp ứng viên, chỉ ra failure mode hoặc mô tả semantics dữ liệu cần thiết. Giữ nghiên cứu nền tảng cũ; kiểm tra tài liệu hiện hành khi hành vi provider có thể thay đổi. Giữ bằng chứng từ domain khác cùng population và giới hạn áp dụng. Không đặt cutoff năm xuất bản tùy ý.

Loại nghiên cứu prediction/market ranking không liên quan, score khó kiểm tra không có phương pháp hữu ích và phiên bản lặp của cùng bằng chứng. Ghi lý do loại. Giữ quan hệ preprint/publication thay vì đếm thành hỗ trợ độc lập. Review hỗ trợ tìm nguồn, không thay việc đọc bằng chứng gốc cho claim quan trọng.

## Ghi nhận và tổng hợp

Dùng [evidence ledger](01_EVIDENCE_LEDGER.md). Ưu tiên bằng chứng gốc đã đọc trực tiếp và artifact tái lập được; ghi rõ secondary synthesis và opinion. Nếu chỉ đọc được abstract, chỉ ghi claim mà abstract hỗ trợ. Đánh dấu full text không truy cập được và trích dẫn gián tiếp là unresolved; không suy ra kết quả từ tiêu đề.

Ghi các claim mâu thuẫn riêng, bao gồm khác biệt dataset, period, định nghĩa và phương pháp. Tổng hợp thành: có hỗ trợ trong phạm vi đã nghiên cứu, còn tranh luận/phụ thuộc phương pháp, hoặc chưa biết đối với SITES. Đóng góp đề xuất chưa phải research gap đã xác lập: claim novelty phải có lượt tìm riêng cho đóng góp và các cách gọi gần nghĩa, kèm search record.

Dừng một luồng khi đã ghi phương pháp chính, alternative nghiêm túc, failure modes, mức phù hợp population mục tiêu, uncertainty còn lại và đủ bằng chứng để đề xuất hoặc bác bỏ lựa chọn. Cũng dừng với kết luận thiếu bằng chứng nếu giới hạn truy cập/dữ liệu ngăn kết luận. Trước Research Gate ngày 27/09, mỗi work package phải có đề xuất có căn cứ hoặc báo cáo bằng chứng còn thiếu và phép kiểm tra nhỏ nhất tiếp theo; ngày đến không làm gate đạt. Số papers không phải tiêu chí hoàn thành.

## Công việc và bàn giao

[Backlog thực hiện](../master/08_MONTH1_BACKLOG.md) định nghĩa A (chỉ báo) và B (nguồn/corpus), tối đa hai work items active. A gửi field requirements cho B; B trả kết quả coverage và temporal trước khi A hoàn tất đề xuất D08. Cả hai giữ lineage theo R5. R8 là walkthrough theo nhiệm vụ sau khi có prototype dùng được; chấp thuận D06 không phải user validation.

Dùng [source audit plan](02_SOURCE_AUDIT_PLAN.md), [case protocol](03_CASE_SELECTION_PROTOCOL.md) và [signal candidates](04_SIGNAL_CANDIDATES.md). Việc tạo tài liệu này chưa thực hiện lấy mẫu hay thí nghiệm chỉ báo. Provider, corpus, công thức, nhãn, ngưỡng và cách tạo reference label vẫn cần con người chấp thuận ở D07/D08 trước implementation phụ thuộc hoặc holdout. D09 là gate sau đó.

Research Entry được kiểm tra riêng trong [checklist](05_RESEARCH_ENTRY_CHECKLIST.md). Thiếu historical availability chỉ cho phép retrospective analysis; E3 vẫn NOT PASSED và chưa đáp ứng M1.
