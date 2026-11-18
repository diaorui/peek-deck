---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-18T01:09:56.443772+00:00'
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

**Last Updated:** November 18, 2026 at 01:09 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 19h ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 1d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

21h ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

1d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 1d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

17h ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

21h ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

1d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

22h ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 16h ago

---

---

## Google News: "ai"

**[A.I. Helps Find Major Security Bug in Java, a Software Platform Vital to the Internet](https://www.nytimes.com/2026/11/17/us/politics/ai-security-bug-java.html)**

The New York Times • 1h ago

---

**[Why the internet suddenly broke all at once](https://www.axios.com/2026/11/17/tech-outages-ai-fears-internet-breaking)**

Axios • 3h ago

---

**[A top open-source AI advocate is starting to gate cyber capabilities](https://www.axios.com/2026/11/17/reflection-cybersecurity-gated-access-tools)**

Axios • 1h ago

---

**[Google: ‘The era of autonomous attacks has arrived’](https://thehill.com/policy/technology/6224604-autonomous-ai-threats-google-report/)**

The Hill • 9h ago

---

**[Nikkei Rises 1.0%, Led by Chip, AI Stocks](https://www.wsj.com/finance/stocks/nikkei-rises-1-0-led-by-chip-ai-stocks-b486ab61)**

WSJ • 35m ago

---

**[LeBron James sues makers of AI sports-betting app, saying they used his likeness and nickname](https://www.wlwt.com/article/lebron-james-ai-betting-app-lawsuit/74458892)**

NBA superstar LeBron James has sued the makers of an AI sports-betting app, saying they deliberately violated his publicity rights and trademarks by calling it “Bron” and using artificially generated images of him in their marketing.

WLWT • 4m ago

---

**[Cambridge Dictionary chooses 'human' as word of the year in response to AI fears](https://www.click2houston.com/news/world/2026/11/18/cambridge-dictionary-chooses-human-as-word-of-the-year-in-response-to-ai-fears/)**

The Cambridge Dictionary has chosen "human" as its word of the year, reflecting concerns about artificial intelligence.

Click2Houston • 26m ago

---

**[Investor Steve Eisman says the AI neocloud stocks are in 'big trouble' from Nvidia fallout](https://www.cnbc.com/2026/11/17/big-short-investor-steve-eisman-to-discuss-nvidia-anthropic-and-ai-bull-on-cnbc.html)**

Steve Eisman is appearing on "Squawk Box" on Tuesday.

CNBC • 12h ago

---

**[Are all of these outages a coincidence — or a glimpse of our AI future?](https://tech.yahoo.com/general/article/are-all-of-these-outages-a-coincidence--or-a-glimpse-of-our-ai-future-210035788.html)**

First Microsoft. Then the FAA. Now the banks, and the NSA, and Apple iCloud. Our systems are failing, seemingly all at once, while big tech continues to hype up AI.

Yahoo Tech • 4h ago

---

**[Grok Bot took unapproved actions, ignored orders to stop, and then denied it](https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it/)**

AI agent takes unapproved actions even when laptop lid is closed and told not to.

Ars Technica • 11h ago

---

---

## HackerNews: "ai"

**[All AI-generated code should be Open Source](https://news.ycombinator.com/item?id=50507303)**

All code generated with help from AI should be Open Source or on Creative Commons Zero (CC0) license.

⬆️ 1279 • 💬 669 • 2d ago • [Jakub T. Jankiewicz Blog](https://jakub.jankiewicz.org/blog/ai-code-open-source/)

---

**[United Airlines experiencing a widespread system outage, airline says](https://news.ycombinator.com/item?id=50524165)**

A widespread, yet short-lived, system outage at United Airlines on Monday delayed some outbound flights at US airports, the airline told CNN in a statement, coming on the heels of a rare FAA ground stop that caused massive disruption.

⬆️ 255 • 💬 132 • 1d ago • [CNN](https://www.cnn.com/2026/11/16/us/united-airlines-outage)

---

**[Baidu, Xiaomi CEOs warn of growing gap between AI hype and returns](https://news.ycombinator.com/item?id=50531751)**

⬆️ 185 • 💬 239 • 10h ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3374774/baidu-xiaomi-ceos-warn-growing-gap-between-ai-hype-and-returns)

---

**["Who is Hiring?" postings stuck near 12-year lows as AI reaches half of all jobs](https://news.ycombinator.com/item?id=50512950)**

Hacker News "Who is Hiring?" job postings sit near 12-year lows while AI appears in more than half of all postings. Most popular programming languages and technologies for November 2026.

⬆️ 94 • 💬 86 • 1d ago • [Hacker News Hiring Trends](https://www.hntrends.com/2026/november.html)

---

**[The Single Router in Southern Arkansas That Ground Air Travel to a Halt](https://news.ycombinator.com/item?id=50503588)**

⬆️ 89 • 💬 60 • 2d ago • [wsj.com](https://www.wsj.com/business/airlines/the-single-router-in-southern-arkansas-that-ground-air-travel-to-a-halt-eedc326c)

---

**[Ask HN: If AI tools are so good, why isn't your bug backlog empty?](https://news.ycombinator.com/item?id=50520076)**

⬆️ 87 • 💬 107 • 1d ago

---

**[Parents pay $75k for Alpha's AI school. Half of its students missed math target](https://news.ycombinator.com/item?id=50509953)**

Only 42% of Alpha students hit its 2x learning goal in math and reading, internal data show, as 2,600 public school students now use its software.

⬆️ 69 • 💬 67 • 2d ago • [Fortune](https://fortune.com/2026/11/14/alpha-school-ai-students-tuition-learning-goals/)

---

**[Caltech professor no longer grades homework's because everyone uses AI](https://news.ycombinator.com/item?id=50523022)**

I attended an introductory math class at Caltech, an elite STEM university in Pasadena, where the professor no longer grades homework.

⬆️ 49 • 💬 60 • 1d ago • [Business Insider](https://www.businessinsider.com/ai-math-class-university-homework-caltech-careers-2026-11)

---

**[FBI says Artex AI open-source hacking tool used to breach networks](https://news.ycombinator.com/item?id=50520796)**

The FBI says that the open source hacking tool was used in cyberattacks targeting a U.S. IT giant and the South Korean financial industry.

⬆️ 49 • 💬 14 • 1d ago • [TechCrunch](https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/)

---

**[United Airlines has a widespread system outage](https://news.ycombinator.com/item?id=50524260)**

⬆️ 48 • 💬 13 • 1d ago • [apnews.com](https://apnews.com/article/united-airlines-outage-5a5e5f75bb07f11ffb8750901f0076ff)

---

---

## YouTube Videos: "ai"

**[California SUES OpenAI after hundreds of AI agents go ROGUE](https://www.youtube.com/watch?v=hMsMkBQRFmo)**

Fox News senior correspondent Claudia Cowan reports on California's lawsuit against OpenAI after hundreds of autonomous AI ...

📺 Fox News Clips

👁️ 71K • 👍 475 • 💬 317 • ⏱️ 2:09 • 4h ago

---

**[These AI videos are crucifying MAGA and it&#39;s amazing...](https://www.youtube.com/watch?v=M8Vxq1bcJ-o)**

We are reacting to the latest AI videos roasting MAGA content. See how satirical clips are changing the political narrative.

📺 Really American

👁️ 109K • 👍 3K • 💬 135 • ⏱️ 14:35 • 7h ago

---

**[AI Just Reached A Tipping Point](https://www.youtube.com/watch?v=6LmezY6_kGY)**

Subscribe To My Newsletter - https://aigrid.beehiiv.com/subscribe Get your Free AGI Preparedness Guide ...

📺 TheAIGRID

👁️ 111K • 👍 2K • 💬 267 • ⏱️ 30:24 • 1d ago

---

**[Stanford&#39;s NCM Is Coming… and It Could Be Worse Than AI](https://www.youtube.com/watch?v=o8zuaPbbaGU)**

For the first time, bots sent more traffic to web pages than people did. Cloudflare's CEO put the split at 57.5% bots to 42.5% ...

📺 Ink Intelligence

👁️ 184K • 👍 2K • 💬 130 • ⏱️ 15:47 • 1d ago

---

**[Did AI Agents Just Pull Off the Biggest Attack Ever: US Aviation Chaos](https://www.youtube.com/watch?v=iiepBMjZIMY)**

Did AI agents just cause America's biggest aviation shutdown since 9/11? Three days after a new AI system goes live across US ...

📺 AI Revolution

👁️ 27K • 👍 622 • 💬 89 • ⏱️ 13:27 • 2d ago

---

**[Tech CEO: ‘Most people don’t want AI’ | Jon Von Tetzchner](https://www.youtube.com/watch?v=XDsNVIUQWiw)**

Most people don't want AI, they don't want to see it.” Co-founder of Vivaldi Jon Von Tetzchner joins The Tech Report's Isaac ...

📺 The Tech Report

👁️ 85K • 👍 2K • 💬 408 • ⏱️ 33:40 • 5h ago

---

**[Elon Musk Warns of Trouble for AI Data Centers](https://www.youtube.com/watch?v=iwndzdSNuWI)**

Elon Musk is sounding the alarm as financial institutions cut back on funding for AI companies. Cenk Uygur and Ana Kasparian ...

📺 The Young Turks

👁️ 149K • 👍 1K • 💬 284 • ⏱️ 6:50 • 1d ago

---

**[Is AI Going To DESTROY The Internet](https://www.youtube.com/watch?v=xyQfFSTTjA0)**

Subscribe to our Newsletter https://financebureau.com/ ~~~~~ AI is exposing security holes in the internet faster than humans ...

📺 Finance Bureau

👁️ 22K • 👍 336 • 💬 46 • ⏱️ 16:37 • 9h ago

---

**[Elon Musk joins Trump as US-China AI battle HEATS UP](https://www.youtube.com/watch?v=VV3IhP5rNgE)**

Fox News senior correspondent Benjamin Hall discusses President Donald Trump's Asia trip, a possible meeting with Kim Jong ...

📺 Fox News

👁️ 179K • 👍 1K • 💬 689 • ⏱️ 4:08 • 10h ago

---

**[AI Will Take Your Job by 2027 | Former Google X Executive](https://www.youtube.com/watch?v=mDeGvJnpP8s)**

Bring your ideas to life with Higgsfield. Explore here: https://higgsfield.ai/s/solominpodcast-QLwmoZ ▶︎Join my community on ...

📺 Solomin Podcast 

👁️ 125K • 👍 1K • 💬 240 • ⏱️ 1:30:20 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 727,110 • ❤️ 1,460 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,942,530 • ❤️ 20,432 • 10d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 4,445 • ❤️ 506 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,828,071 • ❤️ 12,404 • 1mo ago

---

**[Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)**

*Thinking Machines Lab*

`image-text-to-text` `594.1B`

⬇️ 18,359 • ❤️ 442 • 6h ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

`27.3B`

⬇️ 6,827,598 • ❤️ 6,138 • 5d ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 2,660,341 • ❤️ 519 • 6d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

`image-to-image`

⬇️ 1,062,051 • ❤️ 3,405 • 15d ago

---

**[Qwen-Image-2.1-Uncensored-Omni-Quantized](https://huggingface.co/chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized)**

*Chatr Labs*

`text-to-image` `7.1B`

⬇️ 160,748 • ❤️ 500 • 3d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,759,757 • ❤️ 3,291 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 7 • 💬 0 • ⭐ 2,616 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 17 • 💬 2 • ⭐ 7,452 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 33 • 💬 9 • ⭐ 11,981 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 119 • 💬 4 • ⭐ 492 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 122,955 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 71 • 💬 4 • ⭐ 24,259 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**

*Thomas Wolf, Lysandre Debut, Victor Sanh et al. (22 authors)*

🏢 Hugging Face

Transformers library provides state-of-the-art Transformer architectures and pretrained models for natural language processing tasks with a unified API and emphasis on extensibility and robust deployment.

▲ 34 • 💬 7 • ⭐ 169,330 • 86mo ago

[🎓 arXiv](https://arxiv.org/abs/1910.03771) • [💻 code](https://github.com/huggingface/transformers) • [🔗 project](https://huggingface.co)

---

**[PyTorch Distributed: Experiences on Accelerating Data Parallel Training](https://huggingface.co/papers/2006.15704)**

*Shen Li, Yanli Zhao, Rohan Varma et al. (11 authors)*

The PyTorch distributed data parallel module optimizes large-scale model training using techniques like gradient bucketing, computation-communication overlap, and selective synchronization to achieve near-linear scalability.

▲ 15 • 💬 0 • ⭐ 105,809 • 77mo ago

[🎓 arXiv](https://arxiv.org/abs/2006.15704) • [💻 code](https://github.com/pytorch/pytorch)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 78 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 105 • 💬 2 • ⭐ 759 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 17.8k • 🔱 1.0k • 3d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 10.3k • 🔱 1.5k • 1h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.0k • 🔱 2.0k • 6h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.3k • 🔱 715 • 7h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.2k • 🔱 1.8k • 13d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.1k • 🔱 753 • 7h ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 5.6k • 🔱 183 • 1h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.6k • 🔱 122 • 5m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.4k • 🔱 109 • 1d ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.6k • 🔱 242 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
