---
title: "A reality check on trading rule performance in the cryptocurrency market: Machine learning vs. technical analysis"
authors: "Anghel, Dan-Gabriel"
year: 2021
venue: "Finance Research Letters 39, 101655"
url: "https://ideas.repec.org/a/eee/finlet/v39y2021ics1544612320304414.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "n/a"
tags: "crypto, machine-learning, reality-check, data-snooping, market-frictions, risk-premium, negative-result"
---

## Key insight
The main peer-reviewed negative result for crypto. When both machine-learning and technical-analysis trading rules are tested with a Reality Check that controls for data snooping, and market frictions are included, statistically significant positive excess returns are rarely achieved. What performance exists lines up with exposure to risk factors, suggesting the rules harvest risk premia more than they predict prices.

## Method
Only the abstract was read. It states that the paper investigates whether machine-learning and technical-analysis trading rules have superior predictive ability in the cryptocurrency market, using a reality-check approach that controls for data snooping and market frictions. Results are examined across sampling frequencies, position types and significance levels, and cross-sectional performance is related to risk factors. The specific models, rule universe, coins, period and cost levels are not given in the abstract.

## Data and sample
Not confirmed. The abstract refers to the cryptocurrency market and to several sampling frequencies without listing them.

## Reported results
From the abstract only:
- Statistically significant positive excess returns are rarely achieved, irrespective of sampling frequency, type of position, or significance level.
- Cross-sectional performance is correlated with risk factors such as beta and idiosyncratic volatility, which suggests the rules mostly capture market risk premiums.
- The author concludes that trading rules offer no clear advantage in crypto markets over traditional markets.

No numbers appear in the abstract. A later working paper I read (Mroziewicz and Ślepaczuk) summarizes this study the same way: rare significant returns once the Reality Check is applied.

## Signal construction
Not a signal. It supplies two checks:
1. Run the Reality Check (or SPA) over the union of machine-learning models and technical rules, not over each family separately, so that the model search is part of the tested universe.
2. Regress strategy returns on the asset's own return and on volatility to see whether the "alpha" is leveraged beta or a volatility premium.

## Relevance to SOL perpetuals at minutes to hours
The second check matters for a perp bot. A long-biased SOL rule in a rising market, or a mean-reversion rule that is implicitly short volatility, will look profitable without any forecasting skill. Benchmarking each rule against a random-entry strategy with the same average exposure and holding time is the simplest guard. The claim that machine learning does not rescue technical inputs also sets a prior for the reinforcement-learning and boosted-tree approaches noted elsewhere in this folder: the model class is unlikely to be the source of an edge.

## Caveats
Abstract-only, so the strength of the result cannot be assessed: the Reality Check is conservative and a universe padded with poor rules will rarely reject. It is not known from the abstract whether intraday frequencies below one hour were included or what frictions were assumed. Bakker and Hudson and Urquhart, using stepwise or FDR methods, find more survivors, so part of the disagreement is the test, not the data.
