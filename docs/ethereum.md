---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-06T03:32:55.029275+00:00'
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

**Last Updated:** November 06, 2026 at 03:32 UTC  
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

### $2,245.38

---

## Ethereum Chart

**24h:** -8.0%  
**7d:** -1.1%  
**30d:** -9.8%  
**90d:** +16.9%  
**1y:** -35.0%  

---

## Ethereum Market Stats

**Market Cap:** $272.92B
Rank #2

**Circulating Supply:** 122,192,072 ETH
No max supply

**All-Time High:** $4,946.05
-54.8%

**All-Time Low:** $0.43
+515707.9%

---

## Reddit: r/ethereum

**[Daily General Discussion November 04, 2026](https://www.reddit.com/r/ethereum/comments/1xngmbp/daily_general_discussion_november_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[Ethereum for digital public infrastructure](https://www.reddit.com/r/ethereum/comments/1xmpq8r/ethereum_for_digital_public_infrastructure/)**

Explore how Ethereum's open, global network can support digital public infrastructure, verifiable records, and coordination across institutions without a central operator.

🔗 [Ethereum for digital public infrastructure](https://publicsector.ethereum.foundation/) • 2d ago

---

**[Daily General Discussion November 03, 2026](https://www.reddit.com/r/ethereum/comments/1xml6ff/daily_general_discussion_november_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Are stablecoins becoming more useful than ETH for everyday payments?](https://www.reddit.com/r/ethereum/comments/1xlwz8b/are_stablecoins_becoming_more_useful_than_eth_for/)**

Most people seem to hold ETH as an investment, while USDT and USDC are increasingly being used for transfers and everyday payments. With more ways to spend crypto in real life now, I'm curious if anyone here pays with ETH or prefers using stablecoins. Do you think ETH will ever be widely used for everyday purchases or will stablecoins take that role?

3d ago

---

**[Daily General Discussion November 02, 2026](https://www.reddit.com/r/ethereum/comments/1xlpgqb/daily_general_discussion_november_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[🚨 Ethereum solo stakers: CVE-2026-98432 is a critical Linux TCP vulnerability with potential remote root access.](https://www.reddit.com/r/ethereum/comments/1xlidhr/ethereum_solo_stakers_cve202698432_is_a_critical/)**

My Geth node had a publicly listening MPTCP socket. Disabling MPTCP didn't close existing listeners! Check ss -Mlntp, apply mitigations and patch your kernel ASAP. https://ubuntu.com/security/CVE-2026-98432

4d ago

---

**[Daily General Discussion November 01, 2026](https://www.reddit.com/r/ethereum/comments/1xkulhh/daily_general_discussion_november_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[8 years ago a CREATE2 “Wisp” post asked what stops a bait and switch with selfdestruct. What actually changed?](https://www.reddit.com/r/ethereum/comments/1xl5h2q/8_years_ago_a_create2_wisp_post_asked_what_stops/)**

Found an old post on CREATE2 Wisp contracts (a contract created, used and selfdestructed in one call so the same address can run different code later) and the top question in the comments was what prevents someone from auditing one version and deploying another at the same address. The honest answer back then was “selfdestruct is a red flag, check Etherscan.” What happened since - the Tornado Cash governance attack in 2023 did exactly that and EIP-6780 (Dencun, March 2024) limited SELFDESTRUCT to contracts created in the same transaction. EIP-7702 (Pectra, May 2025) later let EOAs delegate to contract code. Does the Wisp pattern still work post-6780 (create, use and destroy in one tx) and is anyone using it? Is same-transaction metamorphism still a practical risk for governance or allowlists? And how are people checking code identity at execution time now, EXTCODEHASH at execution, something else? UPD thanks u/Bloqarl. So the Wisp pattern still works post-6780 because create and destroy happen in the same tx but swapping code at the same address across txs is dead and the bait and switch moved to upgradeable proxies (an EXTCODEHASH pin never changes while the logic does) and to 7702 accounts that can re-delegate in their next tx. Still curious how people pin code identity in practice

4d ago

---

**[Cool video on ethereum and quantum posted today.](https://www.reddit.com/r/ethereum/comments/1xkldwq/cool_video_on_ethereum_and_quantum_posted_today/)**

From the original post on x: Quantum computing poses a serious threat to the cryptography blockchains currently rely on, while advances in AI compress best estimates for the threat's timeline. That's why experts gathered in Cambridge to coordinate research upgrading our cryptography to be quantum-resistant.

5d ago

---

**[Anyone needs a devcon ticket ?](https://www.reddit.com/r/ethereum/comments/1xkrt7e/anyone_needs_a_devcon_ticket/)**

So the thing is I bought a devcon ticket but it seems like I won't be able to attend due to some emergency situation...in case anyone's willing to buy one for a discounted price, we can discuss Win win for both

5d ago

---

---

## Google News: "ethereum"

**[Why Bitmine Immersion Technologies Stock Is In Focus After Its Ethereum Buying Spree](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-stock-043344012.html)**

Bitmine Immersion Technologies recently acquired nearly US$20 million of Ethereum, bringing its ETH holdings to 6.06 million tokens, equal to 4.9% of the 122.2 million total supply, alongside US$14.5b in combined crypto, cash and marketable securities. This sizeable Ethereum position, together with Tom Lee’s comments on the market’s resilience after the Binance hack, places Bitmine’s operating focus squarely on digital asset exposure and AI infrastructure demand rather than near term...

Yahoo Finance • 1d ago

---

**[Bitcoin, Ethereum, XRP Slide as Peter Schiff Warns ‘Expect More Days Like Today’](https://www.tradingview.com/news/benzinga:9544553c4094b:0-bitcoin-ethereum-xrp-slide-as-peter-schiff-warns-expect-more-days-like-today/)**

Bitcoin CRYPTO:BTCUSD, Ethereum CRYPTO:ETHUSD and XRP CRYPTO:XRPUSD are down over 5% Thursday, with Peter Schiff warning "expect more days like today."Schiff Calls Thursday’s Selloff ‘Perfectly Rational’Schiff noted that Wednesday’s stock rally following the Democratic landslide "made no sense," wh…

TradingView • 9h ago

---

**[Not Hyperliquid. Not Zcash. This Will Be the Top-Performing Cryptocurrency of 2027.](https://www.fool.com/investing/2026/11/05/not-x-not-y-this-will-be-the-top-performing-crypto/)**

If history is any guide, Ethereum will be one of the biggest winners during the next DeFi boom.

The Motley Fool • 17h ago

---

**[Current price of Ethereum for November 5, 2026](https://fortune.com/article/price-of-ethereum-11-05-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 14h ago

---

**[Most big cryptocurrencies increase as Ethereum rallies](https://www.marketwatch.com/data-news/most-big-cryptocurrencies-increase-as-ethereum-rallies-51642d12-b2906bfb97c4)**

MarketWatch • 1d ago

---

**[Ethereum’s decentralization model is the answer to an AI arms race: Vitalik Buterin](https://ambcrypto.com/ethereums-decentralization-model-is-the-answer-to-ai-arms-race-vitalik-buterin/)**

Ethereum’s decentralization could strengthen its long-term value as AI risks increase demand for open infrastructure.

AMBCrypto • 1d ago

---

**[Bitcoin squeezes higher as Ethereum momentum heats up](https://www.kitco.com/opinion/2026-11-05/bitcoin-squeezes-higher-ethereum-momentum-heats)**

.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position:…

Kitco • 12h ago

---

**[Ethereum Holds Two-Thirds of Ripple’s $2.6 Billion RLUSD Stablecoin Even as Ripple CEO Pushes XRP Ledger](https://www.tipranks.com/news/ethereum-holds-two-thirds-of-ripples-2-6-billion-rlusd-stablecoin-even-as-ripple-ceo-pushes-xrp-ledger)**

TipRanks • 12h ago

---

**[Designing for sovereignty: Ethereum for digital public infrastructure](https://blog.ethereum.org/2026/11/03/digital-pub-infra)**

Public services increasingly rely on digital systems that enable institutions to collaborate across organizational and national boundaries. Such cooperation...

ethereum.org • 3d ago

---

**[Ethereum prepares to overhaul its state structure with a Partitioned Binary Tree](https://cryptobriefing.com/ethereum-partitioned-binary-tree-eip-8297/)**

Ethereum's EIP-8297 Partitioned Binary Tree passed a mainnet shadowfork test, aiming for smaller state proofs and state expiry by Q4 2026.

Crypto Briefing • 2h ago

---

---

## YouTube Videos: "ethereum"

**[I sold my Ethereum, here’s why](https://www.youtube.com/watch?v=mcrJu_BYqMw)**

AMERICANS LONG AND SHORT CRYPTO ON KALSHI - $25 FREE and 0.01% FEES ONLY WITH THIS LINK ...

📺 Lark Davis

👁️ 6K • 👍 186 • 💬 35 • ⏱️ 10:12 • 6h ago

---

**[Arthur Hayes: Ethereum Is Headed For A Historic Run (Bull Case)](https://www.youtube.com/watch?v=7IzqpFtFRuI)**

Arthur Hayes says the market has bottomed and belief is back: Wall Street money and AI agents are heading onchain.

📺 The Rollup

👁️ 2K • 👍 61 • 💬 60 • ⏱️ 9:00 • 3h ago

---

**[Bitcoin And Ethereum Are Preparing For Something Massive Crypto Whales Are Doing The Unthinkable](https://www.youtube.com/watch?v=fI-6zqZly_M)**

When crypto prices fall, retail investors flee the market, unable to understand that something bigger is happening behind the ...

📺 The Modern Investor

👁️ 8K • 👍 643 • 💬 139 • ⏱️ 32:49 • 17h ago

---

**[Ethereum Price: Where This Correction Could End](https://www.youtube.com/watch?v=H6C2BP7r8pQ)**

Sign up for Kalshi with our link: https://kalshi.com/p/morecryptoonline Paid partnership. US residents only (not available in the UK ...

📺 More Crypto Online

👁️ 5K • 👍 158 • 💬 5 • ⏱️ 8:19 • 7h ago

---

**[Why Ethereum Is Now Following the Amazon Playbook: Sharplink CEO](https://www.youtube.com/watch?v=tTM2FHu_2b0)**

Is Ethereum having its Amazon moment? Sharplink CEO Joseph Chalom believes investors may be making the same mistake ...

📺 Coinage

👁️ 16K • 👍 155 • 💬 84 • ⏱️ 20:55 • 1d ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=qeo2K_BmmXI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 5K • 👍 97 • 💬 67 • ⏱️ 23:02 • 1d ago

---

**[A hacker drained $50 million, so Ethereum rewound time ⏪](https://www.youtube.com/watch?v=nMGJ2JhRw2o)**

In 2016, a bug let a hacker drain about 3.6 million ether from The DAO, a fund run by code instead of managers. A 28-day lock ...

📺 Crazy Crypto Stories

👁️ 1K • 👍 26 • ⏱️ 0:52 • 9h ago

---

**[ICP is the SOLUTION! Vitalik&#39;s Message Raises a BIG Question for Ethereum](https://www.youtube.com/watch?v=27aZZXoGUSU)**

Join the OC HERO Community: https://oc.app/community/s6uwt-5iaaa-aaaac-be5xa-cai/channel/3896146702 HERO: ...

📺 Zero to Hero

👁️ 1K • 👍 138 • 💬 13 • ⏱️ 20:41 • 8h ago

---

**[BITCOIN FLIPPED: IT&#39;S HAPPENING AGAIN (Price Target)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=aZiGwaGsnTM)**

BITCOIN FLIPPED: IT'S HAPPENING AGAIN (Price Target)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 15K • 👍 311 • 💬 166 • ⏱️ 21:26 • 1d ago

---

**[IS CRYPTO SETTING UP FOR A RALLY? BITCOIN, XRP, ETHEREUM, &amp; CANTON NETWORK ANALYSIS!](https://www.youtube.com/watch?v=t6ZZoTZiGfc)**

Brian from Santiment joined me to break down the latest crypto market trends, key on-chain metrics, and investor sentiment for ...

📺 Thinking Crypto

👁️ 6K • 👍 198 • 💬 59 • ⏱️ 25:45 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
