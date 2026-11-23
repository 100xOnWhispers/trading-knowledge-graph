# Topic 09 synthesis: liquidity measurement and price impact

Fifteen source notes sit in `notes/`. Thirteen have an open-access PDF in `sources/09-liquidity-price-impact/`; two are web pages. The web search budget for the session ran out part-way through, so several sub-areas rest on fewer sources than planned. The gaps are listed at the end of the second section.

## What the literature agrees on

1. **Impact is concave in size and scales with volatility and volume.** The average price move from a metaorder of size Q is close to `Y * sigma_daily * sqrt(Q / V_daily)` with Y near one. This holds on futures ([Toth 2011](notes/toth-2011-anomalous-impact-critical-liquidity.md)), US equities with a slightly higher exponent ([Almgren 2005](notes/almgren-2005-direct-estimation-equity-market-impact.md)), Bitcoin spot ([Donier 2015](notes/donier-2015-million-metaorder-bitcoin-impact.md)) and Japanese equities ([Maitrier 2025](notes/maitrier-2025-double-square-root-law-impact.md)). The practical unit of impact is `sigma / sqrt(V)`.

2. **Impact is transient.** Order flow has long memory because large orders are split, so each trade's impact must decay for prices to stay unpredictable ([Bouchaud 2008](notes/bouchaud-2008-markets-slowly-digest-supply-demand.md)). The decay is roughly an inverse square root of elapsed time ([Maitrier 2025](notes/maitrier-2025-double-square-root-law-impact.md)). Flow that is uncorrelated with the rest of the market leaves little or no permanent impact ([Donier 2015](notes/donier-2015-million-metaorder-bitcoin-impact.md)), and pre-announced flow leaves less than hidden flow ([Barone 2026](notes/barone-2026-hyperliquid-market-impact-adverse-selection.md)).

3. **Visible liquidity is a small fraction of true liquidity.** Volume at the best quotes is about a thousandth of daily turnover ([Toth 2011](notes/toth-2011-anomalous-impact-critical-liquidity.md)); the book holds about 1% of daily volume ([Bouchaud 2008](notes/bouchaud-2008-markets-slowly-digest-supply-demand.md)). Displayed depth also reacts to flow: it rises to absorb visible TWAPs ([Barone 2026](notes/barone-2026-hyperliquid-market-impact-adverse-selection.md)) and collapses in a liquidation cascade ([FTI 2025](notes/fticonsulting-2025-crypto-crash-leverage-liquidity.md)).

4. **No single liquidity measure does everything.** In crypto, high-low based spread estimators track changes in liquidity over time, while volatility-over-volume measures (Amihud, Kyle-Obizhaeva) are better for levels and for ranking venues ([Brauneis 2021](notes/brauneis-2021-measure-liquidity-cryptocurrency-markets.md)). Bar-based spread estimators are biased when trades are sparse, and the EDGE estimator corrects this ([Ardia 2024](notes/ardia-2024-efficient-bid-ask-spread-ohlc.md), [Abdi 2017](notes/abdi-2017-bid-ask-spread-close-high-low.md)).

5. **Crypto liquidity has a clock.** Volatility, volume and illiquidity vary by weekday, hour and minute of the hour, with bursts at funding times and on the hour ([Hansen 2021](notes/hansen-2021-periodicity-crypto-volatility-liquidity.md)). Liquidity is concentrated on a few venues, and volume share is a poor guide to depth share ([Kaiko 2023](notes/kaiko-2023-crypto-liquidity-concentration-report.md)).

6. **Liquidity conditions predict volatility better than direction.** Microstructure liquidity measures predict the sign of the change in realized volatility for SOL and four other coins with accuracy of 0.56 to 0.58, and predict nothing about skewness ([Easley 2024](notes/easley-2024-microstructure-dynamics-crypto-markets.md)). Illiquidity shocks coincide with price falls in equities ([Amihud 2002](notes/amihud-2002-illiquidity-stock-returns.md)).

7. **Price-contingent orders create short-lived continuation.** Stops cluster just beyond round numbers and prices trend for minutes to about two hours after crossing them ([Osler 2002](notes/osler-2002-stop-loss-orders-price-cascades.md)).

## Where it disagrees or is weak

- **The exponent.** One half is the consensus, but Almgren et al. reject it for 0.6 on equities, and Barone and Lillo find about 0.3 for visible TWAPs and a saturating curve for hidden metaorders on Hyperliquid perps. The one large study on crypto perpetuals is the one that fits the square-root law worst. A paper opened but not noted (Bonart, arXiv:2606.07059, 2026) argues the square-root law follows from requiring realized and counterfactual prices both to be diffusive, with a crossover to linear impact when flow is informed.
- **Mechanical versus informational impact.** Maitrier et al. and Donier and Bonart argue impact is mechanical. Barone and Lillo find that who trades and whether the order is announced changes both temporary and permanent impact, which is an adverse-selection result. Both can be true if the mechanical part is common and the permanent part depends on information, but this is not settled.
- **Amihud in crypto.** The most used illiquidity measure fails to track time variation in crypto spreads because volume and costs rise together ([Brauneis 2021](notes/brauneis-2021-measure-liquidity-cryptocurrency-markets.md)). Yet Easley et al. and Hansen et al. still use Amihud-type ratios. Treat it as a level or venue-ranking tool only.
- **Spread estimators disagree on level.** On Binance pairs, Abdi-Ranaldo and Corwin-Schultz change about tenfold with bar frequency ([Ardia 2024](notes/ardia-2024-efficient-bid-ask-spread-ohlc.md)). None of the bar-based estimators has been validated against quote data for SOL or for any perpetual.
- **Stop-run evidence is old and from FX.** The measured effect is about one basis point at 15 minutes. There is no rigorous crypto study in this folder linking liquidation clusters to continuation or reversal.
- **Liquidity crises.** The only source on the October 2025 crash is an unsourced consulting article (grade D). Other accounts seen in search results gave different magnitudes for the depth collapse.
- **Machine learning.** The only ML source is a random forest on five hand-built features ([Easley 2024](notes/easley-2024-microstructure-dynamics-crypto-markets.md)). It predicts volatility regime, not direction, at a one-day look-ahead.

**Not covered, because search was cut short:**
- Commonality in liquidity across crypto assets and venues. A liquidity-connectedness paper in Financial Innovation (DOI 10.1186/s40854-021-00308-3) and a 2025 JRFM paper on order-book liquidity across exchanges appeared in search results but could not be opened.
- Deep learning, reinforcement learning and evolutionary methods applied to liquidity or impact forecasting. Two candidates appeared in search results and were not opened: arXiv:2506.05764 (crypto limit-order-book models, simple versus deep) and arXiv:2602.00776 (explainable patterns in Binance Futures microstructure). Reinforcement learning with learned impact models sits mainly in topic 27 (execution).
- Resiliency (speed of book refill after a shock) in crypto, measured directly.
- Roll (1984) and Corwin and Schultz (2012) as primary sources. Their formulas are covered through Brauneis, Abdi and Ardia. A conference copy of Corwin-Schultz was downloaded and then removed without a note.
- Bouchaud, Gefen, Potters and Wyart (2004), the original propagator paper, was downloaded and is covered here only through the 2008 review.
- Donier and Bouchaud, "Why do markets crash? Bitcoin data offers unprecedented insights" (arXiv:1503.06704), on impact as a crash predictor, was seen but not opened.
- Any SOL-specific depth or impact study, and any data on Kalshi's own book.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Impact unit `sigma_24h / sqrt(V_24h)` and expected move from net flow | Trades or 1-min bars on reference venue | minutes to hours | A (law), untested as signal | [toth-2011](notes/toth-2011-anomalous-impact-critical-liquidity.md), [donier-2015](notes/donier-2015-million-metaorder-bitcoin-impact.md) |
| Pre-trade cost model, permanent plus temporary | Order size, duration, sigma, V | hours | B | [almgren-2005](notes/almgren-2005-direct-estimation-equity-market-impact.md), [barone-2026](notes/barone-2026-hyperliquid-market-impact-adverse-selection.md) |
| Non-linear propagator pressure: sum of sign * sqrt(size) / sqrt(age) | Public trade tape | seconds to minutes | B | [maitrier-2025](notes/maitrier-2025-double-square-root-law-impact.md), [bouchaud-2008](notes/bouchaud-2008-markets-slowly-digest-supply-demand.md) |
| Fade of uncorrelated or forced flow | Signed flow per venue, liquidation prints | minutes to hours | B (inference from impact decay) | [donier-2015](notes/donier-2015-million-metaorder-bitcoin-impact.md) |
| Visible TWAP pressure on Hyperliquid | Active TWAP notional by side, 24h volume | minutes to hours | B | [barone-2026](notes/barone-2026-hyperliquid-market-impact-adverse-selection.md) |
| EDGE effective spread from candles | 1-min OHLC | minutes | A (equities), C (crypto) | [ardia-2024](notes/ardia-2024-efficient-bid-ask-spread-ohlc.md) |
| Abdi-Ranaldo spread as liquidity-change tracker | 1-min HLC | hours | A | [abdi-2017](notes/abdi-2017-bid-ask-spread-close-high-low.md), [brauneis-2021](notes/brauneis-2021-measure-liquidity-cryptocurrency-markets.md) |
| Kyle-Obizhaeva or Amihud ratio for venue ranking and impact level | Bars with dollar volume | hours to daily | A | [brauneis-2021](notes/brauneis-2021-measure-liquidity-cryptocurrency-markets.md), [amihud-2002](notes/amihud-2002-illiquidity-stock-returns.md) |
| Volatility-regime classifier from Roll, VPIN, Amihud, Kyle lambda | 1-min bars for SOL, BTC, ETH | hours to one day | B | [easley-2024](notes/easley-2024-microstructure-dynamics-crypto-markets.md) |
| Seasonal multipliers by weekday, hour, minute | 1-min returns and volume | minutes | B | [hansen-2021](notes/hansen-2021-periodicity-crypto-volatility-liquidity.md) |
| Depth bands and depth share by venue | Order-book snapshots | minutes | C | [kaiko-2023](notes/kaiko-2023-crypto-liquidity-concentration-report.md) |
| Round-number and stop-cluster crossing | Price, level grid, liquidation map | 15 minutes to 2 hours | B (FX), untested in crypto | [osler-2002](notes/osler-2002-stop-loss-orders-price-cascades.md) |
| Liquidity circuit breaker | Depth and spread versus same-hour median, funding, open interest | minutes | D | [fticonsulting-2025](notes/fticonsulting-2025-crypto-crash-leverage-liquidity.md) |

## Open questions worth testing on SOL perps

1. What are the impact exponent and prefactor for SOL perps on Binance, Bybit, OKX and Hyperliquid, and do they match the Hyperliquid pooled values (0.12 on participation, 0.31 on duration)?
2. On Kalshi, how does realized slippage on the bot's own fills compare with `Y * sigma * sqrt(Q/V)` using Kalshi's volume? What is Kalshi's Y?
3. Does the impact unit `sigma / sqrt(V)` on the reference venue, relative to its same-hour history, predict the next hour's realized volatility or the probability of a large move?
4. After a burst of one-sided taker flow on one venue that other venues do not confirm, how much of the move reverts and how fast? Is the decay close to inverse square root in time?
5. Do liquidation prints behave like the "uninformed" metaorders of Donier and Bonart, with near-complete reversal? Does the answer change in thin-book hours?
6. Which bar-based spread estimator (EDGE, Abdi-Ranaldo, Corwin-Schultz) best tracks Kalshi's actual quoted and effective spread at 15-minute and hourly frequency?
7. Does the Easley et al. feature set predict SOL volatility changes at 1-hour and 4-hour look-aheads, on perp data, out of sample after 2023? Do gradient-boosted or sequence models add anything over the random forest?
8. What is SOL's hour-of-day and minute-of-hour liquidity profile on Kalshi versus Binance? Are there windows when Kalshi is thin while offshore venues are active, and does Kalshi lag in those windows?
9. Do Kalshi's 8-hour funding times produce the volatility and volume bursts seen at 00, 08 and 16 UTC on offshore venues?
10. Does SOL show round-number stop clustering, and is there continuation for 15 minutes to 2 hours after a clean cross, net of costs?
11. Does active Hyperliquid TWAP notional in SOL predict returns on other venues over the TWAP's remaining life?
12. In past stress episodes, how far and for how long did depth fall on each venue, and did a depth-and-spread circuit breaker trigger early enough to matter?

## Reading order

1. [bouchaud-2008](notes/bouchaud-2008-markets-slowly-digest-supply-demand.md): the framework for everything else on impact.
2. [toth-2011](notes/toth-2011-anomalous-impact-critical-liquidity.md): the square-root law and why liquidity vanishes near the price.
3. [donier-2015](notes/donier-2015-million-metaorder-bitcoin-impact.md): the law on Bitcoin, and the decay of uninformed impact.
4. [barone-2026](notes/barone-2026-hyperliquid-market-impact-adverse-selection.md): the same questions on crypto perpetuals, with results that deviate.
5. [maitrier-2025](notes/maitrier-2025-double-square-root-law-impact.md): the time decay of impact at the trade level.
6. [almgren-2005](notes/almgren-2005-direct-estimation-equity-market-impact.md): a practical permanent-plus-temporary cost model.
7. [brauneis-2021](notes/brauneis-2021-measure-liquidity-cryptocurrency-markets.md): which liquidity proxies work in crypto.
8. [ardia-2024](notes/ardia-2024-efficient-bid-ask-spread-ohlc.md): the spread estimator to use on a thin venue.
9. [abdi-2017](notes/abdi-2017-bid-ask-spread-close-high-low.md): the simpler estimator behind it.
10. [amihud-2002](notes/amihud-2002-illiquidity-stock-returns.md): the classic ratio and its limits.
11. [hansen-2021](notes/hansen-2021-periodicity-crypto-volatility-liquidity.md): liquidity around the clock.
12. [easley-2024](notes/easley-2024-microstructure-dynamics-crypto-markets.md): liquidity measures as machine-learning features for volatility, with SOL in the sample.
13. [osler-2002](notes/osler-2002-stop-loss-orders-price-cascades.md): stop clusters and cascades.
14. [kaiko-2023](notes/kaiko-2023-crypto-liquidity-concentration-report.md): depth metrics and venue concentration.
15. [fticonsulting-2025](notes/fticonsulting-2025-crypto-crash-leverage-liquidity.md): what a liquidity crisis looks like, read with caution.
