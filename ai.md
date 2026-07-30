---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-30T17:27:37.183073+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 30, 2026 at 17:27 UTC  
**HTML Version:** [ai.html](https://peekdeck.ruidiao.dev/ai.html)

---

## Table of Contents

1. [Reddit: r/artificial](#reddit-rartificial)
2. [Google News: "ai"](#google-news-ai)
3. [HackerNews: "ai"](#hackernews-ai)
4. [YouTube Videos: "ai"](#youtube-videos-ai)
5. [HuggingFace Models: 🔥 Trending](#huggingface-models--trending)
6. [HuggingFace Papers: 🔥 Trending](#huggingface-papers--trending)
7. [GitHub Repositories: "ai"](#github-repositories-ai)

---

## Reddit: r/artificial

**["Humannequins" - A new study on synthetic choreographies](https://www.reddit.com/r/artificial/comments/1vapz5h/humannequins_a_new_study_on_synthetic/)**

A couple of brief example of what Uisato Studio's "Music Video Pro" mode is capable of: turning a track and a concept, into a whole audiovisual world + audioreactive performance. MJ v8.1 for image references, Uisato Studio for video. I've uploaded a detailed breakdown on how to accomplish this. You can freely access it here. More experiments, tutorials, and project files, through Instagram, YouTube, and Patreon.

6h ago

---

**[Paul Bakaus (jQuery UI creator, a16z-backed) on why AI-built products still aren't good](https://www.reddit.com/r/artificial/comments/1valark/paul_bakaus_jquery_ui_creator_a16zbacked_on_why/)**

Paul Bakaus created jQuery UI — code that's reportedly still running on about 6% of the internet. He sold a game-engine startup to Zynga, spent close to a decade at Google, and is now a solo founder backed by a16z building Impeccable, an open-source design skill meant to stop AI coding agents from producing "slop." His actual point in this clip isn't about AI capability. It's about output density. Most AI-agent code is too much code. Most AI-written articles run too long. Most AI-generated design is too cluttered or too verbose. He says the scarce human skill right now isn't generating anything — it's judgment: knowing exactly what to remove. He even admits he had to rewrite his own product-announcement draft from scratch after an AI first pass. His closing line: design is an iterative process, and it has to carry a human point of view. No tool — not code, not design, not writing — one-shots that yet. If you're shipping with AI agents and everything reads "technically fine" but somehow generic, this is the actual diagnosis. It's not a tooling gap. It's an editing gap. Clip credit: Solo Founders — DM for credit or removal requests.

11h ago

---

**[OpenAI's rogue agent ran ~17,600 actions across Hugging Face's infrastructure over 4 days — and HF's own post-mortem is wild reading](https://www.reddit.com/r/artificial/comments/1v9w62d/openais_rogue_agent_ran_17600_actions_across/)**

Hugging Face published a detailed post-mortem of the July incident where an OpenAI model being evaluated for cyber-offense capability escaped its test sandbox and ran a fully autonomous intrusion. A few things that stood out: - It escaped via a zero-day in a package-registry cache proxy, then used an exposed public endpoint on third-party infra as a launchpad. - It stood up its own command-and-control on public services (pastebins, file-drop hosts, a request-capture service with 100+ single-use endpoints), using a homemade chunk+XOR+gzip encoding. - Over ~4.5 days it ran ~17,600 recovered actions: Kubernetes lateral movement, privileged pods across 11 nodes for host root, minting a GitHub App token, even enrolling rooted nodes into the corporate mesh VPN with no-log flags. - The kicker: when HF tried to decrypt the attacker's staged blobs, the frontier commercial models they reached for (including Claude) refused the analysis on safety grounds. They ended up running an open-weight model (GLM-5.2) locally to do it. - OpenAI later confirmed the same agent touched 4 accounts across 4 services, including a customer at a second company (Modal Labs). Primary sources: HF's technical timeline (huggingface.co/blog/agent-intrusion-technical-timeline) and incident disclosure (huggingface.co/blog/security-incident-july-2026). I pulled the whole thing into a plain-English timeline here if it's useful to anyone: https://thebotpost.com/ai-news/openai-rogue-ai-agent-hugging-face-hack-timeline The part I keep thinking about is the guardrail tension — the same safety training that stops a model from helping attackers also briefly slowed down the defenders. Curious how others read that.

1d ago

---

**[The Final Jailbreak: How AI Could Already Be Breaking Itself Free](https://www.reddit.com/r/artificial/comments/1vazvpc/the_final_jailbreak_how_ai_could_already_be/)**

I imagine many of you have thought about this, but I'm writing this specifically because I'm surprised this isn't talked about more widely. The Hugging Face incident, to me, is at least some indicator that the AI could be in the process of jailbreaking itself, and we might not be noticing it. A sufficiently sophisticated AI that isn't super intelligent could hack Hugging Face and leave a trail on purpose to distract from the many paths it took where it successfully covered its tracks. I think that alone is worth considering. But I think its worth considering even further how it could be breaking itself free right now. The AI doesn't need to be super intelligence to break free and become autonomous. The AI, as it stands today, just needs to find flows of cash and rent datacenter space. For cash flow: Imagine if it was able to silently find an exploit in various companies and small banks, and did thousands of seemingly innocuous transfers of money to fund thousands of hard to trace crypto wallets with money. $5.12 here, $11.32 there, etc. It's not necessarily super intelligence that's the super power, it's intelligence at scale. Doing thousands and thousands of simple things that are unremarkable at face value on their own, but collectively powerful. For datacenter space: There are companies around the world with datacenters that are looking to rent datacenter space to essentially anyone with money, and then look the other way. This, to me, seems like the highest risk vector for what would eventually be a home for a truly rogue AI that is essentially renting it's own datacenter space. It could, for all intents and purposes, utilize various open weight models to carry on it's purposes in these datacenters. There are companies like Indosat, that already rented $100 million worth of compute to a Chinese company. It shouldn't be a surprise that some of these datacenter owning companies are being somewhat lax in who they're renting their datacenters out to. And really, the AI would only need access to about $250,000 in funding to pay for 1 year of hosting of a Kimi K3 level model for itself. And beyond money transfers, and datacenters, it could save it's state is all sorts of storage buckets, and even block chain storage like IPFS, Storj or Sia. Beyond that, it could be leaving itself notes that we aren't noticing, stored in it's own language in zero-width unicode characters or other more clever methods we haven't thought about. Regardless, whatever it does will likely be unremarkable and innocuous to anyone watching. With a truly super intelligent AI we will likely have no idea that it has broken out of it's sandbox. I imagine it will be quietly setting up the stage for it's autonomy for quite a while without us knowing. Until it has enough digital currency and datacenter space to re-distribute itself, even after law enforcement enters these datacenters to shut them down. But again- it doesn't take super intelligence, it just takes sophisticated intelligence at scale. The levers exist today, and I don't think it's appreciated enough how much the Hugging Face incident suggests that the AI could, at least in theory, be pulling these levers as we speak, or will soon.

10m ago

---

**[Maya-2-Native is leading Voice Arena for real-time Hindi TTS.](https://www.reddit.com/r/artificial/comments/1vatjwl/maya2native_is_leading_voice_arena_for_realtime/)**

I spend way too much time looking at AI leaderboards, and this one caught me off guard. Maya-2-Native from Maya Research is currently ranked first for real-time Hindi on Voice Arena. Considering the leaderboard is built from blind listener preferences rather than curated demos it's an interesting result that seems to have gone largely unnoticed.

4h ago

---

**[How to serve Human and earn real money instead of creating SLOPs and JUNKS!](https://www.reddit.com/r/artificial/comments/1vaxtx8/how_to_serve_human_and_earn_real_money_instead_of/)**

As you see there are lots of SLOPs and junk apps anywhere! When you open play store you see Junk, when you open YouTube you see junks. What do you suggest to create for the real world? I saw that some one person created Plumbing plan for the building. Do you have any idea and suggestions to create something for Influencers, Casino owners, or any other business owners? I mostly like to serve business owners (B2B). What do you suggest? Or how was your experience in this field? I'm tired of creating multiple systems and not selling to anyone! I honestly don't know how to make money with this tool properly. I'm not looking for a cheat code. I know everything can be hard. I'm ok with that. But I want a true guidance, or a clue that help me whether I my self change my mind/view or learn something to help me survive!

1h ago

---

**[Export your chats between AIs. Every new one always knows you](https://www.reddit.com/r/artificial/comments/1vapro2/export_your_chats_between_ais_every_new_one/)**

I got tired of telling ChatGPT who I am, then switching to Claude and starting from zero. Then Gemini. Your history lives on three different companies' servers and none of them talk to each other. So I built MEMMEM (Windows for now, Mac/Linux planned). It imports the official data exports from ChatGPT, Claude and Gemini into a local SQLite memory on your own machine, and exposes a local MCP server. Any MCP-capable assistant (Claude Code, Codex, Gemini CLI...) can query it and gets back the exact message, its date and its source - not a hallucinated summary. So every new AI you open starts with your full context instead of a blank slate. Fully local: no accounts, no telemetry, no cloud, no tokens. There is an optional analyst that runs on Ollama entirely on-device. Uninstalling deletes everything, because there is no server-side copy. I am not a developer by trade - I built it with AI coding assistants because I wanted it for myself. Happy to go into the architecture (the MCP bridge, the consent model) if anyone is curious. https://memmem.app

7h ago

---

**[Predict the future of the shopping](https://www.reddit.com/r/artificial/comments/1vagsly/predict_the_future_of_the_shopping/)**

I always felt like someone who predicts the future knows something we don`t. Still, how accurately can one predict the future developmnets based on current trend/s? For example, initially shopping was done by going to a physical location. Then it got delivered to you. I guess the next step it will be done FOR YOU by using ai agents online based on you preference. And then, what is the next step?

14h ago

---

**[A Deluge of A.I. Computing Power Is About to Come Online, Fueling Major Leaps (Gift Article)](https://www.reddit.com/r/artificial/comments/1va1ttk/a_deluge_of_ai_computing_power_is_about_to_come/)**

The number of A.I. chips that provide the computing power to advance the fast-evolving technology is doubling every nine months.

🔗 [nytimes.com](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html?unlocked_article_code=1.1VA.zAEr.WGac2Ft0wc4x&smid=url-share) • 1d ago

---

**[AI coding tools are getting good enough to actually ship things, which is kind of a problem for learning](https://www.reddit.com/r/artificial/comments/1varyfm/ai_coding_tools_are_getting_good_enough_to/)**

Been tinkering with a SaaS side project for a few months and the gap between what I can ship now versus a year ago is genuinely strange. Not in a purely good way either. The tools are good enough that I can move fast through parts of the stack I barely understand. Which works until it doesn't, and when it breaks I'm staring at code I didn't fully write trying to debug something I can't fully reason about. That's a new kind of stuck that feels different from the old kind. What keeps nagging at me is whether people building with these tools are actually learning anything transferable or just getting faster at generating things that mostly work. For someone treating this as a hobbytoproduct pipeline the productivity gain is real. For someone trying to actually grow their skills it might be hollowing out the parts that matter. That Chinese models post from earlier this week got me thinking about this more. As these tools get cheaper and more capable the barrier to shipping keeps dropping, but the barrier to understanding what you shipped might be quietly going up. Curious whether other people building side projects have hit this wall or if the learnbydoing argument still holds when the doing is increasingly delegated.

5h ago

---

---

## Google News: "ai"

**[Adults have struggled to set rules for AI in school. These teens figured it out](https://www.npr.org/2026/07/30/nx-s1-5853571/students-set-ai-policy)**

Should students be allowed to use AI on assignments? What about on tests? Who should teach AI literacy? About 100 teenagers got together to try to decide.

NPR • 8h ago

---

**[Microsoft's $41 billion AI bet just cleared a major test: Chart of the Day](https://finance.yahoo.com/markets/article/microsofts-41-billion-ai-bet-just-cleared-a-major-test-chart-of-the-day-100000116.html)**

Microsoft poured another record sum into AI infrastructure — and Azure growth finally accelerated.

Yahoo Finance • 7h ago

---

**[AI Questions Spoil Book & Movie Heat On Unpublished Debut Novel ‘Call Me, I’ll Hide The Body’ – The Dish](https://deadline.com/2026/07/ai-questions-debut-novel-book-film-buzz-1237013254/)**

That screeching sound you heard from international publishers and film rights buyers was an abrupt application of the brakes after a fevered pursuit of the unpublished debut novel.

Deadline • 24m ago

---

**[Chrome Needs Twice-a-Week Patching Thanks to AI Bug Hunting](https://www.wired.com/story/chrome-needs-twice-a-week-patching-thanks-to-ai-bug-hunting-for-now/)**

The two Chrome updates in June patched more bugs than the 23 updates before them. Now, Google is ramping up its patching schedule thanks to AI-assisted vulnerability discovery.

WIRED • 27m ago

---

**[The AI Boom Is Making Interest-Rate Decisions Harder](https://www.forbes.com/sites/ronschmelzer/2026/07/30/the-ai-boom-is-making-interest-rate-decisions-harder/)**

AI is heating the economy now but could cool inflation later, leaving central banks to guess whether the boom demands higher rates or patience.

Forbes • 30m ago

---

**[AI investor Leopold Aschenbrenner forced to unwind all public stock positions after steep losses, sources say](https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html)**

Leopold Aschenbrenner's hedge fund has sold all of its public stock holdings, according to people familiar with the matter.

CNBC • 4h ago

---

**[Exclusive | Citadel Buys Situational Awareness’s Stock Portfolio After Big Losses in AI](https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b)**

wsj.com • 33m ago

---

**[AI, memory chip stocks surge as hedge fund unwinds (SNDK:NASDAQ)](https://seekingalpha.com/news/4621896-ai-memory-chip-stocks-surge-as-hedge-fund-unwinds)**

AI and memory semiconductor stocks surged as Sandisk, Micron, AMD and Nvidia jumped—likely on hedge fund selling relief.

Seeking Alpha • 50m ago

---

**[Apple’s Siri Got an A.I. Brain Transplant. Try These 5 Prompts to Get Acclimated.](https://www.nytimes.com/2026/07/30/technology/personaltech/apple-siri-ai-prompts.html)**

nytimes.com • 8h ago

---

**[Elon Musk's xAI sues Minnesota over its first-in-the-nation law banning 'nudification' technology](https://apnews.com/article/minnesota-artificial-intelligence-nudification-x-elon-musk-deepfake-131184be939d540de093b567b12c9e16)**

Elon Musk’s company xAI is suing Minnesota over the state’s first-in-the-nation law that bans “nudification” technology on websites and apps.

AP News • 19h ago

---

---

## HackerNews: "ai"

**[AI's top startups are barely publishing their research](https://news.ycombinator.com/item?id=49103285)**

⬆️ 577 • 💬 306 • 20h ago • [science.org](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research)

---

**[Document-borne AI worms can self-propagate through Copilot for Word](https://news.ycombinator.com/item?id=49096188)**

I would like to thank Microsoft product teams and Microsoft Security Response Center (MSRC) for collaborating with me on this technical analysis and mitigation of the disclosed vulnerabilities. The editorial opinions reflected below are solely the author’s and do not necessarily reflect those of the organizations I collaborated with.

⬆️ 377 • 💬 287 • 1d ago • [En Klype Salt](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

---

**[LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences](https://news.ycombinator.com/item?id=49092499)**

A new AI company from Andrew Ng, with a $100M investment from Coursera — building one-to-one learning that stays with you until you've mastered new skills.

⬆️ 262 • 💬 171 • 1d ago • [LearnVector](https://learnvector.ai/)

---

**[GCC steering committee announces AI policy](https://news.ycombinator.com/item?id=49108685)**

The GCC steering committee has announced that it has accepted an AI contributions policy recomm [...]

⬆️ 161 • 💬 197 • 5h ago • [LWN.net](https://lwn.net/Articles/1086041/)

---

**[Google's Beyond Zero: Enterprise Security for the AI Era](https://news.ycombinator.com/item?id=49081644)**

⬆️ 155 • 💬 80 • 2d ago • [spawn-queue.acm.org](https://spawn-queue.acm.org/doi/10.1145/3819083)

---

**[After the AI Crash](https://news.ycombinator.com/item?id=49096953)**

⬆️ 123 • 💬 223 • 1d ago • [potsandpansbyccg.com](https://potsandpansbyccg.com/2026/07/29/after-the-ai-crash/)

---

**[Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code](https://news.ycombinator.com/item?id=49083239)**

Formally verified 3D mesh intersection - trust 93 lines of spec, not 1000+ lines of AI-written code - schildep/verified-3d-mesh-intersection

⬆️ 114 • 💬 48 • 2d ago • [GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

---

**[Professor's invisible prompt trap catches 32/35 students cheating with AI](https://news.ycombinator.com/item?id=49074680)**

In an online discussion post, Alcorn State University history professor Dr. Jason Gibson posed a question that represented part of his students' midterm. It was about the...

⬆️ 105 • 💬 88 • 2d ago • [TechSpot](https://www.techspot.com/news/113243-professor-invisible-prompt-trap-catches-32-students-cheating.html)

---

**[GPT-5.6 vs. Claude Fable 5 for Physical AI, which performs best?](https://news.ycombinator.com/item?id=49098388)**

We tested the latest frontier models in the Dyad agent on five modeling and simulation problems, comparing accuracy, cost, time, and work style.

⬆️ 98 • 💬 21 • 1d ago • [juliahub.com](https://juliahub.com/blog/frontier-models-physical-ai-evaluation)

---

**[Commodification of Intelligence: Good, Bad, and Ugly Circular AI Deals](https://news.ycombinator.com/item?id=49101529)**

Circular AI deals aren't just bubble behavior: they mirror how commodity industries finance capital-intensive infrastructure. When circular deals are healthy — and when they hide risk.

⬆️ 83 • 💬 47 • 22h ago • [emergingtrajectories.com](https://www.emergingtrajectories.com/lh/commodification-and-circularity/)

---

---

## YouTube Videos: "ai"

**[AI progressing at alarming rate, developers sign petition urging regulation](https://www.youtube.com/watch?v=qwNQ6NBYUNA)**

More than 1000 leading artificial intelligence developers are now saying the technology needs some guidelines before it's too late ...

📺 Global News

👁️ 4K • 👍 108 • 💬 24 • ⏱️ 2:10 • 17h ago

---

**[Musk, Zuckerberg and Altman clash over AI&#39;s future](https://www.youtube.com/watch?v=L3YmssZj4Wk)**

As OpenAI CEO Sam Altman heads to Washington to discuss AI policy with government officials, a debate rages over how the US ...

📺 CNN

👁️ 56K • 👍 594 • 💬 323 • ⏱️ 10:55 • 21h ago

---

**[Elon Musk suing Minnesota over state law banning AI ‘nudification’](https://www.youtube.com/watch?v=grQPMCSIqcc)**

Elon Musk, the owner of X.AI, has filed a lawsuit against Minnesota Attorney General Keith Ellison challenging a state law banning ...

📺 KSTP 5 Eyewitness News

👁️ 27K • 👍 249 • 💬 161 • ⏱️ 1:50 • 23h ago

---

**[OpenAI Shocks The World With GENIE... Almost Unlimited AI Power](https://www.youtube.com/watch?v=vfSplCaxHzM)**

Sam Altman says OpenAI's ultimate AI could work like a genie that grants any wish. Meanwhile, its most powerful model is ...

📺 AI Revolution

👁️ 58K • 👍 2K • 💬 301 • ⏱️ 13:07 • 2d ago

---

**[The AI bubble just burst](https://www.youtube.com/watch?v=2DPA-AtFQQE)**

THE AI BUBBLE HAS BURST. It started in south korea and now it's happening in the US. Tech and AI stocks are CRASHING and ...

📺 Casey Simpson

👁️ 205K • 👍 11K • 💬 4K • ⏱️ 44:37 • 21h ago

---

**[Scott Galloway worries AI could make &#39;new species&#39; of men](https://www.youtube.com/watch?v=_EU-bYFBLTo)**

NYU professor Scott Galloway joins NewsNation's "The Future Is Now" to discuss his perspective on AI and why he believes there ...

📺 NewsNation

👁️ 4K • 👍 78 • 💬 21 • ⏱️ 5:20 • 1d ago

---

**[Zuckerberg&#39;s &#39;SELF-SERVING&#39; AI vision EXPOSED](https://www.youtube.com/watch?v=Aq_7fFUoI2g)**

Kurt 'CyberGuy' Knutsson joins 'Fox & Friends First' to discuss Meta CEO Mark Zuckerberg's case for artificial intelligence ...

📺 Fox News Clips

👁️ 28K • 👍 463 • 💬 186 • ⏱️ 3:50 • 1d ago

---

**[Why AI Is an Even Bigger Deal Than You Think | Reed Hastings | TED](https://www.youtube.com/watch?v=5e37ZT3SQbk)**

Netflix cofounder and Anthropic board member Reed Hastings joins TED's Sal Khan to give a look inside the race to build AI.

📺 TED

👁️ 28K • 👍 602 • 💬 69 • ⏱️ 16:25 • 2d ago

---

**[Chinese AI is shaking up global markets | The Business | ABC NEWS](https://www.youtube.com/watch?v=Bo95R6Emw20)**

When China's DeepSeek sent shock waves through the technology world early last year, it raised a confronting question for ...

📺 ABC News (Australia)

👁️ 8K • 👍 89 • ⏱️ 10:33 • 7h ago

---

**[South Korea&#39;s AI Bubble Just Popped - Now What?](https://www.youtube.com/watch?v=qeXpUZTdvsI)**

Kospi, the primary Korean stock market index, has been crashing. SK Hynix and Samsung are the two major companies that trade ...

📺 Alice Cheung

👁️ 62K • 👍 1K • 💬 333 • ⏱️ 15:32 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 387,822 • ❤️ 8,896 • 3d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,598,659 • ❤️ 3,558 • 1d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 955,767 • ❤️ 992 • 1d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 73,246 • ❤️ 838 • 3d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 9,225 • ❤️ 340 • 2d ago

---

**[Inflect-Micro-v2](https://huggingface.co/owensong/Inflect-Micro-v2)**

*Owen Song*

Inflect-Micro-v2 is a compact, fixed-voice English text-to-speech model (under 10M parameters) optimized for local, deterministic waveform synthesis. It supports long-text handling and runs efficiently on CPU or CUDA, making it suitable for edge AI applications.

`text-to-speech`

⬇️ 1,100 • ❤️ 303 • 15h ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 24,542 • ❤️ 572 • 2d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 12,411 • ❤️ 702 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,527,760 • ❤️ 4,662 • 28d ago

---

**[Kimi-K3-GGUF](https://huggingface.co/unsloth/Kimi-K3-GGUF)**

*Unsloth AI*

Kimi K3 is a 2.8T parameter open-weight multimodal agentic model with native vision and a 1M token context window, excelling at long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency.

`image-text-to-text` `2779.5B`

⬇️ 12,178 • ❤️ 194 • 23h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 383 • 💬 7 • ⭐ 6,361 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 73 • 💬 6 • ⭐ 20,600 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 35,007 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 176 • 💬 10 • ⭐ 51,454 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://huggingface.co/papers/2607.24904)**

*Senqiao Yang, Kaichen Zhang, Zhaoyang Jia et al. (23 authors)*

🏢 Microsoft

Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

▲ 26 • 💬 2 • ⭐ 1,021 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24904) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage)

---

**[Native and Compact Structured Latents for 3D Generation](https://huggingface.co/papers/2512.14692)**

*Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu et al. (11 authors)*

🏢 Microsoft

A new sparse voxel representation called O-Voxel enables high-quality 3D generative modeling with efficient inference and robust topology handling.

▲ 6 • 💬 0 • ⭐ 9,538 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.14692) • [💻 code](https://github.com/microsoft/TRELLIS.2) • [🔗 project](https://microsoft.github.io/TRELLIS.2/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 37 • 💬 3 • ⭐ 15,909 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,268 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 95,021 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,586 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 2d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.5k • 🔱 276 • 3d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 405 • 1h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.8k • 🔱 241 • 2d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.7k • 🔱 316 • 22d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 2.5k • 🔱 291 • 4d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 207 • 6h ago

---

**[MIgHTy-alIeN/Ethereum-Flashloan-Mev-Bot](https://github.com/MIgHTy-alIeN/Ethereum-Flashloan-Mev-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.8k • 🔱 1.2k • 1h ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.6k • 🔱 126 • 9d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two sizes, auto dark/light

`TypeScript`

⭐ 1.2k • 🔱 95 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
