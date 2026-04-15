---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-15T13:47:50.532588+00:00'
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

**Last Updated:** April 15, 2026 at 13:47 UTC  
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

10h ago

---

**[I tracked what AI agents actually do when nobody's watching. Built a tool that replays every decision.](https://www.reddit.com/r/artificial/comments/1sm261q/i_tracked_what_ai_agents_actually_do_when_nobodys/)**

Been building AI agents for about a year now and the thing that always drove me crazy is you deploy an agent, it runs for hours, and you have absolutely no idea what it did. The logs say "task complete" 47 times but did it actually do 47 different things or did it just loop the same task over and over? I had an agent burn through about $340 in API credits over a weekend because it got stuck retrying the same request. The logs showed 200 OK on every call. Everything looked fine. It just kept doing the same thing for 6 hours straight while I slept. So I built something to fix this. It's called Octopoda and its basically an observability layer that sits underneath your agents. Every memory write, every decision, every recall gets logged on a timeline. You can literally press play and watch what your agent did at 3am, step by step, like scrubbing through a video. The part that surprised me most was the loop detection. Once I could see the full timeline I realised how often agents loop without you knowing. Not obvious infinite loops, subtle stuff. An agent that rewrites the same conclusion 8 times with slightly different wording. Or one that keeps checking the same API endpoint every 30 seconds even though the data hasn't changed. Each iteration costs tokens but produces nothing new. We track 5 signals for this: write similarity, key overwrite frequency, velocity spikes, alert frequency, and goal drift. When enough signals fire together it flags it and estimates how much money the loop is costing you per hour. One user had a research agent that was wasting about $10 an hour on duplicate writes before the detection caught it. It also does auto-checkpoints. Every 25 writes it saves a snapshot automatically so if something goes wrong you can roll back to any point with one click. No more losing an entire night of agent work because something corrupted at 4am. Works with LangChain, CrewAI, AutoGen, and OpenAI Agents SDK. One line to integrate: The dashboard shows everything in real time. Agent health scores, cost per agent, shared memory between agents, full audit trail with reasoning for every decision. Honestly the most useful thing is just being able to answer "what happened overnight" without spending an hour reading logs. Anyone else dealing with the "I have no idea what my agent did" problem? Curious how other people are handling observability for autonomous workflows. Let me know if anyone wants to check it out!

3h ago

---

**[UK gov's Mythos AI tests help separate cybersecurity threat from hype](https://www.reddit.com/r/artificial/comments/1sm4277/uk_govs_mythos_ai_tests_help_separate/)**

New model is the first AI system to complete a difficult multistep infiltration challenge.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/04/uk-govs-mythos-ai-tests-help-separate-cybersecurity-threat-from-hype/) • 1h ago

---

**[Made a tool to gather logistical intelligence from satellite data](https://www.reddit.com/r/artificial/comments/1slzt9g/made_a_tool_to_gather_logistical_intelligence/)**

Hey guys, I've been workin on something new to track logistical activity near military bases and other hubs. The core problem is that Google maps isn't updated that frequently even with sub meter res and other map providers such as maxar are costly for osint analysts. But there's a solution. Drish detects moving vehicles on highways using Sentinel-2 satellite imagery. The trick is physics. Sentinel-2 captures its red, green, and blue bands about 1 second apart. Everything stationary looks normal. But a truck doing 80km/h shifts about 22 meters between those captures, which creates this very specific blue-green-red spectral smear across a few pixels. The tool finds those smears automatically, counts them, estimates speed and heading for each one, and builds volume trends over months. It runs locally as a FastAPl app with a full browser dashboard. All open source. Uses the trained random forest model from the Fisser et al 2022 paper in Remote Sensing of Environment, which is the peer reviewed science behind the detection method. GitHub: https://github.com/sparkyniner/DRISH-X-Satellite-powered-freight-intelligence-

5h ago

---

**[Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://www.reddit.com/r/artificial/comments/1slzjhh/gemini_roboticser_16_powering_realworld_robotics/)**

Gemini Robotics-ER 1.6 is a significant upgrade to the reasoning-first model that enables robots to understand their environments with unprecedented precision. By enhancing spatial reasoning and multi-view understanding, researchers are bringing a new level of autonomy to physical agents.

🔗 [Google DeepMind](https://deepmind.google/blog/gemini-robotics-er-1-6/) • 5h ago

---

**[The IRS Wants Smarter Audits. Palantir Could Help Decide Who Gets Flagged](https://www.reddit.com/r/artificial/comments/1slhx3l/the_irs_wants_smarter_audits_palantir_could_help/)**

Documents show the tax agency is testing a Palantir tool to surface “highest-value” audit and investigation targets from a maze of legacy systems.

🔗 [WIRED](https://www.wired.com/story/documents-reveal-palantir-irs-contract-fraud-clean-energy-credits/) • 18h ago

---

**[OpenAI expands its cyber defense program with GPT-5.4-Cyber for vetted researchers](https://www.reddit.com/r/artificial/comments/1slzihs/openai_expands_its_cyber_defense_program_with/)**

The company is scaling its Trusted Access for Cyber (TAC) program to thousands of verified individual defenders and hundreds of teams responsible for defending critical software. Alongside that expansion, OpenAI is releasing GPT-5.4-Cyber, a version of GPT-5.4 fine-tuned specifically for defensive cybersecurity work.

🔗 [Help Net Security](https://www.helpnetsecurity.com/2026/04/15/openai-gpt-5-4-cyber/) • 5h ago

---

**[Comparison of AI code generation: looking for insights](https://www.reddit.com/r/artificial/comments/1sm395z/comparison_of_ai_code_generation_looking_for/)**

Supposedly C3 Code won an AI coding shootout. I’d be very interested in anyone who’s got a knowledgeable critique of this. The box score (in the story) rates Claude lower than I’d personally expect but this is not my wheelhouse. Other parts of the comparison also make me wonder about the objectively of it, so anyone who is familiar with comparisons of code generation capabilities… what say you?? https://aithority.com/robots/automation/c3-ai-announces-c3-code/

2h ago

---

**[thought experiment about how people see AI - AKA - triggering a ton of people on a sub](https://www.reddit.com/r/artificial/comments/1slppzq/thought_experiment_about_how_people_see_ai_aka/)**

I posted on the neurodiversity about how I feel that AI is an ADHD accomodation, and OH BOY did people NOT like that! RUMBLE! Essentially I blieve that AI is becoming a legitimate acocmodation with people with ADHD - it allows me personally to accomplish things I have not in the past. The subreddit basically exploded on me saying that using AI is making me stupid. Which I personally find both surprising and funny. disclaimer: I did not mean to annoy people - just happened https://www.reddit.com/r/neurodiversity/comments/1slocdq/comment/og881os/

13h ago

---

**[I built Synapse AI: An open-source, DAG-based orchestrator for AI agents.](https://www.reddit.com/r/artificial/comments/1slu8m1/i_built_synapse_ai_an_opensource_dagbased/)**

Hey Everyone, For the past three months, I’ve been building an open-source orchestration platform for AI agents called Synapse AI. I started this because I found existing frameworks (like LangChain or AutoGen) either too bloated or too unpredictable for production workflows. Letting agents freely "chat" with each other often leads to infinite loops, high API costs, and debugging nightmares. I wanted strict, predictable control. The Architecture: Instead of conversational routing, Synapse AI relies on a Directed Acyclic Graph (DAG) architecture. You define the work, strictly control the hand-offs between agents, and get a completed task on the other side. Under the Hood: Tool Agnostic: Build custom tools from scratch (Python/webhooks) or instantly plug in existing Model Context Protocol (MCP) servers. Local-First Emphasis: Full native support for Ollama so you can run routing and tasks entirely locally. (It also supports Gemini, Claude, and OpenAI for the heavy lifting). CLI Integration: Just shipped a community-requested feature to connect Claude Code, Gemini CLI, Codex CLI, and GitHub Copilot CLI directly to your agents. Frictionless Setup: A 1-step installation process across macOS, Windows, and Linux. What I'm looking for: I am currently maintaining this solo and rolling it out for an early pilot phase. I would love for this community to take a look under the hood. Specifically: Code Review: I’d love brutal feedback on the DAG implementation and overall architecture. Contributors & Collaborators: If you find the project worthwhile, I am actively looking for people to team up with! Whether it's adding new LLM providers, fixing UI quirks, or improving the 1-step installer, PRs are incredibly welcome. Repo: https://github.com/naveenraj-17/synapse-ai If you bump into any bugs, please drop an issue so I can patch it. Would love to hear your thoughts!

10h ago

---

---

## Google News: "ai"

**[Opinion | Don’t Use A.I. to Do This](https://www.nytimes.com/2026/04/15/opinion/art-artificial-intelligence.html)**

The New York Times • 4h ago

---

**[Turn your best AI prompts into one-click tools in Chrome](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

blog.google • 20h ago

---

**[Allbirds announces stunning pivot from shoes to AI, stock explodes more than 200%](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)**

Allbirds announced a deal with American Exchange Group to sell its intellectual property and other assets for $39 million in March.

CNBC • 22m ago

---

**[Allbirds is turning into an AI compute provider, because of course it is](https://www.ft.com/content/a4b63cc1-2d1c-44c8-a22a-425cf0efb5cf)**

Flipping the ‘Bird

Financial Times • 42m ago

---

**[Allbirds, Inc. Executes $50M Convertible Financing Facility Agreement; Announces Expansion into AI Compute Infrastructure](https://finance.yahoo.com/markets/stocks/articles/allbirds-inc-executes-50m-convertible-120000880.html)**

Yahoo Finance • 1h ago

---

**[How to Hedge Your Portfolio Against AI Overhype](https://www.bloomberg.com/news/newsletters/2026-04-15/how-to-hedge-your-portfolio-against-ai-overhype)**

Bloomberg.com • 32m ago

---

**[The AI threat undercutting the White House’s FISA push](https://www.politico.com/live-updates/2026/04/15/congress/ai-in-fisa-fight-00872629)**

Politico • 3m ago

---

**[This monkey selfie will protect you from AI slop](https://www.bbc.com/future/article/20260414-the-monkey-selfie-that-predicted-the-ai-age)**

What happens when something that isn't human makes art? The answer lies with this image and it will change what ends up on your screen and in your headphones forever.

BBC • 4h ago

---

**[Exclusive: AI's revolution comes with risks, Sen. McCormick says](https://www.axios.com/2026/04/15/mccormick-ai-revolution-risks-energy)**

Axios • 50m ago

---

**[Are factory workers training AI to replace themselves?](https://www.cnn.com/2026/04/15/world/video/are-factory-workers-training-ai-to-replace-themselves-digvid-vrtc-hnk)**

A viral video from a factory has sparked conversation both online and within the industry about whether workers are training AI to replace their jobs. CNN’s Rhea Mogul explains.

CNN • 5h ago

---

---

## HackerNews: "ai"

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 428 • 💬 380 • 2d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 259 • 💬 396 • 1d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 208 • 💬 206 • 1d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

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

⬆️ 181 • 💬 99 • 20h ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

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

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 122 • 💬 88 • 8h ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

---

## YouTube Videos: "ai"

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 135K • 👍 11K • 💬 1K • ⏱️ 7:52 • 21h ago

---

**[China&#39;s NEW Autonomous AI DESTROYS OpenAI?](https://www.youtube.com/watch?v=kdSEsM5gCEY)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 3K • 👍 45 • 💬 5 • ⏱️ 8:36 • 19h ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 114K • 👍 3K • 💬 743 • ⏱️ 2:10:48 • 22h ago

---

**[The 7 Skills You Need to Build AI Agents](https://www.youtube.com/watch?v=mtiOK2QG9Q0)**

As AI agents become more capable, the skills needed for AI jobs are shifting. Bri Kopecki breaks down the 7 skills you need to ...

📺 IBM Technology

👁️ 71K • 👍 4K • 💬 186 • ⏱️ 14:37 • 1d ago

---

**[The Banks Know Something Terrifying About AI — And They&#39;re Not Telling You](https://www.youtube.com/watch?v=z22HnACwl7k)**

FULL EPISODE: https://youtube.com/live/Q_QHDxdeFQY The government just called an emergency meeting. Every major bank ...

📺 BTC Sessions

👁️ 7K • 👍 214 • 💬 408 • ⏱️ 27:15 • 2d ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 20K • 👍 640 • 💬 153 • ⏱️ 1:27:18 • 2d ago

---

**[Watch it before it gets BANNED/ DELETED! #ai #dataprivacy #metarayban #humanoidrobot #dependence](https://www.youtube.com/watch?v=4OUS7zXmpWk)**

AI, Data Privacy, Meta Ray-Ban, Glasses, Humanoid, Robot, Training, Job displacement, Future of AI, Tech Monopoly, Digital ...

📺 bluntboard_

👁️ 39K • 👍 2K • 💬 49 • ⏱️ 1:06 • 1d ago

---

**[The AI Job APOCALYPSE](https://www.youtube.com/watch?v=pU2prVifda8)**

Yo can we not do this Thanks for watching :) my ig: https://instagram.com/itsraylikesunshine.

📺 RayLikeSunshine

👁️ 165K • 👍 12K • 💬 1K • ⏱️ 35:49 • 1d ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 184K • 👍 4K • 💬 265 • ⏱️ 6:26 • 2d ago

---

**[Trump AI Jesus Scandal is Crazier Than You Think](https://www.youtube.com/watch?v=RahSlovHhCo)**

Watch this after: https://youtu.be/wKcbkiD4W_0 Go to https://HelloFresh.com/defranco10fm now to get 10 free meals + free ...

📺 Philip DeFranco

👁️ 640K • 👍 24K • 💬 3K • ⏱️ 30:29 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 85,549 • ❤️ 746 • 18h ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 91,474 • ❤️ 1,218 • 3d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 12,827 • ❤️ 906 • 7d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 818 • ❤️ 566 • 1d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,894,077 • ❤️ 1,915 • 4d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 134,547 • ❤️ 1,119 • 5d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 26,673 • ❤️ 265 • 3d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 445 • ❤️ 249 • 7h ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 51,148 • ❤️ 219 • 5d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 821 • 8d ago

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

▲ 43 • 💬 2 • ⭐ 50,593 • 15mo ago

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

▲ 51 • 💬 1 • ⭐ 76,614 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

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

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 23,737 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 46.3k • 🔱 6.0k • 1h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 33.6k • 🔱 6.6k • 20h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 31.3k • 🔱 1.5k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 27.0k • 🔱 2.9k • 14h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.9k • 🔱 502 • 2h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.7k • 🔱 1.1k • 20d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 172 • 3h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.5k • 🔱 755 • 1d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 449 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
