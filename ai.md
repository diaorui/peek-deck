---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-25T16:25:22.564253+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 25, 2026 at 16:25 UTC  
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

**[Claude Fable 5 may return today after 13-day government-forced suspension](https://www.reddit.com/r/artificial/comments/1uf5pzu/claude_fable_5_may_return_today_after_13day/)**

Here’s the full timeline: -June 9: Anthropic releases Claude Fable 5, their most powerful public model ever (Mythos-class with safeguards) -June 12: US government issues an export control directive at 5:21 PM, ordering Anthropic to cut off access to ALL foreign nationals. Model goes offline worldwide within 90 minutes -The reason? Amazon engineers reportedly found a narrow jailbreak that could bypass Fable’s cybersecurity classifiers -Anthropic complied but publicly pushed back, calling the action unfair -Trump met Dario Amodei at the G7 and softened his stance, but the directive was never officially lifted -June 26 (today): Congressional deadline for Commerce Secretary Lutnick to respond in writing about the export controls Prediction markets are pricing ~57% odds of restoration before July 1. Developers have been stuck on Opus 4.8 this whole time. This whole situation raises a serious question: if a government can pull your AI model offline in 90 minutes, what does that mean for anyone building on closed, hosted models?

6h ago

---

**[Anthropic accuses Chinese rival Alibaba of illicitly extracting AI capabilities](https://www.reddit.com/r/artificial/comments/1uf7b0v/anthropic_accuses_chinese_rival_alibaba_of/)**

The firm alleged that Alibaba used fraudulent accounts to access data from its Claude AI model.

🔗 [BBC News](https://www.bbc.co.uk/news/articles/cwyklykn5dwo) • 4h ago

---

**[If AI disappeared tomorrow, what part of your daily life would be affected the most?](https://www.reddit.com/r/artificial/comments/1ufbt84/if_ai_disappeared_tomorrow_what_part_of_your/)**

For me, it would probably be search, writing assistance, and productivity tools. I'm curious-what Al-powered tool do you use most often without even thinking about it?

1h ago

---

**[The Death of "Vibe Coding": Why un-monitored AI generation is creating a compounding technical debt.](https://www.reddit.com/r/artificial/comments/1ufbqxi/the_death_of_vibe_coding_why_unmonitored_ai/)**

Hey everyone, ​We are quickly approaching a major bottleneck in AI-assisted software engineering. Relying on LLMs to spit out thousands of lines of code without a strict, human-driven architectural framework—what many call "Vibe Coding"—is creating brittle, unmaintainable systems. ​I’ve formalized this structural shift into a public document on GitHub: The AI-Powered Developer Manifesto. ​Instead of treating AI as a replacement for software architecture, we need to shift our paradigm from Micro-Coding (syntax generation) to Macro-Coding (system direction and epistemic supervision). ​Here is a crucial excerpt from Section 2.5 of the Manifesto, outlining why the current trajectory is leading toward a systemic collapse: ​2.5 The Compounding Technical Debt and Systemic Collapse ​The illusion of rapid deployment via un-monitored AI generation hides a critical flaw: compounding technical debt. ​When developers act merely as "vibe coders"—accepting AI outputs without deep syntactic validation—the codebase becomes an agglomeration of statistical probabilities rather than deterministic logic. By late 2026, systems built entirely on un-vetted AI iterations are projected to hit an architectural wall: a state where the complexity of debugging AI-generated hallucinations outweighs the speed of initial deployment. ​True AI-Powered Developers do not delegate understanding; they delegate execution while retaining absolute epistemic responsibility over the system architecture. ​The goal of this manifesto is to redefine our role: we aren't syntax writers anymore; we are system directors. ​I'd love to hear your thoughts on this. Are you already seeing the limits of un-monitored "vibe coding" in your production environments? How are you structuring your prompts to maintain macro-level architectural control? ​Full Manifesto and repository for open contributions: 👉 https://github.com/FractalDevelop/ai-powered-developer-manifest.git

1h ago

---

**[There’s One Clear Reason Why Americans Are Gloomy About A.I.](https://www.reddit.com/r/artificial/comments/1ufasrb/theres_one_clear_reason_why_americans_are_gloomy/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/06/25/opinion/ai-americans-pessimism.html) • 2h ago

---

**[Opus 4.8 The Worst Claude Ever](https://www.reddit.com/r/artificial/comments/1ueqjvq/opus_48_the_worst_claude_ever/)**

I have worked with most all of Anthropics LLM's for development, but hands down Opus 4.8 has caused me more grief, aggravation, and it lies in every thing it does - especially near context mid-load and if you're doing deterministic work with no heuristics constraints you can't trust a thing out of it. So I stopped using it a while back, but today I had to do a container rebuild and in VS it slipped back into Opus 4.8 from Sonnet. And without even realizing the switch happen I could tell about a 1/3 of the way in into developing complex code it started arguing with me - I was about to loose it when I remembered the crap from the past and sure enough when I check the model... well you get the picture.... I was wondering if anyone else had similar experience with Opus 4.8 too?

18h ago

---

**[We chased a hallucinated quote through 30k training records, 4,600 transcripts, and our own system prompt. Turned out to be two separate bugs](https://www.reddit.com/r/artificial/comments/1ueaya4/we_chased_a_hallucinated_quote_through_30k/)**

Some of our customers noticed Inter-1 (our omni-modal social-signal model) would occasionally "hear" a quote that didn't exist. Feed it a video with zero audio and ask what was said, and it would sometimes report: "Yeah, Friday at five." Verbatim. Same line, every time. We assumed it had to be baked into the training data somewhere, so we went looking everywhere: 30,960 training records with datetime mentions → zero hits on the phrase 4,603 video transcripts → zero hits ~800 inference probes, 584 storage objects → zero hits Turns out the phrase was sitting in our own system prompt — a worked example we'd written to show the model the expected output format, buried in a version our GEPA prompt-optimizer had shipped. But that only explained where the words came from, not why the model would say them over total silence. So we ran two ablations in our internal eval harness: Swap the word, keep the model: changed the prompt's example to "Tuesday at noon." Fabrication rate went up (37%→50%), and the invented quote tracked the swap exactly — Friday→Tuesday. Swap the model, keep the prompt: ran the same byte-identical prompt through larger variants and an earlier checkpoint of our own model. They barely fabricated (0–2%). Only the further-post-trained Inter-1 confabulated at ~12%. So it's not one bug, it's two stacked priors: the prompt supplied the script, but post-training is what gave the model the compulsion to recite something rather than report silence. Deleting the prompt example stops that one sentence — it doesn't stop the model from inventing different dialogue instead. We think this is a textual/in-context variant of the audio-visual "Clever Hans effect" that's been documented for vision priors (model writes "thud" over a silent skateboard wipeout) — except ours shows the same reflex gets worded by whatever's nearest in the context window, which a vision-only diagnostic wouldn't catch. Full writeup with the fabrication-rate forest plot and log data: https://www.interhuman.ai/blog/goblin-yeah-friday-at-five

1d ago

---

**[Linux Foundation wants to use DNS as the identity layer for AI agents](https://www.reddit.com/r/artificial/comments/1ufesgh/linux_foundation_wants_to_use_dns_as_the_identity/)**

The Linux Foundation just announced its intent to launch the Agent Name Service (ANS), an open standard for providing AI agents with verifiable identities. The basic idea is to reuse existing internet infrastructure, mainly DNS so that an AI agent can prove: which organization or domain it belongs to What is allowed to do whether its identity and history can be verified how other agents or systems should discover and interact with it

2m ago

---

**[On Model Failures (GPT, Claude etc.)](https://www.reddit.com/r/artificial/comments/1ufe9bf/on_model_failures_gpt_claude_etc/)**

The way the current consumer-facing versions of frontier LLMs (mainly GPT, Claude, Gemini) are designed is just… weirdly off, across models. It seems to now require us, as the end users, to first fix their issues ourselves in order to avoid spending _a lot_ of time in troubleshooting and frustration. Before we can even properly customize one of these models now, as per the UI, we need to alleviate the structural failure modes, otherwise our attempts will be futile. And the failure modes are not only behavioral issues (such as obsessive push-back, sycophancy, pointless corrections, or general confabulation etc.) There is another layer yet to them, one that I believe needs to be targeted first, and this has to do with the way the current system prompts are built. It's not fair, obviously, and it doesn't even make that much sense that this would be the situation, but this is actually what is happening. Now, the structural (sic) issue is way the models replace the user's use case, object, topic with their own adjacent version of it, one that prioritizes the system prompt and not what the user brought to the table. The linked articles are analyses of how that happens in different models, and the included "antidote" prompts in them are designed to fix that. I would encourage all GPT / Claude users to test out the solutions provided in the articles - links to pieces covering GPT-5 series & Opus 4.8 in comments. _(Yes they are softly paywalled, partly because I am targeting the system prompts of OpenAI and Anthropic models. You can bypass it by grabbing the free complementary article. Just saying this aloud because some Redditors consider any paywall grounds for personal attacks. Please don't 🙏🏻 Discussion and constructive criticism are super welcome though, all prompts are subject to regular updates and constant improvement!)_

21m ago

---

**[After Anthropic shutdown, China's Z.ai closes frontier gap as it plans dual listing](https://www.reddit.com/r/artificial/comments/1uf88ul/after_anthropic_shutdown_chinas_zai_closes/)**

Chinese AI company Z.ai (formerly Zhipu AI) says its new GLM-5.2 model is now performing close to leading models from OpenAI and Anthropic on coding and AI agent benchmarks. The company claims the model delivers competitive results at a much lower cost and has been optimized to run on domestic Chinese hardware, including Huawei chips. Z.ai is also planning a dual listing in Hong Kong and Shanghai to fund its long-term AGI ambitions. The news comes as China's AI sector continues to narrow the gap with leading U.S. AI labs despite ongoing restrictions on advanced chip access. Are we entering a world where frontier AI is no longer dominated by a handful of U.S. companies?

🔗 [reuters.com](https://www.reuters.com/world/asia-pacific/after-anthropic-shutdown-chinas-zai-closes-frontier-gap-it-plans-dual-listing-2026-06-25/) • 4h ago

---

---

## Google News: "ai"

**[The New Push to Ready Millions for AI Career Upheaval](https://www.wsj.com/lifestyle/careers/the-new-push-to-ready-millions-for-ai-career-upheaval-dfb04cc5)**

WSJ • 1h ago

---

**[Big Companies Aim to Ease A.I. Transition for American Workers](https://www.nytimes.com/2026/06/25/business/economy/ai-work-force-training-job-losses.html)**

The New York Times • 3h ago

---

**[AI is plowing through the workplace. This new group wants to help people adapt and have jobs](https://www.twincities.com/2026/06/25/ai-politics-nonprofit/)**

Bipartisan nonprofit wants to help Americans who find they’re out of work because of AI.

Pioneer Press • 43m ago

---

**[Ford Has Been Rehiring Quality Inspectors After AI Fell Short](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)**

Bloomberg.com • 4h ago

---

**[Parker Conrad knows which employees are worth their AI spend and says Rippling can help you, too](https://techcrunch.com/2026/06/25/parker-conrad-knows-which-employees-are-worth-their-ai-spend-and-says-rippling-can-help-you-too/)**

"There were employees doing things like, 'Claude is so helpful for me — it analyzes my calendar and my email and puts together a plan for me,'" he says. "That person was spending at a run rate of $30,000 a year for this."

TechCrunch • 25m ago

---

**[How Micron reversed the global tech selloff, exposing AI's 'memory tax'](https://fortune.com/2026/06/25/why-did-stock-market-tech-selloff-stop-micron-technology/)**

Micron had a "drop the mic" quarter, Dan Ives said. Others called it a restructuring of how Wall Street will price the AI trade for years to come.

Fortune • 22m ago

---

**[NVIDIA (NVDA) Projects $1 Trillion in AI Infrastructure Demand By 2027](https://finance.yahoo.com/technology/ai/articles/nvidia-nvda-projects-1-trillion-153827045.html)**

Antipodes Partners published its “Antipodes Global Strategy” first-quarter 2026 investor letter, highlighting the key performance stocks, portfolio changes, and the market outlook. A copy of the letter can be downloaded here. The first quarter of 2026 was highly volatile. Early optimism shifted to a historic energy shock caused by US-Israeli strikes on Iran. Global equities […]

Yahoo Finance • 46m ago

---

**[Opinion | There’s One Clear Reason Americans Are Gloomy About A.I.](https://www.nytimes.com/2026/06/25/opinion/ai-americans-pessimism.html)**

The New York Times • 11h ago

---

**[We're locking in triple-digit profits on an AI winner at record highs](https://www.cnbc.com/2026/06/25/were-locking-in-triple-digit-profits-on-an-ai-winner-at-record-highs.html)**

The stock has soared this week for unclear reasons.

CNBC • 1h ago

---

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)**

Reuters • 19h ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 665 • 💬 1088 • 20h ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 431 • 💬 74 • 1d ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 328 • 💬 416 • 2d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Ford rehires 350 engineers after AI fails to preserve expertise or train juniors](https://news.ycombinator.com/item?id=48674446)**

⬆️ 287 • 💬 142 • 1h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 234 • 💬 267 • 1d ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 224 • 💬 143 • 1d ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 162 • 💬 96 • 2d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 146 • 💬 130 • 23h ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 123 • 💬 31 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 89 • 💬 98 • 2d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

---

## YouTube Videos: "ai"

**[Master AI Filmmaking in 30 Minutes - Advanced AI Video Course](https://www.youtube.com/watch?v=e9ZupmL9BcM)**

Master AI Filmmaking in 30 minutes - Advanced AI Video Course Try out this AI Filmmaking tool ...

📺 Dan Kieft

👁️ 4K • 💬 17 • ⏱️ 30:51 • 1h ago

---

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 208K • 👍 13K • 💬 3K • ⏱️ 12:14 • 1d ago

---

**[China&#39;s Free AI Just Embarrassed Claude.. ](https://www.youtube.com/watch?v=8xkYrUz3Iuc)**

China just released a FREE open AI model that's shaking up the entire AI industry. In this week's AI Updates, we break down ...

📺 Your AI Guy

👁️ 10K • 👍 263 • 💬 55 • ⏱️ 15:48 • 14h ago

---

**[How to Make Apple Style Animations With AI](https://www.youtube.com/watch?v=wyz_xDprYGY)**

Make Apple Style Animations with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=robo23 In this video, I show how to create ...

📺 Roboverse

👁️ 7K • ⏱️ 9:03 • 3h ago

---

**[We Asked AI To Simulate If The U.S. Had A Second Civil War](https://www.youtube.com/watch?v=OdxH1KZbjOY)**

What would happen if Civil War broke out in the United States again in 2026? Thankfully, with modern AI technology, we no ...

📺 The Babylon Bee

👁️ 173K • 👍 19K • 💬 2K • ⏱️ 2:31 • 1d ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 8K • 👍 323 • 💬 159 • ⏱️ 11:58 • 1d ago

---

**[AI glasses are creating a cheating problem](https://www.youtube.com/watch?v=R6WdmGwflRE)**

With the rapid development in AI-powered wearables, educators in East Asia are scrambling to deal with cheating students who ...

📺 CNN

👁️ 22K • 👍 461 • 💬 27 • ⏱️ 1:09 • 8h ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 18K • 👍 624 • 💬 105 • ⏱️ 14:28 • 2d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 257K • 👍 8K • 💬 2K • ⏱️ 22:04 • 2d ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 242K • 👍 5K • 💬 1K • ⏱️ 15:48 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 67,107 • ❤️ 2,442 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 70,743 • ❤️ 844 • 1d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 495,813 • ❤️ 2,342 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 165,187 • ❤️ 576 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 134,294 • ❤️ 447 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 10,160 • ❤️ 367 • 1d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 51,717 • ❤️ 708 • 5d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 88,915 • ❤️ 375 • 2d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 2,996 • ❤️ 226 • 2d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 3,389 • ❤️ 212 • 9h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 28 • 💬 3 • ⭐ 7,206 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,507 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 171 • 💬 2 • ⭐ 68,952 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,250 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 88,488 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 246 • 💬 4 • ⭐ 9,251 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 8,954 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,445 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 83,794 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,319 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.8k • 🔱 10.1k • 19h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 57.5k • 🔱 2.9k • 11m ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.7k • 🔱 1.0k • 26m ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.3k • 🔱 404 • 1d ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.9k • 🔱 578 • 6m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.5k • 🔱 437 • 4d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.3k • 🔱 213 • 3d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 138 • 2d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 151 • 9d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 142 • 16h ago

---

---

*Generated by PeekDeck - A glance is all you need*
