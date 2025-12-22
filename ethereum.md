---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2025-12-22T13:41:29.460549+00:00'
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

**Last Updated:** December 22, 2025 at 13:41 UTC  
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

### $3,055.61

---

## Ethereum Chart

**24h:** +2.9%  
**7d:** +3.0%  
**30d:** +8.9%  
**90d:** -26.3%  
**1y:** -10.9%  

---

## Ethereum Market Stats

**Market Cap:** $368.64B
Rank #2

**Circulating Supply:** 120,695,004 ETH
No max supply

**All-Time High:** $4,946.05
-38.2%

**All-Time Low:** $0.43
+705465.4%

---

## Reddit: r/ethereum

**[Daily General Discussion December 22, 2025](https://www.reddit.com/r/ethereum/comments/1pss4f5/daily_general_discussion_december_22_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

7h ago

---

**[Many Web3 devs hear “OWASP” but what does it actually mean for smart contracts?](https://www.reddit.com/r/ethereum/comments/1psshj9/many_web3_devs_hear_owasp_but_what_does_it/)**

A lot of builders mention OWASP, but not everyone really knows what it stands for in a smart contract context. At a high level, the OWASP Smart Contract Top 10 is a security awareness standard that highlights the most common and most exploited vulnerabilities in production smart contracts. It’s not theoretical it’s based on what attackers actually use in the wild. Why it’s useful for devs > Helps identify common smart contract failure patterns > Acts as a prevention guide during development > Works as a checklist before audits or deployments > Gives teams a shared security baseline The 2025 OWASP Smart Contract Top 10 i covers issues like access control flaws, oracle manipulation, logic errors, reentrancy, flash loan attacks, insecure randomness, DoS, and more the same classes of bugs responsible for $1.4B+ in losses across 149 incidents in 2024. What makes the list solid is that it’s backed by real exploit data (loss reports, attack research, incident databases), not just best-guess rankings. Curious how many teams here actively reference OWASP during development or only look at it during audits? https://preview.redd.it/6zw9wba58p8g1.jpg?width=1280&format=pjpg&auto=webp&s=1a5a35edfaac83fed2c847383abb31793a8c273e

7h ago

---

**[Daily General Discussion December 21, 2025](https://www.reddit.com/r/ethereum/comments/1przbh3/daily_general_discussion_december_21_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Tx-dependency trie for parallel block production and validation](https://www.reddit.com/r/ethereum/comments/1ps7nwg/txdependency_trie_for_parallel_block_production/)**

I was recently threatened with a ban for mentioning one thing I think is neglected in scaling, so I assume I will not mention that here. But another important thing, is parallel contract execution. This is probably a topic many people here have expertise on since upwards 10 years, and thus something where those with expertise can share, or when there is unsolved problems, there can be discussion. Ethereum in 2014 ordered all transactions in a block sequentially in the transaction-trie (sequence number as key in trie). It seems an upgrade from that to parallel execution could be the "transaction dependency trie". Where the keys are the number of dependencies (from 0 and upwards), and then each key stores a nested trie with the transactions. Block validators can them simply run transactions in order of dependencies. This trie can be constructed based on read/writes of storage slots. It also seems meaningful with the old flat storage trie idea, which I assume was always about parallelization. It could have "storage objects" that each contain a trie where the keys are storage slots, and storage slots can contain pointers to storage objects. Thus you can have mappings and arrays and such that can be operated on in parallel by shards (I will avoid mentioning my other idea on how such sharding should be organized, as I am threatened with a ban if I do, although it would be easier if moderation here could moderate itself to behave more in line with normal civil discourse). Such is quite easily shardable it seems, arbitrarily (and how arbitrary sharding is allowed, is in that idea I am not allowed to mention by the moderator Edmund with support from Ligi who has publicly threatened a ban if I do). The key is shards can easily collaborate on assembling the Merkle roots for such tries, and mange ranges of keys (based on most significant bits), this has always been a known property of Patricia Merkle Tries. Why is parallelization important to me? Well I invented "video pseudonym parties" between 2015 and 2018 (Gavin Wood who alone built first version of Ethereum is currently approaching same idea and he calls it "proof-of-video-interaction") and it requires hundreds of thousands of transactions per second for 10 billion citizens. The whitepaper is public and published since 2018, it has been cited by MIT researched Bryan Ford in numerous publications, was in Frontiers and Bloomberg, and has been well known by "the community" (but it was originally invented together with a controversial organization). Note, inter-shard "mutexes" (which will be in contract code most likely) is part of such coordination too, but again, me being forbidden from mentioning the elephant in the room on sharding does make it harder to have a technical discussion, and it would be good if the moderation here could overrule that moderator's threat. I do not see how it is productive to forbid mentioning the elephant in the room on sharding, it ought to make it impossible to move past that bottleneck. Edit: The dependency trie probably needs storage slots nested under each transaction, and for multiple accesses sequential list, and then the transaction hash dependencies for each. The block validator has to run every transaction in parallel, but the dependency trie acts as implicit "mutex" for each point of contention, with no deadlocks as the block producer could run it. It is a bit complicated, but it seems it should work. The "number of dependencies" part in the trie can be skipped, it is meaningless. But it would be easier if I was not threatened with ban if I mention the elephant in the room in scaling, as it is important here in how the sharding is ideally organized (or, the only way it works in this current paradigm).

23h ago

---

**[Ever wanted to send an EIP-4844 blob?](https://www.reddit.com/r/ethereum/comments/1prnppx/ever_wanted_to_send_an_eip4844_blob/)**

1d ago

---

**[Recovering old, mined ETH](https://www.reddit.com/r/ethereum/comments/1prob1d/recovering_old_mined_eth/)**

Hi! I mined some ETH around 2018 but I haven't touched it in a long time and I haven't been following the developments around ETH for a while. I started looking into it recently and was wondering if anybody has up to date advice on how best to recover the funds in my account? I found a backup folder on my PC that has a binary file starting with "UTC--" and also a doc where I had just saved a long hex value in it. I think the hex value is the wallet address which I used to access with nanopool, so I looked it up on etherscan and can see it still has some value in it. Is there anything else that I need? If a password is needed to decrypt the binary file, I'm not sure if I remember what that is, but if possible I could try to guess a few passwords I used to use...

1d ago

---

**[Daily General Discussion December 20, 2025](https://www.reddit.com/r/ethereum/comments/1pr76mk/daily_general_discussion_december_20_2025/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

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

3d ago

---

---

## Google News: "ethereum"

**[ETH news: Ethereum’s ‘Glamsterdam’ upgrade aims to fix MEV fairness](https://www.coindesk.com/tech/2025/12/20/ethereum-s-glamsterdam-upgrade-aims-to-fix-mev-fairness)**

The full scope of Glamsterdam has not yet been finalized, but developers are targeting it to go live in 2026.

CoinDesk • 1d ago

---

**[Ethereum Foundation refocuses to security over speed – sets strict 128-bit rule for 2026](https://cryptoslate.com/ethereum-foundation-refocuses-to-security-over-speed-sets-strict-128-bit-rule-for-2026/)**

Speed is no longer enough: The Foundation warns that without formally verified soundness, attackers could rewrite state, rendering high-speed proving a critical liability.

CryptoSlate • 2d ago

---

**[Ethereum Hit Harder Than Bitcoin as $952 Million Exits Crypto Funds—Here’s Why](https://finance.yahoo.com/news/ethereum-hit-harder-bitcoin-952-110702690.html)**

US Clarity Act delays cause $952 million in crypto outflows, with regulatory fears hitting Ethereum hardest.

Yahoo Finance • 2h ago

---

**[Where Will Cryptocurrency Ethereum Be in 5 Years?](https://www.fool.com/investing/2025/12/22/where-will-cryptocurrency-ethereum-be-in-5-years/)**

Ethereum is a long way from the high mark it reached in August, but it still has a strong case as an investment.

The Motley Fool • 2h ago

---

**[Bitcoin Rises, Traders Bet on a 5% Crypto Rally By Christmas. Ethereum, XRP Also Up.](https://www.barrons.com/articles/bitcoin-price-rally-ethereum-xrp-crypto-52d2771f?gaa_at=eafs&gaa_n=AWEtsqcocrerkLhc8Cb21asj3YuEpunbGFkafsnE5vpJn9WW0aoZYsRKqn6X&gaa_ts=69494def&gaa_sig=ISpmJVJXSV4lyfYKjXZBp2ryvBvhCXdpZJ1YzzDgXSCwZe3F-X5mtf5Ej6q8S1G0M6x7T4hJba7Wz6AqyurOXQ%3D%3D)**

Barron's • 1h ago

---

**[Solana to Surpass Ethereum in Yearly Revenue](https://www.tradingview.com/news/u_today:85769ad66094b:0-solana-to-surpass-ethereum-in-yearly-revenue/)**

Solana founder Anatoly Yakovenko has shared new data that shows Solana has outperformed Ethereum in yearly revenue, highlighting what he sees as a pivotal shift in how value may be distributed across the crypto market.The infographics by DeFi Development Corp. show the projected chain revenue compa…

TradingView — Track All Markets • 1d ago

---

**[Ethereum whales move in! $644 mln ETH ETF outflows drain the market](https://ambcrypto.com/ethereum-whales-move-in-644-mln-eth-etf-outflows-drain-the-market/)**

Large holders are buying like never before while ETF numbers collapse.

AMBCrypto • 5h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC, ETH and XRP eye breakout for fresh recovery](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-eth-and-xrp-eye-breakout-for-fresh-recovery-202512220400)**

Bitcoin (BTC), Ethereum (ETH), and Ripple (XRP) are approaching key technical levels at the time of writing on Monday as the broader crypto market stabilizes.

FXStreet • 9h ago

---

**[ETHE: What You Need To Know About This Ethereum ETF](https://seekingalpha.com/article/4854984-ethe-what-you-need-to-know-about-this-ethereum-etf)**

ETHE had structural issues before the uplisting, which, after July 2024, have been limited. See why the fund is a volatile solution linked to ETH-USD and the crypto market

Seeking Alpha • 11m ago

---

**[Vitalik Warned of TRON Overtaking Ethereum—6 years Later, Here’s ETH vs. Tron](https://zycrypto.com/vitalik-warned-of-tron-overtaking-ethereum-6-years-later-heres-eth-vs-tron/)**

Six years ago, Ethereum co-founder Vitalik Buterin said he would respect a technically competent rival overtaking Ethereum.

ZyCrypto • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee: The 2026 Crypto Bull Run Has CHANGED (New Prediction)](https://www.youtube.com/watch?v=MiobwJAGZ-g)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 17K • 👍 634 • 💬 63 • ⏱️ 15:49 • 22h ago

---

**[Tom Lee&#39;s Fundstrat Sees $60K BTC $1.8k ETH and $50 SOL In H1 2026... Stablecoin Battle, BTC ETF...](https://www.youtube.com/watch?v=PrjHeXsAGfE)**

Welcome back for another daily market update as always this will be a jam packed one! Join the Patreon and get exclusive ...

📺 AllinCrypto

👁️ 12K • 👍 664 • 💬 450 • ⏱️ 11:34 • 1d ago

---

**[XRP BITCOIN ETHEREUM ‼️ KNOW THIS BEFORE TOMORROW!](https://www.youtube.com/watch?v=bBU6oHVTtXQ)**

1️⃣ *Join Moe's Discord Code CYBER save 60%* ➡https://www.patreon.com/stockmoe/membership 2️⃣ *Save Big on the ...

📺 Stock Moe

👁️ 12K • 👍 846 • 💬 18 • ⏱️ 11:18 • 15h ago

---

**[CRITICAL ETHEREUM UPDATE🚨 (ETH Price Prediction 2025)](https://www.youtube.com/watch?v=Iyi5qnSnU2Q)**

ETHEREUM ETH PRICE PREDICTION 2025 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 108 • 👍 13 • 💬 2 • ⏱️ 4:38 • 3h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=baVZ1J_gs5w)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 161 • 💬 9 • ⏱️ 6:15 • 9h ago

---

**[ETH Ethereum Price Prediction: 21st of December](https://www.youtube.com/watch?v=2_OtXgqgS7Q)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 521 • 👍 39 • 💬 10 • ⏱️ 9:36 • 15h ago

---

**[The BMNR Collapse Explained: Tom Lee’s ETH Bet vs Reality](https://www.youtube.com/watch?v=lz3zPqKVqbQ)**

BMNR Stock Collapsed 80% — Was Tom Lee Wrong or Is This a Setup? | ETH Treasury Risk Breakdown BMNR (BitMine ...

📺 Darren Steves

👁️ 2K • 👍 112 • 💬 22 • ⏱️ 11:28 • 19h ago

---

**[Is Ethereum Massively Overvalued? w/ Haseeb Qureshi](https://www.youtube.com/watch?v=DzS0ldchsps)**

In this episode, Haseeb Qureshi breaks down the viral debate that split Crypto Twitter: Should blockchains be valued like ...

📺 Milk Road

👁️ 3K • 👍 222 • 💬 116 • ⏱️ 11:26 • 1d ago

---

**[Wall Street&#39;s Biggest Bitcoin Bull Is lying to You](https://www.youtube.com/watch?v=iJIcoKxtrGY)**

Tom Lee says “buy Bitcoin” on TV… but his firm is quietly making an Ethereum bet so big it can't be ignored. While he's publicly ...

📺 Ryan’s Money Lab

👁️ 7K • 👍 307 • 💬 42 • ⏱️ 8:06 • 22h ago

---

**[Bitcoin &amp; Ethereum. Wir dürfen weiter verhalten optimistisch sein!!](https://www.youtube.com/watch?v=KB3rgh9gIqU)**

Kanalmitglied werden und exklusive Vorteile erhalten: https://www.youtube.com/channel/UCGUi8e21DGy9YzbkRs1cxTQ/join DIE ...

📺 Krypto Trading & Investing

👁️ 3K • 👍 637 • 💬 145 • ⏱️ 11:01 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
