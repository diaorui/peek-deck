---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-19T06:48:55.107974+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 19, 2026 at 06:48 UTC  
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

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 2d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

1d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

2d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

2d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

2d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 1d ago

---

---

## Google News: "ai"

**[Top Dem senator says AI is contributing to outages as Rubio says incidents not connected](https://www.foxnews.com/live-news/tech-outages-us-airlines-faa-microsoft-banks-november-18)**

Sen. Mark Warner, D-Va., suggested on Tuesday that artificial intelligence is behind a series of outages across U.S. industries this week, but Secretary of State Marco Rubio insists there is "no evidence" the incidents are connected.

Fox News • 3h ago

---

**[Hacks, AI or just overdue updates - why have there been so many outages?](https://www.bbc.com/news/articles/c6z0kly2lll7o)**

There is no evidence these are linked, but the constant series of tech disruptions can be unnerving.

BBC • 17h ago

---

**[Tech outages are piling up, and AI is raising the stakes. Could this be the new normal?](https://www.seattletimes.com/business/tech-outages-are-piling-up-and-ai-is-raising-the-stakes-could-this-be-the-new-normal/)**

The Seattle Times • 1h ago

---

**[Anthropic IPO raises over $81 billion in largest offering on record, topping SpaceX](https://www.cnbc.com/2026/11/18/anthropic-ipo-ai-offering-price.html)**

Anthropic stock is set to begin trading on the Nasdaq under the ticker symbol ANT on Thursday.

CNBC • 15h ago

---

**[Four Maryland high school students sue after AI mistakes Doritos bag for gun](https://www.theguardian.com/us-news/2026/nov/18/maryland-baltimore-county-doritos-gun-ai-lawsuit)**

Football players say they are ‘traumatized’ after being handcuffed and detained by police while waiting for rides home

The Guardian • 6h ago

---

**[Baltimore students sue over AI that allegedly mistook Doritos bag for gun](https://www.usatoday.com/story/news/nation/2026/11/19/baltimore-students-lawsuit-ai-gun-alert-chips/92855684007/)**

Four Baltimore students sued after an AI weapon detection system allegedly mistook a Doritos bag of chips for a firearm.

USA Today • 44m ago

---

**[A.I. Mistook a Bag of Chips for a Gun, Teenagers’ Lawsuit Says](https://www.nytimes.com/2026/11/17/us/baltimore-school-chips-gun-alert.html)**

The New York Times • 1d ago

---

**[Watch Inside Google's AI Race with Ruth Porat](https://www.bloomberg.com/news/videos/2026-11-19/alphabet-s-ruth-porat-on-the-ai-investment-frenzy-video)**

Bloomberg.com • 1h ago

---

**[Morgan Stanley sees AI IPO appetite building amid 'biggest capex cycle in our lifetimes'](https://www.cnbc.com/video/2026/11/19/morgan-stanleys-co-president-on-the-ai-industry-ipo-markets-can-handle.html)**

Morgan Stanley Co-President Dan Simkowitz discusses investor appetite for AI IPOs, the scale of the industry's investment cycle and the importance of financial discipline under Nvidia's new leadership. He also sees a strong outlook for global M&A, supported by abundant credit and a favorable regulatory environment.

CNBC • 1h ago

---

**[NYC, LA and Chicago School Districts Weigh Breaking Up With Google Search Over A.I.](https://www.nytimes.com/2026/11/18/technology/google-gemini-ai-search-schools-nyc-la-chicago.html)**

The New York Times • 12h ago

---

---

## HackerNews: "ai"

**[AI is killing All About Berlin](https://news.ycombinator.com/item?id=50542705)**

They used my work to train their AI, and now they're using their AI to put me out of work.

⬆️ 775 • 💬 691 • 1d ago • [nicolasbouliane.com](https://nicolasbouliane.com/blog/death-by-ai)

---

**[Google's AI answers reducing search traffic by 40%](https://news.ycombinator.com/item?id=50540178)**

Google's AI answers are taking clicks from websites in the search results. In a randomized experiment, researchers hid AI Overviews from some US desktop users. Comparing them with users who still saw Overviews shows that an Overview cuts clicks to outside websites by about 40%. Those Overviews now appear on more than half the US keywords DataForSEO tracks, up from 6% two years ago. The industry's answer, GEO (generative engine optimization), has yet to show a way to compensate for the loss. While AI citations correlate with the same kind of link profile that goes with higher Google rankings, in March AI assistants sent websites just 0.3% of their traffic.

⬆️ 696 • 💬 544 • 1d ago • [revscope.co](https://revscope.co/blog/search-seo-geo-2026/)

---

**[AI agents ask better questions than KPMG accountants in audit trial](https://news.ycombinator.com/item?id=50547777)**

LONDON, November 18, 2026 — Artificial intelligence has taken another significant step into the world of professional services after KPMG revealed that AI

⬆️ 438 • 💬 189 • 14h ago • [European Business Magazine](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

---

**[Harvard researchers find AI coding agents shifted the bottleneck to code review](https://news.ycombinator.com/item?id=50538303)**

Harvard study: AI coding agents raised code output 30 percent; finished work did not measurably rise, and getting code through review took 49 percent longer.

⬆️ 320 • 💬 441 • 1d ago • [ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)

---

**[United Airlines experiencing a widespread system outage, airline says](https://news.ycombinator.com/item?id=50524165)**

A widespread, yet short-lived, system outage at United Airlines on Monday delayed some outbound flights at US airports, the airline told CNN in a statement, coming on the heels of a rare FAA ground stop that caused massive disruption.

⬆️ 257 • 💬 134 • 2d ago • [CNN](https://www.cnn.com/2026/11/16/us/united-airlines-outage)

---

**[Baidu, Xiaomi CEOs warn of growing gap between AI hype and returns](https://news.ycombinator.com/item?id=50531751)**

⬆️ 191 • 💬 257 • 1d ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3374774/baidu-xiaomi-ceos-warn-growing-gap-between-ai-hype-and-returns)

---

**["Anthropic Is Not a Safe AI Company" – Coalition Challenges Anthropic Safety](https://news.ycombinator.com/item?id=50548485)**

⬆️ 130 • 💬 77 • 14h ago • [businesswire.com](https://www.businesswire.com/news/home/20261118974464/en/Anthropic-is-Not-a-Safe-AI-Company---Broad-Coalition-of-Scientists-Legal-Scholars-and-Tech-Leaders-Challenge-Anthropics-Safety-Branding-Ahead-of-IPO)

---

**[Ask HN: If AI tools are so good, why isn't your bug backlog empty?](https://news.ycombinator.com/item?id=50520076)**

⬆️ 101 • 💬 114 • 2d ago

---

**[Bank CEOs, NSA Tell Congress That AI-Driven Patches Are Behind Outages](https://news.ycombinator.com/item?id=50540836)**

Artificial intelligence is not causing the disruptions but identifying gaps that are difficult to fix.

⬆️ 96 • 💬 57 • 1d ago • [The Washington Sun](https://www.washingtonsun.com/technology/bank-ceos-nsa-tell-congress-ai-driven-patches-behind-outages)

---

**[AI will not make you rich (2025)](https://news.ycombinator.com/item?id=50555093)**

The disruption is real. It's also predictable.

⬆️ 90 • 💬 53 • 4h ago • [Colossus](https://colossus.com/article/ai-will-not-make-you-rich/)

---

---

## YouTube Videos: "ai"

**[California SUES OpenAI after hundreds of AI agents go ROGUE](https://www.youtube.com/watch?v=hMsMkBQRFmo)**

Fox News senior correspondent Claudia Cowan reports on California's lawsuit against OpenAI after hundreds of autonomous AI ...

📺 Fox News Clips

👁️ 285K • 👍 1K • 💬 781 • ⏱️ 2:09 • 1d ago

---

**[OpenAI’s New AI Just Crossed the Self-Improvement Threshold…](https://www.youtube.com/watch?v=1oIzVB5Ues4)**

OpenAI says GPT-6.2 Astra is its first publicly released model to hit “High” in AI self-improvement. I break down what Astra actually ...

📺 AI Copium

👁️ 40K • 👍 348 • 💬 89 • ⏱️ 9:22 • 15h ago

---

**[Insane AI Breakthroughs Nobody Is Talking About](https://www.youtube.com/watch?v=-oA6oLxWpJg)**

12 AI breakthroughs you probably missed, from incredibly human AI voices to a walking robot powered by an old phone.

📺 Matt Wolfe

👁️ 76K • 👍 1K • 💬 93 • ⏱️ 29:25 • 8h ago

---

**[Stanford&#39;s NCM Is Coming… and It Could Be Worse Than AI](https://www.youtube.com/watch?v=o8zuaPbbaGU)**

For the first time, bots sent more traffic to web pages than people did. Cloudflare's CEO put the split at 57.5% bots to 42.5% ...

📺 Ink Intelligence

👁️ 448K • 👍 5K • 💬 259 • ⏱️ 15:47 • 2d ago

---

**[Former Googler Says AI Will Destroy Humanity at Current Pace w/ Nate Soares | The 1600](https://www.youtube.com/watch?v=CDZetGZiVGw)**

Are we moving too fast with AI? Nate Soares thinks so. He joins Carlo Versano to talk superintelligence, AI systems learning to ...

📺 Newsweek

👁️ 43K • 👍 433 • 💬 232 • ⏱️ 1:01:11 • 1d ago

---

**[I Tested AI Slop In Real Life](https://www.youtube.com/watch?v=aMdqOvT_AJw)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha.

📺 Sambucha

👁️ 89K • 👍 5K • 💬 129 • ⏱️ 0:59 • 12h ago

---

**[The AI Takeover Has Completely BACKFIRED](https://www.youtube.com/watch?v=OXwwYvoW9H4)**

Replacing Humans With AI Has Been A Total DISASTER. The AI takeover is beginning to backfire during a period defined by ...

📺 Damon Cassidy

👁️ 449K • 👍 11K • 💬 2K • ⏱️ 22:33 • 1d ago

---

**[실직이면 차라리 다행?” 노벨상 경제학자가 경고한 AI 시대의 진짜 재앙](https://www.youtube.com/watch?v=sWJuXdeJB4Q)**

AI가 당신의 일자리를 대체한다면, 그다음엔 무슨 일이 벌어질까요? 전문가들은 단순히 '실업률 증가'를 넘어 자본주의 시스템 자체의 ...

📺 원빅월드쇼 | One Big World Show | 1BWS

👁️ 940K • 👍 8K • 💬 977 • ⏱️ 17:26 • 2d ago

---

**[Autonomous AI Attacks Are Here &amp; America Doesn’t Want to Admit It](https://www.youtube.com/watch?v=gLEcm15gbSM)**

The FBI and Google both revealed that autonomous AI attacks are a real thing and it's not going to get better. But officially, other ...

📺 DeFranco News Clips

👁️ 1.0M • 👍 49K • 💬 2K • ⏱️ 1:04 • 1d ago

---

**[AI Hackers Are Coming for EVERYTHING](https://www.youtube.com/watch?v=xyQfFSTTjA0)**

Subscribe to our Newsletter https://financebureau.com/ ~~~~~ AI is exposing security holes in the internet faster than humans ...

📺 Finance Bureau

👁️ 133K • 👍 1K • 💬 142 • ⏱️ 16:37 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 5,314 • ❤️ 931 • 6d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 759,661 • ❤️ 1,597 • 2d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,888,351 • ❤️ 20,580 • 12d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 159 • ❤️ 257 • 1d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 377 • ❤️ 624 • 14h ago

---

**[tiny-voca](https://huggingface.co/n4ze3m/tiny-voca)**

*Muhammed Nazeem *

`text-to-speech`

⬇️ 4,430 • ❤️ 299 • 17h ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 230 • 1d ago

---

**[LongCat-Video-Avatar-1.6](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6)**

*LongCat*

⬇️ 1,226 • ❤️ 275 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,871,190 • ❤️ 12,627 • 1mo ago

---

**[Maxwell-V1-Flash](https://huggingface.co/maxwell-model/Maxwell-V1-Flash)**

*maxwell-model*

`text-generation` `36.8B`

⬇️ 1,052 • ❤️ 239 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 8 • 💬 0 • ⭐ 4,521 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 18 • 💬 2 • ⭐ 7,686 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 13 • 💬 2 • ⭐ 230 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 34 • 💬 9 • ⭐ 12,041 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 132 • 💬 4 • ⭐ 734 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 168 • 💬 6 • ⭐ 123,068 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 69 • 💬 4 • ⭐ 24,412 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 18 • 💬 0 • ⭐ 42,020 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 93,766 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 18.4k • 🔱 1.1k • 4d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 10.8k • 🔱 1.6k • 4h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.1k • 🔱 2.1k • 2h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.4k • 🔱 720 • 5h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.3k • 🔱 1.9k • 20h ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.2k • 🔱 770 • 7m ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 5.9k • 🔱 201 • 1h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.7k • 🔱 129 • 8m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.7k • 🔱 110 • 22h ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.8k • 🔱 249 • 14d ago

---

---

*Generated by PeekDeck - A glance is all you need*
