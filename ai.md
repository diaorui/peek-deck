---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-27T03:05:20.097159+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 27, 2026 at 03:05 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 9d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 10d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

9d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

10d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 10d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

9d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

9d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

10d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

10d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 9d ago

---

---

## Google News: "ai"

**[SAP Weighs Cutting at Least 10,000 Positions in AI Restructuring](https://www.bloomberg.com/news/articles/2026-11-26/sap-weighs-cutting-at-least-10-000-positions-in-ai-restructuring)**

Bloomberg.com • 10h ago

---

**[SAP considers at least 10,000 job cuts in AI restructuring, Bloomberg reports](https://www.reuters.com/technology/sap-considers-least-10000-job-cuts-ai-restructuring-bloomberg-reports-2026-11-26/)**

Reuters • 10h ago

---

**[SAP looks to cut another 10,000 jobs in new AI-driven restructuring](https://www.calcalistech.com/ctechnews/article/al8iwkfjx)**

The reported layoffs would mark a second major workforce overhaul in less than three years. SAP is seeking to reorganize product development and sales around AI while protecting its growth in cloud software.

CTech • 8h ago

---

**[EXCLUSIVE: US chip curbs, distillation crackdown threaten Chinese AI model development, sources say](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/)**

Reuters • 19h ago

---

**[AI boom fuels demand for commercial and industrial space: JLL](https://www.cnbc.com/video/2026/11/27/industrial-remains-the-worldas-top-performing-asset-class.html)**

JLL's Christian Ulbrich says commercial real estate demand is robust, with office leasing rising on steady GDP growth and AI companies among the strongest drivers. He says industrial space is also in strong demand, driven by data center buildout, but access to grid power is the main constraint on new data centers.

CNBC • 59m ago

---

**[The AI Boom Looks Alive and Well in Asia](https://www.wsj.com/tech/ai/the-ai-boom-looks-alive-and-well-in-asia-59841697)**

WSJ • 5m ago

---

**[New book warns leadership crisis grows as AI changes offices](https://foxbaltimore.com/news/local/new-book-warns-leadership-crisis-grows-as-ai-changes-offices)**

Artificial intelligence is quickly changing how people work in all kinds of businesses, but two leadership experts, Christian Anschuetz and Luis Serpa, believe there's a bigger issue than just keeping up with technology.

WBFF • 40m ago

---

**[US authorizes SpaceX to deploy 1 million satellites for AI data centers in space](https://www.cnn.com/2026/11/26/business/spacex-satellites-space-data-centers-intl)**

The technology is central to SpaceX’s growth ambitions, though the company warned earlier this year that it relied on “unproven” technologies.

CNN • 14h ago

---

**[Musk pledges two SpaceX shares for every US child in $18 billion AI charm offensive](https://www.reuters.com/business/media-telecom/musk-says-every-child-us-will-get-two-spacex-shares-2026-11-26/)**

Reuters • 22h ago

---

**[Can Elon Musk really put AI datacentres in space? - The Latest](https://www.theguardian.com/news/video/2026/nov/26/can-elon-musk-really-put-ai-datacentres-in-space-the-latest)**

The Trump administration has approved Elon Musk’s plan to launch one million satellites into orbit to create datacentres in space. SpaceX argues the project could reduce the impact of datacentres on Earth as the AI industry grows. But how realistic is the plan and what could the consequences be? Michael Safi speaks to Guardian global technology editor Dan Milmo

The Guardian • 8h ago

---

---

## HackerNews: "ai"

**[The New York Times warns photographers not to update Photoshop over AI features](https://news.ycombinator.com/item?id=50647673)**

The NYT doesn’t want AI metadata inadvertently added to its photos.

⬆️ 656 • 💬 522 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

---

**[AI made self-hosting fun again](https://news.ycombinator.com/item?id=50660180)**

I’ve been self-hosting things for many years. There were times when I was quite enthusiastic about it, constantly trying out new software and tinkering with my infrastructure. But at some point, that enthusiasm faded a bit.

⬆️ 368 • 💬 205 • 5h ago • [Jan-Lukas Else](https://janlukas.blog/posts/ai-self-hosting)

---

**[Tidal bans AI-generated music](https://news.ycombinator.com/item?id=50630309)**

The music streaming service Tidal said Tuesday that it would ban tracks it believes are completely AI-generated starting next month,

⬆️ 337 • 💬 344 • 2d ago • [Variety](https://variety.com/2026/music/news/tidal-bans-ai-generated-music-1236956924/)

---

**[Tracking Diseases Cured by AI](https://news.ycombinator.com/item?id=50657307)**

⬆️ 305 • 💬 182 • 9h ago • [diseasescuredbyai.com](https://diseasescuredbyai.com/)

---

**[Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://news.ycombinator.com/item?id=50653477)**

From February 2027, Google's terms require AI agents to reach Gmail, Drive and the rest of Workspace through Google's own MCP servers. What the rule says, what the servers can and can't do, and what to change before the deadline.

⬆️ 260 • 💬 220 • 17h ago • [techstackups.com](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

---

**[Marginalia Search, Money, C++, Rust, AI, Stuff](https://news.ycombinator.com/item?id=50638220)**

Title possibly signs checks the article doesn’t have backing for. This is just a brief pro forma project update.
Not much new functionality or anything to announce, last few months have mostly been bug fixes and technical debt cleanup. Most big parts of the search engine are in place, and while there are many things that could be better, we’re less likely to straight up see massive new features, at least in the immediate future. Per familiar intuition from binary searches, the closer you get to your goal the smaller and more deliberate steps you need to take in order to get even closer.

⬆️ 223 • 💬 85 • 1d ago • [marginalia.nu](https://www.marginalia.nu/log/a_141_marginalia_update/)

---

**[Working with AI](https://news.ycombinator.com/item?id=50634734)**

We interviewed people at 58 companies that use Claude about how AI is changing their work. They described few layoffs but reduced hiring, and said the most valuable uses of AI often involved reorganizing roles and workplaces around it.

⬆️ 89 • 💬 77 • 2d ago • [anthropic.com](https://www.anthropic.com/research/working-with-ai)

---

**[Jevons Paradox in AI: Cheaper Tokens Won't Pay for Capex](https://news.ycombinator.com/item?id=50625888)**

Google processes 330 times more tokens than two years ago, yet prices fall almost as fast. Why the Jevons paradox alone won't pay for $560 billion of AI capex.

⬆️ 82 • 💬 40 • 2d ago • [Philipp D. Dubach](https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/)

---

**[New York bans AI toys, including those using internet to talk to children](https://news.ycombinator.com/item?id=50644909)**

The state attorney general says she would ‘not hesitate to enforce’ the five-year ban signed by Governor Kathy Hochul

⬆️ 55 • 💬 14 • 1d ago • [the Guardian](https://www.theguardian.com/us-news/2026/nov/25/new-york-bans-ai-toys)

---

**[Quit Internet Videos Before AI Perfects Them](https://news.ycombinator.com/item?id=50627131)**

⬆️ 39 • 💬 18 • 2d ago • [nomagicpill.substack.com](https://nomagicpill.substack.com/p/quit-internet-videos-before-ai-perfects)

---

---

## YouTube Videos: "ai"

**[Anthropic’s AI Is Starting to Scare Its Own Researchers…](https://www.youtube.com/watch?v=r1aEPmGqQrs)**

While the top AI employees are sounding the alarm... Anthropic releases a new "Siren" report that tests whether Claude will ...

📺 AI Copium

👁️ 25K • 👍 288 • 💬 182 • ⏱️ 9:05 • 12h ago

---

**[China&#39;s Fall In The AI Race Is Worse Than We Thought | VisualEconomik EN](https://www.youtube.com/watch?v=it6DM4-vZQw)**

Get an early access to Proton's Black Friday sale at https://protonvpn.com/visualeconomik and get up to 75% off on their VPN ...

📺 VisualEconomik EN

👁️ 56K • 👍 1K • 💬 174 • ⏱️ 14:19 • 14h ago

---

**[The Most Productive Hour You’ll Spend on AI, Its Dangers, and Potential Solutions | Geoffrey Hinton](https://www.youtube.com/watch?v=KPELRl6y7vY)**

Known as the “Godfather of AI,” Professor Geoffrey Hinton won a Nobel Prize for work that helped lay the foundation for the AI ...

📺 Sinead Bovell

👁️ 62K • 👍 1K • 💬 209 • ⏱️ 1:00:15 • 2d ago

---

**[AI Is Changing FAST (15 Wild New Breakthroughs)](https://www.youtube.com/watch?v=PsKKvsnvN-o)**

15 AI breakthroughs this week: Genie 4, Kling Image 4.0, Pika Enact and more. Try HeyGen: ...

📺 AI Samson

👁️ 32K • 👍 526 • 💬 36 • ⏱️ 20:36 • 1d ago

---

**[OpenAI and Anthropic are done with AI](https://www.youtube.com/watch?v=kNN7FqVsO3k)**

Get up to 75% off during Proton's Black Friday sale, ending soon: https://www.protonvpn.com/mobitar OpenAI built an AI it had to ...

📺 Mo Bitar

👁️ 996K • 👍 25K • 💬 4K • ⏱️ 9:54 • 1d ago

---

**[How a new generation of AI agents could change holiday shopping](https://www.youtube.com/watch?v=Nl13uO4xOdM)**

The internet revolutionized holiday shopping by allowing people to make purchases without leaving their homes. Now, a new ...

📺 CBS News

👁️ 6K • 👍 11 • 💬 4 • ⏱️ 3:35 • 1d ago

---

**[The “Godfather of AI” on the Risks That Worry Him Most | Geoffrey Hinton | TED](https://www.youtube.com/watch?v=L8HdlknRkA4)**

Geoffrey Hinton helped create the neural networks behind today's AI, won a Nobel Prize for it — and has spent the years since ...

📺 TED

👁️ 569K • 👍 5K • 💬 559 • ⏱️ 25:55 • 2d ago

---

**[OpenAI insider: An AI accident is the most likely way people will die](https://www.youtube.com/watch?v=qgL_IbP2qKg)**

OpenAI Board Member Paul Christiano details a warning: within the next one to three years, there is a high risk of an artificial ...

📺 CNN

👁️ 1.5M • 👍 7K • 💬 4K • ⏱️ 21:55 • 2d ago

---

**[‘A TERRIFYING picture’: AI employees warn some advanced models are NOT SAFE to release, AXIOS](https://www.youtube.com/watch?v=ak5kr5yM7aI)**

AXIOS senior AI reporter Madison Mills joins Way Too Early to discuss her latest piece titled, 'AI employees sound alarm: models ...

📺 MS NOW

👁️ 190K • 👍 1K • 💬 581 • ⏱️ 6:01 • 2d ago

---

**[Big &amp; Tiny AI Fruit Babies Sharing Fruits 🍓👶 | Oddly Satisfying ASMR](https://www.youtube.com/watch?v=mNWtSRaFRSI)**

Big & Tiny AI Fruit Babies share colorful fruits in a cozy kitchen! Enjoy adorable fruit baby duos, tiny companions, and playful ...

📺 Oddly Satisfying AI ASMR

👁️ 33K • 👍 74 • 💬 2 • ⏱️ 6:11 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 96,527 • ❤️ 6,275 • 2d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 2,445,633 • ❤️ 1,503 • 3d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 762,491 • ❤️ 940 • 4h ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 189,735 • ❤️ 1,221 • 5d ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 15,244 • ❤️ 968 • 13d ago

---

**[Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)**

*Prism ML*

`text-generation` `26.9B`

⬇️ 59,366 • ❤️ 531 • 2d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 3,041,405 • ❤️ 13,600 • 16h ago

---

**[Nemotron-Labs-Image-30B-A3B](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)**

*NVIDIA*

`text-to-image` `32.6B`

⬇️ 218 • ❤️ 284 • 1d ago

---

**[OCRia-nano-1](https://huggingface.co/llamaindex/OCRia-nano-1)**

*LlamaIndex*

`image-to-text`

⬇️ 126 • ❤️ 285 • 2d ago

---

**[DepthPro2](https://huggingface.co/apple/DepthPro2)**

*Apple*

`depth-estimation`

⬇️ 0 • ❤️ 1,322 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 19 • 💬 0 • ⭐ 6,502 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 112 • 💬 7 • ⭐ 32,845 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 72 • 💬 4 • ⭐ 25,320 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 41 • 💬 3 • ⭐ 771 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 168 • 💬 6 • ⭐ 123,844 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 39mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 87 • 💬 7 • ⭐ 94,398 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 166 • 💬 4 • ⭐ 1,584 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 158 • 💬 10 • ⭐ 19,950 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[InCoder-32B: Code Foundation Model for Industrial Scenarios](https://huggingface.co/papers/2603.16790)**

*Jian Yang, Wei Zhang, Jiajun Wu et al. (28 authors)*

🏢 Beihang University

InCoder-32B is a 32-billion-parameter code model trained on industrial datasets with extended context length and execution verification to improve performance in hardware-aware programming tasks.

▲ 169 • 💬 6 • ⭐ 621 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.16790) • [💻 code](https://github.com/CSJianYang/Industrial-Coder) • [🔗 project](https://huggingface.co/Multilingual-Multimodal-NLP/IndustrialCoder)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 22.3k • 🔱 1.4k • 12d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 13.7k • 🔱 2.0k • 14h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 10.1k • 🔱 2.3k • 1h ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 8.3k • 🔱 797 • 17m ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 7.3k • 🔱 837 • 2h ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 4.9k • 🔱 461 • 2m ago

---

**[XinaTian/MROffice](https://github.com/XinaTian/MROffice)**

MR Office — the open-source editors of the AI office suite closest to Microsoft Office: documents, spreadsheets, presentations, PDF and code in the browser. Copilot in every editor edits real Word, Excel and PowerPoint files with you; an MCP server lets Claude, ChatGPT, Cursor and Codex create and edit them; embed it in your app with one line.

`TypeScript` `ai` `ai-agent` `claude-code` `codex` `copilot`

⭐ 4.5k • 🔱 418 • 3h ago

---

**[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)**

Private AI meeting notes that stay on your computer. No meeting bot. Free and open source for Mac, Windows and Linux. An alternative to Granola, Otter and Fireflies.

`TypeScript` `ai-meeting-assistant` `ai-notetaker` `electron` `granola-alternative` `linux`

⭐ 3.7k • 🔱 327 • 7h ago

---

**[wquguru/cicada](https://github.com/wquguru/cicada)**

知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

`Swift` `android` `linux` `live-captions` `macos` `meeting-notes`

⭐ 3.5k • 🔱 557 • 1d ago

---

**[Immortal-Protocols/lastbook](https://github.com/Immortal-Protocols/lastbook)**

Offline knowledge AI, maps and videos for survival and rebuilding

`Python`

⭐ 3.1k • 🔱 387 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
