---
title: "DeMarkAlgorithm: DeMark Setup strategy on BTCUSD (QuantConnect embedded backtest)"
authors: "not confirmed (anonymous QuantConnect user)"
year: 2017
venue: "QuantConnect embedded backtest page"
url: "https://www.quantconnect.com/terminal/cache/embedded_backtest_862923da501f65af59c1a3c36f36dcee.html"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "15-demark-indicators"
asset_class: "crypto"
horizon: "hours"
tags: "td-setup, bitcoin, four-hour-bars, backtest, fees, momentum-entry, crypto"
---

## Key insight
The only crypto backtest of a DeMark rule found with code, fees and full statistics. Trading in the direction of a completed 9-bar TD Setup on 4-hour BTCUSD bars, with a fixed 2% stop and 2% target, came out flat after fees over nine months of 2017. A 55% win rate did not help because the average loss exceeded the average win.

## Method
The page shows the statistics panel and the full C# source (`DeMarkAlgorithm.cs`, `DeMarkSetup.cs`).

- Bars: ticks consolidated to 4-hour bars (1-hour and daily are supported but not used in this run).
- Setup detection: bars 0 to 8 each close beyond the close 4 bars earlier, and bar 9 closes on the other side (a price flip precedes the run). So the signal fires on bar 9 of a flip-initiated setup.
- Entry used in this run (`OpenOnTrend = true`): go long when nine closes are each above the close 4 bars earlier, short when nine are each below. This trades with the run, the opposite of DeMark's intended fade. Entries on perfected setups and on countdown 13 are coded but switched off.
- Exits: stop loss 2% and take profit 2% from the fill price. Trailing stop off. One position at a time, full account size, long or short.
- Brokerage model: Bitfinex margin account with its fee model. Starting cash $100,000.

## Data and sample
BTCUSD on Bitfinex, tick data, 1 January 2017 to 1 October 2017.

## Reported results
- Total trades 102; win rate 55%, loss rate 45%.
- Average win 2.10%, average loss -2.49%; profit-loss ratio 0.84; expectancy 0.012.
- Net profit -0.124%; compounding annual return -0.165%; Sharpe ratio 0.089; drawdown 11.1%.
- Total fees $20,669.13.
- Annual standard deviation 0.195; alpha -0.077; beta 0.058.

## Signal construction
As in the code: a rolling window of at least 15 closed bars; test the nine most recent closes against their 4-bar lags plus the flip bar; emit +1 or -1 on completion. The source also codes the perfection test and a `close <= low[2]` countdown.

## Relevance to SOL perpetuals at minutes to hours
This is the nearest match to the target use: a crypto pair, intraday bars, costs charged. Fees were about 20.7% of starting capital on 102 trades at full account size, against a net result near zero, so the rule's gross gain was roughly the size of its fees (my arithmetic from the reported figures). The average loss (-2.49%) exceeds the 2% stop while the average win (2.10%) sits near the target; the page does not say whether fees or stop slippage explain the gap. Any SOL test should model the Kalshi fee schedule and spread explicitly and should check stops on finer data than the signal bar.

## Caveats
One asset, one parameter set, nine months inside a strong bull market, anonymous author, publication date not confirmed (the year field is the backtest year). No benchmark is shown. BTC rose strongly during 2017 (background knowledge, not from the page), so a flat long-short result is poor in context but says little about the signal in other regimes. The 2% bracket is the author's choice, not a DeMark rule. The fade variant is not tested.
