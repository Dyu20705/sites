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

## Kiểm tra cụ thể và phụ trách

Bằng chứng và decision mappings ở trên vẫn là câu hỏi nghiên cứu mở. Chấp thuận D05/D06 xác định yêu cầu và người dùng mục tiêu, chưa trả lời R5/R8. A và B là hai [research work packages](08_MONTH1_BACKLOG.md); [research protocol](../research/00_RESEARCH_PROTOCOL.md) quy định cách ghi bằng chứng.

| RQ | Construct cần đo/làm rõ | Failure / falsifier cần kiểm tra | Phụ trách và bàn giao |
| --- | --- | --- | --- |
| R1 | Activity/frequency/share so với novelty/impact | Định nghĩa được chọn suy ra emergence hoặc impact chỉ từ count | A → phạm vi claim D08 |
| R2 | Độ nhạy chỉ báo với activity và confounders | Kết luận đổi chủ yếu do denominator, coverage, alias, query hoặc window | A với field evidence từ B → D08 |
| R3 | Field fitness và corpus coverage | Field thiết yếu thiếu, không hợp lệ hoặc lệch theo thời gian khiến metric dự định không có đủ dữ liệu | B → D07 và requirements cho A |
| R4 | Availability từng giá trị tại cutoff T | Chỉ có metadata hiện tại hoặc event dates; không chứng minh được khả năng biết trong quá khứ | B → D07/D08; chỉ retrospective, E3 NOT PASSED |
| R5 | Traceability và reproducibility của claim | Không tái tạo được record đóng góp, phép biến đổi hoặc phiên bản input/config | A+B xuyên suốt; sau đó executable checks D05 và thiết kế D09 |
| R6 | Đánh giá độc lập không hindsight selection/tuning | Case hoặc reference labels phụ thuộc output chỉ báo, hoặc đổi ngưỡng sau khi xem holdout | A cùng feasibility từ B → D08 |
| R7 | Mức đủ của một nguồn | Thiếu hụt bắt buộc vẫn tồn tại sau khi thu hẹp chỉ báo/corpus; nguồn khác phải có lợi ích đo được | B → D07; không tự mở rộng multi-source |
| R8 | Hiểu nhiệm vụ và giá trị sử dụng | Researcher không giải thích được chỉ báo, tìm bằng chứng hoặc nhận biết giới hạn claim | Walkthrough khi có prototype → xem lại D06 nếu cần; acceptance chưa hoàn thành R8 |

P0 thất bại trong phạm vi kiểm tra nếu không có chỉ báo khả thi vượt qua các kiểm tra này mà vẫn giữ trace/replay và temporal evidence. Giữ kết quả âm thay vì đổi câu hỏi sau đánh giá.

## Giả thuyết về chỉ báo

**HYPOTHESIS:** count/share theo thời gian là baseline dễ kiểm tra nhưng có thể tạo trend giả khi kích thước corpus hoặc cách gọi khái niệm thay đổi.

Các hướng khác như burst/persistence có thể bổ sung thông tin nhưng chưa được chọn.

Citation velocity/acceleration và influential growth cần observation lịch sử của metric; cumulative citation count hiện tại không đủ để tái tạo trạng thái citation tại một cutoff trong quá khứ.

Concept emergence, diffusion theo venue/institution và frontier papers là các hướng từ thiết kế cũ, không mặc định nằm trong M1.

**Insufficient evidence** là một kết quả hợp lệ. Hệ thống không cần ép mọi khái niệm vào emerging / growing / stable / declining.
