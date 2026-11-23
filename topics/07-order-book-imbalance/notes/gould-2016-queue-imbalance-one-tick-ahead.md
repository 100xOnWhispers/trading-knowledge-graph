---
title: "Queue Imbalance as a One-Tick-Ahead Price Predictor in a Limit Order Book"
authors: "Gould, Martin D.; Bonart, Julius"
year: 2016
venue: "Market Microstructure and Liquidity (journal details not confirmed in this session; read as arXiv:1512.03492v1, December 2015)"
url: "https://arxiv.org/pdf/1512.03492"
pdf: "sources/07-order-book-imbalance/gould-2016-queue-imbalance-one-tick-ahead.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "tick"
tags: "queue-imbalance, top-of-book, logistic-regression, tick-size, direction-prediction"
---

## Key insight
The static imbalance between best-bid and best-ask queue sizes predicts the direction of the next mid-price move, with out-of-sample tests. The effect is strong for large-tick stocks and only moderate for small-tick stocks. This is the cleanest statement of the "book pressure" signal that practitioners use, and of its dependence on relative tick size.

## Method
Queue imbalance is `I = (n_b - n_a) / (n_b + n_a)`, in [-1, 1], using sizes at the best bid and ask. The target is the direction of the next mid-price change. The authors fit a logistic regression `P(up) = 1 / (1 + exp(-(x0 + x1 I)))` per stock and a semi-parametric local logistic regression, and compare both with a null model that always predicts probability 1/2. Evaluation is out of sample using ROC curves, area under the curve, and mean squared residuals.

## Data and sample
LOBSTER data for ten liquid Nasdaq stocks for all of 2014, 10:00 to 15:30 each day. Five large-tick stocks (MSFT, INTC, MU, CSCO, ORCL; price below 50 dollars) and five small-tick stocks (price above 100 dollars, including GOOG and AMZN).

## Reported results
- The relationship is strongly statistically significant for all ten stocks.
- Relative to the null model, out-of-sample binary classification improves by about 50% to 60% for large-tick stocks and about 10% to 30% for small-tick stocks; probabilistic prediction improves by about 20% to 30% and about 2% to 6% respectively.
- Area under the ROC curve is about 0.7 to 0.8 for large-tick stocks and about 0.6 to 0.65 for small-tick stocks; in-sample values are very similar.
- Fitted slopes `x1` are about 2 to 3 for large-tick stocks and about 0.5 to 0.8 for small-tick stocks. At extreme imbalance the fitted up-move probability is about 0.8 to 0.9 for large-tick and about 0.6 to 0.7 for small-tick stocks.
- Local logistic regression is only slightly better than the plain logistic fit.
- Small-tick stocks show round-number effects in queue sizes.

## Signal construction
Inputs: best bid and ask sizes from the L1 stream. Compute `I` on every update. Map to a probability with a logistic curve fitted on a trailing sample per instrument and venue. The prediction horizon is event-time: until the next mid-price change.

## Relevance to SOL perpetuals at minutes to hours
The signal is cheap and available on every venue, but its horizon is one price change, which on a liquid SOL perp is typically well under a second to a few seconds. For a minutes-to-hours bot its direct use is entry and exit timing (cross the spread or wait). The tick-size dependence must be measured per venue: where the spread is pinned at one tick, the queue ratio is informative; where the tick is negligible, the touch queues are small and noisy and the effect weakens. A time-averaged or multi-level version should be tested for longer horizons rather than assumed.

## Caveats
Predicts direction of the next tick, not magnitude net of spread; no trading test. 2014 equity data. Queue sizes at the touch can be manipulated, and competition for this well-known signal has increased.
