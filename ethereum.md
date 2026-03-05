---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-05T21:37:17.361859+00:00'
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

**Last Updated:** March 05, 2026 at 21:37 UTC  
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

### $2,095.88

---

## Ethereum Chart

**24h:** -2.3%  
**7d:** +7.9%  
**30d:** -3.1%  
**90d:** -31.4%  
**1y:** -5.6%  

---

## Ethereum Market Stats

**Market Cap:** $252.56B
Rank #2

**Circulating Supply:** 120,692,109 ETH
No max supply

**All-Time High:** $4,946.05
-57.7%

**All-Time Low:** $0.43
+483214.4%

---

## Reddit: r/ethereum

**[Daily General Discussion March 05, 2026](https://www.reddit.com/r/ethereum/comments/1rl9qdi/daily_general_discussion_march_05_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

15h ago

---

**[TerraNullius: The Ethereum Message Board from Block 49,880 (August 7, 2015) — Still Getting Claims in 2026](https://www.reddit.com/r/ethereum/comments/1rlidmx/terranullius_the_ethereum_message_board_from/)**

Two weeks after Ethereum's genesis block, a Reddit user named "Semiel" deployed one of the earliest smart contracts on the network: TerraNullius. What it does: Anyone can "claim" a hex coordinate and attach a message to it — a permanent, uncensorable message board on the blockchain. No tokens, no governance, no economic incentive. Just messages, forever. The numbers: - Deployed at block 49,880 (August 7, 2015) - Compiled with Solidity v0.1.1 - 25 claims in 2015, then it sat mostly dormant - 687 claims during the 2021 NFT boom (people realized these were basically proto-NFTs) - 805 total transactions and counting — still active in 2026 It was referenced by the Guinness World Records and is one of the earliest surviving interactive contracts on Ethereum. The original announcement was a Reddit post right here on r/ethereum, with Semiel sharing a Pastebin script so people could interact with it. What's fascinating is how it predates every pattern we now take for granted — ERC-20, ERC-721, ENS, DAOs. This was someone experimenting with permanence on a chain that was two weeks old. Contract: 0x6e38A457C722C6011B2dfa06d49240e797844d66 Full writeup with sources and verification: EthereumHistory.com If anyone has stories about early Ethereum experiments like this, I'd love to hear them. We're trying to document the pre-2017 era before the context is lost entirely.

7h ago

---

**[X402 Real Use Cases](https://www.reddit.com/r/ethereum/comments/1rlmuqu/x402_real_use_cases/)**

I spent 1 month talking to 10 SaaS and AI companies trying to sell them on x402. Here's what almost all of them said: "Why would an AI agent pay per usage for a certain app when you can just create a SaaS product, ask for a top-up, and internally use credits?" x402 doesn't replace the per-usage model. It solves one specific problem: no human in the loop. There are 2 use cases: Anonymous autonomous agent. No account. No signup. No pre-loaded balance. Pays mid-task and moves on. Humans with accounts created - that want to automate - a top-up credit model wins with pay per usage with credits. BUT Almost every SaaS would want you to create your account. SO x402 is really only good for automatic top-ups / payments. Change my mind.

4h ago

---

**[The endgame for Ethereum UX? A breakdown of EIP-7702 (SetCode Transactions)](https://www.reddit.com/r/ethereum/comments/1rlpxm9/the_endgame_for_ethereum_ux_a_breakdown_of/)**

Hi everyone, If you've been following the Account Abstraction roadmap, you know the community pivoted hard toward EIP-7702, a proposal driven by Vitalik to allow EOAs (standard wallets) to temporarily act like smart contracts. I write a lot about blockchain architecture, and I noticed that while the hype around "gasless transactions" is loud, the actual mechanics of how EIP-7702 achieves this safely aren't discussed enough. I published an architectural breakdown to clarify how this works under the hood. The core of the design is the SetCode transaction type. Instead of permanently migrating an EOA to a smart contract, EIP-7702 allows a transaction to temporarily attach smart contract code to an EOA for the exact duration of that single transaction. The deep dive covering: How this solves the security debates around previous proposals. The technical flow of batching operations What this means for the current ERC-4337 infrastructure. I'd love to hear from people that building in the space: How quickly do you expect it to be broadly used

2h ago

---

**[Built a Rust tool to scan Ethereum smart contracts for vulnerabilities](https://www.reddit.com/r/ethereum/comments/1rlsfeq/built_a_rust_tool_to_scan_ethereum_smart/)**

I built SCPF (Smart Contract Pattern Finder) - an open-source security scanner for Ethereum smart contracts. What it does: - Scans contracts for reentrancy, delegatecall, unchecked calls, and other vulnerabilities - Uses YAML templates (easy to customize) - Integrates with GitHub Actions (SARIF output) - Supports up to 6 Etherscan API keys with automatic failover Quick example: bash scpf scan 0x1234... --chains ethereum Built with Rust for speed. MIT licensed. GitHub: https://github.com/Teycir/smartcontractpatternfinder Would love feedback from the community! 🚀

1h ago

---

**[DeFi didn't start in 2020: a March 2016 token-swap contract pattern worth revisiting](https://www.reddit.com/r/ethereum/comments/1rljum1/defi_didnt_start_in_2020_a_march_2016_tokenswap/)**

Been doing Ethereum archaeology and found a useful reminder: token-for-token swap behavior existed on-chain in 2016, long before AMMs were mainstream. What was different vs modern DeFi: - no pooled liquidity / routing engines - much heavier coordination + trust assumptions - primitive UX, but clearly permissionless exchange intent It feels like DeFi history is better modeled as a slow primitive stack (2015-2018) rather than a sudden 2020 birth. Question for the OGs here: which pre-2018 contracts do you consider the most important proto-DeFi stepping stones?

6h ago

---

**[Daily General Discussion March 04, 2026](https://www.reddit.com/r/ethereum/comments/1rkdlum/daily_general_discussion_march_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Understanding Block-Level Access Lists, a headliner of the Glamsterdam upgrade](https://www.reddit.com/r/ethereum/comments/1rkpno9/understanding_blocklevel_access_lists_a_headliner/)**

EIP-7928 (Block-Level Access Lists) is the headliner of the upcoming Glamsterdam upgrade, expected to activate mid-year. The EIP website summarizes it as a feature that unlocks “parallel transaction execution on Ethereum”. In this article we’ll see what that means, how the EIP works, and why it’s designed the way it is.

🔗 [Cethology](https://paragraph.com/@cethology/understanding-block-level-access-lists) • 1d ago

---

**[Compliance and taxes for payments on Dapps](https://www.reddit.com/r/ethereum/comments/1rkmh8e/compliance_and_taxes_for_payments_on_dapps/)**

My question is for devs and teams which are running Defi apps, DApps, Web apps with wallet connect feature. How are you doing compliance and taxes for the payments that comes directly though wallet connect feature? User can deposit funds that came from any random source. How do you manage all these anonymous payments coming to you?

1d ago

---

**[I reverse-engineered the source code of GavCoin (2016) and got an exact bytecode match - now trying to get Etherscan to verify it](https://www.reddit.com/r/ethereum/comments/1rk91ha/i_reverseengineered_the_source_code_of_gavcoin/)**

GavCoin (0xb4abc1bfc403a7b82c777420c81269858a4b8aa4) was deployed on April 26, 2016 - one of the earliest token contracts on Ethereum. The original source used #require directives from the Mix IDE preprocessor, which hasn't existed for years. The code was never verified on Etherscan. I spent a while reconstructing the source from bytecode analysis: Brute-forced all 12 function selectors via keccak256 to recover the exact function names (turns out Gav used changeOwner not setOwner, nameRegAddress not name) Discovered the contract has zero events, no inheritance, and a flat storage layout - unusual for something based on dapp-bin's coin.sol Found that function declaration order matters in solc 0.3.x because it controls where the shared return trampoline gets placed in bytecode The constructor registers itself as "GavCoin" in the old global NameReg contract and mints 1,000,000 tokens to the deployer, plus has a proof-of-work mining function anyone could call End result: exact byte-for-byte match of the 905-byte runtime bytecode across solc v0.1.6 through v0.3.2 with optimizer enabled. Source and one-command verification script: https://github.com/cartoonitunes/gavcoin-verify The problem: Etherscan's verification form only supports solc v0.4.11 and newer. GavCoin was compiled with v0.3.1. So I've emailed them requesting manual verification. I also submitted verification requests for two other historic contracts from the same era - Alex Van de Sande's Unicorn Meat system (the MeatConversionCalculator and MeatGrindersAssociation). The Grinder Association is one of the earliest DAOs on Ethereum, featuring quadratic voting and on-chain proposals. Source for those is in avsa's original gist. These early contracts are fascinating. Pre-ERC-20, pre-EIP, people were just experimenting. Proof-of-work token mining, on-chain name registries, quadratic voting DAOs - all in 2016. If anyone has other unverified historic contracts they'd like help with, happy to share the approach.

1d ago

---

---

## Google News: "ethereum"

**[Ethereum news (ETH): Foundation wants the network to be the trust layer for AI](https://www.coindesk.com/tech/2026/03/04/ethereum-foundation-wants-the-network-to-be-the-trust-layer-for-ai)**

Davide Crapis, the foundation's AI lead,  sees the network acting as a coordination and verification layer in an increasingly AI-mediated world.

CoinDesk • 1d ago

---

**[Bitcoin, Ethereum ETFs Snap Five-Week Losing Streak as Crypto Funds Add $1 Billion](https://decrypt.co/359587/bitcoin-ethereum-etfs-snap-losing-streak-crypto-funds-1-billion)**

Bitcoin and other crypto funds rebounded with $1 billion worth of inflows last week, ending a five-week, $4 billion losing streak.

Decrypt • 3d ago

---

**[This Investor Dumped a $3 Million Ethereum ETF, but Added to a Bitcoin Position Last Quarter](https://finance.yahoo.com/news/investor-dumped-3-million-ethereum-181155991.html)**

The iShares Ethereum Trust ETF offers regulated ether exposure via a trust structure, trading on NASDAQ with daily liquidity for investors.

Yahoo Finance • 3h ago

---

**[Bitcoin and Ethereum Price to Surge in March? Tom Lee Bullish On Rebound Despite WW3 Threat](https://finance.yahoo.com/news/bitcoin-ethereum-price-surge-march-104526423.html)**

Tom Lee expects a March rebound despite geopolitical tensions. Other analysts see signs of a bottom. Price outlook remains uncertain. Bitcoin and Ethereum’s prices could ...

Yahoo Finance • 1d ago

---

**[ETH, BMNR news: Short seller Culper Research says ether tokenomics is 'impaired'](https://www.coindesk.com/markets/2026/03/05/short-seller-culper-bets-against-ether-bitmine-citing-death-spiral-risk)**

The short seller firm said that Ethereum's native token is "impaired," leaving treasury firm BitMine holding the bag while co-founder Vitalik buterin is selling.

CoinDesk • 21m ago

---

**[BitMine Stock Soars 8% as Ethereum Price Defies the War Fog & Tom Lee Aggressively Piles into the $9.1 Billion Vault](https://www.tipranks.com/news/bitmine-stock-soars-8-as-ethereum-price-defies-the-war-fog-tom-lee-aggressively-piles-into-the-9-1-billion-vault)**

TipRanks • 14h ago

---

**[Bitcoin, XRP, Ethereum Are Having a Great Week Despite Iran War. Why Cryptos Are on the Up.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-iran-war-cryptos-ba05311d?gaa_at=eafs&gaa_n=AWEtsqc7CvX4VoOd8aFwmVpK6demM670VjrKvESw7fA67Ka2R_cPE3rrDU2H&gaa_ts=69a9faf4&gaa_sig=aABj0qlycdQCWa3zEThXXEoroMaPKiyhkJIEXTI30920GDgzV0SuE1ip5vR2RdaSVL2VJZ20PDOVCPw8ZD8FHw%3D%3D)**

Barron's • 11h ago

---

**[Crypto Market Crash: Top Analyst Reveals What’s Next For Bitcoin, Ethereum and XRP](https://www.tradingview.com/news/coinpedia:0c8387655094b:0-crypto-market-crash-top-analyst-reveals-what-s-next-for-bitcoin-ethereum-and-xrp/)**

The recent volatility in the crypto market has left investors questioning whether the latest pullback means a deeper crash or just a temporary correction. While prices have struggled to maintain momentum, one market strategist believes the current setup could still lead to a short-term rally before…

TradingView • 5h ago

---

**[Better Cryptocurrency to Buy Right Now With $2,000 and Hold for 5 Years: XRP vs. Ethereum](https://www.nasdaq.com/articles/better-cryptocurrency-buy-right-now-2000-and-hold-5-years-xrp-vs-ethereum)**

Key PointsEthereum is a general-purpose smart contract chain.

Nasdaq • 2d ago

---

**[Current price of Ethereum for March 4, 2026](https://fortune.com/article/price-of-ethereum-03-04-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 23h ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee has gone insane (ethereum).](https://www.youtube.com/watch?v=KUl2p8MQGBg)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 11K • 👍 398 • 💬 14 • ⏱️ 1:16 • 8h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=FV9pHXeiaxk)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 127 • 💬 3 • ⏱️ 3:54 • 5h ago

---

**[Is the BMNR Bottom ALREADY IN? When will BMNR reach $51.86?](https://www.youtube.com/watch?v=A05qWHPyuho)**

With all the volatility in the middle-east, crypto prices have been relatively steady. BMNR is preparing to buy more ETH because ...

📺 Elijah Cheng

👁️ 1K • 👍 116 • 💬 18 • ⏱️ 25:01 • 7h ago

---

**[Bitcoin &amp; Ethereum &quot;Buy&quot; 50% Below Record Highs, ETFs Adding Exposure](https://www.youtube.com/watch?v=zr0xNUhtXcY)**

Mike Willis, co-founder and CEO of Cyber Hornet ETFs, says Bitcoin and Ethereum are both buys amid steep sell-offs in the crypto ...

📺 Schwab Network

👁️ 6K • 👍 70 • 💬 11 • ⏱️ 8:40 • 2d ago

---

**[FINALLY REVEALED → Why Crypto Is Going Up Right Now](https://www.youtube.com/watch?v=9U0ctEDMJw8)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 61K • 👍 2K • 💬 125 • ⏱️ 10:14 • 2d ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=i84p4a-itsY)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 3K • 👍 167 • 💬 7 • ⏱️ 4:00 • 21h ago

---

**[BITCOIN BREAKOUT CONFIRMED: Next Target Revealed!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=prGnQUx-jQI)**

BITCOIN BREAKOUT CONFIRMED: Next Target Revealed!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 8K • 👍 360 • 💬 100 • ⏱️ 17:29 • 21h ago

---

**[Sui Founder Explains Why Ethereum &amp; Solana Will Be Left Behind | E161](https://www.youtube.com/watch?v=5Tunu3t7kQ4)**

Evan Cheng co-founded SUI after leading Facebook's Libra project - then threw away everything they built because it wasn't good ...

📺 When Shift Happens

👁️ 3K • 👍 238 • 💬 74 • ⏱️ 49:16 • 6h ago

---

**[BUY ETHEREUM!](https://www.youtube.com/watch?v=LfrCGteIJsE)**

Join Discord Group https://painofcrypto.netlify.app/ X https://twitter.com/PainofCrypt0 Instagram ...

📺 Pain of Crypto

👁️ 4K • 👍 136 • 💬 45 • ⏱️ 6:27 • 2d ago

---

**[Vendo TODO MI ETHEREUM y ALTCOINS antes del GRAN CRASH...?](https://www.youtube.com/watch?v=1hI6IxmQYUM)**

Bitcoin y cripto con buenas subidas tras el conflicto de Irán pero... será para nuevos MINIMOS??? Rodéate de la información ...

📺 Tu Primer Bitcoin

👁️ 2K • 👍 345 • 💬 90 • ⏱️ 17:21 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
