# Học thuật hóa dự án (Academize Project)

---

## 1. Định nghĩa Bài toán (Problem Definition)

### 1.1 Bối cảnh và Thách thức (Context and Challenge)

Nghiên cứu tính toán hiện đại về sự tiến hóa của khoa học—chẳng hạn như khai phá xu hướng công nghệ, động lực trích dẫn và phát hiện các bước chuyển dịch mô hình (paradigm shifts)—đòi hỏi phải tổng hợp siêu dữ liệu thư mục từ nhiều nhà cung cấp dữ liệu học thuật khác nhau. Một bộ máy khai phá xu hướng không thể chỉ dựa vào một kho lưu trữ cục bộ cô lập; nó phải kết hợp được tốc độ cập nhật preprint theo thời gian thực của **arXiv**, cấu trúc tô-pô đồ thị học thuật mở của **OpenAlex**, cơ sở đăng ký nhà xuất bản chính thức của **Crossref**, cùng các chỉ số tác động và phân loại ý định trích dẫn phong phú của **Semantic Scholar (S2AG)**.

Tuy nhiên, kỹ thuật dữ liệu học thuật luôn phải đối mặt với sự không đồng nhất sâu sắc về mặt cấu trúc:
* **Vòng đời Xuất bản Phi tập trung**: Một đóng góp khoa học bắt đầu dưới dạng bản thảo chưa qua bình duyệt (preprint), phát triển qua nhiều lần sửa đổi (preprint revisions), trải qua bình duyệt đồng cấp (peer review), được xuất bản trong hội thảo hoặc tạp chí kèm định danh đối tượng số (DOI), và sau đó có thể được lập chỉ mục lại hoặc bị rút bài (retracted).
* **Sự Phân kỳ Ngữ nghĩa**: Không có hai nền tảng nào chia sẻ mô hình thực thể hoàn toàn giống nhau. Thông tin cơ quan trực thuộc (affiliation) của tác giả trong Crossref là một chuỗi văn bản tự do do nhà xuất bản cung cấp; trong OpenAlex, nó được ánh xạ tới một tổ chức chuẩn hóa theo Danh mục Tổ chức Nghiên cứu (ROR). Trong arXiv, phần tóm tắt (abstract) là các chuỗi TeX/LaTeX thô; trong OpenAlex, chúng là các chỉ mục đảo theo vị trí từ (inverted indices) nhằm tránh các hạn chế về bản quyền; trong Semantic Scholar, chúng là văn bản thuần túy được trích xuất.
* **Sự Phân mảnh Định danh**: Các bản preprint không có DOI khi mới khởi tạo; tác giả hiếm khi cung cấp mã ORCID nhất quán; các địa điểm xuất bản (venues) thường xuyên đổi tên hoặc thay đổi đơn vị bảo trợ.
* **Bất đồng giữa các Nguồn**: Năm xuất bản, thứ tự tác giả và số lượng trích dẫn thường xuyên mâu thuẫn một cách có hệ thống giữa các bộ tổng hợp dữ liệu.

```
[arXiv: Quan sát Preprint] ────────────┐
[OpenAlex: Quan sát Đồ thị & Chủ đề] ──┼──► [Thu thập & Phân giải] ──► [Mô hình Học thuật Chuẩn hóa]
[Crossref: Đăng ký DOI Nhà xuất bản] ──┤                                 (Tách rời, Chuẩn hóa,
[Semantic Scholar: Ý định Trích dẫn] ──┘                                 Kiểm toán, Lũy đẳng)
```

### 1.2 Sứ mệnh của Mô hình hóa Dữ liệu Học thuật Chuẩn hóa
Mục tiêu của mô hình hóa dữ liệu học thuật chuẩn hóa là xây dựng một tầng phân tích quan hệ đáng tin cậy, được tối ưu hóa cho truy vấn (triển khai thông qua **DuckDB**), đáp ứng năm tiên đề bất di bất dịch:
1. **Tách biệt Quan sát khỏi Định danh**: Biểu diễn chuẩn hóa của một thực thể phải tồn tại độc lập với ID độc quyền của bất kỳ nhà cung cấp nào.
2. **Nguồn gốc Dữ liệu Không mất mát (Lossless Provenance)**: Hệ thống phải theo dõi được *ai đã khẳng định điều gì, vào thời điểm nào và với độ tin cậy ra sao*. Việc hợp nhất các bản ghi không bao giờ được phép xóa bỏ lịch sử quan sát thô.
3. **Giải quyết Xung đột Xác định (Deterministic Conflict Resolution)**: Các bất đồng giữa các nguồn phải được giải quyết thông qua các chính sách ưu tiên minh bạch, xác định thay vì ghi đè tùy tiện.
4. **Tính Lũy đẳng Nghiêm ngặt khi Nạp dữ liệu (Strict Ingestion Idempotency)**: Các pipeline nạp dữ liệu phải có khả năng phát lại và chịu lỗi; việc chạy lặp lại trên cùng một lô dữ liệu hoặc các lô chồng lấn phải cho ra trạng thái giống hệt nhau, không phát sinh lỗi hay dữ liệu rác.
5. **Tiện ích Phân tích Tối ưu (Analytical Ergonomics)**: Nền tảng dữ liệu phải hỗ trợ các truy vấn nghiên cứu xuôi dòng—chẳng hạn như theo dõi tốc độ trích dẫn, xếp hạng uy tín nơi xuất bản và phát hiện cộng đồng đồng tác giả—với hiệu năng truy vấn SQL quan hệ dưới 1 giây.

---

## 2. Bức tranh Toàn cảnh Dữ liệu Học thuật (Scholarly Data Landscape)

Để thiết kế một nền tảng thu thập và chuẩn hóa vững chắc, kỹ sư dữ liệu phải nắm vững ngữ nghĩa API cụ thể, thế mạnh cũng như các kịch bản lỗi của các nhà cung cấp dữ liệu học thuật lớn.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        CÁC NHÀ CUNG CẤP DỮ LIỆU HỌC THUẬT                              │
├────────────────────┬────────────────────┬────────────────────┬─────────────────────────┤
│       arXiv        │      OpenAlex      │      Crossref      │    Semantic Scholar     │
├────────────────────┼────────────────────┼────────────────────┼─────────────────────────┤
│ * Tốc độ: Vài giờ  │ * Tốc độ: Hàng tuần│ * Tốc độ: Vài ngày │ * Tốc độ: Hàng tuần     │
│ * Preprints        │ * Đồ thị Mở toàn cầu│* Bản ghi NXB gốc  │ * Ý định trích dẫn      │
│ * Văn bản thô      │ * ROR / Khái niệm  │ * Thẩm quyền DOI   │ * Trích dẫn ảnh hưởng   │
│ * Tóm tắt mã TeX   │ * Chỉ mục đảo      │ * JATS XML/Paywall │ * PaperId / CorpusId    │
└────────────────────┴────────────────────┴────────────────────┴─────────────────────────┘
```

### 2.1 arXiv (Kho Lưu trữ Preprint Tiên phong)
* **SỰ THẬT**: Được thành lập năm 1991, arXiv là kho lưu trữ bản thảo sơ bộ (preprint) hàng đầu cho Vật lý, Toán học, Khoa học Máy tính, Sinh học Định lượng và Học máy.
* **SỰ THẬT**: Endpoint OAI-PMH chính thức là `https://oaipmh.arxiv.org/oai` (giao thức v2.0).
* **SỰ THẬT**: Các định danh tuân theo hai quy ước:
  - *Định dạng hiện đại* (sau năm 2007): `YYMM.NNNNN` (ví dụ: `1706.03762`), kèm hậu tố phiên bản tùy chọn `vN` (ví dụ: `1706.03762v5`).
  - *Định dạng cũ* (trước năm 2007): `arch-ive/YYMMNNN` (ví dụ: `hep-th/9901001`).
* **SỰ THẬT**: arXiv cung cấp siêu dữ liệu qua OAI-PMH (XML) theo các định dạng: `arXiv` (chuẩn), `arXivRaw` (lịch sử phiên bản), và `oai_dc` (Dublin Core).
* **Ngữ nghĩa Định danh Preprint (Work != Version)**:
  - Một đóng góp trên arXiv trải qua các trạng thái phiên bản (`v1`, `v2`, `v3`).
  - **Định danh Work Chuẩn hóa**: Được sinh ra có tính xác định từ định danh không chứa phiên bản (`arxiv:YYMM.NNNNN`), đảm bảo tất cả các phiên bản đều được phân giải về cùng một thực thể work chuẩn hóa duy nhất.
  - **Quan sát Phiên bản**: Được lưu trữ không mất mát ở tầng Silver (`source_work_observations`), bảo toàn sự tiến hóa theo thời gian của tóm tắt, tiêu đề và các sửa đổi tác giả.
* **Ngữ nghĩa & Đặc thù**:
  - Không có đồ thị trích dẫn nội tại.
  - Thông tin tác giả là các chuỗi thô, không có ID tổ chức và hiếm khi có ORCID; quá trình phân tích XML trích xuất họ (keynames), tên (forenames) và chuỗi cơ quan trực thuộc chưa qua xử lý.
  - Văn bản tóm tắt thường xuyên chứa các lệnh định dạng LaTeX (ví dụ: `$\mathcal{O}(n \log n)$`, `\textbf{Transformer}`). Parser phải áp dụng phương pháp chuẩn hóa không phá hủy (giữ nguyên công thức toán trong khi giải mã các thực thể XML an toàn).
  - Resumption tokens hết hạn hàng ngày và không chứa siêu dữ liệu về con trỏ hay tổng độ dài; việc phân trang dừng lại khi thẻ `<resumptionToken/>` rỗng được trả về.
  - Các bài bị xóa được báo hiệu thông qua bia mộ `<header status="deleted">`.
* **Vai trò trong Pipeline**: Cảm biến thời gian sớm nhất phát hiện các đột phá công nghệ và các mô hình kiến trúc mới nổi.

### 2.2 OpenAlex (Đồ thị Học thuật Mở Toàn diện)
* **SỰ THẬT**: Kế thừa Microsoft Academic Graph (MAG), do OurResearch vận hành, lập danh mục cho hơn 250 triệu công trình.
* **SỰ THẬT**: Cung cấp các REST API có cấu trúc và bản kết xuất tệp phẳng hàng tháng trên AWS S3 / Databricks.
* **SỰ THẬT**: ID thực thể là các chuỗi định dạng URI với tiền tố kiểu cụ thể:
  - Work: `https://openalex.org/W...`
  - Author: `https://openalex.org/A...`
  - Source/Venue: `https://openalex.org/S...`
  - Institution: `https://openalex.org/I...`
  - Topic/Concept: `https://openalex.org/T...` hoặc `C...`
* **Ngữ nghĩa & Đặc thù**:
  - Phần tóm tắt được lưu dưới dạng **chỉ mục đảo (inverted index)** (`abstract_inverted_index`: `{"word": [pos1, pos2]}`) nhằm tuân thủ quy định bản quyền của các nhà xuất bản. Cần thuật toán tái tạo để chuyển đổi cấu trúc này lại thành văn bản đọc được.
  - Khử nhập nhằng tác giả và viện nghiên cứu bằng các mô hình học máy độc quyền. Tác giả được liên kết với ROR ID.
  - Tài liệu tham khảo được cung cấp dưới dạng danh sách URI OpenAlex Work (`referenced_works: ["https://openalex.org/W..."]`).
* **Vai trò trong Pipeline**: Xương sống cấu trúc tô-pô toàn cầu, ánh xạ viện/trường và phân loại chủ đề tự động.

### 2.3 Crossref (Sổ Đăng ký DOI của Nhà Xuất bản)
* **SỰ THẬT**: Cơ quan đăng ký Định danh Đối tượng Số (DOI) chính thức cho xuất bản học thuật, bao gồm các nhà xuất bản thương mại, hiệp hội học thuật và xuất bản mở.
* **SỰ THẬT**: Khóa chính là DOI đã chuẩn hóa (ví dụ: `10.1145/3292500.3330964`).
* **Ngữ nghĩa & Đặc thù**:
  - Nguồn chân lý có thẩm quyền cao nhất cho siêu dữ liệu **bản ghi chính thức (Version of Record - VoR)**: ngày xuất bản chính thức, tên tạp chí/hội thảo chuẩn mực, tập (volume), số (issue), số trang và tên nhà xuất bản.
  - Cơ quan trực thuộc của tác giả là các chuỗi văn bản không đồng nhất do nhà xuất bản gửi trực tiếp (ví dụ: `"Dept of CS, Stanford Univ, CA"` so với `"Stanford University"`).
  - Danh sách tài liệu tham khảo được gửi dưới dạng văn bản thư mục phi cấu trúc hoặc danh sách một phần các DOI đích. Nhiều nhà xuất bản thương mại bỏ qua danh mục tham khảo trừ khi tham gia Sáng kiến Trích dẫn Mở (I4OC).
* **Vai trò trong Pipeline**: Thẩm quyền cao nhất về ngày xuất bản sau bình duyệt, tên nơi xuất bản chính thức và xác thực đăng ký DOI.

### 2.4 Semantic Scholar (S2AG - Viện Trí tuệ Nhân tạo Allen)
* **SỰ THẬT**: Công cụ tìm kiếm học thuật và đồ thị mở lập chỉ mục hơn 200 triệu bài báo, cung cấp API và bộ dữ liệu Semantic Scholar Academic Graph (S2AG).
* **SỰ THẬT**: Các định danh chính gồm `paperId` (chuỗi băm SHA1 hex 40 ký tự) và `corpusId` (số nguyên). Các ánh xạ ID ngoài gồm `DOI`, `ArXiv`, `PubMed`, `DBLP`, và `ACL`.
* **Ngữ nghĩa & Đặc thù**:
  - Tiên phong trong **Mô hình hóa Trích dẫn theo Ngữ cảnh**: phân loại trích dẫn theo ý định (`Methodology`, `Background`, `Result`) và gắn cờ các trích dẫn có tầm ảnh hưởng (`isInfluential`) dựa trên số lượng trích dẫn, tần suất nhắc đến trong nội dung bài báo và cảm xúc của đoạn trích dẫn.
  - Tính toán các chỉ số thuật toán: `citationCount`, `referenceCount`, và `influentialCitationCount`.
* **Vai trò trong Pipeline**: Bộ lọc nhiễu tín hiệu cao, cho phép các công cụ khai phá xu hướng công nghệ bỏ qua các trích dẫn bề nổi và tập trung vào những sự kế thừa phương pháp luận thực chất.

---

## 3. Mô hình hóa Dữ liệu Chuẩn hóa (Canonical Data Modeling)

### 3.1 Định nghĩa Kiến trúc
```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                     MÔ HÌNH DỮ LIỆU CHUẨN HÓA (CDM)                              │
├──────────────────────────────────────────────────────────────────────────────────┤
│ Một biểu diễn miền dữ liệu tập trung, chuẩn mực giúp tách rời các bên sản xuất   │
│ dữ liệu thượng nguồn (upstream) khỏi các bên tiêu thụ phân tích hạ nguồn.         │
└──────────────────────────────────────────────────────────────────────────────────┘
```

* **SỰ THẬT**: Xuất phát từ mẫu kiến trúc Tích hợp Doanh nghiệp (Enterprise Integration Patterns - Hohpe & Woolf), Mô hình Dữ liệu Chuẩn hóa loại bỏ vấn đề dịch chuyển điểm-tới-điểm phức tạp $O(N^2)$ bằng cách định tuyến tất cả các schema nguồn qua một giao ước trung gian có thẩm quyền độ phức tạp $O(N)$.
* **SUY LUẬN**: Trong kiến trúc dữ liệu học thuật, Mô hình Chuẩn hóa KHÔNG đơn thuần là một vỏ bọc chứa JSON thô; nó là một schema quan hệ được chuẩn hóa và định kiểu nghiêm ngặt, hài hòa các mô hình thực thể không đồng nhất trong khi vẫn bảo toàn đầy đủ nguồn gốc lịch sử quan sát ban đầu.

### 3.2 So sánh Mô hình Quan hệ vs. Bán cấu trúc vs. Dạng tài liệu
Các kiến trúc sư dữ liệu phải đánh đổi khi lựa chọn cấu trúc lưu trữ trong DuckDB:

| Tiêu chí | Quan hệ Chuẩn hóa Hoàn toàn (3NF / Star) | Tài liệu Bán cấu trúc (Nested JSON) | Lai: Quan hệ + Mảng Định kiểu (`LIST` / `STRUCT`) |
| :--- | :--- | :--- | :--- |
| **Công cụ Lưu trữ** | Dạng cột (Native vectors của DuckDB) | Blob JSON văn bản/nhị phân | Mảng định kiểu dạng cột |
| **Hiệu năng Join** | Cao (Hash join được vector hóa) | Thấp (Đòi hỏi parse JSON lúc chạy) | Cao cho bảng cha; Cần unnest cho bảng con |
| **Thực thi Ràng buộc** | Đầy đủ (PK, UNIQUE, FK, CHECK) | Không có (Schema-on-read) | PK trên cha; Không có FK/UNIQUE trên phần tử lồng |
| **Tiến hóa Schema** | Đòi hỏi migration tường minh (`ALTER`) | Linh hoạt không ma sát | Linh hoạt ở cấp mảng; migration cho struct |
| **Tiện ích SQL Phân tích**| Chuẩn SQL (`GROUP BY`, Window) | Rườm rà (`json_extract_string`, ...) | Rất cao với list comprehensions / `UNNEST` |
| **Tầng Kiến trúc** | **Gold (Tầng Chuẩn hóa)** | **Bronze (Tầng Lưu trữ Thô)** | **Silver (Tầng Quan sát Chuẩn hóa)** |

### 3.3 Các Thực thể Học thuật Cốt lõi
Một nền tảng học thuật chuẩn hóa mô hình hóa sáu khái niệm nghiệp vụ nền tảng:
1. **Work (Bài báo/Công trình)**: Một đóng góp trí tuệ trừu tượng (ví dụ: bài báo, preprint, kỷ yếu hội thảo, bài tổng quan).
2. **Author (Tác giả)**: Một nhà nghiên cứu cá nhân đóng góp vào đầu ra trí tuệ.
3. **Institution (Cơ quan/Viện trường)**: Một thực thể tổ chức (đại học, viện nghiên cứu, doanh nghiệp) mà các tác giả trực thuộc.
4. **Venue (Nơi xuất bản)**: Một nền tảng công bố khoa học (tạp chí, kỷ yếu hội nghị, hội thảo, máy chủ preprint).
5. **Authorship / Contribution (Quan hệ Tác giả)**: Bảng nối nhiều-nhiều ràng buộc Tác giả với Bài báo, được bổ sung các thuộc tính như thứ tự tác giả và đơn vị công tác tại thời điểm xuất bản.
6. **Citation (Trích dẫn)**: Một cạnh bằng chứng có hướng nối từ Bài báo trích dẫn đến Bài báo được trích dẫn, kèm theo ngữ cảnh, ý định và mốc thời gian.

---

## 4. Định danh Thực thể (Entity Identity)

### 4.1 Khái niệm: Bản sắc (Identity) vs. Định danh (Identifier) vs. Trạng thái (State)
```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                       KIẾN TRÚC ĐỊNH DANH THỰC THỂ                                │
├───────────────────┬───────────────────────────────────────────────────────────────┤
│ Khái niệm         │ Định nghĩa trong Kỹ thuật Dữ liệu Học thuật                   │
├───────────────────┼───────────────────────────────────────────────────────────────┤
│ Source ID         │ Định danh nội bộ của nhà cung cấp (ví dụ: OpenAlex `W123`...)  │
│ Source Identity Key│ Khóa định kiểu đã chuẩn hóa (ví dụ: `doi:10.1145/...`)        │
│ Candidate Cluster │ Tập hợp các khóa định danh nguồn trỏ về cùng một bài báo      │
│ Canonical ID      │ Khóa đại diện xác định biểu diễn cho thực thể thế giới thực    │
│ Entity State      │ Giá trị các thuộc tính có thể biến đổi (tiêu đề, trích dẫn...) │
└───────────────────┴───────────────────────────────────────────────────────────────┘
```

* **Vì sao điều này quan trọng**: Việc đánh đồng khóa định danh có nguồn gốc từ bên ngoài với định danh chuẩn hóa sẽ dẫn đến việc phân mảnh các cụm thực thể. Nếu một hệ thống ngây thơ sinh `UUIDv5(namespace_doi, doi)` và một hệ thống khác sinh `UUIDv5(namespace_arxiv, arxiv_id)` một cách độc lập, thì cùng một bài báo xuất hiện từ arXiv rồi sau đó từ Crossref sẽ tạo ra hai UUID "chuẩn hóa" tách rời nhau!
* **Nguyên tắc Mô hình hóa Chuẩn mực**:
  1. Phân biệt rõ **Khóa Định danh Bắt nguồn từ Nguồn** với **Định danh Chuẩn hóa Đã Phân giải**.
  2. Công cụ nạp dữ liệu trích xuất tất cả các khóa đã chuẩn hóa từ một bản ghi nguồn (`doi:...`, `arxiv:...`, `s2:...`).
  3. Bộ giải quyết tìm kiếm trong chỉ mục `canonical_work_identifiers` hiện có.
  4. Nếu bất kỳ khóa nào khớp với một thực thể chuẩn hóa hiện có, `canonical_work_id` đó sẽ được giữ lại.
  5. Chỉ khi KHÔNG tìm thấy bất kỳ sự trùng khớp nào, hệ thống mới sinh ra một `canonical_work_id` mới mang tính xác định từ khóa neo chính đã giải quyết (ví dụ: `UUIDv5(NAMESPACE_CANONICAL_WORK, primary_key)` với mức ưu tiên: `doi:` > `arxiv:` > khóa cụm nội bộ).

---

## 5. Phân giải Thực thể & Khử Trùng lặp (Entity Resolution & Deduplication)

### 5.1 Khử trùng lặp vs. Phân giải Thực thể
* **SỰ THẬT**: **Khử trùng lặp (Deduplication)** là việc loại bỏ các bản ghi trùng lặp chính xác bên trong một nguồn hoặc tập dữ liệu đơn lẻ.
* **SỰ THẬT**: **Phân giải Thực thể (Entity Resolution - ER)** là nhiệm vụ xác suất hoặc xác định nhằm xác minh xem hai bản ghi riêng biệt—xuất phát từ các schema, mốc thời gian hoặc nguồn khác nhau—có cùng đề cập đến một thực thể thực tế trong thế giới thực hay không.

### 5.2 Chiến lược Phân giải Đa bước Xác định & Các Cấp độ Khớp
Trong các nền tảng dữ liệu học thuật, việc phân giải thực thể phải phân loại độ tin cậy của sự trùng khớp một cách rõ ràng thay vì tự động gộp mù quáng:

```
┌───────────────────┬───────────────────────────┬───────────────────────────────────────┐
│ Cấp độ Khớp       │ Quy tắc Bằng chứng        │ Hành động Phân giải                   │
├───────────────────┼───────────────────────────┼───────────────────────────────────────┤
│ **EXACT_MATCH**   │ Khớp DOI đã chuẩn hóa     │ Tự động hợp nhất chuẩn hóa            │
│ **EXACT_MATCH**   │ Khớp arXiv ID đã chuẩn hóa│ Tự động hợp nhất chuẩn hóa            │
│ **PROBABLE_MATCH**│ Dấu vân tay Tiêu đề +     │ CHỈ LÀ ỨNG VIÊN: Ghi vào hàng đợi     │
│                   │ Năm + Tác giả             │ xem xét; KHÔNG tự gộp để tránh va chạm│
│ **NO_MATCH**      │ Không khớp khóa nào đã biết│ Tạo mới thực thể chuẩn hóa            │
└───────────────────┴───────────────────────────┴───────────────────────────────────────┘
```

* **Quy tắc Tối quan trọng về Dấu vân tay (Fingerprints)**: Các dấu vân tay tổng hợp (`title_slug + publication_year + first_author`) **TUYỆT ĐỐI KHÔNG BAO GIỜ** được kích hoạt việc tự động hợp nhất chuẩn hóa trong pipeline sản xuất. Sự khác biệt giữa phiên bản hội nghị, bài mở rộng trên tạp chí, đính chính (corrigenda), preprint và hiện tượng trùng tên tác giả sẽ tạo ra các va chạm dương tính giả (false-positive collisions) vô cùng nghiêm trọng. Khớp dấu vân tay chỉ được gắn nhãn `CANDIDATE_ONLY`.

---

## 8. Mô hình hóa Đồ thị Trích dẫn & Vòng đời Stub (Citation Graph Modeling & Stub Lifecycle)

### 8.1 Các Đặc tính Đồ thị Có hướng
* **SỰ THẬT**: Đồ thị trích dẫn học thuật là một đồ thị có hướng trong thế giới mở, nơi các bài báo trích dẫn tham chiếu đến những tài liệu nằm ngoài phạm vi cơ sở dữ liệu cục bộ hiện có.

### 8.2 Ngữ nghĩa Thực thể Thế chỗ (Stub) & Lộ trình Nâng cấp
Khi bài báo $P$ trích dẫn một công trình chưa được lập chỉ mục, chỉ được định danh qua DOI `10.1234/xyz`:
1. **Khởi tạo Stub**: Hệ thống cấp phát một bài báo stub trong bảng `canonical_works`:
   - `canonical_work_id = UUIDv5(NAMESPACE_CANONICAL_WORK, "doi:10.1234/xyz")`
   - `is_stub = TRUE`
   - `stub_reason = 'DANGLING_CITATION_TARGET'`
   - `created_from_source = 'semantic_scholar'`
   - `title = '[Stub Citation Target: 10.1234/xyz]'`
2. **Toàn vẹn Tham chiếu**: Cạnh trích dẫn trong `canonical_citations` tham chiếu `citing_work_id` và `cited_work_id` mà không vi phạm khóa ngoại.
3. **Nâng cấp từ Stub lên Chuẩn hóa**:
   - Khi siêu dữ liệu nguồn thực tế cho `10.1234/xyz` sau đó được nạp vào (ví dụ từ Crossref hoặc OpenAlex):
   - Bộ phân giải tìm thấy bài báo stub hiện có thông qua `canonical_work_identifiers`.
   - Thay vì chèn bài báo mới, hệ thống **nâng cấp tại chỗ** bản ghi stub:
     `UPDATE canonical_works SET is_stub = FALSE, title = ?, abstract = ?, updated_at = ? WHERE canonical_work_id = ?`
   - Tất cả các cạnh trích dẫn trỏ đến trước đó ngay lập tức liên kết với bài báo chuẩn hóa đầy đủ thông tin mà không làm gãy khóa ngoại hay sinh ra thực thể trùng lặp!

---

## 9. Kiến trúc Nguồn gốc & Dòng Dữ liệu (Provenance & Lineage Architecture)

### 9.1 Bốn Tầng của Dòng Dữ liệu & Nguồn gốc
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       KIẾN TRÚC DÒNG DỮ LIỆU & NGUỒN GỐC                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Dòng dữ liệu Lần chạy (`ingestion_runs`):                                │
│    run_id, nguồn, URI đầu vào, mã băm, số lượng bản ghi, phiên bản, thời gian│
│ 2. Lưu trữ Tệp Thô & Payload (`raw_source_manifest` / `raw_records`):       │
│    Tệp bất biến trên đĩa + xác thực mã băm payload SHA256                   │
│ 3. Quan sát Cấp độ Bản ghi (`source_work_observations`):                    │
│    nguồn, source_work_id, thời điểm quan sát, thuộc tính chuẩn hóa, run_id   │
│ 4. Nguồn gốc Cấp độ Thuộc tính (`canonical_work_provenance`):               │
│    canonical_work_id, attribute_name, winning_source, source_observation_id │
└─────────────────────────────────────────────────────────────────────────────┘
```

* **Loại bỏ Khái niệm Trùng lặp**:
  - `source_work_observations` ghi lại toàn bộ ảnh chụp quan sát thực thể từ nguồn tại lần chạy đó.
  - `canonical_work_provenance` ghi lại con trỏ dòng dữ liệu: `source_observation_id` nào đã chiến thắng cho từng thuộc tính chuẩn hóa (`title`, `abstract`, `venue`, `publication_date`).
  - `metrics_provenance` được dành riêng cho các ảnh chụp chuỗi thời gian ghi nối tiếp (append-only) của các chỉ số biến động (`citation_count`, `influential_citation_count`) được ghi nhận qua các lần nạp liên tiếp.

---

## 15. Khung Khẳng định Chất lượng Dữ liệu & Cách ly (Data Quality Assertion Framework & Quarantine)

Các pipeline dữ liệu phải thực thi các ràng buộc Chất lượng Dữ liệu (DQ) rõ ràng với các mức độ nghiêm trọng và hành động xử lý được xác định trước:

```
┌────────┬─────────────────────────────┬───────────┬───────────────────────────────────────────┐
│ Quy tắc│ Điều kiện / Khẳng định      │ Mức độ    │ Hành động khi Vi phạm                     │
├────────┼─────────────────────────────┼───────────┼───────────────────────────────────────────┤
│ **DQ-01**│ Định dạng ID & Checksum     │ REJECT_ID │ Cách ly ID lỗi định dạng; tiếp tục parse  │
│        │ (Hợp lệ DOI / arXiv / ORCID)│           │ nếu còn định danh thay thế khác.          │
│ **DQ-02**│ Độ hoàn thiện của Tiêu đề   │ QUARANTINE│ Bác bỏ toàn bộ bản ghi sang bảng          │
│        │ (độ dài >= 3, không giữ chỗ)│           │ `quarantine`; loại khỏi phân giải Gold.   │
│ **DQ-03**│ Giới hạn Năm Xuất bản       │ SANITIZE  │ Đặt `publication_year = NULL`; ghi log    │
│        │ (1665 <= year <= hiện_tại+1)│           │ cảnh báo; cho phép nạp canonical.         │
│ **DQ-04**│ Cạnh Đồ thị Trích dẫn Hợp lệ│ DROP_EDGE │ Bỏ trích dẫn chính mình (`citing==cited`);│
│        │ (`citing_id != cited_id`)   │           │ ngăn chặn vòng lặp tự thân lặp lại.       │
│ **DQ-05**│ Tính Hợp lệ của Tác giả     │ SANITIZE  │ Mặc định vị trí >= 1; giữ lại đề cập tác  │
│        │ (vị trí >= 1, tên != '')    │           │ giả hợp lệ; bỏ các tên rỗng.              │
└────────┴─────────────────────────────┴───────────┴───────────────────────────────────────────┘
```

---

## 6. Chiến lược Định danh (Identifier Strategy)

### 6.1 Phân tích Định danh Có Hệ thống
Hệ thống học thuật tương tác với sáu nhóm định danh chính:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             PHÂN LOẠI ĐỊNH DANH HỌC THUẬT                                │
├───────────────┬─────────────────────────┬──────────────────┬─────────────────────────────┤
│ Định danh     │ Đối tượng Thế giới Thực │ Tiêu chuẩn Cú pháp│ Quy tắc Chuẩn hóa           │
├───────────────┼─────────────────────────┼──────────────────┼─────────────────────────────┤
│ **DOI**       │ Bài báo, Tập dữ liệu    │ ISO 26324        │ Chữ thường, bỏ `https://`   │
│ **arXiv ID**  │ Preprints               │ Chuẩn arXiv      │ Chữ thường, bỏ `vN`         │
│ **ORCID**     │ Tác giả                 │ ISO 7746         │ 16 ký tự có gạch nối, số KT │
│ **ROR ID**    │ Viện / Trường           │ ROR Schema v2    │ URL thường hoặc mã 9 ký tự  │
│ **OpenAlex ID**│ Bài báo/Tác giả/Venue   │ URI OpenAlex     │ Trích xuất Tiền tố + Chữ số │
│ **S2 PaperId**│ Bài báo trên S2         │ SHA1 Hex 40 ký tự│ Chữ thường hex 40 ký tự     │
└───────────────┴─────────────────────────┴──────────────────┴─────────────────────────────┘
```

### 6.2 Các Thuật toán Chuẩn hóa
* **Chuẩn hóa DOI**:
  $$N(\text{DOI}) = \text{lower}\Big(\text{regex\_replace}\big(\text{raw}, \text{`\^(https?://(dx\.)?doi\.org/\|doi:)'}, \text{`'}\big)\Big)$$
  *Ví dụ*: `https://doi.org/10.1145/3292500.3330964` $\longrightarrow$ `10.1145/3292500.3330964`
* **Chuẩn hóa arXiv ID**:
  $$N(\text{arXiv}) = \text{lower}\Big(\text{regex\_replace}\big(\text{regex\_replace}(\text{raw}, \text{`\^arxiv:'}, \text{`'}\big), \text{`v[0-9]+$'}, \text{`'}\big)\Big)$$
  *Ví dụ*: `arXiv:1706.03762v5` $\longrightarrow$ `1706.03762`
  *Điểm phân biệt cốt lõi*: ID không chứa phiên bản đại diện cho *bài báo chuẩn hóa (canonical work)*; ID có phiên bản đại diện cho *quan sát nguồn (source observation)* cụ thể.
* **Chuẩn hóa ORCID**:
  $$N(\text{ORCID}) = \text{regex\_extract}\big(\text{raw}, \text{`[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]'}\big)$$
  *Xác thực*: Phải thỏa mãn xác minh số kiểm tra theo ISO/IEC 7064 MOD 11-2.

### 6.3 Mô hình hóa Quan hệ cho các Định danh Bên ngoài
* **Câu hỏi A**: Có nên lưu các ID bên ngoài dưới dạng `STRUCT(source VARCHAR, id VARCHAR)[]` trên bảng `works`, hay lưu trong một bảng quan hệ riêng biệt `work_identifiers`?
* **Phân tích Đánh đổi**:
  - `STRUCT[]` bên trong `works`:
    - *Ưu điểm*: Gọn gàng khi tuần tự hóa; lấy toàn bộ ID chỉ với một dòng đọc.
    - *Nhược điểm*: Giảm hiệu năng đánh chỉ mục nghiêm trọng trong DuckDB. Tìm kiếm thực thể theo DOI yêu cầu hàm unnest hoặc lọc danh sách lambda (`list_filter(...)`). DuckDB không thể thực thi ràng buộc `UNIQUE` trên các phần tử trong mảng, dẫn đến việc nhiều bài báo có thể trùng DOI.
  - Bảng `work_identifiers` riêng biệt:
    - *Ưu điểm*: Cho phép đặt khóa chính phức hợp `(identifier_type, normalized_value) PRIMARY KEY`, đảm bảo không có hai bài báo chuẩn hóa nào cùng nhận một DOI. Cho phép tra cứu B-Tree được vector hóa tức thì phục vụ khử trùng lặp khi nạp dữ liệu.
* **QUYẾT ĐỊNH THIẾT KẾ**:
  **Áp dụng Kiến trúc Lai (Hybrid Architecture).**
  1. Duy trì một bảng quan hệ chuyên dụng được đánh chỉ mục `canonical_work_identifiers` để đảm bảo tính duy nhất tuyệt đối, phân giải thực thể đa bước và tra cứu hai chiều.
  2. Hiện thực hóa các khóa tra cứu có tần suất sử dụng cao (`canonical_doi`, `canonical_arxiv_id`) dưới dạng các cột cấp một được đánh chỉ mục trực tiếp trên `canonical_works` để đạt hiệu năng phân tích tức thì không cần join bảng.

---

## 7. Mô hình hóa Mối quan hệ (Relationship Modeling)

### 7.1 Mối quan hệ Nhiều-Nhiều giữa Bài báo và Tác giả
Mối quan hệ giữa Bài báo và Tác giả không phải là một phép join đơn giản; nó chứa các thuộc tính miền quan trọng:
* **Thứ tự / Vị trí**: Tác giả đầu tiên (chủ trì nghiên cứu), tác giả cuối cùng (tác giả cao cấp/tác giả liên hệ trong y sinh), hoặc sắp xếp theo bảng chữ cái (phổ biến trong toán thuần túy/khoa học máy tính lý thuyết).
* **Trạng thái Tác giả Liên hệ (Corresponding Status)**: Cờ boolean cho biết trách nhiệm liên hệ pháp lý của bài báo.
* **Cơ quan Trực thuộc tại thời điểm Xuất bản**: Một tác giả có thể chuyển từ Stanford sang Google DeepMind. Đơn vị công tác lịch sử của họ trên bài báo năm 2017 vẫn phải là Stanford, ngay cả khi hồ sơ hiện tại của họ ghi nhận Google DeepMind.

```
┌─────────────────┐       ┌───────────────────────────────┐       ┌──────────────────┐
│ canonical_works │───1:N─┤ canonical_work_authors        │─N:1───│ canonical_authors│
└─────────────────┘       ├───────────────────────────────┤       └──────────────────┘
                          │ * canonical_work_id (FK)      │
                          │ * canonical_author_id (FK)    │
                          │ * canonical_institution_id(FK)│
                          │ * author_position (INT)       │
                          │ * raw_author_name (VARCHAR)   │
                          │ * raw_affiliation_str (VARCHAR)
                          └───────────────────────────────┘
```

* **Kịch bản Lỗi**: Gán tác giả trực tiếp vào viện nghiên cứu hiện tại của họ, phá hủy bằng chứng lịch sử về đơn vị công tác tại thời điểm nghiên cứu được xuất bản.
* **Nguyên tắc Mô hình hóa Chuẩn xác**:
  `canonical_work_authors` ghi lại trạng thái chụp nhanh của tên tác giả và đơn vị công tác *tại thời điểm xuất bản*, trong khi các khóa ngoại liên kết tới các thực thể chuẩn hóa.

---

## 8. Mô hình hóa Đồ thị Trích dẫn (Citation Graph Modeling)

### 8.1 Đặc tính Đồ thị Có hướng
* **SỰ THẬT**: Đồ thị trích dẫn học thuật về mặt lý thuyết là một đồ thị có hướng không chu trình (DAG - bài báo trích dẫn quá khứ), nhưng trên thực tế lại chứa các chu trình do các trích dẫn preprint diễn ra đồng thời, trích dẫn chéo trong các tập san chuyên đề và sự sai lệch về độ trễ xuất bản.
* **SỰ THẬT**: Mật độ đồ thị phân bố lệch mạnh theo quy luật lũy thừa (power-law): 1% bài báo thu hút 90% tổng số lượt trích dẫn.

### 8.2 Vấn đề Cạnh Lơ lửng trong Không gian Mở (Open-World Dangling Edge Problem)
* **Khái niệm**: Khi nạp một bài báo mới xuất bản $P$, nó trích dẫn 40 bài báo cũ hơn $C_1, \dots, C_{40}$. Phần lớn các bài được trích dẫn này có thể chưa từng tồn tại trong cơ sở dữ liệu DuckDB nội bộ của chúng ta.
* **Kịch bản Lỗi**:
  Thực thi ràng buộc khóa ngoại quan hệ nghiêm ngặt:
  ```sql
  CREATE TABLE citations (
      citing_work_id VARCHAR REFERENCES works(canonical_work_id),
      cited_work_id VARCHAR REFERENCES works(canonical_work_id)
  );
  ```
  *Hậu quả*: Việc nạp bài báo $P$ sẽ sập ngay lập tức với lỗi `ConstraintException: Violates foreign key constraint` do thiếu các bài $C_1, \dots, C_{40}$.
* **Các Giải pháp Kiến trúc**:
  1. **Phương án A: Bảng Cạnh Đồ thị Không ràng buộc**: Bỏ khóa ngoại trên `cited_work_id`. Lưu ID chuẩn hóa nếu biết, hoặc lưu định danh đích đã chuẩn hóa (ví dụ: DOI đích).
  2. **Phương án B: Tự động Khởi tạo Thực thể Thế chỗ (Stub Entity)**: Khi bắt gặp một bài báo được trích dẫn chưa lập chỉ mục, tạo động một bản ghi "stub" trong `canonical_works` với `is_stub = TRUE`, chỉ điền các định danh đã biết.
* **QUYẾT ĐỊNH THIẾT KẾ**:
  Triển khai **Phương án B với Lưu trữ Cạnh Hai Tầng**:
  - `canonical_citations` duy trì tính toàn vẹn tham chiếu nghiêm ngặt bằng cách tự động chèn các bài báo stub gọn nhẹ (`is_stub = TRUE`) khi bài đích chưa được phân giải.
  - `citation_context` lưu trữ ý định trích dẫn (`Methodology`, `Background`, `Result`) và các cờ `is_influential` bắt nguồn từ Semantic Scholar.

---

## 9. Nguồn gốc Dữ liệu (Provenance)

### 9.1 Các Cấp độ Nguồn gốc
Dòng dữ liệu trong các hệ thống dữ liệu khoa học vận hành trên ba mức độ chi tiết khác nhau:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CÁC CẤP ĐỘ NGUỒN GỐC                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Nguồn gốc Lần chạy Pipeline: Tem thời gian, git commit, cấu hình runtime │
│ 2. Nguồn gốc Cấp độ Bản ghi: Nhà cung cấp nguồn, mã băm payload, lô nạp     │
│ 3. Nguồn gốc Cấp độ Thuộc tính: Nguồn nào đã cung cấp tiêu đề, năm, venue   │
└─────────────────────────────────────────────────────────────────────────────┘
```

* **Vì sao điều này quan trọng**: Nếu OpenAlex báo cáo 150 trích dẫn và Semantic Scholar báo cáo 95 trích dẫn, nền tảng dữ liệu không thể tùy tiện chọn một con số mà không ghi lại siêu dữ liệu quan sát. Một bài báo nghiên cứu thực nghiệm khi trích dẫn các con số này phải có khả năng tái lập lại chính xác trạng thái đã quan sát vào ngày hôm đó.

### 9.2 Quan sát (Observation) vs. Trạng thái Hiện tại (Current State)
* **Khái niệm**:
  - **Quan sát Nguồn (Source Observation)**: Bản ghi bất biến, chỉ ghi nối tiếp (append-only) về những gì API bên ngoài đã trả về tại một mốc thời gian cụ thể.
  - **Trạng thái Hiện tại (Current State)**: Góc nhìn tổng hợp, hợp nhất hiện đang được chấp nhận là chuẩn mực có thẩm quyền.
* **Kịch bản Lỗi**:
  Ghi đè trực tiếp trạng thái hiện tại qua `ON CONFLICT DO UPDATE` mà không lưu lại quan sát lịch sử. Nếu nhà cung cấp thượng nguồn gặp lỗi hoặc đưa vào dữ liệu sai hỏng, quan sát hợp lệ ban đầu sẽ bị phá hủy vĩnh viễn.
* **Nguyên tắc Mô hình hóa Chuẩn xác**:
  **Không bao giờ sửa đổi các quan sát.** Các quan sát được ghi vào tầng Silver chỉ ghi thêm (`source_work_observations`). Tầng Gold (`canonical_works`) là một hình chiếu mang tính xác định được suy ra từ các quan sát này thông qua các chính sách phân giải minh bạch.

---

## 10. Xung đột & Bất đồng Nguồn (Source Conflicts & Disagreements)

### 10.1 Các Kịch bản Bất đồng Điển hình
Các bộ tổng hợp học thuật thường xuyên báo cáo siêu dữ liệu mâu thuẫn cho cùng một bài báo:

| Thuộc tính | Nguồn A (ví dụ: arXiv) | Nguồn B (ví dụ: Crossref) | Nguyên nhân Gốc rễ của Bất đồng |
| :--- | :--- | :--- | :--- |
| **Năm Xuất bản** | `2021` (Ngày preprint) | `2023` (Ngày in tạp chí) | Định nghĩa khác nhau về "xuất bản" |
| **Tiêu đề** | `"BERT: Pre-training of Deep..."` | `"BERT: PRE-TRAINING OF DEEP..."` | Phong cách sắp chữ của nhà xuất bản |
| **Số lượng Tác giả**| 5 tác giả | 3 tác giả + "et al." | Cắt bớt trong lập chỉ mục thứ cấp |
| **Tên Nơi xuất bản**| `"arXiv.org"` | `"NAACL-HLT 2019"` | Nâng hạng xuất bản sau bình duyệt |

### 10.2 Hệ thống Phân cấp Giải quyết Xung đột
Để giải quyết các xung đột thuộc tính một cách xác định mà không cần can thiệp thủ công của con người, bộ máy chuẩn hóa triển khai một **Ma trận Ưu tiên Nguồn Thẩm quyền (Source Authority Priority Matrix)**:

```
Thuộc tính: Ngày Xuất bản & Nơi xuất bản (Publication Date & Venue)
Crossref (Bản ghi NXB VoR) > OpenAlex (Đã kiểm chứng) > S2AG > arXiv (Dự phòng preprint)

Thuộc tính: Tốc độ & Ý định Trích dẫn (Citation Velocity & Intents)
Semantic Scholar (S2AG) > OpenAlex > Crossref (Chỉ tham chiếu tĩnh)

Thuộc tính: Tóm tắt & Chủ đề (Abstract & Topics)
Semantic Scholar (Văn bản sạch) > arXiv (Toàn văn TeX) > OpenAlex (Dựng lại từ Inverted Index)

Thuộc tính: Phân cấp Cơ quan / Viện trường (Institutional Hierarchy)
OpenAlex (Chuẩn ROR) > Crossref (Chuỗi thô) > arXiv (Không có)
```

---

## 11. Kiến trúc Medallion: Thô → Chuẩn hóa Quan sát → Chuẩn hóa Thực thể

Để đảm bảo khả năng kiểm toán, phục hồi và tốc độ phân tích, các pipeline dữ liệu tuân theo kiến trúc Medallion ba tầng:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            CÁC TẦNG MEDALLION                                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   BRONZE (Lưu trữ Thô)                                                       │
│   * Payload JSON / JSONL chỉ ghi thêm (append-only)                          │
│   * Phản hồi HTTP thô, thời điểm lấy dữ liệu, mã băm MD5/SHA256 payload      │
│   * Schema: Linh hoạt, không đánh chỉ mục, không biến đổi dữ liệu            │
│                                                                              │
│                                      ▼                                       │
│   SILVER (Quan sát Chuẩn hóa)                                                │
│   * Các bảng quan hệ định kiểu theo từng nguồn: `source_arxiv_works`, ...    │
│   * Chuẩn hóa định danh; tiêu chuẩn hóa cú pháp; xác thực ngày tháng         │
│   * Bảo toàn khẳng định chính xác từ nguồn; 1 hàng cho mỗi quan sát nguồn    │
│                                                                              │
│                                      ▼                                       │
│   GOLD (Mô hình Miền Chuẩn hóa)                                              │
│   * Thực thể hợp nhất: `canonical_works`, `canonical_authors`                │
│   * Phân giải thực thể đa bước; áp dụng chính sách xử lý xung đột thẩm quyền │
│   * Ràng buộc quan hệ nghiêm ngặt; đánh chỉ mục phân tích dưới một giây      │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 12. Thu thập Tăng dần & CDC (Incremental Ingestion & CDC)

### 12.1 Các Chiến lược Tăng dần
Các kho ngữ liệu khoa học tăng thêm hàng triệu bản ghi mỗi năm. Việc quét lại toàn bộ bảng là bất khả thi về mặt tính toán.
* **Theo dõi Watermark**: Duy trì bảng `ingestion_watermarks` ghi lại `(source_name, entity_type, last_cursor_or_timestamp)`.
* **Change Data Capture (CDC)**: Chỉ nạp các bản ghi có `updated_date >= last_watermark`.
* **Trích dẫn Đến sau (Late-Arriving Citations)**: Một cạnh trích dẫn được tạo ra vào năm 2024 có thể trỏ tới một bài báo viết từ năm 1980. Bộ máy nạp dữ liệu phải xử lý việc bổ sung cạnh mà không đòi hỏi phải lập chỉ mục lại toàn bộ siêu dữ liệu của bài báo năm 1980.

---

## 13. Tính Lũy đẳng (Idempotency)

### 13.1 Tính Lũy đẳng trong Toán học
Một thao tác nạp dữ liệu $f$ được gọi là lũy đẳng nếu áp dụng nó nhiều lần cho cùng một trạng thái đầu vào $x$ đều cho ra trạng thái đầu ra giống hệt nhau:
$$f(f(x)) = f(x)$$

### 13.2 Kịch bản Lỗi Điển hình trong Dữ liệu Học thuật
* Một worker thu thập dữ liệu bị crash giữa chừng khi đang phân tích tệp JSONL 50.000 dòng từ arXiv.
* Một pipeline ngây thơ không có tính lũy đẳng sẽ đơn giản chạy lại lô đó từ đầu.
* *Hậu quả*: Bộ đếm bị cộng dồn hai lần; các cạnh trích dẫn bị nhân đôi; các liên kết tác giả - bài báo bị lặp lại.
* **Yêu cầu Triển khai**:
  1. Mỗi lô dữ liệu thô được định danh bằng một `batch_id` xác định được tính toán từ mã băm nội dung tệp.
  2. Bảng trung gian (staging) sử dụng các giao dịch nguyên tử:
     `BEGIN TRANSACTION; DELETE FROM staging WHERE batch_id = ?; INSERT ...; COMMIT;`
  3. Quá trình hợp nhất chuẩn hóa sử dụng các khóa xác định: các đầu vào giống nhau sinh ra các khóa đại diện giống nhau và thực hiện upsert các bản ghi trùng khớp mà không nhân đôi số dòng.

---

## 14. Tiến hóa Schema (Schema Evolution)

* **SỰ THẬT**: Các API học thuật thường xuyên bổ sung các trường dữ liệu mới (ví dụ: OpenAlex bổ sung Mục tiêu Phát triển Bền vững `sdgs` và chủ đề chính).
* **Thiết kế Schema Phòng thủ**:
  - Tại **tầng Bronze**, lưu trữ payload dưới dạng cột `JSON` gốc của DuckDB. Điều này đảm bảo rằng các trường mới từ thượng nguồn không bao giờ làm gián đoạn việc thu thập.
  - Tại **tầng Silver**, trích xuất các thuộc tính mới cần thiết thông qua các kịch bản migration rõ ràng (`ALTER TABLE ADD COLUMN`).
  - Tại **tầng Gold**, cung cấp các view ổn định hoặc schema có phiên bản, bảo vệ các thuật toán khai phá xu hướng ở hạ nguồn khỏi những thay đổi đột ngột làm gãy hệ thống từ thượng nguồn.

---

## 15. Cổng Khẳng định & Chất lượng Dữ liệu (Data Quality & Assertion Gates)

Các pipeline dữ liệu phải thực thi các cổng xác thực nghiêm ngặt trước khi chuyển tiếp các bản ghi từ tầng Silver sang tầng Gold:
1. **Tính Hợp lý về Thời gian**: Năm xuất bản phải thỏa mãn:
   $$1665 \le \text{publication\_year} \le \text{CurrentYear} + 1$$
   (Năm 1665 đánh dấu sự ra đời của tập san học thuật *Philosophical Transactions of the Royal Society*).
2. **Độ Dài Văn bản Hợp lệ**: Tiêu đề phải chứa ít nhất 3 ký tự không phải khoảng trắng và không bao gồm toàn các chuỗi giữ chỗ (ví dụ: `"[Untitled]"`, `"None"`).
3. **Cú pháp Định danh Hợp lệ**: DOI phải khớp với biểu thức chính quy `^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$`.
4. **Toàn vẹn Tham chiếu**: Một mục thông tin tác giả không thể tham chiếu đến một tác giả hoặc bài báo không tồn tại.

---

## 16. DuckDB - Động cơ Phân tích cho Dữ liệu Học thuật

### 16.1 Các Khả năng Kiến trúc
* **SỰ THẬT**: DuckDB là hệ quản trị cơ sở dữ liệu quan hệ dạng cột (RDBMS) hoạt động in-process, được tối ưu hóa cho Xử lý Phân tích Trực tuyến (OLAP).
* **SỰ THẬT**: Các đặc tính cốt lõi của công cụ được kiểm chứng trên phiên bản DuckDB 1.5.5:
  - Vectorized Execution Engine (tính toán song song chia nhỏ morsel được tăng tốc bởi SIMD).
  - Hỗ trợ giao dịch ACID gốc bên trong các tệp cơ sở dữ liệu đơn lẻ.
  - Hỗ trợ kiểu dữ liệu gốc `JSON`, `STRUCT`, `LIST`, và `MAP` với khả năng cắt cột không cần sao chép (zero-copy).
  - Hỗ trợ đầy đủ cú pháp SQL `MERGE INTO`, `INSERT ... ON CONFLICT DO UPDATE`, và các hàm window.
  - Tương tác trực tiếp không qua trung gian (zero-copy interop) với Apache Arrow, Parquet và không gian bộ nhớ Python.

### 16.2 Hạn chế và Biện pháp Giảm thiểu
* **Xử lý Đồng thời Đơn-Writer**: DuckDB cho phép nhiều tiến trình đọc đồng thời, nhưng chỉ cho phép **duy nhất một giao dịch ghi đang hoạt động** trên mỗi tệp cơ sở dữ liệu.
  - *Biện pháp*: Các worker thu thập dữ liệu nên ghi các tệp Parquet được phân vùng hoặc các bảng staging độc lập, sau đó thực hiện hợp nhất theo lô vào tệp DuckDB chuẩn hóa thông qua một tiến trình ghi được tuần tự hóa.
* **Dung lượng Bộ nhớ**: Các phép join hàng triệu dòng quy mô lớn có thể kích hoạt cơ chế tràn đĩa (out-of-core spilling).
  - *Biện pháp*: Cấu hình giới hạn bộ nhớ rõ ràng (`SET max_memory = '8GB'`) và kích hoạt vùng lưu trữ đệm tạm thời trên đĩa.

---

## 17. Dữ liệu Lồng nhau trong DuckDB: JSON vs. STRUCT vs. LIST

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   CÁC KIỂU LỒNG NHAU CỦA DUCKDB CHO DỮ LIỆU HỌC THUẬT       │
├───────────────┬─────────────────────────────────────────────────────────────┤
│ Kiểu          │ Ứng dụng Phù hợp Nhất trong Dữ liệu Học thuật               │
├───────────────┼─────────────────────────────────────────────────────────────┤
│ `JSON`        │ Payload API thô tầng Bronze; siêu dữ liệu NXB phi cấu trúc  │
│ `VARCHAR[]`   │ Từ khóa, chủ đề nghiên cứu, thẻ khái niệm                   │
│ `STRUCT`      │ Ảnh chụp chỉ số tại một thời điểm (trích dẫn, tốc độ, hạng) │
│ `STRUCT[]`    │ Pipeline unnest trung gian trước khi nạp vào bảng 3NF       │
└───────────────┴─────────────────────────────────────────────────────────────┘
```

* **Thực hành Tốt nhất**: Sử dụng `read_json_auto()` để nạp các tệp JSONL không đồng nhất vào các bảng staging, nhưng sau đó chiếu các trường lồng nhau này vào các bảng quan hệ đã chuẩn hóa để phục vụ phân tích hạ nguồn nhằm tối đa hóa tốc độ quét cột được vector hóa.

---

## 18. Thiết kế Truy vấn Phân tích (Analytical Query Design)

Cơ sở dữ liệu học thuật chuẩn hóa được xây dựng để cung cấp năng lực cho các truy vấn phân tích phức tạp. Schema phải được tối ưu cho ba mô hình truy vấn chuẩn mực:
1. **Tốc độ & Gia tốc Trích dẫn (Citation Velocity & Acceleration)**:
   $$\text{Velocity}(W, t) = \frac{\Delta \text{Citations}(W)}{\Delta t}$$
   Đòi hỏi quét chỉ mục nhanh chóng trên `canonical_citations (cited_work_id, citing_year)`.
2. **Duyệt Mạng lưới Đồng Tác giả (Co-Authorship Network Traversal)**:
   Trích xuất đồ thị hợp tác đòi hỏi join bảng `canonical_work_authors` với chính nó:
   $$W \bowtie A_1 \bowtie A_2 \quad (A_1 \ne A_2)$$
3. **Theo dõi Tác động Nơi Xuất bản theo Thời gian (Temporal Venue Impact Tracking)**:
   Tính toán hệ số tác động (impact factor) trượt 2 năm của các hội thảo/tạp chí AI hàng đầu đòi hỏi gom nhóm hàng triệu cạnh trích dẫn được lọc theo năm xuất bản và phân hạng venue.

---

## 19. Các Kịch bản Thất bại trong Kỹ thuật Dữ liệu Học thuật (Failure Modes)

| Kịch bản Thất bại | Nguyên nhân Gốc rễ | Tác động | Biện pháp Kỹ thuật Phòng ngừa Chuẩn xác |
| :--- | :--- | :--- | :--- |
| **Trùng lặp do Chữ hoa/thường DOI** | So khớp chuỗi phân biệt hoa thường (`10.1145/...` vs `10.1145/...`) | Phân mảnh định danh, trùng lặp bản ghi | Chuẩn hóa chữ thường nghiêm ngặt ngay tại ngõ vào |
| **Trích dẫn Lơ lửng (Dangling Citations)** | Bài báo được trích dẫn chưa có trong chỉ mục | Vi phạm FK quan hệ làm dừng toàn bộ lô dữ liệu | Tự động tạo thực thể stub |
| **Ghi đè Mất Siêu dữ liệu** | Sử dụng `ON CONFLICT DO UPDATE` mù quáng từ nguồn cấp thấp | Siêu dữ liệu chất lượng cao bị thay bằng dữ liệu thưa thớt | Ma trận Ưu tiên Nguồn Thẩm quyền |
| **Cạn kiệt Bộ nhớ (OOM)** | Nạp trực tiếp 100GB JSON vào bộ nhớ qua `read_json` | Pipeline bị crash do tràn RAM (OOM) | Đọc phân đoạn JSONL dạng streaming qua DuckDB cursor |
| **Va chạm Trùng tên Tác giả** | Chỉ hợp nhất tác giả dựa vào `display_name` | "Wei Wang" bị hợp nhất thành một tác giả siêu nhân | Giới hạn tác giả theo viện nghiên cứu/ORCID hoặc không gộp |

---

## 20. Đánh đổi Kiến trúc (Architectural Trade-offs)

1. **Dung lượng Lưu trữ vs. Tốc độ Truy vấn**:
   - Việc hiện thực hóa các định danh bên ngoài ở cả `canonical_work_identifiers` và dưới dạng các cột tóm tắt trên `canonical_works` làm tăng dung lượng lưu trữ khoảng ~15%, nhưng giúp tăng tốc 95% các truy vấn tra cứu của người dùng nhờ tránh được phép join quan hệ tốn kém.
2. **Tính Nhất quán Tức thì vs. Thông lượng Nạp Dữ liệu**:
   - Việc chạy thuật toán phân giải thực thể đa bước đồng bộ trên từng dòng dữ liệu nạp vào sẽ làm suy giảm nghiêm trọng thông lượng.
   - *Giải pháp*: Thực hiện so khớp khóa đơn có tính xác định (DOI / arXiv) một cách đồng bộ trong quá trình nạp; hoãn việc gom cụm đồ thị mờ đa tín hiệu sang một tiến trình làm giàu theo lô không đồng bộ.

---

## 21. Bài học Thực tiễn từ các Cơ sở Dữ liệu Khoa học trong Môi trường Production

1. **Tuyệt đối không bao giờ tin tưởng mù quáng vào ngày xuất bản từ nguồn**: Ngày của arXiv phản ánh ngày nộp preprint; ngày của Crossref phản ánh ngày cấp giấy phép của nhà xuất bản; ngày của Semantic Scholar phản ánh thời điểm bot cào dữ liệu. Phải ghi nhận rõ ràng loại ngày (`preprint_date`, `published_date`).
2. **Phần tóm tắt đòi hỏi làm sạch phòng thủ**: Các nhà xuất bản thường chèn thông báo bản quyền (`"Copyright (c) 2023 IEEE..."`), arXiv chèn các mã điều khiển TeX, và OpenAlex đòi hỏi dựng lại chỉ mục đảo. Pipeline nạp dữ liệu bắt buộc phải có các bộ lọc làm sạch văn bản chuyên dụng.
3. **Các định danh có thể bị gán lại hoặc bị xóa**: DOI có thể bị nhà xuất bản rút lại hoặc tái chỉ định. Đừng bao giờ mặc định các khóa tự nhiên là bất biến 100%. Luôn duy trì các khóa đại diện nội bộ chuẩn hóa.

---

## 22. Các Nguyên lý Thiết kế Cốt lõi (Core Design Principles)

```
1. Nghiên cứu kỹ lưỡng trước khi dựng kiến trúc.
2. Thiết kế kiến trúc vững vàng trước khi triển khai code.
3. Dựa trên bằng chứng thực nghiệm trước khi đưa ra giả định.
4. Định danh chuẩn hóa (Canonical identity) ≠ Định danh nguồn (Source identity).
5. Trạng thái hiện tại (Current state) ≠ Quan sát nguồn (Source observation).
6. Khử trùng lặp (Deduplication) ≠ Phân giải thực thể (Entity resolution).
7. Nạp dữ liệu (Ingestion) ≠ Chuẩn hóa thực thể (Canonicalization).
8. Nguồn gốc dữ liệu (Provenance) là dữ liệu thực tế, không phải comment chú thích.
9. Tính lũy đẳng (Idempotency) là một yêu cầu bắt buộc, không phải một tối ưu hóa tùy chọn.
10. Kiểm thử là bằng chứng chứng minh, không phải đồ trang trí.
```
