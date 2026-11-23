---
title: "Thomas DeMark's Sequential (TD SEQUENTIAL) using artificial intelligence"
authors: "Marchukajtes, Mihail"
year: 2017
venue: "MQL5 Articles (MetaQuotes), article 2773"
url: "https://www.mql5.com/en/articles/2773"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "fx"
horizon: "minutes"
tags: "machine-learning, meta-labeling, td-sequential, intraday, neural-network, signal-filter"
---

## Key insight
The only source found that pairs a DeMark signal with a learned model, and it does so on intraday bars. The design idea is sound and reusable: let the rule generate candidate entries, and train a classifier on context features to decide which candidates to take. The execution is not credible evidence: about 30 training examples, no reported statistics, and proprietary inputs.

## Method
- Signal generator: only the first stage of Sequential (setup and intersection), in an "adaptive" form. The count is not fixed at nine; a signal fires when the run of qualifying closes ends.
- Labels: each historical signal is labeled 1 if it made a profit and 0 if it lost.
- Features: values on the signal bar from volume and delta indicators of a subscription service (ClusterDelta), plus a daily "market context" with nine states built from the day's change in futures volume and open interest, entered by hand from the CME daily bulletin.
- Model: Reshetov's optimizer produces two nonlinear functions used as a committee. Both yes: take the signal. Both no: skip. Disagreement: "not sure", handled as a third class.
- Separate models for buy and sell signals. The trader also checks each day whether the model is "oriented" correctly and inverts its output if not.
- Training depth: about 30 signals, roughly 8 to 10 days of 15-minute data. Expected useful life: about one third of the training span, so about 10 signals.

## Data and sample
British pound against the US dollar, with CME futures volume and open interest as context, on 5-minute and 15-minute bars. The demonstration covers 4 days; the dates are not stated. The article says Sequential produces 2 to 5 signals a day on 15-minute bars.

## Reported results
No win rate, profit factor, drawdown or equity statistics. Results appear only as chart screenshots that the author describes as "not impressive" before orientation and better after. The author states the article is "purely methodological", that results may not reproduce on another broker's quotes, and that a target is an error rate under 20% over 10 to 15 signals.

## Signal construction
The reusable pattern for a bot:
1. Generate events from a DeMark rule (setup 9, perfected 9, countdown 13, TDST break).
2. For each event, record features known at that bar: order-flow imbalance, open-interest change, funding, volatility state, distance to TDST, count length.
3. Label by forward return net of costs over a fixed horizon.
4. Fit a regularized classifier and trade only events above a probability threshold.
This is the approach usually called meta-labeling. The sample must be thousands of events, not thirty.

## Relevance to SOL perpetuals at minutes to hours
The horizon matches. On 5-minute to 15-minute SOL bars a setup completes often enough to build a large labeled set within months, and the context features the author wanted (volume delta, open interest) are freely available for crypto perpetuals from Binance, Bybit, OKX and Hyperliquid. That removes the article's main practical obstacle.

## Caveats
Thirty training samples with a daily manual "orientation" step is curve fitting. The article's claim that the optimizer's network "cannot be overtrained" should not be accepted for any flexible model. Inputs are paywalled, so the work cannot be reproduced. No reinforcement-learning or evolutionary study of DeMark indicators was found in this session's searches.
