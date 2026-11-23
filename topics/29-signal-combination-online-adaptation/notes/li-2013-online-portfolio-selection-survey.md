---
title: "Online Portfolio Selection: A Survey"
authors: "Li, Bin; Hoi, Steven C. H."
year: 2013
venue: "arXiv preprint 1212.2129 (v2, May 2013); prepared for ACM Computing Surveys"
url: "https://arxiv.org/pdf/1212.2129"
pdf: "sources/29-signal-combination-online-adaptation/li-2013-online-portfolio-selection-survey.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "daily"
tags: "online-portfolio-selection, universal-portfolio, exponential-gradient, meta-learning, constant-rebalanced, transaction-costs"
---

## Key insight
Online portfolio selection treats allocation as a sequential game with no statistical model: each period choose weights on the simplex, observe price relatives, and aim to grow log wealth nearly as fast as the best fixed-weight rebalanced portfolio chosen in hindsight. The survey organizes the field into follow-the-winner, follow-the-loser, pattern-matching and meta-learning algorithms. For this repository its most useful parts are the meta-learning family, which allocates among whole strategies, and its frank statement that transaction costs and liquidity are largely unsolved in this literature.

## Method
Setting: m assets, price-relative vector x_t, portfolio b_t on the simplex, wealth S_n = Π b_t'x_t. Benchmarks: buy-and-hold, best single stock, uniform constant rebalanced portfolio (UCRP, the 1/N analogue), and the best constant rebalanced portfolio in hindsight (BCRP). Families:
- Follow-the-winner: Cover's universal portfolio (a wealth-weighted average over all constant rebalanced portfolios), exponential gradient (b_{t+1,i} ∝ b_{t,i} exp(η x_{t,i} / b_t'x_t)), follow-the-leader, follow-the-regularized-leader including online Newton step, and aggregating algorithms. Singer's switching portfolios add a fixed-share step, b_{t+1} = (1 − γ − γ/(m−1)) b_t + γ/(m−1), to track a changing best asset.
- Follow-the-loser: Anticor, passive-aggressive mean reversion, confidence-weighted mean reversion, online moving-average reversion, robust median reversion.
- Pattern matching: find past windows similar to the present and optimize on what followed.
- Meta-learning: treat each base strategy as an expert and combine their portfolios by the aggregating algorithm (weights multiplied by β^loss), by buy-and-hold pooling of expert wealth ("fast universalization"), by online gradient or Newton updates over experts, or by "follow the leading history", which keeps experts started at different times so the mix can adapt to changing environments.
- Transaction costs: a proportional-cost model is defined, with a net-wealth factor solved per rebalance.

## Data and sample
A survey; no new experiments. The algorithms it reviews are typically back-tested on daily or lower-frequency stock datasets (for example NYSE data).

## Reported results
Statements read in the survey:
- The heuristic mean-reversion method Anticor, which has no regret guarantee, "empirically outperforms all other strategies at the time"; later follow-the-loser methods are described as outperforming on most datasets. Uniform rebalancing itself is shown to be an implicit mean-reversion bet.
- Switching portfolios outperformed universal portfolios, exponential gradient and BCRP "in most cases" on Cover's two-stock pairs.
- Follow-the-leading-history with online Newton step "can significantly outperform" plain online Newton step.
- Open problems listed by the authors: incorporating risk; shorting and margin (one cited NYSE study found no gain from short selling but a large gain from leverage); extending algorithms to transaction costs; and market liquidity, which no algorithm models and which back-tests on liquid stocks do not settle.

## Signal construction
Combiner template. Let each strategy k output a position p_k,t in [−1, 1] and realise a net return r_k,t. Keep weights w_k; after each period set w_k ← w_k exp(η r_k,t) (exponentiated gradient on strategy returns), mix with a small uniform share γ so no strategy's weight reaches zero, renormalise, and trade Σ w_k p_k,t. η and γ are the only parameters; γ sets how fast a revived strategy can regain weight.

## Relevance to SOL perpetuals at minutes to hours
The meta-learning view (strategies as experts, UCRP as the benchmark) is the right frame for a single-instrument bot with several signals. The asset-level results do not transfer: they are long-only, multi-asset, daily, and their best performers exploit daily cross-sectional reversal in stock datasets. Fixed-share and leading-history variants are the pieces designed for non-stationarity.

## Caveats
The surveyed back-tests are mostly gross of costs on a few historical datasets that the whole field reuses, which invites dataset-level overfitting. Regret guarantees are relative to the best fixed mix, which may itself be unprofitable. The arXiv version was read; the journal version was not confirmed in this session.
