---
title: "The predictive power of public Twitter sentiment for forecasting cryptocurrency prices"
authors: "Kraaijeveld, Olivier; De Smedt, Johannes"
year: 2020
venue: "Journal of International Financial Markets, Institutions and Money (peer-reviewed version from Edinburgh Research Explorer)"
url: "https://www.pure.ed.ac.uk/ws/files/138685006/INTFIN_2018_414_R2.pdf"
pdf: "sources/18-positioning-sentiment/kraaijeveld-2020-predictive-power-twitter-sentiment-crypto.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "hours"
tags: "twitter-sentiment, vader, bullishness-ratio, granger-causality, altcoins, bots, hourly"
---

## Key insight
Across nine large coins, lexicon-based Twitter sentiment has some daily predictive power for a minority (Bitcoin, Bitcoin Cash, Litecoin), while at the hourly level the dominant direction runs from price to tweets. For most coins and lags, Twitter reacts to the market. The authors also estimate that 1% to 14% of tweets per coin came from bot accounts, and say the true share is likely higher.

## Method
Tweets are scored with VADER, extended by the Loughran-McDonald finance word list and a hand-made lexicon of 63 crypto terms. Scores are averaged into daily and hourly series. Three predictors are built per coin: mean sentiment, a bullishness ratio (following Antweiler and Frank 2004, based on counts of positive and negative tweets), and message volume. Bilateral Granger causality is tested against price returns and trading volume, using the Toda-Yamamoto procedure for non-stationary series and the standard test for stationary ones, with Johansen cointegration as a cross-check. Bots are flagged by six heuristics (giveaway wording, referral requests, account-follow patterns and similar); a tweet counts as bot-posted if it meets two.

## Data and sample
24,035,075 public tweets collected by live stream between 4 June 2018 and 4 August 2018 for Bitcoin, Ethereum, XRP, Bitcoin Cash, EOS, Litecoin, Cardano, Stellar and TRON. Daily and hourly prices from the CoinMarketCap API. The daily series have 61 observations per coin.

## Reported results
- Bitcoin: daily sentiment predicts returns over the past three days under the standard Granger test (p < 0.05) but not under Toda-Yamamoto. At the hourly interval no predictive power in either direction.
- Ethereum: no predictive power from sentiment; returns Granger-cause message volume at all intraday lags.
- XRP: message volume predicts returns at lags 4 and 5; hourly sentiment is an effect of returns.
- Bitcoin Cash: sentiment predicts returns at hourly lags 1 and 3, not daily.
- Litecoin: daily sentiment predicts returns for the first three lags; message volume predicts returns and volume.
- EOS and TRON: predictive power appears only through the bullishness ratio.
- Summary in the conclusion: sentiment and message volume are the stronger predictors at the daily level, while price returns are the strongest predictor variable at the intraday level.

## Signal construction
Inputs: stream of posts tagged with the asset. Per interval compute (a) mean VADER compound score with a crypto lexicon, (b) bullishness from positive and negative counts, (c) post count. Filter accounts matching bot heuristics before aggregation. The paper gives no trading rule; the features would enter a model as lagged regressors at 1 to 5 daily lags or 1 to 4 hourly lags.

## Relevance to SOL perpetuals at minutes to hours
This is one of few peer-reviewed tests at an hourly interval and across altcoins, and its hourly message is cautionary: expect sentiment to lag price. Results differ coin by coin, so nothing can be assumed for SOL (not in the sample) without a direct test. The bot share matters more for SOL, where promotional and memecoin posting is heavy.

## Caveats
Two months of data in a falling 2018 market; 61 daily points per coin; many coin-lag-variable combinations tested with no multiple-testing correction. The authors call the daily sample "close to suboptimal". No trading simulation or costs. Lexicon scores are unvalidated for crypto slang.
