---
title: "BTNL 26-089 Self-Certification Pursuant to CFTC Regulation 40.2(a): Listing of Solana US Dollar Deci Perpetual Futures Contract"
authors: "Bitnomial Exchange, LLC (signed Walsh, James A.)"
year: 2026
venue: "CFTC product filing (self-certification), September 2, 2026"
url: "https://www.cftc.gov/filings/ptc/ptc09022623092.pdf"
pdf: "sources/06-kalshi-venue/bitnomial-2026-solana-deci-perpetual-futures-filing.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "bitnomial, sol, perpetual-futures, competing-venue, funding-formula, position-limits, regulated-us-perps"
---

## Key insight
Bitnomial lists a third regulated US SOL perpetual, with hard position limits where Kalshi has only an accountability level, and with a funding rule that includes an interest term. Together with the CFTC filing index, it shows that Bitnomial certified crypto perpetuals before Kalshi's May 2026 approval, which qualifies Kalshi's "first in America" claim.

## Method
A six-page self-certification with a specification table. The funding method is not in the filing; it points to a methodology page on Bitnomial's site, which was fetched and read through a page-to-text summariser.

## Data and sample
One contract: Solana US Dollar Deci Perpetual Futures, code PSOLUI, for trading on or after September 4, 2026, cleared by Bitnomial Clearinghouse. Market statistics in the filing are from CoinGecko as of August 30, 2026.

## Reported results
From the filing:
- Reportable contract size 1,000 SOL; minimum contract size 0.1 SOL; tick $0.01 per SOL.
- Price band variation 5% of the reference price; price limit 50% of the reference price.
- Position limit 1,700 contracts (1.7M SOL, about 0.29% of circulating supply); reportable level 25 contracts.
- Market hours 24/7. Index price: "CF Solana Mid-Price Spot Rate".
- SOL market capitalisation $59.8B and 30-day spot volume $82.8B at the filing date.

From Bitnomial's methodology page (as summarised by the fetch tool):
- Funding every 8 hours with intervals 7 PM to 3 AM, 3 AM to 11 AM and 11 AM to 7 PM Central.
- `FR = avg(P) + clamp(IR - avg(P), -0.05%, 0.05%)`, IR fixed at 0.01%.
- Premium `P = [max(0, CI_bid - S) - max(0, S - CI_ask)] / S`, sampled every 15 seconds (1,920 samples), index-weighted so later samples count more.
- Settlement price `= median(S, S + ma(S), ma(C))` using 2.5-minute averages.

From the CFTC filing index (rows read, documents not opened): Bitnomial perpetual futures on SOL and other tokens certified May 14, 2026, an Ethereum perpetual certified January 28, 2026, and single-stock perps marked "Approved" on November 2, 2026.

## Signal construction
Not a signal by itself. Adds a third US venue to a cross-venue premium and funding panel. Inputs: Bitnomial premium and funding at its Central-time boundaries; Kalshi and OG.com equivalents.

## Relevance to SOL perpetuals at minutes to hours
All three US SOL perps reviewed (Kalshi, OG.com, Bitnomial) use an impact-price premium with linearly increasing weights and 8-hour funding, but their interval boundaries fall at different clock times: Kalshi at 12 AM, 8 AM and 4 PM Eastern; Bitnomial at 3 AM, 11 AM and 7 PM Central; OG.com at 00:00, 08:00 and 16:00 UTC. Late-window premium matters most on each. Staggered boundaries mean the hours in which funding-motivated flow is most likely differ by venue, which is a testable source of intraday seasonality.

## Caveats
The evidence grade is C because the funding formula comes from a web page read through a summariser, not from the filing, and should be re-read directly before use. The September filing appears to resize contracts already listed in May; the relationship between the two sets was not checked. No Bitnomial volume, spread, leverage or fee data was obtained. The index named here may differ from the CME CF Real Time Index used by Kalshi; the exact index family was not confirmed.
