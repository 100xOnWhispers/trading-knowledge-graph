---
title: "Time Series Forecasting based on Solana Digital Asset Dataset"
authors: "Xiao, Yufeng; Wang, Minxing; Braslavski, Pavel; Ignatov, Dmitry I."
year: 2026
venue: "arXiv preprint arXiv:2608.19521"
url: "https://arxiv.org/pdf/2608.19521"
pdf: "sources/19-onchain-flows-solana/xiao-2026-solana-digital-asset-forecasting-dataset.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "multi-day"
tags: "solana, dex-volume, machine-learning, patchtst, chronos, timegpt, feature-importance, memecoins, dataset"
---

## Key insight
A daily dataset of 1,584 Solana tokens shows that ecosystem activity moves as one block: DEX volume, token trading volume, active wallets, new traders, liquidity-pool balances and the SOL price all peaked together in mid-November 2024 and mid-January 2025. In forecasting token market capitalisation, the SOL price and its moving averages, total DEX volume, DEX trader counts and newly created pairs are among the most informative covariates. SOL and Solana DEX activity are tightly coupled, though the paper models tokens given SOL, not SOL given activity.

## Method
- Dataset construction: 27 daily variables per token combining token transactions, prices, liquidity-pool balances, trader activity, Solana-wide DEX volume, DEX trader counts, newly created pairs and SOL price indicators.
- Benchmark: three-day-ahead forecasts of token market capitalisation, comparing deep models (PatchTST, Temporal Fusion Transformer, TiDE), foundation models (Chronos zero-shot and fine-tuned, TimeGPT) and baselines (Prophet, SeasonalNaive). Metrics: MAE, RMSE, MAPE and rank across tokens.
- Feature importance: permutation importance for TFT and SHAP values for TimeGPT.

## Data and sample
1,584 Solana tokens, daily, 24 March 2024 to 16 March 2025. Sourced from DEX and Solana on-chain data; the specific providers were not confirmed in the parts read. Abstract, introduction and results summaries were read, not every table.

## Reported results
- Synchronised market-wide peaks in mid-November 2024 and mid-January 2025; the January peak coincides with the TRUMP token launch and is followed by a visible shift from liquidity accumulation to withdrawals.
- PatchTST has the best overall rank; fine-tuned Chronos is close; statistical baselines stay competitive for trend-dominated tokens. PatchTST beat SeasonalNaive on 772 tokens and Prophet on 93.
- Most informative covariates: SOL price, SOL moving averages, total DEX volume, DEX trader counts and newly created pairs.
- The authors state they make no deployment or trading recommendations.

## Signal construction
Not a signal for SOL. It suggests which ecosystem series belong in a SOL feature set and should be tested in the reverse direction:
- Inputs: Solana-wide DEX volume, unique DEX traders, new trading pairs created, and aggregate liquidity-pool deposits minus withdrawals, per hour.
- Features: z-scored changes and the share of volume in SOL-quoted pairs.
- Hypothesis: surges in new-pair creation and trader counts raise demand for SOL as the quote and fee asset; net liquidity withdrawals mark the end of an activity burst.

## Relevance to SOL perpetuals at minutes to hours
Indirect. The horizon is three days at daily resolution and the target is small-token market capitalisation. The useful content is the evidence of common ecosystem regimes and the list of covariates. Whether intraday DEX activity leads SOL, lags it or merely co-moves is the open question; with prices set mainly on centralised exchanges, the default expectation is that DEX activity follows SOL price at short horizons.

## Caveats
One year of data that contains a single boom and bust. Feature importance for token forecasts says nothing about causality or about predicting SOL. Using the SOL price as a covariate for SOL-quoted tokens is close to mechanical. Thinly traded tokens have unreliable prices. No trading evaluation. Not peer-reviewed.
