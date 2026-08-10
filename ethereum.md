---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-08-10T08:26:45.752140+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- news
- videos
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** August 10, 2026 at 08:26 UTC  
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

### $1,926.70

---

## Ethereum Chart

**24h:** +0.3%  
**7d:** +3.0%  
**30d:** +6.7%  
**90d:** -14.7%  
**1y:** -54.5%  

---

## Ethereum Market Stats

**Market Cap:** $232.38B
Rank #2

**Circulating Supply:** 120,682,058 ETH
No max supply

**All-Time High:** $4,946.05
-61.1%

**All-Time Low:** $0.43
+444621.3%

---

## Reddit: r/ethereum

**[Daily General Discussion August 10, 2026](https://www.reddit.com/r/ethereum/comments/1vkbhyh/daily_general_discussion_august_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3h ago

---

**[Daily General Discussion August 09, 2026](https://www.reddit.com/r/ethereum/comments/1vjgud3/daily_general_discussion_august_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[CCA Monitor update: 6 chains, 5 real auctions, and a few things that broke along the way.](https://www.reddit.com/r/ethereum/comments/1vkaohy/cca_monitor_update_6_chains_5_real_auctions_and_a/)**

I’ve been building an open-source monitor for Capped Continuous Auctions (CCAs). What’s new: 6 chains monitored Ethereum, Base, Arbitrum, Unichain, Optimism, and Polygon. The monitor auto-detects new auctions across all factory contracts. Multi-channel alerts Telegram, Discord, Slack webhooks, and email via SendGrid. Whale bids, auction endings, daily digests. Auction comparison Compare up to 4 auctions side-by-side: clearing ratios, bidder overlap, concentration, and more. Post-graduation tracking Graduated tokens now get sparkline charts with -10%, -20%, and -30% alert bands. REST API Cloudflare Workers API with a free tier for basic data and a pro tier for concentration/overlap analytics. 4 of 5 real CCAs graduated. AKITA on Base was the first to fail. And honestly, that's a good thing. If every auction graduated, the mechanism wouldn't be doing much filtering. A failed auction is evidence that the graduation threshold actually matters. The more interesting signal is bidder overlap. Some wallets are showing up in almost every CCA. As more auctions launch, that cross-auction behavior could become one of the most valuable datasets from the monitor. And then things broke. polygon-rpc.com started returning 401s. They silently introduced API key requirements. Lesson: never depend on a single RPC provider. The monitor now has 2–3 fallback RPCs per chain and automatically fails over between Blockscout, dRPC, PublicNode, and others. Windows + PM2 started spawning console windows. The watchdog uses execSync to check PM2 status every 5 minutes. On Windows, that meant a console window popping up every time. One little windowsHide: true fixed it. Small problem. Surprisingly annoying. Viem's default RPCs went stale. If you don't explicitly configure an RPC, viem uses the chain's built-in default. Those endpoints can eventually stop working without much warning. The client factory now falls back to the monitor's public RPC list instead. Current state The whole thing is running on a Windows box: 4 PM2 processes ~250 MB RAM ~$0/month infrastructure 30-second polling Automatic auction detection Automatic analysis Automatic dashboard updates Waiting for the next wave of CCA launches. Dashboard: cca-monitor dashboard Repo: GitHub repository Dashboard and API are free. PRs welcome.

4h ago

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

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-34/) • 2d ago

---

**[I rebuilt OGame on EVM, fully open source](https://www.reddit.com/r/ethereum/comments/1vhcq8d/i_rebuilt_ogame_on_evm_fully_open_source/)**

Hi folks! Been building on EVM chains since 2016, and finally got some free time to do something I've always wanted: rebuilding OGame (my favorite mid-2000 browser game) fully on EVM smart contracts! All open source (github.com/Borodutch/veydrift) and already has 69 commanders who did 92,798 transactions since the launch 30 days ago. Mechanics is classic OGame: you build mines, get resources, settle planets, join alliances, defend from raids and build fleets to raid other players! All three main resources are tokens and i'm building an inter-dimensional rift to extract these tokens from the game + inject the tokens from the open market. The game has been through countless iterations by now and includes a thing i call "lazy reconciliation" which allows to decrease number of transactions (i.e. when the resources accumulate, they are "collected" within the very next transaction a player submits before doing an action like sending ships, starting an upgrade, etc). It is the most complex system i've built on EVM (full on solidity) and I could use more testers trying to break the game! Lmk if you have any questions or comments :) I'm super happy to share my experience and chat about various EVM's. Cheers! https://preview.redd.it/vczwk5wssshh1.png?width=1696&format=png&auto=webp&s=ca676655064957ca32a4574e7662728245258686 https://preview.redd.it/5i5zbgdtsshh1.png?width=1696&format=png&auto=webp&s=d7ffa2fdd9c6d6fa86ea39b6159ea52d34bb484d https://preview.redd.it/oc4d74busshh1.png?width=1696&format=png&auto=webp&s=9c8b3feceed209aeca47ab3c18020b99df454ac6 https://preview.redd.it/su9wkbxvsshh1.png?width=1696&format=png&auto=webp&s=08b1171093244141b803bc53d6d407f13cae8e98

3d ago

---

**[Daily General Discussion August 06, 2026](https://www.reddit.com/r/ethereum/comments/1vgupjx/daily_general_discussion_august_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[Dev Tools Guild July 2026 update | Solidity 0.8.36 adds Amsterdam EVM support. Sourcify passes 42M+ verified contracts. Foundry adds symbolic testing.](https://www.reddit.com/r/ethereum/comments/1vgubj5/dev_tools_guild_july_2026_update_solidity_0836/)**

**TL;DR**: Solidity 0.8.36 adds Amsterdam EVM support. Sourcify passes 42M+ verified contracts. Foundry adds symbolic testing.

🔗 [devtoolsguild.xyz](https://devtoolsguild.xyz/blog/devtoolsguild-july-2026-update) • 4d ago

---

**[We made a free tool to check if you have any lost tokens (ETH, USDC, etc...) waiting to be claimed](https://www.reddit.com/r/ethereum/comments/1vgb19k/we_made_a_free_tool_to_check_if_you_have_any_lost/)**

TL;DR and quick context - I work at DeFi Saver, and we built a completely free tool that lets you check if you have any smart wallets that have "lost tokens" sitting around waiting to be claimed. Just re-iterating, there are no strings attached - it's completely free and we quickly built it after realizing there was over $67M in unclaimed tokens sitting across 87,021 smart wallets. I'm just disclosing that I work for DFS to underscore that this isn't some hidden shill for DFS. No need to connect your wallet to the tool - just run your wallet address, check if you have tokens to claim - and claim them on DeFi Saver. The leftover tokens typically happen as leftover dust from DeFi transactions, long-forgotten airdrop (such as $UNI) or regular DeFi activity where you forgot the funds on your smart wallet. Full Info about the tool: We found over $67M in unclaimed tokens sitting in numerous smart wallets across the DeFi landscape. Not random tokens, but blue chip assets - including: $ETH - $3.4M $USDT - $6.9M $sUSDS - $10M $WBTC - $6M And many more. We then built a tool that lets you claim the tokens you forgot you had. Simply connect your main wallet to TokenSaver, check, and claim on DeFi Saver: https://tokensaver.fyi/ How do these assets end up in a smart wallet? Option 1: When you manage your lending position through a DeFi app (such as DeFi Saver, Summer.Fi, Instadapp) - it utilizes a smart wallet in order to perform advanced transactions such as 1-tx leveraging, unwinding, and more. All of these advanced transactions typically require swapping an asset to pay back a flash loan. When these swaps happen - It's possible that it swaps a bit more than necessary to make sure the transaction goes through despite small price movement. Those leftover funds remain sitting in the smart wallet holding the position. Or, perhaps you have/had a Maker position? All Maker CDPs are held on DSProxy smart wallets, so it’s worth connecting your CDP owner wallet to TokenSaver - maybe there are some leftover funds waiting to be claimed. That’s up to 8 years of potentially accumulating assets that never ended up in your EOA wallet. Option 2: You were eligible for an airdrop and received it due to your DeFi activity - but because it was distributed to your smart wallet, you never realized it. There's currently over $5.5M in $UNI that were likely distributed this way - and are unclaimed to this day. Option 3: Through regular DeFi activity over the years - some funds might have ended up on your smart wallet, and due to smart wallets typically lacking dedicated frontends - you forgot about them. While Safe (Gnosis) smart wallets have a dedicated UI - some, such as DSProxy, DSA, and SummerFi proprietary wallets lack it. So, it’s possible you continued on your DeFi journey without ever realizing you had funds leftover on the smart wallet(s). Since smart wallets need to have an owner wallet - you should simply connect with your main wallet, and TokenSaver will find all smart wallets owned by it. Note for nested Safe owners - Please input your owner Safe’s address into TokenSaver, not your EOA. You can then access DeFi Saver through the Safe app and claim your funds that way. That's pretty much it! Please try the tool out and let me know if you found anything interesting, such as a bag that you never realized you had available to claim :)

4d ago

---

---

## Google News: "ethereum"

**[ETH news: Ethereum staking token weETH splits from restaking as rewards debate heats up](https://www.coindesk.com/tech/2026/08/07/ethereum-staking-token-weeth-splits-from-restaking-as-rewards-debate-heats-up)**

The move separates ordinary Ethereum staking from higher-risk restaking exposure as a new proposal to cap validator rewards divides the staking sector.

CoinDesk • 3d ago

---

**[Crypto News: Ethereum Based Pepeto Sells Out Another Crypto Presale Round in Record Time as Funding Tops $10.6 Million](https://markets.businessinsider.com/news/stocks/crypto-news-ethereum-based-pepeto-sells-out-another-crypto-presale-round-in-record-time-as-funding-tops-10-6-million-1036434608)**

DUBAI, United Arab Emirates, Aug.  10, 2026  (GLOBE NEWSWIRE) -- Pepeto, an Ethereum based project, is taking the spotlights in latest crypto news...

markets.businessinsider.com • 1h ago

---

**[Bitcoin, Ethereum and XRP Face a CLARITY Act Shock — 4 AI Models Predict the Winners and Losers](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-face-clarity-091738695.html)**

Four leading AI models expect the passage of the CLARITY Act to be broadly bullish for the crypto market. XRP has the greatest potential percentage ...

Yahoo Finance • 1d ago

---

**[Which Crypto Do AI Models Say to Buy Right Now: Bitcoin, Ethereum, or XRP?](https://247wallst.com/investing/cryptocurrency/2026/08/09/which-crypto-do-ai-models-say-to-buy-right-now-bitcoin-ethereum-or-xrp/)**

We gave ChatGPT and Claude live data on Bitcoin, Ethereum, and XRP and asked them to rank all three based on which is best to buy now.

24/7 Wall St. • 14h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC bulls strengthen, ETH eyes breakout, XRP rebounds](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-bulls-strengthen-eth-eyes-breakout-xrp-rebounds-202608100230)**

Bitcoin (BTC) and Ethereum (ETH) show signs of strength as bulls defend key support on Monday after gaining 2% and 1.3% in the previous week. Meanwhile, Ripple (XRP) recovers mildly at the start of the week on Monday after sliding over 5% last week.

FXStreet • 5h ago

---

**[Bitcoin, XRP, Solana and Tron beat Ethereum and Cardano every month since 2022 on investor buying](https://cryptoslate.com/bitcoin-xrp-solana-and-tron-beat-ethereum-and-cardano-every-month-since-2022-on-investor-buying/)**

CryptoRank data shows the same DCA strategy produced radically different outcomes across Bitcoin, Ethereum, XRP, Solana, Cardano and TRX.

CryptoSlate • 1d ago

---

**[BlackRock’s spot Ethereum ETF to undergo 1-for-3 reverse share split in October](https://www.theblock.co/news/markets/2026-08-04-blackrocks-spot-ethereum-etf-to-undergo-1-for-3-reverse-share-split-in-october-410663)**

The split will consolidate every three ETHA shares into one, increasing the fund’s per-share net asset value.

The Block • 5d ago

---

**[Bitcoin ETF pulls in $102M as Ethereum ETF adds $50M, while Solana and XRP sit idle](https://www.tradingview.com/news/cryptobriefing:a3219d691094b:0-bitcoin-etf-pulls-in-102m-as-ethereum-etf-adds-50m-while-solana-and-xrp-sit-idle/)**

US spot Bitcoin ETFs attracted roughly $102 million in net inflows on August 7, while their Ethereum counterparts pulled in about $50 million on the same day. Solana and XRP ETFs, meanwhile, recorded exactly zero net change.The Bitcoin figure is notable not just on its own but as part of a broader…

TradingView • 2d ago

---

**[1 Popular Cryptocurrency to Buy Before Its Next Massive Rally, According to 1 Wall Street Bull](https://www.fool.com/investing/2026/08/09/1-popular-cryptocurrency-to-buy-before-its-next-ma/)**

One bullish scenario calls for Ethereum to hit a price of $250,000. But just how likely is that?

fool.com • 14h ago

---

**[CLARITY Act Delay Means It's 'Pretty Much Dead,' Expert Says: Bitcoin, Ethereum Don't Care](https://www.benzinga.com/crypto/cryptocurrency/26/08/61046907/clarity-act-delay-means-its-pretty-much-dead-expert-says-bitcoin-ethereum-dont-care)**

Bitcoin and Ethereum remain resilient despite fading hopes for U.S. crypto legislation. Other altcoins, such as Solana and Dogecoin, are also performing well.

Benzinga • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Is the Ethereum Bull Market Already Here](https://www.youtube.com/watch?v=eKMWhhBxn9E)**

In this video I break down the current Ethereum price action to determine if we are entering a new bull market or facing a potential ...

📺 More Crypto Online

👁️ 6K • 👍 274 • 💬 8 • ⏱️ 7:37 • 1d ago

---

**[BITCOIN: IT&#39;S HAPPENING AGAIN (Liquidations Coming)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=9JIhxX94oBY)**

BITCOIN: IT'S HAPPENING AGAIN (Liquidations Coming)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 4K • 👍 215 • 💬 26 • ⏱️ 17:48 • 11h ago

---

**[THESE CRYPTOS COULD GO TO ZERO. BE CAREFUL IF YOU ARE HOLDING! #ethereum #xrp #crypto](https://www.youtube.com/watch?v=_lo2Njd0hNk)**

📺 CryptoWendyO

👁️ 10K • 👍 534 • 💬 22 • ⏱️ 1:29 • 1d ago

---

**[The Unthinkable Has Happened To Bitcoin &amp; Solana This Could Be Time For XRP &amp; Ethereum To Shine](https://www.youtube.com/watch?v=ol2fQMclVuY)**

This one is going to shock a lot of people within the cryptocurrency market. As more and more time goes on... it just becomes ...

📺 The Modern Investor

👁️ 6K • 👍 643 • 💬 105 • ⏱️ 33:45 • 1d ago

---

**[Ethereum ETH: Big Problems, No Solutions](https://www.youtube.com/watch?v=oIzNeKieY7w)**

I have serious concerns with Ethereum and I don't see how it works out over time — join the Family with me to talk through the big ...

📺 Jerry Banfield Crypto Reviews

👁️ 380 • 👍 13 • 💬 2 • ⏱️ 0:43 • 20h ago

---

**[Jesse Pollak: Why Base Will Make Ethereum Win Long-Term (Consumer Grade Scale)](https://www.youtube.com/watch?v=E3skTXfZ6_Q)**

Jesse Pollak joins us on CLARITY week to break down how Base is leading in trading, onchain finance, and payments. He also ...

📺 The Rollup

👁️ 2K • 👍 94 • 💬 6 • ⏱️ 25:29 • 10h ago

---

**[Ethereum Just Got A Security Upgrade That Could Make It Unstoppable](https://www.youtube.com/watch?v=JBPD6P3WMlY)**

Lean Ethereum introduces native recursive STARKs, post quantum cryptography, and a state redesign targeting 10x fee reduction ...

📺 Lark Davis

👁️ 3K • 👍 123 • 💬 12 • ⏱️ 1:08 • 2d ago

---

**[Ethereum’s Staking Yield Could Go to Zero](https://www.youtube.com/watch?v=851HcRILQBw)**

SPOTIFY PREMIUM RSS FEED | USE CODE: SPOTIFY24 https://bankless.cc/spotify-premium --- Ethereum's monetary policy is ...

📺 Bankless

👁️ 7K • 👍 230 • 💬 36 • ⏱️ 1:06:58 • 2d ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=mCd7Fu4GAuA)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 234 • 👍 38 • ⏱️ 7:52 • 4h ago

---

**[BEST INVESTMENT ADVICE! #xrp #ethereum #finance](https://www.youtube.com/watch?v=TZXeVdGLX9c)**

📺 CryptoWendyO

👁️ 2K • 👍 136 • 💬 2 • ⏱️ 1:00 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*
