---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-15T10:24:52.267787+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- news
- cryptocurrency
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 15, 2026 at 10:24 UTC  
**HTML Version:** [ethereum.html](https://peekdeck.ruidiao.dev/ethereum.html)

---

## Table of Contents

1. [Ethereum Price](#ethereum-price)
2. [Ethereum Chart](#ethereum-chart)
3. [Ethereum Market Stats](#ethereum-market-stats)
4. [Reddit: r/ethereum](#reddit-rethereum)
5. [Google News: "ethereum"](#google-news-ethereum)
6. [YouTube Videos: "ethereum"](#youtube-videos-ethereum)

---

## Ethereum Price

### $2,304.72

---

## Ethereum Chart

**24h:** +0.1%  
**7d:** -3.0%  
**30d:** -3.9%  
**90d:** +14.8%  
**1y:** -11.1%  

---

## Ethereum Market Stats

**Market Cap:** $272.28B
Rank #2

**Circulating Supply:** 120,686,088 ETH
No max supply

**All-Time High:** $4,946.05
-54.4%

**All-Time Low:** $0.43
+520897.6%

---

## Reddit: r/ethereum

**[Daily General Discussion May 15, 2026](https://www.reddit.com/r/ethereum/comments/1tdm9xw/daily_general_discussion_may_15_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

5h ago

---

**[put $2.5k into a mid-cap through a dex and walked away $180 short, what went wrong?](https://www.reddit.com/r/ethereum/comments/1tdr5oj/put_25k_into_a_midcap_through_a_dex_and_walked/)**

swapped $2.5k worth of ETH into a mid-cap token recently. the preview showed 3% slippage, I set my tolerance to 4% and went ahead. came out $183 below the quoted amount. the pool showed roughly $800k in 24h volume so I assumed it was fine. I s this expected at this size or did I mess something up?

55m ago

---

**[Without stablecoin treasury yield, defi is a proof that finance is zero sum](https://www.reddit.com/r/ethereum/comments/1tdp2jc/without_stablecoin_treasury_yield_defi_is_a_proof/)**

2h ago

---

**[Daily General Discussion May 14, 2026](https://www.reddit.com/r/ethereum/comments/1tco2pd/daily_general_discussion_may_14_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[$770 million stolen in defi this year. 40+ protocols shut down. bridges are the common denominator and nobody is fixing the actual problem.](https://www.reddit.com/r/ethereum/comments/1tcu2m4/770_million_stolen_in_defi_this_year_40_protocols/)**

the numbers from 2026 so far are genuinely scary: kelp DAO: $293M drained through their layerzero bridge. single exploit hit 20+ chains because one bridge contract held the reserves for all of them drift protocol: $285M. north korean hackers spent 6 months social engineering their way in 1inch/trustedvolumes: $6.7M last week. same attacker from the 2025 hack came back and found a new door april 2026 alone: $600M+ stolen across 28-30 separate incidents. worst single month in crypto history 40+ protocols have shut down or entered wind-down mode this year. aave froze rsETH markets and lost $6 billion in TVL from panic withdrawals even though their contracts weren't touched. the pattern isn't random. bridges keep producing the biggest single-day losses because they're designed as massive honeypots. $22 billion in bridge TVL as of march, each one a single point of failure for every protocol downstream. what bugs me is the response is always the same. "we need better audits." "we need better monitoring." nobody is questioning whether the bridge model itself is fundamentally broken. bridges work by locking assets on one chain and minting representations on another through a trusted intermediary (multisig, oracle network, validator set). every one of these is an attack surface. kelp's bridge got spoofed because layerzero's messaging layer was fooled into thinking the withdrawal was legitimate. the alternative exists. data availability layers can handle cross-chain verification without lock-and-mint. instead of one contract holding $293M that can be drained in a single tx, you verify data availability cryptographically across chains. no honeypot, no single point of failure, no trusted intermediary to spoof. DA layers like avail, celestia, eigenda are live and production ready. the tech isn't theoretical anymore. it's an adoption problem not a research problem. at what point do we stop patching bridges and start replacing them?

23h ago

---

**[I cracked Vitalik’s 2015 on-chain ad platform. He was the only bidder. Total cost: $2.](https://www.reddit.com/r/ethereum/comments/1tbzzvi/i_cracked_vitaliks_2015_onchain_ad_platform_he/)**

Three months after mainnet launched, Vitalik deployed an advertising auction system to Ethereum. Eight ad slots, four auction mechanisms (one-phase winner-pays, cumulative, sealed-bid first-price, sealed-bid second-price), all managed by a factory contract called adStorer from ethereum/dapp-bin. I matched the deployed bytecode to source through compiler archaeology. Exact match, 8,752 bytes, solc v0.1.1. Then I decoded every transaction across all 8 child auction contracts. The only bidder was Vitalik himself. Two wallets (his old deployer and what’s now vitalik.eth), 229 transactions, 0.064 ETH in bids. The winning “advertisements” were two image URLs: me.jpg (a photo of himself) and heiko.jpg (a photo of Heiko Hees, who was building pyethereum). Both are 404 today. Some details: Slot 5 is a second-price sealed-bid auction. vitalik.eth bid 0.0005 ETH, his old wallet bid 0.0003 ETH. Second-price rules made vitalik.eth pay the runner-up’s price. The first Vickrey auction on Ethereum selected a photo of a pyethereum developer over its own creator. Gas cost more than the bids. Vitalik burned ~1 ETH on gas (at 60 gwei, hard-coded in his deploy script) to move 0.064 ETH through the auction mechanics. At October 2015 prices, the whole experiment cost about $2. Slot 1 was a stress test. 159 transactions, with Vitalik rebidding the same 0.0001 ETH increment 19 times in a row to validate cumulative bidding. Three of the four all-pay auction variants got zero bids. He abandoned the one he tried before revealing. Even Vitalik didn’t trust his own all-pay math. The sealed-bid auctions had a frontend bug where bid hashes were passed as ASCII hex instead of raw bytes, making commitments readable in calldata. Didn’t matter since the only participant wrote the code. 0.029 ETH (~$70 today, $0.03 in 2015) is still locked in the child contracts from unrevealed sealed bids. This was deployed three weeks before DevCon 1, on a network with maybe a few hundred users. A mechanism design experiment that nobody participated in except its creator, preserved on-chain for ten years. I checked the Wayback Machine for the ad images. The closest capture of vitalik.ca/files/ is from June 2016. Neither photo was archived. Full documentation with verified source, decoded bids, and all 8 slots mapped: https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e This is part of the EthereumHistory project where we’re documenting and verifying the earliest Ethereum contracts. If you want to help, the project is open.

🔗 [Ethereum History](https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e) • 1d ago

---

**[Why are banks and institutional funds actually interested in Ethereum?](https://www.reddit.com/r/ethereum/comments/1tcbpby/why_are_banks_and_institutional_funds_actually/)**

I get the basics of how Ethereum works, but I’m trying to understand the institutional side better. What do they actually want from it? And does their involvement change where Ethereum is headed, whether that’s decentralization, governance, or how the protocol develops? Genuinely curious what people who follow this space think.

1d ago

---

**[Upgrading Finality - Edition 1 | Protocol Consensus](https://www.reddit.com/r/ethereum/comments/1tcjd00/upgrading_finality_edition_1_protocol_consensus/)**

Turning consensus research into practice. We design, analyze, and formally verify consensus protocols for Ethereum.

🔗 [consensus.ethereum.foundation](https://consensus.ethereum.foundation/blog/upgrading-finality-edition-1) • 1d ago

---

**[Every time I try to move money between my bank and crypto I feel like a criminal even though I've done nothing wrong](https://www.reddit.com/r/ethereum/comments/1tc5b1e/every_time_i_try_to_move_money_between_my_bank/)**

My bank has flagged two of my transfers to a crypto exchange in the last three months. First time they put the money on hold for 48 hours. Second time someone from their fraud team called me to ask what I was buying and why. I answered everything honestly and they released the funds but the whole interaction felt accusatory. I'm not doing anything illegal, I'm just buying some ETH. Has anyone found a way to make this less terrible

1d ago

---

**[Aztec Foundation contributes 1% of AZTEC token supply toward supporting Ethereum Core Development via Protocol Guild](https://www.reddit.com/r/ethereum/comments/1tc65xb/aztec_foundation_contributes_1_of_aztec_token/)**

🔗 [X (formerly Twitter)](https://x.com/ProtocolGuild/status/2054190784061091896?s=20) • 1d ago

---

---

## Google News: "ethereum"

**[Ethereum Crushes Rivals With Nearly 900000 Validators Worldwide, Leaves SOL And ADA Behind](https://www.tradingview.com/news/coinpedia:f1de50b5a094b:0-ethereum-crushes-rivals-with-nearly-900000-validators-worldwide-leaves-sol-and-ada-behind/)**

Ethereum is making headlines today. New data from Chainspect reveals the network now has more than 897,000 validators spread across the world, a number that completely overshadows almost every competing blockchain.Cardano has around 2,900 validators, Algorand has around 1,600, while Solana has roug…

TradingView • 3h ago

---

**[Ethereum TD Sequential Flashes Sell Signal – Is A New 50% Corrective Phase Starting?](https://www.tradingview.com/news/newsbtc:75f77f89c094b:0-ethereum-td-sequential-flashes-sell-signal-is-a-new-50-corrective-phase-starting/)**

As the market reacts to the latest crypto legislation, Ethereum (ETH) is flashing warning signs after a fresh technical sell signal emerged for the first time in months and a spike in on‑chain realized profits.Ethereum Risks New Leg Down After Key Sell SignalOn Thursday, Ethereum jumped 3.5 % intra…

TradingView • 3h ago

---

**[Key facts: BTBT Q1 loss; $79.5M cash, $295M assets, WhiteFiber $322M; pivots Ethereum/AI](https://www.tradingview.com/news/tradingview:d6b0b7c10518c:0-key-facts-btbt-q1-loss-79-5m-cash-295m-assets-whitefiber-322m-pivots-ethereum-ai/)**

TradingView • 3h ago

---

**[Analyst Reveals What CLARITY Act Passing Today Means for Bitcoin, Ethereum and XRP Prices](https://coinpedia.org/news/analyst-reveals-what-clarity-act-passing-today-means-for-bitcoin-ethereum-and-xrp-prices/)**

Coinpedia • 9h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Jump After Crypto Act Passes Key Senate Vote: Analyst Says BTC 'Positioned' For A Rebound Toward $86,000](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-dogecoin-jump-015048079.html)**

Leading cryptocurrencies were up in the green on Thursday after the Clarity Act passed the Senate Banking Committee on a bipartisan vote. Cryptocurrency24-Hour Gains +/-Price (Recorded at 9:05 p.m. EDT)Bitcoin (CRYPTO: BTC)+2.46%$81,561.50Ethereum (CRYPTO: ETH) +1.18%$2,293.12XRP (CRYPTO: XRP) +4.49%$1.49Solana (CRYPTO: SOL) +1.33%$92.42Dogecoin (CRYPTO: DOGE) +2.10%$0.1167 Crypto Market Pops Bitcoin hit $82,000 in the afternoon, then stalled and moved sideways. The trading volume soared 27% in

Yahoo Finance • 8h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC gains traction, ETH consolidates, XRP turns bullish after channel breakout](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-gains-traction-eth-consolidates-xrp-turns-bullish-after-channel-breakout-202605150351)**

Bitcoin (BTC) and Ripple (XRP) prices trade slightly higher on Friday, while Ethereum (ETH) continues to consolidate around a key support zone. BTC rebounds after finding support at the key level hit the previous day, and ETH consolidates around its crucial 50-day EMA near $2,274.

FXStreet • 6h ago

---

**[Ethereum app builder Consensys has delayed its potential IPO until fall](https://www.coindesk.com/business/2026/05/13/ethereum-app-builder-consensys-has-delayed-its-potential-ipo-until-fall)**

The MetaMask wallet builder had reportedly engaged bankers from JPMorgan and Goldman Sachs to lead the process.

CoinDesk • 1d ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 17h ago

---

**[Charles Schwab Begins Offering Bitcoin, Ethereum Trading to US Users](https://decrypt.co/367768/charles-schwab-begins-bitcoin-ethereum-trading-us-users)**

Charles Schwab started allowing select users to trade Bitcoin and Ethereum directly alongside their other investments.

Decrypt • 1d ago

---

**[Current price of Ethereum for May 14, 2026](https://fortune.com/article/price-of-ethereum-05-14-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 21h ago

---

---

## YouTube Videos: "ethereum"

**[&quot;Ethereum To $12,000,  Bitcoin To $250,000 - Here&#39;s WHY&quot; Tom Lee | Crypto Prediction 2026](https://www.youtube.com/watch?v=zQGTvz_2YM4)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 10K • 👍 358 • 💬 53 • ⏱️ 18:57 • 17h ago

---

**[ETH Supply Shock Could Send Ethereum To $20K Explained](https://www.youtube.com/watch?v=7WiPJ8CUCo8)**

Tom Lee says Ethereum could eventually reach $20000+ Explained Earn $ETH with MaxFi - https://www.maxfi.tech/ Big Time ...

📺 Big Time Trades

👁️ 1K • 👍 47 • 💬 9 • ⏱️ 23:46 • 10h ago

---

**[BITCOIN DUMP &amp; PUMP: LIQUIDATIONS COMING SOON!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=044o4K5-hME)**

BITCOIN DUMP & PUMP: LIQUIDATIONS COMING SOON!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 5K • 👍 217 • 💬 122 • ⏱️ 16:42 • 7h ago

---

**[🚨 BTC &amp; ETH: THIS IS BAD!!!](https://www.youtube.com/watch?v=0JR0z7vRGqM)**

This data is terrible for bitcoin, ethereum and the rest of crypto! WATCH OUT NOW!!!! ---------- Join My FREE Trading Group ...

📺 Thomas Kralow

👁️ 9K • 👍 2K • 💬 20 • ⏱️ 4:30 • 1d ago

---

**[Ethereum Y Altcoins: Analisis A Largo Plazo #2](https://www.youtube.com/watch?v=epKcp_P9z1o)**

Registrate en Bitget (20% de descuento en comisiones EN SPOT Y FUTUROS DE POR VIDA) ...

📺 CdeCripto

👁️ 3K • 👍 407 • 💬 56 • ⏱️ 26:03 • 13h ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=gAR14kuRpZ8)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 1K • 👍 70 • 💬 2 • ⏱️ 7:18 • 7h ago

---

**[Ethereum VS XRP – Which Is Better?](https://www.youtube.com/watch?v=AiaKtqyYLcA)**

Ethereum and Ripple are often compared, but they're solving completely different problems. One is a global app platform, the ...

📺 CoinGecko

👁️ 2K • 👍 148 • 💬 101 • ⏱️ 3:46 • 23h ago

---

**[XRP FLIPS BITCOIN AND ETHEREUM CLARITY THREATENS XRP SOLANA AND MORE! #xrp #crypto #bitcoin](https://www.youtube.com/watch?v=f_aFtTWDTB0)**

📺 CryptoWendyO

👁️ 17K • 👍 1K • 💬 60 • ⏱️ 2:13 • 1d ago

---

**[Why Ethereum is Stuck Under $2.4K](https://www.youtube.com/watch?v=8TUiX3l06XM)**

Ethereum keeps failing at the $2400 resistance level, and the data shows why: weak ETF inflows, falling leverage, and rising ETH ...

📺 Coin Bureau Podcast

👁️ 2K • 👍 47 • 💬 4 • ⏱️ 1:11 • 2d ago

---

**[☠ Ethereum Story Is Breaking - ETH Crypto Analysis](https://www.youtube.com/watch?v=x2HEF-EuTkw)**

Join Premium: https://the-bitcoin-strategy.com Instagram: https://www.instagram.com/gerhard_bitcoin_strategy/ My Chart ...

📺 Gerhard - Bitcoin Strategy

👁️ 3K • 👍 90 • 💬 14 • ⏱️ 10:03 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
