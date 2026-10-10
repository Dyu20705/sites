# 10 — Design handoff có điều kiện (CHƯA ACCEPT D09)

**Trạng thái: PROPOSED / NON-BINDING.** Chuẩn bị cùng review Research Exit ngày 10/10/2026; tài liệu này không làm #71 đạt, không accept D09 và không mở implementation. **#70 Research Exit vẫn NOT PASSED.** Các lựa chọn provider, thời gian, metric, threshold, storage, UI/runtime đều cần owner acceptance tại đúng gate.

## Vertical slice theo invariants

bounded frozen source extract → raw observation/provenance bất biến → eligible-work projection hợp lệ với cutoff → lexical match/count/share tất định → evidence bundle → query in-process → dashboard local tối thiểu → replay trên snapshot.

Tách scientific meaning khỏi hệ thống vận chuyển dữ liệu. Không thêm LLM classifier, forecasting, recommendation, multi-provider identity, graph DB, distributed queue, public hosting hoặc agent subsystem trong M1.

## Logical contracts đề xuất, không phải physical schema

- **SourceSnapshot:** provider, release URI/date, published checksum, verified download hash, access/license, acquisition timestamp, freeze ID.
- **RawObservation:** snapshot ref, raw locator/hash, provider work/version key, raw fields và parsing diagnostics; chỉ lưu raw bytes khi điều khoản cho phép.
- **EligibleWork:** work ID, version basis, title, event-time và precision, available_at + evidence, membership definition / membership availability + evidence, inclusion reason, raw observation refs.
- **ConceptDefinition:** concept ID, rule/version và aliases, vocabulary_available_at cùng bằng chứng độc lập; không cho synonym tương lai vào cutoff cũ.
- **SignalPoint:** concept/bin, matched count, eligible denominator, share hoặc INSUFFICIENT_EVIDENCE với typed reason, contributor/denominator IDs, method version.
- **EvidenceBundle:** signal ref, toàn bộ contributor và denominator IDs (hoặc immutable membership file/hash), provenance, snapshot/config/code hashes, cutoff, inclusion rules, missingness, sensitivity và limitations.
- **ReplayManifest:** input/config/code/runtime identity, freeze record, semantic output hash, verification result.

## Temporal semantics phải chốt trước code

**A — as-of theo frozen snapshot:** chỉ nói điều provider release tại snapshot date chứa, cùng hạn chế về indexing lag và membership. Snapshot không chứng minh metadata đã tồn tại ở thời điểm publication cũ; D07 phải xác minh field/cutoff.

**B — retrospective event-time series:** dùng snapshot muộn, xem chuỗi publication/event time nhưng **không gọi historical backtest**. Với D05/E3 hiện đã ACCEPTED, riêng lựa chọn này không thể khiến M1 pass; muốn đổi mục tiêu phải xin owner scope gate.

Không bịa bin tháng cho DBLP khi chỉ có publication year. Không áp dụng category/ontology hiện tại vào as-of 2019 mà không ghi giới hạn.

## Các lựa chọn D09 còn PROPOSED

| Thành phần | Ứng viên đơn giản | Điều kiện đổi |
| --- | --- | --- |
| Storage | Files gồm raw snapshot, normalized JSONL và manifests bất biến; SQLite nếu đo thực chứng minh cần index/query | Database server chỉ khi có measured need |
| Runtime | Deterministic Python standard-library batch | Thêm thư viện chỉ nếu giảm complexity đã đo |
| Query | In-process trên frozen results | HTTP API chỉ khi có user/client requirement |
| Dashboard | Local read-only HTML: concept/time plot + evidence links + limitations | Framework nếu task usability cần |
| ML/LLM | None | Post-M1, cần RQ và evaluation riêng |
| Security | Public metadata, không secrets, bounded requests, input limits, read-only | Đánh giá lại khi có dữ liệu bảo vệ |
| Deployment | Local replay/package, không public hosting | Public deploy cần gate riêng |

## Gate và tests trước implementation

Cần D07/D08 ACCEPTED: raw corpus, cutoff semantics, formula/vocabulary, numeric support/quality, development/holdout freeze và budget. Sau đó #71 mới chốt D09. Kiểm tra zero-vs-missing, duplicate/version, inclusion, cutoff, late indexing, alias, title thiếu, denominator completeness, idempotency, semantic replay, full lineage và typed abstention. E1–E8 là tiêu chí phải kiểm tra, không thể coi PASS do synthetic fixtures.

**STOP:** không có corpus → quay lại source audit; chỉ có retrospective → owner phải xem scope/E3; reference/threshold chưa có → không inspect holdout; D09 chưa accepted → không xây production schema/API/dashboard.

Trình tự còn hiệu lực: #64/#65 measured evidence → owner gate #70 D07/D08 + freeze → #71 D09 → #72 implement đúng accepted slice.

