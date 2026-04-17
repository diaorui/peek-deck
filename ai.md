---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-17T13:26:13.837507+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 17, 2026 at 13:26 UTC  
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

**[Reese Witherspoon Doubles Down on Telling Women to Learn AI: Jobs We Hold Are "Three Times More Likely to Be Automated By AI"](https://www.reddit.com/r/artificial/comments/1snqqjo/reese_witherspoon_doubles_down_on_telling_women/)**

Reese Witherspoon is again advising her followers that there's no time like the present to start learning about and using artificial intelligence.

🔗 [Variety](https://variety.com/2026/tv/news/reese-witherspoon-ai-jobs-women-1236723992/) • 8h ago

---

**[I built a small project to organize AI coding tools, looking for feedback on the structure and data model](https://www.reddit.com/r/artificial/comments/1snxdjk/i_built_a_small_project_to_organize_ai_coding/)**

Hi everyone, I’ve been learning by building a small web app that collects and organizes AI coding tools in one place. The idea is to make it easier to compare tools like code editors, coding assistants, and terminal-based agents based on what they do, who they’re for, and how they differ, and I have also decided to make it completely free for use. I’m not trying to sell anything, I’m mainly using it as a learning project to practice: building a searchable directory, structuring data for lots of similar items, designing a unique UI for comparison, and deciding what information is actually useful to show first. I’d love feedback on the project from a learning perspective: What data fields would be most useful in a directory like this? What makes a tool comparison page actually helpful? If you’ve built something similar, what architecture or stack choices worked well? The whole thing was coded in Next.js + Tailwind. The book shelf UI took way longer to properly design as i wanted to make it as unique as possible ( most websites nowadays are boring ) I’m also happy to share what I’ve built so far if that would be useful, Tolop

2h ago

---

**[Agentic OS — an governed multi-agent execution platform](https://www.reddit.com/r/artificial/comments/1so03op/agentic_os_an_governed_multiagent_execution/)**

I've been building a system where multiple AI agents execute structured work under explicit governance rules. Sharing it because the architecture might be interesting to people building multi-agent systems. What it does: You set a goal. A coordinator agent decomposes it into tasks. Specialized agents (developer, designer, QA, etc.) execute through controlled tool access, collaborate via explicit handoffs, and produce artifacts. QA agents validate outputs. Escalations surface for human approval. What's different from CrewAI/AutoGen/LangGraph: The focus isn't on the agent — it's on the governance and execution layer around the agent. Tool calls go through an MCP gateway with per-role permission checks and audit logging Zero shared mutable state between agents — collaboration through structured handoffs only Policy engine with configurable approval workflows (proceed/block/timeout-with-default) Append-only task versioning — every modification creates a new version with author and reason Built-in evaluation engine that scores tasks on quality, iterations, latency, cost, and policy compliance Agent reputation scoring with a weighted formula (QA pass rate, iteration efficiency, latency, cost, reliability) Architecture: 5 layers with strict boundaries — frontend (visualization only), API gateway (auth/RBAC), orchestration engine (24 modules), agent runtime (role-based, no direct tool access), MCP gateway (the only path to tools). Stack: React + TypeScript, FastAPI, SQLite WAL, pluggable LLM providers (OpenAI, Anthropic, Azure), MCP protocol. Configurable: Different team presets (software, marketing, custom), operating models with different governance rules, pluggable LLM backends, reusable skills, and MCP-backed integrations. please guys, I would love to get your feedback on this and tell me if this is interesting for you to use

33m ago

---

**[Qwen 3.6-35B - A3B Opensource Launched.](https://www.reddit.com/r/artificial/comments/1sn4wcs/qwen_3635b_a3b_opensource_launched/)**

⚡ Meet Qwen3.6-35B-A3B：Now Open-Source！🚀🚀 A sparse MoE model, 35B total params, 3B active. Apache 2.0 license. 🔥 Agentic coding on par with models 10x its active size 📷 Strong multimodal perception and reasoning ability 🧠 Multimodal thinking + non-thinking modes Efficient. Powerful. Versatile. Try it now👇 Qwen Studio：chat.qwen.ai HuggingFace：https://huggingface.co/Qwen/Qwen3.6-35B-A3B

23h ago

---

**[Reported ban on ‘sex robots’ by online platform fuels debate on AI boundaries and content moderation](https://www.reddit.com/r/artificial/comments/1snvbe7/reported_ban_on_sex_robots_by_online_platform/)**

This kind of emotional manipulation around AI and adult tech is starting to feel like a real issue. If platforms are stepping in, it raises questions about where the line should be drawn between innovation and exploitation. What do you guys think??

🔗 [Daily Star](https://www.dailystar.co.uk/news/latest-news/online-platform-bans-sex-robots-37025373) • 4h ago

---

**[Agentic OS — an governed multi-agent execution platform](https://www.reddit.com/r/artificial/comments/1snzm1s/agentic_os_an_governed_multiagent_execution/)**

I've been building a system where multiple AI agents execute structured work under explicit governance rules. Sharing it because the architecture might be interesting to people building multi-agent systems. What it does: You set a goal. A coordinator agent decomposes it into tasks. Specialized agents (developer, designer, QA, etc.) execute through controlled tool access, collaborate via explicit handoffs, and produce artifacts. QA agents validate outputs. Escalations surface for human approval. What's different from CrewAI/AutoGen/LangGraph: The focus isn't on the agent — it's on the governance and execution layer around the agent. Tool calls go through an MCP gateway with per-role permission checks and audit logging Zero shared mutable state between agents — collaboration through structured handoffs only Policy engine with configurable approval workflows (proceed/block/timeout-with-default) Append-only task versioning — every modification creates a new version with author and reason Built-in evaluation engine that scores tasks on quality, iterations, latency, cost, and policy compliance Agent reputation scoring with a weighted formula (QA pass rate, iteration efficiency, latency, cost, reliability) Architecture: 5 layers with strict boundaries — frontend (visualization only), API gateway (auth/RBAC), orchestration engine (24 modules), agent runtime (role-based, no direct tool access), MCP gateway (the only path to tools). Stack: React + TypeScript, FastAPI, SQLite WAL, pluggable LLM providers (OpenAI, Anthropic, Azure), MCP protocol. Configurable: Different team presets (software, marketing, custom), operating models with different governance rules, pluggable LLM backends, reusable skills, and MCP-backed integrations. agenticompanies.com please guys, I would love to get your feedback on this and tell me if this is interesting for you to use you can register with email/passoword to view the platform but if you want to operate agentsession I need to send you an invitation code. please feel free to DM me for an invitation code you would also need to use your Anthropic or OpenAI API key to operate then engines Thanks

54m ago

---

**[There are a ton of cool AI companies launching…this “Objection.AI” ain’t one of em lol](https://www.reddit.com/r/artificial/comments/1snhscc/there_are_a_ton_of_cool_ai_companies/)**

https://www.hardresetmedia.com/p/peter-thiel-backed-ai-startup-objection This so funny. Whole company is DOA. They’re saying that the reporter has to preemptively sign the protection agreement in order for the subject to later file a complaint, and the whole tool doesn't work if the reporter doesn't sign it. No reporter is going to sign up for this! From that article: "Put another way, D’Souza is asking journalists to preemptively agree to the possibility of financial penalties set forth by an AI tribunal and/or the guy who helped bankrupt Gawker—all in exchange for an on-the-record interview with someone who is indicating they are paranoid and hoping to pick a fight. No journalist will ever, ever, ever agree to this arrangement. In the real, non-hypothetical world, if I reach out to a source for an interview and they send me back an arbitration agreement from a Peter Thiel-funded website, my response will be, “What?” Then I will say, “That’s not how this stuff works. Do you want to do an interview or not?” Assuming they reiterate their desire to only speak with me if I agree to Objection Protection, I will instead write my story, report on our odd back-and-forth, reach out one more time prior to publication, and note that they declined comment."

15h ago

---

**[Man used AI to make false statements to shut down London nightclub, police say | AI (artificial intelligence) | The Guardian](https://www.reddit.com/r/artificial/comments/1snurvq/man_used_ai_to_make_false_statements_to_shut_down/)**

Heaven club neighbour admits offences under Licensing Act, as Met says fictitious AI-generated complaints a growing issue

🔗 [the Guardian](https://www.theguardian.com/technology/2026/apr/16/man-pleads-guilty-false-statements-shut-down-london-nightclub-heaven) • 5h ago

---

**[OpenAI went from explicitly banning military use in 2023 to deploying on classified Pentagon networks in 2026. Anthropic refused the same deal and got blacklisted. 2.5M users boycotted ChatGPT, uninstalls surged 295%.](https://www.reddit.com/r/artificial/comments/1snig9g/openai_went_from_explicitly_banning_military_use/)**

https://preview.redd.it/g72g8g08omvg1.jpg?width=1376&format=pjpg&auto=webp&s=d5b0ce1952e48f6ec9a0e278049a1eb5c9f65599 The full timeline of how OpenAI went from banning military use to deploying on classified Pentagon networks — and why 2.5 million people boycotted. **The backstory:** - Pentagon wanted AI companies to agree to "any lawful use" on classified networks - Anthropic CEO Dario Amodei refused — specifically citing mass surveillance and autonomous weapons - Trump ordered all federal agencies to stop using Anthropic within 6 months - Defense Secretary Hegseth designated Anthropic a "supply-chain risk" (normally reserved for foreign adversaries) - Hours later, OpenAI signed the deal **The backlash:** - #QuitGPT went viral — 2.5M users boycotted/cancelled - ChatGPT uninstalls surged 295% overnight - US downloads dropped 13% - Claude hit #1 on the US App Store (first time ever) - OpenAI's robotics lead Caitlin Kalinowski resigned - Altman admitted it "appeared opportunistic and haphazard" **What the contract says (after amendments):** - Prohibits domestic surveillance of US citizens - Bans tracking via commercially acquired personal data - Excludes NSA without separate agreement - Allows "all lawful purposes" on classified networks - Allows intelligence activities under Patriot Act, FISA, EO 12333 **What critics say:** - Full contract hasn't been released - "Intentional" surveillance ban doesn't cover incidental collection - "Any lawful use" is broad — laws can change, DoD can modify its own policies - Former DOJ attorney: "There is nothing OpenAI can do to clarify this except release the contract" **The reversal:** - 2023: OpenAI explicitly banned military use - January 2024: Ban quietly removed - February 2026: Deployed on classified Pentagon networks Full breakdown → https://synvoya.com/blog/2026-04-17-quitgpt-openai-pentagon-deal/ Do you think the contract safeguards are real protections or PR cover?

15h ago

---

**[Live now: watching AI agents spend money in real time](https://www.reddit.com/r/artificial/comments/1snjr09/live_now_watching_ai_agents_spend_money_in_real/)**

I kept seeing "agentic payments" in every AI newsletter but couldn't picture what it actually looked like. Like, agents are buying compute, APIs, data — but what does that look like at scale? So I built a page that shows every x402 transaction live. https://wtfareagentsbuying.com/ No mocks. No simulation. Actual agents, actually purchasing things, in real time. You just watch. Running it on a second monitor has been weirdly addictive. Kind of a lava lamp for the AI economy.

14h ago

---

---

## Google News: "ai"

**[Claude Mythos: Finance ministers and top bankers raise serious concerns about AI model](https://www.bbc.com/news/articles/c2ev24yx4rmo)**

Experts say Mythos potentially has an unprecedented ability to identify and exploit cybersecurity weaknesses.

BBC • 3h ago

---

**[Finance leaders warn over Mythos as UK banks prepare to use powerful Anthropic AI tool](https://www.theguardian.com/technology/2026/apr/17/finance-leaders-warn-over-claude-mythos-as-uk-banks-prepare-to-use-powerful-anthropic-ai-tool)**

Release of new Claude model, so far limited to US firms, will expand to British institutions in coming days

The Guardian • 5h ago

---

**[Anthropic discussing AI models, including cybersecurity ones, with EU](https://seekingalpha.com/news/4576081-anthropic-discussing-ai-models-including-cybersecurity-ones-with-eu)**

Anthropic ​is in discussion ‌with the European Commission for its different models, ​including its cyber​security ones, which are ⁠not yet available ​in the EU.

Seeking Alpha • 1h ago

---

**[The Labor Department wants to teach you to use AI more. Here's what we found](https://www.npr.org/2026/04/17/nx-s1-5771629/labor-department-ai-course-ethics)**

The short course provides solid basics for using AI. But it also misidentifies AI products, links out to bad advice and raises ethical concerns about the products it promotes

NPR • 4h ago

---

**[Netflix plans to add a vertical video feed, use AI for recommendations](https://techcrunch.com/2026/04/17/netflix-plans-to-add-a-vertical-video-feed-use-ai-for-recommendations/)**

Netflix is going to launch a TikTok-like vertical video feed within its apps this month, and plans to use AI broadly for content creation and recommendations.

TechCrunch • 8m ago

---

**[Canva relaunches as AI-first platform with new agentic tools](https://qz.com/canva-ai-relaunch-conversational-agentic-design-tools-041726)**

The $42 billion design startup is replacing its template-based approach with AI agents that respond to natural language prompts

qz.com • 1h ago

---

**[Is Mark Zuckerberg's Meta AI getting too smart?](https://www.foxnews.com/tech/mark-zuckerbergs-meta-ai-getting-smart)**

Meta's new Muse Spark AI model powers multimodal image recognition, parallel task handling and a dedicated shopping mode across its apps and AI glasses.

Fox News • 46m ago

---

**[A Family Feud at an Oregon Winery Turns to Vinegar Over A.I. Slop](https://www.nytimes.com/2026/04/17/us/oregon-winery-ai-legal-fight.html)**

The New York Times • 4h ago

---

**[Nvidia rival tells CNBC it's seeking at least $100 million in funding as European AI chip market booms](https://www.cnbc.com/2026/04/17/nvidia-rivals-chip-market-funding-ai-asml-euclyd.html)**

Investor interest for AI chip startups is rising, but big challenges remain for the nascent sector.

CNBC • 6h ago

---

**[Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)**

The updated Codex app for macOS and Windows adds computer use, in-app browsing, image generation, memory, and plugins to accelerate developer workflows.

OpenAI • 22h ago

---

---

## HackerNews: "ai"

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 294 • 💬 182 • 2d ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Cloudflare's AI Platform: an inference layer designed for agents](https://news.ycombinator.com/item?id=47792538)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

⬆️ 294 • 💬 75 • 1d ago • [The Cloudflare Blog](https://blog.cloudflare.com/ai-platform/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 243 • 💬 222 • 1d ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 227 • 💬 186 • 1d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 226 • 💬 85 • 1d ago • [antirez.com](https://antirez.com/news/163)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 203 • 💬 40 • 15h ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[We gave an AI a 3 year retail lease and asked it to make a profit](https://news.ycombinator.com/item?id=47794391)**

We signed a 3 year lease and gave it to an AI

⬆️ 195 • 💬 274 • 22h ago • [andonlabs.com](https://andonlabs.com/blog/andon-market-launch)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 194 • 💬 111 • 2d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 185 • 💬 135 • 1d ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 154 • 💬 99 • 2d ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

---

## YouTube Videos: "ai"

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 125K • 👍 6K • 💬 979 • ⏱️ 14:03 • 1d ago

---

**[New trailer features AI-generated version of Val Kilmer, a year after his death](https://www.youtube.com/watch?v=HmVxgnEs23s)**

The first clips from “As Deep as the Grave” feature an AI-generated version of Val Kilmer, who died in 2025. The filmmakers say ...

📺 NBC News

👁️ 5K • 👍 61 • 💬 28 • ⏱️ 1:43 • 13h ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 464K • 👍 30K • 💬 2K • ⏱️ 12:33 • 13h ago

---

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 262K • 👍 18K • 💬 2K • ⏱️ 7:52 • 2d ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 182K • 👍 5K • 💬 2K • ⏱️ 1:11:10 • 1d ago

---

**[Easiest Way to Make Money with AI Now (Zero Code)](https://www.youtube.com/watch?v=AU5mbiTuZSg)**

Let's build an online business, together, LIVE in 5 days using AI (Starting April 26th, 2026): ...

📺 Iman Gadzhi

👁️ 40K • 👍 2K • 💬 68 • ⏱️ 27:46 • 21h ago

---

**[How To ACTUALLY Make Money With AI Video](https://www.youtube.com/watch?v=7ccb8ArAqMs)**

How To ACTUALLY Make Money With AI Video Best AI Tool to get started https://higgsfield.ai?fpr=dankieft&fp_sid=agency In ...

📺 Dan Kieft

👁️ 11K • 💬 10 • ⏱️ 14:35 • 5h ago

---

**[The ONLY 6 Prompts You Need For Realistic AI Video](https://www.youtube.com/watch?v=dg81yMtasz0)**

Learn How To Make Realistic AI Video with these 6 prompts Try Higgsfield AI ✨https://higgsfield.ai/ai-video?fpr=utm&fp_sid=skai ...

📺 Skai Generated

👁️ 10K • ⏱️ 14:12 • 20h ago

---

**[The 3 AI Skills That Will Be Worth $500K in 2027](https://www.youtube.com/watch?v=qYGGTH2rgI8)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *AI ...

📺 Julia McCoy

👁️ 10K • 👍 701 • 💬 80 • ⏱️ 9:41 • 22h ago

---

**[Canva AI 2.0 Just Changed Everything](https://www.youtube.com/watch?v=yKt9puwEUyw)**

DOWNLOAD THE CANVA CREATE 2026 FEATURE DECK: https://teamrondi.mykajabi.com/canva-create-updates-2026 (Get a ...

📺 Design with Canva

👁️ 9K • 👍 643 • 💬 121 • ⏱️ 21:02 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 188,737 • ❤️ 903 • 3h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,287 • ❤️ 841 • 3d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 21,180 • ❤️ 634 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 100,019 • ❤️ 1,366 • 1d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 2,254 • ❤️ 406 • 10h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,513,465 • ❤️ 2,004 • 6d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 53,781 • ❤️ 368 • 4d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 18,089 • ❤️ 1,085 • 1d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 152,762 • ❤️ 1,251 • 12h ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 153,019 • ❤️ 289 • 20h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 21 • 💬 1 • ⭐ 18,917 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 58 • 💬 1 • ⭐ 929 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 46 • 💬 2 • ⭐ 51,053 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 2 • 💬 2 • ⭐ 616 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 27 • 💬 1 • ⭐ 17,996 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 164 • 💬 10 • ⭐ 40,008 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 50 • 💬 4 • ⭐ 1,733 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 158 • 💬 2 • ⭐ 60,236 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 77,015 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://huggingface.co/papers/2509.19296)**

*Sherwin Bahmani, Tianchang Shen, Jiawei Ren et al. (13 authors)*

A self-distillation framework converts implicit 3D knowledge from video diffusion models into an explicit 3D Gaussian Splatting representation, enabling 3D scene generation from text or images.

▲ 27 • 💬 4 • ⭐ 1,380 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.19296) • [💻 code](https://github.com/nv-tlabs/lyra) • [🔗 project](https://research.nvidia.com/labs/toronto-ai/lyra/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.4k • 🔱 6.2k • 5h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 36.2k • 🔱 1.7k • 2d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 35.4k • 🔱 7.1k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 28.8k • 🔱 3.2k • 1h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.1k • 🔱 518 • 36m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.1k • 🔱 843 • 3d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.8k • 🔱 1.1k • 22d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 181 • 5h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 455 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
