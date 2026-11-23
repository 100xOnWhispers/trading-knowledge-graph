---
title: "Are Transformers Effective for Time Series Forecasting?"
authors: "Zeng, Ailing; Chen, Muxi; Zhang, Lei; Xu, Qiang"
year: 2022
venue: "arXiv:2205.13504v3 (August 2022); conference publication not confirmed in this session"
url: "https://arxiv.org/pdf/2205.13504"
pdf: "sources/23-ml-feature-prediction/zeng-2022-are-transformers-effective-time-series-forecasting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "multi"
horizon: "n/a"
tags: "transformer, linear-baseline, dlinear, nlinear, exchange-rate, naive-forecast, overfitting, contrarian"
---

## Key insight
A one-layer linear model beat five purpose-built transformer forecasters on all nine standard long-horizon benchmarks, often by 20 to 50%. On the one financial dataset, exchange rates, simply repeating the last observed value beat every transformer by about 45%. The paper is the standard reference for the rule that a complex sequence model must first be shown to beat a linear model and a naive forecast.

## Method
The authors define three linear models that map the last L observations directly to the next T: a plain linear layer, DLinear (decompose the input into moving-average trend and remainder, one linear layer each, then sum) and NLinear (subtract the last value, apply a linear layer, add it back). These are compared with FEDformer, Autoformer, Informer, Pyraformer and LogTrans, and with a "Repeat" baseline that carries the last value forward. Metrics are mean squared and mean absolute error. Ablations test whether transformers use temporal order: the look-back window is lengthened, and the input sequence is shuffled before embedding.

## Data and sample
Nine public benchmarks: four electricity-transformer temperature sets, traffic, electricity load, weather, influenza-like illness, and exchange rates. No crypto data and no return series.

## Reported results
- The linear models outperform the best transformer (FEDformer) "in most cases by 20% to 50%" on multivariate forecasting.
- On the exchange-rate set, the Repeat baseline outperforms all transformer methods by around 45%. The authors attribute this to transformers predicting wrong trends by overfitting "sudden change noises" in training data.
- Transformer error stays flat or worsens as the look-back window grows, while the linear models improve.
- Shuffling the input order barely changes transformer performance on the exchange-rate data, whereas the linear models are "damaged significantly". The authors conclude the transformers "preserve quite limited temporal relations and are prone to overfit on noisy financial data".
- On data with clearer periodicity (ETTh1), shuffling does hurt FEDformer and Autoformer, with average drops of 73.28% and 56.91%.

## Signal construction
Not a signal. It supplies two mandatory baselines for any deep sequence model on bar data: (1) a ridge or one-layer linear map from the lagged window to the target, in the NLinear form that removes the last level; (2) the naive forecast (zero return). It also supplies a diagnostic: shuffle the order of the input window, and if performance does not fall the model is not using temporal structure.

## Relevance to SOL perpetuals at minutes to hours
Price series for SOL are closer to the exchange-rate benchmark than to electricity load: aperiodic and near random walk. The result argues for regularised linear models and boosted trees on engineered lags before any transformer, and for evaluating on returns, where the naive forecast is zero, not on price levels, where a model that copies the last price looks accurate. The intraday seasonalities documented under topic 10 are the kind of periodic structure where sequence models did add value in this paper, so volatility and volume forecasting are better candidates for them than direction.

## Caveats
The benchmarks are long-horizon level forecasts scored by squared error, not return or direction forecasts scored by trading outcome. The transformers tested are 2020 to 2022 designs; later patch-based and inverted transformers (for example PatchTST and iTransformer, not read here) reportedly recover an advantage on several of these benchmarks, though not specifically on financial series; that claim is from memory and unverified here. The exchange-rate benchmark is a single small dataset, and its description is in an appendix I did not read.
