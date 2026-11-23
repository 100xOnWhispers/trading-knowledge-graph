---
title: "Misguided Price Discovery: When Overshooting Is Mistaken for Leadership"
authors: "Shen, Shulin; Huang, Xin; Zuo, Yuehua; Zivot, Eric"
year: 2026
venue: "Working paper, University of Washington Department of Economics (dated January 15, 2026)"
url: "https://econ.washington.edu/sites/econ/files/documents/research/Misguided_Price_Discovery.pdf"
pdf: "sources/05-price-discovery-cross-venue/shen-2026-misguided-price-discovery-overshooting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "multi"
horizon: "seconds"
tags: "price-discovery, overshooting, liquidation-cascade, perp-vs-spot, ipes, binance, methodology"
---

## Key insight
Modern price-discovery metrics (ILS, PILS, NLS, CovIS) name as leader the market with the largest instantaneous response to a permanent shock. That rule breaks when a market overshoots or first moves the wrong way, which is what leveraged perpetuals do in liquidation cascades. The authors propose ranking markets by how close their initial response is to the long-run effect, and show that under this rule Binance BTC spot, not the perp, leads during a cascade.

## Method
Structural moving-average representation of a VECM with long-run permanent responses normalized to one. Let d0_i be market i's contemporaneous response to the permanent shock. Instantaneous pricing error is |d0_i - 1|. The Instantaneous Pricing Efficiency Share is

IPES_i = exp(-|d0_i - 1|) / sum_j exp(-|d0_j - 1|).

It penalizes underreaction (d0 < 1), overshooting (d0 > 1) and perverse responses (d0 < 0) alike. Evaluated in simulations of partial-adjustment and dominant-satellite models, then in two event studies with rolling VECMs.

## Data and sample
(1) SPY versus IVV during the 2010 Flash Crash. (2) Binance BTC/USDT spot versus perpetual futures, 1-second transaction data on January 3, 2024, rolling 60-minute windows with a 5-minute step.

## Reported results
- Before the January 3, 2024 crash, responses sit in roughly (0.5, 1) with the perpetual slightly larger, "suggesting that it leads price discovery under normal market conditions".
- Around 12:00 UTC both markets briefly show perverse responses (d0 < 0). Afterwards spot rebounds to about 0.7-1 while the perpetual overshoots above 1.25.
- The spot leadership share under NLS/PILS collapses briefly toward zero and otherwise sits around 30-40%; CovIS stays around 35-45%; IPES assigns spot a share peaking above 50%.
- In simulations, magnitude-based measures misclassify leadership under overshooting; IPES matches the theoretical benchmark (for example exactly 50.00% in a symmetric case).

## Signal construction
Primarily a diagnostic, but it suggests a regime feature. On rolling windows of 1-second Binance SOL spot and perp mids, estimate the VECM, recover d0 for each market, and track (a) IPES of spot and (b) a flag for perp d0 > 1 or < 0. When the perp is overshooting, the spot price (or the CF spot index) is the better estimate of fair value and perp moves are more likely to partially revert.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant: Kalshi's funding and index reference a spot index (CME CF real-time index), while offshore perps are the usual "leader". In cascades, following the offshore perp tick-for-tick means importing its overshoot. A bot should distinguish normal regimes (perp leads, follow it) from stress regimes (perp overshoots, anchor to spot). Needs re-estimation on SOL, where leverage and liquidation intensity differ from BTC.

## Caveats
Two hand-picked episodes; one day of crypto data; no out-of-sample trading test. Structural identification rests on the unit long-run normalization. Working paper, not yet peer reviewed as far as confirmed. The exponential mapping in IPES is a design choice.
