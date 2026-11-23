---
title: "Crypto Fear & Greed Index: methodology and API"
authors: "Alternative.me"
year: 2026
venue: "alternative.me (index provider web page, fetched 2026-11-22)"
url: "https://alternative.me/crypto/fear-and-greed-index/"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "daily"
tags: "fear-and-greed-index, composite-sentiment, volatility, momentum, social-media, dominance, google-trends, contrarian"
---

## Key insight
The most widely quoted crypto sentiment gauge is a daily 0 to 100 composite for Bitcoin only, and half of its weight is price-derived: volatility (25%) and momentum/volume (25%). The remainder is social media activity, surveys (currently paused), Bitcoin dominance and Google Trends. The provider frames it as contrarian (extreme fear as a possible buying opportunity, extreme greed as a sign of a coming correction) but publishes no test. A bot that already has volatility and momentum features gains little new information from the index level.

## Method
Components and weights as described on the page:
- Volatility, 25%: current volatility and maximum drawdown compared with 30-day and 90-day averages. Unusual rises in volatility are read as fear.
- Market momentum and volume, 25%: current volume and momentum compared with 30-day and 90-day averages. High buying volume in a positive market is read as greed.
- Social media, 15%: counts of posts on hashtags and their interaction rates on Twitter; unusually high interaction is read as greed. Reddit analysis is described as not in the live index.
- Surveys, 15%: weekly polls via a polling platform; currently paused.
- Dominance, 10%: Bitcoin's share of total crypto market capitalization. Rising dominance is read as fear (flight to Bitcoin), falling dominance as greed (altcoin speculation).
- Trends, 10%: Google Trends changes for Bitcoin-related queries.
The exact formulas, normalization and how the paused survey weight is redistributed are not disclosed.

## Data and sample
Bitcoin only; the page says separate indices for large altcoins are planned. Updated once per day. Scale 0 (extreme fear) to 100 (extreme greed). API: `GET https://api.alternative.me/fng/` with `limit` (0 returns all history), `format` (json or csv) and `date_format`; the response includes `time_until_update` when `limit=1`.

## Reported results
None. The page offers interpretation only and states the index is not investment advice.

## Signal construction
Inputs: daily index value `F_t` from the API. Options, all untested in sources read for this topic:
- Level extremes: `F_t <= 20` or `F_t >= 80` as regime flags.
- Residual sentiment: regress `F_t` on the bot's own realized-volatility and momentum features and keep the residual, which isolates the social, dominance and search components.
- Change: `F_t - F_{t-7}`.
Because the value changes once a day at a time visible only through `time_until_update`, align it to the first bar after publication to avoid look-ahead.

## Relevance to SOL perpetuals at minutes to hours
Limited. It is daily, Bitcoin-specific and half price-derived. Its plausible role is a slow conditioning variable (for example, whether SOL reversal signals behave differently in extreme-fear regimes). The dominance component is directionally interesting for SOL, since falling Bitcoin dominance coincides with altcoin risk appetite, but dominance can be computed directly and intraday.

## Caveats
Opaque construction, undocumented revisions, and a paused component. The contrarian interpretation is the provider's claim; because half of the index mechanically rises with price and volume, extreme readings coincide with strong trends, and fading them amounts in part to fading momentum; that should be checked against the momentum evidence in topic 13 before use. Academic tests of this index exist but could not be retrieved in this session (search budget exhausted), so this note records the definition only.
