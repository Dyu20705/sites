from decimal import Decimal, ROUND_HALF_EVEN
from html import escape
from pathlib import Path

from .contracts import canonical_json


STYLE = b"""body{font:16px/1.5 system-ui,sans-serif;max-width:76rem;margin:auto;padding:1rem;color:#202020}a{color:#0645ad}table{border-collapse:collapse;width:100%;margin:1rem 0}th,td{border:1px solid #bbb;padding:.45rem;text-align:left;vertical-align:top}th{background:#eee}.notice{border-left:.35rem solid #9a6700;padding:.7rem;background:#fff8c5}.limits{border:1px solid #cf222e;padding:.8rem}code{overflow-wrap:anywhere}.matrix{width:auto}.matrix td,.matrix th{text-align:center}.evidence-list{columns:3}.muted{color:#555}svg{max-width:100%;height:auto;border:1px solid #bbb}svg text{font:12px system-ui,sans-serif}"""
MONTHS = tuple(f"2019-{month:02d}" for month in range(1, 7))


def _page(title, body, prefix=""):
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>{escape(title)}</title><link rel=\"stylesheet\" href=\"{prefix}style.css\"></head>"
            f"<body><main>{body}</main></body></html>\n").encode("utf-8")


def _percent(rational):
    if rational is None:
        return "undefined"
    value = (Decimal(rational["numerator"]) * 100 / Decimal(rational["denominator"])).quantize(
        Decimal("0.0001"), rounding=ROUND_HALF_EVEN)
    return f"{value}%"


def _ratio(rational):
    return "undefined" if rational is None else f'{rational["numerator"]}/{rational["denominator"]} ({_percent(rational)})'


def _limitations():
    return ("<section class=\"limits\"><h2>Claim limits</h2><ul>"
            "<li>Observed October 2026 current-query population; event bins use January–June 2019 v1 submissions.</li>"
            "<li>Title-only lexical rule; semantic accuracy and historical completeness are not measured.</li>"
            "<li>Sparse support: 9 matches among 598 works. No directional, importance, causal, or forecasting label.</li>"
            "<li>Original historical E3 is not passed; public availability at the historical cutoff is unknown.</li>"
            "</ul></section>")


def _index(queries):
    lookup = {(row["start"], row["end"]): f'windows/{row["start"]}_{row["end"]}.html' for row in queries}
    months = sorted({row["start"] for row in queries} | {row["end"] for row in queries})
    head = "".join(f"<th scope=\"col\">{month}</th>" for month in months)
    rows = []
    for start in months:
        cells = []
        for end in months:
            href = lookup.get((start, end))
            cells.append(f'<td><a href="{href}">{start} → {end}</a></td>' if href else "<td>—</td>")
        rows.append(f'<tr><th scope="row">{start}</th>{"".join(cells)}</tr>')
    body = ("<h1>Observed v1-title lexical prevalence</h1>"
            "<p class=\"notice\"><strong>Fixed concept/rule:</strong> fuzzing — "
            "<code>RE-20260927-01-documented-word-boundary-v1</code>.</p>"
            "<p>Select one of the 21 contiguous month windows. Each result exposes n, N, the complete denominator, "
            "matches, source evidence and limitations.</p>"
            f'<table class="matrix"><thead><tr><th>Start / End</th>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'
            '<p><a href="sensitivities.html">Declared sensitivities and diagnostics</a></p>' + _limitations())
    return _page("SITES M1 offline evidence demo", body)


def _svg(monthly):
    points = []
    for index, row in enumerate(monthly):
        rational = row["share"]
        value = Decimal(0) if rational is None else Decimal(rational["numerator"]) / Decimal(rational["denominator"])
        x, y = 55 + index * 95, 170 - int(value * 3500)
        points.append((x, max(20, min(170, y)), row["months"][0], _ratio(rational)))
    circles = "".join(
        f'<a href="{month}_{month}.html#rule"><circle cx="{x}" cy="{y}" r="5">'
        f'<title>{escape(month)}: {escape(label)}</title></circle></a>'
        for x, y, month, label in points)
    line = " ".join(f"{x},{y}" for x,y,_,_ in points)
    labels = "".join(f'<text x="{x}" y="195" text-anchor="middle">{escape(month[5:])}</text>' for x,_,month,_ in points)
    return (f'<svg role="img" aria-labelledby="chart-title chart-desc" viewBox="0 0 600 215">'
            f'<title id="chart-title">Monthly lexical share</title><desc id="chart-desc">The adjacent table is the authoritative textual equivalent.</desc>'
            f'<line x1="55" y1="170" x2="530" y2="170" stroke="black"/><polyline points="{line}" fill="none" stroke="#0969da" stroke-width="3"/>{circles}{labels}</svg>')


def _work_link(work_id, prefix="../"):
    return f'<a href="{prefix}evidence/{escape(work_id)}v1.html"><code>{escape(work_id)}</code></a>'


def _window(row):
    monthly_rows = []
    for point in row["monthly"]:
        month = point["months"][0]
        target = f"{month}_{month}.html"
        n = point["n"] if point["n"] is not None else "null"
        denominator = point["N"] if point["N"] is not None else "null"
        monthly_rows.append(
            f'<tr><td>{month}</td><td><a href="{target}#numerator">{n}</a></td>'
            f'<td><a href="{target}#denominator">{denominator}</a></td>'
            f'<td>{_ratio(point["share"])}</td><td>{point["status"]}</td>'
            f'<td><a href="{target}#rule">fixed rule</a></td></tr>')
    numerator = " ".join(_work_link(work_id) for work_id in row["pooled"]["matched_ids"]) or "None"
    denominator = " ".join(_work_link(work_id) for work_id in row["pooled"]["denominator_ids"])
    body = (f'<p><a href="../index.html">← All windows</a></p><h1>fuzzing: {row["start"]} → {row["end"]}</h1>'
            f'<p class="notice" id="rule"><strong>Fixed rule:</strong> fuzzing / '
            f'<code>RE-20260927-01-documented-word-boundary-v1</code>. '
            f'<strong>Pooled n/N:</strong> {_ratio(row["pooled"]["share"])}. '
            'The pooled value is a ratio of summed counts, not an average of monthly shares.</p>'
            + _svg(row["monthly"]) +
            '<table><thead><tr><th>Month</th><th>n</th><th>N</th><th>n/N</th><th>Status</th><th>Rule</th></tr></thead>'
            f'<tbody>{"".join(monthly_rows)}</tbody></table><h2 id="numerator">Numerator evidence</h2><p>{numerator}</p>'
            f'<h2 id="denominator">Complete denominator ({len(row["pooled"]["denominator_ids"])})</h2><div class="evidence-list">{denominator}</div>'
            + _limitations())
    return _page(f'fuzzing {row["start"]} to {row["end"]}', body, "../")


def _evidence(bundle):
    work = bundle["work"]
    current, v1 = work["current_ref"], work["v1_ref"]
    raw_current = Path(current["artifact"]["path"]).name
    raw_v1 = Path(v1["artifact"]["path"]).name
    window_links = " ".join(
        f'<a href="../windows/{start}_{end}.html">{start}→{end}</a>'
        for index, start in enumerate(MONTHS) for end in MONTHS[index:])
    body = (f'<p><a href="../index.html">← Demo index</a></p>'
            f'<details><summary>Return to a selected window</summary><nav>{window_links}</nav></details>'
            f'<h1>Evidence: <code>{escape(work["version_id"])}</code></h1>'
            f'<p class="notice"><strong>Contribution:</strong> {escape(bundle["contribution"])}; '
            f'<strong>lexical match:</strong> {escape(str(bundle["matched"]))}.</p>'
            '<table><tbody>'
            f'<tr><th>v1 title</th><td>{escape(str(work["title_v1"]))}</td></tr>'
            f'<tr><th>current title</th><td>{escape(str(work["title_current"]))}</td></tr>'
            f'<tr><th>v1 submitted UTC</th><td>{escape(str(work["submitted_v1_at"]))}</td></tr>'
            f'<tr><th>current updated UTC</th><td>{escape(str(work["updated_current_at"]))}</td></tr>'
            f'<tr><th>v1 source</th><td><a href="../raw/{escape(raw_v1)}">raw Atom</a>; index {v1["entry_index"]}; '
            f'<code>{escape(v1["entry_id"])}</code>; SHA-256 <code>{v1["artifact"]["sha256"]}</code></td></tr>'
            f'<tr><th>current source</th><td><a href="../raw/{escape(raw_current)}">raw Atom</a>; index {current["entry_index"]}; '
            f'<code>{escape(current["entry_id"])}</code>; SHA-256 <code>{current["artifact"]["sha256"]}</code></td></tr>'
            '</tbody></table><details><summary>Escaped v1 entry excerpt</summary><pre>'
            f'{escape(bundle["v1_entry_text"])}</pre></details><details><summary>Escaped current entry excerpt</summary><pre>'
            f'{escape(bundle["current_entry_text"])}</pre></details>' + _limitations())
    return _page(f'Evidence {work["version_id"]}', body, "../")


def render(queries, bundles):
    artifacts = {"style.css": STYLE, "index.html": _index(queries),
                 "data/windows.json": canonical_json(queries),
                 "data/works.json": canonical_json([bundle["work"] for bundle in bundles])}
    for row in queries:
        artifacts[f'windows/{row["start"]}_{row["end"]}.html'] = _window(row)
    for bundle in bundles:
        artifacts[f'evidence/{bundle["work"]["version_id"]}.html'] = _evidence(bundle)
    return artifacts


def render_sensitivities(value):
    rows = []
    for name, result in sorted(value["variants"].items()):
        counts = ", ".join(f'{row["month"]}: {row["count"]}/{row["eligible_works"]}' for row in result["months"])
        rows.append(f'<tr><th>{escape(name)}</th><td>{escape(counts)}</td><td>{len(result["matched_ids"])}</td></tr>')
    adjacent = "".join(
        f'<tr><td>{escape(" → ".join(row["months"]))}</td>'
        f'<td>{row["count"]}/{row["eligible_works"]}</td><td>{escape(str(row["share"]))}</td></tr>'
        for row in value["adjacent_bimonth"])
    body = ('<p><a href="index.html">← Demo index</a></p><h1>Declared sensitivities and diagnostics</h1>'
            '<p>These checks expose rule and corpus sensitivity; they do not supply directional or scientific labels.</p>'
            '<table><thead><tr><th>Variant</th><th>Monthly n/N</th><th>Total matched IDs</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>'
            '<h2>Adjacent bimonth ratio of sums</h2>'
            '<table><thead><tr><th>Months</th><th>n/N</th><th>Frozen share</th></tr></thead>'
            f'<tbody>{adjacent}</tbody></table>' + _limitations())
    return _page("SITES sensitivities", body)
