# Search strings

All searches were run in October 2026 and limited to publications from 2015 to 2026.

## IEEE Xplore (Command Search, All Metadata)

```
("All Metadata":"procedural content generation" OR "All Metadata":"procedural generation" OR "All Metadata":"procedurally generated" OR "All Metadata":PCGML OR "All Metadata":"level generation" OR "All Metadata":"level generator" OR "All Metadata":"generated levels")
AND ("All Metadata":"reinforcement learning" OR "All Metadata":"deep learning" OR "All Metadata":"machine learning" OR "All Metadata":"neural network" OR "All Metadata":"large language model" OR "All Metadata":LLM OR "All Metadata":"AI agent" OR "All Metadata":"intelligent agent" OR "All Metadata":"player model" OR "All Metadata":"procedural persona" OR "All Metadata":"automated agent")
AND ("All Metadata":playtesting OR "All Metadata":playtest OR "All Metadata":"game testing" OR "All Metadata":"automated testing" OR "All Metadata":"automated evaluation" OR "All Metadata":"quality assurance" OR "All Metadata":"bug detection" OR "All Metadata":playability OR "All Metadata":solvability OR "All Metadata":"testing agent")
AND ("All Metadata":game OR "All Metadata":games)
```

Records exported: 25 (`database_exports/ieee_xplore.bib`).

## ACM Digital Library (Advanced Search, ACM Full-Text Collection)

```
[[Abstract: "procedural content generation"] OR [Abstract: "procedural generation"] OR [Abstract: "procedurally generated"] OR [Abstract: PCGML] OR [Abstract: "level generation"] OR [Abstract: "generated levels"] OR [Title: "procedural generation"] OR [Title: "procedural content generation"]]
AND [[Abstract: "reinforcement learning"] OR [Abstract: "deep learning"] OR [Abstract: "machine learning"] OR [Abstract: "neural network"] OR [Abstract: "large language model"] OR [Abstract: LLM] OR [Abstract: "AI agent"] OR [Abstract: "intelligent agent"] OR [Abstract: "player model"] OR [Abstract: "automated agent"]]
AND [[Abstract: playtest*] OR [Abstract: "game testing"] OR [Abstract: "automated testing"] OR [Abstract: "automated evaluation"] OR [Abstract: playability] OR [Abstract: solvability] OR [Abstract: "testing agent"] OR [Abstract: "quality assurance"]]
```

Records exported: 16 (`database_exports/acm_dl.bib`).

## Google Scholar (seven queries, first 30 results of each, ranked by relevance)

| ID | Query | Export file |
|----|-------|-------------|
| G1 | `"procedural content generation" playtesting agent` | google_scholar_G1.bib |
| G2 | `"procedurally generated" levels "reinforcement learning" "automated testing" OR playtesting` | google_scholar_G2.bib |
| G3 | `"procedural content generation" "large language model" OR LLM OR VLM testing agent` | google_scholar_G3.bib |
| G4 | `"generated levels" playability OR solvability "deep learning" OR "reinforcement learning"` | google_scholar_G4.bib |
| G5 | `"game testing" "procedural generation" bugs agents` | google_scholar_G5.bib |
| G6 | `"procedural content generation" "player model" OR "procedural persona" evaluation` | google_scholar_G6.bib |
| G7 | `"procedural content generation" survey OR review automated testing OR playtesting` | google_scholar_G7.bib |

Records exported: 211 (G2 contains one entry that is a saved results page, not a paper).

## Totals

252 records in total; 50 duplicates removed; 202 records screened in Rayyan.

## Targeted search of software engineering venues

A general web search engine, with AI assistance, was used to find candidate
papers from ICSE, ESEC/FSE, ASE, ISSTA, TSE and TOSEM. Each candidate's venue and
metadata were checked against the publisher's page. The queries and decisions
are logged in `targeted_search/targeted_search_log.xlsx`. Eight papers were included.
