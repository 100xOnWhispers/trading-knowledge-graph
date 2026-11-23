---
title: "Using Genetic Algorithms to Find Technical Trading Rules"
authors: "Allen, Franklin; Karjalainen, Risto"
year: 1999
venue: "Rodney L. White Center for Financial Research working paper, Wharton School (version dated 9 October 1995); later published in the Journal of Financial Economics (1999)"
url: "https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9520.pdf"
pdf: "sources/16-oscillators-technical-rules/allen-1999-genetic-algorithms-technical-trading-rules.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "equities"
horizon: "daily"
tags: "genetic-programming, evolutionary-algorithms, rule-discovery, out-of-sample, transaction-costs, overfitting"
---

## Key insight
The founding paper on evolving trading rules by machine instead of taking them from practitioners. Rules bred on 1964 to 1967 S&P 500 data beat buy-and-hold after costs in 1970 to 1989, but the same procedure applied to other training and test periods back to 1929 produced no excess return after costs. What was robust was timing of volatility: the evolved rules were in the market on calmer, higher-return days and out on volatile, lower-return days.

## Method
Genetic programming over tree-structured rules. Building blocks are arithmetic and boolean operators, real constants, the closing price, and functions for the moving average, maximum and minimum of past prices and for lags. A 50-day moving average rule and a 30-day trading range break rule are both expressible, and crossover can combine them. Fitness is the continuously compounded excess return over buy-and-hold in the training period after a one-way cost c:

r = sum of r_t on "in" days + sum of r_f on "out" days + n log((1 - c)/(1 + c)), fitness = r - r_bh

with n the number of round trips and c = 0.1%. Positions are long or in the risk-free asset; no shorts. To limit overfitting, the best rule of each generation is checked on a separate selection period and saved only if it improves there. Settings: population 500, at most 100 nodes and 10 levels per tree, up to 50 generations, 100 independent trials. Prices are normalized by a 250-day moving average before rules are evaluated.

## Data and sample
S&P composite index, daily, 1963 to 1989 from CRSP (6,789 observations), extended back to 1929 for robustness. Training 1964 to 1967, selection 1968 to 1969, test 1970 to 1989.

## Reported results
- The 100 trials produced 82 distinct rules. Mean cumulative excess return over 1970 to 1989 was +90.23%, equal to 4.51% a year above a buy-and-hold return of 6.72%, at 0.1% one-way cost. Excess returns stay positive on average while the cost is below 0.18%.
- Applied to 1929 to 1963, the same rules earned a mean excess return of -0.72% a year (range -3.96% to +3.91%).
- Retraining on 1929 to 1938, 1939 to 1948 and 1949 to 1958 gave rules that did not, on average, beat buy-and-hold in the following test periods. Some learned features specific to the training window.
- Robust across periods: daily volatility was roughly 20% lower on days the rules were long.
- The authors conclude that the 1970 to 1989 excess returns "were more of an exception than the rule".
- For comparison, the BLL rules traded 4.2 times a year against 33.9 for the evolved rules and broke even at one-way costs up to 0.29% over 1929 to 1989.

## Signal construction
A rule-discovery procedure, not a signal. For a bot: define a grammar of indicator primitives (moving averages, rolling extrema, lags, RSI, band widths), use net-of-cost return as fitness, and keep a validation window that the search never optimizes on. The paper's main warning is that evolved rules trade far more often than hand-picked ones, so the cost term in the fitness function decides everything.

## Relevance to SOL perpetuals at minutes to hours
Evolutionary search is attractive for intraday crypto because the space of indicator combinations is large. This paper shows the likely outcome: a strong result on one test window and none on others. The volatility-timing result is the part worth carrying over, since scaling exposure down in high-volatility regimes is cheaper to verify than directional skill. Fitness should include funding payments and realistic taker fees.

## Caveats
I read the 1995 working paper. Park and Irwin's survey summarizes the published 1999 version as finding that evolved rules underperformed buy-and-hold for the S&P 500 over a long period, which is a more negative headline than the working-paper abstract. Daily equity index, long-only. One training window drives the positive result.
