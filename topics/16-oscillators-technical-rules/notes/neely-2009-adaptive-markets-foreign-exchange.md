---
title: "The Adaptive Markets Hypothesis: Evidence from the Foreign Exchange Market"
authors: "Neely, Christopher J.; Weller, Paul A.; Ulrich, Joshua M."
year: 2009
venue: "Federal Reserve Bank of St. Louis Working Paper 2006-046B (revised March 2007); later published in the Journal of Financial and Quantitative Analysis"
url: "https://files.stlouisfed.org/files/htdocs/wp/2006/2006-046.pdf"
pdf: "sources/16-oscillators-technical-rules/neely-2009-adaptive-markets-foreign-exchange.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "fx"
horizon: "daily"
tags: "post-publication-decay, adaptive-markets, filter-rules, moving-average, channel-rules, genetic-programming, fx"
---

## Key insight
The cleanest evidence on what happens to technical rules after they are published. Taking the exact rules from earlier well-known FX papers and running them on data that did not exist when those papers were written, the authors find the original profits were real, but returns to simple filter and moving-average rules had vanished by the early 1990s. More complex or less-studied rules decayed more slowly. They read this as support for the Adaptive Markets Hypothesis.

## Method
True out-of-sample replication. Rules are taken from Sweeney (1986, filters), Levich and Thomas (1993, filters and moving averages), Taylor (1994, channel and ARIMA rules), Neely, Weller and Dittmar (1997, rules evolved by genetic programming), and Dueker and Neely (2007, Markov-switching rules). Each is evaluated on its original sample and on the later "ex post" sample. Transaction costs follow a time trend, falling linearly from 10 basis points per switch of position in 1973 to 1.88 basis points in mid-2005, so that falling costs are not mistaken for falling skill. Structural-break tests with unknown break dates complement the split-sample comparison.

## Data and sample
Daily dollar exchange rates (DEM, JPY, CHF, GBP and others, depending on the original paper), 1973 to June 2005.

## Reported results
- Sweeney filters, original sample: the 1% filter earned an average net return of 8.61% a year across ten rates; in the later sample that fell to 1.82%. For the equal-weighted portfolio of filters, the average Sharpe ratio fell from 0.84 to 0.41.
- Levich and Thomas rules, 1976 to 1990 against 1991 to mid-2005: the 1% filter averaged 8.47% a year across four currencies, then -1.14%, a drop of 9.61 points. MA rule returns fell by 7 to 10 points and were mostly negative.
- Taylor channel rules: mean net excess return fell from 5.74% to 1.91%; no mean was significantly above zero in the later period. ARIMA rules fell from 7.09% to 2.97%, with the Sharpe ratio moving from 0.69 to 0.31.
- Genetic-programming rules: average net return fell from 2.94% (Sharpe 0.36) to 0.15% (Sharpe 0.02) after October 1995.
- Markov-switching rules: 6.24% to 2.87%.
- Break tests find clear mean breaks for filter and MA rules but little evidence of one for channel, ARIMA, genetic-programming or Markov rules.

## Signal construction
Not a signal. It gives a monitoring design: track the rolling net return of each rule family and test for a mean break, and expect widely known simple rules to decay first.

## Relevance to SOL perpetuals at minutes to hours
Any edge from standard MA, RSI or breakout rules on SOL should be treated as temporary. Crypto perps are younger than 1970s FX was when these rules worked, but information spreads far faster now, and the crypto evidence (Bakker; Hudson and Urquhart out of sample) already shows decay within a few years. The practical implication is to prefer less-crowded constructions, to size positions on recent rather than full-sample performance, and to build in a retirement test for every rule.

## Caveats
The paper stresses that high exchange-rate volatility makes annual mean returns imprecise, so few individual declines are statistically significant even when large. Daily FX only. Decay could reflect lower volatility or central-bank behavior in the later period as well as learning; the paper cannot fully separate these. I read the 2007 working-paper revision.
