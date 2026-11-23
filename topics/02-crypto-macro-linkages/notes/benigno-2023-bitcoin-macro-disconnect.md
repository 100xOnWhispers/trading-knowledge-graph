---
title: "The Bitcoin-Macro Disconnect"
authors: "Benigno, Gianluca; Rosa, Carlo"
year: 2023
venue: "Federal Reserve Bank of New York Staff Reports, no. 1052"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1052.pdf"
pdf: "sources/02-crypto-macro-linkages/benigno-2023-bitcoin-macro-disconnect.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "multi"
horizon: "minutes"
tags: "event-study, intraday, fomc, cpi, nonfarm-payrolls, macro-surprises, null-result"
---

## Key insight
In 30-minute windows around US macro releases and FOMC statements from 2017 to 2022, Bitcoin does not respond systematically to macro surprises, unlike exchange rates, gold, silver and the S&P 500. The only significant macro response is to core CPI, and that is not robust to dropping 2022. This is the main contrarian reference against the view that crypto trades macro news intraday.

## Method
Intraday event study. The dependent variable is the percentage return from 5 minutes before to 25 minutes after the event.
- Monetary news: R = a + bT Target + bP Path + bL LSAP + e on scheduled FOMC days. Target and Path are the two principal components of 30-minute changes in fed funds and eurodollar futures (Gurkaynak-Sack-Swanson method); LSAP is the residual of the change in the 2-by-8 forward Treasury rate.
- Macro news: R = a + b MacroNews + e, estimated separately per release, where MacroNews = (announced value minus Bloomberg consensus) divided by the sample standard deviation of that difference. Surprises above five standard deviations are dropped.
- OLS with White standard errors; robustness with median regression and with one-hour and one-day windows.

## Data and sample
Five-minute prices for Bitcoin, six USD exchange rates, gold, silver and S&P 500 E-mini futures. Traditional assets January 2000 to December 2022; Bitcoin regressions January 2017 to December 2022 (47 FOMC observations). Releases: industrial production, retail sales, nonfarm payrolls, unemployment rate, jobless claims, trade balance, consumer confidence, ISM manufacturing, core PPI, core CPI. The Bitcoin price source is not stated in the parts read.

## Reported results
- Five-minute return standard deviation: Bitcoin about 0.4 percent, against about 0.04 percent for major exchange rates and about 0.07 to 0.08 percent for gold and the S&P 500.
- FOMC regression for Bitcoin: Target -15.06 (insignificant), Path -5.91 (significant at 5 percent), LSAP -0.29 (insignificant), R-squared 0.239. A one-standard-deviation Target or Path surprise corresponds to about a 0.6 percent move in Bitcoin.
- Macro releases, Bitcoin column (percent per one-standard-deviation surprise): nonfarm payrolls -0.06, ISM -0.08, retail sales -0.01, core PPI 0.07, all insignificant; core CPI -0.66, significant at 5 percent, R-squared 16.1 percent.
- Footnote: restricting to 2017 to 2021, the CPI coefficient is no longer significant for Bitcoin.
- Over 2017 to 2022 the S&P 500 responds to core CPI with -0.45 (significant at 1 percent), so in the same window Bitcoin's point estimate is larger than the equity response even though less precisely estimated.
- Results for Bitcoin are not robust across the robustness exercises; the authors conclude additional evidence is needed.

## Signal construction
The regression is the template for a post-release directional signal: at release time compute z = (actual minus consensus) / historical standard deviation of that gap, and map z to an expected 30-minute return using an estimated coefficient. On this paper's estimates only core CPI has a usable coefficient (about -0.66 percent per standard deviation in 2017 to 2022), and it should be treated as unstable. Inputs: a consensus feed and a release feed with sub-second timestamps; the bot needs the surprise within seconds to act before the adjustment completes.

## Relevance to SOL perpetuals at minutes to hours
The window length matches the bot's horizon exactly. The paper's point estimates suggest why a naive "trade every macro print" rule would have failed on Bitcoin through 2022: outside CPI the responses are indistinguishable from zero against a 0.4 percent five-minute volatility. SOL is not studied. Later work (see the Kroner note, read only second-hand) reports that sensitivity became significant after 2021, so this null should be re-estimated on 2021 to 2026 data, split by year, for SOL and BTC.

## Caveats
Only 47 FOMC observations and six years of monthly releases per series for Bitcoin (about 70 each, by arithmetic rather than a count read from the tables), so power is low given Bitcoin's volatility: a true effect of several tens of basis points could go undetected. Sample ends December 2022. Bitcoin only. Staff report, not peer reviewed. The "disconnect" headline partly reflects noise rather than a precisely estimated zero.
