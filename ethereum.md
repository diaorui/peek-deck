---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-06-10T04:57:54.913980+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- social
- videos
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** June 10, 2026 at 04:57 UTC  
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

### $1,659.49

---

## Ethereum Chart

**24h:** -3.8%  
**7d:** -8.3%  
**30d:** -28.6%  
**90d:** -22.4%  
**1y:** -41.3%  

---

## Ethereum Market Stats

**Market Cap:** $196.08B
Rank #2

**Circulating Supply:** 120,684,382 ETH
No max supply

**All-Time High:** $4,946.05
-67.2%

**All-Time Low:** $0.43
+375121.4%

---

## Reddit: r/ethereum

**[Diving into Ethereum staking after Shanghai – my setup headaches and questions for the community](https://www.reddit.com/r/ethereum/comments/1u1cq9h/diving_into_ethereum_staking_after_shanghai_my/)**

Hey everyone, I've been running a solo validator for about 8 months now and wanted to share some concrete details from my experience post-Shanghai upgrade since it feels like the subreddit has been light on real-user staking stories lately. I started with 32 ETH on mainnet using Lighthouse + Geth on a used Dell OptiPlex with 32GB RAM and a 1TB NVMe drive, mostly because I wanted to avoid the big pools and actually control my keys. Before the upgrade withdrawals were basically impossible without full exit, but now I've been able to pull out 0.4 ETH in partial rewards last month to cover electricity and still keep the validator happy. What surprised me most was the MEV-Boost integration – I had to switch from the default relay to Flashbots after seeing my effective APR drop to 3.1% for two weeks straight; the concrete difference was an extra 0.12 ETH over 30 days once I configured the builder API correctly with mev-boost 1.6.0. Hardware-wise the Pi 4 I tried first kept crashing on sync after the Dencun changes so I migrated everything to the desktop and added a 2TB external SSD for the archive node because geth was eating 800GB+ alone. Gas fees for the withdrawal credential change were only 0.0008 ETH which felt almost too cheap compared to 2021 levels, but I still double-checked the contract address against Etherscan three times before signing. One thing I'm still puzzled about is why my attestation success rate dipped to 96% for a few days even though uptime was 99.8% – turned out to be a beacon chain checkpoint issue after a recent client update. Anyone running similar hardware seeing the same? Also curious how people are handling the new 0x01 withdrawal credentials in terms of tax tracking since the partial withdrawals create way more on-chain events than before. Would love to hear specific client configs or relay recommendations that have worked for others without getting rate-limited. Thanks in advance, this community has been super helpful with my earlier posts about testnet debugging.

10h ago

---

**[Daily General Discussion June 09, 2026](https://www.reddit.com/r/ethereum/comments/1u0vguk/daily_general_discussion_june_09_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

23h ago

---

**[Would anybody be willing to explain in simple terms how this works - getting paid by a website via an Ethereum wallet?](https://www.reddit.com/r/ethereum/comments/1u0hxza/would_anybody_be_willing_to_explain_in_simple/)**

I signed up with a well-known legitimate site to get paid posting clips of their content to tiktok, youtube, etc. but found out the only way they pay is to an ethereum wallet, which I have never heard of before. I am not familiar with how to use cryptocurrency at all. I've spent the whole morning trying to find info to understand how it works, called my bank and spoke with someone who told me I can't convert it into real money to deposit it with them, etc. and it's still all just Greek to me. I'm wondering if it's worth bothering with.

1d ago

---

**[Daily General Discussion June 08, 2026](https://www.reddit.com/r/ethereum/comments/1tzyakv/daily_general_discussion_june_08_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[How to extract yield from defi via the "flywheel effect"](https://www.reddit.com/r/ethereum/comments/1u0i9bg/how_to_extract_yield_from_defi_via_the_flywheel/)**

Create a reward token that doubles in supply yearly. Promise a 51% yield to provide trading liquidity for the token, which is expected to lose 50% of its value in a year. Secretly send the other 49% to a stablecoin farming pool or something. Profit.

1d ago

---

**[Lighter Due Diligence: the highest growth L2?](https://www.reddit.com/r/ethereum/comments/1tzpmiu/lighter_due_diligence_the_highest_growth_l2/)**

Due diligence: Beta on HYPE: Hyperliquid is amazing right now, and I expect them to do well. Perpification of all assets is going way faster that most realized, while tokenization of rwa’s have taken much longer due to the complexity of regulations, cross chain considerations, liquidity concerns, split order books etc. Perps have become the top choice for people to gamble on commodities like gold, silver, oil, and of course stocks and even pre IPO stocks. Volatility is a tailwind for perp dex revenue, and I expect further volatility this summer and rest of the year. Notice I didn’t even mention crypto perps. Even when crypto has low liquidity and mindshare, perp dex’s will still do well as people trade all assets. Lighter is currently much smaller than HYPE. About 2% of both MC and FDV. $LIT alpha: US based: Vlad, the founder of Lighter, has strong connections to both Silicon Valley, DC heavyweights, and NYC tradfi institutions. He has strong connections to Robinhood, and was an early advisor and HS friend to the other Vlad, ceo of RH. RH was an early investor to Lighter, and I expect some collaboration with them in the future, as Vlad mentioned in a few interviews. I expected some integration of the options market form RH may be able to flow through Lighter on chain, or lighter can help RH with the perps in Us market. Vlad is also friends with Mike Selig of the CFTC, and also with David Sacks. Sacks was an early investor in Lighter before divesting and working for the Trump admin. I expect lighter to receive CFTC approval for us perps market and perhaps tokenization way before hyperliquid Ken Griffin, ceo of citadel, personally hired Vlad when he was 19. Citadel looks to be the perfect partner to provide liquidity to lighter. Citadel would make money on spreads. They also would need to buy $LIT token to be included in the liquidity pool as that’s how the tokenomics are set up 3) token buybacks. Lighter is using 100% of the revenue to buy back the $LIT token, and their buybacks is about 150% higher than $HYPE as % of market cap 4) Vlad also has strong relationships with EF and Vitalik, BMNR and tom Lee. Excited to see where these partnerships go. And I wouldn’t be surprised if these orgs invest in lighter as ethereum community is in their lowest sentiment. They need a killer app.

2d ago

---

**[Daily General Discussion June 07, 2026](https://www.reddit.com/r/ethereum/comments/1tz2vsm/daily_general_discussion_june_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Daily General Discussion June 06, 2026](https://www.reddit.com/r/ethereum/comments/1ty7xyl/daily_general_discussion_june_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

3d ago

---

**[Sent 0.04485299 ETH but nothing arrived.](https://www.reddit.com/r/ethereum/comments/1tydlyy/sent_004485299_eth_but_nothing_arrived/)**

3d ago

---

**[ETH powers most of DeFi but the spending layer is still broken for most people](https://www.reddit.com/r/ethereum/comments/1txklof/eth_powers_most_of_defi_but_the_spending_layer_is/)**

Billions in USDC and USDT sitting on Ethereum, some of the most sophisticated financial infrastructure ever built, and i still have to convert everything to fiat just to buy groceries. The DeFi side is incredible. Lending, borrowing, yield all of it works seamlessly but the moment you want to actually spend your stablecoins in real life you're back to exchanges, fees and waiting for bank transfers. Everything works perfectly until you want to spend it somewhere normal

4d ago

---

---

## Google News: "ethereum"

**[Circle debuts cirBTC on Ethereum to challenge Coinbase in the wrapped bitcoin market](https://www.coindesk.com/business/2026/06/09/circle-debuts-cirbtc-on-ethereum-to-challenge-coinbase-in-the-wrapped-bitcoin-market)**

Circle unveiled "cirBTC", a token backed 1:1 with the world's largest cryptocurrency to allow users to utilise their bitcoin wealth in DeFi protocols.

CoinDesk • 18h ago

---

**[cirBTC Is Live on Ethereum for Wrapped BTC Deployment](https://www.circle.com/blog/cirbtc-is-now-live-on-ethereum)**

Now live on Ethereum, cirBTC is a 1:1 BTC-backed token that delivers secure, neutral collateral across DeFi on Ethereum, with planned Arc and multichain support.

Circle Internet Financial • 1d ago

---

**[Bitcoin and ethereum prices today, Tuesday, June 9, 2026: Values stabilize as investors may seek alternatives](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-tuesday-june-9-2026-values-stabilize-as-investors-may-seek-alternatives-114631191.html)**

These are today's bitcoin and ethereum prices, Tuesday, June 9, 2026. Bitcoin opened at $63,078.89, down 0.3% from yesterday’s opening price. Ethereum opened at $1,689.88, up 0.2% from yesterday's open.

Yahoo Finance • 17h ago

---

**[BitMine buys the dip, makes largest ethereum purchase this year](https://sherwood.news/crypto/bitmine-buys-the-dip-makes-largest-ethereum-purchase-this-year/)**

The largest ethereum treasury firm acquired 126,971 tokens last week....

Sherwood News • 1d ago

---

**[Seattle-Area Man Gets Prison for Laundering Foreign Fraud Funds With Bitcoin, Ethereum](https://decrypt.co/370576/seattle-man-prison-laundering-foreign-fraud-funds-bitcoin-ethereum)**

The fraudster took in nearly $100 million from victims before laundering funds via Bitcoin, Ethereum, and stablecoins.

Decrypt • 8h ago

---

**[MetaMask debuts Agent Wallet giving AI bots self-custody access to Ethereum](https://www.theblock.co/post/403865/metamask-debuts-agent-wallet-giving-ai-bots-self-custody-access-ethereum)**

Consensys-backed MetaMask is rolling out a non-custodial wallet for AI agents for general availability this summer.

The Block • 1d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.54 Million Tokens, and Total Crypto and Total Cash Holdings of $9.6 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-54-million-tokens-and-total-crypto-and-total-cash-holdings-of-9-6-billion-302793756.html)**

Bitmine owns 4.59% of the total ETH coin supply of 120.7 million Bitmine is 92% of the way to the 'Alchemy of 5%' in just 11 months Ethereum continues to...

PR Newswire • 1d ago

---

**[Crypto News: Bitcoin, Ethereum, XRP and Cardano Enter Historical Buy Zones as MVRV Turns Negative](https://www.binance.com/en/square/post/332239443761601)**

Binance • 17h ago

---

**[Crypto News Today: MemeToro AI Agents Gain Momentum as Ethereum Price Faces Pressure](https://markets.businessinsider.com/news/stocks/crypto-news-today-memetoro-ai-agents-gain-momentum-as-ethereum-price-faces-pressure-1036235368)**

ZURICH, June  09, 2026  (GLOBE NEWSWIRE) -- MemeToro AI Labs, an innovative developer of decentralized artificial intelligence infrastructure, tod...

markets.businessinsider.com • 15h ago

---

**[Ethereum Flashes 'Historic Opportunity,' Says Analyst, as Tom Lee's Bitmine Buys $218M](https://finance.yahoo.com/markets/crypto/articles/ethereum-flashes-historic-opportunity-says-084217435.html)**

Ethereum hits its most oversold level ever. Tom Lee's Bitmine is buying the dip aggressively. Bullish forecasts remain despite the crash. Ethereum may be approaching ...

Yahoo Finance • 20h ago

---

---

## YouTube Videos: "ethereum"

**[ETHEREUM - THIS HASN&#39;T HAPPENED IN OVER Y 7EARS (LAST TIME WE PUMPED 5,000%)](https://www.youtube.com/watch?v=4kj-j6zxK54)**

Welcome Back To The Channel! ✔️ https://fortisx.fi/kol/tylerhillyt ✔️ Deposit from $100: Get a 1% bonus Join The Trading ...

📺 Tyler Hill Crypto

👁️ 5K • 👍 247 • 💬 62 • ⏱️ 15:00 • 13h ago

---

**[MASSIVE XRP JAPAN BANK NEWS $10,000 ETHEREUM (MANIFESTING) #xrp #ethereum #ai](https://www.youtube.com/watch?v=7nea-f-tin0)**

📺 CryptoWendyO

👁️ 3K • 👍 290 • 💬 2 • ⏱️ 2:28 • 3h ago

---

**[Ethereum’s Future Just Took a Sharp Turn](https://www.youtube.com/watch?v=HAAhbq_lefc)**

Ethereum's founder just made his most dramatic announcement yet: foundation downsizing, less ETH selling, and a personal step ...

📺 Coin Bureau

👁️ 24K • 👍 806 • 💬 79 • ⏱️ 16:49 • 2d ago

---

**[DeFi Dad: Ethereum Will Be The Backbone of Finance (Tokenization &amp; Stablecoins)](https://www.youtube.com/watch?v=_Bpzr0AQ3gc)**

DeFi Dad breaks down why lighter's ETH escape hatch makes it the most underrated security feature versus HyperLiquid, why ...

📺 The Rollup

👁️ 4K • 👍 123 • 💬 22 • ⏱️ 38:13 • 1d ago

---

**[Is Ethereum Falling Behind? The 2026 Upgrades That Could Change EVERYTHING: Glamsterdam, Hegotá](https://www.youtube.com/watch?v=bv7Er1OMY8c)**

What's next for Ethereum in 2026? Glamsterdam, Hegotá, and a quantum‑ready future, that's what!* In this episode, we strip it ...

📺 Binance

👁️ 8K • 👍 289 • 💬 21 • ⏱️ 5:46 • 1d ago

---

**[Ethereum Bottom REVEALED: This ETH Historical Pattern Triggers Massive Bull Runs](https://www.youtube.com/watch?v=WJVONw_V21I)**

When will #ethereum finally bottom? In this video, I break down a historical patterns that has appeared near major Ethereum bear ...

📺 Humble Market Timer

👁️ 179 • 👍 3 • ⏱️ 9:34 • 16h ago

---

**[😱 3 FORMAS DE ACUMULAR ETH EN LA BAJADA](https://www.youtube.com/watch?v=R91fJQnpTI8)**

Gracias por ver! Únase a la conversación en nuestro Telegram: https://telegram.me/valueindexchat Links de interés: Socios ...

📺 Value Index | Bitcoin y altcoins

👁️ 3K • 👍 340 • 💬 62 • ⏱️ 16:03 • 14h ago

---

**[Bitcoin &amp; Ethereum, bereit für den LONG? Habt Geduld, bald ist es soweit!](https://www.youtube.com/watch?v=YbcYeaHTpi8)**

DIE BESTE EXCHANGE AUF DEM KRYPTOMARKT!! OKX!! Das wird mein neuer Partner OKX! Nur bei mir bekommt ihr 300€ ...

📺 Krypto Trading & Investing

👁️ 523 • 👍 125 • 💬 11 • ⏱️ 12:47 • 55m ago

---

**[Why Can&#39;t Anyone Kill Ethereum](https://www.youtube.com/watch?v=iEuxV-LicfA)**

FOLLOW ANDY, ROBBIE & THE ROLLUP ⏬ Twitter (X): https://x.com/therollupco Andy Twitter (X): https://x.com/andyyy Robbie ...

📺 The Rollup

👁️ 330 • 👍 17 • 💬 25 • ⏱️ 2:36 • 12h ago

---

**[ETH Final Flush (Rotation Next?) + BTC Bottom Signal](https://www.youtube.com/watch?v=ZAPYekLDvyQ)**

CoinGPT AI - Find High-Probability Setups, Draft & Execute! https://marzell.org/CoinGPT BloFin - No KYC/No VPN needed ...

📺 Marzell Crypto

👁️ 337 • 👍 26 • 💬 61 • ⏱️ 6:16 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
