---
title: "Intraday Technical Trading in the Foreign Exchange Market"
authors: "Neely, Christopher J.; Weller, Paul A."
year: 1999
venue: "Federal Reserve Bank of St. Louis Working Paper 1999-016B (version dated 10 January 2001)"
url: "https://files.stlouisfed.org/files/htdocs/wp/1999/99-016.pdf"
pdf: "sources/12-time-encodings-cycles/neely-1999-intraday-technical-trading-genetic-programming.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "fx"
horizon: "minutes"
tags: "genetic-programming, time-of-day, intraday, transaction-costs, out-of-sample"
---

## Key insight
A genetic program was given the hour of the day as one of three inputs and allowed to evolve intraday trading rules for a 24-hour market. The evolved rules found stable out-of-sample predictability at zero cost, yet earned nothing once realistic transaction costs and trading hours were imposed, and the time-of-day input turned out to be uninformative for direction. A plain autoregressive model did at least as well as the evolved rules.

## Method
Genetic programming over decision trees. Function set: plus, minus, times, divide, norm (absolute difference), moving average, max, min, lag; Boolean and, or, not, greater than, less than; if-then and if-then-else; random constants from (0, 6); true and false. Inputs:
1. the exchange rate divided by its two-week moving average,
2. a short-term interest-rate futures differential,
3. the hour of the day (GMT), included "because of the large and consistent intraday fluctuation in trading volume", which "may also have an effect on the first moment".

A rule maps these to a long (+1) or short (-1) position each half-hour. An illustrative rule is: long if the rate exceeds its 48-period moving average and the time is between 0800 and 1600 GMT, short otherwise. Fitness is continuously compounded excess return net of a one-way cost c of 0, 1 or 2 basis points. Each generation creates 1,000 offspring by fitness-weighted crossover; the run stops after 40 generations or 10 generations without a new best rule on the selection period. Twenty-five rules are evolved per currency and cost level and combined with equal weights. The comparison model is an autoregression with a no-trade filter; an extended linear model adds the same three inputs. A second scenario restricts trading to a 12-hour active window on business days.

## Data and sample
Half-hourly bid and ask quotes for 1996 from the Olsen and Associates HFDF96 set: DEM, JPY, GBP and CHF against the dollar. Training 1 February to 31 March 1996, selection 1 April to 31 May, out-of-sample test 1 June to 31 December.

## Reported results
- Rules trained at zero cost earn out-of-sample excess returns above 100% a year in three of four currencies before costs, trading about once an hour. The highest break-even cost is 1.01 basis points one-way (GBP).
- Raising the in-sample cost lowers trading frequency and raises break-even cost towards the two to three basis points the authors take as an institutional trader's cost.
- The autoregressive model has higher break-even costs under 24-hour trading (24.4 basis points for DEM), but under restricted trading hours break-even costs fall below realistic costs in all cases.
- Adding the normalized rate, time of day and interest differential to the linear model gave results "not significantly different"; the authors conclude these variables carry "no additional forecasting power" and that uninformative inputs degrade the genetic program.
- Half-hourly returns show significant negative first-order autocorrelation.

## Signal construction
Not a recommended signal. As a template for evolutionary search with clock inputs:
1. Give the search an integer hour or minute-of-day terminal and comparison operators, so it can express session windows.
2. Put transaction costs in the fitness function; rules evolved at zero cost overtrade.
3. Use separate training, selection and test periods, and evolve many rules to check agreement among them.
4. Benchmark against a small linear model with the same inputs.

## Relevance to SOL perpetuals at minutes to hours
The design maps closely onto a 24/7 perpetual: half-hourly decisions, long or short, cost-aware fitness. The paper's main lessons transfer: time of day was valuable for knowing when costs are low, not for predicting direction, and the profitable-looking trades clustered in illiquid hours. For SOL on a small venue the same trap exists on weekends and in thin Asian-morning hours.

## Caveats
One year of data from 1996, with two months of training. Quotes are indicative, not firm. Only one evolutionary configuration was tried. The time-of-day input is a raw hour number, with no cyclical encoding, though tree rules with comparisons do not need one. The published journal version was not read.
