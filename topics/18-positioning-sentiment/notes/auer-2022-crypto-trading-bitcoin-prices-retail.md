---
title: "Crypto trading and Bitcoin prices: evidence from a new database of retail adoption"
authors: "Auer, Raphael; Cornelli, Giulio; Doerr, Sebastian; Frost, Jon; Gambacorta, Leonardo"
year: 2022
venue: "BIS Working Papers No 1049 (revised version)"
url: "https://www.bis.org/publ/work1049.htm"
pdf: "sources/18-positioning-sentiment/auer-2022-crypto-trading-bitcoin-prices-retail.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "multi-day"
tags: "retail-adoption, app-downloads, whales-vs-retail, feedback-trading, retail-losses, bis"
---

## Key insight
Retail entry into crypto follows price. A rising Bitcoin price is followed by more exchange-app users, especially young men, and while small holders add to positions during price rises the largest holders sell. The authors estimate that roughly three-quarters of app users had lost money on Bitcoin by late 2022. Retail participation is a lagging, price-chasing variable, and large holders are on the other side.

## Method
A country-day panel of crypto exchange app usage is related to Bitcoin price and controls, with monthly panel regressions on log daily active users and a panel VAR. Causality from price to entry is supported by an exogenous price shock: the January 2022 unrest in Kazakhstan, which disrupted mining and coincided with a fall of almost 20% in Bitcoin, studied excluding Kazakh users. Holder behaviour comes from blockchain balances bucketed by wallet size: addresses below 1 BTC proxy for retail; miners and large wallets proxy for whales. Profit and loss is simulated by assuming each new user buys USD 100 of Bitcoin in the month of first download and each month after.

## Data and sample
Sensor Tower app data for more than 200 crypto exchange apps across 95 countries, 2015 to 2022 (187 of 296 exchanges matched). Price data from CCData. Blockchain holdings by wallet size.

## Reported results
- Monthly average daily active users rise with the Bitcoin price; the Kazakhstan episode shows the price decline significantly dampened entry of new users.
- 40% of users are men under 35, and this group is more sensitive to price changes.
- Small-balance holdings carry a positive and significant price coefficient; miner (whale) holdings carry a negative one. Small investors behave more procyclically in high-volatility periods.
- 73% of users downloaded their app when Bitcoin was above USD 20,000, which was above the October 2022 price. Under the USD 100 per month assumption, the introduction says over 75% of users would have lost money and the body text gives 81%; the median investor would have lost 48% of USD 900 invested.
- Around the Terra/Luna and FTX episodes (replicating Cornelli et al. 2023), owners of large wallets reduced Bitcoin holdings in the days after the shocks while medium and especially small holders increased them.

## Signal construction
Inputs: daily app download or active-user estimates for major exchange apps (commercial data), or public proxies such as app-store rank. Compute a z-score of new-user growth against a trailing window. Per the paper this is a lagging indicator of price, so its use is as a crowding and late-cycle gauge: extreme retail inflow combined with falling large-holder balances marks distribution. Update daily at best.

## Relevance to SOL perpetuals at minutes to hours
Too slow for entries. It supports two design choices: treat retail-heavy measures as trend-following and late, and give more weight to large-account positioning when the two diverge. The whale-versus-retail divergence can be approximated faster with Binance top-trader versus global account ratios and Hyperliquid wallet-size cohorts, which is where the idea should be re-tested on SOL.

## Caveats
Monthly and daily app data, Bitcoin only. The loss simulation rests on a uniform dollar-cost-averaging assumption and a price snapshot near the 2022 low; a later evaluation date would change the losing share. Miners as the whale proxy sell for operating reasons, not only on views. Whale selling into strength does not by itself establish that whales predict returns.
