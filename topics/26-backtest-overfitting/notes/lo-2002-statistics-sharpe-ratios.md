---
title: "The Statistics of Sharpe Ratios"
authors: "Lo, Andrew W."
year: 2002
venue: "Financial Analysts Journal"
url: "https://api.openalex.org/works/doi:10.2469/faj.v58.n4.2453"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "sharpe-ratio, standard-error, serial-correlation, annualization, estimation-error"
---

## Key insight
The Sharpe ratio is an estimate with a sampling distribution, and that distribution depends on the time-series properties of returns. Per the abstract, monthly Sharpe ratios cannot be annualized by multiplying by the square root of 12 except under very special circumstances, and serial correlation can cause large overstatement of annual Sharpe ratios.

## Method
Per the abstract: explicit expressions for the statistical distribution of the Sharpe ratio are derived using standard asymptotic theory under several assumptions about the return-generating process: independently and identically distributed returns, stationary returns, and time aggregation. The correct method of converting a higher-frequency Sharpe to a lower-frequency one is derived for stationary returns.

The full text was not accessible in this session (publisher page blocked, author page had no PDF). The IID-case result is restated in Bailey, Borwein, Lopez de Prado and Zhu (2014), which was read in full: the estimated annualized Sharpe from y years sampled q times per year is asymptotically normal with mean SR and variance (1 + SR²/(2q)) / y. That restatement, not Lo's own text, is the source for this formula here.

## Data and sample
Per the abstract: an illustrative empirical example using mutual funds and hedge funds. Sample details not confirmed.

## Reported results
From the abstract only:
- The annual Sharpe ratio for a hedge fund can be overstated by as much as 65 percent because of serial correlation in monthly returns.
- Once serial correlation is taken into account, rankings of hedge funds by Sharpe ratio can change dramatically.
- Square-root-of-time annualization holds only under very special circumstances.

## Signal construction
Not a signal. It is the basis for putting a confidence interval on any Sharpe ratio a backtest or live record produces, and for annualizing correctly. In practice: estimate the autocorrelations of the strategy's per-period net returns and adjust the annualization factor and the standard error for them before comparing strategies or feeding a Sharpe into the probabilistic or deflated Sharpe ratio.

## Relevance to SOL perpetuals at minutes to hours
High relevance as a correction step. A bot evaluated on one-minute or five-minute returns and annualized with a square-root factor of roughly 725 (square root of 525,600 minutes) or similar will report an inflated Sharpe if bar returns are positively autocorrelated, which happens with positions held across many bars, marked-to-mid P&L on a thin book, and smoothed funding accruals. Evaluating at a frequency where returns are close to uncorrelated (per trade or per day), or applying the autocorrelation correction, is the transferable lesson. Negative autocorrelation (mean-reverting P&L) biases the other way.

## Caveats
Abstract-only note: the specific formulas for the stationary case and the size of the mutual fund and hedge fund sample were not read. The results are asymptotic; short crypto samples with fat tails will have wider true confidence bands than the normal approximation gives (the probabilistic Sharpe ratio extends the IID case to skewness and kurtosis). The annualization arithmetic in the relevance section is this note's own illustration, not from the paper.
