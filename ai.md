---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-25T18:46:09.112690+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 25, 2026 at 18:46 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 8d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 8d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

8d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

8d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 9d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

8d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

8d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

9d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

8d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 8d ago

---

---

## Google News: "ai"

**[Stock Sell-Off Continues as Investors Fret About A.I., Tariffs and Inflation](https://www.nytimes.com/2026/11/25/business/stocks-sp500-nvidia-ai.html)**

The New York Times • 6h ago

---

**[Nvidia sellers seek new buyers as U.S. curbs China AI chip access, sources tell CNBC](https://www.cnbc.com/2026/11/25/nvidia-china-ai-chip-remote-access.html)**

Nvidia GPU sellers are seeking new buyers after new U.S. rules tightened remote access to advanced AI chips for China-linked customers

CNBC • 1h ago

---

**[AI debt worries grow as Nvidia rebound masks Big Tech spending squeeze](https://www.cnbc.com/2026/11/25/ai-debt-big-tech-spending-nvidia.html)**

Big Tech could find it increasingly tough to secure funding from debt markets critical to the AI build-out, as lenders become pickier over corporate bonds.

CNBC • 12h ago

---

**[This Is When AI’s Circular Deals Bite Back](https://www.bloomberg.com/news/newsletters/2026-11-25/the-us-stock-selloff-is-unravelling-the-ai-trade-s-circular-deals)**

Bloomberg.com • 1h ago

---

**[Iran War Updates: Tehran denounces U.S. for using AI in strikes it claims violate international law](https://www.cbsnews.com/live-updates/iran-war-us-military-ai-weapons-oil/)**

Iran's U.N. envoy claims the U.S. military used Palantir and Anthropic AI systems to select some 2,000 targets over just four days.

CBS News • 39m ago

---

**[AI agents promise to transform work. Big Tech wants to collect the tolls.](https://www.businessinsider.com/google-ai-agent-access-limits-fees-gmail-drive-microsoft-copilot-2026-11)**

Google's new AI agent access limits could raise costs for OpenAI, Anthropic, and other companies building workplace agents.

Business Insider • 33m ago

---

**[Are you getting ‘housefished’ by AI in real estate listings?](https://www.boston.com/real-estate/home-buying/2026/11/25/ai-real-estate-listings-massachusetts-new-york-housefishing/)**

New York is considering legally requiring AI disclosures in real estate listings. Should Massachusetts do the same?

Boston.com • 46m ago

---

**[What to know before using AI agents for Black Friday shopping](https://www.npr.org/2026/11/25/nx-s1-6048524/what-to-know-before-using-ai-agents-for-black-friday-shopping)**

59% of U.S. shoppers plan to use AI for holiday shopping this weekend, according to the National Retail Federation

NPR • 4h ago

---

**[Scoop: Anthropic and OpenAI employees fear unreleased AI models are too unsafe to release](https://www.axios.com/2026/11/24/anthropic-openai-unreleased-ai-safety-risks)**

Axios • 1d ago

---

**[Tidal bans 100% AI-generated music with plans to delete more than 27m tracks](https://www.theguardian.com/music/2026/nov/25/tidal-streaming-service-bans-ai-generated-music)**

Streaming service says 43% of uploads to platform in past 90 days were made entirely by artificial intelligence

The Guardian • 16h ago

---

---

## HackerNews: "ai"

**[A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://news.ycombinator.com/item?id=50603845)**

We have AI at home! Set up your own free personal ChatGPT on your PC with Unsloth and Inkling or Qwen. It's private, and the whole house can use it.

⬆️ 775 • 💬 316 • 2d ago • [gpupartner.com](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

---

**[Tidal bans AI-generated music](https://news.ycombinator.com/item?id=50630309)**

The music streaming service Tidal said Tuesday that it would ban tracks it believes are completely AI-generated starting next month,

⬆️ 334 • 💬 325 • 1d ago • [Variety](https://variety.com/2026/music/news/tidal-bans-ai-generated-music-1236956924/)

---

**[Marginalia Search, Money, C++, Rust, AI, Stuff](https://news.ycombinator.com/item?id=50638220)**

Title possibly signs checks the article doesn’t have backing for. This is just a brief pro forma project update.
Not much new functionality or anything to announce, last few months have mostly been bug fixes and technical debt cleanup. Most big parts of the search engine are in place, and while there are many things that could be better, we’re less likely to straight up see massive new features, at least in the immediate future. Per familiar intuition from binary searches, the closer you get to your goal the smaller and more deliberate steps you need to take in order to get even closer.

⬆️ 207 • 💬 78 • 14h ago • [marginalia.nu](https://www.marginalia.nu/log/a_141_marginalia_update/)

---

**[Declare is a UI language for you and your AI](https://news.ycombinator.com/item?id=50622854)**

Designed from the ground up for interfaces that act and move like the best native apps, in a few hundred lines your AI can write and its compiler can check.

⬆️ 114 • 💬 94 • 1d ago • [Declare](https://davidtemkin.github.io/declarelang/)

---

**[Working with AI](https://news.ycombinator.com/item?id=50634734)**

We interviewed people at 58 companies that use Claude about how AI is changing their work. They described few layoffs but reduced hiring, and said the most valuable uses of AI often involved reorganizing roles and workplaces around it.

⬆️ 81 • 💬 74 • 21h ago • [anthropic.com](https://www.anthropic.com/research/working-with-ai)

---

**[Jevons Paradox in AI: Cheaper Tokens Won't Pay for Capex](https://news.ycombinator.com/item?id=50625888)**

Google processes 330 times more tokens than two years ago, yet prices fall almost as fast. Why the Jevons paradox alone won't pay for $560 billion of AI capex.

⬆️ 81 • 💬 40 • 1d ago • [Philipp D. Dubach](https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/)

---

**[Amodei reportedly suggested games could pacify masses after AI took their jobs (2015)](https://news.ycombinator.com/item?id=50610830)**

A profile of Dario and Daniela Amodei, published in the Wall Street Journal following Anthropic’s record-breaking IPO, includes an anecdote in which Dario seems to acknowledge the world-destabilizing potential of AI, then suggests a particularly dystopian solution:
> There, he engaged in debates with his fellow employees, suggesting that immersive video games might be a solution for the political strife caused by AI-induced joblessness, according to widely circulated Slack messages.

⬆️ 79 • 💬 85 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1039745/dario-amodei-video-games-ai-joblessness)

---

**[0rwx – A simple model of AI usage, inspired by Unix permissions](https://news.ycombinator.com/item?id=50605445)**

A simple model of AI usage, inspired by unix permissions.

⬆️ 71 • 💬 17 • 2d ago • [0rwx.com](https://0rwx.com/)

---

**[Quit Internet Videos Before AI Perfects Them](https://news.ycombinator.com/item?id=50627131)**

⬆️ 36 • 💬 18 • 1d ago • [nomagicpill.substack.com](https://nomagicpill.substack.com/p/quit-internet-videos-before-ai-perfects)

---

**[Buckle Up the AI Bubble Is Popping](https://news.ycombinator.com/item?id=50614037)**

⬆️ 34 • 💬 58 • 2d ago • [mathbabe.org](https://mathbabe.org/2026/11/23/buckle-up-the-ai-bubble-is-popping/)

---

---

## YouTube Videos: "ai"

**[OpenAI insider: An AI accident is the most likely way people will die](https://www.youtube.com/watch?v=qgL_IbP2qKg)**

OpenAI Board Member Paul Christiano details a warning: within the next one to three years, there is a high risk of an artificial ...

📺 CNN

👁️ 1.1M • 👍 5K • 💬 3K • ⏱️ 21:55 • 1d ago

---

**[‘A TERRIFYING picture’: AI employees warn some advanced models are NOT SAFE to release, AXIOS](https://www.youtube.com/watch?v=ak5kr5yM7aI)**

AXIOS senior AI reporter Madison Mills joins Way Too Early to discuss her latest piece titled, 'AI employees sound alarm: models ...

📺 MS NOW

👁️ 159K • 👍 1K • 💬 515 • ⏱️ 6:01 • 1d ago

---

**[The “Godfather of AI” on the Risks That Worry Him Most | Geoffrey Hinton | TED](https://www.youtube.com/watch?v=L8HdlknRkA4)**

Geoffrey Hinton helped create the neural networks behind today's AI, won a Nobel Prize for it — and has spent the years since ...

📺 TED

👁️ 233K • 👍 2K • 💬 300 • ⏱️ 25:55 • 1d ago

---

**[OpenAI Declares War On Self-Improving AI... Something Is Wrong](https://www.youtube.com/watch?v=HbosmW-RS-U)**

OpenAI just revealed the private scale it uses to measure AI intelligence, and its chief scientist warns self-improving AI could ...

📺 AI Revolution

👁️ 84K • 👍 972 • 💬 191 • ⏱️ 15:40 • 1d ago

---

**[Anthropic&#39;s Engineers Stopped Building AI Agents (Here&#39;s What They Build Instead)](https://www.youtube.com/watch?v=IMSYKloMFrE)**

Get the Claude Skills Guide for free ...

📺 Jay E | RoboNuggets

👁️ 600K • 👍 8K • 💬 239 • ⏱️ 16:34 • 1d ago

---

**[OpenAI and Anthropic are done with AI](https://www.youtube.com/watch?v=kNN7FqVsO3k)**

Get up to 75% off during Proton's Black Friday sale, ending soon: https://www.protonvpn.com/mobitar OpenAI built an AI it had to ...

📺 Mo Bitar

👁️ 374K • 👍 12K • 💬 2K • ⏱️ 9:54 • 7h ago

---

**[Yes, you should panic about AI](https://www.youtube.com/watch?v=VCg2RlsPxBU)**

For ten years, a small group of experts has been saying insane things about AI. And for ten years, they've been proven right.

📺 Rutger Bregman

👁️ 239K • 👍 5K • 💬 2K • ⏱️ 12:40 • 2d ago

---

**[AI Cyberattacks Reach TERRIFYING New Level](https://www.youtube.com/watch?v=Xh__vpPjBbM)**

Cyberattackers are reportedly using artificial intelligence to target government agencies as multiple tech outages raise major ...

📺 The Young Turks

👁️ 336K • 👍 5K • 💬 2K • ⏱️ 17:58 • 14h ago

---

**[n8n Just Dropped a FREE AI Agent. OpenAI Didn&#39;t See It Coming](https://www.youtube.com/watch?v=mPZS1cn--bs)**

Run Nod 24/7 on Hostinger, the server we used: https://www.hostg.xyz/SHKPW Use code STAYINGAHEAD for an extra 10% off.

📺 Vaibhav Sisinty

👁️ 12K • 👍 388 • 💬 22 • ⏱️ 17:04 • 3h ago

---

**[The REAL Reason AI Drones Are Coming For Everyone](https://www.youtube.com/watch?v=dMJuwtypCyY)**

Former Google X Chief Business Officer Mo Gawdat believes the biggest danger of artificial intelligence isn't job losses or ...

📺 The Diary Of A CEO Clips

👁️ 135K • 👍 1K • 💬 106 • ⏱️ 14:02 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 96,527 • ❤️ 5,949 • 1d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 2,445,633 • ❤️ 1,332 • 2d ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 15,244 • ❤️ 864 • 11d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 762,491 • ❤️ 811 • 1d ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 189,735 • ❤️ 1,008 • 4d ago

---

**[Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)**

*Prism ML*

`text-generation` `26.9B`

⬇️ 59,366 • ❤️ 276 • 21h ago

---

**[DepthPro2](https://huggingface.co/apple/DepthPro2)**

*Apple*

`depth-estimation`

⬇️ 0 • ❤️ 1,220 • 5d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 3,844 • ❤️ 1,089 • 1d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 10,026 • ❤️ 991 • 12d ago

---

**[OCRia-nano-1](https://huggingface.co/llamaindex/OCRia-nano-1)**

*LlamaIndex*

`image-to-text`

⬇️ 126 • ❤️ 207 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 17 • 💬 0 • ⭐ 6,342 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 111 • 💬 7 • ⭐ 32,750 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 40 • 💬 3 • ⭐ 723 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 71 • 💬 4 • ⭐ 25,118 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 165 • 💬 4 • ⭐ 1,517 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,738 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://huggingface.co/papers/2611.31201)**

*Xiao-Ming Wu, Kang Liao, Yuexiao Ma et al. (15 authors)*

🏢 MMLab@NTU

A systematic framework shows that frontier multimodal models can serve as robot policies when harnessed with interfaces favoring native visual reasoning and tool use, achieving high success in simulated and real manipulation tasks.

▲ 103 • 💬 2 • ⭐ 65 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2611.31201) • [💻 code](https://github.com/DravenALG/Embo-Harness) • [🔗 project](https://dravenalg.github.io/projects/Embo-Harness/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 8,097 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 94,311 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 39mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 21.7k • 🔱 1.3k • 10d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 13.3k • 🔱 1.9k • 9h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 10.0k • 🔱 2.2k • 8h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 9.2k • 🔱 2.4k • 9h ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 8.1k • 🔱 732 • 1h ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 6.4k • 🔱 764 • 2m ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 5.1k • 🔱 160 • 5m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 120 • 1d ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 4.6k • 🔱 434 • 48s ago

---

**[XinaTian/MROffice](https://github.com/XinaTian/MROffice)**

MR Office — the open-source editors of the AI office suite closest to Microsoft Office: documents, spreadsheets, presentations, PDF and code in the browser. Copilot in every editor edits real Word, Excel and PowerPoint files with you; an MCP server lets Claude, ChatGPT, Cursor and Codex create and edit them; embed it in your app with one line.

`TypeScript` `ai` `ai-agent` `claude-code` `codex` `copilot`

⭐ 4.5k • 🔱 475 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
