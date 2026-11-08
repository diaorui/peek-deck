---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-08T06:57:36.640527+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- cryptocurrency
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** November 08, 2026 at 06:57 UTC  
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

### $2,232.79

---

## Ethereum Chart

**24h:** -0.6%  
**7d:** -0.9%  
**30d:** -10.9%  
**90d:** +18.6%  
**1y:** -37.7%  

---

## Ethereum Market Stats

**Market Cap:** $272.58B
Rank #2

**Circulating Supply:** 122,200,877 ETH
No max supply

**All-Time High:** $4,946.05
-54.9%

**All-Time Low:** $0.43
+515070.5%

---

## Reddit: r/ethereum

**[Daily General Discussion November 04, 2026](https://www.reddit.com/r/ethereum/comments/1xngmbp/daily_general_discussion_november_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[Ethereum for digital public infrastructure](https://www.reddit.com/r/ethereum/comments/1xmpq8r/ethereum_for_digital_public_infrastructure/)**

Explore how Ethereum's open, global network can support digital public infrastructure, verifiable records, and coordination across institutions without a central operator.

🔗 [Ethereum for digital public infrastructure](https://publicsector.ethereum.foundation/) • 4d ago

---

**[Daily General Discussion November 03, 2026](https://www.reddit.com/r/ethereum/comments/1xml6ff/daily_general_discussion_november_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

5d ago

---

**[Are stablecoins becoming more useful than ETH for everyday payments?](https://www.reddit.com/r/ethereum/comments/1xlwz8b/are_stablecoins_becoming_more_useful_than_eth_for/)**

Most people seem to hold ETH as an investment, while USDT and USDC are increasingly being used for transfers and everyday payments. With more ways to spend crypto in real life now, I'm curious if anyone here pays with ETH or prefers using stablecoins. Do you think ETH will ever be widely used for everyday purchases or will stablecoins take that role?

5d ago

---

**[Daily General Discussion November 02, 2026](https://www.reddit.com/r/ethereum/comments/1xlpgqb/daily_general_discussion_november_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

6d ago

---

**[🚨 Ethereum solo stakers: CVE-2026-98432 is a critical Linux TCP vulnerability with potential remote root access.](https://www.reddit.com/r/ethereum/comments/1xlidhr/ethereum_solo_stakers_cve202698432_is_a_critical/)**

My Geth node had a publicly listening MPTCP socket. Disabling MPTCP didn't close existing listeners! Check ss -Mlntp, apply mitigations and patch your kernel ASAP. https://ubuntu.com/security/CVE-2026-98432

6d ago

---

**[Daily General Discussion November 01, 2026](https://www.reddit.com/r/ethereum/comments/1xkulhh/daily_general_discussion_november_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

7d ago

---

**[8 years ago a CREATE2 “Wisp” post asked what stops a bait and switch with selfdestruct. What actually changed?](https://www.reddit.com/r/ethereum/comments/1xl5h2q/8_years_ago_a_create2_wisp_post_asked_what_stops/)**

Found an old post on CREATE2 Wisp contracts (a contract created, used and selfdestructed in one call so the same address can run different code later) and the top question in the comments was what prevents someone from auditing one version and deploying another at the same address. The honest answer back then was “selfdestruct is a red flag, check Etherscan.” What happened since - the Tornado Cash governance attack in 2023 did exactly that and EIP-6780 (Dencun, March 2024) limited SELFDESTRUCT to contracts created in the same transaction. EIP-7702 (Pectra, May 2025) later let EOAs delegate to contract code. Does the Wisp pattern still work post-6780 (create, use and destroy in one tx) and is anyone using it? Is same-transaction metamorphism still a practical risk for governance or allowlists? And how are people checking code identity at execution time now, EXTCODEHASH at execution, something else? UPD thanks u/Bloqarl. So the Wisp pattern still works post-6780 because create and destroy happen in the same tx but swapping code at the same address across txs is dead and the bait and switch moved to upgradeable proxies (an EXTCODEHASH pin never changes while the logic does) and to 7702 accounts that can re-delegate in their next tx. Still curious how people pin code identity in practice

6d ago

---

**[Cool video on ethereum and quantum posted today.](https://www.reddit.com/r/ethereum/comments/1xkldwq/cool_video_on_ethereum_and_quantum_posted_today/)**

From the original post on x: Quantum computing poses a serious threat to the cryptography blockchains currently rely on, while advances in AI compress best estimates for the threat's timeline. That's why experts gathered in Cambridge to coordinate research upgrading our cryptography to be quantum-resistant.

7d ago

---

**[Anyone needs a devcon ticket ?](https://www.reddit.com/r/ethereum/comments/1xkrt7e/anyone_needs_a_devcon_ticket/)**

So the thing is I bought a devcon ticket but it seems like I won't be able to attend due to some emergency situation...in case anyone's willing to buy one for a discounted price, we can discuss Win win for both

7d ago

---

---

## Google News: "ethereum"

**[Crypto foundation demanded employees endorse suicide pledge, then fired leaders who objected, Colorado lawsuit alleges](https://www.denverpost.com/2026/11/06/ethereum-suicide-pledge-lawsuit-mandate-boulder-crypto/)**

On a Friday in March, employees at an international technology foundation received a 38-page document outlining leadership’s vision for the foundation for the next 1,000 years.

The Denver Post • 1d ago

---

**[EIP-8037/EIP-8038 Glamsterdam](https://blog.ethereum.org/2026/11/06/glamsterdam-8037-8038)**

In the previous weeks Chainsecurity has found a few projects that would be vulnerable after Glamsterdam since they rely on certain invariants. These invariants...

ethereum.org • 1d ago

---

**[Where Will Ethereum Be in 3 Years?](https://finance.yahoo.com/markets/crypto/articles/where-ethereum-3-years-190100780.html)**

Ethereum isn't broken; it's just slow. Here's why that matters over the next three years.

Yahoo Finance • 2d ago

---

**[Moscow Exchange sets December 1 to launch Bitcoin and Ethereum trading](https://cryptoslate.com/moscow-exchange-sets-dec-1-to-launch-bitcoin-and-ethereum-trading/)**

Russia's final Bitcoin, Ethereum, and USDT rules take effect Nov. 17, with retail purchase limits and testing.

CryptoSlate • 1d ago

---

**[1 Top Cryptocurrency to Buy Before It Soars by 11,000%, According to Bitmine's Tom Lee](https://www.fool.com/investing/2026/11/06/1-cryptocurrency-buy-soars-11000-bitmines-tom-lee/)**

Lee thinks the Ether cryptocurrency is entering a new era, and it could create significant value for investors.

The Motley Fool • 1d ago

---

**[How Low Could Bitcoin, Ethereum, and XRP Go If Crypto Keeps Dumping?](https://coinpedia.org/news/how-low-could-bitcoin-ethereum-and-xrp-go-if-crypto-keeps-dumping/)**

Since the start of this month, the global crypto market has lost more than $180 billion, bringing its total value down to $2.64 trillion. The drop comes

Coinpedia • 13h ago

---

**[Zilliqa: Builds vLEI Layer for Agentic Finance on Ethereum](https://blockchain.news/flashnews/zilliqa-builds-vlei-layer-agentic-finance-ethereum)**

Zilliqa detailed its push to establish verified legal entity identity infrastructure on Ethereum so AI agents can trade and settle on behalf of regulated...

Blockchain News • 1d ago

---

**[Grayscale says Ethereum leads smart contract platforms in stablecoins and tokenized assets](https://cryptobriefing.com/grayscale-ethereum-leads-stablecoins-tokenized-assets/)**

Grayscale Research says Ethereum leads smart contract platforms with nearly $140 billion in stablecoins and about 40% of tokenized assets.

Crypto Briefing • 14h ago

---

**[Is XRP a Good Investment Right Now at $1.18?](https://247wallst.com/investing/cryptocurrency/2026/11/06/is-xrp-a-good-investment-right-now-at-1-18/)**

XRP trades at $1.18, down sharply in 2026. Here's what needs to happen for it to reach $2 again and whether it's a smart investment now.

24/7 Wall St. • 1d ago

---

**[Bitmine Resumes Stock Buybacks As Ethereum Purchases Slow](https://finance.yahoo.com/markets/stocks/articles/bitmine-resumes-stock-buybacks-ethereum-144900850.html)**

Bitmine Immersion Technologies (NYSE: $BMNR) is ramping up its stock buybacks as it nears its goal of owning 5% of ...

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee: &quot;The Crypto Bull Market Just Started”, How ETH Hits $50,000](https://www.youtube.com/watch?v=lQPebhVEMlc)**

CNBC's Tom Lee (Fundstrat Founder, Bitmine CEO) shares his thoughts on crypto in 2027, AI bubble, ETH outlook, crypto ...

📺 Altcoin Daily

👁️ 43K • 👍 1K • 💬 114 • ⏱️ 28:10 • 8h ago

---

**[You&#39;re Not Ready For ETH&#39;s Come Back](https://www.youtube.com/watch?v=x1EFpB251gE)**

Ethereum could move before Bitcoin and lead the altcoin market out of this pullback. That's my thesis in this Sunday deep dive, ...

📺 Aaron Dishner aka Moonin Papa

👁️ 4K • 👍 246 • 💬 35 • ⏱️ 10:11 • 6h ago

---

**[XRP And Ethereum Are Involved &quot;It&#39;s Almost Done&quot; Crypto Holders Are In For The Shock Of Their Lives](https://www.youtube.com/watch?v=OqYKMVMwDz4)**

I can almost guarantee only 5% of you rememeber which blockchains Visa and Mastercard are going to be using to send trillions ...

📺 Money Rules - Investing Tips 

👁️ 37K • 👍 2K • 💬 321 • ⏱️ 11:45 • 18h ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=j5Wr41xwS7U)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 9K • 👍 198 • 💬 107 • ⏱️ 23:30 • 14h ago

---

**[Arthur Hayes: Ethereum Is Headed For A Historic Run (Bull Case)](https://www.youtube.com/watch?v=7IzqpFtFRuI)**

Arthur Hayes says the market has bottomed and belief is back: Wall Street money and AI agents are heading onchain.

📺 The Rollup

👁️ 22K • 👍 287 • 💬 5 • ⏱️ 9:00 • 2d ago

---

**[Tom Lee :&quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” | 2026 Crypto Prediction](https://www.youtube.com/watch?v=lRFhJK1McaI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 6K • 👍 109 • 💬 63 • ⏱️ 23:50 • 1d ago

---

**[I sold my Ethereum, here’s why](https://www.youtube.com/watch?v=mcrJu_BYqMw)**

AMERICANS LONG AND SHORT CRYPTO ON KALSHI - $25 FREE and 0.01% FEES ONLY WITH THIS LINK ...

📺 Lark Davis

👁️ 17K • 👍 302 • 💬 74 • ⏱️ 10:12 • 2d ago

---

**[I Built a Live Trading Bot with Claude Code AI (Ethereum AI Trading)](https://www.youtube.com/watch?v=1hoICfzfZoE)**

Full Tutorial Guide: https://tr.ee/q2uIoc Timeline: 00:00 - Results Preview 00:37 - Setup Guide and Platform 01:16 - Compile and ...

📺 Thomas Sutton

👁️ 6K • 👍 47 • 💬 31 • ⏱️ 5:59 • 22h ago

---

**[Bitcoin Investors Won&#39;t See This Coming Ethereum And Ripple Are Shaking Up The Cryptocurrency Market](https://www.youtube.com/watch?v=J6buGQxWwcU)**

How much Bitcoin and XRP do you think these companies and banks will own by the time we get to the year 2030? Not one single ...

📺 The Modern Investor

👁️ 8K • 👍 609 • 💬 102 • ⏱️ 30:21 • 20h ago

---

**[Ripple And XRP Are Making Major Moves And No One Notices Ethereum Is About To Become Mainstream](https://www.youtube.com/watch?v=ZInfCw1FagQ)**

Everyone out there is going to miss out on whats going on and its a shame. The cryptocurrency market has never seen this much ...

📺 The Modern Investor

👁️ 10K • 👍 756 • 💬 271 • ⏱️ 33:44 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
