---
title: "Multi-Horizon Forecasting for Limit Order Books: Novel Deep Learning Approaches and Hardware Acceleration using Intelligent Processing Units"
authors: "Zhang, Zihao; Zohren, Stefan"
year: 2021
venue: "arXiv:2105.10430v2 (journal publication not confirmed in this session)"
url: "https://arxiv.org/abs/2105.10430"
pdf: "sources/22-deep-learning-lob/zhang-2021-multi-horizon-forecasting-lob.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "seconds"
tags: "multi-horizon, seq2seq, attention, encoder-decoder, deeplob, transfer-learning, lse, hardware"
---

## Key insight
Replacing DeepLOB's single output with an encoder-decoder that emits a path of forecasts (one per horizon) matches the single-horizon model at short horizons and beats it at the longest one. One network then serves all horizons. The attention weights show the model leaning almost entirely on the most recent book states, which the authors read as the current book already holding most of the available information.

## Method
Encoder: the DeepLOB convolution plus Inception block. Decoder: either Seq2Seq (context is the encoder's last hidden state) or Luong attention (context is a weighted sum of all encoder states), each with one 64-unit LSTM, rolled forward so that the prediction for one horizon feeds the next. Targets are the usual down, stationary, up classes at each horizon; loss is categorical cross-entropy. Baselines: linear model, MLP, LSTM, CNN-I, DeepLOB. The paper also times training on Graphcore IPUs against a single NVIDIA RTX 2080.

## Data and sample
FI-2010 with horizons k = 10, 20, 30, 50, 100 ticks. LSE data for Lloyds, Barclays, Tesco, BT and Vodafone for all of 2018, 08:30 to 16:00, more than 169 million samples; six months train, three validate, three test (more than 46 million test samples), horizons k = 20, 50, 100. Transfer test on 20 further LSE stocks not used in training.

## Reported results
- FI-2010: the two new models are close to DeepLOB at k = 10 to 50 and better at k = 100, with DeepLOB-Attention best.
- LSE at k = 20, F1: linear 42.38%, MLP 46.89%, LSTM 66.68%, CNN-I 64.64%, DeepLOB 68.40%, DeepLOB-Seq2Seq 67.76%, DeepLOB-Attention 68.09%. The multi-horizon models do better at the longer horizons.
- Transfer to 20 unseen stocks: all three deep models keep strong results, attention slightly ahead.
- Attention weights are largest for the most recent observations; older states are close to inactive.
- An encoder-decoder trains on the IPU in about 15% of the GPU wall-clock time.

## Signal construction
Same input as DeepLOB (last 100 snapshots of the 10-level book). Output is a vector of class probabilities at several horizons. A bot can read the term structure: agreement across horizons as a confidence filter, or the longest horizon alone as the directional feature. Training one multi-output model is cheaper than several single-horizon models.

## Relevance to SOL perpetuals at minutes to hours
The multi-horizon design is the part worth copying, because the horizon that matters for us is longer than any single LOB paper tests. Define horizons in clock time (for example 10 seconds, 1 minute, 5 minutes) on a lead-venue SOL book and check where the forecast stops beating a no-change baseline. The attention finding suggests long look-back windows add little at this resolution, which conflicts with Sirignano and Cont's path-dependence result and should be tested directly.

## Caveats
No trading simulation and no costs. Differences between the deep models on LSE are about one F1 point or less. Horizons are in book updates, so the clock-time horizon varies by stock and hour. Same author group and data source as DeepLOB; not an independent replication. The IPU comparison is against one consumer GPU.
