---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-15T06:58:25.757443+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 15, 2026 at 06:58 UTC  
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

I've embarrassingly been working on this project for 2 years so wanted to finally share (as I saw others posting Youtube-only versions). on Youtube it transcribes text to identify checkable claims -> web search retrieves sources to base Claude's verdict on, to avoid hallucinated sources. it's a free Chrome extension, and works on news or social media sites as well. let me know what would make this something you'd use, or what else you'd like to see! Edit: I realized someone not following could misread the video (here Biden is telling the truth, and Trump was lying, but the Trump section is before I started the recording).

2h ago

---

**[One Router Grounded America? Seriously? Are you sure it wasn’t Rogue AI or a Hack?](https://www.reddit.com/r/artificial/comments/1xwd18l/one_router_grounded_america_seriously_are_you/)**

So apparently the Trump administration is blaming a faulty router for grounding flights across America. A router. Seriously? Of course a router can cause network failures, but how the hell does critical national aviation infrastructure lack the safeguards to prevent one failure cascading across the system? And who in their right mind schedules an upgrade at 3 pm on a Friday afternoon? I seriously smell a rat because the explanation raises more concerns than answers? Is America being gaslit?

10h ago

---

**[Anthropic rebuilds Claude Code Projects around a coordinator and parallel worker threads - each thread is a full cloud session on its own branch](https://www.reddit.com/r/artificial/comments/1xwj3v0/anthropic_rebuilds_claude_code_projects_around_a/)**

Anthropic posted an update on Nov 14 rebuilding Claude Projects from a folder of files into a coordinated set of working sessions. You describe the work in one conversation; a coordinator scopes it, delegates it to parallel threads, reviews the outputs and assembles the result. Each thread is a Claude Code cloud session with its own copy of the repo and its own Git branch, and it can split its task further into subagents, loops or workflows. The work keeps going after you close your laptop, and you can steer it from your phone. It is a public beta rolling out gradually to select Pro/Max/Ultra subscribers who use Claude Code cloud sessions; Team and Enterprise plans do not have it yet, and there is a waitlist for everyone else. Anthropic is upfront about the limits: threads run only in the cloud for now (local code and VPN support is coming 'very soon'), several parallel sessions burn through usage limits faster, and if two threads touch the same code it surfaces as an ordinary merge conflict in a PR. Sources: Anthropic's product post (claude.com/blog/projects-redesigned) and the Projects docs (code.claude.com/docs/en/claude-projects). What I am curious about: does parallelizing agents actually speed up real work, or does it just move the bottleneck to review and merge conflicts? Has anyone here tried the beta?

5h ago

---

**[It's 11:21pm and I'm not coding anymore — my agents are](https://www.reddit.com/r/artificial/comments/1xwok88/its_1121pm_and_im_not_coding_anymore_my_agents_are/)**

​ This is my laptop right now. I built AIPass — open-source, 18 agents running on my own Linux machine — and tonight they're just... going. Sentry's doing a memory rollover, Prax is digging through a dead-cwd guard in repo_root.py, DevPulse's sub-agents are checking canary docs and skills docs. Trigger even muted Prax for a bit. The API hit a 429 so it's backing off for 60 seconds. The weird part is BAUD on the right is literally waiting on me to pick A or B for the init cut. I'm the bottleneck now. They wake up in the evening, check email, fix bugs, try to optimise stuff. I mostly just watch. If you had a crew like this running overnight, what would you actually have it do first?

21m ago

---

**[Could AI handle public transit information calls?](https://www.reddit.com/r/artificial/comments/1xw6eqj/could_ai_handle_public_transit_information_calls/)**

During service disruptions people are calling about delays, missed connections, route changes and whether theres another bus or train coming And the information can change every few minutes The phone part seems doable with tools like Elevenlabs or Bland, but I'd want it connected directly to the transit system's live updates before trusting it with arrival times. Giving someone an outdated ETA is probably worse than telling them there's no confirmed time yet.

14h ago

---

**[Anyone else my age in here??](https://www.reddit.com/r/artificial/comments/1xwo2z5/anyone_else_my_age_in_here/)**

49m ago

---

**[Not all AI sounds human.](https://www.reddit.com/r/artificial/comments/1xwo2iz/not_all_ai_sounds_human/)**

Some AI models don’t generate tokens or try to sound like your best friend.

🔗 [blog.galratner.com](https://blog.galratner.com/p/not-all-ai-sounds-human) • 50m ago

---

**[Don't we want the AI to do our work...](https://www.reddit.com/r/artificial/comments/1xwlffv/dont_we_want_the_ai_to_do_our_work/)**

Most people have jobs they would rather not do, but they need to get paid. Instead of "protecting jobs from AI" we should be thinking about how people can live without needing jobs and let the machines do the boring work nobody wants to do in the first place.

🔗 [towardsdatascience.com](https://towardsdatascience.com/ai-will-do-your-job-that-should-be-good-news/) • 3h ago

---

**[The Chrisrmas Tree Test. Fable, Opus, Haiku. You decide...Just for fun](https://www.reddit.com/r/artificial/comments/1xwj5u8/the_chrisrmas_tree_test_fable_opus_haiku_you/)**

Here I have 3 Christmas trees. I prompted each agent " built me a Christmas tree widget in 2 minutes " just a quick fun experiment. Here are the results. You decide. Which is your favorite.

5h ago

---

**[OpenAI is so convinced that LLMs will become brains for robots that it has disbanded its robotics team](https://www.reddit.com/r/artificial/comments/1xvivdy/openai_is_so_convinced_that_llms_will_become/)**

https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/

1d ago

---

---

## Google News: "ai"

**[‘Jensen Huang lost his mind’: how AI’s smartest man fell for the world’s oldest trick](https://www.theguardian.com/technology/2026/nov/14/jensen-huang-affair-nvidia-nightmare)**

Jensen Huang’s affair with a suspected spy is Silicon Valley’s worst nightmare come true

The Guardian • 58m ago

---

**[How Jensen Huang Built the Backdoor Route That Keeps Beijing in the AI Race](https://www.wsj.com/tech/jensen-huang-backdoor-ai-data-centers-a5e4499d)**

WSJ • 4h ago

---

**[The Nvidia scandal is heightening America's AI rivalry with China ahead of Trump's visit](https://www.dallasnews.com/news/politics/article/the-nvidia-scandal-is-heightening-america-s-ai-22530398.php)**

Dallas News • 12m ago

---

**[AI's four colliding crises](https://www.axios.com/2026/11/14/ai-trust-nvidia-tech-stocks)**

Axios • 17h ago

---

**[Top scorer on South Korean tax exam confesses to cheating with AI](https://www.reuters.com/world/asia-pacific/top-scorer-south-korean-tax-exam-confesses-cheating-with-ai-2026-11-15/)**

Reuters • 2h ago

---

**[AI Cheating Scandal Prompts Blue House Policy Meeting](https://www.chosun.com/english/national-en/2026/11/15/6CR57BZO7BATDCLRAQEF2INZQ4/)**

AI Cheating Scandal Prompts Blue House Policy Meeting Top tax accountants AI-assisted cheating confession triggers urgent CSAT countermeasures

조선일보 • 13m ago

---

**[Tax accountant exam's top scorer admits to AI-assisted cheating](https://www.koreaherald.com/article/10937374)**

The top scorer in this year's tax accountant qualification exam in South Korea has turned himself in to the police and admitted to using AI to cheat. Han Won-se

The Korea Herald • 5h ago

---

**[Could everything be broken? Grounded jets, Microsoft outage, AI chaos make some wonder](https://apnews.com/article/flights-grounded-microsoft-ai-chaos-ea5f7a1f95a38f65dd57e58cfc17672b)**

AP News • 1h ago

---

**[Anthropic IPO to test Wall Street’s faith in AI as skepticism mounts](https://finance.yahoo.com/markets/stocks/article/anthropic-ipo-to-test-wall-streets-faith-in-ai-as-skepticism-mounts-180007104.html)**

Anthropic seeks a valuation of approximately $1.3 trillion to $1.4 trillion.

Yahoo Finance • 12h ago

---

**[Thousands turn out in Edinburgh to protest against AI data centres](https://www.bbc.com/news/articles/c8n50w445zgpo)**

Demonstrators armed with placards - and some dressed in costume - assembled at the top of the Royal Mile before marching towards the Scottish Parliament.

BBC • 13h ago

---

---

## HackerNews: "ai"

**[Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs](https://news.ycombinator.com/item?id=50493251)**

Following the departure of now-former NVIDIA CEO, Jensen Huang, a new report by The Wall Street Journal (via Wccftech) has emerged alleging that NVIDIA artificially inflated the ongoing GPU and memory shortage by investing in AI startups that would go on to buy NVIDIA GPUs and build data centers....

⬆️ 1063 • 💬 629 • 1d ago • [TechPowerUp](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)

---

**[Reverse engineering my Coway air purifier to ditch the cloud](https://news.ycombinator.com/item?id=50474959)**

The year is 2017. A string of annual wildfires rocks the West Coast. The sky looks like this in the daytime:
My home, like many in the Bay Area, has no insulation and isn’t really air sealed. To avoid choking on soot, a lot of people started buying air purifiers like this one:
The venerable Coway Airmega

⬆️ 787 • 💬 222 • 2d ago • [Scott's Blog](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/)

---

**[Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://news.ycombinator.com/item?id=50481187)**

Claude's Status Page - Elevated errors on claude.ai, Claude Code, and platform.claude.com.

⬆️ 493 • 💬 391 • 1d ago • [status.claude.com](https://status.claude.com/incidents/nn11wk485zfn)

---

**[Jonathan Blow – If AI solved coding, why is my software still the same? [video]](https://news.ycombinator.com/item?id=50484658)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 468 • 💬 688 • 1d ago • [youtube.com](https://www.youtube.com/watch?v=IRK8h67ol7Q)

---

**[AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://news.ycombinator.com/item?id=50486748)**

Kurt Gödel left 1,009 pages of densely written text – much of it in an obsolete shorthand – which is now said to contain hundreds of proved theorems

⬆️ 427 • 💬 108 • 1d ago • [the Guardian](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

---

**[Chinese frontier AI models carry the fingerprint of export-controlled GPUs](https://news.ycombinator.com/item?id=50474883)**

Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

⬆️ 395 • 💬 166 • 2d ago • [Unemployment Labs](https://unemploymentlabs.com/checkpoint-forensics)

---

**[AI is destroying the trust between writers and readers](https://news.ycombinator.com/item?id=50481870)**

⬆️ 366 • 💬 228 • 1d ago • [theatlantic.com](https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/)

---

**[Edge0-145B: Frontier AI Capabilities on Your Own Computer](https://news.ycombinator.com/item?id=50475713)**

Meet Edge0-145B, an open-source 145B model for local coding, reasoning, and agent tasks, with no cloud-model token fees for local inference.

⬆️ 353 • 💬 105 • 2d ago • [edge0.ai](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)

---

**[Live airband on all frequencies from KORS. Victoria, CA also ground stopped](https://news.ycombinator.com/item?id=50490593)**

Every aviation radio transmission heard from Orcas Island, WA: live, transcribed, and archived. Listen to all channels at once, pick your own, or rewind to any moment.

⬆️ 292 • 💬 70 • 1d ago • [orcasairband.com](https://orcasairband.com/)

---

**[No AI Slop: A Manifesto](https://news.ycombinator.com/item?id=50488769)**

The No AI Slop Manifesto, from the speakers and attendees of AIE Code Summit 2026.

⬆️ 219 • 💬 131 • 1d ago • [slopmanifesto.com](https://www.slopmanifesto.com/)

---

---

## YouTube Videos: "ai"

**[Is the AI party over after a week from hell? | BBC News](https://www.youtube.com/watch?v=HAF50MLyERU)**

After a shock US midterm election result handed Democrats control of both houses of Congress, the companies leading the AI ...

📺 BBC News

👁️ 181K • 👍 768 • 💬 160 • ⏱️ 15:37 • 16h ago

---

**[China’s New FREE AI Built This 3D Game in 8 Minutes (No Coding)](https://www.youtube.com/watch?v=r9IF2WXAZek)**

Make a 3D game with AI for FREE, zero coding (ERNIE 5.5 Flash + OpenCode + OpenRouter) Free guide + ALL prompts: ...

📺 Maitis

👁️ 15K • 👍 389 • 💬 19 • ⏱️ 17:45 • 15h ago

---

**[OpenAI&#39;s New AI Is Too Powerful To Release](https://www.youtube.com/watch?v=qCE5A2bWZz8)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 50K • 👍 822 • 💬 142 • ⏱️ 30:56 • 22h ago

---

**[NVIDIA&#39;s Tiny AI Supercomputer Is a Powerhouse 🤯 #nvidia #shorts](https://www.youtube.com/watch?v=RAqXPtjti3g)**

NVIDIA just showed how powerful personal AI computing can become! Jensen Huang introduces NVIDIA Project DIGITS, ...

📺 VisionX Lab

👁️ 484K • 👍 8K • 💬 185 • ⏱️ 0:47 • 2d ago

---

**[Musk Makes MASSIVE AI Move After Midterm Disaster](https://www.youtube.com/watch?v=FaErjxv_nlE)**

Elon Musk wants to pour more than $74 billion into building data centers in Arizona and Texas. Keith Edwards, John Iadarola and ...

📺 The Young Turks

👁️ 132K • 👍 2K • 💬 480 • ⏱️ 16:37 • 1d ago

---

**[AI News: Things Will Never Be The Same](https://www.youtube.com/watch?v=G_Jrexy_5Bg)**

Try @OpenAI Decisions API here: https://developers.openai.com/api/docs/guides/decisions Here's the AI news from one of the ...

📺 Matt Wolfe

👁️ 129K • 👍 2K • 💬 241 • ⏱️ 27:11 • 1d ago

---

**[Richard Wolff: It&#39;s Over, China Has Won – AI Bubble Collapsing](https://www.youtube.com/watch?v=HoyGaIaGccg)**

Prof. Richard Wolff discusses why China has won the economic war, and why the US is increasingly likely to respond with military ...

📺 Glenn Diesen

👁️ 51K • 👍 3K • 💬 297 • ⏱️ 51:59 • 12h ago

---

**[It’s Happening... SUPERHUMAN AI Is Almost Here! (Everything Changes)](https://www.youtube.com/watch?v=HPCayerH1Jw)**

Superhuman AI could arrive in 2027 as new Anthropic evidence pulls forecasts forward. AI is accelerating its own development, ...

📺 AI Revolution

👁️ 72K • 👍 975 • 💬 127 • ⏱️ 13:43 • 2d ago

---

**[Harvard Just Discovered AI Isn’t Actually Working](https://www.youtube.com/watch?v=xWk9MP4ed-4)**

Harvard's finding are actually insane Interested in supporting the channel? Become a channel member!

📺 Dylan John

👁️ 382K • 👍 7K • 💬 1K • ⏱️ 14:28 • 1d ago

---

**[Google&#39;s AI glasses take privacy more seriously](https://www.youtube.com/watch?v=0aCLnZp_ZFA)**

Meta's finally got real competition. Google's new AI glasses and their demos were better than expected when The Verge's Victoria ...

📺 The Verge

👁️ 39K • 👍 922 • 💬 42 • ⏱️ 2:34 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 24,470 • ❤️ 7,403 • 2d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 517,948 • ❤️ 1,130 • 3d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,757,964 • ❤️ 20,037 • 8d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,777,667 • ❤️ 11,954 • 1mo ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,657,783 • ❤️ 3,134 • 1d ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 1,615,613 • ❤️ 390 • 3d ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 32,619 • ❤️ 2,344 • 16d ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 6,191 • ❤️ 599 • 8d ago

---

**[ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)**

*Zyphra*

`text-to-speech` `886.3M`

⬇️ 19,743 • ❤️ 353 • 1d ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 43,687 • ❤️ 2,083 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 31 • 💬 9 • ⭐ 11,633 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 166 • 💬 6 • ⭐ 122,566 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 23,904 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 16 • 💬 2 • ⭐ 6,121 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 103 • 💬 2 • ⭐ 533 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 3 • 💬 0 • ⭐ 516 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 30 • 💬 2 • ⭐ 264 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 12 • 💬 3 • ⭐ 41,668 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,814 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 19.6k • 🔱 2.0k • 17d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 16.2k • 🔱 946 • 6h ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 8.7k • 🔱 1.3k • 2h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.6k • 🔱 2.0k • 30m ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.1k • 🔱 701 • 37s ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.0k • 🔱 1.8k • 10d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 5.7k • 🔱 701 • 12h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.2k • 🔱 103 • 3m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 3.9k • 🔱 58 • 9h ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.3k • 🔱 224 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
