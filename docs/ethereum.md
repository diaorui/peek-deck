---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-09-02T20:57:11.414774+00:00'
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

**Last Updated:** September 02, 2026 at 20:57 UTC  
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

### $2,378.19

---

## Ethereum Chart

**24h:** -0.9%  
**7d:** -4.7%  
**30d:** +28.0%  
**90d:** +51.1%  
**1y:** -46.3%  

---

## Ethereum Market Stats

**Market Cap:** $291.99B
Rank #2

**Circulating Supply:** 122,012,213 ETH
No max supply

**All-Time High:** $4,946.05
-51.6%

**All-Time Low:** $0.43
+552693.6%

---

## Reddit: r/ethereum

**[Daily General Discussion September 02, 2026](https://www.reddit.com/r/ethereum/comments/1w50oyb/daily_general_discussion_september_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

15h ago

---

**[Dev Tools Guild August 2026 update](https://www.reddit.com/r/ethereum/comments/1w57swl/dev_tools_guild_august_2026_update/)**

**TL;DR**: Platåberget testnet available for Glamsterdam upgrade testing. Foundry v1.8.0 symbolic testing preview. Ox v1 stable.

🔗 [devtoolsguild.xyz](https://devtoolsguild.xyz/blog/devtoolsguild-august-2026-update) • 9h ago

---

**[What’s stopping you from using a crypto payment card?](https://www.reddit.com/r/ethereum/comments/1w4dajd/whats_stopping_you_from_using_a_crypto_payment/)**

I’ve been looking into crypto payment cards because I’d rather spend directly from my wallet than constantly cash out to my bank. The convenience sounds great, especially for everyday purchases, but I’m curious what the actual experience is like. What’s stopping you from using one fees, KYC, taxes, security or something else? And if you already use one, has it actually replaced your regular card for anything?

1d ago

---

**[Daily General Discussion September 01, 2026](https://www.reddit.com/r/ethereum/comments/1w424z1/daily_general_discussion_september_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

1d ago

---

**[Daily General Discussion August 31, 2026](https://www.reddit.com/r/ethereum/comments/1w33wbe/daily_general_discussion_august_31_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

2d ago

---

**[If your deployment template references a smart contract audit, does that reference survive upgrades?](https://www.reddit.com/r/ethereum/comments/1w3bq23/if_your_deployment_template_references_a_smart/)**

I work on the assessment side at a smart contract auditing company. This came out of an audit we did on a governance-approved deployment system on a permissioned chain. The system stores metadata for each approved deployment template: a bytecode hash, a storage layout hash, a link to the audit report, and the source repository commit. On paper, every deployed proxy maps back to reviewed and approved code. At deployment time, nothing checks those fields. The factory resolves the implementation live from the beacon, and the beacon owner can publish a new version at any point after the template was registered. The bytecodeHash field is in storage, but no require statement compares it to address.codehash on what actually gets deployed. After the first beacon upgrade, every new deployment runs code that was never part of the original audit, while the template still points at the old audit URI and the old commit. When we flagged it, the project team didn't start enforcing the hash. They removed the bytecode and storage layout hashes from the template entirely. I'd argue that's more honest than keeping fields that imply verification and deliver none. But what's left is a pipeline where the only governance control is trusting the beacon owner, and the on-chain record of what was audited diverges silently from what's actually running. Regulators running MiCA compliance assessments or CASP license reviews want to see governance over what gets deployed to production. If your template stores an audit reference and an assessor asks whether it's enforced, "recorded but not checked" puts you in a worse position than having no reference at all. The reference misrepresents what the deployed code went through. Open your template registry or deployment manifest. Find the field that references the audit or stores a bytecode hash. Grep for it on the deploy path. If the field is written once at registration and never appears in a require or assert during deployment, you have decorative governance metadata. address.codehash exists on-chain. The check is one comparison. Nobody wrote it. Plenty of governance models handle this off-chain with CI/CD gates, human sign-offs, and change management procedures, and those work for permissioned systems. The gap opens when the on-chain record looks like it provides a guarantee it doesn't, because the next person who reads that template will assume enforcement already happened. If a MiCA license or VARA license assessor asked you to demonstrate that your template's bytecodeHash is enforced at deployment, could you show them the require statement?

2d ago

---

**[Daily General Discussion August 30, 2026](https://www.reddit.com/r/ethereum/comments/1w2874e/daily_general_discussion_august_30_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

3d ago

---

**[Daily General Discussion August 29, 2026](https://www.reddit.com/r/ethereum/comments/1w1d8l9/daily_general_discussion_august_29_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Calendar: https://dailydoots.com/events/

4d ago

---

**[I have built a tool which can provide bulk wallet address labels (CEX wallets, entities, risk tags) - cheap, fast, any list size](https://www.reddit.com/r/ethereum/comments/1w1lt0r/i_have_built_a_tool_which_can_provide_bulk_wallet/)**

I run a pipeline that enriches crypto wallet addresses with the kind of labels you'd normally dig out of block explorers and intelligence platforms one address at a time: Entity / owner - e.g. Binance: Hot Wallet, Coinbase: Cold Wallet, Deribit Category tags - Centralized Exchange, Hot/Cold Wallet, Mixer, Gambling, Sanctioned (OFAC/UK), High Transacting, etc. First-funder relationships and contract flags Per-chain coverage - Ethereum, BSC, Base, Arbitrum, Polygon, Avalanche and more, one row per network Format: clean CSV/JSON, your list in → labeled list out. Turnaround is fast (100k addresses in under an hour) and pricing is a fraction of what intelligence-platform subscriptions cost - it scales down to small one-off lists and up to millions of addresses. Useful if you're doing compliance/AML screening, fraud or theft investigations, exchange flow analysis, dataset enrichment for research, or tagging counterparties in your own analytics. DM me with roughly how many addresses and what chains - I'll quote you same day. Happy to run a free sample on 50–100 of your addresses first so you can judge the quality yourself.

4d ago

---

**[ethstaker-deposit-cli 1.3.1 pre-release](https://www.reddit.com/r/ethereum/comments/1w1lqgs/ethstakerdepositcli_131_prerelease/)**

4d ago

---

---

## Google News: "ethereum"

**[Sality Botnet Dismantled After Eight Years of Stealing Bitcoin and Ethereum](https://decrypt.co/377156/sality-botnet-dismantled-after-eight-years-of-stealing-bitcoin-and-ethereum)**

CrowdStrike and the DOJ isolated more than 15,000 infected machines in a malware takedown spanning four countries.

Decrypt • 9h ago

---

**[Bitcoin and ethereum prices today, Wednesday, September 2, 2026: Crypto prices tumble as Iran war reignites](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-wednesday-september-2-2026-crypto-prices-tumble-as-iran-war-reignites-112639522.html)**

Bitcoin opened at $77,395.89 on Wednesday, September 2, 2026, 1.5% lower than Tuesday's opening price. As of 7:13 a.m. ET, bitcoin moved down to $76,597.13. Ethereum opened at $2,417.66 today, down 2.0% from Tuesday's opening price. Ethereum fell further this morning to $2,373.76 as of 7:13 a.m. ET.

Yahoo Finance • 9h ago

---

**[Current price of Ethereum for September 1, 2026](https://fortune.com/article/price-of-ethereum-09-01-2026/)**

Ethereum isn’t just digital money; it's a decentralized computing platform, meaning users can build and run apps on it without oversight of a company or bank.

Fortune • 1d ago

---

**[Elon Musk Grok AI Predicts Ethereum Price by January 1, 2027](https://www.tradingview.com/news/99Bitcoins:d595a9eb7094b:0-elon-musk-grok-ai-predicts-ethereum-price-by-january-1-2027/)**

Elon Musk Grok AI predicts that while Ethereum (ETH) could hit some big targets by the end of 2026, the chatbot predicts modest gains by January 1, 2027, something that ETH maxis won’t want to hear.ETH is currently trading for $2,450, down around -0.5% over the past 24 hours and -1.5% over the past…

TradingView • 10h ago

---

**[USDT: Tron Supply Tops Ethereum at $94.27B](https://blockchain.news/flashnews/usdt-tron-supply-tops-ethereum-94-27b)**

USDT supply on Tron hits $94.27B after $4B gain, overtaking Ethereum as Tron vs Ethereum stablecoin dominance shifts.

blockchain.news • 9h ago

---

**[Lido funds ValOS initiative to enhance Ethereum validator standards](https://cryptobriefing.com/lido-valos-ethereum-validator-standards/)**

Lido DAO allocated $60K through its LEGO program to fund ValOS, a framework bringing ISO 27001 and SOC 2 standards to Ethereum validator

Crypto Briefing • 1d ago

---

**[What price will Ethereum hit in September Odds & Prediction Market Analysis](https://cryptoslate.com/predictions/market/what-price-will-ethereum-hit-in-september-2026/)**

Track What price will Ethereum hit in September prediction market analysis with live Polymarket odds, probabilities, liquidity, and market catalysts.

CryptoSlate • 1d ago

---

**[Ethereum Targets $6,000 as Bitmine Chairman Tom Lee Cites Four Major Catalysts](https://www.tipranks.com/news/ethereum-targets-6000-as-bitmine-chairman-tom-lee-cites-four-major-catalysts)**

Bitmine Immersion Technologies ($BMNR) Chairman Tom Lee projects that Ethereum (ETH-USD) could hit $6,000 as capital flows back into the crypto sector. Lee pointed ...

TipRanks • 2d ago

---

**[Bitcoin, Ethereum, XRP, Dogecoin Retreat Amid Trump's Iran Warning: Analyst Says BTC Mirroring 2023 Botto](https://www.benzinga.com/crypto/cryptocurrency/26/09/61565865/bitcoin-ethereum-xrp-dogecoin-retreat-trump-iran-warning-btc-breakout)**

Leading cryptocurrencies corrected on Tuesday, August 1, as investors weighed in on President Donald Trump's latest threats to Iran.

benzinga.com • 19h ago

---

**[Wall Street Crypto Treasuries Are Buying Bitcoin and Ethereum Again. Why?](https://finance.yahoo.com/markets/crypto/articles/wall-street-crypto-treasuries-buying-210000500.html)**

ETF money returned, Washington set a calendar, and crypto treasuries started buying again. Here is what actually changed.

Yahoo Finance • 1d ago

---

---

## YouTube Videos: "ethereum"

**[Is Robinhood BEATING Ethereum?](https://www.youtube.com/watch?v=0-4jN1C2B5M)**

Join CBC Lite https://go.coinbureau.com/CBC-Lite-CB-Des Get The Hottest Crypto Deals ...

📺 Coin Bureau

👁️ 3K • 👍 149 • 💬 10 • ⏱️ 11:39 • 2h ago

---

**[Its Game Over For Anyone Not Holding Crypto Bitcoin, Ethereum &amp; XRP Are About To Change Lives](https://www.youtube.com/watch?v=xwC9JD4zq5w)**

Who could have ever imagined that 40 countries and 20+ banks buying Bitcoin and XRP would have a positive effect on their ...

📺 The Modern Investor

👁️ 11K • 👍 822 • 💬 560 • ⏱️ 31:53 • 11h ago

---

**[BITCOIN LIQUIDATIONS CONFIRMED (This is Next)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=j5hs78mWEOo)**

BITCOIN LIQUIDATIONS CONFIRMED (This is Next)!!! - Bitcoin News Today, Ethereum & Altcoins *LBANK* ...

📺 Crypto World

👁️ 13K • 👍 294 • 💬 660 • ⏱️ 18:58 • 18h ago

---

**[Right Before Crypto Goes Parabolic, Ethereum Always Does This](https://www.youtube.com/watch?v=YkOrogr_ntM)**

Latest Bitcoin, Ethereum, Solana, TAO News TRADE on WEEX - WIN THE AMALFI COAST GETAWAY: ...

📺 Altcoin Daily

👁️ 58K • 👍 2K • 💬 88 • ⏱️ 9:05 • 1d ago

---

**[BMNR Is About to Own 5% of Ethereum… Then What?](https://www.youtube.com/watch?v=tPYIn-uv_2I)**

Get lifetime access to my full investing system + all spreadsheets, my real-time portfolio, trade alerts, DAILY member-only ...

📺 Future Investing

👁️ 5K • 👍 152 • 💬 91 • ⏱️ 8:53 • 6h ago

---

**[Tom Lee on Going From Owning 5% to 10% of All Ethereum](https://www.youtube.com/watch?v=nMBLD6tffys)**

Bitmine Chair Tom Lee discusses why he landed on owning 5% of Ethereum — and why owning 10% wouldn't be out of the ...

📺 Coinage

👁️ 124 • 👍 5 • ⏱️ 1:03 • 6h ago

---

**[XRP + Goldman Sachs is TOP again, Ripple Goes ETHEREUM STANDARD, Japan OIL, Canton Moving to FLIP](https://www.youtube.com/watch?v=1Gf3Ltl-hyA)**

xrp #xrpl #Ripple #goldmansachs #cantonnetwork Follow me on Twitter: @sentosumosaba Patreon: ...

📺 crypto Eri

👁️ 14K • 👍 436 • 💬 27 • ⏱️ 10:20 • 1d ago

---

**[Bitcoin, Ethereum &amp; XRP Aren&#39;t Done Yet This Is Going To Shock The Living Daylights Out Of You](https://www.youtube.com/watch?v=PMnxp61twvE)**

Some people will get it and some wont. Some people will invest and make tons of money and others will continue to wait for prices ...

📺 The Modern Investor

👁️ 14K • 👍 842 • 💬 278 • ⏱️ 33:07 • 2d ago

---

**[THIS IS CRAZY $10,000 ETHEREUM INCOMING #xrp #ethereum #crypto](https://www.youtube.com/watch?v=GqLyLuh0Kz8)**

📺 CryptoWendyO

👁️ 9K • 👍 419 • 💬 27 • ⏱️ 2:17 • 1d ago

---

**[Will crypto ever go back up? (AMA Bitcoin PulseChain HEX Ethereum)](https://www.youtube.com/watch?v=wRpgHNT1qWU)**

public DCA wallet: 0x96Fb732038F5Ba439bb4792Ec279a0ed56B76893 get yours at https://zkxwallet.com how to buy ...

📺 Crypto Coffee

👁️ 2K • 👍 126 • 💬 61 • ⏱️ 1:01:29 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*
