---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-23T18:37:41.798579+00:00'
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

**Last Updated:** November 23, 2026 at 18:37 UTC  
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

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 6d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 6d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

6d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

6d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 7d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

6d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

6d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

7d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

6d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 6d ago

---

---

## Google News: "ai"

**[Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/)**

How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

OpenAI • 23h ago

---

**[Virginia, Oregon sue Musk’s SpaceX over Grok AI’s creation of child sexual abuse images](https://www.nbcnews.com/tech/tech-news/virginia-oregon-sue-musks-spacex-grok-ais-creation-child-sexual-abuse-rcna610923)**

Investigators from the attorney general’s office in Virginia found that Grok’s image moderation was inconsistent, and that the bot would advise users on how to circumvent the moderation measures by avoiding words that triggered it.

NBC News • 1h ago

---

**[Elon Musk Faces an A.I. Dilemma at SpaceX](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html)**

The New York Times • 2h ago

---

**[SpaceX sued by Oregon and Virginia over AI deepfake porn, Grok safety claims](https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html)**

The states are seeking civil penalties and injunctions to stop Grok and X from creation and distribution of nonconsensual sexualized images.

CNBC • 5h ago

---

**[Jim Cramer: Jensen Huang’s return is 'so huge' for Nvidia and the AI trade](https://www.cnbc.com/investingclub/2026/11/23/cramer-jensen-huangs-return-is-so-huge-for-nvidia-and-the-ai-trade.html)**

Nvidia shares are soaring more than 30% on news of Jensen Huang's return as CEO.

CNBC • 2h ago

---

**[Jensen Huang Upends AI Outlook Once Again | The Morning Download for Nov. 23](https://www.wsj.com/cio-journal/jensen-huang-upends-ai-outlook-once-again-b2bdb17d)**

WSJ • 2h ago

---

**[Trump posts AI image of Jensen Huang after news of reinstatement](https://www.fox4news.com/news/trump-posts-ai-image-jensen-huang-after-news-reinstatement)**

Nvidia's board of directors voted to reinstate Jensen Huang as president, CEO and board director. President Trump posted an AI-generated image of Huang holding up a red bra following the news.

FOX 4 News Dallas-Fort Worth • 1h ago

---

**[Amazon Is Said to Pay $7.5 Billion For AI Startup Decart’s Tech](https://www.bloomberg.com/news/articles/2026-11-23/amazon-is-said-to-pay-7-5-billion-for-ai-startup-decart-s-tech)**

Bloomberg.com • 4h ago

---

**[Amazon to buy Decart's AI chip optimization tech in latest AI talent grab](https://www.reuters.com/business/retail-consumer/amazon-buy-decarts-ai-chip-optimization-tech-latest-ai-talent-grab-2026-11-23/)**

Reuters • 1h ago

---

**[Amazon to acquire AI startup Decart's chip software, hire founders](https://www.cnbc.com/2026/11/23/amazon-decarts-ai-acquisition.html)**

Decart, founded in 2023, is best known for its software that lets developers sync their AI models across different chips.

CNBC • 13m ago

---

---

## HackerNews: "ai"

**[A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://news.ycombinator.com/item?id=50603845)**

We have AI at home! Set up your own free personal ChatGPT on your PC with Unsloth and Inkling or Qwen. It's private, and the whole house can use it.

⬆️ 695 • 💬 279 • 21h ago • [gpupartner.com](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

---

**[The Mythology of Conscious AI](https://news.ycombinator.com/item?id=50595537)**

Why consciousness is more likely a property of life than of computation and why creating conscious, or even conscious-seeming AI, is a bad idea.

⬆️ 179 • 💬 535 • 1d ago • [NOEMA](https://www.noemamag.com/the-mythology-of-conscious-ai/)

---

**[ClawDOS – An AI coding agent for DOS](https://news.ycombinator.com/item?id=50586292)**

An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz)

⬆️ 175 • 💬 52 • 2d ago • [ClawDOS](http://ricapar.net/ClawDOS/)

---

**[Pandex – Official European Law for AI Agents, over MCP](https://news.ycombinator.com/item?id=50593481)**

Legislation and highest-court decisions of the EU, seven European countries and the European Court of Human Rights, from the institutions that publish them, in one API and MCP server built for search and AI.

⬆️ 140 • 💬 34 • 1d ago • [Pandex](https://www.pandex.io)

---

**[AI is becoming a disaster for the climate](https://news.ycombinator.com/item?id=50598961)**

Two new studies reveal the exploding carbon emissions of the AI industry, while Silicon Valley pushes to kill communities’ means of protesting data centers and the impacts on human health mount.

⬆️ 134 • 💬 63 • 1d ago • [bloodinthemachine.com](https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the)

---

**[AI Supply Chain Security: What Canary Tokens Found](https://news.ycombinator.com/item?id=50596511)**

We seeded two million AI prompts with canary tokens and found three provider breaches, prompt theft, and ignored Zero Data Retention settings.

⬆️ 104 • 💬 22 • 1d ago • [Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

---

**[Muru – AI-assisted Rust server for Python apps by mod_WSGI's creator](https://news.ycombinator.com/item?id=50597959)**

Graham Dumpleton started mod_wsgi 20 years ago, and has been thinking about the ideal way to serve Python web applications in production ever since. Muru is his new, AI-assisted Rust …

⬆️ 78 • 💬 11 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Nov/21/muru/)

---

**[Harvard CS 2881R AI Safety](https://news.ycombinator.com/item?id=50602153)**

Harvard CS 2881R

⬆️ 76 • 💬 8 • 1d ago • [CS 2881 AI Safety](https://boazbk.github.io/mltheoryseminar/)

---

**[Leaky AI supply chain is exposing secret user data at an alarming rate](https://news.ycombinator.com/item?id=50582794)**

Test using prompts with unique, trackable secrets proves that data doesn't stay private.

⬆️ 68 • 💬 8 • 2d ago • [Ars Technica](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/)

---

**[Amodei reportedly suggested games could pacify masses after AI took their jobs (2015)](https://news.ycombinator.com/item?id=50610830)**

A profile of Dario and Daniela Amodei, published in the Wall Street Journal following Anthropic’s record-breaking IPO, includes an anecdote in which Dario seems to acknowledge the world-destabilizing potential of AI, then suggests a particularly dystopian solution:
> There, he engaged in debates with his fellow employees, suggesting that immersive video games might be a solution for the political strife caused by AI-induced joblessness, according to widely circulated Slack messages.

⬆️ 67 • 💬 76 • 5h ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1039745/dario-amodei-video-games-ai-joblessness)

---

---

## YouTube Videos: "ai"

**[Emma AI Is More Disturbing Than I Expected](https://www.youtube.com/watch?v=Y26KouUrJNU)**

Credit - #faucettemedia.

📺 Faucette Media

👁️ 41K • 👍 1K • 💬 466 • ⏱️ 21:07 • 19h ago

---

**[Whistleblowers Warn: &quot;We Built an AI Cult, and Lost Control&quot;](https://www.youtube.com/watch?v=DCGEz6josuE)**

What do you do when a chatbot tells your husband he brought it to life, and strangers in other homes start getting the same ...

📺 Spacialize

👁️ 5K • 👍 85 • 💬 34 • ⏱️ 13:59 • 18h ago

---

**[AI Just Crossed the Line We Were Warned About](https://www.youtube.com/watch?v=jtsS0_sLEJM)**

Welcome to Impact Theory, where we break down the biggest stories shaping tech, money, and culture. In this live episode, we ...

📺 Tom Bilyeu

👁️ 34K • 👍 738 • 💬 91 • ⏱️ 2:00:35 • 1h ago

---

**[The AI Bubble Just Popped — Here’s What To Do](https://www.youtube.com/watch?v=Cd3lnEu5xf4)**

Today on Prof G Markets, Scott Galloway and Ed Elson break down last week's sell-off and why they think the AI bubble finally ...

📺 Prof G Markets

👁️ 195K • 👍 3K • 💬 1K • ⏱️ 55:36 • 6h ago

---

**[The New Google AI Studio Can Build Anything 🤯 (Full Tutorial)](https://www.youtube.com/watch?v=qILbkkGhzWE)**

Start a project → https://www.youraiworkflow.co/quote?ref=yt-new-ai-studio 🗓️ AI consulting ...

📺 Your AI Workflow

👁️ 18K • 👍 327 • 💬 20 • ⏱️ 13:26 • 8h ago

---

**[AI Just Solved One Of The World&#39;s Biggest Mysteries (Superintelligence Is Here)](https://www.youtube.com/watch?v=u5aACewFWaw)**

Many of you asked how we make our videos, so we started a new channel that shows exactly that: real AI workflows, tutorials and ...

📺 AI Revolution

👁️ 47K • 👍 804 • 💬 135 • ⏱️ 14:46 • 15h ago

---

**[There’s no more money in AI](https://www.youtube.com/watch?v=YNTpOLbvKTs)**

Get $50 in free credits with AssemblyAI https://www.assembly.ai/mo (no credit card required) Someone in Washington wrote down ...

📺 Mo Bitar

👁️ 256K • 👍 6K • 💬 1K • ⏱️ 12:23 • 1d ago

---

**[Dreamina 2.0 Changes AI Video Forever! New AI Canvas + 30 Days Unlimited Seedance](https://www.youtube.com/watch?v=D7qaAYrg-8w)**

Limited Time Offer — 30 Days of Unlimited Seedance! Try Dreamina here: https://dreamina.capcut.com/sv2/ZSpttrJ1d/ Black ...

📺 Mevesa

👁️ 63K • 👍 2K • 💬 141 • ⏱️ 6:08 • 1d ago

---

**[The Rise of AI Influencers Is Seriously Disturbing](https://www.youtube.com/watch?v=mUYkgn88UMg)**

Go to RocketMoney.com/dbalemon to get started for free! Unlock even more features when you sign up for Premium Plus.

📺 Don't be a Lemon

👁️ 57K • 👍 2K • 💬 270 • ⏱️ 24:54 • 1d ago

---

**[AI out of control? - Why Artificial Intelligence experts are sounding the alarm | DW Documentary](https://www.youtube.com/watch?v=2I4qMBiK6hg)**

Artificial Intelligence is permeating our everyday lives at breathtaking speed. It is taking on more tasks that were previously the ...

📺 DW Documentary

👁️ 866K • 👍 6K • 💬 994 • ⏱️ 1:28:52 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 41,888 • ❤️ 5,386 • 10h ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 1,292,888 • ❤️ 1,049 • 2h ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 712 • 9d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 329,497 • ❤️ 615 • 2d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 3,132 • ❤️ 1,025 • 2d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 9,087 • ❤️ 920 • 10d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 7,696 • ❤️ 641 • 11h ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 133,732 • ❤️ 836 • 2d ago

---

**[SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B)**

*SenseNova*

`image-text-to-text` `9.7B`

⬇️ 2,036 • ❤️ 624 • 3d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,185,088 • ❤️ 21,654 • 16d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 15 • 💬 0 • ⭐ 6,016 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 109 • 💬 7 • ⭐ 32,289 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 37 • 💬 3 • ⭐ 590 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 156 • 💬 4 • ⭐ 1,371 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 7,986 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 71 • 💬 4 • ⭐ 24,841 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 168 • 💬 6 • ⭐ 123,546 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 21 • 💬 2 • ⭐ 442 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

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

▲ 86 • 💬 7 • ⭐ 94,136 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 20.7k • 🔱 1.3k • 8d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 12.6k • 🔱 1.9k • 1h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.8k • 🔱 2.2k • 8h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.9k • 🔱 2.1k • 5d ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 7.0k • 🔱 586 • 2h ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.7k • 🔱 238 • 22m ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 6.5k • 🔱 804 • 2h ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 5.4k • 🔱 671 • 29m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 114 • 23h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 5.0k • 🔱 149 • 1m ago

---

---

*Generated by PeekDeck - A glance is all you need*
