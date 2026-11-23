---
title: "LOB-Bench: Benchmarking Generative AI for Finance - an Application to Limit Order Book Data"
authors: "Nagy, Peer; Frey, Sascha; Li, Kang; Sarkar, Bidipta; Vyetrenko, Svitlana; Zohren, Stefan; Calinescu, Anisoara; Foerster, Jakob"
year: 2025
venue: "ICML 2025 (PMLR 267); arXiv:2502.09172"
url: "https://arxiv.org/abs/2502.09172"
pdf: "sources/31-rl-evolutionary-second-pass/nagy-2025-lob-bench-generative-order-book-benchmark.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "tick"
tags: "generative-model, limit-order-book, benchmark, simulator-realism, price-impact, error-accumulation"
---

## Key insight
Generative order-book models can now be scored on realism with a common yardstick, and the scores are sobering. Even the best model tested is told apart from real data by a simple classifier most of the time, and every model's generated data drifts further from reality the longer it is rolled forward. A learned simulator is therefore usable for short counterfactuals at best, and its fidelity has to be measured before any policy is trained in it.

## Method
- Input: generated and real message-by-order data in LOBSTER format.
- Distribution scores: for each statistic (spread, book volumes, order imbalance, message inter-arrival times, distance of new orders and cancellations from the mid-price, and more) compare the histogram from generated data with real data using the L1 distance scaled to [0, 1] and the Wasserstein-1 distance. Conditional versions compute the same statistics conditioned on another variable or on the number of steps since generation began, which measures error accumulation.
- Adversarial score: a small 1-D convolutional classifier is trained to distinguish real from generated sequences; its ROC score is the metric (0.5 would be indistinguishable).
- Impact metrics: price response functions by event type (market orders, limit orders, cancellations, split by whether they move the mid-price), compared between real and generated data.
- Downstream test: train a mid-price trend classifier with generated data added and check the F1 score.
- Models compared: a parametric arrival-rate model after Cont et al. (2010), a conditional GAN after Coletta et al. (2022), an autoregressive state-space model (LOBS5, 35 million parameters) and two RWKV sequence models.

## Data and sample
LOBSTER data for Alphabet (GOOG) and Intel (INTC). LOBS5 trained on all of 2022 and evaluated on a sub-sample of January 2023. The GAN was trained on three days of January 2019 and tested on the next three because of its compute cost.

## Reported results
- LOBS5 has the lowest aggregate L1 and Wasserstein scores; the GAN beats the parametric baseline on Wasserstein but not on L1.
- The classifier separates LOBS5 output from real GOOG data with ROC score 0.83; for the parametric baseline the score is about 1.
- Distribution errors rise with rollout length for all models ("model derailment"), fastest for the RWKV models.
- Impact curves: average L1 distance to real response functions 2.45 for LOBS5 and 126 for RWKV-6; the parametric baseline "cannot faithfully reproduce impact curves".
- Adding GAN-generated data to training reduced the trend classifier's F1 score.

## Signal construction
Not a signal. It supplies an acceptance test for any synthetic-data generator or simulator the project might adopt: stylized-fact distances, a discriminator score, response-function match and drift with horizon.

## Relevance to SOL perpetuals at minutes to hours
Model-based RL and synthetic augmentation are the proposed cures for having one history. This benchmark shows the cure is not yet reliable at message level for liquid US equities, where data are cleanest. For SOL perps the same tests can be run on bar-level or book-snapshot generators with crypto data; a generator that fails them should not be used to train or rank policies. Rollout drift matters most for the bot's horizon, because minutes to hours means thousands of generated events.

## Caveats
Two US stocks, one test month, message-level data of a kind most crypto venues do not publish. The benchmark authors also wrote the best-scoring model. Passing distributional tests does not establish that a policy's profit in the simulator transfers to the market; that link is not tested here.
