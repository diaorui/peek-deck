---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-01-26T12:52:03.823475+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- news
- cryptocurrency
- videos
- social
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** January 26, 2026 at 12:52 UTC  
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

### $2,910.35

---

## Ethereum Chart

**24h:** -1.4%  
**7d:** -1.3%  
**30d:** -1.7%  
**90d:** -25.7%  
**1y:** -8.7%  

---

## Ethereum Market Stats

**Market Cap:** $348.77B
Rank #2

**Circulating Supply:** 120,694,419 ETH
No max supply

**All-Time High:** $4,946.05
-41.5%

**All-Time Low:** $0.43
+667620.6%

---

## Reddit: r/ethereum

**[Daily General Discussion January 26, 2026](https://www.reddit.com/r/ethereum/comments/1qn7wd5/daily_general_discussion_january_26_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

6h ago

---

**[Revisiting the Mountain Man](https://www.reddit.com/r/ethereum/comments/1qn2871/revisiting_the_mountain_man/)**

I no longer agree with this previous tweet of mine - since 2017, I have become a much more willing connoisseur of mountains. It's worth explaining why. https://x.com/VitalikButerin/status/873177382164848641 First, the original context. That tweet was in a debate with Ian Grigg, who argued that blockchains should track the order of transactions, but not the state (eg. user balances, smart contract code and storage): The messages are logged, but the state (e.g., UTXO) is implied, which means it is constructed by the computer internally, and then (can be) thrown away. I was heavily against this philosophy, because it would imply that users have no way to get the state other than either (i) running a node that processed every transaction in all of history, or (ii) trusting someone else. In blockchains that commit to the state in the block header (like Ethereum), you can simply prove any value in the state with a Merkle branch. This is conditional on the honest majority assumption: if >= 50% of the consensus participants are honest, then the chain with the most PoW (or PoS) support will be valid, and so the state root will be correct. Trusting an honest majority is far better than trusting a single RPC provider. Not trusting at all (by personally verifying every transaction in the chain) is theoretically ideal, but it's a computation load infeasible for regular users, unless we take the (even worse) tradeoff of keeping blockchain capacity so low that most people cannot even use the chain. Now, what has changed since then? The biggest thing is of course ZK-SNARKs. We now have a technology that lets you verify the correctness of the chain, without literally re-executing every transaction. WE INVENTED THE THING THAT GETS YOU THE BENEFITS WITHOUT THE COSTS! This is like if someone from the future teleported back into US healthcare debates in 2008, and demonstrated a clearly working pill that anyone could make for $15 that cured all diseases. Like, yes, if we have that pill, we should get the government fully out of healthcare, let people make the pill and sell it at Walgreens, and healthcare becomes super affordable so everyone is happy. ZK-SNARKs are literally like that but for the block size war. (With two asterisks for block building centralization and data bandwidth, but that's a separate topic) With better technology, we should raise our expectations, and revisit tradeoffs that we made grudgingly in a previous era. But also, I have actually changed my mind on some of the underlying issues. In 2017, I was thinking about blockchains in terms of academic assumptions - what is okay to rely on honest majority for, when we are ok with 1-of-N trust assumption, etc. If a construction gave better properties under known-acceptable assumptions, I would eagerly embrace it. On a raw subconscious level, I don't think I was sufficiently appreciative of the fact that in the real world, lots of things break. Sometimes the p2p network goes down. Sometimes the p2p network has 20x the latency you expected - anyone who has played WoW can attest to long spans of time when the latency spiked up from its usual ~200ms to 1000-5000ms. Sometimes a third party service you've been relying on for years shuts down, and there isn't a good alternative. If the alternative is that you personally go through a github repo and figure out how to PERSONALLY RUN A SERVER, lots of people will give up and never figure it out and end up permanently losing access to their money. Sometimes mining or staking gets concentrated to the point where 51% attacks are very easy to imagine, and you almost have to game-theoretically analyze consensus security as though 75% of miners or stakers are controlled by one single agent. Sometimes, as we saw with tornado cash, intermediaries all start censoring some application, and your only option becomes to directly use the chain. If we are making a self-sovereign blockchain to last through the ages, THE ANSWER TO THE ABOVE CONUNDRUMS CANNOT ALWAYS BE "CALL THE DEVS". If it is, the devs themselves become the point of centralization - they become DEVS in the ancient Roman sense, where the letter V was used to represent the U sound. The Mountain Man's cabin is not meant as the replacement lifestyle for everyone. It is meant as the safe place to retreat to when things go wrong. It is also meant as the universal BATNA ("Best Alternative to a Negotiated Agreement") - the alternative option that improves your well-being not just in the case when you end up needing it, but also because knowledge of it existing motivates third parties to give you better terms. This is like how Bittorrent existing is an important check on the power of music and video streaming platforms, driving them to offer customers better terms. We do not need to start living every day in the Mountain Man's cabin. But part of maintaining the infinite garden of Ethereum is certainly keeping the cabin well-maintained.

11h ago

---

**[US Spot ETH ETFs recorded $1.5B in net outflows in Q4 2025, the single highest quarter of net outflows for the sector.](https://www.reddit.com/r/ethereum/comments/1qnblvo/us_spot_eth_etfs_recorded_15b_in_net_outflows_in/)**

Despite net outflows and a decline in ETH’s price, ETH ETFs have still had a strong year, posting 48.2% YoY growth. ETHA retains its commanding lead with 57.4% share of assets under management (AUM), followed by ETHE at 14.6%, Fidelity’s FETH at 12.3%, and ETH at 12.3%. Source: https://www.coingecko.com/research/publications/2025-annual-crypto-report

3h ago

---

**[How to exchange ETH to XMR without KYC?](https://www.reddit.com/r/ethereum/comments/1qndzqt/how_to_exchange_eth_to_xmr_without_kyc/)**

Hey, I have been holding some ETH for a while and I am looking to swap part of it into XMR. I would rather avoid big centralized exchanges if possible. Privacy matters to me and I like keeping control of my own funds. I have looked at a few decentralized or peer to peer options, but it is hard to know which ones are actually reliable or have enough liquidity. Mostly looking for something that is smooth to use and does not involve heavy KYC. Thanks in advance.

59m ago

---

**[Ledger Wallet - Ethereum Kiln Staking And/Or Other Ethereum Staking Service Recommendations](https://www.reddit.com/r/ethereum/comments/1qn6e9w/ledger_wallet_ethereum_kiln_staking_andor_other/)**

8h ago

---

**[Daily General Discussion January 25, 2026](https://www.reddit.com/r/ethereum/comments/1qmaztv/daily_general_discussion_january_25_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

**[Has anyone actually bought digital gift cards with cryptocurrency?](https://www.reddit.com/r/ethereum/comments/1qmiimm/has_anyone_actually_bought_digital_gift_cards/)**

I’m curious if people are really using crypto to buy digital gift cards, or if it’s more of a niche thing. I’ve been holding some crypto for a while and don’t really want to cash it out to a bank just to spend a small amount. I’m looking for a simple way to use it for normal stuff like food, online shopping, or even travel. The idea of buying a digital gift card sounds convenient, especially when cards get blocked or payments fail. I also like the fact that delivery is instant and there’s no shipping involved. My main concerns are whether it actually works smoothly and if the cards are easy to use afterward. If you’ve done this before, how was the experience? Did the gift cards work as expected, and would you do it again?

23h ago

---

**[Most Web3 losses don’t start with a smart contract bug](https://www.reddit.com/r/ethereum/comments/1qmemlb/most_web3_losses_dont_start_with_a_smart_contract/)**

A lot of major Web3 losses don’t begin with a Solidity vulnerability. They start with systemic weaknesses: > Key mismanagement > Over-privileged or poorly designed access controls > Centralized infrastructure dependencies >Unsafe upgrade paths and admin mechanisms While smart contract bugs often get the spotlight, real-world incidents show a different pattern. Many failures happen around the contracts not inside them. Smart contract security isn’t just about what’s written in Solidity. It’s about how systems are operated, upgraded, and controlled once they’re live. Audits still matter, but security only works when the

1d ago

---

**[Daily General Discussion January 24, 2026](https://www.reddit.com/r/ethereum/comments/1qlf2ht/daily_general_discussion_january_24_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

2d ago

---

**[Really? Safe Mobile (formerly Gnosis Safe) no longer generates keys on-device, only imports seed phrases](https://www.reddit.com/r/ethereum/comments/1qlou3u/really_safe_mobile_formerly_gnosis_safe_no_longer/)**

Hi all. I am setting up a safe multisig with multiple phones belonging to different people as signers. With the former Safe Wallet app it was relatively easy to do, but I see now that since transitioning to the Safe GmbH entity, Safe Wallet is being replaced by the new Safe Mobile app which doesn't allow generating keys anymore. It is only possible to import existing ones by manually typing a seed phrase. I have been, to put it mildly, extremely surprised that securely generating a key on device is not possible anymore. Is one really supposed to generate new keys elsewhere, then import them into the device through their seed phrase? Doesn't this go against all technical and UX security principles? Among all the wallet providers, Safe is the last one I would expect something like this from given their reputation. My immediate reaction was: "I must have installed a fake app which is phishing me for my seed phrases", but I got confirmation from their support team that it's actually by design! I think this is a huge step backwards and I am genuinely out of options now for secure and simple multisig setups. Any advice?

1d ago

---

---

## Google News: "ethereum"

**[How SharpLink Aims to Be the Most 'Focused, Disciplined' Ethereum Treasury in 2026](https://decrypt.co/355733/how-sharplink-most-focused-disciplined-ethereum-treasury-2026)**

Ethereum treasury firm SharpLink Gaming hopes to stand apart from the pack by focusing on the long-term—with shareholders top of mind.

Decrypt • 19h ago

---

**[Ethereum treasury firm ETHZilla (ETHZ) buys jet engines for $12 million in RWA tokenization push](https://www.coindesk.com/business/2026/01/24/ethereum-treasury-firm-buys-jet-engines-amid-tokenization-push-after-selling-eth)**

ETHZilla is betting on bringing real-world assets on blockchain rails after it sold at least $114.5 million of its ETH stash over the past months.

CoinDesk • 1d ago

---

**[Robert Kiyosaki Not Worried by Bitcoin and Ethereum Price Fluctuations](https://finance.yahoo.com/news/robert-kiyosaki-not-worried-bitcoin-183151754.html)**

Robert Kiyosaki, the author of “Rich Dad Poor Dad” and investment guru, is not bothered by the price volatility of Bitcoin (CRYPTO: BTC) and Ethereum (CRYPTO: ETH). He maintains his stance of purchasing both cryptocurrencies irrespective of their price movements. Kiyosaki recently displayed interest in Ethereum, the world’s second-largest cryptocurrency. He holds the conviction that Bitcoin is set to reach a valuation of $1 million within the next few years or decade. In a post on X, Kiyosaki re

Yahoo Finance • 18h ago

---

**[Ethereum Foundation forms post-quantum security team, adds $1 million research prize](https://www.theblock.co/post/386938/ethereum-foundation-forms-post-quantum-security-team-adds-1-million-research-prize)**

The Block • 1d ago

---

**[What Drove Ethereum's 11% Decline This Past Week?](https://www.fool.com/investing/2026/01/25/what-drove-ethereums-11-decline-this-past-week/)**

A good week it was not for the world's second-largest cryptocurrency.

The Motley Fool • 21h ago

---

**[Analyst Says You’re Not Bullish Enough On Ethereum – What Does He Mean?](https://www.tradingview.com/news/newsbtc:fd9e8f6a0094b:0-analyst-says-you-re-not-bullish-enough-on-ethereum-what-does-he-mean/)**

A growing number of analysts believe Ethereum’s current price action is being misunderstood. Although frustration is growing due to Ethereum’s inability to hold above $3,000, some technical analysts are quick to point out that the structure forming beneath the surface tells a very different story…

TradingView • 1d ago

---

**[Did BlackRock Send an Ethereum Signal? Traders Speculate Over CEO Comments as Tom Lee’s Bitmine Buys More ETH](https://finance.yahoo.com/news/did-blackrock-send-ethereum-signal-103034447.html)**

Tom Lee’s Bitmine expanded its Ethereum holdings by more than $100 million. Traders are speculating over whether recent comments by BlackRock CEO Larry Fink signal ...

Yahoo Finance • 3d ago

---

**[Ethereum Builds Team To Guard Against Quantum Threat](https://bitcoinist.com/ethereum-builds-team-to-guard-against-quantum-threat/)**

Reports say the Ethereum Foundation has started a new team to prepare the network for possible quantum computer attacks. These machines could one day break

Bitcoinist.com • 22h ago

---

**[Ethereum ETF Outflows Surge as Bitwise’s ETHW Loses 4% of Assets in a Single Session](https://www.tipranks.com/news/cryptocurrencies/ethereum-etf-outflows-surge-as-bitwises-ethw-loses-4-of-assets-in-a-single-session)**

Ethereum Outflows Test Investor Nerves as Bitwise ETF Bleeds 4% of Assets in a Day The Bitwise Ethereum ETF, ETHW, saw a sharp reversal in sentiment on January 23, ...

TipRanks • 23h ago

---

**[Ethereum OG whale wakes up after nine years, deposits 50K ETH into Gemini](https://cryptobriefing.com/ethereum-og-whale-wakes-up-deposits-50-000-eth-gemini/)**

Ethereum whale deposits 50,000 ETH into Gemini after 9 years, signaling strategic profit-taking amid market weakness.

Crypto Briefing • 46m ago

---

---

## YouTube Videos: "ethereum"

**[ETHEREUM REVERSAL INCOMING?🔥 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=WIV9A_fCVVs)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 122 • 👍 15 • 💬 2 • ⏱️ 5:00 • 2h ago

---

**[Tom Lee - &quot;Biggest Crypto Reset EVER&quot; | Bitcoin &amp; ETH Price Prediction](https://www.youtube.com/watch?v=lZSS8ZRghvA)**

My FREE Daily On-Chain Analysis & Crypto News In 5-Mins: https://www.cryptonutshell.com/subscribe You can NOW ...

📺 Jamie Tree 

👁️ 2K • 👍 75 • 💬 33 • ⏱️ 17:46 • 21h ago

---

**[Why BlackRock CEO Thinks ETH is The FUTURE (BMNR RECAP)](https://www.youtube.com/watch?v=_jKWPZt3lYs)**

BMNR #bitmine #bmnr #tomlee #ethereum $ETH $BTC #btc #bitcoin Please Drop a Like & Subscribe if you enjoyed this video: ...

📺 Tevis

👁️ 23K • 👍 1K • 💬 186 • ⏱️ 29:47 • 1d ago

---

**[BITCOIN &amp; ALTCOIN WARNING: TOTAL COLLAPSE (Urgent Update)! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=qGnI8xHGp5Q)**

BITCOIN & ALTCOIN WARNING: TOTAL COLLAPSE (Urgent Update)! - Bitcoin News Today, Ethereum & Altcoins *Toobit* ...

📺 Crypto World

👁️ 8K • 👍 298 • 💬 329 • ⏱️ 24:21 • 14h ago

---

**[https://www.benjamincowen.com/Ethereum: Dubious Speculation](https://www.youtube.com/watch?v=J-QHMNnRK-Q)**

Into The Cryptoverse Premium: https://intothecryptoverse.com Into The Cryptoverse Newsletter: ...

📺 Benjamin Cowen

👁️ 31K • 👍 2K • 💬 145 • ⏱️ 26:46 • 9h ago

---

**[Ethereum Elliott Wave Update – Key Resistance Levels Ahead](https://www.youtube.com/watch?v=62ZnX-dwv9g)**

This video provides a professional Elliott Wave and technical analysis of Ethereum (ETH), focusing on market structure, major ...

📺 More Crypto Online

👁️ 2K • 👍 104 • 💬 6 • ⏱️ 5:06 • 13h ago

---

**[Raoul Pal: “This Is EXACTLY How The 2026 Bull Run Starts” [New Bitcoin &amp; Ethereum Prediction 2026]](https://www.youtube.com/watch?v=GHuKIq-EmnQ)**

Raoul Pal: “This Is EXACTLY How The 2026 Bull Run Starts” [New Bitcoin & Ethereum Prediction 2026] My FREE Daily 5-Min ...

📺 Crypto Nutshell

👁️ 15K • 👍 544 • 💬 79 • ⏱️ 14:27 • 21h ago

---

**[BITCOIN: You Need to See This Chart! (massive) - BTC, ETH, XRP Price Prediction Today](https://www.youtube.com/watch?v=i6s40KUqU8g)**

Want a free $30000 bonus + $20 just for signing up? Go here: ...

📺 BitcoinHyper

👁️ 9K • 👍 580 • 💬 14 • ⏱️ 57:29 • 15h ago

---

**[BlackRock’s CIO Gets Fed Chair Greenlight!! Huge News for Crypto &amp; Ethereum](https://www.youtube.com/watch?v=QzmMeRSqENo)**

Take Control of Your Retirement — Grow Crypto & Gold Tax-Advantaged. https://www.itrustcapital.com/go/savvy-finance If you're ...

📺 Savvy Finance

👁️ 6K • 👍 302 • 💬 17 • ⏱️ 18:21 • 19h ago

---

**[TRUMP: “BlackRock is likely to take over as Fed Chair” (Big Bitcoin &amp; Ethereum News)](https://www.youtube.com/watch?v=xsPBE4yghyA)**

BlackRock is likely to take over as Fed Chair” (Big Bitcoin & Ethereum News) ⭐ Follow Altcoin Daily on X: ...

📺 Altcoin Daily

👁️ 51K • 👍 2K • 💬 242 • ⏱️ 11:14 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
