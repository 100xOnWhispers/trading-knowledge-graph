---
title: "A Survey on Concept Drift Adaptation"
authors: "Gama, Joao; Zliobaite, Indre; Bifet, Albert; Pechenizkiy, Mykola; Bouchachia, Abdelhamid"
year: 2014
venue: "ACM Computing Surveys (accepted author version read)"
url: "https://www.win.tue.nl/~mpechen/publications/pubs/Gama_ACMCS_AdaptationCD_accepted.pdf"
pdf: "sources/29-signal-combination-online-adaptation/gama-2014-survey-concept-drift-adaptation.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "concept-drift, cusum, page-hinkley, drift-detection, statistical-process-control, prequential-evaluation, forgetting"
---

## Key insight
The standard taxonomy of how a deployed predictive model should cope when the relation between inputs and target changes. It separates four design choices (memory, change detection, learning, loss estimation), distinguishes "blind" adaptation at a fixed forgetting rate from "informed" adaptation triggered by a detector, and gives the working formulas of the classic detectors. Its framing translates directly into rules for when to retrain, down-weight or switch off a live trading signal.

## Method
Survey. Drift types: sudden, incremental, gradual, reoccurring; a one-off outlier is not drift and should not trigger adaptation. Requirements: detect quickly, be robust to noise, run in bounded time and memory.
Detectors, applied to a stream of model errors or losses x_t:
- CUSUM (Page 1954): g_t = max(0, g_{t−1} + (x_t − δ)), g_0 = 0; alarm when g_t > λ, then reset. δ is the tolerated change, λ the threshold. Memoryless; lower δ detects faster with more false alarms.
- Page-Hinkley: m_T = Σ_{t≤T} (x_t − x̄_T − δ), M_T = min_t m_t; alarm when m_T − M_T > λ.
- Statistical process control (the drift detection method of Gama et al. 2004): track error rate p_i and s_i = sqrt(p_i(1 − p_i)/i) and the minimum of p + s; "warning" when p_i + s_i ≥ p_min + 2 s_min, "out of control" when p_i + s_i ≥ p_min + 3 s_min. The warning state starts buffering recent data so a replacement model can be trained from the suspected change point.
- EWMA charts: Z_t = (1 − λ) Z_{t−1} + λ e_t; alarm when Z_t exceeds the baseline by L standard deviations.
- Two-window methods such as ADWIN: compare a reference window with a recent window.
Adaptation: blind (fixed sliding window, example weighting with a fading factor α in (0, 1) applied to the stored statistics before each update, periodic retraining) versus informed (retrain, replace or re-weight on alarm); single model versus ensembles whose member weights follow recent accuracy (for example Dynamic Weighted Majority, which multiplies an expert's weight by β < 1 on a mistake, deletes experts below a threshold and creates new ones); handling of reoccurring concepts by storing old models.
Evaluation: holdout on later data, or prequential (test on each example, then train on it) with a sliding window or fading factor so that recent performance is not averaged away.

## Data and sample
None of its own beyond illustrative stream-mining experiments on synthetic data in an appendix. Applications discussed are monitoring, planning, personal assistance and ubiquitous computing; finance is not a focus.

## Reported results
Qualitative conclusions read in the survey:
- Blind strategies forget at a constant speed whether or not change is happening, so they react slowly to sudden drift and waste data in stable periods.
- Detector parameters trade detection delay against false alarms; no setting avoids both.
- Complexity: sequential tests such as CUSUM and Page-Hinkley need constant time and memory per observation; two-window methods need memory between logarithmic and linear in the window.
- Running the Page-Hinkley test on the ratio of a short-memory to a long-memory error estimate is reported (Gama et al. 2013) to detect drift somewhat faster with fading factors than with sliding windows; the choice of fading factor or window size is described as critical.
- Supervised adaptation assumes labels arrive promptly; delayed or missing feedback is flagged as a main open problem.

## Signal construction
Per live signal, monitor a loss stream: for example the negative of the signal's per-trade net return in units of its expected volatility, or a hit/miss indicator. Run Page-Hinkley or CUSUM with δ set to the degradation that can be tolerated and λ chosen from the acceptable false-alarm rate on historical in-control data. Map states to actions: warning means halve the weight and start a shadow refit on data since the warning; out-of-control means set the weight to zero and promote the refit only after it passes its own in-control period.

## Relevance to SOL perpetuals at minutes to hours
Directly applicable as the monitoring layer that topic 26 notes is missing. Two properties of trading data need care. Labels are delayed by the holding period, so detection lags by at least one horizon. Losses are heavy-tailed and autocorrelated, so thresholds derived for Bernoulli errors (the 2-sigma and 3-sigma rule) will raise false alarms; calibrate λ by simulation on the signal's own in-control history, and prefer monitoring a bounded statistic such as hit rate or rank correlation.

## Caveats
Classification-centred and not specific to finance. With signal-to-noise as low as in intraday returns, any detector with a tolerable false-alarm rate will need many trades to confirm a real loss of edge; the survey does not quantify detection delay in that regime. The year follows the usual citation; the copy read is the accepted manuscript.
