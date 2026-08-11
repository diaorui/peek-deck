---
title: Bitcoin Dashboard
description: Live Bitcoin monitoring dashboard
category: crypto
page_id: bitcoin
updated: '2026-08-11T23:40:10.255686+00:00'
url: https://peekdeck.ruidiao.dev/bitcoin.html
markdown_url: https://peekdeck.ruidiao.dev/bitcoin.md
widgets: 8
data_types:
- social
- videos
- news
- cryptocurrency
---

# Bitcoin Dashboard

Live Bitcoin monitoring dashboard

**Last Updated:** August 11, 2026 at 23:40 UTC  
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

### $63,687.04

---

## Bitcoin Chart

**24h:** -0.7%  
**7d:** -1.6%  
**30d:** +2.0%  
**90d:** -21.5%  
**1y:** -47.1%  

---

## Bitcoin Market Stats

**Market Cap:** $1275.44B
Rank #1

**Circulating Supply:** 20,068,915 BTC
95.6% of max

**All-Time High:** $126,080.00
-49.6%

**All-Time Low:** $67.81
+93631.0%

---

## Fear & Greed Index

### 29
**FEAR**

---

## Reddit: r/Bitcoin

**[The guy you convinced to buy bitcoin at $126K and you with a cost basis of $10K](https://www.reddit.com/r/Bitcoin/comments/1vlf7ap/the_guy_you_convinced_to_buy_bitcoin_at_126k_and/)**

11h ago

---

**[Whatever Bitcoin does next, I’ve already predicted it!](https://www.reddit.com/r/Bitcoin/comments/1vlarqf/whatever_bitcoin_does_next_ive_already_predicted/)**

16h ago

---

**[My brain at 2 AM:](https://www.reddit.com/r/Bitcoin/comments/1vlcecm/my_brain_at_2_am/)**

14h ago

---

**[The average fiat currency dies in 27 years.](https://www.reddit.com/r/Bitcoin/comments/1vlv5yj/the_average_fiat_currency_dies_in_27_years/)**

1h ago

---

**[How corporations like McDonalds benefit from our rigged theft-based monetary system](https://www.reddit.com/r/Bitcoin/comments/1vlv7pk/how_corporations_like_mcdonalds_benefit_from_our/)**

1h ago

---

**[If there’s ever a button to smash, this would be the one.](https://www.reddit.com/r/Bitcoin/comments/1vlldnl/if_theres_ever_a_button_to_smash_this_would_be/)**

7h ago

---

**[Could something like Coldcard happen to Ledger?](https://www.reddit.com/r/Bitcoin/comments/1vlfrec/could_something_like_coldcard_happen_to_ledger/)**

Well, that’s what I wanna learn more about. What are the best wallets out there these days? How to get maximum security? Explain like I’m dumb, which I am lately. They promised us freedom, in fact they take it all away lately.

11h ago

---

**[Why did Coinkite destroy its inventory?](https://www.reddit.com/r/Bitcoin/comments/1vld3rt/why_did_coinkite_destroy_its_inventory/)**

The company published a note claiming they destroyed all their inventory (devices affected by the bug). Why? Why couldn’t they just reflash them with the fixed firmware? I can’t stop thinking there is something else to it. Should users of coldcard devices be concerned? They are being asked to upgrade firmware and be at peace of mind. Why didn’t Coinkite do 5he same? Could there be more we are not being told and involves a hardware-level bug?

🔗 [COINKITE Blog](https://blog.coinkite.com/update-sunday/) • 13h ago

---

**[Seed Generator Built with Dice and a Calculator](https://www.reddit.com/r/Bitcoin/comments/1vlbzc5/seed_generator_built_with_dice_and_a_calculator/)**

I've been into Bitcoin for about 9 years now. In my second year, I bought a Ledger Nano S, and it served me well. Just about when I was running out of storage on the Nano S, the Nano S Plus was released, which I used happily up until recently. I run my own node and mempool, and I've been using a multisig wallet set up with my Ledgers. During the Amazon Prime Day sale last June, I picked up a Trezor Safe 3 and a Blockstream Jade, and upgraded my multisig setup using hardware from different vendors. Then came the recent Coldcard drama... which inspired me to build my own seed generator using dice roll. I knew that SeedSigner could generate a seed from D6 dice rolls, so I tried building one with a Raspberry Pi I had lying around. Unfortunately, I didn't have the right screen for it, so that plan fell through. After giving it some thought, I realized I could just use the Python feature on my Casio calculator to build one. I coded it up, and it actually works perfectly! ^^ P.S. This program was built using the MicroPython built into modern Casio graphing calculators. Instead of using any built-in dice tool on the calculator, you roll actual physical dice 99+ times and sequentially input the results via the keypad. The program then performs a SHA-256 operation, handles checksum padding and 11-bit slicing according to BIP39 standards, and generates a 24-word mnemonic. Since MicroPython is stripped down to the bare essentials and lacks a built-in hashlib, I actually had to implement the SHA-256 algorithm from scratch. This program brings the physical dice-based entropy generation found in devices like Coldcard, SeedSigner, and Keystone Pro right onto a graphing calculator! p.s.2 A site someone told me about recently was helpful. https://hashexplained.com/entropy Source for casio calc. dice.py - This is a pretty sloppy/clunky piece of code that I'm kind of embarrassed to share, but I'm posting it because some people asked for it. - Caution: This program does not check the number of input dice. It will run even if you enter 99 or fewer dice, and will generate a mnemonic even if you roll a die just once. When passed through the sha256 function, it outputs 256-bit data, which is then used to create the mnemonic. I wanted to see why a seed is generated without any issues even when low-entropy data is inputted. Please be careful when using it in practice. --------------------------------------------------------------------------- # --- [Casio File-less BIP39 (Ultimate)] --- _K = ( 0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2 ) class PureSHA256: def __init__(self, data=None): self.h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19] self.data = [] self.bytes_processed = 0 if data: self.update(data) def _rotr(self, x, n): return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF def update(self, data): self.data.extend(data) while len(self.data) >= 64: self._process_chunk(self.data[:64]) self.data = self.data[64:] self.bytes_processed += 64 def _process_chunk(self, chunk): w = [0] * 64 for i in range(16): idx = i * 4 w[i] = (chunk[idx] << 24) | (chunk[idx+1] << 16) | (chunk[idx+2] << 8) | chunk[idx+3] for i in range(16, 64): s0 = self._rotr(w[i-15], 7) ^ self._rotr(w[i-15], 18) ^ (w[i-15] >> 3) s1 = self._rotr(w[i-2], 17) ^ self._rotr(w[i-2], 19) ^ (w[i-2] >> 10) w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF a, b, c, d, e, f, g, h = self.h for i in range(64): S1 = self._rotr(e, 6) ^ self._rotr(e, 11) ^ self._rotr(e, 25) ch = (e & f) ^ ((~e) & g) temp1 = (h + S1 + ch + _K[i] + w[i]) & 0xFFFFFFFF S0 = self._rotr(a, 2) ^ self._rotr(a, 13) ^ self._rotr(a, 22) maj = (a & b) ^ (a & c) ^ (b & c) temp2 = (S0 + maj) & 0xFFFFFFFF h, g, f = g, f, e e = (d + temp1) & 0xFFFFFFFF d, c, b = c, b, a a = (temp1 + temp2) & 0xFFFFFFFF self.h = [(x + y) & 0xFFFFFFFF for x, y in zip(self.h, [a, b, c, d, e, f, g, h])] def digest(self): length = (self.bytes_processed + len(self.data)) * 8 self.data.append(0x80) while (len(self.data) % 64) != 56: self.data.append(0x00) for i in range(7, -1, -1): self.data.append((length >> (i * 8)) & 0xFF) self._process_chunk(self.data) out = [] for val in self.h: out.append((val >> 24) & 0xFF) out.append((val >> 16) & 0xFF) out.append((val >> 8) & 0xFF) out.append(val & 0xFF) return out # 동적 생성된 128개의 청크 튜플 삽입 W = ( "abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid", "acoustic acquire across act action actor actress actual adapt add addict address adjust admit adult advance", "advice aerobic affair afford afraid again age agent agree ahead aim air airport aisle alarm album", "alcohol alert alien all alley allow almost alone alpha already also alter always amateur amazing among", "amount amused analyst anchor ancient anger angle angry animal ankle announce annual another answer antenna antique", "anxiety any apart apology appear apple approve april arch arctic area arena argue arm armed armor", "army around arrange arrest arrive arrow art artefact artist artwork ask aspect assault asset assist assume", "asthma athlete atom attack attend attitude attract auction audit august aunt author auto autumn average avocado", "avoid awake aware away awesome awful awkward axis baby bachelor bacon badge bag balance balcony ball", "bamboo banana banner bar barely bargain barrel base basic basket battle beach bean beauty because become", "beef before begin behave behind believe below belt bench benefit best betray better between beyond bicycle", "bid bike bind biology bird birth bitter black blade blame blanket blast bleak bless blind blood", "blossom blouse blue blur blush board boat body boil bomb bone bonus book boost border boring", "borrow boss bottom bounce box boy bracket brain brand brass brave bread breeze brick bridge brief", "bright bring brisk broccoli broken bronze broom brother brown brush bubble buddy budget buffalo build bulb", "bulk bullet bundle bunker burden burger burst bus business busy butter buyer buzz cabbage cabin cable", "cactus cage cake call calm camera camp can canal cancel candy cannon canoe canvas canyon capable", "capital captain car carbon card cargo carpet carry cart case cash casino castle casual cat catalog", "catch category cattle caught cause caution cave ceiling celery cement census century cereal certain chair chalk", "champion change chaos chapter charge chase chat cheap check cheese chef cherry chest chicken chief child", "chimney choice choose chronic chuckle chunk churn cigar cinnamon circle citizen city civil claim clap clarify", "claw clay clean clerk clever click client cliff climb clinic clip clock clog close cloth cloud", "clown club clump cluster clutch coach coast coconut code coffee coil coin collect color column combine", "come comfort comic common company concert conduct confirm congress connect consider control convince cook cool copper", "copy coral core corn correct cost cotton couch country couple course cousin cover coyote crack cradle", "craft cram crane crash crater crawl crazy cream credit creek crew cricket crime crisp critic crop", "cross crouch crowd crucial cruel cruise crumble crunch crush cry crystal cube culture cup cupboard curious", "current curtain curve cushion custom cute cycle dad damage damp dance danger daring dash daughter dawn", "day deal debate debris decade december decide decline decorate decrease deer defense define defy degree delay", "deliver demand demise denial dentist deny depart depend deposit depth deputy derive describe desert design desk", "despair destroy detail detect develop device devote diagram dial diamond diary dice diesel diet differ digital", "dignity dilemma dinner dinosaur direct dirt disagree discover disease dish dismiss disorder display distance divert divide", "divorce dizzy doctor document dog doll dolphin domain donate donkey donor door dose double dove draft", "dragon drama drastic draw dream dress drift drill drink drip drive drop drum dry duck dumb", "dune during dust dutch duty dwarf dynamic eager eagle early earn earth easily east easy echo", "ecology economy edge edit educate effort egg eight either elbow elder electric elegant element elephant elevator", "elite else embark embody embrace emerge emotion employ empower empty enable enact end endless endorse enemy", "energy enforce engage engine enhance enjoy enlist enough enrich enroll ensure enter entire entry envelope episode", "equal equip era erase erode erosion error erupt escape essay essence estate eternal ethics evidence evil", "evoke evolve exact example excess exchange excite exclude excuse execute exercise exhaust exhibit exile exist exit", "exotic expand expect expire explain expose express extend extra eye eyebrow fabric face faculty fade faint", "faith fall false fame family famous fan fancy fantasy farm fashion fat fatal father fatigue fault", "favorite feature february federal fee feed feel female fence festival fetch fever few fiber fiction field", "figure file film filter final find fine finger finish fire firm first fiscal fish fit fitness", "fix flag flame flash flat flavor flee flight flip float flock floor flower fluid flush fly", "foam focus fog foil fold follow food foot force forest forget fork fortune forum forward fossil", "foster found fox fragile frame frequent fresh friend fringe frog front frost frown frozen fruit fuel", "fun funny furnace fury future gadget gain galaxy gallery game gap garage garbage garden garlic garment", "gas gasp gate gather gauge gaze general genius genre gentle genuine gesture ghost giant gift giggle", "ginger giraffe girl give glad glance glare glass glide glimpse globe gloom glory glove glow glue", "goat goddess gold good goose gorilla gospel gossip govern gown grab grace grain grant grape grass", "gravity great green grid grief grit grocery group grow grunt guard guess guide guilt guitar gun", "gym habit hair half hammer hamster hand happy harbor hard harsh harvest hat have hawk hazard", "head health heart heavy hedgehog height hello helmet help hen hero hidden high hill hint hip", "hire history hobby hockey hold hole holiday hollow home honey hood hope horn horror horse hospital", "host hotel hour hover hub huge human humble humor hundred hungry hunt hurdle hurry hurt husband", "hybrid ice icon idea identify idle ignore ill illegal illness image imitate immense immune impact impose", "improve impulse inch include income increase index indicate indoor industry infant inflict inform inhale inherit initial", "inject injury inmate inner innocent input inquiry insane insect inside inspire install intact interest into invest", "invite involve iron island isolate issue item ivory jacket jaguar jar jazz jealous jeans jelly jewel", "job join joke journey joy judge juice jump jungle junior junk just kangaroo keen keep ketchup", "key kick kid kidney kind kingdom kiss kit kitchen kite kitten kiwi knee knife knock know", "lab label labor ladder lady lake lamp language laptop large later latin laugh laundry lava law", "lawn lawsuit layer lazy leader leaf learn leave lecture left leg legal legend leisure lemon lend", "length lens leopard lesson letter level liar liberty library license life lift light like limb limit", "link lion liquid list little live lizard load loan lobster local lock logic lonely long loop", "lottery loud lounge love loyal lucky luggage lumber lunar lunch luxury lyrics machine mad magic magnet", "maid mail main major make mammal man manage mandate mango mansion manual maple marble march margin", "marine market marriage mask mass master match material math matrix matter maximum maze meadow mean measure", "meat mechanic medal media melody melt member memory mention menu mercy merge merit merry mesh message", "metal method middle midnight milk million mimic mind minimum minor minute miracle mirror misery miss mistake", "mix mixed mixture mobile model modify mom moment monitor monkey monster month moon moral more morning", "mosquito mother motion motor mountain mouse move movie much muffin mule multiply muscle museum mushroom music", "must mutual myself mystery myth naive name napkin narrow nasty nation nature near neck need negative", "neglect neither nephew nerve nest net network neutral never news next nice night noble noise nominee", "noodle normal north nose notable note nothing notice novel now nuclear number nurse nut oak obey", "object oblige obscure observe obtain obvious occur ocean october odor off offer office often oil okay", "old olive olympic omit once one onion online only open opera opinion oppose option orange orbit", "orchard order ordinary organ orient original orphan ostrich other outdoor outer output outside oval oven over", "own owner oxygen oyster ozone pact paddle page pair palace palm panda panel panic panther paper", "parade parent park parrot party pass patch path patient patrol pattern pause pave payment peace peanut", "pear peasant pelican pen penalty pencil people pepper perfect permit person pet phone photo phrase physical", "piano picnic picture piece pig pigeon pill pilot pink pioneer pipe pistol pitch pizza place planet", "plastic plate play please pledge pluck plug plunge poem poet point polar pole police pond pony", "pool popular portion position possible post potato pottery poverty powder power practice praise predict prefer prepare", "present pretty prevent price pride primary print priority prison private prize problem process produce profit program", "project promote proof property prosper protect proud provide public pudding pull pulp pulse pumpkin punch pupil", "puppy purchase purity purpose purse push put puzzle pyramid quality quantum quarter question quick quit quiz", "quote rabbit raccoon race rack radar radio rail rain raise rally ramp ranch random range rapid", "rare rate rather raven raw razor ready real reason rebel rebuild recall receive recipe record recycle", "reduce reflect reform refuse region regret regular reject relax release relief rely remain remember remind remove", "render renew rent reopen repair repeat replace report require rescue resemble resist resource response result retire", "retreat return reunion reveal review reward rhythm rib ribbon rice rich ride ridge rifle right rigid", "ring riot ripple risk ritual rival river road roast robot robust rocket romance roof rookie room", "rose rotate rough round route royal rubber rude rug rule run runway rural sad saddle sadness", "safe sail salad salmon salon salt salute same sample sand satisfy satoshi sauce sausage save say", "scale scan scare scatter scene scheme school science scissors scorpion scout scrap screen script scrub sea", "search season seat second secret section security seed seek segment select sell seminar senior sense sentence", "series service session settle setup seven shadow shaft shallow share shed shell sheriff shield shift shine", "ship shiver shock shoe shoot shop short shoulder shove shrimp shrug shuffle shy sibling sick side", "siege sight sign silent silk silly silver similar simple since sing siren sister situate six size", "skate sketch ski skill skin skirt skull slab slam sleep slender slice slide slight slim slogan", "slot slow slush small smart smile smoke smooth snack snake snap sniff snow soap soccer social", "sock soda soft solar soldier solid solution solve someone song soon sorry sort soul sound soup", "source south space spare spatial spawn speak special speed spell spend sphere spice spider spike spin", "spirit split spoil sponsor spoon sport spot spray spread spring spy square squeeze squirrel stable stadium", "staff stage stairs stamp stand start state stay steak steel stem step stereo stick still sting", "stock stomach stone stool story stove strategy street strike strong struggle student stuff stumble style subject", "submit subway success such sudden suffer sugar suggest suit summer sun sunny sunset super supply supreme", "sure surface surge surprise surround survey suspect sustain swallow swamp swap swarm swear sweet swift swim", "swing switch sword symbol symptom syrup system table tackle tag tail talent talk tank tape target", "task taste tattoo taxi teach team tell ten tenant tennis tent term test text thank that", "theme then theory there they thing this thought three thrive throw thumb thunder ticket tide tiger", "tilt timber time tiny tip tired tissue title toast tobacco today toddler toe together toilet token", "tomato tomorrow tone tongue tonight tool tooth top topic topple torch tornado tortoise toss total tourist", "toward tower town toy track trade traffic tragic train transfer trap trash travel tray treat tree", "trend trial tribe trick trigger trim trip trophy trouble truck true truly trumpet trust truth try", "tube tuition tumble tuna tunnel turkey turn turtle twelve twenty twice twin twist two type typical", "ugly umbrella unable unaware uncle uncover under undo unfair unfold unhappy uniform unique unit universe unknown", "unlock until unusual unveil update upgrade uphold upon upper upset urban urge usage use used useful", "useless usual utility vacant vacuum vague valid valley valve van vanish vapor various vast vault vehicle", "velvet vendor venture venue verb verify version very vessel veteran viable vibrant vicious victory video view", "village vintage violin virtual virus visa visit visual vital vivid vocal voice void volcano volume vote", "voyage wage wagon wait walk wall walnut want warfare warm warrior wash wasp waste water wave", "way wealth weapon wear weasel weather web wedding weekend weird welcome west wet whale what wheat", "wheel when where whip whisper wide width wife wild will win window wine wing wink winner", "winter wire wisdom wise wish witness wolf woman wonder wood wool word work world worry worth", "wrap wreck wrestle wrist write wrong yard year yellow you young youth zebra zero zone zoo" ) def get_word(index): chunk_idx = index // 16 word_idx = index % 16 s = W[chunk_idx] start = 0 for _ in range(word_idx): start = s.find(" ", start) + 1 end = s.find(" ", start) if end == -1: return s[start:] return s[start:end] def main(): print("=== BIP39 Dice Seed ===") print("Enter dice (1-6)") print("99 rolls rec.") dice_input = input("> ") for char in dice_input: if char not in "123456": print("Invalid input!") input("[Press EXE]") return print("\nGenerating...\n") dice_bytes = [] for char in dice_input: dice_bytes.append(ord(char)) entropy_hash = PureSHA256(dice_bytes) entropy_bytes = entropy_hash.digest() checksum_hash = PureSHA256(entropy_bytes) checksum_byte = checksum_hash.digest()[0] val = 0 for b in entropy_bytes: val = (val << 8) | b val = (val << 8) | checksum_byte words = [] for i in range(24): shift = (23 - i) * 11 index = (val >> shift) & 0x7FF words.append(get_word(index)) # 카시오 화면(가로 21자)에 맞춘 2열 배치 포맷 for i in range(0, 12, 2): print("%02d:%-7s %02d:%-7s" % (i+1, words[i][:7], i+2, words[i+1][:7])) input("[EXE for 13~24]") for i in range(12, 24, 2): print("%02d:%-7s %02d:%-7s" % (i+1, words[i][:7], i+2, words[i+1][:7])) print("-" * 15) print("DONE! PRESS RESTART") input("[Press EXE]") main()

14h ago

---

**[Traveling internationally with a hardware wallet: what's been your experience with customs/immigration?](https://www.reddit.com/r/Bitcoin/comments/1vljr6d/traveling_internationally_with_a_hardware_wallet/)**

Hey everyone, curious to hear people's real-world experiences with this. When traveling internationally, most countries require you to declare if you're carrying over $10k in cash or monetary instruments. Crypto creates a weird gray area for border control. Technically, carrying a hardware wallet isn't carrying money across the border. The funds reside on the blockchain, not on the device. It's fundamentally no different than carrying a phone with a banking app or a bank token device. That said, border control and immigration agents usually stick strictly to their playbook, and many might not understand or care about how the blockchain works if they inspect your bags. For those who travel often with hardware wallets: Have you ever been asked about your wallet by border agents? How do you handle declarations or questions if custom officials bring it up? What seems to be the broadly accepted or safest approach when crossing borders? Would love to hear how you guys approach this in practice!

8h ago

---

---

## Google News: "bitcoin"

**[Riot Platforms strikes deal with Anthropic as bitcoin miners shift focus to AI infrastructure](https://www.cnbc.com/2026/08/11/riot-platforms-signs-anthropic-deal-as-miners-shift-to-ai-infrastructure-.html)**

Bitcoin miner Riot Platform has struck a $9 billion, 20-year compute deal with Anthropic

cnbc.com • 5h ago

---

**[XRP, ETH price news: Ripple-linked token leads drop as traders eye $70,000 bitcoin](https://www.coindesk.com/markets/2026/08/11/xrp-ether-lead-crypto-losses-as-traders-eye-usd70-000-bitcoin-next)**

Bitcoin failed to hold $65,000 for a fourth day as an oil rally revived inflation worries before Wednesday's U.S. price data.

CoinDesk • 18h ago

---

**[Watch Bitcoin Will 'Survive' Cold Wallet Hack: Alex Thorn](https://www.bloomberg.com/news/videos/2026-08-11/bitcoin-will-survive-cold-wallet-hack-alex-thor-video)**

Bloomberg.com • 3h ago

---

**[After a $130 Million Hack of Coldcard, Money Is Flowing Into Bitcoin ETFs. Here's the Best Bitcoin ETF to Buy Right Now.](https://finance.yahoo.com/markets/crypto/articles/130-million-hack-coldcard-money-151200491.html)**

Institutions might start to win more trust from investors.

Yahoo Finance • 2d ago

---

**[Is Bitcoin Self-Custody Dead? Inside The Coldcard Hack](https://www.forbes.com/sites/davidbirnbaum/2026/08/11/is-bitcoin-self-custody-dead-inside-the-coldcard-hack/)**

The Coldcard hack has profoundly shaken the bitcoin community, challenging the very foundations of the bitcoin ethos. Is self-custody still worth it?

Forbes • 1h ago

---

**[Bitcoin Price Prediction: Can Bitcoin Reach $1 Million?](https://finance.yahoo.com/markets/crypto/articles/bitcoin-price-prediction-bitcoin-reach-225618780.html)**

Some of the biggest names in finance have staked their reputations on Bitcoin reaching seven figures, and their reasoning is harder to dismiss than it sounds. The real question is not whether it can happen, but what would have to go right for it to actually get there.

Yahoo Finance • 43m ago

---

**[Crypto Market Today, Aug. 11: Macro Worries Pull Bitcoin Below $64,000 and the SEC May Have a Regulatory Plan](https://finance.yahoo.com/markets/crypto/articles/crypto-market-today-aug-11-221427458.html)**

On Aug. 11, 2026, oil's rebound stoked fresh inflation concerns ahead of Wednesday's inflation data, keeping risk assets subdued.

Yahoo Finance • 1h ago

---

**[Strategy dumps yet more Bitcoin, latest $109 million sell-off comes amid a seven-week buying hiatus](https://fortune.com/2026/08/10/strategy-bitcoin-109-million-sell-off-seven-week-buying-hiatus/)**

The company’s fourth Bitcoin sale since June underscores its push to build cash and reassure investors.

Fortune • 1d ago

---

**[Pulling the plug on Bitcoin ATMs in Murfreesboro](https://www.wkrn.com/video/pulling-the-plug-on-bitcoin-atms-in-murfreesboro/12057869/)**

WKRN News 2 • 3h ago

---

**[Bitcoin slips toward $64,000 as traders await Wednesday's inflation test](https://www.theblock.co/news/markets/2026-08-11-bitcoin-slips-toward-64000-as-traders-await-wednesdays-inflation-test-411418)**

Bitcoin eased toward $64,000 before Wednesday's US CPI report, with analysts split on whether the stall breaks higher or reverses.

The Block • 9h ago

---

---

## HackerNews: "bitcoin"

**[Controversial Bitcoin fork BIP-110 mines two blocks, then stops](https://news.ycombinator.com/item?id=49245272)**

The breakaway chain inherited bitcoin’s mining difficulty with only a tiny share of hashpower, leaving blocks hours apart while both chains still accept the same transactions.

⬆️ 10 • 💬 1 • 1d ago • [coindesk.com](https://www.coindesk.com/tech/2026/08/09/controversial-bitcoin-fork-bip-110-mines-two-blocks-then-stops)

---

**[Bitcoin BIP110 mandatory activation this Saturday, how game theory will unfold?](https://news.ycombinator.com/item?id=49180531)**

Where do I stand on BIP-110 and the "spam war"? Discover why I believe this is a strategy of tension, the game theory behind this consensus battle, and why running a node and holding your own keys remains Bitcoin’s ultimate defense against corporate capture.

⬆️ 9 • 💬 4 • 6d ago • [simondixon.com](https://www.simondixon.com/blog/bip-110-the-spam-war-and-the-battle-nobody-wants-to-name-where-i-stand-simon-dixon)

---

**[After $140M hack, Bitcoin users 'soul-searching' over self-custody](https://news.ycombinator.com/item?id=49179540)**

A coding error in bitcoin wallets made by Coinkite Inc. allowed hackers to steal from individuals storing their own cryptocurrency

⬆️ 3 • 💬 0 • 6d ago • [The Globe and Mail](https://www.theglobeandmail.com/investing/article-after-140-million-hack-bitcoin-users-soul-searching-over-self-custody/)

---

**[What Bitcoin sextortion emails actually earned](https://news.ycombinator.com/item?id=49178750)**

Try out Artifacts created by Claude users

⬆️ 2 • 💬 0 • 6d ago • [claude.ai](https://claude.ai/code/artifact/4806cb5d-8582-460e-ab31-2a321f1b23cb)

---

**[Is your Bitcoin seed safe after Coldcard accident? What about iancoleman/bip39?](https://news.ycombinator.com/item?id=49207230)**

In late July 2026, Coldcard, the open-source hardware wallet many consider the gold standard in Bitcoin security, failed in the worst possible way.

A firmware integration error from March 2021 had silently replaced the device's hardware random number generator with a deterministic software PRNG, seeded only from the serial number

⬆️ 1 • 💬 1 • 4d ago • [Tech blog](https://grigio.org/is-you-bitcoin-seed-safe-after-coldcard-accident-what-about-iancoleman-bip39/)

---

**[MicroStrategy Sells More Bitcoin to Fix STRC Stock: Will It Work?](https://news.ycombinator.com/item?id=49249823)**

Strategy sold 1,690 Bitcoin for $108.6 million to buy back STRC shares still trading below their $100 par value.

⬆️ 1 • 💬 0 • 1d ago • [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/microstrategy-sells-more-bitcoin-fix-125133681.html)

---

**[Mining Bitcoin with 2013 USB sticks, a Jalapeño and my phone (pure Python)](https://news.ycombinator.com/item?id=49211160)**

Solo Bitcoin lottery mining with 2013 USB ASIC sticks, your CPU, or any phone browser - pure Python, retro CRT dashboard - 03012009BTC/miners-bitcoin-lottery

⬆️ 1 • 💬 0 • 4d ago • [GitHub](https://github.com/03012009BTC/miners-bitcoin-lottery)

---

**[Notice of ICANN .bitcoin TLD community application](https://news.ycombinator.com/item?id=49188412)**

Notice of ICANN .bitcoin TLD community application

⬆️ 1 • 💬 0 • 6d ago • [X (formerly Twitter)](https://twitter.com/wiz/status/2085029140453830725)

---

**[Show HN: I built an economy designed to crash](https://news.ycombinator.com/item?id=49180864)**

⬆️ 3 • 💬 0 • 6d ago • [glaxom.netlify.app](https://glaxom.netlify.app)

---

**[Making Postgres 300x faster for analytics: batching, operator fusion, and SIMD](https://news.ycombinator.com/item?id=49208535)**

Last week we released version 0.2 of pgrust. This release was all about performance. It’s 10x faster than the previous version of pgrust. On OLTP benchmarks, pgrust is 30% faster than Postgres, and on Clickbench, Clickhouse’s benchmark for analytical databases, pgrust is 300x faster than Postgres. It’s even ahead of Clickhouse! The query engine is […]

⬆️ 336 • 💬 176 • 4d ago • [malisper.me](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/)

---

---

## YouTube Videos: "bitcoin"

**[A HURRICANE is about To Hit Crypto.. (HUGE NEWS)](https://www.youtube.com/watch?v=sGhG1DEXW0Y)**

MASSIVE: A HURRICANE is about To Hit Crypto! 🌪️ ⭐ Follow Altcoin Daily on X: https://twitter.com/AltcoinDaily 50% deposit ...

📺 Altcoin Daily

👁️ 38K • 👍 2K • 💬 134 • ⏱️ 9:23 • 1d ago

---

**[Bitcoin: It&#39;s Almost Crunch Time](https://www.youtube.com/watch?v=zsnxQO7tC9M)**

Let's talk about where Bitcoin is in the cycle, and why it's almost crunch time. Come to the 1st ITC Conference: ...

📺 Benjamin Cowen

👁️ 120K • 👍 7K • 💬 355 • ⏱️ 8:04 • 1d ago

---

**[This Ends Every Bitcoin Bear Market](https://www.youtube.com/watch?v=1lHFaniXiw0)**

GET ON KRAKEN TODAY kraken.com/lark?inviteCode=kjtfbzb3 The Korean market dropped 45%. AI stocks got cut in half.

📺 Lark Davis

👁️ 11K • 👍 584 • 💬 65 • ⏱️ 7:38 • 11h ago

---

**[New Lows Coming For Crypto ??](https://www.youtube.com/watch?v=UcAX4VpRTfg)**

New Lows Coming For Crypto ?? Stocks repeating DAX rally Metals at inflection point TA & Live Trades Get the CF Cycle trading ...

📺 Camel Finance

👁️ 8K • 👍 563 • 💬 91 • ⏱️ 12:02 • 14h ago

---

**[🚨 ¿ESTOY EQUIVOCADO CON BITCOIN? y este se desplomara a 60K como todo mundo dice?](https://www.youtube.com/watch?v=pLaPCpw8DuQ)**

Estoy equivocado con Bitcoin? El precio se está debilitando y cada vez más traders hablan de una posible caída hacia los 60K.

📺 BITLOBO TRADING

👁️ 3K • 👍 732 • 💬 6 • ⏱️ 47:41 • 5h ago

---

**[Bitcoin Captured? The Battle That Changes Everything!](https://www.youtube.com/watch?v=8g_rqh1dF3U)**

Bitcoin's BIP-110 soft fork briefly split the chain—but the failed Bitcoin fork may have proven the opposite of corporate capture: ...

📺 Simply Bitcoin

👁️ 20K • 👍 2K • 💬 254 • ⏱️ 20:00 • 1d ago

---

**[This Week Could Decide Bitcoin&#39;s Direction](https://www.youtube.com/watch?v=8rb0sPhh6K0)**

Bitcoin is entering a tight compression phase, and the next breakout could be closer than most traders expect. Sheldon breaks ...

📺 Crypto Banter

👁️ 6K • 👍 354 • 💬 18 • ⏱️ 12:44 • 13h ago

---

**[THIS IS EXACTLY WHAT BITCOIN WILL DO NEXT.](https://www.youtube.com/watch?v=9B76KNPZm8M)**

TRADE LIKE I DO (LIVE STRATEGY) Bybit (my main exchange) https://partner.bybit.com/b/Didi ⚡ APPLY TO WORK WITH ME ...

📺 THE BITCOIN FAMILY Didi Taihuttu

👁️ 10K • 👍 789 • 💬 44 • ⏱️ 12:27 • 1d ago

---

**[Give Me 14 Minutes and You&#39;ll Finally Know How Much Bitcoin You Need To Retire](https://www.youtube.com/watch?v=rbxsWA3ysh8)**

How much Bitcoin do you actually need to retire? Not one coin. Not 0.01. The real number for your life, built from four inputs you ...

📺 Trey Sellers

👁️ 9K • 👍 293 • 💬 152 • ⏱️ 14:23 • 1d ago

---

**[Cycle Signal Triggers as Bitcoin Price Chart ABC&#39;s with XRP On-Chain Hitting 42.4 Billion at $1.00](https://www.youtube.com/watch?v=U5postwKrF8)**

Blockchain Backer Newsletter - https://blockchainbacker.substack.com Blockchain Backer's Technical Analysis Toolkit for Crypto ...

📺 Blockchain Backer

👁️ 26K • 👍 3K • 💬 3 • ⏱️ 19:18 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
