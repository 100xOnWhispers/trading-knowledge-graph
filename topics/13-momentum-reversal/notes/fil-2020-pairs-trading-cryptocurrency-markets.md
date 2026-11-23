---
title: "Pairs Trading in Cryptocurrency Markets"
authors: "Fil, Miroslav; Kristoufek, Ladislav"
year: 2020
venue: "IEEE Access 8, 172644-172651"
url: "https://api.openalex.org/works/doi:10.1109/ACCESS.2020.3024619"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "minutes"
tags: "pairs-trading, mean-reversion, cointegration, distance-method, binance, intraday"
---

## Key insight
Pairs trading on liquid Binance coins underperforms simple benchmarks overall, but performance depends heavily on frequency: the standard distance method loses slightly on daily bars and earns large paper returns on 5-minute bars. The authors report simple mean-reverting behaviour in intraday prices that is absent in daily data. Mean reversion in crypto is therefore an intraday phenomenon, and it is fragile to costs and execution assumptions.

## Method
Only the abstract was read, through the open metadata record for the article's DOI (the publisher page and PDF could not be retrieved). It describes applying the distance method and the cointegration method of pairs trading to a basket of coins at three bar sizes and back-testing against classical benchmarks, with sensitivity checks on parameters, transaction costs and execution windows. Formation and trading window lengths, thresholds and the cost level were not confirmed.

## Data and sample
26 liquid cryptocurrencies traded on Binance, at 5-minute, 1-hour and daily frequencies. Sample dates not confirmed from the abstract.

## Reported results
From the abstract only:
- In the back-tests, the strategies underperform classical benchmarks.
- Results are quite sensitive to parameter settings and to external factors such as transaction costs and execution windows.
- Higher frequency delivers significantly better performance: the daily distance method returns -0.07% a month, rising to 11.61% a month at 5-minute frequency.
- Intraday prices show simple mean-reverting behaviour that is missing in daily data.

## Signal construction
Distance method (standard form, not confirmed as the paper's exact specification): normalise two price series over a formation window, compute the spread, and open a convergence trade when the spread exceeds a multiple of its formation-period standard deviation. For a directional SOL bot the pairs spread becomes a relative-value tilt: z-score of log(SOL) minus beta times log(ETH or BTC) on 5-minute to 1-hour bars, fading large z.

## Relevance to SOL perpetuals at minutes to hours
Supports placing mean-reversion signals at the 5-minute to 1-hour end of the bot's horizon and trend signals at the daily end, the same horizon split found in the single-asset literature. The warning is equally important: the 11.61% monthly figure sits beside "underperform benchmarks" and "sensitive to transaction costs", which is the signature of an edge that lives inside the spread. Any SOL relative-value signal must be evaluated at executable prices with realistic fill delay.

## Caveats
Abstract-only. The headline 5-minute return is almost certainly before realistic costs for a taker, and 5-minute mean reversion in close prices is partly bid-ask bounce. Pairs results are for two-legged trades; a one-legged directional version carries the full market move. Data pre-date 2021 and the current perpetual market structure. The open-access PDF exists on IEEE Xplore and should be read before using any parameter.
