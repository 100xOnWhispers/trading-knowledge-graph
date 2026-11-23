---
title: "On the Intraday Behavior of Bitcoin"
authors: "De Nicola, Giacomo"
year: 2021
venue: "Ledger, Vol. 6, 58-80"
url: "https://ledger.pitt.edu/ojs/ledger/article/download/213/212/1232"
pdf: "sources/28-shock-response-price-pressure/denicola-2021-intraday-behavior-bitcoin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "hours"
tags: "reversal, jumps, autocorrelation, conditional-on-move-size, bitcoin, liquidation-cascade-hypothesis"
---

## Key insight
Bitcoin returns on Bitstamp show significant negative first-order autocorrelation not only at one to five minutes, where bid-ask bounce is expected, but at one, two and four hours. The reversal gets stronger as the preceding move gets larger: after a two-hour move of six standard deviations the correlation with the next two-hour return is -0.40. This is the most direct evidence found on the bot's core question, and its sign is reversal.

## Method
Compute log returns from one-minute closes at 1, 5, 15 and 30 minutes, 1, 2 and 4 hours and 1 day. Report first-order autocorrelation at each. Then condition on move size: keep only bars whose absolute return exceeds a multiple k of the standard deviation of that bar size (k from 0 to 6), and correlate those returns with the returns of the bar that follows. A simple strategy is applied in sample: after a bar return larger than the threshold, take the opposite position for exactly one bar. Thresholds and bar sizes were fixed in advance without optimization. A 10,000-run random long/short strategy is the benchmark.

## Data and sample
BTC/USD on Bitstamp (spot, no leverage), one-minute bars from a public Kaggle data set, 1 March 2015 to 27 June 2018.

## Reported results
- First-order autocorrelation: -0.1445 (1 min), -0.1016 (5 min), -0.0575 (15 min), -0.0440 (30 min), -0.0557 (1 hour), -0.0858 (2 hours), -0.0564 (4 hours), all significant; -0.0071 (1 day), not significant. Higher-order autocorrelations are insignificant.
- Conditional on move size (only significant values are printed): at 1 hour the correlation goes from -0.056 (all bars) to -0.098 (2 sigma), -0.148 (4 sigma) and -0.186 (5 sigma). At 2 hours: -0.086, -0.165, -0.231, -0.331 and -0.401 at 6 sigma. At 5 minutes: -0.103 to -0.219 at 6 sigma. At 1 minute the relation weakens with size (-0.200 at 1 sigma to -0.045 at 6 sigma). At 4 hours no significant value is printed at 3, 5 or 6 sigma.
- Mean profit per trade of the fade strategy, before fees: at 2 hours 0.05% (every bar), 0.30% (2 sigma), 0.74% (4 sigma), 1.81% (6 sigma); at 1 hour 0.03%, 0.15%, 0.34%, 0.58%; at 5 minutes 0.02% to 0.30%. At 4 hours and 5 sigma the mean is negative (-0.17%).
- Trading every two-hour bar, uncompounded, multiplies capital by more than 8 over the sample before fees; none of 10,000 random strategies reached 8.5.
- Negative intraday returns are slightly larger than positive ones (5 minutes: 0.184% against 0.176%).
- Scope record: horizon 5 minutes to 4 hours; conditioning variable size of the preceding bar return; sign reversal, stronger for larger moves; costs not charged in any table. The author observes that taker fees below 0.1% per trade would leave the larger-threshold trades viable and would erase the small-bar ones.

## Signal construction
At each bar close compute `z = r / sigma`, with `sigma` the standard deviation of returns at that bar size (the paper uses the full-sample value; a live version needs a trailing or volatility-model estimate). If `|z|` exceeds a threshold, expected next-bar return is `-rho(z) * r`, with `rho` rising in `|z|`. Bars of 1 and 2 hours gave the cleanest results. Exit after one bar.

## Relevance to SOL perpetuals at minutes to hours
The horizons match the bot exactly, and the author attributes the effect to overreaction and to liquidation cascades transmitted from leveraged venues to spot, which is the mechanism of interest. It must be re-tested before use: the data end in mid-2018, cover one spot venue and one asset, use a full-sample sigma (a mild look-ahead), and include no spread or fee. Kitron and Wengrowicz (2026) in topic 08 is the recent cross-market measurement of the same short-horizon reversal and should be read alongside. The paper itself calls for a comparison between leveraged and unleveraged venues, which is a natural test on SOL: perp versus spot.

## Caveats
In-sample only, no costs, one exchange. Close prices, not mids, so part of the 1- and 5-minute effect is bounce. Per-trade profit at 6 sigma rests on few observations. The author expects the inefficiency to fade as the market matures.
