# Prompt used for the AI-assisted search

The AI-assisted search used Claude (Anthropic) with web search. The exact prompt was not retained; the text below is a reconstruction of its content by the authors and is approximate, not verbatim. The queries it actually ran are logged verbatim in the ‘Search Log S12–S44’ sheet of TSE_PCG_Research_Papers.xlsx. The dates in that log were recorded by the AI assistant and have not been independently verified. All candidate papers were screened and verified by the authors.

## Approximate reconstruction of the prompt

> You are an expert researcher helping me design my Systematic Literature Review (SLR) project. Do not run the full review yourself, but please help me put together the protocol and find a few extra papers.
> Here are my research questions:
>
> * RQ1. What automated methods, frameworks, and tools have been proposed for testing or playtesting procedurally generated games?
> * RQ2. What properties of procedurally generated game content are evaluated by these methods?
> * RQ3. How are existing approaches evaluated and compared, and what constitutes established automated practice versus the current state of the art?
> * RQ4. What limitations and open problems remain in automated testing and playtesting of procedurally generated games?
>
> Based on these RQs, please do the following:
>
> 1. Database Search Queries: Give me Boolean search strings for IEEE Xplore and ACM Digital Library (2015–2026) combining procedural content generation, AI techniques, and game testing/playtesting, plus seven short queries for Google Scholar (where I'll take the top 30 results of each).
> 2. Targeted SE Venue Search: Do a quick search specifically across Software Engineering venues (like ICSE, ASE, FSE, TSE, TOSEM, ISSTA, etc.) for automated game testing/playtesting papers (2015–2026) and give me a list of relevant papers we might have missed so we can screen them.
> 3. Inclusion & Exclusion Criteria: Draft clear criteria for peer-reviewed full papers and surveys (2015–2026, English) that propose an automated method/agent/oracle to test or evaluate games, PCG, or game AI and report on at least one property (bugs, coverage, playability, difficulty, balance)—while excluding generation-only papers, human-only studies, standard game-playing AI not used for testing, manual/scripted testing, theses/short papers, and duplicates.
> 4. Methodology Draft: Write a clean methodology section covering our search, screening (using Rayyan and PRISMA 2020), a 6-item quality assessment (scored 0, 0.5, 1 without excluding papers), and descriptive mapping + thematic synthesis.
