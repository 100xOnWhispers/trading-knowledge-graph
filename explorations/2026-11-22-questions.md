# A. The venue: the Kalshi SOL perpetual
How far behind Binance does a small or regulated venue's price move, and is that lag exploitable after fees?
How is the Kalshi perpetual's funding rate computed from the premium index, and when is it charged?
How is the CF Benchmarks real time index calculated from constituent exchange order books?
What do Kalshi's price bands, leverage limits and liquidation rules imply for a trading bot?
What spread, depth and one-minute volatility has been measured on the Kalshi SOL perpetual?
Do market makers on a small venue hedge on a larger venue, and how does that link the two order books?
How do maker rebates and fee tiers change which venue leads and which strategies are profitable?
What happens to a venue's quotes and data when the reference venue has an outage or a liquidation cascade?
Does a perpetual's premium to its index mean-revert, and at what speed?
Do prediction market prices for crypto price ranges contain information beyond spot and options?
# B. Passive execution
What determines the probability that a limit order at the best bid fills within a given time?
How does queue position change the post-fill return of a passive order?
When should a resting order be cancelled, and what signals predict an adverse fill?
How much does latency cost a trader who is not high-frequency?
How should a limit price offset be chosen as a function of time left, volatility and remaining size?
What fraction of crypto execution cost is exchange fee versus spread and impact?
Does order book imbalance predict the next price change, and can a taker profit from it after fees?
How should transaction costs be estimated from one's own fills?
Is the micro-price a better estimate of fair value than the mid?
Survival models for the time to fill of a limit order
How do spoofing and fleeting liquidity distort displayed depth, and how can a bot filter them?
Using a short-lived signal inside an execution schedule: optimal trading with signals
How do TWAP and other scheduled execution algorithms leave detectable footprints in the tape?
What is the expected price impact of a taker order as a function of its size, volume and volatility?
# C. Trade flow signals
Does signed taker flow predict returns beyond the bar in which it occurs?
Long memory of order flow sign and how prices stay unpredictable despite it
How does the price impact of a trade decay over time (propagator models)?
Does a move pushed by aggressive flow reverse more than a move that flow opposed?
Does average trade size or the number of trades carry information about volatility or direction?
Round-sized trades and trades at clock boundaries: telling algorithmic flow from manual flow
Does order flow in one asset or venue move prices in another (cross-impact)?
Is VPIN or flow toxicity a useful predictor of volatility or of liquidity withdrawal?
Does volume interacted with return predict continuation versus reversal?
What distinguishes informed order flow from uninformed or forced order flow in the data?
How do retail front-end traders differ from algorithmic traders in timing and performance?
Visible scheduled orders on Hyperliquid as known future flow
How much of contemporaneous price change does net order flow explain?
Multi-level order flow imbalance versus top-of-book imbalance: how much do deeper levels add?
Does a large resting order that absorbs repeated market orders predict the direction of price?
# D. Momentum, reversal and shocks
At what horizon does intraday reversal in crypto give way to momentum?
What follows a large one-hour or two-hour move in bitcoin: reversal size by shock size
Does the first half hour of a session predict the last half hour in crypto (intraday momentum)?
How do liquidation cascades unfold in time, and when does the rebound begin?
Does the perpetual overshoot spot during a crash, and how quickly does the gap close?
Is time-series momentum in crypto real at hourly to weekly horizons after costs?
Do support and resistance levels or round numbers cause bounces or cascades?
Stop-loss order clusters and price cascades
Does high volume make a return more or less likely to reverse?
Price jumps: what predicts them and what follows over the next hour?
Do residual returns of one coin against bitcoin and ether mean-revert?
Do end-of-day or end-of-session reversals exist?
# E. Volatility and distribution forecasting
Which model forecasts realised volatility best: HAR, GARCH, EWMA or machine learning?
How large is the time-of-day pattern in crypto volatility and how should returns be deseasonalised?
Forecasting the high-low range, or the probability of touching a price level within an hour
Do volatility spillovers run from Binance perpetuals to other venues, and with what lead?
Does option-implied volatility forecast realised volatility in crypto better than past volatility?
Quantile and probabilistic forecasts of crypto returns: methods and calibration
How should density forecasts from several models be combined and scored?
Realised semivariance, signed jumps and realised skewness as predictors of returns or volatility
What sampling frequency and estimator give a reliable realised variance under microstructure noise?
Does volume or trade count forecast volatility better than past volatility?
Volatility around scheduled macro announcements: how early does it rise and how long does it last?
Tail risk and liquidation probability of a leveraged position over a holding period
Rough volatility and long memory in crypto volatility
# F. Across venues and assets
Which market leads price discovery for a crypto asset: spot or perpetual, Binance or Coinbase?
Does bitcoin lead altcoins at one-minute or shorter horizons?
Do lagged returns of other coins predict a coin's next return (cross-predictability)?
How do equity index futures moves transmit to crypto within minutes?
Is the Coinbase premium or a US-hours price gap informative about subsequent returns?
How does the tether to dollar rate affect comparisons between USDT and USD venues?
What share of a coin's variance is the crypto market factor, and how stable is its beta?
Measuring lead-lag between asynchronous high-frequency series
Is overshooting mistaken for price leadership in information share measures?
Do Solana DEX prices or on-chain activity lead centralised exchange prices?
# G. Perpetual mechanics: funding, basis, open interest
Does the funding rate or premium predict the perpetual's return, and at what horizon?
What happens to liquidity, volume and volatility around funding settlement times?
Are funding rates predictable from their own history?
Does the change in open interest together with the price change distinguish new positioning from forced closing?
Is there any early warning variable for liquidation cascades?
How reliable are reported volume and open interest across crypto venues (wash trading, reconciliation)?
What are the no-arbitrage bounds on the perpetual basis, and what breaks them?
Is crypto carry from funding compensated by crash risk?
Exchange long/short ratios and top-trader positioning as contrarian indicators
Auto-deleveraging and insurance fund events: what do they do to prices?
# H. Clock and events
Why does volume spike at the top of the hour and at quarter-hours in crypto?
Do returns show any reliable hour-of-day or day-of-week pattern after correcting for data snooping?
How do benchmark fixings, option expiries and futures settlement windows move prices?
How do crypto prices respond to CPI, payrolls and FOMC surprises in the first 30 minutes?
Is there a price drift before scheduled announcements?
Weekend versus weekday liquidity and volatility in crypto
Does the return at one time of day repeat at the same time on following days?
How should time of day be encoded for a model: Fourier terms, dummies or learned embeddings?
Do dominant-cycle or spectral indicators add predictive value?
# I. Supervised learning
How accurate are machine learning models at predicting the sign of crypto returns at 5 to 60 minutes?
Do linear or shallow models beat deep networks for short-horizon return prediction?
Which input features matter most in crypto microstructure prediction models?
Do models pooled across many instruments transfer to a new instrument or venue?
How should labels be built: fixed horizon, triple barrier or cost-aware thresholds?
Meta-labelling: a second model that decides whether to take a primary signal's trade
How should a model be updated as the market drifts (incremental learning, refit frequency)?
Multi-horizon forecasting: does predicting several horizons jointly help?
Do deep order book models retain predictive power beyond a few seconds?
Stationarity, fractional differentiation and feature scaling for financial machine learning
Do pretrained time-series foundation models or language models forecast returns?
Does training on trading profit instead of forecast error change what a model learns?
Autoencoders and learned representations of market state
Overlapping labels: sample weights, purging and embargo
# J. Reinforcement learning and evolutionary search
What state, action and reward formulation works for an RL trading agent on perpetual futures?
In what settings does RL beat simple baselines for trade execution?
Why do RL trading agents fail out of sample, and how variable are results across random seeds?
Hierarchical or regime-conditioned RL policies for trading
Offline RL and decision transformers trained on logged market data
Risk-sensitive rewards: differential Sharpe ratio, drawdown penalties, CVaR
Do genetic programming trading rules beat random search and survive out of sample?
Quality-diversity and ensembles in evolutionary strategy search
LLM-driven strategy evolution: what did honest evaluation find?
Automated alpha and factor mining: fitness functions that avoid redundant factors
Simulators and generative order book models for training agents: how realistic are they?
Shielding or constraining an RL policy inside hard risk limits
How do transaction costs in the training objective change the turnover a policy learns?
Fitted Q-iteration and tabular value functions for trading or execution
Multi-agent and mixture-of-experts architectures for trading
# K. Combining signals and adapting online
Are equal weights hard to beat when combining forecasts, and why?
Online learning with expert advice or bandits for choosing among trading signals
Detecting concept drift and deciding when to retire a signal
Dynamic model averaging and time-varying weights for crypto forecasts
How fast do published or discovered trading signals decay?
Regime detection with hidden Markov models, jump models or changepoint detection, and what regimes predict
Gating a strategy by liquidity stress or by how unfamiliar the current state is
How should signals with different decay rates be blended under trading costs?
# L. Validation
Deflated Sharpe ratio and the number of trials: how to discount a backtest
Probability of backtest overfitting and combinatorial purged cross-validation
Reality check and bootstrap tests for the best of many trading rules
Walk-forward design: window lengths and how often to re-optimise
What sample length or track record is needed to trust a Sharpe ratio?
Common sources of look-ahead leakage in crypto backtests
What baselines and null strategies should a trading policy be compared with?
How do simulated fills at the mid or without queue modelling inflate backtest results?
# M. Sizing, risk and exits
Volatility targeting: does scaling position by forecast volatility improve risk-adjusted return?
Kelly sizing under estimation error with a leverage or liquidation constraint
Do stop-loss rules add value, and under what return dynamics?
Optimal holding period and exit given a decaying signal and proportional costs
Drawdown control rules and expected maximum drawdown
Optimal profit-taking and stop-loss thresholds for a mean-reverting process
Adding to a winning position versus keeping a fixed size
# N. Other information sources
Do stablecoin mints or exchange inflows precede price moves within hours?
Do large on-chain transfers to exchanges predict returns?
Solana network congestion, priority fees and failed transactions as market signals
Does social media attention or sentiment predict crypto returns or only volatility?
Options market signals: skew, net buying pressure and dealer gamma and their effect on spot
Do ETF flows drive bitcoin's price?
Do language-model-scored news headlines predict returns?
Which daily macro state variables change how crypto behaves intraday?
Does bitcoin's beta to equities vary by regime and time of day?
