---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-08T03:27:36.423646+00:00'
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

**Last Updated:** July 08, 2026 at 03:27 UTC  
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

**[Air Force Engineer Accused of Cutting Down Flock AI Surveillance Cameras, Says U.S. is Becoming Police State](https://www.reddit.com/r/artificial/comments/1uq91lr/air_force_engineer_accused_of_cutting_down_flock/)**

Jeffrey Sovern faces 25 charges after Virginia police say he destroyed 13 Flock license plate cameras. Supporters are paying his legal bills.

🔗 [Military.com](https://www.military.com/air-force-engineer-accused-of-cutting-down-13-police-cameras-says-they-are-unconstitutional) • 5h ago

---

**[AI can’t simulate human preferences - new study tests LLMs against thousands of real users](https://www.reddit.com/r/artificial/comments/1uq52r8/ai_cant_simulate_human_preferences_new_study/)**

https://arxiv.org/abs/2605.18311 There’s a massive trend right now where companies are trying to replace real human feedback with LLM-driven "synthetic users." The idea sounds great on paper - why would you spend money and time recruiting real people to test products, pick design choices, or evaluate options when you can just prompt? They tested LLMs across 28 real-world studies spanning 78 choice tasks to see if their selections matched thousands of actual human participants. The result? The LLMs matched the human majority only 53% of the time. Since most tasks were a choice between two options, that's pretty much same as flipping a coin. Even worse for the "simulation" argument: adding detailed personas and chain-of-thought reasoning yielded practically no improvement. It actually made the semantic similarity to real human justifications worse because the model's "reasoning" just homogenized the outputs and failed to capture actual lived experiences. It looks like LLMs are just trained to replicate what we like about their outputs rather than making them capable of predicting human preferences. Is it time to admit that LLM simulation has hit a hard wall when it comes to replicating human choice?

8h ago

---

**[AI is scaling 3x faster than the internet wave and it’s NOT slowing down](https://www.reddit.com/r/artificial/comments/1upou8z/ai_is_scaling_3x_faster_than_the_internet_wave/)**

One thing that stands out about the current AI boom is that it hasn't had a slow phase. A lot of previous technology waves had a big moment, cooled off for a while and then found their next use case. Recent estimates suggest GenAI companies are generating around $110B in annual revenue and the growth rate is reportedly around 3x faster than previous IT waves like the internet and mobile. What's interesting is that the pace has held through every phase since 2022; first it was chatbots, then coding copilots and now it's AI agents and if you’ve followed this space closely enough, you can see instead of one trend replacing another, each wave seems to be creating demand for the next one. I think that's also changing how people build and consume. A year or two ago, most of the conversation was about finding the best model, but now devs are paying attention to everything around the model too such as: retrieval, evaluations, data pipelines, deployment, and infrastructure. If AI is becoming part of more products, the supporting stack starts to matter just as much as the model itself. You can see it in the open-source ecosystem. Models keep improving, but so do the tools around them

19h ago

---

**[LinkedIn's behavioral scoring system and what it means for anyone building AI automations on the platform](https://www.reddit.com/r/artificial/comments/1uq718e/linkedins_behavioral_scoring_system_and_what_it/)**

LinkedIn removed the fixed connection request cap sometime in the last couple of years. Well, it was more in general cuts, the latest of which happened this year, and replaced it with a dynamic per-account scoring model that most people building automation on the platform haven't fully mapped yet. The system weighs several behavioral inputs. Namely these: acceptance rate, reply rate, SSI (Social Selling Index), organic posting activity, and the number of pending unaccepted invitations sitting in your queue, which it uses to produce a trust score that directly controls how many outbound actions your account is allowed to take. In practice, this means that accounts with high trust signals (SSI around 65 or above, acceptance rates above 40%) can push up to 200 connection requests per week without triggering restrictions. However, accounts with low trust signals get throttled to around 50 per week, sometimes significantly lower at 25-30. That's 4 times the capacity difference between two accounts on the same platform running the same automation tooling, based purely on how LinkedIn grades their reputation. I think this is very relevant to anyone building or in any way using LinkedIn automations and as head of GTM at Expandi I’ve had the opportunity to see these patterns I’m talking about, in practice, over dozens of dozens of accounts running outreach at various volumes. But what makes this relevant to anyone building LinkedIn automation - is that the system creates a feedback loop that's really hard to reverse once it starts working against you. Low acceptance rates from poor targeting push your trust score down, which throttles your volume, which in turn pressures you to cast a wider net with less precise targeting, which drops your acceptance rate even further. And so on and so forth. I've watched accounts downgrade from 150 requests/week capacity down to 40 in under just a month because the initial list quality was bad and every subsequent adjustment made it worse. The diagnostic is pretty straightforward, though, if you want to check where an account sits: - Pull your SSI at linkedin.com/sales/ssi - Check your acceptance rate for the last month from your sent invitations - Withdraw pending invitations older than 2 weeks - each one is dragging your score - Look at whether your sends are clustered since these burst patterns are a detection signal TL;DR version - The acceptance rate on LinkedIn is the single highest weight input in the scoring model from what I've been able to observe and will impact your ability to automate profile actions more than anything. LinkedIn accounts that maintain 40% plus acceptance consistently get capacity that makes automation viable at scale, while accounts below ~25% acceptance hit flat walls the platform sets that no tool configuration can work around.

6h ago

---

**[AI should be private and optional!](https://www.reddit.com/r/artificial/comments/1uplbps/ai_should_be_private_and_optional/)**

AI should be private and optional.

22h ago

---

**[I stopped treating business setup like five separate chores](https://www.reddit.com/r/artificial/comments/1uq2wgs/i_stopped_treating_business_setup_like_five/)**

I kept putting off the business setup side because every step felt like another tool, account or subscription This time I tried running it through Claude and kept the whole thing in one workflow: setup, verification, bank account and basic finance admin after. Still early but it’s been way easier than jumping between random sites and notes. The nice part is not needing a bunch of separate tools just to get the business side ready. Am I the only one doing it this way? I don’t think it’s that crazy tbh

9h ago

---

**[SpaceX burned up 260 of its own satellites in 6 months and this is just routine apparently](https://www.reddit.com/r/artificial/comments/1upbdoa/spacex_burned_up_260_of_its_own_satellites_in_6/)**

Saw this in an article and it's been on my mind since 260 satellites intentionally burned in the atmosphere in 6 months and another 349 queued. They're planning 42,000 total eventually. No debris which is fine but researchers are asking what happens when you're burning hundreds of massive metal objects in the upper atmosphere repeatedly over years. Aluminum particles, potential atmospheric chemistry changes. Science is still catching up and the FCC is now proposing to exempt satellites from environmental review entirely Idk,we're moving faster than we're studying this...anyone else find this a bit much?

1d ago

---

**[Microsoft Moves Toward In-House AI Models](https://www.reddit.com/r/artificial/comments/1uq7fsg/microsoft_moves_toward_inhouse_ai_models/)**

Microsoft is beginning to replace AI models from OpenAI and Anthropic with its own internally developed alternatives across key products like Excel and Outlook. The shift signals a broader strategy…

🔗 [Wealthari](https://wealthari.com/microsoft-moves-toward-in-house-ai-models/) • 6h ago

---

**[What do normal people use ai for?](https://www.reddit.com/r/artificial/comments/1upq8r2/what_do_normal_people_use_ai_for/)**

I understand very generally that AI is good at "writing code" but I'm wondering what specifically normal people would need the capability to write code for in their daily lives? Unless they work in an industry that relies on coding in which case it's self explanatory. I personally just use chatgpt for general conversation and talking about life.

17h ago

---

**[Companies are laying off humans and replacing them with AI agents without proper testing. Is this crazy?](https://www.reddit.com/r/artificial/comments/1uqgzqb/companies_are_laying_off_humans_and_replacing/)**

I keep seeing more and more stories about entire teams being laid off and replaced by AI agents almost overnight. It feels reckless-like companies are going all-in on technology that’s still quite unpredictable in real-world conditions. Why don’t more companies take a safer approach? For example, create a parallel “AI branch” or pilot team for 3-6 months: run the AI agents alongside human employees, measure real performance, error rates, customer satisfaction, and edge cases before making permanent cuts. Is this just greed and pressure from investors to cut costs immediately? Or do companies actually have internal data showing that the risks are lower than we think? Maybe they’re seeing such massive productivity gains that they’re willing to take the gamble. I’d really love to hear from people who work (or have worked) at companies that already went through this kind of AI replacement. How did it actually go? Were there major failures, hidden costs, or surprisingly good results? What lessons would you share?

4m ago

---

---

## Google News: "ai"

**[Introducing Muse Image: Image Generation Built for Your World](https://about.fb.com/news/2026/07/introducing-muse-image-meta-ai/)**

Muse Image is the first image generation model from Meta Superintelligence Labs, now available in Meta AI.

Meta Store • 9h ago

---

**[Meta Now Lets Anyone Use Your Instagram Photos in AI Images—Unless You Opt Out](https://www.wired.com/story/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images-unless-you-opt-out/)**

As part of Meta’s Muse Image model rollout, Instagram users with public accounts need to opt out to block AI generations of their content.

WIRED • 5h ago

---

**[If You Have a Public Instagram Account, You Might Be Surprised What AI Users Can Now Do With Your Face](https://gizmodo.com/if-you-have-a-public-instagram-account-you-might-be-surprised-what-ai-users-can-now-do-with-your-face-2000782694)**

Gizmodo • 1h ago

---

**[EXCLUSIVE: Beijing is looking at curbing overseas access to China's top AI models, sources say](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/)**

Reuters • 17h ago

---

**[Why this billion-dollar tech company is sending data centers to space](https://www.cnn.com/2026/07/07/business/video/starcloud-space-ai-data-centers-hnk-spc?cid=external-feeds_iluminar_google)**

With AI straining Earth’s infrastructure, space-tech startup Starcloud is developing orbital data centers designed to meet the world’s growing computing needs.

CNN • 1h ago

---

**[Tencent WeChat AI Agent Shows Promise in Super-App Fight: Review](https://www.bloomberg.com/news/articles/2026-07-08/tencent-wechat-ai-agent-shows-promise-in-super-app-fight-review)**

Bloomberg.com • 27m ago

---

**[AI deployment is now as much of a CFO decision as a CTO one: JP Morgan](https://www.cnbc.com/video/2026/07/08/jitters-about-ai-led-borrowing-while-the-direction-of-travel-is-a-concern-the-magnitude-of-borrowing-is-not-high-relative-to.html)**

JP Morgan Asset Management' Tai Hui says AI adoption will reshape industries, but businesses are increasingly weighing the cost of deployment alongside its potential returns. He adds that while investors are watching AI companies' borrowing more closely, debt levels remain manageable relative to the size of these businesses.

CNBC • 45m ago

---

**[Column | How to stop ChatGPT from ruining how you think](https://www.washingtonpost.com/technology/2026/07/07/how-stop-chatgpt-ruining-how-you-think/)**

Studies show that using AI can lead people to “cognitive surrender.” But with the right approach, it can also elevate your thinking.

The Washington Post • 11h ago

---

**[‘Absolutely bananas’: San Francisco homes sell for $1m above asking price amid AI boom](https://www.theguardian.com/us-news/2026/jul/07/san-francisco-home-sale-prices-ai)**

Report finds widespread overbidding as rapid AI growth generates increased wealth in city where housing is scarce

The Guardian • 4h ago

---

**[Anthropic Expands in Manhattan, Part of an A.I. Boom in New York](https://www.nytimes.com/2026/07/07/nyregion/anthropic-ai-boom-nyc.html)**

Anthropic, the artificial intelligence company, plans to lease a 16-story building in Hudson Square and to double its work force in New York City to 1,000 people this year.

The New York Times • 6h ago

---

---

## HackerNews: "ai"

**[GLM 5.2 and the coming AI margin collapse](https://news.ycombinator.com/item?id=48809877)**

GLM 5.2 is the first open weights model I'd call a genuine competitor to Opus and GPT for agentic work - at ~15-20% of the price. Part one of why AI inference margins are about to collapse.

⬆️ 666 • 💬 450 • 1d ago • [Martin Alderson](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

---

**[AMD Ryzen AI Halo – $4k AI Dev Kit](https://news.ycombinator.com/item?id=48805624)**

Welcome to LTT Labs - your go-to destination for all things tech. Explore comprehensive test results, insightful commentary, and the latest analysis in hardware.

⬆️ 371 • 💬 256 • 1d ago • [LTT Labs](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

---

**[Small AI Models Gain Traction In places with unreliable networks](https://news.ycombinator.com/item?id=48812055)**

In places with unreliable networks and no data-center infrastructure, smaller is better

⬆️ 263 • 💬 78 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals)

---

**[We charge $10k a week to delete AI-generated code](https://news.ycombinator.com/item?id=48823359)**

Your AI-built product works, but past 100,000 lines every change breaks two things. Three senior engineers make your codebase maintainable again. One week, fixed price, guaranteed.

⬆️ 242 • 💬 142 • 6h ago • [odra.dev](https://odra.dev/slopfix/)

---

**[OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files](https://news.ycombinator.com/item?id=48807225)**

OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation req...

⬆️ 212 • 💬 62 • 1d ago • [GitHub](https://github.com/iOfficeAI/OfficeCLI)

---

**[New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://news.ycombinator.com/item?id=48796817)**

⬆️ 178 • 💬 112 • 2d ago • [intextbooks.science.uu.nl](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf)

---

**[Delta flight hit by firework while landing at Midway Airport on Fourth of July](https://news.ycombinator.com/item?id=48797141)**

A Delta flight arriving at Chicago's Midway International Airport on the Fourth of July reportedly made contact with a firework, the airline said.

⬆️ 173 • 💬 395 • 2d ago • [NBC Chicago](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

---

**[Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://news.ycombinator.com/item?id=48799256)**

Instead, buy domestic product, and out in the open.

⬆️ 164 • 💬 79 • 2d ago • [readtheline.ca](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)

---

**[Mark Zuckerberg tells staff that AI agents haven't progressed enough](https://news.ycombinator.com/item?id=48795826)**

At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated.

⬆️ 133 • 💬 2 • 2d ago • [TechCrunch](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/)

---

**[When AI Costs More Than the Engineer](https://news.ycombinator.com/item?id=48801493)**

Anthropic spends 2.3x payroll on compute. Top software firms spend 0.4x. Three scenarios for where the rest of the market lands by 2029.

⬆️ 125 • 💬 113 • 1d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-spend-breakeven-2029/)

---

---

## YouTube Videos: "ai"

**[One Chinese AI Model Wiped Out $1 Trillion In A Single Day — And They&#39;re Just Getting Started](https://www.youtube.com/watch?v=WUTkCiNEDWU)**

ATT Business: Switch to AT&T Business at business.att.com Paleovalley: 30 for $36 https://bit.ly/PaleovalleyIT 80% of every dollar ...

📺 Tom Bilyeu

👁️ 71K • 👍 3K • 💬 596 • ⏱️ 34:31 • 14h ago

---

**[AI Agents Explained: Build Your First One in 2026](https://www.youtube.com/watch?v=-Zhntlk0v80)**

Host Hermes Agent on Hostinger http://hostinger.com/yourihermes In this video, I show you how to build your own AI agent from ...

📺 Roboverse

👁️ 10K • 💬 7 • ⏱️ 12:39 • 11h ago

---

**[The Dirty AI lie : How the GREATEST bet in human history started to crack in June 2026?](https://www.youtube.com/watch?v=WcckBmkauBQ)**

Check out Odoo: https://www.odoo.com/r/ChAT ⭐️ Think School's flagship Communication course with live doubt sessions ...

📺 Think School

👁️ 1.2M • 👍 33K • 💬 1K • ⏱️ 20:53 • 1d ago

---

**[AI expert worries about the risk of humans losing control | Four Corners](https://www.youtube.com/watch?v=gYORRh377Gw)**

Jeffrey Ladish consulted on security for AI giant Anthropic. Now as Executive Director at Palisade Research he tests AI agents and ...

📺 ABC News In-depth

👁️ 34K • 👍 900 • 💬 81 • ⏱️ 15:06 • 1d ago

---

**[AI Just Decoded These Mysterious Crop Circles!](https://www.youtube.com/watch?v=I1ivRkaQyPQ)**

Hi, it's Katrina! We are exploring the mysterious radio broadcasts and geometric patterns that have appeared across our world's ...

📺 Origins Explained

👁️ 53K • 👍 2K • 💬 331 • ⏱️ 28:46 • 2d ago

---

**[The Best Way To Make Money With AI In 24 Hours](https://www.youtube.com/watch?v=JZ9mxEsQUNc)**

Stop guessing what your customers want and start analyzing their actual questions to write better sales copy today.

📺 Ross Minchev

👁️ 2K • 👍 133 • 💬 7 • ⏱️ 32:28 • 16h ago

---

**[The Moment America Realized China Won the AI Race](https://www.youtube.com/watch?v=2TwEWXO9_S8)**

China is winning the AI Race and if you need proof you just need to see look at how American companies are now dumping ...

📺 Cyrus Janssen

👁️ 53K • 👍 4K • 💬 246 • ⏱️ 10:28 • 1d ago

---

**[AI CEOS PANIC After Public Outrage Over Job Loss](https://www.youtube.com/watch?v=Xxodq1QWvMk)**

Ryan and Saagar discuss AI CEOs panicking and trying to backtrack on projections of job losses. Sign up for a PREMIUM ...

📺 Breaking Points

👁️ 177K • 👍 5K • 💬 989 • ⏱️ 19:42 • 10h ago

---

**[Artificial Intelligence: Complete path to 2030](https://www.youtube.com/watch?v=XXaUd0fGpOs)**

Which of these predictions are starting to happen right now? ___ CHAPTERS: 00:00 AI In The Next 5 Years (2026 to 2030) 19:46 ...

📺 Future Business Tech

👁️ 10K • 👍 399 • 💬 37 • ⏱️ 2:02:04 • 15h ago

---

**[China Is About To Pop The AI Bubble](https://www.youtube.com/watch?v=siazPdsZHuI)**

China Is About To Pop The AI Bubble ▻ Go to https://ground.news/jikh to access world-wide perspectives in one place, compare ...

📺 Andrei Jikh

👁️ 146K • 👍 11K • 💬 1K • ⏱️ 30:47 • 4h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,683,711 • ❤️ 1,767 • 9d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 121 • ❤️ 493 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 281,584 • ❤️ 3,601 • 5d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,084,945 • ❤️ 1,836 • 4d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 14,723 • ❤️ 376 • 4d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 9,458 • ❤️ 290 • 3d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 502,663 • ❤️ 781 • 12d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 538,687 • ❤️ 315 • 7d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 3,886 • ❤️ 184 • 3d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 384,383 • ❤️ 1,077 • 18d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 31 • 💬 1 • ⭐ 339 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 8 • 💬 0 • ⭐ 6,260 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 109 • 💬 4 • ⭐ 91,648 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 252 • 💬 4 • ⭐ 11,418 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,617 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 73,772 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Multiplayer Interactive World Models with Representation Autoencoders](https://huggingface.co/papers/2607.05352)**

*Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. (27 authors)*

A large-scale multiplayer world model trained on extensive gameplay data demonstrates stable long-horizon rollouts in a complex physics-based environment while maintaining coherence across multiple agents' actions.

▲ 14 • 💬 0 • ⭐ 236 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05352) • [💻 code](https://github.com/mira-wm/mira) • [🔗 project](https://mira-wm.com/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 3 • ⭐ 10,167 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,800 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 41 • 💬 1 • ⭐ 181 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 77.0k • 🔱 4.1k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.6k • 🔱 1.1k • 13h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.7k • 🔱 885 • 8m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 6.4k • 🔱 825 • 7h ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 3.4k • 🔱 762 • 10h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.5k • 🔱 216 • 5h ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.2k • 🔱 78 • 1d ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 89 • 24d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 1.4k • 🔱 198 • 9h ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.4k • 🔱 121 • 9d ago

---

---

*Generated by PeekDeck - A glance is all you need*
