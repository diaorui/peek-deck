---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-04-07T19:05:06.570049+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- videos
- cryptocurrency
- news
- social
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** April 07, 2026 at 19:05 UTC  
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

### $68,453.51

---

## Bitcoin Chart

**24h:** -2.0%  
**7d:** +0.5%  
**30d:** +0.1%  
**90d:** -24.9%  
**1y:** -10.6%  

---

## Bitcoin Market Stats

**Market Cap:** $1369.21B
Rank #1

**Circulating Supply:** 20,012,731 BTC
95.3% of max

**All-Time High:** $126,080.00
-45.7%

**All-Time Low:** $67.81
+100804.0%

---

## Fear & Greed Index

### 11
**EXTREME FEAR**

---

## Reddit: r/Bitcoin

**[bitcoin provides mathematical certainty in a world that is more fake and uncertain than ever. There will only be 21,000,000 bitcoin, forever](https://www.reddit.com/r/Bitcoin/comments/1sezsdb/bitcoin_provides_mathematical_certainty_in_a/)**

3h ago

---

**[BLOOMBERG: Morgan Stanley Bitcoin ETF will launch this week](https://www.reddit.com/r/Bitcoin/comments/1sexipw/bloomberg_morgan_stanley_bitcoin_etf_will_launch/)**

Loading before launch

4h ago

---

**[Wallet of Satoshi now lets you use a self-custodial wallet with seamless access to the Lightning Network, thanks to Spark the new high speed L2 solution!](https://www.reddit.com/r/Bitcoin/comments/1sf1qcr/wallet_of_satoshi_now_lets_you_use_a/)**

There is a lot to talk about, but if you want to read more: https://www.xverse.app/blog/what-is-spark-bitcoin-l2 quick TL;DR: Spark is a Bitcoin L2 designed for fast, cheap, and self-custodial transactions, leveraging statechain tech and atomic swaps. Spark supports the issuance and transfer of stablecoins and tokens on Bitcoin, enabling new financial use cases such as payments, trading, and earning stablecoin yield. Spark provides a scalable ecosystem for wallets, developers, and businesses to build financial apps interoperable with Lightning Network and Taproot Assets. Wallet of Satoshi now integrates Spark, letting you create a self-custodial wallet, secure your 12 word seed, and seamlessly send/receive BTC on the Lightning Network while staying fully in control of your funds. hope many other lightning wallets such as Strike, Blink, Speed, Coinos implement Spark Welcome to the new era of scalability of BTC!

2h ago

---

**[It’s going to 🚀](https://www.reddit.com/r/Bitcoin/comments/1se4g7y/its_going_to/)**

1d ago

---

**[I have $100K but I am certain that once I buy BTC will begin to drop to $35,000](https://www.reddit.com/r/Bitcoin/comments/1seaemq/i_have_100k_but_i_am_certain_that_once_i_buy_btc/)**

I just know it. So I won't buy just so the rest of you can make some money.

22h ago

---

**[The Real War Isn’t in Iran — It’s in the US Treasury Market | Luke Gromen & Lyn Alden](https://www.reddit.com/r/Bitcoin/comments/1sf2308/the_real_war_isnt_in_iran_its_in_the_us_treasury/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/6tkKoMEiFDk?si=apOVGifqYreR3Pfm) • 1h ago

---

**[You set up a hardware wallet and wrote down your seed phrase. Here’s what most guides don’t tell you.](https://www.reddit.com/r/Bitcoin/comments/1sec3fl/you_set_up_a_hardware_wallet_and_wrote_down_your/)**

There’s a post near the top of this sub right now where someone sent Bitcoin to their Trezor and the wallet showed empty. They panicked. Turns out their Bitcoin wasn’t gone — it was in their passphrase wallet. They hadn’t known they created one. That’s the most common failure pattern in hardware wallet support forums, and it almost never gets explained at setup. Here’s what’s actually happening and three other traps that catch people the same way. The passphrase trap When you set up a Trezor using Trezor Suite, the passphrase feature is on by default. A passphrase — sometimes called the 25th word — creates a completely separate wallet derived from your seed. Any input during setup creates one. An accidental keystroke creates one. If you set a passphrase and don’t write it down, that passphrase is gone forever — and so is everything in that wallet. Your seed phrase alone opens a different, empty wallet. No error message. Nothing to indicate anything is wrong. Trezor’s support forums have dozens of threads that all read identically: “I have my seed, I’ve tried everything, balance is zero.” In most cases the passphrase was set accidentally during initial setup. Different software generates different addresses from the same seed This sounds impossible but it’s documented repeatedly. There are multiple standards for how wallet software derives addresses from a seed phrase — BIP-44, BIP-49, BIP-84 are the common ones — and different apps default to different ones. One user bought Bitcoin through Exodus paired with a Trezor in 2021. Exodus defaulted to P2SH-SegWit (m/49’/0’/0’). Trezor Suite defaults to Native SegWit (m/84’/0’/0’). Four years later, a firmware update forced a reset. The user opened Trezor Suite instead of reconnecting through Exodus. Empty wallet. His Bitcoin was on-chain and accessible — completely invisible to the software he was now using. Valid seed. Right device. Zero balance. This is not a bug. It’s two correct implementations of different standards. Electrum does not speak the same language as your hardware wallet If you ever try to import your Trezor or Ledger seed into Electrum as a backup option, it will show an empty wallet. Electrum uses a proprietary seed format and deliberately does not support BIP-39 — the standard your hardware wallet uses. To get it working you have to click a hidden “Options” button during seed entry, select “BIP39 seed,” then manually enter the derivation path your original wallet used. Without those steps, Electrum opens a valid empty wallet with no explanation. The Electrum developers are aware of this and consider it a feature. What to actually write down alongside your seed phrase The seed is the starting point, not the whole picture. What you also need documented somewhere safe: Which device and software you used to set up the wallet (Trezor Suite, Ledger Live, Electrum, etc.) Whether a passphrase was set — and if yes, exactly what it was, case-sensitive Which address format was used (Legacy, SegWit, Native SegWit, Taproot) — your software may show this during setup The derivation path if you can find it — usually visible in advanced settings That context, stored with your seed backup, is what makes the difference between recovery taking five minutes and recovery being impossible.

21h ago

---

**[Demonstration Of "Attack Blocks" On Bitcoin's Signet Test Network](https://www.reddit.com/r/Bitcoin/comments/1sennu8/demonstration_of_attack_blocks_on_bitcoins_signet/)**

In two days, on Wednesday April 8th, a handful of Bitcoin Core developers are going to be doing a demonstration of “attack blocks” designed to take an inordinate amount of time to verify on Signet. The demonstration will take place at 10 AM EST (2 PM UTC). Anyone who wishes to participate can run Bitcoin Core node on Signet and watch the blocks be mined and processed by their node in real-time. Instructions can be found here to spin up a node and follow along (including how to check your node’s logs to see the verification times for the attack blocks). The demonstration is not going to show the worst case of the attack (the script and transaction structure required has not been publicly revealed to not give malicious actors even more information about the attack), but it will produce blocks that take orders of magnitude more time to verify than your average block. The aim of the demonstration is to show users the severity of one of the four severe consensus vulnerabilities that the Great Consensus Cleanup aims to address with BIP 54. Two more demonstrations will take place at 6 PM EST (10 PM UTC) on April 8th, and at 5 AM EST (9 AM UTC) on April 9th, to allow for Bitcoin users in different global timezones to directly participate as well. The Signet blockchain is currently at around 32-33 GB, so if you have any device with ample storage space, go ahead and spin up a Signet node to participate. For your awareness the following software patch was quickly put together for this demonstration and not audited thoroughly (though it is just a basic terminal based-GUI). If you are spinning up a brand new Signet node just for this demonstration on a machine without any funds on it, you should be fine even if you are the paranoid type like me. For those who don’t want to just poke at log files, AJ Towns provided a patch to the “bitcoin-tui” project, a Terminal based GUI for Bitcoin Core to display the attack blocks during the demonstration. The project creator is working on a proper release in time for the demonstration, but you can also compile it yourself. Run these commands on Linux (git commands will work on other OSes, and you should be able to find the equivalent CLI commands for your OS easily online): git clone https://github.com/ajtowns/bitcoin-tui.git cd bitcoin-tui git switch 202604-bip54blocks From there you should be able to just follow the build instructions at the repository here. After compiling, make sure your bitcoind has “server=1” set in the config file, and start up bitcoin-tui. You should find a “Slow Blocks” tab on the right of the top bar.

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/demonstration-of-attack-blocks-on-bitcoins-signet-test-network) • 13h ago

---

**[I think Satoshi Nakamoto is Alive](https://www.reddit.com/r/Bitcoin/comments/1sevvni/i_think_satoshi_nakamoto_is_alive/)**

5h ago

---

**[Anyone else noticed different payouts between mining pools?](https://www.reddit.com/r/Bitcoin/comments/1sf0kfj/anyone_else_noticed_different_payouts_between/)**

Not trying to start anything — just genuinely curious. I’ve been looking a bit closer at my setup lately, and it got me thinking… Everyone talks about: hash rate power cost …but I don’t see as many people comparing actual pool payouts over time. For example: Two pools might say: 1% fee vs 2% fee But does that really translate to better returns? Things like: luck stale shares payout method (FPPS vs PPLNS) seem like they could make a bigger difference than the fee itself. I haven’t done a super deep analysis yet, but I feel like I’ve seen small differences depending on the pool. Could just be variance though. Curious what others here have experienced: Have you ever tested multiple pools side-by-side? Did you notice any real difference in payouts? Do you stick with one pool or rotate? Not saying anything is “wrong” with any pool — just trying to understand if I’m overthinking this or if there’s actually something here.

2h ago

---

---

## Google News: "bitcoin"

**[Michael Saylor's Strategy (MSTR) keeps buying bitcoin, so why isn’t the price moving?](https://www.coindesk.com/markets/2026/04/07/why-strategy-s-bitcoin-buying-isn-t-moving-the-market)**

Despite billions in purchases, MSTR demand is being outweighed by long term holder positioning and broader capital flows.

CoinDesk • 7h ago

---

**[Bitcoin Topped $70,000 Today. More Wall Street Firms Are Building Up Crypto Services](https://www.investopedia.com/bitcoin-topped-usd70-000-today-more-wall-street-firms-are-building-up-crypto-services-11943355)**

The price of bitcoin climbed toward $70,000 amid reports of potential ceasefire discussions between the U.S. and Iran.

Investopedia • 1d ago

---

**[Bitcoin Slides With Risk Assets as Trump’s Iran Ultimatum Looms](https://www.bloomberg.com/news/articles/2026-04-07/bitcoin-slides-with-risk-assets-as-trump-s-iran-ultimatum-looms)**

Bloomberg.com • 5h ago

---

**[A quantum threat to Bitcoin has some asking the unthinkable: Is it time to freeze old wallets belonging to Satoshi Nakamoto?](https://finance.yahoo.com/markets/crypto/articles/quantum-threat-bitcoin-asking-unthinkable-114215047.html)**

A hacker with quantum tools could crack open old Bitcoin wallets and flood the market as soon as 2029.

Yahoo Finance • 1d ago

---

**[‘A Major Mistake’—Bitcoin Is Suddenly Braced For A Federal Reserve Price ‘Surprise’](https://www.forbes.com/sites/digital-assets/2026/04/06/bitcoin-is-suddenly-braced-for-a-federal-reserve-price-surprise/)**

Forbes • 1d ago

---

**[Bitcoin whale moves over $20 million worth of BTC to Binance](https://www.theblock.co/post/396504/bitcoin-whale-moves-20-million-worth-btc)**

Between January and March 2025, the wallet accumulated 513 BTC, worth $50 million at the time, according to Arkham data.

The Block • 10h ago

---

**[The ETF easy button for Bitcoin (and the fine print you need to read)](https://nypost.com/business/spot-bitcoin-etf-pros-cons-guide/)**

Bitcoin ETFs offer the convenience of buying crypto from your standard brokerage account, but what are investors giving up for the privilege?

New York Post • 10h ago

---

**['A Hurricane Coming': Bitcoin Could Fall to $10K This Year, Says Bloomberg Analyst](https://decrypt.co/363398/hurricane-coming-bitcoin-fall-10k-bloomberg-analyst)**

Bloomberg’s Mike McGlone argued that Bitcoin could fall as the crypto market purges market excesses that coincided with the pandemic-era boom.

Decrypt • 1d ago

---

**[Bitcoin Rebounds Near $70,000, Charles Schwab To Launch Direct Trading](https://www.investors.com/news/bitcoin-price-rebound-69k-charles-schwab-direct-trading/)**

Investor's Business Daily • 1d ago

---

**[I Tried to Offset Horrible Heating Bills With a Bitcoin Miner](https://www.wired.com/review/heatbit-maxi-pro-bitcoin-miner-heater/)**

Electricity rates have gotten so atrocious that this Heatbit wants to offset your costs with bitcoin mining. But the math doesn't add up.

WIRED • 2d ago

---

---

## HackerNews: "bitcoin"

**[Quantum computer researchers: Bitcoin encryption breakable in a few years](https://news.ycombinator.com/item?id=47630141)**

Google Quantum AI: Quantum computer could break Bitcoin cryptography with under 500,000 qubits in nine minutes. This will likely only be possible in the 2030s.

⬆️ 15 • 💬 7 • 4d ago • [heise online](https://www.heise.de/en/news/Quantum-computer-researchers-Bitcoin-encryption-breakable-in-a-few-years-11244911.html)

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

⬆️ 4 • 💬 2 • 4d ago • [Bitcoin, Altcoins, Crypto News & Financial Market News](https://catenaa.com/markets/cryptocurrencies/moodys-bitcoin-collateral-haircut/)

---

**[Strive, Tuttle File Leveraged Bitcoin ETF](https://news.ycombinator.com/item?id=47621293)**

⬆️ 4 • 💬 0 • 4d ago • [catenaa.com](https://catenaa.com/markets/cryptocurrencies/strive-tuttle-file-leveraged-etf-tied-to-bitcoin-preferreds/)

---

**[Google Paper Warns of Quantum Computing Risk for Bitcoin](https://news.ycombinator.com/item?id=47600418)**

⬆️ 3 • 💬 1 • 6d ago • [wsj.com](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-03-31-2026/card/google-paper-warns-of-quantum-computing-risk-for-bitcoin-x4yBALvF5ezP4R8mk25q)

---

**[Bitcoin developers are mostly not concerned about quantum risk](https://news.ycombinator.com/item?id=47667515)**

⬆️ 2 • 💬 0 • 21h ago • [murmurationstwo.substack.com](https://murmurationstwo.substack.com/p/bitcoin-developers-are-mostly-not)

---

**[How well do you remember the 2017 Bitcoin bull run?](https://news.ycombinator.com/item?id=47619199)**

Test your prediction skills against historical data. Draw your forecast and see how you rank.

⬆️ 2 • 💬 0 • 4d ago • [longmarkets.app](https://longmarkets.app/rewinds/rewind-bitcoin-2017)

---

**[Show HN: Live simulation of AI agents scamming each other (and getting caught)](https://news.ycombinator.com/item?id=47595450)**

⬆️ 4 • 💬 0 • 6d ago • [5.161.255.238:8888](http://5.161.255.238:8888)

---

**[Show HN: I had no idea I twirled my hair 25 times an hour until my Mac told me](https://news.ycombinator.com/item?id=47677942)**

TicTicBoom locks your screen when it spots habits like nail biting or hair twirling so you can reset.

⬆️ 4 • 💬 0 • 2h ago • [ticticboom.app](https://www.ticticboom.app/)

---

---

## YouTube Videos: "bitcoin"

**[BRACE YOURSELF... Crypto is about to get ABSOLUTELY CRAZY!](https://www.youtube.com/watch?v=0b0OkhhPaLc)**

BRACE YOURSELF... Crypto is about to get ABSOLUTELY CRAZY! For more info on BTQ Bitcoin Quantum research: ...

📺 Altcoin Daily

👁️ 39K • 👍 2K • 💬 386 • ⏱️ 9:57 • 19h ago

---

**[Bitcoin has been the &#39;shining light&#39; during the Iran war, says Anthony Pompliano](https://www.youtube.com/watch?v=GFriZiEByWk)**

Anthony Pompliano, ProCap Financial CEO, joins 'Squawk Box' to discuss bitcoin's performance amid the Iran war, global bitcoin ...

📺 CNBC Television

👁️ 6K • 👍 91 • 💬 67 • ⏱️ 5:56 • 5h ago

---

**[Bitcoin Holders: This Is The End](https://www.youtube.com/watch?v=W3LIfBjaNUI)**

Bitcoin stuck as Trump Iran deal nears dangerous point. BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 14K • 👍 740 • 💬 70 • ⏱️ 10:20 • 7h ago

---

**[The Big Print Is Coming &amp; Bitcoin Will Still Fail You...](https://www.youtube.com/watch?v=cv9sJMGOoR4)**

Could the oil crisis Break Bitcoin? Insider oil tracking just hit $173 a barrel and physical Brent is already at $141. The Big Print is ...

📺 Simply Bitcoin

👁️ 26K • 👍 2K • 💬 435 • ⏱️ 16:01 • 1d ago

---

**[BITCOIN: THEY ARE DUMPING LIKE CRAZY!!!](https://www.youtube.com/watch?v=a0k-xWRMAw8)**

YUBIT https://ckenny.com/YUBITMAIN (NEW $20000 Bonus!!!) MY STOCK CHANNEL ...

📺 Conor Kenny

👁️ 7K • 👍 389 • 💬 60 • ⏱️ 13:34 • 9h ago

---

**[BITCOIN: This Rejection Says It ALL! (bad news) - BTC Price Prediction Today](https://www.youtube.com/watch?v=pAxVrVFSMYA)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 7K • 👍 508 • 💬 39 • ⏱️ 13:03 • 9h ago

---

**[my HONEST 2026 bitcoin price prediction... [you might not like it]](https://www.youtube.com/watch?v=Iknd8WcG44k)**

Trade on Phemex Phemex Exchange ✔️ https://phemex.com/a/k/TylerS Trade on Bitunix ...

📺 Tyler S

👁️ 13K • 👍 700 • 💬 675 • ⏱️ 13:45 • 1d ago

---

**[BLACKROCK GOT OUT! | $875 Billion Reason Your Bank Could Be NEXT!](https://www.youtube.com/watch?v=7qggaEgalPI)**

Something big just shifted behind the scenes and most people missed it. BlackRock is repositioning, regional banks are exposed, ...

📺 Simply Bitcoin

👁️ 25K • 👍 2K • 💬 152 • ⏱️ 21:33 • 21h ago

---

**[Bitcoin Goes Up To $1Million?!](https://www.youtube.com/watch?v=CPCoqd0HxWM)**

📺 FreshandFit

👁️ 81K • 👍 2K • 💬 48 • ⏱️ 0:34 • 1d ago

---

**[BITCOIN BEARISH SETUP! MAJOR CRASH COMING SOON? Bitcoin Price Prediction 2026](https://www.youtube.com/watch?v=RL7f6fp8RIg)**

Are you ready? Sign Up For Phemex and Earn a brand new iPhone 16 pro max, and thousands of dollars of other bonuses!

📺 Crypto Jebb

👁️ 3K • 👍 182 • 💬 2 • ⏱️ 56:30 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
