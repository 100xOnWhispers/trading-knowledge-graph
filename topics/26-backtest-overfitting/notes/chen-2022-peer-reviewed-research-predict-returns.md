---
title: "Does Peer-Reviewed Research Help Predict Stock Returns?"
authors: "Chen, Andrew Y.; Lopez-Lira, Alejandro; Zimmermann, Tom"
year: 2022
venue: "arXiv preprint 2212.10317 (first posted December 2022; v7, December 2025)"
url: "https://arxiv.org/pdf/2212.10317"
pdf: "sources/26-backtest-overfitting/chen-2022-peer-reviewed-research-predict-returns.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "26-backtest-overfitting"
asset_class: "equities"
horizon: "multi-day"
tags: "data-mining, alpha-decay, post-sample, theory-versus-empirics, anomalies"
---

## Key insight
Naive data mining with a simple t-statistic filter produces out-of-sample predictability about as good as the peer-reviewed literature. Both retain roughly half of their in-sample performance after the original sample ends. Economic theory attached to a predictor, including risk-based and equilibrium-model explanations, does not improve post-sample survival. This challenges the common prescription that an ex-ante economic story is the main defence against overfitting.

## Method
The authors generate 29,315 accounting-ratio signals from 242 "ingredient" variables (241 Compustat annual variables plus CRSP market equity) using two functional forms: simple ratios and scaled first differences. Each June, signals are sorted into five bins by their mean long-short return over the past 30 years, and the mean return over the following year is recorded. For comparison with published predictors (the Chen-Zimmermann dataset of more than 200), data-mined benchmarks are matched on sample period and in-sample t-statistic above 2.0, then tracked in event time after the original sample ends. Published papers are hand-classified by explanation (risk, mispricing, agnostic), modelling approach, discipline and journal rank.

## Data and sample
US equities, CRSP and Compustat, 1963 onward; published predictors from the Chen-Zimmermann open dataset.

## Reported results
- For both peer-reviewed and data-mined predictors, about 50% of predictability remains after the original sample periods; data-mined returns decay slightly more, and the data-mined benchmark is within one standard error of published predictors.
- Equal-weighted extreme bin: −59 basis points per month in-sample (average t-statistic −4.2) and −47 basis points out-of-sample, a decay of only 20%; the opposite extreme bin decays by 32%.
- Mining the 1963 to 1980 sample surfaces themes later published (investment, issuance, accruals, inventory growth, earnings surprise); decay of the top data-mined numerators in 1981 to 2004 is on average zero.
- Peer review attributes 60% of findings to mispricing, 20% to risk, and is agnostic for 20%; 15% are backed by an equilibrium model.
- Of 11 research categories, only theory-agnostic research shows consistent outperformance over data mining: 31 percentage points more retained performance in factor-adjusted alpha, falling to 9 when raw long-short returns are used. The authors say this should be shrunk toward zero for multiple comparisons.
- Predictors attributed to risk also decay post-sample.

## Signal construction
Not a signal. It is evidence about research process. Systematic enumeration of a predefined signal space, a t-statistic filter, and a rolling out-of-sample check is a legitimate discovery method, provided the expected edge is haircut by about half and the in-sample ranking is used as a relative guide, since out-of-sample returns rose monotonically with in-sample returns.

## Relevance to SOL perpetuals at minutes to hours
This is the strongest counterweight in the folder to the "theory first, never mine" doctrine, and it bears on whether machine-driven discovery (feature enumeration, genetic programming, automated machine learning) can be trusted. The answer it supports: yes, about as much as human research, with the same 50% haircut, if the search space is fixed in advance and evaluation is strictly rolling. What does not transfer: the sample is 60 years of monthly cross-sectional equity data with thousands of stocks per period. A single-instrument intraday crypto search has far less independent information per signal, so mined results there are more fragile than this paper would suggest.

## Caveats
Working paper, though long-circulated and with public code. Returns are before trading costs. The mined space is restricted to accounting ratios with simple functional forms; flexible nonlinear searches are a different regime. "Half remains" is an average; dispersion across predictors is large. Equity anomaly evidence does not establish anything about intraday crypto.
