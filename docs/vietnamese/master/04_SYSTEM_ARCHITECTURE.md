# 04 — Kiến trúc khái niệm

**PROPOSED — D09.** Tài liệu này chỉ chia trách nhiệm cho M1 slice. Nó **không** quy định microservice, package layout, queue, network topology hay framework.

Toàn bộ luồng có thể được triển khai trong một chương trình nếu đó là phương án nhỏ nhất đáp ứng yêu cầu.

~~~text
nguồn bằng chứng
→ thu thập
→ lưu observation
→ chuẩn hóa
→ tính chỉ báo
→ đánh giá mô tả
→ tạo gói bằng chứng
→ truy vấn
→ trình bày
~~~

## Trách nhiệm theo giai đoạn

| Giai đoạn | Trách nhiệm | Bất biến đề xuất | Còn mở |
| --- | --- | --- | --- |
| Nguồn bằng chứng | Cung cấp record/snapshot và điều kiện truy cập | Dữ liệu nguồn không phải kết luận của SITES | Provider, license, snapshot availability |
| Thu thập | Query/export → corpus + metadata thu thập | Phải công bố truncation, missing page và lỗi; không giả dữ liệu là đầy đủ | API hay export, retry, format |
| Lưu observation | Giữ record như nguồn đã cung cấp cùng provenance/version | Xử lý downstream không được âm thầm ghi đè điều nguồn đã báo | Storage, snapshot identity, retention |
| Chuẩn hóa | Tạo các trường tối thiểu và báo invalid/missing/duplicate | Unknown khác zero; record bị loại phải có reason | Time fields, alias rules, duplicate semantics |
| Tính chỉ báo | Corpus + definition/config/cutoff → giá trị | Cùng input/config phải cho cùng semantic result | Công thức, window, denominator |
| Đánh giá mô tả | Chỉ báo + rule → label hoặc insufficient evidence | Label phải có lý do, phạm vi và limitation | Label, threshold, minimum support |
| Gói bằng chứng | Gom assessment + lineage thành artifact có thể kiểm tra | Phải có input, definition, config, code version và output | Serialization, hash/canonicalization |
| Truy vấn | Đọc kết quả theo concept/window | Không trả một score tách rời bằng chứng | In-process hay API |
| Trình bày | Bảng/biểu đồ + evidence drill-down | Hiện corpus, cutoff, đơn vị, missingness và limitation | Dashboard stack, local/hosted |

## Xử lý lỗi và dữ liệu thiếu

- thu thập không đầy đủ → phải có báo cáo coverage/quality;
- thiếu trường thời gian cần thiết → không âm thầm thay bằng giá trị giả;
- chỉ báo không đủ điều kiện → trả **insufficient evidence**, không tự gán declining;
- chạy lại cùng snapshot → không được làm tăng count do duplicate ingestion;
- dữ liệu upstream thay đổi → được xem là observation mới, không phải replay cùng input.

## Quyết định kiến trúc còn mở

Research Gate / Preimplementation Gate mới được phép chốt:

- nguồn dữ liệu;
- một nguồn hay nhiều nguồn;
- storage/database;
- framework;
- giao diện truy vấn;
- dashboard;
- deployment;
- identity strategy;
- serialization.

M0 không thiết kế distribution, plugin registry, service mesh hoặc schema đầy đủ. Chỉ thêm boundary vật lý khi workload hoặc failure case đã đo cho thấy cần thiết.
