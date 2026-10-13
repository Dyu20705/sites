# #73 — Phiếu reviewer độc lập với người viết code

Reviewer đã đăng ký: **owner Dyu20705**, vai trò **reviewer**. Tự khai trước task: máy Windows hiện tại; đã xem kết quả, chưa đọc corpus/code. Đây là review có biết trước kết quả, không phải blind study, holdout hoặc đánh giá chất lượng khoa học. Agent viết code và chạy engineering checks riêng; không được trả lời thay reviewer.

Trạng thái ban đầu: **NOT MEASURED**. Chưa có câu trả lời, replay hoặc thao tác browser nào của reviewer được suy ra từ việc đăng ký vai trò.

1. Dùng gói và lệnh trong [REPLAY.md](REPLAY.md) để verify, test, build hai thư mục mới, compare và mở `index.html`. Ghi lỗi nguyên văn nếu có; không sửa code/input. Gửi lại hai `execution.json`, kết quả compare và semantic root. Nếu chỉ thực hiện một phần, ghi đúng phần đó.
2. Ghi ngày/giờ, máy/OS, Python, trình duyệt/tên phiên bản, internet có ngắt hay không và có được người khác trợ giúp không. Profile tự động chỉ xác minh file browser đã cài; không chứng minh browser đã mở hoặc task đã thành công.
3. Trên dashboard, chọn **2019-02 → 2019-04** trong ma trận. Mở một bản ghi MATCH và một bản ghi NONMATCH từ danh sách của khoảng đó, kiểm tra nguồn v1/current rồi dùng Back để quay lại. Ghi hai work/version ID và mọi lỗi điều hướng. Có thể xem các giới hạn và sensitivity trên giao diện. Không yêu cầu suy luận chủ đề từ full text.
4. Trả lời năm câu bằng lời của bạn, dựa trên giao diện:

   - **Q1/count_share:** Trong khoảng đã chọn, n, N và tỷ lệ gộp là bao nhiêu? Tỷ lệ gộp được tính thế nào?
   - **Q2/denominator:** Những công trình nào nằm trong mẫu số? Vì sao công trình không khớp vẫn có mặt?
   - **Q3/evidence:** Hai ID bạn vừa mở là gì? Trường nào quyết định MATCH/NONMATCH, và bằng chứng raw nào hỗ trợ giá trị đó?
   - **Q4/temporal:** Mốc năm 2019 và mốc thu nhận năm 2026 có ý nghĩa khác nhau thế nào? Có thể kết luận dữ liệu/title/category đã công khai đúng thời điểm năm 2019 không?
   - **Q5/claim_limits:** Kết quả này cho phép mô tả điều gì? Nó có chứng minh chất lượng phát hiện xu hướng khoa học, sự tăng/giảm của lĩnh vực hoặc độ chính xác ngữ nghĩa không?

5. Ghi điều gây khó hiểu, thời gian hoàn thành task và mức trợ giúp thực tế. PASS usability đòi hỏi **5/5 câu đúng**, mở cả match và nonmatch, chọn đúng khoảng, không sửa code. Câu trả lời thiếu/sai giữ nguyên để ghi kết quả; không sửa protocol sau khi xem câu trả lời nhằm tạo PASS.

Engineering rubric đã frozen trước task: Q1 phải nhất quán với query của khoảng và ratio-of-sums; Q2 phải giải thích toàn bộ corpus đủ điều kiện, không lọc theo concept; Q3 phải đối chiếu title v1/rule và raw ID/index/hash; Q4 phải tách event khỏi acquisition và giữ availability UNKNOWN; Q5 phải giữ retrospective lexical / sparse support / scientific quality NOT MEASURED. Hỗ trợ hướng dẫn thao tác phải được ghi. Không dùng rubric để viết câu trả lời thay người review.

Bảy checklist demo ở #66/#73 giữ **0/7 independently verified** đến khi kết quả người review thực sự được đối chiếu. Những engineering checks đã PASS được báo riêng, không biến thành human validation.
