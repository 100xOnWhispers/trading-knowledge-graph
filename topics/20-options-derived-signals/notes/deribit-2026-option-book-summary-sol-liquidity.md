---
title: "Deribit public API: option book summary by currency (snapshot of BTC, ETH and SOL option open interest, 23 November 2026 UTC)"
authors: "Deribit"
year: 2026
venue: "Deribit public API, endpoint public/get_book_summary_by_currency"
url: "https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=USDC&kind=option"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "n/a"
tags: "sol-options, open-interest, liquidity, deribit, bid-ask-spread, data-availability"
---

## Key insight
On the largest crypto options venue, SOL options are about 0.3% of bitcoin options by open interest and by 24-hour notional volume, with quoted spreads roughly twice as wide. SOL's own option surface is too thin to support order-flow, gamma or expiry signals; option-derived inputs for a SOL bot have to come from BTC and ETH, with SOL implied volatility used at most as a slow level.

## Method
One snapshot of the unauthenticated endpoint for currencies BTC, ETH and USDC (the last returns the USDC-settled linear options, including SOL_USDC), taken in this session at about 02:13 UTC on 23 November 2026. For each instrument the response gives bid, ask, mark price, mark implied volatility, open interest (in units of the underlying), 24-hour volume and the underlying forward price. Aggregation by this note: open interest and volume multiplied by the underlying price and summed; relative spread = (ask - bid) / mark for instruments with both quotes; "near the money" = strike within 5% of the forward.

## Data and sample
A single point in time. 1,014 BTC, 830 ETH and 638 SOL_USDC option instruments. Index levels in the snapshot: BTC about 61,776, ETH about 1,749, SOL about 70.3.

## Reported results
Computed from the snapshot:

| Underlying | Open interest (USD) | 24h notional volume (USD) | Expiries | Instruments traded in 24h | Median relative spread, near the money |
|---|---|---|---|---|---|
| BTC (inverse) | 25.8 billion | 1,154 million | 12 | 498 | 4.8% |
| ETH (inverse) | 3.07 billion | 123 million | 12 | 314 | 5.2% |
| BTC_USDC (linear) | 708 million | 80 million | 8 | 190 | 3.4% |
| XRP_USDC | 84 million | 1.4 million | 6 | 56 | 8.6% |
| SOL_USDC | 76.5 million | 3.7 million | 6 | 108 | 9.8% |

- SOL open interest is concentrated in two expiries: 25 December (49 million) and 27 November (18 million). The two daily expiries (23 and 24 November) and the 4 December weekly held about 3.1 million combined.
- Median mark implied volatility near the money: SOL about 79, ETH about 70, BTC about 58.
- BTC options expiring within one day traded about 242 million notional in 24 hours; SOL options for the same expiry traded about 0.65 million.

## Signal construction
Not a signal. It is a feasibility check and a data recipe:
- Poll this endpoint (or subscribe to the ticker channels) to build BTC and ETH surfaces, 25-delta risk reversals, term structure and open interest by strike.
- For SOL, keep only a daily or hourly at-the-money mark implied volatility at the monthly expiry, and the ratio SOL implied volatility / BTC implied volatility as a relative-risk feature.
- Before using any SOL option quantity, check its staleness: with 108 of 638 instruments trading in a day, most mark prices are model marks, not traded prices.

## Relevance to SOL perpetuals at minutes to hours
Direct. Hedging flow from SOL options is negligible next to SOL perpetual volume, so dealer gamma, pinning and "max pain" stories for SOL have no plausible mechanism at current size. For scale: SOL options traded 3.7 million in a day on this venue, a figure a liquid perpetual trades in minutes. The comparison with perpetual volume was not measured in this session and should be.

## Caveats
One snapshot taken early on a Monday UTC (Sunday evening in the US), so the 24-hour volume window is a weekend; volume varies by day and regime. Deribit only: options on CME Solana futures, Bybit, OKX and Binance options and on-chain venues were not measured. Notional volume is contracts times the forward price, which overstates the economic size of far out-of-the-money trades. Relative spreads on cheap options are mechanically wide. The endpoint's field definitions come from the API response itself; the reference page was not opened.
