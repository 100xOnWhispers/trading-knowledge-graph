---
title: "Transformers versus LSTMs for electronic trading"
authors: "Bilokon, Paul; Qiu, Yitao"
year: 2023
venue: "arXiv:2309.11400v1"
url: "https://arxiv.org/abs/2309.11400"
pdf: "sources/22-deep-learning-lob/bilokon-2023-transformers-versus-lstm-electronic-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "22-deep-learning-lob"
asset_class: "crypto"
horizon: "seconds"
tags: "transformer, lstm, dlstm, autoformer, informer, binance, btc-usdt, eth-usdt, out-of-sample-r2, transaction-costs, price-difference"
---

## Key insight
On Binance BTC-USDT and ETH-USDT order book data, time-series transformers (Autoformer, FEDformer, Informer, Reformer) only beat LSTMs at forecasting the price level, a task where every model has negative out-of-sample R2 once measured on price changes. For forecasting price differences and movement classes, LSTM-based models are better and more robust, and their simulated profits survive small transaction costs better than those of transformers.

## Method
Three tasks on LOB input, comparing LSTM-family models (LSTM, CNN-LSTM, DeepLOB, DeepLOB-Seq2Seq, DeepLOB-Attention) with transformer-family models:
1. Mid-price level forecasting over 96 to 720 steps, scored by MSE and MAE, then by out-of-sample R2 on implied price differences.
2. Mid-price difference forecasting, scored by out-of-sample R2.
3. Three-class movement prediction with smoothed labels at horizons 20, 30, 50, 100 ticks. The authors add DLSTM, an LSTM applied separately to a moving-average trend component and the remainder (the decomposition idea from DLinear and Autoformer).

Trading simulation follows DeepLOB (act on up and down signals, fixed size), first with no cost and then with a hypothetical cost of 0.002% per trade, and with a sweep of increasing costs.

## Data and sample
Binance LOB collected live through the cryptofeed WebSocket API. Task 1: BTC-USDT, one day (15 July 2022), 863,397 ticks, about 0.1 second apart on average. Task 2: BTC-USDT, 3 to 6 July 2022, 3,432,211 ticks. Task 3: ETH-USDT, 3 to 14 July 2022, 10,255,144 ticks; first six days train, last three test.

## Reported results
- Task 1: transformers have 10% to 25% lower error than LSTM, but all models' out-of-sample R2 on price differences is negative; the authors call level forecasts useless for trading and say MSE and MAE hide this.
- Task 2: plain LSTM is best, with out-of-sample R2 peaking around 11.5% at forecast lengths of 5 to 15 ticks; CNN-LSTM is comparable; transformers are worse.
- Task 3: DLSTM reaches 63.73% to 73.31% accuracy and is best at every horizon; DeepLOB-Attention is second at horizons 50 and 100.
- Simulation without costs: LSTM-family models earn more than transformers; Autoformer sometimes does worse than the vanilla transformer despite better classification scores.
- With a 0.002% cost: DLSTM has the highest cumulative return and Sharpe ratio at all horizons; Autoformer turns negative at horizons 50 and 100. Returns and Sharpe ratios of all models decline as costs rise.
- DLSTM inference takes 4.4 ms with 193.9k parameters.

## Signal construction
Forecast the mid-price difference (not the level) over the next 5 to 15 book updates with an LSTM on z-scored 10-level book inputs; or classify smoothed movement with a decomposed LSTM. Score with out-of-sample R2 against a zero forecast, never with MSE on levels.

## Relevance to SOL perpetuals at minutes to hours
Direct crypto evidence that architecture fashion does not help: a small recurrent model is the sensible default for a SOL book model, and classification accuracy is a poor guide to simulated profit. The R2 peak at 5 to 15 ticks (roughly 0.5 to 1.5 seconds at this data rate) again places book-based predictability at the seconds scale. The products are named BTC-USDT and ETH-USDT, which reads as spot (not confirmed in the paper); perps and cross-venue inputs are untested here.

## Caveats
Very short samples from a single fortnight in July 2022. The cost tested, 0.002% (0.2 basis points), is far below typical exchange taker fees, and the simulation follows the DeepLOB mid-price setup, so the "robust to costs" claim does not show net profitability; the authors themselves call the annualised Sharpe ratios unrealistic. DLSTM is the authors' own model, tuned on the same data.
