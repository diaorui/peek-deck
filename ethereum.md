---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-08T19:26:54.793535+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- cryptocurrency
- news
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 08, 2026 at 19:26 UTC  
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

### $2,109.76

---

## Ethereum Chart

**24h:** +0.5%  
**7d:** -9.9%  
**30d:** -31.6%  
**90d:** -38.1%  
**1y:** -19.6%  

---

## Ethereum Market Stats

**Market Cap:** $252.37B
Rank #2

**Circulating Supply:** 120,692,627 ETH
No max supply

**All-Time High:** $4,946.05
-57.7%

**All-Time Low:** $0.43
+482805.6%

---

## Reddit: r/ethereum

**[Daily General Discussion February 08, 2026](https://www.reddit.com/r/ethereum/comments/1qz13nm/daily_general_discussion_february_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

13h ago

---

**[Staking on coinbase or... ??](https://www.reddit.com/r/ethereum/comments/1qzfbqx/staking_on_coinbase_or/)**

So I have some eth staked on coinbase but wondering how risky it is.. should I be looking somewhere else or is coinbase a good call? I don't answer private messages thanks

1h ago

---

**[What I learned building an Optimism node and why binary matters.](https://www.reddit.com/r/ethereum/comments/1qzg7d1/what_i_learned_building_an_optimism_node_and_why/)**

I manually architected a Dual-STACK Execution and Consensus Engine that bypasses the entire public RPC industry. Hardware; Managed a 4TB NVMe volume with 3.3TB Optimism state and a pruned L1 Reth/Lighthouse combo. I compiled Lighthouse and Reth from source after Optimism-specific codebase was deprecated mid-sync. I achieved 0ms IPC round trips by killing the dependency on Alchemy/Infura Ran into a few problems along the way. I tried to run a standard Ethereum binary on Optimism data. The node crashed because it saw a transaction type it didn't recognize (Type 126 which is an Optimism deposit) Standard Ethereum node thinks this is illegal data. To fix it, I identified that i needed a specialized OP-Stack aware version of Reth. I tracked down the Paradigm Reth Optimism binary. By switching to the op-reth binary i gave the node the dictionary it needed to translate those Type 126 deposits into valid blocks. I moved from a blind Ethereum node to a Super chain-aware engine. The Reth engine was idling. It had peers and a database, but it didn't know where the tip of the chain was, so it stayed at block 0. I realized a modern node was a Two-Part Machine. So I built the Lighthouse Consensus Client from source to be the "Driver" Instead of waiting weeks to download the chain from 2015 i used a Checkpoint Sync URL. I linked Lighthouse to Reth via the Engine API ()Port 8551/8552) using a shared JWT Secret. The moment Lighthouse found the "Truth" on the network, it handed the coordinates to Reth. The node immediately jumped from 0 to 21,800,000 and the 1.9TB of free space started filling with real history. The real nightmare scenario happened when I was syncing the snapshot data and because of a single transaction type the whole thing crashed. My sync was flying for about 15 hours and when I woke up to check it found it had stalled. It hit block 144,528215 where it encountered an Optimism-specific Type 126 Deposit transaction. Because I was running the standard Ethereum Reth binary instead of the specialized Op-Reth version from paradigm, the node literally didn't have the code to read it understand what type 126 transaction it was. This didn't just crash the sync, it left garbage data at the tip of my database, which blocked further progress until I swapped binary and manually forced a stage rewind to clear corruption. In the grand scheme of thing's it was a rookie mistake.

1h ago

---

**[Stock Trader’s Crypto Panic: Sell BTC/ETH at 70% Peak or HODL the Dip?](https://www.reddit.com/r/ethereum/comments/1qzhvbi/stock_traders_crypto_panic_sell_btceth_at_70_peak/)**

Hey Redditors, I’m feeling pretty confused right now and could really use your collective wisdom: should I sell my Bitcoin and Ethereum, or should I hold tight through this volatility? I’ve been successfully trading stocks and options for over 20 years; everything from forex to commodities….but I finally decided to dip my toes into crypto for the first time late last year, thinking it was the next big diversification play for me. Here’s the deal: I bought in at Bitcoin around $82k USD and grabbed ETH at roughly $3,800 each. Fast forward to now in early February 2026, BTC’s hovering around $71k after some wild swings (dipped below $61k recently, now rebounding a bit), and ETH is sitting lower too amid all the “crypto winter” chatter, whale sells, ETF flows, and macro noise like Fed uncertainty and seasonal sell-offs. I’m down on paper, which stings after decades of stock market discipline, but I’ve seen cycles before; just not ones this intense! As a newbie to this space (stocks felt way more predictable), I’m torn: Cut losses and rotate back to traditional markets? HODL for the long-term upside with institutional adoption and potential QE boosts? Dollar-cost average down? Or maybe sell half and let the rest ride? What’s worked for you in similar spots, especially fellow stock vets who’ve crossed over? Thanks a ton!

12m ago

---

**[Laundry Cash - Ethereum Privacy Protocol](https://www.reddit.com/r/ethereum/comments/1qzekia/laundry_cash_ethereum_privacy_protocol/)**

Non-custodial privacy protocol for anonymous ETH transactions. Break the on-chain link using zero-knowledge proofs. Live on Ethereum mainnet.

🔗 [Laundry Cash](https://ethlaundry.xyz) • 2h ago

---

**[I built the first fully on-chain, 100% decentralized, ETH-in ETH-out (no new token), skill based competitive gaming platform](https://www.reddit.com/r/ethereum/comments/1qz1wbo/i_built_the_first_fully_onchain_100_decentralized/)**

12h ago

---

**[Daily General Discussion February 07, 2026](https://www.reddit.com/r/ethereum/comments/1qy5yxh/daily_general_discussion_february_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[We're building an open-source archive of the earliest Ethereum smart contracts (2015-2017) — looking for contributors](https://www.reddit.com/r/ethereum/comments/1qymum3/were_building_an_opensource_archive_of_the/)**

1d ago

---

**[Daily General Discussion February 06, 2026](https://www.reddit.com/r/ethereum/comments/1qx9o40/daily_general_discussion_february_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Ethereal news weekly #10 | Vitalik: role of L2s has changed, Hegotá upgrade headliner proposals, Lido v3 live](https://www.reddit.com/r/ethereum/comments/1qxheul/ethereal_news_weekly_10_vitalik_role_of_l2s_has/)**

Vitalik: role of L2s has changed, Hegotá upgrade headliner proposals, Lido v3 live

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-10/) • 2d ago

---

---

## Google News: "ethereum"

**[Ethereum makes game-changing decision that could change future of cryptocurrency: 'Poised to lead the way'](https://www.thecooldown.com/green-business/ethereum-cryptocurrency-sustainable-proof-of-stake/)**

Ethereum's shift to a new cryptocurrency mining mechanism has demonstrated how the industry is changing its ways.

The Cool Down • 1d ago

---

**[How Buying Ethereum Today Could 10x Your Net Worth](https://www.nasdaq.com/articles/how-buying-ethereum-today-could-10x-your-net-worth)**

Key PointsEther’s price has plunged in 2026.

Nasdaq • 2d ago

---

**[Ethereum Price Is Not Going To Keep Falling Forever, Analyst Says](https://www.tradingview.com/news/newsbtc:6ebc821a3094b:0-ethereum-price-is-not-going-to-keep-falling-forever-analyst-says/)**

Ethereum’s recent sell-off has weighed heavily on sentiment after the price fell below the $2,000 level and pulled much of the altcoin market lower alongside it. The move has caused sweeping fear and caution among Ethereum traders. However, some analysts are of the notion that a bullish upside will…

TradingView • 16h ago

---

**[Ethereum Rebounds from Lows, but ETF Flows Still Point to Caution](https://www.tipranks.com/news/can-ethereum-rebounds-from-lows-but-etf-flows-still-point-to-cautioncan)**

Ethereum (ETH-USD) faced a tough week as selling pressure built up across the crypto market. Indeed, Ethereum fell more than 30% over the past week and briefly slid...

TipRanks • 1d ago

---

**[How cryptocurrency’s second largest coin missed out on the industry’s boom](https://www.theguardian.com/technology/2026/feb/05/cryptocurrency-ethereum-bitcoin-industry)**

A leaked pitch to reshape Ethereum’s leadership exposed deep divisions over politics, power and Ether’s static price

The Guardian • 3d ago

---

**[BitMine Ethereum Treasury Losses And Leadership Changes Put BMNR Under Scrutiny](https://finance.yahoo.com/news/bitmine-ethereum-treasury-losses-leadership-170707091.html)**

BitMine Immersion Technologies, ticker NYSEAM:BMNR, is reporting nearly $8b in unrealized losses tied to its Ethereum holdings after a sharp pullback in ETH prices. The company continues to frame its large Ethereum position and staking operations as part of a long term treasury approach, while continuing to accumulate ETH. Recent executive turnover, including the amicable separation of President Erik Nelson, is adding another layer of uncertainty for shareholders during heightened crypto...

Yahoo Finance • 1d ago

---

**[ENS Labs scraps Namechain L2, shifts ENSv2 fully to Ethereum mainnet](https://www.theblock.co/post/388932/ens-labs-scraps-namechain-l2-shifts-ensv2-fully-ethereum-mainnet)**

ENS Labs is canceling the launch of the Namechain Layer 2, which began development in 2024 to support the forthcoming ENSv2 update.

The Block • 1d ago

---

**[Crypto prices on Friday: Bitcoin, Ethereum and more tick upward](https://mashable.com/article/crypto-bitcoin-ethereum-prices-tick-upward-friday-2-6-2026)**

Prices are climbing back up after the biggest crypto crash since 2022.

Mashable • 2d ago

---

**[Ethereum and Solana Are Getting Hit Hard. Are These Top Cryptocurrencies Buys on the Dip?](https://www.fool.com/investing/2026/02/07/ethereum-and-solana-are-getting-hit-hard-are-these/)**

Here's why giving up on Ethereum and Solana now would be a mistake.

The Motley Fool • 1d ago

---

**[Solana’s quiet takeover – Can SOL profit from the FUD around Ethereum?](https://ambcrypto.com/solanas-quiet-takeover-can-sol-profit-from-the-fud-around-ethereum/)**

Solana may be outperforming Ethereum across key metrics right now.

AMBCrypto • 14h ago

---

---

## YouTube Videos: "ethereum"

**[BE READY FOR THESE MOVES!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=Kse3VGjjDP0)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 584 • 👍 19 • 💬 12 • ⏱️ 4:21 • 9h ago

---

**[Fundstrat&#39;s Tom Lee: Crypto looks like it is bottoming now](https://www.youtube.com/watch?v=Fh8djni6jHU)**

Tom Lee, Fundstrat, joins 'Closing Bell' to discuss the state of crypto markets, Bitmine's business and much more.

📺 CNBC Television

👁️ 79K • 👍 820 • 💬 323 • ⏱️ 3:53 • 1d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=3YC2YldLk78)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 208 • 💬 12 • ⏱️ 5:21 • 13h ago

---

**[BITCOIN &amp; ALTCOINS: New Targets Confirmed (Prepare Now)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=5dz7kqlC6mQ)**

BITCOIN & ALTCOINS: New Targets Confirmed (Prepare Now)!!! - Bitcoin News Today, Ethereum & Altcoins *Bitunix* ...

📺 Crypto World

👁️ 13K • 👍 430 • 💬 227 • ⏱️ 17:07 • 21h ago

---

**[🚨 BTC &amp; ETH: THIS IS IT!!!! ITS TIME!!!!!](https://www.youtube.com/watch?v=8QI8ukpRpEI)**

One of the biggest crypto crashes in history! Here is what happened, why and my plan going further. ---------- LIVE VIRTUAL ...

📺 Thomas Kralow

👁️ 41K • 👍 2K • 💬 81 • ⏱️ 11:51 • 2d ago

---

**[Pour l&#39;Empereur d&#39;Ethereum, les rollups doivent être jetés aux lions - Actu crypto 🗞️](https://www.youtube.com/watch?v=kBAooka4YCo)**

10 % de remise à vie sur vos frais de trading en achetant des cryptos sur Binance ▻ https://journalducoin.com/Binance/CTA10 ...

📺 Journal du Coin

👁️ 396 • 👍 73 • ⏱️ 10:35 • 2h ago

---

**[I Think Something Insane Is About To Happen To Bitcoin And Ethereum But No One Is Seeing The Signs](https://www.youtube.com/watch?v=edXKNl2JR_s)**

Uhh... so... is anyone else getting that strange feeling that something big is about to go down in the crypto market. We've seen tons ...

📺 Money Rules - Investing Tips 

👁️ 13K • 👍 2K • 💬 218 • ⏱️ 13:13 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=H_Y7-M-mSto)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 4K • 👍 205 • 💬 11 • ⏱️ 4:56 • 23h ago

---

**[Il se passe quelque chose de fou sur Ethereum](https://www.youtube.com/watch?v=d9cazkz9KTo)**

L'exchange crypto le plus sérieux du marché, c'est lui. Régulé US & Europe, jamais hacké, interface clean, support 24/7 ...

📺 Crypto Mindset Podcast 

👁️ 2K • 👍 164 • 💬 59 • ⏱️ 10:19 • 7h ago

---

**[“This Crash Might Be the Setup Most Crypto Holders Are Missing&quot; – Matt Hougan](https://www.youtube.com/watch?v=gMUdNWz4eaI)**

Take Control of Your Retirement — Grow Crypto & Gold Tax-Advantaged. https://www.itrustcapital.com/go/savvy-finance If you're ...

📺 Savvy Finance

👁️ 8K • 👍 346 • 💬 12 • ⏱️ 20:57 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
