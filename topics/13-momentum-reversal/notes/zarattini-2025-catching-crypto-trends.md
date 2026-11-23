---
title: "Catching Crypto Trends: A Tactical Approach for Bitcoin and Altcoins"
authors: "Zarattini, Carlo; Pagani, Alberto; Barbon, Andrea"
year: 2025
venue: "Swiss Finance Institute Research Paper No. 25-80"
url: "https://concretumgroup.com/wp-content/uploads/2026/02/Catching-Crypto-Trends.pdf"
pdf: "sources/13-momentum-reversal/zarattini-2025-catching-crypto-trends.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "multi-day"
tags: "trend-following, donchian-channel, breakout, volatility-targeting, ensemble, crypto"
---

## Key insight
A classic breakout system (Donchian channel entry, trailing stop at the channel midline, volatility-targeted size) works on Bitcoin and on a rotating portfolio of liquid coins over 2015 to 2025. Short look-backs of 5 to 30 days gave the best risk-adjusted results, in line with the finding elsewhere that crypto trends are fast. Averaging nine look-backs into one ensemble position gives a smoother result than any single window.

## Method
For look-back n in {5, 10, 20, 30, 60, 90, 150, 250, 360} days: upper band = max of the last n closes, lower = min, mid = average of the two. Go long when the close equals the upper band; exit on the first close below a trailing stop that starts at the midline and only ratchets up: `Stop(t+1) = max(Stop(t), Mid(t))`. Weight = min(25% / sigma_t, 200%) while in a position, with sigma the 3-month annualised volatility. The Combo model averages the nine weights. Costs of 10, 25 and 50 basis points are tested; a rule that skips volatility-driven resizing unless the weight is off target by more than 20% reduces turnover. The portfolio version selects the most liquid coins monthly. A long-short variant is in the appendix.

## Data and sample
CoinMarketCap daily data described as survivorship-bias-free: 21,616 coins, January 2010 to March 2025. Backtests run 1 January 2015 to 19 March 2025.

## Reported results
- Bitcoin, no costs: 5 to 30 day models have Sharpe ratios near 1.6. Combo: CAGR 30%, Sharpe 1.58, Sortino 2.03, maximum drawdown 19% (above 80% for passive Bitcoin), annualised alpha 14% versus Bitcoin. Alphas are significant except for the 150- and 250-day models.
- Costs hurt the short-window models most; the 20% rebalance threshold recovers roughly 100 basis points a year at 50 basis point costs.
- Top-20 rotating portfolio, net of 10 basis points: Sharpe 1.57, maximum drawdown 11%, alpha about 10.8% a year versus Bitcoin.
- Average 6-month rolling correlation with the SG Trend Index is about 7.4%.

## Signal construction
Inputs: closes and a volatility estimate. For each n, a binary state (in trend or not) from breakout entry and ratcheting midline stop; ensemble signal = mean of states, in [0, 1] (or [-1, 1] long-short); size = signal * vol target / vol. Update per bar.

## Relevance to SOL perpetuals at minutes to hours
The structure is frequency-agnostic and can be recomputed on hourly bars: n-bar breakout with a midline trailing stop, averaged across several n. The graded ensemble output suits a low-leverage venue because it rarely asks for full size. The daily result gives a slow trend state for SOL. Whether 5 to 30 bar breakouts work on hourly SOL bars after perpetual fees is not shown here. The rebalance-threshold idea transfers directly as a turnover control.

## Caveats
Lead author's firm sells trading research; not peer-reviewed. Long-only results in an asset that rose enormously benefit from drift and from volatility targeting (compare Huang et al. 2020); the long-short appendix is the fairer test and was not examined in detail here. Daily closes from an aggregator are not executable prices. Nine windows chosen by the authors; in-sample only.
