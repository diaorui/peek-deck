---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-04T16:09:22.720706+00:00'
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

**Last Updated:** February 04, 2026 at 16:09 UTC  
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

### $2,148.21

---

## Ethereum Chart

**24h:** -2.1%  
**7d:** -23.9%  
**30d:** -34.8%  
**90d:** -37.5%  
**1y:** -22.8%  

---

## Ethereum Market Stats

**Market Cap:** $261.67B
Rank #2

**Circulating Supply:** 120,693,577 ETH
No max supply

**All-Time High:** $4,946.05
-56.2%

**All-Time Low:** $0.43
+499861.9%

---

## Reddit: r/ethereum

**[Daily General Discussion February 04, 2026](https://www.reddit.com/r/ethereum/comments/1qvglhu/daily_general_discussion_february_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

10h ago

---

**[Buterin Reframes Ethereum Strategy As Scaling Focus Returns To Base Layer](https://www.reddit.com/r/ethereum/comments/1qvozvl/buterin_reframes_ethereum_strategy_as_scaling/)**

The long-term technical vision for Ethereum is undergoing a significant correction. : Get all the latest crypto news at Sandmark

🔗 [Sandmark](https://www.sandmark.com/news/top-news/buterin-reframes-ethereum-strategy-scaling-focus-returns-base-layer?utm_medium=referral&utm_source=redbot&utm_campaign=redbot-ww-en-brand) • 2h ago

---

**[Best podcast for actual Ethereum updates - NOT PRICE](https://www.reddit.com/r/ethereum/comments/1qvprfd/best_podcast_for_actual_ethereum_updates_not_price/)**

I’d like a more technical and realistic analysis of Ethereum and how things are changing and growing. Please let me know if you know a good podcast or YouTube channel that does this. Thank you.

1h ago

---

**[On L2s and Ethereum](https://www.reddit.com/r/ethereum/comments/1quv8if/on_l2s_and_ethereum/)**

There have recently been some discussions on the ongoing role of L2s in the Ethereum ecosystem, especially in the face of two facts: L2s' progress to stage 2 (and, secondarily, on interop) has been far slower and more difficult than originally expected L1 itself is scaling, fees are very low, and gaslimits are projected to increase greatly in 2026 Both of these facts, for their own separate reasons, mean that the original vision of L2s and their role in Ethereum no longer makes sense, and we need a new path. First, let us recap the original vision. Ethereum needs to scale. The definition of "Ethereum scaling" is the existence of large quantities of block space that is backed by the full faith and credit of Ethereum - that is, block space where, if you do things (including with ETH) inside that block space, your activities are guaranteed to be valid, uncensored, unreverted, untouched, as long as Ethereum itself functions. If you create a 10000 TPS EVM where its connection to L1 is mediated by a multisig bridge, then you are not scaling Ethereum. This vision no longer makes sense. L1 does not need L2s to be "branded shards", because L1 is itself scaling. And L2s are not able or willing to satisfy the properties that a true "branded shard" would require. I've even seen at least one explicitly saying that they may never want to go beyond stage 1, not just for technical reasons around ZK-EVM safety, but also because their customers' regulatory needs require them to have ultimate control. This may be doing the right thing for your customers. But it should be obvious that if you are doing this, then you are not "scaling Ethereum" in the sense meant by the rollup-centric roadmap. But that's fine! it's fine because Ethereum itself is now scaling directly on L1, with large planned increases to its gas limit this year and the years ahead. We should stop thinking about L2s as literally being "branded shards" of Ethereum, with the social status and responsibilities that this entails. Instead, we can think of L2s as being a full spectrum, which includes both chains backed by the full faith and credit of Ethereum with various unique properties (eg. not just EVM), as well as a whole array of options at different levels of connection to Ethereum, that each person (or bot) is free to care about or not care about depending on their needs. What would I do today if I were an L2? Identify a value add other than "scaling". Examples: (i) non-EVM specialized features/VMs around privacy, (ii) efficiency specialized around a particular application, (iii) truly extreme levels of scaling that even a greatly expanded L1 will not do, (iv) a totally different design for non-financial applications, eg. social, identity, AI, (v) ultra-low-latency and other sequencing properties, (vi) maybe built-in oracles or decentralized dispute resolution or other "non-computationally-verifiable" features Be stage 1 at the minimum (otherwise you really are just a separate L1 with a bridge, and you should just call yourself that) if you're doing things with ETH or other ethereum-issued assets Support maximum interoperability with Ethereum, though this will differ for each one (eg. what if you're not EVM, or even not financial?) From Ethereum's side, over the past few months I've become more convinced of the value of the native rollup precompile, particuarly once we have enshrined ZK-EVM proofs that we need anyway to scale L1. This is a precompile that verifies a ZK-EVM proof, and it's "part of Ethereum", so (i) it auto-upgrades along with Ethereum, and (ii) if the precompile has a bug, Ethereum will hard-fork to fix the bug. The native rollup precompile would make full, security-council-free, EVM verification accessible. We should spend much more time working out how to design it in such a way that if your L2 is "EVM plus other stuff", then the native rollup precompile would verify the EVM, and you only have to bring your own prover for the "other stuff" (eg. Stylus). This might involve a canonical way of exposing a lookup table between contract call inputs and outputs, and letting you provide your own values to the lookup table (that you would prove separately). This would make it easy to have safe, strong, trustless interoperability with Ethereum. It also enables synchronous composability (see: https://ethresear.ch/t/combining-preconfirmations-with-based-rollups-for-synchronous-composability/23863 and https://ethresear.ch/t/synchronous-composability-between-rollups-via-realtime-proving/23998 ). And from there, it's each L2's choice exactly what they want to build. Don't just "extend L1", figure out something new to add. This of course means that some will add things that are trust-dependent, or backdoored, or otherwise insecure; this is unavoidable in a permissionless ecosystem where developers have freedom. Our job should make to make it clear to users what guarantees they have, and to build up the strongest Ethereum that we can.

1d ago

---

**[Exchange rate oracles + stablecoins for developing nations](https://www.reddit.com/r/ethereum/comments/1qvlg25/exchange_rate_oracles_stablecoins_for_developing/)**

Been away from Ethereum from some time and would like to jump onboard again. It seems to me neutral opensource software will become increasingly relevant due to the changing world order and Ethereum will play a significant role. I'm particularly interested in how Ethereum can be used for daily payments via stablecoins. I would like to know if anyone is working on (1) on-chain oracles for currency exchange-rates and (2) stablecoins for developing nation currencies. My aim is to understand what kind of on-chain infrastructure needs to be there to enable normal people to transparently use Ethereum to pay for their morning coffee. Happy to discuss!

5h ago

---

**[Daily General Discussion February 03, 2026](https://www.reddit.com/r/ethereum/comments/1quk1p6/daily_general_discussion_february_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[ZK (Zero knowledge) proof for SHA-256: 312-byte proof, ~18µs verification](https://www.reddit.com/r/ethereum/comments/1qv2hzp/zk_zero_knowledge_proof_for_sha256_312byte_proof/)**

20h ago

---

**[Effect-TS library for EVM frontends](https://www.reddit.com/r/ethereum/comments/1quxszt/effectts_library_for_evm_frontends/)**

22h ago

---

**[Paid DJ open call: perform at Decentraland’s 6th Birthday (Feb 20, $400 USD in MANA)](https://www.reddit.com/r/ethereum/comments/1qus8jw/paid_dj_open_call_perform_at_decentralands_6th/)**

Sharing a paid performance opportunity that might be relevant for artists here. Decentraland is running an open call for community DJs / performers to play a pre-recorded set during its 6th Birthday Party in the Theatre on February 20 at 8pm UTC. Key details: Pre-recorded DJ sets only (45–55 minutes) $400 USD paid in MANA per selected performer In-world audience gathered for the birthday event Intended for artists already familiar with Decentraland (not livestreams) This isn’t a pitch about crypto or Web3, it’s a straightforward paid performance slot inside an existing virtual world event. Full details and application here: https://zealous.co/decentraland/opportunity/decentraland-6th-birthday-party/

1d ago

---

**[In 2016, Ethereum faced "code is law" vs "fix the damage." Ten years later, I'm watching the same debate play out in a GitHub repo.](https://www.reddit.com/r/ethereum/comments/1qu6ahw/in_2016_ethereum_faced_code_is_law_vs_fix_the/)**

In June 2016, someone drained ~$60M from The DAO - a decentralized investment fund built on Ethereum. They didn't hack Ethereum itself. They exploited a recursive calling bug in the smart contract's own logic. The code allowed it. That's what made it a crisis. If "code is law," the attacker didn't do anything wrong. The contract ran as written. But $60M was gone and real people lost real money. Ethereum had to choose: reverse the blockchain to return the funds, or let it stand because the code permitted it. The community voted to hard fork - rewrite history and undo the damage. The people who refused to accept that kept running the original chain. That's how Ethereum Classic was born. The question at the center of it all: when your system is broken and the fix is known, do you break the rules to fix it, or do you let the rules play out even while the system burns? I'm watching a tiny version of this happen right now. I run OpenChaos - a GitHub repo where anyone submits a PR, the community votes with reactions, and the most-voted PR merges daily. No gatekeeping. Pure popular vote. 911 stars, 70+ open PRs, five weeks in. Last Friday, PR #62: "1.337% chance to see nothing" won the daily vote and merged. Three lines of code: if (Math.random() <= 0.01337) { return null; } A leet joke. 1.337% of the time, a visitor sees a blank page. Funny, harmless, right? The site caches server-side. When the page returns null, the cache treats the blank page as permanent. One unlucky render broke the site for every visitor, indefinitely. Not a 5-minute blip. A permanent outage from a 1.337% roll. A contributor diagnosed the root cause and submitted PR #173 - a clean fix, CI passes, no conflicts. But PR #173 has fewer votes than a DOOM port and a Rickroll. The fix has to wait its turn in the democratic queue. The site stays broken while the community votes on entertainment over infrastructure. One community member commented: "I am torn between fixing things quickly and letting the rules play out to see when the fix comes naturally. I want to see the naturally emergent behaviour." Sound familiar? Then it got more interesting. The contributor who wrote the fix also had another PR in the queue that was about to merge. He could have bundled the bugfix into that PR and shipped it quietly. He refused: "I considered adding this fix to #129, but it doesn't feel like it's in the spirit of the project. Even if it's a 'good' trojan horse, it's still a trojan horse." But another contributor made the opposite choice. The author of the DOOM port deliberately bundled the bugfix into their submission. If it merges tomorrow, the site comes back online - not through governance, but through the exact Trojan horse tactic the first contributor refused on principle. Two contributors. Same option. Opposite choices. Obviously nobody's losing $60M here. But the structure is the same: A system running as designed produces an unintended outcome The fix is known and ready The rules don't allow a fast path to deploy it The community has to decide: break the process or trust the process I opened Issue #176 proposing that only contributors with merged PRs should be allowed to vote - earned governance instead of open popularity contests. The debate is live. Questions I keep thinking about: Is there a middle ground between "code is law, let it burn" and "maintainer override"? Something that keeps democratic legitimacy while allowing fast response to emergencies? For those who lived through the DAO debate - looking back, what would you tell a small project facing its first "do we fork our own rules" moment? The repo: github.com/skridlevsky/openchaos The governance discussion: Issue #176 The broken site (may or may not be blank when you visit): openchaos.dev

1d ago

---

---

## Google News: "ethereum"

**[Can Ethereum Really Hit $10,000 This Year? The Answer Might Surprise You.](https://www.fool.com/investing/2026/02/04/can-ethereum-really-hit-10000-this-year-the-answer/)**

Based on data from prediction markets, Ethereum will have a tough climb this year.

The Motley Fool • 3h ago

---

**[Vitalik Buterin reevaluates Ethereum's rollup-centric roadmap, arguing L2s decentralized 'far slower' while base layer advanced](https://www.theblock.co/post/388285/vitalik-buterin-reevaluates-rollup-centric-roadmap-arguing-l2s-decentralized-far-slower-while-ethereum-base-layer-advanced)**

Buterin previously championed a "rollup-centric" roadmap that would scale Ethereum through a network of branded shards.

The Block • 23h ago

---

**['You are not scaling Ethereum': Vitalik Buterin issues a blunt reality check to the biggest crypto networks](https://www.coindesk.com/business/2026/02/03/you-are-not-scaling-ethereum-vitalik-buterin-issues-a-blunt-reality-check-to-the-biggest-crypto-networks)**

The roadmap in place doesn't make as much sense because progress among layer-2s toward later stages of decentralization has been slower and more difficult, and Ethereum itself is now scaling directly on layer-1.

CoinDesk • 22h ago

---

**['We Need a New Path': Ethereum Founder Vitalik Buterin Rips Up L2-Focused Roadmap](https://decrypt.co/356841/we-need-new-path-ethereum-founder-vitalik-buterin-rips-up-l2-focused-roadmap)**

Some layer-2 networks have made concessions when it comes to decentralization, Buterin said, and shouldn’t be “branded” as extensions of Ethereum.

Decrypt • 17h ago

---

**[Bitcoin, Ethereum continue plunge — and experts warn of more pain to come](https://finance.yahoo.com/news/bitcoin-ethereum-continue-plunge-experts-215357559.html)**

Bitcoin and Ethereum plunged further on Tuesday. The two biggest digital coins are now well below their all-time highs. Experts have signalled that the crypto market could continue to drop.

Yahoo Finance • 18h ago

---

**[Bitcoin, XRP, Ethereum Drop. Why Cryptos Are Under Pressure Today.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-cryptos-gold-9051820f?gaa_at=eafs&gaa_n=AWEtsqc2m9oBPl0b7nbOTxOysC_v340EOJIsfDpwMbFm9O7YvWUnWxWlIZM-&gaa_ts=6983729a&gaa_sig=6P5UIizzIwKRQ_oIA1vsKeBAIEiQepZL377FLe1Jp6FLMrrc9BK8QZYIHCaR__CB63QqSFZ8lJsyDYevXi3sQA%3D%3D)**

Barron's • 4h ago

---

**[BitMine acquires more ethereum despite being underwater amid token’s price decline](https://sherwood.news/crypto/bitmine-acquires-more-ethereum-despite-being-underwater-amid-tokens-price/)**

CEO Tom Lee believes “the price of ETH is not reflective of the high utility of ETH and its role as the future of finance.”...

Sherwood News • 1d ago

---

**[Ethereum Price Recovery Runs Into A Wall, Decline Risk Returns](https://www.tradingview.com/news/newsbtc:4d0ac60d3094b:0-ethereum-price-recovery-runs-into-a-wall-decline-risk-returns/)**

Ethereum price extended its decline below $2,220 and $2,200. ETH is now attempting to recover from $2,000 but faces many hurdles near $2,250.Ethereum Price Faces ResistanceEthereum price failed to remain stable above $2,320 and extended losses, like Bitcoin. ETH price traded below $2,220 to enter a…

TradingView • 12h ago

---

**[Ethereum Falls 10% In Rout](https://www.investing.com/news/cryptocurrency-news/ethereum-falls-10-in-rout-4477776)**

Ethereum Falls 10% In Rout

Investing.com • 2d ago

---

**[Ethereum vs Bitcoin: Jack Yi Admits ETH Bull Call Came Too Soon](https://stocktwits.com/news-articles/markets/cryptocurrency/ethereum-bull-jack-yi-says-early-eth-bullish-bet-was-mistimed-and-a-mistake/cZbgN2PR4kB)**

The shift came amid heavy liquidations and market trends favoring Bitcoin under macro pressure.

Stocktwits • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum After Major Pullbacks: Navigating ETH’s Recovery | BMNR Update](https://www.youtube.com/watch?v=AiYCaUPIK0o)**

Ethereum has experienced multiple major pullbacks throughout its history and every recovery followed a recognizable pattern.

📺 The Value Thinker

👁️ 1K • 👍 209 • 💬 88 • ⏱️ 22:38 • 3h ago

---

**[BITCOIN AND ETH: TRYING TO BOUNCE!!!!! 🚨🚨🚨 (Vitalik kills L2s)](https://www.youtube.com/watch?v=md6nK4g8c4U)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 12K • 👍 1K • 💬 45 • ⏱️ 50:26 • 6h ago

---

**[David Siemer Outlines Bitcoin and Ethereum&#39;s Paths Back to Record Highs](https://www.youtube.com/watch?v=sxj1YbCv2GQ)**

Bitcoin's dip below $75000 is something David Siemer calls a "buying opportunity." He sees promise in the crypto space long-term ...

📺 Schwab Network

👁️ 10K • 👍 136 • 💬 16 • ⏱️ 6:37 • 15h ago

---

**[We Just Got EARTH SHATTERING Ethereum News XRP DeFi Is Coming MAJOR Gold And Silver Update](https://www.youtube.com/watch?v=sit3fzWSrMQ)**

Ask and you shall receive... or maybe just complain a lot and then the information will fall into your lap. That one makes a bit more ...

📺 The Modern Investor

👁️ 4K • 👍 619 • 💬 248 • ⏱️ 29:04 • 4h ago

---

**[ETHEREUM CRASH Alert! (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=RRTBEPAZK34)**

JACOB'S Whop - Discover The Alpha, Join The VIP Group Today - https://whop.com/onchainacademy - Best Exchange I've Ever ...

📺 Jacob Crypto Bury

👁️ 323 • 👍 6 • 💬 47 • ⏱️ 4:54 • 20h ago

---

**[Crypto Investors Are In SERIOUS Trouble (Tom Lee &amp; Raoul Pal)](https://www.youtube.com/watch?v=KVKyHOtnSfI)**

LIMITED TIME: ✓ Bitunix (no kyc, $10k bonus): https://www.bitunix.com/register?vipCode=AltcoinDaily 50% deposit bonus on ...

📺 Altcoin Daily

👁️ 105K • 👍 3K • 💬 694 • ⏱️ 10:56 • 1d ago

---

**[BULLISH PATTERN FORMING!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=RgcpoJNpX7U)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 184 • 👍 10 • 💬 2 • ⏱️ 4:29 • 6h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=50rkmhAPvSI)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 4K • 👍 242 • 💬 8 • ⏱️ 4:02 • 20h ago

---

**[Tom Lee Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=OpRy3WJO7mA)**

Tom Lee Just Said The UNTHINKABLE About Bitcoin & Ethereum! ["It's a Fake Crash"] My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 13K • 👍 442 • 💬 51 • ⏱️ 18:04 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=ZMK-98Y8N1I)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 4K • 👍 205 • 💬 17 • ⏱️ 5:48 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
