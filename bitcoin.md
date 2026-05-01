---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-05-01T13:21:07.530048+00:00'
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

**Last Updated:** May 01, 2026 at 13:21 UTC  
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

### $78,216.75

---

## Bitcoin Chart

**24h:** +2.5%  
**7d:** +0.8%  
**30d:** +17.0%  
**90d:** +1.7%  
**1y:** -19.2%  

---

## Bitcoin Market Stats

**Market Cap:** $1548.98B
Rank #1

**Circulating Supply:** 20,023,128 BTC
95.3% of max

**All-Time High:** $126,080.00
-38.7%

**All-Time Low:** $67.81
+113942.2%

---

## Fear & Greed Index

### 26
**FEAR**

---

## Reddit: r/Bitcoin

**[Looking for “Stone Man” — Bitcointalk user from August 2010](https://www.reddit.com/r/Bitcoin/comments/1t0bvaf/looking_for_stone_man_bitcointalk_user_from/)**

Looking for “Stone Man” — Bitcointalk user from August 2010 TL;DR: I’ve spent the past 18 months analyzing the change-address bug in Bitcoin 0.3.2 that caused the loss of 8,900 BTC by Bitcointalk user #288 (“Stone Man”) on August 9, 2010. I believe these coins can be recovered if the original owner can be found and is willing to share a few technical details. The coins remain his — I’m not asking for anything except to help return them. Background On August 9, 2010, a forum user posted about losing 8,900 BTC due to the notorious “change-address bug” in the Bitcoin 0.3.2 wallet. He had restored an older wallet.dat and made a 1 BTC self-send; the change went to a newly-generated address whose private key was lost when his Live USB system was rebooted. The transaction is on-chain: Tx: eb5b761c7380ed4c6adf688f9e5ab94953dcabeda47d9eeabd77261902fccccf Block 73272, August 9, 2010, 21:35:11 UTC Output[1]: 8,899 BTC → 167ZWTT8n6s4ya8cGjqNNQjDwDGY31vmHg (unspent for 15+ years) The user’s last message ended with “gone for good” and he never returned to the forum. What I’ve found The wallet’s private-key generation in this environment depends on a chain of weak entropy sources I’ve been able to model in detail: Linux 2.6.26 kernel seed) random.c boot-time pool seeding (Live USB, no persistent random- OpenSSL 0.9.8g-15 (Debian Lenny patched) md_rand state machine, bit-for-bit Bitcoin 0.3.2’s RAND_add and RAND_bytes call sequence in CreateTransaction I’ve built a CUDA implementation that searches the parameter space at ~2M keys/sec on a single laptop GPU. Without specific hardware/timing information from the original user, the search space is too large (~10^16 to 10^22). With his cooperation — confirming utsname, hardware, boot timing, network state, and a few session details — the search space shrinks by roughly 10 orders of magnitude. With his old wallet.dat (or the sender address private key alone), the search becomes nearly instantaneous: minutes on a laptop. The key reason cooperation is so leveraged: the same PRNG state that produced the change-address private key also produced the ECDSA signing nonce used in the transaction. If the sender’s private key is known (it’s in his old wallet.dat anyway), the nonce can be derived from the on-chain signature, providing a powerful verification channel that eliminates the most expensive part of the search. Why I’m doing this I have no claim on these coins. They belong to the original user. My goal is to return them. If a small thank-you is offered after a successful recovery, I’d accept — but it’s not a condition. What I need Just to talk. If you are this person, or you know who is, please reach out. I can run the entire recovery on your computer using your wallet.dat without it ever leaving your hands. You don’t need to trust me with anything sensitive — only confirm a few non-sensitive details about the original setup. Verification To filter out impersonators, real correspondence will include questions that only the original user would know. Please reach out via: reply to this thread / DM. This is a serious 18-month research effort. Happy to share the technical write-up with anyone qualified to evaluate it, including security researchers who can vouch for the methodology. The full analysis (CUDA code, kernel/OpenSSL state machine modeling, blockchain forensics) is available on request.

14h ago

---

**[Whales scooped up an insane 11k BTC just yesterday, supply is shrinking into long term holders](https://www.reddit.com/r/Bitcoin/comments/1t057ao/whales_scooped_up_an_insane_11k_btc_just/)**

18h ago

---

**[Power projection](https://www.reddit.com/r/Bitcoin/comments/1t0a525/power_projection/)**

Okay, Major Lowery, you've got it.

15h ago

---

**[Just curious does anyone sometimes sell their bitcoin?](https://www.reddit.com/r/Bitcoin/comments/1t0imkk/just_curious_does_anyone_sometimes_sell_their/)**

Not as a panic sell but just to pay the bills when you have to and then later buy more when you can when it dips. I know that’s a random question but have you been in that situation?

9h ago

---

**[Daily Discussion, May 01, 2026](https://www.reddit.com/r/Bitcoin/comments/1t0kvml/daily_discussion_may_01_2026/)**

Please utilize this sticky thread for all general Bitcoin discussions! If you see posts on the front page or /r/Bitcoin/new which are better suited for this daily discussion thread, please help out by directing the OP to this thread instead. Thank you! If you don't get an answer to your question, you can try phrasing it differently or commenting again tomorrow. Please check the previous discussion thread for unanswered questions.

7h ago

---

**[Just out of Curuosity... how much fiat Money do you all invest in Bitcoin?](https://www.reddit.com/r/Bitcoin/comments/1t0osin/just_out_of_curuosity_how_much_fiat_money_do_you/)**

For me its like 50 percent of my capital and every now and then i buy more :)

3h ago

---

**[Mining dirt cheap with dead forklift batteries and busted solar panels](https://www.reddit.com/r/Bitcoin/comments/1szxlp8/mining_dirt_cheap_with_dead_forklift_batteries/)**

A while back I met a guy on Facebook Marketplace, a tree fell on his house and he had 30× 300W solar panels he needed gone. I rented a U-Haul and bought all of them for $30 each. I had a friend Joe who works on forklift batteries help me get started. He told me anything below like 60% gets scrapped and the scrap price is dirt cheap for what you’re actually getting. He ended up hooking me up with two 500Ah 24V forklift batteries for free, which was huge. I rented a $100 truck, the company loaded it with forklifts, and then up in Maine my cousin has a Kubota so I got lucky unloading it. I also grabbed some UPS batteries that are 12V, wired them in series to get 24V and then paralleled them, and then paralleled that with the two 24V forklift batteries. Total comes out to about 1500Ah @ 24V. The UPS batteries cost me $600 for 500Ah, which is crazy cheap. I’ve got some land in Maine so I just started throwing panels out there, nothing fancy. Literally just threw everything on the ground and put as many as I could on top of a camper. This winter a bunch of them blew off so I had to go out and put them back up lol. I’m honestly lucky the camper is still there considering the wiring… and surprised I didn’t burn it down at some point. I also found 500W panels for $10 each with cracked glass. Didn’t fix anything and they still do like 400W after 4 years. Solar panels are dirt cheap right now because China overproduced like crazy, there’s just too many panels out there. Setup: ~4–5kW+ solar ~1500Ah @ 24V battery bank One 200A charge controller 4000W inverter In full daylight I could mine all day pulling like 150 amps, which is pretty wild for basically scrap parts. First time wiring it I was pushing so much current one of the cables basically caught fire… so yeah learned about wire size real quick. I also burned up a couple inverters early on pushing too many watts through them, but eventually found a couple 4000W inverters cheap on eBay and those have been working great. Only thing that sucked is I didn’t have a cutoff so I had to manually unplug the miner or it would just drain the batteries. In the end I actually stopped mining with it and just run the camper. I used to burn like 150 gallons of gas, now I use basically nothing. I run the AC, microwave, everything with no issues. It’s still half-assed, but at least I upgraded to thicker gauge wires so it’s a little less sketchy now. The pictures below are from when I first started the setup — it’s missing a ton of panels and one of the forklift batteries. From there I ended up starting ING Mining, and now we’re one of the larger retail disruptors of used miners lol. Still, for broken panels, “dead” batteries, and Facebook deals… it worked way better than it should. -Nick Squires https://preview.redd.it/hsfmphq06cyg1.jpg?width=4032&format=pjpg&auto=webp&s=7eee2bea775028182fe5c1357be14531dc96066c https://preview.redd.it/ziy3biq06cyg1.jpg?width=4032&format=pjpg&auto=webp&s=bb3d7ead92d0f7566d2a50db1ff5d06f4a23ba48 https://preview.redd.it/zokyfiq06cyg1.jpg?width=4032&format=pjpg&auto=webp&s=0709627755b9007ab03a296f49a5b890a92ea03e

22h ago

---

**[Airgapped signing with COLDCARD Q](https://www.reddit.com/r/Bitcoin/comments/1t0682m/airgapped_signing_with_coldcard_q/)**

Been playing around with the COLDCARD Q and wanted to see how “airgapped” signing actually works in practice. Knowing that my private keys are fully Airgapped gives me a peace of mind. Would love to hear your guys’ thoughts on the ColdCard Q.

17h ago

---

**[Don't Do What You Are Told](https://www.reddit.com/r/Bitcoin/comments/1t0ezkb/dont_do_what_you_are_told/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=i6MOEWeK6QM) • 12h ago

---

**[Alternative to coinmetrics](https://www.reddit.com/r/Bitcoin/comments/1t0li3u/alternative_to_coinmetrics/)**

Guys, do you know a site similar to coinmetrics which is possible to see "advanced" metrics of the blockchain? % holders are divided by quantity, history graph etc.. A year ago coinmetrics was free, now it has a subscription of thousands of dollars.

6h ago

---

---

## Google News: "bitcoin"

**[Bitcoin edges above $77,000, but institutional activity suggests downside hedging](https://www.coindesk.com/markets/2026/05/01/bitcoin-edges-above-usd77-000-but-institutional-activity-suggests-downside-hedging)**

Bitcoin rises above $77,000 on solid volume, but rising put open interest and cautious market sentiment suggest traders are hedging against downside risk.

CoinDesk • 3h ago

---

**[Elon Musk likes Bitcoin—but he just told a jury most crypto coins are scams](https://fortune.com/2026/04/30/elon-musk-bitcoin-crypto-scams/)**

The billionaire’s thoughts on crypto came up during the OpenAI trial

Fortune • 21h ago

---

**[Bitcoin and ethereum prices today, Friday, May 1, 2026: Prices moving higher this morning](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-may-1-2026-prices-moving-higher-this-morning-113211522.html)**

Bitcoin opened at $76,306.55 on Friday, and as of 7:17 a.m ET, its value was $77,376.65. Ethereum opened at $2,256.39 on Friday, and the value of ethereum as of 7:17 a.m. ET was $2,284.34.

Yahoo Finance • 1h ago

---

**[BTC price bounces as big tech earnings fuel optimism; short-term pressures remain: Crypto Daily](https://www.coindesk.com/daybook-us/2026/05/01/bitcoin-bounces-as-big-tech-earnings-fuel-optimism-short-term-pressures-remain)**

The day ahead in crypto: May 1, 2026

CoinDesk • 2h ago

---

**[BTC price holds gains, but lacks conviction as derivatives signal caution](https://www.coindesk.com/markets/2026/05/01/bitcoin-ticks-higher-but-remains-range-bound-as-traders-keep-short-bias)**

BTC rises to $77,000 after holding $75,000 support, but negative funding, flat open interest and cautious positioning signal lack of conviction.

CoinDesk • 2h ago

---

**[Gov. Mike Braun ceremonially signs bill banning the use of bitcoin ATMS in Indiana](https://www.14news.com/2026/05/01/gov-mike-braun-signs-bill-banning-use-bitcoin-atms-indiana/)**

Governor Mike Braun ceremonially signed an emergency declaration banning the use of bitcoin ATMS in the state of Indiana.

14 News • 11h ago

---

**[Option Traders Build ‘Electric Fence’ Around Bitcoin at $80,000](https://www.bloomberg.com/news/articles/2026-04-29/option-traders-build-electric-fence-around-bitcoin-at-80-000)**

Bloomberg.com • 1d ago

---

**[Bitcoin miner MARA to acquire Long Ridge in $1.5 billion Ohio gas plant deal](https://www.theblock.co/post/399605/bitcoin-miner-mara-to-acquire-long-ridge-in-1-5-billion-ohio-gas-plant-deal)**

MARA will acquire an Ohio natural gas plant operator for $1.5 billion, shifting from bitcoin mining to digital infrastructure.

The Block • 22h ago

---

**[How Eric Trump Got Rich From Bitcoin While Losing Investors A Fortune](https://www.forbes.com/sites/danalexander/2026/04/28/how-eric-trump-got-rich-from-bitcoin-while-losing-investors-a-fortune/)**

The president’s second son pitches his bitcoin company as a money-printing machine. It’s actually an arbitrage vehicle that preys on MAGA-minded investors.

Forbes • 3d ago

---

**[Bitcoin is having its best month in a year — but the retail crowd is looking elsewhere](https://www.marketwatch.com/story/bitcoin-is-having-its-best-month-in-a-year-but-the-retail-crowd-is-looking-elsewhere-d01aa6c1)**

MarketWatch • 1d ago

---

---

## HackerNews: "bitcoin"

**[Your Terminal Is Burning Battery Like It's Mining Bitcoin](https://news.ycombinator.com/item?id=47941517)**

How a 1970s-era application like a terminal emulator can consume more battery than Zoom with video. The irony, the causes, and the solutions.

⬆️ 81 • 💬 54 • 2d ago • [frr.dev](https://www.frr.dev/posts/terminal-gpu-battery-macbook-ghostty-iterm2/)

---

**[SatoshiGuesser – Roll for Bitcoin](https://news.ycombinator.com/item?id=47964897)**

Roll for lost bitcoin. Contribute to Pathos0925/SatoshiGuesser development by creating an account on GitHub.

⬆️ 50 • 💬 52 • 20h ago • [GitHub](https://github.com/Pathos0925/SatoshiGuesser)

---

**[Bitcoin Dev Plans to 'Reassign' Coins Linked to Satoshi Nakamoto in Hard Fork](https://news.ycombinator.com/item?id=47927451)**

Paul Sztorc’s proposed eCash fork would give investors coins cloned from wallets believed to belong to Bitcoin creator Satoshi Nakamoto.

⬆️ 6 • 💬 8 • 3d ago • [Decrypt](https://decrypt.co/365712/bitcoin-developer-reassign-coins-linked-satoshi-nakamoto-hard-fork)

---

**[Bitcoin 'Q-Day' Draws Nearer as Quantum Researcher Breaks Simplified Key](https://news.ycombinator.com/item?id=47896517)**

The quantum threat to Bitcoin keeps inching closer, this time thanks to a researcher who broke a simplified cryptographic key.

⬆️ 3 • 💬 3 • 6d ago • [Decrypt](https://decrypt.co/365444/bitcoin-q-day-draws-nearer-quantum-researcher-breaks-simplified-key)

---

**[Bitcoin Is Digging Deeeeeper](https://news.ycombinator.com/item?id=47925278)**

⬆️ 3 • 💬 1 • 3d ago • [alphametrics.substack.com](https://alphametrics.substack.com/p/bitcoin-is-digging-deeper)

---

**[Guess at lost Bitcoin, right in the browser](https://news.ycombinator.com/item?id=47958759)**

A slot machine that guesses Satoshi Nakamoto's Bitcoin private keys. Astronomically unlikely. Mathematically non-zero.

⬆️ 2 • 💬 0 • 1d ago • [satoshiguesser.com](https://satoshiguesser.com)

---

**[U.S. Seizes $15B in Bitcoin in Crypto 'Scam' Crackdown](https://news.ycombinator.com/item?id=47971809)**

⬆️ 1 • 💬 2 • 6h ago • [forbes.com](https://www.forbes.com/sites/martinacastellanos/2025/10/14/us-seizes-15-billion-in-bitcoin-sanctions-cambodias-prince-group-in-global-crypto-scam-crackdown/)

---

**[Jack Dorsey's Block launches new Bitcoin hardware wallet, Bitkey](https://news.ycombinator.com/item?id=47924028)**

Bitkey is a bitcoin self-custody wallet with an app, hardware device, and built-in recovery, so you keep your private keys without losing access.

⬆️ 1 • 💬 2 • 3d ago • [Bitkey](https://bitkey.world)

---

**[Show HN: Bitcoin Monitor Widget](https://news.ycombinator.com/item?id=47973253)**

Bitcoin Monitor Widget -  Build your own real-time crypto space with price widgets, portfolio views, themes, logs, terminal, games, custom API cards, alerts.

⬆️ 1 • 💬 0 • 2h ago • [Bitcoin Monitor Widget](https://btcwid.com)

---

**[Iran Proposes Bitcoin Oil Toll](https://news.ycombinator.com/item?id=47958343)**

Iranian officials said Bitcoin payments would ensure the tolls “can’t be traced or confiscated due to sanctions.”

⬆️ 1 • 💬 0 • 1d ago • [Decrypt](https://decrypt.co/363641/iran-bitcoin-payments-oil-ships-seeking-hormuz-passage)

---

---

## YouTube Videos: "bitcoin"

**[Be SCARED If You Don&#39;t Own Bitcoin | Michael Saylor’s $10M Endgame Is Here](https://www.youtube.com/watch?v=00r6gKyA_wI)**

A billionaire just issued a global warning and it is not subtle. Tim Draper and Michael Saylor lay out a future where fiat breaks and ...

📺 Simply Bitcoin

👁️ 31K • 👍 2K • 💬 151 • ⏱️ 18:17 • 1d ago

---

**[The Fed Shakeup That Sets Off Bitcoin&#39;s Biggest Rally Ever!](https://www.youtube.com/watch?v=sjCHEGFDJks)**

Bitcoin may be entering one of the most important macro setups in its history as AI disruption, Fed policy, negative real rates, ...

📺 Simply Bitcoin

👁️ 23K • 👍 2K • 💬 134 • ⏱️ 18:39 • 16h ago

---

**[Get Ready...Bitcoin Is One Level Away From Exploding](https://www.youtube.com/watch?v=gM2kDjaJ1l4)**

Make FREE Crypto Predictions & Compete Weekly ▻ https://www.clashpicks.com/ Research. Tracking. Charting. All In One AI ...

📺 CryptosRUs

👁️ 19K • 👍 1K • 💬 301 • ⏱️ 43:42 • 22h ago

---

**[Bitcoin&#39;s Bearish Pattern: Key Level to Watch Before the Next Big Move](https://www.youtube.com/watch?v=zAaoofe5f18)**

In this episode of Pro Charts: Crypto, Master Trader Gareth Soloway breaks down the current technical structure on Bitcoin, ...

📺 Verified Pro Traders

👁️ 17K • 👍 1K • 💬 102 • ⏱️ 8:44 • 19h ago

---

**[Bitcoin Isn&#39;t Replacing Gold. It&#39;s Replacing THIS](https://www.youtube.com/watch?v=wESDdd9P60I)**

While everyone's arguing about whether Bitcoin replaces gold. What if I told you it doesn't matter? Gold is a $30 trillion debate.

📺 Mark Moss

👁️ 44K • 👍 2K • 💬 245 • ⏱️ 28:23 • 18h ago

---

**[THIS chart will change your 2026 Bitcoin price prediction...](https://www.youtube.com/watch?v=iqf2RG2s7OY)**

Trade on Phemex Phemex Exchange ✔️ https://phemex.com/a/k/TylerS Trade on Bitunix ...

📺 Tyler S

👁️ 9K • 👍 614 • 💬 182 • ⏱️ 13:02 • 20h ago

---

**[Eric Trump JUST LEAKED Americas Strategic Bitcoin Reserve Plan?! | EP 1494](https://www.youtube.com/watch?v=13Ek3AJjbVE)**

Eric Trump might've had the most bullish soundclip coming out of Bitcoin 2026 Las Vegas ...

📺 Simply Bitcoin

👁️ 8K • 👍 389 • 💬 58 • ⏱️ 1:26:37 • 19h ago

---

**[Keynote: Jack Mallers - The Bitcoin Company | Bitcoin 2026](https://www.youtube.com/watch?v=dEsSHoHZRH0)**

What does the ideal Bitcoin company actually look like? In this Bitcoin 2026 keynote, Jack Mallers CEO of Strike and Twenty One ...

📺 Bitcoin Magazine

👁️ 33K • 👍 1K • 💬 165 • ⏱️ 37:06 • 1d ago

---

**[Bitcoin 2026 | Day 3 Livestream](https://www.youtube.com/watch?v=KXBp1g9e3cA)**

Tune in to the Bitcoin 2026 Las Vegas Day 3 livestream, featuring Eric Trump, Jack Mallers, and Afroman and more global Bitcoin ...

📺 Bitcoin Magazine

👁️ 19K • 👍 443 • 💬 10 • ⏱️ 8:59:08 • 1d ago

---

**[Bitcoiner Holders: Banks Suggesting 4% To Bitcoin](https://www.youtube.com/watch?v=zEzFnjQalA8)**

See if your SSN is for sale right now. My sponsor Cloaked will tell you for free in 2 seconds here: https://cloaked.com/aaronbennett ...

📺 Aaron Bennett

👁️ 4K • 👍 252 • 💬 23 • ⏱️ 11:18 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
