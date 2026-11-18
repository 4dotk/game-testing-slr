# Eligibility criteria

Both reviewers applied these criteria during title/abstract screening (in Rayyan)
and full-text assessment. A record had to meet all inclusion criteria and none of
the exclusion criteria.

Exclusion reasons were not logged per record at title/abstract screening. Reasons
were recorded only for the 4 papers excluded at full text (see
`../extraction/fulltext_decisions.csv`).

## Inclusion criteria

| ID | Criterion |
|----|-----------|
| I1 | Peer-reviewed journal or conference paper (full paper), or a peer-reviewed survey/review |
| I2 | Written in English; full text accessible |
| I3 | Published 2015 to 2026 |
| I4 | Subject is content or generators that are procedurally generated (algorithmic, ML-based or PCGML) in games |
| I5 | The testing/playtesting method is AI-based: it uses RL, supervised/deep learning, learned player models, neural networks, LLMs or VLMs (see the borderline rule below) |
| I6 | The method tests, playtests, validates or evaluates the generated content or generator, and this is a stated aim or contribution (in the abstract, objectives or contributions) |
| I7 | At least one identifiable property of the content or generator is evaluated (playability, solvability, difficulty, diversity, bugs, balance, etc.) |
| I8 | Reports some evaluation (experiment, case study or comparison). Surveys are exempt from I7 and I8 and are judged on whether they cover automated testing of PCG |

**Borderline rule (I5):** Testers built on search or evolution without learning (for example MCTS, A* or genetic algorithms) were labelled BORDERLINE at title/abstract screening and decided at full-text stage.

## Exclusion criteria

| ID | Criterion |
|----|-----------|
| E1 | Generator paper where an agent or metric is only an incidental sanity check (fails I6) |
| E2 | Testing of hand-authored games or levels, or general game/GUI testing, with no PCG application |
| E3 | Human-only playtesting or user studies as the sole evaluation (human data used as ground truth for an automated method is fine) |
| E4 | Generation-only paper with no testing or evaluation component |
| E5 | Testing of engines, rendering or performance unrelated to generated content |
| E6 | Procedural environments used only as RL training or generalization benchmarks, where the content itself is not tested |
| E7 | Non-peer-reviewed: theses, blogs, slides, posters, abstract-only, keynotes |
| E8 | Duplicate or earlier version of an extended paper (keep the extended one) |
| E9 | The generated content is LLM-generated (e.g. LLM-written quests or levels), even if automated evaluation is present |
| E10 | The tester is not AI-based (pure constraint solver, hand-written heuristic bot, plain metric script) |
