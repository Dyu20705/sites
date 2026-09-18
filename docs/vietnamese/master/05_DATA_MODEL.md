# 05 — Conceptual Data Model

**PROPOSED — HUMAN DECISION REQUIRED (D05/D09).** Các tên dưới đây là domain vocabulary để research, không phải class, table hoặc SQL DDL. Chỉ triển khai khái niệm cần cho signal đã được chấp thuận.

| Concept | Ý nghĩa và thông tin tối thiểu cần khảo sát | Quan hệ / ranh giới |
| --- | --- | --- |
| EvidenceSource | Nơi phát hành dữ liệu; mô tả nguồn, query/export, quyền sử dụng | Một nguồn có nhiều observations; không cấp chân lý tuyệt đối |
| Observation | Điều nguồn báo ở một lần/version cụ thể; source record reference, payload/snapshot reference, acquisition time và availability evidence nếu có | Một work có thể có nhiều observations; observation khác derived claim |
| ScholarlyWork | Đơn vị học thuật được phân tích trong corpus; source-local identifier và metadata cần cho signal | Cross-source canonical identity DEFERRED; không tự gộp preprint và publication |
| Concept/Technology | Nhãn cùng definition/vocabulary version và quy tắc nối với evidence | Alias match là phép biến đổi có version, không mặc định ontology toàn cục |
| TemporalMetric | Giá trị đo/quan sát, đơn vị, time interval, timestamp semantics và missingness | Source citation count và system document count phải phân biệt origin |
| Signal | Phép biến đổi có definition/version/config; giá trị, window, denominator và input references | Không tự là nhận định về xu hướng; một signal dùng nhiều observations |
| TrendAssessment | Nhận định có phạm vi, rule version, signal references, cutoff, label và limitation | System-derived claim; có thể insufficient evidence |
| EvidenceLink | Liên kết assessment → signal → observation và transformation | Không chỉ liên kết vài bài đại diện; phải truy được tập đóng góp vào tính toán |

Input snapshot và execution record là metadata hỗ trợ replay, không áp đặt thêm entities vật lý. Đại diện evidence trên dashboard là một subset được chọn bằng quy tắc công khai; bundle phải giữ lineage đầy đủ.

## Temporal semantics

| Thời gian | Câu hỏi nó trả lời | Rủi ro nếu đánh đồng |
| --- | --- | --- |
| Appearance/submission | Bản này xuất hiện/nộp khi nào? | Không phải ngày publication |
| Publication | Nguồn nói công bố chính thức khi nào? | Có thể cập nhật hoặc chỉ có độ chính xác năm |
| Revision | Nội dung/version đổi khi nào? | Revision sau cutoff có thể đưa từ khóa tương lai vào quá khứ |
| Observation | Nguồn/collector quan sát giá trị khi nào? | Không tự chứng minh giá trị đã biết tại publication date |
| Ingestion | SITES nạp lúc nào? | Không phản ánh chronology nghiên cứu |
| Metric observation | Citation count hoặc metric được đo khi nào? | Tổng hiện tại không phải tổng tại historical cutoff |

Giữ unknown, precision và provenance của timestamp. Không gán ngày giả cho year-only record mà không ghi chính sách. Field availability tại cutoff cần bằng chứng riêng (snapshot/version); event date trước cutoff là điều kiện chưa đủ. Dataset tải hôm nay có thể chỉ hỗ trợ retrospective analysis dù chứa bài cũ. [Evaluation Protocol](06_EVALUATION_PROTOCOL.md) quy định giới hạn đó.

## Minimum identity và các quyết định hoãn

**OPEN — Research Gate:** đơn vị đếm là source record, version hay work? D07/D08 phải chốt cách xử lý duplicate/version vì nó đổi denominator. Đề xuất dùng source-local identity trong một corpus để giảm scope; vẫn cần test duplicate/revision. Không mặc định DOI đồng nghĩa cùng work hoặc title giống nhau thì merge.

**DEFERRED D10:** global canonical identity, surrogate-key algorithm, fuzzy entity resolution, typed relation graph, full citation topology. Nếu signal đã chọn buộc dùng chúng, phải quay lại scope gate thay vì âm thầm mở rộng model.
