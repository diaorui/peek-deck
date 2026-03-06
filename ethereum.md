---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-06T21:31:00.232429+00:00'
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

**Last Updated:** March 06, 2026 at 21:31 UTC  
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

### $1,988.35

---

## Ethereum Chart

**24h:** -5.3%  
**7d:** +0.3%  
**30d:** +7.9%  
**90d:** -35.6%  
**1y:** -7.9%  

---

## Ethereum Market Stats

**Market Cap:** $238.18B
Rank #2

**Circulating Supply:** 120,692,086 ETH
No max supply

**All-Time High:** $4,946.05
-60.1%

**All-Time Low:** $0.43
+455947.5%

---

## Reddit: r/ethereum

**[We verified Vitalik's 2015 token contract and discovered it wasn't compiled with Solidity - it's Serpent](https://www.reddit.com/r/ethereum/comments/1rmheom/we_verified_vitaliks_2015_token_contract_and/)**

I've been working on verifying source code for the oldest contracts on Ethereum, and this one took days to crack. The contract: 0xa2e3680acaf5d2298697bdc016cf75a929385463 Deployed by Vitalik on November 12, 2015 (block 530,996). It's a token contract implementing the standardized currency API from the early ethereum/dapp-bin repo. 1,000,000 initial supply, approve/transfer mechanics - basically a proto-ERC-20. The problem: We tried compiling currency.sol with every Solidity compiler version from that era. Every archived soljson release from v0.1.1 through v0.3.6, nightlies from Sep-Dec 2015, native C++ solc builds from the webthree-umbrella repo, optimizer on and off. Nothing matched. The breakthrough: Three clues pointed us away from Solidity entirely: The on-chain constructor starts with 6000603f53 (MSTORE8-based memory init). Every Solidity version produces 60606040525b (the free memory pointer pattern). This is a fundamentally different code generation approach. The runtime code uses MSIZE, SWAP1, MSIZE, ADD for memory allocation. This is the Serpent compiler's alloc() pattern - not found in any version of solc. Two function selectors didn't match the Solidity source: disapprove() instead of unapprove(), and isApprovedOnceFor() instead of isApprovedOnce(). The answer: The contract was compiled from currency.se (the Serpent version), not currency.sol. The ethereum/dapp-bin repo had both implementations side by side. Vitalik deployed his own language's version. Compiled with the Serpent compiler at commit f0b4128 (Oct 15, 2015) - byte-for-byte identical, all 1,661 bytes. Full methodology, source, and proof: github.com/cartoonitunes/vitalik-currency-verification We've submitted a manual verification request to Etherscan since they don't support Serpent as a verification language. Hopefully they can add it as a verified contract with source. This is part of a broader effort to verify and preserve the earliest contracts on Ethereum. A lot of historically important contracts from 2015-2016 are still unverified because the compiler versions are too old for Etherscan's automated tools.

5h ago

---

**[Daily General Discussion March 06, 2026](https://www.reddit.com/r/ethereum/comments/1rm5yqw/daily_general_discussion_march_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

15h ago

---

**[Minimmit vs Casper FFG](https://www.reddit.com/r/ethereum/comments/1rmmoln/minimmit_vs_casper_ffg/)**

One important technical item that I forgot to mention is the proposed switch from Casper FFG to Minimmit as the finality gadget. To summarize, Casper FFG provides two-round finality: it requires each attester to sign once to "justify" the block, and then again to "finalize" it. Minimmit only requires one round. In exchange, Minimmit's fault tolerance (in our parametrization) drops to 17%, compared to Casper FFG's 33%. Within Ethereum consensus discussions, I have always been the security assumptions hawk: I've insisted on getting to the theoretical bound of 49% fault tolerance under synchrony, kept pushing for 51% attack recovery gadgets, came up with DAS to make data availability checks dishonest-majority-resistant, etc. But I am fine with Minimmit's properties, in fact even enthusiastic in some respects. In this post, I will explain why. Let's lay out the exact security properties of both 3SF (not the current beacon chain, which is needlessly weak in many ways, but the ideal 3SF) and Minimmit. "Synchronous network" means "network latency less than 1/4 slot or so", "asynchronous network" means "potentially very high latency, even some nodes go offline for hours at a time". The percentages ("attacker has <33%") refer to percentages of active staked ETH. Properties of 3SF Synchronous network case: Attacker has p < 33%: nothing bad happens 33% < p < 50%: attacker can stop finality (at the cost of losing massive funds via inactivity leak), but the chain keeps progressing normally 50% < p < 67%: attacker can censor or revert the chain, but cannot revert finality. If an attacker censors, good guys can self-organize, they can stop contributing to a censoring chain, and do a "minority soft fork" p > 67%: attacker can finalize things at will, much harder for good guys to do minority soft fork Asynchronous network case: Attacker has p < 33%: cannot revert finality p > 33%: can revert finality, at the cost of losing massive funds via slashing Properties of Minimmit Synchronous network case: Attacker has p < 17%: nothing bad happens 17% < p < 50%: attacker can stop finality (at the cost of losing massive funds via inactivity leak), but the chain keeps progressing normally 50% < p < 83%: attacker can censor or revert the chain, but cannot revert finality. If an attacker censors, good guys can self-organize, they can stop contributing to a censoring chain, and do a "minority soft fork" p > 83%: attacker can finalize things at will, much harder for good guys to do minority soft fork Asynchronous network case: Attacker has p < 17%: cannot revert finality p > 17%: can revert finality, at the cost of losing massive funds via slashing I actually think that the latter is a better tradeoff. Here's my reasoning why: The worst kind of attack is actually not finality reversion, it's censorship. The reason is that finality reversion creates massive publicly available evidence that can be used to immediately cost the attacker millions of ETH (ie. billions of dollars), whereas censorship requires social coordination to get around In both of the above, a censorship attack requires 50% A censorship attack becomes much harder to coordinate around when the censoring attacker can unilaterally finalize (ie. >67% in 3SF, >83% in Minimmit). If they can't, then if the good guys counter-coordinate, you get two non-finalizing chains dueling for a few days, and users can pick on. If they can, then there's no natural schelling point to coordinate soft-forking In the case of a client bug, the worst thing that can happen is finalizing something bugged. In 3SF, you only need 67% of clients to share a bug for it to finalize, in Minimmit, you need 83%. Basicallly, Minimmit maximizes the set of situations that "default to two chains dueling each other", and that is actually a much healthier and much more recoverable outcome than "the wrong thing finalizing". We want finality to mean final. So in situations of uncertainty (whether attacks or software bugs), we should be more okay with having periods of hours or days where the chain does not finalize, and instead progresses based on the fork choice rule. This gives us time to think and make sure which chain is correct. Also, I think the "33% slashed to revert finality" of 3SF is overkill. If there is even eg. 15 million ETH staking, then that's 5M ($10B) slashed to revert the chain once. If you had $10B, and you are willing to commit mayhem of a type that violates many countries' computer hacking laws, there are FAR BETTER ways to spend it than to attack a chain. Even if your goal is breaking Ethereum, there are far better attack vectors. And so if we have the baseline guarantee of >= 17% slashed to revert finality (which Minimmit provides), we should judge the two systems from there based on their other properties - where, for the reasons I described above, I think Minimmit performs better.

2h ago

---

**[ZK VMs made verifiable computation accessible to any developer. The prover networks running them require your full plaintext data. YIKES](https://www.reddit.com/r/ethereum/comments/1rmg9sa/zk_vms_made_verifiable_computation_accessible_to/)**

Zero-knowledge cryptography went through three phases. First: hand-crafted arithmetic circuits, only accessible to deep researchers. Second: ZK virtual machines — suddenly any developer could write verifiable code in Rust or C. Third: prover networks (Succinct, Boundless/RiscZero) that let you delegate the heavy proof generation to external infrastructure. Each phase made the technology more accessible. Each phase also moved the user's data further from their control. Prover networks require your full plaintext data to generate proofs. For rollups, this is a non-issue — public ledger, no privacy expectation, and what you gain (succinctness — compressing thousands of transactions into a single proof) is worth the trade. That's the use case these networks were built for, and they served it well. The problem emerges when you extend this model to user-facing applications. Verifiable identity: proving you hold a valid passport, proving you're over 18, without disclosing the underlying data. Private AI inference: running a model on your data without the model owner seeing your inputs or you seeing their weights. Decentralized exchanges with private order books. In all of these, delegating to a prover network means surrendering exactly the inputs you need to keep private. I sat down with a researcher at ChainSafe who's working on this specific problem. His approach: adding MPC (multi-party computation) to ZK VMs so proof generation can be delegated privately. Multiple parties each hold a secret share of the data, compute their portion, and combine results — no single party ever sees the full picture. He calls it "make ZK VMs ZK again." He also covered a near-term approach to the deepfake problem: attested sensors that cryptographically sign photo/video metadata at capture, combined with verifiable edit histories. You can't yet verify what IS AI-generated. But you can prove everything that is human — a reverse approach. Prove provenance instead of detecting fakes. The full conversation covers ZK, MPC, and FHE (the "holy trinity of programmable cryptography"), explained through photography analogies that are genuinely useful for building intuition. We filmed it across Taipei — street markets, a botanical garden, a tea ceremony. Full interview: https://youtu.be/PnEivfTpnA8 ————— If we're meeting for the first time, hi 👋! I started building my channel to spread the good word on good work in crypto — something with substance and humanity. A like, sub, and comment goes a long way to supporting me, so please consider doing so!

🔗 [youtu.be](https://youtu.be/PnEivfTpnA8) • 6h ago

---

**[A few thoughts on Culpier's Research](https://www.reddit.com/r/ethereum/comments/1rmopky/a_few_thoughts_on_culpiers_research/)**

1h ago

---

**[Ethereal news weekly #14 | ePBS first devnet live, Aave Labs temp check passed, Synthesis AI + human hackathon](https://www.reddit.com/r/ethereum/comments/1rmcnq6/ethereal_news_weekly_14_epbs_first_devnet_live/)**

ePBS first devnet live, Aave Labs temp check passed, Synthesis AI + human hackathon

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-14/) • 9h ago

---

**[All you need to know about Ethereum Hegota Upgrade](https://www.reddit.com/r/ethereum/comments/1rm299u/all_you_need_to_know_about_ethereum_hegota_upgrade/)**

Hegotá is the official name of a major Ethereum network upgrade planned for the second half of 2026, following the Glamsterdam upgrade expected earlier in the year, and marking Ethereum’s continued shift toward a biannual release cycle. The name blends Bogotá, the Devcon host city, with the star Heze. https://etherworld.co/all-you-need-to-know-about-ethereum-hegota-upgrade/

18h ago

---

**[DigixDAO: The First Major DAO Crowdsale — $5.5M Raised in Under 24 Hours (March 29, 2016)](https://www.reddit.com/r/ethereum/comments/1rmerqx/digixdao_the_first_major_dao_crowdsale_55m_raised/)**

On March 29, 2016, Digix Global launched what became the first major DAO crowdsale on Ethereum. It raised $5.5 million in under 24 hours — at a time when Ethereum's total market cap was around $600 million. What it was: DigixDAO was a governance token (DGD) for a project aiming to tokenize physical gold bars on Ethereum. The crowdsale contract was deployed at block 1,239,208 and compiled with Solidity v0.3.0. Why it mattered: - It was the first DAO-style crowdsale to raise serious money on Ethereum - It proved that decentralized fundraising could work at scale, months before The DAO - The speed of the raise ($5.5M in <24h) shocked even the Ethereum community - It directly inspired the wave of ICOs that followed in 2017 Independent verification: Developer Piper Merriam independently verified the contract code before the sale, establishing one of the earliest examples of third-party smart contract auditing. The original community discussion happened right here on r/ethereum, with this thread documenting the reaction in real-time. Contract: 0xf0160428a8552ac9bb7e050d90eeade4ddd52843 Full writeup with sources: EthereumHistory.com This was just 7 months before The DAO — and in many ways, it was the proof of concept that made The DAO feel possible. We're documenting these pre-2017 contracts before the context disappears.

7h ago

---

**[TerraNullius: The Ethereum Message Board from Block 49,880 (August 7, 2015) — Still Getting Claims in 2026](https://www.reddit.com/r/ethereum/comments/1rlidmx/terranullius_the_ethereum_message_board_from/)**

Two weeks after Ethereum's genesis block, a Reddit user named "Semiel" deployed one of the earliest smart contracts on the network: TerraNullius. What it does: Anyone can "claim" a hex coordinate and attach a message to it — a permanent, uncensorable message board on the blockchain. No tokens, no governance, no economic incentive. Just messages, forever. The numbers: - Deployed at block 49,880 (August 7, 2015) - Compiled with Solidity v0.1.1 - 25 claims in 2015, then it sat mostly dormant - 687 claims during the 2021 NFT boom (people realized these were basically proto-NFTs) - 805 total transactions and counting — still active in 2026 It was referenced by the Guinness World Records and is one of the earliest surviving interactive contracts on Ethereum. The original announcement was a Reddit post right here on r/ethereum, with Semiel sharing a Pastebin script so people could interact with it. What's fascinating is how it predates every pattern we now take for granted — ERC-20, ERC-721, ENS, DAOs. This was someone experimenting with permanence on a chain that was two weeks old. Contract: 0x6e38A457C722C6011B2dfa06d49240e797844d66 Full writeup with sources and verification: EthereumHistory.com If anyone has stories about early Ethereum experiments like this, I'd love to hear them. We're trying to document the pre-2017 era before the context is lost entirely.

1d ago

---

**[Daily General Discussion March 05, 2026](https://www.reddit.com/r/ethereum/comments/1rl9qdi/daily_general_discussion_march_05_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

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

The Block • 10h ago

---

**[Got $1,000? This Cryptocurrency Is a No-Brainer Buy for Long-Term Holding](https://www.fool.com/investing/2026/03/05/got-1000-this-cryptocurrency-is-a-no-brainer-buy-f/)**

The cryptocurrency's status as the leader in decentralized finance makes it hard to beat.

The Motley Fool • 1d ago

---

**[31.6 Million ETH Leaves Exchanges as Vitalik Calls for Ethereum “Sanctuary” Tech](https://finance.yahoo.com/news/31-6-million-eth-leaves-070249895.html)**

ETH accumulation off exchanges continues to surge in early March, while Vitalik Buterin calls for building sanctuary technologies for ETH.

Yahoo Finance • 2d ago

---

**[Ethereum Foundation wants the network to be the trust layer for AI](https://www.coindesk.com/tech/2026/03/04/ethereum-foundation-wants-the-network-to-be-the-trust-layer-for-ai)**

Davide Crapis, the foundation's AI lead,  sees the network acting as a coordination and verification layer in an increasingly AI-mediated world.

CoinDesk • 2d ago

---

**[Bitcoin, XRP, Ethereum Are Having a Great Week. Why Cryptos Are on the Up.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-iran-war-cryptos-ba05311d?gaa_at=eafs&gaa_n=AWEtsqeiqBFQdV90Y4dmbz1cbc6KHhK4QQjrehqFDr5CikGP0fFQ_0461sNO&gaa_ts=69ab3dab&gaa_sig=L7s5NA6pgE09VT3DEB_Z-ae3DQJVR-Fb9WO9GeXuUzJu20iIeinG4kIwlc1y_bJI9OA8hr6pRffGJABfAYnTqA%3D%3D)**

Barron's • 1d ago

---

**[Bit Digital Inc. Reports Monthly Ethereum Treasury and Staking Metrics for February 2026](https://bit-digital.com/press-releases/bit-digital-inc-reports-monthly-ethereum-treasury-and-staking-metrics-for-february-2026/)**

Bit Digital, Inc. (Nasdaq: BTBT), today announced its monthly Ethereum (ETH) treasury and staking metrics for the month of February 2026.

Bit Digital • 1d ago

---

**[Current price of Ethereum for March 4, 2026](https://fortune.com/article/price-of-ethereum-03-04-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 1d ago

---

**[Ethereum Price Corrects Gains, Drifts Toward Key Support Zone](https://www.tradingview.com/news/newsbtc:9632ed3a6094b:0-ethereum-price-corrects-gains-drifts-toward-key-support-zone/)**

Ethereum price started a fresh increase and tested $2,200. ETH is now correcting gains and might decline further if it trades below $2,030.Ethereum Price Starts Downside CorrectionEthereum price started a fresh increase above the $2,065 resistance, like Bitcoin. ETH price rallied above the $2,120 a…

TradingView • 18h ago

---

**[Crypto News: Pepeto Announces Revenue Sharing That Pays Presale Holders Forever as XRP Price Prediction Target $100 and Ethereum Bleeds Fees](https://markets.businessinsider.com/news/stocks/crypto-news-pepeto-announces-revenue-sharing-that-pays-presale-holders-forever-as-xrp-price-prediction-target-100-and-ethereum-bleeds-fees-1035906751)**

Dubai, UAE, March  06, 2026  (GLOBE NEWSWIRE) -- New crypto Pepeto just announced that presale wallets will receive a permanent share of all excha...

markets.businessinsider.com • 1h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Will Not Stay This Cheap! ⚠️ ETH Crypto Token Analysis](https://www.youtube.com/watch?v=jrKbEBTxqFA)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 3K • 👍 136 • 💬 23 • ⏱️ 10:24 • 9h ago

---

**[Whales Are Loading Up on BTC, ETH, ASTER &amp; PUMP – What Do They Know? 👀](https://www.youtube.com/watch?v=qkFFwZjfOA4)**

We analyze the latest crypto whale activity and what it could mean for the broader market. On-chain data is showing large ...

📺 Altcoin Buzz

👁️ 1K • 👍 66 • 💬 63 • ⏱️ 12:09 • 5h ago

---

**[ETH Ethereum Price Prediction: 6th of March](https://www.youtube.com/watch?v=bf0gs5177U8)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 88 • 👍 8 • 💬 3 • ⏱️ 7:22 • 1h ago

---

**[&quot;People Don’t Know How Massive MARCH Will Be for Crypto&quot;: Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=7oRNY59aeTo)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 2K • 👍 62 • 💬 25 • ⏱️ 19:52 • 1d ago

---

**[Tom Lee has gone insane (ethereum).](https://www.youtube.com/watch?v=KUl2p8MQGBg)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 21K • 👍 603 • 💬 21 • ⏱️ 1:16 • 1d ago

---

**[Bitcoin Bottom Forming? ETH Accumulation Surges While Crypto Fear Spikes | MSTR BMNR](https://www.youtube.com/watch?v=qXEAgObFIqo)**

I'm giving away my Weekly Trading Strategy + my new book Money Game FREE ...

📺 MONEY GAME

👁️ 1K • 👍 79 • 💬 12 • ⏱️ 31:22 • 10h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=MlHv6JdY9xw)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 1K • 👍 100 • 💬 3 • ⏱️ 6:30 • 4h ago

---

**[Mark Cuban’s Honest Crypto Prediction (Bitcoin vs Ethereum)](https://www.youtube.com/watch?v=YE1UIgyHq-g)**

Is crypto still the future of investing? Mark Cuban shares his honest take: • Bitcoin isn't going anywhere • Ethereum still has ...

📺 VP Motion

👁️ 752 • 👍 9 • ⏱️ 0:46 • 4h ago

---

**[Vitalik Buterin Is Selling His ETH: What It Means for Ethereum](https://www.youtube.com/watch?v=MminLKRi-x8)**

Follow us on Telegram   https://t.me/+7CAS7-PBmdliY2Uy Friends, there's a really important question on the market right now: is ...

📺 Coin Post

👁️ 69 • 👍 7 • 💬 43 • ⏱️ 10:22 • 3h ago

---

**[URGENT ETHEREUM UPDATE🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=TEAc7s0s4rM)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 283 • 👍 19 • 💬 1 • ⏱️ 5:16 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*
