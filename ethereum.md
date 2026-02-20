---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-02-20T02:09:51.620508+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- social
- cryptocurrency
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** February 20, 2026 at 02:09 UTC  
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

### $1,944.30

---

## Ethereum Chart

**24h:** -0.9%  
**7d:** -6.2%  
**30d:** -33.7%  
**90d:** -30.2%  
**1y:** -26.4%  

---

## Ethereum Market Stats

**Market Cap:** $235.92B
Rank #2

**Circulating Supply:** 120,692,388 ETH
No max supply

**All-Time High:** $4,946.05
-60.5%

**All-Time Low:** $0.43
+451413.8%

---

## Reddit: r/ethereum

**[Wall Street giants massively increased holdings in BitMine — the largest corporate ETH holder](https://www.reddit.com/r/ethereum/comments/1r93mxh/wall_street_giants_massively_increased_holdings/)**

New 13F filings show major financial institutions sharply increased positions in BitMine, a public company widely known as the largest corporate holder of Ethereum. Morgan Stanley now holds 12.2M shares (+26%), ARK 9.5M (+27%), BlackRock 9M (+166%), and Goldman Sachs 5.2M (+588%). Vanguard, Bank of America, Schwab, RBC, Citi and BNY Mellon also expanded exposure. In total, 457 institutional holders now control about 136.7M BitMine shares (~$2.86B). This suggests institutions are increasingly accessing ETH exposure via equity structures rather than direct custody — similar to how MicroStrategy functions as a BTC proxy. Full breakdown: https://btcusa.com/wall-street-giants-boost-bitmine-holdings-as-institutional-ethereum-exposure-expands/ Curious how people here see this trend — does equity-based ETH exposure accelerate or delay direct institutional ETH ownership?

9h ago

---

**[On FOCIL and native AA synergies](https://www.reddit.com/r/ethereum/comments/1r980ut/on_focil_and_native_aa_synergies/)**

There is an important synergy between FOCIL and AA (EIP-8141, which is based on 7701): 8141 makes not just smart accounts (including multisig, quantum-resistant signatures, key changes, gas sponsorship) first-class citizens, it also can do the same for privacy protocols (either indirectly via paymaster, or if we add 2D nonces, directly as a multi-tenant account). "First-class citizen" means that operations sent from that account can be included directly onchain as transactions, with no wrappers. FOCIL enables censorship-resistant rapid inclusion of any transaction. Hence, with FOCIL and 8141 together, anything, including smart wallet txs, gas sponsored txs, and even privacy protocol txs, can be included onchain through one of 17 different actors (the proposer or the includers) that are all chosen randomly in each slot. This gives us guaranteed rapid inclusion, meaning almost certainly within 1-2 slots, of any such tx, even in an adversarial environment. In this iteration, the FOCILs are 8 kB each, so they are very small in size. However, there is a natural future extension path to making them much larger, so that the majority of transactions to a block could, if needed, come through FOCILs. Such a design would have many of the properties of multiple concurrent proposer (MCP) designs, with the key difference being that FOCILs do not try to control the MEV-relevant "last look" role - that's still auctioned off with ePBS. The behavior of the last look role in "full MCP" depends strongly on the specifics of the design. The FOCIL design ensures that even if literally 100% of all slots get sold off via proposer-builder separation to a hostile actor that refuses to connect to public mempools, discriminates against certain applications, or is otherwise abusive, all transactions can still get quickly included. It's not eliminating the centralization of the proposer role, but it is heavily disempowering it. With EIP-8141 (AA), transactions from smart wallets, privacy protocols, etc, could be sent through a public mempool, and directly received by a FOCIL includer, no wrappers, "public broadcasters", or other intermediaries required. Ethereum is going hard.

7h ago

---

**[Daily General Discussion February 19, 2026](https://www.reddit.com/r/ethereum/comments/1r8rcjv/daily_general_discussion_february_19_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

20h ago

---

**[TIL the first ERC-20 token was deployed on November 3, 2015 — written in Solidity 0.1.6, months before the standard even had a name](https://www.reddit.com/r/ethereum/comments/1r94uig/til_the_first_erc20_token_was_deployed_on/)**

I've been going down a rabbit hole on early Ethereum contract archaeology and found something I thought was worth sharing. MistCoin was deployed on November 3, 2015 — just a few months after Ethereum's mainnet launch. It implements what we'd now recognize as the ERC-20 interface (transfer, balanceOf, totalSupply, approve/transferFrom), but ERC-20 as a formal standard didn't exist until Fabian Vogelsteller's EIP in late 2015, and wasn't widely adopted until 2017. A few things that stood out to me looking at the contract: **Solidity 0.1.6.** The syntax looks almost alien compared to modern Solidity. No `pragma`, no `view`/`pure`, no SafeMath. It's like looking at a fossil record of the language. **Fixed supply of 1,000,000 tokens.** No mint function, no owner privileges, no upgradability. The entire supply was assigned in the constructor and that was it. Immutable from day one. **The contract structure itself became the blueprint.** If you compare MistCoin's layout to the ERC-20 standard that was formalized later, the resemblance is striking. The pattern of mapping balances, emitting Transfer events, and the approve/transferFrom flow — it's all there. What I find interesting isn't the token itself, but what it tells us about how Ethereum's developer culture evolved. In 2015, people were hand-rolling token contracts from scratch with no standards, no templates, no OpenZeppelin. The fact that multiple developers independently converged on nearly identical patterns is what eventually made ERC-20 possible as a standard — it codified what was already emerging organically. The contract is still on-chain, obviously. Blockchain archaeology is one of those things that reminds you everything on Ethereum is permanent. The earliest experiments are still sitting there, readable and verifiable. More details on the history: [mistcoineth.com](https://mistcoineth.com) Has anyone else found interesting pre-standard contracts from 2015? I'd love to know what other early experiments are still sitting on mainnet.

9h ago

---

**[Glamsterdam Gas Repricing: share your feedback in the stakeholder survey](https://www.reddit.com/r/ethereum/comments/1r8pk7s/glamsterdam_gas_repricing_share_your_feedback_in/)**

Your guide to Ethereum's upcoming gas repricing changes

🔗 [gasrepricing.com](https://gasrepricing.com/) • 21h ago

---

**[Why EF should split AI evangelism between builders and storytellers](https://www.reddit.com/r/ethereum/comments/1r8n9xr/why_ef_should_split_ai_evangelism_between/)**

I was blown away by the recent interviews where Davide Crapis explained the exciting potential of Ethereum and AI agents. This feels like one of the biggest narrative opportunities the ecosystem has had in years. Precisely because the stakes are so high, I’d actually love to see EF lean into a very classic split of responsibilities: let the deepest technical people focus on building, coordination, and experimentation, and have a dedicated public‑facing person whose main job is interviews, conference talks, and selling the vision to AI founders and researchers -- similar to how Steve Wozniak and Steve Jobs complemented each other at Apple I understand the urge of putting Davide out there, he's good looking, charming, technically brilliant, and filled with enthusiasm. However in a lot of successful orgs, the people doing the most important technical work are not the ones doing the most public communication, not because they’re bad at it, but because their highest leverage is elsewhere. A specialized “storyteller for AI/agents,” backed by folks like Davide on the technical side, feels like the kind of structure that could really help Ethereum capture this moment.

23h ago

---

**[Episode 391 - Introduction to Lean Ethereum with Justin Drake](https://www.reddit.com/r/ethereum/comments/1r8pqnw/episode_391_introduction_to_lean_ethereum_with/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/Dad2UonQ9Ag) • 21h ago

---

**[Is it better to swap directly from cold wallet or nah?](https://www.reddit.com/r/ethereum/comments/1r8sy4h/is_it_better_to_swap_directly_from_cold_wallet_or/)**

90% of my coins are on Ledger and I mostly don’t touch them. But I need to get a little into more active trading and look to do more swaps. The problem tho, ledger’s fees are a bit higher than i expected and I don’t really want to be transferring money wallet to wallet. Swaps from cold wallet also feel like too much and that’s not even considering the routes. What everyone else does?

18h ago

---

**[Announcing the Platform Team at EF](https://www.reddit.com/r/ethereum/comments/1r8d9io/announcing_the_platform_team_at_ef/)**

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/02/17/platform) • 1d ago

---

**[Protocol Priorities Update for 2026](https://www.reddit.com/r/ethereum/comments/1r8j4dh/protocol_priorities_update_for_2026/)**

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/02/18/protocol-priorities-update-2026) • 1d ago

---

---

## Google News: "ethereum"

**[Harvard shakes up its crypto strategy by selling Bitcoin and purchasing Ethereum](https://fortune.com/2026/02/18/harvard-shakes-up-its-crypto-strategy/)**

The Ivy League school still has more money invested in Bitcoin than any other US stock.

Fortune • 1d ago

---

**[Harvard University Cuts Bitcoin ETF Holdings In Q4, Enters Ethereum ETF For First Time — Crypto Billionaire Changpeng Zhao Wonders 'What's Next'](https://finance.yahoo.com/news/harvard-university-cuts-bitcoin-etf-233111982.html)**

Harvard University has cut back on its Bitcoin (CRYPTO: BTC) position and dived into Ethereum (CRYPTO: ETH) for the first time, according to its latest 13F filing released on Friday. Harvard Loses Significant Chunk Of Bitcoin ETF Harvard Management Company,...

Yahoo Finance • 2h ago

---

**[Harvard Just Chose Ethereum Over Bitcoin — Here's Why](https://www.binance.com/en/square/post/292721446559250)**

Binance • 2d ago

---

**[Peter Thiel Exits ETHZilla Investment After Ethereum Treasury Stock Craters](https://finance.yahoo.com/news/peter-thiel-exits-ethzilla-investment-210444026.html)**

Billionaire investor Peter Thiel and Founders Fund held a 7.5% stake in Ethereum treasury company ETHZilla last year—but not anymore.

Yahoo Finance • 1d ago

---

**[Peter Thiel and Founders Fund exit Ethereum treasury firm ETHZilla, SEC filing shows](https://www.theblock.co/post/390285/peter-thiel-and-founders-fund-exit-ethereum-treasury-firm-ethzilla-sec-filing-shows)**

Peter Thiel fully exits ETHZilla, filing shows, as shares slide and the firm shifts from ether buildup to tokenization.

The Block • 1d ago

---

**[Peter Thiel Exits ETHZilla Investment After Ethereum Treasury Stock Craters](https://decrypt.co/358468/peter-thiel-exits-ethzilla-investment-ethereum-treasury-stock-craters)**

Billionaire investor Peter Thiel and Founders Fund held a 7.5% stake in Ethereum treasury company ETHZilla last year—but not anymore.

Decrypt • 1d ago

---

**[Bitcoin Price Falls to $68,000. Why Ethereum, XRP Are Struggling to Find Direction.](https://www.barrons.com/articles/bitcoin-price-xrp-ether-cryptos-ai-tech-stocks-5e824042?gaa_at=eafs&gaa_n=AWEtsqfPlWvG7oE4FNVgxQ8dq5d8iJBJy26DWpYfsaadKYXaEwomZJkCN7JV&gaa_ts=6997c5d7&gaa_sig=W62Od92dKzzZT6gogfIl-SwPvn4GxBrtw7Lk5MwwtL_wKg4LdjWF_vN07beVKhzi_rTTzB4nMvOZyl7ngkiDYg%3D%3D)**

Barron's • 1d ago

---

**[BlackRock begins acquiring ETH for upcoming Ethereum staking ETF](https://www.theblock.co/post/390244/blackrock-begins-acquiring-eth-upcoming-ethereum-staking-etf)**

A BlackRock affiliate purchased 4,000 seed shares of the fund for $100,000, providing the initial capital the trust will use to purchase ether, according to an amended S-1 filing.

The Block • 2d ago

---

**[Robinhood (HOOD) L2 testnet logs 4 million transactions in first week](https://www.coindesk.com/tech/2026/02/19/robinhood-testnet-l2-logs-4-million-transactions-following-vitalik-questions-of-ethereum-s-rollup-roadmap)**

Centralized exchanges are moving forward building their own blockchain infrastructure even as the broader Ethereum ecosystem debates its future.

CoinDesk • 9h ago

---

**[The Ethereum creator and early Polymarket backer doesn't like the direction prediction markets are headed](https://www.businessinsider.com/ethereum-creator-polymarket-backer-raises-concern-about-prediction-markets-future-2026-2)**

Vitalik Buterin, an early Polymarket backer, said prediction markets risk devolving into "corposlop" rather than having long-term financial utility.

Business Insider • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Coinbase Moves To ETH!🔥Robinhood vs Coinbase🔥SHOTS FIRED!](https://www.youtube.com/watch?v=jSKfTE-aZBQ)**

Optimism has plunged to a new all-time low after intense selling pressure overwhelmed recent demand. The decline accelerated ...

📺 Paul Barron Network

👁️ 29K • 👍 2K • 💬 124 • ⏱️ 15:12 • 5h ago

---

**[Blackrock Ethereum ETF SUBMITTED (Major Price Reaction)](https://www.youtube.com/watch?v=IDB13BcKlLE)**

Nick Valdez looks at the VERY bullish news regarding Blackrock and Ethereum. But the charts aren't as bullish! Will the bulls or ...

📺 Discover Crypto

👁️ 973 • 👍 59 • 💬 15 • ⏱️ 4:54 • 3h ago

---

**[The Next Phase of Ethereum: Prediction from Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=uwpXnuUsoiM)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 3K • 👍 68 • 💬 3 • ⏱️ 18:58 • 1d ago

---

**[BITCOIN &amp; ALTCOINS: This Changes EVERYTHING (for now)!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=vNgyvosrXYg)**

BITCOIN & ALTCOINS: This Changes EVERYTHING (for now)!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 1K • 👍 105 • 💬 12 • ⏱️ 16:59 • 1h ago

---

**[Tom Lee: The 44x Opportunity EVEN Bigger Than Bitcoin (2026 Prediction)](https://www.youtube.com/watch?v=DAkb7jk3oUE)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Claim your $20 Kalshi bonus when you ...

📺 Crypto Nutshell

👁️ 9K • 👍 368 • 💬 22 • ⏱️ 21:01 • 10h ago

---

**[ETH Ethereum Price Predictions: Possible Scenarios](https://www.youtube.com/watch?v=E4vrczwZzt8)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 119 • 👍 17 • 💬 4 • ⏱️ 16:35 • 2h ago

---

**[Ethereum Is About To Fix This Huge Privacy Problem #shorts](https://www.youtube.com/watch?v=eYtmkv__ZtI)**

Right now, every time someone sends you ETH, your wallet address is exposed publicly. Anyone can see your full history.

📺 Ivan on Tech

👁️ 788 • 👍 29 • 💬 2 • ⏱️ 0:42 • 5h ago

---

**[SUPER INVESTOR JUST SOLD HIS ENTIRE ETHEREUM POSITION](https://www.youtube.com/watch?v=Wsk-n6e2dh0)**

CHECK OUT MY LINKTREE FOR EXCHANGES I USE, BONUSES, FREE VIDEOS, AND MORE! https://linktr.ee/Myfinancialfriend I ...

📺 My Financial Friend

👁️ 7K • 👍 318 • 💬 34 • ⏱️ 12:25 • 1d ago

---

**[Raoul Pal: Don&#39;t SELL Before These EXACT Dates (New 2026 Bitcoin &amp; Ethereum Prediction)](https://www.youtube.com/watch?v=7S8_zqg7o8A)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Claim your $20 Kalshi bonus when you ...

📺 Crypto Nutshell

👁️ 20K • 👍 683 • 💬 39 • ⏱️ 21:56 • 1d ago

---

**[BITCOIN AND ETH: IT WILL GET WORSE!!!!](https://www.youtube.com/watch?v=tsEU2bvemCM)**

FREE TRAINING: https://www.bullmania.com EXCHANGES I USE (bybit, pionex): https://www.bullmania.com/partners My ...

📺 Ivan on Tech

👁️ 17K • 👍 1K • 💬 93 • ⏱️ 43:48 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
