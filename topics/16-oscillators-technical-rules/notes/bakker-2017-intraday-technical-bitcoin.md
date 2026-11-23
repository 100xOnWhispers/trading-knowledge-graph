---
title: "Technical Analysis in the Cryptocurrency Market: Assessment of intra-day trading strategies in the BitCoin market based on multiple data-snooping tests"
authors: "Bakker, Joris"
year: 2017
venue: "Master's thesis, Quantitative Finance, Erasmus School of Economics"
url: "https://thesis.eur.nl/pub/41546/Bakker.pdf"
pdf: "sources/16-oscillators-technical-rules/bakker-2017-intraday-technical-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "minutes"
tags: "bitcoin, five-minute, bollinger-bands, rsi, contrarian, data-snooping, spa-test, transaction-costs, decay, neural-network"
---

## Key insight
The only source in this folder that tests oscillators on intraday crypto with data-snooping corrections and real fees. At five minutes, contrarian rules beat trend-following ones, and the best rule before costs is a short-window Bollinger Band reversal. Fees reverse the picture: the Bollinger rule's break-even cost is below the exchange's minimum fee, the number of significant rules falls from 541 to 22, and after 2014 no rule is significant in any year.

## Method
A universe of 3,312 rules in seven classes: filters, moving averages, support and resistance, channel breakouts, RSI oscillators, on-balance volume averages and Bollinger Bands. Most classes include a contrarian twin. Rules carry a delay filter d and holding period c. The RSI rule is RSI(m, v, d, c): buy when RSI falls below 50 - v, sell above 50 + v. The Bollinger rule is BB(j, k, d, c) with a j-period mean and bands of k standard deviations. Benchmarked against buy-and-hold on mean excess return, Sharpe and Sortino ratios. Four data-snooping tests: White's Reality Check, Hansen's SPA, the Romano-Wolf stepM and the stepwise SPA of Hsu et al. Costs enter as g times the absolute change in position each bar. A final section feeds rule signals into a neural-network classifier.

## Data and sample
BTC/USD on Bitstamp, tick data from Bitcoincharts resampled to 5-minute closes, 1 January 2013 to 17 July 2017. Subperiods are the calendar years 2013 to 2017.

## Reported results
- Without costs: the stepwise SPA test finds 541 significant rules (16.3% of the universe) on the Sharpe criterion. Trend-reversal rules do much better than trend-following ones. Significant rules trade about once every 70 minutes.
- Best rule without costs: BB(4, 0.25, 0, 0), with a mean excess log return of 3.816 basis points per 5-minute bar, earning mainly when volatility spikes. Its break-even one-way cost is 6.32 basis points, below Bitstamp's minimum fee of 10 basis points.
- With one-way costs of 13 basis points: 22 significant rules remain (0.7%). The best becomes a filter rule, F(3, 0.001, 1, 0), trading once every 223 minutes for 0.379 basis points per bar.
- Subperiods with costs: significant rules exist only in 2013 and 2014. From 2015 on, none.
- Neural-network combinations of rule signals outperform the best single rule on return, Sharpe ratio and break-even cost.
- Intraday pattern: volume peaks between 13:00 and 16:00 UTC and is lowest between 03:00 and 06:00 UTC.

## Signal construction
Bollinger reversal on 5-minute closes: z_t = (P_t - mean of last j closes) / (standard deviation of last j closes); go short when z_t > k, long when z_t < -k; the unconstrained optimum was j = 4, k = 0.25, which trades almost every bar. RSI reversal: long when RSI(m) < 50 - v, short when RSI(m) > 50 + v. Filter rule for the cost-aware case: go long when price rises a threshold x above its recent low (the low over the last e bars), short when it falls x below the recent high, with the signal required to persist for d bars. The winning rule is labelled F(3, 0.001, 1, 0); the thesis defines the label order as F(x, e, d, c), but the values read more naturally as a 3-bar extreme window, a 0.001 threshold and a one-bar delay, and the units of the threshold were not confirmed.

## Relevance to SOL perpetuals at minutes to hours
This is the closest match to the bot's horizon. It says short-horizon mean reversion is real in crypto prices but is roughly a bid-ask-bounce-sized effect: about 6 basis points per round of the best rule. It is capturable only by a maker, or by a taker on a venue whose all-in cost is below that. The first number to obtain for Kalshi SOL perps is therefore the all-in cost per side, to compare against 6 and 13 basis points. The rapid decay after 2014 also warns that any intraday rule found on recent SOL data may have a life measured in months.

## Caveats
A master's thesis, not peer reviewed. Spot Bitstamp in 2013 to 2017, which was thin; close-to-close 5-minute returns include bid-ask bounce, which favors contrarian rules mechanically. Execution is assumed at the bar close. The neural-network section was not read in detail and its out-of-sample design was not confirmed.
