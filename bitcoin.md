---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-07-12T04:54:40.877757+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- cryptocurrency
- news
- videos
- social
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** July 12, 2026 at 04:54 UTC  
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

### $63,800.00

---

## Bitcoin Chart

**24h:** -0.3%  
**7d:** -0.0%  
**30d:** -0.7%  
**90d:** -13.7%  
**1y:** -46.3%  

---

## Bitcoin Market Stats

**Market Cap:** $1282.40B
Rank #1

**Circulating Supply:** 20,055,134 BTC
95.5% of max

**All-Time High:** $126,080.00
-49.3%

**All-Time Low:** $67.81
+94197.3%

---

## Fear & Greed Index

### 26
**FEAR**

---

## Reddit: r/Bitcoin

**[I built an autonomous ESP32-S3 controller to mine Bitcoin strictly using solar surplus (Zero grid consumption). Open Source! ☀️⛏️](https://www.reddit.com/r/Bitcoin/comments/1utpsqd/i_built_an_autonomous_esp32s3_controller_to_mine/)**

Hey everyone, I just dropped v4.0 of my open-source Solar Crypto Mining Farm project, and I wanted to share the architecture. The goal was simple: mine Bitcoin only when there’s free solar energy, and never pay for grid electricity to do it. I’m running a 7,740Wp solar array into a custom mining fleet (Avalon Q, Nerd Octaxe, NerdQAxe+, and a BitAxe Gamma). To orchestrate this, I built an edge-computing controller using an auto-detected ESP32-S3. How it works: The ESP32-S3 polls a 6-channel Refoss EM06P energy monitor every 30 seconds via HTTP API. It calculates the exact solar surplus across a bi-phase circuit (W, VA, and VAR). The decision engine automatically switches between 16 calculated mining profiles (from a single 21W BitAxe up to a 2001W full fleet blasting 104.5 TH/s) to perfectly match the live surplus. Relays handle the smaller ASICs, while the Avalon Q is controlled via CGMiner API commands to scale its modes (Low/Mid/High). Everything is logged to a Supabase cloud database, and the ESP32 serves a live local web dashboard. I also built a live Three.js 3D visualization of the whole cluster operating in real-time. You can check out the live 3D dashboard here:https://0xraphael.com/solar-mining-clusterAnd the full repo (including the v4 per-phase W/VA/VAR scalar math and Tasmota configs) is available here: https://github.com/0xrphl/Solar-crypto-mining-farm-maximization-control Would love to hear any feedback on the energy modeling or the edge logic!

11h ago

---

**[Long live bitcoin hodler](https://www.reddit.com/r/Bitcoin/comments/1utcfrs/long_live_bitcoin_hodler/)**

22h ago

---

**[Anyone else worried that it’s too easy?](https://www.reddit.com/r/Bitcoin/comments/1utpo6w/anyone_else_worried_that_its_too_easy/)**

Bitcoin is the best performing asset in human history, and we can just scale in at the scheduled bear market lows that occur every 4 years and 5x our money in a few years? I had these same thoughts after the FTX capitulation, that surely it can’t be this easy to buy here and wait. Sure enough, bitcoin went up almost 800% off the lows and I made a ton of money. Are they really going to let us do it again??

11h ago

---

**[Bitcoin logo displayed on the Las Vegas Sphere 👀](https://www.reddit.com/r/Bitcoin/comments/1usz2g5/bitcoin_logo_displayed_on_the_las_vegas_sphere/)**

1d ago

---

**[The future of Bitcoin](https://www.reddit.com/r/Bitcoin/comments/1utxkz8/the_future_of_bitcoin/)**

In 2012, when I first bought Bitcoin, it was $13 a coin. I watched it go from $13 to over $100,000. Now I’ll watch it go $100,000 to $1 million a coin. You believe yet?

6h ago

---

**[Post-Mortem: What Happened Between Samourai Wallet and Me](https://www.reddit.com/r/Bitcoin/comments/1utroht/postmortem_what_happened_between_samourai_wallet/)**

How a wallet that adopted my privacy framework turned technical disagreement into a reputational war—and what I got wrong too The fully sourced and illustrated version, together with the complete evidence archive, is available on GitHub. The archive preserves court filings, source-code snapshots, public posts, private-message records, Research Club transcripts, and screenshots. After law enforcement seized Samourai Wallet’s servers, William Hill—TDevD—messaged an associate: “Not good.” “I’m not thinking so much about Whirlpool as I am about the wallet backends (xpubs).” An extended public key cannot spend a user’s bitcoin, but it can reveal the addresses derived from a wallet and follow their history. For years, I had argued that Samourai’s default backend created exactly this point of failure. Hill’s message, reproduced in the government’s sentencing memorandum, showed that he understood why the seizure of that backend mattered. The seizure did not create the xpub problem. It exposed the consequences of a design choice that had been there from the start. I do not offer this post-mortem as vindication. A prison sentence cannot settle a protocol dispute, and an indictment cannot make every allegation true. I will distinguish what the public record establishes, what I infer from it, and what I remember but cannot independently prove. To understand what was sitting on that server—and why I had spent years shouting about it—we have to go back to a README file in July 2017, before the feud began. How ZeroLink actually began I wanted Samourai to succeed in implementing ZeroLink. I wanted more wallets to implement serious Bitcoin privacy, and I wanted ZeroLink to become useful software rather than another specification admired by a small circle and ignored by everyone else. I created ZeroLink. The repository history makes the chronology clear. I opened it on July 28, 2017. Before Samourai made a single commit, I had made 19 commits and written a 184-line, 2,883-word document containing the framework’s core architecture. Samourai’s first commit arrived two days later. Its title was “Fix typos”. It did exactly that. ZeroLink was not merely a name for a CoinJoin transaction. It was a privacy framework for Bitcoin wallets: blinded coordination together with rules for network privacy, coin selection, transaction chains, and spending after the mix. Chaumian CoinJoin was the protocol; ZeroLink was the wider wallet framework. That is the work Samourai later claimed to have co-created. At the August 14 publication snapshot, Git blame attributes 6,126 of the document’s 6,627 words to me and 242 to Bill/TDevD. Their only sizeable technical addition concerned BIP47 and stealth addresses. At the time, I did not understand what problem that proposal solved or why it belonged in ZeroLink. Instead of challenging it, I assumed I was missing something and accepted it out of politeness. Two days later, I clarified that BIP47 was not part of the protocol, and I removed the section in 2019. The rest of their work was overwhelmingly light editing. I had also placed TDevD in the Authors section before that proposal was committed. Both decisions came from the same reflex: they spoke with confidence, I assumed any confusion was mine, and I tried to be generous. That politeness was later used to support an authorship claim the repository does not support. By 2022—three years after I had publicly challenged the co-creation story, with the Git history still open for inspection—Samourai was still repeating it. I regard those later repetitions as a lie. “Collaboration” can be innocent shorthand before anyone disputes it. It stops being innocent after the primary record is placed in front of you and you continue telling the version that promotes you from reviewer and prospective implementer to co-creator. Our contact was limited. We barely spoke, and I was never part of Samourai. I had created ZeroLink; Samourai said it intended to implement it. Brian “Shinobi” Trollz, who observed the dispute at the time, later recalled a specific turning point. I asked for a week to consider whether coordinators could be run altruistically. During that week, he said, Samourai’s posture toward me shifted into mockery. By April 2019, I had recorded that they were no longer interested or responsive and that I had continued independently. People can disagree about why our limited contact ended. The authorship record is not a matter of recollection. The central privacy difference The authorship dispute mattered to me. The architectural difference between the wallets mattered to users. Wasabi’s default architecture was designed to deny its own operator the wallet graph. The backend distributed block filters; clients checked addresses locally; wallet traffic went through Tor; and blinded CoinJoin credentials prevented the coordinator from linking a registered input to its output. A user did not have to operate a personal server to hide addresses and transaction history from us. Privacy from the service operator was the default. Samourai’s default client sent extended public keys to Samourai’s hosted backend. Whoever possesses an xpub can derive its associated addresses and follow their transactions. Samourai’s own Dojo documentation disclosed the consequence indirectly. Running MyDojo improved privacy by “completely bypassing” the default hosted servers, while its Tracker recorded registered xpubs and addresses. Then came the clearest lie in the xpub argument. In October 2022, Kruw pointed out that the default app exposed the user’s xpub and asked why Samourai would not use BIP157/BIP158 client-side filters. The official wallet account refused, defended what it called “the best architecture for our needs,” and claimed it had been “open and truthful from day one.” When asked whether wider BIP157 adoption would change that decision, the official account answered: “We are a full node wallet. Always have been.” That statement remains public. It was false. The Android app was a light client of a backing server. Dojo could place that server and a Bitcoin Core node under the user’s control, but it did not turn the phone into a full node. Samourai’s own 2019 announcement said default users had to trust its servers with their public keys. Hill’s sentencing submission later described the architecture as one used by “light wallets.” Tor support existed, but it was not enabled by default. Samourai’s signed source allowed a user to create a wallet while Tor remained off, treated the Tor preference as false unless the user enabled it, and used the ordinary network path for xpub requests when Tor was disabled. An April 2023 report on Samourai’s own GitLab included the wallet-creation screen with Tor off, Dojo unconfigured, and Create a new wallet still available. The issue, titled “Important privacy features are disabled by default,” proposed enabling Tor and Dojo by default or at least warning users what the disabled settings exposed. A Samourai project owner said the proposal would not be merged, called the report “concern trolling,” issued a “first and final warning,” and immediately closed it. The archived issue preserves the exchange. The privacy problem was reported on their own development platform. Their response was to reject the change and threaten the reporter. An earlier exchange used a different evasion. In July 2022, a user wrote: “Xpub is sent to whirlpool servers.” Hill answered: “No xpubs are handled by the coordinator.” The xpubs went to Samourai’s wallet backend, not the Whirlpool coordinator. He changed the noun while avoiding the issue. In the same reply, he claimed Samourai had implemented ZeroLink “on spec,” something I supposedly “didn’t have the skill set to do.” The post simultaneously evaded the backend question and reversed the authorship record. Sentinel, Samourai’s watch-only app, made the architecture even easier to see. A watch-only wallet legitimately needs an xpub, and Sentinel correctly said it could not spend the user’s coins. The privacy question was what happened after the user imported that xpub. In August 2017, Samourai committed a change titled “move XPUB multiaddr to Samourai API”. From then on, Sentinel sent tracked xpubs to Samourai’s hosted backend. It did so for more than two years before Tor routing was added. When Tor arrived, its preference defaulted to off. Sentinel could not steal users’ coins. Its hosted mode could map their wallets. That collection was integral to the product, not incidental telemetry. Dojo arrived years later Dojo did not erase what the default client had already disclosed. Dojo’s server code was released on June 2, 2019, nearly four years into Samourai’s life. Even then, Samourai said the wallet required another update before it could pair with Dojo. Version 0.99.81 finally added pairing on July 11, 2019, but only for a newly created wallet. Restoring an existing wallet was explicitly unsupported. Samourai’s own release announcement instructed users to create a new wallet after pairing. An earlier user who wanted to stop using Samourai’s hosted servers therefore had to create a new wallet behind Dojo and move funds out of the old wallet. That could prevent disclosure of the new wallet’s xpub. It could not retract the old xpub or history already sent to Samourai. A direct transfer between the wallets would also remain visible on-chain. Dojo gave later self-hosters a way to avoid future disclosure. It did not retroactively protect default users. The Blockchain.info lineage William led the Blockchain.info Android wallet project that preceded Samourai. He opened the surviving Android-Wallet-2-App history with its April 2014 initial commit and is its dominant visible developer by commit count. His sentencing submission calls him Blockchain.com’s senior mobile developer. Contemporary coverage identifies Keonne Rodriguez as the product lead responsible for the refreshed wallet’s interface and user experience. William’s commits even include “UI prep for shared coin”, referring to Blockchain.info’s earlier mixing product. They did not create Blockchain.info itself. They did lead the mobile-wallet project from which Samourai emerged. Samourai then kept its own source private for approximately a year. At the time, it said this delay was deliberate and intended to give the product a competitive “leg-up.” When the first public Samourai snapshot appeared in March 2016, it contained unmistakable Blockchain.info lineage. That does not mean the entire application was a verbatim copy. It does contradict the image of a clean-sheet privacy wallet appearing from nowhere. SharedCoin matters because its trust problem was already understood. It was noncustodial, but its server constructed the joins and knew their links. Public transaction ambiguity could not provide privacy from the operator that already knew the mapping. Samourai rebuilt that operator-trust problem by collecting wallet-level public keys on its default server. I raised this before the seizure. In an April 2020 Wasabi Research Club discussion about ZeroLink, I described the rejected design plainly: a trusted central server to which everyone sends their xpubs. That, I said, “obviously sounds pretty stupid,” which is why ZeroLink used blinded coordination. In July 2021, I again explained that if a server possesses the xpub, repeated mixing cannot erase what the server already knows. In September 2022, during a discussion of balance-query architectures, I warned that an xpub retained on another computer could later be exposed through hacking or seizure. The government seized Samourai’s servers in April 2024. The practical distinction was whether the operator was technically prevented from learning wallet relationships or merely trusted not to use them. Wasabi was not perfect against every imaginable adversary. No honest system built on Bitcoin, Tor, fallible software, and human behavior can promise that. But against the service operator—the adversary at the center of this dispute—Wasabi placed cryptography and local processing between the user and us. Samourai relied on trust in its operator. Sockpuppets and attacks on critics My first SamouraiLeaks investigation began with the suspicion that one of Samourai’s developers was promoting the project and attacking critics through an identity presented as independent. In April 2019, I published the evidence that “foneBTC” and “fone-btc” were TDevD/William Hill’s sockpuppet accounts. The investigation itself contains the proof. The problem was not the use of a pseudonym. Pseudonyms are normal in Bitcoin. The problem was hidden affiliation used to manufacture consensus: one participant appearing to be several, promotion made to look organic, and an interested party presenting himself as a neutral observer. In a field where few users can audit every cryptographic claim themselves, reputation becomes part of the security model. Astroturfing corrupts that model. Before publishing, I tried private discussion, sought a mediator, and offered to stop discussing Samourai if the attacks stopped. Eventually, I concluded that my silence was being treated as permission rather than de-escalation. Other developers then began describing the same treatment. Gregory Maxwell said architectural criticism was answered with harassment and accusations instead of a technical response. Nicolas Dorier described the reaction he received after pointing out that the default backend received users’ extended public keys. Their comments remain in the original discussion, including Dorier’s account. Luke Dashjr said that disclosing an RPC-password exposure in a setup guide brought an accusation that he operated a criminal protection racket. Chris Belcher later described substantive BIP47 objections being answered by smears against the people raising them. These were independent developers, not a Wasabi group. Several of them also criticized Wasabi. Their accounts described the same response: technical objections were redirected toward the critic’s motives, status, or character. Accuse loudly, qualify quietly After enough repetitions, the pattern became predictable: begin with something real—an uncertainty, compromise, or bug—then attach the most damaging possible interpretation and promote that interpretation as the headline. When contrary evidence appears, place the qualification where fewer people will see it: inside a reply, outside a screenshot, or silently inside a later code change. Samourai claimed I had admitted Wasabi supplied its own liquidity. I had made no such admission. The journalist responsible for the report corrected that characterization, but the correction never travelled as far as the accusation. Another observer documented how Samourai’s presentation excluded my correction and contrary replies. The same technique appeared in the Tor-identity dispute. In April 2023, a user asked whether Whirlpool changed Tor circuits between input registration and output registration. Keonne Rodriguez answered categorically that it did and dismissed the questioner as a known liar. In March 2024, the Whirlpool client added an explicit changeIdentity() call immediately before output registration. The code comment said the new identity was used to “unlink from input.” The later commit cannot establish that previous users were deanonymized or that anyone exploited the earlier behavior. It does establish that the categorical answer was not justified. A precise response in 2023 would have explained what the code did, what had been verified, and what remained uncertain. Rodriguez answered with certainty and an insult. The code changed later. That response culture made reporting problems socially expensive. Even small bugs became difficult to discuss because the reporter risked becoming the subject. OXT was owned by Samourai OXT was not an independent research group that happened to agree with Samourai. In December 2017, Samourai announced that it had “finalized the acquisition” of OXT in an all-bitcoin transaction and described the purchase as a long-term strategic investment. Years later, an OXT developer’s support letter included in William’s own sentencing submission described OXT as a Bitcoin forensic tool “owned and operated by Samourai Wallet.” The government separately described William and Keonne as operating OXT as a tracing and wallet-attribution tool. Samourai denounced surveillance companies while owning and operating a blockchain tracing and wallet-attribution tool of its own. In August 2020, this Samourai-owned research arm announced two supposed Wasabi vulnerabilities, rated them High/Critical, claimed they could cancel privacy gained from earlier mixes, and gave us forty-eight hours to publish a warning on its terms. The full report contained a fatal premise: the attacker had to know the composition of the target’s wallet at a chosen point in time and know events affecting that wallet’s participation in later rounds. That was not a small condition. It supplied the wallet membership the alleged attack was supposed to uncover. OXT’s demonstration avoided the problem by controlling both sides. Its “Alice” started with a known coin. Its “Eve” already knew which funds belonged to Alice and ran a modified Wasabi client that logged round events. Given the wallet’s exact starting state, public coin-selection code could sometimes predict which coins the client would offer next. That showed that known software can behave predictably when the observer is handed its private starting state. It did not demonstrate how an outside observer could discover an unknown wallet’s contents, identify an unknown mixed output as the target’s, or recover the blinded input-to-output link. Even in that constructed test, predictions failed because of confirmation states, failed rounds, and coordinator behavior. OXT called those deviations “exogenous randomness.” Its reported “adjusted anonsets” were values produced by its own model—not identities uncovered or input-output links recovered. My contemporaneous response explained that distinction. Adding randomness can be reasonable hardening without validating a claimed exploit. Samourai later treated Wasabi 2’s different coin-selection behavior as an admission that OXT had been right. The timeline contradicts that story. The Wasabi 2 research effort began in January 2020, and WabiSabi was publicly presented in June—before OXT’s August disclosure. The hypocrisy was direct: OXT’s hypothetical attacker needed to begin with a target’s wallet map, while Samourai’s actual default backend collected wallet maps. OXT itself later wrote that privacy guarantees must come from default software behavior, not burdens placed on users. Samourai’s default failed that standard. Avoiding its hosted backend required the user to run Dojo. Criminal association as a marketing weapon Samourai and OXT repeatedly attached Wasabi’s name to alleged criminal activity and then treated the association itself as evidence against us. The trap worked either way. If we answered, we helped spread the association. If we stayed silent, they presented the silence as a concession. In some cases, answering meaningfully would have required disclosing operational knowledge or investigative methods that could not safely be made public. The absence of a public response did not mean agreement. Samourai’s double standard became especially ugly after Luke Dashjr’s theft. On January 4, 2023, OXTObserver flagged 204.77460928 BTC as #LUKE-JR_STOLEN_FUNDS and described the wallet as controlled by hackers. Samourai Wallet reposted the alert. A user asked what Samourai would do if the thieves tried to mix the coins in Whirlpool. The official account answered: “If they go into Whirlpool? Relish in the delicious irony and extra salt in Luke’s gaping wound.” The exchange remains public. It does not establish that the stolen coins entered Whirlpool. It establishes how Samourai’s official account reacted to the possibility because the victim was Luke. By 2022, legal and regulatory pressure on zkSNACKs was threatening the survival of the company-run coordination service. The default coordinator began rejecting some UTXOs. I had argued against blacklisting, and users who felt betrayed had a legitimate grievance. That policy was censorship by one service. It did not reveal the relationship between accepted inputs and their outputs. The protocol still blinded that relationship; Wasabi remained MIT-licensed; and alternative coordinators could operate without zkSNACKs’ policy. Samourai turned the policy dispute into the claim that Wasabi had become a surveillance wallet. The comparison ignored the architectures: zkSNACKs refused some inputs without learning their outputs, while Samourai’s default backend received and retained ordinary users’ wallet maps. The megaphone was bigger than the product Samourai’s Twitter presence made the rivalry look symmetrical despite the large difference in usage. Dumplings—my reproducible CoinJoin scanner—separated fresh bitcoin entering a mixer from coins merely being remixed. From Whirlpool’s first detected month in April 2019 through the dataset’s end in August 2022, it identified approximately 247,675 fresh BTC entering Wasabi and 30,228 entering Whirlpool. Wasabi led in every one of those forty-one months. This measures bitcoin volume, not unique users. It is nevertheless the opposite of adoption parity. Whirlpool’s headline transaction totals were enlarged by free remixes, through which the same bitcoin could appear in round after round without representing a new user or newly arriving funds. Samourai had a large social-media megaphone. It did not have comparable adoption by this measure. Moving privacy problems did not solve them Whirlpool advertised CoinJoin transactions with no toxic change. Its TX0 transaction kept the change outside the CoinJoin and placed it in a separate account so users would be less likely to spend it accidentally with mixed coins. That was useful. It did not make the toxic change disappear. Samourai itself later called those coins “unmixed toxic change” while proposing a way to swap them into Monero. TX0 publicly joined the deposit inputs, created fixed-denomination premix outputs, and exposed which first Whirlpool rounds spent them. Peeling change off before the CoinJoin did not create another on-chain break between that change and the first mix. It moved the point where the change appeared. Fixed denominations created costs at both ends. A user could have to combine inputs publicly to enter a pool. Later, an ordinary payment would rarely equal one pool denomination, so the user could have to combine post-mix outputs and create new change. Equal-output CoinJoins still provided privacy. Remix counts alone could not show whether that privacy survived the eventual spend. The coordinator-fee address revealed another double standard. In 2020, Samourai condemned Wasabi’s reuse of a coordinator-fee address in absolute terms and said there was “no going back” from the damage. In October 2023, Kruw reported that Whirlpool’s coordinator had reused one fee address across 37 transactions. In one cited transaction, 36 outputs from that address were consolidated as inputs. The archived report survives. That reuse does not itself prove Whirlpool users were demixed. The issue is the standard Samourai applied: it described address reuse in Wasabi as irreversible architectural damage, while Kruw says his equivalent report about Whirlpool was deleted. Precision matters in both directions The record contains real Samourai security failures, ambiguous claims, and some historical mislabeling. They should not be treated as one undifferentiated charge sheet. In 2021, an independent researcher disclosed a genuine local PIN-bypass weakness. Restarting the app reset the attempt counter; wallet metadata required for an offline PIN search was available on the device; and the PIN space was small. The issue became CVE-2021-36689. That was a defined security failure with a specific version and threat model. It was not evidence that every Samourai wallet could be drained remotely. My SamouraiLeaks Part 3 investigation concerned an earlier and different codebase: the Blockchain.info Android wallet William led before Samourai. That repository contained a generator that fetched entropy from Random.org over unencrypted HTTP. Under a narrow fallback path on older Android devices, a redirect combined with failed local entropy could produce deterministic key material. Ars Technica reported the conditions and risks in 2015. That history documents a serious engineering failure under particular conditions. It does not establish that every Samourai wallet used broken randomness or that William stole anybody’s coins. Those distinctions are what responsible security disclosure requires: what happened, who was affected, what is inferred, and what remains unknown. Samourai’s communications culture often treated those distinctions as weakness when answering critics, then demanded endless qualification when scrutiny turned inward. When you wrestle with a pig, you both get dirty The public posts document individual incidents, but they cannot fully convey their cumulative effect over several years. I began to approach technical conversations as possible trials of character because bug reports, imprecise reporting, and edited recordings could all be reframed as evidence of bad intent. Leaving a false claim unanswered allowed it to spread. Answering prolonged the conflict. I spent time preserving evidence that I wanted to spend on code. Friends and independent developers had to decide whether correcting the record was worth becoming the next target. I did not handle that well. I called the project “Scamourai” and swore at them. In 2019, CoinDesk quoted one of my replies simply saying, “Fuck you.” That anger produced little of value. The childish nickname allowed a long evidentiary record to be mistaken for reciprocal mudslinging and made it easier for outsiders to conclude that both sides were merely marketing tribes. I also sometimes spoke with more certainty than the evidence allowed. Receiving an xpub, retaining it, selling it, and maliciously querying it are separate claims. I knew the default backend received wallet-level public information. Before the server analysis became public, I did not know everything Samourai retained or did with it. I should have marked those boundaries in an angry tweet as carefully as I would in a protocol review. I regret the way I spoke. It made the documented issues easier to dismiss. Threats and doxxing By April 2023, the conflict had passed far beyond professional hostility. I received multiple threats that I understood as death threats from William Hill. I also received anonymous private threats during the same campaign. The screenshots cannot establish who controlled those anonymous accounts, so I distinguish them from Hill’s public posts. One anonymous message sent me a full address in Besenyszög. I censored the street-level portion before preserving it. Another sender claimed to have checked an address and seen me and my “stinking tribe,” asked whether I thought I could stay safe, and ended: “Don’t worry Nopara. We shall meet. Won’t be pretty on your end.” The screenshots establish what I received. They do not establish who operated the anonymous accounts. Hill’s public conduct requires less inference. He posted my parents’ home address more than once. I will not reproduce or link to those posts, because documenting doxxing does not require doing it again. On April 18, 2023, the official Samourai Wallet account posted “Snitches get stitches”. Two days later, Hill addressed me directly: “As a die hard collaborator, you deserve much worse.” “Let’s see how this plays out, OK bud?” The attached image showed armed men surrounding a seated captive whose head was being shaved. I understood the combination of those words and that image as a threat. The post remains available here. In February 2024, Hill wrote that I was “way overdue to get yours” and appended the name of my parents’ town. A follower replied: “Hope he gets stitches and ends up in a ditch.” Hill answered: “Yes.” “Soon.” The first post and Hill’s reply remain public. Six weeks later, Hill wrote: “It ain’t over until the fat boy is gutted (see bio).” He placed those words above Yasushi Nagao’s famous photograph of the onstage assassination of Japanese Socialist Party chairman Inejirō Asanuma. I had originally misremembered the victim as a Japanese prime minister. The recovered post identifies the photograph correctly. That correction does not change the nature of the post. As preserved on July 10, 2026, Hill’s public profile still named me, repeated the “gutted” language, and appended the small town where my parents live. Publishing my family’s location beside violent language was intimidation. What the server seizure revealed When Samourai’s founders were arrested in April 2024, I refused to treat the indictment as a verdict. Privacy software is not money laundering simply because criminals use it. The legal boundary around noncustodial software was—and remains—important. But law enforcement also seized Samourai’s servers, and later court filings addressed the technical issues I had been raising for years. In October 2025, the government said its server analysis showed that Rodriguez and Hill had retained enough information to trace or “demix” many mobile users’ Whirlpool transactions. By cross-referencing stored xpubs with past, present, and future Whirlpool transactions, an analyst could connect inputs and outputs through complex analysis. The filing stated an important limit: this did not by itself connect those transactions to real-world identities. The defense did not deny xpub collection. Hill’s sentencing submission tried to recast it as a functional necessity: users without their own nodes needed the backend to calculate balances, it said, and the design affected “only 20%” of Whirlpool users. That was a consequence of Samourai’s chosen architecture, not a universal requirement of light wallets. Wasabi obtained block filters and checked addresses on the client without giving our server the wallet’s xpub. The filing supplied no citation, methodology, underlying counts, or independent measurement for its 20 percent figure. It may have been a figure provided by Samourai and repeated by its lawyers. The public submission gives us no way to know. Even if accepted for the sake of argument, one in five Whirlpool users is not trivial. More importantly, the argument conceded the architecture I had objected to: A class of users gave its wallet graph to Samourai’s infrastructure. Samourai retained that information. The seizure placed it in government hands. The government’s “demix” finding is a representation in a sentencing memorandum, not an independently published forensic report. That qualification matters. So does the fact that Hill’s own post-seizure concern was not primarily Whirlpool itself, but “the wallet backends (xpubs).” The darknet double standard The June 2025 superseding indictment reproduced private messages and Dread posts in which Hill steered people who openly described criminal proceeds away from a competing mixer and toward Whirlpool. It alleged that Rodriguez knew Hill was doing substantial promotional work on Dread. This mattered because Samourai and OXT had repeatedly used alleged criminal use of Wasabi as part of their public case against us. The later record showed Samourai pursuing those same users as customers. On Dread, competitor disparagement was not abstract privacy research. It was a sales pitch aimed at people asking how to conceal criminal proceeds. In August 2025, Rodriguez and Hill each pleaded guilty to conspiring to operate a money-transmitting business knowing it transmitted crime proceeds. The money-laundering conspiracy count was dropped through their plea agreements. In November, Rodriguez received five years in prison and Hill four. The sentences did not resolve the software arguments. The prosecution also raised troubling due-process questions. Before the pleas, the defense argued that prosecutors had disclosed too late a FinCEN communication saying Samourai’s lack of control over users’ keys strongly suggested it was not a money-services business under FinCEN’s rules. The government disputed the significance of that communication. Anyone who cares about open-source privacy software should care about that issue too. The lies and hypocrisies Developers can be mistaken, remember events differently, or speak with unjustified confidence. I use “lie” more narrowly: a materially false account repeated after contrary evidence has been presented because the false version remains useful. By that standard: The ZeroLink co-creation story was a lie. The framework predated Samourai’s involvement. Its first contribution fixed typos. Samourai kept repeating the joint-origin account after I challenged it with the repository. The claim that I admitted Wasabi supplied its own liquidity was false. The journalist corrected the interpretation, but Samourai continued promoting the damaging version without my correction. The categorical Tor answer was false or recklessly certain. Rodriguez insulted the person asking, and the code later added the identity change the question had asked about. “We are a full node wallet. Always have been” was false. Without Dojo, the Android application was a light client of Samourai’s backend. The coordinator answer was an evasion. The Whirlpool coordinator may not have handled xpubs, but Samourai’s wallet backend did. OXT was not an independent referee. It was acquired, owned, and operated by Samourai while presenting severe claims against Samourai’s main competitor under a research label. Samourai’s position on surveillance was hypocritical. It denounced blockchain-surveillance companies while operating a tracing and wallet-attribution tool and collecting wallet maps on its default backend. Its position on address reuse was a double standard. It described Wasabi’s reuse as irreversible architectural damage, while equivalent reuse later appeared in Whirlpool. Its use of criminal association was selective. It attacked Wasabi through alleged criminal use while privately promoting Whirlpool to darknet users describing criminal proceeds. Its central privacy promise was contradicted by its defaults. The wallet sent xpubs to Samourai’s hosted backend and left Tor off unless the user enabled it. In that configuration, the same service could receive both the wallet graph and the connecting IP address. I use the name “Scamourai” to describe what I see as a false central promise, not as a legal accusation of fraud. The product sold resistance to surveillance while placing its operator in a position to surveil. It promoted verification while asking default users to trust that Samourai would not misuse wallet information its servers retained. To me, that went beyond imperfect privacy because the contradiction was built into the default architecture. Post-mortem The lasting damage was not only personal. It affected the authorship record and the possibility of productive competition. I gave TDevD more credit than the repository justified. Samourai inflated that credit into co-creation. Minor edits became joint research through repetition. The same culture made correction look like surrender and uncertainty look like weakness, turning technical competition into personal hostility. I contributed to that hostility by answering contempt with contempt. I cannot undo those words, but I can document the history more carefully now. Future privacy developers should not take this essay as a request to trust me or as a rule that every server and coordinator is unacceptable. The practical lesson is simpler: examine what an operator can learn if its infrastructure is compromised, coerced, hacked, or seized. Team identity, marketing, and a founder’s character are not privacy guarantees. A sound privacy protocol should continue protecting its users when trust in the operator fails. That is the standard I tried to build into ZeroLink. It is also the standard Samourai told its users to expect. The seized servers show why the difference mattered.

10h ago

---

**[Cold storage vs. ETFs](https://www.reddit.com/r/Bitcoin/comments/1uti3ju/cold_storage_vs_etfs/)**

At 46 years old and minimal retirement savings so far, I've been absorbing alot of people's perspectives on the best route for achieving my goals in a 15-yearish window. I'm unlikely to live to see hyperbitcoinization or the collapse of the fiat system. It seems like the most rational, reasonable approach would be to heavy index funds along with some Bitcoin ETFs. Safe and uncomplicated. I'm going with real Bitcoin in cold storage. Why? Because it stirs something in me. It makes me feel like I'm part of a revolution that the world desperately needs, rather than simply riding it's coattails to get my basic needs met. It feels more like living life rather than just prolonging it. That to me is worth some extra risk and effort.

17h ago

---

**[I built Freeport - a P2P marketplace over Nostr with a built-in self-custodial Lightning wallet](https://www.reddit.com/r/Bitcoin/comments/1utowmn/i_built_freeport_a_p2p_marketplace_over_nostr/)**

Freeport is a P2P marketplace (rides, services, goods) running entirely on Nostr relays - no server, no middleman. It now has payments built in: - Self-custodial Lightning (Breez SDK / Spark) - the app never holds funds - Wallet key derived from your Nostr key: one backup covers identity + wallet - No signup - keypair generated on-device, optional passkey login - Lightning address, bolt11, on-chain - Confirmed deals get a Pay button / QR with the agreed amount, auto-converted from fiat Fun fact: you can download the HTML file from releases page to run the whole app 😎

12h ago

---

**[This sub is full of troll but bitcoin never trolls](https://www.reddit.com/r/Bitcoin/comments/1utxuna/this_sub_is_full_of_troll_but_bitcoin_never_trolls/)**

As an ex troller this sub is full of troll, price is just as usual, every cycle. But the people are like to troll. Real life.

6h ago

---

**[When BTC shows you some mercy](https://www.reddit.com/r/Bitcoin/comments/1uspu5o/when_btc_shows_you_some_mercy/)**

1d ago

---

---

## Google News: "bitcoin"

**[Bitcoin halving cycle history challenges $300,000–$500,000 moonshot forecasts](https://www.coindesk.com/markets/2026/07/10/bitcoin-analysts-predict-usd300-000-usd500-000-price-in-2029-the-math-says-no)**

Analysts predict a rally to $300,000 or more by 2029. But key data suggests the era of moonshots may be over.

CoinDesk • 1d ago

---

**[Bitcoin, ether ETFs snap eight-week outflow streaks with $282 million combined inflow](https://www.theblock.co/post/407957/bitcoin-ether-etfs-snap-eight-week-outflow-streaks-with-282-million-combined-inflow)**

The preceding eight weeks drained a combined $9.46 billion from the two groups, meaning this week’s rebound recovered only about 3% of those outflows.

The Block • 13h ago

---

**[Anthony Scaramucci's Model Portfolio: 30% to Bitcoin, Some Gold, 'Bet the Long Term of the US'](https://finance.yahoo.com/markets/crypto/articles/anthony-scaramuccis-model-portfolio-30-120126142.html)**

SkyBridge Capital founder Anthony Scaramucci maintains his long-term bullish stance on Bitcoin, saying that he believes artificial intelligence is likely in bubble territory. Scaramucci’s 30% BTC Allocation In an interview with Phil Rose on Thursday, Scaramucci attributed Bitcoin’s recent correction...

Yahoo Finance • 16h ago

---

**[Eric Trump’s Bitcoin Bet Erases $600 Million From Family Fortune](https://www.bloomberg.com/news/articles/2026-07-09/eric-trump-s-bitcoin-bet-erases-600-million-from-family-fortune)**

Bloomberg.com • 2d ago

---

**[Michael Saylor’s recent Bitcoin sales are a worry for crypto investors](https://nypost.com/2026/07/10/business/michael-saylors-recent-bitcoin-sales-are-a-worry-for-crypto-investors/)**

Is Saylor going to turn the current Bitcoin winter into the storm of the century for crypto?

New York Post • 1d ago

---

**[Bitcoin Is The Hardest Hurdle Rate To Beat, Says Strive CEO Matt Cole, And ‘Cash Is Almost Irresponsible’](https://www.tradingview.com/news/stocktwits:531895894094b:0-bitcoin-is-the-hardest-hurdle-rate-to-beat-says-strive-ceo-matt-cole-and-cash-is-almost-irresponsible/)**

Strive (ASST) CEO Matt Cole said that Bitcoin (BTC) has become a corporate "hurdle rate,” the benchmark companies should measure their capital's performance against, rather than traditional returns."Bitcoin is the hardest hurdle rate to beat," Cole said in a Bitcoin Magazine interview on Wednesday…

TradingView • 12h ago

---

**[Bitcoin holds gains above $64,000 as U.S. crypto policy remains in focus](https://www.investing.com/news/cryptocurrency-news/bitcoin-stays-above-64000-as-us-crypto-policy-advances-adoption-grows-4787225)**

Investing.com • 18h ago

---

**[Even with Gold Below $4,150 and Bitcoin Under $64,000, I'd Still Rather Buy This Unstoppable Dividend Stock in July](https://www.fool.com/investing/2026/07/10/even-with-gold-below-4150-and-bitcoin-under-64000/)**

Gold and Bitcoin have been in a funk, and so has this global consumer staples giant, but a business can grow.

The Motley Fool • 1d ago

---

**[Bitcoin treasury company sells 48% of holdings to repay debt](https://www.thestreet.com/crypto/markets/bitcoin-treasury-company-sells-48-of-holdings-to-repay-debt)**

thestreet.com • 1d ago

---

**[Eric Trump’s bitcoin bet erases $600 million from family fortune](https://www.staradvertiser.com/2026/07/10/breaking-news/eric-trumps-bitcoin-bet-erases-600-million-from-family-fortune/)**

American Bitcoin Corp. was built around a simple idea: that owning and mining bitcoin would be enough to mint money.

Honolulu Star-Advertiser • 1d ago

---

---

## HackerNews: "bitcoin"

**[Strategy sells $216M of Bitcoin as it abandons 'never sell' mantra](https://news.ycombinator.com/item?id=48807923)**

Crypto-treasury giant Strategy sold $216 million of Bitcoin last week – a sign that it is abandoning co-founder Michael Saylor’s “Never sell your Bitcoin” mantra as a slumping digital asset market …

⬆️ 5 • 💬 2 • 5d ago • [New York Post](https://nypost.com/2026/07/06/business/michael-saylors-strategy-sells-216m-of-bitcoin-as-it-abandons-never-sell-mantra/)

---

**[Bull Bitcoin challenges EU's DAC8 crypto surveillance rules in French court](https://news.ycombinator.com/item?id=48839604)**

Bull Bitcoin, a MiCA-licensed non-custodial exchange, has filed a landmark legal challenge before France's Conseil d'État to annul Decree No. 2025-1276, which implements the EU's DAC8 crypto tax reporting directive. The exchange argues the rules create a mass surveillance database linking identities and crypto activity, endangering holders' physical safety.

⬆️ 3 • 💬 1 • 3d ago • [The Coin Headlines](https://thecoinheadlines.com/crypto/bull-bitcoin-challenges-eus-dac8-crypto-surveillance-rules-in-french-court/article-25451/)

---

**[Satd: Bitcoin Transaction Filtering Language](https://news.ycombinator.com/item?id=48837026)**

Operator, integrator, and packager reference for satd — a Bitcoin Core-compatible full node in Rust.

⬆️ 2 • 💬 1 • 3d ago • [epochbtc.github.io](https://epochbtc.github.io/satd/policy.html)

---

**[Pipe Bitcoin's mempool into Gource and watch blocks settle it live](https://news.ycombinator.com/item?id=48860722)**

ai experiments reproducible on a single consumer GPU - VitaAI-SCG/one-gpu-lab

⬆️ 1 • 💬 0 • 1d ago • [GitHub](https://github.com/VitaAI-SCG/one-gpu-lab/tree/main/episodes/14-the-live-tree)

---

**[Could Strategy's Potential Bitcoin Sale Reshape Market Sentiment?](https://news.ycombinator.com/item?id=48859909)**

Read this crypto post from greatHydra_997 posted on 2026/07/10 on CoinMarketCap’s Community message board. See user comments and interaction, plus replies from greatHydra_997 as they discuss up-to-date cryptocurrency topics.

⬆️ 1 • 💬 0 • 1d ago • [coinmarketcap.com](https://coinmarketcap.com/community/post/377668818/)

---

**[Show HN: Glyph a blockchain where the proof-of-work is neural network inference](https://news.ycombinator.com/item?id=48795126)**

Contribute to raphaelwkago69-create/GLYPH development by creating an account on GitHub.

⬆️ 2 • 💬 0 • 6d ago • [GitHub](https://github.com/raphaelwkago69-create/GLYPH)

---

**[Why developers are ditching GitHub for Codeberg and self-hosting alternatives](https://news.ycombinator.com/item?id=48842611)**

It’s supposed to be a decentralized service, after all...

⬆️ 365 • 💬 256 • 2d ago • [How-To Geek](https://www.howtogeek.com/why-developers-are-ditching-github-for-codeberg-and-self-hosting-alternatives/)

---

**[Ditching Vagrant: VMs with KVM and Virsh on Debian](https://news.ycombinator.com/item?id=48805342)**

⬆️ 99 • 💬 45 • 5d ago • [benjamintoll.com](https://benjamintoll.com/2026/06/29/on-ditching-vagrant/)

---

---

## YouTube Videos: "bitcoin"

**[Has Bitcoin Hit The Bottom?](https://www.youtube.com/watch?v=TP9AEulCw9g)**

Jordi Visser (@JordiVisserLabs) is a veteran macro investor with 30+ years of experience and the author of the VisserLabs ...

📺 Anthony Pompliano

👁️ 46K • 👍 2K • 💬 78 • ⏱️ 52:26 • 15h ago

---

**[Data Scientist WARNS Bitcoin Holders ⮕ “History is REPEATING!”](https://www.youtube.com/watch?v=FjmHBEzHUZw)**

Data Scientist Ben Cowen Issues DIRE WARNING to Bitcoin Holders “History is REPEATING!” 🎟️ Use Code “AD2026” for 10% ...

📺 Altcoin Daily

👁️ 29K • 👍 2K • 💬 142 • ⏱️ 27:14 • 12h ago

---

**[Bitcoin Already Won | Wall Street Just Doesn&#39;t Know It Yet!](https://www.youtube.com/watch?v=9CwwPwv8Yeg)**

For years, Bitcoin was dismissed as a scam that governments would eventually ban. Now the conversation has shifted from ...

📺 Simply Bitcoin

👁️ 22K • 👍 2K • 💬 129 • ⏱️ 14:28 • 1d ago

---

**[Lyn Alden - &quot;Something Is VERY Wrong With Bitcoin &amp; Nobody Is Talking About it&quot;](https://www.youtube.com/watch?v=Oi2wSqHzwPo)**

Grow your crypto and gold tax-free with iTrustCapital IRA — no monthly fees, and get a $100 bonus when you fund your account.

📺 Savvy Finance

👁️ 5K • 👍 172 • 💬 42 • ⏱️ 17:34 • 1d ago

---

**[MONETARY BLOW-UP: Coinbase FIRES BACK at Jamie Dimon&#39;s crypto criticism](https://www.youtube.com/watch?v=PSXf8xhmRy8)**

Coinbase Vice Chair Ryan Vangrack joins 'Mornings with Maria' to discuss Congress' latest push to pass the CLAIRTY Act, Jamie ...

📺 Fox Business

👁️ 96K • 👍 2K • 💬 726 • ⏱️ 12:46 • 1d ago

---

**[Bitcoin About To Print Its First Bull Market Signal In 3 Years...](https://www.youtube.com/watch?v=zJIHEcOd88w)**

My Links: ▻ Get the risk models I use to track accumulation and exit zones. Free trial https://app.cryptocapitalventure.ai Intro ...

📺 Crypto Capital Venture

👁️ 10K • 👍 604 • 💬 255 • ⏱️ 17:47 • 1d ago

---

**[Bitcoin is Quietly HOLDING This Key Level… (HERE’S WHAT IT MEANS)](https://www.youtube.com/watch?v=5_v4BZvddlo)**

Bitcoin is quietly holding a key level of support and is appearing to bounce from that level. Could this be important for bitcoin in ...

📺 Alessio Rastani

👁️ 19K • 👍 2K • 💬 389 • ⏱️ 9:13 • 1d ago

---

**[Bitcoin &amp; Crypto Good News Friday!](https://www.youtube.com/watch?v=UcXX9BE8VhQ)**

From Trump to Coinbase to ETH we have NOTHING BUT GOOD NEWS TODAY! (rare) Join us Nov. 20-22nd In Miami for Ben's ...

📺 Digital Asset News

👁️ 9K • 👍 604 • 💬 70 • ⏱️ 27:47 • 1d ago

---

**[Bitcoin: Dubious Speculation](https://www.youtube.com/watch?v=sigSZCnSa6M)**

Bitcoin has a way of making investors question everything during the most difficult parts of the cycle. In this video, we take a step ...

📺 Benjamin Cowen

👁️ 91K • 👍 5K • 💬 346 • ⏱️ 29:53 • 1d ago

---

**[Is The Bitcoin Power Law Broken? | Matthew Mezinskis](https://www.youtube.com/watch?v=oJXECyP_oas)**

I think in ten years, the financial system and the Bitcoin system are going to collide.” Matthew Mezinskis is a macroeconomic ...

📺 What Bitcoin Did

👁️ 12K • 👍 397 • 💬 285 • ⏱️ 1:40:44 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
