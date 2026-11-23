# Topic 12 synthesis: time oscillators, cyclical encodings and cycle analysis

Scope: how to turn clock time into model inputs, and how to detect cycles in price. Which hours and days matter empirically is covered by topics 10 and 11 and is not repeated here. Sixteen sources were read; fifteen in full text and one (Boudt, Croux and Laurent) as an abstract only.

The short version: clock time is a strong, cheap and reliable input for volatility, volume and cost, and the tools for encoding it are settled. Price-cycle indicators (Hilbert, Fourier, wavelet and EMD "dominant cycle" methods) have no rigorous evidence of predictive value in anything read here, and the academic results that looked strong for decomposition features are largely explained by look-ahead leakage.

## What the literature agrees on

1. **Intraday periodicity lives in the second moment and is large.** Volatility has a deterministic time-of-day and time-of-week shape that distorts any model that ignores it. A handful of sine and cosine terms fitted to log squared returns captures it ([Andersen and Bollerslev 1997](notes/andersen-1997-intraday-periodicity-volatility-persistence.md)). The standard treatment is multiplicative: return volatility = slow level x periodic factor, with the periodic factor averaging one.

2. **The periods are known in advance.** In 24-hour FX the seasonal sits at integer cycles per day; what drifts is amplitude, not frequency ([Vatter et al. 2013](notes/vatter-2013-intraday-spot-volatility-trend-seasonality.md)). Fixed-period harmonics of the day and week are therefore the right basis, and there is little to gain from estimating the period.

3. **The seasonal must be estimated robustly and causally.** Jumps bias classical estimators ([Boudt et al. 2011](notes/boudt-2011-robust-intraweek-periodicity-jump-detection.md), abstract only). Windows centred on the present look ahead; a live estimate must use trailing data.

4. **How to encode time depends on the model.** Trees handle raw integer hour and weekday well. Linear models need a non-monotonic basis, and one sine and cosine pair is too rigid for a multi-peaked pattern; several harmonics or periodic splines are needed, plus interactions ([scikit-learn example](notes/scikit-learn-2025-time-related-feature-engineering.md)). RL environments feed `cos` and `sin` of the time angle to neural policies and advise against it for tree learners ([Salaorni et al. 2025](notes/salaorni-2025-gym4real-benchmarking-real-world-rl.md)). A genetic program can use a raw hour terminal with comparison operators ([Neely and Weller 1999](notes/neely-1999-intraday-technical-trading-genetic-programming.md)).

5. **Clock time has not been shown to predict direction.** In the one evolutionary study, hour of day added no forecasting power for half-hourly FX direction, and apparent profits came from trading in illiquid hours ([Neely and Weller 1999](notes/neely-1999-intraday-technical-trading-genetic-programming.md)). An RL agent with lagged returns plus time-of-day `cos` and `sin` did not beat passive baselines ([Salaorni et al. 2025](notes/salaorni-2025-gym4real-benchmarking-real-world-rl.md)). Timestamp embeddings help Transformers on strongly periodic targets and do nothing for exchange rates, where a last-value forecast wins ([Zeng et al. 2022](notes/zeng-2022-are-transformers-effective-time-series.md)).

6. **Decomposition features leak unless computed on trailing data.** EMD, wavelets, SSA and the Hilbert transform use both sides of each point. Decomposing the full series before splitting produces error reductions above 90% that vanish, or turn slightly negative, under causal processing ([Jiang et al. 2024](notes/jiang-2024-signal-decomposition-leakage-time-series-prediction.md)). The same warning, with a rolling protocol and end-effect correction, is in [Leung and Zhao 2021](notes/leung-2021-hht-feature-generation-machine-learning.md).

7. **Edge estimates are the worst estimates.** The wavelet cone of influence ([Torrence and Compo 1998](notes/torrence-1998-practical-guide-wavelet-analysis.md)) and the EMD end effect ([Leung and Zhao 2021](notes/leung-2021-hht-feature-generation-machine-learning.md)) both say the most recent values, the only ones a live bot can use, are the least reliable, and more so at longer periods.

8. **A spectral peak is not a cycle until it beats a red-noise null.** Many real series give wavelet pictures that resemble AR(1) noise; significance must be tested against that background ([Torrence and Compo 1998](notes/torrence-1998-practical-guide-wavelet-analysis.md)). Short-scale coherence in Bitcoin is patchy and may be noise ([Kristoufek 2015](notes/kristoufek-2015-bitcoin-price-drivers-wavelet-coherence.md)).

## Where it disagrees or is weak

- **Constant versus time-varying seasonality.** Andersen and Bollerslev fit one shape per sample; Vatter et al. report the main daily amplitude ranging from about 0.6 to 1.4 within eight months. No source tests which choice forecasts better out of sample.
- **Fixed versus learned frequencies.** [Time2Vec](notes/kazemi-2019-time2vec-learning-vector-representation-time.md) finds learned frequencies beat fixed ones, but on event-sequence tasks where the period is unknown and the signal is clean. The FX evidence says the frequencies are fixed integers. Nothing read tests Time2Vec on financial returns.
- **Whether positional and timestamp embeddings matter.** [Irani and Metsis 2025](notes/irani-2025-positional-encoding-time-series-survey.md) report 5 to 12% accuracy gains from positional encoding, but only for classification of physiological and sensor data, and the paper is inconsistent about its own experimental scope. Zeng et al. show the embeddings do not rescue Transformers on financial data.
- **Whether causal decomposition features help at all.** Leung and Zhao report modest MSE gains from Hilbert-Huang features on four daily financial series under a causal protocol; Jiang et al. find none on six physical series. Different domains, different models, no replication of either.
- **Ehlers's cycle indicators.** The three papers read ([MAMA and the Hilbert discriminator](notes/ehlers-2001-mama-hilbert-transform-adaptive-average.md), [Fourier transform](notes/ehlers-2006-fourier-transform-for-traders.md), [bandpass "EMD"](notes/ehlers-2009-empirical-mode-decomposition-cycle-trend.md)) give complete code and almost no evidence: one three-year, long-only stock backtest and several charts. The estimators always return a period inside their clamp range, on any input. It is a standard result, not sourced from a paper read in this session, that band-limiting filters applied to random walks produce smooth pseudo-cycles; none of the Ehlers papers tests against that null. No independent test of these indicators was found.
- **Crypto-specific evidence is thin.** Only Kristoufek is crypto, and it is daily data from 2011 to 2014. Hansen, Kim and Kimbrough, "Periodicity in Cryptocurrency Volatility and Liquidity" (arXiv 2109.12142, opened but owned by topic 10), report that GARCH-type models with day-of-week periodicity fit BTC and ETH better in and out of sample and link within-day patterns to perpetual funding times; it is the closest crypto evidence for point 1.
- **RL and evolutionary evidence is sparse and old.** The RL source has no ablation of time features. The evolutionary source is FX from 1996. Nothing was found that evolves or learns time encodings on crypto.
- **Not covered at source.** Gallant's 1981 Fourier flexible form paper (no abstract or open text), Hurst's cycle work (no credible source located), Huang et al.'s original EMD paper, and Granger and Morgenstern's spectral study of stock prices were not read; see the gaps in the run report.

## Candidate signals and methods

### Explicit oscillator formulas

Let `u` be Unix time in seconds (UTC).

Phases in [0, 1):

```
x_day  = (u mod 86400) / 86400                     # 0 at 00:00 UTC
x_week = ((u + 259200) mod 604800) / 604800        # 0 at Monday 00:00 UTC (epoch was a Thursday)
x_fund = ((u - f0) mod 28800) / 28800              # 0 at each 8-hour funding time; f0 = any funding timestamp
```

Time-of-day oscillator, harmonic k = 1..K_d:

```
TOD_sin[k] = sin(2*pi*k*x_day)
TOD_cos[k] = cos(2*pi*k*x_day)
```

k = 1 is the 24-hour cycle, k = 2 is 12 hours, k = 3 is 8 hours (the funding period when funding falls on 00:00, 08:00 and 16:00 UTC), k = 4 is 6 hours. K_d = 4 to 6 is the range used by Andersen and Bollerslev. A single oscillator peaking at hour h0 is `cos(2*pi*(x_day - h0/24))`.

Time-of-week oscillator, harmonic k = 1..K_w:

```
TOW_sin[k] = sin(2*pi*k*x_week)
TOW_cos[k] = cos(2*pi*k*x_week)
```

k = 1 is the 7-day cycle; k = 7 on the week equals k = 1 on the day, so keep K_w at 3 or below and carry intraday detail in the TOD terms. A weekend flag times the TOD terms lets the daily shape differ on Saturday and Sunday.

Local-clock variant, because US and European sessions move by an hour in UTC with daylight saving: compute `x_ny` from seconds since local midnight in America/New_York and add `sin(2*pi*x_ny)`, `cos(2*pi*x_ny)`.

Tree-model variant: `minute_of_day = floor((u mod 86400) / 60)`, `day_of_week = floor(((u + 259200) mod 604800) / 86400)` as integers.

Fitted volatility seasonal (Fourier flexible form), on 5-minute returns `r` with trailing daily variance `v`:

```
y = 2*log|r - mean(r)| - log(v) + log(288)
y ~ c + sum_k [ a_k*cos(2*pi*k*x) + b_k*sin(2*pi*k*x) ] + dummies(funding bins, scheduled releases)
s(x) = exp(fit/2), rescaled so mean(s^2) = 1
amplitude_k = sqrt(a_k^2 + b_k^2),  phase_k = atan2(b_k, a_k)
```

with `x = x_week` and k drawn from weekly harmonics {1, 2, 3} and daily harmonics {7, 14, 21, 28}. Standardized return = `r / (sqrt(v/288) * s)`.

### Table

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Time-of-day and time-of-week harmonics as features | Timestamp only | minutes to hours | A for volatility and volume targets; no support for direction | [andersen-1997](notes/andersen-1997-intraday-periodicity-volatility-persistence.md), [scikit-learn-2025](notes/scikit-learn-2025-time-related-feature-engineering.md), [neely-1999](notes/neely-1999-intraday-technical-trading-genetic-programming.md) |
| FFF volatility seasonal factor, static | 5-minute returns from a liquid venue, daily variance | minutes | A | [andersen-1997](notes/andersen-1997-intraday-periodicity-volatility-persistence.md) |
| Rolling FFF with amplitude and phase tracking | Same, trailing two-week window | minutes to hours | B | [vatter-2013](notes/vatter-2013-intraday-spot-volatility-trend-seasonality.md) |
| Robust time-of-week scale and seasonally adjusted shock flag | Returns, jump-robust local volatility | minutes | A for the method (abstract only); implementation untested | [boudt-2011](notes/boudt-2011-robust-intraweek-periodicity-jump-detection.md) |
| Periodic splines or multi-harmonic basis for linear and neural models | Timestamp | minutes to hours | C | [scikit-learn-2025](notes/scikit-learn-2025-time-related-feature-engineering.md) |
| Time2Vec learnable time embedding | Timestamp scalars | minutes to hours | B on non-financial tasks; untested in finance | [kazemi-2019](notes/kazemi-2019-time2vec-learning-vector-representation-time.md) |
| RL state with `cos` and `sin` of time angle | Returns window, timestamp, position | minutes | C; no ablation, agent did not beat baselines | [salaorni-2025](notes/salaorni-2025-gym4real-benchmarking-real-world-rl.md) |
| Evolved rules with hour-of-day terminal and cost-aware fitness | Normalized price, hour, carry variable | minutes to hours | B; negative result net of costs | [neely-1999](notes/neely-1999-intraday-technical-trading-genetic-programming.md) |
| Positional encoding plus clock features in a Transformer | Bar index, timestamp | minutes to hours | C for classification; B negative for financial forecasting | [irani-2025](notes/irani-2025-positional-encoding-time-series-survey.md), [zeng-2022](notes/zeng-2022-are-transformers-effective-time-series.md) |
| Hilbert homodyne dominant-cycle period and phase | Bar midpoints | bars (any) | D | [ehlers-2001](notes/ehlers-2001-mama-hilbert-transform-adaptive-average.md) |
| Rolling DFT dominant cycle and spectral concentration | Bar midpoints, 50-bar window | bars (any) | D | [ehlers-2006](notes/ehlers-2006-fourier-transform-for-traders.md) |
| Bandpass oscillator and trend-versus-cycle regime flag | Bar midpoints | bars (any) | D | [ehlers-2009](notes/ehlers-2009-empirical-mode-decomposition-cycle-trend.md) |
| Rolling wavelet coherence and phase between two series | Two return series | hours to days | B descriptive; unusable at the live edge for long scales | [kristoufek-2015](notes/kristoufek-2015-bitcoin-price-drivers-wavelet-coherence.md), [torrence-1998](notes/torrence-1998-practical-guide-wavelet-analysis.md) |
| Causal CEEMD and Hilbert features with end-effect factor | Trailing price window | daily tested; intraday untested | B, modest MSE gain | [leung-2021](notes/leung-2021-hht-feature-generation-machine-learning.md) |
| Red-noise significance test for any claimed cycle | Returns or log-volatility | n/a | A (method) | [torrence-1998](notes/torrence-1998-practical-guide-wavelet-analysis.md) |
| Causality audit for filtered or decomposed features | Any feature pipeline | n/a | B (method) | [jiang-2024](notes/jiang-2024-signal-decomposition-leakage-time-series-prediction.md) |
| Shuffle test and last-value baseline for sequence models | Any forecasting model | n/a | B (method) | [zeng-2022](notes/zeng-2022-are-transformers-effective-time-series.md) |

Suggested default for the bot: integer clock features for tree models, four daily harmonics plus three weekly harmonics plus a funding-phase pair for neural and linear models, a rolling robust FFF seasonal for volatility scaling, and no price-cycle indicator in production until it passes the tests below.

## Open questions worth testing on SOL perps

1. **Does clock time predict anything beyond volatility and cost?** Fit direction models with and without the harmonic block on walk-forward SOL data. The prior from Neely and Weller is no. Check separately for the hours around funding.
2. **Static or rolling seasonal?** Compare a full-sample FFF, a trailing two-week FFF and a robust time-of-week median scale by out-of-sample log-likelihood of standardized returns. Track `amplitude_1` through time on Binance SOL to see whether the daily pattern is strengthening or fading.
3. **How many harmonics?** Choose K_d and K_w by out-of-sample fit, and test whether the 8-hour harmonic (k = 3) and funding dummies add to a 24-hour basis.
4. **UTC clock or local clocks?** Test whether adding a New York local-time pair improves the seasonal fit across daylight-saving changes.
5. **Kalshi versus offshore shape.** Estimate the seasonal on Binance, Coinbase and Kalshi separately. A US-regulated venue may have a US-hours liquidity shape that differs from the global one; spreads and depth by time of week matter more for the bot than volatility.
6. **Fixed harmonics versus Time2Vec versus splines** as the time block of the same neural model, under identical walk-forward splits.
7. **Does an RL agent use its time inputs?** Ablate the `cos` and `sin` state entries and compare net P&L and turnover by hour.
8. **Is there any band-limited component in SOL returns?** Run a periodogram and Morlet power on 5-minute returns with an AR(1) null and a multiple-testing correction, looking specifically at 8-hour, 24-hour and 7-day periods. Do the same on signed funding-window returns.
9. **Do Ehlers-style adaptive periods beat fixed ones?** Same oscillator, adaptive look-back versus fixed look-back, net of fees, with the indicator also run on shuffled-return surrogates to measure the false-discovery rate.
10. **Do causal CEEMD or wavelet features add anything intraday?** Use the trailing-window protocol only, and report against the same model without them.
11. **Evolutionary search with cost-aware fitness.** Repeat the Neely and Weller design on SOL with integer minute-of-day and funding-phase terminals, a separate selection period, and a liquidity-hours restriction.
12. **Is the cycle versus trend regime flag informative?** Test whether momentum and mean-reversion signals from other topics perform differently conditional on the bandpass regime flag, against a simple efficiency-ratio alternative.

## Reading order

1. [Andersen and Bollerslev 1997](notes/andersen-1997-intraday-periodicity-volatility-persistence.md): the Fourier flexible form and why periodicity must be removed.
2. [Vatter et al. 2013](notes/vatter-2013-intraday-spot-volatility-trend-seasonality.md): the seasonal drifts; rolling FFF.
3. [Boudt et al. 2011](notes/boudt-2011-robust-intraweek-periodicity-jump-detection.md): robust, intraweek estimation (abstract only).
4. [scikit-learn example](notes/scikit-learn-2025-time-related-feature-engineering.md): encodings by model class, with code.
5. [Kazemi et al. 2019](notes/kazemi-2019-time2vec-learning-vector-representation-time.md): learnable time embeddings.
6. [Zeng et al. 2022](notes/zeng-2022-are-transformers-effective-time-series.md): what embeddings do not fix; baselines to keep.
7. [Neely and Weller 1999](notes/neely-1999-intraday-technical-trading-genetic-programming.md): evolved intraday rules with a time-of-day input, net of costs.
8. [Salaorni et al. 2025](notes/salaorni-2025-gym4real-benchmarking-real-world-rl.md): time in an RL trading state.
9. [Torrence and Compo 1998](notes/torrence-1998-practical-guide-wavelet-analysis.md): how to test a cycle claim.
10. [Jiang et al. 2024](notes/jiang-2024-signal-decomposition-leakage-time-series-prediction.md): leakage in decomposition features.
11. [Leung and Zhao 2021](notes/leung-2021-hht-feature-generation-machine-learning.md): a causal protocol for EMD and Hilbert features.
12. [Kristoufek 2015](notes/kristoufek-2015-bitcoin-price-drivers-wavelet-coherence.md): wavelet coherence on Bitcoin.
13. [Ehlers 2001](notes/ehlers-2001-mama-hilbert-transform-adaptive-average.md), [Ehlers 2006](notes/ehlers-2006-fourier-transform-for-traders.md), [Ehlers and Way 2009](notes/ehlers-2009-empirical-mode-decomposition-cycle-trend.md): practitioner cycle indicators, for the code.
14. [Irani and Metsis 2025](notes/irani-2025-positional-encoding-time-series-survey.md): positional encodings, lowest priority.
