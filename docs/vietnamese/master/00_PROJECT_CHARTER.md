# 00 — Project Charter

## Định nghĩa và problem space

**SITES — Scholar Intelligent Trend Evolution System** hướng tới biến bằng chứng thành hiểu biết có thể kiểm tra về sự tiến hóa khoa học và công nghệ. Đây là intended capability, không phải mô tả một hệ thống đang hoạt động.

**HYPOTHESIS về nhu cầu:** người khảo sát một lĩnh vực kỹ thuật khó phân biệt sự thay đổi thực trong hoạt động nghiên cứu với nhiễu do số lượng tài liệu, cách gọi khái niệm hoặc độ phủ nguồn. M1 cần xác minh nhu cầu này với một người dùng chính, thay vì mặc định phục vụ mọi đối tượng.

Giá trị hướng tới là giúp người dùng kiểm tra một nhận định: thay đổi gì, trong corpus và khoảng thời gian nào, dựa trên signal nào, có bằng chứng và hạn chế gì. Nhận định về hoạt động học thuật không tự chứng minh mức độ ứng dụng công nghiệp, tính ưu việt kỹ thuật hoặc lợi ích kinh doanh.

## Tầm nhìn và miền khởi đầu

```text
evidence acquisition → monitoring → mining → trend detection
→ forecasting → recommendation / decision support → automation / optimization
```

Đây là capability space dài hạn. **ACCEPTED DECISION D03:** M1 chỉ detection/descriptive intelligence. **ACCEPTED DECISION D04:** scholarly evidence là miền khởi đầu. Đây là lựa chọn scope, không phải kết luận rằng bài báo là nguồn tốt nhất hoặc các nguồn khác luôn khó khai thác hơn. Patent, phần mềm và tín hiệu thị trường chưa được đánh giá trong M1.

## Mission M1 và nguyên tắc

Đến 17/10/2026, mục tiêu là một demo nhỏ có thể tái lập đi từ corpus bị giới hạn tới nhận định mô tả có dẫn chứng. [M1 contract](../baseline/M1.md) là nơi quy định đầy đủ input/output và exit criteria; target user, corpus, signal và stack còn chờ duyệt.

**PROPOSED — D05, HUMAN DECISION REQUIRED:** giữ các nguyên tắc truy nguyên claim tới evidence; tách observation khỏi suy luận; giữ ngữ nghĩa thời gian; tái lập kết quả từ input/config/code/metric; chạy lại không nhân đôi đóng góp; signal có thể giải thích. Đây là các yêu cầu ứng viên được rút ra từ lịch sử, chưa chứng minh đã thỏa mãn. [Prior Art Map](03_PRIOR_ART_MAP.md) ghi nguồn và giới hạn của từng insight.

## Chính sách source-of-truth

**ACCEPTED DECISION D04**, theo yêu cầu reset/M0: khi có mâu thuẫn về trạng thái kỹ thuật, ưu tiên bằng chứng theo thứ tự:

```text
tests / experiments / empirical evidence có thể kiểm tra
> verified implementation
> accepted ADR/spec
> active issue
> conversation
> assumptions
```

Áp dụng trong đúng phạm vi, version và thời điểm của bằng chứng. Test cũ hoặc test không phù hợp không chứng minh capability hiện tại. Hiện chưa có test/implementation nên không được giả định hai tầng đó tồn tại. Evidence có thể bác bỏ một giả định kỹ thuật; thay đổi scope hoặc quyền phê duyệt vẫn cần người phụ trách chấp thuận. Yêu cầu trực tiếp của chủ dự án là nguồn thẩm quyền cho các quyết định scope D01–D04, không phải bằng chứng hệ thống đã chạy.

External evidence source là nơi cung cấp dữ liệu quan sát. Một scholarly API không đứng thay cho chính sách source-of-truth của dự án, cũng không tự bảo đảm mọi metadata là đúng. Mọi experiment cần ghi input, phương pháp, kết quả, giới hạn và liên kết quyết định được hỗ trợ.

## Trạng thái và quản trị

[Current State](09_CURRENT_STATE.md) xác nhận M0 đang review, không có implementation hiện hành. [Decision Log](07_DECISION_LOG.md) là nơi ghi nhận acceptance; lịch sử không tự trở thành quyết định mới. Không phục hồi code hay cấu hình phụ thuộc chỉ để đáp ứng tài liệu. Thay đổi tài liệu phải thể hiện rõ vision, đề xuất và verified state.
