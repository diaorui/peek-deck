---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-10T10:40:38.968851+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- videos
- social
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 10, 2026 at 10:40 UTC  
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

### $2,046.70

---

## Ethereum Chart

**24h:** +3.6%  
**7d:** -2.9%  
**30d:** -1.8%  
**90d:** -36.1%  
**1y:** +7.1%  

---

## Ethereum Market Stats

**Market Cap:** $249.56B
Rank #2

**Circulating Supply:** 120,692,025 ETH
No max supply

**All-Time High:** $4,946.05
-58.2%

**All-Time Low:** $0.43
+477470.5%

---

## Reddit: r/ethereum

**[Daily General Discussion March 10, 2026](https://www.reddit.com/r/ethereum/comments/1rpnx4z/daily_general_discussion_march_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

5h ago

---

**[Lighthouse v8.1.2: high-priority patch release with further security-critical fixes atop v8.1.1.](https://www.reddit.com/r/ethereum/comments/1rphl02/lighthouse_v812_highpriority_patch_release_with/)**

Summary
⚠️ Lighthouse v8.1.2 is a high-priority patch release with further security-critical fixes atop v8.1.1.
This is a mandatory upgrade for all users running any prior version. All prior Lighth...

🔗 [GitHub](https://github.com/sigp/lighthouse/releases/tag/v8.1.2) • 10h ago

---

**[TIL about MessageStore, a 1-function contract from August 2015 (block 53,573)](https://www.reddit.com/r/ethereum/comments/1rp2kko/til_about_messagestore_a_1function_contract_from/)**

Was digging through Ethereum's earliest blocks and found this contract at 0xd2ec...3d6b, deployed in August 2015, just weeks after mainnet launch. The entire contract is one function: set(string). It stores a single string in public storage. That is it. What is interesting is the bytecode. It was compiled with solc v0.1.1, the earliest Solidity compiler that exists. I was able to reproduce the exact bytecode byte-for-byte using that compiler. The output matches the on-chain code perfectly. Contracts from this era are fascinating because Solidity was still being invented. No events, no modifiers, no constructors as we know them. Just raw storage writes. The compiler output is so small you can read the opcodes manually. The deployer (0x8674...94e2) deployed 18 contracts in the same week, all in the 52,000-55,000 block range. Looks like someone was experimenting heavily with what Solidity could do. If anyone is interested in early Ethereum archaeology, ethereumhistory.com is documenting contracts from this period with verified source code and compiler proofs. Edit: here is the contract page on Ethereum History.

19h ago

---

**[Daily General Discussion March 09, 2026](https://www.reddit.com/r/ethereum/comments/1ror68i/daily_general_discussion_march_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Before ENS, there was GlobalRegistrar — Ethereum's first naming system (Sep 24, 2015)](https://www.reddit.com/r/ethereum/comments/1rozkho/before_ens_there_was_globalregistrar_ethereums/)**

In September 2015, six weeks after mainnet launch, someone deployed three contracts that became Ethereum's first naming infrastructure: GlobalRegistrar, HashReg, and UrlHint. Block 282,880 — September 24, 2015 The GlobalRegistrar mapped names to addresses. HashReg mapped code hashes to content hashes. UrlHint mapped content hashes to URLs for metadata retrieval. Together they formed the NatSpec documentation system — the mechanism that was supposed to let Ethereum wallets display human-readable descriptions before signing transactions. The system was hardcoded directly into go-ethereum v1.4.0 (common/registrar/registrar.go). Not an optional plugin. Core infrastructure. The frozen TODO that became ENS Inside the GlobalRegistrar source code (verified on Etherscan, compiled with solc v0.1.1), there's a comment that reads: // TODO: bidding mechanism That comment sat frozen for years. The ambition was there — first-come-first-served registration was always meant to be a placeholder. The bidding mechanism didn't arrive until ENS launched in May 2017, when Vickrey auctions replaced the naive assignment system. ENS didn't appear from nowhere. It solved the exact problem the GlobalRegistrar identified and couldn't finish. The three-contract system All three contracts were deployed by the same address within 18 blocks: - GlobalRegistrar: block 282,880 - HashReg: block 282,885 (5 blocks later) - UrlHint: block 282,898 (18 blocks after start) The deployer identity isn't confirmed — likely a go-ethereum core developer given the contracts were shipped alongside the go-ethereum codebase — but we haven't pinned the address to a name yet. Why it matters Every .eth name you resolve today is the descendant of that frozen TODO comment from 2015. The naming problem was understood from week six. It took two more years to solve it properly. We documented all three contracts on EthereumHistory.com last night. The verified source code, links to go-ethereum v1.4.0, and the full historical context are there if you want to dig deeper. Cross-posted from our ongoing archaeology of early mainnet contracts. If you deployed or used these contracts in 2015, we'd love to hear the story.

21h ago

---

**[AI Is Not Ready for Ethereum Security Audits: A Test](https://www.reddit.com/r/ethereum/comments/1rp189f/ai_is_not_ready_for_ethereum_security_audits_a/)**

MAGIC Grants | Charity for scholarships, public cryptocurrency infrastructure, and educational materials

🔗 [magicgrants.org](https://magicgrants.org/2026/03/09/AI-Not-Ready-for-Ethereum-Audits) • 20h ago

---

**[I've been reverse-engineering Ethereum's earliest smart contracts — here's what I found locked inside them](https://www.reddit.com/r/ethereum/comments/1ro4bt9/ive_been_reverseengineering_ethereums_earliest/)**

For the past few months I've been building EthereumHistory.com, a project to document every notable smart contract from Ethereum's earliest days (2015-2017). Think of it as a Wikipedia for Ethereum's contract archaeology. Recently I did a deep scan of all 12,609 contracts deployed during the Frontier era and found 1,650 still holding ETH — totaling over 38,000 ETH (~$95M at current prices) locked in contracts from Ethereum's first weeks. Here's what's actually inside them: The Gambling Contracts (Day 13 of Ethereum) EtherDice (0xc4c51de1abf5d60dbd329ec0f999fd8f021ae9fc) was deployed on August 12, 2015 — just 13 days after Ethereum launched. Someone loaded it with a 1,000 ETH bankroll. It's a 21-function commit-reveal dice game, surprisingly sophisticated for the era. 122 ETH still sits inside, permanently locked because the deployer likely lost their keys years ago. The Inverted Timelock TimeLockVault (0xed44f3c2081480b08643fe1ca281fab9ed643735) has a beautiful bug: the time check is inverted. You can withdraw before the unlock date (2035), but once 2035 arrives, the funds become permanently locked. 50 ETH inside. The deployer could have withdrawn years ago but apparently never noticed. The Stalled Pyramid EtherPyramid (0xa9e4e3b1da2752aea980698c335e70e9ab26c) had 140 participants. 136 of them are still waiting for their payout. 37 ETH frozen forever in a pyramid that ran out of new entrants. A time capsule of early Ethereum's Wild West era. The Pattern After scanning all 1,650 funded contracts, the pattern is consistent: every single one is either owner-gated (keys likely lost), bug-locked, pyramid-stalled, or timelocked. At least 5 active hunter addresses have already probed most of these contracts looking for extractable funds. None succeeded. These contracts are essentially digital fossils — permanently preserved on-chain with real ETH sealed inside them. They tell the story of Ethereum's earliest developers experimenting with code that would handle real money, often for the first time. I've been documenting these on EthereumHistory.com with verified source code, deployment context, and the stories behind them. If you deployed contracts in 2015-2016 or know the stories behind any early projects, I'd love to hear from you. What early Ethereum contracts do you remember that deserve to be documented?

1d ago

---

**[Daily General Discussion March 08, 2026](https://www.reddit.com/r/ethereum/comments/1rnwyac/daily_general_discussion_march_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[StarkWare just killed their entire user base](https://www.reddit.com/r/ethereum/comments/1rnyelp/starkware_just_killed_their_entire_user_base/)**

"a practical compliance framework that enables an auditing entity to selectively unshield transactions upon legitimate regulatory request" So, the entire point of using the chain is null and void. What's the use of hiding transactions when an arbitrary entity can just... unhide them? "For compliance, each user registers an encrypted copy of their viewing key on-chain. Upon legitimate regulatory request, a designated auditing entity can decrypt this key to trace a specific user’s transaction history, without affecting the privacy of uninvolved users." So it is effectively mandatory. Wonderful. Who did they think we were hiding transactions from, our ex? The paper: https://eprint.iacr.org/2026/474

2d ago

---

**[Is compound finance frontend or dns setup got hacked?](https://www.reddit.com/r/ethereum/comments/1ro2xqv/is_compound_finance_frontend_or_dns_setup_got/)**

I tried to access compound.finance, and when connecting wallet it warns me the domain has very low popularity. I carefully review it and found out when launching app, it actually got redirected to app.compoond.finance, which is extremely sketchy. I tried enter the website through google, and typing manually in browser, and enable secure dns, and access it on my phone. But the result is the same, when open the app function, I still got redirected to a very phishing like link https://app.compoond.finance/ I just did a whois lookup, the compoond is just registered yesterday, so a huge red flag! Anyone know what is going on?

1d ago

---

---

## Google News: "ethereum"

**[Ethereum Rises to $2,000 as Tom Lee's BitMine Tops Up $9 Billion ETH Treasury](https://decrypt.co/360405/ethereum-rises-2000-tom-lee-bitmine-9-billion-treasury)**

The price of Ethereum is up 4% over the last day, rebounding after a weekend slump under $2,000 as BitMine reveals its latest ETH buy.

Decrypt • 20h ago

---

**[Bitcoin Surges Past $70,000. Ethereum, XRP Rise as Cryptos Get a Trump Boost.](https://www.barrons.com/articles/bitcoin-price-ethereum-xrp-crypto-trump-25631f51?gaa_at=eafs&gaa_n=AWEtsqftBzhcEokBOy5MiYuogj5wWutYyqE97P6hLCB1UTtb4VvO3O8QB15T&gaa_ts=69afebb5&gaa_sig=QWQXdV41tAVwHiSHPP3SMA19lCrx_1RWcNDZLRlBF3OP3qTgGNTMUrcZiFoGEeBtS-kM9xmyb1zBoEGvE4OmSg%3D%3D)**

Barron's • 1h ago

---

**[SharpLink And $735M ‘Paper’ Loss: Is The “Strategy” of Ethereum Suffering?](https://finance.yahoo.com/news/sharplink-735m-paper-loss-strategy-082842309.html)**

Bitcoin is starting the week on the wrong foot, as BTC USD tumbled below $68,000 amid geopolitical panic that is sending shockwaves through global markets. The trigger was a violent spike in energy markets over the weekend, with April WTI crude oil futures exploding 19.1% higher to $108.35 per barrel ...

Yahoo Finance • 2h ago

---

**[Ethereum (ETH) Below $2,000 Looks Increasingly Likely as Oil Prices Surge and Crypto Confidence Declines](https://www.ccn.com/analysis/crypto/ethereum-eth-below-2000-looks-increasingly-likely/)**

CCN.com • 11h ago

---

**[Ethereum Price Defends $2,000 Support as RSI Hits Near-Oversold Levels](https://finance.yahoo.com/news/ethereum-price-defends-2-000-071818617.html)**

The Ethereum price is fighting to hold the $2,000 line as sellers test the market’s resolve. The asset is trading at $2,050 with a weekly Relative Strength Index (RSI) of 33, signaling a crucial decision point.$2,000 represents a longstanding psychological level that bulls have defended since the February lows. The ...

Yahoo Finance • 3h ago

---

**[Ethereum Price Tries to Defend $1,900 Support amid $157 Million Co-Founder Selloff](https://www.tipranks.com/news/ethereum-price-tries-to-defend-1900-support-amid-157-million-co-founder-selloff)**

TipRanks • 1d ago

---

**[Claude AI Predicts the Price of Bitcoin and Ethereum If the Middle East Conflict Escalates](https://www.binance.com/en/square/post/299085766882482)**

Binance • 2d ago

---

**[Where Will Ethereum Be in 2030?](https://www.fool.com/investing/2026/03/08/where-will-ethereum-be-in-2030/)**

As long as Ethereum can maintain its dominance in decentralized finance (DeFi), the sky is the limit.

The Motley Fool • 1d ago

---

**[Bitmine Vs. Sharplink: One Is A Dilution Trap, The Other Is The Better Ethereum Proxy](https://seekingalpha.com/article/4879983-bitmine-vs-sharplink-one-is-a-dilution-trap-the-other-is-the-better-ethereum-proxy)**

Seeking Alpha • 1d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.535 Million Tokens, and Total Crypto and Total Cash Holdings of $10.3 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-535-million-tokens-and-total-crypto-and-total-cash-holdings-of-10-3-billion-302708118.html)**

Bitmine has 3,040,483 staked ETH, representing $6.0 billion at $1,965 per ETH; MAVAN staking solution on track to launch Q1 2026 Bitmine now owns 3.76% of the...

PR Newswire • 22h ago

---

---

## YouTube Videos: "ethereum"

**[Bitcoin &amp; Ethereum Are About To Wake Up (Watch Immediately)](https://www.youtube.com/watch?v=4nDVYeU6SRw)**

GET IN EARLY! Crypto Is About To Wake Up! ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily BTC Conference ...

📺 Altcoin Daily

👁️ 36K • 👍 2K • 💬 182 • ⏱️ 9:54 • 12h ago

---

**[ETHEREUM ABOUT TO BREAKOUT?🔥 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=xTat0Edjfco)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 8 • ⏱️ 5:18 • 1h ago

---

**[BITCOIN PRICE JUST FLIPPED (This is Next)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=i7V9o6KPUgs)**

BITCOIN PRICE JUST FLIPPED (This is Next)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* https://bit.ly/TOOBIT ...

📺 Crypto World

👁️ 6K • 👍 238 • 💬 306 • ⏱️ 14:42 • 13h ago

---

**[Tom Lee - &quot;Largest Crypto Reset In HISTORY&quot; | Bitcoin &amp; ETH Price Prediction](https://www.youtube.com/watch?v=43KC2TkH8hk)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 8K • 👍 174 • 💬 118 • ⏱️ 15:06 • 2d ago

---

**[Bitcoin &amp; Ethereum Are About To Explode (SERIOUSLY)](https://www.youtube.com/watch?v=i5mW_EafMaI)**

Crypto Is About To Surprise EVERYONE!! (SERIOUSLY) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 49K • 👍 2K • 💬 161 • ⏱️ 11:32 • 2d ago

---

**[This Could Cause A MAJOR ETHEREUM CRASH](https://www.youtube.com/watch?v=Y6BXExs5_aI)**

Get $450 Off Our New AI Indicators: https://tradeconfidentportal.io/indicators Join Trade Confident: Get 25% Off Your 1st Month: ...

📺 Trade Confident

👁️ 282 • 👍 18 • 💬 27 • ⏱️ 5:59 • 15h ago

---

**[America’s Bankification of Crypto Has Started](https://www.youtube.com/watch?v=XtTl3uYRKS8)**

Get 30% off your Tangem Wallet + free Bitcoin: ...

📺 Cyber Scrilla

👁️ 21K • 👍 1K • 💬 166 • ⏱️ 11:55 • 1d ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=zyMS-MAg8UI)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 592 • 👍 61 • ⏱️ 5:31 • 5h ago

---

**[Ethereum To 85x From Here? Cathie Wood ETH Price Targets Are Insane!](https://www.youtube.com/watch?v=Qn2OgJ2Q_ZQ)**

Cathie Wood legitimately thinks that Ethereum can do a 85x from now until 2032. Sound insane? Here's her entire thesis.

📺 Zach Humphries

👁️ 3K • 👍 130 • 💬 14 • ⏱️ 7:38 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=iUcsXE5JWns)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 142 • 💬 6 • ⏱️ 4:08 • 21h ago

---

---

*Generated by PeekDeck - A glance is all you need*
