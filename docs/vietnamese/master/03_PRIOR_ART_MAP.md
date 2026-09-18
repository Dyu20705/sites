# 03 — Prior Art Map

Đây là bản đồ khảo sát cho [RQs](02_RESEARCH_QUESTIONS.md), không phải literature review hoàn chỉnh. Ngày kiểm tra nguồn: 18/09/2026. VERIFIED ở đây chỉ nói citation và nội dung tóm tắt đã đối chiếu với nguồn; không khẳng định phương pháp phù hợp SITES.

## Nguồn học thuật đã xác minh bước đầu

| Nguồn sơ cấp | Nội dung đã đối chiếu | Liên hệ nghiên cứu SITES — chưa phải quyết định |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/abs/1503.00673) | Abstract phân biệt novelty, growth, coherence, impact và uncertainty/ambiguity; không chỉ một chỉ số tăng trưởng. Đã đọc abstract, chưa critical-review toàn bài | R1: hạn chế việc gọi mọi tăng trưởng là emergence; cần operational definition nhỏ hơn |
| Kleinberg (2002), [Bursty and Hierarchical Structure in Streams — trang tác giả và kết quả mẫu](https://www.cs.cornell.edu/home/kleinber/kdd02.html) | Trang tác giả mô tả burst theo thay đổi tần suất và các ví dụ trên dòng tài liệu. Đã kiểm tra mô tả và citation, chưa đánh giá thuật toán trên corpus SITES | R2: burst detection là candidate, không đồng nghĩa với phát hiện công nghệ có giá trị |
| Sandve, Nekrutenko, Taylor & Hovig (2013), [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285) | Hướng dẫn theo dõi cách tạo kết quả, phiên bản phần mềm, input và tham số. Đã đọc các rule liên quan, không có experiment SITES | R5/R6: thiết kế replay record; chưa chọn tool hay storage |

## Research families và việc còn phải đọc

| Family | Cần khảo sát / evidence artifact | Liên hệ | Trạng thái |
| --- | --- | --- | --- |
| Scientometrics / bibliometrics | Bias độ phủ, field/age normalization; bảng giới hạn của count/citation | R1–R3 | TO RESEARCH |
| Science mapping | Co-word/co-citation, đơn vị phân tích, rủi ro interpret cluster | R1/R3 | TO RESEARCH |
| Emerging technology detection | Đọc đầy đủ Rotolo và phương pháp thực nghiệm liên quan; operationalization matrix | R1/R2 | Nguồn đầu đã xác minh; TO RESEARCH |
| Burst detection | Đọc paper Kleinberg, assumptions, tuning và baseline đơn giản | R2/R6 | Nguồn đầu đã xác minh; TO RESEARCH |
| Temporal citation dynamics | Censoring, delay, as-of metric availability và cohort bias | R2/R4 | TO RESEARCH |
| Topic/concept evolution | Alias drift, vocabulary theo cutoff và dictionary vs learned topics | R3/R4 | TO RESEARCH |
| Technology forecasting | Phân biệt detection với prediction; ghi boundary, chưa chọn phương pháp | Sau M1 | DEFERRED |
| Scholarly knowledge graphs | Work/version identity và provenance; chỉ đọc phần cần cho corpus | R3/R5/R7 | TO RESEARCH; full graph DEFERRED |
| Reproducible computational research | Chuyển rule sang replay/trace checks có thể chạy | R5/R6 | Nguồn đầu đã xác minh; chưa thực nghiệm |

Mỗi research note tiếp theo cần citation/version, câu hỏi, phương pháp/data gốc, finding, limitation, applicability và decision liên quan. Không coi abstract hoặc citation count là bằng chứng đã tái lập nghiên cứu. Research Gate yêu cầu evidence cho lựa chọn cụ thể, không yêu cầu đọc hết mọi family.

## Internal historical design lessons

**HISTORICAL — không phải prior academic art.** Đã inspect README và cả bốn design/academy documents tại snapshot [9b9f8ee](https://github.com/Dyu20705/sites/tree/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7), cùng toàn bộ issues #36–#61. Có thể đọc lại bằng `git show 9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7:<path>`; không khôi phục file cũ vào HEAD.

Các tài liệu gốc: [English design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/design/scholarly-data-platform.md), [English academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/academy/scholarly-data-model.md), [Vietnamese design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/design/scholarly-data-platform.md), [Vietnamese academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/academy/scholarly-data-model.md).

| Insight tìm lại | Evidence lịch sử | Cách xử lý trong M0 |
| --- | --- | --- |
| Observation không đồng nhất với derived claim; provenance cần trace được | [#47](https://github.com/Dyu20705/sites/issues/47), [#57](https://github.com/Dyu20705/sites/issues/57), [#59](https://github.com/Dyu20705/sites/issues/59) | Durable domain insight ứng viên; PROPOSED requirement D05, không lấy dataclass/table cũ |
| Nhiều loại timestamp và nguy cơ look-ahead leakage | [#46](https://github.com/Dyu20705/sites/issues/46) | PROPOSED temporal invariant và evaluation checks; chưa có chứng cứ dataset hỗ trợ |
| Replay phải gắn input/config/code/metric/output; chạy lại không nhân đôi signal | [#45](https://github.com/Dyu20705/sites/issues/45), [#55](https://github.com/Dyu20705/sites/issues/55) | PROPOSED reproducibility/idempotency D05; mechanism OPEN |
| Identifier, version, relation và identity không tương đương | [#48](https://github.com/Dyu20705/sites/issues/48), [#60](https://github.com/Dyu20705/sites/issues/60) | Durable insight ứng viên; minimum duplicate semantics cần research, global canonical identity DEFERRED |
| Velocity, acceleration, influential growth, emergence, persistence, diffusion, frontier papers | [#52](https://github.com/Dyu20705/sites/issues/52), [#53](https://github.com/Dyu20705/sites/issues/53), [#54](https://github.com/Dyu20705/sites/issues/54) | HYPOTHESIS/candidate signal; không nhận composite score như truth |
| Extensibility và performance cần empirical evidence | [#56](https://github.com/Dyu20705/sites/issues/56), [#58](https://github.com/Dyu20705/sites/issues/58), [#61](https://github.com/Dyu20705/sites/issues/61) | Candidate design concern; kiểm tra thời gian/tài nguyên của demo là PROPOSED, generic registry và large benchmark DEFERRED |

## Lựa chọn lịch sử không được kế thừa

**HISTORICAL CANDIDATE — NOT ACCEPTED IN CURRENT BASELINE:** DuckDB/DuckDB 1.5.5; Medallion (Bronze/Silver/Gold); Parquet; uv; schema 13 bảng; canonical UUIDv5; stub lifecycle; Source Authority Priority Matrix; exact `canonical_*` schemas; kiến trúc bốn provider; arXiv-first; vai trò cố định của OpenAlex/Crossref/Semantic Scholar; SourceRegistry, Observation dataclasses và provider adapters cũ.

Không kết luận các công nghệ đó sai; chỉ bác bỏ việc kế thừa tự động. Mọi lựa chọn mới phải qua evidence và decision gate. Issue graph #36–#61 đã retired; #57 đóng `completed` chỉ phản ánh lịch sử, không chứng minh implementation hiện hành. Không tái tạo graph đó dưới tên mới.
