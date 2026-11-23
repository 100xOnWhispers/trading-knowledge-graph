# Open interest, leverage and liquidation cascades: synthesis

Scope: open interest as a signal, leverage cycles, liquidation and auto-deleveraging mechanics, forced-flow price impact, liquidation maps, and the October 2025 deleveraging as a case study. Funding rates (topic 03) and long/short ratio sentiment (topic 18) are covered elsewhere. Nineteen source notes were written; all were opened on 2026-11-22.

## What the literature agrees on

1. **Leverage plus forced selling produces fat tails and sudden liquidity loss.** The theory is settled. [Brunnermeier and Pedersen](notes/brunnermeier-2009-market-liquidity-funding-liquidity.md) show that funding constraints and market liquidity reinforce each other through loss and margin spirals, with a non-linear effect when capital is already scarce. [Thurner, Farmer and Geanakoplos](notes/thurner-2010-leverage-fat-tails-clustered-volatility.md) show a leverage cap alone generates heavy tails and volatility clustering, and that leverage accumulates in calm periods.

2. **Liquidations in crypto perps are large, routine and skewed to the long side.** On BitMEX in 2020 about 3.5% of open interest was liquidated long and 1.9% short on an average day, with liquidated traders at roughly 60x ([Cheng et al.](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md)). Long liquidations dominate regardless of instrument, size or trend, and small positions contribute disproportionately ([Soska et al.](notes/soska-2021-cryptocurrency-derivatives-bitmex-case-study.md)).

3. **Inside a cascade the signature is in liquidity, not in price memory.** Price impact rises several-fold (1.2 to 3.5 times on Binance, 3.2 to 9.1 times on Hyperliquid), open interest clears by a quarter to two thirds, and cross-asset correlation jumps ([Garcia Seuma, branching](notes/garcia-seuma-2026-branching-ratio-liquidation-cascade.md)). On Hyperliquid on 10 October 2025 the median inside spread across five majors rose more than 25-fold in the peak hour and was back near 1 bp two hours later, while depth stayed impaired for weeks ([Lim](notes/lim-2026-liquidity-recovery-hyperliquid-liquidation-cascade.md)).

4. **Cascades are fast and front-loaded.** In October 2025, 88% of post-onset forced selling on Hyperliquid landed within 30 minutes ([Garcia Seuma, branching](notes/garcia-seuma-2026-branching-ratio-liquidation-cascade.md)); the main ADL waves ran within about five minutes, with long-tail coins first and ETH, SOL, BTC and XRP about a minute later ([Campbell et al.](notes/campbell-2026-risk-based-auto-deleveraging.md)).

5. **Venue rules shape the cascade.** Partial liquidation clips, backstop vaults and ADL queues are published and differ by venue ([Hyperliquid docs](notes/hyperliquid-2026-liquidations-auto-deleveraging-docs.md), [Kalshi docs](notes/kalshi-2026-perps-api-margin-liquidation-docs.md)). The queue-style ADL used by most venues is neither fair nor risk-optimal ([Chitra](notes/chitra-2025-autodeleveraging-impossibilities-optimization.md), [Campbell et al.](notes/campbell-2026-risk-based-auto-deleveraging.md)), and it can close a correctly positioned trade early.

6. **The raw data are unreliable.** Exchange open interest fails a basic consistency test against volume at one-minute resolution on several venues ([Giagkiozis and Said](notes/giagkiozis-2024-reconciling-open-interest-traded-volume.md)). Binance's liquidation stream pushes at most one order per symbol per second ([Binance docs](notes/binance-2026-liquidation-order-stream-docs.md)), so liquidation totals are lower bounds.

## Where it disagrees or is weak

- **Does leverage build-up predict a cascade?** The popular view says high open interest warns of a flush. The only multi-event tests found say otherwise. [Garcia Seuma, early warning](notes/garcia-seuma-2026-early-warning-liquidation-cascades.md) finds no event-invariant early-warning variable across seven BTC cascades; the October 2025 pattern in open interest inverted out of sample on August 2024. The companion paper finds that no scalar pre-state (leverage stock, book fragility or their product) grades severity. Both are single-author preprints with seven events, so this is a serious challenge, not a settled result.
- **Chain reaction or single sweep?** Theory and practitioner language describe self-reinforcing feedback. The measured within-venue branching ratio in October 2025 was 0.1 to 0.2, far below 1, partly because the backstop absorbed 63% of forced flow off-book. Cross-venue amplification was not measured, so the two views are not yet reconciled.
- **Sign of the open interest signal.** [Hong and Yogo](notes/hong-2012-futures-open-interest-asset-prices.md) find rising open interest predicts higher returns in commodities at monthly horizon (0.73% per month per standard deviation). Crypto practice reads rising open interest as crowding. No crypto study with out-of-sample tests at intraday horizon was found for either sign.
- **Liquidation heatmaps.** The only source opened ([Glassnode](notes/manrique-2025-liquidation-heatmaps-market-bias.md)) offers a visual comparison with no statistics. Whether clusters attract price, or only scale the move once reached, is untested. Maps for centralized venues rest on assumed leverage and entry prices.
- **Size of the October 2025 ADL overshoot.** Chitra's estimate was revised between versions (USD 45 to 52 million in PnL terms in v3); Campbell et al. use a different risk metric. Headline liquidation totals (USD 19 billion) come from incomplete feeds ([FTI Consulting](notes/fticonsulting-2025-crypto-crash-leverage-liquidity.md)).
- **Machine learning, reinforcement learning and evolutionary methods.** Coverage is thin. No paper was found that uses open interest or liquidation data as model features with a proper out-of-sample test. The two ML sources bear on cascade survival, not on leverage signals: a boosted-tree strategy that profited as a taker and failed as a maker on 10 October 2025 ([Bieganowski and Slepaczuk](notes/bieganowski-2026-explainable-patterns-crypto-microstructure.md)), and an RL ensemble with out-of-distribution gating for 5x leveraged futures ([Qin et al., FineFT](notes/qin-2025-fineft-ensemble-rl-futures-trading.md)). No evolutionary-algorithm work in this scope was located.
- **Almost everything is BTC.** SOL appears only in the Hyperliquid liquidity and ADL studies.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Open interest data-quality filter: `max(abs(dOI) - volume, 0)` per venue and interval | Tick or 1-minute OI and trades per venue | minutes | B | [giagkiozis-2024](notes/giagkiozis-2024-reconciling-open-interest-traded-volume.md) |
| Inferred forced flow: OI drop coinciding with one-sided taker volume | 1 to 5 minute OI, signed taker volume | minutes | C | [binance-2026](notes/binance-2026-liquidation-order-stream-docs.md), [garcia-seuma-2026 early warning](notes/garcia-seuma-2026-early-warning-liquidation-cascades.md) |
| Taker-flow variance compression (falling variance of detrended log taker buy/sell ratio) | 5-minute taker buy/sell ratio, 1 to 3 day trend | hours | C | [garcia-seuma-2026 early warning](notes/garcia-seuma-2026-early-warning-liquidation-cascades.md) |
| Liquidity-stress gauge: quoted impact spread relative to trailing baseline | Hyperliquid impact prices per asset | minutes | C | [garcia-seuma-2026 branching](notes/garcia-seuma-2026-branching-ratio-liquidation-cascade.md) |
| Spread and depth ratios to baseline (carry both; depth recovers slower) | L2 snapshots | minutes | B | [lim-2026](notes/lim-2026-liquidity-recovery-hyperliquid-liquidation-cascade.md) |
| Cross-asset correlation jump as regime flag | 5-minute returns for 20 to 30 perps | minutes | C | [garcia-seuma-2026 branching](notes/garcia-seuma-2026-branching-ratio-liquidation-cascade.md) |
| Exact liquidation map from on-chain positions | Hyperliquid positions, margin, published liquidation formula | minutes to hours | D as a predictor | [hyperliquid-2026](notes/hyperliquid-2026-liquidations-auto-deleveraging-docs.md), [manrique-2025](notes/manrique-2025-liquidation-heatmaps-market-bias.md) |
| Lending liquidation sensitivity curve | On-chain SOL-collateral loans and thresholds | hours | B as a measure, untested as a predictor | [qin-2021](notes/qin-2021-empirical-study-defi-liquidations.md) |
| Liquidation intensity and turnover: liquidations over OI, volume over OI | Daily or intraday liquidations, OI, volume | hours to daily | B, descriptive | [cheng-2021](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md), [soska-2021](notes/soska-2021-cryptocurrency-derivatives-bitmex-case-study.md) |
| Open interest growth as conditioning variable | Aggregated dollar OI growth, standardized | hours to multi-day | B in commodities, untested in crypto | [hong-2012](notes/hong-2012-futures-open-interest-asset-prices.md) |
| Long-tail-first sequencing (stress in thin perps leads majors) | ADL or liquidation activity in small-cap perps | seconds to minutes | C, one event | [campbell-2026](notes/campbell-2026-risk-based-auto-deleveraging.md) |
| Collateral dislocation monitor | Venue-local prices of margin collateral against other venues | minutes | D | [fticonsulting-2025](notes/fticonsulting-2025-crypto-crash-leverage-liquidity.md) |
| Out-of-distribution gate (go flat when state is unfamiliar) | Model feature vector, reconstruction loss | minutes | B | [qin-2025](notes/qin-2025-fineft-ensemble-rl-futures-trading.md), [bieganowski-2026](notes/bieganowski-2026-explainable-patterns-crypto-microstructure.md) |
| Tail-based leverage sizing (GEV margin for a target liquidation probability) | 5-minute to daily return extremes | hours | B | [cheng-2021](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md) |
| ADL exposure control (limit leverage and unrealized gain per position) | Venue ADL ranking rule, own positions | n/a | B | [chitra-2025](notes/chitra-2025-autodeleveraging-impossibilities-optimization.md), [campbell-2026](notes/campbell-2026-risk-based-auto-deleveraging.md) |
| Kalshi venue state: OI, liquidation mark versus reference price, leverage estimate | Kalshi perps API | minutes | B as documentation | [kalshi-2026](notes/kalshi-2026-perps-api-margin-liquidation-docs.md) |

## Open questions worth testing on SOL perps

1. Replicate the early-warning panel on SOL using Binance's public 5-minute metrics. Does taker-flow variance compression hold for SOL, and does any open interest feature survive a placebo test?
2. Conditional on a shock (for example a 1% move in 5 minutes), does the subsequent SOL move scale with open interest relative to book depth? This tests the non-linearity that theory predicts without asking open interest to time the event.
3. Does the SOL liquidation map on Hyperliquid predict the probability of reaching a cluster, or only the size and speed of the move once price enters it? Compare against a null map built from randomized positions.
4. Does the Hyperliquid map carry information about forced flow on Binance, Bybit and OKX, where positions are not visible?
5. How large is the Binance liquidation undercount for SOL? Compare stream totals with open interest drops and taker volume in known events.
6. After forced-flow bursts, does SOL mean-revert or continue over 5 minutes to 4 hours, net of the spreads documented for October 2025? No source in this topic answers this.
7. Does stress in long-tail perps lead SOL by tens of seconds in events other than October 2025?
8. How does Kalshi SOL open interest, its liquidation mark and its book depth respond when offshore venues cascade? Does Kalshi lag enough to trade, and is its book deep enough to exit?
9. Does adding open interest, liquidation and impact features to an ML model improve out-of-sample direction or volatility forecasts at 5 to 60 minutes, and does an out-of-distribution gate trained on them fire before or only during a cascade?
10. What loss-allocation rule applies on Kalshi if liquidations fail? The API documentation does not say.

## Reading order

1. [brunnermeier-2009](notes/brunnermeier-2009-market-liquidity-funding-liquidity.md): the mechanism.
2. [thurner-2010](notes/thurner-2010-leverage-fat-tails-clustered-volatility.md): leverage cycles and why calm periods are dangerous.
3. [hyperliquid-2026](notes/hyperliquid-2026-liquidations-auto-deleveraging-docs.md) and [kalshi-2026](notes/kalshi-2026-perps-api-margin-liquidation-docs.md): how liquidation actually works on a transparent venue and on the reference venue.
4. [soska-2021](notes/soska-2021-cryptocurrency-derivatives-bitmex-case-study.md) and [cheng-2021](notes/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.md): baseline facts on liquidations and leverage.
5. [giagkiozis-2024](notes/giagkiozis-2024-reconciling-open-interest-traded-volume.md) and [binance-2026](notes/binance-2026-liquidation-order-stream-docs.md): what is wrong with the data before any feature is built.
6. [garcia-seuma-2026 early warning](notes/garcia-seuma-2026-early-warning-liquidation-cascades.md) then [garcia-seuma-2026 branching](notes/garcia-seuma-2026-branching-ratio-liquidation-cascade.md): the evidence against simple leverage-based prediction.
7. [lim-2026](notes/lim-2026-liquidity-recovery-hyperliquid-liquidation-cascade.md), [chitra-2025](notes/chitra-2025-autodeleveraging-impossibilities-optimization.md), [campbell-2026](notes/campbell-2026-risk-based-auto-deleveraging.md), [fticonsulting-2025](notes/fticonsulting-2025-crypto-crash-leverage-liquidity.md): the October 2025 case study from four angles.
8. [manrique-2025](notes/manrique-2025-liquidation-heatmaps-market-bias.md) and [qin-2021](notes/qin-2021-empirical-study-defi-liquidations.md): liquidation maps, estimated and exact.
9. [bieganowski-2026](notes/bieganowski-2026-explainable-patterns-crypto-microstructure.md) and [qin-2025](notes/qin-2025-fineft-ensemble-rl-futures-trading.md): how ML and RL strategies behave in and around cascades.
10. [hong-2012](notes/hong-2012-futures-open-interest-asset-prices.md): open interest as a predictor in traditional futures, for contrast.

Neighboring works opened but not noted here: Gornall, Rinaldi and Xiao, "Perpetual Futures and Basis Risk" (May 2025 draft), which reports that liquidations shifted from quarterly futures to perps and that quarterly futures fall 8 to 10% more than spot in large moves against about 3% for perps (belongs with topic 03); Chitra et al., "Autodeleveraging as Online Learning" (arXiv 2602.15182), summarized inside the Chitra note; and BIS Working Paper 1171, "DeFi leverage" (Heimbach and Huang, 2024), read at abstract level only, which finds wallet leverage of 1.4 to 1.9 on DeFi lending platforms and that higher leverage raises the share of debt near liquidation.
