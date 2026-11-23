---
title: "Technical Trading Revisited: False Discoveries, Persistence Tests, and Transaction Costs"
authors: "Bajgrowicz, Pierre; Scaillet, Olivier"
year: 2012
venue: "Journal of Financial Economics 106(3), 473-491"
url: "https://ideas.repec.org/a/eee/jfinec/v106y2012i3p473-491.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "equities"
horizon: "daily"
tags: "false-discovery-rate, data-snooping, persistence, transaction-costs, moving-average"
---

## Key insight
Even with a more powerful multiple-testing method than the Reality Check, the historical success of technical rules on the Dow has no economic value. An investor could not have selected the future best rules in advance, and low transaction costs remove the in-sample performance. The paper is the main counterweight to Brock, Lakonishok and LeBaron.

## Method
Only the abstract was read. It states that the authors use the false discovery rate (FDR) as a new approach to data snooping. Compared with existing methods, FDR is described as more powerful: it selects more outperforming rules, which lets an investor diversify against model uncertainty rather than bet on a single best rule. The paper then runs persistence tests (do rules selected in one period keep working in the next?) and adds transaction costs.

## Data and sample
Dow Jones Industrial Average, daily prices, 1897 to 2011 (per the abstract). The rule universe is not described in the abstract; the Wei thesis noted in this folder says Bajgrowicz and Scaillet follow the Sullivan, Timmermann and White universe, which I did not confirm in the paper itself.

## Reported results
From the abstract only:
- Persistence tests show that an investor would never have been able to select ex ante the future best-performing rules, even using the more powerful FDR method.
- In-sample performance is completely offset once low transaction costs are introduced.
- The authors conclude that the economic value of technical trading rules reported for early periods is questionable.

No numerical results are given in the abstract.

## Signal construction
Not a signal. It supplies two acceptance tests for any rule library:
1. FDR control. From the p-values of all candidate rules, estimate the share of selected rules that are false positives and choose the selection threshold so that share stays below a target (for example 10%). This yields a portfolio of rules, not one winner.
2. Persistence. Select rules on a window, trade them on the next window, roll forward, and judge only the out-of-window returns net of costs.
The general FDR logic above is standard; the paper's exact estimator was not read.

## Relevance to SOL perpetuals at minutes to hours
The persistence test is the right design for a live bot, which must re-select rules as it goes. Crypto studies that report many "significant" rules after FDR or Bonferroni correction (Hudson and Urquhart) do not run this ex ante selection test over many windows, and where a single out-of-sample window is tried, Bitcoin fails it. For SOL at intraday frequency, turnover is far higher than for daily Dow rules, so the "low costs erase it" result is the base case to beat.

## Caveats
Abstract-only, so no numbers and no detail on the rule universe or cost levels. One equity index, daily data. A null result on the Dow does not prove a null in a young 24/7 market, but it shifts the burden of proof. FDR methods assume enough true nulls to estimate the null proportion, which may be fragile with highly correlated rules.
