---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-20T05:37:59.386897+00:00'
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

**Last Updated:** February 20, 2026 at 05:37 UTC  
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

### $1,940.09

---

## Ethereum Chart

**24h:** -1.0%  
**7d:** -6.0%  
**30d:** -33.5%  
**90d:** -30.1%  
**1y:** -26.2%  

---

## Ethereum Market Stats

**Market Cap:** $233.49B
Rank #2

**Circulating Supply:** 120,692,388 ETH
No max supply

**All-Time High:** $4,946.05
-60.9%

**All-Time Low:** $0.43
+447009.4%

---

## Reddit: r/ethereum

**[Wall Street giants massively increased holdings in BitMine — the largest corporate ETH holder](https://www.reddit.com/r/ethereum/comments/1r93mxh/wall_street_giants_massively_increased_holdings/)**

New 13F filings show major financial institutions sharply increased positions in BitMine, a public company widely known as the largest corporate holder of Ethereum. Morgan Stanley now holds 12.2M shares (+26%), ARK 9.5M (+27%), BlackRock 9M (+166%), and Goldman Sachs 5.2M (+588%). Vanguard, Bank of America, Schwab, RBC, Citi and BNY Mellon also expanded exposure. In total, 457 institutional holders now control about 136.7M BitMine shares (~$2.86B). This suggests institutions are increasingly accessing ETH exposure via equity structures rather than direct custody — similar to how MicroStrategy functions as a BTC proxy. Full breakdown: https://btcusa.com/wall-street-giants-boost-bitmine-holdings-as-institutional-ethereum-exposure-expands/ Curious how people here see this trend — does equity-based ETH exposure accelerate or delay direct institutional ETH ownership?

13h ago

---

**[On FOCIL and native AA synergies](https://www.reddit.com/r/ethereum/comments/1r980ut/on_focil_and_native_aa_synergies/)**

There is an important synergy between FOCIL and AA (EIP-8141, which is based on 7701): 8141 makes not just smart accounts (including multisig, quantum-resistant signatures, key changes, gas sponsorship) first-class citizens, it also can do the same for privacy protocols (either indirectly via paymaster, or if we add 2D nonces, directly as a multi-tenant account). "First-class citizen" means that operations sent from that account can be included directly onchain as transactions, with no wrappers. FOCIL enables censorship-resistant rapid inclusion of any transaction. Hence, with FOCIL and 8141 together, anything, including smart wallet txs, gas sponsored txs, and even privacy protocol txs, can be included onchain through one of 17 different actors (the proposer or the includers) that are all chosen randomly in each slot. This gives us guaranteed rapid inclusion, meaning almost certainly within 1-2 slots, of any such tx, even in an adversarial environment. In this iteration, the FOCILs are 8 kB each, so they are very small in size. However, there is a natural future extension path to making them much larger, so that the majority of transactions to a block could, if needed, come through FOCILs. Such a design would have many of the properties of multiple concurrent proposer (MCP) designs, with the key difference being that FOCILs do not try to control the MEV-relevant "last look" role - that's still auctioned off with ePBS. The behavior of the last look role in "full MCP" depends strongly on the specifics of the design. The FOCIL design ensures that even if literally 100% of all slots get sold off via proposer-builder separation to a hostile actor that refuses to connect to public mempools, discriminates against certain applications, or is otherwise abusive, all transactions can still get quickly included. It's not eliminating the centralization of the proposer role, but it is heavily disempowering it. With EIP-8141 (AA), transactions from smart wallets, privacy protocols, etc, could be sent through a public mempool, and directly received by a FOCIL includer, no wrappers, "public broadcasters", or other intermediaries required. Ethereum is going hard.

10h ago

---

**[Daily General Discussion February 19, 2026](https://www.reddit.com/r/ethereum/comments/1r8rcjv/daily_general_discussion_february_19_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

23h ago

---

**[How much do you know about Ethereum ?](https://www.reddit.com/r/ethereum/comments/1r9msb7/how_much_do_you_know_about_ethereum/)**

13m ago

---

**[Highlights from the All Core Developers Consensus (ACDC) Call #175](https://www.reddit.com/r/ethereum/comments/1r9ix9b/highlights_from_the_all_core_developers_consensus/)**

ACDC #175 saw steady progress on Glamsterdam’s ePBS Devnet and the formal selection of FOCIL as Hegotá’s Consensus Layer headliner.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-consensus-acdc-call-175/) • 3h ago

---

**[TIL the first ERC-20 token was deployed on November 3, 2015 — written in Solidity 0.1.6, months before the standard even had a name](https://www.reddit.com/r/ethereum/comments/1r94uig/til_the_first_erc20_token_was_deployed_on/)**

I've been going down a rabbit hole on early Ethereum contract archaeology and found something I thought was worth sharing. MistCoin was deployed on November 3, 2015 — just a few months after Ethereum's mainnet launch. It implements what we'd now recognize as the ERC-20 interface (transfer, balanceOf, totalSupply, approve/transferFrom), but ERC-20 as a formal standard didn't exist until Fabian Vogelsteller's EIP in late 2015, and wasn't widely adopted until 2017. A few things that stood out to me looking at the contract: **Solidity 0.1.6.** The syntax looks almost alien compared to modern Solidity. No `pragma`, no `view`/`pure`, no SafeMath. It's like looking at a fossil record of the language. **Fixed supply of 1,000,000 tokens.** No mint function, no owner privileges, no upgradability. The entire supply was assigned in the constructor and that was it. Immutable from day one. **The contract structure itself became the blueprint.** If you compare MistCoin's layout to the ERC-20 standard that was formalized later, the resemblance is striking. The pattern of mapping balances, emitting Transfer events, and the approve/transferFrom flow — it's all there. What I find interesting isn't the token itself, but what it tells us about how Ethereum's developer culture evolved. In 2015, people were hand-rolling token contracts from scratch with no standards, no templates, no OpenZeppelin. The fact that multiple developers independently converged on nearly identical patterns is what eventually made ERC-20 possible as a standard — it codified what was already emerging organically. The contract is still on-chain, obviously. Blockchain archaeology is one of those things that reminds you everything on Ethereum is permanent. The earliest experiments are still sitting there, readable and verifiable. More details on the history: [mistcoineth.com](https://mistcoineth.com) Has anyone else found interesting pre-standard contracts from 2015? I'd love to know what other early experiments are still sitting on mainnet.

12h ago

---

**[Glamsterdam Gas Repricing: share your feedback in the stakeholder survey](https://www.reddit.com/r/ethereum/comments/1r8pk7s/glamsterdam_gas_repricing_share_your_feedback_in/)**

Your guide to Ethereum's upcoming gas repricing changes

🔗 [gasrepricing.com](https://gasrepricing.com/) • 1d ago

---

**[Why EF should split AI evangelism between builders and storytellers](https://www.reddit.com/r/ethereum/comments/1r8n9xr/why_ef_should_split_ai_evangelism_between/)**

I was blown away by the recent interviews where Davide Crapis explained the exciting potential of Ethereum and AI agents. This feels like one of the biggest narrative opportunities the ecosystem has had in years. Precisely because the stakes are so high, I’d actually love to see EF lean into a very classic split of responsibilities: let the deepest technical people focus on building, coordination, and experimentation, and have a dedicated public‑facing person whose main job is interviews, conference talks, and selling the vision to AI founders and researchers -- similar to how Steve Wozniak and Steve Jobs complemented each other at Apple I understand the urge of putting Davide out there, he's good looking, charming, technically brilliant, and filled with enthusiasm. However in a lot of successful orgs, the people doing the most important technical work are not the ones doing the most public communication, not because they’re bad at it, but because their highest leverage is elsewhere. A specialized “storyteller for AI/agents,” backed by folks like Davide on the technical side, feels like the kind of structure that could really help Ethereum capture this moment.

1d ago

---

**[Episode 391 - Introduction to Lean Ethereum with Justin Drake](https://www.reddit.com/r/ethereum/comments/1r8pqnw/episode_391_introduction_to_lean_ethereum_with/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/Dad2UonQ9Ag) • 1d ago

---

**[Is it better to swap directly from cold wallet or nah?](https://www.reddit.com/r/ethereum/comments/1r8sy4h/is_it_better_to_swap_directly_from_cold_wallet_or/)**

90% of my coins are on Ledger and I mostly don’t touch them. But I need to get a little into more active trading and look to do more swaps. The problem tho, ledger’s fees are a bit higher than i expected and I don’t really want to be transferring money wallet to wallet. Swaps from cold wallet also feel like too much and that’s not even considering the routes. What everyone else does?

22h ago

---

---

## Google News: "ethereum"

**[Harvard shakes up its crypto strategy by selling Bitcoin and purchasing Ethereum](https://fortune.com/2026/02/18/harvard-shakes-up-its-crypto-strategy/)**

The Ivy League school still has more money invested in Bitcoin than any other US stock.

Fortune • 1d ago

---

**[Peter Thiel and Founders Fund exit Ethereum treasury firm ETHZilla, SEC filing shows](https://www.theblock.co/post/390285/peter-thiel-and-founders-fund-exit-ethereum-treasury-firm-ethzilla-sec-filing-shows)**

Peter Thiel fully exits ETHZilla, filing shows, as shares slide and the firm shifts from ether buildup to tokenization.

The Block • 1d ago

---

**[Peter Thiel Exits ETHZilla Investment After Ethereum Treasury Stock Craters](https://finance.yahoo.com/news/peter-thiel-exits-ethzilla-investment-210444026.html)**

Billionaire investor Peter Thiel and Founders Fund held a 7.5% stake in Ethereum treasury company ETHZilla last year—but not anymore.

Yahoo Finance • 1d ago

---

**[Peter Thiel Exits ETHZilla Investment After Ethereum Treasury Stock Craters](https://decrypt.co/358468/peter-thiel-exits-ethzilla-investment-ethereum-treasury-stock-craters)**

Billionaire investor Peter Thiel and Founders Fund held a 7.5% stake in Ethereum treasury company ETHZilla last year—but not anymore.

Decrypt • 1d ago

---

**[BlackRock begins acquiring ETH for upcoming Ethereum staking ETF](https://www.theblock.co/post/390244/blackrock-begins-acquiring-eth-upcoming-ethereum-staking-etf)**

A BlackRock affiliate purchased 4,000 seed shares of the fund for $100,000, providing the initial capital the trust will use to purchase ether, according to an amended S-1 filing.

The Block • 2d ago

---

**[The Ethereum creator and early Polymarket backer doesn't like the direction prediction markets are headed](https://www.businessinsider.com/ethereum-creator-polymarket-backer-raises-concern-about-prediction-markets-future-2026-2)**

Vitalik Buterin, an early Polymarket backer, said prediction markets risk devolving into "corposlop" rather than having long-term financial utility.

Business Insider • 1d ago

---

**[Bitcoin, Ethereum, XRP Waffle as Crypto Crisis Deepens. Why It Could Get Worse.](https://www.barrons.com/articles/bitcoin-ethereum-xrp-crypto-crisis-e43f4227?gaa_at=eafs&gaa_n=AWEtsqd3mJ3a6OIgU87_LKoA2DuHIA7pKyPkAdyx-pyp32u33q9oaqwRRc0j&gaa_ts=6997f69f&gaa_sig=meM_0PJhUrGfPiRoUtUtj23XaipVQs82out91GNvdvCZT9S0W5oBynPu_FhaUMbYNPodUJZ0dorvjHJ8FQdUgQ%3D%3D)**

Barron's • 8h ago

---

**[Ethereum 50% staking figure by Santiment draws criticism from researchers](https://www.coindesk.com/business/2026/02/18/ethereum-s-50-staking-milestone-triggers-backlash-over-misleading-supply-data)**

CoinShares and Ethplorer.io say the 50% figure reflects cumulative deposits, not active staked ETH, which remains closer to 30% of supply.

CoinDesk • 19h ago

---

**[Tom Lee Expects 'Defining Year for Ethereum' as BitMine Buys ETH Amid 'Rock Bottom' Vibes](https://finance.yahoo.com/news/tom-lee-expects-defining-ethereum-165418778.html)**

BitMine Immersion Technologies is sitting on a nearly $8 billion unrealized loss, but Tom Lee remains optimistic about Ethereum.

Yahoo Finance • 2d ago

---

**[Bitmine Immersion: Ethereum's Biggest Public Whale (NYSE:BMNR)](https://seekingalpha.com/article/4871611-bitmine-immersion-ethereum-biggest-public-whale)**

Asymmetric upside for Bitmine Immersion Technologies is likely if Ethereum (and the whole crypto space) recovers from the recent downtrend. More on BMNR stock.

Seeking Alpha • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Coinbase Moves To ETH!🔥Robinhood vs Coinbase🔥SHOTS FIRED!](https://www.youtube.com/watch?v=jSKfTE-aZBQ)**

Optimism has plunged to a new all-time low after intense selling pressure overwhelmed recent demand. The decline accelerated ...

📺 Paul Barron Network

👁️ 37K • 👍 2K • 💬 133 • ⏱️ 15:12 • 9h ago

---

**[Blackrock Ethereum ETF SUBMITTED (Major Price Reaction)](https://www.youtube.com/watch?v=IDB13BcKlLE)**

Nick Valdez looks at the VERY bullish news regarding Blackrock and Ethereum. But the charts aren't as bullish! Will the bulls or ...

📺 Discover Crypto

👁️ 2K • 👍 74 • 💬 19 • ⏱️ 4:54 • 6h ago

---

**[The Next Phase of Ethereum: Prediction from Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=uwpXnuUsoiM)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 3K • 👍 69 • 💬 4 • ⏱️ 18:58 • 1d ago

---

**[Tom Lee: The 44x Opportunity EVEN Bigger Than Bitcoin (2026 Prediction)](https://www.youtube.com/watch?v=DAkb7jk3oUE)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Claim your $20 Kalshi bonus when you ...

📺 Crypto Nutshell

👁️ 10K • 👍 391 • 💬 22 • ⏱️ 21:01 • 14h ago

---

**[🚨 BREAKING: Deep State 911 Insider BUYS ETHEREUM (Howard Lutnick) ($20K ETH) (Tom Lee)](https://www.youtube.com/watch?v=F22KAmIsKd4)**

Donation Address: yourfriendsommi.eth / yourfriendsommi.pls Click Subscribe + Bell Button 'All' Follow on Twitter: ...

📺 🌟yourfriendsommi

👁️ 212 • 👍 36 • 💬 7 • ⏱️ 16:03 • 1h ago

---

**[BITCOIN &amp; ALTCOINS: This Changes EVERYTHING (for now)!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=vNgyvosrXYg)**

BITCOIN & ALTCOINS: This Changes EVERYTHING (for now)!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 3K • 👍 156 • 💬 40 • ⏱️ 16:59 • 5h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=LCBhYanceJE)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 128 • 💬 10 • ⏱️ 4:52 • 14h ago

---

**[Your Next Move Is CRUCIAL! (ETH Pumped +341% Last Time)](https://www.youtube.com/watch?v=okN2OECB1uQ)**

Get $450 Off Our New AI Indicators: https://tradeconfidentportal.io/indicators Join Trade Confident: Get 25% Off Your 1st Month: ...

📺 Trade Confident

👁️ 660 • 👍 19 • 💬 2 • ⏱️ 4:36 • 1d ago

---

**[BITCOIN AND ETH: IT WILL GET WORSE!!!!](https://www.youtube.com/watch?v=tsEU2bvemCM)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 17K • 👍 1K • 💬 93 • ⏱️ 43:48 • 19h ago

---

**[SUPER INVESTOR JUST SOLD HIS ENTIRE ETHEREUM POSITION](https://www.youtube.com/watch?v=Wsk-n6e2dh0)**

CHECK OUT MY LINKTREE FOR EXCHANGES I USE, BONUSES, FREE VIDEOS, AND MORE! https://linktr.ee/Myfinancialfriend I ...

📺 My Financial Friend

👁️ 7K • 👍 319 • 💬 34 • ⏱️ 12:25 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
