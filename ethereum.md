---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-18T04:23:39.261563+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- videos
- cryptocurrency
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 18, 2026 at 04:23 UTC  
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

### $2,097.42

---

## Ethereum Chart

**24h:** -3.1%  
**7d:** -6.9%  
**30d:** -6.4%  
**90d:** +8.3%  
**1y:** -16.4%  

---

## Ethereum Market Stats

**Market Cap:** $255.76B
Rank #2

**Circulating Supply:** 120,685,747 ETH
No max supply

**All-Time High:** $4,946.05
-57.2%

**All-Time Low:** $0.43
+489249.4%

---

## Reddit: r/ethereum

**[Uniswap alternative for large swaps?](https://www.reddit.com/r/ethereum/comments/1tfy50a/uniswap_alternative_for_large_swaps/)**

Hi everyone, been using Uniswap for a while now but every time I try to swap anything above $10k the price impact just kills me. Did a $14k ETH to USDC swap last week and lost around $300 to slippage alone which seems way too much for such a common pair. Is there a better option for larger amounts or is there something I should be setting differently? Any advice appreciated!

9h ago

---

**[Cheapest way to convert stETH to ETH?](https://www.reddit.com/r/ethereum/comments/1tfvisj/cheapest_way_to_convert_steth_to_eth/)**

I had no idea the Lido withdrawal process was this painful. Submitted my unstake request and got some NFT back, then waited 18 days just to manually claim my ETH. Missed the whole reason I needed it in the first place. Is there a faster way to get ETH out of a stETH position or is this just how it works? Feels like there has to be something I'm missing. Thanks

11h ago

---

**[Daily General Discussion May 17, 2026](https://www.reddit.com/r/ethereum/comments/1tffsqu/daily_general_discussion_may_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

23h ago

---

**[Build projects or learn Uniswap v4 ??](https://www.reddit.com/r/ethereum/comments/1tfq5kj/build_projects_or_learn_uniswap_v4/)**

Heyy Guys, im back from learning foundry and next looking to build some projects and host them in the testnet. I was thinking of building a standard and solid project (like DAO/DEX) instead of small projects.. So when i looked up, i came to know that uniswap is very useful in developing commercial level projects and has many built-in features ideal for production grade apps.. Now should i learn Uniswap and then build a solid project or just build a project and then learn Uniswap.. Thanks in advance...

14h ago

---

**[Instant way to Unstake stETH?](https://www.reddit.com/r/ethereum/comments/1tf06ed/instant_way_to_unstake_steth/)**

I am trying to unstake through Lido but the withdrawal queue is showing multiple days, tried a small amount and my steth just disappeared and i received a weird NFT Is there currently a instant way to Unstake Lido ETH / a cheap way to do that? It's so frustrating

1d ago

---

**[How do you get yields/interests on USDC?](https://www.reddit.com/r/ethereum/comments/1tey6g1/how_do_you_get_yieldsinterests_on_usdc/)**

I hold Bitcoin and Ethereum and USDC on the side that aren't moving/being used at all, I'd like to "stake" some of it in order to get extra %/free money. I've started digging how to do it safely (without involving a CEX) but every guide either points to coinbase/kraken... Is there a non-custodial way to Stake USDC? What are you guys using for it?

1d ago

---

**[Daily General Discussion May 16, 2026](https://www.reddit.com/r/ethereum/comments/1tejwhl/daily_general_discussion_may_16_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Architectural Breakdown: EVM Events, Transaction Receipts, and RPC Log Filtering](https://www.reddit.com/r/ethereum/comments/1tepe86/architectural_breakdown_evm_events_transaction/)**

Events (logs) are the EVM’s native asynchronous data pipeline, but they are fundamentally distinct from contract storage. Instead of modifying the state trie, events write directly to the transaction receipt trie. This structural separation is what makes them highly gas-efficient for off-chain indexing. Under the hood, an emitted event is partitioned into topics and data: Topics are the search keys: Capped at 4 topics per log. Topic[0] is always the keccak256 hash of the event signature (e.g., Transfer(address,address,uint256)). Topic[1] through Topic[3] are your indexed parameters, padded to fixed 32-byte values. This allows RPC nodes to build bloom filters, enabling highly efficient eth_getLogs queries over millions of blocks without reading the full log payload. Data (The Blob): All non-indexed parameters are ABI-encoded into a single raw byte string. While cheaper in gas, this data is strictly unsearchable at the RPC layer; you must fetch the raw log and decode it client-side. When querying an RPC provider via eth_getLogs, you are searching against these bloom filters. Passing an array of topics in your RPC call allows for direct intersection matching to isolate specific contract interactions without touching the execution environment. Source/Full Breakdown:https://andreyobruchkov1996.substack.com/p/understanding-events-the-evms-built Since event logs aren't accessible from within smart contracts, how would you securely prove to a downstream L1 contract that a specific event was emitted on an L2 roll-up without relying on a trusted centralized indexer?

1d ago

---

**[Ethereal news weekly #23 | Clear signing, CLARITY Act advanced out of Senate Banking committee, Ben Edgington fast finality plan](https://www.reddit.com/r/ethereum/comments/1tdy4x1/ethereal_news_weekly_23_clear_signing_clarity_act/)**

Clear signing, CLARITY Act advanced out of Senate Banking committee, Ben Edgington fast finality plan

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-23/) • 2d ago

---

**[Daily General Discussion May 15, 2026](https://www.reddit.com/r/ethereum/comments/1tdm9xw/daily_general_discussion_may_15_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Justin Sun-Led Liberland Micronation Awards Ethereum Founder Vitalik Buterin Its Top Honor](https://decrypt.co/368116/justin-sun-liberland-awards-ethereum-founder-vitalik-buterin-top-honor)**

The micronation honored Vitalik Buterin during ETH Prague 2026 as it continued promoting blockchain-based governance and digital citizenship.

Decrypt • 1d ago

---

**[Harvard Just Cut Its Bitcoin and Ethereum Investment](https://beincrypto.com/harvard-dumps-bitcoin-ethereum-investment/)**

Harvard's endowment slashes its Bitcoin ETF stake 43% and exits Ethereum, while Abu Dhabi's Mubadala adds to IBIT.

BeInCrypto • 17h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Fall Amid Trump's 'Clock Is Ticking' Iran Warning: Analyst Says BTC Can Slip If This 'Important' Support Is Lost](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-dogecoin-fall-023535283.html)**

Leading cryptocurrencies plunged alongside stock futures on Sunday evening after President Donald Trump’s latest warning to Iran spooked investors. Cryptocurrency24-Hour Gains +/-Price (Recorded at 9:20 p.m. EDT)Bitcoin (CRYPTO: BTC)-1.37%$76,959.12Ethereum (CRYPTO: ETH) -3.24%$2,110.19XRP (CRYPTO: XRP) -1.22%$1.39Solana (CRYPTO: SOL) -1.06%$85.35Dogecoin (CRYPTO: DOGE) -2.14%$0.1067 Crypto Market Sinks Bitcoin dived below $77,000 late in the evening, while trading volume plunged 13% in the 24 h

Yahoo Finance • 1h ago

---

**[XRP Is Crushing Ethereum and Solana in 1 Key Area, but Will It Matter for Holders?](https://www.fool.com/investing/2026/05/17/xrp-is-crushing-ethereum-and-solana-in-1-key-area/)**

Success for a blockchain isn't always the same as success for investors.

The Motley Fool • 17h ago

---

**[Ethereum Triangle Breakdown Adds Pressure On Its Recovery Outlook](https://www.tradingview.com/news/newsbtc:367940313094b:0-ethereum-triangle-breakdown-adds-pressure-on-its-recovery-outlook/)**

Ethereum pressure mounts as the ETHBTC pair breaks down from a key descending triangle structure. The weakening performance against Bitcoin suggests that bearish momentum may still be dominating the market, leaving Ethereum vulnerable to deeper pullbacks unless bulls quickly reclaim critical resist…

TradingView • 1d ago

---

**[Ethereum hosts 72.6% of all tokenized ETFs as market eyes $20 trillion by 2030](https://cryptobriefing.com/ethereum-tokenized-etfs-market-dominance/)**

Ethereum commands 72.6% of all tokenized ETF products as the broader tokenization market targets $20 trillion by 2030. Here's why institutions keep choosing it.

Crypto Briefing • 14h ago

---

**[Congress's New Crypto Bill Has Traditional Banks Terrified—and Could Change How Our Economy Works](https://www.inc.com/brian-contreras/congresss-new-crypto-bill-banks-economy-trump-bitcoin-ethereum-stablecoins/91344970)**

The Clarity Act would be a boon for backers of Bitcoin, Ethereum and stablecoins. But not everyone is on board.

inc.com • 3d ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 3d ago

---

**[Ethereum News: Ronin’s Ethereum L2 Migration Is Bigger Than It Looks for ETH](https://www.aol.com/articles/ethereum-news-ronin-ethereum-l2-223706000.html)**

Every few months, a move in the broader crypto space quietly signals something important about where Ethereum (CRYPTO: ETH) is headed. Ronin’s completed migration from an independent sidechain to a full Ethereum Layer 2 on May 12, 2026, is one of those moves. On the surface, it reads as a gaming chain upgrade. But Ronin ... Ethereum News: Ronin’s Ethereum L2 Migration Is Bigger Than It Looks for ETH

AOL.com • 5h ago

---

**[Ethereum Price Prediction: Why ETH Needs to Clear $2,400 by End of May](https://247wallst.com/investing/2026/05/15/ethereum-price-prediction-why-eth-needs-to-clear-2400-by-end-of-may/)**

Ethereum trades at $2,223, around 8% from $2,400. Here's why the $2.4K level matters and what could push the ETH price through it.

24/7 Wall St. • 2d ago

---

---

## YouTube Videos: "ethereum"

**[🚨 BTC &amp; ETH: EXTREME WARNING TO EVERYONE!!!!!](https://www.youtube.com/watch?v=pXaVmd68Frw)**

This is not looking great for bitcoin, ethereum and the rest of crypto! Pay attention to these four main core macro pillars!

📺 Thomas Kralow

👁️ 20K • 👍 2K • 💬 62 • ⏱️ 10:04 • 12h ago

---

**[Raoul Pal :&quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” |  2026 Crypto Prediction](https://www.youtube.com/watch?v=XMa4ImNquPE)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 11K • 👍 308 • 💬 37 • ⏱️ 23:02 • 12h ago

---

**[Tom Lee: &quot;Ethereum To $444,000 In The Next Few Years - How ETH Could Realistically 120x&quot; | 2026](https://www.youtube.com/watch?v=nUp6xKbaL_Q)**

Our FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Library Of Wealth

👁️ 5K • 👍 127 • 💬 102 • ⏱️ 15:37 • 1d ago

---

**[Gareth Soloway: Bitcoin &amp; BTC Bear Flag Warning — $49K Target, ETH, XRP, Crypto Breakdown 2026](https://www.youtube.com/watch?v=KJ35xjFGkXs)**

Is Bitcoin's bear flag about to trigger? Gareth Soloway, Chief Market Strategist at VerifiedInvesting.com, breaks down the LATEST ...

📺 Gareth Soloway

👁️ 58K • 👍 4K • 💬 243 • ⏱️ 12:17 • 14h ago

---

**[If Ethereum Does This We&#39;re Going To Have The Best Altcoin Season Ever Made In 2026](https://www.youtube.com/watch?v=SovKhWex5q0)**

Even crypto investors dont seem to understand the amount of money and wealth there are to be made from this market. Estimates ...

📺 The Modern Investor

👁️ 6K • 👍 671 • 💬 252 • ⏱️ 32:55 • 19h ago

---

**[Crypto Market Crash or Correction | BTC &amp; ETH Price Prediction Today | क्या होगा आगे?](https://www.youtube.com/watch?v=RQipsKqzMOY)**

BTC & ETH Price Prediction Today | Will Crypto Market Go Up or Down? | Hindi Analysis Premium on Telegram ...

📺 Crypto Gyan

👁️ 379 • 👍 62 • ⏱️ 7:30 • 1h ago

---

**[SET ALERTS On Ethereum For These Signals! (Called +5587% In 2018)](https://www.youtube.com/watch?v=1oDqjqLy7Qo)**

Join Trade Confident: Get 25% Off Your 1st Month: https://tinyurl.com/tcmembergift • Weekly Market Forecasts • Monthly Zoom Call ...

📺 Trade Confident

👁️ 490 • 👍 14 • 💬 12 • ⏱️ 5:45 • 2d ago

---

**[Ethereum tokenized money market fund](https://www.youtube.com/watch?v=6veNM0AALlk)**

BlackRock's launch of a tokenized money market fund on Ethereum marks a major step in bringing traditional financial products ...

📺 Andrew Shpanchuk | Web3 Builder

👁️ 558 • 👍 13 • 💬 1 • ⏱️ 0:44 • 8h ago

---

**[Ethereum’s Institutional Era Has Arrived](https://www.youtube.com/watch?v=b7xVgaG0o-w)**

Sharplink CEO Joseph Chalom joins Gareth Jenkinson at Consensus to explain why SharpLink has taken an institutional-first ...

📺 The Block

👁️ 7K • 👍 179 • 💬 47 • ⏱️ 13:36 • 2d ago

---

**[BITCOIN &amp; ALTCOINS JUST BROKE (Get Ready)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=Q-W7ekx-zGs)**

BITCOIN & ALTCOINS JUST BROKE (Get Ready)!!! - Bitcoin News Today, Ethereum & Altcoins ⭐ *WEEX* https://bit.ly/WEEX1 ...

📺 Crypto World

👁️ 10K • 👍 380 • 💬 149 • ⏱️ 18:50 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
