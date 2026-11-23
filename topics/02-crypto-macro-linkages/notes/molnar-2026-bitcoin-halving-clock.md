---
title: "Bitcoin Runs on a Clock: Why Every Price Indicator Dies and the Halving Clock Doesn't"
authors: "Molnar, Josh"
year: 2026
venue: "arXiv 2607.26188 (v1, July 2026; paper dated June 2026)"
url: "https://arxiv.org/pdf/2607.26188"
pdf: "sources/02-crypto-macro-linkages/molnar-2026-bitcoin-halving-clock.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "multi-day"
tags: "halving-cycle, m2-liquidity, yield-curve, cycle-timing, small-sample, indicator-decay, power-law"
---

## Key insight
The strongest recent statement of the halving-cycle claim, and unusually candid about its limits. The three mature Bitcoin cycle tops fell 525, 546 and 534 days after their halvings, while popular price and on-chain oscillators lost their calibration across cycles. For this topic the most useful part is the negative result on macro liquidity: US M2 growth and the yield-curve spread show no stable sign or lead against forward Bitcoin returns across cycles, and the folklore "M2 leads Bitcoin by about 10 weeks" appears to be a one-era artifact.

## Method
Daily data across four halving epochs (E1 to E4). Cycle tops and bottoms are dated retrospectively by a fixed rule: an all-time high followed by a drawdown of at least 45 percent. Evidence for clustering comes from uniform timing nulls and a block-bootstrap null in which resampled return paths are passed through the same rule. Indicator decay is measured with rank information coefficients per epoch. Macro confounders are tested four ways: sign stability of the information coefficient per epoch, lead-lag stability, distance from macro turning points to Bitcoin tops, and a joint regression of forward 180-day returns on halving phase, M2 growth and the 10-year minus 2-year spread (Newey-West, lag 180). A rotation null is used to check the true size of HAC inference with persistent regressors. A power law in days since genesis is fit on an expanding window.

## Data and sample
Bitstamp BTC/USD daily, 18 August 2011 to 10 June 2026; Coin Metrics community series as cross-check and for on-chain measures; Ethereum from August 2015. FRED M2SL and T10Y2Y with publication lags of 28 and 7 days.

## Reported results
- Tops: 525, 546 and 534 days after halving (the immature 2013 top came at 371 days). Bottoms: 406, 364 and 366 days after tops.
- Block-bootstrap null reproduces the top-timing regularity in zero of 10,000 paths (0.10 to 0.25 percent in a variant that lets the null pick among candidate tops), but reproduces the bottom-timing regularity in 31 to 43 percent of paths, so the bottom spacing is largely a property of drawdowns in general.
- M2 year-on-year growth, 180-day information coefficient with forward returns: +0.41, -0.10, -0.83 across E2 to E4. Yield-curve spread: +0.42, -0.35, -0.79.
- Lagged M2 against forward 90-day returns is positive at every lead in E2 (peaking near +0.45 at a 120-day lead) and negative throughout E3 and E4.
- M2-growth peaks miss Bitcoin tops by 67 to 253 days with mixed sign.
- Joint regression t-statistics: phase -2.00, M2 +0.20, spread -0.07.
- HAC inference over-rejects badly at these sample sizes: empirical size 0.17 to 0.33 at nominal 0.05. The author therefore declines to rest claims on per-epoch significance.
- RSI-14's 30-day information coefficient decays from +0.28 to -0.02 across epochs.
- Pre-registered prediction: a cycle bottom between 5 October and 16 November 2026.

## Signal construction
Days since the last halving (or block height modulo 210,000) as a slow phase variable; the paper's simple rule is to be out of Bitcoin from roughly 525 to 900 days after each halving. This is a multi-month regime prior, not a signal at minutes to hours. More useful here is what not to build: a lagged M2 or "global liquidity" lead indicator, which this paper finds unstable in sign across cycles.

## Relevance to SOL perpetuals at minutes to hours
Indirect. At most the halving phase is a low-weight prior on the sign of drift and on drawdown risk over months, for an asset (SOL) that has no halving of its own and has existed for only part of two cycles. The M2 result is relevant when deciding which macro inputs to include: a slow liquidity series with an assumed fixed lead is not supported. The bottom-window prediction ended six days before this note was written (22 November 2026); the outcome was not checked in this session and should be before giving the paper any weight.

## Caveats
Three or four cycles is the whole sample, and the author says so. Turn dates are identified after the fact. The halving and the liquidity cycle are roughly co-periodic and cannot be separated with so few overlaps. US M2 only, not a global aggregate, and monthly data only from 2018. Independent researcher, not peer reviewed, no independent replication found. The paper's own diagnostics show conventional significance tests are unreliable here, which applies equally to its horse race.
