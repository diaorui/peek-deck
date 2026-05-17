---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-17T20:53:24.636255+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- social
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 17, 2026 at 20:53 UTC  
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

### $2,185.92

---

## Ethereum Chart

**24h:** +0.3%  
**7d:** -6.4%  
**30d:** -6.8%  
**90d:** +10.0%  
**1y:** -12.3%  

---

## Ethereum Market Stats

**Market Cap:** $264.16B
Rank #2

**Circulating Supply:** 120,685,789 ETH
No max supply

**All-Time High:** $4,946.05
-55.7%

**All-Time Low:** $0.43
+505915.3%

---

## Reddit: r/ethereum

**[Cheapest way to convert stETH to ETH?](https://www.reddit.com/r/ethereum/comments/1tfvisj/cheapest_way_to_convert_steth_to_eth/)**

I had no idea the Lido withdrawal process was this painful. Submitted my unstake request and got some NFT back, then waited 18 days just to manually claim my ETH. Missed the whole reason I needed it in the first place. Is there a faster way to get ETH out of a stETH position or is this just how it works? Feels like there has to be something I'm missing. Thanks

3h ago

---

**[Daily General Discussion May 17, 2026](https://www.reddit.com/r/ethereum/comments/1tffsqu/daily_general_discussion_may_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

15h ago

---

**[Uniswap alternative for large swaps?](https://www.reddit.com/r/ethereum/comments/1tfy50a/uniswap_alternative_for_large_swaps/)**

Hi everyone, been using Uniswap for a while now but every time I try to swap anything above $10k the price impact just kills me. Did a $14k ETH to USDC swap last week and lost around $300 to slippage alone which seems way too much for such a common pair. Is there a better option for larger amounts or is there something I should be setting differently? Any advice appreciated!

2h ago

---

**[Build projects or learn Uniswap v4 ??](https://www.reddit.com/r/ethereum/comments/1tfq5kj/build_projects_or_learn_uniswap_v4/)**

Heyy Guys, im back from learning foundry and next looking to build some projects and host them in the testnet. I was thinking of building a standard and solid project (like DAO/DEX) instead of small projects.. So when i looked up, i came to know that uniswap is very useful in developing commercial level projects and has many built-in features ideal for production grade apps.. Now should i learn Uniswap and then build a solid project or just build a project and then learn Uniswap.. Thanks in advance...

7h ago

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

**[XRP and Solana ETFs Keep Pulling Inflows While Ethereum ETFs Bleed](https://247wallst.com/investing/2026/05/15/xrp-and-solana-etfs-keep-pulling-inflows-while-ethereum-etfs-bleed/)**

Ethereum spot ETFs bled $189M across 4 days while XRP and Solana ETFs kept pulling inflows—even as the CLARITY Act passed.

24/7 Wall St. • 2d ago

---

**[Japan’s Biggest Brokerages Open a New Door for Bitcoin and Ethereum Investment](https://finance.yahoo.com/markets/crypto/articles/japan-biggest-brokerages-open-door-185114630.html)**

SBI, Rakuten and Nomura plan Bitcoin and Ethereum investment trusts, opening crypto access for Japanese investors.

Yahoo Finance • 2h ago

---

**[$5,000 in XRP vs $5,000 in Ethereum: Which Returns More by 2028?](https://finance.yahoo.com/markets/crypto/articles/5-000-xrp-vs-5-194612174.html)**

A $5,000 bet on XRP (CRYPTO: XRP) or Ethereum (CRYPTO: ETH) today could look very different by 2028, and the difference between the two investments is wider than most people expect. XRP has momentum behind it, Ripple’s payments business keeps growing, and the regulatory pressure that crushed the token for years has mostly faded. Meanwhile, ... $5,000 in XRP vs $5,000 in Ethereum: Which Returns More by 2028?

Yahoo Finance • 1h ago

---

**[XRP Is Crushing Ethereum and Solana in 1 Key Area, but Will It Matter for Holders?](https://www.fool.com/investing/2026/05/17/xrp-is-crushing-ethereum-and-solana-in-1-key-area/)**

Success for a blockchain isn't always the same as success for investors.

The Motley Fool • 9h ago

---

**[Ethereum Triangle Breakdown Adds Pressure On Its Recovery Outlook](https://www.tradingview.com/news/newsbtc:367940313094b:0-ethereum-triangle-breakdown-adds-pressure-on-its-recovery-outlook/)**

Ethereum pressure mounts as the ETHBTC pair breaks down from a key descending triangle structure. The weakening performance against Bitcoin suggests that bearish momentum may still be dominating the market, leaving Ethereum vulnerable to deeper pullbacks unless bulls quickly reclaim critical resist…

TradingView • 17h ago

---

**[Ethereum hosts 72.6% of all tokenized ETFs as market eyes $20 trillion by 2030](https://cryptobriefing.com/ethereum-tokenized-etfs-market-dominance/)**

Ethereum commands 72.6% of all tokenized ETF products as the broader tokenization market targets $20 trillion by 2030. Here's why institutions keep choosing it.

Crypto Briefing • 7h ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 3d ago

---

**[NUVAFinance: $19B Figure RWA Assets on Ethereum](https://blockchain.news/flashnews/nuvafinance-19b-figure-rwa-assets-ethereum)**

NUVAFinance launches access to $19 billion Figure tokenized assets on Ethereum backed by Animoca Brands partnership.

blockchain.news • 20h ago

---

**[Crypto Today: Bitcoin, Ethereum, XRP edge down, testing support as resistance holds](https://www.fxstreet.com/cryptocurrencies/news/crypto-today-bitcoin-ethereum-xrp-edge-down-testing-support-as-resistance-holds-202605151200)**

Cryptocurrency prices are broadly correcting on Friday, following a failed attempt to recover losses incurred earlier in the week after the United States (US) Senate Banking Committee advanced the Digital Asset Market Clarity Act, commonly known as the Clarity Act of 2025.

FXStreet • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Gareth Soloway: Bitcoin &amp; BTC Bear Flag Warning — $49K Target, ETH, XRP, Crypto Breakdown 2026](https://www.youtube.com/watch?v=KJ35xjFGkXs)**

Is Bitcoin's bear flag about to trigger? Gareth Soloway, Chief Market Strategist at VerifiedInvesting.com, breaks down the LATEST ...

📺 Gareth Soloway

👁️ 29K • 👍 3K • 💬 245 • ⏱️ 12:17 • 6h ago

---

**[Raoul Pal :&quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” |  2026 Crypto Prediction](https://www.youtube.com/watch?v=XMa4ImNquPE)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 2K • 👍 145 • 💬 18 • ⏱️ 23:02 • 4h ago

---

**[🚨 BTC &amp; ETH: EXTREME WARNING TO EVERYONE!!!!!](https://www.youtube.com/watch?v=pXaVmd68Frw)**

This is not looking great for bitcoin, ethereum and the rest of crypto! Pay attention to these four main core macro pillars!

📺 Thomas Kralow

👁️ 7K • 👍 2K • 💬 22 • ⏱️ 10:04 • 5h ago

---

**[Tom Lee: &quot;Ethereum To $444,000 In The Next Few Years - How ETH Could Realistically 120x&quot; | 2026](https://www.youtube.com/watch?v=nUp6xKbaL_Q)**

Our FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Library Of Wealth

👁️ 5K • 👍 123 • 💬 101 • ⏱️ 15:37 • 1d ago

---

**[If Ethereum Does This We&#39;re Going To Have The Best Altcoin Season Ever Made In 2026](https://www.youtube.com/watch?v=SovKhWex5q0)**

Even crypto investors dont seem to understand the amount of money and wealth there are to be made from this market. Estimates ...

📺 The Modern Investor

👁️ 5K • 👍 589 • 💬 149 • ⏱️ 32:55 • 11h ago

---

**[Ethereum’s Institutional Era Has Arrived](https://www.youtube.com/watch?v=b7xVgaG0o-w)**

Sharplink CEO Joseph Chalom joins Gareth Jenkinson at Consensus to explain why SharpLink has taken an institutional-first ...

📺 The Block

👁️ 7K • 👍 167 • 💬 46 • ⏱️ 13:36 • 2d ago

---

**[BITCOIN: Warning to All Holders! (get ready) - BTC, ETH, XRP Price Prediction Today](https://www.youtube.com/watch?v=VU_ivlGex5M)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 2K • 👍 180 • 5h ago

---

**[BITCOIN &amp; ALTCOINS JUST BROKE (Get Ready)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=Q-W7ekx-zGs)**

BITCOIN & ALTCOINS JUST BROKE (Get Ready)!!! - Bitcoin News Today, Ethereum & Altcoins ⭐ *WEEX* https://bit.ly/WEEX1 ...

📺 Crypto World

👁️ 9K • 👍 368 • 💬 121 • ⏱️ 18:50 • 18h ago

---

**[Clarity Passes, Stocks Rip, &amp; Wall Street Piles Into Ethereum](https://www.youtube.com/watch?v=2_TwBsL3U9o)**

GALAXY | INSTITUTIONAL DIGITAL FINANCE https://bankless.cc/Galaxy --- Markets are ignoring every warning sign as stocks hit ...

📺 Bankless

👁️ 7K • 👍 241 • 💬 35 • ⏱️ 1:05:23 • 2d ago

---

**[ETH ожидания #eth #ethereum #crypto](https://www.youtube.com/watch?v=32zkWVYcaUM)**

tg romchekcrypto ETH ожидания.

📺 Новые деньги Криптовалюты Биткоин

👁️ 501 • 👍 23 • 💬 2 • ⏱️ 1:04 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
