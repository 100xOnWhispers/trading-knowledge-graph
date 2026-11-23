---
title: "Is Technical Analysis in the Foreign Exchange Market Profitable? A Genetic Programming Approach"
authors: "Neely, Christopher; Weller, Paul; Dittmar, Robert"
year: 1997
venue: "Journal of Financial and Quantitative Analysis, December 1997 (Federal Reserve Bank of St. Louis Working Paper 1996-006C read)"
url: "https://s3.amazonaws.com/real.stlouisfed.org/wp/1996/96-006.pdf"
pdf: "sources/13-momentum-reversal/neely-1997-genetic-programming-technical-rules-fx.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "fx"
horizon: "multi-day"
tags: "evolutionary-algorithms, genetic-programming, trading-rules, out-of-sample, trend-following, fx"
---

## Key insight
Genetic programming, an evolutionary search over tree-structured trading rules, found rules on 1975 to 1980 exchange-rate data that earned economically significant excess returns over the following fifteen years, after transaction costs, in all six currency pairs tested. Because the rules were fixed before the test period, the usual objection that technical rules are picked with hindsight does not apply. The evolved rules behave like trend-following rules that trade infrequently.

## Method
Rules are trees built from arithmetic functions of past prices (average, max, min and lag over a window, plus, minus, times, divide), Boolean operators (and, or, not, greater than, less than) and constants. A population of random rules is evolved by selecting parents with probability weighted towards higher fitness and applying crossover (swapping subtrees between parents). Fitness is excess return over a training period (1975 to 1977); the best rule of each generation is checked on a separate selection period (1978 to 1980) and kept only if it improves there, which limits overfitting. One hundred rules per currency are generated from independent runs. Validation is 1981 to 1995. One-way transaction cost is set to 0.1% during training and selection, deliberately high to bias the search towards low-turnover rules, and 0.05% in validation. Rules are also combined by uniform weighting and by majority vote. Bootstrapping against random-walk, ARMA and ARMA-GARCH models tests whether standard statistical models can generate the profits.

## Data and sample
Daily data for six exchange rates (dollar against mark, yen, pound and Swiss franc, plus mark/yen and pound/Swiss franc), 1975 to 1995.

## Reported results
- Mean annual out-of-sample excess return across 100 rules: 6.05% for dollar/mark and 4.10% for mark/yen; positive for all six; 2.87% on average.
- All but four of the dollar/mark rules were profitable; the weakest pair still had 89% of rules profitable.
- A majority-vote portfolio rule raised the cross-currency average to 3.67%.
- When the dollar/mark rules were used to determine trades in the other markets, performance improved significantly in all cases except mark/yen.
- Betas against benchmark portfolios give no evidence the returns are compensation for systematic risk; bootstraps indicate the rules detect patterns not captured by standard models.
- A companion paper reports trading frequencies from once every two weeks to once every three months.

## Signal construction
Offline: evolve rule trees over price-derived primitives with a three-way split (train, select, validate) and an inflated cost during search. Online: evaluate the frozen rule set each bar and take the majority vote as the position. Parameters: primitive set, population and generations, cost penalty, number of independent runs.

## Relevance to SOL perpetuals at minutes to hours
This is the methodological anchor for any evolutionary search over SOL trading rules: a selection period distinct from training, an inflated cost in the fitness function, many independent runs, and voting ensembles. The cross-market transfer result suggests evolving rules on BTC and ETH data and validating on SOL. The evidence is for slow rules on daily data; the same authors' intraday study found no profit after costs (see the 2001 note).

## Caveats
Daily FX in 1981 to 1995, a period of large managed-float trends and central bank intervention. Later literature generally finds technical trading profits in major currencies declined after the early 1990s; that decline was not examined in this session. One hundred rules per pair are highly correlated, so the "89% profitable" figures are not independent tests.
