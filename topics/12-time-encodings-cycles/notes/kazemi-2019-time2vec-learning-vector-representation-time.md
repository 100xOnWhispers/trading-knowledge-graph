---
title: "Time2Vec: Learning a Vector Representation of Time"
authors: "Kazemi, Seyed Mehran; Goel, Rishab; Eghbali, Sepehr; Ramanan, Janahan; Sahota, Jaspreet; Thakur, Sanjay; Wu, Stella; Smyth, Cathal; Poupart, Pascal; Brubaker, Marcus"
year: 2019
venue: "arXiv preprint arXiv:1907.05321"
url: "https://arxiv.org/pdf/1907.05321"
pdf: "sources/12-time-encodings-cycles/kazemi-2019-time2vec-learning-vector-representation-time.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "n/a"
tags: "time2vec, time-embedding, learned-frequencies, lstm, machine-learning"
---

## Key insight
Time can be fed to a neural network as a small vector made of one linear term and several sine terms whose frequencies and phases are learned. On the datasets tested, replacing a raw time input with this vector improved or matched an LSTM in every case, and learned frequencies beat fixed ones. It is the reference design for learnable time embeddings.

## Method
For a scalar time `tau`, Time2Vec is a vector of size k+1:

`t2v(tau)[0] = w_0*tau + phi_0`
`t2v(tau)[i] = sin(w_i*tau + phi_i)`, i = 1..k

with all `w_i` and `phi_i` trained by backpropagation. A sine with `w = 2*pi/7` repeats every 7 units, so weekly patterns can be learned from a day counter without feature engineering. The linear term carries non-periodic drift. The authors prove the representation is invariant to rescaling time. It is concatenated to the other inputs (LSTM+Time2Vec) or substituted for time inside time-aware LSTM variants.

Ablations: periodic versus non-periodic activations, and fixed versus learned frequencies. The fixed alternatives are equally spaced Fourier frequencies and the exponentially decaying frequencies of the Transformer positional encoding.

## Data and sample
A synthetic set (integers 1 to 365, label is "multiple of 7", first 75% for training), Event-MNIST, N_TIDIGITS18 audio spikes, Stack Overflow badges (about 6K users, 480K events), Last.FM (about 1K users, 819K events) and CiteULike (about 36K events). No financial data.

## Reported results
- LSTM+Time2Vec improves on LSTM with raw time in most cases and never does worse, by the authors' description of their Figure 1.
- On the synthetic task the model learns a 7-day period and classifies the held-out last quarter of the year perfectly.
- Sine outperforms sigmoid, tanh, ReLU, mod and triangle activations on Event-MNIST; non-periodic activations fail on the synthetic task.
- Learning frequencies and phases beats both fixed schemes on Event-MNIST (their Figure 5b). Results are shown as curves; no single headline number is given in the text read.

## Signal construction
Not a signal. It is an input layer:
1. Choose time scalars: seconds since midnight UTC, seconds since Monday 00:00 UTC, seconds to next funding.
2. Pass each through `t2v` with k of roughly 4 to 16.
3. Concatenate with market features before the first layer of the network or RL policy.
A cautious variant initializes the `w_i` at the known periods (24 hours, 8 hours, 7 days) and lets training adjust them, or freezes them.

## Relevance to SOL perpetuals at minutes to hours
The idea transfers; the evidence does not. The benefit shown comes from tasks where the model must discover an unknown period. In crypto the candidate periods are known in advance, and returns have a far lower signal-to-noise ratio than badge or music sequences. Learned frequencies add free parameters that can latch onto spurious periodicities in a short training sample. The test worth running is fixed harmonics versus Time2Vec on walk-forward data, with the fixed version as the baseline to beat.

## Caveats
Preprint. No financial or noisy forecasting benchmark. Comparisons are against a raw time scalar, not against well-built fixed cyclical features, except in one ablation on Event-MNIST. A raw unbounded time input (the linear term) can make a model extrapolate badly when the test period lies outside the training range.
