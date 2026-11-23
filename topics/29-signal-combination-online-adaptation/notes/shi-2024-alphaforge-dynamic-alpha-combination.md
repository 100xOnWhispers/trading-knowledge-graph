---
title: "AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors"
authors: "Shi, Hao; Song, Weili; Zhang, Xinting; Shi, Jiahe; Luo, Cuicui; Ao, Xiang; Arian, Hamid; Seco, Luis"
year: 2024
venue: "arXiv preprint 2406.18394 (v5, December 2024; carries an AAAI 2025 copyright line)"
url: "https://arxiv.org/pdf/2406.18394"
pdf: "sources/29-signal-combination-online-adaptation/shi-2024-alphaforge-dynamic-alpha-combination.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "daily"
tags: "dynamic-combination, factor-timing, alpha-mining, rolling-reselection, learned-combiner, fixed-vs-dynamic-weights"
---

## Key insight
One of the few papers with an explicit ablation of fixed versus re-estimated combination weights for machine-mined signals. After mining a library of formulaic factors with a generative neural network, the authors re-rank the factors every day on recent performance, keep the best few, and refit a linear combiner on recent data. Replacing a fixed-weight combination by this dynamic one raised the information coefficient from 2.43% to 4.40% on CSI 300 and from 2.05% to 2.84% on CSI 500. Neither an equal-weight combination nor realistic costs are part of the comparison, so it is evidence for adaptivity over static fitted weights, not over 1/N.

## Method
Stage 1 (mining, in scope of topic 25): a generative-predictive network proposes formula trees; factors enter a "factor zoo" only if they pass thresholds on information coefficient (IC), IC information ratio and low correlation with existing members. The zoo is then frozen.
Stage 2 (combination, the part relevant here): at each date t, using the preceding n days, recompute each factor's recent IC, ICIR and rank IC; select the top N factors; fit a linear model of returns on those factors with the latest data; use it to produce that day's composite "Mega-Alpha". The motivation given is factor momentum: factors that worked recently tend to keep working. The ablation "Static" uses the same mined factors with fixed weights set as in the reinforcement-learning baseline (AlphaGen, Yu et al. 2023).

## Data and sample
Chinese A-shares, CSI 300 and CSI 500 constituents, daily, from Qlib. Tests cover 2018 to 2022 with annual retraining (first split: train 2010 to 2016, validate 2017, test 2018). Baselines: gradient-boosted trees, a multilayer perceptron, genetic programming, deep symbolic optimization and AlphaGen. The simulated strategy holds the 50 highest-scored stocks equally weighted and changes at most 5 names per day "to avoid excessive trading costs"; an explicit fee model was not found in the main text.

## Reported results
IC and rank IC in percent (standard deviation across runs in brackets), CSI 300 then CSI 500:
- Full model (dynamic): 4.40 (0.56) and 5.89 (0.69); 2.84 (0.58) and 5.57 (0.58).
- Static ablation: 2.43 (0.57) and 3.67 (0.46); 2.05 (0.29) and 4.48 (0.46).
- AlphaGen: 2.09 and 2.72; 1.91 and 4.03. Genetic programming: 1.29 and 2.72; 0.37 and 2.34. LightGBM: 0.84 and 1.85; 1.75 and 3.81.
- Performance is non-monotonic in pool size and peaks at about 10 factors in use.
- Simulated trading 2018 to 2022: highest final net value among compared methods (figure only). A live account of 3 million RMB is reported to have earned 21.68% excess return over CSI 500 after about nine months.

## Signal construction
Rolling re-selection combiner: keep a fixed library of signals; each period compute every signal's trailing rank correlation with forward returns and its stability (mean over standard deviation); keep the top N by that score, subject to the sign being as designed; refit a ridge or ordinary least squares combination on the same trailing window; trade the fitted composite. Parameters: look-back n, N (about 10 in the paper), refit frequency.

## Relevance to SOL perpetuals at minutes to hours
The combination stage is asset-agnostic and maps onto intraday bars with trailing time-series IC in place of cross-sectional IC. The gain it reports is conditional on factor momentum existing in the signal library; whether intraday crypto signals show performance persistence over the chosen look-back is the thing to test first. With one instrument there is no cross-section, so IC estimates are far noisier per day than in a 300-stock universe.

## Caveats
Preprint; the live-account figure is a single short unaudited anecdote. No equal-weight or inverse-variance combiner benchmark. Costs appear only as a turnover cap. Chinese equities over 2018 to 2022 only. Daily refitting on a short window is itself a high-variance procedure, and the look-back and N were presumably tuned; the supplementary material with hyperparameters was not read.
