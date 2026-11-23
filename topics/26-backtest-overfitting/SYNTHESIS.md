# Backtest methodology, overfitting and alpha decay: synthesis

Scope: how to test strategies without fooling yourself. This covers multiple-testing corrections, Sharpe ratio inference, the probability of backtest overfitting, purged and combinatorial cross-validation, walk-forward design, perpetual-specific look-ahead and cost errors, fill modelling, post-discovery decay, and live monitoring. It applies to hand-built rules and equally to machine-learning, reinforcement-learning and evolutionary searches, which are treated here as large automated multiple-testing engines. Model families themselves belong to topics 22 to 25.

Twenty notes: sixteen from full text, two abstract-only (Lo 2002; McLean and Pontiff 2016), two from software documentation.

## What the literature agrees on

1. **The best of many backtests is biased upward, and the bias is quantifiable.** With zero true skill, ten independent trials on one year of data produce an expected best annualized Sharpe of about 1.57, and five years of data support only about 45 independent trials before a Sharpe of 1 is expected by luck ([Bailey et al. 2014](notes/bailey-2014-pseudo-mathematics-financial-charlatanism.md)). White's example makes the same point empirically: a naive p-value of 0.0036 becomes 0.2040 once the 3,654-model search is accounted for ([White 2000](notes/white-2000-reality-check-data-snooping.md)).

2. **Under the null, more bars do not help; more calendar time does.** The variance of an annualized Sharpe estimate at zero true Sharpe depends on years, not sampling frequency ([Bailey et al. 2014](notes/bailey-2014-pseudo-mathematics-financial-charlatanism.md)). Serial correlation makes naive annualization wrong, by as much as 65% in Lo's hedge fund example ([Lo 2002](notes/lo-2002-statistics-sharpe-ratios.md), abstract only).

3. **The number of trials must be recorded, and correlation between trials matters.** Every correction needs a trial count: the deflated Sharpe ratio ([Bailey and Lopez de Prado 2014](notes/bailey-2014-deflated-sharpe-ratio.md)), the haircut Sharpe ([Harvey and Liu 2015](notes/harvey-2015-backtesting.md)), t-ratio hurdles near 3.0 ([Harvey, Liu and Zhu 2014](notes/harvey-2014-cross-section-expected-returns.md)), and the research protocol ([Arnott, Harvey and Markowitz 2019](notes/arnott-2019-backtesting-protocol-machine-learning.md)). Highly correlated trials cost less than independent ones.

4. **A single hold-out is weak, and a hold-out consulted more than once is in-sample.** This is stated by [Bailey et al. 2015](notes/bailey-2015-probability-backtest-overfitting.md) and [Arnott et al. 2019](notes/arnott-2019-backtesting-protocol-machine-learning.md). The constructive answers are combinatorial schemes (CSCV for selection processes; purged combinatorial CV for fitted models, [skfolio documentation](notes/skfolio-2026-combinatorial-purged-cross-validation.md)) and a final period touched once ([Mroziewicz and Slepaczuk 2026](notes/mroziewicz-2026-walk-forward-window-optimization-bitcoin.md)).

5. **Expect to keep about half.** Published equity predictors lose 26% out of sample and 58% after publication ([McLean and Pontiff 2016](notes/mclean-2016-academic-research-destroy-predictability.md), abstract only); a replication finds a 43% Sharpe drop ([Falck, Rej and Thesmar 2021](notes/falck-2021-why-how-systematic-strategies-decay.md)); mined and peer-reviewed predictors both retain roughly 50% ([Chen, Lopez-Lira and Zimmermann 2022](notes/chen-2022-peer-reviewed-research-predict-returns.md)). Marginal backtests should be cut far more than strong ones ([Harvey and Liu 2015](notes/harvey-2015-backtesting.md)).

6. **Costs and execution assumptions move results as much as signals do.** On crypto perpetuals, fee-only and zero-cost runs raised Sharpe from 2.05 to 2.51 and 2.71 for one fixed configuration on 4-hour bars ([Deng 2025](notes/deng-2025-autoquant-execution-constrained-crypto-perps.md)). Passive fills must be modelled conservatively and calibrated live ([hftbacktest documentation](notes/hftbacktest-2026-order-fill-queue-models.md)).

7. **Automated search does not escape any of this.** A Bayesian tuner on BTC perpetuals left a probability of backtest overfitting of 0.586 ([Deng 2025](notes/deng-2025-autoquant-execution-constrained-crypto-perps.md)); reinforcement-learning hyperparameter sweeps on five-minute crypto data showed estimated overfitting probabilities from 8% to 21% depending on agent and validation scheme ([Gort et al. 2022](notes/gort-2022-deep-rl-crypto-backtest-overfitting.md)).

## Where it disagrees or is weak

- **How bad is the false-discovery problem?** Harvey, Liu and Zhu say most claimed findings are likely false. [Jensen, Kelly and Pedersen 2021](notes/jensen-2021-replication-crisis-finance.md) estimate replication near 84% with a Bayesian hierarchical model and argue attenuation is expected shrinkage. The dispute is partly about the size of the unobserved pool of failed trials, which is exactly the quantity an in-house search can record and the published literature cannot.
- **Does an economic rationale protect against overfitting?** Arnott, Harvey and Markowitz put it first in their protocol. Chen, Lopez-Lira and Zimmermann find theory-backed predictors survive no better than mined ones, and Falck et al. find the in-sample t-statistic is only a weak predictor of decay while complexity and outlier-sensitivity are better ones.
- **Reject or shrink?** Frequentist tools (Reality Check, [SPA](notes/hansen-2005-test-superior-predictive-ability.md), deflated Sharpe) give accept/reject answers; the Bayesian view shrinks the edge and sizes accordingly. Family-wise control versus false-discovery control is a design choice that depends on whether one strategy or an ensemble is traded.
- **Walk-forward versus combinatorial CV.** Gort et al. reject walk-forward on overfitting grounds; Mroziewicz and Slepaczuk keep walk-forward and tune its windows. Combinatorial schemes train on the future, which tests generalization but is not a deployment simulation. The one controlled comparison known to us (Arian, Norouzi and Seco 2024) could not be opened.
- **Crypto-specific evidence is thin and low grade.** The three crypto sources are preprints graded C. Gort's performance claim rests on one 58-day window in which every agent lost 35% or more. Nothing here measures decay rates of intraday crypto signals.
- **Not covered by any opened source:** survivorship and delisting bias in crypto universes (Ammann, Burdorf, Liebi and Stockl 2022 exists on SSRN but was inaccessible), exchange data quality (Alexander and Dakos 2020, inaccessible), strategy capacity, and latency modelling. Capacity appears only as an excluded assumption in Deng and in the no-impact warning of hftbacktest. See topic 09 for impact models and topic 06 for Kalshi specifics.
- **Estimating the effective number of independent trials** is acknowledged as the weak link by the deflated Sharpe paper itself.

## Candidate signals and methods

These are validation and monitoring methods, not alpha signals.

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Trial budget (MinBTL) | Years of data, target Sharpe, count of independent configurations | Research stage | A | [bailey-2014-pseudo-mathematics](notes/bailey-2014-pseudo-mathematics-financial-charlatanism.md) |
| Deflated Sharpe ratio | Winner's returns (SR, T, skew, kurtosis), variance of trial Sharpes, effective trial count | Research stage | A | [bailey-2014-deflated-sharpe-ratio](notes/bailey-2014-deflated-sharpe-ratio.md) |
| Haircut Sharpe and profit hurdle | Sharpe, sample length, autocorrelation, number of tests, average correlation | Research stage | A | [harvey-2015-backtesting](notes/harvey-2015-backtesting.md), [harvey-2014-cross-section](notes/harvey-2014-cross-section-expected-returns.md) |
| PBO by CSCV | Net return matrix of every configuration tried | Research stage | A (method), C (crypto use) | [bailey-2015-probability-backtest-overfitting](notes/bailey-2015-probability-backtest-overfitting.md), [gort-2022](notes/gort-2022-deep-rl-crypto-backtest-overfitting.md), [deng-2025](notes/deng-2025-autoquant-execution-constrained-crypto-perps.md) |
| Reality Check and SPA test | Per-period performance of every rule versus benchmark; stationary bootstrap | Research stage | A | [white-2000](notes/white-2000-reality-check-data-snooping.md), [hansen-2005](notes/hansen-2005-test-superior-predictive-ability.md) |
| Purged combinatorial CV | Features, labels with horizons, fold and purge sizes | Model fitting | D (documentation only here) | [skfolio-2026](notes/skfolio-2026-combinatorial-purged-cross-validation.md), [gort-2022](notes/gort-2022-deep-rl-crypto-backtest-overfitting.md) |
| Walk-forward with tuned windows and single-use final period | Bars, re-fit and look-back lengths, neighbourhood-smoothed Sharpe | Minutes to hours | C | [mroziewicz-2026](notes/mroziewicz-2026-walk-forward-window-optimization-bitcoin.md) |
| Strict perpetual backtest semantics | Closed-bar signals, next-bar fills, time-aligned funding, fee and slippage grid | Minutes to hours | C | [deng-2025](notes/deng-2025-autoquant-execution-constrained-crypto-perps.md) |
| Conservative fill and queue model | Tick trades and depth; trade-through rule; risk-averse queue | Tick to minutes | D | [hftbacktest-2026](notes/hftbacktest-2026-order-fill-queue-models.md) |
| Decay-risk scorecard | Parameter-neighbourhood Sharpe spread, outlier sensitivity, operation count | Research stage | B | [falck-2021](notes/falck-2021-why-how-systematic-strategies-decay.md) |
| Shrinkage of expected edge | Backtest edge, its standard error, family of related signals and venues | Sizing | A (equities) | [jensen-2021](notes/jensen-2021-replication-crisis-finance.md), [chen-2022](notes/chen-2022-peer-reviewed-research-predict-returns.md) |
| Probabilistic Sharpe ratio and minimum track record length | Live net returns per period, benchmark Sharpe | Live monitoring | A | [bailey-2012-sharpe-ratio-efficient-frontier](notes/bailey-2012-sharpe-ratio-efficient-frontier.md), [lo-2002](notes/lo-2002-statistics-sharpe-ratios.md) |
| Drawdown and time-under-water limits with autocorrelation | Mean, volatility and lag-1 autocorrelation of P&L | Live monitoring | B | [bailey-2014-stop-outs](notes/bailey-2014-stop-outs-serial-correlation-triple-penance.md) |
| Research protocol checklist | Written hypothesis, trial log, frozen sample, costs everywhere | Process | B | [arnott-2019](notes/arnott-2019-backtesting-protocol-machine-learning.md) |

## Open questions worth testing on SOL perps

1. What is the effective number of independent trials in a typical search here (indicator grid, Bayesian tuner, genetic programming run, reinforcement-learning sweep)? Cluster trial return series and compare deflated Sharpe under different estimates.
2. How large is the cost-ladder inflation at 1, 5, 15 and 60 minute horizons on SOL, using the strict semantics of Deng 2025 with taker fills, real funding timestamps and a spread-based slippage term?
3. Do signals discovered on Binance or Bybit SOL perpetuals keep their sign and roughly half their size on a later, untouched period, and on Kalshi's own tape? This is the local version of the McLean-Pontiff test and the only clean out-of-sample evidence available.
4. Does PBO computed on a search predict realized forward decay across many searches? Gort et al. could not show this convincingly.
5. Do the Falck et al. proxies (neighbourhood sensitivity, outlier sensitivity, expression complexity) predict which mined crypto signals decay? This matters most for evolved or machine-generated features.
6. Walk-forward against purged combinatorial CV for intraday labels: how much does unpurged leakage inflate accuracy at 5 to 60 minute label horizons?
7. How long must a paper-traded strategy run on Kalshi before the probabilistic Sharpe ratio can distinguish its haircut backtest Sharpe from zero, given the skew and kurtosis of its returns?
8. What fill rate and adverse selection do small passive orders experience on Kalshi relative to the risk-averse queue model, and at what size does the no-impact assumption fail?
9. Does a hierarchical shrinkage across BTC, ETH and SOL and across venues give better forward estimates of edge than per-instrument backtests?

## Reading order

1. [Bailey, Borwein, Lopez de Prado and Zhu 2014](notes/bailey-2014-pseudo-mathematics-financial-charlatanism.md): the problem stated plainly, with the trial budget.
2. [Arnott, Harvey and Markowitz 2019](notes/arnott-2019-backtesting-protocol-machine-learning.md): the process checklist.
3. [Bailey and Lopez de Prado 2014](notes/bailey-2014-deflated-sharpe-ratio.md) and [Harvey and Liu 2015](notes/harvey-2015-backtesting.md): the two standard Sharpe corrections.
4. [Bailey et al. 2015](notes/bailey-2015-probability-backtest-overfitting.md): PBO and CSCV.
5. [White 2000](notes/white-2000-reality-check-data-snooping.md) then [Hansen 2005](notes/hansen-2005-test-superior-predictive-ability.md): bootstrap tests over a rule universe.
6. [Deng 2025](notes/deng-2025-autoquant-execution-constrained-crypto-perps.md), [Gort et al. 2022](notes/gort-2022-deep-rl-crypto-backtest-overfitting.md), [Mroziewicz and Slepaczuk 2026](notes/mroziewicz-2026-walk-forward-window-optimization-bitcoin.md): the crypto applications, read critically.
7. [skfolio documentation](notes/skfolio-2026-combinatorial-purged-cross-validation.md) and [hftbacktest documentation](notes/hftbacktest-2026-order-fill-queue-models.md): implementation detail for purged CV and fills.
8. [McLean and Pontiff 2016](notes/mclean-2016-academic-research-destroy-predictability.md), [Falck, Rej and Thesmar 2021](notes/falck-2021-why-how-systematic-strategies-decay.md), [Chen, Lopez-Lira and Zimmermann 2022](notes/chen-2022-peer-reviewed-research-predict-returns.md), [Jensen, Kelly and Pedersen 2021](notes/jensen-2021-replication-crisis-finance.md): decay, and the debate over how much of it is overfitting.
9. [Bailey and Lopez de Prado 2012](notes/bailey-2012-sharpe-ratio-efficient-frontier.md), [Lo 2002](notes/lo-2002-statistics-sharpe-ratios.md), [Bailey and Lopez de Prado stop-outs](notes/bailey-2014-stop-outs-serial-correlation-triple-penance.md): live monitoring.
10. [Harvey, Liu and Zhu 2014](notes/harvey-2014-cross-section-expected-returns.md): background for the t-ratio hurdle.
