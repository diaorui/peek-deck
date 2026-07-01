---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-07-01T03:58:55.882983+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** July 01, 2026 at 03:58 UTC  
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

### $1,591.00

---

## Ethereum Chart

**24h:** +0.6%  
**7d:** +1.8%  
**30d:** -14.2%  
**90d:** -22.3%  
**1y:** -37.8%  

---

## Ethereum Market Stats

**Market Cap:** $192.37B
Rank #2

**Circulating Supply:** 120,683,397 ETH
No max supply

**All-Time High:** $4,946.05
-67.8%

**All-Time Low:** $0.43
+367966.3%

---

## Reddit: r/ethereum

**[Daily General Discussion June 30, 2026](https://www.reddit.com/r/ethereum/comments/1ujfphl/daily_general_discussion_june_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

22h ago

---

**[What is the Ethereum Glamsterdam Upgrade? Everything You Need to Know](https://www.reddit.com/r/ethereum/comments/1ujo1lo/what_is_the_ethereum_glamsterdam_upgrade/)**

15h ago

---

**[When your home bank card continues getting denied, what is the simplest way to pay for hotels or Uber overseas?](https://www.reddit.com/r/ethereum/comments/1ujobxe/when_your_home_bank_card_continues_getting_denied/)**

I frequently experience this when traveling. The transaction is rejected, the card is flagged, and the bank must be contacted from a different time zone. truly draining. began storing cryptocurrency as a backup just for this purpose. discovered a crypto platform, which offers travel and mobility gift cards that can be purchased using cryptocurrency and sent instantaneously to Hotels.com, Uber, and airline platforms. Thus, in the event that my card is blocked, I can obtain a Bitcoin or Ethereum gift card and complete the reservation without having to deal with the bank. Does anyone else use this as a backup plan when traveling? I want to know if this is a frequent workaround or if there are better choices.

15h ago

---

**[Daily General Discussion June 29, 2026](https://www.reddit.com/r/ethereum/comments/1uiixw7/daily_general_discussion_june_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Daily General Discussion June 28, 2026](https://www.reddit.com/r/ethereum/comments/1uho4u1/daily_general_discussion_june_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Dappnode Home i764 For Sale (Unopened)](https://www.reddit.com/r/ethereum/comments/1uhljd0/dappnode_home_i764_for_sale_unopened/)**

Hi all, I have an unopened Dappnode Home that I purchased in August of 2023 that I ended up not setting up because of internet and power reliability issues in my housing unit. I'm looking to rehome it for a reasonable price, basically just parts without Dappnode premium so it gets put to use. The specs are: CPU: Intel NUC i7 RAM: 64 GB DDR4 Storage: 4 TB NVMe SSD I also posted in Ethstaker and Dappnode Discords. Happy to send pictures, order confirmation, and whatever else you'd like to see. I'm @pompeyplottin on Discord and Twitter as well, thanks.

3d ago

---

**[I built a ZK + BLS-based customs clearance prototype on L2 — looking for feedback on the on-chain verification architecture.](https://www.reddit.com/r/ethereum/comments/1uh8lq7/i_built_a_zk_blsbased_customs_clearance_prototype/)**

The problem: Single-authority customs approval is a rational bribery target. One official, one decision, predictable cost. The incentive structure is broken by design. Game theory layer: UBLP changes the incentive structure before any cryptography kicks in: - 2/3 committee threshold required (Byzantine fault tolerant) - Committee members have conflicting interests by design - Any anomalous signing pattern is visible on-chain Corrupting the system is no longer a cost-benefit calculation — it becomes a coordination problem that defeats itself. On-chain verification: L2 smart contract verifies two independent proofs at settlement: BLS12-381 aggregate signature — 2/3 committee threshold SP1 Groth16 ZK proof — document validity + holder privacy Neither alone is sufficient for settlement. The contract independently verifies both before writing the immutable record. L2 → Ethereum mainnet anchoring: Settlement records are written to L2. L2 periodically commits a batch proof to Ethereum mainnet — inheriting Ethereum's security guarantees without paying mainnet gas per document. Each customs clearance is ultimately anchored to Ethereum's consensus. Tampering with a settled record requires breaking both the L2 and Ethereum mainnet — economically infeasible. This is the finality layer: L2 handles throughput, Ethereum handles trust. ZK circuit (SP1 zkVM): Private inputs (never leave the circuit): - ministry_signature — P-256 ECDSA, 64 byte - holder_signature — P-256 ECDSA, 64 byte - holder_pub_key_raw — uncompressed SEC1, 65 byte - document_hash — SHA256("ublp-doc-v1:" + canonicalJson), 32 byte - ministry_pub_key_raw — uncompressed SEC1, 65 byte - document_id_hash — 32 byte Public outputs (verified on L2): - document_hash — document fingerprint - ministry_pub_key_hash — ministry key commitment - document_id_hash — replay protection - holder_pub_key_hash — holder identity proof without identity exposure Architecture: - Ministry signs document (EC P-256 ECDSA) → issues Verifiable Credential - Agent generates ZK proof via SP1 zkVM (Groth16/PLONK) - Independent committee verifies ZK proof, then BLS12-381 threshold signs (2/3) - L2 smart contract verifies both → immutable settlement Open questions I'd love feedback on: Is verifying both BLS + ZK on L2 the right approach, or should BLS verification move inside the ZK circuit? BLS 2/3 threshold — right model for this trust setup? Agent-first flow: committee never sees raw document, only the ZK proof — any attack vectors I'm missing? Domain-separated document hash `SHA256("ublp-doc-v1:" + canonicalJson)` — idiomatic for this use case? Security model — if you spot any attack vectors, trust assumption violations, or cryptographic weaknesses I haven't considered, please flag them. This is a prototype and I'd rather find the holes here than later. This is a prototype — mock ZK in dev mode, real SP1 in prod mode. GitHub: github.com/ekacin/UBLP

3d ago

---

**[Daily General Discussion June 27, 2026](https://www.reddit.com/r/ethereum/comments/1ugtj0j/daily_general_discussion_june_27_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

---

**[Daily General Discussion June 26, 2026](https://www.reddit.com/r/ethereum/comments/1ufx7b9/daily_general_discussion_june_26_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

4d ago

---

**[Ethereal news weekly #29 | Strawmap updated, Ethereum Foundation restructure, Ethlabs launched](https://www.reddit.com/r/ethereum/comments/1ug4xsj/ethereal_news_weekly_29_strawmap_updated_ethereum/)**

Strawmap updated, Ethereum Foundation restructure, Ethlabs launched

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-29/) • 4d ago

---

---

## Google News: "ethereum"

**[Sharplink Buys Ethereum for First Time in 2026—With ETH Down 68% From Peak](https://decrypt.co/372432/harplink-buys-ethereum-first-time-2026-eth-down)**

Ethereum treasury firm Sharplink purchased around $16 million worth of ETH last week, marking its first crypto buy since last year.

Decrypt • 12h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Slide as 'Extreme Fear' Persists: Analyst Notes Half of BTC Circulating Network Now Sitting 'Underwater'](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-dogecoin-slide-014634065.html)**

Leading cryptocurrencies reversed course on Tuesday amid negative sentiment in the market, but analysts believe the sell-off may have carved out a bottom. Cryptocurrency24-Hour Gains +/-Price (Recorded at 9:10 p.m. EDT)Bitcoin (CRYPTO: BTC)-2.52%$58,223.10Ethereum (CRYPTO: ETH) -1.54%$1,566.30XRP (CRYPTO: XRP) -1.43%$1.03Solana (CRYPTO: SOL) -1.34%$73.20Dogecoin (CRYPTO: DOGE) -1.38%$0.07144 Crypto Market Retreats Bitcoin pulled back to about $58,000 after Monday’s surge, while 24‑hour trading v

Yahoo Finance • 2h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC recovers from fresh yearly low, ETH and XRP consolidate at key levels](https://www.mitrade.com/au/insights/news/live-news/article-3-1859972-20260701)**

Bitcoin (BTC), Ethereum (ETH) and Ripple (XRP) are showing early signs of stabilization on Wednesday after a recent correction.

Mitrade • 12m ago

---

**[What to Expect From Ethereum (ETH) in July 2026](https://www.mitrade.com/au/insights/crypto/ethereum/beincrypto-ETHUSD-202607010957)**

Ethereum (ETH) enters July 2026 trading near $1,570, close to multi-month lows, after recording its first run of three consecutive red quarterly candles in its history.On-chain data and price charts n

Mitrade • 1h ago

---

**[Vitalik Buterin says crypto’s most powerful idea is still nowhere near ready](https://www.coindesk.com/tech/2026/06/29/vitalik-buterin-says-crypto-s-most-powerful-idea-is-still-nowhere-near-ready)**

The Ethereum co-founder says indistinguishability obfuscation could one day act like a “trustless trusted third party,” but today’s versions remain far too slow for real use.

CoinDesk • 1d ago

---

**[Whales Rotate Back To Bitcoin And Ethereum As Altcoin Risk Cools](https://www.tradingview.com/news/newsbtc:19795a310094b:0-whales-rotate-back-to-bitcoin-and-ethereum-as-altcoin-risk-cools/)**

TL;DRWhat HappenedWhales Rotate Back To Bitcoin And Ethereum As Altcoin Risk Cools. The update comes from Tokenpost, with the core claim checked against Glassnode exchange flows / IntoTheBlock address statistics. That matters because this is the sort of story that can quickly become noisy if it is…

TradingView • 10h ago

---

**[Bitmine Acquires $43 Million Of Ethereum As Price Slides](https://finance.yahoo.com/markets/crypto/articles/bitmine-acquires-43-million-ethereum-134200182.html)**

Bitmine Immersion Technologies (NYSE: $BMNR) bought another 27,084 of Ethereum (CRYPTO: $ETH) over the past week as...

Yahoo Finance • 1d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.70 Million Tokens, and Total Crypto and Total Cash Holdings of $9.8 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-70-million-tokens-and-total-crypto-and-total-cash-holdings-of-9-8-billion-302812787.html)**

Bitmine owns 4.7% of the total ETH coin supply of 120.7 million Bitmine is 94% of the way to the 'Alchemy of 5%' in just 11 months Bitmine was added to the...

PR Newswire • 1d ago

---

**[Bitmine lifts Ethereum treasury to 5.7 million ETH through 'challenging' weekly slide, joins Russell 1000](https://www.theblock.co/post/406538/bitmine-lifts-ethereum-treasury-to-5-7-million-eth-through-challenging-weekly-slide-joins-russell-1000)**

Bitmine added 27,084 ETH last week, bringing total holdings to 5.70M coins worth $8.9B as the company hits 94% of its 5% ETH supply target.

The Block • 1d ago

---

**[Ethereum zkRollup project Loopring sunsets DEX, citing lack of meaningful adoption](https://www.theblock.co/post/406492/loopring-sunsets-dex)**

Loopring plans to return all remaining user funds through a smart contract upgrade, without requiring users to cover transaction costs.

The Block • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Fox Business Expert Reveals MASSIVE Crypto News (bitcoin, ethereum)](https://www.youtube.com/watch?v=ykiG4u9Y3vA)**

Buy, Sell, Trade Crypto: Trade Stocks (unlock $100k): https://www.weex.com/events/promo/en-campaignlist-1?vipCode=oz5p ...

📺 Altcoin Daily

👁️ 18K • 👍 1K • 💬 75 • ⏱️ 11:44 • 5h ago

---

**[BIGGEST CRYPTO NEWS HAPPENING NOW (JPMorgan, Clarity, Saylor, Ethereum)](https://www.youtube.com/watch?v=qS34CLtPpOo)**

JPMorgan Backs Crypto Clarity Act!! Bitcoin Saylor News + Bull Case For Ethereum ⭐ Follow Altcoin Daily on X: ...

📺 Altcoin Daily

👁️ 46K • 👍 2K • 💬 138 • ⏱️ 11:49 • 1d ago

---

**[The Secret War That Could Make Ethereum Explode w/ John Gillen](https://www.youtube.com/watch?v=b0hzBtXhk3Q)**

We called Micron (217%), Bloom (130%), Hyperliquid (55%), and Galaxy (37%) before their big runs. Want to see what we're ...

📺 Milk Road

👁️ 5K • 👍 156 • 💬 66 • ⏱️ 41:52 • 1d ago

---

**[🚨 TOM LEE INTERVIEW: HUGE ETH &amp; BMNR NEWS](https://www.youtube.com/watch?v=txV6L1Dd8j4)**

BMNR, ETH & MSTR: Tom Lee Just Dropped a Bomb | Huge Ethereum News & Crypto Market Update MaxFi: ...

📺 Big Time Trades

👁️ 3K • 👍 135 • 💬 42 • ⏱️ 29:00 • 9h ago

---

**[Why Bit Digital Sold Its Bitcoin to Bet on Ethereum &amp; AI](https://www.youtube.com/watch?v=heyjP_yj3DI)**

The first generation of crypto treasury companies was all about accumulating digital assets. But according to Bit Digital CEO Sam ...

📺 Coinage

👁️ 762 • 👍 20 • 💬 21 • ⏱️ 17:46 • 11h ago

---

**[Joseph Chalom: Ethereum Is Extremely Oversold Here (New Catalysts)](https://www.youtube.com/watch?v=rLd9qCWOAO8)**

Joseph Chalom makes the case that this is one of the best ETH entry points we've seen, why step-function demand from ...

📺 The Rollup

👁️ 5K • 👍 112 • 💬 21 • ⏱️ 5:59 • 1d ago

---

**[BITCOIN JUST REJECTED: New Signal Flashing Now!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=Ux_u_EKbT78)**

BITCOIN JUST REJECTED: New Signal Flashing Now!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 3K • 👍 203 • 💬 319 • ⏱️ 20:44 • 5h ago

---

**[40-Year Trading Veteran Reveals MASSIVE Crypto Prediction](https://www.youtube.com/watch?v=3O3ySBPSJHE)**

Buy, Sell, Trade Crypto: Claim $100 on WEEX (w/ first trade): https://www.weex.com/events/welcome-event?vipCode=oz5p ...

📺 Altcoin Daily

👁️ 59K • 👍 2K • 💬 127 • ⏱️ 9:55 • 2d ago

---

**[ETH: Diese Indikatoren machen mir jetzt große Sorgen!](https://www.youtube.com/watch?v=-UwQWxngHkU)**

In dieser Elliott-Wellen-Analyse besprechen wir die aktuelle Situation bei Ethereum sowie die wichtigsten Unterstützungen, ...

📺 HKCM

👁️ 23K • 👍 2K • 💬 90 • ⏱️ 17:42 • 11h ago

---

**[The New Plan to Make Ethereum Win](https://www.youtube.com/watch?v=9rYyZaO0-EI)**

SPOTIFY PREMIUM RSS FEED | USE CODE: SPOTIFY24 https://bankless.cc/spotify-premium --- Ethereum has a new R&D lab, ...

📺 Bankless

👁️ 9K • 👍 287 • 💬 52 • ⏱️ 1:01:02 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
