---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-30T21:42:49.254122+00:00'
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

**Last Updated:** March 30, 2026 at 21:42 UTC  
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

### $2,070.42

---

## Ethereum Chart

**24h:** +3.5%  
**7d:** -5.2%  
**30d:** +5.4%  
**90d:** -31.3%  
**1y:** +11.8%  

---

## Ethereum Market Stats

**Market Cap:** $244.13B
Rank #2

**Circulating Supply:** 120,691,444 ETH
No max supply

**All-Time High:** $4,946.05
-59.1%

**All-Time Low:** $0.43
+467005.8%

---

## Reddit: r/ethereum

**[Daily General Discussion March 30, 2026](https://www.reddit.com/r/ethereum/comments/1s7hcs2/daily_general_discussion_march_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

16h ago

---

**[The hidden gas and security trade-offs of using CREATE2 + Minimal Proxies for multi-chain deployments](https://www.reddit.com/r/ethereum/comments/1s83w01/the_hidden_gas_and_security_tradeoffs_of_using/)**

Hey everyone, Over the last four years of writing smart contracts and teaching these concepts in EVM bootcamps, I keep seeing teams stumble into the exact same architectural traps when trying to achieve cross-chain address parity. Leveraging CREATE2 for deterministic addresses fundamentally changes how we handle multi-chain deployments. But because init_code includes constructor arguments, maintaining that exact same address across chains is impossible if you need to pass in chain-specific variables (like local router addresses or bridge endpoints). The standard industry workaround is deploying EIP-1167 Minimal Proxies via a universal factory, deploying deterministically, then initializing the state in the same transaction. However, this introduces some severe trade-offs that often get overlooked until they hit production: The DELEGATECALL Gas Tax: Minimal proxies are incredibly cheap to deploy (~45 bytes of bytecode), but they add a DELEGATECALL overhead to every single execution (2600 gas cold, 100 warm). At scale, this execution cost compounds brutally for your users. MEV Front-running Risks: If your proxy deployment and initialize() call are not strictly atomic within the factory contract execution, MEV bots might front-run the initialization transaction. This either bricks the instance entirely or hijacks the contract ownership. Immutability vs Upgradeability: To retain the exact same address while upgrading logic, you have to wrap the implementation in UUPS or Transparent Proxies. This inflates the initial deployment cost and introduces strict storage collision risks (requiring flawless adherence to EIP-1967 storage slots). I just published a full breakdown of these mechanics on my blog, diving into the math behind the gas trade-offs and how patterns like CREATE3 are solving the issue for non-proxy contracts where constructor arguments must differ. If you are currently architecting a multi-chain protocol, you can read the full technical deep dive here:https://andreyobruchkov1996.substack.com/p/understanding-contract-deployments-proxies-and-create2-part-2-df8f05998d5e Would love to hear how you all are handling cross-chain deterministic deployments right now. Are you still relying heavily on customized off-chain salt-mining scripts, or have you migrated to CREATE3 wrappers?

16m ago

---

**[EtherWorld Weekly — Edition 357](https://www.reddit.com/r/ethereum/comments/1s7mopy/etherworld_weekly_edition_357/)**

World News, Stories By EtherWorld, Technical Explainers, Client News & Updates, Podcasts, Upcoming Events & Jobs

🔗 [EtherWorld.co](https://etherworld.co/etherworld-weekly-edition-357/) • 11h ago

---

**[Daily General Discussion March 29, 2026](https://www.reddit.com/r/ethereum/comments/1s6m76c/daily_general_discussion_march_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Daily General Discussion March 28, 2026](https://www.reddit.com/r/ethereum/comments/1s5rbnm/daily_general_discussion_march_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Post-Quantum Ethereum client Lantern developer Pier Two acquired by BMNR](https://www.reddit.com/r/ethereum/comments/1s5pxbi/postquantum_ethereum_client_lantern_developer/)**

Effective March 25, 2026, Pier Two Holdings Pty Ltd has been wholly acquired by Bitmine Immersion Technologies, Inc (NYSE: BMNR)

🔗 [piertwo.com](https://piertwo.com/insights/pier-two-is-joining-mavan-a-bitmine-company) • 2d ago

---

**[Privacy preserving transaction verifier](https://www.reddit.com/r/ethereum/comments/1s5fd8h/privacy_preserving_transaction_verifier/)**

I Built a Privacy-Preserving Bitcoin transaction Receipt Verifier (No KYC, No Screenshots, No wallet). https://github.com/Teycir/Ghostreceipt Would like to have feedback.

3d ago

---

**[Daily General Discussion March 27, 2026](https://www.reddit.com/r/ethereum/comments/1s4uv0g/daily_general_discussion_march_27_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

---

**[Ethereal news weekly #17 | Frame transaction Considered for Inclusion for Hegotá, EthStaker staking survey, EF post-quantum website](https://www.reddit.com/r/ethereum/comments/1s53fx5/ethereal_news_weekly_17_frame_transaction/)**

Frame transaction Considered for Inclusion for Hegotá, EthStaker staking survey, EF post-quantum website

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-17/) • 3d ago

---

**[Highlights from the All Core Developers Execution (ACDE) Call #233](https://www.reddit.com/r/ethereum/comments/1s4s7lw/highlights_from_the_all_core_developers_execution/)**

Ethereum pushes Glamsterdam testing forward as Hegotá headliner debates remain unresolved.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-execution-acde-call-233/) • 3d ago

---

---

## Google News: "ethereum"

**[New Ethereum project aims to fix network fragmentation and improve user experience](https://www.coindesk.com/tech/2026/03/29/new-ethereum-project-aims-to-fix-network-fragmentation-and-improve-user-experience)**

The project is designed to make Ethereum’s many layer 2s work together more seamlessly.

CoinDesk • 1d ago

---

**[Gnosis and Zisk announce 'Ethereum Economic Zone' rollup framework with Ethereum Foundation co-funding](https://www.theblock.co/post/395578/gnosis-and-zisk-announce-ethereum-economic-zone-rollup-framework-with-ethereum-foundation-co-funding)**

The Ethereum Foundation is co-funding the "easy" initiative, which was announced at EthCC in Cannes, and partners include Aave, Titan, Centrifuge, and more.

The Block • 1d ago

---

**[Ethereum Foundation Stakes More ETH, Boosting Total to $50 Million](https://finance.yahoo.com/markets/crypto/articles/ethereum-foundation-stakes-more-eth-195247383.html)**

The Ethereum Foundation staked another $46 million ETH as part of its new treasury plan unveiled last year.

Yahoo Finance • 1h ago

---

**[Ethereum Funds Shed $222 Million as Crypto Bill Fears Rattle Investors](https://finance.yahoo.com/markets/crypto/articles/ethereum-funds-shed-222-million-174737564.html)**

Ethereum funds took the biggest hit as Clarity Act fears and macro headwinds pushed crypto outflows to $414 million for the week.

Yahoo Finance • 3h ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.732 Million Tokens, and Total Crypto and Total Cash Holdings of $10.7 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-732-million-tokens-and-total-crypto-and-total-cash-holdings-of-10-7-billion-302728176.html)**

Bitmine has 3,142,643 staked ETH, representing $6.3 billion at $2,005 per ETH MAVAN (Made in America VAlidator Network) launched staking solution on March 25,...

PR Newswire • 9h ago

---

**[Tom Lee's BitMine Adds More Ethereum as Strategy Takes a Break From Bitcoin Buying](https://finance.yahoo.com/markets/crypto/articles/tom-lees-bitmine-adds-more-144553148.html)**

BitMine continued its Ethereum accumulation, adding to its leading ETH treasury while Strategy took a week off from Bitcoin purchases.

Yahoo Finance • 6h ago

---

**[BMNR, ETH news: Bitmine buys 71,000 ETH as digital asset treasuries dial back purchases](https://www.coindesk.com/business/2026/03/30/bitmine-makes-biggest-ether-purchase-in-2026-while-other-digital-asset-treasuries-pull-back)**

Tom Lee's Ethereum treasury bought more than 71,000 ETH over the past week, remaining the sole large corporate crypto buyer as Strategy broke its 13-week bitcoin purchase streak.

CoinDesk • 6h ago

---

**[Ethereum vs. Solana: Which Crypto Has More Upside?](https://www.fool.com/investing/2026/03/28/ethereum-vs-solana-which-crypto-has-more-upside/)**

Ethereum's vast ecosystem goes up against Solana's lightning-quick network.

The Motley Fool • 2d ago

---

**[Ethereum (ETH) Price Holds $2K Support—Analyst Predicts Shocking $62,000 Target](https://www.tradingview.com/news/coinpedia:09b742ff2094b:0-ethereum-eth-price-holds-2k-support-analyst-predicts-shocking-62-000-target/)**

Ethereum’s volatility has picked up notably since the start of the month, reflecting a market caught between recovery attempts and persistent selling pressure. After rallying through the first half, the ETH price faced a firm rejection near $2,372, triggering a sharp pullback that erased a chunk of…

TradingView • 1d ago

---

**[Current price of Ethereum for March 30, 2026](https://fortune.com/article/price-of-ethereum-03-30-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 8h ago

---

---

## YouTube Videos: "ethereum"

**[LIVE: Tom Lee on Ethereum Crash &amp; BMNR Stock Drop - ETH Price Analysis](https://www.youtube.com/watch?v=6rR--df9psw)**

ETH #Ethereum #Cryptocurrency Join Tom Lee for his groundbreaking keynote at the Ethereum Conference.

📺 Elvis Nash

👁️ 2K • 👍 1K • 2h ago

---

**[LIVE: Tom Lee on Ethereum Crash &amp; BMNR Stock Drop - ETH Price Analysis](https://www.youtube.com/watch?v=5PZdYV1_FzI)**

ETH #Ethereum #Cryptocurrency Join Tom Lee for his groundbreaking keynote at the Ethereum Conference.

📺 The Boss Barber - Yudi

👁️ 2K • 👍 1K • 2h ago

---

**[🚨 BTC &amp; ETH: SELL ALL ASAP &amp; RUN!!!!!! (New disturbing data!)](https://www.youtube.com/watch?v=6bWLOUY6xAM)**

New data shows the future of markets and crypto in general. Its important for bitcoin, ethereum and so on. BEWARE!

📺 Thomas Kralow

👁️ 13K • 👍 2K • 💬 69 • ⏱️ 11:48 • 10h ago

---

**[LIVE: Tom Lee on Ethereum Crash &amp; BMNR Stock Drop - ETH Price Analysis](https://www.youtube.com/watch?v=ZJeCBwWl1Jw)**

ETH #Ethereum #Cryptocurrency Join Tom Lee for his groundbreaking keynote at the Ethereum Conference.

📺 James Vasanthan

👁️ 2K • 👍 1K • 3h ago

---

**[FINAL WARNING to ALL Crypto Holders!! (I will delete this in 24 hours)](https://www.youtube.com/watch?v=hzfc05Bphkk)**

If you hold Bitcoin or Ethereum... watch this! (alert!) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily BTC ...

📺 Altcoin Daily

👁️ 44K • 👍 2K • 💬 291 • ⏱️ 9:24 • 1d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=0mrjO9FKdbc)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 74 • 💬 9 • ⏱️ 3:53 • 9h ago

---

**[Former BlackRock Exec Reveals Ethereum&#39;s Future Outlook! | Joseph Chalom](https://www.youtube.com/watch?v=iOmQYMafYG0)**

Joseph Chalom, CEO of SharpLink, joined me to discuss the company's Ethereum treasury strategy and the future of ETH. Topics: ...

📺 Thinking Crypto

👁️ 1K • 👍 110 • 💬 143 • ⏱️ 55:54 • 9h ago

---

**[Ethereum to $40,000 by 2030: Why ETH Could MASSIVELY Outperform Bitcoin](https://www.youtube.com/watch?v=4ZjG0_XW0DU)**

Check prices, drink coffee, read Milk Road. It's the easiest 5-minute habit to stay smart on crypto: ...

📺 Milk Road

👁️ 7K • 👍 199 • 💬 60 • ⏱️ 11:06 • 2d ago

---

**[Why Banks Don&#39;t Want Ethereum or Solana — And What They Actually Need](https://www.youtube.com/watch?v=WPtXmFrLrto)**

At the Digital Asset Summit 2026 in New York, a key question came up: what do banks actually need from blockchain?

📺 Learn Cardano

👁️ 2K • 👍 293 • 💬 45 • ⏱️ 10:53 • 10h ago

---

**[ALERT: Ethereum Foundation&#39;s $46.2M ETH Stake Confirmed — Is This a Huge Signal for Crypto Market?](https://www.youtube.com/watch?v=wbbPQrjr4ds)**

IMPORTANT DISCLAIMER ⚠️ This video is for educational and entertainment purposes only. NOT financial, investment, or ...

📺 The Kenzo Guy

👁️ 122 • 👍 14 • ⏱️ 25:42 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
