---
title: "Machine learning and the cross-section of cryptocurrency returns"
authors: "Cakici, Nusret; Shahzad, Syed Jawad Hussain; Bedowska-Sojka, Barbara; Zaremba, Adam"
year: 2024
venue: "International Review of Financial Analysis 94, 103244"
url: "https://ideas.repec.org/a/eee/finana/v94y2024ics1057521924001765.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "multi-day"
tags: "cross-sectional, machine-learning, model-complexity, illiquidity, momentum, limits-to-arbitrage, trading-costs"
---

## Key insight
The crypto counterpart of Gu, Kelly and Xiu. According to the abstract, every machine-learning method tested produces substantial economic gains in the cross-section of coin returns, but added model complexity brings limited benefit, the predictability comes from a handful of simple characteristics, and the alphas are concentrated in small, illiquid, volatile coins that are hard to trade.

## Method
Only the abstract was read (on RePEc IDEAS; the publisher page and the SSRN copy returned access errors). It states that a range of machine-learning models is applied to test cross-sectional predictability of cryptocurrency returns. The specific models, the number of characteristics, the rebalancing frequency and the validation design were not confirmed.

## Data and sample
Not confirmed from the abstract. The SSRN working-paper version is dated 2022 in the OpenAlex record.

## Reported results
From the abstract only, with no numbers given there:
- All methods yield substantial economic gains.
- Greater model complexity gives limited additional benefit.
- Predictability derives mainly from a few simple characteristics, named as market price, past alpha, illiquidity and momentum.
- Unlike in equities, the abnormal returns come from the long side of the trade and persist over time.
- Most strategies remain profitable after trading costs despite high turnover.
- The alphas are concentrated in hard-to-trade assets and depend on capturing extreme returns of small, illiquid and volatile coins.

## Signal construction
Not a signal for a single instrument. It is used as evidence on model choice: in crypto, a penalised linear or shallow tree model on a few characteristics (price level, past risk-adjusted return, illiquidity, momentum) captures most of what more complex learners find.

## Relevance to SOL perpetuals at minutes to hours
Two points matter. First, it supports spending effort on features and validation, not on architecture. Second, it warns that published crypto machine-learning profits are largely a small-coin, long-side phenomenon. SOL is a large liquid asset traded on a perp, so the reported gains should be assumed not to apply until shown on liquid coins. The horizon is also far longer than the bot's.

## Caveats
Abstract-only: no figures, sample dates or model list could be verified, so this note must not be cited for numbers. The grade is provisional and reflects that a peer-reviewed paper exists with an after-cost claim that I could not inspect. A full read is needed to see how large the effect is in the liquid half of the universe, which is the only part relevant here.
