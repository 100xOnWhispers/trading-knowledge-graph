---
title: "A Comparison of the Real-Time Performance of Business Cycle Dating Methods"
authors: "Chauvet, Marcelle; Piger, Jeremy"
year: 2005
venue: "Federal Reserve Bank of St. Louis Working Paper 2005-021A"
url: "https://files.stlouisfed.org/files/htdocs/wp/2005/2005-021.pdf"
pdf: "sources/01-macro-regime-detection/chauvet-2005-real-time-business-cycle-dating.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "multi"
horizon: "multi-day"
tags: "real-time, look-ahead, vintage-data, markov-switching, dynamic-factor, turning-points, confirmation-rule"
---

## Key insight
The cleanest demonstration of how to test a regime detector without look-ahead. The authors rebuild the data exactly as it existed at each past date, re-estimate the model at each date, and apply a fixed decision rule. A Markov-switching dynamic-factor model then identifies US recessions accurately with no false positives over about 27 years, but only after a confirmation delay, and it is much faster at calling the end of a recession than the start.

## Method
Two dating rules are compared. (1) A nonparametric algorithm based on Bry and Boschan (1971) that finds local peaks and troughs in each series and combines them. (2) A dynamic-factor Markov-switching (DFMS) model in which a common factor of four coincident indicators has a mean that switches between expansion and recession. The DFMS decision rule: a recession is declared when the recession probability moves from below to above 0.8 and stays above 0.8 for three consecutive months; the trough rule mirrors this with a 0.2 threshold. Parameters are re-estimated for each data vintage; model specification (lag orders) is held fixed.

## Data and sample
A newly assembled unrevised real-time data set of US nonfarm payroll employment, industrial production, manufacturing and trade sales, and personal income. Monthly vintages from December 1976 to November 2003, each containing only the data available then. Four NBER recessions fall in the window: 1980, 1981 to 1982, 1990 to 1991, 2001.

## Reported results
- Both methods identify all eight NBER turning points in real time with no false positives.
- DFMS dates are within one month of the NBER date in seven of eight cases.
- Troughs: DFMS would have called them on average 249 days (about 8 months) before the NBER announcement; the nonparametric algorithm 135 days (about 4.5 months), with a maximum lead of 290 days for the 1991 trough.
- Peaks: neither method beats the NBER on speed. The nonparametric algorithm lagged the NBER announcement by about a quarter on average.

## Signal construction
Not a trading signal. Two reusable components:
1. Evaluation protocol: at each decision time use only data that had been published, refit, record the label, and never revise it afterwards.
2. Confirmation rule: require the filtered regime probability to cross a high threshold and stay there for k consecutive periods before switching, with a separate lower threshold to switch back (hysteresis).

## Relevance to SOL perpetuals at minutes to hours
Market data are not revised the way macro data are, but the same error appears in other forms: features computed with future bars, full-sample standardisation, cluster centroids fitted on the whole history, or funding and open-interest values stamped earlier than they were published. The threshold-plus-persistence rule transfers directly to bar data and is the simplest defence against regime flicker. The asymmetry is the caution: zero false positives was bought with delay, and delay at the start of a move is where a short-horizon trader loses most.

## Caveats
Only four recessions, so "no false positives" rests on eight events. The 0.8 threshold and three-month persistence are fixed by the authors; I did not find a sensitivity test for them in the sections read. The version read is the 2005 working paper; a later journal version exists but was not confirmed in this session.
