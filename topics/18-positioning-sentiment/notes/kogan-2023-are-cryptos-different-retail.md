---
title: "Are Cryptos Different? Evidence from Retail Trading"
authors: "Kogan, Shimon; Makarov, Igor; Niessner, Marina; Schoar, Antoinette"
year: 2023
venue: "NBER Working Paper 31317"
url: "https://www.nber.org/system/files/working_papers/w31317/w31317.pdf"
pdf: "sources/18-positioning-sentiment/kogan-2023-are-cryptos-different-retail.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "multi"
horizon: "daily"
tags: "retail-positioning, contrarian, momentum, etoro, portfolio-share, hodl"
---

## Key insight
The same retail investors who trade against price moves in stocks and gold do not do so in crypto. After a crypto price move they leave their holdings untouched, so their portfolio share rises with price and falls with price, which is momentum-like behaviour. This breaks the standard equity assumption that retail flow is contrarian and can be faded as a liquidity-providing counterparty. In crypto, retail positioning is better read as trend-confirming.

## Method
Following Calvet et al. (2009), the daily log change in the portfolio share of an asset is regressed on its contemporaneous and lagged returns, at cohort level (to reduce noise from sporadic traders) and at account level for the most active half of accounts. The total share change is decomposed into a passive part (price drift) and an active part (rebalancing trades). Days are also sorted into return quintiles to see whether behaviour is driven by extreme moves. Robustness checks cover investor characteristics, attention, fees, lottery preferences, and same-investor comparisons across asset classes.

## Data and sample
Trades of 200,000 individual accounts at eToro, 2015 to 2019. The 200 most traded stocks (over 91% of stock trading on the platform), gold, and cryptocurrencies, of which Bitcoin, Ethereum and Ripple account for over 78% of crypto trading.

## Reported results
- Stocks: a significant negative relation between the change in portfolio share and same-day return, driven by active selling of winners and buying of losers. The effect is much weaker for one-week lagged returns and absent beyond a week.
- Gold: the same contrarian pattern as stocks.
- Crypto: a strong positive relation between share change and same-day return, and a weaker positive relation with one-week lagged returns. This comes mainly from the absence of rebalancing in either direction.
- Contrarian trading in stocks and gold is concentrated on days with large moves; in crypto there is no change in active rebalancing across return quintiles, even on extreme days.
- Individual characteristics do not explain the difference, and it holds within the same investors.
- Footnote: crypto returns in the sample show no meaningful daily autocorrelation (a one-standard-deviation return is followed by -0.2%, not significant).
- The authors conjecture that retail investors read price rises as evidence of future adoption.

## Signal construction
Not a signal. It is a prior for interpreting retail positioning measures (exchange long/short account ratios, small-wallet holdings, app activity): do not assume that retail net buying follows price declines in crypto, and do not assume that fading retail is the default.

## Relevance to SOL perpetuals at minutes to hours
Transfers as an interpretive rule, not as a tested intraday effect. The eToro sample is mostly unlevered or lightly levered spot-like exposure with holding periods of days, whereas perp traders on Binance or Hyperliquid are levered and can be forcibly closed. Liquidations create involuntary contrarian flow that this paper cannot see. The crypto retail population has also changed since 2019. What needs testing: whether Binance global account long/short ratios rise or fall after SOL up-moves, and at what lag.

## Caveats
One broker, 2015 to 2019, mainly BTC, ETH and XRP. Platform is not a perp venue. The paper measures behaviour, not the return to trading against or with it. Working paper without replication in this session.
