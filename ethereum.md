---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-02T04:26:44.156593+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- news
- cryptocurrency
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 02, 2026 at 04:26 UTC  
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

### $1,925.93

---

## Ethereum Chart

**24h:** -2.0%  
**7d:** +6.5%  
**30d:** -13.2%  
**90d:** -38.2%  
**1y:** -8.8%  

---

## Ethereum Market Stats

**Market Cap:** $238.00B
Rank #2

**Circulating Supply:** 120,692,218 ETH
No max supply

**All-Time High:** $4,946.05
-60.1%

**All-Time Low:** $0.43
+455268.5%

---

## Reddit: r/ethereum

**[[Roadmap] More execution layer changes](https://www.reddit.com/r/ethereum/comments/1ri30rj/roadmap_more_execution_layer_changes/)**

Now, execution layer changes. I've already talked about account abstraction, multidimensional gas, BALs, and ZK-EVMs. I've also talked here about a short-term EVM upgrade that I think will be super-valuable: a vectorized math precompile (basically, do 32-bit or potentially 64-bit operations on lists of numbers at the same time; in principle this could accelerate many hashes, STARK validation, FHE, lattice-based quantum-resistane signatures, and more by 8-64x); think "the GPU for the EVM". https://firefly.social/post/x/2027405623189803453 Today I'll focus on two big things: state tree changes, and VM changes. State tree changes are in this roadmap. VM changes (ie. EVM -> RISC-V or something better) are longer-term and are still more non-consensus, but I have high conviction that it will become "the obvious thing to do" once state tree changes and the long-term state roadmap (see https://ethresear.ch/t/hyper-scaling-state-by-creating-new-forms-of-state/24052 ) are finished, so I'll make my case for it here. What these two have in common is: They are the big bottlenecks that we have to address if we want efficient proving (tree + VM are like >80%) They're basically mandatory for various client-side proving use cases They are "deep" changes that many shrink away from, thinking that it is more "pragmatic" to be incrementalist I'll make the case for both. Binary trees The state tree change (worked on by @gballet and many others) is https://eips.ethereum.org/EIPS/eip-7864, switching from the current hexary keccak MPT to a binary tree based on a more efficient hash function. This has the following benefits: 4x shorter Merkle branches (because binary is 32log(n) and hexary is 512log(n)/4), which makes client-side branch verification more viable. This makes Helios, PIR and more 4x cheaper by data bandwidth Proving efficiency. 3-4x comes from shorter Merkle branches. On top of that, the hash function change: either blake3 [perhaps 3x vs keccak] or a Poseidon variant [100x, but more security work to be done] Client-side proving: if you want ZK applications that compose with the ethereum state, instead of making their own tree like today, then the ethereum state tree needs to be prover-friendly. Cheaper access for adjacent slots: the binary tree design groups together storage slots into "pages" (eg. 64-256 slots, so 2-8 kB). This allows storage to get the same efficiency benefits as code in terms of loading and editing lots of it at a time, both in raw execution and in the prover. The block header and the first ~1-4 kB of code and storage live in the same page. Many dapps today already load a lot of data from the first few storage slots, so this could save them >10k gas per tx Reduced variance in access depth (loads from big contracts vs small contracts) Binary trees are simpler Opportunity to add any metadata bits we end up needing for state expiry Zooming out a bit, binary trees are an "omnibus" that allows us to take all of our learnings from the past ten years about what makes a good state tree, and actually apply them. VM changes See also: https://ethereum-magicians.org/t/long-term-l1-execution-layer-proposal-replace-the-evm-with-risc-v/23617 One reason why the protocol gets uglier over time with more special cases is that people have a certain latent fear of "using the EVM". If a wallet feature, privacy protocol, or whatever else can be done without introducing this "big scary EVM thing", there's a noticeable sigh of relief. To me, this is very sad. Ethereum's whole point is its generality, and if the EVM is not good enough to actually meet the needs of that generality, then we should tackle the problem head-on, and make a better VM. This means: More efficient than EVM in raw execution, to the point where most precompiles become unnecessary More prover-efficient than EVM (today, provers are written in RISC-V, hence my proposal to just make the new VM be RISC-V) Client-side-prover friendly. You should be able to, client-side, make ZK-proofs about eg. what happens if your account gets called with a certain piece of data Maximum simplicity. A RISC-V interpreter is only a couple hundred lines of code, it's what a blockchain VM "should feel like" This is still more speculative and non-consensus. Ethereum would certainly be fine if all we do is EVM + GPU. But a better VM can make Ethereum beautiful and great. A possible deployment roadmap is: NewVM (eg. RISC-V) only for precompiles: 80% of today's precompiles, plus many new ones, become blobs of NewVM code Users get the ability to deploy NewVM contracts EVM is retired and turns into a smart contract written in NewVM EVM users experience full backwards compatibility except gas cost changes (which will be overshadowed by the next few years of scaling work). And we get a much more prover-efficient, simpler and cleaner protocol.

11h ago

---

**[Daily General Discussion March 01, 2026](https://www.reddit.com/r/ethereum/comments/1rhpjtf/daily_general_discussion_march_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

22h ago

---

**[Is this possible to bridge BTC to ETH?](https://www.reddit.com/r/ethereum/comments/1ri86sz/is_this_possible_to_bridge_btc_to_eth/)**

Hi ethereumers (if that's the way we call the ethereum community eheh), firstly i'm sorry if this is an frequent question but i couldn't find the answer anywhere so i wanna ask about it. I'm holding Bitcoins in trustwallet which i'm willing to convert to eth to pay gas for my usdt, is there a simple/fast way to do it? Advices appreciated

7h ago

---

**[Vitalik’s new account abstraction design could change Ethereum wallets](https://www.reddit.com/r/ethereum/comments/1rhtx38/vitaliks_new_account_abstraction_design_could/)**

Ethereum has talked about account abstraction for years, but EIP-8141 might finally move it into the protocol itself. Instead of wallets + relayers handling validation and gas, transactions would contain that logic directly (“frame transactions”). That could enable: • gas in any token • built-in batching • smart-account features for all wallets • no relayers Simple explanation here: https://btcusa.com/ethereum-account-abstraction-reaches-protocol-layer-inside-vitaliks-eip-8141-framework/

18h ago

---

**[If you're not a developer, have you still ever wanted to create a smart contract?](https://www.reddit.com/r/ethereum/comments/1rifzlz/if_youre_not_a_developer_have_you_still_ever/)**

I've been a crypto developer for about 10 years, so I don't think I can answer this question to myself anymore. and most of my social circle is developers as well so it's kind of the same thing. I'm trying to figure out if (or what anecdotal percentage of) non-developers have any desire to create smart contracts. Or rather, just the desire to create non-template crypto projects. (Full transparency: this is related to something I'm building, but I don't want to promote it here because I'm really just looking to have a discussion) Have you ever wanted to create a crypto project but felt like you couldn't because of the skill gap?

2h ago

---

**[TIL the first on-chain proof of attendance token was deployed at Devcon2 in 2016 — three years before POAP launched](https://www.reddit.com/r/ethereum/comments/1rhxzxq/til_the_first_onchain_proof_of_attendance_token/)**

Piper Merriam deployed the IndividualityTokenRoot contract in September 2016 for Devcon2 in Shanghai. Each attendee could mint a unique on-chain token proving they were there — fully ERC-20 compliant, written in Solidity 0.3.6. The idea was simple: if you attended Devcon2, you could claim a token. The minting window closed after the event. No metadata, no images, no marketplace speculation — just cryptographic proof you were in the room. Three years later, POAP launched at ETHDenver 2019 and turned this concept into a whole ecosystem. But the original idea was already deployed and functional on mainnet in 2016. What I find interesting is how many "firsts" are buried in Ethereum's early history. The Devcon2 token was a working proof-of-attendance system years before anyone coined the term "POAP." Alex Van de Sande's Unicorn token (April 2016) had a DAO-governed token grinder with quadratic voting. The DAO itself was mid-2016. All of this predates DeFi Summer by four years. The contract is still on mainnet: 0xdd94de9cfe063577051a5eb7465d08317d8808b6 Source: Piper Merriam's GitHub repo with deployment details and minting logic. If you're interested in exploring more of these early contracts, ethereumhistory.com has been documenting them — 75+ contracts from 2015-2017 with sourced narratives.

14h ago

---

**[Littercoin smart contracted updated. New diagrams added.](https://www.reddit.com/r/ethereum/comments/1ribzeb/littercoin_smart_contracted_updated_new_diagrams/)**

Littercoin smart contract for Ethereum. Contribute to OpenLitterMap/littercoin-eth development by creating an account on GitHub.

🔗 [GitHub](https://github.com/OpenLitterMap/littercoin-eth) • 5h ago

---

**[AI coding Ethereum for speed and for security](https://www.reddit.com/r/ethereum/comments/1rh6rt4/ai_coding_ethereum_for_speed_and_for_security/)**

https://firefly.social/post/x/2026252944639934778 This is quite an impressive experiment. Vibe-coding the entire 2030 roadmap within weeks. Obviously such a thing built in two weeks without even having the EIPs has massive caveats: almost certainly lots of critical bugs, and probably in some cases "stub" versions of a thing where the AI did not even try making the full version. But six months ago, even this was far outside the realm of possibility, and what matters is where the trend is going. AI is massively accelerating coding (yesterday, I tried agentic-coding an equivalent of my blog software, and finished within an hour, and that was using gpt-oss:20b running on my laptop (!!!!), kimi-2.5 would have probably just one-shotted it). But probably, the right way to use it, is to take half the gains from AI in speed, and half the gains in security: generate more test-cases, formally verify everything, make more multi-implementations of things. A collaborator of the @leanethereum effort managed to AI-code a machine-verifiable proof of one of the most complex theorems that STARKs rely on for security. A core tenet of @leanethereum is to formally verify everything, and AI is greatly accelerating our ability to do that. Aside from formal verification, simply being able to generate a much larger body of test cases is also important. Do not assume that you'll be able to put in a single prompt and get a highly-secure version out anytime soon; there WILL be lots of wrestling with bugs and inconsistencies between implementations. But even that wrestling can happen 5x faster and 10x more thoroughly. People should be open to the possibility (not certainty! possibility) that the Ethereum roadmap will finish much faster than people expect, at a much higher standard of security than people expect. On the security side, I personally am excited about the possibility that bug-free code, long considered an idealistic delusion, will finally become first possible and then a basic expectation. If we care about trustlessness, this is a necessary piece of the puzzle. Total security is impossible because ultimately total security means exact correspondence between lines of code and contents of your mind, which is many terabytes (see https://firefly.social/post/x/2025653045414273438 ). But there are many specific cases, where specific security claims can be made and verified, that cut out >99% of the negative consequences that might come from the code being broken.

1d ago

---

**[TIL Ethereum had quadratic voting on-chain in 2016, and the DAO that used it is still alive](https://www.reddit.com/r/ethereum/comments/1rh1qsb/til_ethereum_had_quadratic_voting_onchain_in_2016/)**

Was digging through early Ethereum contracts and found something wild. In April 2016, Alex Van de Sande (@avsa) deployed a token called Unicorn Meat as an April Fool's joke. You could "grind" Unicorn tokens (0 decimals, basically NFTs before NFTs) into Unicorn Meat (3 decimals, fungible). The grinder contract handled the conversion on-chain. But here's the part that blew my mind: the Grinder Association DAO that governed the system used quadratic voting. In 2016. Before Gitcoin, before Vitalik's QV paper got popular, before anyone was talking about it. The voting weight scaled with the square root of tokens held, specifically to prevent whale dominance. Piper Merriam (yes, the py-evm / web3.py Piper Merriam) ended up taking over governance of the association. The DAO is technically still functional on mainnet. The technical design is also interesting from a token engineering perspective. The 0-decimal to 3-decimal conversion was essentially an early attempt at what we'd now call a token upgrade or migration path, but done through a grinder mechanic instead of a proxy pattern. One indivisible input, 1000 divisible units out. Irreversible by design. It's a tiny piece of Ethereum history that somehow combined: - Quadratic voting governance (years before it was mainstream) - On-chain token transformation (not just wrapping, actual decimal conversion) - A DAO with real authority over contract parameters - All of it deployed before The DAO hack even happened The contracts are all still on mainnet if anyone wants to poke around. Just search for UnicornGrinder on Etherscan. Sometimes the best innovations start as jokes.

1d ago

---

**[Daily General Discussion February 28, 2026](https://www.reddit.com/r/ethereum/comments/1rgut7b/daily_general_discussion_february_28_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

---

## Google News: "ethereum"

**[Better Cryptocurrency to Buy With $5,000 and Hold Forever: XRP vs. Ethereum](https://www.nasdaq.com/articles/better-cryptocurrency-buy-5000-and-hold-forever-xrp-vs-ethereum)**

Key PointsThe longer your investing time horizon, the more uncertainty you'll have to take into account.

Nasdaq • 2d ago

---

**[Crypto News: New Ethereum Based Crypto Pepeto Announces Presale Passing $7.403M Following Elon Musk Favorite Crypto Dogecoin Success](https://markets.businessinsider.com/news/stocks/crypto-news-new-ethereum-based-crypto-pepeto-announces-presale-passing-7-403m-following-elon-musk-favorite-crypto-dogecoin-success-1035882586)**

Dubai, UAE, March  01, 2026  (GLOBE NEWSWIRE) -- New Ethereum Based Crypto Pepeto just broke past $7.403 million in presale funding after the late...

markets.businessinsider.com • 4h ago

---

**[New Crypto Ethereum Based: Pepeto Unveils $7.391M Presale Milestone as XRP News Make Waves and Bitcoin Target $150,000 This Year](https://markets.businessinsider.com/news/stocks/new-crypto-ethereum-based-pepeto-unveils-7-391m-presale-milestone-as-xrp-news-make-waves-and-bitcoin-target-150-000-this-year-1035882544)**

Dubai, UAE, March  01, 2026  (GLOBE NEWSWIRE) -- New crypto Ethereum based Pepeto just crossed $7.391 million raised in presale funding and demand...

markets.businessinsider.com • 4h ago

---

**[Vitalik Buterin lays out a two-part plan to overhaul Ethereum's execution layer from the ground up](https://www.theblock.co/post/391681/vitalik-buterin-lays-out-a-two-part-plan-to-overhaul-ethereums-execution-layer-from-the-ground-up)**

The binary tree proposal is a concrete, in-progress effort, while the VM transition remains more speculative and lacks broad consensus among developers.

The Block • 6h ago

---

**[Bitcoin, Ethereum ‘pumping hard’ after Iran strikes, but states brace for financial fallout](https://finance.yahoo.com/news/bitcoin-ethereum-pumping-hard-iran-105754078.html)**

Bitcoin rises near $67,000 mark, with Ethereum nearing $2,000. Iran has confirmed the death of supreme leader Ayatollah Ali Khamenei. The real price reveal is coming tomorrow, expert says.

Yahoo Finance • 17h ago

---

**[Bitcoin, Ethereum drop after US and Israel strike Iran](https://www.dlnews.com/articles/markets/bitcoin-price-drops-after-trump-announced-iran-strikes/)**

President Donald Trump announced Saturday that the US and Israel attacked Iran. Bitcoin and Ethereum immediately dropped on the news.  It isn’t clear how long the military operation will take.

dlnews.com • 1d ago

---

**[Bitcoin, Ethereum, XRP Fall as Cryptos Unwind Gains. Blame Nvidia.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-crypto-nvidia-f093b2bd?gaa_at=eafs&gaa_n=AWEtsqfOwamOXV4W9nnlhtqAnbF8L4pFi1SsRSsuXWrBx1LYd6ctSmPTrABK&gaa_ts=69a514ef&gaa_sig=CCS8wdeW7afhJO4JKG_K6mlZxKXAmEjQBemCJj1U7kNBxj22TjS101j6dT_Ker6e8vi2-mD-do05WzdeHGWThw%3D%3D)**

Barron's • 2d ago

---

**[Ethereum news: Vitalik Buterin reveals his bold new plan to fix the network’s scaling problem](https://www.coindesk.com/tech/2026/02/27/vitalik-buterin-reveals-his-bold-new-plan-to-fix-ethereum-s-scaling-problem)**

The new post reflects Buterin’s renewed focus on scaling Ethereum’s base layer, after several years in which much of the ecosystem’s scaling strategy centered on layer-2 rollups.

CoinDesk • 2d ago

---

**[Why institutions still prefer Ethereum despite faster blockchains](https://www.tradingview.com/news/cointelegraph:69ebf507b094b:0-why-institutions-still-prefer-ethereum-despite-faster-blockchains/)**

Ethereum continues to host the largest concentration of stablecoins and decentralized finance (DeFi) capital, even as successive waves of faster networks emerge.Newer blockchains have promised higher throughput and lower costs, raising questions about whether institutional capital could eventually…

TradingView • 1d ago

---

**[How Chainlink CCIP Connects Ethereum, Solana, and Private Bank Chains in 2026](https://financefeeds.com/how-chainlink-ccip-connects-ethereum-solana-and-private-bank-chains-in-2026/)**

The need for blockchains to enable transactions among themselves has become a necessity. In 2026, the cross-chain interoperability protocol (CCIP) is making

FinanceFeeds • 6h ago

---

---

## YouTube Videos: "ethereum"

**[Vitalik Buterin Is Selling His ETH: What It Means for Ethereum](https://www.youtube.com/watch?v=PuX5B18EZvs)**

Did Vitalik Buterin just dump Ethereum at the worst possible time? After announcing a “few years” funding plan, nearly half the ...

📺 Coin Bureau

👁️ 56K • 👍 2K • 💬 229 • ⏱️ 18:01 • 15h ago

---

**[Ethereum &amp; BMNR Are Becoming Wall Street’s Rails — MSTR Is Positioning](https://www.youtube.com/watch?v=SMXtIWnXCoU)**

I'm giving away my Weekly Trading Strategy + my new book Money Game FREE ...

📺 MONEY GAME

👁️ 3K • 👍 131 • 💬 28 • ⏱️ 36:54 • 7h ago

---

**[BITCOIN &amp; CRYPTO: This Could Change EVERYTHING!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=tCR2YKL1_0o)**

BITCOIN & CRYPTO: This Could Change EVERYTHING!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 3K • 👍 192 • 💬 24 • ⏱️ 15:02 • 4h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=3LGeKJcLvIU)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 533 • 👍 51 • 💬 2 • ⏱️ 5:32 • 3h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=TTtNEO2AICc)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 159 • 💬 9 • ⏱️ 7:25 • 15h ago

---

**[BE READY FOR THIS PRICE ACTION!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=-3ajnM3ZrjQ)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 422 • 👍 12 • 💬 3 • ⏱️ 4:36 • 18h ago

---

**[Is Ethereum the BEST Risk-Reward Asset in Crypto Right Now?](https://www.youtube.com/watch?v=ZMgG1xWOipE)**

Check prices, drink coffee, read Milk Road. It's the easiest 5-minute habit to stay smart on crypto: ...

📺 Milk Road

👁️ 4K • 👍 120 • 💬 59 • ⏱️ 8:43 • 1d ago

---

**[Tom Lee: The Dark Truth About What&#39;s REALLY Happening With Crypto (New 2026 Prediction)](https://www.youtube.com/watch?v=UbCbRrPUimU)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 9K • 👍 381 • 💬 17 • ⏱️ 21:26 • 2d ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=MmKkOwMy2lE)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Profit First

👁️ 192 • 👍 38 • ⏱️ 7:27 • 31m ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=KfpsSUAcpRY)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 150 • 💬 6 • ⏱️ 3:55 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
