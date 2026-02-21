---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-21T11:45:41.160789+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- social
- videos
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 21, 2026 at 11:45 UTC  
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

### $1,966.74

---

## Ethereum Chart

**24h:** +1.5%  
**7d:** +0.7%  
**30d:** -33.1%  
**90d:** -33.0%  
**1y:** -28.4%  

---

## Ethereum Market Stats

**Market Cap:** $238.84B
Rank #2

**Circulating Supply:** 120,692,373 ETH
No max supply

**All-Time High:** $4,946.05
-60.0%

**All-Time Low:** $0.43
+456878.3%

---

## Reddit: r/ethereum

**[Daily General Discussion February 21, 2026](https://www.reddit.com/r/ethereum/comments/1rajeg9/daily_general_discussion_february_21_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

5h ago

---

**[We built a fully onchain orderbook for two of Ethereum's oldest tokens (2016 Unicorn experiment)](https://www.reddit.com/r/ethereum/comments/1ra98op/we_built_a_fully_onchain_orderbook_for_two_of/)**

Some backstory In February 2016 — less than a year after Ethereum launched — Alex Van de Sande (avsa) from the Ethereum Foundation deployed an experimental contract called Unicorns (0x89205A3A). It was one of the very first token contracts on Ethereum, predating the ERC-20 standard. A month later, he created Unicorn Meat (0xED6aC8de) — another experimental token — along with the Grinder Association DAO, one of the earliest DAOs on Ethereum. The Grinder let you exchange Unicorns for Unicorn Meat, effectively the first onchain token swap. These were demo contracts for the Mist browser. They were never meant to become "real" tokens, but they've survived for 10 years now — still on mainnet, still functional, still held in wallets. The problem Because these tokens predate ERC-20 (they have 0 decimal places, non-standard transfer functions), they don't work well with modern DEXes. Uniswap V3's fee math rounds to 0 for 0-decimal tokens. AMM pooling is essentially broken for them. Wrapped versions exist (w🦄 and w🍖 are standard ERC-20s), but the 0-decimal problem persists. What we built Unicorn Market — a fully onchain orderbook contract, purpose-built for these tokens: No backend, no matching engine, no admin keys — pure smart contract Escrowed limit orders — maker's tokens held in contract until filled or cancelled Partial fills — take any portion of an order Deterministic rounding — uses OpenZeppelin's Math.mulDiv with ceiling rounding so makers never get shorted All state onchain, all settlement via events Verified contract: 0xA352B50A91C648c97F7aC0a80D686D297b62693E Trade interface: unicornmeateth.com/market Source: github.com/cartoonitunes/unicorn-market Why this matters (beyond the meme) There are hundreds of pre-ERC-20 and non-standard tokens stuck on Ethereum mainnet with no good trading infrastructure. AMMs assume standard decimals and transfer behavior. A simple, auditable orderbook contract is arguably the right primitive for these edge cases. If you hold any legacy Ethereum tokens from 2015-2017, you probably know the pain of trying to trade them on modern infra. Technical details Reentrancy-guarded, CEI pattern throughout Happy to answer questions about the contract design or the history of these tokens.

13h ago

---

**[Daily General Discussion February 20, 2026](https://www.reddit.com/r/ethereum/comments/1r9nfzz/daily_general_discussion_february_20_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[How to x402: A Complete Guide to permissionless Agent payments](https://www.reddit.com/r/ethereum/comments/1r9z82d/how_to_x402_a_complete_guide_to_permissionless/)**

Hey, Just finished integrating x402 (Coinbase's new payment protocol for AI agents) into an API endpoint after a few days working through the official docs and SDK. It’s running end-to-end: send a request, receive a 402, sign a USDC transfer, retry, and get the response back. A lot of the documentation is confusing due to differences between v1 and v2, so I compiled everything into a single post that should make things clearer. It includes an interactive demo where you can generate a wallet, fund it, and make a real x402 payment against a live endpoint. The goal was to create one resource that’s enough to understand x402 and build your own agent payment integration. The guide also includes some background on the origins of 402. Check it out here: https://simplescraper.io/blog/x402-payment-protocol Let me know what you think!

19h ago

---

**[Let your Agent Pay for Blockchain Data](https://www.reddit.com/r/ethereum/comments/1ra43dn/let_your_agent_pay_for_blockchain_data/)**

Lobsters like block too You can use x402 for agents to pay and get access to blockchain data now. There’s no clean way for agents to access onchain data without API keys, accounts, or billing friction. Until now. With x402, agents can pay per request using stablecoins over HTTP, wallet in, data out. https://goldrush.dev/blog/goldrush-x402-blockchain-data-for-agents/

16h ago

---

**[Even the Ethereum Foundation is highlighting the same smart contract risks](https://www.reddit.com/r/ethereum/comments/1r9x3eh/even_the_ethereum_foundation_is_highlighting_the/)**

There’s been a lot of talk lately about how fast teams are shipping contracts especially with AI-assisted “vibe coding.” Recently, the Ethereum Foundation highlighted the release of the OWASP Smart Contract Top 10, which outlines the most critical risks developers and security teams should be protecting against today. What stands out is how familiar many of these failure patterns still are: access control issues, logic flaws, unsafe assumptions, and upgrade risks. The tooling is getting better. The awareness is getting better. But the same classes of bugs keep showing up in production. Feels like the real challenge in 2026 isn’t whether we can write contracts faster it’s whether we can operate them safely at scale. Curious how others here are thinking about this balance between speed and security.

21h ago

---

**[Justin Drake dives deep into Lean Ethereum](https://www.reddit.com/r/ethereum/comments/1r9qidy/justin_drake_dives_deep_into_lean_ethereum/)**

Justin Drake dives deep into Lean Ethereum In this episode (which is the first in a six-part series on Lean Ethereum) we covered: - This vision for ethereum, spanning the consensus, data, and execution layers. - How post-quantum cryptography, faster finality, and enshrined ZK are all being used to future-proof Ethereum’s core. They also lay out some of the topics that will be covered in subsequent parts of the series. Listen here

1d ago

---

**[Vibehouse: Ethereum’s Vibecoded Consensus Client from Lighthouse](https://www.reddit.com/r/ethereum/comments/1r9rytg/vibehouse_ethereums_vibecoded_consensus_client/)**

Vibehouse, an AI generated fork of Lighthouse, implemented ePBS in 72 hours and passed consensus tests on a multi node devnet.

🔗 [EtherWorld.co](https://etherworld.co/vibehouse-ethereums-vibecoded-consensus-client-from-lighthouse/) • 1d ago

---

**[Quantum computing isn’t FUD anymore how ready is Ethereum really?](https://www.reddit.com/r/ethereum/comments/1r9vjvf/quantum_computing_isnt_fud_anymore_how_ready_is/)**

Few years Ago no one believe quantum threat is even a thing. But lately it feels different. Not because quantum computers can suddenly crack wallets tomorrow, but because the timeline is slowly shifting from sci-fi to strategic planning. Here’s the uncomfortable part, most of crypto security today relies on elliptic curve cryptography. If a sufficiently powerful quantum computer runs Shor’s algorithm at scale, it could theoretically derive private keys from public keys. The bigger issue isn’t quantum breaks crypto overnight. It’s the long runway required to migrate billions in value to new cryptographic standards before that day ever comes. That kind of coordination takes years. What I find interesting is that Ethereum developers aren’t brushing this off. There’s active research into post-quantum signature schemes lattice-based and hash-based approaches and discussions about how Ethereum’s account abstraction model could make upgrading signatures more flexible compared to more rigid systems. The idea isn’t to panic-fork tomorrow, but to design the protocol so it can evolve if needed. Vitalik has openly talked about the possibility of a hard fork to move toward quantum-resistant signatures if the threat becomes imminent. There’s also ongoing work around making cryptographic components more modular, so the base layer isn’t permanently locked into one signature scheme forever. That kind of design thinking matters. At the same time, this isn’t trivial. Post-quantum signatures are typically much larger. They consume more bandwidth. They increase verification costs. Gas implications are real. And then there’s the elephant in the room: dormant wallets. If a public key is already exposed on-chain, and quantum becomes viable before migration, those funds could be at risk. There’s also the harvest now, decrypt later scenario. Even if quantum isn’t powerful enough today, adversaries could store cryptographic data now and wait for future breakthroughs. That’s not conspiracy talk that’s standard long-term threat modeling. So the question isn’t whether quantum computing will eventually be powerful. It’s whether Ethereum and crypto as a whole can coordinate upgrades in time. Ethereum at least has one advantage: it was built to evolve. It’s already gone through massive upgrades. Social coordination is part of its DNA. Personally, I don’t think this is immediate doom. But I also don’t think it’s something to laugh off anymore. The chains that treat quantum seriously today are probably the ones that survive smoothly tomorrow. Curious where everyone stands. Is this a 2040 problem? A 2030 problem? Or just another narrative that gets recycled every bull run?

22h ago

---

**[Wall Street giants massively increased holdings in BitMine — the largest corporate ETH holder](https://www.reddit.com/r/ethereum/comments/1r93mxh/wall_street_giants_massively_increased_holdings/)**

New 13F filings show major financial institutions sharply increased positions in BitMine, a public company widely known as the largest corporate holder of Ethereum. Morgan Stanley now holds 12.2M shares (+26%), ARK 9.5M (+27%), BlackRock 9M (+166%), and Goldman Sachs 5.2M (+588%). Vanguard, Bank of America, Schwab, RBC, Citi and BNY Mellon also expanded exposure. In total, 457 institutional holders now control about 136.7M BitMine shares (~$2.86B). This suggests institutions are increasingly accessing ETH exposure via equity structures rather than direct custody — similar to how MicroStrategy functions as a BTC proxy. Full breakdown: https://btcusa.com/wall-street-giants-boost-bitmine-holdings-as-institutional-ethereum-exposure-expands/ Curious how people here see this trend — does equity-based ETH exposure accelerate or delay direct institutional ETH ownership?

1d ago

---

---

## Google News: "ethereum"

**[Vitalik Buterin is building a 'cypherpunk principled non-ugly Ethereum' as devs officially add FOCIL to upgrade roadmap](https://www.theblock.co/post/390682/vitalik-buterin-is-building-a-cypherpunk-principled-non-ugly-ethereum-as-devs-officially-add-focil-to-upgrade-roadmap)**

FOCIL was officially “scheduled for inclusion” as the consensus-layer (CL) headliner for the upcoming Hegota upgrade, targeted for late 2026.

The Block • 15h ago

---

**[BNP Paribas taps Ethereum for new money market fund tokenization pilot](https://www.theblock.co/post/390686/bnp-paribas-taps-ethereum-new-money-market-fund-tokenization-pilot)**

The tokenized shares were issued by the BNP Paribas’ AssetFoundryTM platform using a "permissioned access model on Ethereum."

The Block • 14h ago

---

**[Harvard shakes up its crypto strategy by selling Bitcoin and purchasing Ethereum](https://fortune.com/2026/02/18/harvard-shakes-up-its-crypto-strategy/)**

The Ivy League school still has more money invested in Bitcoin than any other US stock.

Fortune • 2d ago

---

**[BlackRock Signals $270M Bitcoin, Ethereum Sell-Off as $2.4B in Crypto Options Expire](https://finance.yahoo.com/news/blackrock-signals-270m-bitcoin-ethereum-125715997.html)**

BlackRock, the world’s largest asset manager, looks set to offload Bitcoin and Ethereum following the net daily outflows that the crypto ETFs recorded yesterday. This comes as $2.4 billion in crypto options expire, another development that could trigger market volatility. BlackRock Moves $270M In BTC, ETH To Coinbase Arkham data shows that the asset manager

Yahoo Finance • 22h ago

---

**[Bitcoin vs. Ethereum: Which Is the Smarter Buy for 2026 and Beyond?](https://www.nasdaq.com/articles/bitcoin-vs-ethereum-which-smarter-buy-2026-and-beyond)**

Key PointsBitcoin could struggle to retain its reputation as "digital gold".

Nasdaq • 19h ago

---

**[The Ethereum creator and early Polymarket backer doesn't like the direction prediction markets are headed](https://www.businessinsider.com/ethereum-creator-polymarket-backer-raises-concern-about-prediction-markets-future-2026-2)**

Vitalik Buterin, an early Polymarket backer, said prediction markets risk devolving into "corposlop" rather than having long-term financial utility.

Business Insider • 3d ago

---

**[Bitcoin, Ethereum, XRP Waffle as Crypto Crisis Deepens. Why It Could Get Worse.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-crypto-crisis-e43f4227?gaa_at=eafs&gaa_n=AWEtsqeflJiJAwc_HnEGxYr-O9HxBWsD-1oPDz1wv1-rhr8DJmGKIFGtUddL&gaa_ts=69999de5&gaa_sig=YPvX5QH0UTJBB25H_9iY0xlUT4VF9wmztTEE0TS7uoeQa3IUQDDLVghy_GOaK1QHqBZ32mJ0sdCreDOUylDw4g%3D%3D)**

Barron's • 1d ago

---

**[Dual South Korean listings send Ethereum layer-2 token AZTEC surging 82%](https://www.coindesk.com/markets/2026/02/20/dual-s-korea-listings-send-ethereum-layer-2-token-aztec-surging-82)**

Korean exchanges Upbit and Bithumb both added local currency pairs for the privacy-focused layer-2 token, triggering a sharp move in a thinly traded market.

CoinDesk • 1d ago

---

**[Bitmine Immersion: Ethereum's Biggest Public Whale (NYSE:BMNR)](https://seekingalpha.com/article/4871611-bitmine-immersion-ethereum-biggest-public-whale)**

Asymmetric upside for Bitmine Immersion Technologies is likely if Ethereum (and the whole crypto space) recovers from the recent downtrend. More on BMNR stock.

Seeking Alpha • 2d ago

---

**[Prediction: 2026 Will Be the Year of Ethereum (ETH)](https://www.fool.com/investing/2026/02/18/prediction-2026-will-be-the-year-of-ethereum-eth/)**

Ethereum could more than double in price in 2026 to reclaim its all-time high near $5,000.

The Motley Fool • 3d ago

---

---

## YouTube Videos: "ethereum"

**[WHY ETH CAN RALLY NEXT MONTH!🔥 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=50RuciUyE7w)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 74 • 👍 3 • ⏱️ 4:35 • 1h ago

---

**[Tom Lee: The 44x Opportunity EVEN Bigger Than Bitcoin (2026 Prediction)](https://www.youtube.com/watch?v=DAkb7jk3oUE)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Claim your $20 Kalshi bonus when you ...

📺 Crypto Nutshell

👁️ 15K • 👍 504 • 💬 30 • ⏱️ 21:01 • 1d ago

---

**[BITCOIN PRICE PATTERN NO ONE IS WATCHING!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=ZLIMj73KyWg)**

BITCOIN PRICE PATTERN NO ONE IS WATCHING!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 5K • 👍 221 • 💬 24 • ⏱️ 15:50 • 11h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=HI7Dxj99nms)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 98 • 💬 5 • ⏱️ 4:31 • 9h ago

---

**[Coinbase Moves To ETH!🔥Robinhood vs Coinbase🔥SHOTS FIRED!](https://www.youtube.com/watch?v=jSKfTE-aZBQ)**

Optimism has plunged to a new all-time low after intense selling pressure overwhelmed recent demand. The decline accelerated ...

📺 Paul Barron Network

👁️ 55K • 👍 3K • 💬 166 • ⏱️ 15:12 • 1d ago

---

**[🚨 BREAKING: Deep State 911 Insider BUYS ETHEREUM (Howard Lutnick) ($20K ETH) (Tom Lee)](https://www.youtube.com/watch?v=F22KAmIsKd4)**

Donation Address: yourfriendsommi.eth / yourfriendsommi.pls Click Subscribe + Bell Button 'All' Follow on Twitter: ...

📺 🌟yourfriendsommi

👁️ 2K • 👍 240 • 💬 22 • ⏱️ 16:03 • 1d ago

---

**[🚨 BTC &amp; ETH: ALL IN NOW!!!!! &quot;MEGA FOMO PUMP INCOMING!!!&quot;](https://www.youtube.com/watch?v=Rc6HxdvIdd8)**

Bitcoin, ethereum and the rest of crypto is hinting at a pump. Here is my take on all of it. An objective one. ---------- AI Trading ...

📺 Thomas Kralow

👁️ 24K • 👍 4K • 💬 54 • ⏱️ 10:36 • 1d ago

---

**[21 February Today Crypto Live Trading | @bullishbullmaster #bitcoin #ethereum #cryptotrading #gold](https://www.youtube.com/watch?v=HeryDXz0Snw)**

ALL TRADING PLATFORMS Telegram Link https://telegram.me/bullishbull Join Whatsapp Channel ...

📺 Bullish Bull Master

👁️ 6K • 👍 667 • 2h ago

---

**[☠️ What does Howard Lutnick know about Ethereum&#39;s Future?](https://www.youtube.com/watch?v=ki0X2Ur6hGQ)**

Donation Address: yourfriendsommi.eth / yourfriendsommi.pls Click Subscribe + Bell Button 'All' Follow on Twitter: ...

📺 🌟yourfriendsommi

👁️ 542 • 👍 90 • 💬 7 • ⏱️ 10:25 • 3h ago

---

**[The Next Phase of Ethereum: Prediction from Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=uwpXnuUsoiM)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 4K • 👍 77 • 💬 7 • ⏱️ 18:58 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
