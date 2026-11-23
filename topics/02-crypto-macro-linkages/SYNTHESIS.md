# Topic 02: Crypto links to macro variables, liquidity and announcements

Sixteen source notes: fourteen read in full (three of those are journal articles read in their working-paper or accepted-preprint versions), one from its abstract only, and one through a news report. Web search was cut off partway through the session by a shared budget limit, so coverage of 2025 and 2026 work, and of machine-learning and reinforcement-learning studies in particular, is thinner than intended. Gaps are listed at the end of the second section.

## What the literature agrees on

1. **The macro link is a post-2020 feature, not a constant.** Through 2018, crypto returns had no significant exposure to equity factors beyond a CAPM beta, to currencies, metals or macro factors ([Liu and Tsyvinski](notes/liu-2021-risks-returns-cryptocurrency.md)). In data through September 2025 the weekly correlation of the coin market with global equities is 1 percent before 2020 and 39 percent after ([Borri et al.](notes/borri-2026-cryptocurrency-investable-asset-class.md)). Intraday, Bitcoin was statistically unresponsive to almost all US macro surprises in 2017 to 2022 ([Benigno and Rosa](notes/benigno-2023-bitcoin-macro-disconnect.md)), while a 2026 Federal Reserve staff study, known here only second-hand, reports strong and fast responses after 2021 ([Kroner et al.](notes/kroner-2026-cryptocurrencies-price-economic-news.md)).

2. **When crypto does respond, it responds as a high-beta risk asset.** Hot inflation and tightening surprises push prices down: Bitcoin falls about 24 basis points per standard deviation of inflation surprise in 2013 to 2021 ([Pinchuk](notes/pinchuk-2023-bitcoin-not-hedge-inflation.md)); the crypto factor falls 0.41 standard deviations per percentage point of Fed surprise in 2018 to 2026 ([Copestake et al.](notes/copestake-2026-crypto-cycle-institutional-investors.md)); BTC and ETH fall on unexpected fed funds increases by about as much as the Nasdaq ([Kyriazis et al.](notes/kyriazis-2023-monetary-policy-digital-assets-defi.md)). No study in this folder finds crypto acting as an inflation hedge in announcement windows.

3. **Volatility around scheduled events is the most robust effect.** Five-minute volatility is elevated around FOMC and ECB announcements ([Karau](notes/karau-2021-monetary-policy-bitcoin.md)), at least doubles for DeFi collateral tokens at the FOMC statement and again at the press conference, more for altcoins than Bitcoin ([Kyriazis et al.](notes/kyriazis-2023-monetary-policy-digital-assets-defi.md)), and by one peer-reviewed account begins before the release ([Ben Omrane et al.](notes/benomrane-2025-crypto-volatility-intraday-macro-news.md), abstract only). Direction is far less reliable than volatility.

4. **One common factor dominates.** A single crypto factor explains 67 percent of the price variance of seven major coins ([Copestake et al.](notes/copestake-2026-crypto-cycle-institutional-investors.md)); cross-sectionally, market, size and momentum span returns ([Liu, Tsyvinski and Wu](notes/liu-2022-common-risk-factors-cryptocurrency.md)), and size and momentum remain robust in later data ([Borri et al.](notes/borri-2026-cryptocurrency-investable-asset-class.md)). For a SOL bot this means BTC and ETH on the large venues are the first-order input and SOL-specific signals belong on residuals.

5. **US policy is what matters; stablecoin supply follows.** Comparable ECB and Bank of England surprises produce no negative response of the crypto factor ([Copestake et al.](notes/copestake-2026-crypto-cycle-institutional-investors.md)). Stablecoin capitalization falls over about three months after a Fed tightening shock and after negative crypto shocks; it is an outcome of monetary conditions and crypto prices ([Aldasoro et al.](notes/aldasoro-2024-stablecoins-mmf-monetary-policy.md)).

6. **Machine learning has not rescued macro features.** A LightGBM volatility model finds macro-financial inputs negligible next to volume, lagged variance and search interest ([Dudek et al.](notes/dudek-2025-bitcoin-volatility-gradient-boosting.md)). An LSTM with 18 macro inputs and an LLM-built hawk-dove index is not significantly better than ARIMA out of sample ([Nicolas et al.](notes/nicolas-2026-bitcoin-monetary-policy-expectations-llm.md)). A Bayesian-network feature selector in an RL trading system chose macro-financial series for one coin in five ([Amirzadeh et al.](notes/amirzadeh-2023-causal-reinforcement-learning-crypto-trading.md)).

## Where it disagrees or is weak

- **Sign of the Fed effect.** Karau's 2013 to 2021 proxy VAR has Bitcoin rising after a US tightening; every later study here has it falling. A later ECB paper cites a 2023 journal version of Karau as showing a fall. That version was not opened. Treat the early positive sign as a sample artifact of the pre-institutional, China-heavy period until shown otherwise.
- **Is there an intraday response at all?** Benigno and Rosa say no (except CPI, and not robustly); Pinchuk says yes for inflation only; Kroner et al. reportedly say yes after 2021 for CPI, payrolls and FOMC. The reconciliation by sample period is plausible but rests on a paper this repository has not read. Bitcoin's five-minute volatility of about 0.4 percent means effects of 20 to 60 basis points per standard deviation are hard to detect with 50 to 100 events.
- **Sign of real-economy news.** Pre-2020 daily evidence has Bitcoin falling on good labor-market news coverage ([Corbet et al.](notes/corbet-2020-macroeconomic-news-bitcoin-returns.md)); the payrolls response is reported to have flipped sign around 2020. Rules of the form "good data is bullish" are regime-dependent.
- **Why the link appeared.** Institutional participation and leverage ([Copestake et al.](notes/copestake-2026-crypto-cycle-institutional-investors.md)) is the best-developed explanation, but Borri et al. state the literature has not reached consensus, and the institutional-share proxy trends with price.
- **Altcoins.** Evidence beyond BTC and ETH is thin and mixed: Pinchuk finds no response in ETH, LTC or ADA through 2021; Kyriazis finds larger volatility responses in altcoins; ETH reportedly responds about 1.5 times as much as BTC post-2021. No study here tests SOL.
- **Liquidity and halving cycles.** The claim that M2 leads Bitcoin with a fixed lag fails a sign-stability test across cycles in the one paper that tests it, and the halving-timing evidence rests on three tops ([Molnar](notes/molnar-2026-bitcoin-halving-clock.md)). A separate synthetic-control study (Virtonen 2025, arXiv 2511.05512, opened but not noted) finds a positive effect for the 2024 halving and none for 2020. There is no serious test of a properly constructed global liquidity series.
- **Daily versus intraday.** Much of the monetary-policy evidence (Copestake, Aldasoro, Karau's VAR, Kyriazis's regressions) is daily or weekly. It establishes regime context, not tradable intraday signals.

Gaps from the search cutoff and access limits: the Kroner, Mohammed and Vega paper itself (SSRN blocked); Che et al., IMF WP 23/163 and Iyer's IMF spillover notes (IMF PDF downloads blocked; Iyer and Popescu WP 23/213 was seen only as a machine summary: daily Diebold-Yilmaz connectedness with equities the strongest cross-asset link); Pyo and Lee (2020) on FOMC days; Karau's journal version; real-yield and dollar-index sensitivity studies; BTC dominance as a regime variable; pre-FOMC drift in crypto; any reinforcement-learning or evolutionary-algorithm study that uses macro announcements or macro state intraday. MacroHFT (Zong et al., KDD 2024, arXiv 2406.14537) was opened and uses "macro" to mean market trend and volatility context, not macroeconomics; it belongs with the RL and regime topics.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Scheduled-event volatility state | FOMC, CPI, payrolls calendar; flag from before release to about 90 minutes after FOMC statement, with peaks at 14:00 and 14:30 ET | minutes to hours | B | [karau](notes/karau-2021-monetary-policy-bitcoin.md), [kyriazis](notes/kyriazis-2023-monetary-policy-digital-assets-defi.md), [benomrane](notes/benomrane-2025-crypto-volatility-intraday-macro-news.md) |
| CPI surprise direction | z = (actual minus consensus) / historical sd; expected BTC move roughly -0.25 to -0.65 percent per sd over 30 minutes depending on sample | minutes | B (unstable across samples) | [pinchuk](notes/pinchuk-2023-bitcoin-not-hedge-inflation.md), [benigno](notes/benigno-2023-bitcoin-macro-disconnect.md), [kroner](notes/kroner-2026-cryptocurrencies-price-economic-news.md) |
| Equity-futures proxy for macro surprise | S&P 500 or Nasdaq futures move in the first seconds after a release, as the surprise sign and size | minutes | C (inferred from reported 0.88 response correlation; not tested as a signal) | [kroner](notes/kroner-2026-cryptocurrencies-price-economic-news.md), [borri](notes/borri-2026-cryptocurrency-investable-asset-class.md) |
| Macro-sensitivity regime from funding | 3-day mean of annualized Binance BTC-USDT funding, standardized around median, logistic with gamma 1.5; high state means larger response to Fed news | daily state, applied intraday | B | [copestake](notes/copestake-2026-crypto-cycle-institutional-investors.md) |
| Institutional-participation regime | 30-day mean of large-transfer share or an ETF/CME proxy | daily | B | [copestake](notes/copestake-2026-crypto-cycle-institutional-investors.md) |
| Rolling crypto-equity correlation | crypto market return versus equity index, rolling window | daily to multi-day | B | [borri](notes/borri-2026-cryptocurrency-investable-asset-class.md), [copestake](notes/copestake-2026-crypto-cycle-institutional-investors.md) |
| Macro versus crypto-native decomposition | residual of crypto index return regressed (elastic net) on equity, rates, dollar, gold, oil, VIX | multi-day in source; adaptable intraday | B | [aldasoro](notes/aldasoro-2024-stablecoins-mmf-monetary-policy.md) |
| Stablecoin supply growth | 4- to 13-week log change in USDT plus USDC capitalization, as lagging liquidity regime | multi-day | B (as regime descriptor; no evidence as a lead) | [aldasoro](notes/aldasoro-2024-stablecoins-mmf-monetary-policy.md) |
| Crypto market factor and residual | value-weighted market return; SOL return minus beta times market | any | A | [liu-2022](notes/liu-2022-common-risk-factors-cryptocurrency.md), [copestake](notes/copestake-2026-crypto-cycle-institutional-investors.md) |
| Time-series and cross-sectional momentum | prior day or 1- to 4-week return; rank among large caps | daily to multi-day | A (weekly; untested intraday) | [liu-2021](notes/liu-2021-risks-returns-cryptocurrency.md), [liu-2022](notes/liu-2022-common-risk-factors-cryptocurrency.md) |
| LLM hawk-dove index | policy-tagged text classified on a five-point scale, engagement-weighted | multi-day in source | B (small, mostly insignificant gains) | [nicolas](notes/nicolas-2026-bitcoin-monetary-policy-expectations-llm.md) |
| Feature-group selection before RL | selector allowed to reject macro inputs; probability forecast fed into agent state | daily | C | [amirzadeh](notes/amirzadeh-2023-causal-reinforcement-learning-crypto-trading.md) |
| Crypto-native volatility forecast | lagged realized variance, volume change, search interest; macro levels omitted | daily | B | [dudek](notes/dudek-2025-bitcoin-volatility-gradient-boosting.md) |
| Halving phase | days since halving | multi-day | C | [molnar](notes/molnar-2026-bitcoin-halving-clock.md) |
| Lagged M2 lead (negative result) | US M2 growth shifted 10 weeks | multi-day | C (evidence against) | [molnar](notes/molnar-2026-bitcoin-halving-clock.md) |

## Open questions worth testing on SOL perps

1. Replicate the 30-minute surprise regressions for SOL, BTC and ETH on 2021 to 2026 data, year by year, for CPI, payrolls and FOMC. Does SOL's coefficient exceed ETH's, and is it stable?
2. How long does the adjustment take on SOL? The reported 15 to 30 minutes for BTC and ETH implies room for a non-colocated bot; measure the cumulative response at 10 seconds, 1, 5, 15 and 30 minutes after release, net of spread.
3. Does conditioning on the funding regime (Binance BTC funding, or SOL funding) change the size of the announcement response, as the daily evidence implies?
4. Volatility multiple by event and by minute for SOL: when does it start rising before a release, and how do spreads on Kalshi behave relative to Binance in that window?
5. Does the first-seconds move in equity-index futures predict the subsequent 5- to 30-minute SOL move after a release better than the numeric surprise does?
6. On non-announcement days, how much of SOL's hourly variance is explained by equity futures, rates and the dollar during US hours versus Asian hours? This sets how much weight macro inputs deserve outside events.
7. After removing the BTC and ETH component, is there any macro sensitivity left in SOL's residual?
8. Does Kalshi's 8-hour funding carry the same leverage information as Binance funding, given low maximum leverage and a different participant base?
9. Ablation for any ML or RL policy: train with and without macro features and event flags, walk-forward, and keep macro inputs only if they survive.
10. Check the outcome of the halving-clock bottom window (5 October to 16 November 2026) before assigning any weight to cycle-phase features.

## Reading order

1. [Borri, Liu, Tsyvinski and Wu 2026](notes/borri-2026-cryptocurrency-investable-asset-class.md): current stylized facts, including the post-2020 equity link.
2. [Liu and Tsyvinski 2021](notes/liu-2021-risks-returns-cryptocurrency.md): the pre-2020 baseline of no macro exposure.
3. [Benigno and Rosa 2023](notes/benigno-2023-bitcoin-macro-disconnect.md): the intraday event-study template and the null result.
4. [Pinchuk 2023](notes/pinchuk-2023-bitcoin-not-hedge-inflation.md): the inflation-surprise response with one-minute data.
5. [Kroner, Mohammed and Vega 2026](notes/kroner-2026-cryptocurrencies-price-economic-news.md): second-hand, then obtain and read the paper itself.
6. [Copestake, Furceri and Terracciano 2026](notes/copestake-2026-crypto-cycle-institutional-investors.md): state dependence on institutional share and funding.
7. [Kyriazis et al. 2023](notes/kyriazis-2023-monetary-policy-digital-assets-defi.md) and [Ben Omrane et al. 2025](notes/benomrane-2025-crypto-volatility-intraday-macro-news.md): intraday volatility around FOMC and macro news.
8. [Karau 2021](notes/karau-2021-monetary-policy-bitcoin.md): announcement volatility and the contested sign of the Fed effect.
9. [Aldasoro et al. 2024](notes/aldasoro-2024-stablecoins-mmf-monetary-policy.md): stablecoin supply as an outcome of monetary policy.
10. [Liu, Tsyvinski and Wu 2022](notes/liu-2022-common-risk-factors-cryptocurrency.md): factor structure.
11. [Dudek et al. 2025](notes/dudek-2025-bitcoin-volatility-gradient-boosting.md), [Nicolas et al. 2026](notes/nicolas-2026-bitcoin-monetary-policy-expectations-llm.md), [Amirzadeh et al. 2023](notes/amirzadeh-2023-causal-reinforcement-learning-crypto-trading.md): what machine learning and RL add with macro inputs.
12. [Corbet et al. 2020](notes/corbet-2020-macroeconomic-news-bitcoin-returns.md): pre-2020 daily news evidence, for the sign-instability point.
13. [Molnar 2026](notes/molnar-2026-bitcoin-halving-clock.md): halving-cycle claim and the M2 negative result.
