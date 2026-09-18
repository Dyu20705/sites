# SITES — Scholar Intelligent Trend Evolution System

**SITES** là dự án scholarly intelligence định hướng nghiên cứu, nhằm tìm hiểu cách các khái niệm khoa học và công nghệ thay đổi theo thời gian dựa trên bằng chứng có thể kiểm tra.

Tầm nhìn dài hạn của SITES không giới hạn ở bài báo khoa học hay một dashboard xu hướng. Scholarly literature là miền dữ liệu khởi đầu; về sau hệ thống có thể mở rộng sang các nguồn bằng chứng khác và các năng lực ở mức cao hơn.

~~~text
thu thập bằng chứng → theo dõi → khai phá → phát hiện xu hướng
→ dự báo → khuyến nghị / hỗ trợ quyết định → tự động hóa / tối ưu hóa
~~~

## Trọng tâm hiện tại

Repository đang ở **M0 — định nghĩa dự án**. Cây mã nguồn hiện tại chưa có sản phẩm đang hoạt động hoặc bộ kiểm thử thực thi đại diện cho implementation hiện hành.

Trong **Month 1 (17/09–17/10/2026)**, phạm vi cam kết được cố ý thu hẹp:

- bắt đầu từ scholarly evidence;
- tập trung vào phát hiện và mô tả xu hướng;
- xây một luồng end-to-end nhỏ nhưng có thể tái lập;
- chưa đưa forecasting, recommendation, optimization, autonomous agents hoặc hạ tầng quy mô lớn vào phạm vi cam kết, trừ khi có quyết định mới được chấp thuận rõ ràng.

Các lựa chọn cụ thể như người dùng chính, nguồn dữ liệu, corpus, định nghĩa chỉ báo, cách lưu trữ, framework, công nghệ dashboard và cách triển khai vẫn phải đi qua bước nghiên cứu và các điểm phê duyệt.

## Tài liệu

Tài liệu của repository tách rõ **tầm nhìn dài hạn**, **đề xuất**, **quyết định đã chấp thuận** và **trạng thái đã xác minh** để tránh nhầm kế hoạch với năng lực đã tồn tại.

- **English:** [README gốc](../../README.md) là trang giới thiệu công khai của dự án. Bản tài liệu tiếng Anh đầy đủ sẽ được đặt trong **docs/english/** khi cấu trúc tài liệu đã đủ ổn định.
- **Tiếng Việt:** tài liệu này là bản dịch của README gốc và là điểm vào cho bộ tài liệu M0/M1 hiện tại.
- **日本語:** dự kiến có bản tiếng Nhật trong **docs/japanese/**. Chỉ tạo khi có bản dịch thật đã được review, không tạo thư mục hoặc file rỗng để giữ chỗ.

Bộ tài liệu chi tiết hiện có:

- [Định nghĩa Month 1](baseline/M1.md)
- [Tuyên bố dự án](master/00_PROJECT_CHARTER.md)
- [Phạm vi và các nội dung không thực hiện](master/01_SCOPE_AND_NON_GOALS.md)
- [Câu hỏi nghiên cứu](master/02_RESEARCH_QUESTIONS.md)
- [Bản đồ nghiên cứu liên quan](master/03_PRIOR_ART_MAP.md)
- [Kiến trúc khái niệm](master/04_SYSTEM_ARCHITECTURE.md)
- [Mô hình dữ liệu khái niệm](master/05_DATA_MODEL.md)
- [Quy trình đánh giá](master/06_EVALUATION_PROTOCOL.md)
- [Nhật ký quyết định](master/07_DECISION_LOG.md)
- [Kế hoạch Month 1](master/08_MONTH1_BACKLOG.md)
- [Trạng thái hiện tại đã xác minh](master/09_CURRENT_STATE.md)

## Trạng thái repository và lịch sử

Code, thiết kế và issue cũ vẫn được giữ trong Git history. Chúng là bằng chứng và tư liệu thiết kế có thể tham khảo, nhưng **không tự động trở thành kiến trúc hoặc roadmap hiện tại**.

Baseline mới không mặc định rằng implementation, nguồn dữ liệu, schema, metric hay công nghệ từng được sử dụng trong lịch sử vẫn còn phù hợp. Muốn sử dụng lại phải đánh giá lại theo yêu cầu và bằng chứng hiện hành.

Xem [PR #62](https://github.com/Dyu20705/sites/pull/62) để theo dõi quá trình reset repository và review bộ tài liệu M0.
