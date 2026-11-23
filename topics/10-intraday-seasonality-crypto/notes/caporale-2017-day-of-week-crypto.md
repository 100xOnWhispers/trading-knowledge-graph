---
title: "The Day of the Week Effect in the Crypto Currency Market"
authors: "Caporale, Guglielmo Maria; Plastun, Alex"
year: 2017
venue: "CESifo Working Paper No. 6716 (later published in Finance Research Letters)"
url: "https://www.cesifo.org/DocDL/cesifo1_wp6716.pdf"
pdf: "sources/10-intraday-seasonality-crypto/caporale-2017-day-of-week-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "daily"
tags: "day-of-week, monday-effect, bitcoin, litecoin, ripple, dash, trading-simulation"
---

## Key insight
The origin of the "Bitcoin Monday effect". Among four coins, only Bitcoin shows a day-of-week anomaly: Monday returns are higher than on other days in 2013 to 2017. A long-on-Monday rule is profitable over the full sample, but in most single years its profit is not statistically different from random trading, so the authors do not claim the market as a whole is inefficient.

## Method
Daily close-to-close percentage returns. Five tests for differences across weekdays: comparison of averages, Student's t-test, ANOVA, the Kruskal-Wallis test, and an OLS regression on weekday dummies, R_t = a_0 + sum of a_n D_nt + e_t. Where an anomaly appears, a trading "robot" in MetaTrader (MQL4) simulates the rule, and a t-test compares average profit per trade with zero (the expected profit of random trading without costs).

## Data and sample
Daily data from CoinMarketCap for Bitcoin, Litecoin, Ripple and Dash, 2013 to 2017 (each from its first available date).

## Reported results
- Bitcoin shows the anomaly on all five tests; Litecoin, Ripple and Dash do not show it consistently.
- For Bitcoin the anomalous day is Monday (flagged by all five methods). Other weekdays are flagged by at most two methods (the per-day table did not extract cleanly from the PDF, so the exact counts are not confirmed).
- Strategy "open long on Monday, close at the end of the day": full sample 245 trades, 60% profitable, t = 2.01 against a critical value of 1.78 (null of no difference from random rejected).
- By year, share of profitable trades: 75% (2013), 39% (2014), 60% (2015), 59% (2016), 71% (2017). The null is rejected only in 2015 (t = 1.96); in 2013, 2014, 2016 and 2017 it is not.
- 2017 contributes 11,662 of the 16,990 total profit (in the simulator's units).

## Signal construction
A day-of-week dummy for the UTC day (Monday = 1). As a rule: long from Monday 00:00 UTC to Monday 24:00 UTC. In a model: include weekday as a categorical feature with heavy regularisation and monitor its coefficient on a rolling window.

## Relevance to SOL perpetuals at minutes to hours
Low. It is a daily-bar effect in one coin from a period when Bitcoin rose strongly on most days, and later studies with GARCH controls (Kinateder note) and multi-exchange data (Baur note) do not find a robust Monday return effect. The useful residue is the idea that the Sunday-to-Monday transition is special: CME reopening and the start of the Asian week concentrate repricing there (the Hansen note finds the first UTC hour is especially volatile on Mondays). That is a volatility timing cue, not a direction cue.

## Caveats
Four coins, about 250 Mondays, no transaction costs, no adjustment for volatility clustering or fat tails in the dummy regression, and multiple testing across five weekdays and four coins. Profit is in price units and dominated by 2017. The abstract of this working-paper version reads more strongly ("evidence against efficiency") than the paper's own conclusion.
