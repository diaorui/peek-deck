---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-10-01T00:42:24.685168+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- news
- cryptocurrency
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** October 01, 2026 at 00:42 UTC  
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

### $2,682.40

---

## Ethereum Chart

**24h:** +0.5%  
**7d:** -0.3%  
**30d:** +12.3%  
**90d:** +50.7%  
**1y:** -40.1%  

---

## Ethereum Market Stats

**Market Cap:** $327.44B
Rank #2

**Circulating Supply:** 122,092,941 ETH
No max supply

**All-Time High:** $4,946.05
-45.8%

**All-Time Low:** $0.43
+619403.5%

---

## Reddit: r/ethereum

**[Daily General Discussion September 30, 2026](https://www.reddit.com/r/ethereum/comments/1wtw77f/daily_general_discussion_september_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

19h ago

---

**[Is a global voting system possible?](https://www.reddit.com/r/ethereum/comments/1wu9p5h/is_a_global_voting_system_possible/)**

a global government I would support system based on existing technological solutions. the expulsion of incompetence, lies and manipulation to choose our own destiny. voting is done over the phone. each person 1 vote. biometric fingerprint. decentralized. using advanced cryptography. transparency. for global issues, all locals vote for local ones. formation of global expert councils. their role is to provide an analysis and evaluation of the proposal. members are chosen exclusively on the basis of expertise and competence in given professions. basic 4 branches: Society Ethical-legal group Psychological-sociological group Cultural and educational group Resources Ecological-climatic group Economic and resource group Logistic-operational group Technology Technical and engineering group Digital-cybernetic group Science Logical-mathematical group Medical-biological group the council's role is to adopt, give, and formulate clear and transparent proposals for solving problems or situations every decision they make is transparent. with minutes for the archive. presenting a problem or proposing a solution is available to all residents. cognitive ability test before submitting a proposal each proposal must pass the acceptance threshold. ethical, logical, mathematical. technical let's say we have 10 valid suggestions for a solution.. the global advice gives a score of 1 or 0 each of those 10 groups. the ethics council gives the final assessment in the event that several proposals have the same number of positives. the proposal with the most positives goes to a global referendum every voter, i.e. individual or group, has the right of veto. they are obliged to present a valid counter-argument in the shortest possible time. any veto attempt that is driven by ego vanity or the desire for power is automatically rejected. algorithmic assessment. open source. mandatory system calibration, ethical, logical, mathematical. plus a decentralized network of jurors chosen on the basis of expertise. randomly selected. a valid argument is voted against the proposal of the council. in case of adoption of the argument, the proposal is rejected. if the vote is 50-50%, both sides have 24 hours to present new insights the vote is repeated. voting is optional. the possibility of voting is. it is not a problem for me that people wiser than me decide about our fate and social vector. as long as they ask all of us, because ultimately it concerns all of us I support expertise and objectivity as well as the diversity of the local community.

8h ago

---

**[guys is anyone else exhausted by the L2 fragmentation?](https://www.reddit.com/r/ethereum/comments/1wudnwc/guys_is_anyone_else_exhausted_by_the_l2/)**

spent an hour moving eth around mainnet gas is still insane for simple swaps, and then you bridge to an L2 and the liquidity is half what you expect its a mess i love ethereum but its becoming a chore to actually use. ngl i still keep some eth on gemini just to have a clean way to stake and trade without thinking about gas or which rollup im on. centralization sucks but my sanity is worth something. back to staring at etherscan

5h ago

---

**[Running an Ethereum Node and Validator on RISC-V hardware](https://www.reddit.com/r/ethereum/comments/1wt8peh/running_an_ethereum_node_and_validator_on_riscv/)**

About 2 years ago RISC-V hardware got powerful enough to do initial tests for running an Ethereum node on such hardware. As expected, the speed wasn't quite there yet, but we started getting some clients ready, submitted PRs, got a Devcon talk and even got some core devs interested in it. There were steady improvements in the last 2 years. We were able to run nodes for larger test networks until we managed to sync mainnet about a year ago. But only barely so. Technically it stayed in sync, but practically it was always 1-2 slots behind. This changed this summer with the newest hardware iteration. I managed to run a fully synced Ethereum node on a RISC-V single board computer (Spacemit K3 CoM260). The validator running through that node attested flawlessly and correctly attested head votes, even right after epoch boundaries. The node still is a bit slower than my usual NUCs, but that is not surprising as the board has about the power of a Raspberry Pi 5. In my impression the bottleneck still is the consensus workload. Reducing the number of individual validators helped here quite a bit. The execution client has some spare power to be able to handle gas limit increases and thanks to ePBS it should get more time per slot to do its duties anyway. So I hope my node can handle the workload for 1 or 2 more years. Currently 2 Consensus clients run out of the box (Nimbus and Lighthouse). On the execution side, geth has always just worked. Now, Ethrex is also running, even though the initial sync is a bit more involved because the board has a 'only' 32 GB of RAM. But when Ethrex works it works perfectly and is very resource efficient. It is great to see that a second execution client now runs on RISC-V hardware. Grandine builds, but fails to run. I did not have the time yet to investigate as to why. Eth-docker also works, but does not support all client pairs just yet. As RISC-V is an open standard, I see these CPUs to be able to capture a junk of the consumer market in the long run. It already happens with a lot of lower cost applications, where RISC-V CPUs replace more expensive ARM and other chips. There are also well funded companies building servers and consumer PCs using RISC-V CPUs There are also a some who specialize on building accelerator cards using the RISC-V standard. We will have to see if RISC-V CPUs manage to capture large parts of the market. If it it happens it will take years (~ a decade). With the direction Ethereum is taking with zk proving the network, I definitely see a possibility that smaller nodes will run on low cost hardware. RISC-V CPUs have a clear advantage here. Currently with the resource usage of an Ethereum node, combined with the RAM and SSD prices, the price advantage a RISC-V CPU can have does not really matter. I expect it will in the long run though. For people wanting to know more about the progress, here are some reddit posts in chronological order: First post in 2024: https://www.reddit.com/r/ethfinance/comments/1ewn8dw/daily_general_discussion_august_20_2024/lj2anr4/ Announcement of the Devcon talk we gave in Bangkok in 2024: https://www.reddit.com/r/ethfinance/comments/1gn3k7p/daily_general_discussion_november_9_2024/lw85ry2/ First person to run execution and consensus client simultaneously on RISC-V hardware (two boards) in 2025 for Ethereum mainnet. They later improved Lighthouse to support RISC-V out of the box: https://www.reddit.com/r/RISCV/comments/1j5uqrs/ethereum_node_on_riscv_yes_its_possible/ Summary of the progress in 2025/2026 with first node running on one board: https://old.reddit.com/r/ethereum/comments/1t9tdqb/daily_general_discussion_may_11_2026/ol54wr4/

1d ago

---

**[Daily General Discussion September 29, 2026](https://www.reddit.com/r/ethereum/comments/1wt16ck/daily_general_discussion_september_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[Glamsterdam Testnet Announcement | Ethereum Foundation Blog](https://www.reddit.com/r/ethereum/comments/1wt0x0n/glamsterdam_testnet_announcement_ethereum/)**

Glamsterdam follows the Fusaka upgrade, advancing Ethereum's L1 scaling roadmap with enshrined proposer-builder separation, block-level access lists, and...

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/09/17/glamsterdam-testnet-announcement) • 1d ago

---

**[Daily General Discussion September 28, 2026](https://www.reddit.com/r/ethereum/comments/1ws5jwv/daily_general_discussion_september_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[Compute and Consensus](https://www.reddit.com/r/ethereum/comments/1wsig29/compute_and_consensus/)**

🔗 [akeysfamoffice.substack.com](https://akeysfamoffice.substack.com/p/compute-and-consensus?r=95seez&utm_campaign=post-expanded-share&utm_medium=web) • 2d ago

---

**[The cryptographic world computer | Vitalik](https://www.reddit.com/r/ethereum/comments/1ws2z7z/the_cryptographic_world_computer_vitalik/)**

🔗 [vitalik.eth.limo](https://vitalik.eth.limo/general/2026/09/27/the_cryptographic_world_computer.html) • 2d ago

---

**[Daily General Discussion September 27, 2026](https://www.reddit.com/r/ethereum/comments/1wrbb9b/daily_general_discussion_september_27_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

---

## Google News: "ethereum"

**[Aztec relaunches zk.money privacy wallet on its Ethereum Layer 2](https://www.theblock.co/news/defi/2026-09-29-aztec-zk-money-privacy-wallet-ethereum-layer-2-417174)**

The wallet returns three years after its shutdown, now running on Aztec Network with private balances and transactions.

The Block • 1d ago

---

**[Cardano vs Ethereum: Which Smart Contract Platform Wins by 2030?](https://247wallst.com/investing/cryptocurrency/2026/09/29/cardano-vs-ethereum-which-smart-contract-platform-wins-by-2030/)**

Cardano has outperformed Ethereum over 90 days, yet Ethereum's market value is 35 times larger. Who wins Cardano vs. Ethereum by 2030?

24/7 Wall St. • 1d ago

---

**[Which Major Cryptocurrency Has the Most Potential for Growth? Ranking Bitcoin, Ethereum, XRP, and Solana by Distance from Their All-Time Highs](https://finance.yahoo.com/markets/crypto/articles/major-cryptocurrency-most-potential-growth-110049314.html)**

Bitcoin, Ethereum, XRP, and Solana all crashed from their 2025 peaks, but one of them stands out as having a uniquely powerful combination of factors that could fuel a sharper recovery than the others.

Yahoo Finance • 13h ago

---

**[Current price of Ethereum for Sept. 30, 2026](https://fortune.com/article/price-of-ethereum-09-30-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 9h ago

---

**[Hayes sets bullish Bitcoin, Ethereum predictions; crypto stocks jump](https://seekingalpha.com/news/4648479-hayes-sets-bullish-bitcoin-ethereum-predictions-crypto-stocks-jump)**

Arthur Hayes predicts Bitcoin could hit $1M by 2030 as an AI bubble drives liquidity, with ETH eyeing $10K.

Seeking Alpha • 11h ago

---

**[Ethereum users get another way to pay privately as zk.money returns after three years](https://www.coindesk.com/tech/2026/09/29/embargo-12-et-ethereum-users-get-another-way-to-pay-privately-as-zk-money-returns-after-three-years)**

The relaunched wallet hides payments made on the Aztec Network, while deposits from Ethereum remain visible.

CoinDesk • 1d ago

---

**[Bitcoin Dips, While Ethereum, XRP, Dogecoin Gain: Bull Market 'Intact,' but Rally 'Showing Cracks,' Says Analyst](https://www.tradingview.com/news/benzinga:931a8d2c5094b:0-bitcoin-dips-while-ethereum-xrp-dogecoin-gain-bull-market-intact-but-rally-showing-cracks-says-analyst/)**

Leading cryptocurrencies stayed resilient on Tuesday while rising government bond yields weighed on stock markets.Crypto Market Holds SteadyBitcoin held on to support in the mid-$82,000 region, while bulls attempted a break above $85,000. Ethereum oscillated between $2,650 and $2,740, while XRP and…

TradingView • 22h ago

---

**[Glamsterdam Testnet Announcement](https://blog.ethereum.org/2026/09/17/glamsterdam-testnet-announcement)**

Glamsterdam follows the Fusaka upgrade, advancing Ethereum's L1 scaling roadmap with enshrined proposer-builder separation, block-level access lists, and...

ethereum.org • 2d ago

---

**[Bitmine Continues to Load Up on Ethereum, Now Owns 4.9% of all ETH in Circulation. Is BMNR Stock a Buy?](https://currently.att.yahoo.com/att/bitmine-continues-load-ethereum-now-172001755.html)**

Bitmine has gone all in on Ethereum, the second-largest cryptocurrency in the world.

Currently.com • 1d ago

---

**[Tom Lee's Bitmine Buys Another $47M of ETH, Taking It to 4.9% of Ethereum Supply](https://decrypt.co/379418/tom-lees-bitmine-buys-another-47m-of-eth-taking-it-to-4-9-of-ethereum-supply)**

Bitmine has staked 84% of its tokens, a position it projects will generate some $358 million a year in staking rewards.

Decrypt News • 2d ago

---

---

## YouTube Videos: "ethereum"

**[BREAKING WALL STREET IS COMING! $10,000 ETHEREUM CALL?! XRP MILESTONE COULD SEND ALTCOINS CRAZY](https://www.youtube.com/watch?v=BAJpGVA8inA)**

BREAKING WALL STREET IS COMING! $10000 ETHEREUM CALL?! XRP MILESTONE COULD SEND ALTCOINS CRAZY Claim ...

📺 CryptoWendyO

👁️ 12K • 👍 468 • 💬 14 • ⏱️ 30:38 • 6h ago

---

**[Why I Think Ethereum Can Reach $16K This Bull Run](https://www.youtube.com/watch?v=PlLT0t3MQbk)**

Join my community | Work with me directly: https://whop.cryptoarchieyt.com/redirect.php?link=youtube_long_form_v46 ______ I ...

📺 Crypto Archie

👁️ 1K • 👍 38 • 💬 1 • ⏱️ 5:39 • 10h ago

---

**[Jack Mallers :&quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” | 2026 Crypto Prediction](https://www.youtube.com/watch?v=yLqfrDPHyxA)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 13K • 👍 283 • 💬 21 • ⏱️ 17:08 • 1d ago

---

**[Massive XRP Purchase Cardano ADA MIGHT Get More Support Ethereum Announces NEW Upgrade](https://www.youtube.com/watch?v=mTlBOW4lpAE)**

Not a day goes by in the cryptocurrency market where we dont get some kind of intense news. Companies have upped their ...

📺 The Modern Investor

👁️ 11K • 👍 817 • 💬 333 • ⏱️ 33:16 • 15h ago

---

**[Raoul Pal: Ethereum To $444,000 In The Next Few Years - How ETH Could Realistically 120x](https://www.youtube.com/watch?v=lkki8XmPoj8)**

Get your $25 Kalshi bonus here!: https://kalshi.com/p/cryptonutshell My FREE Daily 5-Min Crypto Newsletter: ...

📺 Crypto Nutshell

👁️ 19K • 👍 390 • 💬 34 • ⏱️ 21:29 • 2d ago

---

**[ETH Could Shock Everyone!](https://www.youtube.com/watch?v=A8YcphcuZ3U)**

Ethereum could have a massive move ahead if it breaks the $5000 level. The speaker argues that ETH may not stop at the 1.618 ...

📺 Crypto Archie Plus

👁️ 13 • 👍 2 • ⏱️ 0:38 • 2h ago

---

**[Joseph Chalom: Ethereum Is The Toll Road To Everything (Larry Fink&#39;s Words)](https://www.youtube.com/watch?v=s-Gu-S-VM6Y)**

Joseph Chalom says Larry Fink's line that Ethereum is the toll road to tokenization is exactly the right way to think about the asset, ...

📺 The Rollup

👁️ 28K • 👍 407 • 💬 19 • ⏱️ 31:51 • 2d ago

---

**[$10k ETH will cause Alt Season](https://www.youtube.com/watch?v=CUDFg3otido)**

Join Discord Group https://whop.com/checkout/plan_lyc1AoLEUzNVD X https://twitter.com/PainofCrypt0 Instagram ...

📺 Pain of Crypto

👁️ 10K • 👍 197 • 💬 24 • ⏱️ 6:17 • 1d ago

---

**[XRP TO $200 Bitcoin To 1 Million Ethereum To 10K After Trump Devalues The Dollar!](https://www.youtube.com/watch?v=zAxTrrxztYE)**

CASH APP= $CRYPTOTEACHER https://www.patreon.com/deathofcashbtc XRP TO $200 Bitcoin To 1 Million Ethereum To 10K ...

📺 Cryptoteacher

👁️ 842 • 👍 84 • 💬 2 • ⏱️ 29:31 • 4h ago

---

**[ETH: The Most Bullish Quarter in 5 Years!!! #ethereum](https://www.youtube.com/watch?v=C2lLeZwFOpQ)**

FeeDrip - up to (67%) of your trading fees back, paid daily ...

📺 Marzell Crypto

👁️ 972 • 👍 20 • 💬 1 • ⏱️ 3:20 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
