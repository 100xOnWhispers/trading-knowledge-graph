---
title: "Forecast Combinations"
authors: "Timmermann, Allan"
year: 2006
venue: "Handbook of Economic Forecasting, vol. 1, chapter 4 (Elsevier); draft dated November 2004 read"
url: "https://econweb.ucsd.edu/~atimmerm/combine.pdf"
pdf: "sources/29-signal-combination-online-adaptation/timmermann-2006-forecast-combinations-handbook.pdf"
access: "full-text"
source_type: "book"
evidence_grade: "A"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "forecast-combination, equal-weights, shrinkage, trimming, estimation-error, time-varying-weights"
---

## Key insight
The standard reference on why combining forecasts works and why simple averages are so hard to beat. Combination is a diversification argument applied to forecast errors: it hedges against model misspecification and against breaks that hit individual models differently. Estimated "optimal" weights lose to equal weights when the number of models is large relative to the sample, when error variances are similar and when the environment is unstable, because weight estimation error swamps the theoretical gain.

## Method
Theory plus literature survey plus Monte Carlo. Under squared-error loss the optimal linear weights minimise w'Σw subject to weights summing to one, where Σ is the forecast-error covariance matrix. Equal weights are optimal in population only when error variances are identical and pairwise correlations are identical. The chapter then reviews estimators of the weights: least squares (Granger and Ramanathan), recursive performance-based weights, relative-performance weights that ignore correlations (weight proportional to inverse mean squared error raised to a power; power 0 gives equal weights, power 1 gives inverse-MSE weights), rolling-window and exponentially discounted weights (Bates and Granger), regime-switching and time-varying-parameter weights, shrinkage toward equal weights (Diebold and Pauly), and trimming or clustering before combining.

## Data and sample
Survey of studies mostly on macroeconomic series (Stock and Watson; the M competitions) at monthly and quarterly frequency. The chapter's own simulation uses a factor model with 4 to 20 forecasts, samples of 100, 500 and 1,000 observations, and seven designs (equal quality, heterogeneous quality, persistent factors, block factor loadings, biased forecasts).

## Reported results
- Empirical regularities stated by the author: (i) parameter estimation error drives the ranking of schemes, so shrinkage and correlation-ignoring weights do well; (ii) trimming the worst models and clustering can give large gains with many forecasts; (iii) some limited time variation in weights can help.
- Selecting the single model with the best track record is usually worse than combining; rankings both persist and "cross".
- The optimal degree of shrinkage toward equal weights is found to be large in the cited studies; in the chapter's simulation with 20 models and 100 observations the strongest shrinkage cut MSE by close to 10% relative to unconstrained least squares.
- Equal weights degrade as heterogeneity in model quality rises; regressing the target on an intercept and the equal-weighted forecast was the best scheme in most designs with many models.
- Evidence on time-varying weights is "mixed": Stock and Watson are quoted as finding that more time variation and heavier discounting make forecasts less robust. One cited trimming study found the best result from keeping only the top 20% of models.
- Shrinkage and trimming pull in opposite directions; trimming first and then shrinking is suggested.

## Signal construction
Not a signal. It is the design guide for the combiner layer. A defensible default for a bot: (1) put every signal's forecast on the same scale; (2) drop signals whose recent out-of-sample loss is in the worst tail; (3) weight the survivors equally or by inverse recent MSE; (4) if weights are estimated, shrink them hard toward equal; (5) allow only slow drift in weights.

## Relevance to SOL perpetuals at minutes to hours
High as a prior. Short-horizon crypto signals have low and unstable signal-to-noise, similar error variances and frequent breaks, which is the configuration in which equal or inverse-MSE weights are expected to win. What needs re-testing: the loss here is trading profit after fees, not MSE, and the chapter itself shows that results under asymmetric loss can reverse in favour of estimated weights.

## Caveats
The copy read is the 2004 draft, not the printed 2006 chapter, and its PDF font encoding required decoding, so some formulas were not legible. Evidence is macro forecasting at low frequency; nothing is intraday or cost-aware. The author stresses that counter-examples exist for every regularity.
