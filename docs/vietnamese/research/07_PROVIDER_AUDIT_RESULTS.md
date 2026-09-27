# 07 — Kết quả sàng lọc provider và truy cập

**27/09/2026 — #65, đã screen tài liệu; audit corpus thực đo bị chặn.** Chưa accept provider. Bảng dưới không phải phép đo coverage. Chi phí chỉ phản ánh điều kiện truy cập trong tài liệu; chưa đo runtime/transfer.

## Sàng lọc năm ứng viên

| Ứng viên / evidence ID | VERIFIED từ tài liệu chính thức đã đọc | Suy luận, unknown và kết quả screen |
| --- | --- | --- |
| arXiv / EL-101 | [API manual](https://info.arxiv.org/help/api/user-manual.html), QuickStart/§3.1/§3.3/§5.1.1: endpoint query được tài liệu ghi là `http://export.arxiv.org/api/query`; có Atom IDs/titles, versioned retrieval, submission dates, paging/totals. [Terms](https://info.arxiv.org/help/api/tou.html): descriptive metadata CC0; một connection, cách request ≥3 giây. | **Probe giới hạn đầu tiên** vẫn hợp lý, nhưng hai probe đã chạy dùng HTTPS thay vì endpoint HTTP trong manual đã đọc. Hai 406 vì vậy bị confound bởi endpoint và chưa chứng minh đường truy cập được tài liệu mô tả đã fail. Còn phải xác minh public availability và category membership lịch sử; chưa loại provider. |
| OpenAlex / EL-102 | [Attributes](https://help.openalex.org/data/works/attributes/): `id`, `title`, `publication_date`, `created_date`, `updated_date`; update time của object hiện tại. [Authentication](https://help.openalex.org/api/authentication/): basic query không key, cursor sau basic paging limit. [Snapshot](https://help.openalex.org/access/snapshot/): public dump miễn phí, daily snapshot trả phí riêng. | Metadata hiện tại không tự tái tạo field lịch sử. Chưa chứng minh bounded historical extract. **Dự phòng**, chưa sample. Data CC0 theo [API reference](https://help.openalex.org/api/); đọc docs không phải đo coverage. |
| Crossref / EL-103 | [REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) và [schema](https://github.com/CrossRef/rest-api-doc/blob/master/api_format.md): DOI, title, publication/deposit/index dates, cursor. [Licensing](https://www.crossref.org/documentation/retrieve-metadata/): metadata thư mục nhìn chung tái sử dụng được; abstract có thể còn bản quyền. [Snapshots](https://www.crossref.org/documentation/retrieve-metadata/bulk-downloads): public data file; monthly snapshot cần Metadata Plus. | Deposit/index time hiện tại không cung cấp field quá khứ. Chưa đo khả thi annual dump miễn phí; monthly trả phí trái ranh giới sprint. **Dự phòng**, chưa sample. Đọc quota headers trước acquisition, không giả định rate cụ thể. |
| Semantic Scholar / EL-104 | [Graph docs](https://api.semanticscholar.org/api-docs/snippets): `paperId`, `externalIds`, `title`, `publicationDate` nullable, `year`. [Tutorial chính thức](https://webflow.semanticscholar.org/product/api/tutorial): có dataset theo release, download links cần API key. | **Historical download bị chặn theo giả định không credentials**, không phải không có lịch sử. Terms và quyền phân phối dataset cụ thể còn unresolved; chưa tải records. Ngày thiếu có thể cản bin tháng; chưa đo missingness. |
| DBLP / EL-105 | [Snapshot guidance](https://dblp.org/faq/4621382.html): monthly release cố định khác daily dump thay đổi. [DROPS artifact tháng 04/2019](https://drops.dagstuhl.de/entities/artifact/10.4230/dblp.xml.2019-04-01) xác minh DOI/version `2019-04-01`, CC0, file `dblp-2019-04-01.xml.gz` (468,04 MB), MD5 `cdf6416c27ab24eaef5aa4560e38aa3c` và schema DOI. [XML guidance](https://dblp.org/faq/1474681.html) mô tả streaming parse/local DTD. | **Đã xác minh danh tính snapshot**, nhưng chưa có bounded venue/domain extract hoặc field fitness thực đo. XML work key/title/year có thể hỗ trợ title-level annual analysis; không bịa độ chính xác theo tháng. HEAD reset trên đường legacy vẫn được giữ như access observation, không phải bằng chứng snapshot không tồn tại. |

Mô tả key/title/year của DBLP có cơ sở từ [Ley (2009), §2, tr.1–2](https://www.vldb.org/pvldb/vol2/vldb09-98.pdf), được XML guide liên kết. Đây là mô tả schema lịch sử, không phải fitness thực đo của extract hiện tại hay quá khứ. Phần historical log trong paper không chứng minh log đó còn truy cập được hôm nay.

## Mapping field cho audit arXiv đã thử

| Field logic | Path được mô tả | Fitness thực đo |
| --- | --- | --- |
| Identity/version | Atom `entry/id`, `id_list=<id>v1` cụ thể | NOT MEASURED |
| Text cho concept | `entry/title` dạng string; không dùng abstract cho signal | NOT MEASURED; chưa đo missingness |
| Event time | `entry/published`; `entry/updated` liên quan version trả về | NOT MEASURED |
| Scope | `entry/category/@term`, query `cat:cs.SE` | Historical membership UNKNOWN |
| Denominator/completeness | `opensearch:totalResults`, `start`, `max_results` | Total UNKNOWN; chưa có page thành công |
| Availability | Bằng chứng version/announcement, không phải retrieval timestamp | NOT VERIFIED |

[Version policy](https://info.arxiv.org/help/versions.html) mô tả giữ các version public; [availability policy](https://info.arxiv.org/help/availability.html) phân biệt submission và announcement, có moderation delay. Vì vậy phải audit field cụ thể; không suy availability từ `published`. Docs hiện tại không chứng minh trạng thái năm 2019 của từng record.

## Mẫu khai báo trước và lỗi truy cập quan sát được

[Preregistration](../../../experiments/research_exit_20260927/preregistration.json) giữ query cs.SE sáu tháng, sort submission tăng dần, page ≤500, yêu cầu các ID `v1`, bound 2.000 works. Không thay bằng first-N hay chọn mẫu theo signal.

| Quan sát | Kết quả / artifact |
| --- | --- |
| Request HTTPS đầu, 12:46:11–12:46:12 UTC | HTTP 406; [manifest](../../../experiments/research_exit_20260927/acquisition.json). Endpoint khác base HTTP trong manual đã đọc. |
| AM-01 HTTPS, 12:47:33–12:47:34 UTC | Cùng query, thêm Atom Accept; HTTP 406, diagnostic response excerpt rỗng; [manifest](../../../experiments/research_exit_20260927/accept-atom-diagnostic/acquisition.json). Vẫn có cùng confound về scheme. |
| AM-02 diagnostic theo HTTP trong manual | **CHƯA CHẠY trong changeset này.** `acquire.py --http-endpoint-diagnostic` ghi manifest riêng, lưu redirect/final URL rồi dừng sau một request. |
| DBLP HEAD đường legacy, 12:51:08 UTC | Connection reset, chưa có HTTP status/size; [probe](../../../experiments/research_exit_20260927/dblp-access.json). Sau đó đã xác minh metadata snapshot chính xác qua DROPS artifact có DOI. |
| Corpus records dùng được trả về | **0**; không có nghĩa query không có matches |
| Total, missingness, duplicates, revisions, invalid values, coverage, truncation | **NOT MEASURED**, không phải 0% |
| Snapshot thật, replay dữ liệu thật, so sánh signal thật | **NOT AVAILABLE / NOT RUN** |

Đã giữ stop rule; không dùng identity khác, proxy, credentials hay bulk download. Manifest là bằng chứng truy cập, không phải sample dataset. Hai 406 arXiv còn bị confound bởi việc dùng HTTPS thay cho base HTTP trong manual đã đọc, nên chưa tách được lỗi provider/network/client construction. DBLP reset chỉ thuộc đường direct legacy; artifact snapshot có DOI đã được xác minh độc lập.

## B → A và phép kiểm tra tiếp theo

Bàn giao **INSUFFICIENT EVIDENCE**: chưa có field fitness, denominator hay corpus hợp lệ temporal được đo để hỗ trợ D08. Giữ real-signal/support/quality claims unresolved.

Chạy phép kiểm tra sạch nhỏ nhất trước: đúng một request AM-02 tới endpoint HTTP trong arXiv manual đã đọc, ghi redirect/final URL/status và không lấy holdout. Response thành công vẫn chưa đủ D07; còn phải kiểm tra version-specific text, membership lịch sử và announcement evidence. Nếu đường này tiếp tục fail hoặc temporal semantics không đủ, preregister bounded streaming extract từ snapshot DBLP đã xác minh `10.4230/dblp.xml.2019-04-01`. Trước khi tải/scan artifact upstream 468,04 MB, khai báo transfer/storage/scan budget và rule lấy ≤5.000 works theo venue/domain/period; toàn archive rộng hơn corpus M1 nhiều. Dùng bin năm nếu chỉ có publication year. Không ghi đè preregistration ban đầu hoặc coi live API DBLP tái tạo archive.

Chưa có bằng chứng rằng cả năm provider đều fail E3. Hiện chưa có **mẫu giới hạn truy cập được và đã xác minh** đáp ứng E3. Không tích hợp nguồn thứ hai.
