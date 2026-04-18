---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-18T23:36:35.592270+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- cryptocurrency
- news
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** April 18, 2026 at 23:36 UTC  
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

### $2,358.77

---

## Ethereum Chart

**24h:** -2.8%  
**7d:** +7.5%  
**30d:** +9.7%  
**90d:** -26.2%  
**1y:** +45.8%  

---

## Ethereum Market Stats

**Market Cap:** $284.16B
Rank #2

**Circulating Supply:** 120,690,751 ETH
No max supply

**All-Time High:** $4,946.05
-52.4%

**All-Time Low:** $0.43
+543522.2%

---

## Reddit: r/ethereum

**[Daily General Discussion April 18, 2026](https://www.reddit.com/r/ethereum/comments/1soo7xp/daily_general_discussion_april_18_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

18h ago

---

**[Can someone give me feedback on an Ethereum page that I built?](https://www.reddit.com/r/ethereum/comments/1sp0z7a/can_someone_give_me_feedback_on_an_ethereum_page/)**

Hello everyone. I recently built an Ethereum page that shows how Ethereum would look if investments never lost value and I’d love someone to look at the page and give me some honest feedback on it.

7h ago

---

**[My master's thesis project - A web3 video streaming app](https://www.reddit.com/r/ethereum/comments/1sohdzd/my_masters_thesis_project_a_web3_video_streaming/)**

Hey all. I just wrapped my master's thesis and figured this sub would actually care about the technical side instead of the price-talk side, so here goes. The thing that always bugged me about existing web3 video platforms is that each one only solves one slice of the problem. Livepeer does transcoding. Theta does P2P relay. Odysee does storage + discovery. PeerTube does federation. None of them stitch identity + gating + payouts + delivery + governance into a single app you can actually use end to end. So I tried to build that, and then benchmark it honestly to see where the real walls are. Stack ended up being: SIWE (EIP-4361) for auth, no email/password anywhere. Wallet address is the user ID across every microservice. ERC-1155 for tiered content gating (Viewer / Supporter / VIP). VIP holders also get priority + a reward multiplier in the P2P layer. 0xSplits + a thin StreamRevenue contract for per-stream revenue distribution. Anyone can trigger the payout, the platform can't withhold. StreamToken (ERC-20 + Votes) for tipping, P2P rewards, and DAO voting. OZ Governor + Timelock controlling a ModerationRegistry contract, so bans actually go through a vote instead of a mod's mood. A custom P2P tracker (Node + WebSocket) that matches viewers by Haversine distance and rewards relays based on bytes × quality multiplier × uptime bonus, instead of the flat-rate model Theta uses. IPFS via Pinata for VOD persistence, with graceful fallback to local if pinning is down. The base streaming pipeline is boring on purpose: NGINX-RTMP ingest, FFmpeg multi-bitrate HLS (1080/720/480/360), Shaka Player on the client. Everything talks to chain through a single Web3 service (ethers.js) so the Go and Python services don't each need to know about Solidity. Target deploy is Arbitrum, dev is on a local Hardhat node. Numbers from the benchmarks (single-machine docker, M4 Pro, 2 CPU / 8 GB allocated to docker so this is conservative): NFT gate verification: P95 = 43 ms (target was <100 ms). 60s Redis cache on top. Revenue API under 50 VUs: P95 = 97 ms, 0% errors at ~78 req/s. P2P browser benchmark with 20 real headless Chromium peers: 92.6% bandwidth savings, 92% hit rate, sub-linear origin growth as peers double. Gas on Arbitrum: NFT mint ~0.024 dollars, tip ~0.018 dollars, full governance lifecycle (propose+vote+queue+execute) ~0.17 dollars. On L1 the same stuff is 100-500x more, which kills the whole thing economically. L2 isn't optional. Stuff that didn't work / I want to be honest about: I tried WHIP (WebRTC ingest) for like 3 weeks. Three different approaches with Pion + FFmpeg, all of them either gave me color corruption from RTP header extensions or frozen frames from clock mismatch. Eventually realized it was pointless: HLS segment buffering (6-12s) dominates end-to-end latency, so saving 80ms on ingest does nothing for the viewer. Killed it and went back to RTMP. Calling that out as a negative result in the thesis felt better than pretending it worked. The P2P layer right now uses a WebSocket relay through the tracker as fallback when WebRTC datachannels can't be established. Adds a hop. Direct WebRTC + proper STUN/TURN is on the future-work list. All benchmarks are single-machine. So peers share the same loopback, which obviously inflates the hit rates a bit. Real geo-distributed numbers would be worse, but the relative comparison still holds. 24h batching of P2P rewards instead of per-segment, because per-segment micropayments at 0.018 dollars a pop aren't economical even on L2. Per-stream channels (state channels / payment streams) could fix this but I didn't get there. What I'd actually love feedback on from this sub: The quality-aware reward formula (bytes × resolution multiplier × uptime). Is this gameable in obvious ways I'm missing? A peer can fake reporting bytes served, but the requesting peer also reports received bytes, so there's a cross-check. Still feels weak. Anyone running production P2P video at scale who can sanity-check the 88-93% savings number? My gut says it's optimistic for real cross-NAT conditions. Is governance-controlled moderation a complete dead end for anything bigger than a small DAO? Voting periods of "5 minutes to 24 hours" are useless for actual abuse response and I don't have a great answer for that.

23h ago

---

**[Get rid of layer 2](https://www.reddit.com/r/ethereum/comments/1sohm0n/get_rid_of_layer_2/)**

Is it feasible to build on layer 1 and completely get rid of layer 2?

23h ago

---

**[Daily General Discussion April 17, 2026](https://www.reddit.com/r/ethereum/comments/1snr9kw/daily_general_discussion_april_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[I think Coinbase is building a fantastic business with stablecoins, and I would love others' opinions and thoughts.](https://www.reddit.com/r/ethereum/comments/1so3od4/i_think_coinbase_is_building_a_fantastic_business/)**

1d ago

---

**[Highlights from the All Core Developers Execution (ACDC) Call #177](https://www.reddit.com/r/ethereum/comments/1snumwg/highlights_from_the_all_core_developers_execution/)**

Glamsterdam devnets drive Ethereum’s execution readiness while Hegotá opens the next phase of upgrade proposals & protocol evolution.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-consensus-acdc-call-177/) • 1d ago

---

**[Ethereal news mini #0 | Solidity developer survey results, ether.fi migrated to OP Mainnet, X $ETH cashtag](https://www.reddit.com/r/ethereum/comments/1snt515/ethereal_news_mini_0_solidity_developer_survey/)**

Solidity developer survey results, ether.fi migrated to OP Mainnet, X $ETH cashtag

🔗 [Ethereal news](https://ethereal.news/ethereal-news-mini-0/) • 1d ago

---

**[Daily General Discussion April 16, 2026](https://www.reddit.com/r/ethereum/comments/1smtw3t/daily_general_discussion_april_16_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Ep. 146 - Justin Ahn - quidli.xyz - The Daily Doots Podcast](https://www.reddit.com/r/ethereum/comments/1sn7qz6/ep_146_justin_ahn_quidlixyz_the_daily_doots/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/73hHq2ua1ts?si=fwxBRn1_pW7xDziX) • 2d ago

---

---

## Google News: "ethereum"

**[Ethereum co-founder Joseph Lubin warns of the dangers of AI being controlled by a few big tech firms](https://www.coindesk.com/tech/2026/04/18/ethereum-co-founder-joseph-lubin-warns-of-the-dangers-of-ai-being-controlled-by-a-few-big-tech-firms)**

In an interview with CoinDesk, the Ethereum co-founder spoke also about Ethereum’s evolution through MetaMask, stablecoins and tokenization, while downplaying quantum computing as a long-term, manageable issue.

CoinDesk • 4h ago

---

**[Why BitMine’s Tom Lee Sees Ethereum at $62,500 in 2030 - and What the Numbers Actually Show](https://247wallst.com/investing/2026/04/18/why-bitmines-tom-lee-sees-ethereum-at-62500-in-2030-and-what-the-numbers-actually-show/)**

Crypto investors have watched Ethereum (CRYPTO:ETH) trade in a narrow range near $2,362 while Bitcoin hovers around $76,000 and institutional money quietly builds positions in digital assets. Adoption metrics keep climbing — stablecoins on Ethereum now handle trillions in annual volume, and layer-2 networks process thousands of transactions per second. Yet price action feels stuck. ... Why BitMine’s Tom Lee Sees Ethereum at $62,500 in 2030 — and What the Numbers Actually Show

24/7 Wall St. • 11h ago

---

**[Charles Schwab CEO on launching bitcoin, ethereum trading](https://www.cnbc.com/video/2026/04/16/charles-schwab-ceo-on-launching-bitcoin-ethereum-trading.html)**

Charles Schwab CEO Rick Wurster joins 'Money Movers' to discuss the company's latest earnings report, market themes, and more.

CNBC • 2d ago

---

**[Charles Schwab begins rollout of spot bitcoin, ethereum trading platform](https://www.theblock.co/post/397756/charles-schwab-begins-rollout-spot-bitcoin-ethereum-trading-platform)**

The new platform, called Schwab Crypto, will roll out over the coming weeks and will only support bitcoin and ethereum at first.

The Block • 2d ago

---

**[Charles Schwab Weighs Prediction Markets Move as Bitcoin, Ethereum Trading Nears](https://decrypt.co/364617/charles-schwab-weighs-prediction-markets-bitcoin-ethereum-trading-nears)**

Charles Schwab President and CEO Rick Wurster indicated that America’s largest discount brokerage will likely support prediction markets.

Decrypt • 2d ago

---

**[Crypto Trader Turns $2,500 Into $500K on Skyrocketing Ethereum Meme Coin](https://finance.yahoo.com/markets/crypto/articles/crypto-trader-turns-2-500-182605699.html)**

A meme coin trader turned $2,500 into nearly $500,000 in a matter of hours via the Elon Musk-linked ASTEROID token on Ethereum.

Yahoo Finance • 1d ago

---

**[Ethereum Foundation exec Josh Stark is stepping down](https://www.theblock.co/post/397777/ethereum-foundation-exec-josh-stark-is-stepping-down)**

The move comes amid ongoing changes at the EF, including a renewed focus on scaling and developing the Ethereum mainnet.

The Block • 2d ago

---

**[Should You Buy Ethereum Before the Next Crypto Bull Run?](https://www.fool.com/investing/2026/04/18/should-you-buy-crypto-before-the-next-crypto-bull/)**

This blockchain is a lot more formidable than in the past.

The Motley Fool • 4h ago

---

**[When Will The Ethereum Price Hit $5,000 And $10,000?](https://www.tradingview.com/news/newsbtc:08000b09e094b:0-when-will-the-ethereum-price-hit-5-000-and-10-000/)**

In the last bull run, when the Bitcoin price surged and crossed $100,000, the Ethereum price was expected to follow the same trajectory as it had in the past. But that was not the case, and the second-largest cryptocurrency by market cap was barely able to cross its previous all-time high price, bu…

TradingView — Track All Markets • 13h ago

---

**[Bitcoin Nears $75,000 as XRP Jumps. How Cryptos Can Break Out.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-cryptos-today-351ec782)**

Barron's • 2d ago

---

---

## YouTube Videos: "ethereum"

**[More Powerful Ethereum Coming This Summer🚨Ethereum Economic Zone INTERVIEW](https://www.youtube.com/watch?v=3uuRT5Zoi5s)**

The Ethereum Economic Zone (EEZ) is a framework co-funded by the Ethereum Foundation, Gnosis, and Zisk to unify fragmented ...

📺 Paul Barron Network

👁️ 10K • 👍 669 • 💬 33 • ⏱️ 19:55 • 7h ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [2026 Realistic Prediction]](https://www.youtube.com/watch?v=o6-yoeXkA9c)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 1K • 👍 117 • 💬 6 • ⏱️ 20:54 • 7h ago

---

**[BITCOIN WARNING: The Next TRAP Just Started!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=tnFuByG5Bl0)**

BITCOIN WARNING: The Next TRAP Just Started!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 2K • 👍 188 • 💬 27 • ⏱️ 19:52 • 4h ago

---

**[Michael Saylor on Ethereum: It’s Still the Leader](https://www.youtube.com/watch?v=BtiLtGZXPX4)**

Michael Saylor's Ethereum view has changed. Bitcoin is digital capital. Ethereum is leading the tokenization race. #Bitcoin ...

📺 Bankless

👁️ 12K • 👍 248 • 💬 45 • ⏱️ 1:17 • 3d ago

---

**[🤩 Don&#39;t Miss The Opportunity In Ethereum !](https://www.youtube.com/watch?v=ZP5mgPEADco)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 5K • 👍 167 • 💬 21 • ⏱️ 8:23 • 2d ago

---

**[WILL ETHEREUM DUMP NOW?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=A7nVwLwBVNs)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 212 • 👍 13 • ⏱️ 5:31 • 14h ago

---

**[Bitcoin Warning: Why BTC Hasn&#39;t Bottomed — Plus ETH, SOL, XRP &amp; Altcoin Targets](https://www.youtube.com/watch?v=qSxd31mu0UQ)**

Gareth Soloway, Chief Market Strategist at Verified Investing, breaks down the latest crypto price action across Bitcoin, Ethereum, ...

📺 Verified Pro Traders

👁️ 17K • 👍 1K • 💬 321 • ⏱️ 8:13 • 1d ago

---

**[Everything is Surprising ? Latest Crypto Market News Today &amp; BTC - ETH Analysis](https://www.youtube.com/watch?v=yIATT4AGalo)**

Everything is Surprising ? Latest Crypto Market News Today & BTC - ETH Analysis Welcome to Al Makkah Tech & Business Hub!

📺 AL MAKKAH TECH & BUSINESS HUB

👁️ 695 • 👍 135 • 💬 14 • ⏱️ 13:25 • 4h ago

---

**[Insane Ethereum Fractal: Ignite Altcoins Or Trap Bulls...](https://www.youtube.com/watch?v=MM9bTgBSVrQ)**

Ethereum is flashing a fractal that mirrors the November 2024 altcoin breakout, and the setup is showing up across Cardano, Sui, ...

📺 Crypto Capital Venture

👁️ 9K • 👍 549 • 💬 212 • ⏱️ 11:01 • 2d ago

---

**[This Bitcoin &amp; Ethereum Move Will SHOCK The Market](https://www.youtube.com/watch?v=t8fLZXrAxf0)**

In this video, we're diving deep into the implications of a CIA operation on blockchain and Bitcoin investments, questioning the ...

📺 TMG Trades

👁️ 926 • 👍 78 • 💬 29 • ⏱️ 12:42 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*
