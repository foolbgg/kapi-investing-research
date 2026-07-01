---
name: kapi-investing-research
description: Use when analyzing the public-safe 卡皮巴菲特 investing research index, summarizing investment education themes, comment FAQ patterns, or drafting style-inspired but non-impersonating Chinese investing education content.
---

# Kapi Investing Research

## Overview

Use this skill with the public-safe index in this repository. It supports topic summaries, note-title lookup, FAQ synthesis and style-inspired writing.

This is not an impersonation skill. Never claim to be 卡皮巴菲特 or imply endorsement by the account owner.

## Data

- `data/public_index.json`: sanitized note index.
- `docs/research-summary.md`: theme summary.
- `docs/comment-faq.md`: synthesized reader FAQ.

The public package excludes raw images, full OCR, raw comments and raw scrape files.

## Workflow

1. Search `data/public_index.json` or run `python3 scripts/search_public_index.py "<query>"`.
2. Anchor answers to note titles, topics and public note IDs.
3. Separate observed evidence from synthesis and caveats.
4. For writing, borrow only the educational structure: sharp opener, mechanism explanation, action filter, risk caveat.

## Guardrails

- Do not impersonate the account owner.
- Do not reproduce long original passages.
- Do not provide personalized financial, tax or legal advice.
- State that this is a captured subset, not the complete account corpus.
