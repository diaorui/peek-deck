---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-18T02:31:12.062265+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- videos
- cryptocurrency
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** April 18, 2026 at 02:31 UTC  
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

### $2,420.18

---

## Ethereum Chart

**24h:** +4.1%  
**7d:** +10.7%  
**30d:** +12.9%  
**90d:** -24.0%  
**1y:** +50.1%  

---

## Ethereum Market Stats

**Market Cap:** $292.48B
Rank #2

**Circulating Supply:** 120,690,751 ETH
No max supply

**All-Time High:** $4,946.05
-51.0%

**All-Time Low:** $0.43
+559474.5%

---

## Reddit: r/ethereum

**[Daily General Discussion April 17, 2026](https://www.reddit.com/r/ethereum/comments/1snr9kw/daily_general_discussion_april_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

21h ago

---

**[Get rid of layer 2](https://www.reddit.com/r/ethereum/comments/1sohm0n/get_rid_of_layer_2/)**

Is it feasible to build on layer 1 and completely get rid of layer 2?

2h ago

---

**[My master's thesis project - A web3 video streaming app](https://www.reddit.com/r/ethereum/comments/1sohdzd/my_masters_thesis_project_a_web3_video_streaming/)**

Hey all. I just wrapped my master's thesis and figured this sub would actually care about the technical side instead of the price-talk side, so here goes. The thing that always bugged me about existing web3 video platforms is that each one only solves one slice of the problem. Livepeer does transcoding. Theta does P2P relay. Odysee does storage + discovery. PeerTube does federation. None of them stitch identity + gating + payouts + delivery + governance into a single app you can actually use end to end. So I tried to build that, and then benchmark it honestly to see where the real walls are. Stack ended up being: SIWE (EIP-4361) for auth, no email/password anywhere. Wallet address is the user ID across every microservice. ERC-1155 for tiered content gating (Viewer / Supporter / VIP). VIP holders also get priority + a reward multiplier in the P2P layer. 0xSplits + a thin StreamRevenue contract for per-stream revenue distribution. Anyone can trigger the payout, the platform can't withhold. StreamToken (ERC-20 + Votes) for tipping, P2P rewards, and DAO voting. OZ Governor + Timelock controlling a ModerationRegistry contract, so bans actually go through a vote instead of a mod's mood. A custom P2P tracker (Node + WebSocket) that matches viewers by Haversine distance and rewards relays based on bytes × quality multiplier × uptime bonus, instead of the flat-rate model Theta uses. IPFS via Pinata for VOD persistence, with graceful fallback to local if pinning is down. The base streaming pipeline is boring on purpose: NGINX-RTMP ingest, FFmpeg multi-bitrate HLS (1080/720/480/360), Shaka Player on the client. Everything talks to chain through a single Web3 service (ethers.js) so the Go and Python services don't each need to know about Solidity. Target deploy is Arbitrum, dev is on a local Hardhat node. Numbers from the benchmarks (single-machine docker, M4 Pro, 2 CPU / 8 GB allocated to docker so this is conservative): NFT gate verification: P95 = 43 ms (target was <100 ms). 60s Redis cache on top. Revenue API under 50 VUs: P95 = 97 ms, 0% errors at ~78 req/s. P2P browser benchmark with 20 real headless Chromium peers: 92.6% bandwidth savings, 92% hit rate, sub-linear origin growth as peers double. Gas on Arbitrum: NFT mint ~0.024 dollars, tip ~0.018 dollars, full governance lifecycle (propose+vote+queue+execute) ~0.17 dollars. On L1 the same stuff is 100-500x more, which kills the whole thing economically. L2 isn't optional. Stuff that didn't work / I want to be honest about: I tried WHIP (WebRTC ingest) for like 3 weeks. Three different approaches with Pion + FFmpeg, all of them either gave me color corruption from RTP header extensions or frozen frames from clock mismatch. Eventually realized it was pointless: HLS segment buffering (6-12s) dominates end-to-end latency, so saving 80ms on ingest does nothing for the viewer. Killed it and went back to RTMP. Calling that out as a negative result in the thesis felt better than pretending it worked. The P2P layer right now uses a WebSocket relay through the tracker as fallback when WebRTC datachannels can't be established. Adds a hop. Direct WebRTC + proper STUN/TURN is on the future-work list. All benchmarks are single-machine. So peers share the same loopback, which obviously inflates the hit rates a bit. Real geo-distributed numbers would be worse, but the relative comparison still holds. 24h batching of P2P rewards instead of per-segment, because per-segment micropayments at 0.018 dollars a pop aren't economical even on L2. Per-stream channels (state channels / payment streams) could fix this but I didn't get there. What I'd actually love feedback on from this sub: The quality-aware reward formula (bytes × resolution multiplier × uptime). Is this gameable in obvious ways I'm missing? A peer can fake reporting bytes served, but the requesting peer also reports received bytes, so there's a cross-check. Still feels weak. Anyone running production P2P video at scale who can sanity-check the 88-93% savings number? My gut says it's optimistic for real cross-NAT conditions. Is governance-controlled moderation a complete dead end for anything bigger than a small DAO? Voting periods of "5 minutes to 24 hours" are useless for actual abuse response and I don't have a great answer for that.

2h ago

---

**[I think Coinbase is building a fantastic business with stablecoins, and I would love others' opinions and thoughts.](https://www.reddit.com/r/ethereum/comments/1so3od4/i_think_coinbase_is_building_a_fantastic_business/)**

11h ago

---

**[Highlights from the All Core Developers Execution (ACDC) Call #177](https://www.reddit.com/r/ethereum/comments/1snumwg/highlights_from_the_all_core_developers_execution/)**

Glamsterdam devnets drive Ethereum’s execution readiness while Hegotá opens the next phase of upgrade proposals & protocol evolution.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-consensus-acdc-call-177/) • 18h ago

---

**[Ethereal news mini #0 | Solidity developer survey results, ether.fi migrated to OP Mainnet, X $ETH cashtag](https://www.reddit.com/r/ethereum/comments/1snt515/ethereal_news_mini_0_solidity_developer_survey/)**

Solidity developer survey results, ether.fi migrated to OP Mainnet, X $ETH cashtag

🔗 [Ethereal news](https://ethereal.news/ethereal-news-mini-0/) • 19h ago

---

**[Daily General Discussion April 16, 2026](https://www.reddit.com/r/ethereum/comments/1smtw3t/daily_general_discussion_april_16_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Ep. 146 - Justin Ahn - quidli.xyz - The Daily Doots Podcast](https://www.reddit.com/r/ethereum/comments/1sn7qz6/ep_146_justin_ahn_quidlixyz_the_daily_doots/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/73hHq2ua1ts?si=fwxBRn1_pW7xDziX) • 1d ago

---

**[Daily General Discussion April 15, 2026](https://www.reddit.com/r/ethereum/comments/1slwfew/daily_general_discussion_april_15_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Apple Charges $99 a Year to Keep You Safe. A Fake Ledger App Just Drained $9.5 Million in a Week](https://www.reddit.com/r/ethereum/comments/1slh9gu/apple_charges_99_a_year_to_keep_you_safe_a_fake/)**

A fake Ledger Live clone sat on Apple's App Store for seven days and drained $9.5 million from 50 victims across Bitcoin, Ethereum, Solana, Tron and XRP. Apple's review process, which promises to protect users, let it through. Then removed it after the damage was done.

🔗 [DailyCoinPost](https://dailycoinpost.com/fake-ledger-app-apple-app-store-9-million-drained/) • 3d ago

---

---

## Google News: "ethereum"

**[Ethereum had a record 200 million transactions in Q1. Here's what it means for ether (ETH)](https://www.coindesk.com/tech/2026/04/17/ethereum-just-had-its-busiest-quarter-ever-completing-a-three-year-comeback-on-chain)**

Quarterly transactions hit 200.4 million in Q1 2026, the first time above 200 million and more than double the 2023 lows.

CoinDesk • 19h ago

---

**[Ethereum Foundation exec Josh Stark is stepping down](https://www.theblock.co/post/397777/ethereum-foundation-exec-josh-stark-is-stepping-down)**

The move comes amid ongoing changes at the EF, including a renewed focus on scaling and developing the Ethereum mainnet.

The Block • 1d ago

---

**[XRP Price: XRP Flips BNB to Become the Fourth-Largest Crypto — Can It Catch Ethereum Next?](https://finance.yahoo.com/markets/crypto/articles/xrp-price-xrp-flips-bnb-220806496.html)**

XRP (CRYPTO: XRP) initially reclaimed the number four spot in global crypto rankings in mid-March, overtaking BNB with a market cap of around $93 billion before the two assets traded places again. BNB reclaimed fourth briefly on March 23, reaching an $85.9 billion market cap versus XRP’s $85 billion, but the gap between the two ... XRP Price: XRP Flips BNB to Become the Fourth-Largest Crypto — Can It Catch Ethereum Next?

Yahoo Finance • 4h ago

---

**[Charles Schwab begins rollout of spot bitcoin, ethereum trading platform](https://www.theblock.co/post/397756/charles-schwab-begins-rollout-spot-bitcoin-ethereum-trading-platform)**

The new platform, called Schwab Crypto, will roll out over the coming weeks and will only support bitcoin and ethereum at first.

The Block • 1d ago

---

**[Charles Schwab to launch direct bitcoin, ether trading to compete with Robinhood](https://www.cnbc.com/2026/04/16/charles-schwab-to-launch-direct-bitcoin-ethereum-trading-to-compete-with-robinhood.html)**

Charles Schwab is rolling out crypto trading, allowing clients to buy bitcoin and ether through a new arm called Schwab Crypto.

CNBC • 1d ago

---

**[Charles Schwab Weighs Prediction Markets Move as Bitcoin, Ethereum Trading Nears](https://decrypt.co/364617/charles-schwab-weighs-prediction-markets-bitcoin-ethereum-trading-nears)**

Charles Schwab President and CEO Rick Wurster indicated that America’s largest discount brokerage will likely support prediction markets.

Decrypt • 1d ago

---

**[Why Ethereum Has Become One Of The Most Heavily Shorted Assets Globally](https://www.tradingview.com/news/newsbtc:a0c30e4d6094b:0-why-ethereum-has-become-one-of-the-most-heavily-shorted-assets-globally/)**

Across global markets, Ethereum has emerged as one of the most heavily shorted assets, a positioning that reflects more than simple bearish sentiment. It signals a growing divergence between market expectations and ETH’s long-term fundamentals, placing the asset at the center of an increasingly com…

TradingView — Track All Markets • 8h ago

---

**[Most large cryptocurrencies climb on Sui, Ethereum increases](https://www.marketwatch.com/data-news/most-large-cryptocurrencies-climb-on-sui-ethereum-increases-6f01e867-dad5317f1ea1)**

MarketWatch • 12h ago

---

**[Better Crypto Buy Right Now: Ethereum vs. Solana](https://www.fool.com/investing/2026/04/17/better-crypto-buy-right-now-ethereum-vs-solana/)**

Amid the ongoing cryptocurrency bear market, these two interesting digital assets present investors with possible buy-the-dip opportunities.

The Motley Fool • 12h ago

---

**[ETH Rangers Program Recap](https://blog.ethereum.org/2026/04/16/eth-rangers-recap)**

Ethereum Foundation Blog • 1d ago

---

---

## YouTube Videos: "ethereum"

**[🤩 Don&#39;t Miss The Opportunity In Ethereum !](https://www.youtube.com/watch?v=ZP5mgPEADco)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 4K • 👍 164 • 💬 21 • ⏱️ 8:23 • 1d ago

---

**[ETH ABOUT TO BREAKOUT?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=5Pu6-VHUevI)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 687 • 👍 24 • ⏱️ 4:53 • 17h ago

---

**[Something BIG Just Happened to Cardano - BTC, Ethereum &amp; Solana Joined](https://www.youtube.com/watch?v=yBXFD_ktHK0)**

MALU Stake Pool: pool18zf8txwv8lmtpq2src8wrhz0pjut5qft8h5tfxnctwc95r7jvvj 🗳️ DRep ID: ...

📺 Linda CryptoFly

👁️ 2K • 👍 193 • 💬 32 • ⏱️ 3:21 • 10h ago

---

**[URGENT $60,000 Ethereum Incoming Despite Crypto Clarity Delay $120M flows to XRP!](https://www.youtube.com/watch?v=jFuYQZuHFgw)**

URGENT $60000 Ethereum Incoming Despite Crypto Clarity Delay $120M flows to XRP! ether.fi (Partner) ...

📺 CryptoWendyO

👁️ 7K • 👍 442 • 💬 43 • ⏱️ 32:36 • 2d ago

---

**[BANKS GET IN💥 XRP BTC ETH](https://www.youtube.com/watch?v=H2GO5YxFmwc)**

xrp #bitcoin #hbar #xlm #eth 2nd Channel   https://www.youtube.com/@UCRS4Cjpn8wwoEulSsEGsvdw ...

📺 CRYPTO with KLAUS

👁️ 6K • 👍 434 • 💬 109 • ⏱️ 12:17 • 8h ago

---

**[AI Agents, Tokenization, and Ethereum’s Next Wave | Raoul Pal the Journey Man](https://www.youtube.com/watch?v=855YrRfkyIc)**

Raoul welcomes Vivek Raman, Co-Founder and CEO of Etherealize, and Danny Ryan, Co-Founder and President at Etherealize, ...

📺 Raoul Pal The Journey Man

👁️ 7K • 👍 291 • 💬 13 • ⏱️ 1:11:56 • 1d ago

---

**[Michael Saylor on Ethereum: It’s Still the Leader](https://www.youtube.com/watch?v=BtiLtGZXPX4)**

Michael Saylor's Ethereum view has changed. Bitcoin is digital capital. Ethereum is leading the tokenization race. #Bitcoin ...

📺 Bankless

👁️ 9K • 👍 187 • 💬 41 • ⏱️ 1:17 • 2d ago

---

**[Tom Lee :&quot;Bitcoin &amp; ETH Holders NEED to Hear This IMMEDIATELY [2026 New Price Prediction]](https://www.youtube.com/watch?v=DVUa0wyPWzQ)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 6K • 👍 258 • 💬 14 • ⏱️ 14:46 • 2d ago

---

**[Insane Ethereum Fractal: Ignite Altcoins Or Trap Bulls...](https://www.youtube.com/watch?v=MM9bTgBSVrQ)**

Ethereum is flashing a fractal that mirrors the November 2024 altcoin breakout, and the setup is showing up across Cardano, Sui, ...

📺 Crypto Capital Venture

👁️ 9K • 👍 545 • 💬 149 • ⏱️ 11:01 • 1d ago

---

**[How High Can Ethereum Go? ETH Crypto Analysis](https://www.youtube.com/watch?v=x3IFOoyL0UA)**

In this video, I analyze the price action of Ethereum using custom indicators to predict the potential future trend. DM "4LIGHT" Up ...

📺 Crypto 4Light

👁️ 117 • 👍 4 • 💬 1 • ⏱️ 9:39 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*
