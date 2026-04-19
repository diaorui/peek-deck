---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-19T19:22:51.757700+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- cryptocurrency
- social
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** April 19, 2026 at 19:22 UTC  
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

### $2,289.77

---

## Ethereum Chart

**24h:** -2.2%  
**7d:** -2.9%  
**30d:** +10.4%  
**90d:** -21.8%  
**1y:** +45.1%  

---

## Ethereum Market Stats

**Market Cap:** $277.52B
Rank #2

**Circulating Supply:** 120,690,543 ETH
No max supply

**All-Time High:** $4,946.05
-53.6%

**All-Time Low:** $0.43
+530288.3%

---

## Reddit: r/ethereum

**[Daily General Discussion April 19, 2026](https://www.reddit.com/r/ethereum/comments/1spjkzn/daily_general_discussion_april_19_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

14h ago

---

**[Someone Warned Kelp DAO About This Exact Vulnerability 15 Months Ago. Nobody Listened. $292 Million Is Gone](https://www.reddit.com/r/ethereum/comments/1spoe1h/someone_warned_kelp_dao_about_this_exact/)**

The Kelp DAO exploit that drained $292 million and froze Aave was preventable. A developer posted on the Aave governance forum in January 2025 that Kelp's single-validator bridge security was the weakest configuration LayerZero allows. Kelp never added the second validator. On Saturday, an attacker used that exact vulnerability.

🔗 [DailyCoinPost](https://dailycoinpost.com/kelp-dao-292-million-hack-warning-ignored-layerzero/) • 9h ago

---

**[Ethereum Opening a Real Physical Hub in Hong Kong Feels Bigger Than It Sounds](https://www.reddit.com/r/ethereum/comments/1spo0jw/ethereum_opening_a_real_physical_hub_in_hong_kong/)**

Feels kinda bigger than a normal crypto meetup tbh Ethereum getting a real physical hub in Hong Kong with Foundation backing sounds like a sign the ecosystem is trying to build something more lasting than just online hype and conference cycles Hong Kong is also a pretty smart place for it if the goal is to connect builders, institutions and actual adoption in Asia Do you guys think this stuff actually matters for Ethereum long term, or is it mostly optics? https://btcusa.com/ethereum-foundation-backs-asias-first-physical-ethereum-hub-in-hong-kong-as-institutional-web3-race-intensifies/

10h ago

---

**[Key Takeaways from Mike Toutonghi’s Paris Blockchain Week 2026 Keynote](https://www.reddit.com/r/ethereum/comments/1sps1nj/key_takeaways_from_mike_toutonghis_paris/)**

6h ago

---

**[Open-sourced a multi-agent contract audit skill for Claude Code](https://www.reddit.com/r/ethereum/comments/1spodq7/opensourced_a_multiagent_contract_audit_skill_for/)**

9h ago

---

**[Daily General Discussion April 18, 2026](https://www.reddit.com/r/ethereum/comments/1soo7xp/daily_general_discussion_april_18_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Can someone give me feedback on an Ethereum page that I built?](https://www.reddit.com/r/ethereum/comments/1sp0z7a/can_someone_give_me_feedback_on_an_ethereum_page/)**

Hello everyone. I recently built an Ethereum page that shows how Ethereum would look if investments never lost value and I’d love someone to look at the page and give me some honest feedback on it.

1d ago

---

**[My master's thesis project - A web3 video streaming app](https://www.reddit.com/r/ethereum/comments/1sohdzd/my_masters_thesis_project_a_web3_video_streaming/)**

Hey all. I just wrapped my master's thesis and figured this sub would actually care about the technical side instead of the price-talk side, so here goes. The thing that always bugged me about existing web3 video platforms is that each one only solves one slice of the problem. Livepeer does transcoding. Theta does P2P relay. Odysee does storage + discovery. PeerTube does federation. None of them stitch identity + gating + payouts + delivery + governance into a single app you can actually use end to end. So I tried to build that, and then benchmark it honestly to see where the real walls are. Stack ended up being: SIWE (EIP-4361) for auth, no email/password anywhere. Wallet address is the user ID across every microservice. ERC-1155 for tiered content gating (Viewer / Supporter / VIP). VIP holders also get priority + a reward multiplier in the P2P layer. 0xSplits + a thin StreamRevenue contract for per-stream revenue distribution. Anyone can trigger the payout, the platform can't withhold. StreamToken (ERC-20 + Votes) for tipping, P2P rewards, and DAO voting. OZ Governor + Timelock controlling a ModerationRegistry contract, so bans actually go through a vote instead of a mod's mood. A custom P2P tracker (Node + WebSocket) that matches viewers by Haversine distance and rewards relays based on bytes × quality multiplier × uptime bonus, instead of the flat-rate model Theta uses. IPFS via Pinata for VOD persistence, with graceful fallback to local if pinning is down. The base streaming pipeline is boring on purpose: NGINX-RTMP ingest, FFmpeg multi-bitrate HLS (1080/720/480/360), Shaka Player on the client. Everything talks to chain through a single Web3 service (ethers.js) so the Go and Python services don't each need to know about Solidity. Target deploy is Arbitrum, dev is on a local Hardhat node. Numbers from the benchmarks (single-machine docker, M4 Pro, 2 CPU / 8 GB allocated to docker so this is conservative): NFT gate verification: P95 = 43 ms (target was <100 ms). 60s Redis cache on top. Revenue API under 50 VUs: P95 = 97 ms, 0% errors at ~78 req/s. P2P browser benchmark with 20 real headless Chromium peers: 92.6% bandwidth savings, 92% hit rate, sub-linear origin growth as peers double. Gas on Arbitrum: NFT mint ~0.024 dollars, tip ~0.018 dollars, full governance lifecycle (propose+vote+queue+execute) ~0.17 dollars. On L1 the same stuff is 100-500x more, which kills the whole thing economically. L2 isn't optional. Stuff that didn't work / I want to be honest about: I tried WHIP (WebRTC ingest) for like 3 weeks. Three different approaches with Pion + FFmpeg, all of them either gave me color corruption from RTP header extensions or frozen frames from clock mismatch. Eventually realized it was pointless: HLS segment buffering (6-12s) dominates end-to-end latency, so saving 80ms on ingest does nothing for the viewer. Killed it and went back to RTMP. Calling that out as a negative result in the thesis felt better than pretending it worked. The P2P layer right now uses a WebSocket relay through the tracker as fallback when WebRTC datachannels can't be established. Adds a hop. Direct WebRTC + proper STUN/TURN is on the future-work list. All benchmarks are single-machine. So peers share the same loopback, which obviously inflates the hit rates a bit. Real geo-distributed numbers would be worse, but the relative comparison still holds. 24h batching of P2P rewards instead of per-segment, because per-segment micropayments at 0.018 dollars a pop aren't economical even on L2. Per-stream channels (state channels / payment streams) could fix this but I didn't get there. What I'd actually love feedback on from this sub: The quality-aware reward formula (bytes × resolution multiplier × uptime). Is this gameable in obvious ways I'm missing? A peer can fake reporting bytes served, but the requesting peer also reports received bytes, so there's a cross-check. Still feels weak. Anyone running production P2P video at scale who can sanity-check the 88-93% savings number? My gut says it's optimistic for real cross-NAT conditions. Is governance-controlled moderation a complete dead end for anything bigger than a small DAO? Voting periods of "5 minutes to 24 hours" are useless for actual abuse response and I don't have a great answer for that.

1d ago

---

**[Get rid of layer 2](https://www.reddit.com/r/ethereum/comments/1sohm0n/get_rid_of_layer_2/)**

Is it feasible to build on layer 1 and completely get rid of layer 2?

1d ago

---

**[Daily General Discussion April 17, 2026](https://www.reddit.com/r/ethereum/comments/1snr9kw/daily_general_discussion_april_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Solana Has Processed More Transactions Than Ethereum -- Is It a Buy?](https://www.fool.com/investing/2026/04/18/with-hugetransaction-volume-is-solana-a-buy/)**

Transaction volumes are one of many ways to see how well a cryptocurrency is performing.

The Motley Fool • 17h ago

---

**[Why BitMine’s Tom Lee Sees Ethereum at $62,500 in 2030 - and What the Numbers Actually Show](https://247wallst.com/investing/2026/04/18/why-bitmines-tom-lee-sees-ethereum-at-62500-in-2030-and-what-the-numbers-actually-show/)**

Crypto investors have watched Ethereum (CRYPTO:ETH) trade in a narrow range near $2,362 while Bitcoin hovers around $76,000 and institutional money quietly builds positions in digital assets. Adoption metrics keep climbing — stablecoins on Ethereum now handle trillions in annual volume, and layer-2 networks process thousands of transactions per second. Yet price action feels stuck. ... Why BitMine’s Tom Lee Sees Ethereum at $62,500 in 2030 — and What the Numbers Actually Show

24/7 Wall St. • 1d ago

---

**[Ethereum Price Prediction: How Much Will 1 ETH Be Worth by 2030?](https://finance.yahoo.com/markets/crypto/articles/ethereum-price-prediction-much-1-175358502.html)**

Ethereum (CRYPTO: ETH) is trading around $2,350 after one of its worst quarters in years. ETH dipped by 32% in Q1, marking its third-worst first quarter since 2016. Despite the awful first quarter, Ethereum’s on-chain activity keeps hitting record highs in 2026, and ETH is up 6% over the past week. Looking at the long ... Ethereum Price Prediction: How Much Will 1 ETH Be Worth by 2030?

Yahoo Finance • 1h ago

---

**[Ethereum Flips Key Resistance, ETF Demand Returns, Analysts Eye Next Leg Higher](https://www.tradingview.com/news/newsbtc:acbe10895094b:0-ethereum-flips-key-resistance-etf-demand-returns-analysts-eye-next-leg-higher/)**

Ethereum is flashing a combination of technical and on-chain signals that analysts say could be the beginning of a meaningful recovery. For the first time in months, the structure of Ethereum’s price action appears to be shifting in the favor of bulls.The latest price action has brought the ETH pri…

TradingView • 1h ago

---

**[Ethereum co-founder Joseph Lubin warns of the dangers of AI being controlled by a few big tech firms](https://www.coindesk.com/tech/2026/04/18/ethereum-co-founder-joseph-lubin-warns-of-the-dangers-of-ai-being-controlled-by-a-few-big-tech-firms)**

In an interview with CoinDesk, the Ethereum co-founder spoke also about Ethereum’s evolution through MetaMask, stablecoins and tokenization, while downplaying quantum computing as a long-term, manageable issue.

CoinDesk • 1d ago

---

**[Bitmine Immersion: Ethereum Pivot Driving Hidden Upside (NYSE:BMNR)](https://seekingalpha.com/article/4891793-bitmine-immersion-ethereum-pivot-driving-hidden-upside)**

Bitmine Immersion’s ETH staking drives 97%+ gross margins and surging revenue, but dilution and negative cash flow raise risks. Read why BMNR stock is a buy.

Seeking Alpha • 1d ago

---

**[AAVE TVL drops $6B after $290M KelpDAO exploit, Ethereum sentiment bearish](https://cryptobriefing.com/aave-tvl-drops-6b-after-290m-kelpdao-exploit-ethereum-sentiment-bearish/)**

Aave's total value locked dropped by $6 billion after a $290 million exploit on KelpDAO. Ethereum reaching $10,000 by December 31, 2026 at 4% YES.

Crypto Briefing • 5h ago

---

**[Ethereum Price Prediction 2026: Can ETH Hit $5,000 This Year?](https://coinpedia.org/price-analysis/ethereum-price-prediction-2026-can-eth-hit-5000-this-year/)**

Ethereum price has displayed significant strength after breaking above the structure, with follow-through volume strength despite the selling pressure

Coinpedia • 1d ago

---

**[Charles Schwab begins rollout of spot bitcoin, ethereum trading platform](https://www.theblock.co/post/397756/charles-schwab-begins-rollout-spot-bitcoin-ethereum-trading-platform)**

The new platform, called Schwab Crypto, will roll out over the coming weeks and will only support bitcoin and ethereum at first.

The Block • 3d ago

---

**[Weekly ETF recap: How Bitcoin, Ethereum, Solana & XRP funds stacked up?](https://ambcrypto.com/weekly-etf-recap-how-bitcoin-ethereum-solana-xrp-funds-stacked-up/)**

AMBCrypto • 1h ago

---

---

## YouTube Videos: "ethereum"

**[🚨 BTC &amp; ETH: ITS TIME!!!!!!!!!!!!!!!](https://www.youtube.com/watch?v=U1zfC9BL5hM)**

Its a video about bitcoin, ethereum, crypto in general. But its quite an unusual one! So dont miss it! ---------- Join My FREE ...

📺 Thomas Kralow

👁️ 11K • 👍 2K • 💬 63 • ⏱️ 7:52 • 9h ago

---

**[What Just Happened!? Billions Of $ Just Exited ETH Defi As Hacker Leave Defi Protocols In Trouble!!](https://www.youtube.com/watch?v=LxUnO-6QPH4)**

Welcome back for another daily market update as always this will be a jam packed one! Join the Patreon and get exclusive ...

📺 AllinCrypto

👁️ 8K • 👍 592 • 💬 232 • ⏱️ 19:21 • 6h ago

---

**[IT’S RIGGED! Buckle Up’ Bitcoin &amp; Crypto Holders](https://www.youtube.com/watch?v=Wji5JRqdlZk)**

IT'S RIGGED! Buckle Up' Bitcoin & Crypto Holders ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 36K • 👍 2K • 💬 136 • ⏱️ 11:59 • 21h ago

---

**[More Powerful Ethereum Coming This Summer🚨Ethereum Economic Zone INTERVIEW](https://www.youtube.com/watch?v=3uuRT5Zoi5s)**

The Ethereum Economic Zone (EEZ) is a framework co-funded by the Ethereum Foundation, Gnosis, and Zisk to unify fragmented ...

📺 Paul Barron Network

👁️ 21K • 👍 1K • 💬 89 • ⏱️ 19:55 • 1d ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [2026 Realistic Prediction]](https://www.youtube.com/watch?v=o6-yoeXkA9c)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 4K • 👍 221 • 💬 19 • ⏱️ 20:54 • 1d ago

---

**[BITCOIN WARNING: The Next TRAP Just Started!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=tnFuByG5Bl0)**

BITCOIN WARNING: The Next TRAP Just Started!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 10K • 👍 397 • 💬 208 • ⏱️ 19:52 • 1d ago

---

**[Forget Ethereum — $BMNR Only Cares About Iran Now](https://www.youtube.com/watch?v=d0a2Q-odIWM)**

http://www.x10daytrading.com/?video=d0a2Q-odIWM TRADE TO $1M WHILE WORKING 9 TO 5? Copy Pro Traders With ...

📺 Wolf Of Dubai 2 - X10 DAY TRADING

👁️ 1K • 👍 53 • 💬 5 • ⏱️ 9:31 • 19h ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=6aFJrX4iix4)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 446 • 👍 66 • ⏱️ 5:07 • 5h ago

---

**[🔴BITCOIN ФИНАЛЬНЫЙ РЫВОК | АЛЬТКОЙНЫ ETH](https://www.youtube.com/watch?v=-OvyJvM6LZQ)**

Присоединяйся Telegram сообществу https://t.me/trend_gen Присоединяйся к новостному Telegram сообществу ...

📺 GENESIS LIVE

👁️ 2K • 👍 167 • 2h ago

---

**[WILL ETHEREUM DUMP LOWER?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=DZkd1_Eqzk0)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 194 • 👍 16 • 💬 1 • ⏱️ 4:47 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
