---
title: "Slow Momentum with Fast Reversion: A Trading Strategy Using Deep Learning and Changepoint Detection"
authors: "Wood, Kieran; Roberts, Stephen; Zohren, Stefan"
year: 2021
venue: "arXiv preprint 2105.13727 (v3)"
url: "https://arxiv.org/pdf/2105.13727"
pdf: "sources/13-momentum-reversal/wood-2021-slow-momentum-fast-reversion.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "futures"
horizon: "daily"
tags: "machine-learning, changepoint-detection, gaussian-process, lstm, momentum-turning-points, mean-reversion"
---

## Key insight
Trend strategies lose most at momentum turning points, when a slow signal is still pointing the old way. Feeding an online changepoint detector's outputs (how severe and how recent a break is) into a Deep Momentum Network lets the model learn when to trust slow momentum and when to switch to fast mean reversion. The addition raised the out-of-sample Sharpe ratio by about one third over 1995 to 2020 and by about two thirds over 2015 to 2020, a period when plain momentum struggled.

## Method
Changepoint detection (CPD) uses Gaussian process regression on a look-back window of daily returns. Two models are fitted by maximum marginal likelihood: a single covariance kernel, and a changepoint kernel that joins two kernels through a sigmoid with location c and steepness s. The severity score nu in (0, 1) is derived from the reduction in negative log marginal likelihood achieved by the changepoint model, and the normalised location gamma in (0, 1) says how far back in the window the break sits. Both are computed for window lengths l in {10, 21, 63, 126, 252} days and appended to the standard inputs (volatility-normalised returns over several horizons and normalised MACD). An LSTM maps the sequence to a position and is trained on the Sharpe-ratio loss. Expanding-window evaluation: train and validate on 1990 to 1995, test 1995 to 2000, then extend by five years each time. The window length is also treated as a hyperparameter chosen on validation loss.

## Data and sample
50 liquid continuous futures contracts (commodities, equities, fixed income, FX) from the Pinnacle Data Corp CLC database, daily, 1990 to 2020.

## Reported results
- Adding the CPD module improves Sharpe by one third over the LSTM baseline for 1995 to 2020 (33% once the window length is re-selected per training window).
- Over 2015 to 2020 the improvement is approximately two thirds.
- Gains appear even with a two-week CPD window, grow up to about one quarter, and fade as the window approaches one year.
- The model learns a mix of slow momentum and fast reversion, flipping position briefly around localised moves.
- Main results exclude transaction costs; an appendix covers them.

## Signal construction
For each bar and each window l: fit the two Gaussian-process models to standardised returns in the window, compute severity nu and location gamma. Use (nu, gamma) as regime features alongside trend features. A simple non-neural use: scale down the slow trend position, and allow a short-look-back contrarian position, when nu is high and gamma indicates a recent break. Gaussian-process fits are costly; pre-compute or use a cheaper online detector at intraday frequency.

## Relevance to SOL perpetuals at minutes to hours
The problem it targets is central for crypto: sharp reversals that punish trend signals. The explicit regime features give the bot a way to decide between its trend and mean-reversion components instead of running both at fixed weights. The finding that short detection windows already help suggests an intraday version (windows of tens of bars) is plausible, but that is untested.

## Caveats
Daily futures, no crypto, costs excluded from headline numbers, and the fast-reversion component implies higher turnover. Gaussian-process changepoint fitting at every bar is computationally heavy for minute data. Improvement is relative to a deep-learning baseline, not to a costed live strategy. Same research group as the baseline paper; no independent replication seen.
