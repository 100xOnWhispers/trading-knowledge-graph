---
title: "Detecting Toxic Flow"
authors: "Cartea, Alvaro; Duran-Martin, Gerardo; Sanchez-Betancourt, Leandro"
year: 2023
venue: "arXiv 2312.05827 (v1 December 2023, v2 January 2026; EconPapers lists a 2026 Quantitative Finance version, not opened in this session)"
url: "https://arxiv.org/pdf/2312.05827"
pdf: "sources/08-trade-flow-toxicity/cartea-2023-detecting-toxic-flow.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "fx"
horizon: "seconds"
tags: "toxic-flow, machine-learning, online-learning, bayesian-neural-network, adverse-selection, internalisation"
---

## Key insight
Toxicity can be defined and predicted per trade instead of per market. A trade is toxic if the client could unwind it at a profit within a horizon of G seconds, which is a loss for the liquidity provider. A neural network updated online after every trade with a Bayesian rule (PULSE) predicts this label better than logistic regression, random forests and a running-frequency estimator, and a broker who hedges the trades predicted toxic keeps more PnL. Toxic does not mean informed: random price moves make many uninformed trades toxic at longer horizons.

## Method
Label y = 1 if, within G seconds after the fill, the best quotes move so that the client could close at a profit, for G in {1, 5, 10, 20, 30, 40, 50, 60, 70} seconds. Features (183 per client): eight statistics of recent activity (midprice volatility, the client's trade count, number of best-quote updates, midprice return, average transformed best bid and ask volume, average spread, average top-of-book imbalance) measured over seven intervals on three clocks (time, transaction, volume), plus fifteen state features such as client cash and inventory, order size, spread and imbalance at arrival, and the client's past share of toxic trades. PULSE splits the network's last layer from the feature layers, projects the feature-layer parameters onto a low-dimensional affine subspace, and updates a Gaussian posterior recursively with an extended-Kalman-style formula; one update and prediction takes under one millisecond. The strategy internalises a trade when predicted toxicity is at or below a cutoff and externalises it otherwise.

## Data and sample
Proprietary EUR/USD data from LMAX Broker (client trades with identifiers, six clients analysed) and LMAX Exchange (order book), 28 June to 21 October 2022. Models are initialised on 28 June to 31 July and deployed on 1 August to 21 October.

## Reported results
- Share of toxic trades: 6.6% at a 1-second horizon, rising to roughly 70% at one minute.
- PULSE has the highest average daily AUC of the four methods at every horizon; AUC for PULSE and random forest falls as the horizon lengthens, and PULSE's advantage over random forest grows. The running-frequency estimator stays near 0.5; logistic regression is unstable.
- One universal model with client-specific features beats one model per client.
- Removing client identity features (cash, inventory, recent activity) makes PULSE "deteriorate substantially".
- PULSE gives the best combination of PnL and avoided loss across horizons.

## Signal construction
Adapted to a taker bot the label flips: for each of the bot's own candidate entries, y = 1 if the entry could be closed at a profit within G. Online features per decision: volatility, trade counts, quote-update counts, returns, spread and top-of-book imbalance over several windows on time, trade and volume clocks. Train a small network or boosted model and update it online after each resolved label. For passive entries on Kalshi the original definition applies: estimate the probability that a resting order, once filled, is adversely selected within G seconds, and pull quotes when it is high.

## Relevance to SOL perpetuals at minutes to hours
The useful transfers are the per-trade, horizon-specific definition of toxicity, the three-clock feature design, and online updating, which fits non-stationary crypto flow. The strongest features here were client identities, which no public crypto feed offers; Hyperliquid's public per-address fills are the closest analogue and would need separate testing. Horizons of 1 to 70 seconds are shorter than the bot's, and the fall in AUC with horizon suggests flow-toxicity prediction weakens quickly toward minutes.

## Caveats
One currency pair, one broker, six clients, under four months. Proprietary data, so no replication. FX dealer-client structure differs from an anonymous perp order book. The paper reports classification and broker PnL, not a directional strategy. The journal version was not read.
