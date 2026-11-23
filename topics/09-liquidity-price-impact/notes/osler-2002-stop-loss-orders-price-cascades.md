---
title: "Stop-Loss Orders and Price Cascades in Currency Markets"
authors: "Osler, Carol L."
year: 2002
venue: "Federal Reserve Bank of New York Staff Report No. 150"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.pdf"
pdf: "sources/09-liquidity-price-impact/osler-2002-stop-loss-orders-price-cascades.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "fx"
horizon: "minutes"
tags: "stop-loss, price-cascade, round-numbers, stop-run, positive-feedback, order-clustering"
---

## Key insight
Stop-loss orders cluster just beyond round numbers, and exchange rates move unusually fast after crossing those levels. The response is larger and lasts longer than the response at take-profit clusters, which is what one would expect if stops are triggered in waves. This is early direct evidence for "price cascades" driven by non-informative, price-contingent order flow.

## Method
Step one uses the order book of the Royal Bank of Scotland, a major foreign exchange dealing bank, to locate where stop-loss and take-profit orders cluster. Step two tests exchange-rate behavior near those levels using minute-by-minute quotes. A rate "reaches" a level when it comes within 0.01 percent of it. Behavior at round numbers (rates ending in 00 or 50) is compared with behavior at 10,000 sets of 30 arbitrary levels within each 10-trading-day interval, and significance is assessed by a bootstrap-style sign test across intervals. Crossing a level identifies stop-loss dominated episodes; failing to cross identifies take-profit dominated ones.

## Data and sample
Orders: 9,655 stop-loss and take-profit orders, aggregate face value over 55 billion US dollars, in dollar-yen, dollar-pound and euro-dollar, 1 August 1999 to 11 April 2000. Stop-loss orders are 43 percent of all orders "by volume" and 45 percent by value. Quotes: Reuters minute-by-minute quotes for dollar-mark, dollar-yen and dollar-pound, 9 a.m. to 4 p.m. New York time, January 1996 to April 1998.

## Reported results
- Almost 10 percent of orders sit at rates ending in 00, about 3 percent at each other rate ending in 0, about 2 percent at each rate ending in 5.
- Executed stop-loss buy orders cluster just above round numbers: 14.3 percent have rates ending in 01 to 10 versus 6.9 percent ending in 90 to 99. Stop-loss sells cluster just below.
- Executed take-profit orders cluster exactly on 00: 9.9 percent by value versus 3.8 percent for stop-loss orders.
- After crossing round numbers, the excess move relative to arbitrary levels and relative to not crossing is positive at 15 minutes (1.12, 1.30 and 0.77 hundredths of a percent for mark, yen and pound), and stays positive out to 2 hours. At 1 and 2 days it is mostly negative.
- The average move after round numbers exceeded that after arbitrary numbers in 51 of 58 intervals.
- Rates reverse more often than chance on reaching take-profit clusters.

## Signal construction
1. Level map: round-number grid for SOL (for example every 1 and 5 dollars, and prior-day high and low), plus estimated liquidation-price clusters where available.
2. Event: price crosses a level by more than a small buffer (the paper uses 0.01 percent).
3. Hypothesis to trade or avoid: continuation for 15 minutes to 2 hours after a clean cross; reversal tendency when price approaches but fails to cross.
4. Risk use: place own stops away from the "just beyond the round number" zone where others' stops cluster.

## Relevance to SOL perpetuals at minutes to hours
The mechanism maps closely onto perps, where exchange liquidations are mandatory stop orders at computable prices, so cascades should be stronger than in spot FX. The horizon of the effect (minutes to about two hours) matches the bot's. What must be re-tested: whether SOL shows round-number clustering, the size of the effect net of costs, and whether thin Kalshi books amplify it or simply follow Binance.

## Caveats
The measured excess moves are about one basis point, small against trading costs. The price data are quotes, not transactions, from 1996 to 1998, for dealer FX markets. The abstract says most results are significant for hours but not for days. Stop placement is inferred from one bank's orders in a different period from the price tests. The paper says stop-loss orders are not claimed to be the only or main cause of large moves.
