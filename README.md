# Kapi Investing Research

Public-safe companion package for a local research library built from the Xiaohongshu account **卡皮巴菲特** (`dingtou_plan`).

This repository is not affiliated with, endorsed by, or operated by the account owner. It is a research and writing-assistance index.

## What Is Included

- Public-safe topic summary and view map.
- A sanitized note index with titles, note IDs, topics, counts and public note links.
- A comment FAQ synthesized from visible comments, without raw usernames or full comment text.
- A small search script for the sanitized index.
- A Codex skill scaffold for research and style-inspired, non-impersonating writing assistance.

## What Is Not Included

- Downloaded Xiaohongshu images.
- Full OCR text from image notes.
- Raw comments, usernames, author replies, or raw detail JSON.
- Login-state query tokens from Xiaohongshu URLs.

## Scope

- Captured note subset: 32 visible profile notes.
- Profile displayed note count: 235.
- The local private research library had OCR for 418 images and 311 visible comments/replies, but those raw materials are intentionally excluded here.

This package should not be treated as a complete archive of the account.

## Usage

Search the sanitized public index:

```bash
python3 scripts/search_public_index.py "VOO QQQ"
python3 scripts/search_public_index.py "CRS 港卡"
python3 scripts/search_public_index.py "定投 EDCA"
```

Use the skill locally by copying `skill/kapi-investing-research` into your Codex skills directory, then invoking `$kapi-investing-research`.

## Caution

This is for educational research and writing support only. It is not financial, tax, legal, or investment advice. For tax, brokerage access, CRS, account-opening, or product suitability decisions, check current official sources and professional guidance.
