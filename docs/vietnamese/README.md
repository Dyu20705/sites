# sites - Hệ thống Trí tuệ Học thuật & Tiến hóa Công nghệ (Scholar Intelligence & Tech Evolution System)

Kho lưu trữ (repository) này triển khai một pipeline khai phá dữ liệu tự động, được thiết kế để trích xuất, phân tích và dự báo **các xu hướng phát triển công nghệ** từ các cơ sở dữ liệu học thuật và thư mục quy mô lớn.

Thay vì chỉ tìm kiếm tài liệu học thuật thông thường, pipeline này hoạt động theo các nguyên tắc chọn lọc định hướng chặt chẽ (highly opinionated). Hệ thống lọc ra **các nghiên cứu uy tín, có tầm ảnh hưởng cao** và chủ động định hướng quá trình khám phá tri thức theo các hướng nghiên cứu cụ thể do người dùng xác định (ví dụ: Hệ thống đa tác tử - Multi-Agent Systems, MLOps, Kiến trúc phân tán - Distributed Architecture).

## Mục tiêu Cốt lõi

* **Phân tích Xu hướng Trọng tâm (Targeted Trend Analysis):** Khai phá đồ thị trích dẫn và siêu dữ liệu văn bản để xác định các công nghệ đang lên, các bước chuyển dịch mô hình (paradigm shifts), và các phương pháp luận đang suy thoái theo thời gian.
* **Lọc theo Mức độ Ảnh hưởng & Độ tin cậy (Impact & Authority Filtering):** Loại bỏ nhiễu bằng cách ưu tiên tài liệu học thuật dựa trên "tốc độ tăng trưởng trích dẫn" (citation velocity), các chỉ số trích dẫn có tầm ảnh hưởng (influential citations), cùng uy tín lịch sử của tác giả và hội thảo/tạp chí (venue).
* **Căn chỉnh Ngữ nghĩa Chặt chẽ (Strict Semantic Alignment):** Đảm bảo các xu hướng được khai phá bám sát các hướng kỹ thuật cụ thể bằng cách sử dụng vector embeddings và điểm tương đồng ngữ nghĩa đối với các prompt mục tiêu.
* **Tổng hợp Tri thức & Thông tin Chi tiết (Insight Synthesis):** Tự động tạo các báo cáo xu hướng theo thời gian, bản đồ nhiệt khái niệm (concept heatmaps), và làm nổi bật các bài báo tiên phong ("frontier" papers) đang dẫn dắt các làn sóng công nghệ hiện tại.

## Nguồn Dữ liệu (Data Sources)

| Nguồn | Vai trò trong Pipeline |
| :--- | :--- |
| **Semantic Scholar (S2AG)** | Lọc dữ liệu tín hiệu cao (high-signal) sử dụng nhãn "trích dẫn có tầm ảnh hưởng" (influential citation) và phân loại ý định trích dẫn (citation intent). |
| **OpenAlex** | Đồ thị học thuật toàn diện để theo dõi sự phát triển theo thời gian của các khái niệm công nghệ cụ thể. |
| **arXiv (OAI-PMH)** | Nguồn chính cho các bài báo tiền ấn bản (preprints) tiên phong trong lĩnh vực Khoa học Máy tính, Trí tuệ Nhân tạo và Hệ thống. |
| **DBLP** | Siêu dữ liệu đã được xác thực cho các hội thảo và tạp chí khoa học máy tính hàng đầu. |

## Kiến trúc Pipeline (Nền tảng Dữ liệu Học thuật Chuẩn hóa - Canonical Scholarly Data Platform)

```text
[1. arXiv OAI-PMH Harvester]
      │ Thu thập dữ liệu tăng dần (Watermark + cửa sổ hồi quy, giới hạn số lần thử lại, resumptionToken)
      ▼
[2. Tầng Bronze: Lưu trữ Thô & Manifest (Raw Landing & Manifest)]
      │ ├── Lưu trữ thô bất biến (Immutable): data/raw/arxiv/YYYY/MM/...
      │ ├── raw_source_manifest: Khử trùng lặp payload qua SHA-256 & lưu vết kiểm toán (audit trail)
      │ └── ingestion_quarantine: Định tuyến cô lập XML lỗi định dạng & vi phạm DQ-02
      ▼
[3. Tầng Silver: Quan sát Bản ghi Nguồn (Source Work Observations)]
      │ ├── Trình phân tích cú pháp XML độ chính xác cao: arXiv, arXivRaw, oai_dc
      │ ├── Bảo toàn nguyên vẹn công thức LaTeX/TeX ($\mathcal{O}(n \log n)$)
      │ └── Thu thập preprints, các bản sửa đổi (v1, v2), bài rút (withdrawals), phân loại, bản quyền
      ▼
[4. Tầng Gold: Phân giải Thực thể Chuẩn hóa (Canonical Entity Resolution)]
      │ ├── Định danh Work xác định bằng UUIDv5 (Work != Version)
      │ ├── Cập nhật bản sửa đổi tại chỗ (in-place) với Ma trận Ưu tiên Nguồn thẩm quyền
      │ └── Truy vết nguồn gốc không mất mát thông tin trong canonical_work_provenance
```

## Bắt đầu Nhanh & Kiểm thử Xác thực (Quick Start & Verification)

### Chạy Xác thực Pipeline Đầu-Cuối (End-to-End)
Chạy bộ kiểm thử xác thực 7 bước tự động (phân tích cú pháp XML, tính toán manifest, nạp dữ liệu Medallion, phát lại idempotent, an toàn watermark, cô lập quarantine, tóm tắt các tầng):
```bash
uv run python scripts/verify_arxiv_pipeline.py
```

### Chạy Toàn bộ Test Suite
Thực thi toàn bộ bộ kiểm thử (57 bài test bao gồm Harvester, Parser, Watermark, Idempotency, Schema, Resolution):
```bash
uv run pytest -v
```
