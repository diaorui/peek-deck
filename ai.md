---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-30T14:13:22.796891+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 30, 2026 at 14:13 UTC  
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

**[Mystery company accidentally blew $500 million on Claude AI in a single month — failed to put usage limit on licenses for employees](https://www.reddit.com/r/artificial/comments/1trmvgh/mystery_company_accidentally_blew_500_million_on/)**

A mysterious, unnamed company is reported to have accidentally spent half a billion dollars in a single month on Claude AI after forgetting to set usage limits for Claude licenses for employees.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/mystery-company-accidentally-blew-usd500-million-on-claude-in-a-single-month-failed-to-put-usage-limit-on-licenses-for-employees) • 12h ago

---

**[Ronny Chieng Tells Harvard to ‘Destroy AI’ as Graduates Cheer](https://www.reddit.com/r/artificial/comments/1trfunt/ronny_chieng_tells_harvard_to_destroy_ai_as/)**

The comedian and The Daily Show host gave the keynote address for Class Day 2026.

🔗 [Harvard Magazine](https://www.harvardmagazine.com/commencement/class-day-ronny-chieng-harvard) • 16h ago

---

**[Meta lays off more than 2,000 from Menlo Park headquarters](https://www.reddit.com/r/artificial/comments/1trevkk/meta_lays_off_more_than_2000_from_menlo_park/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/more-meta-layoffs-22282871.php) • 17h ago

---

**[Deep Neural Network that turns any Image into a Playable Game ! All on consumer GPUs and Not Datacenters](https://www.reddit.com/r/artificial/comments/1trs21e/deep_neural_network_that_turns_any_image_into_a/)**

Hi everyone!! I really wanted to share my research what I've been working on. I wanted to build a nn that can simulate games, or at least start doing that Most video generators are too large to run on consumer hardware realtime, so I I designed a model that does this from scratch. No fine tuning bs or anything The core de noiser network is fully trained from scratch to support this goal. From image to games data. That video. above is on a RTX 5090. The nn is a small Transformer-like model and works in a causal way, just like LLMs. That lets us KV Cache all past information and do a simple autoregressive decode forward passes for every new frame we want. In the video shared, the model is a 0.4B variant with some SIGNIFICANT ISSUES like poor motion and some weird flashes, some context issues It's taking the keyboard actions I give it in realtime and utilising that in the forward pass. (no classifier free guidance though) Im training the next iteration , a 0.8B model now. Btw I haven't done quantisation yet, that can save a LOT more time. bf16 is slow.

7h ago

---

**[Weekly AI roundup (May 23–30, 2026): Claude Opus 4.8 Fast Mode 3x cheaper, Qwen 3.7 Max beats Claude at half the price, ChatGPT moves into Excel](https://www.reddit.com/r/artificial/comments/1trz2pd/weekly_ai_roundup_may_2330_2026_claude_opus_48/)**

Pulling together this week's major AI releases for anyone who didn't have time to track every blog post. Sticking to substantive changes, not hype. Anthropic — Claude Opus 4.8 Released this week. Headline pricing unchanged, but Fast Mode dropped from $30 input / $150 output per million tokens to $10 / $50 — a 3x reduction on the premium tier. Reported improvements in "judgment" and longer autonomous runs. Also shipped 20+ legal MCP connectors and Microsoft 365 add-ins (Excel, PowerPoint, Word) in GA. Alibaba — Qwen 3.7 Max Launched May 20 at Alibaba Cloud Summit. 1M-token context. Reported to top Claude Opus 4.6 Max on Terminal-Bench 2.0, SWE-Bench Pro, and MCP-Atlas. Pricing $2.50 / $7.50 per million tokens — roughly half of Opus 4.7. Alibaba claims autonomous operation up to 35 hours without performance degradation. Alibaba is now ranked #6 lab globally on Arena text leaderboard. OpenAI — GPT-5.5 Instant Now default in ChatGPT. Reports 52.5% fewer hallucinated claims than GPT-5.3 Instant on high-stakes prompts (medicine, law, finance). OpenAI also shipped a ChatGPT sidebar inside Excel and Google Sheets, plus a personal finance dashboard for Pro users (US only). Google — Gemini 3.5 Flash Reported to beat Gemini 3.1 Pro on coding and agentic benchmarks at ~4x faster output token rate. Ultra subscription cut from $250 to $200/month; new $100/month Developer tier introduced. xAI — Grok Build 0.1 Coding agent moved to public API beta May 28. Custom Skills feature added for reusable user-defined tasks. Connectors for SharePoint, OneDrive, Notion, GitHub, Linear, plus bring-your-own MCP support. Mistral Launched Vibe (unified work + code agent, replaces Le Chat). Acquired Emmi AI for physics-based simulation. Targeting €1B revenue in 2026; new 10MW inference DC announced. Hugging Face Launched an app store for the Reachy Mini robot. ~10,000 units shipped. Also reported a malicious repo masquerading as an OpenAI release that accumulated 244K downloads before takedown — relevant for anyone pinning models from HF in production. My take as someone building on top of these APIs: The 3x Opus Fast Mode price cut and Qwen 3.7 Max's pricing + autonomous duration are the real signal this week. The cost floor on premium-tier inference is dropping faster than most app-layer products have repriced for. Anyone running multi-step agent workflows needs to recompute unit economics this week — either pass through the savings or reinvest the margin. The other pattern worth noting: OpenAI and Anthropic are both pushing into Excel/M365 surfaces. Distribution is becoming the next battleground, not raw model capability. If you're building a productivity SaaS, the giants are now inside the same surface as you.

1h ago

---

**[Your brain does on 20 watts what AI needs a nuclear reactor to attempt. Last week a team figured out how to print something that actually speaks to living brain cells.](https://www.reddit.com/r/artificial/comments/1tr4kau/your_brain_does_on_20_watts_what_ai_needs_a/)**

Amazon bought a 960 megawatt nuclear reactor for AI servers. Microsoft restarted Three Mile Island. Stargate is spending 500 billion dollars on data centres. All of this to do, badly, what your brain does for free on the power of a dim light bulb. The reason is that silicon processes information nothing like the brain does. Rigid chips with identical transistors trying to mimic something soft, three dimensional, constantly rewiring itself, with billions of different neurons each doing something slightly different. Northwestern University just published research showing they printed artificial neurons from MoS2 and graphene ink that produced biologically realistic electrical spikes. They tested on living mouse brain cells. The brain responded as if the signal came from one of its own cells. The breakthrough was accidental. Every other lab had been burning away the polymer residue left in the ink after printing. This team kept it. That residue created the switching behaviour that made the spikes biologically realistic. The neuromorphic computing implications here seem significant. If you can print devices that process information the way neurons do at scale, the energy math changes completely.

23h ago

---

**[Building an Agent with the Cline SDK](https://www.reddit.com/r/artificial/comments/1trxwyx/building_an_agent_with_the_cline_sdk/)**

In this article, we will build a small release notes generator that uses the Cline SDK to inspect recent git history and turn it into readable markdown.

🔗 [packagemain.tech](https://packagemain.tech/p/building-an-agent-with-the-cline-sdk) • 2h ago

---

**[I made an Epstein Files RAG](https://www.reddit.com/r/artificial/comments/1trq0p9/i_made_an_epstein_files_rag/)**

A lot of people talk about the Epstein files. Almost nobody actually reads them. So I made a searchable version where you can just ask questions naturally instead of digging through thousands of pages manually. You can explore names, timelines, mentions, connections, locations, etc. way faster now. Repo: https://github.com/AbhisumatK/Epstein\_Files\_RAG

🔗 [GitHub](https://github.com/AbhisumatK/Epstein_Files_RAG) • 9h ago

---

**[We wrote an open-source interactive playbook for Agentic DevOps (How to move multi-agent systems from local notebooks to production).](https://www.reddit.com/r/artificial/comments/1trxgvc/we_wrote_an_opensource_interactive_playbook_for/)**

Hey everyone, If you’ve built a multi-agent system, you already know the painful truth: wiring nodes together locally is fun, but deploying them is an absolute infrastructure nightmare. When a standard app fails, it throws a 500 error. When an autonomous swarm fails, it can get stuck in a ReAct loop, hallucinate an answer, and quietly burn through your API budget without triggering a single traditional alert. Standard DevOps practices don't natively map to stochastic AI outputs. We just published a massive, no-fluff playbook on the AgentSwarms blog detailing exactly how to build an Agentic DevOps pipeline using entirely open-source tooling. Here is what we cover in the playbook: Observability & Tracing: Why standard logging fails, and how to implement open-source tracing to capture the state, prompt, token count, and latency at every single node handoff. Test-Driven Prompt Evals (CI/CD): You can't just change a system prompt based on "vibes" and push it to main. We break down how to run matrix evaluations against historical user inputs before deployment to catch regressions instantly. Deterministic Guardrails: How to implement middleware that scrubs PII and blocks destructive code execution before the LLM even sees the state. Cost Control & Routing: How to prevent vendor lock-in and implement dynamic routing to keep token economics from destroying your cloud budget. If you are currently wrestling with the deployment phase of your AI projects, I highly recommend giving this a read. It focuses entirely on open-source solutions so you don't have to sign a massive enterprise contract just to get visibility into your swarms. Would love to hear what open-source tools you guys are currently slotting into your LLMOps pipelines! Link: https://agentswarms.fyi/blog/devops-for-agentic-ai-open-source-playbook

2h ago

---

**[G7 agrees on shared language around open-source AI, open weights AI](https://www.reddit.com/r/artificial/comments/1trx8p4/g7_agrees_on_shared_language_around_opensource_ai/)**

Ahead of the 52nd G7 Summit being held in Evian, France next month, the recently conducted G7 Digital and Technology Ministers’ Meeting came to agreement on shared language around open-source AI and on the importance of open-source in AI.

🔗 [phoronix.com](https://www.phoronix.com/news/G7-On-Open-Source-AI) • 2h ago

---

---

## Google News: "ai"

**["The pitchforks are here": Billionaires work to contain AI's populist revolt](https://www.axios.com/2026/05/29/ai-billionaires-tech-taxes-wealth)**

Axios • 15h ago

---

**[Should AI steal your job?](https://www.ft.com/content/aceabeb1-1152-43d1-ad76-e1531cd37f39?syn-25a6b1a6=1)**

The real question is not what the technology can do but what it ought to do. Sarah O’Connor on the people fighting for the future of work

Financial Times • 10h ago

---

**[Ukraine using AI drones to strike vital convoys supplying Russian troops](https://www.bbc.com/news/articles/cdjp0n7rn41o)**

BBC Verify has analysed videos of attacks in occupied Ukraine on Russian trucks carrying ammunition, fuel and food.

BBC • 12h ago

---

**[Opinion | The First A.I. High School in the U.S. Is Surprisingly Human](https://www.nytimes.com/2026/05/30/opinion/ai-high-school.html)**

The New York Times • 3h ago

---

**[The NTSB tries to keep cockpit audio recordings private. AI is making that harder](https://www.npr.org/2026/05/30/nx-s1-5835242/ntsb-cockpit-audio-cvr-reconstruction)**

The National Transportation Safety Board temporarily pulled its docket system offline after digital images were used to reconstruct cockpit voice recordings of the pilots in a recent crash.

NPR • 4h ago

---

**[Meta has struggled at selling anything other than ads. Will AI be different?](https://www.cnbc.com/2026/05/30/meta-struggled-selling-anything-other-than-ads-will-ai-be-different.html)**

Meta is making a major push to expand its business beyond online advertising, but past efforts show that success is far from guaranteed.

CNBC • 2h ago

---

**[The Feeling of Control Slipping Away](https://www.theatlantic.com/technology/2026/05/ai-agents-agency-crisis-humanity/687379/)**

AI is causing a crisis of agency.

The Atlantic • 3h ago

---

**[Anthropic’s alliance with pope on AI harms: all in good faith or ‘Vatican-washing?’](https://www.theguardian.com/technology/2026/may/30/pope-leo-anthropic-ai)**

Experts say AI firm’s engagement with Vatican risks creating ‘feelgood’ discourse that lacks critical examination

The Guardian • 1h ago

---

**[The Pope and Anthropic agree: AI Companies cannot govern this alone](https://fortune.com/2026/05/30/ai-governance-pope-leo-anthropic-fatf-framework-shlomit-wagman/)**

A Harvard fellow and former financial intelligence chief argues the right model for AI governance isn't nuclear arms control — it's the global framework that brought down ISIS financing.

Fortune • 5h ago

---

**[The Pope’s Admirers Are Missing Something](https://www.theatlantic.com/ideas/2026/05/pope-leo-ai-big-tech/687375/)**

Leo’s new encyclical challenges much more than Big Tech.

The Atlantic • 2h ago

---

---

## HackerNews: "ai"

**[YouTube to automatically label AI-generated videos](https://news.ycombinator.com/item?id=48299753)**

We've heard consistently from our community that they value transparency when it comes to generative AI content. Two new updates will make this process much simpler and more intuitive for creators and viewers on YouTube.

⬆️ 1308 • 💬 819 • 2d ago • [blog.youtube](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/)

---

**[DuckDuckGo search saw 28% more visits after Google said people love AI mode](https://news.ycombinator.com/item?id=48296649)**

"People just want a choice."

⬆️ 1067 • 💬 518 • 2d ago • [PC Gamer](https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/)

---

**[Please Use AI](https://news.ycombinator.com/item?id=48323101)**

⬆️ 752 • 💬 384 • 1d ago • [shawnsmucker.substack.com](https://shawnsmucker.substack.com/p/please-use-ai)

---

**[Tech CEOs are apparently suffering from AI psychosis](https://news.ycombinator.com/item?id=48295679)**

"CEOs are uniquely prone to AI psychosis," Box CEO Aaron Levie opines. Maybe that explains the almost religious belief in AI productivity gains.

⬆️ 716 • 💬 355 • 2d ago • [TechCrunch](https://techcrunch.com/2026/05/27/tech-ceos-are-apparently-suffering-from-ai-psychosis/)

---

**[Notes from the Mistral AI Now Summit](https://news.ycombinator.com/item?id=48325340)**

A few days in Paris for the Mistral AI Now Summit: open models, on-prem deployment, agentic harnesses, and why Mistral wants to be the European full-stack AI partner.

⬆️ 405 • 💬 176 • 21h ago • [koenvangilst.nl](https://koenvangilst.nl/lab/mistral-ai-now-summit)

---

**[Is AI causing a repeat of frontend’s lost decade?](https://news.ycombinator.com/item?id=48321631)**

AI is doing to programming what framework-brain did to the frontend before. Deskilling, or just working at a higher level of abstraction?

⬆️ 384 • 💬 318 • 1d ago • [mastrojs.github.io](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

---

**[Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue](https://news.ycombinator.com/item?id=48308376)**

A 30-second game about LLM permission fatigue. How carefully do you really read AI commands?

⬆️ 376 • 💬 156 • 2d ago • [llmgame.scalex.dev](https://llmgame.scalex.dev)

---

**[SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims](https://news.ycombinator.com/item?id=48317093)**

The guests behind the bookings have received negative reviews from a number of Bay Area hosts, alleging they damaged the property and personal belongings.

⬆️ 263 • 💬 148 • 1d ago • [sfstandard.com](https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/)

---

**[Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions](https://news.ycombinator.com/item?id=48314363)**

Some leaders like Goldman Sachs’s David Solomon and Box’s Aaron Levie have been saying all along that there won’t be a white-collar wipeout.

⬆️ 232 • 💬 179 • 1d ago • [Fortune](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)

---

**[Training our own AI models](https://news.ycombinator.com/item?id=48296359)**

I really think we're on the verge of some of our best work through the next six months. Over the past year, we've started building more AI-powered…

⬆️ 215 • 💬 143 • 2d ago • [posthog.com](https://posthog.com/blog/training-ai-models)

---

---

## YouTube Videos: "ai"

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 14K • 👍 470 • 💬 53 • ⏱️ 1:32:36 • 3h ago

---

**[I Asked Grok AI To Predict The 2028 Election... LANDSLIDE Incoming!](https://www.youtube.com/watch?v=hqTezFeXrlA)**

Pollsmax* 》https://www.pollsmax.com/ ...

📺 Election Time

👁️ 71K • 👍 3K • 💬 430 • ⏱️ 18:32 • 20h ago

---

**[How Helpful Is A.I. ACTUALLY? Here’s The Truth](https://www.youtube.com/watch?v=M4eKkEmuoXo)**

Mack Weldon - Go to MackWeldon.com and get 20% off your first order of $125 or more, with promo code WALSH. AI is repeatedly ...

📺 Matt Walsh

👁️ 35K • 👍 2K • 💬 512 • ⏱️ 9:44 • 1d ago

---

**[Seedance 2.0 + Claude Changed How I Make AI Videos](https://www.youtube.com/watch?v=Nqifd6VHU1k)**

Start creating with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=robo18 In this video, I show how I use Claude with Seedance ...

📺 Roboverse

👁️ 4K • ⏱️ 16:13 • 1h ago

---

**[I Created an Army of AI Influencers With Higgsfield Supercomputer](https://www.youtube.com/watch?v=kXo2_X5Z9Uw)**

Create Your Own Army of AI Influencers with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=isa17 In this video, I build a full ...

📺 Isa does AI

👁️ 5K • ⏱️ 11:28 • 2h ago

---

**[AI Data Centers (This is Disturbing)](https://www.youtube.com/watch?v=9sGEzO-sXH8)**

Due to the ability to earn higher profits through increased electric usage for Power Companies, it's no wonder Power Companies ...

📺 EKE ACRES

👁️ 10K • 💬 206 • ⏱️ 3:40 • 1d ago

---

**[AI Whistleblower WARNS: You Have NO Idea About The AI Wave That Is Coming](https://www.youtube.com/watch?v=fo2ggNE-44g)**

Eliezer Yudkowsky, who has spent 30 years on the AI safety problem, makes a firm prediction: if anyone builds a superintelligence ...

📺 Neural Nutshell

👁️ 19K • 👍 549 • 💬 127 • ⏱️ 22:04 • 2d ago

---

**[If you’re trying to get rich with AI, you need to hear this…](https://www.youtube.com/watch?v=TWuzAO7ukk0)**

Want my AI Tech Stack? Get it here: https://go.danmartell.com/4nUvaZi Are you building an AI software company? Partner with ...

📺 Dan Martell

👁️ 58K • 👍 2K • 💬 106 • ⏱️ 14:06 • 2d ago

---

**[They Are Building A &quot;New God&quot; | Revelation 13 and the AI Image Of The Beast](https://www.youtube.com/watch?v=ErNmkFo0COw)**

They are building an ai god, is this the image of the beast from Revelation 13? Today I look at this end times prophecy from the ...

📺 Sling and Stone

👁️ 16K • 👍 2K • 💬 325 • ⏱️ 16:13 • 1d ago

---

**[Google Just Dropped The Singularity Bomb](https://www.youtube.com/watch?v=BH5_FEJNOGY)**

Google DeepMind's Demis Hassabis says humanity may already be standing in the foothills of the singularity. AI agents are now ...

📺 AI Revolution

👁️ 46K • 👍 2K • 💬 186 • ⏱️ 13:24 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 28,793 • ❤️ 589 • 4d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 18,327 • ❤️ 454 • 3d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 399 • 4d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,227,885 • ❤️ 1,083 • 1mo ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,856 • ❤️ 978 • 2d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 17,084 • ❤️ 245 • 4h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,918,111 • ❤️ 4,452 • 24d ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 437 • ❤️ 187 • 4d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 15,780 • ❤️ 450 • 5h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 138,118 • ❤️ 416 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 204 • 💬 3 • ⭐ 3,086 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 80,706 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 27,494 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 44 • 💬 2 • ⭐ 356 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 5 • 💬 0 • ⭐ 1,346 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,651 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 14 • 💬 2 • ⭐ 2,493 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 86 • 💬 3 • ⭐ 1,497 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,357 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 128 • 💬 8 • ⭐ 78,997 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.4k • 🔱 540 • 1d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.0k • 🔱 628 • 1h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.8k • 🔱 190 • 3h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 399 • 8d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 358 • 13d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.1k • 🔱 190 • 1d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.1k • 🔱 141 • 51m ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.0k • 🔱 208 • 5d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 227 • 23d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 209 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
