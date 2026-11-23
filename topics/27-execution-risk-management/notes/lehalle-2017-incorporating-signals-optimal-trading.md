---
title: "Incorporating Signals into Optimal Trading"
authors: "Lehalle, Charles-Albert; Neuman, Eyal"
year: 2017
venue: "arXiv preprint 1704.00847 (version 3, June 2018)"
url: "https://arxiv.org/pdf/1704.00847"
pdf: "sources/27-execution-risk-management/lehalle-2017-incorporating-signals-optimal-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "seconds"
tags: "signal-aware-execution, order-book-imbalance, transient-impact, optimal-execution, market-participants"
---

## Key insight
A short-term price predictor can be built into the optimal execution problem, and when it is, the schedule speeds up when the signal says price is about to move against the order and slows or pauses when it is favourable. A mean-reverting signal and decaying market impact push short-term prices in opposite directions, so the two must be handled together. Labelled trade data show that fast participants already condition their order type on order book imbalance.

## Method
Theory: a Markovian signal is added to the transient-impact execution framework of Gatheral, Schied and Slynko; existence and uniqueness of the optimal strategy are proved. For an Ornstein-Uhlenbeck signal with exponentially decaying impact the optimal strategy is derived explicitly and includes singular (block) trades. In the limit where transient impact becomes instantaneous the strategy becomes continuous and matches the Cartea and Jaimungal framework, with an inventory penalty `phi` and a terminal penalty.

Empirics: descriptive statistics of top-of-book imbalance just before trades, split by participant class and order type, and plots relating imbalance to subsequent price moves and showing its mean reversion.

## Data and sample
13 liquid, large-tick stocks on NASDAQ OMX Stockholm, January to September 2013 (180 trading days), tick-by-tick trades with buyer and seller identities, matched to order book recordings from Capital Fund Management. Participants grouped into global investment banks, institutional brokers, high-frequency market makers and high-frequency proprietary traders.

## Reported results
Average imbalance before a trade, signed so that positive means the imbalance favours the trade's direction ("average stock", their Table 3):

| Class | Limit orders | Market orders | Share by limit orders |
|---|---|---|---|
| Global banks | -0.41 | 0.56 | 48.2% |
| HF market makers | -0.31 | 0.62 | 73.0% |
| HF proprietary traders | -0.37 | 0.63 | 47.2% |
| Institutional brokers | -0.56 | 0.33 | 33.6% |

- High-frequency participants take liquidity on the weak side of the book when imbalance averages about 0.60 in their favour.
- Institutional brokers use market orders most (66.4%) and with the least favourable imbalance.
- Everyone's passive fills occur on average when imbalance was against them, which is adverse selection of resting orders.
- Banks are involved in 58% of trades, high-frequency firms in 32%, institutional brokers in 10%.

## Signal construction
Imbalance at the touch: `(bid_size - ask_size) / (bid_size + ask_size)`, updated on every book change. Fit an Ornstein-Uhlenbeck process to it (mean-reversion speed and volatility) and estimate the drift it implies for the mid price over the next seconds. Execution rule in the continuous limit: baseline schedule from the inventory penalty, plus a term proportional to the discounted expected future signal. In practice: cross the spread when imbalance is strongly in the trade's direction and the order is behind schedule; rest passively otherwise.

## Relevance to SOL perpetuals at minutes to hours
The bot's directional decision is made at minutes to hours, but each entry and exit is an execution problem lasting seconds to minutes, and that is where this applies. Imbalance on the Kalshi book may be less informative than imbalance on Binance or Coinbase for the same instant, since price discovery is elsewhere; the natural test is to use reference-venue imbalance as the execution signal. The adverse-selection pattern for passive fills is likely to hold and is measured directly on a crypto perpetual in the Albers et al. note.

## Caveats
The empirical section is descriptive: averages and plots, no out-of-sample trading test and no costs. 2013 Nordic equities with large ticks; SOL perps on a small tick behave differently. Signal dynamics are assumed known. One author is employed by the firm that supplied the order book data.
