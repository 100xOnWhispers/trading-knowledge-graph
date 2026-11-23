---
title: "The Information of Option Volume for Future Stock Prices"
authors: "Pan, Jun; Poteshman, Allen"
year: 2004
venue: "NBER Working Paper 10925 (later published in the Review of Financial Studies, 2006)"
url: "https://www.nber.org/system/files/working_papers/w10925/w10925.pdf"
pdf: "sources/20-options-derived-signals/pan-2004-information-option-volume-stock-prices.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "20-options-derived-signals"
asset_class: "equities"
horizon: "daily"
tags: "put-call-ratio, option-volume, informed-trading, open-buy-volume, public-vs-private-signal, leverage"
---

## Key insight
Option volume predicts stock returns when it is measured as buyer-initiated volume that opens new positions, a quantity only the exchange can see. The version built from public trade and quote data predicts for one or two days and then reverses, which looks like price pressure, not information. This is the foundational result behind every "put-call ratio" signal, and its main lesson is that the publicly observable ratio is the weak one.

## Method
For each stock and day, a put-call ratio is formed from put and call contracts bought by non-market-makers to open new positions (the exact formula was not read; the usual form is `P / (P + C)`). Stocks are sorted into quintiles on the ratio and risk-adjusted returns are tracked over following days and weeks. The signal is split into a public part (buyer-initiated volume inferred with the Lee and Ready algorithm from public trades and quotes) and the non-public remainder. Further splits: by investor class (firm proprietary, discount-broker customers, full-service-broker customers), by a probability-of-informed-trading measure for the stock, and by option moneyness as a proxy for leverage.

## Data and sample
Chicago Board Options Exchange data that record, for every option, volume by initiator type (buy or sell, open or close) and investor class; individual US stocks, 1990 to 2001, daily.

## Reported results
- Stocks in the lowest put-call quintile outperform those in the highest by more than 40 basis points on the next day and more than 1% over the next week, risk-adjusted. Predictability fades over several weeks without reversing.
- The publicly observable signal predicts returns for only the next one or two trading days and prices then reverse. In a joint test the public signal has no predictive power and the non-public signal keeps its full effect.
- Signals from customers of full-service brokers (which include hedge funds) are much stronger than those from discount-broker customers. Firm proprietary volume has no predictive content.
- Predictability is greater for stocks with a higher concentration of informed traders and for deep out-of-the-money (high leverage) contracts.

## Signal construction
For crypto the closest available construction uses the aggressor flag in the Deribit trade feed: `PC_t = buy_put_volume / (buy_put_volume + buy_call_volume)` per hour or day, preferably delta-weighted and restricted to out-of-the-money options, where both this paper and [alexander-2023-net-buying-pressure-bitcoin-option-trades](alexander-2023-net-buying-pressure-bitcoin-option-trades.md) locate directional information. Open versus close cannot be observed trade by trade; the change in open interest per instrument over the interval is a coarse substitute. By this paper's taxonomy that feature is a public signal, so the expectation is a short-lived effect that may reverse.

## Relevance to SOL perpetuals at minutes to hours
What transfers is the mechanism (leverage attracts informed directional traders to out-of-the-money options) and the warning about public signals. What does not transfer: the cross-section of thousands of stocks with firm-specific private news. Crypto has two liquid option underlyings, information is mostly market-wide, and perpetuals already offer high leverage, which removes much of the reason for an informed trader to use options. The test worth running is whether hourly out-of-the-money signed option flow in BTC leads BTC and SOL perpetual returns beyond what perpetual order flow already explains.

## Caveats
Individual equities in the 1990s, daily horizon, with a proprietary exchange dataset that has no public crypto equivalent. Returns are before transaction costs. The working-paper version was read; the published article may differ in detail. Deribit's aggressor flag is public, so any edge from it should be competed away faster than the private signal studied here.
