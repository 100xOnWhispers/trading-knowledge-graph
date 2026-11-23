---
title: "Fluctuations and response in financial markets: the subtle nature of 'random' price changes"
authors: "Bouchaud, Jean-Philippe; Gefen, Yuval; Potters, Marc; Wyart, Matthieu"
year: 2004
venue: "arXiv cond-mat/0307332v2, August 2003 (journal version in Quantitative Finance, 2004; journal details not confirmed in this session)"
url: "https://arxiv.org/pdf/cond-mat/0307332"
pdf: "sources/08-trade-flow-toxicity/bouchaud-2004-fluctuations-response-financial-markets.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "08-trade-flow-toxicity"
asset_class: "equities"
horizon: "tick"
tags: "trade-sign-autocorrelation, propagator, transient-impact, informed-trading, market-orders"
---

## Key insight
Prices look like a random walk only because two opposing forces cancel: market-order signs are long-range correlated, which alone would make prices trend, while the impact of each trade decays over time as liquidity providers mean-revert the price. The paper formalizes this with a "propagator" model in which price is the sum of decaying impacts of all past signed trades. It also finds that the share of market orders that are informed in the sense of anticipating short-term moves by more than their cost is very small.

## Method
Price at trade n is modelled as p_n = sum over past trades n' of G0(n - n') * eps_n' * ln(V_n') plus noise, where eps is the trade sign, V the volume and G0 the bare impact of a single trade. Empirical objects: the sign autocorrelation C0(l) = <eps_n eps_{n+l}>, the response function R(l) = <(p_{n+l} - p_n) * eps_n>, and the price diffusion D(l). Requiring diffusive prices given a power-law C0(l) proportional to l^(-gamma) pins down the decay of G0(l) proportional to l^(-beta) with the critical value beta_c = (1 - gamma) / 2. The distribution of signed post-trade price moves is inspected for the skew that informed trading would create.

## Data and sample
Paris Bourse trades and quotes, 2001 and 2002, mainly France Telecom (about 2 million trades in 2002), with other French stocks and some British stocks for comparison.

## Reported results
- Sign autocorrelation decays as a power law with gamma about 1/5 for France Telecom (C0 about 0.2) and about 2/3 for Total; gamma below one in all cases.
- The response function R(l) for France Telecom rises by a factor of about 2 between l = 1 and l about 1000 trades, then decreases.
- Impact depends on volume very weakly (approximately logarithmically), so the sign matters more than the size.
- For France Telecom the diffusive condition gives beta_c about 2/5: the bare impact of a single trade must decay as a slow power law.
- The distribution of signed price changes after a trade, once shifted by half the spread, is nearly symmetric; the authors conclude one "can hardly detect the statistical presence of informed trades" that anticipate the short-term move enough to cover costs.

## Signal construction
A propagator-based fair-value adjustment. Inputs: the trade tape with aggressor signs. Estimate C0(l) and the response function R(l) for lags up to roughly 1000 trades, back out G0(l) (or fit beta with gamma), then compute the expected remaining price drift from past trades as the sum over past trades of [G0(l + h) - G0(l)] * eps * ln(V). Because G0 decays, this term predicts partial reversion of the impact of recent one-sided flow, offset by the expected continuation of that flow. Update on each trade or each second.

## Relevance to SOL perpetuals at minutes to hours
The framework gives a principled way to decide whether a burst of taker buying on Binance SOL perp should be faded or followed: it depends on whether realized flow exceeds what sign persistence predicted and on how fast impact decays on that venue. The weak size dependence suggests testing trade-count imbalance alongside volume imbalance. The "few trades are informed" result is a useful prior against reading every large print as smart money. Exponents must be re-estimated on SOL data; the consistency relation between gamma and beta is a check on the estimates.

## Caveats
Large-cap French equities in 2001 and 2002. Event time. No trading rule or cost test. A linear propagator ignores the order book state, so it overlaps with topics 07 and 09, which cover book imbalance and impact laws. Liquidation cascades in perps violate the stationary-response assumption.
