---
title: "Bitcoin flash crash on May 19, 2021: What did really happen on Binance?"
authors: "Baumgartner, Tim; Guettler, Andre"
year: 2022
venue: "IWH Discussion Papers No. 25/2022, Halle Institute for Economic Research (November 2022)"
url: "https://www.econstor.eu/bitstream/10419/266345/1/1822049504.pdf"
pdf: "sources/28-shock-response-price-pressure/baumgartner-2022-bitcoin-flash-crash-binance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "minutes"
tags: "flash-crash, liquidation-burst, venue-outage, price-dislocation, recovery-path, data-quality"
---

## Key insight
A forensic event study of the largest liquidation crash of 2021 on the largest venue. Bitcoin futures fell to a low 33.9% below the midnight level at 13:09 UTC, stabilized within the hour and made a post-crash high about three and a half hours after the low. During the worst 40 minutes Binance stopped reporting trades, locked out retail clients while its liquidation engine kept running, and its price diverged from other venues by about seven times the normal gap. The data for that window were back-filled later and fail a Benford's Law test.

## Method
Tick-level Bitcoin futures trades with millisecond timestamps and an insurance-fund flag, plus minute-level data from other exchanges. The crash window (12:00 to 14:00 UTC on 19 May) is compared with a ten-day reference period using t-tests and Wilcoxon tests on the absolute price gap between Binance and the cross-exchange average, the gap to the mark price, volumes, trade counts and API latency. Benford tests are applied to trade sizes in the back-filled interval. A model estimates the insurance fund's unreported trading.

## Data and sample
73 million Bitcoin futures transactions on Binance from Tardis, 9 to 20 May 2021, completed with data Binance published in March 2022; minute data for other exchanges from TradingView and Tiingo.

## Reported results
- Price was USD 43,025 at 00:00 and 38,630 at 12:00. The sharp decline began about 12:30; the minimum of 28,758 came at 13:09; stabilization near 35,000 by about 14:00; a new intraday high of 38,764 at 16:38.
- Binance volume from 12:00 to 16:00 was 357,607 BTC (USD 12.7 billion) in 2.7 million trades.
- Transaction reporting was missing from 13:16 to 13:56 and was filled in about a week later.
- Mean absolute price gap between Binance and other exchanges: 53 before the crash and 375 during it (USD, as tabulated); medians 43 and 189. Against the mark price: 41 and 295.
- Binance traded above its peers early in the outage and well below them between 13:30 and 14:00, which the authors link to a surplus of sell orders from forced liquidations.
- Insurance-fund trading spiked just before the outage. Reported volume during the outage was about 20% of the level the authors' model expects. Modelled fund trading in the gap is about USD 1 billion. The published fund balance moved from USD 290.4 million to 288.7 million.
- Scope record: horizon minutes to hours after a liquidation burst; conditioning variable a single event; sign reversal (about 22% up from the low within an hour, about 35% within three and a half hours, computed from the tabulated prices); no strategy, no costs.

## Signal construction
Not a signal. It supplies monitoring rules for cascade conditions: (1) track the gap between each venue's last price and the cross-venue median and between last price and mark price; a gap several times its normal size marks venue-local forced selling. (2) Track feed health (message latency, gaps in the trade stream) and treat a stale or delayed venue as untradeable and its data as unreliable. (3) Do not train on data from outage windows without checking whether it was back-filled.

## Relevance to SOL perpetuals at minutes to hours
The rebound was fast and large, but the paper shows why capturing it is hard: the venue with the cheapest prices was the one where clients could not trade, and the prints from that window may not be real. A backtest that fades liquidation lows using recorded prices from the affected venue will overstate what was achievable. For a bot trading a different venue (Kalshi) on signals from Binance, the lesson is to use a cross-venue composite and to down-weight a venue whose price departs from the rest. The 10 October 2025 studies in topic 04 describe the same combination of venue-local dislocation and thin books.

## Caveats
One event, one exchange, Bitcoin only. The interpretation (manipulation to protect the insurance fund) is the authors' inference and was the subject of litigation; the measurements stand independently of it. Units of the price-gap table are taken as USD from the table caption. Working paper, not peer-reviewed.
