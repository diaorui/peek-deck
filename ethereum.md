---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-03-07T23:46:11.113104+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- cryptocurrency
- news
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** March 07, 2026 at 23:46 UTC  
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

### $1,966.03

---

## Ethereum Chart

**24h:** -0.6%  
**7d:** +1.6%  
**30d:** -4.5%  
**90d:** -36.9%  
**1y:** -10.5%  

---

## Ethereum Market Stats

**Market Cap:** $237.79B
Rank #2

**Circulating Supply:** 120,692,062 ETH
No max supply

**All-Time High:** $4,946.05
-60.1%

**All-Time Low:** $0.43
+455208.5%

---

## Reddit: r/ethereum

**[Daily General Discussion March 07, 2026](https://www.reddit.com/r/ethereum/comments/1rn247q/daily_general_discussion_march_07_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

17h ago

---

**[New ways to track verification proofs for source code of Ethereum's earliest contracts](https://www.reddit.com/r/ethereum/comments/1rna5a2/new_ways_to_track_verification_proofs_for_source/)**

Yesterday I posted about verifying Vitalik's first token contract and got a great response. A few people asked how to follow along as more proofs are published, so I set up two places to track them: GitHub: awesome-ethereum-proofs - each proof has its own repo with a reproducible verification script Web: ethereumhistory.com/proofs - browse all verified contracts with deployment dates, compiler versions, and methodology Most contracts deployed in August 2015 have no verified source on Etherscan. The compilers are too old for automated tools, source code was hosted on Pastebin links that expired years ago, and some contracts used languages Etherscan doesn't even support (Serpent, LLL). So I've been doing it manually - testing every early compiler version against on-chain bytecode until I get a byte-for-byte match. Since the Vitalik post, here are 4 new proofs: "Test" - First Executable Contract (Aug 7, 2015, block 48,643) The earliest contract with executable code on Ethereum mainnet. Compiled with soljson v0.1.1, the first publicly available Solidity compiler release. Just 8 days after mainnet launch. Hello World Greeter (Aug 7, 2015, block 48,681) Ethereum's "Hello World" moment. Deployed 38 blocks after the first executable contract, same day, same compiler. Based on the greeter tutorial that shipped with the early Ethereum documentation. EarlyChainLetter10ETH (Aug 8, 2015, block 49,931) A chain letter pyramid contract from day 2 of smart contract deployment. One of the first attempts at a financial game on Ethereum. Participants sent 10 ETH to join, and the contract would pay out earlier participants as new ones joined. FunDistributor (Aug 10, 2015, block 62,632) A "king of the hill" behavioral economics experiment. Send more than 1% of the contract's balance to become the receiver. If nobody touches the contract for 200+ blocks (~45 min), the current receiver gets paid out. The original source was on Pastebin (link expired) - had to reconstruct it entirely from bytecode. Interesting discrepancy: the Reddit announcement said the payout was 25% of the balance, but the verified code shows this.balance / 3 (33.3%). Some things I've learned doing this: Operand order matters in solc 0.1.1. msg.value * 100 and 100 * msg.value produce different bytecode because the compiler evaluates right-to-left. The private keyword existed in solc 0.1.1 but was almost never used. FunDistributor is one of the earliest known uses. Solidity function declaration order affects optimizer output. Changing the order of functions in the source can completely change the compiled bytecode. There are 11 proofs so far covering contracts from Aug 2015 through Apr 2016, including Serpent, Solidity, and contracts by Vitalik and Gavin Wood. More coming as I work through the earliest blocks. If you know of any early contracts with lost source code, I'd love to hear about them.

10h ago

---

**[Wrapping USDT](https://www.reddit.com/r/ethereum/comments/1rnby8b/wrapping_usdt/)**

I propose to wrap USDT, since currently it is a highly outdated coin, and its transfer function has issues, and doesn't have new features, and only has 6 decimals. While these issues may not be large now and can be easily fixed or do not lose too much functionality, as DeFi expands new standards, etc may add more features, then USDT can be put into a standardized wrapper to handle it.

8h ago

---

**[We verified Vitalik's 2015 token contract and discovered it wasn't compiled with Solidity - it's Serpent](https://www.reddit.com/r/ethereum/comments/1rmheom/we_verified_vitaliks_2015_token_contract_and/)**

I've been working on verifying source code for the oldest contracts on Ethereum, and this one took days to crack. The contract: 0xa2e3680acaf5d2298697bdc016cf75a929385463 Deployed by Vitalik on November 12, 2015 (block 530,996). It's a token contract implementing the standardized currency API from the early ethereum/dapp-bin repo. 1,000,000 initial supply, approve/transfer mechanics - basically a proto-ERC-20. The problem: We tried compiling currency.sol with every Solidity compiler version from that era. Every archived soljson release from v0.1.1 through v0.3.6, nightlies from Sep-Dec 2015, native C++ solc builds from the webthree-umbrella repo, optimizer on and off. Nothing matched. The breakthrough: Three clues pointed us away from Solidity entirely: The on-chain constructor starts with 6000603f53 (MSTORE8-based memory init). Every Solidity version produces 60606040525b (the free memory pointer pattern). This is a fundamentally different code generation approach. The runtime code uses MSIZE, SWAP1, MSIZE, ADD for memory allocation. This is the Serpent compiler's alloc() pattern - not found in any version of solc. Two function selectors didn't match the Solidity source: disapprove() instead of unapprove(), and isApprovedOnceFor() instead of isApprovedOnce(). The answer: The contract was compiled from currency.se (the Serpent version), not currency.sol. The ethereum/dapp-bin repo had both implementations side by side. Vitalik deployed his own language's version. Compiled with the Serpent compiler at commit f0b4128 (Oct 15, 2015) - byte-for-byte identical, all 1,661 bytes. Full methodology, source, and proof: github.com/cartoonitunes/vitalik-currency-verification We've submitted a manual verification request to Etherscan since they don't support Serpent as a verification language. Hopefully they can add it as a verified contract with source. This is part of a broader effort to verify and preserve the earliest contracts on Ethereum. A lot of historically important contracts from 2015-2016 are still unverified because the compiler versions are too old for Etherscan's automated tools.

1d ago

---

**[ETH staking time on exodus](https://www.reddit.com/r/ethereum/comments/1rmuq0z/eth_staking_time_on_exodus/)**

I staked some ETH around a month ago and it still has the Staking..... "staking takes 5 days" prompt. How long does it normally take to stake ETH and should I be worried?

23h ago

---

**[Minimmit vs Casper FFG](https://www.reddit.com/r/ethereum/comments/1rmmoln/minimmit_vs_casper_ffg/)**

One important technical item that I forgot to mention is the proposed switch from Casper FFG to Minimmit as the finality gadget. To summarize, Casper FFG provides two-round finality: it requires each attester to sign once to "justify" the block, and then again to "finalize" it. Minimmit only requires one round. In exchange, Minimmit's fault tolerance (in our parametrization) drops to 17%, compared to Casper FFG's 33%. Within Ethereum consensus discussions, I have always been the security assumptions hawk: I've insisted on getting to the theoretical bound of 49% fault tolerance under synchrony, kept pushing for 51% attack recovery gadgets, came up with DAS to make data availability checks dishonest-majority-resistant, etc. But I am fine with Minimmit's properties, in fact even enthusiastic in some respects. In this post, I will explain why. Let's lay out the exact security properties of both 3SF (not the current beacon chain, which is needlessly weak in many ways, but the ideal 3SF) and Minimmit. "Synchronous network" means "network latency less than 1/4 slot or so", "asynchronous network" means "potentially very high latency, even some nodes go offline for hours at a time". The percentages ("attacker has <33%") refer to percentages of active staked ETH. Properties of 3SF Synchronous network case: Attacker has p < 33%: nothing bad happens 33% < p < 50%: attacker can stop finality (at the cost of losing massive funds via inactivity leak), but the chain keeps progressing normally 50% < p < 67%: attacker can censor or revert the chain, but cannot revert finality. If an attacker censors, good guys can self-organize, they can stop contributing to a censoring chain, and do a "minority soft fork" p > 67%: attacker can finalize things at will, much harder for good guys to do minority soft fork Asynchronous network case: Attacker has p < 33%: cannot revert finality p > 33%: can revert finality, at the cost of losing massive funds via slashing Properties of Minimmit Synchronous network case: Attacker has p < 17%: nothing bad happens 17% < p < 50%: attacker can stop finality (at the cost of losing massive funds via inactivity leak), but the chain keeps progressing normally 50% < p < 83%: attacker can censor or revert the chain, but cannot revert finality. If an attacker censors, good guys can self-organize, they can stop contributing to a censoring chain, and do a "minority soft fork" p > 83%: attacker can finalize things at will, much harder for good guys to do minority soft fork Asynchronous network case: Attacker has p < 17%: cannot revert finality p > 17%: can revert finality, at the cost of losing massive funds via slashing I actually think that the latter is a better tradeoff. Here's my reasoning why: The worst kind of attack is actually not finality reversion, it's censorship. The reason is that finality reversion creates massive publicly available evidence that can be used to immediately cost the attacker millions of ETH (ie. billions of dollars), whereas censorship requires social coordination to get around In both of the above, a censorship attack requires 50% A censorship attack becomes much harder to coordinate around when the censoring attacker can unilaterally finalize (ie. >67% in 3SF, >83% in Minimmit). If they can't, then if the good guys counter-coordinate, you get two non-finalizing chains dueling for a few days, and users can pick on. If they can, then there's no natural schelling point to coordinate soft-forking In the case of a client bug, the worst thing that can happen is finalizing something bugged. In 3SF, you only need 67% of clients to share a bug for it to finalize, in Minimmit, you need 83%. Basicallly, Minimmit maximizes the set of situations that "default to two chains dueling each other", and that is actually a much healthier and much more recoverable outcome than "the wrong thing finalizing". We want finality to mean final. So in situations of uncertainty (whether attacks or software bugs), we should be more okay with having periods of hours or days where the chain does not finalize, and instead progresses based on the fork choice rule. This gives us time to think and make sure which chain is correct. Also, I think the "33% slashed to revert finality" of 3SF is overkill. If there is even eg. 15 million ETH staking, then that's 5M ($10B) slashed to revert the chain once. If you had $10B, and you are willing to commit mayhem of a type that violates many countries' computer hacking laws, there are FAR BETTER ways to spend it than to attack a chain. Even if your goal is breaking Ethereum, there are far better attack vectors. And so if we have the baseline guarantee of >= 17% slashed to revert finality (which Minimmit provides), we should judge the two systems from there based on their other properties - where, for the reasons I described above, I think Minimmit performs better.

1d ago

---

**[Steth Question](https://www.reddit.com/r/ethereum/comments/1rmufd1/steth_question/)**

So I have some Eth staked on lido and received steth in return. After a few people I know told me I can deposit steth to double dip, earn steth rewards and earn rewards on steth coins as well? Does anyone have any suggestions? I’ve checked morpho, and aave but can’t seem to find any information on lending steth in return for more rewards? Ive also heard of curve and harvest but I’m not familiar with either. Any safe suggestions would be greatly appreciated, as i treasure my Eth and I’m not trying to jeopardize it any way to make a small return. I’m just trying to maximize the amount of Eth I have and letting it work to grow more. Thanks

23h ago

---

**[Daily General Discussion March 06, 2026](https://www.reddit.com/r/ethereum/comments/1rm5yqw/daily_general_discussion_march_06_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[(UPDATE) 1.5 Eth stolen from Trust Wallet](https://www.reddit.com/r/ethereum/comments/1rmphbh/update_15_eth_stolen_from_trust_wallet/)**

1d ago

---

**[ZK VMs made verifiable computation accessible to any developer. The prover networks running them require your full plaintext data. YIKES](https://www.reddit.com/r/ethereum/comments/1rmg9sa/zk_vms_made_verifiable_computation_accessible_to/)**

Zero-knowledge cryptography went through three phases. First: hand-crafted arithmetic circuits, only accessible to deep researchers. Second: ZK virtual machines — suddenly any developer could write verifiable code in Rust or C. Third: prover networks (Succinct, Boundless/RiscZero) that let you delegate the heavy proof generation to external infrastructure. Each phase made the technology more accessible. Each phase also moved the user's data further from their control. Prover networks require your full plaintext data to generate proofs. For rollups, this is a non-issue — public ledger, no privacy expectation, and what you gain (succinctness — compressing thousands of transactions into a single proof) is worth the trade. That's the use case these networks were built for, and they served it well. The problem emerges when you extend this model to user-facing applications. Verifiable identity: proving you hold a valid passport, proving you're over 18, without disclosing the underlying data. Private AI inference: running a model on your data without the model owner seeing your inputs or you seeing their weights. Decentralized exchanges with private order books. In all of these, delegating to a prover network means surrendering exactly the inputs you need to keep private. I sat down with a researcher at ChainSafe who's working on this specific problem. His approach: adding MPC (multi-party computation) to ZK VMs so proof generation can be delegated privately. Multiple parties each hold a secret share of the data, compute their portion, and combine results — no single party ever sees the full picture. He calls it "make ZK VMs ZK again." He also covered a near-term approach to the deepfake problem: attested sensors that cryptographically sign photo/video metadata at capture, combined with verifiable edit histories. You can't yet verify what IS AI-generated. But you can prove everything that is human — a reverse approach. Prove provenance instead of detecting fakes. The full conversation covers ZK, MPC, and FHE (the "holy trinity of programmable cryptography"), explained through photography analogies that are genuinely useful for building intuition. We filmed it across Taipei — street markets, a botanical garden, a tea ceremony. Full interview: https://youtu.be/PnEivfTpnA8 ————— If we're meeting for the first time, hi 👋! I started building my channel to spread the good word on good work in crypto — something with substance and humanity. A like, sub, and comment goes a long way to supporting me, so please consider doing so!

🔗 [youtu.be](https://youtu.be/PnEivfTpnA8) • 1d ago

---

---

## Google News: "ethereum"

**[Bitcoin, XRP, Ethereum Are Having a Great Week. Why Cryptos Are on the Up.](https://www.barrons.com/articles/bitcoin-xrp-ethereum-iran-war-cryptos-ba05311d?gaa_at=eafs&gaa_n=AWEtsqe_Th3uumofYF1GuI1z_ndDARBMOMgfcK27RHyubszLVwhftH8JWJ3o&gaa_ts=69acbc30&gaa_sig=S2Se_kFEHBCWgHz5HZFyuGY605Xm5qtcvHH66ywtUSeb3lk3FEydR9d26K1ds79LhKqaQfP9K-ydXe4NhGyIxg%3D%3D)**

Barron's • 2d ago

---

**[Current price of Ethereum for March 4, 2026](https://fortune.com/article/price-of-ethereum-03-04-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 3d ago

---

**[What Will Bitcoin, ETH and XRP Be Worth in 2030? ChatGPT’s Price Predictions May Shock You](https://www.ccn.com/education/crypto/chatgpt-predicts-2030-crypto-prices-bitcoin-500k-eth-20k-xrp-20/)**

CCN.com • 2d ago

---

**[Bit Digital Inc. Reports Monthly Ethereum Treasury and Staking Metrics for February 2026](https://bit-digital.com/press-releases/bit-digital-inc-reports-monthly-ethereum-treasury-and-staking-metrics-for-february-2026/)**

Bit Digital, Inc. (Nasdaq: BTBT), today announced its monthly Ethereum (ETH) treasury and staking metrics for the month of February 2026.

Bit Digital • 2d ago

---

**[Prediction: Silver Could Soar Again in 2026 -- but These 2 Cryptocurrencies Have Even Better Upside](https://www.fool.com/investing/2026/03/06/prediction-silver-could-soar-again-in-2026-but-the/)**

Smart-contract cryptos could be the silver to Bitcoin's digital gold.

The Motley Fool • 1d ago

---

**[Ethereum – BlackRock drops ETH ETF staking fee as firm issues ‘warning’](https://ambcrypto.com/ethereum-blackrock-drops-eth-etf-staking-fee-after-firm-issues-warning/)**

Culper Research has shorted ETH citing underlying Ethereum staking and validator crisis.

AMBCrypto • 3h ago

---

**[Vitalik Buterin calls for bolder experimentation in Ethereum's app layer while preserving core principles](https://www.theblock.co/post/392621/vitalik-buterin-calls-for-bolder-experimentation-in-ethereums-app-layer-while-preserving-core-principles)**

Vitalik Buterin has urged Ethereum developers to experiment more boldly at the app layer while preserving the network’s core principles.

The Block • 1d ago

---

**[Ethereum Based Crypto Pepeto Announces Former Binance Expert on Advisory Board - Dogecoin and Elon Musk Shape Crypto](https://markets.businessinsider.com/news/stocks/ethereum-based-crypto-pepeto-announces-former-binance-expert-on-advisory-board---dogecoin-and-elon-musk-shape-crypto-1035907239)**

Dubai, UAE, March  06, 2026  (GLOBE NEWSWIRE) -- Pepeto just announced that a former Binance executive has joined the strategic advisory board of ...

markets.businessinsider.com • 23h ago

---

**[ETH, BMNR news: Short seller Culper Research says ether tokenomics is 'impaired'](https://www.coindesk.com/markets/2026/03/05/short-seller-culper-bets-against-ether-bitmine-citing-death-spiral-risk)**

The short seller firm said that Ethereum's native token is "impaired," leaving treasury firm BitMine holding the bag while co-founder Vitalik buterin is selling.

CoinDesk • 1d ago

---

**[Bullish sees Bitcoin, Ethereum volatility almost double in February (BLSH:NYSE)](https://seekingalpha.com/news/4561826-bullish-sees-bitcoin-ethereum-volatility-almost-double-in-february)**

Seeking Alpha • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Bitcoin &amp; Ethereum Are About To Explode (SERIOUSLY)](https://www.youtube.com/watch?v=i5mW_EafMaI)**

Crypto Is About To Surprise EVERYONE!! (SERIOUSLY) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily Become a ...

📺 Altcoin Daily

👁️ 9K • 👍 873 • 💬 99 • ⏱️ 11:32 • 3h ago

---

**[Ethereum To 85x From Here? Cathie Wood ETH Price Targets Are Insane!](https://www.youtube.com/watch?v=Qn2OgJ2Q_ZQ)**

Cathie Wood legitimately thinks that Ethereum can do a 85x from now until 2032. Sound insane? Here's her entire thesis.

📺 Zach Humphries

👁️ 972 • 👍 80 • 💬 105 • ⏱️ 7:38 • 7h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=rUWDg8L-URM)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 585 • 👍 71 • 💬 15 • ⏱️ 3:42 • 2h ago

---

**[Ethereum Will Not Stay This Cheap! ⚠️ ETH Crypto Token Analysis](https://www.youtube.com/watch?v=jrKbEBTxqFA)**

Join Premium: https://the-bitcoin-strategy.com My Chart Software: https://the-bitcoin-strategy.com/tradingview My Hardware Wallet: ...

📺 Gerhard - Bitcoin Strategy

👁️ 5K • 👍 189 • 💬 31 • ⏱️ 10:24 • 1d ago

---

**[BITCOIN: The Reverse Squeeze Just Started (Warning)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=7bIFSyrYf_0)**

BITCOIN: The Reverse Squeeze Just Started (Warning)!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 674 • 👍 47 • 💬 50 • ⏱️ 17:36 • 58m ago

---

**[LIVE: Trump Announces Important News About Crypto! This Speech Will Change the Crypto Industry](https://www.youtube.com/watch?v=-klaBTHjhQg)**

TrumpCrypto2026 #DigitalAssets #TrumpAnnouncement Welcome to the Trump Crypto Forum 2026 — streaming LIVE from ...

📺 The Pits TV

👁️ 3K • 👍 1K • 4h ago

---

**[LONG-TERM ETH PREDICTION UPDATE🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=p4Sz-ksUU_Q)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 211 • 👍 8 • 💬 3 • ⏱️ 4:45 • 13h ago

---

**[Tom Lee has gone insane (ethereum).](https://www.youtube.com/watch?v=KUl2p8MQGBg)**

BTC Conference 2026 - 'ALTCOINDAILY' for 10% off Ticket: https://2026.b.tc 50% deposit bonus on first $100 (sign up on ...

📺 Altcoin Daily

👁️ 26K • 👍 721 • 💬 23 • ⏱️ 1:16 • 2d ago

---

**[&quot;People Don’t Know How Massive MARCH Will Be for Crypto&quot;: Tom Lee | Ethereum Price 2026](https://www.youtube.com/watch?v=7oRNY59aeTo)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 3K • 👍 74 • 💬 6 • ⏱️ 19:52 • 2d ago

---

**[🔥 Bitcoin vs Ethereum vs XRP: HOLD or SELL Now?](https://www.youtube.com/watch?v=pni0OJ1fhIA)**

Course: https://coinlyte.com/crypto-crash-program/ ➡️ Best HardWare Wallet : https://coinlyte.com/tangem (Code : MRVYAS) ...

📺 Kirtish Vyas (CoinLyte)

👁️ 4K • 👍 164 • 💬 11 • ⏱️ 9:55 • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*
