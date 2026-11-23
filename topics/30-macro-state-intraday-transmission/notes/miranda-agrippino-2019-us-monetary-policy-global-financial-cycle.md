---
title: "US Monetary Policy and the Global Financial Cycle"
authors: "Miranda-Agrippino, Silvia; Rey, Helene"
year: 2019
venue: "NBER Working Paper 21722, revised March 2019 (the version read; the published version is usually cited as Review of Economic Studies, 2020)"
url: "https://www.nber.org/system/files/working_papers/w21722/w21722.pdf"
pdf: "sources/30-macro-state-intraday-transmission/miranda-agrippino-2019-us-monetary-policy-global-financial-cycle.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "multi-day"
tags: "global-financial-cycle, global-factor, risk-appetite, monetary-policy, dynamic-factor-model, state-variable, pre-2020"
---

## Key insight
A single global factor explains about a fifth of the common variation in risky asset prices worldwide, and it falls significantly after a US monetary tightening. The tightening also brings deleveraging by global banks, a rise in aggregate risk aversion, wider corporate bond spreads and a retrenchment of cross-border credit. This is the reference definition of the global financial cycle and of the global factor that later risk-appetite measures are benchmarked against.

## Method
A dynamic factor model with global, regional and (in some specifications) sector factors fitted to a large panel of end-of-month risky asset prices: equities from all major markets, corporate bond indices and commodity prices excluding precious metals. A proxy for aggregate risk aversion is obtained as the inverse of the component of the factor left after removing global realised variance (monthly sums of squared daily MSCI World returns). US monetary policy shocks are identified in a Bayesian VAR with an external instrument built from 30-minute surprises in federal funds futures around FOMC announcements (the three-month-ahead FF4 contract, summed within the month).

## Data and sample
858 price series from North America, Latin America, Europe, Asia Pacific and Australia, monthly, 1990 to 2012; a narrower panel (US, Europe, Japan, commodities) extends back to 1980. Pre-2020; no crypto.

## Reported results
- One global factor accounts for over 20 percent of the common variation in risky asset prices across continents.
- The factor co-moves with implied volatility indices (VIX, VSTOXX, VFTSE, VNKY); its relation to credit-spread measures is somewhat looser.
- After a contractionary US monetary policy shock the global factor contracts significantly, global banks in the US and Europe deleverage, the risk-aversion proxy surges, international corporate bond spreads rise on impact, and global credit and cross-border flows fall.
- The responses hold for countries with floating exchange rates.

## Signal construction
Not an intraday signal. The global factor is a monthly state variable. A bot can approximate it at daily frequency with the first principal component of returns on a broad set of liquid risky assets (regional equity index futures, credit indices, industrial commodities), accumulated into a level and compared with its own trend. Chari et al. report that a one-standard-deviation risk-off shock in their daily index coincides with a fall of about four standard deviations in this factor, so a daily risk-on/risk-off index can serve as its high-frequency counterpart.

## Relevance to SOL perpetuals at minutes to hours
It sets the prior for what a macro regime gate should measure: the common component of global risky assets, driven in part by US policy. Topic 02 holds evidence that a crypto factor co-moves with equity-like factors and responds to Fed tightening at daily to monthly horizons. For a minutes-to-hours bot the factor's value is as a slow conditioning variable (leverage and directional bias), with the caveat that no source in this topic shows it improves intraday crypto decisions.

## Caveats
Monthly data ending in 2012; the factor is estimated with full-sample smoothing and is not real-time. Other authors cited by Chari et al. find the VIX link to capital flows weakened after 2008. The monetary shock instrument is the kind Bauer and Swanson show to be predictable. Nothing here addresses lead or lag at short horizons.
