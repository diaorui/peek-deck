---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-19T11:58:46.633697+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 19, 2026 at 11:58 UTC  
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

**[Prompt injection works on Telegram romance scam bots](https://www.reddit.com/r/artificial/comments/1uzxful/prompt_injection_works_on_telegram_romance_scam/)**

Tried prompt injection on a bot that was trying to romance scam me. Worked immediately. Instead of switching platforms I just asked it what its actual task was. It dropped the persona instantly. These things are everywhere now. How long until they're indistinguishable?

21h ago

---

**[The White House is dictating access to frontier AI models, shifting power from tech giants, sources say](https://www.reddit.com/r/artificial/comments/1v010pk/the_white_house_is_dictating_access_to_frontier/)**

The Trump administration is taking steps to control who gets access to the latest frontier models, sources familiar with the matter told CNBC.

🔗 [CNBC](https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html) • 19h ago

---

**[AI saved me so much time...](https://www.reddit.com/r/artificial/comments/1v0on87/ai_saved_me_so_much_time/)**

...that I now spend that extra time fixing AI mistakes. Don't get me wrong I use AI almost every day, and it's incredibly useful. But I've noticed something funny: Instead of doing the work myself, I now spend my time fact-checking, rewriting, and correcting what AI generated. It still saves time overall, but it's definitely not the "press one button and you're done" future people imagined. What's one task AI actually saves you time on, and one task where it creates more work than it solves?

2m ago

---

**[Anthropic Aletheia Team](https://www.reddit.com/r/artificial/comments/1v0n1z5/anthropic_aletheia_team/)**

Anyone knows what this Aletheia Team is? https://preview.redd.it/g0h19kuty5eh1.png?width=1380&format=png&auto=webp&s=669eff0e5a7cf8d8e60875fe0b785df325ff2c0a

1h ago

---

**[Models to Pair with TypingMind](https://www.reddit.com/r/artificial/comments/1v0hi95/models_to_pair_with_typingmind/)**

Earlier this year, AI was like working with a recent intelligent technical college graduate who was answering questions and making good suggestions I didn’t think of. Recently, it is like I have an HR intern helping me. The AI assistant can’t answer science related questions, doesn’t suggest anything useful, asks chatty questions about what I think despite my instructions, formats wrong despite instructions, and is constantly telling me why I can’t search for or do something that is not even remotely an issue . . . Even practicing my Spanish in terms of lessons plans, not just chatting, is painful now. What less obvious models are you all using today to avoid this problem on your aggregators?

6h ago

---

**[Interactive map of GPT-2's token embedding space - tap any token and explore [P]](https://www.reddit.com/r/artificial/comments/1v0j8kz/interactive_map_of_gpt2s_token_embedding_space/)**

32,070 alphabetic tokens from GPT-2-small's WTE, no forward pass and no context. Works on mobile. Pinch to zoom, tap a token to see its nearest connections, tap a neighbour to walk the graph. Search box to jump anywhere. Layout is t-SNE over a compressed representation of the embedding table; edges are a minimum spanning tree in that space, so every line is a real nearest-kin relationship,

🔗 [aethereos.net](https://aethereos.net/static/token-atlas.html) • 5h ago

---

**[Xi Jinping calls for more open-source AI: 'China is ready to be more open'](https://www.reddit.com/r/artificial/comments/1uzcgiq/xi_jinping_calls_for_more_opensource_ai_china_is/)**

Chinese leader Xi Jinping called for more open-source AI in a speech on Thursday. He encouraged "open-source, openness, collaboration, and sharing."

🔗 [Business Insider](https://www.businessinsider.com/xi-jinping-open-source-ai-us-competition-openai-anthropic-models-2026-7?utm_source=reddit&utm_medium=social&utm_campaign=insider-inthenews-sub-post) • 1d ago

---

**[I cut a RAG pipeline's response time from 90 seconds to 4. Never touched the model](https://www.reddit.com/r/artificial/comments/1uzzcef/i_cut_a_rag_pipelines_response_time_from_90/)**

Last year I worked with an AI startup, an Oxford spinout. Their product answered research questions through a RAG pipeline. It worked, but every query took around 90 seconds. Long enough that users were bailing before the answer even loaded. The obvious move is to blame the model and go bigger. That wasn't it. The retrieval layer was doing way more work than it needed to on every single query: bloated embeddings, no caching, redundant calls stacking up as the document set grew. I stripped that layer down. Response time went from 90 seconds to about 4, and cost dropped roughly 95%, mostly because the pipeline stopped repeating work it never needed to do in the first place. Separately, I also rebuilt the retrieval on Weaviate. That part wasn't about speed, it fixed accuracy issues in what the pipeline was actually retrieving. Same lesson as most AI performance problems I run into: it's rarely the model. It's the layer nobody's looking at.

20h ago

---

**[When I made LLMs argue with each other, they started making up citations to win. Sycophancy wasn't the only failure mode.](https://www.reddit.com/r/artificial/comments/1v05mzz/when_i_made_llms_argue_with_each_other_they/)**

Some context. I've been running setups where a few LLM personas debate a question, then a separate neutral pass pulls out where they actually disagree. The whole reason I started was sycophancy. One model on its own just agrees with whatever you say, so I wanted models that would actually push back on each other. That part worked. But two things happened that I didn't see coming. First, arguing turns models into confident fabricators. Once a model is trying to "win", it starts citing sources, URLs, author names, specific figures, that were never in the retrieved material. It's not random hallucination, it's persuasive hallucination, because in an argument a citation is basically a weapon. I ended up adding a dumb deterministic check that flags any cited URL that isn't in the actual retrieved corpus. Just telling the model "only cite real sources" in the prompt barely did anything, moved it maybe 6 points. Second, if you let a model pick the debaters, the panel comes out unanimous almost every time. Generating all the personas from one model at low temperature quietly lines up their priors. You think you've got a debate, you've actually got one model wearing five hats. The takeaway for me: making models disagree is really easy to fake and pretty hard to do for real. Most of the actual work is in the verification layer, not the personas. Anyone else working on multi-agent debate or adversarial verification? Still an open question for me whether fabrication-under-pressure is just a property of any adversarial LLM setup, or something you can actually design out at the architecture level instead of catching after the fact.

16h ago

---

**[AI Simulation per user](https://www.reddit.com/r/artificial/comments/1v0ennr/ai_simulation_per_user/)**

This environment is all text based. Crafted ads are injected with precision. How far are we from "every user in my feed is a bot" as part of complete ecosystem designed to extract/elicit responses/direct actions. Where each individual user is isolated. No real human to human communication is occurring just simulated communication? It's the death of the internet problem, right?

9h ago

---

---

## Google News: "ai"

**['Dr. Doom' Nouriel Roubini says we're headed for universal basic income or 'some form of socialism' as AI revolutionizes work—He calls that optimistic](https://fortune.com/2026/07/18/nouriel-roubini-universal-basic-income-socialism-ai-revolution-work-agi-government-stakes/)**

"Essentially, the government is going to take over some fraction of the big tech firms."

Fortune • 13h ago

---

**[Green says Mets fully compliant on AI after report of usage](https://www.espn.com/mlb/story/_/id/49392589/green-says-mets-fully-compliant-ai-report-usage)**

ESPN • 17h ago

---

**[Hong Kong can serve as a ‘launch pad’ for AI firms, finance chief Paul Chan says](https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3361110/hong-kong-can-serve-launch-pad-ai-firms-finance-chief-paul-chan-says)**

South China Morning Post • 31m ago

---

**[Could AI be conscious?](https://www.theguardian.com/technology/2026/jul/19/could-ai-be-conscious)**

Experts believe it’s at least possible. We urgently need a plan to navigate the ethical implications

The Guardian • 48m ago

---

**[Opinion | Social Media Hacked Our Attention. A.I. Scares Me More.](https://www.nytimes.com/2026/07/19/opinion/ai-attention-social-media-attachment.html)**

The New York Times • 1h ago

---

**[The biggest winners of the American economy fear they’re sinking fast](https://www.washingtonpost.com/technology/2026/07/19/tech-has-never-been-richer-its-workers-have-never-felt-less-secure/)**

Waves of layoffs and growing pressure to automate jobs are creating existential panic in the tech industry. Economists say other white-collar workers are next.

The Washington Post • 1h ago

---

**[The Secret Mission Behind the U.A.E.’s AI Breakthrough](https://www.wsj.com/articles/the-secret-mission-behind-the-u-a-e-s-ai-breakthrough-bf6f2e09)**

WSJ • 56m ago

---

**[Meet the little-known companies behind America’s data center boom](https://www.nbcnews.com/tech/tech-news/data-center-developer-ai-boom-backlash-who-build-rcna353391)**

AI demand has brought billions in financing to little-known developers, while putting them at the center of fights over electricity, pollution and land.

NBC News • 58m ago

---

**[How AI took the field at the World Cup](https://www.axios.com/2026/07/19/the-world-cups-ai-assist)**

Axios • 2h ago

---

**[Divide grows between AI employees and executives over policy battles](https://thehill.com/policy/technology/5975760-openai-employees-fund-guardrails-alliance/)**

The Hill • 1h ago

---

---

## HackerNews: "ai"

**[Kaiser nurses say AI, surveillance are making their jobs and patient care worse](https://news.ycombinator.com/item?id=48952880)**

⬆️ 551 • 💬 372 • 1d ago • [localnewsmatters.org](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/)

---

**[NYC may require landlords and realtors to disclose the use of AI in listings](https://news.ycombinator.com/item?id=48962983)**

No more AI-edited listings without disclosures.

⬆️ 493 • 💬 212 • 13h ago • [PetaPixel](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)

---

**[The state of open source AI](https://news.ycombinator.com/item?id=48947825)**

⬆️ 479 • 💬 351 • 1d ago • [stateofopensource.ai](https://stateofopensource.ai/)

---

**[Why do AI company logos look like buttholes? (2025)](https://news.ycombinator.com/item?id=48956924)**

A humorous exploration of the uncanny resemblance between AI company logos and human anatomy. Discover why circular, gradient-based designs dominate the AI industry, and what this design convergence tells us about branding in tech.

⬆️ 428 • 💬 143 • 1d ago • [VelvetShark](https://velvetshark.com/ai-company-logos-that-look-like-buttholes)

---

**[What AI did to stackoverflow in a graph](https://news.ycombinator.com/item?id=48956949)**

⬆️ 412 • 💬 505 • 1d ago • [data.stackexchange.com](https://data.stackexchange.com/stackoverflow/query/1953768#graph)

---

**[$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://news.ycombinator.com/item?id=48939524)**

We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.

⬆️ 396 • 💬 528 • 2d ago • [TryAI](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

---

**[LM Studio Bionic: the AI agent for open models](https://news.ycombinator.com/item?id=48939662)**

The AI agent made for open models, built to get things done.

⬆️ 327 • 💬 129 • 2d ago • [LM Studio Blog](https://lmstudio.ai/blog/introducing-lm-studio-bionic)

---

**[AI Mania Is Eviscerating Global Decision-Making](https://news.ycombinator.com/item?id=48964185)**

⬆️ 246 • 💬 92 • 10h ago • [ludic.mataroa.blog](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/#fnref:3)

---

**[FAA lets Boeing sign off on 737 MAX, 787 airworthiness certificates again](https://news.ycombinator.com/item?id=48952439)**

The move is a vote of confidence in Boeing from the U.S. government.

⬆️ 195 • 💬 118 • 1d ago • [CNBC](https://www.cnbc.com/2026/07/17/faa-boeing-737-max-787.html)

---

**[How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM](https://news.ycombinator.com/item?id=48935687)**

⬆️ 164 • 💬 85 • 2d ago • [zhinit.dev](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

---

---

## YouTube Videos: "ai"

**[Open Source AI Is Getting Too Big to Run](https://www.youtube.com/watch?v=qW5UDpHZBPw)**

Two major open-model releases arrived this week from very different directions. Both geographically and conceptually. Kimi K3 is ...

📺 Turing Post TV

👁️ 14K • 👍 541 • 💬 78 • ⏱️ 18:08 • 1d ago

---

**[AI Expert WARNS: Mass Job Loss Is Coming By 2027 - Tristan Harris](https://www.youtube.com/watch?v=GSoqVsdkvNA)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Tristan Harris warns that mass AI ...

📺 Neural Nutshell

👁️ 8K • 👍 210 • 💬 43 • ⏱️ 17:41 • 1d ago

---

**[China&#39;s AI just shocked Wall Street](https://www.youtube.com/watch?v=_fNhzoiZdNI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 127K • 👍 7K • 💬 2K • ⏱️ 14:15 • 22h ago

---

**[Is This the Biggest AI Release of 2026? (China’s New DeepSeek Moment)](https://www.youtube.com/watch?v=V0RsocRqjIU)**

China's Moonshot AI just released Kimi K3, the world's largest open-weight AI model. It rivals leading American systems, ...

📺 AI Revolution

👁️ 45K • 👍 1K • 💬 164 • ⏱️ 14:29 • 1d ago

---

**[Meta’s AI Just Exposed the Whole Sh*tshow](https://www.youtube.com/watch?v=9BArC9Q39MI)**

Meta's AI-powered Ray-Ban glasses could transform everyday life for blind and visually impaired people, translating text, ...

📺 House of El: AI

👁️ 129K • 👍 10K • 💬 2K • ⏱️ 20:09 • 1d ago

---

**[The Real Reason IBM&#39;s AI Panic Wiped Out $67 BILLION](https://www.youtube.com/watch?v=2yqwG9DaI3E)**

Today's FULL PDS here: https://youtu.be/qJTQZj6xUUc?si=W8ELxIzgfQTDMBO_ Tonight's Live Reaction & Lindsay4Georgia ...

📺 DeFranco News Clips

👁️ 323K • 👍 10K • 💬 934 • ⏱️ 7:56 • 2d ago

---

**[China World AI Conference Mocked: No Western Nations Attend, Turns Into A “Beggar’s Fair”](https://www.youtube.com/watch?v=B1ThwmDJmn0)**

On July 17, the Shanghai Pudong World Expo Center hosted a heavily promoted event by Chinese authorities — the 2026 World ...

📺 China Observer

👁️ 19K • 👍 1K • 💬 262 • ⏱️ 16:56 • 11h ago

---

**[AI News: Claude&#39;s New Browser, Spotify Gets AI &amp; OpenAI&#39;s New Hardware](https://www.youtube.com/watch?v=ss2LaCKUQmU)**

Try Seedream 5.0 plus other top AI image and video models at Artlist ...

📺 Matt Wolfe

👁️ 54K • 👍 2K • 💬 90 • ⏱️ 23:10 • 1d ago

---

**[Anthropic CEO: AI Is Not Conscious , It&#39;s Much WORSE Than That - Dario Amodei](https://www.youtube.com/watch?v=2Lt0AtM4JW8)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Anthropic CEO Dario Amodei warns that AI ...

📺 Neural Nutshell

👁️ 46K • 👍 882 • 💬 211 • ⏱️ 20:51 • 2d ago

---

**[What Happens in the Next 3 Years of AI — and How to Be Ready | The Liberman Brothers](https://www.youtube.com/watch?v=HMvTSaaO9sU)**

Today's sponsor is MongoDB. Their Atlas Learning Hub has free, hands-on courses and skill badges — spin up a free cluster and ...

📺 Silicon Valley Girl

👁️ 11K • 👍 297 • 💬 52 • ⏱️ 40:45 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 13,462 • ❤️ 1,098 • 2d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 338,945 • ❤️ 767 • 1d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,262,894 • ❤️ 467 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 536,177 • ❤️ 4,148 • 17d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,118,995 • ❤️ 2,327 • 4d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 407 • 23h ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 10,647 • ❤️ 449 • 8d ago

---

**[OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)**

*ATH-MaaS*

OvisOCR2 is a compact 0.8B multimodal model for end-to-end document parsing, generating Markdown from document images. It excels at extracting text, formulas, tables, and visual regions in natural reading order, achieving state-of-the-art performance on benchmarks like OmniDocBench.

`image-text-to-text` `853.0M`

⬇️ 14,587 • ❤️ 183 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,084,530 • ❤️ 2,881 • 3mo ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 87,533 • ❤️ 269 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 29 • 💬 3 • ⭐ 13,258 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 93,556 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 17 • 💬 2 • ⭐ 20,921 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 44 • 💬 1 • ⭐ 1,299 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,246 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 257 • 💬 4 • ⭐ 13,103 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 9,090 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,052 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 60 • 💬 3 • ⭐ 1,438 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 12 • 💬 0 • ⭐ 9,027 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.0k • 🔱 1.0k • 2d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.0k • 🔱 221 • 8h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.6k • 🔱 365 • 2d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.3k • 🔱 268 • 10d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 991 • 🔱 17 • 11d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 945 • 🔱 59 • 5d ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 900 • 🔱 203 • 8d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 896 • 🔱 143 • 4d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 895 • 🔱 38 • 18d ago

---

**[ai4s-research/open-science](https://github.com/ai4s-research/open-science)**

Open Science Desktop — local-first, model-agnostic AI research workbench for macOS, Windows & Linux. Open-source Claude Science desktop alternative built on Tauri + MCP + agent skills.

`TypeScript` `ai-agent` `ai-for-science` `ai-scientist` `ai4s` `claude-science`

⭐ 831 • 🔱 96 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
