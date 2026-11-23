---
title: "Statistical Arbitrage in the U.S. Equities Market"
authors: "Avellaneda, Marco; Lee, Jeong-Hyun"
year: 2010
venue: "Quantitative Finance (author version dated 15 June 2009 read; journal details not confirmed in session)"
url: "https://math.nyu.edu/~avellane/AvellanedaLeeStatArb20090616.pdf"
pdf: "sources/13-momentum-reversal/avellaneda-2010-statistical-arbitrage-us-equities.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "equities"
horizon: "multi-day"
tags: "statistical-arbitrage, mean-reversion, ornstein-uhlenbeck, s-score, pca, volume-time"
---

## Key insight
Mean reversion is far more reliable in the residual of an asset against its systematic factors than in the raw price. Modelling that residual as an Ornstein-Uhlenbeck process gives a standardised distance from equilibrium, the s-score, which is the standard template for contrarian signals. Performance decayed sharply after 2002, and measuring returns in volume time (trusting high-volume moves, fading low-volume ones) restored much of it.

## Method
Each stock's return is regressed on factor returns, either the top principal components of the correlation matrix (15 in the base case) or its sector ETF. The cumulative residual X is fitted as `dX = kappa*(m - X)dt + sigma*dW` by an AR(1) regression on a 60-day trailing window. Only residuals with fast reversion are traded: kappa > 252/30, a mean-reversion time under half the window. The signal is

`s = (X - m) / sigma_eq`, with `sigma_eq = sigma / sqrt(2*kappa)`.

Rules: open long if s < -1.25, open short if s > +1.25, close long when s > -0.50, close short when s < +0.75. Positions are hedged with the factors. A modified s-score adjusts for residual drift. The volume variant rescales each day's return by average volume over actual volume, so that moves on unusually high volume count for less in the contrarian signal.

## Data and sample
Broad universe of US stocks, daily data, back-tests 1997 to 2007, with a detailed look at August 2007. Thresholds were tuned on 2000 to 2002. Costs: 5 basis points per trade (10 round trip).

## Reported results
- PCA strategies: average annual Sharpe ratio 1.44 over 1997 to 2007 after costs, much stronger before 2003; only 0.9 over 2003 to 2007.
- ETF-factor strategies: Sharpe 1.1 over 1997 to 2007, with similar degradation after 2002.
- ETF strategies using volume-time signals: Sharpe 1.51 over 2003 to 2007.
- The August 2007 drawdown is consistent with the Khandani and Lo unwinding account.

## Signal construction
For SOL: (1) regress SOL returns on BTC and ETH returns (or the first principal components of a liquid-perp basket) over a rolling window; (2) cumulate the residual; (3) fit AR(1) to get kappa, m, sigma_eq; (4) compute s; (5) trade only if the implied half-life is short relative to the window. Because the bot is directional and unhedged, s is a tilt on SOL: negative s argues for long, positive for short. Recompute every bar; apply the volume-time rescaling with venue-aggregated volume.

## Relevance to SOL perpetuals at minutes to hours
The residual framing is the main transfer. "SOL is extended" should mean extended relative to what BTC and ETH explain, since the common crypto factor trends while idiosyncratic deviations revert. The volume-time rule matches crypto evidence (Bianchi et al. 2022) that low-volume moves revert and high-volume moves persist. Thresholds, window and the kappa filter must be re-estimated on intraday crypto data; Fil and Kristoufek (2020) suggest reversion in crypto is an intraday phenomenon.

## Caveats
US equities, daily, hedged market-neutral portfolios of hundreds of names; an unhedged single-asset tilt carries the factor risk the paper removes. The post-2002 decay shows capacity and crowding erode this signal. Crypto residual relationships break during idiosyncratic events (outages, unlocks, listings), where the s-score will signal "fade" into genuine repricing.
