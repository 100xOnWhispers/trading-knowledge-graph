---
title: "Forecasting and trading cryptocurrencies with machine learning under changing market conditions"
authors: "Sebastiao, Helder; Godinho, Pedro"
year: 2021
venue: "Financial Innovation 7(1), article 3"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC7785332/"
pdf: "none"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "daily"
tags: "random-forest, svm, linear-model, ensemble-voting, model-agreement, transaction-costs, bear-market, on-chain-features"
---

## Key insight
Individual models (linear, random forest, support vector machine) forecast next-day returns of bitcoin, ethereum and litecoin poorly, with hit rates between 46% and 60% and several below 50%. Trading only when most models agree does much better: an ensemble that goes long when at least five of six models predict a rise earned positive returns after a 0.5% round-trip cost in ethereum and litecoin during a severe bear market. The gain comes from trading rarely, not from forecasting well.

## Method
Six models per coin: linear, random forest and support vector machine, each as a regression (next-day return) and as a classifier (up or down). The starting feature set has 50 variables: 31 trading variables, 12 blockchain variables and 7 day-of-week dummies, including lags 1 to 7 of all three coins' log returns, the lagged relative price range and Parkinson range volatility at lags 1 to 7. Non-stationary variables are first-differenced. Eighteen input sets were tried; for each model class the set and hyperparameters were chosen by average trading return in the validation block, not by forecast error. The sample is split by time into roughly 50% training (648 days), 25% validation (324 days) and 25% test (325 days, from 13 April 2018), with a rolling 648-day estimation window. Strategies are long-only: hold when at least 4, 5 or 6 of the 6 models forecast a rise, otherwise stay in cash. Results are shown with zero cost and with a 0.5% proportional round-trip cost.

## Data and sample
Daily data for bitcoin, ethereum and litecoin, 15 August 2015 to 3 March 2019, from CoinMarketCap (price, volume, market cap) and Coin Metrics (blockchain variables).

## Reported results
- Test-sample classification hit rates range from 46.15% (linear, bitcoin) to 60.00% (random forest, ethereum); regression hit rates from 46.46% to 59.69%. Five of 18 individual models are below 50%.
- Theil's U2 exceeds 100 for several models, meaning they do not beat the naive forecast.
- Ensemble 5, test sample: ethereum in the market 56 days (17.2%), win rate 60.71%, annualised return 44.65% gross and 9.62% after costs, Sharpe 80.17%; litecoin 53 days, win rate 50.94%, 34.86% gross and 5.73% net, Sharpe 91.35%; bitcoin 73 days, 5.87% gross and -23.66% net.
- Ensemble 6 for ethereum: 30 days in the market, 14.35% net, Sharpe 95.05%.
- Buy-and-hold over the test period lost about 55% (bitcoin), 77% (ethereum) and 66% (litecoin) annualised.
- Ensemble 5 maximum drawdowns were 28.92% (ethereum) and 23.46% (litecoin).

## Signal construction
Fit several structurally different models on the same rolling window and convert each to an up or down vote. Trade only when a supermajority agrees; stay flat otherwise. The vote count is the signal; the threshold sets the participation rate.

## Relevance to SOL perpetuals at minutes to hours
The transferable idea is model agreement as a trade filter under costs, which is the same economic logic as meta-labeling: weak forecasts become usable when most are discarded. On a perp the rule can be made symmetric (short when most models predict a fall), which the authors could not test. The specific features and the daily horizon do not transfer; the unanimity threshold and number of models need re-tuning on intraday data.

## Caveats
One test period of 325 days, with 30 to 73 trading days per strategy, so the Sharpe ratios rest on few observations. Selection on validation trading return is itself a search. Long-only in a falling market flatters "stay in cash" rules against buy-and-hold. The paper's conclusion names Ensemble 5 as best for ethereum although its own table shows Ensemble 6 ahead. No PDF was saved because the publisher and repository copies were behind bot checks; the text was read on PubMed Central.
