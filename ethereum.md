---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-03T09:43:14.875905+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 03, 2026 at 09:43 UTC  
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

### $2,277.26

---

## Ethereum Chart

**24h:** +0.9%  
**7d:** -23.7%  
**30d:** -28.8%  
**90d:** -30.7%  
**1y:** -16.1%  

---

## Ethereum Market Stats

**Market Cap:** $276.33B
Rank #2

**Circulating Supply:** 120,693,657 ETH
No max supply

**All-Time High:** $4,946.05
-53.7%

**All-Time Low:** $0.43
+528872.5%

---

## Reddit: r/ethereum

**[Daily General Discussion February 03, 2026](https://www.reddit.com/r/ethereum/comments/1quk1p6/daily_general_discussion_february_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3h ago

---

**[In 2016, Ethereum faced "code is law" vs "fix the damage." Ten years later, I'm watching the same debate play out in a GitHub repo.](https://www.reddit.com/r/ethereum/comments/1qu6ahw/in_2016_ethereum_faced_code_is_law_vs_fix_the/)**

In June 2016, someone drained ~$60M from The DAO - a decentralized investment fund built on Ethereum. They didn't hack Ethereum itself. They exploited a recursive calling bug in the smart contract's own logic. The code allowed it. That's what made it a crisis. If "code is law," the attacker didn't do anything wrong. The contract ran as written. But $60M was gone and real people lost real money. Ethereum had to choose: reverse the blockchain to return the funds, or let it stand because the code permitted it. The community voted to hard fork - rewrite history and undo the damage. The people who refused to accept that kept running the original chain. That's how Ethereum Classic was born. The question at the center of it all: when your system is broken and the fix is known, do you break the rules to fix it, or do you let the rules play out even while the system burns? I'm watching a tiny version of this happen right now. I run OpenChaos - a GitHub repo where anyone submits a PR, the community votes with reactions, and the most-voted PR merges daily. No gatekeeping. Pure popular vote. 911 stars, 70+ open PRs, five weeks in. Last Friday, PR #62: "1.337% chance to see nothing" won the daily vote and merged. Three lines of code: if (Math.random() <= 0.01337) { return null; } A leet joke. 1.337% of the time, a visitor sees a blank page. Funny, harmless, right? The site caches server-side. When the page returns null, the cache treats the blank page as permanent. One unlucky render broke the site for every visitor, indefinitely. Not a 5-minute blip. A permanent outage from a 1.337% roll. A contributor diagnosed the root cause and submitted PR #173 - a clean fix, CI passes, no conflicts. But PR #173 has fewer votes than a DOOM port and a Rickroll. The fix has to wait its turn in the democratic queue. The site stays broken while the community votes on entertainment over infrastructure. One community member commented: "I am torn between fixing things quickly and letting the rules play out to see when the fix comes naturally. I want to see the naturally emergent behaviour." Sound familiar? Then it got more interesting. The contributor who wrote the fix also had another PR in the queue that was about to merge. He could have bundled the bugfix into that PR and shipped it quietly. He refused: "I considered adding this fix to #129, but it doesn't feel like it's in the spirit of the project. Even if it's a 'good' trojan horse, it's still a trojan horse." But another contributor made the opposite choice. The author of the DOOM port deliberately bundled the bugfix into their submission. If it merges tomorrow, the site comes back online - not through governance, but through the exact Trojan horse tactic the first contributor refused on principle. Two contributors. Same option. Opposite choices. Obviously nobody's losing $60M here. But the structure is the same: A system running as designed produces an unintended outcome The fix is known and ready The rules don't allow a fast path to deploy it The community has to decide: break the process or trust the process I opened Issue #176 proposing that only contributors with merged PRs should be allowed to vote - earned governance instead of open popularity contests. The debate is live. Questions I keep thinking about: Is there a middle ground between "code is law, let it burn" and "maintainer override"? Something that keeps democratic legitimacy while allowing fast response to emergencies? For those who lived through the DAO debate - looking back, what would you tell a small project facing its first "do we fork our own rules" moment? The repo: github.com/skridlevsky/openchaos The governance discussion: Issue #176 The broken site (may or may not be blank when you visit): openchaos.dev

13h ago

---

**[How a premature software standard has led to billions in losses](https://www.reddit.com/r/ethereum/comments/1qtw9fe/how_a_premature_software_standard_has_led_to/)**

🔗 [hugo0.com](https://hugo0.com/blog/how-erc20-held-back-blockchain-payments-a-decade) • 19h ago

---

**[Daily General Discussion February 02, 2026](https://www.reddit.com/r/ethereum/comments/1qtn0fr/daily_general_discussion_february_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[a whitepaper on a yield-focused dao](https://www.reddit.com/r/ethereum/comments/1qubsh4/a_whitepaper_on_a_yieldfocused_dao/)**

i’ve been working on a yield/token architecture that tries to be very explicit about separation of concerns, and i’m mostly looking for feedback from people who are already uncomfortable with how tightly coupled most defi tokens are today. the basic premise is simple: the token contract should not know or care about yield. no rebases, no transfer hooks, no strategy logic bleeding into balance accounting. instead, all yield is routed through a single on-chain component that handles normalization, accounting, and distribution according to policy. i ended up implementing this as a modular system with a canonical “revenue router”: the base token is just erc20 + voting, nothing else all yield sources plug into a router instead of the token yield gets normalized into a treasury asset before distribution distribution is policy-driven (buybacks, staking, hybrid), not hardcoded yield sources are plugins with tiered trust and execution limits failure isn’t implicit: plugins can be quarantined without nuking the system the goal isn’t yield maximization per se, but predictable value accrual with reduced blast radius. plugins can be permissionless, but they don’t all get the same authority. everything that touches value has explicit constraints. accounting is deterministic. no component can “surprise” the token. i wrote all of this up as a whitepaper (vastitas) and tried to be very concrete about invariants, routing rules, quarantine mechanics, and trade-offs, including some simulated comparisons against monolithic tokens and yield aggregators i’m not trying to sell this as obviously correct. i’m more interested in whether this direction resonates with people who think long-term token sustainability is more about architecture than clever incentives. i made a faulty deployment on arbitrum and a half working one on base. nothing is finalized. i’m mainly looking to pressure-test the ideas with people who agree that this might be a good project. feel free to poke holes, challenge assumptions, or point me to similar work i might have missed.

10h ago

---

**[Staking](https://www.reddit.com/r/ethereum/comments/1qu0vj0/staking/)**

Should I be staking 100% of my Ethereum? Can someone explain to me like im 5 what this means? Apologies if this type of post is not allowed, moderators.

16h ago

---

**[Two-layer governance](https://www.reddit.com/r/ethereum/comments/1qtndkm/twolayer_governance/)**

Re https://firefly.social/post/x/2018205196568944653 I actually don't think it's complicated. IMO the future of onchain mechanism design is mostly going to fit into one pattern: [something that looks like a prediction market] -> [something that looks like a capture-resistant, non-financialized preference-setting gadget] In other words: One layer that is maximally open and maximizes accountability (it's a market, anyone can buy and sell, if you make good decisions you win money if you make bad decisions you lose money) One layer that is decentralized and pluralistic, and that maximizes space for intrinsic motivation. This cannot be token-based, because token owners are not pluralistic, and anyone can buy in and get 51% of them. Votes here should be anonymous, ideally MACI'd to reduce risk of collusion. The prediction market is the correct way to do a "decentralized executive", because the most logical primitive for "accountability" in a permissionless concept is exactly that. Though sometimes you will want to keep it simple, and do a centralized executive at that layer instead: [replaceable centralized executive] -> [something that looks like a capture-resistant, non-financialized preference-setting gadget] Thinking in these two layers explicitly: (i) what is doing your execution, (ii) what is doing your preference-setting and is judging the executor(s), is best.

1d ago

---

**[Sold BTC into USDC (ERC20) now want to get back into BTC via WBTC. Best way to swap?](https://www.reddit.com/r/ethereum/comments/1qtmbfd/sold_btc_into_usdc_erc20_now_want_to_get_back/)**

1d ago

---

**[Where can I sell an unused gift card for crypto?](https://www.reddit.com/r/ethereum/comments/1qtu5js/where_can_i_sell_an_unused_gift_card_for_crypto/)**

20h ago

---

**[Daily General Discussion February 01, 2026](https://www.reddit.com/r/ethereum/comments/1qsqd70/daily_general_discussion_february_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Bitcoin, Ethereum ETF Investments Flip Negative for 2026 as Crypto Funds Shed $1.7B](https://decrypt.co/356622/bitcoin-ethereum-etf-investments-flip-negative-for-2026-as-crypto-funds-shed-1-7b)**

U.S.-listed crypto funds led withdrawals as Bitcoin and Ethereum prices slid after Donald Trump’s nomination of Kevin Warsh for Fed chair.

Decrypt • 16h ago

---

**[Ethereum (ETH) news: ‘We need to prepare’ for quantum computing](https://www.coindesk.com/tech/2026/02/01/quantum-threat-gets-real-ethereum-foundation-prioritizes-security-with-leanvm-and-pq-signatures)**

Earlier in January, the Ethereum Foundation formally elevated post-quantum security to a strategic priority, creating a dedicated Post-Quantum team.

CoinDesk • 1d ago

---

**[Ethereum Falls 10% In Rout](https://www.investing.com/news/cryptocurrency-news/ethereum-falls-10-in-rout-4477776)**

Ethereum Falls 10% In Rout

Investing.com • 1d ago

---

**[BitMine Immersion Can’t Stop Buying Ethereum as Crypto Prices Tank](https://finance.yahoo.com/news/bitmine-immersion-t-stop-buying-204823044.html)**

BitMine Immersion continues to accumulate Ethereum amid price declines, following a treasury strategy inspired by Strategy.

Yahoo Finance • 3d ago

---

**[A sudden shift in Ethereum staking is draining billions from exchanges toward a new corporate elite](https://cryptoslate.com/how-staking-turned-ethereum-into-a-treasury-trade/)**

Corporate Ethereum treasuries use staking to earn additional ETH, turning reserves into a compounding strategy instead of passive exposure.

CryptoSlate • 1d ago

---

**[Prediction: 2026 Will Be the Year of Ethereum (ETH)](https://www.fool.com/investing/2026/02/02/prediction-2026-will-be-the-year-of-ethereum-eth/)**

The adoption, technology, and regulation stars may all align for Ethereum this year.

The Motley Fool • 19h ago

---

**[Ethereum: Does creator vision matter more than ETH’s chart? Vitalik Buterin says…](https://ambcrypto.com/ethereum-does-creator-vision-matter-more-than-eths-chart-vitalik-buterin-says/)**

Ether may be hurting, but the founder is thinking years ahead.

AMBCrypto • 10h ago

---

**[Ethereum vs Bitcoin: Jack Yi Admits ETH Bull Call Came Too Soon](https://stocktwits.com/news-articles/markets/cryptocurrency/ethereum-bull-jack-yi-says-early-eth-bullish-bet-was-mistimed-and-a-mistake/cZbgN2PR4kB)**

The shift came amid heavy liquidations and market trends favoring Bitcoin under macro pressure.

Stocktwits • 23h ago

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

**[BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=ObRvo0J4ygM)**

BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 9K • 👍 345 • 💬 160 • ⏱️ 23:54 • 11h ago

---

**[Tom Lee Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=OpRy3WJO7mA)**

Tom Lee Just Said The UNTHINKABLE About Bitcoin & Ethereum! ["It's a Fake Crash"] My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 10K • 👍 395 • 💬 103 • ⏱️ 18:04 • 18h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=zCCN5NIzpqk)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 170 • 💬 12 • ⏱️ 5:14 • 10h ago

---

**[BITCOIN AND ETH: LAST CHANCE TO RECOVER!!!! 🚨🚨🚨 (MicroStrategy REKT)](https://www.youtube.com/watch?v=bLiHfECZH3k)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 28K • 👍 2K • 💬 219 • ⏱️ 46:08 • 23h ago

---

**[Shorting Ethereum: My Life-Changing Trade](https://www.youtube.com/watch?v=L9tejtx7sXA)**

After getting chopped up in ETH shorts over the past few months, I found a moment of Tom Lee weakness to short ETH one last ...

📺 Taiki Maeda

👁️ 14K • 👍 729 • 💬 194 • ⏱️ 48:54 • 1d ago

---

**[Bitcoin, Ethereum &amp; Altcoins DOWN BAD (NOW THIS!?)](https://www.youtube.com/watch?v=CxKURlwrfIM)**

In today's video, we're breaking down why the pain for Bitcoin (BTC), Ethereum (ETH), and the broader Altcoin market might not ...

📺 Discover Crypto

👁️ 9K • 👍 461 • 💬 147 • ⏱️ 1:43:46 • 16h ago

---

**[Tom Lee Drops HUGE Warning About 2026 | The Bull Run Has CHANGED](https://www.youtube.com/watch?v=3dh-JR2mdzA)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 7K • 👍 161 • 💬 202 • ⏱️ 15:18 • 1d ago

---

**[Tom Lee: This Is a Fake Sell-off! The Bull Run Continues By THIS Date](https://www.youtube.com/watch?v=af5DO4Y_8cc)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 23K • 👍 839 • 💬 115 • ⏱️ 21:16 • 1d ago

---

**[Why Bitcoin, ETH &amp; Altcoins Are CRASHING HARD](https://www.youtube.com/watch?v=-rrpLsrAr9Q)**

Nick Valdez looks at the latest market crash with the next level Bitcoin MUST hold for support! Join Our Trading Group Discord ...

📺 Discover Crypto

👁️ 26K • 👍 830 • 💬 182 • ⏱️ 4:28 • 2d ago

---

**[Ethereum’s Vision Is Incredibly Bullish… So Why Is the Price So Bad? w/ Jeff Park](https://www.youtube.com/watch?v=tJLZausdujc)**

Free Milk Road Newsletters: ...

📺 Milk Road

👁️ 14K • 👍 346 • 💬 31 • ⏱️ 15:51 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
