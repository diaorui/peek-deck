---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-16T11:04:22.927532+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 16, 2026 at 11:04 UTC  
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

### $2,171.71

---

## Ethereum Chart

**24h:** -3.4%  
**7d:** -8.1%  
**30d:** -10.0%  
**90d:** +9.0%  
**1y:** -12.0%  

---

## Ethereum Market Stats

**Market Cap:** $262.62B
Rank #2

**Circulating Supply:** 120,685,841 ETH
No max supply

**All-Time High:** $4,946.05
-56.0%

**All-Time Low:** $0.43
+502522.5%

---

## Reddit: r/ethereum

**[Daily General Discussion May 16, 2026](https://www.reddit.com/r/ethereum/comments/1tejwhl/daily_general_discussion_may_16_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

6h ago

---

**[Architectural Breakdown: EVM Events, Transaction Receipts, and RPC Log Filtering](https://www.reddit.com/r/ethereum/comments/1tepe86/architectural_breakdown_evm_events_transaction/)**

Events (logs) are the EVM’s native asynchronous data pipeline, but they are fundamentally distinct from contract storage. Instead of modifying the state trie, events write directly to the transaction receipt trie. This structural separation is what makes them highly gas-efficient for off-chain indexing. Under the hood, an emitted event is partitioned into topics and data: Topics are the search keys: Capped at 4 topics per log. Topic[0] is always the keccak256 hash of the event signature (e.g., Transfer(address,address,uint256)). Topic[1] through Topic[3] are your indexed parameters, padded to fixed 32-byte values. This allows RPC nodes to build bloom filters, enabling highly efficient eth_getLogs queries over millions of blocks without reading the full log payload. Data (The Blob): All non-indexed parameters are ABI-encoded into a single raw byte string. While cheaper in gas, this data is strictly unsearchable at the RPC layer; you must fetch the raw log and decode it client-side. When querying an RPC provider via eth_getLogs, you are searching against these bloom filters. Passing an array of topics in your RPC call allows for direct intersection matching to isolate specific contract interactions without touching the execution environment. Source/Full Breakdown:https://andreyobruchkov1996.substack.com/p/understanding-events-the-evms-built Since event logs aren't accessible from within smart contracts, how would you securely prove to a downstream L1 contract that a specific event was emitted on an L2 roll-up without relying on a trusted centralized indexer?

1h ago

---

**[Ethereal news weekly #23 | Clear signing, CLARITY Act advanced out of Senate Banking committee, Ben Edgington fast finality plan](https://www.reddit.com/r/ethereum/comments/1tdy4x1/ethereal_news_weekly_23_clear_signing_clarity_act/)**

Clear signing, CLARITY Act advanced out of Senate Banking committee, Ben Edgington fast finality plan

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-23/) • 20h ago

---

**[Daily General Discussion May 15, 2026](https://www.reddit.com/r/ethereum/comments/1tdm9xw/daily_general_discussion_may_15_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[put $2.5k into a mid-cap through a dex and walked away $180 short, what went wrong?](https://www.reddit.com/r/ethereum/comments/1tdr5oj/put_25k_into_a_midcap_through_a_dex_and_walked/)**

swapped $2.5k worth of ETH into a mid-cap token recently. the preview showed 3% slippage, I set my tolerance to 4% and went ahead. came out $183 below the quoted amount. the pool showed roughly $800k in 24h volume so I assumed it was fine. I s this expected at this size or did I mess something up?

1d ago

---

**[Without stablecoin treasury yield, defi is a proof that finance is zero sum](https://www.reddit.com/r/ethereum/comments/1tdp2jc/without_stablecoin_treasury_yield_defi_is_a_proof/)**

1d ago

---

**[Daily General Discussion May 14, 2026](https://www.reddit.com/r/ethereum/comments/1tco2pd/daily_general_discussion_may_14_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[$770 million stolen in defi this year. 40+ protocols shut down. bridges are the common denominator and nobody is fixing the actual problem.](https://www.reddit.com/r/ethereum/comments/1tcu2m4/770_million_stolen_in_defi_this_year_40_protocols/)**

the numbers from 2026 so far are genuinely scary: kelp DAO: $293M drained through their layerzero bridge. single exploit hit 20+ chains because one bridge contract held the reserves for all of them drift protocol: $285M. north korean hackers spent 6 months social engineering their way in 1inch/trustedvolumes: $6.7M last week. same attacker from the 2025 hack came back and found a new door april 2026 alone: $600M+ stolen across 28-30 separate incidents. worst single month in crypto history 40+ protocols have shut down or entered wind-down mode this year. aave froze rsETH markets and lost $6 billion in TVL from panic withdrawals even though their contracts weren't touched. the pattern isn't random. bridges keep producing the biggest single-day losses because they're designed as massive honeypots. $22 billion in bridge TVL as of march, each one a single point of failure for every protocol downstream. what bugs me is the response is always the same. "we need better audits." "we need better monitoring." nobody is questioning whether the bridge model itself is fundamentally broken. bridges work by locking assets on one chain and minting representations on another through a trusted intermediary (multisig, oracle network, validator set). every one of these is an attack surface. kelp's bridge got spoofed because layerzero's messaging layer was fooled into thinking the withdrawal was legitimate. the alternative exists. data availability layers can handle cross-chain verification without lock-and-mint. instead of one contract holding $293M that can be drained in a single tx, you verify data availability cryptographically across chains. no honeypot, no single point of failure, no trusted intermediary to spoof. DA layers like avail, celestia, eigenda are live and production ready. the tech isn't theoretical anymore. it's an adoption problem not a research problem. at what point do we stop patching bridges and start replacing them?

2d ago

---

**[I cracked Vitalik’s 2015 on-chain ad platform. He was the only bidder. Total cost: $2.](https://www.reddit.com/r/ethereum/comments/1tbzzvi/i_cracked_vitaliks_2015_onchain_ad_platform_he/)**

Three months after mainnet launched, Vitalik deployed an advertising auction system to Ethereum. Eight ad slots, four auction mechanisms (one-phase winner-pays, cumulative, sealed-bid first-price, sealed-bid second-price), all managed by a factory contract called adStorer from ethereum/dapp-bin. I matched the deployed bytecode to source through compiler archaeology. Exact match, 8,752 bytes, solc v0.1.1. Then I decoded every transaction across all 8 child auction contracts. The only bidder was Vitalik himself. Two wallets (his old deployer and what’s now vitalik.eth), 229 transactions, 0.064 ETH in bids. The winning “advertisements” were two image URLs: me.jpg (a photo of himself) and heiko.jpg (a photo of Heiko Hees, who was building pyethereum). Both are 404 today. Some details: Slot 5 is a second-price sealed-bid auction. vitalik.eth bid 0.0005 ETH, his old wallet bid 0.0003 ETH. Second-price rules made vitalik.eth pay the runner-up’s price. The first Vickrey auction on Ethereum selected a photo of a pyethereum developer over its own creator. Gas cost more than the bids. Vitalik burned ~1 ETH on gas (at 60 gwei, hard-coded in his deploy script) to move 0.064 ETH through the auction mechanics. At October 2015 prices, the whole experiment cost about $2. Slot 1 was a stress test. 159 transactions, with Vitalik rebidding the same 0.0001 ETH increment 19 times in a row to validate cumulative bidding. Three of the four all-pay auction variants got zero bids. He abandoned the one he tried before revealing. Even Vitalik didn’t trust his own all-pay math. The sealed-bid auctions had a frontend bug where bid hashes were passed as ASCII hex instead of raw bytes, making commitments readable in calldata. Didn’t matter since the only participant wrote the code. 0.029 ETH (~$70 today, $0.03 in 2015) is still locked in the child contracts from unrevealed sealed bids. This was deployed three weeks before DevCon 1, on a network with maybe a few hundred users. A mechanism design experiment that nobody participated in except its creator, preserved on-chain for ten years. I checked the Wayback Machine for the ad images. The closest capture of vitalik.ca/files/ is from June 2016. Neither photo was archived. Full documentation with verified source, decoded bids, and all 8 slots mapped: https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e This is part of the EthereumHistory project where we’re documenting and verifying the earliest Ethereum contracts. If you want to help, the project is open.

🔗 [Ethereum History](https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e) • 2d ago

---

**[Why are banks and institutional funds actually interested in Ethereum?](https://www.reddit.com/r/ethereum/comments/1tcbpby/why_are_banks_and_institutional_funds_actually/)**

I get the basics of how Ethereum works, but I’m trying to understand the institutional side better. What do they actually want from it? And does their involvement change where Ethereum is headed, whether that’s decentralization, governance, or how the protocol develops? Genuinely curious what people who follow this space think.

2d ago

---

---

## Google News: "ethereum"

**[Ethereum News: Tom Lee's BitMine Just Slashed ETH Buying by 74%, Here's What Comes Next](https://247wallst.com/investing/2026/05/14/ethereum-news-tom-lees-bitmine-just-slashed-eth-buying-by-74-heres-what-comes-next/)**

BitMine Immersion Technologies has cut its Ethereum (ETH) buying pace by 74% as it nears its 5% supply target. Here's the market reaction.

24/7 Wall St. • 1d ago

---

**[Sharplink CEO points out 3 catalysts for Ethereum's price to surge higher](https://www.tradingview.com/news/cointelegraph:06e190bf8094b:0-sharplink-ceo-points-out-3-catalysts-for-ethereum-s-price-to-surge-higher/)**

Ethereum needs three catalysts to fall into place for its price to regain momentum and surge higher, according to SharpLink Gaming CEO Joseph Chalom.“One is the CLARITY Act to pass in the US,” Chalom pointed out in an interview with Robert Baggs on Cointelegraph’s Chain Reaction show published to Y…

TradingView • 2h ago

---

**[Bitmine Pivots To Ethereum Staking Yield As NYSE Uplisting Draws Focus](https://finance.yahoo.com/markets/crypto/articles/bitmine-pivots-ethereum-staking-yield-091827775.html)**

Bitmine Immersion Technologies (NYSE:BMNR) is slowing its aggressive Ethereum accumulation strategy and shifting toward optimizing staking yield. The move aligns with management's view that the crypto winter is ending and that Ethereum offers attractive staking economics. The company recently uplisted to the NYSE, which has increased institutional investor visibility and trading liquidity. Bitmine Immersion Technologies, now trading on the NYSE under the ticker BMNR, operates in a corner of...

Yahoo Finance • 1h ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 1d ago

---

**[Ethereum To $5,000? Muted Predictions As JPMorgan Claims ETH Will Stay Behind Bitcoin Without Improvements](https://www.ccn.com/news/crypto/ethereum-price-5000-jpmorgan-eth-bitcoin/)**

CCN.com • 1d ago

---

**[Thorchain halts trading after $10 million cross-chain exploit, RUNE token drops 12%](https://www.coindesk.com/tech/2026/05/15/thorchain-halts-trading-after-usd10-million-cross-chain-exploit-rune-token-drops-12)**

CoinDesk • 21h ago

---

**[Bitcoin and ethereum prices today, Friday, May 15, 2026: Prices open higher, but slipping this morning](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-may-15-2026-prices-open-higher-but-slipping-this-morning-111851137.html)**

Bitcoin opened at $81,069.54 on Friday, up 2.3% from Thursday’s open. The value of bitcoin fell to $80,596.43 by 7:10 a.m ET. Ethereum opened at $2,282.46 on Friday, up 1.1% from Thursday’s open. The value of ethereum was down as of 7:10 a.m. ET, at $2,257.73.

Yahoo Finance • 23h ago

---

**[Crypto Today: Bitcoin, Ethereum, XRP edge down, testing support as resistance holds](https://www.fxstreet.com/cryptocurrencies/news/crypto-today-bitcoin-ethereum-xrp-edge-down-testing-support-as-resistance-holds-202605151200)**

Cryptocurrency prices are broadly correcting on Friday, following a failed attempt to recover losses incurred earlier in the week after the United States (US) Senate Banking Committee advanced the Digital Asset Market Clarity Act, commonly known as the Clarity Act of 2025.

FXStreet • 23h ago

---

**[Analyst Reveals What CLARITY Act Passing Today Means for Bitcoin, Ethereum and XRP Prices](https://coinpedia.org/news/analyst-reveals-what-clarity-act-passing-today-means-for-bitcoin-ethereum-and-xrp-prices/)**

Coinpedia • 1d ago

---

**[Current price of Ethereum for May 15, 2026](https://fortune.com/article/price-of-ethereum-05-15-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 19h ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee :&quot;Ethereum To $444,000 In The Next Few Years - How ETH Could Realistically 120x&quot; | 2026](https://www.youtube.com/watch?v=nUp6xKbaL_Q)**

Our FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Library Of Wealth

👁️ 713 • 👍 39 • 💬 68 • ⏱️ 15:37 • 4h ago

---

**[&quot;Ethereum To $12,000,  Bitcoin To $250,000 - Here&#39;s WHY&quot; Tom Lee | Crypto Prediction 2026](https://www.youtube.com/watch?v=zQGTvz_2YM4)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 13K • 👍 426 • 💬 53 • ⏱️ 18:57 • 1d ago

---

**[ETHEREUM BUY TARGET SOON!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=mREX7HVUtJ4)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 127 • 👍 12 • 💬 2 • ⏱️ 4:43 • 1h ago

---

**[BITCOIN &amp; ALTCOINS AT BREAKING POINT (Final Warning)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=OjVCJDZBRlI)**

BITCOIN & ALTCOINS AT BREAKING POINT (Final Warning)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 7K • 👍 277 • 💬 49 • ⏱️ 18:49 • 7h ago

---

**[Clarity Passes, Stocks Rip, &amp; Wall Street Piles Into Ethereum](https://www.youtube.com/watch?v=2_TwBsL3U9o)**

GALAXY | INSTITUTIONAL DIGITAL FINANCE https://bankless.cc/Galaxy --- Markets are ignoring every warning sign as stocks hit ...

📺 Bankless

👁️ 5K • 👍 194 • 💬 39 • ⏱️ 1:05:23 • 1d ago

---

**[Ethereum’s Institutional Era Has Arrived](https://www.youtube.com/watch?v=b7xVgaG0o-w)**

Sharplink CEO Joseph Chalom joins Gareth Jenkinson at Consensus to explain why SharpLink has taken an institutional-first ...

📺 The Block

👁️ 3K • 👍 86 • 💬 25 • ⏱️ 13:36 • 21h ago

---

**[ETH Supply Shock Could Send Ethereum To $20K Explained](https://www.youtube.com/watch?v=7WiPJ8CUCo8)**

Tom Lee says Ethereum could eventually reach $20000+ Explained Earn $ETH with MaxFi - https://www.maxfi.tech/ Big Time ...

📺 Big Time Trades

👁️ 2K • 👍 75 • 💬 63 • ⏱️ 23:46 • 1d ago

---

**[Ethereum June Outlook: Historical Pattern Turns Bearish](https://www.youtube.com/watch?v=ixVrjnkjc3w)**

In this video we take the first proper public look inside the MCO Terminal and analyze Ethereum using the MCO Seasonality Tool.

📺 More Crypto Online

👁️ 2K • 👍 139 • 💬 11 • ⏱️ 25:53 • 10h ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=hPHHGHYtFAY)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 2K • 👍 105 • ⏱️ 7:27 • 7h ago

---

**[SET ALERTS On Ethereum For These Signals! (Called +5587% In 2018)](https://www.youtube.com/watch?v=1oDqjqLy7Qo)**

Join Trade Confident: Get 25% Off Your 1st Month: https://tinyurl.com/tcmembergift • Weekly Market Forecasts • Monthly Zoom Call ...

📺 Trade Confident

👁️ 343 • 👍 11 • 💬 1 • ⏱️ 5:45 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
