---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-04T06:52:31.671054+00:00'
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

**Last Updated:** November 04, 2026 at 06:52 UTC  
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

### $2,240.00

---

## Ethereum Chart

**24h:** +1.7%  
**7d:** +2.0%  
**30d:** -14.8%  
**90d:** +20.0%  
**1y:** -32.9%  

---

## Ethereum Market Stats

**Market Cap:** $280.21B
Rank #2

**Circulating Supply:** 122,189,135 ETH
No max supply

**All-Time High:** $4,946.05
-53.6%

**All-Time Low:** $0.43
+529542.3%

---

## Reddit: r/ethereum

**[Daily General Discussion November 04, 2026](https://www.reddit.com/r/ethereum/comments/1xngmbp/daily_general_discussion_november_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

51m ago

---

**[Ethereum for digital public infrastructure](https://www.reddit.com/r/ethereum/comments/1xmpq8r/ethereum_for_digital_public_infrastructure/)**

Explore how Ethereum's open, global network can support digital public infrastructure, verifiable records, and coordination across institutions without a central operator.

🔗 [Ethereum for digital public infrastructure](https://publicsector.ethereum.foundation/) • 20h ago

---

**[Daily General Discussion November 03, 2026](https://www.reddit.com/r/ethereum/comments/1xml6ff/daily_general_discussion_november_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[Are stablecoins becoming more useful than ETH for everyday payments?](https://www.reddit.com/r/ethereum/comments/1xlwz8b/are_stablecoins_becoming_more_useful_than_eth_for/)**

Most people seem to hold ETH as an investment, while USDT and USDC are increasingly being used for transfers and everyday payments. With more ways to spend crypto in real life now, I'm curious if anyone here pays with ETH or prefers using stablecoins. Do you think ETH will ever be widely used for everyday purchases or will stablecoins take that role?

1d ago

---

**[Daily General Discussion November 02, 2026](https://www.reddit.com/r/ethereum/comments/1xlpgqb/daily_general_discussion_november_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[🚨 Ethereum solo stakers: CVE-2026-98432 is a critical Linux TCP vulnerability with potential remote root access.](https://www.reddit.com/r/ethereum/comments/1xlidhr/ethereum_solo_stakers_cve202698432_is_a_critical/)**

My Geth node had a publicly listening MPTCP socket. Disabling MPTCP didn't close existing listeners! Check ss -Mlntp, apply mitigations and patch your kernel ASAP. https://ubuntu.com/security/CVE-2026-98432

2d ago

---

**[Daily General Discussion November 01, 2026](https://www.reddit.com/r/ethereum/comments/1xkulhh/daily_general_discussion_november_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[8 years ago a CREATE2 “Wisp” post asked what stops a bait and switch with selfdestruct. What actually changed?](https://www.reddit.com/r/ethereum/comments/1xl5h2q/8_years_ago_a_create2_wisp_post_asked_what_stops/)**

Found an old post on CREATE2 Wisp contracts (a contract created, used and selfdestructed in one call so the same address can run different code later) and the top question in the comments was what prevents someone from auditing one version and deploying another at the same address. The honest answer back then was “selfdestruct is a red flag, check Etherscan.” What happened since - the Tornado Cash governance attack in 2023 did exactly that and EIP-6780 (Dencun, March 2024) limited SELFDESTRUCT to contracts created in the same transaction. EIP-7702 (Pectra, May 2025) later let EOAs delegate to contract code. Does the Wisp pattern still work post-6780 (create, use and destroy in one tx) and is anyone using it? Is same-transaction metamorphism still a practical risk for governance or allowlists? And how are people checking code identity at execution time now, EXTCODEHASH at execution, something else? UPD thanks u/Bloqarl. So the Wisp pattern still works post-6780 because create and destroy happen in the same tx but swapping code at the same address across txs is dead and the bait and switch moved to upgradeable proxies (an EXTCODEHASH pin never changes while the logic does) and to 7702 accounts that can re-delegate in their next tx. Still curious how people pin code identity in practice

2d ago

---

**[Cool video on ethereum and quantum posted today.](https://www.reddit.com/r/ethereum/comments/1xkldwq/cool_video_on_ethereum_and_quantum_posted_today/)**

From the original post on x: Quantum computing poses a serious threat to the cryptography blockchains currently rely on, while advances in AI compress best estimates for the threat's timeline. That's why experts gathered in Cambridge to coordinate research upgrading our cryptography to be quantum-resistant.

3d ago

---

**[Anyone needs a devcon ticket ?](https://www.reddit.com/r/ethereum/comments/1xkrt7e/anyone_needs_a_devcon_ticket/)**

So the thing is I bought a devcon ticket but it seems like I won't be able to attend due to some emergency situation...in case anyone's willing to buy one for a discounted price, we can discuss Win win for both

3d ago

---

---

## Google News: "ethereum"

**[Why Bitmine Immersion Technologies Stock Is In Focus After Its Ethereum Buying Spree](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-stock-043344012.html)**

Bitmine Immersion Technologies recently acquired nearly US$20 million of Ethereum, bringing its ETH holdings to 6.06 million tokens, equal to 4.9% of the 122.2 million total supply, alongside US$14.5b in combined crypto, cash and marketable securities. This sizeable Ethereum position, together with Tom Lee’s comments on the market’s resilience after the Binance hack, places Bitmine’s operating focus squarely on digital asset exposure and AI infrastructure demand rather than near term...

Yahoo Finance • 2h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Surrender Early Gains as Midterm Polls Close—Analyst Sees ‘Sell the Rumor, Buy the News’ Play](https://www.tradingview.com/news/benzinga:f1a5c7082094b:0-bitcoin-ethereum-xrp-dogecoin-surrender-early-gains-as-midterm-polls-close-analyst-sees-sell-the-rumor-buy-the-news-play/)**

Leading cryptocurrencies retreated late Tuesday evening as investors awaited the outcome of the midterm elections.Crypto Market on Election DayBitcoin climbed to an intraday high of $77,965.50 before pulling back later in the evening. Ethereum also gave up earlier gains with a sharp overnight decli…

TradingView • 5h ago

---

**[ETHGas wants to bring Wall Street to public Ethereum by selling advance block reservations](https://www.coindesk.com/business/2026/11/03/ethgas-courts-wall-street-with-ethereum-blockspace-but-compensation-for-missed-trades-is-zero)**

CoinDesk • 18h ago

---

**[XRP or Ethereum: Which Is the Smarter Buy for the Next 5 Years?](https://247wallst.com/investing/cryptocurrency/2026/11/01/xrp-or-ethereum-which-is-the-smarter-buy-for-the-next-5-years/)**

XRP and Ethereum both trade far below their 2025 peaks. Here's which one has a better chance of rebounding by 2031.

24/7 Wall St. • 2d ago

---

**[Designing for sovereignty: Ethereum for digital public infrastructure](https://blog.ethereum.org/2026/11/03/digital-pub-infra)**

Public services increasingly rely on digital systems that enable institutions to collaborate across organizational and national boundaries. Such cooperation...

ethereum.org • 1d ago

---

**[Current price of Ethereum for November 3, 2026](https://fortune.com/article/price-of-ethereum-11-03-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 18h ago

---

**[Ethereum Privacy Network Aztec Rolls Out Major Security and Speed Upgrade](https://decrypt.co/382387/ethereum-privacy-network-aztec-security-speed-upgrade)**

Aztec, the privacy-focused Ethereum layer-2 network, has rolled out a major upgrade that fixes a critical vulnerability.

Decrypt • 16h ago

---

**[Tom Lee calls Ethereum’s 4% post-hack fall bullish](https://cryptoslate.com/tom-lee-calls-ethereums-4-post-hack-fall-bullish-but-the-bybit-comparison-has-a-catch/)**

Tom Lee calls Ethereum’s 4% fall after Binance’s hack bullish. His Bybit comparison uses a longer period, while BitMine keeps buying ETH.

CryptoSlate • 1d ago

---

**[Aptos joins Solana and Ethereum in Bullish’s tokenized stock plan](https://www.thestreet.com/crypto/innovation/aptos-joins-solana-and-ethereum-in-bullishs-tokenized-stock-plan)**

TheStreet • 12h ago

---

**[Ethereum Foundation highlights wallet protocols for enhanced privacy](https://cryptobriefing.com/ethereum-foundation-kohaku-wallet-privacy/)**

The Ethereum Foundation's Kohaku SDK brings stealth addresses, shielded balances and formally verified privacy tools to Ethereum wallets.

Crypto Briefing • 7h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum&#39;s Bull Case Is Getting INSANE - Here Are 3 Reasons Why](https://www.youtube.com/watch?v=0JeoNGi7C_o)**

Want to see what John's actually buying? He just deployed a big chunk of his portfolio into alts, and Milk Road PRO members can ...

📺 Milk Road

👁️ 19K • 👍 369 • 💬 121 • ⏱️ 47:29 • 1d ago

---

**[Ethereum (ETH/USDT) daily check, 02 November 2026 #mindset #trading #cryptotrading](https://www.youtube.com/watch?v=DqJsr22iKDk)**

Who's in control: neither side (long-term and short-term trends disagree). Verdict: NO TRADE · Level to watch: 2490.32 Don't trade ...

📺 Verdict of the Day

👁️ 80 • 👍 4 • ⏱️ 0:51 • 1d ago

---

**[ETHEREUM swung $63.78 in 3 days](https://www.youtube.com/watch?v=5F0bvyseFwY)**

What happened to ETHEREUM? A 2.2% move over the last three days, broken down. Range $2242 - $2306. Follow ...

📺 The Crypto Goblin

👁️ 2 • ⏱️ 0:39 • 14h ago

---

**[Ethereum Bounces From Major Support. Is the Low In?](https://www.youtube.com/watch?v=0FRKySfUK9A)**

Ethereum is showing some upside momentum and is approaching the top of its channel. Here is what would confirm a low, and ...

📺 More Crypto Online

👁️ 9K • 👍 222 • 💬 8 • ⏱️ 6:40 • 2d ago

---

**[Ethereum&#39;s Biggest Bull Case Has One Massive Flaw](https://www.youtube.com/watch?v=yj1Aug58WpA)**

Want to see what Buffett, Pelosi and Vitalik own? Track their holdings for free with our Insider Portfolios at: ...

📺 Milk Road

👁️ 7K • 👍 77 • 💬 74 • ⏱️ 14:53 • 2d ago

---

**[Ethereum Head and Shoulders Targets $1,986 #Ethereum #ETH #ChartPattern](https://www.youtube.com/watch?v=v-aRP5khDos)**

Ethereum Head and Shoulders Targets $1986 #Ethereum #ETH #ChartPattern ⏱️ From main video at 1:33 - 2:14 Watch full ...

📺 The Trading Parrot

👁️ 453 • 👍 20 • 💬 2 • ⏱️ 1:02 • 2d ago

---

**[Raoul Pal :&quot;This F**ked my BTC &amp; ETH Prediction But It&#39;s About to Turn VERY BULLISH&quot;](https://www.youtube.com/watch?v=IPWeLJ5RaZk)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 18K • 👍 308 • 💬 93 • ⏱️ 23:22 • 2d ago

---

**[XRP HYPE 🚨 I AM FINISHED (Bitcoin Ethereum)](https://www.youtube.com/watch?v=gD77sM3hzFc)**

Save 40% code MOE is back!* ➡https://join.stockmoeacademy.com/join-page *   FREE month of Earner Plus + 12 free fractional ...

📺 Stock Moe

👁️ 23K • 👍 562 • 💬 44 • ⏱️ 12:04 • 2d ago

---

**[The Race to Build the Private Ethereum](https://www.youtube.com/watch?v=UszyU_XrX9o)**

SPOTIFY PREMIUM RSS FEED | USE CODE: SPOTIFY24 https://bankless.cc/spotify-premium --- Can Ethereum become private ...

📺 Bankless

👁️ 4K • 👍 77 • 💬 21 • ⏱️ 46:15 • 19h ago

---

**[How $6 Billion Crypto Was Stolen](https://www.youtube.com/watch?v=ibwI8ntxxjg)**

The attacker left exactly one ETH behind on purpose. That's what let the heist keep going. One transaction pulled out roughly $2.5 ...

📺 Andrei Jikh

👁️ 33K • 👍 754 • 💬 28 • ⏱️ 1:08 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
