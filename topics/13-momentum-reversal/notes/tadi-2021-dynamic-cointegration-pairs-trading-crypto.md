---
title: "Evaluation of Dynamic Cointegration-Based Pairs Trading Strategy in the Cryptocurrency Market"
authors: "Tadi, Masood; Kortchemski, Irina"
year: 2021
venue: "arXiv preprint 2109.10662"
url: "https://arxiv.org/pdf/2109.10662v1"
pdf: "sources/13-momentum-reversal/tadi-2021-dynamic-cointegration-pairs-trading-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "minutes"
tags: "pairs-trading, cointegration, ornstein-uhlenbeck, half-life, bitmex, perpetuals"
---

## Key insight
A cointegration pairs strategy on BitMEX perpetual and futures contracts, re-selected weekly and traded on minute bars, shows very high back-tested returns. The useful contribution is procedural: the half-life of the spread's Ornstein-Uhlenbeck fit is used both to choose the pair and to set the z-score look-back window. A material share of reported profit comes from maker rebates, which is a warning about how such back-tests should be read.

## Method
Weekly cycle. In the formation period (three months of minute-binned closes), candidate pairs are tested for cointegration with the Engle-Granger procedure using ADF or the nonlinear Kapetanios-Snell-Shin test, or the Johansen test for baskets. The spread is fitted as an Ornstein-Uhlenbeck process and the half-life computed; the cointegrated combination with the shortest half-life is chosen. The z-score of the spread uses a rolling mean and standard deviation whose window is derived from the half-life (treated as the half-life of an exponential moving average and converted to an equivalent simple-moving-average length). Entry when the z-score diverges by two standard deviations; exit when it falls back below one. Three scenarios: one pair per week; a Johansen basket of all coins; fixed pairs with a one-day window.

## Data and sample
BitMEX minute-binned data, 27 September 2018 to 2 October 2019; thirty-nine trading weeks. Contracts are denominated in Bitcoin. Fees modelled: maker -0.025% (a rebate), taker 0.075%; funding every 8 hours is described.

## Reported results
- Scenario 1: average monthly return 17.3% (ADF selection) and 13.9% (KSS selection); about 90% of months positive; maximum drawdown about 0.15 XBT on roughly 1 XBT of capital.
- Commission rebates make up 35% and 26% of total profit under ADF and KSS.
- Reported Sharpe ratios: 6.96 and 6.57 for scenario 1, and 7.94 for the basket scenario.
- The nonlinear KSS test did not improve profitability over ADF.

## Signal construction
Rolling regression of log(SOL) on log(BTC) or a basket gives the spread S. Fit `dS = theta*(mu - S)dt + sigma*dW`; half-life = ln(2)/theta. Set the z-score window from the half-life, compute z = (S - mean)/std, act at |z| > 2, stand down at |z| < 1. Re-estimate weekly. Skip periods when the cointegration test fails or the half-life is long relative to the intended holding time.

## Relevance to SOL perpetuals at minutes to hours
One of the few papers that works with perpetual contracts and 8-hour funding at minute frequency, which matches the reference instrument's structure. The half-life-driven window is a sensible way to avoid a hand-picked look-back. The half-life itself is a direct estimate of the horizon at which SOL's relative mispricing reverts, which is the quantity the bot needs.

## Caveats
Grade C. Sharpe ratios near 7 on one year of data, with assumed maker fills at the limit price and rebates supplying a quarter to a third of profit, are not credible as live expectations. No queue or adverse-selection modelling. Bitcoin-denominated profit and loss. Kalshi's fee schedule is unlikely to pay maker rebates of this kind, and BitMEX's 2018 to 2019 altcoin contracts were thin. Not peer-reviewed in the version read.
