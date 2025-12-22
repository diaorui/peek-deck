---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2025-12-22T22:29:59.526678+00:00'
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

**Last Updated:** December 22, 2025 at 22:29 UTC  
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

### $2,981.92

---

## Ethereum Chart

**24h:** -0.4%  
**7d:** +0.9%  
**30d:** +6.6%  
**90d:** -27.8%  
**1y:** -12.7%  

---

## Ethereum Market Stats

**Market Cap:** $360.93B
Rank #2

**Circulating Supply:** 120,695,004 ETH
No max supply

**All-Time High:** $4,946.05
-39.5%

**All-Time Low:** $0.43
+690739.5%

---

## Reddit: r/ethereum

**[Daily General Discussion December 22, 2025](https://www.reddit.com/r/ethereum/comments/1pss4f5/daily_general_discussion_december_22_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

16h ago

---

**[Sending EIP-4844 Blob Transactions using ethers.js and kzg-wasm](https://www.reddit.com/r/ethereum/comments/1pt3u12/sending_eip4844_blob_transactions_using_ethersjs/)**

I just published a walkthrough on sending EIP-4844 blob transactions with ethers.js and kzg-wasm! If you’re curious about: How to send blobs on Ethereum today Working Sepolia RPC endpoints Using KZG commitments and proofs Attaching blobs to contract calls This guide takes you from setup to a full working example, including a TypeScript repo I built: https://github.com/0xKurt/eip-4844-ethers-examples

🔗 [medium.com](https://medium.com/@Kurt0x/sending-eip-4844-blob-transactions-using-ethers-js-and-kzg-wasm-d84224be6b81) • 6h ago

---

**[Many Web3 devs hear “OWASP” but what does it actually mean for smart contracts?](https://www.reddit.com/r/ethereum/comments/1psshj9/many_web3_devs_hear_owasp_but_what_does_it/)**

A lot of builders mention OWASP, but not everyone really knows what it stands for in a smart contract context. At a high level, the OWASP Smart Contract Top 10 is a security awareness standard that highlights the most common and most exploited vulnerabilities in production smart contracts. It’s not theoretical it’s based on what attackers actually use in the wild. Why it’s useful for devs > Helps identify common smart contract failure patterns > Acts as a prevention guide during development > Works as a checklist before audits or deployments > Gives teams a shared security baseline The 2025 OWASP Smart Contract Top 10 i covers issues like access control flaws, oracle manipulation, logic errors, reentrancy, flash loan attacks, insecure randomness, DoS, and more the same classes of bugs responsible for $1.4B+ in losses across 149 incidents in 2024. What makes the list solid is that it’s backed by real exploit data (loss reports, attack research, incident databases), not just best-guess rankings. Curious how many teams here actively reference OWASP during development or only look at it during audits? https://preview.redd.it/6zw9wba58p8g1.jpg?width=1280&format=pjpg&auto=webp&s=1a5a35edfaac83fed2c847383abb31793a8c273e

16h ago

---

**[Daily General Discussion December 21, 2025](https://www.reddit.com/r/ethereum/comments/1przbh3/daily_general_discussion_december_21_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Tx-dependency trie for parallel block production and validation](https://www.reddit.com/r/ethereum/comments/1ps7nwg/txdependency_trie_for_parallel_block_production/)**

Edit: The "deferred ordering" array does not need deferred ordering. Nodes can keep meta-data about length at each trie branch, thus always know order. Much like a mapping in Golang has an order and you can run through it sequentially (with "range") and something similar could grab by index (Golang does not allow that but you could). An ability for keys to fetch their "order ID". Thus whenever mapping does not change (contracts make sure to use them that way), such ID can be used. Would work perfectly in my "video pseudonym parties". But requires the array/mapping is its own trie, and the generalized storage architecture described below fits for that. Edit: Probably better to do dependency per transaction rather than storage slot, like Polygon is doing as NaturalCarob5611 pointed out. It avoids conflicts in ETH transfer dependency too. Transactions do storage slot I/O by 2-phase commit, try and run and whenever they request access to slot they take a form of "mutex". Shards keep track of what txID is waiting and which has mutex, and they sync this so all shards with mutex or in queue know it. If a deadlock happens, the shard processing the transaction then knows this directly, and then some rule to choose winner (the one to cause deadlock aborts or by txID). I am still not allowed to mention the elephant in the room in sharding as an Edmund with support of a Ligi threatens a ban if I do, but Polygon seems to be sharding correctly as well, that is, "internal" to the validator, which respects that the validator attestation is actually trust-based and any approach that does not respect that and assumes trustless will fail. But Polygon does not have a flat storage trie, and it seems certain types of "algorithms" that run well in a parallelized way might favor those, my dApp needs to register 10 billion people in 2 weeks (each "period" of 4 weeks) and "delayed ordering" array could allow that in parallel way + shuffling randomly, whereas current array has a bottleneck for writing to the length slot and that cannot be done in parallel, so I think the storage model has to be innovated for true parallel Ethereum. I was recently threatened with a ban for mentioning one thing I think is neglected in scaling, so I assume I will not mention that here. But another important thing, is parallel contract execution. This is probably a topic many people here have expertise on since upwards 10 years, and thus something where those with expertise can share, or when there is unsolved problems, there can be discussion. Ethereum in 2014 ordered all transactions in a block sequentially in the transaction-trie (sequence number as key in trie). It seems an upgrade from that to parallel execution could be the "transaction dependency trie". Where the keys are the number of dependencies (from 0 and upwards), and then each key stores a nested trie with the transactions. Block validators can them simply run transactions in order of dependencies. This trie can be constructed based on read/writes of storage slots. It also seems meaningful with the old flat storage trie idea, which I assume was always about parallelization. It could have "storage objects" that each contain a trie where the keys are storage slots, and storage slots can contain pointers to storage objects. Thus you can have mappings and arrays and such that can be operated on in parallel by shards (I will avoid mentioning my other idea on how such sharding should be organized, as I am threatened with a ban if I do, although it would be easier if moderation here could moderate itself to behave more in line with normal civil discourse). Such is quite easily shardable it seems, arbitrarily (and how arbitrary sharding is allowed, is in that idea I am not allowed to mention by the moderator Edmund with support from Ligi who has publicly threatened a ban if I do). The key is shards can easily collaborate on assembling the Merkle roots for such tries, and mange ranges of keys (based on most significant bits), this has always been a known property of Patricia Merkle Tries. Why is parallelization important to me? Well I invented "video pseudonym parties" between 2015 and 2018 (Gavin Wood who alone built first version of Ethereum is currently approaching same idea and he calls it "proof-of-video-interaction") and it requires hundreds of thousands of transactions per second for 10 billion citizens. The whitepaper is public and published since 2018, it has been cited by MIT researched Bryan Ford in numerous publications, was in Frontiers and Bloomberg, and has been well known by "the community" (but it was originally invented together with a controversial organization). Note, inter-shard "mutexes" (which will be in contract code most likely) is part of such coordination too, but again, me being forbidden from mentioning the elephant in the room on sharding does make it harder to have a technical discussion, and it would be good if the moderation here could overrule that moderator's threat. I do not see how it is productive to forbid mentioning the elephant in the room on sharding, it ought to make it impossible to move past that bottleneck. Edit: The dependency trie probably needs storage slots nested under each transaction, and for multiple accesses sequential list, and then the transaction hash dependencies for each. The block validator has to run every transaction in parallel, but the dependency trie acts as implicit "mutex" for each point of contention, with no deadlocks as the block producer could run it. It is a bit complicated, but it seems it should work. The "number of dependencies" part in the trie can be skipped, it is meaningless. But it would be easier if I was not threatened with ban if I mention the elephant in the room in scaling, as it is important here in how the sharding is ideally organized (or, the only way it works in this current paradigm).

1d ago

---

**[Ever wanted to send an EIP-4844 blob?](https://www.reddit.com/r/ethereum/comments/1prnppx/ever_wanted_to_send_an_eip4844_blob/)**

2d ago

---

**[Recovering old, mined ETH](https://www.reddit.com/r/ethereum/comments/1prob1d/recovering_old_mined_eth/)**

Hi! I mined some ETH around 2018 but I haven't touched it in a long time and I haven't been following the developments around ETH for a while. I started looking into it recently and was wondering if anybody has up to date advice on how best to recover the funds in my account? I found a backup folder on my PC that has a binary file starting with "UTC--" and also a doc where I had just saved a long hex value in it. I think the hex value is the wallet address which I used to access with nanopool, so I looked it up on etherscan and can see it still has some value in it. Is there anything else that I need? If a password is needed to decrypt the binary file, I'm not sure if I remember what that is, but if possible I could try to guess a few passwords I used to use...

2d ago

---

**[Daily General Discussion December 20, 2025](https://www.reddit.com/r/ethereum/comments/1pr76mk/daily_general_discussion_december_20_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[DTCC processed $3.7 quadrillion in 2024?? and they’re tokenizing U.S. treasuries now?? ON F*CKING CANTON???](https://www.reddit.com/r/ethereum/comments/1prnc2q/dtcc_processed_37_quadrillion_in_2024_and_theyre/)**

why tf is the biggest post-trade player picking a private-by-default network instead of Ethereum that everyone already uses?

🔗 [Daily Crypto Briefs](https://dailycryptobriefs.com/news/dtcc-tokenizes-us-treasuries-canton-network/) • 2d ago

---

**[Trust funds don’t exist where I live, can I substitute it with crypto?](https://www.reddit.com/r/ethereum/comments/1pqv5m1/trust_funds_dont_exist_where_i_live_can_i/)**

I live in Indonesia. Trust funds basically don’t exist here, and investing in foreign ETFs is messy (brokers, FX, income tax, reporting).Crypto is weirdly simpler. Trades here are taxed with a final tax (~0.1–0.2%) buy/sell and you’re done.That made me wonder: could smart contracts act like a low-cost “trust fund”? Rule-based investing (tokenized ETFs/T-bills), auto-rebalancing, monthly cash-outs to local currency, no banks or trustees. But maybe I’m missing something: - wallet loss / key management - smart contract risk - regulation catching up? Is there already a service for this use case?

3d ago

---

---

## Google News: "ethereum"

**[ETH news: Ethereum’s ‘Glamsterdam’ upgrade aims to fix MEV fairness](https://www.coindesk.com/tech/2025/12/20/ethereum-s-glamsterdam-upgrade-aims-to-fix-mev-fairness)**

The full scope of Glamsterdam has not yet been finalized, but developers are targeting it to go live in 2026.

CoinDesk • 2d ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC, ETH and XRP eye breakout for fresh recovery](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-eth-and-xrp-eye-breakout-for-fresh-recovery-202512220400)**

Bitcoin (BTC), Ethereum (ETH), and Ripple (XRP) are approaching key technical levels at the time of writing on Monday as the broader crypto market stabilizes.

FXStreet • 18h ago

---

**[$270 Million From BlackRock Wallets Hit Coinbase; Bitcoin and Ethereum at Risk of Sell-Off](https://www.tradingview.com/news/u_today:ac09f76e3094b:0-270-million-from-blackrock-wallets-hit-coinbase-bitcoin-and-ethereum-at-risk-of-sell-off/)**

BlackRock-linked wallets sent about $270 million in Bitcoin and Ethereum to Coinbase Prime, according to the on-chain transfer screenshots from Lookonchain and Arkham. The transfers add up to 2,019 BTC valued at around $181.7 million and 29,928 ETH worth about $91.3 million. Instead of one big pack…

TradingView — Track All Markets • 9h ago

---

**[Ethereum Leads Wall Street Tokenization Race as Mass Adoption Looms](https://finance.yahoo.com/news/ethereum-leads-wall-street-tokenization-120215998.html)**

As Wall Street embraces tokenization, institutions are converging around Ethereum. Some of the largest tokenized assets today include money market funds issued on Ethereum. With ...

Yahoo Finance • 2d ago

---

**[Ethereum Leverage Hits Record Highs: Why Your ETH Now Sits on a Time Bomb](https://99bitcoins.com/news/altcoins/ethereum-leverage-hits-record-highs-why-your-eth-now-sits-on-a-time-bomb/)**

99Bitcoins • 1d ago

---

**[BitMine Immersion Highlights Record Ethereum Treasury and Liquidity](https://www.tipranks.com/news/company-announcements/bitmine-immersion-highlights-record-ethereum-treasury-and-liquidity)**

TipRanks • 8h ago

---

**[Ethereum developers name post-Glamsterdam upgrade 'Hegota' as 2026 roadmap takes shape](https://www.theblock.co/post/383275/ethereum-developers-name-post-glamsterdam-upgrade-hegota-as-2026-roadmap-takes-shape)**

The Block • 3d ago

---

**[Vitalik Warned of TRON Overtaking Ethereum—6 years Later, Here’s ETH vs. Tron](https://zycrypto.com/vitalik-warned-of-tron-overtaking-ethereum-6-years-later-heres-eth-vs-tron/)**

Six years ago, Ethereum co-founder Vitalik Buterin said he would respect a technically competent rival overtaking Ethereum.

ZyCrypto • 2d ago

---

**[Ethereum whales move in! $644 mln ETH ETF outflows drain the market](https://ambcrypto.com/ethereum-whales-move-in-644-mln-eth-etf-outflows-drain-the-market/)**

Large holders are buying like never before while ETF numbers collapse.

AMBCrypto • 14h ago

---

**[Ethereum Foundation refocuses to security over speed – sets strict 128-bit rule for 2026](https://cryptoslate.com/ethereum-foundation-refocuses-to-security-over-speed-sets-strict-128-bit-rule-for-2026/)**

Speed is no longer enough: The Foundation warns that without formally verified soundness, attackers could rewrite state, rendering high-speed proving a critical liability.

CryptoSlate • 2d ago

---

---

## YouTube Videos: "ethereum"

**[THE BITCOIN SQUEEZE JUST STARTED (This is Next)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=Ryb8qPUZCUc)**

THE BITCOIN SQUEEZE JUST STARTED (This is Next)!!! - Bitcoin News Today, Ethereum & Altcoins *Pionex* ...

📺 Crypto World

👁️ 4K • 👍 207 • 💬 42 • ⏱️ 17:34 • 6h ago

---

**[Tom Lee: The 2026 Crypto Bull Run Has CHANGED (New Prediction)](https://www.youtube.com/watch?v=MiobwJAGZ-g)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 20K • 👍 710 • 💬 73 • ⏱️ 15:49 • 1d ago

---

**[TOM LEE JUST DROPPED $40M ON ETH! (Whale Alert)](https://www.youtube.com/watch?v=iNSNWJAiXX0)**

Today's Whale Buy Alert The wallet just activated. And the size of the buy is staggering. According to on-chain data, BitMine ...

📺 Wall Street Stockcast

👁️ 1K • 👍 41 • 💬 15 • ⏱️ 7:32 • 9h ago

---

**[BMNR Owns 3.37% of Ethereum — Why $60+ Is the Next Technical Target](https://www.youtube.com/watch?v=GR9JlQ34Z8Y)**

BitMine Immersion Technologies ($BMNR) has officially secured ~3.37% of the total Ethereum supply, holding over 4 million ETH ...

📺 CryptoStock Lab

👁️ 152 • 👍 8 • ⏱️ 16:54 • 2h ago

---

**[Ethereum’s Setup Signals Volatility Ahead Into 2026](https://www.youtube.com/watch?v=LNC18lqDyPs)**

HUGE CHRISTMAS SALE! GET $600 OFF AI INDICATORS! https://www.tradeconfident.io/indicators ✓ Get 25% Off Membership: ...

📺 Trade Confident

👁️ 54 • 👍 5 • 💬 2 • ⏱️ 5:29 • 1h ago

---

**[Tom Lee&#39;s Fundstrat Sees $60K BTC $1.8k ETH and $50 SOL In H1 2026... Stablecoin Battle, BTC ETF...](https://www.youtube.com/watch?v=PrjHeXsAGfE)**

Welcome back for another daily market update as always this will be a jam packed one! Join the Patreon and get exclusive ...

📺 AllinCrypto

👁️ 13K • 👍 683 • 💬 405 • ⏱️ 11:34 • 1d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=baVZ1J_gs5w)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 175 • 💬 10 • ⏱️ 6:15 • 18h ago

---

**[ETH Ethereum Price Prediction: 22nd Of December](https://www.youtube.com/watch?v=nDUm4G5qRso)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 180 • 👍 30 • 💬 8 • ⏱️ 5:02 • 3h ago

---

**[Is $BMNR Signaling A New ETH Bull Run? (The &quot;Smart Money&quot; Indicator)](https://www.youtube.com/watch?v=bX-vqqC2d88)**

Is $BMNR Signaling a New ETH Bull Run? In the crypto markets, the miners are the "Canary in the Coal Mine." History shows that ...

📺 NextMove Stocks

👁️ 449 • 👍 17 • 💬 13 • ⏱️ 7:50 • 8h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=HXb6p0wUQt0)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 135 • 💬 4 • ⏱️ 4:52 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
