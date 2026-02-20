---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-20T13:01:35.076436+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- videos
- news
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 20, 2026 at 13:01 UTC  
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

### $1,971.43

---

## Ethereum Chart

**24h:** +0.5%  
**7d:** -6.6%  
**30d:** -34.0%  
**90d:** -30.5%  
**1y:** -26.7%  

---

## Ethereum Market Stats

**Market Cap:** $235.17B
Rank #2

**Circulating Supply:** 120,692,388 ETH
No max supply

**All-Time High:** $4,946.05
-60.6%

**All-Time Low:** $0.43
+449944.9%

---

## Reddit: r/ethereum

**[Daily General Discussion February 20, 2026](https://www.reddit.com/r/ethereum/comments/1r9nfzz/daily_general_discussion_february_20_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

7h ago

---

**[Vitalik Pushes Back on “Sovereign AI” as Web4 Essay Sparks Debate](https://www.reddit.com/r/ethereum/comments/1r9rnmm/vitalik_pushes_back_on_sovereign_ai_as_web4_essay/)**

Vitalik Buterin challenges the Web4 “sovereign AI” narrative, warning that expanding AI autonomy without strong human alignment could increase systemic risk as crypto and AI converge.

🔗 [EtherWorld.co](https://etherworld.co/vitalik-pushes-back-on-sovereign-ai-as-web4-essay-sparks-debate/) • 2h ago

---

**[Justin Drake dives deep into Lean Ethereum](https://www.reddit.com/r/ethereum/comments/1r9qidy/justin_drake_dives_deep_into_lean_ethereum/)**

Justin Drake dives deep into Lean Ethereum In this episode (which is the first in a six-part series on Lean Ethereum) we covered: - This vision for ethereum, spanning the consensus, data, and execution layers. - How post-quantum cryptography, faster finality, and enshrined ZK are all being used to future-proof Ethereum’s core. They also lay out some of the topics that will be covered in subsequent parts of the series. Listen here

3h ago

---

**[Wall Street giants massively increased holdings in BitMine — the largest corporate ETH holder](https://www.reddit.com/r/ethereum/comments/1r93mxh/wall_street_giants_massively_increased_holdings/)**

New 13F filings show major financial institutions sharply increased positions in BitMine, a public company widely known as the largest corporate holder of Ethereum. Morgan Stanley now holds 12.2M shares (+26%), ARK 9.5M (+27%), BlackRock 9M (+166%), and Goldman Sachs 5.2M (+588%). Vanguard, Bank of America, Schwab, RBC, Citi and BNY Mellon also expanded exposure. In total, 457 institutional holders now control about 136.7M BitMine shares (~$2.86B). This suggests institutions are increasingly accessing ETH exposure via equity structures rather than direct custody — similar to how MicroStrategy functions as a BTC proxy. Full breakdown: https://btcusa.com/wall-street-giants-boost-bitmine-holdings-as-institutional-ethereum-exposure-expands/ Curious how people here see this trend — does equity-based ETH exposure accelerate or delay direct institutional ETH ownership?

20h ago

---

**[Ethereal news weekly #12 | FOCIL is Hegotá consensus layer headliner, EF protocol priorities: Scale, Improve UX & Harden the L1, Base moving to own stack](https://www.reddit.com/r/ethereum/comments/1r9sy7v/ethereal_news_weekly_12_focil_is_hegotá_consensus/)**

FOCIL is Hegotá consensus layer headliner, EF protocol priorities: Scale, Improve UX & Harden the L1, Base moving to own stack

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-12/) • 1h ago

---

**[Vibehouse: Ethereum’s Vibecoded Consensus Client from Lighthouse](https://www.reddit.com/r/ethereum/comments/1r9rytg/vibehouse_ethereums_vibecoded_consensus_client/)**

Vibehouse, an AI generated fork of Lighthouse, implemented ePBS in 72 hours and passed consensus tests on a multi node devnet.

🔗 [EtherWorld.co](https://etherworld.co/vibehouse-ethereums-vibecoded-consensus-client-from-lighthouse/) • 2h ago

---

**[On FOCIL and native AA synergies](https://www.reddit.com/r/ethereum/comments/1r980ut/on_focil_and_native_aa_synergies/)**

There is an important synergy between FOCIL and AA (EIP-8141, which is based on 7701): 8141 makes not just smart accounts (including multisig, quantum-resistant signatures, key changes, gas sponsorship) first-class citizens, it also can do the same for privacy protocols (either indirectly via paymaster, or if we add 2D nonces, directly as a multi-tenant account). "First-class citizen" means that operations sent from that account can be included directly onchain as transactions, with no wrappers. FOCIL enables censorship-resistant rapid inclusion of any transaction. Hence, with FOCIL and 8141 together, anything, including smart wallet txs, gas sponsored txs, and even privacy protocol txs, can be included onchain through one of 17 different actors (the proposer or the includers) that are all chosen randomly in each slot. This gives us guaranteed rapid inclusion, meaning almost certainly within 1-2 slots, of any such tx, even in an adversarial environment. In this iteration, the FOCILs are 8 kB each, so they are very small in size. However, there is a natural future extension path to making them much larger, so that the majority of transactions to a block could, if needed, come through FOCILs. Such a design would have many of the properties of multiple concurrent proposer (MCP) designs, with the key difference being that FOCILs do not try to control the MEV-relevant "last look" role - that's still auctioned off with ePBS. The behavior of the last look role in "full MCP" depends strongly on the specifics of the design. The FOCIL design ensures that even if literally 100% of all slots get sold off via proposer-builder separation to a hostile actor that refuses to connect to public mempools, discriminates against certain applications, or is otherwise abusive, all transactions can still get quickly included. It's not eliminating the centralization of the proposer role, but it is heavily disempowering it. With EIP-8141 (AA), transactions from smart wallets, privacy protocols, etc, could be sent through a public mempool, and directly received by a FOCIL includer, no wrappers, "public broadcasters", or other intermediaries required. Ethereum is going hard.

18h ago

---

**[Daily General Discussion February 19, 2026](https://www.reddit.com/r/ethereum/comments/1r8rcjv/daily_general_discussion_february_19_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Highlights from the All Core Developers Consensus (ACDC) Call #175](https://www.reddit.com/r/ethereum/comments/1r9ix9b/highlights_from_the_all_core_developers_consensus/)**

ACDC #175 saw steady progress on Glamsterdam’s ePBS Devnet and the formal selection of FOCIL as Hegotá’s Consensus Layer headliner.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-consensus-acdc-call-175/) • 10h ago

---

**[How much do you know about Ethereum ?](https://www.reddit.com/r/ethereum/comments/1r9msb7/how_much_do_you_know_about_ethereum/)**

7h ago

---

---

## Google News: "ethereum"

**[Harvard shakes up its crypto strategy by selling Bitcoin and purchasing Ethereum](https://fortune.com/2026/02/18/harvard-shakes-up-its-crypto-strategy/)**

The Ivy League school still has more money invested in Bitcoin than any other US stock.

Fortune • 1d ago

---

**[Peter Thiel and Founders Fund exit Ethereum treasury firm ETHZilla, SEC filing shows](https://www.theblock.co/post/390285/peter-thiel-and-founders-fund-exit-ethereum-treasury-firm-ethzilla-sec-filing-shows)**

Peter Thiel fully exits ETHZilla, filing shows, as shares slide and the firm shifts from ether buildup to tokenization.

The Block • 2d ago

---

**[Peter Thiel Exits ETHZilla Investment After Ethereum Treasury Stock Craters](https://finance.yahoo.com/news/peter-thiel-exits-ethzilla-investment-210444026.html)**

Billionaire investor Peter Thiel and Founders Fund held a 7.5% stake in Ethereum treasury company ETHZilla last year—but not anymore.

Yahoo Finance • 1d ago

---

**[Peter Thiel Exits ETHZilla Investment After Ethereum Treasury Stock Craters](https://decrypt.co/358468/peter-thiel-exits-ethzilla-investment-ethereum-treasury-stock-craters)**

Billionaire investor Peter Thiel and Founders Fund held a 7.5% stake in Ethereum treasury company ETHZilla last year—but not anymore.

Decrypt • 1d ago

---

**[Dual South Korean listings send Ethereum layer-2 token AZTEC surging 82%](https://www.coindesk.com/markets/2026/02/20/dual-s-korea-listings-send-ethereum-layer-2-token-aztec-surging-82)**

Korean exchanges Upbit and Bithumb both added local currency pairs for the privacy-focused layer-2 token, triggering a sharp move in a thinly traded market.

CoinDesk • 1h ago

---

**[Ethereum Struggles Below $2,000, Yet BitMine Sees Rebound: Here’s What They’re Watching](https://finance.yahoo.com/news/ethereum-struggles-below-2-000-094348887.html)**

Ethereum trades below realized price as BitMine doubles down on accumulation, citing historical rebound patterns despite paper losses.

Yahoo Finance • 3h ago

---

**[The Ethereum creator and early Polymarket backer doesn't like the direction prediction markets are headed](https://www.businessinsider.com/ethereum-creator-polymarket-backer-raises-concern-about-prediction-markets-future-2026-2)**

Vitalik Buterin, an early Polymarket backer, said prediction markets risk devolving into "corposlop" rather than having long-term financial utility.

Business Insider • 2d ago

---

**[BlackRock begins acquiring ETH for upcoming Ethereum staking ETF](https://www.theblock.co/post/390244/blackrock-begins-acquiring-eth-upcoming-ethereum-staking-etf)**

A BlackRock affiliate purchased 4,000 seed shares of the fund for $100,000, providing the initial capital the trust will use to purchase ether, according to an amended S-1 filing.

The Block • 2d ago

---

**[Bitcoin, Ethereum, XRP Waffle as Crypto Crisis Deepens. Why It Could Get Worse.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-crypto-crisis-e43f4227?gaa_at=eafs&gaa_n=AWEtsqd7nLKlYKoM_CyRwPbQayeQRB4B1qu9QhHu3nmhHqDIm9Ab8CK172sy&gaa_ts=69985e92&gaa_sig=qwBaw8Gjh3xcwcm8PlM_3f93evjgF0x9_LXoCn7j7rI7_N9wCZHF1GJaJdraYBKYB-yGs1ovurGVHFB0WlaV8w%3D%3D)**

Barron's • 15h ago

---

**[Bitmine Immersion: Ethereum's Biggest Public Whale (NYSE:BMNR)](https://seekingalpha.com/article/4871611-bitmine-immersion-ethereum-biggest-public-whale)**

Asymmetric upside for Bitmine Immersion Technologies is likely if Ethereum (and the whole crypto space) recovers from the recent downtrend. More on BMNR stock.

Seeking Alpha • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Blackrock Ethereum ETF SUBMITTED (Major Price Reaction)](https://www.youtube.com/watch?v=IDB13BcKlLE)**

Nick Valdez looks at the VERY bullish news regarding Blackrock and Ethereum. But the charts aren't as bullish! Will the bulls or ...

📺 Discover Crypto

👁️ 4K • 👍 107 • 💬 34 • ⏱️ 4:54 • 14h ago

---

**[Coinbase Moves To ETH!🔥Robinhood vs Coinbase🔥SHOTS FIRED!](https://www.youtube.com/watch?v=jSKfTE-aZBQ)**

Optimism has plunged to a new all-time low after intense selling pressure overwhelmed recent demand. The decline accelerated ...

📺 Paul Barron Network

👁️ 47K • 👍 2K • 💬 149 • ⏱️ 15:12 • 16h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=UB5auWMWxOg)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 460 • 👍 61 • 💬 2 • ⏱️ 6:09 • 1h ago

---

**[The Next Phase of Ethereum: Prediction from Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=uwpXnuUsoiM)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 4K • 👍 72 • 💬 6 • ⏱️ 18:58 • 1d ago

---

**[🚨 BREAKING: Deep State 911 Insider BUYS ETHEREUM (Howard Lutnick) ($20K ETH) (Tom Lee)](https://www.youtube.com/watch?v=F22KAmIsKd4)**

Donation Address: yourfriendsommi.eth / yourfriendsommi.pls Click Subscribe + Bell Button 'All' Follow on Twitter: ...

📺 🌟yourfriendsommi

👁️ 1K • 👍 170 • 💬 16 • ⏱️ 16:03 • 9h ago

---

**[Tom Lee: The 44x Opportunity EVEN Bigger Than Bitcoin (2026 Prediction)](https://www.youtube.com/watch?v=DAkb7jk3oUE)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Claim your $20 Kalshi bonus when you ...

📺 Crypto Nutshell

👁️ 12K • 👍 441 • 💬 28 • ⏱️ 21:01 • 21h ago

---

**[ETH BOTTOM PATTERN FORMED!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=TJNwtdERzRY)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 69 • 👍 10 • 💬 2 • ⏱️ 4:18 • 2h ago

---

**[☠️ Is Ethereum going to ZERO? (DOWN in 12 of 15 months) !?](https://www.youtube.com/watch?v=Cg8VY5MS-Wc)**

Donation Address: yourfriendsommi.eth / yourfriendsommi.pls Click Subscribe + Bell Button 'All' Follow on Twitter: ...

📺 🌟yourfriendsommi

👁️ 418 • 👍 76 • 💬 9 • ⏱️ 10:02 • 2h ago

---

**[Raoul Pal: Don&#39;t SELL Before These EXACT Dates (New 2026 Bitcoin &amp; Ethereum Prediction)](https://www.youtube.com/watch?v=7S8_zqg7o8A)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Claim your $20 Kalshi bonus when you ...

📺 Crypto Nutshell

👁️ 21K • 👍 718 • 💬 46 • ⏱️ 21:56 • 1d ago

---

**[SUPER INVESTOR JUST SOLD HIS ENTIRE ETHEREUM POSITION](https://www.youtube.com/watch?v=Wsk-n6e2dh0)**

CHECK OUT MY LINKTREE FOR EXCHANGES I USE, BONUSES, FREE VIDEOS, AND MORE! https://linktr.ee/Myfinancialfriend I ...

📺 My Financial Friend

👁️ 7K • 👍 320 • 💬 35 • ⏱️ 12:25 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
