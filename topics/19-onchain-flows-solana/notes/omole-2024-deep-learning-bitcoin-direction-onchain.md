---
title: "Deep learning for Bitcoin price direction prediction: models and trading strategies empirically compared"
authors: "Omole; Enke (first names not confirmed)"
year: 2024
venue: "Financial Innovation, 10"
url: "https://api.crossref.org/works/10.1186/s40854-024-00643-1"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "daily"
tags: "machine-learning, deep-learning, cnn-lstm, genetic-algorithm, boruta, feature-selection, on-chain-metrics, bitcoin, backtest"
---

## Key insight
A deep-learning study that predicts Bitcoin price direction from on-chain data and uses a genetic algorithm as one of three feature-selection methods. Boruta selection combined with a CNN-LSTM is reported as the best pairing, at 82.44 percent directional accuracy, and a long-short backtest is reported to return 6,654 percent a year. The paper is the clearest example in this topic of an evolutionary method applied to on-chain features, and also of results too good to accept without replication.

## Method
Only the publisher's abstract (via the Crossref metadata record) was read; the publisher pages redirected to a login and the open-access PDF could not be downloaded in this session. The record lists the authors by surname (Omole, Enke), volume 10 and an issue date of 5 August 2024. Per the abstract:
- Models compared: CNN-LSTM, a long- and short-term time-series network (LSTNet), a temporal convolutional network, and ARIMA as benchmark.
- Inputs: on-chain data for Bitcoin.
- Feature selection, to deal with a large feature set: Boruta, a genetic algorithm, and LightGBM importance.
- Evaluation: directional accuracy, then backtests of three trading strategies under three investment positions.

## Data and sample
Bitcoin on-chain data. Vendor, number of features, sample period and frequency were not confirmed from the abstract; the horizon in the front matter is assumed daily and is not confirmed.

## Reported results
From the abstract only:
- Boruta plus CNN-LSTM "consistently outperforms other combinations", with accuracy of 82.44 percent.
- The long-and-short buy-and-sell approach generated an annual return of 6,654 percent when driven by the higher-accuracy predictions.
- The authors conclude there is evidence of potential profitability of predictive models in Bitcoin trading.
How the genetic algorithm performed relative to Boruta is not stated beyond Boruta being best.

## Signal construction
Not a signal. A pipeline pattern:
- Start from a wide panel of on-chain metrics.
- Reduce it with a wrapper or evolutionary search (Boruta's shadow-feature test, or a genetic algorithm over feature subsets with validation accuracy as fitness).
- Feed the survivors to a sequence model that outputs up or down for the next bar.
For a bot, the selection step must sit inside the walk-forward loop; selecting features once on the full sample leaks the future.

## Relevance to SOL perpetuals at minutes to hours
Method only. It shows that evolutionary feature selection over on-chain metrics has been tried and was not the winner against Boruta in the authors' comparison. Nothing is known from the abstract about intraday horizons or about SOL. Together with [demosthenous-2024](demosthenous-2024-onchain-macro-data-source-diversity.md) and [huang-2023](huang-2023-reinforcement-learning-onchain-portfolio-management.md), it represents a machine-learning literature on on-chain data that is daily, Bitcoin-centred and thin on realistic evaluation.

## Caveats
Abstract-only. Directional accuracy above 80 percent on daily Bitcoin returns and an annual return of several thousand percent are far outside what liquid markets permit and usually indicate leakage: on-chain metrics that embed the same day's price (market-value ratios, realised-price measures), features selected on the test period, or vendor data revised after the fact. Costs, shorting constraints and funding are not mentioned in the abstract. Treat the performance figures as unverified until the full text and data handling are checked.
