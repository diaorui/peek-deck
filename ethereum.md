---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-17T14:04:18.101165+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- videos
- social
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 17, 2026 at 14:04 UTC  
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

### $2,193.43

---

## Ethereum Chart

**24h:** +0.5%  
**7d:** -6.4%  
**30d:** -6.8%  
**90d:** +10.0%  
**1y:** -12.3%  

---

## Ethereum Market Stats

**Market Cap:** $264.28B
Rank #2

**Circulating Supply:** 120,685,789 ETH
No max supply

**All-Time High:** $4,946.05
-55.7%

**All-Time Low:** $0.43
+505647.4%

---

## Reddit: r/ethereum

**[Daily General Discussion May 17, 2026](https://www.reddit.com/r/ethereum/comments/1tffsqu/daily_general_discussion_may_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

9h ago

---

**[Build projects or learn Uniswap v4 ??](https://www.reddit.com/r/ethereum/comments/1tfq5kj/build_projects_or_learn_uniswap_v4/)**

Heyy Guys, im back from learning foundry and next looking to build some projects and host them in the testnet. I was thinking of building a standard and solid project (like DAO/DEX) instead of small projects.. So when i looked up, i came to know that uniswap is very useful in developing commercial level projects and has many built-in features ideal for production grade apps.. Now should i learn Uniswap and then build a solid project or just build a project and then learn Uniswap.. Thanks in advance...

12m ago

---

**[Instant way to Unstake stETH?](https://www.reddit.com/r/ethereum/comments/1tf06ed/instant_way_to_unstake_steth/)**

I am trying to unstake through Lido but the withdrawal queue is showing multiple days, tried a small amount and my steth just disappeared and i received a weird NFT Is there currently a instant way to Unstake Lido ETH / a cheap way to do that? It's so frustrating

20h ago

---

**[Daily General Discussion May 16, 2026](https://www.reddit.com/r/ethereum/comments/1tejwhl/daily_general_discussion_may_16_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[How do you get yields/interests on USDC?](https://www.reddit.com/r/ethereum/comments/1tey6g1/how_do_you_get_yieldsinterests_on_usdc/)**

I hold Bitcoin and Ethereum and USDC on the side that aren't moving/being used at all, I'd like to "stake" some of it in order to get extra %/free money. I've started digging how to do it safely (without involving a CEX) but every guide either points to coinbase/kraken... Is there a non-custodial way to Stake USDC? What are you guys using for it?

21h ago

---

**[Architectural Breakdown: EVM Events, Transaction Receipts, and RPC Log Filtering](https://www.reddit.com/r/ethereum/comments/1tepe86/architectural_breakdown_evm_events_transaction/)**

Events (logs) are the EVM’s native asynchronous data pipeline, but they are fundamentally distinct from contract storage. Instead of modifying the state trie, events write directly to the transaction receipt trie. This structural separation is what makes them highly gas-efficient for off-chain indexing. Under the hood, an emitted event is partitioned into topics and data: Topics are the search keys: Capped at 4 topics per log. Topic[0] is always the keccak256 hash of the event signature (e.g., Transfer(address,address,uint256)). Topic[1] through Topic[3] are your indexed parameters, padded to fixed 32-byte values. This allows RPC nodes to build bloom filters, enabling highly efficient eth_getLogs queries over millions of blocks without reading the full log payload. Data (The Blob): All non-indexed parameters are ABI-encoded into a single raw byte string. While cheaper in gas, this data is strictly unsearchable at the RPC layer; you must fetch the raw log and decode it client-side. When querying an RPC provider via eth_getLogs, you are searching against these bloom filters. Passing an array of topics in your RPC call allows for direct intersection matching to isolate specific contract interactions without touching the execution environment. Source/Full Breakdown:https://andreyobruchkov1996.substack.com/p/understanding-events-the-evms-built Since event logs aren't accessible from within smart contracts, how would you securely prove to a downstream L1 contract that a specific event was emitted on an L2 roll-up without relying on a trusted centralized indexer?

1d ago

---

**[Ethereal news weekly #23 | Clear signing, CLARITY Act advanced out of Senate Banking committee, Ben Edgington fast finality plan](https://www.reddit.com/r/ethereum/comments/1tdy4x1/ethereal_news_weekly_23_clear_signing_clarity_act/)**

Clear signing, CLARITY Act advanced out of Senate Banking committee, Ben Edgington fast finality plan

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-23/) • 1d ago

---

**[Daily General Discussion May 15, 2026](https://www.reddit.com/r/ethereum/comments/1tdm9xw/daily_general_discussion_may_15_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[put $2.5k into a mid-cap through a dex and walked away $180 short, what went wrong?](https://www.reddit.com/r/ethereum/comments/1tdr5oj/put_25k_into_a_midcap_through_a_dex_and_walked/)**

swapped $2.5k worth of ETH into a mid-cap token recently. the preview showed 3% slippage, I set my tolerance to 4% and went ahead. came out $183 below the quoted amount. the pool showed roughly $800k in 24h volume so I assumed it was fine. I s this expected at this size or did I mess something up?

2d ago

---

**[Without stablecoin treasury yield, defi is a proof that finance is zero sum](https://www.reddit.com/r/ethereum/comments/1tdp2jc/without_stablecoin_treasury_yield_defi_is_a_proof/)**

2d ago

---

---

## Google News: "ethereum"

**[Justin Sun-Led Liberland Micronation Awards Ethereum Founder Vitalik Buterin Its Top Honor](https://decrypt.co/368116/justin-sun-liberland-awards-ethereum-founder-vitalik-buterin-top-honor)**

The micronation honored Vitalik Buterin during ETH Prague 2026 as it continued promoting blockchain-based governance and digital citizenship.

Decrypt • 20h ago

---

**[XRP and Solana ETFs Keep Pulling Inflows While Ethereum ETFs Bleed](https://247wallst.com/investing/2026/05/15/xrp-and-solana-etfs-keep-pulling-inflows-while-ethereum-etfs-bleed/)**

Ethereum spot ETFs bled $189M across 4 days while XRP and Solana ETFs kept pulling inflows—even as the CLARITY Act passed.

24/7 Wall St. • 1d ago

---

**[Harvard Dumps Its Ethereum and Bitcoin ETF Investment](https://finance.yahoo.com/markets/crypto/articles/harvard-dumps-ethereum-bitcoin-etf-103709099.html)**

Harvard's endowment slashes its Bitcoin ETF stake 43% and exits Ethereum, while Abu Dhabi's Mubadala adds to IBIT.

Yahoo Finance • 3h ago

---

**[XRP Is Crushing Ethereum and Solana in 1 Key Area, but Will It Matter for Holders?](https://www.fool.com/investing/2026/05/17/xrp-is-crushing-ethereum-and-solana-in-1-key-area/)**

Success for a blockchain isn't always the same as success for investors.

The Motley Fool • 3h ago

---

**[Ethereum Triangle Breakdown Adds Pressure On Its Recovery Outlook](https://www.tradingview.com/news/newsbtc:367940313094b:0-ethereum-triangle-breakdown-adds-pressure-on-its-recovery-outlook/)**

Ethereum pressure mounts as the ETHBTC pair breaks down from a key descending triangle structure. The weakening performance against Bitcoin suggests that bearish momentum may still be dominating the market, leaving Ethereum vulnerable to deeper pullbacks unless bulls quickly reclaim critical resist…

TradingView • 11h ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 2d ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Jump After Crypto Act Passes Key Senate Vote: Analyst Says BTC 'Positioned' For A Rebound Toward $86,000](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-dogecoin-jump-015048079.html)**

Leading cryptocurrencies were up in the green on Thursday after the Clarity Act passed the Senate Banking Committee on a bipartisan vote. Cryptocurrency24-Hour Gains +/-Price (Recorded at 9:05 p.m. EDT)Bitcoin (CRYPTO: BTC)+2.46%$81,561.50Ethereum (CRYPTO: ETH) +1.18%$2,293.12XRP (CRYPTO: XRP) +4.49%$1.49Solana (CRYPTO: SOL) +1.33%$92.42Dogecoin (CRYPTO: DOGE) +2.10%$0.1167 Crypto Market Pops Bitcoin hit $82,000 in the afternoon, then stalled and moved sideways. The trading volume soared 27% in

Yahoo Finance • 2d ago

---

**[Congress's New Crypto Bill Has Traditional Banks Terrified—and Could Change How Our Economy Works](https://www.inc.com/brian-contreras/congresss-new-crypto-bill-banks-economy-trump-bitcoin-ethereum-stablecoins/91344970)**

The Clarity Act would be a boon for backers of Bitcoin, Ethereum and stablecoins. But not everyone is on board.

inc.com • 2d ago

---

**[Analyst Reveals What CLARITY Act Passing Today Means for Bitcoin, Ethereum and XRP Prices](https://coinpedia.org/news/analyst-reveals-what-clarity-act-passing-today-means-for-bitcoin-ethereum-and-xrp-prices/)**

Coinpedia • 2d ago

---

**[Corporate Ethereum reserves reach $16B as companies stockpile 7.3M ETH](https://cryptobriefing.com/corporate-ethereum-reserves-16-billion/)**

Public companies now hold 7.3M ETH worth nearly $16B on their balance sheets, driven by staking yields and DeFi returns as corporate adoption accelerates.

Crypto Briefing • 23h ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee: &quot;Ethereum To $444,000 In The Next Few Years - How ETH Could Realistically 120x&quot; | 2026](https://www.youtube.com/watch?v=nUp6xKbaL_Q)**

Our FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Library Of Wealth

👁️ 4K • 👍 119 • 💬 101 • ⏱️ 15:37 • 1d ago

---

**[If Ethereum Does This We&#39;re Going To Have The Best Altcoin Season Ever Made In 2026](https://www.youtube.com/watch?v=SovKhWex5q0)**

Even crypto investors dont seem to understand the amount of money and wealth there are to be made from this market. Estimates ...

📺 The Modern Investor

👁️ 2K • 👍 406 • 💬 116 • ⏱️ 32:55 • 4h ago

---

**[BITCOIN &amp; ALTCOINS JUST BROKE (Get Ready)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=Q-W7ekx-zGs)**

BITCOIN & ALTCOINS JUST BROKE (Get Ready)!!! - Bitcoin News Today, Ethereum & Altcoins ⭐ *WEEX* https://bit.ly/WEEX1 ...

📺 Crypto World

👁️ 7K • 👍 334 • 💬 113 • ⏱️ 18:50 • 11h ago

---

**[&quot;Ethereum To $12,000,  Bitcoin To $250,000 - Here&#39;s WHY&quot; Tom Lee | Crypto Prediction 2026](https://www.youtube.com/watch?v=zQGTvz_2YM4)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 14K • 👍 469 • 💬 50 • ⏱️ 18:57 • 2d ago

---

**[Ethereum’s Institutional Era Has Arrived](https://www.youtube.com/watch?v=b7xVgaG0o-w)**

Sharplink CEO Joseph Chalom joins Gareth Jenkinson at Consensus to explain why SharpLink has taken an institutional-first ...

📺 The Block

👁️ 7K • 👍 159 • 💬 45 • ⏱️ 13:36 • 2d ago

---

**[SET ALERTS On Ethereum For These Signals! (Called +5587% In 2018)](https://www.youtube.com/watch?v=1oDqjqLy7Qo)**

Join Trade Confident: Get 25% Off Your 1st Month: https://tinyurl.com/tcmembergift • Weekly Market Forecasts • Monthly Zoom Call ...

📺 Trade Confident

👁️ 459 • 👍 13 • 💬 12 • ⏱️ 5:45 • 1d ago

---

**[Clarity Passes, Stocks Rip, &amp; Wall Street Piles Into Ethereum](https://www.youtube.com/watch?v=2_TwBsL3U9o)**

GALAXY | INSTITUTIONAL DIGITAL FINANCE https://bankless.cc/Galaxy --- Markets are ignoring every warning sign as stocks hit ...

📺 Bankless

👁️ 7K • 👍 231 • 💬 35 • ⏱️ 1:05:23 • 2d ago

---

**[ETHEREUM BUY TARGET SOON!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=mREX7HVUtJ4)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 770 • 👍 32 • 💬 2 • ⏱️ 4:43 • 1d ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin: Crypto Update &amp; Targets](https://www.youtube.com/watch?v=IDLjsyUACLI)**

Bitcoin soared to $81000, hitting the 200-day moving average. But is it a bull trap? Analysis suggests a potential deeper correction ...

📺 CryptoMeownalysis

👁️ 52 • 👍 3 • 💬 1 • ⏱️ 8:52 • 23h ago

---

**[ETH Supply Shock Could Send Ethereum To $20K Explained](https://www.youtube.com/watch?v=7WiPJ8CUCo8)**

Tom Lee says Ethereum could eventually reach $20000+ Explained Earn $ETH with MaxFi - https://www.maxfi.tech/ Big Time ...

📺 Big Time Trades

👁️ 3K • 👍 86 • 💬 45 • ⏱️ 23:46 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
