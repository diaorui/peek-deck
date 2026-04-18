---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-18T06:46:03.931837+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- videos
- social
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** April 18, 2026 at 06:46 UTC  
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

### $2,410.09

---

## Ethereum Chart

**24h:** +3.4%  
**7d:** +10.2%  
**30d:** +12.4%  
**90d:** -24.4%  
**1y:** +49.5%  

---

## Ethereum Market Stats

**Market Cap:** $290.81B
Rank #2

**Circulating Supply:** 120,690,751 ETH
No max supply

**All-Time High:** $4,946.05
-51.3%

**All-Time Low:** $0.43
+556712.2%

---

## Reddit: r/ethereum

**[Daily General Discussion April 18, 2026](https://www.reddit.com/r/ethereum/comments/1soo7xp/daily_general_discussion_april_18_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1h ago

---

**[Get rid of layer 2](https://www.reddit.com/r/ethereum/comments/1sohm0n/get_rid_of_layer_2/)**

Is it feasible to build on layer 1 and completely get rid of layer 2?

6h ago

---

**[My master's thesis project - A web3 video streaming app](https://www.reddit.com/r/ethereum/comments/1sohdzd/my_masters_thesis_project_a_web3_video_streaming/)**

Hey all. I just wrapped my master's thesis and figured this sub would actually care about the technical side instead of the price-talk side, so here goes. The thing that always bugged me about existing web3 video platforms is that each one only solves one slice of the problem. Livepeer does transcoding. Theta does P2P relay. Odysee does storage + discovery. PeerTube does federation. None of them stitch identity + gating + payouts + delivery + governance into a single app you can actually use end to end. So I tried to build that, and then benchmark it honestly to see where the real walls are. Stack ended up being: SIWE (EIP-4361) for auth, no email/password anywhere. Wallet address is the user ID across every microservice. ERC-1155 for tiered content gating (Viewer / Supporter / VIP). VIP holders also get priority + a reward multiplier in the P2P layer. 0xSplits + a thin StreamRevenue contract for per-stream revenue distribution. Anyone can trigger the payout, the platform can't withhold. StreamToken (ERC-20 + Votes) for tipping, P2P rewards, and DAO voting. OZ Governor + Timelock controlling a ModerationRegistry contract, so bans actually go through a vote instead of a mod's mood. A custom P2P tracker (Node + WebSocket) that matches viewers by Haversine distance and rewards relays based on bytes × quality multiplier × uptime bonus, instead of the flat-rate model Theta uses. IPFS via Pinata for VOD persistence, with graceful fallback to local if pinning is down. The base streaming pipeline is boring on purpose: NGINX-RTMP ingest, FFmpeg multi-bitrate HLS (1080/720/480/360), Shaka Player on the client. Everything talks to chain through a single Web3 service (ethers.js) so the Go and Python services don't each need to know about Solidity. Target deploy is Arbitrum, dev is on a local Hardhat node. Numbers from the benchmarks (single-machine docker, M4 Pro, 2 CPU / 8 GB allocated to docker so this is conservative): NFT gate verification: P95 = 43 ms (target was <100 ms). 60s Redis cache on top. Revenue API under 50 VUs: P95 = 97 ms, 0% errors at ~78 req/s. P2P browser benchmark with 20 real headless Chromium peers: 92.6% bandwidth savings, 92% hit rate, sub-linear origin growth as peers double. Gas on Arbitrum: NFT mint ~0.024 dollars, tip ~0.018 dollars, full governance lifecycle (propose+vote+queue+execute) ~0.17 dollars. On L1 the same stuff is 100-500x more, which kills the whole thing economically. L2 isn't optional. Stuff that didn't work / I want to be honest about: I tried WHIP (WebRTC ingest) for like 3 weeks. Three different approaches with Pion + FFmpeg, all of them either gave me color corruption from RTP header extensions or frozen frames from clock mismatch. Eventually realized it was pointless: HLS segment buffering (6-12s) dominates end-to-end latency, so saving 80ms on ingest does nothing for the viewer. Killed it and went back to RTMP. Calling that out as a negative result in the thesis felt better than pretending it worked. The P2P layer right now uses a WebSocket relay through the tracker as fallback when WebRTC datachannels can't be established. Adds a hop. Direct WebRTC + proper STUN/TURN is on the future-work list. All benchmarks are single-machine. So peers share the same loopback, which obviously inflates the hit rates a bit. Real geo-distributed numbers would be worse, but the relative comparison still holds. 24h batching of P2P rewards instead of per-segment, because per-segment micropayments at 0.018 dollars a pop aren't economical even on L2. Per-stream channels (state channels / payment streams) could fix this but I didn't get there. What I'd actually love feedback on from this sub: The quality-aware reward formula (bytes × resolution multiplier × uptime). Is this gameable in obvious ways I'm missing? A peer can fake reporting bytes served, but the requesting peer also reports received bytes, so there's a cross-check. Still feels weak. Anyone running production P2P video at scale who can sanity-check the 88-93% savings number? My gut says it's optimistic for real cross-NAT conditions. Is governance-controlled moderation a complete dead end for anything bigger than a small DAO? Voting periods of "5 minutes to 24 hours" are useless for actual abuse response and I don't have a great answer for that.

7h ago

---

**[Daily General Discussion April 17, 2026](https://www.reddit.com/r/ethereum/comments/1snr9kw/daily_general_discussion_april_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[I think Coinbase is building a fantastic business with stablecoins, and I would love others' opinions and thoughts.](https://www.reddit.com/r/ethereum/comments/1so3od4/i_think_coinbase_is_building_a_fantastic_business/)**

15h ago

---

**[Highlights from the All Core Developers Execution (ACDC) Call #177](https://www.reddit.com/r/ethereum/comments/1snumwg/highlights_from_the_all_core_developers_execution/)**

Glamsterdam devnets drive Ethereum’s execution readiness while Hegotá opens the next phase of upgrade proposals & protocol evolution.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-consensus-acdc-call-177/) • 22h ago

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

🔗 [youtu.be](https://youtu.be/73hHq2ua1ts?si=fwxBRn1_pW7xDziX) • 1d ago

---

**[Daily General Discussion April 15, 2026](https://www.reddit.com/r/ethereum/comments/1slwfew/daily_general_discussion_april_15_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

---

---

## Google News: "ethereum"

**[Ethereum had a record 200 million transactions in Q1. Here's what it means for ether (ETH)](https://www.coindesk.com/tech/2026/04/17/ethereum-just-had-its-busiest-quarter-ever-completing-a-three-year-comeback-on-chain)**

Quarterly transactions hit 200.4 million in Q1 2026, the first time above 200 million and more than double the 2023 lows.

CoinDesk • 23h ago

---

**[ETH Rangers Program Recap](https://blog.ethereum.org/2026/04/16/eth-rangers-recap)**

Ethereum Foundation Blog • 1d ago

---

**[Charles Schwab to launch direct bitcoin, ether trading to compete with Robinhood](https://www.cnbc.com/2026/04/16/charles-schwab-to-launch-direct-bitcoin-ethereum-trading-to-compete-with-robinhood.html)**

Charles Schwab is rolling out crypto trading, allowing clients to buy bitcoin and ether through a new arm called Schwab Crypto.

CNBC • 1d ago

---

**[Bitcoin and ethereum prices today, Friday, April 17, 2026: Higher prices hold with ceasefire in effect](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-april-17-2026-higher-prices-hold-with-ceasefire-in-effect-114918376.html)**

Bitcoin (BTC-USD) opened at $75,151.99 on Friday, 0.5% higher than Thursday’s opening price of $74,810.87. Ethereum (ETH-USD) opened at $2,348.49 on Friday, down 0.5% from Thursday’s opening price of $2,359.70.

Yahoo Finance • 18h ago

---

**[Ethereum Foundation exec Josh Stark is stepping down](https://www.theblock.co/post/397777/ethereum-foundation-exec-josh-stark-is-stepping-down)**

The move comes amid ongoing changes at the EF, including a renewed focus on scaling and developing the Ethereum mainnet.

The Block • 1d ago

---

**[Charles Schwab Weighs Prediction Markets Move as Bitcoin, Ethereum Trading Nears](https://decrypt.co/364617/charles-schwab-weighs-prediction-markets-bitcoin-ethereum-trading-nears)**

Charles Schwab President and CEO Rick Wurster indicated that America’s largest discount brokerage will likely support prediction markets.

Decrypt • 1d ago

---

**[Why Ethereum Has Become One Of The Most Heavily Shorted Assets Globally](https://www.tradingview.com/news/newsbtc:a0c30e4d6094b:0-why-ethereum-has-become-one-of-the-most-heavily-shorted-assets-globally/)**

Across global markets, Ethereum has emerged as one of the most heavily shorted assets, a positioning that reflects more than simple bearish sentiment. It signals a growing divergence between market expectations and ETH’s long-term fundamentals, placing the asset at the center of an increasingly com…

TradingView — Track All Markets • 12h ago

---

**[Most large cryptocurrencies climb on Sui, Ethereum increases](https://www.marketwatch.com/data-news/most-large-cryptocurrencies-climb-on-sui-ethereum-increases-6f01e867-dad5317f1ea1)**

MarketWatch • 16h ago

---

**[Better Crypto Buy Right Now: Ethereum vs. Solana](https://www.fool.com/investing/2026/04/17/better-crypto-buy-right-now-ethereum-vs-solana/)**

Amid the ongoing cryptocurrency bear market, these two interesting digital assets present investors with possible buy-the-dip opportunities.

The Motley Fool • 16h ago

---

**[Crypto News: Pepeto Presale Fast Sell Out Stage Whilst Ethereum Price Prediction Reaches $7,500 By Standard Chartered](https://markets.businessinsider.com/news/stocks/crypto-news-pepeto-presale-fast-sell-out-stage-whilst-ethereum-price-prediction-reaches-7-500-by-standard-chartered-1036034987)**

Dubai, UAE, April  17, 2026  (GLOBE NEWSWIRE) -- The Ethereum based token Pepeto just confirmed that its latest presale stage closed out in hours,...

markets.businessinsider.com • 2h ago

---

---

## YouTube Videos: "ethereum"

**[BITCOIN PRICE SQUEEZE: Everyone is WRONG (important)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=QY0Yi3_UQNM)**

BITCOIN PRICE SQUEEZE: Everyone is WRONG (important)!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 788 • 👍 71 • 💬 12 • ⏱️ 25:40 • 2h ago

---

**[This Ethereum Analysis Says BUY BEFORE IT&#39;S TOO LATE! Ethereum Technical Analysis 2026](https://www.youtube.com/watch?v=jgUZRil56eA)**

Buy Ethereum? CRYPTO RETIREMENT ACCOUNT HERE Sign up for iTrustCapital and get a $100 funding bonus after ...

📺 Crypto Jebb

👁️ 7K • 👍 291 • 💬 127 • ⏱️ 14:10 • 2d ago

---

**[BANKS GET IN💥 XRP BTC ETH](https://www.youtube.com/watch?v=H2GO5YxFmwc)**

xrp #bitcoin #hbar #xlm #eth 2nd Channel   https://www.youtube.com/@UCRS4Cjpn8wwoEulSsEGsvdw ...

📺 CRYPTO with KLAUS

👁️ 7K • 👍 451 • 💬 111 • ⏱️ 12:17 • 12h ago

---

**[🤩 Don&#39;t Miss The Opportunity In Ethereum !](https://www.youtube.com/watch?v=ZP5mgPEADco)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 4K • 👍 164 • 💬 21 • ⏱️ 8:23 • 1d ago

---

**[ETH ABOUT TO BREAKOUT?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=5Pu6-VHUevI)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 718 • 👍 24 • ⏱️ 4:53 • 21h ago

---

**[🚨ACİL! ETHEREUM&#39;DA TARİHİ SİNYAL YANDI! Yükselebilecek 10 Altcoin! XRP, Bonk, Ena Altcoin Analizi](https://www.youtube.com/watch?v=f54yw1SjfLw)**

Kripto para piyasasında herkes korku içindeyken, ETH grafiğinde tarihte sadece 4 kez görülen o devasa sinyal 5. kez yandı!

📺 Kripto Kafalar

👁️ 1K • 👍 156 • 💬 40 • ⏱️ 9:43 • 15h ago

---

**[Michael Saylor on Ethereum: It’s Still the Leader](https://www.youtube.com/watch?v=BtiLtGZXPX4)**

Michael Saylor's Ethereum view has changed. Bitcoin is digital capital. Ethereum is leading the tokenization race. #Bitcoin ...

📺 Bankless

👁️ 9K • 👍 199 • 💬 42 • ⏱️ 1:17 • 2d ago

---

**[URGENT $60,000 Ethereum Incoming Despite Crypto Clarity Delay $120M flows to XRP!](https://www.youtube.com/watch?v=jFuYQZuHFgw)**

URGENT $60000 Ethereum Incoming Despite Crypto Clarity Delay $120M flows to XRP! ether.fi (Partner) ...

📺 CryptoWendyO

👁️ 7K • 👍 442 • 💬 43 • ⏱️ 32:36 • 2d ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=8UP1U6xAIsk)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 383 • 👍 58 • ⏱️ 6:12 • 3h ago

---

**[Ethereum vs Canton… Is Privacy About to Take Over Crypto?](https://www.youtube.com/watch?v=Wiik0gNJdrk)**

THE WEALTH MINDSET   *** GET IN TOUCH *** SPONSOR INTEREST: mrforesightbs@gmail.com Tangem ...

📺 Grow Rich Grow Happy

👁️ 412 • 👍 86 • 💬 21 • ⏱️ 13:28 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
