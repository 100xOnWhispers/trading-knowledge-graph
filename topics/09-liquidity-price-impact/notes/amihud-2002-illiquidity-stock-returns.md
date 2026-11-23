---
title: "Illiquidity and stock returns: cross-section and time-series effects"
authors: "Amihud, Yakov"
year: 2002
venue: "Journal of Financial Markets (read as NYU Stern working paper FIN-00-041, August 2000 version)"
url: "https://archive.nyu.edu/jspui/bitstream/2451/26706/2/FIN-00-041.pdf"
pdf: "sources/09-liquidity-price-impact/amihud-2002-illiquidity-stock-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "09-liquidity-price-impact"
asset_class: "equities"
horizon: "daily"
tags: "amihud, illiquidity-ratio, price-impact, liquidity-premium, flight-to-liquidity"
---

## Key insight
Amihud defines illiquidity as the average ratio of absolute return to dollar volume, a price-impact proxy that needs only bar data. Expected market illiquidity raises expected excess returns, while an unexpected rise in illiquidity lowers prices at the same time. Both effects are stronger for small, illiquid stocks, which the paper reads as a "flight to liquidity".

## Method
The measure for stock i in year y is

ILLIQ_iy = (1/D_iy) * sum over days t of |R_iyt| / VOLD_iyt

where R is the daily return and VOLD the daily dollar volume. Market illiquidity AILLIQ_y is the cross-sectional average. Cross-section: monthly Fama-MacBeth regressions of stock returns on mean-adjusted ILLIQ, beta, size, volatility, dividend yield and past returns. Time series: log market illiquidity is modeled as an AR(1); the fitted value is "expected" illiquidity and the residual is "unexpected" illiquidity. Market excess return is regressed on both.

## Data and sample
NYSE stocks, 1963 to 1997, daily and monthly CRSP data. The cross-section tests cover 408 months (1964 to 1997). The copy read is the August 2000 working paper; the published 2002 article may differ in detail.

## Reported results
- Cross-section: the mean coefficient on mean-adjusted ILLIQ is 0.163 (t = 6.90), median 0.141, positive in 275 of 408 months. Excluding January it is 0.131 (t = 5.73).
- Annual log market illiquidity is persistent: AR(1) slope 0.764 (t = 5.89), R-squared 0.53; the bias-corrected slope is 0.869.
- The paper states that both time-series hypotheses are supported: expected illiquidity has a positive effect on ex ante excess return, and unexpected illiquidity has a negative effect on the contemporaneous return. I did not extract the coefficient values.
- Effects are stronger for small-firm portfolios.

## Signal construction
Rolling Amihud ratio on bars of length b over a window of W bars:

ILLIQ_t = mean over the last W bars of |r_i| / dollar_volume_i

Inputs: SOL perp trades or 1-minute bars from the reference venue (Binance, Bybit, OKX, Hyperliquid). Use it as a ratio to its own trailing median, and compare the same clock hour across days, because volume is strongly periodic. Use it as a state variable for position sizing and for an impact-cost estimate, not as a direction signal. A jump in the ratio relative to its expectation is the intraday analogue of Amihud's "unexpected illiquidity".

## Relevance to SOL perpetuals at minutes to hours
The formula transfers directly. The evidence does not: Amihud tests monthly and annual equity returns, and the "illiquidity premium" is a slow risk-premium result. On crypto, Brauneis et al. (2021) find the ratio does not track time variation in spreads or price impact, because volume and trading costs rise together there; it does rank venues by liquidity level. So on SOL the ratio is better for comparing Kalshi against Binance than for timing. The hypothesis that an unexpected illiquidity shock coincides with negative returns is worth testing at the hourly horizon on SOL.

## Caveats
Equity data ending in 1997. The ratio mixes volatility and volume, so it rises mechanically in volatile periods. It is undefined for zero-volume bars, which will occur on a thin venue such as Kalshi. The premium result is a low-frequency finding and gives no intraday edge by itself.
