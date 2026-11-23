---
title: "No Place to Hide: An Analysis on Protected Order Flow Sandwich Attacks"
authors: "Heimbach, Lioba; Solmaz, Ozan; Oz, Burak; Ferreira Torres, Christof"
year: 2026
venue: "arXiv preprint arXiv:2609.28115"
url: "https://arxiv.org/pdf/2609.28115"
pdf: "sources/19-onchain-flows-solana/heimbach-2026-protected-order-flow-sandwich-attacks.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "n/a"
tags: "solana, mev, sandwich, jito, validators, dex, execution-quality, measurement"
---

## Key insight
A three-year, six-chain measurement finds that Solana carries almost all sandwich attacks against supposedly protected order flow: 28.0 million attacks by 8,631 bots, against tens of thousands on Ethereum and Tron. Interventions that removed stake from offending validators changed the form of the attacks (from same-block to cross-block) but not their daily count. Solana DEX prints therefore contain a persistent layer of predatory, non-directional volume.

## Method
Detection heuristics that capture "wide" sandwiches, within and across blocks, with filters on bot behaviour to separate attacks from ordinary trading. A "tight" sandwich has the two attacker legs immediately around the victim. An attack is "interfered" when another swap in the pool lands between the legs. For Solana the analysis is organised by eras bounded by interventions: the Jito public mempool (until March 2024), the Solana Foundation removing validators from its delegation programme (June 2024), Marinade blocklisting validators (February 2025) and the JitoSOL pool delisting more validators (October 2025). The share of attacks landing in slots of over-represented leaders is used to measure validator-level exposure.

## Data and sample
Ethereum, Solana, Tron, Base, Arbitrum and Monad, 1 July 2023 to 30 June 2026. Solana venues include Meteora and the Pump.fun AMM among others. Only the abstract, summary sections and the Solana passages were read.

## Reported results
- Solana: 28.0 million sandwiches, 8,631 bots, USD 383.4 million gross profit and USD 345.2 million after fees (fees take 10.0 percent).
- Other chains: 38,567 attacks on Tron, 30,607 on Ethereum (7 bots), 1,889 on Base; none persistent on Arbitrum or Monad.
- Solana averages 25,586 attacks per day, peaking at 125,169 just before Jito shut its mempool; about 41,063 per day until January 2025, 26,127 per day through 2025 and 20,663 after the October 2025 delistings.
- Share of attacks in slots led by over-represented validators fell from 50 percent in the Jito-mempool era to 2 percent in the final era, while daily volume did not fall in step.
- Tight sandwiches were 54 to 87 percent of attacks before the delistings, 18 percent in the Marinade era and 1 percent after the JitoSOL delisting; 96 percent of attacks now span blocks.
- 44.6 percent of Solana attacks have another swap between the legs. 88.0 percent of Solana attacks are profitable.

## Signal construction
Not a signal. Used for data hygiene and as a possible activity gauge:
- When building trade-flow or order-flow-imbalance features from Solana DEX swaps, pair and remove sandwich legs (same bot, same pool, opposite directions within a few slots), since the two legs net to zero and inflate both volume and apparent two-way flow.
- Cross-block attacks mean an attacker holds inventory for several slots; a filter limited to same-block patterns now misses nearly all of them.
- Daily or hourly attack counts could be tested as a proxy for retail swap activity, since attackers follow victims.

## Relevance to SOL perpetuals at minutes to hours
Matters for anyone using Solana DEX data as an input to a SOL perp model: raw swap volume overstates genuine demand, and signed-flow measures are polluted by attacker legs. It also quantifies an execution cost of trading SOL on-chain that does not exist on Kalshi or centralised venues, which is one reason price discovery for SOL stays on centralised exchanges. No link to SOL returns is tested.

## Caveats
Preprint, not yet peer-reviewed. Heuristic detection has false positives and negatives, and the wide-sandwich definition is more permissive than earlier work. Profit figures depend on token price sources. Authors are affiliated with firms active in this area (Category Labs, Flashbots). Only part of the paper was read.
