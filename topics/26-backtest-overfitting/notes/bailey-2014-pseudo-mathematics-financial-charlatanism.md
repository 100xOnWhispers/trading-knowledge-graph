---
title: "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance"
authors: "Bailey, David H.; Borwein, Jonathan M.; Lopez de Prado, Marcos; Zhu, Qiji Jim"
year: 2014
venue: "Notices of the American Mathematical Society"
url: "https://www.davidhbailey.com/dhbpapers/backtest-pseudo.pdf"
pdf: "sources/26-backtest-overfitting/bailey-2014-pseudo-mathematics-financial-charlatanism.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "backtest-overfitting, minimum-backtest-length, multiple-testing, sharpe-ratio, hold-out"
---

## Key insight
A high in-sample Sharpe ratio is easy to obtain after trying only a handful of strategy configurations, even when every configuration has zero true skill. The paper turns this into a budget: for a given length of history there is a maximum number of independent configurations a researcher may try before the best in-sample Sharpe becomes meaningless. When returns have memory (serial correlation or a global constraint), the overfit winner is expected to lose money out of sample, not merely to earn zero.

## Method
Theory plus Monte Carlo. Using Lo's asymptotic distribution of the estimated Sharpe ratio, the authors derive the expected maximum of N independent standard-normal draws:

E[max_N] ≈ (1 − γ) Z⁻¹[1 − 1/N] + γ Z⁻¹[1 − 1/(N e)], with γ ≈ 0.5772 (Euler-Mascheroni), bounded above by sqrt(2 ln N).

Rescaling by y^(−1/2) for y years of data gives the Minimum Backtest Length:

MinBTL ≈ ( E[max_N as above] / target Sharpe )² < 2 ln(N) / (target Sharpe)²  (years).

Later sections show by simulation that "compensation effects" (a global constraint on the sample, or first-order serial correlation) make in-sample and out-of-sample performance negatively related.

## Data and sample
No market data in the core results; simulated IID normal and autoregressive return series. One illustrative seasonal-strategy example is worked through.

## Reported results
- Trying only N = 10 configurations on one year of data is expected to yield a best in-sample annualized Sharpe of 1.57 when the true Sharpe of every configuration is zero.
- With 5 years of data, no more than 45 independent configurations should be tried, or a skill-less strategy with in-sample annualized Sharpe of 1 is almost guaranteed.
- Under the null of zero Sharpe, increasing the sampling frequency q does not reduce the variance of the annualized Sharpe estimate; only more years (y) do.
- The hold-out method is criticized because it ignores the number of trials run before the hold-out is consulted.
- With memory in the series, "good backtest performance is an indicator of negative future results" when overfitting is not controlled.
- MinBTL is a necessary, not sufficient, condition; correlated trials make it conservative, and the authors suggest reducing trials to an effective independent count (for example by principal components).

## Signal construction
Not a signal. It is a research-budget rule. Before a parameter search, compute the number of years of data y and the Sharpe that would be considered interesting; cap the number of effectively independent configurations at roughly N such that 2 ln(N) / SR² < y, and log every configuration tried.

## Relevance to SOL perpetuals at minutes to hours
Directly applicable and sobering. SOL perpetual history on the large offshore venues is only a few years long and Kalshi's is months. The frequency result matters most: having millions of one-minute bars does not relax the limit, because the binding quantity is calendar years for an annualized Sharpe under the null. A grid search, Bayesian optimizer, genetic algorithm or reinforcement-learning hyperparameter sweep each consumes this budget; an evolutionary run with thousands of fitness evaluations exhausts it immediately unless trials are highly correlated. The negative-drift result under memory is a warning for mean-reverting crypto series.

## Caveats
The derivation assumes independent trials and IID normal returns; real parameter grids are highly correlated, so the effective N must be estimated and the paper gives only a pointer for doing so. Intraday strategies with a genuinely high true Sharpe need far less time to prove themselves than the null-based bound suggests; MinBTL speaks only to rejecting skill-less winners. The version read is the authors' preprint dated April 2014.
