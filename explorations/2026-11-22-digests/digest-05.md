Q121. Fitted Q-iteration and tabular value functions for execution
- Established: Tabular RL for execution (10,000 shares, 2 minutes) learns the same shape on three stocks: more inventory and less time left means more aggressive pricing; Q-values are trading costs; the exact policy is stock-specific (nevmyvaka-2006, A, paper).
- Weak or missing: nothing on tree-based fitted Q-iteration, directional trading or crypto.
- For this system: plot fitted Q against time-in-position and inventory; a non-monotone shape signals a bug.

Q122. Multi-agent and mixture-of-experts architectures
- Established: A mixture of K double-DQN experts routed by K-means on episode features (K=4; 2, 4, 8 ablated) routes on the previously processed episode, whose order is not chronological; the authors say the router "cannot" identify the regime (ardaiz-2026, B, paper). LLM multi-agent systems stop at factor mining, without execution or sizing (yun-2025, C, paper).
- Weak or missing: no result table in the passage; the rest is literature review.
- For this system: no regime router; if tried, compare with random routing.

Q123. Are equal weights hard to beat?
- Established: Yes: weight-estimation error dominates when optimal weights are near equal, samples short and conditions unstable (timmermann-2006, A, note; wang-2022, B, paper). With 20 models and 100 observations the strongest shrinkage cut MSE by close to 10%; one study did best keeping the top 20%; equal weights degrade when model quality is heterogeneous (timmermann-2006, A, note). None of 14 optimisers beat 1/N (synthesis citing demiguel-2009, abstract only).
- Weak or missing: forecast-loss evidence, monthly or slower, no costs; Zischke et al. dissent.
- For this system: equal-weight the cone's sub-models and seeds; trim, then shrink.

Q124. Expert advice or bandits for choosing signals
- Established: only a scope statement (synthesis, topic 29). Elsewhere: a Thompson-sampling selector was level with or below equal weights on daily data (synthesis citing zhu-2019); starting values eta about sqrt(log K / T_eff), share rate about 1/T_eff (synthesis citing Hazan).
- Weak or missing: no primary passage; nothing intraday.
- For this system: nothing beyond equal weights as the control.

Q125. Concept drift and retiring a signal
- Established: Pair a stable long-history model with a reactive short-window one and switch when the reactive one is significantly more accurate; ADWIN needs inputs bounded in [0,1] (gama-2014, A, paper). Design choices: memory, detection, learning, loss estimation; blind versus informed adaptation (gama-2014, A, note).
- Weak or missing: no trading evidence; no source measures detection delay for a small edge under heavy-tailed autocorrelated P&L (synthesis).
- For this system: run a stable/reactive pair on post-fill markouts; measure delay on replay.

Q126. Dynamic model averaging for crypto
- Established: Averaging time-varying-parameter regressions gave small, significant gains over AR(1) for Bitcoin and Ethereum at one to two days; averaging beat selection; kitchen-sink regressions were erratic (catania-2018, B, note), up to 12 times worse (synthesis). Daily 2015 to 2017, no equal-weight benchmark, no costs (synthesis). Heavier discounting made forecasts less robust (timmermann-2006, A, note).
- Weak or missing: nothing intraday or on SOL.
- For this system: average, never select; a time-varying tilt must beat equal weights net of costs.

Q127. How fast signals decay
- Established: Six of 11 candidate variables predict post-publication Sharpe decay; publication date is the main one; "every decade the applicable haircut decreases by approximately 50%" (ambiguous wording); factors in large firms decay more (falck-2021, B, paper). LLM news edge decays yearly (lopezlira-2023, B, note).
- Weak or missing: equities, multi-day; no intraday crypto rate.
- For this system: halve any published edge before sizing; record each feature's source sample dates.

Q128. Regime detection and what regimes predict
- Established: A statistical jump model (k-means plus switch penalty) beat buy-and-hold and an HMM on Sharpe and drawdown on three equity indices, 1990 to 2023, one-day delay, 10 bp costs, with far less turnover (shu-2024, B, note). Regimes separate volatilities, not means (synthesis citing ang-2011). A four-state covariate-driven HMM gave the best density forecasts for BTC, ETH, XRP, but states alternate frequently (koki-2020, C, paper and note). A changepoint feature's gain vanished above about 2 bp cost (synthesis citing wood-2022).
- Weak or missing: never shown to beat a realised-volatility threshold (synthesis).
- For this system: risk gate only; benchmark against that threshold.

Q129. Gating by liquidity stress or unfamiliarity
- Established: synthesis only: spread-and-depth circuit breaker, novelty gate, drawdown and time-under-water limits, drift detectors that halve or zero a weight, all outside the learned parts. FineFT's conservative policy was chosen in most test periods, more often further from training; removing the risk threshold lowered performance (qin-2025-fineft, C, note).
- Weak or missing: no thresholds; no cost in missed trades.
- For this system: track the gate-closed share by week since training.

Q130. Blending signals with different decay under costs
- Established: With quadratic costs, trade a fixed fraction toward an aim in which each signal is scaled by 1/(1 + phi_k a/gamma), phi_k its decay rate; persistence matters as much as strength (garleanu-2009, B, paper p.13 and note).
- Weak or missing: the repository's only source; daily, quadratic costs, whereas Kalshi's are linear.
- For this system: discount the cone's five-minute leads by measured decay before the policy sees them.

Q131. Deflated Sharpe ratio and trial counts
- Established: Expected maximum Sharpe of N null trials: SR0 = sqrt(V)[(1-g)Z^-1(1-1/N) + g Z^-1(1-1/(Ne))], g = 0.5772; DSR is the probabilistic Sharpe at SR0 (bailey-2014-deflated, A, note and paper). A 50% haircut is the rule of thumb (harvey-2015, A, paper). N and V should come from a complete trial ledger (gencay-2026, B, paper). Pointers: 102 trials gave design Sharpe 1.69, threshold 1.21, DSR 0.86, held-out 0.18; a planted oracle scored DSR 1.00 (synthesis).
- Weak or missing: correlated trials handled only by an average-correlation shortcut.
- For this system: every genetic individual and random draw is a ledger row.

Q132. Probability of backtest overfitting, combinatorial CV
- Established: PBO is the probability the in-sample best ranks below the out-of-sample median, from performance series alone (bailey-2015, A, note). Deep-RL crypto: PBO 17.5% walk-forward PPO, 7.9% k-fold, 8.0% combinatorial, 9.6% TD3, 21.3% SAC; test returns -34.96% combinatorial PPO, -47.78% equal weight, -59.08% TD3 (gort-2022, C, note). Seven trials suffice for a spurious two-year Sharpe above 1 (harvey-2015, A, paper).
- Weak or missing: one test window; CPCV superiority unverified (skfolio-2026, D, note).
- For this system: use eight-hour blocks as CSCV groups over the genetic population.

Q133. Reality check for the best of many rules
- Established: White's test gives a search-wide p-value allowing dependence (white-2000, A, note). The best of 7,846 Dow rules survives 1897 to 1986; nothing works in the next ten years or in S&P futures; p 0.04 became 0.90 (sullivan-1999, A, note). With one-day delay the best mean return fell from 17.2% to 7.8%; best Sharpe 0.34 had p 0.26 (sullivan-1999, A, paper). SPA, stepM and false-discovery variants exist; the tests are called conservative (bakker-2017, B, paper).
- Weak or missing: Bakker's Bitcoin results absent.
- For this system: bootstrap the whole evaluated population against random search.

Q134. Walk-forward window design
- Established: Train and test lengths are influential hyperparameters. EMA rule on Bitcoin at 1 to 60 minutes, 81 window combinations (1 to 28 days), 19-month design period, two best settings run once on 21 months, 0.1% cost: fast bars mostly unprofitable; 60-minute mean Sharpe positive, no negative combination (mroziewicz-2026, C/B, paper). Selection used a neighbourhood-smoothed Sharpe (note).
- Weak or missing: table values absent; 15 minutes described both ways.
- For this system: choose refit cadence by a plateau; open the final period once.

Q135. Track record needed to trust a Sharpe
- Established: Observed annual Sharpe 2 needs 2.73 years of daily returns to exceed 1 at 95% (3.24 monthly; 4.99 with skew -0.72, kurtosis 5.78) (bailey-2012, A, note). True Sharpe 0.6 needs about eleven years for t near 2; a high-frequency operation gains power in months (gencay-2026, B, paper). Pointers: MinBTL < 2 ln(N)/SR^2 years; Kalshi SOL history starts June 2026 (synthesis).
- Weak or missing: "two configurations need 1.4 years" is the synthesis author's arithmetic.
- For this system: Kalshi tape confirms and calibrates costs; it cannot discover.

Q136. Look-ahead leakage in crypto backtests
- Established: Enforce strict t+1 execution and carry-forward funding using only values visible at each timestamp (deng-2025, C, paper). Usual inflators: bar-close fills, no spread, no self-impact, no competition for fills; leakage also occurs inside training procedures (synthesis, topic 24). LLM backtests leak through training data (glasserman-2023, B, paper).
- Weak or missing: no leak-size estimate for a 15-second system.
- For this system: plant an oracle feature and confirm the pipeline flags it; deflation will not.

Q137. Baselines and null strategies
- Established: Execution RL was compared with optimised submit-and-leave, in bp over the opening mid, on a six-month test set (nevmyvaka-2006, A, paper). FinRL: buy-and-hold, mean-variance, min-variance, momentum, equal weight (liu-2020, C, paper). FineFT: 12 baselines, 0.02% cost, 5x leverage (qin-2025, B, paper). Best-of-K null ceiling: PnL0 + sigma0 sqrt(2 ln K), K = 335 (kvasiuk-2026, C, paper).
- Weak or missing: Kvasiuk's z-scores (103.2, 44.9; baseline Sharpe 4.81) are implausible.
- For this system: add submit-and-leave, a fixed band rule and the best-of-K ceiling.

Q138. Mid fills and missing queue models
- Established: one passage, which concedes the point: fills sampled from an exponential distance-to-mid intensity on one-minute Hyperliquid mids are "not a queue-position or latency-aware execution model", so results only compare policies under a common proxy (le-2026, C, paper).
- Weak or missing: no number for the inflation; the queue-model source is grade D (synthesis).
- For this system: report replay results under optimistic and trade-through-only fills; the gap is the uncertainty.

Q139. Volatility targeting
- Established: Volatility-managed portfolios raise factor Sharpe because volatility does not forecast returns; utility gains about 65% (moreira-2017, A, paper). Scaling does not meaningfully improve bond Sharpe; estimates use t-2 data, half-lives 10 to 90 days (harvey-2018, A, paper and note). In Bitcoin trend following (90-day volatility, 200% cap) scaling cut exposure in the strongest trends (zarattini-2025, B, paper).
- Weak or missing: daily or slower; no intraday crypto test.
- For this system: size by target risk over forecast holding-period volatility; test against fixed size.

Q140. Kelly sizing under error and liquidation constraint
- Established: synthesis only: notional = equity x sigma_target / sigma_hat, capped at venue leverage; tail cap from the worst adverse move per holding-period block of 5-minute returns, per side (citing cheng-2021); drawdown-constrained Kelly: largest L with E[(1+L r)^(-lambda)] <= 1, lambda = log(beta)/log(alpha) (citing busseti-2016).
- Weak or missing: no primary passage; no numbers.
- For this system: compute the per-side tail cap from the recorded index at 60-minute blocks.

Q141. Do stop-losses add value?
- Established: A stop's value is a property of the return process; some policies raised return and lowered volatility for index futures at longer sampling frequencies (kaminski-2014, B, note, abstract only). A stop tuned over 8,800 combinations on a random walk gave Sharpe 1.27 (bailey-2015, A, paper).
- Weak or missing: nothing intraday or crypto.
- For this system: treat an evolved stop as noise unless within-trade P&L shows momentum; test that first.

Q142. Holding period and exit with decaying signal, proportional costs
- Established: The optimal rule is hysteresis: hold maximum long or short and flip only when the predictor crosses q*; q* = Gamma*eps (weak signal), (1.5*Gamma*beta^2)^(1/3) (intermediate), Gamma (strong); always q* <= Gamma (delataillade-2012, B, note and paper p.13; formulas via synthesis).
- Weak or missing: one autocorrelated predictor, immediate fills; no resting-order version.
- For this system: fit eps and beta to the cone's mean forecast; use q* as the fixed-rule baseline.

Q143. Drawdown control
- Established: Expected maximum drawdown of a drifting Brownian P&L grows logarithmically if profitable, as square root at zero edge, linearly if losing (magdon-ismail-2003, B, note and paper). Proportional drawdown rules trade more in fast markets and pay spread (grossman-1993, B, note, abstract only).
- Weak or missing: an hour-of-day Bitcoin note (quantpedia-2023, C) is off-topic and cost-free.
- For this system: halt at the drawdown expected from zero edge over elapsed live time.

Q144. Profit-taking and stop thresholds for mean reversion
- Established: Derive thresholds by simulating a fitted Ornstein-Uhlenbeck process; as half-life lengthens the optimum becomes small profit-taking with wide stops and Sharpe falls (about 9, 2.7, 0.8, 0.32; half-life values garbled); near a random walk no optimum exists (carr-2014, C, paper and note). A pairs study chose entry 3.0 by a plateau and scanned stops 1.25 to 3.25 (lebiedz-2026, B, paper).
- Weak or missing: simulation only.
- For this system: estimate half-life after entries; if near random walk, remove threshold genes.

Q145. Adding to winners versus fixed size
- Established: nothing; the only passage (score 0.06) concerns exchange auto-deleveraging (chitra-2025, B, paper).
- Weak or missing: the whole question.
- For this system: "add once" has no support here; ablate it in replay.

Q146. Stablecoin mints and exchange inflows
- Established (synthesis pointers): Bitcoin's response to a Tether mint peaks at 30 minutes, fades by 60; mints not burns; 1 billion USDT moves Bitcoin 0.68% at peak (saggu-2022). USDT exchange inflows predict BTC and ETH returns at 1 and 2 hours only (chi-2024, C, paper). No daily effect (lyons-2020, B, note); supply follows prices (aldasoro-2024, B, note).
- Weak or missing: data end 2019 to 2023; untested on SOL.
- For this system: not recorded; an event flag at most.

Q147. Large on-chain transfers
- Established: Non-exchange transfers: -0.0267% at minute 2; cold-wallet deposits +0.0404% in the event minute, -0.3444% over 31 minutes (ante-2020, B, paper). Effects do not grow with size; hot-wallet deposits were followed by rises (note). ETH inflows predict lower ETH returns at 1 to 6 hours; BTC inflows mostly nothing (chi-2024, C, note).
- Weak or missing: nothing on SOL.
- For this system: nothing; effects are below maker costs.

Q148. Solana congestion, fees, failures
- Established: Failed transactions are prevalent because of bot spam (zheng-2025, B, paper); over half of raw transactions fail; there is a 24-hour cycle (note). Tips, priority fees and failure rate are grade D, never tested against price (synthesis). Halt flag: no confirmed slot for 30 to 60 seconds across providers (helius-2025, C, note).
- Weak or missing: no link to returns or volatility.
- For this system: low priority; the index uses centralised exchanges.

Q149. Social attention and sentiment
- Established: Tweet volume drives next-day realised volatility and volume, not returns (shen-2019, B, paper). Hourly: no Bitcoin predictability either way; intraday, returns are the strongest predictor (kraaijeveld-2020, C, note).
- Weak or missing: scattered altcoin lags look like multiple testing; no SOL.
- For this system: nothing for direction.

Q150. Options skew, buying pressure, dealer gamma
- Established (synthesis): the popular gamma formula assumes dealers long calls and short puts, unsupported in Deribit flow; cash-settled European options show repulsion from the strike; no source quantifies dealer gamma's effect on spot or perps. Net buying pressure is delta-weighted signed volume split into directional and volatility demand (alexander-2023, B, note).
- Weak or missing: Alexander's results absent.
- For this system: nothing.

Q151. ETF flows
- Established: Launch inflows coincided with a 67% rise by March 2024 (guliyev-2025, C, paper); levels regressions contain price in the regressor; flows follow price (synthesis citing oefele-2025, abstract).
- Weak or missing: SOL ETFs only since October 2025; daily data.
- For this system: nothing.

Q152. Language-model-scored headlines
- Established: GPT-4 headline scores predict stock returns for two days: 34 and 19 bp (overnight news), 32 and 30 bp entering 15 minutes after intraday news (lopezlira-2023, B, paper); the edge vanishes at 20 bp round trip and decays yearly (note). Backtests carry look-ahead and "distraction" bias (glasserman-2023, B, paper).
- Weak or missing: equities, daily.
- For this system: nothing at these fees.

Q153. Macro state variables and intraday crypto
- Established: no source tests a risk-state measure as an intraday crypto conditioner (synthesis). Macro levels add little to Bitcoin volatility forecasts; announcement timing is the useful input (dudek-2025, B, note). 5.6% of macro exercises survive out of sample against 32.2% of technical (synthesis citing sanhueza-2026).
- Weak or missing: no equity-futures-to-crypto lead-lag at seconds to minutes.
- For this system: an announcement calendar as a volatility and gate input.

Q154. Bitcoin's equity beta by regime and time of day
- Established: Bitcoin's beta to US equities on 30-minute US-hours returns was near zero before 2020 and persistently positive after a break around late 2020; the Dow matters more than the NASDAQ; data to March 2026 (drexler-2026, B, paper and note). Weekly coin-equity correlation 1% before 2020, 39% after (synthesis citing borri-2026).
- Weak or missing: contemporaneous, not a lead; no within-day profile.
- For this system: tag US cash hours; test whether post-fill markouts differ.

## Ideas from this block

1. Decay-weighted aim plus hysteresis band as the fixed-rule opponent. Sources: aim scaling (garleanu-2009); band q* <= Gamma (delataillade-2012). Inference: collapse the twelve leads into one aim with fast leads discounted, removing the shortest-horizon dependence of concluded item 3. Data: cone archive, Kalshi book. Kill: on replay it does no better than a threshold on the five-minute lead.

2. Range-contract quotes as one more forecaster, equal-weighted with the cone. Sources: equal weights and diversity (timmermann-2006, wang-2022); the Kalshi-implied-probability idea is grade D, no evidence (synthesis). Inference: the 300 bands give a market density for the top-of-hour average. Data: range quotes, cone, index. Kill: a 50/50 blend does not improve log score at leads ending on the hour.

3. One evaluation entry point with a ledger, eight-hour blocks as CSCV groups, and a best-of-K ceiling. Sources: gencay-2026, bailey-2014-deflated, bailey-2015, kvasiuk-2026, sullivan-1999. Inference: the random-search control supplies N and V; the fitness blocks double as folds. Data: replay results. Kill: PBO above one half, or the genetic winner under the ceiling.

4. Simulate exits before evolving them. Sources: carr-2014, bailey-2015, kaminski-2014. Inference: fit a half-life to price after resting fills and after quarter-hour imbalance bursts; if near a random walk, delete stop and target genes, shrinking the 20 to 30 parameters. Data: Kalshi and Binance tapes. Kill: half-life indistinguishable from infinite.

5. Markout drift monitor with a zero-edge drawdown halt. Sources: gama-2014, magdon-ismail-2003, bailey-2012. Inference: monitor post-fill markout, the system's open measurement, not P&L. Data: own fills, replay. Kill: with the edge switched off in replay, the detector fires later than the drawdown halt.

6. Volatility-scaled resting size with per-side tail cap. Sources: moreira-2017, harvey-2018, cheng-2021 (synthesis). Inference: cone dispersion is the volatility forecast. Data: cone, index. Kill: no reduction in the eight-hour tail penalty against fixed size.

7. US-hours state for adverse selection, not direction. Source: drexler-2026. Inference: equity-driven variance may worsen resting-order markouts on a US venue. Data: Kalshi fills by session (equity futures are not recorded). Kill: markouts equal across sessions.

## Contradictions and surprises

- Majority vote fits the combination literature, but equal weights degrade when model quality is heterogeneous and one study did best keeping the top 20% (Timmermann): trim before voting.
- A regime router built without look-ahead carried no information (Ardaiz); the unfamiliar-state gate rests on one grade C source.
- Gort's overfitting screen accepted an agent that lost 59.08%, and the rejected walk-forward agent beat the accepted k-fold one.
- Synthesis: only calendar time buys Sharpe confidence. Gencay: high-frequency operations gain power in months. Reconcilable only at a high true Sharpe.
- PBO is defined against the median in the note, the mean in the paper's p.28.
- Volatility targeting: large gains (Moreira), none for bonds (Harvey), costly in trends (Zarattini).
- HMM strategies profitable (Bulla) or trailing buy-and-hold in two of three markets (Shu); Koki's best-forecasting states are not persistent.
- Stablecoins: Griffin yes conditionally, Lyons no daily effect, Saggu under an hour, Aldasoro supply follows price.
- Exchange deposits preceded rises (Ante), against folklore; ETH inflows are bearish (Chi).
- A changepoint gain vanished above 2 bp and the LLM news edge at 20 bp, both under this venue's taker round trip.
- Consistent with concluded item 5: no measured lead from BTC or equities to a liquid coin at one minute or longer; open-interest data fail consistency checks at one minute (synthesis).
- Do not quote Falck's "haircut decreases 50% per decade" or Kvasiuk's z-scores without the source.
- Reader's note: "synthesis" marks a research-agent summary whose numbers are pointers. Passages printed only as "(text under Qn)" for questions outside this pack (Q10, Q22, Q29, Q35, Q40, Q45, Q56, Q63) were not in the file.
