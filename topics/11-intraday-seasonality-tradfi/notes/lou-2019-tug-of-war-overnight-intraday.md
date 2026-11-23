---
title: "A tug of war: Overnight versus intraday expected returns"
authors: "Lou, Dong; Polk, Christopher; Skouras, Spyros"
year: 2019
venue: "Journal of Financial Economics 134(1), 192-213"
url: "https://personal.lse.ac.uk/polk/research/TugOfWar.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/lou-2019-tug-of-war-overnight-intraday.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "daily"
tags: "overnight-returns, intraday-returns, return-decomposition, investor-clienteles, momentum, persistence"
---

## Key insight
Close-to-close returns hide two components with very different behaviour. A stock's overnight return predicts its future overnight returns positively and its future intraday returns negatively, and the same holds in mirror image for intraday returns; the persistence lasts for years. The authors read this as two investor clienteles that trade at different times of day pushing prices in opposite directions. Classic strategy profits accrue entirely in one component: momentum and short-term reversal earn their premium overnight, most other anomalies intraday.

## Method
Each daily return is split into overnight (prior close to the open, where the open price is the volume-weighted average price over the first half-hour of trading) and intraday (that open to the close). Stocks are sorted into deciles on the past month's overnight or intraday component; the next month's overnight, intraday and close-to-close returns and three-factor alphas are measured. The decomposition is repeated for 14 strategies. A smoothed spread between a strategy's overnight and intraday returns is used to forecast its close-to-close performance. Institutional-trading proxies are used to link momentum's decomposition to a specific clientele.

## Data and sample
CRSP-Compustat US stocks with TAQ intraday prices, 1993 to 2013. Robust to CRSP opens, opening midquotes and excluding small caps. An appendix applies the decomposition to futures (not read in detail).

## Reported results
- Value-weighted overnight winners minus losers: three-factor overnight alpha 3.47% per month (t = 16.83) and intraday alpha -3.02% per month (t = -9.74).
- Value-weighted intraday winners minus losers: intraday alpha 2.41% per month (t = 7.70) and overnight alpha -1.77% per month (t = -7.89).
- For all 14 strategies, profits are earned either entirely overnight or entirely intraday, typically with opposite signs in the other component.
- Momentum profits accrue overnight; the overnight-intraday momentum spread varies by about 2% per month with institutional activity.

## Signal construction
Define a session boundary, then maintain two rolling return histories per asset: r_session_A (for example, outside US hours) and r_session_B (US hours). Features: trailing 20-day mean of each component; the persistence signal is "expect component A's sign to repeat in the next A window and to be faded in the next B window". The smoothed A-minus-B spread is a slow state variable for whether trend or reversal logic should dominate.

## Relevance to SOL perpetuals at minutes to hours
The idea that different participants dominate different clock windows, and that their price pressure persists within a window and reverses in the other, maps naturally onto a 24-hour market with Asia, Europe and US sessions. The test is cheap: decompose SOL returns by session, measure same-session autocorrelation and cross-session reversal over trailing weeks. What does not transfer: the equity result is cross-sectional (relative to other stocks) and relies on a market closure with distinct information flow, borrowing cost and price impact; crypto has no close, so the boundary is a choice and a source of overfitting.

## Caveats
Sample ends 2013. Cross-sectional alphas ignore trading costs, and trading the open is expensive. A single asset has one time series, so the statistical power is far lower than in a panel of thousands of stocks. Crypto session decompositions are covered in topic 10.
