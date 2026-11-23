---
title: "Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?"
authors: "DeMiguel, Victor; Garlappi, Lorenzo; Uppal, Raman"
year: 2009
venue: "Review of Financial Studies 22(5), 1915-1953"
url: "https://ideas.repec.org/a/oup/rfinst/v22y2009i5p1915-1953.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "multi-day"
tags: "one-over-n, equal-weight, mean-variance, estimation-error, estimation-window, benchmark"
---

## Key insight
The paper that made equal weighting the mandatory benchmark for any allocation rule. Across 14 optimizing models and seven datasets, none consistently beat the 1/N portfolio out of sample on Sharpe ratio, certainty-equivalent return or turnover. The gain from optimal diversification is more than offset by estimation error, and the amount of data needed to reverse that is far beyond what exists. Only the abstract was read in this session.

## Method
From the abstract: out-of-sample comparison of the sample-based mean-variance model and its extensions designed to reduce estimation error against the naive 1/N rule, on three criteria (Sharpe ratio, certainty-equivalent return, turnover). An analytical and simulation exercise, calibrated to the US equity market, then derives the estimation window length needed for the mean-variance strategy and its extensions to outperform 1/N.

## Data and sample
Seven empirical datasets (not listed in the abstract). A later paper opened in this session, Zhu et al. (2019), describes them as monthly; the datasets and dates were not confirmed from the source itself.

## Reported results
From the abstract:
- Of the 14 models evaluated across seven datasets, none is consistently better than 1/N on Sharpe ratio, certainty-equivalent return or turnover.
- Required estimation window for sample-based mean-variance and its extensions to beat 1/N: about 3,000 months for a portfolio of 25 assets and about 6,000 months for 50 assets.
- The authors conclude there are still many "miles to go" before the gains promised by optimal portfolio choice can be realized out of sample.

## Signal construction
Not a signal. It defines the benchmark. For strategy-level allocation inside a bot, 1/N means equal risk (or equal capital) across the live strategies or signals. Any estimated allocation, whether inverse-variance, mean-variance, hierarchical risk parity, bandit or learned gate, should be reported next to 1/N on the same net-of-cost basis, including turnover.

## Relevance to SOL perpetuals at minutes to hours
The arithmetic gets worse, not better, at short horizons. The number of periods needed scales with how noisy the mean estimates are, and intraday strategy returns have tiny means relative to variance and are non-stationary, so more bars do not buy more information about the mean (see the minimum-backtest-length argument in topic 26). With a handful of correlated intraday strategies and months of data, the paper's logic says equal risk weights are the rational default and that any deviation must be justified by a variance or correlation estimate (which is learnable quickly) more than by a mean estimate (which is not).

## Caveats
Abstract-only, so the per-dataset numbers, the list of 14 models and the treatment of transaction costs were not read. The setting is monthly long-only equity portfolios; strategies here are long-short return streams whose volatilities differ a great deal, which is why "equal risk" is the practical analogue of 1/N. Later literature proposes shrinkage and constrained rules that sometimes beat 1/N; that literature was not opened here.
