---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-08-14T11:15:37.749778+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- social
- news
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** August 14, 2026 at 11:15 UTC  
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

### $1,885.89

---

## Ethereum Chart

**24h:** -0.7%  
**7d:** -2.2%  
**30d:** +0.6%  
**90d:** -12.0%  
**1y:** -57.8%  

---

## Ethereum Market Stats

**Market Cap:** $225.90B
Rank #2

**Circulating Supply:** 120,681,973 ETH
No max supply

**All-Time High:** $4,946.05
-62.2%

**All-Time Low:** $0.43
+432179.6%

---

## Reddit: r/ethereum

**[Daily General Discussion August 12, 2026](https://www.reddit.com/r/ethereum/comments/1vm4mto/daily_general_discussion_august_12_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion August 11, 2026](https://www.reddit.com/r/ethereum/comments/1vl7z30/daily_general_discussion_august_11_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Daily General Discussion August 10, 2026](https://www.reddit.com/r/ethereum/comments/1vkbhyh/daily_general_discussion_august_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[We built a free tool to monitor your ETH long on a lending protocol through Telegram (with health factor notifications too)](https://www.reddit.com/r/ethereum/comments/1vkisg2/we_built_a_free_tool_to_monitor_your_eth_long_on/)**

TL;DR: We built a free tool that lets you connect your lending protocol position to Telegram. From there, you can set up monitors that send you a Telegram notification based on your Health Ratio changes. For transparency sake - I'm part of the DeFi Saver team (that built this tool). My goal here is to share info about a free, useful tool we built - and not to shill any paid tool on our app. More context: I'm part of the DeFi Saver team - and our main focus is providing tools for lending protocol users. That said, I'm not here to shill any paid tool from our app. Instead, I'd like to share a completely free tool within our app that might be useful if you have an ETH long on Aave, Maker, Compound, Morpho, etc... It's a Telegram mini-app that lets you view your borrow position(s) directly from Telegram, and also set notifications when your position's Health Factor falls/increases to a certain % Point being - you don't have to visit any of the lending protocols directly, or use the DeFi Saver app. You can get all information about your position directly through Telegram. Links: Disclaimer - I totally understand apprehension for clicking random links you see on Reddit (especially crypto-related subreddits). As such, please feel free to find DeFi Saver on Twitter directly - as we'll share all relevant info/links there. This way, you're keeping yourself safe, and I really believe in being super careful when it comes to your portfolio. If you're okay with clicking links here, I'll just share some non-app links that have useful info (if you're interested in this tool): Twitter post with more info on the tool and link to the app: https://x.com/DeFiSaver/status/2085720327859122524 Knowledge Base guide on the tool: https://help.defisaver.com/features/notify/telegram-bot-for-monitoring-your-position Just to re-iterate, there's no hidden fee, catch, or anything when using this tool. We already have a healthy business model from our premium tools - so we're cool with just building neat, useful, and free tools for the DeFi community. Feel free to ask me any questions in the comments here :)

3d ago

---

**[CCA Monitor update: 6 chains, 5 real auctions, and a few things that broke along the way.](https://www.reddit.com/r/ethereum/comments/1vkaohy/cca_monitor_update_6_chains_5_real_auctions_and_a/)**

I’ve been building an open-source monitor for Capped Continuous Auctions (CCAs). What’s new: 6 chains monitored Ethereum, Base, Arbitrum, Unichain, Optimism, and Polygon. The monitor auto-detects new auctions across all factory contracts. Multi-channel alerts Telegram, Discord, Slack webhooks, and email via SendGrid. Whale bids, auction endings, daily digests. Auction comparison Compare up to 4 auctions side-by-side: clearing ratios, bidder overlap, concentration, and more. Post-graduation tracking Graduated tokens now get sparkline charts with -10%, -20%, and -30% alert bands. REST API Cloudflare Workers API with a free tier for basic data and a pro tier for concentration/overlap analytics. 4 of 5 real CCAs graduated. AKITA on Base was the first to fail. And honestly, that's a good thing. If every auction graduated, the mechanism wouldn't be doing much filtering. A failed auction is evidence that the graduation threshold actually matters. The more interesting signal is bidder overlap. Some wallets are showing up in almost every CCA. As more auctions launch, that cross-auction behavior could become one of the most valuable datasets from the monitor. And then things broke. polygon-rpc.com started returning 401s. They silently introduced API key requirements. Lesson: never depend on a single RPC provider. The monitor now has 2–3 fallback RPCs per chain and automatically fails over between Blockscout, dRPC, PublicNode, and others. Windows + PM2 started spawning console windows. The watchdog uses execSync to check PM2 status every 5 minutes. On Windows, that meant a console window popping up every time. One little windowsHide: true fixed it. Small problem. Surprisingly annoying. Viem's default RPCs went stale. If you don't explicitly configure an RPC, viem uses the chain's built-in default. Those endpoints can eventually stop working without much warning. The client factory now falls back to the monitor's public RPC list instead. Current state The whole thing is running on a Windows box: 4 PM2 processes ~250 MB RAM ~$0/month infrastructure 30-second polling Automatic auction detection Automatic analysis Automatic dashboard updates Waiting for the next wave of CCA launches. Dashboard: cca-monitor dashboard Repo: GitHub repository Dashboard and API are free. PRs welcome.

4d ago

---

**[Daily General Discussion August 09, 2026](https://www.reddit.com/r/ethereum/comments/1vjgud3/daily_general_discussion_august_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

5d ago

---

**[Daily General Discussion August 08, 2026](https://www.reddit.com/r/ethereum/comments/1vimypu/daily_general_discussion_august_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

6d ago

---

**[Daily General Discussion August 07, 2026](https://www.reddit.com/r/ethereum/comments/1vhr87x/daily_general_discussion_august_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

7d ago

---

**[Ethereal news weekly #34 | EIP8363 tapered issuance burn proposal, Dark Forest Aztec, MetaMask Agent Wallet](https://www.reddit.com/r/ethereum/comments/1vi1fba/ethereal_news_weekly_34_eip8363_tapered_issuance/)**

EIP8363 tapered issuance burn proposal, Dark Forest Aztec, MetaMask Agent Wallet

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-34/) • 6d ago

---

**[I rebuilt OGame on EVM, fully open source](https://www.reddit.com/r/ethereum/comments/1vhcq8d/i_rebuilt_ogame_on_evm_fully_open_source/)**

Hi folks! Been building on EVM chains since 2016, and finally got some free time to do something I've always wanted: rebuilding OGame (my favorite mid-2000 browser game) fully on EVM smart contracts! All open source (github.com/Borodutch/veydrift) and already has 69 commanders who did 92,798 transactions since the launch 30 days ago. Mechanics is classic OGame: you build mines, get resources, settle planets, join alliances, defend from raids and build fleets to raid other players! All three main resources are tokens and i'm building an inter-dimensional rift to extract these tokens from the game + inject the tokens from the open market. The game has been through countless iterations by now and includes a thing i call "lazy reconciliation" which allows to decrease number of transactions (i.e. when the resources accumulate, they are "collected" within the very next transaction a player submits before doing an action like sending ships, starting an upgrade, etc). It is the most complex system i've built on EVM (full on solidity) and I could use more testers trying to break the game! Lmk if you have any questions or comments :) I'm super happy to share my experience and chat about various EVM's. Cheers! https://preview.redd.it/vczwk5wssshh1.png?width=1696&format=png&auto=webp&s=ca676655064957ca32a4574e7662728245258686 https://preview.redd.it/5i5zbgdtsshh1.png?width=1696&format=png&auto=webp&s=d7ffa2fdd9c6d6fa86ea39b6159ea52d34bb484d https://preview.redd.it/oc4d74busshh1.png?width=1696&format=png&auto=webp&s=9c8b3feceed209aeca47ab3c18020b99df454ac6 https://preview.redd.it/su9wkbxvsshh1.png?width=1696&format=png&auto=webp&s=08b1171093244141b803bc53d6d407f13cae8e98

7d ago

---

---

## Google News: "ethereum"

**[Down 62% From Its Highs, Is Ethereum a Buy Right Now?](https://finance.yahoo.com/markets/crypto/articles/down-62-highs-ethereum-buy-105300199.html)**

There are still plenty of reasons to believe in the second-largest cryptocurrency.

Yahoo Finance • 22m ago

---

**[Current price of Ethereum for Aug. 14, 2026](https://fortune.com/article/price-of-ethereum-08-14-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 30m ago

---

**[Bitcoin Slides; Ethereum, XRP, Dogecoin Gain Amid Softer PPI Inflation: Crypto 'Dead' Chatter Shows Retai](https://www.benzinga.com/news/26/08/61200030/bitcoin-slides-ethereum-xrp-dogecoin-gain-amid-softer-ppi-inflation-crypto-dead-chatter-shows-retail-patience-breaking-says-market-intelligence-firm)**

Leading cryptocurrencies held steady on Thursday, August 13, while stocks climbed to record highs following softer-than-expected producer inflation data.

Benzinga • 9h ago

---

**[Ethereum staking climbs to 34% as proposal targets validator rewards and ETH treasury firm yields](https://www.theblock.co/news/ecosystems/2026-08-12-ethereum-staking-climbs-34-proposal-targets-validator-rewards-eth-treasury-firm-yields-411312)**

Researchers recently filed EIP-8361, a "tapered issuance burn" that destroys a growing share of validator rewards as the staking ratio rises.

The Block • 1d ago

---

**[FG Nexus dumped all its Ethereum at a $45 million loss](https://cryptoslate.com/fg-nexus-dumped-all-its-ethereum-at-a-45-million-loss-to-buy-mobile-home-parks-after-earning-just-144000-in-staking-rewards/)**

FG Nexus has sold its entire Ethereum portfolio and is shifting its capital into income-producing real estate.

CryptoSlate • 18h ago

---

**[Fidelity Files to Let Its Ethereum ETF Stake and Pay Investors](https://decrypt.co/375457/fidelity-files-ethereum-etf-stake-pay-investors)**

Fidelity wants its FETH fund to stake up to 100% of its Ethereum and distribute the rewards to holders as quarterly cash.

Decrypt • 1d ago

---

**[Here's why Bitcoin, Ethereum, XRP recovery is sluggish](https://www.fxstreet.com/cryptocurrencies/news/crypto-today-bitcoin-ethereum-xrp-remain-sluggish-amid-mixed-etf-flows-202608131100)**

The cryptocurrency market continues to trade sideways on Thursday, with Bitcoin (BTC) struggling to reclaim the $64,000 level. Ethereum (ETH) is attempting to build momentum near the key $1,900 resistance, while Ripple (XRP) maintains support above $1.00, yet upward movement remains limited.

FXStreet • 1d ago

---

**[Why Ethereum Price Could Skyrocket to $3,000 Within Days or Weeks](https://coinpedia.org/news/why-ethereum-could-skyrocket-to-3000-within-days-or-weeks/)**

Ethereum (ETH) is poised for a rally that could see its price skyrocket to $3,000 and beyond, a level last visited at the beginning of the year. Reasons

Coinpedia • 1d ago

---

**[What is Ultrasound Money? Understanding Ethereum’s Monetary Policy](https://financefeeds.com/what-is-ultrasound-money/)**

Ethereum's ultrasound money thesis relies on EIP-1559 burns exceeding new issuance, but Layer 2 scaling pushed ETH back into mild inflation.

FinanceFeeds • 12h ago

---

**[Ethereum: Staking Ratio Hits 34.4% as Exit Queue Nears Zero](https://blockchain.news/flashnews/ethereum-staking-ratio-hits-34-4-exit-queue-nears-zero)**

Ethereum staking ratio climbs to 34.4% with exit queue near zero, tightening ETH supply at $1877.99 amid bearish 4h chart signals.

blockchain.news • 30m ago

---

---

## YouTube Videos: "ethereum"

**[Crypto Holders - IT&#39;S A TRAP! Ethereum will EXPLODE!!?](https://www.youtube.com/watch?v=st_sKcHrVQw)**

"It's A Trap!" Crypto Expert WARNING To Bitcoin & Ethereum Holders ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily ...

📺 Altcoin Daily

👁️ 32K • 👍 2K • 💬 150 • ⏱️ 9:22 • 1d ago

---

**[ALT WARNING: 1ST TIME IN 6 YEARS](https://www.youtube.com/watch?v=meRlW9iUKYA)**

Trade Like A Tourist Or Join The Pros FFA Is Where The Real Ones Go https://cryptocrewuniversity.com/ffa DOMINATE ...

📺 Crypto Crew University

👁️ 24K • 👍 2K • 💬 164 • ⏱️ 8:55 • 22h ago

---

**[Ethereum Has Not Touched This Line Since October, $1,900 Decides Every Altcoin](https://www.youtube.com/watch?v=EtuZrQdyhow)**

Crypto Bull Market Comes Down To THIS Ethereum Test, Altcoins Lie In Wait... Intro 00:00 Crazy sideways 1:20 Ethereum price to ...

📺 Crypto Capital Venture

👁️ 6K • 👍 344 • 💬 190 • ⏱️ 11:59 • 1d ago

---

**[XRP And Ethereum Won&#39;t Be The Same After This The Buy Signals Are MASSIVE And People Don&#39;t See It](https://www.youtube.com/watch?v=QgzMrXRKNis)**

The public seems to be almost entirely unaware of the fact that not only are the very wealthy accumulating massive amounts of ...

📺 Money Rules - Investing Tips 

👁️ 13K • 👍 1K • 💬 415 • ⏱️ 12:21 • 23h ago

---

**[BITCOIN LIQUIDATIONS: DON&#39;T BE FOOLED (price target)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=NYLzSgpYBr4)**

BITCOIN LIQUIDATIONS: DON'T BE FOOLED (price target)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 5K • 👍 221 • 💬 108 • ⏱️ 18:22 • 16h ago

---

**[Lighter CEO: Why Robinhood Chain And Lighter Core Are Built On Ethereum (The Technical Thesis)](https://www.youtube.com/watch?v=YJ3iFvRts7c)**

Vladimir Novakovski breaks down why Lighter's separate instances for Robinhood Chain and Telegram Wallet create a unified ...

📺 The Rollup

👁️ 841 • 👍 25 • 💬 4 • ⏱️ 10:10 • 12h ago

---

**[ETHEREUM: TIME TO LOCK IN](https://www.youtube.com/watch?v=P7co89RhibM)**

The outlook on Ethereum and the crypto market at the moment. Today, we will discuss the current charts of Bitcoin and the altcoin ...

📺 Jordan Camirand

👁️ 9K • 👍 513 • 💬 218 • ⏱️ 19:05 • 2d ago

---

**[Bitcoin, Ethereum &amp; Chainlink BIG Move Incoming](https://www.youtube.com/watch?v=035ENTeXpiE)**

Bitcoin, Ethereum, and Chainlink could be setting up for a BIG move as the crypto market enters a critical zone! We break down ...

📺 Discover Crypto

👁️ 5K • 👍 257 • 💬 47 • ⏱️ 1:01:54 • 1d ago

---

**[MAJOR Ripple XRP Federal Reserve News Just Dropped Solana &amp; Ethereum Holders Are About To Be Happy](https://www.youtube.com/watch?v=MbN-GNPVioY)**

Well, it looks like 3 altcoins are taking center state in the world of the cryptocurrency market. Companies have continually ...

📺 The Modern Investor

👁️ 6K • 👍 587 • 💬 94 • ⏱️ 30:14 • 2d ago

---

**[Is Ethereum Preparing for a Breakout or Another Rejection?](https://www.youtube.com/watch?v=8YEpkqqKUCo)**

Bybit is currently running a limited promotion for the MCO community. Deposit at least $100 within 30 days and receive $25 worth ...

📺 More Crypto Online

👁️ 4K • 👍 201 • 💬 12 • ⏱️ 7:07 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
