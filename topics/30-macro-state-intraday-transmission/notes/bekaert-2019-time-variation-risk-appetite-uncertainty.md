---
title: "The Time Variation in Risk Appetite and Uncertainty"
authors: "Bekaert, Geert; Engstrom, Eric C.; Xu, Nancy R."
year: 2019
venue: "NBER Working Paper 25673 (the version read; the published version is usually cited as Management Science, 2022)"
url: "https://www.nber.org/system/files/working_papers/w25673/w25673.pdf"
pdf: "sources/30-macro-state-intraday-transmission/bekaert-2019-time-variation-risk-appetite-uncertainty.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "daily"
tags: "risk-aversion, uncertainty, variance-risk-premium, credit-spread, state-variable, asset-pricing-model, pre-2020"
---

## Key insight
Risk aversion (a price-of-risk state) and economic uncertainty (a quantity-of-risk state) are different things and can be separated using asset prices. In a no-arbitrage model for equities and corporate bonds, the extracted risk-aversion process is almost entirely spanned by the equity variance risk premium (risk-neutral variance minus expected realised variance), while uncertainty is spanned mostly by credit spreads and corporate bond volatility. Both can be computed daily from observable series.

## Method
A dynamic asset pricing model with habit-like stochastic risk aversion that is not perfectly correlated with fundamentals, and heteroskedastic, non-Gaussian shocks to macro fundamentals and cash flows. Estimation by GMM on monthly data. Risk aversion and uncertainty are then projected on six financial instruments so that they can be tracked at high frequency: (1) credit spread (Moody's Baa minus 10-year Treasury), (2) detrended dividend or earnings yield, (3) realised equity return variance, (4) risk-neutral equity variance (VIX squared), (5) realised corporate bond return variance, (6) term spread.

## Data and sample
US monthly data, June 1986 to February 2015 (345 months) for estimation; industrial production as the macro fundamental; CRSP equity returns; VIX and VXO; Dow Jones corporate bond index. The authors state the indices are posted on an author web page. Pre-2020; no crypto.

## Reported results
- Risk aversion loads positively on risk-neutral equity variance and negatively on realised variance. Regressing risk aversion on the variance premium gives R-squared of 96.2 percent; 96.8 percent of the variance premium's variance is accounted for by risk aversion.
- Risk aversion accounts for 85 percent of the variance of risk-neutral variance, so VIX is mostly, not purely, a risk-aversion gauge.
- Model-implied and observed risk-neutral variance correlate at 90.06 percent, although the model misses the sharpest VIX spikes.
- For uncertainty, the financial instruments give an R-squared near 50 percent, with the credit spread contributing almost 63 percent of the explained variation.
- Risk aversion mean-reverts much faster than habit models imply.
- Model-implied risk premia predict equity and corporate bond excess returns better than standard instruments; the uncertainty index predicts output growth negatively.

## Signal construction
Two daily state variables. Risk-aversion proxy: variance premium = VIX squared (scaled to the horizon) minus a forecast of realised variance from lagged realised variance and lagged VIX squared. Uncertainty proxy: a fitted combination dominated by the Baa-Treasury spread plus corporate bond realised variance. Using both lets a gate distinguish a selloff driven by repricing of risk (fast-reverting) from one driven by rising fundamental uncertainty (slow).

## Relevance to SOL perpetuals at minutes to hours
The distinction is useful for a regime gate: Hu et al. show returns follow spikes in the price of risk, while persistent uncertainty states should mean lower leverage for longer. The crypto analogue of the variance premium (DVOL squared minus realised variance) is covered in topic 20. Whether the equity variance premium conditions SOL's intraday behaviour is untested.

## Caveats
A structural model with many assumptions; the spanning coefficients are full-sample. Monthly estimation, daily application. Sample ends February 2015. The variance premium needs a realised-variance forecast, which adds model choice. Nothing here is intraday.
