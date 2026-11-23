Tags are (source, grade, paper|note). "Synthesis" or "pointer" marks a research-agent summary. Albers 2021 has two notes (graded B and C), both cited as albers-2021.

Q1. How far a small venue lags Binance, and whether that pays
- Established: Polymarket BTC 15-minute quotes follow large Binance moves with a median delay near 347 ms, yet a walk-forward model on 43 features did not beat Polymarket's own mid and lost after costs (young-2026, B, note). Pointers: venue lags of 100 to 800 ms; R-squared 10-37% on 500 ms returns with negative taker P&L at default fees; Binance leads Hyperliquid in 29 of 29 assets including SOL (nayyar-2026, C). Kalshi one-day snapshot: one-minute return correlation 0.976, about -0.01 at a one-minute lead or lag; basis to Coinbase +1.8 bp, s.d. 2.1 bp (snapshot, C, via synthesis).
- Weak or missing: Kalshi's sub-minute lag is unmeasured.
- For this system: measure it on recorded timestamps; use for cancel timing only.

Q2. Kalshi funding formula and timing
- Established: a per-second premium of the impact bid/ask over the CF index, back-weighted toward the end of the 8-hour interval, 0.01% deadband, 2% cap (kalshi-2026-nearperp, B, note). Pointers: linear weights put about 44% of the rate in the last two hours; 401 of 517 SOL intervals exactly zero, mean 0.15 bp, largest 8.5 bp; settlement at 04/12/20 UTC in summer, 05/13/21 in winter. Binance uses the same linear weighting (he-2022, B, paper). Nadex's SOL perp on the same index pays 0.01% per 8 hours when quiet (nadex-2026, B, note).
- Weak or missing: the help center describes an equal-weight TWAP of 480 one-minute premiums (C, note).
- For this system: rebuild the premium from recorded book and index; regress settled rates on both weightings.

Q3. How the CF real-time index is built
- Established: resting orders only, never trades. Constituent books are merged, each level capped by a dynamic size cap, uncrossed, turned into price-volume and spread-volume curves; the mid curve is weighted by an exponential density up to a "utilized depth" (cfbenchmarks-2026, B, paper; nadex-2026, B, paper). Stale, crossed or median-deviating books are dropped. Constituents: Coinbase, Kraken, Gemini, LMAX Digital, Bitstamp (kalshiex-2026 filing, B, paper).
- Weak or missing: no parameter values or update interval.
- For this system: a Coinbase-book proxy to nowcast index moves and constituent drop-outs.

Q4. Price bands, leverage, liquidation
- Established (pointers): API leverage 3.59x long, 3.09x short at $1,000 notional; initial margin 1.3 times maintenance (topic 06 synthesis). Help center: variation margin near 12:00 and 16:00 ET, Thursday maintenance 03:00-05:00 ET, and "a position cannot be closed while a resting limit order exists on it" (C, note). Self-clearing members pay 4/2 bp and get a 98% taker rebate through 2026-12-31.
- Weak or missing: liquidation distance unknown; liquidations are market orders (help center) or IOC limits that can fail and bypass the price band (API). Band widths are not given.
- For this system: the replay must model cancel-before-exit; the bot's own leverage cap should bind (busseti-2016, B, note).

Q5. Measured spread, depth, volatility
- Established: one-day snapshot: median spread 4.5 bp, one-minute volatility 8.3 bp; book adequate for $1,000-$20,000 clips, impact price moves above about $100,000; about 248,000 one-minute bars exist (snapshot, C, note). One-minute realised variance is among the best estimators for liquid assets (liu-2015, A, note).
- Weak or missing: one day only; no profile by hour, weekend, maintenance or funding time.
- For this system: replace the snapshot with recorder statistics by hour and event window.

Q6. Do small-venue makers hedge on a larger venue?
- Established: nothing. One note conjectures, untested, that Kalshi makers hedge on venues like Hyperliquid, so depth withdrawal there could propagate (lim-2026-liquidity-recovery, B, note).
- Weak or missing: the whole question.
- For this system: test whether Kalshi touch depth falls seconds after Binance depth withdrawals.

Q7. Fees, rebates and who leads
- Established: across 14 Bitcoin markets a high taker fee with high maker rebate predisposes a venue to lag, low fees to lead; taker strategies paid only where a venue lagged more than its fees implied. Net fee is roughly uniform across venues; Bybit's 2.5 bp rebate was the largest. Taker fee and impact for orders above $100k offset each other (albers-2021, B/C, paper).
- Weak or missing: the Bybit live maker test is announced; its result is not in the passages.
- For this system: Kalshi's fees predict a strong follower with a tight book.

Q8. Follower behaviour in a leader outage or cascade
- Established: nothing above 0.5. After a Hyperliquid cascade the quoted spread recovered while inside depth stayed reduced for weeks (lim-2026-liquidity-recovery, B, paper). Kalshi pauses funding if the CF feed fails (help center, C).
- Weak or missing: no evidence on a follower's quotes.
- For this system: gate on inside depth, not spread; a stale leader or index feed is an unfamiliar state.

Q9. Does the premium to index mean-revert?
- Established: nothing above 0.5. After a spot move above about 5% in an hour the perp overshoots by a few percent of the move, reverting within hours; funding turns against the winning side over one or two windows (gornall-2025, B, note). Kalshi's premium was zero in 68% of seconds, 99th percentile 5.5 bp, maximum 25 bp (snapshot, via synthesis).
- Weak or missing: no reversion speed.
- For this system: estimate the half-life of Kalshi mid minus index.

Q10. Information in prediction-market range prices
- Established: little. An unopened abstract reports a mean gap near 6 percentage points between prediction-market and option-implied binary values for bitcoin thresholds, half-life near four hours (Portnaya, pointer). Polymarket's mid was not beaten by Binance features (young-2026, B). The top passage is off-question (weekend crypto volatility and Monday variance; ebadollahyvahed-2026, B, paper).
- Weak or missing: nothing on Kalshi range contracts.
- For this system: score the band-implied density against the cone.

Q11. What sets fill probability at the best bid
- Established: the two top-of-book queue sizes and queue position describe it; about 50% with balanced queues at a one-tick spread (albers-2025, B, note). 95,998 of 172,800 minimum-size orders filled before the touch moved (albers-2025, B, paper). In equities, orders inside the spread fill fast or not at all (arroyo-2023, B, paper; table garbled). Cancellation probability falls as the queue grows (bouchaud-2008, B, paper).
- Weak or missing: nothing for a thin follower venue; L2 data hides exact position.
- For this system: queue-model inputs are near queue, opposite queue, position.

Q12. Queue position and post-fill return
- Established: a back-of-queue fill is hit by the order that moves the mid against it. One-second markout with favourable imbalance: -0.058 bp front, -0.775 bp back; both queues large: -0.296 and -1.157 bp. The naive maker lost 0.44 bp per round trip net of rebates. About 15% of orders are reversals; posting only above a 24-26% predicted reversal probability gained 0.1-0.2 bp, barely profitable and not scalable (albers-2025, B, note and paper).
- Weak or missing: Binance BTC at one second only.
- For this system: report replay markouts by assumed queue position; the fill model decides passive results (hftbacktest-2026, D, note).

Q13. When to cancel
- Established: an imbalance-based cancel rule "only slightly mitigates" maker losses; it catches slow adverse drift, not sudden moves from large taker orders (albers-2025, B, paper).
- Weak or missing: "cancel when the reference venue moves" is the synthesis's own untested rule; no Kalshi markouts exist.
- For this system: test whether leader moves in the preceding second predict adverse Kalshi fills.

Q14. Cost of latency
- Established: latency cost falls from about 20% of the cost of immediacy at 500 ms to 5% at 5 ms; the limit-price adjustment at 500 ms is about 1.4 * sigma * sqrt(dt); immaterial next to a retail commission (moallemi-2013, B, note and paper).
- Weak or missing: equities, stylised model.
- For this system: my arithmetic: at 8.3 bp per minute this is about 1 bp at 500 ms, small against the 10 bp fee gap.

Q15. Choosing a limit offset
- Established: a note only. A learned policy maps time left, volume left, spread, cost to cross, queue imbalance, recent returns and volume to an offset; the fee term dominates the reward (schnaubelt-2020, B, note).
- Weak or missing: no formula.
- For this system: a fixed offset is the baseline both learners must beat.

Q16. Fee versus spread and impact
- Established: for moderate crypto orders about 90% of shortfall is commission (schnaubelt-2020, B, via synthesis). Adding effective spread at a high fee tier cut a funding-arbitrage Sharpe from 3.35 to 3.27 for BTC (he-2022, B, paper). A taker RL agent on five-minute bars reported 350% total return, execution costing 54 points, funding adding 71 (borrageiro-2022, B, note). Bitcoin metaorder impact is of the order of spread plus fees (donier-2015, A, paper).
- Weak or missing: nothing on Kalshi.
- For this system: funding income will not transfer; Kalshi funding is near zero.

Q17. Book imbalance: predictive, tradable?
- Established: the expected move is linear in imbalance and well below the spread (lipton-2013, B, paper). Live on the Binance BTC perp: about +1 bp per round trip before fees as taker, negative after 1.5 bp per leg; passive orders with the imbalance rarely fill, and the fills are where it was wrong (albers-2025, B, paper). In Nasdaq equities, three to five imbalance regimes made a maker profitable out of sample (cartea-2018, A, paper).
- Weak or missing: raw imbalance misleads after volatility spikes (albers-2021, C, paper).
- For this system: use imbalance for post-or-wait and markout prediction, not direction.

Q18. Costs from own fills
- Established: a large manager's live costs were an order of magnitude below literature estimates (frazzini-2018, B, note, abstract only); simulated passive fills err the other way (albers-2025, via synthesis).
- Weak or missing: no method.
- For this system: a small live quoting phase calibrates the queue model.

Q19. Micro-price versus mid
- Established: the micro-price is the limit of expected future mids given mid, imbalance and spread, a martingale; the abstract says it beats mid and weighted mid (stoikov-2018, B, note from abstract and slides; slide example garbled).
- Weak or missing: no accuracy numbers; duflot-2025 (B, paper) calls the weighted mid "micro-price".
- For this system: a Stoikov micro-price on the Kalshi book as markout reference.

Q20. Survival models for time to fill
- Established: a Transformer encoder with monotonic decoder estimates fill-time survival from recent book history, on equities (arroyo-2023, B, paper).
- Weak or missing: no crypto, no numbers.
- For this system: a plain censored survival fit on simulated touch orders.

Q21. Spoofing and fleeting depth
- Established: nothing above 0.5. A table lists a spoof-robust depth filter using size, distance and age of large orders (fabre-2025, B, pointer).
- For this system: nothing yet.

Q22. Signals inside an execution schedule
- Established: with an Ornstein-Uhlenbeck signal and decaying impact an explicit optimal schedule exists; it speeds up when the signal is adverse and pauses when favourable; fast participants choose order type by imbalance (lehalle-2017, B, paper and note).
- Weak or missing: large parent orders; no crypto.
- For this system: short cone leads set urgency (post or cross), not direction.

Q23. Footprints of scheduled execution
- Established: nothing above 0.5. Hyperliquid native TWAPs are public while active, with lower temporary impact and smooth square-root paths; reconstructed metaorders show U-shaped schedules and larger permanent displacement (barone-2026, B, paper).
- Weak or missing: no detection method.
- For this system: nothing with current data.

Q24. Impact of a taker order
- Established: impact is about Y * sigma_daily * sqrt(Q / V_daily), Y near one (topic 09 synthesis). A single market order's impact grows as sqrt(q) after volume-time q even when immediate impact is zero (maitrier-2025, B, paper). Maker adverse selection equals taker impact, so maker return should fall with fill size (albers-2025, B, paper).
- Weak or missing: SOL and Kalshi coefficients.
- For this system: fit Kalshi's Y before sizing capped crosses.

Q25. Does signed taker flow predict beyond its bar?
- Established: cross-venue flow predicts 500 ms returns, unprofitable for takers at default fees (albers-2021, C, note). Pointers: gross edges of 0.5 bp per quarter-hour boundary and 1.3 bp at best against 5 bp costs. Quarter-hour opening flow is positively autocorrelated across successive quarter-hours; return dependence also sits on the five-minute grid (kim-2026, B, paper).
- Weak or missing: SOL decay time.
- For this system: find the bar length where the lagged-imbalance coefficient reaches zero (chordia-2005, A, note); split returns into flow-explained and residual (evans-2002, A, note).

Q26. Long memory of order signs
- Established: signs have power-law autocorrelation, yet returns stay near-unpredictable because size and liquidity adjust against expected flow (lillo-2004, A, paper). Bar-level tick rules misclassify 38.7% against 11.6% trade by trade (andersen-2013, via synthesis).
- Weak or missing: no crypto estimate.
- For this system: use the surprise in flow, not its level.

Q27. Impact decay
- Established: price is a sum of decaying impacts of past signed trades; kernel exponent beta = (1 - gamma)/2; the response peaks after 100-1,000 trades (bouchaud-2004, A, paper). Post-metaorder decay is about t^(-1/2) (maitrier-2025, barone-2026, B, paper).
- Weak or missing: Maitrier says the propagator alone cannot explain concavity in volume; kvasiuk-2026's formula is garbled.
- For this system: feature: sum of sign * sqrt(size) / sqrt(age) per venue.

Q28. Flow-driven versus flow-opposed moves
- Established: about 70% of 15-minute Binance bars are flow-driven; reversal concentrates after them and grows with imbalance; AUC 0.540 against 0.519; depth consumed and a retail proxy add nothing; gross edge peaks near 1.3 bp (kitron-2026, B, paper and note).
- Weak or missing: imbalance adds no skill beyond the price path.
- For this system: a flow-driven flag gating reversal-side resting orders.

Q29. Trade size and trade count
- Established: variance scales with trade count and, given count, rises with average trade size on perps (pinto-2025, B, note). In E-mini futures average trade size falls as VIX rises (correlation -0.38 to -0.86) (andersen-2014, A, paper).
- Weak or missing: the two disagree in sign; nothing on direction.
- For this system: count and size per trade as cone-width inputs.

Q30. Round sizes and clock boundaries
- Established: the round-size share of trades drops at clock boundaries, from -0.04 s.d. at ordinary minutes to -0.20 s.d. at the top of the hour for BTC, read as algorithmic participation (kim-2026, B, paper).
- Weak or missing: liquidations or institutional flow could do the same, the authors concede.
- For this system: round-size share as a manual-flow proxy; untested.

Q31. Cross-impact
- Established: once the common factor in order-flow imbalance is included, cross-impact terms add little (cont-2023, A, paper). Pointers: lagged cross-asset imbalance helps at one minute, fading by 30; venue-specific flow explains a venue's deviation, which then reverts (Makarov and Schoar); feed latency alone (median 479 ms for Hyperliquid) can fake a lead. Aggressive flow carries more signal than passive (albers-2021, B, paper).
- Weak or missing: untested in crypto at minutes.
- For this system: one common three-venue flow factor plus a Kalshi-specific residual.

Q32. VPIN
- Established: VPIN from true signs is negatively correlated with volatility; bulk-classified VPIN predicts only through errors tied to volume and volatility; nothing remains after controlling for both (andersen-2013, B; andersen-2014, A, paper). The originators claim it signals toxicity-driven volatility (easley-2012, B, paper).
- For this system: nothing; realised volatility and volume suffice.

## Ideas from this block

1. Post only on the absorbing side of flow-pushed moves. Sources: passive fills are mostly the cases where imbalance was wrong, and counter-imbalance entries are the only maker variant near profit (albers-2025); 15-minute reversal concentrates after flow-driven bars (kitron-2026). Inference: a resting order is contrarian by construction, so offer it when the forecast is contrarian too. Data: Binance taker flow, Kalshi book and trades. Kill: simulated Kalshi touch orders; if 1-to-15-minute markouts after flow-driven bars are no better than after flow-opposed bars.

2. Classify Kalshi takers by cross-venue confirmation. Sources: venue-specific flow creates a deviation that reverts (Makarov and Schoar, pointer); uncorrelated flow leaves little permanent impact (donier-2015, pointer); maker markout equals taker impact (albers-2025). Inference: Kalshi prints not confirmed by Binance or Coinbase flow in the preceding seconds are cheap to fill. Data: taker-side trades on three venues. Kill: no markout gap between confirmed and unconfirmed prints.

3. Cancel on leader bursts. Sources: imbalance-based cancelling misses sudden taker-driven moves (albers-2025); flow trickles to laggards within hundreds of milliseconds (albers-2021, young-2026); latency cost (moallemi-2013). Inference: on a follower the sudden move shows first elsewhere. Kill: lead-lag on event timestamps, corrected for feed latency; drop if the lag is below the system's reaction time or adverse fills are not preceded by leader moves.

4. Treat 2026-12-31 as a regime break. Source: the self-clearing 98% taker rebate expires then (pointer); fees shape who lags (albers-2021). Inference: until then some takers pay almost nothing and can pick off slightly stale quotes; afterwards spread, depth and markouts may shift, so earlier tape may mislead the replay learners. Kill: spread, touch depth and simulated markouts four weeks either side show no change.

5. Funding-window pull. Sources: 44% of the rate sits in the final two hours, with a 1 bp deadband; premium zero in 68% of seconds (Q2, Q9). Inference: when the running weighted premium nears the deadband late in an interval, the paying side has reason to press the mid toward the index. Data: recorded book and index. Kill: basis half-life in the last two hours equals that of the first six.

6. Range contracts as a second cone. Sources: a follower prediction market's mid was not beaten by 43 leader features (young-2026); the index is a book blend that drops stale constituents (Q3); Portnaya's four-hour half-life (abstract only). Inference: band prices are a free density forecast of a 60-second index average; a Coinbase-book index proxy matters most in the final minute. Kill: band-implied density does not improve the cone's log score.

7. Count-and-size volatility nowcast in place of toxicity metrics. Sources: pinto-2025, andersen-2014, the VPIN null. Inference: log variance = c + n + beta * q on Binance feeds cone width and the unfamiliar-state gate. Kill: no gain over lagged realised volatility and volume.

## Contradictions and surprises

- Funding average: filing (per-second, back-weighted) versus help center (equal-weight TWAP of 480 minutes) versus API reference. Unresolved.
- Liquidation: market orders (help center) versus IOC limits that can fail (API).
- Index constituents: the methodology note says six USD books and that the filing was not retrieved; the filing lists five.
- Hourly volatility: the fee note's 64 bp assumes independent minutes; the brief says about 71 bp.
- Cartea 2018 (imbalance regimes rescue a maker, equities, grade A) versus Albers 2025 (every imbalance-based variant loses live in crypto).
- Pinto versus Andersen 2014 on trade size and volatility; Easley 2012 versus Andersen on VPIN, whose originators hold a financial interest.
- High volume: follow (daily, cross-sectional) or fade (15-minute); the synthesis says do not carry one rule across horizons.
- Against conclusion 1: resting is necessary, not sufficient. The naive maker lost 0.44 bp per round trip on Binance while receiving rebates; Kalshi charges makers 2 bp.
- Against conclusion 5 (BTC leading SOL): lagged cross-asset imbalance helps at one minute in equities (cont-2023, A); untested in crypto.
- Borrageiro's taker agent was net positive, but 71 of 350 points came from funding.
- Operational surprises: a Kalshi position cannot be closed while a resting order sits on it; Kalshi's funding clock is four to five hours off the offshore clock; the one-minute lag correlation is about zero, so any usable lag is sub-minute.
