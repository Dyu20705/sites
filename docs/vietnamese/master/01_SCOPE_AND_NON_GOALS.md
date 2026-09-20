# 01 — Phạm vi và các nội dung không thực hiện

[Định nghĩa M1](../baseline/M1.md) là tài liệu quyết định phạm vi Month 1. File này chỉ diễn giải ranh giới đó, không tự mở rộng scope.

## 1. Ba mức phạm vi

| Mức | Nội dung | Trạng thái |
| --- | --- | --- |
| Dài hạn | Chuỗi năng lực từ thu thập bằng chứng tới tự động hóa/tối ưu hóa | Định hướng, chưa phải cam kết triển khai |
| Month 1 | Corpus giới hạn → provenance → chuẩn hóa tối thiểu → 1–2 chỉ báo → truy vấn → dashboard demo | Hướng M1 và D05/D06 đã được chấp thuận; chi tiết D07–D09 vẫn là PROPOSED |
| Sau Month 1 | Forecasting, recommendation, optimization, automation, mở rộng nguồn dữ liệu | DEFERRED |

## 2. Phạm vi M1 đang đề xuất

**ACCEPTED — D06:** một researcher khảo sát một chủ đề kỹ thuật.

**PROPOSED — D07–D09:**

- 1 lĩnh vực kỹ thuật;
- 1 nguồn dữ liệu;
- tối đa 5.000 bản ghi;
- tối đa 24 tháng dữ liệu lịch sử đã kết thúc;
- 1 chỉ báo chính; chỉ thêm chỉ báo thứ hai khi có bằng chứng;
- 1 trường hợp lịch sử dùng để đánh giá.

Các con số trên là **giới hạn thử nghiệm**, chưa phải benchmark hay workload đã được xác nhận.

Luồng tối thiểu vẫn phải đi xuyên hệ thống:

~~~text
thu thập/export
→ observation
→ chuẩn hóa
→ chỉ báo
→ gói bằng chứng
→ truy vấn
→ dashboard
~~~

Không bắt buộc phải có network API riêng. Dashboard tối thiểu chỉ cần đủ để xem một kết quả, chỉ báo tạo nên kết quả và bằng chứng liên quan.

## 3. Yêu cầu đối với corpus

Corpus giới hạn phải công bố:

- truy vấn hoặc cách xác định lĩnh vực;
- ngày hoặc cutoff áp dụng;
- cách chọn bản ghi;
- độ phủ và dữ liệu thiếu;
- cách lấy mẫu nếu nguồn trả nhiều hơn giới hạn.

Không được lấy “5.000 bản ghi đầu tiên” rồi ngầm coi chúng đại diện cho toàn lĩnh vực nếu chưa kiểm tra bias.

## 4. Ngoài phạm vi Month 1

Theo **D03 — ACCEPTED**, M1 không làm:

- forecasting;
- recommendation;
- optimization;
- autonomous agents;
- hạ tầng phân tán quy mô lớn;
- nhiều nguồn dữ liệu nếu chưa có bằng chứng cần thiết;
- chấm điểm xu hướng bằng LLM theo cách khó giải thích;
- kết luận “công nghệ A tốt hơn B” từ số lượng bài báo;
- general-purpose platform, real-time production monitoring hoặc vận hành production.

Theo **D10 — DEFERRED**, tiếp tục hoãn:

- global entity resolution;
- ontology đầy đủ;
- graph enrichment rộng;
- full-text mining quy mô lớn;
- composite ranking;
- public deployment mặc định;
- benchmark quy mô lớn.

## 5. Kiểm soát scope creep

Muốn thêm nguồn, chỉ báo hoặc capability phải trả lời bốn câu:

1. Slice hiện tại thiếu gì?
2. Bằng chứng nào cho thấy phần thiếu đó ảnh hưởng mục tiêu M1?
3. Chi phí mới là bao nhiêu?
4. Phần việc nào sẽ bị bỏ để giữ deadline?

Sau đó cập nhật D06–D09 và chỉ triển khai khi có human acceptance.

WIP tối đa 2. Nếu acquisition hoặc bằng chứng theo thời gian không khả thi, ưu tiên **giảm corpus, khoảng thời gian hoặc số chỉ báo** trước khi mở rộng kiến trúc.
