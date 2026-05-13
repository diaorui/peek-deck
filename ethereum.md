---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-05-13T19:56:17.409296+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- videos
- news
- cryptocurrency
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** May 13, 2026 at 19:56 UTC  
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

### $2,260.69

---

## Ethereum Chart

**24h:** -1.3%  
**7d:** -1.6%  
**30d:** -2.9%  
**90d:** +10.1%  
**1y:** -13.7%  

---

## Ethereum Market Stats

**Market Cap:** $272.11B
Rank #2

**Circulating Supply:** 120,686,235 ETH
No max supply

**All-Time High:** $4,946.05
-54.4%

**All-Time Low:** $0.43
+520615.8%

---

## Reddit: r/ethereum

**[I cracked Vitalik’s 2015 on-chain ad platform. He was the only bidder. Total cost: $2.](https://www.reddit.com/r/ethereum/comments/1tbzzvi/i_cracked_vitaliks_2015_onchain_ad_platform_he/)**

Three months after mainnet launched, Vitalik deployed an advertising auction system to Ethereum. Eight ad slots, four auction mechanisms (one-phase winner-pays, cumulative, sealed-bid first-price, sealed-bid second-price), all managed by a factory contract called adStorer from ethereum/dapp-bin. I matched the deployed bytecode to source through compiler archaeology. Exact match, 8,752 bytes, solc v0.1.1. Then I decoded every transaction across all 8 child auction contracts. The only bidder was Vitalik himself. Two wallets (his old deployer and what’s now vitalik.eth), 229 transactions, 0.064 ETH in bids. The winning “advertisements” were two image URLs: me.jpg (a photo of himself) and heiko.jpg (a photo of Heiko Hees, who was building pyethereum). Both are 404 today. Some details: Slot 5 is a second-price sealed-bid auction. vitalik.eth bid 0.0005 ETH, his old wallet bid 0.0003 ETH. Second-price rules made vitalik.eth pay the runner-up’s price. The first Vickrey auction on Ethereum selected a photo of a pyethereum developer over its own creator. Gas cost more than the bids. Vitalik burned ~1 ETH on gas (at 60 gwei, hard-coded in his deploy script) to move 0.064 ETH through the auction mechanics. At October 2015 prices, the whole experiment cost about $2. Slot 1 was a stress test. 159 transactions, with Vitalik rebidding the same 0.0001 ETH increment 19 times in a row to validate cumulative bidding. Three of the four all-pay auction variants got zero bids. He abandoned the one he tried before revealing. Even Vitalik didn’t trust his own all-pay math. The sealed-bid auctions had a frontend bug where bid hashes were passed as ASCII hex instead of raw bytes, making commitments readable in calldata. Didn’t matter since the only participant wrote the code. 0.029 ETH (~$70 today, $0.03 in 2015) is still locked in the child contracts from unrevealed sealed bids. This was deployed three weeks before DevCon 1, on a network with maybe a few hundred users. A mechanism design experiment that nobody participated in except its creator, preserved on-chain for ten years. I checked the Wayback Machine for the ad images. The closest capture of vitalik.ca/files/ is from June 2016. Neither photo was archived. Full documentation with verified source, decoded bids, and all 8 slots mapped: https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e This is part of the EthereumHistory project where we’re documenting and verifying the earliest Ethereum contracts. If you want to help, the project is open.

🔗 [Ethereum History](https://ethereumhistory.com/contract/0xaf0334bf30c401b7e3afafbac1dbcdc712be8b9e) • 6h ago

---

**[Daily General Discussion May 13, 2026](https://www.reddit.com/r/ethereum/comments/1tbpq6u/daily_general_discussion_may_13_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

14h ago

---

**[Every time I try to move money between my bank and crypto I feel like a criminal even though I've done nothing wrong](https://www.reddit.com/r/ethereum/comments/1tc5b1e/every_time_i_try_to_move_money_between_my_bank/)**

My bank has flagged two of my transfers to a crypto exchange in the last three months. First time they put the money on hold for 48 hours. Second time someone from their fraud team called me to ask what I was buying and why. I answered everything honestly and they released the funds but the whole interaction felt accusatory. I'm not doing anything illegal, I'm just buying some ETH. Has anyone found a way to make this less terrible

3h ago

---

**[Aztec Foundation contributes 1% of AZTEC token supply toward supporting Ethereum Core Development via Protocol Guild](https://www.reddit.com/r/ethereum/comments/1tc65xb/aztec_foundation_contributes_1_of_aztec_token/)**

🔗 [X (formerly Twitter)](https://x.com/ProtocolGuild/status/2054190784061091896?s=20) • 2h ago

---

**[Grayscale weighs in on Ethereum issuance](https://www.reddit.com/r/ethereum/comments/1tbndv4/grayscale_weighs_in_on_ethereum_issuance/)**

🔗 [grayscale.com](https://www.grayscale.com/the-stack/ethereums-staking-model-needs-an-update) • 16h ago

---

**[Ethereum impact from Chainlink deal launching Collateral AppChain platform](https://www.reddit.com/r/ethereum/comments/1tbioxg/ethereum_impact_from_chainlink_deal_launching/)**

The DTCC and Chainlink partnership directly benefits Ethereum by establishing its enterprise-grade client, Besu, as the foundational infrastructure for a major global post-trade system. The Collateral AppChain is built on Hyperledger Besu, an Ethereum-compatible network, which validates Ethereum’s technical standards for institutional use and drives demand for enterprise blockchain solutions. This integration significantly boosts the utility and credibility of Chainlink’s oracle services within traditional finance. By utilizing Chainlink’s Runtime Environment (CRE) and data standards to automate pricing, margining, and settlement, the deal demonstrates that decentralized oracles can securely manage critical financial workflows. This positions Chainlink as a default infrastructure layer for tokenized real-world assets (RWA), potentially increasing its usage across other financial institutions following DTCC’s October 2026 launch. For the broader financial ecosystem, the partnership accelerates the tokenization of assets on blockchain rails. It enables 24/7 near real-time collateral management, moving away from legacy T+1 or T+2 settlement times to instant, smart-contract-verified transactions. This efficiency improves capital utilization for institutions and sets a precedent for other clearinghouses to adopt similar Ethereum-based and Chainlink-powered infrastructures.

20h ago

---

**[Clear Signing | See What You Sign](https://www.reddit.com/r/ethereum/comments/1tb6ku5/clear_signing_see_what_you_sign/)**

The open standard for human-readable transaction signing.

🔗 [Clear Signing](https://clearsigning.org/) • 1d ago

---

**[Daily General Discussion May 12, 2026](https://www.reddit.com/r/ethereum/comments/1tariy9/daily_general_discussion_may_12_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[$14 Trillion BlackRock Picks Ethereum for Tokenized Funds](https://www.reddit.com/r/ethereum/comments/1tahzx0/14_trillion_blackrock_picks_ethereum_for/)**

BlackRock filed for tokenized money-market fund shares on Ethereum, adding pressure to the chain race for real-world asset settlement.

🔗 [Daily Crypto Briefs](https://dailycryptobriefs.com/news/blackrock-picks-ethereum-tokenized-funds/) • 1d ago

---

**[Protocol Cluster Updates: May 2026](https://www.reddit.com/r/ethereum/comments/1taex6u/protocol_cluster_updates_may_2026/)**

🔗 [Ethereum Foundation Blog](https://blog.ethereum.org/2026/05/11/protocol-update-may-26) • 1d ago

---

---

## Google News: "ethereum"

**[Ethereum closes gap with Solana as DEX volumes converge near $45 billion](https://www.theblock.co/post/400806/ethereum-closes-gap-solana-dex-volumes-converge-45-billion)**

The current near-parity gives both chains another chance to position themselves to capture volume when onchain activity rotates back.

The Block • 6h ago

---

**[JPMorgan Files to Launch Tokenized Money Market Fund on Ethereum](https://decrypt.co/367664/jpmorgan-tokenized-money-market-fund-ethereum)**

Global banking giant JPMorgan filed for a new tokenized money market fund that will initially run on the Ethereum network.

Decrypt • 22h ago

---

**[Bitcoin, Ethereum, XRP Wobble As Markets Await Clarity Act Markup, Dogecoin Extends Rally](https://finance.yahoo.com/news/bitcoin-ethereum-xrp-wobble-markets-190118320.html)**

Bitcoin slipped below $80,000 on Wednesday as crypto markets turned cautious ahead of Thursday's highly anticipated U.S. Senate Banking Committee markup meeting on the Clarity Act. CryptocurrencyTickerPriceBitcoin(CRYPTO: BTC)$79,611Ethereum(CRYPTO: ETH)$2,258.88Solana(CRYPTO: SOL)$90.92XRP(CRYPTO: XRP)$1.42Dogecoin(CRYPTO: DOGE)$0.1132Shiba Inu(CRYPTO: SHIB)$0.056293 Notable Statistics: Coinglass data shows 120,108 traders were liquidated in the past 24 hours for $374.66 million. SoSoValue data

Yahoo Finance • 54m ago

---

**[Ethereum app builder Consensys has delayed its potential IPO until fall](https://www.coindesk.com/business/2026/05/13/ethereum-app-builder-consensys-has-delayed-its-potential-ipo-until-fall)**

The MetaMask wallet builder had reportedly engaged bankers from JPMorgan and Goldman Sachs to lead the process.

CoinDesk • 49m ago

---

**[Clear Signing: Making Transaction Approvals Safer on Ethereum](https://blog.ethereum.org/2026/05/12/clear-signing-announcement)**

ethereum.org • 1d ago

---

**[How Will the CLARITY Act May 14 Vote Impact Bitcoin, ETH and XRP?](https://www.disruptionbanking.com/2026/05/12/how-will-the-clarity-act-may-14-vote-impact-bitcoin-eth-and-xrp/)**

Disruption Banking • 1d ago

---

**[Bitcoin, Ethereum and XRP Price Analysis: What’s Coming Next?](https://coinpedia.org/news/bitcoin-ethereum-and-xrp-price-analysis-whats-coming-next/)**

Coinpedia • 5h ago

---

**[Novogratz’s Galaxy And Ethereum Treasury Company Sharplink To Launch $125 Million DeFi Fund](https://www.forbes.com/sites/ninabambysheva/2026/05/11/novogratzs-galaxy-and-ethereum-treasury-company-sharplink-to-launch-125-million-defi-fund/)**

Galaxy will manage the private fund, seeded with $100 million from Sharplink’s ether treasury and $25 million of its own capital, bringing fresh liquidity to a bruised DeFi sector.

Forbes • 2d ago

---

**[Current price of Ethereum for May 13, 2026](https://fortune.com/article/price-of-ethereum-05-13-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 6h ago

---

**[‘Positive for ETH price’ – Grayscale backs Ethereum staking reward cap](https://ambcrypto.com/positive-for-eth-price-grayscale-backs-ethereum-staking-reward-cap/)**

AMBCrypto • 3h ago

---

---

## YouTube Videos: "ethereum"

**[🚨 BTC &amp; ETH: THIS IS BAD!!!](https://www.youtube.com/watch?v=0JR0z7vRGqM)**

This data is terrible for bitcoin, ethereum and the rest of crypto! WATCH OUT NOW!!!! ---------- Join My FREE Trading Group ...

📺 Thomas Kralow

👁️ 3K • 👍 2K • 💬 22 • ⏱️ 4:30 • 3h ago

---

**[☠ Ethereum Story Is Breaking - ETH Crypto Analysis](https://www.youtube.com/watch?v=x2HEF-EuTkw)**

Join Premium: https://the-bitcoin-strategy.com Instagram: https://www.instagram.com/gerhard_bitcoin_strategy/ My Chart ...

📺 Gerhard - Bitcoin Strategy

👁️ 1K • 👍 59 • 💬 36 • ⏱️ 10:03 • 7h ago

---

**[MASSIVE Clarity Act Update! This Is a HUGE Win for Bitcoin &amp; Crypto - Tom Lee](https://www.youtube.com/watch?v=0tN78rPvgms)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 8K • 👍 245 • 💬 108 • ⏱️ 17:25 • 1d ago

---

**[Ethereum&#39;s Next Move Could Trigger Final Crash](https://www.youtube.com/watch?v=Weg4uuozGiU)**

Get $450 Off Our New AI Indicators: https://tradeconfidentportal.io/indicators Join Trade Confident: Get 25% Off Your 1st Month: ...

📺 Trade Confident

👁️ 48 • 👍 1 • 💬 1 • ⏱️ 5:10 • 25m ago

---

**[ELIZABETH WARREN FIGHTS CLARITY ACT! JPMORGAN TOKENIZATION ETHEREUM &amp; BERMUDA STELLAR XLM!](https://www.youtube.com/watch?v=s-I_zD6SBTA)**

Crypto News: Elizabeth Warren pushes back on Clarity Act draft bill. JPMorgan launching second tokenized money market fund ...

📺 Thinking Crypto

👁️ 10K • 👍 688 • 💬 383 • ⏱️ 20:45 • 15h ago

---

**[BITCOIN: This Move Was a BRUTAL Trap! (here’s why) - BTC, ETH Price Prediction Today](https://www.youtube.com/watch?v=Z6xK8hoMBTM)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 7K • 👍 488 • 💬 185 • ⏱️ 15:09 • 9h ago

---

**[ETH Deep Dive (bullish and bearish projections)](https://www.youtube.com/watch?v=S1e5MeaFoSg)**

Ethereum has been lagging badly behind Bitcoin, and in this video Aaron breaks down why ETH still looks weaker even after its ...

📺 Coin Bureau Trading

👁️ 5K • 👍 305 • 💬 30 • ⏱️ 23:49 • 1d ago

---

**[Why Crypto May Be Entering a New Bull Market](https://www.youtube.com/watch?v=HZ6b_i9Ce3U)**

Tom Lee breaks down why Ethereum, Bitcoin, tokenization, and AI could drive the next major crypto bull market. From Ethereum's ...

📺 Cointelegraph

👁️ 5K • 👍 150 • 💬 14 • ⏱️ 9:08 • 2d ago

---

**[Dumping BTC for AI?! 🤯 Agentic ETH, Massive Flows  &amp; Levge +  AI Masterplan! 🚀](https://www.youtube.com/watch?v=ZI4eRwNmSqA)**

JOIN THE FAMILY: http://www.patreon.com/investanswers IA MODELS: https://investanswers.io/indicators 🏖️ IA ...

📺 InvestAnswers

👁️ 32K • 💬 94 • ⏱️ 19:51 • 22h ago

---

**[Why Ethereum is Stuck Under $2.4K](https://www.youtube.com/watch?v=8TUiX3l06XM)**

Ethereum keeps failing at the $2400 resistance level, and the data shows why: weak ETF inflows, falling leverage, and rising ETH ...

📺 Coin Bureau Podcast

👁️ 2K • 👍 41 • 💬 2 • ⏱️ 1:11 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
