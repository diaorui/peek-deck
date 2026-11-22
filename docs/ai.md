---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-22T23:44:33.199167+00:00'
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

**Last Updated:** November 22, 2026 at 23:44 UTC  
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

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 6d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

5d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

6d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 6d ago

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

**[Looking for the Formula to Stop an Apocalypse](https://www.nytimes.com/2026/11/22/magazine/looking-for-the-formula-to-stop-an-apocalypse.html)**

The New York Times • 11h ago

---

**[Anthropic Mathematician Claims to Have Solved Math’s Most Famous Problem](https://www.nytimes.com/2026/11/20/science/anthropic-ai-math-riemann-hypothesis.html)**

The New York Times • 2d ago

---

**[Why I won’t leave mathematics, despite AI solving centuries-old problems | Ken Ono](https://www.theguardian.com/commentisfree/2026/nov/22/why-i-wont-leave-mathematics-despite-ai-solving-centuries-old-problems)**

I believe human judgment remains essential

The Guardian • 12h ago

---

**[Stocks are 'on fire sale' as Anthropic IPO fails to calm AI trade jitters](https://finance.yahoo.com/markets/article/stocks-are-on-fire-sale-as-anthropic-ipo-fails-to-calm-ai-trade-jitters-190051253.html)**

Anthropic's public debut did little to calm the stock market as the AI trade unravels.

Yahoo Finance • 4h ago

---

**[Investors Brave Stock Market ‘Fragility’ as AI Trade Falters](https://www.bloomberg.com/news/articles/2026-11-22/investors-brave-stock-market-fragility-as-ai-trade-falters)**

Bloomberg.com • 8h ago

---

**[3 AI Hardware Stocks Down More Than 30% From Their Records to Buy Now and Hold Through 2030](https://finance.yahoo.com/technology/ai/articles/3-ai-hardware-stocks-down-220302382.html)**

Each of these AI suppliers sits well below its record close. Has data center demand actually cooled that much?

Yahoo Finance • 1h ago

---

**[Trump’s AI Chip Crackdown Inflicts Collateral Damage Across Asia](https://www.bloomberg.com/news/features/2026-11-22/trump-s-ai-chip-crackdown-on-china-after-nvidia-crisis-squeezes-southeast-asia)**

Bloomberg.com • 1h ago

---

**[Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/)**

How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

OpenAI • 4h ago

---

**[OpenAI Chief Scientist Urges Industry Limits on AI Development](https://www.bloomberg.com/news/articles/2026-11-22/openai-chief-scientist-urges-industry-limits-on-ai-development)**

Bloomberg.com • 4h ago

---

**[OpenAI scientist proposes industry AI limits tied to model intelligence metric](https://www.reuters.com/business/openai-scientist-proposes-industry-ai-limits-tied-model-intelligence-metric-2026-11-22/)**

Reuters • 34m ago

---

---

## HackerNews: "ai"

**[Frostbite: A new CPU architecture discovered, designed and verified by AI](https://news.ycombinator.com/item?id=50572503)**

Frostbite is a general-purpose CPU built around interaction nets, discovered, designed, and verified end-to-end by our AI systems, reaching 4.59x the performance-per-watt of a modern superscalar (dual-issue, in-order) CPU core.

⬆️ 678 • 💬 362 • 2d ago • [Architect Labs](https://architectlabs.com/blog/frostbite)

---

**[Restricting AI agents in mobile operating systems platforms from capturing data](https://news.ycombinator.com/item?id=50572348)**

Privacy is our mission; it’s why we exist, and we do everything we can to protect it. This means that we are restricting the latest AI agents built into mobile operating systems from potentially capturing and storing your Signal data.

⬆️ 577 • 💬 346 • 2d ago • [Signal Messenger](https://signal.org/blog/protecting-your-privacy/)

---

**[Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day](https://news.ycombinator.com/item?id=50574383)**

Asian markets record worst week since 2020 as investors question huge sums being poured into AI buildout

⬆️ 527 • 💬 919 • 2d ago • [the Guardian](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

---

**[Google workers tell their employer not to punish schools that don't want AI](https://news.ycombinator.com/item?id=50577901)**

Executives are “convinced that resistance to AI" just means schools "don’t see the vision,” a Google staffer said.

⬆️ 283 • 💬 229 • 2d ago • [Mother Jones](https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/)

---

**[ClawDOS – An AI coding agent for DOS](https://news.ycombinator.com/item?id=50586292)**

An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz)

⬆️ 172 • 💬 52 • 1d ago • [ClawDOS](http://ricapar.net/ClawDOS/)

---

**[The Mythology of Conscious AI](https://news.ycombinator.com/item?id=50595537)**

Why consciousness is more likely a property of life than of computation and why creating conscious, or even conscious-seeming AI, is a bad idea.

⬆️ 164 • 💬 456 • 21h ago • [NOEMA](https://www.noemamag.com/the-mythology-of-conscious-ai/)

---

**[Pandex – Official European Law for AI Agents, over MCP](https://news.ycombinator.com/item?id=50593481)**

Legislation and highest-court decisions of the EU, seven European countries and the European Court of Human Rights, from the institutions that publish them, in one API and MCP server built for search and AI.

⬆️ 139 • 💬 33 • 1d ago • [Pandex](https://www.pandex.io)

---

**[AI is giving everyone the same advice](https://news.ycombinator.com/item?id=50577872)**

I asked 65 AIs from 30 companies the questions people ask them every day, 127,918 times. 73 of every 100 people were told to read the same book. See every answer, and the two prompts that get you your own.

⬆️ 124 • 💬 53 • 2d ago • [A90](https://a90.com/experiments/same-advice/)

---

**[A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://news.ycombinator.com/item?id=50603845)**

We have AI at home! Set up your own free personal ChatGPT on your PC with Unsloth and Inkling or Qwen. It's private, and the whole house can use it.

⬆️ 122 • 💬 39 • 2h ago • [gpupartner.com](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

---

**[AI is becoming a disaster for the climate](https://news.ycombinator.com/item?id=50598961)**

Two new studies reveal the exploding carbon emissions of the AI industry, while Silicon Valley pushes to kill communities’ means of protesting data centers and the impacts on human health mount.

⬆️ 97 • 💬 42 • 11h ago • [bloodinthemachine.com](https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the)

---

---

## YouTube Videos: "ai"

**[It Happened... The AI Bubble Just Cracked (Worst Week For AI Ever)](https://www.youtube.com/watch?v=_4NZedIB55o)**

AI just had its best week and its worst week at the same time. Anthropic went public at nearly $2 trillion while protesters chanted ...

📺 AI Revolution

👁️ 41K • 👍 656 • 💬 88 • ⏱️ 14:05 • 22h ago

---

**[OpenAI Warns AI Could Take Over Within 12 Months](https://www.youtube.com/watch?v=Dx_oAiLIK1E)**

Subscribe To My Newsletter - https://aigrid.beehiiv.com/subscribe Learn AI With Me For Free ...

📺 TheAIGRID

👁️ 63K • 👍 853 • 💬 264 • ⏱️ 29:39 • 16h ago

---

**[Since last year, we asked: “What if AI solved the Riemann Hypothesis?”](https://www.youtube.com/watch?v=zqzk43bSdDI)**

Hypothetical no more Announcement by Levent Alpöge: https://alpo.ge/remark.pdf Announcement by Alessandro Masullo on his ...

📺 3Blue1Brown

👁️ 2.0M • 👍 34K • 💬 4K • ⏱️ 13:39 • 21h ago

---

**[AI Genius Predicts the Exact Month Superintelligence Arrives](https://www.youtube.com/watch?v=rOXnBQrxGqs)**

Ryan Christian of Vals.ai and Joe Lonsdale discuss the Vals RSI index, which projects Anthropic reaching full recursive ...

📺 Joe Lonsdale

👁️ 58K • 👍 537 • 💬 103 • ⏱️ 7:00 • 2d ago

---

**[Jan Local AI in Linux &amp; Windows](https://www.youtube.com/watch?v=mzrrVhgWTq4)**

Jan local AI installation and demos. Video mainly runs the Jan Desktop client in Linux (Ubuntu), but also includes installation and ...

📺 ExplainingComputers

👁️ 54K • 👍 3K • 💬 248 • ⏱️ 24:16 • 9h ago

---

**[How to Make Long AI Videos with Consistent Characters (2026)](https://www.youtube.com/watch?v=dx05ivXQ4Ko)**

Create Your Own 2D Cartoon Animations https://higgsfield.ai?fpr=ai&fp_sid=isa Sign Up to Higgsfield & Get My AI Kit for ...

📺 Isa does AI

👁️ 7K • 💬 1 • ⏱️ 10:10 • 8h ago

---

**[GTA 6 Needed 1,000 Devs... One 20-Year-Old Used 250 AI Agents Instead! 🤯](https://www.youtube.com/watch?v=H8cdQs6GGBs)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://join.switchit.app/YT ...

📺 Vaibhav Sisinty

👁️ 30K • 👍 937 • 💬 11 • ⏱️ 1:37 • 12h ago

---

**[I know who&#39;s popping the AI bubble now](https://www.youtube.com/watch?v=YNTpOLbvKTs)**

Get $50 in free credits with AssemblyAI https://www.assembly.ai/mo (no credit card required) The Federal Reserve decided AI was ...

📺 Mo Bitar

👁️ 177K • 👍 5K • 💬 846 • ⏱️ 12:23 • 12h ago

---

**[AI Is Getting Intelligent. But Not How You Think](https://www.youtube.com/watch?v=-MiM5xfAe2c)**

Thanks to Mammouth AI for sponsoring this video: https://mammouth.ai No one really knows how AI works. Scientists are figuring it ...

📺 Sabine Hossenfelder

👁️ 373K • 👍 8K • 💬 1K • ⏱️ 6:51 • 1d ago

---

**[&quot;Where do we go next?&quot; Mathematics after AI cracks the Riemann hypothesis • FRANCE 24 English](https://www.youtube.com/watch?v=fvN_vCRuBec)**

Anthropic mathematician Levent Alpöge says he used Claude to prove the Riemann hypothesis, one of maths' $1 million ...

📺 FRANCE 24 English

👁️ 307K • 👍 2K • 💬 492 • ⏱️ 6:17 • 9h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 23,543 • ❤️ 4,948 • 1d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 805,993 • ❤️ 873 • 19h ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 632 • 8d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 6,617 • ❤️ 620 • 3d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 2,831 • ❤️ 991 • 1d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 129,693 • ❤️ 476 • 1d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 8,608 • ❤️ 892 • 9d ago

---

**[DepthPro2](https://huggingface.co/apple/DepthPro2)**

*Apple*

`depth-estimation`

⬇️ 0 • ❤️ 281 • 2d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,297,396 • ❤️ 20,884 • 15d ago

---

**[SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B)**

*SenseNova*

`image-text-to-text` `9.7B`

⬇️ 1,863 • ❤️ 533 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 12 • 💬 0 • ⭐ 5,916 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 106 • 💬 7 • ⭐ 32,005 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 34 • 💬 3 • ⭐ 444 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 150 • 💬 4 • ⭐ 1,299 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 7,948 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,502 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 20 • 💬 2 • ⭐ 429 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 71 • 💬 4 • ⭐ 24,775 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 22 • 💬 0 • ⭐ 42,402 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

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

⭐ 20.3k • 🔱 1.2k • 7d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 12.2k • 🔱 1.8k • 8h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.6k • 🔱 2.2k • 5h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.8k • 🔱 764 • 1d ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.8k • 🔱 2.0k • 4d ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 6.8k • 🔱 541 • 10m ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.5k • 🔱 235 • 4h ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.4k • 🔱 796 • 18h ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 5.0k • 🔱 629 • 47m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 112 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
