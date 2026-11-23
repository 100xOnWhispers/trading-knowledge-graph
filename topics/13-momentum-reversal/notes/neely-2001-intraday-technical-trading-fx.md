---
title: "Intraday Technical Trading in the Foreign Exchange Market"
authors: "Neely, Christopher J.; Weller, Paul A."
year: 2001
venue: "Federal Reserve Bank of St. Louis Working Paper 1999-016B (published in Journal of International Money and Finance)"
url: "https://s3.amazonaws.com/real.stlouisfed.org/wp/1999/1999-016.pdf"
pdf: "sources/13-momentum-reversal/neely-2001-intraday-technical-trading-fx.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "fx"
horizon: "minutes"
tags: "evolutionary-algorithms, genetic-programming, intraday, negative-autocorrelation, transaction-costs, null-result"
---

## Key insight
At half-hourly frequency in a 24-hour market, both a genetic program and a simple autoregressive model find strong, stable out-of-sample predictability, yet neither earns excess returns once realistic transaction costs and trading hours are imposed. The predictability is almost entirely low-order negative serial correlation (short-horizon reversal), and a plain linear model captures it as well as the evolved rules. Predictability is not profitability, and sophisticated search adds nothing when the structure is this simple.

## Method
Genetic programming over rule trees, with separate training (February to March 1996), selection (April to May 1996) and out-of-sample test (June to December 1996) periods. Twenty-five rules per currency are evolved under each of three in-sample one-way cost settings (0, 1 and 2 basis points); rules with positive selection-period return are combined with equal weights. The benchmark is an autoregressive model on log exchange-rate changes with an optimised no-trade filter. Break-even transaction cost is the cost that reduces out-of-sample excess return to zero. A second experiment restricts position changes to a 12-hour window of active trading on weekdays.

## Data and sample
Half-hourly bid and ask quotes for the dollar against the German mark, Japanese yen, British pound and Swiss franc, 1996, from the Olsen and Associates HFDF96 data set.

## Reported results
- Half-hourly returns show significant negative first-order autocorrelation (the paper cites means around -0.12 to -0.17 depending on hours), too large to be explained by non-synchronous quoting.
- Rules trained at zero cost earn over 100% a year before costs in three of four currencies, but trade about once an hour; the highest break-even cost is 1.01 basis points one-way (pound).
- Raising the in-sample cost cuts trading frequency and gross returns and raises break-even cost.
- The autoregressive model does at least as well as the genetic program; its break-even cost reaches 24.4 basis points for the mark with round-the-clock trading.
- With trading restricted to active hours, break-even costs generally fall below what an institutional trader would pay (the authors use 2 to 2.5 basis points); the pound at 4.2 basis points is the one exception.
- Conclusion: no evidence of excess returns under realistic conditions; consistent with market efficiency.

## Signal construction
The discovered structure is: next half-hour return = negative coefficient times the last one or two half-hour returns, traded only when the forecast exceeds a filter equal to the cost. This is the baseline any intraday reversal signal must beat. As a signal for a taker it is not profitable in this study.

## Relevance to SOL perpetuals at minutes to hours
Closest classic analogue to the bot's setting: a 24-hour market, 30-minute bars, evolved rules against a linear benchmark, costs in basis points. Three lessons transfer. Compute break-even cost per trade for every candidate signal and compare with the all-in cost on Kalshi. Always fit a low-order autoregression as the benchmark before trusting a machine-learned or evolved rule. Check whether apparent profits come from illiquid hours, when quoted prices are least executable. Crypto perpetual fees and spreads are typically larger than 1 to 2 basis points, so the hurdle is higher than in this paper.

## Caveats
One year of data, four currency pairs, indicative quotes instead of firm tradable prices (the authors discuss this). FX in 1996 is not crypto in 2026; the size of short-horizon reversal in SOL must be measured. A null result on one sample does not rule out conditional versions (for example reversal only after low-volume moves).
