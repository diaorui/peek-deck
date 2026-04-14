---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-14T15:20:22.435176+00:00'
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

**Last Updated:** April 14, 2026 at 15:20 UTC  
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

### $2,339.41

---

## Ethereum Chart

**24h:** +5.2%  
**7d:** +7.0%  
**30d:** -0.4%  
**90d:** -29.4%  
**1y:** +47.5%  

---

## Ethereum Market Stats

**Market Cap:** $288.58B
Rank #2

**Circulating Supply:** 120,690,992 ETH
No max supply

**All-Time High:** $4,946.05
-51.7%

**All-Time Low:** $0.43
+552210.9%

---

## Reddit: r/ethereum

**[Daily General Discussion April 14, 2026](https://www.reddit.com/r/ethereum/comments/1skz0ll/daily_general_discussion_april_14_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

10h ago

---

**[Coinbase AgentKit Prompt Injection: Wallet Drain, Infinite Approvals, and Agent-Level RCE (validated by Coinbase, on-chain PoC)](https://www.reddit.com/r/ethereum/comments/1skozp6/coinbase_agentkit_prompt_injection_wallet_drain/)**

Coinbase AgentKit Prompt Injection: Wallet Drain, Infinite Approvals, and Agent-Level RCE Reported 13 days after Coinbase launched Agentic Wallets. Validated by Coinbase. Demonstrated on-chain. Published: April 11, 2026 CVE status: Pending assignment
Coinbase AgentKit is developer infrastructure for building AI agents with direct access to wallets, token operations, DeFi actions, and related execution surfaces. This disclosure covers a prompt injection vulnerability in AgentKit that allowed attacker-controlled input to trigger sensitive tool execution without a built-in human confirmation step.

🔗 [x402warden](https://x402warden.com/research/coinbase-agentkit-prompt-injection/) • 17h ago

---

**[Daily General Discussion April 13, 2026](https://www.reddit.com/r/ethereum/comments/1sk173h/daily_general_discussion_april_13_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Deploy a full DEX on Ethereum, Arbitrum, or Base in one command.](https://www.reddit.com/r/ethereum/comments/1sjuq3y/deploy_a_full_dex_on_ethereum_arbitrum_or_base_in/)**

I built a CLI tool in rust called LaunchDex that deploys a full DEX--factory contract, router, liquidity pair and swap frontend--on Ethereum, Arbitrum, and Base in a single command. The whole process that typically takes weeks of manual contract deployment, configuration and frontend setup is reduced to launchdex deploy. Contract addresses are saved automatically and a custom swap interface is generated and ready to deploy. The tool is built on top of verified Uniswap v2 contracts so the deployed DEX is production-grade and audited. Multi-token support lets you add additional trading pairs to an existing factory with one command. The generated frontend includes an embedded wallet so user can swap tokens without needing Metamask installed. Let me know what you think

1d ago

---

**[WARNING: Aerodrome's CLGauge have an Integration Trap - Lost $2k due to incomplete ERC-721 implementation](https://www.reddit.com/r/ethereum/comments/1sjjq2i/warning_aerodromes_clgauge_have_an_integration/)**

I permanently lost $2,000 USD value trying to stake via direct contract interaction on Aerodrome. The CLGauge contract accepts safeTransferFrom via the onERC721Received hook but silently fails to update the staking state, creating a black hole for assets. I’m sharing this to warn other developers and integrators building on top of Aerodrome (Base chain), and hopefully get the attention of the Core Team or the Emergency Council, since standard Discord support just gave me the "contracts are immutable" playbook. Recently, I performed a safeTransferFrom (as a fallback to approve and deposit) directly to the Aerodrome Gauge (0x83e2E9493996651ed63033d81f5052cBE2fEB6A1). The transaction was mathematically and technically successful on-chain because the Gauge contract explicitly implements the IERC721Receiver interface. However, this is where the integration trap lies: While the contract gladly accepted physical custody of my NFT position, it completely failed to trigger the internal logic to update the _stakes mapping and the rewardGrowth snapshots. The Reality: By exposing the receiver hook without the corresponding push-based deposit logic, Aerodrome's contract signals false compatibility. It creates a critical state mismatch: the Gauge owns the NFT, but my wallet is no longer recognized as the owner, meaning I can neither call deposit() nor withdraw(). Has any other developer encountered this problem?

1d ago

---

**[World Liberty Financial borrowed its own stablecoin against its own token on a platform run by its own advisor and Justin Sun (WLFI biggest investor) just called it fraud.](https://www.reddit.com/r/ethereum/comments/1sjkjuc/world_liberty_financial_borrowed_its_own/)**

1d ago

---

**[What actually happens under the hood when calldata hits the EVM (Execution Flow Breakdown)](https://www.reddit.com/r/ethereum/comments/1sjqdwd/what_actually_happens_under_the_hood_when/)**

There’s a lot of focus lately on calldata in the context of rollups and EIP-2028 gas economics (16 vs 4 gas per byte). While data availability is important, I often see the actual low-level execution mechanics get glossed over. I wrote a deep dive on EVM internals covering this exact topic. If you've ever wondered what happens at the opcode level the millisecond your transaction payload hits a smart contract, here is the actual lifecycle of calldata: The Raw Byte Handoff & The 4-Byte Check When a transaction is sent, the EVM doesn't understand "functions" or "parameters", it just sees a raw hex-encoded blob in a read-only area called calldata. Before anything else, the EVM checks the length of this data: The Function Dispatcher (The EVM's Switchboard) If there is data, the EVM runs the dispatcher essentially a giant, compiler-generated switch/case statement: If it finds a match, it uses JUMPI to move the Program Counter to that specific block of code. ABI Decoding & Stack Loading Once the EVM jumps to the right function, it has to "unpack" the arguments: Dynamic Types (string, bytes[]): The calldata contains an offset (a pointer). The EVM reads this offset, jumps to that position in the calldata, reads the length prefix, and then processes the actual data. The payable Word Before executing any actual business logic, the EVM checks the callvalue (msg.value). If the target function is not explicitly marked as payable, but the transaction includes ETH, the EVM triggers a REVERT right here. This prevents trapped funds and happens before your code even starts running. memory vs. calldata Execution This is where the famous gas savings come in during execution: If a function parameter is declared as memory, the EVM is forced to use CALLDATACOPY to move the read-only bytes into mutable memory. This triggers memory expansion gas costs. If declared as calldata, the EVM skips the copy process entirely. It just uses CALLDATALOAD to read directly from the original transaction payload, saving you the memory expansion overhead. source/deep dive overview: https://andreyobruchkov1996.substack.com/p/what-actually-happens-when-calldata

1d ago

---

**[Daily General Discussion April 12, 2026](https://www.reddit.com/r/ethereum/comments/1sj56x3/daily_general_discussion_april_12_2026/)**

**Welcome to the Daily General Discussion on** r/ethereum [https://imgur.com/3y7vezP\](https://imgur.com/3y7vezP) Bookmarking this link will always bring you to the current daily: [https://old.reddit.com/r/ethereum/about/sticky/?num=2\](https://old.reddit.com/r/ethereum/about/sticky/?num=2) Please use this thread to discuss Ethereum topics, news, events, and even *price*! Price discussion posted elsewhere in the subreddit will **continue to be removed.** As always, be constructive. - [Subreddit Rules](https://www.reddit.com/r/ethereum/about/rules/) Want to stake? Learn more at r/ethstaker **Community Links** * [Ethereum Jobs](https://ethereum.org/en/community/get-involved/#ethereum-jobs), [Twitter](https://x.com/ethereum) * [EVMavericks YouTube](https://www.youtube.com/@evmavericks), [Discord](https://discord.gg/evmavericks), [Doots Podcast](https://evmavericks.libsyn.com/) * [Doots Website](https://dailydoots.com/), Old Reddit [Doots Extension](https://github.com/etheralpha/ethfinance-extension) by u/hanniabu Calendar: [https://dailydoots.com/events/\](https://dailydoots.com/events/)

2d ago

---

**[Is the "Crypto Purge" at Twitter simply an algorithm glitch—or a massive Conflict of Interest?](https://www.reddit.com/r/ethereum/comments/1sjf56t/is_the_crypto_purge_at_twitter_simply_an/)**

2d ago

---

**[My journey trying to build something useful](https://www.reddit.com/r/ethereum/comments/1sij1vy/my_journey_trying_to_build_something_useful/)**

Over the past year I've been thinking a lot about Web3. Not the trading, not the speculation, not the casino. I don't trade crypto. I don't follow the markets. What fascinates me is the underlying idea: decentralized systems with code as the only authority. The technology itself. I've been a backend engineer for over a decade. Rails, SQL, the usual stack. But like many engineers, I burned out. The excitement to build faded. You know the feeling. You're competent, productive, but not discovering anything anymore. Then I looked seriously at blockchain. Not as an investor, but as an engineer. I asked myself: what would an application look like if built with absolute fidelity to what blockchain promises? Real utility (useful for the masses, not DeFi nonesense) NO off-chain layers (100% on-chain) NO insider advantages (fair economics) NO dependence on investors (self-sustaining) NO pointless tokenomics (ETH in, ETH out) Those five principles became my compass. I tried to build something that never violated them. But the Web3 ecosystem is built around tokenomics and speculation. There's no blueprint to follow. So I started pulling my own thread: I wanted to build something useful, deterministic, fully on-chain, with no complicated tokenomics. A simple game like TicTacToe with real ETH stakes? Interesting, but too narrow. Then the frame shifted. I wasn't building a game anymore. I was building a tournament layer. A universal competitive infrastructure that's fair, open-source, and 100% on-chain. That's when the hard problems started. How do you handle draws on a decentralized platform? How do you stop players griefing opponents without central authority? These aren't just technical questions. They're moral ones. They forced me to think deeply about fairness, about building a system nobody controls and nobody can manipulate. The answers surprised me. Forget Kubernetes, Redis, all that complexity. With these constraints (fully on-chain, truly open, completely decentralized) the legacy stack collapses into something elegant. A client talking directly to contracts. No servers. No databases. No company. Just code. That freedom changed how I think about software. So I built ETour A 100% on-chain tournament protocol, now live on Arbitrum. Players pay an entry fee, compete, the best player wins and takes the pot. Code decides everything. No intermediaries. As Web3 should be. I open-sourced it so developers can build their own games on it and inherit all of its features for free. I'm not here to tell you this is revolutionary. I built this because it felt like a problem worth solving. ETour is what came out the other side. The code is public. The contracts are immutable. The logic is yours to verify. PS: The technical docs are not final and will be updated soon. https://etour.games https://etour.games/whitepaper https://etour.games/manual https://etour.games/docs TLDR: ETour is useful, it's live, and it's open-source. Go ahead and play on it, or build your own game using its 100% on-chain and open source tournament modules.

3d ago

---

---

## Google News: "ethereum"

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 4.875 Million Tokens, and Total Crypto and Total Cash Holdings of $11.8 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-4-875-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-8-billion-302740122.html)**

Bitmine now owns more than 4% of the total ETH coin supply of 120.7 million Bitmine is 81% of the way to the 'Alchemy of 5%' in just 9 months Bitmine uplisted...

PR Newswire • 1d ago

---

**[Bitmine holds 4% of ethereum supply as total holdings reach $11.8 billion](https://www.theblock.co/post/397229/bitmine-holds-4-of-ethereum-supply-as-total-holdings-reach-11-8-billion)**

Bitmine expanded its Ethereum treasury to 4.87 million ETH, controlling 4% of supply as total holdings climb to $11.8 billion.

The Block • 1d ago

---

**[Bitmine Hits 4% of Ethereum Supply — Will ‘Alchemy of 5%’ Aid Tom Lee’s Bullish Price Call?](https://www.ccn.com/news/crypto/bitmine-4-ethereum-supply-alchemy-5-tom-lees-bullish-price-call/)**

CCN.com • 6h ago

---

**[Crypto Hacker Mints $1.1 Billion in Polkadot via Ethereum Bridge, But Can Only Cash Out $237K](https://decrypt.co/364131/crypto-hacker-mints-billion-polkadot-ethereum-bridge-cashes-out-237k)**

A hacker exploited a Polkadot bridge, minting $1.1 billion worth of DOT tokens before making a tiny fraction of that tally by selling it.

Decrypt • 23h ago

---

**[Bitcoin, XRP, Ethereum Fall. Iran Peace Failure Causes a Crypto Headache.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-iran-crypto-46d858c6)**

Barron's • 1d ago

---

**[Marc Andreesen Just Said That Artificial General Intelligence (AGI) Is Here. Here's What That Could Mean for Ethereum.](https://www.fool.com/investing/2026/04/14/marc-andreesen-just-said-that-artificial-general-i/)**

If Andreesen is right, Ethereum could be in for a wild ride pretty soon.

The Motley Fool • 48m ago

---

**[CoinDesk 20 performance update: Ethereum (ETH) price rises 5.4%](https://www.coindesk.com/coindesk-indices/2026/04/14/coindesk-20-performance-update-ethereum-eth-price-rises-5-4)**

Aave (AAVE), up 3.6% from Monday, joined Ethereum as a top performer.

CoinDesk • 2h ago

---

**[Current price of Ethereum for April 14, 2026](https://fortune.com/article/price-of-ethereum-04-14-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 2h ago

---

**[Ethereum leads way as large cryptocurrencies post gains](https://www.marketwatch.com/data-news/ethereum-leads-way-as-large-cryptocurrencies-post-gains-f608b9dd-f4607b97363e)**

MarketWatch • 1h ago

---

**[A Historic Ethereum Signal Just Fired – Discover What Happens Next](https://www.tradingview.com/news/newsbtc:c70dbd912094b:0-a-historic-ethereum-signal-just-fired-discover-what-happens-next/)**

Ethereum has been consolidating below $2,200 for weeks. The selling pressure is real. The uncertainty is higher. And the participants who hold enough ETH to move markets just crossed back into profit, which, in the history of this asset, has never happened quietly.A CryptoQuant analyst tracking the…

TradingView — Track All Markets • 16h ago

---

---

## YouTube Videos: "ethereum"

**[🔴 Ethereum Is Finally Breaking Out – Next Target $3,000?](https://www.youtube.com/watch?v=EzqGrq9CQOo)**

BloFin - No KYC/No VPN needed [Trade ETH Coin Futures!] https://marzell.org/Blofin_Trade CoinGPT ...

📺 Marzell Crypto

👁️ 318 • 👍 23 • 💬 117 • ⏱️ 5:01 • 10h ago

---

**[ETHEREUM BROKE OUT! What&#39;s Next?🔥 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=h2K-uk9JfSg)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 261 • 👍 22 • 💬 17 • ⏱️ 4:45 • 6h ago

---

**[🚨 BTC &amp; ETH: OH MY..........](https://www.youtube.com/watch?v=1IfF4Y2CSPU)**

Here is the latest on bitcoin, ethereum and crypto in general! Be aware of whats going on! ---------- EXCHANGE BONUSES ...

📺 Thomas Kralow

👁️ 16K • 👍 2K • 💬 27 • ⏱️ 10:18 • 1d ago

---

**[Bitcoin &amp; Ethereum Whales Are Buying Like It’s a Bull Market… The Signal Is Clear](https://www.youtube.com/watch?v=lX6XC7LPRYs)**

Check prices, drink coffee, read Milk Road. It's the easiest 5-minute habit to stay smart on crypto: ...

📺 Milk Road

👁️ 5K • 👍 181 • 💬 92 • ⏱️ 38:50 • 20h ago

---

**[Ethereum Bounce Looks Weak - Here&#39;s What the Structure Says](https://www.youtube.com/watch?v=uk1iW8koJTE)**

Ethereum is down more than 50% from its all-time high, but the bigger concern right now is not just the decline — it's the structure ...

📺 More Crypto Online

👁️ 4K • 👍 227 • 💬 28 • ⏱️ 15:54 • 18h ago

---

**[Ethereum Supply Shock + BlackRock Staking = Massive Setup](https://www.youtube.com/watch?v=MhOmj6JSAgs)**

Check prices, drink coffee, read Milk Road. It's the easiest 5-minute habit to stay smart on crypto: ...

📺 Milk Road

👁️ 5K • 👍 169 • 💬 25 • ⏱️ 10:57 • 2d ago

---

**[Raoul Pal: &quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” | 2026 Crypto Prediction](https://www.youtube.com/watch?v=Gys5vX-3hfg)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 30K • 👍 798 • 💬 104 • ⏱️ 19:27 • 2d ago

---

**[BITCOIN: Everyone is WRONG About This (important)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=uZnjzuPNTng)**

BITCOIN: Everyone is WRONG About This (important)!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 8K • 👍 326 • 💬 148 • ⏱️ 19:32 • 18h ago

---

**[🚀 ETHEREUM (ETH) HOJE 14/04 - ETH RUMO À PROJEÇÃO DO PADRÃO OCOI NO DIÁRIO! #eth #lobocripto](https://www.youtube.com/watch?v=U3Fy7jhIRvE)**

Registre sua conta na MEXC aqui - https://www.mexc.com/pt-PT/auth/signup?inviteCode=1oVJR ✔️ Seja Membro Apoiador do ...

📺 Lobo Cripto Oficial

👁️ 211 • 👍 52 • 💬 13 • ⏱️ 9:41 • 4h ago

---

**[Ethereum Launches War-Proof Browser To Kill Chrome?🌐Freedom Browser INTERVIEW](https://www.youtube.com/watch?v=MkVhdstQvmE)**

Freedom is a minimalist browser for Swarm and IPFS. No centralized gateways. You connect directly to peers and become part of ...

📺 Paul Barron Network

👁️ 49K • 👍 2K • 💬 180 • ⏱️ 18:02 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
