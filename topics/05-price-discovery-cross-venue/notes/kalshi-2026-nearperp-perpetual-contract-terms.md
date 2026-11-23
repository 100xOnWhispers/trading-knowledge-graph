---
title: "KalshiEX LLC: CFTC Regulation 40.2(a) Notification Regarding the Initial Listing of the NEARPERP Futures Contract"
authors: "KalshiEX LLC"
year: 2026
venue: "CFTC product self-certification filing (June 23, 2026)"
url: "https://www.cftc.gov/filings/ptc/ptc0623267006.pdf"
pdf: "sources/05-price-discovery-cross-venue/kalshi-2026-nearperp-perpetual-contract-terms.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "hours"
tags: "kalshi, perpetual, index-price, funding-rate, premium-index, settlement-price, cf-benchmarks, contract-specification"
---

## Key insight
Kalshi's crypto perpetuals are tethered to a third-party spot index from CF Benchmarks, not to offshore perps or to Kalshi's own trades. Funding is computed from a per-second premium of Kalshi's impact bid/ask over that index, back-weighted toward the end of each 8-hour interval, with a 0.01% deadband and a 2% cap. The structure defines exactly what "fair value" the venue pulls toward and when.

## Method
Primary-source contract terms (Appendix A of the filing). I read the NEARPERP filing in full for the terms and the parallel BNBPERP filing (August 27, 2026, https://www.cftc.gov/filings/ptc/ptc08272622306.pdf) for the source-agency appendix; both share the same template. Formulas:

- Underlying Price Index UPI_t: last recorded value of the CME CF NEAR Protocol-Dollar Real Time Index (BNB uses the CF BNB-Dollar Spot Rate).
- Premium Index each second: PI(t) = (max(0, IBP_t - UPI_t) - max(0, UPI_t - IAP_t)) / UPI_t, where IBP and IAP are the average fill prices of a $1,000 "impact notional" market sell and buy; an undefined side counts as zero; t is drawn uniformly at random within each second.
- Funding Rate: WAPI = sum(i * PI_i) / sum(i) over the n one-second samples (28,800 in a standard interval), a linearly time-weighted average and explicitly not a TWAP; set to zero if |WAPI| < 0.01%; clamped at +/-2%.
- Funding intervals end at 12:00 AM, 8:00 AM and 4:00 PM Eastern Time; the payment uses the contract's 60-second VWAP before the interval end.
- Settlement Price (for variation margin, at 12:00 PM and 4:00 PM ET): tier 1 outlier-filtered 60-second trade VWAP; tier 2 mean of sampled two-sided midpoints; tier 3 prior settlement plus the net change in the index.

## Data and sample
Not empirical. Contract specification for a Kalshi digital-asset perpetual: 24/7 trading, cash settled, centrally cleared by Kalshi Klear, risk-based margin, position accountability level of $5,000,000.

## Reported results
- The filing states perpetuals are "a significant locus of price discovery in digital-asset markets".
- The BNBPERP filing describes the CF index as built from consolidated order books of constituent exchanges (Coinbase and Kraken for BNB), not from trades, and cites Kaiko for Bitcoin perpetuals being 68% of Bitcoin trading volume in 2025.
- No statistics on Kalshi's own basis, spreads or volume appear in the filings.

## Signal construction
Three live computations follow from the terms. (1) Replicate the premium index: (Kalshi impact bid or ask at $1,000 notional minus the CF real-time index) / index, sampled each second. (2) Running funding estimate: linearly weighted average of the premium samples so far in the interval; because weights rise linearly, the last hours dominate, so the predicted funding becomes informative late in the interval. (3) Index-versus-offshore gap: CF real-time index (US-regulated spot venues) minus Binance perp mark; Kalshi is pulled toward the former while price discovery happens at the latter.

## Relevance to SOL perpetuals at minutes to hours
The SOL perp filing itself was not retrieved, so its index is not confirmed; by the template it should reference the CME CF Solana-Dollar Real Time Index. If so, Kalshi's anchor is a blend of Coinbase, Kraken and similar spot books. When offshore perps trade at a premium or discount to US spot, Kalshi's fair value sits with US spot plus expected funding. The deadband means small persistent premia cost nothing to hold.

## Caveats
Terms are from the NEAR and BNB filings, not SOL; leverage limits and fees are not in these documents. The exchange can amend the funding methodology prospectively. A mark-price formula for liquidations is not given beyond "risk-based margin methodology". Kalshi's own web pages returned rate-limit errors in this session.
