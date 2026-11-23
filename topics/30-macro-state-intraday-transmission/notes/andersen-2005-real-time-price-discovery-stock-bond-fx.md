---
title: "Real-Time Price Discovery in Stock, Bond and Foreign Exchange Markets"
authors: "Andersen, Torben G.; Bollerslev, Tim; Diebold, Francis X.; Vega, Clara"
year: 2005
venue: "NBER Working Paper 11312 (the version read; the published version is usually cited as Journal of International Economics, 2007)"
url: "https://www.nber.org/system/files/working_papers/w11312/w11312.pdf"
pdf: "sources/30-macro-state-intraday-transmission/andersen-2005-real-time-price-discovery-stock-bond-fx.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "minutes"
tags: "announcement, state-dependence, equity-futures, bond-futures, cross-market-linkage, heteroskedasticity-identification, pre-2020"
---

## Key insight
The sign of the equity response to the same macro surprise depends on the state of the economy. Good real-activity news lowers stock prices in expansions (the discount-rate effect dominates) and raises them in recessions (the cash-flow effect dominates), so the response looks weak when averaged over regimes although it is strong within each. Bonds respond most and with a stable sign. Beyond the direct news effect there are strong contemporaneous cross-market links at five-minute frequency.

## Method
Five-minute futures returns regressed on standardised surprises (surprise divided by its sample standard deviation, survey expectations from Money Market Services) for 25 US announcements, on announcement bars and in a system that adds own and cross-asset lags, estimated by weighted least squares with an intraday volatility model. The sample is split into expansion (to February 2001) and recession (March 2001 onward), dated from payroll declines. Contemporaneous cross-market coefficients are identified through heteroskedasticity, following Rigobon and Sack, because ordinary regression cannot separate simultaneous causation.

## Data and sample
Tick transaction prices from Tick Data for futures on USD/GBP, USD/JPY and USD/EUR, the S&P 500 (from January 1994, with pre-open GLOBEX trades to cover 8:30 releases), the 30-year US Treasury bond (January 1992 to December 2002), and FTSE 100, Euro Stoxx 50, Gilt and Bobl (July 1998 to December 2002). Common system sample July 1998 to December 2002: 15,764 five-minute observations in windows around releases. Pre-2020; no crypto.

## Reported results
- News produces conditional mean jumps in all three asset classes, mostly inside the first five-minute bar.
- Unconditionally, bonds react most, then currencies, then equities; conditioning on the cycle, equities and currencies are about equally responsive.
- Equity response to positive real shocks is negative in the expansion sample and positive in the recession sample, for US and foreign indices alike. Inflation surprises (CPI, PPI) are significantly negative for stocks in the expansion and insignificant in the recession.
- Stock-bond return correlation is small and positive in the expansion and strongly negative in the recession.
- Largest five-minute moves for the S&P 500 and Euro Stoxx futures exceed two percent.
- Spillovers run from the US equity market to foreign equity markets and not the reverse.
- The authors stress the limitation that the high-frequency sample has one expansion and one recession.

## Signal construction
Not a ready signal. It supplies a rule for one: the mapping from a surprise to a direction for a risk asset must be conditioned on a state variable. A live version estimates the surprise beta separately by regime (for example, by whether the market currently treats strong data as hawkish), or uses the realised stock-bond return correlation over recent announcement windows as the regime indicator and flips or shrinks the expected sign accordingly.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant to the reported sign flip in Bitcoin's payroll response around 2020 (topic 02): a risk asset's reaction to growth news is not a constant. For a bot, a fixed-sign rule on payrolls or retail sales is unsafe; inflation releases have had a more stable sign in tightening regimes. Using the first-minute move in equity-index futures as the sign reference avoids having to model the regime at all, which is why that proxy deserves a test on SOL.

## Caveats
One business cycle; the recession sample is 22 months. Five-minute bars. The regime definition is ex post. Futures on indices and bonds in 1992 to 2002 had different participants and speeds from today's markets.
