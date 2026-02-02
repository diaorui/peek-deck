---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-02T23:08:46.293433+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- videos
- social
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 02, 2026 at 23:08 UTC  
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

### $2,339.88

---

## Ethereum Chart

**24h:** +2.5%  
**7d:** -22.3%  
**30d:** -25.3%  
**90d:** -31.3%  
**1y:** -18.5%  

---

## Ethereum Market Stats

**Market Cap:** $283.24B
Rank #2

**Circulating Supply:** 120,693,748 ETH
No max supply

**All-Time High:** $4,946.05
-52.5%

**All-Time Low:** $0.43
+542175.7%

---

## Reddit: r/ethereum

**[In 2016, Ethereum faced "code is law" vs "fix the damage." Ten years later, I'm watching the same debate play out in a GitHub repo.](https://www.reddit.com/r/ethereum/comments/1qu6ahw/in_2016_ethereum_faced_code_is_law_vs_fix_the/)**

In June 2016, someone drained ~$60M from The DAO - a decentralized investment fund built on Ethereum. They didn't hack Ethereum itself. They exploited a recursive calling bug in the smart contract's own logic. The code allowed it. That's what made it a crisis. If "code is law," the attacker didn't do anything wrong. The contract ran as written. But $60M was gone and real people lost real money. Ethereum had to choose: reverse the blockchain to return the funds, or let it stand because the code permitted it. The community voted to hard fork - rewrite history and undo the damage. The people who refused to accept that kept running the original chain. That's how Ethereum Classic was born. The question at the center of it all: when your system is broken and the fix is known, do you break the rules to fix it, or do you let the rules play out even while the system burns? I'm watching a tiny version of this happen right now. I run OpenChaos - a GitHub repo where anyone submits a PR, the community votes with reactions, and the most-voted PR merges daily. No gatekeeping. Pure popular vote. 911 stars, 70+ open PRs, five weeks in. Last Friday, PR #62: "1.337% chance to see nothing" won the daily vote and merged. Three lines of code: if (Math.random() <= 0.01337) { return null; } A leet joke. 1.337% of the time, a visitor sees a blank page. Funny, harmless, right? The site caches server-side. When the page returns null, the cache treats the blank page as permanent. One unlucky render broke the site for every visitor, indefinitely. Not a 5-minute blip. A permanent outage from a 1.337% roll. A contributor diagnosed the root cause and submitted PR #173 - a clean fix, CI passes, no conflicts. But PR #173 has fewer votes than a DOOM port and a Rickroll. The fix has to wait its turn in the democratic queue. The site stays broken while the community votes on entertainment over infrastructure. One community member commented: "I am torn between fixing things quickly and letting the rules play out to see when the fix comes naturally. I want to see the naturally emergent behaviour." Sound familiar? Then it got more interesting. The contributor who wrote the fix also had another PR in the queue that was about to merge. He could have bundled the bugfix into that PR and shipped it quietly. He refused: "I considered adding this fix to #129, but it doesn't feel like it's in the spirit of the project. Even if it's a 'good' trojan horse, it's still a trojan horse." But another contributor made the opposite choice. The author of the DOOM port deliberately bundled the bugfix into their submission. If it merges tomorrow, the site comes back online - not through governance, but through the exact Trojan horse tactic the first contributor refused on principle. Two contributors. Same option. Opposite choices. Obviously nobody's losing $60M here. But the structure is the same: A system running as designed produces an unintended outcome The fix is known and ready The rules don't allow a fast path to deploy it The community has to decide: break the process or trust the process I opened Issue #176 proposing that only contributors with merged PRs should be allowed to vote - earned governance instead of open popularity contests. The debate is live. Questions I keep thinking about: Is there a middle ground between "code is law, let it burn" and "maintainer override"? Something that keeps democratic legitimacy while allowing fast response to emergencies? For those who lived through the DAO debate - looking back, what would you tell a small project facing its first "do we fork our own rules" moment? The repo: github.com/skridlevsky/openchaos The governance discussion: Issue #176 The broken site (may or may not be blank when you visit): openchaos.dev

2h ago

---

**[Daily General Discussion February 02, 2026](https://www.reddit.com/r/ethereum/comments/1qtn0fr/daily_general_discussion_february_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

17h ago

---

**[How a premature software standard has led to billions in losses](https://www.reddit.com/r/ethereum/comments/1qtw9fe/how_a_premature_software_standard_has_led_to/)**

🔗 [hugo0.com](https://hugo0.com/blog/how-erc20-held-back-blockchain-payments-a-decade) • 8h ago

---

**[Staking](https://www.reddit.com/r/ethereum/comments/1qu0vj0/staking/)**

Should I be staking 100% of my Ethereum? Can someone explain to me like im 5 what this means? Apologies if this type of post is not allowed, moderators.

6h ago

---

**[Two-layer governance](https://www.reddit.com/r/ethereum/comments/1qtndkm/twolayer_governance/)**

Re https://firefly.social/post/x/2018205196568944653 I actually don't think it's complicated. IMO the future of onchain mechanism design is mostly going to fit into one pattern: [something that looks like a prediction market] -> [something that looks like a capture-resistant, non-financialized preference-setting gadget] In other words: One layer that is maximally open and maximizes accountability (it's a market, anyone can buy and sell, if you make good decisions you win money if you make bad decisions you lose money) One layer that is decentralized and pluralistic, and that maximizes space for intrinsic motivation. This cannot be token-based, because token owners are not pluralistic, and anyone can buy in and get 51% of them. Votes here should be anonymous, ideally MACI'd to reduce risk of collusion. The prediction market is the correct way to do a "decentralized executive", because the most logical primitive for "accountability" in a permissionless concept is exactly that. Though sometimes you will want to keep it simple, and do a centralized executive at that layer instead: [replaceable centralized executive] -> [something that looks like a capture-resistant, non-financialized preference-setting gadget] Thinking in these two layers explicitly: (i) what is doing your execution, (ii) what is doing your preference-setting and is judging the executor(s), is best.

16h ago

---

**[Sold BTC into USDC (ERC20) now want to get back into BTC via WBTC. Best way to swap?](https://www.reddit.com/r/ethereum/comments/1qtmbfd/sold_btc_into_usdc_erc20_now_want_to_get_back/)**

17h ago

---

**[Where can I sell an unused gift card for crypto?](https://www.reddit.com/r/ethereum/comments/1qtu5js/where_can_i_sell_an_unused_gift_card_for_crypto/)**

10h ago

---

**[Daily General Discussion February 01, 2026](https://www.reddit.com/r/ethereum/comments/1qsqd70/daily_general_discussion_february_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[How I would do creator coins](https://www.reddit.com/r/ethereum/comments/1qsysag/how_i_would_do_creator_coins/)**

We've seen about 10 years of people trying to do content incentivization in crypto, from early-stage platforms like Bihu and Steemit, to BitClout in 2021, to Zora, to tipping features inside of decentralized social, and more. So far, I think we have not been very successful, and I think this is because the problem is fundamentally hard. First, my view of what the problem is. A major difference between doing "creator incentives" in the 00s vs doing them today, is that in the 00s, a primary problem was having not enough content at all. In the 20s, there's plenty of content, AI can generate an entire metaverse full of it for like $10. The problem is quality. And so your goal is not incentivizing content, it's surfacing good content. Personally, I think that the most successful example of creator incentives we've seen is Substack. To see why, take a look at the top 10: https://substack.com/leaderboard/technology/paid https://substack.com/leaderboard/culture/paid https://substack.com/leaderboard/world-politics/paid Now, you may disagree with many of these authors. But I have no doubt that: They are on the whole high quality, and contribute positively to the discussion They are mostly people who would not have been elevated without Substack's presence So Substack is genuinely surfacing high quality and pluralism. Now, we can compare to creator coin projects. I don't want to pick on a single one, because I think there's a failure mode of the entire category. For example: Top Zora creator coins: https://www.coingecko.com/en/categories/zora-creator-coins BitClout: https://www.businessofbusiness.com/articles/inside-the-rise-of-bitclout-a-crypto-based-social-network-influencers-andreessen-horowitz-sequoia/#:~:text=Most%20of%20the,about%20BitClout%E2%80%99s%20users Basically, the top 10 are people who already have very high social status, and who are often impressive but primarily for reasons other than the content they create. At the core, Substack is a simple subscription service: you pay $N per month, and you get to see the person's articles. But a big part of Substack's success is that they did not just set the mechanism and forget. Their launch process was very hands-on, deliberately seeding the platform with high-quality creators, based on a very particular vision of what kind of high-quality intellectual environment they wanted to foster, including giving selected people revenue guarantees. So now, let's get to one idea that I think could work (of course, coming up with new ideas is inherently a more speculative project than criticizing existing ones, and more prone to error). Create a DAO, that is not token-based. Instead, the inspiration should be Protocol Guild: there are N members, and they can (anonymously) vote new members in and out. If N gets above ~200, consider auto-splitting it. Importantly, do not try to make the DAO universal or even industry-wide. Instead, embrace the opinionatedness. Be okay with having a dominant type of content (long-form writing, music, short-form video, long-form video, fiction, educational...), and be okay with having a dominant style (eg. country or region of origin, political viewpoint, if within crypto which projects you're most friendly to...). Hand-pick the initial membership set, in order to maximize its alignment with the desired style. The goal is to have a group that is larger than one creator and can accumulate a public brand and collectively bargain to seek revenue opportunities, but at the same time small enough that internal governance is tractable. Now, here is where the tokens come in. In general, one of my hypotheses this decade is that a large portion of effective governance mechanisms will all have the form factor of "large number of people and bots participating in a prediction market, with the output oracle being a diverse set of people optimized for mission alignment and capture resistance". In this case, what we do is: anyone can become a creator and create a creator coin, and then, if they get admitted to a creator DAO, a portion of their proceeds from the DAO are used to burn their creator coins. This way, the token speculators are NOT participating in a recursive-speculation attention game backed only by itself. Instead, they are specifically being predictors of what new creators the high-value creator DAOs will be willing to accept. At the same time, they also provide a valuable service to the creator DAOs: they are helping surface promising creators for the DAOs to choose from. So the ultimate decider of who rises and falls is not speculators, but high-value content creators (we make the assumption that good creators are also good judges of quality, which seems often true). Individual speculators can stay in the game and thrive to the extent that they do a good job of predicting the creator DAOs' actions.

1d ago

---

**[Daily General Discussion January 31, 2026](https://www.reddit.com/r/ethereum/comments/1qrucxq/daily_general_discussion_january_31_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Ethereum (ETH) news: ‘We need to prepare’ for quantum computing](https://www.coindesk.com/tech/2026/02/01/quantum-threat-gets-real-ethereum-foundation-prioritizes-security-with-leanvm-and-pq-signatures)**

Earlier in January, the Ethereum Foundation formally elevated post-quantum security to a strategic priority, creating a dedicated Post-Quantum team.

CoinDesk • 1d ago

---

**[Tom Lee's BitMine Buys the Ethereum Dip, Even as Unrealized Losses Top $6 Billion](https://finance.yahoo.com/news/tom-lees-bitmine-buys-ethereum-162425009.html)**

Publicly traded Ethereum treasury BitMine Immersion Technologies is still buying as ETH plunges, despite the firm's growing losses.

Yahoo Finance • 6h ago

---

**[Prediction: 2026 Will Be the Year of Ethereum (ETH)](https://finance.yahoo.com/news/prediction-2026-ethereum-eth-142300297.html)**

The adoption, technology, and regulation stars may all align for Ethereum this year.

Yahoo Finance • 8h ago

---

**[Ethereum Falls 10% In Rout](https://www.investing.com/news/cryptocurrency-news/ethereum-falls-10-in-rout-4477776)**

Ethereum Falls 10% In Rout

Investing.com • 19h ago

---

**[Bitcoin, XRP, Ethereum Fall on News of Kevin Warsh Fed Appointment.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-crypto-today-954298d9?gaa_at=eafs&gaa_n=AWEtsqeAASuN436_LsvGNlUdF9d4z5VeuTHilaheRouBXb_yX5w_yuxGCDQw&gaa_ts=698131e4&gaa_sig=I6YELROZzB_PqaWh57LJJtBkjFzYLG4me_eyghvmUzicwbgrcGGwGhZ_QMgsfUC61IZ2qRZ2-PC_P52Sx2luow%3D%3D)**

Barron's • 3d ago

---

**[A sudden shift in Ethereum staking is draining billions from exchanges toward a new corporate elite](https://cryptoslate.com/how-staking-turned-ethereum-into-a-treasury-trade/)**

Corporate Ethereum treasuries use staking to earn additional ETH, turning reserves into a compounding strategy instead of passive exposure.

CryptoSlate • 1d ago

---

**[Ethereum Supply Tightens With 45% of ETH Locked: Sygnum](https://thedefiant.io/news/research-and-opinion/ethereum-supply-tightens-with-45-of-eth-locked-sygnum)**

ETF buying, staking and corporate holdings continue to reduce liquid ETH.

thedefiant.io • 3d ago

---

**[Ethereum vs Bitcoin: Jack Yi Admits ETH Bull Call Came Too Soon](https://stocktwits.com/news-articles/markets/cryptocurrency/ethereum-bull-jack-yi-says-early-eth-bullish-bet-was-mistimed-and-a-mistake/cZbgN2PR4kB)**

The shift came amid heavy liquidations and market trends favoring Bitcoin under macro pressure.

Stocktwits • 12h ago

---

**[Why are Bitcoin, Ethereum and XRP Prices Crashing Today?](https://www.tradingview.com/news/coinpedia:b99ef7f8a094b:0-why-are-bitcoin-ethereum-and-xrp-prices-crashing-today/)**

The crypto market is facing a major sell-off today, with total market value dropping to $2.66 trillion, down more than 6% in the last 24 hours. Bitcoin, Ethereum, XRP and other major cryptocurrencies have all fallen sharply, wiping out nearly $500 billion from the market in just a few days.The bigg…

TradingView • 1d ago

---

**[Crypto Crash: Liquidations Top $2.5 Billion as Bitcoin, Ethereum and XRP Prices Plummet](https://finance.yahoo.com/news/crypto-crash-liquidations-top-2-203516968.html)**

The crypto market's recent decline only accelerated Saturday, with Bitcoin falling to nearly $77,000 as liquidations piled up.

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=OpRy3WJO7mA)**

Tom Lee Just Said The UNTHINKABLE About Bitcoin & Ethereum! ["It's a Fake Crash"] My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 7K • 👍 327 • 💬 66 • ⏱️ 18:04 • 7h ago

---

**[BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=ObRvo0J4ygM)**

BITCOIN CRASH JUST FLIPPED (Trading Strategy Revealed)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 2K • 👍 145 • 💬 15 • ⏱️ 23:54 • 1h ago

---

**[BITCOIN AND ETH: LAST CHANCE TO RECOVER!!!! 🚨🚨🚨 (MicroStrategy REKT)](https://www.youtube.com/watch?v=bLiHfECZH3k)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 26K • 👍 2K • 💬 196 • ⏱️ 46:08 • 13h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=fEyNvRFi_OA)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 216 • 💬 6 • ⏱️ 4:10 • 10h ago

---

**[Ethereum’s Vision Is Incredibly Bullish… So Why Is the Price So Bad? w/ Jeff Park](https://www.youtube.com/watch?v=tJLZausdujc)**

Free Milk Road Newsletters: ...

📺 Milk Road

👁️ 13K • 👍 327 • 💬 32 • ⏱️ 15:51 • 1d ago

---

**[Tom Lee Drops HUGE Warning About 2026 | The Bull Run Has CHANGED](https://www.youtube.com/watch?v=3dh-JR2mdzA)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 7K • 👍 155 • 💬 372 • ⏱️ 15:18 • 17h ago

---

**[Bitcoin, Ethereum &amp; Altcoins DOWN BAD (NOW THIS!?)](https://www.youtube.com/watch?v=CxKURlwrfIM)**

In today's video, we're breaking down why the pain for Bitcoin (BTC), Ethereum (ETH), and the broader Altcoin market might not ...

📺 Discover Crypto

👁️ 7K • 👍 429 • 💬 106 • ⏱️ 1:43:46 • 5h ago

---

**[Tom Lee: This Is a Fake Sell-off! The Bull Run Continues By THIS Date](https://www.youtube.com/watch?v=af5DO4Y_8cc)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 22K • 👍 828 • 💬 152 • ⏱️ 21:16 • 1d ago

---

**[Shorting Ethereum: My Life-Changing Trade](https://www.youtube.com/watch?v=L9tejtx7sXA)**

After getting chopped up in ETH shorts over the past few months, I found a moment of Tom Lee weakness to short ETH one last ...

📺 Taiki Maeda

👁️ 12K • 👍 650 • 💬 264 • ⏱️ 48:54 • 1d ago

---

**[WILL ETH CRASH LOWER?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=lhB4BzX0HCQ)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 507 • 👍 16 • 💬 5 • ⏱️ 5:10 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
