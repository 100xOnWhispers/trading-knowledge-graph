---
title: "Aggregate illiquidity and crypto option returns"
authors: "Atanasova, Christina; Miao, Terrel; Segarra, Ignacio; Willeboordse, Frederick"
year: 2025
venue: "Finance Research Letters 85(PC)"
url: "https://ideas.repec.org/a/eee/finlet/v85y2025ipcs1544612325012619.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "hours"
tags: "dealer-gamma, gamma-inventory, deribit, market-makers, option-spreads, momentum-amplification, hedging-flow"
---

## Key insight
The only peer-reviewed study found in this session that measures dealer gamma in bitcoin options from signed trade and quote data. Its abstract states that when aggregate market-maker gamma inventory is negative, market makers "trade in the same direction as BTC price momentum, amplifying price pressure and increasing trading costs". This is the crypto counterpart of the equity-index result in Baltussen and co-authors, which is covered in topic 11.

## Method
From the abstract only: the authors build an aggregate gamma inventory (AGI) measure for market makers from high-frequency Deribit trades and quotes, relate it to option effective spreads, and estimate a dynamic factor model of bitcoin option returns in which illiquidity loads on the first latent factor. How trades are assigned to market makers, the exact gamma aggregation and the control variables were not read.

## Data and sample
Deribit bitcoin options, high-frequency trade and quote data, January 2021 to December 2024.

## Reported results
Abstract only:
- With negative AGI, market makers trade in the direction of bitcoin price momentum.
- Option spreads widen as AGI becomes more negative.
- "A one-standard-deviation decrease in AGI is associated with a 0.12% (0.19%) increase in effective spreads for out-of-the-money calls (puts)."
- Illiquidity loads significantly on the first latent factor priced in bitcoin option returns.

The abstract gives no number for the effect on the bitcoin price itself, on spot or perpetual volatility, or on return autocorrelation.

## Signal construction
A bot would need its own inventory estimate:
1. Sign every Deribit option trade by aggressor (the trade feed gives a direction; block trades need care).
2. Treat the passive side as the market maker and accumulate signed position per instrument, removing expired contracts.
3. Multiply by each option's gamma at the current index price and sum: `AGI_t = sum_i position_i * gamma_i * S_t^2 * 0.01`, giving the dollar delta to be traded per 1% move. The scaling is this note's convention; the paper's normalisation was not read.
4. Feature: sign and size of AGI relative to perpetual and spot volume. Hypothesis from the abstract: negative AGI raises short-horizon return continuation and volatility; positive AGI damps both.

Vendors publish a similar series ([amberdata-2026-gamma-exposure-gex-documentation](amberdata-2026-gamma-exposure-gex-documentation.md)).

## Relevance to SOL perpetuals at minutes to hours
Relevant through bitcoin: if dealer hedging amplifies BTC moves when gamma is negative, the amplification reaches SOL through the BTC lead. SOL's own dealer gamma is too small to matter by comparison ([deribit-2026-option-book-summary-sol-liquidity](deribit-2026-option-book-summary-sol-liquidity.md)). The useful test is whether the BTC intraday momentum and reversal features from topic 13 change sign or strength with the sign of AGI.

## Caveats
Abstract-only note; the full text is behind a publisher wall and the working-paper copy is on a site that blocks automated access. The headline numbers concern option spreads, not underlying returns. Inventory built from signed trades drifts: it misses positions opened off-exchange and assumes market makers never take liquidity. Deribit is one venue; ETF options and CME options held by the same dealers are not seen.
