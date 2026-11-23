---
title: "Monetary Policy and Bitcoin"
authors: "Karau, Soeren"
year: 2021
venue: "Deutsche Bundesbank Discussion Paper No 41/2021"
url: "https://bundesbank.de/resource/blob/880226/8334c7e2b5c8058038ca8f1393ca2edd/472B63F073F071307366337C94F8C870/2021-11-19-dkp-41-data.pdf"
pdf: "sources/02-crypto-macro-linkages/karau-2021-monetary-policy-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "multi-day"
tags: "monetary-policy-shocks, proxy-var, fomc, ecb, announcement-volatility, emerging-markets"
---

## Key insight
Bitcoin's intraday volatility is systematically higher in narrow windows around FOMC and ECB announcements, so monetary news matters to the market, but the direction of the response is not simply related to rate changes. In a weekly proxy VAR over 2013 to 2021, an ECB tightening lowers Bitcoin while a Fed tightening raises it, which the author attributes to demand from emerging markets when global dollar conditions tighten.

## Method
Two parts.
1. High-frequency description: realized volatility of five-minute Bitcoin returns inside announcement windows compared with the same clock windows on non-announcement days. FOMC window: 10 minutes before to 20 minutes after the statement, or to 60 minutes after the start of the press conference when there is one. ECB window: 10 minutes before the statement to 75 minutes after the start of the press conference. Days in the top decile of Bitcoin volatility are dropped.
2. Structural analysis: weekly proxy VAR with 8 lags. Monetary policy shocks are identified with external instruments built from high-frequency asset-price changes around announcements, with sign restrictions separating pure policy shocks from central-bank information shocks (in the spirit of Jarocinski and Karadi). Responses are scaled to a 10 basis point rise in two-year yields. Additional variables: equity indices, EUR-USD, five-year inflation swaps, Bitcoin price spreads across fiat currencies, and exchange flows and balances built from clustered blockchain data.

## Data and sample
Five-minute Bitcoin prices in USD and EUR from bitcoincharts.com, January 2014 to June 2021. Weekly VAR sample June 2013 to June 2021 (blockchain flow series end in 2017). Bitcoin daily prices from bitcoinity.org.

## Reported results
- The distribution of announcement-window volatility is shifted upward relative to control windows for both central banks.
- The standard deviation of daily Bitcoin returns in USD from January 2014 to June 2021 is "almost 4 percent", about four times that of the S&P 500.
- Impact responses of the Bitcoin price to a contractionary shock (10 basis points on two-year yields): around -20 percent for the euro area and around +7 percent for the US. The author notes these are roughly in line with other asset prices once Bitcoin's higher volatility is considered.
- Instrument F statistics are about 12 (US) and 30 (euro area).
- After a US tightening, Bitcoin prices in emerging-market currencies, above all the Chinese yuan, rise more than in USD, and exchanges serving those currencies see net coin inflows.
- A footnote cites a companion paper reporting an upward Bitcoin drift before ECB announcements and a downward drift before FOMC announcements.

## Signal construction
The robust, usable element is a volatility regime flag, not a direction: mark the window from 10 minutes before a scheduled FOMC or ECB statement until 60 to 75 minutes after the press conference begins as a high-volatility state. Inputs are the published central-bank calendars. The signed VAR responses are not a signal as estimated; they are weekly and sample-dependent.

## Relevance to SOL perpetuals at minutes to hours
The volatility finding transfers directly to position sizing and stop placement around central-bank events. The sign finding (Fed tightening is positive for Bitcoin) should not be used: it comes from a sample ending June 2021, before the 2022 tightening, and conflicts with the later evidence in the Copestake, Kyriazis and Kroner notes, which find negative responses. A later ECB/BIS paper in this folder (Aldasoro et al.) cites a 2023 journal version of this paper as documenting Bitcoin falling after US tightening; that version was not opened and the discrepancy is not resolved here.

## Caveats
Single asset, pre-2021 market structure, heavy Chinese influence in the early sample that later disappeared. VAR results depend on identification and on a short weekly sample. The emerging-market demand channel relies on exchange-clustering data ending in 2017. Announcement-window volatility is descriptive, with the most volatile decile of days removed.
