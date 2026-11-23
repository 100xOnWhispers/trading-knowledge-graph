---
title: "The Sharpe Ratio Efficient Frontier"
authors: "Bailey, David H.; Lopez de Prado, Marcos"
year: 2012
venue: "Journal of Risk (forthcoming per the preprint read)"
url: "https://www.davidhbailey.com/dhbpapers/sharpe-frontier.pdf"
pdf: "sources/26-backtest-overfitting/bailey-2012-sharpe-ratio-efficient-frontier.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "probabilistic-sharpe-ratio, minimum-track-record-length, non-normality, live-monitoring"
---

## Key insight
An estimated Sharpe ratio is a noisy statistic whose uncertainty depends on track-record length, skewness and kurtosis. The paper defines the probabilistic Sharpe ratio (PSR), the probability that the true Sharpe exceeds a chosen benchmark, and inverts it to obtain the minimum track record length (MinTRL) needed to claim skill at a given confidence.

## Method
For n observations with estimated (non-annualized) Sharpe SR, skewness γ3 and kurtosis γ4, and benchmark SR*:

PSR(SR*) = Z[ (SR − SR*) · sqrt(n − 1) / sqrt(1 − γ3·SR + ((γ4 − 1)/4)·SR²) ]

MinTRL = 1 + [1 − γ3·SR + ((γ4 − 1)/4)·SR²] · ( Z_α / (SR − SR*) )²   (observations)

The paper then builds a "Sharpe ratio efficient frontier" that optimizes portfolios on PSR, which is outside this topic.

## Data and sample
Analytical results, simulated mixtures of normals, and Hedge Fund Research monthly style indices from January 2000 to May 2011 (134 monthly observations).

## Reported results
- With daily IID normal returns, a 2.73-year track record is needed for an observed annualized Sharpe of 2 to be judged greater than 1 at 95% confidence; 2.83 years with weekly returns and 3.24 years with monthly returns.
- With the skewness (−0.72) and kurtosis (5.78) reported for the HFR aggregate index, the monthly requirement rises to 4.99 years.
- A hedge fund with annualized Sharpe 1.59 over two years of monthly data passes the 95% test under normality but fails once its negative skewness and excess kurtosis are included; with three years it would pass.
- On HFR indices, most styles show Sharpe above zero, but only 9 style indices substantiate an annualized Sharpe above 0.5 at 95% confidence.
- MinTRL is expressed in observations, and the asymptotics need more than about 30 observations; the moments should be estimated on longer series.

## Signal construction
Not a trading signal; a monitoring statistic. For a live strategy, at each review compute SR, skewness and kurtosis of realized net returns per period, then PSR against (a) zero and (b) the backtest Sharpe haircut to a realistic level. Use MinTRL before going live to state how long the strategy must run before a verdict is possible, and treat PSR falling below a pre-set level against the minimum acceptable Sharpe as a decay alarm.

## Relevance to SOL perpetuals at minutes to hours
This is the cleanest tool in the set for the live-monitoring part of the scope. An intraday bot generates many trades, so n grows quickly, but only if returns are close to independent; daily net P&L is the safer unit. Crypto strategy returns with stop-losses or liquidation exposure have negative skew and fat tails, which lengthen MinTRL materially, as in the hedge fund example. A new venue such as Kalshi adds a second question the formula does not answer: whether fills and funding there match the backtest venue.

## Caveats
Assumes IID returns; positive autocorrelation inflates the apparent Sharpe and shortens MinTRL spuriously. The benchmark SR* is single-trial; if the strategy was selected from many, the threshold must be deflated (see the deflated Sharpe ratio). The hedge fund evidence uses indices from 2000 to 2011 and is illustrative only.
