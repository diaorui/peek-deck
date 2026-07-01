---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-07-01T08:19:03.406415+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- social
- news
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** July 01, 2026 at 08:19 UTC  
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

### $1,576.02

---

## Ethereum Chart

**24h:** -0.6%  
**7d:** +0.4%  
**30d:** -15.4%  
**90d:** -23.3%  
**1y:** -38.7%  

---

## Ethereum Market Stats

**Market Cap:** $189.86B
Rank #2

**Circulating Supply:** 120,683,397 ETH
No max supply

**All-Time High:** $4,946.05
-68.2%

**All-Time Low:** $0.43
+363130.1%

---

## Reddit: r/ethereum

**[Daily General Discussion June 30, 2026](https://www.reddit.com/r/ethereum/comments/1ujfphl/daily_general_discussion_june_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[What is the Ethereum Glamsterdam Upgrade? Everything You Need to Know](https://www.reddit.com/r/ethereum/comments/1ujo1lo/what_is_the_ethereum_glamsterdam_upgrade/)**

19h ago

---

**[When your home bank card continues getting denied, what is the simplest way to pay for hotels or Uber overseas?](https://www.reddit.com/r/ethereum/comments/1ujobxe/when_your_home_bank_card_continues_getting_denied/)**

I frequently experience this when traveling. The transaction is rejected, the card is flagged, and the bank must be contacted from a different time zone. truly draining. began storing cryptocurrency as a backup just for this purpose. discovered a crypto platform, which offers travel and mobility gift cards that can be purchased using cryptocurrency and sent instantaneously to Hotels.com, Uber, and airline platforms. Thus, in the event that my card is blocked, I can obtain a Bitcoin or Ethereum gift card and complete the reservation without having to deal with the bank. Does anyone else use this as a backup plan when traveling? I want to know if this is a frequent workaround or if there are better choices.

19h ago

---

**[Daily General Discussion June 29, 2026](https://www.reddit.com/r/ethereum/comments/1uiixw7/daily_general_discussion_june_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion June 28, 2026](https://www.reddit.com/r/ethereum/comments/1uho4u1/daily_general_discussion_june_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

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

4d ago

---

**[Daily General Discussion June 26, 2026](https://www.reddit.com/r/ethereum/comments/1ufx7b9/daily_general_discussion_june_26_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

5d ago

---

**[Ethereal news weekly #29 | Strawmap updated, Ethereum Foundation restructure, Ethlabs launched](https://www.reddit.com/r/ethereum/comments/1ug4xsj/ethereal_news_weekly_29_strawmap_updated_ethereum/)**

Strawmap updated, Ethereum Foundation restructure, Ethlabs launched

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-29/) • 4d ago

---

---

## Google News: "ethereum"

**[Sharplink Buys Ethereum for First Time in 2026—With ETH Down 68% From Peak](https://decrypt.co/372432/harplink-buys-ethereum-first-time-2026-eth-down)**

Ethereum treasury firm Sharplink purchased around $16 million worth of ETH last week, marking its first crypto buy since last year.

Decrypt • 16h ago

---

**[Is Bitmine Immersion Technologies’ (BMNR) Russell Debut Reshaping Its Ethereum-Heavy Investment Narrative?](https://finance.yahoo.com/markets/stocks/articles/bitmine-immersion-technologies-bmnr-russell-071743433.html)**

In late June 2026, Bitmine Immersion Technologies, Inc. was added to multiple Russell equity indexes, including the Russell 1000, 2500, 3000 and related value and completeness benchmarks, while also declaring a cash dividend on its 9.50% Series A Perpetual Preferred Stock listed as BMNP. These moves highlight Bitmine’s emergence as a large-cap index constituent with one of the largest Ethereum treasuries and staking operations in the market, underscoring its growing presence at the...

Yahoo Finance • 1h ago

---

**[Bitmine Acquires $43 Million Of Ethereum As Price Slides](https://finance.yahoo.com/markets/crypto/articles/bitmine-acquires-43-million-ethereum-134200182.html)**

Bitmine Immersion Technologies (NYSE: $BMNR) bought another 27,084 of Ethereum (CRYPTO: $ETH) over the past week as...

Yahoo Finance • 1d ago

---

**[Tom Lee blames bitcoin, ether weakness on quarter-end rebalancing as Bitmine (BMNR) buys $43M ETH](https://www.coindesk.com/business/2026/06/29/tom-lee-blames-crypto-weakness-on-quarter-end-window-dressing-as-bitmine-adds-another-usd43-million-of-eth)**

Bitmine made its smallest purchase since early May as Lee pointed to investors cutting losses before the start of the second half of the year.

CoinDesk • 1d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.70 Million Tokens, and Total Crypto and Total Cash Holdings of $9.8 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-70-million-tokens-and-total-crypto-and-total-cash-holdings-of-9-8-billion-302812787.html)**

Bitmine owns 4.7% of the total ETH coin supply of 120.7 million Bitmine is 94% of the way to the 'Alchemy of 5%' in just 11 months Bitmine was added to the...

PR Newswire • 1d ago

---

**[Ethereum zkRollup project Loopring sunsets DEX, citing lack of meaningful adoption](https://www.theblock.co/post/406492/loopring-sunsets-dex)**

Loopring plans to return all remaining user funds through a smart contract upgrade, without requiring users to cover transaction costs.

The Block • 2d ago

---

**[Whales Rotate Back To Bitcoin And Ethereum As Altcoin Risk Cools](https://www.tradingview.com/news/newsbtc:19795a310094b:0-whales-rotate-back-to-bitcoin-and-ethereum-as-altcoin-risk-cools/)**

TL;DRWhat HappenedWhales Rotate Back To Bitcoin And Ethereum As Altcoin Risk Cools. The update comes from Tokenpost, with the core claim checked against Glassnode exchange flows / IntoTheBlock address statistics. That matters because this is the sort of story that can quickly become noisy if it is…

TradingView • 15h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC recovers from fresh yearly low, ETH and XRP consolidate at key levels](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-recovers-from-fresh-yearly-low-eth-and-xrp-consolidate-at-key-levels-202607010326)**

Bitcoin (BTC), Ethereum (ETH) and Ripple (XRP) are showing early signs of stabilization on Wednesday after a recent correction.

FXStreet • 4h ago

---

**[Is Ethereum's Golden Goose Finally Cooked?](https://www.fool.com/investing/2026/06/29/is-ethereums-golden-goose-finally-cooked/)**

Sentiment about the coin is in the dumps, and it's no surprise why.

The Motley Fool • 1d ago

---

**[Current price of Ethereum for June 30, 2026](https://fortune.com/article/price-of-ethereum-06-30-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 18h ago

---

---

## YouTube Videos: "ethereum"

**[Fox Business Expert Reveals MASSIVE Crypto News (bitcoin, ethereum)](https://www.youtube.com/watch?v=ykiG4u9Y3vA)**

Buy, Sell, Trade Crypto: Trade Stocks (unlock $100k): https://www.weex.com/events/promo/en-campaignlist-1?vipCode=oz5p ...

📺 Altcoin Daily

👁️ 31K • 👍 1K • 💬 90 • ⏱️ 11:44 • 9h ago

---

**[BIGGEST CRYPTO NEWS HAPPENING NOW (JPMorgan, Clarity, Saylor, Ethereum)](https://www.youtube.com/watch?v=qS34CLtPpOo)**

JPMorgan Backs Crypto Clarity Act!! Bitcoin Saylor News + Bull Case For Ethereum ⭐ Follow Altcoin Daily on X: ...

📺 Altcoin Daily

👁️ 46K • 👍 2K • 💬 138 • ⏱️ 11:49 • 1d ago

---

**[The Secret War That Could Make Ethereum Explode w/ John Gillen](https://www.youtube.com/watch?v=b0hzBtXhk3Q)**

We called Micron (217%), Bloom (130%), Hyperliquid (55%), and Galaxy (37%) before their big runs. Want to see what we're ...

📺 Milk Road

👁️ 6K • 👍 165 • 💬 67 • ⏱️ 41:52 • 1d ago

---

**[Joseph Chalom: Ethereum Is Extremely Oversold Here (New Catalysts)](https://www.youtube.com/watch?v=rLd9qCWOAO8)**

Joseph Chalom makes the case that this is one of the best ETH entry points we've seen, why step-function demand from ...

📺 The Rollup

👁️ 6K • 👍 116 • 💬 22 • ⏱️ 5:59 • 1d ago

---

**[🚨 TOM LEE INTERVIEW: HUGE ETH &amp; BMNR NEWS](https://www.youtube.com/watch?v=txV6L1Dd8j4)**

BMNR, ETH & MSTR: Tom Lee Just Dropped a Bomb | Huge Ethereum News & Crypto Market Update MaxFi: ...

📺 Big Time Trades

👁️ 3K • 👍 144 • 💬 41 • ⏱️ 29:00 • 13h ago

---

**[Why Bit Digital Sold Its Bitcoin to Bet on Ethereum &amp; AI](https://www.youtube.com/watch?v=heyjP_yj3DI)**

The first generation of crypto treasury companies was all about accumulating digital assets. But according to Bit Digital CEO Sam ...

📺 Coinage

👁️ 1K • 👍 27 • 💬 12 • ⏱️ 17:46 • 16h ago

---

**[The New Plan to Make Ethereum Win](https://www.youtube.com/watch?v=9rYyZaO0-EI)**

SPOTIFY PREMIUM RSS FEED | USE CODE: SPOTIFY24 https://bankless.cc/spotify-premium --- Ethereum has a new R&D lab, ...

📺 Bankless

👁️ 10K • 👍 295 • 💬 58 • ⏱️ 1:01:02 • 1d ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=0D8Fyz3CZXg)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 522 • 👍 59 • ⏱️ 6:30 • 4h ago

---

**[🚨 BTC &amp; ETH: AHHH… JESUS CHRIST HELP US NOW!!!!!](https://www.youtube.com/watch?v=D1DmwkPwiyc)**

Bitcoin, ethereum and general markets are showing us clear patterns now! Here is what I am doing!!!! ---------- Join My FREE ...

📺 Thomas Kralow

👁️ 15K • 👍 1K • 💬 32 • ⏱️ 9:18 • 1d ago

---

**[BITCOIN JUST REJECTED: New Signal Flashing Now!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=Ux_u_EKbT78)**

BITCOIN JUST REJECTED: New Signal Flashing Now!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 5K • 👍 258 • 💬 267 • ⏱️ 20:44 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
