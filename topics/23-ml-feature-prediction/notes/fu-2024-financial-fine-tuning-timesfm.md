---
title: "Financial Fine-tuning a Large Time Series Model"
authors: "Fu, Xinghong; Hirano, Masanori; Imajo, Kentaro"
year: 2024
venue: "arXiv:2412.09880v1"
url: "https://arxiv.org/pdf/2412.09880"
pdf: "sources/23-ml-feature-prediction/fu-2024-financial-fine-tuning-timesfm.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "23-ml-feature-prediction"
asset_class: "multi"
horizon: "daily"
tags: "timesfm, foundation-model, fine-tuning, zero-shot-failure, crypto-hourly, market-neutral, ar1-baseline"
---

## Key insight
Google's TimesFM applied zero-shot to price series is worse than a chance-rate guesser on four of seven forecast horizons. Fine-tuning it on a corpus the authors describe as 100 million points of financial data, dominated by hourly crypto bars, lifts directional accuracy above chance at every horizon. But in mock trading the fine-tuned model's crypto Sharpe ratio is only 0.26 with no costs, barely ahead of a one-lag autoregression, and it loses to that autoregression in currencies.

## Method
Continual pretraining of TimesFM on log-transformed price series with random masking of context length, minimising squared error on the next output block. Data before 2023 is split 75/25 into training and validation; 2023 onward is the test set. Evaluation: directional accuracy and macro F1 at horizons from 2 to 128 steps, against the original TimesFM and a chance-rate model that guesses "up" at the base rate. Mock trading uses a basic long-short rule on the forecast direction and a market-neutral variant that subtracts the cross-sectional mean position; results are reported with zero trading costs, together with a "neutral cost", the per-trade cost that would reduce the return to zero. Benchmarks are the original TimesFM, a random model and an AR(1) model.

## Data and sample
Yahoo Finance and Binance. The fine-tuning set includes daily series for TOPIX500 stocks, S&P 500 stocks, currencies, Japanese investment trusts, commodities and stock indices; hourly stock indices and stock prices; daily crypto (1,680 series, about 1.1 million points); and hourly crypto (79,153 series, about 50.7 million points, by far the largest row in the data table). Every row has exactly 640 points per "series", so the series counts are fixed-length chunks, not distinct instruments.

## Reported results
- Original TimesFM underperforms the chance rate on 4 of 7 horizons; the authors conclude it "cannot be used in its original state for price prediction".
- Fine-tuned TimesFM beats both the original and the chance rate at all horizons from 2 to 128.
- S&P 500 market-neutral results by horizon are erratic at short horizons (annualised Sharpe 0.52 at horizon 2, -0.48 at 4, 0.00 at 16) and best at the longest (1.29 at 64, 1.68 at 128, with 3.6% annual return).
- Sharpe ratio by market (fine-tuned, original TimesFM, random, AR1): S&P 500 1.68, 0.42, 0.03, 1.58; TOPIX500 1.06, -1.75, 0.11, -0.82; currencies 0.25, -0.04, -0.03, 0.88; crypto daily 0.26, -0.03, 0.01, 0.17.
- Neutral cost for crypto daily: fine-tuned 0.44%, AR1 0.88%.
- The authors write that performance on currencies and crypto "is left to be desired".

## Signal construction
Not directly usable as specified. If tested, the recipe is: fine-tune a pretrained decoder-only time-series model on log prices of many instruments at the target frequency, forecast H steps ahead, and take the sign of the forecast change as the position, de-meaned across instruments.

## Relevance to SOL perpetuals at minutes to hours
It is one of the few foundation-model papers that trains on hourly crypto and reports a crypto trading number, and the number is weak. The practical reading for the bot: an off-the-shelf general time-series model should not be used on price data; a fine-tuned one must be benchmarked against AR(1) and other trivial baselines, which it barely beats here; and short-horizon results were unstable even in the best market. Hourly crypto trading results are not reported despite hourly crypto dominating the training data.

## Caveats
Preprint with zero-cost mock trading, a single test period from 2023, and no confidence intervals. The S&P 500 AR(1) baseline reaching Sharpe 1.58 suggests the market-neutral construction itself harvests a known short-term reversal effect. The hourly crypto "series" are 640-point chunks, so the number of distinct coins is not stated and the effective sample is smaller than the counts suggest. For crypto the AR1 model has a lower Sharpe ratio but a higher neutral cost than the fine-tuned model, so the two metrics disagree on which is better.
