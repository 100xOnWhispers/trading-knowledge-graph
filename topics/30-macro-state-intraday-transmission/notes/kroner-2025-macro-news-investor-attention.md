---
title: "How Markets Process Macro News: The Importance of Investor Attention"
authors: "Kroner, T. Niklas"
year: 2025
venue: "Working paper, draft of 18 February 2025 (author-hosted; also a Federal Reserve FEDS working paper)"
url: "https://raw.githubusercontent.com/tnkroner/website/master/inflation_attention_073123.pdf"
pdf: "sources/30-macro-state-intraday-transmission/kroner-2025-macro-news-investor-attention.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "hours"
tags: "announcement, cpi, investor-attention, state-dependence, bitcoin, overreaction, event-study, post-2020"
---

## Key insight
The size of the market response to a given macro release is not a constant; it scales with how much attention investors are paying to that release beforehand. During the 2021 to 2023 inflation surge the response to CPI surprises rose by an order of magnitude in yields and sharply in equities, the VIX, the euro and Bitcoin, while responses to other releases were unchanged. A pre-release attention measure built from professional news coverage predicts the response size, and high-attention releases are followed by partial reversal over the next days.

## Method
Event study of 60-minute log changes on standardised surprises (actual minus Bloomberg mean forecast, divided by its standard deviation) for 16 releases, with separate coefficients for a low-inflation period (July 2009 to May 2021) and a high-inflation period (to 12 July 2023). Attention for series k on day d: IA = N_k,d / N-bar, the number of Bloomberg Terminal articles about that series divided by the trailing one-year average of total daily articles. Pre-announcement attention (CPI-IA) is built from the days before each release and interacted with the surprise, in a horse-race against uncertainty measures. Daily local projections test for over- or under-reaction. The same construction is applied to payrolls and Fed announcements.

## Data and sample
Intraday futures and spot prices, July 2009 to July 2023: Treasury yields, inflation swaps, E-mini S&P 500, VIX futures, commodity index, corporate bond ETF, euro and Bitcoin spot against the dollar. Covers pre- and post-2020. Bitcoin only; no altcoins or SOL.

## Reported results
Table 3, 60-minute response to a one-standard-deviation positive CPI surprise, in basis points (standard errors in parentheses; the mapping of cells was reconstructed from extracted text):
- Bitcoin: -3.87 (11.13) in the low-inflation period, -114.25 (40.41) in the high-inflation period; equality rejected with p = 0.01.
- S&P 500 futures: -4.98 (2.60) versus -66.09 (18.46); p = 0.00.
- VIX futures: +27.75 versus +188.53. Euro: -1.77 versus -30.83. Commodities: -0.30 versus -22.99.
Other findings:
- Yield responses to CPI are more than ten times larger in the high-inflation period; no other release shows a comparable rise.
- Trading volume around CPI rose exceptionally; volumes around other releases were stable.
- CPI-IA predicts stronger reactions even when uncertainty measures are allowed to do the same.
- Interest rates and inflation swaps overreact in the first days after high-attention CPI releases.
- Attention matters similarly for payrolls and Fed announcements historically.

## Signal construction
Attention gate for event sizing. For each scheduled release, count news items mentioning it over the prior several days and normalise by the trailing-year average of total daily items; standardise per series. Expected response = beta_k x surprise x (1 + gamma x attention). Without terminal data, substitutes named in the paper are Dow Jones Newswires counts, Google searches and mainstream media coverage; pre-release futures volume is a further proxy. After a high-attention release, the reversal finding argues for taking profit within the day and not carrying the move.

## Relevance to SOL perpetuals at minutes to hours
This is the one full-text source in the topic with a measured intraday Bitcoin response: about 1.7 times the S&P 500 futures response in the same 60-minute window in 2021 to 2023, and statistically zero before. It supports sizing event trades by regime (which release the market is currently obsessed with) and warns that CPI betas estimated in 2022 will overstate the response once attention moves on, for instance to labour data. SOL is not covered; an ETH-like higher beta is plausible but unmeasured.

## Caveats
The high-inflation period runs from mid-2021 to July 2023, roughly two years of monthly CPI releases, so the Bitcoin coefficient rests on few observations and has a wide standard error. Bitcoin spot source and venue are not confirmed here. Working paper. The attention measure requires licensed news counts; proxies may behave differently.
