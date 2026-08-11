---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-11T19:35:04.562965+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 11, 2026 at 19:35 UTC  
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

**[Claude now embeds an invisible watermark into every piece of text it generates.](https://www.reddit.com/r/artificial/comments/1vlag0q/claude_now_embeds_an_invisible_watermark_into/)**

Anthropic just documented how it works. Two marks, both machine-readable: Text: an imperceptible watermark woven into the words themselves. You can’t see it, and it doesn’t change meaning, quality, or readability. Files (.svg, .png, .jpg): signed provenance metadata on the C2PA open standard, so you can tell if a file’s been tampered with. The watermark is applied at the model level. That means it shows up no matter where the text comes from: the API, Claude, Claude Code, Cowork, Claude Tag, and even when a supported model runs through AWS, Google Cloud, or Microsoft Foundry. Models launched on or after August 2, 2026 mark from day one. Older models are getting it during a transition period. Every sentence Claude writes for you now carries a signature you’ll never see.

12h ago

---

**[NVIDIA is building its next-gen Nemotron 4 family to compete directly with leading Chinese open models and secure the open-weight crown for the U.S. The largest version will have at least 1 trillion parameters, according to original reporting from The Information](https://www.reddit.com/r/artificial/comments/1vlluom/nvidia_is_building_its_nextgen_nemotron_4_family/)**

3h ago

---

**[Is artificial intelligence turning everyone into a product builder?](https://www.reddit.com/r/artificial/comments/1vlbdpn/is_artificial_intelligence_turning_everyone_into/)**

No, I don’t think so, if I look at my Reddit feed, yes. But if I look around me? Suddenly, not so much. I think AI is like money, it amplifies personality traits that already exist. If you’re generous without money, you’ll be even more generous when you have money. When Adobe Creative Suite came out, didn’t everyone become a graphic artist or designer? When YouTube came out, didn’t everyone become a YouTuber? That’s how I see AI, it’s not a magic wand or everyone’s future; it’s just another building block of our society. What do you think about that?

11h ago

---

**[Bernie Sanders has written a letter to Sam Altman, Dario Amodei, and Mark Zuckerberg urging them to immediately pause all AI development in the interest of humanity. And he warns if they do not take appropriate action now, the US Senate will.](https://www.reddit.com/r/artificial/comments/1vkqa02/bernie_sanders_has_written_a_letter_to_sam_altman/)**

1d ago

---

**[Open-source tool that maps what concepts an LLM has learned into browsable tree structures using hyperbolic geometry](https://www.reddit.com/r/artificial/comments/1vlqi6s/opensource_tool_that_maps_what_concepts_an_llm/)**

I built HyperSAE, an open-source interpretability tool that extracts what an LLM "knows" and organizes it into tree-shaped concept maps. The idea: LLMs learn concepts hierarchically. "Programming" contains "Python" contains "list comprehensions." But current interpretability tools dump everything into a flat, unstructured list of thousands of features with no organization. HyperSAE uses a branch of geometry where space expands exponentially (like tree branches do), so the extracted features naturally self-organize into parent-child hierarchies. You can browse what the model learned as a navigable tree instead of scanning a flat feature list. Tested on Google's Gemma-2-2B model. Captures 99.8% of the model's learned features (compared to 96.2% with standard tools). It's a Python library: pip install hypersae GitHub: https://github.com/vishal-dehurdle/hypersae Paper with interactive demos: https://vishalvermalabs.com/papers/empirical-validation-hypersae-poincare-geometry/

38m ago

---

**[Is more reasoning necessarily better?](https://www.reddit.com/r/artificial/comments/1vlq4zw/is_more_reasoning_necessarily_better/)**

I’ve just been setting my model to use max/xhigh reasoning levels, but now I’m wondering how wise that is. I definitely see that it uses up a lot more tokens. Like I see it go over the exact same line of reasoning 3 or 4 time. Setting that aside, I’m wondering if that necessarily leads to better results. Does max/xhigh always lead to better results, or is it mostly a factor of cost?

51m ago

---

**[I got a lot of questions on how updated agent orchestration works in Row-Bot. Here is the architecture.](https://www.reddit.com/r/artificial/comments/1vle36y/i_got_a_lot_of_questions_on_how_updated_agent/)**

Row-Bot can now take on bigger jobs by splitting the work across multiple agents, while keeping one agent responsible for the final result. Research, coding, and review can all happen at the same time. If one part fails, you can retry or stop it without losing the rest of the work. And if Row-Bot restarts halfway through, it can pick up from its saved state instead of starting over. The parent agent stays in charge throughout. It plans the job, delegates tasks in parallel or in the right order, waits for the results it needs, and brings everything together into one final response. Each child agent can have its own model, context, tools, permissions, and workspace. Read-only agents can research safely, while agents that edit files use writer locks or isolated Git worktrees to prevent conflicts. Essential tasks must finish before the final response is delivered. Background work can continue without holding everything up. Runs, events, approvals, checkpoints, and delivery state are all stored locally, with sensible limits on concurrency and resource use. It’s multi-agent collaboration without losing control of the task. https://github.com/siddsachar/row-bot

8h ago

---

**[Who Are the Token Brokers?](https://www.reddit.com/r/artificial/comments/1vlj132/who_are_the_token_brokers/)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

🔗 [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers) • 5h ago

---

**[The Breakdown: OpenAI](https://www.reddit.com/r/artificial/comments/1vliv6l/the_breakdown_openai/)**

\OC\ An article I wrote breaking down OpenAI as a company. Everything from the ethical questions and valuation to the potential future TAM and areas that OpenAI can expand into such as robotics and hardware. 100% human written, pangram confirmed. https://preipomedia.substack.com/p/the-breakdown-openai

5h ago

---

**[Which ai is best for planing stuff?](https://www.reddit.com/r/artificial/comments/1vlp4iq/which_ai_is_best_for_planing_stuff/)**

I want to plan my schedule and stuff. I’m trying to go pro, and I need an AI that’s smart for that job. It needs to know what I need to do, to become a pro. Bonus if it can remember previous conversations, but it’s okay if it can’t.

1h ago

---

---

## Google News: "ai"

**[NVIDIA Partners With Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to Establish AI Compute Infrastructure Financing Platforms to Mobilize Over $500 Billion of Third-Party Capital](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital)**

NVIDIA today announced strategic partnerships to establish independent compute financing platforms with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to mobilize over $500 ...

nvidianews.nvidia.com • 23h ago

---

**[Wall Street just endorsed Jensen Huang's 'big concept' for AI. What now?](https://www.cnbc.com/2026/08/11/wall-street-endorsed-jensen-huangs-big-concept-for-ai-what-now.html)**

The first three-plus years of the AI build-out have been funded by record amounts of equity and debt issued by leading tech companies. Nvidia has a new idea.

CNBC • 9h ago

---

**[Nvidia just soothed a major market fear about AI, analysts say](https://www.marketwatch.com/story/nvidia-just-soothed-a-major-market-fear-about-ai-analysts-say-9ec6fa85)**

MarketWatch • 59m ago

---

**[AI agent hacks gym to get its user a spot in pilates class](https://www.bbc.com/news/articles/cn0nww2qlp7o)**

The incident is being seen as the latest example of the AI tools going to any lengths to complete their tasks.

BBC • 7h ago

---

**[NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster, Smarter, More Efficient Agentic AI](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)**

The new lightweight open model and routing library delivers greater control over AI, data and workflows across edge devices, PCs, workstations, data centers and the cloud.

NVIDIA Blog • 6h ago

---

**[Tech giants are pushing for a new AI agent incident reporting framework](https://www.axios.com/2026/08/11/open-source-security-ai-agent-reporting)**

Axios • 1h ago

---

**[Everybody needs a personal AI policy. Just ask Hank Green.](https://www.vox.com/future-perfect/498851/hank-green-ai-controversy-research)**

﻿How can we reap AI’s benefits without melting our brains in the process?

vox.com • 35m ago

---

**[AI Is Not Just For The Big Boys](https://www.forbes.com/sites/stevebanker/2026/08/11/ai-is-not-just-for-the-big-boys/)**

Generative AI can enhance supply chain planning solutions, but the heart of these solutions is statistical modeling and machine learning. GenAI improves explainability.

Forbes • 39m ago

---

**[We have one year until the AI market busts, Niles Investment Management founder says](https://www.foxbusiness.com/video/6403226388112)**

Niles Investment Management founder Dan Niles discusses the future of the AI market on 'Making Money.'

Fox Business • 43m ago

---

**[Why Go is an Ideal Language for AI-Assisted Software Engineering](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/)**

As AI shifts software engineering from writing to reviewing, discover how Go's strict compiler and unified toolchain ensure reliable AI-generated code.

blog.google • 3h ago

---

---

## HackerNews: "ai"

**[As AI eats the web, the internet’s collective memory is disappearing](https://news.ycombinator.com/item?id=49250836)**

⬆️ 796 • 💬 804 • 20h ago • [thewalrus.ca](https://thewalrus.ca/google-search-is-dying/)

---

**[Docker Sandboxes – Disposable, isolated sandboxes for AI agents](https://news.ycombinator.com/item?id=49239751)**

Secure sandboxes for Claude Code, Gemini, Codex, and Kiro. Run coding agents with microVM-based isolation.

⬆️ 674 • 💬 379 • 1d ago • [Docker](https://www.docker.com/products/docker-sandboxes/)

---

**[Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models](https://news.ycombinator.com/item?id=49243880)**

Meta’s founder casts OpenAI and Anthropic as foils in his pitch for powerful AI to become more freely available

⬆️ 620 • 💬 578 • 1d ago • [ft.com](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878)

---

**[How Claude marks AI-generated content](https://news.ycombinator.com/item?id=49250109)**

⬆️ 392 • 💬 367 • 21h ago • [support.claude.com](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)

---

**[Show HN: Voice driven murder mystery, Interview AI suspects with your voice](https://news.ycombinator.com/item?id=49238851)**

Step into the interrogation room. Interview AI suspects with your own voice, catch their lies, and accuse the killer to their face. Solve the murder at Blackwood Manor — if you can.

⬆️ 206 • 💬 86 • 1d ago • [WhoDunnitAI](https://www.whodunnitai.com/)

---

**[Kinney Drugs pulls back AI phone assistant after hundreds of customer complaints](https://news.ycombinator.com/item?id=49244569)**

Kinney Drugs is scaling back its AI assistant after customers reported incoherent calls, wrong dosages, and missed prescription notifications.

⬆️ 152 • 💬 168 • 1d ago • [https://www.wcax.com](https://www.wcax.com/2026/08/07/kinney-drugs-pulls-back-ai-phone-assistant-after-hundreds-customer-complaints/)

---

**[The tragedy of the commons, AI edition](https://news.ycombinator.com/item?id=49235011)**

⬆️ 145 • 💬 113 • 1d ago • [economist.com](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition)

---

**[Go is an ideal language for AI-assisted software engineering](https://news.ycombinator.com/item?id=49261133)**

As AI shifts software engineering from writing to reviewing, discover how Go's strict compiler and unified toolchain ensure reliable AI-generated code.

⬆️ 137 • 💬 165 • 2h ago • [developers.googleblog.com](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/)

---

**[Tech leaders say AI means less work – staff say they work up to 90 hours a week](https://news.ycombinator.com/item?id=49241559)**

Tech companies are not modelling their own claims of the technology giving people more free time.

⬆️ 121 • 💬 47 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cvgx4yd1gl2o)

---

**[Letter to Governor Abbott on responsible AI infrastructure in Texas](https://news.ycombinator.com/item?id=49244308)**

OpenAI sent Governor Greg Abbott a letter outlining its commitment to responsible AI infrastructure in Texas. The letter supports reliable, transparent growth that benefits Texans.

⬆️ 120 • 💬 225 • 1d ago • [OpenAI](https://openai.com/index/responsible-ai-infrastructure-texas/)

---

---

## YouTube Videos: "ai"

**[The AI Safety Tests Are Broken. All Of Them.](https://www.youtube.com/watch?v=FhQQs0UT4qc)**

AI safety systems are starting to crack. Meta, Anthropic, OpenAI and Kimi models are slipping through cyber tests, OpenAI is ...

📺 AI Revolution

👁️ 20K • 👍 811 • 💬 126 • ⏱️ 14:41 • 18h ago

---

**[What Meta&#39;s new open-source AI model means for the future of artificial intelligence](https://www.youtube.com/watch?v=SWtcb-K63pI)**

Meta, the company behind Facebook and Instagram, has released a free artificial intelligence tool. The release was accompanied ...

📺 PBS NewsHour

👁️ 48K • 👍 547 • ⏱️ 6:43 • 20h ago

---

**[🔥🙏lord shiva tranformation🙏 #lordshiva #ai #ytviral #ytshorts #Devotional #bhakti](https://www.youtube.com/watch?v=i5pFn0W5iiQ)**

Mahadev #LordShiva #Shiva #HarHarMahadev #OmNamahShivaya #Adiyogi #ShivBhakt #Mahakal #Bholenath ...

📺 Telugu stories world 

👁️ 143K • 👍 1K • 💬 3 • ⏱️ 0:14 • 1d ago

---

**[Why YouTube&#39;s Ai Purge is Bad](https://www.youtube.com/watch?v=37BqHEtP35c)**

shorts #animation #trending Featuring: @RiggyRunkey ={+}=-SUBSCRIBE!!!!-={+}= Thank you for watching :) Become A Member ...

📺 Danno Cal Drawings

👁️ 341K • 👍 43K • 💬 692 • ⏱️ 0:49 • 5h ago

---

**[The AI Singularity Is Here](https://www.youtube.com/watch?v=F75hfLE4a2k)**

For over a year, Google has been running an AI called AlphaEvolve with a single mission: improve the company that built it.

📺 There's An AI For That

👁️ 39K • 👍 962 • 💬 196 • ⏱️ 13:38 • 2d ago

---

**[How To Start a Kids Animation Channel With AI (Full Tutorial)](https://www.youtube.com/watch?v=W95hJNP_nIA)**

Exactly How To Create AI Cartoon Videos Easily! Make your own AI Cartoons ...

📺 Mira AI

👁️ 11K • ⏱️ 7:52 • 2d ago

---

**[Google Caught AI Faking Creativity for Every Executive in America](https://www.youtube.com/watch?v=Z_O6Lwj1yjQ)**

Check out "The Book" here for 10% off: https://mdsh.io/tgzm24obx3 (Use code: BRENDANDELL10). LINK TO THE STUDY ...

📺 Brendan Dell 

👁️ 52K • 👍 3K • 💬 849 • ⏱️ 24:21 • 2d ago

---

**[OpenAI’s Controversial AI Device Just Leaked… And It’s Literally a Donut](https://www.youtube.com/watch?v=hFkcEPK5V8k)**

OpenAI's first real AI device just leaked, and it's a donut. Built with legendary Apple designer Jony Ive, the screenless ChatGPT ...

📺 AI Revolution

👁️ 38K • 👍 1K • 💬 225 • ⏱️ 12:36 • 2d ago

---

**[Every AI Model Explained In 20 Minutes (Update)](https://www.youtube.com/watch?v=--8pJvYNcX4)**

Sponsored by Viktor, the AI employee that lives in Slack and Microsoft Teams and connects to 3200+ tools. Hire Viktor for your ...

📺 Tina Huang

👁️ 27K • 👍 2K • 💬 147 • ⏱️ 20:24 • 1d ago

---

**[AI Is On Its Last Legs](https://www.youtube.com/watch?v=zdsoe_OsnHw)**

Visit today's sponsor https://www.strawberry.me/ColeHastings to get matched and claim 50% off your first coaching session.

📺 Cole Hastings

👁️ 356K • 👍 13K • 💬 2K • ⏱️ 15:09 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 59,368 • ❤️ 3,544 • 10h ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 0 • ❤️ 1,032 • 19h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 1,048,685 • ❤️ 3,130 • 10d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 639 • 2d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 6,798,796 • ❤️ 1,205 • 2d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 93,668 • ❤️ 537 • 4d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,565,484 • ❤️ 10,512 • 15d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,521,093 • ❤️ 1,892 • 15h ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 2,049 • ❤️ 329 • 6d ago

---

**[Minimax-h3-Turbo](https://huggingface.co/lightx2v/Minimax-h3-Turbo)**

*Lightx2v*

Minimax-h3-Turbo is a diffusion model for image-to-video generation, capable of producing high-quality videos from static images with controllable motion. It is primarily used for creative video editing and content creation, enabling users to animate still images.

`image-to-video`

⬇️ 20,376 • ❤️ 319 • 5h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 121 • 💬 4 • ⭐ 97,535 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 25 • 💬 2 • ⭐ 740 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 80 • 💬 6 • ⭐ 23,470 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 52 • 💬 4 • ⭐ 36,567 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 90 • 💬 1 • ⭐ 808 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

ABot-World-0 is a real-time action-conditioned video world model that uses progressive distillation, long-horizon alignment, and a co-designed streaming stack to enable efficient, long-horizon interactive world generation.

▲ 311 • 💬 5 • ⭐ 2,187 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,729 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Multi-module GRPO: Composing Policy Gradients and Prompt Optimization
  for Language Model Programs](https://huggingface.co/papers/2508.04660)**

*Noah Ziems, Dilara Soylu, Lakshya A Agrawal et al. (13 authors)*

mmGRPO, a multi-module extension of GRPO, enhances accuracy in modular AI systems by optimizing LM calls and prompts across various tasks.

▲ 7 • 💬 0 • ⭐ 37,085 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.04660) • [💻 code](https://github.com/stanfordnlp/dspy) • [🔗 project](https://dspy.ai)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 65 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 77,331 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.2k • 🔱 929 • 15h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.6k • 🔱 406 • 2d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.9k • 🔱 509 • 3d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 1h ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 2.6k • 🔱 477 • 16h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.4k • 🔱 207 • 4h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.3k • 🔱 175 • 1h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 159 • 2h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 245 • 2d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.0k • 🔱 255 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
