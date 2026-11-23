---
title: "Technical trading: Is it still beating the foreign exchange market?"
authors: "Hsu, Po-Hsuan; Taylor, Mark P.; Wang, Zigan"
year: 2016
venue: "Journal of International Economics 102, 188-208"
url: "https://profiles.wustl.edu/en/publications/technical-trading-is-it-still-beating-the-foreign-exchange-market/"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "fx"
horizon: "daily"
tags: "fx, stepwise-test, data-snooping, oscillators, emerging-markets, time-variation"
---

## Key insight
The largest data-snooping-robust test of technical rules in currencies finds real predictability and excess profitability in both developed and emerging currencies, but the strength varies over time and across country groups. The authors read that variation as a sign of temporarily irrational behavior and market immaturity, not a permanent edge. Its five-class rule universe is the template for the main crypto study in this folder.

## Method
Only the abstract was read. It states that the authors apply a stepwise test, designed to counter data-snooping bias, to more than 21,000 technical trading rules, judge results on several performance metrics, and cross-validate with out-of-sample analysis. Hudson and Urquhart, who say they follow this paper, describe the five rule classes as moving averages, filters, support-resistance, oscillators and channel breakouts; that description comes from their paper, not from this one.

## Data and sample
Daily data over 45 years for 30 developed and emerging market currencies (per the abstract). Exact dates were not confirmed.

## Reported results
From the abstract only:
- Substantial predictability and excess profitability in both developed and emerging currencies, on several performance metrics.
- The findings are supported by out-of-sample analysis.
- Predictability varies across subperiods and across cultural or geographic groups of countries.
- The authors suggest temporarily not-fully-rational behavior and market immaturity as explanations.

The abstract gives no numbers on transaction costs or on the size of any decline over time.

## Signal construction
Not a single signal. The usable part is the oscillator class as the follow-on crypto paper implements it: compute an n-period RSI, treat readings above 50 + v as overbought and below 50 - v as oversold, and trade the reversal when the indicator crosses back, with optional delay and holding-period filters. Those parameter names come from the Bakker thesis and the Hudson and Urquhart appendix, which adopt this family of rules.

## Relevance to SOL perpetuals at minutes to hours
Two points transfer. The immaturity argument predicts that a new instrument such as SOL perps, and especially a new venue, should show more rule predictability than Bitcoin or major FX, and that it should fade. And the stepwise test is the practical tool for a bot's rule library, because it identifies the set of rules that beat the benchmark and not only whether the best one does. The daily FX evidence does not speak to minute-to-hour horizons.

## Caveats
Abstract-only. The open working-paper copy on the Hong Kong University repository was blocked to automated download, so I could not read the cost assumptions, the subperiod tables, or how many rules survive. Neely, Weller and Ulrich (noted separately) find that the classic FX rules had lost their profits by the early 1990s, so the two papers need to be read together before treating FX as supportive evidence.
