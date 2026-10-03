---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-10-03T06:05:25.963504+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- cryptocurrency
- social
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** October 03, 2026 at 06:05 UTC  
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

### $2,680.53

---

## Ethereum Chart

**24h:** -2.1%  
**7d:** -0.4%  
**30d:** +9.1%  
**90d:** +48.9%  
**1y:** -40.3%  

---

## Ethereum Market Stats

**Market Cap:** $327.05B
Rank #2

**Circulating Supply:** 122,101,617 ETH
No max supply

**All-Time High:** $4,946.05
-45.8%

**All-Time Low:** $0.43
+618523.5%

---

## Reddit: r/ethereum

**[Daily General Discussion September 30, 2026](https://www.reddit.com/r/ethereum/comments/1wtw77f/daily_general_discussion_september_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Is a global voting system possible?](https://www.reddit.com/r/ethereum/comments/1wu9p5h/is_a_global_voting_system_possible/)**

a global government I would support system based on existing technological solutions. the expulsion of incompetence, lies and manipulation to choose our own destiny. voting is done over the phone. each person 1 vote. biometric fingerprint. decentralized. using advanced cryptography. transparency. for global issues, all locals vote for local ones. formation of global expert councils. their role is to provide an analysis and evaluation of the proposal. members are chosen exclusively on the basis of expertise and competence in given professions. basic 4 branches: Society Ethical-legal group Psychological-sociological group Cultural and educational group Resources Ecological-climatic group Economic and resource group Logistic-operational group Technology Technical and engineering group Digital-cybernetic group Science Logical-mathematical group Medical-biological group the council's role is to adopt, give, and formulate clear and transparent proposals for solving problems or situations every decision they make is transparent. with minutes for the archive. presenting a problem or proposing a solution is available to all residents. cognitive ability test before submitting a proposal each proposal must pass the acceptance threshold. ethical, logical, mathematical. technical let's say we have 10 valid suggestions for a solution.. the global advice gives a score of 1 or 0 each of those 10 groups. the ethics council gives the final assessment in the event that several proposals have the same number of positives. the proposal with the most positives goes to a global referendum every voter, i.e. individual or group, has the right of veto. they are obliged to present a valid counter-argument in the shortest possible time. any veto attempt that is driven by ego vanity or the desire for power is automatically rejected. algorithmic assessment. open source. mandatory system calibration, ethical, logical, mathematical. plus a decentralized network of jurors chosen on the basis of expertise. randomly selected. a valid argument is voted against the proposal of the council. in case of adoption of the argument, the proposal is rejected. if the vote is 50-50%, both sides have 24 hours to present new insights the vote is repeated. voting is optional. the possibility of voting is. it is not a problem for me that people wiser than me decide about our fate and social vector. as long as they ask all of us, because ultimately it concerns all of us I support expertise and objectivity as well as the diversity of the local community.

2d ago

---

**[guys is anyone else exhausted by the L2 fragmentation?](https://www.reddit.com/r/ethereum/comments/1wudnwc/guys_is_anyone_else_exhausted_by_the_l2/)**

spent an hour moving eth around mainnet gas is still insane for simple swaps, and then you bridge to an L2 and the liquidity is half what you expect its a mess i love ethereum but its becoming a chore to actually use. ngl i still keep some eth on gemini just to have a clean way to stake and trade without thinking about gas or which rollup im on. centralization sucks but my sanity is worth something. back to staring at etherscan

2d ago

---

**[Running an Ethereum Node and Validator on RISC-V hardware](https://www.reddit.com/r/ethereum/comments/1wt8peh/running_an_ethereum_node_and_validator_on_riscv/)**

About 2 years ago RISC-V hardware got powerful enough to do initial tests for running an Ethereum node on such hardware. As expected, the speed wasn't quite there yet, but we started getting some clients ready, submitted PRs, got a Devcon talk and even got some core devs interested in it. There were steady improvements in the last 2 years. We were able to run nodes for larger test networks until we managed to sync mainnet about a year ago. But only barely so. Technically it stayed in sync, but practically it was always 1-2 slots behind. This changed this summer with the newest hardware iteration. I managed to run a fully synced Ethereum node on a RISC-V single board computer (Spacemit K3 CoM260). The validator running through that node attested flawlessly and correctly attested head votes, even right after epoch boundaries. The node still is a bit slower than my usual NUCs, but that is not surprising as the board has about the power of a Raspberry Pi 5. In my impression the bottleneck still is the consensus workload. Reducing the number of individual validators helped here quite a bit. The execution client has some spare power to be able to handle gas limit increases and thanks to ePBS it should get more time per slot to do its duties anyway. So I hope my node can handle the workload for 1 or 2 more years. Currently 2 Consensus clients run out of the box (Nimbus and Lighthouse). On the execution side, geth has always just worked. Now, Ethrex is also running, even though the initial sync is a bit more involved because the board has a 'only' 32 GB of RAM. But when Ethrex works it works perfectly and is very resource efficient. It is great to see that a second execution client now runs on RISC-V hardware. Grandine builds, but fails to run. I did not have the time yet to investigate as to why. Eth-docker also works, but does not support all client pairs just yet. As RISC-V is an open standard, I see these CPUs to be able to capture a junk of the consumer market in the long run. It already happens with a lot of lower cost applications, where RISC-V CPUs replace more expensive ARM and other chips. There are also well funded companies building servers and consumer PCs using RISC-V CPUs There are also a some who specialize on building accelerator cards using the RISC-V standard. We will have to see if RISC-V CPUs manage to capture large parts of the market. If it it happens it will take years (~ a decade). With the direction Ethereum is taking with zk proving the network, I definitely see a possibility that smaller nodes will run on low cost hardware. RISC-V CPUs have a clear advantage here. Currently with the resource usage of an Ethereum node, combined with the RAM and SSD prices, the price advantage a RISC-V CPU can have does not really matter. I expect it will in the long run though. For people wanting to know more about the progress, here are some reddit posts in chronological order: First post in 2024: https://www.reddit.com/r/ethfinance/comments/1ewn8dw/daily_general_discussion_august_20_2024/lj2anr4/ Announcement of the Devcon talk we gave in Bangkok in 2024: https://www.reddit.com/r/ethfinance/comments/1gn3k7p/daily_general_discussion_november_9_2024/lw85ry2/ First person to run execution and consensus client simultaneously on RISC-V hardware (two boards) in 2025 for Ethereum mainnet. They later improved Lighthouse to support RISC-V out of the box: https://www.reddit.com/r/RISCV/comments/1j5uqrs/ethereum_node_on_riscv_yes_its_possible/ Summary of the progress in 2025/2026 with first node running on one board: https://old.reddit.com/r/ethereum/comments/1t9tdqb/daily_general_discussion_may_11_2026/ol54wr4/

3d ago

---

**[Daily General Discussion September 29, 2026](https://www.reddit.com/r/ethereum/comments/1wt16ck/daily_general_discussion_september_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[Glamsterdam Testnet Announcement | Ethereum Foundation Blog](https://www.reddit.com/r/ethereum/comments/1wt0x0n/glamsterdam_testnet_announcement_ethereum/)**

Glamsterdam follows the Fusaka upgrade, advancing Ethereum's L1 scaling roadmap with enshrined proposer-builder separation, block-level access lists, and...

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/09/17/glamsterdam-testnet-announcement) • 4d ago

---

**[Daily General Discussion September 28, 2026](https://www.reddit.com/r/ethereum/comments/1ws5jwv/daily_general_discussion_september_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

5d ago

---

**[Compute and Consensus](https://www.reddit.com/r/ethereum/comments/1wsig29/compute_and_consensus/)**

🔗 [akeysfamoffice.substack.com](https://akeysfamoffice.substack.com/p/compute-and-consensus?r=95seez&utm_campaign=post-expanded-share&utm_medium=web) • 4d ago

---

**[The cryptographic world computer | Vitalik](https://www.reddit.com/r/ethereum/comments/1ws2z7z/the_cryptographic_world_computer_vitalik/)**

🔗 [vitalik.eth.limo](https://vitalik.eth.limo/general/2026/09/27/the_cryptographic_world_computer.html) • 5d ago

---

**[Daily General Discussion September 27, 2026](https://www.reddit.com/r/ethereum/comments/1wrbb9b/daily_general_discussion_september_27_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

6d ago

---

---

## Google News: "ethereum"

**[Introducing zkAPI: private usage credits for any API](https://blog.ethereum.org/2026/10/01/introducing-zkapi)**

tl;dr: zkAPI lets you pay for a metered API without being known. Deposit credits into an Ethereum vault once, then authorize bounded usage with zero-knowledge...

ethereum.org • 1d ago

---

**[Once a $2.3 Billion Network, Ethereum Layer-2 Blast Is Shutting Down](https://decrypt.co/379972/ethereum-layer-2-blast-shutting-down)**

Blast said operating costs now exceed the revenue its Ethereum layer-2 generates and asked users to withdraw their assets to mainnet.

Decrypt News • 12h ago

---

**[Bitcoin and ethereum prices today, Thursday, October 1, 2026: Not much price movement this morning, but Citigroup says that will change](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-thursday-october-1-2026-not-much-price-movement-this-morning-but-citigroup-says-that-will-change-113313201.html)**

Bitcoin opened at $83,566.34 on Thursday, October 1, 2026, down 0.1% from Wednesday's open. As of 7:20 a.m. ET this morning, bitcoin moved up to $83,805.02. Ethereum opened at $2,684.27 today, up 0.3% from Wednesday's opening price. The price of ethereum moved up further to $2,695.01 as of 7:20 a.m. ET.

Yahoo Finance • 1d ago

---

**[Bitcoin, Ethereum, XRP Pare Earlier Gains as Sentiment Turns Negative](https://www.tradingview.com/news/benzinga:c06a50342094b:0-bitcoin-ethereum-xrp-pare-earlier-gains-as-sentiment-turns-negative/)**

Bitcoin CRYPTO:BTCUSD has pared gains from Friday morning trading, selling off $84,600 after a rally to $86,500 into a weaker-than-expected jobs numbers report.Ethereum CRYPTO:ETHUSD and XRP CRYPTO:XRPUSD followed the reversal, with social sentiment flipping sharply negative, according to data prov…

TradingView • 12h ago

---

**[DOGE price: Dogecoin gets Ethereum-style testnet for trading, lending and stablecoins](https://www.coindesk.com/tech/2026/10/01/dogecoin-gets-defi-testnet-as-dogeos-bets-miners-will-eventually-secure-its-apps)**

DogeOS wants to turn DOGE into more than a payments and speculation asset, but its applications still rely on selected operators rather than Dogecoin miners.

coindesk.com • 2d ago

---

**[MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)**

MetaMask is remediating an infrastructure security incident and exiting affected Ethereum validators; it reports no immediate wallet threat.

The Hacker News • 2d ago

---

**[Ethereum staking reward burn proposal EIP-8363 pulled from Hegota upgrade](https://www.theblock.co/news/ecosystems/2026-10-01-ethereum-staking-reward-burn-proposal-eip-8363-pulled-hegota-upgrade-417419)**

Co-author and Ethereum France president Jérôme de Tychey said industry feedback convinced him the issuance change needs its own process, with forums and workshops planned through EthCC in April.

The Block • 1d ago

---

**[New Crypto: Pepeto Announces $11.16 While Ethereum Price Prediction Points to $6,000 and Traders Hunt the Next Dogecoin](https://markets.businessinsider.com/news/stocks/new-crypto-pepeto-announces-11-16-while-ethereum-price-prediction-points-to-6-000-and-traders-hunt-the-next-dogecoin-1036593848)**

Dubai, UAE, Oct.  02, 2026  (GLOBE NEWSWIRE) -- New crypto Pepeto announces fresh presale numbers this week: funding past $11.16 million, holders ...

markets.businessinsider.com • 13h ago

---

**[Ethereum is preparing a 200 million gas push as its Layer 1 scaling strategy accelerates](https://cryptoslate.com/ethereum-is-preparing-a-200-million-gas-push-as-its-layer-1-scaling-strategy-accelerates/)**

Ethereum's Oct. 6 Glamsterdam test will show whether validators coordinate around a target more than three times today’s 60 million default.

CryptoSlate • 1d ago

---

**[Current price of Ethereum for Sept. 30, 2026](https://fortune.com/article/price-of-ethereum-09-30-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 2d ago

---

---

## YouTube Videos: "ethereum"

**[BITCOIN DUMP: Exact Trading Strategy Exposed (WARNING)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=LfIbptPM1KM)**

BITCOIN DUMP: Exact Trading Strategy Exposed (WARNING)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 5K • 👍 276 • 💬 44 • ⏱️ 26:47 • 6h ago

---

**[Why I Think Ethereum Can Reach $16K This Bull Run](https://www.youtube.com/watch?v=PlLT0t3MQbk)**

Join my community | Work with me directly: https://whop.cryptoarchieyt.com/redirect.php?link=youtube_long_form_v46 ______ I ...

📺 Crypto Archie

👁️ 4K • 👍 58 • 💬 9 • ⏱️ 5:39 • 2d ago

---

**[Uptober Begins?🚀Tom Lee Calls For $50k ETH Potential 🔥](https://www.youtube.com/watch?v=LG35gk-PH2o)**

Tom Lee says the bull run is officially on and Uptober is here, with a path to $50K ETH this cycle. We break down his ETH 10x call, ...

📺 Paul Barron Network

👁️ 107K • 👍 2K • 💬 217 • ⏱️ 12:18 • 1d ago

---

**[Jack Mallers Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [2026 New Prediction]](https://www.youtube.com/watch?v=AV0igI0P9SE)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 9K • 👍 192 • 💬 4 • ⏱️ 19:58 • 1d ago

---

**[#1 Altcoin Right Now | Bitcoin &amp; Ethereum Bull Run Update](https://www.youtube.com/watch?v=OBnxZ7vDR5I)**

Join my community | Work with me directly: https://whop.cryptoarchieyt.com/redirect.php?link=youtube_long_form_v47 ______ ...

📺 Crypto Archie

👁️ 3K • 👍 78 • ⏱️ 10:16 • 16h ago

---

**[🔥 Ethereum Is Waking Up - ETH Crypto Analysis](https://www.youtube.com/watch?v=pfdpDbYgAnM)**

Automatic Copy Trading: https://the-bitcoin-strategy.com/r/dREosge4 Ask Gerhard AI: mybtcguy.com My Chart Software: ...

📺 Bitcoin Strategy

👁️ 8K • 👍 107 • 💬 15 • ⏱️ 10:17 • 1d ago

---

**[XRP AND ETH SENTIMENT CRASHES! #xrp #ethereum #crypto](https://www.youtube.com/watch?v=9p2Y9LFqzJg)**

📺 CryptoWendyO

👁️ 3K • 👍 225 • 💬 3 • ⏱️ 1:58 • 5h ago

---

**[Ethereum Just BROKE OUT.. I Moved My Stop!!](https://www.youtube.com/watch?v=FQMnlrMqoyA)**

FeeDrip - Get up to 67% Back, Daily on Your Trading Fees https://marzell.org/feedrip Ethereum (ETH) just broke out of the ...

📺 Marzell Crypto

👁️ 516 • 👍 17 • 💬 7 • ⏱️ 3:08 • 15h ago

---

**[Bitcoin, XRP &amp; Ethereum Are Part Of The Largest Wealth Transfer In Human History](https://www.youtube.com/watch?v=8q8z7iZikUo)**

Its estimated that by the year 2040 corporate landlords will own most, if not all of single family homes and apartments around the ...

📺 Money Rules - Investing Tips 

👁️ 34K • 👍 2K • 💬 491 • ⏱️ 19:06 • 1d ago

---

**[Ethereum Breaks Bear Pattern: Juicy Investment Opportunity!](https://www.youtube.com/watch?v=ppKb5RCnrB0)**

Ethereum has broken its weekly bear pattern, outperforming Bitcoin. We've been watching it break highs for weeks. This is a prime ...

📺 Crypto School - Brian Longest

👁️ 266 • 👍 3 • ⏱️ 0:30 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
