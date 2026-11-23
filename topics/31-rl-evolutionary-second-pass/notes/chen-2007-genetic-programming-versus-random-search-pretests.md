---
title: "Failure of Genetic-Programming Induced Trading Strategies: Distinguishing between Efficient Markets and Inefficient Algorithms"
authors: "Chen, Shu-Heng; Navet, Nicolas"
year: 2007
venue: "Book chapter, Springer (author copy; volume title not confirmed from the PDF)"
url: "https://nicolas.navet.eu/publi/SHC_NN_Springer2007.pdf"
pdf: "sources/31-rl-evolutionary-second-pass/chen-2007-genetic-programming-versus-random-search-pretests.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "daily"
tags: "genetic-programming, random-search, equal-budget, head-to-head, lottery-trading, pretest, baselines"
---

## Key insight
Before crediting an evolutionary search with a discovery, compare it with two nulls that cost almost nothing: random search given the same number of distinct candidates, and random trading with the same trade frequency and time in the market. In nine index-period experiments genetic programming beat equal-budget random search in only three, and wherever GP beat random trading, random search usually did too. Buy-and-hold is a poor benchmark because it is the best strategy in a rising market and the worst in a falling one by construction.

## Method
- Equal search intensity: two searches are equivalent if they evaluate the same number of syntactically distinct strategies on the training data. GP with population 500 over 100 generations corresponds to about 50,000 random strategies, drawn from the same function and terminal set (the GP run stopped at generation zero with an enlarged population).
- Pretest 1: GP against equal-intensity random search, both with training and validation stages.
- Pretest 3: random strategies applied out of sample with no selection at all.
- Pretest 4: GP against "lottery trading", random long/flat decisions constrained to match GP's expected number of transactions (frequency) and share of periods in the market (intensity).
- Pretest 5: equal-intensity random search against lottery trading.
- Reading the outcomes: neither GP nor random search beats lottery trading means there is nothing to learn from this training data; both beat it means there is; random search beats it but GP does not means GP is overfitting; GP must also beat random search before its operators can be said to add anything.
- Statistics: Student's t-test at 95% on 50 GP runs, 50 random-search runs and 100 lottery runs per market.

## Data and sample
Three stock indices (TSE 300 of Canada, the Nikkei, and Taiwan's capitalization-weighted index), daily, normalized by a 250-day moving average. Three out-of-sample periods each (1999-2000, 2001-2002, 2003-2004), preceded by 3 years of validation and 3 of training. Short selling allowed.

## Reported results
- 4 of 9 markets: evidence of something to learn (both GP and random search beat lottery trading).
- 3 of 9: nothing to learn (neither beats lottery trading).
- 2 of 9: GP beats lottery trading but random search does not.
- GP beat equal-intensity random search with significance in 3 of 9 markets; random search never beat GP with significance.
- In two rising markets where GP passed the pretests it returned 5% and -4% while buy-and-hold made more than 30%.
- The authors conclude their GP "may only be able to take advantage of simple regularities".

## Signal construction
Not a signal. Two baselines to compute for every search the project runs: (1) draw as many random candidates from the same rule grammar or parameter space as the optimizer evaluated, select the best on training and validation in the same way, and compare out of sample; (2) simulate random entries with the candidate's trade count and exposure share under the same costs.

## Relevance to SOL perpetuals at minutes to hours
Directly usable. Any genetic, Bayesian or LLM-driven search over SOL rules should be reported next to equal-budget random search and exposure-matched random trading on the same bars and fees. Because a SOL perp can be shorted and carries funding, the lottery baseline should match long share, short share and turnover separately.

## Caveats
Daily index data from 1993 to 2004 and a single GP implementation. Nine market-period cells with a per-cell t-test and no correction across cells. Treatment of transaction costs in the experiments was not confirmed in the parts read. The equal-budget definition counts evaluations, not compute time. The pretests show whether search adds value over chance; passing them is, as the authors say, "far from implying profitability".
