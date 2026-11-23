---
title: "The Crypto Carry Trade"
authors: "Christin, Nicolas; Routledge, Bryan R.; Soska, Kyle; Zetlin-Jones, Ariel"
year: 2022
venue: "Working paper, Carnegie Mellon University (version 1.0, 1 August 2022)"
url: "https://www.andrew.cmu.edu/user/azj/files/CarryTrade.v1.0.pdf"
pdf: "sources/03-perp-pricing-funding/christin-2022-crypto-carry-trade.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "funding-rate, carry, leverage-demand, basis, binance, crowding"
---

## Key insight
Being short a perp and long spot earned a high, low-volatility return on Binance in 2020 to 2022, which means longs systematically overpaid for leveraged exposure. The return comes from the funding payment, not from basis moves, and it fell sharply when Binance cut maximum leverage. Funding is therefore a direct measure of net long-side demand for leverage.

## Method
One period is one 8-hour funding window. Return to long spot plus short perp is split into `x(t)`, the funding received (known at `t` on Binance because the rate is set one period ahead), and `y(t+1)`, the change in the perp-minus-index basis. Returns ignore margin, leverage and transaction costs. USDT-margined and coin-margined contracts are compared, and a model of margin risk explains why leveraged longs prefer the USDT contract.

## Data and sample
Binance API, minute data aggregated to 8-hour windows, 2020-08-11 to 2022-06-20 (N = 2,036 windows for BTC). BTC plus 17 other coins, each with USDT- and coin-margined perps. A search of the text found no mention of SOL by ticker; the coin list was not checked in full.

## Reported results
- BTC carry, annualised (Table 3): USDT contract mean 21.84%, standard deviation 1.90%, Sharpe 11.47; coin contract 16.74%, 2.61%, Sharpe 6.41. Long spot over the same period: Sharpe 0.41. (The abstract says "7 to 10" and the introduction "12.8 and 7.0"; the table values are used here.)
- By epoch the USDT carry falls from 39.00% (August 2020 to April 2021) to 7.63% (November 2021 onward).
- Median funding is 0.01% per 8 hours (about 11% a year), the exchange default when the basis is inside the clamp; the funding series is "pinned" there much of the time.
- The funding component is serially correlated; the basis-change component looks i.i.d.; their correlation is about 0.11.
- After Binance cut maximum leverage from 125x to 50x on 2021-07-23, BTC USDT carry fell from 33.03% to 10.22% and ETH from 44.60% to 9.75%.
- The carry return was positive in both rising and falling BTC sub-periods.

## Signal construction
Inputs: the funding rate for the coming payment (under the paper's timing convention it is set at `t` and paid at `t+1`; on a live venue use the exchange's running predicted rate) and the perp-minus-index basis. `carry_8h = funding_rate - risk_free`. For a directional bot: a rolling mean of funding in excess of the 0.01% default as a long-crowding gauge; the cost of holding a long over the next window is known in advance and can be netted from expected return.

## Relevance to SOL perpetuals at minutes to hours
The decomposition transfers directly: over one 8-hour window the bot's perp P&L is price change minus funding, and funding is predictable while basis change is close to noise. The leverage result matters for Kalshi: with low maximum leverage, the paper's mechanism predicts structurally smaller funding and a weaker crowding signal than on offshore venues. That prediction needs checking on Kalshi data.

## Caveats
In-sample, no costs, no margin. One venue, 22 months that include the 2021 bull market. [He et al.](he-2022-fundamentals-perpetual-futures.md) find the same static carry earns Sharpe 2.24 on BTC over January 2020 to March 2024, so most of the reported edge has decayed.
