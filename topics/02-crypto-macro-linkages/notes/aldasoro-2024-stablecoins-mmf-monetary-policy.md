---
title: "Stablecoins, money market funds and monetary policy"
authors: "Aldasoro, Inaki; Cornelli, Giulio; Ferrari Minesso, Massimo; Gambacorta, Leonardo; Habib, Maurizio Michael"
year: 2024
venue: "ECB Working Paper Series No 2987 (also issued as BIS Working Paper No 1219)"
url: "https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2987~1919e51abf.en.pdf"
pdf: "sources/02-crypto-macro-linkages/aldasoro-2024-stablecoins-mmf-monetary-policy.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "multi-day"
tags: "stablecoin-supply, monetary-policy-shocks, local-projections, crypto-shocks, elastic-net, liquidity"
---

## Key insight
Stablecoin market capitalization is driven by US monetary policy and by crypto prices, not the other way round. After a contractionary Fed surprise, stablecoin capitalization falls persistently over about three months while prime money market fund assets rise. Negative crypto shocks also shrink stablecoins but leave traditional markets untouched. The authors conclude that dollar monetary policy is the main link between traditional and crypto markets.

## Method
- Crypto shocks: residuals from an elastic-net regression of Bloomberg Galaxy Crypto Index returns on contemporaneous and lagged financial variables (change in the 3-month yield, log gold, Citi economic surprise index, term spread, log VIX, oil, dollar NEER, S&P 500), lagged index returns and year dummies. The elastic net selects predictors; the unexplained part is the shock.
- Monetary policy shocks: change in the 3-month fed funds futures rate from 10 minutes before to 20 minutes after FOMC announcements (Gurkaynak-Sack-Swanson).
- Local projections (Jorda 2005) of log stablecoin capitalization, money market fund assets and yields, and financial controls on each shock, horizons up to 13 weeks, with 68 and 90 percent bands. The monetary shock is scaled so that Bitcoin falls 10 percent, about one standard deviation.

## Data and sample
Weekly, January 2019 to July 2024. Stablecoin circulating capitalization for Tether, USDC and Dai from Messari (as of July 2024 these three were about USD 150 billion and 95 percent of USD-pegged stablecoins). Bitcoin prices from CCData. Money market fund data from iMoneyNet. Macro-financial series from Haver.

## Reported results
- After a contractionary monetary shock of that size, stablecoin capitalization drops by around 10 percentage points after three months; the decline is significant and persistent and is driven by Tether and USDC.
- The stablecoin decline after a monetary shock is "much larger" than after a crypto shock that moves Bitcoin by a similar amount.
- Prime money market fund assets and yields rise after the monetary shock; non-prime funds do not react within 13 weeks.
- Crypto shocks have no effect on money market funds or traditional financial variables.
- The crypto shock series falls at the May 2021 China crackdown, the May 2022 TerraUSD collapse and the November 2022 FTX failure.
- The stock market response to monetary shocks is weak in this sample, which the authors attribute to resilient risk-taking in the period.

## Signal construction
Not an intraday signal. It tells the bot how to interpret stablecoin supply:
- Aggregate stablecoin capitalization growth (for example the 4- to 13-week log change in USDT plus USDC supply) is a slow regime variable that responds to monetary conditions and crypto prices with a lag of weeks. Use it as a liquidity-regime feature updated daily or weekly, not as a lead indicator.
- The elastic-net residual method is a reusable recipe for a "crypto-specific shock" series: regress crypto index returns on equity, rates, dollar, gold, oil and VIX moves and keep the residual. At intraday frequency the same decomposition separates macro-driven from crypto-native moves.

## Relevance to SOL perpetuals at minutes to hours
Practitioners often present stablecoin supply growth as "dry powder" that leads prices. This paper's evidence points the other way: supply follows monetary shocks and crypto prices. For a minutes-to-hours bot that makes it context for position sizing and directional bias at most. The decomposition into macro and crypto-native components is the more actionable idea, since a SOL move during a macro-driven episode should be read against equity futures while a crypto-native one should not. Individual large mints or burns and exchange stablecoin flows at high frequency are not studied here.

## Caveats
Weekly data, 5.5 years, a period with one tightening cycle and several crypto crises, so few independent monetary episodes. Crypto-shock identification assumes financial markets do not react within the week to crypto. Scaling the shock to a 10 percent Bitcoin fall means the magnitude is relative, not per basis point. Central-bank working paper, not peer reviewed in the version read. No direct test of stablecoin supply as a predictor of crypto returns.
