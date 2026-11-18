# Codebook

All CSV files in this package are UTF-8, comma-separated, with one header row.

The blank data extraction form (fields, what to record, allowed values) is
`extraction_template.csv`. Extraction rule used by both reviewers: extract what the
paper says, with page number; write `NR` (not reported) instead of leaving a field
blank; interpretation goes in `Reviewer comment`.

`extraction_log.csv` is the completed form: one row per full text (P01 to P29), 30
columns, exported from the reviewers' extraction workbook. Extractors are given as
Person A (reviewer A) and Person B (reviewer B).
P14 and P16 were excluded at full text before extraction, so their rows are empty.
The other tables in this folder are derived from it.

## extraction_table.csv (25 included papers)

| Column | Source |
|--------|--------|
| paper_id | Log: `Paper ID` |
| bibtex_key | Key of the matching entry in `../references.bib` (matched on title) |
| title | Log: `Title (auto)` |
| reference | Log: `Authors/Year/Venue` (verbatim) |
| year | `year` field of the matching refs.bib entry |
| venue | `journal` or `booktitle` field of the matching refs.bib entry |
| setting | Log: `Setting` (Academic / Industry / Both) |
| genre | Log: `Genre` |
| primary_goal | Log: `Primary goal` |
| main_technique | Log: `AI technique` |
| agent_type | Log: `Agent / persona` |
| quality_score | Sum of Q1 to Q6 in `quality_scores.csv` |

## fulltext_decisions.csv (29 full texts)

| Column | Meaning |
|--------|---------|
| paper_id | P01 to P29 |
| route | `database` (P01 to P20 and P29: the 21 records advanced from screening) or `ai_search (SE venue)` (P21 to P28) |
| screening_record_id | Rayyan id in `../screening/screening_decisions.csv` (empty for AI-route papers) |
| full_text_decision | `included` or `excluded` |
| exclusion_reason | For excluded papers: the log's `Reviewer comment` (P09, P19) or the reviewer's note on the record (P14, P16), verbatim |

## quality_scores.csv

Quality checklist, scored 1 = yes, 0.5 = partly, 0 = no. Used to describe the
strength of evidence, not to exclude papers.

| Item | Question |
|------|----------|
| Q1 | Aim clearly stated |
| Q2 | Method described well enough to replicate |
| Q3 | Evaluation/validation reported (not just proposal) |
| Q4 | Compared against baseline/human data |
| Q5 | Limitations discussed |
| Q6 | Findings clearly linked to the aims |
| total | Sum of Q1 to Q6 (0 to 6) |

Excluded papers have `NA` (not assessed), never 0. Summary: 25 included papers,
total 118, mean 4.72.

The log's `Quality (0-6)` column was a working copy and differs from the Q1 to Q6
sum for four papers (P07 5.5 vs 5.0, P11 4.5 vs 4.0, P13 5.5 vs 5.0, P26 2.0 vs 5.0).
The item scores are authoritative and are used everywhere in this package.

## synthesis_matrix.csv (in ../synthesis/)

One row per included paper (25); columns `paper_id`, `bibtex_key`, `title`, then one
column per theme with 1 (paper supports the theme) or 0. Themes and assignments are
from Table 6 of the paper. The synthesis method is described in
`../synthesis/synthesis_method.md`.

| Theme | Name | Papers |
|-------|------|-------:|
| T1 | Coverage used as a proxy for bugs | 6 |
| T2 | Human-likeness gap | 12 |
| T3 | PCG transfer proposed but untested | 8 |
