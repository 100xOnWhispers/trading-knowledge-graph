---
title: "What Does Futures Market Interest Tell Us about the Macroeconomy and Asset Prices?"
authors: "Hong, Harrison; Yogo, Motohiro"
year: 2012
venue: "NBER Working Paper 16712 (January 2011, revised June 2012)"
url: "https://www.nber.org/system/files/working_papers/w16712/w16712.pdf"
pdf: "sources/04-open-interest-liquidations/hong-2012-futures-open-interest-asset-prices.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "futures"
horizon: "multi-day"
tags: "open-interest, return-predictability, commodities, hedging-demand, limited-arbitrage"
---

## Key insight
Growth in aggregate futures open interest predicts returns, and does so better than futures prices or hedger net positioning. The argument is that open interest rises when economic activity and hedging demand rise, while the futures price can move either way depending on which side hedges, so the gross quantity is the cleaner signal when risk-absorption capacity is limited. This is the main traditional-markets evidence that open interest changes carry information about future prices.

## Method
A simple model with limited risk absorption by speculators, then predictive regressions of monthly returns on standardized predictors. The new predictor is the growth rate of "market interest": for each commodity, dollar open interest is spot price times contracts outstanding; this is aggregated within sectors, converted to a monthly growth rate, aggregated across sectors, and smoothed with a 12-month geometric average. Controls are the short rate, yield spread, Chicago Fed National Activity Index, basis, hedger imbalance and past returns. Analogous variables are built for currency, bond and stock futures.

## Data and sample
US futures markets at monthly frequency. The commodity sample starts in 1966 and runs to 2008; currency, bond and stock samples start in 1984. Commodity returns are equally weighted across four sectors using fully collateralized futures positions with more than one and less than 13 months to maturity.

## Reported results
- A one standard deviation increase in commodity market interest raises expected commodity returns by 0.73% per month (t-statistic 2.50).
- Adding market interest raises the R-squared of the commodity return regression from 2.58% to 4.96%.
- A one standard deviation increase in commodity market interest lowers expected bond returns by 0.32% per month, described as highly significant.
- The 12-month growth rate of commodity market interest has a mean of 1.47% per month and a standard deviation of 2.06%.
- Evidence for currency, bond and stock market interest is described as qualitatively similar but statistically weaker.
- Open interest growth is pro-cyclical: positively correlated with the Chicago Fed National Activity Index in all four markets.

## Signal construction
The paper's variable is slow: 12-month smoothed growth of dollar open interest, used at monthly horizon. A crypto adaptation would be `g_t = log(OI_usd_t / OI_usd_{t-k})` aggregated across major venues for an asset, standardized over a rolling window, with k chosen for the target horizon. The paper's sign (rising open interest predicts higher returns) is a trend-confirmation reading, opposite to the "crowded leverage precedes a flush" reading common in crypto.

## Relevance to SOL perpetuals at minutes to hours
The transferable idea is that open interest is a quantity signal distinct from price and from net positioning, and that it matters when arbitrage capital is limited, which describes crypto well. What does not transfer is the mechanism (commercial hedging demand over the business cycle) and the horizon (months). In perps, open interest growth mostly reflects speculative leverage, so the sign of any intraday relation must be estimated from scratch. The paper is best used as justification for testing open interest growth as a conditioning variable, not as evidence for a specific intraday rule.

## Caveats
Monthly data, in-sample regressions with modest R-squared, and no transaction-cost analysis in the sections read. No out-of-sample test was found by keyword search of the text. The journal version was not opened in this session, so the grade is held at B.
