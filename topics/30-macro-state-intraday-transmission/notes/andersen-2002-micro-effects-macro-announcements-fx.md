---
title: "Micro Effects of Macro Announcements: Real-Time Price Discovery in Foreign Exchange"
authors: "Andersen, Torben G.; Bollerslev, Tim; Diebold, Francis X.; Vega, Clara"
year: 2002
venue: "NBER Working Paper 8959 (the version read; the published version is usually cited as American Economic Review, 2003)"
url: "https://www.nber.org/system/files/working_papers/w8959/w8959.pdf"
pdf: "sources/30-macro-state-intraday-transmission/andersen-2002-micro-effects-macro-announcements-fx.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "fx"
horizon: "minutes"
tags: "announcement, standardized-surprise, jump, event-study, sign-asymmetry, volatility-response, pre-2020"
---

## Key insight
This is the paper that fixed the template for announcement studies. Standardised surprises in scheduled US releases move the conditional mean of dollar exchange rates in a jump that is essentially complete within the first five-minute bar, while volatility adjusts gradually over about an hour. Only the unexpected part of a release matters, earlier releases within a category matter more than later ones, and bad news moves prices more than good news.

## Method
Standardised news for indicator k: S_kt = (A_kt - E_kt) / sigma_k, where A is the announced value, E the median survey forecast (Money Market Services, collected the Friday before) and sigma_k the sample standard deviation of the surprise. Model (1): the five-minute return regressed on five own lags and on contemporaneous and two lagged values of each of 41 news series, estimated by two-step weighted least squares. The volatility equation (2) for the absolute residual uses a daily GARCH(1,1) forecast, a Fourier flexible form for the intraday pattern, calendar dummies, and absolute news with a third-order polynomial decay over 12 bars (one hour). Equation (3) regresses the post-release five-minute return on the surprise using announcement observations only.

## Data and sample
Five-minute returns from Reuters interbank quotes (Olsen and Associates) for DEM, GBP, JPY, CHF and EUR against the dollar, 3 January 1992 to 30 December 1998; 1,724 days and 496,512 five-minute observations after filters. Forty-one US and German indicators plus the federal funds target. Entirely pre-2020; no crypto.

## Reported results
- The mean adjusts in a jump immediately after the release with little movement afterwards; the allowance for negative lags (leakage) proved unnecessary in this sample.
- A one-standard-deviation payroll surprise moves DEM/USD by 0.16 percent, against a typical spread near 0.06 percent; only 0.7 percent of all five-minute returns exceed 0.10 percent in absolute value.
- In announcement-only regressions R-squared is often around 0.3 and sometimes near 0.6; across all bars it is very small because releases occupy about 0.2 percent of observations.
- Within indicator groups, earlier releases have higher R-squared (the timing effect).
- One hour is enough for full volatility adjustment for all indicators and currencies.
- German releases with unknown intraday timing have much weaker effects than US releases with known times.
- Sign effect: negative surprises have larger impact; the authors link this to forecast dispersion rising after bad news.

## Signal construction
A calendar of release times, a consensus forecast and a trailing standard deviation of past surprises give z = (actual - consensus) / sigma. The expected immediate return is beta_k times z, with beta_k estimated per indicator and instrument on announcement bars only. The volatility response is a separate, slower object: scale risk for about an hour after a release using a decaying multiplier fitted to absolute returns.

## Relevance to SOL perpetuals at minutes to hours
What transfers is the measurement design: surprise standardisation, announcement-only regressions, separate mean and volatility responses, and the expectation that the mean reaction is over in minutes while elevated volatility persists. What needs re-testing is the speed: the crypto evidence known to this repository (topic 02) reports adjustment over 15 to 30 minutes, slower than the jump found here. Betas for SOL must be estimated on post-2021 data.

## Caveats
1990s dealer-quoted FX, a single expansion, and five-minute bars that cannot resolve sub-minute dynamics. The sample has no recession, so state dependence could not be tested (the 2005 follow-up addresses it). A jump that completes inside one bar is not tradable without the number in advance.
