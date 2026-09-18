# 03 — Bản đồ nghiên cứu liên quan

Tài liệu này là **bản đồ khảo sát**, chưa phải literature review hoàn chỉnh.

**Ngày kiểm tra nguồn:** 18/09/2026.  
Nhãn **VERIFIED** ở đây chỉ có nghĩa citation và nội dung được mô tả đã được đối chiếu với nguồn; nó không có nghĩa phương pháp đã được chứng minh phù hợp với SITES.

## 1. Nguồn học thuật đã kiểm tra bước đầu

| Nguồn | Điều đã kiểm tra | Liên hệ với SITES |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/abs/1503.00673) | Abstract nêu năm đặc trưng: radical novelty, relatively fast growth, coherence, prominent impact, uncertainty/ambiguity | R1: không nên đồng nhất “tăng số lượng” với “emerging technology” |
| Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/kdd02.html) | Trang tác giả mô tả burst là giai đoạn feature xuất hiện với cường độ cao trong một khoảng thời gian; model dựa trên thay đổi tần suất | R2: burst detection là candidate, không phải bằng chứng trực tiếp rằng một công nghệ có giá trị |
| Sandve et al. (2013), [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285) | Các rule yêu cầu ghi lại workflow, input, parameter và software version để tái lập kết quả | R5/R6: hỗ trợ yêu cầu về replay record và provenance |

Giới hạn hiện tại:

- Rotolo: mới kiểm tra abstract, chưa critical review toàn bài;
- Kleinberg: mới kiểm tra mô tả thuật toán và sample page, chưa chạy trên corpus SITES;
- Sandve: đã kiểm tra các rule liên quan, chưa có experiment SITES.

## 2. Các nhóm nghiên cứu cần tiếp tục khảo sát

| Nhóm | Evidence cần tạo | Liên hệ | Trạng thái |
| --- | --- | --- | --- |
| Scientometrics / bibliometrics | Coverage bias, field/age normalization, giới hạn của count/citation | R1–R3 | TO RESEARCH |
| Science mapping | Co-word/co-citation, đơn vị phân tích, rủi ro diễn giải cluster | R1/R3 | TO RESEARCH |
| Emerging technology detection | Đọc đầy đủ Rotolo và các operationalization thực nghiệm | R1/R2 | TO RESEARCH |
| Burst detection | Đọc paper Kleinberg, assumptions, tuning, baseline | R2/R6 | TO RESEARCH |
| Temporal citation dynamics | Censoring, delay, as-of availability, cohort bias | R2/R4 | TO RESEARCH |
| Topic/concept evolution | Alias drift, vocabulary cutoff, dictionary vs learned topics | R3/R4 | TO RESEARCH |
| Technology forecasting | Tách detection khỏi prediction | Sau M1 | DEFERRED |
| Scholarly knowledge graphs | Work/version identity, provenance | R3/R5/R7 | TO RESEARCH; full graph DEFERRED |
| Reproducible computational research | Biến các rule thành replay/trace checks có thể chạy | R5/R6 | TO RESEARCH |

Mỗi research note tiếp theo cần ghi: nguồn/version, câu hỏi, phương pháp và dữ liệu gốc, finding, limitation, mức áp dụng cho SITES và quyết định liên quan.

## 3. Bài học từ thiết kế lịch sử

**HISTORICAL — không phải prior academic art.**

Đã kiểm tra README, bốn design/academy documents tại snapshot [9b9f8ee](https://github.com/Dyu20705/sites/tree/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7) và issues #36–#61.

Tài liệu gốc:

- [English design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/design/scholarly-data-platform.md)
- [English academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/academy/scholarly-data-model.md)
- [Vietnamese design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/design/scholarly-data-platform.md)
- [Vietnamese academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/academy/scholarly-data-model.md)

| Bài học lịch sử | Evidence | Cách dùng trong M0 |
| --- | --- | --- |
| Observation phải tách khỏi derived claim; provenance phải truy được | #47, #57, #59 | PROPOSED requirement D05; không kế thừa dataclass/table cũ |
| Có nhiều loại timestamp và nguy cơ look-ahead leakage | #46 | PROPOSED temporal invariant; cần dataset audit mới |
| Replay cần gắn input/config/code/metric/output; chạy lại không được nhân đôi | #45, #55 | PROPOSED reproducibility/idempotency requirement |
| Identifier, version, relation và identity không tương đương | #48, #60 | Cần semantics tối thiểu; global canonical identity DEFERRED |
| Velocity, acceleration, influential growth, emergence, persistence, diffusion, frontier papers | #52–#54 | Candidate/HYPOTHESIS; không coi composite score là truth |
| Extensibility và performance cần bằng chứng thực nghiệm | #56, #58, #61 | Chỉ kiểm tra workload M1; generic registry/large benchmark DEFERRED |

## 4. Những lựa chọn cũ chưa được kế thừa

**HISTORICAL CANDIDATE — NOT ACCEPTED IN CURRENT BASELINE:**

DuckDB, Medallion (Bronze/Silver/Gold), Parquet, uv, schema 13 bảng, canonical UUIDv5, stub lifecycle, Source Authority Priority Matrix, các schema canonical cũ, kiến trúc bốn provider, arXiv-first, vai trò cố định của OpenAlex/Crossref/Semantic Scholar, SourceRegistry, Observation dataclasses và provider adapters cũ.

Điều này **không có nghĩa các lựa chọn đó sai**. Chúng chỉ không được tự động mang sang baseline mới.

Issue graph #36–#61 là tài liệu lịch sử. Việc #57 từng ở trạng thái completed không chứng minh implementation hiện tại còn tồn tại.
