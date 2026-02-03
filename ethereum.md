---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-03T23:54:24.407987+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- cryptocurrency
- news
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 03, 2026 at 23:54 UTC  
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

### $2,231.02

---

## Ethereum Chart

**24h:** -5.2%  
**7d:** -26.0%  
**30d:** -30.9%  
**90d:** -32.8%  
**1y:** -18.6%  

---

## Ethereum Market Stats

**Market Cap:** $272.79B
Rank #2

**Circulating Supply:** 120,693,657 ETH
No max supply

**All-Time High:** $4,946.05
-54.3%

**All-Time Low:** $0.43
+522491.2%

---

## Reddit: r/ethereum

**[On L2s and Ethereum](https://www.reddit.com/r/ethereum/comments/1quv8if/on_l2s_and_ethereum/)**

There have recently been some discussions on the ongoing role of L2s in the Ethereum ecosystem, especially in the face of two facts: L2s' progress to stage 2 (and, secondarily, on interop) has been far slower and more difficult than originally expected L1 itself is scaling, fees are very low, and gaslimits are projected to increase greatly in 2026 Both of these facts, for their own separate reasons, mean that the original vision of L2s and their role in Ethereum no longer makes sense, and we need a new path. First, let us recap the original vision. Ethereum needs to scale. The definition of "Ethereum scaling" is the existence of large quantities of block space that is backed by the full faith and credit of Ethereum - that is, block space where, if you do things (including with ETH) inside that block space, your activities are guaranteed to be valid, uncensored, unreverted, untouched, as long as Ethereum itself functions. If you create a 10000 TPS EVM where its connection to L1 is mediated by a multisig bridge, then you are not scaling Ethereum. This vision no longer makes sense. L1 does not need L2s to be "branded shards", because L1 is itself scaling. And L2s are not able or willing to satisfy the properties that a true "branded shard" would require. I've even seen at least one explicitly saying that they may never want to go beyond stage 1, not just for technical reasons around ZK-EVM safety, but also because their customers' regulatory needs require them to have ultimate control. This may be doing the right thing for your customers. But it should be obvious that if you are doing this, then you are not "scaling Ethereum" in the sense meant by the rollup-centric roadmap. But that's fine! it's fine because Ethereum itself is now scaling directly on L1, with large planned increases to its gas limit this year and the years ahead. We should stop thinking about L2s as literally being "branded shards" of Ethereum, with the social status and responsibilities that this entails. Instead, we can think of L2s as being a full spectrum, which includes both chains backed by the full faith and credit of Ethereum with various unique properties (eg. not just EVM), as well as a whole array of options at different levels of connection to Ethereum, that each person (or bot) is free to care about or not care about depending on their needs. What would I do today if I were an L2? Identify a value add other than "scaling". Examples: (i) non-EVM specialized features/VMs around privacy, (ii) efficiency specialized around a particular application, (iii) truly extreme levels of scaling that even a greatly expanded L1 will not do, (iv) a totally different design for non-financial applications, eg. social, identity, AI, (v) ultra-low-latency and other sequencing properties, (vi) maybe built-in oracles or decentralized dispute resolution or other "non-computationally-verifiable" features Be stage 1 at the minimum (otherwise you really are just a separate L1 with a bridge, and you should just call yourself that) if you're doing things with ETH or other ethereum-issued assets Support maximum interoperability with Ethereum, though this will differ for each one (eg. what if you're not EVM, or even not financial?) From Ethereum's side, over the past few months I've become more convinced of the value of the native rollup precompile, particuarly once we have enshrined ZK-EVM proofs that we need anyway to scale L1. This is a precompile that verifies a ZK-EVM proof, and it's "part of Ethereum", so (i) it auto-upgrades along with Ethereum, and (ii) if the precompile has a bug, Ethereum will hard-fork to fix the bug. The native rollup precompile would make full, security-council-free, EVM verification accessible. We should spend much more time working out how to design it in such a way that if your L2 is "EVM plus other stuff", then the native rollup precompile would verify the EVM, and you only have to bring your own prover for the "other stuff" (eg. Stylus). This might involve a canonical way of exposing a lookup table between contract call inputs and outputs, and letting you provide your own values to the lookup table (that you would prove separately). This would make it easy to have safe, strong, trustless interoperability with Ethereum. It also enables synchronous composability (see: https://ethresear.ch/t/combining-preconfirmations-with-based-rollups-for-synchronous-composability/23863 and https://ethresear.ch/t/synchronous-composability-between-rollups-via-realtime-proving/23998 ). And from there, it's each L2's choice exactly what they want to build. Don't just "extend L1", figure out something new to add. This of course means that some will add things that are trust-dependent, or backdoored, or otherwise insecure; this is unavoidable in a permissionless ecosystem where developers have freedom. Our job should make to make it clear to users what guarantees they have, and to build up the strongest Ethereum that we can.

8h ago

---

**[Daily General Discussion February 03, 2026](https://www.reddit.com/r/ethereum/comments/1quk1p6/daily_general_discussion_february_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

17h ago

---

**[Effect-TS library for EVM frontends](https://www.reddit.com/r/ethereum/comments/1quxszt/effectts_library_for_evm_frontends/)**

6h ago

---

**[Paid DJ open call: perform at Decentraland’s 6th Birthday (Feb 20, $400 USD in MANA)](https://www.reddit.com/r/ethereum/comments/1qus8jw/paid_dj_open_call_perform_at_decentralands_6th/)**

Sharing a paid performance opportunity that might be relevant for artists here. Decentraland is running an open call for community DJs / performers to play a pre-recorded set during its 6th Birthday Party in the Theatre on February 20 at 8pm UTC. Key details: Pre-recorded DJ sets only (45–55 minutes) $400 USD paid in MANA per selected performer In-world audience gathered for the birthday event Intended for artists already familiar with Decentraland (not livestreams) This isn’t a pitch about crypto or Web3, it’s a straightforward paid performance slot inside an existing virtual world event. Full details and application here: https://zealous.co/decentraland/opportunity/decentraland-6th-birthday-party/

10h ago

---

**[ZK (Zero knowledge) proof for SHA-256: 312-byte proof, ~18µs verification](https://www.reddit.com/r/ethereum/comments/1qv2hzp/zk_zero_knowledge_proof_for_sha256_312byte_proof/)**

3h ago

---

**[In 2016, Ethereum faced "code is law" vs "fix the damage." Ten years later, I'm watching the same debate play out in a GitHub repo.](https://www.reddit.com/r/ethereum/comments/1qu6ahw/in_2016_ethereum_faced_code_is_law_vs_fix_the/)**

In June 2016, someone drained ~$60M from The DAO - a decentralized investment fund built on Ethereum. They didn't hack Ethereum itself. They exploited a recursive calling bug in the smart contract's own logic. The code allowed it. That's what made it a crisis. If "code is law," the attacker didn't do anything wrong. The contract ran as written. But $60M was gone and real people lost real money. Ethereum had to choose: reverse the blockchain to return the funds, or let it stand because the code permitted it. The community voted to hard fork - rewrite history and undo the damage. The people who refused to accept that kept running the original chain. That's how Ethereum Classic was born. The question at the center of it all: when your system is broken and the fix is known, do you break the rules to fix it, or do you let the rules play out even while the system burns? I'm watching a tiny version of this happen right now. I run OpenChaos - a GitHub repo where anyone submits a PR, the community votes with reactions, and the most-voted PR merges daily. No gatekeeping. Pure popular vote. 911 stars, 70+ open PRs, five weeks in. Last Friday, PR #62: "1.337% chance to see nothing" won the daily vote and merged. Three lines of code: if (Math.random() <= 0.01337) { return null; } A leet joke. 1.337% of the time, a visitor sees a blank page. Funny, harmless, right? The site caches server-side. When the page returns null, the cache treats the blank page as permanent. One unlucky render broke the site for every visitor, indefinitely. Not a 5-minute blip. A permanent outage from a 1.337% roll. A contributor diagnosed the root cause and submitted PR #173 - a clean fix, CI passes, no conflicts. But PR #173 has fewer votes than a DOOM port and a Rickroll. The fix has to wait its turn in the democratic queue. The site stays broken while the community votes on entertainment over infrastructure. One community member commented: "I am torn between fixing things quickly and letting the rules play out to see when the fix comes naturally. I want to see the naturally emergent behaviour." Sound familiar? Then it got more interesting. The contributor who wrote the fix also had another PR in the queue that was about to merge. He could have bundled the bugfix into that PR and shipped it quietly. He refused: "I considered adding this fix to #129, but it doesn't feel like it's in the spirit of the project. Even if it's a 'good' trojan horse, it's still a trojan horse." But another contributor made the opposite choice. The author of the DOOM port deliberately bundled the bugfix into their submission. If it merges tomorrow, the site comes back online - not through governance, but through the exact Trojan horse tactic the first contributor refused on principle. Two contributors. Same option. Opposite choices. Obviously nobody's losing $60M here. But the structure is the same: A system running as designed produces an unintended outcome The fix is known and ready The rules don't allow a fast path to deploy it The community has to decide: break the process or trust the process I opened Issue #176 proposing that only contributors with merged PRs should be allowed to vote - earned governance instead of open popularity contests. The debate is live. Questions I keep thinking about: Is there a middle ground between "code is law, let it burn" and "maintainer override"? Something that keeps democratic legitimacy while allowing fast response to emergencies? For those who lived through the DAO debate - looking back, what would you tell a small project facing its first "do we fork our own rules" moment? The repo: github.com/skridlevsky/openchaos The governance discussion: Issue #176 The broken site (may or may not be blank when you visit): openchaos.dev

1d ago

---

**[Advice/tips/resources on finding a CTO (growth stage company)](https://www.reddit.com/r/ethereum/comments/1quqccs/advicetipsresources_on_finding_a_cto_growth_stage/)**

11h ago

---

**[a whitepaper on a yield-focused dao](https://www.reddit.com/r/ethereum/comments/1qubsh4/a_whitepaper_on_a_yieldfocused_dao/)**

i’ve been working on a yield/token architecture that tries to be very explicit about separation of concerns, and i’m mostly looking for feedback from people who are already uncomfortable with how tightly coupled most defi tokens are today. the basic premise is simple: the token contract should not know or care about yield. no rebases, no transfer hooks, no strategy logic bleeding into balance accounting. instead, all yield is routed through a single on-chain component that handles normalization, accounting, and distribution according to policy. i ended up implementing this as a modular system with a canonical “revenue router”: the base token is just erc20 + voting, nothing else all yield sources plug into a router instead of the token yield gets normalized into a treasury asset before distribution distribution is policy-driven (buybacks, staking, hybrid), not hardcoded yield sources are plugins with tiered trust and execution limits failure isn’t implicit: plugins can be quarantined without nuking the system the goal isn’t yield maximization per se, but predictable value accrual with reduced blast radius. plugins can be permissionless, but they don’t all get the same authority. everything that touches value has explicit constraints. accounting is deterministic. no component can “surprise” the token. i wrote all of this up as a whitepaper (vastitas) and tried to be very concrete about invariants, routing rules, quarantine mechanics, and trade-offs, including some simulated comparisons against monolithic tokens and yield aggregators i’m not trying to sell this as obviously correct. i’m more interested in whether this direction resonates with people who think long-term token sustainability is more about architecture than clever incentives. i made a faulty deployment on arbitrum and a half working one on base. nothing is finalized. i’m mainly looking to pressure-test the ideas with people who agree that this might be a good project. feel free to poke holes, challenge assumptions, or point me to similar work i might have missed.

1d ago

---

**[How a premature software standard has led to billions in losses](https://www.reddit.com/r/ethereum/comments/1qtw9fe/how_a_premature_software_standard_has_led_to/)**

🔗 [hugo0.com](https://hugo0.com/blog/how-erc20-held-back-blockchain-payments-a-decade) • 1d ago

---

**[Daily General Discussion February 02, 2026](https://www.reddit.com/r/ethereum/comments/1qtn0fr/daily_general_discussion_february_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

---

## Google News: "ethereum"

**[Vitalik Buterin reevaluates Ethereum's rollup-centric roadmap, arguing L2s decentralized 'far slower' while base layer advanced](https://www.theblock.co/post/388285/vitalik-buterin-reevaluates-rollup-centric-roadmap-arguing-l2s-decentralized-far-slower-while-ethereum-base-layer-advanced)**

Buterin previously championed a "rollup-centric" roadmap that would scale Ethereum through a network of branded shards.

The Block • 7h ago

---

**['You are not scaling Ethereum': Vitalik Buterin issues a blunt reality check to the biggest crypto networks](https://www.coindesk.com/business/2026/02/03/you-are-not-scaling-ethereum-vitalik-buterin-issues-a-blunt-reality-check-to-the-biggest-crypto-networks)**

The roadmap in place doesn't make as much sense because progress among layer-2s toward later stages of decentralization has been slower and more difficult, and Ethereum itself is now scaling directly on layer-1.

CoinDesk • 6h ago

---

**[Vitalik Buterin Weighs In as Devs Add Frame Transactions to Ethereum’s Next Upgrade Debate](https://finance.yahoo.com/news/vitalik-buterin-weighs-devs-add-222346815.html)**

Ethereum core devs have put “Frame Transactions” on the shortlist of Hegota headliner candidates, with Vitalik Buterin publicly engaging in the proposal thread the next day and arguing that the design can inherit ERC-4337-style mempool acceptance rules via paymasters.ETH was trading at $2,304.7 (-0.6% 24h) across spot venues while the ...

Yahoo Finance • 1h ago

---

**[Bitcoin, Ethereum continue plunge — and experts warn of more pain to come](https://www.dlnews.com/articles/markets/bitcoin-and-ethereum-could-drop-further-experts-say/)**

Bitcoin and Ethereum plunged further on Tuesday.  The two biggest digital coins are now well below their all-time highs.  Experts have signalled that the crypto market could continue to drop.

dlnews.com • 1h ago

---

**[ING opens retail access to Bitcoin, Ethereum, Solana ETPs in Germany](https://www.theblock.co/post/388120/ing-bitcoin-ethereum-solana-etps)**

Still, ING Deutschland noted that crypto ETPs carry significant risks and stated that crypto has no intrinsic value.

The Block • 18h ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.285 Million Tokens, and Total Crypto and Total Cash Holdings of $10.7 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-285-million-tokens-and-total-crypto-and-total-cash-holdings-of-10-7-billion-302676048.html)**

Bitmine staked ETH stands at 2,873,459 and MAVAN staking solution on track to launch Q1 2026 Bitmine now owns 3.55% of the ETH token supply, over 70% of the...

PR Newswire • 1d ago

---

**[Ethereum Price Slips Below $2,500 — Here Are The Next Support Levels](https://www.tradingview.com/news/newsbtc:8023eb943094b:0-ethereum-price-slips-below-2-500-here-are-the-next-support-levels/)**

The Ethereum price has been under intense bearish pressure over the past few weeks, reflecting the overall fragile state of the cryptocurrency market. The altcoin lost nearly 20% of its value in the past week, free-falling under the psychological $3,000 level since Thursday, January 29th. With the…

TradingView • 2d ago

---

**[Ethereum Falls 10% In Selloff](https://www.investing.com/news/cryptocurrency-news/ethereum-falls-10-in-selloff-4477658)**

Ethereum Falls 10% In Selloff

Investing.com • 3d ago

---

**[Why Are Bitcoin, Ethereum and XRP Prices Going Down Today Again?](https://coinpedia.org/news/why-are-bitcoin-ethereum-and-xrp-prices-going-down-today-again/)**

After a brief recovery yesterday, the crypto market has turned red again. On Monday, prices moved higher after comments from US President Donald Trump,

Coinpedia • 7h ago

---

**[3 Things Investors Need to Know About Ethereum Classic in 2026](https://www.fool.com/investing/2026/02/03/3-things-investors-need-to-know-about-ethereum-cla/)**

Ethereum and Ethereum Classic started as one blockchain, but their paths and performance have diverged over the past decade.

The Motley Fool • 9h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=ZMK-98Y8N1I)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 200 • 💬 17 • ⏱️ 5:48 • 10h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=50rkmhAPvSI)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 166 • 💬 22 • ⏱️ 4:02 • 4h ago

---

**[Ethereum’s Vision Is Incredibly Bullish… So Why Is the Price So Bad? w/ Jeff Park](https://www.youtube.com/watch?v=tJLZausdujc)**

Free Milk Road Newsletters: ...

📺 Milk Road

👁️ 15K • 👍 369 • 💬 37 • ⏱️ 15:51 • 2d ago

---

**[BITCOIN AND ETH: BULLS HAVE A CHANCE HERE!!! 🚨🚨🚨 (ISM)](https://www.youtube.com/watch?v=pdpUrzqUSZ0)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 23K • 👍 1K • 💬 105 • ⏱️ 59:39 • 14h ago

---

**[TOM LEE owes investors $6bn. ETHEREUM &amp; BITCOIN PRICE PREDICTION](https://www.youtube.com/watch?v=lkj4hbXKIPc)**

WEEX EXCHANGE | NO KYC | 50% deposit Bonus | Up To $30000 In Bonus https://www.weex.com/en/register?vipCode=dqqj ...

📺 TMG Trades

👁️ 2K • 👍 119 • 💬 40 • ⏱️ 10:53 • 8h ago

---

**[Shorting Ethereum: My Life-Changing Trade](https://www.youtube.com/watch?v=L9tejtx7sXA)**

After getting chopped up in ETH shorts over the past few months, I found a moment of Tom Lee weakness to short ETH one last ...

📺 Taiki Maeda

👁️ 16K • 👍 797 • 💬 219 • ⏱️ 48:54 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=fEyNvRFi_OA)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 4K • 👍 220 • 💬 7 • ⏱️ 4:10 • 1d ago

---

**[BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=ObRvo0J4ygM)**

BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 11K • 👍 374 • 💬 507 • ⏱️ 23:54 • 1d ago

---

**[Tom Lee Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=OpRy3WJO7mA)**

Tom Lee Just Said The UNTHINKABLE About Bitcoin & Ethereum! ["It's a Fake Crash"] My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 12K • 👍 424 • 💬 114 • ⏱️ 18:04 • 1d ago

---

**[Crypto Investors Are In SERIOUS Trouble (Tom Lee &amp; Raoul Pal)](https://www.youtube.com/watch?v=KVKyHOtnSfI)**

LIMITED TIME: ✓ Bitunix (no kyc, $10k bonus): https://www.bitunix.com/register?vipCode=AltcoinDaily 50% deposit bonus on ...

📺 Altcoin Daily

👁️ 89K • 👍 3K • 💬 792 • ⏱️ 10:56 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
