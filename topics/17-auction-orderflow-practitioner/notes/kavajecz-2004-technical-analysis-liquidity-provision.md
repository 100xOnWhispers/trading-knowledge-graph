---
title: "Technical Analysis and Liquidity Provision"
authors: "Kavajecz, Kenneth A.; Odders-White, Elizabeth R."
year: 2004
venue: "Review of Financial Studies, 17(4), pp. 1043-1071"
url: "https://academic.oup.com/rfs/article-lookup/doi/10.1093/rfs/hhg057"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "equities"
horizon: "n/a"
tags: "support-resistance, limit-order-book, depth, liquidity-provision, moving-averages, technical-analysis"
---

## Key insight
According to the abstract, support and resistance levels coincide with peaks in depth on the limit order book, and moving-average forecasts carry information about where depth sits on the book. The authors argue that technical rules work, to the extent they do, because they locate liquidity that is already resting in the book. This reframes chart levels as a noisy proxy for something a bot can observe directly.

## Method
Only the abstract and the publisher landing page were read. They state that the paper relates technical-analysis signals (support and resistance levels, moving averages) to the state of the limit order book. The construction of the levels, the regression design and the controls were not visible and are not reported here.

## Data and sample
Not confirmed from the pages read. The abstract refers to "the limit order book" without naming venue, period or instruments.

## Reported results
From the abstract only:
- Support and resistance levels coincide with peaks in depth on the limit order book.
- Moving-average forecasts reveal information about the relative position of depth on the book.
- These relations arise because technical rules locate depth already on the book.

No magnitudes, significance levels or sample sizes were visible.

## Signal construction
Not a signal in itself; it justifies replacing chart-derived levels with measured ones. For crypto, where full depth is public, the direct construction is: aggregate resting bid and ask size by price bucket across the main venues (Binance, Bybit, OKX, Hyperliquid), find local maxima of depth within a few percent of mid, and use distance to the nearest large depth peak on each side, the size of that peak relative to recent traded volume, and its persistence (how long it has rested) as features. Chart levels then serve only as a prior for where depth is likely to appear or reappear after being pulled.

## Relevance to SOL perpetuals at minutes to hours
The paper supports the practitioner intuition behind volume-profile nodes, order blocks and "liquidity pools": levels matter when orders rest there. In crypto a bot does not need to guess; depth is visible, although it can be withdrawn or spoofed in milliseconds, which was much less true of a 1990s exchange book. The useful test on SOL is whether chart-defined levels add anything once visible depth and recent trade flow are in the feature set. The formal treatment of book imbalance belongs to topics 07 and 08; the point for this topic is that practitioner levels should be benchmarked against the book itself.

## Caveats
Abstract-only access, so every detail above the abstract level is unconfirmed. Equity market evidence from a period when displayed depth was more stable than in present-day crypto books. Coincidence of levels with depth does not establish that trading the levels is profitable. The RePEc record lists only the first author; the second author was confirmed on the publisher page.
