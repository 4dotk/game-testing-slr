# Replication package

**Automated Video Game Testing with Agents and Test Oracles: A Systematic Review and Implications for PCG**

## Contents

| Path | What it contains |
|------|------------------|
| `search_strings.md` | Full search strings for IEEE Xplore, ACM Digital Library and Google Scholar, with record counts |
| `database_exports/` | The 252 records exported from the three databases (BibTeX), one file per search |
| `targeted_search/targeted_search_log.xlsx` | Log of the targeted search of software engineering venues |
| `extraction/extraction_form.tsv` | Data extraction form for all 29 full texts assessed (25 included, 4 excluded), with quality scores |
| `scripts/kappa.py` | Computes Cohen's kappa and percentage agreement from a Rayyan export |

## Selection flow

252 records identified → 50 duplicates removed → 202 screened → 181 excluded →
21 full texts assessed → 4 excluded → 17 included from databases, plus 8 from
the targeted search → **25 included papers**.

## Reproducing the agreement statistics

```
python3 scripts/kappa.py rayyan_export.csv
```

The script reads each reviewer's decision from the `notes` column of a Rayyan
CSV export. Run `python3 scripts/kappa.py -h` for other options.
