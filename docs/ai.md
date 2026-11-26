---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-26T20:24:16.814938+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 26, 2026 at 20:24 UTC  
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

9d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 9d ago

---

---

## Google News: "ai"

**[I’m an AI leader at a tech giant. Our industry has stopped taking safety seriously | Anonymous](https://www.theguardian.com/commentisfree/2026/nov/26/ai-leader-tech-giant-trust-safeguarding-privacy-profit)**

We’re developing the most powerful tech in history – but trust, safeguarding and privacy are being sidelined in favour of huge profit, says an anonymous AI expert

The Guardian • 6h ago

---

**[SAP Weighs Cutting at Least 10,000 Positions in AI Restructuring](https://www.bloomberg.com/news/articles/2026-11-26/sap-weighs-cutting-at-least-10-000-positions-in-ai-restructuring)**

Bloomberg.com • 4h ago

---

**[US authorizes SpaceX to deploy 1 million satellites for AI data centers in space](https://www.cnn.com/2026/11/26/business/spacex-satellites-space-data-centers-intl)**

The technology is central to SpaceX’s growth ambitions, though the company warned earlier this year that it relied on “unproven” technologies.

CNN • 8h ago

---

**[US approves SpaceX plan to send a million data satellites to space](https://www.bbc.com/news/articles/cwp836l8n1jgo)**

The Starmind constellation aims to be the most cost and energy-efficient way to meet the growing demand for AI computing power.

BBC • 10h ago

---

**[Can Elon Musk really put AI datacentres in space? - The Latest](https://www.theguardian.com/news/video/2026/nov/26/can-elon-musk-really-put-ai-datacentres-in-space-the-latest)**

The Trump administration has approved Elon Musk’s plan to launch one million satellites into orbit to create datacentres in space. SpaceX argues the project could reduce the impact of datacentres on Earth as the AI industry grows. But how realistic is the plan and what could the consequences be? Michael Safi speaks to Guardian global technology editor Dan Milmo

The Guardian • 1h ago

---

**[Global stocks rally as investors shrug off U.S. tariffs and AI jitters to 'fish for bargains'](https://www.cnbc.com/2026/11/26/stock-markets-today-.html)**

Investors appeared to have shrugged off a fresh set of tariffs unveiled by the White House on Wednesday, targeting more than a dozen major trading partners.

CNBC • 20h ago

---

**[How to Talk With Your Family About A.I. Doom at Thanksgiving](https://www.nytimes.com/2026/11/25/technology/thanksgiving-ai-doom-family.html)**

The New York Times • 1d ago

---

**[Sam Altman needs a physical AI device because Apple won't give OpenAI data for ChatGPT—Tony Fadell](https://fortune.com/2026/11/26/sam-altman-needs-jony-ive-to-create-a-physical-ai-device-because-apple-will-never-give-openai-the-real-world-data-chatgpt-needs-tony-fadell-says/)**

Former Apple executive Tony Fadell says privacy rules stop OpenAI from reading context data on the iPhone. A companion gadget would let it collect that data itself.

Fortune • 10h ago

---

**[Explainer-How China got access to Nvidia's AI chips despite rules to stop them](https://finance.yahoo.com/news/explainer-china-got-access-nvidias-193901126.html)**

Nov 25 (Reuters) - AI chips are a central battleground in the US-China technology race.

Yahoo Finance • 1d ago

---

**[Andrew Bailey says unreleased AI models have raised encryption concerns](https://www.ft.com/content/450920b9-82b8-4a66-960b-5740aa7f94ae?syn-25a6b1a6=1)**

Financial Times • 3h ago

---

---

## HackerNews: "ai"

**[The New York Times warns photographers not to update Photoshop over AI features](https://news.ycombinator.com/item?id=50647673)**

The NYT doesn’t want AI metadata inadvertently added to its photos.

⬆️ 626 • 💬 495 • 23h ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

---

**[Tidal bans AI-generated music](https://news.ycombinator.com/item?id=50630309)**

The music streaming service Tidal said Tuesday that it would ban tracks it believes are completely AI-generated starting next month,

⬆️ 337 • 💬 342 • 2d ago • [Variety](https://variety.com/2026/music/news/tidal-bans-ai-generated-music-1236956924/)

---

**[Tracking Diseases Cured by AI](https://news.ycombinator.com/item?id=50657307)**

⬆️ 280 • 💬 166 • 3h ago • [diseasescuredbyai.com](https://diseasescuredbyai.com/)

---

**[Marginalia Search, Money, C++, Rust, AI, Stuff](https://news.ycombinator.com/item?id=50638220)**

Title possibly signs checks the article doesn’t have backing for. This is just a brief pro forma project update.
Not much new functionality or anything to announce, last few months have mostly been bug fixes and technical debt cleanup. Most big parts of the search engine are in place, and while there are many things that could be better, we’re less likely to straight up see massive new features, at least in the immediate future. Per familiar intuition from binary searches, the closer you get to your goal the smaller and more deliberate steps you need to take in order to get even closer.

⬆️ 222 • 💬 85 • 1d ago • [marginalia.nu](https://www.marginalia.nu/log/a_141_marginalia_update/)

---

**[Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://news.ycombinator.com/item?id=50653477)**

From February 2027, Google's terms require AI agents to reach Gmail, Drive and the rest of Workspace through Google's own MCP servers. What the rule says, what the servers can and can't do, and what to change before the deadline.

⬆️ 122 • 💬 141 • 10h ago • [techstackups.com](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

---

**[Declare is a UI language for you and your AI](https://news.ycombinator.com/item?id=50622854)**

Designed from the ground up for interfaces that act and move like the best native apps, in a few hundred lines your AI can write and its compiler can check.

⬆️ 120 • 💬 96 • 2d ago • [Declare](https://davidtemkin.github.io/declarelang/)

---

**[Working with AI](https://news.ycombinator.com/item?id=50634734)**

We interviewed people at 58 companies that use Claude about how AI is changing their work. They described few layoffs but reduced hiring, and said the most valuable uses of AI often involved reorganizing roles and workplaces around it.

⬆️ 89 • 💬 77 • 1d ago • [anthropic.com](https://www.anthropic.com/research/working-with-ai)

---

**[Jevons Paradox in AI: Cheaper Tokens Won't Pay for Capex](https://news.ycombinator.com/item?id=50625888)**

Google processes 330 times more tokens than two years ago, yet prices fall almost as fast. Why the Jevons paradox alone won't pay for $560 billion of AI capex.

⬆️ 82 • 💬 40 • 2d ago • [Philipp D. Dubach](https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/)

---

**[New York bans AI toys, including those using internet to talk to children](https://news.ycombinator.com/item?id=50644909)**

The state attorney general says she would ‘not hesitate to enforce’ the five-year ban signed by Governor Kathy Hochul

⬆️ 55 • 💬 13 • 1d ago • [the Guardian](https://www.theguardian.com/us-news/2026/nov/25/new-york-bans-ai-toys)

---

**[Quit Internet Videos Before AI Perfects Them](https://news.ycombinator.com/item?id=50627131)**

⬆️ 39 • 💬 18 • 2d ago • [nomagicpill.substack.com](https://nomagicpill.substack.com/p/quit-internet-videos-before-ai-perfects)

---

---

## YouTube Videos: "ai"

**[OpenAI insider: An AI accident is the most likely way people will die](https://www.youtube.com/watch?v=qgL_IbP2qKg)**

OpenAI Board Member Paul Christiano details a warning: within the next one to three years, there is a high risk of an artificial ...

📺 CNN

👁️ 1.4M • 👍 7K • 💬 4K • ⏱️ 21:55 • 2d ago

---

**[The State Of AI Memes - PART 1](https://www.youtube.com/watch?v=mJjPmKRyX2s)**

in this town, we look at the state of AI memes HUSS HUSS HUSS Please comment if you know more about this meme's origins.

📺 Lessons in Meme Culture

👁️ 310K • 👍 8K • 💬 662 • ⏱️ 8:50 • 8h ago

---

**[Anthropic’s AI Is Starting to Scare Its Own Researchers…](https://www.youtube.com/watch?v=r1aEPmGqQrs)**

While the top AI employees are sounding the alarm... Anthropic releases a new "Siren" report that tests whether Claude will ...

📺 AI Copium

👁️ 15K • 👍 205 • 💬 143 • ⏱️ 9:05 • 5h ago

---

**[AI Design Tools Ranked from Worst to Best (2026)](https://www.youtube.com/watch?v=gUNi7pNi9dM)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 In ...

📺 Mikey Website

👁️ 10K • 💬 7 • ⏱️ 25:54 • 6h ago

---

**[AI Is Speedrunning India&#39;s Economic Demise](https://www.youtube.com/watch?v=4hPRHFTY08I)**

Position yourself for the AI revolution, for free: https://80000hours.org/economicsexplained 95000+ read our free newsletter that ...

📺 Economics Explained

👁️ 1.4M • 👍 14K • 💬 2K • ⏱️ 17:36 • 1d ago

---

**[Trump Administration announces new tariffs &amp; disturbing warning about AI](https://www.youtube.com/watch?v=4P1lSMu32jA)**

The Trump Administration announces new tariffs against several different countries. Oakland University Associate Professor of ...

📺 FOX 2 Detroit

👁️ 25K • 👍 116 • 💬 48 • ⏱️ 24:00 • 19h ago

---

**[I Found an AI Video Generator That&#39;s ACTUALLY FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=uIcXoBl-gPg)**

Get up to 70% OFF Higgsfield this Black Friday — create stunning AI videos with Magi 2 for just $0.08/sec ...

📺 Malva AI

👁️ 24K • 👍 362 • 💬 58 • ⏱️ 8:16 • 1d ago

---

**[My Updated Thoughts on AI](https://www.youtube.com/watch?v=gNPH2axWjF8)**

I wanted to shared my updated thoughts on AI, where I think software engineering is headed, and my thoughts on the job market.

📺 SuperSimpleDev

👁️ 91K • 👍 1K • 💬 309 • ⏱️ 9:53 • 15h ago

---

**[‘A TERRIFYING picture’: AI employees warn some advanced models are NOT SAFE to release, AXIOS](https://www.youtube.com/watch?v=ak5kr5yM7aI)**

AXIOS senior AI reporter Madison Mills joins Way Too Early to discuss her latest piece titled, 'AI employees sound alarm: models ...

📺 MS NOW

👁️ 187K • 👍 1K • 💬 571 • ⏱️ 6:01 • 2d ago

---

**[OpenAI and Anthropic are done with AI](https://www.youtube.com/watch?v=kNN7FqVsO3k)**

Get up to 75% off during Proton's Black Friday sale, ending soon: https://www.protonvpn.com/mobitar OpenAI built an AI it had to ...

📺 Mo Bitar

👁️ 920K • 👍 23K • 💬 3K • ⏱️ 9:54 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 96,527 • ❤️ 6,218 • 2d ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 2,445,633 • ❤️ 1,483 • 3d ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 15,244 • ❤️ 956 • 12d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 762,491 • ❤️ 920 • 22m ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 189,735 • ❤️ 1,203 • 5d ago

---

**[Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)**

*Prism ML*

`text-generation` `26.9B`

⬇️ 59,366 • ❤️ 504 • 1d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 3,041,405 • ❤️ 13,566 • 9h ago

---

**[DepthPro2](https://huggingface.co/apple/DepthPro2)**

*Apple*

`depth-estimation`

⬇️ 0 • ❤️ 1,309 • 6d ago

---

**[OCRia-nano-1](https://huggingface.co/llamaindex/OCRia-nano-1)**

*LlamaIndex*

`image-to-text`

⬇️ 126 • ❤️ 278 • 2d ago

---

**[Nemotron-Labs-Image-30B-A3B](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)**

*NVIDIA*

`text-to-image` `32.6B`

⬇️ 218 • ❤️ 267 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 19 • 💬 0 • ⭐ 6,462 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 112 • 💬 7 • ⭐ 32,824 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 72 • 💬 4 • ⭐ 25,320 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 168 • 💬 6 • ⭐ 123,813 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 41 • 💬 3 • ⭐ 771 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 166 • 💬 4 • ⭐ 1,562 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

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

⭐ 22.2k • 🔱 1.4k • 11d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 13.6k • 🔱 2.0k • 7h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 10.1k • 🔱 2.3k • 32m ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 8.2k • 🔱 793 • 2h ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 7.1k • 🔱 819 • 14m ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 5.2k • 🔱 164 • 4m ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 4.8k • 🔱 457 • 35m ago

---

**[XinaTian/MROffice](https://github.com/XinaTian/MROffice)**

MR Office — the open-source editors of the AI office suite closest to Microsoft Office: documents, spreadsheets, presentations, PDF and code in the browser. Copilot in every editor edits real Word, Excel and PowerPoint files with you; an MCP server lets Claude, ChatGPT, Cursor and Codex create and edit them; embed it in your app with one line.

`TypeScript` `ai` `ai-agent` `claude-code` `codex` `copilot`

⭐ 4.4k • 🔱 414 • 24m ago

---

**[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)**

Private AI meeting notes that stay on your computer. No meeting bot. Free and open source for Mac, Windows and Linux. An alternative to Granola, Otter and Fireflies.

`TypeScript` `ai-meeting-assistant` `ai-notetaker` `electron` `granola-alternative` `linux`

⭐ 3.7k • 🔱 324 • 53m ago

---

**[wquguru/cicada](https://github.com/wquguru/cicada)**

知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

`Swift` `android` `linux` `live-captions` `macos` `meeting-notes`

⭐ 3.5k • 🔱 553 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
