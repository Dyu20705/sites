# 13 — Phản hồi review Issue #65 và handoff B → A

**Outcome investigation đề xuất: INSUFFICIENT EVIDENCE.** Corpus và historical screen đã review có thể kiểm tra; population lịch sử còn unresolved. Đóng investigation #65 là quyết định owner riêng với acceptance D07 hoặc pass #70. Phản hồi này chưa cho phép đóng issue hoặc đổi scope.

## 01. Findings và disposition

| Finding | Disposition |
| --- | --- |
| P0: chưa tái dựng được population lịch sử | Giữ blocker khoa học; denominator/share lịch sử null; E3 NOT PASSED |
| P1: search log thiếu execution metadata | Ghi nhận; chuẩn bị template cho lần sau, chưa thực thi |
| P1: A chưa acknowledgment handoff B | [Đã gửi handoff sang #64](https://github.com/Dyu20705/sites/issues/64#issuecomment-6097343828); acknowledgment còn pending |
| P2: preregistration thiếu bằng chứng thời gian độc lập | Giữ limitation; plan confirmatory sau cần commit trước execution hoặc timestamped immutable record |

Review chưa phát hiện defect code nghiêm trọng mới. Không sửa parser, acquisition, thử lại trang abstract, tính signal hoặc xem holdout. [Review-response record](../../../experiments/research_exit_20260927/runs/20261010-review-response-01/review-response.json) ghi rõ các mục unresolved.

## 02. Provenance search và preregistration

[Search log gốc](../../../experiments/research_exit_20260927/runs/20261010-historical-screen-01/source-screen-results.json) giữ bốn query và phân biệt exploratory/preregistered. Nó thiếu committed record đầy đủ về service, exact execution timestamps, filters, số kết quả đã screen và URL từng kết quả. Thiếu hụt này hạn chế việc tái dựng search độc lập; không chứng minh archive lịch sử không tồn tại. Không tự tạo hoặc backdate metadata còn thiếu.

Timestamp local của plan và thứ tự execution do agent ghi nhận chưa chứng minh độc lập rằng plan tồn tại trước exposure. Plan và results được push cùng nhau sau execution. Đây là giới hạn provenance, chưa phải bằng chứng vi phạm protocol hoặc confirmatory acceptance.

[Template search execution cho lần sau](../../../experiments/research_exit_20260927/runs/20261010-review-response-01/future-search-execution-template.json) giữ **TEMPLATE_NOT_EXECUTED**. Tại lần screen thực tế tiếp theo, ghi service/tool, timestamps UTC bắt đầu/kết thúc, query chính xác, mọi filters, counts returned/screened/opened và URL/disposition/access depth/source location từng kết quả. Phân biệt count unavailable với zero và filter unknown với không dùng filter. Giữ response/capture references được phép và checksums nếu có capture. Search ranking vẫn có thể đổi; metadata đầy đủ giúp audit nhưng không bảo đảm kết quả tương lai giống hệt.

Trước confirmatory exposure, commit plan đầy đủ trước execution hoặc dùng timestamped immutable record; ghi freeze reference và timing evidence. Ưu tiên time anchor độc lập. Push sau execution không chứng minh ngược lại timing đó. D07/D08 và experiment freeze được owner chấp thuận vẫn phải có trước holdout.

## 03. Đã gửi handoff, chờ acknowledgment

Comment #64 dẫn corpus audit, normalized records, missingness/revisions, raw anomaly references, temporal limitations và replay verification tại commit cố định. A có thể kiểm tra 598 work riêng biệt với đúng version v1 và retrospective denominators theo tháng 91/79/97/103/122/106. Bảy core fields không missing/invalid dưới syntactic checks đã khai báo; 161 current versions v2+, 55 title khác và bốn bộ category khác.

Đối với D08 as-of, `published_at`/`updated_at` là submission times, chưa phải first-public times đã xác minh. `available_at` null ở 598/598; membership và denominator lịch sử unresolved. Titles/categories có version lấy năm 2026 chưa chứng minh knowability tại T. Chín anomaly ID tháng 07/08 và exposure của development query cần đối soát trước holdout freeze. Vocabulary, reference rubric, support/quality threshold và signal chưa được accept hoặc đo bởi handoff này.

Đã yêu cầu A xác nhận nhận dữ liệu và ghi fields/denominators không phù hợp D08 as-of, requirements còn thiếu hoặc điều kiện cho retrospective-only proposal. Gửi comment từ B chưa phải acknowledgment của A; không tạo acknowledgment giả tại đây.

## 04. Gói owner review cụ thể

[Corpus audit](11_REAL_CORPUS_AUDIT_20261010.md) và [historical screen](12_HISTORICAL_AVAILABILITY_SCREEN_20261010.md) hỗ trợ hai quyết định riêng:

1. **Disposition investigation:** chấp thuận báo cáo insufficient-evidence của #65 để nghiệm thu investigation sau A acknowledgment, hoặc yêu cầu thêm bounded historical-capture test. #65 giữ OPEN đến khi đủ điều kiện và có chỉ thị rõ của owner cho phép đóng.
2. **Research scope tại #70:** tiếp tục historical as-of reconstruction, hoặc yêu cầu scope proposal retrospective-only có kiểm soát. Chọn chuẩn bị proposal chưa accept corpus/protocol của nó, chưa làm E3 pass hoặc cho phép implementation phụ thuộc.

Nếu tiếp tục historical reconstruction, phép thử tiếp theo phụ thuộc nguồn: trước hết xác định dated category/announcement capture cụ thể có provenance và coverage, rồi preregister request/byte bounds và reconcile cả anomalies đã biết lẫn membership độc lập với current positives. Screen trước chưa tìm được capture phù hợp nên chưa chọn acquisition parameters cụ thể. Mở thêm trang abstract riêng lẻ không trả lời population completeness.

D07/D08/D09 giữ PROPOSED; #70 giữ NOT PASSED. Owner review và A acknowledgment còn pending. Validation phản hồi này gồm links tài liệu, parse JSON và gate statuses giữ nguyên; 17 tests/replay trước là evidence đã có, chưa phải checks mới chạy lại.
