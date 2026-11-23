# Assessment: 154 questions against the corpus

Written 2026-11-22. Questions are in `2026-11-22-questions.md`. Each was run through `tools/kb.py ask` (ten best passages, relevance floor 0.5), giving 748 passages. Five readers each digested one fifth of the pack; their digests are in `2026-11-22-digests/`. This file is the reading across all five.

How to read it:

- A source slug in brackets is a note or PDF in this repository. "Inference" marks a step that is this document's own and appears in no source.
- No source tests anything on SOL on Kalshi. Most numbers are gross of costs and from other assets.
- The system assumed: SOL perpetual on Kalshi, 12 bp taker and 2 bp maker, a 15-second forecast of 64 price paths to 60 minutes, and a stateful policy learned by genetic search or fitted Q-iteration on a replay of the recorded Kalshi, Binance and Coinbase tapes.

## The one reframing

At these fees the system is a selective maker. A maker's fills are not a random sample of moments: a resting bid fills when someone sells into it. So the quantity to predict is the price path **given that the order filled**, not the unconditional path the forecast now produces. Almost every recommendation below is a way to predict, score or exploit that conditional quantity.

The evidence for the reframing: live resting orders on the Binance BTC perp filled mostly when the next second went against them, a naive maker lost 0.44 bp per round trip even with rebates, and the only variant near profit posted against the book imbalance [albers-2025]. Resting is necessary at these fees and is not sufficient.

## Recommended algorithms, logic and signals

### A. The maker core

**A1. Predict the post-fill path at several horizons.** Every Kalshi print is a fill of someone's resting order. Label each print with the passive side's return at 10 seconds, 1, 5, 30 and 60 minutes, and fit a model of that curve from the state just before the print. This is the multi-horizon prediction the policy should consume. Sources: per-trade toxicity labels [cartea-2023]; a second model that decides whether to take a trade [singh-2019]; markout by queue position [albers-2025]. Inference: using it as the main prediction target, and emulating queue position by the share of the level the print consumed. Kill: out-of-sample ranking no better than chance (AUC at or below 0.52), or the selected fills no better than all fills.

**A2. Score the forecast on touch-conditional outcomes, then plan on it.** The 64 paths carry highs and lows per five-minute step, so for any resting price the paths that touch it are the forecast's own statement of what happens after a fill. Two uses. First, a new score: among real futures that touched a level, compare where price went with where the touching paths said it would go. A forecast can be well calibrated overall and wrong after a touch. Second, a third contender beside the two learners: at each decision, value every allowed action on the 64 paths with fees and fills applied, and take the best (planning on the forecast). Sources: a forecast plus a one-step cost rule is argued sufficient for a price taker [ma-2025]; the no-trade band [delataillade-2012]; hindsight action values as a teacher [qin-2023]. Inference: the touch-conditional score, planning on the paths, and valuing "hold or exit" by regression across paths as early exercise of an option is valued. Limits: 64 paths at five-minute steps is coarse, and using the same paths to fit and to value overstates. Kill: touch-conditional calibration no worse than overall calibration and the planner no better than a threshold on the five-minute lead.

**A3. Post by the clock.** The first 10 seconds of each quarter-hour on Binance perps carry about 26% more trades and 32% more dollar volume, the share of round-sized trades falls (an algorithm signature), and the imbalance of that burst reverses over the next half hour [kim-2026]. Flow that arrives on a schedule and then reverses is the flow a maker wants. Reversal at 15 minutes also concentrates after bars that taker flow pushed [kitron-2026]. Funding hours look different: volume up over 50% while spreads widen 3.2% [ruan-2024]. Inference: bucket Kalshi post-fill returns by seconds since the boundary, by funding hour (05, 13 and 21 UTC on Kalshi in winter; 00, 08 and 16 offshore) and by weekday. Also test whether the sign of a slot's burst repeats at the same slot on later days, as scheduled flow does in equities [heston-2010]; if it does, the side to post is known in advance. Kill: no spread in post-fill returns between buckets; autocorrelation at a one-day lag no larger than at neighbouring lags.

**A4. Know who is hitting you.** On Hyperliquid, manual front-end traders lost USD 1.11 billion and market makers gained USD 208 million; manual traders open with the recent move, in large orders that ignore displayed depth, and are right briefly before the move decays [jia-2026]. Isolated one-venue order flow leaves little lasting impact while flow that the whole market shares keeps it [donier-2015]. Perpetuals overshoot spot in fast moves and spot leads in cascades [shen-2026, gornall-2025]. Inference, four state variables for the post-fill model: (1) whether Binance and Coinbase flow in the preceding seconds agrees with the Kalshi taker; (2) whether the taker trades with the last 5 to 15 minutes' return; (3) the share of round-sized prints on Kalshi as a manual-flow proxy; (4) how much further the Binance perp has moved than Coinbase spot, since Kalshi's index is US spot and takers copying Binance may hit quotes at prices the index will not confirm. Kill: no gap in post-fill returns across any of the four.

**A5. Anchor fair value to the index, link by link.** The index is built only from resting orders on Coinbase, Kraken, Gemini, LMAX and Bitstamp, depth-weighted near the mid, with stale books dropped [cfbenchmarks-2026, kalshiex-2026 filing]. Measure each link of Binance perp, Coinbase spot, index, Kalshi mid with the tick-level lead/lag ratio and its surrogate test, by hour [huth-2014]; response speed elsewhere rises with trade count, so Kalshi's lag should lengthen in thin hours [kurihara-2026]. Use the result for cancel timing: an imbalance-based cancel rule missed sudden taker-driven moves [albers-2025], and on a follower those show first on the leader. Latency of half a second costs about 1 bp here, small against the 10 bp fee gap [moallemi-2013, arithmetic in digest 1]. Kill: lag below reaction time, or adverse fills not preceded by leader moves.

### B. The forecast

**B1. Read the hourly range contracts as implied volatility.** Inference throughout; the corpus has no test (question 54 returned nothing, and the idea is graded D in the backlog). The bands give a market distribution for a 60-second index average at each hour. Its width is an implied volatility for SOL at one hour, and the events for the next two hours give a forward variance for hour two. Implied variance usually sits above realised [almeida-2024 via synthesis], so calibrate before use. The settlement window also sits on the largest clock burst of the hour [hansen-2021, hansen-2024], so check the forecast's calibration and the perp's path around :00 against :15, :30 and :45. Kill: implied width adds nothing to forecast width out of sample; no difference at :00.

**B2. Width from the clock and the lead venue.** For bitcoin, deterministic periodicity improved out-of-sample fit more than realised variance did [hansen-2024]. The Binance USDT perp transmits volatility to other venues and volume leads volatility by one five-minute interval, with lag-two volume reversing [alexander-2021]. Variance scales with trade count and average trade size [pinto-2025, contemporaneous only]. Raw volume beats VPIN [andersen-2014]. Macro releases: the price jump is done in five minutes and volatility takes about an hour [andersen-2002]. Build: minute-of-hour, hour-of-week and release-calendar factor, times a three-scale model of log realised variance on Binance SOL, plus lagged volume, trade count and trade size, with Coinbase trade count as the clean activity measure [cong-2023]. Kill: no gain over an exponentially weighted average times the same clock factor.

**B3. Give the policy a short summary of the twelve leads.** A three-parameter constrained model beat free lag weights in 15 of 15 cells including SOL, and free weights flipped sign in 30% of folds [kitron-2026]. Signals should be weighted down by their decay rate [garleanu-2009]. The one study of forecast-then-agent found the agent leaning on the shortest horizon [jaddu-2023]. Build: a two or three parameter kernel over the leads, discounted by measured decay. Kill: an agent given twelve free leads does as well and does not concentrate on the five-minute lead.

### C. Learning and validation logic

**C1. Bracket every learner.** Floor: a lottery policy matched on trade count and time in market, and equal-budget random search [chen-2007]. Ceiling: the hindsight-optimal value on the same replay [qin-2023]. Report each learner as a fraction of that distance. Caution (inference): hindsight values assume foresight, so use them as a ceiling and an auxiliary target, never as the regression target alone.

**C2. Archive by behaviour, vote, and switch slowly.** Populations collapse onto one idea [chen-2025, gencay-2026]; generation 20 beat generation 100 out of sample [yun-2025]; the best rule in selection was among the worst afterwards while a vote of 100 held [neely-1997]; switching only on a supermajority of recent fits roughly doubled net return [martin-2019]. Build: keep policies in cells by trades per block, maker share and holding time; fingerprint each by its actions on fixed probe slices [cui-2021]; vote across distinct fingerprints; train at a fee above the live fee. Trim the worst before voting, since equal weights degrade when quality is uneven [timmermann-2006].

**C3. One logged evaluation entry point.** Every replay evaluation is a ledger row, which supplies the trial count and variance for deflating the result [bailey-2014, gencay-2026]. The eight-hour fitness blocks double as folds for the overfitting probability [bailey-2015]. Plant a feature that sees the future and confirm the pipeline catches it; statistics will not [gencay-2026]. Forecasts every 15 seconds with 60-minute labels overlap 240-fold, so purge an hour plus the longest look-back between blocks.

**C4. Earn each exit parameter.** Stop and target thresholds have an optimum only when price mean-reverts after entry; near a random walk none exists [carr-2014], and a stop tuned on a random walk produced a Sharpe of 1.27 [bailey-2015]. Estimate the half-life of price after fills first; if it is indistinguishable from infinite, delete those genes. "Add once" has no support in the corpus (question 145 returned nothing): ablate it.

**C5. Risk logic outside the learners.** Long and short tails differ: eight-hour margins for bitcoin perps were 46.98% long against 26.34% short at the 0.001 level [cheng-2021], so penalise them separately. Halt at the drawdown a zero-edge strategy would show over the elapsed time [magdon-ismail-2003]. Monitor post-fill returns for drift with a stable and a reactive estimator [gama-2014]. Gate on inside depth, not spread, since spread recovered while depth stayed down after a cascade [lim-2026].

## Operational facts that change the build

- **31 December 2026.** The fee note says self-clearing members get 98% of taker fees rebated until then. It cites a companion CFTC filing (`rules10182634493.pdf`) that is not downloaded here, and the fee filing that is downloaded does not mention a rebate, so check that filing before relying on the date. Fees shape which venue lags and who profits from it [albers-2021]. Inference: if the rebate ends, tape before and after may differ in spread, depth and post-fill returns; treat it as a regime break and re-validate in January.
- A Kalshi position cannot be closed while a resting order sits on it (help center, grade C). The replay must cancel before exiting.
- Three Kalshi documents describe the funding average differently. Rebuild the premium from the recorded book and index and regress settled rates on both weightings.
- Data gaps: no USDT to dollar series (every Binance-to-index gap contains the peg); only one of five index constituents; no open interest (and the corpus gives no reason to add it).

## Where this reading corrects the earlier summary

- "Reverses over 30 minutes and continues over 4 to 12 hours" is one paper's flow measure. A second paper has price reversal fading to zero by four hours, on about 103 observations [kitron-2026].
- For SOL the lagged boundary returns were the stronger predictor block, though the target was the 10-second opening return, not a holding return [kim-2026].
- A regime router built without look-ahead carried no information [ardaiz-2026], and the unfamiliar-state gate rests on one source [qin-2025].
- Boosted trees scored worse than the base rate at one hour in the one study that includes SOL [kitron-2026]. This bears on tree-based fitted Q-iteration: include a constrained low-parameter learner.
- First half-hour predicting the last half-hour is grade A on bitcoin with a 7 to 10 bp break-even [shen-2022], above a maker round trip. Clock rules are not all dead; this one is untested on SOL.

## What the corpus could not answer

Nine questions returned nothing relevant: a follower venue during a leader outage; mean reversion speed of the premium; spoofing filters; footprints of scheduled execution; absorbing resting orders as a direction signal; mean reversion of SOL's residual against BTC and ETH; the Coinbase premium; the tether rate across venues; adding to winners. Three more returned only open questions: forecasting range or touch probability, settlement and fixing windows in crypto, and combining density forecasts. Several of these are exactly what the recorded tapes can measure first.

## Order of work

1. One offline study on the recorded tape produces A1, A3, A4 and the half-life for C4: post-fill returns of every Kalshi print, with the state before it.
2. Touch-conditional scoring of the archived forecasts (A2), which needs no new data.
3. Link-by-link lag (A5) and the width model (B2).
4. Range contracts as implied volatility (B1) once the poller has run for some weeks.
5. C1 to C3 before any learner is compared.
