---
title: "A Comprehensive Look at Bitcoin Return Predictability (Chapter 1 of Three Essays on Predictability, Hedging, and Financial Contagion in the Crypto Market)"
authors: "Sanhueza Herrera, Aliro Joel"
year: 2026
venue: "Doctoral dissertation, Universidad Diego Portales, Santiago (advisors Nicolas Magner and Nicolas Hardy)"
url: "https://doctorados.udp.cl/cms/wp-content/uploads/2026/06/Tesis_Doctoral_Aliro_Sanhueza.pdf"
pdf: "sources/30-macro-state-intraday-transmission/sanhueza-2026-bitcoin-return-predictability-comprehensive.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "30-macro-state-intraday-transmission"
asset_class: "crypto"
horizon: "daily"
tags: "out-of-sample, predictor-zoo, macro-predictors, clark-west, bitcoin, technical-indicators, negative-result"
---

## Key insight
A Welch-and-Goyal style audit of 141 candidate predictors of Bitcoin returns finds that most in-sample predictability does not survive out of sample, and macro variables fare worst. Of 67 predictors significant in sample, 29 help out of sample at one horizon or more and 4 beat the benchmark at all horizons. Trend-based technical indicators carry most of the robust signal; macroeconomic and on-chain variables help only episodically; sentiment is weakest.

## Method
Two stages. In-sample predictive regressions of the h-day log return (h = 1, 7, 14, 28) on each lagged predictor, with Newey-West errors. Predictors significant at any horizon go to out-of-sample tests against two nested benchmarks, a random walk specification (a driftless version was set aside as uncompetitive) and an AR(1), under both recursive and rolling estimation and several evaluation windows, using out-of-sample R-squared and the Clark-West test. Category factors are built by principal components. Economic value is assessed with two trading exercises, one of them a mean-variance allocation between Bitcoin and the risk-free asset with weight restricted to [0, 1] (risk aversion 6, 28-day rolling variance), net of a proportional cost of 0.01 percent, reporting annualised returns and Sharpe ratios against buy-and-hold.

## Data and sample
Daily Bitcoin returns, September 2014 to April 2025: 3,854 observations for seven-day-a-week series, 2,749 for market-hours series. 141 predictors in four categories: technical, fundamental (on-chain, CoinMetrics), sentiment, and macroeconomic (ten currencies, global equity indices, fixed income and others from LSEG Datastream). Spans pre- and post-2020. Bitcoin only; no altcoins or SOL. For macro series the Monday forecast uses Friday's data.

## Reported results
- In sample, 155 of 564 predictor-horizon exercises (27 percent) are significant: 37 percent of technical, 17.1 percent of fundamental, 16.5 percent of macroeconomic, 15.6 percent of sentiment. Within macro, 38 percent of fixed-income exercises are significant against 15 percent for global equity indices.
- Average in-sample R-squared: 0.13 percent at 1 day, 0.2 at 7, 0.78 at 14, 0.82 at 28.
- Out of sample against the random-walk-type benchmark: 32.2 percent of technical exercises show significant gains, 16.7 percent of fundamental, 18.8 percent of sentiment and 5.6 percent of macroeconomic.
- Among macro variables the Shanghai Composite stands out at longer horizons (in-sample R-squared 0.96 percent at 14 days).
- In trading exercises the Nasdaq Composite and a medium-term Treasury ETF (IEI) raise the Sharpe ratio by about 0.2; trend indicators (ADX, slow EMA) consistently beat buy-and-hold and AR(1).
- Macro and fundamental variables show episodic, horizon-dependent value; gains are often confined to subsamples.

## Signal construction
Not a signal; it is evidence about which inputs deserve a place. The template to copy is the test battery: require a candidate macro state variable to (1) be significant in sample, (2) deliver positive out-of-sample R-squared with a Clark-West rejection under both rolling and recursive schemes, and (3) add economic value after costs, before it is admitted as a feature.

## Relevance to SOL perpetuals at minutes to hours
The 5.6 percent out-of-sample hit rate for macro predictors is the strongest caution in this topic against using lagged macro levels or returns as directional predictors of crypto. It is consistent with macro acting as a contemporaneous driver and a regime descriptor, which is how the other notes use it. The study is daily and Bitcoin-only; it does not test announcement surprises, intraday lead-lag or interaction effects (macro state conditioning another signal), which remain open.

## Caveats
A dissertation chapter, not yet peer reviewed as far as could be confirmed. With 564 exercises some out-of-sample successes are expected by chance; no multiple-testing correction was seen. Trading cost of 0.01 percent is low for most venues. Liquidity aggregates (central bank balance sheet, stablecoin supply) were not seen among the listed macro predictors.
