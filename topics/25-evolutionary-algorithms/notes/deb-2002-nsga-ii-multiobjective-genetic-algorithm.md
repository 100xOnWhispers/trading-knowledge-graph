---
title: "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II"
authors: "Deb, Kalyanmoy; Pratap, Amrit; Agarwal, Sameer; Meyarivan, T."
year: 2002
venue: "IEEE Transactions on Evolutionary Computation 6(2), 182-197"
url: "https://sci2s.ugr.es/sites/default/files/files/Teaching/OtherPostGraduateCourses/Metaheuristicas/Deb_NSGAII.pdf"
pdf: "sources/25-evolutionary-algorithms/deb-2002-nsga-ii-multiobjective-genetic-algorithm.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "25-evolutionary-algorithms"
asset_class: "multi"
horizon: "n/a"
tags: "nsga-ii, multi-objective, pareto-front, crowding-distance, elitism, constraint-handling"
---

## Key insight
NSGA-II is the standard algorithm for optimizing several conflicting objectives at once without collapsing them into one weighted score. It returns a set of non-dominated solutions (a Pareto front) spread evenly across the trade-off, using a fast sorting procedure, elitism and a parameter-free diversity measure. It contains no finance; it is the method behind "optimize return, drawdown and turnover together" in trading-strategy search, and its successor NSGA-III is the default sampler in the Freqtrade crypto bot's optimizer.

## Method
Solution A dominates B when A is no worse on every objective and strictly better on at least one.

1. Fast non-dominated sort: rank the population into fronts (front 1 is dominated by nobody, front 2 only by front 1, and so on) in O(M N^2) operations for M objectives and population N, against O(M N^3) for the original NSGA.
2. Crowding distance: within a front, sort by each objective and assign each solution the sum of the normalized gaps between its two neighbors; boundary solutions get infinite distance. Larger distance means a less crowded region. No sharing parameter is needed.
3. Selection: binary tournament preferring lower front rank, then larger crowding distance.
4. Elitism: merge parents and offspring (size 2N), sort into fronts, and fill the next population front by front, cutting the last admitted front by crowding distance.
5. Constraints: a feasible solution beats an infeasible one; between two infeasible solutions the smaller total violation wins; between two feasible ones, ordinary dominance applies.

## Data and sample
Nine unconstrained two-objective test problems and several constrained ones, including a five-objective, seven-constraint problem. Runs use a maximum of 25,000 function evaluations (250 generations in the main comparisons), in real-coded and binary-coded variants.

## Reported results
On most test problems NSGA-II found a better spread of solutions and better convergence to the true Pareto front than the two other elitist algorithms compared, PAES and SPEA. The constrained version outperformed another constrained multi-objective optimizer on the constrained set. The paper notes that problems with strong interactions between parameters remain hard.

## Signal construction
Not a signal. For strategy search, each candidate (a parameter vector or a rule) is scored on several objectives, for example net return, maximum drawdown, turnover or fees paid, and number of trades. Constraints carry the hard requirements: a minimum trade count, a leverage cap, a maximum time in position. The output is a front; the user then picks a region of it, not a single optimum.

## Relevance to SOL perpetuals at minutes to hours
Two uses are worth having. First, a turnover objective makes the cost-sensitivity of every candidate visible instead of burying it in a single net figure. Second, the shape of the front is a diagnostic: a front where a small step in turnover or parameter value produces a jump in return indicates fitting to noise, while a smooth front indicates a real trade-off. Kalshi's low leverage cap and 8-hour funding can be written as constraints.

## Caveats
The algorithm optimizes whatever sample it is given. Every point on an in-sample Pareto front is a selected maximum, and a front has many more points than a single-objective search has winners, so the multiple-testing burden rises. Crowding distance loses discriminating power beyond about three objectives, which motivated NSGA-III (a point from general knowledge, not from this paper). No evidence here on financial data. The PDF is a copy on a University of Granada teaching page.
