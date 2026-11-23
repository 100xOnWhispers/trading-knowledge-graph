---
title: "Asset Allocation under Multivariate Regime Switching"
authors: "Guidolin, Massimo; Timmermann, Allan"
year: 2007
venue: "Journal of Economic Dynamics and Control (read as Federal Reserve Bank of St. Louis Working Paper 2005-002C, revised October 2006)"
url: "https://files.stlouisfed.org/files/htdocs/wp/2005/2005-002.pdf"
pdf: "sources/01-macro-regime-detection/guidolin-2007-asset-allocation-multivariate-regime-switching.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "01-macro-regime-detection"
asset_class: "multi"
horizon: "multi-day"
tags: "markov-switching, four-state, crash-recovery, asset-allocation, out-of-sample, learning"
---

## Key insight
Two regimes are not enough to describe the joint behaviour of stocks and bonds. The authors find four: crash, slow growth, bull and recovery. The crash state is short and usually exits into a volatile recovery state, so large negative and large positive months cluster together. Optimal allocations change sharply with the filtered state probabilities, and the richer model holds up in a recursive out-of-sample test, though not at every horizon.

## Method
A multivariate Markov-switching model for the joint distribution of large-stock, small-stock and long-bond excess returns, with regime-dependent means and covariance matrices and, in some specifications, the dividend yield as predictor. Investors do not observe the state and update probabilities by Bayes' rule. Optimal buy-and-hold and rebalancing portfolios are solved by Monte Carlo for power utility. Evaluation: certainty-equivalent cost of ignoring regimes, a recursive pseudo out-of-sample experiment (parameters re-estimated each month on an expanding window), and a simulation asking whether four states overfit relative to two.

## Data and sample
Monthly CRSP returns, January 1954 to December 1999 (552 observations): small stocks (bottom two size deciles), large stocks, 10-year Treasury bonds, with T-bills as the riskless asset. Out-of-sample window 1980:01 to 1999:12 (240 months), plus a held-back 2000 to 2003 period.

## Reported results
- Average state durations: crash about two months, slow growth seven, bull eight, recovery just over three. Steady-state probabilities 9%, 40%, 28% and 23%.
- Exits from the crash state go almost always to recovery, with close to 50% probability each month.
- The null of zero welfare cost from ignoring regimes is rejected; the lower confidence bound on the cost reaches 7 to 8% of wealth at long horizons.
- Out of sample 1980 to 1999: a VAR(1) is best at the 1-month horizon, statistically indistinguishable from the regime model; the pure regime model gives the highest mean realized utility at 12 and 120 months.
- 2000 to 2003: the pure regime model does somewhat worse at 12 months because it stayed about 70% in stocks.
- Over 1980 to 2003 the four-state model is best at 1 and 120 months and the VAR(1) is best at 12 months.

## Signal construction
Not a directly usable signal. The design ideas a bot can borrow: (1) allow a separate rebound state after a crash state instead of forcing a two-state bull/bear split; (2) trade on filtered state probabilities, not hard labels; (3) re-estimate recursively and score out of sample against a simple linear benchmark.

## Relevance to SOL perpetuals at minutes to hours
The crash-then-recovery structure resembles crypto liquidation cascades, where a sharp drop is often followed by a violent bounce. A two-state model would label both as "high volatility" and miss that the sign of the expected return differs. Whether a four-state model is identifiable on intraday SOL data is an open question; the paper needed 46 years of monthly data and still found mixed out-of-sample results.

## Caveats
Monthly horizon, 1954 to 1999. The authors note that the choice of a four-state specification itself used the full sample. Out-of-sample superiority is horizon-dependent and a plain VAR wins at some horizons. No transaction costs.
