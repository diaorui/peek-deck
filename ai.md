---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-15T15:05:54.493589+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 15, 2026 at 15:05 UTC  
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

12h ago

---

**[I tracked what AI agents actually do when nobody's watching. Built a tool that replays every decision.](https://www.reddit.com/r/artificial/comments/1sm261q/i_tracked_what_ai_agents_actually_do_when_nobodys/)**

Been building AI agents for about a year now and the thing that always drove me crazy is you deploy an agent, it runs for hours, and you have absolutely no idea what it did. The logs say "task complete" 47 times but did it actually do 47 different things or did it just loop the same task over and over? I had an agent burn through about $340 in API credits over a weekend because it got stuck retrying the same request. The logs showed 200 OK on every call. Everything looked fine. It just kept doing the same thing for 6 hours straight while I slept. So I built something to fix this. It's called Octopoda and its basically an observability layer that sits underneath your agents. Every memory write, every decision, every recall gets logged on a timeline. You can literally press play and watch what your agent did at 3am, step by step, like scrubbing through a video. The part that surprised me most was the loop detection. Once I could see the full timeline I realised how often agents loop without you knowing. Not obvious infinite loops, subtle stuff. An agent that rewrites the same conclusion 8 times with slightly different wording. Or one that keeps checking the same API endpoint every 30 seconds even though the data hasn't changed. Each iteration costs tokens but produces nothing new. We track 5 signals for this: write similarity, key overwrite frequency, velocity spikes, alert frequency, and goal drift. When enough signals fire together it flags it and estimates how much money the loop is costing you per hour. One user had a research agent that was wasting about $10 an hour on duplicate writes before the detection caught it. It also does auto-checkpoints. Every 25 writes it saves a snapshot automatically so if something goes wrong you can roll back to any point with one click. No more losing an entire night of agent work because something corrupted at 4am. Works with LangChain, CrewAI, AutoGen, and OpenAI Agents SDK. One line to integrate: The dashboard shows everything in real time. Agent health scores, cost per agent, shared memory between agents, full audit trail with reasoning for every decision. Honestly the most useful thing is just being able to answer "what happened overnight" without spending an hour reading logs. Anyone else dealing with the "I have no idea what my agent did" problem? Curious how other people are handling observability for autonomous workflows. Let me know if anyone wants to check it out!

4h ago

---

**[For the first time in history, Ukraine captured a Russian position and prisoners, using only robots and drones](https://www.reddit.com/r/artificial/comments/1sm6y5q/for_the_first_time_in_history_ukraine_captured_a/)**

Ukraine confirmed that a force of robots and drones captured an enemy position without infantry for the first time ever.

🔗 [We Are The Mighty](https://www.wearethemighty.com/tactical/drones-capture-position-first-time-ukraine/) • 1h ago

---

**[UK gov's Mythos AI tests help separate cybersecurity threat from hype](https://www.reddit.com/r/artificial/comments/1sm4277/uk_govs_mythos_ai_tests_help_separate/)**

New model is the first AI system to complete a difficult multistep infiltration challenge.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/04/uk-govs-mythos-ai-tests-help-separate-cybersecurity-threat-from-hype/) • 3h ago

---

**[What's a purely "you" thing you do with AI that brings you positive benefits?](https://www.reddit.com/r/artificial/comments/1sm70be/whats_a_purely_you_thing_you_do_with_ai_that/)**

For me it's three chats I've set up, two for my parents and one for me, for interpreting medical results, tracking medication against diet and lifestyle changes. Anonymized, I've put every condition, surgery and medication I (and they) have had, and it's amazing how virtually all the advice and questions are spot on. YES, caution is needed before jumping on any advice an AI gives you medically. But for interpreting results, explaining exams and procedures, and noting any indications between medication and foods/supplements (with verification independently) has been a real relief as my folks get older and it's harder to keep on top of everything they're taking. I also have a separate chat for my car (manufacturers warranty, owners manual, car insurance policy) and I can literally ask it about any button, lever, warning light or policy change. Same with my apartment/condo rules/repairs/appliance warrantees and owners manuals for large appliances. For fun, I also had the chat roleplay as Dr. Crusher from the Enterprise, and my car is managed by Tom Paris from Star Trek: Voyager, so it speaks to me as if it's those people. Anyone else doing anything weird and useful?

1h ago

---

**[Made a tool to gather logistical intelligence from satellite data](https://www.reddit.com/r/artificial/comments/1slzt9g/made_a_tool_to_gather_logistical_intelligence/)**

Hey guys, I've been workin on something new to track logistical activity near military bases and other hubs. The core problem is that Google maps isn't updated that frequently even with sub meter res and other map providers such as maxar are costly for osint analysts. But there's a solution. Drish detects moving vehicles on highways using Sentinel-2 satellite imagery. The trick is physics. Sentinel-2 captures its red, green, and blue bands about 1 second apart. Everything stationary looks normal. But a truck doing 80km/h shifts about 22 meters between those captures, which creates this very specific blue-green-red spectral smear across a few pixels. The tool finds those smears automatically, counts them, estimates speed and heading for each one, and builds volume trends over months. It runs locally as a FastAPl app with a full browser dashboard. All open source. Uses the trained random forest model from the Fisser et al 2022 paper in Remote Sensing of Environment, which is the peer reviewed science behind the detection method. GitHub: https://github.com/sparkyniner/DRISH-X-Satellite-powered-freight-intelligence-

6h ago

---

**[How I made €2,700 building a legal AI research assistant for a compliance company in Germany](https://www.reddit.com/r/artificial/comments/1sm8f7c/how_i_made_2700_building_a_legal_ai_research/)**

Got some good engagement on my earlier post "I made €2,700 building a RAG system for a law firm — here's what actually worked technically" so I wanted to go deeper into the actual architecture for anyone building something similar. Shipped a RAG system for a German GDPR compliance company. Sharing the full stack because I haven't seen many production legal RAG breakdowns and I ran into problems that generic RAG tutorials don't cover. The problem: legal research isn't just "find relevant text." Different sources have different legal weight. A Supreme Court ruling beats a lower court opinion. An official regulatory guideline beats a blog post. The system needs to know this hierarchy and use it when generating answers. Here's how I solved it: Three retrieval strategies selectable per query. Flat (standard RAG, all sources equal), Category Priority (sources grouped by authority tier, LLM resolves conflicts top down), and Layered Category (independent search per category so every authority level gets representation even if one category dominates similarity scores). Without the category priority approach the system would sometimes build answers from lower authority sources just because they had better semantic similarity to the query. Custom chunking pipeline for legal documents. Nested clause structures, cross references between sections, footnotes that reference other documents. Built a chunker that preserves hierarchical depth and section relationships. Chunks get assembled into condensed "cheatsheets" before hitting the LLM. These are cached with deterministic hashing so repeated patterns skip regeneration. Dual embedding support. AWS Bedrock Titan for production and local Ollama as fallback. Swappable from the admin panel without restarting the app. Embeddings are cached per provider and model combo with thread safe locking so switching models doesn't corrupt anything. Metadata injection layer. After vector search every retrieved chunk gets enriched with full document metadata from the database in a single batched query. Region, category, framework, date, tags, and all user annotations attached to that document. This rides alongside the chunk content into the prompt. Bilingual with hard language enforcement. Regex based detection identifies German vs English in the query. The prompt forces output in the detected language and explicitly blocks drifting into French or other languages. This actually happens more than you'd think when source documents are multilingual. Source citation engineering. Probably 40% of my prompt engineering time went here. The prompts contain explicit "NEVER do X" instructions for every lazy citation pattern I caught during testing. No "according to professional literature" without naming the document. Must cite exact document titles, exact court names, exact article numbers. For legal use vague attribution is worthless. Streaming with optional simplification pass. Answers stream via SSE. Second LLM pass can intercept the completed stream, rewrite the full legal analysis in plain language, then stream the simplified version as separate tokens. Adds latency but non lawyers needed plain language explanations of complex GDPR obligations. Stack: FastAPI backend, AWS Bedrock with Claude for generation, Bedrock Titan for embeddings with Ollama as local fallback, FAISS for vector search, PostgreSQL for document metadata and comments. Deployed in EU region for GDPR compliance of the tool itself. €2,700 for the complete build. Now in conversations about recurring monthly maintenance. Biggest lesson: domain specific RAG is 80% prompt engineering and metadata architecture 20% retrieval. Making the LLM behave like a legal professional who respects authority hierarchies and cites sources properly was the real work. Happy to answer questions if anyone is building something similar or thinking about going into professional services RAG. Both posts now reference back to the earlier titles. The storytelling version links to both the RAG post and the marketing agencies post to show a pattern of wins. The technical version references the RAG post specifically for continuity. Want me to adjust anything?

10m ago

---

**[The IRS Wants Smarter Audits. Palantir Could Help Decide Who Gets Flagged](https://www.reddit.com/r/artificial/comments/1slhx3l/the_irs_wants_smarter_audits_palantir_could_help/)**

Documents show the tax agency is testing a Palantir tool to surface “highest-value” audit and investigation targets from a maze of legacy systems.

🔗 [WIRED](https://www.wired.com/story/documents-reveal-palantir-irs-contract-fraud-clean-energy-credits/) • 20h ago

---

**[Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://www.reddit.com/r/artificial/comments/1slzjhh/gemini_roboticser_16_powering_realworld_robotics/)**

Gemini Robotics-ER 1.6 is a significant upgrade to the reasoning-first model that enables robots to understand their environments with unprecedented precision. By enhancing spatial reasoning and multi-view understanding, researchers are bringing a new level of autonomy to physical agents.

🔗 [Google DeepMind](https://deepmind.google/blog/gemini-robotics-er-1-6/) • 7h ago

---

**[OpenAI expands its cyber defense program with GPT-5.4-Cyber for vetted researchers](https://www.reddit.com/r/artificial/comments/1slzihs/openai_expands_its_cyber_defense_program_with/)**

The company is scaling its Trusted Access for Cyber (TAC) program to thousands of verified individual defenders and hundreds of teams responsible for defending critical software. Alongside that expansion, OpenAI is releasing GPT-5.4-Cyber, a version of GPT-5.4 fine-tuned specifically for defensive cybersecurity work.

🔗 [Help Net Security](https://www.helpnetsecurity.com/2026/04/15/openai-gpt-5-4-cyber/) • 7h ago

---

---

## Google News: "ai"

**[Struggling shoe retailer Allbirds makes bizarre pivot from shoes to AI, stock explodes more than 300%](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)**

Allbirds announced a deal with American Exchange Group to sell its intellectual property and other assets for $39 million in March.

CNBC • 1h ago

---

**[Opinion | Don’t Use A.I. to Do This](https://www.nytimes.com/2026/04/15/opinion/art-artificial-intelligence.html)**

The New York Times • 6h ago

---

**[Allbirds stock surged 373% after the sneaker brand pivoted to AI computing](https://qz.com/allbirds-newbird-ai-pivot-stock-041526)**

The San Francisco company is selling its footwear assets for $39 million and rebranding as NewBird AI, a GPU-as-a-Service provider

qz.com • 13m ago

---

**[Trump Just Posted An AI Image Of Himself With Jesus](https://www.forbes.com/sites/maryroeloffs/2026/04/15/trump-posts-ai-photo-with-jesus-days-after-he-was-slammed-for-blasphemy/)**

Forbes • 1h ago

---

**[This monkey selfie will protect you from AI slop](https://www.bbc.com/future/article/20260414-the-monkey-selfie-that-predicted-the-ai-age)**

What happens when something that isn't human makes art? The answer lies with this image and it will change what ends up on your screen and in your headphones forever.

BBC • 5h ago

---

**[Are factory workers training AI to replace themselves?](https://www.cnn.com/2026/04/15/world/video/are-factory-workers-training-ai-to-replace-themselves-digvid-vrtc-hnk)**

A viral video from a factory has sparked conversation both online and within the industry about whether workers are training AI to replace their jobs. CNN’s Rhea Mogul explains.

CNN • 6h ago

---

**[The AI threat undercutting the White House’s FISA push](https://www.politico.com/live-updates/2026/04/15/congress/ai-in-fisa-fight-00872629)**

Politico • 1h ago

---

**[NVIDIA Launches Ising, the World’s First Open AI Models to Accelerate the Path to Useful Quantum Computers](http://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers)**

NVIDIA today announced the world’s first family of open source quantum AI models, NVIDIA Ising, designed to help researchers and enterprises build quantum processors capable of running useful applications.

NVIDIA Newsroom • 1d ago

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)**

Reuters • 1h ago

---

**[Exclusive: AI's revolution comes with risks, Sen. McCormick says](https://www.axios.com/2026/04/15/mccormick-ai-revolution-risks-energy)**

Axios • 2h ago

---

---

## HackerNews: "ai"

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 429 • 💬 380 • 2d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 259 • 💬 397 • 1d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 209 • 💬 209 • 1d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 201 • 💬 135 • 2d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 184 • 💬 277 • 2d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 183 • 💬 100 • 21h ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 159 • 💬 101 • 9h ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 152 • 💬 34 • 1d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 149 • 💬 41 • 2d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 134 • 💬 126 • 1d ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

---

## YouTube Videos: "ai"

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 150K • 👍 12K • 💬 1K • ⏱️ 7:52 • 22h ago

---

**[&#39;It offended me&#39;: Trump supporters react to AI Jesus post](https://www.youtube.com/watch?v=WBvOpT_zrRE)**

MS NOW's Jake Traylor speaks with Trump supporters in Atlanta about the president's post of an AI image depicting him as ...

📺 MS NOW

👁️ 27K • 👍 640 • 💬 494 • ⏱️ 4:06 • 2h ago

---

**[Trump AI Video | Iran Embassy Shares Video of Jesus Punching Trump Amid AI Image Row](https://www.youtube.com/watch?v=NTGPj7WxaFQ)**

Several Iranian diplomatic accounts have launched a satirical social media offensive mocking US President Donald Trump for an ...

📺 NDTV

👁️ 15K • 👍 642 • 💬 194 • ⏱️ 2:06 • 4h ago

---

**[STOP Paying! 3 Free AI Video Generators That Actually Work](https://www.youtube.com/watch?v=ew7iQCYqpac)**

Get Unlimited Seedance 2.0 & up to 70% OFF on Higgsfield → https://higgsfield.ai/?fpr=malva Download the FREE Prompt ...

📺 Malva AI

👁️ 1K • 👍 100 • 💬 33 • ⏱️ 9:51 • 4h ago

---

**[Local AI Agents In 26 Minutes](https://www.youtube.com/watch?v=M-NTwkM3VwM)**

Sign up now at grammarly.com/tina In this video I explain the fundamentals of local AI agents! Want to get ahead in your career ...

📺 Tina Huang

👁️ 1K • 👍 216 • 💬 25 • ⏱️ 26:00 • 1h ago

---

**[Donald Trump deletes AI image of himself as Jesus after attacking Pope Leo • FRANCE 24 English](https://www.youtube.com/watch?v=D9hTiBmTrQA)**

Donald Trump launched an extraordinary attack on Pope Leo late on Sunday, also going as far as to share an AI-generated ...

📺 FRANCE 24 English

👁️ 165K • 👍 3K • 💬 920 • ⏱️ 5:11 • 1d ago

---

**[The 7 Skills You Need to Build AI Agents](https://www.youtube.com/watch?v=mtiOK2QG9Q0)**

As AI agents become more capable, the skills needed for AI jobs are shifting. Bri Kopecki breaks down the 7 skills you need to ...

📺 IBM Technology

👁️ 81K • 👍 4K • 💬 245 • ⏱️ 14:37 • 1d ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 125K • 👍 3K • 💬 797 • ⏱️ 2:10:48 • 1d ago

---

**[THE AI BUBBLE POP HAS STARTED...](https://www.youtube.com/watch?v=b5wOx2lZRM0)**

Hello guys and gals, it's me Mutahar again! This time we take another look at the AI bubble and see the cracks finally start.

📺 SomeOrdinaryGamers

👁️ 251K • 👍 13K • 💬 2K • ⏱️ 20:54 • 12h ago

---

**[PI HARD | Official Trailer 2026 | AI OR DIE Productions](https://www.youtube.com/watch?v=CNbmoVdirxw)**

Brought to you by AI OR DIE. TOOLS USED: Grok (xAI) — grok.com Freepik — freepik.com Kling AI — klingai.com Fish Audio ...

📺 AI OR DIE

👁️ 8K • 👍 694 • 💬 111 • ⏱️ 2:22 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 85,549 • ❤️ 758 • 19h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 818 • ❤️ 581 • 1d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 91,474 • ❤️ 1,227 • 3d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 12,827 • ❤️ 910 • 2h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,894,077 • ❤️ 1,922 • 4d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 134,547 • ❤️ 1,124 • 5d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 26,673 • ❤️ 273 • 3d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 445 • ❤️ 261 • 8h ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 51,148 • ❤️ 221 • 5d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 826 • 8d ago

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

▲ 158 • 💬 2 • ⭐ 59,900 • 6mo ago

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

▲ 37 • 💬 2 • ⭐ 29,660 • 1mo ago

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

⭐ 46.4k • 🔱 6.0k • 2h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 33.7k • 🔱 6.7k • 21h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 31.7k • 🔱 1.5k • 2h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 27.1k • 🔱 2.9k • 15h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.9k • 🔱 508 • 55m ago

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

⭐ 4.6k • 🔱 761 • 1d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 172 • 3h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 449 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
