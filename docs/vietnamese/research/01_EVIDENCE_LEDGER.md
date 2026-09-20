# 01 — Sổ bằng chứng

**Trạng thái:** đã có format ghi nhận; chưa ghi finding literature mới hoặc phép đo provider. [Prior-art map](../master/03_PRIOR_ART_MAP.md) vẫn là nguồn cho phạm vi kiểm tra giới hạn ngày 18/09. Không nâng các lần kiểm tra đó thành full-text review mới.

## Bản ghi claim

Mỗi claim quan trọng có một bản ghi và ID ổn định, ví dụ `EL-001`. Nhiều claim có thể cùng nguồn; chúng không phải các nghiên cứu độc lập. Ghi rõ `unknown`, `not inspected` hoặc `not applicable` thay vì suy diễn phần thiếu.

| Field | Nội dung bắt buộc |
| --- | --- |
| Source/version/location | Tiêu đề, tác giả/tổ chức, năm, DOI/URL, phiên bản, section/page/table; ngày và mức độ đọc |
| Claim | Phát biểu hẹp thực sự được hỗ trợ hoặc phản bác |
| Evidence type | Empirical / theoretical / benchmark / design / opinion |
| Population và period | Domain, dataset, đơn vị và thời kỳ được nghiên cứu |
| Method | Phương pháp, phép so sánh và giả định liên quan |
| Directness | Bằng chứng đã đọc trực tiếp hay suy luận/trích dẫn gián tiếp |
| Limitations | Bias, confounders, thông tin thiếu, giới hạn truy cập và áp dụng |
| SITES relevance | RQ, D07/D08 hoặc kiểm chứng D05; work package A/B |
| Status | supports / contradicts / mixed / unresolved đối với claim được nêu |
| Provenance | Search-record ID, người trích xuất, artifact/snapshot nếu có và các lần sửa bản ghi |

Với bản ghi dài, dùng bảng hai cột dưới claim ID thay vì bảng quá rộng. Hai bản ngôn ngữ dùng cùng ID và giữ đúng ý nghĩa kỹ thuật.

## Bản ghi tìm kiếm và loại nguồn

Mỗi search record giữ dịch vụ, query chính xác, ngày, bộ lọc, trang/kết quả đã sàng lọc, source IDs liên quan và giới hạn. Mỗi mục bị loại giữ nguồn/phiên bản và lý do. Phân biệt phiên bản trùng với bằng chứng độc lập. Giữ hiển thị kết quả mâu thuẫn và nguồn không truy cập được.

## Nguồn gợi ý đã có — chưa phải finding mới trong ledger

| Nguồn từ prior-art map | Giới hạn đọc đã ghi nhận | Việc tiếp theo |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015) | Chỉ abstract; chưa critical review toàn bài | A: đọc toàn bài trước khi mở rộng claim được hỗ trợ |
| Kleinberg (2002) | Đã kiểm tra trang mô tả của tác giả và paper; chưa có thí nghiệm SITES | A: trích assumptions và so sánh baseline đơn giản hơn |
| Sandve et al. (2013) | Đã kiểm tra các rule liên quan; chưa có thí nghiệm SITES | A+B: nối rule với bằng chứng trace/replay, không claim đã triển khai |

Không tự điền population thực nghiệm, vị trí chính xác trong paper hoặc finding mới cho các nguồn gợi ý. Chỉ tạo claim record sau khi đọc nguồn liên quan và giữ nguyên giới hạn truy cập. Số nguồn hoặc bảng đã điền không chứng minh corpus phù hợp và không làm Research Gate đạt.
