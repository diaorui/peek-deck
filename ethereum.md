---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-31T08:09:11.641822+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- cryptocurrency
- social
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 31, 2026 at 08:09 UTC  
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

### $2,065.16

---

## Ethereum Chart

**24h:** +0.1%  
**7d:** -5.2%  
**30d:** +1.5%  
**90d:** -31.5%  
**1y:** +8.0%  

---

## Ethereum Market Stats

**Market Cap:** $248.01B
Rank #2

**Circulating Supply:** 120,691,415 ETH
No max supply

**All-Time High:** $4,946.05
-58.4%

**All-Time Low:** $0.43
+474602.0%

---

## Reddit: r/ethereum

**[Daily General Discussion March 31, 2026](https://www.reddit.com/r/ethereum/comments/1s8e3ii/daily_general_discussion_march_31_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3h ago

---

**[What is ZCHF?](https://www.reddit.com/r/ethereum/comments/1s8g4y2/what_is_zchf/)**

ZCHF is a decentralized stablecoin that is designed to track the value of the Swiss franc (CHF). Unlike popular stablecoins like USDT or USDC that are pegged to the US dollar, ZCHF is pegged 1:1 to Switzerland’s currency. It is issued by the Frankencoin protocol and operates on blockchain infrastructure, which means it doesn’t rely on traditional banks in the same way centralised stablecoins do. Instead, it uses a system of collateral and smart contracts to maintain its value. Why People Are Talking About It Interest in ZCHF has increased after Vitalik Buterin recently swapped a significant amount of USDC into ZCHF. Moves like this bring attention to the idea that DeFi may not stay centered only around the US dollar.

1h ago

---

**[Google warns quantum computers could break current crypto security sooner than expected](https://www.reddit.com/r/ethereum/comments/1s8h1j2/google_warns_quantum_computers_could_break/)**

Google’s new research is basically saying the quantum threat may be less distant than people assumed. Not an “Ethereum is doomed” story, but definitely a reminder that post-quantum migration may become a much more serious issue across crypto sooner than expected Do you think Ethereum is actually positioned well for a transition like that, or is the ecosystem still underestimating how hard this would be?

16m ago

---

**[Beginner's Game Tournament for r/ethereum only](https://www.reddit.com/r/ethereum/comments/1s8gw8d/beginners_game_tournament_for_rethereum_only/)**

I've been all over daily threads for the last two weeks, and some of those really nice folks have been having fun with this little game dapp that I built. I call it Stupid Games, because you play really easy, simple games, but get to win awesome real ETH prizes! It's an arcade type game platform, full of crypto memes, that pays out real ETH prizes to the winners. All managed by smart contracts of course. I'm creating a beginner friendly, mini tournament just for this sub. No players from the current Leaderboard allowed! And when I say beginner, I mean JT level beginner like from the Daily Doots Podcast #143! Lol! No offence JT 😆 Its free, no gas, no cash, just real fun! The prize is $20 or more, but more than that, its bragging rights to be the king of this hill. It's even got a Burner Wallet login, so you know it's not sus. More dapps should do that right? If you want to give it a shot, there's only space for 9-10 players, so drop your [burner] address and I'll let you in. The FLY game is similar to Flappy Bird, and the SHOOT game is similar to Asteroids. Try them and pick your vibe. So what's in it for me? I worked hard on the app and really want to see it being used. I also think it's genuinely fun when you get it. Plus, I took a job break and built it as a porfolio piece so I would love to get feedback. Many features were actually suggestions from users on the daily threads, which I appreciate so much (Alexis and Tricky)! Any and all feedback/criticism welcome. Questions too! Chips are ERC20 tokens but 1:1 exchangeable for 0.0001 eth from the contract. No promotion of any product in this post. No monetary gain for me, only loss 🙁! Play Stupid Games, Win Awesome Prizes! https://reddit.com/link/1s8gw8d/video/us22jk9r2csg1/player https://reddit.com/link/1s8gw8d/video/9zhhtl9r2csg1/player

25m ago

---

**[The hidden gas and security trade-offs of using CREATE2 + Minimal Proxies for multi-chain deployments](https://www.reddit.com/r/ethereum/comments/1s83w01/the_hidden_gas_and_security_tradeoffs_of_using/)**

Hey everyone, Over the last four years of writing smart contracts and teaching these concepts in EVM bootcamps, I keep seeing teams stumble into the exact same architectural traps when trying to achieve cross-chain address parity. Leveraging CREATE2 for deterministic addresses fundamentally changes how we handle multi-chain deployments. But because init_code includes constructor arguments, maintaining that exact same address across chains is impossible if you need to pass in chain-specific variables (like local router addresses or bridge endpoints). The standard industry workaround is deploying EIP-1167 Minimal Proxies via a universal factory, deploying deterministically, then initializing the state in the same transaction. However, this introduces some severe trade-offs that often get overlooked until they hit production: The DELEGATECALL Gas Tax: Minimal proxies are incredibly cheap to deploy (~45 bytes of bytecode), but they add a DELEGATECALL overhead to every single execution (2600 gas cold, 100 warm). At scale, this execution cost compounds brutally for your users. MEV Front-running Risks: If your proxy deployment and initialize() call are not strictly atomic within the factory contract execution, MEV bots might front-run the initialization transaction. This either bricks the instance entirely or hijacks the contract ownership. Immutability vs Upgradeability: To retain the exact same address while upgrading logic, you have to wrap the implementation in UUPS or Transparent Proxies. This inflates the initial deployment cost and introduces strict storage collision risks (requiring flawless adherence to EIP-1967 storage slots). I just published a full breakdown of these mechanics on my blog, diving into the math behind the gas trade-offs and how patterns like CREATE3 are solving the issue for non-proxy contracts where constructor arguments must differ. If you are currently architecting a multi-chain protocol, you can read the full technical deep dive here:https://andreyobruchkov1996.substack.com/p/understanding-contract-deployments-proxies-and-create2-part-2-df8f05998d5e Would love to hear how you all are handling cross-chain deterministic deployments right now. Are you still relying heavily on customized off-chain salt-mining scripts, or have you migrated to CREATE3 wrappers?

10h ago

---

**[Daily General Discussion March 30, 2026](https://www.reddit.com/r/ethereum/comments/1s7hcs2/daily_general_discussion_march_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[ERC20 token network mistakes - anyone sent to the wrong chain before?](https://www.reddit.com/r/ethereum/comments/1s8bk4i/erc20_token_network_mistakes_anyone_sent_to_the/)**

Curious how many people here have made this mistake at least once. Sending an ERC20 token but picking the wrong network, or mixing up chains like sending to a non-compatible address. It’s one of those errors that feels small in the moment but can turn into a real headache depending on where the funds land. Sometimes recoverable, sometimes not. What’s your experience with this? Did you manage to recover the funds or was it a total loss? And what habits or checks do you use now to avoid it happening again?

5h ago

---

**[EtherWorld Weekly — Edition 357](https://www.reddit.com/r/ethereum/comments/1s7mopy/etherworld_weekly_edition_357/)**

World News, Stories By EtherWorld, Technical Explainers, Client News & Updates, Podcasts, Upcoming Events & Jobs

🔗 [EtherWorld.co](https://etherworld.co/etherworld-weekly-edition-357/) • 21h ago

---

**[Daily General Discussion March 29, 2026](https://www.reddit.com/r/ethereum/comments/1s6m76c/daily_general_discussion_march_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion March 28, 2026](https://www.reddit.com/r/ethereum/comments/1s5rbnm/daily_general_discussion_march_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

---

---

## Google News: "ethereum"

**[What’s on the Ethereum Roadmap: Glamsterdam, Hegota and Beyond](https://decrypt.co/resources/whats-on-ethereum-roadmap-glamsterdam-hegota-beyond)**

Ethereum has rolled out a steady stream of upgrades since 2022. Here’s how those changes fit together—and what’s still ahead.

Decrypt • 1d ago

---

**[Ethereum vs. Solana: Which Crypto Has More Upside?](https://www.fool.com/investing/2026/03/28/ethereum-vs-solana-which-crypto-has-more-upside/)**

Ethereum's vast ecosystem goes up against Solana's lightning-quick network.

The Motley Fool • 2d ago

---

**[BMNR, ETH news: Bitmine buys 71,000 ETH as digital asset treasuries dial back purchases](https://www.coindesk.com/business/2026/03/30/bitmine-makes-biggest-ether-purchase-in-2026-while-other-digital-asset-treasuries-pull-back)**

Tom Lee's Ethereum treasury bought more than 71,000 ETH over the past week, remaining the sole large corporate crypto buyer as Strategy broke its 13-week bitcoin purchase streak.

CoinDesk • 17h ago

---

**[Tom Lee's BitMine Adds More Ethereum as Strategy Takes a Break From Bitcoin Buying](https://finance.yahoo.com/markets/crypto/articles/tom-lees-bitmine-adds-more-144553148.html)**

BitMine continued its Ethereum accumulation, adding to its leading ETH treasury while Strategy took a week off from Bitcoin purchases.

Yahoo Finance • 17h ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.732 Million Tokens, and Total Crypto and Total Cash Holdings of $10.7 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-732-million-tokens-and-total-crypto-and-total-cash-holdings-of-10-7-billion-302728176.html)**

Bitmine has 3,142,643 staked ETH, representing $6.3 billion at $2,005 per ETH MAVAN (Made in America VAlidator Network) launched staking solution on March 25,...

PR Newswire • 19h ago

---

**[Gnosis and Zisk announce 'Ethereum Economic Zone' rollup framework with Ethereum Foundation co-funding](https://www.theblock.co/post/395578/gnosis-and-zisk-announce-ethereum-economic-zone-rollup-framework-with-ethereum-foundation-co-funding)**

The Ethereum Foundation is co-funding the "easy" initiative, which was announced at EthCC in Cannes, and partners include Aave, Titan, Centrifuge, and more.

The Block • 1d ago

---

**[Ethereum’s Incredible Position](https://finance.yahoo.com/markets/crypto/articles/ethereum-incredible-position-180149031.html)**

This market isn't what we wanted. But looking forward, ETH is still in a great place.

Yahoo Finance • 2d ago

---

**[Brace For Impact: Ethereum Price Is Now Forming A Counter-Trend Correction](https://www.tradingview.com/news/newsbtc:dc3a0c114094b:0-brace-for-impact-ethereum-price-is-now-forming-a-counter-trend-correction/)**

Ethereum is trading just above the important $2,000 psychological level, but the apparent stabilization may be deceptive. According to a technical analysis published on TradingView by crypto analyst RLinda, what looks like a recovery attempt is, in fact, a counter-trend correction, a bear market bo…

TradingView • 9h ago

---

**[Current price of Ethereum for March 30, 2026](https://fortune.com/article/price-of-ethereum-03-30-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 19h ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Move Sideways Amid Possible US Invasion Of Iran: Analyst Says 'Billion-Dollar' Trades Flooding Back To BTC And ETH](https://www.benzinga.com/crypto/cryptocurrency/26/03/51530287/bitcoin-ethereum-xrp-dogecoin-flat-amid-iran-tensions)**

Leading cryptocurrencies remained flat, while stock futures fell Sunday evening as investors speculated about a ground invasion of Iran by the U.S.

Benzinga • 1d ago

---

---

## YouTube Videos: "ethereum"

**[🚨 BTC &amp; ETH: SELL ALL ASAP &amp; RUN!!!!!! (New disturbing data!)](https://www.youtube.com/watch?v=6bWLOUY6xAM)**

New data shows the future of markets and crypto in general. Its important for bitcoin, ethereum and so on. BEWARE!

📺 Thomas Kralow

👁️ 19K • 👍 2K • 💬 78 • ⏱️ 11:48 • 20h ago

---

**[&quot;I&#39;m Buying The Dip RIGHT NOW&quot; - Tom Lee | Bitcoin &amp; ETH Price Prediction](https://www.youtube.com/watch?v=-kMU5CXpx_Q)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 340 • 👍 24 • 💬 222 • ⏱️ 16:21 • 3h ago

---

**[FINAL WARNING to ALL Crypto Holders!! (I will delete this in 24 hours)](https://www.youtube.com/watch?v=hzfc05Bphkk)**

If you hold Bitcoin or Ethereum... watch this! (alert!) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily BTC ...

📺 Altcoin Daily

👁️ 48K • 👍 3K • 💬 286 • ⏱️ 9:24 • 1d ago

---

**[ALERT: Ethereum Foundation&#39;s $46.2M ETH Stake Confirmed — Is This a Huge Signal for Crypto Market?](https://www.youtube.com/watch?v=wbbPQrjr4ds)**

IMPORTANT DISCLAIMER ⚠️ This video is for educational and entertainment purposes only. NOT financial, investment, or ...

📺 The Kenzo Guy

👁️ 559 • 👍 21 • 💬 1 • ⏱️ 25:42 • 13h ago

---

**[Bitcoin &amp; Ethereum. Wie es jetzt weitergehen sollte bei BTC! Wir haben noch NICHTS geschafft!](https://www.youtube.com/watch?v=GEVEO8aaeu0)**

Hier Handle ich Kryptowährungen!! Bitunix (Instant VIP LVL 3 und 20% Deposit Zurück bis max 400 USDT) ...

📺 Krypto Trading & Investing

👁️ 2K • 👍 506 • 💬 78 • ⏱️ 11:46 • 4h ago

---

**[Former BlackRock Exec Reveals Ethereum&#39;s Future Outlook! | Joseph Chalom](https://www.youtube.com/watch?v=iOmQYMafYG0)**

Joseph Chalom, CEO of SharpLink, joined me to discuss the company's Ethereum treasury strategy and the future of ETH. Topics: ...

📺 Thinking Crypto

👁️ 2K • 👍 144 • 💬 116 • ⏱️ 55:54 • 20h ago

---

**[BITCOIN DUMP &amp; PUMP EXPLAINED: This is Next!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=aAglFZYcX68)**

BITCOIN DUMP & PUMP EXPLAINED: This is Next!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 4K • 👍 186 • 💬 124 • ⏱️ 20:19 • 8h ago

---

**[ETHEREUM, THE FED, AND BITCOIN —(THIS CHANGES EVERYTHING)](https://www.youtube.com/watch?v=69b-uYwAlpY)**

Crypto looks calm… but underneath, everything is moving. The Ethereum Foundation just deployed $46M into staking, shifting ...

📺 CLOCKWISE CRYPTO 

👁️ 630 • 👍 69 • 💬 32 • ⏱️ 9:26 • 6h ago

---

**[Ethereum to $40,000 by 2030: Why ETH Could MASSIVELY Outperform Bitcoin](https://www.youtube.com/watch?v=4ZjG0_XW0DU)**

Check prices, drink coffee, read Milk Road. It's the easiest 5-minute habit to stay smart on crypto: ...

📺 Milk Road

👁️ 7K • 👍 205 • 💬 61 • ⏱️ 11:06 • 2d ago

---

**[Why Banks Don&#39;t Want Ethereum or Solana — And What They Actually Need](https://www.youtube.com/watch?v=WPtXmFrLrto)**

At the Digital Asset Summit 2026 in New York, a key question came up: what do banks actually need from blockchain?

📺 Learn Cardano

👁️ 3K • 👍 377 • 💬 80 • ⏱️ 10:53 • 21h ago

---

---

*Generated by PeekDeck - A glance is all you need*
