---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-25T04:45:41.171838+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 25, 2026 at 04:45 UTC  
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

**[I simply do not understand how massively expensive AI and robotics are expected to be more cost effective than humans.](https://www.reddit.com/r/artificial/comments/1tmffqn/i_simply_do_not_understand_how_massively/)**

Can someone help me understand this? I mean, how on earth are these companies who are planning to replace us all with beep boops expecting these unimaginably high expense technologies to be better for their bottom line than just paying us low wage unwashed masses? I mean, some dude (respectfully, I use that term genderlessly) here just posted about min wage in their area being $7.25! You are not getting a robot or AI that costs less annualized. Even adding in annual benefits - that is a steal compared to data centers and complex robots who will be absurdly expensive to fix when they break. I’m a white collar worker with deep knowledge of worker costs, even at the top it’s cheaper than what all of this new buggy crap is going to cost. I’m so confused. What am I missing? Why are the evil overlords not interested in our already too cheap labor? EDIT: I just want to thank everyone for the discussion on this. There are so many different situations and buckets of AI, it can be an imprecise topic, but the high level viewpoints have been helpful.

13h ago

---

**[Testing a Cold War-Era AI on Satellite Image Datasets](https://www.reddit.com/r/artificial/comments/1tmnb54/testing_a_cold_warera_ai_on_satellite_image/)**

I came across a cool model developed during the Cold War. I wanted to see how it would perform at image recognition, so I downloaded the UC Merced Land Use Dataset and wrote a script to add Gaussian noise to the photos and measure performance over a series of trials using Monte Carlo simulations. It is very efficient and appears well suited for FPGA implementation. It only uses about 50 MB of RAM. The satellite photos are converted to grayscale, downscaled to roughly 32×32, and converted into a fingerprint that is roughly 128 bytes in size. Therefore, the database of 800 TIFs is about 100 KB total. I’ll include the test and debug images so you can see how the process works. The model basically selects the stored pattern that best matches the noisy input based on what it has learned from the data.

8h ago

---

**[How to Hit Claude Limits in One Click](https://www.reddit.com/r/artificial/comments/1tmpfa9/how_to_hit_claude_limits_in_one_click/)**

6h ago

---

**["I'm retired. I showed my MS Paint paintings to AI for feedback. It accidentally invented an entire fake art movement. Google believes it's real."](https://www.reddit.com/r/artificial/comments/1tmb7c6/im_retired_i_showed_my_ms_paint_paintings_to_ai/)**

"I'm retired and started showing my MS Paint paintings to AI for criticism. The AI invented feuding critics, manifestos and a legal barrister to defend my work. Google now has a definition for my made up term. Here's what an accidental human/AI creative partnership looks like." Ralph Rumpelton https://zootsims1.wordpress.com/

16h ago

---

**[The problem of 'brand' facing the platform providers in the age of AI](https://www.reddit.com/r/artificial/comments/1tmshey/the_problem_of_brand_facing_the_platform/)**

It is easy to forecast that the majority of use a particular platform provider (Gmail, etc) will face in the next few years will be from non-UI-using AI agents. AI agents will open up (say) Gmail using OAuth, fiddle around reading/writing emails, changing settings, etc etc... all without using the traditional UI. So Gmail itself will become more of a process of AI, rather than a standalone application in its own right. This, of course, will destroy the brand which has required years/dollars$ to create and maintain. I can see these platform providers fighting back and either limiting the non-UI access, or banning it outright. So I see this all coming to a nasty fight in the next few years. Any thoughts?

4h ago

---

**[Multi-agent loop failures might be org-design failures, not prompt failures](https://www.reddit.com/r/artificial/comments/1tme23u/multiagent_loop_failures_might_be_orgdesign/)**

Repo: https://github.com/jeongmk522-netizen/agentlas\_org\_chart Almost every multi-agent setup I have shipped or tested eventually hits the same wall. Agents bouncing between each other, reviewers asking for one more polish pass forever, research workers spawning indefinite subtopics, tool calls spiraling until the recursion limit kicks in. The framework docs usually call these "loops" and offer a max-iteration knob. I started suspecting the knob is treating a symptom, and the real issue is closer to how the agents are organized to begin with. The pattern that kept reappearing: when agents are designed as peers (researcher talks to analyst, analyst talks to writer, writer hands back to reviewer), nobody clearly owns the outcome. Every agent can keep asking another agent for more work. The graph has stop conditions on paper, but no single agent has the authority to declare "this is done, stop the run." That authority is implicit at best and gets diluted across the peer network. The hypothesis I am testing is that loop failures are organization-design failures more than prompt failures. The fix is to treat the agent network as an org chart with explicit reporting lines, not a chat room of peers. One accountable mission owner. One owner per workstream. Finite delegation depth. A typed return contract per worker (status, evidence, output, blockers, next action). Manager-only authority to reopen or terminate. Memory lives at the authority layers, specialists get scoped context only. The layers I have been working with are roughly chair, strategy office, division manager, team lead, and specialist worker, with QA and policy as separate staff offices that can reject and escalate but cannot themselves spawn unbounded new work. The reviewer-recursion failure mode in particular gets killed when verifiers are structurally allowed one reject pass, then must escalate. Frameworks already have most of the primitives. CrewAI has a hierarchical process where a manager validates worker output. LangGraph has supervisors, subagents, and an explicit recursion limit. OpenAI Agents SDK has manager-style orchestration distinct from peer handoffs. AutoGen has GroupChatManager. Anthropic's published research system is orchestrator-worker. What I think is underused is treating the manager not as a moderator for an open group chat but as a formal reporting line with authority to terminate. Two things I am unsure about. First, hierarchy can become its own bottleneck. If every decision routes upward, the chair agent becomes a single point of latency and a single point of failure. Second, escalation-as-feature only works if the top of the org chart has real stop authority. If the chair just calls another LLM that calls more LLMs, the loop just moved one floor up.

14h ago

---

**[What AI image generator do you use?](https://www.reddit.com/r/artificial/comments/1tmkupv/what_ai_image_generator_do_you_use/)**

I'd like to put together a big list of all of the image generators out there with a pros/cons comparison. I don't care if it's paid or free, what do you use and why do you like it. Also if there's one you don't like, why aren't you a fan?

9h ago

---

**[We built a managed memory API for AI agents (open-source SDK + AGM-style belief revision for handling contradictions)](https://www.reddit.com/r/artificial/comments/1tmsehf/we_built_a_managed_memory_api_for_ai_agents/)**

Hey all! We just launched a managed memory API for conversational AI, letting developers add long-term memory to their agents with a single HTTP call. It's built on our in-house xmem SDK, which automatically extracts facts, episodes, and artifacts from multi-turn conversations and handles contradictions and updates through an AGM-style belief revision mechanism. When a user changes a preference or corrects an earlier statement, old memories get automatically flagged as "superseded" instead of piling up as noise. At query time, you can also walk the supersede chain to trace the full version history of any memory. Under the hood, PostgreSQL + pgvector (with HNSW indexing) delivers millisecond-level semantic retrieval, Redis handles multi-pod session caching, and the system natively supports multi-tenant isolation with data separation at the user and org level. For developers, this means you no longer have to stand up your own vector store, design dedup logic, or babysit session state. Hand off the memory layer to us and focus on what your agent actually does. Feel free to try it out, it's free to start. Please let us know your thoughts on how we can improve or features to add! https://github.com/XTraceAI/memory-sdk-ts https://docs.mem.xtrace.ai/introduction

4h ago

---

**[Vision-capable LLMs vs. OCR for long-document (including charts, images, tables, etc.) QA](https://www.reddit.com/r/artificial/comments/1tlzy43/visioncapable_llms_vs_ocr_for_longdocument/)**

I benchmarked vision-capable LLMs (the "just attach the PDF and let the model read it" pattern) against OCR-based pipelines on 30 long, image-heavy PDFs from MMLongBench-Doc (https://github.com/mayubo2333/MMLongBench-Doc). There were 171 questions in total, using Claude Sonnet 4.5 as the LLM. Post-retry results: Approach Accuracy $/query LlamaCloud premium + full-context 59.6% $0.1885 Azure premium + full-context 58.5% $0.2051 Azure basic + full-context 54.4% $0.1062 Agentic RAG 53.2% $0.0827 Native PDF (vision LLM) 52.0% $0.2552 LlamaCloud basic + full-context 50.9% $0.1049 Native PDF came 5th of 6 on accuracy and was the most expensive arm at $0.2552 per query. Two findings: Vision underperformed on chart-heavy and table-heavy pages, the territory that the "vision LLMs make OCR obsolete" claim most often points to. Premium OCR with layout extraction held up better there. The native-PDF arm had a 7% intrinsic failure rate (related to PDF file size) that survived retries. There were 27 first-pass failures, with 5 attempts of exponential backoff per failed query. Fifteen recovered, and 12 stayed permanently broken. These were concentrated in two specific PDFs that fail for predictable transport-layer reasons (the blog identifies them). OCR-based arms had a 0% intrinsic failure rate after retries. Caveats: 30 docs is a small sample. I ran McNemar's pairwise test to determine which gaps are real and which are within noise. Only 3 of 15 head-to-head gaps are statistically distinguishable at α = 0.05, so the order in the table is partly noise. The vision-versus-OCR finding survives the test. Full writeup: https://www.surfsense.com/blog/agentic-rag-vs-long-context-llms-benchmark

1d ago

---

**[What Will be the next industries to be completely disrupted by AI?](https://www.reddit.com/r/artificial/comments/1tm6mpt/what_will_be_the_next_industries_to_be_completely/)**

Curious if there are any industries that are not typically considered in the context of AI, which are likely to get disrupted by AI soon, or at least heavily enhanced? Any ideas?

20h ago

---

---

## Google News: "ai"

**[Inside the British Lab Hunting for Dangers Lurking in A.I.](https://www.nytimes.com/2026/05/24/technology/uk-ai-safety-institute.html)**

The New York Times • 19h ago

---

**[Pope Leo Is About to Make an A.I. Mic Drop. Here’s Why It Matters.](https://www.nytimes.com/2026/05/25/world/europe/pope-leo-encyclical-ai.html)**

The New York Times • 44m ago

---

**[Pope Leo will take on AI alongside an Anthropic co-founder](https://www.nbcnews.com/tech/tech-news/pope-leo-address-human-dignity-age-ai-rcna345744)**

The pope will join leading Catholic theologians and an Anthropic co-founder on Monday to release a landmark encyclical on “safeguarding the human person in the time of artificial intelligence.”

NBC News • 16h ago

---

**[Silicon Valley Takes Its AI Pitch to Pope Leo](https://www.businessinsider.com/pope-leo-ai-opinion-silicon-valley-meta-amazon-google-openai-2026-5)**

As Leo XIV prepares his first encyclical, tech firms and Western diplomats have worked to make their case for AI inside the Vatican.

Business Insider • 1h ago

---

**[AI Rally Drives Best Run in Global Momentum Stocks on Record](https://www.bloomberg.com/news/articles/2026-05-25/ai-rally-drives-best-run-in-global-momentum-stocks-on-record)**

Bloomberg.com • 37m ago

---

**[AI is learning to fly airplanes — and aviation is starting to embrace it](https://www.cnn.com/2026/05/24/us/ai-flying-airplanes)**

The small Cessna Caravan accelerates down the runway and climbs into the air, all while the pilot beside me keeps his hands off the controls.

CNN • 10h ago

---

**[Bay Area mom out thousands after scammers use AI to mimic daughter's voice in fake kidnapping; part of growing trend](https://abc7news.com/post/bay-area-mom-thousands-scammers-use-ai-mimic-daughters-voice-fake-kidnapping-part-growing-trend/19154381/)**

Thousands of dollars were stolen from a Bay Area woman after scammers used artificial intelligence to mimic her daughter's voice in what authorities describe as a growing type of fraud.

ABC7 San Francisco • 7h ago

---

**[Bernie Sanders warns of 'the most transformative economic revolution in the history of this country'](https://www.foxbusiness.com/politics/bernie-sanders-warns-the-most-transformative-economic-revolution-history-country)**

Sen. Bernie Sanders warned that AI and robotics controlled by billionaires could replace American workers and harm children's social development.

Fox Business • 4h ago

---

**[How AI is forcing McKinsey and its peers to rethink pricing](https://www.ft.com/content/8318a754-7b63-4f1f-8978-7691e7ed3511?syn-25a6b1a6=1)**

Clients are questioning the value of advice while getting more used to fees based on successful task completion

Financial Times • 1d ago

---

**[What to know about the AI models that are jolting Washington](https://www.politico.com/news/2026/05/24/anthropic-openai-mythos-what-to-know-00934668)**

Politico • 17h ago

---

---

## HackerNews: "ai"

**[Steve Wozniak cheered after telling students they have AI – actual intelligence](https://news.ycombinator.com/item?id=48233563)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

⬆️ 645 • 💬 544 • 2d ago • [Business Insider](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 341 • 💬 360 • 12h ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[AI has a multiplying effect on existing technical skills](https://news.ycombinator.com/item?id=48235526)**

Friendly articles and tutorials for front-end web developers. ❤️

⬆️ 337 • 💬 311 • 2d ago • [joshwcomeau.com](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

---

**[Italy moves to Airbus A330 tankers](https://news.ycombinator.com/item?id=48248775)**

Rome shifts course: six Airbus A330 MRTT tanker aircraft, worth around €1.39 billion in total, to bolster the European pillar in NATO. #EuropeNews

⬆️ 277 • 💬 111 • 1d ago • [euronews](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

---

**[Is AI Profitable Yet?](https://news.ycombinator.com/item?id=48243863)**

⬆️ 259 • 💬 201 • 2d ago • [isaiprofitable.com](https://isaiprofitable.com/)

---

**[Microsoft reports AI is more expensive than paying human employees](https://news.ycombinator.com/item?id=48244434)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

⬆️ 228 • 💬 70 • 2d ago • [Fortune](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

---

**[DeepSeek to Make Permanent 75% Discount on Flagship AI Model](https://news.ycombinator.com/item?id=48257410)**

⬆️ 206 • 💬 2 • 14h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

---

**[The Companies Cutting Headcount for AI Will Lose to the Ones Who Didn't](https://news.ycombinator.com/item?id=48234547)**

Organisations using AI to cut headcount are making a short-term trade with long-term consequences. The ones holding their teams together and investing in how those teams operate with AI are building something more durable.

⬆️ 202 • 💬 203 • 2d ago • [libertas.software](https://libertas.software/en/knowledge-hub/19/the-companies-cutting-headcount-for-ai-will-lose-to-the-ones-who-didnt)

---

**[Don't just paste the AI at me](https://news.ycombinator.com/item?id=48242648)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 180 • 💬 113 • 2d ago • [dontquotetheai.com](https://dontquotetheai.com/)

---

**[Models.dev: open-source database of AI model specs, pricing, and capabilities](https://news.ycombinator.com/item?id=48241172)**

An open-source database of AI models. Contribute to anomalyco/models.dev development by creating an account on GitHub.

⬆️ 156 • 💬 27 • 2d ago • [GitHub](https://github.com/anomalyco/models.dev)

---

---

## YouTube Videos: "ai"

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 37K • 👍 2K • 💬 188 • ⏱️ 13:31 • 2d ago

---

**[The singularity is near: Google unveils next phase of AI](https://www.youtube.com/watch?v=zvJ5KfNjOCk)**

ABC News' Nathan Rousseau Smith travels to Google I/O where the search giant unveiled AI agent Gemini Spark, new smart ...

📺 ABC News

👁️ 163K • 👍 2K • 💬 595 • ⏱️ 5:06 • 2d ago

---

**[Nobody Actually Wants AI Anymore](https://www.youtube.com/watch?v=FQpZdCKgc6w)**

People often compare AI to the internet, but there's one big problem with that comparison: people naturally adopted the internet as ...

📺 Vanessa Wingårdh

👁️ 143K • 👍 10K • 💬 3K • ⏱️ 12:37 • 16h ago

---

**[This New AI Agent Turns You Into a One-Person Company](https://www.youtube.com/watch?v=HJN3husu1oM)**

Try Accio Work : https://www.accio.com/work?src=p_ytkol_vaibhav @Accio_official Join our WhatsApp Community Get the ...

📺 Vaibhav Sisinty

👁️ 42K • 👍 2K • 💬 72 • ⏱️ 16:03 • 13h ago

---

**[Google’s AI endgame is here… everything you missed at I/O 2026](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

Try using Emergent's specialized agents in parallel to build any full-stack application ...

📺 Fireship

👁️ 732K • 👍 22K • 💬 1K • ⏱️ 5:44 • 2d ago

---

**[Claude Obsidian is Insane (FREE!) 🤯](https://www.youtube.com/watch?v=JqIrJgwmTm8)**

Get the Claude + Obsidian OS https://www.skool.com/ai-profit-lab-7462/about Want to make money and save time with AI?

📺 Julian Goldie SEO

👁️ 4K • 👍 78 • 💬 6 • ⏱️ 18:47 • 21h ago

---

**[Narrative that connects AI to job loss ‘too lazy’: Nvidia CEO Jensen Huang](https://www.youtube.com/watch?v=tDQcQv6M5e4)**

The narrative that connects AI to job loss is "too lazy", Nvidia founder and CEO Jensen Huang told CNA on Monday (May 25).

📺 CNA

👁️ 631 • 👍 5 • 💬 4 • ⏱️ 1:07 • 36m ago

---

**[Don&#39;t Buy AI Bath Bombs](https://www.youtube.com/watch?v=uocwJAi2y_U)**

Get your $10 sign-up bonus at http://privacy.com/pleasantgreen. You can use it on your first purchase! Privacy has a free plan with ...

📺 Pleasant Green

👁️ 609K • 👍 25K • 💬 2K • ⏱️ 10:02 • 1d ago

---

**[College Kids Don’t Want Your AI](https://www.youtube.com/watch?v=5YISwyxmty4)**

The unique threat artificial intelligence poses to students' education and their hopes of someday landing a job has made ...

📺 Bloomberg Podcasts

👁️ 3K • 👍 46 • 💬 40 • ⏱️ 6:01 • 13h ago

---

**[AI co-scientist, AI for DNA, AI NPCs, open-source robots, new Qwen, new video editors: AI NEWS](https://www.youtube.com/watch?v=pC6KHflGye0)**

HUGE AI NEWS: Qwen 3.7, Bytedance Lance, Stable Audio 3, L2P, MegaASR, & more #ai #ainews #aitools #aivideo #agi ...

📺 AI Search

👁️ 55K • 👍 2K • 💬 210 • ⏱️ 47:07 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,474 • ❤️ 771 • 1d ago

---

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, 1.8B parameter multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 4,534 • ❤️ 640 • 2d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 6,032 • ❤️ 312 • 4d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale (30B parameters, MoE) multilingual translation model supporting 33 languages. It excels in general, business, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 1,243 • ❤️ 314 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 43,119 • ❤️ 648 • 6d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 84,346 • ❤️ 272 • 3d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,331,058 • ❤️ 1,327 • 3d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 660,321 • ❤️ 459 • 4d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for on-device image and video understanding, offering strong foundation and multimodal capabilities with mixed visual token compression for flexible speed/accuracy trade-offs.

`image-text-to-text` `1.3B`

⬇️ 269,589 • ❤️ 920 • 5d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 5,627 • ❤️ 190 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 81 • 💬 3 • ⭐ 79,292 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 64,742 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,505 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 108 • 💬 3 • ⭐ 1,958 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,700 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 127 • 💬 3 • ⭐ 499 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,801 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 72 • 💬 4 • ⭐ 835 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,625 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,526 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.8k • 🔱 497 • 2d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 7d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 179 • 1m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 389 • 3d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 346 • 7d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.1k • 🔱 468 • 3d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.9k • 🔱 129 • 4d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 215 • 17d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.7k • 🔱 118 • 11h ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 187 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
