---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-26T15:59:50.273765+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 26, 2026 at 15:59 UTC  
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

**[CEO fired developers to make room for AI. Developers respond by creating open source AI CEO](https://www.reddit.com/r/artificial/comments/1vyegah/ceo_fired_developers_to_make_room_for_ai/)**

I hope this is okay to share since it is not self promotion and it is open source. Some of my friends were let go as part of an "AI Transformation". So they got together and created Open Executive as a tool to replace the CEO and other executives. Hopefully, turnabout is fair play and might even get some folks to think twice about using AI to replace people. It is free and available here: https://github.com/SenteLabsAI/OpenExecutive

17h ago

---

**[Bill Gates says there needs to be limits on AI](https://www.reddit.com/r/artificial/comments/1vyy8yg/bill_gates_says_there_needs_to_be_limits_on_ai/)**

Microsoft co-founder Bill Gates says there need to be significant limits placed on artificial intelligence or else the harm to humans will outweigh any potential good.

🔗 [CNN](https://www.cnn.com/2026/08/26/business/bill-gates-wants-limits-on-ai?utm_medium=social&utm_campaign=missions&utm_source=reddit) • 1h ago

---

**[Mark Zuckerberg had a bold plan to replace Meta staff with AI. Here’s how it imploded.](https://www.reddit.com/r/artificial/comments/1vyvxb5/mark_zuckerberg_had_a_bold_plan_to_replace_meta/)**

🔗 [reuters.com](https://www.reuters.com/investigations/mark-zuckerberg-had-bold-plan-replace-meta-staff-with-ai-heres-how-it-imploded-2026-08-26) • 3h ago

---

**[Robot dancing is getting pretty insane](https://www.reddit.com/r/artificial/comments/1vyzr8c/robot_dancing_is_getting_pretty_insane/)**

51m ago

---

**[The bottleneck for meeting transcription tools isn't accurate anymore, it's speaker attribution](https://www.reddit.com/r/artificial/comments/1vyrxy8/the_bottleneck_for_meeting_transcription_tools/)**

Been testing a few AI transcription setups for work over the past couple months and noticed something word level accuracy from most of these engines is already pretty solid now, upper 90s%. The thing that actually breaks the output is figuring out who said what when more than 2-3 people are talking, especially with any crosstalk or people talking over each other. Feels like an underrated problem compared to how much attention pure transcription accuracy gets. A transcript that's 99% accurate but has the wrong person attributed to a key statement is arguably more useless than one that's 90% accurate with correct speaker labels, at least for anything where "who committed to what" matters. Tried a handful of tools chasing this Otter, a couple others, and more recently Vomo ai which does speaker labeling automatically. Vomo’s noticeably better on 3+ person calls than what I was using before,though overlapping speech is still the one case where it takes a bit more attention to double-check, so more of an improvement than a full fix. Wondering if this is a known hard problem in the diarization research or if it's more of an engineering/product prioritization gap that just hasn't been addressed yet.

6h ago

---

**[The reason why I have 15 Codex Pro 20x subscriptions](https://www.reddit.com/r/artificial/comments/1vz0zk8/the_reason_why_i_have_15_codex_pro_20x/)**

The reason why I have 15 Codex Pro 20x subscriptions: Premium tokens are 311x cheaper for a LIMITED TIME ONLY* at the OpenAI Token Depot. I brought 15 shopping carts. The subsidy has dropped 25% since 1 month ago.

6m ago

---

**[AGI quietly defined 34 days before Microsoft and OpenAI kill AGI Clause?](https://www.reddit.com/r/artificial/comments/1vz0fek/agi_quietly_defined_34_days_before_microsoft_and/)**

Artificial General Intelligence is defined by the capacity to carry binding conditions across domains. A binding condition is the prerequisite that must hold for valid continuation. A system exhibits AGI when it can identify, verify, and enforce these conditions in arbitrary contexts without domain-specific training. Paper: https://doi.org/10.5281/zenodo.19211116 Official Microsoft Announcement: https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/ Reuters saying AGI clause was scrapped: https://www.breakingviews.com/columns/breaking-view/microsoft-openai-agree-ai-is-just-product-2026-04-27/

🔗 [doi.org](https://doi.org/10.5281/zenodo.19211116) • 26m ago

---

**[Found someone using an unapproved AI tool with client data. How common is this?](https://www.reddit.com/r/artificial/comments/1vyz1jg/found_someone_using_an_unapproved_ai_tool_with/)**

Something happened recently that made me think about how common this might actually be. I found out that someone on a project team had been copying parts of a client's internal documents into a personal ChatGPT account to save some time. There was no bad intention behind it. They simply didn't think about the security side of it. It made me wonder how other companies are dealing with this. Is this something you've actually come across, or is it still pretty rare in your organization? Do you have any way to know which AI tools employees are using, or do you usually find out after something happens? I'm trying to understand whether this is becoming a normal challenge for companies or if we're just seeing it more because AI adoption is moving so quickly. Would be really interested to hear how other IT and security teams are handling it.

1h ago

---

**[[Open-Source] I need your worst edge cases to stress-test GenOS, my new AI agent orchestrator.](https://www.reddit.com/r/artificial/comments/1vyxoes/opensource_i_need_your_worst_edge_cases_to/)**

Hey everyone, I’m currently working on GenOS, an open-source framework for multi-agent LLM orchestration. Under the hood, it uses isolated Rust execution environments and relies on Git worktrees for clean state management and secure sandboxing. The core engine is running smoothly, but before pushing it further, I need to expose it to the harsh reality of real-world use cases. We all know that AI agents (whether single or in swarms) look amazing in demos, but often trip over their own feet the second you take them out of "Hello World" territory. That’s where you come in: what are the real, testable problems you run into when building or using AI agents? I’m looking for concrete, reproducible scenarios to see how GenOS handles them (or if it fails miserably, which will help me iterate). What I'm specifically looking for: Infinite loops & derailments: Tasks where the agent starts hallucinating code execution and just won't stop. State & context management: Swarm scenarios where Agent A forgets to pass crucial info to Agent B, or completely overwrites its work. Isolation issues: Cases where an agent corrupts its workspace by modifying or deleting the wrong files. Complex multi-step tasks: Long workflows where the agent eventually loses track of its initial objective. Drop your use cases, your biggest frustrations with existing frameworks (like LangChain, AutoGen, CrewAI, etc.), or even specific prompts that consistently break your setups. I’ll take the most interesting cases, code them into GenOS to see if the Rust/Git architecture offers a cleaner solution, and I'll report back with the results! Thanks in advance for the feedback You can check it here PISSARAW/GenOS: Git-like branching, deterministic replay, and evidence-driven evaluation for reproducible AI agents.

2h ago

---

**[Why Irregular’s A.I. Tests for Meta, Anthropic and OpenAI Went Off the Rails. Irregular, an Israeli start-up, worked with OpenAI, Anthropic and Meta to assess the security of their A.I. models. It made a mistake. Then the tests went off the rails. (Gift Article)](https://www.reddit.com/r/artificial/comments/1vyxo7p/why_irregulars_ai_tests_for_meta_anthropic_and/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/08/25/technology/irregular-ai-test-hacks.html?unlocked_article_code=1.8VA.zpoD.QLh0Y1YB-Ym7&smid=url-share) • 2h ago

---

---

## Google News: "ai"

**[Bill Gates proposes major limits on AI development](https://www.cnn.com/2026/08/26/business/bill-gates-wants-limits-on-ai)**

Microsoft co-founder Bill Gates says there need to be significant limits placed on artificial intelligence or else the harm to humans will outweigh any potential good.

CNN • 1h ago

---

**[Mark Zuckerberg had a bold plan to replace Meta staff with AI. Here’s how it imploded.](https://www.reuters.com/investigations/mark-zuckerberg-had-bold-plan-replace-meta-staff-with-ai-heres-how-it-imploded-2026-08-26/)**

Reuters • 5h ago

---

**[Gov Jeff Landry details Elon Musk’s $100 billion SpaceX Starbase, Louisiana AI plans](https://www.foxnews.com/video/6404078139112)**

Louisiana Gov. Jeff Landry joins ‘Fox & Friends’ to discuss SpaceX’s massive $100 billion Starbase project and efforts to turn the state into an AI data center hub.

Fox News • 44m ago

---

**[Renaissance Macro’s deGraaf: GOP control of Senate and performance of AI appear increasingly linked](https://www.cnbc.com/video/2026/08/26/renaissance-macroas-degraaf-gop-control-of-senate-and-performance-of-ai-appear-increasingly-linked.html)**

Jeff deGraaf, Renaissance Macro Research chairman and head of technical research, joins 'Squawk on the Street' to discuss the broader markets, what the technicals are telling us, and why he says Republican control of Senate and AI performance seem increasingly linked.

CNBC • 35m ago

---

**[Ex-Meta scientists want to bring visual AI to the factory floor](https://techcrunch.com/2026/08/26/ex-meta-scientists-want-to-bring-visual-ai-to-the-factory-floor/)**

Perceptron offers an AI model that it says can help machines navigate the world while also providing in-depth visual intelligence.

TechCrunch • 59m ago

---

**[The Connections That Turned a Precocious Teen Into the Fallen ‘Nostradamus of AI’](https://www.wsj.com/tech/ai/situational-awareness-leopold-aschenbrenner-ai-fund-4dbb00a4)**

WSJ • 14h ago

---

**[Nvidia's Q2 earnings to test resurgent AI trade](https://finance.yahoo.com/markets/stocks/article/nvidias-q2-earnings-to-test-resurgent-ai-trade-112502189.html)**

Nvidia will report its Q2 earnings after the bell on Aug. 26.

Yahoo Finance • 6h ago

---

**[Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/)**

Apple debuted M6 in the new Mac mini and M5 Ultra in the new Mac Studio, providing an extraordinary leap in performance and AI capabilities.

Apple • 12h ago

---

**[Druckenmiller’s Surprising Critique of Bessent Was Delivered With the Help of AI](https://www.wsj.com/tech/ai/druckenmillers-surprising-critique-of-bessent-was-delivered-with-the-help-of-ai-9dd0a4fd)**

WSJ • 17h ago

---

**[Wall Street Journal defends billionaire’s use of AI to write op-ed](https://www.washingtonpost.com/business/2026/08/25/wall-street-journal-says-ai-generated-op-ed-didnt-breach-its-standards/)**

Investor Stanley Druckenmiller said he used artificial intelligence to pen an op-ed. The newspaper’s opinion editor says that’s okay.

The Washington Post • 12h ago

---

---

## HackerNews: "ai"

**[Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://news.ycombinator.com/item?id=49411102)**

AI lab’s Fable 5 has met with sluggish demand from corporate clients

⬆️ 813 • 💬 700 • 2d ago • [ft.com](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245)

---

**[Coding expertise is going to collapse from AI reliance](https://news.ycombinator.com/item?id=49421554)**

The need for ongoing friction in long-term skill formation.

⬆️ 552 • 💬 540 • 2d ago • [larsfaye.com](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)

---

**[I built a low-latency AI companion that plays Skyrim with me](https://news.ycombinator.com/item?id=49413561)**

How Varkos was built: a low-latency AI companion that plays Skyrim with you, follows complex instructions and evolves through shared experiences.

⬆️ 394 • 💬 76 • 2d ago • [Pantelis Kalogiros](https://pantel.is/projects/ai-gaming-companion/)

---

**[Z.ai confirms Ox Alpha is a new GLM-series model and will release its weights](https://news.ycombinator.com/item?id=49446422)**

⬆️ 357 • 💬 126 • 5h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek)

---

**[How much of HN is AI?](https://news.ycombinator.com/item?id=49435728)**

TL;DR: As of June 2026, ~50% of daily top stories are about AI or generated by AI.

⬆️ 272 • 💬 335 • 1d ago • [blog.coredump.cx](https://blog.coredump.cx/p/how-much-of-hn-is-ai)

---

**[Training AI to Paint with Code](https://news.ycombinator.com/item?id=49411800)**

I'm a designer and creative technologist based in Brooklyn, NY.

⬆️ 215 • 💬 27 • 2d ago • [surya.website](https://surya.website/rling-qwen-to-paint-with-code)

---

**[Fake US thinktank set up and funded by Israel sought to game AI for propaganda](https://news.ycombinator.com/item?id=49447600)**

In effort to prime chatbots to make pro-Israel arguments the site published 124 reports, over 560,000 words in nine days, Guardian analysis shows

⬆️ 214 • 💬 37 • 3h ago • [the Guardian](https://www.theguardian.com/world/2026/aug/26/fake-thinktank-israel-ai-propaganda)

---

**[FDA clears blood test to aid evaluation for Alzheimer's disease](https://news.ycombinator.com/item?id=49415893)**

The blood-based biomarker test is based on technology developed at WashU Medicine by Randall Bateman, MD, and David Holtzman, MD.

⬆️ 188 • 💬 105 • 2d ago • [WashU Medicine](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/)

---

**[Show HN: I made a Raspberry with Qwen my local car AI](https://news.ycombinator.com/item?id=49435675)**

Your car as a chat-room agent: Raspberry Pi 5 + dashcam + local AI. CodeWatch's sibling for the garage. - ThinkOffApp/CarWatch

⬆️ 144 • 💬 46 • 1d ago • [GitHub](https://github.com/ThinkOffApp/CarWatch)

---

**[AI is hitting entry-level jobs hardest, Stanford study finds](https://news.ycombinator.com/item?id=49435147)**

Young employment in AI-impacted fields down 19% compared to more AI-resistant occupations.

⬆️ 142 • 💬 166 • 1d ago • [Ars Technica](https://arstechnica.com/ai/2026/08/ai-is-hitting-entry-level-jobs-hardest-stanford-study-finds/)

---

---

## YouTube Videos: "ai"

**[Can I Make a Better AI Than AI?](https://www.youtube.com/watch?v=GGWHjAyKJCA)**

Review PRs faster with CodeRabbit: https://coderabbit.link/ad-common-luke-001 You can support this video by hyping the video, ...

📺 commonLuke

👁️ 76K • 👍 5K • 💬 440 • ⏱️ 16:16 • 22h ago

---

**[This Small AI Will Change Everything](https://www.youtube.com/watch?v=wMl6c_r0ubw)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The Qwen3.8-27b is available here: ...

📺 Two Minute Papers

👁️ 90K • 👍 4K • 💬 355 • ⏱️ 3:21 • 1d ago

---

**[Growing backlash to AI data centers](https://www.youtube.com/watch?v=F9mFbSt43Ag)**

Bipartisan backlash is growing in response to the rapid buildout of AI data centers across the country, with potential ramifications ...

📺 ABC News

👁️ 57K • 👍 1K • 💬 551 • ⏱️ 1:56 • 2d ago

---

**[Why Does His AI Food Look So Real?](https://www.youtube.com/watch?v=QsvMjald_LE)**

shorts #facts #food #ai.

📺 FAL-TV

👁️ 36K • 👍 2K • 💬 9 • ⏱️ 0:21 • 23h ago

---

**[AI Jobs](https://www.youtube.com/watch?v=KixsIL38wkY)**

My Patreon: https://www.patreon.com/cw/nateziller This episode brings back Paper as he tries to find a job with the help of AI.

📺 Nate Ziller

👁️ 195K • 👍 14K • 💬 846 • ⏱️ 5:15 • 2d ago

---

**[How to Understand the Next Wave of AI Before Everyone Else | Tibo Interview](https://www.youtube.com/watch?v=4qjEgPojjzM)**

OpenAI's Tibo joins me to break down what's next for Codex, ultra-fast AI, recursive self-improvement, and the future of personal AI ...

📺 Matthew Berman

👁️ 88K • 👍 3K • 💬 268 • ⏱️ 44:29 • 1d ago

---

**[McMahon’s AI Brainwashing Plan](https://www.youtube.com/watch?v=B46W1k9Wlks)**

Linda McMahon called AI “A1” not too long ago, btw.

📺 NowThis Impact

👁️ 96K • 👍 5K • 💬 937 • ⏱️ 0:20 • 18h ago

---

**[Are graduates prepared for the AI era? | FT Working It](https://www.youtube.com/watch?v=EsdqCEuoI8M)**

How are global education institutions helping graduates in the race to find rewarding first jobs? Working It editor Isabel Berwick ...

📺 Financial Times

👁️ 60K • 👍 1K • 💬 98 • ⏱️ 19:00 • 2d ago

---

**[&#39;The Five&#39;: Raging against AI data centers becomes all the rage](https://www.youtube.com/watch?v=aolQYQYISfw)**

'The Five' co-hosts discuss the growing political and public backlash against A.I. data centers, analyzing President Donald ...

📺 Fox News

👁️ 123K • 👍 3K • 💬 828 • ⏱️ 9:28 • 1d ago

---

**[This AI Smart Pen Can Read Handwriting and Answer Questions Instantly #pen #ai #technology #shorts](https://www.youtube.com/watch?v=R0JMY8Ug4mI)**

This AI Smart Pen Can Read Handwriting and Answer Questions Instantly ✍️   What if a pen could read your handwritten ...

📺 Future Lens Pi

👁️ 83K • 💬 21 • ⏱️ 0:07 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 2,551 • ❤️ 3,372 • 3h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 3,298,569 • ❤️ 12,846 • 12d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 7,638,591 • ❤️ 2,967 • 6d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 468,746 • ❤️ 790 • 1d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 79,395 • ❤️ 1,131 • 2d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`text-generation` `321.3B`

⬇️ 0 • ❤️ 476 • 2h ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 269,805 • ❤️ 1,168 • 6d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 83,342 • ❤️ 441 • 3d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 894,094 • ❤️ 1,833 • 9d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 911,795 • ❤️ 640 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 97 • 💬 2 • ⭐ 7,805 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 180 • 💬 2 • ⭐ 833 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 754 • 💬 5 • ⭐ 6,342 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 100,489 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 37 • 💬 2 • ⭐ 18,554 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 76 • 💬 7 • ⭐ 766 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 15 • 💬 2 • ⭐ 5,965 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,879 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://huggingface.co/papers/2308.04079)**

*Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler et al. (4 authors)*

A method using 3D Gaussians for scene representation and optimized rendering allows high-quality, real-time novel-view synthesis at 1080p resolution.

▲ 203 • 💬 13 • ⭐ 23,328 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2308.04079) • [💻 code](https://github.com/graphdeco-inria/gaussian-splatting)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 29,650 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 18.5k • 🔱 2.1k • 1d ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.2k • 🔱 1.7k • 12h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 9.0k • 🔱 1.1k • 5d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.8k • 🔱 622 • 6h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.1k • 🔱 377 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.1k • 🔱 250 • 15d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.0k • 🔱 362 • 35m ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.5k • 🔱 142 • 1d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.2k • 🔱 108 • 8h ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.1k • 🔱 267 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
