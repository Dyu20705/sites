"""Deterministic static HTML/SVG; provider text never becomes markup or a URL."""
from html import escape
from pathlib import PurePosixPath

from .contracts import F1_SHA, MONTHS, RULE, canonical, percent, require

CSS = """*{box-sizing:border-box}body{margin:0;background:#f4f5f0;color:#1c302d;font:16px/1.6 system-ui,sans-serif}a{color:#075d64;text-underline-offset:3px}a:hover{color:#a44119}a:focus-visible,summary:focus-visible{outline:3px solid #b85120;outline-offset:3px}header,main,footer{max-width:1120px;margin:auto;padding:24px}header{border-bottom:1px solid #c3cec7}header .brand{font-weight:800;letter-spacing:.12em;font-size:14px}h1{font-size:clamp(28px,4vw,42px);line-height:1.2;margin:16px 0}h2{font-size:23px;margin-top:36px}h3{font-size:18px}.eyebrow,.muted{color:#52635e}.scope{border-left:4px solid #b85120;background:#fff8ee;padding:14px 18px;margin:24px 0}.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.stat{background:white;padding:22px;border:1px solid #d6dfd7;border-radius:8px}.stat strong{display:block;font-size:34px;line-height:1.3}.stat span{font-size:14px}.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;margin:12px 0 24px;background:white}caption{text-align:left;font-weight:600;padding:8px 0}th,td{border-bottom:1px solid #dce2dd;text-align:left;padding:10px 12px;vertical-align:top}th{background:#e4ece5;font-weight:650}td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}.matrix td,.matrix th{white-space:nowrap}.matrix a{display:block;padding:4px}.chosen{background:#d3e3d8;font-weight:700}code,pre{font-family:ui-monospace,monospace;font-size:13px}code{overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#e9eee8;padding:18px;border-radius:6px}details{border:1px solid #d1dcd2;padding:14px;margin:14px 0;background:white}summary{cursor:pointer;font-weight:600}.chart{width:100%;height:auto;background:white;border:1px solid #d6dfd7;border-radius:8px}.bar{fill:#167467}.axis{stroke:#b9c9c0;stroke-width:1}.chart text{fill:#213c35;font:14px system-ui,sans-serif}.chart .small{font-size:12px}.back{display:flex;gap:24px;flex-wrap:wrap}.badge{font-size:12px;font-weight:750;background:#dce9df;padding:3px 7px;border-radius:3px}footer{font-size:13px;border-top:1px solid #c3cec7;margin-top:40px}.title{max-width:670px}.limits{max-width:900px}dt{font-weight:650;margin-top:12px}dd{margin-left:0}nav{margin:16px 0}@media(max-width:650px){header,main,footer{padding:18px}.stats{grid-template-columns:1fr}.stat strong{font-size:28px}th,td{padding:8px}table{font-size:14px}}@media print{body{background:white}.matrix{display:none}details{break-inside:avoid}a{color:inherit}.scope{border:1px solid #777}}\n"""


def h(value):
    return escape(str(value), quote=True)


def shell(title, body, prefix=""):
    return ("<!doctype html><html lang=\"vi\"><head><meta charset=\"utf-8\">"
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'self\'; img-src \'self\'; base-uri \'none\'; form-action \'none\'">'
            f'<title>{h(title)} · SITES M1</title><link rel="stylesheet" href="{prefix}style.css"></head><body>'
            f'<header><a class="brand" href="{prefix}index.html">SITES / M1</a>'
            '<div class="eyebrow">Bằng chứng học thuật · bản xem offline</div></header><main>'
            f'<h1>{h(title)}</h1>' + body + '<aside class="scope limits"><strong>Phạm vi kết luận</strong>'
            '<br>Corpus current cs.SE được quan sát ngày 10/10/2026; các bin là ngày nộp v1 trong tháng 1–6/2019 (UTC). '
            'Đây là mức xuất hiện của từ trong title v1, không phải phép đo xu hướng khoa học đã được kiểm định. '
            'Chỉ 9 title khớp trong 598 công trình; hỗ trợ thưa. Public availability = UNKNOWN/null; '
            'không chứng minh corpus lịch sử đầy đủ hoặc tri thức đã có tại thời điểm 2019. '
            'Scientific quality: NOT MEASURED. E3 gốc: NOT PASSED.</aside></main>'
            f'<footer>F1 <code>{F1_SHA}</code><br>Rule <code>{RULE}</code>'
            '<br>Không cần API, máy chủ, JavaScript hoặc kết nối mạng. Tất cả số đếm là công trình riêng biệt.</footer></body></html>\n').encode("utf-8")


def window_name(start, end):
    require(start in MONTHS and end in MONTHS and start <= end, "INVALID_QUERY", "invalid page range")
    return f"windows/{start}_{end}.html"


def matrix(prefix="", selected=None):
    cells = ['<nav aria-label="Chọn khoảng thời gian"><div class="scroll"><table class="matrix">',
             '<caption>Chọn tháng bắt đầu (hàng) và tháng kết thúc (cột) · 21 khoảng hợp lệ</caption>',
             '<thead><tr><th scope="col">Bắt đầu ↓ / kết thúc →</th>']
    cells.extend(f'<th scope="col">{m}</th>' for m in MONTHS)
    cells.append('</tr></thead><tbody>')
    for start in MONTHS:
        cells.append(f'<tr><th scope="row">{start}</th>')
        for end in MONTHS:
            if start > end:
                cells.append('<td aria-label="Khoảng không hợp lệ">—</td>')
            else:
                chosen = ' class="chosen"' if selected == (start, end) else ''
                current = ' aria-current="page"' if chosen else ''
                cells.append(f'<td{chosen}><a{current} href="{prefix}{window_name(start, end)}" aria-label="{start} đến {end}">Mở →</a></td>')
        cells.append('</tr>')
    return ''.join(cells) + '</tbody></table></div></nav>'


def number(value):
    return "UNKNOWN" if value is None else str(value)


def table(points):
    result = ['<div class="scroll"><table><caption>Giá trị chính xác và hỗ trợ theo tháng</caption>'
              '<thead><tr><th>Tháng UTC</th><th class="num">n · khớp title</th><th class="num">N · corpus</th>'
              '<th class="num">n/N · tỷ lệ</th><th>Trạng thái</th></tr></thead><tbody>']
    for p in points:
        result.append(f'<tr><th scope="row">{h(" – ".join(p["months"]))}</th><td class="num">{number(p["n"])}</td>'
                      f'<td class="num">{number(p["N"])}</td><td class="num">{percent(p["share"])}</td><td>{h(p["status"])}</td></tr>')
    return ''.join(result) + '</tbody></table></div>'


def chart(points):
    # A fixed 0–5% axis across windows prevents the view from exaggerating a zoom.
    parts = ['<svg class="chart" viewBox="0 0 900 300" role="img" aria-labelledby="chart-title chart-desc" xmlns="http://www.w3.org/2000/svg">',
             '<title id="chart-title">Mức xuất hiện lexical theo tháng</title>',
             '<desc id="chart-desc">Trục cố định từ 0 đến 5 phần trăm. Bảng ngay bên dưới cung cấp cùng số liệu, gồm n và N.</desc>']
    for tick in range(6):
        y = 240 - tick * 40
        parts.append(f'<line class="axis" x1="60" y1="{y}" x2="870" y2="{y}"/><text x="10" y="{y + 5}">{tick}%</text>')
    for i, p in enumerate(points):
        x = 85 + i * 130
        value = p["share"]
        height = 0 if value is None else round(value["numerator"] * 4000 / value["denominator"], 6)
        parts.append(f'<rect class="bar" x="{x}" y="{240-height:g}" width="82" height="{height:g}"/>'
                     f'<text x="{x}" y="265">{p["months"][0]}</text><text class="small" x="{x}" y="286">{number(p["n"])}/{number(p["N"])}</text>'
                     f'<text class="small" x="{x}" y="{max(18, 229-height):g}">{h(percent(value))}</text>')
    return ''.join(parts) + '</svg>'


def stats(pooled):
    return (f'<div class="stats"><div class="stat"><span>n · title v1 khớp rule</span><strong>{number(pooled["n"])}</strong></div>'
            f'<div class="stat"><span>N · tất cả công trình đủ điều kiện</span><strong>{number(pooled["N"])}</strong></div>'
            f'<div class="stat"><span>Σn / ΣN · tỷ lệ gộp</span><strong>{percent(pooled["share"])}</strong></div></div>')


def evidence_list(ids, works, prefix, matched, caption):
    rows = [f'<div class="scroll"><table><caption>{h(caption)} · {len(ids)} công trình</caption>'
            '<thead><tr><th>Công trình / v1</th><th>Title v1</th><th>Đóng góp</th></tr></thead><tbody>']
    for work in ids:
        row = works[work]
        rows.append(f'<tr><td><a href="{prefix}evidence/{work}v1.html">{work}v1</a></td>'
                    f'<td class="title">{h(row["title_v1"])}</td><td>{"MATCH" if work in matched else "NONMATCH"}</td></tr>')
    return ''.join(rows) + '</tbody></table></div>'


def evidence(bundle):
    w = bundle["work"]
    body = (f'<nav class="back"><a href="../index.html">← Chọn khoảng thời gian</a>'
            f'<a href="../{window_name(w["event_month"],w["event_month"])}">Mở tháng {w["event_month"]}</a></nav>'
            '<p>Dùng nút Back của trình duyệt để trở lại đúng khoảng vừa chọn.</p>'
            f'<p><span class="badge">{bundle["contribution"]}</span> · Đóng góp N = 1; '
            f'đóng góp n = {1 if bundle["matched"] else 0}. NONMATCH không có nghĩa là bài không liên quan về mặt ngữ nghĩa.</p>'
            f'<h2>Title v1 được dùng để tính</h2><p class="title">{h(w["title_v1"])}</p>'
            f'<h2>Title current · v{w["current_version"]}</h2><p class="title">{h(w["title_current"])}</p>'
            '<dl>'
            f'<dt>Nộp v1 / bin UTC</dt><dd>{h(w["submitted_v1_at"])} / {w["event_month"]}</dd>'
            f'<dt>Cập nhật current</dt><dd>{h(w["updated_current_at"])}</dd>'
            f'<dt>Category v1 / current</dt><dd>{h(", ".join(w["categories_v1"]))} / {h(", ".join(w["categories_current"]))}</dd>'
            '<dt>Public availability</dt><dd>UNKNOWN / null</dd></dl>')
    for role in ("v1", "current"):
        ref = w[role + "_ref"]
        name = PurePosixPath(ref["artifact"]["path"]).name
        body += (f'<h2>Raw Atom · {role}</h2><dl><dt>Entry ID</dt><dd><code>{h(ref["entry_id"])}</code></dd>'
                 f'<dt>Vị trí trong feed (zero-based)</dt><dd>{ref["entry_index"]}</dd>'
                 f'<dt>Thu nhận UTC</dt><dd>{h(ref["acquired_at"])}</dd>'
                 f'<dt>Artifact</dt><dd><code>{h(ref["artifact"]["path"])}</code></dd>'
                 f'<dt>SHA-256 toàn bộ file</dt><dd><code>{ref["artifact"]["sha256"]}</code></dd></dl>'
                 f'<p><a download href="../raw/{name}">Mở/tải raw Atom đã frozen: {name}</a></p>'
                 '<details><summary>Xem entry đã escape an toàn</summary>'
                 '<p>Đây là subtree được serialize lại để hiển thị. Hash định danh toàn bộ raw file gốc phía trên.</p>'
                 f'<pre>{h(bundle[role + "_entry_text"])}</pre></details>')
    return shell(w["version_id"], body, "../")


def artifacts(snapshot):
    works = {w["work_id"]: w for w in snapshot["works"]}
    full = next(w for w in snapshot["windows"] if w["start"] == MONTHS[0] and w["end"] == MONTHS[-1])
    matched = set(full["pooled"]["matched_ids"])
    intro = ('<p class="eyebrow">Khái niệm cố định: fuzzing · title v1 · 2019-01 → 2019-06 UTC</p>'
             '<p class="limits">Đếm công trình có từ <code>fuzz / fuzzing / fuzzer / fuzzers</code> '
             'ở ranh giới từ (không phân biệt hoa thường). Mẫu số gồm cả công trình không khớp. '
             'Chọn một khoảng bên dưới, xem n/N, rồi mở từng bản ghi để kiểm tra nguồn.</p>')
    body = intro + stats(full["pooled"]) + matrix() + '<h2>Sáu tháng trong corpus frozen</h2>'
    body += chart(snapshot["points"]) + table(snapshot["points"])
    body += '<p>Tỷ lệ gộp là tổng n chia tổng N, không phải trung bình các tỷ lệ tháng. Không áp dụng nhãn tăng/giảm.</p>'
    body += '<p><a href="sensitivities.html">Xem toàn bộ sensitivity đã khai báo →</a> · <a href="data/windows.json">Query JSON</a></p>'
    yield "index.html", shell("Title fuzzing trong corpus đã quan sát", body)
    yield "style.css", CSS.encode("utf-8")
    for window in snapshot["windows"]:
        start, end = window["start"], window["end"]
        body = intro + stats(window["pooled"]) + matrix("../", (start, end))
        body += chart(window["monthly"]) + table(window["monthly"])
        body += '<p>Tỷ lệ khoảng = Σn / ΣN; phần trăm làm tròn half-even 4 chữ số. JSON giữ cặp số nguyên chính xác.</p>'
        body += evidence_list(window["pooled"]["matched_ids"], works, "../", matched, "Tử số n: các title khớp")
        body += evidence_list(window["evidence_ids"], works, "../", matched, "Mẫu số N đầy đủ: khớp và không khớp")
        yield window_name(start, end), shell(f"Fuzzing · {start} → {end}", body, "../")
    for work in sorted(snapshot["bundles"]):
        yield f"evidence/{work}v1.html", evidence(snapshot["bundles"][work])
    labels = {
        "archived_literal_transport_diagnostic": "Literal transport / decoded-pattern equality",
        "exact_fuzzing": "Chỉ từ fuzzing chính xác: 5 công trình khớp",
        "current_title_diagnostic": "Title current thay title v1 · diagnostic",
        "v1_category_subset": "Chỉ category cs.SE tại v1 · subset",
        "exclude_nine_late_ids_diagnostic_not_as_of": "Bỏ 9 ID muộn · perturbation, không sửa historical as-of",
    }
    body = '<p>Giữ nguyên mọi sensitivity từ research. Không chọn biến thể theo kết quả. Các bảng cung cấp n/N; JSON lưu toàn bộ ID và lý do loại.</p>'
    for name, label in labels.items():
        value = snapshot["sensitivities"][name]
        body += f'<h2>{h(label)}</h2>' + table(value["points"])
        body += evidence_list(value["matched_ids"], works, "", set(value["matched_ids"]), "Bằng chứng khớp trong biến thể")
    body += '<h2>Gộp tháng liền kề · ratio of sums</h2>' + table(snapshot["sensitivities"]["adjacent_bimonth"])
    body += '<p><a href="data/sensitivities.json">Đầy đủ denominator IDs, matches và exclusions (JSON)</a></p>'
    yield "sensitivities.html", shell("Sensitivity và giới hạn của rule", body)
    for key in ("works", "windows", "sensitivities", "bundles"):
        yield f"data/{key}.json", canonical(snapshot[key])
    raw_names = sorted({w[role + "_ref"]["artifact"]["path"] for w in snapshot["works"] for role in ("v1", "current")})
    for name in raw_names:
        yield "raw/" + PurePosixPath(name).name, snapshot["files"][name]
