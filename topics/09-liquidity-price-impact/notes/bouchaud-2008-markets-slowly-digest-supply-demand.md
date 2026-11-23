---
title: "How markets slowly digest changes in supply and demand"
authors: "Bouchaud, Jean-Philippe; Farmer, J. Doyne; Lillo, Fabrizio"
year: 2008
venue: "arXiv:0809.0822; published 2009 in Handbook of Financial Markets: Dynamics and Evolution"
url: "https://arxiv.org/pdf/0809.0822"
pdf: "sources/09-liquidity-price-impact/bouchaud-2008-markets-slowly-digest-supply-demand.pdf"
access: "full-text"
source_type: "book"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "equities"
horizon: "tick"
tags: "price-impact, propagator, long-memory, order-flow, transient-impact, spread-volatility"
---

## Key insight
Visible liquidity is tiny compared with what investors want to trade, so large orders are split and executed over long periods. This makes the sign of order flow a long-memory process. For prices to stay close to unpredictable, the impact of each trade must be transient and liquidity must adapt asymmetrically to the flow. The review argues that most price movement comes from supply and demand itself, not from external news.

## Method
A 111-page review of empirical work on equities (London, Paris, New York) and of the models built on it. The core model is the transient-impact "propagator":

m_n = sum over past trades j of G0(n - j) * sign_j + noise

where G0(l) is the "bare" impact of one trade after l trades. If the sign autocorrelation decays as l^(-gamma) with gamma < 1, the price is diffusive only if G0 decays as l^(-beta) with beta = (1 - gamma)/2. The review shows that this is equivalent to a model where impact is permanent but depends on how predictable the order was (asymmetric liquidity). It also covers concave impact of single trades, hidden-order (metaorder) impact, and the relation between spread, impact and volatility per trade.

## Data and sample
Secondary: the review draws on trade and quote data and exchange-membership-coded data from the London, Paris and Spanish stock exchanges and the NYSE. No new sample.

## Reported results
- The outstanding volume in the book is of the order of 1% of daily traded volume, while daily volume is roughly 0.1% to 1% of market capitalization.
- Order-sign long memory was found in every stock examined. On the London Stock Exchange the Hurst exponent was about H = 0.7, that is gamma = 0.6; the NYSE range for gamma is 0.2 to 0.7.
- Impact is concave in volume in all markets studied, including anonymous ones.
- Empirically extracted G0(l) decays as a power law.
- Volatility per trade is proportional to the bid-ask spread, and isolated market orders cost about half the spread on average.

## Signal construction
Not a signal in itself. It supplies three building blocks for a bot:
1. A propagator-weighted order-flow feature: sum of recent signed volume weighted by a decaying kernel, for example (age + s0)^(-beta) with beta near 0.2 to 0.4, re-fitted on SOL data.
2. A surprise decomposition: predict the next trade sign from past signs, and treat only the unexpected part as price-moving.
3. A sanity relation: spread should scale with volatility per trade. A venue where the spread is far wider than that relation implies is expensive to cross.

## Relevance to SOL perpetuals at minutes to hours
The framework is venue-agnostic, and Donier and Bonart (2015) later confirmed the main impact law on Bitcoin. For a taker on a thin venue the message is that visible depth understates true liquidity over hours, but overstates it over seconds. The long-memory exponent, the kernel decay and the spread-volatility ratio all need to be estimated on SOL perp data from the large venues. Crypto perps add forced flow (liquidations) that the review does not treat.

## Caveats
A review by authors who built much of the framework; competing information-based views get critical treatment. The data are equities before 2008, with tick sizes and market-maker structures unlike crypto. The parameter values quoted are not transferable without re-estimation.
