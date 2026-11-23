---
title: "Does Meta Labeling Add to Signal Efficacy?"
authors: "Singh, Ashutosh; Joubert, Jacques"
year: 2019
venue: "Hudson & Thames research article (WorldQuant University MSFE capstone project)"
url: "https://hudsonthames.org/does-meta-labeling-add-to-signal-efficacy-triple-barrier-method/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "23-ml-feature-prediction"
asset_class: "futures"
horizon: "daily"
tags: "meta-labeling, triple-barrier, cusum-filter, dollar-bars, random-forest, trade-filter, lopez-de-prado"
---

## Key insight
A worked, public test of two labeling ideas from López de Prado's "Advances in Financial Machine Learning": the triple-barrier label and meta-labeling. A simple rule chooses the side of the trade; a random forest then predicts whether that trade will be a winner and filters out the ones it expects to lose. On E-mini S&P 500 futures the filter raised out-of-sample precision modestly for both a trend rule and a mean-reversion rule. It is the most accessible empirical description of the method; the book itself was not opened in this session.

## Method
- Bars: tick data are aggregated into dollar bars, which the authors found closest to normal among time, tick, volume and dollar bars (Jarque-Bera statistics 1,782,853 for time bars against 143,045 for dollar bars).
- Event sampling: a symmetric CUSUM filter with a threshold tied to current volatility picks the bars at which a trade is considered.
- Triple-barrier label: an upper barrier (take profit) and lower barrier (stop loss) at multiples of the daily standard deviation of log returns, and a vertical barrier at a maximum holding period of one day. Label +1, -1 or 0 by which barrier is touched first.
- Primary model (side): either a 20/50-bar moving-average crossover or Bollinger bands at 1.5 standard deviations.
- Secondary model (meta-label): a random forest predicting 1 (take the primary model's trade) or 0 (skip), tuned by grid search over depth and number of trees, with the minority class up-sampled. Features are rolling volatility at several windows, serial correlation at lags one to five, momentum at one to five periods, and for the mean-reversion version RSI and moving averages.
- Splits: training, validation and an untouched out-of-sample set.

## Data and sample
E-mini S&P 500 futures tick data. Out-of-sample windows run from January 2018 to January 2019. The page gives no publication date; its references were accessed in March 2019, so the year is approximate.

## Reported results
- Mean-reversion rule, out of sample: meta-labeling raised precision from 0.17 to 0.20 and accuracy from 17% to 63%.
- Trend rule, out of sample: precision rose from 0.48 to 0.54 and accuracy from 48% to 55%.
- In validation the jumps were larger (mean-reversion accuracy from 20% to 77%).
- The authors say the meta-model did not beat the primary trend model on every metric but did on a risk-adjusted basis. Return, Sharpe and drawdown are shown only as charts.

## Signal construction
1. Define a primary rule that outputs long or short at sampled events.
2. Label each historical event 1 if the trade, run with volatility-scaled profit and stop barriers and a time limit, hit the profit barrier first, else 0.
3. Train a classifier on state features (volatility, autocorrelation, momentum, time of day, and for a perp funding, open interest and spread) to predict that label.
4. Live: take the primary signal only when the classifier's probability exceeds a threshold, and optionally size by the probability.

## Relevance to SOL perpetuals at minutes to hours
High as a design pattern. A directional perp bot already has primary rules (trend, order-flow, funding extremes); meta-labeling is a disciplined way to add machine learning as a filter on those rules instead of asking it to forecast returns from scratch, which the crypto evidence says yields only 52 to 56% accuracy. Volatility-scaled barriers suit SOL's changing volatility. The barrier multiples, time limit and event filter all need tuning on SOL data, which is itself a search that must be controlled.

## Caveats
A student capstone published on a vendor's site; Hudson & Thames sells a library implementing these methods. One instrument, two rules, about one year out of sample, no transaction costs, no bet sizing, and manual tuning of the CUSUM threshold during validation. The accuracy jump for the mean-reversion rule largely reflects predicting "no trade" for a rule that loses most of the time, and the precision change (from 0.17 to 0.20) shows the real gain is small.
