---
title: "Regime-Specific interdependencies in cryptocurrency markets: A high-frequency GMM-VAR approach"
authors: "Joshi, Prashant"
year: 2025
venue: "Data Science in Finance and Economics 5(3), 419-439"
url: "https://www.aimspress.com/aimspress-data/dsfe/2025/3/PDF/DSFE-05-03-017.pdf"
pdf: "sources/01-macro-regime-detection/joshi-2025-regime-specific-interdependencies-crypto-gmm-var.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "crypto"
horizon: "minutes"
tags: "gaussian-mixture, one-minute-data, calm-volatile, lead-lag, btc-transmission, var, spillover"
---

## Key insight
Using one-minute returns for BTC, ETH and Monero over more than five years, a Gaussian mixture splits minutes into a calm and a volatile regime, and the cross-coin dynamics differ between them. In calm minutes each coin's variance is mostly explained by its own shocks; in volatile minutes BTC accounts for a larger share of the other coins' variance. Lagged (Granger) predictability between coins is present in both regimes and is statistically much stronger in the calm one. It is one of the few regime studies at the frequency this bot trades.

## Method
Step 1: fit a Gaussian mixture model to the three-dimensional vector of one-minute returns and assign each minute to a component by posterior probability. No Markov structure is imposed on the sequence of labels. Step 2: estimate a separate VAR(5) on the minutes in each regime, then compute impulse responses over a 20-minute horizon, forecast-error variance decompositions and Granger-causality tests per regime.

## Data and sample
One-minute closing prices for BTC, ETH and XMR, 1 January 2020 to 25 April 2025, from EOD Historical Data. The exchange or price composite behind the series is not stated in the sections I read.

## Reported results
- BIC preferred five mixture components, but two of them were empty and one had near-zero variance; three- and four-component fits were similarly unstable. The author settled on two components on these grounds.
- Volatile-regime covariances are larger than calm-regime ones (reported on different scales: 1e-4 versus 1e-5).
- The monthly share of volatile minutes spikes around the COVID crash, the China mining ban, the TerraUSD and FTX collapses and tariff news.
- Calm regime: BTC's own shocks explain over 95% of its forecast-error variance; BTC explains about 22% of ETH's variance and about 10% of XMR's.
- Volatile regime: BTC explains over 92% of its own variance, nearly 36% of ETH's and about 20% of XMR's; ETH contributes about 5% to BTC and 12% to XMR; XMR is a receiver.
- Granger-causality nulls are rejected at 1% in every direction in both regimes, but the chi-square statistics (5 lags) are far larger in the calm regime (for example BTC to ETH: 32,680 calm versus 46.56 volatile). The author reads this as stress dampening linear lagged predictability. So the variance-share measure says linkage rises in volatile minutes while the lagged-predictability measure says it falls.

## Signal construction
A live adaptation: classify the current minute as calm or volatile using a mixture (or simply a realised-volatility threshold) fitted on trailing data only; keep two sets of lead-lag coefficients from BTC and ETH returns to the target coin, one per regime; apply the set matching the current regime. The paper itself fits the mixture on the full sample, so this online version is untested.

## Relevance to SOL perpetuals at minutes to hours
The result bears directly on using BTC moves on large venues as a leading input for SOL: the weight on that input should be regime-dependent. The direction is ambiguous, though. Shares of variance attributed to BTC rise in volatile minutes, which in an orthogonalised VAR largely reflects same-minute co-movement, while lagged predictability, the part a bot can trade, looks statistically stronger in calm minutes. The share of minutes in each regime is not reported in the sections I read, so the difference in test statistics may partly be sample size. SOL is not in the sample, and Monero is a poor proxy for it. The 20-minute response horizon matches the bot's range.

## Caveats
Full-sample regime assignment, so the labels use future data. With several million observations, every Granger test rejects, which says nothing about economic size. Regime labels come from the return vector itself, so "volatile" minutes are partly defined by large co-movements, which mechanically raises measured linkage. The text has internal inconsistencies in the variance-decomposition shares. No trading test and no costs. Minute-level lead-lag is studied properly in the microstructure topics; this note is here for the regime-conditioning result.
