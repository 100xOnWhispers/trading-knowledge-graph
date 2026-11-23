---
title: "Social signals and algorithmic trading of Bitcoin"
authors: "Garcia, David; Schweitzer, Frank"
year: 2015
venue: "Royal Society Open Science 2:150288 (arXiv:1506.01513)"
url: "https://arxiv.org/pdf/1506.01513"
pdf: "sources/18-positioning-sentiment/garcia-2015-social-signals-algorithmic-trading-bitcoin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "daily"
tags: "twitter-polarization, valence, exchange-volume, var-impulse-response, leave-out-backtest, trading-costs"
---

## Key insight
In a multivariate system of social and economic signals, increases in Twitter opinion polarization and in exchange volume precede Bitcoin price increases, and emotional valence precedes both. Search volume and tweet counts add nothing once these are included. A daily strategy voting across polarization, valence and volume was profitable on a one-year leave-out sample after moderate costs. Disagreement, not average mood, carried the most information.

## Method
A VAR on daily returns and first differences of seven signals: exchange volume, on-chain transaction volume, client downloads, Google search volume, tweet count, tweet valence, tweet polarization. Valence and polarization come from psycholinguistic lexicons (polarization measures the simultaneous presence of positive and negative expression). Impulse-response functions, corrected for correlated errors and checked with permutation tests, identify which signals lead returns. Each leading signal Y becomes a predictor:

`sign(Ret(t+1)) = sign(s_Y * (Y(t) - Y(t-1)))`

where `s_Y` is the sign of the impulse response. A Combined strategy takes the majority vote. Strategies may go long or short. Benchmarks: buy-and-hold, momentum, up-down persistence, RSI, and 10,000 random traders.

## Data and sample
Daily data from early 2011. Model estimation uses data up to 1 January 2014 (almost three years). The leave-out backtest runs through 2014 on the BTC/USD rate at Bitfinex, with a Bitcoin Price Index variant.

## Reported results
- Cumulative return response to a one-standard-deviation shock exceeds 0.1% only for polarization, valence and exchange volume, reaching up to 0.5% in one day.
- Leave-out Sharpe ratios (annualized, 365 days): Combined 1.7653, Polarization 1.0120, Valence 0.6410, FXVolume 0.5738, Momentum 0.9146, Buy-and-hold -0.7741, RSI -0.1772, random -1.6590.
- Mean daily return: Combined 0.3229%, Polarization 0.1779%.
- Costs: the Combined strategy remains profitable at low costs and stops being profitable above 0.25% per trade. Forced daily position closing reduces returns but stays profitable at 0.1%.
- Short-only outperformed long-only, as expected in a falling year.

## Signal construction
Inputs per day: posts mentioning the asset, exchange volume.
1. Compute daily valence from a word-valence lexicon, and polarization as the geometric mean of the daily ratios of positive and of negative words per tweet (the paper uses LIWC word classes), so that polarization is high only when positive and negative expression coexist.
2. `vote_i = sign(Y_i(t) - Y_i(t-1))` for polarization, valence and volume (all positive sign).
3. Position for t+1 = sign of the sum of votes.
Parameters: none beyond the lexicon. Update daily in the paper; an hourly variant is an untested extension.

## Relevance to SOL perpetuals at minutes to hours
The transferable ideas are the polarization measure and the practice of deriving signal signs from a VAR on one period and testing on another. Costs on a SOL perp are far below 0.25%, so the cost hurdle is not binding, but the daily horizon and 2014 market structure are. Rising disagreement as a bullish lead is counter-intuitive and worth a direct test on hourly SOL data.

## Caveats
The grade is held at B despite peer review, a leave-out test and cost analysis, because the test is one year (2014) of one asset in a monotonic decline, where any short-biased rule looks good. Sharpe ratios from 365 daily points have wide error bands. Twitter access and bot composition have changed completely since 2014. No independent replication was examined in this session.
