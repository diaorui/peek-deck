---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-14T18:17:38.473183+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- social
- videos
- cryptocurrency
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 14, 2026 at 18:17 UTC  
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

### $2,305.12

---

## Ethereum Chart

**24h:** +2.6%  
**7d:** +0.3%  
**30d:** -1.9%  
**90d:** +11.0%  
**1y:** -9.1%  

---

## Ethereum Market Stats

**Market Cap:** $278.40B
Rank #2

**Circulating Supply:** 120,686,173 ETH
No max supply

**All-Time High:** $4,946.05
-53.3%

**All-Time Low:** $0.43
+532900.4%

---

## Reddit: r/ethereum

**[Daily General Discussion May 14, 2026](https://www.reddit.com/r/ethereum/comments/1tco2pd/daily_general_discussion_may_14_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

13h ago

---

**[$770 million stolen in defi this year. 40+ protocols shut down. bridges are the common denominator and nobody is fixing the actual problem.](https://www.reddit.com/r/ethereum/comments/1tcu2m4/770_million_stolen_in_defi_this_year_40_protocols/)**

the numbers from 2026 so far are genuinely scary: kelp DAO: $293M drained through their layerzero bridge. single exploit hit 20+ chains because one bridge contract held the reserves for all of them drift protocol: $285M. north korean hackers spent 6 months social engineering their way in 1inch/trustedvolumes: $6.7M last week. same attacker from the 2025 hack came back and found a new door april 2026 alone: $600M+ stolen across 28-30 separate incidents. worst single month in crypto history 40+ protocols have shut down or entered wind-down mode this year. aave froze rsETH markets and lost $6 billion in TVL from panic withdrawals even though their contracts weren't touched. the pattern isn't random. bridges keep producing the biggest single-day losses because they're designed as massive honeypots. $22 billion in bridge TVL as of march, each one a single point of failure for every protocol downstream. what bugs me is the response is always the same. "we need better audits." "we need better monitoring." nobody is questioning whether the bridge model itself is fundamentally broken. bridges work by locking assets on one chain and minting representations on another through a trusted intermediary (multisig, oracle network, validator set). every one of these is an attack surface. kelp's bridge got spoofed because layerzero's messaging layer was fooled into thinking the withdrawal was legitimate. the alternative exists. data availability layers can handle cross-chain verification without lock-and-mint. instead of one contract holding $293M that can be drained in a single tx, you verify data availability cryptographically across chains. no honeypot, no single point of failure, no trusted intermediary to spoof. DA layers like avail, celestia, eigenda are live and production ready. the tech isn't theoretical anymore. it's an adoption problem not a research problem. at what point do we stop patching bridges and start replacing them?

7h ago

---

**[I cracked Vitalik’s 2015 on-chain ad platform. He was the only bidder. Total cost: $2.](https://www.reddit.com/r/ethereum/comments/1tbzzvi/i_cracked_vitaliks_2015_onchain_ad_platform_he/)**

Three months after mainnet launched, Vitalik deployed an advertising auction system to Ethereum. Eight ad slots, four auction mechanisms (one-phase winner-pays, cumulative, sealed-bid first-price, sealed-bid second-price), all managed by a factory contract called adStorer from ethereum/dapp-bin. I matched the deployed bytecode to source through compiler archaeology. Exact match, 8,752 bytes, solc v0.1.1. Then I decoded every transaction across all 8 child auction contracts. The only bidder was Vitalik himself. Two wallets (his old deployer and what’s now vitalik.eth), 229 transactions, 0.064 ETH in bids. The winning “advertisements” were two image URLs: me.jpg (a photo of himself) and heiko.jpg (a photo of Heiko Hees, who was building pyethereum). Both are 404 today. Some details: Slot 5 is a second-price sealed-bid auction. vitalik.eth bid 0.0005 ETH, his old wallet bid 0.0003 ETH. Second-price rules made vitalik.eth pay the runner-up’s price. The first Vickrey auction on Ethereum selected a photo of a pyethereum developer over its own creator. Gas cost more than the bids. Vitalik burned ~1 ETH on gas (at 60 gwei, hard-coded in his deploy script) to move 0.064 ETH through the auction mechanics. At October 2015 prices, the whole experiment cost about $2. Slot 1 was a stress test. 159 transactions, with Vitalik rebidding the same 0.0001 ETH increment 19 times in a row to validate cumulative bidding. Three of the four all-pay auction variants got zero bids. He abandoned the one he tried before revealing. Even Vitalik didn’t trust his own all-pay math. The sealed-bid auctions had a frontend bug where bid hashes were passed as ASCII hex instead of raw bytes, making commitments readable in calldata. Didn’t matter since the only participant wrote the code. 0.029 ETH (~$70 today, $0.03 in 2015) is still locked in the child contracts from unrevealed sealed bids. This was deployed three weeks before DevCon 1, on a network with maybe a few hundred users. A mechanism design experiment that nobody participated in except its creator, preserved on-chain for ten years. I checked the Wayback Machine for the ad images. The closest capture of vitalik.ca/files/ is from June 2016. Neither photo was archived. Full documentation with verified source, decoded bids, and all 8 slots mapped: https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e This is part of the EthereumHistory project where we’re documenting and verifying the earliest Ethereum contracts. If you want to help, the project is open.

🔗 [Ethereum History](https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e) • 1d ago

---

**[Why are banks and institutional funds actually interested in Ethereum?](https://www.reddit.com/r/ethereum/comments/1tcbpby/why_are_banks_and_institutional_funds_actually/)**

I get the basics of how Ethereum works, but I’m trying to understand the institutional side better. What do they actually want from it? And does their involvement change where Ethereum is headed, whether that’s decentralization, governance, or how the protocol develops? Genuinely curious what people who follow this space think.

21h ago

---

**[Upgrading Finality - Edition 1 | Protocol Consensus](https://www.reddit.com/r/ethereum/comments/1tcjd00/upgrading_finality_edition_1_protocol_consensus/)**

Turning consensus research into practice. We design, analyze, and formally verify consensus protocols for Ethereum.

🔗 [consensus.ethereum.foundation](https://consensus.ethereum.foundation/blog/upgrading-finality-edition-1) • 16h ago

---

**[Every time I try to move money between my bank and crypto I feel like a criminal even though I've done nothing wrong](https://www.reddit.com/r/ethereum/comments/1tc5b1e/every_time_i_try_to_move_money_between_my_bank/)**

My bank has flagged two of my transfers to a crypto exchange in the last three months. First time they put the money on hold for 48 hours. Second time someone from their fraud team called me to ask what I was buying and why. I answered everything honestly and they released the funds but the whole interaction felt accusatory. I'm not doing anything illegal, I'm just buying some ETH. Has anyone found a way to make this less terrible

1d ago

---

**[Aztec Foundation contributes 1% of AZTEC token supply toward supporting Ethereum Core Development via Protocol Guild](https://www.reddit.com/r/ethereum/comments/1tc65xb/aztec_foundation_contributes_1_of_aztec_token/)**

🔗 [X (formerly Twitter)](https://x.com/ProtocolGuild/status/2054190784061091896?s=20) • 1d ago

---

**[Daily General Discussion May 13, 2026](https://www.reddit.com/r/ethereum/comments/1tbpq6u/daily_general_discussion_may_13_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Grayscale weighs in on Ethereum issuance](https://www.reddit.com/r/ethereum/comments/1tbndv4/grayscale_weighs_in_on_ethereum_issuance/)**

🔗 [grayscale.com](https://www.grayscale.com/the-stack/ethereums-staking-model-needs-an-update) • 1d ago

---

**[Ethereum impact from Chainlink deal launching Collateral AppChain platform](https://www.reddit.com/r/ethereum/comments/1tbioxg/ethereum_impact_from_chainlink_deal_launching/)**

The DTCC and Chainlink partnership directly benefits Ethereum by establishing its enterprise-grade client, Besu, as the foundational infrastructure for a major global post-trade system. The Collateral AppChain is built on Hyperledger Besu, an Ethereum-compatible network, which validates Ethereum’s technical standards for institutional use and drives demand for enterprise blockchain solutions. This integration significantly boosts the utility and credibility of Chainlink’s oracle services within traditional finance. By utilizing Chainlink’s Runtime Environment (CRE) and data standards to automate pricing, margining, and settlement, the deal demonstrates that decentralized oracles can securely manage critical financial workflows. This positions Chainlink as a default infrastructure layer for tokenized real-world assets (RWA), potentially increasing its usage across other financial institutions following DTCC’s October 2026 launch. For the broader financial ecosystem, the partnership accelerates the tokenization of assets on blockchain rails. It enables 24/7 near real-time collateral management, moving away from legacy T+1 or T+2 settlement times to instant, smart-contract-verified transactions. This efficiency improves capital utilization for institutions and sets a precedent for other clearinghouses to adopt similar Ethereum-based and Chainlink-powered infrastructures.

1d ago

---

---

## Google News: "ethereum"

**[Charles Schwab Begins Offering Bitcoin, Ethereum Trading to US Users](https://decrypt.co/367768/charles-schwab-begins-bitcoin-ethereum-trading-us-users)**

Charles Schwab started allowing select users to trade Bitcoin and Ethereum directly alongside their other investments.

Decrypt • 1d ago

---

**[Protocol Cluster Updates: May 2026](https://blog.ethereum.org/2026/05/11/protocol-update-may-26)**

ethereum.org • 3d ago

---

**[Bitcoin, Ethereum, XRP Fall, But Dogecoin Gains Ahead Of Crypto Act Markup In Senate: This Analyst Is Bracing For More BTC Pain Ahead](https://finance.yahoo.com/markets/crypto/articles/bitcoin-ethereum-xrp-fall-dogecoin-014834273.html)**

Leading cryptocurrencies slipped on Wednesday as the Senate Banking Committee gears up to vote on the Clarity Act. Cryptocurrency24-Hour Gains +/-Price (Recorded at 9:20 p.m. EDT)Bitcoin (CRYPTO: BTC)-1.77%$79,580.06Ethereum (CRYPTO: ETH) -1.16%$2,264.35XRP (CRYPTO: XRP) -1.00%$1.43Solana (CRYPTO: SOL) -4.11%$91.14Dogecoin (CRYPTO: DOGE) +2.91%$0.1145 Crypto Market Lags Bitcoin dipped below $79,000 during early trading but staged a partial recovery by late evening. Ethereum fell to an intraday l

Yahoo Finance • 16h ago

---

**[JPMorgan launching second tokenized money market fund on Ethereum](https://www.theblock.co/post/401028/jpmorgan-launching-tokenized-money-market-fund-ethereum)**

The new fund will invest in U.S. Treasurys and overnight repurchase agreements collateralized by Treasurys or cash.

The Block • 1d ago

---

**[JPMorgan Launching Second Tokenized Money Market Fund on Ethereum — Bullish For ETH Price?](https://finance.yahoo.com/news/jpmorgan-launching-second-tokenized-money-100215730.html)**

JPMorgan has filed for a second tokenized money market fund on Ethereum. The proposed JLTXX fund would tokenize Treasury-backed assets on Ethereum. Some analysts and ...

Yahoo Finance • 1d ago

---

**[JPMorgan Files to Launch Tokenized Money Market Fund on Ethereum](https://decrypt.co/367664/jpmorgan-tokenized-money-market-fund-ethereum)**

Global banking giant JPMorgan filed for a new tokenized money market fund that will initially run on the Ethereum network.

Decrypt • 1d ago

---

**[Ethereum app builder Consensys has delayed its potential IPO until fall](https://www.coindesk.com/business/2026/05/13/ethereum-app-builder-consensys-has-delayed-its-potential-ipo-until-fall)**

The MetaMask wallet builder had reportedly engaged bankers from JPMorgan and Goldman Sachs to lead the process.

CoinDesk • 23h ago

---

**[How Will the CLARITY Act May 14 Vote Impact Bitcoin, ETH and XRP?](https://www.disruptionbanking.com/2026/05/12/how-will-the-clarity-act-may-14-vote-impact-bitcoin-eth-and-xrp/)**

Disruption Banking • 2d ago

---

**[Wall Street’s Stablecoin Darling Raises $222 Million to Starve Ethereum](https://gizmodo.com/wall-streets-stablecoin-darling-raises-222-million-to-starve-ethereum-2000757094)**

Gizmodo • 3d ago

---

**[Current price of Ethereum for May 14, 2026](https://fortune.com/article/price-of-ethereum-05-14-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 5h ago

---

---

## YouTube Videos: "ethereum"

**[🚨 BTC &amp; ETH: THIS IS BAD!!!](https://www.youtube.com/watch?v=0JR0z7vRGqM)**

This data is terrible for bitcoin, ethereum and the rest of crypto! WATCH OUT NOW!!!! ---------- Join My FREE Trading Group ...

📺 Thomas Kralow

👁️ 8K • 👍 2K • 💬 59 • ⏱️ 4:30 • 1d ago

---

**[Crypto Corner: Clarity Act Progress &amp; Blackrock Eyes Ethereum Network Fund](https://www.youtube.com/watch?v=ijvDw0bo58o)**

CharlesSchwab's Nathan Peterson offers his latest in-depth look into the price action of Bitcoin and developments surrounding the ...

📺 Schwab Network

👁️ 2K • 👍 37 • 💬 2 • ⏱️ 7:44 • 20h ago

---

**[MASSIVE Clarity Act Update! This Is a HUGE Win for Bitcoin &amp; Crypto - Tom Lee](https://www.youtube.com/watch?v=0tN78rPvgms)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 10K • 👍 281 • 💬 104 • ⏱️ 17:25 • 1d ago

---

**[Ethereum VS XRP – Which Is Better?](https://www.youtube.com/watch?v=AiaKtqyYLcA)**

Ethereum and Ripple are often compared, but they're solving completely different problems. One is a global app platform, the ...

📺 CoinGecko

👁️ 729 • 👍 90 • 💬 62 • ⏱️ 3:46 • 7h ago

---

**[XRP FLIPS BITCOIN AND ETHEREUM CLARITY THREATENS XRP SOLANA AND MORE! #xrp #crypto #bitcoin](https://www.youtube.com/watch?v=f_aFtTWDTB0)**

📺 CryptoWendyO

👁️ 12K • 👍 843 • 💬 51 • ⏱️ 2:13 • 17h ago

---

**[Live Crypto Trading | Bitcoin, Ethereum, Altcoin Scalping &amp; Analysis in Real-Time](https://www.youtube.com/watch?v=MUmDs_a7OVQ)**

Open Crypto Trading Account ➡️ https://india.delta.exchange/?code=stockburner Get Free access on - Crypto Trading Club ...

📺 Trade with Burner

👁️ 5K • 👍 253 • 💬 1 • ⏱️ 46:45 • 2h ago

---

**[☠ Ethereum Story Is Breaking - ETH Crypto Analysis](https://www.youtube.com/watch?v=x2HEF-EuTkw)**

Join Premium: https://the-bitcoin-strategy.com Instagram: https://www.instagram.com/gerhard_bitcoin_strategy/ My Chart ...

📺 Gerhard - Bitcoin Strategy

👁️ 2K • 👍 87 • 💬 13 • ⏱️ 10:03 • 1d ago

---

**[WHY ETHEREUM COULD DUMP!🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=UuSsvgaMEgM)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 164 • 👍 14 • 💬 1 • ⏱️ 4:45 • 8h ago

---

**[BITCOIN &amp; ALTCOIN WARNING: Don&#39;t Be Fooled!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=2ds-AXVtzE8)**

BITCOIN & ALTCOIN WARNING: Don't Be Fooled!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* https://bit.ly/TOOBIT ...

📺 Crypto World

👁️ 7K • 👍 289 • 💬 82 • ⏱️ 19:06 • 15h ago

---

**[Ethereum&#39;s Next Move Could Trigger Final Crash](https://www.youtube.com/watch?v=Weg4uuozGiU)**

Join Trade Confident: Get 25% Off Your 1st Month: https://tinyurl.com/tcmembergift • Weekly Market Forecasts • Monthly Zoom Call ...

📺 Trade Confident

👁️ 278 • 👍 8 • 💬 1 • ⏱️ 5:10 • 22h ago

---

---

*Generated by PeekDeck - A glance is all you need*
