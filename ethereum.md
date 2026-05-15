---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-15T12:17:17.738781+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- videos
- news
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 15, 2026 at 12:17 UTC  
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
**7d:** -3.1%  
**30d:** -4.0%  
**90d:** +14.7%  
**1y:** -11.2%  

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

7h ago

---

**[put $2.5k into a mid-cap through a dex and walked away $180 short, what went wrong?](https://www.reddit.com/r/ethereum/comments/1tdr5oj/put_25k_into_a_midcap_through_a_dex_and_walked/)**

swapped $2.5k worth of ETH into a mid-cap token recently. the preview showed 3% slippage, I set my tolerance to 4% and went ahead. came out $183 below the quoted amount. the pool showed roughly $800k in 24h volume so I assumed it was fine. I s this expected at this size or did I mess something up?

2h ago

---

**[Without stablecoin treasury yield, defi is a proof that finance is zero sum](https://www.reddit.com/r/ethereum/comments/1tdp2jc/without_stablecoin_treasury_yield_defi_is_a_proof/)**

4h ago

---

**[Daily General Discussion May 14, 2026](https://www.reddit.com/r/ethereum/comments/1tco2pd/daily_general_discussion_may_14_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[$770 million stolen in defi this year. 40+ protocols shut down. bridges are the common denominator and nobody is fixing the actual problem.](https://www.reddit.com/r/ethereum/comments/1tcu2m4/770_million_stolen_in_defi_this_year_40_protocols/)**

the numbers from 2026 so far are genuinely scary: kelp DAO: $293M drained through their layerzero bridge. single exploit hit 20+ chains because one bridge contract held the reserves for all of them drift protocol: $285M. north korean hackers spent 6 months social engineering their way in 1inch/trustedvolumes: $6.7M last week. same attacker from the 2025 hack came back and found a new door april 2026 alone: $600M+ stolen across 28-30 separate incidents. worst single month in crypto history 40+ protocols have shut down or entered wind-down mode this year. aave froze rsETH markets and lost $6 billion in TVL from panic withdrawals even though their contracts weren't touched. the pattern isn't random. bridges keep producing the biggest single-day losses because they're designed as massive honeypots. $22 billion in bridge TVL as of march, each one a single point of failure for every protocol downstream. what bugs me is the response is always the same. "we need better audits." "we need better monitoring." nobody is questioning whether the bridge model itself is fundamentally broken. bridges work by locking assets on one chain and minting representations on another through a trusted intermediary (multisig, oracle network, validator set). every one of these is an attack surface. kelp's bridge got spoofed because layerzero's messaging layer was fooled into thinking the withdrawal was legitimate. the alternative exists. data availability layers can handle cross-chain verification without lock-and-mint. instead of one contract holding $293M that can be drained in a single tx, you verify data availability cryptographically across chains. no honeypot, no single point of failure, no trusted intermediary to spoof. DA layers like avail, celestia, eigenda are live and production ready. the tech isn't theoretical anymore. it's an adoption problem not a research problem. at what point do we stop patching bridges and start replacing them?

1d ago

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

**[Bitcoin, Ethereum Up 2%, XRP Skyrockets 6% On Clarity Act Advancement](https://www.benzinga.com/crypto/cryptocurrency/26/05/52575736/bitcoin-ethereum-up-2-xrp-skyrockets-6-on-clarity-act-advancement)**

Bitcoin climbed back above $81,000 after the Senate Banking committee advanced the Clarity Act, helping boost optimism around improving crypto regulation and institutional adoption.

Benzinga • 17h ago

---

**[Ethereum News: Vitalik Buterin ‘Puts Skin in the Game’ with $113K Privacy Pools Transfer](https://finance.yahoo.com/markets/crypto/articles/ethereum-news-vitalik-buterin-puts-100247306.html)**

In the latest news, Ethereum co-founder Vitalik Buterin transferred 50.25 ETH, approximately $113,000 at current prices, through Privacy Pools, the compliance-aware privacy protocol he co-authored in a 2023 research paper, publicly validating the tool with real capital rather than white-paper advocacy.The move comes weeks after 0xbow.io launched the protocol on ...

Yahoo Finance • 2h ago

---

**[Thorchain halts trading after $10 million cross-chain exploit, RUNE token drops 12%](https://www.coindesk.com/tech/2026/05/15/thorchain-halts-trading-after-usd10-million-cross-chain-exploit-rune-token-drops-12)**

CoinDesk • 1h ago

---

**[Bitcoin and ethereum prices today, Thursday, May 14, 2026: Bitcoin and ethereum prices slipping this week](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-thursday-may-14-2026-bitcoin-and-ethereum-prices-slipping-this-week-111938059.html)**

Bitcoin opened at $79,283.34 on Thursday, down 1.5% from Wednesday's opening price. Ethereum opened at $2,257.71 on Thursday, down 0.7% from Wednesday’s opening value.

Yahoo Finance • 1d ago

---

**[Bitcoin and ethereum prices today, Friday, May 15, 2026: Prices open higher, but slipping this morning](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-may-15-2026-prices-open-higher-but-slipping-this-morning-111851137.html)**

Bitcoin opened at $81,069.54 on Friday, up 2.3% from Thursday’s open. The value of bitcoin fell to $80,596.43 by 7:10 a.m ET. Ethereum opened at $2,282.46 on Friday, up 1.1% from Thursday’s open. The value of ethereum was down as of 7:10 a.m. ET, at $2,257.73.

Yahoo Finance • 58m ago

---

**[Analyst Reveals What CLARITY Act Passing Today Means for Bitcoin, Ethereum and XRP Prices](https://coinpedia.org/news/analyst-reveals-what-clarity-act-passing-today-means-for-bitcoin-ethereum-and-xrp-prices/)**

Coinpedia • 10h ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 19h ago

---

**[Ethereum Leverage Tells Two Different Stories On Binance And OKX: Traders Face A Fragile Setup](https://www.tradingview.com/news/newsbtc:3ab10ffc2094b:0-ethereum-leverage-tells-two-different-stories-on-binance-and-okx-traders-face-a-fragile-setup/)**

Ethereum is consolidating between $2,250 and $2,450 as the market searches for the catalyst or the structural shift that forces a decisive move in either direction. The price is holding but not breaking — and CryptoQuant analyst MorenoDV has identified a divergence in the derivatives data across tw…

TradingView • 23h ago

---

**[JPMorgan launching second tokenized money market fund on Ethereum](https://www.theblock.co/post/401028/jpmorgan-launching-tokenized-money-market-fund-ethereum)**

The new fund will invest in U.S. Treasurys and overnight repurchase agreements collateralized by Treasurys or cash.

The Block • 2d ago

---

**[JPMorgan Launching Second Tokenized Money Market Fund on Ethereum — Bullish For ETH Price?](https://finance.yahoo.com/news/jpmorgan-launching-second-tokenized-money-100215730.html)**

JPMorgan has filed for a second tokenized money market fund on Ethereum. The proposed JLTXX fund would tokenize Treasury-backed assets on Ethereum. Some analysts and ...

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "ethereum"

**[&quot;Ethereum To $12,000,  Bitcoin To $250,000 - Here&#39;s WHY&quot; Tom Lee | Crypto Prediction 2026](https://www.youtube.com/watch?v=zQGTvz_2YM4)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 10K • 👍 358 • 💬 53 • ⏱️ 18:57 • 19h ago

---

**[ETH Supply Shock Could Send Ethereum To $20K Explained](https://www.youtube.com/watch?v=7WiPJ8CUCo8)**

Tom Lee says Ethereum could eventually reach $20000+ Explained Earn $ETH with MaxFi - https://www.maxfi.tech/ Big Time ...

📺 Big Time Trades

👁️ 1K • 👍 47 • 💬 9 • ⏱️ 23:46 • 12h ago

---

**[BITCOIN DUMP &amp; PUMP: LIQUIDATIONS COMING SOON!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=044o4K5-hME)**

BITCOIN DUMP & PUMP: LIQUIDATIONS COMING SOON!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 5K • 👍 217 • 💬 122 • ⏱️ 16:42 • 8h ago

---

**[🚨 BTC &amp; ETH: THIS IS BAD!!!](https://www.youtube.com/watch?v=0JR0z7vRGqM)**

This data is terrible for bitcoin, ethereum and the rest of crypto! WATCH OUT NOW!!!! ---------- Join My FREE Trading Group ...

📺 Thomas Kralow

👁️ 9K • 👍 2K • 💬 20 • ⏱️ 4:30 • 1d ago

---

**[Ethereum Y Altcoins: Analisis A Largo Plazo #2](https://www.youtube.com/watch?v=epKcp_P9z1o)**

Registrate en Bitget (20% de descuento en comisiones EN SPOT Y FUTUROS DE POR VIDA) ...

📺 CdeCripto

👁️ 3K • 👍 407 • 💬 56 • ⏱️ 26:03 • 15h ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=gAR14kuRpZ8)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 1K • 👍 70 • 💬 2 • ⏱️ 7:18 • 9h ago

---

**[Ethereum VS XRP – Which Is Better?](https://www.youtube.com/watch?v=AiaKtqyYLcA)**

Ethereum and Ripple are often compared, but they're solving completely different problems. One is a global app platform, the ...

📺 CoinGecko

👁️ 2K • 👍 148 • 💬 101 • ⏱️ 3:46 • 1d ago

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
