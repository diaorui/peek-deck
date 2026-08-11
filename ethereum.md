---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-08-11T11:42:52.182768+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- news
- cryptocurrency
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** August 11, 2026 at 11:42 UTC  
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

### $1,881.07

---

## Ethereum Chart

**24h:** -1.7%  
**7d:** -1.1%  
**30d:** +6.2%  
**90d:** -17.3%  
**1y:** -58.9%  

---

## Ethereum Market Stats

**Market Cap:** $227.47B
Rank #2

**Circulating Supply:** 120,682,036 ETH
No max supply

**All-Time High:** $4,946.05
-61.9%

**All-Time Low:** $0.43
+435232.9%

---

## Reddit: r/ethereum

**[Daily General Discussion August 11, 2026](https://www.reddit.com/r/ethereum/comments/1vl7z30/daily_general_discussion_august_11_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

6h ago

---

**[Clients still don't get that smart contracts are immutable](https://www.reddit.com/r/ethereum/comments/1vkvjmp/clients_still_dont_get_that_smart_contracts_are/)**

it actually drives me insane. We deploy a massive dApp to mainnet, and literally two days later the client is like "can we just quickly edit the logic in this one function?" like no bro, that's the whole point of ethereum. I had to explain to a grown man that we can't just git push a hotfix to a live contract We actually ended up having to bring in an external dev shop cisin just to build out a whole complicated proxy contract architecture for their v2 because management flat out refuses to finalize business logic before we deploy things Im just so tired of web2 brain in web3 spaces. If one more project manager asks me to just "patch the blockchain real quick" i might actually throw my monitor out the window.

15h ago

---

**[Daily General Discussion August 10, 2026](https://www.reddit.com/r/ethereum/comments/1vkbhyh/daily_general_discussion_august_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[We built a free tool to monitor your ETH long on a lending protocol through Telegram (with health factor notifications too)](https://www.reddit.com/r/ethereum/comments/1vkisg2/we_built_a_free_tool_to_monitor_your_eth_long_on/)**

TL;DR: We built a free tool that lets you connect your lending protocol position to Telegram. From there, you can set up monitors that send you a Telegram notification based on your Health Ratio changes. For transparency sake - I'm part of the DeFi Saver team (that built this tool). My goal here is to share info about a free, useful tool we built - and not to shill any paid tool on our app. More context: I'm part of the DeFi Saver team - and our main focus is providing tools for lending protocol users. That said, I'm not here to shill any paid tool from our app. Instead, I'd like to share a completely free tool within our app that might be useful if you have an ETH long on Aave, Maker, Compound, Morpho, etc... It's a Telegram mini-app that lets you view your borrow position(s) directly from Telegram, and also set notifications when your position's Health Factor falls/increases to a certain % Point being - you don't have to visit any of the lending protocols directly, or use the DeFi Saver app. You can get all information about your position directly through Telegram. Links: Disclaimer - I totally understand apprehension for clicking random links you see on Reddit (especially crypto-related subreddits). As such, please feel free to find DeFi Saver on Twitter directly - as we'll share all relevant info/links there. This way, you're keeping yourself safe, and I really believe in being super careful when it comes to your portfolio. If you're okay with clicking links here, I'll just share some non-app links that have useful info (if you're interested in this tool): Twitter post with more info on the tool and link to the app: https://x.com/DeFiSaver/status/2085720327859122524 Knowledge Base guide on the tool: https://help.defisaver.com/features/notify/telegram-bot-for-monitoring-your-position Just to re-iterate, there's no hidden fee, catch, or anything when using this tool. We already have a healthy business model from our premium tools - so we're cool with just building neat, useful, and free tools for the DeFi community. Feel free to ask me any questions in the comments here :)

23h ago

---

**[CCA Monitor update: 6 chains, 5 real auctions, and a few things that broke along the way.](https://www.reddit.com/r/ethereum/comments/1vkaohy/cca_monitor_update_6_chains_5_real_auctions_and_a/)**

I’ve been building an open-source monitor for Capped Continuous Auctions (CCAs). What’s new: 6 chains monitored Ethereum, Base, Arbitrum, Unichain, Optimism, and Polygon. The monitor auto-detects new auctions across all factory contracts. Multi-channel alerts Telegram, Discord, Slack webhooks, and email via SendGrid. Whale bids, auction endings, daily digests. Auction comparison Compare up to 4 auctions side-by-side: clearing ratios, bidder overlap, concentration, and more. Post-graduation tracking Graduated tokens now get sparkline charts with -10%, -20%, and -30% alert bands. REST API Cloudflare Workers API with a free tier for basic data and a pro tier for concentration/overlap analytics. 4 of 5 real CCAs graduated. AKITA on Base was the first to fail. And honestly, that's a good thing. If every auction graduated, the mechanism wouldn't be doing much filtering. A failed auction is evidence that the graduation threshold actually matters. The more interesting signal is bidder overlap. Some wallets are showing up in almost every CCA. As more auctions launch, that cross-auction behavior could become one of the most valuable datasets from the monitor. And then things broke. polygon-rpc.com started returning 401s. They silently introduced API key requirements. Lesson: never depend on a single RPC provider. The monitor now has 2–3 fallback RPCs per chain and automatically fails over between Blockscout, dRPC, PublicNode, and others. Windows + PM2 started spawning console windows. The watchdog uses execSync to check PM2 status every 5 minutes. On Windows, that meant a console window popping up every time. One little windowsHide: true fixed it. Small problem. Surprisingly annoying. Viem's default RPCs went stale. If you don't explicitly configure an RPC, viem uses the chain's built-in default. Those endpoints can eventually stop working without much warning. The client factory now falls back to the monitor's public RPC list instead. Current state The whole thing is running on a Windows box: 4 PM2 processes ~250 MB RAM ~$0/month infrastructure 30-second polling Automatic auction detection Automatic analysis Automatic dashboard updates Waiting for the next wave of CCA launches. Dashboard: cca-monitor dashboard Repo: GitHub repository Dashboard and API are free. PRs welcome.

1d ago

---

**[Daily General Discussion August 09, 2026](https://www.reddit.com/r/ethereum/comments/1vjgud3/daily_general_discussion_august_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion August 08, 2026](https://www.reddit.com/r/ethereum/comments/1vimypu/daily_general_discussion_august_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Daily General Discussion August 07, 2026](https://www.reddit.com/r/ethereum/comments/1vhr87x/daily_general_discussion_august_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[Ethereal news weekly #34 | EIP8363 tapered issuance burn proposal, Dark Forest Aztec, MetaMask Agent Wallet](https://www.reddit.com/r/ethereum/comments/1vi1fba/ethereal_news_weekly_34_eip8363_tapered_issuance/)**

EIP8363 tapered issuance burn proposal, Dark Forest Aztec, MetaMask Agent Wallet

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-34/) • 3d ago

---

**[I rebuilt OGame on EVM, fully open source](https://www.reddit.com/r/ethereum/comments/1vhcq8d/i_rebuilt_ogame_on_evm_fully_open_source/)**

Hi folks! Been building on EVM chains since 2016, and finally got some free time to do something I've always wanted: rebuilding OGame (my favorite mid-2000 browser game) fully on EVM smart contracts! All open source (github.com/Borodutch/veydrift) and already has 69 commanders who did 92,798 transactions since the launch 30 days ago. Mechanics is classic OGame: you build mines, get resources, settle planets, join alliances, defend from raids and build fleets to raid other players! All three main resources are tokens and i'm building an inter-dimensional rift to extract these tokens from the game + inject the tokens from the open market. The game has been through countless iterations by now and includes a thing i call "lazy reconciliation" which allows to decrease number of transactions (i.e. when the resources accumulate, they are "collected" within the very next transaction a player submits before doing an action like sending ships, starting an upgrade, etc). It is the most complex system i've built on EVM (full on solidity) and I could use more testers trying to break the game! Lmk if you have any questions or comments :) I'm super happy to share my experience and chat about various EVM's. Cheers! https://preview.redd.it/vczwk5wssshh1.png?width=1696&format=png&auto=webp&s=ca676655064957ca32a4574e7662728245258686 https://preview.redd.it/5i5zbgdtsshh1.png?width=1696&format=png&auto=webp&s=d7ffa2fdd9c6d6fa86ea39b6159ea52d34bb484d https://preview.redd.it/oc4d74busshh1.png?width=1696&format=png&auto=webp&s=9c8b3feceed209aeca47ab3c18020b99df454ac6 https://preview.redd.it/su9wkbxvsshh1.png?width=1696&format=png&auto=webp&s=08b1171093244141b803bc53d6d407f13cae8e98

4d ago

---

---

## Google News: "ethereum"

**[Vitalik Buterin Says Ethereum Is Betting Its Future on Quantum Security and AI](https://decrypt.co/375285/vitalik-buterin-ethereum-betting-future-quantum-ai)**

The updated roadmap for Ethereum puts quantum resistance, privacy and AI-assisted formal verification at the center of technical ambitions.

Decrypt • 13h ago

---

**[Ethereum, Solana, Avalanche Are Booming, so Why Are Prices Down 50%?](https://coinmarketcap.com/academy/article/ethereum-solana-avalanche-booming-eth-sol-avax-tokens-down)**

Ethereum, Solana, and Avalanche usage is rising as fees fall. So why are ETH, SOL, and AVAX still down, and which metrics matter?

CoinMarketCap • 3d ago

---

**[Ethereum news: Bitmine (BMNR) buys $14 million in ETH as Tom Lee expects tailwind for crypto](https://www.coindesk.com/business/2026/08/10/bitmine-s-eth-buying-slows-as-tom-lee-s-firm-shifts-capital-to-share-buybacks)**

Chairman Tom Lee said easing financial conditions could support crypto, even as the CLARITY Act failed to reach a Senate vote before the August recess.

CoinDesk • 21h ago

---

**[Bitcoin, Ethereum and XRP Face a CLARITY Act Shock — 4 AI Models Predict the Winners and Losers](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-face-clarity-091738695.html)**

Four leading AI models expect the passage of the CLARITY Act to be broadly bullish for the crypto market. XRP has the greatest potential percentage ...

Yahoo Finance • 3d ago

---

**[Vitalik Buterin puts privacy and quantum resistance front and center in Ethereum’s latest roadmap](https://www.theblock.co/news/ecosystems/2026-08-10-vitalik-buterin-privacy-quantum-resistance-front-and-center-ethereum-latest-roadmap-411298)**

Buterin previously said the upgrades included in Lean Ethereum will form the protocol's “third major iteration.”

The Block • 19h ago

---

**['Everything Except Bitcoin Is Dead'? No, Watch ETH and SOL, Industry Veterans Say](https://www.tradingview.com/news/benzinga:803e6f560094b:0-everything-except-bitcoin-is-dead-no-watch-eth-and-sol-industry-veterans-say/)**

Crypto industry veterans are skeptical of a revival for altcoins but argue that Ethereum (CRYPTO: ETH) and Solana (CRYPTO: SOL) remain among the few assets with compelling long-term cases.Is Everything Except Bitcoin Dead?Speaking with Milk Road, Electric Capital co-founder Avichal Garg pushed back…

TradingView • 14h ago

---

**[Current price of Ethereum for August 10, 2026](https://fortune.com/article/price-of-ethereum-08-10-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 1d ago

---

**[Standard Chartered Targets LINK At $200, Joining Hyperbullish Bitcoin, Ethereum Calls](https://www.benzinga.com/crypto/cryptocurrency/26/08/61073855/standard-chartered-targets-link-at-200-joining-hyperbullish-bitcoin-ethereum-calls)**

Chainlink gets a $200 target from Standard Chartered as tokenization and DeFi growth could drive LINK fees 25-fold by 2030.

Benzinga • 22h ago

---

**[ProShares Ultra Ether ETF: Ethereum Needs A Trend, Not Just A Rebound (NYSEARCA:ETHT)](https://seekingalpha.com/article/4933942-proshares-ultra-ether-etf-ethereum-needs-a-trend-not-just-a-rebound)**

Seeking Alpha • 1d ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC bulls strengthen, ETH eyes breakout, XRP rebounds](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-bulls-strengthen-eth-eyes-breakout-xrp-rebounds-202608100230)**

Bitcoin (BTC) and Ethereum (ETH) show signs of strength as bulls defend key support on Monday after gaining 2% and 1.3% in the previous week. Meanwhile, Ripple (XRP) recovers mildly at the start of the week on Monday after sliding over 5% last week.

FXStreet • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Just Flipped](https://www.youtube.com/watch?v=hMIK9mFAwd8)**

GET ON KRAKEN TODAY kraken.com/lark?inviteCode=kjtfbzb3 A mysterious wallet just spent $50 million buying 25000 ETH ...

📺 Lark Davis

👁️ 12K • 👍 605 • 💬 91 • ⏱️ 6:34 • 23h ago

---

**[Ethereum’s New EIP Could Break DeFi](https://www.youtube.com/watch?v=NCvOUkryd1k)**

SPOTIFY PREMIUM RSS FEED | USE CODE: SPOTIFY24 https://bankless.cc/spotify-premium --- Ethereum's latest staking ...

📺 Bankless

👁️ 4K • 👍 129 • 💬 51 • ⏱️ 54:27 • 1d ago

---

**[ETH Flashing More Bearish Reversal Warning Signals](https://www.youtube.com/watch?v=UUpFHJ83ALI)**

Bitcoin remains the lead market signal as BTC tests its current structure, nearby support, and the levels that would confirm either ...

📺 Aaron Dishner aka Moonin Papa

👁️ 7K • 👍 595 • 💬 108 • ⏱️ 55:35 • 1d ago

---

**[Ethereum: Will this support zone hold or fail?](https://www.youtube.com/watch?v=FCYdxhDLbgM)**

In this video I break down the current Ethereum price action and provide a clear technical outlook on the ETH chart. We analyze ...

📺 More Crypto Online

👁️ 3K • 👍 186 • 💬 5 • ⏱️ 6:31 • 23h ago

---

**[THESE CRYPTOS COULD GO TO ZERO. BE CAREFUL IF YOU ARE HOLDING! #ethereum #xrp #crypto](https://www.youtube.com/watch?v=_lo2Njd0hNk)**

📺 CryptoWendyO

👁️ 12K • 👍 637 • 💬 28 • ⏱️ 1:29 • 2d ago

---

**[CLARITY Act delay, Ethereum roadmap update and Solstice Finance STRC product](https://www.youtube.com/watch?v=38SenhMRpk8)**

CLARITY Act delay, Ethereum roadmap update and Solstice Finance STRC product The CLARITY Act's vote moves to after the ...

📺 The Coin Daily

👁️ 2K • ⏱️ 5:58 • 18h ago

---

**[Is the Ethereum Bull Market Already Here](https://www.youtube.com/watch?v=eKMWhhBxn9E)**

In this video I break down the current Ethereum price action to determine if we are entering a new bull market or facing a potential ...

📺 More Crypto Online

👁️ 6K • 👍 286 • 💬 8 • ⏱️ 7:37 • 2d ago

---

**[Bitcoin&#39;s 200-Week Indicator: MASSIVE Buy Opportunity Revealed! #shorts](https://www.youtube.com/watch?v=C74YloRR-Iw)**

The 200-week moving average has historically signaled major buying opportunities in crypto. Bitcoin and ETH are key vehicles for ...

📺 CryptoLabs Research | Defi Income & Investing

👁️ 411 • 👍 6 • 💬 1 • ⏱️ 0:49 • 10h ago

---

**[Ethereum ETH: Big Problems, No Solutions](https://www.youtube.com/watch?v=oIzNeKieY7w)**

I have serious concerns with Ethereum and I don't see how it works out over time — join the Family with me to talk through the big ...

📺 Jerry Banfield Crypto Reviews

👁️ 530 • 👍 16 • 💬 2 • ⏱️ 0:43 • 1d ago

---

**[📈 ETH Supply Shrinks While Dollar Grows 6.8%](https://www.youtube.com/watch?v=Ak6naqsVZ0A)**

Ethereum is quietly becoming one of the scarcest assets on the planet. The math between a shrinking supply and an expanding ...

📺 Gerhard - Bitcoin Strategy

👁️ 330 • 👍 9 • 💬 1 • ⏱️ 1:23 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*
