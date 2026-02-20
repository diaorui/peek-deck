---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-02-20T17:39:09.238597+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- news
- cryptocurrency
- videos
- social
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** February 20, 2026 at 17:39 UTC  
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

### $67,115.19

---

## Bitcoin Chart

**24h:** +0.1%  
**7d:** -4.0%  
**30d:** -25.1%  
**90d:** -22.9%  
**1y:** -30.3%  

---

## Bitcoin Market Stats

**Market Cap:** $1339.87B
Rank #1

**Circulating Supply:** 19,992,337 BTC
95.2% of max

**All-Time High:** $126,080.00
-46.9%

**All-Time Low:** $67.81
+98705.5%

---

## Fear & Greed Index

### 7
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[Watching a skeptic explain why BTC is over for the 100th time](https://www.reddit.com/r/Bitcoin/comments/1r9tyhl/watching_a_skeptic_explain_why_btc_is_over_for/)**

5h ago

---

**[Power Law model shows BTC at $68k is deep in the buy zone (13.7%)](https://www.reddit.com/r/Bitcoin/comments/1ra0vwj/power_law_model_shows_btc_at_68k_is_deep_in_the/)**

Been tracking the Bitcoin Power Law model for a while now. Here's this week's update. BTC is sitting at $67,745. Power Law fair value is around $123,947 — about 45% below fair value. Oscillator reads 13.7% The oscillator has ticked up marginally from 13.6% to 13.7%, remaining firmly entrenched in the Deep Buy Zone (0–25%). This is historically rare territory that typically occurs only 1–2 times per halving cycle. The oscillator's EMA(150) at 31.2% remains below its EMA(350) at 37.7%, maintaining a bearish spread of -6.5 points. This configuration — deep value combined with bearish momentum — represents the model's maximum accumulation signal. Full breakdown with charts here if anyone's interested: https://timetobuybitcoin.com/analysis/maximum-accumulation-zone-deepens-oscillator-at-137-amid-his-2026-02-20 Not financial advice, just sharing the data. Curious what you guys think.

38m ago

---

**[Today My Family Got off Zero & Joined the .1 club🚀](https://www.reddit.com/r/Bitcoin/comments/1r9hwmw/today_my_family_got_off_zero_joined_the_1_club/)**

I don’t care if it dips more…. We just had to get in with that tax return. I’d rather it dip to 50k & miss out on those small amounts of BTC than have it rip to 100k or beyond tomorrow and live with the regret that I’ll never see BTC that low ever again! Tonight is the first night I can rest peacefully knowing my family is hedged against the decaying dollar and positioned to benefit from deflation from government inflation. The last one using the dollar gets stuck holding the bag of poverty. Not this family🙏🏼🚀

16h ago

---

**[What does Bitcoin look like in 20 years if adoption keeps growing?](https://www.reddit.com/r/Bitcoin/comments/1r9rnci/what_does_bitcoin_look_like_in_20_years_if/)**

I’ve been thinking less about short-term price lately and more about what Bitcoin could actually look like 10–20 years from now. Not in terms of “how high does it go,” but in terms of real usage. Like… what happens if adoption just keeps growing? More people self-custodying instead of leaving coins on exchanges. More businesses accepting BTC directly. Cross-border payments without needing banks in the middle. People choosing to save in something with a fixed supply instead of constantly inflating currencies. At some point, if that trend continues, Bitcoin stops being seen as just a speculative asset and starts looking more like infrastructure. A base layer. A monetary network that people actually rely on. And historically, when a new monetary network gains critical mass, the people who paid attention early weren’t just “lucky.” They understood what was happening before it became obvious to everyone else. So for me the real question isn’t will price go up. It’s what happens if a censorship resistant, fixed-supply asset just keeps gaining adoption globally. Curious how others here think about the 10–20 year outlook, purely from a network and usage perspective.

7h ago

---

**[Something is changing in this Bitcoin cycle. Our Lightning data since 2022 suggests it.](https://www.reddit.com/r/Bitcoin/comments/1r9w97t/something_is_changing_in_this_bitcoin_cycle_our/)**

We have accepted Bitcoin Lightning since May 2022. This downturn is fundamentally different from previous cycles. In the past, both transaction count and total volume dropped. This time, they have not. Why?

3h ago

---

**[Fear and Greed Index](https://www.reddit.com/r/Bitcoin/comments/1r9lbwo/fear_and_greed_index/)**

The fear-and-greed index is in a state of sustained extreme fear. This has historically signaled the bottom of a cycle. I don't think the index alone is a good barometer for trading, but it's hard to ignore when it's pegged to extreme fear for weeks or months. I'm buying - we'll see how that works out. ;)

13h ago

---

**[We're searching for Bitcoin wallets generated with weak entropy from 2009-2012 — here's what early wallet software got wrong](https://www.reddit.com/r/Bitcoin/comments/1r9xxr0/were_searching_for_bitcoin_wallets_generated_with/)**

Between 2009 and 2012, Bitcoin wallet software was experimental. Many early tools used predictable random number generators to create private keys: - Debian OpenSSL bug (CVE-2008-0166) — A catastrophic bug shipped in 2008 reduced all randomness to just the process ID. Only 65,536 possible private keys. Any wallet generated on Debian/Ubuntu during that period is trivially crackable. - Timestamp-seeded LCGs — glibc and MSVC srand(time(NULL)) followed by rand() to generate each byte of the private key. The entire search space is just ~62.8 million seeds (one per second from genesis to early 2011). - Randstorm (V8 MWC1616) — BitcoinJS and other web-based wallets relied on Chrome's Math.random(), which used a weak PRNG before 2013. Disclosed by Unciphered in 2023, this affected wallets created through browser interfaces. - Brain wallets — SHA256("password"), SHA256("1"), SHA256("12345") — people actually did this, and the keys are still sitting on-chain. - Java LCG — Early Android wallets (BitcoinJ) seeded java.util.Random with millisecond timestamps. There are roughly 2,845 known funded addresses believed to have been created by these weak methods. We built a distributed GPU project to systematically search through all 23 weak key patterns. The pipeline runs entirely on CUDA — each GPU thread generates a private key using the weak algorithm, does the full secp256k1 multiplication, SHA-256, RIPEMD-160, and checks against all target addresses via a bloom filter. An RTX 3090 tests ~130 million keys per second. The small keyspaces are already exhausted (Debian OpenSSL was done in milliseconds). We're currently grinding through SHA-256 of sequential integers — a 2^64 keyspace that will take sustained GPU power. How rewards work if a wallet is found: - 70% distributed to GPU contributors based on verified compute time - 20% to platform development and infrastructure - 10% donated to medical research Website with live stats and the full technical writeup: https://b4q.io Curious if anyone here remembers using any of these early wallet tools. Some of these bugs were well-known at the time but the affected addresses are still funded years later.

2h ago

---

**[Bitcoin doesn't give a duck about you](https://www.reddit.com/r/Bitcoin/comments/1r9b1pc/bitcoin_doesnt_give_a_duck_about_you/)**

20h ago

---

**[These Finnish homes are being heated by a surprising source: Bitcoin](https://www.reddit.com/r/Bitcoin/comments/1r9rqi9/these_finnish_homes_are_being_heated_by_a/)**

Heating homes with Bitcoin obviously isn't a surprise to this sub. What's surprising is the website, publishing the article - Grist. Their about us page says: Grist is a nonprofit, independent media organization dedicated to reporting on climate change. Since 1999, we have used the power of journalism to engage the public about the perils of one of the most existential threats we face. We seek to document the often unequal impacts of climate change on communities in the United States and globally — as well as to show the promise of equitable climate solutions. With 40 journalists spread across nearly 20 U.S. states, Grist is the largest and most experienced climate-focused newsroom in the country. Our work aims to illustrate how the effects of a warming planet intersect with, well, everything.... https://grist.org/about/

🔗 [Grist](https://grist.org/buildings/bitcoin-cryptocurrency-district-heat-finland/) • 7h ago

---

**[What if your heating system actually paid you back?](https://www.reddit.com/r/Bitcoin/comments/1r9y132/what_if_your_heating_system_actually_paid_you_back/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=Jg89U0y3tK4) • 2h ago

---

---

## Google News: "bitcoin"

**[Eric Trump shrugs off bitcoin's recent slump: 'If you don't have the backbone ... go invest in some boring bond'](https://finance.yahoo.com/news/eric-trump-shrugs-off-bitcoins-recent-slump-if-you-dont-have-the-backbone--go-invest-in-some-boring-bond-193400545.html)**

During a wide-ranging interview with Yahoo Finance, Eric Trump weighed in on bitcoin, crypto legislation, his personal debanking experience, and the latest digital asset project between the Trump Organization and his flagship crypto venture, World Liberty Financial.

Yahoo Finance • 22h ago

---

**[Bitcoin difficulty jumps 15% largest increase since 2021, despite price slump](https://www.coindesk.com/markets/2026/02/20/bitcoin-difficulty-jumps-15-largest-increase-since-2021-despite-price-slump)**

Bitcoin difficulty rebounds to 144.4T as hashrate recovers to 1 ZH/s despite multi year low hashprice.

CoinDesk • 7h ago

---

**[France Clears Sale of EDF Data Center Unit to Bitcoin Miner MARA](https://www.bloomberg.com/news/articles/2026-02-20/france-clears-sale-of-edf-data-center-unit-to-bitcoin-miner-mara)**

Bloomberg • 2h ago

---

**[Bitcoin Trapped in Fragile Trading as Hedge Funds Pivot to Cash](https://www.bloomberg.com/news/articles/2026-02-19/bitcoin-settles-in-trading-range-while-hedge-funds-pivot-to-cash)**

Bloomberg • 19h ago

---

**[Bitcoin and Ethereum are off to their worst start of the year in a decade—but some see a rebound in sight](https://fortune.com/2026/02/20/bitcoin-ethereum-price-today-worst-starts-in-history-rebound-in-sight/)**

The year-to-date performances of the world’s two largest cryptocurrencies are some of the most bearish on record, according to data from CoinGecko.

Fortune • 38m ago

---

**[Bitcoin Won Over Wall Street and Now It’s Paying the Price](https://finance.yahoo.com/news/bitcoin-won-over-wall-street-124511013.html)**

Since Oct. 10, roughly $8.5 billion has flowed out of US-listed spot Bitcoin exchange-traded funds.  Futures exposure on the Chicago Mercantile Exchange has fallen by about two-thirds from its late-2024 peak to roughly $8 billion.  Prices on Coinbase, the venue favored by many American institutions, have persistently traded at a discount to offshore exchange Binance — a signal of sustained US selling.

Yahoo Finance • 2d ago

---

**[Bitcoin Pops After Supreme Court Strikes Down Trump’s Tariffs](https://bitcoinmagazine.com/news/bitcoin-pops-after-supreme-court)**

The Supreme Court on Friday struck down Trump’s global tariffs, ruling 6-3 that he exceeded his emergency powers.

Bitcoin Magazine • 44m ago

---

**[Bitcoin remains below key onchain level as ETF outflows persist, liquidity stays tight: analysts](https://www.theblock.co/post/390602/bitcoin-remains-below-key-onchain-level-as-etf-outflows-persist-liquidity-stays-tight-analysts)**

Analysts warned that weak ETF flows, constrained liquidity, and fragile accumulation are keeping bitcoin's price rangebound and indecisive.

The Block • 5h ago

---

**[Clarity Act Odds Briefly Spike; Bitcoin Miner Tumbles On AI Funding Plans](https://www.investors.com/news/clarity-act-odds-spike-stablecoin-discussions-white-house-bitdeer-funds-ai-data-center/)**

Investor's Business Daily • 20h ago

---

**[Opinion: Stablecoins, the new kid on the crypto block, may be killing Bitcoin](https://www.theglobeandmail.com/business/commentary/article-stablecoins-cryptocurrency-bitcoin-genius-act/)**

The more enticing features of stablecoins, including the quasi-anonymous nature of payments, could limit Bitcoin’s growth

The Globe and Mail • 1d ago

---

---

## HackerNews: "bitcoin"

**[£189,486,935,770 in Bitcoin. Lost Forever](https://news.ycombinator.com/item?id=47018882)**

Track billions in lost Bitcoin. Explore case studies, check dormant wallets, calculate your losses, and protect your Bitcoin inheritance.

⬆️ 3 • 💬 5 • 5d ago • [BTC Graveyard](https://btcgraveyard.com/)

---

**[Bitcoin oracle that sells cryptographically signed price data for micropayments](https://news.ycombinator.com/item?id=47050321)**

SLO is a minimal protocol that allows agents and contracts to purchase signed, verifiable BTCUSD price assertions—using Lightning payments—with a design that generalizes to other metrics with varia...

⬆️ 3 • 💬 0 • 3d ago • [GitHub](https://github.com/jonathanbulkeley/sovereign-lightning-oracle)

---

**[A Bitcoin Blunder for the Ages: $40B Accidentally Given Away](https://news.ycombinator.com/item?id=47017670)**

⬆️ 2 • 💬 0 • 5d ago • [wsj.com](https://www.wsj.com/finance/currencies/a-bitcoin-blunder-for-the-ages-40-billion-accidentally-given-away-3a207eac)

---

**[Bitcoin's plunge should end the hype that it is digital gold](https://news.ycombinator.com/item?id=47047392)**

⬆️ 1 • 💬 2 • 3d ago • [thehill.com](https://thehill.com/opinion/finance/5735525-bitcoin-gold-performance-disparity/)

---

**[Show HN: GPU-accelerated search for Bitcoin keys generated with weak entropy](https://news.ycombinator.com/item?id=47053532)**

Distributed GPU computing platform searching for Bitcoin private keys generated by weak entropy sources in early Bitcoin software. 70% of recovered BTC goes to contributors.

⬆️ 1 • 💬 1 • 2d ago • [b4q.io](https://b4q.io/research)

---

**[Professional Bitcoin Asset Tracing – Intelligence Cyber Wizard](https://news.ycombinator.com/item?id=47086751)**

⬆️ 1 • 💬 0 • 5h ago

---

**[Fire calculator that takes Bitcoin holdings into account](https://news.ycombinator.com/item?id=47075139)**

Financial independence on a bitcoin standard

⬆️ 1 • 💬 0 • 1d ago • [FIRE BTC](https://calc.firebtc.io/)

---

**[Show HN: Natural language search across Kalshi and Polymarket](https://news.ycombinator.com/item?id=47088680)**

Fast natural language search across 60,000+ prediction markets on Kalshi and Polymarket. Sports, crypto, weather, politics and more.

⬆️ 1 • 💬 0 • 2h ago • [Attena](https://www.attena.xyz/)

---

**[Regulated Crypto Investigation Team – Intelligence Cyber Wizard Services](https://news.ycombinator.com/item?id=47085488)**

⬆️ 1 • 💬 0 • 8h ago

---

**[Regulated Crypto Investigation Team – Intelligence Cyber Wizard Services](https://news.ycombinator.com/item?id=47084865)**

⬆️ 1 • 💬 0 • 10h ago

---

---

## YouTube Videos: "bitcoin"

**[Trump Is About To Unleash A Massive SHOCK To The Bitcoin Price | Larry Lepard](https://www.youtube.com/watch?v=R1RgSzYtHg8)**

Watch The FULL Interview: https://www.youtube.com/watch?v=-i8humbpZJQ FREE Daily On-Chain Analysis & Crypto News In ...

📺 Library Of Wealth

👁️ 4K • 👍 240 • 💬 74 • ⏱️ 14:04 • 12h ago

---

**[BITCOIN REVERSAL IMMINENT — IT&#39;S HAPPENING NOW!](https://www.youtube.com/watch?v=B_6KEvI4cB0)**

https://youtu.be/RThI3UUSpwc?si=t0m9cQVPXyt35ZMD BUY ONE 1-STEP CHALLENGE → GET ...

📺 100XClub

👁️ 7K • 👍 876 • 💬 272 • ⏱️ 9:49 • 7h ago

---

**[Bitcoin’s “Final” Warning: The 7-Day Countdown](https://www.youtube.com/watch?v=kwWrreTKJmA)**

Aliens, Bitcoin, Tesla, and altcoin updates as Clarity Act looms. BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 10K • 👍 613 • 💬 86 • ⏱️ 17:34 • 6h ago

---

**[IS BITCOIN ACTUALLY DEAD??!!](https://www.youtube.com/watch?v=-itjlUK81JA)**

Join The Community: https://bit.ly/FefeCommunity FOLLOW FEFE FOR THE BEST ALPHA ...

📺 100XClub

👁️ 2K • 👍 182 • 💬 61 • ⏱️ 1:35 • 2h ago

---

**[🚨 BREAKING: Trump’s Global Tariffs DENIED!](https://www.youtube.com/watch?v=C-xzZJYNVzY)**

The clock is ticking. The White House has officially set a March 1st deadline for the Digital Asset Market Clarity Act (CLARITY Act), ...

📺 Discover Crypto

👁️ 3K • 👍 275 • 💬 24 • ⏱️ 1:01:02 • 1h ago

---

**[Billionaire Investor Reveals Why Bitcoin Keeps Dropping | Mike Novogratz](https://www.youtube.com/watch?v=AIJezYSx0NU)**

Mike Novogratz is a veteran macro investor and the founder & CEO of Galaxy. This conversation was recorded live at Bitcoin ...

📺 Anthony Pompliano

👁️ 59K • 👍 2K • 💬 101 • ⏱️ 28:28 • 1d ago

---

**[Why BlackRock Can&#39;t Destroy Bitcoin | Jack Mallers EXCLUSIVE](https://www.youtube.com/watch?v=tMzcG8T-4_4)**

Is Bitcoin being hijacked by Wall Street or is that the point? This conversation cuts through the noise on BlackRock, institutions, ...

📺 Simply Bitcoin

👁️ 19K • 👍 1K • 💬 95 • ⏱️ 13:18 • 19h ago

---

**[BITCOIN HOLDERS... YOU NEED TO SEE THIS CHART](https://www.youtube.com/watch?v=FVYPL5Y_tt0)**

I AM NOT A FINANCIAL ADVISOR. ALL VIDEOS IS FOR ENTERTAINTMENT PURPOSE; AND I AM DOCUMENTING MY OWN ...

📺 Satoshi Stacker

👁️ 8K • 👍 492 • 💬 40 • ⏱️ 13:06 • 9h ago

---

**[BITCOIN: MOST WILL MISS IT!!! #BTC Price Prediction &amp; Crypto Crash News Today](https://www.youtube.com/watch?v=p1KmGNZW05s)**

My Free Trading Course https://www.rt1m.com/free My Discord Server (FREE) https://discord.com/invite/jRAnCV9CTB ...

📺 Road To $1 Million USD

👁️ 3K • 👍 202 • 💬 21 • ⏱️ 5:51 • 19h ago

---

**[Bitcoin Bull Trap to $71k?!](https://www.youtube.com/watch?v=P8LTLf7Nhks)**

Bitcoin is flashing short-term signs of life, and while the broader structure remains clearly bearish, there are legitimate reasons for ...

📺 Coin Bureau Trading

👁️ 4K • 👍 301 • 💬 16 • ⏱️ 13:24 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
