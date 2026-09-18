# 06 — Evaluation Protocol

**PROPOSED — HUMAN DECISION REQUIRED (D05/D08).** Đây là kế hoạch kiểm chứng, chưa có test hoặc kết quả thực nghiệm. [M1 contract](../baseline/M1.md) dùng các mã E1–E8 làm exit criteria đề xuất. Chốt protocol trước khi triển khai và trước khi xem kết quả holdout.

## Claim cần kiểm tra

M1 kiểm tra mô tả thay đổi trong corpus đã định nghĩa, không dự đoán tương lai hay chứng minh một công nghệ tốt hơn. Phải báo riêng: correctness của phép tính, chất lượng evidence, khả năng giải thích, và mức phù hợp của detection với case đã định nghĩa. Demo chạy được không chứng minh detection có giá trị.

## Thiết kế đánh giá

1. Chốt user task, domain/query, corpus/window, đơn vị đếm, signal definition, threshold và minimum support. Ghi version cùng người chấp thuận trong D06–D08; khóa chúng trước holdout. Không chọn threshold sau khi thấy case để làm demo đẹp.
2. Synthetic examples được tính tay độc lập: tăng, giảm, không đổi, mẫu bằng không/thiếu dữ liệu, duplicate/revision và future-dated observation. Bao gồm trường hợp toàn corpus tăng nhưng tỷ trọng concept không đổi. Expected output gồm giá trị, reason và hành vi từ chối kết luận, theo signal đã chọn.
3. Chọn một historical case gồm development interval và holdout interval/cutoff. Ghi tiêu chí chọn case trước chạy; thêm control concept/window không có thay đổi theo rubric độc lập. Người review ghi expected interpretation và evidence trước khi nhìn system labels. Case chỉ minh họa phạm vi hẹp, không đại diện mọi lĩnh vực.
4. Với **as-of evaluation**, mỗi input field dùng ở cutoff T phải có bằng chứng available-at ≤ T; publication date không thay thế bằng chứng availability. Không dùng vocabulary học từ toàn future corpus, revision sau T hoặc current citation total cho lịch sử. Thuật ngữ/cấu hình cho phép ở T phải được ghi rõ.
5. Nếu không có snapshot/availability evidence, chỉ chạy **retrospective case analysis** và báo thiếu điều kiện as-of; E3 không pass. Không dùng retrospective result như backtest. Muốn hạ phạm vi claim phải có quyết định scope/evaluation được duyệt, không tự đổi tên để pass gate.
6. Báo sensitivity khi đổi window/threshold hợp lý và khi loại record thiếu fields; giữ negative results. Replay từ frozen inputs độc lập với live API.

## Acceptance matrix đề xuất

| ID | Check | Evidence cần lưu | Exit criterion |
| --- | --- | --- | --- |
| E1 | Deterministic correctness | Fixtures nhỏ, expected values tính độc lập, actual values và diff | 100% case đã định nghĩa đúng; số nguyên exact, tolerance số thực phải chốt trước test; missing/zero không tạo claim giả |
| E2 | Historical case và signal explainability | Case protocol, control, values/components, annotations độc lập, disagreement và sensitivity report | Có ít nhất 1 case và 1 control; reviewer giải thích được mọi label; mọi disagreement được phân tích, không có lỗi vận hành unresolved. Ngưỡng chất lượng detection phải chốt ở Research Gate, chưa có số accuracy mặc định |
| E3 | Temporal isolation | Field availability audit, cutoff/config/vocabulary record, injected future records | 0 input trái cutoff trong as-of run; thêm future records không đổi output trước T. Không đủ availability evidence ⇒ NOT PASSED |
| E4 | Reproducibility | Snapshot identity, config, code/version, metric definition, environment record, outputs | 2 lần chạy độc lập cùng frozen input/config/code cho cùng semantic output; chỉ timestamp vận hành được loại theo quy tắc công bố trước |
| E5 | Traceability | Full lineage và evidence bundle audit | 100% assessments của demo truy được tới signals và tập observations đóng góp; mọi excluded record có reason; không chỉ trace bài đại diện |
| E6 | Idempotency | Chạy lại cùng input; báo số records và signal values trước/sau | 0 đóng góp bị nhân đôi, semantic output không đổi; revision mới được phân biệt với replay |
| E7 | Usability/demo | Reviewer walkthrough và checklist | User chọn concept/window, xem label hoặc insufficient evidence, giải thích signal và mở evidence mà không sửa code; có ít nhất 1 kết quả có thể giải thích ngoài failure cases |
| E8 | Bounded operation và disclosure | Corpus size/coverage/missingness, thời gian chạy, peak resource nếu đo được, lỗi và hướng dẫn replay | Công bố số đo trên máy/demo corpus thực tế; đáp ứng runtime budget do Preimplementation Gate chốt. Không suy diễn khả năng scale hoặc production |

E2 tách hai phần: completeness của đánh giá và quality threshold. Hoàn thành báo cáo không tự pass quality. Research Gate phải ghi metric/rubric, cách tạo reference label, hạn chế và ngưỡng pass/fail trước holdout; chưa có quyết định này thì chưa preimplementation-ready. Precision/recall chỉ có ý nghĩa nếu có reference labels độc lập đủ phù hợp; không tự gán chúng cho trend “truth”. Không dùng prediction metrics trong M1.

## Demo acceptance và kết luận âm

Một reviewer ngoài người viết phải replay theo hướng dẫn từ snapshot được phép sử dụng, kiểm tra bundle và hoàn thành E7; kết quả và environment được ghi. Delivery có thể local, không yêu cầu public hosting. Hiện chưa có hướng dẫn chạy vì implementation chưa tồn tại.

M1 đạt khi gates đã được chấp thuận và các E1–E8 áp dụng đều pass, có demo trước 17/10/2026, không còn BLOCKER/MAJOR về correctness, temporal semantics hoặc traceability. Nếu không đủ dữ liệu hoặc signal không vượt tiêu chí đã chốt: ghi **M1 NOT PASSED / scope review required**, kèm negative finding hữu ích. Không thay threshold sau đánh giá; thay đổi protocol phải mở phiên bản và evaluation mới.
