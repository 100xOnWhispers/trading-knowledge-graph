---
title: "Reconciling Open Interest with Traded Volume in Perpetual Swaps"
authors: "Giagkiozis, Ioannis; Said, Emilio"
year: 2024
venue: "Ledger, Volume 9 (2024), 1-15 (read as arXiv 2310.14973v2)"
url: "https://arxiv.org/pdf/2310.14973"
pdf: "sources/04-open-interest-liquidations/giagkiozis-2024-reconciling-open-interest-traded-volume.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "minutes"
tags: "open-interest, data-quality, liquidations, exchange-reporting, tick-data"
---

## Key insight
Exchange-reported open interest cannot always be trusted at intraday resolution. Open interest can only change through trades, so the absolute change in open interest over any interval is bounded above by traded volume in that interval. Testing this bound on tick data from seven large venues shows that several of them, most clearly Bybit, report open interest changes that their own reported volume cannot explain, which the authors attribute to misreported open interest, unreported volume, or delayed liquidation messages.

## Method
For intervals `(t_i, t_{i+1}]` the identity `sum of V_k >= |O_{t_{i+1}} - O_{t_i}|` must hold if reporting follows event order. The authors define open interest total variation `OTV = sum |O_{t_{i+1}} - O_{t_i}|`, total volume `VT` (trades, block trades and liquidations), and excess total variation `XTV = sum over intervals of max(|delta O| - V, 0)`. A positive `XTV` is a lower bound on missing volume if open interest is right, or on overstated open interest change if volume is right. They report `XTV` for whole periods and the probability and conditional size of violations at 1-day, 1-hour and 1-minute resolution.

## Data and sample
Tick-by-tick trades, block trades, liquidations and open interest collected by direct connection to Bybit, Binance, OKX, BitMEX, Deribit, HTX and Kraken for BTC linear (USDT) and inverse (USD) perpetuals. Two periods: January 2023, and July to September 2023. The data and infrastructure are proprietary.

## Reported results
- January 2023: only Bybit shows excess over the whole month. For Bybit BTC/USDT linear, open interest total variation was USD 45.66 billion against reported volume of USD 30.32 billion, an excess of USD 15.34 billion; the Bybit inverse contract shows USD 5.52 billion of excess.
- July to September 2023: Bybit's excess grew and OKX also shows non-negligible excess; the Binance inverse contract starts to show signs of misreporting. Reconciling Bybit's open interest would require more than USD 128 billion of volume under perfect synchrony, or USD 156 to 213 billion using other venues' ratios.
- At finer resolution, the authors state that virtually all exchanges have less than ideal reporting. Bybit's open interest is irreconcilable every day, almost every hour, and in more than 70% of one-minute intervals, with expected one-minute excess above USD 500,000 on the linear contract.
- Only HTX and Kraken, and to some degree BitMEX, are described as almost reconcilable at every resolution.

## Signal construction
Not a trading signal. It is a data-quality filter to run before any open interest feature is trusted: per venue and per interval, compute `max(|delta OI| - volume, 0)`; flag or down-weight intervals and venues where it is positive; and prefer venues with low violation rates when building aggregated open interest. A second use is as a detector of delayed liquidation reporting: violations that cluster in stress periods suggest forced trades missing from the trade feed.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant. A bot that uses minute-level open interest changes from Binance, Bybit and OKX as inputs is exposed to exactly these errors, and the authors show they are largest at one-minute resolution. The test is cheap and venue-agnostic, so it should be rerun on SOL contracts and on current data, including Hyperliquid (where positions are on-chain) and Kalshi (which reports one-sided open interest).

## Caveats
BTC contracts only and 2023 data; reporting practices may have changed. The authors cannot tell whether volume or open interest is the wrong series. Timestamp resolution is 1 ms and endpoint ordering can cause small spurious violations, though not at the sizes reported. One author is affiliated with a trading firm.
