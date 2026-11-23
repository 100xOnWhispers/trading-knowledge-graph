---
title: "What do price discovery metrics really measure?"
authors: "Putnins, Talis J."
year: 2013
venue: "Journal of Empirical Finance"
url: "https://opus.lib.uts.edu.au/bitstream/10453/27707/3/Price%20discovery%20metric%20simulations%2020130506%20FINAL.pdf"
pdf: "sources/05-price-discovery-cross-venue/putnins-2013-price-discovery-metrics-measure.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "05-price-discovery-cross-venue"
asset_class: "multi"
horizon: "n/a"
tags: "information-share, component-share, information-leadership-share, noise, methodology, simulation"
---

## Key insight
Hasbrouck's information share (IS) and the Gonzalo-Granger / Harris-McInish-Wood component share (CS) only identify "who moves first" when the competing price series are equally noisy. When noise differs, both metrics reward the less noisy series, so a slow but quiet market can appear to dominate. The information leadership share (ILS), built from IS and CS together, cancels the noise term and isolates speed of information incorporation.

## Method
Monte Carlo simulation of a two-price structural model in which each price tracks a common random-walk fundamental with its own delay and its own noise level; 1,000 simulated samples per parameter setting. IS is computed under both Cholesky orderings and averaged (Baillie et al. 2002). Following Yan and Zivot (2010):

IL1 = | (IS1 / IS2) * (CS2 / CS1) |, IL2 = | (IS2 / IS1) * (CS1 / CS2) |

ILS1 = IL1 / (IL1 + IL2), ILS2 = IL2 / (IL1 + IL2)

ILS above 0.5 means the series leads in impounding new information. The metric is defined only for bivariate systems. The paper then recomputes ILS for four published empirical studies.

## Data and sample
Simulated data; plus reported IS and CS values taken from four earlier empirical studies (for example Rittler 2012 on EU emission allowances spot versus futures).

## Reported results
- "Only ILS reliably measures price discovery in a 'who moves first' sense"; ILS makes zero attribution errors across the simulated grid, while IS and CS regions "cut diagonally across the parameter space".
- Example from the simulations: with p2 slower (7-second delay versus 5 seconds) but less noisy, IS2 = 0.70 and CS2 = 0.85, wrongly naming p2 dominant; raising p2's noise drops IS2 to 0.27 and CS2 to 0.37 with no change in relative speed.
- IS weights speed more heavily than CS does.
- Re-analysis of the four studies with ILS reverses conclusions "in many cases", including Rittler's futures-dominance result.

## Signal construction
Not a signal. It is the correction to apply when ranking venues. For each venue pair (Kalshi vs Binance, perp vs spot), estimate the VECM, compute IS (average of both orderings) and CS (normalized orthogonal complement of the error-correction loadings), then ILS. Use ILS to decide which feed is the leader and IS/CS to judge which is cleaner.

## Relevance to SOL perpetuals at minutes to hours
This matters a great deal for a new, thin venue. Kalshi's SOL perp will have wider spreads and sparser quotes than Binance, so IS and CS will be biased against it by noise alone; equally, a slow index-like series can look "dominant" because it is smooth. ILS is the appropriate bivariate metric for asking whether Kalshi ever moves first. Much of the crypto literature (Baur-Dimpfl, Alexander-Heck) reports IS/CS only, so its leadership claims partly reflect relative noise.

## Caveats
Simulation evidence under one structural model; ILS is bivariate only and can be unstable when IS or CS is near 0 or 1. Shen et al. (2026) show ILS-type magnitude measures can mistake overshooting for leadership during stress. I read the accepted working-paper version, not the typeset journal article.
