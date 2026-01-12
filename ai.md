---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-12T23:40:27.795919+00:00'
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

**Last Updated:** January 12, 2026 at 23:40 UTC  
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

**[Geoffrey Hinton says agents can share knowledge at a scale far beyond humans. 10,000 agents can study different topics, sync their learnings instantly, and all improve together. "Imagine if 10,000 students each took a different course, and when they finish, each student knows all the courses."](https://www.reddit.com/r/artificial/comments/1qb0rry/geoffrey_hinton_says_agents_can_share_knowledge/)**

6h ago

---

**[Cowork: Claude Code for the rest of your work](https://www.reddit.com/r/artificial/comments/1qb5xxv/cowork_claude_code_for_the_rest_of_your_work/)**

Claude Code's agentic capabilities, now for everyone. Give Claude access to your files and let it organize, create, and edit documents while you focus on what matters.

🔗 [claude.com](https://claude.com/blog/cowork-research-preview) • 3h ago

---

**[China is closing in on US technology lead despite constraints, AI researchers say](https://www.reddit.com/r/artificial/comments/1qae670/china_is_closing_in_on_us_technology_lead_despite/)**

By Laurie Chen BEIJING, Jan 10 (Reuters) - China can narrow its technological gap with the U.S. driven by growing risk-taking and innovation, though the lack of advanced chipmaking tools is hobbling

🔗 [Yahoo Tech](https://tech.yahoo.com/ai/articles/china-closing-us-technology-lead-154328876.html) • 1d ago

---

**[The Intelligence Paradox: Why centralized AI is hitting a "Power Wall" and the case for decentralized inference hubs](https://www.reddit.com/r/artificial/comments/1qb46h5/the_intelligence_paradox_why_centralized_ai_is/)**

As we scale to GPT-5.2 and beyond, the energy footprint of centralized data centers in the US is becoming a physical limit. I'm theorizing that the next step isn't "bigger models," but smarter routing to specialized, regionally-hosted inference hubs. If we can't shrink the models, we must optimize the path to the user. I'm curious about the community's take on "Inference-at-the-edge" for LLMs. Is the future a single global brain, or a fragmented network of sovereign AI nodes?

4h ago

---

**[I built Plano - the framework-agnostic runtime data plane for agentic applications](https://www.reddit.com/r/artificial/comments/1qafw8d/i_built_plano_the_frameworkagnostic_runtime_data/)**

Thrilled to be launching Plano today - delivery infrastructure for agentic apps: An edge and service proxy server with orchestration for AI agents. Plano's core purpose is to offload all the plumbing work required to deliver agents to production so that developers can stay focused on core product logic. Plano runs alongside your app servers (cloud, on-prem, or local dev) deployed as a side-car, and leaves GPUs where your models are hosted. The problem On the ground AI practitioners will tell you that calling an LLM is not the hard part. The really hard part is delivering agentic applications to production quickly and reliably, then iterating without rewriting system code every time. In practice, teams keep rebuilding the same concerns that sit outside any single agent’s core logic: This includes model agility - the ability to pull from a large set of LLMs and swap providers without refactoring prompts or streaming handlers. Developers need to learn from production by collecting signals and traces that tell them what to fix. They also need consistent policy enforcement for moderation and jailbreak protection, rather than sprinkling hooks across codebases. And they need multi-agent patterns to improve performance and latency without turning their app into orchestration glue. These concerns get rebuilt and maintained inside fast-changing frameworks and application code, coupling product logic to infrastructure decisions. It’s brittle, and pulls teams away from core product work into plumbing they shouldn’t have to own. What Plano does Plano moves core delivery concerns out of process into a modular proxy and dataplane designed for agents. It supports inbound listeners (agent orchestration, safety and moderation hooks), outbound listeners (hosted or API-based LLM routing), or both together. Plano provides the following capabilities via a unified dataplane: - Orchestration: Low-latency routing and handoff between agents. Add or change agents without modifying app code, and evolve strategies centrally instead of duplicating logic across services. - Guardrails & Memory Hooks: Apply jailbreak protection, content policies, and context workflows (rewriting, retrieval, redaction) once via filter chains. This centralizes governance and ensures consistent behavior across your stack. - Model Agility: Route by model name, semantic alias, or preference-based policies. Swap or add models without refactoring prompts, tool calls, or streaming handlers. - Agentic Signals™: Zero-code capture of behavior signals, traces, and metrics across every agent, surfacing traces, token usage, and learning signals in one place. The goal is to keep application code focused on product logic while Plano owns delivery mechanics. More on Architecture Plano has two main parts: Envoy-based data plane. Uses Envoy’s HTTP connection management to talk to model APIs, services, and tool backends. We didn’t build a separate model server—Envoy already handles streaming, retries, timeouts, and connection pooling. Some of us are core Envoy contributors at Katanemo. Brightstaff, a lightweight controller and state machine written in Rust. It inspects prompts and conversation state, decides which agents to call and in what order, and coordinates routing and fallback. It uses small LLMs (1–4B parameters) trained for constrained routing and orchestration. These models do not generate responses and fall back to static policies on failure. The models are open sourced here: https://huggingface.co/katanemo

🔗 [GitHub](https://github.com/katanemo/plano) • 23h ago

---

**[Is the snake eating its tail yet?](https://www.reddit.com/r/artificial/comments/1qb3wek/is_the_snake_eating_its_tail_yet/)**

Found an article about a professor who used an AI bot to administer an oral exam to students because they were using AI to do school work. He them proceeded to have the AI bot grade the real exam. And now, an AI bot has found and summarized this news for me to read quicker. I guess all that's missing is to have an AI bot read this summary and react to it. Wait a minute... Source: Yahoo https://search.app/vWcje

4h ago

---

**[What is something current AI systems are very good at, but people still don’t trust them to do?](https://www.reddit.com/r/artificial/comments/1qakw7h/what_is_something_current_ai_systems_are_very/)**

We see benchmarks and demos showing strong performance, but hesitation still shows up in real use. Curious where people draw the trust line and why, whether it’s technical limits, incentives, or just human psychology.

19h ago

---

**[The bottleneck isn't AI capability anymore. It's human reception.](https://www.reddit.com/r/artificial/comments/1qb2u2s/the_bottleneck_isnt_ai_capability_anymore_its/)**

Somewhere between GPT-3.5 and Claude 3, something shifted. AI capability stopped being the constraint. The new bottleneck: Can humans understand enough to decide with confidence? After 416K messages over 2.5 years, I packaged this thesis into a "seed" — a JSON you paste into any LLM. Type "unpack" and explore 17 themes at your own pace. The singularity can't happen. Not because AI isn't smart enough. Because humans won't use what they can't verify. https://github.com/mordechaipotash/thesis

5h ago

---

**[Multimodal LLMs are the real future of AI (especially for robotics)](https://www.reddit.com/r/artificial/comments/1qasdce/multimodal_llms_are_the_real_future_of_ai/)**

I strongly believe multimodal LLMs (AI that can understand text, images, audio, and actions) are the next big step in AI. Right now, most LLMs are mainly used for chatting. But I think the real breakthrough will happen in robotics, where AI needs to see, hear, and act in the real world. Think about it: Every robot already has (or will have) sensors: Cameras (drones, vehicles, humanoid robots) Microphones Depth sensors / LiDAR GPS / IMU Maybe even tactile sensors A robot doesn’t just need to talk, it needs to: see the world understand scenes reason about physical space plan actions and execute in real-time And multimodal models are basically built for this. I feel like as robotics advances accelerate, the demand for multimodal intelligence is going to explode, because robots are not operating inside a browser, they’re operating in the real world. I’m building in this space. What’s your opinion on the future of multimodal LLMs?

12h ago

---

**[Geoffrey Hinton says LLMs are no longer just predicting the next word - new models learn by reasoning and identifying contradictions in their own logic. This unbounded self-improvement will "end up making it much smarter than us."](https://www.reddit.com/r/artificial/comments/1q9an1z/geoffrey_hinton_says_llms_are_no_longer_just/)**

2d ago

---

---

## Google News: "ai"

**[UK media regulator investigating Elon Musk’s X after outcry over sexualised AI images](https://www.theguardian.com/technology/2026/jan/12/ofcom-investigating-x-outcry-sexualised-ai-images-grok-elon-musk)**

Media regulator investigating site under Online Safety Act, with a de facto ban among possible punishments

The Guardian • 12h ago

---

**[Google Bets on AI-Based Shopping With New AI Agents for Retailers](https://www.wsj.com/articles/google-bets-on-ai-based-shopping-with-new-ai-agents-for-retailers-45ad3f27?gaa_at=eafs&gaa_n=AWEtsqc13yYfMtDxKUxMoOnXIZ3YDatkbaPDY0mKNU1yoq9gbQ6joz8vMTZR&gaa_ts=696589c5&gaa_sig=3YeYKhJTCT8sclxW3aDWDX0rD4BLFG8bgYsBi49k7Yau8Dzfp6fkcswuAyeNxfTWFecnMyEj1z5bkgto18iFeA%3D%3D)**

The Wall Street Journal • 1d ago

---

**[‘Dangerous and alarming’: Google removes some of its AI summaries after users’ health put at risk](https://www.theguardian.com/technology/2026/jan/11/google-ai-overviews-health-guardian-investigation)**

Guardian investigation finds AI Overviews provided inaccurate and false information when queried over blood tests

The Guardian • 21h ago

---

**[Apple Picks Gemini to Run AI-Powered Siri | Bloomberg Tech 1/12/2026](https://www.bloomberg.com/news/videos/2026-01-12/bloomberg-tech-1-12-2026-video)**

Bloomberg.com • 1h ago

---

**[Why Amazon bought Bee, an AI wearable](https://techcrunch.com/2026/01/12/why-amazon-bought-bee-an-ai-wearable/)**

Amazon explains where its wearable Bee fits in and whether it will merge with Alexa.

TechCrunch • 1h ago

---

**[Central Florida senator proposes AI bill to protect kids and personal data](https://www.wesh.com/article/central-florida-senator-proposes-ai-bill-protect-kids/69980259)**

State Sen. Tom Leek, a Republican from Volusia County, filed a proposal he calls an AI Bill of Rights.

WESH • 36m ago

---

**[New EHR and patient record integrations with Claude AI](https://www.healthcareitnews.com/news/new-ehr-and-patient-record-integrations-claude-ai)**

Elation Health and HealthEx announced they are integrating Anthropic's Claude artificial intelligence to better synthesize health data for doctors and patients.

Healthcare IT News • 1h ago

---

**[This CEO laid off nearly 80% of his staff because they refused to adopt AI fast enough. 2 years later, he says he’d do it again](https://finance.yahoo.com/news/ceo-laid-off-nearly-80-185033733.html)**

“It was extremely difficult,” IgniteTech CEO Eric Vaughan tells Fortune. “But changing minds was harder than adding skills.”

Yahoo Finance • 1d ago

---

**[AI can now 'see' optical illusions. What does it tell us about our own brains?](https://www.bbc.com/future/article/20251218-how-ai-is-shedding-new-light-on-optical-illusions)**

Our eyes can frequently play tricks on us, but scientists have discovered that some artificial intelligence can fall for the same illusions.

BBC • 13h ago

---

**[The Dangerous Paradox of A.I. Abundance](https://www.newyorker.com/news/the-financial-page/the-dangerous-paradox-of-ai-abundance)**

Silicon Valley envisions artificial intelligence ushering in an era of economic plenty. But what if the benefits are largely confined to corporations and investors that own the technology itself?

The New Yorker • 12h ago

---

---

## HackerNews: "ai"

**[Don't fall into the anti-AI hype](https://news.ycombinator.com/item?id=46574276)**

⬆️ 1185 • 💬 1522 • 1d ago • [antirez.com](https://antirez.com/news/158)

---

**[AI is a business model stress test](https://news.ycombinator.com/item?id=46567392)**

AI commoditizes anything you can specify. It can't commoditize what you have to operate.

⬆️ 337 • 💬 330 • 2d ago • [dri.es](https://dri.es/ai-is-a-business-model-stress-test)

---

**[Ai, Japanese chimpanzee who counted and painted dies at 49](https://news.ycombinator.com/item?id=46585947)**

Ai's cognitive abilities had been studied extensively since she was brought to a Japanese institute in 1977.

⬆️ 166 • 💬 55 • 14h ago • [bbc.com](https://www.bbc.com/news/articles/cj9r3zl2ywyo)

---

**[The chess bot on Delta Air Lines will destroy you (2024) [video]](https://news.ycombinator.com/item?id=46593395)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 110 • 💬 52 • 3h ago • [youtube.com](https://www.youtube.com/watch?v=c0mLhHDcY3I)

---

**[Show HN: AI in SolidWorks](https://news.ycombinator.com/item?id=46591100)**

Create and modify SolidWorks 3D models through natural language with LAD's AI-powered CAD assistant.

⬆️ 98 • 💬 48 • 6h ago • [TryLAD](https://www.trylad.com)

---

**[Show HN: Yolobox – Run AI coding agents with full sudo without nuking home dir](https://news.ycombinator.com/item?id=46592344)**

Let your AI go full send. Your home directory stays home. - finbarr/yolobox

⬆️ 44 • 💬 39 • 5h ago • [GitHub](https://github.com/finbarr/yolobox)

---

**[Show HN: GlyphLang – An AI-first programming language](https://news.ycombinator.com/item?id=46571166)**

⬆️ 42 • 💬 25 • 1d ago

---

**[UK threatens action against X over sexualised AI images of women and children](https://news.ycombinator.com/item?id=46586334)**

Government signals support for possible Ofcom intervention on Grok as scrutiny of X’s AI tool intensifies

⬆️ 33 • 💬 43 • 13h ago • [the Guardian](https://www.theguardian.com/technology/2026/jan/12/uk-threatens-action-against-x-over-sexualised-ai-images-of-women-and-children)

---

**[Ask HN: Senior engineering mngrs: how has AI changed your day-to-day work?](https://news.ycombinator.com/item?id=46565262)**

⬆️ 33 • 💬 7 • 2d ago

---

**[Show HN: What if AI agents had Zodiac personalities?](https://news.ycombinator.com/item?id=46581832)**

AI agents with different personalities responding to moral dilemmas - baturyilmaz/what-if-ai-agents-had-zodiac-personalities

⬆️ 29 • 💬 16 • 23h ago • [GitHub](https://github.com/baturyilmaz/what-if-ai-agents-had-zodiac-personalities)

---

---

## YouTube Videos: "ai"

**[The $1.5 Billion Anthropic Lawsuit That Could Change AI Forever](https://www.youtube.com/watch?v=XQXVA5M9AUk)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *The ...

📺 Julia McCoy

👁️ 11K • 👍 809 • 💬 94 • ⏱️ 10:39 • 8h ago

---

**[we just arrived at the &quot;WTF&quot; moment in AI](https://www.youtube.com/watch?v=N8I2wYXt4m8)**

GPT 5.2 just solved the Erdos Problems. Terence Tao confirms. We're officially at the "WTF" moment in AI development. The latest ...

📺 Wes Roth

👁️ 71K • 👍 3K • 💬 595 • ⏱️ 23:05 • 19h ago

---

**[Wired&#39;s Steven Levy on DeepSeek&#39;s latest AI model, state of AI tech race](https://www.youtube.com/watch?v=_67YjLqjYbk)**

Steven Levy, Wired editor-at-large, joins 'Squawk Box' to discuss what to expect from Chinese AI startup DeepSeek's latest model, ...

📺 CNBC Television

👁️ 22K • 👍 222 • 💬 51 • ⏱️ 7:57 • 9h ago

---

**[Every Way To Get Rich With AI in 2026 (Explained in 10mins)](https://www.youtube.com/watch?v=mZecvMwmvGk)**

The Join the #1 community for AI entrepreneurs and connect with 280k+ members: https://bit.ly/4pQ0dpc We help ...

📺 Liam Ottley

👁️ 14K • 👍 982 • 💬 60 • ⏱️ 10:29 • 16h ago

---

**[I Asked AI If It Supports the Operation in Venezuela. And Here’s What It Said](https://www.youtube.com/watch?v=BLLa0DblYaE)**

In this video, I ask AI what it thinks about the U.S. military operation in Venezuela, the real reason behind the capture of Nicolas ...

📺 I Ask AI

👁️ 14K • 👍 3K • 💬 325 • ⏱️ 14:02 • 2d ago

---

**[AI has gotten out of hand... (The Beast System)](https://www.youtube.com/watch?v=3468sgevZiU)**

Every month, it feels like a new update, model, or software hits the scene, and people are quick to either claim it's groundbreaking ...

📺 Seethruthescript

👁️ 2K • 👍 203 • 💬 61 • ⏱️ 24:00 • 1d ago

---

**[AI Hype](https://www.youtube.com/watch?v=90XC-Of43eE)**

The next episode of my AI series. The AI character is making using AI, but is still pretty heavily edited. Everything else done ...

📺 Nate Ziller

👁️ 281K • 👍 28K • 💬 2K • ⏱️ 4:38 • 2d ago

---

**[The Biggest AI News Updates Were NOT at CES](https://www.youtube.com/watch?v=LhpCVkDpYZM)**

LTX 2 Open-Source has officially launched! Explore the open-source release today: https://ltx.io/model I thought this week would ...

📺 Matt Wolfe

👁️ 64K • 👍 2K • 💬 170 • ⏱️ 14:39 • 2d ago

---

**[Did AI Just Solve an Erdős Problem? (This Changes Everything)](https://www.youtube.com/watch?v=5DUabMi02js)**

In recent days, multiple Erdős problems have been solved by GPT-5.2 Pro, with solutions accepted by Terence Tao. This is not a ...

📺 Dr Brian Keating

👁️ 8K • 👍 204 • 💬 25 • ⏱️ 5:50 • 1d ago

---

**[Open Source AI Agents Just Got Too Powerful: Confucius AI Agent](https://www.youtube.com/watch?v=GnQCyxa4TjA)**

Meta and Harvard just released an open-source coding agent called Confucius Code Agent, built on top of the Confucius SDK, ...

📺 AI Revolution

👁️ 30K • 👍 993 • 💬 42 • ⏱️ 14:29 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 735,985 • ❤️ 851 • 4d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 23,889 • ❤️ 508 • 5d ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 10,682 • ❤️ 730 • 11d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 2,687 • ❤️ 320 • 6d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 12,797 • ❤️ 290 • 3d ago

---

**[LFM2.5-Audio-1.5B](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B)**

*Liquid AI*

LFM2.5-Audio-1.5B is an end-to-end audio foundation model enabling real-time speech-to-speech conversational interactions with low latency. It supports interleaved and sequential generation for tasks like ASR, TTS, and seamless chatbot conversations.

`audio-to-audio` `1.5B`

⬇️ 670 • ❤️ 226 • 6d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 30,603 • ❤️ 360 • 6d ago

---

**[Alpamayo-R1-10B](https://huggingface.co/nvidia/Alpamayo-R1-10B)**

*NVIDIA*

Alpamayo-R1-10B is a Vision-Language-Action (VLA) Transformer model for autonomous driving, integrating Chain-of-Causation reasoning with diffusion-based trajectory planning for complex scenarios and rare events. It processes multi-camera images, text commands, and egomotion history to output interpretable reasoning traces and a 6.4-second future trajectory.

`robotics` `11.1B`

⬇️ 13,820 • ❤️ 270 • 4d ago

---

**[LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy)**

*Jukka Seppänen*

LTXV2_comfy is a separated checkpoint model designed for ComfyUI, enabling an alternative method for loading LTX2 models. It is compatible with LTX2 GGUFs that include metadata, though it may require a specific PR for ComfyUI-GGUF nodes.

`18.9B`

⬇️ 23,310 • ❤️ 198 • 2d ago

---

**[Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B)**

*Qwen*

Qwen3-VL-Embedding-8B is a multimodal embedding model that generates high-dimensional vectors from text, images, and videos for tasks like retrieval and clustering. It supports over 30 languages and customizable embedding dimensions, enabling efficient cross-modal understanding and search.

`image-to-text` `8.1B`

⬇️ 19,641 • ❤️ 183 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 174 • 💬 5 • ⭐ 4,585 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 100 • 💬 1 • ⭐ 2,139 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[Thinking with Map: Reinforced Parallel Map-Augmented Agent for Geolocalization](https://huggingface.co/papers/2601.05432)**

*Yuxiang Ji, Yong Wang, Ziyu Ma et al. (9 authors)*

🏢 alibaba-inc

Large vision-language models are enhanced for image geolocalization by incorporating map-based reasoning and agent-in-the-map loop optimization, achieving superior accuracy compared to existing models.

▲ 129 • 💬 3 • ⭐ 107 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.05432) • [💻 code](https://github.com/AMAP-ML/Thinking-with-Map) • [🔗 project](https://amap-ml.github.io/Thinking-with-Map/)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 23 • 💬 2 • ⭐ 824 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking](https://huggingface.co/papers/2601.04720)**

*Mingxin Li, Yanzhao Zhang, Dingkun Long et al. (12 authors)*

🏢 Qwen

The Qwen3-VL-Embedding and Qwen3-VL-Reranker models form an end-to-end multimodal search pipeline, leveraging multi-stage training and cross-attention mechanisms to achieve high-precision retrieval across diverse modalities.

▲ 20 • 💬 1 • ⭐ 620 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.04720) • [💻 code](https://github.com/QwenLM/Qwen3-VL-Embedding)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 130 • 💬 18 • ⭐ 49,840 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context
  Videos](https://huggingface.co/papers/2502.01549)**

*Xubin Ren, Lingrui Xu, Long Xia et al. (6 authors)*

VideoRAG enhances large language models for multi-modal video processing with a dual-channel architecture that integrates textual knowledge grounding and multi-modal context encoding.

▲ 3 • 💬 0 • ⭐ 2,431 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.01549) • [💻 code](https://github.com/hkuds/videorag)

---

**[Orient Anything V2: Unifying Orientation and Rotation Understanding](https://huggingface.co/papers/2601.05573)**

*Zehan Wang, Ziang Zhang, Jiayang Xu et al. (8 authors)*

Orient Anything V2 enhances 3D orientation understanding through scalable 3D asset synthesis, symmetry-aware periodic distribution fitting, and multi-frame relative rotation prediction, achieving state-of-the-art performance across multiple benchmarks.

▲ 7 • 💬 1 • ⭐ 82 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.05573) • [💻 code](https://github.com/SpatialVision/Orient-Anything-V2) • [🔗 project](https://orient-anythingv2.github.io/)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 19 • 💬 3 • ⭐ 14,915 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 3 • 💬 0 • ⭐ 28,333 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 8.2k • 🔱 1.0k • 7h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 3.3k • 🔱 436 • 5d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.3k • 🔱 139 • 5h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.0k • 🔱 228 • 1d ago

---

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 1.9k • 🔱 66 • 5h ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

Learn vibe coding from 0 to 1 | 从零学会 vibe coding，项目制学习

`ai` `coding` `course` `vibe-coding`

⭐ 1.5k • 🔱 126 • 8h ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.4k • 🔱 73 • 20d ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.3k • 🔱 114 • 2h ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.2k • 🔱 85 • 14d ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.2k • 🔱 143 • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*
