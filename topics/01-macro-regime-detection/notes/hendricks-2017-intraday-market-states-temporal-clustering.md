---
title: "Detecting intraday financial market states using temporal clustering"
authors: "Hendricks, D.; Gebbie, T.; Wilcox, D."
year: 2017
venue: "arXiv preprint arXiv:1508.04900v3 (q-fin.TR)"
url: "https://arxiv.org/pdf/1508.04900"
pdf: "sources/01-macro-regime-detection/hendricks-2017-intraday-market-states-temporal-clustering.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "equities"
horizon: "minutes"
tags: "intraday-states, temporal-clustering, genetic-algorithm, microstructure-features, online-state-detection, state-space-reduction, potts-model"
---

## Key insight
Intraday time periods can be clustered into market states using microstructure features (price change, volume, spread, volume imbalance) across many instruments, with the number of states discovered from the data instead of fixed in advance. The clustering is done offline by a GPU-parallel genetic algorithm; a compact "state signature vector" per state then allows the current state to be identified online by nearest-match. The authors frame the states as a reduced state space for learning and planning agents, and report that 5-, 15- and 30-minute states could be assigned reliably while 60-minute states were less stable.

## Method
Objects to cluster are time periods, not stocks. For each period build a vector of feature changes across all stocks, compute the period-by-period correlation matrix, and find the cluster configuration that maximises the Giada-Marsili likelihood (derived from a Potts-model analogy), which needs no preset number of clusters. Optimisation uses a parallel genetic algorithm implemented in CUDA, with the likelihood as the fitness function; the authors say run times permit overnight or intraday recalibration. Features are relative changes in trade price, trade volume, spread and quote volume imbalance. Online detection: for each significant cluster, average the four feature changes across stocks and across member periods to get a four-element state signature vector; assign a new period's four-element feature vector to the state with the smallest Euclidean distance. The authors call this "merely one candidate scheme" and accept that it loses information. Assignments are then used to build and update one-step state transition probability matrices at each time scale.

## Data and sample
Tick-level trades and top-of-book quotes for the 42 constituents of the FTSE/JSE Top40 index on the Johannesburg Stock Exchange, 1 to 30 November 2012, from Thomson Reuters Tick History. Aggregated to 5-, 15-, 30- and 60-minute periods.

## Reported results
- Cluster configurations and their size distributions differ by time scale, with power-law fits suggesting a hierarchy of behaviour; the authors conclude that state definitions should be specific to the time scale an agent trades.
- Online assignment by signature vector reproduced the offline state assignment reliably at 30, 15 and 5 minutes and less so at 60 minutes.
- One analysis retains the 10 clusters with at least 14 member periods as the significant states.
- No forecasting or trading results are reported.

## Signal construction
Offline, on a trailing window: for each bar compute cross-sectional feature changes (return, volume, spread, order-book imbalance) for a basket of instruments; cluster bars by correlation of these vectors; keep clusters above a minimum size; store each cluster's cross-sectional mean of the four feature changes. Online, each bar: compute the same four averages, assign the nearest signature, update the empirical transition matrix. The state index and transition row become inputs to a policy or a reinforcement-learning agent.

## Relevance to SOL perpetuals at minutes to hours
This is the closest source in the folder to the bot's actual setting: intraday bars, microstructure features, an online assignment step, and states intended as inputs to a learning agent. For SOL the "cross-section" could be the same features measured across venues (Binance, Bybit, OKX, Hyperliquid, Coinbase) and across related coins. The genetic algorithm is an implementation choice for a hard combinatorial likelihood; simpler clustering with a persistence penalty may do as well, which is untested here. It is also the one place in this folder where an evolutionary method is applied to state detection itself.

## Caveats
One month of data from one equity market in 2012; "stability" is judged over days, not across market conditions. States are never shown to predict anything. The nearest-signature rule has no persistence control. The authors themselves call for a longer study. The version read is the 2017 arXiv revision; journal publication was not confirmed in this session.
