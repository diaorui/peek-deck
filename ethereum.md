---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-14T21:44:50.303760+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- videos
- social
- news
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 14, 2026 at 21:44 UTC  
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

### $2,304.72

---

## Ethereum Chart

**24h:** +1.7%  
**7d:** -0.4%  
**30d:** -2.6%  
**90d:** +10.2%  
**1y:** -9.7%  

---

## Ethereum Market Stats

**Market Cap:** $277.46B
Rank #2

**Circulating Supply:** 120,686,173 ETH
No max supply

**All-Time High:** $4,946.05
-53.5%

**All-Time Low:** $0.43
+530711.0%

---

## Reddit: r/ethereum

**[Daily General Discussion May 14, 2026](https://www.reddit.com/r/ethereum/comments/1tco2pd/daily_general_discussion_may_14_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

16h ago

---

**[$770 million stolen in defi this year. 40+ protocols shut down. bridges are the common denominator and nobody is fixing the actual problem.](https://www.reddit.com/r/ethereum/comments/1tcu2m4/770_million_stolen_in_defi_this_year_40_protocols/)**

the numbers from 2026 so far are genuinely scary: kelp DAO: $293M drained through their layerzero bridge. single exploit hit 20+ chains because one bridge contract held the reserves for all of them drift protocol: $285M. north korean hackers spent 6 months social engineering their way in 1inch/trustedvolumes: $6.7M last week. same attacker from the 2025 hack came back and found a new door april 2026 alone: $600M+ stolen across 28-30 separate incidents. worst single month in crypto history 40+ protocols have shut down or entered wind-down mode this year. aave froze rsETH markets and lost $6 billion in TVL from panic withdrawals even though their contracts weren't touched. the pattern isn't random. bridges keep producing the biggest single-day losses because they're designed as massive honeypots. $22 billion in bridge TVL as of march, each one a single point of failure for every protocol downstream. what bugs me is the response is always the same. "we need better audits." "we need better monitoring." nobody is questioning whether the bridge model itself is fundamentally broken. bridges work by locking assets on one chain and minting representations on another through a trusted intermediary (multisig, oracle network, validator set). every one of these is an attack surface. kelp's bridge got spoofed because layerzero's messaging layer was fooled into thinking the withdrawal was legitimate. the alternative exists. data availability layers can handle cross-chain verification without lock-and-mint. instead of one contract holding $293M that can be drained in a single tx, you verify data availability cryptographically across chains. no honeypot, no single point of failure, no trusted intermediary to spoof. DA layers like avail, celestia, eigenda are live and production ready. the tech isn't theoretical anymore. it's an adoption problem not a research problem. at what point do we stop patching bridges and start replacing them?

11h ago

---

**[I cracked Vitalik’s 2015 on-chain ad platform. He was the only bidder. Total cost: $2.](https://www.reddit.com/r/ethereum/comments/1tbzzvi/i_cracked_vitaliks_2015_onchain_ad_platform_he/)**

Three months after mainnet launched, Vitalik deployed an advertising auction system to Ethereum. Eight ad slots, four auction mechanisms (one-phase winner-pays, cumulative, sealed-bid first-price, sealed-bid second-price), all managed by a factory contract called adStorer from ethereum/dapp-bin. I matched the deployed bytecode to source through compiler archaeology. Exact match, 8,752 bytes, solc v0.1.1. Then I decoded every transaction across all 8 child auction contracts. The only bidder was Vitalik himself. Two wallets (his old deployer and what’s now vitalik.eth), 229 transactions, 0.064 ETH in bids. The winning “advertisements” were two image URLs: me.jpg (a photo of himself) and heiko.jpg (a photo of Heiko Hees, who was building pyethereum). Both are 404 today. Some details: Slot 5 is a second-price sealed-bid auction. vitalik.eth bid 0.0005 ETH, his old wallet bid 0.0003 ETH. Second-price rules made vitalik.eth pay the runner-up’s price. The first Vickrey auction on Ethereum selected a photo of a pyethereum developer over its own creator. Gas cost more than the bids. Vitalik burned ~1 ETH on gas (at 60 gwei, hard-coded in his deploy script) to move 0.064 ETH through the auction mechanics. At October 2015 prices, the whole experiment cost about $2. Slot 1 was a stress test. 159 transactions, with Vitalik rebidding the same 0.0001 ETH increment 19 times in a row to validate cumulative bidding. Three of the four all-pay auction variants got zero bids. He abandoned the one he tried before revealing. Even Vitalik didn’t trust his own all-pay math. The sealed-bid auctions had a frontend bug where bid hashes were passed as ASCII hex instead of raw bytes, making commitments readable in calldata. Didn’t matter since the only participant wrote the code. 0.029 ETH (~$70 today, $0.03 in 2015) is still locked in the child contracts from unrevealed sealed bids. This was deployed three weeks before DevCon 1, on a network with maybe a few hundred users. A mechanism design experiment that nobody participated in except its creator, preserved on-chain for ten years. I checked the Wayback Machine for the ad images. The closest capture of vitalik.ca/files/ is from June 2016. Neither photo was archived. Full documentation with verified source, decoded bids, and all 8 slots mapped: https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e This is part of the EthereumHistory project where we’re documenting and verifying the earliest Ethereum contracts. If you want to help, the project is open.

🔗 [Ethereum History](https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e) • 1d ago

---

**[Why are banks and institutional funds actually interested in Ethereum?](https://www.reddit.com/r/ethereum/comments/1tcbpby/why_are_banks_and_institutional_funds_actually/)**

I get the basics of how Ethereum works, but I’m trying to understand the institutional side better. What do they actually want from it? And does their involvement change where Ethereum is headed, whether that’s decentralization, governance, or how the protocol develops? Genuinely curious what people who follow this space think.

1d ago

---

**[Upgrading Finality - Edition 1 | Protocol Consensus](https://www.reddit.com/r/ethereum/comments/1tcjd00/upgrading_finality_edition_1_protocol_consensus/)**

Turning consensus research into practice. We design, analyze, and formally verify consensus protocols for Ethereum.

🔗 [consensus.ethereum.foundation](https://consensus.ethereum.foundation/blog/upgrading-finality-edition-1) • 20h ago

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

**[Ethereum app builder Consensys has delayed its potential IPO until fall](https://www.coindesk.com/business/2026/05/13/ethereum-app-builder-consensys-has-delayed-its-potential-ipo-until-fall)**

The MetaMask wallet builder had reportedly engaged bankers from JPMorgan and Goldman Sachs to lead the process.

CoinDesk • 1d ago

---

**[Charles Schwab Begins Offering Bitcoin, Ethereum Trading to US Users](https://decrypt.co/367768/charles-schwab-begins-bitcoin-ethereum-trading-us-users)**

Charles Schwab started allowing select users to trade Bitcoin and Ethereum directly alongside their other investments.

Decrypt • 1d ago

---

**[Bitcoin and ethereum prices today, Thursday, May 14, 2026: Bitcoin and ethereum prices slipping this week](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-thursday-may-14-2026-bitcoin-and-ethereum-prices-slipping-this-week-111938059.html)**

Bitcoin opened at $79,283.34 on Thursday, down 1.5% from Wednesday's opening price. Ethereum opened at $2,257.71 on Thursday, down 0.7% from Wednesday’s opening value.

Yahoo Finance • 10h ago

---

**[Sharplink CEO says ETH treasury firms are diverging from Strategy model as Ethereum's tokenization role expands](https://www.theblock.co/post/401288/sharplink-ceo-says-eth-treasury-firms-are-diverging-from-strategy-model-as-ethereums-tokenization-role-expands)**

Joseph Chalom said growing institutional adoption of tokenization could strengthen Ethereum's role as infrastructure for onchain assets.

The Block • 4h ago

---

**[How Will the CLARITY Act May 14 Vote Impact Bitcoin, ETH and XRP?](https://www.disruptionbanking.com/2026/05/12/how-will-the-clarity-act-may-14-vote-impact-bitcoin-eth-and-xrp/)**

Disruption Banking • 2d ago

---

**[Clear Signing: Making Transaction Approvals Safer on Ethereum](https://blog.ethereum.org/2026/05/12/clear-signing-announcement)**

ethereum.org • 2d ago

---

**[Wall Street’s Stablecoin Darling Raises $222 Million to Starve Ethereum](https://gizmodo.com/wall-streets-stablecoin-darling-raises-222-million-to-starve-ethereum-2000757094)**

Gizmodo • 3d ago

---

**[Top 3 Price Prediction: Bitcoin, Ethereum, Ripple – BTC consolidates, ETH holds support, XRP eyes breakout](https://www.fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-consolidates-eth-holds-support-xrp-eyes-breakout-202605130342)**

Bitcoin (BTC), Ethereum (ETH), and Ripple (XRP) trade cautiously on Wednesday as price action approaches key technical levels across these top three cryptocurrencies. BTC stalls near the key resistance level around $82,000 while ETH holds firm above the key support at $2,275.

FXStreet • 1d ago

---

**[Prediction: Ethereum Will Be Worth $5,000 by 2030](https://www.fool.com/investing/2026/05/14/prediction-ethereum-will-be-worth-x-by-2030/)**

If Ethereum can grow at a steady 20% rate, it could reclaim its all-time high from 2025.

The Motley Fool • 11h ago

---

**[Blockchain.com rolls out crypto backed loans for Bitcoin, Ethereum, and USDC holders](https://cryptobriefing.com/crypto-backed-loans-by-blockchaincom/)**

Blockchain.com launched crypto backed loans globally with rates from 1.9%, letting users borrow against BTC, ETH, and USDC.

Crypto Briefing • 3h ago

---

---

## YouTube Videos: "ethereum"

**[&quot;Ethereum To $12,000,  Bitcoin To $250,000 - Here&#39;s WHY&quot; Tom Lee | Crypto Prediction 2026](https://www.youtube.com/watch?v=zQGTvz_2YM4)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 3K • 👍 159 • 💬 46 • ⏱️ 18:57 • 5h ago

---

**[🚨 BTC &amp; ETH: THIS IS BAD!!!](https://www.youtube.com/watch?v=0JR0z7vRGqM)**

This data is terrible for bitcoin, ethereum and the rest of crypto! WATCH OUT NOW!!!! ---------- Join My FREE Trading Group ...

📺 Thomas Kralow

👁️ 9K • 👍 2K • 💬 42 • ⏱️ 4:30 • 1d ago

---

**[Ethereum VS XRP – Which Is Better?](https://www.youtube.com/watch?v=AiaKtqyYLcA)**

Ethereum and Ripple are often compared, but they're solving completely different problems. One is a global app platform, the ...

📺 CoinGecko

👁️ 1K • 👍 104 • 💬 112 • ⏱️ 3:46 • 10h ago

---

**[Crypto Corner: Clarity Act Progress &amp; Blackrock Eyes Ethereum Network Fund](https://www.youtube.com/watch?v=ijvDw0bo58o)**

CharlesSchwab's Nathan Peterson offers his latest in-depth look into the price action of Bitcoin and developments surrounding the ...

📺 Schwab Network

👁️ 2K • 👍 42 • 💬 2 • ⏱️ 7:44 • 23h ago

---

**[MASSIVE Clarity Act Update! This Is a HUGE Win for Bitcoin &amp; Crypto - Tom Lee](https://www.youtube.com/watch?v=0tN78rPvgms)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 11K • 👍 303 • 💬 95 • ⏱️ 17:25 • 2d ago

---

**[XRP FLIPS BITCOIN AND ETHEREUM CLARITY THREATENS XRP SOLANA AND MORE! #xrp #crypto #bitcoin](https://www.youtube.com/watch?v=f_aFtTWDTB0)**

📺 CryptoWendyO

👁️ 13K • 👍 881 • 💬 52 • ⏱️ 2:13 • 20h ago

---

**[Why Ethereum is Stuck Under $2.4K](https://www.youtube.com/watch?v=8TUiX3l06XM)**

Ethereum keeps failing at the $2400 resistance level, and the data shows why: weak ETF inflows, falling leverage, and rising ETH ...

📺 Coin Bureau Podcast

👁️ 2K • 👍 46 • 💬 2 • ⏱️ 1:11 • 2d ago

---

**[BITCOIN &amp; ALTCOIN WARNING: Don&#39;t Be Fooled!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=2ds-AXVtzE8)**

BITCOIN & ALTCOIN WARNING: Don't Be Fooled!!! - Bitcoin News Today, Ethereum & Altcoins *Toobit* https://bit.ly/TOOBIT ...

📺 Crypto World

👁️ 7K • 👍 292 • 💬 149 • ⏱️ 19:06 • 18h ago

---

**[☠ Ethereum Story Is Breaking - ETH Crypto Analysis](https://www.youtube.com/watch?v=x2HEF-EuTkw)**

Join Premium: https://the-bitcoin-strategy.com Instagram: https://www.instagram.com/gerhard_bitcoin_strategy/ My Chart ...

📺 Gerhard - Bitcoin Strategy

👁️ 3K • 👍 87 • 💬 13 • ⏱️ 10:03 • 1d ago

---

**[Bitcoin &amp; Ethereum, kommt noch eine Erholung? Weiter kein Bruch von Support!](https://www.youtube.com/watch?v=YIFi5tZ2J58)**

DIE BESTE EXCHANGE AUF DEM KRYPTOMARKT!! OKX!! Das wird mein neuer Partner OKX! Nur bei mir bekommt ihr 20€ + ...

📺 Krypto Trading & Investing

👁️ 3K • 👍 478 • 💬 133 • ⏱️ 12:55 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*
