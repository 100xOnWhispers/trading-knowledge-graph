---
title: "Dynamic trade execution: a grammatical evolution approach"
authors: "Cui, Wei; Brabazon, Anthony; O'Neill, Michael"
year: 2011
venue: "International Journal of Financial Markets and Derivatives, vol. 2, no. 1/2, pp. 4-31"
url: "https://ideas.repec.org/a/ids/ijfmkd/v2y2011i1-2p4-31.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "n/a"
tags: "evolutionary-algorithms, grammatical-evolution, optimal-execution, agent-based-simulation, trade-scheduling"
---

## Key insight
Execution strategies can be evolved instead of derived: a grammar defines the space of possible execution rules, an evolutionary search finds rules with low trading cost, and an agent-based artificial market supplies the test bed. According to the abstract, the evolved strategies beat a set of benchmark strategies in that artificial market. This is the main evolutionary-computation entry in the execution literature located in this session.

## Method
From the abstract only. Grammatical evolution is a form of genetic programming in which candidate solutions are generated from a formal grammar, so the evolved object is a readable rule (for example, conditions on market state that set order aggressiveness or slice size) and not a fixed-length parameter vector. The authors combine this "evolutionary methodology whereby we evolve high-quality trade execution strategies" with "an agent-based artificial stock market, wherein the evolved strategies are tested". The grammar, the fitness function (the abstract frames the objective as minimising total trading cost, balancing market impact against opportunity cost), population size, number of generations and the design of the artificial market were not read.

## Data and sample
Per the abstract, an agent-based artificial stock market; no real market data is mentioned. Whether any calibration to real order book data was done is not confirmed.

## Reported results
From the abstract only:
- "The evolved strategies are found to outperform a series of benchmark strategies".
- "Several avenues are suggested for future work".

No magnitudes, benchmark names or statistical tests were read. Page range and issue are taken from the RePEc record's identifier.

## Signal construction
Not a signal; a search method for execution rules. A version for the bot: define a small grammar over state variables (time left, fraction unfilled, spread, touch imbalance on Kalshi and on a reference venue, recent signed volume) and actions (rest at touch, improve by one tick, cross, cancel). Fitness is realised implementation shortfall including fees on recorded or simulated episodes. Evolve on one period, select on a second, report on a third. Keep rules short, and penalise length, so that the result can be inspected.

## Relevance to SOL perpetuals at minutes to hours
The appeal for this project is interpretability and small-data behaviour: an evolved rule of three or four conditions can be read, sanity-checked against the Albers et al. evidence, and compared with a hand-written submit-and-leave rule, which is harder to do with a neural policy. The weakness is the same one that affects reinforcement learning for execution, only more acute: the fitness evaluation depends on a simulator, and an evolutionary search will exploit any optimistic fill assumption in it. With five months of Kalshi history and many candidate rules, selection bias is severe (topic 26 covers the corrections). Evolution strategies as a gradient-free optimiser for the parameters of a fixed rule (offset, patience, cancel threshold) are a lower-risk use than evolving rule structure.

## Caveats
Abstract-only; the article is behind the publisher's paywall and no open copy was located without search access. Results come from an artificial market whose realism is unknown, so the "outperform" claim says little about live markets. No costs or fees are mentioned. Evolutionary methods for execution are thinly studied compared with reinforcement learning; no crypto application and no replication were found in this session. Grade C reflects the simulated setting and the limited access.
