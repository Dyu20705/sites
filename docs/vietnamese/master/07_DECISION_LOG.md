# 07 — Nhật ký quyết định

**Ngày lập:** 18/09/2026.

Trạng thái hợp lệ: **PROPOSED, ACCEPTED, REJECTED, DEFERRED, SUPERSEDED**.

Một quyết định ở trạng thái ACCEPTED chỉ có nghĩa lựa chọn đó đã được người có thẩm quyền chấp thuận. Nó **không** chứng minh phần triển khai đã tồn tại hoặc hoạt động đúng.

## 1. Quyết định đã chấp thuận

| ID | Quyết định | Căn cứ | Hệ quả |
| --- | --- | --- | --- |
| D01 | Giữ Git history; cleanup HEAD; không phục hồi implementation cũ. **ACCEPTED — 18/09/2026** | Yêu cầu reset/M0 của chủ dự án | Không restore code/config cũ chỉ để khớp tài liệu; không rewrite history |
| D02 | Docs/issues lịch sử chỉ là reference; baseline M0 không khóa vào kiến trúc cũ. **ACCEPTED** | Reset/M0 và retirement issue graph #36–#61 | Mọi stack/model mới phải được đánh giá lại |
| D03 | M1 17/09–17/10 tập trung detection/descriptive intelligence. **ACCEPTED** | Mục tiêu Month 1 | Forecasting/recommendation/optimization/agents và hạ tầng lớn nằm ngoài M1 |
| D04 | Scholarly evidence là miền khởi đầu; phải tách tầm nhìn khỏi trạng thái hiện tại và dùng evidence hierarchy. **ACCEPTED** | Yêu cầu M0 | Không tự chọn provider; papers không được mặc định là nguồn “tốt nhất” |

## 2. D05 — Bằng chứng và tính đúng

**Trạng thái:** ACCEPTED — 20/09/2026, bởi chủ dự án.

**Vấn đề:** cần giữ những bài học bền vững từ thiết kế cũ mà không kéo theo schema/stack cũ.

**Nguyên tắc đã chấp thuận:**

- truy nguyên từ kết luận về bằng chứng;
- tách observation khỏi derived result;
- temporal isolation;
- replay/reproducibility;
- idempotency;
- explainability.

Thiếu bằng chứng được phép dẫn tới **insufficient evidence**. Phép tính deterministic phải cho cùng semantic result từ cùng frozen input/config/code; replay không được nhân đôi đóng góp. Mỗi kết luận phải truy qua derived results và signals tới observations đóng góp và source evidence.

**Bản ghi chấp thuận:** trong cuộc trao đổi lập kế hoạch Research Entry ngày 20/09/2026, chủ dự án đã chọn chấp thuận D05, gồm idempotency và yêu cầu E3 hiện tại, sau đó yêu cầu triển khai kế hoạch. Bản ghi này lưu quyết định, không phải kết quả thí nghiệm.

**Căn cứ:** [Bản đồ nghiên cứu liên quan](03_PRIOR_ART_MAP.md) và tư liệu lịch sử; chưa có experiment M1.

**Hệ quả:** demo M1 vẫn phải đáp ứng E1–E8. Nếu không chứng minh historical availability của field, dùng thuật ngữ retrospective analysis; E3 vẫn NOT PASSED. Đây không phải cách thay thế tự động để M1 đạt. Công thức metric, reference labels, ngưỡng và sensitivity settings vẫn mở ở D08; D05 không chọn schema hoặc stack.

**Phương án khác và xem xét lại:** hoãn evidence contract sẽ khiến research thiếu yêu cầu correctness rõ ràng; kế thừa thiết kế vật lý cũ sẽ khóa D09 quá sớm. Lựa chọn đã chấp thuận chỉ giữ invariants. Nếu R4 không chứng minh temporal evidence, review scope với chủ dự án; không âm thầm nới E3.

## 3. D06 — Người dùng chính và nhiệm vụ

**Trạng thái:** ACCEPTED — 20/09/2026, bởi chủ dự án.

**Các phương án:**

- researcher khảo sát tài liệu chuyên ngành;
- engineer ra quyết định công nghệ;
- người dùng phổ thông xem xu hướng.

**Lựa chọn đã chấp thuận:** researcher khảo sát một chủ đề kỹ thuật. Trong corpus xác định, researcher chọn concept/khoảng thời gian, xem thay đổi, hiểu chỉ báo, mở bằng chứng hỗ trợ và hiểu giới hạn kết luận.

**Bản ghi chấp thuận:** chủ dự án đã chấp thuận rõ user/task này trong cuộc trao đổi lập kế hoạch Research Entry ngày 20/09/2026 và yêu cầu triển khai kế hoạch đã chấp thuận. Quyết định cho phép research có ranh giới, chưa xác nhận giá trị người dùng.

Lý do: phù hợp trực tiếp với scholarly evidence và giữ phạm vi hẹp hơn use case ra quyết định công nghệ.

**Thiếu:** chưa có user validation.

**Xem xét lại:** R8 sau khi có prototype dùng được. Ghi task walkthrough và misunderstanding; nếu researcher không dùng hoặc diễn giải được output, xem lại nhiệm vụ với chủ dự án. Engineer và người dùng phổ thông vẫn là alternative, không phải nhóm M1 bổ sung.

## 4. D07 — Lĩnh vực, nguồn dữ liệu và corpus

**Trạng thái:** PROPOSED.

Các nguồn từng được nhắc như arXiv, OpenAlex, Crossref, Semantic Scholar và DBLP chỉ là **candidates**; chưa nguồn nào có vai trò cố định.

**Khuyến nghị hiện tại:**

- 1 lĩnh vực kỹ thuật;
- 1 nguồn dữ liệu;
- ≤5.000 bản ghi;
- ≤24 tháng lịch sử đã kết thúc;
- 1 trường hợp lịch sử để đánh giá.

Trước khi chọn provider cần kiểm tra access/license, field coverage, missingness và temporal availability.

Nếu một nguồn thiếu field, ưu tiên đổi chỉ báo hoặc thu hẹp corpus trước khi thêm nguồn thứ hai.

## 5. D08 — Chỉ báo, nhãn và đánh giá

**Trạng thái:** PROPOSED.

**Các hướng đang xem xét:** count/share, burst/persistence, citation dynamics.

**Khuyến nghị hiện tại:** bắt đầu từ một deterministic count/share-based indicator nếu data audit cho thấy phù hợp; chỉ thêm chỉ báo thứ hai khi chứng minh được giá trị bổ sung.

Chưa chốt:

- công thức;
- bin/window;
- threshold;
- minimum support;
- bộ nhãn;
- cách tạo reference label;
- quality threshold.

Không được suy ra emerging chỉ từ count tăng.

## 6. D09 — Cách triển khai tối thiểu

**Trạng thái:** PROPOSED.

Các lựa chọn cần cân nhắc:

- files vs embedded database vs database service;
- in-process query vs HTTP API;
- local dashboard vs hosted;
- dictionary/rules vs learned model.

**Nguyên tắc:** chọn phương án nhỏ nhất vẫn đáp ứng replay, truy vấn, dashboard và evaluation.

Khuyến nghị hiện tại là local demo + in-process query nếu chưa có nhu cầu rõ cho network API.

Framework, database, dashboard stack, deployment, identity và việc dùng ML/LLM **chưa được chấp thuận**.

## 7. D10 — Phần hoãn

**Trạng thái:** DEFERRED.

Tiếp tục hoãn:

- global canonical identity/schema;
- generic source registry;
- graph enrichment rộng;
- distributed scaling;
- benchmark lớn;
- public deployment mặc định.

Các lựa chọn cũ không bị cấm vĩnh viễn; chỉ không được kế thừa tự động.

## 8. Nguyên tắc cập nhật log

Mọi thay đổi trạng thái phải ghi:

- ai chấp thuận;
- ngày;
- bằng chứng hoặc artifact liên quan;
- lý do thay đổi.

Không quyết định nào được xem là ACCEPTED chỉ vì AI agent đề xuất hoặc vì nó từng xuất hiện trong lịch sử.
