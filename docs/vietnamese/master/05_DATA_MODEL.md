# 05 — Mô hình dữ liệu khái niệm

**PROPOSED — D05/D09.** Các khái niệm dưới đây là vocabulary phục vụ research và design. Chúng **không phải** class, table hay SQL schema đã được chấp thuận.

Chỉ triển khai những khái niệm thực sự cần cho chỉ báo M1.

## Các khái niệm chính

| Khái niệm | Ý nghĩa tối thiểu | Ranh giới |
| --- | --- | --- |
| EvidenceSource | Nguồn phát hành dữ liệu, query/export và điều kiện sử dụng | Một nguồn có thể sinh nhiều Observation; không phải chân lý tuyệt đối |
| Observation | Điều nguồn báo tại một lần/version cụ thể; có source reference, snapshot/payload reference, acquisition time và availability evidence nếu có | Observation khác derived claim |
| ScholarlyWork | Đơn vị học thuật được phân tích trong corpus | Cross-source canonical identity DEFERRED; không tự gộp preprint với publication |
| Concept / Technology | Khái niệm được theo dõi cùng definition/vocabulary version | Alias matching là phép biến đổi có version, không phải ontology toàn cục |
| TemporalMetric | Giá trị đo cùng đơn vị, khoảng thời gian, timestamp semantics và missingness | Phải phân biệt metric do nguồn cung cấp với metric hệ thống tính |
| Signal | Chỉ báo được tính từ definition/version/config, có window và denominator | Không tự đồng nghĩa với “trend” |
| TrendAssessment | Kết luận mô tả có rule version, cutoff, signal references và limitation | Có thể là insufficient evidence |
| EvidenceLink | Liên kết assessment → signal → observation → transformation | Phải truy được toàn bộ đóng góp, không chỉ vài paper đại diện |

Input snapshot và execution record là metadata hỗ trợ việc chạy lại; chưa cần biến thành entity vật lý riêng nếu không có nhu cầu.

## Ngữ nghĩa thời gian

| Loại thời gian | Trả lời câu hỏi | Rủi ro khi dùng sai |
| --- | --- | --- |
| Appearance / submission | Bản này xuất hiện hoặc được nộp khi nào? | Không đồng nghĩa publication date |
| Publication | Nguồn nói công bố chính thức khi nào? | Có thể chỉ chính xác tới năm hoặc được cập nhật |
| Revision | Version đổi khi nào? | Revision sau cutoff có thể đưa thông tin tương lai vào quá khứ |
| Observation | Nguồn/collector quan sát giá trị khi nào? | Không chứng minh giá trị đã tồn tại từ publication date |
| Ingestion | SITES nạp dữ liệu khi nào? | Không phản ánh chronology của nghiên cứu |
| Metric observation | Citation count/metric được đo khi nào? | Tổng hiện tại không phải tổng tại historical cutoff |

Cần giữ unknown, precision và provenance của timestamp. Không tự tạo ngày giả cho record chỉ có year nếu không công bố policy.

Việc event date nằm trước cutoff **không đủ** để chứng minh một field đã available tại cutoff. Dataset tải hôm nay vẫn có thể chỉ hỗ trợ retrospective analysis dù record mang ngày lịch sử.

## Identity tối thiểu và phần hoãn

**OPEN — Research Gate:** đơn vị đếm là source record, version hay work?

D07/D08 phải chốt cách xử lý duplicate/version vì lựa chọn này thay đổi denominator.

Đề xuất hiện tại là ưu tiên source-local identity trong một corpus để giảm scope, nhưng vẫn phải kiểm tra duplicate và revision.

**DEFERRED — D10:**

- global canonical identity;
- surrogate-key algorithm;
- fuzzy entity resolution;
- typed relation graph;
- full citation topology.

Nếu chỉ báo được chọn bắt buộc cần những phần này, phải quay lại scope gate thay vì âm thầm mở rộng data model.
