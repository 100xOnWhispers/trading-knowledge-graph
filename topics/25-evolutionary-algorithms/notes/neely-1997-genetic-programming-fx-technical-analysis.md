---
title: "Is Technical Analysis in the Foreign Exchange Market Profitable? A Genetic Programming Approach"
authors: "Neely, Christopher; Weller, Paul; Dittmar, Robert"
year: 1997
venue: "Journal of Financial and Quantitative Analysis, December 1997 (read: Federal Reserve Bank of St. Louis Working Paper 1996-006C)"
url: "https://files.stlouisfed.org/files/htdocs/wp/1996/96-006.pdf"
pdf: "sources/25-evolutionary-algorithms/neely-1997-genetic-programming-fx-technical-analysis.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "25-evolutionary-algorithms"
asset_class: "fx"
horizon: "daily"
tags: "genetic-programming, fx, out-of-sample, rule-ensembles, transaction-costs, overfitting, decay"
---

## Key insight
Genetic programming trained on 1975 to 1980 found long/short currency rules that earned positive excess returns after costs over a 15-year out-of-sample period in all six exchange rates tested. Two design lessons outlast the result: the single best rule in the selection period was one of the worst out of sample, while an equal-weighted or majority-vote ensemble of 100 independently evolved rules was reliable; and raising the cost charged during training steered the search away from high-turnover rules that overfit.

## Method
Rules are trees over `plus, minus, times, divide, norm, average, max, min, lag`, boolean operators, `if-then(-else)` and constants, capped at 100 nodes and 10 levels. Output is +1 (long foreign currency) or -1 (short). Fitness is cumulative log excess return including the overnight interest differential:

r = sum_t z_t r_t + n ln((1 - c)/(1 + c))

with n the number of round trips and c the one-way cost. Each trial: 500 random rules; rank on the training period; build each new generation by fitness-weighted crossover (no mutation); test the top training rule on a selection period and keep it only if it improves; stop after 50 generations or 25 without improvement. A rule with negative selection-period return is discarded. Prices are divided by their 250-day moving average. Cost is c = 0.1% during training and selection, deliberately above the 0.05% used in the test, to penalize frequent trading.

## Data and sample
Daily $/DM, $/yen, $/pound, $/Swiss franc, and DM/yen and pound/Swiss franc cross rates, 1974 to October 1995, with BIS overnight rates. Training 1975 to 1977, selection 1978 to 1980, test 1981 to 1995. 100 rules per currency.

## Reported results
- Mean annual excess return across the 100 rules: 6.05% for $/DM, 4.10% for DM/yen, positive for all six, 2.87% on average.
- A majority-vote rule over the 100 rules raised the cross-currency average to 3.67%.
- All but four $/DM rules were profitable out of sample. The rule ranked first in the selection period was one of those four.
- Trading frequency differed widely: about 30 trades a year for DM/yen, under four for pound/Swiss franc; the mean $/DM rule traded seven times a year.
- "Rogue" rules that trade very often perform poorly beyond what costs explain.
- Betas against benchmark portfolios do not explain the returns; bootstrap tests reject random-walk, ARMA and ARMA-GARCH nulls for $/DM.

## Signal construction
Not a signal. A recipe for search: (1) run many independent evolutions, (2) aggregate their outputs by vote or equal weight rather than picking a winner, (3) charge more than the real cost inside the fitness function, (4) normalize inputs so constants stay stationary.

## Relevance to SOL perpetuals at minutes to hours
The ensemble and inflated-cost tricks are cheap to adopt for any evolved SOL rule set, and the funding rate plays the role of the interest differential in the fitness formula. The profits themselves do not transfer: these are slow trend rules on 1980s currencies. The same authors' intraday study, summarized in `../../11-intraday-seasonality-tradfi/notes/neely-2003-intraday-technical-trading-fx-genetic.md`, found no profit after costs at half-hour frequency.

## Caveats
The follow-up by Neely, Weller and Ulrich (St. Louis Fed WP 2006-046B, which I opened; see `../../16-oscillators-technical-rules/notes/neely-2009-adaptive-markets-foreign-exchange.md`) re-ran these exact rules on October 1995 to June 2005. Net annual returns of the equal-weighted portfolios were 4.68% for DEM/USD, 0.40% JPY/USD, 1.44% GBP/USD, -2.48% CHF/USD, -1.13% DEM/JPY and -2.03% GBP/CHF, and only 8 of 100 GBP/CHF rules stayed profitable. The edge decayed, though structural-break tests could not date the change. One training window; daily data only.
