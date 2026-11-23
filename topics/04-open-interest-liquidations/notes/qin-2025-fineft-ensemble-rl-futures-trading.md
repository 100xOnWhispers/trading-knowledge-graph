---
title: "FineFT: Efficient and Risk-Aware Ensemble Reinforcement Learning for Futures Trading"
authors: "Qin, Molei; Cai, Xinyu; Li, Yewen; Xia, Haochong; Zong, Chuqiao; Sun, Shuo; Wang, Xinrun; An, Bo"
year: 2025
venue: "KDD '26 (read as arXiv 2512.23773v1, December 2025)"
url: "https://arxiv.org/pdf/2512.23773"
pdf: "sources/04-open-interest-liquidations/qin-2025-fineft-ensemble-rl-futures-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, ensemble, leverage, liquidation-risk, out-of-distribution, regime-detection"
---

## Key insight
Reinforcement-learning agents trained for spot markets break down on leveraged crypto futures for two reasons: leverage amplifies reward noise so training does not converge, and agents have no sense of when market conditions are outside what they were trained on, which exposes them to liquidation in abrupt regime shifts. FineFT addresses the second problem with an explicit out-of-distribution detector that hands control to a conservative policy when recent market states look unfamiliar. This is the closest reinforcement-learning work found to the problem of surviving deleveraging events with a leveraged directional bot.

## Method
Three stages. Stage I trains an ensemble of deep Q-networks, pre-trained on demonstrations, where each transition updates only the learner with the smallest temporal-difference error and its neighbors, so learners specialize in different market dynamics. Stage II back-tests each learner on labelled market dynamics, keeps the profitable ones, and trains a variational autoencoder (VAE) on the market-state representations of each dynamic to mark each learner's capability boundary. Stage III scores a rolling window of recent states by VAE loss, smoothed with an exponential moving average; if the best score is below a risk threshold the system switches to a conservative policy, otherwise it routes to the matching learner. The state is about 300 technical indicators built from trades and the limit order book plus the current position. Actions are target positions with a leverage choice from a finite pool. The environment models leverage, transaction costs, slippage and funding fees.

## Data and sample
Crypto futures for BNB, BTC, DOT and ETH against USDT at minute level, 1 January 2022 to 1 January 2024 (210,241 steps each). The first year is for training, the next six months for validation and the last six months for testing. Leverage is 5x and transaction cost 0.02%, which the authors say is aligned with Binance. An appendix reports additional tests on corn and ES futures, not read here.

## Reported results
- Against 12 baselines (policy-based, value-based, hierarchical, ensemble and distributional RL, plus two rule-based methods), FineFT has the lowest risk on all four datasets, the best risk-adjusted profit on three and the highest profit on two.
- The abstract states risk is reduced by more than 40% relative to the runner-up with superior profitability.
- Hierarchical RL baselines earn high profits but show large maximum drawdowns, which the authors attribute to lacking a capability boundary.
- Ablations show the VAE routing significantly reduces maximum drawdown.
- The paper illustrates a late-2022 shock in which a cluster in the one-dimensional state embedding jumps abruptly.

## Signal construction
Not an alpha signal. It is a risk-gating method: fit a density or reconstruction model (here a VAE) on the feature vectors seen in training, compute reconstruction loss on a rolling window of live states, and force the bot flat or to minimum size when the loss exceeds a threshold tuned on validation data. Update every bar.

## Relevance to SOL perpetuals at minutes to hours
The horizon and leverage match the bot's setting closely, and the gating idea applies to any model, not only RL. A cascade such as October 2025 is exactly an out-of-distribution state. Two things need re-testing: SOL is not in the sample, and the state vector contains no open interest, liquidation or funding features, so whether adding them improves either the policy or the detector is open. No evolutionary or genetic-algorithm work on leverage or liquidation signals was located for this topic.

## Caveats
Two-year sample with a single six-month test window per asset and no major cascade in the test period identified in the text read. Market orders are assumed to fill instantly. Many baselines and hyperparameters create selection risk. Results are from the authors' own simulator.
