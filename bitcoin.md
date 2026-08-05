---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-08-05T17:37:50.842023+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- news
- videos
- cryptocurrency
- social
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** August 05, 2026 at 17:37 UTC  
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

### $64,511.84

---

## Bitcoin Chart

**24h:** +0.5%  
**7d:** -0.3%  
**30d:** +2.0%  
**90d:** -19.5%  
**1y:** -43.9%  

---

## Bitcoin Market Stats

**Market Cap:** $1294.78B
Rank #1

**Circulating Supply:** 20,066,115 BTC
95.6% of max

**All-Time High:** $126,080.00
-48.8%

**All-Time Low:** $67.81
+95040.8%

---

## Fear & Greed Index

### 27
**FEAR**

---

## Reddit: r/Bitcoin

**[SpaceX Reports $540 Million Loss On Bitcoin Holdings](https://www.reddit.com/r/Bitcoin/comments/1vg885b/spacex_reports_540_million_loss_on_bitcoin/)**

SpaceX (NASDAQ: $SPCX) has reported a $540 million U.S. paper loss on its Bitcoin (CRYPTO: $BTC) holdings.

🔗 [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/spacex-reports-540-million-loss-134200453.html) • 3h ago

---

**[Coldcard Thief Starts Mixing 64 BTC](https://www.reddit.com/r/Bitcoin/comments/1vg1rlc/coldcard_thief_starts_mixing_64_btc/)**

https://xcancel.com/LightningNewsX/status/2084923135174844805#m

8h ago

---

**[Legit Feelings Right There](https://www.reddit.com/r/Bitcoin/comments/1vg46a3/legit_feelings_right_there/)**

Hacker keeps getting message, I wonder if they really found his location.

6h ago

---

**[Every cycle](https://www.reddit.com/r/Bitcoin/comments/1vgblzi/every_cycle/)**

1h ago

---

**[What's ColdCard's CEO doing during an emergency? He's on X, Deleting posts](https://www.reddit.com/r/Bitcoin/comments/1vfxsv0/whats_coldcards_ceo_doing_during_an_emergency_hes/)**

NVK is currently deleting old posts from 2020 to try to clean up the history. Screenshot them while you can. They will all be gone soon.

🔗 [X (formerly Twitter)](https://x.com/zherbert/status/2083377265593692242) • 12h ago

---

**[Retirement Attack: Many more details pointing straight to the CEO and CTO stealing the coins. This is more than enough evidence of probable cause to charge them and start a prosecution.](https://www.reddit.com/r/Bitcoin/comments/1vfvogm/retirement_attack_many_more_details_pointing/)**

https://x.com/inverse_hanlon/status/2084689208627925384 A CEO who dismissed the threat by name, a pseudonym that turned out to be the CTO, two warnings four years apart, and a company whose entire answer was that it would have already known. They Sold the Warning On 21 December 2020 (22 Dec UTC), replying to Bitcoin security researcher Michael Flaxman, who had just posted about hardware wallets eliminating the risk of a retirement attack during seed generation and Rodolfo Novak “NVK” addressed the question head on. My money is on people screwing themselves out of their BTC before any vendor tries a retirement attack.Alternatively people could just use dice ;) Ten weeks later on 1 March 2021, Coinkite’s CTO shipped a commit titled “First pass w/ libNgU” that routed Coldcard’s seed generation into a software pseudorandom number generator seeded from the device’s serial number and a clock. NVK’s threat model in December 2020 pointed outward. Users were the risk. Vendors were not. Ten weeks after he said so his co-founder shipped the vendor version and it stayed shipped for five years. The dice line is the other half: He offered it with a wink and it turned out to be the only thing standing between his customers and total loss. Oops They sold it again On 10 October 2021: seven months into shipping the defect the official Coldcard account posted that Coldcard makes retirement attacks impossible. Someone in the replies asked what a retirement attack was. Coinkite answered it themselves. It’s when the project makers could have a “bug” in the entropy generation for later retrieval. Their scare quotes not mine. By then somebody had already tried to warn them. The escape hatch was optional on purpose Look at what that 2021 post was actually selling: Dice rolls. The documentation it linked to still opens with a sentence that reads differently today; if you don’t trust the TRNGs in your COLDCARD, you can introduce your own randomness with dice. At least ninety nine rolls for a full 256 bits. But that setting is “opt in” and sits behind the default that looks fine from the outside.It asks the user to press buttons a hundred times to avoid trusting the manufacturer. Every person who still has their bitcoin took that option, or used a (strong) passphrase, or ran multisig. Every person who got swept trusted the default. That is the architecture a retirement attack requires. You can’t make the mitigation mandatory because then there’s nothing left to collect. You can’t omit it because the paranoid customers will ask why. So you offer it, document it, recommend at least ninety nine rolls, and let the default do the work. When it detonates the record shows you warned your users, therefore neatly covering your tracks if this was an inside job. Coinkite built the structure, warned of the attack it enables, and then pushed a firmware with a backdoor for five years. The pseudonym was the CTO Here is the detail that reorganizes everything else. Coldcard’s crypto ran through libngu, a library on GitHub under the account switck. About six stars. Maintained by one person: apparently pseudonymous. When James O’Beirne audited the firmware that’s what he found: a random number generation for a device holding billions of dollars in bitcoin backed up to what he described as a shady library with six stars maintained solely by a pseudoanon. Dylan LeClair ran GPG verification against that repo and published the output. James O’Beirne then published a full census: fifty-eight commits authored as Switck carry a good signature from Peter D. Gray’s personal key: the same key that signs nineteen other commits in the same repo under Gray’s own name. The key is expired and the signatures are still good. The RNG selection commit is among them. Signed 28 January 2021, switck published no GPG key of they/their own. Peter Gray is Coinkite’s CTO and cofounded the company with NVK. Coinkite has never had more than about twenty people and by most accounts Gray wrote the large majority of the firmware. So switck was Coinkite’s own CTO. Cryptographically proven; not inferred. Every outside reviewer who looked at libngu saw an unaudited third party dependency by an anonymous stranger and worried about supply chain risk. Coinkite’s own people knew it was in house and had no reason to review it as external code. The use of a pseudonym here means that no one audited that chunk of code. Outsiders assumed insiders had. Insiders knew there was no outside to check. They were warned in 2021 Five weeks after the commit on 7 April 2021 someone in a Telegram group flagged the change. Their post sounds in retrospect like a man watching a car roll toward a cliff. Roughly quoting: “The 4.0.x firmware was a radical deviation from every firmware since 2018, with all crypto and BIP39 related code replaced by libNgU. Is it was wise to replace the many-years-old TrezorCrypto code, which has been heavily scrutinized by white hats like Johoe and penetration tested by wallet.fail, with something new. “switck” might be a talented pseudonymous coder, but the commit history is bad” (and they linked to it) The post sat in a Coldcard Telegram group under an embedded NVK tweet about the 4.0.x upgrade: the same tweet in which he said he doesn’t check Telegram. That warning posted five weeks after the defect shipped was correct in every single way. Five years and four months before the money starting mysteriously leaving peoples cold storage. They were warned again in 2025 In May 2025 James O’Beirne audited coldcard/firmware. He wanted to establish conclusively where the RNG was sourced from. He traced it into libngu, found the six-star pseudonymous repo, and was confused about why it was there at all. Because linking libsecp256k1 from Python is easy and that appeared to be the stated purpose. He sent Coinkite a report. In his own words: he had “doubts about whether the true RNG was actually in use”, and he pointed out that the “hardcoded yasmarang constants in libngu were sloppy”. He advised them to rip the whole thing out and link against libsecp256k1 directly. That’s the bug! He identified the exact library, constants, and the question of whether the hardware RNG was being used. And he told them to remove it! Coinkite’s answer, as O’Beirne reports, was that if something was wrong “we’d already know about it by now” and that everything was properly configured for the real boards. That is not a technical response. That is an appeal to their own reputation offered to a developer who had just traced the code and found otherwise. And in a separate post O’Beirne identifies Peter Gray “@DocHex” as “the same guy that shrugged off my report of the possibility of the defect in May 2025.” The same Gray who wrote the library. The same Gray who was switck. There was follow-up of a kind. A Signal group titled “LNGU Clean up” was created on 23 May 2025, with members shown as “n,” “Doc,” “andres,” and one other. Doc-hex is Gray. “n” is NVK. So Coinkite formed a group about cleaning up libNgU and named it after the problem. Then they shipped… nothing! Absolutely no fix fourteen months. The group’s messages were set to disappear after four weeks so whatever was said there is gone, just like the bitcoins that were in hundres of hard working peoples Coldcards. O’Beirne blames himself for not pushing harder. He calls not following up rigorously a horrible mistake on his part. Hold that next to Coinkite’s public explanation which is that an attacker probably used AI to find something nobody could reasonably have caught. The developer who caught it is apologizing. The company that was responsibly informed is blaming the clankers. He didn’t know what was in his own crypto library Coinkite’s technical postmortem is worth reading in full because its author is if nothing else candid. He explains that he set the macro to zero believing it meant neither implementation would be compiled. That is not what it does. And he writes that the bulk of the randomness in the device was coming from a PRNG he did not know was in the codebase at all because it arrived through a submodule. Meanwhile the carefully written hardware TRNG code was still being used, but only by accident and only for things that didn’t matter. He is describing a submodule he wrote. The company selling immunity to entropy tampering did not know which random number generator its product used for five years. The man who says he didn’t know is the man who authored both sides of the mistake. And the answer when it finally surfaced was that libngu XORed one software PRNG against a second software PRNG seeded from constants hardcoded in public source. Two deterministic streams XORed together produce a deterministic stream. The built in health check rejects adjacent repeated values which any nondegenerate PRNG passes without effort. Those are the same hardcoded yasmarang constants O’Beirne told them to rip out. Coldcard seeds generated in that window contained no physical randomness whatsoever. They bought a press release not an audit Peter Todd says Coinkite brought him on in early 2014 as “Chief Naysayer”: an advisory role. Years before the first hardware wallet existed there was a press release. By his account he was given nothing to work on: no tasks, no work to bill for, and then the arrangement quietly dropped. He says it’s still on a LinkedIn profile that he hasn’t logged into in a over decade. His assessment now in his own words: “if they had kept him on and asked him to audit the codebases, there’s a good chance he’d have spotted the practices at issue, and maybe eighty million dollars wouldn’t have been stolen”. He puts that audit at roughly $50k and asks what Coinkite spent on podcast sponsorships instead. The company announced that a famous skeptic was reviewing them and then never asked him to review anything. The press release was the product. All the things they said Coinkite’s public position throughout this crisis has been that it had no idea the flaw existed until the day the money started moving. Two documented warnings and a Signal group named after the problem say otherwise. NVK’s stated position on attribution: they “don’t have full attribution or scope yet”, and they “won’t speculate until the technical evaluation is complete”. Coinkite then suggested publicly that the attacker likely used an automated tool to comb the public source and find the flaw before they did. That’s speculation. This propisition rests on absolutely no evidence. And it happens to be the only theory of the case in which nobody at Coinkite knew and nobody at Coinkite failed. You can decline to speculate or you can float the hypothesis that clears you. Doing both inside the same week tells you which one was the priority. Coinkite told customers it kept purchase data for 90 days. When breach notifications went out they reached buyers going back to 2019. Challenged, the company pointed at a policy page, conceded it has no deletion schedule and said the addresses would be kept “for now.” A verifiable lie caught within a few days of the largest breach of trust in hardware wallet history, and on a question where the answer was easily verifiable. This speaks volumes of NVK’s character. The fix broke too On 31 July Coinkite shipped out an emergency firmware update. Three days later a contributor opened pull request #692 against the Coldcard firmware repo, reporting that the hotfix had introduced a new failure on the hardware RNG path. The entropy fix itself is correct: rng_get() now resolves to the board’s true hardware accessor instead of the software fallback. But rng_get_or_fault() had no recovery path for the STM32’s RNG seed error flags. After a seed error the peripheral stops delivering data and the shipped code never clears the condition; so every later call times out and raises OSError(EFAULT) for the rest of that boot. Because rng_get() now sits on the keypad scan path (an interrupt callback that runs before login) that exception lands before the PIN prompt. Power cycling clears the flags; if the error recurs on the next boo: the user is locked out of the upgrade menu too and the device is essentially bricked. The original report overstated the stickiness. The flags do not survive a power cycle: so this is not a permanent brick from a single glitch. It is still a serious regression: an emergency patch for a five-year review failure shipped fast that can take the device down before the user can enter a PIN. 692 was closed in favor of #693, a cleaner recovery sequence from a Coinkite contributor, with #698 as the Mk3 follow-up. Both were still open when this was written. The point is not that nobody noticed. The point is that the first hotfix for a five-year entropy failure needed a second round of patches within days. Giving the attacker MORE TIME to execute sweeping funds from vulnerable wallets. What they’ll say Three objections are coming, and they’re the ones I’d make if I was NVK for sure Galaxy says the waves may not share an operator. True: and irrelevant to the part that matters. Galaxy’s caution is about waves two, three, and four. Once wave one went loud on 30 July the vulnerability was public property and anyone with tooling could pile in. That’s what waves three and four look like. Wave one is the one that tells you something. 1,082 BTC out of 1,195 addresses in 41 minutes with seeds already computed; executed by someone who had been preparing while nobody else on earth knew there was anything to prepare for. The bug was publicly findable: anyone could have found it. Two people found it in public and said so, in 2021 and in 2025. Both were told it was fine. The set of people who knew this was a live question before 30 July is not the general public. It’s a short list and Coinkite was on it. A mass sweep is too loud for an insider. It’s too loud for the rational insider who bleeds quietly over years and never triggers a referral. The loudness cuts against a careful inside job. It does not erase the warnings, the Signal group, or their response that if something was wrong they’d already know. What I think happened Somebody inside that company knew what was sitting in the codebase and knew what it was worth. Look at the timeline: Ten weeks before the bug shipped the CEO publicly waved off the idea that a vendor would ever run a retirement attack and pointed at dice as the alternative. His co-founder and CTO then wrote a crypto library under a pseudonymous GitHub account with about six stars, and shipped the device’s entire randomness path through it. Five weeks later someone flagged the swap in a Coldcard Telegram group and was ignored. Seven months after that the company marketed immunity to the exact attack class the defect enables and made the only reliable defense an “opt in”. Four years in: a Bitcoin developer audited the firmware found the library, named the hardcoded constants, told them to remove the whole thing, and was told they’d already know if something was wrong. They opened a Signal group called “LNGU Clean up,” set the messages to disappear, and shipped nothing. Coins were leaving through 695 transactions nobody noticed. Then somebody who had been precomputing seeds for a long time took 1,082 BTC in 41 minutes. Each of these has an innocent explanation available. All of them stacked in the same direction inside a company of twenty people. This is not a run of bad luck. Inverse Hanlon’s razor exists for exactly this shape: when incompetence needs that many separate coincidences to line up the same way the incentive is the simpler explanation. I can’t say for 100% it was an inside job of course: every document that would definititevly prove it belongs to them. The “LNGU Clean up” thread, whatever survived a four week expiration. Whatever code review they ran and when. The commit history around anyone who touched rng.c after May 2025. Roughly 600 attacker addresses are already in front of federal investigators and Coinkite says it’s cooperating. Cooperation is cheap. Coinkite has apologized, published a postmortem, shipped a fix that needed a second round of patches within days, and offered its customers not a single sat as compensation. The man who found this in May 2025 is publicly apologizing for not pushing harder. And NVK is blaming AI. The people who still have their bitcoins are the ones who read Coldcard’s own documentation, saw the line offering them a way to distrust the manufacturer’s randomness, and took it. Nobody told them that one sentence in the docs was the difference between keeping their money and losing it.

14h ago

---

**[[GER] Petition for Bundestag: Beibehaltung der steuerlichen Haltefrist für Bitcoin](https://www.reddit.com/r/Bitcoin/comments/1vgaw3p/ger_petition_for_bundestag_beibehaltung_der/)**

There is an active petition for keeping Bitcoin tax free in Germany (after one year hodling). It reached 21.000 signatures within the first 24 hours - let's make it 30.000 to put it on the agenda of german Bundestag. You need to sign up in order to put your signature but it's worth it. Everyone can sign - not just germans! https://epetitionen.bundestag.de/petitionen/_2026/_05/_30/Petition_201716.nc.html Thank you!

1h ago

---

**[Wow, Bitcoin just delivered one of the biggest on-chain performances ever!](https://www.reddit.com/r/Bitcoin/comments/1vg85pg/wow_bitcoin_just_delivered_one_of_the_biggest/)**

The network processed 20,364,529 transactions in July 2026, making it the second-best month in entire history by transaction count. As new users, institutions, and Bitcoin-native applications continue to arrive, on-chain activity keeps pushing toward record territory. We think that, it's a remarkable achievement for a network that has been operating for more than 17 years and continues to reach new milestones. Congratulations to everyone contributing to the Bitcoin ecosystem!

3h ago

---

**[Coinkite](https://www.reddit.com/r/Bitcoin/comments/1vfyzcd/coinkite/)**

11h ago

---

**[Coinkite CTO Peter Gray linked to the code behind the $114M Coldcard hack](https://www.reddit.com/r/Bitcoin/comments/1vfpadi/coinkite_cto_peter_gray_linked_to_the_code_behind/)**

Researchers have tied the faulty randomness code at the center of the Coldcard wallet breach to Coinkite co-founder and CTO Peter Gray, who Bitcoin developer

🔗 [Cryptopolitan](https://www.cryptopolitan.com/coinkite-cto-peter-gray-linked-coldcard-hack/) • 19h ago

---

---

## Google News: "bitcoin"

**[Elon Musk's SpaceX (SPCX) tops earnings as bitcoin (BTC) holding value drops by $540 million](https://www.coindesk.com/business/2026/08/04/spacex-tops-wall-street-revenue-forecast-posts-usd540-million-decline-on-bitcoin-holding-value)**

Elon Musk's space company posted its first earnings as a public company ahead of a major insider share unlock.

CoinDesk • 17h ago

---

**[Coldcard wallet attack drains up to $89M in Bitcoin from 1,200+ addresses](https://www.foxbusiness.com/fox-news-tech/coldcard-wallet-attack-drains-up-89m-bitcoin-from-1200-addresses)**

A Coldcard firmware bug may have let attackers steal roughly $70 million in bitcoin in under an hour, and the company says attacks are still ongoing. Estimated losses now at $89M.

foxbusiness.com • 2d ago

---

**["You stole, please return some." Coldcard hacker's wallet becomes a graffiti wall of pleas and hustles](https://www.coindesk.com/markets/2026/08/05/you-stole-please-return-some-coldcard-hacker-s-wallet-becomes-a-graffiti-wall-of-pleas-and-hustles)**

The Coldcard hacker's bitcoin wallet has turned into a graffiti wall of pleas, poetry and scams, as victims and opportunists pay to leave permanent messages using Bitcoin's OP_RETURN function.

CoinDesk • 12h ago

---

**[What we know about ongoing Coldcard hack that's stolen over $100M worth of bitcoin](https://www.cbc.ca/news/world/bitcoin-coinkite-security-hack-9.7295582)**

A Toronto-based company that made Coldcard, a bitcoin-only hardware wallet that has been the latest target of a data breach, 
has reportedly lost $100 million US worth of bitcoin as a result of the hack.

CBC • 22h ago

---

**[Keeping Your Bitcoin Riches Safe Has Never Been Harder](https://www.bloomberg.com/opinion/articles/2026-08-05/bitcoin-keeping-your-crypto-stash-safe-has-never-been-harder)**

Bloomberg.com • 6h ago

---

**[Current price of Bitcoin for August 4, 2026](https://fortune.com/article/price-of-bitcoin-08-04-2026/)**

Bitcoin runs on a P2P network instead of being controlled by the government, a bank, etc. It lets you send value directly to someone else without a middleman.

Fortune • 1d ago

---

**[A $140-million hack has bitcoin users rethinking how they store their crypto](https://www.theglobeandmail.com/investing/article-after-140-million-hack-bitcoin-users-soul-searching-over-self-custody/)**

A coding error in bitcoin wallets made by Coinkite Inc. allowed hackers to steal from individuals storing their own cryptocurrency

The Globe and Mail • 15h ago

---

**[Eric Trump-Led American Bitcoin To Adopt Michael Saylor’s Approach of Selling BTC to Support Economics? CEO Says…](https://finance.yahoo.com/markets/crypto/articles/eric-trump-led-american-bitcoin-073725523.html)**

American Bitcoin Corp. (NASDAQ:ABTC) CEO Mike Ho sidestepped questions on Monday about selling Bitcoin (CRYPTO: BTC) to fund equity buybacks, a move some other companies in the industry have pursued. American Bitcoin’s ‘North Star’ During American Bitcoin’s second-quarter earnings call, Ho was questioned about the company’s treasury management strategy and whether it would contemplate selling Bitcoin to improve business economics, similar to the approach taken by Michael Saylor’s Strategy Inc. (

Yahoo Finance • 1d ago

---

**[Trump-Linked Bitcoin Venture Reached $2.5 Million Settlement Over Improperly Obtained Loan Allegation](https://www.forbes.com/sites/antoniopequenoiv/2026/08/04/trump-linked-bitcoin-venture-reached-25-million-settlement-over-improperly-obtained-loan-allegation/)**

The settlement was noted in the company’s 10-Q filing, excluded from its earnings narrative.

Forbes • 19h ago

---

**[Trump brothers-backed American Bitcoin swings to second-quarter loss](https://www.reuters.com/business/trump-brothers-backed-american-bitcoin-swings-second-quarter-loss-2026-08-03/)**

Reuters • 2d ago

---

---

## HackerNews: "bitcoin"

**[Bitcoin cold-wallet attack spreads to 4,500 addresses as losses near $89M](https://news.ycombinator.com/item?id=49149222)**

Galaxy Research flagged a third wave of sweeps tied to weak Coldcard-generated keys, with the attacker now targeting smaller balances and changing how funds are collected onchain.

⬆️ 69 • 💬 23 • 2d ago • [coindesk.com](https://www.coindesk.com/tech/2026/08/02/bitcoin-cold-wallet-attack-spreads-to-4-500-addresses-as-losses-near-usd89-million)

---

**[Coldcard wallet RNG flaw likely linked to $88M Bitcoin theft](https://news.ycombinator.com/item?id=49148905)**

A vulnerability in COLDCARD hardware wallet firmware allowed attackers to steal an estimated $88.6 million in Bitcoin from thousands of wallets whose seeds were generated using a flawed random number generator.

⬆️ 19 • 💬 0 • 2d ago • [BleepingComputer](https://www.bleepingcomputer.com/news/security/coldcard-wallet-rng-flaw-likely-linked-to-88-million-bitcoin-theft/)

---

**[U.S. sanctions Iranian firms for Bitcoin maritime insurance operation in Hormuz](https://news.ycombinator.com/item?id=49141295)**

OFAC Sanctions Illicit Maritime Insurance Scheme and Iran’s Shadow Fleet  WASHINGTON—Today, the U.S. Department of the Treasury’s Office of Foreign Assets Control (OFAC) is taking further action against the Iranian regime’s desperate efforts to monetize the Strait of Hormuz and prop up the nation’s failing economy.  OFAC is designating two firms integral to an Islamic Revolutionary Guard Corps (IRGC)-backed extortion scheme that forces commercial vessels to purchase mandatory maritime “insurance” to transit the Strait.  Although this coverage purports to protect vessels from risks such as seizures, these risks are overwhelmingly created by Iran itself.  Through the Persian Gulf Marine Insurance Company and HormuzSafe Marine Services Authority, the regime brokers IRGC-approved policies designed to extract revenue under the guise of maritime services, including payments in digital assets to evade sanctions—allowing Iran to tighten control over shipping activity and funnel funds into IRGC operations.“With its economy in freefall and inflation in the triple digits, the regime is desperate for cash,” said Secretary of the Treasury Scott Bessent. “The United States will not allow Iran to hold global commerce hostage or use international shipping to finance the IRGC’s terrorism, aggression, and repression.”                            OFAC is also reinforcing U.S. military interdiction efforts and intensifying pressure on Iran’s energy shipments by imposing sanctions on several vessels that transported Iranian crude oil and petrochemical products.  Since the beginning of the year, OFAC has sanctioned over 100 vessels linked to Iran’s shadow fleet, a covert logistics network that enables the regime to keep oil revenues flowing despite international sanctions. Today’s action was taken pursuant to Executive Order (E.O.) 13902, which targets Iran’s petroleum and petrochemical sectors and advances the President’s National Security Presidential Memorandum 2 (NSPM-2), to impose maximum economic pressure on Iran. IRANIAN Regime’s EXTORTION SCHEMEIn an attempt to prop up revenue streams decimated by Operation Epic Fury, Iran has established illegitimate schemes through the Persian Gulf Marine Insurance Company (PGMIC) and HormuzSafe Marine Services Authority, also known as Hormuz Safe, to extort vessels attempting to conduct routine commercial passages through the Strait of Hormuz.  Established by the Central Insurance of the Islamic Republic of Iran, Iran’s primary insurance regulator, the PGMIC brokers and issues insurance policies approved by the U.S.-designated, IRGC-backed Persian Gulf Strait Authority (PGSA).  The insurance covers risks, most of which are created by Iran itself, such as vessel seizures, and aims to generate revenue to fund the regime’s terror and corruption. PGSA was designated pursuant to E.O. 13224, as amended, on May 27, 2026 for having materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services to or in support of, the IRGC. Hormuz Safe is an Iranian digital insurance firm that advertises itself as a company offering trusted maritime services, including insurance, traffic control, security, and emergency response, to vessels transiting the Strait of Hormuz.  Developed by Iran’s Ministry of Economy, it accepts payment in Bitcoin and other digital assets as part of the regime’s attempts to bypass Western sanctions. Disgraced regime financier Babak Morteza Zanjani, who was sanctioned earlier this year, promoted Hormuz Safe to his social media followers.  Hormuz Safe generates revenue on behalf of the IRGC in an attempt to give the regime tighter control over shipping activity. The Persian Gulf Marine Insurance Company and HormuzSafe Marine Services Authority are being designated pursuant to E.O. 13902 for operating in the financial sector of the Iranian economy. shadow fleet ACTORSTreasury is also taking action today against multiple shadow fleet vessels responsible for transporting millions of barrels of Iranian crude oil and petroleum products.  Iran’s shadow fleet provides an essential lifeline to the Iranian regime, which relies on oil sales to bolster its ailing economy. The Marshall Islands-flagged chemical/products tanker WELL SAIL (IMO 9321938), owned, operated, and managed by China-based Qi Hang Ship Management Limited, has transported hundreds of thousands of barrels of Iranian petroleum products to the United Arab Emirates (UAE) in 2026. The Mozambique-flagged crude oil tanker LILY (IMO 9294331), owned and operated by Hong Kong-based Confident Apex Limited, has transported millions of barrels of Iranian oil since 2025.The unknown-flagged crude oil tanker AL SALMI (IMO 9298296), owned and operated by Hong Kong-based Billion Nexus Int’l Co., Limited, has transported hundreds of thousands of barrels of Iranian oil to China since 2025.The Barbados-flagged crude oil tanker BREEZE V (IMO 9259355), owned and operated by Hong Kong-based Nevada Spirit Company Limited, has transported millions of barrels of Iranian oil to China in 2026. The Barbados-flagged crude oil tanker NATSUMI (IMO 9331244), owned, operated, and managed by Hong Kong-based Marinova Freight Limited, has transported millions of barrels of Iranian crude oil to China since 2022. The Vanuatu-flagged crude oil tanker CRYSTAL (IMO 9223887), owned, operated, and managed by Hong Kong and Marshall Islands-based Vast Mighty Limited, has transported millions of barrels of Iranian crude oil to China in 2026. The Vanuatu-flagged crude oil tanker NIRETA (IMO 9237785), owned, operated, and managed by Marshall Islands-based Ocean Tranquility Limited, has transported hundreds of thousands of barrels of Iranian crude oil to China in 2026. The Barbados-flagged crude oil tanker YEHOPE (IMO 9243320), owned by Marshall Islands-based Branch Saying International Trading Co Ltd, has transported hundreds of thousands of barrels of Iranian crude oil to China in 2026.   The following companies are being designated pursuant to E.O. 13902 for operating in the petroleum sector of the Iranian economy: Qi Hang Ship Management Limited;Marinova Freight Limited;Vast Mighty Limited;Ocean Tranquility Limited; Branch Saying International Trading Co Ltd;Confident Apex Limited;Billion Nexus Int’l Co., Limited; andNevada Spirit Company Limited.The following vessels are being identified as blocked property of the previously identified blocked persons: WELL SAIL (Qi Hang Ship Management Limited);NATSUMI (Marinova Freight Limited); CRYSTAL (Vast Mighty Limited); NIRETA (Ocean Tranquility Limited); YEHOPE (Branch Saying International Trading Co Ltd);LILY (Confident Apex Limited);AL SALMI (Billion Nexus Int’l Co., Limited); andBREEZE V (Nevada Spirit Company Limited). SANCTIONS IMPLICATIONSAs a result of today’s action, all property and interests in property of the designated or blocked persons described above that are in the United States or in the possession or control of U.S. persons are blocked and must be reported to OFAC.  In addition, any entities that are owned, directly or indirectly, individually or in the aggregate, 50 percent or more by one or more blocked persons are also blocked.  Unless authorized by OFAC, or exempt, OFAC’s regulations generally prohibit all transactions by U.S. persons or within (or transiting) the United States that involve any property or interests in property of blocked persons. Violations of U.S. sanctions may result in the imposition of civil or criminal penalties on U.S. and foreign persons.  OFAC may impose civil penalties for sanctions violations on a strict liability basis.  OFAC’s Economic Sanctions Enforcement Guidelines provide more information regarding OFAC’s enforcement of U.S. economic sanctions. In addition, financial institutions and other persons may risk exposure to sanctions for engaging in certain transactions or activities involving designated or otherwise blocked persons.  The prohibitions include the making of any contribution or provision of funds, goods, or services by, to, or for the benefit of any designated or blocked person, or the receipt of any contribution or provision of funds, goods, or services from any such person.  Non-U.S. persons are also prohibited from causing or conspiring to cause U.S. persons to wittingly or unwittingly violate U.S. sanctions, as well as engaging in conduct that evades U.S. sanctions.  Individuals located in the U.S. or abroad who provide information about sanctions violations to FinCEN’s whistleblower incentive program may be eligible for awards if the information they provide leads to a successful enforcement action that results in monetary penalties exceeding $1,000,000. The power and integrity of OFAC sanctions derive not only from OFAC’s ability to designate and add persons to the SDN List, but also from its willingness to remove persons from the SDN List consistent with the law.  The ultimate goal of sanctions is not to punish, but to bring about a positive change in behavior.  For information concerning the process for seeking removal from an OFAC list, including the SDN List, or to submit a request, please refer to OFAC’s guidance on Filing a Petition for Removal from an OFAC List.Click here for more information on the persons designated and any property identified as blocked property today.###

⬆️ 10 • 💬 2 • 3d ago • [U.S. Department of the Treasury](https://home.treasury.gov/news/press-releases/sb0581)

---

**[Has the Bitcoin Moved?](https://news.ycombinator.com/item?id=49160843)**

BitGo's CEO put 100 BTC ($6.3M) in a wallet and dared Anthropic's AI to take it. Live wallet tracker.

⬆️ 8 • 💬 2 • 1d ago • [hasthebitcoinmoved.com](https://hasthebitcoinmoved.com/)

---

**[What we know about ongoing Coldcard hack that's stolen over $100M in Bitcoin](https://news.ycombinator.com/item?id=49174951)**

A Toronto-based company that made Coldcard, a bitcoin-only hardware wallet that has been the latest target of a data breach, 
has reportedly lost $100 million US worth of bitcoin as a result of the hack.

⬆️ 8 • 💬 0 • 20h ago • [CBC](https://www.cbc.ca/news/world/bitcoin-coinkite-security-hack-9.7295582)

---

**[Bitcoin BIP110 mandatory activation this Saturday, how game theory will unfold?](https://news.ycombinator.com/item?id=49180531)**

Where do I stand on BIP-110 and the "spam war"? Discover why I believe this is a strategy of tension, the game theory behind this consensus battle, and why running a node and holding your own keys remains Bitcoin’s ultimate defense against corporate capture.

⬆️ 7 • 💬 4 • 8h ago • [simondixon.com](https://www.simondixon.com/blog/bip-110-the-spam-war-and-the-battle-nobody-wants-to-name-where-i-stand-simon-dixon)

---

**[Coldcard Bitcoin Exploit Balloons to $88M as Attackers Keep Draining Wallets](https://news.ycombinator.com/item?id=49147088)**

Galaxy Research says a third wave of thefts from Coldcard Bitcoin wallets has pushed observed losses to roughly $88.6 million worth of BTC.

⬆️ 6 • 💬 1 • 2d ago • [Decrypt](https://decrypt.co/374817/coldcard-bitcoin-exploit-88-million-attackers-draining-wallets)

---

**[Hackers Hit Bitcoin's Safest Hiding Place in Ongoing Attack](https://news.ycombinator.com/item?id=49167125)**

⬆️ 4 • 💬 1 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-08-03/hackers-target-bitcoin-s-safest-hiding-place-in-ongoing-attack)

---

**[After $140M hack, Bitcoin users 'soul-searching' over self-custody](https://news.ycombinator.com/item?id=49179540)**

A coding error in bitcoin wallets made by Coinkite Inc. allowed hackers to steal from individuals storing their own cryptocurrency

⬆️ 2 • 💬 0 • 10h ago • [The Globe and Mail](https://www.theglobeandmail.com/investing/article-after-140-million-hack-bitcoin-users-soul-searching-over-self-custody/)

---

**[Bitcoin owners rocked by $116M hack: What we know about the Coldcard exploit](https://news.ycombinator.com/item?id=49164690)**

The hack, which has drained 1,816 Bitcoin across 5,200 addresses, is devastating because it affected hyper-secure cold storage wallets.

⬆️ 2 • 💬 0 • 1d ago • [Fortune](https://fortune.com/2026/08/03/bitcoin-owners-116-million-hack-coldcard-coinkite-exploit/)

---

---

## YouTube Videos: "bitcoin"

**[Crypto will EXPLODE in August! (Explained in 10 minutes)](https://www.youtube.com/watch?v=mVk1_eKbtfE)**

August Could Send Crypto to NEW HIGHS!! (Explained in 10 minutes) ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily ...

📺 Altcoin Daily

👁️ 30K • 👍 2K • 💬 214 • ⏱️ 10:08 • 19h ago

---

**[Are Washington&#39;s Fingerprints On This $100 Million Bitcoin Hack?](https://www.youtube.com/watch?v=ggc2Cq4NUQk)**

The Coldcard wallet exploit has already resulted in the theft of more than $100 million in Bitcoin, but new details are raising even ...

📺 Simply Bitcoin

👁️ 17K • 👍 1K • 💬 201 • ⏱️ 10:16 • 19h ago

---

**[Saylor: &quot;Everyone Has Been Sold a Lie&quot; on Bitcoin](https://www.youtube.com/watch?v=I2y6CcOiBKk)**

Michael Saylor, Jim Cramer, Blackrock CEO latest crypto news Trade Stocks (unlock $100k): ...

📺 Altcoin Daily

👁️ 56K • 👍 2K • 💬 138 • ⏱️ 9:49 • 1d ago

---

**[CRYPTO BOTTOM Forming...Saylor Sells $100m Bitcoin, Coldcard Hack, Market Holds!](https://www.youtube.com/watch?v=8LHF1gpTmZo)**

My Links: ▻ Get the risk models I use to track accumulation and exit zones. Free trial https://app.cryptocapitalventure.ai Crypto ...

📺 Crypto Capital Venture

👁️ 8K • 👍 511 • 💬 218 • ⏱️ 10:47 • 1d ago

---

**[XRP &amp; Bitcoin Interest Surges We&#39;re About To See Something Insane In the Cryptocurrency Market](https://www.youtube.com/watch?v=1AqGE-7Pozo)**

Open interest in the cryptocurrency market is ramping up... quickly. Long gone are the days of having to wait months or even years ...

📺 The Modern Investor

👁️ 3K • 👍 550 • 💬 140 • ⏱️ 34:31 • 8h ago

---

**[“100% CERTAINTY! This Is About to TRIGGER Bitcoin’s BIGGEST Bull Market” | Jordi Visser](https://www.youtube.com/watch?v=90HjIMZMlA0)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 5K • 👍 193 • ⏱️ 17:44 • 1d ago

---

**[Hackers Steal Over $100 Million From &quot;Safe&quot; Bitcoin Wallets](https://www.youtube.com/watch?v=iYxVLvsaneA)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 692K • 👍 35K • 💬 2K • ⏱️ 1:39 • 1d ago

---

**[Strategy CEO Phong Le: Expecting Strategy to outperform bitcoin in next year&#39;s bull cycle](https://www.youtube.com/watch?v=bs6yz79MneQ)**

Phone Le, Strategy CEO, joins 'Power Lunch' to discuss the company's decision to sell more bitcoin, the outlook for the ...

📺 CNBC Television

👁️ 19K • 👍 153 • 💬 123 • ⏱️ 4:12 • 1d ago

---

**[Bitcoin: A Decision Will be Forced](https://www.youtube.com/watch?v=WRftdLFrepU)**

Bitcoin has a decision to make soon. Let's discuss! Come to the 1st ITC Conference: https://www.benjamincowen.com/conference ...

📺 Benjamin Cowen

👁️ 109K • 👍 6K • 💬 255 • ⏱️ 7:53 • 2d ago

---

**[How Bitcoin Custody Works &amp; Breaking Down The Coldcard Incident](https://www.youtube.com/watch?v=QU1nJ4b6Hro)**

0:00 Show Opening and Somber Mood 0:45 Urgent Warning to Coldcard Users 2:17 What the Coldcard Bug Means 3:35 Owning ...

📺 THE JACK MALLERS SHOW

👁️ 19K • 👍 863 • 💬 297 • ⏱️ 2:14:49 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
