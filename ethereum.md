---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2025-12-21T20:50:28.479747+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- cryptocurrency
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** December 21, 2025 at 20:50 UTC  
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

### $2,989.50

---

## Ethereum Chart

**24h:** +0.3%  
**7d:** +0.8%  
**30d:** +7.6%  
**90d:** -28.5%  
**1y:** -8.8%  

---

## Ethereum Market Stats

**Market Cap:** $360.89B
Rank #2

**Circulating Supply:** 120,695,010 ETH
No max supply

**All-Time High:** $4,946.05
-39.5%

**All-Time Low:** $0.43
+690993.6%

---

## Reddit: r/ethereum

**[Daily General Discussion December 21, 2025](https://www.reddit.com/r/ethereum/comments/1przbh3/daily_general_discussion_december_21_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

14h ago

---

**[Tx-dependency trie for parallel block production and validation](https://www.reddit.com/r/ethereum/comments/1ps7nwg/txdependency_trie_for_parallel_block_production/)**

I was recently threatened with a ban for mentioning one thing I think is neglected in scaling, so I assume I will not mention that here. But another important thing, is parallel contract execution. This is probably a topic many people here have expertise on since upwards 10 years, and thus something where those with expertise can share, or when there is unsolved problems, there can be discussion. Ethereum in 2014 ordered all transactions in a block sequentially in the transaction-trie (sequence number as key in trie). It seems an upgrade from that to parallel execution could be the "transaction dependency trie". Where the keys are the number of dependencies (from 0 and upwards), and then each key stores a nested trie with the transactions. Block validators can them simply run transactions in order of dependencies. This trie can be constructed based on read/writes of storage slots. It also seems meaningful with the old flat storage trie idea, which I assume was always about parallelization. It could have "storage objects" that each contain a trie where the keys are storage slots, and storage slots can contain pointers to storage objects. Thus you can have mappings and arrays and such that can be operated on in parallel by shards (I will avoid mentioning my other idea on how such sharding should be organized, as I am threatened with a ban if I do, although it would be easier if moderation here could moderate itself to behave more in line with normal civil discourse). Such is quite easily shardable it seems, arbitrarily (and how arbitrary sharding is allowed, is in that idea I am not allowed to mention by the moderator Edmund with support from Ligi who has publicly threatened a ban if I do). The key is shards can easily collaborate on assembling the Merkle roots for such tries, and mange ranges of keys (based on most significant bits), this has always been a known property of Patricia Merkle Tries. Why is parallelization important to me? Well I invented "video pseudonym parties" between 2015 and 2018 (Gavin Wood who alone built first version of Ethereum is currently approaching same idea and he calls it "proof-of-video-interaction") and it requires hundreds of thousands of transactions per second for 10 billion citizens. The whitepaper is public and published since 2018, it has been cited by MIT researched Bryan Ford in numerous publications, was in Frontiers and Bloomberg, and has been well known by "the community" (but it was originally invented together with a controversial organization). Note, inter-shard "mutexes" (which will be in contract code most likely) is part of such coordination too, but again, me being forbidden from mentioning the elephant in the room on sharding does make it harder to have a technical discussion, and it would be good if the moderation here could overrule that moderator's threat. I do not see how it is productive to forbid mentioning the elephant in the room on sharding, it ought to make it impossible to move past that bottleneck. Edit: The dependency trie probably needs storage slots nested under each transaction, and for multiple accesses sequential list, and then the transaction hash dependencies for each. The block validator has to run every transaction in parallel, but the dependency trie acts as implicit "mutex" for each point of contention, with no deadlocks as the block producer could run it. It is a bit complicated, but it seems it should work. The "number of dependencies" part in the trie can be skipped, it is meaningless. But it would be easier if I was not threatened with ban if I mention the elephant in the room in scaling, as it is important here in how the sharding is ideally organized (or, the only way it works in this current paradigm).

6h ago

---

**[Ever wanted to send an EIP-4844 blob?](https://www.reddit.com/r/ethereum/comments/1prnppx/ever_wanted_to_send_an_eip4844_blob/)**

1d ago

---

**[Daily General Discussion December 20, 2025](https://www.reddit.com/r/ethereum/comments/1pr76mk/daily_general_discussion_december_20_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Recovering old, mined ETH](https://www.reddit.com/r/ethereum/comments/1prob1d/recovering_old_mined_eth/)**

Hi! I mined some ETH around 2018 but I haven't touched it in a long time and I haven't been following the developments around ETH for a while. I started looking into it recently and was wondering if anybody has up to date advice on how best to recover the funds in my account? I found a backup folder on my PC that has a binary file starting with "UTC--" and also a doc where I had just saved a long hex value in it. I think the hex value is the wallet address which I used to access with nanopool, so I looked it up on etherscan and can see it still has some value in it. Is there anything else that I need? If a password is needed to decrypt the binary file, I'm not sure if I remember what that is, but if possible I could try to guess a few passwords I used to use...

1d ago

---

**[DTCC processed $3.7 quadrillion in 2024?? and they’re tokenizing U.S. treasuries now?? ON F*CKING CANTON???](https://www.reddit.com/r/ethereum/comments/1prnc2q/dtcc_processed_37_quadrillion_in_2024_and_theyre/)**

why tf is the biggest post-trade player picking a private-by-default network instead of Ethereum that everyone already uses?

🔗 [Daily Crypto Briefs](https://dailycryptobriefs.com/news/dtcc-tokenizes-us-treasuries-canton-network/) • 1d ago

---

**[Trust funds don’t exist where I live, can I substitute it with crypto?](https://www.reddit.com/r/ethereum/comments/1pqv5m1/trust_funds_dont_exist_where_i_live_can_i/)**

I live in Indonesia. Trust funds basically don’t exist here, and investing in foreign ETFs is messy (brokers, FX, income tax, reporting).Crypto is weirdly simpler. Trades here are taxed with a final tax (~0.1–0.2%) buy/sell and you’re done.That made me wonder: could smart contracts act like a low-cost “trust fund”? Rule-based investing (tokenized ETFs/T-bills), auto-rebalancing, monthly cash-outs to local currency, no banks or trustees. But maybe I’m missing something: - wallet loss / key management - smart contract risk - regulation catching up? Is there already a service for this use case?

2d ago

---

**[Daily General Discussion December 19, 2025](https://www.reddit.com/r/ethereum/comments/1pqdmmk/daily_general_discussion_december_19_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Getting Ethereum Ready for GigaGas](https://www.reddit.com/r/ethereum/comments/1pqhdeq/getting_ethereum_ready_for_gigagas/)**

Reproducible benchmarks reveal true Ethereum client throughput under real and extreme load, with Nethermind sustaining 2â10x higher performance.

🔗 [nethermind.io](https://www.nethermind.io/blog/getting-ethereum-ready-for-gigagas) • 2d ago

---

**[Why are dApps moving to ethereum?](https://www.reddit.com/r/ethereum/comments/1pqfnqo/why_are_dapps_moving_to_ethereum/)**

Why are dApps moving to Ethereum? Ethereum has a powerful "network effect" other L1s dont. Its the pioneer of smart contracts, has most users, deepest liquidity, and mature dev tools, making it the default "operating system" (via the EVM) for the decentralized web. ​The Fusaka upgrade solved the scalability bottleneck with PeerDAS to allow Ethereum to handle a massive increase in "blobs"—the specialized data packets used by rollups. This dropped L2 tx fees by another 50–90%, making it nearly impossible for "Ethereum Killers" to compete on cost alone. ​The Scalability Pivot: older chains tried to scale everything on one layer, Ethereum’s Fusaka and Pectra upgrades proved that a "modular" approach works. ​Interoperability: the roadmap moves towards shared sequencers and unified liquidity, the "fragmentation" between different L2s is beginning to dissolve, making the entire Ethereum ecosystem feel like one giant, seamless super-network.

2d ago

---

---

## Google News: "ethereum"

**[Ethereum’s 2026 ‘Hegota’ Upgrade Targets State Bloat and Fees](https://finance.yahoo.com/news/ethereum-2026-hegota-upgrade-targets-160129535.html)**

This week started shaky as we reacted to Federal Reserve uncertainty, but sentiment flipped fast. Ethereum surged nearly 2%, and confidence returned as macro data softened. Right from the start, the ongoing Bessent Warren dispute framed much of the conversation, especially as the Bitcoin price held firm despite volatility. But ...

Yahoo Finance • 4h ago

---

**[ETH news: Ethereum’s ‘Glamsterdam’ upgrade aims to fix MEV fairness](https://www.coindesk.com/tech/2025/12/20/ethereum-s-glamsterdam-upgrade-aims-to-fix-mev-fairness)**

The full scope of Glamsterdam has not yet been finalized, but developers are targeting it to go live in 2026.

CoinDesk • 1d ago

---

**[Ethereum developers name post-Glamsterdam upgrade 'Hegota' as 2026 roadmap takes shape](https://www.theblock.co/post/383275/ethereum-developers-name-post-glamsterdam-upgrade-hegota-as-2026-roadmap-takes-shape)**

The Block • 2d ago

---

**[Ethereum Foundation refocuses to security over speed – sets strict 128-bit rule for 2026](https://cryptoslate.com/ethereum-foundation-refocuses-to-security-over-speed-sets-strict-128-bit-rule-for-2026/)**

Speed is no longer enough: The Foundation warns that without formally verified soundness, attackers could rewrite state, rendering high-speed proving a critical liability.

CryptoSlate • 1d ago

---

**[Solana to Surpass Ethereum in Yearly Revenue](https://www.tradingview.com/news/u_today:85769ad66094b:0-solana-to-surpass-ethereum-in-yearly-revenue/)**

Solana founder Anatoly Yakovenko has shared new data that shows Solana has outperformed Ethereum in yearly revenue, highlighting what he sees as a pivotal shift in how value may be distributed across the crypto market.The infographics by DeFi Development Corp. show the projected chain revenue compa…

TradingView — Track All Markets • 19h ago

---

**[3 Predictions for Ethereum in 2026](https://www.fool.com/investing/2025/12/19/3-predictions-for-ethereum-eth-in-2026/)**

Next year could be good but won't be driven by blockchain tech upgrades.

The Motley Fool • 2d ago

---

**[BitMine Immersion Technologies (BMNR) Stock News Today: Ethereum Treasury Update, Insider Sale Filing, Analyst Forecasts, and What Comes Next (Dec. 19, 2025)](https://ts2.tech/en/bitmine-immersion-technologies-bmnr-stock-news-today-ethereum-treasury-update-insider-sale-filing-analyst-forecasts-and-what-comes-next-dec-19-2025/)**

BitMine Immersion Technologies (BMNR) Stock News Today: Ethereum Treasury Update, Insider Sale Filing, Analyst Forecasts, and What Comes Next (Dec. 19, 2025) - TechStock²

ts2.tech • 2d ago

---

**[Vitalik Warned of TRON Overtaking Ethereum—6 years Later, Here’s ETH vs. Tron](https://zycrypto.com/vitalik-warned-of-tron-overtaking-ethereum-6-years-later-heres-eth-vs-tron/)**

Six years ago, Ethereum co-founder Vitalik Buterin said he would respect a technically competent rival overtaking Ethereum.

ZyCrypto • 1d ago

---

**[SoFi Unveils Ethereum Stablecoin for Trading and Payments](https://decrypt.co/352815/sofi-unveils-ethereum-stablecoin-trading-and-payments)**

SoFi Technologies said that it will soon offer its own stablecoin on Ethereum, following the company’s re-entry into crypto last month.

Decrypt • 3d ago

---

**[Bitcoin vs. Ethereum vs. XRP – Which crypto will be 2026’s winner?](https://ambcrypto.com/bitcoin-vs-ethereum-vs-xrp-which-crypto-will-be-2026s-winner/)**

ETF flows and on-chain data reveal sharply diverging setups for Bitcoin, Ethereum, and XRP.

AMBCrypto • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee&#39;s Fundstrat Sees $60K BTC $1.8k ETH and $50 SOL In H1 2026... Stablecoin Battle, BTC ETF...](https://www.youtube.com/watch?v=PrjHeXsAGfE)**

Welcome back for another daily market update as always this will be a jam packed one! Join the Patreon and get exclusive ...

📺 AllinCrypto

👁️ 7K • 👍 504 • 💬 377 • ⏱️ 11:34 • 7h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=stp8NpOeNj8)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 107 • 💬 8 • ⏱️ 4:12 • 5h ago

---

**[Tom Lee Warns HUGE BMNR &amp; ETH CRASH  in 2026](https://www.youtube.com/watch?v=WxO07sZvBFY)**

BMNR #bitmine #bmnr #tomlee #ethereum $ETH $BTC #btc #bitcoin Please Drop a Like & Subscribe if you enjoyed this video: ...

📺 Tevis

👁️ 18K • 👍 1K • 💬 256 • ⏱️ 35:41 • 20h ago

---

**[Ethereum Is Approaching a Key Level — Big Move Coming?](https://www.youtube.com/watch?v=35KwTlk-t70)**

Follow My Live Trades   https://kingcobratrade.com/vip/ Join the free discord https://discord.gg/AcpwbgTMYc TELEGRAM ...

📺 Crypto Cobra

👁️ 464 • 👍 38 • 💬 13 • ⏱️ 14:27 • 3h ago

---

**[WILL ETH BREAKOUT NEXT WEEK?🔥 (ETH Price Prediction 2025)](https://www.youtube.com/watch?v=b_vOMteFZts)**

ETHEREUM ETH PRICE PREDICTION 2025 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 261 • 👍 16 • 💬 1 • ⏱️ 5:02 • 10h ago

---

**[Is Ethereum Massively Overvalued? w/ Haseeb Qureshi](https://www.youtube.com/watch?v=DzS0ldchsps)**

In this episode, Haseeb Qureshi breaks down the viral debate that split Crypto Twitter: Should blockchains be valued like ...

📺 Milk Road

👁️ 3K • 👍 84 • 💬 101 • ⏱️ 11:26 • 1d ago

---

**[Crypto Altcoin Technical Analysis: Ethereum, Solana, XRP, Cardano, Avalanche, Chainlink And More](https://www.youtube.com/watch?v=b-yhuBpnzfg)**

Chief Market Strategist Gareth Soloway uses technical analysis to give his near-term forecasts on altcoins like Ethereum (ETH), ...

📺 Gareth Soloway

👁️ 5K • 👍 784 • 💬 33 • ⏱️ 16:45 • 3h ago

---

**[&quot;My Top 5 Honest Predictions for BTC, SOL &amp; ETH in 2026&quot;- Matt Hougan](https://www.youtube.com/watch?v=LJnaNv3Fuuo)**

Trade Crypto, Gold, and Silver 24/7 with tax advantages, 1% fees, top security, and easy sign-up—start now!

📺 Savvy Finance

👁️ 14K • 👍 509 • 💬 14 • ⏱️ 21:53 • 2d ago

---

**[Whales Are Buying Ethereum  Retail Is Selling](https://www.youtube.com/watch?v=MFBeoCbJwM8)**

Ethereum is getting wrecked — down 40%+ from its recent peak — while Bitcoin is down ~30%. But here's the twist: retail is ...

📺 Ryan’s Money Lab

👁️ 3K • 👍 143 • 💬 17 • ⏱️ 14:00 • 1d ago

---

**[BMNR Stock &amp; ETH Technical Analysis Prediction | Tom Lee’s BitMine Set For Monster Q1 Move!](https://www.youtube.com/watch?v=-DWATwifb1Y)**

ethereum #bmnr #bitcoin In this video, I break down why BMNR stock and Ethereum are setting up for a major move into January ...

📺 alliseeisW 

👁️ 2K • 👍 76 • 💬 116 • ⏱️ 9:51 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
