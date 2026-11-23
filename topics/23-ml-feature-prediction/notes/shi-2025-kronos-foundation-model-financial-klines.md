---
title: "Kronos: A Foundation Model for the Language of Financial Markets"
authors: "Shi, Yu; Fu, Zongliang; Chen, Shuo; Zhao, Bohan; Xu, Wei; Zhang, Changshui; Li, Jian"
year: 2025
venue: "arXiv:2508.02739v1 (Tsinghua University)"
url: "https://arxiv.org/pdf/2508.02739"
pdf: "sources/23-ml-feature-prediction/shi-2025-kronos-foundation-model-financial-klines.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "multi"
horizon: "daily"
tags: "foundation-model, candlestick, tokenizer, zero-shot, binance, rank-ic, pretraining, transformer"
---

## Key insight
Kronos is a decoder-only transformer pretrained specifically on candlestick (OHLCV) bars, not on generic time series. The authors report that general-purpose time-series foundation models often underperform non-pretrained models on bar data, and that a finance-native tokenizer and corpus reverse this in zero-shot tests that include Binance spot pairs. It is the main openly released candidate for a pretrained bar-data forecaster, but its evidence of economic value is a Chinese equity backtest, not a crypto one.

## Method
A tokenizer quantises each multivariate bar into discrete tokens (a binary spherical quantisation scheme split into coarse and fine sub-tokens), and an autoregressive transformer is pretrained to predict the next token. Sampling the model several times gives a distribution of future paths. Evaluation is zero-shot on five tasks: price-series forecasting and return forecasting (scored by IC and RankIC across assets), realised-volatility forecasting, synthetic bar generation, and an investment simulation. Baselines include non-pretrained models trained on each task (among them iTransformer, PatchTST, TimesNet, TimeMixer, TimeXer and FEDformer), zero-shot foundation models (among them TimesFM, Chronos, MOMENT and Time-MoE), and ARCH and GARCH volatility models.

## Data and sample
Pretraining corpus: more than 12 billion bar records from 45 exchanges across stocks, crypto, futures and forex, at several frequencies, extending to June 2024; under-represented classes (crypto, futures, forex) are resampled upward. Test period starts July 2024. Test assets: nine stock exchanges (six in the pretraining distribution, three held out), all Binance spot pairs, and over 1,000 forex pairs. For crypto and forex only OHLC is supplied at test time, no volume.

## Reported results
- Abstract: price-series forecasting RankIC is 93% higher than the leading time-series foundation model and 87% higher than the best non-pretrained baseline; volatility forecasting MAE is 9% lower; generative fidelity is 22% better.
- Performance improves with model size.
- Averaging more sampled paths improves IC and RankIC.
- Investment simulation: long-only top-k portfolios on CSI 300 and CSI 800 constituents with daily bars, 90-day lookback, a 5-day minimum holding period and a 0.15% cost per trade. Kronos has the highest annualised excess return and information ratio among the baselines.
- I did not find per-asset-class tables in the pages read that isolate the crypto RankIC or any crypto trading result.

## Signal construction
Feed the last N bars of an instrument (OHLC, with volume where reliable) to the pretrained model, sample a set of future paths over the horizon, and use the mean forecast return (and the dispersion of paths as an uncertainty estimate) as one feature in a downstream model. The paper's own signal is the average forecast price over H steps relative to the current close.

## Relevance to SOL perpetuals at minutes to hours
Promising as a feature generator, unproven as a standalone signal. The corpus includes crypto and intraday frequencies, and the model is public, so a direct test on SOL perp bars at 5 to 60 minutes is cheap. Two cautions: RankIC is a cross-sectional metric and says little about timing one asset; and any evaluation on data before July 2024 is contaminated by pretraining, so tests must use later data only. Perp-specific inputs (funding, open interest) are outside the model's input format and would have to enter through a second-stage model.

## Caveats
Author-run preprint. The trading evidence is long-only A-shares at daily frequency. No crypto backtest, no costs for crypto, and the comparison baselines were tuned by the authors. The zero-shot claim depends on the July 2024 cutoff being clean across all 45 source exchanges, which cannot be audited from the paper.
