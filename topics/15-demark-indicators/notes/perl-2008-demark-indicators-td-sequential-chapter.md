---
title: "DeMark Indicators, Chapter 1: TD Sequential - Defining the Trend and Identifying Exhaustion Points"
authors: "Perl, Jason"
year: 2008
venue: "Bloomberg Press (publisher's sample chapter, ISBN 9781576603147)"
url: "https://catalogimages.wiley.com/images/db/pdf/9781576603147.excerpt.pdf"
pdf: "sources/15-demark-indicators/perl-2008-demark-indicators-td-sequential-chapter.pdf"
access: "full-text"
source_type: "book"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "multi"
horizon: "n/a"
tags: "td-sequential, td-setup, td-countdown, tdst, perfection, recycle, risk-level, rules"
---

## Key insight
The standard public rulebook for TD Sequential. The 58-page sample chapter states every rule for setup, TDST, perfection, countdown, deferral, cancellation, recycle, entry and stop. It contains no performance statistics; all support is chart examples.

## Method
Buy side (sell side mirrors, with highs for lows). C, H, L are close, high, low.

- Bearish price flip: `C[t-1] > C[t-5]` then `C[t] < C[t-4]`. That bar is setup bar 1.
- Buy setup: nine consecutive closes each below the close four bars earlier. Any interruption cancels it. The setup keeps extending past nine until a bullish flip.
- TDST: a completed buy setup's true high is TDST resistance; a completed sell setup's true low is TDST support. Only closes through the level count.
- Scenario I: no close beyond the opposing TDST level through bar 9, so expect a reversal or consolidation of at least one to four bars. Scenario II: a close beyond it, so expect extension toward a countdown 13.
- Perfection: the low of bar 8 or 9, or a later low, is at or below the lows of bars 6 and 7.
- Perl's setup trade: perfected; no setup bar closed below TDST support; bar 9 closes near support. Stop is the true low of the lowest setup bar minus that bar's true range. Target is TDST resistance, taken only if reward exceeds 1.5 times risk.
- Countdown: starts at setup bar 9 inclusive; count each bar with `C <= L[2 bars earlier]`, not necessarily consecutive.
- Bar 13 qualifier: `L(13) <= C(countdown bar 8)`, otherwise deferred and shown as "+". Optional stricter rule: `L(8) <= C(5)`.
- Cancellation: a completed sell setup, or a true low above TDST resistance.
- Recycle qualifier I: a new buy setup whose true range is at least the previous setup's but under 1.618 times it replaces it. Qualifier II: a new setup inside the prior setup's true range, with no sell setup between, leaves the prior one active.
- "R": a setup running to 18 bars recycles the countdown.
- Entry: aggressive at the close of bar 13; conservative at the first later bullish price flip.
- Risk level: the bar with the lowest true low anywhere in the countdown; its true low minus its true range. Perl stops out intrabar; DeMark's four-step qualified break is also given.
- Timing: expect a response within twelve bars.
- 9-13-9: after a 13, a bullish flip, then a fresh buy setup with no sell setup between gives a second entry.
- Entry triggers TD Camouflage, Clop, Clopwin, Open and Trap are defined from open, close and prior-bar relations.

## Data and sample
None. Illustrations use daily charts of FX pairs, bond futures, equity indices and single stocks.

## Reported results
No statistics. Qualitative claims: the indicator applies unchanged "from one minute to one year", and a completed setup that holds TDST should produce a one-to-four-bar reaction.

## Signal construction
Maintain per bar: flip state, signed setup count including extension beyond 9, setup true range, TDST levels, perfection flag, countdown count with deferral, cancel and recycle state, and risk level. All inputs are OHLC of closed bars.

## Relevance to SOL perpetuals at minutes to hours
The rules are scale-free and run on any bar size. In a 24-hour market the open equals the prior close on most bars, so true range equals bar range and the open-based triggers (Open, Trap, Clop) rarely fire. Every claimed tendency needs testing.

## Caveats
The book is published by Bloomberg Press, and Bloomberg is a licensed distributor of the indicators, so it is not an independent assessment. The sample text has typos that swap "buy" and "sell" in places. Recycle thresholds differ from current vendor documentation (see the DeMARK Analytics note). Chapters on TD Combo, D-Wave, REI, DeMarker, Pressure, Lines and Moving Averages were not accessible.
