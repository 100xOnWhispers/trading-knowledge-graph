---
title: "The Cost of Latency in High-Frequency Trading"
authors: "Moallemi, Ciamac C.; Saglam, Mehmet"
year: 2013
venue: "Author manuscript, revision of February 5, 2013 (later journal publication not confirmed in this session)"
url: "https://moallemi.com/ciamac/papers/latency-2009.pdf"
pdf: "sources/27-execution-risk-management/moallemi-2013-cost-of-latency-high-frequency-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "seconds"
tags: "latency, limit-orders, cost-of-immediacy, pegging, execution-cost"
---

## Key insight
Latency has a price even for a trader who is not racing anyone. A trader working a limit order cannot keep it pegged to a moving market if there is a delay between decision and execution, so the order must be priced more conservatively, and the lost value has a closed form. The cost depends on one ratio: how far price typically moves during the delay, relative to the bid-offer spread.

## Method
A risk-neutral trader must sell one share over a short horizon, choosing between limit and market orders. The bid follows a Brownian motion with volatility `sigma`; impatient buyers arrive at random and pay up to a premium `delta` (interpreted as the bid-offer spread) over the bid. Without latency the optimal policy is to peg the limit order at a constant spread above the bid. With latency `dt` between decision and effect, the trader shades the limit price down as a safety margin. Dynamic programming gives the value lost. "Latency cost" is defined as that loss as a fraction of the cost of immediacy (the premium a patient seller earns over an impatient one). As `dt` goes to zero:

`latency cost ~ (sigma * sqrt(dt) / delta) * sqrt( log( delta^2 / (2 * pi * sigma^2 * dt) ) )`.

## Data and sample
Calibration example: Goldman Sachs stock on January 4, 2010 (price $170.00, spread $0.058 or 3.4 bp, 12.03 market-order arrivals per minute, daily volatility $1.92). Historical study: NYSE common stocks, 1995 to 2005, at a fixed latency of 500 ms.

## Reported results
- For the Goldman Sachs example, latency cost falls from approximately 20% of the cost of immediacy at 500 ms to 5% at 5 ms.
- With 500 ms latency the limit price adjustment reaches about `1.4 * sigma * sqrt(dt)`.
- The marginal benefit of cutting latency increases as latency approaches zero.
- Median latency cost at a human time scale across NYSE stocks roughly tripled from 1995 to 2005; implied latency (the latency at which cost is 10% of immediacy cost) fell by about two orders of magnitude.
- Going from 500 ms to under 1 ms is worth approximately $0.0015 to $0.0025 per share, comparable to commissions and exchange fees paid by cost-efficient institutions.

## Signal construction
Not a signal; a sizing tool for engineering effort. Inputs: mid-price volatility per second `sigma`, quoted spread `delta` in the same units, and the bot's measured round-trip latency `dt` (decision to acknowledgement). Compute the ratio `sigma * sqrt(dt) / delta` and the formula above. If the result is a small fraction, latency work has low priority; if it approaches the formula's range of validity (ratio no longer small), passive orders are effectively stale on arrival and the bot should either cross or quote wider.

## Relevance to SOL perpetuals at minutes to hours
An illustrative calculation with the topic 06 snapshot figures (one-minute volatility 8.3 bp, median spread 4.5 bp; my arithmetic, assuming independent seconds): per-second volatility is about 1.07 bp. At 500 ms latency the ratio is about 0.17 and the formula gives roughly 0.22; at 100 ms roughly 0.14. So on this venue's current spread, a retail-grade connection gives up on the order of a fifth of the benefit of quoting passively, which is material but not prohibitive for a bot whose edge is at minutes to hours. The cost rises in volatile periods, exactly when the bot is most likely to be trading. One could argue that the spread in the formula stands for the value of passive execution, which on Kalshi also includes the 10 bp maker-taker fee gap at the entry retail tier; on that reading the effective ratio is smaller and latency matters less still. That reading is mine, not the paper's.

## Caveats
Stylised: one share, risk-neutral, Brownian price, no queue position, no adverse selection from informed takers, no fees. The asymptotic formula is valid only for small latency relative to spread. Equity calibration from 1995 to 2010. The model prices the trader's own staleness, not the cost of being picked off by faster traders, which Albers et al. measure directly. Manuscript version read.
