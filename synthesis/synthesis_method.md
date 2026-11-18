# Synthesis method

The review is reported following PRISMA 2020. The 25 included papers were
synthesised in two stages, both qualitative/descriptive; no meta-analysis was
performed.

## Stage 1: Descriptive mapping

The included papers were mapped by year and venue, game genre, AI technique, primary
goal, evaluation metrics and validation approach, using the categorical columns of
the extraction log (`../extraction/extraction_log.csv`).

## Stage 2: Thematic synthesis (Thomas and Harden, 2008)

1. **Familiarisation.** Each reviewer read the other's extraction rows, so that both
   knew all included papers.
2. **Coding.** The "Key results" and "Stated limitations" text of each paper was coded
   line by line with short codes (for example persona diversity, sparse reward,
   human-likeness gap). Candidate codes were proposed with AI assistance and
   finalised by the authors.
3. **Descriptive themes.** Similar codes were grouped into themes.
4. **Analytical themes.** Themes were mapped to the research questions RQ1 to RQ4,
   noting agreements, contradictions and gaps. Each theme is supported by at least
   two papers.

The resulting themes are:

| Theme | Name | Papers |
|-------|------|-------:|
| T1 | Coverage used as a proxy for bugs | 6 |
| T2 | Human-likeness gap | 12 |
| T3 | PCG transfer proposed but untested | 8 |

The paper-by-theme assignments are in `synthesis_matrix.csv`.

## Consistency

The same extraction form was used for every paper, with a pilot on four papers
extracted by both reviewers, cross-checking of each other's extractions and one
shared codebook (`../extraction/codebook.md`). Disagreements were resolved by
discussion. Quality scores describe the strength of evidence and were not used to
exclude papers.
