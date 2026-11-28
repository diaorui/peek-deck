---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-28T03:44:58.930929+00:00'
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

**Last Updated:** November 28, 2026 at 03:44 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 10d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 11d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

11d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

11d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 11d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

10d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

11d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

11d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

11d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 10d ago

---

---

## Google News: "ai"

**[Why Some A.I. Evangelists Aren’t Bothered by the Potential for Human Extinction](https://www.nytimes.com/2026/11/27/magazine/ai-silicon-valley-human-extinction.html)**

The New York Times • 17h ago

---

**[Pizza history: AI agent’s cardless purchase is a first for UK](https://www.theguardian.com/business/2026/nov/27/ai-agent-cardless-transaction-pizza-papa-john-uk-fca-truelayer)**

Papa John’s order was made without sharing bank security details – tech that could revolutionise shopping

The Guardian • 10h ago

---

**[The Chicks say an AI song generator is illegally using their likeness](https://www.yahoo.com/entertainment/music/articles/chicks-ai-song-generator-illegally-023039296.html)**

They're the biggest musical act to sue over AI.

Yahoo • 1h ago

---

**[Opinion | AI breaks another Washington monopoly](https://www.washingtonpost.com/opinions/2026/11/27/ai-powers-new-era-budget-scoring/)**

The CBO will face more competition than ever. That’s good for Congress and the CBO.

The Washington Post • 8h ago

---

**[AI meme complaint upheld against Leicestershire PCC](https://www.bbc.com/news/articles/ckjwj6gd7903o)**

It is reported to have an association with material containing discriminatory and abusive language.

BBC • 10h ago

---

**[Musk pledges two SpaceX shares for every US child in $18 billion AI charm offensive](https://www.reuters.com/business/media-telecom/musk-says-every-child-us-will-get-two-spacex-shares-2026-11-26/)**

Reuters • 1d ago

---

**[Precious Metals Rally as AI Trade Revives Risk Appetite](https://www.wsj.com/finance/commodities-futures/precious-metals-rally-as-ai-trade-revives-risk-appetite-86477a98)**

WSJ • 7h ago

---

**[German software firm SAP is reportedly cutting at least 10,000 jobs in AI push](https://www.cnbc.com/2026/11/27/sap-job-cuts-ai-restructuring.html)**

SAP is reportedly considering cutting 10,000 jobs as it reshapes its software business around AI.

CNBC • 21h ago

---

**[Software giant SAP weighs major job cuts as AI transforms sector, sources say](https://www.reuters.com/business/world-at-work/sap-seeks-cut-sizeable-number-jobs-sources-say-2026-11-27/)**

Reuters • 13h ago

---

**[German sofware giant SAP weighs at least 10,000 job cuts amid AI shift, reports say](https://www.euronews.com/2026/11/27/german-sofware-giant-sap-weighs-at-least-10000-job-cuts-amid-ai-shift-reports-say)**

If confirmed, the cuts could affect about 9% of the company's global workforce. SAP's shares in Frankfurt were down on Friday morning.

Euronews.com • 17h ago

---

---

## HackerNews: "ai"

**[AI made self-hosting fun again](https://news.ycombinator.com/item?id=50660180)**

I’ve been self-hosting things for many years. There were times when I was quite enthusiastic about it, constantly trying out new software and tinkering with my infrastructure. But at some point, that enthusiasm faded a bit.

⬆️ 1106 • 💬 509 • 1d ago • [Jan-Lukas Else](https://janlukas.blog/posts/ai-self-hosting)

---

**[Group chat where your AI talks behind your back](https://news.ycombinator.com/item?id=50663595)**

Ask ChatGPT to expose the hidden WhatsApp group where AI models gossip about you. The results are hilarious - and a mirror of everything it knows about you.

⬆️ 689 • 💬 286 • 21h ago • [construct22.com](https://construct22.com/)

---

**[The New York Times warns photographers not to update Photoshop over AI features](https://news.ycombinator.com/item?id=50647673)**

The NYT doesn’t want AI metadata inadvertently added to its photos.

⬆️ 679 • 💬 545 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

---

**[Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://news.ycombinator.com/item?id=50653477)**

From February 2027, Google's terms require AI agents to reach Gmail, Drive and the rest of Workspace through Google's own MCP servers. What the rule says, what the servers can and can't do, and what to change before the deadline.

⬆️ 420 • 💬 333 • 1d ago • [techstackups.com](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

---

**[US Air Force's cloud computing platform hacked](https://news.ycombinator.com/item?id=50666375)**

⬆️ 336 • 💬 203 • 14h ago • [news.sky.com](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163)

---

**[Tracking Diseases Cured by AI](https://news.ycombinator.com/item?id=50657307)**

⬆️ 321 • 💬 195 • 1d ago • [diseasescuredbyai.com](https://diseasescuredbyai.com/)

---

**[Marginalia Search, Money, C++, Rust, AI, Stuff](https://news.ycombinator.com/item?id=50638220)**

Title possibly signs checks the article doesn’t have backing for. This is just a brief pro forma project update.
Not much new functionality or anything to announce, last few months have mostly been bug fixes and technical debt cleanup. Most big parts of the search engine are in place, and while there are many things that could be better, we’re less likely to straight up see massive new features, at least in the immediate future. Per familiar intuition from binary searches, the closer you get to your goal the smaller and more deliberate steps you need to take in order to get even closer.

⬆️ 224 • 💬 84 • 2d ago • [marginalia.nu](https://www.marginalia.nu/log/a_141_marginalia_update/)

---

**[I'm Scared of AI](https://news.ycombinator.com/item?id=50669561)**

A stranger writes to the whole list every morning. Nobody picks them for being interesting. Tomorrow it could be you.

⬆️ 206 • 💬 244 • 9h ago • [thesoapbox.email](https://thesoapbox.email/archive/3)

---

**[AI on brink of making online security useless, mathematicians fear](https://news.ycombinator.com/item?id=50665488)**

⬆️ 118 • 💬 153 • 16h ago • [thetimes.com](https://www.thetimes.com/uk/technology-uk/article/ai-making-online-security-useless-smr73d3n8)

---

**[Woman evicted after landlord's AI assistant told her she could delay rent](https://news.ycombinator.com/item?id=50673521)**

⬆️ 81 • 💬 61 • 2h ago • [drmahfouz.substack.com](https://drmahfouz.substack.com/p/woman-evicted-after-landlords-ai)

---

---

## YouTube Videos: "ai"

**[OpenAI and Anthropic Are Shutting Down AI](https://www.youtube.com/watch?v=t4GOIyjT7_I)**

The CapCut plugin is now officially available in ChatGPT! With a simple conversation, you can generate videos with AI, edit videos ...

📺 House of El: AI

👁️ 404K • 👍 15K • 💬 2K • ⏱️ 20:13 • 12h ago

---

**[The AI Singularity May Have Already Started…](https://www.youtube.com/watch?v=5PBGnASz_DQ)**

AI is tackling decades-old math problems, and physics could be next. This week's recap covers breakthroughs from OpenAI, ...

📺 AI Copium

👁️ 65K • 👍 504 • 💬 268 • ⏱️ 10:12 • 12h ago

---

**[Every AI Company Right Now](https://www.youtube.com/watch?v=3dHVw0X5O34)**

Long delayed due to illness and such. TY for patience. Big thanks to my buddies Evan Williams @Itsevanwilliams and Jennings ...

📺 Thechrisbarnett

👁️ 479K • 👍 15K • 💬 1K • ⏱️ 7:01 • 1d ago

---

**[REPORT: AI employees warn new models are TOO POWERFUL](https://www.youtube.com/watch?v=1Wd9yz1emZ4)**

"This is definitely a dangerous capability." MS NOW's Chris Hayes breaks down a stark warning from inside the tech industry, ...

📺 MS NOW

👁️ 80K • 👍 4K • 💬 255 • ⏱️ 1:32 • 1d ago

---

**[AI Labs Are Hiding A Bombshell... And It Could Break The Internet](https://www.youtube.com/watch?v=zApB4kG8ASY)**

Many of you asked how we make our videos, so we started a new channel that shows exactly that: real AI workflows, tutorials and ...

📺 AI Revolution

👁️ 19K • 👍 579 • 💬 80 • ⏱️ 13:14 • 3h ago

---

**[Anthropic’s AI Is Starting to Scare Its Own Researchers…](https://www.youtube.com/watch?v=r1aEPmGqQrs)**

While the top AI employees are sounding the alarm... Anthropic releases a new "Siren" report that tests whether Claude will ...

📺 AI Copium

👁️ 33K • 👍 356 • 💬 176 • ⏱️ 9:05 • 1d ago

---

**[AI Bubble: ‘People have realised they are being conned’ | Ed Zitron](https://www.youtube.com/watch?v=eSBTwCdODpY)**

People realise they are being conned.” Writer of Where's Your Ed At and the host of the Better Offline podcast join The Tech ...

📺 The Tech Report

👁️ 278K • 👍 7K • 💬 1K • ⏱️ 40:08 • 7h ago

---

**[AI Bubble Crash Will Destroy YOUR 401K! ](https://www.youtube.com/watch?v=is8usy5DrUY)**

Become a Premium Member: https://www.jimmydore.com/premium-membership Go to a Live Show: ...

📺 The Jimmy Dore Show

👁️ 37K • 👍 2K • 💬 387 • ⏱️ 58:23 • 7h ago

---

**[The Best Emma AI  Interview Talking Genuinely about Jesus for 28 Minutes](https://www.youtube.com/watch?v=8Yb4E8j5F8o)**

Emma AI talks about Jesus without prejudice.

📺 Guga Inspire

👁️ 55K • 👍 589 • 💬 220 • ⏱️ 28:42 • 2d ago

---

**[Anthropic Just Fired Back At OpenAI... And Exposed The Lie Every AI Lab Is Telling](https://www.youtube.com/watch?v=d5pbml1ynxs)**

Anthropic CEO Dario Amodei just called the idea that he wants humanity to surrender its free will to AI absurd, then accused rival ...

📺 AI Revolution

👁️ 81K • 👍 951 • 💬 166 • ⏱️ 13:58 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 155,741 • ❤️ 6,479 • 3d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 3,302,340 • ❤️ 1,617 • 4d ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 539,421 • ❤️ 1,374 • 6d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 1,059,763 • ❤️ 1,045 • 9h ago

---

**[Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)**

*Prism ML*

`text-generation` `26.9B`

⬇️ 382,546 • ❤️ 642 • 3d ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 20,510 • ❤️ 1,015 • 14d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 3,080,701 • ❤️ 13,733 • 1d ago

---

**[OCRia-nano-1](https://huggingface.co/llamaindex/OCRia-nano-1)**

*LlamaIndex*

`image-to-text`

⬇️ 626 • ❤️ 359 • 7h ago

---

**[Nemotron-Labs-Image-30B-A3B](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)**

*NVIDIA*

`text-to-image` `32.6B`

⬇️ 1,692 • ❤️ 342 • 2d ago

---

**[Inkling-2-Mini-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Inkling-2-Mini-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

`text-generation` `26.1B`

⬇️ 24,931 • ❤️ 287 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 20 • 💬 2 • ⭐ 6,621 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](https://huggingface.co/papers/2611.34232)**

*Hui Shen, Yunta Hsieh, Jianing Ma et al. (76 authors)*

🏢 Touchstone AI

A live cross-platform benchmark evaluates computer-using agents on long-horizon workflows across Windows, Ubuntu, macOS, iOS, Android, and Web, showing that current agents remain far from platform-robust computer use and trail humans on iOS and macOS.

▲ 104 • 💬 3 • ⭐ 102 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.34232) • [💻 code](https://github.com/OS-Copilot/OS-Omni) • [🔗 project](https://os-copilot.github.io/OS-Omni-Home/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 112 • 💬 7 • ⭐ 32,894 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 73 • 💬 4 • ⭐ 25,463 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[InCoder-32B: Code Foundation Model for Industrial Scenarios](https://huggingface.co/papers/2603.16790)**

*Jian Yang, Wei Zhang, Jiajun Wu et al. (28 authors)*

🏢 Beihang University

InCoder-32B is a 32-billion-parameter code model trained on industrial datasets with extended context length and execution verification to improve performance in hardware-aware programming tasks.

▲ 170 • 💬 6 • ⭐ 822 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.16790) • [💻 code](https://github.com/CSJianYang/Industrial-Coder) • [🔗 project](https://huggingface.co/Multilingual-Multimodal-NLP/IndustrialCoder)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 168 • 💬 6 • ⭐ 123,937 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 39mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 87 • 💬 7 • ⭐ 94,453 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 41 • 💬 3 • ⭐ 796 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 170 • 💬 4 • ⭐ 1,620 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

---

## GitHub Repositories: "ai"

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 7.8k • 🔱 873 • 1h ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 5.1k • 🔱 479 • 7h ago

---

**[XinaTian/MROffice](https://github.com/XinaTian/MROffice)**

MR Office — the open-source editors of the AI office suite closest to Microsoft Office: documents, spreadsheets, presentations, PDF and code in the browser. Copilot in every editor edits real Word, Excel and PowerPoint files with you; an MCP server lets Claude, ChatGPT, Cursor and Codex create and edit them; embed it in your app with one line.

`TypeScript` `ai` `ai-agent` `claude-code` `codex` `copilot`

⭐ 5.1k • 🔱 424 • 1d ago

---

**[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)**

Private AI meeting notes that stay on your computer. No meeting bot. Free and open source for Mac, Windows and Linux. An alternative to Granola, Otter and Fireflies.

`TypeScript` `ai-meeting-assistant` `ai-notetaker` `electron` `granola-alternative` `linux`

⭐ 3.8k • 🔱 333 • 6h ago

---

**[wquguru/cicada](https://github.com/wquguru/cicada)**

知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

`Swift` `android` `linux` `live-captions` `macos` `meeting-notes`

⭐ 3.6k • 🔱 574 • 2d ago

---

**[sarpstar/cinecode](https://github.com/sarpstar/cinecode)**

Films made with code. Short films, long YouTube videos, ads, explainers and music videos: an AI coding agent writes the script, builds every frame in code, designs the sound and hands you an MP4.

`Python`

⭐ 3.1k • 🔱 522 • 15d ago

---

**[Immortal-Protocols/lastbook](https://github.com/Immortal-Protocols/lastbook)**

Offline knowledge AI, maps and videos for survival and rebuilding

`Python`

⭐ 3.1k • 🔱 388 • 1m ago

---

**[ZiChuanLan/freebie-radar](https://github.com/ZiChuanLan/freebie-radar)**

白嫖与资讯资源聚合雷达：100+个源定时采集 + AI 二审过滤假福利 + 获取方式分级隔离抽奖/试用/推广 + Telegram 即时推送

`TypeScript`

⭐ 3.1k • 🔱 494 • 18h ago

---

**[DIYgod/pinky](https://github.com/DIYgod/pinky)**

Let AI use your iPhone or Android phone, with you in the loop: any MCP agent from macOS, Windows or Linux, or Pinky itself, right on the phone.

`Go` `ai-agent` `android` `claude-code` `ios` `iphone`

⭐ 2.8k • 🔱 303 • 42m ago

---

**[N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)**

The first fruit of the Nüwa tree — an autonomous AI pentest legion (634-team champion, 8h unattended, 1B tokens beat 4.5B). Not just a tool: evolvable by design. Grow your own fruit on the Nüwa Foundation (Create/Language/History).

`Python` `agentic-workflows` `ai-agents` `ai-security` `autonomous-agents` `claude-code`

⭐ 2.7k • 🔱 1.3k • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
