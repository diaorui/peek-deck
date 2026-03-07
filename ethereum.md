---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-07T02:01:52.075614+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- news
- social
- cryptocurrency
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 07, 2026 at 02:01 UTC  
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

### $1,979.92

---

## Ethereum Chart

**24h:** -4.9%  
**7d:** +2.1%  
**30d:** -4.1%  
**90d:** -36.6%  
**1y:** -10.1%  

---

## Ethereum Market Stats

**Market Cap:** $239.15B
Rank #2

**Circulating Supply:** 120,692,062 ETH
No max supply

**All-Time High:** $4,946.05
-59.9%

**All-Time Low:** $0.43
+457414.1%

---

## Reddit: r/ethereum

**[We verified Vitalik's 2015 token contract and discovered it wasn't compiled with Solidity - it's Serpent](https://www.reddit.com/r/ethereum/comments/1rmheom/we_verified_vitaliks_2015_token_contract_and/)**

I've been working on verifying source code for the oldest contracts on Ethereum, and this one took days to crack. The contract: 0xa2e3680acaf5d2298697bdc016cf75a929385463 Deployed by Vitalik on November 12, 2015 (block 530,996). It's a token contract implementing the standardized currency API from the early ethereum/dapp-bin repo. 1,000,000 initial supply, approve/transfer mechanics - basically a proto-ERC-20. The problem: We tried compiling currency.sol with every Solidity compiler version from that era. Every archived soljson release from v0.1.1 through v0.3.6, nightlies from Sep-Dec 2015, native C++ solc builds from the webthree-umbrella repo, optimizer on and off. Nothing matched. The breakthrough: Three clues pointed us away from Solidity entirely: The on-chain constructor starts with 6000603f53 (MSTORE8-based memory init). Every Solidity version produces 60606040525b (the free memory pointer pattern). This is a fundamentally different code generation approach. The runtime code uses MSIZE, SWAP1, MSIZE, ADD for memory allocation. This is the Serpent compiler's alloc() pattern - not found in any version of solc. Two function selectors didn't match the Solidity source: disapprove() instead of unapprove(), and isApprovedOnceFor() instead of isApprovedOnce(). The answer: The contract was compiled from currency.se (the Serpent version), not currency.sol. The ethereum/dapp-bin repo had both implementations side by side. Vitalik deployed his own language's version. Compiled with the Serpent compiler at commit f0b4128 (Oct 15, 2015) - byte-for-byte identical, all 1,661 bytes. Full methodology, source, and proof: github.com/cartoonitunes/vitalik-currency-verification We've submitted a manual verification request to Etherscan since they don't support Serpent as a verification language. Hopefully they can add it as a verified contract with source. This is part of a broader effort to verify and preserve the earliest contracts on Ethereum. A lot of historically important contracts from 2015-2016 are still unverified because the compiler versions are too old for Etherscan's automated tools.

10h ago

---

**[Best SUI to ETH Bridge?](https://www.reddit.com/r/ethereum/comments/1rmu6fk/best_sui_to_eth_bridge/)**

Hi everyone. I’ve been holding some SUI and I’m thinking about moving a portion to Ethereum. I haven’t done a cross chain transfer from Sui before, so I’m trying to understand what people normally use. What bridge do you prefer when going from SUI to ETH? Just looking for something simple and reliable and with the most affordable fees :))) Muchas gracias!!!!

2h ago

---

**[Minimmit vs Casper FFG](https://www.reddit.com/r/ethereum/comments/1rmmoln/minimmit_vs_casper_ffg/)**

One important technical item that I forgot to mention is the proposed switch from Casper FFG to Minimmit as the finality gadget. To summarize, Casper FFG provides two-round finality: it requires each attester to sign once to "justify" the block, and then again to "finalize" it. Minimmit only requires one round. In exchange, Minimmit's fault tolerance (in our parametrization) drops to 17%, compared to Casper FFG's 33%. Within Ethereum consensus discussions, I have always been the security assumptions hawk: I've insisted on getting to the theoretical bound of 49% fault tolerance under synchrony, kept pushing for 51% attack recovery gadgets, came up with DAS to make data availability checks dishonest-majority-resistant, etc. But I am fine with Minimmit's properties, in fact even enthusiastic in some respects. In this post, I will explain why. Let's lay out the exact security properties of both 3SF (not the current beacon chain, which is needlessly weak in many ways, but the ideal 3SF) and Minimmit. "Synchronous network" means "network latency less than 1/4 slot or so", "asynchronous network" means "potentially very high latency, even some nodes go offline for hours at a time". The percentages ("attacker has <33%") refer to percentages of active staked ETH. Properties of 3SF Synchronous network case: Attacker has p < 33%: nothing bad happens 33% < p < 50%: attacker can stop finality (at the cost of losing massive funds via inactivity leak), but the chain keeps progressing normally 50% < p < 67%: attacker can censor or revert the chain, but cannot revert finality. If an attacker censors, good guys can self-organize, they can stop contributing to a censoring chain, and do a "minority soft fork" p > 67%: attacker can finalize things at will, much harder for good guys to do minority soft fork Asynchronous network case: Attacker has p < 33%: cannot revert finality p > 33%: can revert finality, at the cost of losing massive funds via slashing Properties of Minimmit Synchronous network case: Attacker has p < 17%: nothing bad happens 17% < p < 50%: attacker can stop finality (at the cost of losing massive funds via inactivity leak), but the chain keeps progressing normally 50% < p < 83%: attacker can censor or revert the chain, but cannot revert finality. If an attacker censors, good guys can self-organize, they can stop contributing to a censoring chain, and do a "minority soft fork" p > 83%: attacker can finalize things at will, much harder for good guys to do minority soft fork Asynchronous network case: Attacker has p < 17%: cannot revert finality p > 17%: can revert finality, at the cost of losing massive funds via slashing I actually think that the latter is a better tradeoff. Here's my reasoning why: The worst kind of attack is actually not finality reversion, it's censorship. The reason is that finality reversion creates massive publicly available evidence that can be used to immediately cost the attacker millions of ETH (ie. billions of dollars), whereas censorship requires social coordination to get around In both of the above, a censorship attack requires 50% A censorship attack becomes much harder to coordinate around when the censoring attacker can unilaterally finalize (ie. >67% in 3SF, >83% in Minimmit). If they can't, then if the good guys counter-coordinate, you get two non-finalizing chains dueling for a few days, and users can pick on. If they can, then there's no natural schelling point to coordinate soft-forking In the case of a client bug, the worst thing that can happen is finalizing something bugged. In 3SF, you only need 67% of clients to share a bug for it to finalize, in Minimmit, you need 83%. Basicallly, Minimmit maximizes the set of situations that "default to two chains dueling each other", and that is actually a much healthier and much more recoverable outcome than "the wrong thing finalizing". We want finality to mean final. So in situations of uncertainty (whether attacks or software bugs), we should be more okay with having periods of hours or days where the chain does not finalize, and instead progresses based on the fork choice rule. This gives us time to think and make sure which chain is correct. Also, I think the "33% slashed to revert finality" of 3SF is overkill. If there is even eg. 15 million ETH staking, then that's 5M ($10B) slashed to revert the chain once. If you had $10B, and you are willing to commit mayhem of a type that violates many countries' computer hacking laws, there are FAR BETTER ways to spend it than to attack a chain. Even if your goal is breaking Ethereum, there are far better attack vectors. And so if we have the baseline guarantee of >= 17% slashed to revert finality (which Minimmit provides), we should judge the two systems from there based on their other properties - where, for the reasons I described above, I think Minimmit performs better.

7h ago

---

**[Daily General Discussion March 06, 2026](https://www.reddit.com/r/ethereum/comments/1rm5yqw/daily_general_discussion_march_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

20h ago

---

**[Steth Question](https://www.reddit.com/r/ethereum/comments/1rmufd1/steth_question/)**

So I have some Eth staked on lido and received steth in return. After a few people I know told me I can deposit steth to double dip, earn steth rewards and earn rewards on steth coins as well? Does anyone have any suggestions? I’ve checked morpho, and aave but can’t seem to find any information on lending steth in return for more rewards? Ive also heard of curve and harvest but I’m not familiar with either. Any safe suggestions would be greatly appreciated, as i treasure my Eth and I’m not trying to jeopardize it any way to make a small return. I’m just trying to maximize the amount of Eth I have and letting it work to grow more. Thanks

2h ago

---

**[ZK VMs made verifiable computation accessible to any developer. The prover networks running them require your full plaintext data. YIKES](https://www.reddit.com/r/ethereum/comments/1rmg9sa/zk_vms_made_verifiable_computation_accessible_to/)**

Zero-knowledge cryptography went through three phases. First: hand-crafted arithmetic circuits, only accessible to deep researchers. Second: ZK virtual machines — suddenly any developer could write verifiable code in Rust or C. Third: prover networks (Succinct, Boundless/RiscZero) that let you delegate the heavy proof generation to external infrastructure. Each phase made the technology more accessible. Each phase also moved the user's data further from their control. Prover networks require your full plaintext data to generate proofs. For rollups, this is a non-issue — public ledger, no privacy expectation, and what you gain (succinctness — compressing thousands of transactions into a single proof) is worth the trade. That's the use case these networks were built for, and they served it well. The problem emerges when you extend this model to user-facing applications. Verifiable identity: proving you hold a valid passport, proving you're over 18, without disclosing the underlying data. Private AI inference: running a model on your data without the model owner seeing your inputs or you seeing their weights. Decentralized exchanges with private order books. In all of these, delegating to a prover network means surrendering exactly the inputs you need to keep private. I sat down with a researcher at ChainSafe who's working on this specific problem. His approach: adding MPC (multi-party computation) to ZK VMs so proof generation can be delegated privately. Multiple parties each hold a secret share of the data, compute their portion, and combine results — no single party ever sees the full picture. He calls it "make ZK VMs ZK again." He also covered a near-term approach to the deepfake problem: attested sensors that cryptographically sign photo/video metadata at capture, combined with verifiable edit histories. You can't yet verify what IS AI-generated. But you can prove everything that is human — a reverse approach. Prove provenance instead of detecting fakes. The full conversation covers ZK, MPC, and FHE (the "holy trinity of programmable cryptography"), explained through photography analogies that are genuinely useful for building intuition. We filmed it across Taipei — street markets, a botanical garden, a tea ceremony. Full interview: https://youtu.be/PnEivfTpnA8 ————— If we're meeting for the first time, hi 👋! I started building my channel to spread the good word on good work in crypto — something with substance and humanity. A like, sub, and comment goes a long way to supporting me, so please consider doing so!

🔗 [youtu.be](https://youtu.be/PnEivfTpnA8) • 11h ago

---

**[ETH staking time on exodus](https://www.reddit.com/r/ethereum/comments/1rmuq0z/eth_staking_time_on_exodus/)**

I staked some ETH around a month ago and it still has the Staking..... "staking takes 5 days" prompt. How long does it normally take to stake ETH and should I be worried?

1h ago

---

**[A few thoughts on Culpier's Research](https://www.reddit.com/r/ethereum/comments/1rmopky/a_few_thoughts_on_culpiers_research/)**

5h ago

---

**[(UPDATE) 1.5 Eth stolen from Trust Wallet](https://www.reddit.com/r/ethereum/comments/1rmphbh/update_15_eth_stolen_from_trust_wallet/)**

5h ago

---

**[DigixDAO: The First Major DAO Crowdsale — $5.5M Raised in Under 24 Hours (March 29, 2016)](https://www.reddit.com/r/ethereum/comments/1rmerqx/digixdao_the_first_major_dao_crowdsale_55m_raised/)**

On March 29, 2016, Digix Global launched what became the first major DAO crowdsale on Ethereum. It raised $5.5 million in under 24 hours — at a time when Ethereum's total market cap was around $600 million. What it was: DigixDAO was a governance token (DGD) for a project aiming to tokenize physical gold bars on Ethereum. The crowdsale contract was deployed at block 1,239,208 and compiled with Solidity v0.3.0. Why it mattered: - It was the first DAO-style crowdsale to raise serious money on Ethereum - It proved that decentralized fundraising could work at scale, months before The DAO - The speed of the raise ($5.5M in <24h) shocked even the Ethereum community - It directly inspired the wave of ICOs that followed in 2017 Independent verification: Developer Piper Merriam independently verified the contract code before the sale, establishing one of the earliest examples of third-party smart contract auditing. The original community discussion happened right here on r/ethereum, with this thread documenting the reaction in real-time. Contract: 0xf0160428a8552ac9bb7e050d90eeade4ddd52843 Full writeup with sources: EthereumHistory.com This was just 7 months before The DAO — and in many ways, it was the proof of concept that made The DAO feel possible. We're documenting these pre-2017 contracts before the context disappears.

12h ago

---

---

## Google News: "ethereum"

**[Bitcoin Price Predictions Flip Bullish, But Ethereum Is Still Stuck](https://decrypt.co/360131/bitcoin-price-predictions-flip-bullish-but-ethereum-stuck)**

Prediction market traders are becoming more bullish on Bitcoin's near-term price, but they're not as confident on Ethereum.

Decrypt • 2d ago

---

**[$31.6M Ethereum Leaves Exchanges as Supply Hits Multi-Year Lows – Is a Price Reversal Coming?](https://finance.yahoo.com/news/31-6m-ethereum-leaves-exchanges-222200336.html)**

Ethereum just saw a noticeable shift in liquidity, which might affect ETH price positively.About $31.6 million worth of ETH left centralized exchanges in a single day, pushing exchange reserves down to multi-year lows. Moves like this usually mean coins are being pulled into long-term storage rather than prepared for sale.Ethereum ...

Yahoo Finance • 3h ago

---

**[Got $1,000? This Cryptocurrency Is a No-Brainer Buy for Long-Term Holding](https://www.fool.com/investing/2026/03/05/got-1000-this-cryptocurrency-is-a-no-brainer-buy-f/)**

The cryptocurrency's status as the leader in decentralized finance makes it hard to beat.

The Motley Fool • 1d ago

---

**[Bitcoin, XRP, Ethereum Are Having a Great Week. Why Cryptos Are on the Up.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-iran-war-cryptos-ba05311d?gaa_at=eafs&gaa_n=AWEtsqdDqaVuq3V7ld4GWW84nz7lpP0C3ED6qQP0gswRs8ACRVvkcVo5Bo45&gaa_ts=69ab8a7c&gaa_sig=uo8nRS3bDjL7DpztTmxXnjOEHjnLfiIQXArTJExgp-k2NQ_kuUmIvi4cSFBJf5rj6whFUmnOVb2tXH_EN0hwOw%3D%3D)**

Barron's • 1d ago

---

**[Bit Digital Inc. Reports Monthly Ethereum Treasury and Staking Metrics for February 2026](https://bit-digital.com/press-releases/bit-digital-inc-reports-monthly-ethereum-treasury-and-staking-metrics-for-february-2026/)**

Bit Digital, Inc. (Nasdaq: BTBT), today announced its monthly Ethereum (ETH) treasury and staking metrics for the month of February 2026.

Bit Digital • 1d ago

---

**[Ethereum Foundation wants the network to be the trust layer for AI](https://www.coindesk.com/tech/2026/03/04/ethereum-foundation-wants-the-network-to-be-the-trust-layer-for-ai)**

Davide Crapis, the foundation's AI lead,  sees the network acting as a coordination and verification layer in an increasingly AI-mediated world.

CoinDesk • 2d ago

---

**[Current price of Ethereum for March 4, 2026](https://fortune.com/article/price-of-ethereum-03-04-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 2d ago

---

**[Ethereum Based Crypto Pepeto Announces Former Binance Expert on Advisory Board - Dogecoin and Elon Musk Shape Crypto](https://markets.businessinsider.com/news/stocks/ethereum-based-crypto-pepeto-announces-former-binance-expert-on-advisory-board---dogecoin-and-elon-musk-shape-crypto-1035907239)**

Dubai, UAE, March  06, 2026  (GLOBE NEWSWIRE) -- Pepeto just announced that a former Binance executive has joined the strategic advisory board of ...

markets.businessinsider.com • 1h ago

---

**[Vitalik Buterin calls for bolder experimentation in Ethereum's app layer while preserving core principles](https://www.theblock.co/post/392621/vitalik-buterin-calls-for-bolder-experimentation-in-ethereums-app-layer-while-preserving-core-principles)**

Vitalik Buterin has urged Ethereum developers to experiment more boldly at the app layer while preserving the network’s core principles.

The Block • 15h ago

---

**[Bullish sees Bitcoin, Ethereum volatility almost double in February (BLSH:NYSE)](https://seekingalpha.com/news/4561826-bullish-sees-bitcoin-ethereum-volatility-almost-double-in-february)**

Seeking Alpha • 13h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Will Not Stay This Cheap! ⚠️ ETH Crypto Token Analysis](https://www.youtube.com/watch?v=jrKbEBTxqFA)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 3K • 👍 154 • 💬 29 • ⏱️ 10:24 • 14h ago

---

**[ETH Ethereum Price Prediction: 6th of March](https://www.youtube.com/watch?v=bf0gs5177U8)**

Welcome to Czar Gets Crypto! Please note the following: Educational Purposes Only: All content on this channel is for ...

📺 C-Zar Gets Crypto 

👁️ 203 • 👍 18 • 💬 4 • ⏱️ 7:22 • 6h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=MlHv6JdY9xw)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 120 • 💬 5 • ⏱️ 6:30 • 9h ago

---

**[&quot;People Don’t Know How Massive MARCH Will Be for Crypto&quot;: Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=7oRNY59aeTo)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 2K • 👍 67 • 💬 11 • ⏱️ 19:52 • 1d ago

---

**[Whales Are Loading Up on BTC, ETH, ASTER &amp; PUMP – What Do They Know? 👀](https://www.youtube.com/watch?v=qkFFwZjfOA4)**

We analyze the latest crypto whale activity and what it could mean for the broader market. On-chain data is showing large ...

📺 Altcoin Buzz

👁️ 1K • 👍 78 • 💬 84 • ⏱️ 12:09 • 9h ago

---

**[BITCOIN &amp; ALTCOIN WARNING: Signal Confirmed!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=ydehcU1COIw)**

BITCOIN & ALTCOIN WARNING: Signal Confirmed!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 802 • 👍 58 • 💬 8 • ⏱️ 18:59 • 59m ago

---

**[Tom Lee has gone insane (ethereum).](https://www.youtube.com/watch?v=KUl2p8MQGBg)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 22K • 👍 614 • 💬 20 • ⏱️ 1:16 • 1d ago

---

**[Mark Cuban’s Honest Crypto Prediction (Bitcoin vs Ethereum)](https://www.youtube.com/watch?v=YE1UIgyHq-g)**

Is crypto still the future of investing? Mark Cuban shares his honest take: • Bitcoin isn't going anywhere • Ethereum still has ...

📺 VP Motion

👁️ 1K • 👍 12 • 💬 1 • ⏱️ 0:46 • 9h ago

---

**[Bitcoin Bottom Forming? ETH Accumulation Surges While Crypto Fear Spikes | MSTR BMNR](https://www.youtube.com/watch?v=qXEAgObFIqo)**

I'm giving away my Weekly Trading Strategy + my new book Money Game FREE ...

📺 MONEY GAME

👁️ 1K • 👍 81 • 💬 12 • ⏱️ 31:22 • 14h ago

---

**[BITCOIN: Watch Out for This Move! (big warning) - BTC, ETH Price Prediction Today](https://www.youtube.com/watch?v=qFlz6OhhLK4)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 7K • 👍 464 • 💬 97 • ⏱️ 12:55 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
