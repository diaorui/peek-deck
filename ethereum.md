---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-10T13:03:46.049960+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- social
- cryptocurrency
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 10, 2026 at 13:03 UTC  
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

### $2,054.18

---

## Ethereum Chart

**24h:** +1.5%  
**7d:** -3.6%  
**30d:** -2.5%  
**90d:** -36.6%  
**1y:** +6.3%  

---

## Ethereum Market Stats

**Market Cap:** $247.59B
Rank #2

**Circulating Supply:** 120,692,025 ETH
No max supply

**All-Time High:** $4,946.05
-58.5%

**All-Time Low:** $0.43
+473657.4%

---

## Reddit: r/ethereum

**[Daily General Discussion March 10, 2026](https://www.reddit.com/r/ethereum/comments/1rpnx4z/daily_general_discussion_march_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

8h ago

---

**[Ethereum's Top Corporate Whale Fattens Up with $10bn Treasury Holding](https://www.reddit.com/r/ethereum/comments/1rpv1ia/ethereums_top_corporate_whale_fattens_up_with/)**

Bitmine Immersion Technologies (BMNR) is expanding beyond its origins as a Bitcoin miner to consolidate as the world's largest corporate holder of Ether (ETH). : Get all the latest crypto news at Sandmark

🔗 [Sandmark](https://www.sandmark.com/news/top-news/ethereums-top-corporate-whale-fattens-10bn-treasury-holding) • 1h ago

---

**[Lighthouse v8.1.2: high-priority patch release with further security-critical fixes atop v8.1.1.](https://www.reddit.com/r/ethereum/comments/1rphl02/lighthouse_v812_highpriority_patch_release_with/)**

Summary
⚠️ Lighthouse v8.1.2 is a high-priority patch release with further security-critical fixes atop v8.1.1.
This is a mandatory upgrade for all users running any prior version. All prior Lighth...

🔗 [GitHub](https://github.com/sigp/lighthouse/releases/tag/v8.1.2) • 12h ago

---

**[TIL about MessageStore, a 1-function contract from August 2015 (block 53,573)](https://www.reddit.com/r/ethereum/comments/1rp2kko/til_about_messagestore_a_1function_contract_from/)**

Was digging through Ethereum's earliest blocks and found this contract at 0xd2ec...3d6b, deployed in August 2015, just weeks after mainnet launch. The entire contract is one function: set(string). It stores a single string in public storage. That is it. What is interesting is the bytecode. It was compiled with solc v0.1.1, the earliest Solidity compiler that exists. I was able to reproduce the exact bytecode byte-for-byte using that compiler. The output matches the on-chain code perfectly. Contracts from this era are fascinating because Solidity was still being invented. No events, no modifiers, no constructors as we know them. Just raw storage writes. The compiler output is so small you can read the opcodes manually. The deployer (0x8674...94e2) deployed 18 contracts in the same week, all in the 52,000-55,000 block range. Looks like someone was experimenting heavily with what Solidity could do. If anyone is interested in early Ethereum archaeology, ethereumhistory.com is documenting contracts from this period with verified source code and compiler proofs. Edit: here is the contract page on Ethereum History.

22h ago

---

**[Daily General Discussion March 09, 2026](https://www.reddit.com/r/ethereum/comments/1ror68i/daily_general_discussion_march_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Before ENS, there was GlobalRegistrar — Ethereum's first naming system (Sep 24, 2015)](https://www.reddit.com/r/ethereum/comments/1rozkho/before_ens_there_was_globalregistrar_ethereums/)**

In September 2015, six weeks after mainnet launch, someone deployed three contracts that became Ethereum's first naming infrastructure: GlobalRegistrar, HashReg, and UrlHint. Block 282,880 — September 24, 2015 The GlobalRegistrar mapped names to addresses. HashReg mapped code hashes to content hashes. UrlHint mapped content hashes to URLs for metadata retrieval. Together they formed the NatSpec documentation system — the mechanism that was supposed to let Ethereum wallets display human-readable descriptions before signing transactions. The system was hardcoded directly into go-ethereum v1.4.0 (common/registrar/registrar.go). Not an optional plugin. Core infrastructure. The frozen TODO that became ENS Inside the GlobalRegistrar source code (verified on Etherscan, compiled with solc v0.1.1), there's a comment that reads: // TODO: bidding mechanism That comment sat frozen for years. The ambition was there — first-come-first-served registration was always meant to be a placeholder. The bidding mechanism didn't arrive until ENS launched in May 2017, when Vickrey auctions replaced the naive assignment system. ENS didn't appear from nowhere. It solved the exact problem the GlobalRegistrar identified and couldn't finish. The three-contract system All three contracts were deployed by the same address within 18 blocks: - GlobalRegistrar: block 282,880 - HashReg: block 282,885 (5 blocks later) - UrlHint: block 282,898 (18 blocks after start) The deployer identity isn't confirmed — likely a go-ethereum core developer given the contracts were shipped alongside the go-ethereum codebase — but we haven't pinned the address to a name yet. Why it matters Every .eth name you resolve today is the descendant of that frozen TODO comment from 2015. The naming problem was understood from week six. It took two more years to solve it properly. We documented all three contracts on EthereumHistory.com last night. The verified source code, links to go-ethereum v1.4.0, and the full historical context are there if you want to dig deeper. Cross-posted from our ongoing archaeology of early mainnet contracts. If you deployed or used these contracts in 2015, we'd love to hear the story.

1d ago

---

**[AI Is Not Ready for Ethereum Security Audits: A Test](https://www.reddit.com/r/ethereum/comments/1rp189f/ai_is_not_ready_for_ethereum_security_audits_a/)**

MAGIC Grants | Charity for scholarships, public cryptocurrency infrastructure, and educational materials

🔗 [magicgrants.org](https://magicgrants.org/2026/03/09/AI-Not-Ready-for-Ethereum-Audits) • 22h ago

---

**[I've been reverse-engineering Ethereum's earliest smart contracts — here's what I found locked inside them](https://www.reddit.com/r/ethereum/comments/1ro4bt9/ive_been_reverseengineering_ethereums_earliest/)**

For the past few months I've been building EthereumHistory.com, a project to document every notable smart contract from Ethereum's earliest days (2015-2017). Think of it as a Wikipedia for Ethereum's contract archaeology. Recently I did a deep scan of all 12,609 contracts deployed during the Frontier era and found 1,650 still holding ETH — totaling over 38,000 ETH (~$95M at current prices) locked in contracts from Ethereum's first weeks. Here's what's actually inside them: The Gambling Contracts (Day 13 of Ethereum) EtherDice (0xc4c51de1abf5d60dbd329ec0f999fd8f021ae9fc) was deployed on August 12, 2015 — just 13 days after Ethereum launched. Someone loaded it with a 1,000 ETH bankroll. It's a 21-function commit-reveal dice game, surprisingly sophisticated for the era. 122 ETH still sits inside, permanently locked because the deployer likely lost their keys years ago. The Inverted Timelock TimeLockVault (0xed44f3c2081480b08643fe1ca281fab9ed643735) has a beautiful bug: the time check is inverted. You can withdraw before the unlock date (2035), but once 2035 arrives, the funds become permanently locked. 50 ETH inside. The deployer could have withdrawn years ago but apparently never noticed. The Stalled Pyramid EtherPyramid (0xa9e4e3b1da2752aea980698c335e70e9ab26c) had 140 participants. 136 of them are still waiting for their payout. 37 ETH frozen forever in a pyramid that ran out of new entrants. A time capsule of early Ethereum's Wild West era. The Pattern After scanning all 1,650 funded contracts, the pattern is consistent: every single one is either owner-gated (keys likely lost), bug-locked, pyramid-stalled, or timelocked. At least 5 active hunter addresses have already probed most of these contracts looking for extractable funds. None succeeded. These contracts are essentially digital fossils — permanently preserved on-chain with real ETH sealed inside them. They tell the story of Ethereum's earliest developers experimenting with code that would handle real money, often for the first time. I've been documenting these on EthereumHistory.com with verified source code, deployment context, and the stories behind them. If you deployed contracts in 2015-2016 or know the stories behind any early projects, I'd love to hear from you. What early Ethereum contracts do you remember that deserve to be documented?

2d ago

---

**[Daily General Discussion March 08, 2026](https://www.reddit.com/r/ethereum/comments/1rnwyac/daily_general_discussion_march_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[StarkWare just killed their entire user base](https://www.reddit.com/r/ethereum/comments/1rnyelp/starkware_just_killed_their_entire_user_base/)**

"a practical compliance framework that enables an auditing entity to selectively unshield transactions upon legitimate regulatory request" So, the entire point of using the chain is null and void. What's the use of hiding transactions when an arbitrary entity can just... unhide them? "For compliance, each user registers an encrypted copy of their viewing key on-chain. Upon legitimate regulatory request, a designated auditing entity can decrypt this key to trace a specific user’s transaction history, without affecting the privacy of uninvolved users." So it is effectively mandatory. Wonderful. Who did they think we were hiding transactions from, our ex? The paper: https://eprint.iacr.org/2026/474

2d ago

---

---

## Google News: "ethereum"

**[Ethereum Rises to $2,000 as Tom Lee's BitMine Tops Up $9 Billion ETH Treasury](https://decrypt.co/360405/ethereum-rises-2000-tom-lee-bitmine-9-billion-treasury)**

The price of Ethereum is up 4% over the last day, rebounding after a weekend slump under $2,000 as BitMine reveals its latest ETH buy.

Decrypt • 23h ago

---

**[Current price of Ethereum for March 10, 2026](https://fortune.com/article/price-of-ethereum-03-10-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 17m ago

---

**[Ethereum Price Defends $2,000 Support as RSI Hits Near-Oversold Levels](https://finance.yahoo.com/news/ethereum-price-defends-2-000-071818617.html)**

The Ethereum price is fighting to hold the $2,000 line as sellers test the market’s resolve. The asset is trading at $2,050 with a weekly Relative Strength Index (RSI) of 33, signaling a crucial decision point.$2,000 represents a longstanding psychological level that bulls have defended since the February lows. The ...

Yahoo Finance • 5h ago

---

**[Ethereum (ETH) Below $2,000 Looks Increasingly Likely as Oil Prices Surge and Crypto Confidence Declines](https://www.ccn.com/analysis/crypto/ethereum-eth-below-2000-looks-increasingly-likely/)**

CCN.com • 13h ago

---

**[Here's What Would Need to Happen For Ethereum to Flip Bitcoin by 2030](https://www.fool.com/investing/2026/03/10/heres-what-would-need-to-happen-for-ethereum-to-fl/)**

What once seemed inevitable now seems like a long shot.

The Motley Fool • 2h ago

---

**[Claude AI Predicts the Price of Bitcoin and Ethereum If the Middle East Conflict Escalates](https://www.binance.com/en/square/post/299085766882482)**

Binance • 2d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.535 Million Tokens, and Total Crypto and Total Cash Holdings of $10.3 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-535-million-tokens-and-total-crypto-and-total-cash-holdings-of-10-3-billion-302708118.html)**

Bitmine has 3,040,483 staked ETH, representing $6.0 billion at $1,965 per ETH; MAVAN staking solution on track to launch Q1 2026 Bitmine now owns 3.76% of the...

PR Newswire • 1d ago

---

**[Sharplink Posts $734 Million Loss as Ethereum Staking Revenue Soars](https://finance.yahoo.com/news/sharplink-posts-734-million-loss-185152070.html)**

The Ethereum-buying firm attributed its full-year performance to the asset’s volatility.

Yahoo Finance • 18h ago

---

**[Bitmine Vs. Sharplink: One Is A Dilution Trap, The Other Is The Better Ethereum Proxy](https://seekingalpha.com/article/4879983-bitmine-vs-sharplink-one-is-a-dilution-trap-the-other-is-the-better-ethereum-proxy)**

Seeking Alpha • 1d ago

---

**[Bitcoin, Ethereum, XRP Brace for U.S. CPI Report](https://www.tradingview.com/news/99Bitcoins:19a7bb65e094b:0-bitcoin-ethereum-xrp-brace-for-u-s-cpi-report/)**

Bitcoin, Ethereum, and XRP are all trading in the green this week. On the surface, the crypto market looks calm. But under that calm, traders are waiting for one of the biggest macro events of the month: the U.S. CPI (inflation) report.Economists expect inflation to edge up to about 2.5%, slightly…

TradingView • 12h ago

---

---

## YouTube Videos: "ethereum"

**[Bitcoin &amp; Ethereum Are About To Wake Up (Watch Immediately)](https://www.youtube.com/watch?v=4nDVYeU6SRw)**

GET IN EARLY! Crypto Is About To Wake Up! ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily BTC Conference ...

📺 Altcoin Daily

👁️ 41K • 👍 2K • 💬 192 • ⏱️ 9:54 • 15h ago

---

**[This is FALLING RAPIDLY for ETH. Should we be concerned? (BMNR Stock)](https://www.youtube.com/watch?v=WfO0K8zmO-A)**

Follow me on X: @kross_roads 15% Off Fiscal.ai Plans! Unlock institutional-grade data with my link: https://fiscal.ai/?via=roy ...

📺 Crossroads

👁️ 5K • 👍 270 • 💬 37 • ⏱️ 18:25 • 13h ago

---

**[ETHEREUM ABOUT TO BREAKOUT?🔥 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=xTat0Edjfco)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 98 • 👍 6 • ⏱️ 5:18 • 3h ago

---

**[Ethereum To 85x From Here? Cathie Wood ETH Price Targets Are Insane!](https://www.youtube.com/watch?v=Qn2OgJ2Q_ZQ)**

Cathie Wood legitimately thinks that Ethereum can do a 85x from now until 2032. Sound insane? Here's her entire thesis.

📺 Zach Humphries

👁️ 3K • 👍 131 • 💬 14 • ⏱️ 7:38 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=iUcsXE5JWns)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 143 • 💬 6 • ⏱️ 4:08 • 1d ago

---

**[Bitcoin &amp; Ethereum Are About To Explode (SERIOUSLY)](https://www.youtube.com/watch?v=i5mW_EafMaI)**

Crypto Is About To Surprise EVERYONE!! (SERIOUSLY) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 49K • 👍 2K • 💬 161 • ⏱️ 11:32 • 2d ago

---

**[BITCOIN PRICE JUST FLIPPED (This is Next)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=i7V9o6KPUgs)**

BITCOIN PRICE JUST FLIPPED (This is Next)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* https://bit.ly/TOOBIT ...

📺 Crypto World

👁️ 7K • 👍 252 • 💬 300 • ⏱️ 14:42 • 15h ago

---

**[Identify Real BREAKOUTS !! ✅ ETHEREUM Analysis | Crypto Analysis](https://www.youtube.com/watch?v=jsKlIebxehU)**

Delta Exchange India - https://www.delta.exchange/?code=SHXFQP (10% discount on trading fees with this link) If you have ...

📺 Trading Secrets With Two Side Traders

👁️ 178 • 👍 40 • 💬 5 • ⏱️ 13:36 • 1h ago

---

**[Tom Lee - &quot;Largest Crypto Reset In HISTORY&quot; | Bitcoin &amp; ETH Price Prediction](https://www.youtube.com/watch?v=43KC2TkH8hk)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 8K • 👍 177 • 💬 119 • ⏱️ 15:06 • 2d ago

---

**[CRYPTO LIVE TRADING || 10 Mar  | ‪@ClockTraderlive‬ #bitcoin #ethereum #crypto #btclivetrading](https://www.youtube.com/watch?v=Ghw4p5I9vHo)**

join my social platforms for updates and analysis ✓Instagram: ...

📺 Aryan trader Live

👁️ 5K • 👍 2K • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
