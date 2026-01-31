---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-01-31T23:24:03.272782+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- social
- videos
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** January 31, 2026 at 23:24 UTC  
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

### $2,406.50

---

## Ethereum Chart

**24h:** -10.9%  
**7d:** -14.4%  
**30d:** -22.8%  
**90d:** -32.9%  
**1y:** -22.6%  

---

## Ethereum Market Stats

**Market Cap:** $293.73B
Rank #2

**Circulating Supply:** 120,694,153 ETH
No max supply

**All-Time High:** $4,946.05
-50.6%

**All-Time Low:** $0.43
+564035.9%

---

## Reddit: r/ethereum

**[Daily General Discussion January 31, 2026](https://www.reddit.com/r/ethereum/comments/1qrucxq/daily_general_discussion_january_31_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

17h ago

---

**[Built a free source open honeypot scanner to protect Ethereum traders](https://www.reddit.com/r/ethereum/comments/1qsf7hh/built_a_free_source_open_honeypot_scanner_to/)**

Honeypot tokens are killing Ethereum's reputation. People get rugged, blame "Ethereum scams," when really it's malicious ERC20 implementations. Source: [github.com/Teycir/honeypotscan](https://github.com/Teycir/honeypotscan) to help clean this up. ## The Problem Scammers deploy ERC20 tokens with hidden logic that blocks sells: - tx.origin checks in transfer/balanceOf/allowance - Hidden 95-100% sell taxes - Whitelist-only transfers - Asymmetric transfer logic You can buy on Uniswap, but when you try to sell, the transaction reverts or drains your tokens. Funds gone. ## How It Works Paste a contract address → fetches verified source from Etherscan → runs 13 regex patterns → returns results in ~2 seconds. Detection patterns include: - **Core ERC20 abuse** (3 patterns) - tx.origin in balanceOf/allowance/transfer - **Hidden helpers** (2 patterns) - _taxPayer, _isSuper with tx.origin - **Auth bypasses** (4 patterns) - tx.origin in require/if/assert/mapping - **Transfer blocks** (4 patterns) - Sell restrictions, whitelists, extreme taxes Threshold: 2+ patterns = 95% confidence honeypot. Testing shows 98% sensitivity, 97% specificity. ## Why tx.origin is the red flag When you buy via Uniswap: - `tx.origin = YOUR_WALLET` ✅ - `msg.sender = YOUR_WALLET` ✅ When you sell via Uniswap: - `tx.origin = YOUR_WALLET` ✅ - `msg.sender = UNISWAP_ROUTER` ❌ Honeypots exploit this. They check `tx.origin` in access control, so DEX sells always fail while direct buys work. ## Tech Stack - Next.js 16 frontend on Cloudflare Pages - Cloudflare Workers for edge scanning - Cloudflare KV for caching (95% hit rate) - 6 Etherscan API keys with rotation - Supports Ethereum, Polygon, Arbitrum ## Try it Live: [honeypotscan.pages.dev](https://honeypotscan.pages.dev) Completely free, no rate limits, no tracking. Help protect the ecosystem 🛡️

1h ago

---

**[EtherWorld Weekly — Edition 349](https://www.reddit.com/r/ethereum/comments/1qs3kzo/etherworld_weekly_edition_349/)**

World News, Stories By EtherWorld, Technical Explainers, Client News & Updates, Podcasts, Upcoming Events & Jobs

🔗 [EtherWorld.co](https://etherworld.co/etherworld-weekly-edition-349/) • 9h ago

---

**[Listening to Polymarket trades in real-time (open source, no third party)](https://www.reddit.com/r/ethereum/comments/1qs3l8c/listening_to_polymarket_trades_in_realtime_open/)**

9h ago

---

**[I am personally allocating 16,384 ETH to support full-stack open-source security and verifiability.](https://www.reddit.com/r/ethereum/comments/1qqzw02/i_am_personally_allocating_16384_eth_to_support/)**

In these five years, the Ethereum Foundation is entering a period of mild austerity, in order to be able to simultaneously meet two goals: Deliver on an aggressive roadmap that ensures Ethereum's status as a performant and scalable world computer that does not compromise on robustness, sustainability and decentralization. Ensures the Ethereum Foundation's own ability to sustain into the long term, and protect Ethereum's core mission and goals, including both the core blockchain layer as well as users' ability to access and use the chain with self-sovereignty, security and privacy. To this end, my own share of the austerity is that I am personally taking on responsibilities that might in another time have been "special projects" of the EF. Specifically, we are seeking the existence of an open-source, secure and verifiable full stack of software and hardware that can protect both our personal lives and our public environments ( see https://vitalik.eth.limo/general/2025/09/24/openness_and_verifiability.html ). This includes applications such as finance, communication and governance, blockchains, operating systems, secure hardware, biotech (including both personal and public health), and more. If you have seen the Vensa announcement (seeking to make open silicon a commercially viable reality at least for security-critical applications), the ucritter.com including recent versions with built in ZK + FHE + differential-privacy features, the air quality work, my donations to encrypted messaging apps, my own enthusiasm and use for privacy-preserving, walkaway-test-friendly and local-first software (including operating systems), then you know the general spirit of what I am planning to support. For this reason I have just withdrawn 16,384 ETH, which will be deployed toward these goals over the next few years. I am also exploring secure decentralized staking options that will allow even more capital from staking rewards to be put toward these goals in the long term. Ethereum itself is an indispensable part of the "full-stack openness and verifiability" vision. The Ethereum Foundation will continue with a steadfast focus on developing Ethereum, with that goal in mind. "Ethereum everywhere" is nice, but the primary priority is "Ethereum for people who need it". Not corposlop, but self-sovereignty, and the baseline infrastructure that enables cooperation without domination. In a world where many people's default mindset is that we need to race to become a big strong bully, because otherwise the existing big strong bullies will eat you first, this is the needed alternative. It will involve much more than technology to succeed, but the technical layer is something which is in our control to make happen. The tools to ensure your, and your community's, autonomy and safety, as a basic right that belongs to everyone. Open not in a bullshit "open means everyone has the right to buy it from us and use our API for $200/month" way, but actually open, and secure and verifiable so that you know that your technology is working for you.

1d ago

---

**[Daily General Discussion January 30, 2026](https://www.reddit.com/r/ethereum/comments/1qqxc92/daily_general_discussion_january_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Major developments for ETH](https://www.reddit.com/r/ethereum/comments/1qrhhyb/major_developments_for_eth/)**

It was some time ago that ETH went from proof of work to proof of stake. At the time Vitalik said that there were other changes coming such as faster transaction or lower transaction cost. I have not heard any more since then? Is there any progress?

1d ago

---

**[DIY crypto inheritance on Ethereum](https://www.reddit.com/r/ethereum/comments/1qrc60c/diy_crypto_inheritance_on_ethereum/)**

Hello Folks, I just published a smart contract to handle crypto inheritance 100% on-chain, without the owner having to do anything offline. I know there are many solutions that are trying to solve this problem, but I wanted to design my own with my logic, which is the following: - the contract acts like a wallet, owner can deposit, withdraw and transfer - the owner can assign beneficiaries, and update them at any time - the wallet contains an "alive check", which is automatically updated on any transaction - if you wanna use it as a vault (dormant), you can update the "alive check" manually - the owner defines a "consider me death time" in years, eg: if the last alive check is older than 10 years, I'm dead :( - once that happen, any of the beneficiaries can access the wallet and withdraw all the funds At this point, my favorite feature: the wallet gets locked, will reject any future deposit and "answer" with an epitaph... your "last worlds" recorded on-chain that you can configure when you create the wallet. All of the above is less then 100 lines of solidity... amazing :) At the moment I only did the backend (github link), but I'd like to do a nice interface to make it easy to deploy. Of course, free and open source in the Ethereum spirit! Would you give me a feedback on the logic? Do you see any pitfall or edge cases? Thanks, Francesco

1d ago

---

**[Just one Scan that can save you from exploits [Its free to scan]](https://www.reddit.com/r/ethereum/comments/1qrvb61/just_one_scan_that_can_save_you_from_exploits_its/)**

Watch before one bug costs you everything. https://x.com/SolidityScan/status/2017172006056390715?s=20

16h ago

---

**[138 - Mac Budkowski - NO BS Crypto GTM Guide](https://www.reddit.com/r/ethereum/comments/1qrj8o9/138_mac_budkowski_no_bs_crypto_gtm_guide/)**

The Doots live stream is all about showcasing the best of the week from the Daily General Discussion from the r/ethereum Community on Reddit! Today we talked to Mac Budkowski from macbudkowski.com. He's made the "No BS Crypto GTM guide." Dig into what he has learned about timing, messaging, and why best isn't always good. Host: JT Technical Host: LogrisTheBard https://dailydoots.com by Hanniabu Daily Doots Curator: Tricky_Troll Weekly Doots Curator: The-A-Word Farcaster and Backend Host Support: Ben Broad Media Content Support: Twelve Meatballs Discord Bouncer and Watchdog: Treebeard As always, if you know someone who wants a piece of this action, send em our way. Buy us a ☕ dailydoots.eth All of our channels can be found here: https://dailydoots.com/podcast/ 🕸️https://dailydoots.com 📢https://discord.gg/EVMavericks 📰https://reddit.com/r/ethereum 🔊MINTABLE Podcast 👉: https://pods.media/evmavericks 🍎Apple https://podcasts.apple.com/us/podcast/ethfinance-evmavericks-daily-doots-livestream/id1750089604 🔊Spotify https://open.spotify.com/show/7AotdyMtcvHZLv3pVqkxre 🦁https://x.com/EVMavericks ⏱️TikTok: https://www.tiktok.com/@evmavericks 📺https://www.youtube.com/channel/UC51nlNbIkBm5Qhm7EwQuWLw Twitch: https://www.twitch.tv/evmavericks LinkedIN: https://www.linkedin.com/company/evmavericks-daily-doots-podcast

🔗 [youtu.be](https://youtu.be/lDG5GrjKgew) • 1d ago

---

---

## Google News: "ethereum"

**[Crypto Crash: Liquidations Top $2.5 Billion as Bitcoin, Ethereum and XRP Prices Plummet](https://decrypt.co/356557/crypto-crash-liquidations-2-5-billion-bitcoin-ethereum-xrp-plummet)**

The crypto market's recent decline only accelerated Saturday, with Bitcoin falling to nearly $77,000 as liquidations piled up.

Decrypt • 2h ago

---

**[Bitcoin, XRP, Ethereum Fall on News of Kevin Warsh Fed Appointment.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-crypto-today-954298d9?gaa_at=eafs&gaa_n=AWEtsqcRnSsml79rPPnQbA17JdlJDygs_7E9WXessBYhgeB8h71MVaHqsEx8&gaa_ts=697e847d&gaa_sig=O9w3gLbwidbbyh1ggg_2EBs50-8FDnUOUI-75Zq_bxPLlmil76TCzCjZ5vPCI-Hn8iH_pMlzFnMp2L7A9tYbHQ%3D%3D)**

Barron's • 1d ago

---

**[AI Models Predict Ethereum, Solana, and XRP 2026 Prices—Which Altcoin Has the Biggest Upside?](https://finance.yahoo.com/news/ai-models-predict-ethereum-solana-193044962.html)**

Four major AI models have projected 2026 price targets for Ethereum (CRYPTO: ETH), Solana (CRYPTO: SOL), and XRP (CRYPTO: XRP). The forecasts range from conservative consolidation to triple-digit percentage gains, with each asset showing different upside potential based on adoption trends, network activity, and market positioning. Ethereum anchors institutional DeFi with mature Layer 2 networks, ... AI Models Predict Ethereum, Solana, and XRP 2026 Prices—Which Altcoin Has the Biggest Upside?

Yahoo Finance • 1d ago

---

**[Ethereum Supply Tightens With 45% of ETH Locked: Sygnum](https://thedefiant.io/news/research-and-opinion/ethereum-supply-tightens-with-45-of-eth-locked-sygnum)**

ETF buying, staking and corporate holdings continue to reduce liquid ETH.

thedefiant.io • 1d ago

---

**[Ethereum Falls 10% In Selloff](https://www.investing.com/news/cryptocurrency-news/ethereum-falls-10-in-selloff-4477658)**

Ethereum Falls 10% In Selloff

Investing.com • 6h ago

---

**[BitMine Immersion Can’t Stop Buying Ethereum as Crypto Prices Tank](https://www.barchart.com/story/news/37329357/bitmine-immersion-cant-stop-buying-ethereum-as-crypto-prices-tank)**

BitMine Immersion continues to accumulate Ethereum amid price declines, following a treasury strategy inspired by Strategy.

Barchart.com • 1d ago

---

**[Vitalik Buterin Withdraws $44.7M in ETH to Support Ethereum Growth Through ‘Mild Austerity’](https://decrypt.co/356490/vitalik-buterin-withdraws-44-7m-in-eth-to-support-ethereum-growth-through-mild-austerity)**

The Ethereum co-founder wants to pursue an “aggressive” roadmap that will strengthen its status as a decentralized world computer.

Decrypt • 1d ago

---

**[Vitalik Buterin to spend $43 million on Ethereum development](https://www.coindesk.com/business/2026/01/30/vitalik-buterin-withdraws-usd17-million-in-eth-as-ethereum-foundation-enters-mild-austerity)**

Ethereum’s co-founder said the $43 million withdrawal will support a broader “full-stack openness and verifiability” vision as the foundation tightens spending.

CoinDesk • 1d ago

---

**[Vitalik Buterin Withdraws 16,384 ETH as Ethereum Foundation Enters ‘Austerity Phase’ — What For?](https://www.tradingview.com/news/cryptonews:c7dddcebf094b:0-vitalik-buterin-withdraws-16-384-eth-as-ethereum-foundation-enters-austerity-phase-what-for/)**

Ethereum co-founder Vitalik Buterin has withdrawn 16,384 ETH, worth roughly $44.5 million at current prices, as the Ethereum Foundation enters what he described as a period of “mild austerity.”In a post on X, Buterin said the Ethereum Foundation is adjusting its spending approach to meet two parall…

TradingView • 1d ago

---

**[Brock Pierce-backed Ethereum treasury firm Bit Digital to fully wind down bitcoin mining operations](https://www.theblock.co/post/387748/brock-pierce-ethereum-treasury-bit-digital-wind-down-bitcoin-mining)**

Bit Digital entered the bitcoin mining business in 2020 and was an early diversifier into the HPC/AI sector.

The Block • 2d ago

---

---

## YouTube Videos: "ethereum"

**[BITCOIN CRASH: PRICE TARGETS HIT (this is next)!!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=8mqEKXWHZOE)**

BITCOIN CRASH: PRICE TARGETS HIT (this is next)!!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 4K • 👍 284 • 💬 195 • ⏱️ 27:07 • 2h ago

---

**[&quot;Why I&#39;m Loading Up MASSIVELY In Ethereum Before MARCH&quot; - Tom Lee (4 WEEKS LEFT!)](https://www.youtube.com/watch?v=UjCE1TUJ4lI)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 2K • 👍 58 • 💬 117 • ⏱️ 18:25 • 8h ago

---

**[Why Bitcoin, ETH &amp; Altcoins Are CRASHING HARD](https://www.youtube.com/watch?v=-rrpLsrAr9Q)**

Nick Valdez looks at the latest market crash with the next level Bitcoin MUST hold for support! Join Our Trading Group Discord ...

📺 Discover Crypto

👁️ 3K • 👍 292 • 💬 158 • ⏱️ 4:28 • 1h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=XFntGyzd46U)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 217 • 💬 21 • ⏱️ 4:54 • 3h ago

---

**[BITCOIN AND ETH: GOING LOWER RIGHT NOW!!!! SILVER COLLAPSES 40% 🚨🚨🚨🚨🚨🚨](https://www.youtube.com/watch?v=F3Cgt1tHjfI)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 20K • 👍 1K • 💬 117 • ⏱️ 44:59 • 5h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=soWYVsa4xZc)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 145 • 💬 8 • ⏱️ 4:18 • 9h ago

---

**[Cathie Wood: “This Is WHEN The 2026 Bull Run Starts” [New Bitcoin &amp; Ethereum Prediction 2026]](https://www.youtube.com/watch?v=xsRdyWYOUJA)**

Join UpTrade today - Your personal crypto broker: https://www.uptrade.au/ My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 9K • 👍 323 • 💬 106 • ⏱️ 16:36 • 8h ago

---

**[Ethereum vs Bitcoin: The Trade Everyone Is Missing in 2026 w/ Kyle Reidhead &amp; John Gillen](https://www.youtube.com/watch?v=wIsd5_VNgbs)**

Go PRO and become a better investor: ...

📺 Milk Road

👁️ 2K • 👍 76 • 💬 54 • ⏱️ 12:13 • 11h ago

---

**[CRYPTO WARNING ⛔️ KNOW THIS TODAY! ‼️ XRP ETHEREUM BITCOIN](https://www.youtube.com/watch?v=5XfakzNwbjo)**

1️⃣ *Join Moe's Discord Code 2026 save 50%* ➡https://www.patreon.com/stockmoe/membership 2️⃣ *Save Big on the ...

📺 Crypto Moe

👁️ 228 • 👍 44 • 💬 15 • ⏱️ 11:41 • 25m ago

---

**[When Will Stop The Crash? 💀 ETH Crypto Token Analysis](https://www.youtube.com/watch?v=LUAphGQ2Yls)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 5K • 👍 138 • 💬 49 • ⏱️ 7:13 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
