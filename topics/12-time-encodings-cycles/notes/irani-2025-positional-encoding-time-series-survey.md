---
title: "Positional Encoding in Transformer-Based Time Series Models: A Survey"
authors: "Irani, Habib; Metsis, Vangelis"
year: 2025
venue: "arXiv preprint arXiv:2502.12370 (v3, 5 May 2026)"
url: "https://arxiv.org/pdf/2502.12370"
pdf: "sources/12-time-encodings-cycles/irani-2025-positional-encoding-time-series-survey.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "n/a"
tags: "positional-encoding, transformers, time-series-classification, survey, benchmark"
---

## Key insight
For Transformer models on time series, some form of positional encoding is necessary, and the choice among encodings matters less than having one. More elaborate relative and hybrid encodings gain a few points of accuracy over the fixed sinusoidal scheme at extra compute cost, with the size of the gain depending on sequence length and signal type. The evidence is for classification only.

## Method
A survey plus a benchmark. Encodings are grouped as fixed (sinusoidal), learnable, relative, and hybrid. The methods named in the text include sinusoidal, learnable, RPE, tAPE, RoPE, eRPE, TUPE, ConvSPE, SPE and T-PE (temporal positional encoding), plus a no-encoding baseline. Each is trained inside two encoder architectures, a patch-free time series Transformer and PatchTST, with shared hyperparameters, and scored by classification accuracy with 95% confidence intervals over repeated runs. Average ranks across datasets summarize the comparison.

For reference, the fixed sinusoidal scheme being benchmarked is the standard one: as described in the Time2Vec paper, position j adds `sin(j / 10000^(k/d))` to embedding dimension k when k is even and `sin(j / 10000^(k/d) + pi/2)` when k is odd, with d the embedding size.

## Data and sample
Public classification datasets from biomedical signals (EEG, EMG, sleep), sensors, activity recognition, audio and others. The paper is internally inconsistent on counts: the introduction says eight methods on eleven datasets, the conclusion says ten methods and fifteen datasets, and one table caption averages over ten datasets. The exact count is not confirmed. No financial forecasting dataset was identified in the results read.

## Reported results
- SPE (stochastic positional encoding) has the best average rank on both architectures; TUPE is next (rank about 1.9 to 2.3), then T-PE (about 2.4 to 2.6).
- The conclusion states 5 to 12% accuracy improvement over the no-encoding baseline.
- Without positional encoding, accuracy drops 3 to 17% and confidence intervals are two to three times wider.
- Gains from advanced encodings are larger on long sequences; on very short sequences the gap to no encoding is about 5.5 to 5.7%.
- The authors list as a limitation that encoder-only classification does not generalize to forecasting.

## Signal construction
Not a signal. Guidance for a sequence model over a window of bars:
1. Never run self-attention over bars without positional information.
2. Position in window (bar index) and clock time (time of day, time of week) are different inputs. Supply both: a positional encoding for order, and cyclical clock features concatenated to each bar's feature vector.
3. Start with fixed sinusoidal or learnable absolute encodings; treat relative or stochastic variants as a later, low-priority experiment.

## Relevance to SOL perpetuals at minutes to hours
Indirect. It confirms an architecture-level requirement and gives no evidence about return prediction. Look-back windows for a minutes-to-hours bot are short (tens to a few hundred bars), the regime in which the paper finds the smallest differences between encodings. Effort is better spent on the clock features and on the validation protocol than on the choice of positional encoding.

## Caveats
Preprint with inconsistent descriptions of its own experimental scope. Classification accuracy on physiological and sensor data says little about noisy financial forecasting. No comparison with non-Transformer baselines, which the Zeng et al. results suggest is the more important comparison.
