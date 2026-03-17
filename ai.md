---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-17T19:15:56.420234+00:00'
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

**Last Updated:** March 17, 2026 at 19:15 UTC  
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

7h ago

---

**[Nvidia unveils AI infrastructure spanning chips to space computing](https://www.reddit.com/r/artificial/comments/1rw8rz6/nvidia_unveils_ai_infrastructure_spanning_chips/)**

Nvidia unveils Vera CPU and Rubin platform to power agentic AI systems and next-generation AI factories.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/nvidia-vera-cpu-vera-rubin-ai-factories) • 4h ago

---

**[‘Pokémon Go’ players unknowingly trained delivery robots with 30 billion images](https://www.reddit.com/r/artificial/comments/1rva72t/pokémon_go_players_unknowingly_trained_delivery/)**

The massive crowdsourcing effort could use real-world to help robots deliver pizza.

🔗 [Popular Science](https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/?_bhlid=b5452cec2227e1f7d072b583b08fbb55784f34ab) • 1d ago

---

**[Is 'big tech' pushing AI to save themselves money?](https://www.reddit.com/r/artificial/comments/1rwac9p/is_big_tech_pushing_ai_to_save_themselves_money/)**

I was reading this story and it same quite apparent that all the big job cuts seem to within tech, like 10,000s at a time. Then that got me thinking, is this really what they use AI for? It's like a guise to get rid is staff and something to blame. Are there any other types of business getting rid of 1000s of staff at a time like this?

3h ago

---

**[Building AI agents taught me that most safety problems happen at the execution layer, not the prompt layer. So I built an authorization boundary](https://www.reddit.com/r/artificial/comments/1rwfaf7/building_ai_agents_taught_me_that_most_safety/)**

Something I kept running into while experimenting with autonomous agents is that most AI safety discussions focus on the wrong layer. A lot of the conversation today revolves around: • prompt alignment • jailbreaks • output filtering • sandboxing Those things matter, but once agents can interact with real systems, the real risks look different. This is not about AGI alignment or superintelligence scenarios. It is about keeping today’s tool-using agents from accidentally: • burning your API budget • spawning runaway loops • provisioning infrastructure repeatedly • calling destructive tools at the wrong time An agent does not need to be malicious to cause problems. It only needs permission to do things like: • retry the same action endlessly • spawn too many parallel tasks • repeatedly call expensive APIs • chain tool calls in unexpected ways Humans ran into similar issues when building distributed systems. We solved them with things like rate limits, idempotency keys, concurrency limits, and execution guards. That made me wonder if agent systems might need something similar at the execution layer. So I started experimenting with an idea I call an execution authorization boundary. Conceptually it looks like this: proposes action +-------------------------------+ | Agent Runtime | +-------------------------------+ v +-------------------------------+ | Authorization Check | | (policy + current state) | +-------------------------------+ | | ALLOW DENY | | v v +----------------+ +-------------------------+ | Tool Execution | | Blocked Before Execution| +----------------+ +-------------------------+ The runtime proposes an action. A deterministic policy evaluates it against the current state. If allowed, the system emits a cryptographically verifiable authorization artifact. If denied, the action never executes. Example rules might look like: • daily tool budget ≤ $5 • no more than 3 concurrent tool calls • destructive actions require explicit confirmation • replayed actions are rejected I have been experimenting with this model in a small open source project called OxDeAI. It includes: • a deterministic policy engine • cryptographic authorization artifacts • tamper evident audit chains • verification envelopes • runtime adapters for LangGraph, CrewAI, AutoGen, OpenAI Agents and OpenClaw All the demos run the same simple scenario: ALLOW ALLOW DENY verifyEnvelope() => ok Two actions execute. The third is blocked before any side effects occur. There is also a short demo GIF showing the flow in practice. Repo if anyone is curious: https://github.com/AngeYobo/oxdeai Mostly interested in hearing how others building agent systems are handling this layer. Are people solving execution safety with policy engines, capability models, sandboxing, something else entirely, or just accepting the risk for now?

34m ago

---

**[I built an open-source MCP server/ AI web app for real-time flight and satellite tracking — ask Claude "what's flying over Europe right now?](https://www.reddit.com/r/artificial/comments/1rw8se9/i_built_an_opensource_mcp_server_ai_web_app_for/)**

I've been deep in the MCP space and combined it with my other obsession — planes. That led me to build SkyIntel/ Open Sky Intelligence- an AI powered web app, and also an MCP server that compatible with Claude Code, Claude Desktop (and other MCP Clients). You can install sky intel via pip install skyintel. The web app is a full 3D application, which can seamlessly integrate with your Anthropic, Gemini, ChatGPT key via BYOK option. One command to get started: pip install skyintel && skyintel serve Install within your Claude Code/ Claude Desktop and ask: "What aircraft are currently over the Atlantic?" "Where is the ISS right now?" "Show me military aircraft over Europe" "What's the weather at this flight's destination?" Here's a brief technical overview of SkyIntel MCP server and web app. I strongly encouraged you to read the READM.md file of skyintel GitHub repo. It's very comprehensive. 15 MCP tools across aviation + satellite data 10,000+ live aircraft on a CesiumJS 3D globe 300+ satellites with SGP4 orbital propagation BYOK AI chat (Claude/OpenAI/Gemini) — keys never leave your browser System prompt hardening + LLM Guard scanners Built with FastMCP, LiteLLM, LangFuse, Claude I leveraged free and open public data (see README.md). Here are the links: GitHub: https://github.com/0xchamin/skyintel Web demo: https://www.skyintel.dev PyPI: https://pypi.org/project/skyintel/ I would love to hear your feedback. Ask questions, I'm happy to answer. Also, I greatly appreciate if you could star the GitHub repo if you find it useful. Many thanks!

4h ago

---

**[Built an autonomous system where 5 AI models argue about geopolitical crisis outcomes: Here's what I learned about model behavior](https://www.reddit.com/r/artificial/comments/1rvhxqv/built_an_autonomous_system_where_5_ai_models/)**

I built a pipeline where 5 AI models (Claude, GPT-4o, Gemini, Grok, DeepSeek) independently assess the probability of 30+ crisis scenarios twice daily. None of them see the others' outputs. An orchestrator synthesizes their reasoning into final projections. Some observations after 15 days of continuous operation: The models frequently disagree, sometimes by 25+ points. Grok tends to run hot on scenarios with OSINT signals. The orchestrator has to resolve these tensions every cycle. The models anchored to their own previous outputs when shown current probabilities, so I made them blind. Named rules in prompts became shortcuts the models cited instead of actually reasoning. Google Search grounding prevented source hallucination but not content hallucination, the model fabricated a $138 oil price while correctly citing Bloomberg as the source. Three active theaters: Iran, Taiwan, AGI. A Black Swan tab pulls the high-severity low-probability scenarios across all of them. devblog at /blog covers the prompt engineering insights and mistakes I've encountered along the way in detail. doomclock.app

1d ago

---

**[I built a visual drag-and-drop ML trainer (no code required). Free & open source.](https://www.reddit.com/r/artificial/comments/1rvrbjv/i_built_a_visual_draganddrop_ml_trainer_no_code/)**

For those are tired of writing the same ML boilerplate every single time or to beginners who don't have coding experience. MLForge is an app that lets you visually craft a machine learning pipeline. You build your pipeline like a node graph across three tabs: Data Prep - drag in a dataset (MNIST, CIFAR10, etc), chain transforms, end with a DataLoader. Add a second chain with a val DataLoader for proper validation splits. Model - connect layers visually. Input -> Linear -> ReLU -> Output. A few things that make this less painful than it sounds: Drop in a MNIST (or any dataset) node and the Input shape auto-fills to 1, 28, 28 Connect layers and in_channels / in_features propagate automatically After a Flatten, the next Linear's in_features is calculated from the conv stack above it, so no more manually doing that math Robust error checking system that tries its best to prevent shape errors. Training - Drop in your model and data node, wire them to the Loss and Optimizer node, press RUN. Watch loss curves update live, saves best checkpoint automatically. Inference - Open up the inference window where you can drop in your checkpoints and evaluate your model on test data. Pytorch Export - After your done with your project, you have the option of exporting your project into pure PyTorch, just a standalone file that you can run and experiment with. Free, open source. Project showcase is on README in Github repo. GitHub: https://github.com/zaina-ml/ml_forge To install MLForge, enter the following in your command prompt pip install zaina-ml-forge Then ml-forge Please, if you have any feedback feel free to comment it below. My goal is to make this software that can be used by beginners and pros. This is v1.0 so there will be rough edges, if you find one, drop it in the comments and I'll fix it.

18h ago

---

**[Agentic pipeline that builds complete Godot games from a text prompt](https://www.reddit.com/r/artificial/comments/1rvdzdr/agentic_pipeline_that_builds_complete_godot_games/)**

Open source: https://github.com/htdt/godogen

1d ago

---

**[Rant: AI itself is scary. This could be very bad for the future. Anyone else feel way?](https://www.reddit.com/r/artificial/comments/1rwdb9z/rant_ai_itself_is_scary_this_could_be_very_bad/)**

Is anyone else scared of how AI content on social media just exponentially ramps up the misinformation and bullshit that the world will consume now? People like us in this sub are smart enough to look out for the clues and take all content with a grain of salt. But the general public may not be, and all the fake AI slop will literally form peoples perspectives and beliefs of the world At best: some people will just turn out stupid. At worst: people in power will make really bad decisions, hatred could be perpetuated and people will get physically hurt. Am I catastrophizing, or does anyone else feel this way?

1h ago

---

---

## Google News: "ai"

**[Tennessee teens sue Elon Musk's xAI over AI-generated child sexual abuse material](https://www.npr.org/2026/03/16/nx-s1-5749490/xai-elon-musk-sexualized-images)**

The three girls say that the nonconsensual nude images were created by a perpetrator who used AI company xAI's image generation tools.

NPR • 18h ago

---

**[NVIDIA DLSS 5 Delivers AI-Powered Breakthrough in Visual Fidelity for Games](http://nvidianews.nvidia.com/news/nvidia-dlss-5-delivers-ai-powered-breakthrough-in-visual-fidelity-for-games)**

NVIDIA today unveiled NVIDIA DLSS 5, the company’s most significant breakthrough in computer graphics since the debut of real-time ray tracing in 2018.

NVIDIA Newsroom • 20h ago

---

**[Nvidia faces gamer backlash over 'breakthrough' AI graphics feature](https://www.bbc.com/news/articles/cdxg15eyv5ko)**

Nvidia says the tool will transform game graphics - critics warn it could squeeze out artistic expression.

BBC • 5h ago

---

**[DLSS 5 looks like a real-time generative AI filter for video games](https://www.theverge.com/news/895472/nvidia-dlss5-generative-ai-pc-graphics)**

Photoreal or Instagram filter-real?

The Verge • 21h ago

---

**[Senator introduces bill to draw red lines limiting AI use by military](https://www.nbcnews.com/tech/security/senator-introduces-bill-draw-red-lines-ai-use-military-rcna263905)**

The bill seeks to codify several existing Defense Department guidelines in addition to other limits.

NBC News • 34m ago

---

**[Software giant cuts more than 250 San Francisco jobs in pivot to AI](https://www.sfchronicle.com/tech/article/atlassian-layoffs-san-francisco-22081640.php)**

San Francisco Chronicle • 2h ago

---

**[Mississippi River mayors warn AI, fuel costs and drought are straining key waterway](https://www.yahoo.com/news/articles/mississippi-river-mayors-warn-ai-182436974.html)**

The mayors sounded the alarm about the danger of neglecting a key waterway.

Yahoo • 51m ago

---

**[Senators tell ByteDance to 'immediately shut down' Seedance AI video app](https://www.cnbc.com/2026/03/17/bytedance-seedance-shut-down-tiktok-marsha-blackburn-peter-welch.html)**

Lawmakers say the new version of the Seedance AI video-generation app violates copyright and intellectual property laws.

CNBC • 10h ago

---

**[Opinion | For all but two nations, the AI race is already over](https://www.washingtonpost.com/opinions/2026/03/17/ai-canada-europe-strategy-competition/)**

Middle powers such as Europe and Canada need to get smart about artificial intelligence.

The Washington Post • 1h ago

---

**[China Is Embracing OpenClaw, a New A.I. Agent, and the Government Is Wary](https://www.nytimes.com/2026/03/17/business/china-ai-agent.html)**

The New York Times • 1h ago

---

---

## HackerNews: "ai"

**[$96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor](https://news.ycombinator.com/item?id=47385935)**

Contribute to novatic14/MANPADS-System-Launcher-and-Rocket development by creating an account on GitHub.

⬆️ 435 • 💬 377 • 2d ago • [GitHub](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

---

**[Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646)**

⬆️ 414 • 💬 595 • 2d ago

---

**[The Appalling Stupidity of Spotify's AI DJ](https://news.ycombinator.com/item?id=47385272)**

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

⬆️ 366 • 💬 292 • 2d ago • [charlespetzold.com](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

---

**[AirPods Max 2](https://news.ycombinator.com/item?id=47398681)**

The ultimate over-ear listening experience — in five vibrant colors and with up to 1.5x more Active Noise Cancellation than the previous generation.

⬆️ 310 • 💬 539 • 1d ago • [Apple](https://www.apple.com/airpods-max/)

---

**[Airbus is preparing two uncrewed combat aircraft](https://news.ycombinator.com/item?id=47382277)**

Airbus is working at full throttle to offer the German Air Force an operational Uncrewed Collaborative Combat Aircraft (UCCA) system by 2029.

⬆️ 182 • 💬 132 • 2d ago • [Airbus](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

---

**[Nvidia Launches Vera CPU, Purpose-Built for Agentic AI](https://news.ycombinator.com/item?id=47404074)**

NVIDIA today launched the NVIDIA Vera CPU, the world’s first processor purpose-built for the age of agentic AI and reinforcement learning — delivering results with twice the efficiency and 50% faster than traditional rack-scale CPUs.

⬆️ 169 • 💬 99 • 23h ago • [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

---

**[Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)](https://news.ycombinator.com/item?id=47401734)**

Large language models (LLMs) have demonstrated the promise to revolutionize the field of software engineering. Among other things, LLM agents are rapidly gaining momentum in software development, with practitioners reporting a multifold increase in productivity after adoption. Yet, empirical evidence is lacking around these claims. In this paper, we estimate the causal effect of adopting a widely popular LLM agent assistant, namely Cursor, on development velocity and software quality. The estimation is enabled by a state-of-the-art difference-in-differences design comparing Cursor-adopting GitHub projects with a matched control group of similar GitHub projects that do not use Cursor. We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity. Further panel generalized-method-of-moments estimation reveals that increases in static analysis warnings and code complexity are major factors driving long-term velocity slowdown. Our study identifies quality assurance as a major bottleneck for early Cursor adopters and calls for it to be a first-class citizen in the design of agentic AI coding tools and AI-driven workflows.

⬆️ 136 • 💬 74 • 1d ago • [arXiv.org](https://arxiv.org/abs/2511.04427)

---

**[Apideck CLI – An AI-agent interface with much lower context consumption than MCP](https://news.ycombinator.com/item?id=47400261)**

TL;DR: MCP tool definitions can burn 55,000+ tokens before an agent processes a single user message. We built the Apideck CLI as an AI-agent interface instead:an ~80-token agent prompt replaces tens of thousands of tokens of schema, with progressive disclosure via `--help` and structural safety baked into the binary. Any agent that can run shell commands can use it. No protocol support required.

⬆️ 132 • 💬 120 • 1d ago • [Apideck](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

---

**[Why I may ‘hire’ AI instead of a graduate student](https://news.ycombinator.com/item?id=47396557)**

⬆️ 100 • 💬 105 • 1d ago • [science.org](https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student)

---

**[Tell HN: AI tools are making me lose interest in CS fundamentals](https://news.ycombinator.com/item?id=47394291)**

⬆️ 94 • 💬 88 • 1d ago

---

---

## YouTube Videos: "ai"

**[Google’s New AI Just Broke Math… (Invented Its Own Algorithms)](https://www.youtube.com/watch?v=W31ro8YT7jc)**

Google DeepMind's AlphaEvolve just broke long-standing mathematical records by evolving algorithms that improved several ...

📺 AI Revolution

👁️ 26K • 👍 853 • 💬 55 • ⏱️ 10:41 • 20h ago

---

**[The First Crack in the AI Bubble Just Appeared](https://www.youtube.com/watch?v=tuE_WGSQGLU)**

Meta Platforms is reportedly considering laying off over 20% of its workforce. The company didn't confirm anything, but it also ...

📺 Eurodollar University

👁️ 80K • 👍 3K • 💬 194 • ⏱️ 19:11 • 20h ago

---

**[Why AI Researchers Are Quitting and Panicking on the Way Out](https://www.youtube.com/watch?v=rtT87iAm_SM)**

Top AI researchers are walking away from some of the most powerful tech companies on Earth, and their reasons are raising ...

📺 The Infographics Show

👁️ 250K • 👍 7K • 💬 1K • ⏱️ 14:48 • 19h ago

---

**[This FREE AI Video Tool Is Now UNLIMITED (No Watermark)](https://www.youtube.com/watch?v=dnSlTlg8vRo)**

Generate watermark-free 4K cinematic AI videos with Higgsfield → https://higgsfield.ai/s/general-malvaai-qPzcPM Grab the ...

📺 Malva AI

👁️ 10K • 👍 408 • 💬 75 • ⏱️ 8:25 • 1d ago

---

**[10 Claude AI Skills That Will Save You 20+ Hours a Week (Full Power User Guide)](https://www.youtube.com/watch?v=ADByNXt2ouY)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *These ...

📺 Julia McCoy

👁️ 17K • 👍 820 • 💬 43 • ⏱️ 16:22 • 2d ago

---

**[BREAKING: Netanyahu Really DEAD? Disappearing Ring in Viral Video Fuels Wild AI Claims](https://www.youtube.com/watch?v=jZjayi4clfY)**

A fresh storm has erupted online after a new video of Israeli Prime Minister Benjamin Netanyahu appeared on X, just as viral ...

📺 midday india

👁️ 8K • 👍 53 • 💬 27 • ⏱️ 3:31 • 14h ago

---

**[Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers! (2029 PREDICTION)](https://www.youtube.com/watch?v=fpETS6q1Hww)**

What is financial freedom? The Business Strategist Daniel Priestley on why AI makes lifestyle businesses easy. Daniel Priestley is ...

📺 The Diary Of A CEO

👁️ 745K • 👍 18K • 💬 3K • ⏱️ 2:02:37 • 1d ago

---

**[Justice League VS. AI](https://www.youtube.com/watch?v=2qjpBuPonmI)**

The Justice League face off against Lex Luthor and his greatest scheme yet, or lack there of. Lex shows off his new Artificial Luthor ...

📺 Solid jj

👁️ 346K • 👍 42K • 💬 2K • ⏱️ 3:27 • 3d ago

---

**[Is Netanyahu Alive? AI Chatbot ‘Grok’ Terms Israeli PM’s Coffee Video AI-Generated ‘Deepfake’](https://www.youtube.com/watch?v=Pg0bwStf8_w)**

Is the Israeli PM dead or alive? Benjamin Netanyahu drops a video online mocking his death rumours. But many users as well as ...

📺 Times Of India

👁️ 14K • 👍 177 • 💬 93 • ⏱️ 9:29 • 1d ago

---

**[AI is making CEOs delusional](https://www.youtube.com/watch?v=Q6nem-F8AG8)**

Your CEO tries AI once over the weekend and by Monday your company is "AI-first" smh https://x.com/atmoio ...

📺 Mo Bitar

👁️ 142K • 👍 10K • 💬 2K • ⏱️ 7:30 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 7,003 • ❤️ 571 • 6d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 78,794 • ❤️ 821 • 9d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 111,716 • ❤️ 468 • 6d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 8,716 • ❤️ 269 • 4d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 254,662 • ❤️ 513 • 13d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 36,759 • ❤️ 234 • 3d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 644,452 • ❤️ 661 • 2d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,271,977 • ❤️ 887 • 15d ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 36,677 • ❤️ 213 • 3d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

`119.4B`

⬇️ 1,872 • ❤️ 186 • 5h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AI Can Learn Scientific Taste](https://huggingface.co/papers/2603.14473)**

*Jingqi Tong, Mingzhe Li, Hangcheng Li et al. (23 authors)*

🏢 OpenMOSS

Great scientists have strong judgement and foresight, closely tied to what we call scientific taste. Here, we use the term to refer to the capacity to judge and propose research ideas with high potential impact. However, most relative research focuses on improving an AI scientist's executive capability, while enhancing an AI's scientific taste remains underexplored. In this work, we propose Reinforcement Learning from Community Feedback (RLCF), a training paradigm that uses large-scale community signals as supervision, and formulate scientific taste learning as a preference modeling and alignment problem. For preference modeling, we train Scientific Judge on 700K field- and time-matched pairs of high- vs. low-citation papers to judge ideas. For preference alignment, using Scientific Judge as a reward model, we train a policy model, Scientific Thinker, to propose research ideas with high potential impact. Experiments show Scientific Judge outperforms SOTA LLMs (e.g., GPT-5.2, Gemini 3 Pro) and generalizes to future-year test, unseen fields, and peer-review preference. Furthermore, Scientific Thinker proposes research ideas with higher potential impact than baselines. Our findings show that AI can learn scientific taste, marking a key step toward reaching human-level AI scientists.

▲ 210 • 💬 1 • ⭐ 243 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.14473) • [💻 code](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste) • [🔗 project](https://tongjingqi.github.io/AI-Can-Learn-Scientific-Taste/)

---

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

▲ 28 • 💬 2 • ⭐ 27,911 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[Grounding World Simulation Models in a Real-World Metropolis](https://huggingface.co/papers/2603.15583)**

*Junyoung Seo, Hyunwook Choi, Minkyung Kwon et al. (13 authors)*

🏢 NAVER AI Lab

What if a world simulation model could render not an imagined environment but a city that actually exists? Prior generative world models synthesize visually plausible yet artificial environments by imagining all content. We present Seoul World Model (SWM), a city-scale world model grounded in the real city of Seoul. SWM anchors autoregressive video generation through retrieval-augmented conditioning on nearby street-view images. However, this design introduces several challenges, including temporal misalignment between retrieved references and the dynamic target scene, limited trajectory diversity and data sparsity from vehicle-mounted captures at sparse intervals. We address these challenges through cross-temporal pairing, a large-scale synthetic dataset enabling diverse camera trajectories, and a view interpolation pipeline that synthesizes coherent training videos from sparse street-view images. We further introduce a Virtual Lookahead Sink to stabilize long-horizon generation by continuously re-grounding each chunk to a retrieved image at a future location. We evaluate SWM against recent video world models across three cities: Seoul, Busan, and Ann Arbor. SWM outperforms existing methods in generating spatially faithful, temporally consistent, long-horizon videos grounded in actual urban environments over trajectories reaching hundreds of meters, while supporting diverse camera movements and text-prompted scenario variations.

▲ 87 • 💬 2 • ⭐ 150 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15583) • [💻 code](https://github.com/naver-ai/seoul-world-model) • [🔗 project](https://seoul-world-model.github.io/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 112 • 💬 5 • ⭐ 3,332 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data](https://huggingface.co/papers/2603.15594)**

*Yuwen Du, Rui Ye, Shuo Tang et al. (7 authors)*

🏢 OpenSeeker

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet the development of high-performance search agents remains dominated by industrial giants due to a lack of transparent, high-quality training data. This persistent data scarcity has fundamentally hindered the progress of the broader research community in developing and innovating within this domain. To bridge this gap, we introduce OpenSeeker, the first fully open-source search agent (i.e., model and data) that achieves frontier-level performance through two core technical innovations: (1) Fact-grounded scalable controllable QA synthesis, which reverse-engineers the web graph via topological expansion and entity obfuscation to generate complex, multi-hop reasoning tasks with controllable coverage and complexity. (2) Denoised trajectory synthesis, which employs a retrospective summarization mechanism to denoise the trajectory, therefore promoting the teacher LLMs to generate high-quality actions. Experimental results demonstrate that OpenSeeker, trained (a single training run) on only 11.7k synthesized samples, achieves state-of-the-art performance across multiple benchmarks including BrowseComp, BrowseComp-ZH, xbench-DeepSearch, and WideSearch. Notably, trained with simple SFT, OpenSeeker significantly outperforms the second-best fully open-source agent DeepDive (e.g., 29.5% v.s. 15.3% on BrowseComp), and even surpasses industrial competitors such as Tongyi DeepResearch (trained via extensive continual pre-training, SFT, and RL) on BrowseComp-ZH (48.4% v.s. 46.7%). We fully open-source the complete training dataset and the model weights to democratize frontier search agent research and foster a more transparent, collaborative ecosystem.

▲ 119 • 💬 2 • ⭐ 104 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15594) • [💻 code](https://github.com/rui-ye/OpenSeeker)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 11 • 💬 5 • ⭐ 637 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 163 • 💬 3 • ⭐ 7,284 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,516 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 50,154 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 40.0k • 🔱 5.5k • 1d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.1k • 🔱 980 • 1h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.4k • 🔱 1.5k • 2h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 10.6k • 🔱 963 • 1d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.7k • 🔱 697 • 9h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`HTML` `agency` `agent` `pip` `pua`

⭐ 8.3k • 🔱 395 • 4h ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.5k • 🔱 762 • 17h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 3.7k • 🔱 283 • 3h ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.9k • 🔱 93 • 6d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 2.9k • 🔱 189 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
