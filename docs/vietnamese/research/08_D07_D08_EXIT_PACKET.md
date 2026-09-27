# 08 — Gói quyết định D07/D08 và review Research Exit

**PROPOSED — 27/09/2026. Khuyến nghị: giữ #70 NOT PASSED.** Gói này có thể review như một kết quả thiếu bằng chứng; **chưa** sẵn sàng chấp thuận thành experiment contract đã freeze. D05/D06 giữ ACCEPTED; D07/D08/D09 giữ PROPOSED.

## D07 — Domain/source/corpus

**Mục tiêu:** một corpus học thuật tái lập được, hợp lệ tại cutoff cho nhiệm vụ researcher đã chốt, một nguồn, ≤5.000 works, ≤24 tháng đã kết thúc.

**Ứng viên khảo sát:** software engineering/testing, arXiv `cat:cs.SE`, development 01–06/2019, candidate holdout 07–12/2019, work ID riêng biệt và title version đầu. Acquisition sáu tháng có bound chặt hơn là 2.000 works. Query membership hiện dựa category index hôm nay, còn rủi ro membership lịch sử chưa giải quyết. Không suy rộng thành toàn bộ literature software testing.

**Bằng chứng:** [EL-101–105 và access logs](07_PROVIDER_AUDIT_RESULTS.md). Hai request arXiv không trả records, nhưng cả hai dùng HTTPS trong khi manual đã đọc trình bày endpoint query qua HTTP; vì vậy hai 406 bị confound bởi endpoint. Probe DBLP đường legacy trước đó reset, còn snapshot tháng 04/2019 có DOI trên DROPS hiện đã được xác minh ở mức metadata artifact. Chưa audit bounded extract. Chưa xác lập missingness, counts, membership tại cutoff hay input snapshot.

**Alternatives và trade-offs:**

1. Chạy đúng một request AM-02 tới endpoint HTTP trong arXiv manual đã đọc và ghi redirect/final URL/status. Nếu truy cập thành công, đo version/membership/announcement fitness. Đây là sửa đổi nhỏ nhất của khảo sát; temporal evidence vẫn có thể fail sau đó.
2. Preregister bounded venue/domain extract từ snapshot DBLP đã xác minh `10.4230/dblp.xml.2019-04-01`. Danh tính snapshot/license/checksum file đã có bằng chứng, nhưng upstream transfer/scan 468,04 MB và độ chính xác thời gian thô hơn vẫn cần audit giới hạn riêng, không tự accept.
3. Metadata OpenAlex/Crossref/DBLP hiện tại cho retrospective analysis. Có thể hỗ trợ exploration nhưng tự nó không đáp ứng E3 giữ nguyên. Historical download Semantic Scholar cũng cần key chưa có.

**Khuyến nghị:** chưa chọn provider cuối cùng hay freeze corpus. Giữ lỗi truy cập và chạy phép kiểm tra giới hạn tiếp theo trong provider report. Không có bằng chứng để kết luận mọi provider đều bất khả thi.

**Falsifier:** một extract được phép dùng, đầy đủ, ≤5.000 works, có coverage field cần thiết và bằng chứng field/vocabulary/membership tại T sẽ thay đổi kết quả thiếu bằng chứng hiện nay. HTTP thành công đơn lẻ chưa đủ.

**Acceptance cần sau này:** provider/domain/query/period cụ thể, temporal interpretation, inclusion/version/sampling, quyền chia sẻ và snapshot identity đã xác minh. Gói này không yêu cầu chủ dự án accept corpus còn thiếu.

## D08 — Chỉ báo/đánh giá

**Định nghĩa ứng viên, chưa accept:** với tháng b, C_b là tập works version đầu đủ điều kiện và M_c(w) là lexical match đã freeze. `N_b = |C_b|`, `n_cb = sum(M_c(w) for w in C_b)`, `p_cb = n_cb/N_b` khi N_b>0. Giữ n và N cạnh p. Input thiếu/không đầy đủ dẫn tới insufficient evidence, không phải zero. Count là comparator; share là ứng viên chính tạm thời.

**Bằng chứng:** [EL-001–005 và synthetic checks](06_RESEARCH_EXIT_EVIDENCE.md). Share loại hiệu ứng corpus tăng theo tỷ lệ trong null giả lập, nhưng không loại composition change, alias drift hay selection bias. Chưa chứng minh ưu thế thực nghiệm hoặc detection quality. Alternatives nghiêm túc là raw count, inflation-adjusted growth và burst; chưa chọn cho sản phẩm.

| Thành phần contract | Đề xuất hiện tại / bằng chứng thiếu |
| --- | --- |
| Unit/text | Work riêng biệt; title version đầu. Không biến title thiếu thành nonmatch. |
| Vocabulary | Pattern fuzzing khảo sát trong preregistration; chưa xác minh tính đầy đủ/mọi biến thể lịch sử. |
| Time | Bin tháng submission; candidate cutoff 2019-06-30T23:59:59Z. Phải chứng minh availability riêng. |
| Support/labels | **UNRESOLVED**. Chưa xuất growing/stable/declining/emerging. Cần corpus để biện minh support/abstention. |
| Case/control | Fuzzing từ context độc lập năm 2018; synthetic constant-share null. Context không phải reference trend label. |
| Reference protocol | **PROPOSED:** reviewer do chủ dự án chỉ định gán concept relevance từ evidence được phép, không xem candidate outputs; lưu uncertainty/disagreement. Chưa xác nhận có researcher/annotator tham gia. |
| Quality threshold | **UNRESOLVED**. Lexical agreement không phải trend validity; không tự đặt precision target hay dùng công thức làm reference cho chính nó. |
| Sensitivity | **PROPOSED dimensions:** tháng so với gộp hai tháng liền kề; từ “fuzzing” chính xác so với variants; cách xử lý field thiếu khai báo trước. Support/threshold ranges chờ development evidence. |
| Holdout | Candidate 07–12/2019; chưa xem, chưa lấy hay chạy. Chưa freeze hoặc claim confirmatory. |

**Khuyến nghị:** giữ count/share làm baseline exploration nhỏ nhất; hoàn thiện data fitness thực đo và rubric độc lập trước acceptance. Không code burst để bù thiếu dữ liệu. Giữ negative outcomes.

**Falsifier:** nếu corpus giới hạn không hỗ trợ denominator độc lập, lexical relevance hoặc diễn giải ổn định qua sensitivity đã khai báo, thu hẹp construct hoặc bác bỏ ứng viên. Không hạ threshold sau holdout.

**Acceptance cần sau này:** formula/unit/window/vocabulary/support/labels đầy đủ, case/reference protocol, quality threshold, sensitivity ranges bằng số và development/holdout split chính xác. Chấp thuận kế hoạch khảo sát không phải chấp thuận các giá trị chưa biết này.

## Freeze record — chủ ý NOT FROZEN

`RE-20260927-01` là **audit preregistration**, không phải evaluation freeze M1. Freeze sau này phải có corpus/raw hashes, query/snapshot, case/control, period/cutoff, vocabulary version, formula/unit/denominator, support, reference rubric/threshold, sensitivity values, exposure log, code/config/environment và người/ngày chấp thuận. Các giá trị thiếu phía trên ngăn freeze. Không ghi đè preregistration để che lỗi truy cập.

## Gate checklist và review findings

| Kiểm tra | Trạng thái / bằng chứng |
| --- | --- |
| D05/D06 và Research Entry | PASS — decision log và #68 đã có; không mở lại |
| Protocol giới hạn, search log, construct/alternative notes | PRESENT — coverage có trọng tâm; không claim literature toàn diện |
| Sample/denominator/field fitness thực đo | **BLOCKER — còn thiếu** |
| Historical availability, membership, vocabulary | **BLOCKER — chưa xác minh; E3 NOT PASSED** |
| Development signal comparison và support/quality justification | **BLOCKER — chưa có input thật** |
| Case/reference rubric độc lập, quality threshold frozen | **BLOCKER — chưa hoàn tất** |
| Synthetic arithmetic, duplicate/version/cutoff/lineage | 15 methods đạt ở mỗi lần chạy trong hai tiến trình; chỉ evidence local |
| D07/D08 acceptance và experiment freeze có version | NOT DONE |
| Holdout/product/user validation | NOT RUN; thuộc sau các gate cần thiết |

Tự review theo `sites-review`: đọc docs thay đổi, hành vi script/fixture, acquisition manifests, replay output và đối chiếu trạng thái/ID Việt–Anh. Chưa có independent human review. Mechanical checks và giới hạn nằm trong experiment README; không claim toàn bộ E1–E8 sản phẩm đã đạt.

**Xử lý:** chuẩn bị draft PR bàn giao evidence; không tự merge hoặc đóng #64/#65/#70. Đã đi tới nhánh thiếu bằng chứng trong kế hoạch, nên D09/build phụ thuộc vẫn bị chặn. Chủ dự án có thể review kết quả này mà không accept D07/D08.

## Hệ quả lịch

Giữ deadline M1 17/10. Lịch tăng tốc D09 ngày 28/09, build 29/09–02/10, demo 03–05/10 vẫn phụ thuộc Research Exit. Ngày đến không làm gate đạt. WIP tối đa hai; các hướng mới chờ quyết định gate của slice hiện tại.
