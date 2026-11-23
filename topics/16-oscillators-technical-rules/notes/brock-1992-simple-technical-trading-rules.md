---
title: "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns"
authors: "Brock, William; Lakonishok, Josef; LeBaron, Blake"
year: 1992
venue: "Journal of Finance 47(5), 1731-1764"
url: "https://ideas.repec.org/a/bla/jfinan/v47y1992i5p1731-64.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "equities"
horizon: "daily"
tags: "moving-average, trading-range-breakout, bootstrap, foundational, buy-sell-asymmetry"
---

## Key insight
This is the paper that reopened the academic case for technical analysis. Two of the simplest rule families, moving-average crossovers and trading-range breakouts, produced returns on the Dow Jones index that four standard null models of returns could not reproduce. It also set the template (the "BLL rules" and the model-based bootstrap) that almost every later study, including the crypto ones in this folder, copies.

## Method
Only the abstract was read. It states that two rule families (moving average and trading range break) are tested and that inference uses bootstrap techniques: returns conditional on buy and sell signals are compared with those simulated from four null models (random walk, AR(1), GARCH-M, exponential GARCH). Details of the 26 parameterizations are known in this repository only through Sullivan, Timmermann and White, who replicate them (see `sullivan-1999-data-snooping-technical-trading-bootstrap.md`).

## Data and sample
Dow Jones index, daily, 1897 to 1986 (per the abstract).

## Reported results
From the abstract only:
- The results give strong support to the technical strategies.
- Returns from the strategies are not consistent with any of the four null models.
- Buy signals consistently generate higher returns than sell signals.
- Returns following buy signals are less volatile than returns following sell signals.
- Returns following sell signals are negative, which the authors say is not easily explained by existing equilibrium models.

No transaction-cost figures appear in the abstract. Allen and Karjalainen's working paper (noted separately) describes the BLL excess returns as "before transaction costs".

## Signal construction
The two rule families, in the form later papers use them:
- Variable-length moving average: long when the short MA (for example 1, 2 or 5 periods) is above the long MA (50, 150 or 200 periods), optionally by a 1% band; short or flat otherwise.
- Trading range breakout: long when price exceeds the maximum of the previous n periods, short when it falls below the minimum.
Parameters and the band are from the descriptions in the later papers I read, not from this paper's text.

## Relevance to SOL perpetuals at minutes to hours
The lasting value is the test design, not the parameters: compare the conditional distribution of returns after a signal with the unconditional one, and with what a volatility model alone would generate. For a SOL perp bot the same check applies at 5-minute or hourly bars, where volatility clustering is much stronger than in daily Dow data and can easily masquerade as rule skill. The buy/sell asymmetry (profits concentrated on the long side) recurs in the crypto studies (Hudson and Urquhart, Corbet et al.), which matters because a perp bot can go short as cheaply as long.

## Caveats
Abstract-only. The headline result did not survive in the ten years after the sample ended (Sullivan et al.), and Bajgrowicz and Scaillet argue it never had economic value after costs. Daily equity-index data with non-synchronous trading effects is a poor proxy for a 24/7 perpetual. The rules were chosen because they were popular, which is itself a form of selection.
