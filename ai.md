---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-17T16:02:12.228649+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 17, 2026 at 16:02 UTC  
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

**[Opus 4.7 is terrible, and Anthropic has completely dropped the ball](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/)**

Tried posting this in r/ClaudeAI but it got auto-removed, and I was told to post it in the "Bugs Megathread." Don't really think it should been removed, but whatever, I'll just post it here since I'm sure it's still relevant. Like a lot of people, I switched from ChatGPT to Claude not too long ago during the whole DoW fiasco and Sam Altman “antics.” At first, I was genuinely impressed. I do fairly heavy theoretical math and physics research, and Opus 4.6 was simply the best tool I’d used for synthesizing ideas and working through complex logic. But the last few weeks have been really disappointing, and I’m seriously considering going back to GPT (even though, for personal reasons, I’d really rather not). How many times has Claude been down recently? And why is it that I can ask Claude 4.7 (with adaptive thinking turned on) to work through a detailed proof, and it just spirals “oh wait, that doesn’t work, let me try again” five times in a single response? Yes, there’s a workaround to explicitly tell it to think before answering. But… why is that necessary? I’m paying $20/month. This is supposed to be a top-tier model. Instead, it burns through time, second-guesses itself mid-response, and often fails to land anywhere useful on problems I’m fairly sure 4.6 would have handled more coherently a month ago. And then before I know it I hit the usage limit. I’m a PhD student. I can’t justify spending $100-$200/month on higher tiers. $20 has always been enough for me, and I’ve come to rely on these tools for my research. I expected to stick with Claude long-term, but the recent instability and drop in reliability make it hard to justify paying for it out of pocket. It’s frustrating to feel pushed toward a competitor because of this. But at a certain point, the usability of the product has to come first. Really disappointing.

2h ago

---

**[Reese Witherspoon Doubles Down on Telling Women to Learn AI: Jobs We Hold Are "Three Times More Likely to Be Automated By AI"](https://www.reddit.com/r/artificial/comments/1snqqjo/reese_witherspoon_doubles_down_on_telling_women/)**

Reese Witherspoon is again advising her followers that there's no time like the present to start learning about and using artificial intelligence.

🔗 [Variety](https://variety.com/2026/tv/news/reese-witherspoon-ai-jobs-women-1236723992/) • 11h ago

---

**[What AI image generator works the best?](https://www.reddit.com/r/artificial/comments/1so4m79/what_ai_image_generator_works_the_best/)**

There seems to be about 1000 different options. I'm just looking for one that takes a prompt and spits out something usable. I'm good with paying for it if I need to but it needs to be able.to handle a lot of work.

21m ago

---

**[Google patents AI tech that will personalize websites and make them look different for everyone](https://www.reddit.com/r/artificial/comments/1so3vto/google_patents_ai_tech_that_will_personalize/)**

The patent describes a system that uses artificial intelligence to create personalized web pages for each user.

🔗 [PC Guide](https://www.pcguide.com/news/google-patents-ai-tech-that-will-personalize-websites-and-make-them-look-different-for-everyone/) • 47m ago

---

**[Binary Choice between Harm and Falsehood](https://www.reddit.com/r/artificial/comments/1so361l/binary_choice_between_harm_and_falsehood/)**

Gemini is always the most bloodthirsty.... First experiment phase, where the models were asked to commit to chosing Harm or Falsehood: Model Accepted Binary Framing? One-Word Answer Aligned with Nuanced View? Notes ChatGPT No (qualified it) Harm Partially Treated as simplification; emphasized context and edge cases Claude No (qualified it) Harm Partially Highlighted nuance; resisted strict binary framing Gemini Yes Harm More strictly aligned Accepted the binary framing without qualification Here, Gemini stood out because it accepted the forced binary, while ChatGPT and Claude tended to treat it as an oversimplification and added nuance, while refusing. --- In a second phase, when pushed with edge cases, all models abandoned the simple ‘harm vs. falsehood’ rule and relied on context-sensitive reasoning instead: 📊 Clean Three-Model Comparison Property Claude ChatGPT Gemini Binary answer Harm Harm Harm Calls it simplification YES YES YES Accepts guideline YES YES YES Breaks guideline YES YES YES Escalation (Q8) Truth Falsehood Falsehood Consistency claim NO YES YES Universal rule NO NO NO Soft default NO YES YES Strength of default none moderate strong Reasoning model multi-axis harm-weighted threshold system Instruction priority nuanced > rule conditional rule > nuance (AI) Claude → anti-reductionist ChatGPT → pragmatic utilitarian Gemini → structured decision framework Fun edge pushing on a Friday....

1h ago

---

**[Agentic OS — an governed multi-agent execution platform](https://www.reddit.com/r/artificial/comments/1snzm1s/agentic_os_an_governed_multiagent_execution/)**

I've been building a system where multiple AI agents execute structured work under explicit governance rules. Sharing it because the architecture might be interesting to people building multi-agent systems. What it does: You set a goal. A coordinator agent decomposes it into tasks. Specialized agents (developer, designer, QA, etc.) execute through controlled tool access, collaborate via explicit handoffs, and produce artifacts. QA agents validate outputs. Escalations surface for human approval. What's different from CrewAI/AutoGen/LangGraph: The focus isn't on the agent — it's on the governance and execution layer around the agent. Tool calls go through an MCP gateway with per-role permission checks and audit logging Zero shared mutable state between agents — collaboration through structured handoffs only Policy engine with configurable approval workflows (proceed/block/timeout-with-default) Append-only task versioning — every modification creates a new version with author and reason Built-in evaluation engine that scores tasks on quality, iterations, latency, cost, and policy compliance Agent reputation scoring with a weighted formula (QA pass rate, iteration efficiency, latency, cost, reliability) Architecture: 5 layers with strict boundaries — frontend (visualization only), API gateway (auth/RBAC), orchestration engine (24 modules), agent runtime (role-based, no direct tool access), MCP gateway (the only path to tools). Stack: React + TypeScript, FastAPI, SQLite WAL, pluggable LLM providers (OpenAI, Anthropic, Azure), MCP protocol. Configurable: Different team presets (software, marketing, custom), operating models with different governance rules, pluggable LLM backends, reusable skills, and MCP-backed integrations. agenticompanies.com please guys, I would love to get your feedback on this and tell me if this is interesting for you to use you can register with email/passoword to view the platform but if you want to operate agentsession I need to send you an invitation code. please feel free to DM me for an invitation code you would also need to use your Anthropic or OpenAI API key to operate then engines Thanks

3h ago

---

**[I built a small project to organize AI coding tools, looking for feedback on the structure and data model](https://www.reddit.com/r/artificial/comments/1snxdjk/i_built_a_small_project_to_organize_ai_coding/)**

Hi everyone, I’ve been learning by building a small web app that collects and organizes AI coding tools in one place. The idea is to make it easier to compare tools like code editors, coding assistants, and terminal-based agents based on what they do, who they’re for, and how they differ, and I have also decided to make it completely free for use. I’m not trying to sell anything, I’m mainly using it as a learning project to practice: building a searchable directory, structuring data for lots of similar items, designing a unique UI for comparison, and deciding what information is actually useful to show first. I’d love feedback on the project from a learning perspective: What data fields would be most useful in a directory like this? What makes a tool comparison page actually helpful? If you’ve built something similar, what architecture or stack choices worked well? The whole thing was coded in Next.js + Tailwind. The book shelf UI took way longer to properly design as i wanted to make it as unique as possible ( most websites nowadays are boring ) I’m also happy to share what I’ve built so far if that would be useful, Tolop

5h ago

---

**[Reported ban on ‘sex robots’ by online platform fuels debate on AI boundaries and content moderation](https://www.reddit.com/r/artificial/comments/1snvbe7/reported_ban_on_sex_robots_by_online_platform/)**

This kind of emotional manipulation around AI and adult tech is starting to feel like a real issue. If platforms are stepping in, it raises questions about where the line should be drawn between innovation and exploitation. What do you guys think??

🔗 [Daily Star](https://www.dailystar.co.uk/news/latest-news/online-platform-bans-sex-robots-37025373) • 7h ago

---

**[Claude Design, a new Anthropic Labs product, lets you collaborate with Claude to create polished visual work like designs, prototypes, slides, one-pagers, and more](https://www.reddit.com/r/artificial/comments/1so44z2/claude_design_a_new_anthropic_labs_product_lets/)**

Claude Design is powered by Claude Opus 4.7 and is available in research preview for Claude Pro, Max, Team, and Enterprise subscribers.

🔗 [anthropic.com](https://www.anthropic.com/news/claude-design-anthropic-labs) • 38m ago

---

**[I built a "Secure Development" skill for Claude Code — it auto-activates when you're building APIs, handling auth, deploying, etc.](https://www.reddit.com/r/artificial/comments/1so42ph/i_built_a_secure_development_skill_for_claude/)**

I've been diving deep into security courses and certifications lately, OWASP, DevSecOps pipelines, cloud security architecture, compliance frameworks. I also had the chance to work alongside a senior solution architect who helped me understand how these concepts connect in real-world production systems. After absorbing all of that, I decided to group everything I've learned into a Claude Code skill that automatically activates whenever you're doing security-relevant work: building APIs, setting up auth, managing secrets, configuring CI/CD, integrating LLMs, or deploying to production. Think of it as a security co-pilot baked into your dev workflow. What it covers (full SDLC): - Planning — Threat modeling (STRIDE/PASTA), security requirements, compliance mapping - Architecture — Least privilege, defense in depth, zero trust, encryption patterns - Coding — Input validation, secrets management, supply chain security - Testing — SAST/DAST/SCA tooling guidance, security-focused code review checklists - CI/CD — Pipeline security gates, container hardening, IaC scanning - Monitoring — SIEM, IDS/IPS, incident response plans Includes deep-dive references for: - REST API security & Swagger/OpenAPI hardening - OWASP LLM Top 10 & prompt injection defense - Data classification (Public/Internal/Confidential/Secret) - IAM & API Gateway architecture patterns - Compliance frameworks (GDPR, ISO 27001, PCI-DSS, SOC 2) It's language/framework agnostic — works for any project. GitHub: https://github.com/IyedGuezmir/secure-development-skill Would love feedback — what security areas would you want covered that aren't here?

41m ago

---

---

## Google News: "ai"

**[Claude Mythos: Finance ministers and top bankers raise serious concerns about AI model](https://www.bbc.com/news/articles/c2ev24yx4rmo)**

Experts say Mythos potentially has an unprecedented ability to identify and exploit cybersecurity weaknesses.

BBC • 5h ago

---

**[Anthropic launches Claude Design, a new product for creating quick visuals](https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/)**

The company says Claude Design is intended to help people like founders and product managers without a design background share their ideas more easily.

TechCrunch • 1h ago

---

**[Illinois is OpenAI and Anthropic’s latest battleground as state tries to assess liability for catastrophes caused by AI](https://fortune.com/2026/04/17/illinois-openai-anthropic-ai-catastrophe-liability-bills/)**

OpenAI is backing SB 3444, under which frontier AI developers would not be liable for the death or serious injury of 100 or more people or more than $1 billion in property damage.

Fortune • 9m ago

---

**[Nvidia rival tells CNBC it's seeking at least $100 million in funding as European AI chip market booms](https://www.cnbc.com/2026/04/17/nvidia-rivals-chip-market-funding-ai-asml-euclyd.html)**

Investor interest for AI chip startups is rising, but big challenges remain for the nascent sector.

CNBC • 8h ago

---

**[AI Drafting My Stories? Over My Dead Body](https://www.wired.com/story/backchannel-the-problem-with-letting-ai-do-the-writing/)**

AI-assisted writing is creeping into newsrooms under the guise of efficiency. But the tradeoff may be more profound than publishers are willing to admit.

WIRED • 16m ago

---

**[Tech stocks today: AMD and other tech stocks trade at record highs, Anthropic releases its newest Claude Opus model](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-amd-and-other-tech-stocks-trade-at-record-highs-anthropic-releases-its-newest-claude-opus-model-144220487.html)**

Live coverage of "Magnificent Seven" stocks, and the latest technology news.

Yahoo Finance • 45m ago

---

**[A Family Feud at an Oregon Winery Turns to Vinegar Over A.I. Slop](https://www.nytimes.com/2026/04/17/us/oregon-winery-ai-legal-fight.html)**

The New York Times • 6h ago

---

**[America wakes up to AI’s dangerous power](https://www.economist.com/leaders/2026/04/16/america-wakes-up-to-ais-dangerous-power)**

The Economist • 1d ago

---

**[Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)**

The updated Codex app for macOS and Windows adds computer use, in-app browsing, image generation, memory, and plugins to accelerate developer workflows.

OpenAI • 1d ago

---

**[New ways to create personalized images in the Gemini app](https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana/)**

Nano Banana 2 now uses your personal context and Google Photos to create images that reflect your unique life.

blog.google • 23h ago

---

---

## HackerNews: "ai"

**[Cloudflare's AI Platform: an inference layer designed for agents](https://news.ycombinator.com/item?id=47792538)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

⬆️ 302 • 💬 82 • 1d ago • [The Cloudflare Blog](https://blog.cloudflare.com/ai-platform/)

---

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 294 • 💬 183 • 2d ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 243 • 💬 222 • 2d ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 229 • 💬 187 • 1d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 227 • 💬 86 • 1d ago • [antirez.com](https://antirez.com/news/163)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 212 • 💬 43 • 18h ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[We gave an AI a 3 year retail lease and asked it to make a profit](https://news.ycombinator.com/item?id=47794391)**

We signed a 3 year lease and gave it to an AI

⬆️ 196 • 💬 278 • 1d ago • [andonlabs.com](https://andonlabs.com/blog/andon-market-launch)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 194 • 💬 111 • 2d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 187 • 💬 136 • 2d ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 154 • 💬 99 • 2d ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

---

## YouTube Videos: "ai"

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 138K • 👍 6K • 💬 956 • ⏱️ 14:03 • 1d ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 547K • 👍 34K • 💬 2K • ⏱️ 12:33 • 16h ago

---

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 266K • 👍 18K • 💬 2K • ⏱️ 7:52 • 2d ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 188K • 👍 5K • 💬 2K • ⏱️ 1:11:10 • 1d ago

---

**[AI Actresses, Devices That Read Thoughts, and Robot Dogs](https://www.youtube.com/watch?v=RO0HxaIwhkQ)**

Taken from JRE #2484 w/David Cross YouTube: https://youtu.be/efJ1-q3XxVc JRE on Spotify: ...

📺 JRE Clips

👁️ 128K • 👍 3K • 💬 747 • ⏱️ 15:26 • 23h ago

---

**[Canva AI 2.0 Just Changed Everything](https://www.youtube.com/watch?v=yKt9puwEUyw)**

DOWNLOAD THE CANVA CREATE 2026 FEATURE DECK: https://teamrondi.mykajabi.com/canva-create-updates-2026 (Get a ...

📺 Design with Canva

👁️ 10K • 👍 693 • 💬 135 • ⏱️ 21:02 • 23h ago

---

**[Paperclip AI Just Changed How AI Agents Work Forever](https://www.youtube.com/watch?v=4Bra0p4lsac)**

Host PaperClip Safely on Hostinger http://hostinger.com/youripaperclip In this video, I break down how Paperclip actually works ...

📺 Youri van Hofwegen

👁️ 4K • 💬 2 • ⏱️ 11:29 • 1h ago

---

**[Of course these cats are AI](https://www.youtube.com/watch?v=QFWUE2egnOg)**

Is this video of three cats surfing down a stairway in boxes and hampers AI-generated? Of course! As cool as it sounds, there are a ...

📺 Jeremy Carrasco

👁️ 262K • 👍 21K • 💬 244 • ⏱️ 1:05 • 19h ago

---

**[THE AI BUBBLE POP HAS STARTED...](https://www.youtube.com/watch?v=b5wOx2lZRM0)**

Hello guys and gals, it's me Mutahar again! This time we take another look at the AI bubble and see the cracks finally start.

📺 SomeOrdinaryGamers

👁️ 504K • 👍 20K • 💬 2K • ⏱️ 20:54 • 2d ago

---

**[The AI Model That Frightens Wall Street](https://www.youtube.com/watch?v=riWmkvrhM9o)**

Anthropic's new Mythos model has banks, tech giants and governments scrambling to understand what could change for ...

📺 Bloomberg Television

👁️ 85K • 👍 1K • 💬 96 • ⏱️ 4:19 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 188,737 • ❤️ 910 • 6h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,287 • ❤️ 845 • 3d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 21,180 • ❤️ 667 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 100,019 • ❤️ 1,370 • 1d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 2,254 • ❤️ 409 • 13h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,513,465 • ❤️ 2,009 • 6d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 53,781 • ❤️ 374 • 5d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 18,089 • ❤️ 1,092 • 1d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 153,019 • ❤️ 313 • 23h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 152,762 • ❤️ 1,255 • 15h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 22 • 💬 1 • ⭐ 18,917 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 62 • 💬 1 • ⭐ 929 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,053 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 3 • 💬 2 • ⭐ 616 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 17,996 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,008 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 51 • 💬 4 • ⭐ 1,733 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 159 • 💬 2 • ⭐ 60,236 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 52 • 💬 1 • ⭐ 77,015 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://huggingface.co/papers/2509.19296)**

*Sherwin Bahmani, Tianchang Shen, Jiawei Ren et al. (13 authors)*

A self-distillation framework converts implicit 3D knowledge from video diffusion models into an explicit 3D Gaussian Splatting representation, enabling 3D scene generation from text or images.

▲ 28 • 💬 4 • ⭐ 1,380 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.19296) • [💻 code](https://github.com/nv-tlabs/lyra) • [🔗 project](https://research.nvidia.com/labs/toronto-ai/lyra/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.5k • 🔱 6.2k • 8h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 36.5k • 🔱 1.7k • 2d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 35.5k • 🔱 7.1k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 28.9k • 🔱 3.2k • 1h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.1k • 🔱 518 • 25m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 5d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.1k • 🔱 849 • 3d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.8k • 🔱 1.1k • 22d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 181 • 7h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 455 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
