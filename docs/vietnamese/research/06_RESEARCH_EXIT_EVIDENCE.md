# 06 — Bằng chứng Research Exit, 27/09/2026

**Kết quả: INSUFFICIENT EVIDENCE; research-ready NOT PASSED.** Đây là kết quả khảo sát #64/#65, chưa chấp thuận D07/D08, chưa kết luận M1 thất bại cuối cùng và không chứng minh mọi provider đều không khả thi.

Baseline: `master@0a853636ef6d1be9d3bb85058f34faf368fcb6ce`. [#68 đã đạt](https://github.com/Dyu20705/sites/issues/68#issuecomment-5795799412); D05/D06 giữ ACCEPTED. #70 có thẩm quyền Research Exit. WIP vẫn là #64 + #65; #69 là mục lục bằng chứng. Gói này không đóng issue hoặc thay quyết định gate có thẩm quyền.

## Câu hỏi và bàn giao field

Giữ nguyên P0. **RQ-measurement:** count/share từ từ ngữ trong corpus giới hạn có phân biệt được thay đổi với corpus growth và sai lệch quan sát đã biết không? **RQ-evidence:** từng giá trị có tái tạo được từ records, vocabulary, membership và phép biến đổi hợp lệ tại cutoff không? Đạt một câu hỏi không làm câu hỏi còn lại tự đạt.

Construct khảo sát là **tỷ lệ xuất hiện từ ngữ trong tiêu đề phiên bản đầu thuộc corpus khai báo**, không phải toàn bộ nghiên cứu về một chủ đề, emergence, impact hay adoption. Title-only dễ kiểm tra nhưng bỏ sót alias và nội dung ngoài tiêu đề. Không claim novelty.

| Yêu cầu A → B | Mục đích / bằng chứng cần có |
| --- | --- |
| Work ID + version + source URL | Đếm work riêng biệt; giữ revision mà không nhân đôi |
| Title phiên bản đầu | Match concept; phải đo field thiếu và text thay đổi |
| Event time và bằng chứng public availability | Event time gán bin; availability quyết định được dùng tại T |
| Corpus membership, gồm nonmatches | Tái tạo denominator; query chỉ tìm concept không đủ tính share |
| Membership và vocabulary lịch sử | Không âm thầm đưa category hiện tại hoặc synonym về sau vào as-of claim |
| Query, ordering, snapshot/hash, acquisition time | Phân biệt input tái lập được với live query thay đổi |

Đây là giao diện audit, chưa phải schema sản phẩm. Text, ngày, membership và version phải dùng được tại cutoff liên quan; retrieval time hôm nay không phải bằng chứng đó.

## Bổ sung evidence ledger từ literature

Người trích xuất: Codex, 27/09/2026. Chỉ claim độ sâu đọc tại các mục nêu rõ. Danh tính nguồn và query thực dùng nằm trong [search log](../../../experiments/research_exit_20260927/search-log.json). Đây là critical notes, chưa phải systematic review toàn diện.

| ID / nguồn và vị trí đã đọc | Bằng chứng, population và diễn giải | Giới hạn / quyết định |
| --- | --- | --- |
| EL-001 — Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/html/1503.00673), §§3–4, Bảng 2 | Review khái niệm; construct nhiều chiều rộng hơn frequency. Đã đọc các mục full text trực tiếp, vượt mức abstract-only trước đây. **supports** ranh giới claim hẹp. | Tổng hợp literature, không kiểm chứng SITES; giới hạn tìm kiếm ảnh hưởng coverage. R1/D08: không gọi count tăng là emergence. |
| EL-002 — Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/bhs.pdf), §§2,4, tr.13–16 | Phương pháp và ví dụ tiêu đề hội nghị; mô hình batch dùng relevant/total documents và phạt chuyển trạng thái. Có hiệu ứng thuật ngữ. **mixed**: alternative nghiêm túc cho prevalence. | Chuỗi hội nghị khác sáu tháng cs.SE; phụ thuộc tham số/vocabulary. Chưa đo lợi ích bổ sung. R2/R6: hoãn code burst. |
| EL-003 — Sandve et al. (2013), [Ten Simple Rules](https://doi.org/10.1371/journal.pcbi.1003285), Rules 1–3 | Hướng dẫn phương pháp, không phải nghiên cứu thực nghiệm SITES. **supports** lưu workflow, input, parameters, versions và intermediate evidence. | Sai sót tái lập được vẫn là sai sót. R5: hash/rerun hỗ trợ provenance, không chứng minh detection validity. |
| EL-004 — Nelis et al. (2022), [General Growth Tendency](https://doi.org/10.1371/journal.pone.0268433), Introduction, Methods: GGT calculation/data collection | So sánh tăng trưởng field với tổng publications; dữ liệu life sciences, reviews, patents. **supports** kiểm tra denominator confounding; thêm alternative bằng growth rates. | Chưa kiểm chứng trên corpus này; hiệu growth rates khác share; base nhỏ gây dao động. Phương pháp sau 2019 dùng cho nghiên cứu hôm nay, không làm vocabulary/label lịch sử. R2/R6. |
| EL-005 — Manès et al. (2018), [Fuzzing: Art, Science, and Engineering, v1](https://arxiv.org/abs/1812.00140v1), chỉ abstract và submission history | Context độc lập trước 2019 xác định fuzzing là chủ đề đã có nghiên cứu. **supports** candidate case, không phải kỳ vọng tăng. | Chưa critical review full text phiên bản này; abstract không tạo reference trend label hay từ điển đầy đủ. R6. |

**Tổng hợp:** count, prevalence và burst trả lời các câu hỏi gần nhau nhưng khác nhau. Synthetic evidence cho thấy share có thể giữ nguyên khi count tăng; share cũng đổi khi thành phần denominator đổi. Không đại lượng nào tự chứng minh emergence. Chưa biết với SITES: corpus lịch sử dùng được, lexical recall, minimum support, temporal validity và detection quality thực tế. Chưa xác lập gap/novelty.

## Chọn domain và case trước output

[Preregistration](../../../experiments/research_exit_20260927/preregistration.json) được ghi trước acquisition và xem output chỉ báo. Software engineering/testing là domain audit đầu tiên; automated reasoning và distributed systems được hoãn do chưa có context case trước cutoff được đọc tương đương, **không** phải đã đo thấy dữ liệu kém hơn.

- Historical candidate: fuzzing, dựa EL-005 độc lập với đồ thị; không giả định chiều tăng/giảm.
- Development candidate: `cat:cs.SE`, submissions 01–06/2019, bin tháng, tối đa 2.000 works riêng biệt; lấy toàn query nếu nằm trong bound, vượt thì dừng.
- Holdout candidate: 07–12/2019; chưa lấy hay đánh giá. Corpus/case chưa được chấp thuận.
- Control: synthetic null giữ share khi corpus tăng; chỉ kiểm tra confounding và phép tính, không chứng minh detection ngoài thực tế.
- Exposure: đã xem synthetic outputs; chưa có output corpus thật. Ghi mọi amendment sau này; không gọi lại output đã xem là unseen holdout.

Pattern `\bfuzz(?:ing|er|ers)?\b` là đề xuất khảo sát. EL-005 chứng minh từ “fuzzing” tồn tại trước cutoff, không xác lập độc lập mọi biến thể hoặc tính đầy đủ của pattern. Vocabulary lịch sử còn unresolved.

## Thí nghiệm đã chạy và giới hạn

Xem [provider audit](07_PROVIDER_AUDIT_RESULTS.md), [decision packets](08_D07_D08_EXIT_PACKET.md) và [experiment artifacts](../../../experiments/research_exit_20260927/README.md) dùng chung.

- Count request arXiv đầu tiên: HTTP 406, không có record response thành công. Diagnostic content negotiation AM-01: HTTP 406. Web tool cũng không truy cập được count URL.
- HEAD probe archive DBLP lịch sử: connection reset, chưa tải archive. Đây là quan sát truy cập trong môi trường này, không chứng minh DBLP thiếu snapshots.
- **15 test methods synthetic đều đạt trong mỗi lần chạy ở hai tiến trình riêng**, gồm bảy tình huống series tính tay; hash output giống nhau. Chưa chạy so sánh signal corpus thật, annotation, phép đo missingness hay holdout.
- Ví dụ số: `10/100 = 20/200 = 0,1`; giữ numerator thì `10/100 = 0,1` nhưng `10/200 = 0,05`. Denominator rỗng và bin thiếu trả null, không trả zero.

Output dùng chung giữ expected/actual và input hashes. Availability trong fixture là dữ kiện giả lập, không chứng minh E3, correctness sản phẩm, reviewer replay độc lập hay giá trị người dùng.
