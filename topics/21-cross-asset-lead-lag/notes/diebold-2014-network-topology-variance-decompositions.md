---
title: "On the Network Topology of Variance Decompositions: Measuring the Connectedness of Financial Firms"
authors: "Diebold, Francis X.; Yilmaz, Kamil"
year: 2014
venue: "Journal of Econometrics 182(1), 119-134 (NBER Working Paper 17490, October 2011, read)"
url: "https://www.nber.org/system/files/working_papers/w17490/w17490.pdf"
pdf: "sources/21-cross-asset-lead-lag/diebold-2014-network-topology-variance-decompositions.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "21-cross-asset-lead-lag"
asset_class: "equities"
horizon: "daily"
tags: "connectedness, spillover, variance-decomposition, var, network, methodology"
---

## Key insight
Forecast-error variance decompositions from a vector autoregression define a weighted, directed network among assets. Row sums, column sums and their differences give "from others", "to others" and "net" connectedness for each asset, and the grand off-diagonal share gives one total connectedness number. This is the framework that nearly every crypto spillover study uses, so its definitions and its limits need to be understood before reading that literature.

## Method
Fit a VAR(p) to N series (returns or log realized volatilities). For horizon H, let d_ij be the share of asset i's H-step forecast-error variance due to shocks to asset j, from the generalized variance decomposition (Koop, Pesaran and Potter; Pesaran and Shin), which does not depend on variable ordering, with rows normalized to sum to one.

- Pairwise directional connectedness from j to i: C(i<-j) = d_ij. Net pairwise: d_ji - d_ij.
- From others to i: sum over j != i of d_ij. To others from j: sum over i != j of d_ij. Net total: to minus from.
- Total connectedness: sum of all off-diagonal d_ij divided by N.

Dynamics come from re-estimating on a rolling window. The paper uses a VAR(3), H = 12 days and a 100-day window, and examines nearby horizons and alternative window widths. It notes that connectedness depends on the horizon because a shock may reach another asset only with a lag, relating the measure to multi-step Granger causality.

## Data and sample
Daily realized volatilities, built from high-frequency TAQ data, of the stocks of 13 major US financial institutions, 1999 to 2010.

## Reported results
- Full-sample total volatility connectedness is 78%.
- "From others" ranges narrowly between 70% and 82% across firms, while "to others" ranges from 53% (Fannie Mae) to 106% (Citigroup): firms differ much more as transmitters than as receivers.
- The largest pairwise link is Freddie Mac to Fannie Mae (22%), with 17.6% in the reverse direction.
- The rolling index moves with stress events; the text describes total volatility connectedness jumping up from a low of around 56% in February 2007 as the crisis developed, and earlier jumps of roughly 7 to 15 points around episodes in 2000-2002.

## Signal construction
Not a directional signal. A regime and feature-selection tool. For a bot: fit a rolling VAR on 5-minute or hourly returns (or realized volatilities) of SOL, BTC, ETH, a US equity index future and one or two other large coins; compute H-step generalized decompositions; track (a) total connectedness as a "one-factor market" indicator, (b) SOL's "from BTC" and "from equities" shares, (c) net transmitter rankings. High total connectedness means SOL-specific signals matter less and market-wide ones more; a rise in "from equities" during US hours argues for adding equity-futures features.

## Relevance to SOL perpetuals at minutes to hours
The measure is frequency-agnostic and can be run intraday. It answers "how much of SOL's variance comes from BTC shocks at horizon H", which is the right question for deciding how much weight BTC features deserve at 5 minutes versus 4 hours. It does not say whether those shocks are predictable in advance: most of the measured connectedness in crypto is contemporaneous co-movement within the sampling interval.

## Caveats
Linear, Gaussian and window-dependent. The generalized decomposition attributes contemporaneous correlation to both assets, so "net transmitter" labels can reflect who is more volatile, not who moves first. Results are sensitive to window length, H and the set of included assets. High connectedness is not evidence of exploitable lead-lag. The application is to US financial stocks, not crypto.
