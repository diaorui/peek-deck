---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-25T23:05:36.091538+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- social
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** April 25, 2026 at 23:05 UTC  
**HTML Version:** [ethereum.html](https://peekdeck.ruidiao.dev/ethereum.html)

---

## Table of Contents

1. [Ethereum Price](#ethereum-price)
2. [Ethereum Chart](#ethereum-chart)
3. [Ethereum Market Stats](#ethereum-market-stats)
4. [Reddit: r/ethereum](#reddit-rethereum)
5. [Google News: "ethereum"](#google-news-ethereum)
6. [YouTube Videos: "ethereum"](#youtube-videos-ethereum)

---

## Ethereum Price

### $2,319.83

---

## Ethereum Chart

**24h:** +0.1%  
**7d:** +2.5%  
**30d:** +16.3%  
**90d:** -20.9%  
**1y:** +27.3%  

---

## Ethereum Market Stats

**Market Cap:** $279.47B
Rank #2

**Circulating Supply:** 120,688,915 ETH
No max supply

**All-Time High:** $4,946.05
-53.2%

**All-Time Low:** $0.43
+534734.3%

---

## Reddit: r/ethereum

**[Etherscan officially recognized the 2016 Unicorn Meat token as an Ethereum Foundation contract, so I cracked and verified the Grinder source code](https://www.reddit.com/r/ethereum/comments/1svq7qu/etherscan_officially_recognized_the_2016_unicorn/)**

I wanted to share something interesting that happened recently. Etherscan added an info note to the Unicorn Meat token page that reads: "This token was created by Avsa of the Ethereum Foundation. Read more about it in this post." The link goes to a tweet from the official @ethereum account from April 1, 2016 announcing "the Unicorn Meat Grinder Smart Contract and Bribable DAO" by @avsa. For those who don't know the backstory: Alex Van de Sande (avsa) was one of Ethereum's earliest core team members. He built the Mist Browser, the Ethereum Wallet, and co-created ENS. In early 2016 he deployed a set of contracts as part of the ethereum.org tutorials, including the Unicorns token and the Unicorn Meat Grinder, a DAO that let you convert Unicorns into Unicorn Meat through on-chain governance. The contracts were deployed from his same wallet that deployed the Foundation Tip Jar, which Alex made on behalf of the Foundation to raise money and donors received Unicorn tokens. So the provenance chain is: same deployer address, multiple Etherscan-labeled EF contracts, and now an official Etherscan note confirming the connection. What makes this historically interesting: The Meat Grinder was one of the first DAOs on Ethereum, predating The DAO by months. It used a proposal and voting system where token holders could vote on actions like grinding Unicorns into Meat. It introduced one of the first token upgrade patterns. The Unicorn-to-Meat conversion was essentially a token migration mechanism, something that became standard practice years later. The contracts were based on the ethereum.org tutorials that avsa wrote to teach developers how to build on Ethereum. These tutorials were how an entire generation of Solidity developers learned the language. We've been working on documenting and verifying the source code of these contracts on EthereumHistory, including cracking the bytecode of contracts that were never verified on Etherscan. We recently launched a Collections feature that groups all contracts by their deployer, starting with avsa's 60 contracts and Vitalik's 66 contracts. We also recently cracked and verified the Meat Grinder's source code on Etherscan. The source had been sitting in avsa's public GitHub gist for 10 years but was never formally verified on-chain. The challenge was figuring out the exact compiler settings: these contracts predate Solidity 0.4, so there's no metadata hash in the bytecode to help identify the version. We had to work through early solc releases until we found that solc 0.2.1 with default optimization produced an exact byte-for-byte match against the on-chain runtime bytecode. Once confirmed, we submitted it to both Sourcify and Etherscan, so anyone can now read the original Solidity source directly on Etherscan and verify it themselves. It's a small thing, but these early contracts are historical artifacts. Having their source verified on-chain means the code is permanently readable and auditable, not just sitting in a gist that could disappear. If anyone is interested in Ethereum's early contract history, the provenance page has the full chain of evidence laid out, and EthereumHistory is an open platform where anyone can help document contracts.

25m ago

---

**[Daily General Discussion April 25, 2026](https://www.reddit.com/r/ethereum/comments/1sv2scg/daily_general_discussion_april_25_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

18h ago

---

**[anyone else getting paranoid about how centralized eth liquid staking has become lately](https://www.reddit.com/r/ethereum/comments/1svcywx/anyone_else_getting_paranoid_about_how/)**

been spending way too much time looking at the recent string of defi exploits and the amount of supply locked up in the same three lst platforms is honestly giving me anxiety. having that much of the network reliant on a few centralized points of failure makes me paranoid about massive tail risks. every time the market swings i find myself wanting to hedge this exposure, but the options are terrible. you either convert to fiat and trigger taxable events, or you play russian roulette with wrapped assets and multisig bridges that seem to get drained every other week. i went down a rabbit hole last night trying to find a way to secure my yields natively, maybe even hedging with digital gold or something stable, without fragmenting my liquidity across a dozen vulnerable front-ends. what are you guys actually doing to protect your bags long term? are we just stuck choosing between bare validator yields and accepting the centralized lst risk? curious if anyone has found a trust-minimized way to hedge this without leaving the ecosystem.

9h ago

---

**[JUST IN: Aave DAO Contributes 25,000 ETH To DeFi United](https://www.reddit.com/r/ethereum/comments/1suoxpi/just_in_aave_dao_contributes_25000_eth_to_defi/)**

Aave DAO offers to contribute 25,000 ETH toward DeFi United, a coordinated ecosystem recovery effort to restore the full backing of KelpDAO's rsETH. The coalition, which includes Lido, EtherFi, Ethena, Mantle, and others, aims to cover a ~75,081 ETH residual shortfall.

🔗 [Aave](https://governance.aave.com/t/arfc-rseth-incident-funding-update/24740) • 1d ago

---

**[Daily General Discussion April 24, 2026](https://www.reddit.com/r/ethereum/comments/1su63qw/daily_general_discussion_april_24_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Ethereal news weekly #20 | Etherealize: ETH is productive money, DeFi united effort to restore rsETH backing, Arbitrum security council froze exploiter ETH](https://www.reddit.com/r/ethereum/comments/1sueyao/ethereal_news_weekly_20_etherealize_eth_is/)**

Etherealize: ETH is productive money, DeFi united: effort to restore rsETH backing, Arbitrum security council froze exploiter ETH

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-20/) • 1d ago

---

**[the whole concept of DAOs is basically failing because we can't solve the sybil problem](https://www.reddit.com/r/ethereum/comments/1stujgt/the_whole_concept_of_daos_is_basically_failing/)**

honestly starting to get really cynical about the state of governance on eth right now. i was looking at some recent voting proposals and its just painfully obvious that everything is being manipulated by industrial scale airdrop farmers. The WHOLE web3 dream was supposed to be decentralized consensus and community ownership. but right now whoever spins up the most python scripts and funds 10,000 wallets automatically basically runs the show. it completely hollows out the actual community and makes governance a total joke the frustrating part is software-based sybil resistance just isnt working anymore. Things like gitcoin passport and on-chain activity scores are fine in theory, but the massive bot farms just automate the farming of those scores too now. it feels like we're backed into a corner where protocols will either have to force traditional KYC (which completely ruins the cypherpunk ethos of the network) or we have to rely on physical hardware solutions its crazy but tying wallets to a zero-knowledge biometric credential from something like an Orb is probably the only viable middle ground we have left. you basically get a cryptographic flag that proves you're a unique living person, but you never have to dox your actual government identity to a random multi-sig. it saves the anonymity but breaks the botnets. Im just so exhausted watching cool ecosystem projects get drained by automated scripts instead of rewarding real users. idk, maybe I'm just being pessimistic today but it really feels like until we fix this core human identity layer, all this governance and voting stuff is just us pretending.

2d ago

---

**[The Biggest Backer of Trump's Crypto Project Just Sued It for Fraud](https://www.reddit.com/r/ethereum/comments/1stvjxu/the_biggest_backer_of_trumps_crypto_project_just/)**

Justin Sun invested $45 million into World Liberty Financial. They froze his wallet, stripped his voting rights, and threatened to burn his tokens. Now he is taking them to federal court.

🔗 [DailyCoinPost](https://dailycoinpost.com/trump-world-liberty-financial-justin-sun-lawsuit/) • 2d ago

---

**[MyEtherWallet going all in on Tokenized Stock on Ethereum](https://www.reddit.com/r/ethereum/comments/1strji2/myetherwallet_going_all_in_on_tokenized_stock_on/)**

In the last few months MyEtherWallets been quietly rolling out updates to their products bringin tokenized stocks on Ethereum to the foreground. I think its very interesting timing for Ethereum in general with all the DEFI drama. This feels like crypto might be growing up a bit, and certainly exposing worldwide users to tokenized stocks on Ethereum has to be a bullish signal. Especially if it for srs investors in a buy and hold mentality and not some yolo on whateverCoin. Just did a tweet this morning about doing a bunch of free tokenized stocks on Ethereum and I am super here for it. Heres the tweet: https://x.com/myetherwallet/status/2047343412941377789?s=20

2d ago

---

**[Daily General Discussion April 23, 2026](https://www.reddit.com/r/ethereum/comments/1st94mc/daily_general_discussion_april_23_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Ethereum Foundation sells nearly $24 million of ETH to Tom Lee's Bitmine](https://www.theblock.co/post/398819/ethereum-foundation-sells-nearly-24-million-of-eth-to-tom-lees-bitmine)**

Bitmine Immersion also spent about $10 million when it bought 5,000 ETH from the Ethereum Foundation last month.

The Block • 1d ago

---

**[Bullish Ripple (XRP) Signals, Ethereum (ETH) Price Predictions, and More: Bits Recap, April 24](https://cryptopotato.com/bullish-ripple-xrp-signals-ethereum-eth-price-predictions-and-more-bits-recap-april-24/)**

Here's what's new and catching attention around XRP, ETH, and DOGE.

CryptoPotato • 23h ago

---

**[BitMine’s Tom Lee Sees Ethereum’s Price Reaching $250,000](https://finance.yahoo.com/markets/crypto/articles/bitmine-tom-lee-sees-ethereum-135000677.html)**

Tom Lee, the chairman of BitMine Immersion Technologies (NYSE: $BMNR) sees the price of Ethereum (CRYPTO: $ETH) eve...

Yahoo Finance • 2d ago

---

**[Is Owning Just Bitcoin and Ethereum Enough for a Crypto Portfolio?](https://www.fool.com/investing/2026/04/23/is-owning-just-bitcoin-and-ethereum-enough-for-a-c/)**

Simple portfolios can often outperform overly complicated ones.

The Motley Fool • 2d ago

---

**[Bitcoin Price Falls From 11-Week High. Why, Ethereum, XRP, Cryptos Are Dropping.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-crypto-iran-54088134)**

Barron's • 2d ago

---

**[Grayscale stakes 102,400 ETH via Ethereum Staking ETF, valued at $237M](https://cryptobriefing.com/grayscale-stakes-102400-eth-via-ethereum-staking-etf-valued-at-237m/)**

Grayscale staked 102,400 ETH worth $237M via its Ethereum Staking ETF. Ethereum reaching $10,000 by December 31, 2026 at 4% YES.

Crypto Briefing • 18h ago

---

**[XRP vs Ethereum: Which Digital Giant Will Explode to Make You the Most Money in 2026?](https://www.tipranks.com/news/xrp-vs-ethereum-which-digital-giant-will-explode-to-make-you-the-most-money-in-2026)**

TipRanks • 1d ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC holds gains, ETH eyes breakout, XRP defends key support](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-holds-gains-eth-eyes-breakout-xrp-defends-key-support-202604240334)**

Bitcoin (BTC), Ethereum (ETH) and Ripple (XRP) are supporting a constructive outlook on Friday after surging by 6%, 2% and 3% so far this week, respectively.

FXStreet • 1d ago

---

**[Kevin O'Leary Says 'Just Own Bitcoin And Ethereum' As Altcoins 'Never Came Back'](https://www.benzinga.com/crypto/cryptocurrency/26/04/52001824/kevin-oleary-says-just-own-bitcoin-and-ethereum-as-altcoins-never-came-back)**

Shark Tank star Kevin O&#8217;Leary said investors only need to own Bitcoin (CRYPTO: BTC) and Ethereum

Benzinga • 2d ago

---

**[Ethereum: Holds Bullish Structure](https://blockchain.news/flashnews/ethereum-holds-bullish-structure)**

Ethereum maintains bullish symmetrical triangle amid $2316.7 price, with key ranges over five years signaling potential upside despite bearish 4h trends.

blockchain.news • 38m ago

---

---

## YouTube Videos: "ethereum"

**[THEY ARE PREDICTING - $500K BITCOIN, $40K ETHEREUM, AND $50 XRP BY THIS DATE!](https://www.youtube.com/watch?v=DzdxhLkBDOo)**

THEY ARE PREDICTING - $500K BITCOIN, $40K ETHEREUM, AND $50 XRP BY THIS DATE! GET AUSTIN'S X1 ALGO ...

📺 Austin Hilton

👁️ 4K • 👍 324 • 💬 25 • ⏱️ 9:47 • 6h ago

---

**[ETHEREUM HOLDERS, THE SIGNAL IS FLASHING AGAIN (LAST TIME WE PUMPED FAST)](https://www.youtube.com/watch?v=iZd82wsW2zM)**

Welcome Back To The Channel! ✔️ https://fortisx.fi/kol/tylerhillyt ✔️ Deposit from $100: Get a 1% bonus Join The Trading ...

📺 Tyler Hill Crypto

👁️ 2K • 👍 153 • 💬 118 • ⏱️ 13:36 • 8h ago

---

**[Tom Lee: Ethereum&#39;s &#39;Surprise of the Year&#39; Just Started (2026 ETH Prediction](https://www.youtube.com/watch?v=iE8700MrZQY)**

"UNBELIEVABLE! Ethereum's About to Pull the Surprise of the Year": Tom Lee | (New Prediction 2026) Something is wrong with ...

📺 Library Of Wealth

👁️ 948 • 👍 43 • 💬 133 • ⏱️ 16:26 • 1d ago

---

**[Tom Lee :&quot;Why Ethereum Is Going To $50,000 Per Coin, 1 ETH Will Be Huge! | Eth Price 2026](https://www.youtube.com/watch?v=P131BOKYpf0)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 15K • 👍 448 • 💬 53 • ⏱️ 23:11 • 2d ago

---

**[⚠️ Ethereum&#39;s Dark Days](https://www.youtube.com/watch?v=qlSFMBC7YXs)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 3K • 👍 80 • 💬 19 • ⏱️ 8:31 • 1d ago

---

**[BITCOIN TRADERS ARE MAKING THE SAME MISTAKE!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=fDMBp4nJ_7E)**

BITCOIN TRADERS ARE MAKING THE SAME MISTAKE!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 3K • 👍 200 • 💬 76 • ⏱️ 19:39 • 5h ago

---

**[Ethereum Leading the Next Altcoin Repricing? Charts Say Yes](https://www.youtube.com/watch?v=CAWT4GcMcKE)**

Most people are declaring altcoins dead, but the crypto charts tell a completely different story. In this video, I compare Ethereum's ...

📺 Crypto Capital Venture

👁️ 9K • 👍 552 • 💬 144 • ⏱️ 13:20 • 1d ago

---

**[BE READY FOR THIS MOVE!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=L7uEUKqPQKM)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 165 • 👍 8 • 💬 2 • ⏱️ 4:34 • 14h ago

---

**[Why This Ethereum Rally Might Be a Setup for Lower Prices](https://www.youtube.com/watch?v=08DMA31tS9k)**

Ethereum is consolidating just below a descending trend line that has been with us since the October 2025 high. The market is ...

📺 More Crypto Online

👁️ 3K • 👍 218 • 💬 20 • ⏱️ 10:43 • 23h ago

---

**[Ethereum Price Prediction: How High Can Ethereum Go in This Bull Market?](https://www.youtube.com/watch?v=_q3y8BaT5uc)**

Ethereum has quietly become one of the most watched assets in this bull market cycle — and for good reason. In this video, we ...

📺 Sir Luis

👁️ 33 • 👍 2 • 💬 5 • ⏱️ 11:42 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
