# 02 — Câu hỏi nghiên cứu

Các câu hỏi dưới đây đều đang **OPEN**. Chúng là câu hỏi cần kiểm chứng, không phải kết luận.

Phạm vi tham chiếu [Định nghĩa M1](../baseline/M1.md); cách đánh giá nằm tại [Quy trình đánh giá](06_EVALUATION_PROTOCOL.md).

## Câu hỏi nghiên cứu chính — P0

> Trong một tập tài liệu học thuật thuộc một lĩnh vực kỹ thuật cụ thể, liệu 1–2 chỉ báo đơn giản có đủ để xác định một khái niệm đang xuất hiện nhiều hơn hay ít hơn theo thời gian, đồng thời cho phép kiểm tra nguồn dữ liệu, cách tính và tái tạo lại kết quả hay không?

Mục tiêu là kiểm tra một nhận định nhỏ trước khi dùng các nhãn lớn như “emerging technology”.

Bằng chứng tối thiểu cần có:

- audit corpus;
- định nghĩa chỉ báo;
- ví dụ synthetic có kết quả mong đợi được tính độc lập;
- một trường hợp lịch sử và một negative/control case;
- gói bằng chứng;
- báo cáo chạy lại.

## Các câu hỏi phụ

| ID | Câu hỏi | Bằng chứng cần có | Quyết định được mở khóa |
| --- | --- | --- | --- |
| R1 | “Trend” trong corpus đang đo điều gì: tần suất, tỷ trọng, novelty hay impact? | Định nghĩa từ literature, ví dụ và phản ví dụ | Phạm vi kết luận, nhãn đầu ra D08 |
| R2 | Chỉ báo nào khả thi với dữ liệu M1 và nhạy với nhiễu đến mức nào? | So sánh count/share với burst/persistence; dữ liệu thiếu, sensitivity và negative controls | Chọn chỉ báo, công thức và ngưỡng D08 |
| R3 | Những trường dữ liệu tối thiểu nào cần có và độ phủ bao nhiêu là đủ? | Mẫu dữ liệu, missingness theo thời gian, access/license, query completeness | Nguồn, corpus và khoảng thời gian D07 |
| R4 | Có chứng minh được trường dữ liệu nào đã tồn tại tại cutoff T hay không? | Snapshot/version availability, audit timestamp, future-data tests | As-of evaluation hay chỉ retrospective analysis |
| R5 | Một kết quả có thể truy ngược tới bản ghi và phép biến đổi nào? | Walkthrough output → chỉ báo → observation; tham chiếu input/config/code | Evidence contract D05/D09 |
| R6 | Trường hợp lịch sử có thể đánh giá mà không hindsight tuning không? | Freeze rule trước holdout, annotation độc lập, control và disagreement log | Evaluation protocol D08 |
| R7 | Một nguồn đã đủ hay nguồn thứ hai giải quyết thiếu hụt có thể đo được? | Coverage audit, chi phí reconciliation, temporal consistency | One-source vs multi-source D07 |
| R8 | Người dùng chính có hiểu và dùng được đầu ra cho nhiệm vụ khảo sát không? | Task-based walkthrough và misunderstanding log | User/use case D06 |

## Giả thuyết về chỉ báo

**HYPOTHESIS:** count/share theo thời gian là baseline dễ kiểm tra nhưng có thể tạo trend giả khi kích thước corpus hoặc cách gọi khái niệm thay đổi.

Các hướng khác như burst/persistence có thể bổ sung thông tin nhưng chưa được chọn.

Citation velocity/acceleration và influential growth cần observation lịch sử của metric; cumulative citation count hiện tại không đủ để tái tạo trạng thái citation tại một cutoff trong quá khứ.

Concept emergence, diffusion theo venue/institution và frontier papers là các hướng từ thiết kế cũ, không mặc định nằm trong M1.

**Insufficient evidence** là một kết quả hợp lệ. Hệ thống không cần ép mọi khái niệm vào emerging / growing / stable / declining.
