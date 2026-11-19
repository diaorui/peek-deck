---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-19T16:22:27.525078+00:00'
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

**Last Updated:** November 19, 2026 at 16:22 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 2d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 2d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

2d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

2d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 3d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

2d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

2d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

3d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

2d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 2d ago

---

---

## Google News: "ai"

**[Anthropic Sells $81.3 Billion in Shares for a Record IPO](https://www.nytimes.com/2026/11/18/technology/anthropic-ipo-pricing.html)**

The New York Times • 23h ago

---

**[‘Just Ridiculous’: A Famed Philosopher Takes on AI Consciousness](https://www.wired.com/story/just-ridiculous-a-famed-philosopher-takes-on-ai-consciousness/)**

Thomas Nagel has done landmark work on consciousness in nonhumans; this week, he won the million-dollar Berggruen Prize for his contributions to the field. And he has a lot of thoughts on AI.

WIRED • 1d ago

---

**[Introducing Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)**

Today, we’re introducing Gemini 4 Neon

blog.google • 18h ago

---

**[Visa Is Building Agentic Commerce. But Will Amazon Let AI Agents Shop?](https://www.forbes.com/sites/johnkoetsier/2026/11/19/visa-is-building-agentic-commerce-but-will-amazon-let-ai-agents-shop/)**

Forbes • 39m ago

---

**[‘Anyone forecasting 2027 is forecasting data centers’: The Fed is about to hike into an AI boom it can’t cool, and Main Street gets the bill](https://fortune.com/2026/11/19/fed-minutes-ai-inflation-data-centers-midterms-2027-rate-hike/)**

Voters rejected data centers, giving the Fed a problem: "AI is the number one source of growth for the U.S. economy."

Fortune • 38m ago

---

**[Four Maryland high school students sue after AI mistakes Doritos bag for gun](https://www.theguardian.com/us-news/2026/nov/18/maryland-baltimore-county-doritos-gun-ai-lawsuit)**

Football players say they are ‘traumatized’ after being handcuffed and detained by police while waiting for rides home

The Guardian • 16h ago

---

**[Opinion | Look where the world’s most elite AI talent is going](https://www.washingtonpost.com/opinions/interactive/2026/11/18/us-needs-keep-door-open-chinese-ai-talent/)**

China has a deep bench. Can America still beat it?

The Washington Post • 19h ago

---

**[AI is swallowing maths. Is economics next?](https://www.economist.com/finance-and-economics/2026/11/19/ai-is-swallowing-maths-is-economics-next)**

The Economist • 6h ago

---

**[Can AI Really Engineer Its Way to Superintelligence?](https://spectrum.ieee.org/ai-superintelligence-debate)**

Yet trying for it may still be disastrous

IEEE Spectrum • 1d ago

---

**[Microsoft CEO Satya Nadella explains why he asked 60K employees to quit](https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/)**

Microsoft CEO Satya Nadella explained why he offered buyouts to 60,000 of his employees in October, essentially urging them to voluntarily quit, rather than reducing the workforce via another massive layoff. The short answer is AI, but not in the way you might expect.

TechCrunch • 15h ago

---

---

## HackerNews: "ai"

**[AI is killing All About Berlin](https://news.ycombinator.com/item?id=50542705)**

They used my work to train their AI, and now they're using their AI to put me out of work.

⬆️ 798 • 💬 706 • 1d ago • [nicolasbouliane.com](https://nicolasbouliane.com/blog/death-by-ai)

---

**[Google's AI answers reducing search traffic by 40%](https://news.ycombinator.com/item?id=50540178)**

Google's AI answers are taking clicks from websites in the search results. In a randomized experiment, researchers hid AI Overviews from some US desktop users. Comparing them with users who still saw Overviews shows that an Overview cuts clicks to outside websites by about 40%. Those Overviews now appear on more than half the US keywords DataForSEO tracks, up from 6% two years ago. The industry's answer, GEO (generative engine optimization), has yet to show a way to compensate for the loss. While AI citations correlate with the same kind of link profile that goes with higher Google rankings, in March AI assistants sent websites just 0.3% of their traffic.

⬆️ 707 • 💬 559 • 1d ago • [revscope.co](https://revscope.co/blog/search-seo-geo-2026/)

---

**[AI agents ask better questions than KPMG accountants in audit trial](https://news.ycombinator.com/item?id=50547777)**

LONDON, November 18, 2026 — Artificial intelligence has taken another significant step into the world of professional services after KPMG revealed that AI

⬆️ 477 • 💬 237 • 1d ago • [European Business Magazine](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

---

**[Harvard researchers find AI coding agents shifted the bottleneck to code review](https://news.ycombinator.com/item?id=50538303)**

Harvard study: AI coding agents raised code output 30 percent; finished work did not measurably rise, and getting code through review took 49 percent longer.

⬆️ 322 • 💬 452 • 1d ago • [ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)

---

**[United Airlines experiencing a widespread system outage, airline says](https://news.ycombinator.com/item?id=50524165)**

A widespread, yet short-lived, system outage at United Airlines on Monday delayed some outbound flights at US airports, the airline told CNN in a statement, coming on the heels of a rare FAA ground stop that caused massive disruption.

⬆️ 257 • 💬 135 • 2d ago • [CNN](https://www.cnn.com/2026/11/16/us/united-airlines-outage)

---

**[Baidu, Xiaomi CEOs warn of growing gap between AI hype and returns](https://news.ycombinator.com/item?id=50531751)**

⬆️ 191 • 💬 258 • 2d ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3374774/baidu-xiaomi-ceos-warn-growing-gap-between-ai-hype-and-returns)

---

**["Anthropic Is Not a Safe AI Company" – Coalition Challenges Anthropic Safety](https://news.ycombinator.com/item?id=50548485)**

⬆️ 135 • 💬 77 • 23h ago • [businesswire.com](https://www.businesswire.com/news/home/20261118974464/en/Anthropic-is-Not-a-Safe-AI-Company---Broad-Coalition-of-Scientists-Legal-Scholars-and-Tech-Leaders-Challenge-Anthropics-Safety-Branding-Ahead-of-IPO)

---

**[Black high school students sue after AI mistakes Doritos bag for gun](https://news.ycombinator.com/item?id=50554641)**

Case focuses on alleged failures surrounding AI systems and impact on students BALTIMORE COUNTY, MD – Today, the Lawyers’ Committee for Civil Rights Under Law filed a lawsuit on behalf of four Black current and former students against Omnilert, LLC, Baltimore County Public Schools (BCPS) and personnel, the Baltimore County Police Department, and individual officers […]

⬆️ 107 • 💬 79 • 15h ago • [Lawyers' Committee for Civil Rights Under Law](https://www.lawyerscommittee.org/lawyers-committee-files-lawsuit-on-behalf-of-black-students-detained-and-searched-due-to-ai-alert-falsely-identifying-a-bag-of-chips-as-a-firearm/)

---

**[AI will not make you rich (2025)](https://news.ycombinator.com/item?id=50555093)**

The disruption is real. It's also predictable.

⬆️ 104 • 💬 66 • 14h ago • [Colossus](https://colossus.com/article/ai-will-not-make-you-rich/)

---

**[Ask HN: If AI tools are so good, why isn't your bug backlog empty?](https://news.ycombinator.com/item?id=50520076)**

⬆️ 103 • 💬 115 • 2d ago

---

---

## YouTube Videos: "ai"

**[Stanford&#39;s NCM Is Coming… and It Could Be Worse Than AI](https://www.youtube.com/watch?v=o8zuaPbbaGU)**

For the first time, bots sent more traffic to web pages than people did. Cloudflare's CEO put the split at 57.5% bots to 42.5% ...

📺 Ink Intelligence

👁️ 480K • 👍 6K • 💬 263 • ⏱️ 15:47 • 2d ago

---

**[OpenAI’s New AI Just Crossed the Self-Improvement Threshold…](https://www.youtube.com/watch?v=1oIzVB5Ues4)**

OpenAI says GPT-6.2 Astra is its first publicly released model to hit “High” in AI self-improvement. I break down what Astra actually ...

📺 AI Copium

👁️ 45K • 👍 376 • 💬 102 • ⏱️ 9:22 • 1d ago

---

**[Are AI threats the reason we&#39;re being told to stockpile?](https://www.youtube.com/watch?v=r1urlnOh5gA)**

We're told to stockpile to survive 72 hours in an emergency. But why do we need to stock up and what exactly are we preparing for ...

📺 ITV News

👁️ 324K • 👍 870 • 💬 401 • ⏱️ 8:31 • 1d ago

---

**[Superhuman AI Is Coming Next Year](https://www.youtube.com/watch?v=IO6-9l56jSg)**

At one leading A.I. lab, nine out of ten changes to its code are now written by its own A.I. Some insiders forecast superhuman A.I. ...

📺 The Good Takeoff

👁️ 18K • 👍 215 • 💬 40 • ⏱️ 11:05 • 1d ago

---

**[FBI warns hackers are allegedly using AI to target businesses](https://www.youtube.com/watch?v=JHcQWzkAhbc)**

Fox News justice correspondent David Spunt and tech journalist Kurt Knutsson join 'America Reports' to examine the FBI's ...

📺 Fox News

👁️ 139K • 👍 903 • 💬 576 • ⏱️ 8:13 • 1d ago

---

**[AI, Consciousness and the Future of Humanity | Mustafa Suleyman &amp; Yuval Noah Harari](https://www.youtube.com/watch?v=H43e72-2aAs)**

Everything will change with AI. But will we be any better at understanding ourselves? Microsoft AI CEO Mustafa Suleyman and ...

📺 Yuval Noah Harari 

👁️ 126K • 👍 3K • 💬 368 • ⏱️ 1:07:08 • 23h ago

---

**[John Lennox on How AI Could Take Over the World (and Where It&#39;s Already Happening)](https://www.youtube.com/watch?v=-Pmst8bkRaE)**

Watch the full interview with Professor Lennox https://youtu.be/KIo9qL2LD90 Subscribe to Socrates in the City ...

📺 Socrates in the City

👁️ 136K • 💬 335 • ⏱️ 21:58 • 1d ago

---

**[I Tested AI Slop In Real Life](https://www.youtube.com/watch?v=aMdqOvT_AJw)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha.

📺 Sambucha

👁️ 115K • 👍 6K • 💬 151 • ⏱️ 0:59 • 22h ago

---

**[Autonomous AI Attacks Are Here &amp; America Doesn’t Want to Admit It](https://www.youtube.com/watch?v=gLEcm15gbSM)**

The FBI and Google both revealed that autonomous AI attacks are a real thing and it's not going to get better. But officially, other ...

📺 DeFranco News Clips

👁️ 1.0M • 👍 50K • 💬 2K • ⏱️ 1:04 • 1d ago

---

**[AI Mistakes Chips for Gun, Black Students Sue; Louise Lucas Fights DOJ, Cancer Alley at Risk](https://www.youtube.com/watch?v=iwSON7TgAa8)**

11.17.2026 #RolandMartinUnfiltered: AI Mistakes Chips for Gun, Black Students Sue; Louise Lucas Fights DOJ, Cancer Alley at ...

📺 Roland S. Martin

👁️ 30K • 👍 2K • 💬 30 • ⏱️ 2:06:12 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 6,266 • ❤️ 2,748 • 6d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 2,053 • ❤️ 304 • 4h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,647,301 • ❤️ 20,631 • 12d ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 274 • 1d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 1,320 • ❤️ 680 • 8h ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 821,710 • ❤️ 1,616 • 3d ago

---

**[tiny-voca](https://huggingface.co/n4ze3m/tiny-voca)**

*Muhammed Nazeem *

`text-to-speech`

⬇️ 6,368 • ❤️ 316 • 1d ago

---

**[LongCat-Video-Avatar-1.6](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6)**

*LongCat*

⬇️ 1,923 • ❤️ 306 • 6d ago

---

**[Maxwell-V1-Flash](https://huggingface.co/maxwell-model/Maxwell-V1-Flash)**

*maxwell-model*

`text-generation` `36.8B`

⬇️ 1,703 • ❤️ 263 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,934,937 • ❤️ 12,696 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 9 • 💬 0 • ⭐ 4,521 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 20 • 💬 2 • ⭐ 7,686 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 16 • 💬 2 • ⭐ 230 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 35 • 💬 9 • ⭐ 12,041 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 136 • 💬 4 • ⭐ 734 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 19 • 💬 0 • ⭐ 42,152 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,115 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 24,412 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 78 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 87 • 💬 7 • ⭐ 93,818 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 18.6k • 🔱 1.1k • 4d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 11.0k • 🔱 1.6k • 2h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.2k • 🔱 2.1k • 2h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.4k • 🔱 726 • 14h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.3k • 🔱 1.9k • 1d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.2k • 🔱 774 • 9h ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.1k • 🔱 209 • 25m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.8k • 🔱 110 • 1d ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.7k • 🔱 131 • 12m ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 3.9k • 🔱 359 • 7m ago

---

---

*Generated by PeekDeck - A glance is all you need*
