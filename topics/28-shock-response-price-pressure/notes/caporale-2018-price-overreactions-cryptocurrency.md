---
title: "Price Overreactions in the Cryptocurrency Market"
authors: "Caporale, Guglielmo Maria; Plastun, Alex"
year: 2018
venue: "CESifo Working Paper No. 6861 (January 2018); a version was later published in the Journal of Economic Studies (journal version not opened)"
url: "https://www.ifo.de/DocDL/cesifo1_wp6861.pdf"
pdf: "sources/28-shock-response-price-pressure/caporale-2018-price-overreactions-cryptocurrency.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "daily"
tags: "overreaction, large-moves, contrarian, inertia, transaction-costs, negative-result"
---

## Key insight
After a day with an abnormally large price range, the next day's moves are larger than usual in both directions: both the counter-move and the continuation exceed their normal size. This is a volatility effect, not a directional one. When the two directional readings are traded with costs, fading the overreaction loses money and following it makes money that cannot be told apart from random trading. The paper is the standard citation for "overreactions exist in crypto but are not exploitable".

## Method
Daily return is defined by range, `R = (High - Low) / Low`. A day is an overreaction when `R` exceeds its trailing mean plus `k` standard deviations (`k = 1`, averaging window 30 days, both chosen after preliminary tests). The size of the next-day counter-move is measured from the next open to the next-day extreme against the direction of the shock; the continuation is measured to the extreme in the same direction. Two hypotheses are tested with t-tests, ANOVA, Mann-Whitney tests and dummy regressions: H1, counter-moves after overreactions differ from normal days; H2, same-direction moves differ. A "trading robot" in MetaTrader then simulates two rules on Bitcoin with spread, fees and commissions: Strategy 1 fades the shock at the next open and closes at the end of that day; Strategy 2 follows it. Results are compared with random trades by t-test.

## Data and sample
Daily data for Bitcoin, Litecoin, Ripple and Dash, 28 April 2013 to 31 December 2017. Trading simulation on Bitcoin only, 2015 to 2017.

## Reported results
- With `k = 1` and a 30-day window, 243 of 1,575 Bitcoin days (15%) are overreactions.
- Next-day counter-move after an overreaction averages 3.89% against 1.96% after normal days (t = 4.75).
- Both H1 and H2 are confirmed by every test for all four coins.
- Trading robot, Bitcoin: Strategy 1 (fade) loses in 2015, 2016 and 2017 (for example -6,279 USD on 72 trades in 2017, 46.5% winners). Strategy 2 (follow) gains in each year (for example +5,879 USD on 72 trades in 2017, 53.6% winners). Neither differs significantly from random trading; 155 trades over 2015-2017.
- The authors conclude the anomaly does not contradict market efficiency.
- Scope record: horizon one day after a large-range day; conditioning variable daily range above mean plus one standard deviation; sign none that is reliable (fade negative, follow positive but insignificant); costs charged.

## Signal construction
`R(t) = (High - Low) / Low`; flag when `R(t) > mean(R, 30) + 1 * std(R, 30)`. The supported use is as a volatility-state flag: the day after a flagged day has roughly double the normal excursion in each direction. Direction of the flagged day comes from open versus close. The paper gives no support for a directional position.

## Relevance to SOL perpetuals at minutes to hours
Useful as a negative result and as a design warning. It shows that "large move, then larger moves both ways" is easy to mistake for a reversal signal when the outcome is measured by the adverse excursion alone. Any SOL test should measure signed close-to-close returns over a fixed horizon, not maximum counter-moves. The daily horizon and range-based shock definition are coarser than the bot needs; intraday evidence comes from De Nicola (2021) and from the authors' follow-up on hourly data, both in this folder. The slight edge to continuation after large days is consistent with that follow-up.

## Caveats
Daily data ending in 2017, before perps dominated volume. Parameters were selected using a profitability map of the same data. Profits are reported in USD without position size, so they cannot be converted to returns. Details of the cost assumptions are not given. Outcome measures based on extremes overstate both hypotheses.
