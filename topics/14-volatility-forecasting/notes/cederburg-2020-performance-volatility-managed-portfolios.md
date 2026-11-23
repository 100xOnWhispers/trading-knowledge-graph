---
title: "On the performance of volatility-managed portfolios"
authors: "Cederburg, Scott; O'Doherty, Michael S.; Wang, Feifei; Yan, Xuemin (Sterling)"
year: 2020
venue: "Journal of Financial Economics 138, 95-117"
url: "https://www.lehigh.edu/~xuy219/research/COWY.pdf"
pdf: "sources/14-volatility-forecasting/cederburg-2020-performance-volatility-managed-portfolios.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "equities"
horizon: "multi-day"
tags: "volatility-managed, out-of-sample, real-time, structural-instability, replication, contrarian-evidence"
---

## Key insight
The headline gains from volatility-managed portfolios do not survive a real-time test on a broad set of strategies. Across 103 equity strategies, the managed version beats the unmanaged one about as often as it loses. The positive spanning-regression alphas reported by Moreira and Muir are confirmed in sample, but they describe a combination of managed and unmanaged portfolios whose weights are only known after the fact; realistic out-of-sample versions mostly do worse than simply holding the original portfolio.

## Method
For each strategy the managed portfolio scales the original by the inverse of the previous month's realized variance of daily returns. Three exercises: (1) direct comparison of Sharpe ratios of managed and unmanaged versions; (2) in-sample spanning regressions; (3) real-time "combination" strategies in which an investor estimates, from a training sample, the mean-variance weights on the managed and original portfolios, with variations (expanding versus rolling windows, leverage constraints, alternative weight rules). Performance is measured by certainty equivalent return and Sharpe ratio, and the source of the out-of-sample shortfall is diagnosed.

## Data and sample
103 US equity trading strategies: the nine factors studied by Moreira and Muir plus 94 anomaly portfolios built from the variables catalogued by Hou and co-authors. Daily and monthly returns; long US samples.

## Reported results
- Direct comparison: the managed version has the higher Sharpe ratio in 53 of 103 cases and the original in 50. Only eight strategies show a statistically significant Sharpe difference in favour of volatility management, and these are concentrated among momentum-related strategies.
- Spanning regressions: 77 of 103 managed portfolios have positive alphas in sample (23 significantly positive, 3 significantly negative), consistent with Moreira and Muir.
- Real-time combination strategies earn a lower certainty equivalent return than the original portfolio in 72 of 103 cases in the base design.
- The out-of-sample failure is attributed mainly to structural instability in the spanning regressions.

## Signal construction
Not a signal. It is a testing protocol for any sizing overlay: (1) compare the sized and unsized versions of the same strategy directly, on the same capital, out of sample; (2) do not credit an overlay with gains that require knowing full-sample scaling constants or optimal mixing weights; (3) check stability of the gain across sub-periods before adopting it.

## Relevance to SOL perpetuals at minutes to hours
A direct warning against assuming that inverse-variance sizing improves a SOL strategy's Sharpe ratio. The benefit depends on the specific strategy: the significant gains were concentrated in momentum-related strategies, and absent for most others. Each SOL signal needs its own with-and-without comparison. The risk-stabilising benefit documented in the Harvey note is a separate matter and is not contradicted here.

## Caveats
US equity factor portfolios at monthly frequency; nothing on crypto or intraday trading. The paper tests inverse realized-variance scaling with one-month lookback; other forecasters or inverse-volatility scaling may behave differently. The open copy is the published article on a co-author's university page.
