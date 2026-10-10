# 09 — Research Master và review Research Exit (10/10/2026)

**Trạng thái: đã tổng hợp evidence từ nguồn được kiểm tra; empirical Research Exit NOT PASSED.** Đây là cập nhật sau gói PR #75 ngày 27/09; không chấp thuận D07/D08, không tuyên bố novelty hoặc hoàn tất sản phẩm. Research Entry #68 PASSED; #70 là gate Research Exit có thẩm quyền. D05/D06 ACCEPTED; D07/D08/D09 PROPOSED; chưa dùng holdout.

## RQ, construct và claim boundary

M1 hỏi liệu 1–2 chỉ báo đơn giản có mô tả concept xuất hiện nhiều/ít hơn trong một scholarly corpus giới hạn, đồng thời truy nguyên được tập quan sát, công thức, cutoff và replay hay không.

Ứng viên: **lexical prevalence trong tiêu đề phiên bản đầu**. Với bin b: N_b là tổng số work riêng biệt đủ điều kiện (bao gồm không match), n_cb là số work có title match rule concept cố định, p_cb = n_cb / N_b nếu N_b > 0. Denominator không đầy đủ, title thiếu, membership hoặc availability lịch sử không chứng minh được → INSUFFICIENT EVIDENCE, không thay bằng zero. Phải hiển thị n và N bên cạnh p. Đây chưa phải công thức D08 đã freeze.

Được phép nói mức xuất hiện từ ngữ thay đổi trong population đã khai báo. Không suy ra emergence, conceptual novelty, importance, impact, adoption, causal effect hoặc dự báo. Timestamp publication cũ trong API hiện tại không chứng minh giá trị field đó đã tồn tại tại cutoff lịch sử.

## Prior art và ý nghĩa với SITES

| Nguồn và mức kiểm tra | Evidence có ích | Ranh giới áp dụng |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/html/1503.00673), mục 3–4 | Emergence đa chiều; frequency không tương đương emergence | Không chứng minh SITES |
| Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/bhs.pdf), mục 2/4 theo EL-002 | Burst là serious alternative | Chưa thử trên corpus SITES; thêm tham số |
| Sandve et al. (2013), [Ten Simple Rules](https://doi.org/10.1371/journal.pcbi.1003285), Rules 1–3 | Lưu input, workflow, parameters và versions để replay | Reproducibility không chứng minh kết luận đúng |
| Nelis et al. (2022), [General Growth Tendency](https://doi.org/10.1371/journal.pone.0268433), Introduction/Methods theo EL-004 | Corpus growth là confound; growth normalization là alternative | Khác population và công thức |
| Štimec et al. (2026), [Identifying and evaluating emerging scientific trends through temporal n-gram analysis](https://doi.org/10.1007/s11192-026-05744-5), HTML full text; xuất bản 30/09/2026 | N-gram OpenAlex, bin theo quý, Kleinberg/MACD, normalization và đánh giá con người đã được nghiên cứu | Tác giả nêu synonym fragmentation, disagreement và lexical burst không bằng novelty; không phải kết quả thực nghiệm của SITES |

**Cập nhật quan trọng:** paper ngày 30/09 có prior art rất gần. Không được claim “transparent lexical trend detection” là novelty. Hướng đóng góp **đề xuất** cho SITES là đo đạc và chứng minh temporal evidence, denominator, abstention, lineage và replay trong một corpus giới hạn; vẫn chưa chứng minh đây là research gap mới.

## Source audit — năm provider

Đọc documentation không phải đo field fitness thực.

- **arXiv:** manual có Atom API, version retrieval và ví dụ endpoint HTTP. Hai request HTTPS của PR #75 trả 406 nhưng bị confound bởi endpoint. AM-02 chưa có response thực mới. [OAI-PMH docs](https://info.arxiv.org/help/oa/index.html) mô tả arXivRaw có version history nhưng datestamp có thể phản ánh chỉnh sửa về sau, không phải submission time; OAI không hỗ trợ lọc theo submission date. Membership/announcement tại T còn UNKNOWN.
- **DBLP:** ba monthly snapshots chính thức có DOI và CC0: [01/04/2019](https://doi.org/10.4230/dblp.xml.2019-04-01), [01/07/2019](https://doi.org/10.4230/dblp.xml.2019-07-01), [01/01/2020](https://doi.org/10.4230/dblp.xml.2020-01-01). File tháng 04/2019 468,04 MB và MD5 công bố cdf6416c27ab24eaef5aa4560e38aa3c; chưa download/hash thực tế. Snapshot 04/2019 **không bao phủ toàn bộ 01–06/2019 và không thể chứa đầy đủ 07–12/2019 holdout**. Snapshot 07/2019 và 01/2020 là candidates, không tự đổi input đã preregister. DBLP chủ yếu có publication year: không được bịa độ chính xác theo tháng; cần phân biệt publication year với thời điểm index.
- **OpenAlex:** [snapshot docs](https://help.openalex.org/access/snapshot/) xác nhận cơ chế snapshot/bulk, nhưng snapshot hiện tại và record date không tự tái dựng metadata đúng tại T cũ; dữ liệu toàn bộ quá lớn so với M1.
- **Crossref:** tài liệu API/bulk có DOI và nhiều loại date; chưa đo state lịch sử hoặc bounded coverage.
- **Semantic Scholar:** có API và datasets theo release, nhưng quyền truy cập/phân phối và field history tại T còn chưa kiểm chứng trong dự án.

Snapshot là bằng chứng trạng thái của **database tại ngày release** nếu artifact được xác minh. Nó không chứng minh mọi work đã xuất hiện đúng publication date, không chứng minh completeness hoặc trạng thái field tại một cutoff khác.

## Evidence thực thi

- PR #75 ghi hai lượt chạy trước đây: 15 synthetic test methods đạt ở mỗi lượt trên cùng host; không claim chạy độc lập ở máy khác hay E1–E8 sản phẩm.
- Review mới 10/10: tính lại độc lập bảy series cases của fixture GitHub; **7/7 kết quả khớp expected arithmetic**. Không phải chạy lại 15 Python tests hay đánh giá detection ngoài thực tế.
- Một bounded arXiv HTTP request từ môi trường hiện tại dừng ở **DNS name resolution failure**, không nhận HTTP response; đây là lỗi môi trường, không kết luận service lỗi và không tạo AM-02 manifest.
- **Chưa thu corpus**, chưa đo missingness/denominator, chưa chạy comparison thực, annotation, holdout, demo hoặc user walkthrough.

## Research Gate #70

| Kiểm tra | Kết luận |
| --- | --- |
| R1 construct/claim | Đã có định nghĩa hẹp và prior art rõ |
| R2 count/share | Synthetic + phân tích confound; real comparison MISSING |
| R3 provider | Screen documentation xong; measured field fitness MISSING |
| R4 temporal availability | UNVERIFIED; **E3 NOT PASSED** |
| R5 evidence provenance | Có contract/fixture; real lineage MISSING |
| R6 evaluation | Chưa có independent reference, min support, quality threshold, freeze |
| R7 one-source sufficiency | Chưa được chứng minh; không tự thêm source thứ hai |
| R8 user task | D06 accepted, user validation chưa thực hiện |
| D07/D08 acceptance | Chưa có; Research Exit **NOT PASSED** |

## Smallest discriminating test

1. Chạy đúng **một AM-02 arXiv diagnostic** ở môi trường có mạng, lưu requested/final URL, redirects, headers, status, response hash/error. Giữ nguyên hai manifest trước; dừng khi bị rate-limit/access failure; không đổi proxy hay identity để bypass.
2. Nếu thành công, audit development-only extract đã khai báo, ≤2.000 works: ID/version/title/category/announcement, membership tại T, completeness của cả nonmatches, field missingness, numerator/denominator.
3. Nếu không thành công hoặc R4 vẫn không chứng minh được, viết **preregistration mới** cho exact DBLP snapshot, predicate venue/domain, publication-year bins, transfer/scan budget, checksum, ≤5.000 retained works, lag và snapshot-to-cutoff alignment. Không dùng 04/2019 cho 07–12/2019 holdout.
4. Chỉ sau real development evidence mới đề xuất support bằng số, reference protocol độc lập, quality rubric/threshold, labels hoặc abstention và sensitivity ranges. Owner phải accept D07/D08 rồi freeze trước confirmatory holdout.

**Quyết định review 10/10/2026: Research Exit #70 NOT PASSED / INSUFFICIENT EMPIRICAL EVIDENCE.** Đây là đề xuất của research agent, không phải owner acceptance. Chưa mở #71/#72/#73 như gate đã đạt. Deadline 17/10/2026 không thay đổi; elapsed dates không làm gate pass.

