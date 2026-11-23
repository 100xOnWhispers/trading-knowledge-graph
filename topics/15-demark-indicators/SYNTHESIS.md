# Topic 15: DeMark indicators - synthesis

Twelve notes. One is an academic working paper; the rest are a book chapter, vendor documentation, an open-source library, and practitioner backtests. No rigorous test on crypto or on intraday bars was found, and no reinforcement-learning or evolutionary study of these indicators was found. The web-search budget for this session ran out twice, so the search for machine-learning work in particular was shallow (see Open questions and the gaps listed at the end).

## What the literature agrees on

**The core counting rules are public and consistent across sources.** Buy side shown; the sell side mirrors it. C, H, L are close, high, low of closed bars.

| Element | Rule | Sources |
|---|---|---|
| Price flip | `C[t-1] > C[t-5]` then `C[t] < C[t-4]`; that bar is setup bar 1 | [Perl](notes/perl-2008-demark-indicators-td-sequential-chapter.md), [PowerStocks](notes/powerstocks-2014-modified-demark-setup-jse.md), [QuantConnect code](notes/anonymous-2017-demark-setup-btcusd-quantconnect-backtest.md) |
| Setup | 9 consecutive bars with `C[t] < C[t-4]`; equality or an opposite close resets; the run continues past 9 until the opposite flip | all |
| TDST | Completed buy setup: resistance = its highest true high. Completed sell setup: support = its lowest true low. Only closes through the level count | [Perl](notes/perl-2008-demark-indicators-td-sequential-chapter.md), [DeMARK Analytics](notes/demark-2025-sequential-indicator-symbolik-documentation.md), [Lissandrin](notes/lissandrin-2015-statistical-testing-demark-commodity-futures.md) |
| Perfection | Low of bar 8 or 9, or a later low, at or below the lows of bars 6 and 7 | Perl, DeMARK Analytics |
| Countdown | From setup bar 9 inclusive, count non-consecutive bars with `C[t] <= L[t-2]` to 13 | Perl, DeMARK Analytics, [Wickra](notes/wickra-2026-open-source-td-indicator-suite.md) |
| Bar 13 deferral | Bar 13 counts only if `L(13) <= C(countdown bar 8)` | Perl, DeMARK Analytics, Lissandrin, Wickra |
| Cancellation | An opposite setup completes, or a true low prints above TDST resistance | Perl, DeMARK Analytics, Lissandrin |
| Entry | Aggressive: close of bar 13. Conservative: first later close above the close 4 bars earlier | Perl, Lissandrin, [MarketInOut](notes/marketinout-2011-demark-td-lines-qualifiers-demarker.md) |
| Risk level | Bar with the lowest true low in the whole countdown: its true low minus its true range | Perl |
| Timing | A reaction is expected within 12 bars of a 13; a completed setup that holds TDST should give a 1 to 4 bar reaction | Perl, DeMARK Analytics |
| DeMarker | `SMA(max(H-H[1],0),N) / (SMA(max(H-H[1],0),N) + SMA(max(L[1]-L,0),N))`, N = 14, bands 0.3 and 0.7 | MarketInOut, Wickra; same formula in MetaTrader 5 help |

True high is `max(H, C[1])` and true low is `min(L, C[1])` (stated in the Wickra documentation, citing Perl).

**The signals are sparse on daily bars.** Lissandrin et al. count 3.9 Sequential entries, 1.7 Combo entries and 4.5 TDST-break entries per market per year. Ellison finds 14 Sequential buy signals on S&P 500 futures in about 30 years. PowerStocks reports that a buy count reaching 9 is in the top 6.4% of run lengths on the JSE Top 40.

**Fading a completed countdown is not a proven edge.** The widest test, Oxfordstrat's 42-market futures portfolio over 1980 to 2013, shows profit factors below 1 across nearly the whole parameter grid before costs ([countdown note](notes/oxfordstrat-2013-td-sequential-countdown-futures-backtest.md)). Lissandrin et al. find the signals statistically informative on commodities but say Sequential "does not seem to be able to forecast the correct market direction", and that on energy a buy signal marked a continuing downtrend.

**The setup carries trend information.** Trading with a completed 9 was profitable on the same futures portfolio and survived a $100 round-turn cost at holds of ten days or more ([setup-trend note](notes/oxfordstrat-2013-td-setup-trend-futures-backtest.md)). Lissandrin's TDST-break rule "captures correctly the direction". Perl and the vendor agree in words: a close through TDST (Perl), a setup that extends far enough to recycle the countdown, or a long stay of an oscillator at an extreme (DeMARK Analytics) all signal continuation.

**Buy and sell signals behave differently.** Ellison's S&P buys beat the unconditional mean and sells did not. Lissandrin's results are mostly one-sided per market. PowerStocks uses different thresholds for the two sides.

## Where it disagrees or is weak

**Rule variants.** An implementation must pick, and should expose each as a parameter.

| Item | Variants | Sources |
|---|---|---|
| Intersection | Required in the 1994 rules (high of bar 8 or 9 at or above a low 3 or more bars earlier); dropped in Perl 2008 | MarketInOut, Oxfordstrat, [Ellison](notes/ellison-2012-demark-sequential-sp500-futures-test.md); thinkorswim's SequenceCounter documentation also keeps it |
| Countdown test | `C <= L[2]` (standard); `C < L[2]` (Oxfordstrat's 1994 version); `L <= L[2]` ("aggressive", used by Lissandrin); `C < C[2]` (Ellison) | as listed |
| Recycle | 18-bar setup and range ratio 1.0 to 1.618 (Perl); 22 bars and 100 to 200% (DeMARK Analytics); any wider range (Lissandrin); none (Wickra) | as listed |
| Combo | Four conditions counted from setup bar 1 (Lissandrin); three conditions after the setup (Wickra) | as listed |
| Price flip | Required (Perl); ignored (Wickra, Oxfordstrat, pandas-ta) | as listed |
| Duration split | Under 5 bars in the zone for DeMarker (MarketInOut); 6 or fewer for REI (DeMARK Analytics) | as listed |
| REI bands | Plus or minus 60 in Wickra; not confirmed against DeMark's books | Wickra |

The pandas-ta function `td_seq` (source read, no note written) returns only a run-length count of `close.diff(4)` signs inside a rolling 13-bar window. It is a setup counter, not Sequential, and should not be treated as a countdown.

**Direction of the edge.** Sources split on whether a 9 or 13 should be faded or followed. Perl and the vendor say fade, conditional on TDST. Oxfordstrat's data says follow the 9 and do not fade the 13. Ellison's data says fade on the long side only. Nobody has tested Perl's full conditional rule (perfected, TDST held, bar 9 near TDST, reward above 1.5 times risk) as written.

**Evidence quality.** Only Lissandrin et al. use a formal test, and it has no costs, no out-of-sample split and no multiple-testing correction over 21 markets, two sides, 14 holding periods and 3 metrics. Oxfordstrat publishes charts without tables or significance tests. Everything else is small-sample or visual.

**Coverage gaps.** No source tests TD REI, TD DeMarker, TD Pressure, TD D-Wave, TD Lines, TD Moving Averages or TD Differential with data. Public formulas for D-Wave, Pressure and the Moving Averages are either absent or, in Wickra, simplified stand-ins. The vendor withholds formulas.

**Intraday and crypto.** The only intraday items are an hourly SPY hit-rate count with a flawed null ([Steversteves](notes/steversteves-2022-predictive-power-demark-spy-hourly.md)), a 4-hour BTC backtest that was flat after fees ([QuantConnect](notes/anonymous-2017-demark-setup-btcusd-quantconnect-backtest.md)), and a 15-minute FX article with about 30 training samples ([Marchukajtes](notes/marchukajtes-2017-td-sequential-neural-network-classifier.md)). Claims that the method works "from one minute to one year" rest on assertion.

**Machine learning.** One practitioner article filters Sequential signals with a small neural-network committee. It reports no statistics. No study using DeMark counts as features for gradient boosting, deep learning or reinforcement learning, and no genetic or evolutionary search over DeMark parameters, was located. Oxfordstrat's exhaustive grids are the nearest thing to a parameter search, and they show no stable optimum for the fade.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Signed setup count as a trend state (follow a completed 9; longer runs stronger) | Closes of closed bars, 4-bar lag | hours to multi-day | C | [oxfordstrat setup trend](notes/oxfordstrat-2013-td-setup-trend-futures-backtest.md), [quantconnect btc](notes/anonymous-2017-demark-setup-btcusd-quantconnect-backtest.md) |
| TDST close-through as breakout or regime flag | OHLC, last completed setups | multi-day in the source | B | [lissandrin](notes/lissandrin-2015-statistical-testing-demark-commodity-futures.md), [perl](notes/perl-2008-demark-indicators-td-sequential-chapter.md) |
| Countdown 13 or Combo 13 as an "event ahead" flag, direction unspecified | OHLC | multi-day in the source | B | [lissandrin](notes/lissandrin-2015-statistical-testing-demark-commodity-futures.md) |
| Countdown 13 fade, time exit | OHLC | 1 to 3 bars at most | C (negative) | [oxfordstrat countdown](notes/oxfordstrat-2013-td-sequential-countdown-futures-backtest.md) |
| Buy-side-only countdown 13 after a sharp decline | OHLC of a reference index | multi-day | C | [ellison](notes/ellison-2012-demark-sequential-sp500-futures-test.md) |
| Perfected setup 9 fade when TDST holds, risk-level stop, TDST target | OHLC | 1 to 4 bars | D (untested) | [perl](notes/perl-2008-demark-indicators-td-sequential-chapter.md) |
| Terminal run length at the flip, as a percentile of its own history | Closes | per bar size | D | [powerstocks](notes/powerstocks-2014-modified-demark-setup-jse.md) |
| Oscillator duration: bars spent beyond the band (REI, DeMarker); short stay fade, long stay follow | High, low | minutes to hours | D (untested) | [demark analytics](notes/demark-2025-sequential-indicator-symbolik-documentation.md), [marketinout](notes/marketinout-2011-demark-td-lines-qualifiers-demarker.md), [wickra](notes/wickra-2026-open-source-td-indicator-suite.md) |
| TD Line break with qualifiers 1 and 3 | OHLC, level-1 TD Points | minutes to hours | D (untested) | [marketinout](notes/marketinout-2011-demark-td-lines-qualifiers-demarker.md) |
| TD Differential two-bar pressure shift | OHLC | 1 bar | D (untested) | [wickra](notes/wickra-2026-open-source-td-indicator-suite.md) |
| Meta-labeling: classifier decides which DeMark events to take | Event list plus order flow, open interest, funding, volatility | minutes to hours | D | [marchukajtes](notes/marchukajtes-2017-td-sequential-neural-network-classifier.md) |
| Permutation test for sparse entry signals (method) | Signal series and bar returns | any | B | [lissandrin](notes/lissandrin-2015-statistical-testing-demark-commodity-futures.md) |
| Joint sweep of count parameters and holding period, looking for a plateau (method) | Backtest engine | any | C | both oxfordstrat notes |

Feature encoding for learned models, since no source provides one. For each bar size, emit: signed running setup count; flag and age of the last completed 9; perfection flag; countdown and Combo counts; deferral flag; recycle and cancel events; distance from close to TDST support and resistance in ATR units; distance to the risk level; REI and DeMarker values with bars-in-zone counters; TD Differential sign. These are bounded, cheap, and computable on Binance or Bybit SOL perpetual bars for use on Kalshi. For tree models and reinforcement-learning state vectors they are ordinary categorical and numeric inputs. For an evolutionary search, the genome is (lag n, setup length m, countdown lag u, countdown length p, qualifier bar k, recycle bars, recycle ratio bounds, comparison type), and fitness should be the permutation-test quantile on held-out data, not raw profit, because the Oxfordstrat grids show how easily isolated profitable cells appear.

## Open questions worth testing on SOL perps

1. After a completed 9 on 5-minute, 15-minute and 1-hour bars, is the next 1 to 12 bars' return continuation or reversal, net of Kalshi costs? Test buys and sells separately, and perfected against unperfected.
2. Does conditioning on TDST change the sign, as Perl claims (setup that holds TDST reverses; setup that closes through it extends)?
3. Does a countdown 13 predict higher absolute return or realized volatility over the next 12 bars without predicting direction, as Lissandrin's commodity result suggests?
4. Is the setup count worth anything beyond a plain 4-bar momentum sign and run length? Benchmark against simple momentum and against a drawdown-size trigger.
5. Which venue's bars should drive the count? Compare counts from Binance, Bybit, OKX and Hyperliquid SOL perpetuals and test whether a consensus 9 is cleaner than one venue's.
6. How sensitive are counts to bar alignment and tick size? Equal closes reset a setup, and a 24-hour market has no natural bar boundary, so shifting bar start times by a minute may change the signal. Measure the instability.
7. Does the duration rule hold: REI or DeMarker beyond its band for under 5 or 6 bars against longer stays?
8. Does a meta-label classifier on a large event set (thousands of setups across bar sizes) beat taking all events, using order-flow, open-interest and funding features from the larger venues?
9. For any positive result, does it pass a permutation test with the number of trades and holding period fixed, and survive a correction for the number of variants tried?
10. Open-based patterns (TD Open, Trap, Clop, Propulsion, breakout qualifier 2) need the open to differ from the prior close. Confirm they are inert on continuous bars, or redefine them around funding timestamps or session handovers and test that.

## Reading order

1. [perl-2008-demark-indicators-td-sequential-chapter](notes/perl-2008-demark-indicators-td-sequential-chapter.md) - the rules.
2. [demark-2025-sequential-indicator-symbolik-documentation](notes/demark-2025-sequential-indicator-symbolik-documentation.md) - the vendor's current wording and where it differs.
3. [lissandrin-2015-statistical-testing-demark-commodity-futures](notes/lissandrin-2015-statistical-testing-demark-commodity-futures.md) - the one formal test and the testing method to reuse.
4. [oxfordstrat-2013-td-sequential-countdown-futures-backtest](notes/oxfordstrat-2013-td-sequential-countdown-futures-backtest.md) - the negative result for the fade.
5. [oxfordstrat-2013-td-setup-trend-futures-backtest](notes/oxfordstrat-2013-td-setup-trend-futures-backtest.md) - the positive result for following the setup.
6. [ellison-2012-demark-sequential-sp500-futures-test](notes/ellison-2012-demark-sequential-sp500-futures-test.md) - buy and sell asymmetry.
7. [anonymous-2017-demark-setup-btcusd-quantconnect-backtest](notes/anonymous-2017-demark-setup-btcusd-quantconnect-backtest.md) - the only crypto intraday backtest, with fees.
8. [marketinout-2011-demark-td-lines-qualifiers-demarker](notes/marketinout-2011-demark-td-lines-qualifiers-demarker.md) - TD Lines, qualifiers, projections, DeMarker.
9. [wickra-2026-open-source-td-indicator-suite](notes/wickra-2026-open-source-td-indicator-suite.md) - formulas for REI, Differential and the rest, with their limits.
10. [marchukajtes-2017-td-sequential-neural-network-classifier](notes/marchukajtes-2017-td-sequential-neural-network-classifier.md) - the signal-plus-classifier pattern.
11. [powerstocks-2014-modified-demark-setup-jse](notes/powerstocks-2014-modified-demark-setup-jse.md) - run-length distribution and flip entry.
12. [steversteves-2022-predictive-power-demark-spy-hourly](notes/steversteves-2022-predictive-power-demark-spy-hourly.md) - an example of how not to test a reversal signal.

Sources read but not given notes: thinkorswim SequenceCounter documentation (keeps the 1994 intersection; its array perfection test is `Low <= Close[5 bars ago]`, a bar offset and not countdown bar 8), MetaTrader 5 DeMarker help page, MotiveWave DeMarker page (default period 20, scaled by 100), and the pandas-ta `td_seq` source.

Not accessible in this session: DeMark's own books (The New Science of Technical Analysis; New Market Timing Techniques; DeMark on Day Trading Options); the remaining chapters of Perl's book (TD Combo, D-Wave, REI, DeMarker, Pressure, Lines, Moving Averages); the journal version of Lissandrin et al.; Lissandrin's ETH master's thesis; Coles (2011) on TD Sequential for intraday traders in Stocks & Commodities (HTTP 403); Bloomberg and CQG help pages; Quantified Strategies' DeMarker backtest (bot check).
