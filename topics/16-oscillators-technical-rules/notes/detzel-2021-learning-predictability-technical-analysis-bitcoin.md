---
title: "Learning and predictability via technical analysis: Evidence from bitcoin and stocks with hard-to-value fundamentals"
authors: "Detzel, Andrew; Liu, Hong; Strauss, Jack; Zhou, Guofu; Zhu, Yingzi"
year: 2021
venue: "Financial Management 50(1), 107-137"
url: "https://ideas.repec.org/a/bla/finmgt/v50y2021i1p107-137.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "daily"
tags: "theory, rational-learning, moving-average, price-to-ma-ratio, bitcoin, hard-to-value-assets"
---

## Key insight
A theoretical reason for moving averages to work in crypto that does not require irrational traders. In an equilibrium model where investors learn about an asset whose fundamentals are hard to value, technical analysis arises endogenously, and the ratio of price to its moving average predicts returns. The prediction is confirmed for Bitcoin and for stock groups with similar valuation uncertainty.

## Method
Only the abstract was read. It describes an equilibrium model in which technical analysis emerges from rational learning, offered as a theoretical foundation for its use in practice. The empirical part tests whether ratios of prices to their moving averages forecast daily Bitcoin returns in sample and out of sample, builds trading strategies on those ratios, and repeats the exercise for stocks with hard-to-value fundamentals. Hudson and Urquhart, describing the working-paper version, say the rules use 5 to 100-day moving averages; Corbet et al. describe its scope as horizons of 1 to 20 weeks. Neither detail was confirmed in the paper itself.

## Data and sample
Bitcoin, daily returns; plus small-cap, young-firm and low-analyst-coverage stocks, and NASDAQ stocks during the dot-com era (per the abstract). Sample dates not confirmed.

## Reported results
From the abstract only:
- Ratios of prices to their moving averages forecast daily Bitcoin returns in sample and out of sample.
- Trading strategies based on these ratios generate an economically significant alpha and Sharpe ratio gains relative to buy-and-hold.
- Similar results hold for small-cap, young-firm and low-analyst-coverage stocks, and for NASDAQ stocks during the dot-com era.

No numerical values are given in the abstract.

## Signal construction
Price-to-moving-average ratio as a continuous predictor: x_t(L) = P_t / MA_L(P)_t for several windows L, used either in a predictive regression of next-period return on the set of ratios, or as a rule that is long when the ratio exceeds one. The windows and the exact regression specification were not read.

## Relevance to SOL perpetuals at minutes to hours
The theory makes a testable cross-sectional prediction that fits this project: trend signals should be stronger in assets whose value is harder to pin down, and should weaken as an asset matures. SOL is plausibly harder to value than Bitcoin, which agrees with Hudson and Urquhart's out-of-sample finding that altcoins kept their predictability when Bitcoin lost it. The mechanism is slow learning about fundamentals, so it speaks to daily and multi-day trend context for an intraday bot, not to minute-scale oscillators. A neighboring topic in this repository (time-series momentum) covers the factor interpretation.

## Caveats
Abstract-only. The evidence is daily and long-biased in a sample that includes Bitcoin's largest bull markets. A model that rationalizes moving averages does not show that the specific windows used in practice are optimal, nor that the effect survives fees at higher turnover. Whether transaction costs were included was not confirmed.
