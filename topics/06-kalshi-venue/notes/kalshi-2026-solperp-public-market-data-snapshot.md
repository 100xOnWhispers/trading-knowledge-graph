---
title: "Kalshi Perps public market-data API: KXSOLPERP market record, funding history, candlesticks, order book and premium index (snapshot of 2026-11-22)"
authors: "KalshiEX LLC (data); summary statistics computed in this research session"
year: 2026
venue: "external-api.kalshi.com public REST endpoints"
url: "https://external-api.kalshi.com/trade-api/v2/margin/markets/KXSOLPERP"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "minutes"
tags: "kalshi, sol-perp, liquidity, spread, funding-history, tracking-error, open-interest, leverage, data-availability"
---

## Key insight
No published study of Kalshi SOL perp liquidity was found, so this note records what the exchange's own unauthenticated API returned. The SOL perp quotes a spread of about 4.5 basis points, funding was exactly zero in 78% of intervals since launch, and the book tracked Coinbase spot within a few basis points over one day. Volume is large relative to open interest, which argues against reading volume as depth.

## Method
Unauthenticated GET requests to `/margin/markets`, `/markets/KXSOLPERP`, `/orderbook`, `/candlesticks` (1-minute and daily), `/trades`, `/funding_rates/historical`, `/funding_rates/estimate`, `/funding_rates/premium_index` and `/risk_parameters`. Statistics were computed with a short script. Coinbase SOL-USD one-minute candles were pulled from Coinbase's public API for the basis comparison.

## Data and sample
Snapshot near 01:57 UTC on 2026-11-23 (8:57 PM ET on 2026-11-22). Funding: all 517 intervals from 2026-06-03 20:00 UTC to 2026-11-22 21:00 UTC. One-minute candles and per-second premium index: the preceding 24 hours. Daily candles: 172 days from 2026-06-04.

## Reported results
- Contract fields: `contract_size` 0.1 SOL, `tick_size` $0.0001 per contract, `minimum_quantity` 1, fractional trading off, `funding_cap` 0.02, `funding_deadband` 0.0001, premium handling `dampen`, `schedule` null (24/7).
- Leverage estimates: long 3.59x at $1,000 notional falling to 3.29x at $1,000,000; short 3.09x falling to 2.87x. Headline `leverage_estimate` 3.09. Initial margin multiplier 1.3; queue-entry threshold 0.91; liquidation threshold 1.
- Quote: bid 7.0276, ask 7.0308 per 0.1 SOL. Open interest 203,549 contracts ($1.43M). 24-hour volume $17.2M. Cumulative volume $2.52B.
- Spread from 1,440 one-minute closes: median 4.5 bp, 10th percentile 3.1 bp, 90th 5.5 bp, maximum 8.1 bp. 214 minutes had no trade.
- Depth on the snapshot book: about $19k ask and $21k bid within 5 bp of mid; $144k and $487k within 10 bp; $1.24M and $1.38M within 25 bp.
- Funding: 401 of 517 intervals exactly zero (77.6%); 70 positive, 46 negative. Mean +0.15 bp per 8 hours (about 1.7% annualised). Range -8.5 bp to +7.7 bp. July 2026 had no non-zero interval; November to date averaged -0.97 bp.
- Premium index: 68% of seconds exactly zero; non-zero absolute median 1.0 bp, 99th percentile 5.5 bp, maximum 25 bp.
- Versus Coinbase spot over 1,384 matched minutes: mean basis +1.8 bp, standard deviation 2.1 bp; one-minute return correlation 0.976; correlations at a one-minute lead or lag were about -0.01.
- One-minute mid-return standard deviation 8.3 bp.
- Average daily notional by month: June $6.0M, July $5.6M, August $8.7M, September $12.0M, October $17.5M, November (22 days) $45.5M. Average open interest rose from $0.42M to $3.17M.
- Venue-wide: 143 perps (19 crypto). 24-hour notional $1.14B against $85M open interest. BTC perp $431M volume against $11.5M open interest.
- History: one-minute candles with bid and ask OHLC and trades with taker side are retrievable back to June 2026, at most 5,000 candles per request. The premium index returned nothing for a September window.

## Signal construction
Not a signal; these are the inputs for a cost and fill model. Recompute spread, depth within k bp, premium index and `leverage_estimates` on a schedule and store them, since the premium index is not retained. The gap between `reference_price` and the book mid is the live basis feature.

## Relevance to SOL perpetuals at minutes to hours
A 4.5 bp spread against 8.3 bp one-minute volatility means crossing the spread costs half a minute of typical movement before fees. At $1,000 to $20,000 clip sizes the book is adequate; above roughly $100,000 the impact price moves. About 170 days of one-minute bars is roughly 248,000 samples, thin for training a deep model on Kalshi data alone, so pretraining on offshore venues and fine-tuning here is the natural design.

## Caveats
One day and one book snapshot; depth is not an average. Statistics are my own computations, not exchange-published figures. Candle timestamps were aligned by convention and may be off by one bar, which would bias the lag test. Whether `leverage_estimate` refers to initial or maintenance margin is not confirmed. Volume turnover of 12 times open interest per day for SOL, and 37 times for BTC, coincides with fee-rebate and liquidity-provider programmes; volume may overstate organic liquidity.
