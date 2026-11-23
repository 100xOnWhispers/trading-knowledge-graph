---
title: "The Cross-Section of Intraday and Overnight Returns"
authors: "Bogousslavsky, Vincent"
year: 2021
venue: "Journal of Financial Economics 141(1), 172-194 (December 2016 job-market-paper version read)"
url: "https://finance.unibocconi.eu/sites/default/files/files/media/attachments/The%2520Cross-Section%2520of%2520Intraday%2520and%2520Overnight%2520Returns_21Dec1620170112151545.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/bogousslavsky-2021-cross-section-intraday-overnight-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "hours"
tags: "intraday-returns, overnight-returns, anomalies, last-half-hour, close, liquidity, mispricing"
---

## Key insight
Risk premia and anomaly returns do not accrue evenly over the day. In thirty years of US half-hour data, size and illiquidity premia are earned in the last 30 minutes of trading, momentum is earned overnight, and "gradual" anomalies (betting-against-beta, profitability, idiosyncratic volatility, net issuance) earn steadily through the day but lose in the last half-hour and overnight. The timing points to trading around market closures, deteriorating liquidity before the close and mispricing at the open, as the drivers.

## Method
Long-short anomaly portfolios are formed monthly; their returns are computed for each of the 13 half-hour intraday intervals and the overnight interval, with alphas from interval-level regressions. Robustness uses first-half-hour volume-weighted average prices for the open, volume filters, long and short legs separately, and dummies for earnings and FOMC announcement days. An equilibrium model with infrequently rebalancing traders (from the author's 2016 Journal of Finance paper) is used to explain why premia concentrate where liquidity is expected to worsen.

## Data and sample
All US common stocks, ISSM and TAQ data, 1 October 1985 to 31 December 2015 (363 months), half-hour and overnight returns, nine anomalies. The version read is the December 2016 job-market draft; the published 2021 article may differ in details.

## Reported results
- Size and illiquidity premia are realized in the last half-hour; they tend to be negative in the first hour, but markedly so only on Mondays; elsewhere in the day they look like noise.
- The turnover of small stocks relative to large stocks spikes in the last half-hour.
- Momentum accrues overnight (consistent with Lou, Polk and Skouras); intraday it shows no clear pattern except negative returns at the end of the day. Past winners trade much more actively than losers at the open.
- Gradual anomalies earn positive, significant returns over most of the trading day but have large negative returns in the last half-hour and overnight, driven by the short leg overnight.
- Results hold with volume-weighted opening prices; the paper notes that spurious reversals plague TAQ midquote returns.

## Signal construction
Not a direct signal for a single instrument. It is used as a map of when different return sources are paid: for a relative-value book, hold liquidity-premium exposures into the close and momentum exposures across the closure. For a single asset the transferable construction is a per-bucket conditional mean of returns given the asset's "type" (illiquid versus liquid, recent winner versus loser).

## Relevance to SOL perpetuals at minutes to hours
The transferable hypothesis is that compensation for holding less liquid assets is paid just before predictable liquidity droughts. In crypto the candidates are the hours before the weekend, before the Asia-to-Europe lull, and before funding timestamps. SOL versus BTC is the natural "less liquid versus more liquid" pair on which to test whether relative returns concentrate ahead of low-liquidity windows. The momentum-overnight result suggests testing whether SOL trend returns accrue outside US hours.

## Caveats
Cross-sectional US equity evidence; no trading-cost analysis; the mechanism depends on a hard market close. The version read predates publication. The concentration of premia in one half-hour makes results sensitive to closing-price microstructure.
