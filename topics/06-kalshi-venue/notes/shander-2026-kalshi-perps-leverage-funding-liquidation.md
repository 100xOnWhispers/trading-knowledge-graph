---
title: "Kalshi Perpetual Futures: Leverage, Funding And What Can Liquidate You"
authors: "Shander, Eytan"
year: 2026
venue: "OddsShopper"
url: "https://www.oddsshopper.com/articles/prediction-markets/kalshi-perpetual-futures"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "kalshi, leverage, volume, open-interest, third-party-snapshot, liquidation, retail-explainer"
---

## Key insight
The only independent write-up found that records dated Kalshi perps figures. Its August 2026 snapshots show that maximum leverage differs by asset, by side and by position size, and that venue-wide daily volume was already tens of times open interest. Compared with the API values of November 2026, the leverage numbers have drifted, which shows that Kalshi's leverage caps are recalibrated outputs of a margin model and not fixed tiers.

## Method
A consumer explainer by a betting analyst, dated August 18, 2026. It reports figures the author pulled from Kalshi's market data on two dates and quotes Kalshi's help center. Read through a page-to-text summariser, so the numbers below are as that tool extracted them.

## Data and sample
Kalshi perps market data on August 5 and August 18, 2026. Assets tabulated: Bitcoin, Ethereum, Litecoin, Bitcoin Cash and kSHIB. SOL is not in the extracted tables.

## Reported results
- Headline leverage estimates: Bitcoin 5.9x, Ethereum 4.5x, Litecoin 3.7x, Bitcoin Cash 3.0x, kSHIB 2.0x.
- Long leverage at $1,000 versus $1,000,000 notional: Bitcoin 6.2x and 6.0x; Ethereum 4.7x and 4.5x; Litecoin 3.8x and 2.3x; Bitcoin Cash 4.5x and 2.3x; kSHIB 3.4x and 1.2x. A Bitcoin Cash short at $1,000 was about 3.0x.
- August 18, 2026: about $500 million of 24-hour notional volume and about $14 million of open interest across perps; Bitcoin about 48% and Ethereum about 46% of volume. August 5: about $184 million volume and $13 million open interest.
- 16 perpetual markets listed, 13 active on August 18.
- Funding described as 8-hourly, capped at 2% per window.
- The article states that Coinbase routes US users to perpetuals under CFTC staff no-action relief, citing Letter 26-17.
- A worked liquidation example assumes a maintenance requirement of roughly 6%, which the article labels illustrative.

## Signal construction
Not a signal. Used as a dated cross-check on venue state. The comparison it enables: Bitcoin long leverage at $1,000 was 6.2x in August and 6.90x in the API on November 22, 2026; Ethereum 4.7x then and 4.94x now. A bot should read `long_leverage_estimates` and `short_leverage_estimates` at start-up and before sizing, never hard-code them.

## Relevance to SOL perpetuals at minutes to hours
Two points transfer. Leverage asymmetry by side is systematic: on November 22 the SOL long estimate was 3.59x and the short 3.09x, consistent with the pattern this article found in other assets. That asymmetry caps short exposure more tightly than long exposure for the same collateral, which matters for a symmetric directional strategy. Second, turnover of roughly 14 to 36 times open interest per day venue-wide in August, and about 13 times in November by the API, indicates that most volume is intraday inventory recycling, plausibly by fee-rebated market makers. Volume-based liquidity estimates will overstate what a taker can execute.

## Caveats
A betting-site article with no stated methodology, no SOL figures and a commercial interest in prediction-market traffic. The numbers were not reproduced and reached this note through an automated summariser. The 6% maintenance figure is the author's illustration and conflicts with the scale implied by Kalshi's API, where SOL leverage near 3x implies a margin rate near 30%. The no-action-letter claim about Coinbase was not verified against the CFTC letter. The article's count of 16 markets is far below the 143 the API listed in November, showing how quickly the venue has changed.
