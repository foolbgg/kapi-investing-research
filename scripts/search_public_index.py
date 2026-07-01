#!/usr/bin/env python3
import argparse
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

def compact(text, limit=260):
    text = re.sub(r'\s+', ' ', text or '').strip()
    return text if len(text) <= limit else text[:limit - 1].rstrip() + '…'

parser = argparse.ArgumentParser()
parser.add_argument('query', nargs='+')
parser.add_argument('--limit', type=int, default=8)
args = parser.parse_args()

data = json.loads((ROOT / 'data' / 'public_index.json').read_text(encoding='utf-8'))
terms = [part.lower() for raw in args.query for part in re.split(r'\s+', raw) if part]
rows = []
for note in data['notes']:
    haystack = ' '.join([
        note.get('title', ''),
        ' '.join(note.get('topics', [])),
        ' '.join(note.get('topKeywords', [])),
        note.get('abstract', ''),
    ]).lower()
    score = 0
    for term in terms:
        count = haystack.count(term)
        score += count
        if term in note.get('title', '').lower():
            score += 8
    if score:
        rows.append((score, note))
rows.sort(key=lambda item: (-item[0], item[1].get('order') or 999))
for score, note in rows[:args.limit]:
    print(json.dumps({
        'score': score,
        'order': note.get('order'),
        'noteId': note.get('noteId'),
        'title': note.get('title'),
        'date': note.get('date'),
        'topics': note.get('topics'),
        'topKeywords': note.get('topKeywords'),
        'publicUrl': note.get('publicUrl'),
        'abstract': compact(note.get('abstract')),
    }, ensure_ascii=False, sort_keys=True))
