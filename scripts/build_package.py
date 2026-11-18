#!/usr/bin/env python3
"""Regenerate the derived tables of this replication package.

Run from the repository root:
    python3 scripts/build_package.py

Inputs (source data, not modified except where noted):
    search/exports/*.bib                         raw database exports
    screening/raw/screening_decisions.csv        reviewers' decisions table (titles, first decisions)
    screening/raw/rayyan_articles.ris            current Rayyan export (final decisions)
    screening/raw/rayyan_decision_log.csv        Rayyan decision log (first decisions, labels)
    ai_search/candidates.csv                     AI-assisted search shortlist (columns shortlist_no to
                                                 pcg_relevance are input; paper_id, decision, reason are recomputed)
    extraction/extraction_log.csv                completed extraction form
    extraction/quality_scores.csv                Q1 to Q6 item scores (the `total` column is recomputed)
    references.bib                               BibTeX keys, venues and years of included papers

Outputs:
    screening/screening_decisions.csv
    extraction/fulltext_decisions.csv
    extraction/extraction_table.csv
    extraction/quality_scores.csv  (totals)
    ai_search/candidates.csv  (paper_id, decision, reason)
    synthesis/synthesis_matrix.csv

Standard library only.
"""
import csv
import glob
import os
import re
from collections import Counter, defaultdict

# Reviewer notes on the full-text exclusions of P14 and P16 (recorded as cell
# comments in the reviewers' extraction workbook; their extraction rows are empty).
EXCLUSION_NOTES = {
    'P14': 'Excluded. Not a published paper, so it fails our inclusion criteria',
    'P16': 'Excluded. Out of scope: the paper’s contribution is a human survey of perceived '
           'balance, not an automated playtesting method.',
}

# Decision note for the one record whose final decision was updated in Rayyan.
NOTE_RECORD = 'rayyan-734717092'
NOTE_TEXT = ('Initially excluded at title/abstract screening after a reviewer conflict. After further '
             'discussion, the reviewers decided to include it; it was assessed at full text and included. '
             'Rayyan was updated on 2026-11-18 to reflect this decision.')

# Synthesis themes and paper assignments, from Table 6 of the paper.
THEMES = {
    'T1': ('Coverage used as a proxy for bugs',
           ['sestini2024', 'jang2026', 'mu2026', 'feldmeier2022', 'chen2025mimic', 'zheng2019wuji']),
    'T2': ('Human-likeness gap',
           ['kalafatis2025', 'chen2025minecraft', 'ariyurek2023', 'perez2025', 'gil2026', 'stahlke2020',
            'ledepelletier2022', 'holmgard2019', 'shu2021', 'khalifa2025', 'chen2025mimic', 'rupp2024']),
    'T3': ('PCG transfer proposed but untested',
           ['ariyurek2023', 'zarembo2019', 'stahlke2020', 'sestini2024', 'ledepelletier2022', 'holmgard2019',
            'albaghajati2023', 'feldmeier2022']),
}

SCREEN_REASON = 'not recorded per record (screened against I1-I8 / E1-E10, see criteria.md)'


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.replace('{', '').replace('}', '').lower())


def prefix_match(a, b):
    return a.startswith(b) or b.startswith(a)


def read_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def write_csv(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(header)
        w.writerows(rows)
    print(f'{path}: {len(rows)} rows')


# ---------------------------------------------------------------- sources
SRC = {'acm_dl.bib': 'ACM DL', 'ieee_xplore.bib': 'IEEE Xplore'}
SRC.update({f'google_scholar_G{i}.bib': f'Google Scholar G{i}' for i in range(1, 8)})
SRC_ORDER = [f'Google Scholar G{i}' for i in range(1, 8)] + ['ACM DL', 'IEEE Xplore']
bib_titles, bib_dois = [], {}
for path in sorted(glob.glob('search/exports/*.bib')):
    src = SRC[os.path.basename(path)]
    with open(path, encoding='utf-8') as f:
        entries = re.split(r'@(?=[A-Za-z]+\s*\{)', f.read())[1:]
    for e in entries:
        t = re.search(r'\btitle\s*=\s*[{"](.*?)[}"]\s*,\s*\n', e, re.S | re.I)
        d = re.search(r'\bdoi\s*=\s*[{"]([^}"]+)', e, re.I)
        if t:
            bib_titles.append((norm(t.group(1)), src))
        if d:
            bib_dois.setdefault(d.group(1).strip().lower(), set()).add(src)


def sources(title, doi):
    found = set(bib_dois.get(doi.strip().lower(), set())) if doi else set()
    nt = norm(title)
    for bt, src in bib_titles:
        if len(bt) >= 20 and (nt.startswith(bt[:60]) or bt.startswith(nt[:60])):
            found.add(src)
    return '; '.join(s for s in SRC_ORDER if s in found) or 'not matched'


# ---------------------------------------------------------------- screening
ris, cur = {}, None
with open('screening/raw/rayyan_articles.ris', encoding='utf-8-sig') as f:
    for line in f:
        if line.startswith('AN  - '):
            cur = line[6:].strip()
        elif line.startswith('N1  - ') and cur and 'RAYYAN-INCLUSION' in line:
            ris[cur] = dict(re.findall(r'"([^"]+)"\s*=>\s*"([^"]+)"', line))

LOG_VALUES = {'1': 'include', '-1': 'exclude', '0': 'maybe'}
first, labels = defaultdict(dict), defaultdict(set)
for r in sorted(read_csv('screening/raw/rayyan_decision_log.csv'), key=lambda r: r['created_at']):
    if r['key'] == 'included' and r['value'] in LOG_VALUES:
        first[r['record_id']].setdefault(r['reviewer'], LOG_VALUES[r['value']])
    elif r['key'] != 'included' and r['value'] != 'deleted':
        labels[r['record_id']].add(r['key'].strip('"'))

RIS_VALUES = {'Included': 'include', 'Excluded': 'exclude', 'Maybe': 'maybe'}
screen_rows = []
for s in read_csv('screening/raw/screening_decisions.csv'):
    rid = s['record_id']
    a_first, b_first = first[rid]['A'], first[rid]['B']
    if (a_first, b_first) != (s['Karthikeya_first'], s['Shantanu_first']):
        raise SystemExit(f'{rid}: first decisions differ between decision log and decisions table')
    a_fin, b_fin = RIS_VALUES[ris[rid]['Karthikeya']], RIS_VALUES[ris[rid]['Shantanu']]
    if a_fin != b_fin:
        raise SystemExit(f'{rid}: unresolved final conflict')
    final = 'exclude' if a_fin == 'exclude' else 'advance'
    screen_rows.append([rid, s['title'], s['year'], s['doi'], sources(s['title'], s['doi']),
                        a_first, b_first, a_fin, b_fin, final, '; '.join(sorted(labels[rid])),
                        NOTE_TEXT if rid == NOTE_RECORD else SCREEN_REASON])
write_csv('screening/screening_decisions.csv',
          ['id', 'title', 'year', 'doi', 'source', 'reviewer_A_first', 'reviewer_B_first',
           'reviewer_A_final', 'reviewer_B_final', 'final_decision', 'rayyan_label', 'reason'], screen_rows)
advanced = {norm(r[1]): r[0] for r in screen_rows if r[9] == 'advance'}

# ---------------------------------------------------------------- quality
log = read_csv('extraction/extraction_log.csv')
quality_in = {r['paper_id']: r for r in read_csv('extraction/quality_scores.csv')}
ITEMS = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
quality_rows, totals = [], {}
for d in log:
    pid, q = d['Paper ID'], quality_in[d['Paper ID']]
    items = [q[i] for i in ITEMS]
    if any(i.upper().startswith('NA') for i in items):
        quality_rows.append([pid, d['Title (auto)'], 'excluded'] + ['NA'] * 7)
    else:
        vals = [float(i) for i in items]
        totals[pid] = sum(vals)
        quality_rows.append([pid, d['Title (auto)'], 'included'] + [f'{v:g}' for v in vals] + [f'{totals[pid]:g}'])
write_csv('extraction/quality_scores.csv', ['paper_id', 'title', 'status'] + ITEMS + ['total'], quality_rows)
print(f'  quality: n={len(totals)} total={sum(totals.values()):g} mean={sum(totals.values()) / len(totals):.2f}')

# ---------------------------------------------------------------- full texts and extraction table
refs = {}
with open('references.bib', encoding='utf-8-sig') as f:
    for e in re.split(r'\n@', f.read()):
        t = re.search(r'\btitle\s*=\s*\{(.*)\},?\s*\n', e)
        if not t:
            continue
        v = re.search(r'\b(journal|booktitle)\s*=\s*\{(.*)\},?\s*\n', e)
        y = re.search(r'\byear\s*=\s*\{?(\d{4})', e)
        k = re.match(r'\s*@?\w+\{([^,]+),', e)
        refs[norm(t.group(1))[:45]] = (k.group(1) if k else '',
                                       v.group(2).replace('{', '').replace('}', '') if v else '',
                                       y.group(1) if y else '')

ft_rows, ext_rows = [], []
for d in log:
    pid, title = d['Paper ID'], d['Title (auto)']
    nt = norm(title)
    rid = next((v for k, v in advanced.items() if prefix_match(k, nt)), '')
    included = pid in totals
    reason = '' if included else (d['Reviewer comment'] or EXCLUSION_NOTES.get(pid, 'not recorded'))
    ft_rows.append([pid, title, 'database' if rid else 'ai_search (SE venue)', rid,
                    'included' if included else 'excluded', reason])
    if included:
        key, venue, year = refs.get(nt[:45], ('', '', ''))
        if not key:
            raise SystemExit(f'{pid}: no matching refs.bib entry')
        ext_rows.append([pid, key, title, d['Authors/Year/Venue'], year, venue, d['Setting'], d['Genre'],
                         d['Primary goal'], d['AI technique'], d['Agent / persona'], f'{totals[pid]:g}'])
write_csv('extraction/fulltext_decisions.csv',
          ['paper_id', 'title', 'route', 'screening_record_id', 'full_text_decision', 'exclusion_reason'], ft_rows)
print('  routes:', dict(Counter((r[2], r[4]) for r in ft_rows)))
write_csv('extraction/extraction_table.csv',
          ['paper_id', 'bibtex_key', 'title', 'reference', 'year', 'venue', 'setting', 'genre',
           'primary_goal', 'main_technique', 'agent_type', 'quality_score'], ext_rows)

# ---------------------------------------------------------------- synthesis matrix
keys = {r[1]: r for r in ext_rows}
for tid, (_, papers) in THEMES.items():
    missing = [k for k in papers if k not in keys]
    if missing:
        raise SystemExit(f'{tid}: unknown bibtex keys {missing}')
write_csv('synthesis/synthesis_matrix.csv', ['paper_id', 'bibtex_key', 'title'] + list(THEMES),
          [[r[0], r[1], r[2]] + [int(r[1] in THEMES[t][1]) for t in THEMES] for r in ext_rows])
print('  papers per theme:', {t: len(p) for t, (_, p) in THEMES.items()})

# ---------------------------------------------------------------- AI-assisted shortlist
SHORTLIST_COLS = ['shortlist_no', 'group', 'title', 'authors', 'year', 'venue_as_seen', 'venue_type',
                  'verification', 'pcg_relevance']
shortlist = read_csv('ai_search/candidates.csv')

full_texts = {norm(d['Title (auto)'])[:40]: d['Paper ID'] for d in log}
db_titles = [bt for bt, _ in bib_titles]
cand_rows = []
for c in shortlist:
    k = norm(c['title'])[:40]
    pid = next((v for kk, v in full_texts.items() if kk.startswith(k[:35]) or k.startswith(kk[:35])), '')
    if any(bt.startswith(k[:35]) for bt in db_titles):
        decision, why, pid = 'duplicate', 'also found by database search', ''
    elif pid:
        decision, why = 'included', f'full text assessed and included as {pid}'
    else:
        decision, why = 'excluded', 'not recorded per record'
    cand_rows.append([c[col] for col in SHORTLIST_COLS] + [pid, decision, why])
write_csv('ai_search/candidates.csv', SHORTLIST_COLS + ['paper_id', 'decision', 'reason'], cand_rows)
print('  candidate decisions:', dict(Counter(r[-2] for r in cand_rows)))
