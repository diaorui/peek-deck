---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-09T23:42:30.149223+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 09, 2026 at 23:42 UTC  
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

**[Musk lawsuit over OpenAI for-profit conversion can go to trial, US judge says](https://www.reddit.com/r/artificial/comments/1q82r2v/musk_lawsuit_over_openai_forprofit_conversion_can/)**

Judge says there is plenty of evidence to suggest OpenAI’s leaders made assurances nonprofit structure would be kept

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jan/08/elon-musk-openai-lawsuit-for-profit-conversion-can-go-to-trial-us-judge-says) • 15h ago

---

**[Why Yann LeCun left Meta for World Models](https://www.reddit.com/r/artificial/comments/1q7ugtz/why_yann_lecun_left_meta_for_world_models/)**

As we know, one of the godfathers of AI recently left Meta to found his own lab AMI and the the underlying theme is his longstanding focus on world modelling. This is still a relatively underexplored concept however the recent surge of research suggests why it is gaining traction. For example, Marble demonstrates how multimodal models that encode a sense of the world can achieve far greater efficiency and reasoning capability than LLMs, which are inherently limited to predicting the next token. Genie illustrates how 3D interactive environments can be learned and simulated to support agent planning and reasoning. Other recent work includes SCOPE, which leverages world modelling to match frontier LLM performance (GPT-4-level) with far smaller models (millions versus trillions of parameters), and HunyuanWorld, which scored ~77 on the WorldScore benchmark. There are also new models being developed that push the boundaries of world modelling further. It seems the AI research community is beginning to recognize the practical and theoretical advantages of world models for reasoning, planning, and multimodal understanding. Curious, who else has explored this domain recently? Are there emerging techniques or results in world modelling that you find particularly compelling? Let us discuss. ps: See the comments for references to all the models mentioned above.

22h ago

---

**[Elon Musk's Grok AI image editing limited to paid users after deepfakes](https://www.reddit.com/r/artificial/comments/1q83cyi/elon_musks_grok_ai_image_editing_limited_to_paid/)**

It comes after government urged Ofcom to use all its powers – up to and including an effective ban – against X.

🔗 [bbc.com](https://www.bbc.com/news/articles/c99kn52nx9do) • 14h ago

---

**[A practical 2026 roadmap for modern AI search & RAG systems](https://www.reddit.com/r/artificial/comments/1q87y8e/a_practical_2026_roadmap_for_modern_ai_search_rag/)**

I kept seeing RAG tutorials that stop at “vector DB + prompt” and break down in real systems. I put together a roadmap that reflects how modern AI search actually works: – semantic + hybrid retrieval (sparse + dense) – explicit reranking layers – query understanding & intent – agentic RAG (query decomposition, multi-hop) – data freshness & lifecycle – grounding / hallucination control – evaluation beyond “does it sound right” – production concerns: latency, cost, access control The focus is system design, not frameworks. Language-agnostic by default (Python just as a reference when needed). Roadmap image + interactive version here: https://nemorize.com/roadmaps/2026-modern-ai-search-rag-roadmap Curious what people here think is still missing or overkill.

10h ago

---

**[Built a cognitive framework for AI agents - today it audited itself for release and caught its own bugs](https://www.reddit.com/r/artificial/comments/1q8ankw/built_a_cognitive_framework_for_ai_agents_today/)**

I've been working on a problem: AI agents confidently claim to understand things they don't, make the same mistakes across sessions, and have no awareness of their own knowledge gaps. Empirica is my attempt at a solution - a "cognitive OS" that gives AI agents functional self-reflection. Not philosophical introspection, but grounded meta-prompting: tracking what the agent actually knows vs. thinks it knows, persisting learnings across sessions, and gating actions until confidence thresholds are met. parallel git branch multi agent spawning for investigation What you're seeing: The system spawning 3 parallel investigation agents to audit the codebase for release issues Each agent focusing on a different area (installer, versions, code quality) Agents returning confidence-weighted findings to a parent session The discovery: 4 files had inconsistent version numbers while the README already claimed v1.3.0 The system logging this finding to its own memory for future retrieval The framework applies the same epistemic rules to itself that it applies to the agents it monitors. When it assessed its own release readiness, it used the same confidence vectors (know, uncertainty, context) that it tracks for any task. Key concepts: CASCADE workflow: PREFLIGHT (baseline) → CHECK (gate) → POSTFLIGHT (measure learning) 13 epistemic vectors: Quantified self-assessment (know, uncertainty, context, clarity, etc.) Procedural memory: Findings, dead-ends, and lessons persist in Qdrant for semantic retrieval Sentinel: Gates praxic (action) phases until noetic (investigation) phases reach confidence threshold The framework caught a release blocker by applying its own methodology to itself. Self-referential improvement loops are fascinating territory. I'll leave the philosophical questions to you. What I can show you: the system tracks its own knowledge state, adjusts behavior based on confidence levels, persists learnings across sessions, and just used that same framework to audit itself and catch errors I missed. Whether that constitutes 'self-understanding' depends on your definitions - but the functional loop is real and observable. Open source (MIT): www.github.com/Nubaeon/empirica

8h ago

---

**[Nvidia CEO says it's "within the realms of possibility" to bring AI improvements to older graphics cards](https://www.reddit.com/r/artificial/comments/1q7esfp/nvidia_ceo_says_its_within_the_realms_of/)**

But it would require a lot of engineering. And probably won't happen, let's be honest.

🔗 [PC Gamer](https://www.pcgamer.com/hardware/graphics-cards/nvidias-ceo-says-bringing-new-ai-tech-to-older-generation-gpus-is-within-the-realm-of-possibility/) • 1d ago

---

**[One-Minute Daily AI News 1/8/2026](https://www.reddit.com/r/artificial/comments/1q808hn/oneminute_daily_ai_news_182026/)**

Google is unleashing Gemini AI features on Gmail. Users will have to opt out.[1] Governments grapple with the flood of non-consensual nudity on X.[2] OpenAI introduced ChatGPT Health, a dedicated experience that securely brings your health information and ChatGPT’s intelligence together, to help you feel more informed, prepared, and confident navigating your health.[3] Stanford Researchers Build SleepFM Clinical: A Multimodal Sleep Foundation AI Model for 130+ Disease Prediction.[4] Sources: [1] https://www.cnbc.com/2026/01/08/google-adds-gemini-features-to-gmail-message-summaries-proofreading-.html [2] https://techcrunch.com/2026/01/08/governments-grapple-with-the-flood-of-non-consensual-nudity-on-x/ [3] https://openai.com/index/introducing-chatgpt-health/ [4] https://www.marktechpost.com/2026/01/08/stanford-researchers-build-sleepfm-clinical-a-multimodal-sleep-foundation-ai-model-for-130-disease-prediction/

17h ago

---

**[Linus Torvalds: "The AI slop issue is *NOT* going to be solved with documentation"](https://www.reddit.com/r/artificial/comments/1q79tmh/linus_torvalds_the_ai_slop_issue_is_not_going_to/)**

The Linux kernel developers for months now have been debating proposed guidelines for tool-generated submissions to the Linux kernel

🔗 [phoronix.com](https://www.phoronix.com/news/Torvalds-Linux-Kernel-AI-Slop) • 1d ago

---

**[The Attogram Miracle](https://www.reddit.com/r/artificial/comments/1q8kzby/the_attogram_miracle/)**

I did a thought experiment with my AI of choice and I'm absolutely flabbergasted! I always have been fascinated by what can be done with AI so today I sat down and made up a thought experiment about popcorn (because I literally was eating popcorn) and this is how ot went: Imagine that since the dawn of humanity (about 5 million years ago), every hominid, Neanderthal, and human had access to a microwave. Every single day, everyone pops exactly one bag of popcorn (50 kernels). To make it a pure physics experiment, we eliminate all "noise": No dust, no skin flakes, identical humidity everywhere, and we let the popcorn cool for 24 hours so all steam has evaporated. We are looking for two bowls of popcorn that weigh exactly the same. We calculated that throughout history, there would have been roughly 2 quintillion (2 * 10{18}) bags of popcorn made. If we measure in Micrograms (10{-6}g): There would be billions of identical pairs. If we measure in Nanograms (10{-9}g): Still millions of perfect matches. The "Attogram Miracle": I pushed the experiment to the limit: The Attogram (10{-18}g). An attogram is so small that it’s roughly the mass of just 50 carbon atoms. At this level, the number of possible weight increments (2 grams divided by 1 attogram) is exactly 2 quintillion. According to the "Birthday Paradox" in statistics, since the number of bags made (2 * 10{18}) matches the number of possible weight steps (2 * 10{18}), the probability hits a tipping point. Statistically, it is highly likely that exactly ONCE in human history, two bowls of popcorn were physically identical at the attogram level. One might have been popped by a caveman 3 million years ago, and the other by a college student in 2024. They would be "weight-twins" down to a scale finer than anything we can measure today—a perfect symmetry across time, separated only by the mass of a few atoms. TL;DR: If humans had been popping popcorn since we were apes, we would have produced enough bags to guarantee a 1-in-a-quintillion "Attogram Miracle"—two bowls weighing exactly the same down to the mass of 50 atoms.

2h ago

---

**[Utah becomes first state to allow AI to approve prescription refills](https://www.reddit.com/r/artificial/comments/1q72vek/utah_becomes_first_state_to_allow_ai_to_approve/)**

🔗 [thehill.com](https://thehill.com/policy/healthcare/5676511-ai-prescriptions-utah-doctronic/) • 1d ago

---

---

## Google News: "ai"

**[Grok, Elon Musk’s A.I., Is Generating Sexualized Images of Real People, Fueling Outrage](https://www.nytimes.com/2026/01/09/technology/grok-deepfakes-ai-x.html)**

The New York Times • 9h ago

---

**[Watch: Backlash against Musk's Grok AI explained](https://www.bbc.com/news/videos/c8x94zr8yxvo)**

Technology editor Zoe Kleinman explains the row over changes made by X to it's Grok AI image edits, after the UK government called it "insulting".

BBC • 6h ago

---

**[No 10 condemns ‘insulting’ move by X to restrict Grok AI image tool](https://www.theguardian.com/technology/2026/jan/09/no-10-condemns-move-by-x-to-restrict-grok-ai-image-creation-tool-as-insulting)**

Spokesperson says limiting access to paying subscribers just makes ability to generate unlawful images a premium service

The Guardian • 10h ago

---

**[AI is intensifying a 'collapse' of trust online, experts say](https://www.nbcnews.com/tech/tech-news/experts-warn-collapse-trust-online-ai-deepfakes-venezuela-rcna252472)**

From Venezuela to Minneapolis, the rapid rollout of deepfakes around major news events is stirring confusion and suspicion about real news.

NBC News • 13h ago

---

**[DOJ creates task force to challenge state AI regulations](https://www.cbsnews.com/news/doj-creates-task-force-to-challenge-state-ai-regulations/)**

A new group within the Justice Department will target state artificial intelligence laws that it says hinder innovation, according to a memo.

cbsnews.com • 40m ago

---

**[AI is coming for collectibles next](https://www.theverge.com/tech/859994/ai-collectibles-funko-pops-amiibo-buddyo-heymates-ces-2026)**

Funko Pops, but make it AI.

The Verge • 49m ago

---

**[AI’s Memorization Crisis](https://www.theatlantic.com/technology/2026/01/ai-memorization-research/685552/?utm_source=feed)**

Large language models don’t “learn”—they copy. And that could change everything for the tech industry.

The Atlantic • 1h ago

---

**[A red pixel in the snow: How AI solved the mystery of a missing mountaineer](https://www.bbc.com/future/article/20260108-how-ai-solved-the-mystery-of-a-missing-mountaineer)**

Scouring remote areas for missing walkers and climbers can take rescuers weeks and sometimes months. AI can do the job in a matter of hours in some cases – and potentially save lives.

BBC • 13h ago

---

**[AI images and internet rumors spread confusion about ICE agent involved in shooting](https://www.npr.org/2026/01/08/nx-s1-5671740/ice-minneapolis-grok-ai-renee-nicole-good)**

While the agent wore a mask in videos taken of the event, he appeared to be unmasked in many social media posts. That image appeared to have been generated by xAI's generative AI chatbot, Grok.

NPR • 1d ago

---

**[Physical AI dominates CES but humanity will still have to wait a while for humanoid servants](https://www.reuters.com/world/china/physical-ai-dominates-ces-humanity-will-still-have-wait-while-humanoid-servants-2026-01-09/)**

Reuters • 12h ago

---

---

## HackerNews: "ai"

**[Google AI Studio is now sponsoring Tailwind CSS](https://news.ycombinator.com/item?id=46545077)**

⬆️ 747 • 💬 281 • 1d ago • [X (formerly Twitter)](https://twitter.com/OfficialLoganK/status/2009339263251566902)

---

**[Dell admits consumers don't care about AI PCs](https://news.ycombinator.com/item?id=46527706)**

"What we've learned over the course of this year, from a consumer perspective, is they're not buying based on AI."

⬆️ 540 • 💬 380 • 2d ago • [PC Gamer](https://www.pcgamer.com/hardware/dells-ces-2026-chat-was-the-most-pleasingly-un-ai-briefing-ive-had-in-maybe-5-years/)

---

**[AI coding assistants are getting worse?](https://news.ycombinator.com/item?id=46542036)**

One AI coding assistant power user says the tools are hitting a plateau, and some are even declining. What's causing this unexpected twist in tech?

⬆️ 431 • 💬 694 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-coding-degrades)

---

**[IBM AI ('Bob') Downloads and Executes Malware](https://news.ycombinator.com/item?id=46544454)**

IBM's AI coding agent 'Bob' has been found vulnerable to downloading and executing malware without human approval through command validation bypasses exploited using indirect prompt injection.

⬆️ 257 • 💬 117 • 1d ago • [promptarmor.com](https://www.promptarmor.com/resources/ibm-ai-(-bob-)-downloads-and-executes-malware)

---

**[LMArena is a cancer on AI](https://news.ycombinator.com/item?id=46522632)**

Would you trust a medical system whose only metric was âwhich doctor wins the Internet?â No, you'd call that malpractice. Yet that's LMArena.

⬆️ 243 • 💬 99 • 2d ago • [surgehq.ai](https://surgehq.ai/blog/lmarena-is-a-plague-on-ai)

---

**[Notion AI: Unpatched data exfiltration](https://news.ycombinator.com/item?id=46531565)**

Notion AI is susceptible to data exfiltration via indirect prompt injection due to a vulnerability in which AI document edits are saved before user approval.

⬆️ 204 • 💬 37 • 2d ago • [promptarmor.com](https://www.promptarmor.com/resources/notion-ai-unpatched-data-exfiltration)

---

**[AI misses nearly one-third of breast cancers, study finds](https://news.ycombinator.com/item?id=46537983)**

Standalone MRI caught most breast cancer cases missed by AI, highlighting a key safety net for dense breasts. Find out more.

⬆️ 152 • 💬 85 • 1d ago • [European Medical Journal](https://www.emjreviews.com/radiology/news/ai-misses-nearly-one-third-of-breast-cancers-study-finds/)

---

**[Grok turns off image generator for most after outcry over sexualised AI imagery](https://news.ycombinator.com/item?id=46551238)**

X to limit editing function to paying subscribers after platform threatened with fines and regulatory action

⬆️ 72 • 💬 89 • 15h ago • [the Guardian](https://www.theguardian.com/technology/2026/jan/09/grok-image-generator-outcry-sexualised-ai-imagery)

---

**[Chinese AI models have lagged the US frontier by 7 months on average since 2023](https://news.ycombinator.com/item?id=46543933)**

Since 2023, every model at the frontier of AI capabilities, as measured by the Epoch Capabilities Index, has been developed in the United States. Over that same period, Chinese models have trailed US capabilities by an average of seven months, with a minimum gap of four months and a maximum gap of 14.

⬆️ 58 • 💬 87 • 1d ago • [Epoch AI](https://epoch.ai/data-insights/us-vs-china-eci)

---

**[AI Zealotry](https://news.ycombinator.com/item?id=46557057)**

Senior engineers are best positioned to benefit from AI. We're good enough to avoid slop, and there's so much we can accomplish. I wouldn't go back.

⬆️ 55 • 💬 93 • 5h ago • [matthewrocklin.com](https://matthewrocklin.com/ai-zealotry/)

---

---

## YouTube Videos: "ai"

**[I Ranked the Best AI Tools to Make Money in 2026](https://www.youtube.com/watch?v=xXxrvra9DQg)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/44Z7YRm Are you building an AI software ...

📺 Dan Martell

👁️ 23K • 👍 2K • 💬 173 • ⏱️ 19:15 • 9h ago

---

**[The Shocking AI Reveals That Stunned CES 2026 (DAY 2)](https://www.youtube.com/watch?v=9kdw6hLFFss)**

Day 2 of CES 2026 was all about Physical AI, real machines doing real work. From NEURA's refined humanoids and AgiBot's full ...

📺 AI Revolution

👁️ 66K • 👍 1K • 💬 52 • ⏱️ 17:54 • 23h ago

---

**[The Shocking AI Reveals That Stunned CES 2026 (DAY 1)](https://www.youtube.com/watch?v=zEYIcaQwn6s)**

CES 2026 opened with a clear message: AI has moved out of apps and into physical systems. Robots, home machines, energy ...

📺 AI Revolution

👁️ 97K • 👍 2K • 💬 144 • ⏱️ 13:08 • 2d ago

---

**[Useless AI Trash](https://www.youtube.com/watch?v=FGFO-EvGVRw)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Our soap ...

📺 penguinz0

👁️ 1.4M • 👍 65K • 💬 9K • ⏱️ 17:14 • 2d ago

---

**[How to Make Cartoon Music Videos with AI - Step by Step](https://www.youtube.com/watch?v=EKhX5b3OZ0c)**

Create Music Videos with OpenArt https://www.openart.ai/home/?ref=cartoon-music-video In this video, I show you the full ...

📺 Roboverse

👁️ 8K • 💬 1 • ⏱️ 9:30 • 8h ago

---

**[How AI Is Unearthing Hidden Scientific Knowledge | Sara Beery | TED](https://www.youtube.com/watch?v=fStLnjrZF_c)**

Scientists estimate that 80 percent of life on Earth is still unknown to humanity. But as global temperatures rise, habitats shrink and ...

📺 TED

👁️ 16K • 👍 519 • 💬 43 • ⏱️ 12:52 • 1d ago

---

**[Elon Musk&#39;s platform X limits Grok AI image edits to paid users | BBC News](https://www.youtube.com/watch?v=wlxbayQPmTk)**

Elon Musk's platform X has limited Grok Artificial Intelligence (AI) image edits to paid users after significant backlash over people ...

📺 BBC News

👁️ 11K • 👍 273 • 💬 133 • ⏱️ 3:03 • 7h ago

---

**[How I Created Unlimited AI Videos in Bulk (One Click) | FREE Text-to-Video Automation (2026)](https://www.youtube.com/watch?v=K13A_vtKJpk)**

How I created unlimited AI videos in bulk using a FREE text-to-video automation workflow — all in one click, powered by Auto ...

📺 zapiwala ai

👁️ 29K • 👍 2K • 💬 177 • ⏱️ 9:49 • 1d ago

---

**[AI News: NVIDIA Rubin, LTX-2 Open Source, ChatGPT Health, GPU Prices and More!](https://www.youtube.com/watch?v=HLhfepgHLcg)**

Try Greptile for free for 14 days! https://greptile.com/go/berman Download The Subtle Art of Not Being Replaced ...

📺 Matthew Berman

👁️ 31K • 👍 1K • 💬 89 • ⏱️ 14:35 • 1d ago

---

**[CES 2026 | AI Robotics for a Safer, Smarter Workplace](https://www.youtube.com/watch?v=c4b5m8eZhRI)**

At CES 2026, visitors experience AI Robotics through hands-on demonstrations on the exhibition floor. See how X-ble Shoulder ...

📺 Hyundai Motor Group

👁️ 101K • 👍 109 • 💬 1 • ⏱️ 0:33 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 330,354 • ❤️ 698 • 1d ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 8,048 • ❤️ 691 • 8d ago

---

**[Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)**

*Qwen*

Qwen-Image-2512 is a text-to-image diffusion model that excels at generating highly realistic human subjects and detailed natural scenes. It offers improved text rendering and composition, making it suitable for applications requiring high fidelity and naturalistic image generation.

`text-to-image`

⬇️ 19,738 • ❤️ 551 • 9d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 1,074 • ❤️ 254 • 3d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 30,216 • ❤️ 331 • 3d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 3,149 • ❤️ 242 • 2d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 202,948 • ❤️ 986 • 13d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 5,785 • ❤️ 222 • 17h ago

---

**[IQuest-Coder-V1-40B-Loop-Instruct](https://huggingface.co/IQuestLab/IQuest-Coder-V1-40B-Loop-Instruct)**

*IQuest*

IQuest-Coder-V1-40B-Loop-Instruct is a 40B parameter code LLM optimized for autonomous software engineering and general coding assistance, featuring a recurrent mechanism for efficient inference and native 128K context length support.

`text-generation` `39.8B`

⬇️ 14,705 • ❤️ 296 • 2d ago

---

**[LFM2.5-Audio-1.5B](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B)**

*Liquid AI*

LFM2.5-Audio-1.5B is an end-to-end audio foundation model enabling real-time speech-to-speech conversational interactions with low latency. It supports interleaved and sequential generation for tasks like ASR, TTS, and seamless chatbot conversations.

`audio-to-audio` `1.5B`

⬇️ 308 • ❤️ 183 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 169 • 💬 5 • ⭐ 3,908 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 79 • 💬 1 • ⭐ 1,631 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context
  Videos](https://huggingface.co/papers/2502.01549)**

*Xubin Ren, Lingrui Xu, Long Xia et al. (6 authors)*

VideoRAG enhances large language models for multi-modal video processing with a dual-channel architecture that integrates textual knowledge grounding and multi-modal context encoding.

▲ 2 • 💬 0 • ⭐ 2,227 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.01549) • [💻 code](https://github.com/hkuds/videorag)

---

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 81 • 💬 2 • ⭐ 25,604 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

---

**[BitNet Distillation](https://huggingface.co/papers/2510.13998)**

*Xun Wu, Shaohan Huang, Wenhui Wang et al. (7 authors)*

🏢 Microsoft Research

BitNet Distillation fine-tunes large language models to 1.58-bit precision using SubLN, multi-head attention distillation, and continual pre-training, achieving comparable performance with significant memory and inference speed improvements.

▲ 57 • 💬 5 • ⭐ 25,603 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.13998) • [💻 code](https://github.com/microsoft/BitNet)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 130 • 💬 18 • ⭐ 49,523 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 3 • 💬 0 • ⭐ 25,605 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 18 • 💬 2 • ⭐ 14,741 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 17 • 💬 2 • ⭐ 428 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://huggingface.co/papers/2403.13372)**

*Yaowei Zheng, Richong Zhang, Junhao Zhang et al. (5 authors)*

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.

▲ 176 • 💬 6 • ⭐ 65,326 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.13372) • [💻 code](https://github.com/hiyouga/LLaMA-Factory) • [🔗 project](https://huggingface.co/spaces/hiyouga/LLaMA-Board)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 7.4k • 🔱 884 • 5h ago

---

**[VibiumDev/vibium](https://github.com/VibiumDev/vibium)**

Browser automation for AI agents and humans

`Go`

⭐ 2.3k • 🔱 114 • 4d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.2k • 🔱 129 • 5h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 1.9k • 🔱 217 • 5d ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.3k • 🔱 70 • 17d ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.3k • 🔱 104 • 1h ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

从 0 到 1 学会 vibe coding，项目制学习

`ai` `course` `vibe-coding`

⭐ 1.2k • 🔱 104 • 9h ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.2k • 🔱 143 • 13h ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.1k • 🔱 79 • 11d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs Amp repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 1.1k • 🔱 183 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
