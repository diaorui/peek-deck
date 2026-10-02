---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-10-02T04:25:39.116010+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- cryptocurrency
- videos
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** October 02, 2026 at 04:25 UTC  
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

### $2,686.16

---

## Ethereum Chart

**24h:** +0.6%  
**7d:** +1.4%  
**30d:** +9.1%  
**90d:** +53.3%  
**1y:** -39.3%  

---

## Ethereum Market Stats

**Market Cap:** $333.46B
Rank #2

**Circulating Supply:** 122,098,690 ETH
No max supply

**All-Time High:** $4,946.05
-44.8%

**All-Time Low:** $0.43
+630457.1%

---

## Reddit: r/ethereum

**[Daily General Discussion September 30, 2026](https://www.reddit.com/r/ethereum/comments/1wtw77f/daily_general_discussion_september_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[Is a global voting system possible?](https://www.reddit.com/r/ethereum/comments/1wu9p5h/is_a_global_voting_system_possible/)**

a global government I would support system based on existing technological solutions. the expulsion of incompetence, lies and manipulation to choose our own destiny. voting is done over the phone. each person 1 vote. biometric fingerprint. decentralized. using advanced cryptography. transparency. for global issues, all locals vote for local ones. formation of global expert councils. their role is to provide an analysis and evaluation of the proposal. members are chosen exclusively on the basis of expertise and competence in given professions. basic 4 branches: Society Ethical-legal group Psychological-sociological group Cultural and educational group Resources Ecological-climatic group Economic and resource group Logistic-operational group Technology Technical and engineering group Digital-cybernetic group Science Logical-mathematical group Medical-biological group the council's role is to adopt, give, and formulate clear and transparent proposals for solving problems or situations every decision they make is transparent. with minutes for the archive. presenting a problem or proposing a solution is available to all residents. cognitive ability test before submitting a proposal each proposal must pass the acceptance threshold. ethical, logical, mathematical. technical let's say we have 10 valid suggestions for a solution.. the global advice gives a score of 1 or 0 each of those 10 groups. the ethics council gives the final assessment in the event that several proposals have the same number of positives. the proposal with the most positives goes to a global referendum every voter, i.e. individual or group, has the right of veto. they are obliged to present a valid counter-argument in the shortest possible time. any veto attempt that is driven by ego vanity or the desire for power is automatically rejected. algorithmic assessment. open source. mandatory system calibration, ethical, logical, mathematical. plus a decentralized network of jurors chosen on the basis of expertise. randomly selected. a valid argument is voted against the proposal of the council. in case of adoption of the argument, the proposal is rejected. if the vote is 50-50%, both sides have 24 hours to present new insights the vote is repeated. voting is optional. the possibility of voting is. it is not a problem for me that people wiser than me decide about our fate and social vector. as long as they ask all of us, because ultimately it concerns all of us I support expertise and objectivity as well as the diversity of the local community.

1d ago

---

**[guys is anyone else exhausted by the L2 fragmentation?](https://www.reddit.com/r/ethereum/comments/1wudnwc/guys_is_anyone_else_exhausted_by_the_l2/)**

spent an hour moving eth around mainnet gas is still insane for simple swaps, and then you bridge to an L2 and the liquidity is half what you expect its a mess i love ethereum but its becoming a chore to actually use. ngl i still keep some eth on gemini just to have a clean way to stake and trade without thinking about gas or which rollup im on. centralization sucks but my sanity is worth something. back to staring at etherscan

1d ago

---

**[Running an Ethereum Node and Validator on RISC-V hardware](https://www.reddit.com/r/ethereum/comments/1wt8peh/running_an_ethereum_node_and_validator_on_riscv/)**

About 2 years ago RISC-V hardware got powerful enough to do initial tests for running an Ethereum node on such hardware. As expected, the speed wasn't quite there yet, but we started getting some clients ready, submitted PRs, got a Devcon talk and even got some core devs interested in it. There were steady improvements in the last 2 years. We were able to run nodes for larger test networks until we managed to sync mainnet about a year ago. But only barely so. Technically it stayed in sync, but practically it was always 1-2 slots behind. This changed this summer with the newest hardware iteration. I managed to run a fully synced Ethereum node on a RISC-V single board computer (Spacemit K3 CoM260). The validator running through that node attested flawlessly and correctly attested head votes, even right after epoch boundaries. The node still is a bit slower than my usual NUCs, but that is not surprising as the board has about the power of a Raspberry Pi 5. In my impression the bottleneck still is the consensus workload. Reducing the number of individual validators helped here quite a bit. The execution client has some spare power to be able to handle gas limit increases and thanks to ePBS it should get more time per slot to do its duties anyway. So I hope my node can handle the workload for 1 or 2 more years. Currently 2 Consensus clients run out of the box (Nimbus and Lighthouse). On the execution side, geth has always just worked. Now, Ethrex is also running, even though the initial sync is a bit more involved because the board has a 'only' 32 GB of RAM. But when Ethrex works it works perfectly and is very resource efficient. It is great to see that a second execution client now runs on RISC-V hardware. Grandine builds, but fails to run. I did not have the time yet to investigate as to why. Eth-docker also works, but does not support all client pairs just yet. As RISC-V is an open standard, I see these CPUs to be able to capture a junk of the consumer market in the long run. It already happens with a lot of lower cost applications, where RISC-V CPUs replace more expensive ARM and other chips. There are also well funded companies building servers and consumer PCs using RISC-V CPUs There are also a some who specialize on building accelerator cards using the RISC-V standard. We will have to see if RISC-V CPUs manage to capture large parts of the market. If it it happens it will take years (~ a decade). With the direction Ethereum is taking with zk proving the network, I definitely see a possibility that smaller nodes will run on low cost hardware. RISC-V CPUs have a clear advantage here. Currently with the resource usage of an Ethereum node, combined with the RAM and SSD prices, the price advantage a RISC-V CPU can have does not really matter. I expect it will in the long run though. For people wanting to know more about the progress, here are some reddit posts in chronological order: First post in 2024: https://www.reddit.com/r/ethfinance/comments/1ewn8dw/daily_general_discussion_august_20_2024/lj2anr4/ Announcement of the Devcon talk we gave in Bangkok in 2024: https://www.reddit.com/r/ethfinance/comments/1gn3k7p/daily_general_discussion_november_9_2024/lw85ry2/ First person to run execution and consensus client simultaneously on RISC-V hardware (two boards) in 2025 for Ethereum mainnet. They later improved Lighthouse to support RISC-V out of the box: https://www.reddit.com/r/RISCV/comments/1j5uqrs/ethereum_node_on_riscv_yes_its_possible/ Summary of the progress in 2025/2026 with first node running on one board: https://old.reddit.com/r/ethereum/comments/1t9tdqb/daily_general_discussion_may_11_2026/ol54wr4/

2d ago

---

**[Daily General Discussion September 29, 2026](https://www.reddit.com/r/ethereum/comments/1wt16ck/daily_general_discussion_september_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Glamsterdam Testnet Announcement | Ethereum Foundation Blog](https://www.reddit.com/r/ethereum/comments/1wt0x0n/glamsterdam_testnet_announcement_ethereum/)**

Glamsterdam follows the Fusaka upgrade, advancing Ethereum's L1 scaling roadmap with enshrined proposer-builder separation, block-level access lists, and...

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/09/17/glamsterdam-testnet-announcement) • 2d ago

---

**[Daily General Discussion September 28, 2026](https://www.reddit.com/r/ethereum/comments/1ws5jwv/daily_general_discussion_september_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Compute and Consensus](https://www.reddit.com/r/ethereum/comments/1wsig29/compute_and_consensus/)**

🔗 [akeysfamoffice.substack.com](https://akeysfamoffice.substack.com/p/compute-and-consensus?r=95seez&utm_campaign=post-expanded-share&utm_medium=web) • 3d ago

---

**[The cryptographic world computer | Vitalik](https://www.reddit.com/r/ethereum/comments/1ws2z7z/the_cryptographic_world_computer_vitalik/)**

🔗 [vitalik.eth.limo](https://vitalik.eth.limo/general/2026/09/27/the_cryptographic_world_computer.html) • 4d ago

---

**[Daily General Discussion September 27, 2026](https://www.reddit.com/r/ethereum/comments/1wrbb9b/daily_general_discussion_september_27_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

---

## Google News: "ethereum"

**[Introducing zkAPI: private usage credits for any API](https://blog.ethereum.org/2026/10/01/introducing-zkapi)**

tl;dr: zkAPI lets you pay for a metered API without being known. Deposit credits into an Ethereum vault once, then authorize bounded usage with zero-knowledge...

ethereum.org • 9h ago

---

**[MetaMask exits Ethereum validators after attacker diverts staking rewards](https://www.coindesk.com/tech/2026/10/01/metamask-security-incident-forces-ethereum-staking-exits-with-lido-warning-of-lost-rewards)**

An Ethereum security researcher estimates about 0.36 ETH in rewards was diverted, while precautionary exits cover validators holding roughly 523,000 ETH.

CoinDesk • 20h ago

---

**[BMNR Stock Forms Golden Cross For First Time Since Bitmine’s Ethereum Pivot Rally](https://finance.yahoo.com/markets/stocks/articles/bmnr-stock-forms-golden-cross-170445383.html)**

The last time the 50-day line crossed above the 200-day was more than a year ago, when the company pivoted to buying Ethereum.

Yahoo Finance • 1d ago

---

**[Ethereum staking reward burn proposal EIP-8363 pulled from Hegota upgrade](https://www.theblock.co/news/ecosystems/2026-10-01-ethereum-staking-reward-burn-proposal-eip-8363-pulled-hegota-upgrade-417419)**

Co-author and Ethereum France president Jérôme de Tychey said industry feedback convinced him the issuance change needs its own process, with forums and workshops planned through EthCC in April.

The Block • 12h ago

---

**[MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)**

MetaMask is remediating an infrastructure security incident and exiting affected Ethereum validators; it reports no immediate wallet threat.

The Hacker News • 23h ago

---

**[Current price of Ethereum for Sept. 30, 2026](https://fortune.com/article/price-of-ethereum-09-30-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 1d ago

---

**[Citi Lifts 12-Month Bitcoin Target to $113K, Ethereum to $3K](https://decrypt.co/379808/citi-lifts-12-month-bitcoin-target-to-113k-ethereum-to-3k)**

The bank has revised its 12-month target for BTC up from $82K, though it remains about 10% below Bitcoin's October 2025 record.

Decrypt News • 16h ago

---

**[Cardano vs Ethereum: Which Smart Contract Platform Wins by 2030?](https://247wallst.com/investing/cryptocurrency/2026/09/29/cardano-vs-ethereum-which-smart-contract-platform-wins-by-2030/)**

Cardano has outperformed Ethereum over 90 days, yet Ethereum's market value is 35 times larger. Who wins Cardano vs. Ethereum by 2030?

247wallst.com • 2d ago

---

**[Hayes sets bullish Bitcoin, Ethereum predictions; crypto stocks jump](https://seekingalpha.com/news/4648479-hayes-sets-bullish-bitcoin-ethereum-predictions-crypto-stocks-jump)**

Arthur Hayes predicts Bitcoin could hit $1M by 2030 as an AI bubble drives liquidity, with ETH eyeing $10K.

Seeking Alpha • 1d ago

---

**[Ethereum-Based Stablecoin Issuer ENA Could Surge 600%: Standard Chartered](https://www.benzinga.com/crypto/cryptocurrency/26/09/62087026/ethereum-based-stablecoin-issuer-ena-could-surge-600-standard-chartered)**

Standard Chartered sees Ethena’s ENA reaching $2 by 2028, implying 614% upside and gains ahead of Bitcoin and Ethereum.

benzinga.com • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Uptober Begins?🚀Tom Lee Calls For $50k ETH Potential 🔥](https://www.youtube.com/watch?v=LG35gk-PH2o)**

Tom Lee says the bull run is officially on and Uptober is here, with a path to $50K ETH this cycle. We break down his ETH 10x call, ...

📺 Paul Barron Network

👁️ 74K • 👍 2K • 💬 178 • ⏱️ 12:18 • 10h ago

---

**[BITCOIN &amp; CRYPTO TRADING STRATEGY (Taking Profits Now)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=VcJqDJqq8AU)**

BITCOIN & CRYPTO TRADING STRATEGY (Taking Profits Now)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 2K • 👍 154 • 💬 39 • ⏱️ 23:33 • 3h ago

---

**[Why I Think Ethereum Can Reach $16K This Bull Run](https://www.youtube.com/watch?v=PlLT0t3MQbk)**

Join my community | Work with me directly: https://whop.cryptoarchieyt.com/redirect.php?link=youtube_long_form_v46 ______ I ...

📺 Crypto Archie

👁️ 3K • 👍 51 • 💬 8 • ⏱️ 5:39 • 1d ago

---

**[🔥 Ethereum Is Waking Up - ETH Crypto Analysis](https://www.youtube.com/watch?v=pfdpDbYgAnM)**

Automatic Copy Trading: https://the-bitcoin-strategy.com/r/dREosge4 Ask Gerhard AI: mybtcguy.com My Chart Software: ...

📺 Bitcoin Strategy

👁️ 2K • 👍 61 • 💬 9 • ⏱️ 10:17 • 8h ago

---

**[Bitcoin, XRP &amp; Ethereum Are Part Of The Largest Wealth Transfer In Human History](https://www.youtube.com/watch?v=8q8z7iZikUo)**

Its estimated that by the year 2040 corporate landlords will own most, if not all of single family homes and apartments around the ...

📺 Money Rules - Investing Tips 

👁️ 28K • 👍 2K • 💬 446 • ⏱️ 19:06 • 17h ago

---

**[Jack Mallers Just Said The UNTHINKABLE About Bitcoin &amp; Ethereum! [2026 New Prediction]](https://www.youtube.com/watch?v=AV0igI0P9SE)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 5K • 👍 167 • 💬 12 • ⏱️ 19:58 • 12h ago

---

**[Ethereum: I Sold at a LOSS.. Then Bought It Back!!](https://www.youtube.com/watch?v=yAjokNP-Qpg)**

FeeDrip (this video's sponsor) - part of your trading fees back, paid daily in USDT, no API keys https://marzell.org/feedrip ...

📺 Marzell Crypto

👁️ 234 • 👍 6 • 💬 1 • ⏱️ 3:13 • 6h ago

---

**[BTCS CEO Q&amp;A 2026 | Latest Ethereum Treasury Stock News | Top ETH Stocks to Watch | BTCS](https://www.youtube.com/watch?v=PCkzD7WRSKg)**

BTCS CEO Q&A 2026 | Latest Ethereum Treasury Stock News | Top ETH Stocks to Watch | BTCS This video was conducted on ...

📺 McNallie Money

👁️ 1K • 👍 102 • 💬 12 • ⏱️ 18:53 • 8h ago

---

**[Ethereum UPTOBER Is Here.. And I&#39;m Moving My Long!!](https://www.youtube.com/watch?v=KtyiGA7mlek)**

FeeDrip (this video's sponsor) - part of your trading fees back, paid daily in USDT, no API keys https://marzell.org/feedrip ...

📺 Marzell Crypto

👁️ 1K • 👍 15 • 💬 4 • ⏱️ 3:18 • 15h ago

---

**[BREAKING WALL STREET IS COMING! $10,000 ETHEREUM CALL?! XRP MILESTONE COULD SEND ALTCOINS CRAZY](https://www.youtube.com/watch?v=BAJpGVA8inA)**

BREAKING WALL STREET IS COMING! $10000 ETHEREUM CALL?! XRP MILESTONE COULD SEND ALTCOINS CRAZY Claim ...

📺 CryptoWendyO

👁️ 18K • 👍 563 • 💬 22 • ⏱️ 30:38 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
