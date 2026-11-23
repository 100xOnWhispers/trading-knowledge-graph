---
title: "Bitcoin Liquidity: Is 'Untrusted' Money More Important For Bitcoin"
authors: "Howell, Michael"
year: 2026
venue: "Capital Wars (Substack newsletter), 16 August 2026"
url: "https://capitalwars.substack.com/p/bitcoin-liquidity"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "30-macro-state-intraday-transmission"
asset_class: "crypto"
horizon: "multi-day"
tags: "global-liquidity, lead-lag-claim, bitcoin, solana, practitioner, correlation, no-out-of-sample"
---

## Key insight
The best-known practitioner voice on global liquidity claims that a crypto basket tracks changes in global liquidity with a lead of about 13 weeks, and that Bitcoin's sensitivity to liquidity is very high (a beta of roughly 7.5 to 9 on three-month changes). The post offers correlations and charts, with no significance tests, no out-of-sample check and no stability analysis. It is recorded here as the source of a widely repeated belief, not as evidence for it.

## Method
As described in the post (read through a fetched text rendering; charts are images and were not viewed). Global Liquidity is cited as a 195 trillion USD aggregate; its construction is not explained in this post. A crypto benchmark, BES, is 60 percent Bitcoin, 30 percent Ethereum and 10 percent Solana. The headline comparison uses six-week log changes of both series at weekly frequency with liquidity advanced 13 weeks. A second exercise splits liquidity into trusted and untrusted pools by weighting each economy's liquidity by survey estimates of Bitcoin ownership, then relates three-month log changes in Bitcoin to each pool advanced three months.

## Data and sample
Weekly data since 2021 for the headline chart; monthly data from 2020 for the pools; regression period stated as 2020 to 2026. Post-2020 only. Solana enters through a 10 percent basket weight; no separate SOL result.

## Reported results
- Crypto basket and Global Liquidity are described as tightly related on six-week changes with a 13-week lead for liquidity.
- Trusted liquidity: correlation with Bitcoin price changes about 0.5, beta about 7.5. Stated implication: a 10 percent annualised liquidity expansion is consistent with roughly a 75 percent Bitcoin move over the following three months, all else equal.
- Untrusted liquidity: correlation about 0.4, beta about 9.0.
- The author calls the ownership data imperfect and approximate, and says the trusted and untrusted division is not sufficiently rigorous.
- No p-values, R-squared, sample sizes, confidence intervals or out-of-sample tests are given.

## Signal construction
As claimed: six-week (or three-month) log change in a global liquidity aggregate, shifted forward 13 weeks, as a slow directional bias for a crypto basket. The aggregate itself is proprietary. Public stand-ins used elsewhere are central bank balance sheets net of the Treasury account and reverse repo, or dollar-converted global M2; no source read for this topic tests those against crypto with out-of-sample or sign-stability checks.

## Relevance to SOL perpetuals at minutes to hours
None directly: the claimed lead is a quarter of a year and the frequency is weekly to monthly. It matters only as a candidate input to a weekly risk budget, and only after testing. The tests it would need are stated in the synthesis: a fixed lag chosen before the test period, rolling-window sign stability, comparison with a dollar-index-only benchmark (dollar-denominated liquidity rises mechanically when the dollar falls), and overlapping-observation corrections. The neighbouring topic 02 holds a note that records evidence against a fixed M2 lead.

## Caveats
A subscription newsletter, not research with a stated methodology. Smoothed overlapping changes over five to six years give very few independent observations, so a correlation of 0.5 carries little weight. Lead times differ within the post (13 weeks and three months). The beta-to-forecast step extrapolates from a correlation.
