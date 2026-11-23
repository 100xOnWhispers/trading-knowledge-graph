---
title: "Dynamic Volume-Return Relation of Individual Stocks"
authors: "Llorente, Guillermo; Michaely, Roni; Saar, Gideon; Wang, Jiang"
year: 2002
venue: "NBER Working Paper 8312 (May 2001), the version read; published in the Review of Financial Studies, 2002 (journal version not opened)"
url: "https://www.nber.org/system/files/working_papers/w8312/w8312.pdf"
pdf: "sources/28-shock-response-price-pressure/llorente-2002-dynamic-volume-return-relation.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "28-shock-response-price-pressure"
asset_class: "equities"
horizon: "daily"
tags: "volume, autocorrelation, informed-trading, continuation, reversal, information-asymmetry"
---

## Key insight
Whether a high-volume move reverses or continues depends on why people traded. Returns produced by risk-sharing (hedging) trades reverse; returns produced by trades on private information continue, because the information is only partly in the price. Across 2,226 stocks, the sign of the volume-return interaction lines up with proxies for information asymmetry: liquid large caps reverse after high-volume days, illiquid small caps continue.

## Method
A simple equilibrium model in which investors trade both to hedge and to speculate on private information. Then, for each stock, a time-series regression:

`R(t+1) = C0 + C1 * R(t) + C2 * V(t) * R(t) + e`

where `V` is detrended log daily turnover. `C2 < 0` means high-volume returns reverse; `C2 > 0` means they continue. The stock-level `C2` is then related to information-asymmetry proxies: opening bid-ask spread, market capitalization and analyst following. The body text of the PDF did not extract cleanly; the abstract and introduction were read as page images and the tables as text.

## Data and sample
All NYSE and AMEX common stocks in CRSP with at least 1,000 trading days between 1993 and 1998: 2,226 stocks, daily. Spreads from TAQ. A robustness panel uses ten years (1989-1998).

## Reported results
- By spread tercile (Table 2): low-spread stocks have mean `C2 = -0.0028` (378 of 742 negative); medium `0.0032`; high-spread stocks `0.0355`, with 438 of 742 significant at the 10 percent level and only 141 negative.
- By size tercile (Table 3): small firms `C2 = 0.0303`; medium `0.0049`; large `0.0007`.
- Cross-sectional regression of `C2` on the ordinal spread rank has slope 0.0557 (t = 15.9); on the size rank, slope -0.0442 (t = -12.4).
- The unconditional first-order coefficient `C1` is strongly negative for small and high-spread stocks (about -0.10 to -0.12, consistent with bid-ask bounce) and near zero for large stocks.
- The introduction states the pattern survives removing market-wide components of return and volume.
- Scope record: horizon one day ahead; conditioning variable detrended turnover interacted with information asymmetry; sign negative for low-asymmetry names, positive for high-asymmetry names; costs not charged, no strategy.

## Signal construction
Same feature as Campbell, Grossman and Wang (`V * r`), but the sign of its coefficient is a state variable, not a constant. A bot should estimate `C2` conditionally: separately for windows with high and low adverse-selection proxies (wide spread, high realized impact per unit flow, known news windows, token-specific events). A rolling regression of next-bar return on `r` and `V * r` by regime gives the current sign. Proxies for "speculative" flow in crypto would have to be chosen and tested; the paper's proxies are slow cross-sectional traits, not intraday states.

## Relevance to SOL perpetuals at minutes to hours
This is the paper that prevents a naive reading of the price-pressure literature. A volume spike on SOL caused by liquidations is hedging-type flow and should reverse; a spike caused by a protocol exploit, an ETF decision or a macro release is information and should continue. SOL sits between the paper's groups: liquid, but with frequent idiosyncratic news. The practical implication is that volume alone cannot sign the trade; it needs a second variable that says whether the flow was forced or informed (for example an open interest drop with one-sided taker flow, versus a move on rising open interest).

## Caveats
Daily data on 1990s US equities. The proxies for information asymmetry are correlated with illiquidity, so part of the result could be microstructure. Average `C2` values are small. No costs, no out-of-sample test. Much of the paper's text could not be machine-read in this session.
