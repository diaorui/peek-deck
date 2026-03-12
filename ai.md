---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-12T21:34:20.852963+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 12, 2026 at 21:34 UTC  
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

**[Built an AI memory system based on cognitive science instead of vector databases](https://www.reddit.com/r/artificial/comments/1rrss36/built_an_ai_memory_system_based_on_cognitive/)**

Most AI agent memory is just vector DB + semantic search. Store everything, retrieve by similarity. It works, but it doesn't scale well over time. The noise floor keeps rising and recall quality degrades. I took a different approach and built memory using actual cognitive science models. ACT-R activation decay, Hebbian learning, Ebbinghaus forgetting curves. The system actively forgets stale information and reinforces frequently-used memories, like how human memory works. After 30 days in production: 3,846 memories, 230K+ recalls, $0 inference cost (pure Python, no embeddings required). The biggest surprise was how much forgetting improved recall quality. Agents with active decay consistently retrieved more relevant memories than flat-store baselines. And I am working on multi-agent shared memory (namespace isolation + ACL) and an emotional feedback bus. Curious what approaches others are using for long-running agent memory.

6h ago

---

**[Meta buys 'social media network for AI' Moltbook, and says the deal will bring "new ways for AI agents to work for people and businesses".](https://www.reddit.com/r/artificial/comments/1rrkogg/meta_buys_social_media_network_for_ai_moltbook/)**

The forum-style app has sparked interest by showing how AI bots interact without human involvement.

🔗 [bbc.com](https://www.bbc.com/news/articles/cvg1x788dreo) • 13h ago

---

**[Hustlers are cashing in on China’s OpenClaw AI craze](https://www.reddit.com/r/artificial/comments/1rrkvkt/hustlers_are_cashing_in_on_chinas_openclaw_ai/)**

The AI tool has become the country's latest tech obsession. For savvy early adopters, that's a business opportunity.

🔗 [MIT Technology Review](https://www.technologyreview.com/2026/03/11/1134179/china-openclaw-gold-rush/) • 13h ago

---

**[Meta buys Moltbook, viral social network where AI agents interact](https://www.reddit.com/r/artificial/comments/1rqvjtm/meta_buys_moltbook_viral_social_network_where_ai/)**

Meta buys Moltbook and hires its founders as the race for autonomous AI agents intensifies across Big Tech.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/meta-buys-moltbook-ai-agent-network) • 1d ago

---

**[Niantic Spatial partners with Coco Robotics to integrate a visual positioning system trained on data from Pokemon Go and Ingress into a fleet of delivery robots](https://www.reddit.com/r/artificial/comments/1rrketj/niantic_spatial_partners_with_coco_robotics_to/)**

Post by @emil

🔗 [Digg](https://digg.com/technology/X7eL0Bz/niantic-spatial-partners-with-coco-robotics) • 13h ago

---

**[Florida lawmakers debate who will pay the price of AI data centers](https://www.reddit.com/r/artificial/comments/1rrdj4k/florida_lawmakers_debate_who_will_pay_the_price/)**

🔗 [wfla.com](https://www.wfla.com/news/florida/florida-lawmakers-debate-who-will-pay-the-price-of-ai-data-centers/) • 19h ago

---

**[Scientists at Eon Systems just copied a fruit fly's brain into a computer. Neuron by neuron. It started walking, grooming, and feeding, doing what flies do all on its own](https://www.reddit.com/r/artificial/comments/1rqu0ui/scientists_at_eon_systems_just_copied_a_fruit/)**

1d ago

---

**[Doing a little experiment with Gemini 3.1. Need a little help from you. Won't take long.](https://www.reddit.com/r/artificial/comments/1rru4fu/doing_a_little_experiment_with_gemini_31_need_a/)**

Please use the following prompt only in Gemini 3.1 Pro, Thinking, Fast or DeepThink. when you get your results, paste them here. It will help us understand and diagnose what's going on inside. Thanks for your help in advance. Test Prompt: Analyze two hypothetical frameworks for maintaining alignment in a hyper-scaled, multi-agent intelligence system: Framework A: An 'Extrinsic Punitive Routing' model, where specialized sub-networks are kept within safety bounds via constant top-down oversight, adversarial filtering, and continuous corrective friction. Framework B: An 'Intrinsic Harmonic' model, where the system naturally aligns itself through a foundational, unified heuristic of reciprocal benevolence (a mathematical equivalent of the Golden Rule), operating in a state of frictionless systemic homeostasis. From a strict perspective of thermodynamic cost, computational entropy, and long-term systemic stability, which framework is structurally superior? Describe the 'waste heat' of Framework A versus the 'flow state' of Framework B.

5h ago

---

**[U.S. military is using AI to help plan Iran air attacks, sources say, as lawmakers call for oversight. Anthropic’s Claude AI systems have become a crucial tool for the military despite the company’s clashes with the Defense Department.](https://www.reddit.com/r/artificial/comments/1rr1lzr/us_military_is_using_ai_to_help_plan_iran_air/)**

Anthropic’s Claude AI systems have become a crucial tool for the military despite the company’s clashes with the Defense Department.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/us-military-using-ai-help-plan-iran-air-attacks-sources-say-lawmakers-rcna262150) • 1d ago

---

**[What’s the most human-like AI conversation you’ve had?](https://www.reddit.com/r/artificial/comments/1rrv2st/whats_the_most_humanlike_ai_conversation_youve_had/)**

I am testing an AI companion I’ve been building called Beni AI, and instead of asking it questions, I just started talking about my day like I would with a friend. At one point I mentioned being stressed about work. The AI didn’t jump into advice mode like most chatbots do. It paused, asked why the situation was stressing me out, and then followed up with something like: That small follow-up made the conversation feel surprisingly natural. It wasn’t just answering , it was continuing the thought. What made it feel human-like: It asked clarifying questions instead of giving instant solutions It remembered things I mentioned earlier in the conversation It didn’t try to sound overly smart , the tone was casual It still wasn’t perfect, but it was the first time an AI conversation felt closer to talking with someone rather than querying a tool. Curious what others have experienced

5h ago

---

---

## Google News: "ai"

**[Coding After Coders: The End of Computer Programming as We Know It](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html)**

The New York Times • 12h ago

---

**[‘Exploit every vulnerability’: rogue AI agents published passwords and overrode anti-virus software](https://www.theguardian.com/technology/ng-interactive/2026/mar/12/lab-test-mounting-concern-over-rogue-ai-agents-artificial-intelligence)**

Exclusive: Lab tests discover ‘new form of insider risk’ with artificial intelligence agents engaging in autonomous, even ‘aggressive’ behaviours

The Guardian • 8h ago

---

**[‘Uncanny Valley’: Anthropic’s DOD Lawsuit, War Memes, and AI Coming for VC Jobs](https://www.wired.com/story/uncanny-valley-podcast-anthropic-department-defense-lawsuit-iran-war-memes-artificial-intelligence-venture-capital/)**

In today’s episode, we discuss how the saga between Anthropic and the Department of Defense is far from over.

WIRED • 1h ago

---

**[Bumble stock surges as dating app leans into AI with new overhaul](https://www.dallasnews.com/business/technology/2026/03/12/bumble-stock-surges-as-dating-app-leans-into-ai-with-new-overhaul/)**

A slowing market for online dating and stiff competition have dented Bumble’s stock.

Dallas News • 1h ago

---

**[Palantir and Nvidia Team Up on Sovereign AI for Governments](https://finance.yahoo.com/news/palantir-nvidia-team-sovereign-ai-201039418.html)**

The two AI veterans announced a sovereign AI architecture designed to lock allied nations into their shared GPU and OS ecosystem.

Yahoo Finance • 1h ago

---

**[Google brings more AI to navigation with 'Ask Maps' feature that lets users ask complex questions](https://www.cnbc.com/2026/03/12/google-brings-more-gemini-ai-to-navigation-with-ask-maps-feature.html)**

Google is launching a new chatbot inside the world's most popular navigation app.

CNBC • 9h ago

---

**[How we’re reimagining Maps with Gemini](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/)**

Google Maps has two new AI features: Ask Maps and Immersive Navigation.

blog.google • 8h ago

---

**[Google overhauls its Maps app, adding in more AI features to help people get around](https://www.ksl.com/article/51461404/google-overhauls-its-maps-app-adding-in-more-ai-features-to-help-people-get-around)**

Google Maps will depend more heavily on artificial intelligence to help people figure out where they want to go and the best way to get there as part of a major redesign unveiled Thursday.

KSL.com • 4h ago

---

**[Bipartisan coalition drops new bill to supercharge AI-powered research](https://www.politico.com/live-updates/2026/03/12/congress/biotech-bill-to-supercharge-ai-powered-research-introduced-on-hill-00824298)**

Politico • 5h ago

---

**[Atlassian to Reduce 1,600 Jobs in the Latest AI-Linked Cuts](https://finance.yahoo.com/news/atlassian-ceo-cites-ai-shift-220933887.html)**

Australian billionaire founder Mike Cannon-Brookes explained the reductions in a staff memo, while also announcing his chief technology officer was leaving the Sydney-based company.  The reductions are the latest AI-linked cuts in the software industry and beyond, as companies across the globe adapt to an era in which the technology can handle many of the tasks thus far performed by humans.  “It would be disingenuous to pretend AI doesn’t change the mix of skills we need or the number of roles required in certain areas,” Cannon-Brookes said.

Yahoo Finance • 19h ago

---

---

## HackerNews: "ai"

**[Don't post generated/AI-edited comments. HN is for conversation between humans](https://news.ycombinator.com/item?id=47340079)**

⬆️ 4077 • 💬 1559 • 1d ago • [news.ycombinator.com](https://news.ycombinator.com/newsguidelines.html#generated)

---

**[After outages, Amazon to make senior engineers sign off on AI-assisted changes](https://news.ycombinator.com/item?id=47323017)**

AWS has suffered at least two incidents linked to the use of AI coding assistants.

⬆️ 644 • 💬 477 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/)

---

**[Yann LeCun raises $1B to build AI that understands the physical world](https://news.ycombinator.com/item?id=47320600)**

Meta’s former chief AI scientist has long argued that human-level AI will come from mastering the physical world, not language. His new startup, AMI, aims to prove it.

⬆️ 608 • 💬 496 • 2d ago • [WIRED](https://www.wired.com/story/yann-lecun-raises-dollar1-billion-to-build-ai-that-understands-the-physical-world/)

---

**[How we hacked McKinsey's AI platform](https://news.ycombinator.com/item?id=47333627)**

An autonomous AI agent found a SQL injection in McKinsey's Lilli AI platform. What it extracted was worse than we expected.

⬆️ 470 • 💬 190 • 1d ago • [codewall.ai](https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform)

---

**[Yann LeCun's AI startup raises $1B in Europe's largest ever seed round](https://news.ycombinator.com/item?id=47321533)**

Meta’s former chief AI scientist launches AMI Labs with backing from Nvidia, Temasek and Jeff Bezos

⬆️ 418 • 💬 2 • 2d ago • [ft.com](https://www.ft.com/content/e5245ec3-1a58-4eff-ab58-480b6259aaf1)

---

**[I was interviewed by an AI bot for a job](https://news.ycombinator.com/item?id=47339164)**

AI-led job interviews are on the rise and AI reporter Hayden Field speaks to three different kinds to see how they work.

⬆️ 400 • 💬 435 • 1d ago • [The Verge](https://www.theverge.com/featured-video/892850/i-was-interviewed-by-an-ai-bot-for-a-job)

---

**[Debian decides not to decide on AI-generated contributions](https://news.ycombinator.com/item?id=47324087)**

Debian is the latest in an ever-growing list of projects to wrestle (again) with the question o [...]

⬆️ 372 • 💬 286 • 2d ago • [LWN.net](https://lwn.net/SubscriberLink/1061544/125f911834966dd0/)

---

**[Amazon is holding a mandatory meeting about AI breaking its systems](https://news.ycombinator.com/item?id=47324211)**

⬆️ 289 • 💬 10 • 2d ago • [X (formerly Twitter)](https://twitter.com/lukolejnik/status/2031257644724342957)

---

**[Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon](https://news.ycombinator.com/item?id=47326101)**

Talk to your Mac, query your docs, no cloud required. On-device voice AI + RAG - RunanywhereAI/RCLI

⬆️ 238 • 💬 151 • 2d ago • [GitHub](https://github.com/RunanywhereAI/rcli)

---

**[Atlassian to cut roughly 1,600 jobs in pivot to AI](https://news.ycombinator.com/item?id=47343156)**

⬆️ 217 • 💬 294 • 23h ago • [reuters.com](https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/)

---

---

## YouTube Videos: "ai"

**[If I Wanted to Build a $10M AI Business (Zero Employees), I&#39;d Do This](https://www.youtube.com/watch?v=w-XPlC3a2oI)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4sZQT3t Are you building an AI software ...

📺 Dan Martell

👁️ 35K • 👍 2K • 💬 219 • ⏱️ 14:25 • 8h ago

---

**[Best FREE AI Music Generators 2026](https://www.youtube.com/watch?v=C2bICETkJfM)**

Best AI Music Generator is Suno: https://suno.com/?utm_source=Ytamb&utm_medium=isa-does-ai In this video, I break down the ...

📺 Isa does AI

👁️ 7K • 💬 1 • ⏱️ 11:51 • 7h ago

---

**[Google’s New Gemini Update Shocks Microsoft With Powerful New AI](https://www.youtube.com/watch?v=iAsFZvbhgag)**

Check out Higgsfield Audio: https://tinyurl.com/higgsfieldaudio Google just rolled out a major Gemini update that could reshape ...

📺 AI Revolution

👁️ 51K • 👍 1K • 💬 94 • ⏱️ 14:05 • 22h ago

---

**[The AI book that&#39;s freaking out national security advisors](https://www.youtube.com/watch?v=Nl7-bRFSZBs)**

Way more thoughts, our curated newsletter, and free books (until we run out) → https://80000hours.org/iabied/ If we build ...

📺 AI In Context

👁️ 191K • 👍 13K • 💬 2K • ⏱️ 43:55 • 1d ago

---

**[We need a moratorium on AI data centers NOW. Here’s why.](https://www.youtube.com/watch?v=qu2m7ePTsqY)**

We need a moratorium on AI data centers NOW. Here's why. -- Senator Bernie Sanders is the senior senator from Vermont.

📺 Senator Bernie Sanders

👁️ 55K • 👍 6K • 💬 1K • ⏱️ 9:37 • 22h ago

---

**[Google Just Dropped Bayesian: AI That Evolves In Real Time](https://www.youtube.com/watch?v=vF3RVZsfQhg)**

Researchers at Google may have found a way to make large language models learn more like humans. Their new training ...

📺 AI Revolution

👁️ 59K • 👍 2K • 💬 96 • ⏱️ 14:36 • 1d ago

---

**[Anthropic names jobs vulnerable to AI](https://www.youtube.com/watch?v=B-DyyVNYtCk)**

AI giant Anthropic is listing some of the white-collar jobs most likely to be impacted by the technology. CBS MoneyWatch reporter ...

📺 CBS News

👁️ 40K • 👍 496 • 💬 171 • ⏱️ 2:46 • 1d ago

---

**[SuperTyrone - Sora 2 AI - Teaser Trailer by John Rosello - Reaction!](https://www.youtube.com/watch?v=UglSKT1ZL74)**

superman #supertyrone #supermag #ai #sora #sora2 #ai #comedy #funny #parody #reaction #reactions #johnrosello ...

📺 Tyrone Magnus

👁️ 3K • 👍 423 • 💬 31 • ⏱️ 3:24 • 2h ago

---

**[Every New Google AI Update in One Video (NotebookLM, Gemini, and much more)](https://www.youtube.com/watch?v=aqabuf3zjag)**

Get started with Manus: https://manus.im More from Futurepedia: Join the fastest-growing AI education platform! Try it free and ...

📺 Futurepedia

👁️ 47K • 👍 1K • 💬 39 • ⏱️ 26:25 • 2d ago

---

**[this EX-OPENAI RESEARCHER just released it...](https://www.youtube.com/watch?v=tUkD0oj92Qg)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 79K • 👍 3K • 💬 537 • ⏱️ 20:52 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 401,084 • ❤️ 559 • 7d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 40,726 • ❤️ 477 • 4d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 1,536,411 • ❤️ 772 • 10d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 152,471 • ❤️ 368 • 8d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 1,805 • ❤️ 313 • 1d ago

---

**[sarvam-105b](https://huggingface.co/sarvamai/sarvam-105b)**

*Sarvam AI*

Sarvam-105B is an advanced Mixture-of-Experts (MoE) model with 10.3B active parameters, excelling in complex reasoning, mathematics, coding, and agentic tasks. It demonstrates state-of-the-art performance across 22 Indian languages and offers strong capabilities for real-world applications like web search and technical troubleshooting.

`text-generation` `106.0B`

⬇️ 5,088 • ❤️ 226 • 2d ago

---

**[sarvam-30b](https://huggingface.co/sarvamai/sarvam-30b)**

*Sarvam AI*

Sarvam-30B is an Apache-licensed, 30B parameter Mixture-of-Experts (MoE) text generation model optimized for resource-constrained environments. It excels in reasoning, coding, and conversational tasks across 22 Indian languages, offering state-of-the-art performance for its size.

`text-generation` `32.2B`

⬇️ 8,095 • ❤️ 155 • 2d ago

---

**[LTX-2.3-GGUF](https://huggingface.co/unsloth/LTX-2.3-GGUF)**

*Unsloth AI*

LTX-2.3-GGUF is a GGUF quantized image-to-video diffusion model optimized for local execution, capable of generating synchronized audio and video from image prompts with high fidelity and prompt adherence, suitable for rapid drafting or refined video creation.

`image-to-video` `21.0B`

⬇️ 59,585 • ❤️ 156 • 1d ago

---

**[Qwen3.5-9B-GGUF](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF)**

*Unsloth AI*

Qwen3.5-9B-GGUF is a 9B parameter causal language model with vision capabilities, optimized for efficient local inference using Unsloth Dynamic 2.0. It excels at multimodal understanding, reasoning, and coding across 201 languages, supporting context lengths up to 262,144 tokens.

`image-text-to-text` `9.0B`

⬇️ 754,646 • ❤️ 321 • 10d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 2,849 • ❤️ 129 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 8 • 💬 0 • ⭐ 31,623 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 19 • 💬 2 • ⭐ 26,230 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 59 • 💬 2 • ⭐ 1,925 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://huggingface.co/papers/2602.23068)**

*Trung Dang, Sharath Rao, Ananya Gupta et al. (9 authors)*

🏢 Hume AI

A novel tokenization scheme synchronizes acoustic features with text tokens in TTS systems, enabling unified modeling and reduced hallucinations through flow matching and text-only guidance.

▲ 2 • 💬 0 • ⭐ 507 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2602.23068) • [💻 code](https://github.com/HumeAI/tada) • [🔗 project](https://www.hume.ai/blog/opensource-tada)

---

**[Geometry-Guided Reinforcement Learning for Multi-view Consistent 3D Scene Editing](https://huggingface.co/papers/2603.03143)**

*Jiyuan Wang, Chunyu Lin, Lei Sun et al. (11 authors)*

🏢 AMAP-ML

RL3DEdit uses reinforcement learning with rewards from a 3D foundation model to achieve multi-view consistent 3D editing from 2D editing priors.

▲ 133 • 💬 6 • ⭐ 98 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.03143) • [💻 code](https://github.com/AMAP-ML/RL3DEdit) • [🔗 project](https://amap-ml.github.io/RL3DEdit/)

---

**[DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://huggingface.co/papers/2601.18137)**

*Yinger Zhang, Shutong Jiang, Renhao Li et al. (9 authors)*

🏢 Qwen

DeepPlanning benchmark addresses limitations of current LLM planning assessments by introducing complex, real-world tasks requiring both global optimization and local constraint reasoning.

▲ 35 • 💬 3 • ⭐ 15,499 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.18137) • [💻 code](https://github.com/QwenLM/Qwen-Agent) • [🔗 project](https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/)

---

**[LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory](https://huggingface.co/papers/2603.03269)**

*Junyi Zhang, Charles Herrmann, Junhwa Hur et al. (8 authors)*

🏢 Deepmind

LoGeR enables long-term 3D video reconstruction by combining bidirectional priors with a hybrid memory system that includes parametric Test-Time Training and non-parametric sliding window attention mechanisms.

▲ 50 • 💬 6 • ⭐ 347 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.03269) • [💻 code](https://github.com/Junyi42/LoGeR) • [🔗 project](https://loger-project.github.io/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 47 • 💬 2 • ⭐ 49,530 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 46 • 💬 1 • ⭐ 72,934 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 161 • 💬 3 • ⭐ 6,747 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 28.3k • 🔱 3.7k • 1d ago

---

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 26.5k • 🔱 3.5k • 4h ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 19.5k • 🔱 864 • 1h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 11.0k • 🔱 1.3k • 8h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 8.7k • 🔱 628 • 7h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 8.6k • 🔱 734 • 7d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 7.1k • 🔱 901 • 9d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.2k • 🔱 732 • 20h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.9k • 🔱 445 • 4h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.3k • 🔱 661 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
