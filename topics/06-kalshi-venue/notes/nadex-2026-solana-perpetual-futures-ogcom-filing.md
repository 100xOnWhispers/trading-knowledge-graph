---
title: "Product Certification: Solana (SOL) Perpetual Futures Contract - Submission Pursuant to Commission Regulation 40.2(a)"
authors: "North American Derivatives Exchange, Inc. d/b/a OG.com Markets"
year: 2026
venue: "CFTC product filing (self-certification), October 8, 2026"
url: "https://www.cftc.gov/filings/ptc/ptc10082632644.pdf"
pdf: "sources/06-kalshi-venue/nadex-2026-solana-perpetual-futures-ogcom-filing.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "nadex, og-com, sol, perpetual-futures, competing-venue, funding-formula, interest-rate-component, cf-benchmarks"
---

## Key insight
A second US exchange self-certified a SOL perpetual four months after Kalshi, using the same reference index (CME CF Solana-Dollar Real Time Index) but an offshore-style funding rule with an interest component. When the premium is small this contract pays 0.01% per 8 hours from longs to shorts, whereas Kalshi's pays zero. The two contracts therefore have different carry in quiet markets despite tracking the same index.

## Method
A 23-page self-certification. Exhibit B gives contract terms as new Rulebook Chapter 15; Exhibit B-1 gives the funding provisions.

## Data and sample
One contract: "SOLUSD Perp" (symbol SOL-USD-Perp), intended to list no later than October 12, 2026. The CFTC filing index lists the filer under the code CDNA and shows BTC, ETH, HYPE, SEI and ZEC perpetuals certified the same day and XRP, UNI and CRO on November 19, 2026.

## Reported results
- Contract size 1 SOL, tradable in units of 0.01 contract; tick $0.01 per SOL; 24/7 trading.
- All contracts are intermediated through a registered FCM or an introducing broker connected to one.
- Funding intervals end at 00:00, 08:00 and 16:00 UTC, not Eastern time.
- Premium, sampled each whole minute (480 per interval): `IPD = max(0, FairImpactBid - PI) - max(0, PI - FairImpactAsk)`, `PremiumRate = IPD / PI`, with Fair Impact Size $2,000 and impact prices bounded within 0.5% of the best bid and ask.
- Weighting: sample k carries weight k, as on Kalshi; invalid samples drop out of numerator and denominator.
- Sample sufficiency: if fewer than 50% of samples are valid fifteen minutes before interval end, the rate is the Default Funding Rate of 0%.
- `Funding_Rate = max(-Cap, min(Cap, P_w + max(-Beta, min(Beta, IR - P_w))))` with IR 0.01%, Beta 0.05% and Cap 2% per 8 hours.
- Settlement Times 11:00 AM and 4:00 PM Central; settlement price tiers are a 60-second VWAP, then a duration-weighted midpoint average, then index net change.
- Position accountability level $5,000,000; reportable level 25 contracts.
- The exchange states it "has at least one dedicated Market Maker".

## Signal construction
Not a signal by itself. It supports a cross-venue carry and basis feature: OG.com funding minus Kalshi funding for the same interval class, and the two venues' premium to the shared index. Because both reference SOLUSD_RTI, any persistent difference in premium isolates venue-specific order-flow pressure. Update per minute for premium, per 8 hours for funding.

## Relevance to SOL perpetuals at minutes to hours
The shared index removes reference-price noise from a Kalshi-versus-OG.com comparison, which makes it a cleaner pair than Kalshi versus Coinbase. The funding clocks differ: OG.com uses UTC boundaries and Kalshi uses Eastern time, so the windows are offset by four or five hours depending on daylight saving. Capital that arbitrages funding across the two would act at different times, which could create small predictable flows near each venue's boundary. This is a hypothesis; nothing in the filing tests it.

## Caveats
The filing certifies terms, not activity; no volume, spread or open-interest data for this contract was obtained, and it may be illiquid. Leverage and margin rates are not stated beyond "risk-based". Fees are deferred to a website schedule not opened. The filer names itself North American Derivatives Exchange d/b/a OG.com Markets; its corporate affiliation was not verified in this session. A November 2026 Louisiana court order described in a Kalshi emergency filing names several of these venues' affiliates and concerns event contracts, not perps.
