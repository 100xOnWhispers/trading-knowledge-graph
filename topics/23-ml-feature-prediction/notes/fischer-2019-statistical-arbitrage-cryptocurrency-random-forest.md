---
title: "Statistical Arbitrage in Cryptocurrency Markets"
authors: "Fischer, Thomas Guenter; Krauss, Christopher; Deinert, Alexander"
year: 2019
venue: "Journal of Risk and Financial Management 12(1), 31"
url: "https://api.openalex.org/works/doi:10.3390/jrfm12010031"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "hours"
tags: "random-forest, cross-sectional, minute-bars, statistical-arbitrage, lagged-returns, transaction-costs, limits-to-arbitrage"
---

## Key insight
A random forest trained only on lagged returns of 40 coins, on minute-binned data, predicts which coins will beat the cross-sectional median over the next 120 minutes well enough that a top-3 long, bottom-3 short portfolio earned a small positive return after costs of 15 basis points per half-turn in a three-month out-of-sample test. It is one of very few intraday crypto machine-learning studies that reports a positive result net of a stated cost, and the authors themselves frame it against limits to arbitrage.

## Method
From the abstract (the only part read; the publisher and repository pages were blocked to automated access, and the abstract was retrieved from the OpenAlex metadata record for the DOI):
- Model: random forest.
- Features: lagged returns of 40 cryptocurrency coins on minute-binned data.
- Target: whether a coin outperforms the cross-sectional median of all 40 coins over the subsequent 120 minutes.
- Portfolio: buy the three coins with the highest predictions and short the three with the lowest; reverse after 120 minutes.
The lag structure, training window and forest settings were not confirmed. The design follows the authors' earlier equity work (Krauss, Do and Huck 2017, cited in the abstract).

## Data and sample
40 coins, minute bins. Out-of-sample backtest from 18 June 2018 to 17 September 2018. Venue and training period not confirmed.

## Reported results
From the abstract:
- More than 100,000 trades in the out-of-sample period.
- "Statistically and economically significant returns of 7.1 bps per day, after transaction costs of 15 bps per half-turn."
- The authors say the finding challenges semi-strong market efficiency and then discuss it "in light of limits to arbitrage, focusing on total volume constraints of the presented intraday-strategy."

## Signal construction
For a panel of N liquid perps, every minute compute each instrument's returns over a set of lagged intervals, train a random forest classifier on the binary label "forward 120-minute return above the cross-sectional median", and rank instruments by predicted probability. For a single-instrument bot, SOL's predicted probability (or its rank) is a relative-strength score against the panel; a directional trade additionally needs a view on the panel's common move.

## Relevance to SOL perpetuals at minutes to hours
The horizon (two hours) and input set (bar returns only) match the bot's constraints closely, and the cross-sectional median label removes the market factor, which is a labeling idea worth copying because it makes the target more stationary. The net figure is small: 7.1 bps per day after costs leaves little room for error, and a single-venue, single-instrument bot cannot hold the market-neutral book that produced it. Kalshi's SOL perp cannot be shorted against 39 other coins on the same venue, so the result is best used as a signal-quality benchmark on Binance or Bybit data.

## Caveats
Abstract-only, so sample construction, exchange, and the capacity analysis could not be checked. The out-of-sample window is three months in mid-2018, a falling and comparatively inefficient market. Shorting 2018 altcoins at minute frequency was not generally feasible, which the authors' limits-to-arbitrage discussion appears to acknowledge. Jaquart, Dann and Weinhardt (2021) adopt this paper's cost level (30 bps round-trip) and find single-asset bitcoin strategies unprofitable after it.
