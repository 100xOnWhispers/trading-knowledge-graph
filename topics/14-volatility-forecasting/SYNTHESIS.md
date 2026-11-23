# Topic 14: Volatility measurement, forecasting and sizing

Twenty-two source notes. Scope: realized-volatility estimators, HAR and GARCH-family models in crypto, jumps, intraday periodicity, the volume-volatility relation, machine-learning, evolutionary and reinforcement-learning approaches to volatility and sizing, volatility targeting, Kelly sizing, and leverage under liquidation risk. Options-implied volatility (topic 20) and regime-switching models (topic 01) are excluded.

## What the literature agrees on

1. **Volatility is measurable and forecastable; direction is not the subject here.** Summing squared intraday returns gives a usable measurement of variance, and models fitted to that measurement beat models fitted to daily returns ([Andersen et al. 2003](notes/andersen-2003-modeling-forecasting-realized-volatility.md)). Every later paper in this folder takes this as given.

2. **A three-scale autoregression (HAR) is the benchmark to beat, and it is hard to beat by much.** HAR matches fractionally integrated models with a plain OLS regression ([Corsi 2009](notes/corsi-2009-har-long-memory-realized-volatility.md)). In crypto, neural networks beat GARCH comfortably but beat HAR only narrowly and not consistently ([Huang et al. 2024](notes/huang-2024-forecasting-bitcoin-volatility-machine-learning.md)); for quantile forecasts, linear models on log RV are the best group and GARCH, LASSO and LSTM the worst ([Dudek et al. 2025](notes/dudek-2025-probabilistic-forecasting-cryptocurrency-volatility.md)).

3. **Simple estimators are adequate.** Five-minute RV is rarely beaten significantly across 31 assets, and a jump-truncated 5- or 15-minute RV is the best forecasting input ([Liu et al. 2015](notes/liu-2015-realized-measures-five-minute-rv.md)). Where only OHLC bars exist, Garman-Klass and Parkinson are far more accurate than close-to-close but biased low ([Mouti 2023](notes/mouti-2023-rough-volatility-range-based-estimators.md)).

4. **Volatility has a persistent part and a jump part, and they should be handled separately.** Bipower variation isolates the persistent part ([Barndorff-Nielsen and Shephard 2004](notes/barndorff-nielsen-2004-power-bipower-variation-jumps.md)). In Bitcoin, jumps are frequent, cluster, and are followed by about an hour of elevated volatility and volume ([Scaillet et al. 2020](notes/scaillet-2020-high-frequency-jump-analysis-bitcoin.md)). Component GARCH fitting best on daily Bitcoin data says the same thing in parametric form ([Katsiampa 2017](notes/katsiampa-2017-volatility-estimation-bitcoin-garch.md)).

5. **Crypto volatility has strong calendar structure.** Day-of-week, hour-of-day and minute-of-hour patterns are stable, with bursts at the top of the hour and at funding times; modelling them improves out-of-sample fit more than adding realized variance to a GARCH ([Hansen et al. 2024](notes/hansen-2024-periodicity-cryptocurrency-volatility-liquidity.md)). Session-based activity cycles also appear on Binance perpetuals through 2024 ([Pinto 2025](notes/pinto-2025-high-frequency-bitcoin-futures-microstructure.md)).

6. **Trading activity carries volatility information.** Volume and spread lead squared returns at the one-minute scale ([Barjašić and Antulov-Fantulin 2020](notes/barjasic-2020-bitcoin-volatility-information-flow-minute.md)); variance per trade rises with trade size on perpetuals ([Pinto 2025](notes/pinto-2025-high-frequency-bitcoin-futures-microstructure.md)); order-flow imbalance, taker share and spread precede jumps ([Scaillet et al. 2020](notes/scaillet-2020-high-frequency-jump-analysis-bitcoin.md)); order flow and book data improve 60-second volatility forecasts ([Lensky and Hao 2023](notes/lensky-2023-short-term-volatility-order-flow-images.md)). The one evolutionary-algorithm study found also gets its gain from microstructure inputs ([Yin et al. 2015](notes/yin-2015-genetic-programming-realised-volatility-forecasting.md)).

7. **Volatility dynamics are largely common across coins.** One model trained on a pooled panel of 213 coins beats per-coin models ([Tang et al. 2023](notes/tang-2023-lstm-rough-volatility-crypto-winter.md)).

8. **Volatility-scaled sizing stabilises risk and thins the left tail.** This holds across more than 60 assets ([Harvey et al. 2018](notes/harvey-2018-impact-volatility-targeting.md)).

9. **Over-betting is worse than under-betting, and tails set the leverage limit.** Growth falls to zero at twice the Kelly fraction, and the Kelly fraction is very sensitive to the estimated edge ([MacLean et al. 2010](notes/maclean-2010-good-bad-properties-kelly-criterion.md)). On Bitcoin perpetuals, extreme-value estimates put survivable leverage near 3x to 5x for a 1% daily margin-call probability, with normal-distribution estimates too low by at least half ([Cheng et al. 2021](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md)).

## Where it disagrees or is weak

- **Does volatility timing raise returns, or only stabilise risk?** [Moreira and Muir 2017](notes/moreira-2017-volatility-managed-portfolios.md) report large alphas from inverse-variance scaling. [Cederburg et al. 2020](notes/cederburg-2020-performance-volatility-managed-portfolios.md) show that across 103 strategies the managed version wins only 53 times, with significant gains concentrated in momentum-related strategies, and that real-time versions mostly underperform. [Harvey et al. 2018](notes/harvey-2018-impact-volatility-targeting.md) find a Sharpe gain only where a leverage effect exists. The safe reading is that volatility scaling is a risk-control tool whose effect on returns depends on the strategy.

- **Is there a leverage effect in crypto?** Hansen et al. find the asymmetry parameter insignificant for BTC and ETH. Tang et al. find it inverted (rallies raise volatility). Cheng et al. find the left tail of perpetual prices heavier than the right. These are not contradictory (asymmetry in ordinary volatility response versus asymmetry in extremes), but they imply that equity-style assumptions should not be imported.

- **Machine learning versus HAR.** Huang et al. report LSTM gains over HAR; Tang et al. report gains from pooled LSTMs; Dudek et al. find LSTM among the worst for quantile forecasts. Search results in this session also pointed to studies concluding HAR beats ML in crypto (Korkusuz and Sahiner 2025) and the reverse (Brauneis and Sahiner 2024); those were not opened. Outcomes appear to depend on input cleaning, pooling, horizon and the test window, and the margins are small.

- **Horizon mismatch.** Almost all forecasting evidence is for one day ahead or longer. The only intraday forecasting studies found are a six-week one-minute GARCH-X study and a one-month 60-second CNN study, both grade C. HAR-type forecasting at 15 minutes to 4 hours on crypto perpetuals is essentially untested in what was read.

- **Estimator choice at short windows.** The "5-minute RV is enough" result is for daily variance. A one-hour estimate has 12 five-minute returns. Jump-robust estimators assume neighbouring returns are alike, which the top-of-hour bursts violate (noted by Hansen et al.).

- **Sizing theory ignores perpetual mechanics.** Kelly results assume continuous rebalancing, known distributions and no liquidation. Cheng et al. give unconditional tails with no volatility conditioning. No source combines Kelly sizing, a volatility forecast, funding costs and a liquidation boundary.

- **Reinforcement learning evidence is thin.** [Zhang et al. 2019](notes/zhang-2019-deep-reinforcement-learning-trading.md) is daily data on diversified futures. [Qin et al. 2025](notes/qin-2025-fineft-ensemble-rl-futures-trading.md) is crypto at minute level with leverage, but its low drawdown partly reflects sitting in a non-trading conservative policy for most of a six-month test.

- **Evolutionary methods.** One 2004 FTSE study with 129 test days. A genetic-programming crypto-volatility paper (Ding et al. 2025) appeared in search results but was not accessible.

- **SOL is absent.** No source tests SOL specifically. Everything is BTC, ETH, a broad altcoin panel, or traditional assets.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Realized variance (5-min, subsampled; 1-min for short windows) | Trade or mid prices from the lead venue | minutes to daily | A | [andersen-2003](notes/andersen-2003-modeling-forecasting-realized-volatility.md), [liu-2015](notes/liu-2015-realized-measures-five-minute-rv.md) |
| Garman-Klass / Parkinson range variance | OHLC bars | minutes to daily | B | [mouti-2023](notes/mouti-2023-rough-volatility-range-based-estimators.md) |
| Bipower variation and jump share (RV - BV) / RV | Intraday returns | minutes to daily | A (method), untested intraday in crypto | [barndorff-nielsen-2004](notes/barndorff-nielsen-2004-power-bipower-variation-jumps.md) |
| HAR forecast (three scales, on log RV) | Lagged RV at short, medium, long windows | daily; intraday adaptation untested | A at daily | [corsi-2009](notes/corsi-2009-har-long-memory-realized-volatility.md) |
| Two-speed variance (component GARCH or fast/slow EWMA) | Returns | daily | C | [katsiampa-2017](notes/katsiampa-2017-volatility-estimation-bitcoin-garch.md) |
| Seasonal volatility factor (weekday, hour, minute-of-hour, funding time) | Trailing 1-min absolute returns by calendar bin | minutes to hours | A | [hansen-2024](notes/hansen-2024-periodicity-cryptocurrency-volatility-liquidity.md), [pinto-2025](notes/pinto-2025-high-frequency-bitcoin-futures-microstructure.md) |
| Volume and spread as exogenous variance terms (GARCH-X or HAR-X) | 1-min volume, quoted spread | minutes | C | [barjasic-2020](notes/barjasic-2020-bitcoin-volatility-information-flow-minute.md) |
| Trade-count and trade-size variance nowcast | Trade count, average trade size | minutes to hours | B (contemporaneous) | [pinto-2025](notes/pinto-2025-high-frequency-bitcoin-futures-microstructure.md) |
| Jump-risk state (imbalance, taker share, spread) and one-hour post-jump regime | Signed trades, top-of-book | minutes to one hour | B (2011-2013 data) | [scaillet-2020](notes/scaillet-2020-high-frequency-jump-analysis-bitcoin.md) |
| Order-flow CNN volatility nowcast | Trades and 20-level book, last 4 minutes | seconds to one minute | C | [lensky-2023](notes/lensky-2023-short-term-volatility-order-flow-images.md) |
| Pooled cross-coin volatility model (LSTM or rough-volatility) | Daily RV and returns for many coins | daily | B | [tang-2023](notes/tang-2023-lstm-rough-volatility-crypto-winter.md) |
| LSTM on HAR inputs, pre-averaged RV | Noise-robust RV lags | daily to weekly | B | [huang-2024](notes/huang-2024-forecasting-bitcoin-volatility-machine-learning.md) |
| Genetic-programming feature search for volatility | Lagged RV plus microstructure variables | daily | C | [yin-2015](notes/yin-2015-genetic-programming-realised-volatility-forecasting.md) |
| Residual-simulation quantiles of forecast variance | Any point forecaster's past errors (on log RV) | daily; portable | B | [dudek-2025](notes/dudek-2025-probabilistic-forecasting-cryptocurrency-volatility.md) |
| Volatility-target sizing (notional = equity x target / forecast vol, capped) | Volatility forecast | any | A for risk control; disputed for returns | [harvey-2018](notes/harvey-2018-impact-volatility-targeting.md), [moreira-2017](notes/moreira-2017-volatility-managed-portfolios.md), [cederburg-2020](notes/cederburg-2020-performance-volatility-managed-portfolios.md) |
| Fractional Kelly leverage (fraction x edge / variance) | Edge estimate, variance forecast | any | B (theory) | [maclean-2010](notes/maclean-2010-good-bad-properties-kelly-criterion.md) |
| Extreme-value liquidation-distance constraint | Block extremes of 5-min returns over the holding period | hours | B | [cheng-2021](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md) |
| Volatility-scaled RL reward with cost penalty | Agent action, volatility estimate, cost rate | daily in source | B | [zhang-2019](notes/zhang-2019-deep-reinforcement-learning-trading.md) |
| Novelty gate to a conservative policy | Feature vectors, density or autoencoder model | minutes | C | [qin-2025](notes/qin-2025-fineft-ensemble-rl-futures-trading.md) |

## Open questions worth testing on SOL perps

1. **Intraday HAR.** Does a HAR with scales such as 1 hour, 8 hours and 1 to 7 days, on deseasonalised log RV, beat an EWMA and a GARCH(1,1) for 15-minute, 1-hour and 4-hour-ahead SOL variance, by QLIKE, out of sample?
2. **Which venue's volatility?** Is RV from the Binance or Bybit SOL perp a better predictor of Kalshi SOL perp volatility than Kalshi's own thin history? How large is the basis-volatility wedge?
3. **Seasonal factor for a US-regulated venue.** What are the hour-of-day and funding-time patterns for SOL on Kalshi, and do the top-of-hour bursts documented for BTC and ETH in 2019 to 2021 persist in 2026?
4. **Asymmetry.** Does SOL volatility rise more after up moves, down moves, or neither, at the 1-hour scale? This decides whether volatility targeting behaves like a momentum overlay or the opposite.
5. **Jump handling.** Does separating bipower variation from the jump share improve hour-ahead forecasts, and is the one-hour post-jump decay still about right?
6. **Activity inputs.** Do volume, trade count, average trade size, spread and taker share add out-of-sample forecasting power once seasonality and lagged RV are controlled?
7. **Pooling.** Does a forecaster trained on a pooled panel (BTC, ETH, SOL and other liquid perps) beat a SOL-only model?
8. **Does sizing help each signal?** For every directional signal from other topics, compare fixed-notional, inverse-volatility and inverse-variance sizing directly and out of sample, following the Cederburg protocol. Does the signal's expected return per trade scale with volatility?
9. **Tail-based leverage.** What are the 1-, 4- and 8-hour adverse-excursion quantiles for SOL, conditional on the current volatility forecast, and how do they compare with Kalshi's maintenance margin at its maximum leverage? How often would a stop be gapped through?
10. **Kelly fraction under uncertainty.** Given the standard error of each signal's estimated edge, what Kelly fraction keeps the probability of over-betting (above full Kelly) small?
11. **Quantile sizing.** Does sizing against an upper quantile of forecast volatility reduce drawdowns relative to sizing against the mean forecast, net of the return given up?
12. **Learning-based layers.** Does an ML, evolutionary or RL component add anything over HAR plus rules once costs and a novelty gate are included? The burden of proof is on the complex model.

## Reading order

1. [Andersen et al. 2003](notes/andersen-2003-modeling-forecasting-realized-volatility.md): why realized volatility.
2. [Corsi 2009](notes/corsi-2009-har-long-memory-realized-volatility.md): the benchmark forecaster.
3. [Liu et al. 2015](notes/liu-2015-realized-measures-five-minute-rv.md): which estimator to use.
4. [Barndorff-Nielsen and Shephard 2004](notes/barndorff-nielsen-2004-power-bipower-variation-jumps.md): jumps versus persistent variance.
5. [Hansen et al. 2024](notes/hansen-2024-periodicity-cryptocurrency-volatility-liquidity.md): crypto calendar structure. The most directly useful crypto paper here.
6. [Scaillet et al. 2020](notes/scaillet-2020-high-frequency-jump-analysis-bitcoin.md): jumps in Bitcoin and what precedes them.
7. [Pinto 2025](notes/pinto-2025-high-frequency-bitcoin-futures-microstructure.md) and [Barjašić and Antulov-Fantulin 2020](notes/barjasic-2020-bitcoin-volatility-information-flow-minute.md): volume, trade size and volatility on crypto venues.
8. [Harvey et al. 2018](notes/harvey-2018-impact-volatility-targeting.md), then [Moreira and Muir 2017](notes/moreira-2017-volatility-managed-portfolios.md), then [Cederburg et al. 2020](notes/cederburg-2020-performance-volatility-managed-portfolios.md): the volatility-targeting debate, in that order.
9. [MacLean et al. 2010](notes/maclean-2010-good-bad-properties-kelly-criterion.md) and [Cheng et al. 2021](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md): how much to bet and how much leverage survives.
10. [Huang et al. 2024](notes/huang-2024-forecasting-bitcoin-volatility-machine-learning.md), [Tang et al. 2023](notes/tang-2023-lstm-rough-volatility-crypto-winter.md), [Dudek et al. 2025](notes/dudek-2025-probabilistic-forecasting-cryptocurrency-volatility.md): what machine learning adds.
11. [Zhang et al. 2019](notes/zhang-2019-deep-reinforcement-learning-trading.md) and [Qin et al. 2025](notes/qin-2025-fineft-ensemble-rl-futures-trading.md): reinforcement learning with volatility scaling and leverage.
12. Reference as needed: [Mouti 2023](notes/mouti-2023-rough-volatility-range-based-estimators.md) (OHLC formulas), [Katsiampa 2017](notes/katsiampa-2017-volatility-estimation-bitcoin-garch.md) (GARCH on Bitcoin), [Lensky and Hao 2023](notes/lensky-2023-short-term-volatility-order-flow-images.md) (order-flow nowcast), [Yin et al. 2015](notes/yin-2015-genetic-programming-realised-volatility-forecasting.md) (genetic programming).

## Neighbouring works not noted here

These were named in the task leads or surfaced in search results but were not opened in this session, so they have no note and nothing above relies on them: the original range-estimator papers (Parkinson; Garman and Klass; Rogers and Satchell; Yang and Zhang 2000) and Molnár's 2012 comparison, for which no open copy could be fetched; Kelly's 1956 paper and Thorp's long treatment of the Kelly criterion; a replication study of Katsiampa 2017; Korkusuz and Sahiner 2025 and Brauneis and Sahiner 2024 on HAR versus machine learning in crypto; Ding et al. 2025 on genetic programming for crypto volatility; and 2026 arXiv papers on perpetual-exchange liquidation mechanics (auto-deleveraging, slippage-at-risk). Regime-switching volatility models belong to topic 01 and implied-volatility signals to topic 20.
