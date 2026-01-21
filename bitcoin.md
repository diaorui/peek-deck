---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-01-21T19:28:16.488336+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- news
- cryptocurrency
- social
- videos
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** January 21, 2026 at 19:28 UTC  
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

### $88,764.52

---

## Bitcoin Chart

**24h:** -0.9%  
**7d:** -7.1%  
**30d:** +1.8%  
**90d:** -19.8%  
**1y:** -14.3%  

---

## Bitcoin Market Stats

**Market Cap:** $1768.37B
Rank #1

**Circulating Supply:** 19,978,909 BTC
95.1% of max

**All-Time High:** $126,080.00
-29.8%

**All-Time Low:** $67.81
+130429.4%

---

## Fear & Greed Index

### 24
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[Sold bitcoin at 125k, took my GF out to celebrate.](https://www.reddit.com/r/Bitcoin/comments/1qj28qu/sold_bitcoin_at_125k_took_my_gf_out_to_celebrate/)**

hold strong

3h ago

---

**[Bitcoin at $88,000 is a great buying opportunity imo.](https://www.reddit.com/r/Bitcoin/comments/1qj56gm/bitcoin_at_88000_is_a_great_buying_opportunity_imo/)**

Thank you for your attention to this matter.

1h ago

---

**[It's a Marathon, not a Sprint 🟠](https://www.reddit.com/r/Bitcoin/comments/1qiysy0/its_a_marathon_not_a_sprint/)**

5h ago

---

**[Starting March 1, Steak n Shake will give all hourly employees at its company-operated restaurants a Bitcoin bonus of $0.21 for every hour worked.](https://www.reddit.com/r/Bitcoin/comments/1qiirge/starting_march_1_steak_n_shake_will_give_all/)**

Pretty dang cool. I get it’s just a marketing gimmick by Fold, but this is awesome to see.

🔗 [X (formerly Twitter)](https://x.com/steaknshake/status/2013725339374018680?s=46&t=K4ZzIe6gxU3l48Tj84If6g) • 18h ago

---

**[I found this in my old pictures](https://www.reddit.com/r/Bitcoin/comments/1qipbm8/i_found_this_in_my_old_pictures/)**

and a small piece of me died again

14h ago

---

**[Breaking news](https://www.reddit.com/r/Bitcoin/comments/1qioefo/breaking_news/)**

First ever bitcoin ceo declares war on high prices: “we must lower prices so more people can afford”

14h ago

---

**[HODL](https://www.reddit.com/r/Bitcoin/comments/1qiyj92/hodl/)**

5h ago

---

**[The first Bitcoin Hardware Wallet with Zero-Trust Architecture (No seeds, EAL6+, Anti-Double Spend) Making offline payments possible, trustless, and secure.](https://www.reddit.com/r/Bitcoin/comments/1qj0iqp/the_first_bitcoin_hardware_wallet_with_zerotrust/)**

Hey guys just wanted to drop a quick deep dive into how the security actually works on the Vipper prototype. I know some of this stuff gets pretty dense but i tried to break it down simply. Its honestly kinda wild how much goes into making sure this thing is secure specially for offline payments. Here is the breakdown of the 5 layers I am using Layer 1 // The Vault // SE050 So basically everything happens inside this NXP SE050 chip. Its rated EAL6+ which is the same level as high end banking cards and passports. The biggest thing here is that the private key is generated inside the chip and literally never leaves. There is no API to read it out. If someone tries to physcially hack it with lasers or whatever the chip has mesh sensors that will detect it and destroy the keys (zeroization). Layer 2 // Don't trust the app This is one of the coolest parts imo. Usually with hardware wallets the phone app builds the transaction and just tells the hardware "hey sign this". The problem is a hacked app could show you one thing but tell the hardware to sign something else. We switched that up. The app only sends basic info like "Slot 1, pay Bob, 500 sats". The hardware then pulls the UTXO data from its own internal memory and builds the transaction itself. It uses its own public key to make the scriptCode. So even if the app is malware it cant trick the hardware into signing a tx for a differnt address. Layer 3 // The Magazine System Since we are focused on offline payments we use a "Magazine" system stored in the ESP32s memory. Think of it like a clip with 5 rounds (slots). You load a slot with a UTXO. When you spend it the hardware signs the tx. Immediately marks that slot as SPENT in the permanent memory. Once its marked spent there is literally no code path to make it "unspent" again unless you load a completely new UTXO. Layer 4 // The One Way Counter We use a Monotonic Counter inside the secure element, which is just a fancy way of saying a number that can only go up and never down. This is actually our secondary defense against double spending (and replay attacks). Since every single signature includes this unique counter value, you can never "rewind" the device state. Even if someone managed to glitch the memory in Layer 3 to say a slot was "Unspent," the secure element knows the counter has already moved forward. You cant sign an old state because the math literally wont validate if the counter doesn't match the current timeline. Layer 5 // No Seed Phrases // It's mean to be a spending wallet (Plus real E2EE CHAT), not a cold wallet. This might be controversial but we decided on no seed exports. With normal wallets if someone finds your 24 word paper backup they can drain your wallet from home. With Vipper the key exists only in the silicon. If you loose the device the funds are gone but it also means no one can ever clone your wallet or steal your seed because it doesnt exist outside the chip. Let me know if u have questions or if i explained something weird, still tweaking the firmware a bit! You can leave your e-mail for future updates at epheris.io it will handle cold-storage, Plausible Deniability storage, E2EE (Hardware TRNGK1) CHAT in cloud/loram etc

4h ago

---

**[The 401K of a winner](https://www.reddit.com/r/Bitcoin/comments/1qj5ckj/the_401k_of_a_winner/)**

1h ago

---

**[Upvote or downvote, let's see who's selling and who's buying BTC.](https://www.reddit.com/r/Bitcoin/comments/1qi52se/upvote_or_downvote_lets_see_whos_selling_and_whos/)**

1d ago

---

---

## Google News: "bitcoin"

**[Bitcoin price news: BTC lower for 2026 after reversing earlier Wednesday gain](https://www.coindesk.com/markets/2026/01/20/bitcoin-falls-back-to-usd87-500-giving-up-entire-2026-gain)**

There was a modest bounce after the president said the U.S. had no intention of taking Greenland by force, but prices quickly resumed their decline.

CoinDesk • 2h ago

---

**[Is Bitcoin a Buy, Hold, or Sell in 2026?](https://www.fool.com/investing/2026/01/21/is-bitcoin-a-buy-hold-or-sell-in-2026/)**

Despite losing value in 2025, Bitcoin's long-term trajectory is truly incredible.

The Motley Fool • 4h ago

---

**[BlackRock’s IBIT powers new bitcoin annuity for U.S. retirees via Delaware Life](https://www.coindesk.com/markets/2026/01/21/blackrock-s-ibit-powers-new-bitcoin-annuity-for-u-s-retirees-via-delaware-life)**

The first-of-its-kind FIA, according to the companies, offers crypto exposure with principal protection, aiming to attract cautious investors near retirement.

CoinDesk • 7m ago

---

**[Bitcoin erases 2026 gains despite Trump’s bullish Davos remarks](https://uk.finance.yahoo.com/video/bitcoin-erases-2026-gains-despite-190312613.html)**

Yahoo Finance UK • 25m ago

---

**[This bitcoin evangelist says inflation is far exceeding official statistics — by tracking ribeye prices](https://www.marketwatch.com/story/this-bitcoin-evangelist-says-inflation-is-far-exceeding-official-statistics-by-tracking-ribeye-prices-31e0124c?gaa_at=eafs&gaa_n=AWEtsqe0b_e2Q2J_eIrXNCNw_8p0ETReiQqzthNe60dHiEbO2AoGq7oRP9ZY&gaa_ts=69712c37&gaa_sig=1q9S8Id8APmSYBtGWqN3Isx1Gj3OoZKbXRTbS_G7MUUulb1-Y7XnGQjsIyZ2ZepgK0XtL-HyzlR5NedBYbok8A%3D%3D)**

MarketWatch • 9h ago

---

**[SkyBridge bets on rising volatility, cautiously optimistic on bitcoin, Scaramucci says](https://www.reuters.com/business/davos/skybridge-bets-rising-volatility-cautiously-optimistic-bitcoin-scaramucci-says-2026-01-20/)**

Reuters • 20h ago

---

**[Strategy Purchases $2.13 Billion of Bitcoin, the Most in Seven Months](https://www.bloomberg.com/news/articles/2026-01-20/strategy-purchases-2-13-billion-of-bitcoin-the-most-in-seven-months)**

Bloomberg.com • 1d ago

---

**[Bitcoin hoarder Strategy buys $2.13 billion in bitcoin in eight days](https://finance.yahoo.com/news/bitcoin-hoarder-strategy-buys-2-162429905.html)**

Billionaire Michael Saylor's bitcoin-focused firm Strategy said on Tuesday it ​bought about $2.13 billion worth of bitcoin ‌over the past eight days, stepping up purchases even ‌as its stock has been pressured by cryptocurrency volatility.  The company acquired roughly 22,305 bitcoin between the period of January 12 and January ⁠19, according to ‌a regulatory filing.  Saylor said in an X post on Tuesday that ‍Strategy holds 709,715 bitcoin as of January 19.

Yahoo Finance • 1d ago

---

**[Strategy Stock ($MSTR) Slides 7% as Aggressive Bitcoin Buying Continues](https://bitcoinmagazine.com/markets/strategy-stock-mstr-slides-7-percent)**

Shares of Strategy (MSTR) fell sharply, dropping over 7% in early trading as Bitcoin itself tumbled below $90,000.

Bitcoin Magazine • 1d ago

---

**[Bitcoin January 21 daily chart alert - Bears in control](https://www.kitco.com/news/article/2026-01-21/bitcoin-january-21-daily-chart-alert-bears-control)**

The Kitco News Team brings you the latest news, videos, analysis and opinions regarding Precious Metals, Crypto, Mining, World Markets and Global Economy.

KITCO • 9h ago

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

⬆️ 18 • 💬 4 • 23h ago • [Forbes](https://www.forbes.com/sites/digital-assets/2026/01/20/get-ready-us-dollar-collapse-warning-issued-as-markets-brace-for-gold-and-bitcoin-price-shocks/)

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

👁️ 20K • 👍 1K • 💬 113 • ⏱️ 41:04 • 3h ago

---

**[Did President Trump Just Reveal His Strategic Bitcoin Plan?](https://www.youtube.com/watch?v=VyX3Rz77ITg)**

While the headlines were screaming nonsense, something subtle but massive changed in the Bitcoin world. Politicians, analysts ...

📺 Simply Bitcoin

👁️ 6K • 👍 599 • 💬 77 • ⏱️ 20:50 • 5h ago

---

**[Major Bitcoin Setback As 182,000 Traders Are Wiped Out!](https://www.youtube.com/watch?v=ikWpsze9-Xw)**

Bitcoin #Crypto #Finance Bitcoin and the broader crypto market are under heavy pressure this morning as a perfect storm of ...

📺 The Wolf Of All Streets

👁️ 12K • 👍 1K • 💬 138 • ⏱️ 42:24 • 4h ago

---

**[BITCOIN..IT IS HAPPENING NOW.... *My most important video*](https://www.youtube.com/watch?v=9VJYW-R1uLQ)**

I AM NOT A FINANCIAL ADVISOR. ALL VIDEOS IS FOR ENTERTAINTMENT PURPOSE; AND I AM DOCUMENTING MY OWN ...

📺 Satoshi Stacker

👁️ 13K • 👍 721 • 💬 71 • ⏱️ 19:22 • 11h ago

---

**[Bitcoin Holders... Listen Up](https://www.youtube.com/watch?v=fSGj_s22Icc)**

https://democratizedprime.pxf.io/c/2406113/3755092/37696 Enter to win $25k USDC with Democratized Prime while earning ~9% ...

📺 Aaron Bennett

👁️ 5K • 👍 426 • 💬 69 • ⏱️ 12:17 • 10h ago

---

**[Bitcoin Looks Terrible 💥](https://www.youtube.com/watch?v=ymItXrZmVkE)**

Why Bitcoin ISN'T DEAD (Send This To 1 Friend) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 16K • 👍 362 • 💬 130 • ⏱️ 1:16 • 22h ago

---

**[WARNING: BITCOIN DOUBLE DEATH CROSS – THIS HAPPENS NEXT](https://www.youtube.com/watch?v=7kUfpZ9EM7g)**

Trade Like A Tourist Or Join The Pros FFA Is Where The Real Ones Go https://cryptocrewuniversity.com/ffa MASSIVE ...

📺 Crypto Crew University

👁️ 17K • 👍 2K • 💬 157 • ⏱️ 18:43 • 5h ago

---

**[Could This Single Announcement Send Bitcoin to $10 Million?](https://www.youtube.com/watch?v=hKlFmLnXyBs)**

The financial system is more fragile than ever and central banks know it. From alien disclosure triggering panic to inflation making ...

📺 Simply Bitcoin

👁️ 41K • 👍 3K • 💬 316 • ⏱️ 21:56 • 1d ago

---

**[🚨 REVEALED: BLACKROCK IS ABOUT TO CRASH CRYPTO MARKET](https://www.youtube.com/watch?v=PzY0a31yIbI)**

HERE IS WHY CRYPTO IS CRASHING (WHAT TO DO NEXT) ✓ Trade crypto on Bitunix (no kyc, $10000 bonus): ...

📺 Altcoin Daily

👁️ 63K • 👍 3K • 💬 284 • ⏱️ 9:30 • 21h ago

---

**[URGENT: Bitcoin And Gold MAJOR MOVES AHEAD (Profit Guide With Bitget)](https://www.youtube.com/watch?v=nbFagJSU0tI)**

Nick Valdez goes over the latest news with Gold and Bitcoin in focus. Major macro events are making crypto more volatile and ...

📺 Discover Crypto

👁️ 6K • 👍 241 • 💬 43 • ⏱️ 5:17 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*
