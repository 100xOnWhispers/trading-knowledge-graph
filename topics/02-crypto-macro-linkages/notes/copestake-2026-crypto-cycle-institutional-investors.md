---
title: "The Crypto Cycle and Institutional Investors"
authors: "Copestake, Alexander; Furceri, Davide; Terracciano, Tammaro"
year: 2026
venue: "Working paper, author version dated August 2026; earlier circulated as CEPR Discussion Paper 19810 (2024) and, with Natasha Che, as IMF Working Paper 23/163 'The Crypto Cycle and US Monetary Policy'"
url: "https://copestake.info/workingpaper/cryptofinance/CryptoFinance.pdf"
pdf: "sources/02-crypto-macro-linkages/copestake-2026-crypto-cycle-institutional-investors.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "daily"
tags: "crypto-factor, fomc, monetary-policy-shocks, institutional-share, funding-rate, equity-correlation, state-dependence"
---

## Key insight
A single common "crypto factor" explains about two thirds of the variance of major coin prices, and its link to equities and to US monetary policy is state-dependent. Fed tightening surprises lower the crypto factor, but only when institutional participation is high, and within those periods the effect is concentrated when the Bitcoin perpetual funding rate is high. The authors read this as a balance-sheet channel: levered investors who hold both equities and crypto lose risk-bearing capacity after a tightening.

## Method
- Dynamic factor model on daily prices of seven coins created before 2018 (Bitcoin, Ethereum, Binance Coin, Ripple, Cardano, Dogecoin, Tron) gives the crypto factor; analogous global equity factors (general, tech, small-cap, financial).
- Regression of daily changes in the crypto factor on changes in the equity factor interacted with the lagged institutional trading share.
- Difference-in-differences around the SEC spot Bitcoin ETF approval (10 January 2024): Bitcoin-equity correlation versus Ether-equity correlation.
- Local projections on FOMC days using high-frequency monetary-policy surprises of Acosta et al. (2025), with controls (lagged 10Y-2Y slope, dollar index, oil, gold, equity and crypto factors, VIX, previous surprise), Newey-West errors. Checked with a daily VAR and an event study of cumulative abnormal changes over plus or minus 7 trading days.
- Regime interactions through logistic weights F = 1/(1 + exp(-gamma z)): z is the lagged, median-standardized 30-day moving average of the institutional share (gamma = 3.0), or the lagged three-trading-day moving average of the annualized Binance BTC-USDT perpetual funding rate (gamma = 1.5).

## Data and sample
Daily data January 2018 to March 2026 (CryptoCompare prices). Institutional share from Chainalysis: share of on-chain volume in transfers of at least one million dollars, available through July 2025; Coinbase retail versus institutional volumes from quarterly filings as a second proxy. 71 FOMC events; 54 when the funding rate (available from September 2019) is included.

## Reported results
- The crypto factor explains 67 percent of the variance of crypto prices, against 20 percent for the global equity factor in Miranda-Agrippino and Rey. Bitcoin's average pairwise daily return correlation with other major coins is 60 percent.
- The crypto factor correlates most with the global tech and small-cap equity factors.
- A one-standard-deviation higher lagged institutional share roughly doubles the crypto-equity co-movement.
- Baseline: the crypto factor falls 0.41 standard deviations on impact per one-percentage-point surprise (90 percent interval -0.67 to -0.14), which the authors convert to roughly a 37 percent price decline. A mean-sized surprise is 0.026 percentage points, giving 0.011 standard deviations.
- High institutional regime: -1.04 standard deviations per percentage point on impact; low regime close to zero; the difference is significant.
- Event study by regime: decline concentrated where high institutional share coincides with high funding (CAR at day 0 of -0.054 standard deviations and at day 1 of -0.061, significant at the 90 percent level); the other three cells are flat.
- Comparable ECB and Bank of England surprises produce no negative response.

## Signal construction
A conditioning variable rather than a trade trigger: a "macro sensitivity" state.
1. Funding regime: three-trading-day moving average (nine 8-hour prints) of the annualized BTC-USDT perpetual funding rate on Binance, standardized around its sample median, passed through a logistic with gamma = 1.5. High when above 0.5.
2. Institutional regime: 30-day moving average of an institutional-participation proxy (large-transfer share on-chain, or an ETF and CME activity proxy), logistic with gamma = 3.0.
When both are high, weight Fed-related information (FOMC surprises, rates moves) more heavily and expect larger crypto beta to equities. Update daily.

## Relevance to SOL perpetuals at minutes to hours
The funding-rate conditioning is directly computable for a perpetuals bot and is the paper's most transferable idea. The estimates are daily and for a seven-coin factor that excludes SOL; Appendix correlations include Solana but its factor loading was not read. Intraday timing inside the FOMC window is not studied. Kalshi's own funding rate is too new to substitute for the Binance series; whether Kalshi funding carries the same information needs testing.

## Caveats
The regime-split results rest on 54 to 71 events, and the key event-study cell is significant only at the 90 percent level. The institutional share is a transaction-size proxy that also trends with price. Funding is itself a function of recent returns, so "high funding" partly means "after a rally". The post-2020 dummy cannot fully separate institutional entry from other changes in the same period. Authors are IMF staff and an IESE academic; no trading costs or strategy tests.
