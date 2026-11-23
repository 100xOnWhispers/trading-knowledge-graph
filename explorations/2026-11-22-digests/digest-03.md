Tags are (slug, grade, paper|note). "syn" marks a figure that reaches this pack only through a research-agent synthesis: a pointer. Ten passages were listed as "(text under Qn)" with no text printed here.

Q61. Does volume or trade count forecast volatility better than past volatility?
- Established: In a bivariate LogMEM(2,1) on diurnally adjusted five-minute volume and realised volatility for six bitcoin instruments, lag-1 volume raises volatility and lag-2 volume lowers it; volume is the more persistent (alexander-2021, B, paper). One-day lagged volume forecast volatility with about four times the explanatory power of TR-VPIN, which added nothing once activity was controlled (andersen-2014, A, paper). Volume and lagged realised variance dominate a 69-predictor LightGBM for next-day bitcoin variance (dudek-2025, B, note).
- Weak or missing: No head-to-head of volume, trade count and lagged volatility at minutes; trade count is never separated from volume.
- For this system: Add lag-1 and lag-2 five-minute volume and trade count to the cone's width model; test the lag-2 sign flip.

Q62. Volatility around scheduled macro announcements: how early, how long?
- Established: In FX the mean jump is essentially complete in the first five-minute bar and volatility adjusts over about an hour; bad news moves prices more (andersen-2002, A, note). Pointers: excess variance lasts ten hours or more after FOMC (boehm-2025, syn); volatility at least doubles for DeFi tokens at the FOMC statement and again at the press conference, more for altcoins than bitcoin (kyriazis-2023, syn).
- Weak or missing: "Crypto volatility rises before the release" rests on an abstract; estimator and windows unseen (benomrane-2025, B, note). No SOL number.
- For this system: A calendar flag that widens the cone from about 30 minutes before to 90 minutes after CPI, payrolls and FOMC; estimate the SOL multiplier on the recorded tape.

Q63. Tail risk and liquidation probability over a holding period
- Established: Block-extreme margins for BitMEX bitcoin perpetuals at an eight-hour hold: 7.26% short and 8.36% long at call probability 0.1; 26.34% short and 46.98% long at 0.001; 34.81% two-sided. Normality understates margins by at least half; the left tail is heavier. Daily forced liquidations averaged 3.51% of open interest for longs, 1.89% for shorts (cheng-2021, B, paper and note).
- Weak or missing: Bitcoin on BitMEX only; nothing for SOL or for 5 to 60 minute holds. "Kalshi cap near 3x" is a synthesis pointer.
- For this system: Fit maxima and minima of SOL five-minute returns per eight-hour block and use them for the fitness tail penalty, separately for longs and shorts.

Q64. Rough volatility and long memory in crypto volatility
- Established: Fractional-integration estimates for log realised volatility lie between 0 and 0.5 and agree across series (andersen-2003, A, paper, FX). HAR is the simple stand-in for fractional models, which "lack a clear economic interpretation" (corsi-2009, A, paper). Crypto absolute returns show power-law autocorrelation decay (watorek-2021, B, paper). A pooled 213-coin volatility model beats per-coin models (tang-2023, syn).
- Weak or missing: No Hurst estimate for crypto volatility; Tang's results are not printed; intraday HAR is "untested" (syn).
- For this system: Three-scale HAR on log realised volatility, pooled over SOL, BTC and ETH.

Q65. Which market leads price discovery?
- Established: Offshore perpetuals and futures are "much the strongest" for bitcoin; CME and US spot "react to, rather than lead", "relatively slowly" (alexander-2020, B, note, abstract only, no shares). Volatility transmits from offshore derivatives to US spot venues, a cue for market makers to widen (alexander-2021, B, paper). CME futures lead Binance spot more often than not, but their share was 0.158 on the 5 August 2024 crash day (plazuelo-2025, C, note). Under a closeness-to-long-run rule Binance spot, not the perp, leads in a cascade (shen-2026, B, note).
- Weak or missing: Nothing on SOL, nothing on Binance versus Coinbase directly.
- For this system: Measure the chain Binance perp, Coinbase spot, Kalshi index, Kalshi mid link by link.

Q66. Does bitcoin lead altcoins at one minute or less?
- Established: ETH and LTC respond inside the same minute; only small caps respond at lag one (kurihara-2026, B, paper and note). Responsiveness correlates 0.56 and 0.48 with log trade count in two regimes (syn). Across 80 liquid coins lag-zero correlation dwarfs lag-one (kwapien-2021, B, note). IBIT and Binance BTC correlate 0.982 over 49,170 minutes; the largest displaced correlation is 0.013 (kitron-2026, B, paper).
- Weak or missing: SOL is in neither study; sub-minute lags are unmeasured.
- For this system: Confirms item 5. The trade-count rule predicts the lagging instrument is Kalshi itself: measure its response time to Binance.

Q67. Do lagged returns of other coins predict a coin's next return?
- Established: Opposite signs from two abstract-only notes: positive spillover (guo-2024, B, note) and a negative "seesaw" from large coins (jia-2023, B, note). A random forest on lagged returns of 40 coins earned a small positive 120-minute return net of 15 bp per half-turn, three months out of sample (fischer-2019, B, note). Twelve quarter-hour-spaced lags of the opening 10-second return give positive out-of-sample R-squared for all six assets, average 2.464%; lags are the stronger block for SOL (kim-2026, B, paper). Cross-coin Granger links are stronger in calm minutes (joshi-2025, C, note).
- Weak or missing: Sign and bar length unresolved. Kim's target is the boundary 10-second return, not a tradable holding return.
- For this system: Test the sign of lagged BTC and ETH returns on SOL at 5 and 15 minutes, split by calm and volatile state.

Q68. Equity index futures to crypto within minutes
- Established: Only that no source measures a lead from equity futures to BTC or SOL at seconds to minutes; the link is contemporaneous (syn). Crypto and S&P 500 responses to macro news correlate about 0.88 (kroner-2026, C, note, second-hand).
- Weak or missing: Using the futures' first move as a surprise proxy is the note-writer's suggestion, untested.
- For this system: Nothing; no equity futures feed is recorded.

Q69. Coinbase premium or US-hours gap
- Established: Nothing. No passage scored above 0.5; the one printed (kim-2026, B, paper) describes an unrelated regression design.
- Weak or missing: The whole question.
- For this system: Test directly: Coinbase spot minus Binance perp gap against the next 5 to 60 minutes of the Kalshi index.

Q70. Tether to dollar rate and USDT versus USD venues
- Established: Nothing scored above 0.5. The best passage: order-flow price impact on USDT is far higher than in major currencies, insignificant when Tether is at a discount and much larger at a significant premium (lyons-2020, B, paper, daily).
- Weak or missing: No intraday evidence on how peg deviations distort venue comparisons.
- For this system: Binance is USDT-quoted and the Kalshi index is USD, so any Binance-versus-index gap contains the peg. No USDT/USD series is listed as recorded: a data gap.

Q71. Variance share of the crypto factor and stability of beta
- Established: One factor explains 67% of the variance of seven major coins, against 20% for the global equity factor; a higher institutional share roughly doubles crypto-equity co-movement (copestake-2026, B, note). Pointers: first principal component from 36% (2015-16) to above 80% (2019-20) (aslanidis-2020, syn); bitcoin's 30-minute beta to the Dow from about zero to 1.317 at a December 2020 break (drexler-2026, syn).
- Weak or missing: No SOL loading; no intraday beta-stability estimate. The borri-2026 table is garbled.
- For this system: Rolling first-component share and SOL's loading on five-minute SOL, BTC, ETH returns; compute SOL-specific features on residuals.

Q72. Measuring lead-lag between asynchronous series
- Established: Hayashi-Yoshida cross-correlation on raw ticks, lag grid 0.01 s to 300 s; the lead/lag ratio is the sum of squared correlations at positive lags over negative lags; surrogate Brownian motions at the true timestamps give a ratio of 1; previous-tick resampling is biased toward "the more active asset leads" (huth-2014, A, paper and note). The shifted-contrast estimator assumes no microstructure noise: subsample until the signature plot flattens (hoffmann-2013, B, note). Leaders can differ by time scale (hayashi-2020, B, paper).
- Weak or missing: The other two passages are daily equity methods.
- For this system: Use the lead/lag ratio with the surrogate test for every Binance, Coinbase and Kalshi pair, by scale.

Q73. Is overshooting mistaken for leadership?
- Established: Yes in one source: magnitude-based measures "systematically misclassify leadership, often rewarding the least efficient market" when a market overshoots or first moves the wrong way (shen-2026, B, paper).
- Weak or missing: One paper; its reported results are not printed here.
- For this system: Do not treat a larger Binance perp move as the permanent one; see idea 3.

Q74. Solana DEX or on-chain activity leading centralised prices
- Established: No test exists. Centralised-exchange returns predict Uniswap returns up to about 12 minutes ahead (hansen-2021, B, note). Raw Solana swap volume overstates demand because of sandwich legs (heimbach-2026, B, note). Tips and priority fees update every slot; lead-lag untested (helius-2025, C, note).
- Weak or missing: Ethereum AMM results may not carry to Solana's sub-second blocks.
- For this system: Nothing; no on-chain series is recorded.

Q75. Does funding or the premium predict the perpetual's return?
- Established: No source tests it at minutes to hours. Granger tests at eight hours reject non-causality in both directions, with no sign, size or out-of-sample test (nimmagadda-2019, C, note). Pointers: funding and spot returns correlate 0.08 to 0.23 contemporaneously (he-2022, syn); the funding clock does not condition 15-minute reversal (kitron-2026, syn).
- Weak or missing: Signed returns around settlement are reported nowhere.
- For this system: Nothing for direction; Kalshi funding is usually zero. Agrees with item 5.

Q76. Liquidity, volume and volatility around funding settlement
- Established: In settlement hours spot dollar volume rises over 50%, spreads widen 3.2%, VPIN rises 17.4% and order imbalances shrink (ruan-2024, B, paper); identical figures appear in anonymous-2025 (B, paper), probably the same work, with the effect growing in funding size. Volume and volatility spike at 00:00 and 16:00 UTC, less at 08:00, and bursts are strongest every fourth hour (hansen-2024, A, note).
- Weak or missing: No signed returns; SOL and 2025-26 not covered.
- For this system: A funding-hour and four-hour term in the cone width, and a markout split for resting fills in those minutes.

Q77. Are funding rates predictable from their own history?
- Established: Persistence is the main forecastable feature and a no-change forecast is hard to beat; model lag orders unseen (inan-2026, B, note). A GARCH-type fit on BitMEX has no out-of-sample test (nimmagadda-2019, C, paper).
- Weak or missing: Bitcoin on deep venues only.
- For this system: Nothing; if Kalshi funding turns non-zero, carry the last value forward.

Q78. Open interest change with price change: new positioning or forced closing?
- Established: Nothing tested. The split (open interest falling with one-sided taker flow means forced closing, fade; rising means new positioning, follow) is a synthesis proposal resting on llorente-2002, and the synthesis says "none has been tested in the sources".
- Weak or missing: Everything empirical.
- For this system: Not testable on the listed recordings, which hold no open interest series. Agrees with item 5.

Q79. Early warning for liquidation cascades
- Established: Across seven bitcoin cascades (2022-2025) no variable is event-invariant. The October 2025 pattern inverted on August 2024: price carried the lag-1 autocorrelation signal in 28 of 39 configurations, open interest 3, taker flow 1. The one consistent feature, falling variance of the taker buy/sell ratio, is too weak for an alarm (garcia-seuma-2026-early, C, paper and note). Within-venue branching ratio was 0.1 to 0.2 (garcia-seuma-2026-branching, syn).
- Weak or missing: Single-author preprints, seven events.
- For this system: No alarm feature; rely on the unfamiliar-state gate.

Q80. Reliability of reported volume and open interest
- Established: The change in open interest cannot exceed traded volume, yet the bound fails on most of seven large venues; Bybit and OKX never reconcile (giagkiozis-2024, B, paper). Wash trading averaged 77.5% of volume on unregulated exchanges, but 16.3% by a second method; regulated exchanges pass (cong-2023, A, note). Pointer: Kalshi daily volume is about 12 times open interest during rebate programmes (syn).
- Weak or missing: Cong's data are 2019 spot.
- For this system: Scale volume features per venue; treat Coinbase as the clean volume; never read Kalshi volume as depth.

Q81. No-arbitrage bounds on the perpetual basis
- Established: With round-trip cost C the perpetual lies within a spot-proportional band widened by C on each side; the Binance band depends on the premium coefficient, the clamp and interest (he-2022, B, paper; formula garbled). The clamp is a key cause of deviation (kim-2025, C, paper, citing Dai et al.).
- Weak or missing: No empirical account of when bounds break.
- For this system: My inference: Kalshi mid can sit about one round-trip cost from its index unarbitraged. Measure that gap's distribution and half-life.

Q82. Is crypto carry compensated by crash risk?
- Established: High carry is linked to scarce arbitrage capital, leverage constraints and crash risk (schmeling-2023, B, note, abstract only). A backtest on last-traded prices can report a path the margined account could not survive, and applying today's contract terms to earlier periods leaks (zhu-2026, B, paper).
- Weak or missing: Daily to multi-day, BTC and ETH; untested for SOL or hours.
- For this system: Nothing as a signal. The replay should liquidate on Kalshi's mark rules and time-stamp fee and contract changes.

Q83. Long/short ratios and top-trader positioning
- Established: No rigorous test exists. Binance publishes three ratios; only the top-trader position ratio is size-weighted, the others count accounts (binance-2026, B, note). The contrarian claim rests on one episode (samsoedin-2025, D, note).
- Weak or missing: Everything predictive.
- For this system: Nothing.

Q84. Auto-deleveraging and insurance-fund events
- Established: Description only: auto-deleveraging closes solvent traders at prices that keep the exchange solvent; several venues used it on 10-11 October 2025 (campbell-2026, B, paper).
- Weak or missing: No price-impact measurement.
- For this system: A replay rule that can close a winning position early in stress; read Kalshi's rule.

Q85. Why does volume spike at the top of the hour and at quarter-hours?
- Established: The share of round-sized trades drops in the 10-second bursts, an algorithmic signature (kim-2026, B, paper). The first 10 seconds of quarter-hour minutes carry about 26% more trades and 32% more dollar volume (syn). At one-second resolution volume spikes at the first second of the hour and fades over minutes; Coinbase's largest spike is 20 minutes into the hour, called puzzling (hansen-2021, B, paper). Every-eighth-hour spikes are attributed to funding (alexander-2021, B, paper).
- Weak or missing: Who runs the schedules is inferred, not observed.
- For this system: Check whether Coinbase's minute-20 spike persists in the recorded trades; it would enter the index.

Q86. Hour-of-day or day-of-week return patterns after snooping correction
- Established: Only the general warning that many researchers mining one series with outliers manufacture calendar anomalies (sullivan-2001, A, paper, US equities). A synthesis elsewhere in the pack calls crypto mean-return seasonality weak and unstable.
- Weak or missing: No snooping-adjusted crypto test.
- For this system: Nothing; agrees with item 5. Any clock-return gene the search finds needs a multiple-testing check.

Q87. Benchmark fixings, option expiries, settlement windows
- Established: Nothing. The only passage is a synthesis list of open questions: momentum into the US equity close, the Deribit 08:00 UTC expiry and CME reference windows, and a pre-window drift with post-window reversal.
- Weak or missing: All evidence.
- For this system: Kalshi's hourly range settlement is itself a 60-second fixing: see idea 1.

Q88. Crypto response to CPI, payrolls and FOMC in the first 30 minutes
- Established: Bitcoin did not respond systematically in 30-minute windows, 2017-2022; only core CPI was significant, and not robust to dropping 2022 (benigno-2023, B, paper). The 60-minute bitcoin response per standard deviation of CPI surprise was -3.87 bp (11.13) in low inflation and -114.25 bp (40.41) in high inflation (kroner-2025, B, note, cells reconstructed). Second-hand: about -30 bp bitcoin and -43 to -46 bp ether, absorbed in 15 to 30 minutes; the payrolls sign flipped around 2020 (kroner-2026, C, note).
- Weak or missing: SOL; about 32 events a year.
- For this system: Volatility flag only; a 30 bp response does not clear a 28.5 bp taker round trip.

Q89. Price drift before scheduled announcements
- Established: For seven of 21 market-moving US releases, E-mini and Treasury futures move in the surprise's direction from about 30 minutes before, about half the total adjustment, 2008 to 2014 (kurov-2016, A, paper); not CPI or payrolls (syn). The S&P 500 rose 49 bp in the 24 hours before scheduled FOMC announcements, 1994 to 2011, without reversal (lucca-2015, A, paper); weaker after publication (lucca-2018, syn).
- Weak or missing: No crypto test of direction.
- For this system: Nothing as a rule; the event sample is too small.

## Ideas from this block

1. The hourly range settlement as a fixing inside the clock burst. Sources: the largest volume and volatility burst sits in the first second and minute of each hour (hansen-2021); boundary taker imbalance reverses within 30 minutes (kim-2026, syn); a fixing V-shape is an open hypothesis (Q87). Inference: the range contracts' 60-second index average sits on that burst, so hedging of 300 bands could add a drift and reversal that the :15, :30 and :45 boundaries lack. Data: Kalshi index, perp book, range quotes. Kill: an event study of index and perp mid 10 minutes either side of each hour against the other quarter-hours; no difference.

2. Clock-conditioned markout of resting fills. Sources: at funding hours volume is up 50% while spreads widen only 3.2% and VPIN rises 17.4% (ruan-2024); boundary bursts are algorithmic and their imbalance reverses within 30 minutes (kim-2026). Inference: a resting order filled in the first seconds of an ordinary quarter-hour meets flow that reverses, which pays a maker; the same fill at 00, 08 or 16 UTC meets more informed flow. Data: Kalshi trades with taker side, and book. Kill: 5 and 30 minute markouts by seconds-since-boundary and funding hour; no spread between buckets. This is item 1's open measurement.

3. Perp-minus-spot overshoot as the fade state. Sources: perps overshoot and spot leads in cascades (shen-2026); volatility flows from offshore derivatives into US spot (alexander-2021). Inference: the Kalshi index is US spot, so when the Binance perp has moved further than Coinbase spot, takers who copy Binance hit Kalshi quotes at prices the index will not confirm, and resting on the far side has a favourable markout. Data: Binance and Coinbase trades and books, Kalshi fills. Kill: regress the next 1 to 15 minute index return on the gap; a zero or positive slope kills it.

4. Kalshi as the illiquid lagger, by hour. Sources: response speed rises with trade count (kurihara-2026); Coinbase volume is thin from 05 to 12 UTC (hansen-2024); previous-tick methods fake a lead (huth-2014). Inference: the Binance-to-Kalshi lag lengthens in thin hours, when stale resting orders are picked off; gate or reprice posting by measured lag. Data: all three tick streams. Kill: the lead/lag ratio with surrogates, by hour; a flat lag, or markouts unrelated to it, kills it.

5. Deterministic clock factor ahead of realised variance. Source: for BTC/USD, periodicity improved log-likelihood by about 19 in-sample and 34 out-of-sample, against 5 and 18 for realised variance (hansen-2024). Inference: multiply the cone width by a minute-of-hour, hour-of-week and macro-calendar factor, and score it against range-contract implied widths. Kill: no gain in cone coverage on held-out weeks.

6. Clean-venue activity as the volatility input. Sources: lag-1 volume raises and lag-2 lowers volatility (alexander-2021); raw volume beats VPIN (andersen-2014); offshore volume is partly wash and regulated venues pass (cong-2023). Inference: Coinbase trade count may forecast index volatility better than Binance volume. Kill: out-of-sample 5 to 60 minute variance loss with each input.

7. Asymmetric tail penalty. Source: long margins nearly double short margins at eight hours and 0.001 (cheng-2021). Inference: penalise long and short tails separately within eight-hour fitness blocks. Kill: equal left and right block-extreme parameters for SOL on the recorded tape.

## Contradictions and surprises

- Macro direction: benigno-2023 finds no bitcoin response in 2017-2022; kroner-2025 finds -114 bp in high inflation; kroner-2026 (second-hand) about -30 bp. Regime-specific, and none is measured on SOL.
- Speed: FX adjusts inside five minutes (andersen-2002); crypto is reported at 15 to 30 minutes, second-hand only.
- Cross-coin sign: guo-2024 positive, jia-2023 negative, both abstracts.
- Leadership: alexander-2020 says offshore perps lead; shen-2026 says that is partly an overshoot artefact and spot leads in cascades. It matters because Kalshi's index is spot.
- VPIN: ruan-2024 reads the 17.4% rise at funding as informed trading, but andersen-2014 shows VPIN rises mechanically with volume, which is up 50% in the same hours, and ruan-2024 itself reports imbalances shrinking.
- ruan-2024 and anonymous-2025 report identical numbers: probably one study, not two confirmations.
- Against item 1: fischer-2019 reports a net-positive result at 120 minutes after 15 bp per half-turn, on 40 coins in an early sample.
- Against item 2's "SOL weakest": in kim-2026 lagged boundary returns are the stronger predictor block for SOL, though the target is the 10-second opening return; SOL's 4 and 12 hour slopes are significant only at 90% (syn).
- Rising open interest predicts higher commodity returns, 0.73% a month per standard deviation (hong-2012, syn), opposite to the crypto "crowding" reading.
- The volatility asymmetry term is insignificant (hansen-2024) while the left tail is heavier (cheng-2021).
