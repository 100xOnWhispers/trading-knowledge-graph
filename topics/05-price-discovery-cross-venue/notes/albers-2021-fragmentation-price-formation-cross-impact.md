---
title: "Fragmentation, Price Formation, and Cross-Impact in Bitcoin Markets"
authors: "Albers, Jakob; Cucuringu, Mihai; Howison, Sam; Shestopaloff, Alexander Y."
year: 2021
venue: "arXiv preprint 2108.09750 (later published in Applied Mathematical Finance 28(5))"
url: "https://arxiv.org/pdf/2108.09750"
pdf: "sources/05-price-discovery-cross-venue/albers-2021-fragmentation-price-formation-cross-impact.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "tick"
tags: "lead-lag, cross-impact, machine-learning, lasso, linear-models, perpetuals, fees, binance, bybit, live-trading"
---

## Key insight
Using order book and trade features from 14 liquid bitcoin spot, perpetual and futures markets, simple linear models explain 10% to 37% of the variation in 500 ms-ahead returns, with the most lagging venues the most predictable. Predictability does not map to taker profit: a venue's tendency to lead or lag is tied to its fee regime, and only venues that lag more than their fees imply are profitable to hit. This is the most direct evidence on how to predict a lagging venue from leaders.

## Method
Five features per market (two order book imbalance terms, including a custom depth-weighted version; trade-flow imbalance; past returns; and divergence of the market's price from the cross-market mean, over short lookbacks from 50 ms upward), giving 70 features across 14 markets. A leader-lagger network is built from pairwise regressions of market i's future return on market j's five features, compared by R-squared. Three supervised learners predict each market's 500 ms and 1,000 ms return: OLS on all 70 features, LASSO over several penalties, and OLS after a dimension-reduction ("meta features") step, plus a greedy nonlinear feature transform. Evaluation is a walk-forward taker strategy with PnL (1) before fees, (2) at default taker fees, (3) at the lowest VIP fees, and a live maker strategy on Bybit.

## Data and sample
Order book and trade data at 50 ms resolution for the top 14 BTC markets by volume in February 2021 (Binance, Huobi, OKEx, Bybit, BitMEX, Deribit, FTX; spot, perpetuals and quarterly futures). Training February 22-27, 2021; test February 28 and March 1, 2021. Live experiment: roughly five days, 1.5 million USD notional.

## Reported results
- Binance and Huobi perpetuals and quarterly futures are the strongest leaders; Bybit and FTX perpetuals are strong laggards.
- R-squared up to 36% on the most lagging markets and above 10% even on the most leading market. Out-of-sample 500 ms R-squared averages about 91% of in-sample.
- OLS on all features gives the highest R-squared; LASSO with about half the features retained is similar.
- All PnL figures at default taker fees are negative. At VIP fees FTX is best and even the Binance USDT perpetual is positive; Deribit and BitMEX are worst.
- High taker fee with high maker rebate predisposes a market to lag; low fees to lead.
- The live maker strategy earned about one basis point of alpha over a naive benchmark.

## Signal construction
For target venue k, every 50-100 ms compute for each leader venue j: trade-flow imbalance over 500 ms, order book imbalance, 500 ms and 1 s past returns, and price_k minus the cross-venue mean price (mean divergence). Fit a ridge/LASSO/OLS regression of the target's next 500 ms to few-second mid return on these features, refit daily. Trade only when the predicted move exceeds taker fee plus half-spread; otherwise use the prediction to skew passive quotes.

## Relevance to SOL perpetuals at minutes to hours
Kalshi is the archetypal lagger, so cross-venue features should have high R-squared for its next-second return. The paper's warning applies with force: Kalshi's fees and spread, not predictability, will decide whether a taker can monetize the lag. The mean-divergence feature also works as a slower (seconds to minutes) reversion signal toward the cross-venue consensus. The feature set should be rebuilt for SOL with Binance, Bybit, OKX, Hyperliquid and Coinbase as leaders.

## Caveats
One asset, about one week of data in a single bull-market month; FTX and several fee schedules no longer exist. Sub-second horizons demand colocation-grade latency. Taker backtest assumes top-of-book fills. The live test is short and on one venue. I read the arXiv version, not the journal version.
