# 12 — Replay theo review và screen nguồn lịch sử Issue #65

**VERIFIED:** replay local và đối chiếu XML trực tiếp theo yêu cầu đều pass tại baseline `670bcee8bc0f5a8883ff56979666fb614a1b5d44`. **INSUFFICIENT EVIDENCE:** screen nguồn lịch sử có giới hạn chưa xác định first-public timestamps hoặc toàn bộ population cs.SE lịch sử. E3 và Research Exit #70 giữ NOT PASSED; D07–D09 giữ PROPOSED.

## 01. Phản hồi review và kiểm chứng local

Thực hiện theo [checkpoint review độc lập](https://github.com/Dyu20705/sites/issues/65#issuecomment-6097198637). Working tree sạch trước fetch; đúng nhánh và khớp origin; `pull --ff-only` báo đã cập nhật. Cả 17 unit tests của công cụ pass trong 0,281 giây. Chưa chứng minh defect parser; không sửa code acquisition/audit.

[Replay mới](../../../experiments/research_exit_20260927/runs/20261010-development-01/reviewer-replay-20261010-115331/verification.json) kiểm tra 14 frozen manifest/config/code/raw inputs và tái tạo đúng bytes gốc:

| Artifact | SHA-256 |
| --- | --- |
| audit.json | `53a5aff1d8ea577e5789c7dc96a784f9f3c46339495e38ea78d266b41158dbd8` |
| normalized-records.json | `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1` |
| crosscheck.json | `0664d7dcd1ad3d1fd570696b47b254ce54329ffcc56c9b6416482830379c6591` |

Parser XML trực tiếp riêng kiểm tra lại toàn bộ 598 records và chín raw-file hashes. Output cũng khớp bytes gốc. Đây là lần chạy mới do agent thực hiện trên host producer, chưa phải independent human hoặc second-machine replay. Giữ nguyên run và frozen inputs cũ. [Audit corpus](11_REAL_CORPUS_AUDIT_20261010.md) vẫn là báo cáo acquisition thực đo.

## 02. Screen lịch sử có giới hạn

[Plan HA-20261010-01](../../../experiments/research_exit_20260927/runs/20261010-historical-screen-01/source-screen-plan.json) được ghi trước khi mở chín trang record. Các lần tìm tài liệu thăm dò trước đó được tách rõ trong [results/search log](../../../experiments/research_exit_20260927/runs/20261010-historical-screen-01/source-screen-results.json). Screen thử mỗi trang abstract chính thức một lần, đọc bảy trang hướng dẫn chính thức và dùng tổng cộng bốn query tìm kiếm có trọng tâm. Không harvest API/OAI, acquisition lại corpus, tải PDF hoặc query holdout.

| Trang record chính thức | Submission v1 đã freeze (UTC) | Tháng ID | Quan sát trang |
| --- | --- | --- | --- |
| [1907.00143](https://arxiv.org/abs/1907.00143) | 2019-06-29 04:32:14 | Tháng 07 | Submission v1 khớp |
| [1907.00172](https://arxiv.org/abs/1907.00172) | 2019-06-29 09:37:34 | Tháng 07 | Submission v1 khớp |
| [1907.00282](https://arxiv.org/abs/1907.00282) | 2019-06-29 21:39:03 | Tháng 07 | Submission v1 khớp |
| [1907.00298](https://arxiv.org/abs/1907.00298) | 2019-06-29 23:53:22 | Tháng 07 | Submission v1 khớp |
| [1907.00376](https://arxiv.org/abs/1907.00376) | 2019-06-30 13:04:27 | Tháng 07 | Submission v1 khớp |
| [1907.00468](https://arxiv.org/abs/1907.00468) | 2019-06-30 21:29:48 | Tháng 07 | Submission v1 khớp |
| [1907.00677](https://arxiv.org/abs/1907.00677) | 2019-06-28 07:21:51 | Tháng 07 | Submission v1 khớp |
| [1907.03773](https://arxiv.org/abs/1907.03773) | 2019-06-27 18:44:14 | Tháng 07 | Submission v1 khớp |
| [1908.04451](https://arxiv.org/abs/1908.04451) | 2019-03-07 08:37:23 | Tháng 08 | Web reader cache miss; chưa xác minh trang |

Tám trang đọc được xác nhận submission timestamps và hiển thị Subjects hiện tại. Chúng chưa cung cấp exact first-announcement timestamp hoặc timeline category membership đã xác minh. Lỗi trang thứ chín là quan sát truy cập của công cụ, không chứng minh work không tồn tại. Web reader có thể trả bản cache; chưa capture/hash raw HTML hoặc claim response mới từ provider. Exact announcement timestamps và membership tại cutoff của cả chín work giữ null.

## 03. Fitness của nguồn cho toàn bộ population

| Nguồn | Semantics đã đọc | Fitness lịch sử |
| --- | --- | --- |
| [Availability policy](https://info.arxiv.org/help/availability.html) | Tháng ID theo first announcement, có thể khác submission | INFERENCE: ID tháng 07/08 phản bác eligibility theo submission tại cutoff tháng 06; chưa suy ra exact event time năm 2019 |
| [Identifier policy](https://info.arxiv.org/help/arxiv_identifier.html), [cross-list policy](https://info.arxiv.org/help/cross.html) | ID không chứa phân loại; membership có thể đổi | Liệt kê ID không khôi phục membership cs.SE lịch sử |
| [Tài liệu OAI](https://info.arxiv.org/help/oa/index.html) | Metadata item mới nhất; arXivRaw có version history; datestamp là lần sửa metadata cuối | `until=2019-06-30` trên live harvest không phải snapshot trạng thái lúc đó |
| [API manual](https://info.arxiv.org/help/api/user-manual.html) | Published/updated là ngày submission của version | Lấy đúng v1 chưa chứng minh public availability lịch sử |
| [RSS](https://info.arxiv.org/help/rss.html), [bulk access](https://info.arxiv.org/help/bulk_data.html) | Daily feeds và đường metadata/full-text hiện tại | Screen chưa xác minh capture năm 2019 có ngày, coverage membership và checksums phù hợp |

Đây là tài liệu hiện tại, không phải policy hoặc event ledger năm 2019 đã freeze. Tìm kiếm chưa xác minh snapshot lịch sử tương thích; không chứng minh snapshot đó không tồn tại. Chưa audit inventory archive bên thứ ba, log nội bộ provider hoặc bộ email lịch sử.

Denominator 598 đầy đủ cho query năm 2026. Nó không xác định work bị loại khỏi cs.SE trước query đó hoặc lúc cross-list hiện tại được thêm. Giải quyết chín trường hợp dương tính, trừ chín, hoặc so categories current/v1 không tìm ra những members vắng mặt này. Số lượng của chúng **unknown**, không phải zero. Denominator/share lịch sử và vocabulary validity vẫn unresolved.

## 04. Quyết định owner PROPOSED và phép kiểm tra tiếp theo

**Khuyến nghị:** giữ corpus frozen làm evidence hồi cứu và tiếp tục chặn claim as-of. Hai phương án chờ owner review rõ ràng:

1. Tiếp tục tìm evidence lịch sử. Trước transfer corpus khác, xác định một capture announcement/category có ngày, semantics timestamps, capture provenance, license/access constraints, coverage và checksum bất biến. Phép kiểm tra có giới hạn tiếp theo cần xác minh chín anomaly **và** liệt kê membership độc lập với các positives cs.SE năm 2026, bao gồm removals/additions. Snapshot tại cutoff còn cần đủ history cho các trạng thái as-of theo tháng trước đó nếu có claim này. Preregister request/byte budget và reconciliation checks khi tìm được nguồn cụ thể. Dừng nếu nguồn không hỗ trợ coverage population.
2. Đề xuất mục tiêu retrospective-only với owner. Đổi estimand và claims cần acceptance rõ về scope/corpus/protocol; không biến phép thử E3 lịch sử hiện tại thành pass.

Chưa accept phương án nào tại đây. Screen chưa dẫn tới real signal, reference labels, threshold, freeze, đổi provider, implementation D09 hoặc đóng gate. [Checkpoint control #70 mới nhất](https://github.com/Dyu20705/sites/issues/70#issuecomment-6096887546) đặt demo-ready là 15/10/2026 (trước 16/10), thay mốc execution 17/10 cũ. Deadline không giải quyết khoảng trống evidence.

## 05. Phạm vi validation

Evidence tự động gồm 17 unit tests, replay mới, input hashes và cross-check XML raw trực tiếp. Package report kiểm tra relative links, parse JSON/Python và gate statuses hiện có; không xác minh external links, độ mới của trang cache hoặc completeness lịch sử. Đã self-review hai bản về counts, dates, null fields và trạng thái proposal. Không claim independent human replay hoặc historical ground truth.
