---
title: "Monetary Policy without Moving Interest Rates: The Fed Non-Yield Shock"
authors: "Boehm, Christoph E.; Kroner, T. Niklas"
year: 2025
venue: "Working paper, draft of 15 September 2025 (author-hosted; also circulated as an NBER and Federal Reserve working paper)"
url: "https://raw.githubusercontent.com/tnkroner/website/master/beyond_yield_curve_032521.pdf"
pdf: "sources/30-macro-state-intraday-transmission/boehm-2025-fed-non-yield-shock.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "hours"
tags: "fomc, monetary-policy-surprise, non-yield-shock, risk-premia, heteroskedasticity-identification, press-conference, post-2020"
---

## Key insight
Yield-based monetary policy surprises explain little of what equities and the dollar do around FOMC announcements. A latent shock that is orthogonal to all yield changes, identified from the excess variance of the S&P 500 and dollar exchange rates on FOMC days, accounts for much of the remainder. It raises US and foreign stocks, weakens the dollar and lifts commodities while leaving yields unchanged, and it works mainly through risk premia. The window in which this information is priced is hours, not minutes.

## Method
Returns of E-mini S&P 500 futures and 13 dollar exchange rates over windows from 10 minutes before the announcement to between 20 minutes and 18 hours after are first regressed on nine yield changes. The residual variance on FOMC days is compared with the same clock window on non-FOMC days (Brown-Forsythe test). A single latent factor is then estimated from those residuals by heteroskedasticity-based identification with the Kalman filter. The baseline window is 14 hours. Daily data are used for international effects.

## Data and sample
Intraday futures and exchange rates, January 1996 to July 2025: 240 FOMC days and 5,565 non-FOMC days. Forty countries for the daily spillover analysis. Spans pre- and post-2020. No crypto in the paper. The author's page lists a downloadable shock series.

## Reported results
- The Nakamura-Steinsson shock and Swanson's three shocks explain less than 30 percent of S&P 500 return variation at every horizon up to 16 hours after the announcement.
- Residual variance of S&P 500 futures on FOMC days is 2.6 to 3.1 times that of non-FOMC days at every window from 20 minutes to 10 hours; for the euro the ratio is 6.8 at 20 minutes, falling to 3.3 at 10 hours. All significant at 1 percent.
- Adding the non-yield shock more than doubles explained variation for every asset except the yen; for some exchange rates over 80 percent of the 14-hour variation is explained.
- A one-standard-deviation shock moves stock indices in 40 countries by 49 basis points on average over two days and the dollar by 35 basis points against 30 currencies. Global yields do not respond.
- After a positive shock, implied volatility of major equity indices falls 2.3 percent and of major currencies 1.4 percent.
- Larger shocks occur at meetings with press conferences and with the Summary of Economic Projections.
- Explanatory power of shocks built from 30-minute windows drops off for longer return windows, consistent with slow pricing or information in the press conference.

## Signal construction
Not directly a signal; the shock is estimated ex post. Its real-time proxy is simple: after an FOMC release, the part of the E-mini and dollar move not explained by the change in two- and ten-year yields. A bot can compute residual = equity futures return minus fitted response to yield changes, updated through the press conference, and treat its sign as the risk-premium component of the announcement.

## Relevance to SOL perpetuals at minutes to hours
The topic 02 note on Kroner, Mohammed and Vega (2026) records an unverified claim that a Fed shock leaving yields unchanged still moves crypto; this paper is where that shock comes from. If crypto loads on the non-yield component, then yield-based surprise measures will under-predict SOL's FOMC response, and the relevant horizon runs through the press conference and beyond, well within a minutes-to-hours bot's holding period. Elevated variance for ten hours also bears on stop placement and leverage after 2 pm ET on FOMC days.

## Caveats
Working paper; the shock's structural interpretation is left open by the authors. Identification assumes non-FOMC days are a valid variance baseline. 240 events. Crypto loading is not estimated here and must be tested.
