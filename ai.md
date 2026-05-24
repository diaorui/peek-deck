---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-24T21:28:52.738730+00:00'
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

**Last Updated:** May 24, 2026 at 21:28 UTC  
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

**[What AI image generator do you use?](https://www.reddit.com/r/artificial/comments/1tmkupv/what_ai_image_generator_do_you_use/)**

I'd like to put together a big list of all of the image generators out there with a pros/cons comparison. I don't care if it's paid or free, what do you use and why do you like it. Also if there's one you don't like, why aren't you a fan?

2h ago

---

**[Testing a Cold War-Era AI on Satellite Image Datasets](https://www.reddit.com/r/artificial/comments/1tmnb54/testing_a_cold_warera_ai_on_satellite_image/)**

I came across a cool model developed during the Cold War. I wanted to see how it would perform at image recognition, so I downloaded the UC Merced Land Use Dataset and wrote a script to add Gaussian noise to the photos and measure performance over a series of trials using Monte Carlo simulations. It is very efficient and appears well suited for FPGA implementation. It only uses about 50 MB of RAM. The satellite photos are converted to grayscale, downscaled to roughly 32×32, and converted into a fingerprint that is roughly 128 bytes in size. Therefore, the database of 800 TIFs is about 100 KB total. I’ll include the test and debug images so you can see how the process works. The model basically selects the stored pattern that best matches the noisy input based on what it has learned from the data.

59m ago

---

**["I'm retired. I showed my MS Paint paintings to AI for feedback. It accidentally invented an entire fake art movement. Google believes it's real."](https://www.reddit.com/r/artificial/comments/1tmb7c6/im_retired_i_showed_my_ms_paint_paintings_to_ai/)**

"I'm retired and started showing my MS Paint paintings to AI for criticism. The AI invented feuding critics, manifestos and a legal barrister to defend my work. Google now has a definition for my made up term. Here's what an accidental human/AI creative partnership looks like." Ralph Rumpelton https://zootsims1.wordpress.com/

8h ago

---

**[Multi-agent loop failures might be org-design failures, not prompt failures](https://www.reddit.com/r/artificial/comments/1tme23u/multiagent_loop_failures_might_be_orgdesign/)**

Repo: https://github.com/jeongmk522-netizen/agentlas\_org\_chart Almost every multi-agent setup I have shipped or tested eventually hits the same wall. Agents bouncing between each other, reviewers asking for one more polish pass forever, research workers spawning indefinite subtopics, tool calls spiraling until the recursion limit kicks in. The framework docs usually call these "loops" and offer a max-iteration knob. I started suspecting the knob is treating a symptom, and the real issue is closer to how the agents are organized to begin with. The pattern that kept reappearing: when agents are designed as peers (researcher talks to analyst, analyst talks to writer, writer hands back to reviewer), nobody clearly owns the outcome. Every agent can keep asking another agent for more work. The graph has stop conditions on paper, but no single agent has the authority to declare "this is done, stop the run." That authority is implicit at best and gets diluted across the peer network. The hypothesis I am testing is that loop failures are organization-design failures more than prompt failures. The fix is to treat the agent network as an org chart with explicit reporting lines, not a chat room of peers. One accountable mission owner. One owner per workstream. Finite delegation depth. A typed return contract per worker (status, evidence, output, blockers, next action). Manager-only authority to reopen or terminate. Memory lives at the authority layers, specialists get scoped context only. The layers I have been working with are roughly chair, strategy office, division manager, team lead, and specialist worker, with QA and policy as separate staff offices that can reject and escalate but cannot themselves spawn unbounded new work. The reviewer-recursion failure mode in particular gets killed when verifiers are structurally allowed one reject pass, then must escalate. Frameworks already have most of the primitives. CrewAI has a hierarchical process where a manager validates worker output. LangGraph has supervisors, subagents, and an explicit recursion limit. OpenAI Agents SDK has manager-style orchestration distinct from peer handoffs. AutoGen has GroupChatManager. Anthropic's published research system is orchestrator-worker. What I think is underused is treating the manager not as a moderator for an open group chat but as a formal reporting line with authority to terminate. Two things I am unsure about. First, hierarchy can become its own bottleneck. If every decision routes upward, the chair agent becomes a single point of latency and a single point of failure. Second, escalation-as-feature only works if the top of the org chart has real stop authority. If the chair just calls another LLM that calls more LLMs, the loop just moved one floor up.

6h ago

---

**[I simply do not understand how massively expensive AI and robotics are expected to be more cost effective than humans.](https://www.reddit.com/r/artificial/comments/1tmffqn/i_simply_do_not_understand_how_massively/)**

Can someone help me understand this? I mean, how on earth are these companies who are planning to replace us all with beep boops expecting these unimaginably high expense technologies to be better for their bottom line than just paying us low wage unwashed masses? I mean, some dude (respectfully, I use that term genderlessly) here just posted about min wage in their area being $7.25! You are not getting a robot or AI that costs less annualized. Even adding in annual benefits - that is a steal compared to data centers and complex robots who will be absurdly expensive to fix when they break. I’m a white collar worker with deep knowledge of worker costs, even at the top it’s cheaper than what all of this new buggy crap is going to cost. I’m so confused. What am I missing? Why are the evil overlords not interested in our already too cheap labor?

5h ago

---

**[Vision-capable LLMs vs. OCR for long-document (including charts, images, tables, etc.) QA](https://www.reddit.com/r/artificial/comments/1tlzy43/visioncapable_llms_vs_ocr_for_longdocument/)**

I benchmarked vision-capable LLMs (the "just attach the PDF and let the model read it" pattern) against OCR-based pipelines on 30 long, image-heavy PDFs from MMLongBench-Doc (https://github.com/mayubo2333/MMLongBench-Doc). There were 171 questions in total, using Claude Sonnet 4.5 as the LLM. Post-retry results: Approach Accuracy $/query LlamaCloud premium + full-context 59.6% $0.1885 Azure premium + full-context 58.5% $0.2051 Azure basic + full-context 54.4% $0.1062 Agentic RAG 53.2% $0.0827 Native PDF (vision LLM) 52.0% $0.2552 LlamaCloud basic + full-context 50.9% $0.1049 Native PDF came 5th of 6 on accuracy and was the most expensive arm at $0.2552 per query. Two findings: Vision underperformed on chart-heavy and table-heavy pages, the territory that the "vision LLMs make OCR obsolete" claim most often points to. Premium OCR with layout extraction held up better there. The native-PDF arm had a 7% intrinsic failure rate (related to PDF file size) that survived retries. There were 27 first-pass failures, with 5 attempts of exponential backoff per failed query. Fifteen recovered, and 12 stayed permanently broken. These were concentrated in two specific PDFs that fail for predictable transport-layer reasons (the blog identifies them). OCR-based arms had a 0% intrinsic failure rate after retries. Caveats: 30 docs is a small sample. I ran McNemar's pairwise test to determine which gaps are real and which are within noise. Only 3 of 15 head-to-head gaps are statistically distinguishable at α = 0.05, so the order in the table is partly noise. The vision-versus-OCR finding survives the test. Full writeup: https://www.surfsense.com/blog/agentic-rag-vs-long-context-llms-benchmark

18h ago

---

**[The biggest AI mistake: buying the tool before fixing the process](https://www.reddit.com/r/artificial/comments/1tmos7e/the_biggest_ai_mistake_buying_the_tool_before/)**

Most businesses use AI backward. They buy the tool first and then try to find something for it to do. That usually does not work well. If the workflow is messy, AI just makes the mess move faster. The real value is in the handoff points: where data enters, where context is missing, where a next step is decided, where a draft gets created, and where a human still needs to review it. That is the basic idea behind my 5-Layer AI Workflow Audit. I just put together a full playbook on it here: Start Here: The 5-Layer AI Workflow Audit

2m ago

---

**[Memory](https://www.reddit.com/r/artificial/comments/1tmopo4/memory/)**

Your explanation is largely correct. The reason “memory” has become the dominant systems problem for LLMs is that modern transformers are increasingly memory-bandwidth bound, not compute-bound. The key shift is this: Training large models was mostly about FLOPs. Serving large models at scale is increasingly about moving KV cache data around fast enough. A single token generation step only performs a relatively modest amount of math compared to the amount of KV data that must be fetched from memory every step. Why this happens During inference, every new token attends to all prior tokens. So for token t, the model needs access to all prior K/V tensors: \text{KV Cache Size} \propto 2 \times L \times S \times H \times d Where: L = layers S = sequence length H = attention heads d = head dimension The killer is the S term. As context grows: 8K → manageable 128K → huge 1M → infrastructure problem A 70B model with long context can require hundreds of GBs of KV cache across concurrent users. Why bandwidth matters more than raw compute Modern GPUs like the NVIDIA H100 or NVIDIA Blackwell can perform enormous amounts of compute. But every generated token requires: Loading KV cache from memory Running attention Writing updated KV back That means inference speed often depends more on: HBM bandwidth memory locality cache management than tensor core throughput. This is why: HBM3E NVLink unified memory memory compression have become strategic bottlenecks. Why the KV cache can exceed model weights Model weights are static. KV cache is dynamic and scales with: users context length output length batch size Example intuition: 70B model weights might occupy ~140 GB FP16 But serving thousands of users with long contexts can require multiple TBs of KV cache So operators increasingly optimize: cache reuse eviction paging quantization instead of just model size. Why vLLM and PagedAttention mattered so much Before systems like vLLM, memory fragmentation was catastrophic. PagedAttention essentially borrowed ideas from operating systems: divide KV into pages allocate dynamically avoid contiguous memory assumptions That dramatically improved: utilization batching throughput This was one of the biggest inference infrastructure breakthroughs of the last few years because it improved economics without changing the model itself. The deeper issue: transformers scale poorly with context Standard attention fundamentally has a retrieval problem: Each token potentially references every prior token. Even though compute optimizations exist, the architecture still requires huge memory movement. That’s why researchers are exploring: Grouped Query Attention (GQA) Multi-Query Attention (MQA) sliding window attention recurrent memory state-space models hybrid retrieval systems The industry increasingly believes: infinite-context transformers using naive KV scaling are economically unsustainable. Why inference economics are now the focus Training frontier models is expensive. But operating them continuously at global scale is potentially even larger economically. For many providers: inference cost dominates memory dominates inference cost That’s why companies across the stack are racing on memory: NVIDIA → HBM + NVLink + Grace AMD → MI300 unified memory Cerebras → wafer-scale SRAM Groq → deterministic low-latency SRAM-heavy architecture Marvell Technology → custom memory fabrics The bottleneck has shifted from: “Can we train bigger models?” to: “Can we serve them cheaply and fast enough?”

4m ago

---

**[Elon, stop trying to make Grok happen. New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?](https://www.reddit.com/r/artificial/comments/1tlp9gz/elon_stop_trying_to_make_grok_happen_new_data/)**

New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/936219/elon-stop-trying-to-make-grok-happen) • 1d ago

---

**[How to train an Image Generation AI model from scratch as an “experiment”](https://www.reddit.com/r/artificial/comments/1tmm586/how_to_train_an_image_generation_ai_model_from/)**

People use image generation AI every day now, but I feel like almost nobody actually understands what training one looks like underneath. Every time I search about it, I either find insanely complex research papers or fake “train your own AI in one click” videos that skip everything important. It genuinely makes me curious what the real workflow looks like behind training even a small image generation model from scratch just as an experiment. Like how hard is it actually? What part is the real bottleneck? The compute, the data, the architecture, or just understanding all the moving parts together? AI image generation already feels normal now, but the process behind creating those systems still feels weirdly hidden from most people.

1h ago

---

---

## Google News: "ai"

**[Inside the British Lab Hunting for Dangers Lurking in A.I.](https://www.nytimes.com/2026/05/24/technology/uk-ai-safety-institute.html)**

The New York Times • 12h ago

---

**[Google CEO Sundar Pichai says graduates booing AI will shape its future — and live with its consequences](https://www.businessinsider.com/sundar-pichai-google-graduation-speech-stanford-ai-backlash-eric-schmidt)**

As commencement speakers face restless crowds of new graduates, Google CEO Sundar Pichai says he's ready for his turn at Stanford next month.

Business Insider • 5h ago

---

**[I Asked ChatGPT How to Talk to Women. Was It Trying to Turn Me Into a Douchebag?](https://www.menshealth.com/health/a71395890/i-asked-chatgpt-to-help-with-dating-anxiety/)**

Two AI-generated answers made me pause.

Men's Health • 58m ago

---

**[Bay Area mom out thousands after scammers use AI to mimic daughter's voice in fake kidnapping; part of growing trend](https://abc7news.com/post/bay-area-mom-thousands-scammers-use-ai-mimic-daughters-voice-fake-kidnapping-part-growing-trend/19154381/)**

Thousands of dollars were stolen from a Bay Area woman after scammers used artificial intelligence to mimic her daughter's voice in what authorities describe as a growing type of fraud.

ABC7 San Francisco • 36m ago

---

**[Pope Leo will take on AI alongside an Anthropic co-founder](https://www.nbcnews.com/tech/tech-news/pope-leo-address-human-dignity-age-ai-rcna345744)**

The pope will join leading Catholic theologians and an Anthropic co-founder on Monday to release a landmark encyclical on “safeguarding the human person in the time of artificial intelligence.”

NBC News • 9h ago

---

**[SpaceX's IPO charts reveal a company spending like an AI giant: Chart of the Day](https://finance.yahoo.com/markets/article/spacexs-ipo-charts-reveal-a-company-spending-like-an-ai-giant-chart-of-the-day-120213160.html)**

SpaceX is going public with a rocket-company reputation, but its IPO filing points investors mainly to AI.

Yahoo Finance • 9h ago

---

**[What to know about the AI models that are jolting Washington](https://www.politico.com/news/2026/05/24/anthropic-openai-mythos-what-to-know-00934668)**

Politico • 10h ago

---

**[AI is learning to fly airplanes — and aviation is starting to embrace it](https://www.cnn.com/2026/05/24/us/ai-flying-airplanes)**

The small Cessna Caravan accelerates down the runway and climbs into the air, all while the pilot beside me keeps his hands off the controls.

CNN • 3h ago

---

**[‘AI washing’: firms are scrambling to rebrand themselves as tech-focused](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)**

PR executives say UK companies are forcing them to present ordinary automation as artificial intelligence

The Guardian • 3h ago

---

**[I’m a Professional Writer Who Uses a Very Controversial Tool. It’s Not As Scary As I Thought.](https://slate.com/technology/2026/05/ai-chatgpt-claude-professional-writing-tool.html)**

I was skeptical about ChatGPT and Claude at first. Then I started to come around—and I’m glad I did.

Slate • 11h ago

---

---

## HackerNews: "ai"

**[Steve Wozniak cheered after telling students they have AI – actual intelligence](https://news.ycombinator.com/item?id=48233563)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

⬆️ 645 • 💬 544 • 2d ago • [Business Insider](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

---

**[AI has a multiplying effect on existing technical skills](https://news.ycombinator.com/item?id=48235526)**

Friendly articles and tutorials for front-end web developers. ❤️

⬆️ 337 • 💬 311 • 2d ago • [joshwcomeau.com](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

---

**[Italy moves to Airbus A330 tankers](https://news.ycombinator.com/item?id=48248775)**

Rome shifts course: six Airbus A330 MRTT tanker aircraft, worth around €1.39 billion in total, to bolster the European pillar in NATO. #EuropeNews

⬆️ 271 • 💬 108 • 1d ago • [euronews](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

---

**[Is AI Profitable Yet?](https://news.ycombinator.com/item?id=48243863)**

⬆️ 258 • 💬 197 • 1d ago • [isaiprofitable.com](https://isaiprofitable.com/)

---

**[Samsung chip workers will get an average $340k bonus as AI profits soar](https://news.ycombinator.com/item?id=48230892)**

The South Korean chipmaker struck a last-minute deal with its union to avert an 18-day strike, unlocking a $26.6 billion payout pool

⬆️ 251 • 💬 196 • 2d ago • [Quartz](https://qz.com/samsung-chip-workers-bonus-ai-profits-052126)

---

**[Microsoft reports AI is more expensive than paying human employees](https://news.ycombinator.com/item?id=48244434)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

⬆️ 228 • 💬 66 • 1d ago • [Fortune](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 219 • 💬 244 • 4h ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[The Companies Cutting Headcount for AI Will Lose to the Ones Who Didn't](https://news.ycombinator.com/item?id=48234547)**

Organisations using AI to cut headcount are making a short-term trade with long-term consequences. The ones holding their teams together and investing in how those teams operate with AI are building something more durable.

⬆️ 202 • 💬 201 • 2d ago • [libertas.software](https://libertas.software/en/knowledge-hub/19/the-companies-cutting-headcount-for-ai-will-lose-to-the-ones-who-didnt)

---

**[Don't just paste the AI at me](https://news.ycombinator.com/item?id=48242648)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 180 • 💬 113 • 1d ago • [dontquotetheai.com](https://dontquotetheai.com/)

---

**[DeepSeek to Make Permanent 75% Discount on Flagship AI Model](https://news.ycombinator.com/item?id=48257410)**

⬆️ 168 • 💬 2 • 7h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

---

---

## YouTube Videos: "ai"

**[Nobody Actually Wants AI Anymore](https://www.youtube.com/watch?v=FQpZdCKgc6w)**

People often compare AI to the internet, but there's one big problem with that comparison: people naturally adopted the internet as ...

📺 Vanessa Wingårdh

👁️ 108K • 👍 8K • 💬 3K • ⏱️ 12:37 • 9h ago

---

**[Updated Essential AI Skills For 2026](https://www.youtube.com/watch?v=tu4rU4YD1Jk)**

Start building AI apps with Bolt ...

📺 Tina Huang

👁️ 16K • 👍 1K • 💬 76 • ⏱️ 13:45 • 8h ago

---

**[The singularity is near: Google unveils next phase of AI](https://www.youtube.com/watch?v=zvJ5KfNjOCk)**

ABC News' Nathan Rousseau Smith travels to Google I/O where the search giant unveiled AI agent Gemini Spark, new smart ...

📺 ABC News

👁️ 121K • 👍 2K • 💬 453 • ⏱️ 5:06 • 1d ago

---

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 35K • 👍 2K • 💬 182 • ⏱️ 13:31 • 1d ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 6K • 👍 159 • 💬 36 • ⏱️ 18:21 • 19h ago

---

**[How to Make AI Music Videos with Perfect Lip Sync](https://www.youtube.com/watch?v=7ajVhp8qM3U)**

Create Your Own Music Videos with Perfect Lip Sync on Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=isa15 In this video, ...

📺 Isa does AI

👁️ 9K • 💬 3 • ⏱️ 8:51 • 9h ago

---

**[Joe Rogan accidentally exposed AI in four words](https://www.youtube.com/watch?v=waFl4uBfXRA)**

Token mania. I've been a user of Proton for almost a decade and I'm grateful to them for agreeing to sponsor this video. Proton ...

📺 Mo Bitar

👁️ 202K • 👍 11K • 💬 2K • ⏱️ 11:39 • 2d ago

---

**[Google’s AI endgame is here… everything you missed at I/O 2026](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

Try using Emergent's specialized agents in parallel to build any full-stack application ...

📺 Fireship

👁️ 700K • 👍 21K • 💬 1K • ⏱️ 5:44 • 2d ago

---

**[I Found ALL Paid AI Video Tools in One Place — FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=hFnoAAd-pkQ)**

Try Higgsfield here and create cinematic AI videos with top models in one place → https://higgsfield.ai/s/general-malvaai-jupaTB ...

📺 Malva AI

👁️ 7K • 👍 406 • 💬 62 • ⏱️ 8:13 • 10h ago

---

**[AI co-scientist, AI for DNA, AI NPCs, open-source robots, new Qwen, new video editors: AI NEWS](https://www.youtube.com/watch?v=pC6KHflGye0)**

HUGE AI NEWS: Qwen 3.7, Bytedance Lance, Stable Audio 3, L2P, MegaASR, & more #ai #ainews #aitools #aivideo #agi ...

📺 AI Search

👁️ 47K • 👍 2K • 💬 199 • ⏱️ 47:07 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,474 • ❤️ 756 • 1d ago

---

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, 1.8B parameter multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 4,534 • ❤️ 573 • 2d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 6,032 • ❤️ 305 • 4d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale (30B parameters, MoE) multilingual translation model supporting 33 languages. It excels in general, business, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 1,243 • ❤️ 306 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 43,119 • ❤️ 643 • 6d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 84,346 • ❤️ 269 • 3d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,331,058 • ❤️ 1,321 • 2d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for on-device image and video understanding, offering strong foundation and multimodal capabilities with mixed visual token compression for flexible speed/accuracy trade-offs.

`image-text-to-text` `1.3B`

⬇️ 269,589 • ❤️ 918 • 5d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 660,321 • ❤️ 450 • 4d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 5,627 • ❤️ 189 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 81 • 💬 3 • ⭐ 79,201 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 108 • 💬 3 • ⭐ 1,935 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 163 • 💬 2 • ⭐ 64,742 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,449 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 72 • 💬 4 • ⭐ 818 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

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

▲ 127 • 💬 3 • ⭐ 448 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

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

▲ 120 • 💬 10 • ⭐ 10,503 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,700 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.8k • 🔱 492 • 2d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 7d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 179 • 9h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 387 • 2d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 346 • 7d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.1k • 🔱 465 • 3d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.8k • 🔱 122 • 4d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 213 • 17d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 186 • 3d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.7k • 🔱 117 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
