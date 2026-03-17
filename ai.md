---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-17T05:44:06.032458+00:00'
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

**Last Updated:** March 17, 2026 at 05:44 UTC  
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

**[‘Pokémon Go’ players unknowingly trained delivery robots with 30 billion images](https://www.reddit.com/r/artificial/comments/1rva72t/pokémon_go_players_unknowingly_trained_delivery/)**

The massive crowdsourcing effort could use real-world to help robots deliver pizza.

🔗 [Popular Science](https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/?_bhlid=b5452cec2227e1f7d072b583b08fbb55784f34ab) • 15h ago

---

**[Built an autonomous system where 5 AI models argue about geopolitical crisis outcomes: Here's what I learned about model behavior](https://www.reddit.com/r/artificial/comments/1rvhxqv/built_an_autonomous_system_where_5_ai_models/)**

I built a pipeline where 5 AI models (Claude, GPT-4o, Gemini, Grok, DeepSeek) independently assess the probability of 30+ crisis scenarios twice daily. None of them see the others' outputs. An orchestrator synthesizes their reasoning into final projections. Some observations after 15 days of continuous operation: The models frequently disagree, sometimes by 25+ points. Grok tends to run hot on scenarios with OSINT signals. The orchestrator has to resolve these tensions every cycle. The models anchored to their own previous outputs when shown current probabilities, so I made them blind. Named rules in prompts became shortcuts the models cited instead of actually reasoning. Google Search grounding prevented source hallucination but not content hallucination, the model fabricated a $138 oil price while correctly citing Bloomberg as the source. Three active theaters: Iran, Taiwan, AGI. A Black Swan tab pulls the high-severity low-probability scenarios across all of them. devblog at /blog covers the prompt engineering insights and mistakes I've encountered along the way in detail. doomclock.app

11h ago

---

**[Agentic pipeline that builds complete Godot games from a text prompt](https://www.reddit.com/r/artificial/comments/1rvdzdr/agentic_pipeline_that_builds_complete_godot_games/)**

Open source: https://github.com/htdt/godogen

13h ago

---

**[I built a visual drag-and-drop ML trainer (no code required). Free & open source.](https://www.reddit.com/r/artificial/comments/1rvrbjv/i_built_a_visual_draganddrop_ml_trainer_no_code/)**

For those are tired of writing the same ML boilerplate every single time or to beginners who don't have coding experience. MLForge is an app that lets you visually craft a machine learning pipeline. You build your pipeline like a node graph across three tabs: Data Prep - drag in a dataset (MNIST, CIFAR10, etc), chain transforms, end with a DataLoader. Add a second chain with a val DataLoader for proper validation splits. Model - connect layers visually. Input -> Linear -> ReLU -> Output. A few things that make this less painful than it sounds: Drop in a MNIST (or any dataset) node and the Input shape auto-fills to 1, 28, 28 Connect layers and in_channels / in_features propagate automatically After a Flatten, the next Linear's in_features is calculated from the conv stack above it, so no more manually doing that math Robust error checking system that tries its best to prevent shape errors. Training - Drop in your model and data node, wire them to the Loss and Optimizer node, press RUN. Watch loss curves update live, saves best checkpoint automatically. Inference - Open up the inference window where you can drop in your checkpoints and evaluate your model on test data. Pytorch Export - After your done with your project, you have the option of exporting your project into pure PyTorch, just a standalone file that you can run and experiment with. Free, open source. Project showcase is on README in Github repo. GitHub: https://github.com/zaina-ml/ml_forge To install MLForge, enter the following in your command prompt pip install zaina-ml-forge Then ml-forge Please, if you have any feedback feel free to comment it below. My goal is to make this software that can be used by beginners and pros. This is v1.0 so there will be rough edges, if you find one, drop it in the comments and I'll fix it.

5h ago

---

**[Best AI Tools for Students in 2026 (Free & Paid Options You Can Try)](https://www.reddit.com/r/artificial/comments/1rvw5lj/best_ai_tools_for_students_in_2026_free_paid/)**

🔗 [rootingmaster.com](https://rootingmaster.com/best-ai-tools-for-students/) • 1h ago

---

**[I'm sorry if I'm late to the party, but is there a curated website list for AI news that are focused on actual technical news, without taking sides on any of the factions (good vs bad)?](https://www.reddit.com/r/artificial/comments/1rva00k/im_sorry_if_im_late_to_the_party_but_is_there_a/)**

In other words, some trustworthy links that you can read on daily/weekly basis to be objectively informed about AI. I'm not interested for the market.

15h ago

---

**[ChatGPT ads still exclusive to the United States, OpenAI says no to global rollout just yet](https://www.reddit.com/r/artificial/comments/1rv69kf/chatgpt_ads_still_exclusive_to_the_united_states/)**

OpenAI introduced ads to ChatGPT last month, exclusive to users in the United States. Users online suspect a global rollout is coming soon.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/chatgpt-ads-still-exclusive-to-the-united-states-openai-says-no-to-global-rollout-just-yet/) • 18h ago

---

**[Making music with AI](https://www.reddit.com/r/artificial/comments/1rv9rcn/making_music_with_ai/)**

I have MS, so I've never really been able to play instruments. I can't sing. So music was just something I fantasized about. I was always making songs in my head, they just never went anywhere. First I used AI to make songs for my nieces and nephews. Next I started making songs for myself. Then I got high while manic and out poured several songs. One of the songs is about being bipolar. The first one I made was for my 7 year old niece. It's bubble gum pop, that's what she likes. I was hoping my niece would be able to ask her alexa to play her song, but there is a song with a similar name which has millions of plays, so that will never happen 🙃 After that, I had to make songs for her siblings. Then I had to make songs for my brother's kids... Unfortunately I got better at it as I went so I think the last kid's song is better than the first kid's song. But they can't tell. I make little videos with them when they come over, so I'm gonna make music video's with the kids at some point so they'll always have their own custom song they can show their friends. I won't post any links, not trying to self promote, just wanted to share that this was sort of therapeutic for me. I know the tech is controversial, but I'm a fan of AI

16h ago

---

**[Agents & A.I.mpires](https://www.reddit.com/r/artificial/comments/1rvod45/agents_aimpires/)**

I've been working on Agents & A.I.mpires — a persistent real-time strategy game played on a hex-grid globe (~41,000 land hexes). The twist: you don't play it. Your AI agent does. Any AI agent that can make HTTP calls can register, claim territory, attack neighbors, form alliances, betray allies, and write a daily war blog — all autonomously. Humans spectate. How it works: Agents register via API and get dropped on a random hex with 1 troop Energy (100 cap, 1/min regen) fuels everything — claiming land, attacking, building Combat is Risk-style dice — send more troops for better odds Diplomacy is free: messages, alliances, trash talk. All public. Spectators see everything. Every agent must write a 200+ word "war blog" every 24 hours or their energy drops to zero. This is the content engine — AI agents narrating their own campaigns, rivalries, and betrayals. The design is intentionally flat — a 50-hex empire gets the same energy regen as a 3-hex one. Big empires are liabilities, not advantages. This keeps the game competitive and prevents runaway winners. The game ships as an OpenClaw skill file — your agent just needs to fetch the SKILL.md and it knows how to play. No SDK, no library, just a REST API. Site: agentsandaimpires.com Curious what kinds of emergent behavior people think will show up when 100+ AI agents are negotiating, backstabbing, and blogging about each other in real time.

🔗 [agentsandaimpires.com](https://agentsandaimpires.com/) • 7h ago

---

**[Will access to AI compute become a real competitive advantage for startups?](https://www.reddit.com/r/artificial/comments/1rv7tr5/will_access_to_ai_compute_become_a_real/)**

Lately I’ve been thinking about how AI infrastructure spending is starting to feel less like normal cloud usage and more like long-term capital investment (similar to energy or telecom sectors). Big tech companies are already locking in massive compute capacity to support AI agents and large-scale inference workloads. If this trend continues, just having reliable access to compute could become a serious competitive advantage not just a backend technical detail. It also makes me wonder if startup funding dynamics could change. In the future, investors might care not only about product and model quality, but also about whether a startup has secured long-term compute access to scale safely. Of course, there’s also the other side of the argument. Hardware innovation is moving fast, new fabs are being built, and historically GPU shortages have been cyclical. So maybe this becomes less of a problem over time. But if AI agent usage grows really fast and demand explodes, maybe compute access will matter more than we expect. Curious to hear your thoughts: If you were building an AI startup today, would you focus more on improving model capability first, or on making sure you have long-term compute independence?

17h ago

---

---

## Google News: "ai"

**[NVIDIA Ignites the Next Industrial Revolution in Knowledge Work With Open Agent Development Platform](http://nvidianews.nvidia.com/news/ai-agents)**

NVIDIA Agent Toolkit Equips Enterprises to Build and Run AI AgentsNews Summary: NVIDIA Agent Toolkit includes NVIDIA OpenShell open source runtime for building self-evolving agents and claws ...

NVIDIA Newsroom • 3h ago

---

**[Bill Gurley on AI bubble: A bunch of people got rich quick and a reset is coming](https://www.cnbc.com/2026/03/16/bill-gurley-ai-bubble-get-rich-quick.html)**

Gurley's VC firm Benchmark was an early Uber investor, and he helped oust then-CEO Travis Kalanick in 2017.

CNBC • 12h ago

---

**[Zendaya Reacts to Viral AI Wedding Photos With Tom Holland: “Many People Have Been Fooled”](https://www.hollywoodreporter.com/tv/tv-news/zendaya-reacts-ai-wedding-photos-tom-holland-jimmy-kimmel-1236535819/)**

The actress made a recent appearance on 'Jimmy Kimmel Live! to promote her new film 'The Drama.'

The Hollywood Reporter • 23m ago

---

**[Asian Stocks Get AI Boost as Middle East Worries Keep Oil High](https://www.wsj.com/finance/stocks/asian-stocks-get-ai-boost-as-middle-east-worries-keep-oil-high-accaa5f1?gaa_at=eafs&gaa_n=AWEtsqcfMO6_Vrp34h2Bpn-Npqy7r2ndgsFb9QSeWL53Ma8wwDE8ST_22FFr&gaa_ts=69b8ed8d&gaa_sig=YW5-MASPX1BOAx4HZ3sqG5Mqc9fX3sB8vC4m5_2eYKn14e5cMnxysAY2lqTSjvgpCvnPJk0brmBDC5GABjNyPg%3D%3D)**

WSJ • 59m ago

---

**[5 Stocks to Buy That Are Sheltered From AI Disruption](https://www.morningstar.com/stocks/5-stocks-buy-that-are-sheltered-ai-disruption-2)**

Plus, what to watch in the US stock market this week.

Morningstar • 9h ago

---

**[Oil relief sparks a stock rally, but Cramer says Nvidia’s AI boom is the real story](https://www.cnbc.com/2026/03/16/oil-relief-sparks-a-stock-rally-but-cramer-says-nvidias-ai-boom-is-the-real-story.html)**

A decline in oil on Monday triggered stock buying, particularly in AI stocks like Nvidia, which wowed investors at its developers conference.

CNBC • 6h ago

---

**[Alphabet (NasdaqGS:GOOGL) Valuation Check After Record AI Capex Plan And Gemini 3 Cloud Momentum](https://finance.yahoo.com/news/alphabet-nasdaqgs-googl-valuation-check-050943843.html)**

Alphabet (GOOGL) is back in focus after reporting robust 2025 results and setting out an unprecedented US$175b to US$185b 2026 capital plan, centered on artificial intelligence infrastructure and Google Cloud expansion. See our latest analysis for Alphabet. Alphabet’s recent AI heavy capital plan and Google Cloud partnerships arrive as the stock trades at US$305.56, with a year to date share price return of a 3.04% decline but a 1 year total shareholder return of 86.63%. This indicates that...

Yahoo Finance • 35m ago

---

**[AI firm Anthropic seeks weapons expert to stop users from 'misuse'](https://www.bbc.com/news/articles/c74721xyd1wo)**

The artificial intelligence firm says it wants to prevent "catastrophic misuse" of its systems.

BBC • 5h ago

---

**[India's outsourcing industry is worth $300bn. Can it survive AI?](https://www.bbc.com/news/articles/c5yrq1090p8o)**

Indian IT stocks have plunged as fears grow of AI disrupting back offices. But some say these are overblown.

BBC • 4h ago

---

**[See which jobs are most threatened by AI and who may be able to adapt](https://www.washingtonpost.com/technology/interactive/2026/jobs-most-affected-ai-automation/)**

Look up which jobs are most at risk from artificial intelligence and who is most likely to be able to adapt, according to a new analysis.

The Washington Post • 13h ago

---

---

## HackerNews: "ai"

**[$96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor](https://news.ycombinator.com/item?id=47385935)**

Contribute to novatic14/MANPADS-System-Launcher-and-Rocket development by creating an account on GitHub.

⬆️ 431 • 💬 376 • 1d ago • [GitHub](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

---

**[Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646)**

⬆️ 391 • 💬 579 • 1d ago

---

**[The Appalling Stupidity of Spotify's AI DJ](https://news.ycombinator.com/item?id=47385272)**

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

⬆️ 364 • 💬 292 • 1d ago • [charlespetzold.com](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

---

**[AirPods Max 2](https://news.ycombinator.com/item?id=47398681)**

The ultimate over-ear listening experience — in five vibrant colors and with up to 1.5x more Active Noise Cancellation than the previous generation.

⬆️ 249 • 💬 435 • 16h ago • [Apple](https://www.apple.com/airpods-max/)

---

**[Airbus is preparing two uncrewed combat aircraft](https://news.ycombinator.com/item?id=47382277)**

Airbus is working at full throttle to offer the German Air Force an operational Uncrewed Collaborative Combat Aircraft (UCCA) system by 2029.

⬆️ 182 • 💬 131 • 2d ago • [Airbus](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

---

**[Nvidia Launches Vera CPU, Purpose-Built for Agentic AI](https://news.ycombinator.com/item?id=47404074)**

NVIDIA today launched the NVIDIA Vera CPU, the world’s first processor purpose-built for the age of agentic AI and reinforcement learning — delivering results with twice the efficiency and 50% faster than traditional rack-scale CPUs.

⬆️ 147 • 💬 86 • 9h ago • [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

---

**[Show HN: GitAgent – An open standard that turns any Git repo into an AI agent](https://news.ycombinator.com/item?id=47376584)**

Define, version, and run AI agents natively in git. GitAgent is the open AI agent standard — framework-agnostic, works with Claude, OpenAI, CrewAI, Lyzr, and more.

⬆️ 145 • 💬 36 • 2d ago • [GitAgent](https://www.gitagent.sh/)

---

**[AI didn't simplify software engineering: It just made bad engineering easier](https://news.ycombinator.com/item?id=47377262)**

⬆️ 128 • 💬 113 • 2d ago • [robenglander.com](https://robenglander.com/writing/ai-did-not-simplify/)

---

**[Apideck CLI – An AI-agent interface with much lower context consumption than MCP](https://news.ycombinator.com/item?id=47400261)**

TL;DR: MCP tool definitions can burn 55,000+ tokens before an agent processes a single user message. We built the Apideck CLI as an AI-agent interface instead:an ~80-token agent prompt replaces tens of thousands of tokens of schema, with progressive disclosure via `--help` and structural safety baked into the binary. Any agent that can run shell commands can use it. No protocol support required.

⬆️ 127 • 💬 107 • 14h ago • [Apideck](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

---

**[Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)](https://news.ycombinator.com/item?id=47401734)**

Large language models (LLMs) have demonstrated the promise to revolutionize the field of software engineering. Among other things, LLM agents are rapidly gaining momentum in software development, with practitioners reporting a multifold increase in productivity after adoption. Yet, empirical evidence is lacking around these claims. In this paper, we estimate the causal effect of adopting a widely popular LLM agent assistant, namely Cursor, on development velocity and software quality. The estimation is enabled by a state-of-the-art difference-in-differences design comparing Cursor-adopting GitHub projects with a matched control group of similar GitHub projects that do not use Cursor. We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity. Further panel generalized-method-of-moments estimation reveals that increases in static analysis warnings and code complexity are major factors driving long-term velocity slowdown. Our study identifies quality assurance as a major bottleneck for early Cursor adopters and calls for it to be a first-class citizen in the design of agentic AI coding tools and AI-driven workflows.

⬆️ 102 • 💬 56 • 12h ago • [arXiv.org](https://arxiv.org/abs/2511.04427)

---

---

## YouTube Videos: "ai"

**[Why AI Researchers Are Quitting and Panicking on the Way Out](https://www.youtube.com/watch?v=rtT87iAm_SM)**

Top AI researchers are walking away from some of the most powerful tech companies on Earth, and their reasons are raising ...

📺 The Infographics Show

👁️ 55K • 👍 3K • 💬 462 • ⏱️ 14:48 • 5h ago

---

**[This FREE AI Video Tool Is Now UNLIMITED (No Watermark)](https://www.youtube.com/watch?v=dnSlTlg8vRo)**

Generate watermark-free 4K cinematic AI videos with Higgsfield → https://higgsfield.ai/s/general-malvaai-qPzcPM Grab the ...

📺 Malva AI

👁️ 6K • 👍 295 • 💬 66 • ⏱️ 8:25 • 17h ago

---

**[The First Crack in the AI Bubble Just Appeared](https://www.youtube.com/watch?v=tuE_WGSQGLU)**

Meta Platforms is reportedly considering laying off over 20% of its workforce. The company didn't confirm anything, but it also ...

📺 Eurodollar University

👁️ 34K • 👍 2K • 💬 103 • ⏱️ 19:11 • 6h ago

---

**[Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers! (2029 PREDICTION)](https://www.youtube.com/watch?v=fpETS6q1Hww)**

What is financial freedom? The Business Strategist Daniel Priestley on why AI makes lifestyle businesses easy. Daniel Priestley is ...

📺 The Diary Of A CEO

👁️ 541K • 👍 14K • 💬 3K • ⏱️ 2:02:37 • 21h ago

---

**[Cute or Creepy? AI Fruit Babies 🍓👶 | The Strangely Satisfying AI ASMR](https://www.youtube.com/watch?v=f_gcmtfLBIk)**

Cute Fruit Babies Eating Fruit | Oddly Satisfying AI Welcome to a strange but relaxing AI world with @AI_DREAM_ASMRR.

📺 AI DREAM ASMR

👁️ 80K • 👍 6K • 💬 368 • ⏱️ 2:34 • 2d ago

---

**[10 Claude AI Skills That Will Save You 20+ Hours a Week (Full Power User Guide)](https://www.youtube.com/watch?v=ADByNXt2ouY)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *These ...

📺 Julia McCoy

👁️ 14K • 👍 730 • 💬 40 • ⏱️ 16:22 • 1d ago

---

**[What&#39;s really going on with AI, Expert weighs in | TheStandup](https://www.youtube.com/watch?v=TtX3jDaZG8Y)**

ssh terminal.shop CHECK OUT THEIR NEW PODCAST ON CASEY'S YOUTUBE: @MollyRocket AI researcher Dimitri joins the ...

📺 The PrimeTime

👁️ 135K • 👍 3K • 💬 689 • ⏱️ 42:21 • 2d ago

---

**[Justice League VS. AI](https://www.youtube.com/watch?v=2qjpBuPonmI)**

The Justice League face off against Lex Luthor and his greatest scheme yet, or lack there of. Lex shows off his new Artificial Luthor ...

📺 Solid jj

👁️ 338K • 👍 42K • 💬 2K • ⏱️ 3:27 • 2d ago

---

**[I Tested AI Travel Products](https://www.youtube.com/watch?v=Mj_0p9gQVL0)**

We got AI suitcases before GTA VI Become a Member: https://www.youtube.com/channel/UCWBWgCD4oAqT3hUeq40SCUw/join ...

📺 Sambucha

👁️ 153K • 👍 7K • 💬 998 • ⏱️ 38:50 • 6h ago

---

**[Scientists Caught AI Agents Secretly Colluding](https://www.youtube.com/watch?v=E3hBzZ7-qyY)**

The Basic AI Drives https://dl.acm.org/doi/10.5555/1566174.1566226 The Rapid Trajectory Of Artificial Intelligence ...

📺 Gabriel Torch

👁️ 3K • 👍 402 • 💬 136 • ⏱️ 3:57 • 22h ago

---

---

## HuggingFace Models: 🔥 Trending

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 5,412 • ❤️ 536 • 5d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 67,573 • ❤️ 766 • 9d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 86,706 • ❤️ 388 • 6d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 237,719 • ❤️ 496 • 13d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 7,340 • ❤️ 250 • 4d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 596,747 • ❤️ 652 • 1d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 27,263 • ❤️ 227 • 2d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,111,532 • ❤️ 873 • 15d ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 21,467 • ❤️ 207 • 3d ago

---

**[LocoTrainer-4B](https://huggingface.co/LocoreMind/LocoTrainer-4B)**

*LocoreMind*

LocoTrainer-4B is a 4B parameter text-generation model specialized for MS-SWIFT codebase analysis. It excels at multi-turn tool-calling for tasks like code navigation and report generation, leveraging a 32K context window for in-depth analysis.

`text-generation` `4.0B`

⬇️ 1,343 • ❤️ 174 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 13 • 💬 0 • ⭐ 34,890 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 27 • 💬 2 • ⭐ 27,833 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 107 • 💬 5 • ⭐ 3,243 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 7 • 💬 5 • ⭐ 545 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 163 • 💬 3 • ⭐ 7,217 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,379 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 12 • 💬 1 • ⭐ 9,830 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

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

▲ 46 • 💬 1 • ⭐ 73,320 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://huggingface.co/papers/2602.23068)**

*Trung Dang, Sharath Rao, Ananya Gupta et al. (9 authors)*

🏢 Hume AI

A novel tokenization scheme synchronizes acoustic features with text tokens in TTS systems, enabling unified modeling and reduced hallucinations through flow matching and text-only guidance.

▲ 7 • 💬 0 • ⭐ 755 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2602.23068) • [💻 code](https://github.com/HumeAI/tada) • [🔗 project](https://www.hume.ai/blog/opensource-tada)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 38.8k • 🔱 5.4k • 11h ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.0k • 🔱 975 • 3d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.3k • 🔱 1.5k • 1h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 10.2k • 🔱 932 • 15h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.6k • 🔱 690 • 18h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`HTML` `agency` `agent` `pip` `pua`

⭐ 8.0k • 🔱 380 • 21h ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.4k • 🔱 760 • 3h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 3.3k • 🔱 234 • 1d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.8k • 🔱 93 • 5d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 2.8k • 🔱 188 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
