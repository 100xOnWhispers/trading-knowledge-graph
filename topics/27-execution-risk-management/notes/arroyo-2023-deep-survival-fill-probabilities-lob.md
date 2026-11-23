---
title: "Deep Attentive Survival Analysis in Limit Order Books: Estimating Fill Probabilities with Convolutional-Transformers"
authors: "Arroyo, Alvaro; Cartea, Alvaro; Moreno-Pino, Fernando; Zohren, Stefan"
year: 2023
venue: "arXiv preprint 2306.05479"
url: "https://arxiv.org/pdf/2306.05479"
pdf: "sources/27-execution-risk-management/arroyo-2023-deep-survival-fill-probabilities-lob.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "seconds"
tags: "fill-probability, survival-analysis, limit-orders, transformer, machine-learning, order-placement"
---

## Key insight
The time until a limit order fills can be modelled as a survival problem, and a neural network that reads recent order book history predicts the whole fill-time distribution better than standard survival models. This gives the execution layer a state-dependent answer to "if I rest here, what is the chance I am filled within t seconds?", which is the input a limit-versus-market decision needs.

## Method
Survival analysis with right-censoring: an order that is cancelled or still resting at the horizon is censored, not a failure. The encoder is a convolutional-Transformer over a lookback window of book features; the decoder is a monotonic neural network that outputs a valid survival function on any time grid. Training maximises right-censored log-likelihood, a proper scoring rule, which the authors argue is needed to fit the true survival function. Baselines: DeepSurv, DeepHit, and variants of their model with other encoders (MLP, CNN, LSTM). Shapley values are used for interpretation. Two ways of generating training data are compared: tracking real orders in the book, and "hypothetical" one-share orders placed at the back of a queue and assumed to have no impact.

Features: slow-moving ones (time of day, volatility from a rolling mean of squared mid-price returns over 1,000 trades) and fast-moving ones (top-of-book volume imbalance, microprice, and raw prices and volumes of the best five levels), stored over lookbacks of 50, 500 and 1,000 trades.

## Data and sample
Nasdaq message data from Lobster for nine stocks (AAPL, AMZN, BIDU, COST, DELL, GOOG, MSFT, CSCO, INTC), a mix of small-tick and large-tick names. Model training period 1 September to 26 December 2022; fill statistics reported for 1 October to 27 December 2022.

## Reported results
- The proposed model "significantly outperforms" the survival-analysis baselines on right-censored log-likelihood (per-stock scores are in tables not reproduced here).
- The model relies mostly on fast-moving features; slow features that carry intraday seasonality get less weight.
- All encoders that model the book's time dynamics beat the static ones. LSTM and CNN encoders gain little or degrade with longer lookback windows; the convolutional-Transformer performs best at the longer windows.
- Each training day contributes 100 tracked real orders or 100 hypothetical orders pegged to the best level.
- For orders placed inside the spread of large-tick stocks, fill probability rises sharply at very short horizons and then flattens to the level of orders at the best quote: a fast fill means the order got queue priority and price moved toward it; otherwise price moved away.
- More actively traded stocks have faster-decaying survival curves.

## Signal construction
Not a directional signal; it is a component of the execution policy. Inputs: recent book snapshots and trades. Output: `P(fill within t | state, price level)` for candidate limit prices. Decision rule: choose the price level and patience that minimise `expected cost = P(fill) * (cost if filled, including expected adverse markout) + (1 - P(fill)) * (cost of crossing later)`. A simple first version is a Kaplan-Meier curve or a gradient-boosted survival model per price level, refit weekly, before attempting the Transformer.

## Relevance to SOL perpetuals at minutes to hours
The framing transfers; the fitted model does not. Kalshi publishes one-minute bid and ask candles and trades with taker side back to June 2026 (topic 06), which is too coarse for the hypothetical-order method; the bot would need to record the book itself or learn from its own orders. The Albers et al. note shows why fill probability alone is the wrong objective: fills are negatively correlated with subsequent returns, so the model should predict fill time and post-fill markout jointly.

## Caveats
US equities over four months in one market regime. Hypothetical orders ignore the order's own impact and, as Albers et al. point out, such methods can misjudge queue position and conditioning. No trading test, no costs, no comparison of the resulting execution policy against a simple rule. Deep models of this kind are data-hungry relative to the history available on a venue that opened in mid-2026.
