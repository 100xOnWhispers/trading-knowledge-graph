---
title: "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap"
authors: "Sullivan, Ryan; Timmermann, Allan; White, Halbert"
year: 1999
venue: "Journal of Finance 54(5), 1647-1691 (read as LSE Financial Markets Group Discussion Paper 303, October 1998)"
url: "https://eprints.lse.ac.uk/119144/1/dp303.pdf"
pdf: "sources/16-oscillators-technical-rules/sullivan-1999-data-snooping-technical-trading-bootstrap.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "equities"
horizon: "daily"
tags: "data-snooping, reality-check, bootstrap, moving-average, out-of-sample, futures"
---

## Key insight
The significance of the best rule must be judged against the whole universe of rules it was picked from. Doing this with White's Reality Check, the best of 7,846 rules on the Dow still beats the benchmark in 1897 to 1986, but in the ten years after Brock, Lakonishok and LeBaron's sample ended, and in S&P 500 futures, there is no evidence that any rule works. A rule with a stand-alone p-value of 0.04 can have a snooping-adjusted p-value of 0.90.

## Method
A universe of 7,846 parameterizations in five families: filter rules, moving averages, support and resistance, channel breakouts, and on-balance volume averages. For each performance measure (mean return over the benchmark, Sharpe ratio) the test statistic is the maximum over all rules. Its distribution under the null that no rule beats the benchmark is obtained by a stationary bootstrap of the full matrix of rule returns (500 resamples), which preserves the dependence between rules. The paper also tracks how the p-value moves as rules are added one at a time, showing that adding useless rules raises it.

## Data and sample
Dow Jones Industrial Average, daily, 1897 to 1996 (the BLL sample plus ten new years). S&P 500 index futures, daily, 1984 to 1996, used because costs are low and shorting is easy.

## Reported results
- Full 100 years, Dow: best rule in the full universe is a 5-day moving average with a mean annualized return of 17.2% (Reality Check p below 0.002); best in the 26-rule BLL universe earns 9.4% against 4.3% for buy-and-hold.
- The best rule made 6,310 trades (63.1 per year), implying a break-even cost of 0.27% per trade.
- Out of sample, 1987 to 1996: the best rule as of 1986 (the 5-day MA) earns 2.8% with a nominal p-value of 0.322. The introduction puts the probability that the best rule did not beat the benchmark at nearly 12%.
- S&P 500 futures, 1984 to 1996, full universe: the best rule earns almost 10% per year with an unadjusted p-value of 0.04 and an adjusted p-value of 0.90. On the Sharpe criterion the adjusted p-value is 0.99 against an unadjusted value below 0.002.
- A recursive "follow the rule with the highest cumulative wealth so far" strategy does poorly out of sample and loses money on the futures.

## Signal construction
Not a signal. It is the test to run before trusting any signal: record every rule and parameter set tried (including discarded ones), bootstrap the joint return matrix in blocks, and compare the best rule's performance with the bootstrap distribution of the maximum.

## Relevance to SOL perpetuals at minutes to hours
Directly applicable. A parameter sweep over RSI lengths, thresholds, MA pairs and bar sizes on SOL easily exceeds several thousand variants, and the SOL perp history is short. The Reality Check (or Hansen's SPA and the stepwise versions used in the crypto papers here) should be the default acceptance test. The futures result is the closest analogue to a perp: liquid, shortable, cheap, and no rule survived.

## Caveats
The Reality Check is conservative when the universe contains many poor rules, a point Bajgrowicz and Scaillet and Hsu et al. address with FDR and stepwise tests. The universe is still the authors' choice. Daily data only. I read the 1998 discussion-paper version; numbers in the published article may differ slightly.
