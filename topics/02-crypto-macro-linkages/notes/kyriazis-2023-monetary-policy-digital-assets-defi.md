---
title: "Monetary Policy, Digital Assets, and DeFi Activity"
authors: "Kyriazis, Antzelos; Ofeidis, Iason; Palaiokrassas, Georgios; Tassiulas, Leandros"
year: 2023
venue: "arXiv 2302.10252"
url: "https://arxiv.org/pdf/2302.10252"
pdf: "sources/02-crypto-macro-linkages/kyriazis-2023-monetary-policy-digital-assets-defi.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "minutes"
tags: "fomc, announcement-volatility, fed-funds-surprise, nasdaq, altcoins, defi, intraday"
---

## Key insight
Over 2018 to 2022, unexpected fed funds rate increases on FOMC days are associated with large negative same-day returns on BTC and ETH, similar in size to the Nasdaq response. Five-minute volatility of DeFi collateral tokens at least doubles around the FOMC statement and press conference, more for altcoins than for BTC, and the effect strengthened after December 2021.

## Method
Two exercises.
1. Daily event-study regression on FOMC days: asset return on the expected and unexpected components of the target rate change, with the unexpected component computed from current-month fed funds futures following Bernanke and Kuttner (2005). Assets: BTC index (NYXBT), ETH index (SPETH), S&P broad digital market index (SPCBDM), the same index excluding BTC and ETH (SPCBXM), and the Nasdaq.
2. High-frequency volatility: standard deviation of five-minute returns for each five-minute slot from two hours before to two hours after the FOMC statement (12:00 to 16:00 Eastern, release at 14:00), compared with the same weekday one week before and one week after, following Rosa (2013). Repeated for FOMC Minutes releases, and split at 15 December 2021.
A third part studies DeFi borrowing rates, debt and total value locked; not summarized here.

## Data and sample
FOMC dates from 1 January 2018 to 21 December 2022, 43 observations for the daily regressions. Five-minute prices from Coincap.io for assets used as collateral on the DeFi lending protocols the paper studies (Aave is named in the figure notes; the full token list was not transcribed, MANA is one).

## Reported results
- A one-percentage-point unexpected increase in the fed funds rate lowers the BTC return by 26.33 percent and the ETH return by 30.28 percent, significant at 5 percent, adjusted R-squared near 11 percent. The mean unexpected change is 0.0146 percentage points with standard deviation 0.0576, so typical effects are small.
- Nasdaq response: -23.98 percent per percentage point, with the surprise explaining 27.35 percent of return variation.
- For the broad market index the estimate is -19.53 percent and for the index excluding BTC and ETH -21 percent per percentage point, neither significant at 5 percent.
- With heteroskedasticity-robust standard errors the BTC effect becomes insignificant.
- Volatility: for all assets shown, return volatility is "at least twice higher" on announcement days at the release time, with a second rise half an hour later at the press conference; spikes are larger for altcoins than for BTC. Minutes releases have weaker effects. Both effects are stronger after 15 December 2021.
- Price-level correlations with the Nasdaq over the sample: BTC index 0.885, ETH index 0.856 (these are correlations of index levels as presented in the paper's Table 1, not of returns).

## Signal construction
Volatility-timing rule from the high-frequency part: on scheduled FOMC days, treat 14:00 to about 15:30 Eastern as a high-volatility state, with distinct peaks at 14:00 (statement) and 14:30 (press conference), and expect a larger multiple for altcoins than for BTC. A smaller version applies at 14:00 on Minutes days. Inputs: FOMC calendar only. The directional regression needs a real-time fed funds futures surprise; the coefficient is too fragile to use as a number.

## Relevance to SOL perpetuals at minutes to hours
The intraday volatility profile is directly usable for widening stops, cutting size or pausing entries on a SOL bot, and the finding that altcoins react more than BTC is the closest evidence in this folder on altcoin-specific macro sensitivity. SOL itself is not confirmed as one of the tokens in the parts read. The comparison uses only two control days per event, so the "twice" multiple is rough.

## Caveats
Only 43 FOMC events; the directional result fails under robust standard errors, as the authors acknowledge. The volatility analysis is graphical, without formal tests in the parts read. Level correlations with the Nasdaq are inflated by common trends. Sample ends December 2022. Not peer reviewed. Coincap.io aggregate prices may smooth venue-level moves.
