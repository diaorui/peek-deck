---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-07T23:06:31.237322+00:00'
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

**Last Updated:** May 07, 2026 at 23:06 UTC  
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

**[Anthropic Secures SpaceX Colossus 1 After Growing 80x to a $1.2T Valuation](https://www.reddit.com/r/artificial/comments/1t6b6uz/anthropic_secures_spacex_colossus_1_after_growing/)**

Anthropic grew 80x in Q1 2026, crossed a $30B revenue run rate, & hit a $1.2T valuation. Bank of America warns its IPO could end stock market bull run.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/anthropic-ipo-valuation-80x-growth-spacex/) • 9h ago

---

**[We gave 45 psychological questionnaires to 50 LLMs. What we found was not “personality.”](https://www.reddit.com/r/artificial/comments/1t6o1dl/we_gave_45_psychological_questionnaires_to_50/)**

What is the “personality” of an LLM? What actually differentiates models psychometrically? Since LLMs entered public use, researchers have been giving them psychometric questionnaires, with mixed results. Their answers often do not seem to reflect the same psychological constructs these tests measure in humans. So we asked a slightly different question: What do LLM responses to psychometric questionnaires actually reflect? We analyzed responses to 45 validated psychometric questionnaires completed by 50 different LLMs. The strongest source of variation was whether a model endorsed items about inner experience: emotions, sensations, thoughts, imagery, empathy, and other forms of first-person experience. We call this factor the Pinocchio Dimension. Importantly, the Pinocchio Dimension is not a classical personality trait. It does not tell us whether a model is “extraverted,” “neurotic,” or “agreeable” in the human sense. Rather, it captures the extent to which a model treats the language of inner experience as self-applicable: whether it responds as if it had feelings, mental imagery, and an inner point of view, or instead as a system that reacts behaviorally to inputs. Preprint in the comments.

1h ago

---

**[Coinbase Cuts 700 Jobs and CEO Warns Every Company Will Do the Same](https://www.reddit.com/r/artificial/comments/1t6gf3v/coinbase_cuts_700_jobs_and_ceo_warns_every/)**

Coinbase is cutting 700 jobs, or 14% of its staff, as CEO Brian Armstrong warns every company will follow. Q1 earnings drop today.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/coinbase-stock-layoffs-700-jobs-ai-restructuring-2026/) • 6h ago

---

**[Artificial Intelligence will save entertainment production in the future](https://www.reddit.com/r/artificial/comments/1t6q8mk/artificial_intelligence_will_save_entertainment/)**

https://preview.redd.it/spzys3y8oszg1.png?width=735&format=png&auto=webp&s=24974b9fd17c0fcfd318349ef2913476d71aa079 Today there is strong opposition against AI in the industry, they say that AI will make everything generic and soulless, that this would kill the artistic creativity in pol of the product. Honestly, this is stupid, because this has already happened and didn't even need AI. The vast majority of works, be it anime, series, films, manga, are extremely generic and made only as fast food products, and when a slightly different work appears, it is sabotaged. So no, AI won't hinder artistic creativity, but rather give authors the opportunity to give the middle finger to these industries that destroy our works.

12m ago

---

**[English Centric AI Is Merging Unrelated Communities and Distorting Identities](https://www.reddit.com/r/artificial/comments/1t6ipmk/english_centric_ai_is_merging_unrelated/)**

I’ve been noticing a serious problem in AI generated knowledge systems, especially Grokipedia, and even in normal AI search responses. Different communities, identities, and historical groups are sometimes being merged together simply because their names sound similar in English. A lot of these mistakes begin with humans first. Someone makes an incorrect assumption, mixes up two groups, or writes an oversimplified explanation online. That mistake then gets copied across websites and repeated by other people until it starts looking credible. After that, AI systems absorb those mistakes from training data and begin repeating them at massive scale with an appearance of authority. The deeper issue is that many AI systems rely heavily on English language sources and English transliterations, even when discussing cultures and histories that do not originate in English. But English letters cannot fully represent many sounds from other languages. Once names are flattened into English spellings, unrelated words can suddenly appear connected even when they are completely different in their original languages. What makes this worse is that even when you directly ask AI systems questions about these topics, they often continue searching mostly in English instead of checking sources in the original language that would provide proper context and distinctions. So the AI keeps reinforcing distorted connections instead of correcting them. Eventually two unrelated groups become linked across websites, AI answers, Wikipedia pages, and Grokipedia articles, and the mistake starts looking authoritative simply because it is repeated everywhere. This is not just about hallucinations. It is about how digital systems slowly erase distinctions between cultures through simplification, transliteration, repetition, and inherited human mistakes.

4h ago

---

**[eTPS Site Plan – Simple Leaderboard + What You’ll Actually See](https://www.reddit.com/r/artificial/comments/1t6lbj5/etps_site_plan_simple_leaderboard_what_youll/)**

Building on the last post, here’s what the first version of effectiveTPS will look like. **Core display (v1):** - Clean table comparing popular local models - Raw TPS (the marketing number everyone shows) - eTPS (the new metric that actually measures useful output in real conversations) - Time to First Token (how long you wait before it starts replying) - Effectiveness Index = (eTPS ÷ Raw TPS) × 100 — higher is better **Example leaderboard (early test data):** | Model | Raw TPS | eTPS | Time to First Token | Effectiveness Index | |--------------------|---------|--------|---------------------|---------------------| | Llama 3.1 70B | 45.2 | 38.7 | 1.4s | **86** | | Qwen2.5-32B | 68.4 | 52.1 | 0.8s | **76** | | Gemma 2 27B | 71.3 | 44.6 | 0.6s | **63** | I’ve been running these tests through a structured multi-turn analysis framework I built to evaluate complex workflows. That’s how eTPS was stress-tested — not just single-turn benchmarks, but real back-and-forth sessions. Advanced mode (toggle) will add latency percentiles, cost-per-quality, and consistency scoring later. For v1 the goal is to keep it dead simple and immediately useful, even if you’re not deep into AI. The whole point is to cut through the noise and show which models actually deliver useful work, not just raw speed. What do you think should be added (or removed) for the first version? Any metrics you’d want to see front-and-center? **TL;DR:** Simple leaderboard with Raw TPS, eTPS, Time to First Token, and a clear Effectiveness Index. Advanced stuff stays hidden until you want it. Feedback welcome.

3h ago

---

**[Anthropic just partnered with SpaceX and doubled Claude Code rate limits effective today](https://www.reddit.com/r/artificial/comments/1t5l92i/anthropic_just_partnered_with_spacex_and_doubled/)**

Anthropic just partnered with SpaceX and doubled Claude Code rate limits effective today Big news dropped this morning. Anthropic signed a deal to use all compute capacity at SpaceX's Colossus 1 data center. That's 300+ megawatts and over 220,000 NVIDIA GPUs coming online within the month. But the part that actually matters to developers right now: What changed today: - Claude Code 5-hour rate limits are doubled (Pro, Max, Team, Enterprise) - Peak hours limit reduction on Claude Code is removed for Pro and Max - API rate limits for Claude Opus models raised considerably This is on top of their existing compute deals 5 GW with Amazon, 5 GW with Google/Broadcom, $30B of Azure capacity with Microsoft and NVIDIA, and $50B in infrastructure with Fluidstack. They also mentioned interest in developing orbital AI compute with SpaceX. Which is a sentence I did not expect to read in 2026. For those of us building with Claude Code daily, the doubled limits + no more peak hour throttling is the headline. Rate limits have been the most frustrating bottleneck when you're deep in a long coding session. Anyone else noticing a difference already?

1d ago

---

**[Robert Evans on AI psychosis](https://www.reddit.com/r/artificial/comments/1t6f19i/robert_evans_on_ai_psychosis/)**

Surprised it took this long!

🔗 [open.spotify.com](https://open.spotify.com/episode/0gr3uXLFSlVYADPFQ0J9OK?si=d1d8eab26d6d474c) • 6h ago

---

**[Feels like AI is entering its “infrastructure matters” phase](https://www.reddit.com/r/artificial/comments/1t6p2ln/feels_like_ai_is_entering_its_infrastructure/)**

A year ago, most discussions were about which model was smartest. Now it increasingly feels like the bigger differentiators are becoming: latency orchestration context handling reliability inference economics developer workflow deployment flexibility The interesting shift is that model quality is improving across the board fast enough that “best benchmark” doesn’t automatically translate into “best real-world experience” anymore. We’re seeing more teams optimize around: workload routing hybrid local/cloud setups smaller specialized models faster iteration cycles predictable scaling costs In a weird way, AI feels like it’s maturing into a systems/infrastructure problem almost as much as a model problem. Curious if others are seeing the same shift or if frontier model capability still dominates most decisions for your workflows.

1h ago

---

**[AI is helpful but still not “there” yet](https://www.reddit.com/r/artificial/comments/1t6hhp1/ai_is_helpful_but_still_not_there_yet/)**

what I mean is that every time I use Claude, or Grok or any of the AI platforms and tools, I realize how far this technology is from replacing jobs. yes it can make some things easier but sometimes it can also make things harder. for example, I’ve been editing a legal document and have been toggling between three different tools; each have a mind of their own. some are rather astute but then hallucinate and produce some accurate things and some nonsense, and others act like they have no knowledge of the real world at all — (I understand AI is not sentient). what I’m getting at is that AI is not foolproof and can’t be trusted for things that need to be checked and re-checked with extreme attention to detail. I discover problems and inconsistencies everytime I utilize AI and that’s why I couldnt ever trust it to be a true personal assistant — because sometimes it’s not capable of delivering even basic tasks. it’s relentless and has endurance, but it’s a somewhat flawed repository that sometimes makes tasks even more difficult (like editing) — because rather than checking my own work, I’m flagging AI’s errors, which increases my work load.

5h ago

---

---

## Google News: "ai"

**[France is fan favorite for the FIFA World Cup — but AI is backing another nation for glory, says BofA](https://www.cnbc.com/2026/05/07/france-is-world-cup-favorite-but-ai-is-backing-another-winner.html)**

The 2026 FIFA World Cup is expected to add over $40 billion to the global GDP with its most lucrative edition ever.

CNBC • 8h ago

---

**[The Secret to Understanding AI](https://www.theatlantic.com/ideas/2026/05/ai-for-good-uses/687082/)**

“Imagine the tech without the tech companies.”

The Atlantic • 8h ago

---

**[Nursing survey flags care quality, safety, AI concerns](https://www.bostonglobe.com/2026/05/07/business/nursing-survey-care-quality-safety-ai/)**

Some 71 percent of nurses say the quality of care has worsened in the past two years, the Massachusetts Nurses Association survey found.

The Boston Globe • 51m ago

---

**[Third Way offers game plan for AI job disruption](https://thehill.com/newsletters/technology/5868835-third-way-offers-game-plan-for-ai-job-disruption/)**

The Hill • 51m ago

---

**[Increasing number or employers seek job candidates with AI skills, survey finds](https://www.cbsnews.com/video/increasing-number-employers-seek-job-candidates-ai-skills-survey-finds/)**

As jobs evolve with the use of artificial intelligence, more employers want workers who are familiar with the technology. Eight in 10 hiring managers considered AI skills a priority in 2025, according to Resume Genius research. CBS News MoneyWatch reporter Megan Cerullo has more.

CBS News • 39m ago

---

**[5 new ways to explore the web with generative AI in Search](https://blog.google/products-and-platforms/products/search/explore-web-generative-ai-search/)**

New updates to AI Mode and AI Overviews in Google Search make it easier for you to dive deeper online.

blog.google • 1d ago

---

**[Five Ways A.I. Search Beats an Old-School Google Search](https://www.nytimes.com/2026/05/07/technology/personaltech/google-ai-mode-search.html)**

The New York Times • 14h ago

---

**[Google Unveils 5 New AI Search Features to Push Users Deeper Into the Web](https://www.eweek.com/news/google-ai-search-links-source-previews/)**

eWeek • 9h ago

---

**[NVIDIA and IREN Announce Strategic Partnership to Accelerate Deployment of up to 5 Gigawatts of AI Infrastructure](https://nvidianews.nvidia.com/news/nvidia-and-iren-announce-strategic-partnership-to-accelerate-deployment-of-up-to-5-gigawatts-of-ai-infrastructure)**

NVIDIA (NASDAQ: NVDA) and IREN Limited (NASDAQ: IREN) (“IREN”) today announced a strategic partnership to accelerate deployment of next-generation AI infrastructure.

NVIDIA Newsroom • 2h ago

---

**[IREN shares pop 13% on AI infrastructure deal with Nvidia](https://www.cnbc.com/2026/05/07/iren-stock-ai-infrastructure-nvidia.html)**

Data center operator IREN announced a partnership with semiconductor giant Nvidia.

CNBC • 1h ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 1711 • 💬 1119 • 2d ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 540 • 💬 301 • 2d ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 539 • 💬 349 • 2d ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 385 • 💬 269 • 2d ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[AI slop is killing online communities](https://news.ycombinator.com/item?id=48053203)**

⬆️ 345 • 💬 325 • 4h ago • [AI Slop is Killing Online Communities](https://rmoff.net/2026/05/06/ai-slop-is-killing-online-communities/)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 253 • 💬 89 • 2d ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[Telus Uses AI to Alter Call-Agent Accents](https://news.ycombinator.com/item?id=48031109)**

According to reporting by iPhone in Canada and The Globe and Mail, **Telus** is using AI through its **Telus Digital** unit to modify call-centre agents' accents in real time. iPhone in Canada reports the speech-to-speech tool is built by a company called **Tomato.ai** and is applied to offshore agents' voices to reduce what Telus reportedly calls "accent-related friction." Labour groups have criticised the practice as deceptive and have urged mandatory disclosure, The Globe and Mail reports. According to The Globe and Mail, **Rogers** and **Bell** told the paper they have no plans to adopt similar voice-altering technology. The coverage says the rollout has provoked swift public backlash in Canada.

⬆️ 233 • 💬 210 • 1d ago • [Let's Data Science](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63)

---

**[Motherboard sales 'collapse' amid unprecedented shortages fueled by AI](https://news.ycombinator.com/item?id=48050540)**

Fewer people are buying parts and building new PCs from scratch.

⬆️ 230 • 💬 272 • 7h ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers)

---

**[Show HN: Airbyte Agents – context for agents across multiple data sources](https://news.ycombinator.com/item?id=48023496)**

⬆️ 143 • 💬 45 • 2d ago

---

**[Xbox CEO ends Copilot AI development and overhauls leadership](https://news.ycombinator.com/item?id=48029753)**

Xbox CEO Asha Sharma reshuffled leadership and axed Copilot features as the division looks to reverse declining revenue.

⬆️ 110 • 💬 40 • 2d ago • [Dexerto](https://www.dexerto.com/gaming/xbox-ceo-ends-copilot-ai-development-overhauls-leadership-3361353/)

---

---

## YouTube Videos: "ai"

**[Google&#39;s INSANE new AI Agent](https://www.youtube.com/watch?v=vqBSNTZeLsg)**

Check out tastytrade here: https://tastytrade.com/unleashed. My Links ➡️ Twitter: https://x.com/WesRoth ➡️ AI Newsletter: ...

📺 Wes Roth

👁️ 20K • 👍 466 • 💬 199 • ⏱️ 1:29:12 • 19h ago

---

**[How to Make AI Videos That Really Look Like You (Full Guide)](https://www.youtube.com/watch?v=st7NRTxeKC8)**

Make AI Videos with Yourself using OpenArt https://youricreates.com/realistic-AI In this video, I show the full workflow I used to ...

📺 Youri van Hofwegen

👁️ 10K • 💬 6 • ⏱️ 13:14 • 8h ago

---

**[OH SH*T! The Banks are Dumping AI Loans!](https://www.youtube.com/watch?v=eIz2MrR5xMQ)**

The biggest U.S. banks are quietly dumping their AI debt — a massive red flag that the AI bubble and credit cycle are about to ...

📺 Steven Van Metre

👁️ 47K • 👍 2K • 💬 226 • ⏱️ 16:12 • 23h ago

---

**[Google’s New AI Is The OpenClaw Killer](https://www.youtube.com/watch?v=nov9uoIQt6g)**

Try Higgsfield Marketing Studio here: https://higgsfield.ai/s/marketing-studio-1-0-airevolutionx-lVqpUi Google is testing Remy, ...

📺 AI Revolution

👁️ 49K • 👍 1K • 💬 62 • ⏱️ 13:34 • 1d ago

---

**[Generate FREE &amp; UNLIMITED AI Videos With Claude](https://www.youtube.com/watch?v=m0RiHpyyAis)**

Try the Claude AI video workflow with Higgsfield MCP here → https://higgsfield.ai/s/mcp-malvaai-EDNKNW Download the ...

📺 Malva AI

👁️ 3K • 👍 134 • 💬 41 • ⏱️ 7:19 • 12h ago

---

**[The hidden fraud behind the AI music boom](https://www.youtube.com/watch?v=7xkZDgMPgVI)**

AI music is "flooding" streaming platforms. Deezer says it is now receiving nearly 75000 fully AI-generated tracks a day, which ...

📺 Sky News

👁️ 9K • 👍 202 • 💬 64 • ⏱️ 8:36 • 11h ago

---

**[AI, Layoffs and War - It’s Getting Worse Fast](https://www.youtube.com/watch?v=90vpbHjMNNg)**

The economy is sending clear warning signs, and today we break down the real story behind layoffs, inflation, and global conflict.

📺 I Allegedly

👁️ 14K • 👍 1K • 💬 214 • ⏱️ 10:43 • 1d ago

---

**[Unreal Hyper Realistic AI Humanoid | Android Robots Ready for Purchase #cybergirl #Robotics](https://www.youtube.com/watch?v=G3U7aHvFRyM)**

Would You Dare to Date This Hyper Realistic Humanoid AI Android Cybergirl Robots Unveiled at 2026? These Robotics ...

📺 ejunky66

👁️ 15K • 👍 307 • 💬 21 • ⏱️ 1:00 • 10h ago

---

**[IBM CEO warns this would ‘NOT BE GOOD’ for US in AI race…](https://www.youtube.com/watch?v=u3ZzaMf0ml0)**

IBM CEO Arvind Krishna assesses government oversight of artificial intelligence, quantum computing and more on 'The Claman ...

📺 Fox Business

👁️ 14K • 👍 211 • 💬 85 • ⏱️ 9:05 • 2d ago

---

**[Anthropic&#39;s Dario Amodei and JPMorgan&#39;s Jamie Dimon on AI boom, AI regulation &amp; impact on jobs](https://www.youtube.com/watch?v=FG5JsLHPW_I)**

CNBC's Andrew Ross Sorkin discusses key takeaways from his conversation with Anthropic CEO Dario Amodei and JPMorgan ...

📺 CNBC Television

👁️ 50K • 👍 518 • 💬 66 • ⏱️ 5:23 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 946,264 • ❤️ 3,722 • 1d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 71,149 • ❤️ 368 • 1d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 165,240 • ❤️ 1,342 • 15d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 539 • ❤️ 191 • 1h ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 4,460 • ❤️ 216 • 10d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 28,215 • ❤️ 150 • 21h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 20,905 • ❤️ 469 • 9d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 19,908 • ❤️ 136 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,771,851 • ❤️ 1,174 • 13d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 18,272 • ❤️ 295 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 60 • 💬 3 • ⭐ 71,016 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 75 • 💬 6 • ⭐ 3,374 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 31 • 💬 3 • ⭐ 23,370 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,758 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 16 • 💬 3 • ⭐ 9,451 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 91 • 💬 10 • ⭐ 8,337 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 62,274 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,319 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[RLDX-1 Technical Report](https://huggingface.co/papers/2605.03269)**

*Dongyoung Kim, Huiwon Jang, Myungkyu Koo et al. (68 authors)*

🏢 RLWRLD

RLDX-1 is a general-purpose robotic policy for dexterous manipulation that integrates heterogeneous modalities through a Multi-Stream Action Transformer architecture, demonstrating superior performance in complex real-world tasks compared to existing vision-language-action models.

▲ 85 • 💬 1 • ⭐ 70 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03269) • [💻 code](https://github.com/RLWRLD/RLDX-1) • [🔗 project](http://rlwrld.ai/rldx-1)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,862 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.2k • 🔱 2.8k • 10d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.9k • 🔱 705 • 3d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.8k • 🔱 447 • 5h ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.7k • 🔱 512 • 3d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.1k • 🔱 369 • 11h ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.9k • 🔱 479 • 8h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.6k • 🔱 373 • 16d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.8k • 🔱 359 • 1d ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.7k • 🔱 352 • 14d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.4k • 🔱 675 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
