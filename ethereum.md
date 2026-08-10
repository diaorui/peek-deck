---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-08-10T14:58:27.773027+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** August 10, 2026 at 14:58 UTC  
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

### $1,907.04

---

## Ethereum Chart

**24h:** -1.7%  
**7d:** +1.2%  
**30d:** +4.8%  
**90d:** -16.2%  
**1y:** -55.2%  

---

## Ethereum Market Stats

**Market Cap:** $228.46B
Rank #2

**Circulating Supply:** 120,682,058 ETH
No max supply

**All-Time High:** $4,946.05
-61.7%

**All-Time Low:** $0.43
+436969.7%

---

## Reddit: r/ethereum

**[Daily General Discussion August 10, 2026](https://www.reddit.com/r/ethereum/comments/1vkbhyh/daily_general_discussion_august_10_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

9h ago

---

**[Daily General Discussion August 09, 2026](https://www.reddit.com/r/ethereum/comments/1vjgud3/daily_general_discussion_august_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[CCA Monitor update: 6 chains, 5 real auctions, and a few things that broke along the way.](https://www.reddit.com/r/ethereum/comments/1vkaohy/cca_monitor_update_6_chains_5_real_auctions_and_a/)**

I’ve been building an open-source monitor for Capped Continuous Auctions (CCAs). What’s new: 6 chains monitored Ethereum, Base, Arbitrum, Unichain, Optimism, and Polygon. The monitor auto-detects new auctions across all factory contracts. Multi-channel alerts Telegram, Discord, Slack webhooks, and email via SendGrid. Whale bids, auction endings, daily digests. Auction comparison Compare up to 4 auctions side-by-side: clearing ratios, bidder overlap, concentration, and more. Post-graduation tracking Graduated tokens now get sparkline charts with -10%, -20%, and -30% alert bands. REST API Cloudflare Workers API with a free tier for basic data and a pro tier for concentration/overlap analytics. 4 of 5 real CCAs graduated. AKITA on Base was the first to fail. And honestly, that's a good thing. If every auction graduated, the mechanism wouldn't be doing much filtering. A failed auction is evidence that the graduation threshold actually matters. The more interesting signal is bidder overlap. Some wallets are showing up in almost every CCA. As more auctions launch, that cross-auction behavior could become one of the most valuable datasets from the monitor. And then things broke. polygon-rpc.com started returning 401s. They silently introduced API key requirements. Lesson: never depend on a single RPC provider. The monitor now has 2–3 fallback RPCs per chain and automatically fails over between Blockscout, dRPC, PublicNode, and others. Windows + PM2 started spawning console windows. The watchdog uses execSync to check PM2 status every 5 minutes. On Windows, that meant a console window popping up every time. One little windowsHide: true fixed it. Small problem. Surprisingly annoying. Viem's default RPCs went stale. If you don't explicitly configure an RPC, viem uses the chain's built-in default. Those endpoints can eventually stop working without much warning. The client factory now falls back to the monitor's public RPC list instead. Current state The whole thing is running on a Windows box: 4 PM2 processes ~250 MB RAM ~$0/month infrastructure 30-second polling Automatic auction detection Automatic analysis Automatic dashboard updates Waiting for the next wave of CCA launches. Dashboard: cca-monitor dashboard Repo: GitHub repository Dashboard and API are free. PRs welcome.

10h ago

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

**[Bitcoin and ethereum prices today, Monday, August 10, 2026: BTC breaking past $65,000 yet again](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-monday-august-10-2026-btc-breaking-past-65000-yet-again-125722282.html)**

Bitcoin opened at $64,848.91 on Monday, August 10, 2026, 0.1% lower than Sunday's opening price. As of 8:43 a.m. ET this morning, bitcoin rose to $64,935.75. Ethereum opened at $1,908.93, down 0.3% from Sunday's opening price. The price of ethereum moved up to $1,913.13 this morning.

Yahoo Finance • 2h ago

---

**[Tom Lee's Bitmine Buys $14M in Ethereum as Cash Falls to $104M](https://finance.yahoo.com/markets/crypto/articles/tom-lees-bitmine-buys-14m-141212525.html)**

Bitmine has reported 4.8% of the supply for five straight weeks, leaving its 'Alchemy of 5%' target roughly 230,000 tokens away.

Yahoo Finance • 46m ago

---

**[Ethereum, Solana, Avalanche Are Booming, so Why Are Prices Down 50%?](https://coinmarketcap.com/academy/article/ethereum-solana-avalanche-booming-eth-sol-avax-tokens-down)**

Ethereum, Solana, and Avalanche usage is rising as fees fall. So why are ETH, SOL, and AVAX still down, and which metrics matter?

CoinMarketCap • 2d ago

---

**[Which Crypto Do AI Models Say to Buy Right Now: Bitcoin, Ethereum, or XRP?](https://247wallst.com/investing/cryptocurrency/2026/08/09/which-crypto-do-ai-models-say-to-buy-right-now-bitcoin-ethereum-or-xrp/)**

We gave ChatGPT and Claude live data on Bitcoin, Ethereum, and XRP and asked them to rank all three based on which is best to buy now.

24/7 Wall St. • 21h ago

---

**[Current price of Ethereum for August 10, 2026](https://fortune.com/article/price-of-ethereum-08-10-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 3h ago

---

**[Crypto News: Ethereum Based Pepeto Sells Out Another Crypto Presale Round in Record Time as Funding Tops $10.6 Million](https://markets.businessinsider.com/news/stocks/crypto-news-ethereum-based-pepeto-sells-out-another-crypto-presale-round-in-record-time-as-funding-tops-10-6-million-1036434608)**

DUBAI, United Arab Emirates, Aug.  10, 2026  (GLOBE NEWSWIRE) -- Pepeto, an Ethereum based project, is taking the spotlights in latest crypto news...

markets.businessinsider.com • 7h ago

---

**[ProShares Ultra Ether ETF: Ethereum Needs A Trend, Not Just A Rebound (NYSEARCA:ETHT)](https://seekingalpha.com/article/4933942-proshares-ultra-ether-etf-ethereum-needs-a-trend-not-just-a-rebound)**

Seeking Alpha • 4h ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC bulls strengthen, ETH eyes breakout, XRP rebounds](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-bulls-strengthen-eth-eyes-breakout-xrp-rebounds-202608100230)**

Bitcoin (BTC) and Ethereum (ETH) show signs of strength as bulls defend key support on Monday after gaining 2% and 1.3% in the previous week. Meanwhile, Ripple (XRP) recovers mildly at the start of the week on Monday after sliding over 5% last week.

FXStreet • 12h ago

---

**[Bitcoin and Ethereum ETFs break $1B in their best week since April and BlackRock brought in 80% of the cash](https://cryptoslate.com/bitcoin-and-ethereum-etfs-break-1b-in-their-best-week-since-april-and-blackrock-brought-in-80-of-the-cash/)**

Bitcoin and Ethereum ETFs attracted nearly $1.1 billion this week, their strongest combined inflows since April, with BlackRock taking most of the cash.

CryptoSlate • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Just Flipped](https://www.youtube.com/watch?v=hMIK9mFAwd8)**

GET ON KRAKEN TODAY kraken.com/lark?inviteCode=kjtfbzb3 A mysterious wallet just spent $50 million buying 25000 ETH ...

📺 Lark Davis

👁️ 3K • 👍 332 • 💬 27 • ⏱️ 6:34 • 2h ago

---

**[Is the Ethereum Bull Market Already Here](https://www.youtube.com/watch?v=eKMWhhBxn9E)**

In this video I break down the current Ethereum price action to determine if we are entering a new bull market or facing a potential ...

📺 More Crypto Online

👁️ 6K • 👍 281 • 💬 8 • ⏱️ 7:37 • 1d ago

---

**[Jesse Pollak: Why Base Will Make Ethereum Win Long-Term (Consumer Grade Scale)](https://www.youtube.com/watch?v=E3skTXfZ6_Q)**

Jesse Pollak joins us on CLARITY week to break down how Base is leading in trading, onchain finance, and payments. He also ...

📺 The Rollup

👁️ 3K • 👍 126 • 💬 11 • ⏱️ 25:29 • 17h ago

---

**[Live Crypto &amp; Gold Psychological Trading 10 Aug  ||  #bitcoin #ethereum #cryptotrading #gold](https://www.youtube.com/watch?v=JVOwOrhZRm0)**

TRADE IN CRYPTO AND GOLD SAFELY (CRYPTO/ Gold Token) :- https://india.delta.exchange/?code=JFWJTR Google ...

📺 Vibe With Sahil

👁️ 2K • 👍 345 • 59m ago

---

**[THESE CRYPTOS COULD GO TO ZERO. BE CAREFUL IF YOU ARE HOLDING! #ethereum #xrp #crypto](https://www.youtube.com/watch?v=_lo2Njd0hNk)**

📺 CryptoWendyO

👁️ 10K • 👍 565 • 💬 26 • ⏱️ 1:29 • 1d ago

---

**[The Unthinkable Has Happened To Bitcoin &amp; Solana This Could Be Time For XRP &amp; Ethereum To Shine](https://www.youtube.com/watch?v=ol2fQMclVuY)**

This one is going to shock a lot of people within the cryptocurrency market. As more and more time goes on... it just becomes ...

📺 The Modern Investor

👁️ 6K • 👍 651 • 💬 107 • ⏱️ 33:45 • 2d ago

---

**[BITCOIN: IT&#39;S HAPPENING AGAIN (Liquidations Coming)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=9JIhxX94oBY)**

BITCOIN: IT'S HAPPENING AGAIN (Liquidations Coming)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 6K • 👍 245 • 💬 76 • ⏱️ 17:48 • 17h ago

---

**[Ethereum Just Got A Security Upgrade That Could Make It Unstoppable](https://www.youtube.com/watch?v=JBPD6P3WMlY)**

Lean Ethereum introduces native recursive STARKs, post quantum cryptography, and a state redesign targeting 10x fee reduction ...

📺 Lark Davis

👁️ 4K • 👍 126 • 💬 12 • ⏱️ 1:08 • 2d ago

---

**[Ethereum | Ethereum Prediction | August 9 2026 | Ethereum Price Prediction | Ethereum Analysis Today](https://www.youtube.com/watch?v=rUSSSManu1Q)**

MEMBERS ONLY VIDEOS (Early Access) Get all 7 of today's Elliott Wave analysis videos immediately, not just the 2 that become ...

📺 Forex Forecast | Elliott Wave Analysis ReadyForex

👁️ 46 • 👍 2 • 💬 2 • ⏱️ 4:43 • 1d ago

---

**[BTC, ETH &amp; Shiba Inu | August 2026 Market Analysis](https://www.youtube.com/watch?v=ZZh7VZu4Kqc)**

Bitcoin, Ethereum & Shiba Inu ka August 2026 Market Analysis. Is video mein BTC ke 1D aur 4H charts ko dekhkar important ...

📺 TODAY CRYPTO

👁️ 483 • 👍 58 • 💬 8 • ⏱️ 12:08 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
