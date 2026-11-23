---
title: "Traders in Financial Futures: Explanatory Notes"
authors: "Commodity Futures Trading Commission"
year: 2010
venue: "CFTC Commitments of Traders documentation"
url: "https://www.cftc.gov/idc/groups/public/@commitmentsoftraders/documents/file/tfmexplanatorynotes.pdf"
pdf: "sources/18-positioning-sentiment/cftc-2010-traders-financial-futures-explanatory-notes.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "futures"
horizon: "multi-day"
tags: "commitments-of-traders, tff-report, leveraged-funds, asset-managers, dealers, trader-classification, cme"
---

## Key insight
The Traders in Financial Futures (TFF) report is the regulator's weekly breakdown of open interest in financial futures by four trader types: Dealer/Intermediary, Asset Manager/Institutional, Leveraged Funds, and Other Reportables. It is the format in which CME crypto futures positioning is published. The notes make clear that the CFTC classifies traders, not trades, so a "leveraged fund short" may be a hedge or an arbitrage leg and cannot be read as a directional bet without other information.

## Method
The CFTC collects confidential daily large-trader data for surveillance. For the public report, staff assign each reportable trader to one category using Form 40 filings and other information, according to the trader's predominant activity:
- Dealer/Intermediary: the sell side. Large banks and dealers in securities, swaps and derivatives that tend to run matched books and offset risk across markets.
- Asset Manager/Institutional: pension funds, endowments, insurers, mutual funds and managers with predominantly institutional clients.
- Leveraged Funds: hedge funds and money managers including registered CTAs and CPOs and unregistered funds. Strategies "may involve taking outright positions or arbitrage within and across markets".
- Other Reportables: mostly hedgers of business risk such as corporate treasuries, central banks, smaller banks and mortgage originators.
For each category the report gives long, short and spreading open interest. Spreading is a computed amount of offsetting long and short positions held by the same trader in different calendar months (or futures against options); inter-market spreads are not counted.

## Data and sample
A breakdown of each Tuesday's open interest for markets in which 20 or more traders hold positions at or above the reporting level. Published in futures-only and futures-and-options-combined formats, alongside the legacy COT report (commercial versus non-commercial). Historical TFF data are stated to go back to 13 June 2006, with classifications back-cast from recent ones. Trader counts are suppressed when a category has fewer than four active traders.

## Reported results
No empirical results. Stated properties and limitations:
- The TFF is not a disaggregation of the legacy COT: traders in any TFF category may come from either the commercial or non-commercial legacy group.
- Classification involves staff judgment and can change over time.
- Staff "classifies traders, not their trading activity" and cannot know that all of a hedge fund's activity is speculative.
- Summed trader counts across categories can exceed the total because one trader may appear in both an outright and a spreading count.

## Signal construction
Inputs: weekly TFF rows for CME Bitcoin, Ether and (where listed and above the 20-trader threshold) Solana futures. Per category compute `net = long - short` and `net / open_interest`, their week-over-week change, and a z-score over a trailing year. Non-reportable positions (total open interest minus reportables) proxy for small traders. Update weekly; the data describe Tuesday and are released later in the week, so apply a lag of several days. The publication day and time are not stated in this document.

## Relevance to SOL perpetuals at minutes to hours
A slow regime input only. Weekly data with a multi-day lag cannot time intraday trades. Its use is to describe who holds the regulated-venue side. Because the notes say leveraged funds may hold arbitrage legs, a leveraged-fund net short in a crypto future can be the short side of a basis (carry) trade against spot holdings and need not be a bearish view; the crypto carry literature is covered in topic 03 (Schmeling, Schrimpf and Todorov; Christin et al.). Whether SOL futures on CME meet the reporting threshold each week, and whether Kalshi perps will be covered by any COT-style report, was not confirmed.

## Caveats
The document dates from the 2010 launch of the report and notes a planned Form 40 upgrade; current practice may differ in detail. It contains no crypto-specific content. No test of return predictability from TFF positioning in crypto futures was located in this session; that is a gap, not a negative finding.
