---
title: "A Trend Factor for the Cross Section of Cryptocurrency Returns"
authors: "Fieberg, Christian; Liedtke, Gerrit; Poddig, Thorsten; Walker, Thomas; Zaremba, Adam"
year: 2025
venue: "Journal of Financial and Quantitative Analysis 60(7), 3116-3153"
url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0022109024000747"
pdf: "sources/13-momentum-reversal/fieberg-2025-trend-factor-cryptocurrency-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "multi-day"
tags: "trend-factor, machine-learning, elastic-net, technical-indicators, cross-sectional, crypto"
---

## Key insight
A single trend characteristic, CTREND, built by a machine-learning combination of 28 price, volume and volatility indicators over several horizons, predicts the cross-section of coin returns better than plain momentum and makes the momentum factor insignificant. The predictability survives transaction costs, holds in large liquid coins, and persists for holding periods up to four weeks. It is the strongest peer-reviewed evidence that trend information in crypto is real and that combining many trend measures beats picking one.

## Method
Each week, 28 technical signals are computed per coin from daily data: momentum oscillators, moving-average indicators, volume indicators and volatility indicators, using standard parameter choices from the literature to limit data snooping. Signals are converted to cross-sectional ranks. Cross-sectional regressions of returns on each signal give individual forecasts, and a combined elastic net (the cross-sectional C-ENet of Han, He, Rapach and Zhou) selects and averages the forecasts that survive L1 and L2 shrinkage. The out-of-sample forecast is the CTREND characteristic. Coins are sorted into value-weighted quintiles, rebalanced weekly. Net returns use turnover and per-leg cost assumptions.

## Data and sample
More than 3,000 coins, April 2015 to May 2022, daily data aggregated to weekly portfolio returns.

## Reported results
- High-minus-low CTREND quintile spread: 3.87% per week (t = 5.19), annualised Sharpe ratio 1.94, value-weighted.
- Not subsumed by existing crypto factors; an alternative risk adjustment in the appendix gives a weekly alpha of 2.61%.
- Turnover is about 68% a week. With 30 basis points on the long leg and 40 on the short leg (and two harsher settings), net long-short returns range from 2.90% (t = 3.89) to 2.35% (t = 3.16) per week. Breakeven cost is 1.41%.
- The effect remains in the biggest and most liquid half of coins and across subperiods and market states.
- The factor draws on a wide range of indicators, not a sparse few.

## Signal construction
For one asset the cross-sectional sort is unavailable, but the recipe transfers: compute a panel of trend indicators at several look-backs (price to moving average, moving-average crossovers, rate of change, volume trends, volatility-band position), standardise them, and combine with a penalised regression fitted on a rolling window to forecast the next-period return. Refit weekly. To stay closer to the paper, fit the combination on a panel of liquid perpetuals and read off SOL's forecast and its rank.

## Relevance to SOL perpetuals at minutes to hours
Confirms that liquid-coin trend predictability exists net of realistic costs at weekly horizon, and shows a disciplined way to use machine learning: shrinkage over a pre-specified indicator set, not a search over rules. SOL's CTREND rank is a candidate slow directional prior. The intraday analogue (same combination on hourly bars) is untested and has much higher turnover relative to signal.

## Caveats
Weekly, cross-sectional, long-short across thousands of coins; many short legs are not shortable in practice. Sample ends May 2022 and includes the 2017 and 2021 manias. The indicator set overlaps with oscillators covered under topic 16.
