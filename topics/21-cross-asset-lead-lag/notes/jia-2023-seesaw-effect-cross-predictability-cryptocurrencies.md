---
title: "A seesaw effect in the cryptocurrency market: Understanding the return cross predictability of cryptocurrencies"
authors: "Jia, Yuecheng; Wu, Yangru; Yan, Shu; Liu, Yuzheng"
year: 2023
venue: "Journal of Empirical Finance 74, 101428"
url: "https://ideas.repec.org/a/eee/empfin/v74y2023ics0927539823000956.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "minutes"
tags: "cross-predictability, negative-lead-lag, intraday, lasso, machine-learning, large-coins, seesaw"
---

## Key insight
Within the trading day, cryptocurrency returns predict each other with a negative sign: a rise in a large coin tends to be followed by lower returns in other coins, the opposite of the positive lead-lag documented for stocks. Predictive power runs from large coins to the rest, and small coins seldom predict large ones. This contradicts the popular trading heuristic that altcoins follow Bitcoin's last move in the same direction.

## Method
From the abstract only: a study of intraday return cross-predictability among cryptocurrencies, with a trading strategy that uses LASSO (least absolute shrinkage and selection operator) to select cross-coin predictors. The bar length, lags, coin universe, exchanges and sample period are not stated in the abstract and were not confirmed.

## Data and sample
"Major cryptocurrency exchanges", intraday data. Details not confirmed (abstract-only; publisher full text is paywalled and no open working paper was found in this session).

## Reported results
Only what the abstract states:
- A "negative lead-lag effect in the cryptocurrency market", in contrast to the positive effect in equities.
- Large coins negatively predict other coins; small coins rarely predict large ones.
- A LASSO-based trading strategy exploiting the cross-predictability "generates highly significant profits" on major exchanges after realistic transaction costs. No numbers are given in the abstract.

## Signal construction
Implied form: at each intraday bar, regress each coin's next-bar return on the lagged returns of all coins with a LASSO penalty, refit on a rolling window, and trade on the forecast. The paper's finding says the coefficients on large coins' lagged returns are predominantly negative. For a SOL bot the candidate feature is: minus the last-bar return of BTC and ETH (or the LASSO-weighted combination), as a predictor of SOL's next-bar return, after controlling for SOL's own lagged return. Bar length and lag count must be taken from the full text.

## Relevance to SOL perpetuals at minutes to hours
High, because it is intraday and because it makes the opposite prediction to the "BTC leads, alts follow" story. A plausible reading that reconciles it with the other notes: liquid coins incorporate a BTC move within the same bar (Kurihara and Matsumoto), sometimes overshooting, and capital rotation between coins then produces a partial reversal in relative terms. If so, the sign of the cross-asset coefficient on SOL depends on the bar length and on whether SOL's own contemporaneous move is controlled for. The first empirical task for this topic is to estimate that sign on SOL at 1, 5, 15 and 60 minutes.

## Caveats
Abstract-only: no magnitudes, frequency or sample confirmed. A negative cross-coefficient can be produced mechanically by bid-ask bounce and stale quotes in less liquid coins when returns are computed from trade prices, and by short-term reversal in the target that is correlated with the leader's move. Profitability "after realistic transaction costs" could not be checked. The seesaw mechanism (flows rotating between coins) is the authors' label; its details were not read.
