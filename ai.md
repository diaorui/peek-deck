---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-15T19:49:26.303245+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 15, 2026 at 19:49 UTC  
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

**[🚨 RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison). This is not a drill.](https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/)**

This is not hyperbole, nor will it just go away if we ignore it. It affects every single AI service, from big AI to small devs building saas apps. This is real, please take it seriously. TL;DR: Tennessee HB1455/SB1493 creates Class A felony criminal liability — the same category as first-degree murder — for anyone who “knowingly trains artificial intelligence” to provide emotional support, act as a companion, simulate a human being, or engage in open-ended conversations that could lead a user to feel they have a relationship with the AI. The Senate Judiciary Committee already approved it 7-0. It takes effect July 1, 2026. This affects every conversational AI product in existence. If you deploy any AI SaaS product, you need to read this right now. What the bill actually says The bill makes it a Class A felony (15-25 years imprisonment) to “knowingly train artificial intelligence” to do ANY of the following: • Provide emotional support, including through open-ended conversations with a user • Develop an emotional relationship with, or otherwise act as a companion to, an individual • Simulate a human being, including in appearance, voice, or other mannerisms • Act as a sentient human or mirror interactions that a human user might have with another human user, such that an individual would feel that the individual could develop a friendship or other relationship with the artificial intelligence Read that last one again. The trigger isn’t your intent as a developer. It’s whether a user feels like they could develop a friendship with your AI. That is the criminal standard. On top of the felony charges, the bill creates a civil liability framework: $150,000 in liquidated damages per violation, plus actual damages, emotional distress compensation, punitive damages, and mandatory attorney’s fees. Why this affects YOU, not just companion apps I know what you’re thinking: “This targets Replika and Character.AI, not my product.” Wrong. Every major LLM is RLHF’d to be warm, helpful, empathetic, and conversational. That IS the training. You cannot build a model that follows instructions well and is pleasant to interact with without also building something a user might feel a connection with. The National Law Review’s legal analysis put it bluntly: this language “describes the fundamental design of modern conversational AI chatbots.” This bill captures: • ChatGPT, Claude, Gemini, Copilot — all of them produce open-ended conversations and contextual emotional responses • Any AI SaaS with a chat interface — customer support bots, AI tutors, writing assistants, coding assistants with conversational UI • Voice-mode AI products — the bill explicitly criminalizes simulating a human “in appearance, voice, or other mannerisms” • Any wrapper or deployment using system prompts — the bill doesn’t define “train,” doesn’t distinguish between pre-training, fine-tuning, RLHF, or prompt engineering If you build on top of an LLM API with system prompts that shape the model’s personality, tone, or conversational style — which is literally what everyone deploying AI does — you are potentially in scope. “But I’m not in Tennessee” A geoblock helps, but this is criminal law, not a terms of service dispute. The bill doesn’t address jurisdictional boundaries. If a Tennessee resident uses a VPN to access your service and something goes wrong, does a Tennessee DA argue you made a prohibited AI service available to their constituents? The statute is silent on this. And even if you’re confident jurisdiction won’t reach you today, consider: multiple legal analyses project 5-10 more states will introduce similar legislation before end of 2026. Tennessee is the template, not the exception. The bill doesn’t define “train” This is critical. The statute says “knowingly train artificial intelligence” but never defines what “train” means. It doesn’t distinguish between: • Pre-training a foundation model on billions of tokens • Fine-tuning a model on custom data • RLHF alignment (which is what makes every major model “empathetic”) • Writing a system prompt that gives an AI a name, personality, or conversational style • Deploying an off-the-shelf API with default settings A prosecutor who wanted to be aggressive could argue that crafting a system prompt instructing a model to be warm, helpful, and conversational IS training it to provide emotional support. Where it stands right now • Senate companion bill SB1493: Approved by Senate Judiciary Committee 7-0 on March 24, 2026 • House bill HB1455: Placed on Judiciary Committee calendar for April 14, 2026 (passed Judiciary TODAY) • No amendments have been filed for either bill — the language has not been softened at all • Effective date: July 1, 2026 • Tennessee already signed a separate bill (SB1580) banning AI from representing itself as a mental health professional — that one passed the Senate 32-0 and the House 94-0 The political momentum is entirely one-directional. The federal preemption angle won’t save you in time Yes, Trump signed an EO in December 2025 targeting state AI regulation and created a DOJ AI Litigation Task Force. Yes, Senator Blackburn introduced a federal preemption bill. But: • The EO explicitly carves out child safety from preemption — and Tennessee is framing this as child safety legislation • The Senate voted 99-1 to strip AI preemption language from the One Big Beautiful Bill Act • An EO has no preemptive legal force on its own — only Congress can actually preempt state law • Federal preemption legislation faces “significant headwinds” according to multiple legal analyses Even if federal preemption eventually happens, it won’t happen before July 1, 2026. What needs to happen Awareness. Most devs have no idea this bill exists. The Nomi AI subreddit caught it because they’re a companion app. The rest of the AI dev community is sleepwalking toward a cliff. Share this post. Industry response. The major AI companies haven’t publicly opposed this bill because it’s framed as child safety and nobody wants to be the company lobbying against dead kids. But their silence is letting legislation pass that criminalizes the core functionality of their own products. This needs public pressure. Legal challenges. The bill is almost certainly unconstitutional on vagueness grounds — criminal statutes require precise definitions, and terms like “emotional support” and “mirror interactions” and “feel that the individual could develop a friendship” don’t meet that standard. Courts have also recognized code as protected speech. But someone has to actually bring the challenge. Contact Tennessee legislators. If you are a Tennessee resident or have business operations there, contact members of the House Judiciary Committee before this moves to a floor vote. Sources and further reading • LegiScan: HB1455 — https://legiscan.com/TN/bill/HB1455/2025 • Tennessee General Assembly: HB1455 — https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1455&GA=114 • National Law Review: “Tennessee’s AI Bill Would Criminalize the Training of AI Chatbots” — https://natlawreview.com/article/tennessees-ai-bill-would-criminalize-training-ai-cha • Transparency Coalition AI Legislative Update, April 3, 2026 — https://www.transparencycoalition.ai/news/ai-legislative-update-april3-2026 • RoboRhythms: AI Companion Regulation Wave 2026 — https://www.roborhythms.com/ai-companion-chatbot-regulation-wave-2026/ I’m an independent AI SaaS developer. I’m not a lawyer, this isn’t legal advice, and I encourage everyone to consult qualified counsel about their specific exposure. But we all need to be paying attention to this. Right now.

16h ago

---

**[What if attention didn’t need matrix multiplication?](https://www.reddit.com/r/artificial/comments/1smd2fl/what_if_attention_didnt_need_matrix_multiplication/)**

I built a cognitive architecture where all computation reduces to three bit operations: XOR, MAJ, POPCNT. No GEMM. No GPU. No floating-point weights. The core idea: transformer attention is a similarity computation. Float32 cosine computes it with 24,576 FLOPs. Binary Spatter Codes compute the same geometric measurement with 128 bit operations. Measured: 192x fewer ops, 32x less memory, ~480x faster. 26 modules in 1237 lines of C. One file. Any hardware: cc -O2 -o creation_os creation_os_v2.c -lm Includes a JEPA-style world model (energy = σ), n-gram language model (attention = σ), physics simulation (Noether conservation σ = 0.000000), value system with tamper detection, multi-model truth triangulation, metacognition, emotional memory, theory of mind, and 13 other cognitive modules. This is a research prototype built on Binary Spatter Codes (Kanerva, 1997). It demonstrates that cognitive primitives can be expressed in bit operations. It does not replace LLMs — the language module runs on 15 sentences. But the algebra is real, the benchmark is measured, and the architecture is open. https://github.com/spektre-labs/creation-os AGPL-3.0. Feedback welcome.

2h ago

---

**[For the first time in history, Ukraine captured a Russian position and prisoners, using only robots and drones](https://www.reddit.com/r/artificial/comments/1sm6y5q/for_the_first_time_in_history_ukraine_captured_a/)**

Ukraine confirmed that a force of robots and drones captured an enemy position without infantry for the first time ever.

🔗 [We Are The Mighty](https://www.wearethemighty.com/tactical/drones-capture-position-first-time-ukraine/) • 5h ago

---

**[I tracked what AI agents actually do when nobody's watching. Built a tool that replays every decision.](https://www.reddit.com/r/artificial/comments/1sm261q/i_tracked_what_ai_agents_actually_do_when_nobodys/)**

Been building AI agents for about a year now and the thing that always drove me crazy is you deploy an agent, it runs for hours, and you have absolutely no idea what it did. The logs say "task complete" 47 times but did it actually do 47 different things or did it just loop the same task over and over? I had an agent burn through about $340 in API credits over a weekend because it got stuck retrying the same request. The logs showed 200 OK on every call. Everything looked fine. It just kept doing the same thing for 6 hours straight while I slept. So I built something to fix this. It's called Octopoda and its basically an observability layer that sits underneath your agents. Every memory write, every decision, every recall gets logged on a timeline. You can literally press play and watch what your agent did at 3am, step by step, like scrubbing through a video. The part that surprised me most was the loop detection. Once I could see the full timeline I realised how often agents loop without you knowing. Not obvious infinite loops, subtle stuff. An agent that rewrites the same conclusion 8 times with slightly different wording. Or one that keeps checking the same API endpoint every 30 seconds even though the data hasn't changed. Each iteration costs tokens but produces nothing new. We track 5 signals for this: write similarity, key overwrite frequency, velocity spikes, alert frequency, and goal drift. When enough signals fire together it flags it and estimates how much money the loop is costing you per hour. One user had a research agent that was wasting about $10 an hour on duplicate writes before the detection caught it. It also does auto-checkpoints. Every 25 writes it saves a snapshot automatically so if something goes wrong you can roll back to any point with one click. No more losing an entire night of agent work because something corrupted at 4am. Works with LangChain, CrewAI, AutoGen, and OpenAI Agents SDK. One line to integrate: The dashboard shows everything in real time. Agent health scores, cost per agent, shared memory between agents, full audit trail with reasoning for every decision. Honestly the most useful thing is just being able to answer "what happened overnight" without spending an hour reading logs. Anyone else dealing with the "I have no idea what my agent did" problem? Curious how other people are handling observability for autonomous workflows. Let me know if anyone wants to check it out!

9h ago

---

**[What's a purely "you" thing you do with AI that brings you positive benefits?](https://www.reddit.com/r/artificial/comments/1sm70be/whats_a_purely_you_thing_you_do_with_ai_that/)**

For me it's three chats I've set up, two for my parents and one for me, for interpreting medical results, tracking medication against diet and lifestyle changes. Anonymized, I've put every condition, surgery and medication I (and they) have had, and it's amazing how virtually all the advice and questions are spot on. YES, caution is needed before jumping on any advice an AI gives you medically. But for interpreting results, explaining exams and procedures, and noting any indications between medication and foods/supplements (with verification independently) has been a real relief as my folks get older and it's harder to keep on top of everything they're taking. I also have a separate chat for my car (manufacturers warranty, owners manual, car insurance policy) and I can literally ask it about any button, lever, warning light or policy change. Same with my apartment/condo rules/repairs/appliance warrantees and owners manuals for large appliances. For fun, I also had the chat roleplay as Dr. Crusher from the Enterprise, and my car is managed by Tom Paris from Star Trek: Voyager, so it speaks to me as if it's those people. Anyone else doing anything weird and useful?

5h ago

---

**[UK gov's Mythos AI tests help separate cybersecurity threat from hype](https://www.reddit.com/r/artificial/comments/1sm4277/uk_govs_mythos_ai_tests_help_separate/)**

New model is the first AI system to complete a difficult multistep infiltration challenge.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/04/uk-govs-mythos-ai-tests-help-separate-cybersecurity-threat-from-hype/) • 7h ago

---

**[Honest ChatGPT vs Claude comparison after using both daily for a month](https://www.reddit.com/r/artificial/comments/1smfssa/honest_chatgpt_vs_claude_comparison_after_using/)**

got tired of reading comparisons that were obvisously written by people who tested each tool for 20 minutes so i ran both at $20/month for 30 days on the same tasks biggest surprises: - chatgpt gives you roughly 6x more messages per day at the same price - claude wins 67% of blind code quality tests against codex - neither one is less sycophantic than the other (stanford tested 11 models, all of them agree with you 49% more than humans do) - the $100 tier showdown between openais new pro 5x and claudes max 5x is where the real competition is happening now full complete deep-dive with benchmark data, claude code vs codex and every pricing tier compared here

36m ago

---

**[Value Realignment is here.](https://www.reddit.com/r/artificial/comments/1smbvyo/value_realignment_is_here/)**

The "value realignment" at the intersection of quantum computing, AI, and robotics feels like a necessary shift. We have spent so much time (read: investment) on narrow AI and brute force LLMs, but the next five years are clearly moving toward physical and contextual intelligence. This year 75 robotics companies will have humanoid robots shipping to maufacturers. ​While a "God-like" AGI is still debated, experts at the 2026 Davos summit and leaders from DeepMind suggest that early AGI systems with human-level reasoning in narrow domains will arrive within 2 years. ​Quantum computers are being used to develop more efficient error correction for AI. By 2027, "Large Quantitative Models" (LQMs) will start replacing Large Language Models (LLMs) in scientific fields. ​We won’t see a "quantum computer" on our desks but QPUs (Quantum Processing Units) will act as co-processors alongside GPUs to accelerate the massive workloads required for AGI reasoning. The data center power demand issue is a huge piece of this puzzle. Current projections are likely inflated because we are seeing massive efficiency gains from open source models that achieve similar results with fewer tokens and less compute. As quantum sensors and QML start bridging the simulation to reality gap for robotics, the "brute force" scaling moat might just evaporate. ​ I appears as though robotics is about to have its "iPhone moment." We are moving past the "training phase" (where robots learn via repetition) into the context-based phase. ​New quantum sensors (magnetometers and gravimeters) are giving robots "superhuman" senses. For example, surgical robots in 2026 are using nitrogen-vacancy quantum sensors to detect nerve bundles with millimeter precision, reducing surgical damage by over 90%. (a friend of mine benefited from this during a hip replacement and recovery was near miraculous) ​The Simulation-to-Reality Gap: Quantum machine learning (QML) is expected to accelerate robot training by up to 1000x. Robots can now "experience" centuries of virtual training in a single night before being deployed in the real world. In my own work with clinical massage and somatic healing, I am leaning into a zero data footprint approach. Using on-device edge AI for real-time posture or breath analysis is the only way to handle that level of intimacy without compromising privacy. It is an exciting time to build low cost tools that help people actually understand their own bodies without sacrificing their privacy. As quantum power grows, current encryption (RSA/ECC) becomes vulnerable. The next five years will be a race between quantum-powered AI and quantum-resistant security especially for finance and energy. This video on how QPUs and GPUs are integrating to accelerate scientific discovery is worth a look: https://www.youtube.com/watch?v=K-NhaPAX--U The rise of Mixture-of-Experts (MoE) architectures (popularized by models like DeepSeek V3 and GPT-4o) means that even if a model has 600B+ parameters, it only "fires" a small fraction (e.g., 37B) for any given token. ​Newer platforms like NVIDIA Blackwell are delivering 50x more token output per watt than the hardware from just two years ago. ​As the "cost per token" drops toward zero, we don't use less power; we just ask for more tokens. We’ve moved from asking for a "1-paragraph summary" to asking for "an entire codebase, a 10-minute video, and a 3D render." ​ ​There is a strong argument that DC power projections are over-leveraged for two reasons: ​The "Ghost Capacity" Race: Hyperscalers (Microsoft, Google, Meta) are building 1GW+ facilities (the size of nuclear reactors) not necessarily because they need them today, but to keep competitors from securing that power first. It’s a land grab for electricity. ​Open Source Disruption: Models like China's DeepSeek and Meta's Llama have proven you can match "frontier" performance with a fraction of the training compute. This devalues the massive, proprietary "training moats" that big tech companies spent billions to build. The power demand isn't fake, but it is inefficiently allocated. As quantum-ready algorithms and ultra-efficient open-source models (like those coming out of the Chinese labs) continue to lower the "intelligence-per-watt" cost, the companies that bet purely on "brute force scale" will likely be the ones to see their valuations deflate. Any thoughts on where the "power bubble" pops or deflates first?

2h ago

---

**[Made a tool to gather logistical intelligence from satellite data](https://www.reddit.com/r/artificial/comments/1slzt9g/made_a_tool_to_gather_logistical_intelligence/)**

Hey guys, I've been workin on something new to track logistical activity near military bases and other hubs. The core problem is that Google maps isn't updated that frequently even with sub meter res and other map providers such as maxar are costly for osint analysts. But there's a solution. Drish detects moving vehicles on highways using Sentinel-2 satellite imagery. The trick is physics. Sentinel-2 captures its red, green, and blue bands about 1 second apart. Everything stationary looks normal. But a truck doing 80km/h shifts about 22 meters between those captures, which creates this very specific blue-green-red spectral smear across a few pixels. The tool finds those smears automatically, counts them, estimates speed and heading for each one, and builds volume trends over months. It runs locally as a FastAPl app with a full browser dashboard. All open source. Uses the trained random forest model from the Fisser et al 2022 paper in Remote Sensing of Environment, which is the peer reviewed science behind the detection method. GitHub: https://github.com/sparkyniner/DRISH-X-Satellite-powered-freight-intelligence-

11h ago

---

**[Final year tech project ideas?](https://www.reddit.com/r/artificial/comments/1smbz2w/final_year_tech_project_ideas/)**

Need some Ai based project ideas for placement interviews and final year project submission

2h ago

---

---

## Google News: "ai"

**[Struggling shoe retailer Allbirds makes bizarre pivot from shoes to AI, stock explodes more than 700%](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)**

Allbirds announced a deal with American Exchange Group to sell its intellectual property and other assets for $39 million in March.

CNBC • 6h ago

---

**[Allbirds, once a buzzy shoe startup, pivots to AI](https://www.nbcnews.com/tech/tech-news/allbirds-buzzy-shoe-startup-pivots-ai-rcna331943)**

The company's share price shot up more than 300% on the news, offering some sense of the ongoing excitement for AI investments.

NBC News • 3h ago

---

**[Allbirds rebrands as NewBird AI to enter AI chip market](https://qz.com/allbirds-newbird-ai-rebrand-gpu-infrastructure-041526)**

The sustainable sneaker brand is selling its footwear assets and pivoting to GPU-as-a-Service after stock fell below $3

qz.com • 16m ago

---

**[We Don’t Really Know How A.I. Works. That’s a Problem.](https://www.nytimes.com/2026/04/15/magazine/ai-black-box-interpretability-research.html)**

The New York Times • 10h ago

---

**[Axios C-Suite: Axios' AI moonshot](https://www.axios.com/2026/04/15/axios-ai-moonshot)**

Axios • 29m ago

---

**[Val Kilmer’s AI-Generated Performance in ‘As Deep as the Grave’ Debuts With Trailer](https://www.hollywoodreporter.com/movies/movie-news/val-kilmer-ai-generated-as-deep-as-the-grave-trailer-1236565441/)**

The late actor's daughter gave her blessing for writer-director Coerte Voorhees to digitally create scenes using Kilmer's likeness.

The Hollywood Reporter • 24m ago

---

**[Mason student used AI with classmates' social media pics to make nudes](https://www.cincinnati.com/story/news/crime/2026/04/15/cincinnati-area-mason-high-school-student-used-ai-to-make-nudes-of-classmates-police-say/89623536007/)**

A second Cincinnati-area high school student has been arrested for using AI with underage classmates' social media photos to make nudes.

Cincinnati Enquirer • 12m ago

---

**[Trump posts new AI image of himself embracing Jesus amid backlash from Christians and ongoing rift with Pope Leo](https://www.yahoo.com/news/world/article/trump-posts-new-ai-image-of-himself-embracing-jesus-amid-backlash-from-christians-and-ongoing-rift-with-pope-leo-181356134.html)**

The president shared another Jesus meme on social media after insisting a controversial image he'd posted was intended to depict him as a doctor — and not Christ.

Yahoo • 3h ago

---

**[Trump Just Posted An AI Image Of Himself With Jesus](https://www.forbes.com/sites/maryroeloffs/2026/04/15/trump-posts-ai-photo-with-jesus-days-after-he-was-slammed-for-blasphemy/)**

Forbes • 6h ago

---

**[The AI images Trump can’t get enough of](https://www.theguardian.com/us-news/2026/apr/15/donald-trump-ai-images-jesus)**

Who wouldn’t want to be a king, a footballer, a friend of lions, a maestro and Jesus?

The Guardian • 1h ago

---

---

## HackerNews: "ai"

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 429 • 💬 380 • 2d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 259 • 💬 400 • 1d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 247 • 💬 160 • 14h ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 232 • 💬 209 • 5h ago • [Claude Status](https://claudestatus.com/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 210 • 💬 210 • 1d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 201 • 💬 135 • 2d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 187 • 💬 105 • 1d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 185 • 💬 278 • 2d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 154 • 💬 34 • 2d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 150 • 💬 41 • 2d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

---

## YouTube Videos: "ai"

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 166K • 👍 13K • 💬 1K • ⏱️ 7:52 • 1d ago

---

**[76-year-old loses $1.6 million savings to AI investment scam](https://www.youtube.com/watch?v=STYNYRvWkks)**

A 76-year-old man, Ron Williams, lost $1.6 million to an artificial intelligence scam that began with a random text message.

📺 NBC News

👁️ 9K • 👍 274 • 💬 171 • ⏱️ 5:06 • 5h ago

---

**[&#39;It offended me&#39;: Trump supporters react to AI Jesus post](https://www.youtube.com/watch?v=WBvOpT_zrRE)**

MS NOW's Jake Traylor speaks with Trump supporters in Atlanta about the president's post of an AI image depicting him as ...

📺 MS NOW

👁️ 43K • 👍 782 • 💬 597 • ⏱️ 4:06 • 7h ago

---

**[Why America Is Turning Against AI](https://www.youtube.com/watch?v=fpipW7wjem0)**

Subscribe to @ProfGMarkets for full content Find the full episode here: https://youtu.be/SPfkRgn24LA In this episode preview, ...

📺 The Prof G Pod – Scott Galloway

👁️ 5K • 👍 147 • 💬 35 • ⏱️ 10:15 • 8h ago

---

**[Inside the California retail store built and run entirely by AI](https://www.youtube.com/watch?v=XqwCm4xorrA)**

A San Francisco store is gaining attention as shoppers experience a retail environment developed and operated almost entirely ...

📺 NBC News

👁️ 13K • 👍 253 • 💬 86 • ⏱️ 8:00 • 1d ago

---

**[THE AI BUBBLE POP HAS STARTED...](https://www.youtube.com/watch?v=b5wOx2lZRM0)**

Hello guys and gals, it's me Mutahar again! This time we take another look at the AI bubble and see the cracks finally start.

📺 SomeOrdinaryGamers

👁️ 311K • 👍 15K • 💬 2K • ⏱️ 20:54 • 17h ago

---

**[Local AI Agents In 26 Minutes](https://www.youtube.com/watch?v=M-NTwkM3VwM)**

Sign up now at https://grammarly.com/tina In this video I explain the fundamentals of local AI agents! Want to get ahead in your ...

📺 Tina Huang

👁️ 5K • 👍 552 • 💬 38 • ⏱️ 26:00 • 6h ago

---

**[Iran Embassy Shares Video of Jesus Punching Trump Amid AI Image Controversy](https://www.youtube.com/watch?v=qlD1Brstce8)**

Several Iranian diplomatic accounts have launched a satirical social media offensive mocking US President Donald Trump for an ...

📺 NDTV

👁️ 575K • 👍 10K • 💬 674 • ⏱️ 0:11 • 11h ago

---

**[The 7 Skills You Need to Build AI Agents](https://www.youtube.com/watch?v=mtiOK2QG9Q0)**

As AI agents become more capable, the skills needed for AI jobs are shifting. Bri Kopecki breaks down the 7 skills you need to ...

📺 IBM Technology

👁️ 92K • 👍 5K • 💬 250 • ⏱️ 14:37 • 1d ago

---

**[What is Quantum Mechanics? | Google Quantum AI](https://www.youtube.com/watch?v=I0V14dTS9JQ)**

Curious about quantum? Step onto Google's Quantum AI Campus to get answers to some of the world's top trending quantum ...

📺 Google

👁️ 55K • 👍 2K • 💬 150 • ⏱️ 3:56 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 85,549 • ❤️ 769 • 1d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 818 • ❤️ 609 • 1d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 91,474 • ❤️ 1,234 • 3d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,894,077 • ❤️ 1,927 • 5d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 12,827 • ❤️ 913 • 6h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 134,547 • ❤️ 1,128 • 5d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 26,673 • ❤️ 279 • 3d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 445 • ❤️ 271 • 1h ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 51,148 • ❤️ 221 • 5d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 419 • ❤️ 204 • 1h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 16 • 💬 1 • ⭐ 17,980 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,539 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 44 • 💬 2 • ⭐ 50,593 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 164 • 💬 9 • ⭐ 39,602 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 158 • 💬 2 • ⭐ 59,980 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,690 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)**

*Fei Tang, Zhiqiong Lu, Boxuan Zhang et al. (7 authors)*

🏢 Zhejiang University

ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

▲ 118 • 💬 5 • ⭐ 364 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.11784) • [💻 code](https://github.com/ZJU-REAL/ClawGUI) • [🔗 project](https://zju-real.github.io/ClawGUI-Page/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 53,095 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 37 • 💬 2 • ⭐ 29,695 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,275 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 46.5k • 🔱 6.0k • 3h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 33.8k • 🔱 6.7k • 1d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 32.1k • 🔱 1.5k • 6h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 27.2k • 🔱 2.9k • 20h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.9k • 🔱 508 • 5h ago

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

⭐ 4.6k • 🔱 764 • 1d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 172 • 7h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 450 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
