# 16 — Kiểm tra critical path và bàn giao demo có điều kiện

**12/10/2026; CP-20261012-v1.** Đây là bản tóm tắt tiếng Việt của [báo cáo và thiết kế chi tiết bằng tiếng Anh](../../english/research/16_CRITICAL_PATH_HANDOFF_20261012.md), **không phải bản dịch đầy đủ**. Hai bản giữ cùng số liệu, trạng thái và ranh giới quyết định. Packet M1-R-20261010-v1 cũ không bị sửa.

## Checkpoint và kết quả kiểm tra

Đã xác minh worktree research sạch tại `7ef28119b125c6bcb9f0372516cc0ebe3200326d`, khớp origin sau fetch; base master `0a853636ef6d1be9d3bb85058f34faf368fcb6ce`. PR #75 OPEN/Draft, không có review/thread/comment PR hoặc check rollup được trả về. Không có CI không có nghĩa PASS. Main checkout vẫn ở dev và không bị đổi.

#65 CLOSED/completed; #64 OPEN, READY FOR OWNER REVIEW. #66/#67/#69/#70/#71/#72/#73 còn OPEN. D05/D06 ACCEPTED; exact amendment, D07/D08/D09 và freeze PROPOSED; E3 gốc/#70 NOT PASSED. [Owner direction](https://github.com/Dyu20705/sites/issues/70#issuecomment-6097713689) chỉ chấp thuận hướng retrospective và chuẩn bị proposal. [Audit #64](https://github.com/Dyu20705/sites/issues/64#issuecomment-6104422817) không thay acceptance.

| Mức / phạm vi | Kết quả và xử lý |
| --- | --- |
| **BLOCKER — #70/#71** | Chưa có acceptance từng quyết định và immutable freeze. Owner cần quyết định bảng dưới; không suy ra quyền build từ checkbox. |
| **MAJOR — bảo toàn output legacy; đã sửa entry point hiện tại** | `checks.py:154` ghi đè output có sẵn. Đã tái hiện trên sentinel tạm, không phải evidence lịch sử. `checks_cli_v2.py` chạy checker cũ trong thư mục riêng, chỉ xuất khi thành công bằng exclusive creation; README trỏ sang v2. Ba regression tests kiểm tra bảo toàn, output giống frozen và không publish khi thất bại. Checker frozen giữ nguyên; gọi trực tiếp v1 lên file có sẵn vẫn không an toàn. |
| **MAJOR trước reuse rộng; corpus này không bị ảnh hưởng** | `signal_evaluator.py:53` coi missing current-category là exclusion/empty bin. Raw recount xác nhận cả 598 records có membership hợp lệ. Giữ bytes evaluator; strict projection có version mới và tests chỉ là đề xuất cho #72 sau #71. |
| **MAJOR — tracker chưa nhất quán** | #66 đánh dấu đủ bảy ô demo nhưng prose ghi 0/7 independently verified; không có view/reviewer replay/#73 pass. #64/#69 cũng có checkbox rộng hơn evidence về các nghĩa vụ còn partial/search metadata. Giữ snapshot/hash để review; không sửa các chỉnh sửa owner gần đây hoặc xem checkbox là acceptance. |
| **INFORMATIONAL** | Arithmetic/lineage tái lập được; chưa có real independent annotations. Không phát hiện lỗi mới làm sai chín matches frozen. |

Không có MINOR riêng được xác nhận. WIP giữ audit/correction #64 cùng handoff hỗ trợ, không mở lane implementation.

## Validation đã chạy

Evidence nằm ở [run mới 20261012-critical-path-01](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01).

- Python 3.14.7, Windows 11, standard library, TEMP/TMP trong workspace.
- Suite ban đầu **37/37 PASS**; sau correction **40/40 PASS**, 0 failures/errors, unittest báo **1,367 giây**. Không dùng thời gian test để claim E8.
- Runner cũ: 13 commands, 12 exit 0 và một exit 2 dự kiến khi yêu cầu ghi đè validator output; 15 legacy checks ở mỗi process; 10 controls mỗi signal replay; **13/13 byte comparisons** khớp artifacts lịch sử.
- Recount Atom/token độc lập với parser/evaluator dự án: 14 input hashes/Git bytes, 598 current/v1 lineages, chín numerator refs, 18 lexical boundary cases, năm sensitivity variants và selection pilot 27 works đều xác minh. Vẫn cùng host/agent, không independent human evaluation.
- Python có warning tìm đường dẫn executable nhưng expected outcomes đều đạt. Lần gọi gh trong sandbox không kết nối được; connector, fetch và gh read có quyền đã xác minh GitHub. Chưa có independent clean-host replay.
- Report chi tiết có commands chạy lại, inventory đầy đủ 143 files của PR, giới hạn review, preservation và validation cuối. Các search cũ không được chạy lại; không claim full security audit hoặc independent translation review.

N **91/79/97/103/122/106**, n **0/1/2/1/4/1**, tổng **9/598**. Measurement SHA-256 `214c103f82784665907f76925ea56763fd2e46644ce52ccf6950b08e807cc818`. Historical availability vẫn null 598/598, chín late IDs, 161 revisions, 55 title changes và bốn category-set changes. Exact-fuzzing chỉ năm matches. SYN có 27 fictional records/54 judgments; real annotations = 0.

Tách rõ: **(1)** arithmetic/workflow verified trong các cases đã chạy; **(2)** descriptive corpus replay verified; **(3)** independent semantic quality NOT MEASURED; **(4)** validated scientific trend detection NOT ESTABLISHED; **(5)** product/demo NOT PASSED. Không suy ra emergence, adoption, impact, causality hoặc as-of completeness.

## Quyết định owner — packet cũ giữ nguyên

Từng dòng trỏ tới [M1-R-20261010-v1](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) tại commit `7ef28119b125c6bcb9f0372516cc0ebe3200326d`. Hash Git-blob: VI `164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0`; EN `da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122`. Ghi acceptance ngoài packet, kèm owner/UTC/row/hash; revision dùng addendum version mới. Báo cáo EN §2 ghi evidence, uncertainty, alternative và hệ quả ACCEPT/REJECT/REVISE riêng cho từng dòng.

| ID | Trạng thái / quyết định |
| --- | --- |
| A1 | **PROPOSED** — estimand lexical trên observed corpus 2026, bins v1 2019 và clause M1/D05 chính xác (§§1–2) |
| A2 | **PROPOSED** — E2-R/E3-R, giữ E3 gốc NOT PASSED (§2) |
| A3 | **PROPOSED** — chọn descriptive acceptance với quality NOT MEASURED, hoặc giữ independent reference và chờ evidence thật (§§5–6) |
| D07 | **PROPOSED** — đúng 598 observed works/query/identity/time/denominator/sharing (§3) |
| D08 | **PROPOSED** — rule cố định, n/N/share, null/support, sensitivities và không directional labels (§§4–6) |
| F1 | **PROPOSED** — prospective freeze, exposure, reviewer/replay/budget (§7); không holdout access |
| G70 | **BLOCKED / NOT PASSED** — chỉ quyết định PASS sau acceptance và đủ evidence cho mọi research criterion được giữ (§9) |

Khuyến nghị route descriptive hẹp nếu phù hợp giá trị owner cần; alternative là giữ chuẩn independent reference hoặc defer M1. Chấp thuận một dòng không chấp thuận dòng khác, không tự cho phép D09/build.

## D09 và kế hoạch sau approval — PROPOSED ONLY

**CP-D09-R-20261012-v1**, chi tiết ở EN §4–5. Flow: frozen input thật → strict projection → deterministic count/share → evidence bundle → local read-only view → offline replay. Đề xuất files/JSON(L), Python standard library, in-process query và HTML/SVG tĩnh; so sánh SQLite/dependency/API/framework chỉ chọn nếu requirement đo được cần chúng. Không có product code được viết.

Contracts gồm accepted manifest, projection có current/v1 provenance, result n/N/share/null với toàn bộ IDs, evidence navigation và replay record. Missing/invalid category phải unresolved/fail closed, không exclusion ngầm; title unknown vẫn ở N; event unknown không âm thầm thu nhỏ denominator. Không dùng fallback current-title/event, không thêm contribution từ revision. Canonical bytes tách khỏi timing/path. Input không đúng frozen hashes phải dừng trước success output. Guard mới và tests không sửa evaluator lịch sử.

CLI build/compare và test commands trong EN là **đề xuất chưa tồn tại**. View hoạt động từ local file, chọn concept/range và mở match/nonmatch/raw provenance, không network/assets bên ngoài. Escape metadata; kiểm soát paths/hashes/size và exclusive output. Chỉ metadata/Atom được phép, không mặc định redistribute PDF/full text.

Budget **PROPOSED**: ≤598 works, replay ≤60 giây, peak batch-process memory ≤256 MiB. Chưa đo product E8; thiếu measurement thì NOT MEASURED. Clean reviewer run phải pin input/config/code/runtime, chạy offline hai lần, compare semantic output, mở evidence, ghi môi trường/timing/memory và 5/5 interpretation answers nếu giữ rubric.

#71: sau #70 PASS, owner accepts D09/contracts. #72: sau #71, một vertical slice thật và unit/integration/E2E/replay tests. #73: independent clean-environment replay, traceability, interpretation và budget theo tiêu chí accepted; tiêu chí còn thiếu thì NOT PASSED. Dừng build khi đủ criteria.

**Bước nhỏ nhất tiếp theo:** owner quyết định A1/A2/A3/D07/D08/F1 và G70 theo đúng packet/hash. **Rủi ro deadline CAO**: demo retrospective descriptive trước hoặc trong 15/10 còn có thể nếu gate được duyệt sớm và reviewer thật sẵn sàng; không bảo đảm. Không có evidence để hứa scientifically validated trend-detection product vào mốc đó. [Decision-gate skill](../../../.agents/skills/sites-decision-gate/SKILL.md) yêu cầu “stop before implicit acceptance”; repo contract và yêu cầu owner cũng giữ #70/#71 gates.
