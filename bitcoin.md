---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-01-21T21:53:54.475858+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- news
- social
- videos
- cryptocurrency
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** January 21, 2026 at 21:53 UTC  
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

### $90,115.26

---

## Bitcoin Chart

**24h:** +1.8%  
**7d:** -5.8%  
**30d:** +3.1%  
**90d:** -18.9%  
**1y:** -13.3%  

---

## Bitcoin Market Stats

**Market Cap:** $1799.12B
Rank #1

**Circulating Supply:** 19,978,918 BTC
95.1% of max

**All-Time High:** $126,080.00
-28.6%

**All-Time Low:** $67.81
+132620.8%

---

## Fear & Greed Index

### 24
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[Sold bitcoin at 125k, took my GF out to celebrate.](https://www.reddit.com/r/Bitcoin/comments/1qj28qu/sold_bitcoin_at_125k_took_my_gf_out_to_celebrate/)**

hold strong

5h ago

---

**[Bitcoin at $88,000 is a great buying opportunity imo.](https://www.reddit.com/r/Bitcoin/comments/1qj56gm/bitcoin_at_88000_is_a_great_buying_opportunity_imo/)**

Thank you for your attention to this matter.

3h ago

---

**[The Era of Bitcoin Abundance is Over](https://www.reddit.com/r/Bitcoin/comments/1qjac3u/the_era_of_bitcoin_abundance_is_over/)**

95% of Bitcoin supply has been mined. There will likely never be this much Bitcoin available to purchase ever again. https://en.macromicro.me/charts/29045/bitcoin-exchange-balance-total If you look at the entire history of the Bitcoin exchange balance you can litterally see the exact date it peaked. Monday, July 26th, 2021. That day was the historical day the most Bitcoin was ever available to purchase. Since then, we have descended all the way back to 2018 level supply (nearly 8 years ago). From nearly 3.5 Million total available to purchase 1 year ago to 2.5 million today. All the while price has steadily risen from $4000 to over $120,000. It will likely continue gaining value until hitting a singularity of sorts At current pace this massive stock of Bitcoin for sale will be gone by sometime in the year 2028. Of course some Bitcoin will always be available on the market, but the amount is going to be so microscopically low that the price will be astronomically high.

44m ago

---

**[It's a Marathon, not a Sprint 🟠](https://www.reddit.com/r/Bitcoin/comments/1qiysy0/its_a_marathon_not_a_sprint/)**

7h ago

---

**[Is Bitcoin about to make traditional retirement look like a joke?](https://www.reddit.com/r/Bitcoin/comments/1qj90oh/is_bitcoin_about_to_make_traditional_retirement/)**

Traditional retirement accounts like 401(k)s typically expose you to full market risk with no principal guarantee, and high fees reduce your net returns. Is this a game changer? https://www.coindesk.com/markets/2026/01/21/blackrock-s-ibit-powers-new-bitcoin-annuity-for-u-s-retirees-via-delaware-life

1h ago

---

**[Starting March 1, Steak n Shake will give all hourly employees at its company-operated restaurants a Bitcoin bonus of $0.21 for every hour worked.](https://www.reddit.com/r/Bitcoin/comments/1qiirge/starting_march_1_steak_n_shake_will_give_all/)**

Pretty dang cool. I get it’s just a marketing gimmick by Fold, but this is awesome to see.

🔗 [X (formerly Twitter)](https://x.com/steaknshake/status/2013725339374018680?s=46&t=K4ZzIe6gxU3l48Tj84If6g) • 21h ago

---

**[I found this in my old pictures](https://www.reddit.com/r/Bitcoin/comments/1qipbm8/i_found_this_in_my_old_pictures/)**

and a small piece of me died again

16h ago

---

**[The 401K of a winner](https://www.reddit.com/r/Bitcoin/comments/1qj5ckj/the_401k_of_a_winner/)**

3h ago

---

**[The first Bitcoin Hardware Wallet with Zero-Trust Architecture (No seeds, EAL6+, Anti-Double Spend) Making offline payments possible, trustless, and secure.](https://www.reddit.com/r/Bitcoin/comments/1qj0iqp/the_first_bitcoin_hardware_wallet_with_zerotrust/)**

Hey guys just wanted to drop a quick deep dive into how the security actually works on the Vipper prototype. I know some of this stuff gets pretty dense but i tried to break it down simply. Its honestly kinda wild how much goes into making sure this thing is secure specially for offline payments. Here is the breakdown of the 5 layers I am using Layer 1 // The Vault // SE050 So basically everything happens inside this NXP SE050 chip. Its rated EAL6+ which is the same level as high end banking cards and passports. The biggest thing here is that the private key is generated inside the chip and literally never leaves. There is no API to read it out. If someone tries to physcially hack it with lasers or whatever the chip has mesh sensors that will detect it and destroy the keys (zeroization). Layer 2 // Don't trust the app This is one of the coolest parts imo. Usually with hardware wallets the phone app builds the transaction and just tells the hardware "hey sign this". The problem is a hacked app could show you one thing but tell the hardware to sign something else. We switched that up. The app only sends basic info like "Slot 1, pay Bob, 500 sats". The hardware then pulls the UTXO data from its own internal memory and builds the transaction itself. It uses its own public key to make the scriptCode. So even if the app is malware it cant trick the hardware into signing a tx for a differnt address. Layer 3 // The Magazine System Since we are focused on offline payments we use a "Magazine" system stored in the ESP32s memory. Think of it like a clip with 5 rounds (slots). You load a slot with a UTXO. When you spend it the hardware signs the tx. Immediately marks that slot as SPENT in the permanent memory. Once its marked spent there is literally no code path to make it "unspent" again unless you load a completely new UTXO. Layer 4 // The One Way Counter We use a Monotonic Counter inside the secure element, which is just a fancy way of saying a number that can only go up and never down. This is actually our secondary defense against double spending (and replay attacks). Since every single signature includes this unique counter value, you can never "rewind" the device state. Even if someone managed to glitch the memory in Layer 3 to say a slot was "Unspent," the secure element knows the counter has already moved forward. You cant sign an old state because the math literally wont validate if the counter doesn't match the current timeline. Layer 5 // No Seed Phrases // It's mean to be a spending wallet (Plus real E2EE CHAT), not a cold wallet. This might be controversial but we decided on no seed exports. With normal wallets if someone finds your 24 word paper backup they can drain your wallet from home. With Vipper the key exists only in the silicon. If you loose the device the funds are gone but it also means no one can ever clone your wallet or steal your seed because it doesnt exist outside the chip. Let me know if u have questions or if i explained something weird, still tweaking the firmware a bit! You can leave your e-mail for future updates at epheris.io it will handle cold-storage, Plausible Deniability storage, E2EE (Hardware TRNGK1) CHAT in cloud/loram etc

6h ago

---

**[HODL](https://www.reddit.com/r/Bitcoin/comments/1qiyj92/hodl/)**

7h ago

---

---

## Google News: "bitcoin"

**[Is Bitcoin a Buy, Hold, or Sell in 2026?](https://www.fool.com/investing/2026/01/21/is-bitcoin-a-buy-hold-or-sell-in-2026/)**

Despite losing value in 2025, Bitcoin's long-term trajectory is truly incredible.

The Motley Fool • 6h ago

---

**[Bitcoin price news: BTC lower for 2026 after reversing earlier Wednesday gain](https://www.coindesk.com/markets/2026/01/20/bitcoin-falls-back-to-usd87-500-giving-up-entire-2026-gain)**

There was a modest bounce after the president said the U.S. had no intention of taking Greenland by force, but prices quickly resumed their decline.

CoinDesk • 4h ago

---

**[Bitcoin Price Surges To $90,000 After Trump Delays Tariffs](https://bitcoinmagazine.com/markets/bitcoin-price-surges-to-90000-twice)**

The bitcoin price reclaimed $90,000 after a volatile trading day.

Bitcoin Magazine • 30m ago

---

**[Strategy Purchases $2.13 Billion of Bitcoin, the Most in Seven Months](https://www.bloomberg.com/news/articles/2026-01-20/strategy-purchases-2-13-billion-of-bitcoin-the-most-in-seven-months)**

Bloomberg.com • 1d ago

---

**[Bitcoin hoarder Strategy buys $2.13 billion in bitcoin in eight days](https://finance.yahoo.com/news/bitcoin-hoarder-strategy-buys-2-162429905.html)**

Billionaire Michael Saylor's bitcoin-focused firm Strategy said on Tuesday it ​bought about $2.13 billion worth of bitcoin ‌over the past eight days, stepping up purchases even ‌as its stock has been pressured by cryptocurrency volatility.  The company acquired roughly 22,305 bitcoin between the period of January 12 and January ⁠19, according to ‌a regulatory filing.  Saylor said in an X post on Tuesday that ‍Strategy holds 709,715 bitcoin as of January 19.

Yahoo Finance • 1d ago

---

**[Strategy Looks Interesting With An mNAV To Bitcoin Of 1.05 (NASDAQ:MSTR)](https://seekingalpha.com/article/4861425-strategy-looks-interesting-with-an-mnav-to-bitcoin-of-1-05)**

Strategy offers a compelling proxy for Bitcoin exposure, now trading at a 1.05x mNAV, near parity with its underlying BTC holdings. Read this MSTR stock update.

Seeking Alpha • 8h ago

---

**[This bitcoin evangelist says inflation is far exceeding official statistics — by tracking ribeye prices](https://www.marketwatch.com/story/this-bitcoin-evangelist-says-inflation-is-far-exceeding-official-statistics-by-tracking-ribeye-prices-31e0124c?gaa_at=eafs&gaa_n=AWEtsqcNZa-QFfm-97OyOII5VnLIBAP1MhrN7qJ-KUavcY6Ujh9EdyUwMLsZ&gaa_ts=69714e54&gaa_sig=cDuYfD0HAr-voJSP3zcKgm8LtlR6t1cVA3WTaAAnTvizolXJQW6uQZszDIKpZgZE8tQ2XJR6PvjC9AqIHfQupA%3D%3D)**

MarketWatch • 11h ago

---

**[SkyBridge bets on rising volatility, cautiously optimistic on bitcoin, Scaramucci says](https://www.reuters.com/business/davos/skybridge-bets-rising-volatility-cautiously-optimistic-bitcoin-scaramucci-says-2026-01-20/)**

Reuters • 23h ago

---

**[Delaware Life partners with BlackRock to offer bitcoin exposure through fixed index annuity](https://www.theblock.co/post/386345/delaware-life-partners-blackrock-bitcoin-exposure-fixed-index-annuity)**

The Block • 1d ago

---

**[Volatility is Back, and It's Weighing on Bitcoin. Is Crypto a Hedge or a Risk Asset This Time?](https://www.investopedia.com/bitcoin-dives-as-volatility-returns-is-it-a-hedge-or-risk-asset-this-time-11888610)**

Volatility has soared after President Donald Trump's latest comments suggested the U.S. might take Greenland by force. As investors panned risk assets, the price of bitcoin also took a hit.

Investopedia • 1d ago

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

⬆️ 1 • 💬 0 • 1d ago • [Gumroad](https://hayekians.gumroad.com/l/hayekian-btc-daily-apple-silicon)

---

**[Led by Texas, New Hampshire, states race to prove can –"Bitcoin on bal sheet"](https://news.ycombinator.com/item?id=46682493)**

Many U.S. states are planning bitcoin strategic reserves, and other forms of crypto financing, showing budgets are buying into the digital assets trend.

⬆️ 1 • 💬 0 • 2d ago • [CNBC](https://www.cnbc.com/2026/01/17/texas-us-states-budgets-bitcoin-crypto-strategic-reserve.html)

---

**['It's Now Happening'–Urgent U.S. Dollar 'Collapse' Warning Issued](https://news.ycombinator.com/item?id=46697289)**

Traders are braced for this week’s inflation reading to be higher than previously expected—triggering warnings of "unprecedented stagflation"...

⬆️ 18 • 💬 4 • 1d ago • [Forbes](https://www.forbes.com/sites/digital-assets/2026/01/20/get-ready-us-dollar-collapse-warning-issued-as-markets-brace-for-gold-and-bitcoin-price-shocks/)

---

**[Is This Billionaire a Financial Genius or a Fraudster?](https://news.ycombinator.com/item?id=46648820)**

⬆️ 4 • 💬 0 • 5d ago • [nytimes.com](https://www.nytimes.com/2026/01/16/business/michael-saylor-strategy-bitcoin.html)

---

**[Covid vaccination and post-infection cancer signals [pdf]](https://news.ycombinator.com/item?id=46692325)**

⬆️ 1 • 💬 1 • 1d ago • [brownstone.org](https://brownstone.org/wp-content/uploads/2026/01/oncotarget-26-049705-PUBLISHED-2.pdf)

---

---

## YouTube Videos: "bitcoin"

**[Bitcoin Investors...Trump Just Said This at Davos](https://www.youtube.com/watch?v=AWUYE6mFYJw)**

Today, let's examine Bitcoin's charts and metrics, as well as the latest Macro and Crypto news. Additionally, a look at the latest ...

📺 CryptosRUs

👁️ 28K • 👍 1K • 💬 120 • ⏱️ 41:04 • 6h ago

---

**[Did President Trump Just Reveal His Strategic Bitcoin Plan?](https://www.youtube.com/watch?v=VyX3Rz77ITg)**

While the headlines were screaming nonsense, something subtle but massive changed in the Bitcoin world. Politicians, analysts ...

📺 Simply Bitcoin

👁️ 8K • 👍 701 • 💬 90 • ⏱️ 20:50 • 8h ago

---

**[🚨 REVEALED: BLACKROCK IS ABOUT TO CRASH CRYPTO MARKET](https://www.youtube.com/watch?v=PzY0a31yIbI)**

HERE IS WHY CRYPTO IS CRASHING (WHAT TO DO NEXT) ✓ Trade crypto on Bitunix (no kyc, $10000 bonus): ...

📺 Altcoin Daily

👁️ 66K • 👍 3K • 💬 288 • ⏱️ 9:30 • 1d ago

---

**[BITCOIN..IT IS HAPPENING NOW.... *My most important video*](https://www.youtube.com/watch?v=9VJYW-R1uLQ)**

I AM NOT A FINANCIAL ADVISOR. ALL VIDEOS IS FOR ENTERTAINTMENT PURPOSE; AND I AM DOCUMENTING MY OWN ...

📺 Satoshi Stacker

👁️ 14K • 👍 735 • 💬 66 • ⏱️ 19:22 • 13h ago

---

**[Major Bitcoin Setback As 182,000 Traders Are Wiped Out!](https://www.youtube.com/watch?v=ikWpsze9-Xw)**

Bitcoin #Crypto #Finance Bitcoin and the broader crypto market are under heavy pressure this morning as a perfect storm of ...

📺 The Wolf Of All Streets

👁️ 18K • 👍 1K • 💬 169 • ⏱️ 42:24 • 7h ago

---

**[Bitcoin Looks Terrible 💥](https://www.youtube.com/watch?v=ymItXrZmVkE)**

Why Bitcoin ISN'T DEAD (Send This To 1 Friend) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 17K • 👍 367 • 💬 130 • ⏱️ 1:16 • 1d ago

---

**[WARNING: BITCOIN DOUBLE DEATH CROSS – THIS HAPPENS NEXT](https://www.youtube.com/watch?v=7kUfpZ9EM7g)**

Trade Like A Tourist Or Join The Pros FFA Is Where The Real Ones Go https://cryptocrewuniversity.com/ffa MASSIVE ...

📺 Crypto Crew University

👁️ 23K • 👍 2K • 💬 156 • ⏱️ 18:43 • 7h ago

---

**[BITCOIN PUMP INCOMING 🚨](https://www.youtube.com/watch?v=Qj0CL9RH0Pk)**

WEEX: https://cryptokid.io/WEEX-Bonus UP TO $30000 $14000 Competition: https://cryptokid.io/TradingCompetition ...

📺 Crypto Kid

👁️ 5K • 👍 746 • 💬 63 • ⏱️ 7:51 • 5h ago

---

**[🚨 BLACKROCK IS FORCING BITCOIN..!?!?!?!? 🚀](https://www.youtube.com/watch?v=khC32eGjuic)**

Will you Subscribe?: https://youtube.com/@britishhodl23?sub_confirmation=1 New to Bitcoin? Watch my training, “The $5m ...

📺 BRITISH HODL

👁️ 14K • 👍 895 • 💬 129 • ⏱️ 8:21 • 1d ago

---

**[Michael Saylor Explains Why Bitcoin Doesn’t Need a New High](https://www.youtube.com/watch?v=Ey6aXnh2NKU)**

Bitcoin doesn't need a new all-time high to be winning. In this clip, Michael Saylor explains why regulatory clarity, banking ...

📺 Swan Bitcoin

👁️ 16K • 👍 575 • 💬 31 • ⏱️ 1:32 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
