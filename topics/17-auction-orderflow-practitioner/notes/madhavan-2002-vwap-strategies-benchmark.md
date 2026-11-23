---
title: "VWAP Strategies"
authors: "Madhavan, Ananth"
year: 2002
venue: "Practitioner journal article, Spring 2002 (journal name not confirmed in this session)"
url: "https://alphatrade.readthedocs.io/en/latest/_vwap_2002.html"
pdf: "none"
access: "secondary"
source_type: "industry-research"
evidence_grade: "D"
topic: "17-auction-orderflow-practitioner"
asset_class: "equities"
horizon: "n/a"
tags: "vwap, execution-benchmark, transaction-cost-analysis, participation-strategy, benchmark-gaming"
---

## Key insight
VWAP became a reference price because institutions are judged against it, not because it forecasts anything. Madhavan's article, as summarized by a third party, sets out the logic of the benchmark, the ways of trading to it, and a warning that uncritical use of VWAP as a benchmark can encourage behaviour that raises cost and risk. For this topic it supplies the institutional reason why price might interact with VWAP in equities, and therefore the reason to doubt that the interaction carries over to crypto.

## Method
I did not read the paper. I read a short summary on the documentation site of an open-source project (AlphaTrade), whose author is not named. According to that summary the article is conceptual: it discusses how far the VWAP benchmark can be meaningfully defined, describes alternative VWAP strategies, and weighs their advantages and drawbacks. The summary names these alternatives: selling the order to a broker-dealer who guarantees VWAP; a forward VWAP cross; trading the order to achieve VWAP or better; agency trading; and automated participation strategies, with the automated approach described as especially attractive. A copy of the article exists on a personal website, which I did not use because it is not an authorized open-access source.

## Data and sample
None, per the summary. The article gives insights and recommendations, not empirical results.

## Reported results
From the secondary summary only:
- VWAP strategies are simple in concept but harder to implement than commonly believed.
- Uncritical use of VWAP as a benchmark can promote trading that increases costs and risk.
- No formulas or numbers appear in the summary.
A search-result description of the article adds that Madhavan credits Berkowitz, Logue and Noser (1988) with the rationale for a volume-weighted average of transaction prices as an unbiased benchmark; I could not open that 1988 paper or its abstract.

## Signal construction
Not a signal. It points to a mechanism that could make VWAP matter (the mechanism below is my hypothesis, not a claim from the summary): if a large share of institutional parent orders is sliced to track the day's volume curve and evaluated against VWAP, then executing traders become more aggressive buyers when price is below VWAP late in the session and more patient when it is above, which pulls price toward VWAP. A bot would test for that mechanism by checking whether deviation from session VWAP mean-reverts more strongly late in a defined session than early, and whether the effect scales with the share of volume that is benchmark-driven.

## Relevance to SOL perpetuals at minutes to hours
The mechanism is specific to markets with a defined session, a closing print and a large population of benchmarked agency orders. SOL perps have none of the first two, and the size of VWAP-benchmarked flow in crypto is unknown to me. VWAP on SOL should therefore be treated as a volume-weighted moving average with an arbitrary anchor until a test shows otherwise. The related deep-learning execution study on Binance perpetuals (Genet 2025, noted in this topic) confirms that VWAP execution is practised in crypto but does not measure how much flow uses it.

## Caveats
Secondary access to an anonymous summary; the journal name, page numbers and most of the content are unconfirmed. The summary gives the author's affiliation as ITG Inc., an execution-services firm, so the article is not disinterested. Conceptual article with no data. Written before modern electronic markets and long before crypto.
