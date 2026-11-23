---
title: "How Do Cryptocurrencies Price Economic News?"
authors: "Kroner, T. Niklas; Mohammed, Idrees; Vega, Clara"
year: 2026
venue: "Working paper (Federal Reserve Board authors), March 2026; listed on SSRN as abstract 6447644"
url: "https://tokenpost.com/news/insights/19578"
pdf: "none"
access: "secondary"
source_type: "working-paper"
evidence_grade: "C"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "minutes"
tags: "event-study, intraday, cpi, nonfarm-payrolls, fomc, order-flow, institutional-adoption, regime-shift-2021, secondary-source"
---

## Key insight
Read only through a news article, not the paper. As described there, a Federal Reserve staff study using minute-level data from 2015 to 2025 finds that Bitcoin and Ethereum barely reacted to US macro releases before 2020 but react strongly and quickly after 2021, in the same direction as equities and with larger magnitude. If accurate, this resolves the conflict between the earlier "disconnect" result (Benigno and Rosa) and the post-2021 risk-asset view: both are right for their sample periods.

## Method
From the article: intraday event study around FOMC decisions, CPI releases and nonfarm payrolls, plus an order-flow framework measuring the price impact of buying and selling pressure after announcements. Crypto responses are compared with the S&P 500, gold, the euro and the yen. The paper's regression specification, window lengths and standard errors were not seen.

## Data and sample
From the article: minute-by-minute trading data, 2015 to 2025, for Bitcoin and Ethereum, with venue-level analysis of Binance, OKX and Coinbase. Whether spot or derivatives data are used is not stated in the article.

## Reported results
All of the following are the article's statements about the paper, not figures read from the paper.
- Before 2020 the reaction to these releases was statistically weak; after 2021 volatility and trading activity rise sharply after announcements.
- Prices absorb the news within roughly 15 to 30 minutes.
- A one-standard-deviation upside surprise in headline CPI is associated with a fall of about 29 to 30 basis points in Bitcoin and 43 to 46 basis points in Ethereum, against about 19 basis points for the S&P 500.
- The correlation between crypto and S&P 500 responses to macro news averages about 0.88 to 0.89. Gold and the major currencies show the opposite sensitivity pattern.
- The sign of Bitcoin's response to payroll surprises flipped around 2020, so strong payrolls became negative for Bitcoin.
- Post-announcement order-flow price impact on Binance and OKX becomes statistically meaningful only after 2021. On Coinbase before 2021, net buying sometimes coincided with falling prices, which the paper is said to link to contrarian retail positioning.
- The authors attribute the post-2021 shift to institutional participation.

Identification: the article does not name the paper or its authors; it describes a March paper by three Federal Reserve economists on this subject. The title, co-authors and March 2026 date were confirmed on the first author's homepage (niklaskroner.com, fetched in this session), which links to SSRN abstract 6447644. SSRN refused automated access, so the match between article and paper is an inference, though a strong one. Search-result snippets of a third-party digest that could not be opened add two claims that are unverified: that surprises in non-headline components of CPI and payrolls matter more than headline surprises, and that a Fed policy shock that leaves yields unchanged still moves crypto prices.

## Signal construction
If the paper's numbers hold, the template is the standard surprise signal: at release, z = (actual minus consensus) / historical standard deviation; expected Bitcoin move about -0.3 percent times z for CPI, with Ethereum about 1.5 times that, realized within 15 to 30 minutes. Two refinements suggested by the description: use equity-index futures' immediate reaction as a real-time proxy for the surprise sign and size, and watch signed order flow on Binance and OKX in the first minutes, since post-2021 price impact there is reported as informative.

## Relevance to SOL perpetuals at minutes to hours
This is the closest match in the literature to the bot's horizon and event set, and it implies the adjustment window (15 to 30 minutes) is long enough for a non-colocated bot to participate. SOL is not mentioned in the article. Ethereum's larger response than Bitcoin's suggests higher-beta coins react more, which makes a SOL test worthwhile but proves nothing about SOL. The paper must be read in full before any coefficient is used.

## Caveats
Secondary access through a crypto news outlet; numbers may be rounded, selected or misreported, and the paper's caveats are missing. Working paper, not peer reviewed. The post-2021 sample contains one dominant inflation episode, so CPI sensitivity may be specific to a period when inflation drove policy. Evidence grade C reflects that the methodology could not be inspected; the underlying study, a central-bank working paper with a ten-year intraday sample, would probably merit B once read, and the grade should be revisited then.
