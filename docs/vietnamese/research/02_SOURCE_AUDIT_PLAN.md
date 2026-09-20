# 02 — Kế hoạch audit nguồn

**Trạng thái:** đã có quy trình audit; mọi claim về độ phù hợp provider đều UNVERIFIED. Chưa lấy mẫu hoặc freeze corpus. Phụ trách: work package B, nhận field requirements từ A trong [backlog](../master/08_MONTH1_BACKLOG.md).

## Sàng lọc ứng viên

Sàng lọc các ứng viên D07 hiện có theo cùng yêu cầu. Tên provider chỉ xác định ứng viên, không phải khuyến nghị hay năng lực đã xác minh. Khi thực hiện, tìm và ghi tài liệu chính thức hiện hành.

| Ứng viên | Bản ghi sàng lọc cần có | Kết quả hiện tại |
| --- | --- | --- |
| arXiv | Access/export, điều khoản, field chính xác, coverage, version, ngày, historical availability và replay | NOT AUDITED |
| OpenAlex | Access/export, điều khoản, field chính xác, coverage, version, ngày, historical availability và replay | NOT AUDITED |
| Crossref | Access/export, điều khoản, field chính xác, coverage, version, ngày, historical availability và replay | NOT AUDITED |
| Semantic Scholar | Access/export, điều khoản, field chính xác, coverage, version, ngày, historical availability và replay | NOT AUDITED |
| DBLP | Access/export, điều khoản, field chính xác, coverage, version, ngày, historical availability và replay | NOT AUDITED |

Screen tài liệu cả năm nguồn; chỉ sample audit ứng viên có field được mô tả, quyền sử dụng và cơ chế truy cập có khả năng đáp ứng nhiệm vụ giới hạn. Nếu nhiều nguồn phù hợp, ưu tiên audit nguồn có bằng chứng historical availability và replay rõ nhất, sau đó xét chi phí thu thập được mô tả thấp nhất; ghi lý do mà chưa accept D07. Dừng mở rộng audit khi một ứng viên có đủ bằng chứng đo được để đề xuất D07 và các alternative có kết quả sàng lọc rõ. Chỉ audit thêm để giải quyết thiếu hụt hoặc tradeoff quan trọng. Claim trong tài liệu không phải coverage đo được.

## Contract field cần kiểm tra

Với từng yêu cầu logic dưới đây, ghi field/path chính xác của provider, section tài liệu, type/null behavior, giá trị mẫu quan sát được và chỉ báo nào cần field đó. Mapping này là artifact audit, không phải schema vật lý.

| Yêu cầu logic | Mục đích và kiểm tra |
| --- | --- |
| Work ID, source URL, version/revision ID | Mở lại observation; kiểm tra duplicate/revision; không đồng nhất work và version |
| Title và abstract/category text nếu cần | Gán concept; missingness và thay đổi text/vocabulary |
| Ngày publication/submission | Ghi sự kiện được biểu diễn, độ chính xác và khả năng sửa; không hoán đổi ý nghĩa các sự kiện |
| Ngày update/index/acquisition và historical snapshots | Tách event time khỏi availability time; chứng minh thời điểm có thể biết từng giá trị |
| Scope fields và corpus totals | Tái tạo query membership và denominator, gồm cả record không khớp concept khi tính share |
| Citation/reference observations, chỉ khi cần | Giá trị lịch sử tại từng cutoff; giá trị cộng dồn hiện tại không tái tạo được giá trị quá khứ |
| Query, export identity và provenance | Tái tạo acquisition, cutoff, config và tham chiếu raw observation |

## Audit truy cập, sampling và thời gian

1. Ghi bằng chứng chính thức cùng URL, section/version và ngày đọc về authentication, API/bulk/snapshot, quotas, rate limits, thay đổi version, quyền lưu/phân phối/demo và chi phí request/thời gian/lưu trữ dự kiến. Điều khoản chưa rõ giữ unresolved; public API không mặc nhiên cho phép phân phối lại. Không ghi credentials vào artifact.
2. Trước acquisition, ghi candidate domain/query, thời kỳ đã kết thúc, cutoff, acquisition time và sampling rule. Giữ trong 5.000 records và 24 tháng đã kết thúc. Nếu vượt giới hạn, định nghĩa sampling deterministic qua các tầng thời gian liên quan, gồm seed/order và inclusion rule, đồng thời công bố bias. Không coi N kết quả đầu đại diện cho population. Không chạy chỉ báo để chọn mẫu.
3. Kiểm tra thứ tự pagination, truncation, tính nhất quán của count và query completeness. Báo cáo số yêu cầu so với số nhận, duplicates, revisions, giá trị không hợp lệ và missingness có tử/mẫu theo field và tầng thời gian. Tách field thiếu trong schema, thiếu trong record và giá trị không hợp lệ. Ghi coverage exclusions và publication/indexing delay.
4. Với mỗi field dùng tại cutoff T, ghi ý nghĩa sự kiện, khả năng sửa, bằng chứng giá trị cụ thể đã available trước hoặc tại T, và khả năng nguồn tái tạo trạng thái đó. Retrieval timestamp hôm nay hoặc publication date cũ riêng lẻ không chứng minh historical availability. Đánh giá cả vocabulary và metadata được sửa về sau.
5. Kiểm tra khả năng giữ raw observations được phép dùng, snapshot/export identity ổn định và provenance. Định nghĩa các replay/idempotency checks nhỏ nhất tiếp theo trên frozen input; báo riêng check nào thực sự đã chạy. Live query thay đổi không phải replay snapshot.

## Bàn giao quyết định và xử lý failure

Trả bảng so sánh tách VERIFIED evidence, ASSUMPTION và unknowns; sample coverage/missingness đo được; temporal availability từng field; quyền lưu/chia sẻ; chi phí và sampling bias; thiếu hụt loại ứng viên; và **PROPOSED D07** hoặc báo cáo thiếu bằng chứng. Liên kết sample/query/snapshot cùng nguồn hỗ trợ trong [ledger](01_EVIDENCE_LEDGER.md).

Gửi A các field khả thi, giới hạn đơn vị đếm/denominator và time semantics trước khi A hoàn tất D08. Ưu tiên thu hẹp chỉ báo hoặc corpus nếu thiếu field; nguồn thứ hai cần nhu cầu đo được và human acceptance. Nếu không chứng minh historical availability, gọi kết quả retrospective, ghi **E3 NOT PASSED** và yêu cầu scope review; không tự cho M1 đạt. Kế hoạch này chưa chấp thuận chọn provider, tích hợp live data hay stack triển khai.
