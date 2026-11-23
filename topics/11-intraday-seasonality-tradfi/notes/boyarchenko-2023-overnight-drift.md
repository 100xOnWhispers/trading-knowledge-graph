---
title: "The Overnight Drift"
authors: "Boyarchenko, Nina; Larsen, Lars C.; Whelan, Paul"
year: 2023
venue: "Review of Financial Studies 36(9), 3502-3547 (Federal Reserve Bank of New York Staff Report 917, August 2022 revision read)"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/boyarchenko-2023-overnight-drift.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "futures"
horizon: "hours"
tags: "around-the-clock, overnight-drift, e-mini, order-imbalance, inventory-risk, reversal, european-open"
---

## Key insight
In a futures market that trades almost 24 hours, returns do not accrue evenly around the clock. S&P 500 E-mini returns were concentrated in one hour, 02:00 to 03:00 Eastern Time, when European markets open. The drift is a delayed reversal of order imbalance left at the previous US close: liquidity providers who absorbed late selling are paid when new traders arrive, and the payment is much larger after sell-offs than after rallies.

## Method
Hourly and 5-minute returns around the clock, with bootstrap distributions and Bonferroni and Benjamini-Yekutieli multiple-testing corrections across hours. The order-imbalance proxy is relative signed volume, RSV = signed volume / gross volume, measured over 15:15 to 16:15 ET. Evidence comes from sorts and high-frequency predictive regressions of overnight returns on closing RSV, double sorts with end-of-day VIX, an analysis in volume time, and daylight-saving natural experiments (Japan has no DST; US and Europe are out of sync for about three weeks a year). The framework is Grossman-Miller inventory risk with value-at-risk constrained dealers.

## Data and sample
Tick-by-tick trades and quotes for the E-mini S&P 500 contract (Refinitiv Datascope Select, complemented by CME data), January 1998 to December 2020. VIX tick data for conditioning.

## Reported results
- 02:00 to 03:00 ET averages 3.7% annualized (1.48 basis points per day); it is the only hour that stays significant after multiple-testing corrections in the full sample and subsamples.
- Positive in 20 of 23 years, significant in 17; significant on every weekday and in 9 of 12 months.
- Macro, monetary policy and earnings announcements do not explain it.
- Closing imbalances are followed by overnight reversals; reversals after sell-offs are much stronger than after rallies; near-zero imbalance gives near-zero reversal. Higher closing VIX amplifies the effect.
- In volume time it takes roughly 60,000 contracts to work off the end-of-day imbalance; 2009 to 2020 Asian-hours volume was 50 to 100 times lower than US-hours volume.
- When Tokyo's open shifts by an hour in US clock time, the predictability shifts with it.
- Long 02:00 to 03:00: Sharpe 1.1 before costs, -0.5 after bid-ask spreads. Long 01:30 to 03:30: 1.3 before, 0.3 after.

## Signal construction
At the end of the high-volume session compute RSV_close = (buy volume - sell volume) / total volume over the final hour, with trades signed by aggressor. Expected return over the following low-liquidity hours = -k * RSV_close, with a larger k when RSV_close < 0 and when implied volatility is high. Realize it in volume time: exit after cumulative volume reaches the typical amount needed to absorb the imbalance, or at the next major session open.

## Relevance to SOL perpetuals at minutes to hours
This is the closest template in the topic. Crypto has a daily liquidity cliff when US hours end and thin Asian hours follow. Aggressor-signed volume is available from Binance, Bybit, OKX and Hyperliquid trade feeds, so RSV over the last US hour is directly computable, and the asymmetric-reversal hypothesis can be tested against the Asia and Europe opens. The conditional, state-dependent form is what transfers, not the fixed clock hour.

## Caveats
One contract. The unconditional strategy does not survive spreads by the authors' own numbers. The authors' 2026 follow-up (noted separately) reports the drift vanished after 2021. In crypto, trade signing on perps is exact but imbalance is spread across venues.
