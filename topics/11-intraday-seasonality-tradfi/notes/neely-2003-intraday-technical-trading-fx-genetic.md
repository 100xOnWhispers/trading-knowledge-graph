---
title: "Intraday Technical Trading in the Foreign Exchange Market"
authors: "Neely, Christopher J.; Weller, Paul A."
year: 2003
venue: "Journal of International Money and Finance 22(2), 223-237 (Federal Reserve Bank of St. Louis Working Paper 1999-016B read)"
url: "https://s3.amazonaws.com/real.stlouisfed.org/wp/1999/1999-016.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/neely-2003-intraday-technical-trading-fx-genetic.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "fx"
horizon: "minutes"
tags: "genetic-programming, evolutionary-search, intraday-trading-rules, time-of-day, transaction-costs, out-of-sample, fx"
---

## Key insight
An evolutionary search over intraday FX trading rules, with time of day available as an input, finds strong and stable out-of-sample predictability at zero cost, and none of it survives realistic transaction costs and a restriction to liquid hours. The paper is an early, honest benchmark for what genetic programming does on high-frequency data: it rediscovers microstructure regularities (mainly negative first-order autocorrelation of quote returns) that cannot be traded by a price taker.

## Method
Genetic programming in the style of Koza: candidate rules are decision trees built from arithmetic, logical and time-series functions (moving averages, lags, maxima and minima) that map past data to a long or short position each half-hour. Inputs are (1) the exchange rate normalized by a two-week moving average, (2) the US-foreign short-rate futures price differential, and (3) time of day (GMT). Fitness is in-sample excess return net of an assumed cost c; rules are evolved on a training period, selected on a validation period and evaluated out of sample. Raising c in training penalizes turnover. The benchmark is an optimized linear (autoregressive) forecasting model. Performance is summarized by annual excess return, trade count and the break-even one-way cost that drives excess return to zero.

## Data and sample
Half-hourly bid and ask quotes for DEM, JPY, GBP and CHF against the dollar during 1996, from the Olsen and Associates HFDF96 data set; interest-rate futures from CME and LIFFE.

## Reported results
- With zero cost in training, out-of-sample annual excess returns exceed 100% in three of four currencies, with rules trading about once an hour.
- Break-even costs are tiny in that setting, for example 1.01 basis points one-way for the pound, against a realistic 2 to 2.5 bp for large institutional trades.
- Training with higher assumed costs cuts trading frequency and gross return but raises break-even cost steadily; for the autoregressive benchmark one DEM case reaches 24.4 bp.
- Under 24-hour trading with a 2.5 bp one-way cost, the benchmark rules still appear to earn over 20% a year; the authors reject that reading because it assumes trading through illiquid hours and weekends.
- Once realistic costs are charged and trading is restricted to hours of high market activity, there is no evidence of excess returns from either the genetic program or the linear model.
- Mean first-order autocorrelation of half-hourly returns is -0.17 over all hours and -0.12 in business hours. The autoregressive rules perform at least as well as the genetic program, so the results are attributed largely to low-order negative serial correlation.
- Periods: training February to March 1996, selection April to May, out-of-sample test June to December.

## Signal construction
Not a signal. It is a methodology reference for evolutionary rule search: include time of day as a terminal, put transaction cost in the fitness function, use separate training, selection and out-of-sample periods, report break-even cost alongside return, and always compare with a simple linear benchmark. If the evolved rule does not beat the linear model, it has found autocorrelation, not structure.

## Relevance to SOL perpetuals at minutes to hours
Directly applicable as a design pattern and a warning for any genetic-programming, symbolic-regression or neural search over SOL intraday features. Crypto mid-price returns at short horizons also show bid-ask-related negative autocorrelation, and Kalshi's perp will have wide effective costs, so a search without cost-aware fitness will converge on untradable reversal. Break-even cost per trade is the right headline metric for a venue where the fee and spread are the binding constraint.

## Caveats
One year of data, quote data instead of transaction prices, four currency pairs, 1990s market structure. A single out-of-sample period. The search space and compute were small by current standards; the conclusion concerns that rule class, not all learnable strategies.
