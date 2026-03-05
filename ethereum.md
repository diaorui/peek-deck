---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-05T15:13:14.330657+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- videos
- cryptocurrency
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 05, 2026 at 15:13 UTC  
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

### $2,094.46

---

## Ethereum Chart

**24h:** -2.5%  
**7d:** +8.1%  
**30d:** -2.9%  
**90d:** -31.3%  
**1y:** -5.4%  

---

## Ethereum Market Stats

**Market Cap:** $253.20B
Rank #2

**Circulating Supply:** 120,692,109 ETH
No max supply

**All-Time High:** $4,946.05
-57.8%

**All-Time Low:** $0.43
+482403.8%

---

## Reddit: r/ethereum

**[Daily General Discussion March 05, 2026](https://www.reddit.com/r/ethereum/comments/1rl9qdi/daily_general_discussion_march_05_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

9h ago

---

**[TerraNullius: The Ethereum Message Board from Block 49,880 (August 7, 2015) — Still Getting Claims in 2026](https://www.reddit.com/r/ethereum/comments/1rlidmx/terranullius_the_ethereum_message_board_from/)**

Two weeks after Ethereum's genesis block, a Reddit user named "Semiel" deployed one of the earliest smart contracts on the network: TerraNullius. What it does: Anyone can "claim" a hex coordinate and attach a message to it — a permanent, uncensorable message board on the blockchain. No tokens, no governance, no economic incentive. Just messages, forever. The numbers: - Deployed at block 49,880 (August 7, 2015) - Compiled with Solidity v0.1.1 - 25 claims in 2015, then it sat mostly dormant - 687 claims during the 2021 NFT boom (people realized these were basically proto-NFTs) - 805 total transactions and counting — still active in 2026 It was referenced by the Guinness World Records and is one of the earliest surviving interactive contracts on Ethereum. The original announcement was a Reddit post right here on r/ethereum, with Semiel sharing a Pastebin script so people could interact with it. What's fascinating is how it predates every pattern we now take for granted — ERC-20, ERC-721, ENS, DAOs. This was someone experimenting with permanence on a chain that was two weeks old. Contract: 0x6e38A457C722C6011B2dfa06d49240e797844d66 Full writeup with sources and verification: EthereumHistory.com If anyone has stories about early Ethereum experiments like this, I'd love to hear them. We're trying to document the pre-2017 era before the context is lost entirely.

1h ago

---

**[DeFi didn't start in 2020: a March 2016 token-swap contract pattern worth revisiting](https://www.reddit.com/r/ethereum/comments/1rljum1/defi_didnt_start_in_2020_a_march_2016_tokenswap/)**

Been doing Ethereum archaeology and found a useful reminder: token-for-token swap behavior existed on-chain in 2016, long before AMMs were mainstream. What was different vs modern DeFi: - no pooled liquidity / routing engines - much heavier coordination + trust assumptions - primitive UX, but clearly permissionless exchange intent It feels like DeFi history is better modeled as a slow primitive stack (2015-2018) rather than a sudden 2020 birth. Question for the OGs here: which pre-2018 contracts do you consider the most important proto-DeFi stepping stones?

11m ago

---

**[Daily General Discussion March 04, 2026](https://www.reddit.com/r/ethereum/comments/1rkdlum/daily_general_discussion_march_04_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Understanding Block-Level Access Lists, a headliner of the Glamsterdam upgrade](https://www.reddit.com/r/ethereum/comments/1rkpno9/understanding_blocklevel_access_lists_a_headliner/)**

EIP-7928 (Block-Level Access Lists) is the headliner of the upcoming Glamsterdam upgrade, expected to activate mid-year. The EIP website summarizes it as a feature that unlocks “parallel transaction execution on Ethereum”. In this article we’ll see what that means, how the EIP works, and why it’s designed the way it is.

🔗 [Cethology](https://paragraph.com/@cethology/understanding-block-level-access-lists) • 22h ago

---

**[Compliance and taxes for payments on Dapps](https://www.reddit.com/r/ethereum/comments/1rkmh8e/compliance_and_taxes_for_payments_on_dapps/)**

My question is for devs and teams which are running Defi apps, DApps, Web apps with wallet connect feature. How are you doing compliance and taxes for the payments that comes directly though wallet connect feature? User can deposit funds that came from any random source. How do you manage all these anonymous payments coming to you?

1d ago

---

**[I reverse-engineered the source code of GavCoin (2016) and got an exact bytecode match - now trying to get Etherscan to verify it](https://www.reddit.com/r/ethereum/comments/1rk91ha/i_reverseengineered_the_source_code_of_gavcoin/)**

GavCoin (0xb4abc1bfc403a7b82c777420c81269858a4b8aa4) was deployed on April 26, 2016 - one of the earliest token contracts on Ethereum. The original source used #require directives from the Mix IDE preprocessor, which hasn't existed for years. The code was never verified on Etherscan. I spent a while reconstructing the source from bytecode analysis: Brute-forced all 12 function selectors via keccak256 to recover the exact function names (turns out Gav used changeOwner not setOwner, nameRegAddress not name) Discovered the contract has zero events, no inheritance, and a flat storage layout - unusual for something based on dapp-bin's coin.sol Found that function declaration order matters in solc 0.3.x because it controls where the shared return trampoline gets placed in bytecode The constructor registers itself as "GavCoin" in the old global NameReg contract and mints 1,000,000 tokens to the deployer, plus has a proof-of-work mining function anyone could call End result: exact byte-for-byte match of the 905-byte runtime bytecode across solc v0.1.6 through v0.3.2 with optimizer enabled. Source and one-command verification script: https://github.com/cartoonitunes/gavcoin-verify The problem: Etherscan's verification form only supports solc v0.4.11 and newer. GavCoin was compiled with v0.3.1. So I've emailed them requesting manual verification. I also submitted verification requests for two other historic contracts from the same era - Alex Van de Sande's Unicorn Meat system (the MeatConversionCalculator and MeatGrindersAssociation). The Grinder Association is one of the earliest DAOs on Ethereum, featuring quadratic voting and on-chain proposals. Source for those is in avsa's original gist. These early contracts are fascinating. Pre-ERC-20, pre-EIP, people were just experimenting. Proof-of-work token mining, on-chain name registries, quadratic voting DAOs - all in 2016. If anyone has other unverified historic contracts they'd like help with, happy to share the approach.

1d ago

---

**[Sanctuary technologies](https://www.reddit.com/r/ethereum/comments/1rjyqnx/sanctuary_technologies/)**

Over the past year, many people I talk to have expressed worry about two topics: Various aspects of the way the world is going: government control and surveillance, wars, corporate power and surveillance, tech enshittification / corposlop, social media becoming a memetic warzone, AI and how it interplays with all of the above... The brute reality that Ethereum seems to be absent from meaningfully improving the lives of people subject to these things, even on the dimensions we deeply care about (eg. freedom, privacy, security of digital life, community self-organization) It is easy to bond over the first, to commiserate over the fact that beauty and good in the world seems to be receding and darkness advancing, and uncaring powerful people in high places are making this happen. But ultimately, it is easy to acknowledge problems, the hard thing is actually shining a light forward, coming up with a concrete plan that makes the situation better. The second has been weighing heavily on my mind, and on the minds of many of our brightest and most idealistic Ethereans. I personally never felt any upset or fear when political memecoins went on Solana, or various zero-sum gambling applications go on whatever 250 millisecond block chain strikes their fancy. But it does weigh on me that, through all of the various low-grade online memetic wars, international overreaches of corporate and government power, and other issues of the last few years, Ethereum has been playing a very limited role in making people's lives better. What are the liberating technologies? Starlink is the most obvious one. Locally-running open-weights LLMs are another. Signal is a third. Community Notes is a fourth, tackling the problem from a different angle. One response is to say "stop dreaming big, we need to hunker down and accept that finance is our lane and laser-focus on that". But this is ultimately hollow. Financial freedom and security is critical. But it seems obvious that, while adding a perfectly free and open and sovereign and debasement-proof financial system would fix some things, but it would leave the bulk of our deep worries about the world unaddressed. It's okay for individuals to laser-focus on finance, but we need to be part of some greater whole that has things to say about the other problems too. At the same time, Ethereum cannot fix the world. Ethereum is the "wrong-shaped tool" for that: beyond a certain point, "fixing the world" implies a form of power projection that is more like a centralized political entity than like a decentralized technology community. So what can we do? I think that we in Ethereum should conceptualize ourselves as being part of an ecosystem building "sanctuary technologies": free open-source technologies that let people live, work, talk to each other, manage risk and build wealth, and collaborate on shared goals, in a way that optimizes for robustness to outside pressures. The goal is not to remake the world in Ethereum's image, where all finance is disintermediated, all governance happens through DAOs, and everyone gets a blockchain-based UBI delivered straight to their social-recovery wallet. The goal is the opposite: it's de-totalization. It's to reduce the stakes of the war in heaven by preventing the winner from having total victory (ie. total control over other human beings), and preventing the loser from suffering total defeat. To create digital islands of stability in a chaotic era. To enable interdependence that cannot be weaponized. Ethereum's role is to create "digital space" where different entities can cooperate and interact. Communications channels enable interaction, but communication channels are not "space": they do not let you create single unique objects that canonically represent some social arrangement that changes over time. Money is one important example. Multisigs that can change their members, showing persistence exceeding that of any one person or one public key, are another. Various market and governance structures are a third. There are more. I think now is the time to double down, with greater clarity. Do not try to be Apple or Google, seeing crypto as a tech sector that enables efficiency or shininess. Instead, build our part of the sanctuary tech ecosystem - the "shared digital space with no owner" that enables both open finance and much more. More actively build toward a full-stack ecosystem: both upward to the wallet and application layer (incl AI as interface) and downward to the OS, hardware, even physical/bio security levels. Ultimately, tech is worthless without users. But look for users, both individual and institutional, for whom sanctuary tech is exactly the thing they need. Optimize payments, defi, decentralized social, and other applications precisely for those users, and those goals, which centralized tech will not serve. We have many allies, including many outside of "crypto". It's time we work together with an open mind and move forward.

1d ago

---

**[I know we all hate the dystopian eyeball scanners, but the ZK-ML tech that was just open-sourced is actually a massive win for Ethereum privacy.](https://www.reddit.com/r/ethereum/comments/1rk0jty/i_know_we_all_hate_the_dystopian_eyeball_scanners/)**

Let’s address the elephant in the room first. This community (and Vitalik himself) has rightfully dragged the entire Proof-of-Personhood concept for the massive centralization risks of proprietary hardware and the general "ick" factor of biometric data collection. I have been one of the biggest skeptics of the whole "scan your iris for tokens" model since day one. But setting the tokenomics and the physical hardware aside for a minute, the engineering team behind world just dropped an open-source cryptographic update that is honestly a massive leap forward for Zero-Knowledge Machine Learning (ZK-ML) on Ethereum. They just open-sourced "Remainder", a highly efficient in-house ZK prover built on the GKR protocol combined with a Hyrax polynomial commitment scheme. Why should we care about this? Historically, one of the biggest architectural flaws in biometric identity was the upgrade path. If the recognition algorithm improves, how do you upgrade the user's cryptographic credentials without forcing them to go back to a physical, centralized hardware device to get scanned again? Remainder solves this entirely on the client side. It is specifically optimized to run heavy ML computations directly on standard mobile hardware. This means when the underlying algorithms update, your phone runs the new ML model locally over your securely custodied data, and simply generates a Zero-Knowledge proof that the execution was correct. The raw biometric data never leaves your device. The network just verifies the proof. We talk constantly in this sub about building trustless identity primitives and scaling privacy on-chain. Using GKR to achieve linear-time proving on consumer edge devices - so users no longer have to rely on a centralized server for biometric processing - is exactly the kind of cypherpunk engineering we should be encouraging. I’m genuinely curious to hear from the ZK nerds and privacy maxis here: Does shifting the heavy lifting to local, client-side ZK proofs and open-sourcing the prover code soften your stance on this protocol at all? Or is the reliance on that initial hardware scan still an unforgivable "original sin" for decentralized identity?

1d ago

---

**[Daily General Discussion March 03, 2026](https://www.reddit.com/r/ethereum/comments/1rjhj9n/daily_general_discussion_march_03_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

---

## Google News: "ethereum"

**[Ethereum news (ETH): Foundation wants the network to be the trust layer for AI](https://www.coindesk.com/tech/2026/03/04/ethereum-foundation-wants-the-network-to-be-the-trust-layer-for-ai)**

Davide Crapis, the foundation's AI lead,  sees the network acting as a coordination and verification layer in an increasingly AI-mediated world.

CoinDesk • 21h ago

---

**[Vitalik Buterin Urges Ethereum to Broaden Its Mission Beyond Finance](https://decrypt.co/359895/vitalik-buterin-ethereum-broaden-mission-beyond-finance)**

Ethereum’s co-founder is calling for “sanctuary technologies” spanning privacy tools, social systems, and infrastructure beyond finance.

Decrypt • 3d ago

---

**[Ethereum ETFs Draw In $169M, Highest Level in Two Months](https://finance.yahoo.com/news/ethereum-etfs-draw-169m-highest-124435429.html)**

Ethereum ETFs saw inflows of $169 million Wednesday, as geopolitical tensions and price reset institutions’ crypto appetite.

Yahoo Finance • 2h ago

---

**[Current price of Ethereum for March 4, 2026](https://fortune.com/article/price-of-ethereum-03-04-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 16h ago

---

**[Got $1,000? This Cryptocurrency Is a No-Brainer Buy for Long-Term Holding](https://www.fool.com/investing/2026/03/05/got-1000-this-cryptocurrency-is-a-no-brainer-buy-f/)**

The cryptocurrency's status as the leader in decentralized finance makes it hard to beat.

The Motley Fool • 6h ago

---

**[Bitcoin Price Surges Above $72,000. Ethereum, XRP, Cryptos Defy Iran Risks.](https://www.barrons.com/articles/bitcoin-price-ethereum-xrp-crypto-iran-b5f1f518?gaa_at=eafs&gaa_n=AWEtsqdKzLNPySJt8MU-QU588xfEZNb5VAjkQhfPjyQmjIO9hjS4NyIJ3Wb1&gaa_ts=69a9a07d&gaa_sig=gZbcDEkIre2ifBX5YAPlb_7Ih6YbXCXlPpOFcQ0pWtU7j9jm-GBKRxbp036dbMGZRCpFKnrIFMVKjeRxp35lxQ%3D%3D)**

Barron's • 22h ago

---

**[Ethereum Price, BitMine Shares Jump as Tom Lee's Treasury Reports Latest Buy](https://finance.yahoo.com/news/ethereum-price-bitmine-shares-jump-153447384.html)**

Publicly traded Ethereum treasury BitMine Immersion Technologies added to its ETH stack last week despite its recent decline.

Yahoo Finance • 2d ago

---

**[BitMine Stock Soars 8% as Ethereum Price Defies the War Fog & Tom Lee Aggressively Piles into the $9.1 Billion Vault](https://www.tipranks.com/news/bitmine-stock-soars-8-as-ethereum-price-defies-the-war-fog-tom-lee-aggressively-piles-into-the-9-1-billion-vault)**

TipRanks • 7h ago

---

**[Bitcoin miner turned Ethereum treasury firm stakes over $6B in ETH as BMNR shares slide and ether dips.](https://www.coindesk.com/business/2026/03/02/bitmine-boosts-ether-holdings-to-4-47m-tokens-after-usd98m-eth-purchase)**

Bitmine chair Tom Lee says company keeps accumulating ETH during market pullback while targeting $253M in annual staking rewards.

CoinDesk • 2d ago

---

**[Key facts: Harvard buys $86.8M in Ethereum shares; U.S. ether ETFs see volatility](https://www.tradingview.com/news/tradingview:331ab23c2055e:0-key-facts-harvard-buys-86-8m-in-ethereum-shares-u-s-ether-etfs-see-volatility/)**

TradingView • 15h ago

---

---

## YouTube Videos: "ethereum"

**[Tom Lee has gone insane (ethereum).](https://www.youtube.com/watch?v=KUl2p8MQGBg)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 4K • 👍 206 • 💬 2 • ⏱️ 1:16 • 2h ago

---

**[Bitcoin &amp; Ethereum &quot;Buy&quot; 50% Below Record Highs, ETFs Adding Exposure](https://www.youtube.com/watch?v=zr0xNUhtXcY)**

Mike Willis, co-founder and CEO of Cyber Hornet ETFs, says Bitcoin and Ethereum are both buys amid steep sell-offs in the crypto ...

📺 Schwab Network

👁️ 5K • 👍 65 • 💬 11 • ⏱️ 8:40 • 1d ago

---

**[BITCOIN BREAKOUT CONFIRMED: Next Target Revealed!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=prGnQUx-jQI)**

BITCOIN BREAKOUT CONFIRMED: Next Target Revealed!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 8K • 👍 342 • 💬 81 • ⏱️ 17:29 • 15h ago

---

**[FINALLY REVEALED → Why Crypto Is Going Up Right Now](https://www.youtube.com/watch?v=9U0ctEDMJw8)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 61K • 👍 2K • 💬 124 • ⏱️ 10:14 • 2d ago

---

**[When THIS happens to ETHEREUM, BMNR will reach $51.86!](https://www.youtube.com/watch?v=A05qWHPyuho)**

With all the volatility in the middle-east, crypto prices have been relatively steady. BMNR is preparing to buy more ETH because ...

📺 Elijah Cheng

👁️ 174 • 👍 19 • 💬 2 • ⏱️ 25:01 • 43m ago

---

**[Crypto Live Trading 5 March ||  @MrStarSahil   #bitcoin #ethereum #cryptotrading](https://www.youtube.com/watch?v=lLHugllZtCo)**

ALL TRADING PLATFORMS (CRYPTO/ Gold Token) :- https://india.delta.exchange/?code=JFWJTR Google Form For EMA ...

📺 Vibe With Sahil

👁️ 5K • 👍 463 • 1h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=i84p4a-itsY)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 164 • 💬 7 • ⏱️ 4:00 • 14h ago

---

**[Set Alerts On Ethereum NOW! Bottom Coming Soon?](https://www.youtube.com/watch?v=sl_KQkhjOY4)**

Get $450 Off Our New AI Indicators: https://tradeconfidentportal.io/indicators Join Trade Confident: Get 25% Off Your 1st Month: ...

📺 Trade Confident

👁️ 962 • 👍 24 • 💬 6 • ⏱️ 5:09 • 2d ago

---

**[ETH BREAKOUT OR FAKEOUT?🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=c-sjutJm_no)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 174 • 👍 12 • 💬 2 • ⏱️ 5:41 • 5h ago

---

**[BUY ETHEREUM!](https://www.youtube.com/watch?v=LfrCGteIJsE)**

Join Discord Group https://painofcrypto.netlify.app/ X https://twitter.com/PainofCrypt0 Instagram ...

📺 Pain of Crypto

👁️ 4K • 👍 135 • 💬 44 • ⏱️ 6:27 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
