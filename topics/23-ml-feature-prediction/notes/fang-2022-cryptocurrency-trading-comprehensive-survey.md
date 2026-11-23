---
title: "Cryptocurrency Trading: A Comprehensive Survey"
authors: "Fang, Fan; Ventre, Carmine; Basios, Michail; Kanthan, Leslie; Martinez-Rego, David; Wu, Fan; Li, Lingbo"
year: 2022
venue: "arXiv:2003.11352v5 (January 2022); a journal version in Financial Innovation is widely cited but was not confirmed in this session"
url: "https://arxiv.org/pdf/2003.11352"
pdf: "sources/23-ml-feature-prediction/fang-2022-cryptocurrency-trading-comprehensive-survey.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "n/a"
tags: "survey, machine-learning, lstm, random-forest, technical-indicators, literature-map"
---

## Key insight
A map of 146 papers on cryptocurrency trading up to about 2021. For this topic its value is the catalogue of supervised-learning studies and what it shows by accumulation: most work compares classifiers on technical-indicator features, findings on which model is best contradict one another from paper to paper, and few studies report costs. Machine-learning papers were only 13.7% of the surveyed literature, with LSTM, RNN and GRU the most common family.

## Method
Keyword searches on Google Scholar and publisher databases plus snowballing, yielding 146 papers grouped into trading systems, bubbles and extreme conditions, volatility and return prediction, portfolio construction, technical trading and others. The authors summarise each paper's data, method and stated result; they do not re-run or re-grade any study. They report that more than 85% of the papers appeared since 2018.

## Data and sample
Literature review. Tables list the datasets used by the surveyed papers (market data, sentiment data, others) with resolution and time range. Bitcoin is the most commonly studied asset.

## Reported results
Summaries the survey gives of individual supervised-learning studies (as described by the survey, not verified against the originals):
- Nakano et al.: neural network on 15-minute bitcoin bars with technical indicators (EMA, RSI and others); using several indicators "possibly prevents over-fitting" and beat buy-and-hold.
- Sun et al.: random forest on formulaic "101 alphas" factors with 5-minute data; accuracy rose with the amount of data, and a few alphas dominated importance.
- Vo et al.: random forest on minute data, effective despite multicollinear features.
- Madan et al.: random forest and generalized linear models on daily, 10-minute and 10-second bitcoin data; 10-minute data gave better sensitivity and specificity than 10-second data.
- A study the survey cites as Maryna et al.: a support vector machine strategy ranked fourth of five benchmark strategies, attributed to overfitting from many parameters.
- Zheng et al.: a fully connected network outperformed LSTM on daily prices; Kwon et al.: LSTM beat gradient boosting by about 7% F1 on 10-minute prediction. The two conclusions conflict.
- Samuel et al.: a vector autoregression had "phenomenal" test performance while a ten-layer RNN performed poorly.
- Fan et al.: a universal model across pairs beat pair-specific models, and "walkthrough" retraining when the model degrades improved accuracy.
- Attanasio et al. and Livieris et al.: combinations of classifiers were more reliable than single models.
The survey lists long-and-short-term trading research and sentiment-based research among open opportunities.

## Signal construction
Not a signal. Use it as an index to locate primary studies by feature type, model family and data frequency, then read and grade the originals.

## Relevance to SOL perpetuals at minutes to hours
Useful as background and as a list of candidate designs at 5 to 15 minute frequency (formulaic alphas with random forest, technical-indicator networks, universal cross-pair models with retraining on degradation). It predates perpetual-futures-specific features: funding, open interest and liquidations are essentially absent, as is Solana. Nothing in it is specific to regulated US venues.

## Caveats
Descriptive, not evaluative: the survey repeats each paper's own claims without checking for look-ahead, costs or sample size, and many of the cited studies are small conference papers or theses. Coverage ends before the 2022 to 2026 literature on transformers, foundation models and perp data. Some citations in the text are by first name, which makes tracing harder.
