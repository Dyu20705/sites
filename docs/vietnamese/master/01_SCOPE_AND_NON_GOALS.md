# 01 — Phạm vi và các nội dung không thực hiện

[M1 definition](../baseline/M1.md) là tài liệu quyết định phạm vi Month 1. File này chỉ diễn giải ranh giới đó, không tự mở rộng scope.

## 1. Ba mức phạm vi

| Mức | Nội dung | Trạng thái |
| --- | --- | --- |
| Dài hạn | Chuỗi capability từ evidence acquisition tới automation/optimization | Định hướng, chưa phải cam kết triển khai |
| Month 1 | Corpus giới hạn → provenance → chuẩn hóa tối thiểu → 1–2 chỉ báo → query → dashboard demo | Hướng M1 đã được chấp thuận; chi tiết D06–D09 vẫn là PROPOSED |
| Sau Month 1 | Forecasting, recommendation, optimization, automation, mở rộng nguồn dữ liệu | DEFERRED |

## 2. Phạm vi M1 đang đề xuất

**PROPOSED — D06–D09:**

- 1 researcher khảo sát một chủ đề kỹ thuật;
- 1 technical domain;
- 1 nguồn dữ liệu;
- tối đa 5.000 records;
- tối đa 24 tháng dữ liệu lịch sử đã kết thúc;
- 1 chỉ báo chính; chỉ thêm chỉ báo thứ hai khi có evidence;
- 1 historical evaluation case.

Các con số trên là **trần thử nghiệm**, chưa phải benchmark hay workload đã được xác nhận.

Luồng tối thiểu vẫn phải đi xuyên hệ thống:

~~~text
acquisition/export
→ observation
→ normalization
→ chỉ báo
→ gói bằng chứng
→ query
→ dashboard
~~~

Không bắt buộc phải có network API riêng. Dashboard tối thiểu chỉ cần đủ để xem một kết quả, chỉ báo tạo nên kết quả và evidence liên quan.

## 3. Yêu cầu đối với corpus

Corpus giới hạn phải công bố:

- query hoặc cách xác định domain;
- ngày/cutoff áp dụng;
- cách chọn record;
- coverage và missingness;
- sampling nếu nguồn trả nhiều hơn giới hạn.

Không được lấy “5.000 record đầu tiên” rồi ngầm coi chúng đại diện cho toàn lĩnh vực nếu chưa kiểm tra bias.

## 4. Ngoài phạm vi Month 1

Theo **D03 — ACCEPTED**, M1 không làm:

- forecasting;
- recommendation;
- optimization;
- autonomous agents;
- hạ tầng phân tán lớn;
- multi-source nếu chưa có bằng chứng cần thiết;
- opaque LLM-based trend scoring;
- kết luận “công nghệ A tốt hơn B” từ số lượng paper;
- general-purpose platform, real-time production monitoring hoặc production operation.

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
2. Evidence nào chứng minh phần thiếu đó ảnh hưởng mục tiêu M1?
3. Chi phí mới là bao nhiêu?
4. Phần việc nào sẽ bị bỏ để giữ deadline?

Sau đó cập nhật D06–D09 và chỉ triển khai khi có human acceptance.

WIP tối đa 2. Nếu acquisition hoặc temporal evidence không khả thi, ưu tiên **giảm corpus, window hoặc chỉ báo** trước khi mở rộng kiến trúc.
