# 04 — Conceptual System Architecture

**PROPOSED — HUMAN DECISION REQUIRED (D09).** Đây là phân chia trách nhiệm để kiểm tra [M1 slice](../baseline/M1.md), không phải services, package layout hoặc topology đã chọn. Có thể thực hiện tất cả trong một chương trình; các mũi tên không đòi hỏi queue/network.

```text
Evidence Source → Acquisition → Observation Preservation → Normalization
→ Signal Extraction → Trend Assessment → Evidence Bundle → Query → Presentation
```

| Stage | Trách nhiệm; input → output | Invariant đề xuất | Quyết định còn mở |
| --- | --- | --- | --- |
| Evidence Source | Cung cấp metadata/snapshot → records và mô tả khả năng truy cập | Nguồn bên ngoài không phải kết luận SITES | Provider, license, snapshot availability |
| Acquisition | Bounded query/export → corpus cùng query, thời điểm lấy và coverage report | Công bố giới hạn, truncation, missing pages; lỗi không được giả như corpus đủ | API vs export, retry, format |
| Observation Preservation | Records nhận được → observations và dấu vết nguồn/version | Derived processing không âm thầm thay đổi điều nguồn đã báo | Storage, định danh snapshot, retention |
| Normalization | Observations → trường tối thiểu và báo cáo invalid/missing/duplicates | Giữ liên kết tới observation và lý do loại record; không đồng nhất unknown với zero | Time fields, alias rules, duplicate semantics |
| Signal Extraction | Corpus hợp lệ + definition/config/cutoff → signal values | Cùng input/config cho cùng kết quả; không dùng evidence ngoài cutoff được phép | Công thức, window, denominator |
| Trend Assessment | Signals + rule/threshold → candidate status hoặc insufficient evidence | Nhãn kèm lý do, phạm vi và hạn chế; không phải phán quyết về toàn công nghệ | Nhãn, threshold, minimum support |
| Evidence Bundle | Assessment + lineage → artifact có thể inspect/replay | Bao gồm input reference, definition, config, code version và output | Serialization, hash/canonicalization |
| Query | Bundle + lựa chọn concept/window → kết quả có provenance | Không trả một score tách rời evidence | In-process query vs API; network API có thể hoãn |
| Presentation | Kết quả query → bảng/biểu đồ và evidence drill-down | Hiện corpus, cutoff, đơn vị, missingness và giới hạn claim | Dashboard stack, local vs hosted |

## Failure semantics và giới hạn

Đề xuất: acquisition chưa đủ hoặc normalization thiếu thời gian phải phát sinh coverage/quality report. Signal không xác định trả `insufficient evidence` với lý do, không gán “declining”. Chạy lại cùng snapshot không được tăng count chỉ vì nạp lại; cơ chế cụ thể chờ design. Thay đổi upstream là một observation mới, không phải replay cùng input.

## Open architecture decisions

**OPEN — resolved during Research Gate / Preimplementation Gate:** provider, one-source vs multi-source, storage/database, framework, query interface, dashboard, deployment, identity và serialization. Các alternatives và recommendation có điều kiện nằm ở D07–D09 trong [Decision Log](07_DECISION_LOG.md). Không chọn công nghệ chỉ vì đã dùng trong lịch sử.

Không thiết kế distribution, plugin registry, service mesh hoặc schema đầy đủ ở M0. Chỉ thêm boundary vật lý khi workload hoặc failure case đã đo yêu cầu nó.
