---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-13T15:24:22.491336+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- videos
- news
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 13, 2026 at 15:24 UTC  
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

### $2,272.96

---

## Ethereum Chart

**24h:** -0.3%  
**7d:** -1.5%  
**30d:** -2.8%  
**90d:** +10.2%  
**1y:** -13.6%  

---

## Ethereum Market Stats

**Market Cap:** $272.20B
Rank #2

**Circulating Supply:** 120,686,235 ETH
No max supply

**All-Time High:** $4,946.05
-54.4%

**All-Time Low:** $0.43
+520897.6%

---

## Reddit: r/ethereum

**[I cracked Vitalik’s 2015 on-chain ad platform. He was the only bidder. Total cost: $2.](https://www.reddit.com/r/ethereum/comments/1tbzzvi/i_cracked_vitaliks_2015_onchain_ad_platform_he/)**

Three months after mainnet launched, Vitalik deployed an advertising auction system to Ethereum. Eight ad slots, four auction mechanisms (one-phase winner-pays, cumulative, sealed-bid first-price, sealed-bid second-price), all managed by a factory contract called adStorer from ethereum/dapp-bin. I matched the deployed bytecode to source through compiler archaeology. Exact match, 8,752 bytes, solc v0.1.1. Then I decoded every transaction across all 8 child auction contracts. The only bidder was Vitalik himself. Two wallets (his old deployer and what’s now vitalik.eth), 229 transactions, 0.064 ETH in bids. The winning “advertisements” were two image URLs: me.jpg (a photo of himself) and heiko.jpg (a photo of Heiko Hees, who was building pyethereum). Both are 404 today. Some details: Slot 5 is a second-price sealed-bid auction. vitalik.eth bid 0.0005 ETH, his old wallet bid 0.0003 ETH. Second-price rules made vitalik.eth pay the runner-up’s price. The first Vickrey auction on Ethereum selected a photo of a pyethereum developer over its own creator. Gas cost more than the bids. Vitalik burned ~1 ETH on gas (at 60 gwei, hard-coded in his deploy script) to move 0.064 ETH through the auction mechanics. At October 2015 prices, the whole experiment cost about $2. Slot 1 was a stress test. 159 transactions, with Vitalik rebidding the same 0.0001 ETH increment 19 times in a row to validate cumulative bidding. Three of the four all-pay auction variants got zero bids. He abandoned the one he tried before revealing. Even Vitalik didn’t trust his own all-pay math. The sealed-bid auctions had a frontend bug where bid hashes were passed as ASCII hex instead of raw bytes, making commitments readable in calldata. Didn’t matter since the only participant wrote the code. 0.029 ETH (~$70 today, $0.03 in 2015) is still locked in the child contracts from unrevealed sealed bids. This was deployed three weeks before DevCon 1, on a network with maybe a few hundred users. A mechanism design experiment that nobody participated in except its creator, preserved on-chain for ten years. I checked the Wayback Machine for the ad images. The closest capture of vitalik.ca/files/ is from June 2016. Neither photo was archived. Full documentation with verified source, decoded bids, and all 8 slots mapped: https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e This is part of the EthereumHistory project where we’re documenting and verifying the earliest Ethereum contracts. If you want to help, the project is open.

🔗 [Ethereum History](https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e) • 1h ago

---

**[Daily General Discussion May 13, 2026](https://www.reddit.com/r/ethereum/comments/1tbpq6u/daily_general_discussion_may_13_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

10h ago

---

**[Grayscale weighs in on Ethereum issuance](https://www.reddit.com/r/ethereum/comments/1tbndv4/grayscale_weighs_in_on_ethereum_issuance/)**

🔗 [grayscale.com](https://www.grayscale.com/the-stack/ethereums-staking-model-needs-an-update) • 12h ago

---

**[Ethereum impact from Chainlink deal launching Collateral AppChain platform](https://www.reddit.com/r/ethereum/comments/1tbioxg/ethereum_impact_from_chainlink_deal_launching/)**

The DTCC and Chainlink partnership directly benefits Ethereum by establishing its enterprise-grade client, Besu, as the foundational infrastructure for a major global post-trade system. The Collateral AppChain is built on Hyperledger Besu, an Ethereum-compatible network, which validates Ethereum’s technical standards for institutional use and drives demand for enterprise blockchain solutions. This integration significantly boosts the utility and credibility of Chainlink’s oracle services within traditional finance. By utilizing Chainlink’s Runtime Environment (CRE) and data standards to automate pricing, margining, and settlement, the deal demonstrates that decentralized oracles can securely manage critical financial workflows. This positions Chainlink as a default infrastructure layer for tokenized real-world assets (RWA), potentially increasing its usage across other financial institutions following DTCC’s October 2026 launch. For the broader financial ecosystem, the partnership accelerates the tokenization of assets on blockchain rails. It enables 24/7 near real-time collateral management, moving away from legacy T+1 or T+2 settlement times to instant, smart-contract-verified transactions. This efficiency improves capital utilization for institutions and sets a precedent for other clearinghouses to adopt similar Ethereum-based and Chainlink-powered infrastructures.

15h ago

---

**[Clear Signing | See What You Sign](https://www.reddit.com/r/ethereum/comments/1tb6ku5/clear_signing_see_what_you_sign/)**

The open standard for human-readable transaction signing.

🔗 [Clear Signing](https://clearsigning.org/) • 23h ago

---

**[Daily General Discussion May 12, 2026](https://www.reddit.com/r/ethereum/comments/1tariy9/daily_general_discussion_may_12_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[$14 Trillion BlackRock Picks Ethereum for Tokenized Funds](https://www.reddit.com/r/ethereum/comments/1tahzx0/14_trillion_blackrock_picks_ethereum_for/)**

BlackRock filed for tokenized money-market fund shares on Ethereum, adding pressure to the chain race for real-world asset settlement.

🔗 [Daily Crypto Briefs](https://dailycryptobriefs.com/news/blackrock-picks-ethereum-tokenized-funds/) • 1d ago

---

**[Protocol Cluster Updates: May 2026](https://www.reddit.com/r/ethereum/comments/1taex6u/protocol_cluster_updates_may_2026/)**

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/05/11/protocol-update-may-26) • 1d ago

---

**[Daily General Discussion May 11, 2026](https://www.reddit.com/r/ethereum/comments/1t9tdqb/daily_general_discussion_may_11_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion May 10, 2026](https://www.reddit.com/r/ethereum/comments/1t8xf85/daily_general_discussion_may_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

---

---

## Google News: "ethereum"

**[JPMorgan launching second tokenized money market fund on Ethereum](https://www.theblock.co/post/401028/jpmorgan-launching-tokenized-money-market-fund-ethereum)**

The new fund will invest in U.S. Treasurys and overnight repurchase agreements collateralized by Treasurys or cash.

The Block • 19h ago

---

**[Protocol Cluster Updates: May 2026](https://blog.ethereum.org/2026/05/11/protocol-update-may-26)**

ethereum.org • 1d ago

---

**[XRP Overtakes Bitcoin, Ethereum In Korea: What Is Going On?](https://finance.yahoo.com/news/xrp-overtakes-bitcoin-ethereum-korea-143004710.html)**

XRP (CRYPTO: XRP) topped Bitcoin (CRYPTO: BTC) and Ethereum (CRYPTO: ETH) in South Korean trading volumes over the past day, posting $110.9 million on Upbit and $41 million on Bithumb. Korean Volume Signal Returns XRP/KRW was the most traded pair on Upbit over the past 24 hours, ahead of Bitcoin’s $88.6 million and Ethereum’s $67 million, according to CoinGecko data. On Bithumb, XRP/KRW recorded $41 million in volume, ranking second behind USDT/KRW and above both BTC/KRW and ETH/KRW. Korea has l

Yahoo Finance • 54m ago

---

**[Animoca-backed NUVA connects Figure's $19 billion of tokenized assets to Ethereum](https://www.coindesk.com/business/2026/05/13/animoca-backed-nuva-connects-figure-s-usd19-billion-of-tokenized-assets-to-ethereum)**

The protocol, led by veteran BNY executive Anthony Moro, aims to connect real-world assets with DeFi markets, starting with home equity lines of credit and Treasuries.

CoinDesk • 22m ago

---

**[After Falling 33% in 6 Months, Is Ethereum Still a Buy With $1,000?](https://www.fool.com/investing/2026/05/13/after-falling-33-in-6-months-is-ethereum-still-a-b/)**

This price action isn't the thing to be focusing on.

The Motley Fool • 2h ago

---

**[How Will the CLARITY Act May 14 Vote Impact Bitcoin, ETH and XRP?](https://www.disruptionbanking.com/2026/05/12/how-will-the-clarity-act-may-14-vote-impact-bitcoin-eth-and-xrp/)**

Disruption Banking • 1d ago

---

**[Current price of Ethereum for May 31, 2026](https://fortune.com/article/price-of-ethereum-05-13-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 2h ago

---

**[Circle CEO Reveals CLARITY Act’s Impact on Bitcoin, Ethereum and XRP](https://coinpedia.org/news/circle-ceo-reveals-clarity-acts-impact-on-bitcoin-ethereum-and-xrp/)**

Coinpedia • 1d ago

---

**[BitMine Slows Ethereum Purchases](https://finance.yahoo.com/markets/crypto/articles/bitmine-slows-ethereum-purchases-171700536.html)**

BitMine Immersion Technologies (NYSE: $BMNR) has slowed its Ethereum (CRYPTO: $ETH) purchases over the past week.&n...

Yahoo Finance • 1d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.21 Million Tokens, and Total Crypto and Total Cash Holdings of $13.4 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-21-million-tokens-and-total-crypto-and-total-cash-holdings-of-13-4-billion-302767816.html)**

Bitmine owns more than 4.31% of the total ETH coin supply of 120.7 million Bitmine is 86% of the way to the 'Alchemy of 5%' in just 11 months Crypto Spring has...

PR Newswire • 2d ago

---

---

## YouTube Videos: "ethereum"

**[☠ Ethereum Story Is Breaking - ETH Crypto Analysis](https://www.youtube.com/watch?v=x2HEF-EuTkw)**

Join Premium: https://the-bitcoin-strategy.com Instagram: https://www.instagram.com/gerhard_bitcoin_strategy/ My Chart ...

📺 Gerhard - Bitcoin Strategy

👁️ 559 • 👍 40 • 💬 35 • ⏱️ 10:03 • 2h ago

---

**[MASSIVE Clarity Act Update! This Is a HUGE Win for Bitcoin &amp; Crypto - Tom Lee](https://www.youtube.com/watch?v=0tN78rPvgms)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 7K • 👍 229 • 💬 110 • ⏱️ 17:25 • 20h ago

---

**[ELIZABETH WARREN FIGHTS CLARITY ACT! JPMORGAN TOKENIZATION ETHEREUM &amp; BERMUDA STELLAR XLM!](https://www.youtube.com/watch?v=s-I_zD6SBTA)**

Crypto News: Elizabeth Warren pushes back on Clarity Act draft bill. JPMorgan launching second tokenized money market fund ...

📺 Thinking Crypto

👁️ 8K • 👍 626 • 💬 380 • ⏱️ 20:45 • 10h ago

---

**[ETH Deep Dive (bullish and bearish projections)](https://www.youtube.com/watch?v=S1e5MeaFoSg)**

Ethereum has been lagging badly behind Bitcoin, and in this video Aaron breaks down why ETH still looks weaker even after its ...

📺 Coin Bureau Trading

👁️ 5K • 👍 303 • 💬 30 • ⏱️ 23:49 • 1d ago

---

**[Dumping BTC for AI?! 🤯 Agentic ETH, Massive Flows  &amp; Levge +  AI Masterplan! 🚀](https://www.youtube.com/watch?v=ZI4eRwNmSqA)**

JOIN THE FAMILY: http://www.patreon.com/investanswers IA MODELS: https://investanswers.io/indicators 🏖️ IA ...

📺 InvestAnswers

👁️ 30K • 💬 89 • ⏱️ 19:51 • 17h ago

---

**[Why Ethereum is Stuck Under $2.4K](https://www.youtube.com/watch?v=8TUiX3l06XM)**

Ethereum keeps failing at the $2400 resistance level, and the data shows why: weak ETF inflows, falling leverage, and rising ETH ...

📺 Coin Bureau Podcast

👁️ 2K • 👍 38 • 💬 2 • ⏱️ 1:11 • 23h ago

---

**[Why Crypto May Be Entering a New Bull Market](https://www.youtube.com/watch?v=HZ6b_i9Ce3U)**

Tom Lee breaks down why Ethereum, Bitcoin, tokenization, and AI could drive the next major crypto bull market. From Ethereum's ...

📺 Cointelegraph

👁️ 5K • 👍 146 • 💬 12 • ⏱️ 9:08 • 1d ago

---

**[BITCOIN: This Move Was a BRUTAL Trap! (here’s why) - BTC, ETH Price Prediction Today](https://www.youtube.com/watch?v=Z6xK8hoMBTM)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 5K • 👍 419 • 💬 78 • ⏱️ 15:09 • 4h ago

---

**[Vitalik Just Called Out Ethereum’s Biggest L2s](https://www.youtube.com/watch?v=yNul3atS1Wk)**

Vitalik Buterin just challenged the entire Layer 2 narrative. If Ethereum mainnet keeps getting cheaper, are rollups really scaling ...

📺 CoinGecko

👁️ 3K • 👍 188 • 💬 48 • ⏱️ 8:44 • 2d ago

---

**[Tom Lee: How ETH Could Hit $22,000](https://www.youtube.com/watch?v=tBCnSQ2TzJw)**

Tom Lee explains why he believes Ethereum could still be massively undervalued, arguing that if Bitcoin reaches $250K, ETH ...

📺 Cointelegraph

👁️ 2K • 👍 21 • 💬 124 • ⏱️ 0:43 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
