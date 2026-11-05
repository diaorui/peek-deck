---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-05T17:33:18.630390+00:00'
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

**Last Updated:** November 05, 2026 at 17:33 UTC  
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

### $2,250.00

---

## Ethereum Chart

**24h:** -6.9%  
**7d:** +0.5%  
**30d:** -12.4%  
**90d:** +17.6%  
**1y:** -32.0%  

---

## Ethereum Market Stats

**Market Cap:** $275.02B
Rank #2

**Circulating Supply:** 122,192,072 ETH
No max supply

**All-Time High:** $4,946.05
-54.5%

**All-Time Low:** $0.43
+519705.8%

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

3d ago

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

4d ago

---

**[Anyone needs a devcon ticket ?](https://www.reddit.com/r/ethereum/comments/1xkrt7e/anyone_needs_a_devcon_ticket/)**

So the thing is I bought a devcon ticket but it seems like I won't be able to attend due to some emergency situation...in case anyone's willing to buy one for a discounted price, we can discuss Win win for both

4d ago

---

---

## Google News: "ethereum"

**[Ethereum Price Prediction 2040: ETH Outlook](https://bitcoinfoundation.org/news/analysis/ethereum-falls-4-as-solana-eth-ticker-collision-complicates-2040-outlook/)**

Ethereum fell 4% to $2,327 as a separate Solana token also used the ETH ticker, complicating the ethereum price prediction 2040 search and asset checks.

Bitcoin Foundation • 1h ago

---

**[Why Bitmine Immersion Technologies Stock Is In Focus After Its Ethereum Buying Spree](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-stock-043344012.html)**

Bitmine Immersion Technologies recently acquired nearly US$20 million of Ethereum, bringing its ETH holdings to 6.06 million tokens, equal to 4.9% of the 122.2 million total supply, alongside US$14.5b in combined crypto, cash and marketable securities. This sizeable Ethereum position, together with Tom Lee’s comments on the market’s resilience after the Binance hack, places Bitmine’s operating focus squarely on digital asset exposure and AI infrastructure demand rather than near term...

Yahoo Finance • 1d ago

---

**[Bitcoin near $78,600, Ethereum at $2,300 as US midterm results put crypto regulation in focus](https://www.tradingview.com/news/moodys:8e75edd236e39:0-bitcoin-near-78-600-ethereum-at-2-300-as-us-midterm-results-put-crypto-regulation-in-focus/)**

Bitcoin trades near the $78,000 mark on Wednesday amid institutional outflows and macroeconomic uncertainty. The cryptocurrency was trading at the $78,330 mark, and Ethereum was trading at $2,317.In the past 24 hours, Bitcoin and Ethereum were up 1.87% and 2.41%, respectively. Among the major altco…

TradingView • 1d ago

---

**[Current price of Ethereum for November 5, 2026](https://fortune.com/article/price-of-ethereum-11-05-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 5h ago

---

**[ETHGas brings compliance controls to public Ethereum, but missed trade penalties sit at zero](https://www.coindesk.com/business/2026/11/03/ethgas-courts-wall-street-with-ethereum-blockspace-but-compensation-for-missed-trades-is-zero)**

CoinDesk • 1d ago

---

**[Most big cryptocurrencies increase as Ethereum rallies](https://www.marketwatch.com/data-news/most-big-cryptocurrencies-increase-as-ethereum-rallies-51642d12-b2906bfb97c4)**

MarketWatch • 1d ago

---

**[Ethereum’s decentralization model is the answer to an AI arms race: Vitalik Buterin](https://ambcrypto.com/ethereums-decentralization-model-is-the-answer-to-ai-arms-race-vitalik-buterin/)**

Ethereum’s decentralization could strengthen its long-term value as AI risks increase demand for open infrastructure.

AMBCrypto • 1d ago

---

**[Is Google's New Cryptocurrency Service a Reason to Buy Ethereum or Solana?](https://www.fool.com/investing/2026/11/04/is-googles-new-cryptocurrency-service-a-reason-to/)**

The company's new platform plays to institutional cybersecurity concerns.

The Motley Fool • 1d ago

---

**[Bitcoin and Ethereum await a bounce as stocks slide](https://www.kitco.com/opinion/2026-11-04/bitcoin-and-ethereum-await-bounce-stocks-slide)**

.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position:…

Kitco • 1d ago

---

**[Designing for sovereignty: Ethereum for digital public infrastructure](https://blog.ethereum.org/2026/11/03/digital-pub-infra)**

Public services increasingly rely on digital systems that enable institutions to collaborate across organizational and national boundaries. Such cooperation...

ethereum.org • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Bitcoin And Ethereum Are Preparing For Something Massive Crypto Whales Are Doing The Unthinkable](https://www.youtube.com/watch?v=fI-6zqZly_M)**

When crypto prices fall, retail investors flee the market, unable to understand that something bigger is happening behind the ...

📺 The Modern Investor

👁️ 6K • 👍 538 • 💬 73 • ⏱️ 32:49 • 7h ago

---

**[Why Ethereum Is Now Following the Amazon Playbook: Sharplink CEO](https://www.youtube.com/watch?v=tTM2FHu_2b0)**

Is Ethereum having its Amazon moment? Sharplink CEO Joseph Chalom believes investors may be making the same mistake ...

📺 Coinage

👁️ 13K • 👍 148 • 💬 83 • ⏱️ 20:55 • 1d ago

---

**[Midterms Over, Selling ETH, Altcoin Breakouts Brewing, &amp; Portfolio Roasts](https://www.youtube.com/watch?v=s2BFuUAHbKs)**

Trump loses, ETH gone, altcoins trades, and BTC charts BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 22K • 👍 458 • 💬 73 • ⏱️ 1:12:48 • 1d ago

---

**[BITCOIN FLIPPED: IT&#39;S HAPPENING AGAIN (Price Target)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=aZiGwaGsnTM)**

BITCOIN FLIPPED: IT'S HAPPENING AGAIN (Price Target)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 13K • 👍 308 • 💬 100 • ⏱️ 21:26 • 20h ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=qeo2K_BmmXI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 5K • 👍 94 • 💬 68 • ⏱️ 23:02 • 1d ago

---

**[Ethereum RIPPED $225 Off the Low, I caught the Long!](https://www.youtube.com/watch?v=chO2jgQclYc)**

WEEX - where my trade is placed (up to $10000+ in sign-up rewards) https://marzell.org/wx-v106 Ethereum (ETH) flushed to ...

📺 Marzell Crypto

👁️ 504 • 👍 12 • 💬 1 • ⏱️ 3:10 • 1d ago

---

**[THIS LOOKS VERY BULLISH FOR ETH! (Ethereum Update)](https://www.youtube.com/watch?v=sEaV_T6bbZY)**

ETHEREUM ETH PRICE PREDICTION 2026 Join my Premium Trading Group: https://whop.com/cilinix-crypto/cilinixpremium/ ...

📺 Cilinix Crypto

👁️ 761 • 👍 18 • 💬 4 • ⏱️ 4:41 • 1d ago

---

**[CRUCIAL XRP LEDGER SECURITY FLAW FOUND! Ethereum Was NOT Hacked!](https://www.youtube.com/watch?v=qWlCYaQ9RtQ)**

CRUCIAL XRP LEDGER SECURITY FLAW FOUND! ETHEREUM IS BETTER? Hey babes, an XRP Ledger flaw was found that ...

📺 CryptoWendyO

👁️ 8K • 👍 213 • 💬 35 • ⏱️ 5:52 • 2d ago

---

**[Ethereum&#39;s Bull Case Is Getting INSANE - Here Are 3 Reasons Why](https://www.youtube.com/watch?v=0JeoNGi7C_o)**

Want to see what John's actually buying? He just deployed a big chunk of his portfolio into alts, and Milk Road PRO members can ...

📺 Milk Road

👁️ 23K • 👍 399 • 💬 111 • ⏱️ 47:29 • 2d ago

---

**[XRP, Bitcoin, Ethereum Liquidations: My Prediction Was Right! #shorts](https://www.youtube.com/watch?v=SToP-VLgL4s)**

The market liquidations for XRP, Bitcoin, and Ethereum have arrived, just as predicted. Honesty and confronting issues are key to ...

📺 Martyn Lucas INVESTOR

👁️ 457 • 👍 18 • 💬 10 • ⏱️ 1:22 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
