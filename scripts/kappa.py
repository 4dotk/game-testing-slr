#!/usr/bin/env python3
"""Cohen's kappa and percentage agreement for two screeners.

Usage 1 - from a Rayyan CSV export (Rayyan stores each reviewer's decision in
the "notes" column as: RAYYAN-INCLUSION: {"Name A"=>"Included", "Name B"=>"Excluded"}):
    python3 kappa.py articles.csv
    python3 kappa.py articles.csv --maybe-as Included   # count "Maybe" as include

Usage 2 - from counts you type in yourself (2x2 table):
    python3 kappa.py --counts BOTH_INCLUDE A_ONLY B_ONLY BOTH_EXCLUDE
    (A_ONLY = A included, B excluded; B_ONLY = B included, A excluded)
"""
import argparse, csv, re, sys
from collections import Counter

def kappa(pairs):
    n = len(pairs)
    cats = sorted({c for p in pairs for c in p})
    agree = sum(a == b for a, b in pairs)
    po = agree / n
    ca = Counter(a for a, _ in pairs); cb = Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
    k = (po - pe) / (1 - pe) if pe < 1 else 1.0
    return n, agree, po, pe, k, cats

def from_rayyan(path, maybe_as):
    pairs, names, skipped = [], None, 0
    with open(path, newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            notes = row.get('notes') or row.get('Notes') or ''
            m = re.search(r'RAYYAN-INCLUSION:\s*\{(.*?)\}', notes)
            if not m:
                skipped += 1; continue
            d = dict(re.findall(r'"([^"]+)"\s*=>\s*"([^"]+)"', m.group(1)))
            if names is None:
                names = sorted(d)
            if len(d) != 2 or sorted(d) != names:
                skipped += 1; continue
            dec = [d[n] for n in names]
            if maybe_as:
                dec = [maybe_as if x == 'Maybe' else x for x in dec]
            pairs.append(tuple(dec))
    return pairs, names, skipped

ap = argparse.ArgumentParser()
ap.add_argument('csv', nargs='?')
ap.add_argument('--maybe-as', choices=['Included', 'Excluded'])
ap.add_argument('--counts', nargs=4, type=int,
                metavar=('BOTH_INC', 'A_ONLY', 'B_ONLY', 'BOTH_EXC'))
a = ap.parse_args()

if a.counts:
    bi, ao, bo, be = a.counts
    pairs = ([('I', 'I')] * bi + [('I', 'E')] * ao + [('E', 'I')] * bo + [('E', 'E')] * be)
    names = ['A', 'B']; skipped = 0
elif a.csv:
    pairs, names, skipped = from_rayyan(a.csv, a.maybe_as)
    if not pairs:
        sys.exit('No reviewer decisions found. Check that the export includes '
                 'decisions (notes column with RAYYAN-INCLUSION).')
else:
    ap.print_help(); sys.exit(1)

n, agree, po, pe, k, cats = kappa(pairs)
print(f'Reviewers: {names}')
print(f'Records with two decisions: {n}' + (f' (skipped {skipped})' if skipped else ''))
print(f'Categories: {cats}')
print(f'Agreements: {agree}, disagreements: {n - agree}')
print(f'Percentage agreement: {100 * po:.1f}%')
print(f"Cohen's kappa: {k:.2f}")
