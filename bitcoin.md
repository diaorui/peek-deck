---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-08-07T08:14:07.145708+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- social
- videos
- cryptocurrency
- news
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** August 07, 2026 at 08:14 UTC  
**HTML Version:** [bitcoin.html](https://peekdeck.ruidiao.dev/bitcoin.html)

---

## Table of Contents

1. [Bitcoin Price](#bitcoin-price)
2. [Bitcoin Chart](#bitcoin-chart)
3. [Bitcoin Market Stats](#bitcoin-market-stats)
4. [Fear & Greed Index](#fear--greed-index)
5. [Reddit: r/Bitcoin](#reddit-rbitcoin)
6. [Google News: "bitcoin"](#google-news-bitcoin)
7. [HackerNews: "bitcoin"](#hackernews-bitcoin)
8. [YouTube Videos: "bitcoin"](#youtube-videos-bitcoin)

---

## Bitcoin Price

### $64,391.13

---

## Bitcoin Chart

**24h:** -0.5%  
**7d:** +2.5%  
**30d:** +1.7%  
**90d:** -21.7%  
**1y:** -45.0%  

---

## Bitcoin Market Stats

**Market Cap:** $1290.32B
Rank #1

**Circulating Supply:** 20,066,784 BTC
95.6% of max

**All-Time High:** $126,080.00
-49.0%

**All-Time Low:** $67.81
+94740.0%

---

## Fear & Greed Index

### 29
**FEAR**

---

## Reddit: r/Bitcoin

**[SpaceX Reports $540 Million Loss On Bitcoin Holdings](https://www.reddit.com/r/Bitcoin/comments/1vg885b/spacex_reports_540_million_loss_on_bitcoin/)**

SpaceX (NASDAQ: $SPCX) has reported a $540 million U.S. paper loss on its Bitcoin (CRYPTO: $BTC) holdings.

🔗 [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/spacex-reports-540-million-loss-134200453.html) • 1d ago

---

**[Coldcard Thief Starts Mixing 64 BTC](https://www.reddit.com/r/Bitcoin/comments/1vg1rlc/coldcard_thief_starts_mixing_64_btc/)**

https://xcancel.com/LightningNewsX/status/2084923135174844805#m

1d ago

---

**[Legit Feelings Right There](https://www.reddit.com/r/Bitcoin/comments/1vg46a3/legit_feelings_right_there/)**

Hacker keeps getting message, I wonder if they really found his location.

1d ago

---

**[Every cycle](https://www.reddit.com/r/Bitcoin/comments/1vgblzi/every_cycle/)**

1d ago

---

**[What's ColdCard's CEO doing during an emergency? He's on X, Deleting posts](https://www.reddit.com/r/Bitcoin/comments/1vfxsv0/whats_coldcards_ceo_doing_during_an_emergency_hes/)**

NVK is currently deleting old posts from 2020 to try to clean up the history. Screenshot them while you can. They will all be gone soon.

🔗 [X (formerly Twitter)](https://x.com/zherbert/status/2083377265593692242) • 2d ago

---

**[Retirement Attack: Many more details pointing straight to the CEO and CTO stealing the coins. This is more than enough evidence of probable cause to charge them and start a prosecution.](https://www.reddit.com/r/Bitcoin/comments/1vfvogm/retirement_attack_many_more_details_pointing/)**

https://x.com/inverse_hanlon/status/2084689208627925384 A CEO who dismissed the threat by name, a pseudonym that turned out to be the CTO, two warnings four years apart, and a company whose entire answer was that it would have already known. They Sold the Warning On 21 December 2020 (22 Dec UTC), replying to Bitcoin security researcher Michael Flaxman, who had just posted about hardware wallets eliminating the risk of a retirement attack during seed generation and Rodolfo Novak “NVK” addressed the question head on. My money is on people screwing themselves out of their BTC before any vendor tries a retirement attack.Alternatively people could just use dice ;) Ten weeks later on 1 March 2021, Coinkite’s CTO shipped a commit titled “First pass w/ libNgU” that routed Coldcard’s seed generation into a software pseudorandom number generator seeded from the device’s serial number and a clock. NVK’s threat model in December 2020 pointed outward. Users were the risk. Vendors were not. Ten weeks after he said so his co-founder shipped the vendor version and it stayed shipped for five years. The dice line is the other half: He offered it with a wink and it turned out to be the only thing standing between his customers and total loss. Oops They sold it again On 10 October 2021: seven months into shipping the defect the official Coldcard account posted that Coldcard makes retirement attacks impossible. Someone in the replies asked what a retirement attack was. Coinkite answered it themselves. It’s when the project makers could have a “bug” in the entropy generation for later retrieval. Their scare quotes not mine. By then somebody had already tried to warn them. The escape hatch was optional on purpose Look at what that 2021 post was actually selling: Dice rolls. The documentation it linked to still opens with a sentence that reads differently today; if you don’t trust the TRNGs in your COLDCARD, you can introduce your own randomness with dice. At least ninety nine rolls for a full 256 bits. But that setting is “opt in” and sits behind the default that looks fine from the outside.It asks the user to press buttons a hundred times to avoid trusting the manufacturer. Every person who still has their bitcoin took that option, or used a (strong) passphrase, or ran multisig. Every person who got swept trusted the default. That is the architecture a retirement attack requires. You can’t make the mitigation mandatory because then there’s nothing left to collect. You can’t omit it because the paranoid customers will ask why. So you offer it, document it, recommend at least ninety nine rolls, and let the default do the work. When it detonates the record shows you warned your users, therefore neatly covering your tracks if this was an inside job. Coinkite built the structure, warned of the attack it enables, and then pushed a firmware with a backdoor for five years. The pseudonym was the CTO Here is the detail that reorganizes everything else. Coldcard’s crypto ran through libngu, a library on GitHub under the account switck. About six stars. Maintained by one person: apparently pseudonymous. When James O’Beirne audited the firmware that’s what he found: a random number generation for a device holding billions of dollars in bitcoin backed up to what he described as a shady library with six stars maintained solely by a pseudoanon. Dylan LeClair ran GPG verification against that repo and published the output. James O’Beirne then published a full census: fifty-eight commits authored as Switck carry a good signature from Peter D. Gray’s personal key: the same key that signs nineteen other commits in the same repo under Gray’s own name. The key is expired and the signatures are still good. The RNG selection commit is among them. Signed 28 January 2021, switck published no GPG key of they/their own. Peter Gray is Coinkite’s CTO and cofounded the company with NVK. Coinkite has never had more than about twenty people and by most accounts Gray wrote the large majority of the firmware. So switck was Coinkite’s own CTO. Cryptographically proven; not inferred. Every outside reviewer who looked at libngu saw an unaudited third party dependency by an anonymous stranger and worried about supply chain risk. Coinkite’s own people knew it was in house and had no reason to review it as external code. The use of a pseudonym here means that no one audited that chunk of code. Outsiders assumed insiders had. Insiders knew there was no outside to check. They were warned in 2021 Five weeks after the commit on 7 April 2021 someone in a Telegram group flagged the change. Their post sounds in retrospect like a man watching a car roll toward a cliff. Roughly quoting: “The 4.0.x firmware was a radical deviation from every firmware since 2018, with all crypto and BIP39 related code replaced by libNgU. Is it was wise to replace the many-years-old TrezorCrypto code, which has been heavily scrutinized by white hats like Johoe and penetration tested by wallet.fail, with something new. “switck” might be a talented pseudonymous coder, but the commit history is bad” (and they linked to it) The post sat in a Coldcard Telegram group under an embedded NVK tweet about the 4.0.x upgrade: the same tweet in which he said he doesn’t check Telegram. That warning posted five weeks after the defect shipped was correct in every single way. Five years and four months before the money starting mysteriously leaving peoples cold storage. They were warned again in 2025 In May 2025 James O’Beirne audited coldcard/firmware. He wanted to establish conclusively where the RNG was sourced from. He traced it into libngu, found the six-star pseudonymous repo, and was confused about why it was there at all. Because linking libsecp256k1 from Python is easy and that appeared to be the stated purpose. He sent Coinkite a report. In his own words: he had “doubts about whether the true RNG was actually in use”, and he pointed out that the “hardcoded yasmarang constants in libngu were sloppy”. He advised them to rip the whole thing out and link against libsecp256k1 directly. That’s the bug! He identified the exact library, constants, and the question of whether the hardware RNG was being used. And he told them to remove it! Coinkite’s answer, as O’Beirne reports, was that if something was wrong “we’d already know about it by now” and that everything was properly configured for the real boards. That is not a technical response. That is an appeal to their own reputation offered to a developer who had just traced the code and found otherwise. And in a separate post O’Beirne identifies Peter Gray “@DocHex” as “the same guy that shrugged off my report of the possibility of the defect in May 2025.” The same Gray who wrote the library. The same Gray who was switck. There was follow-up of a kind. A Signal group titled “LNGU Clean up” was created on 23 May 2025, with members shown as “n,” “Doc,” “andres,” and one other. Doc-hex is Gray. “n” is NVK. So Coinkite formed a group about cleaning up libNgU and named it after the problem. Then they shipped… nothing! Absolutely no fix fourteen months. The group’s messages were set to disappear after four weeks so whatever was said there is gone, just like the bitcoins that were in hundres of hard working peoples Coldcards. O’Beirne blames himself for not pushing harder. He calls not following up rigorously a horrible mistake on his part. Hold that next to Coinkite’s public explanation which is that an attacker probably used AI to find something nobody could reasonably have caught. The developer who caught it is apologizing. The company that was responsibly informed is blaming the clankers. He didn’t know what was in his own crypto library Coinkite’s technical postmortem is worth reading in full because its author is if nothing else candid. He explains that he set the macro to zero believing it meant neither implementation would be compiled. That is not what it does. And he writes that the bulk of the randomness in the device was coming from a PRNG he did not know was in the codebase at all because it arrived through a submodule. Meanwhile the carefully written hardware TRNG code was still being used, but only by accident and only for things that didn’t matter. He is describing a submodule he wrote. The company selling immunity to entropy tampering did not know which random number generator its product used for five years. The man who says he didn’t know is the man who authored both sides of the mistake. And the answer when it finally surfaced was that libngu XORed one software PRNG against a second software PRNG seeded from constants hardcoded in public source. Two deterministic streams XORed together produce a deterministic stream. The built in health check rejects adjacent repeated values which any nondegenerate PRNG passes without effort. Those are the same hardcoded yasmarang constants O’Beirne told them to rip out. Coldcard seeds generated in that window contained no physical randomness whatsoever. They bought a press release not an audit Peter Todd says Coinkite brought him on in early 2014 as “Chief Naysayer”: an advisory role. Years before the first hardware wallet existed there was a press release. By his account he was given nothing to work on: no tasks, no work to bill for, and then the arrangement quietly dropped. He says it’s still on a LinkedIn profile that he hasn’t logged into in a over decade. His assessment now in his own words: “if they had kept him on and asked him to audit the codebases, there’s a good chance he’d have spotted the practices at issue, and maybe eighty million dollars wouldn’t have been stolen”. He puts that audit at roughly $50k and asks what Coinkite spent on podcast sponsorships instead. The company announced that a famous skeptic was reviewing them and then never asked him to review anything. The press release was the product. All the things they said Coinkite’s public position throughout this crisis has been that it had no idea the flaw existed until the day the money started moving. Two documented warnings and a Signal group named after the problem say otherwise. NVK’s stated position on attribution: they “don’t have full attribution or scope yet”, and they “won’t speculate until the technical evaluation is complete”. Coinkite then suggested publicly that the attacker likely used an automated tool to comb the public source and find the flaw before they did. That’s speculation. This propisition rests on absolutely no evidence. And it happens to be the only theory of the case in which nobody at Coinkite knew and nobody at Coinkite failed. You can decline to speculate or you can float the hypothesis that clears you. Doing both inside the same week tells you which one was the priority. Coinkite told customers it kept purchase data for 90 days. When breach notifications went out they reached buyers going back to 2019. Challenged, the company pointed at a policy page, conceded it has no deletion schedule and said the addresses would be kept “for now.” A verifiable lie caught within a few days of the largest breach of trust in hardware wallet history, and on a question where the answer was easily verifiable. This speaks volumes of NVK’s character. The fix broke too On 31 July Coinkite shipped out an emergency firmware update. Three days later a contributor opened pull request #692 against the Coldcard firmware repo, reporting that the hotfix had introduced a new failure on the hardware RNG path. The entropy fix itself is correct: rng_get() now resolves to the board’s true hardware accessor instead of the software fallback. But rng_get_or_fault() had no recovery path for the STM32’s RNG seed error flags. After a seed error the peripheral stops delivering data and the shipped code never clears the condition; so every later call times out and raises OSError(EFAULT) for the rest of that boot. Because rng_get() now sits on the keypad scan path (an interrupt callback that runs before login) that exception lands before the PIN prompt. Power cycling clears the flags; if the error recurs on the next boo: the user is locked out of the upgrade menu too and the device is essentially bricked. The original report overstated the stickiness. The flags do not survive a power cycle: so this is not a permanent brick from a single glitch. It is still a serious regression: an emergency patch for a five-year review failure shipped fast that can take the device down before the user can enter a PIN. 692 was closed in favor of #693, a cleaner recovery sequence from a Coinkite contributor, with #698 as the Mk3 follow-up. Both were still open when this was written. The point is not that nobody noticed. The point is that the first hotfix for a five-year entropy failure needed a second round of patches within days. Giving the attacker MORE TIME to execute sweeping funds from vulnerable wallets. What they’ll say Three objections are coming, and they’re the ones I’d make if I was NVK for sure Galaxy says the waves may not share an operator. True: and irrelevant to the part that matters. Galaxy’s caution is about waves two, three, and four. Once wave one went loud on 30 July the vulnerability was public property and anyone with tooling could pile in. That’s what waves three and four look like. Wave one is the one that tells you something. 1,082 BTC out of 1,195 addresses in 41 minutes with seeds already computed; executed by someone who had been preparing while nobody else on earth knew there was anything to prepare for. The bug was publicly findable: anyone could have found it. Two people found it in public and said so, in 2021 and in 2025. Both were told it was fine. The set of people who knew this was a live question before 30 July is not the general public. It’s a short list and Coinkite was on it. A mass sweep is too loud for an insider. It’s too loud for the rational insider who bleeds quietly over years and never triggers a referral. The loudness cuts against a careful inside job. It does not erase the warnings, the Signal group, or their response that if something was wrong they’d already know. What I think happened Somebody inside that company knew what was sitting in the codebase and knew what it was worth. Look at the timeline: Ten weeks before the bug shipped the CEO publicly waved off the idea that a vendor would ever run a retirement attack and pointed at dice as the alternative. His co-founder and CTO then wrote a crypto library under a pseudonymous GitHub account with about six stars, and shipped the device’s entire randomness path through it. Five weeks later someone flagged the swap in a Coldcard Telegram group and was ignored. Seven months after that the company marketed immunity to the exact attack class the defect enables and made the only reliable defense an “opt in”. Four years in: a Bitcoin developer audited the firmware found the library, named the hardcoded constants, told them to remove the whole thing, and was told they’d already know if something was wrong. They opened a Signal group called “LNGU Clean up,” set the messages to disappear, and shipped nothing. Coins were leaving through 695 transactions nobody noticed. Then somebody who had been precomputing seeds for a long time took 1,082 BTC in 41 minutes. Each of these has an innocent explanation available. All of them stacked in the same direction inside a company of twenty people. This is not a run of bad luck. Inverse Hanlon’s razor exists for exactly this shape: when incompetence needs that many separate coincidences to line up the same way the incentive is the simpler explanation. I can’t say for 100% it was an inside job of course: every document that would definititevly prove it belongs to them. The “LNGU Clean up” thread, whatever survived a four week expiration. Whatever code review they ran and when. The commit history around anyone who touched rng.c after May 2025. Roughly 600 attacker addresses are already in front of federal investigators and Coinkite says it’s cooperating. Cooperation is cheap. Coinkite has apologized, published a postmortem, shipped a fix that needed a second round of patches within days, and offered its customers not a single sat as compensation. The man who found this in May 2025 is publicly apologizing for not pushing harder. And NVK is blaming AI. The people who still have their bitcoins are the ones who read Coldcard’s own documentation, saw the line offering them a way to distrust the manufacturer’s randomness, and took it. Nobody told them that one sentence in the docs was the difference between keeping their money and losing it.

2d ago

---

**[[GER] Petition for Bundestag: Beibehaltung der steuerlichen Haltefrist für Bitcoin](https://www.reddit.com/r/Bitcoin/comments/1vgaw3p/ger_petition_for_bundestag_beibehaltung_der/)**

There is an active petition for keeping Bitcoin tax free in Germany (after one year hodling). It reached 21.000 signatures within the first 24 hours - let's make it 30.000 to put it on the agenda of german Bundestag. You need to sign up in order to put your signature but it's worth it. Everyone can sign - not just germans! https://epetitionen.bundestag.de/petitionen/_2026/_05/_30/Petition_201716.nc.html Thank you!

1d ago

---

**[Wow, Bitcoin just delivered one of the biggest on-chain performances ever!](https://www.reddit.com/r/Bitcoin/comments/1vg85pg/wow_bitcoin_just_delivered_one_of_the_biggest/)**

The network processed 20,364,529 transactions in July 2026, making it the second-best month in entire history by transaction count. As new users, institutions, and Bitcoin-native applications continue to arrive, on-chain activity keeps pushing toward record territory. We think that, it's a remarkable achievement for a network that has been operating for more than 17 years and continues to reach new milestones. Congratulations to everyone contributing to the Bitcoin ecosystem!

1d ago

---

**[Coinkite](https://www.reddit.com/r/Bitcoin/comments/1vfyzcd/coinkite/)**

2d ago

---

**[Coinkite CTO Peter Gray linked to the code behind the $114M Coldcard hack](https://www.reddit.com/r/Bitcoin/comments/1vfpadi/coinkite_cto_peter_gray_linked_to_the_code_behind/)**

Researchers have tied the faulty randomness code at the center of the Coldcard wallet breach to Coinkite co-founder and CTO Peter Gray, who Bitcoin developer

🔗 [Cryptopolitan](https://www.cryptopolitan.com/coinkite-cto-peter-gray-linked-coldcard-hack/) • 2d ago

---

---

## Google News: "bitcoin"

**[Breez Glow Brings Passkeys And Stablecoins To Bitcoin Wallets](https://bitcoinmagazine.com/business/breez-announces-glow-an-open-source-bitcoin-to-stablecoins-progressive-web-app)**

The MIT-licensed progressive web app, built with Breez SDK and Spark, lets users send USDT and USDC from a Bitcoin balance while supporting native Lightning payments and Passkey login.

Bitcoin Magazine • 12h ago

---

**[CryptoQuant says bitcoin, ether and XRP whales are accumulating, signaling a 'late-stage bear market'](https://www.theblock.co/post/410920/cryptoquant-bitcoin-ether-xrp-whales-accumulating-late-stage-bear-market)**

Large crypto holders are accumulating bitcoin, ether, and XRP as prices remain under pressure, CryptoQuant said.

theblock.co • 1d ago

---

**[S&P 500 Adds $2.1 Trillion in a Month as Bitcoin Stalls Near $64K — What Is Holding BTC Back?](https://bitcoinfoundation.org/news/bitcoin/sp-500-adds-2-1-trillion-in-a-month-as-bitcoin-stalls-near-64k-what-is-holding-btc-back/)**

S&P 500 adds $2.1T as Bitcoin stalls near $64K, with AI-led stocks, ETF flows, bond yields and crypto-specific pressure limiting BTC upside.

Bitcoin Foundation • 45m ago

---

**[Bitcoin Whales Snap Up $1.2 Billion Worth of BTC as ETF Inflows Surge Toward Four-Month High](https://bitcoinfoundation.org/news/bitcoin/bitcoin-whales-snap-up-1-2-billion-worth-of-btc-as-etf-inflows-surge-toward-four-month-high/)**

Bitcoin whales accumulated $1.2B in BTC while U.S. spot ETFs attracted $754M, reinforcing institutional demand despite regulatory uncertainty.

Bitcoin Foundation • 15m ago

---

**[BTC news: Early bitcoin wallet wakes after 15 years with $3.2 million transfer](https://www.coindesk.com/markets/2026/08/07/bitcoin-wallet-dormant-since-2011-moves-usd3-2-million-toward-falconx-linked-address)**

The 50 BTC remained in the receiving address Friday, but that wallet has previously sent funds to FalconX-labeled deposits, leaving open whether the old stash is being reorganized or moved closer to a trading venue.

CoinDesk • 3h ago

---

**[Hacked Bitcoin Wallet Maker Declines to Estimate Amount Lost](https://www.bloomberg.com/news/articles/2026-08-06/hacked-bitcoin-wallet-maker-declines-to-estimate-amount-lost)**

Bloomberg.com • 12h ago

---

**[What we know about ongoing Coldcard hack that's stolen over $100M worth of bitcoin](https://www.cbc.ca/news/world/bitcoin-coinkite-security-hack-9.7295582)**

A Toronto-based company that made Coldcard, a bitcoin-only hardware wallet that has been the latest target of a data breach, 
has reportedly lost $100 million US worth of bitcoin as a result of the hack.

CBC • 2d ago

---

**[Hack of Supposedly Safe Bitcoin Tool Tries Faith of the Devoted](https://finance.yahoo.com/markets/crypto/articles/hack-supposedly-safe-bitcoin-tool-024624179.html)**

(Bloomberg) -- Tim Lamb was vacationing in the Channel Islands with his family last week when news of the cryptocurrency hack reached him. He faced a quandary: whether to rush home and check on his Bitcoin, or finish the trip.Most Read from BloombergIran Says Agreement on Hormuz Shipping Reached With OmanOpenAI’s New Device Will Be Hockey Puck-Sized and Cost Over $300Iran Wants to Bar US, Israeli Ships From Hormuz in Peace AccordIshbia’s Mortgage Firm Suffers Record Drop on Dividend HaltWhy Do D

Yahoo Finance • 5h ago

---

**[St. Louis trio charged in plot targeting $245 million Bitcoin fortune](https://fox2now.com/news/missouri/st-louis-trio-charged-in-plot-targeting-245-million-bitcoin-fortune/)**

Three St. Louis men were part of a plan to kidnap a cryptocurrency investor and potentially steal hundreds of millions of dollars in Bitcoin, according to newly-filed criminal charges.

FOX 2 • 13h ago

---

**[Eric Trump-Led American Bitcoin To Adopt Michael Saylor’s Approach of Selling BTC to Support Economics? CEO Says…](https://finance.yahoo.com/markets/crypto/articles/eric-trump-led-american-bitcoin-223120136.html)**

American Bitcoin Corp. CEO Mike Ho sidestepped questions on Monday about selling Bitcoin to fund equity buybacks, a move some other companies in the industry have pursued. American Bitcoin’s ‘North Star’ During American Bitcoin’s second-quarter earnings call, Ho was questioned...

Yahoo Finance • 1d ago

---

---

## HackerNews: "bitcoin"

**[Bitcoin cold-wallet attack spreads to 4,500 addresses as losses near $89M](https://news.ycombinator.com/item?id=49149222)**

Galaxy Research flagged a third wave of sweeps tied to weak Coldcard-generated keys, with the attacker now targeting smaller balances and changing how funds are collected onchain.

⬆️ 70 • 💬 23 • 4d ago • [coindesk.com](https://www.coindesk.com/tech/2026/08/02/bitcoin-cold-wallet-attack-spreads-to-4-500-addresses-as-losses-near-usd89-million)

---

**[Coldcard wallet RNG flaw likely linked to $88M Bitcoin theft](https://news.ycombinator.com/item?id=49148905)**

A vulnerability in COLDCARD hardware wallet firmware allowed attackers to steal an estimated $88.6 million in Bitcoin from thousands of wallets whose seeds were generated using a flawed random number generator.

⬆️ 20 • 💬 0 • 4d ago • [BleepingComputer](https://www.bleepingcomputer.com/news/security/coldcard-wallet-rng-flaw-likely-linked-to-88-million-bitcoin-theft/)

---

**[U.S. sanctions Iranian firms for Bitcoin maritime insurance operation in Hormuz](https://news.ycombinator.com/item?id=49141295)**

OFAC Sanctions Illicit Maritime Insurance Scheme and Iran’s Shadow Fleet  WASHINGTON—Today, the U.S. Department of the Treasury’s Office of Foreign Assets Control (OFAC) is taking further action against the Iranian regime’s desperate efforts to monetize the Strait of Hormuz and prop up the nation’s failing economy.  OFAC is designating two firms integral to an Islamic Revolutionary Guard Corps (IRGC)-backed extortion scheme that forces commercial vessels to purchase mandatory maritime “insurance” to transit the Strait.  Although this coverage purports to protect vessels from risks such as seizures, these risks are overwhelmingly created by Iran itself.  Through the Persian Gulf Marine Insurance Company and HormuzSafe Marine Services Authority, the regime brokers IRGC-approved policies designed to extract revenue under the guise of maritime services, including payments in digital assets to evade sanctions—allowing Iran to tighten control over shipping activity and funnel funds into IRGC operations.“With its economy in freefall and inflation in the triple digits, the regime is desperate for cash,” said Secretary of the Treasury Scott Bessent. “The United States will not allow Iran to hold global commerce hostage or use international shipping to finance the IRGC’s terrorism, aggression, and repression.”                            OFAC is also reinforcing U.S. military interdiction efforts and intensifying pressure on Iran’s energy shipments by imposing sanctions on several vessels that transported Iranian crude oil and petrochemical products.  Since the beginning of the year, OFAC has sanctioned over 100 vessels linked to Iran’s shadow fleet, a covert logistics network that enables the regime to keep oil revenues flowing despite international sanctions. Today’s action was taken pursuant to Executive Order (E.O.) 13902, which targets Iran’s petroleum and petrochemical sectors and advances the President’s National Security Presidential Memorandum 2 (NSPM-2), to impose maximum economic pressure on Iran. IRANIAN Regime’s EXTORTION SCHEMEIn an attempt to prop up revenue streams decimated by Operation Epic Fury, Iran has established illegitimate schemes through the Persian Gulf Marine Insurance Company (PGMIC) and HormuzSafe Marine Services Authority, also known as Hormuz Safe, to extort vessels attempting to conduct routine commercial passages through the Strait of Hormuz.  Established by the Central Insurance of the Islamic Republic of Iran, Iran’s primary insurance regulator, the PGMIC brokers and issues insurance policies approved by the U.S.-designated, IRGC-backed Persian Gulf Strait Authority (PGSA).  The insurance covers risks, most of which are created by Iran itself, such as vessel seizures, and aims to generate revenue to fund the regime’s terror and corruption. PGSA was designated pursuant to E.O. 13224, as amended, on May 27, 2026 for having materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services to or in support of, the IRGC. Hormuz Safe is an Iranian digital insurance firm that advertises itself as a company offering trusted maritime services, including insurance, traffic control, security, and emergency response, to vessels transiting the Strait of Hormuz.  Developed by Iran’s Ministry of Economy, it accepts payment in Bitcoin and other digital assets as part of the regime’s attempts to bypass Western sanctions. Disgraced regime financier Babak Morteza Zanjani, who was sanctioned earlier this year, promoted Hormuz Safe to his social media followers.  Hormuz Safe generates revenue on behalf of the IRGC in an attempt to give the regime tighter control over shipping activity. The Persian Gulf Marine Insurance Company and HormuzSafe Marine Services Authority are being designated pursuant to E.O. 13902 for operating in the financial sector of the Iranian economy. shadow fleet ACTORSTreasury is also taking action today against multiple shadow fleet vessels responsible for transporting millions of barrels of Iranian crude oil and petroleum products.  Iran’s shadow fleet provides an essential lifeline to the Iranian regime, which relies on oil sales to bolster its ailing economy. The Marshall Islands-flagged chemical/products tanker WELL SAIL (IMO 9321938), owned, operated, and managed by China-based Qi Hang Ship Management Limited, has transported hundreds of thousands of barrels of Iranian petroleum products to the United Arab Emirates (UAE) in 2026. The Mozambique-flagged crude oil tanker LILY (IMO 9294331), owned and operated by Hong Kong-based Confident Apex Limited, has transported millions of barrels of Iranian oil since 2025.The unknown-flagged crude oil tanker AL SALMI (IMO 9298296), owned and operated by Hong Kong-based Billion Nexus Int’l Co., Limited, has transported hundreds of thousands of barrels of Iranian oil to China since 2025.The Barbados-flagged crude oil tanker BREEZE V (IMO 9259355), owned and operated by Hong Kong-based Nevada Spirit Company Limited, has transported millions of barrels of Iranian oil to China in 2026. The Barbados-flagged crude oil tanker NATSUMI (IMO 9331244), owned, operated, and managed by Hong Kong-based Marinova Freight Limited, has transported millions of barrels of Iranian crude oil to China since 2022. The Vanuatu-flagged crude oil tanker CRYSTAL (IMO 9223887), owned, operated, and managed by Hong Kong and Marshall Islands-based Vast Mighty Limited, has transported millions of barrels of Iranian crude oil to China in 2026. The Vanuatu-flagged crude oil tanker NIRETA (IMO 9237785), owned, operated, and managed by Marshall Islands-based Ocean Tranquility Limited, has transported hundreds of thousands of barrels of Iranian crude oil to China in 2026. The Barbados-flagged crude oil tanker YEHOPE (IMO 9243320), owned by Marshall Islands-based Branch Saying International Trading Co Ltd, has transported hundreds of thousands of barrels of Iranian crude oil to China in 2026.   The following companies are being designated pursuant to E.O. 13902 for operating in the petroleum sector of the Iranian economy: Qi Hang Ship Management Limited;Marinova Freight Limited;Vast Mighty Limited;Ocean Tranquility Limited; Branch Saying International Trading Co Ltd;Confident Apex Limited;Billion Nexus Int’l Co., Limited; andNevada Spirit Company Limited.The following vessels are being identified as blocked property of the previously identified blocked persons: WELL SAIL (Qi Hang Ship Management Limited);NATSUMI (Marinova Freight Limited); CRYSTAL (Vast Mighty Limited); NIRETA (Ocean Tranquility Limited); YEHOPE (Branch Saying International Trading Co Ltd);LILY (Confident Apex Limited);AL SALMI (Billion Nexus Int’l Co., Limited); andBREEZE V (Nevada Spirit Company Limited). SANCTIONS IMPLICATIONSAs a result of today’s action, all property and interests in property of the designated or blocked persons described above that are in the United States or in the possession or control of U.S. persons are blocked and must be reported to OFAC.  In addition, any entities that are owned, directly or indirectly, individually or in the aggregate, 50 percent or more by one or more blocked persons are also blocked.  Unless authorized by OFAC, or exempt, OFAC’s regulations generally prohibit all transactions by U.S. persons or within (or transiting) the United States that involve any property or interests in property of blocked persons. Violations of U.S. sanctions may result in the imposition of civil or criminal penalties on U.S. and foreign persons.  OFAC may impose civil penalties for sanctions violations on a strict liability basis.  OFAC’s Economic Sanctions Enforcement Guidelines provide more information regarding OFAC’s enforcement of U.S. economic sanctions. In addition, financial institutions and other persons may risk exposure to sanctions for engaging in certain transactions or activities involving designated or otherwise blocked persons.  The prohibitions include the making of any contribution or provision of funds, goods, or services by, to, or for the benefit of any designated or blocked person, or the receipt of any contribution or provision of funds, goods, or services from any such person.  Non-U.S. persons are also prohibited from causing or conspiring to cause U.S. persons to wittingly or unwittingly violate U.S. sanctions, as well as engaging in conduct that evades U.S. sanctions.  Individuals located in the U.S. or abroad who provide information about sanctions violations to FinCEN’s whistleblower incentive program may be eligible for awards if the information they provide leads to a successful enforcement action that results in monetary penalties exceeding $1,000,000. The power and integrity of OFAC sanctions derive not only from OFAC’s ability to designate and add persons to the SDN List, but also from its willingness to remove persons from the SDN List consistent with the law.  The ultimate goal of sanctions is not to punish, but to bring about a positive change in behavior.  For information concerning the process for seeking removal from an OFAC list, including the SDN List, or to submit a request, please refer to OFAC’s guidance on Filing a Petition for Removal from an OFAC List.Click here for more information on the persons designated and any property identified as blocked property today.###

⬆️ 10 • 💬 2 • 5d ago • [U.S. Department of the Treasury](https://home.treasury.gov/news/press-releases/sb0581)

---

**[Bitcoin BIP110 mandatory activation this Saturday, how game theory will unfold?](https://news.ycombinator.com/item?id=49180531)**

Where do I stand on BIP-110 and the "spam war"? Discover why I believe this is a strategy of tension, the game theory behind this consensus battle, and why running a node and holding your own keys remains Bitcoin’s ultimate defense against corporate capture.

⬆️ 9 • 💬 4 • 1d ago • [simondixon.com](https://www.simondixon.com/blog/bip-110-the-spam-war-and-the-battle-nobody-wants-to-name-where-i-stand-simon-dixon)

---

**[Has the Bitcoin Moved?](https://news.ycombinator.com/item?id=49160843)**

BitGo's CEO put 100 BTC ($6.3M) in a wallet and dared Anthropic's AI to take it. Live wallet tracker.

⬆️ 8 • 💬 2 • 3d ago • [hasthebitcoinmoved.com](https://hasthebitcoinmoved.com/)

---

**[What we know about ongoing Coldcard hack that's stolen over $100M in Bitcoin](https://news.ycombinator.com/item?id=49174951)**

A Toronto-based company that made Coldcard, a bitcoin-only hardware wallet that has been the latest target of a data breach, 
has reportedly lost $100 million US worth of bitcoin as a result of the hack.

⬆️ 8 • 💬 0 • 2d ago • [CBC](https://www.cbc.ca/news/world/bitcoin-coinkite-security-hack-9.7295582)

---

**[Coldcard Bitcoin Exploit Balloons to $88M as Attackers Keep Draining Wallets](https://news.ycombinator.com/item?id=49147088)**

Galaxy Research says a third wave of thefts from Coldcard Bitcoin wallets has pushed observed losses to roughly $88.6 million worth of BTC.

⬆️ 6 • 💬 1 • 4d ago • [Decrypt](https://decrypt.co/374817/coldcard-bitcoin-exploit-88-million-attackers-draining-wallets)

---

**[Hackers Hit Bitcoin's Safest Hiding Place in Ongoing Attack](https://news.ycombinator.com/item?id=49167125)**

⬆️ 4 • 💬 1 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-08-03/hackers-target-bitcoin-s-safest-hiding-place-in-ongoing-attack)

---

**[After $140M hack, Bitcoin users 'soul-searching' over self-custody](https://news.ycombinator.com/item?id=49179540)**

A coding error in bitcoin wallets made by Coinkite Inc. allowed hackers to steal from individuals storing their own cryptocurrency

⬆️ 3 • 💬 0 • 2d ago • [The Globe and Mail](https://www.theglobeandmail.com/investing/article-after-140-million-hack-bitcoin-users-soul-searching-over-self-custody/)

---

**[What Bitcoin sextortion emails actually earned](https://news.ycombinator.com/item?id=49178750)**

Try out Artifacts created by Claude users

⬆️ 2 • 💬 0 • 2d ago • [claude.ai](https://claude.ai/code/artifact/4806cb5d-8582-460e-ab31-2a321f1b23cb)

---

---

## YouTube Videos: "bitcoin"

**[Bitcoins Move Towards $250k Starts HERE! Bitcoin Price Prediction](https://www.youtube.com/watch?v=1tePMqLARJI)**

Bitcoin is coming — and the setup is forming now. In this video I break down why the next major leg higher in Bitcoin may be ...

📺 Crypto Jebb

👁️ 6K • 👍 359 • 💬 45 • ⏱️ 8:03 • 14h ago

---

**[Don’t Miss What Saylor Said About Bitcoin Today](https://www.youtube.com/watch?v=w2GMdsnSerk)**

AskClash - *AI Tools, Charts, and Agents for Crypto & Markets* ▻ https://www.askclash.ai/ **Exchange Partners** Bitunix ...

📺 CryptosRUs

👁️ 10K • 👍 687 • 💬 105 • ⏱️ 12:39 • 7h ago

---

**[Bitcoin: Where in the Cycle Are We?](https://www.youtube.com/watch?v=CmGkfyot8qY)**

Where in the Bitcoin cycle are we? Come to the 1st ITC Conference: https://www.benjamincowen.com/conference Into The ...

📺 Benjamin Cowen

👁️ 31K • 👍 3K • 💬 203 • ⏱️ 24:00 • 8h ago

---

**[My 15-Year Bitcoin Journey Ends Today](https://www.youtube.com/watch?v=6K2KU_35UJM)**

After mining my very first Bitcoin in 2011 and building multiple million-dollar crypto companies, I've made a decision that took me ...

📺 Filip Martinsson

👁️ 680 • 👍 37 • 💬 29 • ⏱️ 10:08 • 19h ago

---

**[🚨 BITCOIN!!!!!!!! STOP EVERYTHING!!!!!!](https://www.youtube.com/watch?v=80miHxo3Xe4)**

Bitcoin is at a major turning point and could all come down to this! Everyone is wrong? BloFin ...

📺 Crypto Zombie

👁️ 11K • 👍 975 • 💬 131 • ⏱️ 20:41 • 15h ago

---

**[This Could BREAK Bitcoin in 2028.](https://www.youtube.com/watch?v=dSEC1n8TT0Q)**

Could this REALLY break bitcoin in 2028 as Tom Lee suggests? I think EVERYTHING is on the table and we MUST evaluate it ...

📺 Digital Asset News

👁️ 10K • 👍 571 • 💬 97 • ⏱️ 23:41 • 1d ago

---

**[BREAKING: Michael Saylor Just Made A SHOCKING NEW Bitcoin Prediction!](https://www.youtube.com/watch?v=U7HH0v4tbaI)**

BREAKING: Michael Saylor Just Made A SHOCKING NEW Bitcoin Prediction! Earn yield or borrow against your Bitcoin with ...

📺 Luke Mikic

👁️ 5K • 👍 347 • 💬 39 • ⏱️ 38:58 • 12h ago

---

**[Clarity Act DELAYED! What this means for Crypto](https://www.youtube.com/watch?v=BQXrc3OBLBk)**

Crypto is entering a critical decision window as Bitcoin tests major resistance while key regulatory and Ethereum developments ...

📺 Crypto Banter

👁️ 19K • 👍 1K • 💬 33 • ⏱️ 21:53 • 17h ago

---

**[CRYPTO CLARITY ACT Vote! Don&#39;t Get Fooled Too Much By Hype! Here&#39;s the Real Deal!](https://www.youtube.com/watch?v=tn1cJsqINQE)**

Crypto Clarity Act vote likely THIS WEEKEND. Lummis basically just said the Senate isn't leaving for recess without crypto clarity ...

📺 Crypto Capital Venture

👁️ 13K • 👍 678 • 💬 340 • ⏱️ 8:59 • 1d ago

---

**[Man Who Owns 4% Of All Bitcoin: His Final WARNING To Everyone Who Doesn&#39;t Own It | Michael Saylor](https://www.youtube.com/watch?v=1aGpJQ8BMLI)**

Michael made $15 billion last year using ChatGPT, by building something that has never existed in the history of the world.

📺 The Diary Of A CEO

👁️ 564K • 👍 17K • 💬 3K • ⏱️ 1:39:55 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
