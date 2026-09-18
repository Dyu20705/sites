# 00 — Tuyên bố dự án

## Tóm tắt

**SITES — Scholar Intelligent Trend Evolution System** hướng tới biến bằng chứng thành hiểu biết có thể kiểm tra về sự thay đổi của khoa học và công nghệ theo thời gian.

Điểm cần phân biệt:

- đây là **mục tiêu của dự án**, không phải mô tả một hệ thống đã hoàn thiện;
- scholarly evidence là miền dữ liệu khởi đầu, không phải giới hạn lâu dài;
- Month 1 chỉ tập trung vào detection và descriptive intelligence;
- các capability lớn hơn chỉ thuộc tầm nhìn dài hạn cho tới khi có quyết định mới.

## 1. Bài toán

**HYPOTHESIS:** người khảo sát một lĩnh vực kỹ thuật có thể khó phân biệt thay đổi thực trong hoạt động nghiên cứu với nhiễu do kích thước corpus, cách gọi khái niệm hoặc độ phủ nguồn.

Month 1 phải kiểm chứng giả thuyết này với một nhóm người dùng chính thay vì mặc định SITES phù hợp với mọi đối tượng.

Giá trị hướng tới là giúp người dùng trả lời rõ:

- điều gì đang thay đổi;
- trong corpus và khoảng thời gian nào;
- dựa trên chỉ báo nào;
- bằng chứng nào tạo nên kết quả;
- giới hạn của kết luận là gì.

Một thay đổi quan sát được trong literature **không tự chứng minh** mức độ ứng dụng công nghiệp, tính ưu việt kỹ thuật hay giá trị kinh doanh.

## 2. Tầm nhìn dài hạn

~~~text
thu thập bằng chứng → theo dõi → khai phá → phát hiện xu hướng
→ dự báo → khuyến nghị / hỗ trợ quyết định → tự động hóa / tối ưu hóa
~~~

Đây là không gian capability dài hạn.

- **D03 — ACCEPTED:** M1 chỉ tập trung detection/descriptive intelligence.
- **D04 — ACCEPTED:** scholarly evidence là miền khởi đầu.

D04 là quyết định về phạm vi, không phải kết luận rằng papers luôn là nguồn tốt nhất. Patent, phần mềm và tín hiệu thị trường chưa được đánh giá trong M1.

## 3. Mục tiêu Month 1

Đến 17/10/2026, SITES cần có một demo nhỏ, có thể tái lập, đi từ corpus giới hạn tới một kết luận mô tả có bằng chứng.

[M1 definition](../baseline/M1.md) quy định input, output và tiêu chí hoàn thành. Người dùng chính, corpus, chỉ báo và công nghệ triển khai vẫn còn chờ quyết định.

## 4. Các nguyên tắc đang đề xuất

**PROPOSED — D05:**

- mọi kết luận phải truy ngược được tới bằng chứng;
- observation của nguồn và suy luận của hệ thống phải được tách rõ;
- phải giữ đúng ngữ nghĩa thời gian;
- kết quả phải có thể chạy lại từ input, config, code và metric definition;
- chạy lại cùng input không được làm nhân đôi đóng góp;
- chỉ báo phải giải thích được.

Đây là các yêu cầu ứng viên rút ra từ tư liệu lịch sử và nghiên cứu liên quan; chưa có implementation hiện tại chứng minh rằng chúng đã được đáp ứng.

## 5. Thứ tự ưu tiên bằng chứng

Khi các tài liệu hoặc nhận định kỹ thuật mâu thuẫn, ưu tiên:

~~~text
thí nghiệm / bằng chứng thực nghiệm có thể kiểm tra
> implementation đã được xác minh
> ADR/spec đã được chấp thuận
> issue đang hoạt động
> trao đổi
> giả định
~~~

Thứ tự này chỉ có ý nghĩa trong đúng version, phạm vi và thời điểm của bằng chứng. Test cũ không chứng minh capability hiện tại nếu code hoặc contract đã thay đổi.

Nguồn dữ liệu bên ngoài cũng không phải “source of truth” tuyệt đối. Scholarly API chỉ cung cấp observation theo phạm vi và giới hạn của chính nó.

## 6. Quản trị trạng thái

- [Decision Log](07_DECISION_LOG.md) ghi quyết định và người phê duyệt.
- [Current State](09_CURRENT_STATE.md) chỉ ghi điều đã xác minh.
- [Prior Art Map](03_PRIOR_ART_MAP.md) ghi nguồn nghiên cứu và bài học lịch sử.
- Git history giữ lại code và thiết kế cũ để tham khảo, nhưng lịch sử không tự trở thành baseline mới.

Mọi tài liệu cần phân biệt rõ **vision**, **proposal**, **accepted decision** và **verified state**.
