---
title: "The US, Economic News, and the Global Financial Cycle"
authors: "Boehm, Christoph E.; Kroner, T. Niklas"
year: 2023
venue: "NBER Working Paper 30994 (also Federal Reserve IFDP 1371; listed by the author as forthcoming in the Review of Economic Studies)"
url: "https://www.nber.org/system/files/working_papers/w30994/w30994.pdf"
pdf: "sources/30-macro-state-intraday-transmission/boehm-2023-us-economic-news-global-financial-cycle.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "minutes"
tags: "announcement, global-financial-cycle, risk-appetite, vix, international-spillover, event-study, pre-2020"
---

## Key insight
US macro releases move risky assets everywhere within 30 minutes: stock indices of 27 countries, the VIX and commodity prices all jump on US surprises, the foreign responses are about as large as the S&P 500's, and they co-move. Foreign releases have almost no effect on the US market. The pattern of stock, yield and risk-premium responses points to a direct effect on investors' risk-taking capacity and not only to an anticipated Fed reaction. US data are therefore a causal driver of the global risk cycle.

## Method
Standardised surprise = (released value minus survey expectation) divided by its sample standard deviation. Pooled event-study regressions of the 30-minute log change in each country's stock index on the surprise, controlling for other releases in the window; the price change is measured from the average of minutes t-15 to t-5 to the average of t+15 to t+25. Same design for VIX futures, VSTOXX, commodities and yields. Persistence and variance shares at quarterly frequency follow Altavilla, Giannone and Modugno, including non-headline components of releases. A decomposition attributes the equity response to risk-free rates, dividends and the equity premium.

## Data and sample
Thomson Reuters Tick History intraday data, October 1996 to December 2019; 27 countries; 12 major US releases (plus a wider set in the appendix); 60 foreign releases for the reverse test. Ends before 2020; no crypto.

## Reported results
- 11 of 12 major releases have significant pooled effects on foreign stock indices at the 1 percent level (capacity utilisation at 10 percent). A positive payroll surprise raises stocks in all but one country.
- Pooled effect of a one-standard-deviation US advance GDP surprise on foreign indices: 17.60 basis points, close to 30 for some countries.
- Reverse direction: of 60 foreign releases, 8 move the S&P 500 at the 10 percent level; the largest (UK advance GDP) is 4.42 basis points.
- US macro news explains on average 23 percent of quarterly variation in foreign equity prices once non-headline news is included, about 15 percent for the VIX and 25 percent for commodities.
- The equity premium is quantitatively more important than expected dividends in the response; rate responses cannot explain the stock moves.
- Positive real-activity news: S&P 500 up, VIX down, 10-year yield up.

## Signal construction
Event-level risk-appetite impulse: at each major US release, sign and size of the standardised surprise, or more robustly the joint 30-minute move in S&P futures (up) and VIX futures (down). When both agree, classify the event as risk-on; when stocks fall and VIX rises, risk-off. The measurement convention (averaging prices over 11 minutes before and after) is a practical way to reduce noise when estimating response betas.

## Relevance to SOL perpetuals at minutes to hours
This is the mechanism by which US data should reach crypto: through global risk-taking capacity, the same channel that moves Brazilian or Korean equities. It predicts that SOL responds with the sign of the equity and VIX response, not with a crypto-specific sign, and that non-US releases can be ignored for direction. The 23 percent quarterly variance share argues that announcement responses persist and are not noise to be faded. The sample stops in 2019, so the crypto extension rests on the later Kroner, Mohammed and Vega paper (topic 02, secondary access).

## Caveats
Equity sign for growth news was positive on average in this sample; the Andersen et al. note shows it can flip with the cycle. Index data, not futures, for many countries, so stale prices outside local hours are a concern the authors address but cannot remove. Thirty-minute averaged windows hide the first-seconds dynamics.
