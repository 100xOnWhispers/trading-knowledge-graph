---
title: "VPIN and the Flash Crash"
authors: "Andersen, Torben G.; Bondarenko, Oleg"
year: 2014
venue: "Journal of Financial Markets 17, 1-46 (read: CREATES Research Paper 2011-50, May 2013 version)"
url: "https://repec.econ.au.dk/repec/creates/rp/11/rp11_50.pdf"
pdf: "sources/08-trade-flow-toxicity/andersen-2014-vpin-flash-crash.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "08-trade-flow-toxicity"
asset_class: "futures"
horizon: "hours"
tags: "vpin, critique, flash-crash, volatility-forecast, trading-intensity, benchmark"
---

## Key insight
A replication and critique of VPIN on the same instrument. The authors find that tick-rule VPIN is a poor predictor of short-run volatility, that it peaked after, not before, the flash crash, and that its apparent predictive content comes from a mechanical link to trading intensity created by classifying whole time bars as buys or sells. Once that link is removed, the relation between VPIN and volatility turns negative.

## Method
They rebuild the original tick-rule VPIN (TR-VPIN, one-minute time bars) and then construct controlled variants: fixed-volume-bin VPIN (FB-VPIN), which classifies bins of equal volume instead of time bars; transaction-level VPIN using the tick rule on individual trades; "uninformative" VPINs with randomized classification; and bulk-volume VPIN (BV-VPIN). Each is compared with trading volume and the VIX in correlations and in predictive regressions for future realized volatility over several horizons. They also reconstruct what an observer would have seen in real time on 6 May 2010.

## Data and sample
E-mini S&P 500 futures, full Time and Sales record from CME DataMine, January 2008 to July 2010, with timestamps to the second.

## Reported results
- Four stated conclusions: TR-VPIN is not a useful predictor of future return volatility, with VIX and other standard variables "generally vastly superior" even at very short horizons; TR-VPIN is mechanically related to trading intensity and its predictive content is subsumed by it; TR-VPIN did not reach a historical high before the crash, only after; and TR-VPIN has large idiosyncratic noise from the arbitrary starting point of the volume clock.
- TR-VPIN and VIX have a sample correlation of 0.52, while FB-VPIN is strongly negatively related to VIX.
- Controlling for trading volume, TR-VPIN is "if anything, negatively related to future return volatility".
- BV-VPIN has some forecast power for volatility, but the VIX roughly doubles the R-squared.
- Transaction-level and fixed-bin VPIN are negatively correlated with volatility because trade size and order-flow persistence fall when volatility is high.
- A signed version that lets imbalances offset reduced noise and appeared helpful around the crash, but the authors caution against adopting any metric without benchmark tests.

## Signal construction
Not a signal. It is a test protocol: before using any toxicity metric, regress the target (future realized volatility, future absolute return) on the metric together with trailing realized volatility, trailing volume or trade count, and an implied-volatility measure, and keep the metric only if its coefficient survives.

## Relevance to SOL perpetuals at minutes to hours
The mechanical effect transfers directly. Any VPIN built from time bars on SOL will rise when volume per bar rises, so it will look predictive of volatility simply because volume and volatility cluster. For SOL the natural benchmarks are trailing realized volatility, trade count, liquidation volume and a Deribit or Binance implied-volatility index. The finding that signed cumulative imbalance was more informative than unsigned VPIN supports using cumulative volume delta as the primary flow feature and treating VPIN as optional.

## Caveats
One instrument and 31 months. The read version is the 2013 working paper; the published text may differ in detail. The debate was adversarial and the VPIN authors published replies that are not covered by a note here. The result that true-order-imbalance VPIN falls in volatile periods was measured in a market dominated by small-lot high-frequency trading; whether trade size also shrinks in volatile SOL periods, where liquidations produce large prints, is untested.
