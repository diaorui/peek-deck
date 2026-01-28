---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-01-28T05:54:01.478621+00:00'
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

**Last Updated:** January 28, 2026 at 05:54 UTC  
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

### $2,999.96

---

## Ethereum Chart

**24h:** +2.4%  
**7d:** +1.6%  
**30d:** +0.8%  
**90d:** -22.2%  
**1y:** -3.6%  

---

## Ethereum Market Stats

**Market Cap:** $361.86B
Rank #2

**Circulating Supply:** 120,694,374 ETH
No max supply

**All-Time High:** $4,946.05
-39.4%

**All-Time Low:** $0.43
+691721.1%

---

## Reddit: r/ethereum

**[Pouring one out for Week in Ethereum News 🥃 Website is offline. Thank you Evan Van Ness for your tireless efforts serving the Ethereum community. 🙏](https://www.reddit.com/r/ethereum/comments/1qp227f/pouring_one_out_for_week_in_ethereum_news_website/)**

52m ago

---

**[Personal experiment: a smart contract that penalizes me if I skip workouts](https://www.reddit.com/r/ethereum/comments/1qojakt/personal_experiment_a_smart_contract_that/)**

Hi r/ethereum, I’ve been running a personal experiment called FitVow. The idea is simple: I stake real ETH into a smart contract, commit to weekly physical activity goals, and let the contract enforce the rules without a trusted referee. Each week, an Android app reads physical activity data from my smartwatch and publishes it on-chain (e.g. runs, workouts and etc). The contract uses that data to decide whether that week’s goals were met. If a week fails: that week creates an enforceable fine (paid out from the stake) enforcement is permissionless (anyone can trigger it) the fine is split between the enforcer (caller) and a charity wallet (Giveth) At the end of the challenge, I’m allowed to withdraw whatever remains of the stake after any fines. There’s no backend deciding outcomes and no admin override. Once deployed, the rules are the rules. This is not a product — just an experiment exploring whether Ethereum is a good tool for credible self-commitment outside of DeFi. Live dashboard (reads directly from on-chain data): https://fitvow.pedroaugusto.dev/ Technical write-up (architecture + security assumptions): https://pedrooaugusto.github.io/blog/posts/making-missed-workouts-cost-money-with-smart-contracts/ I’d love feedback — especially on whether this feels like a reasonable use of Ethereum, and what you’d poke holes in.

13h ago

---

**[Daily General Discussion January 27, 2026](https://www.reddit.com/r/ethereum/comments/1qo5o60/daily_general_discussion_january_27_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

23h ago

---

**[Built a little ethereum wallet for a metamask interview](https://www.reddit.com/r/ethereum/comments/1qon8y9/built_a_little_ethereum_wallet_for_a_metamask/)**

10h ago

---

**[The scaling hierarchy in blockchains](https://www.reddit.com/r/ethereum/comments/1qo08yq/the_scaling_hierarchy_in_blockchains/)**

Computation > data > state Computation is easier to scale than data. You can parallelize it, require the block builder to provide all kinds of "hints" for it, or just replace arbitrary amounts of it with a proof of it. Data is in the middle. If an availability guarantee on data is required, then that guarantee is required, no way around it. But you can split it up and erasure code it, a la PeerDAS. You can do graceful degradation for it: if a node only has 1/10 the data capacity of the other nodes, it can always produce blocks 1/10 the size. State is the hardest. To guarantee the ability to verify even one transaction, you need the full state. If you replace the state with a tree and keep the root, you need the full state to be able to update that root. There are ways to split it up, but they involve architecture changes, they are fundamentally not general-purpose. Hence, if you can replace state with data (without introducing new forms of centralization), by default you should seriously consider it. And if you can replace data with computation (without introducing new forms of centralization), by default you should seriously consider it.

1d ago

---

**[EqualFi - Public Testnet Soon](https://www.reddit.com/r/ethereum/comments/1qo2lu4/equalfi_public_testnet_soon/)**

Hey r/defi. My name is Matt and I have built something different. EqualFi offers the following: 0% Interest self secured on chain credit. P2P Synthetic and ERC-1155 Covered Calls and Puts. A true P2P Lending system. SOLO AMM and Multi Maker AMMs all time bounded (this is powerful ask me how) Maker Auction Markets(MAM) this is something you have never seen before. Its an MEV resistant way to trade using dutch auction curves on chain. All with a Unified Liquidity pool and Internal ledger. No token(for now). Just DeFi infrastructure that anyone can build on. And here is the kicker. All without oracles or any chance of Liquidation. With this system perpetual leverage without possiblity of liquidation is REAL. This does not mean it is risk free but you cannot get liquidated by a errant wick at 3 am. Below is a link to the Github, and a link to the Discord in case you want to hop in and say hi. You don't have to believe but you should keep an eye on this project. If you want to help shape something new come say hi. Github: https://github.com/EqualFiLabs/EqualFi Discord: https://discord.gg/brsMNDux4T

1d ago

---

**[How to store Private Key in Browser](https://www.reddit.com/r/ethereum/comments/1qob7o2/how_to_store_private_key_in_browser/)**

I am trying to create a delegate wallet for every user which is connected to my dApp. I intend to have access to the private key so that I can initiate and sign transactions on the users behalf. So I am thinking of making the wallet pub and priv key on client side and I don't want the priv key to ever leave client's browser. Is it possible to implement something like this ? I use Privy for siwe if that can help me in any way.

18h ago

---

**[Daily General Discussion January 26, 2026](https://www.reddit.com/r/ethereum/comments/1qn7wd5/daily_general_discussion_january_26_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Liquity's BOLD stablecoin receives A- rating from Bluechip with perfect scores in Management, Decentralization, and Governance](https://www.reddit.com/r/ethereum/comments/1qnid9x/liquitys_bold_stablecoin_receives_a_rating_from/)**

Bluechip (independent stablecoin rating agency) just published their rating for $BOLD, Liquity Protocol's new stablecoin. Thought this sub might find it interesting given the ongoing discussions about decentralized stables and Ethereum's role in the stablecoin ecosystem. Key Findings: Overall Rating: A- (outranks USDC at B+ and DAI at B+) Perfect 1.0 Scores: Management (immutable protocol, no admin keys) Decentralization (no single point of control) Governance (no governance - protocol cannot be altered) Stability Score: 0.88 What Makes BOLD Different: BOLD is the only A- rated stablecoin backed 100% by crypto-native collateral: 100% Ethereum-native collateral (ETH, wstETH, rETH) >200% overcollateralized (currently 291%) Immutable smart contracts (cannot be upgraded or changed) No blacklist function (cannot be frozen) Always redeemable at $1 for underlying collateral For comparison, PYUSD also has an A- rating but is backed by bank deposits and US Treasuries. Context: BOLD is built by the team behind LUSD (Liquity V1), which has been live for 4+ years with $5B peak TVL and zero exploits. Given how much this sub discusses Ethereum's role as the stablecoin settlement layer (especially with $18.8T settled on Ethereum in 2025), figured this was relevant. Full Bluechip Report: https://bluechip.org/en More on Liquity Protocol: https://x.com/LiquityProtocol/status/2015798256186360000 Happy to answer questions about the protocol or rating methodology.

1d ago

---

**[All you need to know about Ethereum Glamsterdam Upgrade](https://www.reddit.com/r/ethereum/comments/1qngb7l/all_you_need_to_know_about_ethereum_glamsterdam/)**

Curated resources by EtherWorld for Glamsterdam Upgrade

🔗 [EtherWorld.co](https://etherworld.co/all-you-need-to-know-about-ethereum-glamsterdam-upgrade/) • 1d ago

---

---

## Google News: "ethereum"

**[Ethereum vs Polkadot: Which Is More Likely to Be a Millionaire-Maker?](https://www.fool.com/investing/2026/01/26/ethereum-vs-polkadot-which-is-more-likely-to-be-a/)**

Should you invest in the blue chip token or the smaller altcoin?

The Motley Fool • 1d ago

---

**[Ethereum whale resurfaces after nine years, moves $145 million in ETH](https://www.theblock.co/post/386974/ethereum-whale-moves-145-million)**

An Ethereum whale moved 50,000 ETH on Sunday after approximately nine years of dormancy, according to onchain data.

The Block • 2d ago

---

**[Ethereum News: Ether Price Surged 226% After This Global Liquidity Signal — Is ETH Setting Up Another Breakout?](https://www.binance.com/en/square/post/01-27-2026-ethereum-news-ether-price-surged-226-after-this-global-liquidity-signal-is-eth-setting-up-another-breakout-35635381799361)**

Binance • 1d ago

---

**[Tom Lee's BitMine Makes Biggest Ethereum Buy Yet in 2026](https://finance.yahoo.com/news/tom-lees-bitmine-makes-biggest-155303327.html)**

Publicly traded Ethereum treasury firm BitMine Immersion Technologies added to its stash with its largest ETH acquisition of the year so far.

Yahoo Finance • 1d ago

---

**[Tom Lee's BitMine nears 70% of Ethereum treasury target with latest 40,302 ETH buy](https://www.theblock.co/post/387035/tom-lee-bitmine-ethereum-buy)**

BitMine's total crypto and cash holdings currently stand at $12.8 billion, and the company owns 3.52% of Ethereum's circulating supply.

The Block • 1d ago

---

**[BitMine Highlights Massive Ethereum Treasury and Staking Strategy](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-and-staking-strategy)**

The latest announcement is out from BitMine Immersion Technologies ( ($BMNR) ). On January 23, 2026, Bitmine Immersion Technologies appointed its current Chief Fina...

TipRanks • 1d ago

---

**[Why This Former BlackRock Executive Thinks Ethereum's TVL Will 10X in 2026](https://www.coindesk.com/markets/2026/01/26/macro-fears-mask-ethereum-s-momentum-sharplink-ceo-says)**

SharpLink CEO Joseph Chalom argues that macro uncertainty is hiding a massive institutional shift toward Ethereum-based tokenization.

CoinDesk • 1d ago

---

**[Zama’s Encrypted Ethereum Token Auction Draws $118M in Commitments](https://thedefiant.io/news/defi/zama-s-encrypted-ethereum-token-auction-draws-usd118m-in-commitments)**

The project said its auction app dominated Ethereum activity on Jan. 24 and that TVS topped $100 million within three days.

thedefiant.io • 1d ago

---

**[Ethereum already ‘20%’ of the way toward quantum resilience: Interview](https://www.tradingview.com/news/cointelegraph:cbf987f35094b:0-ethereum-already-20-of-the-way-toward-quantum-resilience-interview/)**

Antonio Sanso, cryptography researcher at the Ethereum Foundation, is confident the blockchain will be quantum secure long before a quantum attack is even possible.”We as the Ethereum Foundation (EF) and Ethereum community are working massively on this topic,” he told Cointelegraph.“The research pa…

TradingView • 15h ago

---

**[Morning Minute: Ethereum Prepares for the Quantum Era](https://decrypt.co/355831/morning-minute-ethereum-prepares-for-the-quantum-era)**

The Ethereum Foundation is starting to prepare one of the biggest risks facing the crypto industry: quantum computing.

Decrypt • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [2026 New Prediction]](https://www.youtube.com/watch?v=OzflL_FbMXA)**

Tom Lee Just Said The UNTHINKABLE About Bitcoin & Ethereum! [2026 New Prediction] My FREE Daily 5-Min Crypto ...

📺 Crypto Nutshell

👁️ 19K • 👍 587 • 💬 55 • ⏱️ 14:37 • 14h ago

---

**[Ethereum: Das 10x-Szenario, das alle übersehen!](https://www.youtube.com/watch?v=HjIfdWoxja4)**

Jetzt gratis sichern → https://www.blockchain-investor.de/app Die neue „Blockchain-Investor“-App – mit exklusiven ...

📺 Krypto Report

👁️ 8K • 👍 563 • 💬 58 • ⏱️ 17:05 • 12h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=DiW-iNg4n2Y)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 114 • 💬 9 • ⏱️ 4:08 • 12h ago

---

**[Ethereum: Dubious Speculation](https://www.youtube.com/watch?v=J-QHMNnRK-Q)**

Let's talk about Ethereum! For inquirires: https://www.benjamincowen.com/ Into The Cryptoverse Premium: ...

📺 Benjamin Cowen

👁️ 67K • 👍 3K • 💬 232 • ⏱️ 26:46 • 2d ago

---

**[🚨 BTC &amp; ETH: SCARY!!!!!](https://www.youtube.com/watch?v=ChdzwU6zguI)**

These news have huge implications towards bitcoin, ethereum and the rest of crypto! Here is my take on the situation and my ...

📺 Thomas Kralow

👁️ 18K • 👍 3K • 💬 37 • ⏱️ 10:51 • 1d ago

---

**[BITCOIN &amp; CRYPTO JUST FLIPPED (for now)!!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=HLqdFqJvRQQ)**

BITCOIN & CRYPTO JUST FLIPPED (for now)!!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* https://bit.ly/TOOBIT ...

📺 Crypto World

👁️ 4K • 👍 243 • 💬 61 • ⏱️ 18:19 • 7h ago

---

**[Why BlackRock’s Former Crypto Head is Betting on Ethereum](https://www.youtube.com/watch?v=cNz1kdSecWU)**

SharpLink CEO and former BlackRock head of digital assets strategy, Joseph Chalom, joins CoinDesk's Jennifer Sanasie on ...

📺 CoinDesk

👁️ 18K • 👍 570 • 💬 105 • ⏱️ 23:51 • 1d ago

---

**[BITCOIN AND ETH: SILVER CATCHUP RALLY WILL BE INSANE!!!!](https://www.youtube.com/watch?v=aKaFXbZkTnM)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 22K • 👍 1K • 💬 104 • ⏱️ 59:47 • 19h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=jitFf5Sl5ew)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 98 • 💬 6 • ⏱️ 4:04 • 1d ago

---

**[$3.1M Gone: Why Ethereum Bridges Are Failing While Cardano Wins](https://www.youtube.com/watch?v=Qgml_XaP44g)**

This conversation delves into the current state and future of the Cardano ecosystem, focusing on oracles, decentralised ...

📺 Learn Cardano

👁️ 3K • 👍 290 • 💬 48 • ⏱️ 22:54 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*
