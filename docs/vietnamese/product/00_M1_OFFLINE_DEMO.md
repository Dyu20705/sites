# Demo bằng chứng offline M1

English: [English version](../../english/product/00_M1_OFFLINE_DEMO.md)

**Trạng thái triển khai — 16/10/2026:** implementation candidate cho
[#72](https://github.com/Dyu20705/sites/issues/72). Phần này triển khai đúng
[đề xuất D09-M1-20261012-v1](https://github.com/Dyu20705/sites/issues/71#issuecomment-6123770080)
đã được owner chấp thuận với SHA-256
`a6c84f4b54523acd7f6121408c4889978003b9afc6c94dd4069fbd71b572cfbc`.
Tài liệu này không tự đánh dấu FEATURE-READY, E7, E8 hoặc PRODUCT-READY là đạt.

## Ranh giới as-built

Demo chỉ dùng thư viện chuẩn CPython, file frozen, hàm in-process và HTML/SVG
local được sinh sẵn. Không cài package, không database/listener/JavaScript,
remote asset, live provider call, model hoặc đường deploy.

| Module | Trách nhiệm public |
| --- | --- |
| `sites_demo/contracts.py` | Contract JSON/path nghiêm ngặt và record immutable |
| `sites_demo/pipeline.py` | `verify_inputs`, `project`, `measure`, `query`, `evidence`, `build`, `compare` |
| `sites_demo/render.py` | HTML/SVG static đã escape, 21 trang window và 598 trang evidence |
| `sites_demo/__main__.py` | CLI `runtime`, `verify`, `build`, `compare` |

Input cố định là F1-M1-R-20261012-v1, SHA-256
`bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`.
Verification fail-closed khi sai identity của manifest/artifact/runtime, có field
JSON ngoài schema, duplicate key, raw Atom index/ID/hash không khớp, current
category không hợp lệ, query sai hoặc path không an toàn. Oracle chính được
chấp thuận giữ monthly n=`0/1/2/1/4/1`, N=`91/79/97/103/122/106`, pooled
9/598 công trình.

`build` từ chối destination đã tồn tại. Một run hoàn chỉnh gồm:

- `index.html`, `style.css` local và `sensitivities.html`;
- 21 file `windows/*.html` và 598 file `evidence/*.html`;
- `data/works.json`, `data/windows.json`, `data/sensitivities.json` canonical;
- raw Atom đã admit, giữ nguyên byte trong `raw/`;
- `semantic-index.json`, `execution.json` tách riêng và marker `COMPLETE` ghi cuối.

Semantic replay không đưa clock/resource observation vào digest. `compare` từ
chối run chưa hoàn chỉnh và so sánh identity product/F1, toàn bộ path, bytes
từng file và semantic root digest.

## Bootstrap và replay

Không commit evaluation file để thay cho approval. Trước evaluation thật, cần
chuẩn bị và anchor bên ngoài một record `D09-EVAL-v1` immutable, chứa exact
product commit/code digest, identity F1 và D09, reviewer/exposure, runtime
inventory, toàn bộ tám logical schema identity đã chấp thuận, exact control
artifact và sáu sensitivity name, năm interpretation task có tên,
navigation match/nonmatch, semantic replay hai build và limits. Strict reader
từ chối identity thiếu, thừa, placeholder hoặc bị thay thế.

Từ source root đã bàn giao, dùng record đó:

~~~text
python -m sites_demo runtime --browser "RECORDED BROWSER VERSION" --out evaluation/runtime-candidate.json
python -m sites_demo verify --f1 experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-f1-sha bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --evaluation evaluation/demo-v1.json --expected-evaluation-sha EVALUATION_SHA256
python -m unittest discover -s tests -p "test_*.py" -v
python -m sites_demo build --f1 experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-f1-sha bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --evaluation evaluation/demo-v1.json --expected-evaluation-sha EVALUATION_SHA256 --out output/replay-1
python -m sites_demo build --f1 experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-f1-sha bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --evaluation evaluation/demo-v1.json --expected-evaluation-sha EVALUATION_SHA256 --out output/replay-2
python -m sites_demo compare output/replay-1/semantic-index.json output/replay-2/semantic-index.json
~~~

`runtime` chỉ ghi candidate, không tự phê duyệt environment. Record độc lập
phải xác định target Windows x64 / CPython 3.14.7 đã chấp thuận, CPU/RAM
inventory được phát hiện và browser version không phải placeholder. Phải kiểm
tra exit của từng lệnh trước khi đi tiếp. Mỗi CLI `build` khởi động một worker
process mới. Outer monotonic timer bao gồm worker interpreter startup; trên
Windows, execution record ghi peak của worker và launcher, enforce maximum với
256 MiB và ghi tổng của hai peak làm context. Launcher sync mọi output file,
stage exact completion marker, ghi và sync outer execution record, rồi kiểm tra
lại budget trước khi publish `COMPLETE` bằng atomic rename; run vượt budget giữ
trạng thái incomplete. Elapsed time được ghi sau khi exact marker bytes và
execution metadata đã sync. Monotonic guard muộn hơn chỉ có thể làm run fail;
atomic rename cuối chỉ publish các bytes đã sync nên không tính là replay work.

## Evidence development và các gate còn lại

Trên Linux x86_64 với Python 3.12.14, product suite 14 test đã pass ngày 16/10/2026.
Các test chạy freeze thật 598 công trình, hai semantic build giống nhau từng
byte, toàn bộ local link, HTML escaping, failure JSON/path nghiêm ngặt, fixture
null/event, ratio-of-sums, output refusal, CLI và build khi mọi socket connection
bị chặn. Đây là evidence development, không phải review Windows/browser độc lập.

Run Linux cố ý ghi peak process memory là
`NOT_MEASURED_NON_WINDOWS_D09_BOUNDARY`; không thể làm E8 đạt. #73 vẫn cần
evaluation record product/runtime đã anchor bên ngoài, một human độc lập có
identity hoàn thành năm task interpretation/navigation trên target
Windows/browser đã chấp thuận, cùng số đo thời gian full replay và peak process
memory. E3 lịch sử gốc giữ NOT PASSED; scientific quality giữ NOT MEASURED.
