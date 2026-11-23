---
title: "Price drift before U.S. macroeconomic news: private information about public announcements?"
authors: "Kurov, Alexander; Sancetta, Alessio; Strasser, Georg; Wolfe, Marketa Halova"
year: 2016
venue: "ECB Working Paper Series No 1901, May 2016 (the version read; the published version is usually cited as Journal of Financial and Quantitative Analysis, 2019)"
url: "https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1901.en.pdf"
pdf: "sources/30-macro-state-intraday-transmission/kurov-2016-price-drift-before-macro-news.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "futures"
horizon: "minutes"
tags: "pre-announcement-drift, informed-trading, e-mini, treasury-futures, leakage, event-study, pre-2020"
---

## Key insight
For a subset of US macro releases, equity-index and Treasury futures start moving in the direction of the coming surprise about 30 minutes before the official release time. For the seven releases with strong drift, the pre-release move is roughly half of the total price adjustment. The jump-at-release picture from earlier work therefore understates total impact, and the effect appears after 2008 and not before.

## Method
Event-study regression of the futures return over a window on the standardised surprise (actual minus Bloomberg consensus, scaled by its standard deviation). Market-moving releases are selected on the window [t - 5 s, t + 5 min]; the drift test re-estimates on [t - 30 min, t - 5 s]. A joint test across stock and bond markets classifies releases as strong drift, some drift or no drift, with robust regression as a check. Cumulative average returns over [t - 60 min, t + 60 min] and order-flow imbalances confirm the pattern. Explanations tested: leakage linked to release procedures, proprietary data collection that forecasts the surprise, and reprocessing of public information.

## Data and sample
Second-by-second E-mini S&P 500 (ES) and 10-year Treasury note (ZN) futures from Genesis Financial Technologies, 1 January 2008 to 31 March 2014; 30 US announcements, of which 21 are market-moving. Minute data back to 2003 for the comparison period. No crypto.

## Reported results
- 21 of 30 releases move prices at release. Example: a one-standard-deviation positive advance GDP surprise raises ES by 0.171 percent and explains 22 percent of the variation in the release window.
- Seven of the 21 show significant pre-release drift at the 5 percent level, always in the direction of the later surprise: Conference Board consumer confidence, existing home sales, preliminary GDP, industrial production, ISM manufacturing, ISM non-manufacturing, pending home sales.
- No drift for, among others, ADP employment and building permits; CPI, advance GDP, retail sales and jobless claims show only some evidence.
- The joint test of no drift is rejected at 1 percent in both markets (chi-square 63.5 for ES, 79.1 for ZN, 21 degrees of freedom).
- Averaged over the seven releases and both markets, the pre-release share of the total move is 44 percent.
- Cumulative returns from 180 to 30 minutes before release hover around zero; the drift starts about 30 minutes ahead.
- In 2003 to 2007 the effect is weak or absent.
- Back-of-envelope estimate of profits from pre-release trading in ES alone: about 20 million USD per year since 2008.

## Signal construction
For releases on the drift list, compute the ES and ZN return from t - 30 min to t - 5 s. A signed move in the direction implying a positive (negative) surprise is a weak prior on the surprise sign. Note the releases with drift are mostly private-sector or 10:00 ET indicators, not payrolls or CPI. A bot can also treat the same window as a risk interval: position before the release is exposed to informed flow.

## Relevance to SOL perpetuals at minutes to hours
If index futures lean before a release, crypto perpetuals may lean with them, which is testable with the same two-window design on SOL, BTC and ETH. More practically, it argues for measuring crypto reaction from a pre-release anchor (t - 30 min) and not only from the last price before the release, otherwise part of the response is missed or mistaken for noise.

## Caveats
Sample ends in March 2014; lock-up procedures were tightened afterwards and the effect may have shrunk. Classification rests on seven events' worth of cross-section. No trading costs. The headline releases crypto traders watch most (CPI, payrolls, FOMC) are not on the strong-drift list.
