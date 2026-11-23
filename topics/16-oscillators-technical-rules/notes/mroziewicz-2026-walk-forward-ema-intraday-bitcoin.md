---
title: "A novel approach to trading strategy parameter optimization, using double out-of-sample data and walk-forward techniques"
authors: "Mroziewicz, Tomasz; Ślepaczuk, Robert"
year: 2026
venue: "arXiv preprint 2602.10785 (v1, February 2026)"
url: "https://arxiv.org/pdf/2602.10785v1"
pdf: "sources/16-oscillators-technical-rules/mroziewicz-2026-walk-forward-ema-intraday-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "hours"
tags: "ema-crossover, walk-forward-optimization, intraday, bitcoin, transaction-costs, bar-frequency, out-of-sample"
---

## Key insight
An EMA crossover on intraday crypto is unprofitable below roughly 30-minute bars once a 0.1% fee per transaction is charged, and viable at 60-minute bars with a break-even near 0.4%. Even with a carefully protected, single-use out-of-sample period, the best walk-forward configuration from training was not the best afterwards, and the strategy matched buy-and-hold on return while cutting drawdown.

## Method
The strategy is a long/short EMA crossover: long when the fast EMA is above the slow EMA, short otherwise. The EMA window pair is re-optimized by walk-forward: choose the pair that performed best over the last T_train days, trade it for T_test days, roll forward. The paper's contribution is to treat T_train and T_test themselves as parameters, each drawn from {1, 2, 3, 5, 7, 10, 14, 21, 28} days, giving 81 combinations per bar size. Bar sizes are 1, 5, 10, 15, 30 and 60 minutes. Combinations are ranked by a "Robust Sharpe Ratio": each cell of the 9 by 9 Sharpe heat map keeps half its own value and takes the rest from its neighbors, so isolated peaks are discounted. The top two combinations from the training period are run once on the unseen period. Significance is checked with a block bootstrap that shuffles position blocks, and against randomly drawn EMA pairs. A fee of 0.1% applies per transaction, so a long-to-short reversal costs 0.2%.

## Data and sample
One-minute prices for Bitcoin, Ethereum and Binance Coin from a Kaggle forecasting competition data set (exchange not specified). Training period 8 February 2018 to 1 September 2019; unseen period 7 November 2019 to 22 August 2021. Parameters are chosen on Bitcoin only and applied unchanged to the other two.

## Reported results
- Bar size: at 0.1% cost, 1 to 15-minute bars are unprofitable; some 15 and 30-minute combinations are positive; at 60 minutes every one of the 81 combinations has a positive Sharpe ratio in training and beats buy-and-hold there.
- Selected combinations: 7-day training with 28-day testing, and 14-day training with 10-day testing.
- Unseen period: Sharpe ratios fell about 20% on average from training (30% for the best, 10% for the second). The top training configuration (7/28) underperformed both buy-and-hold and the 14/10 alternative. Buy-and-hold led on Sharpe ratio; the walk-forward portfolios had 10% to 20% lower drawdown and lower volatility.
- The strategy did well in high-volatility periods (including March 2020) and lagged in quiet ones.
- Break-even cost at 60-minute bars: about 0.4% per transaction.
- A portfolio mixing buy-and-hold with the two strategies beat every component, with about half the drawdown of buy-and-hold.
- Block bootstrap: better than random at the 5% level.

## Signal construction
On 60-minute closes: s_t = sign(EMA_fast(t) - EMA_slow(t)). Every T_test days, re-select (fast, slow) as the pair with the best performance over the previous T_train days. The paper's evidence favors T_train and T_test of a week or more. The grid of EMA windows is in the paper but was not recorded here.

## Relevance to SOL perpetuals at minutes to hours
The horizon and instrument type match, and the cost sensitivity gives a usable rule of thumb: a trend rule that reverses position needs bars long enough that the expected move per trade exceeds twice the round-trip cost. If the all-in cost per side on the target venue is near 0.1%, sub-hour trend rules are unlikely to pay. The smoothing of the parameter surface before picking a peak is a cheap robustness device worth copying. The drawdown reduction is the dependable benefit; excess return is not.

## Caveats
The unseen period (late 2019 to mid-2021) contains one of the strongest crypto bull runs, which flatters long exposure and buy-and-hold alike. Costs exclude slippage and funding, and the authors list order-book impact, shorting availability and futures holding costs as limitations. One strategy family, three coins, no SOL. Preprint, not peer reviewed. Sharpe figures are not reported here because I did not copy the tables.
