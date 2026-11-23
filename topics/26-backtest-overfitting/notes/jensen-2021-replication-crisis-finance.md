---
title: "Is There a Replication Crisis in Finance?"
authors: "Jensen, Theis Ingerslev; Kelly, Bryan T.; Pedersen, Lasse Heje"
year: 2021
venue: "NBER Working Paper 28432 (published in Journal of Finance, 2023)"
url: "https://www.nber.org/system/files/working_papers/w28432/w28432.pdf"
pdf: "sources/26-backtest-overfitting/jensen-2021-replication-crisis-finance.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "equities"
horizon: "multi-day"
tags: "replication, bayesian-shrinkage, multiple-testing, factor-zoo, out-of-sample"
---

## Key insight
The claim that most published return predictors are false discoveries is overstated. With a Bayesian hierarchical model that shrinks alphas toward zero and pools information across related factors and countries, the authors find that the majority of factors replicate, hold up out of sample in global data, and that the large number of related factors strengthens the evidence. Post-publication attenuation is what a rational Bayesian should expect, not proof of a replication failure.

## Method
A Bayesian model of factor alphas with a zero-alpha prior and a hierarchical structure: factors belong to themes, and themes share information across regions. The posterior alpha of a factor is shrunk toward zero and toward its cluster, which controls the false discovery rate without the conservatism of Bonferroni-style corrections. A factor "replicates" if its posterior alpha is reliably positive. The authors decompose the gap between their replication rate and that of Hou, Xue and Zhang (2020) into sample length, factor construction choices, weighting scheme and the testing method. Factors are clustered into 13 themes.

## Data and sample
153 factors across 93 countries in a new global dataset; US sample as the baseline. Capped value-weighted long-short portfolios; alphas measured against the CAPM.

## Reported results
- Baseline US replication rate (raw-return t-tests): 56.9%, already above Hou, Xue and Zhang because of a longer sample (+4.3%), construction choices (+4.0%) and capped value weights (+8.5%).
- Excluding factors the original studies themselves found insignificant: 64.7%.
- CAPM alphas: the text gives 84.9% at this step.
- Bayesian multiple-testing model, US: 84.0%. Global data with the Bayesian model: 84.9%.
- A conventional Benjamini-Yekutieli correction applied to the OLS alpha tests lowers the rate to 77.3%, below the Bayesian model's 84.0%. A footnote gives 77.3% as the final global Bayesian rate when straight (uncapped) value weights are used.
- More than 75% replication in 10 of the 13 themes.
- Factors with higher in-sample alpha have higher out-of-sample alpha on average; a positive but attenuated post-publication alpha is the expected outcome under the model.
- The paper quotes another study finding that the United States is the only country with a reliable post-publication decline in long-short returns.

## Signal construction
Not a signal. It motivates a shrinkage approach to candidate edges in place of accept/reject thresholds: treat each backtest estimate as a noisy observation, shrink it toward zero by an amount set by its standard error and toward the mean of its family of related signals, and size on the posterior mean. A signal confirmed on several related instruments or venues earns less shrinkage.

## Relevance to SOL perpetuals at minutes to hours
Two transferable ideas. First, correlated confirmations count: an order-flow signal that works on BTC, ETH and SOL perpetuals across Binance, Bybit and Hyperliquid is better evidence than one that works on SOL alone, and a hierarchical model credits that without pretending the tests are independent. Second, the appropriate response to multiplicity is to shrink the expected edge, which feeds position sizing directly, not only to veto. What does not transfer is the reassuring replication rate itself: it concerns decades of monthly equity data and economically motivated factors, not short intraday samples searched by optimizers.

## Caveats
"Replication" here means statistical reliability of alpha before costs; it does not show that factors are profitable to trade. The prior and the cluster structure are modelling choices, and a zero-mean prior with a fitted variance can be too lenient if the population of tried-but-unpublished factors is much larger than the observed one, which is the objection of the multiple-testing school. The title page carries a disclaimer about AQR Capital Management and notes that at least one co-author has disclosed additional relationships of potential relevance, so an asset-manager interest in factor investing should be kept in mind. The working-paper version was read; numbers in the journal version may differ.
