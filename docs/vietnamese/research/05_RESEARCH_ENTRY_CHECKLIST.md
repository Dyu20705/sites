# 05 — Checklist Research Entry

**Đối tượng review:** `docs/research-entry`, từ commit `dev` `0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`; commit chuẩn bị `fc0dba983458dbef7523227451e368cfd5bcef17` cùng liên kết issues và bản ghi review trong lần đóng công việc này. Hoàn tất review: 21/09/2026. Reviewer: Codex, tác giả tự review theo `sites-review`; không phải independent replay hoặc user validation.

**Kết quả hiện tại:** phần **review bộ artifact Research Entry đã PASSED** ngày 21/09, nhưng gate Research Entry có thẩm quyền hiện vẫn **NOT PASSED** khi [#68](https://github.com/Dyu20705/sites/issues/68) còn mở. Control graph được tạo sau đó thay thế mọi cách hiểu rằng self-review trên branch đã làm gate của default branch đạt. Research-ready vẫn NOT PASSED.

| Tiêu chí | Bằng chứng | Trạng thái / finding / việc còn thiếu |
| --- | --- | --- |
| Chủ dự án chấp thuận D05 và D06 | [Decision log](../master/07_DECISION_LOG.md) | PASS — acceptance và các quyết định còn mở nhất quán giữa tài liệu baseline |
| P0 và R1–R8 có construct, evidence, falsifier và owner | [Research questions](../master/02_RESEARCH_QUESTIONS.md) | PASS — giữ P0; bao phủ cả tám RQs |
| Claim giữ mô tả và có giới hạn | [M1](../baseline/M1.md), [scope](../master/01_SCOPE_AND_NON_GOALS.md) | PASS — chưa chọn provider hoặc metric |
| Có search, exclusion, counterevidence và stopping rules | [Research protocol](00_RESEARCH_PROTOCOL.md) | PASS — không claim literature review hoàn chỉnh |
| Capture claim/source giữ giới hạn đọc | [Ledger](01_EVIDENCE_LEDGER.md), [prior-art map](../master/03_PRIOR_ART_MAP.md) | PASS — chưa có findings hoặc phép đo mới |
| Có quy trình audit để chọn provider | [Audit plan](02_SOURCE_AUDIT_PLAN.md) | PASS — chỉ có quy trình; cả năm ứng viên NOT AUDITED |
| Chọn case/control trước output và tránh holdout tuning | [Case protocol](03_CASE_SELECTION_PROTOCOL.md) | PASS — có quy tắc; không claim đã chọn hoặc freeze case |
| Chỉ báo vẫn là ứng viên; D07–D09 còn mở | [Candidates](04_SIGNAL_CANDIDATES.md), [decision log](../master/07_DECISION_LOG.md) | PASS — chưa freeze công thức/ngưỡng/stack |
| Giới hạn temporal không âm thầm làm M1 đạt | [Evaluation protocol](../master/06_EVALUATION_PROTOCOL.md) | PASS — giữ tiêu chí E3; E3 NOT PASSED khi thiếu availability evidence |
| Hai issues tạo hàng đợi giới hạn; có R5/R8 | [Backlog](../master/08_MONTH1_BACKLOG.md) | PASS về cấu trúc hàng đợi — #64/#65 tồn tại nhưng #68 có thẩm quyền vẫn đang chặn thực thi; WIP chỉ là #68 cho tới khi merge được chấp thuận và gate đạt |
| Tách trạng thái hiện tại khỏi lịch sử | [Current state](../master/09_CURRENT_STATE.md) | PASS — snapshot ngày 21/09; giữ riêng lịch sử 18/09 |
| Hai ngôn ngữ nhất quán và links mở đúng | [Documentation policy](../../README.md) | PASS — hoàn tất structural checks và review ý nghĩa Việt–Anh |

## Ý nghĩa các gate

- **define-ready:** D05/D06 accepted và không còn BLOCKER/MAJOR về M0/định nghĩa trong phạm vi review.
- **Research Entry:** bộ artifact phải đáp ứng các điều kiện trên, đồng thời issue #68 có thẩm quyền phải ghi PASSED sau khi documentation merge được chấp thuận. Self-review trên branch không tự làm gate này đạt.
- **research-ready:** cần literature và sample/temporal evidence, so sánh chỉ báo, case/control và freeze proposal về sau, sau đó D07/D08 được chấp thuận rõ ràng thông qua issue #70 có thẩm quyền. Tài liệu chuẩn bị này chưa làm gate đạt.
- Preimplementation, feature và product gates vẫn NOT PASSED. Review tài liệu không đánh dấu E1–E8 đạt.

## Bản ghi review

### Review lịch sử của bộ artifact — 21/09/2026

So với baseline `dev`, cả 36 file thay đổi đã được review: hai mục lục repository/documentation, hai README ngôn ngữ, hai định nghĩa M1, 18 master documents và 12 research documents. Không loại file nào trong changeset `dev → docs/research-entry`. Review Việt–Anh đối chiếu decision status, scope, ngày, RQ ownership, giới hạn bằng chứng, stop conditions và temporal/case rules. Cả hai tài liệu kiến trúc khái niệm đều không thay đổi **so với baseline `dev` đó**, nên không được re-review như thay đổi thiết kế mới; D09 vẫn mở.

Kết quả kiểm tra của review ngày 21/09:

- Giải mã UTF-8 nghiêm ngặt, đích local file links, code fences cân bằng và số cột bảng: 38 file Markdown, 18 cặp ngôn ngữ, 169 local links và 51 bảng; không có lỗi được báo. Đây là structural checks có mục tiêu, không phải full Markdown renderer hoặc external-source audit.
- Decision-state checks: D05/D06 ACCEPTED, D07–D09 PROPOSED, D10 DEFERRED ở cả hai ngôn ngữ. P0 và dòng acceptance E3 khớp baseline gốc. Mọi R1–R8 có dòng evidence/decision và construct/falsifier/owner.
- `git diff --check` so với baseline đó: đạt. Không chạy product tests vì changeset chỉ gồm tài liệu.
- Đọc lại GitHub lúc 07:57 +07:00 ngày 21/09: #64 và #65 OPEN, body khớp bản nháp đã chuẩn bị; cả bảy đường dẫn tài liệu riêng biệt được liên kết đều tồn tại trong commit chuẩn bị `fc0dba9`.

Đã xử lý trong quá trình chuẩn bị: tham chiếu D05/D06 proposal cũ, thiếu RQ ownership/falsifiers, thiếu research procedures, current state cũ và thiếu operational issues. Không còn entry BLOCKER/MAJOR chưa xử lý trong review lịch sử của bộ artifact. Provider sampling, đọc lại toàn bộ papers, runtime tests, independent replay và user validation nằm ngoài review entry đó và vẫn còn thiếu.

### Review đối soát PR #74 — 23/09/2026

PR #74 dùng `master` thay vì `dev` làm base, vì vậy diff hiện tại có **39 file thay đổi**, không phải 36: `.gitignore`; bốn file navigation/README đang hoạt động; hai file baseline M1; 19 master documents; 12 research documents; và việc xóa `docs/japanese/README.md`.

Ba path xuất hiện trong diff `master → docs/research-entry` nhưng không thuộc changeset dùng baseline `dev` ngày 21/09 đã được kiểm tra riêng trong lần đối soát này:

- `.gitignore`: chỉ thêm exclusion `docs/local/` cho artifact review local; không thay đổi quyết định project/research.
- `docs/english/master/04_SYSTEM_ARCHITECTURE.md`: vẫn ở trạng thái **PROPOSED — D09**, cho phép triển khai trong một chương trình và để provider/storage/framework/query/dashboard/deployment ở trạng thái mở.
- việc xóa `docs/japanese/README.md`: loại bỏ một language entry chưa hoàn chỉnh/cũ; documentation index hiện chỉ claim hai bộ English và Vietnamese đã được review.

Phần đối soát gate-sensitive đã re-review `docs/README.md`, cặp Month-1 backlog, cặp current-state document và cặp Research Entry checklist. Các tài liệu này hiện thống nhất rằng #68 có thẩm quyền với Research Entry, #70 có thẩm quyền với Research Exit/research-ready, #64/#65 tiếp tục bị chặn cho tới khi #68 đạt, và D07–D09 vẫn mở. Phần đối soát ngày 23/09 bổ sung cho bản ghi lịch sử ngày 21/09, không viết lại lịch sử đó.

## Cập nhật thẩm quyền — 23/09/2026

Sau lần self-review của bộ tài liệu, dự án đã tạo #66 (Control Tower), #67 (M1 roadmap), #68 (gate Research Entry có thẩm quyền), #69 (prior-art tracker) và #70 (Research Exit gate). Control graph được tạo sau có thẩm quyền đối với thứ tự thực thi. Vì vậy #64/#65 vẫn bị chặn, chưa claim bất kỳ literature/provider experiment nào đã được thực hiện theo hai work package đó, và chữ PASS ngày 21/09 trong tài liệu này chỉ có nghĩa **review bộ artifact đạt** cho tới khi #68 đạt sau một lần merge được chấp thuận.
