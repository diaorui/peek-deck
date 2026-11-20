---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-20T13:26:55.671655+00:00'
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

**Last Updated:** November 20, 2026 at 13:26 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 3d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 3d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

3d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

3d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 3d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

3d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

3d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

4d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

3d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 3d ago

---

---

## Google News: "ai"

**[GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)**

This AI threat update provides GTIG’s findings on adversarial misuse of AI including Gemini and other non-Google tools.

Google Cloud • 3d ago

---

**[Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)**

OpenAI publishes new results on open problems in mathematics from an internal frontier model and shares Lean proof formalizations and research details on GitHub.

OpenAI • 1mo ago

---

**[Nvidia, Oracle, CoreWeave and other AI stocks sink on OpenAI revenue report](https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html)**

OpenAI has told investors that it hit roughly $50 billion in annualized revenue at the end of September, CNBC confirmed.

CNBC • 1mo ago

---

**[Independent Assessment of AI R&D Acceleration at Anthropic in October 2026](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)**

METR's high-access assessment of the degree to which AI is accelerating AI research and development at Anthropic.

METR • 15d ago

---

**[Gemini 4 Argon: our next era of frontier intelligence](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)**

Announcing Gemini 4 Argon, our frontier model for real-world coding, enterprise knowledge work, and cyber defense, rolling out soon.

blog.google • 1mo ago

---

**[PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet](https://www.wiz.io/blog/php2shell-php-rce)**

Core PHP engine flaws enable remote code execution and Heartbleed-style memory disclosure across the web.

wiz.io • 1mo ago

---

**[In China, the AI bubble has already burst](https://www.reuters.com/world/china/china-ai-bubble-has-already-burst-2026-10-26/)**

Reuters • 24d ago

---

**[Google Will Turn Off Search for Schools That Reject A.I.](https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html)**

The New York Times • 17d ago

---

**[The Top 100 Gen AI Consumer Apps — 7th Edition](https://a16z.com/100-gen-ai-apps-7/)**

Which AI apps are people actively using? What’s actually making money, beyond being popular? We analyzed the data in the seventh edition of our Top 100 AI Consumer Apps report.

Andreessen Horowitz • 1mo ago

---

**[AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)**

Storm-0940 used ARTEX agentic AI to accelerate a ConnectWise supply chain compromise, enabling application credential abuse across Microsoft 365 environments.

Microsoft • 1mo ago

---

---

## HackerNews: "ai"

**[AI is killing All About Berlin](https://news.ycombinator.com/item?id=50542705)**

They used my work to train their AI, and now they're using their AI to put me out of work.

⬆️ 810 • 💬 711 • 2d ago • [nicolasbouliane.com](https://nicolasbouliane.com/blog/death-by-ai)

---

**[Google's AI answers reducing search traffic by 40%](https://news.ycombinator.com/item?id=50540178)**

Google's AI answers are taking clicks from websites in the search results. In a randomized experiment, researchers hid AI Overviews from some US desktop users. Comparing them with users who still saw Overviews shows that an Overview cuts clicks to outside websites by about 40%. Those Overviews now appear on more than half the US keywords DataForSEO tracks, up from 6% two years ago. The industry's answer, GEO (generative engine optimization), has yet to show a way to compensate for the loss. While AI citations correlate with the same kind of link profile that goes with higher Google rankings, in March AI assistants sent websites just 0.3% of their traffic.

⬆️ 709 • 💬 564 • 2d ago • [revscope.co](https://revscope.co/blog/search-seo-geo-2026/)

---

**[Fuck Your AI Safeguards](https://news.ycombinator.com/item?id=50562262)**

You can't tell me that you found a security issue in my product and then refuse to fix it.

⬆️ 569 • 💬 229 • 20h ago • [./techtipsy](https://ounapuu.ee/posts/2026/11/19/unsafeguards/)

---

**[AI agents ask better questions than KPMG accountants in audit trial](https://news.ycombinator.com/item?id=50547777)**

LONDON, November 18, 2026 — Artificial intelligence has taken another significant step into the world of professional services after KPMG revealed that AI

⬆️ 492 • 💬 260 • 1d ago • [European Business Magazine](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

---

**[Harvard researchers find AI coding agents shifted the bottleneck to code review](https://news.ycombinator.com/item?id=50538303)**

Harvard study: AI coding agents raised code output 30 percent; finished work did not measurably rise, and getting code through review took 49 percent longer.

⬆️ 327 • 💬 462 • 2d ago • [ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)

---

**[Pete Warden on local AI, open models, voice interfaces, the future of hardware](https://news.ycombinator.com/item?id=50561508)**

⬆️ 263 • 💬 228 • 21h ago • [thedataexchange.media](https://thedataexchange.media/pete-warden-moonshine/)

---

**[Frostbite: A new CPU architecture discovered, designed and verified by AI](https://news.ycombinator.com/item?id=50572503)**

Frostbite is a general-purpose CPU built around interaction nets, discovered, designed, and verified end-to-end by our AI systems, reaching 4.59x the performance-per-watt of a modern superscalar (dual-issue, in-order) CPU core.

⬆️ 236 • 💬 147 • 3h ago • [Architect Labs](https://architectlabs.com/blog/frostbite)

---

**[Baidu, Xiaomi CEOs warn of growing gap between AI hype and returns](https://news.ycombinator.com/item?id=50531751)**

⬆️ 191 • 💬 259 • 2d ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3374774/baidu-xiaomi-ceos-warn-growing-gap-between-ai-hype-and-returns)

---

**["Anthropic Is Not a Safe AI Company" – Coalition Challenges Anthropic Safety](https://news.ycombinator.com/item?id=50548485)**

⬆️ 147 • 💬 79 • 1d ago • [businesswire.com](https://www.businesswire.com/news/home/20261118974464/en/Anthropic-is-Not-a-Safe-AI-Company---Broad-Coalition-of-Scientists-Legal-Scholars-and-Tech-Leaders-Challenge-Anthropics-Safety-Branding-Ahead-of-IPO)

---

**[AI isn't replacing your job. It's turning it into low-paid gig work](https://news.ycombinator.com/item?id=50562500)**

⬆️ 141 • 💬 69 • 20h ago • [restofworld.org](https://restofworld.org/2026/ai-jobs-skills-gig-work/)

---

---

## YouTube Videos: "ai"

**[AI Whistleblower WARNS: &quot;You Have No Idea What&#39;s Coming In 2027&quot;](https://www.youtube.com/watch?v=Cfj0Bfdq3ww)**

In October 2026, security experts gave a month a name: "Black October." An AI found critical holes in software that runs a huge ...

📺 Black Box

👁️ 21K • 👍 130 • 💬 46 • ⏱️ 45:23 • 1d ago

---

**[OpenAI’s New AI Just Crossed the Self-Improvement Threshold…](https://www.youtube.com/watch?v=1oIzVB5Ues4)**

OpenAI says GPT-6.2 Astra is its first publicly released model to hit “High” in AI self-improvement. I break down what Astra actually ...

📺 AI Copium

👁️ 52K • 👍 411 • 💬 108 • ⏱️ 9:22 • 1d ago

---

**[AI chatbots helped plan electrical grid ATTACK, report reveals](https://www.youtube.com/watch?v=9U5yOWi2W3M)**

Cybersecurity expert Morgan Wright joins 'America Reports' to discuss a new Government Accountability Office report on artificial ...

📺 Fox News Clips

👁️ 215K • 👍 1K • 💬 717 • ⏱️ 8:42 • 1d ago

---

**[Superhuman AI Is Coming Next Year](https://www.youtube.com/watch?v=IO6-9l56jSg)**

At one leading A.I. lab, nine out of ten changes to its code are now written by its own A.I. Some insiders forecast superhuman A.I. ...

📺 The Good Takeoff

👁️ 28K • 👍 285 • 💬 60 • ⏱️ 11:05 • 1d ago

---

**[Inside China’s AI-powered Silicon Valley](https://www.youtube.com/watch?v=jfNZHzGaPqU)**

NBC Nightly News anchor Tom Llamas reports from China's version of Silicon Valley in Shenzhen, where a fierce race for AI ...

📺 NBC News

👁️ 176K • 👍 759 • 💬 248 • ⏱️ 2:44 • 1d ago

---

**[“I Don’t Believe in Coincidences:” AI Expert Warns of Recent Tech Outages | Amanpour and Company](https://www.youtube.com/watch?v=kysahSdnsGk)**

Dr. Ayanna Howard has spent her career exploring the reach and implications of artificial intelligence. She says we are only just ...

📺 Amanpour and Company

👁️ 64K • 👍 872 • 💬 73 • ⏱️ 18:16 • 15h ago

---

**[California SUES OpenAI after hundreds of AI agents go ROGUE](https://www.youtube.com/watch?v=hMsMkBQRFmo)**

Fox News senior correspondent Claudia Cowan reports on California's lawsuit against OpenAI after hundreds of autonomous AI ...

📺 Fox News Clips

👁️ 341K • 👍 1K • 💬 867 • ⏱️ 2:09 • 2d ago

---

**[DeepMind Just Released The Best Thing AI Ever Did](https://www.youtube.com/watch?v=Cy7Wz6Z4TWU)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.com/papers The DeepMind AlphaGenome paper is ...

📺 Two Minute Papers

👁️ 167K • 👍 4K • 💬 307 • ⏱️ 6:26 • 1d ago

---

**[John Lennox on How AI Could Take Over the World (and Where It&#39;s Already Happening)](https://www.youtube.com/watch?v=-Pmst8bkRaE)**

Watch the full interview with Professor Lennox https://youtu.be/KIo9qL2LD90 Subscribe to Socrates in the City ...

📺 Socrates in the City

👁️ 236K • 💬 506 • ⏱️ 21:58 • 2d ago

---

**[Is AI a threat to democracy? | The Global Story](https://www.youtube.com/watch?v=2f4HuzzKeHo)**

As China races to catch up with the US on artificial intelligence, the AI revolution is raising questions that go beyond superpower ...

📺 BBC News

👁️ 38K • 👍 161 • 💬 48 • ⏱️ 24:18 • 15h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 7,323 • ❤️ 4,076 • 7d ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 376 • 11h ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 329 • 6d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 1,874 • ❤️ 794 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,454,419 • ❤️ 20,733 • 13d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 876,986 • ❤️ 1,670 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,964,523 • ❤️ 12,800 • 1mo ago

---

**[Qwen-Image-2.1-Uncensored-Omni-Quantized](https://huggingface.co/chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized)**

*Chatr Labs*

`text-to-image` `7.1B`

⬇️ 309,394 • ❤️ 719 • 5d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 3,949 • ❤️ 488 • 1d ago

---

**[SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B)**

*SenseNova*

`image-text-to-text` `9.7B`

⬇️ 1,631 • ❤️ 406 • 7h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 10 • 💬 0 • ⭐ 5,145 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 7,793 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 17 • 💬 2 • ⭐ 337 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 142 • 💬 4 • ⭐ 1,004 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 36 • 💬 9 • ⭐ 12,109 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 20 • 💬 0 • ⭐ 42,312 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,217 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 24,497 • 1mo ago

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

▲ 87 • 💬 7 • ⭐ 93,893 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 19.0k • 🔱 1.1k • 5d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 11.3k • 🔱 1.7k • 6h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.3k • 🔱 2.1k • 7m ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.5k • 🔱 735 • 1d ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.4k • 🔱 1.9k • 2d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.3k • 🔱 781 • 19h ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.2k • 🔱 216 • 4h ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 5.4k • 🔱 420 • 58m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.8k • 🔱 110 • 7h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.8k • 🔱 135 • 3m ago

---

---

*Generated by PeekDeck - A glance is all you need*
