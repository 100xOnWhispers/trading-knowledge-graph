---
title: "Grammatical Evolution-based ensembles for algorithmic trading"
authors: "Martin, Carlos; Quintana, David; Isasi, Pedro"
year: 2019
venue: "Applied Soft Computing 84, 105713"
url: "https://e-archivo.uc3m.es/bitstream/10016/34502/2/grammatical_ASC_2019_ps.pdf"
pdf: "sources/31-rl-evolutionary-second-pass/martin-2019-grammatical-evolution-ensembles-algorithmic-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "daily"
tags: "grammatical-evolution, ensemble, sliding-window, re-optimisation, turnover, transaction-costs, inertia"
---

## Key insight
Re-evolving a trading rule every period and using only the newest rule gives the best gross return and the worst net return, because the rules disagree from one period to the next and the switching generates trades. Keeping the last several rules and changing position only when a supermajority of them agrees ("inertia") recovers most of the adaptivity at a fraction of the turnover. This is the clearest quantified statement in the repository of what periodic re-optimisation costs.

## Method
- Grammatical evolution: an integer genome is decoded through a grammar into a rule built from technical indicators (moving averages, rate of change and others) and comparison and logical operators. The rule outputs 1 (hold the index) or 0 (hold cash at the risk-free rate).
- Fitness: net return over the training window, with a one-way transaction cost of 0.25% per trade inside the fitness function.
- Search: population 500, 50 generations, elitism. One rule takes about 1.2 seconds to evolve on the authors' laptop.
- Six schemes compared, all using a 3-year sliding training window:
  - Static: one rule evolved before the test year and used all year.
  - Naif: a new rule each period, used once.
  - Majority: vote of the `s` most recent rules.
  - Weighted1, Weighted2: votes weighted toward recent rules.
  - Inertia: majority vote, but the position changes only if the share of rules calling for the change reaches an inertia factor (for example 4 of 5).
- Ensemble size and inertia factor were chosen on earlier data (evaluation years to 2012). 30 runs per scheme; Wilcoxon tests on the differences.

## Data and sample
S&P 500 index, daily, 2005 to 2017, with the 3-month Treasury bill rate for cash. Test years 2013, 2014, 2015, 2016 and 2017, each evaluated separately.

## Reported results
Mean annual net return over the five test years (30 runs):
- Inertia 4.77%, Static 2.55%, Majority 2.09%, Weighted1 2.00%, Weighted2 0.17%, Naif -3.96%.
- Inertia was best in three of five years; most differences against Inertia were significant at 1%.
- Gross of costs the order reverses: Naif 7.21%, Majority 6.67%, Static worst at 3.73%.
- Mean trades in 2013: Inertia 4.07, Static 7.20, Naif 14.00.
- Some Static rules gave no buy signal for the whole of 2017 and earned only the risk-free rate.

## Signal construction
Not a signal. A position-change rule for any periodically refitted model: keep the last `s` fitted models; let `v` be the share voting for the opposite of the current position; switch only if `v >= i`, with `i` above one half. Tune `s` and `i` on data before the test period.

## Relevance to SOL perpetuals at minutes to hours
The mechanism is frequency-independent and the authors say so, while noting they did not test intraday. For a SOL bot that refits rules or models daily or weekly, the lesson is to add hysteresis across model generations and to measure the turnover that refitting itself causes. With crypto fees and spreads the gap between Naif and Inertia should be larger, not smaller.

## Caveats
One index, long or cash only, five test years in a rising market. The paper reports no buy-and-hold benchmark, and net returns of 2% to 5% a year were far below what holding the index earned in most of those years (index returns are not in the paper). So the study ranks ensemble schemes against each other; it does not show that grammatical evolution finds useful rules. The cost of 0.25% one-way is high for index futures and makes turnover decisive by construction.
