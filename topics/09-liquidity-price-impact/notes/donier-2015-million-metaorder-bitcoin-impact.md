---
title: "A million metaorder analysis of market impact on the Bitcoin"
authors: "Donier, J.; Bonart, J."
year: 2015
venue: "Market Microstructure and Liquidity 1(2), 1550008 (read as arXiv:1412.4503v3)"
url: "https://arxiv.org/pdf/1412.4503"
pdf: "sources/09-liquidity-price-impact/donier-2015-million-metaorder-bitcoin-impact.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "minutes"
tags: "square-root-law, metaorder, bitcoin, price-impact, impact-decay, permanent-impact"
---

## Key insight
The square-root impact law holds on Bitcoin over four decades of order size, in a market that had almost no professional market makers or statistical arbitrage. It holds along the whole execution path, not only at the end. Metaorders that are uncorrelated with the rest of the order flow leave almost no permanent impact, which points to a mechanical origin of impact.

## Method
The dataset identifies each trader, so metaorders can be reconstructed exactly instead of inferred. The authors measure peak impact, average execution price and post-execution impact as functions of size Q and execution rate. They normalize by daily volatility sigma_D and daily volume V_D:

I(Q) = Y * sigma_D * sqrt(Q / V_D)

and study the distribution of the residual ratio Y. To separate mechanical from informational impact they select metaorders that are uncorrelated with the market's local direction.

## Data and sample
All trades on the MtGox BTC/USD exchange from August 2011 to November 2013, about 13 to 14 million trades with trader identifiers, giving more than 1 million metaorders. Fees were 0.6% per transaction for most users and the average spread was about 0.6%.

## Reported results
- The square-root law is confirmed and holds trajectory-wise, down to the smallest scales.
- The impact prefactor fluctuates strongly over time, and the ratio sigma_D / sqrt(V_D) explains those fluctuations well.
- The residual Y-ratio is close to Gaussian with mean 0.9 and standard deviation 0.35.
- The market reacts to total order flow, not to individual metaorders; impacts of simultaneous metaorders do not add linearly. Typically about 5 metaorders are active at once.
- For isolated metaorders the permanent impact is close to zero, far below the 2/3 of peak impact predicted by equilibrium models.
- Metaorder signs are autocorrelated; execution proceeds at a roughly constant average rate.

## Signal construction
1. Impact unit: u_t = sigma_24h / sqrt(V_24h), updated every few minutes from the reference venue. Expected move from net aggressive flow Q over a window is about 0.9 * u_t * sqrt(|Q|).
2. Fragility indicator: track u_t against its own history. The authors note that this prefactor is a proxy for market stability, with a companion paper applying it to the 2013 Bitcoin crash.
3. Fade rule to test: after a burst of one-sided flow that is not confirmed by flow on other venues, expect reversion of a large part of the move, because uncorrelated flow has little permanent impact.

## Relevance to SOL perpetuals at minutes to hours
This is the closest classic evidence for crypto. It shows the impact law does not depend on a mature market-making ecosystem, which matters for a young venue such as Kalshi. The mean Y near 0.9 is a reasonable starting value. What needs re-testing: MtGox was a spot market with 60 basis point fees and no leverage; SOL perps have liquidations, cross-venue arbitrage and much tighter spreads. On a perp, forced liquidation flow is informationless by construction, so the "uncorrelated flow reverts" result suggests a testable post-liquidation reversal.

## Caveats
One exchange, one asset, 2011 to 2013. MtGox failed in 2014 (background knowledge, not from the paper), so the integrity of some of its recorded flow is open to question. The identification of uninformed flow is by selection, and the authors say the slow-execution measurements are too noisy for a proper fit.
