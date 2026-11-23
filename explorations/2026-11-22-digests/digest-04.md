Digest of pack-04 (Q90 to Q120). Tags are (slug, grade, paper|note|synthesis); note and synthesis numbers are pointers, not source text. Passages listed only as "(text under Qn)" were not printed in this pack.

Q90. Weekend versus weekday liquidity and volatility
- Established: GARCH with periodicity puts volatility below average at weekends and fits better in and out of sample; weekday shares may shift over time (hansen-2021, B, paper). Bitcoin average daily move 2020 to 2026: 3.10% weekdays, 2.33% weekends, about 75%; yet the 10 October 2025 weekend interval was 7.83% against 2.14% earlier that day (cmegroup-2026, C, note). Weekend crypto variance predicts Monday variance of S&P 500, gold and Treasuries (0.256, 0.447, 0.246), only after January 2024 (ebadollahyvahed-2026, B, paper and note).
- Weak or missing: lower weekend liquidity may raise impact per unit; unaddressed (kinateder-2021, B, note). Nothing on SOL or Kalshi.
- For this system: weekday/weekend volatility scaler for cone width and resting distance; tabulate Kalshi spread, depth and post-fill markout by weekday.

Q91. Does a time-of-day return repeat on following days?
- Established: in US stocks a half-hour return predicts the same half-hour on later days: continuation only at multiples of 13 half-hours (smallest t-statistic 9.62 in week one), negative at other lags (heston-2010, A, paper); lasts at least 40 days, attributed to institutional flow on repeating schedules (A, note).
- Weak or missing: cross-sectional equities; no crypto evidence here.
- For this system: test whether signed taker flow in a quarter-hour slot repeats at 24-hour lags on Binance.

Q92. Encoding time of day
- Established: boosted trees did best with raw integer hour and weekday; for a linear model one sine/cosine pair was worse than one-hot, and periodic splines matched one-hot; one pair is too rigid for several peaks (scikit-learn-2025, C, note).
- Weak or missing: one summary note; dataset not stated and not shown to be financial.
- For this system: integer minute-of-hour, hour and weekday for the tree learner; splines only for a linear baseline.

Q93. Dominant-cycle or spectral indicators
- Established: clock time is a strong, cheap input for volatility, volume and cost; Hilbert, Fourier, wavelet and EMD cycle indicators have no rigorous evidence, and strong decomposition results are largely look-ahead leakage (topic-12 synthesis, sixteen sources).
- Weak or missing: synthesis only.
- For this system: nothing; any smoothing feature must be strictly causal.

Q94. ML accuracy on the sign of crypto returns at 5 to 60 minutes
- Established: all models beat 50% and accuracy rises with horizon; boosting best at 5 minutes, ensemble at 15, LSTM at 60 (jaquart-2021, A, paper); 52 to 56%, negative after 30 bp (A, note; synthesis). Twelve coins at 15 to 60 minutes: "over 69%" on many occasions, no costs (akyildirim-2021, B, paper). Daily: trading only when five of six models agree was positive after 0.5% round trip (sebastiao-2021, A, note).
- Weak or missing: 69% is far above the 51 to 56% prior and unexplained.
- For this system: score each cone lead against 52 to 56%; much higher triggers a leak audit.

Q95. Linear or shallow versus deep
- Established: networks peak at three hidden layers; trees pick under six leaves (gu-2020, A, paper). On BTC/ETH/SOL/XRP at 5 minutes to 4 hours a three-parameter shape-constrained logit beat a free AR(12) logit on out-of-sample log-loss in 15 of 15 cells; free AR(24) weights flip sign in 30% of folds, the constrained kernel never; boosted trees and an MLP lost in all cells; BTC 1 hour: 0.6918 against base rate 0.6931, GBM 0.6933, MLP 0.7005 (kitron-2026, B, paper).
- Weak or missing: deep models win only at tick horizon (sirignano-2019, A, note).
- For this system: a constrained lagged-return kernel as baseline per lead, scored against 0.6931.

Q96. Which features matter
- Established: random forest, January 2021 to July 2023: average AUC above 0.55, single features 0.54 to 0.61, skewness 0.50; Roll measure and VPIN drive it (easley-2024, B, paper). Order-flow inputs are in the best-model set 65 to 89% of the time against 5 to 11% for raw levels (lucchese-2022, synthesis). Feature rank stable across five Binance perps (bieganowski-2026, synthesis). Features admitted only if they beat the layer below (jeon-2026, B, paper).
- Weak or missing: Easley's horizon is tagged daily and hours, not minutes.
- For this system: add Roll measure and VPIN per venue under staged admission.

Q97. Pooled models and transfer
- Established: a universal model trained on stocks 1 to 464 beat stock-specific models for all 25 held-out stocks (+1.45%), stable 18 months later; 19 months of training beat the last 1, 3 or 6 months by 7.2%, 3.7%, 1.6% (sirignano-2019, A, note). Fifteen benchmark models fell to 48 to 61% F1 on newer data (prata-2023, synthesis).
- Weak or missing: tick-horizon equities; no venue-to-venue evidence; no study of transferring an RL policy to a similar asset (hambly-2021, B, note).
- For this system: pooled Binance fit calibrated on Kalshi against Kalshi-only, on held-out Kalshi weeks.

Q98. Label construction
- Established: evidence is thin. Triple-barrier rests on a student capstone on E-mini futures without costs and one crypto paper benchmarked against buy-and-hold; no controlled fixed-horizon versus triple-barrier comparison exists (topic-23 synthesis). The capstone used dollar bars, a CUSUM event filter, volatility-scaled barriers and a one-day limit (singh-2019, C, note).
- Weak or missing: everything quantitative.
- For this system: run that comparison on the tape, barriers at maker round trip plus measured adverse selection.

Q99. Meta-labelling
- Established: method only: a random forest decides take or skip for a moving-average or Bollinger rule from volatility, serial correlation, momentum and RSI (singh-2019, C, note). Rated C; the supermajority vote is A at daily and "helps by trading rarely more than by forecasting better" (signals synthesis).
- Weak or missing: no result numbers; nothing intraday.
- For this system: meta-label the fill: will a resting order posted now fill with non-negative markout.

Q100. Updating under drift
- Established: short windows adapt fast and hurt in stable periods (gama-2014, A, paper). Plain incremental updating is often worse than rolling retraining; DoubleAdapt claims better on daily stocks (zhao-2023, B, note). Refitting every period and trading the newest model gave the best gross and worst net return; switching only on a supermajority of recent fits roughly doubled net return against a static rule (martin-2019, synthesis).
- Weak or missing: no intraday crypto evidence on refit frequency.
- For this system: keep the last k policies; change behaviour only on a supermajority.

Q101. Multi-horizon forecasting
- Established: encoder-decoder models match DeepLOB at short horizons and beat it at 100 updates, on LSE data with over 46 million test samples (zhang-2021, B, paper). Seq2seq versions beat single-horizon counterparts at 10 to 50 updates, possibly because multi-horizon targets identify the book regime (lucchese-2022, B, paper).
- Weak or missing: horizons are book updates, not minutes.
- For this system: compare joint against per-lead fits of the twelve leads.

Q102. Deep order-book models beyond seconds
- Established: predictability lasts 50 to 300 book updates, up to about half a second; L2 beats L1 (lucchese-2022, B, paper). Binance BTC perp F1 falls from about 75 at one second to 41 at ten (berti-2025, synthesis). About two price changes (kolm-2023, A, note). A two-hour history beats 100 steps as input (sirignano-2019, A, paper).
- Weak or missing: "often up to a minute" is grade C (jha-2020, C, note).
- For this system: supports concluded item 5. Measure Kalshi horizons in price-change units; two price changes may be long in clock time on a slow venue (inference).

Q103. Stationarity, fractional differentiation, scaling
- Established: only a definition of fixed-width fractional differentiation (slepaczuk-2024, C, paper). Normalising by volatility, price or spread did not help the pooled model (sirignano-2019, A, note), yet the synthesis advises relative-unit features for porting across venues (bieganowski-2026).
- Weak or missing: no evidence fractional differentiation improves prediction.
- For this system: nothing new.

Q104. Foundation models and language models
- Established: off-the-shelf models forecast daily stock returns poorly and fine-tuning does not fix it; finance-native pretraining narrows the gap to CatBoost on lagged returns (rahimikia-2025, B, paper and note). Kronos: averaging more sampled paths improves IC; no crypto result found (shi-2025, B, note; paper passage garbled). Pretrained gains over a random walk were significant in two comparisons; removing the language model can preserve performance; a pretrained model may have seen the test period (zhu-2026, B, paper).
- Weak or missing: daily, no costs.
- For this system: nothing for direction; path averaging supports the cone.

Q105. Training on profit instead of forecast error
- Established: direct reinforcement trains the position function on profit or Sharpe with the previous position as input; it beat Q-learning and traded less (moody-1998, B, note). Prediction-oriented signals trade poorly after costs; cost-aware learning changes the portfolio (zhu-2026, B, paper, citing Jensen 2026).
- Weak or missing: no intraday crypto comparison; the jaddu-2023 passage is off-topic.
- For this system: both learners already optimise net return; add a forecast-plus-threshold rule as comparison.

Q106. Learned state representations
- Established: FineFT fits a variational autoencoder per regime and uses a conservative policy when recent states score below a threshold; ablation says this cuts maximum drawdown; it argues the state-to-return mapping drifts over days (qin-2025, B, paper and note). An autoencoder plus recurrent mixture-density world model trained a policy that stayed positive on held-out data: one stock, a few days (wei-2019, C, note).
- Weak or missing: single studies.
- For this system: a density score on the 38 features as the unfamiliar-state gate; check it predicts cone error.

Q107. Overlapping labels, purging, embargo
- Established: purge at least the label horizon plus the longest overlapping look-back, add an embargo, judge median and lower quantiles of path performance (skfolio-2026, D, note). A scheme without purging gave PBO 7.9% against 8.0% while every agent lost 35 to 59% over 58 days (gort-2022, C, note).
- Weak or missing: no uniqueness weights; no measured leakage inflation.
- For this system: 15-second forecasts with 60-minute labels overlap 240-fold (my arithmetic); purge 60 minutes plus look-back between blocks.

Q108. State, action, reward on perpetuals
- Established: durable results put the previous position in the state, the cost of changing position in the reward, and risk in the reward or volatility scaling: reward = price change x previous position - (half-spread + fee) x |position change| - funding x position (topic-24 synthesis; borrageiro-2022, B, paper). For a price taker a forecast plus one-step cost-aware rule is argued sufficient (ma-2025, synthesis).
- Weak or missing: every formulation assumes a price taker; none has queue state.
- For this system: add order status, queue position and order age to the state; the sufficiency argument does not cover resting orders (inference).

Q109. Where RL beats baselines in execution
- Established: with only time and inventory as state, RL was "vastly superior" to optimised submit-and-leave (nevmyvaka-2006, A, paper). RL-Exec beat TWAP by +2.25 bp at 30 minutes, +7.59 at 60, +22.96 at 120 (duflot-2025, B, paper; table partly garbled). Against that: TWAP at 0.39 bp beat every agent, 25 of 600 runs collapsed to never trading, and later wins are "not evidence that RL execution works" because the replay is frictionless (ardaiz-2026, B, paper).
- Weak or missing: no small venue.
- For this system: TWAP and submit-and-leave baselines; count never-trade collapses per seed.

Q110. Out-of-sample failure and seed variance
- Established: four of five seeds beat the baseline, p about 0.06 (lebiedz-2026, B, paper); CAGR -3% to +199% across them (synthesis). Information ratio 0.22 to 1.76 over 250 initialisations; 11 of 100 agents collapsed (henderson-2017, A, note); conclusions change between 30 and 100 seeds (topic-24 synthesis). Re-run elsewhere, MacroHFT lost 75% on ETH (topic-31 synthesis). Numerical RL fed funding, premium and taker-buy lost out of sample (wang-2026-m3ft, C, note).
- Weak or missing: nothing on tree-based fitted Q-iteration.
- For this system: at least 30 seeds; report worst seed and block-bootstrapped differences.

Q111. Hierarchical or regime-conditioned RL
- Established: EarnHFT computes a hindsight-optimal action value by dynamic programming as a teacher, then routes among trend-specialised agents (qin-2023, B, paper). MacroHFT reports BTC 3.03%, ETH 39.28% on about 20 trades each (zong-2024, B, note). FineFT reports lowest risk on four datasets against 12 baselines; hierarchical baselines had large drawdowns (qin-2025, B, note).
- Weak or missing: each method wins only in its own paper; twenty trades is no sample.
- For this system: hindsight-optimal Q on replay as ceiling and auxiliary target; regime routing is unsupported.

Q112. Offline RL and decision transformers
- Established: learning from a fixed log is counterfactual inference; distributional shift is the central obstacle; "every backtest-trained trading agent is an offline RL system" (levine-2020, B, note). Decision transformer, CQL, IQL and behaviour cloning all reproduce a logged expert; none is consistently best (yun-2024, C, note).
- Weak or missing: daily; experts fitted to the same path.
- For this system: the tape holds no resting-order outcomes of our own, so those action values rest wholly on the queue model (inference); restrict actions to supported regions.

Q113. Risk-sensitive rewards
- Established: a differential Sharpe reward gave inconsistent results, sometimes no learning (sadighian-2020, C, paper). Risk-sensitive RL is "necessary and immature" (hambly-2021, B, note). Sharpe ratios of high-frequency strategies are inflated by non-normality (bailey-2012, A, paper). A drawdown penalty encodes a horizon; a Sharpe objective can exploit volatility estimates (zhu-2026, B, paper).
- Weak or missing: nothing on CVaR or tail-penalised block fitness.
- For this system: keep the block tail penalty, sweep its weight, report what survives.

Q114. Genetic programming against random search
- Established: population 500 over 100 generations equals about 50,000 random strategies; genetic programming beat equal-intensity random search in 3 of 9 markets; a "lottery" control matches trade count and time in market (chen-2007, B, note and paper). Half-hour FX: strong predictability at zero cost, none after costs (neely-1999, B, paper); a fitted autoregression did as well (neely-2003, A, note). The top rule in selection was among the four worst of 100 out of sample; the majority vote was profitable; trained at 0.1% one way, tested at 0.05% (signals synthesis).
- Weak or missing: daily or FX, pre-2010.
- For this system: add the lottery control; train at fees above live.

Q115. Quality-diversity and ensembles
- Established: with a MAP-Elites archive, generation 20 was best out of sample; 80 more generations generalised worse (yun-2025, C, note). 500 crypto agents ended in the same leveraged long; three of five independent LLM searches gave nearly the same strategy (chen-2025, gencay-2026, synthesis).
- Weak or missing: grade C, daily; no test that diversity improves net return.
- For this system: archive by behaviour (trades per block, maker share, holding time), vote across cells, stop on validation.

Q116. LLM-driven strategy evolution
- Established: a planted oracle with Sharpe 35 passed every statistical test, so deflation does not catch leakage; honest evaluation rejected every discovered strategy up to 100 candidates; a pre-registered hypothesis faces almost no deflation (gencay-2026, B, paper). Infrastructure: one logged backtest entry point, leak-proof features, a rising threshold, a held-out window opened once (B, note). Joint feature-and-strategy evolution had the best out-of-sample Sharpe and the largest validation-to-test gap (kvasiuk-2026, C, paper).
- Weak or missing: daily equities and ETFs.
- For this system: log every replay evaluation; pre-register the few mechanism hypotheses.

Q117. Factor mining without redundancy
- Established: AlphaEvolve fingerprints a candidate after pruning redundant operations and reuses cached fitness (cui-2021, C, paper). Discarding correlated candidates versus scoring marginal contribution is unresolved (topic-25 synthesis).
- Weak or missing: one passage, about compute.
- For this system: fingerprint policies by actions on fixed probe slices; distinct fingerprints give the trial count (inference).

Q118. Simulator realism
- Established: the best generative order-book model is told apart from real data by a simple classifier most of the time; drift grows with rollout (nagy-2025, B, note). A usable simulator must be interactive and reproduce latency races, fill probability that falls when the signal is strong, and own impact with partial reversion; then strategies that looked better with size and aggressiveness flatten or decline; large-tick stocks (noble-2026, B, note and paper).
- Weak or missing: no crypto calibration.
- For this system: make queue-model fill probability depend on signal strength; calibrate from Coinbase trades that name the resting order.

Q119. Shielding inside hard limits
- Established: the credible positive results confine RL to timing inside fixed stops, to a fallback in unfamiliar states, or to scheduling an order (signals synthesis). In the cleanest perp head-to-head the headline agent was one seed of five and another lost money (lebiedz-2026, B, note).
- Weak or missing: no ablation with the shield removed.
- For this system: position cap, add-once, time stop and block loss limit sit outside both learners.

Q120. Costs in the objective and turnover
- Established: "train for the decision actually made"; economic training "moves assumptions inside the loss function"; perturb cost curves, turnover limits and delay (zhu-2026, B, paper). Pointers: break-even about one basis point for intraday FX rules trained without costs (topic-25 synthesis); MacroHFT made about 20 trades where baselines made hundreds (zong-2024, note).
- Weak or missing: no measured turnover-versus-cost curve.
- For this system: sweep the fee charged in fitness; plot trades per block against held-out net return.

## Ideas from this block

1. Signal-conditional fill model. Sources: fill probability falls when the signal is strong (noble-2026, Q118); offline learners are weakest where data do not cover the action (levine-2020, Q112). Inference: for real resting orders on Coinbase (trades name the order hit), measure fill probability and 1 to 5 minute markout by cone-forecast decile, then impose that curve on the Kalshi queue model. Data: Coinbase trades and books, cone history. Kill test: fill rate and markout are flat across deciles.

2. Meta-label the fill, not the direction. Sources: meta-labelling (singh-2019, Q99); selectivity beats forecasting (sebastiao-2021, Q94); Roll and VPIN dominate (easley-2024, Q96). Inference: side from the cone; a second classifier predicts "posted now, fills, markout covers 4 bp". Data: Kalshi book and trades. Kill test: AUC at or below 0.52 on purged held-out weeks, or selected fills no better than all fills.

3. Bracket both learners between a ceiling and two floors. Sources: hindsight-optimal Q (qin-2023, Q111); lottery trading and equal-budget random search (chen-2007, Q114); one-step cost-aware rule (ma-2025, Q108). Inference: report each learner as a fraction of the distance from lottery to hindsight optimum. Kill test: neither beats the lottery on held-out blocks; by Chen and Navet's reading there is then nothing to learn from this tape.

4. Low-parameter horizon kernel against shortest-lead dominance. Sources: the constrained logit was sign-stable where free weights flipped in 30% of folds (kitron-2026, Q95); multi-horizon targets help (Q101). Inference, joined to concluded item 3: give the agent a two or three parameter summary of the twelve leads, not twelve free inputs. Kill test: free-lead and kernel agents do equally on held-out blocks and importance is not concentrated on the 5-minute lead.

5. Supermajority across refits, counted by behavioural fingerprint. Sources: supermajority of recent fits doubled net return (martin-2019, Q100); vote of 100 rules (Q114); fingerprints (cui-2021, Q117); population collapse (Q115). Inference: vote among distinct fingerprint clusters only; the cluster count is the trial count. Kill test: the vote is no better than the median single policy out of sample.

6. Weekend-specific novelty gate and posting distance. Sources: weekend volatility about 75% of weekday with rare extremes (cmegroup-2026, hansen-2021, Q90); lower weekend liquidity (kinateder-2021); density gate (qin-2025, Q106). Inference: fit the gate separately for weekends and scale resting distance by the weekday volatility share. Kill test: weekend and weekday markouts and gate-trigger rates are indistinguishable on Kalshi.

7. Same-slot flow repetition. Source: same half-hour continuation at daily multiples from scheduled institutional flow (heston-2010, Q91). Inference, joined to concluded item 2: test whether first-10-second quarter-hour taker imbalance repeats in sign at the same slot on later days; if so it is known in advance. Data: Binance trades. Kill test: autocorrelation at lag 96 quarter-hours and its multiples (my arithmetic) is no larger than at neighbouring lags.

## Contradictions and surprises

- Akyildirim's "over 69%" against Jaquart's 52 to 56%; the synthesis takes the lower range as the prior.
- Kitron (includes SOL) has boosted trees worse than the base rate at one hour, while Gu says trees beat linear models. This bears on tree-based fitted Q-iteration: the regressor may fit worse than a constant.
- RL execution: Duflot reports +2 to +23 bp over TWAP; Ardaiz says no learned policy fairly beats TWAP; Nevmyvaka is positive on 2006 equities.
- Ardaiz collapse counts differ: 25 of 600 runs in the paper passage, 11 of 100 agents in two notes.
- MacroHFT is positive in its own paper and lost 75% on ETH when re-run by FineFT's authors.
- The differential Sharpe ratio is recommended in the RL synthesis and found unreliable by Sadighian.
- A two-hour book history improves a next-move forecast (Sirignano) although predictability lasts under a second (Lucchese): history length is not horizon. Concluded item 5 stands.
- Heston's same-slot continuation sits beside concluded item 5's rejection of hour-of-day return rules; cross-sectional equities, so adjacent, not contradictory.
- Weekends are quieter on average yet held the 10 October 2025 extreme.
- LLM-evolved strategies: Kvasiuk and Huang report gains, Gencay certifies none; the synthesis attributes this to evaluation.
- Lebiedz's abstract says "substantially outperformed" while one seed lost and p is about 0.06.
- Jaddu (C) trained the agent on realised, not predicted, alphas "to avoid training bias", which would hide the failure in concluded item 3.
- Garbled: the Kronos p.1 figure text, the Duflot results table, the M3FT results table.
