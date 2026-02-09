---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-09T11:25:23.607147+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- social
- videos
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 09, 2026 at 11:25 UTC  
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

### $2,026.43

---

## Ethereum Chart

**24h:** -5.0%  
**7d:** -9.3%  
**30d:** -35.1%  
**90d:** -40.6%  
**1y:** -23.8%  

---

## Ethereum Market Stats

**Market Cap:** $246.09B
Rank #2

**Circulating Supply:** 120,692,614 ETH
No max supply

**All-Time High:** $4,946.05
-58.8%

**All-Time Low:** $0.43
+470664.2%

---

## Reddit: r/ethereum

**[Daily General Discussion February 09, 2026](https://www.reddit.com/r/ethereum/comments/1qzwdwq/daily_general_discussion_february_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

5h ago

---

**[EtherWorld Weekly — Edition 350](https://www.reddit.com/r/ethereum/comments/1qzwa9u/etherworld_weekly_edition_350/)**

World News, Stories By EtherWorld, Technical Explainers, Client News & Updates, Podcasts, Upcoming Events & Jobs

🔗 [EtherWorld.co](https://etherworld.co/etherworld-weekly-edition-350/) • 5h ago

---

**[Extremely lightweight transaction monitor for Ethereum. Less than 3MB in RAM.](https://www.reddit.com/r/ethereum/comments/1qzq0sb/extremely_lightweight_transaction_monitor_for/)**

eth-mempool-monitor subscribes to Ethereum pending transactions over WebSocket, filters them against a monitored address set stored in Redis/Valkey, and publishes matching transactions to RabbitMQ. The project builds three binaries: eth_mempool_monitor: WebSocket subscriber + Redis filter + RabbitMQ publisher. rpc_control: newline-delimited JSON-RPC TCP server used to manage monitored addresses in Redis (token-authenticated). rabbitmq_tx_console: RabbitMQ consumer that prints monitored-transaction events in human-readable form.

🔗 [GitHub](https://github.com/ThirdLetterC/eth-mempool-monitor) • 10h ago

---

**[Should I stake my ETH in my ledger with Lido? Is it safe?](https://www.reddit.com/r/ethereum/comments/1qzmo4m/should_i_stake_my_eth_in_my_ledger_with_lido_is/)**

I'm willing to stake my ETH that I have on my ledger, is this safe to use lido from the ledger?

13h ago

---

**[Daily General Discussion February 08, 2026](https://www.reddit.com/r/ethereum/comments/1qz13nm/daily_general_discussion_february_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[What I learned building an Optimism node and why binary matters.](https://www.reddit.com/r/ethereum/comments/1qzg7d1/what_i_learned_building_an_optimism_node_and_why/)**

I manually architected a Dual-STACK Execution and Consensus Engine that bypasses the entire public RPC industry. Hardware; Managed a 4TB NVMe volume with 3.3TB Optimism state and a pruned L1 Reth/Lighthouse combo. I compiled Lighthouse and Reth from source after Optimism-specific codebase was deprecated mid-sync. I achieved 0ms IPC round trips by killing the dependency on Alchemy/Infura Ran into a few problems along the way. I tried to run a standard Ethereum binary on Optimism data. The node crashed because it saw a transaction type it didn't recognize (Type 126 which is an Optimism deposit) Standard Ethereum node thinks this is illegal data. To fix it, I identified that i needed a specialized OP-Stack aware version of Reth. I tracked down the Paradigm Reth Optimism binary. By switching to the op-reth binary i gave the node the dictionary it needed to translate those Type 126 deposits into valid blocks. I moved from a blind Ethereum node to a Super chain-aware engine. The Reth engine was idling. It had peers and a database, but it didn't know where the tip of the chain was, so it stayed at block 0. I realized a modern node was a Two-Part Machine. So I built the Lighthouse Consensus Client from source to be the "Driver" Instead of waiting weeks to download the chain from 2015 i used a Checkpoint Sync URL. I linked Lighthouse to Reth via the Engine API ()Port 8551/8552) using a shared JWT Secret. The moment Lighthouse found the "Truth" on the network, it handed the coordinates to Reth. The node immediately jumped from 0 to 21,800,000 and the 1.9TB of free space started filling with real history. The real nightmare scenario happened when I was syncing the snapshot data and because of a single transaction type the whole thing crashed. My sync was flying for about 15 hours and when I woke up to check it found it had stalled. It hit block 144,528215 where it encountered an Optimism-specific Type 126 Deposit transaction. Because I was running the standard Ethereum Reth binary instead of the specialized Op-Reth version from paradigm, the node literally didn't have the code to read it understand what type 126 transaction it was. This didn't just crash the sync, it left garbage data at the tip of my database, which blocked further progress until I swapped binary and manually forced a stage rewind to clear corruption. In the grand scheme of thing's it was a rookie mistake.

17h ago

---

**[Staking on coinbase or... ??](https://www.reddit.com/r/ethereum/comments/1qzfbqx/staking_on_coinbase_or/)**

So I have some eth staked on coinbase but wondering how risky it is.. should I be looking somewhere else or is coinbase a good call? I don't answer private messages thanks

17h ago

---

**[Laundry Cash - Ethereum Privacy Protocol](https://www.reddit.com/r/ethereum/comments/1qzekia/laundry_cash_ethereum_privacy_protocol/)**

Non-custodial privacy protocol for anonymous ETH transactions. Break the on-chain link using zero-knowledge proofs. Live on Ethereum mainnet.

🔗 [Laundry Cash](https://ethlaundry.xyz) • 18h ago

---

**[I built the first fully on-chain, 100% decentralized, ETH-in ETH-out (no new token), skill based competitive gaming platform](https://www.reddit.com/r/ethereum/comments/1qz1wbo/i_built_the_first_fully_onchain_100_decentralized/)**

1d ago

---

**[Daily General Discussion February 07, 2026](https://www.reddit.com/r/ethereum/comments/1qy5yxh/daily_general_discussion_february_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[With Ethereum Shifting Away From Rollups, These 6 Tokens Will Benefit](https://unchainedcrypto.com/ethereum-lets-go-of-the-rollup-story-here-are-the-6-tokens-that-benefit/)**

Vitalik signals a shift away from the rollup-centric roadmap. We break down what it means for ETH, L2 tokens, and which models actually work.

unchainedcrypto.com • 2d ago

---

**[Ethereum makes game-changing decision that could change future of cryptocurrency: 'Poised to lead the way'](https://www.thecooldown.com/green-business/ethereum-cryptocurrency-sustainable-proof-of-stake/)**

Ethereum's shift to a new cryptocurrency mining mechanism has demonstrated how the industry is changing its ways.

The Cool Down • 1d ago

---

**[Is Ethereum's New AI Agent Scheme a Reason to Buy It Hand Over Fist?](https://www.fool.com/investing/2026/02/09/is-ethereums-new-ai-agent-scheme-a-reason-to-buy-i/)**

Ethereum is leading the development of a new set of standards for the use of AI in crypto.

The Motley Fool • 55m ago

---

**[Ethereum Is More Popular Than Ever. Should You Invest $1,000?](https://finance.yahoo.com/news/ethereum-more-popular-ever-invest-092000879.html)**

This kind of popularity isn't necessarily something to root for as an investor in this coin.

Yahoo Finance • 2h ago

---

**[Bitcoin, Ethereum, XRP Fall. Why There’s Hope for a Crypto Rally.](https://www.barrons.com/articles/bitcoin-price-ethereum-xrp-crypto-c754458e?gaa_at=eafs&gaa_n=AWEtsqdvOem8u9GBKBzvIU8iKUUuanwhHsyZywTBrf11Rzfz5EtZZA2xEz5j&gaa_ts=6989c786&gaa_sig=RbUhZSnjfiJm0b6ufGv0XHaYsGh8qcBOKv3_vvsm2yvyV8obzDxyXsaLMajLT7-Oy4gFzMa92-m3j05dBsMxtQ%3D%3D)**

Barron's • 32m ago

---

**[ENS Labs scraps Namechain L2, shifts ENSv2 fully to Ethereum mainnet](https://www.theblock.co/post/388932/ens-labs-scraps-namechain-l2-shifts-ensv2-fully-ethereum-mainnet)**

ENS Labs is canceling the launch of the Namechain Layer 2, which began development in 2024 to support the forthcoming ENSv2 update.

The Block • 2d ago

---

**[The Vibes From the 'Davos for Degens' as Bitcoin and Ethereum Plummeted](https://decrypt.co/357315/vibes-davos-degens-bitcoin-ethereum-plummeted)**

At a conference dedicated to the riskiest traders in finance, Miami's crypto scene appeared far different than during its pandemic-era boom.

Decrypt • 19h ago

---

**[Ethereum Price Is Not Going To Keep Falling Forever, Analyst Says](https://www.tradingview.com/news/newsbtc:6ebc821a3094b:0-ethereum-price-is-not-going-to-keep-falling-forever-analyst-says/)**

Ethereum’s recent sell-off has weighed heavily on sentiment after the price fell below the $2,000 level and pulled much of the altcoin market lower alongside it. The move has caused sweeping fear and caution among Ethereum traders. However, some analysts are of the notion that a bullish upside will…

TradingView • 1d ago

---

**[Tom Lee’s BitMine Adds Another $42 Million in Ethereum Despite Crypto Winter](https://finance.yahoo.com/news/tom-lee-bitmine-adds-another-210000254.html)**

BitMine has expanded its Ethereum hodings by acquiring an additional 20,000 ETH for nearly $42 million this week.

Yahoo Finance • 14h ago

---

**[Solana’s quiet takeover – Can SOL profit from the FUD around Ethereum?](https://ambcrypto.com/solanas-quiet-takeover-can-sol-profit-from-the-fud-around-ethereum/)**

Solana may be outperforming Ethereum across key metrics right now.

AMBCrypto • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Welcome Back Home, Ethereum!](https://www.youtube.com/watch?v=ZZNFVcbzUE4)**

Welcome back home Ethereum! This time I think ETH will kick its feet back and stay a while. Later this year it will likely go to the ...

📺 Benjamin Cowen

👁️ 26K • 👍 2K • 💬 135 • ⏱️ 14:29 • 5h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=dkRmzBouZ64)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 181 • 💬 11 • ⏱️ 5:37 • 8h ago

---

**[BE READY FOR THESE MOVES!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=Kse3VGjjDP0)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 1K • 👍 22 • 💬 3 • ⏱️ 4:21 • 1d ago

---

**[BITCOIN WILL SHOCK EVERYONE (Breakout Loading)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=6VEtJwjh-Z4)**

BITCOIN WILL SHOCK EVERYONE (Breakout Loading)!!! - Bitcoin News Today, Ethereum & Altcoins *Bitunix* ...

📺 Crypto World

👁️ 10K • 👍 373 • 💬 106 • ⏱️ 16:36 • 12h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=jPf8REU4pbU)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 227 • 💬 13 • ⏱️ 5:58 • 19h ago

---

**[Fundstrat&#39;s Tom Lee: Crypto looks like it is bottoming now](https://www.youtube.com/watch?v=Fh8djni6jHU)**

Tom Lee, Fundstrat, joins 'Closing Bell' to discuss the state of crypto markets, Bitmine's business and much more.

📺 CNBC Television

👁️ 89K • 👍 853 • 💬 336 • ⏱️ 3:53 • 2d ago

---

**[I Think Something Insane Is About To Happen To Bitcoin And Ethereum But No One Is Seeing The Signs](https://www.youtube.com/watch?v=edXKNl2JR_s)**

Uhh... so... is anyone else getting that strange feeling that something big is about to go down in the crypto market. We've seen tons ...

📺 Money Rules - Investing Tips 

👁️ 13K • 👍 2K • 💬 279 • ⏱️ 13:13 • 2d ago

---

**[Il se passe quelque chose de fou sur Ethereum](https://www.youtube.com/watch?v=d9cazkz9KTo)**

L'exchange crypto le plus sérieux du marché, c'est lui. Régulé US & Europe, jamais hacké, interface clean, support 24/7 ...

📺 Crypto Mindset Podcast 

👁️ 4K • 👍 234 • 💬 57 • ⏱️ 10:19 • 23h ago

---

**[Alex Becker just flipped his entire 2026 crypto thesis?!…](https://www.youtube.com/watch?v=vFSE2QvN5iI)**

Alex Becker just flipped his entire 2026 crypto thesis?!… ➡️ Important Links: Join The Inner Circle (wallet tracker): ...

📺 Across The Rubicon

👁️ 11K • 👍 543 • 💬 45 • ⏱️ 22:14 • 16h ago

---

**[🚨 BTC &amp; ETH: THIS IS IT!!!! ITS TIME!!!!!](https://www.youtube.com/watch?v=8QI8ukpRpEI)**

One of the biggest crypto crashes in history! Here is what happened, why and my plan going further. ---------- LIVE VIRTUAL ...

📺 Thomas Kralow

👁️ 43K • 👍 2K • 💬 81 • ⏱️ 11:51 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
