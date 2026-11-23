---
title: "AetherEdge - Adaptive Volume Profile (AE-AVP)"
authors: "AetherEdge (TradingView account)"
year: 2026
venue: "TradingView open-source script description (posted 18 June; year not shown on the page)"
url: "https://www.tradingview.com/script/HiRgqVon/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "17-auction-orderflow-practitioner"
asset_class: "crypto"
horizon: "minutes"
tags: "volume-profile, value-area, online-logistic-regression, ucb-bandit, triple-barrier, acceptance-rejection"
---

## Key insight
The auction-market question "will a move outside the value area be accepted or rejected?" can be posed as an online supervised-learning problem with a bandit on top. This script does exactly that with a seven-feature logistic model and a UCB bandit that tunes the decision threshold per volatility regime. It reports no performance at all, so its value is as a design template that links the practitioner framework to the machine-learning scope of this repository, not as evidence.

## Method
As described on the page (read through a summarizing tool; wording is paraphrased).
- Profile: the price range of the last N bars is split into rows; each bar's volume is spread across the rows its high-low range spans. POC is the highest-volume row. The value area grows from the POC toward the heavier neighbouring row until it holds a set share of volume (default 70%), giving VAH and VAL. Node strength is row volume over the maximum row volume.
- Event: price breaks above VAH or below VAL.
- Features, oriented to the break direction: edge node strength, approach momentum, volume surge, stretch from POC, trend, volatility regime, value-area width.
- Labels by triple barrier: "accept" if price moves beyond the edge by k times ATR; "reject" if it moves back inside the value area; timed-out events are discarded. A horizon parameter exists; its default was not visible.
- Model: online logistic regression giving P(acceptance). The update rule and learning rate are not described.
- Threshold: a contextual UCB bandit chooses the acceptance threshold separately for three volatility regimes (ATR-percentile terciles), rewarded by the same event outcome.
- Output: follow the break when P is at or above the threshold; fade toward the POC when P is at or below one minus the threshold. Signals are evaluated on bar close.
- Suggested settings for BTC and ETH at 15 minutes to 1 hour: lookback 150, 24 rows, 70% value area.

## Data and sample
None reported.

## Reported results
None. The page gives no backtest, accuracy or out-of-sample figures. It states that the probability and threshold are unreliable until a warm-up period has accumulated enough events, and that the weights and bandit table reset whenever symbol, timeframe or inputs change.

## Signal construction
A bot can reproduce and improve the design from trade data.
1. Build a rolling volume profile from actual trades by price bucket (better than spreading bar volume over the bar's range, which this script must do because it only has bars).
2. On each close beyond VAH or VAL, record the seven features plus signed trade flow, book depth beyond the edge and distance to the nearest round number.
3. Label with a triple barrier fixed in advance.
4. Fit an online logistic model or a gradient-boosted classifier with walk-forward validation; compare against a model that sees only momentum and volatility, and against placebo edges (value-area edges of a shuffled-volume profile).
5. If a threshold bandit is used, treat regime as context and include trading cost in the reward.
An evolutionary search could tune lookback, row count and value-area share, but the placebo comparison must be part of the fitness function or the search will fit noise.

## Relevance to SOL perpetuals at minutes to hours
The script targets crypto at 15-minute to 4-hour bars, which is the bot's horizon. It is the only source found for this topic that joins a volume-profile construct to an adaptive learner; I found no peer-reviewed machine-learning, reinforcement-learning or evolutionary study that uses market-profile, volume-profile or smart-money features as inputs. The acceptance-versus-rejection framing is a sound way to turn every level concept in this topic into a classification task with a common label.

## Caveats
No evidence. Pseudonymous author with a public indicator brand. Online learners that reset per chart cannot be audited, and a shared feedback loop between classifier and bandit invites overfitting to recent regime. Bar-based volume allocation is a coarse approximation of volume at price. Dropping timed-out events biases the label set toward decisive outcomes. Year is inferred, not confirmed.
