# 05 — Checklist Research Entry

**Đối tượng review:** `docs/research-entry`, từ commit `dev` `0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`; bộ tài liệu research-entry-v1 và các sửa đổi baseline liên quan. Ngày review: 20/09/2026. Reviewer: Codex, tác giả tự review theo `sites-review`; không phải independent replay hoặc user validation.

**Kết quả hiện tại:** REVIEW PENDING. Trạng thái gate áp dụng cho artifacts đã review trên nhánh này, không tự áp dụng cho remote `master`.

| Tiêu chí | Bằng chứng | Trạng thái / finding / việc còn thiếu |
| --- | --- | --- |
| Chủ dự án chấp thuận D05 và D06 | [Decision log](../master/07_DECISION_LOG.md) | Đã ghi; cần kiểm tra nhất quán giữa các tài liệu baseline |
| P0 và R1–R8 có construct, evidence, falsifier và owner | [Research questions](../master/02_RESEARCH_QUESTIONS.md) | Đã chuẩn bị; cần review coverage |
| Claim giữ mô tả và có giới hạn | [M1](../baseline/M1.md), [scope](../master/01_SCOPE_AND_NON_GOALS.md) | Đã chuẩn bị; chưa chọn provider hoặc metric |
| Có search, exclusion, counterevidence và stopping rules | [Research protocol](00_RESEARCH_PROTOCOL.md) | Đã chuẩn bị; không claim literature review hoàn chỉnh |
| Capture claim/source giữ giới hạn đọc | [Ledger](01_EVIDENCE_LEDGER.md), [prior-art map](../master/03_PRIOR_ART_MAP.md) | Đã chuẩn bị; chưa có findings hoặc phép đo mới |
| Có quy trình audit để chọn provider | [Audit plan](02_SOURCE_AUDIT_PLAN.md) | Đã chuẩn bị; cả năm ứng viên NOT AUDITED |
| Chọn case/control trước output và tránh holdout tuning | [Case protocol](03_CASE_SELECTION_PROTOCOL.md) | Đã chuẩn bị; không claim đã chọn hoặc freeze case |
| Chỉ báo vẫn là ứng viên; D07–D09 còn mở | [Candidates](04_SIGNAL_CANDIDATES.md), [decision log](../master/07_DECISION_LOG.md) | Đã chuẩn bị; chưa freeze công thức/ngưỡng/stack |
| Giới hạn temporal không âm thầm làm M1 đạt | [Evaluation protocol](../master/06_EVALUATION_PROTOCOL.md) | E3 NOT PASSED khi thiếu availability evidence |
| Hai issues tạo hàng đợi giới hạn; có R5/R8 | [Backlog](../master/08_MONTH1_BACKLOG.md) | Chờ đăng và đọc lại issues; WIP tối đa hai |
| Tách trạng thái hiện tại khỏi lịch sử | [Current state](../master/09_CURRENT_STATE.md) | Chờ refresh trạng thái cuối |
| Hai ngôn ngữ nhất quán và links mở đúng | [Documentation policy](../../README.md) | Chờ mechanical checks và bilingual review |

## Ý nghĩa các gate

- **define-ready:** D05/D06 accepted và không còn BLOCKER/MAJOR về M0/định nghĩa trong phạm vi review.
- **Research Entry:** define-ready cùng protocol, capture/audit/case/signal procedures có thể kiểm tra và hàng đợi thực hiện, không còn BLOCKER/MAJOR về entry.
- **research-ready:** cần literature và sample/temporal evidence, so sánh chỉ báo, case/control và freeze proposal về sau, sau đó D07/D08 được chấp thuận rõ ràng. Tài liệu chuẩn bị này chưa làm gate đạt.
- Preimplementation, feature và product gates vẫn NOT PASSED. Review tài liệu không đánh dấu E1–E8 đạt.

## Bản ghi review

Còn chờ: bao quát mọi file thay đổi, kiểm tra UTF-8/Markdown/internal links và ý nghĩa bản dịch, xác minh issue bodies, liệt kê findings cùng kết quả kiểm tra chính xác. Provider sampling, đọc lại toàn bộ papers, runtime tests, independent replay và user validation nằm ngoài entry review này và còn thiếu.
