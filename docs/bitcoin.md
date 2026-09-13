---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-09-13T11:13:28.609891+00:00'
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

**Last Updated:** September 13, 2026 at 11:13 UTC  
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

### $76,758.29

---

## Bitcoin Chart

**24h:** -0.9%  
**7d:** -3.2%  
**30d:** +21.4%  
**90d:** +16.7%  
**1y:** -33.7%  

---

## Bitcoin Market Stats

**Market Cap:** $1538.00B
Rank #1

**Circulating Supply:** 20,083,712 BTC
95.6% of max

**All-Time High:** $126,080.00
-39.3%

**All-Time Low:** $67.81
+112834.7%

---

## Fear & Greed Index

### 61
**GREED**

---

## Reddit: r/Bitcoin

**[Bitcoin Renaissance](https://www.reddit.com/r/Bitcoin/comments/1wf32si/bitcoin_renaissance/)**

1h ago

---

**[Lambos are temporary, the dip is forever.](https://www.reddit.com/r/Bitcoin/comments/1weahzr/lambos_are_temporary_the_dip_is_forever/)**

23h ago

---

**[bitcoin shark knows the bottom already happened](https://www.reddit.com/r/Bitcoin/comments/1wedj9f/bitcoin_shark_knows_the_bottom_already_happened/)**

21h ago

---

**[Bitcoin activity, passports exposed after Revolut falls for fake government request](https://www.reddit.com/r/Bitcoin/comments/1wejz8c/bitcoin_activity_passports_exposed_after_revolut/)**

KYC is getting more dangerous by day. Once you'll have enough of this, have a look at BISQ, Robosats, HodlHodl, PeachBitcoin or Vexl instead.

🔗 [coindesk.com](https://www.coindesk.com/tech/2026/09/12/bitcoin-activity-passports-exposed-after-revolut-falls-for-fake-government-request) • 16h ago

---

**[Lock in.](https://www.reddit.com/r/Bitcoin/comments/1wer97v/lock_in/)**

12h ago

---

**[Daily Discussion, September 13, 2026](https://www.reddit.com/r/Bitcoin/comments/1wf0ijh/daily_discussion_september_13_2026/)**

Please utilize this sticky thread for all general Bitcoin discussions! If you see posts on the front page or /r/Bitcoin/new which are better suited for this daily discussion thread, please help out by directing the OP to this thread instead. Thank you! If you don't get an answer to your question, you can try phrasing it differently or commenting again tomorrow. Please check the previous discussion thread for unanswered questions.

4h ago

---

**[case trezor safe 5 print 3D](https://www.reddit.com/r/Bitcoin/comments/1wet2e0/case_trezor_safe_5_print_3d/)**

10h ago

---

**[Clarity act fail](https://www.reddit.com/r/Bitcoin/comments/1wf261u/clarity_act_fail/)**

Clarity act fail How big a pullback do we see if the clarity act doesn’t get voted through ? 10% 20% ? Do you think that would be probably be the last big dip prior to the end of the bear market

2h ago

---

**[Canada just quietly said "yeah tokenized deposits are just deposits" and it's a bigger deal than it sounds](https://www.reddit.com/r/Bitcoin/comments/1wedsbb/canada_just_quietly_said_yeah_tokenized_deposits/)**

Canada's bank regulator (OSFI) just said tokenized deposits are "not legally distinct" from regular bank deposits. translation: banks have wanted to put deposits on-chain for a while now, tech's been ready. the thing actually holding it up was regulators just... never clearly saying what these things legally ARE. no clear answer = no bank touching it, too much legal risk. Canada just removed that excuse. same rules, no new framework, just "this counts as a normal deposit, go ahead." this is the boring-sounding stuff that actually matters, this is a literal door opening for real banks to start building on-chain instead of just talking about it in press releases curious if US/EU regulators follow suit or if Canada's just built different rn.

20h ago

---

**[I built a small BIP-39 checksum device for manually generated entropy](https://www.reddit.com/r/Bitcoin/comments/1wehrvl/i_built_a_small_bip39_checksum_device_for/)**

The idea started from something that bothered me with hardware wallets and other similar devices, and it really sparked during the coldcard mishap (which shows that letting the hw generate the seed for you is not ideal for real cold storage). Dont get me wrong, I still really like the coldcard hw but the reality of things is that software bugs will always be present no matter what. Ledger and Trezor are no exceptions. Of course some hardware wallets allow you to provide your own entropy, for example using dice rolls. This is already much better than blindly trusting an internal rng, but imho there is still one part of the process you have to trust: you cannot usually verify, step by step, that the entropy bits you provided are actually being mapped to the correct BIP-39 words. You provide the entropy, and eventually the wallet shows you a mnemonic. But what happened in between? This device is meant to solve exactly this problem. I made a similar project before this one but the word-building process wasn't fully auditable, Redditors pointed out this problem, which I really appreciated. This device does not generate entropy. You generate it yourself using coin flips or dice rolls. The device only helps you convert that entropy into a BIP-39 mnemonic and calculate the checksum required for the final word. While entering the entropy, the 2x16 LCD shows the current 11-bit group being built. When the 11 bits are complete, it shows the decimal index and the corresponding BIP-39 word. For example, this is the 7th word while being built, with only 5 bits entered so far: +----------------+ |W07 11000______ | |A:H=0 B:T=1 | +----------------+ ...and this is the final result once all 11 bits have been entered: +----------------+ |W07 11000010110 | |1558 security | +----------------+ So you can independently check: 11000010110 -> 1558 -> security against any BIP-39 wordlist, even a wordlist as pdf or txt file on your computer, it doesn't have to be on paper. Indexes are 0-based !!! This happens for every word. The final word is the only special one because part of its 11 bits comes from the SHA-256 checksum. For a 24-word mnemonic, for example: +----------------+ |W24 101|01100110| |1382 <word> | +----------------+ The 101 bits come directly from your entropy, while the remaining 8 bits are the checksum calculated by the device. Unlike the previous project, this one currently supports 12, 18 and 24 word BIP-39 mnemonics, with three entropy input methods: direct coin flips, Von Neumann debiased coin flips, and dice rolls. Von Neumann allows to get statistically fair results from a biased coin (any real word coin is slightly biased of course). The goal is basically to have a very small device where you provide the randomness and you can audit the entropy-to-word conversion while it happens, instead of trusting a hardware wallet to do that part correctly behind the scenes. Project here: https://github.com/gianlucag/LastWord I would really appreciate any feedback, or simply whether you think this approach makes sense

18h ago

---

---

## Google News: "bitcoin"

**[Bitcoin activity, passports exposed after Revolut falls for fake government request](https://www.coindesk.com/tech/2026/09/12/bitcoin-activity-passports-exposed-after-revolut-falls-for-fake-government-request)**

CoinDesk • 1d ago

---

**[White House Issues Serious Crypto Warning—Bitcoin Price On The Brink Of $8 Trillion Shock](https://www.forbes.com/sites/digital-assets/2026/09/12/white-house-issues-serious-crypto-warning-bitcoin-price-on-the-brink-of-8-trillion-shock/)**

Forbes • 23h ago

---

**[MicroStrategy's Bitcoin Guide Issues a 93% Crash Warning to Investors](https://finance.yahoo.com/markets/crypto/articles/microstrategys-bitcoin-guide-issues-93-101501318.html)**

MicroStrategy's Bitcoin guide warns of a 93% crash. Strategy sits just 2% above its own cost on 845,050 BTC.

Yahoo Finance • 58m ago

---

**[22-year-old pleads guilty in $240 million bitcoin heist, one of the largest in US history](https://www.cnn.com/2026/09/09/us/man-pleads-guilty-massive-crypto-heists-hnk)**

A 22-year-old man pleaded guilty on Tuesday to teaming up with friends to steal nearly a quarter-billion dollars in bitcoin from a Washington, DC, resident — one of the largest cryptocurrency thefts in US history — and then embarking on a wild spending spree with the laundered proceeds.

CNN • 3d ago

---

**[Bitcoin is back, but potential Clarity Act fail and Dem midterms win could come for crypto prices](https://www.cnbc.com/2026/09/11/bitcoin-price-crypto-clarity-act-midterms.html)**

Bitcoin's price has been rallying, but it's still down in 2026. Failure of the Clarity Act ahead of Democratic gains in the midterms could be new headwinds.

CNBC • 1d ago

---

**[Bitcoin’s White-Hat Hack Is Just Old-Fashioned Extortion](https://www.bloomberg.com/opinion/articles/2026-09-11/bitcoin-white-hat-hack-is-just-old-fashioned-extortion)**

Bloomberg.com • 2d ago

---

**[Crypto firm Bitcoin Suisse to cut up to half of jobs in Switzerland](https://www.reuters.com/business/world-at-work/crypto-firm-bitcoin-suisse-cut-up-half-jobs-switzerland-2026-09-11/)**

Reuters • 1d ago

---

**[Why Is Bitcoin Dropping Today?](https://finance.yahoo.com/markets/crypto/articles/why-bitcoin-dropping-today-204955824.html)**

Hot inflation data, a looming Fed decision, and four straight days of ETF outflows are hitting Bitcoin from three directions at once, and the next 72 hours could determine whether the floor holds or breaks.

Yahoo Finance • 14h ago

---

**[How Low Can Bitcoin Go?](https://247wallst.com/investing/cryptocurrency/2026/09/12/how-low-can-bitcoin-go/)**

Bitcoin's bear calls run from a 20% flush to a 75% crash. Here is which level the evidence supports and what would invalidate it.

24/7 Wall St. • 14h ago

---

**[Bitcoin’s ‘Unusual Mix’: Bearish Inflation Print, Bullish Buyback Failure](https://bitcoinmagazine.com/news/bitcoin-has-unusual-mix-says-coinshares)**

A new CoinShares report said bitcoin's price could be hurt in the short-term but benefit in the long-term.

Bitcoin Magazine • 1d ago

---

---

## HackerNews: "bitcoin"

**[Bitcoin sidechain Liquid hacked for ~4k BTC](https://news.ycombinator.com/item?id=49600421)**

Neha Narula

⬆️ 7 • 💬 1 • 5d ago • [nehanarula.org](https://nehanarula.org/2026/09/07/liquid-hack.html)

---

**[A Fruit Fly's Disembodied Brain Is Now Trading Bitcoin on Coinbase](https://news.ycombinator.com/item?id=49673026)**

Stonkfly uses a fruit fly's 166,700-neuron brain map to place real Bitcoin trades on Coinbase with $100, but no profitable results have been shown.

⬆️ 6 • 💬 1 • 20h ago • [Gadget Review](https://www.gadgetreview.com/a-fruit-flys-disembodied-brain-is-now-trading-bitcoin-on-coinbase)

---

**[Revolut confirms it sent passport and Bitcoin data to a fake government address](https://news.ycombinator.com/item?id=49671085)**

Revolut confirme à BeInCrypto qu’un faux email gouvernemental a dérobé des données clients, dont passeports et dossiers Bitcoin.

⬆️ 6 • 💬 0 • 1d ago • [BeInCrypto](https://fr.beincrypto.com/revolut-fuite-donnees-fausse-demande-gouvernement/)

---

**[Liquid Network Pauses After $320M Bitcoin Withdrawal](https://news.ycombinator.com/item?id=49601243)**

Read this crypto post from greatHydra_997 posted on 2026/09/07 on CoinMarketCap’s Community message board. See user comments and interaction, plus replies from greatHydra_997 as they discuss up-to-date cryptocurrency topics.

⬆️ 5 • 💬 1 • 5d ago • [coinmarketcap.com](https://coinmarketcap.com/community/post/379112837/)

---

**[The first AI-run ransomware attack copied its Bitcoin address out of a tutorial](https://news.ycombinator.com/item?id=49589728)**

The thing that gets me isn’t that it worked. It’s that it worked while being this dumb.

⬆️ 5 • 💬 0 • 6d ago • [Medium](https://medium.com/@thenewgencoder/the-first-fully-ai-run-ransomware-attack-copied-its-bitcoin-address-out-of-a-tutorial-a630ee3224dc)

---

**[Hackers drain $320M in Bitcoin from Liquid Network, claim they're the good guys](https://news.ycombinator.com/item?id=49602430)**

Self-described white hats promise to return 'most' of the 4,000 BTC once the vulnerability is fixed

⬆️ 4 • 💬 1 • 5d ago • [theregister](https://www.theregister.com/security/2026/09/07/hackers-drain-320m-in-bitcoin-from-liquid-network-claim-theyre-the-good-guys/5294770)

---

**[Revolut Confirms Sending Passport and Bitcoin Records to Fake Government Email](https://news.ycombinator.com/item?id=49670849)**

Revolut confirms to BeInCrypto a fake government email pulled customer data, including passports and Bitcoin records.

⬆️ 4 • 💬 0 • 1d ago • [BeInCrypto](https://beincrypto.com/revolut-data-breach-fake-government-request/)

---

**[Bitcoin mining data center condemned after leaking 3M gallons of water](https://news.ycombinator.com/item?id=49588413)**

Oklahoma, El Reno city asserts that none of the costs related to the water leak at the property will be passed on to citizens.

⬆️ 4 • 💬 0 • 6d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order)

---

**[The Liquid Network (Bitcoin sidechain) is stuck at block 4050335](https://news.ycombinator.com/item?id=49587562)**

Explore the full Bitcoin ecosystem with The Mempool Open Source Project®. See Liquid transactions & assets, get network info, and more.

⬆️ 3 • 💬 0 • 6d ago • [liquid.network](https://liquid.network/es/block/aad24e4fb64ca8adf4961667da87820cd48e553957ac64e75de7cdb298b5d66b)

---

**[Ask HN: Anyone kicking around the idea that AI came from a state like Bitcoin?](https://news.ycombinator.com/item?id=49672539)**

⬆️ 1 • 💬 1 • 20h ago

---

---

## YouTube Videos: "bitcoin"

**[Gareth Soloway: My Final Warning To Bitcoin Investors](https://www.youtube.com/watch?v=FnmvjWBsS6s)**

Follow Gareth: https://www.youtube.com/@GarethSolowayProTrader WEEX AI Wars ($100K prize pool): ...

📺 Altcoin Daily

👁️ 45K • 👍 2K • 💬 233 • ⏱️ 39:00 • 12h ago

---

**[Why Bitcoin Wins No Matter What The Fed Does](https://www.youtube.com/watch?v=Uzc3tBB9pLg)**

Jordi Visser (@JordiVisserLabs) is a veteran macro investor with 30+ years of experience and the author of the VisserLabs ...

📺 Anthony Pompliano

👁️ 102K • 👍 2K • 💬 99 • ⏱️ 53:38 • 22h ago

---

**[Crypto’s Biggest CEO: My Final Warning To Bitcoin Holders!](https://www.youtube.com/watch?v=FBMJl3WGi04)**

Crypto's Biggest CEO: My Final Warning To Bitcoin Holders Win $100000 in WEEX Trading Competition: ...

📺 Altcoin Daily

👁️ 72K • 👍 2K • 💬 299 • ⏱️ 11:37 • 1d ago

---

**[Bitcoin&#39;s Next Target Is $109,000. Here&#39;s Why...](https://www.youtube.com/watch?v=sWowB0wxyCU)**

Bitcoin's 50-day moving average just crossed its 200-day for the first time since May 2025, and Eric Krown says the pullback that ...

📺 Crypto Banter

👁️ 17K • 👍 352 • 💬 21 • ⏱️ 43:02 • 16h ago

---

**[I Made A Huge Mistake Investing In Bitcoin](https://www.youtube.com/watch?v=Jh91F5qCswQ)**

This is the crazy story of what happened to me investing from 2024-2026. My story of bitcoin and why consistency is key. Open ...

📺 IanOnYouTube

👁️ 28K • 👍 1K • 💬 475 • ⏱️ 15:21 • 11h ago

---

**[Why Today’s CPI Result Is BIG Indicator for Bitcoin!](https://www.youtube.com/watch?v=VCzX8uCezik)**

Bitcoin is holding strong while global markets buckle under macro pressure. In this show, Ran Neuner breaks down why hot ...

📺 Crypto Banter

👁️ 45K • 👍 1K • 💬 43 • ⏱️ 29:08 • 1d ago

---

**[Bitcoin Is Built For The Economy Nobody Sees Coming | Mark Moss](https://www.youtube.com/watch?v=QfJXV85FMrk)**

Bitcoin #Crypto #finance Mark Moss joins the show to break down Bitcoin's sharp rebound, why institutional buyers accumulated ...

📺 The Wolf Of All Streets

👁️ 26K • 👍 611 • 💬 295 • ⏱️ 58:14 • 22h ago

---

**[Why the Dollar Doesn&#39;t Have to Break for Bitcoin to Win](https://www.youtube.com/watch?v=9AYHbFhyh3I)**

There are three ways Bitcoin could go hyperbolic, and only one of them requires the dollar to break. Cory Klippsten makes the ...

📺 Swan Bitcoin

👁️ 22K • 👍 583 • 💬 110 • ⏱️ 12:44 • 1d ago

---

**[Why $800K Bitcoin Targets Miss the Real Story](https://www.youtube.com/watch?v=otZ6P3iAZAY)**

Cake Wallet founder and CEO Vik Sharma reflects on why expecting an $800000 Bitcoin price target was over-optimistic. Despite ...

📺 Natalie Brunell

👁️ 10K • 👍 128 • 💬 21 • ⏱️ 0:52 • 1d ago

---

**[Bitcoin vs. the Fed: What This Means for Michael Saylor&#39;s Strategy Moves](https://www.youtube.com/watch?v=KaVEvKVRFdw)**

The Federal Reserve is expected to raise interest rates next week, the first hike since July 2023. Bitcoin's largest corporate holder ...

📺 Dana Love, PhD

👁️ 24K • 👍 723 • 💬 160 • ⏱️ 22:16 • 21h ago

---

---

*Generated by PeekDeck - A glance is all you need*
