# 07 — Decision Log

Ngày lập: **18/09/2026**. Status hợp lệ: PROPOSED, ACCEPTED, REJECTED, DEFERRED, SUPERSEDED. ACCEPTED là quyết định scope/governance có thẩm quyền, không đồng nghĩa với VERIFIED implementation. Chủ dự án chấp thuận lựa chọn; Control Tower thực hiện review/merge gate. Mọi thay đổi status phải ghi người chấp thuận, ngày và evidence link; không ghi lùi ngày.

Nguồn thẩm quyền D01–D04: yêu cầu trực tiếp của chủ dự án về repository reset và M0 documentation ngày 18/09/2026 trong phiên làm việc cho [PR #62](https://github.com/Dyu20705/sites/pull/62). Bảng ghi lại nội dung được giao; không suy ra acceptance từ issue lịch sử. D05–D09 chỉ là đề xuất của documentation pass này.

## Các quyết định đã được giao

| ID | Decision / Status / Date | Context và options | Evidence / rationale | Consequences / revisit trigger |
| --- | --- | --- | --- | --- |
| D01 | Giữ Git history, cleanup HEAD; không phục hồi implementation. **ACCEPTED**, 18/09/2026 | Cleanup vs phục hồi kiến trúc cũ | Chỉ thị reset/M0 của chủ dự án; trạng thái tree kiểm tra ở 12eccab | Không restore code/config, không archive folders hay rewrite history. Revisit khi có scope implementation mới được duyệt; giữ lịch sử vẫn là ràng buộc |
| D02 | Historical docs/issues là reference, không phải active roadmap; M0 architecture-neutral. **ACCEPTED**, 18/09/2026 | Kế thừa tự động vs đánh giá lại độc lập | Chỉ thị reset/M0; #36–#61 đã đóng | Mọi stack/model mới cần evidence; chỉ thay đổi khi có decision mới rõ ràng, không dùng #57 completed làm proof |
| D03 | M1 17/09–17/10/2026 tập trung detection/descriptive intelligence. **ACCEPTED**, 18/09/2026 | Detection slice nhỏ vs cả capability chain | Mission M0 của chủ dự án | Forecasting/recommendation/optimization/agents, opaque LLM scoring và hạ tầng lớn ngoài M1; deadline 17/10 cố định. Revisit scope chỉ qua human gate |
| D04 | Scholarly evidence là miền khởi đầu; phân biệt vision/current state và dùng evidence hierarchy. **ACCEPTED**, 18/09/2026 | Evidence source khác project source-of-truth; papers không được mặc định “tốt nhất” | Yêu cầu M0 mục 1, 5 và 9; hierarchy tại charter | Không tự chọn provider; claim quan trọng phải rõ status. Revisit domain khi hoàn tất M1 và có evidence cho domain mới |

## Các đề xuất cần human acceptance

### D05 — Evidence và correctness requirements

- **Status / Date:** PROPOSED — HUMAN DECISION REQUIRED / 18/09/2026.
- **Context:** cần phục hồi durable insights mà không kế thừa schema. Claim traceability, observation/derived separation, temporal isolation, replay, idempotency và explainability là requirements ứng viên.
- **Options:** chỉ minh họa dashboard; hoặc demo có evidence bundle và checks E1–E8.
- **Evidence:** [bài học lịch sử và nguồn nghiên cứu](03_PRIOR_ART_MAP.md); chưa có experiment mới.
- **Recommendation / rationale:** chọn demo có evidence checks; chi phí cao hơn nhưng kiểm tra được claim.
- **Consequences:** cần metadata về nguồn/thời gian và replay; không buộc table hay engine.
- **Revisit trigger:** chốt ở Define/Research Gate; nếu data không hỗ trợ temporal evidence phải thu hẹp claim công khai.

### D06 — Primary user và nhiệm vụ

- **Status / Date:** PROPOSED — HUMAN DECISION REQUIRED / 18/09/2026.
- **Context:** user draft bao gồm nhiều đối tượng; chưa có phỏng vấn/quan sát usage.
- **Options:** researcher khảo sát literature một chủ đề; engineer quyết định thay stack; general public xem xu hướng.
- **Evidence:** nhu cầu trong draft charter/M1; chưa validation.
- **Recommendation / rationale:** researcher cần kiểm tra concept nào thay đổi trong literature của một chủ đề. Phù hợp scholarly evidence hơn use case quyết định đầu tư/đổi công nghệ; phạm vi hẹp hơn public product.
- **Consequences:** chỉ một task walkthrough, không recommendation công nghệ.
- **Revisit trigger:** người dùng được chủ dự án xác nhận ở Define Gate; R8 walkthrough bác bỏ nhu cầu thì sửa contract trước design.

### D07 — Domain, nguồn và bounded corpus

- **Status / Date:** PROPOSED — HUMAN DECISION REQUIRED / 18/09/2026.
- **Context:** chưa có provider audit hoặc data sample trong repository.
- **Options:** một source với export/snapshot hoặc API; nhiều nguồn với reconciliation. Các nguồn được nhắc trong lịch sử (arXiv, OpenAlex, Crossref, Semantic Scholar, DBLP) chỉ là candidates chưa đánh giá, không có vai trò cố định.
- **Evidence:** R3/R4/R7 chưa có kết quả. Cần official access/license documentation, field coverage, missingness và temporal availability audit trước chọn provider.
- **Recommendation / rationale:** một technical domain, một nguồn, tối đa 5.000 records, 24 tháng đã kết thúc, một historical case. Trần nhỏ để kiểm tra feasibility; domain cụ thể và ngày bắt đầu/kết thúc vẫn OPEN. Export có thể giảm phụ thuộc live API nhưng availability lịch sử phải được chứng minh.
- **Consequences:** không đại diện toàn khoa học; corpus selection/sampling phải công khai. Multi-source tăng coverage nhưng tăng identity/provenance/time complexity.
- **Revisit trigger:** Research Gate chọn provider/domain/window sau mẫu dữ liệu; nếu trường hoặc thời gian không đủ thì đổi signal/thu hẹp corpus trước cân nhắc nguồn thứ hai.

### D08 — Signal, label và evaluation

- **Status / Date:** PROPOSED — HUMAN DECISION REQUIRED / 18/09/2026.
- **Context:** “mới/mạnh/lụi tàn” chưa có operational meaning.
- **Options:** count/share và thay đổi theo thời gian; burst/persistence; citation dynamics; opaque composite score (ngoài M1 theo D03).
- **Evidence:** nguồn sơ cấp trong prior art mới được kiểm tra bước đầu; R1/R2/R4/R6 chưa trả lời.
- **Recommendation / rationale:** bắt đầu một deterministic count/share-based signal nếu coverage phù hợp; xem signal thứ hai chỉ khi chứng minh thêm giá trị. Count đơn giản nhưng nhạy corpus size; share phụ thuộc denominator; citation dynamics cần historical observations chưa xác nhận có.
- **Consequences:** công thức, bin size, threshold, minimum support, reference-label rubric, quality threshold và nhãn output còn OPEN. `Insufficient evidence` phải được xem xét; không mặc định “emerging” từ tăng count.
- **Revisit trigger:** Research Gate chốt trước holdout; protocol thất bại ⇒ negative finding hoặc decision mới, không tuning âm thầm.

### D09 — Minimal delivery và implementation choices

- **Status / Date:** PROPOSED — HUMAN DECISION REQUIRED / 18/09/2026.
- **Context:** deadline ngắn; chưa workload hay verified implementation.
- **Options / trade-offs:** files vs embedded database vs database service (đơn giản vs query/integrity/operation); in-process query vs HTTP API (ít thành phần vs tái sử dụng); local dashboard vs hosted (ít vận hành vs khả năng truy cập); dictionary/rules vs learned model (inspectability vs coverage/chi phí validation).
- **Evidence:** conceptual boundaries và evaluation requirements; chưa benchmark hoặc prototype mới.
- **Recommendation / rationale:** chọn cách nhỏ nhất đủ replay/query/dashboard; ưu tiên local demo và in-process query, không network API riêng nếu không cần. Framework, database/storage, dashboard stack, deployment, identity và ML/LLM usage chưa được chọn; không thêm model chỉ để làm scoring.
- **Consequences:** kiến trúc và data model là conceptual proposals. Design phải ghi exact choices, resource budget, alternatives và bằng chứng tại Preimplementation Gate.
- **Revisit trigger:** acceptance của D05–D08 và workload sample; không triển khai trước khi các lựa chọn cần thiết được duyệt.

### D10 — Khả năng hoãn và thiết kế cũ

- **Status / Date:** DEFERRED / 18/09/2026.
- **Context / options:** làm full platform trong M1 hoặc giữ slice hẹp.
- **Evidence / rationale:** D02/D03 và deadline; historical architecture không có hiệu lực hiện tại.
- **Consequences:** hoãn global canonical identity/schema, generic source registry, graph enrichment, distributed scaling, full benchmark và public deployment. Các công nghệ cũ trong prior art không bị cấm vĩnh viễn nhưng chưa selected.
- **Revisit trigger:** chỉ khi accepted M1 requirement không thể đáp ứng bằng slice hẹp; cần scope/cost evidence và human acceptance. Forecasting/recommendation/optimization tiếp tục ngoài M1 theo D03.

Không có accepted decision về exact target user, provider, source count, database, framework, canonical schema, scoring formula, ML/LLM hay dashboard stack. Không có quyết định nào được chấp thuận chỉ vì agent đề xuất nó.
