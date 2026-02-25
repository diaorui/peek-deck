---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-25T23:56:14.317616+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- videos
- cryptocurrency
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 25, 2026 at 23:56 UTC  
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

### $2,065.80

---

## Ethereum Chart

**24h:** +10.9%  
**7d:** +5.4%  
**30d:** -32.1%  
**90d:** -32.2%  
**1y:** -11.8%  

---

## Ethereum Market Stats

**Market Cap:** $247.54B
Rank #2

**Circulating Supply:** 120,692,321 ETH
No max supply

**All-Time High:** $4,946.05
-58.5%

**All-Time Low:** $0.43
+474093.9%

---

## Reddit: r/ethereum

**[My comments on Ethereum strawmap](https://www.reddit.com/r/ethereum/comments/1rera79/my_comments_on_ethereum_strawmap/)**

https://strawmap.org/ A very important document. Let's walk through this one "goal" at a time. We'll start with fast slots and fast finality. I expect that we'll reduce slot time in an incremental fashion, eg. I like the "sqrt(2) at a time" formula (12 -> 8 -> 6 -> 4 -> 3 -> 2, though the last two steps are more speculative and depend on heavy research). It is possible to go faster or slower here; but the high level is that we'll view the slot time as a parameter that we adjust down when we're confident it's safe to, similar to the blob target. Fast slots are off in their own lane at the top of the roadmap, and do not really seem to connect to anything. This is because the rest of the roadmap is pretty independent of the slot time: we would need to do roughly the same things whether the slot time is 2 seconds or 32 seconds There are a few intersection areas though. One is p2p improvements. @raulvk has recently been working on an optimized p2p layer for Ethereum, which uses erasure coding to greatly improve on the bandwidth/latency tradeoff frontier. Roughly speaking: in today's design, each node receives a full block body from several peers, and is able to accept and rebroadcast it as soon as it receives the first one. If the "width" (number of peers sending you the block) is low, then one bad peer can greatly delay when you receive the block. If width is high, there is a lot of unneeded data overhead. With erasure coding, you can choose a k-of-n setup, eg: split each block into 8 pieces so that with any 4 of them you can reconstruct the full block. This gives you much of the redundancy benefits of high width, without the overhead. We have stats that show that this architecture can greatly reduce 95th percentile block propagation time, making shorter slots viable with no security tradeoffs (except increased protocol complexity, though here the performance-gain-to-lines-of-code ratio is quite favorable) Another intersection area is the more complex slot structure that comes with ePBS, FOCIL, and the fast confirmation rule. These have important benefits, but they decrease the safe latency maximum from slot/3 to slot/5. There's ongoing research to try to pipeline things better to minimize losses (also note: the slot time is lower-bounded not just by slot latency, but also by the fixed-cost part of ZK prover latency), but there are some tradeoffs here. One way we are exploring to compensate for this is to change to an architecture where only ~256-1024 randomly selected attesters sign on each slot. For a fork choice (non-finalizing) function, this is totally sufficient. The smaller number of signatures lets us remove the aggregation phase, shortening the slots. Fast finality is more complex (the ultimate protocol is IMO simpler than status quo Gasper, but the change path is complex). Today, finality takes 16 minutes (12s slots * 32 slot epochs * 2.5 epochs) on average. The goal is to decouple slots and finality, so allow us to reason about both separately, and we are aiming to use a one-round-finality BFT algorithm (a Minimmit variant) to finalize. So endgame finality time might be eg. 6-16 sec. Because this is a very invasive set of changes, the plan is to bundle the largest step in each change with a switch of the cryptography, notably to post-quantum hash-based signatures, and to a maximally STARK-friendly hash (there are three possible responses to the recent Poseidon2 attacks: (i) increase round count or introduce other countermeasures such as a Monolith layer, (ii) go back to Poseidon1, which is even more lindy than Poseidon2 and has not seen flaws, (iii) use BLAKE3 or other maximally-cheap "conventional" hash. All are being researched). Additionally, there is a plan to introduce many of these changes piece-by-piece, eg. "1-epoch finality" means we adjust the current consensus to change from FFG-style finalization to Minimmit-style finalization. One possible finality time trajectory is: 16 min (today) -> 10m40s (8s slots) -> 6m24s (one-epoch finality) -> 1m12s (8-slot epochs, 6s slots) -> 48s (4s slots) -> 16s (minimmit) -> 8s (minimmit with more aggressive parameters) One interesting consequence of the incremental approach is that there is a pathway to making the slots quantum-resistant much sooner than making the finality quantum-resistant, so we may well quite quickly get to a regime where, if quantum computers suddenly appear, we lose the finality guarantee, but the chain keeps chugging along. Summary: expect to see progressive decreases of both slot time and finality time, and expect to see these changes to be intertwined with a "ship of Theseus" style component-by-component replacement of Ethereum's slot structure and consensus with a cleaner, simpler, quantum-resistant, prover-friendly, end-to-end formally-verified alternative.

1h ago

---

**[Ethereum Foundation publishes “Strawmap” roadmap through 2029 (fast finality, zk L1, native privacy)](https://www.reddit.com/r/ethereum/comments/1req8s0/ethereum_foundation_publishes_strawmap_roadmap/)**

The Ethereum Foundation has published a draft long-term roadmap called “Strawmap,” outlining how the protocol could evolve across multiple forks through the rest of the decade. It organizes Ethereum’s end-state around five core goals: fast L1 (seconds-level finality) gigagas L1 (~10k TPS via zk execution proofs) teragas L2 (massive rollup DA bandwidth) post-quantum L1 native privacy (shielded ETH transfers) Strawmap is described as a coordination tool rather than a fixed plan, mapping one possible path for Ethereum’s base layer architecture over time. Overall it reads like Ethereum’s intended equilibrium design: zk-verified execution + rollup scaling + fast finality + built-in privacy. Full breakdown: https://btcusa.com/ethereum-foundation-publishes-strawmap-roadmap-with-fast-finality-zkevm-scaling-and-native-privacy-goals/ Which part of Strawmap do you see as the biggest shift for Ethereum long-term — zk L1, native privacy, or fast finality?

2h ago

---

**[Daily General Discussion February 25, 2026](https://www.reddit.com/r/ethereum/comments/1re561b/daily_general_discussion_february_25_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

17h ago

---

**[Meta To Begin Stablecoin Integration in 2026 on Ethereum](https://www.reddit.com/r/ethereum/comments/1rduvgk/meta_to_begin_stablecoin_integration_in_2026_on/)**

Meta is reportedly preparing stablecoin payments for Facebook, Instagram, and WhatsApp in H2 2026, a move that could put Ethereum rails behind everyday transfers.

🔗 [Daily Crypto Briefs](https://dailycryptobriefs.com/news/meta-stablecoin-integration-ethereum-h2-2026/) • 1d ago

---

**[Ethereum Foundation begins staking treasury ETH (~70,000 ETH planned)](https://www.reddit.com/r/ethereum/comments/1rdlbr4/ethereum_foundation_begins_staking_treasury_eth/)**

The Ethereum Foundation has started staking a portion of its ETH treasury, with an initial 2,016 ETH deposit and plans to allocate around 70,000 ETH over time. Staking rewards will be directed back into the EF treasury to fund protocol R&D, ecosystem grants, and core operations. The setup uses distributed validator infrastructure (Dirk and Vouch) and minority clients across multiple jurisdictions to avoid single points of failure and support client diversity. This move effectively turns part of the EF treasury into productive staking capital rather than idle ETH. Some potential implications: slightly reduces liquid ETH supply reinforces ETH’s staking-yield model aligns EF funding with network security signals long-term commitment to PoS Full article: [https://btcusa.com/ethereum-foundation-begins-staking-treasury-eth-allocating-70000-eth-to-validators/]() What do you think — should large ecosystem treasuries be staking by default?

1d ago

---

**[The Ethereum Foundation's commitment to DeFi](https://www.reddit.com/r/ethereum/comments/1rdpqsy/the_ethereum_foundations_commitment_to_defi/)**

Supporting the builders shaping decentralized finance and strengthening Ethereum as the global financial settlement layer

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/02/23/commitment-to-defi) • 1d ago

---

**[Why I like private property more than I did a few years ago.](https://www.reddit.com/r/ethereum/comments/1rdppmr/why_i_like_private_property_more_than_i_did_a_few/)**

One variable that changed for me is "stable era mindset vs chaotic era mindset". When you're in a "stable era", you see how private property is suboptimal, how economics can easily churn out 10+ categories of situations where it's obvious that certain taxes, incentives to make things available at better prices, etc can produce first-order gains with only second-order deadweight losses (which means that at low levels, the gains greatly exceed the losses). "Pure" private property is only "optimal" under spherical-cow economic assumptions like perfect competition. But in a "chaotic era", private property is more about schelling points - it's about creating a bulwark that's easy for people to understand and rally around defending, that says "your attempt to intervene in my life from the outside ends here". In the chaotic era, infringements on personal space are less likely to be well-meaning bureaucrats who overreach because they have not read enough Hayek, and more likely to be coming from a place of outright indifference or even hostility to your well-being. And looking at modern politics, yeah, there's a lot of that now. Since a lot of "Vitalik hates private property" sentiment comes from me liking Harberger taxes, I'll address that topic directly. My biggest update since the original 2016-19 era ideas was that, when designing details of Harberger taxes, the best motivating example to organize thought around is not "your house", rather it's "corporate intellectual property and walled gardens". If we think about the underlying complaints that people have about powerful corporations, the walled gardens and various ways in which centralized power accumulates on itself is top 5 on the list. What would it look like to build a "Harberger tax" that would tax eg. social platforms, Apple, etc more if they acted as walled gardens, and less if they enabled interoperability (and zero if they were fully open-source and interoperable and forkable)? There is a lot of energy right now around wanting to tax very wealthy individuals and corporations more, and I wonder: what if the best way to do that is not to tax wealth or unrealized gains (which has large downsides), but instead to tax enclosure? This way you raise revenue in a way that actually increases efficiency (any losses from people working less hard are more-than-compensated by gains from people shifting their work into formats where it's easier for people to build on top of each other and markets becoming more competitive). Any tax is an infringement on private property. But if you think about "tax on social platform that's proportional to some metric of how walled-garden-y they are", in an intuitive human sense, it really doesn't feel like "bureaucrats intervening in my life". It feels like "keeping concentrations of power from getting too out of hand". So I am in favor of doing things like that, and much less than before in favor of anything that forces people (incl entrepreneurs) to outright sell their assets, as eg. "Harberger tax on everything" does. A world where startup entrepreneurs are forced to constantly sell shares, realistically to the same few large VCs, in order to pay unrealized-gains or wealth tax bills strikes me as a world that's likely to be more soulless and homogeneous than today. But a world where the top 50% of large companies ranked by walled-garden-ness are taxed more (and the bottom 25% by that metric taxed less, perhaps some even zero), is a world that feels more dynamic and open and free. But even the above is somewhat of a "stable era" perspective, because it tries to make a more-perfect solution from the perspective of the political layer being friendly. We live in a chaotic era, and the point of crypto should be to solve important problems from the bottom up (whether "individualistic bottom up", enabling people to resist and escape various shackles, or "collective bottom up", communities organizing around shifting entire equilibria to their benefit) This ties into what I mean by wanting Ethereum to protect financial self-sovereignty. I do not think that Ethereum has much to offer to the trillion-dollar companies whose goal it is to offer products and services in a way that maximizes walled gardens and enclosure - in fact, much the opposite, censorship resistance can serve as the baseline for rebel communities that play the adversarial game of routing around those walled gardens. I do think Ethereum offers stronger security to people who want to maintain security of (including ability to use) their own financial resources, including surviving through great economic and political turmoil, for their personal or economic needs. And Ethereum offers a base layer for communities to organize large sudden collective shifts away from harmful equilibria into better ones; DAOs should try to solve that problem more.

1d ago

---

**[Daily General Discussion February 24, 2026](https://www.reddit.com/r/ethereum/comments/1rd88ab/daily_general_discussion_february_24_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Best way to restake rETH?](https://www.reddit.com/r/ethereum/comments/1rd5lq8/best_way_to_restake_reth/)**

1d ago

---

**[Daily General Discussion February 23, 2026](https://www.reddit.com/r/ethereum/comments/1rc9j78/daily_general_discussion_february_23_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Ethereum news: Vitalik Buterin sold 17,000 ETH this month as ether fell 37%](https://www.coindesk.com/markets/2026/02/25/vitalik-buterin-sold-17-000-eth-this-month-as-ether-fell-37)**

The Ethereum co-founder's tracked wallets dropped from 241,000 ETH to 224,000 ETH in February, with sales routed through CoW Protocol in small batches to limit market impact.

CoinDesk • 16h ago

---

**[Bitcoin, Ethereum and XRP Extend Losses. Why the AI Scare Is Weighing on Cryptos.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-prices-cryptos-ai-430073dc?gaa_at=eafs&gaa_n=AWEtsqepQv1I272DpopcvU1MH0l3L7mQep6MMxRkdHeDC-_3E9DKnGnEQZhU&gaa_ts=699f8f83&gaa_sig=lW26gB4S9D_Pv_vCnH4iSZmzIn3rBq300Hj1eSmJIo8-U9ZCnaNwyU4HnXHokhPOk6vsR6sHHXi4GomDpscVqQ%3D%3D)**

Barron's • 1d ago

---

**[Bitcoin, Ethereum and Solana Shorts Get Rekt as BTC Price Rebounds Near $69K](https://decrypt.co/359129/bitcoin-ethereum-solana-shorts-get-rekt-btc-price-rebounds-69k)**

More than $400 million worth of short positions have been liquidated in the last day as Bitcoin nears $69K and Ethereum and Solana surge.

Decrypt • 5h ago

---

**[Bitcoin, Ethereum Rally as Terra Lawsuit Targets Jane Street](https://coindcx.com/blog/crypto-news-global/bitcoin-ethereum-rally-as-terra-lawsuit-targets-jane-street/)**

CoinDCX • 12h ago

---

**[How to buy ethereum](https://finance.yahoo.com/personal-finance/investing/article/how-to-buy-ethereum-221336966.html)**

Ethereum is becoming a staple in modern digital portfolios. Learn how to choose your investment strategy, pick the right platform, execute the trade, and more.

Yahoo Finance • 1h ago

---

**[Bitcoin, Ethereum and Solana rally as analysts flag pause in ‘10 a.m. dump’ after Jane Street lawsuit](https://www.theblock.co/post/391353/bitcoin-ethereum-solana-rally-analysts-flag-pause-dump-jane-street-lawsuit)**

The rally marks one of the strongest single-day rebounds in weeks, snapping a steady slide that had pushed bitcoin down sharply from its October highs.

The Block • 1h ago

---

**[Is Ethereum good enough for Wall Street? If history is any guide, the answer is clear](https://fortune.com/crypto/2026/02/23/ethereum-wall-street-canton-r3-zksync-ethdenver/)**

A consortium of banks is building its own version of blockchain—it will be hard pressed to make it work.

Fortune • 2d ago

---

**[Better Buy: Bitcoin vs. Ethereum](https://www.fool.com/investing/2026/02/24/better-buy-bitcoin-vs-ethereum/)**

Could Ethereum really outperform Bitcoin this year? Harvard seems to think so.

The Motley Fool • 1d ago

---

**[Ethereum Is Growing. So Why Is The ETH Price Collapsing?](https://www.forbes.com/sites/greatspeculations/2026/02/24/ethereum-is-growing-so-why-is-the-eth-price-collapsing/)**

Forbes • 1d ago

---

**[How Strong Will Ethereum Be in 2026](https://www.disruptionbanking.com/2026/02/25/how-strong-will-ethereum-be-in-2026/)**

Ethereum, the world’s second-largest blockchain by market cap, remains the leading platform for smart contracts and DeFi. Its daily transactions are above Ethereum in 2026: Explore network strength, staking yields, Glamsterdam upgrades, ETF inflows, and price forecasts from $4,000 to $5,000+. Will ETH reclaim highs amid volatility?

Disruption Banking • 14h ago

---

---

## YouTube Videos: "ethereum"

**[EXPLOSIVE Ethereum News We Might Have The Craziest Altcoin Season The Crypto Space Has Ever Seen](https://www.youtube.com/watch?v=9JyyG4lipGU)**

I mean... they told us this would happen, so theres no use for any of us being surprised when it actually takes place.

📺 Money Rules - Investing Tips 

👁️ 10K • 👍 1K • 💬 115 • ⏱️ 28:35 • 12h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=vBDrZnXnZLs)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 178 • 💬 10 • ⏱️ 6:58 • 12h ago

---

**[Why Ethereum Isn&#39;t Bitcoin&#39;s Little Brother: Sharplink CEO](https://www.youtube.com/watch?v=pvG3sBnPjZE)**

Ethereum has long been compared to Bitcoin — but according to Sharplink CEO and former BlackRock digital assets leader ...

📺 Coinage

👁️ 4K • 👍 135 • 💬 21 • ⏱️ 21:21 • 11h ago

---

**[🚨IMPORTANT Ethereum $1,800 Support BOUNCE! Can It Hold?](https://www.youtube.com/watch?v=U62slGX_PaQ)**

IMPORTANT Ethereum $1800 Support BOUNCE! Can It Hold? Ethereum just bounced hard off the critical $1800 support ...

📺 Tim Warren

👁️ 3K • 👍 311 • 💬 104 • ⏱️ 13:04 • 1d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=yacmf0otMwA)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 161 • 💬 8 • ⏱️ 3:50 • 5h ago

---

**[BITCOIN &amp; ALTCOIN PUMP: Next Targets Revealed!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=K_-724Tw-sc)**

BITCOIN & ALTCOIN PUMP: Next Targets Revealed!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 2K • 👍 137 • 💬 20 • ⏱️ 20:49 • 1h ago

---

**[BITCOIN &amp; CRYPTO REPEATING HISTORY (Signal Confirmed)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=B51zxN9TVdE)**

BITCOIN & CRYPTO REPEATING HISTORY (Signal Confirmed)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 11K • 👍 345 • 💬 76 • ⏱️ 16:59 • 1d ago

---

**[☢️ It&#39;s Over For Ethereum...](https://www.youtube.com/watch?v=Bz26yGwwFpM)**

Watch the full episode: https://youtu.be/xgJOC10lUWQ Join Premium: https://the-bitcoin-strategy.com My Chart Software: ...

📺 Gerhard - Bitcoin Strategy

👁️ 5K • 👍 150 • 💬 52 • ⏱️ 14:34 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=XTbfzXSdp2g)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 171 • 💬 4 • ⏱️ 6:09 • 1d ago

---

**[BITCOIN CRASH EXPLAINED (This Could Get UGLY)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=hkInfemKTV4)**

BITCOIN CRASH EXPLAINED (This Could Get UGLY)!!! - Bitcoin News Today, Ethereum & Altcoins *Bitunix* ...

📺 Crypto World

👁️ 11K • 👍 322 • 💬 106 • ⏱️ 22:08 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
