# 07 — Nhật ký quyết định

**Ngày lập:** 18/09/2026.

Trạng thái hợp lệ: **PROPOSED, ACCEPTED, REJECTED, DEFERRED, SUPERSEDED**.

Một quyết định ở trạng thái ACCEPTED chỉ có nghĩa lựa chọn đó đã được người có thẩm quyền chấp thuận. Nó **không** chứng minh implementation đã tồn tại hoặc hoạt động đúng.

## 1. Quyết định đã chấp thuận

| ID | Quyết định | Căn cứ | Hệ quả |
| --- | --- | --- | --- |
| D01 | Giữ Git history; cleanup HEAD; không phục hồi implementation cũ. **ACCEPTED — 18/09/2026** | Yêu cầu reset/M0 của chủ dự án | Không restore code/config cũ chỉ để khớp tài liệu; không rewrite history |
| D02 | Docs/issues lịch sử chỉ là reference; baseline M0 không khóa vào kiến trúc cũ. **ACCEPTED** | Reset/M0 và retirement issue graph #36–#61 | Mọi stack/model mới phải được đánh giá lại |
| D03 | M1 17/09–17/10 tập trung detection/descriptive intelligence. **ACCEPTED** | Mục tiêu Month 1 | Forecasting/recommendation/optimization/agents và hạ tầng lớn nằm ngoài M1 |
| D04 | Scholarly evidence là miền khởi đầu; phải tách vision khỏi current state và dùng evidence hierarchy. **ACCEPTED** | Yêu cầu M0 | Không tự chọn provider; papers không được mặc định là nguồn “tốt nhất” |

## 2. D05 — Evidence và correctness

**Trạng thái:** PROPOSED.

**Vấn đề:** cần giữ những bài học bền vững từ thiết kế cũ mà không kéo theo schema/stack cũ.

**Đề xuất:**

- claim traceability;
- tách observation khỏi derived result;
- temporal isolation;
- replay/reproducibility;
- idempotency;
- explainability.

**Căn cứ:** [Prior Art Map](03_PRIOR_ART_MAP.md) và tư liệu lịch sử; chưa có experiment M1.

**Khuyến nghị hiện tại:** demo phải có evidence checks E1–E8, không chỉ có dashboard.

**Xem xét lại:** Define/Research Gate. Nếu data không hỗ trợ temporal evidence, phải thu hẹp claim.

## 3. D06 — Người dùng chính và nhiệm vụ

**Trạng thái:** PROPOSED.

**Các phương án:**

- researcher khảo sát literature;
- engineer quyết định thay công nghệ;
- general public xem xu hướng.

**Khuyến nghị hiện tại:** researcher khảo sát một chủ đề kỹ thuật.

Lý do: phù hợp trực tiếp với scholarly evidence và giữ scope hẹp hơn use case ra quyết định công nghệ.

**Thiếu:** chưa có user validation.

**Xem xét lại:** Define Gate hoặc khi R8 cho thấy task không có giá trị.

## 4. D07 — Domain, nguồn và corpus

**Trạng thái:** PROPOSED.

Các nguồn từng được nhắc như arXiv, OpenAlex, Crossref, Semantic Scholar và DBLP chỉ là **candidates**; chưa nguồn nào có vai trò cố định.

**Khuyến nghị hiện tại:**

- 1 technical domain;
- 1 nguồn;
- ≤5.000 records;
- ≤24 tháng lịch sử đã kết thúc;
- 1 historical case.

Trước khi chọn provider cần kiểm tra access/license, field coverage, missingness và temporal availability.

Nếu một nguồn thiếu field, ưu tiên đổi chỉ báo hoặc thu hẹp corpus trước khi thêm nguồn thứ hai.

## 5. D08 — Chỉ báo, nhãn và đánh giá

**Trạng thái:** PROPOSED.

**Các hướng đang xem xét:** count/share, burst/persistence, citation dynamics.

**Khuyến nghị hiện tại:** bắt đầu từ một deterministic count/share-based indicator nếu data audit cho thấy phù hợp; chỉ thêm chỉ báo thứ hai khi chứng minh được giá trị bổ sung.

Chưa chốt:

- formula;
- bin/window;
- threshold;
- minimum support;
- label set;
- reference-label rubric;
- quality threshold.

Không được suy ra emerging chỉ từ count tăng.

## 6. D09 — Cách hiện thực tối thiểu

**Trạng thái:** PROPOSED.

Các lựa chọn cần cân nhắc:

- files vs embedded database vs database service;
- in-process query vs HTTP API;
- local dashboard vs hosted;
- dictionary/rules vs learned model.

**Nguyên tắc:** chọn phương án nhỏ nhất vẫn đáp ứng replay, query, dashboard và evaluation.

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
- evidence hoặc artifact liên quan;
- lý do thay đổi.

Không quyết định nào được xem là ACCEPTED chỉ vì AI agent đề xuất hoặc vì nó từng xuất hiện trong lịch sử.
