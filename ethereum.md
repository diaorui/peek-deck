---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-06T23:41:58.402871+00:00'
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

**Last Updated:** November 06, 2026 at 23:41 UTC  
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

**24h:** -0.2%  
**7d:** -0.6%  
**30d:** -9.3%  
**90d:** +17.5%  
**1y:** -34.7%  

---

## Ethereum Market Stats

**Market Cap:** $273.66B
Rank #2

**Circulating Supply:** 122,194,930 ETH
No max supply

**All-Time High:** $4,946.05
-54.7%

**All-Time Low:** $0.43
+517151.4%

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

4d ago

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

5d ago

---

---

## Google News: "ethereum"

**[EIP-8037/EIP-8038 Glamsterdam](https://blog.ethereum.org/2026/11/06/glamsterdam-8037-8038)**

In the previous weeks Chainsecurity has found a few projects that would be vulnerable after Glamsterdam since they rely on certain invariants. These invariants...

ethereum.org • 8h ago

---

**[Crypto foundation demanded employees endorse suicide pledge, then fired leaders who objected, Colorado lawsuit alleges](https://www.denverpost.com/2026/11/06/ethereum-suicide-pledge-lawsuit-mandate-boulder-crypto/)**

On a Friday in March, employees at an international technology foundation received a 38-page document outlining leadership’s vision for the foundation for the next 1,000 years.

The Denver Post • 12h ago

---

**[Where Will Ethereum Be in 3 Years?](https://finance.yahoo.com/markets/crypto/articles/where-ethereum-3-years-190100780.html)**

Ethereum isn't broken; it's just slow. Here's why that matters over the next three years.

Yahoo Finance • 1d ago

---

**[1 Top Cryptocurrency to Buy Before It Soars by 11,000%, According to Bitmine's Tom Lee](https://www.fool.com/investing/2026/11/06/1-cryptocurrency-buy-soars-11000-bitmines-tom-lee/)**

Lee thinks the Ether cryptocurrency is entering a new era, and it could create significant value for investors.

The Motley Fool • 7h ago

---

**[Bitcoin, Ethereum, XRP Slide as Peter Schiff Warns ‘Expect More Days Like Today’](https://www.tradingview.com/news/benzinga:9544553c4094b:0-bitcoin-ethereum-xrp-slide-as-peter-schiff-warns-expect-more-days-like-today/)**

Bitcoin CRYPTO:BTCUSD, Ethereum CRYPTO:ETHUSD and XRP CRYPTO:XRPUSD are down over 5% Thursday, with Peter Schiff warning "expect more days like today."Schiff Calls Thursday’s Selloff ‘Perfectly Rational’Schiff noted that Wednesday’s stock rally following the Democratic landslide "made no sense," wh…

TradingView • 1d ago

---

**[Robinhood's crypto chain out-earned Ethereum in network revenue last quarter, exec says | CoinDesk Videos](https://www.coindesk.com/video/robinhood-s-crypto-chain-out-earned-ethereum-in-network-revenue-last-quarter-exec-says)**

CoinDesk • 9h ago

---

**[Ethereum software bug triggers emergency fixes across major layer-2 networks](https://cryptoslate.com/ethereum-software-bug-triggers-emergency-fixes-across-major-layer-2-networks/)**

CryptoSlate • 5h ago

---

**[Current price of Ethereum for November 6, 2026](https://fortune.com/article/price-of-ethereum-11-06-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 10h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Bleed Amid Broader Sell-Off: Analyst Says BTC Will Bottom After Sweeping](https://www.benzinga.com/crypto/cryptocurrency/26/11/62965453/bitcoin-ethereum-xrp-dogecoin-crypto)**

Benzinga • 21h ago

---

**[Bitcoin squeezes higher as Ethereum momentum heats up](https://www.kitco.com/opinion/2026-11-05/bitcoin-squeezes-higher-ethereum-momentum-heats)**

.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position:…

Kitco • 1d ago

---

---

## YouTube Videos: "ethereum"

**[I sold my Ethereum, here’s why](https://www.youtube.com/watch?v=mcrJu_BYqMw)**

AMERICANS LONG AND SHORT CRYPTO ON KALSHI - $25 FREE and 0.01% FEES ONLY WITH THIS LINK ...

📺 Lark Davis

👁️ 13K • 👍 263 • 💬 55 • ⏱️ 10:12 • 1d ago

---

**[Ethereum Price: Where This Correction Could End](https://www.youtube.com/watch?v=H6C2BP7r8pQ)**

Sign up for Kalshi with our link: https://kalshi.com/p/morecryptoonline Paid partnership. US residents only (not available in the UK ...

📺 More Crypto Online

👁️ 9K • 👍 215 • 💬 7 • ⏱️ 8:19 • 1d ago

---

**[Ethereum: The Final Drop of This Correction?](https://www.youtube.com/watch?v=W5wnnUYOJ2M)**

Sign up for Kalshi with our link: https://kalshi.com/p/morecryptoonline Paid partnership. US residents only (not available in the UK ...

📺 More Crypto Online

👁️ 1K • 👍 75 • 💬 18 • ⏱️ 6:44 • 2h ago

---

**[Why Ethereum Is Now Following the Amazon Playbook: Sharplink CEO](https://www.youtube.com/watch?v=tTM2FHu_2b0)**

Is Ethereum having its Amazon moment? Sharplink CEO Joseph Chalom believes investors may be making the same mistake ...

📺 Coinage

👁️ 17K • 👍 162 • 💬 83 • ⏱️ 20:55 • 2d ago

---

**[Arthur Hayes: Ethereum Is Headed For A Historic Run (Bull Case)](https://www.youtube.com/watch?v=7IzqpFtFRuI)**

Arthur Hayes says the market has bottomed and belief is back: Wall Street money and AI agents are heading onchain.

📺 The Rollup

👁️ 16K • 👍 237 • 💬 4 • ⏱️ 9:00 • 23h ago

---

**[Ethereum Just Had Its WORST Day Since June!!](https://www.youtube.com/watch?v=GaCClsZKjYs)**

Ethereum (ETH) just had its worst day since June, down 7.7% in a single day after its best day in seven weeks. Is this the bottom, ...

📺 Marzell Crypto

👁️ 160 • 👍 8 • 💬 2 • ⏱️ 3:19 • 9h ago

---

**[Crypto Altcoin Holders Look Like FOOLS Right Now... But The Story Isn’t Over](https://www.youtube.com/watch?v=9Sphy3OOttw)**

CCV Risk Models & Intelligence System — Start your free trial: https://app.cryptocapitalventure.ai/ Altcoin holders look like fools ...

📺 Crypto Capital Venture

👁️ 8K • 👍 377 • 💬 72 • ⏱️ 16:21 • 6h ago

---

**[Ripple And XRP Are Making Major Moves And No One Notices Ethereum Is About To Become Mainstream](https://www.youtube.com/watch?v=ZInfCw1FagQ)**

Everyone out there is going to miss out on whats going on and its a shame. The cryptocurrency market has never seen this much ...

📺 The Modern Investor

👁️ 9K • 👍 705 • 💬 276 • ⏱️ 33:44 • 13h ago

---

**[CRYPTO MARKET DUMPS! CZ BINANCE VS KEVIN O&#39;LEARY &amp; HUGE ETHEREUM &amp; SOLANA ADOPTION!](https://www.youtube.com/watch?v=_xRm-oXtH64)**

Crypto News: Bitcoin and the crypto market follow the stock market with a big dump. Binance and founder CZ subpoena Shark ...

📺 Thinking Crypto

👁️ 16K • 👍 546 • 💬 194 • ⏱️ 22:07 • 18h ago

---

**[THIS LOOKS VERY BULLISH FOR ETH! (Ethereum Update)](https://www.youtube.com/watch?v=sEaV_T6bbZY)**

ETHEREUM ETH PRICE PREDICTION 2026 Join my Premium Trading Group: https://whop.com/cilinix-crypto/cilinixpremium/ ...

📺 Cilinix Crypto

👁️ 876 • 👍 19 • 💬 4 • ⏱️ 4:41 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
