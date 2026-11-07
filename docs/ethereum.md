---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-07T04:56:22.052584+00:00'
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

**Last Updated:** November 07, 2026 at 04:56 UTC  
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

### $2,236.46

---

## Ethereum Chart

**24h:** +0.8%  
**7d:** -1.5%  
**30d:** -9.9%  
**90d:** +19.7%  
**1y:** -34.2%  

---

## Ethereum Market Stats

**Market Cap:** $273.88B
Rank #2

**Circulating Supply:** 122,197,894 ETH
No max supply

**All-Time High:** $4,946.05
-54.7%

**All-Time Low:** $0.43
+517553.3%

---

## Reddit: r/ethereum

**[Daily General Discussion November 04, 2026](https://www.reddit.com/r/ethereum/comments/1xngmbp/daily_general_discussion_november_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Ethereum for digital public infrastructure](https://www.reddit.com/r/ethereum/comments/1xmpq8r/ethereum_for_digital_public_infrastructure/)**

Explore how Ethereum's open, global network can support digital public infrastructure, verifiable records, and coordination across institutions without a central operator.

🔗 [Ethereum for digital public infrastructure](https://publicsector.ethereum.foundation/) • 3d ago

---

**[Daily General Discussion November 03, 2026](https://www.reddit.com/r/ethereum/comments/1xml6ff/daily_general_discussion_november_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Are stablecoins becoming more useful than ETH for everyday payments?](https://www.reddit.com/r/ethereum/comments/1xlwz8b/are_stablecoins_becoming_more_useful_than_eth_for/)**

Most people seem to hold ETH as an investment, while USDT and USDC are increasingly being used for transfers and everyday payments. With more ways to spend crypto in real life now, I'm curious if anyone here pays with ETH or prefers using stablecoins. Do you think ETH will ever be widely used for everyday purchases or will stablecoins take that role?

4d ago

---

**[Daily General Discussion November 02, 2026](https://www.reddit.com/r/ethereum/comments/1xlpgqb/daily_general_discussion_november_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[🚨 Ethereum solo stakers: CVE-2026-98432 is a critical Linux TCP vulnerability with potential remote root access.](https://www.reddit.com/r/ethereum/comments/1xlidhr/ethereum_solo_stakers_cve202698432_is_a_critical/)**

My Geth node had a publicly listening MPTCP socket. Disabling MPTCP didn't close existing listeners! Check ss -Mlntp, apply mitigations and patch your kernel ASAP. https://ubuntu.com/security/CVE-2026-98432

5d ago

---

**[Daily General Discussion November 01, 2026](https://www.reddit.com/r/ethereum/comments/1xkulhh/daily_general_discussion_november_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

5d ago

---

**[8 years ago a CREATE2 “Wisp” post asked what stops a bait and switch with selfdestruct. What actually changed?](https://www.reddit.com/r/ethereum/comments/1xl5h2q/8_years_ago_a_create2_wisp_post_asked_what_stops/)**

Found an old post on CREATE2 Wisp contracts (a contract created, used and selfdestructed in one call so the same address can run different code later) and the top question in the comments was what prevents someone from auditing one version and deploying another at the same address. The honest answer back then was “selfdestruct is a red flag, check Etherscan.” What happened since - the Tornado Cash governance attack in 2023 did exactly that and EIP-6780 (Dencun, March 2024) limited SELFDESTRUCT to contracts created in the same transaction. EIP-7702 (Pectra, May 2025) later let EOAs delegate to contract code. Does the Wisp pattern still work post-6780 (create, use and destroy in one tx) and is anyone using it? Is same-transaction metamorphism still a practical risk for governance or allowlists? And how are people checking code identity at execution time now, EXTCODEHASH at execution, something else? UPD thanks u/Bloqarl. So the Wisp pattern still works post-6780 because create and destroy happen in the same tx but swapping code at the same address across txs is dead and the bait and switch moved to upgradeable proxies (an EXTCODEHASH pin never changes while the logic does) and to 7702 accounts that can re-delegate in their next tx. Still curious how people pin code identity in practice

5d ago

---

**[Cool video on ethereum and quantum posted today.](https://www.reddit.com/r/ethereum/comments/1xkldwq/cool_video_on_ethereum_and_quantum_posted_today/)**

From the original post on x: Quantum computing poses a serious threat to the cryptography blockchains currently rely on, while advances in AI compress best estimates for the threat's timeline. That's why experts gathered in Cambridge to coordinate research upgrading our cryptography to be quantum-resistant.

6d ago

---

**[Anyone needs a devcon ticket ?](https://www.reddit.com/r/ethereum/comments/1xkrt7e/anyone_needs_a_devcon_ticket/)**

So the thing is I bought a devcon ticket but it seems like I won't be able to attend due to some emergency situation...in case anyone's willing to buy one for a discounted price, we can discuss Win win for both

6d ago

---

---

## Google News: "ethereum"

**[EIP-8037/EIP-8038 Glamsterdam](https://blog.ethereum.org/2026/11/06/glamsterdam-8037-8038)**

In the previous weeks Chainsecurity has found a few projects that would be vulnerable after Glamsterdam since they rely on certain invariants. These invariants...

ethereum.org • 13h ago

---

**[Crypto foundation demanded employees endorse suicide pledge, then fired leaders who objected, Colorado lawsuit alleges](https://www.denverpost.com/2026/11/06/ethereum-suicide-pledge-lawsuit-mandate-boulder-crypto/)**

On a Friday in March, employees at an international technology foundation received a 38-page document outlining leadership’s vision for the foundation for the next 1,000 years.

The Denver Post • 17h ago

---

**[Where Will Ethereum Be in 3 Years?](https://finance.yahoo.com/markets/crypto/articles/where-ethereum-3-years-190100780.html)**

Ethereum isn't broken; it's just slow. Here's why that matters over the next three years.

Yahoo Finance • 1d ago

---

**[Bitcoin, Ethereum, XRP Slide as Peter Schiff Warns ‘Expect More Days Like Today’](https://www.tradingview.com/news/benzinga:9544553c4094b:0-bitcoin-ethereum-xrp-slide-as-peter-schiff-warns-expect-more-days-like-today/)**

Bitcoin CRYPTO:BTCUSD, Ethereum CRYPTO:ETHUSD and XRP CRYPTO:XRPUSD are down over 5% Thursday, with Peter Schiff warning "expect more days like today."Schiff Calls Thursday’s Selloff ‘Perfectly Rational’Schiff noted that Wednesday’s stock rally following the Democratic landslide "made no sense," wh…

TradingView • 1d ago

---

**[1 Top Cryptocurrency to Buy Before It Soars by 11,000%, According to Bitmine's Tom Lee](https://www.fool.com/investing/2026/11/06/1-cryptocurrency-buy-soars-11000-bitmines-tom-lee/)**

Lee thinks the Ether cryptocurrency is entering a new era, and it could create significant value for investors.

The Motley Fool • 12h ago

---

**[Is XRP a Good Investment Right Now at $1.18?](https://247wallst.com/investing/cryptocurrency/2026/11/06/is-xrp-a-good-investment-right-now-at-1-18/)**

XRP trades at $1.18, down sharply in 2026. Here's what needs to happen for it to reach $2 again and whether it's a smart investment now.

24/7 Wall St. • 10h ago

---

**[Ethereum software bug triggers emergency fixes across major layer-2 networks](https://cryptoslate.com/ethereum-software-bug-triggers-emergency-fixes-across-major-layer-2-networks/)**

CryptoSlate • 10h ago

---

**[Robinhood's crypto chain out-earned Ethereum in network revenue last quarter, exec says](https://www.coindesk.com/video/robinhood-s-crypto-chain-out-earned-ethereum-in-network-revenue-last-quarter-exec-says)**

CoinDesk • 14h ago

---

**[Current price of Ethereum for November 6, 2026](https://fortune.com/article/price-of-ethereum-11-06-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 16h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Bleed Amid Broader Sell-Off: Analyst Says BTC Will Bottom After Sweeping](https://www.benzinga.com/crypto/cryptocurrency/26/11/62965453/bitcoin-ethereum-xrp-dogecoin-crypto)**

Benzinga • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Arthur Hayes: Ethereum Is Headed For A Historic Run (Bull Case)](https://www.youtube.com/watch?v=7IzqpFtFRuI)**

Arthur Hayes says the market has bottomed and belief is back: Wall Street money and AI agents are heading onchain. Arthur ...

📺 The Rollup

👁️ 18K • 👍 248 • 💬 4 • ⏱️ 9:00 • 1d ago

---

**[I sold my Ethereum, here’s why](https://www.youtube.com/watch?v=mcrJu_BYqMw)**

AMERICANS LONG AND SHORT CRYPTO ON KALSHI - $25 FREE and 0.01% FEES ONLY WITH THIS LINK ...

📺 Lark Davis

👁️ 14K • 👍 270 • 💬 59 • ⏱️ 10:12 • 1d ago

---

**[Tom Lee :&quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” | 2026 Crypto Prediction](https://www.youtube.com/watch?v=lRFhJK1McaI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 93 • 👍 9 • ⏱️ 23:50 • 40m ago

---

**[Ethereum: The Final Drop of This Correction?](https://www.youtube.com/watch?v=W5wnnUYOJ2M)**

Sign up for Kalshi with our link: https://kalshi.com/p/morecryptoonline Paid partnership. US residents only (not available in the UK ...

📺 More Crypto Online

👁️ 3K • 👍 110 • 💬 3 • ⏱️ 6:44 • 8h ago

---

**[Ripple And XRP Are Making Major Moves And No One Notices Ethereum Is About To Become Mainstream](https://www.youtube.com/watch?v=ZInfCw1FagQ)**

Everyone out there is going to miss out on whats going on and its a shame. The cryptocurrency market has never seen this much ...

📺 The Modern Investor

👁️ 10K • 👍 726 • 💬 276 • ⏱️ 33:44 • 18h ago

---

**[Ethereum Just Had Its WORST Day Since June!!](https://www.youtube.com/watch?v=GaCClsZKjYs)**

Ethereum (ETH) just had its worst day since June, down 7.7% in a single day after its best day in seven weeks. Is this the bottom, ...

📺 Marzell Crypto

👁️ 279 • 👍 8 • 💬 2 • ⏱️ 3:19 • 14h ago

---

**[Bitcoin And Ethereum Are Preparing For Something Massive Crypto Whales Are Doing The Unthinkable](https://www.youtube.com/watch?v=fI-6zqZly_M)**

When crypto prices fall, retail investors flee the market, unable to understand that something bigger is happening behind the ...

📺 The Modern Investor

👁️ 9K • 👍 693 • 💬 128 • ⏱️ 32:49 • 1d ago

---

**[Why Ethereum Is Now Following the Amazon Playbook: Sharplink CEO](https://www.youtube.com/watch?v=tTM2FHu_2b0)**

Is Ethereum having its Amazon moment? Sharplink CEO Joseph Chalom believes investors may be making the same mistake ...

📺 Coinage

👁️ 17K • 👍 162 • 💬 83 • ⏱️ 20:55 • 2d ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=qeo2K_BmmXI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 6K • 👍 99 • 💬 61 • ⏱️ 23:02 • 2d ago

---

**[CRYPTO MARKET DUMPS! CZ BINANCE VS KEVIN O&#39;LEARY &amp; HUGE ETHEREUM &amp; SOLANA ADOPTION!](https://www.youtube.com/watch?v=_xRm-oXtH64)**

Crypto News: Bitcoin and the crypto market follow the stock market with a big dump. Binance and founder CZ subpoena Shark ...

📺 Thinking Crypto

👁️ 16K • 👍 558 • 💬 194 • ⏱️ 22:07 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
