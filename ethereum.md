---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-08-10T19:30:52.826601+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- cryptocurrency
- news
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** August 10, 2026 at 19:30 UTC  
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

### $1,877.93

---

## Ethereum Chart

**24h:** -2.1%  
**7d:** +0.5%  
**30d:** +4.1%  
**90d:** -16.8%  
**1y:** -55.6%  

---

## Ethereum Market Stats

**Market Cap:** $226.41B
Rank #2

**Circulating Supply:** 120,682,058 ETH
No max supply

**All-Time High:** $4,946.05
-62.1%

**All-Time Low:** $0.43
+433145.0%

---

## Reddit: r/ethereum

**[Daily General Discussion August 10, 2026](https://www.reddit.com/r/ethereum/comments/1vkbhyh/daily_general_discussion_august_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

14h ago

---

**[We built a free tool to monitor your ETH long on a lending protocol through Telegram (with health factor notifications too)](https://www.reddit.com/r/ethereum/comments/1vkisg2/we_built_a_free_tool_to_monitor_your_eth_long_on/)**

TL;DR: We built a free tool that lets you connect your lending protocol position to Telegram. From there, you can set up monitors that send you a Telegram notification based on your Health Ratio changes. For transparency sake - I'm part of the DeFi Saver team (that built this tool). My goal here is to share info about a free, useful tool we built - and not to shill any paid tool on our app. More context: I'm part of the DeFi Saver team - and our main focus is providing tools for lending protocol users. That said, I'm not here to shill any paid tool from our app. Instead, I'd like to share a completely free tool within our app that might be useful if you have an ETH long on Aave, Maker, Compound, Morpho, etc... It's a Telegram mini-app that lets you view your borrow position(s) directly from Telegram, and also set notifications when your position's Health Factor falls/increases to a certain % Point being - you don't have to visit any of the lending protocols directly, or use the DeFi Saver app. You can get all information about your position directly through Telegram. Links: Disclaimer - I totally understand apprehension for clicking random links you see on Reddit (especially crypto-related subreddits). As such, please feel free to find DeFi Saver on Twitter directly - as we'll share all relevant info/links there. This way, you're keeping yourself safe, and I really believe in being super careful when it comes to your portfolio. If you're okay with clicking links here, I'll just share some non-app links that have useful info (if you're interested in this tool): Twitter post with more info on the tool and link to the app: https://x.com/DeFiSaver/status/2085720327859122524 Knowledge Base guide on the tool: https://help.defisaver.com/features/notify/telegram-bot-for-monitoring-your-position Just to re-iterate, there's no hidden fee, catch, or anything when using this tool. We already have a healthy business model from our premium tools - so we're cool with just building neat, useful, and free tools for the DeFi community. Feel free to ask me any questions in the comments here :)

7h ago

---

**[Daily General Discussion August 09, 2026](https://www.reddit.com/r/ethereum/comments/1vjgud3/daily_general_discussion_august_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[CCA Monitor update: 6 chains, 5 real auctions, and a few things that broke along the way.](https://www.reddit.com/r/ethereum/comments/1vkaohy/cca_monitor_update_6_chains_5_real_auctions_and_a/)**

I’ve been building an open-source monitor for Capped Continuous Auctions (CCAs). What’s new: 6 chains monitored Ethereum, Base, Arbitrum, Unichain, Optimism, and Polygon. The monitor auto-detects new auctions across all factory contracts. Multi-channel alerts Telegram, Discord, Slack webhooks, and email via SendGrid. Whale bids, auction endings, daily digests. Auction comparison Compare up to 4 auctions side-by-side: clearing ratios, bidder overlap, concentration, and more. Post-graduation tracking Graduated tokens now get sparkline charts with -10%, -20%, and -30% alert bands. REST API Cloudflare Workers API with a free tier for basic data and a pro tier for concentration/overlap analytics. 4 of 5 real CCAs graduated. AKITA on Base was the first to fail. And honestly, that's a good thing. If every auction graduated, the mechanism wouldn't be doing much filtering. A failed auction is evidence that the graduation threshold actually matters. The more interesting signal is bidder overlap. Some wallets are showing up in almost every CCA. As more auctions launch, that cross-auction behavior could become one of the most valuable datasets from the monitor. And then things broke. polygon-rpc.com started returning 401s. They silently introduced API key requirements. Lesson: never depend on a single RPC provider. The monitor now has 2–3 fallback RPCs per chain and automatically fails over between Blockscout, dRPC, PublicNode, and others. Windows + PM2 started spawning console windows. The watchdog uses execSync to check PM2 status every 5 minutes. On Windows, that meant a console window popping up every time. One little windowsHide: true fixed it. Small problem. Surprisingly annoying. Viem's default RPCs went stale. If you don't explicitly configure an RPC, viem uses the chain's built-in default. Those endpoints can eventually stop working without much warning. The client factory now falls back to the monitor's public RPC list instead. Current state The whole thing is running on a Windows box: 4 PM2 processes ~250 MB RAM ~$0/month infrastructure 30-second polling Automatic auction detection Automatic analysis Automatic dashboard updates Waiting for the next wave of CCA launches. Dashboard: cca-monitor dashboard Repo: GitHub repository Dashboard and API are free. PRs welcome.

15h ago

---

**[Daily General Discussion August 08, 2026](https://www.reddit.com/r/ethereum/comments/1vimypu/daily_general_discussion_august_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion August 07, 2026](https://www.reddit.com/r/ethereum/comments/1vhr87x/daily_general_discussion_august_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Ethereal news weekly #34 | EIP8363 tapered issuance burn proposal, Dark Forest Aztec, MetaMask Agent Wallet](https://www.reddit.com/r/ethereum/comments/1vi1fba/ethereal_news_weekly_34_eip8363_tapered_issuance/)**

EIP8363 tapered issuance burn proposal, Dark Forest Aztec, MetaMask Agent Wallet

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-34/) • 3d ago

---

**[I rebuilt OGame on EVM, fully open source](https://www.reddit.com/r/ethereum/comments/1vhcq8d/i_rebuilt_ogame_on_evm_fully_open_source/)**

Hi folks! Been building on EVM chains since 2016, and finally got some free time to do something I've always wanted: rebuilding OGame (my favorite mid-2000 browser game) fully on EVM smart contracts! All open source (github.com/Borodutch/veydrift) and already has 69 commanders who did 92,798 transactions since the launch 30 days ago. Mechanics is classic OGame: you build mines, get resources, settle planets, join alliances, defend from raids and build fleets to raid other players! All three main resources are tokens and i'm building an inter-dimensional rift to extract these tokens from the game + inject the tokens from the open market. The game has been through countless iterations by now and includes a thing i call "lazy reconciliation" which allows to decrease number of transactions (i.e. when the resources accumulate, they are "collected" within the very next transaction a player submits before doing an action like sending ships, starting an upgrade, etc). It is the most complex system i've built on EVM (full on solidity) and I could use more testers trying to break the game! Lmk if you have any questions or comments :) I'm super happy to share my experience and chat about various EVM's. Cheers! https://preview.redd.it/vczwk5wssshh1.png?width=1696&format=png&auto=webp&s=ca676655064957ca32a4574e7662728245258686 https://preview.redd.it/5i5zbgdtsshh1.png?width=1696&format=png&auto=webp&s=d7ffa2fdd9c6d6fa86ea39b6159ea52d34bb484d https://preview.redd.it/oc4d74busshh1.png?width=1696&format=png&auto=webp&s=9c8b3feceed209aeca47ab3c18020b99df454ac6 https://preview.redd.it/su9wkbxvsshh1.png?width=1696&format=png&auto=webp&s=08b1171093244141b803bc53d6d407f13cae8e98

4d ago

---

**[Daily General Discussion August 06, 2026](https://www.reddit.com/r/ethereum/comments/1vgupjx/daily_general_discussion_august_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[Dev Tools Guild July 2026 update | Solidity 0.8.36 adds Amsterdam EVM support. Sourcify passes 42M+ verified contracts. Foundry adds symbolic testing.](https://www.reddit.com/r/ethereum/comments/1vgubj5/dev_tools_guild_july_2026_update_solidity_0836/)**

**TL;DR**: Solidity 0.8.36 adds Amsterdam EVM support. Sourcify passes 42M+ verified contracts. Foundry adds symbolic testing.

🔗 [devtoolsguild.xyz](https://devtoolsguild.xyz/blog/devtoolsguild-july-2026-update) • 4d ago

---

---

## Google News: "ethereum"

**[Ethereum, Solana, Avalanche Are Booming, so Why Are Prices Down 50%?](https://coinmarketcap.com/academy/article/ethereum-solana-avalanche-booming-eth-sol-avax-tokens-down)**

Ethereum, Solana, and Avalanche usage is rising as fees fall. So why are ETH, SOL, and AVAX still down, and which metrics matter?

CoinMarketCap • 2d ago

---

**[ETH news: Ethereum staking token weETH splits from restaking as rewards debate heats up](https://www.coindesk.com/tech/2026/08/07/ethereum-staking-token-weeth-splits-from-restaking-as-rewards-debate-heats-up)**

The move separates ordinary Ethereum staking from higher-risk restaking exposure as a new proposal to cap validator rewards divides the staking sector.

CoinDesk • 3d ago

---

**[1 Popular Cryptocurrency to Buy Before Its Next Massive Rally, According to 1 Wall Street Bull](https://finance.yahoo.com/markets/crypto/articles/1-popular-cryptocurrency-buy-next-172300623.html)**

One bullish scenario calls for Ethereum to hit a price of $250,000. But just how likely is that?

Yahoo Finance • 1d ago

---

**[Bitmine adds 7,391 ether in a week, bringing total Ethereum holdings to 5.81 million ETH](https://www.theblock.co/news/business/2026-08-10-bitmine-adds-7391-eth-411265)**

Bitmine bought 7,391 ether last week, lifting its total Ethereum treasury to 5.81 million ETH, worth roughly $11 billion.

The Block • 5h ago

---

**[Which Crypto Do AI Models Say to Buy Right Now: Bitcoin, Ethereum, or XRP?](https://247wallst.com/investing/cryptocurrency/2026/08/09/which-crypto-do-ai-models-say-to-buy-right-now-bitcoin-ethereum-or-xrp/)**

We gave ChatGPT and Claude live data on Bitcoin, Ethereum, and XRP and asked them to rank all three based on which is best to buy now.

24/7 Wall St. • 1d ago

---

**[Current price of Ethereum for August 10, 2026](https://fortune.com/article/price-of-ethereum-08-10-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 8h ago

---

**[Crypto News: Ethereum Based Pepeto Sells Out Another Crypto Presale Round in Record Time as Funding Tops $10.6 Million](https://markets.businessinsider.com/news/stocks/crypto-news-ethereum-based-pepeto-sells-out-another-crypto-presale-round-in-record-time-as-funding-tops-10-6-million-1036434608)**

DUBAI, United Arab Emirates, Aug.  10, 2026  (GLOBE NEWSWIRE) -- Pepeto, an Ethereum based project, is taking the spotlights in latest crypto news...

markets.businessinsider.com • 12h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC bulls strengthen, ETH eyes breakout, XRP rebounds](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-bulls-strengthen-eth-eyes-breakout-xrp-rebounds-202608100230)**

Bitcoin (BTC) and Ethereum (ETH) show signs of strength as bulls defend key support on Monday after gaining 2% and 1.3% in the previous week. Meanwhile, Ripple (XRP) recovers mildly at the start of the week on Monday after sliding over 5% last week.

FXStreet • 16h ago

---

**[Bitcoin and Ethereum ETFs break $1B in their best week since April and BlackRock brought in 80% of the cash](https://cryptoslate.com/bitcoin-and-ethereum-etfs-break-1b-in-their-best-week-since-april-and-blackrock-brought-in-80-of-the-cash/)**

Bitcoin and Ethereum ETFs attracted nearly $1.1 billion this week, their strongest combined inflows since April, with BlackRock taking most of the cash.

CryptoSlate • 2d ago

---

**[Ethereum roadmap update prioritizes quantum safety, privacy, native rollups](https://cryptobriefing.com/ethereum-roadmap-update-prioritizes-quantum-safety-privacy-native-rollups/)**

Vitalik Buterin updates Ethereum roadmap to focus on quantum safety and privacy. Ethereum reaching $6,500 by December 31, 2026 at 2.7% YES.

Crypto Briefing • 4h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Just Flipped](https://www.youtube.com/watch?v=hMIK9mFAwd8)**

GET ON KRAKEN TODAY kraken.com/lark?inviteCode=kjtfbzb3 A mysterious wallet just spent $50 million buying 25000 ETH ...

📺 Lark Davis

👁️ 7K • 👍 482 • 💬 69 • ⏱️ 6:34 • 7h ago

---

**[Ethereum’s New EIP Could Break DeFi](https://www.youtube.com/watch?v=NCvOUkryd1k)**

SPOTIFY PREMIUM RSS FEED | USE CODE: SPOTIFY24 https://bankless.cc/spotify-premium --- Ethereum's latest staking ...

📺 Bankless

👁️ 2K • 👍 98 • 💬 16 • ⏱️ 54:27 • 9h ago

---

**[Ethereum: Will this support zone hold or fail?](https://www.youtube.com/watch?v=FCYdxhDLbgM)**

In this video I break down the current Ethereum price action and provide a clear technical outlook on the ETH chart. We analyze ...

📺 More Crypto Online

👁️ 2K • 👍 157 • 💬 4 • ⏱️ 6:31 • 6h ago

---

**[THESE CRYPTOS COULD GO TO ZERO. BE CAREFUL IF YOU ARE HOLDING! #ethereum #xrp #crypto](https://www.youtube.com/watch?v=_lo2Njd0hNk)**

📺 CryptoWendyO

👁️ 11K • 👍 584 • 💬 26 • ⏱️ 1:29 • 1d ago

---

**[Is the Ethereum Bull Market Already Here](https://www.youtube.com/watch?v=eKMWhhBxn9E)**

In this video I break down the current Ethereum price action to determine if we are entering a new bull market or facing a potential ...

📺 More Crypto Online

👁️ 6K • 👍 284 • 💬 8 • ⏱️ 7:37 • 1d ago

---

**[Jesse Pollak: Why Base Will Make Ethereum Win Long-Term (Consumer Grade Scale)](https://www.youtube.com/watch?v=E3skTXfZ6_Q)**

Jesse Pollak joins us on CLARITY week to break down how Base is leading in trading, onchain finance, and payments. He also ...

📺 The Rollup

👁️ 4K • 👍 138 • 💬 11 • ⏱️ 25:29 • 21h ago

---

**[Bitcoin To $70K This Week? My Live ETH, SOL And NEAR Trades Explained](https://www.youtube.com/watch?v=bUEfz3gOvFw)**

Sheldon breaks down whether Bitcoin is ready for the next move toward $70K and what could be driving the market higher.

📺 Crypto Banter

👁️ 5K • 👍 367 • 💬 11 • ⏱️ 17:27 • 9h ago

---

**[BITCOIN: IT&#39;S HAPPENING AGAIN (Liquidations Coming)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=9JIhxX94oBY)**

BITCOIN: IT'S HAPPENING AGAIN (Liquidations Coming)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 6K • 👍 252 • 💬 83 • ⏱️ 17:48 • 22h ago

---

**[The Unthinkable Has Happened To Bitcoin &amp; Solana This Could Be Time For XRP &amp; Ethereum To Shine](https://www.youtube.com/watch?v=ol2fQMclVuY)**

This one is going to shock a lot of people within the cryptocurrency market. As more and more time goes on... it just becomes ...

📺 The Modern Investor

👁️ 6K • 👍 655 • 💬 118 • ⏱️ 33:45 • 2d ago

---

**[Is The Bottom In? 2022 Similarities? XRP, Bitcoin and Ethereum Liquidity and TA](https://www.youtube.com/watch?v=1ufDPxD9o74)**

Is this it? Subscribe to my Newsletter - https://theweeklyinsight.substack.com/ Get deep dives and insider crypto analysis delivered ...

📺 Cryptoinsightuk

👁️ 475 • 👍 56 • 💬 7 • ⏱️ 28:25 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
