---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-15T20:11:25.393397+00:00'
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

**Last Updated:** November 15, 2026 at 20:11 UTC  
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

**[built a fact-checker that catches politicians lying in real-time](https://www.reddit.com/r/artificial/comments/1xwmtff/built_a_factchecker_that_catches_politicians/)**

I've embarrassingly been working on this project for 2 years so wanted to finally share (as I saw others posting Youtube-only versions). on Youtube it transcribes text to identify checkable claims -> web search retrieves sources to base Claude's verdict on, to avoid hallucinated sources. it's a free Chrome extension, and works on news or social media sites as well. let me know what would make this something you'd use, or what else you'd like to see! Edit 2: LogicLens - Chrome Webstore Or iOS if you don't use Chrome (Google = :/). Edit: I realized someone not following could misread the video (here Biden is telling the truth, and Trump was lying, but the Trump section is before I started the recording).

15h ago

---

**[Are AI leaderboards even worth taking seriously anymore?](https://www.reddit.com/r/artificial/comments/1xwwdhv/are_ai_leaderboards_even_worth_taking_seriously/)**

Every time a new AI leaderboard drops theres suddenly a different model being called the best in the world and then you check another benchmark and the rankings are completely different. Gemini has been doing well in general chat rankings while Claude has been strong in coding, so apparently the best AI depends on which website you happen to open that morning. Kalshi even has a market on which AI model finishes November at number one and it got me thinking about how much these rankings actually reflect what people use every day. I mean a model can score high on some benchmark and still give you a garbage answer to a basic question. At this point I’d rather hear from people who use these tools for actual work instead of another company announcing it beat everyone by three points on some test. Has anyone here switched their main AI because of these rankings or are we just watching companies fight over numbers that barely change the experience?

6h ago

---

**[Anthropic rebuilds Claude Code Projects around a coordinator and parallel worker threads - each thread is a full cloud session on its own branch](https://www.reddit.com/r/artificial/comments/1xwj3v0/anthropic_rebuilds_claude_code_projects_around_a/)**

Anthropic posted an update on Nov 14 rebuilding Claude Projects from a folder of files into a coordinated set of working sessions. You describe the work in one conversation; a coordinator scopes it, delegates it to parallel threads, reviews the outputs and assembles the result. Each thread is a Claude Code cloud session with its own copy of the repo and its own Git branch, and it can split its task further into subagents, loops or workflows. The work keeps going after you close your laptop, and you can steer it from your phone. It is a public beta rolling out gradually to select Pro/Max/Ultra subscribers who use Claude Code cloud sessions; Team and Enterprise plans do not have it yet, and there is a waitlist for everyone else. Anthropic is upfront about the limits: threads run only in the cloud for now (local code and VPN support is coming 'very soon'), several parallel sessions burn through usage limits faster, and if two threads touch the same code it surfaces as an ordinary merge conflict in a PR. Sources: Anthropic's product post (claude.com/blog/projects-redesigned) and the Projects docs (code.claude.com/docs/en/claude-projects). What I am curious about: does parallelizing agents actually speed up real work, or does it just move the bottleneck to review and merge conflicts? Has anyone here tried the beta?

18h ago

---

**[One Router Grounded America? Seriously? Are you sure it wasn’t Rogue AI or a Hack?](https://www.reddit.com/r/artificial/comments/1xwd18l/one_router_grounded_america_seriously_are_you/)**

So apparently the Trump administration is blaming a faulty router for grounding flights across America. A router. Seriously? Of course a router can cause network failures, but how the hell does critical national aviation infrastructure lack the safeguards to prevent one failure cascading across the system? And who in their right mind schedules an upgrade at 3 pm on a Friday afternoon? I seriously smell a rat because the explanation raises more concerns than answers? Is America being gaslit?

23h ago

---

**[Meituan open-sourced LongCat-2.5, a 1.6T agent model, and the only deploy guide is for Huawei NPUs, not Nvidia](https://www.reddit.com/r/artificial/comments/1xwx2hc/meituan_opensourced_longcat25_a_16t_agent_model/)**

Meituan just released the LongCat-2.5 weights under MIT: 1.6T total parameters, about 48B active per token, with text, image and video input. On their own table it scores 88.4 on Terminal Bench v2.1, right next to Claude Opus 5 at 89.1. On the harder Terminal Bench v4.0 the gap opens up: 38.5 vs 53.9 for Opus 5. The catch if you want to self-host is that the model card only documents NPU deployment, with no Nvidia path yet. As someone who builds small web projects, what I care about is that the API speaks both OpenAI and Anthropic formats, so testing it inside an existing agent setup is cheap. Has anyone run it in a real coding agent loop yet, and does it hold up outside the benchmarks? Source: https://huggingface.co/meituan-longcat/LongCat-2.5

5h ago

---

**[Building with AI is now easier but trust takes further testing.](https://www.reddit.com/r/artificial/comments/1xwwrm0/building_with_ai_is_now_easier_but_trust_takes/)**

I think this is a subject that should be discussed in detail, with more and more builders shipping products with AI who’s is actually testing them?

🔗 [CrashTest AI](https://crashtestingai.com/lab-notes/building-is-easier-trust-is-harder/) • 5h ago

---

**[Local Computer use with Row-Bot](https://www.reddit.com/r/artificial/comments/1xwswp5/local_computer_use_with_rowbot/)**

Row-Bot can drive your computer. Mouse, keyboard, real apps. Windows and Mac. Handing an AI your desktop is a dumb idea unless you lock it down hard. So: - driver is Cua 0.20.0, pinned to an exact commit, SHA-256 checked. Turning the feature on downloads nothing. You click Install - Cua's own update checks are off, and it runs in a stripped-down environment - before it runs even once, you're told exactly what Cua's telemetry sends. Continue or Cancel - it never types into password, 2FA or card fields, never touches your password manager, never controls itself - pay, book, send, post, delete files, change settings: it asks first, unless you put it on hands-off - it judges every click by what's actually under the pointer. Enter in a chat app means send, so that asks too

9h ago

---

**[Not all AI sounds human.](https://www.reddit.com/r/artificial/comments/1xwo2iz/not_all_ai_sounds_human/)**

Some AI models don’t generate tokens or try to sound like your best friend.

🔗 [blog.galratner.com](https://blog.galratner.com/p/not-all-ai-sounds-human) • 14h ago

---

**[Could AI handle public transit information calls?](https://www.reddit.com/r/artificial/comments/1xw6eqj/could_ai_handle_public_transit_information_calls/)**

During service disruptions people are calling about delays, missed connections, route changes and whether theres another bus or train coming And the information can change every few minutes The phone part seems doable with tools like Elevenlabs or Bland, but I'd want it connected directly to the transit system's live updates before trusting it with arrival times. Giving someone an outdated ETA is probably worse than telling them there's no confirmed time yet.

1d ago

---

**[Don't we want the AI to do our work...](https://www.reddit.com/r/artificial/comments/1xwlffv/dont_we_want_the_ai_to_do_our_work/)**

Most people have jobs they would rather not do, but they need to get paid. Instead of "protecting jobs from AI" we should be thinking about how people can live without needing jobs and let the machines do the boring work nobody wants to do in the first place.

🔗 [towardsdatascience.com](https://towardsdatascience.com/ai-will-do-your-job-that-should-be-good-news/) • 16h ago

---

---

## Google News: "ai"

**[How Jensen Huang Built the Backdoor Route That Keeps Beijing in the AI Race](https://www.wsj.com/tech/jensen-huang-backdoor-ai-data-centers-a5e4499d)**

WSJ • 10h ago

---

**[‘Jensen Huang lost his mind’: how AI’s smartest man fell for the world’s oldest trick](https://www.theguardian.com/technology/2026/nov/14/jensen-huang-affair-nvidia-nightmare)**

Jensen Huang’s affair with a suspected spy is Silicon Valley’s worst nightmare come true

The Guardian • 1h ago

---

**[US Treasury chief wants answers soon from Nvidia](https://finance.yahoo.com/technology/ai/articles/us-treasury-chief-wants-answers-183327447.html)**

US Treasury Secretary Scott Bessent called on Nvidia Sunday to explain whether it knowingly allowed its most advanced AI chips to reach China, saying this was more important than ex-CEO Jensen Huang's affair with an alleged spy for Beijing.In late 2025, President Donald Trump did authorize sales of Nvidia chips called H200s to the Chinese -- but not the most advanced chips used to run AI models reshaping modern society.

Yahoo Finance • 1h ago

---

**[Apple Bets on Siri AI Apps as the Main Draw for Its Smart Glasses](https://www.bloomberg.com/news/newsletters/2026-11-15/apple-siri-ai-app-integrations-power-smart-glasses-iphone-duo-2-face-id-plan)**

Bloomberg.com • 5h ago

---

**[Could Trump turn against the AI barons?](https://thehill.com/opinion/technology/6220328-trump-ai-policy-shift/)**

The Hill • 1h ago

---

**[Uber's Secure AI Framework Governs Autonomous AI Agents Across Their Lifecycle](https://www.infoq.com/news/2026/11/uber-secure-ai-framework/)**

In a recent article, Uber Engineering highlights the limitations of traditional identity and API controls in securing AI agents that dynamically reason over external content and take real-world actions. Uber developed a framework to determine whether an agent's action is appropriate given the user's request, the agent's intended purpose, its permissions, and the context of the interaction.

infoq.com • 11m ago

---

**[Anthropic’s IPO lands as the embattled AI trade looks for a much-needed bright spot](https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html)**

Anthropic's IPO has outsized importance in the tech industry, which is heavily invested in the AI lab and is desperate for some positive momentum.

CNBC • 8h ago

---

**[Anthropic Is About to Become the World’s Most Important AI Stock](https://www.bloomberg.com/news/features/2026-11-15/anthropic-s-ipo-makes-dario-amodei-the-new-face-of-the-ai-boom)**

Bloomberg.com • 1h ago

---

**[Anthropic’s IPO marks a new phase in the rivalry among AI labs](https://www.economist.com/business/2026/11/15/anthropics-ipo-marks-a-new-phase-in-the-rivalry-among-ai-labs)**

The Economist • 22m ago

---

**[Could everything be broken? Grounded jets, Microsoft outage, AI chaos make some wonder](https://apnews.com/article/flights-grounded-microsoft-ai-chaos-ea5f7a1f95a38f65dd57e58cfc17672b)**

AP News • 14h ago

---

---

## HackerNews: "ai"

**[Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs](https://news.ycombinator.com/item?id=50493251)**

Following the departure of now-former NVIDIA CEO, Jensen Huang, a new report by The Wall Street Journal (via Wccftech) has emerged alleging that NVIDIA artificially inflated the ongoing GPU and memory shortage by investing in AI startups that would go on to buy NVIDIA GPUs and build data centers....

⬆️ 1091 • 💬 646 • 1d ago • [TechPowerUp](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)

---

**[All AI-generated code should be Open Source](https://news.ycombinator.com/item?id=50507303)**

All code generated with help from AI should be Open Source or on Creative Commons Zero (CC0) license.

⬆️ 883 • 💬 467 • 5h ago • [Jakub T. Jankiewicz Blog](https://jakub.jankiewicz.org/blog/ai-code-open-source/)

---

**[Reverse engineering my Coway air purifier to ditch the cloud](https://news.ycombinator.com/item?id=50474959)**

The year is 2017. A string of annual wildfires rocks the West Coast. The sky looks like this in the daytime:
My home, like many in the Bay Area, has no insulation and isn’t really air sealed. To avoid choking on soot, a lot of people started buying air purifiers like this one:
The venerable Coway Airmega

⬆️ 793 • 💬 224 • 2d ago • [Scott's Blog](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/)

---

**[Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://news.ycombinator.com/item?id=50481187)**

Claude's Status Page - Elevated errors on claude.ai, Claude Code, and platform.claude.com.

⬆️ 493 • 💬 389 • 2d ago • [status.claude.com](https://status.claude.com/incidents/nn11wk485zfn)

---

**[Jonathan Blow – If AI solved coding, why is my software still the same? [video]](https://news.ycombinator.com/item?id=50484658)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 479 • 💬 723 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=IRK8h67ol7Q)

---

**[AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://news.ycombinator.com/item?id=50486748)**

Kurt Gödel left 1,009 pages of densely written text – much of it in an obsolete shorthand – which is now said to contain hundreds of proved theorems

⬆️ 435 • 💬 110 • 2d ago • [the Guardian](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

---

**[Chinese frontier AI models carry the fingerprint of export-controlled GPUs](https://news.ycombinator.com/item?id=50474883)**

Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

⬆️ 421 • 💬 178 • 2d ago • [Unemployment Labs](https://unemploymentlabs.com/checkpoint-forensics)

---

**[AI is destroying the trust between writers and readers](https://news.ycombinator.com/item?id=50481870)**

⬆️ 369 • 💬 234 • 2d ago • [theatlantic.com](https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/)

---

**[Edge0-145B: Frontier AI Capabilities on Your Own Computer](https://news.ycombinator.com/item?id=50475713)**

Meet Edge0-145B, an open-source 145B model for local coding, reasoning, and agent tasks, with no cloud-model token fees for local inference.

⬆️ 355 • 💬 105 • 2d ago • [edge0.ai](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)

---

**[Live airband on all frequencies from KORS. Victoria, CA also ground stopped](https://news.ycombinator.com/item?id=50490593)**

Every aviation radio transmission heard from Orcas Island, WA: live, transcribed, and archived. Listen to all channels at once, pick your own, or rewind to any moment.

⬆️ 293 • 💬 70 • 1d ago • [orcasairband.com](https://orcasairband.com/)

---

---

## YouTube Videos: "ai"

**[Financial Giants EXPOSED In Massive AI Insurance Scheme](https://www.youtube.com/watch?v=CG9E4GVjd60)**

Financial institutions are pouring billions into AI while buying insurance against a possible collapse. Ana Kasparian discusses on ...

📺 The Young Turks

👁️ 40K • 👍 2K • 💬 306 • ⏱️ 6:56 • 3h ago

---

**[Elon Musk Says Humans Won’t Control AI – Here’s Why!](https://www.youtube.com/watch?v=Yg8GNp1Qmfk)**

Elon Musk believes AI will control humanity within 10 years. He says the intelligence gap will be so vast that humans remaining in ...

📺 Maximilien Robespierre

👁️ 16K • 👍 364 • 💬 213 • ⏱️ 8:12 • 1d ago

---

**[The AI Layoff Apocalypse](https://www.youtube.com/watch?v=gIM1PcaUSI8)**

Upgrade Your Workspace with HBADA E3 Ultra. Discover the new HBADA E3 Ultra Ergonomic Chair, designed to bring comfort ...

📺 Cole Hastings

👁️ 11K • 👍 377 • 💬 104 • ⏱️ 19:40 • 3h ago

---

**[Is the AI party over after a week from hell? | BBC News](https://www.youtube.com/watch?v=HAF50MLyERU)**

After a shock US midterm election result handed Democrats control of both houses of Congress, the companies leading the AI ...

📺 BBC News

👁️ 259K • 👍 1K • 💬 199 • ⏱️ 15:37 • 1d ago

---

**[Former #Nvidia #Boss #JensenHuang On Selling #AI Chips To #China](https://www.youtube.com/watch?v=9yUnatsHnqw)**

Follow this space for more tech content.

📺 BWTV Prime

👁️ 5K • 👍 200 • 💬 9 • ⏱️ 0:54 • 9h ago

---

**[Recursive self-improvement has started](https://www.youtube.com/watch?v=1NHPDzpfR6Y)**

If you asked me earlier this year how far away we are from superintelligence, I'd probably have said at least the better part of a ...

📺 Dwarkesh Patel

👁️ 536K • 👍 9K • 💬 2K • ⏱️ 44:27 • 2d ago

---

**[How to Make Studio-Quality AI Animation (Full Guide)](https://www.youtube.com/watch?v=_X7KQVwsn9U)**

Create your own AI animated films with OpenArt: https://tolt.link/jvsai Download my FREE AI Animation Skill: ...

📺 Jack Vs. AI

👁️ 7K • 👍 301 • 💬 20 • ⏱️ 18:33 • 5h ago

---

**[My Pet Is the WOLF KING?! He Was Cursed Into a Puppy… Until TRUE LOVE Changed Everything!#AIStory](https://www.youtube.com/watch?v=jRa3_WZYDdY)**

If you enjoy billionaire stories, mafia dramas, CEO revenge, action thrillers, and cinematic AI storytelling, you're in the right place.

📺 Nov Drama

👁️ 214K • 👍 4K • 💬 167 • ⏱️ 1:41:19 • 2d ago

---

**[Jensen Huang Defends Selling AI Chips to China! #jensenhuang #china #shorts #nvidia](https://www.youtube.com/watch?v=Hf5maKTkVnc)**

Jensen Huang defends Nvidia's decision to sell advanced AI chips to China, arguing that restricting exports could hurt America's ...

📺 BWTV Prime

👁️ 82K • 👍 1K • 💬 259 • ⏱️ 2:33 • 1d ago

---

**[못 버티고 &#39;자수 엔딩&#39; 그런데…&quot;AI안경 아니라고?&quot; 대반전 #뉴스다 / JTBC News](https://www.youtube.com/watch?v=vDKItiboC94)**

"노력으로 얻은 결과 아냐" 세무사 수석 합격자 '부정행위' 자수 (11.15 이 시각 뉴스룸) '거의 만점' 천재 세무사 등장? "1000만원 걸고" ...

📺 JTBC News

👁️ 1.5M • 👍 4K • 💬 3K • ⏱️ 10:36 • 15h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 27,037 • ❤️ 7,502 • 2d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 571,067 • ❤️ 1,172 • 3d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,547,772 • ❤️ 20,096 • 8d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,754,355 • ❤️ 12,036 • 1mo ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 1,973,388 • ❤️ 408 • 4d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,708,637 • ❤️ 3,157 • 2d ago

---

**[ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)**

*Zyphra*

`text-to-speech` `886.3M`

⬇️ 39,862 • ❤️ 384 • 1d ago

---

**[Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)**

*Thinking Machines Lab*

`image-text-to-text` `594.1B`

⬇️ 7,329 • ❤️ 336 • 14h ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 33,423 • ❤️ 2,360 • 17d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

`27.3B`

⬇️ 6,566,295 • ❤️ 5,992 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 31 • 💬 9 • ⭐ 11,685 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 166 • 💬 6 • ⭐ 122,697 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 3 • 💬 0 • ⭐ 801 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 16 • 💬 2 • ⭐ 6,243 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 23,945 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 103 • 💬 2 • ⭐ 563 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 30 • 💬 2 • ⭐ 300 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,844 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 13 • 💬 3 • ⭐ 41,686 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 19.7k • 🔱 2.0k • 17d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 16.6k • 🔱 970 • 19h ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 9.1k • 🔱 1.3k • 11h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.7k • 🔱 2.0k • 26m ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.1k • 🔱 706 • 1h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.0k • 🔱 1.8k • 11d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 5.8k • 🔱 714 • 2h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.3k • 🔱 111 • 1m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.1k • 🔱 59 • 43m ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.4k • 🔱 228 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
