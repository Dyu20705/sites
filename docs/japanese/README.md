# SITES — Scholar Intelligent Trend Evolution System

[English](../../README.md) · [Tiếng Việt](../vietnamese/README.md) · 日本語

**SITES** は、科学技術に関する概念が時間とともにどのように変化するかを、検証可能な根拠に基づいて分析することを目指す研究志向の scholarly intelligence プロジェクトです。

長期的な構想は、学術論文やトレンド可視化だけに限定されません。まずは学術文献を出発点とし、将来的には他の証拠源や、より高度な分析・意思決定支援へ拡張できることを想定しています。

~~~text
evidence acquisition → monitoring → mining → trend detection
→ forecasting → recommendation / decision support → automation / optimization
~~~

## 現在の重点

このリポジトリは現在 **M0 — プロジェクト定義** の段階です。現行ツリーには、現在有効な製品実装や実行可能な製品テストスイートはありません。

**Month 1（2026-09-17〜2026-10-17）** では、対象を意図的に絞ります。

- scholarly evidence から開始する;
- detection と descriptive trend intelligence に集中する;
- 小さく、再現可能な end-to-end slice を構築する;
- forecasting、recommendation、optimization、autonomous agents、大規模インフラは、後続の正式な意思決定がない限り M1 の対象外とする。

主要ユーザー、データ提供元、corpus、signal 定義、storage、framework、dashboard 技術、deployment 方式などの具体的な選択は、研究結果と decision gate を通して決定します。

## ドキュメント

全体の構成と翻訳状況は [documentation index](../README.md) を参照してください。

詳細な M0/M1 ドキュメントは現在ベトナム語版を中心にレビュー中です。日本語版は、内容が安定し実際に翻訳・レビューされたものから順次追加します。

翻訳は逐語訳ではなく、**意味・決定・要件・日付・ステータスを一致させた自然な文章**を優先します。

## リポジトリの状態と履歴

過去のコード、設計文書、issue は Git history に残されています。これらは参考資料として利用できますが、現在のアーキテクチャやロードマップを自動的に決めるものではありません。

古い実装、データソース、schema、metric、technology stack を再利用する場合は、現在の要件と根拠に照らして再評価する必要があります。

M0 の repository reset と documentation review は [PR #62](https://github.com/Dyu20705/sites/pull/62) を参照してください。
