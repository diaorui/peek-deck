---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-21T17:53:33.742862+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 21, 2026 at 17:53 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 4d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 4d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

4d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

4d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 5d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

4d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

4d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

5d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

4d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 4d ago

---

---

## Google News: "ai"

**[Anthropic engineer's warning about Claude Code explains why tech outages could get much worse](https://finance.yahoo.com/technology/article/anthropic-engineers-warning-about-claude-code-explains-why-tech-outages-could-get-much-worse-110000573.html)**

AI can write code faster than we can review it, which is a great benefit and a huge risk.

Yahoo Finance • 6h ago

---

**[My A.I. Hack Emergency Plan](https://www.nytimes.com/2026/11/21/business/ai-emergency-plan.html)**

The New York Times • 7h ago

---

**[Tech Outages Are Only the Beginning. A.I. Will Bring More Disruptions.](https://www.nytimes.com/2026/11/21/us/politics/tech-outages-ai-disruptions.html)**

The New York Times • 12m ago

---

**[Analysis | Entitled and out of touch, AI CEOs are heading for a fall](https://www.washingtonpost.com/business/2026/11/21/history-lesson-ai-ceos-alienate-americans-your-own-peril/)**

Americans tend to turn against out-of-touch CEOs, and a public reckoning on the tech industry could already be underway.

The Washington Post • 20m ago

---

**["Psychologically, it is a mountain to climb." How AI fixes the fear of fundraising.](https://www.axios.com/2026/11/21/tim-cadogan-gofundme-ai-strategy)**

Axios • 33m ago

---

**[Here are the top AI agents that can live in your text messages](https://techcrunch.com/2026/11/21/all-the-ai-agents-that-can-live-in-your-text-messages/)**

We created a list of the most notable AI agents that can live in your text messages, from general assistants to agents designed for families, travel, and work.

TechCrunch • 53m ago

---

**['This seems like an extreme privacy violation.' Surprising messages from the Muse AI agent are unnerving Meta's own employees, report says](https://fortune.com/2026/11/21/meta-employees-muse-ai-agent-extreme-privacy-violation-encrypted-signal-messages/)**

In one example, a Meta staffer reported that Muse sent her a reminder on her personal phone to respond to a message from her sister on the encrypted messaging service Signal.

Fortune • 25m ago

---

**[U.S. stocks slump into correction territory amid tech and AI worries](https://www.washingtonpost.com/business/2026/11/20/us-stock-market-slumps-amid-rising-tech-ai-worries/)**

Markets on Friday posted their worst week since worries about President Donald Trump’s tariffs caused a global sell-off in April 2025.

The Washington Post • 11h ago

---

**[From trash to treasure: Most hated stocks are winning as AI bull market rolls over](https://www.cnbc.com/2026/11/21/from-trash-to-treasure-these-hated-stocks-are-winning-as-ai-flounders.html)**

Several stocks that are unpopular on Wall Street, including Clorox, Boston Beer and Campbell's, are poised to be winners as the AI trade loses steam.

CNBC • 4h ago

---

**[Your 401(k) is full of AI. How to deal with the volatility](https://www.cnn.com/2026/11/21/business/ai-stocks-volatility-investing)**

Indices like the S&P 500 have become heavily concentrated in tech stocks in recent years, due to to the AI boom.

CNN • 6h ago

---

---

## HackerNews: "ai"

**[Frostbite: A new CPU architecture discovered, designed and verified by AI](https://news.ycombinator.com/item?id=50572503)**

Frostbite is a general-purpose CPU built around interaction nets, discovered, designed, and verified end-to-end by our AI systems, reaching 4.59x the performance-per-watt of a modern superscalar (dual-issue, in-order) CPU core.

⬆️ 662 • 💬 349 • 1d ago • [Architect Labs](https://architectlabs.com/blog/frostbite)

---

**[Fuck Your AI Safeguards](https://news.ycombinator.com/item?id=50562262)**

You can't tell me that you found a security issue in my product and then refuse to fix it.

⬆️ 614 • 💬 249 • 2d ago • [./techtipsy](https://ounapuu.ee/posts/2026/11/19/unsafeguards/)

---

**[Restricting AI agents in mobile operating systems platforms from capturing data](https://news.ycombinator.com/item?id=50572348)**

Privacy is our mission; it’s why we exist, and we do everything we can to protect it. This means that we are restricting the latest AI agents built into mobile operating systems from potentially capturing and storing your Signal data.

⬆️ 562 • 💬 331 • 1d ago • [Signal Messenger](https://signal.org/blog/protecting-your-privacy/)

---

**[Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day](https://news.ycombinator.com/item?id=50574383)**

Asian markets record worst week since 2020 as investors question huge sums being poured into AI buildout

⬆️ 444 • 💬 785 • 1d ago • [the Guardian](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

---

**[Google workers tell their employer not to punish schools that don't want AI](https://news.ycombinator.com/item?id=50577901)**

Executives are “convinced that resistance to AI" just means schools "don’t see the vision,” a Google staffer said.

⬆️ 278 • 💬 222 • 1d ago • [Mother Jones](https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/)

---

**[Pete Warden on local AI, open models, voice interfaces, the future of hardware](https://news.ycombinator.com/item?id=50561508)**

⬆️ 270 • 💬 248 • 2d ago • [thedataexchange.media](https://thedataexchange.media/pete-warden-moonshine/)

---

**[AI isn't replacing your job. It's turning it into low-paid gig work](https://news.ycombinator.com/item?id=50562500)**

⬆️ 147 • 💬 82 • 2d ago • [restofworld.org](https://restofworld.org/2026/ai-jobs-skills-gig-work/)

---

**[Chrome AI features wasting much bandwidth](https://news.ycombinator.com/item?id=50562636)**

🔎 Finally solved the mystery. At some point this year (around a few months ago), my bandwidth/data usage went thru the roof. Figured out it was Chrome's...

⬆️ 133 • 💬 51 • 2d ago • [perishablepress.com](https://perishablepress.com/chrome-ai-wasting-much-bandwidth/)

---

**[ClawDOS – An AI coding agent for DOS](https://news.ycombinator.com/item?id=50586292)**

An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz)

⬆️ 132 • 💬 42 • 12h ago • [ClawDOS](http://ricapar.net/ClawDOS/)

---

**[Black high school students sue after AI mistakes Doritos bag for gun](https://news.ycombinator.com/item?id=50554641)**

Case focuses on alleged failures surrounding AI systems and impact on students BALTIMORE COUNTY, MD – Today, the Lawyers’ Committee for Civil Rights Under Law filed a lawsuit on behalf of four Black current and former students against Omnilert, LLC, Baltimore County Public Schools (BCPS) and personnel, the Baltimore County Police Department, and individual officers […]

⬆️ 119 • 💬 92 • 2d ago • [Lawyers' Committee for Civil Rights Under Law](https://www.lawyerscommittee.org/lawyers-committee-files-lawsuit-on-behalf-of-black-students-detained-and-searched-due-to-ai-alert-falsely-identifying-a-bag-of-chips-as-a-firearm/)

---

---

## YouTube Videos: "ai"

**[AI Genius Predicts the Exact Month Superintelligence Arrives](https://www.youtube.com/watch?v=rOXnBQrxGqs)**

Ryan Christian of Vals.ai and Joe Lonsdale discuss the Vals RSI index, which projects Anthropic reaching full recursive ...

📺 Joe Lonsdale

👁️ 20K • 👍 245 • 💬 43 • ⏱️ 7:00 • 1d ago

---

**[AI Insiders Risk Everything to Reveal What Happens to Us in 90 Days](https://www.youtube.com/watch?v=Ettph184FS8)**

Thirty-three messages reached a mailbox on the open internet, and no person wrote a single one of them. Researchers hid one ...

📺 Spacialize

👁️ 23K • 👍 209 • 💬 24 • ⏱️ 12:49 • 20h ago

---

**[AI News: This Is The Make or Break Week!!](https://www.youtube.com/watch?v=wqNIzUmNt9M)**

Hire your own team of agents with Hyperagent for free here: ...

📺 Matt Wolfe

👁️ 89K • 👍 1K • 💬 128 • ⏱️ 33:01 • 22h ago

---

**[Is the AI Trade Headed for a Dot-Com Crash? Dan Niles Weighs In](https://www.youtube.com/watch?v=RT1x8q8ma7I)**

Tech stocks got crushed as the AI trade unraveled, and Dan Niles of Niles Investment Management tells Deirdre Bosa whether ...

📺 Yahoo Finance

👁️ 273K • 👍 2K • 💬 484 • ⏱️ 14:33 • 17h ago

---

**[MARKET FALLS, ANTHROPIC DOWN, AI BUBBLE POP?](https://www.youtube.com/watch?v=P0R2K4-6Wgo)**

The Friday crew is joined by Gary Marcus to breakdown the AI market tumbling. Gary Marcus: https://x.com/GaryMarcus ...

📺 Breaking Points

👁️ 446K • 👍 6K • 💬 1K • ⏱️ 22:12 • 22h ago

---

**[AI Just Made Itself Smarter By Changing Its Own Weights!  #ai #research #tech](https://www.youtube.com/watch?v=VyzoltTI_NA)**

Source: https://arxiv.org/abs/2611.21885.

📺 Better Stack

👁️ 72K • 👍 4K • 💬 220 • ⏱️ 3:00 • 13h ago

---

**[3 AI Video Generators for 100% FREE &amp; UNLIMITED Videos](https://www.youtube.com/watch?v=6_Z5cX1iwug)**

Turn your clips into cinematic 4K scenes with Higgsfield → https://higgsfield.ai/s/malvaai-NdigAx Free Prompt PDFs + AI ...

📺 Malva AI

👁️ 2K • 👍 82 • 💬 14 • ⏱️ 9:46 • 3h ago

---

**[OpenAI Just Revealed How Far AI Self-Improvement Has Gone…](https://www.youtube.com/watch?v=s0ZfyXYp3Ns)**

Try Cardboard, today's sponsor: ...

📺 AI Copium

👁️ 25K • 👍 231 • 💬 58 • ⏱️ 12:57 • 1d ago

---

**[How an AI Makes Images From Pure Static: The Diffusion Model](https://www.youtube.com/watch?v=dOJYDPabyUk)**

There is no cat in the static an AI starts from, so how does it know which static to wipe away to make one? Change one word of the ...

📺 Ordinary Machines

👁️ 3K • ⏱️ 0:54 • 8h ago

---

**[Anthropic Slides as AI Selloff Deepens](https://www.youtube.com/watch?v=euXj_4vMSo8)**

Bloomberg's Ed Ludlow takes a look at Anthropic shares falling after its blockbuster stock market debut, as part of a wider global ...

📺 Bloomberg Tech

👁️ 14K • 👍 124 • 💬 23 • ⏱️ 44:06 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 7,944 • ❤️ 1,744 • 18h ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 238,152 • ❤️ 502 • 9h ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 5,588 • ❤️ 510 • 2d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 3,000,544 • ❤️ 12,896 • 1mo ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 473 • 7d ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 465 • 1d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 2,383 • ❤️ 911 • 13h ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 8,120 • ❤️ 819 • 8d ago

---

**[LongCat-Video-Avatar-1.6](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6)**

*LongCat*

⬇️ 3,031 • ❤️ 359 • 8d ago

---

**[tiny-voca](https://huggingface.co/n4ze3m/tiny-voca)**

*Muhammed Nazeem *

`text-to-speech`

⬇️ 9,323 • ❤️ 348 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 11 • 💬 0 • ⭐ 5,499 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 29 • 💬 2 • ⭐ 284 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 146 • 💬 4 • ⭐ 1,152 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 7,850 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 18 • 💬 2 • ⭐ 391 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,332 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 37 • 💬 9 • ⭐ 12,160 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 22 • 💬 0 • ⭐ 42,358 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 24,603 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

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

⭐ 19.7k • 🔱 1.2k • 6d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 11.7k • 🔱 1.7k • 2h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.4k • 🔱 2.1k • 2h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.6k • 🔱 751 • 2h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.7k • 🔱 2.0k • 3d ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.4k • 🔱 222 • 45m ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 6.4k • 🔱 500 • 39m ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.4k • 🔱 789 • 6h ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 113 • 1d ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.9k • 🔱 139 • 2m ago

---

---

*Generated by PeekDeck - A glance is all you need*
