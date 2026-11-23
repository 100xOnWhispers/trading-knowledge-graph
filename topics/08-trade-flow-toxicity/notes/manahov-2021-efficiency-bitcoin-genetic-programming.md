---
title: "The efficiency of Bitcoin: A strongly typed genetic programming approach to smart electronic Bitcoin markets"
authors: "Manahov, Viktor; Urquhart, Andrew"
year: 2021
venue: "International Review of Financial Analysis 73, 101629 (read: accepted version from the University of Reading repository)"
url: "https://centaur.reading.ac.uk/93822/1/The%20Efficiency%20of%20Bitcoin-revised.pdf"
pdf: "sources/08-trade-flow-toxicity/manahov-2021-efficiency-bitcoin-genetic-programming.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "minutes"
tags: "evolutionary-algorithms, genetic-programming, agent-based, market-efficiency, bitcoin, high-frequency"
---

## Key insight
An artificial Bitcoin market populated by traders whose rules evolve by strongly typed genetic programming (STGP) on real one-minute and five-minute Bitstamp prices produces return series that pass efficiency tests at one minute but fail them at five minutes. Markets populated by zero-intelligence (random) traders fail at both frequencies. The paper is evidence about evolutionary methods as a modelling tool and about where intraday Bitcoin predictability sits, not a test of an evolved trading strategy on trade-flow features.

## Method
Four artificial markets are simulated: high-frequency traders with evolving rules at one-minute and five-minute frequency, and zero-intelligence traders at the same two frequencies. Each trader holds a rule represented as a typed expression tree over price and volume functions that outputs a desired position and a limit price. Rules start random. Fitness is a trailing "breeding fitness return" on wealth; poor performers are replaced by offspring created by crossover and mutation. Listed settings include 100,000 traders, initial wealth of 100,000 USD each, maximum genome depth 20, parent selection 5%, mutation probability 10% per offspring, and a minimum breeding age of 80 quotes. A clearing mechanism sets price from the traders' limit orders. The simulated return series are tested with BDS, ARCH and Kaplan nonlinearity tests, the Hurst exponent, Ljung-Box and runs tests.

## Data and sample
Bitstamp BTC one-minute and five-minute data from bitcoincharts.com, 1 January 2015 to 3 August 2020 (timestamp, volume, price).

## Reported results
- Markets populated by evolving high-frequency traders are efficient at the one-minute frequency and inefficient at the five-minute frequency.
- Zero-intelligence traders show "strong and significant evidence against market efficiency" at both frequencies, which the authors read as evidence against the Hayek hypothesis that markets can be efficient with unintelligent traders.
- Returns show anti-persistence, with Hurst exponents below 0.45 reported for some series (the series this applies to should be checked in the paper's tables).
- An example evolved rule buys when the average price over the past interval is above the current price and current volume is below 500, the volume condition acting as a guard against sweep risk.

## Signal construction
Not a signal. As a method for a bot it suggests one specific use of genetic programming: evolve small typed expression trees over a fixed set of primitives (lagged returns, moving averages, volume, and in this topic's context signed taker volume and imbalance ratios) with a fitness function measured on a rolling recent window and hard limits on tree depth. Any rule found this way needs the out-of-sample and cost tests that this paper does not provide.

## Relevance to SOL perpetuals at minutes to hours
The five-minute versus one-minute result is at least consistent with other notes that find exploitable structure at 15 minutes to hours and little at the finest clock-time bars ([kim-2026-quarter-hour-effect-crypto-futures](kim-2026-quarter-hour-effect-crypto-futures.md), [kitron-2026-short-horizon-mean-reversion-crypto](kitron-2026-short-horizon-mean-reversion-crypto.md)). Beyond that, transfer is limited: the tests are run on simulated market output, the inputs are price and volume only with no signed flow, and no evolved rule is evaluated as a trading strategy on held-out real data.

## Caveats
Peer-reviewed, but graded C for this repository's purpose because the evidence is simulation-based and gives no out-of-sample trading result or cost analysis. Spot BTC on one exchange. Conclusions depend on the artificial clearing mechanism and STGP settings. The paper's stated practical implication is "behaviour-based market profiling", not strategy discovery.
