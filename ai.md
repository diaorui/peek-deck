---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-28T20:46:01.193386+00:00'
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

**Last Updated:** November 28, 2026 at 20:46 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 11d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 12d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

11d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

12d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 12d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

11d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

11d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

12d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

11d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 11d ago

---

---

## Google News: "ai"

**[AI labs sitting on ‘bombshell’ revelations that could cause global chaos, experts believe](https://www.theguardian.com/technology/2026/nov/28/ai-artificial-intelligence-encryption-global-chaos)**

Exclusive: AI may have cracked decades-old maths problems that underpin encryption at banks and government agencies

The Guardian • 15h ago

---

**[Can AI crack encryption?](https://www.ft.com/content/1a29e62d-b18d-4bad-937d-34f3eae0587a?syn-25a6b1a6=1)**

Financial Times • 1d ago

---

**[AI's Capacity To Achieve Mathematical Breakthroughs Could Endanger Financial And Governmental Security, Experts Warn](https://www.yahoo.com/news/science/articles/ais-capacity-achieve-mathematical-breakthroughs-152139957.html)**

Rumors of AI breakthroughs on difficult mathematical problems have raised concerns that future systems could weaken RSA encryption, potentially threatening banking transactions, as well as private per...

Yahoo • 5h ago

---

**[Rumors swirl that AI models have already cracked math secrets too dangerous to publish](https://www.axios.com/2026/11/28/ai-math-breakthroughs-encryption-p-vs-np)**

Axios • 7h ago

---

**[College Board says it is investigating possible AI hack](https://www.washingtonpost.com/nation/2026/11/28/college-board-says-it-is-investigating-possible-ai-hack/)**

The board said it “took immediate action” to protect its users and systems.

The Washington Post • 1h ago

---

**[Musk says Google has ‘expressed interest’ in renting more AI computing power from SpaceX](https://thehill.com/business/6246205-musk-google-spacex-ai-compute/)**

The Hill • 1h ago

---

**[Opinion | Wasting Money Is Exactly What A.I. Companies Should Be Doing](https://www.nytimes.com/2026/11/28/opinion/ai-boom-companies-investments-tech.html)**

The New York Times • 8h ago

---

**[AI meme complaint upheld against Leicestershire PCC](https://www.bbc.com/news/articles/ckjwj6gd7903o)**

It is reported to have an association with material containing discriminatory and abusive language.

BBC • 1d ago

---

**[AI data center boom strains construction labor across the U.S.](https://www.cnbc.com/2026/11/28/ai-data-center-construction-worker-shortage-texas.html)**

CNBC traveled to Abilene, Texas to see how the AI data center construction boom is impacting the local economy in both positive and negative ways.

CNBC • 6h ago

---

**[Jim Cramer Is Still Bullish On These 5 Tech Stocks Despite AI Bear Market](https://finance.yahoo.com/technology/articles/jim-cramer-still-bullish-5-184921596.html)**

The Nasdaq-100 briefly fell 20% below its October 6 record closing high on November 25 before recovering much of the day’s loss. The sell-off had picked up weeks earlier. On November 5, the Nasdaq Composite fell 5.5% as investors reconsidered how quickly the U.S. could build out AI infrastructure after the midterm elections. By late […]

Yahoo Finance • 1d ago

---

---

## HackerNews: "ai"

**[AI made self-hosting fun again](https://news.ycombinator.com/item?id=50660180)**

I’ve been self-hosting things for many years. There were times when I was quite enthusiastic about it, constantly trying out new software and tinkering with my infrastructure. But at some point, that enthusiasm faded a bit.

⬆️ 1143 • 💬 535 • 1d ago • [Jan-Lukas Else](https://janlukas.blog/posts/ai-self-hosting)

---

**[Group chat where your AI talks behind your back](https://news.ycombinator.com/item?id=50663595)**

Ask ChatGPT to expose the hidden WhatsApp group where AI models gossip about you. The results are hilarious - and a mirror of everything it knows about you.

⬆️ 727 • 💬 292 • 1d ago • [construct22.com](https://construct22.com/)

---

**[The New York Times warns photographers not to update Photoshop over AI features](https://news.ycombinator.com/item?id=50647673)**

The NYT doesn’t want AI metadata inadvertently added to its photos.

⬆️ 686 • 💬 548 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

---

**[Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://news.ycombinator.com/item?id=50653477)**

From February 2027, Google's terms require AI agents to reach Gmail, Drive and the rest of Workspace through Google's own MCP servers. What the rule says, what the servers can and can't do, and what to change before the deadline.

⬆️ 422 • 💬 333 • 2d ago • [techstackups.com](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

---

**[US Air Force's cloud computing platform hacked](https://news.ycombinator.com/item?id=50666375)**

⬆️ 356 • 💬 215 • 1d ago • [news.sky.com](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163)

---

**[Donald Knuth suspends error bounties due to an influx of AI-generated reports](https://news.ycombinator.com/item?id=50680168)**

⬆️ 343 • 💬 76 • 2h ago • [cs.stanford.edu](https://cs.stanford.edu/~knuth/moratorium.html)

---

**[Tracking Diseases Cured by AI](https://news.ycombinator.com/item?id=50657307)**

⬆️ 325 • 💬 199 • 2d ago • [diseasescuredbyai.com](https://diseasescuredbyai.com/)

---

**[I'm Scared of AI](https://news.ycombinator.com/item?id=50669561)**

A stranger writes to the whole list every morning. Nobody picks them for being interesting. Tomorrow it could be you.

⬆️ 218 • 💬 251 • 1d ago • [thesoapbox.email](https://thesoapbox.email/archive/3)

---

**[Woman evicted after landlord's AI assistant told her she could delay rent](https://news.ycombinator.com/item?id=50673521)**

⬆️ 212 • 💬 176 • 19h ago • [drmahfouz.substack.com](https://drmahfouz.substack.com/p/woman-evicted-after-landlords-ai)

---

**[AI on brink of making online security useless, mathematicians fear](https://news.ycombinator.com/item?id=50665488)**

⬆️ 119 • 💬 164 • 1d ago • [thetimes.com](https://www.thetimes.com/uk/technology-uk/article/ai-making-online-security-useless-smr73d3n8)

---

---

## YouTube Videos: "ai"

**[Can Humanity Survive What Just Happened In AI Without Immediate Action?](https://www.youtube.com/watch?v=6esLwYuP-3Y)**

iRESTORE: Unlock your best hair & skin with @iRestorelaser and HUGE savings on iRESTORE with code THEORY at ...

📺 Tom Bilyeu

👁️ 89K • 👍 1K • 💬 721 • ⏱️ 51:57 • 6h ago

---

**[Anthropic Just Killed AI Agents - EVERYTHING You Need to Know](https://www.youtube.com/watch?v=fBSI3HLoxWc)**

FREE Skills: https://www.skool.com/wearenocode TOOLS AI Coding: Claude Code: https://claude.ai/referral/hNMjMWDmiA ...

📺 Christian Peverelli

👁️ 185K • 👍 3K • 💬 223 • ⏱️ 7:39 • 17h ago

---

**[Nvidia Chips Flood the Resale Market -AI Financing Crisis Deepens as Banks Freeze Billions in Loans ](https://www.youtube.com/watch?v=Dy5kDK4_RwI)**

BLACK FRIDAY BUNDLE SPECIAL for Trust and Will Courses https://theoxacademy.com/trusts-wills/ Disclaimer: The views and ...

📺 Ox Talks

👁️ 54K • 👍 3K • 💬 407 • ⏱️ 8:44 • 1d ago

---

**[OpenAI and Anthropic Are Shutting Down AI](https://www.youtube.com/watch?v=t4GOIyjT7_I)**

The CapCut plugin is now officially available in ChatGPT! With a simple conversation, you can generate videos with AI, edit videos ...

📺 House of El: AI

👁️ 534K • 👍 19K • 💬 3K • ⏱️ 20:13 • 1d ago

---

**[AI Agents Explained for Beginners (And How to Build One)](https://www.youtube.com/watch?v=YwST-4bQzGk)**

Use code YOURI to get an extra 10% off your Hostinger plan https://www.hostg.xyz/SHJiC In this video, I explain what AI agents ...

📺 Roboverse

👁️ 8K • 💬 1 • ⏱️ 9:57 • 5h ago

---

**[The AI Singularity May Have Already Started…](https://www.youtube.com/watch?v=5PBGnASz_DQ)**

AI is tackling decades-old math problems, and physics could be next. This week's recap covers breakthroughs from OpenAI, ...

📺 AI Copium

👁️ 87K • 👍 623 • 💬 311 • ⏱️ 10:12 • 1d ago

---

**[MIT Physicist on what the United States can do to stop AI from ending humanity](https://www.youtube.com/watch?v=3MH7cywBUJk)**

Lovett sits down with Max Tegmark, a leading expert and thinker on AI and the human response to it, to talk about the latest wave ...

📺 Pod Save America

👁️ 65K • 👍 2K • 💬 291 • ⏱️ 1:29:58 • 6h ago

---

**[This AI Kept Mistaking Him for a Sleeping Driver! 🚗🤖🎥video credit : @zackdfilms](https://www.youtube.com/watch?v=py_NT8xjnPA)**

An AI driver-monitoring system kept warning this man that he was falling asleep, even when he was fully awake. The system ...

📺 বিনোদন টিভি 25

👁️ 247K • 👍 5K • 💬 1 • ⏱️ 0:30 • 13h ago

---

**[REPORT: AI employees warn new models are TOO POWERFUL](https://www.youtube.com/watch?v=1Wd9yz1emZ4)**

"This is definitely a dangerous capability." MS NOW's Chris Hayes breaks down a stark warning from inside the tech industry, ...

📺 MS NOW

👁️ 89K • 👍 4K • 💬 276 • ⏱️ 1:32 • 1d ago

---

**[Iran Releases AI Attack Video Targeting Amazon, Microsoft and SpaceX as Trump Warns Tehran](https://www.youtube.com/watch?v=eYPvhmSWkh4)**

Iranian state media has released an AI-generated video depicting fictional attacks on the headquarters of Amazon, Microsoft and ...

📺 WJACTV

👁️ 56K • 👍 145 • 💬 67 • ⏱️ 2:28 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 177,012 • ❤️ 6,592 • 4d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 3,621,301 • ❤️ 1,680 • 5d ago

---

**[Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)**

*Prism ML*

`text-generation` `26.9B`

⬇️ 473,980 • ❤️ 726 • 3d ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 759,937 • ❤️ 1,447 • 7d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 1,297,386 • ❤️ 1,094 • 1d ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 22,810 • ❤️ 1,053 • 14d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 3,088,512 • ❤️ 13,831 • 2d ago

---

**[OCRia-nano-1](https://huggingface.co/llamaindex/OCRia-nano-1)**

*LlamaIndex*

`image-to-text`

⬇️ 9,982 • ❤️ 403 • 1d ago

---

**[Inkling-2-Mini-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Inkling-2-Mini-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

`text-generation` `26.1B`

⬇️ 97,896 • ❤️ 356 • 1d ago

---

**[Nemotron-Labs-Image-30B-A3B](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)**

*NVIDIA*

`text-to-image` `32.6B`

⬇️ 2,042 • ❤️ 383 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 21 • 💬 2 • ⭐ 6,703 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 74 • 💬 4 • ⭐ 25,491 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 113 • 💬 7 • ⭐ 32,910 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](https://huggingface.co/papers/2611.34232)**

*Hui Shen, Yunta Hsieh, Jianing Ma et al. (76 authors)*

🏢 Touchstone AI

A live cross-platform benchmark evaluates computer-using agents on long-horizon workflows across Windows, Ubuntu, macOS, iOS, Android, and Web, showing that current agents remain far from platform-robust computer use and trail humans on iOS and macOS.

▲ 114 • 💬 4 • ⭐ 108 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.34232) • [💻 code](https://github.com/OS-Copilot/OS-Omni) • [🔗 project](https://os-copilot.github.io/OS-Omni-Home/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,987 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 78 • 💬 1 • ⭐ 86,094 • 39mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[InCoder-32B: Code Foundation Model for Industrial Scenarios](https://huggingface.co/papers/2603.16790)**

*Jian Yang, Wei Zhang, Jiajun Wu et al. (28 authors)*

🏢 Beihang University

InCoder-32B is a 32-billion-parameter code model trained on industrial datasets with extended context length and execution verification to improve performance in hardware-aware programming tasks.

▲ 171 • 💬 6 • ⭐ 824 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.16790) • [💻 code](https://github.com/CSJianYang/Industrial-Coder) • [🔗 project](https://huggingface.co/Multilingual-Multimodal-NLP/IndustrialCoder)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 41 • 💬 3 • ⭐ 807 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 87 • 💬 7 • ⭐ 94,494 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 171 • 💬 4 • ⭐ 1,641 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

---

## GitHub Repositories: "ai"

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 8.2k • 🔱 912 • 6m ago

---

**[XinaTian/MROffice](https://github.com/XinaTian/MROffice)**

MR Office — the open-source editors of the AI office suite closest to Microsoft Office: documents, spreadsheets, presentations, PDF and code in the browser. Copilot in every editor edits real Word, Excel and PowerPoint files with you; an MCP server lets Claude, ChatGPT, Cursor and Codex create and edit them; embed it in your app with one line.

`TypeScript` `ai` `ai-agent` `claude-code` `codex` `copilot`

⭐ 5.5k • 🔱 437 • 1d ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 5.2k • 🔱 487 • 3m ago

---

**[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)**

Private AI meeting notes that stay on your computer. No meeting bot. Free and open source for Mac, Windows and Linux. An alternative to Granola, Otter and Fireflies.

`TypeScript` `ai-meeting-assistant` `ai-notetaker` `electron` `granola-alternative` `linux`

⭐ 3.8k • 🔱 339 • 49m ago

---

**[wquguru/cicada](https://github.com/wquguru/cicada)**

知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

`Swift` `android` `linux` `live-captions` `macos` `meeting-notes`

⭐ 3.7k • 🔱 595 • 2h ago

---

**[sarpstar/cinecode](https://github.com/sarpstar/cinecode)**

Films made with code. Short films, long YouTube videos, ads, explainers and music videos: an AI coding agent writes the script, builds every frame in code, designs the sound and hands you an MP4.

`Python`

⭐ 3.2k • 🔱 527 • 15d ago

---

**[ZiChuanLan/freebie-radar](https://github.com/ZiChuanLan/freebie-radar)**

白嫖与资讯资源聚合雷达：100+个源定时采集 + AI 二审过滤假福利 + 获取方式分级隔离抽奖/试用/推广 + Telegram 即时推送

`TypeScript`

⭐ 3.2k • 🔱 504 • 1d ago

---

**[Immortal-Protocols/lastbook](https://github.com/Immortal-Protocols/lastbook)**

Offline knowledge AI, maps and videos for survival and rebuilding

`Python`

⭐ 3.1k • 🔱 390 • 17h ago

---

**[nexu-io/opengame](https://github.com/nexu-io/opengame)**

The Super Game Agent — the Unity & Unreal for AI agents, with 100+ viral games to remix. Turn 20+ coding agents (Claude Code, Codex, DeepSeek, etc.) into a full-stack AI game studio. Build and publish 3D & mini-games to WeChat, Douyin, TikTok, Telegram, itch.io, and more.

`TypeScript` `agent-skills` `ai-agents` `ai-game-generator` `claude-code` `codex`

⭐ 2.9k • 🔱 446 • 47m ago

---

**[DIYgod/pinky](https://github.com/DIYgod/pinky)**

Let AI use your iPhone or Android phone, with you in the loop: any MCP agent from macOS, Windows or Linux, or Pinky itself, right on the phone.

`Go` `ai-agent` `android` `claude-code` `ios` `iphone`

⭐ 2.9k • 🔱 306 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
