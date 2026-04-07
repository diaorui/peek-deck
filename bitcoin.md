---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-04-07T16:11:10.326331+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- videos
- news
- cryptocurrency
- social
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** April 07, 2026 at 16:11 UTC  
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

### $68,130.81

---

## Bitcoin Chart

**24h:** -1.9%  
**7d:** +0.2%  
**30d:** -0.2%  
**90d:** -25.1%  
**1y:** -10.9%  

---

## Bitcoin Market Stats

**Market Cap:** $1366.02B
Rank #1

**Circulating Supply:** 20,012,671 BTC
95.3% of max

**All-Time High:** $126,080.00
-45.9%

**All-Time Low:** $67.81
+100436.8%

---

## Fear & Greed Index

### 11
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[BLOOMBERG: Morgan Stanley Bitcoin ETF will launch this week](https://www.reddit.com/r/Bitcoin/comments/1sexipw/bloomberg_morgan_stanley_bitcoin_etf_will_launch/)**

Loading before launch

1h ago

---

**[bitcoin provides mathematical certainty in a world that is more fake and uncertain than ever. There will only be 21,000,000 bitcoin, forever](https://www.reddit.com/r/Bitcoin/comments/1sezsdb/bitcoin_provides_mathematical_certainty_in_a/)**

22m ago

---

**[It’s going to 🚀](https://www.reddit.com/r/Bitcoin/comments/1se4g7y/its_going_to/)**

23h ago

---

**[I have $100K but I am certain that once I buy BTC will begin to drop to $35,000](https://www.reddit.com/r/Bitcoin/comments/1seaemq/i_have_100k_but_i_am_certain_that_once_i_buy_btc/)**

I just know it. So I won't buy just so the rest of you can make some money.

19h ago

---

**[You set up a hardware wallet and wrote down your seed phrase. Here’s what most guides don’t tell you.](https://www.reddit.com/r/Bitcoin/comments/1sec3fl/you_set_up_a_hardware_wallet_and_wrote_down_your/)**

There’s a post near the top of this sub right now where someone sent Bitcoin to their Trezor and the wallet showed empty. They panicked. Turns out their Bitcoin wasn’t gone — it was in their passphrase wallet. They hadn’t known they created one. That’s the most common failure pattern in hardware wallet support forums, and it almost never gets explained at setup. Here’s what’s actually happening and three other traps that catch people the same way. The passphrase trap When you set up a Trezor using Trezor Suite, the passphrase feature is on by default. A passphrase — sometimes called the 25th word — creates a completely separate wallet derived from your seed. Any input during setup creates one. An accidental keystroke creates one. If you set a passphrase and don’t write it down, that passphrase is gone forever — and so is everything in that wallet. Your seed phrase alone opens a different, empty wallet. No error message. Nothing to indicate anything is wrong. Trezor’s support forums have dozens of threads that all read identically: “I have my seed, I’ve tried everything, balance is zero.” In most cases the passphrase was set accidentally during initial setup. Different software generates different addresses from the same seed This sounds impossible but it’s documented repeatedly. There are multiple standards for how wallet software derives addresses from a seed phrase — BIP-44, BIP-49, BIP-84 are the common ones — and different apps default to different ones. One user bought Bitcoin through Exodus paired with a Trezor in 2021. Exodus defaulted to P2SH-SegWit (m/49’/0’/0’). Trezor Suite defaults to Native SegWit (m/84’/0’/0’). Four years later, a firmware update forced a reset. The user opened Trezor Suite instead of reconnecting through Exodus. Empty wallet. His Bitcoin was on-chain and accessible — completely invisible to the software he was now using. Valid seed. Right device. Zero balance. This is not a bug. It’s two correct implementations of different standards. Electrum does not speak the same language as your hardware wallet If you ever try to import your Trezor or Ledger seed into Electrum as a backup option, it will show an empty wallet. Electrum uses a proprietary seed format and deliberately does not support BIP-39 — the standard your hardware wallet uses. To get it working you have to click a hidden “Options” button during seed entry, select “BIP39 seed,” then manually enter the derivation path your original wallet used. Without those steps, Electrum opens a valid empty wallet with no explanation. The Electrum developers are aware of this and consider it a feature. What to actually write down alongside your seed phrase The seed is the starting point, not the whole picture. What you also need documented somewhere safe: Which device and software you used to set up the wallet (Trezor Suite, Ledger Live, Electrum, etc.) Whether a passphrase was set — and if yes, exactly what it was, case-sensitive Which address format was used (Legacy, SegWit, Native SegWit, Taproot) — your software may show this during setup The derivation path if you can find it — usually visible in advanced settings That context, stored with your seed backup, is what makes the difference between recovery taking five minutes and recovery being impossible.

18h ago

---

**[Demonstration Of "Attack Blocks" On Bitcoin's Signet Test Network](https://www.reddit.com/r/Bitcoin/comments/1sennu8/demonstration_of_attack_blocks_on_bitcoins_signet/)**

In two days, on Wednesday April 8th, a handful of Bitcoin Core developers are going to be doing a demonstration of “attack blocks” designed to take an inordinate amount of time to verify on Signet. The demonstration will take place at 10 AM EST (2 PM UTC). Anyone who wishes to participate can run Bitcoin Core node on Signet and watch the blocks be mined and processed by their node in real-time. Instructions can be found here to spin up a node and follow along (including how to check your node’s logs to see the verification times for the attack blocks). The demonstration is not going to show the worst case of the attack (the script and transaction structure required has not been publicly revealed to not give malicious actors even more information about the attack), but it will produce blocks that take orders of magnitude more time to verify than your average block. The aim of the demonstration is to show users the severity of one of the four severe consensus vulnerabilities that the Great Consensus Cleanup aims to address with BIP 54. Two more demonstrations will take place at 6 PM EST (10 PM UTC) on April 8th, and at 5 AM EST (9 AM UTC) on April 9th, to allow for Bitcoin users in different global timezones to directly participate as well. The Signet blockchain is currently at around 32-33 GB, so if you have any device with ample storage space, go ahead and spin up a Signet node to participate. For your awareness the following software patch was quickly put together for this demonstration and not audited thoroughly (though it is just a basic terminal based-GUI). If you are spinning up a brand new Signet node just for this demonstration on a machine without any funds on it, you should be fine even if you are the paranoid type like me. For those who don’t want to just poke at log files, AJ Towns provided a patch to the “bitcoin-tui” project, a Terminal based GUI for Bitcoin Core to display the attack blocks during the demonstration. The project creator is working on a proper release in time for the demonstration, but you can also compile it yourself. Run these commands on Linux (git commands will work on other OSes, and you should be able to find the equivalent CLI commands for your OS easily online): git clone https://github.com/ajtowns/bitcoin-tui.git cd bitcoin-tui git switch 202604-bip54blocks From there you should be able to just follow the build instructions at the repository here. After compiling, make sure your bitcoind has “server=1” set in the config file, and start up bitcoin-tui. You should find a “Slow Blocks” tab on the right of the top bar.

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/demonstration-of-attack-blocks-on-bitcoins-signet-test-network) • 10h ago

---

**[Daily Discussion, April 07, 2026](https://www.reddit.com/r/Bitcoin/comments/1senrk6/daily_discussion_april_07_2026/)**

Please utilize this sticky thread for all general Bitcoin discussions! If you see posts on the front page or /r/Bitcoin/new which are better suited for this daily discussion thread, please help out by directing the OP to this thread instead. Thank you! If you don't get an answer to your question, you can try phrasing it differently or commenting again tomorrow. Please check the previous discussion thread for unanswered questions.

10h ago

---

**[Bitcoin from Zero — Day 1: What is Bitcoin and why does it exist?](https://www.reddit.com/r/Bitcoin/comments/1sei2b2/bitcoin_from_zero_day_1_what_is_bitcoin_and_why/)**

Gm r/Bitcoin. 🟠 Starting an educational series — simple, direct, no jargon, no promises. Just verifiable facts. Day 1: What is Bitcoin? Bitcoin is digital money with a fixed supply of 21 million units — hardcoded by Satoshi Nakamoto in 2009. No government, bank, or company can ever change that. Verified data — April 2026: - Over 20 million BTC already mined (95%+ of total supply) - Less than 1 million remain — and will take 100+ years to mine - New block every ~10 minutes - Current reward: 3.125 BTC per block (after April 2024 halving) - Next halving: estimated April 2028 Why does this matter for someone who barely pays rent? The money you keep in the bank loses value every year to inflation. Bitcoin has a fixed supply — nobody can "print more." For the first time in history, an ordinary person has access to a genuinely scarce asset. Don't trust. Verify Next week — Day 2: Why does money lose value? #Bitcoin #Education #BitcoinFromZero

14h ago

---

**[Men only have two moods:](https://www.reddit.com/r/Bitcoin/comments/1sdz0lp/men_only_have_two_moods/)**

1d ago

---

**[Transferring Bitcoin without actually moving it: explaining how Statechains work](https://www.reddit.com/r/Bitcoin/comments/1sesmni/transferring_bitcoin_without_actually_moving_it/)**

A practical look at an alternative scaling method for Bitcoin: transferring ownership, not coins.

🔗 [BitBox Blog](https://blog.bitbox.swiss/en/transferring-bitcoin-without-actually-moving-it-explaining-how-statechains-work/) • 5h ago

---

---

## Google News: "bitcoin"

**[Nobel-winning physicist warns bitcoin could be early target of quantum computing](https://www.coindesk.com/business/2026/04/07/bitcoin-quantum-threat-is-real-and-closer-than-it-looks-says-nobel-physicist)**

Google quantum pioneer says encryption-breaking use cases may arrive sooner than expected, urging crypto industry to prepare now

CoinDesk • 3h ago

---

**[Bitcoin Topped $70,000 Today. More Wall Street Firms Are Building Up Crypto Services](https://www.investopedia.com/bitcoin-topped-usd70-000-today-more-wall-street-firms-are-building-up-crypto-services-11943355)**

The price of bitcoin climbed toward $70,000 amid reports of potential ceasefire discussions between the U.S. and Iran.

Investopedia • 23h ago

---

**[Bitcoin has been the 'shining light' during the Iran war, says Anthony Pompliano](https://www.cnbc.com/video/2026/04/07/bitcoin-has-been-the-shining-light-during-the-iran-war-says-anthony-pompliano.html)**

Anthony Pompliano, ProCap Financial CEO, joins 'Squawk Box' to discuss bitcoin's performance amid the Iran war, global bitcoin adoption, his company's latest agentic AI financial services, and more.

CNBC • 5h ago

---

**[Bitcoin Ticks Up Even as Trump’s Iran War Threats Cloud Markets](https://www.bloomberg.com/news/articles/2026-04-06/bitcoin-ticks-up-even-as-trump-s-iran-war-threats-cloud-markets)**

Bloomberg.com • 1d ago

---

**[Bitcoin slides with risk assets as Trump’s Iran ultimatum looms](https://fortune.com/2026/04/07/bitcoin-slides-with-risk-assets-as-trumps-iran-ultimatum-looms/)**

The decline erased gains from the previous day, when Bitcoin briefly topped $70,000 for the first time since March.

Fortune • 26m ago

---

**[Bitcoin Trader Gets Liquidated After BTC's Rally—Account Once $84 Million Strong, Now Down To The Last $914](https://finance.yahoo.com/markets/crypto/articles/bitcoin-trader-gets-liquidated-btcs-150120120.html)**

Pseudonymous cryptocurrency trader James Wynn, known for their high-risk leveraged bets, has been liquidated shorting Bitcoin once again, on-chain tracking firm Lookonchain reported on Sunday. Bitcoin Moves Against Wynn’s Bet…Again Lookonchain, citing data from Hyperliquid perpetual exchange, stated that Wynn...

Yahoo Finance • 1h ago

---

**[Morgan Stanley’s Bitcoin ETF MBST To Go Live Tomorrow, 16,000 Advisors Ready To Sell It To Clients](https://bitcoinmagazine.com/news/morgan-stanleys-bitcoin-mbst-to-go-live)**

Morgan Stanley’s spot bitcoin ETF (MBST) is set to begin trading on April 8, marking the bank’s entry into the U.S. spot bitcoin ETF market.

Bitcoin Magazine • 47m ago

---

**[Spot bitcoin ETFs report largest single-day inflow in six weeks, worth $471 million](https://www.theblock.co/post/396499/bitcoin-etfs-largest-day-inflow-six-weeks)**

The return in inflows reflects renewed confidence among institutional participants in the crypto market, analysts said.

The Block • 9h ago

---

**[‘A Major Mistake’—Bitcoin Is Suddenly Braced For A Federal Reserve Price ‘Surprise’](https://www.forbes.com/sites/digital-assets/2026/04/06/bitcoin-is-suddenly-braced-for-a-federal-reserve-price-surprise/)**

forbes.com • 1d ago

---

**[The ETF easy button for Bitcoin (and the fine print you need to read)](https://nypost.com/business/spot-bitcoin-etf-pros-cons-guide/)**

Bitcoin ETFs offer the convenience of buying crypto from your standard brokerage account, but what are investors giving up for the privilege?

New York Post • 7h ago

---

---

## HackerNews: "bitcoin"

**[Quantum computer researchers: Bitcoin encryption breakable in a few years](https://news.ycombinator.com/item?id=47630141)**

Google Quantum AI: Quantum computer could break Bitcoin cryptography with under 500,000 qubits in nine minutes. This will likely only be possible in the 2030s.

⬆️ 15 • 💬 7 • 3d ago • [heise online](https://www.heise.de/en/news/Quantum-computer-researchers-Bitcoin-encryption-breakable-in-a-few-years-11244911.html)

---

**[Google warns quantum computing may break Bitcoin earlier than thought](https://news.ycombinator.com/item?id=47596300)**

Google Research said the necessary resources for quantum computers to break cryptocurrencies have seen a 20-fold reduction.

⬆️ 7 • 💬 2 • 6d ago • [The Block](https://www.theblock.co/post/395814/google-quantum-computing-earlier)

---

**[Google researchers just put a new expiration date on Bitcoin](https://news.ycombinator.com/item?id=47602164)**

Bitcoin needs to fix this in the next three years.

⬆️ 5 • 💬 2 • 6d ago • [Mashable](https://mashable.com/article/google-research-bitcoin-cryptography-broken)

---

**[Moody's Prices Bitcoin at a 28% Haircut](https://news.ycombinator.com/item?id=47628597)**

April 03, 2026 - A new $100 million bond deal reveals exactly how traditional finance values BTC as collateral. The numbers are sobering, and the

⬆️ 4 • 💬 2 • 3d ago • [Bitcoin, Altcoins, Crypto News & Financial Market News](https://catenaa.com/markets/cryptocurrencies/moodys-bitcoin-collateral-haircut/)

---

**[Strive, Tuttle File Leveraged Bitcoin ETF](https://news.ycombinator.com/item?id=47621293)**

⬆️ 4 • 💬 0 • 4d ago • [catenaa.com](https://catenaa.com/markets/cryptocurrencies/strive-tuttle-file-leveraged-etf-tied-to-bitcoin-preferreds/)

---

**[Google Paper Warns of Quantum Computing Risk for Bitcoin](https://news.ycombinator.com/item?id=47600418)**

⬆️ 3 • 💬 1 • 6d ago • [wsj.com](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-03-31-2026/card/google-paper-warns-of-quantum-computing-risk-for-bitcoin-x4yBALvF5ezP4R8mk25q)

---

**[Bitcoin developers are mostly not concerned about quantum risk](https://news.ycombinator.com/item?id=47667515)**

⬆️ 2 • 💬 0 • 18h ago • [murmurationstwo.substack.com](https://murmurationstwo.substack.com/p/bitcoin-developers-are-mostly-not)

---

**[How well do you remember the 2017 Bitcoin bull run?](https://news.ycombinator.com/item?id=47619199)**

Test your prediction skills against historical data. Draw your forecast and see how you rank.

⬆️ 2 • 💬 0 • 4d ago • [longmarkets.app](https://longmarkets.app/rewinds/rewind-bitcoin-2017)

---

**[Show HN: Live simulation of AI agents scamming each other (and getting caught)](https://news.ycombinator.com/item?id=47595450)**

⬆️ 4 • 💬 0 • 6d ago • [5.161.255.238:8888](http://5.161.255.238:8888)

---

**[Quad9 Enables DNS over HTTP/3 and DNS over QUIC](https://news.ycombinator.com/item?id=47610777)**

A public and free DNS service for a better security and privacy

⬆️ 68 • 💬 17 • 5d ago • [Quad9](https://quad9.net/news/blog/quad9-enables-dns-over-http-3-and-dns-over-quic/)

---

---

## YouTube Videos: "bitcoin"

**[BRACE YOURSELF... Crypto is about to get ABSOLUTELY CRAZY!](https://www.youtube.com/watch?v=0b0OkhhPaLc)**

BRACE YOURSELF... Crypto is about to get ABSOLUTELY CRAZY! For more info on BTQ Bitcoin Quantum research: ...

📺 Altcoin Daily

👁️ 37K • 👍 2K • 💬 367 • ⏱️ 9:57 • 17h ago

---

**[Bitcoin Holders: This Is The End](https://www.youtube.com/watch?v=W3LIfBjaNUI)**

Bitcoin stuck as Trump Iran deal nears dangerous point. BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 9K • 👍 633 • 💬 57 • ⏱️ 10:20 • 4h ago

---

**[BITCOIN: This Rejection Says It ALL! (bad news) - BTC Price Prediction Today](https://www.youtube.com/watch?v=pAxVrVFSMYA)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 5K • 👍 463 • 💬 35 • ⏱️ 13:03 • 6h ago

---

**[The Big Print Is Coming &amp; Bitcoin Will Still Fail You...](https://www.youtube.com/watch?v=cv9sJMGOoR4)**

Could the oil crisis Break Bitcoin? Insider oil tracking just hit $173 a barrel and physical Brent is already at $141. The Big Print is ...

📺 Simply Bitcoin

👁️ 26K • 👍 2K • 💬 434 • ⏱️ 16:01 • 1d ago

---

**[my HONEST 2026 bitcoin price prediction... [you might not like it]](https://www.youtube.com/watch?v=Iknd8WcG44k)**

Trade on Phemex Phemex Exchange ✔️ https://phemex.com/a/k/TylerS Trade on Bitunix ...

📺 Tyler S

👁️ 12K • 👍 683 • 💬 679 • ⏱️ 13:45 • 1d ago

---

**[Bitcoin Goes Up To $1Million?!](https://www.youtube.com/watch?v=CPCoqd0HxWM)**

📺 FreshandFit

👁️ 79K • 👍 2K • 💬 48 • ⏱️ 0:34 • 1d ago

---

**[Bitcoin Reclaims $69K As Global Instability Ramps Up - Worst Yet To Come?](https://www.youtube.com/watch?v=tw9SqQ6P7Gc)**

Bitcoin #Crypto #Finance Bitcoin uncertainty is rising fast as global instability continues to build across markets. A critical week of ...

📺 The Wolf Of All Streets

👁️ 20K • 👍 1K • 💬 483 • ⏱️ 1:05:40 • 1d ago

---

**[BITCOIN: The Calm Before The Storm (Prepare Now)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=xPusQb5EC1g)**

BITCOIN: The Calm Before The Storm (Prepare Now)!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 10K • 👍 325 • 💬 308 • ⏱️ 18:13 • 1d ago

---

**[A BIG BITCOIN MOVE IS IMMINENT...](https://www.youtube.com/watch?v=-dwy0ou3QJc)**

WEEX: https://www.weex.com/events/welcome-event?vipCode=00dt&qrType=activity 25% FEE DISCOUNT & GET FREE $25 ...

📺 Crypto Rover

👁️ 6K • 👍 466 • 💬 51 • ⏱️ 9:24 • 9h ago

---

**[Here&#39;s When &amp; Where I&#39;m Buying Bitcoin](https://www.youtube.com/watch?v=V1R4Qwb76Kk)**

Here's When & Where I'm Buying Bitcoin The next flush will cause despair Hunting for leadership TA & Live Trades Get the CF ...

📺 Camel Finance

👁️ 6K • 👍 504 • 💬 67 • ⏱️ 21:14 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
