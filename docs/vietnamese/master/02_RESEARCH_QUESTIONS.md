# 02 — Câu hỏi nghiên cứu

Các câu hỏi dưới đây đều đang **OPEN**. Chúng là câu hỏi cần kiểm chứng, không phải kết luận.

Phạm vi tham chiếu [M1 definition](../baseline/M1.md); cách đánh giá nằm tại [Evaluation Protocol](06_EVALUATION_PROTOCOL.md).

## Câu hỏi nghiên cứu chính — P0

> Trong một miền kỹ thuật và corpus học thuật được giới hạn rõ, 1–2 chỉ báo có thể mô tả sự thay đổi mức độ hiện diện của một khái niệm theo thời gian theo cách giải thích được, truy nguyên được và tái lập được hay không?

Mục tiêu là kiểm tra một claim nhỏ trước khi dùng các nhãn lớn như “emerging technology”.

Evidence tối thiểu cần có:

- audit corpus;
- định nghĩa chỉ báo;
- ví dụ synthetic có expected result tính độc lập;
- một historical case và một negative/control case;
- gói bằng chứng;
- báo cáo chạy lại.

## Các câu hỏi phụ

| ID | Câu hỏi | Evidence cần có | Quyết định được mở khóa |
| --- | --- | --- | --- |
| R1 | “Trend” trong corpus đang đo điều gì: tần suất, tỷ trọng, novelty hay impact? | Literature definitions, ví dụ và phản ví dụ | Phạm vi claim, nhãn đầu ra D08 |
| R2 | Chỉ báo nào khả thi với dữ liệu M1 và nhạy với nhiễu đến mức nào? | So sánh count/share với burst/persistence; missingness, sensitivity, negative controls | Chọn chỉ báo, công thức và threshold D08 |
| R3 | Những field tối thiểu nào cần có và coverage bao nhiêu là đủ? | Data sample, missingness theo thời gian, access/license, query completeness | Nguồn, corpus và window D07 |
| R4 | Có chứng minh được field nào đã tồn tại tại cutoff T hay không? | Snapshot/version availability, timestamp audit, future-data tests | As-of evaluation hay chỉ retrospective analysis |
| R5 | Một kết quả có thể truy ngược tới record và phép biến đổi nào? | Walkthrough output → chỉ báo → observation; input/config/code references | Evidence contract D05/D09 |
| R6 | Historical case có thể đánh giá mà không hindsight tuning không? | Freeze rule trước holdout, annotation độc lập, control và disagreement log | Evaluation protocol D08 |
| R7 | Một nguồn đã đủ hay nguồn thứ hai giải quyết thiếu hụt có thể đo được? | Coverage audit, reconciliation cost, temporal consistency | One-source vs multi-source D07 |
| R8 | Người dùng chính có hiểu và dùng được đầu ra cho nhiệm vụ khảo sát không? | Task-based walkthrough và misunderstanding log | User/use case D06 |

## Giả thuyết về chỉ báo

**HYPOTHESIS:** count/share theo thời gian là baseline dễ kiểm tra nhưng có thể tạo trend giả khi kích thước corpus hoặc từ đồng nghĩa thay đổi.

Các hướng khác như burst/persistence có thể bổ sung thông tin nhưng chưa được chọn.

Citation velocity/acceleration và influential growth cần observation lịch sử của metric; cumulative citation count hiện tại không đủ để tái tạo citation state tại một cutoff trong quá khứ.

Concept emergence, diffusion theo venue/institution và frontier papers là candidates từ thiết kế cũ, không mặc định nằm trong M1.

**Insufficient evidence** là một kết quả hợp lệ. Hệ thống không cần ép mọi concept vào emerging / growing / stable / declining.
