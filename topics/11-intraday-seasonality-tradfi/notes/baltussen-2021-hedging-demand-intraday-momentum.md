---
title: "Hedging demand and market intraday momentum"
authors: "Baltussen, Guido; Da, Zhi; Lammers, Sten; Martens, Martin"
year: 2021
venue: "Journal of Financial Economics 142(1), 377-403"
url: "https://www3.nd.edu/~zda/intramom.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/baltussen-2021-hedging-demand-intraday-momentum.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "futures"
horizon: "hours"
tags: "intraday-momentum, gamma-hedging, leveraged-etf, last-half-hour, futures, out-of-sample"
---

## Key insight
Across more than 60 futures in equities, bonds, commodities and currencies, the return from the previous close up to 30 minutes before the close ("rest of day", ROD) positively predicts the last 30-minute return. The effect then reverts over the following days, which marks it as price pressure, not information. The authors tie it to gamma hedging: option market makers and leveraged-ETF managers who are short gamma must trade in the direction of the day's move near the close.

## Method
The day (close to close) is split into overnight (ON), first half-hour (FH), middle (M), second-to-last half-hour (SLH) and last half-hour (LH). Core regression: r_LH(t) = a + b * r_ROD(t) + e(t), with ROD = ON + FH + M + SLH. This is compared with the Gao et al. predictor r_ONFH and with r_M and r_SLH, using in-sample t-values and out-of-sample R-squared. Mechanism tests interact r_ROD with a net gamma exposure proxy for S&P 500 options and with leveraged-ETF rebalancing demand computed from fund size and leverage. A simple sign-following strategy is evaluated.

## Data and sample
Intraday futures data, December 1974 to May 2020: 17 developed equity index futures, 16 government bond futures, 21 commodity futures, 8 currency futures. Trading hours are chosen to match each market's common session.

## Reported results
- In the main equity panel, r_ROD has the highest t-value (7.29) and the highest out-of-sample R-squared (2.88%); in the multi-predictor specification r_ONFH has t = 6.46, r_SLH 4.82 and r_M 4.43.
- r_ROD beats r_ONFH on out-of-sample R-squared for most individual contracts; when the two disagree in sign, r_ROD is the better predictor.
- r_SLH's predictive power does not extend to commodities and currencies.
- Sign-following strategies give annualized Sharpe ratios between 0.87 and 1.73 at the asset-class level, before costs.
- Intraday momentum is present when dealer net gamma is negative and strengthens as it becomes more negative; it is distinct from Heston-style same-time seasonality.
- Costs are not modelled; the authors state the S&P 500 futures version stays positive net of a one-tick cost.

## Signal construction
At T_close minus 30 minutes: r_ROD = log(P_now / P_prev_close). Position = sign(r_ROD) (or proportional), held to the close. Conditioners: stronger when dealer gamma is negative and when leveraged-product rebalancing demand is large (the paper computes it from each fund's market capitalization and leverage; the exact formula was not re-checked here).

## Relevance to SOL perpetuals at minutes to hours
The mechanism translates better than the clock rule. Crypto has its own short-gamma and forced-flow actors: Deribit option dealers, leveraged tokens and leveraged crypto ETFs that rebalance at fixed times, and liquidation engines that trade with the move. A testable version: a move-so-far signal measured into known rebalancing or expiry windows (US equity close for leveraged SOL ETFs, Deribit 08:00 UTC expiry, funding timestamps), conditioned on dealer gamma estimated from Deribit open interest. The subsequent multi-day reversal is as important as the entry.

## Caveats
Gross returns; one trade per day per market. Strength depends on gamma positioning, which changes sign. SOL option and leveraged-product markets are small compared with S&P 500 equivalents, so the forced flow may be too small to matter. Two authors are affiliated with an asset manager.
