---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-06-02T11:18:35.792866+00:00'
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

**Last Updated:** June 02, 2026 at 11:18 UTC  
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

### $1,979.72

---

## Ethereum Chart

**24h:** -0.4%  
**7d:** -2.2%  
**30d:** -15.6%  
**90d:** -4.4%  
**1y:** -23.5%  

---

## Ethereum Market Stats

**Market Cap:** $238.68B
Rank #2

**Circulating Supply:** 120,685,138 ETH
No max supply

**All-Time High:** $4,946.05
-60.0%

**All-Time Low:** $0.43
+456467.2%

---

## Reddit: r/ethereum

**[Daily General Discussion June 02, 2026](https://www.reddit.com/r/ethereum/comments/1tugwmx/daily_general_discussion_june_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

6h ago

---

**[Is WBTC safe?](https://www.reddit.com/r/ethereum/comments/1tuejlb/is_wbtc_safe/)**

I am considering converting a few BTC to WBTC to stake. Theorically WBTC is better because I can also earn passive income while 'holding my keys' which is what i'm trying to understand: Is this custodial? more risky or same as USDT? Was there any freeze or issue on it by past?

8h ago

---

**[zk proofs aren't just for rollups. the more interesting use case is verifiable exchange execution](https://www.reddit.com/r/ethereum/comments/1tun93o/zk_proofs_arent_just_for_rollups_the_more/)**

most of the zk conversation in ethereum right now is about rollups. proving block validity, compressing state, bridging trustlessly. all important stuff. but there's a use case that i think is more immediately impactful and barely anyone talks about: using zk proofs to make exchange matching engines verifiable. here's the problem. every CLOB-style DEX runs a matching engine, and almost all of them are black boxes. your order goes in, a fill comes out, and you trust that the engine matched you fairly. you have no way to verify it. even the "decentralized" ones. the matching layer is the single biggest trust surface on any exchange and it's the one nobody can actually check. the fix isn't moving matching fully on-chain. dydx v4 went that direction and you pay for it in throughput, because every fill has to go through consensus. for a CLOB that's a hard ceiling on what you can offer. the more interesting path: keep matching off-chain for speed, but commit batched state transitions with validity proofs. the engine stays fast, but every batch of fills becomes cryptographically verifiable. no fill can be reordered, front-run, or fabricated without the proof failing. you get execution speed and provability without forcing a tradeoff between them. this feels like it matters more for end users than zk rollups honestly. rollups prove that a block was valid. exchange proofs prove that your specific trade was matched correctly. one is infrastructure-level, the other is directly about your money. curious why this isn't getting more attention in the ethereum zk community. is it a tooling problem? a "nobody's built it yet" problem? or does the market just not care enough about execution verifiability yet?

30m ago

---

**[How should new Ethereum L2s avoid becoming liquidity islands at launch?](https://www.reddit.com/r/ethereum/comments/1tui882/how_should_new_ethereum_l2s_avoid_becoming/)**

One thing I have been thinking about with newer Ethereum L2 ecosystems is the gap between “apps can deploy” and “users can actually bring useful liquidity in.” GIWA/GASOK is a good recent example. Teams are building toward mainnet, but the infrastructure question comes pretty early: If a wallet, DEX, lending app, or consumer app launches on a new L2, should each team be responsible for integrating bridges, routing, liquidity sources, and asset variants on its own? That feels like a lot of duplicated work for early app teams. One possible model is shared cross-network execution infrastructure: apps integrate a single SDK, and routing/liquidity access is handled outside the app. SODAX is preparing this kind of setup for GIWA builders, but the broader question applies to any new Ethereum L2. The tradeoffs seem non-trivial: app teams get faster access to multi-network liquidity users avoid manually bridging through several tools the L2 ecosystem may feel less empty at launch but routing, solver behavior, asset representation, and failure modes need to be easy to reason about For people who have built on or around Ethereum L2s: where do you think this responsibility should sit? Should liquidity/access infrastructure be handled by the L2 ecosystem, each individual app, or external execution layers?

5h ago

---

**[Daily General Discussion June 01, 2026](https://www.reddit.com/r/ethereum/comments/1tti43r/daily_general_discussion_june_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[More than half of crypto losses in May came from bridge failures](https://www.reddit.com/r/ethereum/comments/1ttsgyv/more_than_half_of_crypto_losses_in_may_came_from/)**

https://preview.redd.it/i9m4zgybco4h1.png?width=2700&format=png&auto=webp&s=81f871e9f78b945ff86a1550d8d572929d906bcb We tracked 28 publicly disclosed exploits in May 2026, resulting in $51.9M in losses. What stood out wasn't the total amount lost. It was where the losses came from. Bridge-related incidents accounted for roughly 54% of all stolen funds. The interesting part is that these weren't the same vulnerability repeated: • Verification bypasses • TSS implementation failures • State poisoning attacks • Cross-chain message validation flaws Different architectures. Different codebases. Same outcome. Bridge security continues to be one of the most expensive unsolved problems in crypto. What do you think is driving bridges to remain such a frequent target despite the industry's continued focus on security?

21h ago

---

**[Building Security for Agentic AI in DeFi: Looking for a CTO / Blockchain Dev](https://www.reddit.com/r/ethereum/comments/1ttygz0/building_security_for_agentic_ai_in_defi_looking/)**

Right now, big companies are racing to deploy autonomous agents into the world with almost no audits, no real safeguards, and known vulnerabilities such as prompt injection and AI jailbreak. The result? DAOs and Web3 protocols are bleeding billions from automated exploits and uncontrolled agent actions. I gave my years to FinTech not for it to get filled with slop, but to provide democratic access to financial services. So, we’re fixing this. My team (with backgrounds from the world’s top %1 financial institutions) is building a governance protocol that brings strict, enforceable rules to autonomous AI workflows: starting with DeFi. Think of it as on-chain guardrails + auditability + human-in-the-loop controls for agentic systems. Safe agentic AI, not reckless AI. We’re currently in early-stage development and are actively looking for a strong technical developer to help us build the architecture (considering base primarily), iterate over the product, and build an MVP to collect early traction. If you’re deeply experienced in web3 and smart contract architectures, lets connect

18h ago

---

**[What's the actual plan for ETH to be valuable?](https://www.reddit.com/r/ethereum/comments/1ttppgw/whats_the_actual_plan_for_eth_to_be_valuable/)**

I used to think the plan was threefold: (1) a big economy that burns fees in ETH, (2) being the best store of value, and (3) constantly updating our views and improving the tech. I'd like to revisit each with what we know today. Asking in good faith as a holder. 1. A big economy that burns fees in ETH Fees are tiny right now. Is the plan ever going to change that? If the entire stock-trading market moved onto Ethereum, would the fees still be negligible? Is there a scenario where the fees actually make a difference — and is it realistic? 2. The best store of value What are the main differentiators from Bitcoin and Zcash? Quantum resistance? Privacy plus more functionality than Zcash? 3. We keep updating our views and improving the tech Money is a technology, and technologies get outdated and need new features (e.g. quantum resistance). The EF isn't self-sustainable, and by its own framing the goal is to step aside over time. So is there any self-sustaining entity responsible for keeping ETH the best and most up-to-date tech — or who actually owns that long game?

23h ago

---

**[Unencrypting private keys from keystore file and password](https://www.reddit.com/r/ethereum/comments/1ttddvd/unencrypting_private_keys_from_keystore_file_and/)**

Sorry if this sounds basic. This isn’t a “I lost my keys” post. Back in the early days I had an Ethereum wallet. It required you run a full node of ETH using geth on your machine starting with downloading the entire chain. You had your public keys and your private keys were stored in an encrypted keystore file. This wallet software now seems defunct and few want to DL the entire chain now anyway. To make a paper wallet, how would I “recover”/unencrypt my private keys from the keystore file and my password? DMs on the subject will be ignored.

1d ago

---

**[Daily General Discussion May 31, 2026](https://www.reddit.com/r/ethereum/comments/1tslsdo/daily_general_discussion_may_31_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Ethereum's Vitalik Buterin is rethinking how DeFi handles market crashes](https://www.coindesk.com/tech/2026/06/01/ethereum-s-vitalik-buterin-is-rethinking-how-defi-handles-market-crashes)**

In a research post published Monday, Buterin proposed creating index-tracking assets using options contracts rather than the debt-based structures that underpin much of DeFi today.

CoinDesk • 18h ago

---

**[BMNR Stock Slips After Bitmine Buys Ethereum Dip – Retail Demands 'HYPE-PURR-Style' Rally](https://finance.yahoo.com/markets/crypto/articles/bmnr-stock-slips-bitmine-buys-132744133.html)**

Bitmine announced a fresh purchase of more than 26,000 Ethereum tokens on Monday.

Yahoo Finance • 21h ago

---

**[Ethereum Is Winning But Token Holders Are Losing Faith In What Comes Next](https://www.forbes.com/sites/astanley/2026/05/30/ethereum-is-winning-but-its-token-holders-are-losing-faith/)**

Ethereum the network has become the financial infrastructure its supporters always dreamed of. But ETH the token has taken a different turn

Forbes • 2d ago

---

**[Tom Lee Says Crypto Investors Are 'Rage Quitting' After Mark Cuban Dumped All His Bitcoin](https://www.tradingview.com/news/stocktwits:1a7ecbe0f094b:0-tom-lee-says-crypto-investors-are-rage-quitting-after-mark-cuban-dumped-all-his-bitcoin/)**

Fundstrat’s Tom Lee said on Monday that the recent slump in crypto has triggered “rage quitting” among investors in response to Mark Cuban’s reported decision to sell off his Bitcoin (BTC) holdings.Bitmine Immersion Technologies (BMNR) Chairman Lee, speaking on CNBC’s SquawkBox, partly agreed when…

TradingView • 22h ago

---

**[Ethereum Meme Coin Little Pepe (LILPEPE) Nearly Sells Out Presale, Tops $28 Million Raised](https://markets.businessinsider.com/news/stocks/ethereum-meme-coin-little-pepe-lilpepe-nearly-sells-out-presale-tops-28-million-raised-1036215203)**

DUBAI, United Arab Emirates, June  01, 2026  (GLOBE NEWSWIRE) -- Little Pepe (LILPEPE), an Ethereum-based Layer 2 blockchain project combining mem...

markets.businessinsider.com • 10h ago

---

**[Current price of Ethereum for June 1, 2026](https://fortune.com/article/price-of-ethereum-06-01-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 22h ago

---

**[Insider Reveals Real Reason Ethereum Is Down 65% vs Bitcoin Since The Merge](https://beincrypto.com/ethereum-65-percent-down-bitcoin-merge/)**

An Ethereum insider blames the 65% drop versus Bitcoin since the Merge on execution debt, not market cycles.

BeInCrypto • 1d ago

---

**[Skip XRP and Buy This Top Cryptocurrency Instead](https://www.fool.com/investing/2026/05/30/skip-xrp-and-buy-this-top-cryptocurrency-instead/)**

If history is any guide, investors should be buying Ethereum, not XRP, right now.

The Motley Fool • 2d ago

---

**[Failed Ethereum ICO from 2016 just unlocked 1,003 ETH by exploiting itself](https://cryptoslate.com/failed-ethereum-ico-from-2016-just-unlocked-1003-eth-by-exploiting-itself/)**

A failed Ethereum ICO from 2016 unlocked 1,003 ETH after a self-exploit exposed a flaw in its own smart contract.

CryptoSlate • 19h ago

---

**[Tom Lee's BitMine Stock At Risk As Ethereum ETF Outflows Jump, Network Stats Fall - BitMine Immersion (NY](https://www.benzinga.com/crypto/26/05/52893379/tom-lees-bitmine-stock-at-risk-as-ethereum-etf-outflows-jump-network-stats-fall)**

Tom Lee's BitMine Immersion Technologies (NYSE:BMNR) stock has crashed to a crucial support level, and the ongoing Ethereum performance suggests that it may

Benzinga • 2d ago

---

---

## YouTube Videos: "ethereum"

**[Is the Bitcoin Thesis Broken? Tom Lee Weighs In](https://www.youtube.com/watch?v=NQuKKchNTu4)**

Tom Lee joins 'Squawk Box' to discuss the latest market trends, impact of AI, market outlook, state of crypto, and more.

📺 Fundstrat

👁️ 43K • 👍 967 • 💬 290 • ⏱️ 7:41 • 21h ago

---

**[Joseph Chalom: The Ethereum Bull Thesis in 2026 (Why Now)](https://www.youtube.com/watch?v=tTk6RZMtzVs)**

Joseph Chalom explains why ETH is not dead. Joseph Chalom is CEO of SharpLink, the second largest corporate ETH holder.

📺 The Rollup

👁️ 12K • 👍 345 • 💬 106 • ⏱️ 36:57 • 2d ago

---

**[Is Ethereum The Biggest Scam In Crypto](https://www.youtube.com/watch?v=iZg-fVH2MO4)**

Ethereum is the most hated coin in crypto, is it time to buy ETH? BITUNIX TRADE THE TOP COINS (available everywhere) ...

📺 Lark Davis

👁️ 15K • 👍 751 • 💬 223 • ⏱️ 7:50 • 2d ago

---

**[My Ethereum ETH Price Prediction for June 2026](https://www.youtube.com/watch?v=coIysqHtTjQ)**

Join the $1K to $100K Trading Challenge! - https://bit.ly/1kto100ktradingchallenge or use this ...

📺 Altcoin Doctor

👁️ 73 • 👍 3 • ⏱️ 8:17 • 1d ago

---

**[We could see some of the biggest stock market gains in our lifetime after 2026: Fundstrat&#39;s Tom Lee](https://www.youtube.com/watch?v=gpxPwY5apDg)**

Tom Lee, Fundstrat managing partner and head of research, and Fundstrat Capital CIO, joins 'Squawk Box' to discuss the latest ...

📺 CNBC Television

👁️ 243K • 👍 3K • 💬 713 • ⏱️ 9:01 • 23h ago

---

**[Gareth Soloway: Bitcoin Bear Flag Warning, Technical Chart Deep Dive — BTC, ETH, HYPE, SOL 2026](https://www.youtube.com/watch?v=XNEfvHeq-Ps)**

Bitcoin is sitting at a PIVOTAL support level — and the chart is forming what could become a dangerous bear flag. Gareth Soloway ...

📺 Gareth Soloway

👁️ 51K • 👍 3K • 💬 151 • ⏱️ 13:11 • 1d ago

---

**[🛑TRUMP IRAN🛑 XRP BTC ETH BAD NEWS](https://www.youtube.com/watch?v=6jOYuaOqLk8)**

xrp #bitcoin #hbar #xlm #eth Quality or Cheap merch, you vote here     ...

📺 CRYPTO with KLAUS

👁️ 4K • 👍 316 • 💬 89 • ⏱️ 13:29 • 16h ago

---

**[Bitcoin &amp; Ethereum at Key Support: Is the Crypto Bounce Coming?](https://www.youtube.com/watch?v=63VYWs9GuNs)**

Head Trader Benjamin Poole breaks down key support levels and bounce setups across four major crypto charts — Bitcoin, ...

📺 Verified Pro Traders

👁️ 2K • 👍 212 • 💬 33 • ⏱️ 9:19 • 13h ago

---

**[Before Ethereum… Vitalik Buterin Almost Joined Ripple](https://www.youtube.com/watch?v=5ySL7-XhqaQ)**

Before Ethereum existed, Vitalik applied to work at Ripple and even stayed on CTO David Schwartz's couch while arranging the ...

📺 CoinGecko

👁️ 1K • 👍 90 • 💬 9 • ⏱️ 2:55 • 1d ago

---

**[NEAR&#39;s rejected Ethereum pitch #shorts](https://www.youtube.com/watch?v=g0HQagqlsQM)**

New Uneasy Money: Illia Polosukhin recounts pitching NEAR's tech to the Ethereum Foundation, getting turned down on funding, ...

📺 Unchained

👁️ 291 • 👍 7 • ⏱️ 1:13 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
