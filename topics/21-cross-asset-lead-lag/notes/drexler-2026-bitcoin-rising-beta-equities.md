---
title: "Crypto Is Coming of Age: The Case of Bitcoin's Rising Beta"
authors: "Drexler, Alejandro H.; Guettler, Andre; Sun, Angela"
year: 2026
venue: "Federal Reserve Bank of Chicago Working Paper 2026-16"
url: "https://www.chicagofed.org/-/media/publications/working-papers/2026/wp2026-16.pdf?sc_lang=en"
pdf: "sources/21-cross-asset-lead-lag/drexler-2026-bitcoin-rising-beta-equities.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "multi"
horizon: "minutes"
tags: "bitcoin, equity-beta, intraday, us-hours, nasdaq, dow-jones, structural-break, stability"
---

## Key insight
Measured on 30-minute returns inside US market hours, Bitcoin's beta to US equities was near zero before 2020 and has been persistently positive and large since, with a structural break around late 2020. The exposure is to the broad market: once Dow Jones returns are controlled for, the NASDAQ adds little. Bitcoin now trades as a broad risk-on asset during the US session, and this predates the 2024 spot ETFs.

## Method
- Baseline: r_BTC(t) = alpha + beta * r_stocks(t) + e(t) on contemporaneous 30-minute returns within a common window aligned to US trading hours; beta re-estimated monthly in rolling windows and smoothed with a three-month centred moving average.
- Multi-factor: Bitcoin on Dow Jones, NASDAQ and 10-year Treasury returns; robustness by orthogonalizing NASDAQ on Dow Jones and the reverse.
- Bai-Perron structural break tests on daily returns, with break dates chosen by the data.

The regressions are contemporaneous; the paper does not estimate lead-lag between equities and Bitcoin.

## Data and sample
Minute-level Bitcoin and equity index prices from FirstRate (Bitcoin sourced from major crypto exchanges), Treasury yields from LSEG; April 2013 to March 2026.

## Reported results
- One-break estimates: NASDAQ beta about zero before and 0.428 after a break dated 2020-06 (interval 2018-07 to 2022-02); Dow Jones beta about zero before and 1.317 after a break dated 2020-12 (interval 2020-08 to 2021-09). Both late-regime betas significant at 1%.
- The introduction states the Dow beta rises from roughly 0.4 before 2020 to roughly 1.5 after 2021.
- Two-factor robustness, post-2020 averages: Dow beta 0.87 with residualized NASDAQ beta 0.11; in the reverse orthogonalization NASDAQ beta 0.35 and residualized Dow beta 0.79.
- The 10-year Treasury beta is small and indistinguishable from zero.
- Rolling betas are low and unstable early in the sample and "less noisy, persistently positive" later.
- The authors link the break timing to corporate treasury adoption in 2020-2021 (MicroStrategy, Tesla, the Coinbase listing) without claiming causality.

## Signal construction
Regime input, not a standalone signal. Compute a rolling beta of SOL (and BTC) 5- to 30-minute returns on ES or YM futures returns during US hours over the last 20 to 60 sessions, plus the R-squared. Use it to (a) scale the weight of equity-futures features in the model, (b) decide whether an equity move with no crypto response yet is a candidate catch-up trade, and (c) hedge or size around US cash open and close when equity-driven variance is highest. Whether lagged equity returns predict crypto must be tested separately; this paper only shows that contemporaneous exposure exists and is large.

## Relevance to SOL perpetuals at minutes to hours
It is the best-documented intraday evidence, in the sources opened, that crypto and US equities are tied together during US hours, measured through March 2026. SOL has a high beta to BTC, so an equity beta above one for BTC implies material equity-driven variance in SOL during the US session. Kalshi is a US venue whose activity is likely to concentrate in US hours, which is when this linkage operates. The finding that the Dow matters more than the NASDAQ suggests using a broad index future, not only NQ, as the equity input.

## Caveats
A short working paper, not peer-reviewed. Bitcoin only; no SOL or ETH. Contemporaneous betas say nothing about which market moves first, and 30-minute bars would hide leads of seconds to a few minutes. Index levels, not futures, appear to be used for equities, so overnight linkage is not measured. Possible multicollinearity between the indices is addressed (maximum monthly VIF of four is reported) but limits the NASDAQ-versus-Dow conclusion.
