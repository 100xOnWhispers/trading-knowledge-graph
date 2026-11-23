---
title: "Foreign Exchange Fixings and Returns Around the Clock"
authors: "Krohn, Ingomar; Mueller, Philippe; Whelan, Paul"
year: 2024
venue: "Journal of Finance 79(1), 541-578 (Bank of Canada Staff Working Paper 2021-48 read)"
url: "https://www.bankofcanada.ca/wp-content/uploads/2021/10/swp2021-48.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/krohn-2024-fx-fixings-returns-around-clock.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "fx"
horizon: "hours"
tags: "fx-fixing, around-the-clock, intraday-reversal, dealer-inventory, benchmark, order-flow"
---

## Key insight
In the 24-hour FX market the US dollar systematically appreciates in the hours before the three major benchmark fixings (Tokyo 09:55 local, ECB 14:15 Frankfurt, WM/Reuters 16:00 London) and depreciates afterwards. A foreign-currency portfolio therefore traces V shapes around the fixes and a W over the full day. The authors explain it as constrained dealers pre-hedging an unconditional customer demand for dollars at the fix, with prices reverting once the liquidity event has passed.

## Method
Annualized average cumulative 5-minute log returns around the clock for each currency and an equal-weighted dollar portfolio, with returns measured over windows bounded by the fixes. Signed order flow is taken from the Refinitiv FX Matching inter-dealer platform and from CME FX futures to test which flow explains returns. Predictive regressions of post-fix reversals on the VIX, and simple pre-fix and post-fix trading strategies with and without transaction costs, complete the analysis.

## Data and sample
G9 currencies against the dollar (AUD, CAD, EUR, GBP, JPY, NZD, NOK, SEK, CHF), January 1999 to December 2019. Spot quotes from Refinitiv Tick History; forwards and CME futures; inter-dealer and futures order flow from June 2006.

## Reported results
- From the New York close to the Tokyo fix the foreign-currency portfolio loses 5.0% a year, then gains 5.3% a year until Europe opens.
- From the European open to the ECB fix it loses 4.2% a year; from the London fix to the New York close it gains about 4.6%.
- t-statistics range from 4.5 to 11.7; about 2.5 basis points per day per leg.
- Robust across currencies (the yen is the exception after the London fix), across the sample, and not driven by weekday or month effects. The same pattern appears in forwards and exchange-traded futures.
- Inter-dealer order flow shows net dollar demand at the fixes and is about an order of magnitude more informative for prices than CME futures flow.
- Gross of costs, 1 dollar invested in 1999 grows to 9 (dollar portfolio) or 12 (yen) around the Tokyo fix and to 27 (euro) around the European fixes; most profits disappear after transaction costs. Reversal returns are higher when the VIX is high.

## Signal construction
Clock-event template: for each scheduled benchmark time T, expect drift in the direction of the known structural demand over a pre-window (a few hours before T) and reversal over a post-window. Position = +direction before T, -direction after T, scaled up when implied volatility is high. Parameters: event list, window lengths, direction of structural demand.

## Relevance to SOL perpetuals at minutes to hours
Crypto has its own fixings with predictable one-sided hedging demand: the CME CF reference rates that settle CME futures and price US spot ETF creations and redemptions (16:00 New York and 16:00 London), Deribit's 08:00 UTC expiry index window, and the perpetual funding index snapshots (these crypto mechanics are this note's own mapping and should be verified against venue documentation). The V-shape hypothesis (pre-event drift, post-event reversal) is testable on each. The finding that dealer flow, not futures flow, carries the information suggests using flow on the venue where the hedgers trade.

## Caveats
About 2.5 bp per leg, not profitable after costs for a price taker; useful for timing, not as a stand-alone trade. Requires knowing the sign of structural demand, which for SOL is not established. Crypto fixing effects belong to topic 10. The working-paper version was read; the published version describes a "W" and may differ in details.
