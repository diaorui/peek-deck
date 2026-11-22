---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-22T18:15:41.262766+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 22, 2026 at 18:15 UTC  
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

**[Tech Outages Are Only the Beginning. A.I. Will Bring More Disruptions.](https://www.nytimes.com/2026/11/21/us/politics/tech-outages-ai-disruptions.html)**

The New York Times • 23h ago

---

**[Hacks, AI and conspiracy theories: why are we having so many outages? | Technology](https://www.theguardian.com/technology/2026/nov/22/hacks-ai-internet-outages-airlines-banks-microsoft-apple)**

After chaos at airlines, banks and companies from Microsoft to Apple, people have become convinced the world’s systems are under attack

The Guardian • 12h ago

---

**[Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/)**

How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

OpenAI • 1h ago

---

**[Elon Musk warns data center delays could leave AI companies short on cash: 'Going to be nuts'](https://www.businessinsider.com/elon-musk-warning-ai-compute-data-centers-cash-spacex-tesla-2026-11)**

Elon Musk's warning of a "cash shortage" comes on the heels of an intense market sell-off in AI and tech.

Business Insider • 26m ago

---

**[As AI detects flaws in computer systems, is it causing more tech outages and disruptions?](https://www.pbs.org/newshour/nation/as-ai-detects-flaws-in-computer-systems-is-it-causing-more-tech-outages-and-disruptions)**

PBS • 1h ago

---

**[In China’s tech mecca, Trump and Xi touted AI cooperation. Now comes the harsh reality](https://www.cnn.com/2026/11/22/business/trump-xi-apec-tech-rivalry-intl-hnk)**

Neither Xi or Trump was keen to dredge up the Nvidia scandal threatening a delicate detente between the world’s two largest economies.

CNN • 13h ago

---

**[AI is being used to clone real people's videos](https://www.bbc.com/news/articles/cm7527kp4qrpo)**

Musicians, comedians and dancers are among those finding their videos cloned with AI generated characters.

BBC • 13h ago

---

**[John Kennedy: If Howard Lutnick is giving AI chips away to China, ‘he needs to stop’](https://www.nbcnews.com/meet-the-press/video/john-kennedy-if-howard-lutnick-is-giving-ai-chips-away-to-china-he-needs-to-stop-273979973777)**

Sen. John Kennedy (R-La.) says on Meet the Press he wants answers from Treasury Secretary Scott Bessent and Commerce Secretary Howard Lutnick amid national security concerns and scandals involving Nvidia’s former CEO Jensen Huang.

NBC News • 1h ago

---

**[Michael Burry warns AI stocks mirror 1929 and 2000 crashes — and singles out Nvidia's risky deals](https://finance.yahoo.com/markets/stocks/articles/michael-burry-warns-ai-stocks-223000286.html)**

Was Burry right about the “AI bubble?” Find out what “The Big Short” superinvestor is saying about the AI trade and why he thinks the tech wreck isn’t over.

Yahoo Finance • 1d ago

---

**[Analysis | Entitled and out of touch, AI CEOs are heading for a fall](https://www.washingtonpost.com/business/2026/11/21/history-lesson-ai-ceos-alienate-americans-your-own-peril/)**

Americans tend to turn against out-of-touch CEOs, and a public reckoning on the tech industry could already be underway.

The Washington Post • 1d ago

---

---

## HackerNews: "ai"

**[Frostbite: A new CPU architecture discovered, designed and verified by AI](https://news.ycombinator.com/item?id=50572503)**

Frostbite is a general-purpose CPU built around interaction nets, discovered, designed, and verified end-to-end by our AI systems, reaching 4.59x the performance-per-watt of a modern superscalar (dual-issue, in-order) CPU core.

⬆️ 675 • 💬 362 • 2d ago • [Architect Labs](https://architectlabs.com/blog/frostbite)

---

**[Restricting AI agents in mobile operating systems platforms from capturing data](https://news.ycombinator.com/item?id=50572348)**

Privacy is our mission; it’s why we exist, and we do everything we can to protect it. This means that we are restricting the latest AI agents built into mobile operating systems from potentially capturing and storing your Signal data.

⬆️ 577 • 💬 345 • 2d ago • [Signal Messenger](https://signal.org/blog/protecting-your-privacy/)

---

**[Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day](https://news.ycombinator.com/item?id=50574383)**

Asian markets record worst week since 2020 as investors question huge sums being poured into AI buildout

⬆️ 523 • 💬 915 • 2d ago • [the Guardian](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

---

**[Google workers tell their employer not to punish schools that don't want AI](https://news.ycombinator.com/item?id=50577901)**

Executives are “convinced that resistance to AI" just means schools "don’t see the vision,” a Google staffer said.

⬆️ 283 • 💬 229 • 2d ago • [Mother Jones](https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/)

---

**[ClawDOS – An AI coding agent for DOS](https://news.ycombinator.com/item?id=50586292)**

An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz)

⬆️ 167 • 💬 52 • 1d ago • [ClawDOS](http://ricapar.net/ClawDOS/)

---

**[The Mythology of Conscious AI](https://news.ycombinator.com/item?id=50595537)**

Why consciousness is more likely a property of life than of computation and why creating conscious, or even conscious-seeming AI, is a bad idea.

⬆️ 134 • 💬 367 • 16h ago • [NOEMA](https://www.noemamag.com/the-mythology-of-conscious-ai/)

---

**[Pandex – Official European Law for AI Agents, over MCP](https://news.ycombinator.com/item?id=50593481)**

Legislation and highest-court decisions of the EU, seven European countries and the European Court of Human Rights, from the institutions that publish them, in one API and MCP server built for search and AI.

⬆️ 132 • 💬 31 • 21h ago • [Pandex](https://www.pandex.io)

---

**[AI is giving everyone the same advice](https://news.ycombinator.com/item?id=50577872)**

I asked 65 AIs from 30 companies the questions people ask them every day, 127,918 times. 73 of every 100 people were told to read the same book. See every answer, and the two prompts that get you your own.

⬆️ 124 • 💬 53 • 2d ago • [A90](https://a90.com/experiments/same-advice/)

---

**[Should governments slow frontier AI? Jacob Coxon and Robin Hanson debate [video]](https://news.ycombinator.com/item?id=50564366)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 115 • 💬 258 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=lwfewYL7X0o)

---

**[AI Supply Chain Security: What Canary Tokens Found](https://news.ycombinator.com/item?id=50596511)**

We seeded two million AI prompts with canary tokens and found three provider breaches, prompt theft, and ignored Zero Data Retention settings.

⬆️ 91 • 💬 21 • 13h ago • [Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

---

---

## YouTube Videos: "ai"

**[Since last year, we asked: “What if AI solved the Riemann Hypothesis?”](https://www.youtube.com/watch?v=zqzk43bSdDI)**

Hypothetical no more Announcement by Levent Alpöge: https://alpo.ge/remark.pdf Announcement by Alessandro Masullo on his ...

📺 3Blue1Brown

👁️ 1.6M • 👍 30K • 💬 3K • ⏱️ 13:39 • 16h ago

---

**[How to Make AI Short Films Better than 99% of People](https://www.youtube.com/watch?v=siZcUPnoRE4)**

Create Your Own AI Short Films https://tolt.link/robo-shortfilms Sign up to OpenArt & Get my VIP Package for FREE ...

📺 Roboverse

👁️ 4K • 💬 1 • ⏱️ 19:27 • 2h ago

---

**[AI Genius Predicts the Exact Month Superintelligence Arrives](https://www.youtube.com/watch?v=rOXnBQrxGqs)**

Ryan Christian of Vals.ai and Joe Lonsdale discuss the Vals RSI index, which projects Anthropic reaching full recursive ...

📺 Joe Lonsdale

👁️ 49K • 👍 489 • 💬 93 • ⏱️ 7:00 • 2d ago

---

**[AI out of control? - Why Artificial Intelligence experts are sounding the alarm | DW Documentary](https://www.youtube.com/watch?v=2I4qMBiK6hg)**

Artificial Intelligence is permeating our everyday lives at breathtaking speed. It is taking on more tasks that were previously the ...

📺 DW Documentary

👁️ 404K • 👍 4K • 💬 599 • ⏱️ 1:28:52 • 1d ago

---

**[AI Is Getting Intelligent. But Not How You Think](https://www.youtube.com/watch?v=-MiM5xfAe2c)**

Thanks to Mammouth AI for sponsoring this video: https://mammouth.ai No one really knows how AI works. Scientists are figuring it ...

📺 Sabine Hossenfelder

👁️ 332K • 👍 7K • 💬 990 • ⏱️ 6:51 • 1d ago

---

**[AI Job Interviewer vs. Santa (Full Version)](https://www.youtube.com/watch?v=uXrxSu-sJG0)**

Santa has a job interview with AI Karen… and she's definitely putting him on the naughty list Watch Santa try to convince ...

📺 Nick Reid

👁️ 94K • 👍 2K • 💬 393 • ⏱️ 8:25 • 2d ago

---

**[Big Short Investor: Is the AI Bubble About to Burst? - Steve Eisman](https://www.youtube.com/watch?v=hkdcESS5uMw)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Venice gives you the best AI ...

📺 Triggernometry

👁️ 302K • 👍 4K • 💬 2K • ⏱️ 1:26:10 • 23h ago

---

**[How the U.S. Economy Is Tied to A.I.](https://www.youtube.com/watch?v=ZEYtG84Sf1w)**

Ben Casselman, our chief economics correspondent, explains how A.I. has become a huge piece of the U.S. economy and how it ...

📺 The New York Times

👁️ 726 • 👍 56 • 💬 2 • ⏱️ 3:00 • 30m ago

---

**[I know who&#39;s popping the AI bubble now](https://www.youtube.com/watch?v=YNTpOLbvKTs)**

Get $50 in free credits with AssemblyAI https://www.assembly.ai/mo (no credit card required) The Federal Reserve decided AI was ...

📺 Mo Bitar

👁️ 97K • 👍 4K • 💬 652 • ⏱️ 12:23 • 7h ago

---

**[&#39;We&#39;re seeing in real time the effects that AI is going to have on cybersecurity&#39;, expert says](https://www.youtube.com/watch?v=x70CiWBG_Ps)**

FRANCE 24's Monte Francis speaks with Dr. R. David Edelman, Senior Fellow at the Brookings Institution, also former Director for ...

📺 FRANCE 24 English

👁️ 78K • 👍 243 • 💬 57 • ⏱️ 9:17 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 23,543 • ❤️ 4,550 • 19h ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 805,993 • ❤️ 818 • 13h ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 598 • 8d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 6,617 • ❤️ 596 • 3d ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 520 • 2d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 2,831 • ❤️ 970 • 1d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 8,608 • ❤️ 865 • 9d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 129,693 • ❤️ 426 • 1d ago

---

**[DepthPro2](https://huggingface.co/apple/DepthPro2)**

*Apple*

`depth-estimation`

⬇️ 0 • ❤️ 252 • 2d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,297,396 • ❤️ 20,857 • 15d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 12 • 💬 0 • ⭐ 5,792 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 33 • 💬 3 • ⭐ 444 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 150 • 💬 4 • ⭐ 1,237 • 9d ago

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

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 37 • 💬 9 • ⭐ 12,196 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

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

⭐ 20.1k • 🔱 1.2k • 7d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 12.1k • 🔱 1.8k • 3h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.6k • 🔱 2.2k • 1h ago

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

⭐ 6.8k • 🔱 539 • 2h ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.5k • 🔱 233 • 5h ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.4k • 🔱 796 • 13h ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 112 • 10h ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 4.9k • 🔱 616 • 2m ago

---

---

*Generated by PeekDeck - A glance is all you need*
