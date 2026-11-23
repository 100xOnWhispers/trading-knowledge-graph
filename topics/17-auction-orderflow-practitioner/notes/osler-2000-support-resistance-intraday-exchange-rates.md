---
title: "Support for Resistance: Technical Analysis and Intraday Exchange Rates"
authors: "Osler, Carol"
year: 2000
venue: "FRBNY Economic Policy Review, 6(2), July 2000, pp. 53-68"
url: "https://www.newyorkfed.org/medialibrary/media/research/epr/00v06n2/0007osle.pdf"
pdf: "sources/17-auction-orderflow-practitioner/osler-2000-support-resistance-intraday-exchange-rates.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "17-auction-orderflow-practitioner"
asset_class: "fx"
horizon: "minutes"
tags: "support-resistance, round-numbers, bounce-frequency, bootstrap, placebo-levels, technical-analysis"
---

## Key insight
Support and resistance levels that six dealing firms actually published each morning predicted intraday trend interruptions better than randomly placed levels. The edge is real but small: about 4.6 percentage points of bounce frequency over a baseline that is itself well above 50%. It is the first rigorous test of the most widely used practitioner level concept, and it sets the standard design for testing any "level": compare against arbitrary levels, not against a coin flip.

## Method
A level is "hit" when the bid (for support) or ask (for resistance) comes within 0.01% of it. A "bounce" occurs if, fifteen minutes later, the bid is above the support level (the ask below the resistance level). Bounce frequency = bounces / hits. For each day 10,000 sets of artificial levels are drawn (twenty support, twenty resistance, uniformly within a range around the open set by that month's largest open-to-extreme gap, rounded to the same digits). For each of 28 months the published bounce frequency (BP) is compared with the average artificial one (BA); the number of months with BP > BA is tested against a binomial with p = 0.5. Thresholds of 0.00% and 0.02% and a second horizon were tried as sensitivity checks.

## Data and sample
Levels published daily by six firms (commercial banks, investment banks, news services), January 1996 to March 1998, for dollar-mark, dollar-yen and dollar-pound: about 23,700, 22,800 and 17,700 levels. Prices are Reuters indicative bid-ask quotes sampled each minute, 9 a.m. to 4 p.m. New York time.

## Reported results
- Bounce frequency at arbitrary levels: 56.2% on average. At published levels: 60.8%.
- Published beat arbitrary in all sixteen firm-currency pairs; significant at 5% for all but three.
- Excess bounce frequency: 4.2 points (mark), 5.6 (yen), 4.0 (pound). The best firm's yen levels beat arbitrary by 9.2 points; best and worst firms differ by 4.0 points on average.
- Predictive power lasted at least five business days after publication.
- No firm could rank its own levels by strength.
- Over 70% of levels end in 0 and 96% end in 0 or 5 (chance: 10% and 20%).
- Firms agree on only about 30% of possible level matches (within 5 points); about three-quarters of still-relevant levels are reused the next day.

## Signal construction
Build a level set L(t) from sources a discretionary trader would use (prior swing highs and lows, round numbers, prior-day extremes). On each first touch within a tolerance band, record a binary bounce label at a fixed horizon. Maintain in parallel K placebo level sets matched for distance from price. The live feature is not "price is at a level" but the rolling excess bounce rate of each level family over its placebo. That excess, with level type, age and touch count, is a natural input for a classifier or a contextual bandit that decides fade versus follow.

## Relevance to SOL perpetuals at minutes to hours
The horizon (15 minutes) and the 24-hour, quote-driven market make this the closest classical analogue to crypto perps. Two things transfer directly: the placebo design, and the warning that the unconditional bounce rate is far from 50% (56% here), so naive hit rates flatter every level method. What needs re-testing: whether algorithmically derived SOL levels have any excess at all, since the levels here embedded dealers' private order-book knowledge.

## Caveats
Indicative quotes, not trades. A bounce is not a profit: no spreads, stops or costs are modelled. The 1996-98 dealer market predates electronic trading. The firms had private order-flow information that a public-data bot lacks. The baseline above 50% reflects the bounce definition and short-horizon mean reversion.
