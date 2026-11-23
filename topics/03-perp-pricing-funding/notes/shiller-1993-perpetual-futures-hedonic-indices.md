---
title: "Measuring Asset Values for Cash Settlement in Derivative Markets: Hedonic Repeated Measures Indices and Perpetual Futures"
authors: "Shiller, Robert J."
year: 1993
venue: "NBER Technical Working Paper 131 (December 1992); the NBER listing gives the published version as Journal of Finance 48(3), 1993"
url: "https://www.nber.org/system/files/working_papers/t0131/t0131.pdf"
pdf: "sources/03-perp-pricing-funding/shiller-1993-perpetual-futures-hedonic-indices.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "futures"
horizon: "n/a"
tags: "perpetual-futures, contract-design, funding, no-arbitrage, origin"
---

## Key insight
Shiller proposes the perpetual futures contract: a futures contract with no expiry that cash-settles every day on both the change in its own price and the gap between a dividend (or rent) index and an interest charge on the futures price. That second term is the ancestor of the crypto funding payment. He also states plainly that the link between the perpetual price and the cash price is weaker than a textbook no-arbitrage condition, which is the point every later pricing paper has to deal with.

## Method
Contract design and verbal arbitrage argument, no data. The daily resettlement received by a long is (equation 5 of the working paper):

`s(t+1) = (f(t+1) - f(t)) + (d(t+1) - r(t) * f(t))`

where `f` is the perpetual futures price, `d` the dividend index for the day, and `r` the one-day return on an alternative asset (in practice a riskless short rate). The first bracket is the ordinary daily mark-to-market. The second replaces the single final settlement of a dated future with a small settlement every day. A long who invests `f(t)` in the alternative asset each day reproduces the cash flows of holding the underlying, so `f` should tend to the cash price `p` when one exists.

## Data and sample
None. The first half of the paper is about hedonic repeated-measures index construction for real estate and labour income, which is unrelated to crypto.

## Reported results
- The futures price is "ultimately determined" by the dividend-minus-interest component even though that component is small day to day.
- The argument that `f` tracks `p` "does not quite have the same force as a no-arbitrage condition": over any finite holding period the terminal futures price may differ from the cash price, so the perpetual "might track" the cash price less well than dated futures do.
- Footnote 12: an exchange could announce `r` above the market rate, which would shorten the effective maturity of the contract. This is the idea behind a funding coefficient that sets anchoring strength.
- A single non-expiring contract concentrates liquidity instead of splitting it across maturities.

## Signal construction
Not a signal. It is the conceptual source for reading funding as "dividend minus financing cost" and for expecting the perp premium to be a bounded but not pinned quantity.

## Relevance to SOL perpetuals at minutes to hours
Crypto perps have no dividend index. Exchanges replaced `d - r*f` with a function of the perp-minus-index premium, so the Shiller cash-flow identity survives only in form. What transfers is the warning that convergence is not guaranteed at any date: a premium on the Kalshi SOL perp can persist, and the size of the funding coefficient (and the 8-hour interval) governs how fast it should decay. See [He et al.](he-2022-fundamentals-perpetual-futures.md) and [Ackerer et al.](ackerer-2023-perpetual-futures-pricing.md) for the formal versions.

## Caveats
Theory and proposal only; the grade reflects a peer-reviewed argument, not trading evidence. The copy read is the 1992 working paper (a scan read page by page for sections II.A to II.D); wording may differ in the journal version, which was not opened.
