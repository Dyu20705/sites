# 04 — Các chỉ báo ứng viên

**Trạng thái:** ứng viên cần khảo sát, chưa phải metric đã chấp thuận. Work package A phụ trách R1/R2/R6 và nhận kết quả field/temporal từ B. Công thức, đơn vị đếm, bin/window, threshold, minimum support và nhãn đầu ra vẫn mở ở D08.

| Ứng viên / construct | Nhóm công thức và dữ liệu cần | Confounders và failure modes | Kiểm tra phân biệt |
| --- | --- | --- | --- |
| Absolute count / hoạt động học thuật quan sát được | Số đơn vị khớp concept trong time bin; cần IDs, concept text/definition và observations có ngày | Corpus tăng, coverage shift, duplicate versions, query selection và publication delay; count tăng không chứng minh emergence | Expected counts độc lập; duplicates/revisions; zero khác missing; concept share cố định trong corpus tăng |
| Corpus share / hoạt động tương đối | Số đơn vị khớp chia số đơn vị corpus hợp lệ trong cùng bin; cần denominator tái tạo được gồm cả record không khớp | Denominator drift, retrieval thiếu, support nhỏ, alias changes và provider coverage thay đổi; normalization không loại mọi bias | Giữ numerator và đổi denominator; share ổn định khi count tăng; không âm thầm biến denominator rỗng thành zero |
| Burst / thay đổi cường độ tạm thời | Mô hình thay đổi tần suất ứng viên so với count/share; cần observations có thứ tự và đủ lịch sử | Nhạy window/parameter, mẫu nhỏ, indexing chậm và spike đơn lẻ | Synthetic spike so với thay đổi kéo dài; chỉ đổi parameters đã preregister; so với baseline đơn giản hơn |
| Persistence / hoạt động kéo dài | Phép đo support lặp lại qua bins; cần cách đếm và temporal coverage nhất quán | Duration tùy ý, nhầm missing bin thành inactivity, revisions lặp | Hoạt động kéo dài so với spike đơn lẻ; missing-bin scenarios; chứng minh thông tin baseline chưa cung cấp |
| Citation dynamics / thay đổi hoạt động trích dẫn được ghi nhận | Citation observations lịch sử hoặc events có ngày và bằng chứng availability | Censoring, age/cohort bias, citation delay và rò rỉ giá trị về sau vào cutoff trước | Chứng minh observations lịch sử trước; thiếu chúng thì không tái tạo velocity quá khứ từ cumulative totals hiện tại |

Count và share là baseline để so sánh, chưa phải hai chỉ báo đã chọn cho sản phẩm. Chỉ khảo sát burst/persistence khi literature và data fitness chỉ ra thiếu hụt; citation dynamics cần thêm bằng chứng lịch sử nêu trên. Không mở rộng thành bộ metric lớn.

Với mỗi ứng viên, ghi construct được đo, unit, required fields, temporal assumptions, lợi ích kỳ vọng, failure evidence và ledger IDs liên quan. Bảng là các test cần thiết kế, chưa phải test đã chạy. Mọi ứng viên phụ thuộc định nghĩa concept và source observations hợp lệ tại cutoff. Bằng chứng chỉ đủ retrospective không làm E3 đạt.

## So sánh và bàn giao D08

Dùng expected results độc lập cho tăng, giảm, ổn định, zero/missing, duplicate/revision và future-dated cases. So sánh ảnh hưởng của corpus growth, coverage, alias, query/sampling và publication delay. Quy định cách dùng development/holdout theo [case protocol](03_CASE_SELECTION_PROTOCOL.md); giữ negative findings và không tuning trên holdout.

Sau khi B xác minh field và time semantics khả thi, đề xuất một chỉ báo chính; chỉ thêm chỉ báo thứ hai khi có thông tin bổ sung đã được chứng minh. Đề xuất D08 phải có construct, formula/unit/denominator chính xác, bin/window, cutoff, minimum support, nhãn hoặc insufficient-evidence behavior, cách tạo reference label, quality threshold và sensitivity protocol. Trích literature cùng empirical artifacts hỗ trợ và ghi uncertainty chưa giải quyết. Tài liệu này chưa freeze các lựa chọn đó; cần human acceptance trước implementation/evaluation phụ thuộc.
