---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-15T05:25:20.604867+00:00'
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

**Last Updated:** April 15, 2026 at 05:25 UTC  
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

2h ago

---

**[The IRS Wants Smarter Audits. Palantir Could Help Decide Who Gets Flagged](https://www.reddit.com/r/artificial/comments/1slhx3l/the_irs_wants_smarter_audits_palantir_could_help/)**

Documents show the tax agency is testing a Palantir tool to surface “highest-value” audit and investigation targets from a maze of legacy systems.

🔗 [WIRED](https://www.wired.com/story/documents-reveal-palantir-irs-contract-fraud-clean-energy-credits/) • 10h ago

---

**[I built Synapse AI: An open-source, DAG-based orchestrator for AI agents.](https://www.reddit.com/r/artificial/comments/1slu8m1/i_built_synapse_ai_an_opensource_dagbased/)**

Hey Everyone, For the past three months, I’ve been building an open-source orchestration platform for AI agents called Synapse AI. I started this because I found existing frameworks (like LangChain or AutoGen) either too bloated or too unpredictable for production workflows. Letting agents freely "chat" with each other often leads to infinite loops, high API costs, and debugging nightmares. I wanted strict, predictable control. The Architecture: Instead of conversational routing, Synapse AI relies on a Directed Acyclic Graph (DAG) architecture. You define the work, strictly control the hand-offs between agents, and get a completed task on the other side. Under the Hood: Tool Agnostic: Build custom tools from scratch (Python/webhooks) or instantly plug in existing Model Context Protocol (MCP) servers. Local-First Emphasis: Full native support for Ollama so you can run routing and tasks entirely locally. (It also supports Gemini, Claude, and OpenAI for the heavy lifting). CLI Integration: Just shipped a community-requested feature to connect Claude Code, Gemini CLI, Codex CLI, and GitHub Copilot CLI directly to your agents. Frictionless Setup: A 1-step installation process across macOS, Windows, and Linux. What I'm looking for: I am currently maintaining this solo and rolling it out for an early pilot phase. I would love for this community to take a look under the hood. Specifically: Code Review: I’d love brutal feedback on the DAG implementation and overall architecture. Contributors & Collaborators: If you find the project worthwhile, I am actively looking for people to team up with! Whether it's adding new LLM providers, fixing UI quirks, or improving the 1-step installer, PRs are incredibly welcome. Repo: https://github.com/naveenraj-17/synapse-ai If you bump into any bugs, please drop an issue so I can patch it. Would love to hear your thoughts!

2h ago

---

**[Claude Code Degradation: An interesting and novel find](https://www.reddit.com/r/artificial/comments/1slhln5/claude_code_degradation_an_interesting_and_novel/)**

As many of you have likely seen, the Claude Code community newswire has been ablaze with Claude Code being quite degraded lately, starting in February, and continuing to this day. Curious to understand if there was any "signal" on the wire when using Claude Code, I fired up my old friend WireShark and a --tls-keylog environment flag. Call it a man-in-the-middle attack on my own traffic. The captured TLS network traffic reveals the system prompts, system variables, and various other bits of telemetry The interesting part? A signature routing block that binds the session to a cloud instance with an effort level parameter, named Numbat. Mine, specifically, was numbat-v7-efforts-15-20-40-ab-prod8 So, it would appear that the backend running my instance is tied to an efforts-15-20-40 level. Is this conclusive? Not definitively, since only Antrhopic could tell us what that parameter actually means in production. Side note, a Numbat is an endangered critter that eats Ants in Austrialia :) If the "Numbat" eats the "Ants" (Anthropic), and Numbat is the engine that controls "Effort," the name itself could imply a "cost-eater" or an optimizer designed to reduce the model's footprint, likely in favor of project Glasswing efforts with Mythos Follow for more insights on Claude Code Numabt-v7-Efforts-15-20-40

10h ago

---

**[Lumen's CEO warns that AI bots now rule the internet](https://www.reddit.com/r/artificial/comments/1slq61s/lumens_ceo_warns_that_ai_bots_now_rule_the/)**

Johnson warned that companies must urgently rethink their strategies as autonomous workers flood the web at unpredictable speeds and volumes.

🔗 [Happy Mag](https://happymag.tv/lumens-ceo-warns-ai-bots-rule-internet/) • 5h ago

---

**[thought experiment about how people see AI - AKA - triggering a ton of people on a sub](https://www.reddit.com/r/artificial/comments/1slppzq/thought_experiment_about_how_people_see_ai_aka/)**

I posted on the neurodiversity about how I feel that AI is an ADHD accomodation, and OH BOY did people NOT like that! RUMBLE! Essentially I blieve that AI is becoming a legitimate acocmodation with people with ADHD - it allows me personally to accomplish things I have not in the past. The subreddit basically exploded on me saying that using AI is making me stupid. Which I personally find both surprising and funny. disclaimer: I did not mean to annoy people - just happened https://www.reddit.com/r/neurodiversity/comments/1slocdq/comment/og881os/

5h ago

---

**[A New AI Tool Could Transform How We Diagnose Genetic Diseases](https://www.reddit.com/r/artificial/comments/1sljo6z/a_new_ai_tool_could_transform_how_we_diagnose/)**

Researchers say a new AI system can identify disease-causing mutations and explain their biological effects, potentially changing how genetic disorders are diagnosed.

🔗 [TIME](https://time.com/article/2026/04/14/ai-disease-genetic-mayo-clinic-goodfire/?utm_source=reddit&utm_medium=social&utm_campaign=editorial) • 9h ago

---

**[I think this could be helpful for many.](https://www.reddit.com/r/artificial/comments/1slvogy/i_think_this_could_be_helpful_for_many/)**

All the AI engines on dating https://claude-cheeky-guide.lovable.app

1h ago

---

**[How Do You Use AI in Everyday Life?](https://www.reddit.com/r/artificial/comments/1slvfjc/how_do_you_use_ai_in_everyday_life/)**

Hi everyone! We’re conducting a short academic survey about how people use AI in everyday life and how they view the boundary between humans and AI. We’re interested in topics such as trust, control, uncertainty, dependence, emotional connection, and data use in AI interactions. If you use AI tools for things like study, work, decision-making, or daily support, we’d really appreciate your input. All responses are anonymous and will be used for academic research only. Thanks so much for your time! Survey link: https://docs.google.com/forms/d/e/1FAIpQLSfqnjs5EzI58Cj1plSFzFE1JBCeGHzE1mjsewtVZpR4l7Nhzw/viewform?usp=dialog

1h ago

---

**[Why don't LLMs track time in their conversations?](https://www.reddit.com/r/artificial/comments/1sky7h9/why_dont_llms_track_time_in_their_conversations/)**

Question for everyone: Why do you think LLMs like Claude don't use timestamp data within conversations to build temporal awareness? Like, it seems straightforward to track how long you've been talking, notice when you're looping on the same idea for hours, and suggest pivoting. Or acknowledge that conversation fatigue might be setting in. From a UX perspective, I'd expect this would make the tool way more engaging Is there a technical limitation I'm missing, or is it more of a design choice? Thanks! EDIT: Thanks all for the discussion! I got some pretty interesting insights!

1d ago

---

---

## Google News: "ai"

**[Turn your best AI prompts into one-click tools in Chrome](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

blog.google • 12h ago

---

**[How to Use Google Chrome’s New AI-Powered ‘Skills’](https://www.wired.com/story/how-to-use-google-chrome-ai-powered-skills/)**

The premade Skills available through the Gemini sidebar in Chrome include ways to maximize protein in recipes or summarize YouTube videos.

WIRED • 12h ago

---

**[Google adds AI Skills to Chrome to help you save favorite workflows](https://techcrunch.com/2026/04/14/google-adds-ai-skills-to-chrome-to-help-you-save-favorite-workflows/)**

Google is adding “Skills” to Chrome, letting users save and reuse AI prompts across websites. The feature builds on Gemini’s browser integration.

TechCrunch • 12h ago

---

**[Bosses say AI boosts productivity – workers say they’re drowning in ‘workslop’](https://www.theguardian.com/technology/2026/apr/14/ai-productivity-workplace-errors)**

Workslop refers to AI-generated work that seems polished but is flawed and in need of heavy corrections

The Guardian • 8h ago

---

**[Chip giant ASML raises 2026 guidance as AI semiconductor demand stays strong](https://www.cnbc.com/2026/04/15/asml-q1-2026-earnings-report.html)**

ASML beat first-quarter revenue and profit expectations and raised its sales guidance for 2026.

CNBC • 13m ago

---

**[NVIDIA Launches Ising, the World’s First Open AI Models to Accelerate the Path to Useful Quantum Computers](http://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers)**

NVIDIA today announced the world’s first family of open source quantum AI models, NVIDIA Ising, designed to help researchers and enterprises build quantum processors capable of running useful applications.

NVIDIA Newsroom • 15h ago

---

**[D-Wave CEO says Nvidia should be 'shaking in their boots' as quantum computing battles AI GPUs](https://finance.yahoo.com/news/d-wave-ceo-says-nvidia-should-be-shaking-in-their-boots-as-quantum-computing-battles-ai-gpus-180249321.html)**

D-Wave touts massive energy efficiency gains over Nvidia as World Quantum Day sparks a sector-wide rally.

Yahoo Finance • 11h ago

---

**[Nvidia New AI Models Spark Rally in Quantum Computing Stocks](https://www.bloomberg.com/news/articles/2026-04-15/nvidia-new-ai-models-spark-rally-in-quantum-computing-stocks)**

Bloomberg.com • 1h ago

---

**[Cheap Drones Complicate the Gulf’s AI Boom](https://foreignpolicy.com/2026/04/15/cheap-drones-complicate-gulf-ai-boom/)**

Protection is becoming inseparable from access.

Foreign Policy • 1h ago

---

**[Meta extends custom chips deal with Broadcom to power AI ambitions](https://finance.yahoo.com/sectors/technology/articles/meta-extends-custom-chips-deal-with-broadcom-to-power-ai-ambitions-211850406.html)**

Meta will work with chip designer Broadcom to produce several generations of custom artificial intelligence processors under an expanded deal ‌as the social media giant races to build out the computing ‌capacity needed to power AI features across its apps.  Tuesday's announcement extends the tie-up until 2029 and ​includes an initial commitment of over one gigawatt of computing capacity, enough to power roughly 750,000 U.S. homes on average.  As part of the deal, Broadcom CEO Hock Tan would leave Meta's board and move to an advisory role on its custom chip ‌strategy, the companies said ⁠in a joint statement.

Yahoo Finance • 8h ago

---

---

## HackerNews: "ai"

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 427 • 💬 377 • 2d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 346 • 💬 626 • 2d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 255 • 💬 393 • 1d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 203 • 💬 200 • 20h ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 201 • 💬 135 • 2d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 183 • 💬 267 • 1d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 149 • 💬 41 • 2d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 148 • 💬 33 • 1d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 143 • 💬 63 • 12h ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 133 • 💬 126 • 1d ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

---

## YouTube Videos: "ai"

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 107K • 👍 9K • 💬 961 • ⏱️ 7:52 • 12h ago

---

**[A.I. Official Trailer (2026) Josh Stamberg](https://www.youtube.com/watch?v=W3HTujL75DI)**

A.I. Official Trailer (2026) Josh Stamberg, Ian Sharkey Writer/Director Lanxuan Xie © 2026 - TriCoast Entertainment.

📺 ONE Media

👁️ 21K • 👍 357 • 💬 49 • ⏱️ 2:04 • 13h ago

---

**[I Used AI to Check Trump&#39;s MENTAL HEALTH. The Results Are INSANE](https://www.youtube.com/watch?v=CF_BKce0XSI)**

Head over to my sponsor Venice AI — use my link https://venice.ai/iaskai and code 'IAskAI' to get 20% off a Pro plan.

📺 I Ask AI

👁️ 34K • 👍 3K • 💬 188 • ⏱️ 17:37 • 1d ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 91K • 👍 3K • 💬 627 • ⏱️ 2:10:48 • 14h ago

---

**[China Just Dropped 3 FREE AI Video Generators (No Sign-Up, 100% FREE)](https://www.youtube.com/watch?v=nrQl2rHx6ok)**

Join my Discord community https://discord.gg/QC2YEk7P7n China just dropped 3 FREE AI video generators — no sign-up, ...

📺 Becky the Ai Girl

👁️ 7K • 👍 511 • 💬 35 • ⏱️ 10:36 • 11h ago

---

**[she says AI stole the photo](https://www.youtube.com/watch?v=onQX-mQtaac)**

Go to http://www.squarespace.com/swellentertainment to get a free trial and 10% off your first purchase of a website or domain.

📺 Swell Entertainment

👁️ 57K • 👍 4K • 💬 337 • ⏱️ 27:01 • 12h ago

---

**[China’s New Self Improving Open AI Beats OpenAI](https://www.youtube.com/watch?v=KJ34SHi9CB4)**

MiniMax just open-sourced M2.7, a new self-improving AI model built for coding, software engineering, office work, and ...

📺 AI Revolution

👁️ 35K • 👍 845 • 💬 50 • ⏱️ 14:54 • 2d ago

---

**[Watch it before it gets BANNED/ DELETED! #ai #dataprivacy #metarayban #humanoidrobot #dependence](https://www.youtube.com/watch?v=4OUS7zXmpWk)**

AI, Data Privacy, Meta Ray-Ban, Glasses, Humanoid, Robot, Training, Job displacement, Future of AI, Tech Monopoly, Digital ...

📺 bluntboard_

👁️ 13K • 👍 751 • 💬 30 • ⏱️ 1:06 • 16h ago

---

**[The AI Job APOCALYPSE](https://www.youtube.com/watch?v=pU2prVifda8)**

Yo can we not do this Thanks for watching :) my ig: https://instagram.com/itsraylikesunshine.

📺 RayLikeSunshine

👁️ 159K • 👍 12K • 💬 1K • ⏱️ 35:49 • 1d ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 18K • 👍 606 • 💬 142 • ⏱️ 1:27:18 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 84,784 • ❤️ 1,206 • 3d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 43,645 • ❤️ 727 • 10h ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 10,899 • ❤️ 890 • 6d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,640,636 • ❤️ 1,902 • 4d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 723 • ❤️ 527 • 18h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 117,491 • ❤️ 1,108 • 4d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 12,687 • ❤️ 239 • 2d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 815 • 8d ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 41,945 • ❤️ 216 • 4d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 530,898 • ❤️ 575 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 15 • 💬 1 • ⭐ 17,754 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,282 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 164 • 💬 9 • ⭐ 39,521 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 50,463 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 157 • 💬 2 • ⭐ 59,900 • 6mo ago

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

▲ 52 • 💬 2 • ⭐ 53,042 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 37 • 💬 2 • ⭐ 29,660 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 23,737 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,223 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 46.0k • 🔱 6.0k • 1h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 33.4k • 🔱 6.6k • 11h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 30.3k • 🔱 1.4k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 26.6k • 🔱 2.9k • 5h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.8k • 🔱 495 • 36m ago

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

⭐ 4.6k • 🔱 171 • 5h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 447 • 6d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.4k • 🔱 729 • 22h ago

---

---

*Generated by PeekDeck - A glance is all you need*
