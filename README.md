# Replication package

This repository is the replication package for the systematic literature review
**"Automated Video Game Testing with Agents and Test Oracles: A Systematic Review and
Implications for PCG"** (Karthikeya Aduri and Shantanu Mande, 2026). It contains the
search strings and raw database exports, the Rayyan screening export with the
timestamped decision log, the per-record title/abstract screening decisions of both
reviewers with a script that recomputes inter-rater agreement, the log and shortlist
of the AI-assisted search of software engineering venues, the blank extraction form
and the completed extraction for every full text, the quality appraisal (Q1 to Q6),
the synthesis method, and a derivation of every count in the PRISMA 2020 flow
diagram. Every number in this README can be recomputed from the files listed below.

## Contents

| Path | What it contains |
|------|------------------|
| `README.md` | This file |
| `LICENSE` | CC BY 4.0 for data and documentation, MIT for code |
| `CITATION.cff` | Citation metadata (read by GitHub and Zenodo) |
| `search/search_strings.md` | Exact query per source (IEEE Xplore, ACM DL, Google Scholar G1 to G7), filters and record counts |
| `search/exports/` | Raw BibTeX exports as downloaded: `google_scholar_G1.bib` to `google_scholar_G7.bib`, `acm_dl.bib`, `ieee_xplore.bib` |
| `screening/criteria.md` | Inclusion (I1 to I8) and exclusion (E1 to E10) criteria |
| `screening/screening_decisions.csv` | One row per screened record (202): id, title, year, DOI, source export(s), first and final decision of reviewer A and B, final decision, Rayyan label, reason |
| `screening/agreement.py` | Recomputes percent agreement, Cohen's kappa and the number of conflicts from `screening_decisions.csv` |
| `screening/raw/rayyan_articles.ris` | Current Rayyan export of the 202 deduplicated records (final decisions in `N1`) |
| `screening/raw/rayyan_decision_log.csv` | Rayyan's timestamped decision log (every decision change), with reviewer identities replaced by A/B |
| `screening/raw/screening_decisions.csv` | The reviewers' own decisions table (first and final decisions, columns named by reviewer), made before that update |
| `ai_search/search_log.csv` | Verbatim query log of the AI-assisted search (S12 to S44) |
| `ai_search/candidates.csv` | The 32 shortlisted records with decision (included / duplicate / excluded) and reason |
| `ai_search/prompt_used.md` | How the AI-assisted search was run (tool, logged queries, verification) |
| `extraction/extraction_template.csv` | Blank data extraction form: field, what to record, allowed values |
| `extraction/extraction_log.csv` | Completed extraction for all 29 full texts (P01 to P29), 29 columns |
| `extraction/extraction_table.csv` | 25 included papers: reference, year, venue, setting, genre, primary goal, main technique, agent type, quality score |
| `extraction/fulltext_decisions.csv` | All 29 full texts: route, decision, exclusion reason |
| `extraction/quality_scores.csv` | Q1 to Q6 and total per paper; excluded papers are NA |
| `extraction/codebook.md` | Quality checklist and the meaning and source of every column |
| `synthesis/synthesis_method.md` | Synthesis method (descriptive mapping and thematic synthesis) |
| `synthesis/synthesis_matrix.csv` | Included papers × themes T1 to T3 (Table 6 of the paper) |
| `prisma/prisma_numbers.md` | Every count in the PRISMA flow diagram and how it is derived |
| `prisma/prisma.pdf` | The PRISMA 2020 flow diagram used in the paper |
| `scripts/build_package.py` | Regenerates all derived tables (screening decisions, full-text decisions, extraction table, quality totals, AI-search candidates, synthesis matrix) from the source files |
| `references.bib` | BibTeX entries for the 25 included studies and the method references cited in the paper |

The working files from before this package was organised are kept in the git
history (commit `16e8fdb`).

Reviewer A is Karthikeya Aduri; reviewer B is Shantanu Mande.

No packages beyond the Python 3 standard library are required.

## How to reproduce

### 1. Searches

Run the queries in `search/search_strings.md` in each source:

- **IEEE Xplore**: Command Search, All Metadata, 2015 to 2026 (25 records).
- **ACM Digital Library**: Advanced Search, ACM Full-Text Collection, 2015 to 2026 (16 records).
- **Google Scholar**: seven queries G1 to G7, top three result pages (30 results) of each ranked by relevance, 2015 to 2026. The 211 exported records are G1, G2, G3 and G7 (121) plus G4 to G6 (90); the G2 export also contains one saved results page, which was imported and excluded at screening.

All three sources were searched in October 2026.
Import all exports into Rayyan and remove duplicates; this yields the 202 records in
`screening/raw/rayyan_articles.ris`.

### 2. Screening agreement

```
python3 screening/agreement.py
```

It compares the reviewers' first independent decisions, counting "include" and
"maybe" as "advance to full text". Expected output: 202 records, 34 conflicts,
83.2% agreement, Cohen's kappa 0.27, final decisions 181 exclude / 21 advance.
The first decisions can be checked against the earliest entry per reviewer and
record in `screening/raw/rayyan_decision_log.csv`. All 34 conflicts were resolved
by discussion between the two reviewers.

### 3. Regenerating the tables

```
python3 scripts/build_package.py
```

Rebuilds every derived CSV from the exports, the Rayyan files, the AI-search
workbook, the extraction log and the Q1 to Q6 item scores, and prints the key
counts (181 / 21 screening, 17 + 8 included, quality total 118, mean 4.72).

### 4. PRISMA counts

`prisma/prisma_numbers.md` maps each box of the flow diagram to the file and rule
that produce it:

- Database route: 252 identified (Google Scholar 211, ACM DL 16, IEEE Xplore 25)
  → 50 duplicates removed → 202 screened → 181 excluded → 21 full texts assessed
  → 4 excluded → **17 included**.
- AI-assisted route: 32 shortlisted → 3 duplicates of database records → 29 assessed
  → 21 excluded → **8 included** from SE venues.
- **25 studies included** in total (`extraction/extraction_table.csv`).
- Quality: 25 papers, total 118, mean 4.72 (`extraction/quality_scores.csv`).

One record, Rupp et al. (2024), was initially excluded at title/abstract screening
after a reviewer conflict. After further discussion, the reviewers decided to include
it; it was assessed at full text and included. Rayyan was updated on 2026-11-18 to
reflect this decision; the change is recorded in `screening/raw/rayyan_decision_log.csv`.

## Known limitations

- **Google Scholar results change over time.** Re-running the G1 to G7 queries will
  not return the same 30 records per query; the exports in `search/exports/` are the
  record of what was retrieved.
- **The AI-assisted search route is not reproducible byte-for-byte.** It used a
  general web search engine with AI assistance; results and the assistant's output
  vary between runs. The verbatim queries are logged in `ai_search/search_log.csv`
  and the shortlist in `ai_search/candidates.csv`; the exact instruction prompt was not retained
  (see `ai_search/prompt_used.md`).
- **On-topic game-venue papers found by the AI-assisted route were not included.**
  That route targeted software engineering venues (ICSE, ESEC/FSE, ASE, ISSTA, TSE,
  TOSEM), and only those 8 SE-venue papers were included. On-topic papers it surfaced
  from game venues or preprints (group "On topic" in `ai_search/candidates.csv`) were
  not included.
- Exclusion reasons were not logged per record at title/abstract screening, nor for
  the 21 AI-route exclusions; only the 4 full-text exclusions have recorded reasons.
- The database exports contain abstracts; these are redistributed as exported and
  remain © their respective publishers and authors.

## Data availability statement (for the paper)

> The replication package for this review, including search strings, raw database
> exports, the Rayyan export and decision log, per-record screening decisions, the
> agreement script, the AI-assisted search log, the extraction form and completed
> extraction, the quality appraisal, and the derivation of all PRISMA counts, is
> openly available at https://github.com/4dotk/game-testing-slr under CC BY 4.0
> (data) and MIT (code).

## Use of generative AI

Claude (Anthropic) was used during several stages of this review, including identifying candidate papers through targeted web searches, checking data extraction notes against full texts, suggesting extraction entries and preliminary quality assessments, and proposing codes for thematic synthesis. It also suggested edits to the manuscript and assisted with LaTeX formatting and table preparation.

The authors screened all candidate papers, verified the extracted information, made all inclusion and exclusion decisions, finalized quality assessments and synthesis themes, and reviewed all generated outputs. The authors take full responsibility for the accuracy, interpretation, and integrity of this work.

## Citation

Karthikeya Aduri and Shantanu Mande. 2026. Replication package for "Automated Video
Game Testing with Agents and Test Oracles: A Systematic Review and Implications for
PCG". https://github.com/4dotk/game-testing-slr

```bibtex
@misc{aduri2026replication,
  author       = {Aduri, Karthikeya and Mande, Shantanu},
  title        = {Replication Package for "Automated Video Game Testing with Agents and Test Oracles: A Systematic Review and Implications for {PCG}"},
  year         = {2026},
  howpublished = {\url{https://github.com/4dotk/game-testing-slr}}
}
```

## License

Data and documentation: CC BY 4.0. Code: MIT. See `LICENSE`.
