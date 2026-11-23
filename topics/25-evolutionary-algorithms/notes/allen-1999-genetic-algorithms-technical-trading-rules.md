---
title: "Using Genetic Algorithms to Find Technical Trading Rules"
authors: "Allen, Franklin; Karjalainen, Risto"
year: 1999
venue: "Journal of Financial Economics 51(2), 245-271 (read: Rodney L. White Center for Financial Research working paper, Wharton, version dated 9 October 1995)"
url: "https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9520.pdf"
pdf: "sources/25-evolutionary-algorithms/allen-1999-genetic-algorithms-technical-trading-rules.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "daily"
tags: "genetic-programming, rule-discovery, selection-period, transaction-costs, overfitting, volatility-timing"
---

## Key insight
The first study to let an evolutionary search compose trading rules instead of testing rules chosen by hand. It also introduced the design that every later paper in this topic copies: a training window that drives evolution, a separate selection window that decides which rule is kept, and a test window that neither has touched. The rules found on one window beat buy-and-hold after costs in 1970 to 1989, but the abstract states that for other periods since 1929 they did not.

## Method
Rules are trees. Internal nodes are arithmetic and boolean operators plus `average`, `maximum`, `minimum` and `lag` over a window of past prices; leaves are real and boolean constants and the price. A rule returns "in the index" or "out, earning the risk-free rate". There are no short positions. Crossover swaps a random subtree between two parents, restricted to nodes of the same type; mutation inserts a random subtree with small probability. Fitness is excess return over buy-and-hold in the training period net of a one-way cost of 0.1%.

Overfitting control: after each generation the fittest rule on training data is run on the selection period and saved only if it beats the best rule saved so far. Evolution stops when the selection-period result has not improved for a set number of generations. Prices are divided by a 250-day moving average before rules see them, so constants learned in one decade stay meaningful in the next.

## Data and sample
Daily S&P 500 index. Training 1964 to 1967, selection 1968 to 1969, test 1970 to 1989 (5,054 trading days). 100 independent trials, one rule saved per trial. The abstract reports further periods back to 1929; I did not read those tables.

## Reported results
- 100 trials gave 82 distinct trading patterns. Mean cumulative excess return over 1970 to 1989 was +90.23% (standard deviation across rules 16.88%), or 4.51% a year above a buy-and-hold return of 6.72%.
- Excess returns stay positive on average while the one-way cost is below 0.18%.
- Per-rule yearly excess return ranged from +1.39% to +5.91% with 14 to 42 trades a year.
- Annual volatility of the rules averaged 9.6% against 16.0% for buy-and-hold. Return volatility on "in" days was about 22% lower than on "out" days.
- Most of the excess return accrued in the 1970s; in the 1980s the rules "would not even have matched the market rate of return".
- Abstract: using data for other periods since 1929, the rules identify high-return, low-volatility periods "but do not lead to excess returns after transaction costs".

## Signal construction
Not a signal. It is a search procedure. To reproduce: define a typed grammar of price primitives, score each tree by net-of-cost return on a training window, keep a rule only when it also improves on a selection window, and repeat the whole search many times to see how much the answer varies between runs.

## Relevance to SOL perpetuals at minutes to hours
The three-window design and the cost term inside the fitness function transfer directly. The break-even cost of 0.18% one-way on rules trading 14 to 42 times a year shows how thin an evolved edge is; a bot trading SOL several times a day pays that cost in a week. The volatility-timing behavior is the part that replicated across periods and is worth testing on its own.

## Caveats
I read the 1995 working paper, a scan without a text layer, and viewed the abstract, method and main results pages only. The published 1999 version is generally cited as a negative result; I could not open it. One training window produces the positive result. Long-only daily equity index. A second note on this paper exists in `../../16-oscillators-technical-rules/notes/allen-1999-genetic-algorithms-technical-trading-rules.md`.
