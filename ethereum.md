---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-09T13:54:05.662383+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- cryptocurrency
- videos
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 09, 2026 at 13:54 UTC  
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

### $2,028.40

---

## Ethereum Chart

**24h:** -4.4%  
**7d:** -9.1%  
**30d:** -35.0%  
**90d:** -40.5%  
**1y:** -23.6%  

---

## Ethereum Market Stats

**Market Cap:** $245.58B
Rank #2

**Circulating Supply:** 120,692,614 ETH
No max supply

**All-Time High:** $4,946.05
-59.0%

**All-Time Low:** $0.43
+468636.4%

---

## Reddit: r/ethereum

**[Daily General Discussion February 09, 2026](https://www.reddit.com/r/ethereum/comments/1qzwdwq/daily_general_discussion_february_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

7h ago

---

**[EtherWorld Weekly — Edition 350](https://www.reddit.com/r/ethereum/comments/1qzwa9u/etherworld_weekly_edition_350/)**

World News, Stories By EtherWorld, Technical Explainers, Client News & Updates, Podcasts, Upcoming Events & Jobs

🔗 [EtherWorld.co](https://etherworld.co/etherworld-weekly-edition-350/) • 7h ago

---

**[Extremely lightweight transaction monitor for Ethereum. Less than 3MB in RAM.](https://www.reddit.com/r/ethereum/comments/1qzq0sb/extremely_lightweight_transaction_monitor_for/)**

eth-mempool-monitor subscribes to Ethereum pending transactions over WebSocket, filters them against a monitored address set stored in Redis/Valkey, and publishes matching transactions to RabbitMQ. The project builds three binaries: eth_mempool_monitor: WebSocket subscriber + Redis filter + RabbitMQ publisher. rpc_control: newline-delimited JSON-RPC TCP server used to manage monitored addresses in Redis (token-authenticated). rabbitmq_tx_console: RabbitMQ consumer that prints monitored-transaction events in human-readable form.

🔗 [GitHub](https://github.com/ThirdLetterC/eth-mempool-monitor) • 13h ago

---

**[Nano EVM](https://www.reddit.com/r/ethereum/comments/1r04cnt/nano_evm/)**

This is a compact Ethereum Virtual Machine runtime written in strict C23. Made this for learning purposes. BTW, it has a toy Solidity-like compiler into bytecode and `nano-node` program that "deploys" contracts to local store and gives ability to call them.

🔗 [GitHub](https://github.com/ThirdLetterC/nano-evm) • 19m ago

---

**[The Bug of Solving Bugs](https://www.reddit.com/r/ethereum/comments/1r03voi/the_bug_of_solving_bugs/)**

A bug fix turned into a personal comeback story of coding, parenting, and a small contribution to the open-source world.

🔗 [EtherWorld.co](https://etherworld.co/the-bug-of-solving-bugs/) • 40m ago

---

**[Should I stake my ETH in my ledger with Lido? Is it safe?](https://www.reddit.com/r/ethereum/comments/1qzmo4m/should_i_stake_my_eth_in_my_ledger_with_lido_is/)**

I'm willing to stake my ETH that I have on my ledger, is this safe to use lido from the ledger?

15h ago

---

**[Daily General Discussion February 08, 2026](https://www.reddit.com/r/ethereum/comments/1qz13nm/daily_general_discussion_february_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[What I learned building an Optimism node and why binary matters.](https://www.reddit.com/r/ethereum/comments/1qzg7d1/what_i_learned_building_an_optimism_node_and_why/)**

I manually architected a Dual-STACK Execution and Consensus Engine that bypasses the entire public RPC industry. Hardware; Managed a 4TB NVMe volume with 3.3TB Optimism state and a pruned L1 Reth/Lighthouse combo. I compiled Lighthouse and Reth from source after Optimism-specific codebase was deprecated mid-sync. I achieved 0ms IPC round trips by killing the dependency on Alchemy/Infura Ran into a few problems along the way. I tried to run a standard Ethereum binary on Optimism data. The node crashed because it saw a transaction type it didn't recognize (Type 126 which is an Optimism deposit) Standard Ethereum node thinks this is illegal data. To fix it, I identified that i needed a specialized OP-Stack aware version of Reth. I tracked down the Paradigm Reth Optimism binary. By switching to the op-reth binary i gave the node the dictionary it needed to translate those Type 126 deposits into valid blocks. I moved from a blind Ethereum node to a Super chain-aware engine. The Reth engine was idling. It had peers and a database, but it didn't know where the tip of the chain was, so it stayed at block 0. I realized a modern node was a Two-Part Machine. So I built the Lighthouse Consensus Client from source to be the "Driver" Instead of waiting weeks to download the chain from 2015 i used a Checkpoint Sync URL. I linked Lighthouse to Reth via the Engine API ()Port 8551/8552) using a shared JWT Secret. The moment Lighthouse found the "Truth" on the network, it handed the coordinates to Reth. The node immediately jumped from 0 to 21,800,000 and the 1.9TB of free space started filling with real history. The real nightmare scenario happened when I was syncing the snapshot data and because of a single transaction type the whole thing crashed. My sync was flying for about 15 hours and when I woke up to check it found it had stalled. It hit block 144,528215 where it encountered an Optimism-specific Type 126 Deposit transaction. Because I was running the standard Ethereum Reth binary instead of the specialized Op-Reth version from paradigm, the node literally didn't have the code to read it understand what type 126 transaction it was. This didn't just crash the sync, it left garbage data at the tip of my database, which blocked further progress until I swapped binary and manually forced a stage rewind to clear corruption. In the grand scheme of thing's it was a rookie mistake.

19h ago

---

**[Staking on coinbase or... ??](https://www.reddit.com/r/ethereum/comments/1qzfbqx/staking_on_coinbase_or/)**

So I have some eth staked on coinbase but wondering how risky it is.. should I be looking somewhere else or is coinbase a good call? I don't answer private messages thanks

20h ago

---

**[Laundry Cash - Ethereum Privacy Protocol](https://www.reddit.com/r/ethereum/comments/1qzekia/laundry_cash_ethereum_privacy_protocol/)**

Non-custodial privacy protocol for anonymous ETH transactions. Break the on-chain link using zero-knowledge proofs. Live on Ethereum mainnet.

🔗 [Laundry Cash](https://ethlaundry.xyz) • 20h ago

---

---

## Google News: "ethereum"

**[Ethereum makes game-changing decision that could change future of cryptocurrency: 'Poised to lead the way'](https://www.thecooldown.com/green-business/ethereum-cryptocurrency-sustainable-proof-of-stake/)**

Ethereum's shift to a new cryptocurrency mining mechanism has demonstrated how the industry is changing its ways.

The Cool Down • 1d ago

---

**[Is Ethereum's New AI Agent Scheme a Reason to Buy It Hand Over Fist?](https://www.fool.com/investing/2026/02/09/is-ethereums-new-ai-agent-scheme-a-reason-to-buy-i/)**

Ethereum is leading the development of a new set of standards for the use of AI in crypto.

The Motley Fool • 3h ago

---

**[Ethereum Is More Popular Than Ever. Should You Invest $1,000?](https://finance.yahoo.com/news/ethereum-more-popular-ever-invest-092000879.html)**

This kind of popularity isn't necessarily something to root for as an investor in this coin.

Yahoo Finance • 4h ago

---

**[Bitcoin, Ethereum, XRP Fall. Why There’s Hope for a Crypto Rally.](https://www.barrons.com/articles/bitcoin-price-ethereum-xrp-crypto-c754458e?gaa_at=eafs&gaa_n=AWEtsqeTnlXTKnN6yBBYH6MxcLr4p837pmzDVcfzQU4F1heR9AIrUcqCw17H&gaa_ts=6989ea65&gaa_sig=0l5jberD2FQm5mj5VtLJX5shrpmsyOPED5EzHpw66Qkdhv6KeWAix-EN0Y-G6QJ2O53N7CGGUQLoZ3jyXfIGgg%3D%3D)**

Barron's • 3h ago

---

**[ENS Labs scraps Namechain L2, shifts ENSv2 fully to Ethereum mainnet](https://www.theblock.co/post/388932/ens-labs-scraps-namechain-l2-shifts-ensv2-fully-ethereum-mainnet)**

ENS Labs is canceling the launch of the Namechain Layer 2, which began development in 2024 to support the forthcoming ENSv2 update.

The Block • 2d ago

---

**[The Vibes From the 'Davos for Degens' as Bitcoin and Ethereum Plummeted](https://decrypt.co/357315/vibes-davos-degens-bitcoin-ethereum-plummeted)**

At a conference dedicated to the riskiest traders in finance, Miami's crypto scene appeared far different than during its pandemic-era boom.

Decrypt • 21h ago

---

**[Ethereum Price Is Not Going To Keep Falling Forever, Analyst Says](https://www.tradingview.com/news/newsbtc:6ebc821a3094b:0-ethereum-price-is-not-going-to-keep-falling-forever-analyst-says/)**

Ethereum’s recent sell-off has weighed heavily on sentiment after the price fell below the $2,000 level and pulled much of the altcoin market lower alongside it. The move has caused sweeping fear and caution among Ethereum traders. However, some analysts are of the notion that a bullish upside will…

TradingView • 1d ago

---

**[Solana’s quiet takeover – Can SOL profit from the FUD around Ethereum?](https://ambcrypto.com/solanas-quiet-takeover-can-sol-profit-from-the-fud-around-ethereum/)**

Solana may be outperforming Ethereum across key metrics right now.

AMBCrypto • 1d ago

---

**[Tom Lee’s BitMine Adds Another $42 Million in Ethereum Despite Crypto Winter](https://finance.yahoo.com/news/tom-lee-bitmine-adds-another-210000254.html)**

BitMine has expanded its Ethereum hodings by acquiring an additional 20,000 ETH for nearly $42 million this week.

Yahoo Finance • 16h ago

---

**[Sharplink: An Unfairly Penalized Ethereum Treasury Company](https://seekingalpha.com/article/4867467-sharplink-an-unfairly-penalized-ethereum-treasury-company)**

Seeking Alpha • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Welcome Back Home, Ethereum!](https://www.youtube.com/watch?v=ZZNFVcbzUE4)**

Welcome back home Ethereum! This time I think ETH will kick its feet back and stay a while. Later this year it will likely go to the ...

📺 Benjamin Cowen

👁️ 49K • 👍 4K • 💬 246 • ⏱️ 14:29 • 7h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=dkRmzBouZ64)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 211 • 💬 8 • ⏱️ 5:37 • 11h ago

---

**[Ethereum for Beginners! What’s New in 2026](https://www.youtube.com/watch?v=_JT27HyzTUM)**

Ethereum has evolved beyond its early days. This 2026 update revisits how it works, what's different, and what's in store ahead.

📺 CoinGecko

👁️ 359 • 👍 56 • 💬 40 • ⏱️ 4:15 • 3h ago

---

**[BITCOIN AND ETH: I DO NOT TRUST THIS PUMP!!! 🚨🚨 (wtf is happening)](https://www.youtube.com/watch?v=EORmtCdczdo)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 12K • 👍 1K • 💬 68 • ⏱️ 49:46 • 3h ago

---

**[BITCOIN WILL SHOCK EVERYONE (Breakout Loading)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=6VEtJwjh-Z4)**

BITCOIN WILL SHOCK EVERYONE (Breakout Loading)!!! - Bitcoin News Today, Ethereum & Altcoins *Bitunix* ...

📺 Crypto World

👁️ 12K • 👍 414 • 💬 130 • ⏱️ 16:36 • 14h ago

---

**[WHAT TO EXPECT THIS WEEK!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=TTYJ8xOtbO8)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 208 • 👍 7 • 💬 8 • ⏱️ 5:19 • 3h ago

---

**[Fundstrat&#39;s Tom Lee: Crypto looks like it is bottoming now](https://www.youtube.com/watch?v=Fh8djni6jHU)**

Tom Lee, Fundstrat, joins 'Closing Bell' to discuss the state of crypto markets, Bitmine's business and much more.

📺 CNBC Television

👁️ 90K • 👍 861 • 💬 378 • ⏱️ 3:53 • 2d ago

---

**[I Think Something Insane Is About To Happen To Bitcoin And Ethereum But No One Is Seeing The Signs](https://www.youtube.com/watch?v=edXKNl2JR_s)**

Uhh... so... is anyone else getting that strange feeling that something big is about to go down in the crypto market. We've seen tons ...

📺 Money Rules - Investing Tips 

👁️ 13K • 👍 2K • 💬 279 • ⏱️ 13:13 • 2d ago

---

**[How To Capture FRESH MOVE ? 🤑💰 | Ethereum Price Prediction | Ethereum Analysis ✅](https://www.youtube.com/watch?v=vuzwZjkL_6k)**

How To Get Invite In Private Telegram Group? Open FREE Delta Exchange India - https://www.delta.exchange/?code=SHXFQP ...

📺 Trading Secrets With Two Side Traders

👁️ 405 • 👍 65 • 💬 12 • ⏱️ 12:14 • 6h ago

---

**[BE READY FOR THESE MOVES!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=Kse3VGjjDP0)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 1K • 👍 23 • 💬 3 • ⏱️ 4:21 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
