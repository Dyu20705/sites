# SITES — Scholar Intelligent Trend Evolution System

[English](../../README.md) · Tiếng Việt · [日本語](../japanese/README.md)

**SITES** là một dự án nghiên cứu về scholarly intelligence, hướng tới việc phân tích sự thay đổi của các khái niệm khoa học và công nghệ theo thời gian dựa trên bằng chứng có thể kiểm tra.

Tầm nhìn dài hạn của SITES không dừng ở bài báo khoa học hay dashboard xu hướng. Tài liệu học thuật là miền dữ liệu khởi đầu; về sau dự án có thể mở rộng sang các nguồn bằng chứng khác và các năng lực phân tích, hỗ trợ quyết định ở mức cao hơn.

~~~text
thu thập bằng chứng → theo dõi → khai phá → phát hiện xu hướng
→ dự báo → khuyến nghị / hỗ trợ quyết định → tự động hóa / tối ưu hóa
~~~

## Trọng tâm hiện tại

Repository đang ở **M0 — định nghĩa dự án**. Nhánh hiện tại chưa chứa một phiên bản triển khai của sản phẩm hay bộ kiểm thử thực thi tương ứng.

Trong **Month 1 (17/09–17/10/2026)**, phạm vi cam kết được cố ý thu hẹp:

- bắt đầu từ bằng chứng học thuật;
- tập trung vào phát hiện và mô tả xu hướng;
- xây một luồng end-to-end nhỏ nhưng có thể tái lập;
- chưa đưa forecasting, recommendation, optimization, autonomous agents hoặc hạ tầng quy mô lớn vào phạm vi M1, trừ khi có quyết định mới được chấp thuận rõ ràng.

Các lựa chọn cụ thể như người dùng chính, nguồn dữ liệu, tập tài liệu phân tích, định nghĩa chỉ báo, cách lưu trữ, framework, công nghệ dashboard và cách triển khai vẫn phải đi qua bước nghiên cứu và các điểm phê duyệt.

## Tài liệu

Bắt đầu từ [mục lục tài liệu](../README.md).

Bộ tài liệu định nghĩa M0/M1 hiện đang được review bằng tiếng Việt:

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

Các bản tiếng Anh, tiếng Việt và tiếng Nhật phải tương đương về **nội dung**, không phải từng câu từng chữ. Decision ID, ngày, trạng thái, yêu cầu và ý nghĩa kỹ thuật phải giữ nhất quán giữa các bản dịch.

## Trạng thái repository và lịch sử

Code, thiết kế và issue cũ vẫn được giữ trong Git history. Chúng là bằng chứng và tư liệu thiết kế có thể tham khảo, nhưng **không tự động trở thành kiến trúc hoặc roadmap hiện tại**.

Baseline mới không mặc định rằng phần triển khai, nguồn dữ liệu, schema, metric hay công nghệ từng được sử dụng trong lịch sử vẫn còn phù hợp. Muốn sử dụng lại phải đánh giá lại theo yêu cầu và bằng chứng hiện hành.

Xem [PR #62](https://github.com/Dyu20705/sites/pull/62) để theo dõi quá trình reset repository và review bộ tài liệu M0.
