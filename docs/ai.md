---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-17T18:24:13.714206+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 17, 2026 at 18:24 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 12h ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 22h ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

14h ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

23h ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 1d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

10h ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

14h ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

1d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

15h ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 9h ago

---

---

## Google News: "ai"

**[Aschenbrenner’s Situational Awareness made AI bets again before October rout](https://www.cnbc.com/2026/11/16/situational-awareness-aschenbrenner-new-ai-bets.html)**

Leopold Aschenbrenner's hedge fund, which almost collapsed over the summer, bought AI stocks before shares began tumbling.

CNBC • 19h ago

---

**[Can Google win the AI race without killing its cash cow? : Planet Money](https://www.npr.org/sections/planet-money/2026/11/17/g-s1-153933/can-google-win-the-ai-race-without-killing-its-cash-cow)**

In late October, Google had the worst stock day in its history as a public company. The Planet Money newsletter asks: has Google been caught in "the innovator's dilemma"?

NPR • 6h ago

---

**[Google: ‘The era of autonomous attacks has arrived’](https://thehill.com/policy/technology/6224604-autonomous-ai-threats-google-report/)**

The Hill • 2h ago

---

**[Google makes it easier to use Gemini without training AI on your data](https://arstechnica.com/ai/2026/11/google-will-let-you-opt-out-of-ai-training-in-gemini-without-losing-your-history/)**

AI training and chat history will now have separate toggles in the Gemini activity settings.

Ars Technica • 1h ago

---

**[The Fed seems to be getting worried about AI](https://finance.yahoo.com/economy/article/the-fed-seems-to-be-getting-worried-about-ai-110000457.html)**

Fed Chairman Kevin Warsh said that the potential for higher unemployment and the dangers of bad actors using AI for nefarious purposes could be "highly disruptive and economically costly."

Yahoo Finance • 7h ago

---

**[Tech leaders tell Fed chairman Warsh how AI could transform the economy](https://www.axios.com/2026/11/17/ai-fed-economic-growth-andreessen)**

Axios • 1h ago

---

**[Fed’s first close look at AI buildout finds $3 trillion of commitments off Big Tech’s balance sheets](https://fortune.com/2026/11/17/fed-financial-stability-report-ai-data-center-3-trillion-off-balance-sheet-nvidia/)**

Seven companies’ leases, contracts, and guarantees have grown faster than their debt. Nvidia reports earnings tonight without Jensen Huang.

Fortune • 24m ago

---

**[AI Is Making Solopreneurship More Accessible Than Ever—Here’s How](https://www.forbes.com/sites/aytekintank/2026/11/17/ai-is-making-solopreneurship-more-accessible-than-ever-heres-how/)**

Forbes • 1h ago

---

**[Opinion | What if There Is No A.I. Bubble?](https://www.nytimes.com/2026/11/17/opinion/ai-bubble-workers.html)**

The New York Times • 12h ago

---

**[Nvidia warns chip buyers of legal risks tied to China AI access, sources tell CNBC](https://www.cnbc.com/2026/11/17/nvidia-china-cloud-ai-chip-access.html)**

The U.S. Commerce Department is making moves to tighten export controls.

CNBC • 11h ago

---

---

## HackerNews: "ai"

**[All AI-generated code should be Open Source](https://news.ycombinator.com/item?id=50507303)**

All code generated with help from AI should be Open Source or on Creative Commons Zero (CC0) license.

⬆️ 1277 • 💬 665 • 2d ago • [Jakub T. Jankiewicz Blog](https://jakub.jankiewicz.org/blog/ai-code-open-source/)

---

**[United Airlines experiencing a widespread system outage, airline says](https://news.ycombinator.com/item?id=50524165)**

A widespread, yet short-lived, system outage at United Airlines on Monday delayed some outbound flights at US airports, the airline told CNN in a statement, coming on the heels of a rare FAA ground stop that caused massive disruption.

⬆️ 249 • 💬 131 • 20h ago • [CNN](https://www.cnn.com/2026/11/16/us/united-airlines-outage)

---

**[Baidu, Xiaomi CEOs warn of growing gap between AI hype and returns](https://news.ycombinator.com/item?id=50531751)**

⬆️ 167 • 💬 206 • 4h ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3374774/baidu-xiaomi-ceos-warn-growing-gap-between-ai-hype-and-returns)

---

**["Who is Hiring?" postings stuck near 12-year lows as AI reaches half of all jobs](https://news.ycombinator.com/item?id=50512950)**

Hacker News "Who is Hiring?" job postings sit near 12-year lows while AI appears in more than half of all postings. Most popular programming languages and technologies for November 2026.

⬆️ 94 • 💬 86 • 1d ago • [Hacker News Hiring Trends](https://www.hntrends.com/2026/november.html)

---

**[The Single Router in Southern Arkansas That Ground Air Travel to a Halt](https://news.ycombinator.com/item?id=50503588)**

⬆️ 89 • 💬 60 • 2d ago • [wsj.com](https://www.wsj.com/business/airlines/the-single-router-in-southern-arkansas-that-ground-air-travel-to-a-halt-eedc326c)

---

**[Ask HN: If AI tools are so good, why isn't your bug backlog empty?](https://news.ycombinator.com/item?id=50520076)**

⬆️ 81 • 💬 102 • 1d ago

---

**[Parents pay $75k for Alpha's AI school. Half of its students missed math target](https://news.ycombinator.com/item?id=50509953)**

Only 42% of Alpha students hit its 2x learning goal in math and reading, internal data show, as 2,600 public school students now use its software.

⬆️ 69 • 💬 67 • 1d ago • [Fortune](https://fortune.com/2026/11/14/alpha-school-ai-students-tuition-learning-goals/)

---

**[Caltech professor no longer grades homework's because everyone uses AI](https://news.ycombinator.com/item?id=50523022)**

I attended an introductory math class at Caltech, an elite STEM university in Pasadena, where the professor no longer grades homework.

⬆️ 48 • 💬 60 • 21h ago • [Business Insider](https://www.businessinsider.com/ai-math-class-university-homework-caltech-careers-2026-11)

---

**[United Airlines has a widespread system outage](https://news.ycombinator.com/item?id=50524260)**

⬆️ 48 • 💬 12 • 20h ago • [apnews.com](https://apnews.com/article/united-airlines-outage-5a5e5f75bb07f11ffb8750901f0076ff)

---

**[FBI says Artex AI open-source hacking tool used to breach networks](https://news.ycombinator.com/item?id=50520796)**

The FBI says that the open source hacking tool was used in cyberattacks targeting a U.S. IT giant and the South Korean financial industry.

⬆️ 47 • 💬 13 • 1d ago • [TechCrunch](https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/)

---

---

## YouTube Videos: "ai"

**[How to Make Studio-Quality AI Animation (Full Guide)](https://www.youtube.com/watch?v=_X7KQVwsn9U)**

Create your own AI animated films with OpenArt: https://tolt.link/jvsai Download my FREE AI Animation Skill: ...

📺 Jack Vs. AI

👁️ 153K • 👍 2K • 💬 102 • ⏱️ 18:33 • 2d ago

---

**[Jensen Huang: How to tell if AI will take your job #shorts](https://www.youtube.com/watch?v=cVoiIHB95jI)**

Jensen Huang says the way to judge AI's impact on a job is to separate its purpose from its tasks. Watching him, you might think ...

📺 The AI Takeaway

👁️ 592 • 👍 8 • 💬 1 • ⏱️ 0:52 • 1h ago

---

**[Snapchat AI Got Disqualified For Arguing 😭](https://www.youtube.com/watch?v=k_c9dsy5wMM)**

shorts #gothamchess #chess All credit to @GothamChess Full video: https://www.youtube.com/watch?v=CZGs4g_hVco&t=1229.

📺 Premove Clips

👁️ 50K • 👍 738 • 💬 3 • ⏱️ 0:22 • 1d ago

---

**[AI Just Hacked the Software That Runs the Internet](https://www.youtube.com/watch?v=m9KwBomAhqI)**

In one run, OpenAI's agents wrote 948 working attacks against Linux for about $1.2 million: roughly $1279 each, where a bug ...

📺 Jack Nyange

👁️ 13K • 👍 101 • 💬 11 • ⏱️ 12:04 • 1d ago

---

**[I Made 30-min Long AI Movie using my Avatar 🔥 100% FREE | Google Flow](https://www.youtube.com/watch?v=VJAp3eNETyU)**

I Made 30-min Long AI Movie using my Avatar 100% FREE | Google Flow Iss video me maine step-by-step sikhaya hai ki aap ...

📺 Everything For All

👁️ 5K • 👍 150 • 💬 30 • ⏱️ 15:46 • 11h ago

---

**[I brought a Pig Latin interpreter to an AI interview](https://www.youtube.com/watch?v=n4-lt4rxylg)**

I brought a Pig Latin interpreter to my AI job interview. Hellen was not prepared for this one. Victor came along to translate ...

📺 Bo Bongo

👁️ 409K • 👍 6K • 💬 1K • ⏱️ 13:03 • 1d ago

---

**[How I&#39;m Using AI Agents to Manage My Finances | Live Q&amp;A](https://www.youtube.com/watch?v=c1egSRpBwWk)**

Join the Newsletter. It's Free:* ...

📺 Rob Berger

👁️ 23K • 👍 533 • 💬 27 • ⏱️ 1:32:23 • 16h ago

---

**[AI HAS TAKEN OVER ROBLOX](https://www.youtube.com/watch?v=SAdOlLDNyio)**

AI HAS OFFICALLY TAKEN OVER ROLBLOX Become A Channel Member by pressing the 'JOIN' button next to subscribe to gain ...

📺 Alaska Violet

👁️ 206K • 👍 5K • 💬 644 • ⏱️ 17:02 • 23h ago

---

**[Ex Square Enix exec wants Valve to bend to AI](https://www.youtube.com/watch?v=vYJGAGHqtc8)**

https://starforgepc.com/LegendarydropsSF Thanks for watching! On this channel, you'll find long-form video essays about ...

📺 Legendary Drops

👁️ 166K • 👍 6K • 💬 446 • ⏱️ 0:52 • 2d ago

---

**[Business Documentary AI Se Kaise Banaye 🔥 | 10 Min Long AI Video Using Just 1 Prompt | AI Automation](https://www.youtube.com/watch?v=gsIA1cwofuU)**

Business Documentary AI Se Kaise Banaye | 10 Min Long AI Video Using Just 1 Prompt | AI Automation Register Now ...

📺 Invisible Gyan

👁️ 16K • 💬 59 • ⏱️ 19:00 • 6h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 727,110 • ❤️ 1,407 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,942,530 • ❤️ 20,383 • 10d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,828,071 • ❤️ 12,367 • 1mo ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 4,445 • ❤️ 484 • 4d ago

---

**[Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)**

*Thinking Machines Lab*

`image-text-to-text` `594.1B`

⬇️ 18,359 • ❤️ 434 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

`27.3B`

⬇️ 6,827,598 • ❤️ 6,124 • 5d ago

---

**[ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)**

*Zyphra*

`text-to-speech` `886.3M`

⬇️ 93,909 • ❤️ 505 • 3d ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 2,660,341 • ❤️ 515 • 6d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

`image-to-image`

⬇️ 1,062,051 • ❤️ 3,398 • 14d ago

---

**[sam3](https://huggingface.co/facebook/sam3)**

*AI at Meta*

`mask-generation` `859.9M`

⬇️ 1,971,023 • ❤️ 6,865 • 12mo ago

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

▲ 117 • 💬 4 • ⭐ 492 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 122,889 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 71 • 💬 4 • ⭐ 24,259 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 105 • 💬 2 • ⭐ 745 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

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

▲ 86 • 💬 7 • ⭐ 93,630 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 66 • 💬 5 • ⭐ 47,931 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 17.7k • 🔱 1.0k • 2d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 10.2k • 🔱 1.5k • 24m ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.0k • 🔱 2.0k • 50m ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.3k • 🔱 715 • 58m ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.2k • 🔱 1.8k • 13d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.0k • 🔱 749 • 14m ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 5.5k • 🔱 179 • 1h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.6k • 🔱 121 • 15m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.4k • 🔱 109 • 1d ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.6k • 🔱 241 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
