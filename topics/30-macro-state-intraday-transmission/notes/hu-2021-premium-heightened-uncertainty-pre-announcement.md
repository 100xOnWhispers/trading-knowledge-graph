---
title: "Premium for Heightened Uncertainty: Explaining Pre-Announcement Market Returns"
authors: "Hu, Grace Xing; Pan, Jun; Wang, Jiang; Zhu, Haoxiang"
year: 2021
venue: "NBER Working Paper 25817, revised March 2021 (the version read; the published version is usually cited as Journal of Financial Economics, 2022)"
url: "https://www.nber.org/system/files/working_papers/w25817/w25817.pdf"
pdf: "sources/30-macro-state-intraday-transmission/hu-2021-premium-heightened-uncertainty-pre-announcement.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "futures"
horizon: "hours"
tags: "pre-announcement-return, vix, uncertainty-resolution, nonfarm-payrolls, ism, gdp, fomc, pre-2020"
---

## Key insight
The pre-FOMC drift is one case of a general pattern: equity-index futures earn large returns, with no abnormal variance, in the overnight window before payrolls, ISM and GDP releases as well. The authors explain it as a premium for uncertainty about how large the news impact will be. That uncertainty builds in the days before a release (VIX rises, prices dip) and resolves shortly before it (VIX falls, prices recover). The size of the pre-release return is predictable from the VIX build-up, and unscheduled VIX spikes are followed by the same kind of return.

## Method
Three periods per event: accumulation (six days before, up to the prior close), pre-announcement (prior day's 4 pm close to five minutes before the release) and post-announcement (to the 4 pm close). Returns from S&P 500 futures, which trade nearly around the clock. Sorts of announcement days on the pre-announcement fall in VIX and in realised variance; predictive regressions of the pre-announcement return on the accumulation-period change in VIX; the same regressions on non-announcement days. Heightened-VIX days are defined at the close of day t either by the daily VIX change exceeding a cutoff or by VIX exceeding its exponentially weighted moving average by a cutoff.

## Data and sample
S&P 500 and E-mini futures, VIX; September 1994 to May 2018 for the main results (190 scheduled FOMC releases), with January 1986 to May 2018 for the VIX-spike tests. Pre-2020; equities only; no crypto.

## Reported results
- Average pre-announcement returns: 10.1 basis points before payrolls, 9.1 before ISM, 7.5 before GDP, all significant, against 0.69 on non-announcement days. Pre-FOMC: 27.1 basis points on this window definition (lower than the 49 in Lucca and Moench because the window is shorter and the sample runs past 2011).
- Days with a large pre-announcement fall in VIX earn 76.6 and 64.8 basis points (high and low variance-reduction groups); days with a small fall earn -5.0 and -8.8. The sort on VIX, not on variance, drives the result.
- Non-announcement days following a VIX rise above 2.5 percent (about 11 per year) earn 36.59 basis points next day; above 3.0 percent (about 7.7 per year), 42.70. With smoothing (decay 0.30, cutoff 3 percent, 7.6 days per year) the average is 48.04 basis points.
- The six-day VIX change predicts next-day returns only on heightened-VIX days (adjusted R-squared 2.34 percent); otherwise R-squared is essentially zero.

## Signal construction
(a) Event gate: on the eve of payrolls, ISM, GDP and FOMC, compute the six-day change in VIX. A large build-up predicts a larger pre-release return and a larger VIX fall. (b) Spike rule: at the US close, if VIX minus its exponentially weighted average of past values exceeds about 3 points, flag the next session as a high-premium day. Both are daily-frequency state variables applied to an intraday window.

## Relevance to SOL perpetuals at minutes to hours
If crypto trades as a high-beta risk asset, the pre-release window for the big four announcements may carry positive drift in SOL as well, conditional on prior build-up in implied volatility. The crypto analogue of the state variable would be the Deribit DVOL build-up into the event. None of this has been tested on crypto, and the return accrues overnight in US terms, when crypto liquidity is thinner.

## Caveats
Sample ends in 2018; topic 11 holds notes on the weakening of the pre-FOMC drift after 2015. Averages of 7 to 10 basis points on equity futures are small relative to crypto spreads and funding. The model is one explanation among several. The VIX-spike result is partly a restatement of short-horizon reversal after selloffs.
