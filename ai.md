---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-07T15:26:40.134866+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 07, 2026 at 15:26 UTC  
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

**[AI is scaling 3x faster than the internet wave and it’s NOT slowing down](https://www.reddit.com/r/artificial/comments/1upou8z/ai_is_scaling_3x_faster_than_the_internet_wave/)**

One thing that stands out about the current AI boom is that it hasn't had a slow phase. A lot of previous technology waves had a big moment, cooled off for a while and then found their next use case. Recent estimates suggest GenAI companies are generating around $110B in annual revenue and the growth rate is reportedly around 3x faster than previous IT waves like the internet and mobile. What's interesting is that the pace has held through every phase since 2022; first it was chatbots, then coding copilots and now it's AI agents and if you’ve followed this space closely enough, you can see instead of one trend replacing another, each wave seems to be creating demand for the next one. I think that's also changing how people build and consume. A year or two ago, most of the conversation was about finding the best model, but now devs are paying attention to everything around the model too such as: retrieval, evaluations, data pipelines, deployment, and infrastructure. If AI is becoming part of more products, the supporting stack starts to matter just as much as the model itself. You can see it in the open-source ecosystem. Models keep improving, but so do the tools around them

7h ago

---

**[SpaceX burned up 260 of its own satellites in 6 months and this is just routine apparently](https://www.reddit.com/r/artificial/comments/1upbdoa/spacex_burned_up_260_of_its_own_satellites_in_6/)**

Saw this in an article and it's been on my mind since 260 satellites intentionally burned in the atmosphere in 6 months and another 349 queued. They're planning 42,000 total eventually. No debris which is fine but researchers are asking what happens when you're burning hundreds of massive metal objects in the upper atmosphere repeatedly over years. Aluminum particles, potential atmospheric chemistry changes. Science is still catching up and the FCC is now proposing to exempt satellites from environmental review entirely Idk,we're moving faster than we're studying this...anyone else find this a bit much?

17h ago

---

**[AI should be private and optional!](https://www.reddit.com/r/artificial/comments/1uplbps/ai_should_be_private_and_optional/)**

AI should be private and optional.

10h ago

---

**[What do normal people use ai for?](https://www.reddit.com/r/artificial/comments/1upq8r2/what_do_normal_people_use_ai_for/)**

I understand very generally that AI is good at "writing code" but I'm wondering what specifically normal people would need the capability to write code for in their daily lives? Unless they work in an industry that relies on coding in which case it's self explanatory. I personally just use chatgpt for general conversation and talking about life.

5h ago

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don’t Exist](https://www.reddit.com/r/artificial/comments/1upfz1n/scammers_sell_seeds_for_exotic_aigenerated/)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

🔗 [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/) • 14h ago

---

**[Agent OPFOR — open-source adversary emulation for AI agents. Named after the concept for a reason.](https://www.reddit.com/r/artificial/comments/1upy4cy/agent_opfor_opensource_adversary_emulation_for_ai/)**

OPFOR: Opposition Force. The unit that plays the enemy in training so everyone else learns what real attacks feel like before they come. That's the mental model for this tool. We built Agent OPFOR to red-team AI agents the way an actual adversary would — not a static eval, not a single-shot probe. Multi-turn adversarial conversations, adaptive attack campaigns, full audit trail. What the attack surface covers: Prompt injection and jailbreaks (multi-turn, not single prompt) System prompt extraction Tool misuse and BOLA/BFLA via tool-calling agents MCP endpoint attacks — tool description injection, secret exposure, scope escalation, SSRF Memory poisoning Excessive agency and goal hijacking EU AI Act bias testing opfor hunt — autonomous red team mode: Give it an endpoint and an objective. A commander agent plans the campaign, operators run the probes, a scout handles recon. The commander adapts based on what each response reveals. Add --ui to watch the attack tree live.

🔗 [GitHub](https://github.com/KeyValueSoftwareSystems/agent-opfor) • 9m ago

---

**[you can just watch a language model think now. i built a way to visualize the words AI doesn’t say](https://www.reddit.com/r/artificial/comments/1upejv3/you_can_just_watch_a_language_model_think_now_i/)**

anthropic published the J-space paper today. tl;dr: models have a small emergent set of internal “silent words” (~a few dozen concepts at a time, <10% of activations) that they can report on, control, and use for reasoning. the measurement tool is the jacobian lens and they open sourced it, and neuronpedia posted pre-fitted lenses for qwen. so the obvious next step was to wire it into a chat UI and just… look at it. subtext runs qwen3.5-4B in bf16 on a single 12GB GPU and reads the lens at 9 layers on every token — both while the model reads your message and while it replies. streams at full generation speed (the lens is just a matmul + unembed per layer, basically free). favorite moment: type “is this correct? 12 + 5 = 1” and incorrect lights up mid-network while it’s still reading the equation. zero reply tokens exist at this point. the verdict is just sitting there, internally, before the model says anything. repo: https://github.com/ninjahawk/Subtext no GPU: recorded session replays in the browser: https://ninjahawk.github.io/Subtext/ paper: https://www.anthropic.com/research/global-workspace the live readout path is verified against anthropic’s reference implementation — audit script in the repo, top-5 matches exactly at every layer/position tested, cosine 0.99998. that’s it. questions welcome.

15h ago

---

**[Made a project For helping students in studies [P]](https://www.reddit.com/r/artificial/comments/1upxb80/made_a_project_for_helping_students_in_studies_p/)**

Made a cool project check it out used for learning especially for indian students

37m ago

---

**[Verbalizable Representations Form a Global Workspace in Language Models](https://www.reddit.com/r/artificial/comments/1upwayi/verbalizable_representations_form_a_global/)**

🔗 [transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html) • 1h ago

---

**[I adapted 1,200-year-old Islamic hadith verification methodology into a trust framework for multi-agent AI systems](https://www.reddit.com/r/artificial/comments/1upwa8i/i_adapted_1200yearold_islamic_hadith_verification/)**

When a multi-agent AI system answers you, that answer has passed through several “hands” - a scraper, an ingestion model, a synthesis model. Each can distort or invent. Current tools log what happened, but nothing grades who transformed a claim or how much to trust the result. Classical Islamic hadith scholarship spent ~1,200 years on a structurally identical problem: whether to trust knowledge passed through chains of human narrators. Their solution: grade every transmitter, judge a chain by its weakest link, require independent corroboration, criticize content separately from the chain — maps surprisingly cleanly onto AI pipelines. So I built it, a framework, a paper (with DOI), and a Python package (pip install isnad). I’m developing it in the open and being honest about what’s validated vs. still experimental, early results show the core grading mechanism works, but full pipeline validation is ongoing. I’m an independent researcher, so critique is genuinely welcome! https://doi.org/10.5281/zenodo.21211291

1h ago

---

---

## Google News: "ai"

**[EXCLUSIVE: Beijing is looking at curbing overseas access to China's top AI models, sources say](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/)**

Reuters • 1h ago

---

**[AI Giants Are Handing Out Tons of Free Computing Power to Grab Startup Share](https://www.wsj.com/tech/ai/ai-giants-are-handing-out-tons-of-free-computing-power-to-grab-startup-share-c00a5c5c)**

WSJ • 14h ago

---

**[Pore substitute: can AI be trusted when it comes to skincare advice?](https://www.theguardian.com/commentisfree/2026/jul/08/ai-artificial-intelligence-medical-health-advice-diagnosis-expertise-skincare-dermatology)**

There are more than 3,000 conditions in dermatology, experts warn – and chatbots’ recommendations can be flaky

The Guardian • 25m ago

---

**[Warren demands that Pentagon and AI companies release full military contracts](https://www.nbcnews.com/tech/security/warren-elizabeth-pentagon-ai-companies-release-full-military-contracts-rcna352662)**

In letters seen by NBC News, Sen. Warren raised concerns over the deals between the government and tech companies and the potential for AI-powered surveillance and weapons.

NBC News • 26m ago

---

**[What Cannes Lions 2026 Taught Marketers About AI And Human Connection](https://www.forbes.com/sites/committeeof200/2026/07/07/what-cannes-lions-2026-taught-marketers-about-ai-and-human-connection/)**

Cannes Lions 2026 reframed the role of AI across creativity, strategy, research, personalization, and human connection.

Forbes • 21m ago

---

**[Samsung's 19-fold rise in profit fails to impress investors as AI chip stocks fall](https://finance.yahoo.com/technology/article/samsungs-19-fold-rise-in-profit-fails-to-impress-investors-as-ai-chip-stocks-fall-120636336.html)**

Samsung's record profits failed to impress investors on Tuesday.

Yahoo Finance • 3h ago

---

**[Samsung profits jump 1,800% as AI chip sales soar](https://www.bbc.com/news/articles/c1kyy8yrpxdo)**

It comes as demand for semiconductors continues to outstrip supplies, which has pushed up prices.

BBC • 7h ago

---

**[Glance And Samsung Partner To Bring AI-Assisted Shopping To The TV](https://www.forbes.com/sites/sharonedelson/2026/07/07/glance-and-samsung-partner-to-bring-ai-assisted-shopping-to-the-tv/)**

Glance and Samsung formed a partnership to transform the living room screen into a personalized AI-powered browsing platform, to be available on millions of Samsung smart TVs.

Forbes • 1h ago

---

**[Microsoft cuts 4,800 positions, insists jobs 'not being replaced by AI'](https://www.foxbusiness.com/fox-news-tech/microsoft-ai-layoffs-workforce-restructuring)**

Microsoft is eliminating roughly 4,800 jobs while investing heavily in AI, with executives saying artificial intelligence is changing work but not replacing affected employees.

Fox Business • 1d ago

---

**[AI actor Tilly Norwood set to star in first feature film](https://www.cbsnews.com/news/tilly-norwood-ai-generated-actor-feature-film/)**

AI-generated actor Tilly Norwood is set to star in her first feature film, with her creator saying that "art will be imitating life."

CBS News • 1h ago

---

---

## HackerNews: "ai"

**[GLM 5.2 and the coming AI margin collapse](https://news.ycombinator.com/item?id=48809877)**

GLM 5.2 is the first open weights model I'd call a genuine competitor to Opus and GPT for agentic work - at ~15-20% of the price. Part one of why AI inference margins are about to collapse.

⬆️ 602 • 💬 381 • 19h ago • [Martin Alderson](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

---

**[AMD Ryzen AI Halo – $4k AI Dev Kit](https://news.ycombinator.com/item?id=48805624)**

Welcome to LTT Labs - your go-to destination for all things tech. Explore comprehensive test results, insightful commentary, and the latest analysis in hardware.

⬆️ 366 • 💬 239 • 1d ago • [LTT Labs](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

---

**[Small AI Models Gain Traction In places with unreliable networks](https://news.ycombinator.com/item?id=48812055)**

In places with unreliable networks and no data-center infrastructure, smaller is better

⬆️ 223 • 💬 68 • 15h ago • [IEEE Spectrum](https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals)

---

**[OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files](https://news.ycombinator.com/item?id=48807225)**

OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation req...

⬆️ 202 • 💬 61 • 22h ago • [GitHub](https://github.com/iOfficeAI/OfficeCLI)

---

**[New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://news.ycombinator.com/item?id=48796817)**

⬆️ 178 • 💬 112 • 1d ago • [intextbooks.science.uu.nl](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf)

---

**[Delta flight hit by firework while landing at Midway Airport on Fourth of July](https://news.ycombinator.com/item?id=48797141)**

A Delta flight arriving at Chicago's Midway International Airport on the Fourth of July reportedly made contact with a firework, the airline said.

⬆️ 171 • 💬 389 • 1d ago • [NBC Chicago](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

---

**[Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://news.ycombinator.com/item?id=48799256)**

Instead, buy domestic product, and out in the open.

⬆️ 163 • 💬 79 • 1d ago • [readtheline.ca](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)

---

**[Mark Zuckerberg tells staff that AI agents haven't progressed enough](https://news.ycombinator.com/item?id=48795826)**

At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated.

⬆️ 133 • 💬 2 • 1d ago • [TechCrunch](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/)

---

**[When AI Costs More Than the Engineer](https://news.ycombinator.com/item?id=48801493)**

Anthropic spends 2.3x payroll on compute. Top software firms spend 0.4x. Three scenarios for where the rest of the market lands by 2029.

⬆️ 125 • 💬 111 • 1d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-spend-breakeven-2029/)

---

**[AI has torched the market for junior programmers](https://news.ycombinator.com/item?id=48788361)**

Junior programmers are getting destroyed by AI — down 19%, while devs over 40 thrive. Meanwhile, millions of non-developers are shipping real software without the job title. The credential market collapsed; the activity exploded. The problem: nobody's building the next generation of senior engineers.

⬆️ 100 • 💬 194 • 2d ago • [seldo.com](https://seldo.com/posts/ai-has-torched-the-market-for-junior-programmers/)

---

---

## YouTube Videos: "ai"

**[One Chinese AI Model Wiped Out $1 Trillion In A Single Day — And They&#39;re Just Getting Started](https://www.youtube.com/watch?v=WUTkCiNEDWU)**

ATT Business: Switch to AT&T Business at business.att.com Paleovalley: 30 for $36 https://bit.ly/PaleovalleyIT 80% of every dollar ...

📺 Tom Bilyeu

👁️ 7K • 👍 534 • 💬 117 • ⏱️ 34:31 • 2h ago

---

**[How to Make Animation Videos With Canva AI (Full Guide)](https://www.youtube.com/watch?v=IxHtyTcey5I)**

Watch Next https://www.youtube.com/watch?v=dOmKYJoRboE&pp=0gcJCSgLAYcqIYzv In this video, I show how to create a ...

📺 Isa does AI

👁️ 4K • ⏱️ 9:24 • 56m ago

---

**[I Tried Every AI UGC Ads Video Generator (use this)](https://www.youtube.com/watch?v=ExGT6vbI1Vo)**

Arcads vs Higgsfield vs Topview & More - Which Is Best At AI Ads? Try Higgsfield: https://higgsfield.ai?fpr=utm&fp_sid=mira Hey ...

📺 Mira AI

👁️ 3K • ⏱️ 12:15 • 1h ago

---

**[AI-generated &#39;actress&#39; Tilly Norwood making feature film debut](https://www.youtube.com/watch?v=8LNO6vbLHlI)**

The studio behind AI-generated "actress" Tilly Norwood has announced its creation will be "starring" in a new film. AI-powered ...

📺 ABC News

👁️ 3K • 👍 24 • 💬 67 • ⏱️ 1:31 • 4h ago

---

**[How to Start an AI Agent Business as a Teenager in 2026](https://www.youtube.com/watch?v=fCg0xKdy7CU)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Jake One Page

👁️ 2K • ⏱️ 24:18 • 1h ago

---

**[The Dirty AI lie : How the GREATEST bet in human history started to crack in June 2026?](https://www.youtube.com/watch?v=WcckBmkauBQ)**

Check out Odoo: https://www.odoo.com/r/ChAT ⭐️ Think School's flagship Communication course with live doubt sessions ...

📺 Think School

👁️ 897K • 👍 27K • 💬 1K • ⏱️ 20:53 • 1d ago

---

**[AI expert worries about the risk of humans losing control | Four Corners](https://www.youtube.com/watch?v=gYORRh377Gw)**

Jeffrey Ladish consulted on security for AI giant Anthropic. Now as Executive Director at Palisade Research he tests AI agents and ...

📺 ABC News In-depth

👁️ 28K • 👍 746 • 💬 76 • ⏱️ 15:06 • 1d ago

---

**[Grok AI Was Asked Who Built the Pyramids - The Answer Shocked Everyone](https://www.youtube.com/watch?v=A4cY1bCgC_A)**

There is a structure standing in the desert outside Cairo that, by every measure of physics and mathematics, should not exist.

📺 New Discovery

👁️ 440K • 👍 4K • 💬 629 • ⏱️ 30:44 • 2d ago

---

**[Can China cheat its way to AI supremacy? | BBC News](https://www.youtube.com/watch?v=K8hYErmwhaI)**

The race between America and China to lead the world in artificial intelligence is reshaping the global balance of power.

📺 BBC News

👁️ 56K • 👍 1K • 💬 597 • ⏱️ 26:13 • 1d ago

---

**[I Tested AI&#39;s Morality 🤯](https://www.youtube.com/watch?v=JkLjf4pJi9w)**

📺 Zack D. Films

👁️ 7.4M • 👍 567K • 💬 10K • ⏱️ 0:55 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,683,711 • ❤️ 1,717 • 8d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 281,584 • ❤️ 3,569 • 5d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 121 • ❤️ 427 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,084,945 • ❤️ 1,821 • 4d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 14,723 • ❤️ 363 • 4d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 9,458 • ❤️ 274 • 3d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 538,687 • ❤️ 306 • 7d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 502,663 • ❤️ 771 • 12d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 3,886 • ❤️ 181 • 2d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 384,383 • ❤️ 1,069 • 18d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 28 • 💬 1 • ⭐ 290 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 107 • 💬 4 • ⭐ 91,571 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,561 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 252 • 💬 4 • ⭐ 11,318 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 8 • 💬 0 • ⭐ 5,475 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 73,691 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 3 • ⭐ 10,098 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 35 • 💬 1 • ⭐ 150 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,673 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 13 • 💬 2 • ⭐ 18,912 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 76.6k • 🔱 4.1k • 13h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.6k • 🔱 1.1k • 1h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.6k • 🔱 873 • 27m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 6.4k • 🔱 816 • 4h ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 3.1k • 🔱 706 • 22h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.5k • 🔱 214 • 3d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.1k • 🔱 78 • 19h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 89 • 24d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.4k • 🔱 121 • 9d ago

---

**[apple/coreai-models](https://github.com/apple/coreai-models)**

Model export recipes, Python primitives, and Swift runtime utilities for on-device AI

`Swift`

⭐ 1.3k • 🔱 108 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
