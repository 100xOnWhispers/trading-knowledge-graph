---
title: "smart-money-concepts (smartmoneyconcepts): Python package of ICT / Smart Money Concepts indicators"
authors: "joshyattridge (GitHub account)"
year: 2026
venue: "GitHub repository README (read November 2026)"
url: "https://github.com/joshyattridge/smart-money-concepts"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "17-auction-orderflow-practitioner"
asset_class: "multi"
horizon: "minutes"
tags: "ict, smart-money-concepts, fair-value-gap, order-block, break-of-structure, liquidity-sweep, kill-zones"
---

## Key insight
The ICT or "smart money concepts" vocabulary (fair value gaps, order blocks, break of structure, liquidity, kill zones) reduces to a handful of simple OHLCV rules once someone has to code it. This open-source package is a widely used codification (about 2.3 thousand GitHub stars when read). It provides definitions only, with no evidence, and is used here so that the concepts can be stated precisely enough to test.

## Method
Functions and definitions as described in the README (read through a summarizing tool; wording is paraphrased).
- Fair value gap, `fvg(ohlc, join_consecutive=False)`: a three-candle pattern in which the previous candle's high is below the next candle's low (bullish) or the previous low is above the next high (bearish). Outputs direction, top, bottom and the index at which the gap is later "mitigated" (revisited).
- Swing highs and lows, `swing_highs_lows(ohlc, swing_length=50)`: a candle whose high (low) is the highest (lowest) of swing_length candles before and after it. This uses future bars, so a swing is known only swing_length bars late.
- Break of structure and change of character, `bos_choch(...)`: a break of a prior swing level, by close or by high/low. The README does not explain how the two differ.
- Order blocks, `ob(...)`: described as price ranges where many market orders exist. Outputs top, bottom, a volume figure (the bar's volume plus the two prior bars) and a strength percentage (smaller over larger of two volumes).
- Liquidity, `liquidity(ohlc, swing_highs_lows, range_percent=0.01)`: several swing highs (or lows) within a small price range; outputs the level and the index of the candle that "swept" it.
- Previous high and low for a chosen timeframe (15m to 1M), with broken flags.
- Sessions and kill zones: flags for Sydney, Tokyo, London, New York and named kill-zone windows, with session high and low.
- Retracements: current and deepest percentage retracement from the last swing.

## Data and sample
None. A code library; MIT licence. No release date was visible.

## Reported results
None. The README reports no backtests.

## Signal construction
Each function gives event features from one-minute or five-minute bars: gap present and unfilled, distance to nearest unmitigated gap or order block, equal-highs or equal-lows cluster above or below price, cluster swept in the last k bars, structure-break direction, session flag. Two implementation points matter for a live bot. First, swing-based outputs must be shifted by swing_length bars or recomputed causally, or they leak the future. Second, every zone needs a matched placebo zone (same size, direction and distance from price, at a bar without the pattern) so that any learner is credited only for the pattern's incremental information; the two placebo-controlled studies noted in this topic found none for gaps and order blocks. With those safeguards the features can be offered to a tree model or an evolutionary rule search, which will discard them if they carry nothing.

## Relevance to SOL perpetuals at minutes to hours
The concepts are heavily used by retail crypto traders, so they may matter through crowding even if the "institutional footprint" story is false. In mechanism terms most of them restate ideas with independent evidence: a "liquidity" cluster of equal highs is a stop cluster (Osler); a "sweep" is a failed breakout; a "kill zone" is an intraday seasonality window (topics 10 and 11). The fair value gap is simply a large one-bar move, which overlaps with short-horizon momentum and reversal (topic 13).

## Caveats
No evidence of any kind. Definitions vary between educators; this package is one reading, and the order-block rule in particular is only loosely specified in the README. Look-ahead in swing detection makes naive backtests with this package optimistic. Year in the front matter is the access year.
