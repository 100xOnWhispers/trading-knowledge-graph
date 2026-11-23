---
title: "Essays in cryptocurrencies' forecasting and trading with technical analysis and advanced machine learning methods"
authors: "Wei, Mingzhe"
year: 2022
venue: "PhD thesis, University of Glasgow"
url: "https://theses.gla.ac.uk/82986/1/2021WeiMingzhePhD.pdf"
pdf: "sources/16-oscillators-technical-rules/wei-2022-crypto-technical-analysis-lucky-factors.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "daily"
tags: "crypto, data-snooping, lucky-factors, moving-average, machine-learning, gradient-boosting, sentiment"
---

## Key insight
A crypto study that reaches the opposite conclusion from Hudson and Urquhart using the same kind of rule universe. The top technical rules beat buy-and-hold in sample across six coins and an index, but a bootstrap test for "lucky" factors finds that none of the top performers has genuine predictive power, and significance in early periods does not persist. A later chapter finds that gradient-boosted tree models combining many inputs outperform the best single predictor.

## Method
Three empirical chapters; I read the abstract, the Chapter 3 introduction, part of its results and its conclusion, and only the abstract-level description of Chapters 4 and 5.
- Chapter 3: the Sullivan, Timmermann and White rule universe (filters, moving averages, support and resistance, channel breakouts, on-balance volume) is run on each series. The fifteen best rules by Sharpe ratio and by Sortino ratio are then tested with the Harvey and Liu "Lucky Factors" procedure: orthogonalize candidate factors under the null, bootstrap, and test whether each adds explanatory power beyond a baseline.
- Chapter 4: a wider pool of predictors (blockchain data, technical indicators, online sentiment, conventional financial indicators), 8 August 2015 to 8 December 2018, with the same snooping control.
- Chapter 5: machine-learning models for Bitcoin, combined with narrative sentiment and volatility-based leverage rules, with forecasting ability checked under data-snooping control.

## Data and sample
Chapter 3: daily data for Bitcoin, Dash, Ethereum, Litecoin, Ripple, Stellar and the CRIX index, 2013 to 2018, from CoinMarketCap and the CRIX site, split into subperiods.

## Reported results
- Chapter 3: technical rules produce higher returns than buy-and-hold in every series. The best rules are short moving averages (for Bitcoin, a 1-day against 5-day MA with a fixed percentage band; altcoins favor 10 or 15-day MAs). The Lucky Factors test does not recognize genuine predictive power in the selected rules on either metric. Many rules are significant in the first two subperiods; only a few persist over the whole sample. The thesis states that the predictive power of technical rules "gradually disappears".
- Chapter 4 (abstract): most rules beat buy-and-hold, especially MA rules, but "this profitability may not be genuine but comes from data-snooping bias". One proposed indicator, a log-price to moving-average ratio, retains significant forecasting ability after the correction.
- Chapter 5 (abstract): machine-learning models consistently outperform the best individual model in forecasting ability and profitability, with the gradient-boosted decision tree family best.
- Transaction costs are not applied in Chapter 3; the author says fees vary too much across platforms to adopt a single measure.

## Signal construction
The one indicator that survives is the price-to-moving-average ratio: x_t = log(P_t) - log(MA_n(P)_t), used as a continuous predictor in a regression or tree model instead of as a crossover trigger. The window lengths used were not confirmed in my reading.

## Relevance to SOL perpetuals at minutes to hours
Two design points transfer. First, continuous distance-from-average features fed into a model held up better under snooping control than discrete crossover rules, which matches Detzel et al. Second, the same daily crypto data yields "technical rules work" or "technical rules are luck" depending on the multiple-testing method, so a bot's research process should fix the method in advance. All evidence here is daily and ends in 2018.

## Caveats
A thesis, not peer reviewed, with uneven exposition. The Lucky Factors method was built for cross-sectional factor selection and its use on single-asset timing rules is unusual; pre-selecting the top fifteen rules before testing also complicates interpretation. No costs in Chapter 3. Chapters 4 and 5 are reported from the abstract only, so the machine-learning result is not verified in detail here.
