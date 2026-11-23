---
title: "Introduction to Binance Futures Funding Rates (support FAQ 360033525031)"
authors: "Binance"
year: 2026
venue: "Binance support documentation"
url: "https://www.binance.com/en/support/faq/360033525031"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "funding-rate-formula, premium-index, clamp, funding-interval, settlement-timestamp, binance"
---

## Key insight
Binance funding is a time-weighted average of a 5-second premium index plus a clamped interest term, paid by default every 8 hours at 00:00, 08:00 and 16:00 UTC. Two details matter for prediction: later samples in the interval get more weight, and the interval itself is state-dependent, switching to hourly when a settlement hits the cap or floor.

## Method
Exchange specification, as extracted from the page in this session:
- `Funding amount = mark price * position size * funding rate`; payments pass between longs and shorts with no exchange fee.
- `F = [avg premium index P + clamp(interest - P, -0.05%, +0.05%)] / (8 / N)`, `N` the funding interval in hours.
- Interest is 0.03% a day (0.01% per 8 hours) for most symbols.
- `P = [max(0, impact bid - index) - max(0, index - impact ask)] / index`, with impact prices taken at a notional of 200 USDT divided by the initial margin rate at maximum leverage.
- `P` is sampled every 5 seconds (5,760 points per 8 hours). For intervals longer than one hour the average is linearly time-weighted, `(1*P1 + 2*P2 + ... + n*Pn)/(1 + 2 + ... + n)`; for one-hour intervals samples are equally weighted.
- Cap and floor: plus or minus 0.75 times the maintenance margin ratio at maximum leverage for listed major symbols, plus or minus 2% for others.
- Interval switching: from 2025-05-02, if a settlement hits the cap or floor the next interval becomes one hour. From 2026-01-02, a one-hour contract whose absolute rate stays at or below 0.025% for 16 consecutive cycles moves to four hours.

## Data and sample
None; a specification with worked examples.

## Reported results
- If the averaged premium is between -0.04% and +0.06%, funding equals the 0.01% interest rate. This is why funding prints are "pinned" at 0.01% much of the time ([Christin et al.](christin-2022-crypto-carry-trade.md)).
- Example: index 11,312.66, impact bid 11,316.83 gives `P` about 0.0369%; a time-weighted `P` of 0.0429% gives `F = 0.0100%`.
- Example: a BTCUSDT settlement at the -0.3% floor at 08:00 UTC moves the next settlements to hourly; a settlement at -0.25% does not.

## Signal construction
Reconstruct the running predicted funding rate: sample `P` every 5 seconds from book and index, keep the linearly weighted sum since the last settlement, apply the clamp and cap. Derived features: (1) distance of the running average from the clamp edges (-0.04%, +0.06%), since funding is flat inside and linear outside; (2) time to settlement, noting that the last hour carries about 23% of the weight in an 8-hour linear scheme (my arithmetic: 1 - (7/8)^2); (3) a flag when the rate is near the cap, because the venue then moves to hourly settlement.

## Relevance to SOL perpetuals at minutes to hours
Binance SOLUSDT is the main reference perp for SOL, so its predicted funding and premium are primary inputs. The linear weighting means late-interval premium moves change the print disproportionately, which gives traders a reason to act near the timestamp and fits the U-shape in [Ruan and Streltsov](ruan-2024-perpetual-futures-market-quality.md). Kalshi's formula must be read separately (topic 06) before reusing any of these constants.

## Caveats
Read through an automated page extraction; direct download was blocked, so constants and dates should be re-verified on the live page, which the exchange revises without notice. The grade reflects that this is a rule description, not tested evidence. SOL-specific cap parameters were not listed in what was read.
