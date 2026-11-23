---
title: "The prevalence of price overreactions in the cryptocurrency market"
authors: "Borgards, Oliver; Czudaj, Robert L."
year: 2020
venue: "Journal of International Financial Markets, Institutions and Money, vol. 65"
url: "https://ideas.repec.org/a/eee/intfin/v65y2020ics1042443120300780.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "minutes"
tags: "overreaction, intraday, large-moves, reversal, cross-asset-comparison, abstract-only"
---

## Key insight
According to the abstract as summarized on the RePEc record, price overreactions are highly prevalent in twelve cryptocurrencies at daily and intraday frequencies, at rates broadly comparable to US stocks. A strategy that trades the overreactions earns significantly more in cryptocurrencies than in stocks, mainly because crypto overreactions are larger. Negative overreactions are slightly more frequent than positive ones. Only the abstract-level description was read.

## Method
From the record: a "dynamic modeling approach" to identifying overreactions, applied at daily and several intraday frequencies, with a comparison against the US stock market and an overreaction trading strategy. The definition of an overreaction, the frequencies used, the correction window and the treatment of transaction costs were not visible. A companion paper by the same authors ("Features of overreactions in the cryptocurrency market", Quarterly Review of Economics and Finance, 2021) was seen only in a search summary; it applies random-forest classification to predict overreactions and reports that features describing the price path before the event classify best. It was not opened and is not noted separately.

## Data and sample
Twelve cryptocurrencies and US stocks, daily and intraday. Period, venues and exact frequencies not seen.

## Reported results
Abstract-level only:
- Overreactions are "highly prevalent" in crypto at all frequencies examined.
- Prevalence is broadly comparable to stocks.
- Returns from an overreaction strategy are significantly higher for cryptocurrencies, attributed to the larger size of the overreactions.
- Negative overreactions are slightly more common than positive ones.
- No magnitudes, hit rates, horizons or cost assumptions were seen.
- Scope record: horizon intraday to daily (exact bars not confirmed); conditioning variable a large move identified dynamically; sign reversal (an overreaction is by definition followed by a correction); costs not confirmed.

## Signal construction
Cannot be specified from what was read. The general form in this literature is: flag a move whose size exceeds a volatility-scaled threshold, then measure the return over a following window in the opposite direction. The specific thresholds and windows of this paper need the full text.

## Relevance to SOL perpetuals at minutes to hours
This is the peer-reviewed study most often cited for intraday overreaction in crypto and covers more coins than De Nicola (2021), so it is the natural check on that paper's Bitcoin-only result. Its reported direction (reversal after large moves, larger in crypto than in equities) agrees with De Nicola and with Kitron and Wengrowicz (2026, topic 08), and disagrees with the continuation that Caporale and Plastun (2019) report on overreaction days. Until the full text is read, it supports the direction of the effect but not any parameter choice.

## Caveats
Abstract-only. Whether the strategy return is net of spreads and fees is the decisive unknown, since Kitron and Wengrowicz find the gross 15-minute reversal edge is far below costs. Identification of an "overreaction" by a subsequent correction can build the reversal into the definition; how the paper avoids this was not seen. Published in 2020; the exact sample period was not seen.
