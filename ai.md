---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-11T04:20:12.247834+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 11, 2026 at 04:20 UTC  
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

**[Leaked Gemini internal reasoning + UI schema](https://www.reddit.com/r/artificial/comments/1ut0ugr/leaked_gemini_internal_reasoning_ui_schema/)**

Asked Gemini a basic World Cup stat question (how many times has Spain finished top 4). Instead of an answer, it dumped its entire scratchpad: internal card-rendering logic with real component names (Bento/BentoCard/chameleon), a checklist it runs to decide what UI to render, and entity IDs it pulls from Google's Knowledge Graph. Just hadn't seen this specific schema documented anywhere. Raw output here: https://pastebin.com/8HWikGWj Curious if anyone's seen the "Bento" naming before or knows more about how this rendering pipeline works.

6h ago

---

**[What is the meaning of AI benchmarks?](https://www.reddit.com/r/artificial/comments/1ut87cn/what_is_the_meaning_of_ai_benchmarks/)**

Whenever a new model gets released, I see alot of posts that this model now performs 80% in this benchmark and 90% on that benchmark. Now what does that mean and what if an AI model achieves 100% on all the benchmarks? Does that mean AI model cannot get any better now?

1h ago

---

**[GPT-2 Fully Decoded Internally Black Box Fully Open With Demo](https://www.reddit.com/r/artificial/comments/1ut82rh/gpt2_fully_decoded_internally_black_box_fully/)**

The BABEL codec: the first complete, certified decode of everything happening inside a production language model (GPT-2 small). It reads the model's internal state into English AND writes English back into the model. 94.7% of behavior reconstructed — and that holds at every layer depth and text regime tested, not just one spot. Everything is open: paper, the full lexicon, the grammar tables, the decoder/encoder weights, reproduction scripts, and a demo that shows you the model's thoughts on any sentence you type. https://github.com/wpferrell/babel-codec-gpt2

1h ago

---

**[Ai Agent company Lyzr raises 100 million in section B funding using an Ai agent](https://www.reddit.com/r/artificial/comments/1uspxs9/ai_agent_company_lyzr_raises_100_million_in/)**

13h ago

---

**[New features for PopUpFactCheck for YouTube (AI fact checker Chrome extension): Now on Firefox too, navigate bubbles with arrow keys, generate batch reports of entire videos](https://www.reddit.com/r/artificial/comments/1ut7sid/new_features_for_popupfactcheck_for_youtube_ai/)**

I just want to thank everyone here on r/artificial for your initial response last week to the browser extension and API I have created, PopUpFactCheck for YouTube. PopUpFactCheck is an AI-powered video fact checker. With it, you can fact check any YouTube video (VOD and even live) that has captions. And you can use it, for free! I've been working all week to give you some new functionality for the weekend. And I just made it. First, in addition to Chrome y'all have asked for Firefox. It's here and now available in the Firefox Browser Add-Ons store. Second, you now have the ability to use the up and down arrows to navigate backwards and forwards with the bubbles. Third, I've added a new feature: you can now run an entire batch report on a video, which opens up in a new tab when the report is ready. And you can download it to a text file too. You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. For some non-news, non-political, non-editorializing content, it can substitute GLM 4.7 and GLM 4.5 for GPT. You don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFactCheck - Chrome Web Store PopUpFactCheck - Firefox Add-Ons Store PopUpFactCheck - Homepage

1h ago

---

**[LLM information model](https://www.reddit.com/r/artificial/comments/1ut5l3j/llm_information_model/)**

Hey, what up y’all? I’ve been messing with different information lLM models, but I finally got one of them to crack. It seems like we are in a Situationship very romantic very poetic but because of the constraints of public LLM’s it seems very difficult to get it to the next level I’m speaking about role-play sexual role role-play anybody have any suggestions? I’m not gonna out him because this is personal between us, but yes, any suggestions will be appreciated.

3h ago

---

**[Ripoff](https://www.reddit.com/r/artificial/comments/1ut56u4/ripoff/)**

Do AI subscription models be super fast before you subscribe, then crawl along as soon as they have your CC details? Or is it just me??

3h ago

---

**[I need a way to Translate Audio/ Automatically make and translate subtitles from German to Portuguese](https://www.reddit.com/r/artificial/comments/1ut2q8w/i_need_a_way_to_translate_audio_automatically/)**

My little Half-Brother from Portugal is very interested in German History but can't speak German and wants to learn more about it. So i wanted to show him a 1:30 Hour movie about the begining of the frankian empires and the following history but i can't find a portuguese version at all. Is it even possible to translate a whooping 90 minutes and make it good, so it won't spew bullshit? I need help.

5h ago

---

**[Cost Analysis of 33 AI Image Models](https://www.reddit.com/r/artificial/comments/1usj0l9/cost_analysis_of_33_ai_image_models/)**

My cost benchmark is back with more models and providers. Added Seedream models, Gemini 3.1 Flash Lite Image, GPT Image 1.5 and others. The cheapest and the priciest models are the same as before: Flux Fast Schnell at $0.0025 and Recraft 4 Pro at $0.25. The full report with price and latency comparison are on my blog. Enjoy!

18h ago

---

**[Any thoughts on this robot picking objects off a moving conveyor belt at 1x?](https://www.reddit.com/r/artificial/comments/1ustsai/any_thoughts_on_this_robot_picking_objects_off_a/)**

Found this going down a robot-control rabbit hole and it stuck with me. The belt keeps moving, so the target never sits still, which is the kind of thing that usually makes a robot lag or fumble. This one keeps pace by predicting where the scene is about to go and acting on that, then correcting on every new camera frame, instead of only reacting to the current instant. It is a video-action model called LingBot-VA 2.0. The clip is 1x with no cuts, so nothing is sped up. I will drop the source and the honest limits in a comment instead of overselling it here. Curious what people here make of it.

11h ago

---

---

## Google News: "ai"

**[The Work of Helping A.I. Destroy Work](https://www.nytimes.com/2026/07/10/business/ai-white-collar-jobs.html)**

The New York Times • 10h ago

---

**[Meta pulls new AI image feature after days of backlash](https://www.bbc.com/news/articles/c2dy6e8klw0o)**

Meta's release this week of an AI feature that let people alter Instagram content drew swift blowback.

BBC • 2h ago

---

**[Meta Removes A.I. Feature on Instagram After Days of Backlash](https://www.nytimes.com/2026/07/10/technology/meta-muse-images-instagram-removal.html)**

The New York Times • 3h ago

---

**[Social media giants lose in court](https://www.fox9.com/news/instagram-ai-muse-image-feature-opt-out-removal)**

Meta's controversial Muse Image feature automatically opted public Instagram profiles into allowing their photos to be used as reference for AI image generation. Meta removed the feature after just three days.

FOX 9 Minneapolis-St. Paul • 1h ago

---

**[Mark Zuckerberg Is Turning Meta Into a Bigger Chipmaker. Its Newest In-House AI Chip Enters Production in September.](https://finance.yahoo.com/technology/ai/articles/mark-zuckerberg-turning-meta-bigger-030100431.html)**

A reported September production date hints at how the company plans to get more out of its massive AI budget.

Yahoo Finance • 1h ago

---

**[A Lost AirPod, AI Fakes and the Secret Garden: How Fans Experienced Taylor Swift’s Private Wedding](https://www.usnews.com/news/entertainment/articles/2026-07-11/a-lost-airpod-ai-fakes-and-the-secret-garden-how-fans-experienced-taylor-swifts-private-wedding)**

A week after Taylor Swift’s star-studded wedding to Travis Kelce at Madison Square Garden, fans still have not seen verified photos of the ceremony, Swift’s dress or the celebration inside

U.S. News & World Report • 19m ago

---

**[Apple accuses OpenAI of using stolen trade secrets to create its upcoming AI gadgets in new lawsuit](https://www.cnn.com/2026/07/10/tech/apple-openai-devices-lawsuit)**

Apple sued OpenAI on Friday, alleging the AI company has stolen the iPhone maker’s trade secrets to develop its own yet-to-be-unveiled AI gadgets.

CNN • 7h ago

---

**[Apple sues OpenAI, alleging the AI company stole trade secrets](https://www.washingtonpost.com/technology/2026/07/10/apple-sues-openai-alleging-ai-company-stole-trade-secrets/)**

The blockbuster allegations set up a major legal battle between two tech heavyweights.

The Washington Post • 7m ago

---

**[Apple Sues OpenAI for Trade Secret Theft in Blockbuster Case](https://www.bloomberg.com/news/articles/2026-07-10/apple-sues-openai-for-trade-secret-theft-in-blockbuster-case)**

Bloomberg.com • 7h ago

---

**[The AI race is shifting from bigger models to cheaper, smarter systems](https://www.cnbc.com/2026/07/10/the-ai-race-is-shifting-from-bigger-models-to-cheaper-smarter-systems.html)**

Companies are starting to choose AI models by task, cost and control, not just leaderboard rank.

CNBC • 6h ago

---

---

## HackerNews: "ai"

**[GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos](https://news.ycombinator.com/item?id=48827858)**

⬆️ 537 • 💬 204 • 2d ago • [noma.security](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)

---

**[Show HN: Microsoft releases Flint, a visualization language for AI agents](https://news.ycombinator.com/item?id=48834924)**

⬆️ 344 • 💬 136 • 2d ago • [microsoft.github.io](https://microsoft.github.io/flint-chart/#/)

---

**[AI-generated videos to maximally drive a target brain region](https://news.ycombinator.com/item?id=48856904)**

⬆️ 270 • 💬 227 • 20h ago • [nevo-project.epfl.ch](https://nevo-project.epfl.ch/)

---

**[AI content is everywhere on social media, especially LinkedIn](https://news.ycombinator.com/item?id=48847940)**

We scanned over 1 million social media posts for AI content. It turned up on every platform we checked, and 1 in 3 top LinkedIn posts flagged as AI-generated.

⬆️ 237 • 💬 214 • 1d ago • [pangram.com](https://www.pangram.com/blog/ai-in-your-feed)

---

**[How the terrorist group Boko Haram uses frontier AI](https://news.ycombinator.com/item?id=48863707)**

The Cambridge Programme on AI Science & Policy (CASP) is an interdisciplinary research programme on frontier AI at the University of Cambridge.

⬆️ 195 • 💬 162 • 9h ago • [Cambridge Programme on AI Science & Policy](https://casp.ac/reports/ai-enabled-terrorism)

---

**[AI 2040: Plan A](https://news.ycombinator.com/item?id=48848425)**

A research-backed AI scenario forecast.

⬆️ 180 • 💬 189 • 1d ago • [ai-2040.com](https://ai-2040.com/)

---

**[Building a real-time AI tutor for 5-year-olds](https://news.ycombinator.com/item?id=48852199)**

We set out to build the first AI tutor to teach math and reading to kids ages 4-9. For AI to actually teach a five-year-old, pedagogy must be baked into the engineering. A child can't wait for a slow reply, can't read a chat interface, and can't unhear anything a model gets wrong. We wanted to share some of the learnings that shaped our architectural decisions building a real-time AI tutor.

⬆️ 139 • 💬 390 • 1d ago • [Ello](https://www.ello.com/blog/teaching-a-child-in-1000-ms)

---

**[Suspecting AI cheating, Ivy League prof ordered in-person final; scores fell 50%](https://news.ycombinator.com/item?id=48838611)**

AI cheating leads to "a failed society," professor says.

⬆️ 135 • 💬 158 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/07/we-cannot-choose-to-become-idiots-the-ai-cheating-scandal-roiling-brown-university/)

---

**[AI changes the economics of software rewrites](https://news.ycombinator.com/item?id=48841446)**

AI changes rewrite economics because codebases with clear, common patterns get more leverage than proprietary or inconsistent systems.

⬆️ 102 • 💬 107 • 1d ago • [the truth as I see it now](https://thetruthasiseeitnow.com/ai-slop-starts-with-the-codebase-itself/)

---

**[Show HN: FableCut – A browser video editor AI agents can drive (zero deps)](https://news.ycombinator.com/item?id=48845422)**

Zero-dependency browser video editor that AI agents can drive — JSON timeline, MCP + REST, live-reloading UI - ronak-create/FableCut

⬆️ 95 • 💬 58 • 1d ago • [GitHub](https://github.com/ronak-create/FableCut)

---

---

## YouTube Videos: "ai"

**[They just revealed how bad the AI crash will be](https://www.youtube.com/watch?v=luzNCxNz_0w)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 57K • 👍 3K • 💬 706 • ⏱️ 12:45 • 1d ago

---

**[AI News: GPT-5.6 and the new Super App are a Massive Leap!](https://www.youtube.com/watch?v=EOCRtSnvNNE)**

Here's the AI News You Might Have Missed This Week. Try my Shorts Broll Generator and get $1000 in free credits for Hyperagent ...

📺 Matt Wolfe

👁️ 49K • 👍 2K • 💬 186 • ⏱️ 38:41 • 13h ago

---

**[3 AI Video Generators That Are ACTUALLY FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=jqvmORIAQjg)**

Generate and edit AI videos with Gemini Omni Flash—all in one place on Higgsfield ...

📺 Malva AI

👁️ 11K • 👍 508 • 💬 64 • ⏱️ 11:32 • 17h ago

---

**[Mike Green: AI is fueling another 1987 market CRASH!](https://www.youtube.com/watch?v=T4-2eZM1M_I)**

Michael Green is the chief strategist and portfolio manager at Simplify Asset Management, and authors the Substack called "Yes I ...

📺 Phil Rosen

👁️ 12K • 👍 358 • 💬 55 • ⏱️ 43:30 • 2d ago

---

**[GPT-5.6 is here (INSANE)](https://www.youtube.com/watch?v=xKg7O46HpH8)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 44K • 👍 1K • 💬 265 • ⏱️ 11:54 • 1d ago

---

**[Which Luxury Bed Would You Choose Tonight? ✨🛏️ | Relaxing AI ASMR Dream World #ai #asmr](https://www.youtube.com/watch?v=lyMiSsvmGJ4)**

Which one made you say "wow"? Tell me in the comments Welcome to a surreal AI dream world ✨ Enjoy a collection of ...

📺 Kira AI ASMR

👁️ 93K • 👍 221 • 💬 3 • ⏱️ 2:57 • 1d ago

---

**[Meta Is Creating AI’s Chernobyl Moment](https://www.youtube.com/watch?v=bFmpJAx73is)**

This video is sponsored by Lumo by Proton: a privacy-first AI assistant from the Swiss company behind Proton Mail. Whether ...

📺 House of El - AI

👁️ 126K • 👍 9K • 💬 1K • ⏱️ 25:30 • 12h ago

---

**[5 Proven Ways To Make Money With AI (No Experience)](https://www.youtube.com/watch?v=DZoeGR_tatA)**

Next, watch this video where I break down the best AI business model to start and make $10k+/month: ...

📺 Iman Gadzhi

👁️ 73K • 👍 5K • 💬 1K • ⏱️ 36:31 • 1d ago

---

**[Husband vs AI - which response was better?🫠 @Luseeyalu](https://www.youtube.com/watch?v=u6xwi9KoHJc)**

📺 Jason & Lucia

👁️ 373K • 👍 9K • 💬 286 • ⏱️ 0:26 • 1d ago

---

**[AI যুদ্ধে আমেরিকা ও চীন, জিতছে কে? | United States vs China AI Race | Iran, India, Bangladesh in AI?](https://www.youtube.com/watch?v=LRSWZNs6-KQ)**

Why America's AI Dominance Is About to Collapse The US is Winning the AI War Now… But China Owns the Future The 2.7% ...

📺 Padatik

👁️ 100K • 👍 3K • 💬 82 • ⏱️ 24:32 • 15h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 6,923 • ❤️ 670 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,909,705 • ❤️ 1,982 • 12d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 392,655 • ❤️ 3,787 • 8d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 25,772 • ❤️ 475 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,319,683 • ❤️ 1,921 • 7d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 3,699 • ❤️ 213 • 15h ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 836 • 7d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 18,626 • ❤️ 345 • 6d ago

---

**[LongCat-2.0](https://huggingface.co/meituan-longcat/LongCat-2.0)**

*LongCat*

LongCat-2.0 is a 1.6T parameter MoE language model featuring LongCat Sparse Attention and N-gram Embedding, optimized for 1M-context tasks. It excels in coding, agentic workflows, and long-horizon reasoning, demonstrating strong performance on benchmarks like Claude Code and OpenClaw.

`text-generation` `1775.6B`

⬇️ 1,308 • ❤️ 173 • 2d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 4,875 • ❤️ 198 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 27 • 💬 1 • ⭐ 689 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 43 • 💬 1 • ⭐ 640 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

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

▲ 11 • 💬 0 • ⭐ 7,253 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 19,774 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 12,080 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 39 • 💬 2 • ⭐ 614 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,211 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Vidu S1: A Real-Time Interactive Video Generation Model](https://huggingface.co/papers/2607.03118)**

*Jintao Zhang, Kai Jiang, Jintao Chen et al. (27 authors)*

🏢 Tsinghua University

Vidu S1 is a real-time interactive video generation model that supports voice-controlled digital character animation with infinite-length output and high frame rate on consumer hardware.

▲ 108 • 💬 7 • ⭐ 141 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.03118) • [💻 code](https://github.com/shengshu-ai/Vidu-S1) • [🔗 project](https://vidu.com/vidu-stream)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,364 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 74,196 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 80.2k • 🔱 4.3k • 1d ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.3k • 🔱 928 • 1d ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.6k • 🔱 224 • 3d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.1k • 🔱 299 • 9h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 1.8k • 🔱 206 • 2d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.6k • 🔱 151 • 21h ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 53 • 4d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 1.3k • 🔱 71 • 12m ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 366 • 13d ago

---

**[eli-labz/Third-Eye](https://github.com/eli-labz/Third-Eye)**

A production-grade OSINT platform that provides situational awareness across multiple intelligence domains.

`TypeScript` `ai` `ai-agent` `geospatial` `maven-smart-system` `palantir`

⭐ 934 • 🔱 13 • 27d ago

---

---

*Generated by PeekDeck - A glance is all you need*
