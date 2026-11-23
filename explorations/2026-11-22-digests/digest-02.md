# Digest of pack-02 (Q33 to Q60)

Tags are (slug, grade, paper|note). "synthesis" means a research-agent summary: its numbers are pointers, not verified source text.

Q33. Does volume x return predict continuation versus reversal?
- Established: Crypto short-term reversal is the pay for providing liquidity and sits in low-abnormal-volume pairs and small, illiquid coins; after high-volume moves and in large liquid coins it is near zero or negative (bianchi-2022, B, note). De-trended volume alone has little value; the double sort with lagged return carries it (bianchi-2022, B, paper p.13). Across 2,226 stocks the sign follows information asymmetry (llorente-2002, A, note).
- Weak or missing: All daily; intraday crypto untested (synthesis).
- For this system: add return x relative Binance volume as an interaction feature; test sign stability at 15 minutes.

Q34. What separates informed from uninformed or forced flow?
- Established: Bitcoin metaorders making up more than 75% of market net imbalance over [t0, t0+10T] ("isolated", about 3% of metaorders) have impact decaying far below the 2/3 level; typical metaorders are correlated with the rest of the market and keep impact (donier-2015, A, paper p.15). VPIN treats the normal level of buys and sells as uninformed, abnormal imbalance as informed (easley-2012, B, paper p.8; passage cut off).
- Weak or missing: Scores only 0.60. Nothing on liquidation flow or perps.
- For this system: label a burst "herded" when three-venue signed flow agrees, "isolated" when one venue acts alone; test whether isolated bursts revert (inference).

Q35. Retail front-end versus algorithmic traders.
- Established: Hyperliquid, ten most active perps, 27 Mar 2025 to 30 Jun 2026: front-end (manual) traders lose USD 1.11 billion, market makers gain USD 208 million, algorithmic takers about break even, valued at the mid two hours later net of fees. Channels: voluntary trading (large aggressive orders scaling little with displayed liquidity), forced liquidations, fees (jia-2026, B, paper p.1). Front-end traders open with recent returns, the others against; impact after front-end trades starts favourable, then decays (jia-2026, B, note).
- Weak or missing: Extended abstract; no per-trade magnitudes. Kalshi's client mix unknown.
- For this system: split Kalshi maker markouts by whether the taker traded with the prior 5 to 15 minute return.

Q36. Visible scheduled orders on Hyperliquid as known future flow.
- Established: 4.3 million reconstructed hidden metaorders against 465,000 visible TWAPs: TWAPs pay less and leave smaller permanent impact; hidden same-direction metaorders alongside pay more; displayed depth rises and tilts to the absorbing side (barone-2026, B, paper p.1). Drift formula 0.186 x sigma_daily x eta^0.118 x F^0.306 is a note pointer (barone-2026, B, note). The informed wallet cohort follows Binance at 2, 5 and 10 seconds; a minority anticipates it persistently out of sample (lim-2026-binance-leads, C, paper p.2).
- Weak or missing: Preprints; synthesis flags "one asset, 29 days". No SOL result; Hyperliquid is not recorded.
- For this system: nothing until a Hyperliquid feed exists.

Q37. How much contemporaneous price change does net order flow explain?
- Established: Best-quote OFI explains mid changes linearly, slope inversely proportional to depth, far better than signed trade volume; contemporaneous, not predictive (cont-2014, A, note). Pointers: best-level OFI about 65%, ten-level about 87% in sample, trade imbalance 32%; one-minute-ahead out-of-sample R-squared negative for every model; lagged imbalance predicted for 30 minutes in 1996, 5 in 2002 (synthesis). Daily FX: R-squared 0.64 and 0.45, no next-day reversal (evans-2002, A, note).
- Weak or missing: On BitMEX trade flow beat OFI (silantyev-2019, B, note, abstract only).
- For this system: depth-scaled OFI as the replay simulator's impact model, not a forecast feature.

Q38. Multi-level versus top-of-book OFI.
- Established: With Ridge, levels to the tenth are significant; out-of-sample RMSE improves 65 to 75% for large-tick and 15 to 30% for small-tick stocks (xu-2019, B, note). In-sample R-squared rises from 71.16 (one level) to 89.38 (ten); out-of-sample from 64.64 to a peak of 83.16 at eight levels (cont-2023, A, paper p.34). Depth at levels 5 to 10 matters less than the top but significantly (sirignano-2019, A, paper p.11).
- Weak or missing: All contemporaneous; for forecasting integrated OFI is no better than best-level (synthesis).
- For this system: cap book features at about eight levels.

Q39. Does a large absorbing resting order predict direction?
- Established: Nothing scored above 0.5. Best passage: long memory in order signs is reconciled with efficiency by the hypothesis that after a run of buys the next buy is less likely to penetrate the best price, through more ask volume or a smaller order (lillo-2004, A, paper p.12).
- Weak or missing: No test of absorption as a direction signal.
- For this system: test the absorption feature as a predictor of fill quality for resting orders ("price does not move"), not direction.

Q40. Where does intraday reversal give way to momentum?
- Established: Mean AUC for crypto 0.536, 0.521, 0.496 at 15 minutes, 1 hour, 4 hours; coupling about -0.13 at 1 hour fading toward zero at 4; significant in 4 of 4 coins at 1 hour (SOL from a refetch); 4-hour sample about 103, "suggestive only" (kitron-2026, B, paper p.19). First half-hour predicts the last positively, second-to-last negatively (shen-2022, A, note). Cross-sectional momentum lasts two to four weeks, reversal beyond a month (dobrynskaya-2023, B, note).
- Weak or missing: The crossover is located for no crypto asset (synthesis).
- For this system: map SOL autocorrelation by lag from 5 minutes to 12 hours on Binance.

Q41. What follows a large one- or two-hour bitcoin move?
- Established (note or synthesis only): Bitstamp 2015 to 2018 autocorrelation -0.056 at one hour and -0.086 at two, rising to -0.19 after five-sigma one-hour bars and -0.40 after six-sigma two-hour bars (denicola-2021, B, note; synthesis). Per-trade 0.3% to 0.7% after two- to four-sigma two-hour moves, in-sample, before fees. Kitron: 15-minute reversal in 90% of 183 Binance pairs, gross edge near 1.3 bp against a 5 bp round trip (synthesis).
- Weak or missing: No paper text; old spot data; no net-of-cost test.
- For this system: event-study resting entries after k-sigma 15-minute to 2-hour moves, by shock size.

Q42. Does the first half-hour predict the last half-hour in crypto?
- Established: Slope 0.968, Newey-West t 4.38, R-squared 1.44% (shen-2022, A, paper p.11); 2.12% with the second-to-last half-hour; out-of-sample 1.09%, 1.40%, 1.61%; 3.86% on high-volume days, insignificant on low-volume days; break-even 3, 7 and 10 bp per trade; sessions defined by volume (shen-2022, A, note). Attributed to liquidity provision.
- Weak or missing: BTC spot to 2020; gao-2018 abstract only; nothing on SOL.
- For this system: 7 to 10 bp exceeds a 4 bp maker round trip; test the second-to-last half-hour fade with resting orders only.

Q43. How do liquidation cascades unfold, and when does the rebound begin?
- Established: Flash-crash anatomy: mechanical seller, thin intermediary inventory, volume explosion, rebound when discretionary buyers arrive; crypto has no co-ordinated pause and falling prices create more forced selling (kirilenko-2017, B, note). After a Hyperliquid cascade pricing recovers within three weeks while depth stays contracted at 30 days, 38% and 42% for BTC and ETH (lim-2026-liquidity-recovery, B, paper p.11).
- Weak or missing: No timing rule; no minute-scale signed-return study.
- For this system: carry spread and depth ratios separately; no entry rule is supported.

Q44. Does the perp overshoot spot in a crash?
- Established: Around large spot moves quarterly futures overshoot by 8 to 10% of the move, perpetuals about 3%, closing within hours (gornall-2025, B, note); within 16 hours the perp has lost less than spot because funding pays the losing side (gornall-2025, B, paper p.27). On 3 January 2024 the perp's response overshot above 1.25 while spot rebounded to 0.7 to 1 (shen-2026, B, note).
- Weak or missing: The cushion is funding; Kalshi funding is usually zero (inference).
- For this system: measure the Kalshi-minus-index gap after 3-sigma index moves and its half-life.

Q45. Is crypto time-series momentum real at hourly to weekly horizons after costs?
- Established: A one-standard-deviation BTC daily return (5.55%) predicts +0.33% next day, also days 3, 5, 6; weekly +3.16%, 3.66%, 3.49%, 1.50% at one to four weeks (liu-2021, A, paper p.21). Top weekly quintile 11.22% per week (Sharpe 0.45) against 2.60% (0.19) (liu-2018-attention, B, paper p.21).
- Weak or missing: No costs; pre-2018; nothing hourly. May be drift plus volatility timing (synthesis).
- For this system: at most a slow daily state biasing which side rests; untested on SOL.

Q46. Do support, resistance or round numbers cause bounces or cascades?
- Established: Published FX levels bounce 60.8% against 56.2% for random levels (osler-2000; synthesis pointer). Round numbers raise bounce frequency by 4.6 percentage points in actual rates, 3.4 in simulations (osler-2003, A, paper p.30). Bounce probability rises with prior bounces, absent in shuffled series; unprofitable after costs and delay (garzarelli-2011, B, paper p.17); repeated on 2018 one-minute data (chung-2021, B, note).
- Weak or missing: FX and equities; no crypto test.
- For this system: test bounce rates at SOL round dollars and rolling extremes against shuffled returns.

Q47. Stop-loss clusters and price cascades.
- Established: Rates move unusually fast after reaching stop-loss cluster levels; the response is larger and longer than at take-profit clusters, significant for hours, not days (osler-2002, B, paper p.1). 14.4% of stop-loss buys sit at rates ending 01 to 10 against 7.4% at 90 to 99; take-profits show no asymmetry (osler-2003-technical, B, paper p.20). Dollar-mark moved 0.061% against 0.054% in 15 minutes after crossing a round number (synthesis pointer).
- Weak or missing: FX 1996 to 1998; about 0.7 bp.
- For this system: a "just crossed a round number" veto on fade entries.

Q48. Does high volume make a return more or less likely to reverse?
- Established: High-volume moves reverse more because they reveal non-informational pressure (campbell-1993, A, note). In crypto, value-weighted reversal earns 0.6% daily (p 0.001) after low abnormal volume and -0.18% (p 0.543) after high (bianchi-2022, B, paper p.14). Wash-trade volume lifts the same week's return and reverses the next (cong-2023, A, paper p.30). Many small sell fills consuming little volume raise reversal probability; large taker volume points to further drop (albers-2025, B, paper p.33).
- Weak or missing: Sign disputed; no intraday crypto test.
- For this system: split volume into trade count and average size.

Q49. Price jumps: predictors and aftermath.
- Established: One passage: cumulative returns up to a jump (half-hour return from close beyond the 10th or 90th percentile) positively predict later same-day returns, read as negative-gamma hedging (baltussen-2021, A, paper p.15). Pointer: after a bitcoin jump, volatility and volume stay high about an hour (scaillet-2020, synthesis).
- Weak or missing: Jump predictors and next-hour crypto direction are unanswered.
- For this system: a post-jump flag widening the cone for 60 minutes.

Q50. Do residual returns against bitcoin and ether mean-revert?
- Established: Nothing scored above 0.5; the best passage is unrelated summary statistics (liu-2022, A, paper). Pointers only: residual s-score with Ornstein-Uhlenbeck fit graded A in equities, C in crypto; crypto pairs revert at 5-minute and hourly bars but not daily (fil-2020, abstract only; synthesis).
- Weak or missing: Everything.
- For this system: estimate the half-life of SOL's residual against BTC and ETH before using it.

Q51. End-of-day or end-of-session reversals.
- Established: In US stocks the return from prior close to 3:00pm negatively predicts the 3:30 to 4:00pm return, t -4.18; both overnight and intraday parts revert (baltussen-2026, B, paper p.15). Index-level end-of-session flow is trend-following, asset-specific flow contrarian; 3 to 6 bp per day (baltussen-2026, B, note).
- Weak or missing: Equities only.
- For this system: test SOL-minus-BTC and market-wide returns into the US close separately, expecting opposite signs.

Q52. Best realised-volatility model.
- Established: For bitcoin, GARCH-type models are about 19% worse than HAR at one day and 3 to 6% worse at 7 to 60 days by RMSE (huang-2024, B, paper p.11); neural networks beat HAR narrowly and inconsistently (huang-2024, B, note). AR(30) matches HAR; LSTMs and a rough-volatility model beat it; pooled models beat per-coin ones (tang-2023, B, note). Genetic programming with volume, trade count, spread and duration beats HAR; combining is better (yin-2015, C, note).
- Weak or missing: All daily; no EWMA comparison; intraday HAR on crypto perps untested (synthesis).
- For this system: HAR on deseasonalised log RV against EWMA, by QLIKE, at 15 minutes, 1 hour, 4 hours.

Q53. Time-of-day volatility pattern and deseasonalising.
- Established: The first minute of each hour is the most volatile, with peaks every 15 minutes and smaller ones every 5, strongest every fourth hour except 08h; conjectured cause is perp funding (hansen-2024, A, paper p.22). Volatility, spread, volume and trade count peak 16:00 to 17:00 UTC, coinciding with CME CF reference-rate calculation (brauneis-2025, A, note). Pointers: trough near 05:00 UTC; periodicity added about 34 log-likelihood units against 18 for realised variance; weekend about 75% of weekday (synthesis).
- Weak or missing: BTC and ETH, 2018 to 2021; nothing for SOL or Kalshi.
- For this system: hour-of-day plus minute-of-hour seasonal factor before every volatility-scaled feature.

Q54. Forecasting range or touch probability within an hour.
- Established: Nothing. The only passage is the caveats of a D-grade note on a 48-hour touch test on SPY hourly bars, whose 68.8% may be at or below the base rate (steversteves-2022, D, note).
- Weak or missing: The whole question.
- For this system: score the cone's touch and band probabilities against the hourly range-contract quotes, the only external benchmark available.

Q55. Volatility spillovers from Binance perps.
- Established: At five-minute resolution the Binance USDT perpetual sends strong positive spillovers to all instruments and receives little; total spillover about 30% higher in European and US hours; a volume rise precedes a volatility rise by one interval; Coinbase trades in 84% of seconds, Bitstamp and Kraken about one in four (alexander-2021, B, note and paper p.26). Binance leads Hyperliquid in 400 of 580 hourly windows, ties in 177, lags in 3 on a five-second grid (lim-2026-binance-leads, C, paper p.9).
- Weak or missing: BTC, early 2021.
- For this system: forecast Kalshi SOL volatility from Binance SOL RV and lagged Binance volume.

Q56. Does implied volatility beat past volatility in crypto?
- Established: Bitcoin implied volatility is worse than time-series models for next-day volatility, better at 7 to 15 days, and adds value in combination at every horizon (hoang-2020, B, note; abstract only per synthesis). One-month variance risk premium about 0.14 annualised (almeida-2024, synthesis pointer).
- Weak or missing: No SOL options; nothing intraday.
- For this system: nothing directly. The range contracts are this system's implied distribution; test them for the same upward bias.

Q57. Quantile and probabilistic forecasts.
- Established: Three recipes from point forecasts: residual simulation (QRS), quantile regression stacking with pinball loss, quantile regression forest; scored by CRPS, pinball, calibration frequency and Winkler (dudek-2025-probabilistic, B, note). CRPS 1.07E-03 for QRS-HAR against 8.13E-04 for QRS-LGBM; Diebold-Mariano not significant except once; baselines underestimate quantiles below 0.6 (dudek-2025-gradient-boosting, B, paper p.33).
- Weak or missing: Daily volatility quantiles, not return quantiles.
- For this system: score the cone by CRPS and per-quantile hit frequency at each lead.

Q58. Combining and scoring density forecasts.
- Established: Almost nothing. Multivariate models give no point-forecast gain for cryptocurrencies but large gains in predictive log score (catania-2018, B, paper p.16). The combination review passage only defines scope (wang-2022, B, paper p.40).
- Weak or missing: Pooling weights, linear versus log pools, scoring rules.
- For this system: judge cone variants by log score or CRPS, not directional accuracy.

Q59. Semivariance, signed jumps, realised skewness.
- Established: No passage tests them. Realised variance minus bipower variation estimates the jump part (barndorff-nielsen-2004, A, paper p.1). MedRV is robust to jumps and zero returns (alexander-2021, B, paper p.30). Crypto volatility responds positively to lagged returns, unlike equities (tang-2023, B, note). Pointer: liquidity measures predict the sign of RV change for SOL with accuracy 0.56 to 0.58 (easley-2024, synthesis).
- Weak or missing: The question itself.
- For this system: up and down semivariance as cheap features; expect little.

Q60. Sampling frequency and estimator for realised variance.
- Established: Five-minute RV is the standard sparse choice; Bandi-Russell picks a frequency from quarticity and noise variance (liu-2015, A, paper p.6). Five-minute returns give BTC about 88% and ETH 111% annualised (hansen-2021, B, paper p.9). Bitcoin RV drops 9.24% from 5- to 10-minute sampling (huang-2024, B, paper p.6). Five minutes is the highest reliable frequency for transmission analysis, using pre-averaged one-second data, diurnal adjustment, top 0.05% winsorised (alexander-2021, B, paper p.3, p.30).
- Weak or missing: Nothing on a thin venue; zero returns bias bipower variation low (barndorff-nielsen-2004, A, note).
- For this system: compute RV on Binance; draw a signature plot before trusting one-minute RV on Kalshi.

## Ideas from this block

1. Post-fill markouts on Kalshi split by taker type. Sources: front-end traders open with recent returns using large aggressive orders that ignore displayed depth; impact after their trades starts in their favour, then decays; their losses are mostly fees, execution and liquidations (jia-2026, Q35). Same-sign order runs are offset by lower penetration (lillo-2004, Q39). Inference: if Kalshi's takers resemble front-end traders, a resting order filled by a trend-chaser is under water briefly and recovers, so exit timing matters more than entry. Data: Kalshi trades with taker side, book, index. Kill: maker markout at 10 seconds, 1, 5, 30 and 120 minutes by taker direction against the prior 15-minute return and by size against depth; dead if it never recovers past the 2 bp maker fee.

2. Size-conditioned fade with a cascade veto. Sources: reversal grows with shock size (denicola-2021, Q41, note only); crypto reversal ranks direction at 15 minutes and 1 hour, gross edge near 1.3 bp (kitron-2026, Q40, Q41); continuation after crossing stop clusters lasts hours while reversal at take-profit clusters fades within 30 minutes (osler-2002, Q47); cascades self-extend (kirilenko-2017, Q43). Inference: rest fade orders after volatility-scaled moves unless the move just crossed a round number or rolling extreme. Data: Binance and Coinbase bars, sweeps feature. Kill: next-bar return with and without the veto; dead if the veto does not shrink the left tail.

3. One follow-versus-fade switch: return x volume, with volume split into count and size. Sources: bianchi-2022, llorente-2002, campbell-1993 (Q33, Q48); many small fills revert, large taker volume continues (albers-2025, Q48); momentum is stronger after high-volume openings (shen-2022, Q42); isolated metaorders revert (donier-2015, Q34). Inference: the conflicting signs may resolve once volume is decomposed and cross-venue agreement added. Data: Binance trades, three-venue signed flow. Kill: interaction coefficients on each half of the tape; dead if signs disagree.

4. Minute-of-hour seasonal meets the hourly range contracts. Sources: the first minute of each hour is the most volatile (hansen-2024, Q53); implied variance sits above realised (Q56, synthesis pointer). Inference: the contracts settle on a 60-second average at the top of the hour, inside the burst window, so cone coverage and range-quote bias should be checked for targets landing on :00. Data: cone archive, range quotes, index. Kill: coverage by minute-of-hour of the target; dead if :00 targets are as well calibrated as others.

5. Lead-venue volatility as the common denominator. Sources: the Binance perp transmits volatility and volume leads volatility by five minutes (alexander-2021, Q55); HAR beats GARCH (huang-2024, Q52); an hour of post-jump elevation (scaillet-2020, pointer); QRS quantiles (dudek-2025, Q57). Inference: a Binance-driven HAR with a lagged-volume term, wrapped in residual simulation, could set the cone's width. Data: Binance SOL trades. Kill: QLIKE and CRPS against EWMA times the seasonal factor.

6. Second-to-last half-hour fade into 5pm New York, resting only. Sources: shen-2022 (Q42), break-even 7 bp; asset-specific end-of-session flow is contrarian (baltussen-2026, Q51). Inference: 7 bp exceeds the 4 bp maker round trip. Kill: replicate on SOL 2025 to 2026; dead if out-of-sample R-squared is not positive.

7. Depth-scaled OFI as the simulator's impact law. Sources: cont-2014, cont-2023, xu-2019 (Q37, Q38). Inference: capped crossing orders in the replay should move price by OFI over depth, using up to eight levels. Kill: fit on Kalshi; dead if contemporaneous R-squared is below trade imbalance alone, as on BitMEX (silantyev-2019).

## Contradictions and surprises

- Volume and reversal: campbell-1993 says high volume means reversal; bianchi-2022 finds crypto reversal only after low volume; shen-2022 finds momentum stronger on high-volume days. llorente-2002 reconciles by information asymmetry, yet its cross-section (liquid names reverse after volume) is the opposite of Bianchi's (illiquid coins reverse). Where SOL sits is undetermined.
- After a shock: reversal (denicola-2021), continuation (caporale-2019, C, hindsight entry), continuation from hedging (baltussen-2021), continuation after stop levels (osler-2002).
- Against concluded item 2: kitron-2026 shows reversal fading to zero at four hours, not turning into continuation; its 4-hour sample is about 103.
- Against concluded item 5 (hour-of-day return rules): shen-2022 is grade A with out-of-sample R-squared up to 1.61% and a 7 to 10 bp break-even, above the maker round trip.
- Concluded item 5 on copying Binance holds: Binance leads at sub-five-second lags. The surprise is a persistent minority of Hyperliquid wallets that anticipate Binance (C grade).
- Deep book levels add much contemporaneously (xu-2019, cont-2023) but nothing for forecasting (synthesis), consistent with concluded item 5.
- OFI beats trade imbalance in equities (cont-2014); trade flow beats OFI on BitMEX (silantyev-2019, abstract only).
- Machine learning for volatility: LSTM beats HAR (huang-2024, tang-2023); LSTM is among the worst for quantiles (dudek-2025-probabilistic, synthesis); boosted trees win without Diebold-Mariano significance (dudek-2025-gradient-boosting).
- Retail losses are not mainly adverse selection (jia-2026): their trades are briefly right.
- Perps overshoot less than dated futures because of funding (gornall-2025); Kalshi's near-zero funding removes that anchor.
- Liquidity at the 16:00 UTC peak is disputed: lowest spreads (Dyhrberg, abstract) versus highest illiquidity (brauneis-2025).
