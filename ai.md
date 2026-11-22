---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-22T10:47:45.975583+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 22, 2026 at 10:47 UTC  
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

**[Anthropic S-1: $216bn of staff equity, $160bn still to grant](https://www.reddit.com/r/artificial/comments/1xycep1/anthropic_s1_216bn_of_staff_equity_160bn_still_to/)**

Anthropic's amended filing shows employee options and RSUs worth more than three times the IPO itself, plus a reserve for future hires. Every other startup now writes offer letters against that.

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 5d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 5d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

5d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

5d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 5d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

5d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

5d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

6d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

5d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 5d ago

---

---

## Google News: "ai"

**[Anthropic warns AI models could soon copy themselves across home devices](https://www.cnbc.com/2026/10/13/anthropic-ai-models-self-replication-smart-devices.html)**

Anthropic's latest research adds to the growing safety concerns around AI from the ability for models to carry out cyberattacks to the technology going rogue.

CNBC • 1mo ago

---

**[Scoop: AI companies plot "day after" scenarios for public revolt](https://www.axios.com/2026/10/09/ai-companies-day-after-major-attack)**

Axios • 1mo ago

---

**[Gemini 4 Argon: Built to solve your hardest problems](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)**

We’re giving developers, enterprises, scientists, and consumers access to Gemini 4 Argon, our latest frontier model.

blog.google • 1mo ago

---

**[GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)**

This AI threat update provides GTIG’s findings on adversarial misuse of AI including Gemini and other non-Google tools.

Google Cloud • 5d ago

---

**[AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)**

Small AI models may be only months away from being able to self-replicate across cheap IoT devices like Android TV boxes, with no datacenter needed.

Anthropic • 1mo ago

---

**[Independent Assessment of AI R&D Acceleration at Anthropic in October 2026](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)**

METR's high-access assessment of the degree to which AI is accelerating AI research and development at Anthropic.

METR • 17d ago

---

**[In China, the AI bubble has already burst](https://www.reuters.com/world/china/china-ai-bubble-has-already-burst-2026-10-26/)**

Reuters • 26d ago

---

**[Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)**

OpenAI publishes new results on open problems in mathematics from an internal frontier model and shares Lean proof formalizations and research details on GitHub.

OpenAI • 1mo ago

---

**[Timestral: Mistral's time-series foundation models](https://mistral.ai/news/timestral/)**

State-of-the-art probabilistic forecasting in four sizes (5M–209M params), CPU-efficient, zero-shot ready.

Mistral AI • 1mo ago

---

**[PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet](https://www.wiz.io/blog/php2shell-php-rce)**

Core PHP engine flaws enable remote code execution and Heartbleed-style memory disclosure across the web.

wiz.io • 1mo ago

---

---

## HackerNews: "ai"

**[Frostbite: A new CPU architecture discovered, designed and verified by AI](https://news.ycombinator.com/item?id=50572503)**

Frostbite is a general-purpose CPU built around interaction nets, discovered, designed, and verified end-to-end by our AI systems, reaching 4.59x the performance-per-watt of a modern superscalar (dual-issue, in-order) CPU core.

⬆️ 671 • 💬 359 • 2d ago • [Architect Labs](https://architectlabs.com/blog/frostbite)

---

**[Fuck Your AI Safeguards](https://news.ycombinator.com/item?id=50562262)**

You can't tell me that you found a security issue in my product and then refuse to fix it.

⬆️ 616 • 💬 249 • 2d ago • [./techtipsy](https://ounapuu.ee/posts/2026/11/19/unsafeguards/)

---

**[Restricting AI agents in mobile operating systems platforms from capturing data](https://news.ycombinator.com/item?id=50572348)**

Privacy is our mission; it’s why we exist, and we do everything we can to protect it. This means that we are restricting the latest AI agents built into mobile operating systems from potentially capturing and storing your Signal data.

⬆️ 574 • 💬 340 • 2d ago • [Signal Messenger](https://signal.org/blog/protecting-your-privacy/)

---

**[Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day](https://news.ycombinator.com/item?id=50574383)**

Asian markets record worst week since 2020 as investors question huge sums being poured into AI buildout

⬆️ 511 • 💬 896 • 1d ago • [the Guardian](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

---

**[Google workers tell their employer not to punish schools that don't want AI](https://news.ycombinator.com/item?id=50577901)**

Executives are “convinced that resistance to AI" just means schools "don’t see the vision,” a Google staffer said.

⬆️ 282 • 💬 228 • 1d ago • [Mother Jones](https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/)

---

**[Pete Warden on local AI, open models, voice interfaces, the future of hardware](https://news.ycombinator.com/item?id=50561508)**

⬆️ 272 • 💬 248 • 2d ago • [thedataexchange.media](https://thedataexchange.media/pete-warden-moonshine/)

---

**[ClawDOS – An AI coding agent for DOS](https://news.ycombinator.com/item?id=50586292)**

An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz)

⬆️ 164 • 💬 52 • 1d ago • [ClawDOS](http://ricapar.net/ClawDOS/)

---

**[AI isn't replacing your job. It's turning it into low-paid gig work](https://news.ycombinator.com/item?id=50562500)**

⬆️ 148 • 💬 83 • 2d ago • [restofworld.org](https://restofworld.org/2026/ai-jobs-skills-gig-work/)

---

**[Chrome AI features wasting much bandwidth](https://news.ycombinator.com/item?id=50562636)**

🔎 Finally solved the mystery. At some point this year (around a few months ago), my bandwidth/data usage went thru the roof. Figured out it was Chrome's...

⬆️ 134 • 💬 51 • 2d ago • [perishablepress.com](https://perishablepress.com/chrome-ai-wasting-much-bandwidth/)

---

**[AI is giving everyone the same advice](https://news.ycombinator.com/item?id=50577872)**

I asked 65 AIs from 30 companies the questions people ask them every day, 127,918 times. 73 of every 100 people were told to read the same book. See every answer, and the two prompts that get you your own.

⬆️ 123 • 💬 52 • 1d ago • [A90](https://a90.com/experiments/same-advice/)

---

---

## YouTube Videos: "ai"

**[AI Is Getting Intelligent. But Not How You Think](https://www.youtube.com/watch?v=-MiM5xfAe2c)**

Thanks to Mammouth AI for sponsoring this video: https://mammouth.ai No one really knows how AI works. Scientists are figuring it ...

📺 Sabine Hossenfelder

👁️ 289K • 👍 7K • 💬 881 • ⏱️ 6:51 • 18h ago

---

**[AI Genius Predicts the Exact Month Superintelligence Arrives](https://www.youtube.com/watch?v=rOXnBQrxGqs)**

Ryan Christian of Vals.ai and Joe Lonsdale discuss the Vals RSI index, which projects Anthropic reaching full recursive ...

📺 Joe Lonsdale

👁️ 42K • 👍 428 • 💬 81 • ⏱️ 7:00 • 1d ago

---

**[AI out of control? - Why Artificial Intelligence experts are sounding the alarm | DW Documentary](https://www.youtube.com/watch?v=2I4qMBiK6hg)**

Artificial Intelligence is permeating our everyday lives at breathtaking speed. It is taking on more tasks that were previously the ...

📺 DW Documentary

👁️ 290K • 👍 3K • 💬 463 • ⏱️ 1:28:52 • 17h ago

---

**[Big Short Investor: Is the AI Bubble About to Burst? - Steve Eisman](https://www.youtube.com/watch?v=hkdcESS5uMw)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Venice gives you the best AI ...

📺 Triggernometry

👁️ 234K • 👍 3K • 💬 1K • ⏱️ 1:26:10 • 15h ago

---

**[How to Defeat AI 🤣](https://www.youtube.com/watch?v=_SIBK3M1DK0)**

If you want to help support independent journalism, become a Member: ...

📺 Benny Johnson

👁️ 568K • 👍 24K • 💬 2K • ⏱️ 2:46 • 2d ago

---

**[“I Don’t Believe in Coincidences:” AI Expert Warns of Recent Tech Outages | Amanpour and Company](https://www.youtube.com/watch?v=kysahSdnsGk)**

Dr. Ayanna Howard has spent her career exploring the reach and implications of artificial intelligence. She says we are only just ...

📺 Amanpour and Company

👁️ 116K • 👍 2K • 💬 164 • ⏱️ 18:16 • 2d ago

---

**[US-Made AI Drones vs. Russian Fighter Jets and Trucks | How Ukraine’s Omega Flies Hornet &amp; Bumblebee](https://www.youtube.com/watch?v=ztghNECxqUc)**

American-made drones equipped with AI-powered targeting systems are being used by Ukrainian special forces to strike Russian ...

📺 UNITED24

👁️ 154K • 👍 1K • 💬 76 • ⏱️ 6:56 • 1d ago

---

**[Blackstone JUST Sent a TERRIFYING WARNING About the AI BUBBLE](https://www.youtube.com/watch?v=vOQILY2JOH4)**

Blackstone president Jon Gray warned that some AI investments “will go awry.” Less than two weeks later, Bloomberg reported ...

📺 EUREKA US

👁️ 36K • 👍 254 • 💬 28 • ⏱️ 13:13 • 2d ago

---

**[Why AI engineers are scared of self-building artificial intelligence | The Economist](https://www.youtube.com/watch?v=rE-sazAVQVU)**

Next year AI could start building its own successors, with no human in the loop. Subscribe: ...

📺 The Economist

👁️ 160K • 👍 1K • 💬 170 • ⏱️ 10:01 • 2d ago

---

**[AI just got real: TRILLION DOLLAR launch raises stakes for Dems](https://www.youtube.com/watch?v=u0Yj1R-RpcY)**

Chris Kelly, former Facebook chief privacy officer and general counsel, and Dylan Ratigan, MSNBC and CNBC veteran, join MS ...

📺 MS NOW

👁️ 81K • 👍 724 • 💬 127 • ⏱️ 11:22 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 23,543 • ❤️ 3,655 • 12h ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 805,993 • ❤️ 732 • 6h ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 557 • 8d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 6,617 • ❤️ 569 • 2d ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 504 • 2d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 2,831 • ❤️ 951 • 1d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 8,608 • ❤️ 852 • 9d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,297,396 • ❤️ 20,833 • 15d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 129,693 • ❤️ 331 • 16h ago

---

**[DepthPro2](https://huggingface.co/apple/DepthPro2)**

*Apple*

`depth-estimation`

⬇️ 0 • ❤️ 225 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 11 • 💬 0 • ⭐ 5,792 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 31 • 💬 3 • ⭐ 354 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 148 • 💬 4 • ⭐ 1,237 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 7,926 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 18 • 💬 2 • ⭐ 415 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,423 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 24,703 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 22 • 💬 0 • ⭐ 42,373 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 37 • 💬 9 • ⭐ 12,196 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 78 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 19.9k • 🔱 1.2k • 7d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 12.0k • 🔱 1.8k • 57m ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.6k • 🔱 2.1k • 4h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.7k • 🔱 760 • 18h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.8k • 🔱 2.0k • 4d ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 6.6k • 🔱 518 • 51m ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.5k • 🔱 231 • 9m ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.4k • 🔱 794 • 5h ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 113 • 2h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.9k • 🔱 142 • 7m ago

---

---

*Generated by PeekDeck - A glance is all you need*
