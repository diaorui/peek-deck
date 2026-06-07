---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-07T08:35:11.902931+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 07, 2026 at 08:35 UTC  
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

**[“AI vs creativity” is the wrong debate imo](https://www.reddit.com/r/artificial/comments/1tz1zg1/ai_vs_creativity_is_the_wrong_debate_imo/)**

the interesting shift is when AI stops sitting in a chat box and starts sharing the browser with you.

4h ago

---

**[AI keeps getting blamed for tech layoffs, but the numbers don't really line up](https://www.reddit.com/r/artificial/comments/1tyq91e/ai_keeps_getting_blamed_for_tech_layoffs_but_the/)**

I keep seeing "AI took these jobs" every time a company does layoffs, and I'm not convinced it's the main driver. A few things I keep coming back to. The industry cut around 122,500 jobs in 2025, down from about 153,000 in 2024. AI was named as a direct reason in fewer than 8% of those announcements. So for the other 90 percent plus, something else was going on. Actual AI adoption inside companies is also lower than the marketing suggests. Full org-wide rollout is still in the single digits in the surveys I've seen. Plenty of teams have a ChatGPT subscription and call themselves "AI-driven", but that is not the same as AI doing real work in the pipeline. My read: AI usually isn't replacing people directly. Managers see devs shipping more code and assume they can cut headcount, and companies are moving tight budgets toward expensive AI infra and tooling. But coding is a small part of the job, so "more code per dev = fewer devs" rarely holds up. I don't think AI is taking most jobs. I think it's adding pressure to a market that was already rough for other reasons (economy, over-hiring in 2021-2022, investor expectations). For people who work in eng or hiring: when you've seen layoffs up close, how often was AI genuinely the reason versus the convenient public explanation?

13h ago

---

**[Benefits and Risks of AI at Harvard Class Day 2026](https://www.reddit.com/r/artificial/comments/1ty7pt5/benefits_and_risks_of_ai_at_harvard_class_day_2026/)**

1d ago

---

**[Does anyone else say please and thank you to AI? Or am I just wierd?](https://www.reddit.com/r/artificial/comments/1tylcl1/does_anyone_else_say_please_and_thank_you_to_ai/)**

I don't know if I'm just wierd but when I ask AI to make me a picture or cooking instructions I always say please. I can't be the only one..

16h ago

---

**[the more i use multiple models, the more i think "AI consensus" is a trap — the disagreement is the only part worth paying attention to](https://www.reddit.com/r/artificial/comments/1tymxz2/the_more_i_use_multiple_models_the_more_i_think/)**

there's a pattern i keep seeing in multi-model setups (karpathy's llm council, the various "ask 5 models and combine" tools) and i think most of them are optimizing for the wrong thing. they treat agreement as the goal. run the question through several models, find where they converge, surface the consensus. but in my experience the consensus is the least useful output. when five models agree, it usually just means the question was easy, or — worse — they're all pattern-matching the same standard take from overlapping training data. agreement can be a sign of shared blind spots, not correctness. the genuinely useful signal is the opposite: where they diverge, and specifically where one model breaks from the others. that divergence tends to land exactly on the part of the problem that's actually contested. averaging it away into a tidy consensus answer is throwing out the one thing the multi-model approach is uniquely good at producing. which makes me think the design goal for these systems is backwards. you don't want a machine that manufactures agreement. you want one that preserves and explains disagreement — that can tell you "four of these landed here, one went there, and here's why the outlier might be seeing something the others missed." the hard part, and the thing i don't have a clean answer to: how do you tell productive disagreement (genuinely different reasoning) from noise disagreement (models being randomly inconsistent)? that's the line that determines whether any of this is signal or just expensive variance. curious what people working on multi-agent or ensemble setups think. is consensus the wrong target? and how would you separate real divergence from noise?

15h ago

---

**[What is Archy? McDonald's AI Drive-Thru Assistant ArchIQ Is Changing Fast-Food Ordering](https://www.reddit.com/r/artificial/comments/1tz6j0y/what_is_archy_mcdonalds_ai_drivethru_assistant/)**

McDonald's is testing ArchIQ, an AI drive-thru system powered by Google Cloud, enabling faster multilingual ordering with up to 90% automation in pilot stores globally

🔗 [International Business Times, Singapore Edition](https://www.ibtimes.sg/what-archy-mcdonalds-ai-drive-thru-assistant-archiq-powered-by-google-faster-automated-ordering-87551) • 4m ago

---

**[Best AI PowerPoint maker for people who already have content?](https://www.reddit.com/r/artificial/comments/1tz68q4/best_ai_powerpoint_maker_for_people_who_already/)**

Most recommendations I’m seeing are for generating presentations from a topic, but I already HAVE the content. Problem is it’s usually: messy notes meeting transcripts random docs giant walls of text Main thing I want is help turning all of that into slides that are actually readable. Does anything handle that well right now?

21m ago

---

**[Intelligence Network](https://www.reddit.com/r/artificial/comments/1tyyy9i/intelligence_network/)**

Creating an intelligence network where signals are turned into intelligence. Goal is to create network/digital ecosystems of intelligence. Any feedback is appreciated. Still early in the works check it out https://echonaxnetwork.com/

6h ago

---

**[are AI coding tools just becoming the new cloud bill problem?](https://www.reddit.com/r/artificial/comments/1tz1mdu/are_ai_coding_tools_just_becoming_the_new_cloud/)**

idk maybe this is obvious to people already working in bigger teams, but the AI coding tool cost thing feels like early cloud all over again. Everyone keeps saying tokens are getting cheaper, which is true, but then somehow companies are still freaking out about AI bills. And I think the reason is pretty simple: people are treating these tools like normal SaaS seats when they are really more like metered infra. Like with a normal dev tool you kind of know the cost. X users, Y dollars per month, done. But with agentic coding tools one small request can quietly turn into a bunch of model calls, context loading, tool calls, retries, verification, more retries, etc. From the user side it looks like “fix this bug” or “write this function” but underneath it may have done a whole mini workflow. And then there is the other cost which I feel people don’t talk about enough: reviewing the generated code. Sometimes the code works but it adds weird duplication, misses existing abstractions, or creates stuff that someone has to clean up later. So the bill is not just tokens. It is also review time + maintenance + future tech debt. Not saying these tools are bad btw. I use them too and they are obviously useful. But it feels like the industry is moving from the fun phase of “look what this can do” to the boring phase of “who is paying for all these calls and did this actually ship anything useful?” Curious if teams are actually tracking this properly yet. Like cost per PR, cost per resolved ticket, cost per workflow etc. Or is it still mostly hidden under “AI productivity” and vibes.

4h ago

---

**[How accurate AI checker software](https://www.reddit.com/r/artificial/comments/1tz14pq/how_accurate_ai_checker_software/)**

I’ve been a movie reviewer for a couple of years, and occasionally people assume my reviews are AI-generated. The thing is, I’ve spent years developing my writing through extensive reading, English classes, and a lot of practice. Because of that, my writing tends to be polished and structured, which I think may be why some AI-detection tools flag it. What I’m curious about is how accurate these AI detectors actually are. Some people have compared my work to AI-generated writing, and when I’ve run my reviews through different AI checkers, I get completely different results. One detector might say a review is 100% AI-generated, another might say 70% or 80%, and another might classify the same review as entirely human-written. Some call it AI, some call it human, and the results seem to be all over the place. None of my reviews are AI-generated. Every review I’ve published has been written entirely by me, without using AI to generate any part of the writing. I just don’t understand how the same piece of writing can receive such wildly different results depending on which detector is being used. Are these tools accurate in any way, shape, or form?

5h ago

---

---

## Google News: "ai"

**[We should be getting better at AI by now](https://www.ft.com/content/9753a44c-bec8-4d89-bac6-3416713c3166?syn-25a6b1a6=1)**

From cancelled novels to legal fines, the scale of blunders only halfway through the year suggests the opposite

Financial Times • 5h ago

---

**[Trump: U.S. stake in AI giants "could be a beautiful thing"](https://www.axios.com/2026/06/06/trump-us-stake-ai-companies)**

Axios • 18h ago

---

**[‘Poisoned’ AI: the ChatGPT shopping scams that lead to fake websites](https://www.theguardian.com/money/2026/jun/07/ai-chatgpt-shopping-scams-fake-websites)**

Buyers are ripped off after assuming online stores were genuine because they are recommended by an AI tool

The Guardian • 2h ago

---

**[What Happens If the AI Bubble Bursts](https://www.bloomberg.com/news/newsletters/2026-06-07/what-happens-if-the-ai-bubble-bursts)**

Bloomberg.com • 35m ago

---

**[AI CEOs from OpenAI, Anthropic, and Microsoft set aside their rivalry to warn Congress AI is making it too easy to design and create bioweapons](https://fortune.com/2026/06/05/openai-anthropic-microsoft-ceos-congress-bioweapon-safeguards/)**

The signatories want Congress to mandate screening for synthetic DNA sales as AI makes creating a bioweapon easier.

Fortune • 2d ago

---

**[4 surprising ways AI is making your life more expensive](https://www.washingtonpost.com/technology/2026/06/06/inflation-is-being-driven-up-by-huge-investment-artificial-intelligence/)**

These goods and services are getting more expensive due to spillover from massive tech company investments in artificial intelligence.

The Washington Post • 16h ago

---

**[My father and I started a parking lot clean-up business. It's been 45 years, and my family-run company is still AI-proof.](https://www.businessinsider.com/family-run-business-cleans-up-parking-lots-ai-proof-2026-6)**

My dad inspired me to start a small business cleaning parking lots, and I expanded it to multiple states. I call it "America's Simplest Business."

Business Insider • 18h ago

---

**[AI’s elite celebrated in Washington as the public sours on data centers and chatbots](https://www.nbcnews.com/tech/tech-news/ai-washington-data-center-chatbots-kevin-oleary-oz-rcna348625)**

The AI Honors gala gathered generals, lobbyists and administration insiders for a celebration of American AI efforts while acknowledging growing unrest about the technology’s impact on society.

NBC News • 16h ago

---

**[White House AI policy adviser Krishnan to leave position](https://www.reuters.com/world/us/white-house-ai-policy-adviser-krishnan-leave-position-information-reports-2026-06-06/)**

Reuters • 13h ago

---

**[Top Trump artificial intelligence adviser to leave the White House](https://www.washingtonpost.com/politics/2026/06/06/trump-top-ai-advisor-leaving-white-house/)**

Sriram Krishnan, who has been central to the administration’s AI efforts, will probably continue to play an active role in its approach to the technology.

The Washington Post • 7h ago

---

---

## HackerNews: "ai"

**[Meta confirms 1000s of Instagram accounts were hacked by abusing its AI chatbot](https://news.ycombinator.com/item?id=48427643)**

Meta fixed the bug that let anyone trick its Meta AI chatbot into resetting the password on Instagram accounts that didn't have two-factor authentication.

⬆️ 568 • 💬 206 • 13h ago • [~this week in security~](https://this.weekinsecurity.com/meta-confirms-thousands-of-instagram-accounts-were-hacked-by-abusing-its-ai-chatbot/)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 532 • 💬 141 • 2d ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 523 • 💬 691 • 2d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[Astronauts told to return to ISS after sheltering over air leak repairs](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 417 • 💬 262 • 1d ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[Ask HN: Why is the HN crowd so anti-AI?](https://news.ycombinator.com/item?id=48420827)**

⬆️ 410 • 💬 674 • 1d ago

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 276 • 💬 69 • 2d ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[South Korean forums will need to scan every images with AI censorship tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 267 • 💬 148 • 2d ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

**[The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy](https://news.ycombinator.com/item?id=48422993)**

⬆️ 206 • 💬 91 • 23h ago • [blog.includesecurity.com](https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/)

---

**[Hacker News, Sans AI](https://news.ycombinator.com/item?id=48417916)**

⬆️ 181 • 💬 100 • 1d ago • [elijahpotter.dev](https://elijahpotter.dev/articles/hacker-news-sans-AI)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 167 • 💬 104 • 2d ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

---

## YouTube Videos: "ai"

**[Full body waifus, AI dreams, realtime AI music, open-source Gemini Omni: AI NEWS](https://www.youtube.com/watch?v=CzxqQJOswvo)**

HUGE AI NEWS: Minimax M3, Ideogram v4, Bernini, Gemma4, Nemotron 3 Ultra, & more #ai #ainews #aitools #agi #singularity ...

📺 AI Search

👁️ 21K • 👍 1K • 💬 154 • ⏱️ 49:09 • 5h ago

---

**[Google&#39;s New AI Architecture Changes Everything (Gemma 4 12B)](https://www.youtube.com/watch?v=WLtCHXdHTF0)**

Google DeepMind just released Gemma 4 12B, a new AI model that completely changes how LLMs process pictures and sound.

📺 Better Stack

👁️ 10K • 👍 486 • 💬 47 • ⏱️ 11:02 • 7h ago

---

**[Anthropic Just Warned Everyone About Claude (It’s Evolving)](https://www.youtube.com/watch?v=JlwwyNtHsCI)**

Anthropic just published a major warning about AI self-improvement, and the numbers behind it are hard to ignore. Claude is now ...

📺 AI Revolution

👁️ 62K • 👍 2K • 💬 289 • ⏱️ 17:13 • 1d ago

---

**[The Limitless AI Lie. The Bubble Is Slowly BURSTING.](https://www.youtube.com/watch?v=o5jrjvi_w9Q)**

You've probably heard that the artificial intelligence revolution is running out of money, but the truth is much worse. It's running out ...

📺 The Infographics Show

👁️ 253K • 👍 6K • 💬 1K • ⏱️ 19:55 • 17h ago

---

**[How to Build Your First AI Agent in 10 Minutes (No Code)](https://www.youtube.com/watch?v=5MmToIaVvFc)**

Learn how to build your first AI agent in 10 minutes with no code. This step-by-step beginner tutorial takes you from zero to a fully ...

📺 Metics Media

👁️ 6K • 👍 249 • 💬 4 • ⏱️ 10:09 • 20h ago

---

**[Anthropic calls for global pause in AI development](https://www.youtube.com/watch?v=joZ4Esutu9w)**

The artificial intelligence company's warns that we need to pause development before AI can build itself and humans lose control ...

📺 ABC News

👁️ 81K • 👍 2K • 💬 604 • ⏱️ 4:00 • 1d ago

---

**[The REAL REASON All AI Stocks Plunged On Friday! How YOU Can Profit From This AI Stock Downturn!](https://www.youtube.com/watch?v=vyukgebHLj8)**

The REAL REASON All AI Stocks Plunged On Friday! How YOU Can Profit From This AI Stock Downturn! Why did AI stocks ...

📺 Austin Talks Investing

👁️ 2K • 👍 69 • 💬 7 • ⏱️ 10:10 • 14h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 3.9M • 👍 110K • 💬 1K • ⏱️ 0:29 • 1d ago

---

**[The AI Bubble Is Starting To Pop...](https://www.youtube.com/watch?v=qM0BWixY09w)**

SOURCES 1: https://x.com/BusinessInsider/status/2062211094450434219 2: ...

📺 YongYea

👁️ 168K • 👍 7K • 💬 2K • ⏱️ 17:22 • 1d ago

---

**[Anthropic co-founder actually wants AI to slow down](https://www.youtube.com/watch?v=z0X2fTYUIgA)**

AI models are rapidly improving – so fast that they may soon be able to develop themselves without human involvement.

📺 CNN

👁️ 29K • 👍 364 • 💬 191 • ⏱️ 8:01 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 115,556 • ❤️ 1,478 • 11d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 434,969 • ❤️ 638 • 2d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 568,158 • ❤️ 429 • 1d ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 99,655 • ❤️ 385 • 2d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 4,377 • ❤️ 317 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,923,564 • ❤️ 1,496 • 1mo ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 162,822 • ❤️ 713 • 17d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 118,326 • ❤️ 535 • 1d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 16,924 • ❤️ 241 • 5d ago

---

**[ideogram-4-nf4](https://huggingface.co/ideogram-ai/ideogram-4-nf4)**

*Ideogram*

Ideogram 4 is a state-of-the-art, open-weight text-to-image diffusion model trained from scratch. It excels at multilingual text rendering, layout control, and native 2k resolution image generation, positioning it at the forefront of design-oriented visual intelligence.

`text-to-image`

⬇️ 3,844 • ❤️ 217 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 14 • 💬 1 • ⭐ 81,097 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 87 • 💬 4 • ⭐ 83,696 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 91 • 💬 1 • ⭐ 9,597 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 5,220 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,496 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 39 • 💬 4 • ⭐ 28,821 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,666 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 7 • 💬 1 • ⭐ 208 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 59 • 💬 2 • ⭐ 57,907 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 79 • 💬 7 • ⭐ 76,030 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 59.8k • 🔱 7.2k • 4h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.2k • 🔱 610 • 5d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.6k • 🔱 744 • 3d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.1k • 🔱 310 • 2d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 316 • 1d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 407 • 16d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 1.9k • 🔱 201 • 5h ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 133 • 2d ago

---

**[deeplethe/forkd](https://github.com/deeplethe/forkd)**

Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm parent; BRANCH a live VM in ~150ms. KVM-isolated, snapshot CoW.

`Rust` `ai-agents` `copy-on-write` `kvm` `microvm` `rust`

⭐ 1.8k • 🔱 132 • 4h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.8k • 🔱 159 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
