---
title: "Deep Learning for VWAP Execution in Crypto Markets: Beyond the Volume Curve"
authors: "Genet, Remi"
year: 2025
venue: "arXiv:2502.13722"
url: "https://arxiv.org/abs/2502.13722"
pdf: "sources/17-auction-orderflow-practitioner/genet-2025-deep-learning-vwap-execution-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "crypto"
horizon: "hours"
tags: "vwap, execution-benchmark, deep-learning, binance-perpetuals, volume-curve, direct-loss-optimization"
---

## Key insight
VWAP is a benchmark that depends jointly on price and volume, so the usual approach of forecasting the volume curve and allocating in proportion to it is not optimal in volatile markets. Training a network to minimize VWAP slippage directly, through a differentiable loss, gives lower out-of-sample slippage on Binance perpetuals than volume-curve methods, and the allocations it learns deliberately deviate from the best volume forecast. For this topic the paper matters for what it says about VWAP as a reference: volume in crypto is hard to predict, and a VWAP level is only as stable as the volume profile behind it.

## Method
The order is split across T time bins with weights q_t. Losses: quadratic VWAP loss E[(VWAP_achieved / VWAP_market - 1)^2], an absolute version, and a volume-curve loss. Models compared: naive flat allocation; static and dynamic linear regression on the volume curve; a fixed learned volume curve; and "StaticVWAP" neural models trained on each loss, with dynamic variants. Inputs: volume divided by a trailing two-week moving average (shifted to avoid look-ahead), hour-of-day and day-of-week as categorical features, and bin-level VWAP returns. Main configuration: 120 hourly steps of lookback, 12 steps ahead; 6 and 48 step horizons in the appendix. Adam optimizer, early stopping, thirty random initializations per configuration. Market impact is assumed negligible.

## Data and sample
Hourly Binance perpetual futures for BTC, ETH, BNB, ADA and XRP, 1 January 2020 to 1 July 2024. Chronological split with the last 20% as the test set; a validation set is drawn at random from the first 80%. An earlier illustrative section uses BTC, ETH and ADA from contract inception with an 80/20 split and eight bins.

## Reported results
Numerical table entries did not extract cleanly from the PDF, so only the stated findings are given.
- All learned methods beat the flat allocation on all five assets.
- Dynamic linear regression has the highest R-squared for the volume curve, yet the fixed volume curve executes VWAP better. Volume-forecast accuracy is not the main driver of VWAP performance.
- The StaticVWAP model trained on absolute (quadratic) VWAP loss has the lowest absolute (quadratic) slippage on every asset.
- Dynamic variants of the network often degrade performance.
- Rankings hold at 6 and 48 step horizons. Training takes roughly 15 to 18 seconds per run.

## Signal construction
Not a directional signal. Two uses for the bot. (1) Execution: if the bot's entries and exits are measured against interval VWAP, allocate child orders with weights trained on the slippage loss. (2) Feature hygiene: the paper's volume normalization (volume over a shifted two-week moving average, with hour and weekday categories) is a ready recipe for the volume inputs that VWAP, volume-profile and delta features all need. A forecast of how far the session VWAP can still move, given expected remaining volume, also tells a directional model how "anchored" the level is.

## Relevance to SOL perpetuals at minutes to hours
Same instrument type and venue family as the bot's lead signals, though SOL is not in the sample and the bins are hourly. On Kalshi, a small venue, market impact is not negligible, so the no-impact assumption fails for anything but small size. The direct-loss idea carries over to other objectives, for example training on realized execution shortfall. The paper is a deep-learning example in the spirit of the requested machine-learning scope; I found no reinforcement-learning or evolutionary study that uses VWAP or volume-profile levels as inputs.

## Caveats
Single author, preprint, no impact model, hourly bars. Random validation split inside the training period leaks regime information into model selection. Gains are relative slippage improvements whose economic size I could not read from the tables. Execution study; it does not test VWAP as support, resistance or trend filter.
