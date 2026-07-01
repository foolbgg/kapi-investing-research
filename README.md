# Kapi Investing Research / 卡皮巴菲特投资科普研究索引

## 中文介绍

这是一个面向公开发布的安全版研究索引，来源于本地整理的 **卡皮巴菲特**（小红书号：`dingtou_plan`）小红书投资科普研究库。

本仓库不隶属于、不代表、也未获得账号本人背书。它只用于投资科普内容研究、主题检索、评论区问题归纳，以及“风格启发但不冒充本人”的写作辅助。

### 包含内容

- 公开安全版主题摘要和观点地图。
- 脱敏后的笔记索引：标题、笔记 ID、主题、数量统计和公开笔记链接。
- 从可见评论综合出的 FAQ，不包含原始用户名、完整评论或完整作者回复。
- 一个用于检索公开索引的小脚本。
- 一个 Codex skill scaffold，用于研究、问答和非冒充式写作辅助。

### 不包含内容

- 下载的小红书图片。
- 图片笔记的完整 OCR 文本。
- 原始评论、用户名、作者回复或原始抓取 JSON。
- 带登录态参数的小红书 URL。

### 数据范围

- 本次公开索引覆盖：32 篇主页可见笔记。
- 主页显示笔记数：235。
- 私有本地研究库中曾包含 418 张图片 OCR 和 311 条可见评论/回复，但这些原始材料没有进入公开仓库。

因此，本仓库不应被理解为账号的完整归档。

### 使用方法

检索公开安全索引：

```bash
python3 scripts/search_public_index.py "VOO QQQ"
python3 scripts/search_public_index.py "CRS 港卡"
python3 scripts/search_public_index.py "定投 EDCA"
```

如需本地使用 skill，可将 `skill/kapi-investing-research` 复制到 Codex skills 目录，然后调用 `$kapi-investing-research`。

### 注意事项

本仓库仅用于教育研究和写作辅助，不构成金融、税务、法律或投资建议。涉及税务、券商开户、CRS、账户出入金、产品适配等问题时，应以最新官方信息和专业意见为准。

## English Introduction

This is a public-safe research index derived from a local research library for the Xiaohongshu investing-education account **卡皮巴菲特** (`dingtou_plan`).

This repository is not affiliated with, endorsed by, or operated by the account owner. It is intended for investment-education research, topic lookup, comment FAQ synthesis, and style-inspired writing assistance that does not impersonate the author.

### What Is Included

- Public-safe topic summary and view map.
- A sanitized note index with titles, note IDs, topics, counts and public note links.
- A comment FAQ synthesized from visible comments, without raw usernames, full comments or full author replies.
- A small search script for the sanitized index.
- A Codex skill scaffold for research, Q&A and non-impersonating writing assistance.

### What Is Not Included

- Downloaded Xiaohongshu images.
- Full OCR text from image notes.
- Raw comments, usernames, author replies or raw scrape JSON.
- Xiaohongshu URLs containing login-state query parameters.

### Scope

- Captured note subset: 32 visible profile notes.
- Profile displayed note count: 235.
- The private local research library included OCR for 418 images and 311 visible comments/replies, but those raw materials are intentionally excluded from this public repository.

This repository should not be treated as a complete archive of the account.

### Usage

Search the sanitized public index:

```bash
python3 scripts/search_public_index.py "VOO QQQ"
python3 scripts/search_public_index.py "CRS 港卡"
python3 scripts/search_public_index.py "定投 EDCA"
```

To use the skill locally, copy `skill/kapi-investing-research` into your Codex skills directory and invoke `$kapi-investing-research`.

### Caution

This repository is for educational research and writing support only. It is not financial, tax, legal or investment advice. For tax, brokerage access, CRS, account-opening, fund-transfer or product-suitability decisions, check current official sources and professional guidance.
