---
title: "Exploring volatility reactions in cryptocurrency markets using intraday macroeconomic news analysis"
authors: "Ben Omrane, Walid; Dabbou, Halim; Saadi, Samir; Savaser, Tanseli; Sebai, Saber"
year: 2025
venue: "International Review of Economics & Finance, vol. 103"
url: "https://ideas.repec.org/a/eee/reveco/v103y2025ics1059056025006720.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "minutes"
tags: "announcement-volatility, intraday, macro-news, pre-announcement, bitcoin, ethereum, non-us-news"
---

## Key insight
Only the abstract was read, through the RePEc listing (DOI 10.1016/j.iref.2025.104509). According to it, Bitcoin and Ethereum volatility responds significantly to certain categories of macroeconomic news at five-minute frequency, and much of the response occurs before the official release time. US monetary policy news matters in every phase, and Ethereum reacts more than Bitcoin to US announcements.

## Method
From the abstract: intraday analysis of volatility around scheduled macroeconomic releases from the United States, Germany and Japan, separating the periods before and after the announcement. The volatility estimator, window lengths and model were not seen.

## Data and sample
From the abstract: five-minute data for Bitcoin and Ethereum, 2016 to 2023. Venues and data vendor not seen.

## Reported results
As stated in the abstract (paraphrased by the retrieval tool, so wording is not verbatim):
- Volatility responds significantly to certain news categories, mainly before the announcements.
- US monetary policy news moves volatility in all phases, with a stronger effect during the pandemic period.
- Ethereum reacts more than Bitcoin to US announcements.
- Ethereum shows little response to non-US news, especially before the pandemic.
- The authors conclude that studies of the intraday impact of news on cryptocurrencies should account for both pre- and post-announcement periods.
No coefficients or magnitudes were available.

## Signal construction
A volatility-state adjustment, not a direction signal: raise the expected-volatility estimate in a window that begins before scheduled US releases and FOMC announcements, not only after them. The lead time and size cannot be set from the abstract and need to be estimated from data. German and Japanese releases appear to be lower priority.

## Relevance to SOL perpetuals at minutes to hours
The frequency (five minutes) and assets (the two largest coins) are close to the bot's needs, and the peer-reviewed status adds weight to the announcement-volatility results in the Karau and Kyriazis notes, which are descriptive. The finding that Ethereum responds more than Bitcoin is consistent with the second-hand account in the Kroner note and with the altcoin result in Kyriazis et al., and suggests testing whether SOL's volatility multiple around US events is larger still. The pre-announcement emphasis matters for execution: spreads and volatility may already be elevated when a bot tries to position ahead of a release.

## Caveats
Abstract-only access; no numbers, no methodology detail, and the abstract reached this note as a paraphrase. "Mainly before announcements" could reflect positioning, leaks, or window definitions, which cannot be judged without the paper. Sample ends 2023. Paywalled journal article; no open-access copy was located.
