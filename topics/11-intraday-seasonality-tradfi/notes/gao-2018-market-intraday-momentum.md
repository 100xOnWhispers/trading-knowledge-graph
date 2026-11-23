---
title: "Market intraday momentum"
authors: "Gao, Lei; Han, Yufeng; Li, Sophia Zhengzi; Zhou, Guofu"
year: 2018
venue: "Journal of Financial Economics 129(2), 394-414"
url: "https://profiles.wustl.edu/en/publications/market-intraday-momentum/"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "hours"
tags: "intraday-momentum, first-half-hour, last-half-hour, etf, time-series-predictability"
---

## Key insight
The first half-hour return of the US equity market, measured from the previous close, positively predicts the last half-hour return of the same day. This is the paper that named "market intraday momentum" and started the time-series (as opposed to cross-sectional) intraday predictability literature. Only the abstract was read in this session.

## Method
Per the abstract: predictive regressions of the last half-hour return on the first half-hour return (which includes the overnight gap) using high-frequency ETF data, with conditioning on volatility, volume, recessions and macro news days. Details of estimation, out-of-sample tests and the timing strategy were not read.

## Data and sample
S&P 500 ETF, high-frequency data, 1993 to 2013, plus ten other actively traded domestic and international ETFs (abstract). The later paper by Baltussen et al. (noted separately, read in full) describes this sample as nine equity-index ETFs and one bond ETF.

## Reported results
From the abstract only:
- The first half-hour return predicts the last half-hour return; the predictability is described as both statistically and economically significant.
- It is stronger on more volatile days, higher-volume days, recession days and major macroeconomic news release days.
- It also appears in ten other actively traded ETFs.
- The authors relate it to Bogousslavsky's infrequent-rebalancing model and to late-informed trading near the close.
No coefficients, R-squared values or strategy returns were confirmed in this session.

## Signal construction
r_ONFH = log(price 30 minutes after the open / previous close). Position for the last 30 minutes of the session = sign(r_ONFH), optionally only when realized volatility or volume that day is high. One decision per day. Baltussen et al. (2021) report that the return from the previous close to 30 minutes before the close is a stronger predictor than r_ONFH across futures markets, so the two definitions should be tested side by side.

## Relevance to SOL perpetuals at minutes to hours
A 24-hour market has no open or close, so the signal needs an anchor. Candidate anchors are the US cash-equity session (09:30 to 16:00 ET, relevant because crypto co-moves with US equities), the CME crypto futures settlement window, the 00:00 UTC daily candle boundary and the 8-hour funding timestamps. Whether any of these produces a "last interval" with forced, direction-following flow is an empirical question; the mechanism in equities (end-of-day rebalancing and hedging) has no guaranteed analogue.

## Caveats
Abstract-only: treat every quantitative detail as not confirmed. Sample ends 2013; ETF-based; the effect earns one small return per day and is sensitive to costs. Later work finds a different predictor works better and links the effect to gamma hedging, which implies time variation in strength. No open-access copy from an author or institutional page was located (SSRN returned HTTP 403).
