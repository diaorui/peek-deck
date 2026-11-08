---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-11-08T18:58:05.914205+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- cryptocurrency
- social
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** November 08, 2026 at 18:58 UTC  
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

### $2,230.00

---

## Ethereum Chart

**24h:** +0.0%  
**7d:** -0.8%  
**30d:** -10.8%  
**90d:** +18.7%  
**1y:** -37.7%  

---

## Ethereum Market Stats

**Market Cap:** $273.05B
Rank #2

**Circulating Supply:** 122,200,877 ETH
No max supply

**All-Time High:** $4,946.05
-54.8%

**All-Time Low:** $0.43
+515957.4%

---

## Reddit: r/ethereum

**[Daily General Discussion November 04, 2026](https://www.reddit.com/r/ethereum/comments/1xngmbp/daily_general_discussion_november_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[Ethereum for digital public infrastructure](https://www.reddit.com/r/ethereum/comments/1xmpq8r/ethereum_for_digital_public_infrastructure/)**

Explore how Ethereum's open, global network can support digital public infrastructure, verifiable records, and coordination across institutions without a central operator.

🔗 [Ethereum for digital public infrastructure](https://publicsector.ethereum.foundation/) • 5d ago

---

**[Daily General Discussion November 03, 2026](https://www.reddit.com/r/ethereum/comments/1xml6ff/daily_general_discussion_november_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

5d ago

---

**[Are stablecoins becoming more useful than ETH for everyday payments?](https://www.reddit.com/r/ethereum/comments/1xlwz8b/are_stablecoins_becoming_more_useful_than_eth_for/)**

Most people seem to hold ETH as an investment, while USDT and USDC are increasingly being used for transfers and everyday payments. With more ways to spend crypto in real life now, I'm curious if anyone here pays with ETH or prefers using stablecoins. Do you think ETH will ever be widely used for everyday purchases or will stablecoins take that role?

6d ago

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

7d ago

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

**[Zcash Price Is Flashing a Warning Sign for Bitcoin and Ethereum](https://beincrypto.com/ansem-zcash-price-weakness-bitcoin/)**

BeInCrypto • 17h ago

---

**[Crypto foundation demanded employees endorse suicide pledge, then fired leaders who objected, Colorado lawsuit alleges](https://www.denverpost.com/2026/11/06/ethereum-suicide-pledge-lawsuit-mandate-boulder-crypto/)**

On a Friday in March, employees at an international technology foundation received a 38-page document outlining leadership’s vision for the foundation for the next 1,000 years.

The Denver Post • 2d ago

---

**[In 5 Years, One of These Cryptocurrencies Could Be Worth More Than Bitcoin](https://www.fool.com/investing/2026/11/07/in-5-years-one-of-these-cryptocurrencies-could-be/)**

If Bitcoin hits one serious snag in particular, a few of its smaller competitors might have a shot at overcoming it.

The Motley Fool • 1d ago

---

**[EIP-8037/EIP-8038 Glamsterdam](https://blog.ethereum.org/2026/11/06/glamsterdam-8037-8038)**

In the previous weeks Chainsecurity has found a few projects that would be vulnerable after Glamsterdam since they rely on certain invariants. These invariants...

ethereum.org • 2d ago

---

**[Moscow Exchange sets December 1 to launch Bitcoin and Ethereum trading](https://cryptoslate.com/moscow-exchange-sets-dec-1-to-launch-bitcoin-and-ethereum-trading/)**

Russia's final Bitcoin, Ethereum, and USDT rules take effect Nov. 17, with retail purchase limits and testing.

CryptoSlate • 1d ago

---

**[Where Will Ethereum Be in 3 Years?](https://finance.yahoo.com/markets/crypto/articles/where-ethereum-3-years-190100780.html)**

Ethereum isn't broken; it's just slow. Here's why that matters over the next three years.

Yahoo Finance • 2d ago

---

**[Vitalik Buterin wants ETH to be a store of value, not a fee-burning token](https://cryptobriefing.com/vitalik-buterin-eth-store-of-value/)**

Vitalik Buterin says Ethereum should prioritize ETH as a store of value over fee burning, warning aggressive burns could risk centralization.

Crypto Briefing • 6h ago

---

**[1 Top Cryptocurrency to Buy Before It Soars by 11,000%, According to Bitmine's Tom Lee](https://www.fool.com/investing/2026/11/06/1-cryptocurrency-buy-soars-11000-bitmines-tom-lee/)**

Lee thinks the Ether cryptocurrency is entering a new era, and it could create significant value for investors.

The Motley Fool • 2d ago

---

**[Bitmine Resumes Stock Buybacks As Ethereum Purchases Slow](https://finance.yahoo.com/markets/stocks/articles/bitmine-resumes-stock-buybacks-ethereum-144900850.html)**

Bitmine Immersion Technologies (NYSE: $BMNR) is ramping up its stock buybacks as it nears its goal of owning 5% of ...

Yahoo Finance • 3d ago

---

**[Not Hyperliquid. Not Zcash. This Will Be the Top-Performing Cryptocurrency of 2027.](https://www.fool.com/investing/2026/11/05/not-x-not-y-this-will-be-the-top-performing-crypto/)**

If history is any guide, Ethereum will be one of the biggest winners during the next DeFi boom.

The Motley Fool • 3d ago

---

---

## YouTube Videos: "ethereum"

**[“It Started” Tom Lee Reveals The $50,000 Ethereum Endgame](https://www.youtube.com/watch?v=lQPebhVEMlc)**

CNBC's Tom Lee (Fundstrat Founder, Bitmine CEO) shares his thoughts on crypto in 2027, AI bubble, ETH outlook, crypto ...

📺 Altcoin Daily

👁️ 82K • 👍 2K • 💬 158 • ⏱️ 28:10 • 20h ago

---

**[You&#39;re Not Ready For ETH&#39;s Come Back](https://www.youtube.com/watch?v=x1EFpB251gE)**

Ethereum could move before Bitcoin and lead the altcoin market out of this pullback. That's my thesis in this Sunday deep dive, ...

📺 Aaron Dishner aka Moonin Papa

👁️ 9K • 👍 365 • 💬 50 • ⏱️ 10:11 • 18h ago

---

**[Tom Lee :&quot;This is Why ETH Is Going To $62,000 Per Coin, 1 ETH Will Be Huge!&quot;](https://www.youtube.com/watch?v=4H7pVbT5wRk)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 5K • 👍 69 • 💬 41 • ⏱️ 20:56 • 13h ago

---

**[XRP And Ethereum Are Involved &quot;It&#39;s Almost Done&quot; Crypto Holders Are In For The Shock Of Their Lives](https://www.youtube.com/watch?v=OqYKMVMwDz4)**

I can almost guarantee only 5% of you rememeber which blockchains Visa and Mastercard are going to be using to send trillions ...

📺 Money Rules - Investing Tips 

👁️ 42K • 👍 2K • 💬 447 • ⏱️ 11:45 • 1d ago

---

**[I Built a Live Trading Bot with Claude Code AI (Ethereum AI Trading)](https://www.youtube.com/watch?v=1hoICfzfZoE)**

Full Tutorial Guide: https://tr.ee/q2uIoc Timeline: 00:00 - Results Preview 00:37 - Setup Guide and Platform 01:16 - Compile and ...

📺 Thomas Sutton

👁️ 7K • 👍 63 • 💬 44 • ⏱️ 5:59 • 1d ago

---

**[Tom Lee :&quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” | 2026 Crypto Prediction](https://www.youtube.com/watch?v=lRFhJK1McaI)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 7K • 👍 113 • 💬 63 • ⏱️ 23:50 • 1d ago

---

**[Ethereum: The Final Drop of This Correction?](https://www.youtube.com/watch?v=W5wnnUYOJ2M)**

Sign up for Kalshi with our link: https://kalshi.com/p/morecryptoonline Paid partnership. US residents only (not available in the UK ...

📺 More Crypto Online

👁️ 7K • 👍 178 • 💬 10 • ⏱️ 6:44 • 1d ago

---

**[Arthur Hayes: Ethereum Is Headed For A Historic Run (Bull Case)](https://www.youtube.com/watch?v=7IzqpFtFRuI)**

Arthur Hayes says the market has bottomed and belief is back: Wall Street money and AI agents are heading onchain. Arthur ...

📺 The Rollup

👁️ 23K • 👍 294 • 💬 6 • ⏱️ 9:00 • 2d ago

---

**[HOW LIKELY IS AN ETHEREUM RALLY NOW?🔥 (ETH Update)](https://www.youtube.com/watch?v=G4kxWrRUkKk)**

ETHEREUM ETH PRICE PREDICTION 2026 Join my Premium Trading Group: https://whop.com/cilinix-crypto/cilinixpremium/ ...

📺 Cilinix Crypto

👁️ 314 • 👍 12 • 💬 1 • ⏱️ 4:40 • 8h ago

---

**[Raoul Pal Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [&quot;It&#39;s a Fake Crash&quot;]](https://www.youtube.com/watch?v=j5Wr41xwS7U)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 12K • 👍 227 • 💬 110 • ⏱️ 23:30 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
