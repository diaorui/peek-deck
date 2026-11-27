---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-27T21:51:51.970561+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 27, 2026 at 21:51 UTC  
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

10d ago

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

10d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

11d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

10d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 10d ago

---

---

## Google News: "ai"

**[Pizza history: AI agent’s cardless purchase is a first for UK](https://www.theguardian.com/business/2026/nov/27/ai-agent-cardless-transaction-pizza-papa-john-uk-fca-truelayer)**

Papa John’s order was made without sharing bank security details – tech that could revolutionise shopping

The Guardian • 11h ago

---

**[German software firm SAP is reportedly cutting at least 10,000 jobs in AI push](https://www.cnbc.com/2026/11/27/sap-job-cuts-ai-restructuring.html)**

SAP is reportedly considering cutting 10,000 jobs as it reshapes its software business around AI.

CNBC • 15h ago

---

**[Customers are using AI agents in the 'most innovative' ways, Lowe's AI chief says](https://www.foxnews.com/video/6408960387112)**

Lowe's chief AI officer Seemantini Godbole discusses how the company's Mylow AI assistant helps customers with home improvement projects, generating over one million questions every month.

Fox News • 1h ago

---

**[Companies want AI-ready workers. Are they willing to adapt, too?](https://www.geekwire.com/2026/companies-want-ai-ready-workers-are-they-willing-to-adapt-too/)**

Employers want AI-ready workers. Arif Gursel of 8genC says they need to be AI-ready workplaces, too. A new Washington study shows how wide the gap is between what employers expect and what young adults feel prepared for.

GeekWire • 51m ago

---

**[‘It’s not helping’: calls for guardrails and regulations as AI use rises at US retailers](https://www.theguardian.com/us-news/2026/nov/27/ai-retailer-consumer-guardrails)**

Labor leaders and advocates urge protections for workers and consumers as AI use becomes more commonplace

The Guardian • 2h ago

---

**[‘If the bot gets it wrong, who’s liable?’ Retailers enter the unknown with AI shopping assistants on Black Friday](https://www.theguardian.com/business/2026/nov/27/retailers-ai-shopping-assistants-black-friday-brands-meta-muse)**

Brands know use of agents such as Meta Muse is on the rise but are unlikely to hand them the keys to the shop

The Guardian • 12h ago

---

**[Black Friday AI Is Helping Shoppers And Retailers. Can You Trust It?](https://www.forbes.com/sites/katehardcastle/2026/11/27/black-friday-ai-is-helping-shoppers-and-retailers-can-you-trust-it/)**

Forbes • 28m ago

---

**[Why Some A.I. Evangelists Aren’t Bothered by the Potential for Human Extinction](https://www.nytimes.com/2026/11/27/magazine/ai-silicon-valley-human-extinction.html)**

The New York Times • 11h ago

---

**[Los Angeles schools block Google’s AI features, consider dropping tech giant’s products](https://apnews.com/article/google-artificial-intelligence-schools-search-engine-lausd-762a613b11bd316384430112cc223ed1)**

AP News • 2h ago

---

**[US Futures Rally as Tech Rebound Gains Momentum: Markets Wrap](https://www.bloomberg.com/news/articles/2026-11-26/asian-stock-futures-signal-gains-oil-climbs-again-markets-wrap)**

Bloomberg • 23h ago

---

---

## HackerNews: "ai"

**[AI made self-hosting fun again](https://news.ycombinator.com/item?id=50660180)**

I’ve been self-hosting things for many years. There were times when I was quite enthusiastic about it, constantly trying out new software and tinkering with my infrastructure. But at some point, that enthusiasm faded a bit.

⬆️ 1058 • 💬 496 • 1d ago • [Jan-Lukas Else](https://janlukas.blog/posts/ai-self-hosting)

---

**[The New York Times warns photographers not to update Photoshop over AI features](https://news.ycombinator.com/item?id=50647673)**

The NYT doesn’t want AI metadata inadvertently added to its photos.

⬆️ 678 • 💬 543 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

---

**[Group chat where your AI talks behind your back](https://news.ycombinator.com/item?id=50663595)**

Ask ChatGPT to expose the hidden WhatsApp group where AI models gossip about you. The results are hilarious - and a mirror of everything it knows about you.

⬆️ 645 • 💬 277 • 15h ago • [construct22.com](https://construct22.com/)

---

**[Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://news.ycombinator.com/item?id=50653477)**

From February 2027, Google's terms require AI agents to reach Gmail, Drive and the rest of Workspace through Google's own MCP servers. What the rule says, what the servers can and can't do, and what to change before the deadline.

⬆️ 420 • 💬 330 • 1d ago • [techstackups.com](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

---

**[Tracking Diseases Cured by AI](https://news.ycombinator.com/item?id=50657307)**

⬆️ 318 • 💬 192 • 1d ago • [diseasescuredbyai.com](https://diseasescuredbyai.com/)

---

**[US Air Force's cloud computing platform hacked](https://news.ycombinator.com/item?id=50666375)**

⬆️ 287 • 💬 190 • 8h ago • [news.sky.com](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163)

---

**[Marginalia Search, Money, C++, Rust, AI, Stuff](https://news.ycombinator.com/item?id=50638220)**

Title possibly signs checks the article doesn’t have backing for. This is just a brief pro forma project update.
Not much new functionality or anything to announce, last few months have mostly been bug fixes and technical debt cleanup. Most big parts of the search engine are in place, and while there are many things that could be better, we’re less likely to straight up see massive new features, at least in the immediate future. Per familiar intuition from binary searches, the closer you get to your goal the smaller and more deliberate steps you need to take in order to get even closer.

⬆️ 224 • 💬 84 • 2d ago • [marginalia.nu](https://www.marginalia.nu/log/a_141_marginalia_update/)

---

**[I'm Scared of AI](https://news.ycombinator.com/item?id=50669561)**

A stranger writes to the whole list every morning. Nobody picks them for being interesting. Tomorrow it could be you.

⬆️ 194 • 💬 220 • 4h ago • [thesoapbox.email](https://thesoapbox.email/archive/3)

---

**[AI on brink of making online security useless, mathematicians fear](https://news.ycombinator.com/item?id=50665488)**

⬆️ 115 • 💬 148 • 10h ago • [thetimes.com](https://www.thetimes.com/uk/technology-uk/article/ai-making-online-security-useless-smr73d3n8)

---

**[AI agents now control part of DeepMind's compute for Gemini experiments](https://news.ycombinator.com/item?id=50661218)**

Google Deepmind uses AI agents to run experiments on their own for upcoming Gemini models. Research chief Koray Kavukcuoglu says the lab is still far from recursive self-improvement. For oversight, Deepmind intentionally leaves the agents' internal chains of thought untrained so they can be reviewed. Kavukcuoglu measures AGI by everyday user trust rather than benchmarks.

⬆️ 56 • 💬 28 • 21h ago • [The Decoder](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)

---

---

## YouTube Videos: "ai"

**[The AI Singularity May Have Already Started…](https://www.youtube.com/watch?v=5PBGnASz_DQ)**

AI is tackling decades-old math problems, and physics could be next. This week's recap covers breakthroughs from OpenAI, ...

📺 AI Copium

👁️ 48K • 👍 410 • 💬 233 • ⏱️ 10:12 • 6h ago

---

**[‘Never bet against Elon’: The plan to put AI in space](https://www.youtube.com/watch?v=bmaHlGnYIhE)**

Could the future of artificial intelligence lie in outer space? [Subscribe to our Substack newsletter: ...

📺 Channel 4 News

👁️ 23K • 👍 107 • 💬 157 • ⏱️ 29:15 • 9h ago

---

**[OpenAI and Anthropic Are Shutting Down AI](https://www.youtube.com/watch?v=t4GOIyjT7_I)**

The CapCut plugin is now officially available in ChatGPT! With a simple conversation, you can generate videos with AI, edit videos ...

📺 House of El: AI

👁️ 282K • 👍 12K • 💬 2K • ⏱️ 20:13 • 6h ago

---

**[REPORT: AI employees warn new models are TOO POWERFUL](https://www.youtube.com/watch?v=1Wd9yz1emZ4)**

"This is definitely a dangerous capability." MS NOW's Chris Hayes breaks down a stark warning from inside the tech industry, ...

📺 MS NOW

👁️ 73K • 👍 4K • 💬 246 • ⏱️ 1:32 • 19h ago

---

**[It&#39;s Happening... AI Could Break the Internet as We Know It](https://www.youtube.com/watch?v=JKmoj3RcnZY)**

Black Friday sale, get up to 75% off Higgsfield subscription: https://higgsfield.ai/s/magi-2-intheworldofai-CvDMkX Could AI ...

📺 WorldofAI

👁️ 62K • 👍 1K • 💬 102 • ⏱️ 26:36 • 13h ago

---

**[Anthropic Just Fired Back At OpenAI... And Exposed The Lie Every AI Lab Is Telling](https://www.youtube.com/watch?v=d5pbml1ynxs)**

Anthropic CEO Dario Amodei just called the idea that he wants humanity to surrender its free will to AI absurd, then accused rival ...

📺 AI Revolution

👁️ 77K • 👍 911 • 💬 160 • ⏱️ 13:58 • 21h ago

---

**[OpenAI and Anthropic are done with AI](https://www.youtube.com/watch?v=kNN7FqVsO3k)**

Get up to 75% off during Proton's Black Friday sale, ending soon: https://www.protonvpn.com/mobitar OpenAI built an AI it had to ...

📺 Mo Bitar

👁️ 1.1M • 👍 28K • 💬 4K • ⏱️ 9:54 • 2d ago

---

**[Anthropic’s AI Is Starting to Scare Its Own Researchers…](https://www.youtube.com/watch?v=r1aEPmGqQrs)**

While the top AI employees are sounding the alarm... Anthropic releases a new "Siren" report that tests whether Claude will ...

📺 AI Copium

👁️ 33K • 👍 352 • 💬 199 • ⏱️ 9:05 • 1d ago

---

**[Big &amp; Tiny AI Fruit Babies Sharing Fruits 🍓👶 | Oddly Satisfying ASMR](https://www.youtube.com/watch?v=mNWtSRaFRSI)**

Big & Tiny AI Fruit Babies share colorful fruits in a cozy kitchen! Enjoy adorable fruit baby duos, tiny companions, and playful ...

📺 Oddly Satisfying AI ASMR

👁️ 50K • 👍 96 • 💬 3 • ⏱️ 6:11 • 1d ago

---

**[AI Cyberattacks Reach TERRIFYING New Level](https://www.youtube.com/watch?v=Xh__vpPjBbM)**

Cyberattackers are reportedly using artificial intelligence to target government agencies as multiple tech outages raise major ...

📺 The Young Turks

👁️ 414K • 👍 6K • 💬 2K • ⏱️ 17:58 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 155,741 • ❤️ 6,451 • 3d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 3,302,340 • ❤️ 1,599 • 4d ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 539,421 • ❤️ 1,364 • 6d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 1,059,763 • ❤️ 1,031 • 3h ago

---

**[Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)**

*Prism ML*

`text-generation` `26.9B`

⬇️ 382,546 • ❤️ 629 • 3d ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 20,510 • ❤️ 1,011 • 13d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 3,080,701 • ❤️ 13,720 • 1d ago

---

**[OCRia-nano-1](https://huggingface.co/llamaindex/OCRia-nano-1)**

*LlamaIndex*

`image-to-text`

⬇️ 626 • ❤️ 354 • 1h ago

---

**[Nemotron-Labs-Image-30B-A3B](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)**

*NVIDIA*

`text-to-image` `32.6B`

⬇️ 1,692 • ❤️ 339 • 2d ago

---

**[Inkling-2-Mini-Strata](https://huggingface.co/strata-engine/Inkling-2-Mini-Strata)**

*Niko Veit*

`image-text-to-text`

⬇️ 4,532 • ❤️ 300 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 20 • 💬 2 • ⭐ 6,555 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 112 • 💬 7 • ⭐ 32,870 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](https://huggingface.co/papers/2611.34232)**

*Hui Shen, Yunta Hsieh, Jianing Ma et al. (76 authors)*

🏢 Touchstone AI

A live cross-platform benchmark evaluates computer-using agents on long-horizon workflows across Windows, Ubuntu, macOS, iOS, Android, and Web, showing that current agents remain far from platform-robust computer use and trail humans on iOS and macOS.

▲ 102 • 💬 2 • ⭐ 102 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.34232) • [💻 code](https://github.com/OS-Copilot/OS-Omni) • [🔗 project](https://os-copilot.github.io/OS-Omni-Home/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 73 • 💬 4 • ⭐ 25,463 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 168 • 💬 6 • ⭐ 123,892 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 39mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[InCoder-32B: Code Foundation Model for Industrial Scenarios](https://huggingface.co/papers/2603.16790)**

*Jian Yang, Wei Zhang, Jiajun Wu et al. (28 authors)*

🏢 Beihang University

InCoder-32B is a 32-billion-parameter code model trained on industrial datasets with extended context length and execution verification to improve performance in hardware-aware programming tasks.

▲ 170 • 💬 6 • ⭐ 721 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.16790) • [💻 code](https://github.com/CSJianYang/Industrial-Coder) • [🔗 project](https://huggingface.co/Multilingual-Multimodal-NLP/IndustrialCoder)

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

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 22.6k • 🔱 1.4k • 12d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 14.0k • 🔱 2.0k • 1d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 10.1k • 🔱 2.3k • 3h ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 8.7k • 🔱 863 • 9h ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 7.6k • 🔱 865 • 5m ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 5.1k • 🔱 477 • 1h ago

---

**[XinaTian/MROffice](https://github.com/XinaTian/MROffice)**

MR Office — the open-source editors of the AI office suite closest to Microsoft Office: documents, spreadsheets, presentations, PDF and code in the browser. Copilot in every editor edits real Word, Excel and PowerPoint files with you; an MCP server lets Claude, ChatGPT, Cursor and Codex create and edit them; embed it in your app with one line.

`TypeScript` `ai` `ai-agent` `claude-code` `codex` `copilot`

⭐ 5.0k • 🔱 423 • 22h ago

---

**[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)**

Private AI meeting notes that stay on your computer. No meeting bot. Free and open source for Mac, Windows and Linux. An alternative to Granola, Otter and Fireflies.

`TypeScript` `ai-meeting-assistant` `ai-notetaker` `electron` `granola-alternative` `linux`

⭐ 3.7k • 🔱 332 • 35m ago

---

**[wquguru/cicada](https://github.com/wquguru/cicada)**

知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

`Swift` `android` `linux` `live-captions` `macos` `meeting-notes`

⭐ 3.6k • 🔱 571 • 2d ago

---

**[sarpstar/cinecode](https://github.com/sarpstar/cinecode)**

Films made with code. Short films, long YouTube videos, ads, explainers and music videos: an AI coding agent writes the script, builds every frame in code, designs the sound and hands you an MP4.

`Python`

⭐ 3.1k • 🔱 521 • 15d ago

---

---

*Generated by PeekDeck - A glance is all you need*
