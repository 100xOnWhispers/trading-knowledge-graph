---
title: "Bitcoin Does Not Hedge Inflation"
authors: "Pinchuk, Mykola"
year: 2023
venue: "arXiv 2301.10117 (paper dated 30 May 2021)"
url: "https://arxiv.org/pdf/2301.10117"
pdf: "sources/02-crypto-macro-linkages/pinchuk-2023-bitcoin-not-hedge-inflation.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "minutes"
tags: "event-study, intraday, cpi, ppi, inflation-surprise, macro-announcements, altcoins"
---

## Key insight
Using one-minute prices in 30-minute windows around US macro announcements from 2013 to 2021, Bitcoin falls about 24 basis points per one-standard-deviation inflation surprise, and does not react to growth-related releases. Ethereum, Litecoin and Cardano show no significant reaction to any release type. The negative inflation response contradicts the inflation-hedge narrative and is not explained by co-movement with interest rates in the window.

## Method
Intraday event study. For each announcement the return is measured from 10 minutes before to 20 minutes after the release and regressed on the standardized surprise (actual minus survey forecast, scaled to unit standard deviation over 1997 to 2021). Announcements of the same type are pooled to raise power: a growth group and an inflation group (CPI and PPI). To test the interest-rate channel, window returns on five-year Treasury note futures are compared with Bitcoin window returns.

## Data and sample
Six coins: Bitcoin, Ethereum, Ripple, Litecoin, Cardano, Bitcoin Cash, at one-minute frequency. Bitcoin from March 2013 to May 2021; other coins start later. Nine announcement types released at 8:30 or 10:00 Eastern, with 99 to 101 observations each between 1 January 2013 and 12 May 2021. The exchange or data vendor for prices is not stated in the parts read.

## Reported results
- Growth news: no coin reacts; t-statistics below 0.5 and less than 2 basis points per standard deviation, with 268 to 680 pooled observations depending on the coin.
- Inflation news: Bitcoin -24 basis points per standard deviation (t = 2.44), explaining 2.5 percent of announcement-window return variation. Bitcoin Cash -18 basis points. Ripple -11 basis points (t = 1.0, insignificant). Ethereum, Litecoin and Cardano insignificant.
- Rates channel: no negative co-movement between Bitcoin and rates in the inflation window; the estimated co-movement is positive and insignificant (t = 0.9).
- The author's preferred explanation is a consumption-savings channel, supported by a negative Bitcoin response to consumption news; this is the more speculative part.
- Bitcoin window returns are centered on zero with no announcement premium.

## Signal construction
On CPI and PPI release at 8:30 Eastern: compute z = (actual minus consensus) / historical standard deviation of the gap. Expected 30-minute Bitcoin return is roughly -0.24 percent times z on this sample. A bot would enter within the first seconds after the print in the direction of -z and hold for up to 20 minutes, or use the sign of z only as a filter on other signals. Parameters: window (-10, +20) minutes, pooled CPI and PPI coefficient, re-estimated on a rolling basis.

## Relevance to SOL perpetuals at minutes to hours
Horizon and event type match the bot's use case. Two findings bear on SOL: the response existed for Bitcoin even before the 2021 institutional era, and it did not show up in the other smart-contract coins of that period, so transfer to SOL cannot be assumed and must be estimated on SOL data from 2021 onward. The effect size, 24 basis points per standard deviation with 2.5 percent explained variance, is small relative to Bitcoin's five-minute volatility (about 0.4 percent in the Benigno and Rosa sample), so execution cost and speed decide whether it is tradable.

## Caveats
Single-author working paper, not peer reviewed. Only two inflation release types, so about 200 inflation events. Sample ends May 2021, before the high-inflation period when CPI releases became the dominant macro event. No transaction costs or latency analysis. Pooling CPI and PPI assumes equal coefficients. The consumption-savings interpretation rests on indirect evidence.
