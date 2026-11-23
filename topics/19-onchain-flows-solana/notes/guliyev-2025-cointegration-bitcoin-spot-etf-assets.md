---
title: "From Flows to Value: Cointegration Between Bitcoin Spot ETF Assets and Bitcoin Price"
authors: "Guliyev, Taghi; Ahmadova, Aysu"
year: 2025
venue: "Ledger, 10, 154-172"
url: "https://ledger.pitt.edu/ojs/ledger/article/view/393"
pdf: "sources/19-onchain-flows-solana/guliyev-2025-cointegration-bitcoin-spot-etf-assets.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "multi-day"
tags: "spot-etf, etf-flows, cointegration, fmols, dols, bitcoin, net-assets"
---

## Key insight
The log of total net assets of US spot Bitcoin ETFs and the log Bitcoin price share a long-run relationship, with an estimated elasticity of about 1.3. The authors read this as ETF demand having a lasting influence on price. The evidence is much weaker than that reading: the regressor contains the price mechanically, cointegration is found only at the 10 percent level, and nothing in the design speaks to short-horizon returns.

## Method
- Unit-root tests on both series in levels and first differences.
- Engle-Granger and Phillips-Ouliaris residual-based cointegration tests.
- Long-run coefficient estimated three ways: Fully Modified OLS, Dynamic OLS and Canonical Cointegrating Regression, in log-log form with the Bitcoin price as the dependent variable and ETF net assets as the regressor.

## Data and sample
Daily, 11 January 2024 to 16 May 2025, 352 trading-day observations. Bitcoin price from investing.com; total net assets of spot Bitcoin ETFs in USD millions.

## Reported results
- Both series are non-stationary in levels and stationary in first differences.
- Cointegration is supported only at the 10 percent significance level; the authors attribute this to the short sample.
- Long-run elasticity of Bitcoin price to ETF net assets: about 1.32 with FMOLS, and 1.28 to 1.35 across the three estimators, all significant.
- The authors acknowledge that a rising Bitcoin price mechanically raises the dollar value of ETF holdings and that rallies attract momentum inflows, so causality "can be bidirectional to some extent", but argue that net inflows are the long-run driver.

## Signal construction
Not a usable signal as specified. Net assets equal coins held times price, so regressing price on net assets is close to regressing price on itself. A bot wanting an ETF flow feature should instead use:
- Daily net creations or redemptions in coins or in USD at the prior NAV (issuer disclosures or a flow aggregator), which strip out the price effect.
- Scaled by trailing average daily spot volume, published after the US close.
- For intraday use, ETF share volume and premium or discount to indicative NAV during US hours as a proxy for the pending creation basket.

## Relevance to SOL perpetuals at minutes to hours
Low direct relevance. US spot SOL ETFs have traded only since October 2025 (per [blockworks-2026](blockworks-2026-solana-tokenholder-report-q2.md)), their flows are small next to SOL spot and perp volume, and creation data arrive once a day. The paper is included because it is typical of the ETF-flow literature and shows why most of that literature cannot be used at this horizon. The contrary evidence in [oefele-2025](oefele-2025-one-year-bitcoin-spot-etps-fund-flows.md), that price changes drive flows, is the more plausible baseline.

## Caveats
Mechanical correlation between regressor and dependent variable. Sixteen months of mostly rising prices. Weak cointegration evidence. No flow-based (as opposed to asset-level) specification, no Granger or lead-lag test reported in the sections read, no out-of-sample test. Levels regressions in trending series overstate fit.
