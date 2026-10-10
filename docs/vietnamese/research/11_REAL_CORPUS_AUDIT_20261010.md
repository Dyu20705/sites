# 11 — Audit corpus thật Issue #65, 10/10/2026

**VERIFIED:** AM-02 thành công; đã thu thập 598 work riêng biệt theo query hiện tại và đúng 598 bản v1. Có evidence field, identity, completeness và replay trên cùng host. **INSUFFICIENT EVIDENCE cho D07 as-of lịch sử; E3 và Research Exit #70 giữ NOT PASSED.** D07/D08/D09 giữ PROPOSED. Đây là handoff B → A tại local, không phải đóng issue hoặc acceptance của chủ dự án.

## 01. Experiment identity và preregistration

[RE-20260927-01](../../../experiments/research_exit_20260927/preregistration.json), [20261010-development-01](../../../experiments/research_exit_20260927/runs/20261010-development-01/acquisition.json). Query: `cat:cs.SE AND submittedDate:[201901010000 TO 201906302359]`; submission date tăng dần; page size 500; bound 2.000 works; cutoff `2019-06-30T23:59:59Z`. Chỉ development tháng 01–06. Giữ nguyên query, concept, cutoff và bytes contract gốc. Không chạy query/evaluation holdout tháng 07–12. Các ID tháng sau do query submission-date trả về là exposure của query development; phải đối soát overlap trước một lần freeze holdout sau này.

Baseline đầu phiên: `3c23a44ce0f11e243b0e0ecafef2faa93866d123`, đúng nhánh, working tree ban đầu sạch; fetch xác nhận ahead/behind đều 0. Python 3.14.7, chỉ standard library. [Preflight](../../../experiments/research_exit_20260927/runs/20261010-preflight-01/preflight.json), [khai báo run](../../../experiments/research_exit_20260927/runs/20261010-preflight-01/development-plan.json), [contract nghiệm thu offline](../../../experiments/research_exit_20260927/runs/20261010-preflight-01/offline-audit-contract.json). Config SHA-256: `f4ed7d7bca9c9665a9cb03437c79306f282e15ebb5ad9520bf6126deff61f1f7`.

## 02. Source access / AM-02

DNS và TCP 80/443 trên host thành công. TCP EACCES trong sandbox là giới hạn môi trường, không phải evidence provider. Một [count request AM-02](../../../experiments/research_exit_20260927/http-endpoint-diagnostic/acquisition.json) logic nhận HTTP 301 từ HTTP sang HTTPS rồi HTTP 200 `application/atom+xml; charset=utf-8`. Redirect tạo hai HTTP exchanges, cách nhau 3,1 giây. Đã xác minh Atom, một entry và totalResults=598. [Raw response](../../../experiments/research_exit_20260927/http-endpoint-diagnostic/raw/count.xml): 2.910 bytes, SHA-256 `5bbdec306856327b4bd5ae2892c9b08c4fefa6dedd1185f43975278863cdc80f`. Hash script AM-02: `331e07aeff70096fea36c877a8e226e2434431514fe4f910ac93a2316855c9bc`, local commit `d8e330b`.

Giữ nguyên hai manifest HTTPS 406 cũ. Thành công hôm nay không xác định nguyên nhân lỗi lịch sử; HTTPS là final path thành công hôm nay. Diagnostic đã ghi redirects, final URL và error excerpt có hash, giới hạn 2.048 bytes. Đọc lại [manual](https://info.arxiv.org/help/api/user-manual.html) và [terms](https://info.arxiv.org/help/api/tou.html) ngày 10/10: descriptive metadata CC0; request tuần tự, cách ít nhất ba giây. Không tải PDF.

## 03. Bounded corpus acquisition

[Acquisition](../../../experiments/research_exit_20260927/runs/20261010-development-01/acquisition.json): 11:27:47–11:28:24 UTC, tương ứng 18:27:47–18:28:24 Asia/Bangkok. Chín HTTPS responses tuần tự: một count, hai trang current (500/98), sáu batch v1 (100/100/100/100/100/98). Total query hiện tại giữ 598. Đã xác minh checksum và byte count của toàn bộ raw. Hash script: `cf46527ec6b034afad7d531cb50ffc799ca5accc6ef959694a90fc16e0d4d5e9`; freeze bytes code/config/AM-02 dưới [inputs](../../../experiments/research_exit_20260927/runs/20261010-development-01/inputs/acquire.py). Run phải dùng thư mục mới; raw không được ghi đè.

## 04. Field mapping và fitness

[Normalized records](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-1/normalized-records.json) giữ work_id, version_id cụ thể, title/category v1 và current, published/updated, acquisition timestamp từng request, raw file/entry-index/entry-ID/checksum và validation statuses. `available_at=null`; availability còn unresolved. [Manual](https://info.arxiv.org/help/api/user-manual.html) định nghĩa published là submission của v1 và updated là submission của version được lấy. Cả hai không tự động là public availability.

Các field đã kiểm tra: work_id, version_id, title_v1, published_at, updated_at, categories_v1, categories_current. Date phải parse có timezone; update không được trước publication. Category validation chỉ kiểm tra term không rỗng, không xác minh taxonomy độc lập. Identity/v1/completeness fail closed trước normalization. Mọi record có provenance. Có field trong schema không chứng minh semantic accuracy hoặc tính đại diện.

## 05. Missingness / invalidity theo tháng UTC

| Tháng | Inspected / distinct | Missing title | Missing dates | Invalid dates | Missing categories | Unresolved v1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2019-01 | 91 / 91 | 0 | 0 | 0 | 0 | 0 |
| 2019-02 | 79 / 79 | 0 | 0 | 0 | 0 | 0 |
| 2019-03 | 97 / 97 | 0 | 0 | 0 | 0 | 0 |
| 2019-04 | 103 / 103 | 0 | 0 | 0 | 0 | 0 |
| 2019-05 | 122 / 122 | 0 | 0 | 0 | 0 | 0 |
| 2019-06 | 106 / 106 | 0 | 0 | 0 | 0 | 0 |

[Audit JSON](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-1/audit.json) tách missing/invalid counts, inspected denominators và rates cho từng field/bin. Bảy field đều 0 missing và 0 invalid ở sáu tháng: 0% thực đo, không phải chưa đo. Missing title không chuyển thành nonmatch. Historical availability unresolved 598/598, tách riêng khỏi metadata missingness.

## 06. Work identity và revisions

Không trùng current work ID; nhận đúng toàn bộ v1 đã yêu cầu. 161 current IDs là v2 trở lên; 55 title khác, bốn bộ category khác, không có published-date conflict. Chỉ quan sát current/v1, không lấy intermediate history. Ví dụ: title 1901.02633 khác giữa v1/current v2. Category thay đổi ở 1901.07910, 1902.10056, 1903.07712, 1904.08337. Truy nguyên mỗi khác biệt bằng source_ref. Mỗi work đóng góp một lần. 112 current update timestamps sau cutoff; không được thay metadata tại cutoff bằng metadata hiện tại một cách âm thầm.

## 07. Denominator completeness

Đã xác minh completeness của query hiện tại qua query/sort settings, startIndex/itemsPerPage, offsets liên tục, counts đúng, distinct IDs, population current/v1 khớp và hashes. Denominators hồi cứu: 91/79/97/103/122/106. Toàn bộ 598 work eligible trong corpus current-category hồi cứu đã khai báo; không phải loại record nào. Không lọc theo concept; giữ cả nonmatches. Điều này không liệt kê được work đã bị loại khỏi cs.SE hiện tại. As-of denominators và shares giữ null; chưa tính real signal hoặc trend labels.

## 08. Historical cutoff / availability matrix

| Thành phần tại T | Evidence | Kết luận |
| --- | --- | --- |
| Public availability | Submission trước T; chín IDs mang tháng 07/08 | Unresolved / counterevidence cho submission = public availability |
| v1 title | Bytes v1 cụ thể lấy năm 2026 | Xác minh version content; chưa có timestamp độc lập chứng minh public tại T |
| Category | Sets current/v1; bốn khác biệt | Đo tập trả về; population lịch sử unresolved |
| Vocabulary | Survey trước cutoff trong preregistration | Chưa freeze/accept availability của alias/rule cụ thể và reference protocol |
| Denominator membership | Query hiện tại đầy đủ | Historical completeness unresolved |
| Source state | XML/code/config/hashes freeze năm 2026 | Replay offline được; không phải snapshot năm 2019 |

[Cross-check XML trực tiếp](../../../experiments/research_exit_20260927/runs/20261010-development-01/crosscheck.json) liệt kê chín IDs có tháng ID sau tháng 06 nhưng published trước T. Ví dụ: 1908.04451 có `2019-03-07T08:37:23Z`. [Policy chính thức](https://info.arxiv.org/help/availability.html) gán ID theo tháng first announcement và phân biệt submission với public posting. **INFERENCE:** áp dụng policy được mô tả này cho các ID là counterevidence đối với việc coi mọi work trả về đã public tại T; exact historical announcement timestamps vẫn chưa được xác minh. Không trừ chín work rồi claim denominator lịch sử đã được sửa. [OAI datestamp](https://info.arxiv.org/help/oa/index.html) là lần sửa metadata cuối, không phải original submission/public availability. Không gọi OAI. **E3 NOT PASSED.**

## 09. Frozen input và replay

Hai tiến trình Python riêng cho audit.json giống hệt bytes (SHA-256 `53a5aff1d8ea577e5789c7dc96a784f9f3c46339495e38ea78d266b41158dbd8`) và normalized-records.json (`a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1`): [verification](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-verification.json). Chỉ same-host replay, chưa có independent human replay. Parser XML trực tiếp riêng đối soát 598 records, chín hashes, monthly counts và source references, không import acquisition/audit parsers.

17 unit tests của công cụ và 15 synthetic checks hiện có đạt. Synthetic output vẫn mô tả hai access manifests cũ; real_sample status của nó không mô tả corpus mới. Evidence corpus thật nằm trong audit.json/crosscheck.json. Package checks ghi riêng ở package-validation.json dưới run. Các checks này không chứng minh E1–E8 sản phẩm.

Replay từ repo root vào thư mục mới:

```powershell
py -3 experiments/research_exit_20260927/offline_audit.py --run experiments/research_exit_20260927/runs/20261010-development-01 --output experiments/research_exit_20260927/runs/20261010-development-01/reviewer-replay
py -3 -m unittest discover -s experiments/research_exit_20260927 -p "test_*.py" -v
```

Không ghi đè run hoặc replay directory. Audit offline không gọi API.

## 10. Bias, limitations và unresolved claims

cs.SE không phải toàn bộ literature software testing. Live query state không phải atomic snapshot toàn provider dù counts/pages quan sát nhất quán. Withdrawal/reclassification/removal và announcement delays ảnh hưởng membership. Zero missingness chỉ áp dụng cho records trả về và syntactic checks. Chưa có field annotations độc lập, real signal comparison, reference labels, accepted threshold, product demo, benchmark hoặc user validation. Tái lập năm 2026 không chứng minh tính hợp lệ tại cutoff 2019.

## 11. B → A handoff (#64)

A có thể đọc v1 titles, population hồi cứu thực đo và mọi raw reference. Lexical pattern chỉ được kiểm tra trên title giả, chưa chạy thành corpus signal. Trước D08/freeze cần xử lý temporal/membership gaps, development/holdout overlap từ late ID months, vocabulary version và reference/quality protocol độc lập. Phép thử phân biệt tiếp theo: tìm bounded dated category/announcement snapshot bao phủ T, bắt đầu từ chín IDs mâu thuẫn; preregister query/transfer budget/checksums trước acquisition mới. OAI datestamp hiện tại không đủ. Đổi provider hoặc độ phân giải thời gian cần proposal/preregistration riêng.

## 12. PROPOSED D07 / insufficient evidence

**PROPOSED:** giữ arXiv là ứng viên khả thi cho bounded retrospective corpus; chưa accept làm corpus as-of 2019. Alternatives: tìm evidence membership/public availability có ngày; đề xuất scope retrospective-only với chủ dự án; hoặc preregister historical DBLP tương thích (tháng 04 riêng lẻ không bao phủ sáu tháng). Khuyến nghị giữ run này và khảo sát historical evidence trước product/holdout phụ thuộc. Gói historical field/membership/vocabulary đầy đủ sẽ bác bỏ kết luận thiếu bằng chứng hiện tại. D07/D08/freeze cần chủ dự án acceptance rõ tại #70; D09 là quyết định sau. Chưa đóng issue, accept gate, merge/release/deploy.
