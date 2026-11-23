---
title: "US Futures Fees"
authors: "Kraken Derivatives US (NinjaTrader Clearing, LLC)"
year: 2026
venue: "Kraken Support article, last updated October 30, 2026"
url: "https://support.kraken.com/articles/us-futures-fees"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "fees, bitnomial, kraken, us-regulated-perps, transaction-costs, competing-venues"
---

## Key insight
A US customer can trade Bitnomial-listed perpetual futures through Kraken Derivatives US for a flat fee per contract per side, with no maker and taker split and no volume tiers. Nearly all of that fee is a fixed regulatory charge per contract, so the cost as a share of notional depends entirely on the contract unit, which the page does not state. This is the only confirmed fee figure in the repository for a regulated US perpetual other than Kalshi's.

## Method
A broker support page, read as page text on 2026-11-23. It lists the fee components for CME-listed futures and, in a separate section, for Bitnomial-listed perpetual futures.

## Data and sample
Fees in force on the page's "Last updated: October 30, 2026" date. The page covers all Bitnomial-listed perpetuals as one group and does not name SOL.

## Reported results
- "Kraken Derivatives US charges a flat per-contract fee for perpetual futures. All-in rate: $0.0113/contract per side".
- Components: commission $0.0003 per contract, exchange and clearing fee $0.001 per contract, NFA fee $0.01 per contract.
- "All rates quoted on Kraken's website are per contract and per side"; a round turn is double.
- No maker or taker distinction, no volume tiers and no promotional rates are stated for perpetuals.
- Funding is described separately as a periodic payment between longs and shorts, "aggregated and settled as a single cash adjustment at 3:00 pm CT daily", and "not a per-trade fee".
- Exchange, NFA and clearing fees are "subject to change"; the clearing fee is set by the futures commission merchant and can differ between brokers.
- The page directs users to the order form's estimated-fee field for the fee on a specific trade.

## Signal construction
Not a signal. It is a transaction-cost input for comparing venues. Fee per side as a share of notional is `0.0113 / (contract_unit_in_SOL * SOL_price)`. If the charged unit is the 0.1 SOL minimum size in [the Bitnomial filing](bitnomial-2026-solana-deci-perpetual-futures-filing.md), that is 11.3 bp at a SOL price of $100 and 5.65 bp at $200 (my arithmetic, illustrative prices). If the charged unit is the filing's 1,000 SOL contract, the fee is negligible. The unit must be confirmed on the order form before this venue is costed.

## Relevance to SOL perpetuals at minutes to hours
It gives one comparison point for Kalshi's 12 bp taker and 2 bp maker entry-tier fees ([fee schedule](kalshiex-2026-perpetuals-fee-schedule-amendment.md)). Because the fee is the same for resting and crossing orders, a passive-only plan gains nothing in fees here, whereas on Kalshi it saves 10 bp per leg. Under the 0.1 SOL reading the flat fee sits between Kalshi's maker and taker rates, so this venue would suit a strategy that must cross the spread and Kalshi would suit one that can rest. Nothing here speaks to Bitnomial's spread, depth or leverage, which matter as much as the fee.

## Caveats
The contract unit behind "per contract" is not stated, and the Bitnomial filing gives both a 1,000 SOL contract and a 0.1 SOL minimum size, so the fee in basis points is unconfirmed. The page does not mention SOL by name. A broker support page can change without notice and is not a rule filing. Bitnomial's own exchange fee schedule and the fees charged by other brokers were not opened. Funding here settles daily in cash, which differs from the 8-hour schedule on Bitnomial's methodology page as summarised in the Bitnomial note; the two were not reconciled.
