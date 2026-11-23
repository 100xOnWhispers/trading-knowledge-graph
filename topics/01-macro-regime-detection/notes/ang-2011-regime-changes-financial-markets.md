---
title: "Regime Changes and Financial Markets"
authors: "Ang, Andrew; Timmermann, Allan"
year: 2011
venue: "NBER Working Paper 17182"
url: "https://www.nber.org/system/files/working_papers/w17182/w17182.pdf"
pdf: "sources/01-macro-regime-detection/ang-2011-regime-changes-financial-markets.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "multi"
horizon: "multi-day"
tags: "markov-switching, survey, volatility-regimes, bull-bear, asset-allocation, real-time-filtering"
---

## Key insight
The standard survey of regime switching in finance. Its most useful empirical point for a trader is that regimes estimated on equity, rate and currency returns are separated by volatility, not by mean return: the hypothesis of equal means across regimes cannot be rejected, while equal volatilities are strongly rejected. It also shows why real-time tracking is hard: filtered probabilities miss some true switches and raise false alarms even when the model is correctly specified.

## Method
Review plus illustrative estimation. Canonical model: `y_t = mu_{s_t} + phi_{s_t}*y_{t-1} + sigma_{s_t}*eps_t` with a first-order Markov chain for `s_t`. The paper derives the moments of a two-state mixture (showing how regimes produce skewness, fat tails, volatility clustering and correlations that rise in downturns), solves an equilibrium asset-pricing model with regime-dependent dividend growth, and surveys applications to equities, rates, currencies and asset allocation (including Ang and Bekaert 2002, 2004 and Guidolin and Timmermann 2007, 2008).

## Data and sample
Illustrative two-regime estimates on monthly data, by maximum likelihood: S&P 500 excess returns and three-month T-bill yields over 1953:01 to 2010:12, and USD/Deutschmark-euro excess currency returns over 1975:01 to 2010:12.

## Reported results
- Equity excess returns (monthly, percent): high-volatility regime mean 0.33, sigma 4.89; low-volatility regime mean 0.90, sigma 2.45. Regime persistence parameters 0.977 and 0.951.
- Test of equal means across regimes: p = 0.106 (equities), 0.748 (rates), 0.620 (FX). Test of equal volatilities: p = 0.016, 0.000, 0.003.
- The high-volatility equity regime has the lower mean, which the authors read as bear markets.
- In a simulated two-state example with p00 = 0.95 and p11 = 0.80, the filtered probability tracks the true regime but misses one switch and issues false alarms.
- Cited from Ang and Bekaert (2002): ignoring regimes costs an investor about 2 to 3 cents per dollar of wealth when a risk-free asset is available.
- Cited from Henkel, Martin and Nardari (2011): return predictability is weak in expansions and strong in recessions.

## Signal construction
Not a signal. It tells a bot designer what a regime model can and cannot be expected to deliver: a reliable volatility state, a much less reliable directional state. Use the regime probability to scale position size or to choose which sub-strategy runs, and do not expect the regime label alone to predict direction.

## Relevance to SOL perpetuals at minutes to hours
The volatility-not-mean finding should be assumed to hold for crypto until shown otherwise; the crypto HMM papers in this folder find the same thing ([koki-2020](koki-2020-predictability-cryptocurrencies-bayesian-hmm.md)). The idea that predictability is concentrated in particular regimes is worth testing directly: measure whether order-flow or momentum signals on SOL have different hit rates in high- and low-volatility states. The monthly persistence numbers do not transfer to intraday bars.

## Caveats
A survey with monthly illustrations; no out-of-sample trading test of its own. The asset-allocation welfare numbers it cites assume the investor knows the model parameters, which the authors themselves flag.
