---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-03T17:29:18.027408+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- videos
- cryptocurrency
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 03, 2026 at 17:29 UTC  
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

### $2,249.66

---

## Ethereum Chart

**24h:** -5.0%  
**7d:** -26.0%  
**30d:** -30.9%  
**90d:** -32.8%  
**1y:** -18.6%  

---

## Ethereum Market Stats

**Market Cap:** $269.21B
Rank #2

**Circulating Supply:** 120,693,657 ETH
No max supply

**All-Time High:** $4,946.05
-55.0%

**All-Time Low:** $0.43
+514118.9%

---

## Reddit: r/ethereum

**[On L2s and Ethereum](https://www.reddit.com/r/ethereum/comments/1quv8if/on_l2s_and_ethereum/)**

There have recently been some discussions on the ongoing role of L2s in the Ethereum ecosystem, especially in the face of two facts: L2s' progress to stage 2 (and, secondarily, on interop) has been far slower and more difficult than originally expected L1 itself is scaling, fees are very low, and gaslimits are projected to increase greatly in 2026 Both of these facts, for their own separate reasons, mean that the original vision of L2s and their role in Ethereum no longer makes sense, and we need a new path. First, let us recap the original vision. Ethereum needs to scale. The definition of "Ethereum scaling" is the existence of large quantities of block space that is backed by the full faith and credit of Ethereum - that is, block space where, if you do things (including with ETH) inside that block space, your activities are guaranteed to be valid, uncensored, unreverted, untouched, as long as Ethereum itself functions. If you create a 10000 TPS EVM where its connection to L1 is mediated by a multisig bridge, then you are not scaling Ethereum. This vision no longer makes sense. L1 does not need L2s to be "branded shards", because L1 is itself scaling. And L2s are not able or willing to satisfy the properties that a true "branded shard" would require. I've even seen at least one explicitly saying that they may never want to go beyond stage 1, not just for technical reasons around ZK-EVM safety, but also because their customers' regulatory needs require them to have ultimate control. This may be doing the right thing for your customers. But it should be obvious that if you are doing this, then you are not "scaling Ethereum" in the sense meant by the rollup-centric roadmap. But that's fine! it's fine because Ethereum itself is now scaling directly on L1, with large planned increases to its gas limit this year and the years ahead. We should stop thinking about L2s as literally being "branded shards" of Ethereum, with the social status and responsibilities that this entails. Instead, we can think of L2s as being a full spectrum, which includes both chains backed by the full faith and credit of Ethereum with various unique properties (eg. not just EVM), as well as a whole array of options at different levels of connection to Ethereum, that each person (or bot) is free to care about or not care about depending on their needs. What would I do today if I were an L2? Identify a value add other than "scaling". Examples: (i) non-EVM specialized features/VMs around privacy, (ii) efficiency specialized around a particular application, (iii) truly extreme levels of scaling that even a greatly expanded L1 will not do, (iv) a totally different design for non-financial applications, eg. social, identity, AI, (v) ultra-low-latency and other sequencing properties, (vi) maybe built-in oracles or decentralized dispute resolution or other "non-computationally-verifiable" features Be stage 1 at the minimum (otherwise you really are just a separate L1 with a bridge, and you should just call yourself that) if you're doing things with ETH or other ethereum-issued assets Support maximum interoperability with Ethereum, though this will differ for each one (eg. what if you're not EVM, or even not financial?) From Ethereum's side, over the past few months I've become more convinced of the value of the native rollup precompile, particuarly once we have enshrined ZK-EVM proofs that we need anyway to scale L1. This is a precompile that verifies a ZK-EVM proof, and it's "part of Ethereum", so (i) it auto-upgrades along with Ethereum, and (ii) if the precompile has a bug, Ethereum will hard-fork to fix the bug. The native rollup precompile would make full, security-council-free, EVM verification accessible. We should spend much more time working out how to design it in such a way that if your L2 is "EVM plus other stuff", then the native rollup precompile would verify the EVM, and you only have to bring your own prover for the "other stuff" (eg. Stylus). This might involve a canonical way of exposing a lookup table between contract call inputs and outputs, and letting you provide your own values to the lookup table (that you would prove separately). This would make it easy to have safe, strong, trustless interoperability with Ethereum. It also enables synchronous composability (see: https://ethresear.ch/t/combining-preconfirmations-with-based-rollups-for-synchronous-composability/23863 and https://ethresear.ch/t/synchronous-composability-between-rollups-via-realtime-proving/23998 ). And from there, it's each L2's choice exactly what they want to build. Don't just "extend L1", figure out something new to add. This of course means that some will add things that are trust-dependent, or backdoored, or otherwise insecure; this is unavoidable in a permissionless ecosystem where developers have freedom. Our job should make to make it clear to users what guarantees they have, and to build up the strongest Ethereum that we can.

1h ago

---

**[Daily General Discussion February 03, 2026](https://www.reddit.com/r/ethereum/comments/1quk1p6/daily_general_discussion_february_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

11h ago

---

**[In 2016, Ethereum faced "code is law" vs "fix the damage." Ten years later, I'm watching the same debate play out in a GitHub repo.](https://www.reddit.com/r/ethereum/comments/1qu6ahw/in_2016_ethereum_faced_code_is_law_vs_fix_the/)**

In June 2016, someone drained ~$60M from The DAO - a decentralized investment fund built on Ethereum. They didn't hack Ethereum itself. They exploited a recursive calling bug in the smart contract's own logic. The code allowed it. That's what made it a crisis. If "code is law," the attacker didn't do anything wrong. The contract ran as written. But $60M was gone and real people lost real money. Ethereum had to choose: reverse the blockchain to return the funds, or let it stand because the code permitted it. The community voted to hard fork - rewrite history and undo the damage. The people who refused to accept that kept running the original chain. That's how Ethereum Classic was born. The question at the center of it all: when your system is broken and the fix is known, do you break the rules to fix it, or do you let the rules play out even while the system burns? I'm watching a tiny version of this happen right now. I run OpenChaos - a GitHub repo where anyone submits a PR, the community votes with reactions, and the most-voted PR merges daily. No gatekeeping. Pure popular vote. 911 stars, 70+ open PRs, five weeks in. Last Friday, PR #62: "1.337% chance to see nothing" won the daily vote and merged. Three lines of code: if (Math.random() <= 0.01337) { return null; } A leet joke. 1.337% of the time, a visitor sees a blank page. Funny, harmless, right? The site caches server-side. When the page returns null, the cache treats the blank page as permanent. One unlucky render broke the site for every visitor, indefinitely. Not a 5-minute blip. A permanent outage from a 1.337% roll. A contributor diagnosed the root cause and submitted PR #173 - a clean fix, CI passes, no conflicts. But PR #173 has fewer votes than a DOOM port and a Rickroll. The fix has to wait its turn in the democratic queue. The site stays broken while the community votes on entertainment over infrastructure. One community member commented: "I am torn between fixing things quickly and letting the rules play out to see when the fix comes naturally. I want to see the naturally emergent behaviour." Sound familiar? Then it got more interesting. The contributor who wrote the fix also had another PR in the queue that was about to merge. He could have bundled the bugfix into that PR and shipped it quietly. He refused: "I considered adding this fix to #129, but it doesn't feel like it's in the spirit of the project. Even if it's a 'good' trojan horse, it's still a trojan horse." But another contributor made the opposite choice. The author of the DOOM port deliberately bundled the bugfix into their submission. If it merges tomorrow, the site comes back online - not through governance, but through the exact Trojan horse tactic the first contributor refused on principle. Two contributors. Same option. Opposite choices. Obviously nobody's losing $60M here. But the structure is the same: A system running as designed produces an unintended outcome The fix is known and ready The rules don't allow a fast path to deploy it The community has to decide: break the process or trust the process I opened Issue #176 proposing that only contributors with merged PRs should be allowed to vote - earned governance instead of open popularity contests. The debate is live. Questions I keep thinking about: Is there a middle ground between "code is law, let it burn" and "maintainer override"? Something that keeps democratic legitimacy while allowing fast response to emergencies? For those who lived through the DAO debate - looking back, what would you tell a small project facing its first "do we fork our own rules" moment? The repo: github.com/skridlevsky/openchaos The governance discussion: Issue #176 The broken site (may or may not be blank when you visit): openchaos.dev

21h ago

---

**[Paid DJ open call: perform at Decentraland’s 6th Birthday (Feb 20, $400 USD in MANA)](https://www.reddit.com/r/ethereum/comments/1qus8jw/paid_dj_open_call_perform_at_decentralands_6th/)**

Sharing a paid performance opportunity that might be relevant for artists here. Decentraland is running an open call for community DJs / performers to play a pre-recorded set during its 6th Birthday Party in the Theatre on February 20 at 8pm UTC. Key details: Pre-recorded DJ sets only (45–55 minutes) $400 USD paid in MANA per selected performer In-world audience gathered for the birthday event Intended for artists already familiar with Decentraland (not livestreams) This isn’t a pitch about crypto or Web3, it’s a straightforward paid performance slot inside an existing virtual world event. Full details and application here: https://zealous.co/decentraland/opportunity/decentraland-6th-birthday-party/

3h ago

---

**[Effect-TS library for EVM frontends](https://www.reddit.com/r/ethereum/comments/1quxszt/effectts_library_for_evm_frontends/)**

16m ago

---

**[Advice/tips/resources on finding a CTO (growth stage company)](https://www.reddit.com/r/ethereum/comments/1quqccs/advicetipsresources_on_finding_a_cto_growth_stage/)**

5h ago

---

**[How a premature software standard has led to billions in losses](https://www.reddit.com/r/ethereum/comments/1qtw9fe/how_a_premature_software_standard_has_led_to/)**

🔗 [hugo0.com](https://hugo0.com/blog/how-erc20-held-back-blockchain-payments-a-decade) • 1d ago

---

**[Daily General Discussion February 02, 2026](https://www.reddit.com/r/ethereum/comments/1qtn0fr/daily_general_discussion_february_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[a whitepaper on a yield-focused dao](https://www.reddit.com/r/ethereum/comments/1qubsh4/a_whitepaper_on_a_yieldfocused_dao/)**

i’ve been working on a yield/token architecture that tries to be very explicit about separation of concerns, and i’m mostly looking for feedback from people who are already uncomfortable with how tightly coupled most defi tokens are today. the basic premise is simple: the token contract should not know or care about yield. no rebases, no transfer hooks, no strategy logic bleeding into balance accounting. instead, all yield is routed through a single on-chain component that handles normalization, accounting, and distribution according to policy. i ended up implementing this as a modular system with a canonical “revenue router”: the base token is just erc20 + voting, nothing else all yield sources plug into a router instead of the token yield gets normalized into a treasury asset before distribution distribution is policy-driven (buybacks, staking, hybrid), not hardcoded yield sources are plugins with tiered trust and execution limits failure isn’t implicit: plugins can be quarantined without nuking the system the goal isn’t yield maximization per se, but predictable value accrual with reduced blast radius. plugins can be permissionless, but they don’t all get the same authority. everything that touches value has explicit constraints. accounting is deterministic. no component can “surprise” the token. i wrote all of this up as a whitepaper (vastitas) and tried to be very concrete about invariants, routing rules, quarantine mechanics, and trade-offs, including some simulated comparisons against monolithic tokens and yield aggregators i’m not trying to sell this as obviously correct. i’m more interested in whether this direction resonates with people who think long-term token sustainability is more about architecture than clever incentives. i made a faulty deployment on arbitrum and a half working one on base. nothing is finalized. i’m mainly looking to pressure-test the ideas with people who agree that this might be a good project. feel free to poke holes, challenge assumptions, or point me to similar work i might have missed.

17h ago

---

**[Staking](https://www.reddit.com/r/ethereum/comments/1qu0vj0/staking/)**

Should I be staking 100% of my Ethereum? Can someone explain to me like im 5 what this means? Apologies if this type of post is not allowed, moderators.

1d ago

---

---

## Google News: "ethereum"

**[Tom Lee's BitMine Buys the Ethereum Dip, Even as Unrealized Losses Top $6 Billion](https://finance.yahoo.com/news/tom-lees-bitmine-buys-ethereum-162425009.html)**

Publicly traded Ethereum treasury BitMine Immersion Technologies is still buying as ETH plunges, despite the firm's growing losses.

Yahoo Finance • 1d ago

---

**[Bitcoin, Ethereum ETF Investments Flip Negative for 2026 as Crypto Funds Shed $1.7B](https://decrypt.co/356622/bitcoin-ethereum-etf-investments-flip-negative-for-2026-as-crypto-funds-shed-1-7b)**

U.S.-listed crypto funds led withdrawals as Bitcoin and Ethereum prices slid after Donald Trump’s nomination of Kevin Warsh for Fed chair.

Decrypt • 1d ago

---

**['You are not scaling Ethereum': Vitalik Buterin issues a blunt reality check to the biggest crypto networks](https://www.coindesk.com/business/2026/02/03/you-are-not-scaling-ethereum-vitalik-buterin-issues-a-blunt-reality-check-to-the-biggest-crypto-networks)**

The roadmap in place doesn't make as much sense because progress among layer-2s toward later stages of decentralization has been slower and more difficult, and Ethereum itself is now scaling directly on layer-1.

CoinDesk • 7m ago

---

**[3 Things Investors Need to Know About Ethereum Classic in 2026](https://www.fool.com/investing/2026/02/03/3-things-investors-need-to-know-about-ethereum-cla/)**

Ethereum and Ethereum Classic started as one blockchain, but their paths and performance have diverged over the past decade.

The Motley Fool • 3h ago

---

**[ING opens retail access to Bitcoin, Ethereum, Solana ETPs in Germany](https://www.theblock.co/post/388120/ing-bitcoin-ethereum-solana-etps)**

Still, ING Deutschland noted that crypto ETPs carry significant risks and stated that crypto has no intrinsic value.

The Block • 12h ago

---

**[Ethereum Price $2,200 Collapse Raises Risk Of A Sub-$2K Spike](https://www.tradingview.com/news/newsbtc:7ac8323ae094b:0-ethereum-price-2-200-collapse-raises-risk-of-a-sub-2k-spike/)**

Ethereum price started a major decline after it failed to clear $2,500. ETH is down 20% and is now struggling to stay above the $2,200 support.Ethereum Price Dips 20%Ethereum price failed to remain stable above $2,550 and started a major decline, like Bitcoin. ETH price traded below $2,400 to enter…

TradingView • 1d ago

---

**[Ethereum Falls 10% In Selloff](https://www.investing.com/news/cryptocurrency-news/ethereum-falls-10-in-selloff-4477658)**

Ethereum Falls 10% In Selloff

Investing.com • 2d ago

---

**[A sudden shift in Ethereum staking is draining billions from exchanges toward a new corporate elite](https://cryptoslate.com/how-staking-turned-ethereum-into-a-treasury-trade/)**

Corporate Ethereum treasuries use staking to earn additional ETH, turning reserves into a compounding strategy instead of passive exposure.

CryptoSlate • 1d ago

---

**[Crypto Crash: Liquidations Top $2.5 Billion as Bitcoin, Ethereum and XRP Prices Plummet](https://decrypt.co/356557/crypto-crash-liquidations-2-5-billion-bitcoin-ethereum-xrp-plummet)**

The crypto market's recent decline only accelerated Saturday, with Bitcoin falling to nearly $77,000 as liquidations piled up.

Decrypt • 2d ago

---

**[Why are Bitcoin, Ethereum and XRP Prices Crashing Today?](https://www.tradingview.com/news/coinpedia:b99ef7f8a094b:0-why-are-bitcoin-ethereum-and-xrp-prices-crashing-today/)**

The crypto market is facing a major sell-off today, with total market value dropping to $2.66 trillion, down more than 6% in the last 24 hours. Bitcoin, Ethereum, XRP and other major cryptocurrencies have all fallen sharply, wiping out nearly $500 billion from the market in just a few days.The bigg…

TradingView • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum’s Vision Is Incredibly Bullish… So Why Is the Price So Bad? w/ Jeff Park](https://www.youtube.com/watch?v=tJLZausdujc)**

Free Milk Road Newsletters: ...

📺 Milk Road

👁️ 15K • 👍 364 • 💬 33 • ⏱️ 15:51 • 2d ago

---

**[BITCOIN AND ETH: BULLS HAVE A CHANCE HERE!!! 🚨🚨🚨 (ISM)](https://www.youtube.com/watch?v=pdpUrzqUSZ0)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 19K • 👍 1K • 💬 91 • ⏱️ 59:39 • 7h ago

---

**[Tom Lee Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=OpRy3WJO7mA)**

Tom Lee Just Said The UNTHINKABLE About Bitcoin & Ethereum! ["It's a Fake Crash"] My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 11K • 👍 414 • 💬 115 • ⏱️ 18:04 • 1d ago

---

**[Shorting Ethereum: My Life-Changing Trade](https://www.youtube.com/watch?v=L9tejtx7sXA)**

After getting chopped up in ETH shorts over the past few months, I found a moment of Tom Lee weakness to short ETH one last ...

📺 Taiki Maeda

👁️ 15K • 👍 771 • 💬 215 • ⏱️ 48:54 • 1d ago

---

**[BITCOIN AND ETH: LAST CHANCE TO RECOVER!!!! 🚨🚨🚨 (MicroStrategy REKT)](https://www.youtube.com/watch?v=bLiHfECZH3k)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 28K • 👍 2K • 💬 213 • ⏱️ 46:08 • 1d ago

---

**[BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=ObRvo0J4ygM)**

BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 10K • 👍 366 • 💬 500 • ⏱️ 23:54 • 19h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=zCCN5NIzpqk)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 180 • 💬 29 • ⏱️ 5:14 • 18h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=DUSA5M4i43M)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 4K • 👍 256 • 💬 19 • ⏱️ 5:18 • 1d ago

---

**[Bitcoin, Ethereum &amp; Altcoins DOWN BAD (NOW THIS!?)](https://www.youtube.com/watch?v=CxKURlwrfIM)**

In today's video, we're breaking down why the pain for Bitcoin (BTC), Ethereum (ETH), and the broader Altcoin market might not ...

📺 Discover Crypto

👁️ 9K • 👍 477 • 💬 167 • ⏱️ 1:43:46 • 1d ago

---

**[Tom Lee Drops HUGE Warning About 2026 | The Bull Run Has CHANGED](https://www.youtube.com/watch?v=3dh-JR2mdzA)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 7K • 👍 165 • 💬 201 • ⏱️ 15:18 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
