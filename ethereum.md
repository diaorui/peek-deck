---
title: Ethereum Dashboard
description: Live Ethereum monitoring dashboard
category: crypto
page_id: ethereum
updated: '2026-06-02T19:41:40.426331+00:00'
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

**Last Updated:** June 02, 2026 at 19:41 UTC  
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

### $1,907.55

---

## Ethereum Chart

**24h:** -5.5%  
**7d:** -6.5%  
**30d:** -19.3%  
**90d:** -8.6%  
**1y:** -26.8%  

---

## Ethereum Market Stats

**Market Cap:** $228.67B
Rank #2

**Circulating Supply:** 120,685,138 ETH
No max supply

**All-Time High:** $4,946.05
-61.7%

**All-Time Low:** $0.43
+437563.3%

---

## Reddit: r/ethereum

**[Daily General Discussion June 02, 2026](https://www.reddit.com/r/ethereum/comments/1tugwmx/daily_general_discussion_june_02_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

14h ago

---

**[Dutch crypto broker Knaken (Rotterdam) abruptly shuts down, customers locked out of funds. This is why self-custody matters.](https://www.reddit.com/r/ethereum/comments/1tuu8gn/dutch_crypto_broker_knaken_rotterdam_abruptly/)**

4h ago

---

**[zk proofs aren't just for rollups. the more interesting use case is verifiable exchange execution](https://www.reddit.com/r/ethereum/comments/1tun93o/zk_proofs_arent_just_for_rollups_the_more/)**

most of the zk conversation in ethereum right now is about rollups. proving block validity, compressing state, bridging trustlessly. all important stuff. but there's a use case that i think is more immediately impactful and barely anyone talks about: using zk proofs to make exchange matching engines verifiable. here's the problem. every CLOB-style DEX runs a matching engine, and almost all of them are black boxes. your order goes in, a fill comes out, and you trust that the engine matched you fairly. you have no way to verify it. even the "decentralized" ones. the matching layer is the single biggest trust surface on any exchange and it's the one nobody can actually check. the fix isn't moving matching fully on-chain. dydx v4 went that direction and you pay for it in throughput, because every fill has to go through consensus. for a CLOB that's a hard ceiling on what you can offer. the more interesting path: keep matching off-chain for speed, but commit batched state transitions with validity proofs. the engine stays fast, but every batch of fills becomes cryptographically verifiable. no fill can be reordered, front-run, or fabricated without the proof failing. you get execution speed and provability without forcing a tradeoff between them. this feels like it matters more for end users than zk rollups honestly. rollups prove that a block was valid. exchange proofs prove that your specific trade was matched correctly. one is infrastructure-level, the other is directly about your money. curious why this isn't getting more attention in the ethereum zk community. is it a tooling problem? a "nobody's built it yet" problem? or does the market just not care enough about execution verifiability yet?

8h ago

---

**[Decentralized* Storage in a Plywood Box: ETHPrague Day One](https://www.reddit.com/r/ethereum/comments/1tuqou6/decentralized_storage_in_a_plywood_box_ethprague/)**

(* Not actually decentralized) Day One of ETHPrague My home for the next four nights is a capsule in a constellation of plywood. A Prague hostel has converted bunk-bed rooms into a capsule hotel, filling the room with ten interlocking plywood pods. Each room has a toilet, a shower and two sinks. The rooms share a small kitchen that reeks of ramen spice packets. This looks to be a clever move by the hostel: off season, over half the capsules are full and probably at twice the price that a single bunk bed would have gone for. The capsules are snug: an entrance with a short bench and a mirror and just enough room to stash my suitcase, as long as I have no intention of opening it. I need to step onto the bench to hoist up to the single mattress. My neighbour's bed intersects like a backwards Tetris piece but our privacy is complete other than the shared spaces. The following day I take a tram to Náměstí Republiky where people are already setting up their stands with cocktails and grilled sausages. The flashy Art Nouveau Municipal House is grafted onto a medieval wall, sitting uncomfortably next to the medieval Gothic tower at the boundary of Old Town and New Town. The Art Nouveau building built in 1912 on the site of the former Royal Court palace seems altogether too imposing for a crypto-conference. Two sculptures by Ladislav Šaloun flank the entrance: The Degradation of the People and The Resurrection of the People. Perhaps we are in the right place after all. https://preview.redd.it/9xuwmr8hcv4h1.jpg?width=2542&format=pjpg&auto=webp&s=aa6bb3aa4edf2dcca7a32691ece3c593a7ee7bd9 I join the t-shirted backpacked crowd and walk in. We gather in the "hacker space", Smetana Hall. Small tables fill the space under the domed stained-glass-and-steel ceiling. Mirrors sparkle with the light from gilded lamps. At the far end of the space is a stage with a massive organ of almost 5,000 pipes and two more sculptures. This is the actual room where Czechoslovak independence was proclaimed in 1918. After the opening speeches, the hackers will occupy this space. I can't help wishing that I was a hacker, dedicating the next seventy-two hours to creating something in this ornate hall. https://preview.redd.it/32zerkyjcv4h1.jpg?width=3184&format=pjpg&auto=webp&s=d48961b3ae34a702d9ef2ecf0016a7a7d7c375ff The first talk I attend is Emilien Duc of DeFiScan with the alarming title of How Many People Can Rug You?. He declares 2026 the year of preventable losses, with a common factor of off-chain failures. The problem is we treat "decentralized" as a buzzword, rather than a measurable metric. We need to look at who actually controls the protocol behind the scenes. This misuse of DeFi (Decentralized Finance) is a key theme throughout the conference. Duc's point is that most DeFi today still depends on small groups of admins/keyholders behind the scenes. A quick search tells me that the industry standard is 4-of-7 or 5-of-9 multisig set up, which fits in with his average of seven admins per smart contract. https://preview.redd.it/p4i81o9pcv4h1.jpg?width=3112&format=pjpg&auto=webp&s=a006c2d7355e84aef7137ab500be4bd9dec28438 The answer to the question of how many people, by the way, is that it only takes four or five keyholders to rug you on most platforms. We're mostly just trusting a handful of guys in group chat. Next up is Sem with How we hacked TheDAO, again, relating the 2016 hack that broke DAO and led to an Ethereum fork. The story of how they decided to use the same exploit to recover funds, waiting to see if anyone else spotted them and got there first, was truly gripping. The Crypto regulation and banks panel focuses on the intersection of cryptocurrency regulation and decentralized finance. Czech politician Ondřej Kovařík and Raiffeisenbank's Product Owner for crypto-initiatives Tomáš Piškule speak to Ondrej Pilny, the head of Ecosystem Growth at Gnosis. They discuss the state of DeFi, MiCA regulation, stablecoins as a simple vehicle to transfer value, and the state of legislation. Both predict high crypto adoption in the banks in five years. Most exciting point: Agentic commerce will not happen without stable coins. If this is happening and people will start regularly using any kind of agents to carry out transactions on the internet for them, it will all happen on blockchain rails. https://preview.redd.it/t0q04aqtcv4h1.jpg?width=2691&format=pjpg&auto=webp&s=e8ba6c441a391a4f57b371032ee917e99cb7f4a2 Unlocking AI Agentic UX with Google’s AP2 Standard and the x402 Protocol by Ben Greenberg, a senior dev/rel at Arbitrum, is surprisingly accessible: agents on the web are the new interface and we need to optimize for them. They are even more impatient than humans, who will quietly wait 3-4 seconds for a site to load, and they have difficulties paying. This is where the x402 protocol comes in. I need a break. Ben is standing in the corridor and I join the conversation; we talk about travel and cruise ships and porn. I miss a talk on Optimizing Yield While Prioritizing Safety. Stanislaw Šimek speaks on The Future of DeFi: From the Trenches and the Law, giving Web3 projects a clear decision point: are you tradfi and regulated or are you permissionless? Because, he warns, the current middle ground of pretending to be decentralized to avoid regulation will not survive. If the cocktails were less expensive, I would be getting a drink every time someone told us that most DeFi isn't. Instead I sneak out to have some lunch at Náměstí Republiky which, I notice, has cheaper cocktails available in a variety of stalls. I dismiss the idea of running out of Municipal House every time someone complains about the mis-use of DeFi and settle for some food. I return to the fray for editor Macauley Peterson on When tokens meet reality: why crypto needs disclosure standards. Peterson tells us about the original innovation of trading securities on Wall Street, and twenty-five years later, those traders wrote a constitution and formed what would become the New York Stock Exchange. The Securities Exchange Act, the Chicago Board of Trade and the Futures Act show that same trend: members of a community instituting formal trading strategies and contract standardization. And yet, now, the people who understand the technology are hanging back. The question is whether they will step in to create industry-led standards or continue to allow people who don't understand it to create regulation. I may not be in that group of those who understand the technology but I am hugely motivated by the talks on this first day, loving that feeling that every person can make a difference. https://preview.redd.it/sadw5h62dv4h1.jpg?width=2877&format=pjpg&auto=webp&s=b502c4622b4df6a15e3c0c71f207bc719c232dac Tobias Schreier's talk is a battle cry: Show Me the Users! A Data-Driven Reality Check. He shows us chewy stats from growthepie that show that Ethereum and L2 usage is still heavily dominated by basic financial speculation. The most startling stat: 75% of Polygon fees are coming from users interacting with Polymarket? What happens when they move? But growthepie also shows us real-world traction, for example a shift towards non-USD stablecoins such as EuroC and the Swiss CHF-based Frankencoin that you can use to pay for your cheap groceries at SPAR. By now, the planned presentations are diverging quite a bit from the schedule, especially for those of us changing rooms every 25 minutes, and I dash in late for Monetizing Crazy Times with Prediction Markets by Swiss lawyer Anne-Grace Kleczewski. She convinces me with a single quote: "Greatly designed beliefs certainly contribute to crowd intelligence, but poorly designed ones are merely depicting attempts at making some quick money." Between the three tracks of talks, people gather out on the balcony, standing in the sunshine overlooking the tourists. The conversations swirl around me. "I'm not with them any more but I'm still in Portugal, co-living there, looking for opportunities." "People are saying the old location was better but I like this. It feels like the real Prague." "Yeah, I'm back in Berlin, got a one-year-old daughter, so that's grounding me." "I tell them that they all need x402 but to be honest, I'm not that technical." "I got a gun. Accidentally. It's not a bug, it's a feature." I go back inside. I get back into synch with Who Owns Attention in a Decentralised Future? Toward Value-Aligned Recommendation Systems by Alexander Trauth-Goik, who explains algorithmic curation in surveillance capitalism and that we are being tricked into believing that invasion of our privacy and the fracturing of our attention is a necessary price to taking part in social media. "Do we want recommendation algorithms and technology in general to hijack and undermine our psychological vulnerabilities, or to empower and elevate the better angels of our nature?" Recommendation algorithms could be giving us information that better serve our long-term interests and goals. Veronika Civínová gives us a surprising angle with Practical challenges of EU laws: from climate to crypto. Civínová argues that while the media frames crypto and climate regulations as being in direct conflict, crypto actually fits beautifully into the broader definition of "sustainability." By looking past just environmental impact to include social and corporate governance pillars (like community focus and superior business conduct), crypto can prove it's sustainable, provided it doesn't "significantly harm" the environment. It's only ten past six but I feel like I've already experienced three days of conference into one. I wander aimlessly around Municipal House, sipping water and looking up at the ornate ceilings and dangling chandeliers. Then I walk home, stopping for a hearty meal at a quiet restaurant on the way. One beer at the hostel bar and I have to admit that I'm ready for bed. I snuggle into my plywood pod, head full of ideas. My neighbor enters his pod, slamming the door behind him, shaking the entire unit of four. I consider banging on the wall, annoying everyone with my hiss of "can you keep it down???" but while I'm still considering how to respond in a way that doesn't make things worse, my eyes flutter shut and I fall asleep. --- This series was supported through the generosity of the Peacock Foundation. Tomorrow: I am reminded once again that my greatest vulnerability isn't code. It's me.

6h ago

---

**[Is WBTC safe?](https://www.reddit.com/r/ethereum/comments/1tuejlb/is_wbtc_safe/)**

I am considering converting a few BTC to WBTC to stake. Theorically WBTC is better because I can also earn passive income while 'holding my keys' which is what i'm trying to understand: Is this custodial? more risky or same as USDT? Was there any freeze or issue on it by past?

16h ago

---

**[A new way to fund open source with Ethereum at the core](https://www.reddit.com/r/ethereum/comments/1tuqq7t/a_new_way_to_fund_open_source_with_ethereum_at/)**

Open source software does not have to choose between user freedom and sustainable funding. By combining GPL licensing with paid entitlements to the official service path, projects can keep the code forkable while making it rational for serious users to fund the shared infrastructure they depend on.

🔗 [jthor.eth](https://jthor.eth.link/blog/2026/06/01/new-funding-model-for-open-source/) • 6h ago

---

**[Dev Tools Guild May 2026 update](https://www.reddit.com/r/ethereum/comments/1tuobq1/dev_tools_guild_may_2026_update/)**

**TL;DR**: TheDAO Security Fund Ethereum security quadratic funding round results, Vyper 0.5.0 alpha prereleases, and pattern matching in Core Solidity.

🔗 [devtoolsguild.xyz](https://devtoolsguild.xyz/blog/devtoolsguild-may-2026-update) • 8h ago

---

**[r/BASE FOUNDER 'AMA' SERIES: 'Charms' Join us 7pm UTC Tues 2nd June](https://www.reddit.com/r/ethereum/comments/1tuq4jy/rbase_founder_ama_series_charms_join_us_7pm_utc/)**

6h ago

---

**[How should new Ethereum L2s avoid becoming liquidity islands at launch?](https://www.reddit.com/r/ethereum/comments/1tui882/how_should_new_ethereum_l2s_avoid_becoming/)**

One thing I have been thinking about with newer Ethereum L2 ecosystems is the gap between “apps can deploy” and “users can actually bring useful liquidity in.” GIWA/GASOK is a good recent example. Teams are building toward mainnet, but the infrastructure question comes pretty early: If a wallet, DEX, lending app, or consumer app launches on a new L2, should each team be responsible for integrating bridges, routing, liquidity sources, and asset variants on its own? That feels like a lot of duplicated work for early app teams. One possible model is shared cross-network execution infrastructure: apps integrate a single SDK, and routing/liquidity access is handled outside the app. SODAX is preparing this kind of setup for GIWA builders, but the broader question applies to any new Ethereum L2. The tradeoffs seem non-trivial: app teams get faster access to multi-network liquidity users avoid manually bridging through several tools the L2 ecosystem may feel less empty at launch but routing, solver behavior, asset representation, and failure modes need to be easy to reason about For people who have built on or around Ethereum L2s: where do you think this responsibility should sit? Should liquidity/access infrastructure be handled by the L2 ecosystem, each individual app, or external execution layers?

13h ago

---

**[Daily General Discussion June 01, 2026](https://www.reddit.com/r/ethereum/comments/1tti43r/daily_general_discussion_june_01_2026/)**

Welcome to the Daily General Discussion on r/ethereum https://imgur.com/3y7vezP Bookmarking this link will always bring you to the current daily: https://old.reddit.com/r/ethereum/about/sticky/?num=2 Please use this thread to discuss Ethereum topics, news, events, and even price! Price discussion posted elsewhere in the subreddit will continue to be removed. As always, be constructive. - Subreddit Rules Want to stake? Learn more at r/ethstaker Community Links Ethereum Jobs, Twitter EVMavericks YouTube, Discord, Doots Podcast Doots Website, Old Reddit Doots Extension by u/hanniabu Calendar: https://dailydoots.com/events/

1d ago

---

---

## Google News: "ethereum"

**[Ethereum's Vitalik Buterin is rethinking how DeFi handles market crashes](https://www.coindesk.com/tech/2026/06/01/ethereum-s-vitalik-buterin-is-rethinking-how-defi-handles-market-crashes)**

In a research post published Monday, Buterin proposed creating index-tracking assets using options contracts rather than the debt-based structures that underpin much of DeFi today.

CoinDesk • 1d ago

---

**[BMNR Stock Slips After Bitmine Buys Ethereum Dip – Retail Demands 'HYPE-PURR-Style' Rally](https://finance.yahoo.com/markets/crypto/articles/bmnr-stock-slips-bitmine-buys-132744133.html)**

Bitmine announced a fresh purchase of more than 26,000 Ethereum tokens on Monday.

Yahoo Finance • 1d ago

---

**[Bitmine acquires 26,497 ETH as it targets a slower approach to 5% of Ethereum's total supply](https://www.theblock.co/post/403203/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-total-supply)**

Bitmine Chairman Tom Lee said the company would reach its 5% acquisition target of Ethereum's total supply "sometime in 2026."

The Block • 1d ago

---

**[Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.42 Million Tokens, and Total Crypto and Total Cash Holdings of $11.6 Billion](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-42-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-6-billion-302786720.html)**

Bitmine owns 4.49% of the total ETH coin supply of 120.7 million Bitmine is 90% of the way to the 'Alchemy of 5%' in just 11 months Ethereum continues to...

PR Newswire • 1d ago

---

**[Bitcoin and ethereum prices today, June 2, 2026: Bitcoin's lowest open since April, prices falling further](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-june-2-2026-bitcoins-lowest-open-since-april-prices-falling-further-132451193.html)**

Bitcoin opened at $71,320.49 today, down 3.1% from yesterday’s opening price. The price of bitcoin fell further,  reaching $68,936.01 as of 8:57 a.m. Ethereum opened at $2,003.78, flat compared to yesterday’s opening price. The price of ethereum was fell as well this morning, moving to $1,972.99 as of 8:57 a.m. ET.

Yahoo Finance • 6h ago

---

**[Ethereum Signals Strength As Citigroup Eyes $5.5 Trillion Tokenized Asset Boom](https://www.tradingview.com/news/newsbtc:762347f60094b:0-ethereum-signals-strength-as-citigroup-eyes-5-5-trillion-tokenized-asset-boom/)**

Ethereum’s funding rate climbed to its highest level since August 23, 2025 on May 31, even as the token slipped below the $2,000 mark. The move pointed to heavy long positioning, and that crowding showed up again on June 1 when about $84 million in long ETH bets were wiped out.Citigroup Sees Tokeni…

TradingView • 4h ago

---

**[Ethereum staking rate hits all-time high of 32.42%: Supply tightens, price falls](https://seekingalpha.com/news/4599700-ethereum-staking-rate-hits-all-time-high-of-3242-supply-tightens-price-falls)**

Ethereum staking hits a record 32% with 39M ETH locked, shrinking supply amid volatility and big liquidations.

Seeking Alpha • 6h ago

---

**[Ethereum Is Winning But Token Holders Are Losing Faith In What Comes Next](https://www.forbes.com/sites/astanley/2026/05/30/ethereum-is-winning-but-its-token-holders-are-losing-faith/)**

Ethereum the network has become the financial infrastructure its supporters always dreamed of. But ETH the token has taken a different turn

Forbes • 2d ago

---

**[Crypto Crash Alert: Why Tom Lee Remains Bullish For Bitcoin and Ethereum](https://coinpedia.org/news/crypto-crash-alert-why-tom-lee-remains-bullish-for-bitcoin-and-ethereum/)**

The crypto market is seeing renewed volatility, with Bitcoin trading at around $70,722 after falling 4.23% in just 16 hours. Ethereum is hovering near

Coinpedia • 14h ago

---

**[How Cheaper Fees Could Drive Ethereum Growth](https://etfdb.com/coinshares-crypto-etf-hub/coinshares-channel/cheaper-fees-may-drive-ethereum/)**

ETF Database • 4h ago

---

---

## YouTube Videos: "ethereum"

**[The Billion Dollar Plan To Save Ethereum](https://www.youtube.com/watch?v=U0qHKPoSqHs)**

Ethereum's lead researcher says the Foundation is broken and proposes a $1 billion ETH advocacy fund. We break down his plan ...

📺 Coin Bureau

👁️ 8K • 👍 460 • 💬 51 • ⏱️ 17:48 • 5h ago

---

**[This Is &quot;Just The Beginning&quot; For XRP Bitcoin Ethereum SUPERCYCLE &amp; Cardano ADA Begins To Collapse](https://www.youtube.com/watch?v=f8XivNTF0rs)**

Investors will only wait so long before they begin to move onto bigger and better blockchains. As we enter a brand new era is ...

📺 The Modern Investor

👁️ 5K • 👍 652 • 💬 239 • ⏱️ 38:50 • 10h ago

---

**[The Crypto Dump Is Just Beginning! Prepare For Mega Buying Opportunities [ETH &amp; SOL Targets]](https://www.youtube.com/watch?v=wCjGHHZJErQ)**

The crypto dump is just beginning, but Sheldon is here to show you why this crash is actually the ultimate mega buying ...

📺 Crypto Banter

👁️ 7K • 👍 402 • 💬 18 • ⏱️ 16:30 • 10h ago

---

**[WHY ETH WILL SURPRISE EVERYONE! (Ethereum Update)](https://www.youtube.com/watch?v=AS2o_Yy1cAA)**

ETHEREUM ETH PRICE PREDICTION 2026 Join the Premium Signal Group for trade setups, mentorship & a community ...

📺 Cilinix Crypto

👁️ 770 • 👍 30 • ⏱️ 4:17 • 10h ago

---

**[🛑TRUMP IRAN🛑 XRP BTC ETH BAD NEWS](https://www.youtube.com/watch?v=6jOYuaOqLk8)**

xrp #bitcoin #hbar #xlm #eth Quality or Cheap merch, you vote here     ...

📺 CRYPTO with KLAUS

👁️ 4K • 👍 327 • 💬 105 • ⏱️ 13:29 • 1d ago

---

**[Is the Bitcoin Thesis Broken? Tom Lee Weighs In](https://www.youtube.com/watch?v=NQuKKchNTu4)**

Tom Lee joins 'Squawk Box' to discuss the latest market trends, impact of AI, market outlook, state of crypto, and more.

📺 Fundstrat

👁️ 51K • 👍 1K • 💬 317 • ⏱️ 7:41 • 1d ago

---

**[Bitcoin &amp; Ethereum at Key Support: Is the Crypto Bounce Coming?](https://www.youtube.com/watch?v=63VYWs9GuNs)**

Head Trader Benjamin Poole breaks down key support levels and bounce setups across four major crypto charts — Bitcoin, ...

📺 Verified Pro Traders

👁️ 3K • 👍 234 • 💬 33 • ⏱️ 9:19 • 21h ago

---

**[BITCOIN CRASH: This Will Get UGLY (whales selling)!!! - Bitcoin News Today, Ethereum &amp; Altcoins](https://www.youtube.com/watch?v=OtRwO6NlKds)**

BITCOIN CRASH: This Will Get UGLY (whales selling)!!! - Bitcoin News Today, Ethereum & Altcoins ⭐ *WEEX* ...

📺 Crypto World

👁️ 8K • 👍 297 • 💬 288 • ⏱️ 23:27 • 17h ago

---

**[HUGE SIGNAL FOR ETHEREUM AND ALTCOINS 📈 JUNE 2 $ETH](https://www.youtube.com/watch?v=VVsuUNXDOKc)**

HUGE SIGNAL FOR ETHEREUM AND ALTCOINS JUNE 2 $ETH.

📺 Overkill Trading

👁️ 335 • 👍 20 • 💬 1 • ⏱️ 2:59 • 2h ago

---

**[8,000억 청산, ETH·XRP에 돈이 움직인다](https://www.youtube.com/watch?v=rAYeiyVnE-4)**

이란 리스크와 호르무즈 해협 긴장이 다시 시장을 흔들면서 비트코인이 7만1000달러 초반까지 급락하고 대규모 롱 포지션 청산이 ...

📺 머니 블라블라

👁️ 12K • 💬 4 • ⏱️ 15:58 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
