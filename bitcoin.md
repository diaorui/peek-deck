---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-02-20T19:37:00.652405+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- cryptocurrency
- videos
- social
- news
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** February 20, 2026 at 19:37 UTC  
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

### $67,561.92

---

## Bitcoin Chart

**24h:** +1.2%  
**7d:** -2.8%  
**30d:** -24.2%  
**90d:** -22.0%  
**1y:** -29.5%  

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

7h ago

---

**[Power Law model shows BTC at $68k is deep in the buy zone (13.7%)](https://www.reddit.com/r/Bitcoin/comments/1ra0vwj/power_law_model_shows_btc_at_68k_is_deep_in_the/)**

Been tracking the Bitcoin Power Law model for a while now. Here's this week's update. BTC is sitting at $67,745. Power Law fair value is around $123,947 — about 45% below fair value. Oscillator reads 13.7% The oscillator has ticked up marginally from 13.6% to 13.7%, remaining firmly entrenched in the Deep Buy Zone (0–25%). This is historically rare territory that typically occurs only 1–2 times per halving cycle. The oscillator's EMA(150) at 31.2% remains below its EMA(350) at 37.7%, maintaining a bearish spread of -6.5 points. This configuration — deep value combined with bearish momentum — represents the model's maximum accumulation signal. Full breakdown with charts here if anyone's interested: https://timetobuybitcoin.com/analysis/maximum-accumulation-zone-deepens-oscillator-at-137-amid-his-2026-02-20 Not financial advice, just sharing the data. Curious what you guys think.

2h ago

---

**[Something is changing in this Bitcoin cycle. Our Lightning data since 2022 suggests it.](https://www.reddit.com/r/Bitcoin/comments/1r9w97t/something_is_changing_in_this_bitcoin_cycle_our/)**

We have accepted Bitcoin Lightning since May 2022. This downturn is fundamentally different from previous cycles. In the past, both transaction count and total volume dropped. This time, they have not. Why?

5h ago

---

**[What does Bitcoin look like in 20 years if adoption keeps growing?](https://www.reddit.com/r/Bitcoin/comments/1r9rnci/what_does_bitcoin_look_like_in_20_years_if/)**

I’ve been thinking less about short-term price lately and more about what Bitcoin could actually look like 10–20 years from now. Not in terms of “how high does it go,” but in terms of real usage. Like… what happens if adoption just keeps growing? More people self-custodying instead of leaving coins on exchanges. More businesses accepting BTC directly. Cross-border payments without needing banks in the middle. People choosing to save in something with a fixed supply instead of constantly inflating currencies. At some point, if that trend continues, Bitcoin stops being seen as just a speculative asset and starts looking more like infrastructure. A base layer. A monetary network that people actually rely on. And historically, when a new monetary network gains critical mass, the people who paid attention early weren’t just “lucky.” They understood what was happening before it became obvious to everyone else. So for me the real question isn’t will price go up. It’s what happens if a censorship resistant, fixed-supply asset just keeps gaining adoption globally. Curious how others here think about the 10–20 year outlook, purely from a network and usage perspective.

9h ago

---

**[Today My Family Got off Zero & Joined the .1 club🚀](https://www.reddit.com/r/Bitcoin/comments/1r9hwmw/today_my_family_got_off_zero_joined_the_1_club/)**

I don’t care if it dips more…. We just had to get in with that tax return. I’d rather it dip to 50k & miss out on those small amounts of BTC than have it rip to 100k or beyond tomorrow and live with the regret that I’ll never see BTC that low ever again! Tonight is the first night I can rest peacefully knowing my family is hedged against the decaying dollar and positioned to benefit from deflation from government inflation. The last one using the dollar gets stuck holding the bag of poverty. Not this family🙏🏼🚀

18h ago

---

**[We're searching for Bitcoin wallets generated with weak entropy from 2009-2012 — here's what early wallet software got wrong](https://www.reddit.com/r/Bitcoin/comments/1r9xxr0/were_searching_for_bitcoin_wallets_generated_with/)**

Between 2009 and 2012, Bitcoin wallet software was experimental. Many early tools used predictable random number generators to create private keys: - Debian OpenSSL bug (CVE-2008-0166) — A catastrophic bug shipped in 2008 reduced all randomness to just the process ID. Only 65,536 possible private keys. Any wallet generated on Debian/Ubuntu during that period is trivially crackable. - Timestamp-seeded LCGs — glibc and MSVC srand(time(NULL)) followed by rand() to generate each byte of the private key. The entire search space is just ~62.8 million seeds (one per second from genesis to early 2011). - Randstorm (V8 MWC1616) — BitcoinJS and other web-based wallets relied on Chrome's Math.random(), which used a weak PRNG before 2013. Disclosed by Unciphered in 2023, this affected wallets created through browser interfaces. - Brain wallets — SHA256("password"), SHA256("1"), SHA256("12345") — people actually did this, and the keys are still sitting on-chain. - Java LCG — Early Android wallets (BitcoinJ) seeded java.util.Random with millisecond timestamps. There are roughly 2,845 known funded addresses believed to have been created by these weak methods. We built a distributed GPU project to systematically search through all 23 weak key patterns. The pipeline runs entirely on CUDA — each GPU thread generates a private key using the weak algorithm, does the full secp256k1 multiplication, SHA-256, RIPEMD-160, and checks against all target addresses via a bloom filter. An RTX 3090 tests ~130 million keys per second. The small keyspaces are already exhausted (Debian OpenSSL was done in milliseconds). We're currently grinding through SHA-256 of sequential integers — a 2^64 keyspace that will take sustained GPU power. How rewards work if a wallet is found: - 70% distributed to GPU contributors based on verified compute time - 20% to platform development and infrastructure - 10% donated to medical research Website with live stats and the full technical writeup: https://b4q.io Curious if anyone here remembers using any of these early wallet tools. Some of these bugs were well-known at the time but the affected addresses are still funded years later.

4h ago

---

**[Fear and Greed Index](https://www.reddit.com/r/Bitcoin/comments/1r9lbwo/fear_and_greed_index/)**

The fear-and-greed index is in a state of sustained extreme fear. This has historically signaled the bottom of a cycle. I don't think the index alone is a good barometer for trading, but it's hard to ignore when it's pegged to extreme fear for weeks or months. I'm buying - we'll see how that works out. ;)

15h ago

---

**[Bitcoin doesn't give a duck about you](https://www.reddit.com/r/Bitcoin/comments/1r9b1pc/bitcoin_doesnt_give_a_duck_about_you/)**

22h ago

---

**[Bitcoin historical return calculator (lump sum + DCA)](https://www.reddit.com/r/Bitcoin/comments/1r9zy1g/bitcoin_historical_return_calculator_lump_sum_dca/)**

Made a simple BTC calculator that charts historical returns over time. It supports recurring buys or one time investments. You can change: Amount Start date Contribution schedule (one time, monthly, yearly, etc) It’s mainly to visualize how different entry points and recurring buys play out across cycles.

🔗 [WhatIfInvest](https://www.whatifinvest.com/calculators/BTC_USD) • 3h ago

---

**[These Finnish homes are being heated by a surprising source: Bitcoin](https://www.reddit.com/r/Bitcoin/comments/1r9rqi9/these_finnish_homes_are_being_heated_by_a/)**

Heating homes with Bitcoin obviously isn't a surprise to this sub. What's surprising is the website, publishing the article - Grist. Their about us page says: Grist is a nonprofit, independent media organization dedicated to reporting on climate change. Since 1999, we have used the power of journalism to engage the public about the perils of one of the most existential threats we face. We seek to document the often unequal impacts of climate change on communities in the United States and globally — as well as to show the promise of equitable climate solutions. With 40 journalists spread across nearly 20 U.S. states, Grist is the largest and most experienced climate-focused newsroom in the country. Our work aims to illustrate how the effects of a warming planet intersect with, well, everything.... https://grist.org/about/

🔗 [Grist](https://grist.org/buildings/bitcoin-cryptocurrency-district-heat-finland/) • 9h ago

---

---

## Google News: "bitcoin"

**[Eric Trump shrugs off bitcoin's recent slump: 'If you don't have the backbone ... go invest in some boring bond'](https://finance.yahoo.com/news/eric-trump-shrugs-off-bitcoins-recent-slump-if-you-dont-have-the-backbone--go-invest-in-some-boring-bond-193400545.html)**

During a wide-ranging interview with Yahoo Finance, Eric Trump weighed in on bitcoin, crypto legislation, his personal debanking experience, and the latest digital asset project between the Trump Organization and his flagship crypto venture, World Liberty Financial.

Yahoo Finance • 1d ago

---

**[When Bitcoin prices turned against Michael Saylor, he quietly pivoted to a risky financial gambit at Strategy](https://fortune.com/2026/02/20/michael-saylor-bitcoin-prices-preferred-shares-dilution-strategy/)**

Saylor has been offseting the Bitcoin drag by reverting to different and dangerous scheme: Issuing tons of preferred stock.

Fortune • 10h ago

---

**[Bitcoin vs. Ethereum: Which Is the Smarter Buy for 2026 and Beyond?](https://www.fool.com/investing/2026/02/20/bitcoin-vs-ethereum-which-is-the-smarter-buy-for-2/)**

The world's two largest cryptocurrencies lost their luster over the past year.

The Motley Fool • 3h ago

---

**[Bitcoin Pops After Supreme Court Strikes Down Trump’s Tariffs](https://bitcoinmagazine.com/news/bitcoin-pops-after-supreme-court)**

The Supreme Court on Friday struck down Trump’s global tariffs, ruling 6-3 that he exceeded his emergency powers.

Bitcoin Magazine • 2h ago

---

**[Bitcoin braces for final capitulation amid rising geopolitical risks](https://www.kitco.com/opinion/2026-02-20/bitcoin-braces-final-capitulation-amid-rising-geopolitical-risks)**

The Kitco News Team brings you the latest news, videos, analysis and opinions regarding Precious Metals, Crypto, Mining, World Markets and Global Economy.

KITCO • 3h ago

---

**[Bitcoin Trapped in Fragile Trading as Hedge Funds Pivot to Cash](https://www.bloomberg.com/news/articles/2026-02-19/bitcoin-settles-in-trading-range-while-hedge-funds-pivot-to-cash)**

Bloomberg • 21h ago

---

**[Bitcoin Won Over Wall Street and Now It’s Paying the Price](https://finance.yahoo.com/news/bitcoin-won-over-wall-street-124511013.html)**

Since Oct. 10, roughly $8.5 billion has flowed out of US-listed spot Bitcoin exchange-traded funds.  Futures exposure on the Chicago Mercantile Exchange has fallen by about two-thirds from its late-2024 peak to roughly $8 billion.  Prices on Coinbase, the venue favored by many American institutions, have persistently traded at a discount to offshore exchange Binance — a signal of sustained US selling.

Yahoo Finance • 2d ago

---

**[Bitcoin Price Falls to $68,000. Why Ethereum, XRP Are Struggling to Find Direction.](https://www.barrons.com/articles/bitcoin-price-xrp-ether-cryptos-ai-tech-stocks-5e824042?gaa_at=eafs&gaa_n=AWEtsqcSFZW5c1qPi4TdjEOZw3OiQA7sHD5JonVLIccUYUZGuXBCvRZY2K3k&gaa_ts=6998b09c&gaa_sig=IbS3_8hcX8ViFZefPVRrVlzqhWFStNZNTxwh7xInc3KvWTCy0z9OJPUAJ5xl7LGX1sQj14uszHe_qnw28GVuRA%3D%3D)**

Barron's • 2d ago

---

**[Clarity Act Odds Briefly Spike; Bitcoin Miner Tumbles On AI Funding Plans](https://www.investors.com/news/clarity-act-odds-spike-stablecoin-discussions-white-house-bitdeer-funds-ai-data-center/)**

Investor's Business Daily • 22h ago

---

**[Bitcoin remains below key onchain level as ETF outflows persist, liquidity stays tight: analysts](https://www.theblock.co/post/390602/bitcoin-remains-below-key-onchain-level-as-etf-outflows-persist-liquidity-stays-tight-analysts)**

Analysts warned that weak ETF flows, constrained liquidity, and fragile accumulation are keeping bitcoin's price rangebound and indecisive.

The Block • 7h ago

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

**[Bitfarms shares surge ditching its 'Bitcoin' identity and doubling down on AI](https://news.ycombinator.com/item?id=47091742)**

The company said it will focus on building data centers for high-performance computing and artificial-intelligence workloads.

⬆️ 1 • 💬 0 • 1h ago • [coindesk.com](https://www.coindesk.com/business/2026/02/06/bitfarms-says-it-s-no-longer-a-bitcoin-company-doubling-down-on-ai-with-u-s-move)

---

**[Professional Bitcoin Asset Tracing – Intelligence Cyber Wizard](https://news.ycombinator.com/item?id=47086751)**

⬆️ 1 • 💬 0 • 7h ago

---

**[Fire calculator that takes Bitcoin holdings into account](https://news.ycombinator.com/item?id=47075139)**

Financial independence on a bitcoin standard

⬆️ 1 • 💬 0 • 1d ago • [FIRE BTC](https://calc.firebtc.io/)

---

**[Show HN: Natural language search across Kalshi and Polymarket](https://news.ycombinator.com/item?id=47088680)**

Fast natural language search across 60,000+ prediction markets on Kalshi and Polymarket. Sports, crypto, weather, politics and more.

⬆️ 1 • 💬 0 • 4h ago • [Attena](https://www.attena.xyz/)

---

**[Regulated Crypto Investigation Team – Intelligence Cyber Wizard Services](https://news.ycombinator.com/item?id=47085488)**

⬆️ 1 • 💬 0 • 10h ago

---

---

## YouTube Videos: "bitcoin"

**[Trump Is About To Unleash A Massive SHOCK To The Bitcoin Price | Larry Lepard](https://www.youtube.com/watch?v=R1RgSzYtHg8)**

Watch The FULL Interview: https://www.youtube.com/watch?v=-i8humbpZJQ FREE Daily On-Chain Analysis & Crypto News In ...

📺 Library Of Wealth

👁️ 4K • 👍 240 • 💬 74 • ⏱️ 14:04 • 14h ago

---

**[BITCOIN REVERSAL IMMINENT — IT&#39;S HAPPENING NOW!](https://www.youtube.com/watch?v=B_6KEvI4cB0)**

https://youtu.be/RThI3UUSpwc?si=t0m9cQVPXyt35ZMD BUY ONE 1-STEP CHALLENGE → GET ...

📺 100XClub

👁️ 7K • 👍 876 • 💬 272 • ⏱️ 9:49 • 9h ago

---

**[Bitcoin’s “Final” Warning: The 7-Day Countdown](https://www.youtube.com/watch?v=kwWrreTKJmA)**

Aliens, Bitcoin, Tesla, and altcoin updates as Clarity Act looms. BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 10K • 👍 613 • 💬 86 • ⏱️ 17:34 • 8h ago

---

**[IS BITCOIN ACTUALLY DEAD??!!](https://www.youtube.com/watch?v=-itjlUK81JA)**

Join The Community: https://bit.ly/FefeCommunity FOLLOW FEFE FOR THE BEST ALPHA ...

📺 100XClub

👁️ 2K • 👍 182 • 💬 61 • ⏱️ 1:35 • 4h ago

---

**[🚨 BREAKING: Trump’s Global Tariffs DENIED!](https://www.youtube.com/watch?v=C-xzZJYNVzY)**

The clock is ticking. The White House has officially set a March 1st deadline for the Digital Asset Market Clarity Act (CLARITY Act), ...

📺 Discover Crypto

👁️ 3K • 👍 275 • 💬 24 • ⏱️ 1:01:02 • 3h ago

---

**[Billionaire Investor Reveals Why Bitcoin Keeps Dropping | Mike Novogratz](https://www.youtube.com/watch?v=AIJezYSx0NU)**

Mike Novogratz is a veteran macro investor and the founder & CEO of Galaxy. This conversation was recorded live at Bitcoin ...

📺 Anthony Pompliano

👁️ 59K • 👍 2K • 💬 101 • ⏱️ 28:28 • 1d ago

---

**[Why BlackRock Can&#39;t Destroy Bitcoin | Jack Mallers EXCLUSIVE](https://www.youtube.com/watch?v=tMzcG8T-4_4)**

Is Bitcoin being hijacked by Wall Street or is that the point? This conversation cuts through the noise on BlackRock, institutions, ...

📺 Simply Bitcoin

👁️ 19K • 👍 1K • 💬 95 • ⏱️ 13:18 • 21h ago

---

**[BITCOIN HOLDERS... YOU NEED TO SEE THIS CHART](https://www.youtube.com/watch?v=FVYPL5Y_tt0)**

I AM NOT A FINANCIAL ADVISOR. ALL VIDEOS IS FOR ENTERTAINTMENT PURPOSE; AND I AM DOCUMENTING MY OWN ...

📺 Satoshi Stacker

👁️ 8K • 👍 492 • 💬 40 • ⏱️ 13:06 • 11h ago

---

**[BITCOIN: MOST WILL MISS IT!!! #BTC Price Prediction &amp; Crypto Crash News Today](https://www.youtube.com/watch?v=p1KmGNZW05s)**

My Free Trading Course https://www.rt1m.com/free My Discord Server (FREE) https://discord.com/invite/jRAnCV9CTB ...

📺 Road To $1 Million USD

👁️ 3K • 👍 202 • 💬 21 • ⏱️ 5:51 • 20h ago

---

**[Bitcoin Bull Trap to $71k?!](https://www.youtube.com/watch?v=P8LTLf7Nhks)**

Bitcoin is flashing short-term signs of life, and while the broader structure remains clearly bearish, there are legitimate reasons for ...

📺 Coin Bureau Trading

👁️ 4K • 👍 301 • 💬 16 • ⏱️ 13:24 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
