# 02 — Research Questions

Các câu hỏi dưới đây đều **OPEN**, không phải conclusions. Scope tham chiếu [M1 contract](../baseline/M1.md); evidence được kiểm tra theo [evaluation protocol](06_EVALUATION_PROTOCOL.md).

## Primary RQ — P0

Trong một miền kỹ thuật và corpus học thuật bị giới hạn, 1–2 signal xác định có cho phép mô tả thay đổi mức độ hiện diện của khái niệm theo thời gian, với kết quả giải thích được, truy nguyên được và tái lập được hay không?

Động lực: kiểm tra một claim nhỏ trước khi dùng nhãn lớn như “emerging technology”. Evidence cần có: corpus audit, định nghĩa signal, synthetic examples, một historical case và negative/control case, evidence bundles và replay report. Quyết định mở khóa: có đủ cơ sở đi tới demo detection hay phải thu hẹp claim/scope (D07–D09). Trạng thái: **PROPOSED RQ, OPEN — Research Gate**.

| RQ | Câu hỏi và động lực | Evidence có thể trả lời | Quyết định mở khóa | Trạng thái |
| --- | --- | --- | --- | --- |
| R1 | “Trend” trong corpus đo thay đổi gì? Phân biệt tăng tần suất, tăng tỷ trọng, novelty và tác động để tránh đánh đồng | Định nghĩa từ literature, ví dụ/counterexample và glossary vận hành | Nhãn output và phạm vi claim D08 | OPEN |
| R2 | Signal nào khả thi với dữ liệu M1 và nhạy với nhiễu thế nào? | So sánh baseline count/share với burst/persistence; missingness, sensitivity và negative controls | Chọn 1–2 signal, công thức và threshold D08 | OPEN |
| R3 | Minimum fields và coverage nào đủ? | Mẫu dữ liệu có provenance, tỷ lệ thiếu theo thời gian, query completeness, điều kiện truy cập/tái phân phối | Nguồn, corpus/window, concept definition D07 | OPEN |
| R4 | Có chứng minh được dữ liệu nào đã có tại cutoff T? | Snapshot/version availability, test future-dated metric/revision, audit timestamp semantics | As-of evaluation hay chỉ retrospective claim D07/D08 | OPEN |
| R5 | Một assessment có thể trace tới record và phép biến đổi nào? | Walkthrough output → signal → observation; ghi input/config/code/definition và missing links | Observation/evidence contract D05/D09 | OPEN |
| R6 | Historical case có kiểm tra được detection mà không hindsight tuning? | Freeze query/vocabulary/threshold trước holdout; annotation độc lập, negative controls và disagreement log | Evaluation protocol/threshold D08 | OPEN |
| R7 | Một nguồn có đủ, hay nguồn thứ hai giải quyết thiếu hụt đo được? | Coverage/field audit so với yêu cầu signal; chi phí reconciliation và temporal consistency | One-source vs multi-source D07 | OPEN |
| R8 | Primary user có hiểu và dùng được output để khảo sát? | Một walkthrough có task cụ thể: tìm concept thay đổi và giải thích bằng evidence; ghi misunderstanding | Chấp thuận user/use case và demo contract D06 | OPEN |

## Các giả thuyết signal cần kiểm tra

**HYPOTHESIS:** count/share theo thời gian có thể là baseline dễ kiểm tra, nhưng biến động corpus hoặc từ đồng nghĩa có thể tạo trend giả. Burst/persistence có thể bổ sung thông tin, chưa được chọn. Citation velocity/acceleration và influential growth cần nhiều observation metric theo thời gian; current cumulative citation count không đủ để tái tạo lịch sử.

Concept emergence, venue/institution diffusion và frontier papers từ thiết kế cũ là candidates; không mặc định thuộc M1. Công thức composite chưa được chấp nhận. Kết quả “insufficient evidence” là hợp lệ; không ép mọi concept thành emerging/growing/stable/declining.
