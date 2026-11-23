---
title: "Stop-Outs Under Serial Correlation and the Triple Penance Rule"
authors: "Bailey, David H.; Lopez de Prado, Marcos"
year: 2014
venue: "Author preprint (first version December 2012, this version October 2014); journal not confirmed"
url: "https://www.davidhbailey.com/dhbpapers/stop-out.pdf"
pdf: "sources/26-backtest-overfitting/bailey-2014-stop-outs-serial-correlation-triple-penance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "drawdown, time-under-water, stop-out, serial-correlation, live-monitoring"
---

## Key insight
How deep a drawdown and how long a time under water are consistent with a strategy still being what its Sharpe ratio says it is? Under IID normal outcomes the paper gives closed forms for both, and shows that recovery from the worst expected loss takes three times as long as the loss took to build (the "triple penance rule"). Ignoring positive serial correlation in outcomes grossly understates both quantities, which leads to stopping out strategies that are behaving normally.

## Method
Outcomes per period are modelled as normal with mean μ and standard deviation σ, first IID and then first-order autoregressive, AR(1). For a significance level α the authors derive:
- the maximum quantile-loss MaxQL_α, the worst cumulative loss over any horizon at that confidence, and the number of observations t* at which it occurs;
- the quantile time under water TuW_α;
- the implied time under water for a realized loss, used to translate a loss into "how unusual is this";
- Theorem 1: under IID normal outcomes, TuW_α / t* − 1 = 3 regardless of the Sharpe ratio.
Python code accompanies the analytical results.

## Data and sample
Hedge Fund Research monthly indices from January 1990 to January 2013 (265 observations per index) for the empirical section; the rest is analytical.

## Reported results
- Ignoring first-order serial correlation leads to underestimating the downside potential of hedge fund strategies by as much as 70% (abstract).
- For the HFRI RV Fixed Income-Convertible Arbitrage index, the maximum quantile-loss under independence is 3.79% against 11.60% with first-order autocorrelation (a 67% underestimation), and the quantile time under water is 21.28 monthly observations against 74.42 (a 71% underestimation).
- Penance for hedge fund indices ranges between 1.6 and 3 once autocorrelation is included; with positive serial correlation losses and time under water are larger but the ratio falls below 3.
- The authors estimate some firms may be firing more than three times the number of skillful managers they intended by evaluating them with IID-based metrics.
- Higher-Sharpe strategies warrant looser stop-out limits in absolute terms only in the sense derived; the paper gives the theoretical justification.

## Signal construction
Not a trading signal; a kill-switch calibration. Inputs: the strategy's expected per-period mean, standard deviation and lag-1 autocorrelation of net P&L (from the haircut backtest, then updated live). Outputs: a drawdown limit and a time-under-water limit at a chosen confidence. A live drawdown beyond MaxQL_α, or a time under water beyond TuW_α, is evidence at level α that the strategy's parameters are no longer those assumed.

## Relevance to SOL perpetuals at minutes to hours
A directional intraday bot needs a pre-committed rule that separates ordinary variance from decay or regime break. This paper supplies one that is explicit about autocorrelation, which matters for trend-following P&L (positively autocorrelated across days) and for strategies whose losses cluster in volatile regimes. It complements the probabilistic Sharpe ratio: PSR tests the mean, this tests the path.

## Caveats
Normality is assumed; crypto P&L has jumps and fat tails, so real quantile losses will exceed the formula. The inputs come from the backtest, so an overfit backtest yields limits that are too tight. AR(1) is the only dependence modelled; volatility clustering is not. Empirical evidence is on monthly hedge fund indices, far from intraday crypto.
