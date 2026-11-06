---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-06T11:51:48.532097+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- social
- cryptocurrency
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** November 06, 2026 at 11:51 UTC  
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

**24h:** -6.1%  
**7d:** -0.5%  
**30d:** -9.2%  
**90d:** +17.6%  
**1y:** -34.6%  

---

## Ethereum Market Stats

**Market Cap:** $274.02B
Rank #2

**Circulating Supply:** 122,194,930 ETH
No max supply

**All-Time High:** $4,946.05
-54.7%

**All-Time Low:** $0.43
+517823.5%

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

3d ago

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

**[EIP-8037/EIP-8038 Glamsterdam](https://blog.ethereum.org/2026/11/06/glamsterdam-8037-8038)**

In the previous weeks Chainsecurity has found a few projects that would be vulnerable after Glamsterdam since they rely on certain invariants. These invariants...

ethereum.org • 1h ago

---

**[Crypto foundation demanded employees endorse suicide pledge, then fired leaders who objected, Colorado lawsuit alleges](https://www.denverpost.com/2026/11/06/ethereum-suicide-pledge-lawsuit-mandate-boulder-crypto/)**

On a Friday in March, employees at an international technology foundation received a 38-page document outlining leadership’s vision for the foundation for the next 1,000 years.

The Denver Post • 51m ago

---

**[Bitmine Resumes Stock Buybacks As Ethereum Purchases Slow](https://finance.yahoo.com/markets/stocks/articles/bitmine-resumes-stock-buybacks-ethereum-144900850.html)**

Bitmine Immersion Technologies (NYSE: $BMNR) is ramping up its stock buybacks as it nears its goal of owning 5% of ...

Yahoo Finance • 21h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Bleed Amid Broader Sell-Off: Analyst Says BTC Will Bottom After Sweeping This Level](https://www.tradingview.com/news/benzinga:49111096a094b:0-bitcoin-ethereum-xrp-dogecoin-bleed-amid-broader-sell-off-analyst-says-btc-will-bottom-after-sweeping-this-level/)**

Leading cryptocurrencies sank alongside stocks on Thursday as investors priced in AI sector risks following Democratic control of Congress.Crypto Market Does a U-TurnBitcoin cratered to $75,220, marking its lowest level since mid-September. Ethereum fell to roughly $2,230–$2,315, hitting its lowest…

TradingView • 9h ago

---

**[Current price of Ethereum for November 5, 2026](https://fortune.com/article/price-of-ethereum-11-05-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 22h ago

---

**[Ethereum’s decentralization model is the answer to an AI arms race: Vitalik Buterin](https://ambcrypto.com/ethereums-decentralization-model-is-the-answer-to-ai-arms-race-vitalik-buterin/)**

Ethereum’s decentralization could strengthen its long-term value as AI risks increase demand for open infrastructure.

AMBCrypto • 1d ago

---

**[Bitcoin squeezes higher as Ethereum momentum heats up](https://www.kitco.com/opinion/2026-11-05/bitcoin-squeezes-higher-ethereum-momentum-heats)**

.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position:…

Kitco • 20h ago

---

**[Not Hyperliquid. Not Zcash. This Will Be the Top-Performing Cryptocurrency of 2027.](https://www.fool.com/investing/2026/11/05/not-x-not-y-this-will-be-the-top-performing-crypto/)**

If history is any guide, Ethereum will be one of the biggest winners during the next DeFi boom.

The Motley Fool • 1d ago

---

**[Bitcoin and Ethereum ETFs lose $530 million in one day as $3 trillion Wall Street wipeout rattles crypto](https://cryptoslate.com/bitcoin-and-ethereum-etfs-lose-530-million-in-one-day-as-3-trillion-wall-street-wipeout-rattles-crypto/)**

US Bitcoin ETFs suffered $430 million in withdrawals, while Ethereum funds lost another $100 million as investors retreated from crypto.

CryptoSlate • 1h ago

---

**[ETH Price Prediction: Ethereum loses short-term trend support as derivatives stay long-biased](https://blockchain.news/news/20261106-price-prediction-eth-ethereum-loses-short-term-trend-support)**

Ethereum is trading at $2,220.01 after an 8.68% 24-hour drop, leaving price below the 7-day, 20-day, 50-day, 12-day EMA, and 26-day EMA while still above...

Blockchain News • 4h ago

---

---

## YouTube Videos: "ethereum"

**[Arthur Hayes: Ethereum Is Headed For A Historic Run (Bull Case)](https://www.youtube.com/watch?v=7IzqpFtFRuI)**

Arthur Hayes says the market has bottomed and belief is back: Wall Street money and AI agents are heading onchain.

📺 The Rollup

👁️ 7K • 👍 150 • 💬 60 • ⏱️ 9:00 • 12h ago

---

**[I sold my Ethereum, here’s why](https://www.youtube.com/watch?v=mcrJu_BYqMw)**

AMERICANS LONG AND SHORT CRYPTO ON KALSHI - $25 FREE and 0.01% FEES ONLY WITH THIS LINK ...

📺 Lark Davis

👁️ 10K • 👍 249 • 💬 47 • ⏱️ 10:12 • 14h ago

---

**[Why Ethereum Is Now Following the Amazon Playbook: Sharplink CEO](https://www.youtube.com/watch?v=tTM2FHu_2b0)**

Is Ethereum having its Amazon moment? Sharplink CEO Joseph Chalom believes investors may be making the same mistake ...

📺 Coinage

👁️ 16K • 👍 159 • 💬 82 • ⏱️ 20:55 • 1d ago

---

**[Ripple And XRP Are Making Major Moves And No One Notices Ethereum Is About To Become Mainstream](https://www.youtube.com/watch?v=ZInfCw1FagQ)**

Everyone out there is going to miss out on whats going on and its a shame. The cryptocurrency market has never seen this much ...

📺 The Modern Investor

👁️ 861 • 👍 191 • 💬 63 • ⏱️ 33:44 • 1h ago

---

**[Bitcoin And Ethereum Are Preparing For Something Massive Crypto Whales Are Doing The Unthinkable](https://www.youtube.com/watch?v=fI-6zqZly_M)**

When crypto prices fall, retail investors flee the market, unable to understand that something bigger is happening behind the ...

📺 The Modern Investor

👁️ 8K • 👍 677 • 💬 140 • ⏱️ 32:49 • 1d ago

---

**[Ethereum Price: Where This Correction Could End](https://www.youtube.com/watch?v=H6C2BP7r8pQ)**

Sign up for Kalshi with our link: https://kalshi.com/p/morecryptoonline Paid partnership. US residents only (not available in the UK ...

📺 More Crypto Online

👁️ 7K • 👍 200 • 💬 8 • ⏱️ 8:19 • 15h ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=qeo2K_BmmXI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 5K • 👍 98 • 💬 65 • ⏱️ 23:02 • 2d ago

---

**[Is Canton becoming a BETTER Ethereum? Here&#39;s What Changed!](https://www.youtube.com/watch?v=p33vSeCM7EQ)**

The SEC has classified Canton Coin as a commodity, not a security, and the Canton Network just launched its first meme coin ...

📺 Grow Rich Grow Happy

👁️ 2K • 👍 149 • 💬 14 • ⏱️ 22:00 • 1d ago

---

**[CRYPTO MARKET DUMPS! CZ BINANCE VS KEVIN O&#39;LEARY &amp; HUGE ETHEREUM &amp; SOLANA ADOPTION!](https://www.youtube.com/watch?v=_xRm-oXtH64)**

Crypto News: Bitcoin and the crypto market follow the stock market with a big dump. Binance and founder CZ subpoena Shark ...

📺 Thinking Crypto

👁️ 7K • 👍 376 • 💬 57 • ⏱️ 22:07 • 7h ago

---

**[IS CRYPTO SETTING UP FOR A RALLY? BITCOIN, XRP, ETHEREUM, &amp; CANTON NETWORK ANALYSIS!](https://www.youtube.com/watch?v=t6ZZoTZiGfc)**

Brian from Santiment joined me to break down the latest crypto market trends, key on-chain metrics, and investor sentiment for ...

📺 Thinking Crypto

👁️ 7K • 👍 215 • 💬 65 • ⏱️ 25:45 • 22h ago

---

---

*Generated by PeekDeck - A glance is all you need*
