# PRISMA 2020 flow: counts and how each is derived

Every count below was recomputed from the files in this package.

## Database route

| Box | Count | Derivation |
|-----|------:|------------|
| Records identified: Google Scholar | 211 | Seven queries, top three result pages each: G1, G2, G3 and G7 (121) plus G4 to G6 (90), the entries in `search/exports/google_scholar_G1..G7.bib`. One G2 entry (`noauthor_procedurally_nodate`) is a saved Scholar results page, not a paper |
| Records identified: ACM DL | 16 | Entries in `search/exports/acm_dl.bib` |
| Records identified: IEEE Xplore | 25 | Entries in `search/exports/ieee_xplore.bib` |
| **Records identified (total)** | **252** | 211 + 16 + 25 |
| Duplicates removed | 50 | 252 − 202 records in the Rayyan export (`screening/raw/rayyan_articles.ris`). Deduplication was done in Rayyan. The saved Scholar results page was not removed: it is screened record `rayyan-734749658`, excluded at title/abstract. Note: an exact match on normalised titles across the exports finds 51 repeats rather than 50; the one-record difference from Rayyan's deduplication was not traced |
| **Records screened** | **202** | Rows in `screening/screening_decisions.csv` |
| Excluded at title/abstract | 181 | `final_decision = exclude` |
| **Full texts assessed** | **21** | `final_decision = advance`. These are P01 to P20 and P29 in `extraction/fulltext_decisions.csv` (`route = database`) |
| Excluded at full text | 4 | P09, P14, P16, P19 (`full_text_decision = excluded`, reasons in `exclusion_reason`) |
| **Included from databases** | **17** | 21 − 4 |

Note on Rupp et al. (2024), P29: this record was initially excluded at title/abstract
screening after a reviewer conflict. After further discussion, the reviewers decided
to include it; it was assessed at full text and included. Rayyan was updated on
2026-11-18 to reflect this decision (see `screening/raw/rayyan_decision_log.csv`).

## AI-assisted search route (software engineering venues)

| Box | Count | Derivation |
|-----|------:|------------|
| Shortlisted | 32 | Rows in `ai_search/candidates.csv` (sheet "Shortlist (32)" of `se_venues_search.xlsx`) |
| Duplicates of database records | 3 | Shortlist #9, #10, #12, whose titles appear in the database exports (`decision = duplicate`) |
| Assessed | 29 | 32 − 3 |
| Excluded | 21 | `decision = excluded` |
| **Included (SE venues)** | **8** | P21 to P28 (`decision = included`) |

## Total

| Box | Count | Derivation |
|-----|------:|------------|
| **Studies included in the review** | **25** | 17 + 8; equals the rows of `extraction/extraction_table.csv` |

## Screening agreement (first independent decisions)

From `python3 screening/agreement.py`, with "include" and "maybe" both counted as
"advance to full text": 202 records, 168 agreements, **34 conflicts**, **83.2%**
agreement, **Cohen's kappa 0.27**. (Treating include / maybe / exclude as three
separate categories gives 40 conflicts instead.) All 34 conflicts were resolved by
discussion between the two reviewers.

The first decisions are each reviewer's earliest decision per record in the
timestamped Rayyan decision log (`screening/raw/rayyan_decision_log.csv`); all 404
match the reviewers' own decisions table (`screening/raw/screening_decisions.csv`).

## Quality

25 included papers, total 118, mean 4.72 (`extraction/quality_scores.csv`, sum of
Q1 to Q6 per paper). Excluded papers are NA.

## Figure

`prisma.pdf` in this folder is the flow diagram used in the paper.
