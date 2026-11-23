---
title: "Price discovery in bitcoin spot or futures?"
authors: "Baur, Dirk G.; Dimpfl, Thomas"
year: 2019
venue: "Journal of Futures Markets"
url: "https://econpapers.repec.org/RePEc:wly:jfutmk:v:39:y:2019:i:7:p:803-817"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "minutes"
tags: "price-discovery, cme, cboe, futures, spot, information-share, component-share, contrarian"
---

## Key insight
Per the abstract: after CBOE and CME launched bitcoin futures in December 2017, the spot price led the futures price, not the other way round. This contradicts the usual result from mature markets that futures lead, and the authors attribute it to the spot market's higher volume and longer trading hours compared with the restricted-access US futures.

## Method
Only the abstract was read. It states that the authors "rely on the information share methodology of Hasbrouck (1995) and Gonzalo and Granger (1995)". Sampling frequency, lag structure and spot venue selection are not confirmed.

## Data and sample
CBOE and CME bitcoin futures against bitcoin spot, starting from the December 2017 futures launch. Exact end date, spot exchanges and frequency: not confirmed.

## Reported results
From the abstract only:
- "The spot price leads the futures price."
- The authors "attribute this result to the higher trading volume and the longer trading hours of the globally distributed bitcoin spot market, compared to the relatively restricted access to the US-based futures markets".
No numerical information or component shares were available in what I read. The journal reference is Journal of Futures Markets, 2019, vol. 39, issue 7, pages 803-817.

## Signal construction
Not a signal. It is a counterexample to the rule "derivatives lead". The operational rule it supports is: leadership follows volume and trading hours, so identify the leader empirically (by information share on current data) rather than by instrument type.

## Relevance to SOL perpetuals at minutes to hours
The early CME/CBOE situation resembles Kalshi today: a newly listed, access-restricted, low-leverage US derivative next to a much larger global market that trades around the clock. The paper's result predicts the new regulated derivative follows the big market. For SOL the "big market" is offshore perps plus Binance/Coinbase spot. Kalshi trades 24/7, which removes the trading-hours explanation, so the volume and access channel would have to carry the effect; that needs testing.

## Caveats
Abstract-only; the article is closed access and no open copy was found. Later work disagrees: Alexander and Heck (2020) find offshore derivatives lead both CME and spot, and a search-result summary of Frino et al. (2025), which I did not open, says futures generally lead spot at 1-second sampling. Differences in sampling frequency probably explain part of the conflict, because coarse sampling widens Hasbrouck bounds and favours the smoother series. The sample is the first months of a new, thin futures market.
