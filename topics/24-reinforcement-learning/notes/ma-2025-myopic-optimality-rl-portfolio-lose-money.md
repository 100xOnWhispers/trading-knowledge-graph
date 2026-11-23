---
title: "Myopic Optimality: why reinforcement learning portfolio management strategies lose money"
authors: "Ma, Yuming"
year: 2025
venue: "arXiv:2509.12764"
url: "https://arxiv.org/pdf/2509.12764"
pdf: "sources/24-reinforcement-learning/ma-2025-myopic-optimality-rl-portfolio-lose-money.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "24-reinforcement-learning"
asset_class: "multi"
horizon: "n/a"
tags: "myopic-optimization, critique, action-independent-dynamics, policy-gradient-variance, look-ahead-leakage, phantom-profit, transaction-costs, theory"
---

## Key insight
A theoretical argument that RL is the wrong tool when the trader's actions do not change market dynamics. In such "action-independent market" (AIM) settings, solving a one-period convex problem at each decision time (myopic optimization, MO) is dynamically sufficient: the multi-period credit assignment that RL performs buys nothing, while policy-gradient estimation adds a variance floor that MO does not have. RL earns a genuine premium only where control affects dynamics (impact, state-dependent fills, queue position). The paper also formalizes "phantom profit": backtest gains created when a trained policy is not strictly adapted to information available at decision time.

## Method
Continuous-time stochastic analysis. Market state follows a Stratonovich SDE; wealth is marked to market under a prudent convention that includes spread, transient impact, funding and block-liquidation discounts. Policy gradients are written with Malliavin calculus (Clark-Ocone and Bismut-Elworthy-Li weights), giving a "risk shadow price" under which the Euler-Lagrange/KKT conditions of the one-period problem coincide with HJB stationarity. From this the paper derives convergence statements (geometric for MO; a non-vanishing variance floor for policy-gradient RL), a decomposition of look-ahead bias, and a definition of the control-affects-dynamics (CAD) premium. Taker and maker modes are both treated.

## Data and sample
None. 43 pages of definitions, propositions and proofs.

## Reported results
Claims read in the paper (theoretical unless noted):
- Under AIM dynamics with matched rebalancing clocks, cost schedules and risk budgets, adapted MO dominates effort-matched RL on mean P&L, variance, loss-side CVaR and probability of non-negative P&L.
- Phantom profit channels: solver-induced look-ahead in policy-gradient training, cross-bar leakage, and latency peek-through.
- The CAD premium is asserted to be "0-1 bps per decision day" in most liquid AIM-like environments and low single-digit bps per day in rare strongly CAD-dominated niches. No data or estimation supporting these figures appears in the paper.
- The introduction states that under out-of-sample tests with implementable frictions, reported RL gains "tend to vanish", citing surveys.
- Stated limits: the sufficiency claim fails when trading changes the law of the state; convergence results need smoothness and curvature; jump-heavy or regime-switching periods strain the approximations.

## Signal construction
Not a signal. It prescribes an architecture: forecast expected return and risk, then at each decision time solve a single-period problem (maximize expected net return minus risk penalty minus cost of changing position), which yields a no-trade band around the current position. Reserve RL for the components where the bot's own actions change future state. It also names the leakage channels to audit in any trained policy: look-ahead introduced by the training procedure, information crossing bar boundaries, and fills assumed at prices observed before latency.

## Relevance to SOL perpetuals at minutes to hours
The directional layer of this bot is close to the AIM case (signals from large venues, small size), so the paper's conclusion is that a supervised forecast plus a cost-aware one-step position rule should match or beat an end-to-end RL policy there, with less variance and far easier auditing. The exception it concedes is exactly the Kalshi execution layer, where the bot's orders may be a meaningful share of a thin book. One qualification the paper does not discuss: with a predictable signal that decays over several bars and proportional costs, the one-period problem needs a multi-period forecast as input; "myopic" refers to the optimization, not to the horizon of the alpha model.

## Caveats
Single-author preprint, not peer-reviewed, with no empirical section; the title's empirical claim is argued from theory and from cited literature. The quantitative CAD-premium figures are unsupported assertions. The PDF's text layer has OCR-style errors, so formulas could not be transcribed reliably and none are reproduced here. The assumptions (diffusive dynamics, convexity) are strong for crypto perps with jumps and liquidations. Direct-reinforcement methods that take gradients through a known reward (Moody and Saffell; Jiang et al.) are closer to MO than to the policy-gradient RL the paper criticizes, and are not separately analyzed.
