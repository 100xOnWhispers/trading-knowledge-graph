---
title: "Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems"
authors: "Levine, Sergey; Kumar, Aviral; Tucker, George; Fu, Justin"
year: 2020
venue: "arXiv:2005.01643v3"
url: "https://arxiv.org/pdf/2005.01643"
pdf: "sources/24-reinforcement-learning/levine-2020-offline-rl-tutorial-review-open-problems.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "multi"
horizon: "n/a"
tags: "offline-rl, batch-rl, distributional-shift, off-policy-evaluation, importance-sampling, policy-constraints, behavior-cloning, model-based-rl"
---

## Key insight
Learning a policy from a fixed log of past data, with no further interaction, is a counterfactual inference problem: the learned policy must do something different from the data, so it is evaluated on state-action pairs the data cover poorly. This distributional shift, not optimization, is the central obstacle, and naive application of standard off-policy algorithms to a fixed dataset can fail badly. The tutorial organizes the remedies into importance sampling, policy constraints, uncertainty-aware value estimation and model-based methods. Every backtest-trained trading agent is an offline RL system and inherits these limits wherever its actions would have changed what happened next.

## Method
Tutorial and literature review, 43 pages. It formalizes offline RL (a dataset `D` collected by a behavior policy `pi_beta`; learn `pi` without new data), then covers: off-policy evaluation and policy gradients via importance sampling (plain, weighted, per-decision, marginalized); approximate dynamic programming and why Q-learning breaks on out-of-distribution actions; policy-constraint methods that keep `pi` close to `pi_beta`; uncertainty-based and conservative value methods; model-based offline RL; applications and open problems.

## Data and sample
No original experiments. Examples and cited applications come from robotics, healthcare, dialogue and recommender systems; finance is not a focus.

## Reported results
Statements read in the paper:
- If the dataset does not cover high-reward regions, no algorithm can find them; the tutorial assumes adequate coverage and treats distributional shift as the practical challenge.
- An illustration based on Ross et al. (2011): even with optimal action labels at every state in the data, a policy trained offline accumulates error that scales as `O(H^2)` in the horizon `H`, because a single mistake moves it into states outside the training distribution where it keeps erring.
- Importance-sampling estimators have variance that grows exponentially with horizon because per-step weights multiply. They are usable only when the learned policy deviates by a limited amount from the behavior policy. The maximum reliable improvement is bounded by the suboptimality of the behavior policy, the dimensionality of the state and action spaces, and the effective horizon.
- Dynamic-programming methods suffer from querying the value function at out-of-distribution actions; fixes fall into policy constraints and uncertainty estimation.
- Model-based offline methods "are not immune" to the same shift: the learned model is exploited where it is wrong.

## Signal construction
Not a signal. It gives a checklist for deciding how much a logged-data result can be trusted:
1. Which part of the state does the agent's action change? For a price taker, market prices are exogenous and only position, cash and (on a thin book) fills are action-dependent.
2. For the action-dependent part, is the candidate policy's behavior covered by the data? A policy that trades far more often or in far larger size than anything in the log is extrapolating.
3. Prefer policies constrained to stay near a known, already-evaluated behavior (for example a rule-based strategy with RL adjusting only its size or timing).

## Relevance to SOL perpetuals at minutes to hours
For the directional decision, the bot is close to the benign case: its small orders do not move Binance or Bybit prices, so replaying recorded prices under a different policy is a valid counterfactual and the offline problem reduces to ordinary overfitting. This is the assumption Jiang et al. and Nevmyvaka et al. exploit. For fills on Kalshi the benign case fails: whether a resting order would have filled, and what the book would have done after a crossing order, are true counterfactuals that the log cannot answer. The tutorial's guidance then applies: keep the execution policy close to behavior that has actually been run live, collect live data with deliberate small-scale exploration, and distrust backtested gains from execution behavior never tried.

## Caveats
A methods tutorial from 2020; the algorithms it surveys have been superseded in detail, though the problem statement stands. No financial experiments; the mapping to trading in this note is my reading, not the authors'. Market non-stationarity (the data-generating process itself changing) is a separate problem the tutorial does not address.
