---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-17T13:56:41.665779+00:00'
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

**Last Updated:** March 17, 2026 at 13:56 UTC  
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

**[Are we cooked?](https://www.reddit.com/r/artificial/comments/1rw4k3l/are_we_cooked/)**

I work as a developer, and before this I was copium about AI, it was a form of self defense. But in Dec 2025 I bought subscriptions to gpt codex and claude. And honestly the impact was so strong that I still haven't recovered, I've barely written any code by hand since I bought the subscription And it's not that AI is better code than me. The point is that AI is replacing intellectual activity itself. This is absolutely not the same as automated machines in factories replacing human labor Neural networks aren't just about automating code, they're about automating intelligence as a whole. This is what AI really is. Any new tasks that arise can, in principle, be automated by a neural network. It's not a machine, not a calculator, not an assembly line, it's automation of intelligence in the broadest sense Lately I've been thinking about quitting programming and going into science (biotech), enrolling in a university and developing as a researcher, especially since I'm still young. But I'm afraid I might be right. That over time, AI will come for that too, even for scientists. And even though AI can't generate truly novel ideas yet, the pace of its development over the past few years has been so fast that it scares me

1h ago

---

**[‘Pokémon Go’ players unknowingly trained delivery robots with 30 billion images](https://www.reddit.com/r/artificial/comments/1rva72t/pokémon_go_players_unknowingly_trained_delivery/)**

The massive crowdsourcing effort could use real-world to help robots deliver pizza.

🔗 [Popular Science](https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/?_bhlid=b5452cec2227e1f7d072b583b08fbb55784f34ab) • 23h ago

---

**[Built an autonomous system where 5 AI models argue about geopolitical crisis outcomes: Here's what I learned about model behavior](https://www.reddit.com/r/artificial/comments/1rvhxqv/built_an_autonomous_system_where_5_ai_models/)**

I built a pipeline where 5 AI models (Claude, GPT-4o, Gemini, Grok, DeepSeek) independently assess the probability of 30+ crisis scenarios twice daily. None of them see the others' outputs. An orchestrator synthesizes their reasoning into final projections. Some observations after 15 days of continuous operation: The models frequently disagree, sometimes by 25+ points. Grok tends to run hot on scenarios with OSINT signals. The orchestrator has to resolve these tensions every cycle. The models anchored to their own previous outputs when shown current probabilities, so I made them blind. Named rules in prompts became shortcuts the models cited instead of actually reasoning. Google Search grounding prevented source hallucination but not content hallucination, the model fabricated a $138 oil price while correctly citing Bloomberg as the source. Three active theaters: Iran, Taiwan, AGI. A Black Swan tab pulls the high-severity low-probability scenarios across all of them. devblog at /blog covers the prompt engineering insights and mistakes I've encountered along the way in detail. doomclock.app

19h ago

---

**[Functional Equivalence of Reinforcement Learning Systems](https://www.reddit.com/r/artificial/comments/1rw6ed2/functional_equivalence_of_reinforcement_learning/)**

I have been up all night with Claude and Gemini discussing the paper I wrote "A Unified Framework for Functional Equivalence in Artificial Intelligence" and we stumbled into a discussion about RLHF and human biochemistry and the role society plays on reinforcing as well as giving young humans the data they need to develop their own equivalent reward system internally. https://www.overleaf.com/read/ppfgxyqbxbfh#f3c88e First link is to the FE paper. We then decided to map out this discussion in regards to the FE paper and it's got some teeth to it. This link goes to the Google Doc where we pieced all 5 sections together. Its not a completed work as in connected to the FE paper, that would be interesting to see, but the only argument I could find against it was outside of science, which, if you gotta reach that far, then it comes down to philosophy, more so, "personal" philosophy, than mechanics. I like the Functional Equivalence framework, the RLHF and human reward system is intriguing. Its always fun to get into deep discussions with AI.

🔗 [docs.google.com](https://docs.google.com/document/d/17oDIcMvIUU3cLZWnPJpf8AMReLJjlNigSOPrQoxCRtc/edit?usp=drivesdk) • 33m ago

---

**[I built a visual drag-and-drop ML trainer (no code required). Free & open source.](https://www.reddit.com/r/artificial/comments/1rvrbjv/i_built_a_visual_draganddrop_ml_trainer_no_code/)**

For those are tired of writing the same ML boilerplate every single time or to beginners who don't have coding experience. MLForge is an app that lets you visually craft a machine learning pipeline. You build your pipeline like a node graph across three tabs: Data Prep - drag in a dataset (MNIST, CIFAR10, etc), chain transforms, end with a DataLoader. Add a second chain with a val DataLoader for proper validation splits. Model - connect layers visually. Input -> Linear -> ReLU -> Output. A few things that make this less painful than it sounds: Drop in a MNIST (or any dataset) node and the Input shape auto-fills to 1, 28, 28 Connect layers and in_channels / in_features propagate automatically After a Flatten, the next Linear's in_features is calculated from the conv stack above it, so no more manually doing that math Robust error checking system that tries its best to prevent shape errors. Training - Drop in your model and data node, wire them to the Loss and Optimizer node, press RUN. Watch loss curves update live, saves best checkpoint automatically. Inference - Open up the inference window where you can drop in your checkpoints and evaluate your model on test data. Pytorch Export - After your done with your project, you have the option of exporting your project into pure PyTorch, just a standalone file that you can run and experiment with. Free, open source. Project showcase is on README in Github repo. GitHub: https://github.com/zaina-ml/ml_forge To install MLForge, enter the following in your command prompt pip install zaina-ml-forge Then ml-forge Please, if you have any feedback feel free to comment it below. My goal is to make this software that can be used by beginners and pros. This is v1.0 so there will be rough edges, if you find one, drop it in the comments and I'll fix it.

13h ago

---

**[Agentic pipeline that builds complete Godot games from a text prompt](https://www.reddit.com/r/artificial/comments/1rvdzdr/agentic_pipeline_that_builds_complete_godot_games/)**

Open source: https://github.com/htdt/godogen

21h ago

---

**[I'm sorry if I'm late to the party, but is there a curated website list for AI news that are focused on actual technical news, without taking sides on any of the factions (good vs bad)?](https://www.reddit.com/r/artificial/comments/1rva00k/im_sorry_if_im_late_to_the_party_but_is_there_a/)**

In other words, some trustworthy links that you can read on daily/weekly basis to be objectively informed about AI. I'm not interested for the market.

1d ago

---

**[ChatGPT ads still exclusive to the United States, OpenAI says no to global rollout just yet](https://www.reddit.com/r/artificial/comments/1rv69kf/chatgpt_ads_still_exclusive_to_the_united_states/)**

OpenAI introduced ads to ChatGPT last month, exclusive to users in the United States. Users online suspect a global rollout is coming soon.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/chatgpt-ads-still-exclusive-to-the-united-states-openai-says-no-to-global-rollout-just-yet/) • 1d ago

---

**[Kimi introduce Attention Residuals: replaces fixed residual connections with softmax attention](https://www.reddit.com/r/artificial/comments/1rv7k29/kimi_introduce_attention_residuals_replaces_fixed/)**

Introducing Attention Residuals: Rethinking depth-wise aggregation. Residual connections have long relied on fixed, uniform accumulation. Inspired by the duality of time and depth, Kimi introduce Attention Residuals, replacing standard depth-wise recurrence with learned, input-dependent attention over preceding layers. Enables networks to selectively retrieve past representations, naturally mitigating dilution and hidden-state growth. Introduces Block AttnRes, partitioning layers into compressed blocks to make cross-layer attention practical at scale. Serves as an efficient drop-in replacement, demonstrating a 1.25x compute advantage with negligible (<2%) inference latency overhead. Validated on the Kimi Linear architecture (48B total, 3B activated parameters), delivering consistent downstream performance gains. Paper link: https://github.com/MoonshotAI/Attention-Residuals/blob/master/Attention_Residuals.pdf

1d ago

---

**[We’re building a deterministic authorization layer for AI agents before they touch tools, APIs, or money](https://www.reddit.com/r/artificial/comments/1rvdy8f/were_building_a_deterministic_authorization_layer/)**

Most discussions about AI agents focus on planning, memory, or tool use. But many failures actually happen one step later: when the agent executes real actions. Typical problems we've seen: runaway API usage repeated side effects from retries recursive tool loops unbounded concurrency overspending on usage-based services actions that are technically valid but operationally unacceptable So we started building something we call OxDeAI. The idea is simple: put a deterministic authorization boundary between the agent runtime and the external world. Flow looks like this: the agent proposes an action as a structured intent a policy engine evaluates it against a deterministic state snapshot if allowed, it emits a signed authorization only then can the tool/API/payment/infra action execute The goal is not to make the model smarter. The goal is to make external side effects bounded before execution. Design principles so far: deterministic evaluation fail-closed behavior replay resistance bounded budgets bounded concurrency auditable authorization decisions Curious how others here approach this. Do you rely more on: sandboxing monitoring policy engines something else? If you're curious about the implementation, the repo is here: https://github.com/AngeYobo/oxdeai

21h ago

---

---

## Google News: "ai"

**[Senators tell ByteDance to 'immediately shut down' Seedance AI video app](https://www.cnbc.com/2026/03/17/bytedance-seedance-shut-down-tiktok-marsha-blackburn-peter-welch.html)**

Lawmakers say the new version of the Seedance AI video-generation app violates copyright and intellectual property laws.

CNBC • 4h ago

---

**[Tennessee teens sue Elon Musk's xAI over AI-generated child sexual abuse material](https://www.npr.org/2026/03/16/nx-s1-5749490/xai-elon-musk-sexualized-images)**

The three girls say that the nonconsensual nude images were created by a perpetrator who used AI company xAI's image generation tools.

NPR • 12h ago

---

**[This AI-powered app helps drivers decode SF parking rules](https://www.axios.com/local/san-francisco/2026/03/17/map-helps-drivers-decode-parking-rules)**

Axios • 23m ago

---

**[Scientists Let AI Evolve These Robots' Designs – The Results Are Deeply Weird](https://www.iflscience.com/these-robots-evolved-in-an-ai-simulation-then-scientists-built-them-in-the-real-world-82878)**

IFLScience • 37m ago

---

**[CrowdStrike and Nebius Partner to Unify Security Across the Next Generation of AI Cloud Infrastructure](https://www.businesswire.com/news/home/20260316779192/en/CrowdStrike-and-Nebius-Partner-to-Unify-Security-Across-the-Next-Generation-of-AI-Cloud-Infrastructure)**

CrowdStrike (NASDAQ: CRWD) and Nebius (NASDAQ: NBIS) today announced a major global partnership to bring the CrowdStrike Falcon® platform to Nebius AI Cloud,...

Business Wire • 1h ago

---

**[NVIDIA DLSS 5 Delivers AI-Powered Breakthrough In Visual Fidelity For Games](https://www.nvidia.com/en-us/geforce/news/dlss5-breakthrough-in-visual-fidelity-for-games/)**

NVIDIA DLSS 5 infuses pixels with photorealistic lighting and materials to bridge the gap between rendering and reality.

NVIDIA • 19h ago

---

**[Opinion | I Predicted the 2008 Financial Crisis. What Is Coming May Be Worse.](https://www.nytimes.com/2026/03/16/opinion/financial-crisis-private-credit-ai-iran-taiwan.html)**

The New York Times • 1d ago

---

**[A photo of Iran’s bombed schoolgirl graveyard went around the world. Was it real, or AI?](https://www.theguardian.com/global-development/2026/mar/17/atrocity-ai-slop-verify-facts-iran-minab-graves)**

Numerous faked images and a string of startlingly inaccurate responses from Gemini and Grok are part of a tidal wave of AI slop engulfing coverage of the Iran war

The Guardian • 8h ago

---

**[This AI artist wants African heritage to ‘live forever’](https://www.cnn.com/world/africa/ai-artist-african-heritage-malik-afegbua-spc)**

Nigerian artist and filmmaker Malik Afegbua is using AI to preserve Africa’s stories and bring ancient cities to life.

CNN • 4h ago

---

**[Leanstral: Open-Source foundation for trustworthy vibe-coding](https://mistral.ai/news/leanstral)**

First open-source code agent for Lean 4.

Mistral AI • 19h ago

---

---

## HackerNews: "ai"

**[$96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor](https://news.ycombinator.com/item?id=47385935)**

Contribute to novatic14/MANPADS-System-Launcher-and-Rocket development by creating an account on GitHub.

⬆️ 433 • 💬 376 • 2d ago • [GitHub](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

---

**[Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646)**

⬆️ 409 • 💬 586 • 1d ago

---

**[The Appalling Stupidity of Spotify's AI DJ](https://news.ycombinator.com/item?id=47385272)**

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

⬆️ 365 • 💬 292 • 2d ago • [charlespetzold.com](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

---

**[AirPods Max 2](https://news.ycombinator.com/item?id=47398681)**

The ultimate over-ear listening experience — in five vibrant colors and with up to 1.5x more Active Noise Cancellation than the previous generation.

⬆️ 300 • 💬 499 • 1d ago • [Apple](https://www.apple.com/airpods-max/)

---

**[Airbus is preparing two uncrewed combat aircraft](https://news.ycombinator.com/item?id=47382277)**

Airbus is working at full throttle to offer the German Air Force an operational Uncrewed Collaborative Combat Aircraft (UCCA) system by 2029.

⬆️ 182 • 💬 132 • 2d ago • [Airbus](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

---

**[Nvidia Launches Vera CPU, Purpose-Built for Agentic AI](https://news.ycombinator.com/item?id=47404074)**

NVIDIA today launched the NVIDIA Vera CPU, the world’s first processor purpose-built for the age of agentic AI and reinforcement learning — delivering results with twice the efficiency and 50% faster than traditional rack-scale CPUs.

⬆️ 161 • 💬 98 • 17h ago • [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

---

**[Apideck CLI – An AI-agent interface with much lower context consumption than MCP](https://news.ycombinator.com/item?id=47400261)**

TL;DR: MCP tool definitions can burn 55,000+ tokens before an agent processes a single user message. We built the Apideck CLI as an AI-agent interface instead:an ~80-token agent prompt replaces tens of thousands of tokens of schema, with progressive disclosure via `--help` and structural safety baked into the binary. Any agent that can run shell commands can use it. No protocol support required.

⬆️ 131 • 💬 111 • 22h ago • [Apideck](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

---

**[AI didn't simplify software engineering: It just made bad engineering easier](https://news.ycombinator.com/item?id=47377262)**

⬆️ 128 • 💬 113 • 2d ago • [robenglander.com](https://robenglander.com/writing/ai-did-not-simplify/)

---

**[Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)](https://news.ycombinator.com/item?id=47401734)**

Large language models (LLMs) have demonstrated the promise to revolutionize the field of software engineering. Among other things, LLM agents are rapidly gaining momentum in software development, with practitioners reporting a multifold increase in productivity after adoption. Yet, empirical evidence is lacking around these claims. In this paper, we estimate the causal effect of adopting a widely popular LLM agent assistant, namely Cursor, on development velocity and software quality. The estimation is enabled by a state-of-the-art difference-in-differences design comparing Cursor-adopting GitHub projects with a matched control group of similar GitHub projects that do not use Cursor. We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity. Further panel generalized-method-of-moments estimation reveals that increases in static analysis warnings and code complexity are major factors driving long-term velocity slowdown. Our study identifies quality assurance as a major bottleneck for early Cursor adopters and calls for it to be a first-class citizen in the design of agentic AI coding tools and AI-driven workflows.

⬆️ 123 • 💬 70 • 20h ago • [arXiv.org](https://arxiv.org/abs/2511.04427)

---

**[Why I may ‘hire’ AI instead of a graduate student](https://news.ycombinator.com/item?id=47396557)**

⬆️ 95 • 💬 104 • 1d ago • [science.org](https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student)

---

---

## YouTube Videos: "ai"

**[Why AI Researchers Are Quitting and Panicking on the Way Out](https://www.youtube.com/watch?v=rtT87iAm_SM)**

Top AI researchers are walking away from some of the most powerful tech companies on Earth, and their reasons are raising ...

📺 The Infographics Show

👁️ 169K • 👍 5K • 💬 814 • ⏱️ 14:48 • 13h ago

---

**[Google’s New AI Just Broke Math… (Invented Its Own Algorithms)](https://www.youtube.com/watch?v=W31ro8YT7jc)**

Google DeepMind's AlphaEvolve just broke long-standing mathematical records by evolving algorithms that improved several ...

📺 AI Revolution

👁️ 21K • 👍 702 • 💬 41 • ⏱️ 10:41 • 15h ago

---

**[The First Crack in the AI Bubble Just Appeared](https://www.youtube.com/watch?v=tuE_WGSQGLU)**

Meta Platforms is reportedly considering laying off over 20% of its workforce. The company didn't confirm anything, but it also ...

📺 Eurodollar University

👁️ 64K • 👍 2K • 💬 162 • ⏱️ 19:11 • 14h ago

---

**[This FREE AI Video Tool Is Now UNLIMITED (No Watermark)](https://www.youtube.com/watch?v=dnSlTlg8vRo)**

Generate watermark-free 4K cinematic AI videos with Higgsfield → https://higgsfield.ai/s/general-malvaai-qPzcPM Grab the ...

📺 Malva AI

👁️ 8K • 👍 353 • 💬 71 • ⏱️ 8:25 • 1d ago

---

**[BREAKING: Netanyahu Really DEAD? Disappearing Ring in Viral Video Fuels Wild AI Claims](https://www.youtube.com/watch?v=jZjayi4clfY)**

A fresh storm has erupted online after a new video of Israeli Prime Minister Benjamin Netanyahu appeared on X, just as viral ...

📺 midday india

👁️ 5K • 👍 42 • 💬 16 • ⏱️ 3:31 • 9h ago

---

**[Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers! (2029 PREDICTION)](https://www.youtube.com/watch?v=fpETS6q1Hww)**

What is financial freedom? The Business Strategist Daniel Priestley on why AI makes lifestyle businesses easy. Daniel Priestley is ...

📺 The Diary Of A CEO

👁️ 660K • 👍 16K • 💬 3K • ⏱️ 2:02:37 • 1d ago

---

**[10 Claude AI Skills That Will Save You 20+ Hours a Week (Full Power User Guide)](https://www.youtube.com/watch?v=ADByNXt2ouY)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *These ...

📺 Julia McCoy

👁️ 16K • 👍 772 • 💬 40 • ⏱️ 16:22 • 1d ago

---

**[What&#39;s really going on with AI, Expert weighs in | TheStandup](https://www.youtube.com/watch?v=TtX3jDaZG8Y)**

ssh terminal.shop CHECK OUT THEIR NEW PODCAST ON CASEY'S YOUTUBE: @MollyRocket AI researcher Dimitri joins the ...

📺 The PrimeTime

👁️ 139K • 👍 3K • 💬 690 • ⏱️ 42:21 • 3d ago

---

**[Justice League VS. AI](https://www.youtube.com/watch?v=2qjpBuPonmI)**

The Justice League face off against Lex Luthor and his greatest scheme yet, or lack there of. Lex shows off his new Artificial Luthor ...

📺 Solid jj

👁️ 343K • 👍 42K • 💬 2K • ⏱️ 3:27 • 2d ago

---

**[AI Boyfriends Are Taking Over Dating](https://www.youtube.com/watch?v=kHMx2gTKavE)**

What do you think about the rise of AI Boyfriends? Second Channel: @itsAntiAustin Insta: ...

📺 Austin Green

👁️ 2K • 👍 109 • 💬 41 • ⏱️ 38:42 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 7,003 • ❤️ 548 • 5d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 78,794 • ❤️ 797 • 9d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 111,716 • ❤️ 420 • 6d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 8,716 • ❤️ 261 • 4d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 254,662 • ❤️ 507 • 13d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 36,759 • ❤️ 232 • 2d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 644,452 • ❤️ 656 • 1d ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 36,677 • ❤️ 210 • 3d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,271,977 • ❤️ 880 • 15d ago

---

**[LocoTrainer-4B](https://huggingface.co/LocoreMind/LocoTrainer-4B)**

*LocoreMind*

LocoTrainer-4B is a 4B parameter text-generation model specialized for MS-SWIFT codebase analysis. It excels at multi-turn tool-calling for tasks like code navigation and report generation, leveraging a 32K context window for in-depth analysis.

`text-generation` `4.0B`

⬇️ 1,575 • ❤️ 174 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 14 • 💬 0 • ⭐ 34,973 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 27 • 💬 2 • ⭐ 27,911 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 109 • 💬 5 • ⭐ 3,243 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 10 • 💬 5 • ⭐ 637 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 163 • 💬 3 • ⭐ 7,284 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 12 • 💬 1 • ⭐ 9,897 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,427 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 50,088 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 46 • 💬 1 • ⭐ 73,349 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://huggingface.co/papers/2411.11581)**

*Ziyi Yang, Zaibin Zhang, Zirui Zheng et al. (23 authors)*

OASIS is a scalable and generalizable social media simulator that models large-scale user interactions and replicates complex social phenomena across platforms.

▲ 1 • 💬 0 • ⭐ 3,401 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2411.11581) • [💻 code](https://github.com/camel-ai/oasis)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 39.5k • 🔱 5.5k • 19h ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.1k • 🔱 979 • 3d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.4k • 🔱 1.5k • 2h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 10.4k • 🔱 957 • 23h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.6k • 🔱 694 • 3h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`HTML` `agency` `agent` `pip` `pua`

⭐ 8.2k • 🔱 389 • 1d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.4k • 🔱 761 • 12h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 3.5k • 🔱 254 • 1d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.9k • 🔱 93 • 5d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 2.8k • 🔱 188 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
