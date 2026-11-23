---
title: "The Profitability of Technical Analysis: A Review"
authors: "Park, Cheol-Ho; Irwin, Scott H."
year: 2004
venue: "AgMAS Project Research Report 2004-04, University of Illinois at Urbana-Champaign"
url: "https://farmdoc.illinois.edu/assets/marketing/agmas/AgMAS04_04.pdf"
pdf: "sources/16-oscillators-technical-rules/park-2004-profitability-technical-analysis-review.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "16-oscillators-technical-rules"
asset_class: "multi"
horizon: "daily"
tags: "survey, technical-analysis, futures, fx, data-snooping, transaction-costs, genetic-programming"
---

## Key insight
The standard survey of the field up to 2004. The count of studies favors technical rules, but the authors' own reading is that most positive results rest on flawed tests: data snooping, rules chosen after the fact, and weak treatment of risk and costs. Profitability was concentrated in futures and foreign exchange, was absent in US stocks, and faded from the early 1990s.

## Method
A literature review of 106 pages covering practitioner surveys, theory (martingale and random-walk models against noisy rational expectations, feedback and behavioral models), and empirical studies. Empirical work is split into "early" studies (1960 to 1987, 42 studies) and "modern" studies (1988 to August 2004). Modern studies are sorted into seven groups by test design: standard, model-based bootstrap, genetic programming, Reality Check, chart patterns, nonlinear, and others. The report also gives formulas for the main systems, including dual moving average crossover, outside price channel, Wilder's Relative Strength Index, and Alexander's filter.

## Data and sample
Published studies on stocks, futures and foreign exchange.

## Reported results
- Surveys: about 30% to 40% of practitioners regard technical analysis as an important factor in price movements at horizons up to six months.
- Of 92 modern studies, 58 report positive results, 24 negative and 10 mixed.
- Early studies: profitable in foreign exchange and futures, not in stocks before the 1980s.
- Modern studies: consistent economic profits in a variety of speculative markets "at least until the early 1990s".
- Examples cited: Lukac, Brorsen and Irwin found four systems earning 3.8% to 5.6% annual net portfolio returns across 12 futures markets in 1978 to 1984. Bessembinder and Chan found the average break-even one-way cost for the BLL rules on the Dow fell to 0.22% in 1976 to 1991, against estimated costs of 0.24% to 0.26%.
- Genetic-programming studies: rules found by genetic programs worked in foreign exchange but not in stocks. Neely and Weller's rules earned 1.7% to 8.3% a year net in four currencies in 1981 to 1992, then about zero or negative in 1993 to 1998 except for the yen.

## Signal construction
Not a signal. It is the map of the pre-crypto evidence and a checklist of test flaws. For the RSI specifically, the report gives Wilder's formula: RSI = 100 - 100/(1 + RS), with RS the ratio of average up-closes to average down-closes over n periods.

## Relevance to SOL perpetuals at minutes to hours
Three lessons carry over. First, rule profits have historically been largest in young, trending, leveraged markets (futures, FX in the 1970s and 1980s), which is the optimistic case for crypto perps. Second, those profits decayed within one to two decades as markets matured. Third, the test design matters more than the rule: parameter optimization must be followed by out-of-sample verification with costs. Almost all the surveyed evidence is daily, so it says little about minute-to-hour horizons.

## Caveats
A vote count of published studies is exposed to publication bias, which the authors acknowledge indirectly through their emphasis on testing flaws. Coverage stops in 2004. I read the 2004 research report; a condensed journal version exists but was not opened in this session. Oscillators receive little separate treatment because few of the surveyed studies test them alone.
