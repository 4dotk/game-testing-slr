# Eligibility criteria (version 2, as applied)

Applied to both routes: the database search (IEEE Xplore, ACM Digital Library,
Google Scholar) and the targeted search of software engineering venues (ICSE,
ESEC/FSE, ASE, ISSTA, TSE, TOSEM). The database queries were centred on PCG,
but the criteria below were not restricted to PCG.

## Inclusion criteria (all must hold)

| ID | Criterion |
|----|-----------|
| I1 | Peer-reviewed full paper (journal or conference), or a peer-reviewed survey or review. |
| I2 | Written in English, with the full text accessible. |
| I3 | Published 2015 to 2026. |
| I4 | The paper contributes or evaluates an automated method: a playing agent (learning, search, evolutionary, LLM-based, persona-based or scripted) or a test oracle, including test selection and oracle-only methods with no playing agent. |
| I5 | The stated aim is testing, playtesting or evaluating a game, its content (including procedurally generated content) or its game AI. |
| I6 | Reports an evaluation of at least one property (for example bugs, coverage, playability, difficulty, balance) through an experiment, comparison, case study or industrial deployment account. |

Surveys and reviews are exempt from I4 and I6. They are judged on whether they
cover automated game testing or playtesting.

## Exclusion criteria (any one excludes)

| ID | Criterion |
|----|-----------|
| E1 | Generation-only paper: no testing or evaluation component, or an agent or metric used only as an incidental check. |
| E2 | Evaluated only with human players or participants (human-only playtesting, surveys, user studies). |
| E3 | Game-playing agents built to play well, not used for testing or evaluation. |
| E4 | Purely manual testing, or fixed test scripts with no agent or oracle contribution. |
| E5 | Not a full peer-reviewed paper: theses, doctoral or research plans, position papers, abstracts, posters, slides, blogs. |
| E6 | Duplicate, or an earlier version of an extended paper (the extended paper is kept). |

## Clarifications

- Scripted or rule-based agents are eligible when they are the testing or
  evaluation agent inside an automated method (for example the scripted
  players that provide the balance signal in P29). They are not eligible as
  plain hand-written test scripts (E4).
- Non-AI methods are eligible if they meet I4 and I5 (for example metamorphic
  or asset-based oracles and graph-based regression selection).
- When a paper has an extended version, keep the extended one (E6).
- "Maybe" decisions at title and abstract screening were treated as includes
  and resolved at full-text assessment.

## Mapping of the full-text exclusions in the PRISMA diagram

| Paper | Reason | Code |
|-------|--------|------|
| P09 | Doctoral or research plan | E5 |
| P14 | Thesis | E5 |
| P16 | Human survey only | E2 |
| P19 | No automated method (position paper) | I4 |

The PRISMA figure uses the labels EC and IC for E and I (EC5 = E5, EC2 = E2, IC4 = I4).

## Change note

Version 1 of this file (I1 to I8, E1 to E10) required a PCG subject (I4, I6),
an AI-based tester (I5), and excluded general game or GUI testing (E2) and
non-AI testers (E10). That version does not describe the papers that were
included. Version 2 replaces it, and the broader scope matches the AI-assisted
search prompt and the criteria stated in the paper.
