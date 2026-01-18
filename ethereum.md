---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-01-18T10:23:20.972096+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- videos
- news
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** January 18, 2026 at 10:23 UTC  
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

### $3,309.69

---

## Ethereum Chart

**24h:** +0.5%  
**7d:** +7.2%  
**30d:** +11.4%  
**90d:** -14.0%  
**1y:** +3.1%  

---

## Ethereum Market Stats

**Market Cap:** $400.25B
Rank #2

**Circulating Supply:** 120,694,592 ETH
No max supply

**All-Time High:** $4,946.05
-32.9%

**All-Time Low:** $0.43
+766094.2%

---

## Reddit: r/ethereum

**[Daily General Discussion January 18, 2026](https://www.reddit.com/r/ethereum/comments/1qg0myc/daily_general_discussion_january_18_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

4h ago

---

**[Protocol simplicity as necessary part of trustlessness](https://www.reddit.com/r/ethereum/comments/1qg4ay1/protocol_simplicity_as_necessary_part_of/)**

An important, and perenially underrated, aspect of "trustlessness", "passing the walkaway test" and "self-sovereignty" is protocol simplicity. Even if a protocol is super decentralized with hundreds of thousands of nodes, and it has 49% byzantine fault tolerance, and nodes fully verify everything with quantum-safe peerdas and starks, if the protocol is an unwieldy mess of hundreds of thousands of lines of code and five forms of PhD-level cryptography, ultimately that protocol fails all three tests: It's not trustless because you have to trust a small class of high priests who tell you what properties the protocol has It doesn't pass the walkaway test because if existing client teams go away, it's extremely hard for new teams to get up to the same level of quality It's not self-sovereign because if even the most technical people can't inspect and understand the thing, it's not fully yours It's also less secure, because each part of the protocol, especially if it can interact with other parts in complicated ways, carries a risk of the protocol breaking. One of my fears with Ethereum protocol development is that we can be too eager to add new features to meet highly specific needs, even if those features bloat the protocol or add entire new types of interacting components or complicated cryptography as critical dependencies. This can be nice for short-term functionality gains, but it is highly destructive to preserving long-term self-sovereignty, and creating a hundred-year decentralized hyperstructure that transcends the rise and fall of empires and ideologies. The core problem is that if protocol changes are judged from the perspective of "how big are they as changes to the existing protocol", then the desire to preserve backwards compatibility means that additions happen much more often than subtractions, and the protocol inevitably bloats over time. To counteract this, the Ethereum development process needs an explicit "simplification" / "garbage collection" function. "Simplification" has three metrics: Minimizing total lines of code in the protocol. An ideal protocol fits onto a single page - or at least a few pages Avoiding unnecessary dependencies on fundamentally complex technical components. For example, a protocol whose security solely depends on hashes (even better: on exactly one hash function) is better than one that depends on hashes and lattices. Throwing in isogenies is worst of all, because (sorry to the truly brilliant hardworking nerds who figured that stuff out) nobody understands isogenies. Adding more invariants: core properties that the protocol can rely on, for example EIP-6780 (selfdestruct removal) added the property that at most N storage slots can be changedakem per slot, significantly simplifying client development, and EIP-7825 (per-tx gas cap) added a maximum on the cost of processing one transaction, which greatly helps ZK-EVMs and parallel execution. Garbage collection can be piecemeal, or it can be large-scale. The piecemeal approach tries to take existing features, and streamline them so that they are simpler and make more sense. One example is the gas cost reforms in Glamsterdam, which make many gas costs that were previously arbitrary, instead depend on a small number of parameters that are clearly tied to resource consumption. One large-scale garbage collection was replacing PoW with PoS. Another is likely to happen as part of Lean consensus, opening the room to fix a large number of mistakes at the same time ( youtube.com/watch?v=10Ym34y3E… ). Another approach is "Rosetta-style backwards compatibility", where features that are complex but little-used remain usable but are "demoted" from being part of the mandatory protocol and instead become smart contract code, so new client developers do not need to bother with them. Examples: After we upgrade to full native account abstraction, all old tx types can be retired, and EOAs can be converted into smart contract wallets whose code can process all of those transaction types We can replace existing precompiles (except those that are really needed) with EVM or later RISC-V code We can eventually change the VM from EVM to RISC-V (or other simpler VM); EVM could be turned into a smart contract in the new VM. Finally, we want to move away from client developers feeling the need to handle all older versions of the Ethereum protocol. That can be left to older client versions running in docker containers. In the long term, I hope that the rate of change to Ethereum can be slower. I think for various reasons that ultimately that must happen. These first fifteen years should in part be viewed as an adolescence stage where we explored a lot of ideas and saw what works and what is useful and what is not. We should strive to avoid the parts that are not useful being a permanent drag on the Ethereum protocol. Basically, we want to improve Ethereum in a way that looks like this: https://old.reddit.com/r/SpaceXLounge/comments/1eis952/evolution_of_the_raptor_engine_by_cstanley/

52m ago

---

**[Daily General Discussion January 17, 2026](https://www.reddit.com/r/ethereum/comments/1qf5ctg/daily_general_discussion_january_17_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[2026: the year that we take back lost ground](https://www.reddit.com/r/ethereum/comments/1qer9cy/2026_the_year_that_we_take_back_lost_ground/)**

2026 is the year that we take back lost ground in terms of self-sovereignty and trustlessness. Some of what this practically means: Full nodes: thanks to ZK-EVM and BAL, it will once again become easier to locally run a node and verify the Ethereum chain on your own computer. Helios: actually verify the data you're receiving from RPCs instead of blindly trusting it. ORAM, PIR: ask for data from RPCs without revealing which data you're asking, so you can access dapps without your access patterns being sold off to dozens of third parties all around the world. Social recovery wallets and timelocks: wallets that don't make you lose all your money if you misplace your seedphrase, or if an online or offline attacker extracts your seedphrase, and also don't make all your money backdoored by Google. Privacy UX: make private payments from your wallet, with the same user experience as making public payments. Privacy censorship resistance: private payments with the ERC-4337 mempool, and soon native AA + FOCIL, without relying on the public broadcaster ecosystem. Application UIs: use more dapps from an onchain UI with IPFS, without relying on trusted servers that would lock you our of practical recovery of your assets if they went offline, and would give you a hijacked UI that steals your funds if they get hacked for even a millisecond. In many of these areas, over the last ten years we have seen serious backsliding in Ethereum. Nodes went from easy to run to hard to run. Dapps went from static pages to complicated behemoths that leak all your data to a dozen servers. Wallets went from routing everything through the RPC, which could be any node of your choice including on your own computer, to leaking your data to a dozen servers of their choice. Block building became more centralized, putting Ethereum transaction inclusion guarantees under the whims of a very small number of builders. In 2026, no longer. Every compromise of values that Ethereum has made up to this point - every moment where you might have been thinking, is it really worth diluting ourselves so much in the name of mainstream adoption - we are making that compromise no longer. It will be a long road. We will not get everything we want in the next Kohaku release, or the next hard fork, or the hard fork after that. But it will make Ethereum into an ecosystem that deserves not only its current place in the universe, but a much greater one. In the world computer, there is no centralized overlord. There is no single point of failure. There is only love. Milady.

1d ago

---

**[Re: Best hardware for running ETH node](https://www.reddit.com/r/ethereum/comments/1qfhiwt/re_best_hardware_for_running_eth_node/)**

2 months ago was solving this. With RAM hikes I found a solution that required me to dig in the trash, literally. Bought a cheap Mac Pro (2013), the trashcan Mac off eBay with DDR3 64gb ram, works well. It would have been the same price as one of those NUCs or mini PCs and it has much better specs even so from then. What I need next for it is an external SSD or NVME to house both the beacon and geth node state, account, blockchain data. Regular HDD is impossible to use and keep up with the network, way too slow. HDDs however have good endurance compared to SSDs and cheaper, from what I know, GETH does a lot of read/writes. I was curious if any self-host ETH node folks here can share smartctl output for how much TBs written their SSDs or NVMEs has had to endure for the last year. I want to see how many drives I'll burn through from all the read/writes happening to the drive from continuous syncing. Also feel free to share disk brands, sizes, etc. that you used along with the TBW data.

17h ago

---

**[I have 20 hours to learn as much as I can.](https://www.reddit.com/r/ethereum/comments/1qeuzx0/i_have_20_hours_to_learn_as_much_as_i_can/)**

I have a 20 hour flight and I want to spend it studying all that I can about blockchain, ethereum, smart contracts, and web3. Let me know what are your best recommendations to learn about the technicals - I have a strong background in machine learning and computer science but am completely new to the blockchain as a concept (bar the 3b1b series). Anything works, books, videos, research papers.

1d ago

---

**[Daily General Discussion January 16, 2026](https://www.reddit.com/r/ethereum/comments/1qe818u/daily_general_discussion_january_16_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Total newbie question... doesn't a high ETH price stifle the underlying tokenized economy which in turn acts as a mechanism to drive ETH prices lower?](https://www.reddit.com/r/ethereum/comments/1qejke3/total_newbie_question_doesnt_a_high_eth_price/)**

I have heard ETH being compared to oil. If oil goes up too high, those, who can, will cut back its use. If ETH goes to some stupid high prices, wouldn't people cut back on its usages and help prices go lower. Wouldn't higher prices also encourage the production of more ETH... the old the solution to high prices is high prices. Please explain to me where the flaw is in my reasoning.

1d ago

---

**[Ethereal news weekly #7 | Ethereum must pass walkaway test, Base app focuses on trading, Trail of Bits Claude Code skills](https://www.reddit.com/r/ethereum/comments/1qedycf/ethereal_news_weekly_7_ethereum_must_pass/)**

Ethereum must pass walkaway test, Base app focuses on trading, Trail of Bits Claude Code skills

🔗 [ethereal.news](https://ethereal.news/ethereal-news-weekly-7/) • 1d ago

---

**[What are you building on ENS?](https://www.reddit.com/r/ethereum/comments/1qehrj6/what_are_you_building_on_ens/)**

1d ago

---

---

## Google News: "ethereum"

**[Vitalik Buterin declares 2026 the year Ethereum reverses 'backsliding' of self-sovereignty and trustlessness](https://www.theblock.co/post/386043/vitalik-buterin-declares-2026-the-year-ethereum-reverses-backsliding-of-self-sovereignty-and-trustlessness)**

The Block • 1d ago

---

**[Is Solana's Pain a Game Changer for Ethereum?](https://www.fool.com/investing/2026/01/16/is-solanas-pain-a-game-changer-for-ethereum/)**

The smaller chain could lose ground in an important arena during a critical period.

The Motley Fool • 1d ago

---

**[Ethereum news: Spike in first-time wallet activity over the past month](https://www.coindesk.com/tech/2026/01/16/more-people-are-using-ethereum-for-the-first-time-data-shows)**

The rise in new wallets suggests broader interest in Ethereum, driven by decentralized finance, stablecoin transfers, NFTs, and new applications.

CoinDesk • 2d ago

---

**[Standard Chartered Says '2026 Will Be The Year Of Ethereum' As It Predicts 'ETH Outperformance'](https://finance.yahoo.com/news/standard-chartered-says-2026-ethereum-192131962.html)**

Ethereum will outperform Bitcoin this year, Standard Chartered says. “I think 2026 will be the year of Ethereum, much like 2021 was,” Standard Chartered Global Head of Digital Assets Research Geoffrey Kendrick said in a note accompanying the bank’s most...

Yahoo Finance • 2d ago

---

**[Ethereum smashes $120bn staking record as price seen to hit $40,000](https://www.dlnews.com/articles/markets/ethereum-smashes-120bn-staking-record-as-price-surges/)**

Nearly 30% of all Ethereum circulating supply is now locked up. Bitmine stakes another $600 million and now has $6 billion staked.  Tom Lee urges shareholders vote for his stock split proposal ahead of big meeting.

dlnews.com • 3d ago

---

**[From $3.5K to $12K? Here’s why BMNR’s Ethereum forecast makes sense](https://ambcrypto.com/from-3-5k-to-12k-heres-why-bmnrs-ethereum-forecast-makes-sense/)**

Is Ethereum following Bitcoin’s institutional playbook?

AMBCrypto • 8h ago

---

**[Bitcoin and Ethereum Waver–Why Did Trading Volume Drop?](https://decrypt.co/354916/bitcoin-ethereum-waver-trading-volume-drop)**

The crypto market wavered as trading volumes cooled, with Bitcoin and Ethereum drifting downward despite positive momentum earlier this week.

Decrypt • 2d ago

---

**[Top Analyst Says Next Crypto Rally for Bitcoin, Ethereum and XRP Has Begun](https://www.tradingview.com/news/coinpedia:1d7e1cbd1094b:0-top-analyst-says-next-crypto-rally-for-bitcoin-ethereum-and-xrp-has-begun/)**

A fresh rally may be underway in the cryptocurrency market, according to a senior analyst at blockchain data firm Santiment, who says investor sentiment is setting up a classic bullish signal for Bitcoin, Ethereum, and XRP.Brian Quinlivan, marketing director at Santiment, said in a recent interview…

TradingView — Track All Markets • 1d ago

---

**[ChatGPT Says Ethereum Will Make You Rich in 2026](https://247wallst.com/investing/2026/01/15/chatgpt-says-ethereum-will-make-you-rich-in-2026/)**

This Ethereum price prediction 2026 explores why ChatGPT chose ETH over Bitcoin. Bull $7K-$9K targets, $4K-$5K base, and bear case $2K-$3K.

24/7 Wall St. • 2d ago

---

**[Ethereum Technical Analysis Report 16 January, 2026](https://financefeeds.com/ethereum-technical-analysis-report-16-january-2026-2/)**

FinanceFeeds • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Takes Over Youtube!🚀Tom Lee Buys Mr. Beast🚨](https://www.youtube.com/watch?v=3svKfjrgjtc)**

Bitmine Immersion Technologies said Thursday it's investing $200 million in Beast Industries, the company founded by YouTube ...

📺 Paul Barron Network

👁️ 51K • 👍 2K • 💬 266 • ⏱️ 10:28 • 17h ago

---

**[BlackRock CEO Larry Fink SECRETLY Manipulating Bitcoin &amp; Ethereum](https://www.youtube.com/watch?v=XWwotSf0sbE)**

LIMITED TIME: ✓ Bitunix (no kyc, $100000 bonus): https://www.bitunix.com/register?vipCode=AltcoinDaily 50% deposit bonus ...

📺 Altcoin Daily

👁️ 33K • 👍 2K • 💬 225 • ⏱️ 12:19 • 13h ago

---

**[Ethereum ‼️ IT’S HAPPENING! My New Price Prediction](https://www.youtube.com/watch?v=O8fq92lR3F0)**

1️⃣ *Join Moe's Discord Code 2026 save 50%* ➡https://www.patreon.com/stockmoe/membership 2️⃣ *Save Big on the ...

📺 Stock Moe

👁️ 9K • 👍 689 • 💬 59 • ⏱️ 15:35 • 20h ago

---

**[$15,000 ETH By Year-End? Etherealize Founders Lay Out the Path to a New High](https://www.youtube.com/watch?v=ck6gZ8LWxlc)**

In today's Markets Outlook, Etherealize founders Vivek Raman and Danny Ryan join Jennifer Sanasie to discuss why Ethereum is ...

📺 CoinDesk

👁️ 7K • 👍 201 • 💬 21 • ⏱️ 24:55 • 1d ago

---

**[Tom Lee “I’ve Never Seen A Setup Like This Before” [NEW Bitcoin and Crypto Prediction 2026]](https://www.youtube.com/watch?v=s88GhpCIIBU)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 22K • 👍 796 • 💬 27 • ⏱️ 16:47 • 1d ago

---

**[ETH Ethereum Price Prediction: 17th of January](https://www.youtube.com/watch?v=vpkd8jNtqDs)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 580 • 👍 49 • 💬 14 • ⏱️ 14:00 • 17h ago

---

**[Ethereum Exploding? MrBeast &amp; $200M Investment Hint! #shorts #mrbeast](https://www.youtube.com/watch?v=aPnV-0lVbAE)**

Is MrBeast about to endorse Ethereum? With over half a billion followers, his voice carries weight. A $200M investment deal ...

📺 Traders Reality

👁️ 7K • 👍 216 • 💬 43 • ⏱️ 1:22 • 14h ago

---

**[Why Ethereum’s “Quiet Phase” Just Ended](https://www.youtube.com/watch?v=rVWQfUG8vEk)**

Bybit – Up to $30,050 Bonus, best platform (KYC required) ...

📺 Marzell Crypto

👁️ 2K • 👍 68 • 💬 90 • ⏱️ 6:39 • 3d ago

---

**[BITCOIN WARNING: It&#39;s Getting WORSE (important update)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=pRQdkJ5cqzk)**

BITCOIN WARNING: It's Getting WORSE (important update)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 8K • 👍 348 • 💬 155 • ⏱️ 22:05 • 22h ago

---

**[Tom Lee&#39;s URGENT Message for Bitcoin &amp; Crypto Investors In January!](https://www.youtube.com/watch?v=buMiV8EnaUE)**

FREE Daily On-Chain Analysis & Crypto News In 5-Mins: http://bit.ly/TheCryptoNutshell Watch The FULL Interview: "Tom ...

📺 Library Of Wealth

👁️ 5K • 👍 190 • 💬 203 • ⏱️ 15:03 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
