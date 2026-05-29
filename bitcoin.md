---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-05-29T20:26:36.800177+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- videos
- cryptocurrency
- social
- news
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** May 29, 2026 at 20:26 UTC  
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

### $73,683.34

---

## Bitcoin Chart

**24h:** -0.2%  
**7d:** -4.0%  
**30d:** -3.4%  
**90d:** +12.2%  
**1y:** -29.2%  

---

## Bitcoin Market Stats

**Market Cap:** $1473.92B
Rank #1

**Circulating Supply:** 20,036,240 BTC
95.4% of max

**All-Time High:** $126,080.00
-41.6%

**All-Time Low:** $67.81
+108454.8%

---

## Fear & Greed Index

### 23
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[Texas Names Bitcoin Reserve Advisory Committee As State Eyes Direct Bitcoin Custody](https://www.reddit.com/r/Bitcoin/comments/1tr4rzs/texas_names_bitcoin_reserve_advisory_committee_as/)**

Texas has appointed a five-member advisory committee to oversee its Strategic Bitcoin Reserve as the state prepares to transition from ETF exposure to directly custodied bitcoin.

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/texas-names-bitcoin-reserve-committee) • 5h ago

---

**[I knew better. I still sold near the bottom.](https://www.reddit.com/r/Bitcoin/comments/1tradf3/i_knew_better_i_still_sold_near_the_bottom/)**

When FTX collapsed, I genuinely thought Bitcoin might be finished. Not just another bear market. I mean finished. Regulation, contagion, trust destroyed. I sold most of my position somewhere around $16k telling myself I was being rational. Six months later I was buying back above $25k. The thing that bothers me most isn't the money. It's that I'd already lived through 2018. I knew what capitulation felt like. I'd read everything about not timing the market, about conviction, about long-term thinking. And when the moment came, none of it mattered. The fear was louder. What I've accepted since then is that understanding Bitcoin intellectually and actually holding through chaos are two completely different skills. One you develop reading. The other you only develop by getting it wrong a few times. I'm not sure conviction is something you build in advance. I think you find out if you have it when the moment is bad enough.Anyone else discover that knowing what to do and actually doing it are completely different things? Did the second cycle feel any easier?

2h ago

---

**[Self-Custody: Convenience vs Security](https://www.reddit.com/r/Bitcoin/comments/1tr01ms/selfcustody_convenience_vs_security/)**

A lot of people assume self-custody means making everything way more complicated. But honestly, once you use COLDCARD, you realize a secure setup can still be pretty straightforward. It meets Bitcoiners wherever they’re at, whether you just want to safely hodl long term or you’re into using multisig, and advanced setups. Feels like the “secure vs easy” tradeoff isn’t necessary.

8h ago

---

**[Bitcoin is the Honey Badger](https://www.reddit.com/r/Bitcoin/comments/1trcdzo/bitcoin_is_the_honey_badger/)**

https://www.reddit.com/r/interestingasfuck/s/Os1oXr9RKZ

1h ago

---

**[Bitcars.](https://www.reddit.com/r/Bitcoin/comments/1tr3oog/bitcars/)**

Not sure which one I’d rather own. They both come with advantages and disadvantages.

5h ago

---

**[Collision Protocol: 1000 BTC Challenge Pool (#135, 13.5 BTC)](https://www.reddit.com/r/Bitcoin/comments/1tr2yh1/collision_protocol_1000_btc_challenge_pool_135/)**

Quick background if you have not run into it: the 1000 BTC Challenge is an on-chain puzzle from 2015. Someone funded 160 addresses whose private keys sit in deliberately increasing ranges (key N is between 2N-1 and 2N), and in 2023 the prizes were bumped 10x. The low ones have been picked off over the years; the unsolved ones still hold real coins. #135 is the current target and holds 13.5 BTC. Tracker: https://privatekeys.pw/puzzles/bitcoin-puzzle-tx Collision Protocol is a distributed Pollard's Kangaroo pool that points a fleet of GPUs at one unsolved key at a time. It's on #135 right now and stays on it until it's solved. When that happens the pool doesn't stop: it automatically rolls the whole fleet to the next key most likely to fall (the lowest unsolved range whose public key is exposed, which is what Kangaroo needs). Nothing for you to reconfigure, your worker just follows the pool. Each worker only runs one side of the walk, tame or wild, and sends its distinguished points (DPs) to the server. That split is the anti-cheat: no single machine ever has both halves, so nobody can quietly hit the collision, recover the key, and sweep the coins before the pool does. The upside for you is the payout. Since the solve can only land at the pool, every DP you commit counts toward your share. If the pool cracks the key, the prize is split by contribution: a 5% pool fee, and everything left over distributed in proportion to the verified DPs each worker submitted. Rough scale: RCKangaroo's own estimate for a 2134 range is 1.15 * 267 operations, which at dp_bits 28 is about 6 * 1011 DPs to expect a solve. That is an expectation: a real solve can land anywhere from about half to double that, and DP/GPU overhead pushes the true count up somewhat. Expected time against the pool's aggregate rate: pool DP/s expected solve time, #135 100 ~200 years 1,000 ~20 years 10,000 ~2 years 100,000 ~2.5 months 1,000,000 ~7 days We are at single digits per second today on a couple of test rigs, and the bottom rows of that table are a serious amount of hardware, so this is mostly a question of how many GPUs show up. Rate scales linearly with workers. Open to testers who get that it's early and rough in places, and who will open a GitHub issue when something breaks instead of just walking away. Mainly after Linux and Apple Silicon right now. Client (collider) is open, GPLv3, built on JeanLucPons' RCKangaroo: https://github.com/hevnsnt/collider Issues: https://github.com/hevnsnt/collider/issues Live coverage/stats: https://collisionprotocol.com/pool collider --pool pool.collisionprotocol.com:17403 --worker <btc-payout-address> Worker name is the payout address (So get it right!). The pool tells the client which target, range, and DP size to work, so the same client follows whatever key is active. CUDA on Win/Linux, Metal on Apple Silicon, CPU fallback. What's useful to report: whether it builds and runs on your platform, the rates you get, and anything that breaks or drops the connection. Source is there if you want to pull it apart. collider-pro is a separate paid build for solo and brainwallet work. Not needed for the pool.

6h ago

---

**[BlackRock Clients Sold 0.3% of Their Bitcoin Holdings Yesterday Why the Panic is a Massive Overreaction](https://www.reddit.com/r/Bitcoin/comments/1tr52w9/blackrock_clients_sold_03_of_their_bitcoin/)**

Yesterday's institutional outflow data showed BlackRock's IBIT shedding roughly 2,424 BTC (around $178M). Most mainstream headlines are immediately reading this as a bearish signal, but digging into the raw numbers tells a completely different story. ​Context matters, and BlackRock’s total Bitcoin exposure is still absolutely massive: ​IBIT still holds roughly 792,000 BTC (valued at over $57B). ​The amount sold yesterday represents a mere 0.3% of their total Bitcoin holdings. ​This doesn’t look like a conviction exit or institutional capitulation at all. It looks closer to routine, microscopic portfolio rebalancing or short-term de-risking during broader macro volatility. ​Furthermore, when you look at how BlackRock manages its digital asset products, they maintain a clear divide. While liquidity is occasionally shuffled in alternative crypto products and risk-on tech assets, their core Bitcoin thesis remains incredibly sticky. The institutional giant hasn't even scratched the surface of its primary BTC reserves. ​It feels like the broader market saw a "millions sold" headline and completely ignored the scale of the actual positions. A 0.3% fluctuation is noise, not a trend shift. ​Do you see this as meaningful institutional de-risking, or is it mostly routine portfolio management that the retail market is completely overreacting to

5h ago

---

**[Anonymous Plaintiff Seeks Legal Title To $293 Billion In Dormant Bitcoin, Without Holding Any Private Keys](https://www.reddit.com/r/Bitcoin/comments/1tqgtc9/anonymous_plaintiff_seeks_legal_title_to_293/)**

A pseudonymous claimant, “Noah Doe,” alongside two Wyoming LLCs, has filed a lawsuit in New York Supreme Court seeking recognition as the rightful owner of 39,069 dormant Bitcoin addresses containing roughly 3.8 million BTC—valued at about $293 billion.

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/anonymous-plaintiff-seeks-legal-bitcoin) • 23h ago

---

**[Unexpected dump?](https://www.reddit.com/r/Bitcoin/comments/1tr3o71/unexpected_dump/)**

I know we're still in the bear market, but timewise this is quite an unexpected dump in the last days, right? 12% in the last 2 weeks. No real macro indicators, positive news on war, stocks are flying worldwide. Is everyone fleeing into stocks? BTC too risky all of a sudden?

5h ago

---

**[Best crypto card in 2026 for actually using my holdings?](https://www.reddit.com/r/Bitcoin/comments/1tqtgz7/best_crypto_card_in_2026_for_actually_using_my/)**

I’ve been holding crypto since 2021, mostly BTC, but honestly I’m getting tired of just letting it sit there. Every time I want to actually use it, it feels like a whole process. Move funds to an exchange, convert to fiat, deal with fees, wait for withdrawals, then finally spend it. At that point it barely feels convenient anymore. I’m starting to look into crypto cards because some of them now claim you can spend BTC directly at normal merchants. Some even say you can connect an external wallet and use it anywhere Visa or Mastercard is accepted, which sounds good if the fees aren’t terrible.

13h ago

---

---

## Google News: "bitcoin"

**[Robinhood stock is surging — and bitcoin isn't the reason this time](https://finance.yahoo.com/markets/article/robinhood-stock-is-surging--and-bitcoin-isnt-the-reason-this-time-152104398.html)**

Robinhood's AI-agent rollout is giving investors a new reason to buy the stock — and crypto is not part of it.

Yahoo Finance • 2h ago

---

**[Q-Day could destroy bitcoin – and our retirement savings](https://www.newscientist.com/article/2528342-q-day-could-destroy-bitcoin-and-our-retirement-savings/)**

Even if you’ve never bought any cryptocurrency, like columnist Karmela Padavic-Callaghan, your money may be affected by bitcoin’s fate – which is uncertain, as quantum computing advances are threatening to make the encryption protecting it useless

New Scientist • 12h ago

---

**[Bitcoin price news: BTC off the lows on Trump post, but set to close month of May with losses](https://www.coindesk.com/markets/2026/05/29/live-markets-bitcoin-slides-further-putting-two-month-winning-streak-in-jeopardy)**

A hopeful posting on Iran from President Trump helped erase morning losses.

CoinDesk • 4h ago

---

**[US Bitcoin ETFs Bleed $2.8 Billion in Longest Outflow Streak](https://www.bloomberg.com/news/articles/2026-05-29/us-bitcoin-btc-etfs-bleed-2-8-billion-in-longest-outflow-streak)**

Investors pulled money from US spot-Bitcoin exchange-traded funds for a ninth straight session, the longest run of withdrawals since the products debuted, underscoring a cooling in demand for the largest cryptocurrency even as broader risk assets rally.

Bloomberg.com • 13h ago

---

**[Bitcoin, XRP Prices Slump as U.S., Iran Tensions Hit Cryptos](https://www.barrons.com/articles/bitcoin-xrp-ethereum-cryptos-today-d588a761)**

Barron's • 1d ago

---

**[Bitcoin Slumps, But Strategy Isn't Buying. Here's Why.](https://www.investors.com/news/bitcoin-price-slumps-strategy-buying-power-strc-mstr-stock/)**

Investor's Business Daily • 8h ago

---

**[Bitcoin mining company plans large-scale data center in eastern Kentucky](https://www.wkyt.com/2026/05/26/bitcoin-mining-company-plans-large-scale-data-center-eastern-kentucky/)**

TeraWulf announced it is expanding in eastern Kentucky with the purchase of a new high-performance computing development site called the Muskie Data Campus.

WKYT • 3d ago

---

**[JPMorgan says bitcoin and gold ETF outflows point to 'cooling' debasement trade amid hopes for Iran-US deal](https://www.theblock.co/post/402888/jpmorgan-bitcoin-gold-etf-outflows-cooling-debasement-trade-hopes-iran-us-deal)**

Both bitcoin and gold ETFs have seen outflows over the past two weeks as the debasement trade cools, according to JPMorgan analysts.

The Block • 1d ago

---

**[HIVE Digital Technologies: From Bitcoin Miner To AI Infrastructure (NASDAQ:HIVE)](https://seekingalpha.com/article/4909938-hive-digital-technologies-from-bitcoin-miner-to-ai-infrastructure)**

HIVE Digital Technologies is rapidly transitioning from a renewable bitcoin miner to an AI infrastructure leader. Read more on HIVE stock here.

Seeking Alpha • 12h ago

---

**[‘They’re Going To Print An Insane Amount’—U.S. Dollar Collapse Predicted To Spark A $1 Million Bitcoin Price Boom](https://www.forbes.com/sites/digital-assets/2026/05/29/theyre-going-to-print-an-insane-amount-us-dollar-collapse-predicted-to-spark-a-1-million-bitcoin-price-boom/)**

A closely-watched bitcoin bull has outlined how U.S. dollar debasement could power a bitcoin price surge to $1 million...

Forbes • 7h ago

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

**[Why Would Someone Publicly Burn $8M Worth of Bitcoin?](https://news.ycombinator.com/item?id=48321858)**

⬆️ 3 • 💬 0 • 8h ago • [gizmodo.com](https://gizmodo.com/why-would-someone-publicly-burn-8-million-worth-of-bitcoin-theories-are-flying-2000764705)

---

**[Kinetik – Hear the Bitcoin Market](https://news.ycombinator.com/item?id=48309376)**

Live Bitcoin trades turned into music and motion in real time. Sound on.

⬆️ 2 • 💬 1 • 1d ago • [Kinetik](https://kinetik.coexinbrand.com/)

---

**[RawBit – Visual Bitcoin raw tx builder](https://news.ycombinator.com/item?id=48292709)**

⬆️ 2 • 💬 1 • 2d ago • [rawbit.io](https://rawbit.io)

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

👁️ 37K • 👍 2K • 💬 397 • ⏱️ 15:50 • 23h ago

---

**[The Last 4 Times This Happened Bitcoin Went CRAZY. It Just Happened Again.](https://www.youtube.com/watch?v=1giUPFyt__0)**

Buy, Sell, Trade Crypto: Weex ($100k Trading Giveaway): https://www.weex.com/events/promo/spot-contest?vipCode=oz5p ...

📺 Altcoin Daily

👁️ 38K • 👍 2K • 💬 257 • ⏱️ 10:19 • 1d ago

---

**[Bitcoin Next Move is Massive (Get Ready)](https://www.youtube.com/watch?v=bZ0l2OKMewQ)**

Your AI Platform for Crypto, Markets, and Sports ▻ https://www.askclash.ai/ **Exchange Partners** Bitunix Exchange ...

📺 CryptosRUs

👁️ 12K • 👍 734 • 💬 139 • ⏱️ 55:21 • 5h ago

---

**[The Government is About to Print $1 Trillion to Buy Bitcoin](https://www.youtube.com/watch?v=74dO0cTMUZc)**

Get my free newsletter Letters From a Heretic: https://go.heresy.financial/letters-from-a-heretic TIMECODES 00:00 The ...

📺 Heresy Financial

👁️ 82K • 👍 3K • 💬 790 • ⏱️ 17:21 • 1d ago

---

**[Bitcoin Won&#39;t 100x Anymore – Anthony Pompliano](https://www.youtube.com/watch?v=7-6GWQXmfSc)**

Live from Consensus Miami! Ran Neuner sits down with Anthony Pompliano for a massive crypto market breakdown. Is the 4-year ...

📺 Crypto Banter

👁️ 2K • 👍 32 • 💬 2 • ⏱️ 0:54 • 7h ago

---

**[Bitcoin Is The Only Asset That Survives What’s Coming](https://www.youtube.com/watch?v=hBEQhSxQYtI)**

Jan van Eck is the CEO of VanEck, a $200 billion asset manager and one of the leading ETF companies in the world. In this ...

📺 Anthony Pompliano

👁️ 28K • 👍 1K • 💬 40 • ⏱️ 59:08 • 1d ago

---

**[Bitcoin Bull Saylor To DUMP $30M Today?](https://www.youtube.com/watch?v=jV8AFe2kF7o)**

Bitcoin #Crypto #Finance Bitcoin just cratered to a six week low below $73000 as fresh U.S. airstrikes on Iran reignited Strait of ...

📺 The Wolf Of All Streets

👁️ 10K • 👍 815 • 💬 191 • ⏱️ 22:33 • 6h ago

---

**[Someone BURNED $8 BILLION in Bitcoin | Nobody Believes in BTC Anymore](https://www.youtube.com/watch?v=a9blylvBx1I)**

Comfortable crypto trading with Bybit: https://partner.bybit.com/b/youtbtu ============= All about crypto here: ...

📺 TU Crypto News

👁️ 543 • 👍 2 • ⏱️ 0:30 • 5h ago

---

**[Bitcoin Falls Below The Bear Market Resistance Band](https://www.youtube.com/watch?v=slTIiS-Y65k)**

In today's video, we discuss Bitcoin falling back below the Bear Market Resistance Band and what this could mean for the broader ...

📺 Benjamin Cowen

👁️ 72K • 👍 5K • 💬 264 • ⏱️ 18:38 • 1d ago

---

**[Crypto Crash To LAST LINE Of Support! (Waited 13 Days For This)](https://www.youtube.com/watch?v=s8rLXMVvT0s)**

My Links: ▻ Get the risk models I use to track accumulation and exit zones. Free trial https://app.cryptocapitalventure.ai Intro ...

📺 Crypto Capital Venture

👁️ 10K • 👍 576 • 💬 449 • ⏱️ 15:40 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
