---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-04-12T18:52:48.875996+00:00'
url: https://peekdeck.ruidiao.dev/ethereum.html
markdown_url: https://peekdeck.ruidiao.dev/ethereum.md
widgets: 6
data_types:
- cryptocurrency
- news
- social
- videos
---

# Ethereum Dashboard

Live Ethereum monitoring dashboard

**Last Updated:** April 12, 2026 at 18:52 UTC  
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

### $2,200.87

---

## Ethereum Chart

**24h:** -4.7%  
**7d:** +4.7%  
**30d:** +5.1%  
**90d:** -33.6%  
**1y:** +38.0%  

---

## Ethereum Market Stats

**Market Cap:** $265.69B
Rank #2

**Circulating Supply:** 120,691,054 ETH
No max supply

**All-Time High:** $4,946.05
-55.5%

**All-Time Low:** $0.43
+508368.1%

---

## Reddit: r/ethereum

**[Daily General Discussion April 12, 2026](https://www.reddit.com/r/ethereum/comments/1sj56x3/daily_general_discussion_april_12_2026/)**

**Welcome to the Daily General Discussion on** r/ethereum [https://imgur.com/3y7vezP\](https://imgur.com/3y7vezP) Bookmarking this link will always bring you to the current daily: [https://old.reddit.com/r/ethereum/about/sticky/?num=2\](https://old.reddit.com/r/ethereum/about/sticky/?num=2) Please use this thread to discuss Ethereum topics, news, events, and even *price*! Price discussion posted elsewhere in the subreddit will **continue to be removed.** As always, be constructive. - [Subreddit Rules](https://www.reddit.com/r/ethereum/about/rules/) Want to stake? Learn more at r/ethstaker **Community Links** * [Ethereum Jobs](https://ethereum.org/en/community/get-involved/#ethereum-jobs), [Twitter](https://x.com/ethereum) * [EVMavericks YouTube](https://www.youtube.com/@evmavericks), [Discord](https://discord.gg/evmavericks), [Doots Podcast](https://evmavericks.libsyn.com/) * [Doots Website](https://dailydoots.com/), Old Reddit [Doots Extension](https://github.com/etheralpha/ethfinance-extension) by u/hanniabu Calendar: [https://dailydoots.com/events/\](https://dailydoots.com/events/)

13h ago

---

**[WARNING: Aerodrome's CLGauge have an Integration Trap - Lost $2k due to incomplete ERC-721 implementation](https://www.reddit.com/r/ethereum/comments/1sjjq2i/warning_aerodromes_clgauge_have_an_integration/)**

I permanently lost $2,000 USD value trying to stake via direct contract interaction on Aerodrome. The CLGauge contract accepts safeTransferFrom via the onERC721Received hook but silently fails to update the staking state, creating a black hole for assets. I’m sharing this to warn other developers and integrators building on top of Aerodrome (Base chain), and hopefully get the attention of the Core Team or the Emergency Council, since standard Discord support just gave me the "contracts are immutable" playbook. Recently, I performed a safeTransferFrom (as a fallback to approve and deposit) directly to the Aerodrome Gauge (0x83e2E9493996651ed63033d81f5052cBE2fEB6A1). The transaction was mathematically and technically successful on-chain because the Gauge contract explicitly implements the IERC721Receiver interface. However, this is where the integration trap lies: While the contract gladly accepted physical custody of my NFT position, it completely failed to trigger the internal logic to update the _stakes mapping and the rewardGrowth snapshots. The Reality: By exposing the receiver hook without the corresponding push-based deposit logic, Aerodrome's contract signals false compatibility. It creates a critical state mismatch: the Gauge owns the NFT, but my wallet is no longer recognized as the owner, meaning I can neither call deposit() nor withdraw(). Has any other developer encountered this problem?

2h ago

---

**[World Liberty Financial borrowed its own stablecoin against its own token on a platform run by its own advisor and Justin Sun (WLFI biggest investor) just called it fraud.](https://www.reddit.com/r/ethereum/comments/1sjkjuc/world_liberty_financial_borrowed_its_own/)**

1h ago

---

**[Is the "Crypto Purge" at Twitter simply an algorithm glitch—or a massive Conflict of Interest?](https://www.reddit.com/r/ethereum/comments/1sjf56t/is_the_crypto_purge_at_twitter_simply_an/)**

4h ago

---

**[My journey trying to build something useful](https://www.reddit.com/r/ethereum/comments/1sij1vy/my_journey_trying_to_build_something_useful/)**

Over the past year I've been thinking a lot about Web3. Not the trading, not the speculation, not the casino. I don't trade crypto. I don't follow the markets. What fascinates me is the underlying idea: decentralized systems with code as the only authority. The technology itself. I've been a backend engineer for over a decade. Rails, SQL, the usual stack. But like many engineers, I burned out. The excitement to build faded. You know the feeling. You're competent, productive, but not discovering anything anymore. Then I looked seriously at blockchain. Not as an investor, but as an engineer. I asked myself: what would an application look like if built with absolute fidelity to what blockchain promises? Real utility (useful for the masses, not DeFi nonesense) NO off-chain layers (100% on-chain) NO insider advantages (fair economics) NO dependence on investors (self-sustaining) NO pointless tokenomics (ETH in, ETH out) Those five principles became my compass. I tried to build something that never violated them. But the Web3 ecosystem is built around tokenomics and speculation. There's no blueprint to follow. So I started pulling my own thread: I wanted to build something useful, deterministic, fully on-chain, with no complicated tokenomics. A simple game like TicTacToe with real ETH stakes? Interesting, but too narrow. Then the frame shifted. I wasn't building a game anymore. I was building a tournament layer. A universal competitive infrastructure that's fair, open-source, and 100% on-chain. That's when the hard problems started. How do you handle draws on a decentralized platform? How do you stop players griefing opponents without central authority? These aren't just technical questions. They're moral ones. They forced me to think deeply about fairness, about building a system nobody controls and nobody can manipulate. The answers surprised me. Forget Kubernetes, Redis, all that complexity. With these constraints (fully on-chain, truly open, completely decentralized) the legacy stack collapses into something elegant. A client talking directly to contracts. No servers. No databases. No company. Just code. That freedom changed how I think about software. So I built ETour A 100% on-chain tournament protocol, now live on Arbitrum. Players pay an entry fee, compete, the best player wins and takes the pot. Code decides everything. No intermediaries. As Web3 should be. I open-sourced it so developers can build their own games on it and inherit all of its features for free. I'm not here to tell you this is revolutionary. I built this because it felt like a problem worth solving. ETour is what came out the other side. The code is public. The contracts are immutable. The logic is yours to verify. PS: The technical docs are not final and will be updated soon. https://etour.games https://etour.games/whitepaper https://etour.games/manual https://etour.games/docs TLDR: ETour is useful, it's live, and it's open-source. Go ahead and play on it, or build your own game using its 100% on-chain and open source tournament modules.

1d ago

---

**[I tracked how much MEV I lost over 6 months of trading on DEXs. the number was disgusting.](https://www.reddit.com/r/ethereum/comments/1shi3pv/i_tracked_how_much_mev_i_lost_over_6_months_of/)**

So I went back through my wallet history and used a couple of MEV tracking tools to figure out how much value I actually lost to sandwich attacks and front-running over the past 6 months. not gonna share exact numbers but it was enough to make me seriously rethink where and how I trade on-chain. the thing that pissed me off the most wasn't even the big trades. it was the small ones. $200-500 swaps getting sandwiched for a few bucks each time. doesn't feel like much in the moment but it adds up fast when you're making multiple trades a week. what I learned: AMMs are basically open season for MEV bots. your trade hits the mempool and you're cooked private RPCs like flashbots protect help but they're not a complete solution. you're still trusting the builder not to screw you intent-based systems (cow swap etc) are better but they introduce solver trust assumptions and don't work for everything the only architecture where MEV extraction is structurally impossible is one where transaction ordering is provable and verifiable. not hidden, not trusted, but mathematically proven to be fair honestly the biggest takeaway is that most people have no idea how much they're losing. the "invisible tax" framing is accurate. you never see a line item that says "MEV bot took $4.50 from this trade" but it's happening on basically every swap. anyone else tracked their MEV losses? curious what numbers people are seeing. also curious if anyone has found a setup that actually eliminates it, not just reduces it.

2d ago

---

**[Ethereal news weekly #19 | Roman Storm acquittal hearing, ETHGlobal Cannes hackathon finalists, EVM Now block explorer](https://www.reddit.com/r/ethereum/comments/1shnkzm/ethereal_news_weekly_19_roman_storm_acquittal/)**

Roman Storm acquittal hearing, ETHGlobal Cannes hackathon finalists, EVM Now block explorer

🔗 [Ethereal news](https://ethereal.news/ethereal-news-weekly-19/) • 2d ago

---

**[Highlights from the All Core Developers Execution (ACDE) Call #234](https://www.reddit.com/r/ethereum/comments/1shgin6/highlights_from_the_all_core_developers_execution/)**

Ethereum developers align on Glamsterdam devnet progress, Hegota Account Abstraction direction, & key execution layer upgrades shaping the roadmap.

🔗 [EtherWorld.co](https://etherworld.co/highlights-from-the-all-core-developers-execution-acde-call-234/) • 2d ago

---

**[Staking](https://www.reddit.com/r/ethereum/comments/1sh5tfk/staking/)**

How does staking work? I staked ~0.1 eth through Exodus (they use Everstake) about 64 days ago. Eth validator queue is currently ~52 days. I was told I’d need to wait 1-5 days for it to pool on top of the validator time. It’s now approaching >1 week since the “expected” time to finish staking and start earning rewards, but it still shows staking. Is there a way to check how long I have to wait or know what happened?  [comments]

2d ago

---

**[Trump’s Crypto Project Just Borrowed $50 Million Against Its Own Token and Broke the Lending Pool](https://www.reddit.com/r/ethereum/comments/1sfoaqt/trumps_crypto_project_just_borrowed_50_million/)**

World Liberty Financial deposited 3B WLFI tokens as collateral to borrow $50M of its own stablecoin, pushing its lending pool into negative liquidity and raising concerns over circular treasury practices, governance risks, and regulatory scrutiny.

🔗 [DailyCoinPost](https://dailycoinpost.com/trumps-crypto-project-just-borrowed-50-million-against-its-own-token-and-broke-the-lending-pool/) • 4d ago

---

---

## Google News: "ethereum"

**[$1.5B Deal to Build ‘MicroStrategy of Ethereum’ Collapses](https://beincrypto.com/ether-machine-dynamix-spac-deal-terminated/)**

The Ether Machine terminates its SPAC merger with Dynamix, citing unfavorable market conditions amid ETH's sharp decline from its 2025 highs.

BeInCrypto • 23h ago

---

**[$Ethereum (ETH.CC)$](https://www.moomoo.com/community/feed/ethereum-eth-cc-116392149581830)**

@Etherdude 1166 Views|1 Like

Moomoo • 4h ago

---

**[TD Cuts Bitcoin Giant Strategy's Price Target, Calls Ethereum Treasury Sharplink a ‘Buy’](https://finance.yahoo.com/markets/crypto/articles/td-cuts-bitcoin-giant-strategys-220921727.html)**

TD Cowen remains positive on $55 billion Bitcoin treasury pioneer Strategy, despite trimming its price target yet again.

Yahoo Finance • 2d ago

---

**[Ethereum price prediction: sending mixed signals as ETH ETF inflows rise](https://www.tradingview.com/news/invezz:50b4ccd0c094b:0-ethereum-price-prediction-sending-mixed-signals-as-eth-etf-inflows-rise/)**

Ethereum price has risen in the past few days, helped by the ongoing exchange-traded funds (ETF) inflows and the recently announced US-Iran ceasefire. ETH token was trading at $2,220 on Sunday, up by 30% from its lowest level this year.Ethereum price is sending mixed signals The three-day chart sho…

TradingView — Track All Markets • 12h ago

---

**[Weekly recap of Bitcoin, Ethereum, Solana, and XRP ETF performance](https://ambcrypto.com/weekly-recap-of-bitcoin-ethereum-solana-and-xrp-etf-performance/)**

AMBCrypto • 7h ago

---

**[Most large cryptocurrencies fall as Ethereum tumbles](https://www.marketwatch.com/data-news/most-large-cryptocurrencies-fall-as-ethereum-tumbles-91a2f421-9307bc266dcb)**

MarketWatch • 3d ago

---

**[Bitmine Immersion: Market Is Missing The Hybrid Ethereum Model](https://seekingalpha.com/article/4889757-bitmine-immersion-market-is-missing-the-hybrid-ethereum-model)**

Bitmine Immersion's hybrid model combines large-scale ETH holdings, with MAVAN projected to generate $300 million annually. Learn why BMNR stock is a strong buy.

Seeking Alpha • 2d ago

---

**[Ethereum struggles amid US-Iran tensions, April price targets in doubt](https://cryptobriefing.com/ethereum-struggles-amid-us-iran-tensions-april-price-targets-in-doubt/)**

Ethereum is currently 55% below its all-time high as U.S.-Iran tensions escalate. The likelihood of Ethereum exceeding key April price targets has dropped, with

Crypto Briefing • 13h ago

---

**[Why is Crypto Rallying Today: Price Targets For Bitcoin, Ethereum and XRP](https://coinpedia.org/news/why-is-crypto-rallying-price-targets-for-bitcoin-ethereum-and-xrp/)**

The crypto market has rebounded, with Bitcoin rising 10% over the last eight days and Ethereum up 12% in the same period. The total market cap is now up

Coinpedia • 2d ago

---

**[Ethereum or Solana: Ethereum (ETH), Solana (SOL), and Pepeto, Which One Should You Buy During the Dip in 2026](https://financefeeds.com/ethereum-or-solana-ethereum-eth-solana-sol-and-pepeto-which-one-should-you-buy-during-the-dip-in-2026/)**

FinanceFeeds • 12h ago

---

---

## YouTube Videos: "ethereum"

**[Ethereum Supply Shock + BlackRock Staking = Massive Setup](https://www.youtube.com/watch?v=MhOmj6JSAgs)**

Check prices, drink coffee, read Milk Road. It's the easiest 5-minute habit to stay smart on crypto: ...

📺 Milk Road

👁️ 1K • 👍 90 • 💬 108 • ⏱️ 10:57 • 5h ago

---

**[Raoul Pal: &quot;A TSUNAMI Is Coming For Bitcoin &amp; Ethereum” | 2026 Crypto Prediction](https://www.youtube.com/watch?v=Gys5vX-3hfg)**

My FREE Daily 5-Min Crypto Newsletter: https://www.cryptonutshell.com/subscribe ⮕ Cold Storage Wallet: ...

📺 Crypto Nutshell

👁️ 23K • 👍 684 • 💬 161 • ⏱️ 19:27 • 1d ago

---

**[Ethereum Launches War-Proof Browser To Kill Chrome?🌐Freedom Browser INTERVIEW](https://www.youtube.com/watch?v=MkVhdstQvmE)**

Freedom is a minimalist browser for Swarm and IPFS. No centralized gateways. You connect directly to peers and become part of ...

📺 Paul Barron Network

👁️ 7K • 👍 687 • 💬 86 • ⏱️ 18:02 • 2h ago

---

**[Ethereum Price Analysis – Is a Pullback Coming Next Week?](https://www.youtube.com/watch?v=TKYhyD_smXY)**

Ethereum has completed a five wave move up from the March lows – a critical Elliott Wave signal. In this video I break down what ...

📺 More Crypto Online

👁️ 3K • 👍 181 • 💬 19 • ⏱️ 9:19 • 17h ago

---

**[Bitcoin &amp; Ethereum Price Analysis Today | Market Trend &amp; Next Move | BTC &amp; ETH Price Prediction 2026](https://www.youtube.com/watch?v=Be0MuVrrJvY)**

Bitcoin & Ethereum Price Analysis Today | Market Trend & Next Move | BTC & ETH Price Prediction 2026 Premium on Telegram ...

📺 Crypto Gyan

👁️ 528 • 👍 75 • ⏱️ 5:19 • 3h ago

---

**[CRUCIAL ETHEREUM UPDATE🚨 (Ethereum Price Prediction 2026)](https://www.youtube.com/watch?v=oi3hmciShIc)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 213 • 👍 10 • 💬 3 • ⏱️ 4:41 • 9h ago

---

**[ADA, XRP &amp; ETH Holders NEED to Hear This IMMEDIATELY – Matt Hougan](https://www.youtube.com/watch?v=Ai1_0W5vZBM)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 5K • 👍 221 • 💬 27 • ⏱️ 15:02 • 1d ago

---

**[BITCOIN PRICE SQUEEZE: Final Warning (Urgent)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=OruVCDpa6DY)**

BITCOIN PRICE SQUEEZE: Final Warning (Urgent)!!! - Bitcoin News Today, Ethereum & Altcoins *NOVAVA* ...

📺 Crypto World

👁️ 9K • 👍 317 • 💬 419 • ⏱️ 22:15 • 20h ago

---

**[BMNR Stock Next Week&#39;s Price Analysis | Detailed Analysis with Ethereum Price Action](https://www.youtube.com/watch?v=1bVsQuJ-zvg)**

BMNR Next Week Price Action Forecast | Detailed Analysis with Ethereum Price Action A company on the NYSE quietly ...

📺 Smart Stock Sam

👁️ 99 • 👍 10 • 💬 4 • ⏱️ 14:47 • 2h ago

---

**[CLARITY Rally in 3 Days?📈Crypto Technical Analysis @TimWarrenTrades](https://www.youtube.com/watch?v=96h2EGSZvEk)**

Coinbase Global (NASDAQ: $COIN) CEO Brian Armstrong is calling for the passage in Congress of the U.S. Clarity Act.

📺 Paul Barron Network

👁️ 56K • 👍 3K • 💬 214 • ⏱️ 33:50 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
