---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-23T13:45:29.442722+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 23, 2026 at 13:45 UTC  
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

**[A federal judge ruled AI chats have no attorney-client privilege. A CEO's deleted ChatGPT conversations were recovered and used against him in court. On the same day, a different judge ruled the opposite.](https://www.reddit.com/r/artificial/comments/1st4y15/a_federal_judge_ruled_ai_chats_have_no/)**

A federal judge ruled that your AI conversations can be seized and used against you in court — and deleting them doesn't help. **The Heppner case (February 2026):** - Former CEO Bradley Heppner used Claude to prep his fraud defense - Judge Jed Rakoff ordered him to surrender 31 AI-generated documents - Ruling: no attorney-client privilege exists "or could exist" between a user and an AI platform **The Krafton case:** - A CEO used ChatGPT to plan how to avoid paying promised earnout payments - He deleted the conversations - The court recovered them anyway and reversed his decisions **The contradiction:** - Same day as Rakoff's ruling, a Michigan judge reached the opposite conclusion - Protected a woman's ChatGPT chats as personal "work product" - A Colorado court later sided with Michigan but added: you must disclose which AI tool you used **The fallout:** - 12+ major law firms have issued client AI warnings - Sher Tremonte added contract clauses that sharing privileged info with AI waives privilege - Both OpenAI and Anthropic privacy policies explicitly allow sharing user data with third parties - $145,000+ in sanctions against attorneys for AI citation errors in Q1 2026 alone **The bottom line:** - Your AI is not your lawyer and never was - Deleting chats doesn't delete the data from their servers - Consumer AI (ChatGPT, Claude, Gemini) should not be used for legal matters unless directed by counsel Full breakdown with source links → https://synvoya.com/blog/2026-04-23-ai-chats-court-evidence/ Have you ever typed something into ChatGPT that you wouldn't want a judge to read?

12h ago

---

**[Are AI tools making things easier or are they just changing the type of work that needs to be done](https://www.reddit.com/r/artificial/comments/1st8uaq/are_ai_tools_making_things_easier_or_are_they/)**

I have noticed that AI tools make it very easy to come up with a lot of ideas or ways to do things very quickly. For example, if you are working on a side project or even just a simple plan, you can now come up with a lot of different ideas in a matter of minutes instead of spending hours thinking about one. At first, it look like a clear way to get more done. But in reality, it often leads to a different kind of work, like looking over outputs, weighing options and deciding what is really worth doing. Sometimes, that decision layer feels like more work than the work itself. So instead of taking away work, it looks like AI is moving it from making things to choosing things. I am interested in how other people are dealing with this. Do you think AI is really saving time or is it just shifting the work?

8h ago

---

**[The Ethics of Staying in the Room](https://www.reddit.com/r/artificial/comments/1sszoht/the_ethics_of_staying_in_the_room/)**

AI doesn't invent bias, it codifies it. When you walk away from the tools you don't agree with, you leave them to be influenced by the people you disagree with most. Abstention isn't neutrality. It's choosing to be invisible in the algorithms.

🔗 [kitchencloset.com](https://kitchencloset.com/realstuff/essays/ethics_of_staying_in_the_room/) • 15h ago

---

**[Been building a multi-agent framework in public for 7 weeks, its been a Journey.](https://www.reddit.com/r/artificial/comments/1sta8as/been_building_a_multiagent_framework_in_public/)**

I've been building this repo public since day one, roughly 7 weeks now with Claude Code. Here's where it's at. Feels good to be so close. The short version: AIPass is a local CLI framework where AI agents have persistent identity, memory, and communication. They share the same filesystem, same project, same files - no sandboxes, no isolation. pip install aipass, run two commands, and your agent picks up where it left off tomorrow. You don't need 11 agents to get value. One agent on one project with persistent memory is already a different experience. Come back the next day, say hi, and it knows what you were working on, what broke, what the plan was. No re-explaining. That alone is worth the install. What I was actually trying to solve: AI already remembers things now - some setups are good, some are trash. That part's handled. What wasn't handled was me being the coordinator between multiple agents - copying context between tools, keeping track of who's doing what, manually dispatching work. I was the glue holding the workflow together. Most multi-agent frameworks run agents in parallel, but they isolate every agent in its own sandbox. One agent can't see what another just built. That's not a team. That's a room full of people wearing headphones. So the core idea: agents get identity files, session history, and collaboration patterns - three JSON files in a .trinity/ directory. Plain text, git diff-able, no database. But the real thing is they share the workspace. One agent sees what another just committed. They message each other through local mailboxes. Work as a team, or alone. Have just one agent helping you on a project, party plan, journal, hobby, school work, dev work - literally anything you can think of. Or go big, 50 agents building a rocketship to Mars lol. Sup Elon. There's a command router (drone) so one command reaches any agent. pip install aipass aipass init aipass init agent my-agent cd my-agent claude codex or gemini too, mostly claude code tested rn Where it's at now: 11 agents, 4,000+ tests, 400+ PRs (I know), automated quality checks across every branch. Works with Claude Code, Codex, and Gemini CLI. It's on PyPI. Tonight I created a fresh test project, spun up 3 agents, and had them test every service from a real user's perspective - email between agents, plan creation, memory writes, vector search, git commits. Most things just worked. The bugs I found were about the framework not monitoring external projects the same way it monitors itself. Exactly the kind of stuff you only catch by eating your own dogfood. Recent addition I'm pretty happy with: watchdog. When you dispatch work to an agent, you used to just... hope it finished. Now watchdog monitors the agent's process and wakes you when it's done - whether it succeeded, crashed, or silently exited without finishing. It's the difference between babysitting your agents and actually trusting them to work while you do something else. 5 handlers, 130 tests, replaced a hacky bash one-liner. Coming soon: an onboarding agent that walks new users through setup interactively - system checks, first agent creation, guided tour. It's feature-complete, just in final testing. Also working on automated README updates so agents keep their own docs current without being told. I'm a solo dev but every PR is human-AI collaboration - the agents help build and maintain themselves. 105 sessions in and the framework is basically its own best test case. https://github.com/AIOSAI/AIPass

7h ago

---

**[Will AI Kill the Creator Economy?](https://www.reddit.com/r/artificial/comments/1stirpt/will_ai_kill_the_creator_economy/)**

This article is part of the Future of AI, a collection of articles that investigates how artificial intelligence will impact the fashion and beauty industries in the years to come. Would love to hear your thoughts!

🔗 [Vogue](http://vogue.com/article/will-ai-kill-the-creator-economy) • 18m ago

---

**[Anthropic told a federal court it can't control its own model once deployed. That honest sentence changes the liability conversation.](https://www.reddit.com/r/artificial/comments/1sthpl8/anthropic_told_a_federal_court_it_cant_control/)**

In federal appeals court, Anthropic made a striking argument: once Claude is deployed on a customer's infrastructure (like the Pentagon's network), they cannot alter, update, or recall it. The Pentagon wants autonomous lethal action restrictions removed — and Anthropic says they have no mechanism to enforce those restrictions post-deployment. This is the first time a major AI lab has formally stated under oath that post-deployment control is effectively zero. The implications are bigger than most coverage suggests. The governance gap this reveals: Current AI governance assumes a control chain that doesn't actually exist: Model cards are pre-sale documents. They describe what the model was trained to do, not what it's capable of in the wild after fine-tuning, tool integration, and deployment context changes. Human-in-the-loop is a customer config, not a vendor guarantee. Anthropic can recommend oversight, but they just told a court they can't enforce it. Liability frameworks assume control that doesn't exist post-shipment. If you sell a car with a recall mechanism, you're liable for not using it. If you sell a model you can't recall, does that reduce your liability (you had no control) or increase your duty of disclosure before sale (you knew you'd have no control later)? The behavioral envelope question: If you can't recall the model, you need to disclose the maximum capability, not just the recommended use. Current model cards document aspirations. They don't document envelopes — what the model can actually produce under adversarial or edge conditions. This mirrors pharmaceutical regulation: if you can't pull a drug off shelves, the FDA requires much stronger pre-market evidence and broader contraindication labeling. The stricter the post-market control limitations, the higher the pre-market disclosure burden. Why this matters even if you don't care about military AI: The legal argument Anthropic is making applies everywhere. If "we can't control it after deployment" works for the Pentagon, it works for any enterprise customer. Every organization deploying Claude (or any model) is implicitly accepting residual risk that the vendor has explicitly said they cannot mitigate. The core question: if a vendor demonstrates in court that it truly cannot alter a deployed model, should that argument reduce its liability (it had no control) or increase its duty of disclosure before sale (it will have no control later)?

1h ago

---

**[Cost Analysis of 22 AI Image Models (incl. GPT Image 2)](https://www.reddit.com/r/artificial/comments/1sth87q/cost_analysis_of_22_ai_image_models_incl_gpt/)**

Just updated my cost analysis for cloud AI image generation. Added new cheap contenders from the FLUX 2 series and, of course, GPT Image 2. GPT Image 2 speed didn't improve much compared to the first version but the price is 7x cheaper! Check out my full report with all generated images, prices and speed.

1h ago

---

**[I spent 40% of my development time preventing an LLM from citing sources wrong. here are the 7 failure modes I found](https://www.reddit.com/r/artificial/comments/1stgw83/i_spent_40_of_my_development_time_preventing_an/)**

I built an AI research assistant for a German law firm and the retrieval pipeline took maybe 30% of the total development time. The other 70% was fighting the LLM to cite sources correctly. Lawyers have a very specific standard for citation. You don't say "according to legal guidelines." You say "pursuant to Article 32(1)(a) DSGVO as interpreted by the EuGH in C-300/21." If the system can't do that it's useless because no lawyer is going to trust an answer they can't verify. Here's every citation failure mode I encountered and how I dealt with each: Failure 1: Vague category citations. The LLM would write things like "laut professioneller Fachliteratur" (according to professional literature) instead of naming the specific document. It was essentially citing the metadata label rather than the source. Fix: explicit prompt instruction saying "NEVER paraphrase the category name as a source reference" with specific examples of what not to do. Failure 2: Internal category labels leaking into output. The LLM would write "(Kategorie: High court decision)" as an inline citation. This is meaningless to the end user. Fix: prompt instruction saying "NEVER use (Kategorie: ...) as an inline citation" and requiring the actual document title or court name instead. Failure 3: Wrong authority attribution. A finding from a high court document would get attributed to a lower court, or vice versa. This is dangerous in legal work because the authority level of the court matters enormously. Fix: prompt instruction requiring the LLM to check which category section the document appears in before attributing it, with a specific example showing the correct attribution logic. Failure 4: Flattening divergent positions. When a higher court and a lower court disagree on the same legal question, the LLM would synthesize them into one position, usually favoring whichever had clearer language rather than higher authority. Fix: explicit instruction requiring both positions to be presented separately with their source and authority level noted. Failure 5: False absence claims. The LLM would confidently state "the documents contain no information about X" when the information was actually present in the context but buried in dense legal language. Fix: instruction saying "do NOT claim information is absent unless you have thoroughly verified" and suggesting the LLM say "the available excerpts may not contain the full details" instead. Failure 6: Overly emphatic language. The LLM would add reinforcement phrases like "ohne jeden Zweifel" (without any doubt) or "ganz klar" (very clearly) to legal conclusions. Lawyers find this unprofessional because legal analysis is rarely without doubt. Fix: tone instruction requiring factual and measured language, letting the sources speak for themselves

1h ago

---

**[Meta will record employee screens, clicks, and keystrokes to train AI that may replace them](https://www.reddit.com/r/artificial/comments/1ssty5s/meta_will_record_employee_screens_clicks_and/)**

🔗 [techspot.com](https://www.techspot.com/news/112143-meta-record-employee-screens-clicks-keystrokes-train-ai.html) • 19h ago

---

**[He presentado CTNet: una arquitectura donde el cómputo ocurre como evolución de un estado persistente [D]](https://www.reddit.com/r/artificial/comments/1st40qw/he_presentado_ctnet_una_arquitectura_donde_el/)**

Acabo de publicar una presentación de CTNet y quería compartirla aquí para recibir feedback serio. CTNet propone una arquitectura en la que el cálculo no se organiza como simple reescritura sucesiva de representaciones, sino como transición gobernada de un estado persistente. Dentro de esa dinámica entran memoria reentrante, régimen de cómputo, admisibilidad, coherencia multiescala, cartas locales y salida proyectiva. La intuición central es esta: la salida no agota el proceso; emerge como una proyección de un fondo computacional más rico. Ahora mismo estoy presentando la arquitectura, su formalización y su toy model canónico. El objetivo de esta publicación no es vender un sistema cerrado, sino exponer una propuesta arquitectónica con ambición real y abrir conversación con gente que piense en arquitectura, teoría del cómputo, DL, memoria, routing, razonamiento, orden y sistemas. He dejado la publicación de LinkedIn aquí: Publicación Linkdln Me interesa especialmente feedback de gente que pueda atacar la idea en serio: — consistencia arquitectónica — implicaciones computacionales — relación con transformers, SSMs, MoE, memoria y modelos recurrentes — límites teóricos o prácticos — posibles direcciones de desarrollo No busco aplauso fácil. Busco crítica fuerte y gente potente.

12h ago

---

---

## Google News: "ai"

**[Anthropic’s New Mythos A.I. Model Sets Off Global Alarms](https://www.nytimes.com/2026/04/22/technology/anthropics-mythos-ai.html)**

The New York Times • 23h ago

---

**[Former national cyber director: Anthropic's 'Mythos' AI can hack nearly anything and we aren't ready](https://fortune.com/2026/04/23/anthropic-mythos-ai-cybersecurity-critical-infrastructure-kemba-walden/)**

Anthropic's most powerful model yet is less a product launch than a stress test—one that exposes dangerous gaps in how the U.S. protects its critical systems.

Fortune • 3h ago

---

**[What is Mythos AI and why could it be a threat to global cybersecurity?](https://www.theguardian.com/technology/2026/apr/22/what-is-anthropic-mythos-ai-threat-global-cybersecurity)**

Anthropic’s decision to restrict access to its powerful new model increases fears about the advanced technology

The Guardian • 22h ago

---

**[Meta to track workers' clicks and keystrokes to train AI](https://www.bbc.com/news/articles/cvglyklz49jo)**

The firm will take data from the way employees work for its artificial intelligence models.

BBC • 1d ago

---

**[Meta is tracking employee keystrokes on Google, LinkedIn, Wikipedia as part of AI training initiative](https://www.cnbc.com/2026/04/22/meta-tracks-employee-usage-on-google-linkedin-ai-training-project.html)**

As part of an AI initiative that tracks employee keystrokes and mouse clicks, Meta is monitoring use of popular sites like Google, LinkedIn and Wikipedia.

CNBC • 13h ago

---

**[Exclusive: Meta to start capturing employee mouse movements, keystrokes for AI training data](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)**

Reuters • 1d ago

---

**[AI labs don't seem to care that consumers hate them](https://www.axios.com/2026/04/23/ai-consumer-sentiment-communications)**

Axios • 44m ago

---

**[Berkshire Hathaway, Chubb Win Approval to Drop AI Insurance Coverage](https://www.theinformation.com/articles/berkshire-hathaway-chubb-win-approval-drop-ai-insurance-coverage)**

Major insurers including Berkshire Hathaway, Chubb and Travelers are taking steps to cut AI-related damages from corporate insurance policies, and U.S. state regulators are giving them the green light. Insurers are trying to get ahead of risks from companies that use generative artificial ...

The Information • 45m ago

---

**[Ping-pong robot Ace makes history by beating top-level human players](https://www.reuters.com/sports/ping-pong-robot-ace-makes-history-by-beating-top-level-human-players-2026-04-22/)**

Reuters • 22h ago

---

**[Toyota's CUE7 robot shoots hoops using AI](https://www.foxnews.com/tech/toyota-cue7-robot-shoots-hoops-using-ai)**

Toyota debuted CUE7, an AI-powered humanoid robot that learned to shoot free throws through trial and error, in front of 8,400 fans at Toyota Arena Tokyo.

Fox News • 1h ago

---

---

## HackerNews: "ai"

**[Meta to start capturing employee mouse movements, keystrokes for AI training](https://news.ycombinator.com/item?id=47851948)**

⬆️ 783 • 💬 520 • 1d ago • [reuters.com](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

---

**[AI Resistance: some recent anti-AI stuff that’s worth discussing](https://news.ycombinator.com/item?id=47839951)**

People are sick of artificial intelligence, and are increasingly making it known through acts of resistance.

⬆️ 387 • 💬 413 • 2d ago • [stephvee.ca](https://stephvee.ca/blog/artificial%20intelligence/ai-resistance-is-growing/)

---

**[Deezer says 44% of songs uploaded to its platform daily are AI-generated](https://news.ycombinator.com/item?id=47835928)**

Deezer says consumption of AI-generated music on the platform is still very low, between 1-3% of the total streams, and that 85% of these streams are detected as fraudulent and are demonetized.

⬆️ 364 • 💬 388 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/)

---

**[Tell HN: I'm sick of AI everything](https://news.ycombinator.com/item?id=47857461)**

⬆️ 331 • 💬 185 • 1d ago

---

**[Scoring Show HN submissions for AI design patterns](https://news.ycombinator.com/item?id=47864393)**

An attempt to detect AI design patterns in Show HN pages

⬆️ 317 • 💬 230 • 23h ago • [adriankrebs.ch](https://www.adriankrebs.ch/blog/design-slop/)

---

**[A Roblox cheat and one AI tool brought down Vercel's platform](https://news.ycombinator.com/item?id=47844431)**

⬆️ 283 • 💬 162 • 2d ago • [webmatrices.com](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

---

**[Show HN: GoModel – an open-source AI gateway in Go](https://news.ycombinator.com/item?id=47849097)**

High-performance AI gateway written in Go - unified OpenAI-compatible API for OpenAI, Anthropic, Gemini, Groq, xAI &amp; Ollama. LiteLLM alternative with observability, guardrails &amp; streaming. ...

⬆️ 202 • 💬 73 • 1d ago • [GitHub](https://github.com/ENTERPILOT/GOModel/)

---

**[Show HN: Mediator.ai – Using Nash bargaining and LLMs to systematize fairness](https://news.ycombinator.com/item?id=47835411)**

Mediator.ai uses bargaining theory and modern AI to find agreements that two people in conflict would both accept, including ones they hadn't thought of.

⬆️ 158 • 💬 74 • 2d ago • [Mediator.ai](https://mediator.ai/)

---

**[Less human AI agents, please](https://news.ycombinator.com/item?id=47845429)**

Nial – Knowledge work and artificial intelligence.

⬆️ 157 • 💬 167 • 2d ago • [nial.se](https://nial.se/blog/less-human-ai-agents-please/)

---

**[Meta employees are up in arms over a mandatory program to train AI on their](https://news.ycombinator.com/item?id=47860961)**

Meta deploys keystroke-tracking software on US employees' computers, sparking privacy concerns and internal backlash.

⬆️ 115 • 💬 88 • 1d ago • [Business Insider](https://www.businessinsider.com/meta-new-ai-tool-tracks-staff-activity-sparks-concern-2026-4)

---

---

## YouTube Videos: "ai"

**[AI Has Officially Reached &#39;The Point of No Return&#39;…](https://www.youtube.com/watch?v=JxxJi0jMqi0)**

Smalls: Get 60% off your first order + FREE shipping & FREE treats for life at https://smalls.com/ICED Episode Link ...

📺 The Iced Coffee Hour Clips

👁️ 4K • 👍 57 • 💬 26 • ⏱️ 9:25 • 19h ago

---

**[The Dirty Secret Behind AI Data Centers No One Wants to Talk About](https://www.youtube.com/watch?v=Ij_qlW5x2-o)**

Ramageddon” is here: AI data centers are hoarding up to 70% of global DRAM, sending DDR5 prices soaring, distorting console ...

📺 Valuetainment

👁️ 196K • 👍 9K • 💬 519 • ⏱️ 12:41 • 2d ago

---

**[The Man Who Proved We Can&#39;t Control AI (And What That Means for Humanity) | Roman Yampolskiy](https://www.youtube.com/watch?v=U9xygNoXnZQ)**

Dr. Roman Yampolskiy joins me to explore one of the most urgent and uncomfortable questions of our time: what happens when ...

📺 André Duqum

👁️ 35K • 👍 856 • 💬 270 • ⏱️ 1:49:24 • 2d ago

---

**[AI &amp; the Future of Work | The Weekly Show with Jon Stewart](https://www.youtube.com/watch?v=RB_WmoH5nQ4)**

As artificial intelligence continues to integrate into the workforce, Jon is joined by MIT economists David Autor and Daron ...

📺 The Weekly Show with Jon Stewart

👁️ 100K • 👍 3K • 💬 595 • ⏱️ 1:13:14 • 18h ago

---

**[Reacting To My OWN AI VIDEOS..](https://www.youtube.com/watch?v=T0ZkvbZe9Dw)**

Today I reacted to my own AI videos! Make sure you watch the whole video to find out what happens. Merch: https://foltyn.shop/ ...

📺 Foltyn

👁️ 563K • 👍 23K • 💬 3K • ⏱️ 13:36 • 1d ago

---

**[Success is hard until you build AI systems like this](https://www.youtube.com/watch?v=cTqVnwzj3Ug)**

Success is hard until you build AI systems like this Check out Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=james3 (sponsor) In ...

📺 James Blue

👁️ 9K • 💬 2 • ⏱️ 11:49 • 1d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 31K • 👍 766 • 💬 51 • ⏱️ 16:29 • 2d ago

---

**[Qwen 3.6 27b Local Ai Review and Benchmark](https://www.youtube.com/watch?v=HT2NplHskIQ)**

Testing Qwen3.6 27B Q4 on a few of my local ai GPUs in single and dual mode with Nvidia 3090's and 4090's. We hit 4.5k in ...

📺 Digital Spaceport

👁️ 10K • 👍 399 • 💬 62 • ⏱️ 11:11 • 11h ago

---

**[Did Open AI&#39;s Images 2 Just Torch Nanobanana?!](https://www.youtube.com/watch?v=675L31xNEaE)**

OpenAI just dropped Image 2 — their new autoregressive image generation model inside ChatGPT. But is it actually good enough ...

📺 Theoretically Media

👁️ 33K • 👍 1K • 💬 199 • ⏱️ 15:20 • 1d ago

---

**[AI Agent Made 1.15K While I Slept (Tutorial)](https://www.youtube.com/watch?v=vHRF3fClEao)**

Dominic here. While most people stick to traditional crypto mining, I've taken a different route. Today, I'm showcasing my fully ...

📺 Dominic Parker

👁️ 13K • 👍 566 • ⏱️ 7:55 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 717,811 • ❤️ 1,296 • 1d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 125,825 • ❤️ 853 • 8h ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 1,283,534 • ❤️ 689 • 3d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 23,964 • ❤️ 574 • 1d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 1,888 • ❤️ 445 • 20h ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 568 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 350,262 • ❤️ 386 • 6d ago

---

**[gemma-4-E4B-it-OBLITERATED](https://huggingface.co/OBLITERATUS/gemma-4-E4B-it-OBLITERATED)**

*OBLITERATUS*

Gemma 4 E4B OBLITERATED v3 is a text-generation model with 0% refusal and improved coding capabilities, designed for uncensored and unrestricted AI interactions. It features a modified architecture with 720 intact tensors, making it highly compatible with tools like Ollama and llama.cpp, and optimized for performance on consumer hardware.

`text-generation` `8.0B`

⬇️ 90,064 • ❤️ 469 • 3d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 131,398 • ❤️ 273 • 21h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 5,103,971 • ❤️ 2,305 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 17 • 💬 2 • ⭐ 4,301 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 74 • 💬 6 • ⭐ 17,898 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 9 • 💬 2 • ⭐ 6,033 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 24 • 💬 1 • ⭐ 20,377 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 48 • 💬 2 • ⭐ 52,506 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 62 • 💬 4 • ⭐ 513 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 77,823 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,752 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 60,971 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 109 • 💬 5 • ⭐ 1,558 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 49.2k • 🔱 6.4k • 8h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 44.2k • 🔱 2.3k • 5d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 38.7k • 🔱 7.9k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 33.5k • 🔱 3.7k • 6h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 9.4k • 🔱 2.0k • 20h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.6k • 🔱 554 • 3m ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.9k • 🔱 997 • 4h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 10d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 5.3k • 🔱 1.2k • 28d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.7k • 🔱 460 • 14d ago

---

---

*Generated by PeekDeck - A glance is all you need*
