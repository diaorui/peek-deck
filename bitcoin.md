---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-01-21T16:51:54.326101+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- news
- social
- cryptocurrency
- videos
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** January 21, 2026 at 16:51 UTC  
**HTML Version:** [bitcoin.html](https://peekdeck.ruidiao.dev/bitcoin.html)

---

## Table of Contents

1. [Bitcoin Price](#bitcoin-price)
2. [Bitcoin Chart](#bitcoin-chart)
3. [Bitcoin Market Stats](#bitcoin-market-stats)
4. [Fear & Greed Index](#fear--greed-index)
5. [Reddit: r/Bitcoin](#reddit-rbitcoin)
6. [Google News: "bitcoin"](#google-news-bitcoin)
7. [HackerNews: "bitcoin"](#hackernews-bitcoin)
8. [YouTube Videos: "bitcoin"](#youtube-videos-bitcoin)

---

## Bitcoin Price

### $88,619.65

---

## Bitcoin Chart

**24h:** -1.5%  
**7d:** -7.5%  
**30d:** +1.3%  
**90d:** -20.4%  
**1y:** -14.9%  

---

## Bitcoin Market Stats

**Market Cap:** $1762.72B
Rank #1

**Circulating Supply:** 19,978,850 BTC
95.1% of max

**All-Time High:** $126,080.00
-29.8%

**All-Time Low:** $67.81
+130394.0%

---

## Fear & Greed Index

### 24
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[I found this in my old pictures](https://www.reddit.com/r/Bitcoin/comments/1qipbm8/i_found_this_in_my_old_pictures/)**

and a small piece of me died again

11h ago

---

**[Sold bitcoin at 125k, took my GF out to celebrate.](https://www.reddit.com/r/Bitcoin/comments/1qj28qu/sold_bitcoin_at_125k_took_my_gf_out_to_celebrate/)**

hold strong

34m ago

---

**[Starting March 1, Steak n Shake will give all hourly employees at its company-operated restaurants a Bitcoin bonus of $0.21 for every hour worked.](https://www.reddit.com/r/Bitcoin/comments/1qiirge/starting_march_1_steak_n_shake_will_give_all/)**

Pretty dang cool. I get it’s just a marketing gimmick by Fold, but this is awesome to see.

🔗 [X (formerly Twitter)](https://x.com/steaknshake/status/2013725339374018680?s=46&t=K4ZzIe6gxU3l48Tj84If6g) • 16h ago

---

**[It's a Marathon, not a Sprint 🟠](https://www.reddit.com/r/Bitcoin/comments/1qiysy0/its_a_marathon_not_a_sprint/)**

2h ago

---

**[Breaking news](https://www.reddit.com/r/Bitcoin/comments/1qioefo/breaking_news/)**

First ever bitcoin ceo declares war on high prices: “we must lower prices so more people can afford”

12h ago

---

**[Upvote or downvote, let's see who's selling and who's buying BTC.](https://www.reddit.com/r/Bitcoin/comments/1qi52se/upvote_or_downvote_lets_see_whos_selling_and_whos/)**

1d ago

---

**[HODL](https://www.reddit.com/r/Bitcoin/comments/1qiyj92/hodl/)**

2h ago

---

**[Mmmmmmm the pain](https://www.reddit.com/r/Bitcoin/comments/1qigj2m/mmmmmmm_the_pain/)**

17h ago

---

**[The first Bitcoin Hardware Wallet with Zero-Trust Architecture (No seeds, EAL6+, Anti-Double Spend) Making offline payments possible, trustless, and secure.](https://www.reddit.com/r/Bitcoin/comments/1qj0iqp/the_first_bitcoin_hardware_wallet_with_zerotrust/)**

Hey guys just wanted to drop a quick deep dive into how the security actually works on the Vipper prototype. I know some of this stuff gets pretty dense but i tried to break it down simply. Its honestly kinda wild how much goes into making sure this thing is secure specially for offline payments. Here is the breakdown of the 5 layers I am using Layer 1 // The Vault // SE050 So basically everything happens inside this NXP SE050 chip. Its rated EAL6+ which is the same level as high end banking cards and passports. The biggest thing here is that the private key is generated inside the chip and literally never leaves. There is no API to read it out. If someone tries to physcially hack it with lasers or whatever the chip has mesh sensors that will detect it and destroy the keys (zeroization). Layer 2 // Don't trust the app This is one of the coolest parts imo. Usually with hardware wallets the phone app builds the transaction and just tells the hardware "hey sign this". The problem is a hacked app could show you one thing but tell the hardware to sign something else. We switched that up. The app only sends basic info like "Slot 1, pay Bob, 500 sats". The hardware then pulls the UTXO data from its own internal memory and builds the transaction itself. It uses its own public key to make the scriptCode. So even if the app is malware it cant trick the hardware into signing a tx for a differnt address. Layer 3 // The Magazine System Since we are focused on offline payments we use a "Magazine" system stored in the ESP32s memory. Think of it like a clip with 5 rounds (slots). You load a slot with a UTXO. When you spend it the hardware signs the tx. Immediately marks that slot as SPENT in the permanent memory. Once its marked spent there is literally no code path to make it "unspent" again unless you load a completely new UTXO. Layer 4 // The One Way Counter We use a Monotonic Counter inside the secure element, which is just a fancy way of saying a number that can only go up and never down. This is actually our secondary defense against double spending (and replay attacks). Since every single signature includes this unique counter value, you can never "rewind" the device state. Even if someone managed to glitch the memory in Layer 3 to say a slot was "Unspent," the secure element knows the counter has already moved forward. You cant sign an old state because the math literally wont validate if the counter doesn't match the current timeline. Layer 5 // No Seed Phrases // It's mean to be a spending wallet (Plus real E2EE CHAT), not a cold wallet. This might be controversial but we decided on no seed exports. With normal wallets if someone finds your 24 word paper backup they can drain your wallet from home. With Vipper the key exists only in the silicon. If you loose the device the funds are gone but it also means no one can ever clone your wallet or steal your seed because it doesnt exist outside the chip. Let me know if u have questions or if i explained something weird, still tweaking the firmware a bit! You can leave your e-mail for future updates at epheris.io it will handle cold-storage, Plausible Deniability storage, E2EE (Hardware TRNGK1) CHAT in cloud/loram etc

1h ago

---

**[I was told to drop my updated one here](https://www.reddit.com/r/Bitcoin/comments/1qirbd7/i_was_told_to_drop_my_updated_one_here/)**

Stacking may mean sacrifice today for tomorrow however your future self will thank you for your better choice over that expensive meal, especially in the ends.

9h ago

---

---

## Google News: "bitcoin"

**[Is Bitcoin a Buy, Hold, or Sell in 2026?](https://www.fool.com/investing/2026/01/21/is-bitcoin-a-buy-hold-or-sell-in-2026/)**

Despite losing value in 2025, Bitcoin's long-term trajectory is truly incredible.

The Motley Fool • 1h ago

---

**[Strategy Purchases $2.13 Billion of Bitcoin, the Most in Seven Months](https://www.bloomberg.com/news/articles/2026-01-20/strategy-purchases-2-13-billion-of-bitcoin-the-most-in-seven-months)**

Bloomberg • 1d ago

---

**[Bitcoin hoarder Strategy buys $2.13 billion in bitcoin in eight days](https://finance.yahoo.com/news/bitcoin-hoarder-strategy-buys-2-162429905.html)**

Billionaire Michael Saylor's bitcoin-focused firm Strategy said on Tuesday it ​bought about $2.13 billion worth of bitcoin ‌over the past eight days, stepping up purchases even ‌as its stock has been pressured by cryptocurrency volatility.  The company acquired roughly 22,305 bitcoin between the period of January 12 and January ⁠19, according to ‌a regulatory filing.  Saylor said in an X post on Tuesday that ‍Strategy holds 709,715 bitcoin as of January 19.

Yahoo Finance • 1d ago

---

**[Strategy Stock ($MSTR) Slides 7% as Aggressive Bitcoin Buying Continues](https://bitcoinmagazine.com/markets/strategy-stock-mstr-slides-7-percent)**

Shares of Strategy (MSTR) fell sharply, dropping over 7% in early trading as Bitcoin itself tumbled below $90,000.

Bitcoin Magazine • 1d ago

---

**[Quantum Computing Is Already Hitting Bitcoin—Here’s How](https://finance.yahoo.com/news/quantum-computing-already-hitting-bitcoin-150000966.html)**

Quantum computing risks are already influencing Bitcoin portfolios as institutions reassess security, cryptography vulnerabilities, and the network’s ability to upgrade.

Yahoo Finance • 1h ago

---

**[Steak ‘n Shake Adds $10 Million in Bitcoin Exposure Alongside BTC 'Strategic Reserve'](https://decrypt.co/355051/steak-shake-10-million-bitcoin-exposure-alongside-btc-strategic-reserve)**

Restaurant chain Steak ‘n Shake is doubling down on Bitcoin after crediting the crypto asset with driving rising sales last year.

Decrypt • 1d ago

---

**[Bitcoin news: Stake N Shake ups commitment to BTC](https://www.coindesk.com/business/2026/01/21/fast-food-chain-steak-n-shake-to-pay-hourly-workers-bitcoin-bonus)**

This follows news from a few days ago that the company added $10 million worth of bitcoin to its corporate treasury.

CoinDesk • 1h ago

---

**[Steak ‘n Shake to Pay Hourly Workers in Bitcoin Starting March](https://finance.yahoo.com/news/steak-n-shake-pay-hourly-082118325.html)**

Steak ‘n Shake will begin paying all hourly employees at company-operated restaurants a Bitcoin bonus of $0.21 for every hour worked starting March 1, with funds accessible after a two-year vesting period. The 91-year-old burger chain announced the program through a partnership with Bitcoin rewards app Fold, marking another step ...

Yahoo Finance • 8h ago

---

**[Trump mentions importance of Bitcoin and crypto legislation at Davos in rambling speech](https://www.dlnews.com/articles/regulation/trump-talked-crypto-and-bitcoin-at-davos/)**

Donald Trump spoke at the World Economic Forum in Davos, Switzerland. The US president spoke of the importance of US crypto legislation.  President Trump’s family has pushed further into the crypto world over the past year.

dlnews.com • 36m ago

---

**[Bitcoin price news: BTC rises as Trump as Trump speaks at WEF Davos](https://www.coindesk.com/markets/2026/01/21/bitcoin-bounces-to-usd89-500-gold-falls-as-trump-speaks-in-davos)**

Trump said U.S. prepares to negotiate to acquire Greenland that will not pose threat to NATO.

CoinDesk • 2h ago

---

---

## HackerNews: "bitcoin"

**[Disclosure of Aliens Could Cause Bitcoin Rush – Former Bank of England Analyst](https://news.ycombinator.com/item?id=46678682)**

She warned of "extreme price volatility in financial markets due to catastrophising or euphoria, and a collapse in confidence."

⬆️ 4 • 💬 1 • 2d ago • [Gizmodo](https://gizmodo.com/the-disclosure-of-aliens-could-cause-a-bitcoin-rush-former-bank-of-england-analyst-says-2000711471)

---

**[Show HN: ClientsOK – Forensic e-signature anchored on Bitcoin (eIDAS compliant)](https://news.ycombinator.com/item?id=46647591)**

The world's fastest legal e-signature. Blockchain-certified, mobile-first. Sign contracts instantly. Free forever.

⬆️ 3 • 💬 0 • 5d ago • [ClientsOK](https://clientsok.com/)

---

**[BIP352:  static payment addresses in Bitcoin without on-chain linkability](https://news.ycombinator.com/item?id=46647510)**

Bitcoin Improvement Proposals. Contribute to bitcoin/bips development by creating an account on GitHub.

⬆️ 3 • 💬 0 • 5d ago • [GitHub](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki)

---

**[Led by Texas, New Hampshire, U.S. states put Bitcoin on public balance sheet](https://news.ycombinator.com/item?id=46677022)**

Many U.S. states are planning bitcoin strategic reserves, and other forms of crypto financing, showing budgets are buying into the digital assets trend.

⬆️ 2 • 💬 1 • 2d ago • [CNBC](https://www.cnbc.com/2026/01/17/texas-us-states-budgets-bitcoin-crypto-strategic-reserve.html)

---

**[New fintech company claims Bitcoin will reach 100M by 2050](https://news.ycombinator.com/item?id=46662735)**

Enterprise blockchain infrastructure. Institutional-grade solutions for governments, defense, and global finance.

⬆️ 1 • 💬 2 • 3d ago • [Distributed Ledger Technologies](https://www.distributedledgertechnologies.com/)

---

**[Show HN: Hayekian BTC Daily – a local-first Bitcoin market snapshot CLI](https://news.ycombinator.com/item?id=46694344)**

What you get macOS app (Apple Silicon) — simple desktop experience for advanced BTC analysis. Optional CLI binary — Hayekian BTC Daily is a local-first, privacy-centric Bitcoin daily snapshot CLI for macOS (Apple Silicon). It pulls real BTC market data — spot, OHLC, 24h volume, and ETF flows — and turns it into a compact snapshot plus a human-readable behavioral summary. Everything runs entirely on your machine. No accounts, no telemetry. What you get: BTC spot price (multi-provider)Spot from a prioritized provider order (Binance → Coinbase → Kraken → CoinGecko), with caching and fallbacks when an API is down. Daily OHLC candlesNormalized BTC/USD candles suitable for moving averages and MACD. Kraken timestamps are normalized to candle close time so all providers align. 24h volume (CoinGecko)Global BTC 24h volume in USD, rendered as a clean number — or n/a when data is unavailable. ETF flows (Farside + SoSoValue)Real spot Bitcoin ETF flows from Farside’s HTML tables, with SoSoValue as an optional authenticated fallback. Flows are aggregated by ticker and date and summarized as net inflow or outflow. Behavioral summaryA short plain-English summary of recent Bitcoin price action and ETF flow behavior (with a local prompt and zero data sharing). Why local-first mattersHayekian BTC Daily never sends your requests or data anywhere. No accounts or API keys required. We use public, unauthenticated endpoints for all data providers. No telemetry or analytics. There are zero network calls besides the data API requests themselves. Full offline mode. If you run the CLI with no internet, it just uses cached data from the last successful run. Your Mac, your data. Basic usageAfter purchasing and downloading, unzip the app and double-click Hayekian BTC Daily to run the GUI, or use the CLI binary for advanced workflows. The app window shows today’s BTC snapshot. You can update the data with the Refresh button, or automate via CLI:./hayekian-btc-daily --updateThis updates the cached data in ~/Library/Application Support/hayekian-btc-daily and prints the latest summary to your terminal. Run --help for all CLI options. Trust and licensingHayekian BTC Daily is released under a single-user license. You may install it on multiple Macs you own, but please do not redistribute the binary or your license key. Each purchase supports continued development and additional platform support. For questions or feedback, reply to your Gumroad email receipt. Apple Silicon macOS (arm64) only — M1 / M2 / M3 / M4 Not compatible with Intel Macs / Windows / Linux (yet)

⬆️ 1 • 💬 0 • 23h ago • [Gumroad](https://hayekians.gumroad.com/l/hayekian-btc-daily-apple-silicon)

---

**[Led by Texas, New Hampshire, states race to prove can –"Bitcoin on bal sheet"](https://news.ycombinator.com/item?id=46682493)**

Many U.S. states are planning bitcoin strategic reserves, and other forms of crypto financing, showing budgets are buying into the digital assets trend.

⬆️ 1 • 💬 0 • 1d ago • [CNBC](https://www.cnbc.com/2026/01/17/texas-us-states-budgets-bitcoin-crypto-strategic-reserve.html)

---

**['It's Now Happening'–Urgent U.S. Dollar 'Collapse' Warning Issued](https://news.ycombinator.com/item?id=46697289)**

Traders are braced for this week’s inflation reading to be higher than previously expected—triggering warnings of "unprecedented stagflation"...

⬆️ 18 • 💬 4 • 20h ago • [Forbes](https://www.forbes.com/sites/digital-assets/2026/01/20/get-ready-us-dollar-collapse-warning-issued-as-markets-brace-for-gold-and-bitcoin-price-shocks/)

---

**[Is This Billionaire a Financial Genius or a Fraudster?](https://news.ycombinator.com/item?id=46648820)**

⬆️ 4 • 💬 0 • 4d ago • [nytimes.com](https://www.nytimes.com/2026/01/16/business/michael-saylor-strategy-bitcoin.html)

---

**[Covid vaccination and post-infection cancer signals [pdf]](https://news.ycombinator.com/item?id=46692325)**

⬆️ 1 • 💬 1 • 1d ago • [brownstone.org](https://brownstone.org/wp-content/uploads/2026/01/oncotarget-26-049705-PUBLISHED-2.pdf)

---

---

## YouTube Videos: "bitcoin"

**[BITCOIN..IT IS HAPPENING NOW.... *My most important video*](https://www.youtube.com/watch?v=9VJYW-R1uLQ)**

I AM NOT A FINANCIAL ADVISOR. ALL VIDEOS IS FOR ENTERTAINTMENT PURPOSE; AND I AM DOCUMENTING MY OWN ...

📺 Satoshi Stacker

👁️ 12K • 👍 693 • 💬 67 • ⏱️ 19:22 • 8h ago

---

**[Bitcoin Holders... Listen Up](https://www.youtube.com/watch?v=fSGj_s22Icc)**

https://democratizedprime.pxf.io/c/2406113/3755092/37696 Enter to win $25k USDC with Democratized Prime while earning ~9% ...

📺 Aaron Bennett

👁️ 4K • 👍 357 • 💬 69 • ⏱️ 12:17 • 7h ago

---

**[Bitcoin Investors...Trump Just Said This at Davos](https://www.youtube.com/watch?v=AWUYE6mFYJw)**

Today, let's examine Bitcoin's charts and metrics, as well as the latest Macro and Crypto news. Additionally, a look at the latest ...

📺 CryptosRUs

👁️ 11K • 👍 899 • 💬 78 • ⏱️ 41:04 • 1h ago

---

**[Another HUGE Bitcoin Dump...](https://www.youtube.com/watch?v=CtzuyN72MHo)**

Exchange Partners** Bitunix Exchange ▻ *$100000 Deposit Bonus* ▻ https://bit.ly/3Tmp1Hq BTCC Exchange ▻ *10% ...

📺 CryptosRUs

👁️ 19K • 👍 1K • 💬 312 • ⏱️ 9:10 • 15h ago

---

**[URGENT: Bitcoin And Gold MAJOR MOVES AHEAD (Profit Guide With Bitget)](https://www.youtube.com/watch?v=nbFagJSU0tI)**

Nick Valdez goes over the latest news with Gold and Bitcoin in focus. Major macro events are making crypto more volatile and ...

📺 Discover Crypto

👁️ 6K • 👍 239 • 💬 43 • ⏱️ 5:17 • 16h ago

---

**[🚨 BLACKROCK IS FORCING BITCOIN..!?!?!?!? 🚀](https://www.youtube.com/watch?v=khC32eGjuic)**

Will you Subscribe?: https://youtube.com/@britishhodl23?sub_confirmation=1 New to Bitcoin? Watch my training, “The $5m ...

📺 BRITISH HODL

👁️ 13K • 👍 871 • 💬 190 • ⏱️ 8:21 • 21h ago

---

**[Major Bitcoin Setback As 182,000 Traders Are Wiped Out!](https://www.youtube.com/watch?v=ikWpsze9-Xw)**

Bitcoin #Crypto #Finance Bitcoin and the broader crypto market are under heavy pressure this morning as a perfect storm of ...

📺 The Wolf Of All Streets

👁️ 5K • 👍 655 • 💬 71 • ⏱️ 42:24 • 1h ago

---

**[Bitcoin Looks Terrible 💥](https://www.youtube.com/watch?v=ymItXrZmVkE)**

Why Bitcoin ISN'T DEAD (Send This To 1 Friend) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 15K • 👍 347 • 💬 128 • ⏱️ 1:16 • 20h ago

---

**[Is Davos 2026 the Moment Bitcoin Becomes the Global Reserve Currency?](https://www.youtube.com/watch?v=291AJulZyK8)**

The elites flew private to Davos to plan your future without you. Markets are cracking, trust is collapsing, and Bitcoin is rising from ...

📺 Simply Bitcoin

👁️ 28K • 👍 2K • 💬 205 • ⏱️ 22:10 • 16h ago

---

**[Trump Just Unleashed Chaos in Crypto Markets](https://www.youtube.com/watch?v=UQyqD52P4yM)**

Trump crazy, Greenland, Bitcoin, gold, stocks, and altcoin updates! BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 27K • 👍 1K • 💬 241 • ⏱️ 14:45 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
