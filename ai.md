---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-09T09:53:17.962348+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 09, 2026 at 09:53 UTC  
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

**[Why Yann LeCun left Meta for World Models](https://www.reddit.com/r/artificial/comments/1q7ugtz/why_yann_lecun_left_meta_for_world_models/)**

As we know, one of the godfathers of AI recently left Meta to found his own lab AMI and the the underlying theme is his longstanding focus on world modelling. This is still a relatively underexplored concept however the recent surge of research suggests why it is gaining traction. For example, Marble demonstrates how multimodal models that encode a sense of the world can achieve far greater efficiency and reasoning capability than LLMs, which are inherently limited to predicting the next token. Genie illustrates how 3D interactive environments can be learned and simulated to support agent planning and reasoning. Other recent work includes SCOPE, which leverages world modelling to match frontier LLM performance (GPT-4-level) with far smaller models (millions versus trillions of parameters), and HunyuanWorld, which scored ~77 on the WorldScore benchmark. There are also new models being developed that push the boundaries of world modelling further. It seems the AI research community is beginning to recognize the practical and theoretical advantages of world models for reasoning, planning, and multimodal understanding. Curious, who else has explored this domain recently? Are there emerging techniques or results in world modelling that you find particularly compelling? Let us discuss. ps: See the comments for references to all the models mentioned above.

8h ago

---

**[Nvidia CEO says it's "within the realms of possibility" to bring AI improvements to older graphics cards](https://www.reddit.com/r/artificial/comments/1q7esfp/nvidia_ceo_says_its_within_the_realms_of/)**

But it would require a lot of engineering. And probably won't happen, let's be honest.

🔗 [PC Gamer](https://www.pcgamer.com/hardware/graphics-cards/nvidias-ceo-says-bringing-new-ai-tech-to-older-generation-gpus-is-within-the-realm-of-possibility/) • 18h ago

---

**[Linus Torvalds: "The AI slop issue is *NOT* going to be solved with documentation"](https://www.reddit.com/r/artificial/comments/1q79tmh/linus_torvalds_the_ai_slop_issue_is_not_going_to/)**

The Linux kernel developers for months now have been debating proposed guidelines for tool-generated submissions to the Linux kernel

🔗 [phoronix.com](https://www.phoronix.com/news/Torvalds-Linux-Kernel-AI-Slop) • 22h ago

---

**[Musk lawsuit over OpenAI for-profit conversion can go to trial, US judge says](https://www.reddit.com/r/artificial/comments/1q82r2v/musk_lawsuit_over_openai_forprofit_conversion_can/)**

Judge says there is plenty of evidence to suggest OpenAI’s leaders made assurances nonprofit structure would be kept

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jan/08/elon-musk-openai-lawsuit-for-profit-conversion-can-go-to-trial-us-judge-says) • 1h ago

---

**[One-Minute Daily AI News 1/8/2026](https://www.reddit.com/r/artificial/comments/1q808hn/oneminute_daily_ai_news_182026/)**

Google is unleashing Gemini AI features on Gmail. Users will have to opt out.[1] Governments grapple with the flood of non-consensual nudity on X.[2] OpenAI introduced ChatGPT Health, a dedicated experience that securely brings your health information and ChatGPT’s intelligence together, to help you feel more informed, prepared, and confident navigating your health.[3] Stanford Researchers Build SleepFM Clinical: A Multimodal Sleep Foundation AI Model for 130+ Disease Prediction.[4] Sources: [1] https://www.cnbc.com/2026/01/08/google-adds-gemini-features-to-gmail-message-summaries-proofreading-.html [2] https://techcrunch.com/2026/01/08/governments-grapple-with-the-flood-of-non-consensual-nudity-on-x/ [3] https://openai.com/index/introducing-chatgpt-health/ [4] https://www.marktechpost.com/2026/01/08/stanford-researchers-build-sleepfm-clinical-a-multimodal-sleep-foundation-ai-model-for-130-disease-prediction/

4h ago

---

**[AI Futures Project Delays Timeline of 2030 Human Apocalypse Scenario](https://www.reddit.com/r/artificial/comments/1q83rhw/ai_futures_project_delays_timeline_of_2030_human/)**

Humanity may have gained a few extra years. The AI Futures Project, led by former OpenAI researcher Daniel Kokotajlo, has revised its forecast for superintelligent AI, concluding that the technological breakthroughs once expected by 2027 are now more likely to arrive in the early 2030s.

🔗 [Hungarian Conservative](https://www.hungarianconservative.com/articles/tech/ai-futures-project-ai-2027-apocalypse-timeline-superintelligence-daniel-kokotajlo/) • 31m ago

---

**[Elon Musk's Grok AI image editing limited to paid users after deepfakes](https://www.reddit.com/r/artificial/comments/1q83cyi/elon_musks_grok_ai_image_editing_limited_to_paid/)**

It comes after government urged Ofcom to use all its powers – up to and including an effective ban – against X.

🔗 [bbc.com](https://www.bbc.com/news/articles/c99kn52nx9do) • 56m ago

---

**[Utah becomes first state to allow AI to approve prescription refills](https://www.reddit.com/r/artificial/comments/1q72vek/utah_becomes_first_state_to_allow_ai_to_approve/)**

🔗 [thehill.com](https://thehill.com/policy/healthcare/5676511-ai-prescriptions-utah-doctronic/) • 1d ago

---

**[Quick reliability lesson: if your agent output isn’t enforceable, your system is just improvising](https://www.reddit.com/r/artificial/comments/1q7sbtb/quick_reliability_lesson_if_your_agent_output/)**

I used to think “better prompt” would fix everything. Then I watched my system break because the agent returned: Sure! { "route": "PLAN", } So now I treat agent outputs like API responses: Strict JSON only (no “helpful” prose) Exact schema (keys + types) No extra keys Validate before the next step reads it Retry with validator errors (max 2) If missing info -> return unknown instead of guessing It’s not glamorous, but it’s what turns “cool demo” into “works in production.” If you’ve built agents: what’s your biggest source of failures, format drift, tool errors, or retrieval/routing?

10h ago

---

**[Intel hopes its new chip can be the future of AI](https://www.reddit.com/r/artificial/comments/1q7fvnp/intel_hopes_its_new_chip_can_be_the_future_of_ai/)**

Once the dominant player in chips, Intel has struggled to keep pace with rivals over the past decade. An executive discussed the company’s AI strategy and future direction, driven by the launch of its new Core Ultra 3 chips.

🔗 [CNN](https://www.cnn.com/2026/01/08/tech/comeback-intel-ai-ces?utm_medium=social&utm_campaign=missions&utm_source=reddit) • 17h ago

---

---

## Google News: "ai"

**[Grok turns off image generator for most users after outcry over sexualised AI imagery](https://www.theguardian.com/technology/2026/jan/09/grok-image-generator-outcry-sexualised-ai-imagery)**

X to limit editing function to paying subscribers after platform threatened with fines and regulatory action

The Guardian • 2h ago

---

**[Elon Musk’s xAI under fire for failing to rein in ‘digital undressing’](https://www.cnn.com/2026/01/08/tech/elon-musk-xai-digital-undressing)**

Elon Musk’s AI chatbot, Grok, has been flooded with sexual images of mainly women, many of them real people, by being prompted by users to “digitally undress” them and sometimes placing them in suggestive poses.

CNN • 1d ago

---

**[Ofcom urged to use 'banning' powers over X AI deepfakes](https://www.bbc.com/news/articles/ckgjzknepvzo)**

It follows an ongoing backlash against the use of X's AI Grok to digitally remove clothing from images.

BBC • 3h ago

---

**[Google is unleashing Gemini AI features on Gmail. Users will have to opt out](https://www.cnbc.com/2026/01/08/google-adds-gemini-features-to-gmail-message-summaries-proofreading-.html)**

Google is adding more Gemini features to Gmail, the company's latest effort to spread its core AI product across its product portfolio.

CNBC • 20h ago

---

**[Google Is Adding an ‘AI Inbox’ to Gmail That Summarizes Emails](https://www.wired.com/story/google-ai-inbox-gmail/)**

New Gmail features, powered by the Gemini model, are part of Google’s continued push for users to incorporate AI into their daily life and conversations.

WIRED • 20h ago

---

**[Gmail is entering the Gemini era](https://blog.google/products-and-platforms/products/gmail/gmail-is-entering-the-gemini-era/)**

Learn more about the next era of Gmail, now using Gemini 3 and Personal Intelligence.

blog.google • 20h ago

---

**[Taiwan’s Exports Hit Record in 2025 on AI-Fueled Demand](https://www.wsj.com/economy/trade/taiwans-exports-hit-record-in-2025-on-ai-fueled-demand-bf1f8258?gaa_at=eafs&gaa_n=AWEtsqeA9R498oJNtBzOdz-xamx51G2M-KCQdGcfIk9SwIbNUTCBB45XqGlc&gaa_ts=6960cdea&gaa_sig=RG6i5TcX2cyh4S_50DqxjCljz43UO9LQOWLiC9r_o6GjGlwz17fBf7ZdcXrK51jhnQ3efAfuTxGd0hwpJur1BA%3D%3D)**

The Wall Street Journal • 42m ago

---

**[AI layoffs are looking more and more like corporate fiction that's masking a darker reality, Oxford Economics suggests](https://fortune.com/2026/01/07/ai-layoffs-convenient-corporate-fiction-true-false-oxford-economics-productivity/)**

"Firms don't appear to be replacing workers with AI on a significant scale," the firm said. It suspects some are trying to "dress up layoffs" as good news.

Fortune • 1d ago

---

**[AI Coding Assistants Are Getting Worse](https://spectrum.ieee.org/ai-coding-degrades)**

One AI coding assistant power user says the tools are hitting a plateau, and some are even declining. What's causing this unexpected twist in tech?

IEEE Spectrum • 20h ago

---

**[Analysis | Can AI do your job? See the results from hundreds of tests.](https://www.washingtonpost.com/technology/interactive/2026/ai-jobs-automation/)**

The Washington Post • 15h ago

---

---

## HackerNews: "ai"

**[Opus 4.5 is not the normal AI agent experience that I have had thus far](https://news.ycombinator.com/item?id=46515696)**

Three months ago I would have dismissed claims that AI could replace developers. Today, after using Claude Opus 4.5, I believe AI coding agents can absolutely replace developers.

⬆️ 844 • 💬 1318 • 2d ago • [Burke Holland](https://burkeholland.github.io/posts/opus-4-5-change-everything/)

---

**[Google AI Studio is now sponsoring Tailwind CSS](https://news.ycombinator.com/item?id=46545077)**

⬆️ 641 • 💬 207 • 14h ago • [X (formerly Twitter)](https://twitter.com/OfficialLoganK/status/2009339263251566902)

---

**[Dell admits consumers don't care about AI PCs](https://news.ycombinator.com/item?id=46527706)**

"What we've learned over the course of this year, from a consumer perspective, is they're not buying based on AI."

⬆️ 499 • 💬 353 • 1d ago • [PC Gamer](https://www.pcgamer.com/hardware/dells-ces-2026-chat-was-the-most-pleasingly-un-ai-briefing-ive-had-in-maybe-5-years/)

---

**[AI coding assistants are getting worse?](https://news.ycombinator.com/item?id=46542036)**

One AI coding assistant power user says the tools are hitting a plateau, and some are even declining. What's causing this unexpected twist in tech?

⬆️ 309 • 💬 495 • 18h ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-coding-degrades)

---

**[IBM AI ('Bob') Downloads and Executes Malware](https://news.ycombinator.com/item?id=46544454)**

IBM's AI coding agent 'Bob' has been found vulnerable to downloading and executing malware without human approval through command validation bypasses exploited using indirect prompt injection.

⬆️ 248 • 💬 113 • 15h ago • [promptarmor.com](https://www.promptarmor.com/resources/ibm-ai-(-bob-)-downloads-and-executes-malware)

---

**[LMArena is a cancer on AI](https://news.ycombinator.com/item?id=46522632)**

Would you trust a medical system whose only metric was âwhich doctor wins the Internet?â No, you'd call that malpractice. Yet that's LMArena.

⬆️ 239 • 💬 99 • 2d ago • [surgehq.ai](https://surgehq.ai/blog/lmarena-is-a-plague-on-ai)

---

**[Notion AI: Unpatched data exfiltration](https://news.ycombinator.com/item?id=46531565)**

Notion AI is susceptible to data exfiltration via indirect prompt injection due to a vulnerability in which AI document edits are saved before user approval.

⬆️ 204 • 💬 37 • 1d ago • [promptarmor.com](https://www.promptarmor.com/resources/notion-ai-unpatched-data-exfiltration)

---

**[He was called a 'terrorist sympathizer.' Now his AI company is valued at $3B](https://news.ycombinator.com/item?id=46544276)**

“I must apologize to — absolutely nobody”: Replit founder Amjad Masad isn’t afraid of Silicon Valley.

⬆️ 174 • 💬 208 • 15h ago • [sfstandard.com](https://sfstandard.com/2026/01/07/called-terrorist-sympathizer-now-ai-company-valued-3b/)

---

**[AI misses nearly one-third of breast cancers, study finds](https://news.ycombinator.com/item?id=46537983)**

Standalone MRI caught most breast cancer cases missed by AI, highlighting a key safety net for dense breasts. Find out more.

⬆️ 152 • 💬 84 • 1d ago • [European Medical Journal](https://www.emjreviews.com/radiology/news/ai-misses-nearly-one-third-of-breast-cancers-study-finds/)

---

**[Comparing AI agents to cybersecurity professionals in real-world pen testing](https://news.ycombinator.com/item?id=46518996)**

We present the first comprehensive evaluation of AI agents against human cybersecurity professionals in a live enterprise environment. We evaluate ten cybersecurity professionals alongside six existing AI agents and ARTEMIS, our new agent scaffold, on a large university network consisting of ~8,000 hosts across 12 subnets. ARTEMIS is a multi-agent framework featuring dynamic prompt generation, arbitrary sub-agents, and automatic vulnerability triaging. In our comparative study, ARTEMIS placed second overall, discovering 9 valid vulnerabilities with an 82% valid submission rate and outperforming 9 of 10 human participants. While existing scaffolds such as Codex and CyAgent underperformed relative to most human participants, ARTEMIS demonstrated technical sophistication and submission quality comparable to the strongest participants. We observe that AI agents offer advantages in systematic enumeration, parallel exploitation, and cost -- certain ARTEMIS variants cost $18/hour versus $60/hour for professional penetration testers. We also identify key capability gaps: AI agents exhibit higher false-positive rates and struggle with GUI-based tasks.

⬆️ 124 • 💬 91 • 2d ago • [arXiv.org](https://arxiv.org/abs/2512.09882)

---

---

## YouTube Videos: "ai"

**[The Shocking AI Reveals That Stunned CES 2026 (DAY 2)](https://www.youtube.com/watch?v=9kdw6hLFFss)**

Day 2 of CES 2026 was all about Physical AI, real machines doing real work. From NEURA's refined humanoids and AgiBot's full ...

📺 AI Revolution

👁️ 30K • 👍 825 • 💬 36 • ⏱️ 17:54 • 9h ago

---

**[The Shocking AI Reveals That Stunned CES 2026 (DAY 1)](https://www.youtube.com/watch?v=zEYIcaQwn6s)**

CES 2026 opened with a clear message: AI has moved out of apps and into physical systems. Robots, home machines, energy ...

📺 AI Revolution

👁️ 89K • 👍 2K • 💬 134 • ⏱️ 13:08 • 1d ago

---

**[AI Short Film | So Low - 4K](https://www.youtube.com/watch?v=xbwGK_z9_cU)**

I was playing around with a bunch of different #midjourney style ref codes and found this beautiful teal and olive tinted one. I made ...

📺 Kelly Boesch AI Art

👁️ 9K • 👍 567 • 💬 58 • ⏱️ 2:42 • 19h ago

---

**[Top 6 AI Trends That Will Define 2026 (backed by data)](https://www.youtube.com/watch?v=B23W1gRT9eY)**

Most #AI predictions are speculation. This video covers six trends backed by data from McKinsey, Stanford, #OpenAI, and Epoch ...

📺 Jeff Su

👁️ 83K • 👍 3K • 💬 236 • ⏱️ 13:13 • 2d ago

---

**[Useless AI Trash](https://www.youtube.com/watch?v=FGFO-EvGVRw)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Our soap ...

📺 penguinz0

👁️ 1.3M • 👍 62K • 💬 8K • ⏱️ 17:14 • 1d ago

---

**[Google&#39;s Gmail unveils new AI features powered by Gemini](https://www.youtube.com/watch?v=nzlFoQmMSBk)**

CNBC's MacKenzie Sigalos reports on Gmail's new AI features.

📺 CNBC Television

👁️ 8K • 👍 110 • 💬 13 • ⏱️ 3:43 • 14h ago

---

**[Nvidia unveils new &quot;revolutionary&quot; AI tech](https://www.youtube.com/watch?v=WcWffmAzlPw)**

Artificial intelligence technology giant Nvidia announced a new endeavor that it says will be revolutionary. Emily Bary ...

📺 CBS News

👁️ 10K • 👍 118 • 💬 56 • ⏱️ 3:21 • 2d ago

---

**[Real or AI? 🤔](https://www.youtube.com/watch?v=9sRJM3xGMqo)**

This is a funny meme mixed with storytelling style video about how i have 2 cats on the screen and i let the viewers decide which ...

📺 Tyler Vitelli

👁️ 2.4M • 👍 77K • 💬 6K • ⏱️ 0:10 • 1d ago

---

**[AI Psychosis](https://www.youtube.com/watch?v=gmgiSV-b-Qc)**

Does AI make you delusional? #ai #aipsychology #gpt #gemini #chatgpt #copilot #grok #psychologyfacts #psychology ...

📺 Psych2Go

👁️ 2K • 👍 415 • 💬 42 • ⏱️ 1:54 • 1h ago

---

**[CES 2026 | AI Robotics for a Safer, Smarter Workplace](https://www.youtube.com/watch?v=c4b5m8eZhRI)**

At CES 2026, visitors experience AI Robotics through hands-on demonstrations on the exhibition floor. See how X-ble Shoulder ...

📺 Hyundai Motor Group

👁️ 101K • 👍 101 • 💬 1 • ⏱️ 0:33 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 330,354 • ❤️ 640 • 1d ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 8,048 • ❤️ 684 • 8d ago

---

**[Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)**

*Qwen*

Qwen-Image-2512 is a text-to-image diffusion model that excels at generating highly realistic human subjects and detailed natural scenes. It offers improved text rendering and composition, making it suitable for applications requiring high fidelity and naturalistic image generation.

`text-to-image`

⬇️ 19,738 • ❤️ 541 • 9d ago

---

**[IQuest-Coder-V1-40B-Loop-Instruct](https://huggingface.co/IQuestLab/IQuest-Coder-V1-40B-Loop-Instruct)**

*IQuest*

IQuest-Coder-V1-40B-Loop-Instruct is a 40B parameter code LLM optimized for autonomous software engineering and general coding assistance, featuring a recurrent mechanism for efficient inference and native 128K context length support.

`text-generation` `39.8B`

⬇️ 14,705 • ❤️ 295 • 1d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 202,948 • ❤️ 973 • 12d ago

---

**[K-EXAONE-236B-A23B](https://huggingface.co/LGAI-EXAONE/K-EXAONE-236B-A23B)**

*LG AI Research*

K-EXAONE-236B-A23B is a multilingual text generation model featuring a 236B MoE architecture with 23B active parameters, optimized for efficient inference. It excels in long-context processing (256K), multilingual understanding (6 languages), and agentic capabilities, with a unique focus on Korean cultural context and safety.

`text-generation` `237.1B`

⬇️ 3,644 • ❤️ 443 • 3d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 1,074 • ❤️ 234 • 3d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 30,216 • ❤️ 311 • 3d ago

---

**[IQuest-Coder-V1-40B-Instruct](https://huggingface.co/IQuestLab/IQuest-Coder-V1-40B-Instruct)**

*IQuest*

IQuest-Coder-V1-40B-Instruct is a 40B parameter code LLM trained with a code-flow paradigm for autonomous software engineering, excelling in benchmarks like SWE-Bench and BigCodeBench with native 128K context length.

`text-generation` `39.8B`

⬇️ 4,662 • ❤️ 260 • 6d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 5,785 • ❤️ 205 • 3h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 74 • 💬 1 • ⭐ 1,468 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 169 • 💬 5 • ⭐ 3,440 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 81 • 💬 2 • ⭐ 25,597 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

---

**[BitNet Distillation](https://huggingface.co/papers/2510.13998)**

*Xun Wu, Shaohan Huang, Wenhui Wang et al. (7 authors)*

🏢 Microsoft Research

BitNet Distillation fine-tunes large language models to 1.58-bit precision using SubLN, multi-head attention distillation, and continual pre-training, achieving comparable performance with significant memory and inference speed improvements.

▲ 57 • 💬 5 • ⭐ 25,604 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.13998) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 3 • 💬 0 • ⭐ 25,600 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 130 • 💬 18 • ⭐ 49,477 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 17 • 💬 2 • ⭐ 14,698 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context
  Videos](https://huggingface.co/papers/2502.01549)**

*Xubin Ren, Lingrui Xu, Long Xia et al. (6 authors)*

VideoRAG enhances large language models for multi-modal video processing with a dual-channel architecture that integrates textual knowledge grounding and multi-modal context encoding.

▲ 2 • 💬 0 • ⭐ 2,040 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.01549) • [💻 code](https://github.com/hkuds/videorag)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 141 • 💬 6 • ⭐ 20,104 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[DreamID-V:Bridging the Image-to-Video Gap for High-Fidelity Face Swapping via Diffusion Transformer](https://huggingface.co/papers/2601.01425)**

*Xu Guo, Fulong Ye, Xinghui Li et al. (9 authors)*

🏢 ByteDance

A novel video face swapping framework combines image face swapping techniques with diffusion transformers and curriculum learning to achieve superior identity preservation and visual realism.

▲ 46 • 💬 5 • ⭐ 307 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.01425) • [💻 code](https://github.com/bytedance/DreamID-V) • [🔗 project](https://guoxu1233.github.io/DreamID-V/)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 7.2k • 🔱 866 • 1h ago

---

**[VibiumDev/vibium](https://github.com/VibiumDev/vibium)**

Browser automation for AI agents and humans

`Go`

⭐ 2.2k • 🔱 114 • 4d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.2k • 🔱 130 • 19h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 1.9k • 🔱 217 • 4d ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.3k • 🔱 70 • 16d ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.3k • 🔱 102 • 22h ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

从 0 到 1 学会 vibe coding，项目制学习

`ai` `course` `vibe-coding`

⭐ 1.2k • 🔱 101 • 3h ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.2k • 🔱 143 • 3h ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.1k • 🔱 78 • 10d ago

---

**[aiclientproxy/proxycast](https://github.com/aiclientproxy/proxycast)**

让 AI 编辑器之间自然流动，不仅仅可以其他工具使用，也可以转换成 api 为本地开发提供动力。

`Rust` `claude` `kiro`

⭐ 1.0k • 🔱 120 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
