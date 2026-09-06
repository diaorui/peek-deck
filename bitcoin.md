---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-09-06T22:44:19.770008+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- cryptocurrency
- social
- videos
- news
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** September 06, 2026 at 22:44 UTC  
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

### $79,862.14

---

## Bitcoin Chart

**24h:** +0.2%  
**7d:** +1.8%  
**30d:** +23.1%  
**90d:** +29.6%  
**1y:** -28.3%  

---

## Bitcoin Market Stats

**Market Cap:** $1605.76B
Rank #1

**Circulating Supply:** 20,080,684 BTC
95.6% of max

**All-Time High:** $126,080.00
-36.6%

**All-Time Low:** $67.81
+117820.7%

---

## Fear & Greed Index

### 73
**GREED**

---

## Reddit: r/Bitcoin

**[Liquid Network appears to have been stalled for 5 hours and had 4,000 BTC moved without authorization.](https://www.reddit.com/r/Bitcoin/comments/1w95fvr/liquid_network_appears_to_have_been_stalled_for_5/)**

Explore the full Bitcoin ecosystem with The Mempool Open Source Project®. See Liquid transactions & assets, get network info, and more.

🔗 [liquid.network](https://liquid.network/) • 3h ago

---

**[10 Years Ago Bitcoin Was $610. Where Will It Be in 2036?](https://www.reddit.com/r/Bitcoin/comments/1w90yqo/10_years_ago_bitcoin_was_610_where_will_it_be_in/)**

10 years ago today, Bitcoin was ~$610. Nobody knew if it would survive. Today, it’s ~$80,000. Now imagine someone posting this on September 6, 2036: “Bitcoin was only $80K back in 2026.” What do you think the number will be? $100K? $500K? $1M? $5M? RemindMe! 10 years. 👀

6h ago

---

**[🏃💨](https://www.reddit.com/r/Bitcoin/comments/1w8jtmd/_/)**

20h ago

---

**[Zoom out](https://www.reddit.com/r/Bitcoin/comments/1w91y9j/zoom_out/)**

https://preview.redd.it/1zj50nwenxnh1.png?width=601&format=png&auto=webp&s=18a1918f44db55255417c1d6c6bbb3694ed277ed Bitcoin is going to $1M. Don't be sidelined because you tried to time the exact bottom.

5h ago

---

**[Anyone else just here for gains and not de-centralization?](https://www.reddit.com/r/Bitcoin/comments/1w917l0/anyone_else_just_here_for_gains_and_not/)**

I do not care about self-custody (dangerous, so I use Fidelity custody) or censor-less transactions (I live in the U.S. and can trade freely)

5h ago

---

**[Ancient Bitcoin Wallet That Turned $120 Into $3 Million Wakes Up](https://www.reddit.com/r/Bitcoin/comments/1w8c39u/ancient_bitcoin_wallet_that_turned_120_into_3/)**

The parade of long-dormant Bitcoin wallets springing back to life is showing no signs of slowing, with at least four more now stirring.

🔗 [Decrypt](https://decrypt.co/377510/ancient-bitcoin-wallet-3-million-wakes-up) • 1d ago

---

**[Uk folks, which banks are letting us buy/transfer cash to exchanges?](https://www.reddit.com/r/Bitcoin/comments/1w938rn/uk_folks_which_banks_are_letting_us_buytransfer/)**

Not had my Halifax/Lloyds account too long so I’ve not tried to buy any btc yet. Are they safe to move cash to an exchange or do I need to look at a secondary bank account to build up my crypto loses? Ta.

4h ago

---

**[Made a Bitcoin monitoring app with some extra Claude tokens](https://www.reddit.com/r/Bitcoin/comments/1w91j6k/made_a_bitcoin_monitoring_app_with_some_extra/)**

I had some extra tokens at the end of one of my reset periods and decided to build a fun little hackermans Bitcoin site. A couple cool things on there: A calculator if you want to do dynamic DCA - you can see at what risk metric you'd be buying and selling and tweak the settings to your liking. Based on the daily budget you provide it, it'll give you the $ amount to buy (I've actually been using this as a guide to my DCAs) A space battle visualization of the bitcoin price with buys and sells Some other cool visualizations of nodes, blocks, fair market value, and many more things https://preview.redd.it/0mxwxpl6kxnh1.png?width=1708&format=png&auto=webp&s=c9461b8ea37720220f452436d134f6d531fb8e84 There are a lot of fun themes built in as well, let me know if you have some ideas for things that can be added! Just a project for fun and wanted to share! https://www.bitcoinradar.io

5h ago

---

**[Cold Card incident animation I made for this sub](https://www.reddit.com/r/Bitcoin/comments/1w8lb1u/cold_card_incident_animation_i_made_for_this_sub/)**

18h ago

---

**[I reconstructed the Coldcard RNG losses on-chain and it came out a lot bigger than the public numbers (2,052 seeds, 35,189 drained addresses)](https://www.reddit.com/r/Bitcoin/comments/1w91wk3/i_reconstructed_the_coldcard_rng_losses_onchain/)**

So I spent the last few weeks digging into the Coldcard RNG bug on-chain, and the numbers came out worse than what's been reported so far. Background for anyone who missed it: a batch of firmware shipped with the hardware RNG switched off for seed generation (the MICROPY_HW_ENABLE_RNG=0 thing). So instead of the real TRNG, seeds were coming out of a small software PRNG, and the actual entropy was only around 19 to 20 bits. That is crackable on a single GPU. I brute-forced the affected seeds up to the practical ceiling, roughly 2,052 wallets, and from those derived 35,189 unique addresses that are all drained now. That is about 5 times what the address-list writeups found, because I went after the change and deeper derivation addresses too, not just the final sweep everyone screenshots. Then I pulled the full transaction graph to tell apart internal change-cycling from money that actually left. Net theft comes to roughly 5,080 BTC, about 406 million dollars at today's price. The gross figure, meaning everything that ever passed through the bad keys, is around 10,950 BTC, but that is not the loss, a lot of it is just change bouncing around between the attacker's own addresses. Two things worth flagging. Following the money forward, something like 2,918 BTC is still sitting on-chain and could in principle be frozen, and about 991 BTC made it to exchanges. And the sweeper is still running: the most recent automated drain I could find was on 2026-08-19, and it has been going since at least April 2024, so well over two years before this ever became public. What I am not posting: the recovered seed phrases, the PRNG constants, the exact brute-force parameters, or anyone's name. The first would just hand copycats a way to hit wallets that are not drained yet, and the blame question is for proper investigators, not a reddit thread. The full writeup (English and Russian), the victim address list and the hub map are in a repo. I will put the link in a comment instead of the post so it does not get auto-removed. If anyone wants to dig into how the net-versus-gross split or the derivation was done, I am around in the comments. Mikhail, independent security researcher. Telegram MadMike178, email izautrin at gmail dot com.

5h ago

---

---

## Google News: "bitcoin"

**[Bitcoin Slips Below $80,000 After Jobs Data. 2 Things That Could Power Cryptos Higher.](https://www.barrons.com/articles/bitcoin-price-crypto-5ac5ccf8)**

Barron's • 2d ago

---

**[Mexican Rock Star and Family Murdered Over $1.5M Bitcoin Wallet](https://news.bitcoin.com/security/mexican-rock-star-and-family-murdered-over-1-5m-bitcoin-wallet/)**

Discover the chilling details surrounding the murders linked to Jonathan Meléndez and his Bitcoin holdings in Mexico.

Bitcoin News • 3h ago

---

**[Remember How Bitcoin Was Supposed to Rise With Money Supply? Here's Why That Didn't Happen](https://finance.yahoo.com/markets/crypto/articles/remember-bitcoin-supposed-rise-money-170010779.html)**

Cryptocurrency analyst Benjamin Cowen on Wednesday argued that unlike commonly assumed, Bitcoin does not rise with M2 money supply, which explains weakness against equities. Global Net Liquidity Explains Bitcoin’s Five-Year Lag Cowen detailed on his podcast how rising M2 does...

Yahoo Finance • 5h ago

---

**[‘Like Buying Bitcoin In 2013’—Tiny Crypto Suddenly Rockets 7,300% As Massive $100 Billion Price Boom Predicted](https://www.forbes.com/sites/digital-assets/2026/09/06/like-buying-bitcoin-in-2013-tiny-crypto-suddenly-rockets-7300-as-massive-zcash-price-boom-predicted/)**

Forbes • 10h ago

---

**[Bitcoin mining data center condemned after leaking 3 million gallons of water and forcing school closures — facility operated for years under a city stop-work order](https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order)**

Oklahoma, El Reno city asserts that none of the costs related to the water leak at the property will be passed on to citizens.

Tom's Hardware • 8h ago

---

**[How bitcoin's sudden explosive price spikes make market timing practically impossible for crypto traders](https://www.coindesk.com/markets/2026/09/05/why-crypto-experts-say-buying-and-holding-bitcoin-easily-beats-trying-to-time-the-market)**

CoinDesk • 1d ago

---

**[Fed Governor Waller just reignited the bitcoin debasement trade: Chart of the Day](https://finance.yahoo.com/markets/article/fed-governor-waller-just-reignited-the-bitcoin-debasement-trade-chart-of-the-day-100000584.html)**

Bitcoin is back at the Rubicon —and Fed governor Waller just dared bulls to cross it.

Yahoo Finance • 2d ago

---

**[Bitcoin heads for third winning week in a row as macro pressures mount](https://www.cnbc.com/2026/09/04/bitcoin-heads-for-third-winning-week-in-a-row-as-macro-pressures-mount.html)**

Bitcoin headed for its third straight winning week, as traders searched for refuge amid volatile moves in equities, currencies and bond markets.

CNBC • 2d ago

---

**[Bitcoin down but holds near $80,000 as corporate buying, U.S. crypto vote in focus](https://www.investing.com/news/cryptocurrency-news/bitcoin-trades-near-80000-as-corporate-demand-and-us-crypto-policy-stay-in-focus-4890272)**

Investing.com • 11h ago

---

**[$14.5 Billion Injection: Will U.S. Treasury Trigger 'Round 2' for Bitcoin and XRP?](https://www.tradingview.com/news/u_today:ba16f95cd094b:0-14-5-billion-injection-will-u-s-treasury-trigger-round-2-for-bitcoin-and-xrp/)**

The U.S. Treasury Department will enter the active phase of its government debt buyback program on Monday, Sept. 7, 2026. The weekly limit on operations will amount to $14.5 billion, while the maximum volume of Treasury sessions could reach $16.5 billion.Such a large liquidity injection has sparked…

tradingview.com • 9h ago

---

---

## HackerNews: "bitcoin"

**[The first AI-run ransomware attack copied its Bitcoin address out of a tutorial](https://news.ycombinator.com/item?id=49589728)**

The thing that gets me isn’t that it worked. It’s that it worked while being this dumb.

⬆️ 5 • 💬 0 • 3h ago • [Medium](https://medium.com/@thenewgencoder/the-first-fully-ai-run-ransomware-attack-copied-its-bitcoin-address-out-of-a-tutorial-a630ee3224dc)

---

**[Bitcoin mining data center condemned after leaking 3M gallons of water](https://news.ycombinator.com/item?id=49588413)**

Oklahoma, El Reno city asserts that none of the costs related to the water leak at the property will be passed on to citizens.

⬆️ 4 • 💬 0 • 5h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order)

---

**[Goodbye Bitcoin, Hello AI Data Center](https://news.ycombinator.com/item?id=49536515)**

Hyperscale Data has ended all Bitcoin mining at its Michigan data center and started converting the site into artificial intelligence computing capacity for a contracted customer, the company said September 2. The Las Vegas-based company, which trades on the NYSE

⬆️ 4 • 💬 0 • 4d ago • [American Buildout](https://americanbuildout.com/goodbye-bitcoin-hello-ai-data-center/)

---

**[The Liquid Network (Bitcoin sidechain) is stuck at block 4050335](https://news.ycombinator.com/item?id=49587562)**

Explore the full Bitcoin ecosystem with The Mempool Open Source Project®. See Liquid transactions & assets, get network info, and more.

⬆️ 3 • 💬 0 • 7h ago • [liquid.network](https://liquid.network/es/block/aad24e4fb64ca8adf4961667da87820cd48e553957ac64e75de7cdb298b5d66b)

---

**[Bitcoinica](https://news.ycombinator.com/item?id=49558143)**

⬆️ 2 • 💬 1 • 3d ago • [en.bitcoin.it](https://en.bitcoin.it/wiki/Bitcoinica)

---

**[Generating Bitcoin wallet seed phrases from playing cards](https://news.ycombinator.com/item?id=49519790)**

COLDCARD users lost 1,700 BTC to weak randomness. How to generate a BIP39 seed phrase from a shuffled deck of playing cards on an air-gapped Raspberry Pi.

⬆️ 2 • 💬 0 • 5d ago • [Andreas Brekken](https://brekken.com/posts/a-truly-random-seed-phrase)

---

**[From Bitcoin Bankruptcy to Data Center Billions in West Texas](https://news.ycombinator.com/item?id=49548221)**

Ionic Digital is leasing one of its West Texas sites to an AI infrastructure operator because the most valuable part of the bitcoin mine is not the building or the mining machines. It is the electricity.  The site is already

⬆️ 1 • 💬 0 • 3d ago • [American Buildout](https://americanbuildout.com/from-bitcoin-bankruptcy-to-data-center-billions-in-west-texas/)

---

**[White House Launches Arcade.Gov](https://news.ycombinator.com/item?id=49570467)**

Donald Trump's White House has launched Arcade.Gov, a site with mini-games where you catch and deport immigrants, or use Tetris blocks to build a border wall.

⬆️ 17 • 💬 2 • 2d ago • [IGN](https://www.ign.com/articles/white-house-launches-arcadegov-a-minigame-site-where-you-catch-immigrants-build-a-tetris-border-wall-and-fill-your-kids-trump-accounts-with-bitcoin)

---

**[Launch HN: RonanRX (YC S26) – Personalized Peptides and GLP-1s](https://news.ycombinator.com/item?id=49543530)**

⬆️ 118 • 💬 82 • 4d ago

---

---

## YouTube Videos: "bitcoin"

**[Bitcoin&#39;s &quot;Referee&quot; Status Between Crypto &amp; U.S. Policy, Volatility Ticks Down](https://www.youtube.com/watch?v=Y9Y1e2v6sR4)**

Sam Callahan, director of Bitcoin strategy at OranjeBTC, explains his take on the cryptocurrency's resurgence as it crosses back ...

📺 Schwab Network

👁️ 5K • 👍 46 • 💬 29 • ⏱️ 10:28 • 5h ago

---

**[I’m Not Buying Bitcoin At $80k. Here’s Why....](https://www.youtube.com/watch?v=RNiYDUAsvvg)**

Is the Bitcoin bull market really back? Bitcoin is at $80000, above the bull market support band and the 200-week moving average ...

📺 Crypto Banter

👁️ 21K • 👍 378 • 💬 32 • ⏱️ 23:36 • 1d ago

---

**[Bitcoin Is Entering Its Most Powerful Wave Ever](https://www.youtube.com/watch?v=5UhtaqWLSG0)**

Jordi Visser (@JordiVisserLabs) is a veteran macro investor with 30+ years of experience and the author of the VisserLabs ...

📺 Anthony Pompliano

👁️ 179K • 👍 3K • 💬 142 • ⏱️ 55:09 • 1d ago

---

**[Bitcoin &amp; Crypto Are About To Make People VERY Rich You Cannot Afford To Miss This News](https://www.youtube.com/watch?v=4nh2LyrTT-s)**

Who could have ever imagined that governments and central banks buying up Bitcoin and altcoins would cause more rich people ...

📺 Money Rules - Investing Tips 

👁️ 18K • 👍 1K • 💬 375 • ⏱️ 18:30 • 11h ago

---

**[Bitcoin’s $82K Breakout Just Got REKT by the Fed!](https://www.youtube.com/watch?v=gOuhLyaGotA)**

Bitcoin just posted its highest close in four months, up nearly $20000 in 20 days, and triggered one of the largest short liquidation ...

📺 Simply Bitcoin

👁️ 39K • 👍 2K • 💬 97 • ⏱️ 14:58 • 1d ago

---

**[Bitcoin has 3 Possible Paths from here](https://www.youtube.com/watch?v=MK47H-8RTBo)**

Bitcoin has 3 possible paths from here 2 Bearish & one Bullish count Yellow squiggle still in play TA & Live Trades Get the CF ...

📺 Camel Finance

👁️ 15K • 👍 637 • 💬 122 • ⏱️ 17:23 • 1d ago

---

**[Ben Cowen: Most Accurate Trader In Crypto Flips On Bitcoin](https://www.youtube.com/watch?v=SzQFdsWTJec)**

Ben Cowen called last year's cycle top almost to the week, live on this show. Now he puts a hard number on the bottom.

📺 Kyle Chasse crypto

👁️ 84K • 👍 2K • 💬 314 • ⏱️ 57:03 • 2d ago

---

**[Will Bitcoin Hit $150K This Year?](https://www.youtube.com/watch?v=6HSNPJVbJRc)**

A GIANT STORM Is About To Hit Crypto ⛈️ ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily 50% deposit bonus ...

📺 Altcoin Daily

👁️ 19K • 👍 361 • 💬 10 • ⏱️ 1:09 • 2d ago

---

**[WTF JUST HAPPENED TO BITCOIN??????! (URGENT ZCASH WARNING)](https://www.youtube.com/watch?v=XDW_YmphzVI)**

TRADE PERPS IN THE USA: https://kalshi.com/p/cryptokid $25 BONUS WEEX: https://cryptokid.io/WEEX-Bonus ...

📺 Crypto Kid

👁️ 9K • 👍 368 • 💬 59 • ⏱️ 12:17 • 14h ago

---

**[Bitcoin At A Major Decision Point | BTC Price Analysis](https://www.youtube.com/watch?v=pX8y4khTsBs)**

See Our ETH + COIN Analysis: https://www.wickedstocks.com/ Bitcoin continues to test an important technical level. Cary breaks ...

📺 Wicked Stocks

👁️ 945 • 👍 44 • 💬 2 • ⏱️ 3:49 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
