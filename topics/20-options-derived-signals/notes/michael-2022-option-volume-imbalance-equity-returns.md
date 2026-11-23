---
title: "Option Volume Imbalance as a predictor for equity market returns"
authors: "Michael, Nikolas; Cucuringu, Mihai; Howison, Sam"
year: 2022
venue: "arXiv preprint 2201.09319"
url: "https://arxiv.org/abs/2201.09319"
pdf: "sources/20-options-derived-signals/michael-2022-option-volume-imbalance-equity-returns.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "20-options-derived-signals"
asset_class: "equities"
horizon: "daily"
tags: "option-volume-imbalance, options-order-flow, market-makers, overnight-returns, nonlinear-prediction, pnl-regression, cross-impact"
---

## Key insight
A normalised imbalance between bullish option volume (call buys and put sells) and bearish option volume (call sells and put buys) predicts the next overnight excess return of the underlying stock. The strongest signal is the imbalance of market makers, traded against: market makers hold the other side of informed customer flow. Predictability concentrates in overnight returns, in high-implied-volatility contracts and in puts.

## Method
For asset i, day d and market participant class m:

`OVI = sum_j (X_up - X_down) / sum_j (X_up + X_down)`

over option contracts j, where `X_up` = call-buy plus put-sell volume and `X_down` = call-sell plus put-buy volume. Variants use number of trades or premium-weighted volume. The sign of OVI sets a long or short position in the underlying against the SPY benchmark; results are reported as cumulative profit, annualised Sharpe ratio and profit per dollar traded, for portfolios formed on the magnitude of the signal. The authors avoid linear regression and introduce a "P&L regression" that fits weights by maximising cumulative profit through a smooth objective, which handles correlated, sparse features. A directed network model tests cross-asset effects.

## Data and sample
Nasdaq Options Market and Nasdaq PHLX datasets, 2 January 2015 to 31 December 2019, cumulative volume reports every 10 minutes, split by five participant classes (firm proprietary, broker, market maker, customer, professional customer) and, except for market makers, by opening or closing and buy or sell.

## Reported results
- On PHLX, the market-maker OVI gives annualised Sharpe ratios between 3.5 and 4.4 in absolute value (the raw sign is negative) and cumulative returns of 17% to 25% over five years, depending on the portfolio. Customer OVI gives Sharpe ratios of about 2.7 to 3.5 with the positive sign; broker OVI is negative and significant; firm proprietary and professional customer OVI show nothing.
- Profit per dollar is of the order of 1 to 2 basis points a day; tail portfolios reach up to 4 basis points a day.
- Overnight (close to open) returns carry most of the effect; open-to-close returns the least.
- High-implied-volatility contracts are much more informative than low; puts more than calls. Opening versus closing trades make little difference.
- Cross-asset effects are more numerous than own-asset effects after a Bonferroni correction.
- On the second exchange the market-maker Sharpe ratio is about 2.5 to 3.
- Transaction costs are not included, and the authors state that the strategy may not be executable.

## Signal construction
Crypto analogue from the Deribit trade feed, which gives the aggressor side but no participant class: per interval, `OVI = (call_buy + put_sell - call_sell - put_buy) / total`, by aggressor, in contracts, trades or premium. The passive side approximates the market-maker class with the opposite sign. Compute separately for high-implied-volatility (short-dated, out-of-the-money) contracts and for puts. Evaluate with a sign-based profit measure before fitting anything linear.

## Relevance to SOL perpetuals at minutes to hours
The construction is simple and maps onto data a bot can collect for BTC and ETH. The horizon does not map cleanly: the effect is an overnight one in a market that closes, and crypto has no close. The nearest analogues to test are the low-liquidity hours and the window after the 08:00 UTC Deribit expiry. The cross-asset finding supports using BTC option imbalance as an input for SOL. Profit of 1 to 4 basis points a day before costs is small against perpetual taker fees, so the feature is a candidate input to a combined model, not a standalone strategy.

## Caveats
Preprint, not peer reviewed. No costs. Sharpe ratios are for diversified portfolios of hundreds of stocks; a single-asset time-series version will be far noisier. Many variants are reported (weighting schemes, quantile portfolios, filters), which raises data-snooping risk. The participant-class breakdown that drives the best result does not exist for crypto venues.
