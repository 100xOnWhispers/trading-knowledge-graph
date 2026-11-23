---
title: "Crypto carry"
authors: "Schmeling, Maik; Schrimpf, Andreas; Todorov, Karamfil"
year: 2023
venue: "BIS Working Papers No 1087 (April 2023; a revised version is listed as CEPR Discussion Paper 20719, 2025)"
url: "https://www.bis.org/publications/working-paper-1087-crypto-carry"
pdf: "none"
access: "abstract-only"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "multi-day"
tags: "carry, basis, convenience-yield, crash-risk, retail-demand, limits-to-arbitrage"
---

## Key insight
The futures-minus-spot basis in BTC and ETH ("crypto carry") is large, volatile and mostly unexplained by interest differentials. The authors attribute it to a time-varying convenience yield created by smaller, trend-chasing investors who want leveraged upside, combined with scarce arbitrage capital. High carry predicts future price crashes.

## Method
Only the BIS landing page (focus, contribution, findings, abstract) and the RePEc abstract were read; the PDF could not be downloaded because the BIS site served a bot challenge. From those pages: carry is defined as the difference between futures and spot prices; the cash-and-carry trade is long spot and short futures; the paper relates carry to investor demand, arbitrage capital, liquidations and the price of crash insurance. Estimation details were not seen.

## Data and sample
Not stated on the pages read, beyond a focus on Bitcoin and Ether futures. [He et al.](he-2022-fundamentals-perpetual-futures.md) describe this paper as an analysis of fixed-maturity crypto futures carry, using the Koijen et al. definition of carry. Whether perpetual funding is analysed in the paper was not confirmed.

## Reported results
From the abstract and summary pages only:
- Carry can become very large: "up to 60% p.a." on the BIS page; the RePEc abstract says it sometimes exceeds 40% per annum. The two figures come from different versions of the abstract.
- Average annual carry is above 10% for Bitcoin and Ether, much larger than in equities, fixed income, currencies and commodities.
- Interest-rate differentials explain very little of the variation; convenience-yield fluctuations dominate.
- High carry predicts future price crashes, and rising carry coincides with a rise in the price of crash-risk insurance.
- Cash-and-carry is risky because of margin spikes and liquidations in drawdowns.
- Crypto futures show excess volatility relative to spot; there is some evidence of segmentation between crypto exchanges and traditional finance.

No coefficients, horizons or sample dates were available.

## Signal construction
From what was read: annualised basis of a dated future (CME or offshore quarterly) over spot, `carry = (F/S - 1) * 365/days_to_expiry`, tracked daily; flag high readings as elevated crash risk. The paper's exact construction and thresholds were not seen, so this is the generic definition and not the authors' specification.

## Relevance to SOL perpetuals at minutes to hours
The mechanism (leveraged retail longs pay a premium that arbitrage does not remove) is the same one behind positive perp funding, so carry is a slow-moving state variable for a faster bot: a regime flag for crash risk and long crowding. It is a daily to multi-day signal, measured on BTC and ETH. Its predictive content for SOL and for horizons of hours is untested in anything read here.

## Caveats
Abstract-only. Numbers differ between abstract versions. The full text should be read before any threshold is used; in particular the crash-prediction horizon and whether results survive after 2022, when [He et al.](he-2022-fundamentals-perpetual-futures.md) show spot-perp deviations compressing sharply.
