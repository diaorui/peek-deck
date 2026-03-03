---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-03T13:00:30.087693+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- videos
- news
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 03, 2026 at 13:00 UTC  
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

### $1,952.96

---

## Ethereum Chart

**24h:** -0.5%  
**7d:** -4.4%  
**30d:** -16.1%  
**90d:** -37.1%  
**1y:** -9.5%  

---

## Ethereum Market Stats

**Market Cap:** $237.46B
Rank #2

**Circulating Supply:** 120,692,182 ETH
No max supply

**All-Time High:** $4,946.05
-60.2%

**All-Time Low:** $0.43
+454300.8%

---

## Reddit: r/ethereum

**[Daily General Discussion March 03, 2026](https://www.reddit.com/r/ethereum/comments/1rjhj9n/daily_general_discussion_march_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

6h ago

---

**[Thinking of buying a full ethereum](https://www.reddit.com/r/ethereum/comments/1rjnnh7/thinking_of_buying_a_full_ethereum/)**

I have XRP, I was always interested in ethereum and followed it. It was just up high and I wanted to buy a whole coin. Now I have that opportunity. What’s everyone’s thoughts and opinions? Thanks!

51m ago

---

**[[Roadmap] The block building pipeline](https://www.reddit.com/r/ethereum/comments/1rizbm7/roadmap_the_block_building_pipeline/)**

In Glamsterdam, Ethereum is getting ePBS, which lets proposers outsource to a free permissionless market of block builders. This ensures that block builder centralization does not creep into staking centralization, but it leaves the question: what do we do about block builder centralization? And what are the other problems in the block building pipeline that need to be addressed, and how? This has both in-protocol and extra-protocol components. FOCIL FOCIL is the first step into in-protocol multi-participant block building. FOCIL lets 16 randomly-selected attesters each choose a few transactions, which must be included somewhere in the block (the block gets rejected otherwise). This means that even if 100% of block building is taken over by one hostile actor, they cannot prevent transactions from being included, because the FOCILers will push them in. "Big FOCIL" This is more speculative, but has been discussed as a possible next step. The idea is to make the FOCILs bigger, so they can include all of the transactions in the block. We avoid duplication by having the i'th FOCIL'er by default only include (i) txs whose sender address's first hex char is i, and (ii) txs that were around but not included in the previous slot. So at the cost of one slot delay, only censored txs risk duplication. Taking this to its logical conclusion, the builder's role could become reduced to ONLY including "MEV-relevant" transactions (eg. DEX arbitrage), and computing the state transition. Encrypted mempools Encrypted mempools are one solution being explored to solve "toxic MEV": attacks such as sandwiching and frontrunning, which are exploitative against users. If a transaction is encrypted until it's included, no one gets the opportunity to "wrap" it in a hostile way. The technical challenge is: how to guarantee validity in a mempool-friendly and inclusion-friendly way that is efficient, and what technique to use to guarantee that the transaction will actually get decrypted once the block is made (and not before). The transaction ingress layer One thing often ignored in discussions of MEV, privacy, and other issues is the network layer: what happens in between a user sending out a transaction, and that transaction making it into a block? There are many risks if a hostile actor sees a tx "in the clear" inflight: If it's a defi trade or otherwise MEV-relevant, they can sandwich it In many applications, they can prepend some other action which invalidates it, not stealing money, but "griefing" you, causing you to waste time and gas fees If you are sending a sensitive tx through a privacy protocol, even if it's all private onchain, if you send it through an RPC, the RPC can see what you did, if you send it through the public mempool, any analytics agency that runs many nodes will see what you did There has recently been increasing work on network-layer anonymization for transactions: exploring using Tor for routing transactions, ideas around building a custom ethereum-focused mixnet, non-mixnet designs that are more latency-minimized (but bandwidth-heavier, which is ok for transactions as they are tiny) like Flashnet, etc. This is an open design space, I expect the kohaku initiative @ncsgy will be interested in integrating pluggable support for such protocols, like it is for onchain privacy protocols. There is also room for doing (benign, pro-user) things to transactions before including them onchain; this is very relevant for defi. Basically, we want ideal order-matching, as a passive feature of the network layer without dependence on servers. Of course enabling good uses of this without enabling sandwiching involves cryptography or other security, some important challenges there. Long-term distributed block building There is a dream, that we can make Ethereum truly like BitTorrent: able to process far more transactions than any single server needs to ever coalesce locally. The challenge with this vision is that Ethereum has (and indeed a core value proposition is) synchronous shared state, so any tx could in principle depend on any other tx. This centralizes block building. "Big FOCIL" handles this partially, and it could be done extra-protocol too, but you still need one central actor to put everything in order and execute it. We could come up with designs that address this. One idea is to do the same thing that we want to do for state: acknowledge that >95% of Ethereum's activity doesn't really need full globalness, though the 5% that does is often high-value, and create new categories of txs that are less global, and so friendly to fully distributed building, and make them much cheaper, while leaving the current tx types in place but (relatively) more expensive. This is also an open and exciting long-term future design space.

19h ago

---

**[Accidentally sent USDT to USDT address](https://www.reddit.com/r/ethereum/comments/1rj7c4p/accidentally_sent_usdt_to_usdt_address/)**

Please help me it’s a large amount, is it lost forever? USDT to a USDC address sorry for typo

14h ago

---

**[Daily General Discussion March 02, 2026](https://www.reddit.com/r/ethereum/comments/1rikxzj/daily_general_discussion_march_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[RWA on Ethereum feels less like hype and more like a maturity test](https://www.reddit.com/r/ethereum/comments/1rj5ncr/rwa_on_ethereum_feels_less_like_hype_and_more/)**

Maybe unpopular take, but I don’t think RWA is a “narrative” anymore. A few cycles ago, yield on Ethereum mostly meant emissions. Liquidity mining. Governance token incentives. Boosted pools. You could almost feel the dilution in real time. It worked. Until it didn’t. The structural issue was obvious in hindsight: yield funded by token inflation isn’t the same as yield funded by external cashflow. One depends on reflexivity. The other depends on actual economic activity somewhere outside the EVM. That’s why RWA keeps resurfacing here. Centrifuge tried collateralized real-world assets. Maple leaned into institutional credit. Ondo pushed tokenized Treasuries into DeFi rails. Goldfinch experimented with undercollateralized lending. Different risk models. Same direction: Ethereum as settlement for off-chain cashflows. I’ve been looking at 8lends recently from a portfolio construction angle. RWA-backed lending, fixed monthly payouts, structured more like credit exposure than a farm. Not exciting. Which is kind of the point. Fixed doesn’t mean safe. It just means the risk moves. From token dilution and volatility to underwriting quality and legal enforceability. But if Ethereum wants to evolve beyond cyclical liquidity games, it probably needs primitives that aren’t purely reflexive. So the real question for this sub: Is RWA a necessary evolution for Ethereum DeFi, or are we just wrapping TradFi risk and calling it innovation? And how much transparency would you need before allocating capital to an RWA protocol?

15h ago

---

**[I built a decentralized file vault where only your crypto wallet can decrypt your data — no centralized providers holds your encryption keys](https://www.reddit.com/r/ethereum/comments/1rjhxgu/i_built_a_decentralized_file_vault_where_only/)**

6h ago

---

**[How we evaluate blockchain interoperability and infrastructure for our DAO](https://www.reddit.com/r/ethereum/comments/1rjfyvm/how_we_evaluate_blockchain_interoperability_and/)**

Manage a DAO with about $8m in treasury. Part of my role is evaluating grant applications and infrastructure investments that could benefit our ecosystem. Constantly get pitched for funding. When deciding this is what matters: Does this solve a real problem? We validate with actual developers and users. Is the team capable of executing? Check github, previous projects and references, not just technical skills. What's the total cost? Not just the initial grant but ongoing maintenance, integration costs, potential technical debt. Recently evaluated a $200k proposal for custom dev tooling and infrastructure. We did deep diligence, talked to 15 developers and reviewed the technical approach. We took a different funding approach. Instead of building everything custom, we partnered with existing solutions like caldera that already solved most of the problem. Cost was a fraction of a custom build and shipped in weeks instead of months. Our developers are happy and we didn't take on maintaining custom infrastructure. Managing DAO funds means accountability to the community. Can't just yolo into shiny projects. Think sustainability and actual usage. Good solutions already exist.

8h ago

---

**[What the shift to mobile ZK-ML means for the ecosystem](https://www.reddit.com/r/ethereum/comments/1rj41je/what_the_shift_to_mobile_zkml_means_for_the/)**

I’ve always felt that the biggest hurdle for decentralized identity was the "black box" problem of physical hardware. Most of us here have followed the controversy surrounding the Orb and the inherent trust issues that come with proprietary biometric sensors. It’s a classic security vs. privacy trade-off that usually ends in a stalemate. However, the recent open-sourcing of the Remainder prover marks a pretty significant shift in the technical architecture that’s worth looking at from an Ethereum-centric perspective. We’re essentially seeing the transition from "Trust the Gadget" to "Verify the Math". By moving the heavy ML processing from a physical device directly to a user’s smartphone using a GKR + Hyrax-based proof system, we’re entering the territory of production-grade ZK-ML on consumer hardware. This is a massive engineering leap because running machine learning layers locally and generating a ZK-proof that the model was executed correctly - without the raw data ever leaving the device - is exactly the kind of client-side verifiability we’ve been talking about for years. It turns the phone into a verifiable node of trust, potentially making the physical Orb a one-time gateway rather than a permanent central authority. This is more than just an update to a single project; it’s a high-stakes stress test for ZK-SNARKs on the edge. If we can prove that high-performance provers can handle complex ML inferences on mobile GPUs without compromising privacy or draining the battery, it changes the game for everything from Proof-of-Personhood to private DAO voting. It’s a fascinating pivot from hardware-centric identity to a math-first approach, and I’m curious if this finally bridges the gap for those who were previously put off by the centralized nature of the initial setup.

16h ago

---

**[If you're not a developer, have you still ever wanted to create a smart contract?](https://www.reddit.com/r/ethereum/comments/1rifzlz/if_youre_not_a_developer_have_you_still_ever/)**

I've been a crypto developer for about 10 years, so I don't think I can answer this question to myself anymore. and most of my social circle is developers as well so it's kind of the same thing. I'm trying to figure out if (or what anecdotal percentage of) non-developers have any desire to create smart contracts. Or rather, just the desire to create non-template crypto projects. (Full transparency: this is related to something I'm building, but I don't want to promote it here because I'm really just looking to have a discussion) Have you ever wanted to create a crypto project but felt like you couldn't because of the skill gap?

1d ago

---

---

## Google News: "ethereum"

**[Vitalik Buterin lays out a two-part plan to overhaul Ethereum's execution layer from the ground up](https://www.theblock.co/post/391681/vitalik-buterin-lays-out-a-two-part-plan-to-overhaul-ethereums-execution-layer-from-the-ground-up)**

The binary tree proposal is a concrete, in-progress effort, while the VM transition remains more speculative and lacks broad consensus among developers.

The Block • 1d ago

---

**[Bitcoin miner turned Ethereum treasury firm stakes over $6B in ETH as BMNR shares slide and ether dips.](https://www.coindesk.com/business/2026/03/02/bitmine-boosts-ether-holdings-to-4-47m-tokens-after-usd98m-eth-purchase)**

Bitmine chair Tom Lee says company keeps accumulating ETH during market pullback while targeting $253M in annual staking rewards.

CoinDesk • 21h ago

---

**[Ethereum Price, BitMine Shares Jump as Tom Lee's Treasury Reports Latest Buy](https://finance.yahoo.com/news/ethereum-price-bitmine-shares-jump-153447384.html)**

Publicly traded Ethereum treasury BitMine Immersion Technologies added to its ETH stack last week despite its recent decline.

Yahoo Finance • 21h ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.474 Million Tokens, and Total Crypto and Total Cash Holdings of $9.9 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-474-million-tokens-and-total-crypto-and-total-cash-holdings-of-9-9-billion-302700582.html)**

Bitmine has 3,040,483 staked ETH, representing $6.0 billion at $1,976 per ETH; MAVAN staking solution on track to launch Q1 2026 Bitmine now owns 3.71% of the...

PR Newswire • 23h ago

---

**[Ethereum Price Prediction: Whales Drive 7th Red Month While RWA Sector Hits $15B Record](https://finance.yahoo.com/news/ethereum-price-prediction-whales-drive-115101658.html)**

Ethereum is on the verge of something it has never experienced before: a seventh consecutive red month and that is fueling bearish price prediction.For an asset of this size and history, that kind of streak carries psychological weight. It is not just about price drifting lower, it is about confidence ...

Yahoo Finance • 1h ago

---

**[Better Cryptocurrency to Buy Now With $1,000 and Hold for 3 Years: XRP vs. Ethereum](https://www.nasdaq.com/articles/better-cryptocurrency-buy-now-1000-and-hold-3-years-xrp-vs-ethereum)**

Key PointsXRP will soon have an even more sophisticated regulatory compliance suite.

Nasdaq • 1d ago

---

**[This 1 Accelerating Trend Could Drive XRP and Ethereum Higher and Higher](https://www.fool.com/investing/2026/03/03/this-1-accelerating-trend-could-drive-xrp-and-ethe/)**

If you aren't yet exposed to asset tokenization, there are a couple of coins worth knowing about.

The Motley Fool • 1h ago

---

**[Standard Chartered Says Ethereum (ETH) Will Reach $4,000 This Year. But It Will Fall Further First](https://finance.yahoo.com/news/standard-chartered-says-ethereum-eth-102000184.html)**

Once the crypto slump passes, Ethereum is positioned to soar.

Yahoo Finance • 2h ago

---

**[3 Reasons to Sell Cardano Today and Buy Ethereum or XRP Instead](https://www.nasdaq.com/articles/3-reasons-sell-cardano-today-and-buy-ethereum-or-xrp-instead)**

Key PointsIt's unclear what Cardano's competitive strategy is.

Nasdaq • 1h ago

---

**[Vitalik Buterin unveils plan to curb Ethereum block builder centralization](https://www.coindesk.com/tech/2026/03/02/vitalik-buterin-unveils-plan-to-curb-ethereum-block-builder-centralization)**

Another focus of his post is so-called “toxic MEV,” where traders exploit visibility into pending transactions to front-run or “sandwich” users’ trades.

CoinDesk • 18h ago

---

---

## YouTube Videos: "ethereum"

**[🚨 BTC &amp; ETH: THE END!!!!!!!!!!!](https://www.youtube.com/watch?v=ESyJ5lBpO3Q)**

Iran, middle east, and so on are not helping Bitcoin. Here is why world war 3 narrative isnt the best for crypto people right now.

📺 Thomas Kralow

👁️ 27K • 👍 3K • 💬 63 • ⏱️ 8:18 • 1d ago

---

**[BUY ETHEREUM!](https://www.youtube.com/watch?v=LfrCGteIJsE)**

Join Discord Group https://painofcrypto.netlify.app/ X https://twitter.com/PainofCrypt0 Instagram ...

📺 Pain of Crypto

👁️ 2K • 👍 82 • 💬 25 • ⏱️ 6:27 • 15h ago

---

**[Vitalik Buterin Is Selling His ETH: What It Means for Ethereum](https://www.youtube.com/watch?v=PuX5B18EZvs)**

Did Vitalik Buterin just dump Ethereum at the worst possible time? After announcing a “few years” funding plan, nearly half the ...

📺 Coin Bureau

👁️ 76K • 👍 2K • 💬 278 • ⏱️ 18:01 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=qZ_aRpWh1ZU)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 415 • 👍 54 • 💬 2 • ⏱️ 6:13 • 35m ago

---

**[WILL ETH BREAKDOWN NOW?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=WlhM55U6kZU)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 108 • 👍 7 • 💬 3 • ⏱️ 5:15 • 2h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=iDEbFROubGk)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 133 • 💬 19 • ⏱️ 5:31 • 10h ago

---

**[QUAL SERÁ O FUTURO DO ETHEREUM?](https://www.youtube.com/watch?v=HjQBbwxDgbo)**

Qual será o futuro do Ethereum nos próximos anos? Neste vídeo, faço uma análise estratégica sobre os vetores que realmente ...

📺 Orlando on Crypto

👁️ 3K • 👍 579 • 💬 17 • ⏱️ 15:57 • 13h ago

---

**[CRYPTO LIVE TRADING || 3 Mar  | ‪@ClockTraderlive‬ #bitcoin #ethereum #crypto #btclivetrading](https://www.youtube.com/watch?v=8a_NbWd8WwA)**

join my social platforms for updates and analysis ✓Instagram: ...

📺 Aryan trader Live

👁️ 5K • 👍 2K • 2h ago

---

**[Bitcoin &amp; Ethereum. So gehts hoffentlich weiter für BTC &amp; ETH!! Weitere Hochs und dann ABVERKAUF](https://www.youtube.com/watch?v=FyEKKpVnPPA)**

Hier kannst du mich unterstützen und die die Börse BYDFI ansehen! OFFIZIELLER Partner von Newcastle United!

📺 Krypto Trading & Investing

👁️ 4K • 👍 623 • 💬 92 • ⏱️ 10:34 • 8h ago

---

**[BITCOIN &amp; ALTCOIN WARNING: Time Running Out!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=v2z4by2rQ8o)**

BITCOIN & ALTCOIN WARNING: Time Running Out!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 6K • 👍 247 • 💬 12 • ⏱️ 15:51 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
