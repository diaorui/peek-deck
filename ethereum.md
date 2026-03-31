---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-31T22:03:17.617986+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- social
- news
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 31, 2026 at 22:03 UTC  
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

### $2,100.38

---

## Ethereum Chart

**24h:** +3.7%  
**7d:** -3.2%  
**30d:** +3.6%  
**90d:** -30.1%  
**1y:** +10.2%  

---

## Ethereum Market Stats

**Market Cap:** $253.56B
Rank #2

**Circulating Supply:** 120,691,415 ETH
No max supply

**All-Time High:** $4,946.05
-57.5%

**All-Time Low:** $0.43
+485099.1%

---

## Reddit: r/ethereum

**[Google Set a 2029 Quantum Deadline. Ethereum Has a Plan. Bitcoin Has a Culture War](https://www.reddit.com/r/ethereum/comments/1s8hti2/google_set_a_2029_quantum_deadline_ethereum_has_a/)**

Google just moved the quantum threat from decades away to 2029. Taproot exposed 6.9 million Bitcoin. Ethereum launched a seven-fork roadmap. Bitcoin has BIP-360 and a mailing list. Here's what that difference means.

🔗 [DailyCoinPost](https://dailycoinpost.com/google-quantum-deadline-2029-ethereum-plan-bitcoin-culture-war/) • 13h ago

---

**[Daily General Discussion March 31, 2026](https://www.reddit.com/r/ethereum/comments/1s8e3ii/daily_general_discussion_march_31_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

17h ago

---

**[Been digging into old Ethereum contracts from 2015-2019 to find withdrawable ETH that portfolio trackers miss](https://www.reddit.com/r/ethereum/comments/1s8phlv/been_digging_into_old_ethereum_contracts_from/)**

Hello everyone! I've built a tool to help recover ETH stuck in old smart contracts that no longer have frontends. Portfolio trackers like Debank and Zerion don't index these balances. 116 contracts, 76,000+ ETH, 516k depositors with claimable balance. Idex, Etherdelta, DigixDAO, PoWH3D, ENS old registrar, Fomo3d, MoonCatRescue, to name a few. One address alone has 10,000 ETH locked in the old ENS registrar deeds - a deposit from a name auction on governx.eth that was never released. Even Vitalik has 75 ETH to claim! Most of these addresses are dormant, but if you were active on Etheruem between 2015-2019, check your address at https://forgotteneth.com Twitter thread It scans all 116 contracts and crafts the withdrawal transaction(s) for you. https://preview.redd.it/2rv0j4bq7esg1.png?width=2236&format=png&auto=webp&s=0f5c26c5306475ba4de4325cbae72757b3738f05

7h ago

---

**[I'm making hey.eth a public, free identity layer for everyone. Agents are able to get their own ENS in <10s. Building open source infra for agentic payments using State Channels.](https://www.reddit.com/r/ethereum/comments/1s8o4zh/im_making_heyeth_a_public_free_identity_layer_for/)**

🔗 [X (formerly Twitter)](https://x.com/0xstatechannel/status/2038977772312272942) • 8h ago

---

**[What is ZCHF?](https://www.reddit.com/r/ethereum/comments/1s8g4y2/what_is_zchf/)**

ZCHF is a decentralized stablecoin that is designed to track the value of the Swiss franc (CHF). Unlike popular stablecoins like USDT or USDC that are pegged to the US dollar, ZCHF is pegged 1:1 to Switzerland’s currency. It is issued by the Frankencoin protocol and operates on blockchain infrastructure, which means it doesn’t rely on traditional banks in the same way centralised stablecoins do. Instead, it uses a system of collateral and smart contracts to maintain its value. Why People Are Talking About It Interest in ZCHF has increased after Vitalik Buterin recently swapped a significant amount of USDC into ZCHF. Moves like this bring attention to the idea that DeFi may not stay centered only around the US dollar.

15h ago

---

**[A universal ZK verification layer for Ethereum - any proof system <30k gas, no trusted setup](https://www.reddit.com/r/ethereum/comments/1s8ilry/a_universal_zk_verification_layer_for_ethereum/)**

With all the discussion around L2 fragmentation lately (EEZ announcement, Superchain, AggLayer), I wanted to share something I've been working on that addresses the problem from a different angle. The issue: every rollup ships its own proof system - Groth16, STARK, Plonk, Halo2, Nova - each needing a separate on-chain verifier at 200k+ gas. Some require trusted setup ceremonies. GLYPH is a universal transparent verification layer that compiles any proof into a common intermediate representation (UCIR) and verifies it through a single on-chain contract. What it does: - Verifies any major proof system through one verifier - <30k gas per on-chain verification (~7.5x cheaper than Groth16 alone) - No trusted setup - fully transparent - Supported: Groth16, KZG, IPA, Plonk, Halo2, STARK (Winterfell, Miden, Cairo/Stone, Circle STARK, Stwo), Nova/HyperNova/Sangria/SuperNova (IVC), SP1, Plonky2/3, Binius How it works: - Packed arity-8 sumcheck over p = 2^128 - 159 - Chain-bound Keccak256 Fiat-Shamir challenges - BaseFold PCS - On-chain verifier in pure Solidity assembly - Formal proof pack with soundness bound ~1.88 x 10^-37 Tested on Sepolia + Hoodi. Benchmarks included and reproducible. Everything is open source under MIT: - Full Paper: https://doi.org/10.5281/zenodo.18792566 https://hackmd.io/@ChristopherSchulze/glyph-zk - Code: https://github.com/Christopher-Schulze/glyph-zk I know the on-chain assembly verifier needs a proper audit before anyone touches it in production - that's on the roadmap. Would love feedback from the community. Happy to answer any questions about the architecture or design decisions.

12h ago

---

**[Beginner's Game Tournament for r/ethereum only](https://www.reddit.com/r/ethereum/comments/1s8gw8d/beginners_game_tournament_for_rethereum_only/)**

I've been all over daily threads for the last two weeks, and some of those really nice folks have been having fun with this little game dapp that I built. I call it Stupid Games, because you play really easy, simple games, but get to win awesome real ETH prizes! It's an arcade type game platform, full of crypto memes, that pays out real ETH prizes to the winners. All managed by smart contracts of course. I'm creating a beginner friendly, mini tournament just for this sub. No players from the current Leaderboard allowed! And when I say beginner, I mean JT level beginner like from the Daily Doots Podcast #143! Lol! No offence JT 😆 Its free, no gas, no cash, just real fun! The prize is $20 or more, but more than that, its bragging rights to be the king of this hill. It's even got a Burner Wallet login, so you know it's not sus. More dapps should do that right? If you want to give it a shot, there's only space for 9-10 players, so drop your [burner] address and I'll let you in. The FLY game is similar to Flappy Bird, and the SHOOT game is similar to Asteroids. Try them and pick your vibe. So what's in it for me? I worked hard on the app and really want to see it being used. I also think it's genuinely fun when you get it. Plus, I took a job break and built it as a porfolio piece so I would love to get feedback. Many features were actually suggestions from users on the daily threads, which I appreciate so much (Alexis and Tricky)! Any and all feedback/criticism welcome. Questions too! Chips are ERC20 tokens but 1:1 exchangeable for 0.0001 eth from the contract. No promotion of any product in this post. No monetary gain for me, only loss 🙁! Play Stupid Games, Win Awesome Prizes! https://reddit.com/link/1s8gw8d/video/us22jk9r2csg1/player https://reddit.com/link/1s8gw8d/video/9zhhtl9r2csg1/player

14h ago

---

**[EIP-712](https://www.reddit.com/r/ethereum/comments/1s8l7du/eip712/)**

10h ago

---

**[The hidden gas and security trade-offs of using CREATE2 + Minimal Proxies for multi-chain deployments](https://www.reddit.com/r/ethereum/comments/1s83w01/the_hidden_gas_and_security_tradeoffs_of_using/)**

Hey everyone, Over the last four years of writing smart contracts and teaching these concepts in EVM bootcamps, I keep seeing teams stumble into the exact same architectural traps when trying to achieve cross-chain address parity. Leveraging CREATE2 for deterministic addresses fundamentally changes how we handle multi-chain deployments. But because init_code includes constructor arguments, maintaining that exact same address across chains is impossible if you need to pass in chain-specific variables (like local router addresses or bridge endpoints). The standard industry workaround is deploying EIP-1167 Minimal Proxies via a universal factory, deploying deterministically, then initializing the state in the same transaction. However, this introduces some severe trade-offs that often get overlooked until they hit production: The DELEGATECALL Gas Tax: Minimal proxies are incredibly cheap to deploy (~45 bytes of bytecode), but they add a DELEGATECALL overhead to every single execution (2600 gas cold, 100 warm). At scale, this execution cost compounds brutally for your users. MEV Front-running Risks: If your proxy deployment and initialize() call are not strictly atomic within the factory contract execution, MEV bots might front-run the initialization transaction. This either bricks the instance entirely or hijacks the contract ownership. Immutability vs Upgradeability: To retain the exact same address while upgrading logic, you have to wrap the implementation in UUPS or Transparent Proxies. This inflates the initial deployment cost and introduces strict storage collision risks (requiring flawless adherence to EIP-1967 storage slots). I just published a full breakdown of these mechanics on my blog, diving into the math behind the gas trade-offs and how patterns like CREATE3 are solving the issue for non-proxy contracts where constructor arguments must differ. If you are currently architecting a multi-chain protocol, you can read the full technical deep dive here:https://andreyobruchkov1996.substack.com/p/understanding-contract-deployments-proxies-and-create2-part-2-df8f05998d5e Would love to hear how you all are handling cross-chain deterministic deployments right now. Are you still relying heavily on customized off-chain salt-mining scripts, or have you migrated to CREATE3 wrappers?

1d ago

---

**[Daily General Discussion March 30, 2026](https://www.reddit.com/r/ethereum/comments/1s7hcs2/daily_general_discussion_march_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

---

## Google News: "ethereum"

**[Crypto's quantum threat is real and its driving diverging strategies across Bitcoin, Ethereum, Solana](https://www.coindesk.com/tech/2026/03/28/here-s-how-bitcoin-ethereum-and-other-networks-are-preparing-for-the-looming-quantum-threat)**

Across many of the most well-known ecosystems like Bitcoin, Ethereum, and Solana, responses are diverging along familiar lines: what to do on social consensus and technical iteration, and community members are split between caution and acceleration.

CoinDesk • 3d ago

---

**[What’s on the Ethereum Roadmap: Glamsterdam, Hegota and Beyond](https://decrypt.co/resources/whats-on-ethereum-roadmap-glamsterdam-hegota-beyond)**

Ethereum has rolled out a steady stream of upgrades since 2022. Here’s how those changes fit together—and what’s still ahead.

Decrypt • 2d ago

---

**[BTBT: Shift to Ethereum and AI drove revenue growth but resulted in a net loss amid crypto volatility](https://www.tradingview.com/news/urn:summary_document_report:quartr.com:3217395:0-btbt-shift-to-ethereum-and-ai-drove-revenue-growth-but-resulted-in-a-net-loss-amid-crypto-volatility/)**

Fiscal 2025 saw a strategic pivot to Ethereum and AI infrastructure, with revenue up 5% to $113.6M but a net loss of $80.3M due to crypto volatility. ETH holdings and staking surged, while mining operations were wound down.Original document: Bit Digital, Inc. [BTBT] SEC 8-K Current Report — Apr. 1…

TradingView • 26m ago

---

**[Tether's USAT Stablecoin Expands Beyond Ethereum Mainnet to Celo](https://finance.yahoo.com/markets/crypto/articles/tethers-usat-stablecoin-expands-beyond-183541607.html)**

The Tether-backed USAT stablecoin built for the U.S. market is expanding to Ethereum layer-2 network Celo with help from Google Cloud.

Yahoo Finance • 3h ago

---

**[Conflux Capital Expands Quantitative Trading Framework for Bitcoin and Ethereum Portfolios](https://www.tradingview.com/news/financewire:6ed21c2d1094b:0-conflux-capital-expands-quantitative-trading-framework-for-bitcoin-and-ethereum-portfolios/)**

London, UK, March 31st, 2026, FinanceWireConflux Capital, a provider of automated digital asset solutions, today announced the expansion of its quantitative trading framework designed to provide institutional-grade stability for BTC and ETH portfolios. As digital asset markets experience increased…

TradingView • 4h ago

---

**[Aave V4 launches on Ethereum mainnet with 'hub-and-spoke' architecture](https://www.theblock.co/post/395617/aave-v4-launches-ethereum-mainnet)**

Aave V4 features a hub-and-spoke architecture that concentrates liquidity to supply a wider range of markets and use cases with credit lines.

theblock.co • 1d ago

---

**[Why Ethereum is quietly becoming a key layer of Africa’s digital economy](https://africa.businessinsider.com/local/markets/why-ethereum-is-quietly-becoming-a-key-layer-of-africas-digital-economy/qrv474b)**

#FeaturedPost

Business Insider Africa • 11h ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.732 Million Tokens, and Total Crypto and Total Cash Holdings of $10.7 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-732-million-tokens-and-total-crypto-and-total-cash-holdings-of-10-7-billion-302728176.html)**

Bitmine has 3,142,643 staked ETH, representing $6.3 billion at $2,005 per ETH MAVAN (Made in America VAlidator Network) launched staking solution on March 25,...

PR Newswire • 1d ago

---

**[Tom Lee's BitMine Adds More Ethereum as Strategy Takes a Break From Bitcoin Buying](https://finance.yahoo.com/markets/crypto/articles/tom-lees-bitmine-adds-more-144553148.html)**

BitMine continued its Ethereum accumulation, adding to its leading ETH treasury while Strategy took a week off from Bitcoin purchases.

Yahoo Finance • 1d ago

---

**[BMNR, ETH news: Bitmine buys 71,000 ETH as digital asset treasuries dial back purchases](https://www.coindesk.com/business/2026/03/30/bitmine-makes-biggest-ether-purchase-in-2026-while-other-digital-asset-treasuries-pull-back)**

Tom Lee's Ethereum treasury bought more than 71,000 ETH over the past week, remaining the sole large corporate crypto buyer as Strategy broke its 13-week bitcoin purchase streak.

CoinDesk • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Institutions Thirsty For ETH🔥MASSIVE Ethereum Update!🚀](https://www.youtube.com/watch?v=-ht1A0Z2vIU)**

This year's EthCC event in Cannes has fielded its first major announcement: the Ethereum Economic Zone. This new effort is ...

📺 Paul Barron Network

👁️ 7K • 👍 801 • 💬 43 • ⏱️ 13:00 • 2h ago

---

**[Ethereum &amp; Cardano: Not Yet](https://www.youtube.com/watch?v=1S1XnTwJ2Q8)**

Hang in there everyone! The risk models that say when to accumulate or exit HERE. Free trial ...

📺 Dan Gambardello

👁️ 3K • 👍 373 • 💬 148 • ⏱️ 13:49 • 3h ago

---

**[🚨 BTC &amp; ETH: SELL ALL ASAP &amp; RUN!!!!!! (New disturbing data!)](https://www.youtube.com/watch?v=6bWLOUY6xAM)**

New data shows the future of markets and crypto in general. Its important for bitcoin, ethereum and so on. BEWARE!

📺 Thomas Kralow

👁️ 22K • 👍 2K • 💬 85 • ⏱️ 11:48 • 1d ago

---

**[FINAL WARNING to ALL Crypto Holders!! (I will delete this in 24 hours)](https://www.youtube.com/watch?v=hzfc05Bphkk)**

If you hold Bitcoin or Ethereum... watch this! (alert!) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily BTC ...

📺 Altcoin Daily

👁️ 51K • 👍 3K • 💬 295 • ⏱️ 9:24 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=qe3pEyuy7g8)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 95 • 💬 3 • ⏱️ 4:22 • 10h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=ZWnnH-XMcAg)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 721 • 👍 76 • ⏱️ 3:35 • 2h ago

---

**[ETHEREUM, THE FED, AND BITCOIN —(THIS CHANGES EVERYTHING)](https://www.youtube.com/watch?v=69b-uYwAlpY)**

Crypto looks calm… but underneath, everything is moving. The Ethereum Foundation just deployed $46M into staking, shifting ...

📺 CLOCKWISE CRYPTO 

👁️ 10K • 👍 273 • 💬 50 • ⏱️ 9:26 • 20h ago

---

**[Former BlackRock Exec Reveals Ethereum&#39;s Future Outlook! | Joseph Chalom](https://www.youtube.com/watch?v=iOmQYMafYG0)**

Joseph Chalom, CEO of SharpLink, joined me to discuss the company's Ethereum treasury strategy and the future of ETH. Topics: ...

📺 Thinking Crypto

👁️ 2K • 👍 160 • 💬 117 • ⏱️ 55:54 • 1d ago

---

**[Tom Lee’s 25x Stock Split Plan to Buy More Ethereum](https://www.youtube.com/watch?v=jfY4mp7WLFs)**

Full Video: https://youtube.com/live/JFLhIqxIA88?feature=share.

📺 Cultivate Crypto

👁️ 31 • 👍 3 • ⏱️ 3:01 • 7h ago

---

**[LIVE: Trump Announces Important News About Crypto! This Speech Will Change the Crypto Industry](https://www.youtube.com/watch?v=S20YYPabkf4)**

TrumpCrypto2026 #DigitalAssets #TrumpAnnouncement Welcome to the Trump Crypto Forum 2026 — streaming LIVE from ...

📺 Nasus Ink

👁️ 3K • 👍 1K • 39m ago

---

---

*Generated by PeekDeck - A glance is all you need*
