---
title: "KalshiEX LLC - CFTC Regulation 40.2(a) Notification Regarding the Initial Listing of the SOLPERP Futures Contract"
authors: "KalshiEX LLC (signed Sottile, Xavier)"
year: 2026
venue: "CFTC product filing (self-certification), filed June 2, 2026"
url: "https://www.cftc.gov/filings/ptc/ptc0602265099.pdf"
pdf: "sources/06-kalshi-venue/kalshiex-2026-solperp-contract-terms-cftc-filing.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "kalshi, sol-perp, contract-specification, funding-formula, premium-index, settlement-price, cf-benchmarks"
---

## Key insight
This is the binding legal specification of the reference instrument. It gives the exact funding formula: a per-second impact-price premium against the CME CF Solana-Dollar Real Time Index, combined with linearly increasing weights (not a TWAP), then a 0.01% deadband and a 2% clamp. It also shows the contract was self-certified, not individually approved, three days after the CFTC approved the BTC perp.

## Method
Rule text in Appendix A of a 23-page filing. Formulas as written:

- Underlying Price Index `UPI_t`: last recorded value of the CME CF Solana-Dollar Real Time Index (SOLUSD_RTI); Source Agency CF Benchmarks.
- Premium Index, each second: `PI(t) = (max(0, IBP_t - UPI_t) - max(0, UPI_t - IAP_t)) / UPI_t`, where IBP and IAP are the average fill prices of a market sell and a market buy of Impact Notional $1,000. An undefined side evaluates to 0. Within each second, `t` is drawn uniformly at random.
- Funding: `WAPI = sum(i * PI_i) / (n(n+1)/2)`, i = 1..n, n = 28,800 for a standard interval. The filing states this "is not a time-weighted average price (TWAP)".
- Deadband: `|WAPI| < 0.01%` gives a zero rate. Clamp: `|WAPI| > 2%` is clamped to +/-2%.
- Payment per contract: rate x VWAP of the contract over the 60 seconds before the interval end x Trading Unit; longs pay when positive.
- Settlement Price tiers: (1) VWAP of trades in the 60 seconds before settlement, with a median-based outlier filter; (2) mean of best bid/ask midpoints at 60 one-second observation points; (3) prior settlement plus index net change.

## Data and sample
Not empirical. One contract: SOLPERP on KalshiEX, cleared by Kalshi Klear LLC. The filing dated June 2, 2026 replaces one dated June 1, 2026 (also opened); the only substantive change is the Trading Unit.

## Reported results
- Funding intervals end 12:00 AM, 8:00 AM, 4:00 PM ET; the 8:00 AM interval is 7 or 9 hours on daylight-saving change days.
- Settlement Times: 12:00 PM and 4:00 PM ET daily. Funding obligations are computed at interval end and paid at the next Settlement Time.
- Trading Unit: 1,000 SOL (June 2 version); the June 1 version said 0.1 SOL. Minimum unit: 1/10,000 of a contract, i.e. 0.1 SOL. Minimum price increment: $0.001 per SOL.
- Trading hours: 24/7 subject to halts. Position accountability level: $5,000,000 mark-to-market.
- Margin: "risk-based margin methodology"; no leverage number is stated.
- If the funding rate cannot be determined, including for insufficient book liquidity, it is set to zero. In an emergency the exchange may change the maximum funding magnitude and margin.
- Index constituents named: Coinbase, Kraken, Gemini, LMAX Digital, Bitstamp. The index is built from order books, not trades.

## Signal construction
Not a signal by itself, but it lets a bot replicate funding before it is paid. Inputs: live order book (walk $1,000 each side) and SOLUSD_RTI each second. Compute `PI`, accumulate `sum(i*PI_i)` and divide by `n(n+1)/2`. Derived from the weights (my arithmetic, not in the filing): the final hour of an 8-hour interval carries about 23% of the weight, the final two hours about 44%, the second half 75%. The live estimate therefore matters most late in the window.

## Relevance to SOL perpetuals at minutes to hours
Direct. The premium index is zero whenever the index sits inside the $1,000 impact bid/ask, so funding is zero in tight, balanced markets. A reinforcement-learning or supervised cost model should encode the deadband as a discontinuity, not as a linear carry term. The reference index excludes Binance, Bybit, OKX and Hyperliquid, so offshore lead-lag acts through US-accessible spot books.

## Caveats
Written by the exchange for a regulator; Appendices F and G are confidential. Margin, liquidation and fee details are absent. The 1,000 SOL Trading Unit conflicts with the 0.1 SOL "contract" used by the API and with the June 1 filing; they reconcile only through the 1/10,000 minimum unit. Kalshi's help center describes the same funding as a TWAP of 480 one-minute candles, which contradicts this filing.
