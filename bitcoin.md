---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-05-29T17:33:44.339984+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- videos
- social
- news
- cryptocurrency
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** May 29, 2026 at 17:33 UTC  
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

### $74,254.87

---

## Bitcoin Chart

**24h:** +0.7%  
**7d:** -3.3%  
**30d:** -2.7%  
**90d:** +13.0%  
**1y:** -28.6%  

---

## Bitcoin Market Stats

**Market Cap:** $1485.30B
Rank #1

**Circulating Supply:** 20,036,203 BTC
95.4% of max

**All-Time High:** $126,080.00
-41.2%

**All-Time Low:** $67.81
+109262.9%

---

## Fear & Greed Index

### 23
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[Texas Names Bitcoin Reserve Advisory Committee As State Eyes Direct Bitcoin Custody](https://www.reddit.com/r/Bitcoin/comments/1tr4rzs/texas_names_bitcoin_reserve_advisory_committee_as/)**

Texas has appointed a five-member advisory committee to oversee its Strategic Bitcoin Reserve as the state prepares to transition from ETF exposure to directly custodied bitcoin.

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/texas-names-bitcoin-reserve-committee) • 2h ago

---

**[Self-Custody: Convenience vs Security](https://www.reddit.com/r/Bitcoin/comments/1tr01ms/selfcustody_convenience_vs_security/)**

A lot of people assume self-custody means making everything way more complicated. But honestly, once you use COLDCARD, you realize a secure setup can still be pretty straightforward. It meets Bitcoiners wherever they’re at, whether you just want to safely hodl long term or you’re into using multisig, and advanced setups. Feels like the “secure vs easy” tradeoff isn’t necessary.

5h ago

---

**[Anonymous Plaintiff Seeks Legal Title To $293 Billion In Dormant Bitcoin, Without Holding Any Private Keys](https://www.reddit.com/r/Bitcoin/comments/1tqgtc9/anonymous_plaintiff_seeks_legal_title_to_293/)**

A pseudonymous claimant, “Noah Doe,” alongside two Wyoming LLCs, has filed a lawsuit in New York Supreme Court seeking recognition as the rightful owner of 39,069 dormant Bitcoin addresses containing roughly 3.8 million BTC—valued at about $293 billion.

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/anonymous-plaintiff-seeks-legal-bitcoin) • 20h ago

---

**[Collision Protocol: 1000 BTC Challenge Pool (#135, 13.5 BTC)](https://www.reddit.com/r/Bitcoin/comments/1tr2yh1/collision_protocol_1000_btc_challenge_pool_135/)**

Quick background if you have not run into it: the 1000 BTC Challenge is an on-chain puzzle from 2015. Someone funded 160 addresses whose private keys sit in deliberately increasing ranges (key N is between 2N-1 and 2N), and in 2023 the prizes were bumped 10x. The low ones have been picked off over the years; the unsolved ones still hold real coins. #135 is the current target and holds 13.5 BTC. Tracker: https://privatekeys.pw/puzzles/bitcoin-puzzle-tx Collision Protocol is a distributed Pollard's Kangaroo pool that points a fleet of GPUs at one unsolved key at a time. It's on #135 right now and stays on it until it's solved. When that happens the pool doesn't stop: it automatically rolls the whole fleet to the next key most likely to fall (the lowest unsolved range whose public key is exposed, which is what Kangaroo needs). Nothing for you to reconfigure, your worker just follows the pool. Each worker only runs one side of the walk, tame or wild, and sends its distinguished points (DPs) to the server. That split is the anti-cheat: no single machine ever has both halves, so nobody can quietly hit the collision, recover the key, and sweep the coins before the pool does. The upside for you is the payout. Since the solve can only land at the pool, every DP you commit counts toward your share. If the pool cracks the key, the prize is split by contribution: a 5% pool fee, and everything left over distributed in proportion to the verified DPs each worker submitted. Rough scale: RCKangaroo's own estimate for a 2134 range is 1.15 * 267 operations, which at dp_bits 28 is about 6 * 1011 DPs to expect a solve. That is an expectation: a real solve can land anywhere from about half to double that, and DP/GPU overhead pushes the true count up somewhat. Expected time against the pool's aggregate rate: pool DP/s expected solve time, #135 100 ~200 years 1,000 ~20 years 10,000 ~2 years 100,000 ~2.5 months 1,000,000 ~7 days We are at single digits per second today on a couple of test rigs, and the bottom rows of that table are a serious amount of hardware, so this is mostly a question of how many GPUs show up. Rate scales linearly with workers. Open to testers who get that it's early and rough in places, and who will open a GitHub issue when something breaks instead of just walking away. Mainly after Linux and Apple Silicon right now. Client (collider) is open, GPLv3, built on JeanLucPons' RCKangaroo: https://github.com/hevnsnt/collider Issues: https://github.com/hevnsnt/collider/issues Live coverage/stats: https://collisionprotocol.com/pool collider --pool pool.collisionprotocol.com:17403 --worker <btc-payout-address> Worker name is the payout address (So get it right!). The pool tells the client which target, range, and DP size to work, so the same client follows whatever key is active. CUDA on Win/Linux, Metal on Apple Silicon, CPU fallback. What's useful to report: whether it builds and runs on your platform, the rates you get, and anything that breaks or drops the connection. Source is there if you want to pull it apart. collider-pro is a separate paid build for solo and brainwallet work. Not needed for the pool.

3h ago

---

**[BlackRock Clients Sold 0.3% of Their Bitcoin Holdings Yesterday Why the Panic is a Massive Overreaction](https://www.reddit.com/r/Bitcoin/comments/1tr52w9/blackrock_clients_sold_03_of_their_bitcoin/)**

Yesterday's institutional outflow data showed BlackRock's IBIT shedding roughly 2,424 BTC (around $178M). Most mainstream headlines are immediately reading this as a bearish signal, but digging into the raw numbers tells a completely different story. ​Context matters, and BlackRock’s total Bitcoin exposure is still absolutely massive: ​IBIT still holds roughly 792,000 BTC (valued at over $57B). ​The amount sold yesterday represents a mere 0.3% of their total Bitcoin holdings. ​This doesn’t look like a conviction exit or institutional capitulation at all. It looks closer to routine, microscopic portfolio rebalancing or short-term de-risking during broader macro volatility. ​Furthermore, when you look at how BlackRock manages its digital asset products, they maintain a clear divide. While liquidity is occasionally shuffled in alternative crypto products and risk-on tech assets, their core Bitcoin thesis remains incredibly sticky. The institutional giant hasn't even scratched the surface of its primary BTC reserves. ​It feels like the broader market saw a "millions sold" headline and completely ignored the scale of the actual positions. A 0.3% fluctuation is noise, not a trend shift. ​Do you see this as meaningful institutional de-risking, or is it mostly routine portfolio management that the retail market is completely overreacting to

2h ago

---

**[CLN DoS vulnerability, CoreDev meeting - Bitcoin Optech Newsletter #407](https://www.reddit.com/r/Bitcoin/comments/1tqy5ms/cln_dos_vulnerability_coredev_meeting_bitcoin/)**

Bitcoin Optech newsletter #407 is here: - announces the responsible disclosure of a vulnerability that allowed a remote peer to crash Core Lightning nodes - links to transcripts from a recent Bitcoin Core developer meeting - Optech Newsletter #407 Podcast https://bitcoinops.org/en/newsletters/2026/05/29/ Chandra Pratap posted to Delving Bitcoin disclosing a denial-of-service vulnerability discovered during a Summer of Bitcoin 2025 internship... https://bitcoinops.org/en/newsletters/2026/05/29/#core-lightning-assertion-dos-disclosure Many Bitcoin Core developers met in person in May, and transcripts from the meeting have been published... https://bitcoinops.org/en/newsletters/2026/05/29/#bitcoin-core-developer-meeting-transcripts Bitcoin Optech will host an audio recap discussion of this newsletter streaming live on X/Twitter Tuesday at 16:30 UTC.

🔗 [Bitcoin Optech](https://bitcoinops.org/en/newsletters/2026/05/29/) • 6h ago

---

**[Best crypto card in 2026 for actually using my holdings?](https://www.reddit.com/r/Bitcoin/comments/1tqtgz7/best_crypto_card_in_2026_for_actually_using_my/)**

I’ve been holding crypto since 2021, mostly BTC, but honestly I’m getting tired of just letting it sit there. Every time I want to actually use it, it feels like a whole process. Move funds to an exchange, convert to fiat, deal with fees, wait for withdrawals, then finally spend it. At that point it barely feels convenient anymore. I’m starting to look into crypto cards because some of them now claim you can spend BTC directly at normal merchants. Some even say you can connect an external wallet and use it anywhere Visa or Mastercard is accepted, which sounds good if the fees aren’t terrible.

10h ago

---

**[I ran Bitcoin miners for two years. Here's what it actually taught me.](https://www.reddit.com/r/Bitcoin/comments/1tq2v7z/i_ran_bitcoin_miners_for_two_years_heres_what_it/)**

Started in 2023. Bought ASICs thinking I'd build a side income for my family. Ended up with 9 ASICs and 3 GPU rigs running in my basement. Sounded like a beehive down there. Eventually moved to immersion cooling just to keep the peace at home. Something happened while i was trying to make the operation profitable. I started learning what Bitcoin actually is. Not the price. The blockchain. The supply cap. Why it exists. I was already feeling the weight of the fiat system in my own life. Bitcoin started making sense in a way it never had when I was just holding it on an exchange. Mining killed my price anxiety. When you understand how blocks get produced, how difficulty adjusts, the number on the screen stops feeling like a verdict. Its just where the market is today. We shut down in late 2025. Electricity made it unprofitable. Felt like relief and loss at the same time. That operation brought me most of the Bitcoin I own. I'll get back into it someday. Anyone else come through mining? Curious how many people's conviction got built the same way.

1d ago

---

**[Daily Discussion, May 29, 2026](https://www.reddit.com/r/Bitcoin/comments/1tqsptv/daily_discussion_may_29_2026/)**

Please utilize this sticky thread for all general Bitcoin discussions! If you see posts on the front page or /r/Bitcoin/new which are better suited for this daily discussion thread, please help out by directing the OP to this thread instead. Thank you! If you don't get an answer to your question, you can try phrasing it differently or commenting again tomorrow. Please check the previous discussion thread for unanswered questions.

11h ago

---

**[Mining plan for free electricity](https://www.reddit.com/r/Bitcoin/comments/1tqrupt/mining_plan_for_free_electricity/)**

My solar panels create more electricity than I can use, what is a good suggestion for a setup for mining when electricity is free?

12h ago

---

---

## Google News: "bitcoin"

**[Q-Day could destroy bitcoin – and our retirement savings](https://www.newscientist.com/article/2528342-q-day-could-destroy-bitcoin-and-our-retirement-savings/)**

Even if you’ve never bought any cryptocurrency, like columnist Karmela Padavic-Callaghan, your money may be affected by bitcoin’s fate – which is uncertain, as quantum computing advances are threatening to make the encryption protecting it useless

New Scientist • 9h ago

---

**[Calamos bets protected Bitcoin ETFs can outlast crypto market swings](https://www.coindesk.com/coindesk-news/2026/05/28/calamos-bets-protected-bitcoin-etfs-can-outlast-crypto-market-swings)**

As more than $1 billion exited spot Bitcoin ETFs last week, Calamos says investors are rotating into Bitcoin products with built-in downside protection.

CoinDesk • 19h ago

---

**[Bitcoin Rises While Trump Weighs Iran Deal, But The Bigger Question Is Whether It’s Becoming Digital Gold](https://finance.yahoo.com/markets/crypto/articles/bitcoin-rises-while-trump-weighs-164547362.html)**

Bitcoin rallied toward $74,000 after Donald Trump headed to the Situation Room for a final Iran decision, as analysts noted BTC is acting like digital gold.

Yahoo Finance • 47m ago

---

**[Bitcoin Rallied 146% After Strategy’s First Purchase and 57% After ETF Launch. Could State Reserves Push BTC Past Its ATH?](https://finance.yahoo.com/markets/crypto/articles/bitcoin-rallied-146-strategy-first-171805110.html)**

More than 26 U.S. states have introduced legislation to add Bitcoin (CRYPTO: BTC) and digital assets to their state treasury reserves, with New Hampshire, Arizona, and Texas being the first to sign these bills into law. The bills vary in size and structure, but most propose allocating somewhere between 5% and 10% of state funds ... Bitcoin Rallied 146% After Strategy’s First Purchase and 57% After ETF Launch. Could State Reserves Push BTC Past Its ATH?

Yahoo Finance • 15m ago

---

**[US Bitcoin ETFs Bleed $2.8 Billion in Longest Outflow Streak](https://www.bloomberg.com/news/articles/2026-05-29/us-bitcoin-btc-etfs-bleed-2-8-billion-in-longest-outflow-streak)**

Investors pulled money from US spot-Bitcoin exchange-traded funds for a ninth straight session, the longest run of withdrawals since the products debuted, underscoring a cooling in demand for the largest cryptocurrency even as broader risk assets rally.

Bloomberg • 10h ago

---

**[Bitcoin Slumps, But Strategy Isn't Buying. Here's Why.](https://www.investors.com/news/bitcoin-price-slumps-strategy-buying-power-strc-mstr-stock/)**

Investor's Business Daily • 6h ago

---

**[Bitcoin mining company plans large-scale data center in eastern Kentucky](https://www.wkyt.com/2026/05/26/bitcoin-mining-company-plans-large-scale-data-center-eastern-kentucky/)**

TeraWulf announced it is expanding in eastern Kentucky with the purchase of a new high-performance computing development site called the Muskie Data Campus.

WKYT • 2d ago

---

**[Is Bitcoin Dead? Here Are 3 Reasons It Might Be.](https://www.fool.com/investing/2026/05/29/is-bitcoin-dead-here-are-3-reasons-why-it-might-be/)**

Is this the end of the show for Bitcoin, or just an awkward intermission between acts?

The Motley Fool • 8h ago

---

**[JPMorgan says bitcoin and gold ETF outflows point to 'cooling' debasement trade amid hopes for Iran-US deal](https://www.theblock.co/post/402888/jpmorgan-bitcoin-gold-etf-outflows-cooling-debasement-trade-hopes-iran-us-deal)**

Both bitcoin and gold ETFs have seen outflows over the past two weeks as the debasement trade cools, according to JPMorgan analysts.

The Block • 1d ago

---

**[CFTC Approves Bitcoin Perpetual Futures on Prediction Market Kalshi](https://decrypt.co/369465/cftc-approves-bitcoin-perpetual-futures-kalshi)**

The CFTC issued an order allowing Kalshi to offer perpetual futures in the U.S., starting with contracts tied to Bitcoin's price.

Decrypt • 2h ago

---

---

## HackerNews: "bitcoin"

**[Matching Hashes: Reproducing the Guix-Built Bitcoin Core Release Binary with Nix](https://news.ycombinator.com/item?id=48296063)**

Earlier this week, I produced a Nix-built bitcoind binary for Bitcoin Core v31.0 whose hash exactly matches the official Guix-built x86_64-pc-linux-gnu release binary. The result came out of a three year old side project, with a difficult goal: Can a binary built with Nix be made bit-for-bit identical to one produced by Bitcoin Core’s Guix reproducible build system?

⬆️ 32 • 💬 0 • 2d ago • [b10c's blog](https://b10c.me/projects/027-bitcoind-gunix-match/)

---

**[Billionaire Mark Cuban says bye-bye Bitcoin: Why he is 'disappointed' by crypto](https://news.ycombinator.com/item?id=48289056)**

‘It’s not the hedge that I expected it to be,’ Cuban said

⬆️ 7 • 💬 2 • 2d ago • [Fortune](https://fortune.com/2026/05/26/mark-cuban-bitcoin-disappointed-crypto/)

---

**[Mined in America Act Would Put Bitcoin Network at Risk](https://news.ycombinator.com/item?id=48288300)**

The bill would effectively turn miners into their own surveillance teams, collecting and reporting information to the government in exchange for economic favoritism.

⬆️ 6 • 💬 0 • 2d ago • [The Rage](https://www.therage.co/mined-in-america-act-bitcoin-at-risk/)

---

**[Kinetik – Hear the Bitcoin Market](https://news.ycombinator.com/item?id=48309376)**

Live Bitcoin trades turned into music and motion in real time. Sound on.

⬆️ 2 • 💬 1 • 1d ago • [Kinetik](https://kinetik.coexinbrand.com/)

---

**[RawBit – Visual Bitcoin raw tx builder](https://news.ycombinator.com/item?id=48292709)**

⬆️ 2 • 💬 1 • 2d ago • [rawbit.io](https://rawbit.io)

---

**[Why Would Someone Publicly Burn $8M Worth of Bitcoin?](https://news.ycombinator.com/item?id=48321858)**

⬆️ 2 • 💬 0 • 5h ago • [gizmodo.com](https://gizmodo.com/why-would-someone-publicly-burn-8-million-worth-of-bitcoin-theories-are-flying-2000764705)

---

**[Elon Musk's SpaceX Has More Bitcoin Than Estimated, SEC Filing Shows [video]](https://news.ycombinator.com/item?id=48294364)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 2 • 💬 0 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=bs2cEzpvaow)

---

**[Hacker who sold access to Oregon state emergency network for Bitcoin gets prison](https://news.ycombinator.com/item?id=48290641)**

⬆️ 2 • 💬 0 • 2d ago • [oregonlive.com](https://www.oregonlive.com/crime/2026/05/hacker-who-sold-access-to-oregon-state-emergency-network-for-bitcoin-gets-prison.html)

---

**[The Bitcoin Governance Event Horizon](https://news.ycombinator.com/item?id=48243791)**

⬆️ 2 • 💬 0 • 6d ago • [earthchronicles.substack.com](https://earthchronicles.substack.com/p/the-bitcoin-governance-event-horizon)

---

**[Banca Sella Becomes First Italian Bank Licensed for Bitcoin and Crypto Services](https://news.ycombinator.com/item?id=48295331)**

Banca Sella has become the first Italian bank to receive authorization to offer cryptocurrency services under the European Union’s Markets in Crypto-Assets

⬆️ 1 • 💬 0 • 2d ago • [Italy](https://www.europesays.com/italy/20070/)

---

---

## YouTube Videos: "bitcoin"

**[Bitcoin is Getting CRUSHED By Everything — Here&#39;s Why!](https://www.youtube.com/watch?v=bgjbSsGRk0E)**

Bitcoin is underperforming stocks, gold, silver, AI, and almost every major asset on the board in 2026, but that may be the clearest ...

📺 Simply Bitcoin

👁️ 35K • 👍 2K • 💬 399 • ⏱️ 15:50 • 20h ago

---

**[The Last 4 Times This Happened Bitcoin Went CRAZY. It Just Happened Again.](https://www.youtube.com/watch?v=1giUPFyt__0)**

Buy, Sell, Trade Crypto: Weex ($100k Trading Giveaway): https://www.weex.com/events/promo/spot-contest?vipCode=oz5p ...

📺 Altcoin Daily

👁️ 37K • 👍 2K • 💬 259 • ⏱️ 10:19 • 1d ago

---

**[Bitcoin Next Move is Massive (Get Ready)](https://www.youtube.com/watch?v=bZ0l2OKMewQ)**

Your AI Platform for Crypto, Markets, and Sports ▻ https://www.askclash.ai/ **Exchange Partners** Bitunix Exchange ...

📺 CryptosRUs

👁️ 8K • 👍 655 • 💬 115 • ⏱️ 55:21 • 2h ago

---

**[The Government is About to Print $1 Trillion to Buy Bitcoin](https://www.youtube.com/watch?v=74dO0cTMUZc)**

Get my free newsletter Letters From a Heretic: https://go.heresy.financial/letters-from-a-heretic TIMECODES 00:00 The ...

📺 Heresy Financial

👁️ 79K • 👍 3K • 💬 784 • ⏱️ 17:21 • 1d ago

---

**[Bitcoin Is The Only Asset That Survives What’s Coming](https://www.youtube.com/watch?v=hBEQhSxQYtI)**

Jan van Eck is the CEO of VanEck, a $200 billion asset manager and one of the leading ETF companies in the world. In this ...

📺 Anthony Pompliano

👁️ 27K • 👍 991 • 💬 40 • ⏱️ 59:08 • 1d ago

---

**[Bitcoin Falls Below The Bear Market Resistance Band](https://www.youtube.com/watch?v=slTIiS-Y65k)**

In today's video, we discuss Bitcoin falling back below the Bear Market Resistance Band and what this could mean for the broader ...

📺 Benjamin Cowen

👁️ 71K • 👍 5K • 💬 264 • ⏱️ 18:38 • 1d ago

---

**[ANONYMOUS WHALE IS Using BlackRocks ETF To CRASH Bitcoins Price... | EP 1514](https://www.youtube.com/watch?v=0W201pEdMz4)**

Huge IBIT shadow block tanks bitcoin price - are they trying to suppress bitcoins price?

📺 Simply Bitcoin

👁️ 6K • 👍 328 • 💬 60 • ⏱️ 1:36:37 • 22h ago

---

**[Crypto Crash To LAST LINE Of Support! (Waited 13 Days For This)](https://www.youtube.com/watch?v=s8rLXMVvT0s)**

My Links: ▻ Get the risk models I use to track accumulation and exit zones. Free trial https://app.cryptocapitalventure.ai Intro ...

📺 Crypto Capital Venture

👁️ 10K • 👍 574 • 💬 454 • ⏱️ 15:40 • 1d ago

---

**[Don’t Make This Crypto Mistake | Raoul Pal The Journey Man](https://www.youtube.com/watch?v=YNfWRnp0ATc)**

In this solo presentation, Raoul Pal explains why crypto is a long-term network adoption story, how liquidity and the business cycle ...

📺 Raoul Pal The Journey Man

👁️ 56K • 👍 3K • 💬 507 • ⏱️ 48:46 • 1d ago

---

**[Bitcoin: The Window of Weakness](https://www.youtube.com/watch?v=dIa8HUYDNEY)**

Bitcoin has entered what many traders call the "Window of Weakness"—a period where seasonal trends, market psychology, and ...

📺 Benjamin Cowen

👁️ 44K • 👍 3K • 💬 141 • ⏱️ 23:28 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
