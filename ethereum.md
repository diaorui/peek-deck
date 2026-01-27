---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-01-27T01:56:38.872876+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- news
- videos
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** January 27, 2026 at 01:56 UTC  
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

### $2,934.15

---

## Ethereum Chart

**24h:** +2.4%  
**7d:** -2.0%  
**30d:** -0.2%  
**90d:** -22.9%  
**1y:** -4.6%  

---

## Ethereum Market Stats

**Market Cap:** $353.57B
Rank #2

**Circulating Supply:** 120,694,419 ETH
No max supply

**All-Time High:** $4,946.05
-40.8%

**All-Time Low:** $0.43
+676112.9%

---

## Reddit: r/ethereum

**[Daily General Discussion January 26, 2026](https://www.reddit.com/r/ethereum/comments/1qn7wd5/daily_general_discussion_january_26_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

19h ago

---

**[The scaling hierarchy in blockchains](https://www.reddit.com/r/ethereum/comments/1qo08yq/the_scaling_hierarchy_in_blockchains/)**

Computation > data > state Computation is easier to scale than data. You can parallelize it, require the block builder to provide all kinds of "hints" for it, or just replace arbitrary amounts of it with a proof of it. Data is in the middle. If an availability guarantee on data is required, then that guarantee is required, no way around it. But you can split it up and erasure code it, a la PeerDAS. You can do graceful degradation for it: if a node only has 1/10 the data capacity of the other nodes, it can always produce blocks 1/10 the size. State is the hardest. To guarantee the ability to verify even one transaction, you need the full state. If you replace the state with a tree and keep the root, you need the full state to be able to update that root. There are ways to split it up, but they involve architecture changes, they are fundamentally not general-purpose. Hence, if you can replace state with data (without introducing new forms of centralization), by default you should seriously consider it. And if you can replace data with computation (without introducing new forms of centralization), by default you should seriously consider it.

5m ago

---

**[Liquity's BOLD stablecoin receives A- rating from Bluechip with perfect scores in Management, Decentralization, and Governance](https://www.reddit.com/r/ethereum/comments/1qnid9x/liquitys_bold_stablecoin_receives_a_rating_from/)**

Bluechip (independent stablecoin rating agency) just published their rating for $BOLD, Liquity Protocol's new stablecoin. Thought this sub might find it interesting given the ongoing discussions about decentralized stables and Ethereum's role in the stablecoin ecosystem. Key Findings: Overall Rating: A- (outranks USDC at B+ and DAI at B+) Perfect 1.0 Scores: Management (immutable protocol, no admin keys) Decentralization (no single point of control) Governance (no governance - protocol cannot be altered) Stability Score: 0.88 What Makes BOLD Different: BOLD is the only A- rated stablecoin backed 100% by crypto-native collateral: 100% Ethereum-native collateral (ETH, wstETH, rETH) >200% overcollateralized (currently 291%) Immutable smart contracts (cannot be upgraded or changed) No blacklist function (cannot be frozen) Always redeemable at $1 for underlying collateral For comparison, PYUSD also has an A- rating but is backed by bank deposits and US Treasuries. Context: BOLD is built by the team behind LUSD (Liquity V1), which has been live for 4+ years with $5B peak TVL and zero exploits. Given how much this sub discusses Ethereum's role as the stablecoin settlement layer (especially with $18.8T settled on Ethereum in 2025), figured this was relevant. Full Bluechip Report: https://bluechip.org/en More on Liquity Protocol: https://x.com/LiquityProtocol/status/2015798256186360000 Happy to answer questions about the protocol or rating methodology.

10h ago

---

**[All you need to know about Ethereum Glamsterdam Upgrade](https://www.reddit.com/r/ethereum/comments/1qngb7l/all_you_need_to_know_about_ethereum_glamsterdam/)**

Curated resources by EtherWorld for Glamsterdam Upgrade

🔗 [EtherWorld.co](https://etherworld.co/all-you-need-to-know-about-ethereum-glamsterdam-upgrade/) • 12h ago

---

**[Revisiting the Mountain Man](https://www.reddit.com/r/ethereum/comments/1qn2871/revisiting_the_mountain_man/)**

I no longer agree with this previous tweet of mine - since 2017, I have become a much more willing connoisseur of mountains. It's worth explaining why. https://x.com/VitalikButerin/status/873177382164848641 First, the original context. That tweet was in a debate with Ian Grigg, who argued that blockchains should track the order of transactions, but not the state (eg. user balances, smart contract code and storage): The messages are logged, but the state (e.g., UTXO) is implied, which means it is constructed by the computer internally, and then (can be) thrown away. I was heavily against this philosophy, because it would imply that users have no way to get the state other than either (i) running a node that processed every transaction in all of history, or (ii) trusting someone else. In blockchains that commit to the state in the block header (like Ethereum), you can simply prove any value in the state with a Merkle branch. This is conditional on the honest majority assumption: if >= 50% of the consensus participants are honest, then the chain with the most PoW (or PoS) support will be valid, and so the state root will be correct. Trusting an honest majority is far better than trusting a single RPC provider. Not trusting at all (by personally verifying every transaction in the chain) is theoretically ideal, but it's a computation load infeasible for regular users, unless we take the (even worse) tradeoff of keeping blockchain capacity so low that most people cannot even use the chain. Now, what has changed since then? The biggest thing is of course ZK-SNARKs. We now have a technology that lets you verify the correctness of the chain, without literally re-executing every transaction. WE INVENTED THE THING THAT GETS YOU THE BENEFITS WITHOUT THE COSTS! This is like if someone from the future teleported back into US healthcare debates in 2008, and demonstrated a clearly working pill that anyone could make for $15 that cured all diseases. Like, yes, if we have that pill, we should get the government fully out of healthcare, let people make the pill and sell it at Walgreens, and healthcare becomes super affordable so everyone is happy. ZK-SNARKs are literally like that but for the block size war. (With two asterisks for block building centralization and data bandwidth, but that's a separate topic) With better technology, we should raise our expectations, and revisit tradeoffs that we made grudgingly in a previous era. But also, I have actually changed my mind on some of the underlying issues. In 2017, I was thinking about blockchains in terms of academic assumptions - what is okay to rely on honest majority for, when we are ok with 1-of-N trust assumption, etc. If a construction gave better properties under known-acceptable assumptions, I would eagerly embrace it. On a raw subconscious level, I don't think I was sufficiently appreciative of the fact that in the real world, lots of things break. Sometimes the p2p network goes down. Sometimes the p2p network has 20x the latency you expected - anyone who has played WoW can attest to long spans of time when the latency spiked up from its usual ~200ms to 1000-5000ms. Sometimes a third party service you've been relying on for years shuts down, and there isn't a good alternative. If the alternative is that you personally go through a github repo and figure out how to PERSONALLY RUN A SERVER, lots of people will give up and never figure it out and end up permanently losing access to their money. Sometimes mining or staking gets concentrated to the point where 51% attacks are very easy to imagine, and you almost have to game-theoretically analyze consensus security as though 75% of miners or stakers are controlled by one single agent. Sometimes, as we saw with tornado cash, intermediaries all start censoring some application, and your only option becomes to directly use the chain. If we are making a self-sovereign blockchain to last through the ages, THE ANSWER TO THE ABOVE CONUNDRUMS CANNOT ALWAYS BE "CALL THE DEVS". If it is, the devs themselves become the point of centralization - they become DEVS in the ancient Roman sense, where the letter V was used to represent the U sound. The Mountain Man's cabin is not meant as the replacement lifestyle for everyone. It is meant as the safe place to retreat to when things go wrong. It is also meant as the universal BATNA ("Best Alternative to a Negotiated Agreement") - the alternative option that improves your well-being not just in the case when you end up needing it, but also because knowledge of it existing motivates third parties to give you better terms. This is like how Bittorrent existing is an important check on the power of music and video streaming platforms, driving them to offer customers better terms. We do not need to start living every day in the Mountain Man's cabin. But part of maintaining the infinite garden of Ethereum is certainly keeping the cabin well-maintained.

1d ago

---

**[US Spot ETH ETFs recorded $1.5B in net outflows in Q4 2025, the single highest quarter of net outflows for the sector.](https://www.reddit.com/r/ethereum/comments/1qnblvo/us_spot_eth_etfs_recorded_15b_in_net_outflows_in/)**

Despite net outflows and a decline in ETH’s price, ETH ETFs have still had a strong year, posting 48.2% YoY growth. ETHA retains its commanding lead with 57.4% share of assets under management (AUM), followed by ETHE at 14.6%, Fidelity’s FETH at 12.3%, and ETH at 12.3%. Source: https://www.coingecko.com/research/publications/2025-annual-crypto-report

16h ago

---

**[Ledger Wallet - Ethereum Kiln Staking And/Or Other Ethereum Staking Service Recommendations](https://www.reddit.com/r/ethereum/comments/1qn6e9w/ledger_wallet_ethereum_kiln_staking_andor_other/)**

21h ago

---

**[Daily General Discussion January 25, 2026](https://www.reddit.com/r/ethereum/comments/1qmaztv/daily_general_discussion_january_25_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Has anyone actually bought digital gift cards with cryptocurrency?](https://www.reddit.com/r/ethereum/comments/1qmiimm/has_anyone_actually_bought_digital_gift_cards/)**

I’m curious if people are really using crypto to buy digital gift cards, or if it’s more of a niche thing. I’ve been holding some crypto for a while and don’t really want to cash it out to a bank just to spend a small amount. I’m looking for a simple way to use it for normal stuff like food, online shopping, or even travel. I saw sites like aceb.com where you can pay with crypto and instantly get digital gift cards. The idea sounds convenient, especially when cards get blocked or payments fail. I like that delivery is instant and there’s no shipping involved. My main concerns are whether it actually works smoothly and if the cards are easy to use afterward. If you’ve done this before, how was the experience? Did the gift cards work as expected, and would you do it again?

1d ago

---

**[Most Web3 losses don’t start with a smart contract bug](https://www.reddit.com/r/ethereum/comments/1qmemlb/most_web3_losses_dont_start_with_a_smart_contract/)**

A lot of major Web3 losses don’t begin with a Solidity vulnerability. They start with systemic weaknesses: > Key mismanagement > Over-privileged or poorly designed access controls > Centralized infrastructure dependencies >Unsafe upgrade paths and admin mechanisms While smart contract bugs often get the spotlight, real-world incidents show a different pattern. Many failures happen around the contracts not inside them. Smart contract security isn’t just about what’s written in Solidity. It’s about how systems are operated, upgraded, and controlled once they’re live. Audits still matter, but security only works when the

1d ago

---

---

## Google News: "ethereum"

**[Why This Former BlackRock Executive Thinks Ethereum's TVL Will 10X in 2026](https://www.coindesk.com/markets/2026/01/26/macro-fears-mask-ethereum-s-momentum-sharplink-ceo-says)**

SharpLink CEO Joseph Chalom argues that macro uncertainty is hiding a massive institutional shift toward Ethereum-based tokenization.

CoinDesk • 5h ago

---

**[Ethereum vs Polkadot: Which Is More Likely to Be a Millionaire-Maker?](https://www.fool.com/investing/2026/01/26/ethereum-vs-polkadot-which-is-more-likely-to-be-a/)**

Should you invest in the blue chip token or the smaller altcoin?

The Motley Fool • 3h ago

---

**[Why Ethereum Is Recovering Nicely Today, Up Nearly 5%](https://finance.yahoo.com/news/why-ethereum-recovering-nicely-today-232716446.html)**

Ethereum investors are seeing very nice gains to kick off a new week.

Yahoo Finance • 2h ago

---

**[Why Ethereum Is Recovering Nicely Today, Up Nearly 5%](https://www.fool.com/investing/2026/01/26/why-ethereum-is-recovering-nicely-today-up-nearly/)**

Ethereum investors are seeing very nice gains to kick off a new week.

The Motley Fool • 2h ago

---

**[Ethereum whale resurfaces after nine years, moves $145 million in ETH](https://www.theblock.co/post/386974/ethereum-whale-moves-145-million)**

An Ethereum whale moved 50,000 ETH on Sunday after approximately nine years of dormancy, according to onchain data.

The Block • 20h ago

---

**[Ethereum Classic: Buy, Sell, or Hold in 2026?](https://www.nasdaq.com/articles/ethereum-classic-buy-sell-or-hold-2026)**

Key PointsOver the past decade, Ethereum Classic is up 557%.

Nasdaq • 2d ago

---

**[Ethereum Foundation Forms Post-Quantum Team as Security Concerns Mount](https://decrypt.co/355798/ethereum-foundation-forms-post-quantum-team-security-concerns-mount)**

Ethereum researcher Justin Drake said the ecosystem is moving from research to execution as the threat from quantum computing draws closer.

Decrypt • 2d ago

---

**[Ethereum Stalls In A Critical Zone As Breakout Structures Wait For Confirmation](https://www.tradingview.com/news/newsbtc:4b389a7b2094b:0-ethereum-stalls-in-a-critical-zone-as-breakout-structures-wait-for-confirmation/)**

Ethereum remains under pressure in a key support zone, teetering between a potential rebound and further decline. While bullish patterns like the cup-and-handle and ascending triangle are shaping up, confirmation is required before any decisive move.Last Defense Zone: $2,274–$2,104 And The Libra Re…

TradingView • 7h ago

---

**[Ethereum Whales Fell Into a $4 Billion Bull Trap: What’s Next for ETH Price?](https://beincrypto.com/ethereum-price-analysis-bull-trap/)**

Ethereum price broke out, momentum looked real, and buyers stepped in. Charts now show why that move failed and what risk still lies ahead.

BeInCrypto • 1d ago

---

**[ChatGPT sets Ethereum price for February 1, 2026](https://finbold.com/chatgpt-sets-ethereum-price-for-february-1-2026/)**

Artificial intelligence predicts that the Ethereum price is going see a noticeable pullback before the end of the month.

Finbold • 11h ago

---

---

## YouTube Videos: "ethereum"

**[Why BlackRock’s Former Crypto Head is Betting on Ethereum](https://www.youtube.com/watch?v=cNz1kdSecWU)**

SharpLink CEO and former BlackRock head of digital assets strategy, Joseph Chalom, joins CoinDesk's Jennifer Sanasie on ...

📺 CoinDesk

👁️ 5K • 👍 206 • 💬 50 • ⏱️ 23:51 • 5h ago

---

**[🚨 BTC &amp; ETH: SCARY!!!!!](https://www.youtube.com/watch?v=ChdzwU6zguI)**

These news have huge implications towards bitcoin, ethereum and the rest of crypto! Here is my take on the situation and my ...

📺 Thomas Kralow

👁️ 15K • 👍 3K • 💬 44 • ⏱️ 10:51 • 15h ago

---

**[BITCOIN CRASH: Everyone is WRONG (New Signal)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=gMAHYXlriYY)**

BITCOIN CRASH: Everyone is WRONG (New Signal)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 5K • 👍 233 • 💬 75 • ⏱️ 20:33 • 5h ago

---

**[ETH Ethereum SHAKE OUT: Did You Pass The Test???](https://www.youtube.com/watch?v=budvssxiKYw)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 254 • 👍 24 • 💬 15 • ⏱️ 4:37 • 7h ago

---

**[Ethereum: Dubious Speculation](https://www.youtube.com/watch?v=J-QHMNnRK-Q)**

Let's talk about Ethereum! For inquirires: https://www.benjamincowen.com/ Into The Cryptoverse Premium: ...

📺 Benjamin Cowen

👁️ 56K • 👍 3K • 💬 219 • ⏱️ 26:46 • 23h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=uWx8GLP_YFA)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 96 • 💬 8 • ⏱️ 3:42 • 5h ago

---

**[Tom Lee - &quot;Biggest Crypto Reset EVER&quot; | Bitcoin &amp; ETH Price Prediction](https://www.youtube.com/watch?v=lZSS8ZRghvA)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 2K • 👍 81 • 💬 40 • ⏱️ 17:46 • 1d ago

---

**[ETHEREUM TRAP (Banks Caught MANIPULATING)](https://www.youtube.com/watch?v=s-MKAKR4Gc8)**

Nick Valdez noticed that JPMorgan couldn't be further apart when it comes to actions versus words. This is a clear-cut example of ...

📺 Discover Crypto

👁️ 8K • 👍 404 • 💬 102 • ⏱️ 7:22 • 2d ago

---

**[Will Quantum Computing KILL CRYPTO? (What About Ethereum and PulseChain)](https://www.youtube.com/watch?v=D351fZZESM8)**

how to buy PulseChain coins? https://libertyswap.finance buy with card: https://buy-pulsechain.com | buy with bank account: ...

📺 Crypto Coffee

👁️ 130 • 👍 25 • 💬 44 • ⏱️ 11:06 • 1h ago

---

**[Why BlackRock Is Betting on Ethereum (This Changes Everything)](https://www.youtube.com/watch?v=7CPq9AcLZjk)**

Ethereum isn't just another crypto — it's becoming Wall Street's settlement layer. In this video, we break down why BlackRock ...

📺 Gven Sariol | DeFi  | ARCrypto

👁️ 24 • 👍 9 • 💬 3 • ⏱️ 6:56 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
