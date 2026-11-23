---
title: "A Century of Evidence on Trend-Following Investing"
authors: "Hurst, Brian; Ooi, Yao Hua; Pedersen, Lasse Heje"
year: 2017
venue: "Journal of Portfolio Management 44(1), Fall 2017"
url: "https://fairmodel.econ.yale.edu/ec439/hurst.pdf"
pdf: "sources/13-momentum-reversal/hurst-2017-century-trend-following.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "multi"
horizon: "multi-day"
tags: "trend-following, time-series-momentum, long-history, out-of-sample, drawdowns"
---

## Key insight
A simple time-series momentum strategy applied to 67 markets was profitable in every decade from 1880 to 2016, including the century before the sample used in the original academic studies. The authors treat the first ten decades as out-of-sample evidence that trends are a persistent feature of speculative markets, not a product of data mining. Performance was weakest when markets were highly correlated and when trends reversed sharply.

## Method
An equal-weighted combination of 1-month, 3-month and 12-month time-series momentum signals. For each signal, a market is held long if its excess return over the look-back is positive and short if negative. Each position targets equal volatility, and the combined portfolio is scaled to a 10% annualised ex ante volatility target. Rebalanced monthly. Simulated transaction costs (asset-class estimates scaled up for earlier periods) and a hypothetical 2% management and 20% performance fee are subtracted. A robustness check lags every signal by one month.

## Data and sample
Monthly returns for 29 commodities, 11 equity indices, 15 bond markets and 12 currency pairs. Commodity futures prices before 1951 were hand-collected from Chicago Board of Trade annual reports. Cash index returns financed at local short rates are used where futures did not exist. Strategy returns run 1880 to 2016.

## Reported results
- Positive returns in each decade for the combined strategy, and for each of the 1-, 3- and 12-month signals separately.
- Each of the 67 markets had a positive average return, with an average per-market Sharpe ratio of about 0.4 (gross).
- Lagging the signal by one month still gave positive returns in most decades, but performance deteriorated, most for the shorter-term signals.
- Low correlation to stocks and bonds in the full period and in each decade; positive returns in 8 of the 10 largest drawdowns of a 60/40 portfolio. Those drawdowns lasted about 15 months on average, which gave a monthly trend signal time to turn short. The authors note the strategy may not help in very rapid crashes such as 1987.
- The strategy itself has lost up to about 25% peak to trough; its own stress periods are sharp reversals across many markets or long stretches without clear trends.
- Among macro environments, correlation between markets mattered most: the strategy did best in low-correlation periods.

## Signal construction
For each look-back L in {1, 3, 12 months}: s_L = sign(excess return over L). Combined signal = average of the three signs, scaled by target volatility over estimated volatility. A bot can reproduce the "blend of horizons" idea at any bar size by averaging signs of several look-backs.

## Relevance to SOL perpetuals at minutes to hours
Two things transfer. First, blending several look-backs is more robust than choosing one. Second, the finding that delaying a short-horizon signal costs the most performance implies that fast signals are latency-sensitive, which matters when the signal is computed on Binance or Hyperliquid and executed on a thinner venue. The monthly horizon and the 67-market diversification do not transfer; a single SOL contract is one of the 67 bets with an expected Sharpe closer to 0.4 than to 1.

## Caveats
Monthly data; cost and fee estimates are acknowledged by the authors to be uncertain and exclude roll costs. Early data use cash indices and high-low averages. All three authors are AQR principals. Nothing in the paper speaks to intraday horizons.
