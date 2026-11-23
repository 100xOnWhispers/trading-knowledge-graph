---
title: "Crypto Wash Trading"
authors: "Cong, Lin William; Li, Xi; Tang, Ke; Yang, Yang"
year: 2023
venue: "Management Science 69(11), 6427-6454 (read as arXiv:2108.10984, July 2021 draft)"
url: "https://arxiv.org/abs/2108.10984"
pdf: "sources/31-rl-evolutionary-second-pass/cong-2023-crypto-wash-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "31-rl-evolutionary-second-pass"
asset_class: "crypto"
horizon: "n/a"
tags: "data-quality, wash-trading, volume, benford, trade-size-clustering, power-law, exchanges, training-data"
---

## Key insight
Trade records from unregulated crypto exchanges in 2019 fail statistical regularities that hold in every regulated market, and the authors estimate that over 70% of reported volume on those exchanges was fabricated. Regulated exchanges pass every test. For any learning method this means volume, trade-count and trade-size features from such venues are contaminated at the source, and the contamination differs by venue and over time.

## Method
Three tests applied to each exchange's trade tape, per coin:
- First significant digit of trade size against Benford's law.
- Trade-size clustering: genuine traders favour round sizes, so the histogram should show spikes at multiples of 100, 500, 1,000 and so on base units. Machine-generated wash trades tend to be unrounded.
- Tail of the trade-size distribution: fit a power law and check the exponent against the range seen in traditional markets.

Quantification: take the ratio of unrounded to rounded trades on regulated exchanges as the benchmark for authentic trading; unrounded volume above that ratio on an unregulated exchange is counted as wash volume. A second approach compares actual trade-size distributions with counterfactual ones. Further regressions relate estimated wash trading to exchange rank, age, user base, returns and volatility.

## Data and sample
Trade-level data (id, timestamp, price, amount, pair) from 29 exchanges collected by TokenInsight, 9 July 2019 to 3 November 2019, for BTC, ETH, LTC and XRP. Three exchanges hold a New York BitLicense and are classed as regulated; 10 unregulated exchanges with high web traffic are "Tier-1" and 16 are "Tier-2". Exchanges are anonymized by label in most tables; the sample is stated to include Binance, Coinbase and Huobi.

## Reported results
- Regulated exchanges show the expected patterns in all tests. Tier-1 unregulated exchanges fail about 20.6% of tests on average and Tier-2 about 61.8%.
- Wash trading averages 77.5% of volume across unregulated exchanges (median 79.1%); 53.4% for Tier-1 and 81.7% for Tier-2; about 61% after controlling for exchange characteristics.
- The counterfactual-distribution approach gives much lower figures: 16.3% on average, 12.9% for Tier-1 and 18.5% for Tier-2.
- An exchange with 70% wash trading gains 46 places in volume ranking.
- Wash trading is positively related to short-term prices on the exchange, positively predicted by returns and negatively by volatility.
- Some Tier-1 exchanges behave much like regulated ones.

## Signal construction
Not a signal. Three venue-quality diagnostics a data pipeline can run on any trade tape before using it: Benford fit of first digits of trade size, share of volume at round sizes, and the tail exponent of trade size. Run them per venue and per month, and treat a venue-month that fails as unusable for volume-based features.

## Relevance to SOL perpetuals at minutes to hours
A model trained on volume or signed-flow features from an offshore venue learns that venue's reporting behaviour as well as the market's. Because wash activity responds to returns and volatility, the contamination is correlated with the target, which is the dangerous kind. Prefer features from venues that pass the diagnostics, cross-check volume across venues, and use price-based or book-based features where volume is doubtful. The study covers spot trades; perps are not tested.

## Caveats
Data are from four months of 2019, before the growth of perpetuals and before several ranking sites changed methodology in response to this paper. The two quantification methods disagree by a factor of four or more, so the headline percentage is model-dependent. Exchange identities are masked. Nothing here measures wash trading on Binance, Bybit or OKX perps today or on Solana-based venues.
