---
title: "Fundamentals of Perpetual Futures"
authors: "He, Songrun; Manela, Asaf; Ross, Omri; von Wachter, Victor"
year: 2022
venue: "arXiv working paper 2212.06888 (v7, September 2026)"
url: "https://arxiv.org/pdf/2212.06888"
pdf: "sources/03-perp-pricing-funding/he-2022-fundamentals-perpetual-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "perpetual-futures, funding-rate, no-arbitrage, clamp, basis, limits-to-arbitrage, extrapolation"
---

## Key insight
With a funding rule that rises in the perp premium, the perp price is pinned to a constant multiple of spot by "random-maturity arbitrage" (a trade that pays off for sure at an uncertain but bounded time). With trading costs the price is only pinned inside a band. Empirically the premium on Binance sat far from the benchmark in 2020 and 2021, co-moved across coins, shrank about 22 percentage points a year, and widens after high past returns, which the authors read as extrapolative demand for leverage meeting limited arbitrage capital.

## Method
Funding function on Binance: `Phi(P) = k*P + clamp(i - k*P, -g, g)` with premium index `P = (F - S)/F`, `k = 1`, clamp width `g = 0.05%`, interest `i = 0.01%` per 8 hours. No-arbitrage price (Corollary 2): `F = k / (k + sgn(i - r)*g - r) * S`. With round-trip cost `C` the price lies in `[lambda_L*S - C, lambda_U*S + C]`. The deviation measure is `rho = k*(F - S)/F + sgn(i - r)*g - r`, annualised (times 3 times 365). Strategy: open spot-versus-perp when `rho` leaves the cost band, close when it returns to zero. Regressions of `rho` on a time trend, trailing 120-day return and volatility; an event study on Binance portfolio margin (April 2022); price impact of perp taker order imbalance by premium tercile.

## Data and sample
Binance spot and USDT perps, hourly, BTC, ETH, BNB, DOGE, ADA, January 2020 to 11 March 2024; funding at 00:00, 08:00, 16:00 GMT; Aave stablecoin rates as the risk-free rate; Kaiko order-book snapshots for costs.

## Reported results
- Mean absolute `rho` is 0.52 (BTC) to 0.90 (BNB) per year over the full sample. Mean `rho` falls from 0.69 before 2022 to 0.17 after for BTC, and from 0.92 to 0.16 for ETH.
- `rho` correlates 0.88 between BTC and ETH; funding rates correlate 0.86. Correlation between funding and same-coin spot return is small (0.08 to 0.23 in Table 5).
- Convergence strategy on BTC: Sharpe 11.65 with no fees, 3.35 at the retail fee tier, 3.27 after effective spreads. Using the no-clamp benchmark roughly halves the BTC Sharpe (6.06). A static long-spot short-perp carry earns Sharpe 2.24 on BTC.
- Cost bands for `rho`: plus or minus 53.2% (low fees), 114.3% (medium), 179.4% (high), annualised.
- Trend coefficient about -0.22 per year on absolute `rho`; trailing return enters positively (0.08 to 0.17, significant at 1%); volatility enters with a negative sign, against a simple risk-constraint story.
- Portfolio margin cut absolute deviation by 3.3 to 7.8 points from a base of 23 to 27.
- A one-point rise in taker imbalance moves the premium 0.031 bp when the premium is small (mean 2.47 bp) and 0.094 bp when it is large (mean 12.05 bp).

## Signal construction
Each hour (or faster): `P = (perp_mid - index)/perp_mid`; `rho = P + sgn(i - r)*g - r`, annualised; compare with the cost band for the bot's own fees. Also keep a cross-coin average of `rho` as a leveraged-demand gauge, and the trailing return as a predictor of where `rho` is heading.

## Relevance to SOL perpetuals at minutes to hours
The framework transfers to any clamp-style venue (the paper says Hyperliquid mirrors Binance). SOL is not in the sample. A directional bot cannot run the two-leg arbitrage, but `rho` on Binance or Hyperliquid SOL tells it whether longs are paying up, and the state-dependent impact result says order flow moves the premium most when it is already stretched. Kalshi's own funding parameters must be substituted before computing a band there.

## Caveats
Working paper. Sharpe ratios assume maker fees and hourly closes; post-2022 deviations are far smaller, so the edge has decayed. Exchange solvency is assumed. Earlier drafts used a no-clamp formula that [Ackerer et al.](ackerer-2023-perpetual-futures-pricing.md) criticised.
