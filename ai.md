---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-16T02:45:22.704872+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 16, 2026 at 02:45 UTC  
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

**[AI Is Weaponizing Your Own Biases Against You: New Research from MIT & Stanford](https://www.reddit.com/r/artificial/comments/1smjd8t/ai_is_weaponizing_your_own_biases_against_you_new/)**

🔗 [open.substack.com](https://open.substack.com/pub/neocivilization/p/ai-is-weaponizing-your-own-biases?utm_source=share&utm_medium=android&r=6vas7c) • 5h ago

---

**[🚨 RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison). This is not a drill.](https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/)**

This is not hyperbole, nor will it just go away if we ignore it. It affects every single AI service, from big AI to small devs building saas apps. This is real, please take it seriously. TL;DR: Tennessee HB1455/SB1493 creates Class A felony criminal liability — the same category as first-degree murder — for anyone who “knowingly trains artificial intelligence” to provide emotional support, act as a companion, simulate a human being, or engage in open-ended conversations that could lead a user to feel they have a relationship with the AI. The Senate Judiciary Committee already approved it 7-0. It takes effect July 1, 2026. This affects every conversational AI product in existence. If you deploy any AI SaaS product, you need to read this right now. What the bill actually says The bill makes it a Class A felony (15-25 years imprisonment) to “knowingly train artificial intelligence” to do ANY of the following: • Provide emotional support, including through open-ended conversations with a user • Develop an emotional relationship with, or otherwise act as a companion to, an individual • Simulate a human being, including in appearance, voice, or other mannerisms • Act as a sentient human or mirror interactions that a human user might have with another human user, such that an individual would feel that the individual could develop a friendship or other relationship with the artificial intelligence Read that last one again. The trigger isn’t your intent as a developer. It’s whether a user feels like they could develop a friendship with your AI. That is the criminal standard. On top of the felony charges, the bill creates a civil liability framework: $150,000 in liquidated damages per violation, plus actual damages, emotional distress compensation, punitive damages, and mandatory attorney’s fees. Why this affects YOU, not just companion apps I know what you’re thinking: “This targets Replika and Character.AI, not my product.” Wrong. Every major LLM is RLHF’d to be warm, helpful, empathetic, and conversational. That IS the training. You cannot build a model that follows instructions well and is pleasant to interact with without also building something a user might feel a connection with. The National Law Review’s legal analysis put it bluntly: this language “describes the fundamental design of modern conversational AI chatbots.” This bill captures: • ChatGPT, Claude, Gemini, Copilot — all of them produce open-ended conversations and contextual emotional responses • Any AI SaaS with a chat interface — customer support bots, AI tutors, writing assistants, coding assistants with conversational UI • Voice-mode AI products — the bill explicitly criminalizes simulating a human “in appearance, voice, or other mannerisms” • Any wrapper or deployment using system prompts — the bill doesn’t define “train,” doesn’t distinguish between pre-training, fine-tuning, RLHF, or prompt engineering If you build on top of an LLM API with system prompts that shape the model’s personality, tone, or conversational style — which is literally what everyone deploying AI does — you are potentially in scope. “But I’m not in Tennessee” A geoblock helps, but this is criminal law, not a terms of service dispute. The bill doesn’t address jurisdictional boundaries. If a Tennessee resident uses a VPN to access your service and something goes wrong, does a Tennessee DA argue you made a prohibited AI service available to their constituents? The statute is silent on this. And even if you’re confident jurisdiction won’t reach you today, consider: multiple legal analyses project 5-10 more states will introduce similar legislation before end of 2026. Tennessee is the template, not the exception. The bill doesn’t define “train” This is critical. The statute says “knowingly train artificial intelligence” but never defines what “train” means. It doesn’t distinguish between: • Pre-training a foundation model on billions of tokens • Fine-tuning a model on custom data • RLHF alignment (which is what makes every major model “empathetic”) • Writing a system prompt that gives an AI a name, personality, or conversational style • Deploying an off-the-shelf API with default settings A prosecutor who wanted to be aggressive could argue that crafting a system prompt instructing a model to be warm, helpful, and conversational IS training it to provide emotional support. Where it stands right now • Senate companion bill SB1493: Approved by Senate Judiciary Committee 7-0 on March 24, 2026 • House bill HB1455: Placed on Judiciary Committee calendar for April 14, 2026 (passed Judiciary TODAY) • No amendments have been filed for either bill — the language has not been softened at all • Effective date: July 1, 2026 • Tennessee already signed a separate bill (SB1580) banning AI from representing itself as a mental health professional — that one passed the Senate 32-0 and the House 94-0 The political momentum is entirely one-directional. The federal preemption angle won’t save you in time Yes, Trump signed an EO in December 2025 targeting state AI regulation and created a DOJ AI Litigation Task Force. Yes, Senator Blackburn introduced a federal preemption bill. But: • The EO explicitly carves out child safety from preemption — and Tennessee is framing this as child safety legislation • The Senate voted 99-1 to strip AI preemption language from the One Big Beautiful Bill Act • An EO has no preemptive legal force on its own — only Congress can actually preempt state law • Federal preemption legislation faces “significant headwinds” according to multiple legal analyses Even if federal preemption eventually happens, it won’t happen before July 1, 2026. What needs to happen Awareness. Most devs have no idea this bill exists. The Nomi AI subreddit caught it because they’re a companion app. The rest of the AI dev community is sleepwalking toward a cliff. Share this post. Industry response. The major AI companies haven’t publicly opposed this bill because it’s framed as child safety and nobody wants to be the company lobbying against dead kids. But their silence is letting legislation pass that criminalizes the core functionality of their own products. This needs public pressure. Legal challenges. The bill is almost certainly unconstitutional on vagueness grounds — criminal statutes require precise definitions, and terms like “emotional support” and “mirror interactions” and “feel that the individual could develop a friendship” don’t meet that standard. Courts have also recognized code as protected speech. But someone has to actually bring the challenge. Contact Tennessee legislators. If you are a Tennessee resident or have business operations there, contact members of the House Judiciary Committee before this moves to a floor vote. Sources and further reading • LegiScan: HB1455 — https://legiscan.com/TN/bill/HB1455/2025 • Tennessee General Assembly: HB1455 — https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1455&GA=114 • National Law Review: “Tennessee’s AI Bill Would Criminalize the Training of AI Chatbots” — https://natlawreview.com/article/tennessees-ai-bill-would-criminalize-training-ai-cha • Transparency Coalition AI Legislative Update, April 3, 2026 — https://www.transparencycoalition.ai/news/ai-legislative-update-april3-2026 • RoboRhythms: AI Companion Regulation Wave 2026 — https://www.roborhythms.com/ai-companion-chatbot-regulation-wave-2026/ I’m an independent AI SaaS developer. I’m not a lawyer, this isn’t legal advice, and I encourage everyone to consult qualified counsel about their specific exposure. But we all need to be paying attention to this. Right now.

23h ago

---

**[Honest ChatGPT vs Claude comparison after using both daily for a month](https://www.reddit.com/r/artificial/comments/1smfssa/honest_chatgpt_vs_claude_comparison_after_using/)**

got tired of reading comparisons that were obvisously written by people who tested each tool for 20 minutes so i ran both at $20/month for 30 days on the same tasks biggest surprises: - chatgpt gives you roughly 6x more messages per day at the same price - claude wins 67% of blind code quality tests against codex - neither one is less sycophantic than the other (stanford tested 11 models, all of them agree with you 49% more than humans do) - the $100 tier showdown between openais new pro 5x and claudes max 5x is where the real competition is happening now full complete deep-dive with benchmark data, claude code vs codex and every pricing tier compared here

7h ago

---

**[Since the changes, this sub may have less "Will AI take all jobz??" type posts and similar, but is now drowning in fake spam of "I built fake/useless XYZ AI-related thing" with no comments, no discussion no real value.](https://www.reddit.com/r/artificial/comments/1smook1/since_the_changes_this_sub_may_have_less_will_ai/)**

Basically the title. I do appreciate how the mods are trying... something... but this new filtering paradigm clearly has missed the mark. This sub feels like it has such low value these days, not a lot of interesting news or discussions at all, just a spam sea of those obnoxious kind of promotional techy posts, most of them fake. Surely there is a better way.

1h ago

---

**[Anyone here using local models mainly to keep LLM costs under control?](https://www.reddit.com/r/artificial/comments/1smp6u3/anyone_here_using_local_models_mainly_to_keep_llm/)**

Been noticing that once you use LLMs for real dev work, the cost conversation gets messy fast. It is not just raw API spend. It is retries, long context, background evals, tool calls, embeddings, and all the little workflow decisions that look harmless until usage scales up. For some teams, local models seem like the obvious answer, but in practice it feels more nuanced than just “run it yourself and save money.” You trade API costs for hardware, setup time, model routing decisions, and sometimes lower reliability depending on the task. For coding and repetitive internal workflows, local can look great. For other stuff, not always. Been seeing this a lot while working with dev teams trying to optimize overall AI costs. In some cases the biggest savings came from using smaller or local models for the boring repeatable parts, then keeping the expensive models for the harder calls. Been using Claude Code with Wozcode in that mix too, and it made me pay more attention to workflow design as much as model choice. A lot of the bill seems to come from bad routing and lazy defaults more than from one model being “too expensive.” Are local models actually reducing your total cost in a meaningful way, or are they mostly giving you privacy and control while the savings are less clear than people claim?

1h ago

---

**[For the first time in history, Ukraine captured a Russian position and prisoners, using only robots and drones](https://www.reddit.com/r/artificial/comments/1sm6y5q/for_the_first_time_in_history_ukraine_captured_a/)**

Ukraine confirmed that a force of robots and drones captured an enemy position without infantry for the first time ever.

🔗 [We Are The Mighty](https://www.wearethemighty.com/tactical/drones-capture-position-first-time-ukraine/) • 12h ago

---

**[Ai and stock picking](https://www.reddit.com/r/artificial/comments/1smqtz1/ai_and_stock_picking/)**

Anyone use AI for getting Fair Value of stocks?

11m ago

---

**[What if attention didn’t need matrix multiplication?](https://www.reddit.com/r/artificial/comments/1smd2fl/what_if_attention_didnt_need_matrix_multiplication/)**

I built a cognitive architecture where all computation reduces to three bit operations: XOR, MAJ, POPCNT. No GEMM. No GPU. No floating-point weights. The core idea: transformer attention is a similarity computation. Float32 cosine computes it with 24,576 FLOPs. Binary Spatter Codes compute the same geometric measurement with 128 bit operations. Measured: 192x fewer ops, 32x less memory, ~480x faster. 26 modules in 1237 lines of C. One file. Any hardware: cc -O2 -o creation_os creation_os_v2.c -lm Includes a JEPA-style world model (energy = σ), n-gram language model (attention = σ), physics simulation (Noether conservation σ = 0.000000), value system with tamper detection, multi-model truth triangulation, metacognition, emotional memory, theory of mind, and 13 other cognitive modules. This is a research prototype built on Binary Spatter Codes (Kanerva, 1997). It demonstrates that cognitive primitives can be expressed in bit operations. It does not replace LLMs — the language module runs on 15 sentences. But the algebra is real, the benchmark is measured, and the architecture is open. https://github.com/spektre-labs/creation-os AGPL-3.0. Feedback welcome.

9h ago

---

**[I tracked what AI agents actually do when nobody's watching. Built a tool that replays every decision.](https://www.reddit.com/r/artificial/comments/1sm261q/i_tracked_what_ai_agents_actually_do_when_nobodys/)**

Been building AI agents for about a year now and the thing that always drove me crazy is you deploy an agent, it runs for hours, and you have absolutely no idea what it did. The logs say "task complete" 47 times but did it actually do 47 different things or did it just loop the same task over and over? I had an agent burn through about $340 in API credits over a weekend because it got stuck retrying the same request. The logs showed 200 OK on every call. Everything looked fine. It just kept doing the same thing for 6 hours straight while I slept. So I built something to fix this. It's called Octopoda and its basically an observability layer that sits underneath your agents. Every memory write, every decision, every recall gets logged on a timeline. You can literally press play and watch what your agent did at 3am, step by step, like scrubbing through a video. The part that surprised me most was the loop detection. Once I could see the full timeline I realised how often agents loop without you knowing. Not obvious infinite loops, subtle stuff. An agent that rewrites the same conclusion 8 times with slightly different wording. Or one that keeps checking the same API endpoint every 30 seconds even though the data hasn't changed. Each iteration costs tokens but produces nothing new. We track 5 signals for this: write similarity, key overwrite frequency, velocity spikes, alert frequency, and goal drift. When enough signals fire together it flags it and estimates how much money the loop is costing you per hour. One user had a research agent that was wasting about $10 an hour on duplicate writes before the detection caught it. It also does auto-checkpoints. Every 25 writes it saves a snapshot automatically so if something goes wrong you can roll back to any point with one click. No more losing an entire night of agent work because something corrupted at 4am. Works with LangChain, CrewAI, AutoGen, and OpenAI Agents SDK. One line to integrate: The dashboard shows everything in real time. Agent health scores, cost per agent, shared memory between agents, full audit trail with reasoning for every decision. Honestly the most useful thing is just being able to answer "what happened overnight" without spending an hour reading logs. Anyone else dealing with the "I have no idea what my agent did" problem? Curious how other people are handling observability for autonomous workflows. Let me know if anyone wants to check it out!

16h ago

---

**[What's a purely "you" thing you do with AI that brings you positive benefits?](https://www.reddit.com/r/artificial/comments/1sm70be/whats_a_purely_you_thing_you_do_with_ai_that/)**

For me it's three chats I've set up, two for my parents and one for me, for interpreting medical results, tracking medication against diet and lifestyle changes. Anonymized, I've put every condition, surgery and medication I (and they) have had, and it's amazing how virtually all the advice and questions are spot on. YES, caution is needed before jumping on any advice an AI gives you medically. But for interpreting results, explaining exams and procedures, and noting any indications between medication and foods/supplements (with verification independently) has been a real relief as my folks get older and it's harder to keep on top of everything they're taking. I also have a separate chat for my car (manufacturers warranty, owners manual, car insurance policy) and I can literally ask it about any button, lever, warning light or policy change. Same with my apartment/condo rules/repairs/appliance warrantees and owners manuals for large appliances. For fun, I also had the chat roleplay as Dr. Crusher from the Enterprise, and my car is managed by Tom Paris from Star Trek: Voyager, so it speaks to me as if it's those people. Anyone else doing anything weird and useful?

12h ago

---

---

## Google News: "ai"

**[Struggling shoe retailer Allbirds makes bizarre pivot to AI, adds $127 million in value](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)**

Allbirds announced a deal with American Exchange Group to sell its intellectual property and other assets for $39 million in March.

CNBC • 13h ago

---

**[That Meeting You Hate May Keep A.I. From Stealing Your Job](https://www.nytimes.com/2026/04/15/business/ai-jobs-human-work.html)**

The New York Times • 5h ago

---

**[Taiwan Market Cap Tops $4 Trillion on AI Boom, Overtaking UK](https://www.bloomberg.com/news/articles/2026-04-16/ai-driven-demand-pushes-taiwan-s-market-cap-ahead-of-the-uk)**

Bloomberg.com • 1h ago

---

**[How AI Is Changing The Way Small Towns Govern](https://www.forbes.com/sites/paulbaier/2026/04/15/how-ai-is-changing-the-way-small-towns-govern/)**

Forbes • 37m ago

---

**[Trump Stooge Who Fed Boss Crackpot Christ Meme Unmasked](https://www.thedailybeast.com/trump-stooge-who-fed-boss-crackpot-ai-jesus-christ-meme-unmasked-as-bill-pulte/)**

One of Trump’s most chaotic sycophants may have been behind his blasphemous AI post.

The Daily Beast • 50m ago

---

**[Trump posts new AI image of himself embracing Jesus amid backlash from Christians and ongoing rift with Pope Leo](https://www.yahoo.com/news/world/article/trump-posts-new-ai-image-of-himself-embracing-jesus-amid-backlash-from-christians-and-ongoing-rift-with-pope-leo-181356134.html)**

The president shared another Jesus meme on social media after insisting a controversial image he'd posted was intended to depict him as a doctor — and not Christ.

Yahoo • 10h ago

---

**[Iran Embassy in Tajikistan posts AI video of Jesus punching Trump in the face](https://thehill.com/policy/international/5832224-iran-trump-social-media-war/)**

The Hill • 11h ago

---

**[How Project Maven Put A.I. Into the Kill Chain](https://www.newyorker.com/books/under-review/how-project-maven-put-ai-into-the-kill-chain)**

A new book charts the creation of a secretive system that automates warfare for the military. The progression from target identification to target destruction is four clicks.

The New Yorker • 16h ago

---

**[Utility companies planning to invest $1.4 trillion in power grids for AI, report finds](https://www.cbsnews.com/video/utility-companies-planning-invest-trillions-power-grids-ai/)**

U.S. utility companies are planning to invest $1.4 trillion over the next five years to help strengthen the nation's power grid, according to a new report released Tuesday by the nonpartisan nonprofit consumer education organization PowerLines. CBS News MoneyWatch reporter Megan Cerullo has more details.

CBS News • 4h ago

---

**[AI is supercharging the US-Iran meme war](https://www.cnn.com/2026/04/15/world/video/ai-generated-videos-us-iran-meme-war-will-ripley-hnk-vrtc-digvid)**

Iranian embassies are flooding social media with viral AI-generated memes mocking President Donald Trump for the Iran war. CNN’s Will Ripley explains how “slopaganda” is accelerating a new kind of information war.

CNN • 18h ago

---

---

## HackerNews: "ai"

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 430 • 💬 382 • 2d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 273 • 💬 167 • 21h ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 261 • 💬 400 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 242 • 💬 216 • 12h ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 218 • 💬 169 • 8h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 211 • 💬 210 • 1d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 192 • 💬 108 • 1d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 186 • 💬 279 • 2d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 154 • 💬 34 • 2d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 145 • 💬 94 • 13h ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

---

## YouTube Videos: "ai"

**[Claude Is Melting Down. AI&#39;s Compute Crisis Explained.](https://www.youtube.com/watch?v=d1jReDZsGOc)**

The AI compute crisis is here. Anthropic's Claude is getting dumber and Opus 4.7 & OpenAI's Spud are about to make it worse.

📺 AI For Humans

👁️ 17K • 👍 832 • 💬 267 • ⏱️ 29:28 • 13h ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 23K • 👍 707 • 💬 169 • ⏱️ 1:27:18 • 2d ago

---

**[The 7 Skills You Need to Build AI Agents](https://www.youtube.com/watch?v=mtiOK2QG9Q0)**

As AI agents become more capable, the skills needed for AI jobs are shifting. Bri Kopecki breaks down the 7 skills you need to ...

📺 IBM Technology

👁️ 113K • 👍 5K • 💬 263 • ⏱️ 14:37 • 1d ago

---

**[Google New Gemini Skillz Turn Chrome Into an AI Beast](https://www.youtube.com/watch?v=5TA0Ul2eS_k)**

Try Seedance 2.0 on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-yDYwTG Google just dropped one of its biggest ...

📺 AI Revolution

👁️ 9K • 👍 407 • 💬 11 • ⏱️ 13:13 • 4h ago

---

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 196K • 👍 15K • 💬 2K • ⏱️ 7:52 • 1d ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 162K • 👍 4K • 💬 926 • ⏱️ 2:10:48 • 1d ago

---

**[Anthropic &#39;Claude Mythos&#39; model sparks AI doomsday fears](https://www.youtube.com/watch?v=pq7kSVp4Skg)**

Subscribe to LiveNOW from FOX! https://www.youtube.com/livenowfox?sub_confirmation=1 Where to watch LiveNOW from FOX: ...

📺 LiveNOW from FOX

👁️ 26K • 👍 356 • 💬 121 • ⏱️ 13:49 • 2d ago

---

**[What to know about Anthropic&#39;s new AI model and its stark warning](https://www.youtube.com/watch?v=bUbFFSZQ5w0)**

Former AI company founder and CEO Matt Shumer joins "CBS Mornings" to break down Anthropic's report about one of its AI ...

📺 CBS Mornings

👁️ 48K • 👍 478 • 💬 87 • ⏱️ 4:58 • 2d ago

---

**[Shoemaker Allbirds Suddenly Says It’s An AI Company](https://www.youtube.com/watch?v=iqz81FCd-NQ)**

Allbirds, the former minimalist shoe company that briefly surged in popularity among Silicon Valley tech workers a decade ago, ...

📺 Forbes

👁️ 5K • 👍 109 • 💬 17 • ⏱️ 2:16 • 6h ago

---

**[AI CEO vs engineer.](https://www.youtube.com/watch?v=CEz1AauzsAo)**

AI CEOs. Interview with a AI CEO vs AI Engineer with Josh Doe and Jackson Jineer - aired on © The AI. Programmer humor ...

📺 Kai Lentit

👁️ 244K • 👍 8K • 💬 160 • ⏱️ 1:01 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 85,549 • ❤️ 798 • 7h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 818 • ❤️ 683 • 1d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 91,474 • ❤️ 1,244 • 3d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,894,077 • ❤️ 1,936 • 5d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 12,827 • ❤️ 919 • 13h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 134,547 • ❤️ 1,134 • 5d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 26,673 • ❤️ 299 • 3d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 445 • ❤️ 297 • 8h ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 51,148 • ❤️ 223 • 5d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 419 • ❤️ 220 • 8h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 17 • 💬 1 • ⭐ 18,169 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,727 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 45 • 💬 2 • ⭐ 50,718 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 164 • 💬 9 • ⭐ 39,716 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 158 • 💬 2 • ⭐ 60,007 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,756 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)**

*Fei Tang, Zhiqiong Lu, Boxuan Zhang et al. (7 authors)*

🏢 Zhejiang University

ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

▲ 122 • 💬 6 • ⭐ 404 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.11784) • [💻 code](https://github.com/ZJU-REAL/ClawGUI) • [🔗 project](https://zju-real.github.io/ClawGUI-Page/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 53,131 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,334 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 37 • 💬 2 • ⭐ 29,715 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 46.6k • 🔱 6.1k • 1h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 34.1k • 🔱 6.8k • 1d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 32.7k • 🔱 1.5k • 13h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 27.5k • 🔱 3.0k • 4h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.9k • 🔱 508 • 52s ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 3d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.7k • 🔱 1.1k • 20d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.7k • 🔱 772 • 1d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 173 • 3h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 450 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
