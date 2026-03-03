---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-03T19:57:20.299848+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- social
- videos
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 03, 2026 at 19:57 UTC  
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

### $1,960.63

---

## Ethereum Chart

**24h:** -2.1%  
**7d:** -3.1%  
**30d:** -15.0%  
**90d:** -36.3%  
**1y:** -8.3%  

---

## Ethereum Market Stats

**Market Cap:** $239.06B
Rank #2

**Circulating Supply:** 120,692,182 ETH
No max supply

**All-Time High:** $4,946.05
-60.0%

**All-Time Low:** $0.43
+457252.4%

---

## Reddit: r/ethereum

**[Daily General Discussion March 03, 2026](https://www.reddit.com/r/ethereum/comments/1rjhj9n/daily_general_discussion_march_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

13h ago

---

**[GavCoin: Gavin Wood's 2016 token is still mineable on Ethereum mainnet](https://www.reddit.com/r/ethereum/comments/1rjsruk/gavcoin_gavin_woods_2016_token_is_still_mineable/)**

Before ERC-20 existed, Gavin Wood wrote a token contract called GavCoin and pushed it to the official ethereum/dapp-bin repository. The source code uses sendCoin and coinBalanceOf instead of transfer and balanceOf - it predates any token standard. In July 2015, Vitalik referenced GavCoin five times in his "On Abstraction" blog post as the canonical example for explaining how tokens work on Ethereum. It was already part of the shared vocabulary of early Ethereum developers before mainnet had been live for a week. The contract was deployed to mainnet on April 26, 2016 (block 1,408,600) from a wallet traceable to EthDev and the Genesis block. The name "GavCoin" is hardcoded in the constructor bytecode. A day later, Gavin tweeted "Aww. Me and my key" - his only tweet that month. The mining mechanism is interesting. Anyone can call mine() to mint GAV proportional to the number of blocks elapsed since the last mint. It's essentially a faucet with a time-weighted distribution - earlier miners get more since block intervals accumulate. The validator of the block also receives an equal amount. There's no supply cap. We rebuilt the original dapp as a static site and put it on IPFS, accessible through ENS at gavcoin.eth.limo. You can connect a wallet and actually mine, send, or check balances. The history page documents the full provenance trail with primary sources. The contract: 0xb4abc1bfc403a7b82c777420c81269858a4b8aa4 Original source: ethereum/dapp-bin/coin

4h ago

---

**[Best crypto app/wallet](https://www.reddit.com/r/ethereum/comments/1rjrx6h/best_crypto_appwallet/)**

I’m looking for a mobile wallet that’s easy to use but secure, especially since I don’t have a laptop and need a mobile‑first solution. I know this question gets asked a lot, but older recommendations don’t feel as relevant anymore with recent hacks and data leaks. Right now I’m on an exchange, but I want to move to a hot wallet first and maybe in a few months go to a cold wallet once I feel more comfortable. So, what’s the best hot/mobile wallet out there right now for beginners? What do you use?

4h ago

---

**[[Roadmap] The block building pipeline](https://www.reddit.com/r/ethereum/comments/1rizbm7/roadmap_the_block_building_pipeline/)**

In Glamsterdam, Ethereum is getting ePBS, which lets proposers outsource to a free permissionless market of block builders. This ensures that block builder centralization does not creep into staking centralization, but it leaves the question: what do we do about block builder centralization? And what are the other problems in the block building pipeline that need to be addressed, and how? This has both in-protocol and extra-protocol components. FOCIL FOCIL is the first step into in-protocol multi-participant block building. FOCIL lets 16 randomly-selected attesters each choose a few transactions, which must be included somewhere in the block (the block gets rejected otherwise). This means that even if 100% of block building is taken over by one hostile actor, they cannot prevent transactions from being included, because the FOCILers will push them in. "Big FOCIL" This is more speculative, but has been discussed as a possible next step. The idea is to make the FOCILs bigger, so they can include all of the transactions in the block. We avoid duplication by having the i'th FOCIL'er by default only include (i) txs whose sender address's first hex char is i, and (ii) txs that were around but not included in the previous slot. So at the cost of one slot delay, only censored txs risk duplication. Taking this to its logical conclusion, the builder's role could become reduced to ONLY including "MEV-relevant" transactions (eg. DEX arbitrage), and computing the state transition. Encrypted mempools Encrypted mempools are one solution being explored to solve "toxic MEV": attacks such as sandwiching and frontrunning, which are exploitative against users. If a transaction is encrypted until it's included, no one gets the opportunity to "wrap" it in a hostile way. The technical challenge is: how to guarantee validity in a mempool-friendly and inclusion-friendly way that is efficient, and what technique to use to guarantee that the transaction will actually get decrypted once the block is made (and not before). The transaction ingress layer One thing often ignored in discussions of MEV, privacy, and other issues is the network layer: what happens in between a user sending out a transaction, and that transaction making it into a block? There are many risks if a hostile actor sees a tx "in the clear" inflight: If it's a defi trade or otherwise MEV-relevant, they can sandwich it In many applications, they can prepend some other action which invalidates it, not stealing money, but "griefing" you, causing you to waste time and gas fees If you are sending a sensitive tx through a privacy protocol, even if it's all private onchain, if you send it through an RPC, the RPC can see what you did, if you send it through the public mempool, any analytics agency that runs many nodes will see what you did There has recently been increasing work on network-layer anonymization for transactions: exploring using Tor for routing transactions, ideas around building a custom ethereum-focused mixnet, non-mixnet designs that are more latency-minimized (but bandwidth-heavier, which is ok for transactions as they are tiny) like Flashnet, etc. This is an open design space, I expect the kohaku initiative @ncsgy will be interested in integrating pluggable support for such protocols, like it is for onchain privacy protocols. There is also room for doing (benign, pro-user) things to transactions before including them onchain; this is very relevant for defi. Basically, we want ideal order-matching, as a passive feature of the network layer without dependence on servers. Of course enabling good uses of this without enabling sandwiching involves cryptography or other security, some important challenges there. Long-term distributed block building There is a dream, that we can make Ethereum truly like BitTorrent: able to process far more transactions than any single server needs to ever coalesce locally. The challenge with this vision is that Ethereum has (and indeed a core value proposition is) synchronous shared state, so any tx could in principle depend on any other tx. This centralizes block building. "Big FOCIL" handles this partially, and it could be done extra-protocol too, but you still need one central actor to put everything in order and execute it. We could come up with designs that address this. One idea is to do the same thing that we want to do for state: acknowledge that >95% of Ethereum's activity doesn't really need full globalness, though the 5% that does is often high-value, and create new categories of txs that are less global, and so friendly to fully distributed building, and make them much cheaper, while leaving the current tx types in place but (relatively) more expensive. This is also an open and exciting long-term future design space.

1d ago

---

**[How we evaluate blockchain interoperability and infrastructure for our DAO](https://www.reddit.com/r/ethereum/comments/1rjfyvm/how_we_evaluate_blockchain_interoperability_and/)**

Manage a DAO with about $8m in treasury. Part of my role is evaluating grant applications and infrastructure investments that could benefit our ecosystem. Constantly get pitched for funding. When deciding this is what matters: Does this solve a real problem? We validate with actual developers and users. Is the team capable of executing? Check github, previous projects and references, not just technical skills. What's the total cost? Not just the initial grant but ongoing maintenance, integration costs, potential technical debt. Recently evaluated a $200k proposal for custom dev tooling and infrastructure. We did deep diligence, talked to 15 developers and reviewed the technical approach. We took a different funding approach. Instead of building everything custom, we partnered with existing solutions like caldera that already solved most of the problem. Cost was a fraction of a custom build and shipped in weeks instead of months. Our developers are happy and we didn't take on maintaining custom infrastructure. Managing DAO funds means accountability to the community. Can't just yolo into shiny projects. Think sustainability and actual usage. Good solutions already exist.

15h ago

---

**[Daily General Discussion March 02, 2026](https://www.reddit.com/r/ethereum/comments/1rikxzj/daily_general_discussion_march_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Accidentally sent USDT to USDT address](https://www.reddit.com/r/ethereum/comments/1rj7c4p/accidentally_sent_usdt_to_usdt_address/)**

Please help me it’s a large amount, is it lost forever? USDT to a USDC address sorry for typo

21h ago

---

**[RWA on Ethereum feels less like hype and more like a maturity test](https://www.reddit.com/r/ethereum/comments/1rj5ncr/rwa_on_ethereum_feels_less_like_hype_and_more/)**

Maybe unpopular take, but I don’t think RWA is a “narrative” anymore. A few cycles ago, yield on Ethereum mostly meant emissions. Liquidity mining. Governance token incentives. Boosted pools. You could almost feel the dilution in real time. It worked. Until it didn’t. The structural issue was obvious in hindsight: yield funded by token inflation isn’t the same as yield funded by external cashflow. One depends on reflexivity. The other depends on actual economic activity somewhere outside the EVM. That’s why RWA keeps resurfacing here. Centrifuge tried collateralized real-world assets. Maple leaned into institutional credit. Ondo pushed tokenized Treasuries into DeFi rails. Goldfinch experimented with undercollateralized lending. Different risk models. Same direction: Ethereum as settlement for off-chain cashflows. I’ve been looking at 8lends recently from a portfolio construction angle. RWA-backed lending, fixed monthly payouts, structured more like credit exposure than a farm. Not exciting. Which is kind of the point. Fixed doesn’t mean safe. It just means the risk moves. From token dilution and volatility to underwriting quality and legal enforceability. But if Ethereum wants to evolve beyond cyclical liquidity games, it probably needs primitives that aren’t purely reflexive. So the real question for this sub: Is RWA a necessary evolution for Ethereum DeFi, or are we just wrapping TradFi risk and calling it innovation? And how much transparency would you need before allocating capital to an RWA protocol?

22h ago

---

**[I built a decentralized file vault where only your crypto wallet can decrypt your data — no centralized providers holds your encryption keys](https://www.reddit.com/r/ethereum/comments/1rjhxgu/i_built_a_decentralized_file_vault_where_only/)**

13h ago

---

**[What the shift to mobile ZK-ML means for the ecosystem](https://www.reddit.com/r/ethereum/comments/1rj41je/what_the_shift_to_mobile_zkml_means_for_the/)**

I’ve always felt that the biggest hurdle for decentralized identity was the "black box" problem of physical hardware. Most of us here have followed the controversy surrounding the Orb and the inherent trust issues that come with proprietary biometric sensors. It’s a classic security vs. privacy trade-off that usually ends in a stalemate. However, the recent open-sourcing of the Remainder prover marks a pretty significant shift in the technical architecture that’s worth looking at from an Ethereum-centric perspective. We’re essentially seeing the transition from "Trust the Gadget" to "Verify the Math". By moving the heavy ML processing from a physical device directly to a user’s smartphone using a GKR + Hyrax-based proof system, we’re entering the territory of production-grade ZK-ML on consumer hardware. This is a massive engineering leap because running machine learning layers locally and generating a ZK-proof that the model was executed correctly - without the raw data ever leaving the device - is exactly the kind of client-side verifiability we’ve been talking about for years. It turns the phone into a verifiable node of trust, potentially making the physical Orb a one-time gateway rather than a permanent central authority. This is more than just an update to a single project; it’s a high-stakes stress test for ZK-SNARKs on the edge. If we can prove that high-performance provers can handle complex ML inferences on mobile GPUs without compromising privacy or draining the battery, it changes the game for everything from Proof-of-Personhood to private DAO voting. It’s a fascinating pivot from hardware-centric identity to a math-first approach, and I’m curious if this finally bridges the gap for those who were previously put off by the centralized nature of the initial setup.

23h ago

---

---

## Google News: "ethereum"

**[Bitcoin, Ethereum ETFs Snap Five-Week Losing Streak as Crypto Funds Add $1 Billion](https://decrypt.co/359587/bitcoin-ethereum-etfs-snap-losing-streak-crypto-funds-1-billion)**

Bitcoin and other crypto funds rebounded with $1 billion worth of inflows last week, ending a five-week, $4 billion losing streak.

Decrypt • 1d ago

---

**[Vitalik Buterin lays out a two-part plan to overhaul Ethereum's execution layer from the ground up](https://www.theblock.co/post/391681/vitalik-buterin-lays-out-a-two-part-plan-to-overhaul-ethereums-execution-layer-from-the-ground-up)**

The binary tree proposal is a concrete, in-progress effort, while the VM transition remains more speculative and lacks broad consensus among developers.

The Block • 1d ago

---

**[Inside the Harvard's crypto play: Why the endowment is swapping bitcoin for ethereum ETFs](https://www.coindesk.com/business/2026/03/03/here-is-why-harvard-trimmed-bitcoin-and-bought-ether-and-why-the-move-is-bullish-for-crypto)**

Volatility and private equity cash needs, not a market bet, may explain the endowment’s crypto shift, experts say.

CoinDesk • 4h ago

---

**[Ethereum Price, BitMine Shares Jump as Tom Lee's Treasury Reports Latest Buy](https://finance.yahoo.com/news/ethereum-price-bitmine-shares-jump-153447384.html)**

Publicly traded Ethereum treasury BitMine Immersion Technologies added to its ETH stack last week despite its recent decline.

Yahoo Finance • 1d ago

---

**[Ethereum Price Tests Support Near $1,940 As Risk Sentiment Turns Defensive](https://seekingalpha.com/article/4877752-ethereum-price-tests-support-near-1940-as-risk-sentiment-turns-defensive)**

Ethereum (ETH-USD) moved lower on Tuesday, March 3, trading near $1940 after another failed attempt to retake $2000 left the token pinned near the bottom of its recent range. Read more here.

Seeking Alpha • 2h ago

---

**[Bitcoin And Ethereum Prices Are Recovering Again, But Will The US-Israel War Derail It?](https://www.tradingview.com/news/newsbtc:a1ab0f2d5094b:0-bitcoin-and-ethereum-prices-are-recovering-again-but-will-the-us-israel-war-derail-it/)**

The Bitcoin and Ethereum prices plunged sharply over the weekend as missiles flew across the Middle East, exposing just how quickly geopolitical crises can send shockwaves through the financial markets. A joint US and Israel strike on Iran triggered a violent selloff that wiped out billions of doll…

TradingView • 23h ago

---

**[Ethereum Based Crypto Pepeto Announces $7,44M Raised While XRP Price Prediction Targets $20](https://markets.businessinsider.com/news/stocks/ethereum-based-crypto-pepeto-announces-7-44m-raised-while-xrp-price-prediction-targets-20-1035888761)**

Dubai, UAE, March  02, 2026  (GLOBE NEWSWIRE) -- The Pepeto team just announced a major advancement on the blockchain tools they have been buildin...

markets.businessinsider.com • 19h ago

---

**[Grayscale’s Mini Ethereum Trust Sees $1.5M Exit as Ether Slump Tests Investor Nerves](https://www.tipranks.com/news/cryptocurrencies/grayscales-mini-ethereum-trust-sees-1-5m-exit-as-ether-slump-tests-investor-nerves)**

TipRanks • 9h ago

---

**[John Paller: Traditional finance is outpacing crypto execution, distribution is key for mainstream adoption, and Ethereum's scaling issues drive Layer 2 innovation | Epicenter](https://cryptobriefing.com/john-paller-traditional-finance-is-outpacing-crypto-execution-distribution-is-key-for-mainstream-adoption-and-ethereums-scaling-issues-drive-layer-2-innovation-epicenter/)**

Crypto's path to mainstream hinges on overcoming distribution hurdles and embracing institutional finance.

Crypto Briefing • 11h ago

---

**[Ethereum usage is at record highs yet ETH nears its longest monthly losing streak since 2018](https://cryptoslate.com/ethereum-battles-longest-monthly-loss-streak-since-2018/)**

Ethereum's prolonged price decline contrasts with the blockchain network's busiest phase, perplexing investors.

CryptoSlate • 22h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=qZ_aRpWh1ZU)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 129 • 💬 5 • ⏱️ 6:13 • 7h ago

---

**[🚨 BTC &amp; ETH: THE END!!!!!!!!!!!](https://www.youtube.com/watch?v=ESyJ5lBpO3Q)**

Iran, middle east, and so on are not helping Bitcoin. Here is why world war 3 narrative isnt the best for crypto people right now.

📺 Thomas Kralow

👁️ 27K • 👍 3K • 💬 64 • ⏱️ 8:18 • 1d ago

---

**[BUY ETHEREUM!](https://www.youtube.com/watch?v=LfrCGteIJsE)**

Join Discord Group https://painofcrypto.netlify.app/ X https://twitter.com/PainofCrypt0 Instagram ...

📺 Pain of Crypto

👁️ 2K • 👍 97 • 💬 30 • ⏱️ 6:27 • 21h ago

---

**[Vitalik Buterin Is Selling His ETH: What It Means for Ethereum](https://www.youtube.com/watch?v=PuX5B18EZvs)**

Did Vitalik Buterin just dump Ethereum at the worst possible time? After announcing a “few years” funding plan, nearly half the ...

📺 Coin Bureau

👁️ 77K • 👍 2K • 💬 283 • ⏱️ 18:01 • 2d ago

---

**[Set Alerts On Ethereum NOW! Bottom Coming Soon?](https://www.youtube.com/watch?v=sl_KQkhjOY4)**

Get $450 Off Our New AI Indicators: https://tradeconfidentportal.io/indicators Join Trade Confident: Get 25% Off Your 1st Month: ...

📺 Trade Confident

👁️ 742 • 👍 21 • 💬 6 • ⏱️ 5:09 • 1d ago

---

**[WILL ETH BREAKDOWN NOW?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=WlhM55U6kZU)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 202 • 👍 11 • 💬 3 • ⏱️ 5:15 • 9h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=iDEbFROubGk)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 135 • 💬 19 • ⏱️ 5:31 • 17h ago

---

**[Hold On Tight BlackRock Is Making MAJOR Bitcoin Moves Ethereum Is FINALLY Doing This After 9 Years](https://www.youtube.com/watch?v=J4gLyFNI4Uc)**

Well, it looks like someone finally realized that something had to be done or they would be left behind in the cryptocurrency market ...

📺 The Modern Investor

👁️ 7K • 👍 768 • 💬 64 • ⏱️ 27:48 • 1d ago

---

**[BITCOIN &amp; ALTCOIN WARNING: Time Running Out!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=v2z4by2rQ8o)**

BITCOIN & ALTCOIN WARNING: Time Running Out!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 7K • 👍 256 • 💬 63 • ⏱️ 15:51 • 19h ago

---

**[QUAL SERÁ O FUTURO DO ETHEREUM?](https://www.youtube.com/watch?v=HjQBbwxDgbo)**

Qual será o futuro do Ethereum nos próximos anos? Neste vídeo, faço uma análise estratégica sobre os vetores que realmente ...

📺 Orlando on Crypto

👁️ 4K • 👍 706 • 💬 20 • ⏱️ 15:57 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*
