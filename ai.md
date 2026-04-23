---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-23T10:05:46.767979+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 23, 2026 at 10:05 UTC  
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

8h ago

---

**[The Ethics of Staying in the Room](https://www.reddit.com/r/artificial/comments/1sszoht/the_ethics_of_staying_in_the_room/)**

AI doesn't invent bias, it codifies it. When you walk away from the tools you don't agree with, you leave them to be influenced by the people you disagree with most. Abstention isn't neutrality. It's choosing to be invisible in the algorithms.

🔗 [kitchencloset.com](https://kitchencloset.com/realstuff/essays/ethics_of_staying_in_the_room/) • 12h ago

---

**[Are AI tools making things easier or are they just changing the type of work that needs to be done](https://www.reddit.com/r/artificial/comments/1st8uaq/are_ai_tools_making_things_easier_or_are_they/)**

I have noticed that AI tools make it very easy to come up with a lot of ideas or ways to do things very quickly. For example, if you are working on a side project or even just a simple plan, you can now come up with a lot of different ideas in a matter of minutes instead of spending hours thinking about one. At first, it look like a clear way to get more done. But in reality, it often leads to a different kind of work, like looking over outputs, weighing options and deciding what is really worth doing. Sometimes, that decision layer feels like more work than the work itself. So instead of taking away work, it looks like AI is moving it from making things to choosing things. I am interested in how other people are dealing with this. Do you think AI is really saving time or is it just shifting the work?

5h ago

---

**[Meta will record employee screens, clicks, and keystrokes to train AI that may replace them](https://www.reddit.com/r/artificial/comments/1ssty5s/meta_will_record_employee_screens_clicks_and/)**

🔗 [techspot.com](https://www.techspot.com/news/112143-meta-record-employee-screens-clicks-keystrokes-train-ai.html) • 15h ago

---

**[He presentado CTNet: una arquitectura donde el cómputo ocurre como evolución de un estado persistente [D]](https://www.reddit.com/r/artificial/comments/1st40qw/he_presentado_ctnet_una_arquitectura_donde_el/)**

Acabo de publicar una presentación de CTNet y quería compartirla aquí para recibir feedback serio. CTNet propone una arquitectura en la que el cálculo no se organiza como simple reescritura sucesiva de representaciones, sino como transición gobernada de un estado persistente. Dentro de esa dinámica entran memoria reentrante, régimen de cómputo, admisibilidad, coherencia multiescala, cartas locales y salida proyectiva. La intuición central es esta: la salida no agota el proceso; emerge como una proyección de un fondo computacional más rico. Ahora mismo estoy presentando la arquitectura, su formalización y su toy model canónico. El objetivo de esta publicación no es vender un sistema cerrado, sino exponer una propuesta arquitectónica con ambición real y abrir conversación con gente que piense en arquitectura, teoría del cómputo, DL, memoria, routing, razonamiento, orden y sistemas. He dejado la publicación de LinkedIn aquí: Publicación Linkdln Me interesa especialmente feedback de gente que pueda atacar la idea en serio: — consistencia arquitectónica — implicaciones computacionales — relación con transformers, SSMs, MoE, memoria y modelos recurrentes — límites teóricos o prácticos — posibles direcciones de desarrollo No busco aplauso fácil. Busco crítica fuerte y gente potente.

9h ago

---

**[Been building a multi-agent framework in public for 7 weeks, its been a Journey.](https://www.reddit.com/r/artificial/comments/1sta8as/been_building_a_multiagent_framework_in_public/)**

I've been building this repo public since day one, roughly 7 weeks now with Claude Code. Here's where it's at. Feels good to be so close. The short version: AIPass is a local CLI framework where AI agents have persistent identity, memory, and communication. They share the same filesystem, same project, same files - no sandboxes, no isolation. pip install aipass, run two commands, and your agent picks up where it left off tomorrow. You don't need 11 agents to get value. One agent on one project with persistent memory is already a different experience. Come back the next day, say hi, and it knows what you were working on, what broke, what the plan was. No re-explaining. That alone is worth the install. What I was actually trying to solve: AI already remembers things now - some setups are good, some are trash. That part's handled. What wasn't handled was me being the coordinator between multiple agents - copying context between tools, keeping track of who's doing what, manually dispatching work. I was the glue holding the workflow together. Most multi-agent frameworks run agents in parallel, but they isolate every agent in its own sandbox. One agent can't see what another just built. That's not a team. That's a room full of people wearing headphones. So the core idea: agents get identity files, session history, and collaboration patterns - three JSON files in a .trinity/ directory. Plain text, git diff-able, no database. But the real thing is they share the workspace. One agent sees what another just committed. They message each other through local mailboxes. Work as a team, or alone. Have just one agent helping you on a project, party plan, journal, hobby, school work, dev work - literally anything you can think of. Or go big, 50 agents building a rocketship to Mars lol. Sup Elon. There's a command router (drone) so one command reaches any agent. pip install aipass aipass init aipass init agent my-agent cd my-agent claude codex or gemini too, mostly claude code tested rn Where it's at now: 11 agents, 4,000+ tests, 400+ PRs (I know), automated quality checks across every branch. Works with Claude Code, Codex, and Gemini CLI. It's on PyPI. Tonight I created a fresh test project, spun up 3 agents, and had them test every service from a real user's perspective - email between agents, plan creation, memory writes, vector search, git commits. Most things just worked. The bugs I found were about the framework not monitoring external projects the same way it monitors itself. Exactly the kind of stuff you only catch by eating your own dogfood. Recent addition I'm pretty happy with: watchdog. When you dispatch work to an agent, you used to just... hope it finished. Now watchdog monitors the agent's process and wakes you when it's done - whether it succeeded, crashed, or silently exited without finishing. It's the difference between babysitting your agents and actually trusting them to work while you do something else. 5 handlers, 130 tests, replaced a hacky bash one-liner. Coming soon: an onboarding agent that walks new users through setup interactively - system checks, first agent creation, guided tour. It's feature-complete, just in final testing. Also working on automated README updates so agents keep their own docs current without being told. I'm a solo dev but every PR is human-AI collaboration - the agents help build and maintain themselves. 105 sessions in and the framework is basically its own best test case. https://github.com/AIOSAI/AIPass

4h ago

---

**[Current state of AI in one image.](https://www.reddit.com/r/artificial/comments/1st7kj2/current_state_of_ai_in_one_image/)**

I’m pretty new to AI and my notifications seemed on point for the current state of things. But this feels more polarized than any recent tech I’ve followed. A lot of discussion seems to fall into two camps, either AI is dangerous and needs to be stopped or AI is amazing and needs to get more powerful. I’m curious how much focus is actually going into user experience and behavior, making systems feel genuinely intelligent and useful, rather than just scaling up model size and parameters. It seems like there’s still a lot of untapped potential in improving smaller models through better structure, interaction design, and system-level improvements, not just making them bigger. Are people actively working on that side of things, or is most of the effort still going into scaling?

6h ago

---

**[Are we moving closer towards dead internet theory?](https://www.reddit.com/r/artificial/comments/1ssbjjq/are_we_moving_closer_towards_dead_internet_theory/)**

I mean a)The majority of articles on the internet are written by AIs b) 4 of the top 10 Youtube channels c) 4 in 10 Facebook posts d) 1 in 5 videos shown to new Youtube users e) The #1 most-subscribed Twitch streamer is an AI f) 44% of songs on Deezer Also, most of the ads are now AI generated, like AI creating content for other AI

1d ago

---

**[What was the biggest thing to happen in the field of AI?](https://www.reddit.com/r/artificial/comments/1sso2rb/what_was_the_biggest_thing_to_happen_in_the_field/)**

I personally think it’s either AlphaGo or ChatGPT. AlphaGo showed to the whole world that AIs can be better than its creators in an area that people believed needed ‘intuition’. Most people don’t know go, but it somewhat showed the potential of AI to the world. DeepBlue was also kinda similar to it, but for some reason most people don’t think DeepBlue as “An AI that beat human at chess”, so I’m not counting it. ChatGPT was… on a different level. It was looked as revolutionary that a program can fluently speak and help solve problems it doesn’t specialize in. It made most people use AI in their everyday lives, so definitely takes the cake imo. Edit: Ig the transformers was also very important, (literally why chatgpt was able to exist lol) but a layperson doesn’t know what that is nor why that matters, so…

19h ago

---

**[The hidden gap in enterprise AI adoption: nobody has figured out how to manage AI agents at scale](https://www.reddit.com/r/artificial/comments/1stboz0/the_hidden_gap_in_enterprise_ai_adoption_nobody/)**

We are entering a phase where AI adoption metrics at large companies look good on paper, but a new problem is quietly forming: nobody actually knows how to govern the agents that are being deployed. Here is the maturity curve as I see it: Stage 1: Experimentation. Teams spin up a few agents, see results, get excited. Stage 2: Proliferation. Agents spread across departments. Sales has one. Support has three. Marketing is running five. DevOps is testing two. Stage 3: Chaos. Nobody knows which agents are active, what instructions they are running, who owns them, whether any are duplicating effort, or whether the configs are current. Most mid-to-large enterprises with serious AI programs are hitting Stage 3 right now. The tooling for Stage 3 does not really exist yet. Some of the symptoms I keep seeing: - Customer-facing agents running system prompts that were written 8 months ago and never reviewed - Multiple teams independently building agents to solve the same problem because there is no central inventory - Agents that were stood up for a pilot and never decommissioned, still consuming credits and occasionally responding to real users - No audit trail when something goes wrong. Did the agent say that because the model hallucinated or because someone changed the instructions last Tuesday? The build-side tooling (LangChain, LangGraph, Claude, etc.) is excellent and getting better. The run-side tooling for AI directors and heads of AI who need to actually manage a fleet of agents in production is almost nonexistent. We are working on this at Caliber. We gave the community an open source repo as a foundation for structured AI agent setup (link in comments). And if you are in an AI leadership role trying to navigate this transition, the newsletter at caliber-ai.dev covers exactly this operational layer.

2h ago

---

---

## Google News: "ai"

**[Anthropic’s New Mythos A.I. Model Sets Off Global Alarms](https://www.nytimes.com/2026/04/22/technology/anthropics-mythos-ai.html)**

The New York Times • 14h ago

---

**[Anthropic looks to hire six-figure role for negotiating data center deals to fuel Europe AI expansion](https://www.cnbc.com/2026/04/23/anthropic-ai-europe-data-center-capacity-role.html)**

U.S. tech giants have announced huge infrastructure expenditure in 2026 as they look to scale the deployment of AI.

CNBC • 42m ago

---

**[Anthropic: No "kill switch" for AI in classified settings](https://www.axios.com/2026/04/22/anthropic-no-kill-switch-ai-classified-settings)**

Axios • 9h ago

---

**[AI is already leading to fewer jobs for young people, says Sunak](https://www.bbc.com/news/articles/cvg07x4rejdo)**

The former prime minister said graduates' concerns about getting entry-level jobs are justified.

BBC • 3h ago

---

**[We're former Google coworkers who raised $4.5M for an AI startup. We didn't build a big team — we built fast instead.](https://www.businessinsider.com/former-google-coworkers-raise-millions-ai-startup-tiny-team-2026-4)**

After meeting at Google, two friends reunited years later. They built a six-person AI startup, moved fast, and raised $4.5 million in seed funding.

Business Insider • 54m ago

---

**[Merck’s new AI commercial strategy ‘reimagining engagement with HCPs’](https://www.fiercepharma.com/marketing/mercks-new-ai-commercial-strategy-reimagining-engagement-hcps)**

Merck & Co.’s $1 billion deal with Google Cloud is seeking to bolster its AI credentials—and the U.S. Big Pharma has some big plans for its commercial teams.  | Merck & Co.’s $1 billion deal with Google Cloud is seeking to bolster its AI credentials—and the U.S. Big Pharma has some big plans for its commercial teams.

Fierce Pharma • 2h ago

---

**[Ping-pong robot Ace makes history by beating top-level human players](https://www.reuters.com/sports/ping-pong-robot-ace-makes-history-by-beating-top-level-human-players-2026-04-22/)**

Reuters • 19h ago

---

**[AI-powered robot beats elite table tennis players](https://www.theguardian.com/science/2026/apr/22/ai-powered-robot-beats-elite-table-tennis-players-milestone-robotics)**

In feat hailed as milestone in robotics, Sony AI’s Ace wins three out of five matches played under official rules

The Guardian • 8h ago

---

**[A robot is beating human pros at table tennis. Its maker calls it a milestone for machines](https://apnews.com/article/ai-table-tennis-robot-ping-pong-sony-995b239945e0dc8d7bea918a850969dc)**

A paddle-wielding robot is so adept at playing table tennis that it is posing a tough challenge to elite human players and sometimes defeating them, according to a new study in the journal Nature that shows how advances in artificial intelligence are making robots more agile.

AP News • 18h ago

---

**[House lawmakers get a chilling demo of ‘jailbroken’ AI](https://www.politico.com/news/2026/04/22/ai-chatbots-jailbreak-safety-00887869)**

Politico • 11h ago

---

---

## HackerNews: "ai"

**[Meta to start capturing employee mouse movements, keystrokes for AI training](https://news.ycombinator.com/item?id=47851948)**

⬆️ 780 • 💬 517 • 1d ago • [reuters.com](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

---

**[Atlassian enables default data collection to train AI](https://news.ycombinator.com/item?id=47833247)**

⬆️ 600 • 💬 134 • 2d ago • [letsdatascience.com](https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8)

---

**[AI Resistance: some recent anti-AI stuff that’s worth discussing](https://news.ycombinator.com/item?id=47839951)**

People are sick of artificial intelligence, and are increasingly making it known through acts of resistance.

⬆️ 386 • 💬 412 • 2d ago • [stephvee.ca](https://stephvee.ca/blog/artificial%20intelligence/ai-resistance-is-growing/)

---

**[Deezer says 44% of songs uploaded to its platform daily are AI-generated](https://news.ycombinator.com/item?id=47835928)**

Deezer says consumption of AI-generated music on the platform is still very low, between 1-3% of the total streams, and that 85% of these streams are detected as fraudulent and are demonetized.

⬆️ 364 • 💬 388 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/)

---

**[Tell HN: I'm sick of AI everything](https://news.ycombinator.com/item?id=47857461)**

⬆️ 329 • 💬 184 • 1d ago

---

**[Scoring Show HN submissions for AI design patterns](https://news.ycombinator.com/item?id=47864393)**

An attempt to detect AI design patterns in Show HN pages

⬆️ 310 • 💬 222 • 19h ago • [adriankrebs.ch](https://www.adriankrebs.ch/blog/design-slop/)

---

**[A Roblox cheat and one AI tool brought down Vercel's platform](https://news.ycombinator.com/item?id=47844431)**

⬆️ 282 • 💬 161 • 2d ago • [webmatrices.com](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

---

**[Show HN: GoModel – an open-source AI gateway in Go](https://news.ycombinator.com/item?id=47849097)**

High-performance AI gateway written in Go - unified OpenAI-compatible API for OpenAI, Anthropic, Gemini, Groq, xAI &amp; Ollama. LiteLLM alternative with observability, guardrails &amp; streaming. ...

⬆️ 198 • 💬 72 • 1d ago • [GitHub](https://github.com/ENTERPILOT/GOModel/)

---

**[Show HN: Mediator.ai – Using Nash bargaining and LLMs to systematize fairness](https://news.ycombinator.com/item?id=47835411)**

Mediator.ai uses bargaining theory and modern AI to find agreements that two people in conflict would both accept, including ones they hadn't thought of.

⬆️ 157 • 💬 74 • 2d ago • [Mediator.ai](https://mediator.ai/)

---

**[Less human AI agents, please](https://news.ycombinator.com/item?id=47845429)**

Nial – Knowledge work and artificial intelligence.

⬆️ 156 • 💬 166 • 2d ago • [nial.se](https://nial.se/blog/less-human-ai-agents-please/)

---

---

## YouTube Videos: "ai"

**[AI Has Officially Reached &#39;The Point of No Return&#39;…](https://www.youtube.com/watch?v=JxxJi0jMqi0)**

Smalls: Get 60% off your first order + FREE shipping & FREE treats for life at https://smalls.com/ICED Episode Link ...

📺 The Iced Coffee Hour Clips

👁️ 3K • 👍 50 • 💬 15 • ⏱️ 9:25 • 15h ago

---

**[AI &amp; the Future of Work | The Weekly Show with Jon Stewart](https://www.youtube.com/watch?v=RB_WmoH5nQ4)**

As artificial intelligence continues to integrate into the workforce, Jon is joined by MIT economists David Autor and Daron ...

📺 The Weekly Show with Jon Stewart

👁️ 83K • 👍 3K • 💬 493 • ⏱️ 1:13:14 • 14h ago

---

**[The Dirty Secret Behind AI Data Centers No One Wants to Talk About](https://www.youtube.com/watch?v=Ij_qlW5x2-o)**

Ramageddon” is here: AI data centers are hoarding up to 70% of global DRAM, sending DDR5 prices soaring, distorting console ...

📺 Valuetainment

👁️ 190K • 👍 8K • 💬 494 • ⏱️ 12:41 • 1d ago

---

**[New AI image generator BEATS EVERYTHING](https://www.youtube.com/watch?v=TLFPbMUtErM)**

ChatGPT Images 2.0 review. GPT Image 2.0 vs Nano Banana. #ai #aiart #aitools #imagegenerator #agi Thanks to our sponsor ...

📺 AI Search

👁️ 75K • 👍 3K • 💬 613 • ⏱️ 35:20 • 1d ago

---

**[The Man Who Proved We Can&#39;t Control AI (And What That Means for Humanity) | Roman Yampolskiy](https://www.youtube.com/watch?v=U9xygNoXnZQ)**

Dr. Roman Yampolskiy joins me to explore one of the most urgent and uncomfortable questions of our time: what happens when ...

📺 André Duqum

👁️ 33K • 👍 804 • 💬 256 • ⏱️ 1:49:24 • 1d ago

---

**[I mixed AI with Real Footage… and it’s actually scary.](https://www.youtube.com/watch?v=Q6S8tGOVNb4)**

In this video, I explore 6 techniques to mix AI with real footage using tools inside Higgsfield AI. ⚡Try out Higgsfield here: ...

📺 Sightseeing Stan

👁️ 8K • 👍 913 • 💬 135 • ⏱️ 10:12 • 20h ago

---

**[Reacting To My OWN AI VIDEOS..](https://www.youtube.com/watch?v=T0ZkvbZe9Dw)**

Today I reacted to my own AI videos! Make sure you watch the whole video to find out what happens. Merch: https://foltyn.shop/ ...

📺 Foltyn

👁️ 504K • 👍 21K • 💬 3K • ⏱️ 13:36 • 1d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 30K • 👍 755 • 💬 50 • ⏱️ 16:29 • 2d ago

---

**[FAKE Pro-Trump AI Slop Accounts BOMBARD Social Media As MAGA CRUMBLES TO PIECES | Kyle Kulinski Show](https://www.youtube.com/watch?v=1FM_idmXt-g)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 88K • 👍 7K • 💬 830 • ⏱️ 11:03 • 1d ago

---

**[&#39;WHERE IS THE OFF BUTTON?&#39;: AI fears grow after robot wins half-marathon](https://www.youtube.com/watch?v=TCFRQc0h5BY)**

Humanoid robot 'Lightning' broke a half-marathon world record in Beijing, finishing 13 miles faster than any human.

📺 Fox News Clips

👁️ 51K • 👍 847 • 💬 459 • ⏱️ 5:19 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 717,811 • ❤️ 1,268 • 1d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 125,825 • ❤️ 831 • 4h ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 1,283,534 • ❤️ 680 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 23,964 • ❤️ 522 • 21h ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 561 • 1d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 1,888 • ❤️ 379 • 17h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 350,262 • ❤️ 379 • 6d ago

---

**[gemma-4-E4B-it-OBLITERATED](https://huggingface.co/OBLITERATUS/gemma-4-E4B-it-OBLITERATED)**

*OBLITERATUS*

Gemma 4 E4B OBLITERATED v3 is a text-generation model with 0% refusal and improved coding capabilities, designed for uncensored and unrestricted AI interactions. It features a modified architecture with 720 intact tensors, making it highly compatible with tools like Ollama and llama.cpp, and optimized for performance on consumer hardware.

`text-generation` `8.0B`

⬇️ 90,064 • ❤️ 465 • 3d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 131,398 • ❤️ 243 • 18h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 5,103,971 • ❤️ 2,298 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 14 • 💬 2 • ⭐ 4,176 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 7 • 💬 2 • ⭐ 6,033 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 74 • 💬 6 • ⭐ 17,591 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

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

▲ 61 • 💬 4 • ⭐ 393 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,752 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 77,739 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 60,900 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 107 • 💬 5 • ⭐ 1,558 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 49.1k • 🔱 6.4k • 4h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 43.9k • 🔱 2.3k • 4d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 38.6k • 🔱 7.9k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 33.4k • 🔱 3.7k • 3h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 9.2k • 🔱 2.0k • 17h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.5k • 🔱 552 • 1h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.9k • 🔱 990 • 4d ago

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
