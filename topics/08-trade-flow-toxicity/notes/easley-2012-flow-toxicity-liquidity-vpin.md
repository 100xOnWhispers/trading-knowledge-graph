---
title: "Flow Toxicity and Liquidity in a High Frequency World"
authors: "Easley, David; Lopez de Prado, Marcos M.; O'Hara, Maureen"
year: 2012
venue: "Review of Financial Studies 25(5), 1457-1493 (read: February 2012 forthcoming draft hosted by NYU Stern)"
url: "https://www.stern.nyu.edu/sites/default/files/assets/documents/con_035928.pdf"
pdf: "sources/08-trade-flow-toxicity/easley-2012-flow-toxicity-liquidity-vpin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "futures"
horizon: "hours"
tags: "vpin, flow-toxicity, volume-clock, bulk-volume-classification, volatility-forecast, flash-crash"
---

## Key insight
The paper introduces VPIN, the Volume-Synchronized Probability of Informed Trading: the average absolute buy/sell volume imbalance across equal-volume buckets. It is offered as a real-time proxy for order-flow "toxicity", meaning adverse selection of market makers. The authors report that VPIN is positively correlated with subsequent absolute returns and that it was elevated hours before the 6 May 2010 flash crash. It is a volatility and liquidity-risk indicator, not a directional signal.

## Method
Time is measured in volume: trades are grouped into buckets of fixed volume V. Volume in each one-minute bar is split into buys and sells by bulk classification, V_buy = V_bar * Z(dP / sigma_dP), V_sell = V_bar - V_buy, where Z is the standard normal CDF and sigma_dP the standard deviation of bar price changes. Then

VPIN = sum over the last n buckets of |V_sell - V_buy| / (n * V).

The baseline is V = 1/50 of average daily volume and n = 50; VPIN updates each time a bucket fills. Predictive content is measured as the correlation between ln(VPIN) in bucket tau-1 and the absolute return over bucket tau, and with conditional probability tables of absolute return given the VPIN quantile.

## Data and sample
E-mini S&P 500 futures one-minute bars, 1 January 2008 to August 2011, and WTI crude oil futures for the stability analysis (1 January 2008 to 6 June 2011), front contract by volume, rolled.

## Reported results
- For the (50 buckets per day, 250-bucket sample) setting the correlation between ln(VPIN) and the next bucket's absolute return is 0.400 on 44,537 observations.
- When VPIN is in its bottom quartile, next-bucket absolute returns are in the 0 to 0.25% range more than 90% of the time.
- Over 84% of absolute returns above 0.75% were preceded by VPIN in its upper quartile; across parameter choices this share is between 80% and 90%.
- On 6 May 2010 the CDF of VPIN crossed 0.9 at least two hours before the crash.
- The authors note that even at high VPIN the next-bucket absolute return is usually not large; persistent high readings are what matter.

## Signal construction
Inputs: trade prints with size. Steps: (1) choose V, for example 1/50 of trailing average daily volume; (2) fill buckets in trade order, carrying overflow to the next bucket; (3) sign volume, using exchange aggressor flags where available instead of bulk classification; (4) VPIN = mean of |buy - sell| / V over the last n buckets; (5) convert to an empirical CDF rank over a trailing history. Use as a regime variable: reduce size, widen stops or pause mean-reversion entries when the rank is above a threshold such as 0.9.

## Relevance to SOL perpetuals at minutes to hours
Crypto venues publish the aggressor side, so the classification step is exact. A VPIN on Binance or Bybit SOL perp volume is cheap to compute and gives a horizon (a bucket of 1/50 daily volume is roughly half an hour) that matches the bot. The claim to re-test is narrow: does the VPIN rank add anything for forecasting SOL realized volatility or liquidation cascades beyond trailing realized volatility and volume? The critiques in [andersen-2014-vpin-flash-crash](andersen-2014-vpin-flash-crash.md) and [andersen-2013-order-flow-toxicity-perfect-classification](andersen-2013-order-flow-toxicity-perfect-classification.md) say the answer in E-mini futures was no.

## Caveats
The draft states that VPIN is a trademark of Tudor Investment Corp. and that the authors applied for a patent and have a financial interest. The evidence is in-sample correlation without a benchmark forecast such as lagged realized volatility or VIX. Results depend on bar size, bucket size and classification rule. VPIN says nothing about direction.
