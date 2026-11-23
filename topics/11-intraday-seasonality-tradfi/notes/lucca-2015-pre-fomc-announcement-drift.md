---
title: "The Pre-FOMC Announcement Drift"
authors: "Lucca, David O.; Moench, Emanuel"
year: 2015
venue: "Journal of Finance 70(1), 329-371 (Federal Reserve Bank of New York Staff Report 512, August 2013 revision read)"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/lucca-2015-pre-fomc-announcement-drift.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "hours"
tags: "pre-announcement-drift, fomc, scheduled-events, equity-premium, volatility, event-window"
---

## Key insight
US equities earned large positive excess returns in the 24 hours before scheduled FOMC announcements, with no reversal afterwards and essentially zero average return from the announcement to the close. Over 1994 to 2011 this single recurring window accounted for about 80% of annual realized excess stock returns. The drift occurs while realized volatility and volume are unusually low, which makes it hard to reconcile with a standard risk premium.

## Method
Event study on a fixed clock window: the S&P 500 return from 14:00 the day before to 14:00 on the day of each scheduled FOMC announcement (statements were released around 14:15; none came before 14:10). Dummy-variable regressions compare this window with all other 14:00-to-14:00 windows. Tests cover data-snooping and small-sample robustness, international indices, industry and size portfolios, fixed income, other macro announcements, and conditioning on the VIX and the yield-curve slope. Before 1994, when decisions were not announced, close-to-close returns on meeting days are used.

## Data and sample
Intraday S&P 500 index data from Thomson Reuters TickHistory and Tickdata.com, September 1994 to March 2011 (scheduled meetings, eight per year); daily data back to 1960 with emphasis on 1980 onward.

## Reported results
- Average 14:00-to-14:00 pre-FOMC excess return: 49 basis points, t-statistic above 4.5; annualized Sharpe ratio of the window-only strategy 1.14.
- Close-to-14:00 window: Sharpe 1.43. Starting from the close two days prior: 54 bp, Sharpe about 1.
- 1980 to 1993 meeting days: 20 bp. Pooled 1980 to 2011: 36 bp (t = 4.86). No effect before 1980.
- No pre-FOMC effect in fixed income; no comparable pre-announcement drift before other major US macro releases.
- Higher when the VIX is high and the Treasury slope is low; serially correlated; unrelated to easing versus tightening or to the eventual surprise.
- Realized volatility and volume are lower than usual before the announcement and jump at the release.

## Signal construction
Calendar event rule: go long the equity index from T - 24h to T - 15min for each scheduled FOMC announcement at time T; flat through the release. Scale by the VIX level. Inputs: the published FOMC calendar and a volatility index. Eight events per year.

## Relevance to SOL perpetuals at minutes to hours
Crypto trades as a high-beta risk asset around US macro events, so a pre-FOMC long bias is a natural hypothesis, but it is inherited from equities, not established for SOL. More useful are the secondary facts: volatility and volume are suppressed before scheduled announcements and jump after, and the drift ends at the release. These shape risk limits, stop widths and whether to hold through the event. With eight events a year, SOL's short history gives very little statistical power.

## Caveats
Later evidence shows weakening: the authors' own 2018 update (noted separately) finds the drift only before meetings with press conferences in 2011 to 2018, and a 2021 Finance Research Letters paper reports it essentially disappeared after 2015 (abstract only). Eight events per year over 16.5 years in the core sample (exact count not re-checked); index returns, not traded futures, in the headline tests; no transaction costs, although one trade per event makes costs minor.
