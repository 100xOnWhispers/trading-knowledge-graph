---
title: "The 'double' square-root law: Evidence for the mechanical origin of market impact using Tokyo Stock Exchange data"
authors: "Maitrier, Guillaume; Loeper, Gregoire; Kanazawa, Kiyoshi; Bouchaud, Jean-Philippe"
year: 2025
venue: "arXiv:2502.16246v2 (q-fin.TR)"
url: "https://arxiv.org/pdf/2502.16246"
pdf: "sources/09-liquidity-price-impact/maitrier-2025-double-square-root-law-impact.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "equities"
horizon: "minutes"
tags: "square-root-law, propagator, transient-impact, metaorder, impact-decay, mechanical-impact"
---

## Key insight
With trader-identified data for a whole exchange, the authors show that the square-root law already holds for single child orders once the market has had time to digest them. Metaorder impact is the sum of two square-root effects: each child order's impact grows as the square root of its size and then decays as the inverse square root of time. Synthetic metaorders built by scrambling trader identities have the same impact as real ones, so impact looks mechanical and not information-driven.

## Method
Metaorders are sequences of consecutive same-sign market orders from one trader ID. The authors measure the price change between just before child order 1 and just before child order i+1, conditional on child size q and rank i, and fit a non-linear propagator in which the impact of child order j seen at a later time is proportional to sqrt(q_j) divided by the square root of elapsed time (with a short-time offset). They then build synthetic metaorders from consecutive market orders regardless of who sent them, and compare impact curves. They also classify traders as fast or slow by holding period and study how liquidity providers refill.

## Data and sample
Tokyo Stock Exchange order data from the Japan Exchange Group, all stocks, 2012 to 2018, with virtual server IDs aggregated into trading desks. Provided for academic use only.

## Reported results
- The impact of the first child order scales as the square root of its size relative to daily volume.
- Cumulative impact after i child orders grows as a power law with a fitted propagator decay exponent beta = 0.48, very close to one half; the fit is very good up to about 50 child orders, after which impact saturates.
- The typical number of child orders is around 10 for metaorders below about 1% of daily volume.
- Synthetic metaorders follow the same square-root law as real ones.
- "Fast" traders (holding period under a day) account for 50% to 60% of executed market orders, and nearly half of volume is executed against fast traders. The authors say this is too low for the standard latent-order-book interpretation.
- After a buy (sell) market order, liquidity providers raise (lower) their offered price, by an amount that decreases as a power law in the number of trades already executed.

## Signal construction
A non-linear propagator feature for expected short-horizon price pressure:

P_t = sum over recent aggressive trades j of sign_j * sqrt(q_j / V_daily) * sigma_daily / sqrt(t - t_j + s0)

computed over all public trades on the reference venue, with s0 a short offset to be fitted. Because scrambled flow behaves like real flow, the bot does not need to know who is trading. The gap between P_t and the realized price move is a candidate mean-reversion or continuation feature. Update on every trade or every second.

## Relevance to SOL perpetuals at minutes to hours
The inverse-square-root decay gives a concrete, testable half-life structure for how quickly a burst of taker flow on Binance or Hyperliquid should fade, which is the core question for a minutes-to-hours directional bot. It also says anonymous public trade data are enough to model impact. The exponents come from Japanese equities with their tick sizes and lot rules; Barone and Lillo (2026) find lower exponents on Hyperliquid perps, so the kernel must be re-fitted on SOL.

## Caveats
Preprint. Equities only, one exchange, 2012 to 2018. Metaorder identification still relies on a same-sign consecutive-order rule. A pure inverse-square-root propagator would by itself make prices strongly mean-reverting; the authors discuss how this is reconciled with diffusive prices, and that argument was not read in full. No trading test is reported.
