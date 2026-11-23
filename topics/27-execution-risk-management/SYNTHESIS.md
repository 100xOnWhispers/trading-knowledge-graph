# Execution, transaction costs and risk management for a directional bot: synthesis

Scope: getting in and out cheaply and surviving. 18 source notes. Liquidity and impact measurement is in topic 09, volatility-based sizing in topic 14, liquidation mechanics in topic 04, venue rules in topic 06, backtest statistics in topic 26. Reinforcement learning, machine learning and evolutionary methods are covered here only where they are applied to execution or risk control.

Access was uneven. Fourteen notes are full-text. Four are abstract-only (Kaminski and Lo, Grossman and Zhou, Frazzini et al., Cui et al.) and say so. Web search was unavailable for this topic's session, so sources were reached by direct address; the gaps are listed at the end.

## What the literature agrees on

1. **For a small account the cost that matters is fees and spread, not impact.** The classical execution models ([Almgren and Chriss](notes/almgren-2000-optimal-execution-portfolio-transactions.md), [Obizhaeva and Wang](notes/obizhaeva-2005-optimal-trading-supply-demand-dynamics.md)) optimise the trade-off between impact and price risk and treat the fixed cost per unit as unavoidable. The one crypto study that decomposes cost ([Schnaubelt](notes/schnaubelt-2020-deep-rl-cryptocurrency-limit-order-placement.md)) finds that for moderately sized orders about ninety percent of shortfall is exchange commission. On Kalshi's entry retail tier the taker fee is 12 bp against a 2 bp maker fee ([topic 06 fee note](../06-kalshi-venue/notes/kalshiex-2026-perpetuals-fee-schedule-amendment.md)); on [Hyperliquid](notes/hyperliquid-2026-perps-fee-schedule-docs.md) it is 4.5 bp against 1.5 bp. Scheduling theory becomes relevant only when order size approaches displayed depth.

2. **A passive order is not a cheap market order.** Live orders on the Binance BTC perpetual fill mostly when the next seconds go against them ([Albers et al.](notes/albers-2025-market-makers-dilemma-fill-probability.md): about -0.8 bp average five-second return, and a naive quoting strategy that lost almost 60% in under four days). Labelled equity data show the same pattern from the other side: every class of participant's limit orders fill when imbalance was against them ([Lehalle and Neuman](notes/lehalle-2017-incorporating-signals-optimal-trading.md)). The maker-or-taker decision is therefore an expected-value comparison with three terms: fee saved, adverse markout if filled, and the value of the trade missed if not filled.

3. **Under proportional costs the right response to a forecast is a band, not a continuous adjustment.** With linear costs and a position cap the optimal policy flips position only when the forecast crosses a threshold and otherwise does nothing ([de Lataillade et al.](notes/delataillade-2012-optimal-trading-linear-costs.md)). The naive rule "trade when expected gain exceeds cost" is correct only for weak or memoryless signals. With quadratic costs the answer is partial adjustment toward a target ([Garleanu and Pedersen](notes/garleanu-2009-dynamic-trading-predictable-returns-costs.md)). Both say: turnover is a decision variable.

4. **Signal persistence is worth as much as signal strength.** Fast-decaying predictors deserve less weight once costs are counted (Garleanu and Pedersen: the net Sharpe gain of about 20% over static rules came from down-weighting the 2.4-day signal). In the band model, a slower predictor justifies acting on a smaller instantaneous forecast.

5. **Execution policies that condition on their own state beat static ones, and most of the gain needs no market prediction.** Time remaining and inventory remaining alone gave 27% to 36% lower cost than an optimised static limit order ([Nevmyvaka et al.](notes/nevmyvaka-2006-reinforcement-learning-optimized-trade-execution.md)); spread and cost-to-cross add more; signal-aware schedules speed up when the signal is adverse (Lehalle and Neuman).

6. **Exit thresholds and leverage should be derived from a model of the return process, not searched on history.** Simulation under a fitted process gives take-profit and stop-loss levels, and shows that near a random walk no optimum exists ([Carr and Lopez de Prado](notes/carr-2014-optimal-trading-rules-without-backtesting.md)). A convex condition on the return distribution caps leverage for a chosen drawdown probability ([Busseti et al.](notes/busseti-2016-risk-constrained-kelly-gambling.md)). Closed forms give the drawdown to expect from a given edge and volatility ([Magdon-Ismail et al.](notes/magdon-ismail-2003-maximum-drawdown-brownian-motion.md)). Sizing in proportion to the surplus over a trailing floor enforces a maximum drawdown mechanically ([Grossman and Zhou](notes/grossman-1993-optimal-investment-controlling-drawdowns.md), abstract only).

7. **Costs must be measured from your own fills.** A large manager's realised costs were an order of magnitude below literature estimates ([Frazzini et al.](notes/frazzini-2018-trading-costs.md), abstract only); Albers et al. show simulated passive fills are unreliable in the other direction. Both argue for a live measurement phase with small real orders.

## Where it disagrees or is weak

- **Is passive execution worth it?** Schnaubelt and Nevmyvaka et al. report large savings from limit orders, but both use simulators that cannot see queue position or adverse selection. Albers et al., with real orders, find passive fills lose on average before the rebate. These are reconcilable (the fee gap can exceed the adverse markout), but no source measures both on the same venue, and none on Kalshi.
- **Do stop-losses help?** The only empirical stop-loss source here was read as an abstract ([Kaminski and Lo](notes/kaminski-2014-stop-loss-rules-stop-losses.md)): some policies raised return and cut volatility for index futures at longer sampling frequencies. The simulation evidence (Carr and Lopez de Prado) says tight stops are the worst choice for a mean-reverting position. Neither covers intraday crypto, where each stop-out pays spread and taker fee and where stops cluster and feed cascades ([Osler, topic 09](../09-liquidity-price-impact/notes/osler-2002-stop-loss-orders-price-cascades.md)). The follow-up by Lo and Remorov on serial correlation and transaction costs could not be opened.
- **Model assumptions against crypto reality.** Almgren-Chriss assumes linear permanent impact and a random walk; Obizhaeva-Wang a deterministic refill; the drawdown formulas a Brownian motion; risk-constrained Kelly i.i.d. returns. Crypto intraday returns have jumps, clustering and liquidation-driven tails ([topic 04](../04-open-interest-liquidations/SYNTHESIS.md)). Treat the closed forms as lower bounds on risk.
- **Learning methods are evaluated on simulators.** Every reinforcement learning and evolutionary result here depends on replayed or artificial markets. [Cui et al.](notes/cui-2011-dynamic-trade-execution-grammatical-evolution.md) (abstract only) use an agent-based market; Schnaubelt uses one-minute snapshots and reports that hyperparameters were untuned. Topic 24 holds the general critiques ([reality gap](../24-reinforcement-learning/notes/noble-2026-bridging-reality-gap-lob-simulation.md), [execution failure modes](../24-reinforcement-learning/notes/ardaiz-2026-mixture-experts-crypto-execution-failure-modes.md)).
- **Fill-probability models optimise the wrong target if used alone.** [Arroyo et al.](notes/arroyo-2023-deep-survival-fill-probabilities-lob.md) predict fill-time distributions well on Nasdaq; Albers et al. argue that fill probability is negatively correlated with post-fill return, so a model must predict both.
- **Latency.** [Moallemi and Saglam](notes/moallemi-2013-cost-of-latency-high-frequency-trading.md) price the staleness of one's own quotes; they do not price being picked off by faster traders. There is no study of latency cost for a non-HFT participant on a crypto venue among the sources opened.
- **Thin areas.** No academic source on exchange and operational risk was opened (see gaps). Evolutionary methods for execution rest on a single abstract. Nothing here is specific to SOL.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| No-trade band on the forecast | Forecast of next-interval return, its AR(1) decay and innovation size, per-unit cost | Decision interval (minutes) | B (theory, simulation) | [de Lataillade](notes/delataillade-2012-optimal-trading-linear-costs.md) |
| Decay-weighted aim and partial adjustment | Several signals with estimated decay rates, cost and risk-aversion parameters | Minutes to hours | B | [Garleanu-Pedersen](notes/garleanu-2009-dynamic-trading-predictable-returns-costs.md) |
| Maker-or-taker expected-value rule | Fee schedule, spread, fill probability, expected markout given fill, value of missed trade | Seconds to minutes | B (live crypto experiment) | [Albers](notes/albers-2025-market-makers-dilemma-fill-probability.md), [Hyperliquid fees](notes/hyperliquid-2026-perps-fee-schedule-docs.md) |
| Fill-time survival model | Book snapshots, imbalance, microprice, volatility, time of day | Seconds to minutes | B (equities) | [Arroyo](notes/arroyo-2023-deep-survival-fill-probabilities-lob.md) |
| Imbalance-conditioned aggression | Touch imbalance on Kalshi and on reference venues, schedule slippage | Seconds | B (descriptive) | [Lehalle-Neuman](notes/lehalle-2017-incorporating-signals-optimal-trading.md) |
| State-conditioned limit placement, tabular RL | Time left, inventory left, spread, cost to cross, signed recent volume | 2 to 8 minutes | B | [Nevmyvaka](notes/nevmyvaka-2006-reinforcement-learning-optimized-trade-execution.md) |
| Deep RL limit placement (PPO) | Above plus queue imbalance; reward includes fees | Minutes | B (crypto spot, simulated fills) | [Schnaubelt](notes/schnaubelt-2020-deep-rl-cryptocurrency-limit-order-placement.md) |
| Evolved execution rules | Grammar over state and actions; shortfall fitness | Minutes | C (abstract only, artificial market) | [Cui](notes/cui-2011-dynamic-trade-execution-grammatical-evolution.md) |
| Schedule with half-life and resilience | Volatility, impact slope, book refill rate, deadline | Minutes to hours, large orders only | B (theory) | [Almgren-Chriss](notes/almgren-2000-optimal-execution-portfolio-transactions.md), [Obizhaeva-Wang](notes/obizhaeva-2005-optimal-trading-supply-demand-dynamics.md) |
| Simulated take-profit and stop-loss mesh | Fitted AR(1) of post-entry path, forecast, maximum holding time | Per trade | C (simulation only) | [Carr-Lopez de Prado](notes/carr-2014-optimal-trading-rules-without-backtesting.md) |
| Loss-triggered exposure cut | Cumulative strategy return, threshold, re-entry rule | Daily in the source | B (abstract only) | [Kaminski-Lo](notes/kaminski-2014-stop-loss-rules-stop-losses.md) |
| Drawdown-probability leverage cap | Empirical per-trade return distribution, tolerated drawdown and probability | Account level | B (theory, simulation) | [Busseti](notes/busseti-2016-risk-constrained-kelly-gambling.md) |
| Surplus-proportional sizing | Equity, running maximum, drawdown limit | Account level | B (abstract only) | [Grossman-Zhou](notes/grossman-1993-optimal-investment-controlling-drawdowns.md) |
| Drawdown monitor and kill switch | Strategy mean and volatility, elapsed time, realised drawdown | Account level | B (theory) | [Magdon-Ismail](notes/magdon-ismail-2003-maximum-drawdown-brownian-motion.md) |
| Latency cost estimate | Per-second volatility, spread, measured latency | Engineering decision | B (theory, equity calibration) | [Moallemi-Saglam](notes/moallemi-2013-cost-of-latency-high-frequency-trading.md) |
| Own-fill cost model | Logged orders with arrival mid, fills, fees, depth, volatility | Continuous | B (abstract only) | [Frazzini](notes/frazzini-2018-trading-costs.md) |

### Trade frequency against cost: an illustrative break-even

This is my arithmetic, not a result from any source. Inputs: Kalshi SOL perp one-minute volatility 8.3 bp and median spread 4.5 bp from a one-day snapshot ([topic 06](../06-kalshi-venue/notes/kalshi-2026-solperp-public-market-data-snapshot.md)); entry-tier retail fees 12 bp taker, 2 bp maker. Assumptions: independent minutes, so volatility over h minutes is 8.3 times the square root of h; a forecast with correlation IC to the h-minute return; expected gross gain per trade of IC times volatility times 0.8 when trading every signal, or times 2.37 when trading only forecasts beyond two standard deviations (about 5% of the time).

| Round trip | Cost (bp) | Break-even h, IC 0.05, every signal | IC 0.10, every signal | IC 0.05, only beyond 2 s.d. |
|---|---|---|---|---|
| Taker in, taker out | 28.5 | about 5 days | about 31 hours | about 14 hours |
| Maker in, taker out | 16.25 | about 40 hours | about 10 hours | about 4.5 hours |
| Maker in, maker out, no adverse selection | 4 | about 2.4 hours | about 36 minutes | about 16 minutes |
| Maker both, 2 bp adverse selection assumed | 6 | about 5.5 hours | about 80 minutes | about 37 minutes |

The table's message is robust to its crude assumptions: at this fee tier, a minutes-horizon directional strategy is viable only if most volume executes passively, or if the bot trades rarely and only on its strongest forecasts. Reaching the fee tier at $1M of 30-day volume halves the taker fee and moves every taker row by roughly a factor of three in h. The maker rows omit the cost of trades missed when the passive order does not fill, which Albers et al. show is concentrated in the trades that would have won.

## Open questions worth testing on SOL perps

1. What is the average markout of a small resting order at the Kalshi SOL touch at 5 seconds, 1 minute and 5 minutes, and what fraction of orders fill? Replicate the Albers et al. continuous-quoting experiment at minimum size. This single measurement decides whether the 10 bp fee gap survives adverse selection.
2. Does imbalance or short-horizon return on Binance, Coinbase or Hyperliquid predict whether a Kalshi passive order will be adversely filled? If so, cancel-on-reference-move is the main execution feature.
3. For the bot's actual forecast, what are the fitted decay `eps` and innovation `beta`, which regime of the band formula applies, and does the theoretical threshold beat a threshold chosen by walk-forward search?
4. How does realised cost of a taker exit vary with size relative to displayed depth and with volatility? Fit the own-fill cost model before trusting any backtest.
5. Do the bot's losing trades predict further losses over the next holding period (which would justify stops), or do they revert? Measure the serial correlation of trade returns conditional on a drawdown, separately for calm periods and liquidation cascades.
6. Does a simulated take-profit and stop-loss mesh, with costs and a jump component added, select exits that outperform time-based exits out of sample?
7. With the bot's empirical trade-return distribution, what leverage does the drawdown-probability condition allow for a 10% chance of a 30% drawdown, and how does it compare with the venue cap of roughly 3x?
8. What is the bot's measured decision-to-acknowledgement latency, and what does the latency formula imply at the 90th percentile of volatility?
9. Does a four-state tabular execution learner trained on recorded Kalshi books beat submit-and-leave with a tuned offset when both are scored with real small orders? Only if yes is a deep policy or an evolved rule worth building.
10. How do funding at 8-hour intervals and the fee-tier ladder change the optimal holding period? A cost model with path-dependent tiers is needed to answer this.
11. What happens to spread, depth and fills on Kalshi during an offshore liquidation cascade? This is both an execution question and an operational-risk one (halts, widened margin, queue behaviour); see [topic 04](../04-open-interest-liquidations/SYNTHESIS.md).

## Reading order

1. [Albers et al. 2025](notes/albers-2025-market-makers-dilemma-fill-probability.md): what passive execution on a crypto perpetual really costs. Also noted in topic 07 from the imbalance angle.
2. [de Lataillade et al. 2012](notes/delataillade-2012-optimal-trading-linear-costs.md): the no-trade band for a capped position under proportional costs.
3. [Garleanu and Pedersen 2009](notes/garleanu-2009-dynamic-trading-predictable-returns-costs.md): why signal decay governs trading under costs.
4. [Hyperliquid fee schedule](notes/hyperliquid-2026-perps-fee-schedule-docs.md), with the Kalshi fee note in topic 06: the numbers behind the break-even table.
5. [Schnaubelt 2020](notes/schnaubelt-2020-deep-rl-cryptocurrency-limit-order-placement.md): fees dominate crypto execution cost; reinforcement learning for limit placement.
6. [Nevmyvaka et al. 2006](notes/nevmyvaka-2006-reinforcement-learning-optimized-trade-execution.md): the minimal state-conditioned execution learner. Also noted in topic 24.
7. [Lehalle and Neuman 2017](notes/lehalle-2017-incorporating-signals-optimal-trading.md): signals inside the execution schedule; who uses imbalance.
8. [Arroyo et al. 2023](notes/arroyo-2023-deep-survival-fill-probabilities-lob.md): fill time as a survival problem.
9. [Almgren and Chriss 2000](notes/almgren-2000-optimal-execution-portfolio-transactions.md), then [Obizhaeva and Wang 2005](notes/obizhaeva-2005-optimal-trading-supply-demand-dynamics.md): the classical scheduling models, for when size grows.
10. [Moallemi and Saglam 2013](notes/moallemi-2013-cost-of-latency-high-frequency-trading.md): how much latency matters for a slow trader.
11. [Carr and Lopez de Prado 2014](notes/carr-2014-optimal-trading-rules-without-backtesting.md), then [Kaminski and Lo 2014](notes/kaminski-2014-stop-loss-rules-stop-losses.md): exits and stops. Pair with [Bailey and Lopez de Prado on stop-outs in topic 26](../26-backtest-overfitting/notes/bailey-2014-stop-outs-serial-correlation-triple-penance.md).
12. [Busseti et al. 2016](notes/busseti-2016-risk-constrained-kelly-gambling.md), [Magdon-Ismail et al. 2003](notes/magdon-ismail-2003-maximum-drawdown-brownian-motion.md), [Grossman and Zhou 1993](notes/grossman-1993-optimal-investment-controlling-drawdowns.md): leverage, expected drawdown and drawdown control. Pair with the [Kelly note in topic 14](../14-volatility-forecasting/notes/maclean-2010-good-bad-properties-kelly-criterion.md).
13. [Frazzini et al. 2018](notes/frazzini-2018-trading-costs.md) and [Cui et al. 2011](notes/cui-2011-dynamic-trade-execution-grammatical-evolution.md): abstract-only context on measuring costs from live fills and on evolved execution rules.

## Sources not covered

Not opened in this session, and therefore without notes: Lo and Remorov on stop-losses with serial correlation and transaction costs; Cartea, Jaimungal and Penalva's textbook; Cartea and Jaimungal on order flow in execution; Maglaras, Moallemi and Wang on fill probabilities; the full text of Kaminski and Lo, Grossman and Zhou, and Frazzini et al.; any study of exchange failure, outage or counterparty risk for crypto venues; any crypto-specific stop-loss study. Two papers were opened but not given notes: Lokin and Yu (arXiv 2403.02572, fill probabilities in a queueing model, foreign exchange data) and Ning, Lin and Jaimungal (arXiv 1812.06600, double deep Q-learning for execution on equities). Hafsi and Vittori (arXiv 2411.06389, reinforcement learning for execution) was confirmed to exist by its abstract page only.
