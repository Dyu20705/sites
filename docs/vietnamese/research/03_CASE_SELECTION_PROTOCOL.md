# 03 — Quy trình chọn case

**Trạng thái:** đã chuẩn bị quy trình chọn; chưa freeze concept, corpus, period, reference label hoặc quality threshold. Work package A phụ trách R6; B cung cấp bằng chứng khả thi. Xem [backlog](../master/08_MONTH1_BACKLOG.md).

## Điều kiện chọn trước khi xem output chỉ báo

Lập shortlist historical concept và control từ literature/context độc lập cùng source coverage, trước khi xem output chỉ báo SITES. Ghi mọi ứng viên, lý do nhận/loại, người chọn, ngày, nguồn đã đọc và việc đã từng xem output hay chưa. Không chọn concept có đồ thị đẹp nhất.

Historical case phải phù hợp candidate domain D07, có thời kỳ đã kết thúc và xác định được, đủ records theo support criterion đề xuất từ audit, và có literature độc lập để đặt hoạt động trong thời kỳ đó vào bối cảnh. Context không tự trở thành reference label hoặc ground truth. Domain và minimum support cần acceptance ở D07/D08; tính hợp lệ hiện tại là có điều kiện.

Control phải kiểm tra một failure mode: ví dụ concept có căn cứ độc lập cho kỳ vọng hoạt động ổn định, hoặc synthetic null giữ share cố định khi corpus tăng. Ghi vì sao phép so sánh có ý nghĩa và nó không kiểm chứng được gì. Synthetic control có thể kiểm tra phép tính/confounding nhưng không chứng minh detection quality ngoài thực tế. E2 cần ít nhất một historical case và một control; lựa chọn cụ thể vẫn mở.

## Development, freeze và holdout

1. Ghi selection rules trước khi xem system output. B được kiểm tra coverage/missingness để đánh giá khả thi mà không dùng hiệu năng chỉ báo để chọn case.
2. Đề xuất tách development/holdout bằng period hoặc records chính xác, mục đích được phép dùng và lịch sử truy cập/đã xem. Dùng development evidence để so sánh phương pháp; không tuning bằng kết quả holdout. Output đã xem không được gọi lại là holdout chưa từng thấy.
3. Trước holdout, lấy human acceptance cho D07/D08 và ghi freeze có version: case/control được chọn và phần loại, query/corpus/snapshot, period/cutoff, vocabulary/version, unit/denominator, formula/bin/window, minimum support, cách tạo reference label, quality threshold, sensitivity ranges và tham chiếu software/config khi có. Tài liệu entry này chưa freeze nội dung nào.
4. Xác định người tạo reference labels, bằng chứng độc lập họ được xem, cách giữ disagreement và biểu diễn uncertainty. Tránh tạo reference từ chính chỉ báo được đánh giá. Phương pháp và rubric cần D08 acceptance; chưa có user study hoặc annotation.
5. Giữ failures, counterexamples và disagreement. Sensitivity analysis phải dùng khoảng đã freeze trước holdout và công bố mọi biến thể đã đánh giá.

## Thay đổi và giới hạn thời gian

Mọi amendment ghi ngày, tác giả, lý do, decision bị ảnh hưởng và output/holdout đã được xem hay chưa. Sau khi đã xem, gọi phân tích sửa đổi là exploratory; cần protocol mới được chấp thuận và holdout thực sự chưa xem trước khi đưa claim confirmatory. Không ghi đè freeze gốc hoặc giấu lần chạy thất bại.

Availability phải bao phủ mọi input field và vocabulary tại cutoff T. Thiếu bằng chứng đó thì case chỉ là retrospective; **E3 NOT PASSED** vẫn áp dụng. Câu chuyện lịch sử, control hoặc publication date cũ không chứng minh temporal isolation.

Bàn giao selection log, nguồn context độc lập, case/control đề xuất, freeze proposal, exposure/amendment log và limitations còn mở cho D08. Research Entry kiểm tra các quy tắc này tồn tại; chưa claim đã chọn case hoặc đánh giá thành công.
