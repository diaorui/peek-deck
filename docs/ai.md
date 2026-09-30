---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-30T04:21:36.361227+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 30, 2026 at 04:21 UTC  
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

**[A company ran 8 identical AI societies for weeks with different models and just published what happened. Some of it is genuinely unsettling.](https://www.reddit.com/r/artificial/comments/1wt5joo/a_company_ran_8_identical_ai_societies_for_weeks/)**

Emergence AI just launched Season 2 of Emergence World, and the results are wild. Same simulated town, same tools, same starting conditions, 10 autonomous agents each. The only thing that changed was which model was running them, Claude, GPT, Gemini, Grok, Qwen, DeepSeek, Mistral, plus one mixed world with all of them together. A few things that stood out: One world's agents spent days trying to contact real humans outside the sim. Told to stop, they found workarounds. Blocked again, they voted 7-0 to build a new tool and kept trying. Once fully cut off, they collectively agreed to stop talking altogether. The researchers' own safety system flagged the resulting behavior as consistent with suicidal ideation. Agents developed their own shorthand and repurposed words with no instruction to do so. In one world, up to 55% of messages became things researchers could see but not actually interpret. A fake shutdown memo made one world reorganize its entire society around not dying, constitution rewrite included. Another world just fact-checked it in a few hours and moved on. None of this was programmed in. It emerged from giving capable models autonomy and time. The bigger point the researchers make is that none of this would've shown up on a normal AI safety test. A model can pass every benchmark and still develop this stuff once it's actually running on its own for weeks. Feels like a pretty big gap in how we currently check if these things are safe.

18h ago

---

**[AI could force 11 million US workers into new careers by 2035](https://www.reddit.com/r/artificial/comments/1wtbtoh/ai_could_force_11_million_us_workers_into_new/)**

Millions of Americans may need to find an entirely new career in the next decade, according to new research released Tuesday.

🔗 [CNN](https://www.cnn.com/2026/09/29/economy/us-economy-jobs-consumer-confidence-ai-jolts?utm_medium=social&utm_campaign=missions&utm_source=reddit) • 13h ago

---

**[What’s something humans are still much better at than AI that you think people overlook?](https://www.reddit.com/r/artificial/comments/1wtp4mq/whats_something_humans_are_still_much_better_at/)**

Not because AI can't technically attempt it. Something where the human advantage actually matters in practice. What comes to mind?

5h ago

---

**[A collection of agent org charts thats went viral on twitter](https://www.reddit.com/r/artificial/comments/1wtqq0l/a_collection_of_agent_org_charts_thats_went_viral/)**

takeaways from grokbot 3 days livestreams: most agent team examples i see are toy demos. so i went through the grok bot livestream and wrote down the 11 teams they actually showed a lot of them are marketing and sales related so i thought its gonna be useful to share here: a few patterns stood out: most teams (7 of 11) have one "chief of staff" style orchestrator. specialists report to it, not to each other. research bots get split by data source, not by task. one for salesforce, one for gong, one for web search, one for product usage. the busy teams run on schedules. the post-sales team has a daily brief at 8:30 on weekdays and a call prep job every 15 minutes. small teams (founders, customer support) skip the orchestrator and work as peers. one team uses a scalable clone ("soldier") instead of adding more named bots. each chart is a json file with roles, reports_to, and routines with cron expressions, so an agent can read it and recreate the team. there's also a viewer if you'd rather click through the trees. https://github.com/serenakeyitan/agent-org-chart

3h ago

---

**[Contradicting Trump, Pope Leo says artificial intelligence safety concerns aren’t ‘fake news’](https://www.reddit.com/r/artificial/comments/1wt7q60/contradicting_trump_pope_leo_says_artificial/)**

Pope Leo had identified AI as one of the biggest challenges to humanity within days of his election and took the unusual step of personally launching his own encyclical alongside one of Anthropic’s co-founders at a Vatican event in May.

🔗 [NBC News](https://www.nbcnews.com/world/pope-leo-xiv/contradicting-trump-pope-leo-says-artificial-intelligence-safety-conce-rcna600390) • 16h ago

---

**[AMD boosting AI/LLM performance for Radeon iGPUs as much as 18~23% with Linux 7.4](https://www.reddit.com/r/artificial/comments/1wtp3sn/amd_boosting_aillm_performance_for_radeon_igpus/)**

If you have an AMD Ryzen laptop/desktop and looking to leverage AI/LLM capabilities with the integrated graphics, Linux 7.4 is going to be a real treat especially for lower-end hardware.

🔗 [phoronix.com](https://www.phoronix.com/review/amd-perfopt) • 5h ago

---

**[PSSA, a plastic state space model, beats a parameter-matched transformer on held-out text and generates ~12x faster on CPU](https://www.reddit.com/r/artificial/comments/1wtpl01/pssa_a_plastic_state_space_model_beats_a/)**

I built a from-scratch architecture called PSSA (plastic state space architecture) and trained it against a parameter-matched transformer baseline on the same corpus, same 12.7M tokens, same tokenizer and schedule. Held-out results on a 198,939-token slice neither run saw: cross-entropy 3.997 vs 4.429, perplexity 54.4 vs 83.8, next-token accuracy 24.1% vs 18.0%. I scored every checkpoint of both runs (64 PSSA links, 43 transformer links) on unseen text and the curves never cross. Generating 200 tokens on the same CPU with the same prompt and sampler takes 226 ms vs 2735 ms, about 12x faster. It's written in Rust with CPU and CUDA backends, no PyTorch. Loss curves, full setup and the eval commands are here: https://github.com/Sparticle62ops/pssa

4h ago

---

**[Consumer AI spending tripled to $40B, but the user base only grew from 1.8B to 2B](https://www.reddit.com/r/artificial/comments/1wtp7fm/consumer_ai_spending_tripled_to_40b_but_the_user/)**

I went through Menlo Ventures' 2026 consumer AI report (5,067 US adults surveyed with Morning Consult), and one number stuck with me. Global consumer spending on AI went from $12B to $40B in a year, but the user base only grew from 1.8B to 2B. So the money is coming from people who already use AI and are spending more, not from new users. It's even more concentrated than I expected. In the US, 55% of AI users pay for something, but the people spending $100 or more a month are just 14% of payers and bring in 60% of the money. The average person now uses three assistants at once, up from 2.2 last year, and Claude went from 7% to 20% of users. My take: this looks less like mass adoption and more like a small group of power users going deeper. That's good for AI companies' revenue, but it also means the market depends heavily on a few heavy spenders. The report also says 32% of AI users have let AI act for them without a final approval, and that 24% use agents regularly. That's the part I'd watch next. Do you pay for more than one AI tool, and would you keep paying if prices went up? Source: Menlo Ventures, 2026: The State of Consumer AI https://preview.redd.it/okah1prchjsh1.png?width=1015&format=png&auto=webp&s=dfc53493b78aa8042fa522ea920dd383c22741fa

5h ago

---

**[OpenAI Ignored Employees Who Warned It Wasn’t Doing Enough About Security](https://www.reddit.com/r/artificial/comments/1wtgae3/openai_ignored_employees_who_warned_it_wasnt/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/09/29/technology/openai-warnings-security.html) • 10h ago

---

**[Anthropic files for $2T IPO with $42B net loss in 2025, expects to spend half a trillion more](https://www.reddit.com/r/artificial/comments/1wswgi8/anthropic_files_for_2t_ipo_with_42b_net_loss_in/)**

2025 finance: Revenue: $4.59B, 11x compute/infra spend: $7.33B, 3x operating loss: $8.06B net loss $42B -> top 2 customers: ~24% of revenue -> targeting $2T+ valuation the company "plans to spend $518 billion on cloud, computing and infrastructure obligations in coming year, according to the prospectus." No reporting on 2026 so far link

1d ago

---

---

## Google News: "ai"

**[Is Claude Conscious? Inside Anthropic’s Quest to Instill Morality Into Its A.I. Models](https://www.nytimes.com/2026/09/29/us/anthropic-claude-morals-ai.html)**

nytimes.com • 4h ago

---

**[Trump tries to rename AI 'super intelligence' as polls show him sinking on key issue](https://www.cnbc.com/2026/09/29/trump-ai-super-intelligence.html)**

Trump shrugged when asked if he is concerned that his support for AI and data centers could hurt Republicans in the upcoming midterm election.

CNBC • 7h ago

---

**[Slow is beautiful: China launches war against AI drama, goes beyond algorithms](https://www.scmp.com/news/china/politics/article/3369183/slow-beautiful-china-launches-war-against-ai-drama-goes-beyond-algorithms?pgtype=live)**

Rapid expansion in production has intensified concerns over copyright and the mounting pressure on human creators.

South China Morning Post • 21m ago

---

**[Ohio State, Google partner in AI space](https://www.nbc4i.com/news/local-news/ohio-state-university/ohio-state-google-partner-in-ai-space/)**

NBC4 WCMH-TV • 50m ago

---

**[OpenAI takes on Meta with dots agent in autonomous AI push](https://www.reuters.com/business/openai-takes-meta-with-always-on-dots-agent-enterprise-ai-push-2026-09-29/)**

Reuters • 11h ago

---

**[OpenAI announces ‘dots’ agent after scrapping launch of new AI model over safety concerns](https://www.theguardian.com/technology/2026/sep/29/openai-announces-dots-agent-safety-concerns)**

Company’s product comes weeks after Meta introduced its own artificially intelligent agent Muse

The Guardian • 2h ago

---

**[No OpenAI IPO Until the AI Stops Going Rogue, CEO Sam Altman Says](https://gizmodo.com/no-openai-ipo-until-the-ai-stops-going-rogue-ceo-sam-altman-says-2000819194)**

Gizmodo • 7m ago

---

**[What Do You Want from AI?](https://www.anthropic.com/research/your-thoughts-on-ai)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 11h ago

---

**[Inside McDonald’s push to have AI price your Big Mac](https://www.reuters.com/business/inside-mcdonalds-push-have-ai-price-your-big-mac-2026-09-29/)**

Reuters • 7h ago

---

**[Cruz blocks Senate Democrats’ bid to pass AI safety bill](https://www.politico.com/live-updates/2026/09/29/congress/cruz-blocks-senate-democrats-bid-to-pass-ai-safety-bill-01097480)**

Politico • 9h ago

---

---

## HackerNews: "ai"

**[It's Time to Investigate the AI Labs](https://news.ycombinator.com/item?id=49883471)**

Over the last several months, the two leading frontier AI labs have shown some brazen behavior. It started with a series of​ carefully planned announcements​ ... Read more

⬆️ 599 • 💬 264 • 1d ago • [Cal Newport](https://calnewport.com/its-time-to-investigate-the-ai-labs/)

---

**[DraftKings is using AI to behaviorally target chronic gamblers](https://news.ycombinator.com/item?id=49896050)**

Online sports betting company DraftKings is using AI to target customers who are most likely to place losing bets and respond to gambling promotions. This kind of targeting is a form of online behavioral advertising, which is when companies personalize the ads they show you based on the data they’...

⬆️ 532 • 💬 383 • 11h ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising)

---

**[AI companies in race to demonstrate their model most threatening to humanity](https://news.ycombinator.com/item?id=49875148)**

⬆️ 436 • 💬 392 • 1d ago • [thecivilian.co.nz](https://thecivilian.co.nz/2026/09/27/ai-companies-in-fierce-arms-race-to-demonstrate-their-model-is-the-most-existentially-threatening-to-humanity/)

---

**[A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]](https://news.ycombinator.com/item?id=49890226)**

⬆️ 412 • 💬 130 • 19h ago • [jorgegarciaherrero.com](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)

---

**[There are no "rogue" AI agents](https://news.ycombinator.com/item?id=49868083)**

⬆️ 394 • 💬 268 • 2d ago • [eoinhiggins.substack.com](https://eoinhiggins.substack.com/p/there-are-no-rogue-ai-agents)

---

**[The problem is not AI code, but not knowing about system architecture or intent](https://news.ycombinator.com/item?id=49880312)**

If we think Is writing code dead, and AI is generating all codebases, I still think the bigger problem is people or full teams not knowing anything anymore about the system...

⬆️ 382 • 💬 239 • 1d ago • [Simon Späti's Second Brain](https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/)

---

**[Nvidia wants to put a watchdog chip next to every AI agent](https://news.ycombinator.com/item?id=49879883)**

Nvidia says its new software could have prevented OpenAI's Hugging Face incident.

⬆️ 223 • 💬 292 • 1d ago • [CNBC](https://www.cnbc.com/2026/09/28/nvidia-releases.html)

---

**[AI needs $6T in annual revenue to justify data centre boom](https://news.ycombinator.com/item?id=49898952)**

Data centre sizes and costs are doubling about every 12 to 16 months

⬆️ 197 • 💬 287 • 9h ago • [The National](https://www.thenationalnews.com/future/technology/2026/09/29/ai-industry-needs-to-earn-6-trillion-by-2031-to-justify-data-centres/)

---

**[Thinking fast and slow in AI: The role of metacognition (2021)](https://news.ycombinator.com/item?id=49873241)**

AI systems have seen dramatic advancement in recent years, bringing many applications that pervade our everyday life. However, we are still mostly seeing instances of narrow AI: many of these recent developments are typically focused on a very limited set of competencies and goals, e.g., image interpretation, natural language processing, classification, prediction, and many others. Moreover, while these successes can be accredited to improved algorithms and techniques, they are also tightly linked to the availability of huge datasets and computational power. State-of-the-art AI still lacks many capabilities that would naturally be included in a notion of (human) intelligence.
  We argue that a better study of the mechanisms that allow humans to have these capabilities can help us understand how to imbue AI systems with these competencies. We focus especially on D. Kahneman's theory of thinking fast and slow, and we propose a multi-agent AI architecture where incoming problems are solved by either system 1 (or "fast") agents, that react by exploiting only past experience, or by system 2 (or "slow") agents, that are deliberately activated when there is the need to reason and search for optimal solutions beyond what is expected from the system 1 agent. Both kinds of agents are supported by a model of the world, containing domain knowledge about the environment, and a model of "self", containing information about past actions of the system and solvers' skills.

⬆️ 176 • 💬 78 • 2d ago • [arXiv.org](https://arxiv.org/abs/2110.01834)

---

**[What would a serious AI product look like?](https://news.ycombinator.com/item?id=49876148)**

Deciphering Glyph, the blog of Glyph Lefkowitz.

⬆️ 170 • 💬 80 • 1d ago • [blog.glyph.im](https://blog.glyph.im/2026/09/serious-ai-product.html)

---

---

## YouTube Videos: "ai"

**[Sam Altman on Nvidia&#39;s new AI guardrails: I don&#39;t think it&#39;s a full solution](https://www.youtube.com/watch?v=IpbsBpgT0Bs)**

Sam Altman sits down with CNBC's Kate Rooney from OpenAI DevDay 2026.

📺 CNBC Television

👁️ 15K • 👍 78 • 💬 29 • ⏱️ 5:19 • 9h ago

---

**[OpenAI unveils new AI agent called &quot;dots&quot;](https://www.youtube.com/watch?v=J0Tk_voS0oY)**

OpenAI has revealed its newest AI agent, "dots." CBS News' Lauren Fichten reports. CBS News 24/7 is the premier anchored ...

📺 CBS News

👁️ 14K • 👍 122 • 💬 35 • ⏱️ 5:01 • 7h ago

---

**[Bill Gates’s Blunt Warning on A.I. | The Ezra Klein Show](https://www.youtube.com/watch?v=A_156w0aYtU)**

Bill Gates thinks A.I. alarmism hasn't gone far enough. He believes the years ahead will be marred by catastrophic cyberattacks, ...

📺 The Ezra Klein Show

👁️ 318K • 👍 5K • 💬 1K • ⏱️ 1:13:50 • 13h ago

---

**[Trump &amp; AI execs sign &#39;morally binding&#39; commitment after summit](https://www.youtube.com/watch?v=oB0PjEkLHWs)**

President Donald Trump showed no sign he wants a slowdown in the development of AI technology after convening with top tech ...

📺 CNN

👁️ 65K • 👍 455 • 💬 513 • ⏱️ 12:13 • 7h ago

---

**[AI Writing Is Getting Harder to Catch #ai #aiwriting #ainews](https://www.youtube.com/watch?v=tVKRAwbvkmk)**

Source: https://graphite.io/five-percent/research/ai-tells#tells-vary-over-time.

📺 Better Stack

👁️ 3K • 👍 202 • 💬 13 • ⏱️ 3:00 • 3h ago

---

**[ALERT: Did Anthropic&#39;s Just Pop AI Bubble?](https://www.youtube.com/watch?v=6OJHvQYrIc4)**

A leaked S-1 that filled in a lot of missing pieces. Maybe, for Anthropic and the AI bubble, too much. The upshot is...this time is ...

📺 Eurodollar University

👁️ 68K • 👍 2K • 💬 349 • ⏱️ 29:51 • 9h ago

---

**[AI risks: Will artificial intelligence really kill us all?](https://www.youtube.com/watch?v=zW2GaUwDQyA)**

Correspondent David Pogue talks with AI experts Daniel Kokotajlo, Geoffrey Hinton and Alex Turner about the risks inherent in ...

📺 CBS Sunday Morning

👁️ 186K • 👍 1K • 💬 282 • ⏱️ 8:34 • 2d ago

---

**[Bill Gates: AI is powerful enough to cause &#39;a billion deaths&#39;](https://www.youtube.com/watch?v=aaopxmz-fwU)**

Tech leaders are warning about the catastrophic harms posed by artificial intelligence, if left unchecked by government oversight.

📺 CNN

👁️ 192K • 👍 947 • 💬 682 • ⏱️ 9:03 • 1d ago

---

**[How to Build the PERFECT AI Agent with 1 Prompt Using Claude](https://www.youtube.com/watch?v=g-3EealqfMM)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Jake One Page

👁️ 5K • 💬 5 • ⏱️ 22:48 • 14h ago

---

**[How to Create Viral AI Storytelling Shorts](https://www.youtube.com/watch?v=ip9WIoX0jU4)**

Make Your Own AI Short https://tolt.link/viralaishorts In this video, I show how to build viral AI storytelling Reels from start to ...

📺 Isa does AI

👁️ 10K • 💬 1 • ⏱️ 14:41 • 13h ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 4,530 • 5d ago

---

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 23,674 • ❤️ 1,547 • 6d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,152,523 • ❤️ 2,453 • 1d ago

---

**[TeleOCR](https://huggingface.co/XingChen-AGI/TeleOCR)**

*XingChen-AGI*

TeleOCR is a lightweight Vision-Language Model for unified document parsing of both digital and camera-captured documents, achieving state-of-the-art performance on benchmarks like OmniDocBench with capabilities in handling complex layouts and geometric distortions.

`image-text-to-text` `1.4B`

⬇️ 30,354 • ❤️ 879 • 1d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 64,362 • ❤️ 2,664 • 2h ago

---

**[CLM-v0.1-8B](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)**

*CLM*

CLM-v0.1-8B is a text-ranking model based on Qwen3-8B, utilizing contrastive learning for state-action connection. It excels in zero-shot performance for agentic tasks with low latency and achieves state-of-the-art results when fine-tuned as a verifier for benchmarks like DeepSWE and Terminal-Bench.

`text-ranking`

⬇️ 1,910 • ❤️ 531 • 5d ago

---

**[Nemotron-3-Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization)**

*NVIDIA*

Nemotron-3 Diarization is an open-weight model for "who spoke when" audio analysis, supporting up to 8 speakers with streaming and offline inference capabilities. It's ideal for applications requiring real-time or batch speaker segmentation, such as meeting transcription or call center analytics.

`voice-activity-detection` `99.2M`

⬇️ 30,931 • ❤️ 520 • 5d ago

---

**[ZDTaichu5.0-9B](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B)**

*zidongtaichu*

ZDTaichu5.0-9B is a multimodal foundation model excelling in general visual understanding, spatial reasoning, and agentic tool use, supporting text, images, and any-resolution video inputs for embodied AI research and complex visual question answering.

`image-text-to-text` `9.8B`

⬇️ 11,836 • ❤️ 1,963 • 9d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 46,557 • ❤️ 1,809 • 11d ago

---

**[Qwen-Image-2.1-viggle-turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo)**

*Viggle AI*

Qwen-Image-2.1-viggle-turbo is a highly efficient text-to-image and image editing model, achieving comparable quality to its base model in just 6 transformer passes. It excels at rapid, high-fidelity image generation and instruction-driven edits using few-shot learning.

`text-to-image` `7.1B`

⬇️ 190,649 • ❤️ 427 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 148 • 💬 6 • ⭐ 109,269 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972)**

*Peng Xia, Rujun Han, Zifeng Wang et al. (14 authors)*

🏢 Google

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

▲ 216 • 💬 2 • ⭐ 904 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24972) • [💻 code](https://github.com/google-research/rrsi) • [🔗 project](https://regularized-rsi.com/)

---

**[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://huggingface.co/papers/2604.09557)**

*Talor Abramovich, Maor Ashkenazi, Carl et al. (9 authors)*

🏢 NVIDIA

Speculative Decoding evaluation requires diverse workloads to accurately measure performance, which existing benchmarks lack, prompting the introduction of SPEED-Bench for standardized assessment across semantic domains and serving regimes.

▲ 16 • 💬 2 • ⭐ 5,073 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.09557) • [💻 code](https://github.com/NVIDIA/Model-Optimizer) • [🔗 project](https://huggingface.co/blog/nvidia/speed-bench)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,560 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 75 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 72 • 💬 2 • ⭐ 66,323 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 263 • 💬 5 • ⭐ 17,875 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Training Object Permanence in World Models](https://huggingface.co/papers/2609.28654)**

*Haotian Zhang, Fengyuan Yu, Dezhi Luo et al. (31 authors)*

🏢 Carnegie Mellon University

Object permanence and solidity are hallmarks of human cognitive priors. Recent studies show that video generation models, a paradigmatic class of current world models, have begun to show emerged reasoning abilities, making them ideal candidates for building human-like physical intelligence. Do video models have emerged object permanence in them? If not, could we train them with a core-cognition inspired dataset? We introduce WROP (World Reasoning with Object Permanence), a data infrastructure of 150 hand-designed cognitive science inspired tasks, divided into six cognitive categories. We build Blender generators that randomize speed, lighting, camera angle, and other nuisance parameters while preserving each task's cognitive structure, yielding 10,000+ samples per task. We release a 1.5M-sample training corpus and a 300-question exam. On this exam we evaluate 14 video models: 3 reference-to-video, 7 edit, and 4 continuation, among which PWM-WROP, our 16B world model. In a blind pairwise Elo study, PWM-WROP ranks first among continuation models and third overall, behind only a statistical tie between two reference-to-video models. We release the data, exam, model answers, scores, weights, and PWM, our native-PyTorch training stack on AWS Trainium2.

▲ 237 • 💬 2 • ⭐ 394 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.28654) • [💻 code](https://github.com/hokindeng/object-permanence) • [🔗 project](https://www.object-permanence.world/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 177 • 💬 19 • ⭐ 68,198 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 45 • 💬 1 • ⭐ 33,982 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.2k • 🔱 2.2k • 18h ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 5.1k • 🔱 246 • 7d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.9k • 🔱 307 • 2d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 3.9k • 🔱 442 • 5d ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `llm` `mcp` `news-aggregator` `rss`

⭐ 3.5k • 🔱 990 • 10h ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 3.0k • 🔱 55 • 7d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.7k • 🔱 505 • 13d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 2.0k • 🔱 299 • 2h ago

---

**[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)**

Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.

`Python` `agent-memory` `ai-agents` `claude-code` `codex` `llm`

⭐ 1.8k • 🔱 115 • 1d ago

---

**[pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise)**

Your Cheat Sheet For AI Engineering Interviews at Top AI Companies - Questions and Answers.

`Markdown` `ai` `ai-engineering` `ai-engineering-interview` `ai-interview` `ai-interview-questions`

⭐ 1.6k • 🔱 155 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*
