# 03 — Bản đồ nghiên cứu liên quan

Tài liệu này là **bản đồ khảo sát**, chưa phải literature review hoàn chỉnh.

**Ngày kiểm tra nguồn:** 18/09/2026.  
Nhãn **VERIFIED** ở đây chỉ có nghĩa citation và nội dung được mô tả đã được đối chiếu với nguồn. Nó không có nghĩa phương pháp đã được chứng minh phù hợp với SITES.

## 1. Nguồn học thuật đã kiểm tra bước đầu

| Nguồn | Điều đã kiểm tra | Liên hệ với SITES |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/abs/1503.00673) | Abstract nêu năm đặc trưng của emerging technology: radical novelty, relatively fast growth, coherence, prominent impact, uncertainty/ambiguity | R1: không nên đồng nhất “tăng số lượng” với “emerging technology” |
| Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/kdd02.html) | Trang tác giả mô tả burst là giai đoạn một feature xuất hiện với cường độ cao trong khoảng thời gian giới hạn; thuật toán mô hình hóa sự thay đổi tần suất theo thời gian | R2: burst detection là một phương án chỉ báo, không tự chứng minh một công nghệ “quan trọng” hay “tốt” |
| Sandve et al. (2013), [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285) | Các rule yêu cầu ghi cách tạo kết quả, input, tham số, workflow và phiên bản phần mềm để có thể tái lập | R5/R6: hỗ trợ yêu cầu về replay record và provenance |

Giới hạn của lần đọc hiện tại:

- **Rotolo:** mới kiểm tra abstract, chưa critical review toàn bài;
- **Kleinberg:** đã kiểm tra trang mô tả và paper, chưa thử thuật toán trên corpus SITES;
- **Sandve:** đã kiểm tra các rule liên quan, chưa có experiment SITES.

Không nguồn nào ở trên được dùng để chứng minh rằng một metric cụ thể đã phù hợp với SITES.

## 2. Các nhóm nghiên cứu cần tiếp tục khảo sát

| Nhóm | Bằng chứng cần tạo | Liên hệ | Trạng thái |
| --- | --- | --- | --- |
| Scientometrics / bibliometrics | Coverage bias, field/age normalization, giới hạn của count/citation | R1–R3 | TO RESEARCH |
| Science mapping | Chỉ đọc bằng chứng giải quyết thiếu hụt R1/R3 cụ thể | R1/R3 | CONDITIONAL; không phải work package riêng |
| Emerging technology detection | Đọc đầy đủ Rotolo và các cách operationalize khái niệm emergence | R1/R2 | TO RESEARCH |
| Burst detection | Đọc paper Kleinberg, assumptions, tuning và baseline đơn giản | R2/R6 | TO RESEARCH |
| Temporal citation dynamics | Censoring, delay, as-of availability, cohort bias | R2/R4 | CONDITIONAL khi có observations lịch sử cần thiết |
| Topic/concept evolution | Alias drift, vocabulary cutoff, dictionary vs learned topics | R3/R4 | TO RESEARCH |
| Technology forecasting | Phân biệt detection với prediction | Sau M1 | DEFERRED |
| Scholarly knowledge graphs | Chỉ work/version identity và provenance cần cho RQ còn thiếu | R3/R5/R7 | CONDITIONAL; full graph DEFERRED |
| Reproducible computational research | Chuyển các nguyên tắc thành replay/trace checks có thể chạy | R5/R6 | TO RESEARCH |

Mỗi research note tiếp theo dùng [evidence ledger](../research/01_EVIDENCE_LEDGER.md), gồm vị trí trong nguồn, population/period, directness và counterevidence. Giới hạn đọc hiện có ở trên giữ nguyên.

### Work packages hữu hạn

| Package | Nhóm nghiên cứu và đầu ra | Stop condition | Quyết định |
| --- | --- | --- | --- |
| A — Bằng chứng và chỉ báo ứng viên | Scientometrics, emergence, count/share, burst/persistence và evaluation; so sánh ứng viên cùng định nghĩa, alternatives và confounders | Đã ghi phương pháp chính, alternative nghiêm túc, failure modes và mức áp dụng; đủ literature cùng data evidence từ B để đề xuất, hoặc báo rõ thiếu bằng chứng | R1/R2/R6 → D08 |
| B — Khả thi nguồn và corpus | Scholarly temporal semantics, coverage và concept/vocabulary evolution; provider screening và sample audit giới hạn | Một ứng viên đủ bằng chứng đo được để đề xuất và alternatives có screening outcomes, hoặc ghi thiếu hụt quan trọng cùng phép kiểm tra phân biệt tiếp theo | R3/R4/R7 → D07 |
| Yêu cầu chung, không phải active item thứ ba | Reproducibility, work/version semantics và claim lineage | Mỗi claim quan trọng có provenance; empirical checks vẫn được lên lịch ở gate phù hợp về sau | R5 kiểm chứng D05 và cung cấp căn cứ D09 |

[Protocol](../research/00_RESEARCH_PROTOCOL.md) quy định search và stopping rules; [backlog](08_MONTH1_BACKLOG.md) liên kết issues. R8 chờ prototype dùng được và chưa được kiểm chứng. Không đặt chỉ tiêu số papers.

## 3. Bài học từ thiết kế lịch sử

**HISTORICAL — không phải prior academic art.**

Đã kiểm tra README, bốn tài liệu design/academy tại snapshot [9b9f8ee](https://github.com/Dyu20705/sites/tree/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7) và issues #36–#61.

Tài liệu lịch sử:

- [English design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/design/scholarly-data-platform.md)
- [English academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/academy/scholarly-data-model.md)
- [Vietnamese design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/design/scholarly-data-platform.md)
- [Vietnamese academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/academy/scholarly-data-model.md)

| Bài học lịch sử | Evidence | Cách dùng trong M0 |
| --- | --- | --- |
| Observation phải tách khỏi derived claim; provenance phải truy được | [#47](https://github.com/Dyu20705/sites/issues/47), [#57](https://github.com/Dyu20705/sites/issues/57), [#59](https://github.com/Dyu20705/sites/issues/59) | Nguyên tắc D05 ACCEPTED ngày 20/09; không kế thừa dataclass/table cũ |
| Có nhiều loại timestamp và nguy cơ look-ahead leakage | [#46](https://github.com/Dyu20705/sites/issues/46) | Temporal invariant D05 ACCEPTED; cần audit dataset mới |
| Replay cần gắn input/config/code/metric/output; chạy lại không được nhân đôi | [#45](https://github.com/Dyu20705/sites/issues/45), [#55](https://github.com/Dyu20705/sites/issues/55) | Reproducibility/idempotency D05 ACCEPTED; implementation chưa được xác minh |
| Identifier, version, relation và identity không tương đương | [#48](https://github.com/Dyu20705/sites/issues/48), [#60](https://github.com/Dyu20705/sites/issues/60) | Cần semantics tối thiểu; global canonical identity DEFERRED |
| Velocity, acceleration, influential growth, emergence, persistence, diffusion, frontier papers | [#52](https://github.com/Dyu20705/sites/issues/52), [#53](https://github.com/Dyu20705/sites/issues/53), [#54](https://github.com/Dyu20705/sites/issues/54) | Candidate/HYPOTHESIS; không coi composite score là ground truth |
| Extensibility và performance cần bằng chứng thực nghiệm | [#56](https://github.com/Dyu20705/sites/issues/56), [#58](https://github.com/Dyu20705/sites/issues/58), [#61](https://github.com/Dyu20705/sites/issues/61) | Chỉ kiểm tra workload M1; generic registry và large benchmark DEFERRED |

## 4. Những lựa chọn cũ chưa được kế thừa

**HISTORICAL CANDIDATE — NOT ACCEPTED IN CURRENT BASELINE:**

DuckDB, Medallion (Bronze/Silver/Gold), Parquet, uv, schema 13 bảng, canonical UUIDv5, stub lifecycle, Source Authority Priority Matrix, các schema canonical cũ, kiến trúc bốn provider, arXiv-first, vai trò cố định của OpenAlex/Crossref/Semantic Scholar, SourceRegistry, Observation dataclasses và provider adapters cũ.

Điều này **không có nghĩa các lựa chọn đó sai**. Chúng chỉ không được tự động mang sang baseline mới.

Issue graph #36–#61 là tư liệu lịch sử. Việc #57 từng ở trạng thái completed không chứng minh phần triển khai hiện tại còn tồn tại.
