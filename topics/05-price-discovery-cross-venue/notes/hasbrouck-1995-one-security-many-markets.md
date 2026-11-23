---
title: "One Security, Many Markets: Determining the Contributions to Price Discovery"
authors: "Hasbrouck, Joel"
year: 1995
venue: "Journal of Finance"
url: "https://www.bauer.uh.edu/rsusmel/phd/hasbrouck95.pdf"
pdf: "sources/05-price-discovery-cross-venue/hasbrouck-1995-one-security-many-markets.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "05-price-discovery-cross-venue"
asset_class: "equities"
horizon: "seconds"
tags: "information-share, price-discovery, vecm, cointegration, fragmentation, methodology"
---

## Key insight
When the same (or an arbitrage-linked) security trades on several venues, the prices share one unobserved efficient price. Hasbrouck defines a venue's "information share" as the fraction of the variance of innovations in that common efficient price that is attributable to the venue's own price innovations. It is the standard yardstick used by nearly every crypto spot/perp/venue price-discovery study.

## Method
Prices from n venues are cointegrated with cointegrating vectors of the form (1, -1). Estimate a VAR/VECM on the price vector, invert it to a vector moving average, and take the common row psi of the long-run impact matrix. With residual covariance Omega, the variance of the efficient-price innovation is psi Omega psi'. If Omega is diagonal, the share of venue j is psi_j^2 Omega_jj / (psi Omega psi'). If residuals are contemporaneously correlated, use the Cholesky factor F of Omega: IS_j = ([psi F]_j)^2 / (psi Omega psi'). The result depends on ordering, so rotating a venue first and last gives upper and lower bounds. The paper stresses that the bounds tighten as the sampling interval shrinks, because contemporaneous correlation is mostly an artifact of time aggregation.

## Data and sample
NYSE TAQ quotes for the 30 Dow Jones stocks, August to October 1993. The system is four series (NYSE bid and offer, best non-NYSE bid and offer) sampled at one-second resolution with 60 one-second lags.

## Reported results
- Median NYSE information share: 92.7 percent. For only four stocks is the NYSE share below 90 percent.
- At one-second sampling the upper and lower bounds are "generally within 0.001 of each other".
- The cross-firm mean of information share minus volume market share is 7.0 percent (standard error 1.1 percent): the NYSE contributes more to price discovery than its volume share implies.
- The paper notes that effects resolved at one second "become smeared and indistinct with even a five-second time aggregation".

## Signal construction
Not a signal. It is a measurement tool for deciding which venue's price to treat as the leader. A bot would run it offline: collect synchronized mid-quotes for the SOL perp on Kalshi, Binance, Bybit, OKX, Hyperliquid and SOL spot on Coinbase, fit a VECM at the finest common clock, and report IS bounds per venue. Re-estimate on rolling windows (for example daily) to detect leadership drift.

## Relevance to SOL perpetuals at minutes to hours
The framework transfers directly: Kalshi SOL perp, offshore SOL perps and SOL spot are one security in Hasbrouck's sense. The practical lesson is to sample finely. With 1-minute bars, most cross-venue adjustment is already complete and the bounds will be too wide to be informative. A dominant IS for Binance would justify computing directional features on Binance data and treating the Kalshi price as a lagged, noisier copy.

## Caveats
IS measures a mix of speed and low noise (see the Putnins note), so a quiet venue can score highly without moving first. Bounds can be very wide when venues are sampled coarsely or one feed is slow. The empirical sample is 1993 US equities; nothing in the paper speaks to crypto directly. The stored PDF is a JSTOR scan hosted on a university course page.
