---
title: "Risk-On Risk-Off: A Multifaceted Approach to Measuring Global Investor Risk Aversion"
authors: "Chari, Anusha; Dilts Stedman, Karlye; Lundblad, Christian"
year: 2023
venue: "NBER Working Paper 31907"
url: "https://www.nber.org/system/files/working_papers/w31907/w31907.pdf"
pdf: "sources/30-macro-state-intraday-transmission/chari-2023-risk-on-risk-off-multifaceted.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "daily"
tags: "risk-on-risk-off, risk-appetite, state-variable, principal-component, credit-spreads, vix, funding-liquidity, dollar"
---

## Key insight
Risk-on/risk-off can be defined operationally as variation in global investor risk aversion and measured daily as the first principal component of standardised changes in four groups of market variables: credit spreads, equity returns and implied volatility, funding liquidity, and currencies and gold. The resulting index is strongly right-skewed (risk-off) and fat-tailed, and it carries information the VIX alone does not. The authors argue the VIX has become a weaker proxy since 2008.

## Method
Daily changes in each constituent are signed so that positive means risk-off, normalised, scaled by historical standard deviation, and combined; the RORO index is the z-score of the first principal component. Constituents: (1) ICE BofA BBB option-adjusted spreads for the US and euro area and the Baa minus 10-year Treasury spread; (2) negative total returns on the S&P 500, STOXX 600 and MSCI Advanced Economies, and changes in VIX and VSTOXX; (3) average change in the G-spread on 2-, 5- and 10-year Treasuries, TED spread, LIBOR-OIS spread, and the bid-ask spread on 3-month bills; (4) growth of the trade-weighted dollar against advanced economies and the change in the gold price. Four sub-indices are built the same way and used in a variance decomposition. Applications: weekly panel regressions of EPFR emerging-market equity fund flows and MSCI returns on RORO shocks, and local projections out to 260 days.

## Data and sample
Daily market data; the index covers the global financial crisis through at least 2022 (the exact start date was not confirmed in the text read). Weekly EPFR country flows for emerging markets excluding China. The authors state the daily and weekly index is publicly available. No crypto.

## Reported results
- Skewness 1.56 and kurtosis 21.98. The largest risk-off readings exceed 11 standard deviations (March 2020), with the May 2010 flash crash, the August 2011 US downgrade and the Brexit vote also prominent.
- The equity and implied-volatility sub-index explains most of the index's variation; funding liquidity seldom matters except in the 2008 crisis; credit matters most for equity outflows.
- A one-standard-deviation risk-off shock is associated with emerging-market equity fund outflows of about 11 basis points of the prior week's allocation, about 1.79 billion USD per week at end-2022 assets.
- Return responses of emerging-market equities persist for at least 150 days with no reversal.
- A one-standard-deviation RORO shock coincides with a fall of about four standard deviations in the Miranda-Agrippino and Rey global factor.

## Signal construction
Daily regime gate. Inputs available to a bot: S&P 500 and Euro Stoxx futures returns, VIX and VSTOXX changes, an investment-grade credit spread or CDX index change, a dollar index return, gold return, and one funding spread. Standardise each by a trailing standard deviation, sign to risk-off, take the first principal component with fixed loadings estimated on history, and z-score. An intraday version can use the futures-traded subset (equity futures, VIX futures, dollar index futures, gold futures) updated every few minutes; that variant is not in the paper.

## Relevance to SOL perpetuals at minutes to hours
This is the cleanest published recipe for the daily risk state the bot needs, and the skew and tail statistics say the gate should be asymmetric: rare, very large risk-off readings matter more than ordinary variation. Whether SOL's intraday beta to equity futures, or the profitability of trend signals, differs across RORO states is untested. LIBOR-based constituents are discontinued and need replacement.

## Caveats
The index is contemporaneous, built from the same prices crypto reacts to; no evidence is offered that it leads anything at short horizons. Predictability evidence is for emerging-market equity returns at multi-day to multi-month horizons. Working paper. The principal-component loadings are full-sample.
