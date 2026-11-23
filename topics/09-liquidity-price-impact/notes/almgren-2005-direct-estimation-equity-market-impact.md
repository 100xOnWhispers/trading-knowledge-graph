---
title: "Direct Estimation of Equity Market Impact"
authors: "Almgren, Robert; Thum, Chee; Hauptmann, Emmanuel; Li, Hong"
year: 2005
venue: "Risk 18(7), 58-62 (read as the May 10, 2005 working-paper version)"
url: "https://www.cis.upenn.edu/~mkearns/finread/costestim.pdf"
pdf: "sources/09-liquidity-price-impact/almgren-2005-direct-estimation-equity-market-impact.pdf"
access: "full-text"
source_type: "industry-research"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "equities"
horizon: "hours"
tags: "price-impact, permanent-impact, temporary-impact, power-law, transaction-cost"
---

## Key insight
Using a large broker dataset, the authors separate impact into a permanent part that depends on total size and a temporary part that depends on trading rate. They fit one dimensionless model across stocks and reject the square-root form for temporary impact in favor of a 3/5 power. The result is a cost formula that needs only volatility, daily volume, turnover, order size and duration.

## Method
For an order of X shares executed over a fraction T of a day, with daily volume V, daily volatility sigma and shares outstanding Theta:

I = gamma * sigma * (X / V) * (Theta / V)^(1/4) + noise  (permanent impact, measured after the order)

J = I/2 + sign(X) * eta * sigma * |X / (V T)|^(3/5) + noise  (realized cost against the arrival price)

The exponents and coefficients are estimated by nonlinear least squares on impact normalized by volatility. I is the net price move from before to after the trade; J is the cost actually paid.

## Data and sample
Almost 700,000 US stock orders executed by Citigroup Equity Trading desks over 19 months, December 2001 to June 2003. After filtering, 29,509 orders remain, all in large-cap US stocks. Mean order size is 1.51% of average daily volume; mean duration is 0.39 days.

## Reported results
- Permanent impact exponent alpha = 0.891 +/- 0.10; the authors keep alpha = 1 (linear), the only value free of price-manipulation arbitrage in their framework.
- Temporary impact exponent beta = 0.600 +/- 0.038; the square-root value 0.5 is rejected and 3/5 is adopted.
- Liquidity factor exponent on inverse turnover is approximately 1/4.
- Universal coefficients gamma = 0.314 +/- 0.041 (t = 7.7) and eta = 0.142 +/- 0.0062 (t = 23).
- Regression R-squared values are typically below one percent: impact is small relative to price noise during execution.

## Signal construction
Not a direction signal. Use it as a pre-trade cost estimator and as a way to decide trade speed:
cost_bps = 0.5 * gamma * sigma * (X/V) * liquidity_factor + eta * sigma * (X / (V T))^0.6
For a perp there are no shares outstanding, so the turnover factor has no direct analogue; drop it or replace it with open interest divided by daily volume and re-fit. Recompute sigma and V on a rolling 24-hour basis.

## Relevance to SOL perpetuals at minutes to hours
The split between permanent and temporary impact is what matters for a directional bot: temporary cost is paid twice in a round trip, so it sets the minimum edge a signal needs. The numerical coefficients come from 2001 to 2003 US large caps traded by one broker and should not be reused. The form (cost rising faster than square root in participation rate) is a hypothesis to test on Kalshi fills. Later work on Bitcoin and on Hyperliquid perps finds exponents at or below 0.5 when impact is expressed against total size, so the 3/5 result may reflect the rate-based parameterization.

## Caveats
Broker-affiliated authors and proprietary data. The paper states that out-of-sample backtests were planned for a future paper, so the fit is in-sample. Orders are not randomly assigned; execution speed is chosen by traders who may react to price moves, which biases impact estimates. The "universal" coefficients are specific to the sample.
