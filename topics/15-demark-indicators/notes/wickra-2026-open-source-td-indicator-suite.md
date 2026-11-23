---
title: "Wickra indicator documentation: DeMark family (TD Setup, Countdown, Sequential, Combo, REI, DeMarker, Pressure, D-Wave, Lines, Moving Average, Differential, Risk Level, Range Projection, Propulsion)"
authors: "kingchenc (Wickra project)"
year: 2026
venue: "docs.wickra.org (open-source library, MIT or Apache-2.0)"
url: "https://docs.wickra.org/Indicators/Indicator-TdSequential"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "multi"
horizon: "n/a"
tags: "open-source, implementation, td-rei, td-demarker, td-differential, td-pressure, td-combo, streaming"
---

## Key insight
An open-source streaming library (Rust core with Python and Node bindings) that documents formulas for about twenty DeMark-style indicators. It is the only open source found with explicit formulas for TD REI and TD Differential. Several entries are simplified reconstructions that do not match the book or vendor rules, and the documentation says so in places. Use it as a reference implementation to check against, not as an authority.

## Method
Documentation pages for each indicator were read. Formulas as documented:

- TD Setup: signed count of consecutive `C[t] < C[t-4]` (buy, positive) or `>` (sell, negative); equality resets; saturates at 9. No price-flip requirement, no perfection.
- TD Sequential and Countdown: after a 9, count `C <= L[t-2]` (buy). Bar 13 counts only if `L <= C(countdown bar 8)`, else deferred. An opposite setup invalidates. Recycle is "not implemented". No TDST cancellation.
- TD Combo: after a 9, a bar counts if `C <= L[t-2]` and `L <= L[t-1]` and `C < C[t-1]`. This omits the comparison with the previous Combo bar's close and the start from setup bar 1 that Lissandrin et al. describe.
- TD REI (period 5): `num = (H-H[2]) + (L-L[2])` if the bar overlaps bars 5 to 6 back (`(H >= L[5] or H >= L[6]) and (L <= H[5] or L <= H[6])`) or the bar two back overlaps closes 7 to 8 back; else 0. `den = |H-H[2]| + |L-L[2]|`. `REI = 100 * sum(num,5) / sum(den,5)`. Bands stated as plus or minus 60.
- TD DeMarker (period 14): `sum(max(H-H[1],0)) / (sum(max(H-H[1],0)) + sum(max(L[1]-L,0)))`; bands 0.7 and 0.3; 0.5 when both sums are zero.
- TD Differential: with `TrueLow = min(L, C[1])`, `TrueHigh = max(H, C[1])`, buying = `C - TrueLow`, selling = `TrueHigh - C`. Buy when two consecutive lower closes occur and buying pressure rises while selling pressure falls versus the prior bar. Sell is the mirror.
- TD Pressure: `100 * SMA(((C-O)/(H-L))*V, n) / SMA(V, n)`.
- TD Risk Level: lowest-low bar of a buy setup, low minus that bar's true range (mirror for sells).
- TD Range Projection: `X = H+2L+C` if `C<O`, `2H+L+C` if `C>O`, `H+L+2C` if equal; next high `X/2 - L`, next low `X/2 - H`.
- TD Propulsion: +1 if `O >= C[1]` and `C > H[1]`; mirror for -1.
- "TD Lines" in this library is TDST: max high of the last buy setup and min low of the last sell setup.
- TD Moving Average: 5 and 13 bar SMAs of the median price. TD D-Wave: a counter cycling 1 to 8 on fractal swing pivots; the page calls it "a simplified swing-leg count".

## Data and sample
None. Unit-test fixtures only.

## Reported results
No performance evidence. Interpretive statements such as Combo being "higher conviction" are unsupported assertions.

## Signal construction
The streaming `update(candle)` interface matches what a live bot needs. Port or wrap the Setup, Countdown, REI, DeMarker and Differential formulas, then add what is missing from Perl: price-flip start, perfection, TDST cancellation, recycle, and the countdown-wide risk level.

## Relevance to SOL perpetuals at minutes to hours
Directly usable as feature code on any bar size. The TD Pressure formula needs bar volume, which should come from the venue where price discovery happens, not from Kalshi. Propulsion and Range Projection depend on the open differing from the prior close and carry little information on continuous bars.

## Caveats
Unofficial and unaudited by me; I read the documentation, not the Rust source. Naming is loose (TDST is labeled TD Lines; the moving-average and D-Wave entries differ from the vendor's descriptions of those studies). The REI bands and the Pressure formula could not be checked against DeMark's books. A library published in 2026 by a single maintainer has no track record.
