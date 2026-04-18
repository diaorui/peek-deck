---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-18T14:09:42.232312+00:00'
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

**Last Updated:** April 18, 2026 at 14:09 UTC  
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

### $2,350.00

---

## Ethereum Chart

**24h:** -3.6%  
**7d:** +7.6%  
**30d:** +9.8%  
**90d:** -26.1%  
**1y:** +46.0%  

---

## Ethereum Market Stats

**Market Cap:** $284.38B
Rank #2

**Circulating Supply:** 120,690,751 ETH
No max supply

**All-Time High:** $4,946.05
-52.4%

**All-Time Low:** $0.43
+544076.5%

---

## Reddit: r/ethereum

**[Daily General Discussion April 18, 2026](https://www.reddit.com/r/ethereum/comments/1soo7xp/daily_general_discussion_april_18_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

9h ago

---

**[The .eth.limo domain is compromised, don't trust vitalik.eth.limo or any other .eth.limo domain](https://www.reddit.com/r/ethereum/comments/1soshkj/the_ethlimo_domain_is_compromised_dont_trust/)**

Join the conversation on Firefly: follow, comment and engage with Web3 social posts in real time.

🔗 [firefly.social](https://firefly.social/post/bsky/qmajrxvehl6ss6w2h4uuv5bg_3mjqy6376q22j) • 5h ago

---

**[Get rid of layer 2](https://www.reddit.com/r/ethereum/comments/1sohm0n/get_rid_of_layer_2/)**

Is it feasible to build on layer 1 and completely get rid of layer 2?

14h ago

---

**[My master's thesis project - A web3 video streaming app](https://www.reddit.com/r/ethereum/comments/1sohdzd/my_masters_thesis_project_a_web3_video_streaming/)**

Hey all. I just wrapped my master's thesis and figured this sub would actually care about the technical side instead of the price-talk side, so here goes. The thing that always bugged me about existing web3 video platforms is that each one only solves one slice of the problem. Livepeer does transcoding. Theta does P2P relay. Odysee does storage + discovery. PeerTube does federation. None of them stitch identity + gating + payouts + delivery + governance into a single app you can actually use end to end. So I tried to build that, and then benchmark it honestly to see where the real walls are. Stack ended up being: SIWE (EIP-4361) for auth, no email/password anywhere. Wallet address is the user ID across every microservice. ERC-1155 for tiered content gating (Viewer / Supporter / VIP). VIP holders also get priority + a reward multiplier in the P2P layer. 0xSplits + a thin StreamRevenue contract for per-stream revenue distribution. Anyone can trigger the payout, the platform can't withhold. StreamToken (ERC-20 + Votes) for tipping, P2P rewards, and DAO voting. OZ Governor + Timelock controlling a ModerationRegistry contract, so bans actually go through a vote instead of a mod's mood. A custom P2P tracker (Node + WebSocket) that matches viewers by Haversine distance and rewards relays based on bytes × quality multiplier × uptime bonus, instead of the flat-rate model Theta uses. IPFS via Pinata for VOD persistence, with graceful fallback to local if pinning is down. The base streaming pipeline is boring on purpose: NGINX-RTMP ingest, FFmpeg multi-bitrate HLS (1080/720/480/360), Shaka Player on the client. Everything talks to chain through a single Web3 service (ethers.js) so the Go and Python services don't each need to know about Solidity. Target deploy is Arbitrum, dev is on a local Hardhat node. Numbers from the benchmarks (single-machine docker, M4 Pro, 2 CPU / 8 GB allocated to docker so this is conservative): NFT gate verification: P95 = 43 ms (target was <100 ms). 60s Redis cache on top. Revenue API under 50 VUs: P95 = 97 ms, 0% errors at ~78 req/s. P2P browser benchmark with 20 real headless Chromium peers: 92.6% bandwidth savings, 92% hit rate, sub-linear origin growth as peers double. Gas on Arbitrum: NFT mint ~0.024 dollars, tip ~0.018 dollars, full governance lifecycle (propose+vote+queue+execute) ~0.17 dollars. On L1 the same stuff is 100-500x more, which kills the whole thing economically. L2 isn't optional. Stuff that didn't work / I want to be honest about: I tried WHIP (WebRTC ingest) for like 3 weeks. Three different approaches with Pion + FFmpeg, all of them either gave me color corruption from RTP header extensions or frozen frames from clock mismatch. Eventually realized it was pointless: HLS segment buffering (6-12s) dominates end-to-end latency, so saving 80ms on ingest does nothing for the viewer. Killed it and went back to RTMP. Calling that out as a negative result in the thesis felt better than pretending it worked. The P2P layer right now uses a WebSocket relay through the tracker as fallback when WebRTC datachannels can't be established. Adds a hop. Direct WebRTC + proper STUN/TURN is on the future-work list. All benchmarks are single-machine. So peers share the same loopback, which obviously inflates the hit rates a bit. Real geo-distributed numbers would be worse, but the relative comparison still holds. 24h batching of P2P rewards instead of per-segment, because per-segment micropayments at 0.018 dollars a pop aren't economical even on L2. Per-stream channels (state channels / payment streams) could fix this but I didn't get there. What I'd actually love feedback on from this sub: The quality-aware reward formula (bytes × resolution multiplier × uptime). Is this gameable in obvious ways I'm missing? A peer can fake reporting bytes served, but the requesting peer also reports received bytes, so there's a cross-check. Still feels weak. Anyone running production P2P video at scale who can sanity-check the 88-93% savings number? My gut says it's optimistic for real cross-NAT conditions. Is governance-controlled moderation a complete dead end for anything bigger than a small DAO? Voting periods of "5 minutes to 24 hours" are useless for actual abuse response and I don't have a great answer for that.

14h ago

---

**[The Blockchain Raised Half A Billion Dollars And Forgot To Build A F******Blockchain.](https://www.reddit.com/r/ethereum/comments/1sothv6/the_blockchain_raised_half_a_billion_dollars_and/)**

4h ago

---

**[Daily General Discussion April 17, 2026](https://www.reddit.com/r/ethereum/comments/1snr9kw/daily_general_discussion_april_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[I think Coinbase is building a fantastic business with stablecoins, and I would love others' opinions and thoughts.](https://www.reddit.com/r/ethereum/comments/1so3od4/i_think_coinbase_is_building_a_fantastic_business/)**

23h ago

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

---

## Google News: "ethereum"

**[Ethereum had a record 200 million transactions in Q1. Here's what it means for ether (ETH)](https://www.coindesk.com/tech/2026/04/17/ethereum-just-had-its-busiest-quarter-ever-completing-a-three-year-comeback-on-chain)**

Quarterly transactions hit 200.4 million in Q1 2026, the first time above 200 million and more than double the 2023 lows.

CoinDesk • 1d ago

---

**[Crypto Trader Turns $2,500 Into $500K on Skyrocketing Ethereum Meme Coin](https://decrypt.co/364767/crypto-trader-turns-2500-into-500k-skyrocketing-ethereum-meme-coin)**

A meme coin trader turned $2,500 into nearly $500,000 in a matter of hours via the Elon Musk-linked ASTEROID token on Ethereum.

Decrypt • 19h ago

---

**[Why BitMine’s Tom Lee Sees Ethereum at $62,500 in 2030 — and What the Numbers Actually Show](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-tom-lee-sees-121409901.html)**

Crypto investors have watched Ethereum (CRYPTO:ETH) trade in a narrow range near $2,362 while Bitcoin hovers around $76,000 and institutional money quietly builds positions in digital assets. Adoption metrics keep climbing — stablecoins on Ethereum now handle trillions in annual volume, and layer-2 networks process thousands of transactions per second. Yet price action feels stuck. ... Why BitMine’s Tom Lee Sees Ethereum at $62,500 in 2030 — and What the Numbers Actually Show

Yahoo Finance • 1h ago

---

**[When Will The Ethereum Price Hit $5,000 And $10,000?](https://www.tradingview.com/news/newsbtc:08000b09e094b:0-when-will-the-ethereum-price-hit-5-000-and-10-000/)**

In the last bull run, when the Bitcoin price surged and crossed $100,000, the Ethereum price was expected to follow the same trajectory as it had in the past. But that was not the case, and the second-largest cryptocurrency by market cap was barely able to cross its previous all-time high price, bu…

TradingView — Track All Markets • 4h ago

---

**[Ethereum co-founder Joseph Lubin warns of the dangers of AI being controlled by a few big tech firms](https://www.coindesk.com/tech/2026/04/18/ethereum-co-founder-joseph-lubin-warns-of-the-dangers-of-ai-being-controlled-by-a-few-big-tech-firms)**

In an interview with CoinDesk, the Ethereum co-founder spoke also about Ethereum’s evolution through MetaMask, stablecoins and tokenization, while downplaying quantum computing as a long-term, manageable issue.

CoinDesk • 1h ago

---

**[Charles Schwab to launch direct bitcoin, ether trading to compete with Robinhood](https://www.cnbc.com/2026/04/16/charles-schwab-to-launch-direct-bitcoin-ethereum-trading-to-compete-with-robinhood.html)**

Charles Schwab is rolling out crypto trading, allowing clients to buy bitcoin and ether through a new arm called Schwab Crypto.

CNBC • 2d ago

---

**[Ethereum Foundation exec Josh Stark is stepping down](https://www.theblock.co/post/397777/ethereum-foundation-exec-josh-stark-is-stepping-down)**

The move comes amid ongoing changes at the EF, including a renewed focus on scaling and developing the Ethereum mainnet.

The Block • 1d ago

---

**[Bitcoin Nears $75,000 as XRP Jumps. How Cryptos Can Break Out.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-cryptos-today-351ec782)**

Barron's • 1d ago

---

**[Crypto News: Pepeto Presale Fast Sell Out Stage Whilst Ethereum Price Prediction Reaches $7,500 By Standard Chartered](https://markets.businessinsider.com/news/stocks/crypto-news-pepeto-presale-fast-sell-out-stage-whilst-ethereum-price-prediction-reaches-7-500-by-standard-chartered-1036034987)**

Dubai, UAE, April  17, 2026  (GLOBE NEWSWIRE) -- The Ethereum based token Pepeto just confirmed that its latest presale stage closed out in hours,...

markets.businessinsider.com • 10h ago

---

**[Ethereum Price Nears Breakout: Can ETH Rally Toward $3,000 Next?](https://coinpedia.org/price-analysis/ethereum-price-nears-breakout-can-eth-rally-toward-3000-next/)**

Ethereum is edging closer to a breakout, and the current setup is beginning to draw serious attention. After weeks of sideways movement, ETH is now

Coinpedia • 2d ago

---

---

## YouTube Videos: "ethereum"

**[BITCOIN PRICE SQUEEZE: Everyone is WRONG (important)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=QY0Yi3_UQNM)**

BITCOIN PRICE SQUEEZE: Everyone is WRONG (important)!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 5K • 👍 291 • 💬 44 • ⏱️ 25:40 • 9h ago

---

**[WILL ETHEREUM DUMP NOW?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=A7nVwLwBVNs)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 96 • 👍 9 • ⏱️ 5:31 • 4h ago

---

**[🤩 Don&#39;t Miss The Opportunity In Ethereum !](https://www.youtube.com/watch?v=ZP5mgPEADco)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 4K • 👍 166 • 💬 21 • ⏱️ 8:23 • 2d ago

---

**[BANKS GET IN💥 XRP BTC ETH](https://www.youtube.com/watch?v=H2GO5YxFmwc)**

xrp #bitcoin #hbar #xlm #eth 2nd Channel   https://www.youtube.com/@UCRS4Cjpn8wwoEulSsEGsvdw ...

📺 CRYPTO with KLAUS

👁️ 7K • 👍 470 • 💬 197 • ⏱️ 12:17 • 19h ago

---

**[Insane Ethereum Fractal: Ignite Altcoins Or Trap Bulls...](https://www.youtube.com/watch?v=MM9bTgBSVrQ)**

Ethereum is flashing a fractal that mirrors the November 2024 altcoin breakout, and the setup is showing up across Cardano, Sui, ...

📺 Crypto Capital Venture

👁️ 9K • 👍 546 • 💬 143 • ⏱️ 11:01 • 2d ago

---

**[Michael Saylor on Ethereum: It’s Still the Leader](https://www.youtube.com/watch?v=BtiLtGZXPX4)**

Michael Saylor's Ethereum view has changed. Bitcoin is digital capital. Ethereum is leading the tokenization race. #Bitcoin ...

📺 Bankless

👁️ 11K • 👍 223 • 💬 45 • ⏱️ 1:17 • 2d ago

---

**[Ethereum vs Canton… Is Privacy About to Take Over Crypto?](https://www.youtube.com/watch?v=Wiik0gNJdrk)**

THE WEALTH MINDSET   *** GET IN TOUCH *** SPONSOR INTEREST: mrforesightbs@gmail.com Tangem ...

📺 Grow Rich Grow Happy

👁️ 628 • 👍 106 • 💬 25 • ⏱️ 13:28 • 14h ago

---

**[AI Agents, Tokenization, and Ethereum’s Next Wave | Raoul Pal the Journey Man](https://www.youtube.com/watch?v=855YrRfkyIc)**

Raoul welcomes Vivek Raman, Co-Founder and CEO of Etherealize, and Danny Ryan, Co-Founder and President at Etherealize, ...

📺 Raoul Pal The Journey Man

👁️ 8K • 👍 329 • 💬 16 • ⏱️ 1:11:56 • 2d ago

---

**[ETH ABOUT TO BREAKOUT?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=5Pu6-VHUevI)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 799 • 👍 24 • ⏱️ 4:53 • 1d ago

---

**[Ethereum (ETH) - Análise de hoje, 18/04/2026 #ETH #Ethereum #BTC #bitcoin #XRP #vitalik #ETH](https://www.youtube.com/watch?v=5izGJ3GlSpw)**

ASSINE agora GEMAS Altcoins Alert !!! - (R$100/mês): https://pay.hotmart.com/Y93614691E https://degenscan.io #eth #BTC ...

📺 Trade with Renato Ulianov

👁️ 295 • 👍 69 • 💬 1 • ⏱️ 2:31 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
