---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-06T19:34:38.758956+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- news
- videos
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 06, 2026 at 19:34 UTC  
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

### $1,977.36

---

## Ethereum Chart

**24h:** -4.5%  
**7d:** +0.8%  
**30d:** +8.5%  
**90d:** -35.3%  
**1y:** -7.5%  

---

## Ethereum Market Stats

**Market Cap:** $239.08B
Rank #2

**Circulating Supply:** 120,692,086 ETH
No max supply

**All-Time High:** $4,946.05
-60.0%

**All-Time Low:** $0.43
+457143.9%

---

## Reddit: r/ethereum

**[We verified Vitalik's 2015 token contract and discovered it wasn't compiled with Solidity - it's Serpent](https://www.reddit.com/r/ethereum/comments/1rmheom/we_verified_vitaliks_2015_token_contract_and/)**

I've been working on verifying source code for the oldest contracts on Ethereum, and this one took days to crack. The contract: 0xa2e3680acaf5d2298697bdc016cf75a929385463 Deployed by Vitalik on November 12, 2015 (block 530,996). It's a token contract implementing the standardized currency API from the early ethereum/dapp-bin repo. 1,000,000 initial supply, approve/transfer mechanics - basically a proto-ERC-20. The problem: We tried compiling currency.sol with every Solidity compiler version from that era. Every archived soljson release from v0.1.1 through v0.3.6, nightlies from Sep-Dec 2015, native C++ solc builds from the webthree-umbrella repo, optimizer on and off. Nothing matched. The breakthrough: Three clues pointed us away from Solidity entirely: The on-chain constructor starts with 6000603f53 (MSTORE8-based memory init). Every Solidity version produces 60606040525b (the free memory pointer pattern). This is a fundamentally different code generation approach. The runtime code uses MSIZE, SWAP1, MSIZE, ADD for memory allocation. This is the Serpent compiler's alloc() pattern - not found in any version of solc. Two function selectors didn't match the Solidity source: disapprove() instead of unapprove(), and isApprovedOnceFor() instead of isApprovedOnce(). The answer: The contract was compiled from currency.se (the Serpent version), not currency.sol. The ethereum/dapp-bin repo had both implementations side by side. Vitalik deployed his own language's version. Compiled with the Serpent compiler at commit f0b4128 (Oct 15, 2015) - byte-for-byte identical, all 1,661 bytes. Full methodology, source, and proof: github.com/cartoonitunes/vitalik-currency-verification We've submitted a manual verification request to Etherscan since they don't support Serpent as a verification language. Hopefully they can add it as a verified contract with source. This is part of a broader effort to verify and preserve the earliest contracts on Ethereum. A lot of historically important contracts from 2015-2016 are still unverified because the compiler versions are too old for Etherscan's automated tools.

3h ago

---

**[Daily General Discussion March 06, 2026](https://www.reddit.com/r/ethereum/comments/1rm5yqw/daily_general_discussion_march_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

13h ago

---

**[ZK VMs made verifiable computation accessible to any developer. The prover networks running them require your full plaintext data. YIKES](https://www.reddit.com/r/ethereum/comments/1rmg9sa/zk_vms_made_verifiable_computation_accessible_to/)**

Zero-knowledge cryptography went through three phases. First: hand-crafted arithmetic circuits, only accessible to deep researchers. Second: ZK virtual machines — suddenly any developer could write verifiable code in Rust or C. Third: prover networks (Succinct, Boundless/RiscZero) that let you delegate the heavy proof generation to external infrastructure. Each phase made the technology more accessible. Each phase also moved the user's data further from their control. Prover networks require your full plaintext data to generate proofs. For rollups, this is a non-issue — public ledger, no privacy expectation, and what you gain (succinctness — compressing thousands of transactions into a single proof) is worth the trade. That's the use case these networks were built for, and they served it well. The problem emerges when you extend this model to user-facing applications. Verifiable identity: proving you hold a valid passport, proving you're over 18, without disclosing the underlying data. Private AI inference: running a model on your data without the model owner seeing your inputs or you seeing their weights. Decentralized exchanges with private order books. In all of these, delegating to a prover network means surrendering exactly the inputs you need to keep private. I sat down with a researcher at ChainSafe who's working on this specific problem. His approach: adding MPC (multi-party computation) to ZK VMs so proof generation can be delegated privately. Multiple parties each hold a secret share of the data, compute their portion, and combine results — no single party ever sees the full picture. He calls it "make ZK VMs ZK again." He also covered a near-term approach to the deepfake problem: attested sensors that cryptographically sign photo/video metadata at capture, combined with verifiable edit histories. You can't yet verify what IS AI-generated. But you can prove everything that is human — a reverse approach. Prove provenance instead of detecting fakes. The full conversation covers ZK, MPC, and FHE (the "holy trinity of programmable cryptography"), explained through photography analogies that are genuinely useful for building intuition. We filmed it across Taipei — street markets, a botanical garden, a tea ceremony. Full interview: https://youtu.be/PnEivfTpnA8 ————— If we're meeting for the first time, hi 👋! I started building my channel to spread the good word on good work in crypto — something with substance and humanity. A like, sub, and comment goes a long way to supporting me, so please consider doing so!

🔗 [youtu.be](https://youtu.be/PnEivfTpnA8) • 4h ago

---

**[All you need to know about Ethereum Hegota Upgrade](https://www.reddit.com/r/ethereum/comments/1rm299u/all_you_need_to_know_about_ethereum_hegota_upgrade/)**

Hegotá is the official name of a major Ethereum network upgrade planned for the second half of 2026, following the Glamsterdam upgrade expected earlier in the year, and marking Ethereum’s continued shift toward a biannual release cycle. The name blends Bogotá, the Devcon host city, with the star Heze. https://etherworld.co/all-you-need-to-know-about-ethereum-hegota-upgrade/

16h ago

---

**[DigixDAO: The First Major DAO Crowdsale — $5.5M Raised in Under 24 Hours (March 29, 2016)](https://www.reddit.com/r/ethereum/comments/1rmerqx/digixdao_the_first_major_dao_crowdsale_55m_raised/)**

On March 29, 2016, Digix Global launched what became the first major DAO crowdsale on Ethereum. It raised $5.5 million in under 24 hours — at a time when Ethereum's total market cap was around $600 million. What it was: DigixDAO was a governance token (DGD) for a project aiming to tokenize physical gold bars on Ethereum. The crowdsale contract was deployed at block 1,239,208 and compiled with Solidity v0.3.0. Why it mattered: - It was the first DAO-style crowdsale to raise serious money on Ethereum - It proved that decentralized fundraising could work at scale, months before The DAO - The speed of the raise ($5.5M in <24h) shocked even the Ethereum community - It directly inspired the wave of ICOs that followed in 2017 Independent verification: Developer Piper Merriam independently verified the contract code before the sale, establishing one of the earliest examples of third-party smart contract auditing. The original community discussion happened right here on r/ethereum, with this thread documenting the reaction in real-time. Contract: 0xf0160428a8552ac9bb7e050d90eeade4ddd52843 Full writeup with sources: EthereumHistory.com This was just 7 months before The DAO — and in many ways, it was the proof of concept that made The DAO feel possible. We're documenting these pre-2017 contracts before the context disappears.

5h ago

---

**[Ethereal news weekly #14 | ePBS first devnet live, Aave Labs temp check passed, Synthesis AI + human hackathon](https://www.reddit.com/r/ethereum/comments/1rmcnq6/ethereal_news_weekly_14_epbs_first_devnet_live/)**

ePBS first devnet live, Aave Labs temp check passed, Synthesis AI + human hackathon

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-14/) • 7h ago

---

**[TerraNullius: The Ethereum Message Board from Block 49,880 (August 7, 2015) — Still Getting Claims in 2026](https://www.reddit.com/r/ethereum/comments/1rlidmx/terranullius_the_ethereum_message_board_from/)**

Two weeks after Ethereum's genesis block, a Reddit user named "Semiel" deployed one of the earliest smart contracts on the network: TerraNullius. What it does: Anyone can "claim" a hex coordinate and attach a message to it — a permanent, uncensorable message board on the blockchain. No tokens, no governance, no economic incentive. Just messages, forever. The numbers: - Deployed at block 49,880 (August 7, 2015) - Compiled with Solidity v0.1.1 - 25 claims in 2015, then it sat mostly dormant - 687 claims during the 2021 NFT boom (people realized these were basically proto-NFTs) - 805 total transactions and counting — still active in 2026 It was referenced by the Guinness World Records and is one of the earliest surviving interactive contracts on Ethereum. The original announcement was a Reddit post right here on r/ethereum, with Semiel sharing a Pastebin script so people could interact with it. What's fascinating is how it predates every pattern we now take for granted — ERC-20, ERC-721, ENS, DAOs. This was someone experimenting with permanence on a chain that was two weeks old. Contract: 0x6e38A457C722C6011B2dfa06d49240e797844d66 Full writeup with sources and verification: EthereumHistory.com If anyone has stories about early Ethereum experiments like this, I'd love to hear them. We're trying to document the pre-2017 era before the context is lost entirely.

1d ago

---

**[Daily General Discussion March 05, 2026](https://www.reddit.com/r/ethereum/comments/1rl9qdi/daily_general_discussion_march_05_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[X402 Real Use Cases](https://www.reddit.com/r/ethereum/comments/1rlmuqu/x402_real_use_cases/)**

I spent 1 month talking to 10 SaaS and AI companies trying to sell them on x402. Here's what almost all of them said: "Why would an AI agent pay per usage for a certain app when you can just create a SaaS product, ask for a top-up, and internally use credits?" x402 doesn't replace the per-usage model. It solves one specific problem: no human in the loop. There are 2 use cases: Anonymous autonomous agent. No account. No signup. No pre-loaded balance. Pays mid-task and moves on. Humans with accounts created - that want to automate - a top-up credit model wins with pay per usage with credits. BUT Almost every SaaS would want you to create your account. SO x402 is really only good for automatic top-ups / payments. Change my mind.

1d ago

---

**[The endgame for Ethereum UX? A breakdown of EIP-7702 (SetCode Transactions)](https://www.reddit.com/r/ethereum/comments/1rlpxm9/the_endgame_for_ethereum_ux_a_breakdown_of/)**

Hi everyone, If you've been following the Account Abstraction roadmap, you know the community pivoted hard toward EIP-7702, a proposal driven by Vitalik to allow EOAs (standard wallets) to temporarily act like smart contracts. I write a lot about blockchain architecture, and I noticed that while the hype around "gasless transactions" is loud, the actual mechanics of how EIP-7702 achieves this safely aren't discussed enough. I published an architectural breakdown to clarify how this works under the hood. The core of the design is the SetCode transaction type. Instead of permanently migrating an EOA to a smart contract, EIP-7702 allows a transaction to temporarily attach smart contract code to an EOA for the exact duration of that single transaction. The deep dive covering: How this solves the security debates around previous proposals. The technical flow of batching operations What this means for the current ERC-4337 infrastructure. I'd love to hear from people that building in the space: How quickly do you expect it to be broadly used

1d ago

---

---

## Google News: "ethereum"

**[Bitcoin Price Predictions Flip Bullish, But Ethereum Is Still Stuck](https://decrypt.co/360131/bitcoin-price-predictions-flip-bullish-but-ethereum-stuck)**

Prediction market traders are becoming more bullish on Bitcoin's near-term price, but they're not as confident on Ethereum.

Decrypt • 2d ago

---

**[Vitalik Buterin calls for bolder experimentation in Ethereum's app layer while preserving core principles](https://www.theblock.co/post/392621/vitalik-buterin-calls-for-bolder-experimentation-in-ethereums-app-layer-while-preserving-core-principles)**

Vitalik Buterin has urged Ethereum developers to experiment more boldly at the app layer while preserving the network’s core principles.

theblock.co • 8h ago

---

**[Got $1,000? This Cryptocurrency Is a No-Brainer Buy for Long-Term Holding](https://www.fool.com/investing/2026/03/05/got-1000-this-cryptocurrency-is-a-no-brainer-buy-f/)**

The cryptocurrency's status as the leader in decentralized finance makes it hard to beat.

The Motley Fool • 1d ago

---

**[Bitcoin, XRP, Ethereum Are Having a Great Week. Why Cryptos Are on the Up.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-iran-war-cryptos-ba05311d?gaa_at=eafs&gaa_n=AWEtsqfuK45xBQqYvZCKLfisF7yzfkxn-qndkwVtUmS_gLJ7fm9k04krAhmH&gaa_ts=69ab253b&gaa_sig=xJtoPFJRC6v8PkHJGmyxvu4mnLtgQZUWszy9tWruZLucSmZ6AzqDDaki5a-5F6sY_1yomtm8Eq2OceAIF30R8Q%3D%3D)**

Barron's • 1d ago

---

**[Ethereum Foundation wants the network to be the trust layer for AI](https://www.coindesk.com/tech/2026/03/04/ethereum-foundation-wants-the-network-to-be-the-trust-layer-for-ai)**

Davide Crapis, the foundation's AI lead,  sees the network acting as a coordination and verification layer in an increasingly AI-mediated world.

CoinDesk • 2d ago

---

**[Bit Digital Inc. Reports Monthly Ethereum Treasury and Staking Metrics for February 2026](https://bit-digital.com/press-releases/bit-digital-inc-reports-monthly-ethereum-treasury-and-staking-metrics-for-february-2026/)**

Bit Digital, Inc. (Nasdaq: BTBT), today announced its monthly Ethereum (ETH) treasury and staking metrics for the month of February 2026.

Bit Digital • 1d ago

---

**[31.6 Million ETH Leaves Exchanges as Vitalik Calls for Ethereum “Sanctuary” Tech](https://finance.yahoo.com/news/31-6-million-eth-leaves-070249895.html)**

ETH accumulation off exchanges continues to surge in early March, while Vitalik Buterin calls for building sanctuary technologies for ETH.

Yahoo Finance • 2d ago

---

**[Current price of Ethereum for March 6, 2026](https://fortune.com/article/price-of-ethereum-03-06-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 5h ago

---

**[While Bitcoin and Ethereum Consolidate, This Altcoin Is Quietly Preparing for a Major Rally](https://www.tradingview.com/news/coinpedia:2a6c70131094b:0-while-bitcoin-and-ethereum-consolidate-this-altcoin-is-quietly-preparing-for-a-major-rally/)**

While Bitcoin and Ethereum continue to move sideways, one major altcoin appears to be quietly building momentum beneath the surface. Growing institutional interest and a tightening technical structure suggest that Solana’s price could be positioning itself for a significant move in the coming weeks…

TradingView • 7h ago

---

**[Bullish sees Bitcoin, Ethereum volatility almost double in February (BLSH:NYSE)](https://seekingalpha.com/news/4561826-bullish-sees-bitcoin-ethereum-volatility-almost-double-in-february)**

Seeking Alpha • 6h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Will Not Stay This Cheap! ⚠️ ETH Crypto Token Analysis](https://www.youtube.com/watch?v=jrKbEBTxqFA)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 2K • 👍 117 • 💬 21 • ⏱️ 10:24 • 7h ago

---

**[Whales Are Loading Up on BTC, ETH, ASTER &amp; PUMP – What Do They Know? 👀](https://www.youtube.com/watch?v=qkFFwZjfOA4)**

We analyze the latest crypto whale activity and what it could mean for the broader market. On-chain data is showing large ...

📺 Altcoin Buzz

👁️ 592 • 👍 51 • 💬 171 • ⏱️ 12:09 • 3h ago

---

**[&quot;People Don’t Know How Massive MARCH Will Be for Crypto&quot;: Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=7oRNY59aeTo)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 2K • 👍 61 • 💬 25 • ⏱️ 19:52 • 1d ago

---

**[Tom Lee has gone insane (ethereum).](https://www.youtube.com/watch?v=KUl2p8MQGBg)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 20K • 👍 598 • 💬 21 • ⏱️ 1:16 • 1d ago

---

**[URGENT ETHEREUM UPDATE🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=TEAc7s0s4rM)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 283 • 👍 19 • 💬 1 • ⏱️ 5:16 • 9h ago

---

**[Bitcoin Bottom Forming? ETH Accumulation Surges While Crypto Fear Spikes | MSTR BMNR](https://www.youtube.com/watch?v=qXEAgObFIqo)**

I'm giving away my Weekly Trading Strategy + my new book Money Game FREE ...

📺 MONEY GAME

👁️ 1K • 👍 77 • 💬 12 • ⏱️ 31:22 • 8h ago

---

**[BITCOIN: Watch Out for This Move! (big warning) - BTC, ETH Price Prediction Today](https://www.youtube.com/watch?v=qFlz6OhhLK4)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 6K • 👍 440 • 💬 88 • ⏱️ 12:55 • 9h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=FV9pHXeiaxk)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 162 • 💬 6 • ⏱️ 3:54 • 1d ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=kQI9AEFYc50)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 508 • 👍 62 • 💬 1 • ⏱️ 5:14 • 4h ago

---

**[Sui Founder Explains Why Ethereum &amp; Solana Will Be Left Behind | E161](https://www.youtube.com/watch?v=5Tunu3t7kQ4)**

Evan Cheng co-founded SUI after leading Facebook's Libra project - then threw away everything they built because it wasn't good ...

📺 When Shift Happens

👁️ 14K • 👍 439 • 💬 154 • ⏱️ 49:16 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
