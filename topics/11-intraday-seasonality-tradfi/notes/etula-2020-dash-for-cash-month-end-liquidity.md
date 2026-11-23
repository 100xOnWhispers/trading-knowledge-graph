---
title: "Dash for Cash: Monthly Market Impact of Institutional Liquidity Needs"
authors: "Etula, Erkko; Rinne, Kalle; Suominen, Matti; Vaittinen, Lauri"
year: 2020
venue: "Review of Financial Studies 33(1), 75-111"
url: "https://acris.aalto.fi/ws/portalfiles/portal/40965155/hhz054.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/etula-2020-dash-for-cash-month-end-liquidity.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "multi"
horizon: "multi-day"
tags: "turn-of-month, liquidity-needs, settlement, price-pressure, reversal, payment-cycle, calendar-effects"
---

## Key insight
The turn-of-the-month effect has a mechanism. Pensions, dividends and salaries are paid around month-end, so institutions must sell securities early enough for cash to settle in time. This creates selling pressure roughly eight to four business days before month-end and a predictable positive reversal in the last three days, followed by buying pressure in the first three days of the new month. The timing lines up with each market's settlement convention, which is what distinguishes the result from a mined calendar pattern.

## Method
Average and cumulative daily returns of the CRSP value-weighted index by day relative to the last trading day of the month (T), with windows T-8 to T-4 (selling pressure), T-3 to T-1 (positive reversal), T+1 to T+3 (buying pressure) and T+4 to T+8 (negative reversal). Parallel analysis of repo, Libor and federal funds rates, Treasury and corporate bond yields. Identification comes from differences in settlement conventions across markets (three days for US equities in the sample, one day for Treasuries), a European settlement-rule change used as a quasi-experiment, months whose last business day is a Friday (pension and weekly salary payments coincide), and trade-level data identifying institutions that demand month-end liquidity. Only the first sections were read in detail.

## Data and sample
US equities mainly July 1995 (start of three-day settlement) to December 2013, with cumulative-return evidence from January 1980; US money-market rates and bonds; 23 international equity markets.

## Reported results
- 2003 to 2013: cumulative excess return over the positive-reversal days was 103%, or 73% of the US equity market's total excess return; over the selling-pressure days it was -31%.
- The correlation between T-8 to T-4 returns and T-3 to T-1 returns was -0.54.
- Equity yields peak around T-4 and Treasury yields stay elevated until T-2, matching settlement lags.
- All 23 equity markets show some pre-month-end reversal; it is statistically significant in 20. The three exceptions (Finland, New Zealand, Sweden) make substantial pension payments away from month-end.
- Reversals are two to three times larger when the month's last trading day is a Friday.
- The patterns became more pronounced over time within the sample.

## Signal construction
Daily state variable d = business days to month-end. Bias: short or underweight for d in [8, 4], long for d in [3, 1] and the first three days of the month, with size proportional to minus the realized T-8 to T-4 return (the reversal is conditional on prior pressure). Scale up when month-end falls on a Friday.

## Relevance to SOL perpetuals at minutes to hours
This is a multi-day effect driven by payment calendars and settlement lags that do not exist in crypto, so it does not transfer as a SOL signal. It matters in two ways. First, as an input from equities: if US equity index futures carry a month-end bias and SOL co-moves with them intraday, the bot's risk-asset bias should be aware of the calendar. Second, as a template: crypto has its own dated cash needs (monthly and quarterly option and futures expiries, ETF rebalancing dates, token unlock schedules, tax dates) where forced selling followed by reversal can be tested with the same design.

## Caveats
Sample ends 2013; US equity settlement has since shortened to two days and then one day, which should shift the timing. Horizon is days, beyond the bot's holding period. Authors include practitioners at financial firms. No evidence in the paper on crypto or on intraday timing.
