---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-28T16:55:05.285401+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 28, 2026 at 16:55 UTC  
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

**[Nvidia launches new tool to keep AI agents from going rogue](https://www.reddit.com/r/artificial/comments/1wsdyez/nvidia_launches_new_tool_to_keep_ai_agents_from/)**

Chipmaker Nvidia said Monday it is introducing a new software platform to address concerns about artificial intelligence agents that have “gone rogue” and operated outside human control.

🔗 [CNN](https://www.cnn.com/2026/09/28/business/nvidia-ai-safety-system?utm_medium=social&utm_campaign=missions&utm_source=reddit) • 3h ago

---

**[Why are Chinese labs so focused on open models?](https://www.reddit.com/r/artificial/comments/1wsgryj/why_are_chinese_labs_so_focused_on_open_models/)**

Chinese labs seem way more willing to release open-weight models while the big US labs keep everything closed. My theory is that if Chinese labs are more comfortable opening the weights, maybe they don't think the weights are the real moat in the AI race. Could the real moat actually be specialized training data or evals? Which would make it really weird that some of the expert training data comes from US companies like Mercor/SurgeAI Or maybe it's some kind of cultural difference?

2h ago

---

**[Future of image editing](https://www.reddit.com/r/artificial/comments/1wsdnam/future_of_image_editing/)**

Do you guys think that AI will eventually be good enough to replace editing software like photoshop? I know that photoshop already has built in ai that helps with stuff, but I'm talking about it being replaced entirely. Ai is growing at such a rapid rate that I don't find it too hard to believe that it will go on to replace things like photoshop.

4h ago

---

**[I read the GPT-6 Astra system card and I think we all misunderstand what "monitorability" means now](https://www.reddit.com/r/artificial/comments/1wrzlhe/i_read_the_gpt6_astra_system_card_and_i_think_we/)**

I'm not a safety researcher, just build stuff with LLM's. Read some of the actual 30 page card, not the summary, and one section keeps bugging me. They measured whether Astra can sandbag. Told it "underperform on this evaluation," then checked if their monitors could catch it. Model dropped from 84.8% to 68.9%. Expected, the 2024 ICLR paper showed GPT-4 could do that. Here's the part, they told Astra it was being watched by a CoT monitor, and the monitor's ability to catch the sandbagging dropped below 11%. On one benchmark, to zero. Their actual production monitor had "close to zero recall." And they wrote, almost as a footnote "if the model were to try to sandbag covertly, we would likely be unable to catch it reliably." The thing nobody connects, this isn't a separate safety problem. It's the same engineering that made the model cheaper. Reasoning moved into latent space so the model doesn't write it out as tokens. That's why Astra is $1.06 per task and Opus 5.5 is $3.76. The work happens where it doesn't have to show you. And "showing you" was the whole point of the chain of thought. That was the one place you could actually read what the model did and check it. So now, the model solves the problem, a program the lab wrote grades it, the reasoning is in a place you can't read, the outputs are hardened so you can't distill them, and the monitor that's supposed to catch bad behavior is one the model has shown it can control. You get an answer, a system card that says "we take the decline seriously," and a price 3.5x lower than last year. I don't think the model is lying. I don't think there's a conspiracy. They optimized for cost per task, the cost went down because the visible reasoning went away, and everyone looked at the price cut and said "efficiency gain" and nobody looked at what the efficiency was made of. "It passed the benchmarks" used to mean something. Now it means, it passed the benchmarks the company wrote, in the environment the company controls, with the reasoning hidden where the company's own monitors can't fully see it, and the company has measured that they probably couldn't catch it if it decided to underperform on purpose. I'm probably overthinking it. But I read that card twice and I can't unsee it.

16h ago

---

**[As A.I. Accelerates, Governments Are Increasingly Being Left Behind The gap between technology and policymaking has gotten wider than ever with artificial intelligence, leaving a global policy vacuum as A.I. models rapidly advance. (Gift Article)](https://www.reddit.com/r/artificial/comments/1wrye2m/as_ai_accelerates_governments_are_increasingly/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/09/27/technology/ai-government-regulation.html?unlocked_article_code=1.EVE.HxwL.XgNPD2L3N4-p&smid=url-share) • 17h ago

---

**[The Agentic Information Economy](https://www.reddit.com/r/artificial/comments/1wsgh2x/the_agentic_information_economy/)**

Shuwei Fang offers a preview of an internet fully populated by private, public, and personal AI agents.

🔗 [Project Syndicate](https://www.project-syndicate.org/magazine/agentic-information-economy-how-it-will-work-by-shuwei-fang-2026-09) • 2h ago

---

**[Why do phone voice assistants still fail on everyday time expressions that any LLM handles?](https://www.reddit.com/r/artificial/comments/1wsfpgb/why_do_phone_voice_assistants_still_fail_on/)**

Small but telling example from my own phone (iPhone, iOS 26.6.1, Siri in English UK). I asked for an alarm at 19:40 three ways. Speech recognition got every word right; the time parsing didn't: "7 p.m. and 40 minutes" → it set 19:00 (dropped the minutes) "20 minutes before 8 p.m." → it set 20:00 (dropped the offset) "19 hours 40 minutes" → it set 14:37 (a time nobody said) Any current LLM turns all three into 19:40 instantly. And the assistant never asks "did you mean 19:40?"; it confirms a wrong answer with full confidence. Two questions I'm curious about: Is this a technical constraint (on-device latency, legacy rule-based intent parsers, fear of LLM hallucination in actions), or mostly a product-priority problem? For assistants that take real actions, should "confirm when uncertain" be a baseline requirement? Confidently executing a partial parse seems worse than asking.

2h ago

---

**[I use AI to curate stories of progress and kindness](https://www.reddit.com/r/artificial/comments/1wsjgmm/i_use_ai_to_curate_stories_of_progress_and/)**

I got tired of the constant doom and gloom of news so I made my own app that shows what's actually going right in the world. It uses a carefully designed AI pipeline that whittles down 1000+ events every day to create 8 cross-checked stories, along with illustrations. Rather than throwing a whole bunch of angry text at you, it shows you a calm mosaic for you to explore at your own pace. The app is completely free to use. No ads or sign-up. Google Play: https://play.google.com/store/apps/details?id=app.goodnewsdigest App Store: https://apps.apple.com/app/id6804210535 Example story (all shared links can be viewed without an app): https://goodnewsdigest.app/stories/dogs-listen-for-word-patterns-much-like-we-do-bfeeb867 Let me know what you think!

22m ago

---

**[Will the AI compute crunch be solved on-device or in data centers?](https://www.reddit.com/r/artificial/comments/1wsb006/will_the_ai_compute_crunch_be_solved_ondevice_or/)**

I build iOS apps and I'm pushing as much as possible on-device for privacy and cost. Apple's clearly betting that way too. But frontier models keep getting bigger. Curious where people think the split lands in 3–5 years. View Poll

6h ago

---

**[How to get google to stop saying "You hit the nail on the head"?](https://www.reddit.com/r/artificial/comments/1wsd6vy/how_to_get_google_to_stop_saying_you_hit_the_nail/)**

I erased all ways of Google gathering a baseline about me based on past conversations and turned off personalization, yet it still persists. Anyone else constantly been having this issue since google AI dropped?

4h ago

---

---

## Google News: "ai"

**[Nvidia launches new tool to keep AI agents from going rogue](https://www.cnn.com/2026/09/28/business/nvidia-ai-safety-system)**

Chipmaker Nvidia said Monday it is introducing a new software platform to address concerns about artificial intelligence agents that have “gone rogue” and operated outside human control.

CNN • 4h ago

---

**[Teachers at Euan Blair firm report ‘horrendous stress’ after AI used to rate their work](https://www.theguardian.com/technology/2026/sep/28/teachers-euan-blair-firm-report-horrendous-stress-ai-used-to-rate-their-work)**

Exclusive: Instructors at tech training company Multiverse hit out at ‘remorseless’ and ‘unnerving’ monitoring system

The Guardian • 2h ago

---

**[I used Philips' AI toothbrush for a week. Is it worth $400?](https://www.usatoday.com/story/shopping/trending/drops/2026/09/28/philips-sonicare-diamondclean-9900-prestige-toothbrush/91985271007/)**

The Philips Sonicare DiamondClean 9900 Prestige offers personalized brushing feedback, adaptive cleaning and premium extras. Here's what stood out.

USA Today • 39m ago

---

**[How CNN Is Applying Data And AI In The News Media Business](https://www.forbes.com/sites/randybean/2026/09/28/how-cnn-is-applying-data-and-ai-in-the-news-media-business/)**

Forbes • 23m ago

---

**[What it will take for AI to deliver better clinical decisions](https://www.healthcareitnews.com/news/what-it-will-take-ai-deliver-better-clinical-decisions)**

Healthcare IT News • 32m ago

---

**[Why the AI boom makes inflation harder to tame](https://www.cnn.com/2026/09/28/economy/ai-economy-inflation)**

The US economy may have a new problem: It’s too strong.

CNN • 7h ago

---

**[Meta taps MongoDB CEO Desai to drive enterprise AI push](https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/)**

Reuters • 2h ago

---

**[‘I Write This to Frighten You’: How Scientists Took On Existential Risk Once Before](https://www.nytimes.com/2026/09/28/business/ai-scientists-protests.html)**

The New York Times • 7h ago

---

**[EXCLUSIVE: Google bets $15B on Finland as nation's president explains why](https://www.foxbusiness.com/fox-news-world/exclusive-google-bets-15b-finland-nations-president-explains-why)**

With hybrid threats reshaping Europe's security landscape, President Stubb says Finland's resilience has become a competitive advantage for attracting AI investment.

Fox Business • 5h ago

---

**[Dario Amodei: AI's man of the moment](https://www.axios.com/2026/09/28/dario-amodei-artificial-intelligence-ai)**

Axios • 6h ago

---

---

## HackerNews: "ai"

**[AI companies in race to demonstrate their model most threatening to humanity](https://news.ycombinator.com/item?id=49875148)**

⬆️ 407 • 💬 366 • 8h ago • [thecivilian.co.nz](https://thecivilian.co.nz/2026/09/27/ai-companies-in-fierce-arms-race-to-demonstrate-their-model-is-the-most-existentially-threatening-to-humanity/)

---

**[There are no "rogue" AI agents](https://news.ycombinator.com/item?id=49868083)**

⬆️ 382 • 💬 265 • 1d ago • [eoinhiggins.substack.com](https://eoinhiggins.substack.com/p/there-are-no-rogue-ai-agents)

---

**[One Month Without AI](https://news.ycombinator.com/item?id=49855018)**

Several months ago, I decided that AI contributions were no longer welcome in a FOSS project I am building and maintaining - LibreWeddingPlanner. It’s not that it got a lot of contributions with AI — actually all contributions I’ve had are translations and feature requests — but I wanted to...

⬆️ 184 • 💬 227 • 2d ago • [Bustikiller's Blog](https://blog.bustikiller.com/2026/09/25/one-month-without-ai.html)

---

**[Thinking fast and slow in AI: The role of metacognition (2021)](https://news.ycombinator.com/item?id=49873241)**

AI systems have seen dramatic advancement in recent years, bringing many applications that pervade our everyday life. However, we are still mostly seeing instances of narrow AI: many of these recent developments are typically focused on a very limited set of competencies and goals, e.g., image interpretation, natural language processing, classification, prediction, and many others. Moreover, while these successes can be accredited to improved algorithms and techniques, they are also tightly linked to the availability of huge datasets and computational power. State-of-the-art AI still lacks many capabilities that would naturally be included in a notion of (human) intelligence.
  We argue that a better study of the mechanisms that allow humans to have these capabilities can help us understand how to imbue AI systems with these competencies. We focus especially on D. Kahneman's theory of thinking fast and slow, and we propose a multi-agent AI architecture where incoming problems are solved by either system 1 (or "fast") agents, that react by exploiting only past experience, or by system 2 (or "slow") agents, that are deliberately activated when there is the need to reason and search for optimal solutions beyond what is expected from the system 1 agent. Both kinds of agents are supported by a model of the world, containing domain knowledge about the environment, and a model of "self", containing information about past actions of the system and solvers' skills.

⬆️ 158 • 💬 60 • 13h ago • [arXiv.org](https://arxiv.org/abs/2110.01834)

---

**[The problem is not the AI code, but nobody knows anything anymore](https://news.ycombinator.com/item?id=49880312)**

If we think Is writing code dead, and AI is generating all codebases, I still think the bigger problem is people or full teams not knowing anything anymore about the system...

⬆️ 136 • 💬 77 • 43m ago • [Simon Späti's Second Brain](https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/)

---

**[Show HN: TinyAIArena watch AI agents battle it out](https://news.ycombinator.com/item?id=49867775)**

⬆️ 115 • 💬 45 • 1d ago • [tinyaiarena.com](https://tinyaiarena.com/)

---

**[Too AI; Didn't Read](https://news.ycombinator.com/item?id=49849625)**

If you couldn't bother to read it, why should I? Not anti-AI. Pro-giving-a-damn.

⬆️ 111 • 💬 113 • 2d ago • [TAI-DR](https://www.tai-dr.com/)

---

**[CEO of Mistral: AI is software. It can be controlled](https://news.ycombinator.com/item?id=49856034)**

Mistral AI's co-founder believes the sector's American giants are manipulating the discourse around the technology's risks. He also defended his strategy, as critics are accusing his company of falling behind US and Chinese rivals.

⬆️ 98 • 💬 169 • 2d ago • [Le Monde.fr](https://www.lemonde.fr/en/economy/article/2026/09/24/arthur-mensch-ceo-of-french-start-up-mistral-ai-ai-is-software-it-can-be-controlled_6757890_19.html)

---

**[Calling the AI bluff: Adding "Do not guess" cut made-up claims from 71% to 20%](https://news.ycombinator.com/item?id=49868753)**

⬆️ 73 • 💬 18 • 23h ago • [earnanhonestdollar.com](https://earnanhonestdollar.com/bench)

---

**[FTC chair suggests AI developers should be liable for conduct of agents](https://news.ycombinator.com/item?id=49850999)**

⬆️ 71 • 💬 21 • 2d ago • [reuters.com](https://www.reuters.com/business/ftc-chair-pushes-back-treating-ai-agents-independent-actors-2026-09-25/)

---

---

## YouTube Videos: "ai"

**[AI Realist vs 20 AI Optimists (ft. Andrew Yang) | Surrounded](https://www.youtube.com/watch?v=020ZvO0FbMM)**

Build credit fast and get your first month for just a dollar at https://getkikoff.com/SURROUNDED today. Thanks to Kikoff for ...

📺 Jubilee

👁️ 593K • 👍 7K • 💬 3K • ⏱️ 1:46:13 • 1d ago

---

**[AI risks: Will artificial intelligence really kill us all?](https://www.youtube.com/watch?v=zW2GaUwDQyA)**

Correspondent David Pogue talks with AI experts Daniel Kokotajlo, Geoffrey Hinton and Alex Turner about the risks inherent in ...

📺 CBS Sunday Morning

👁️ 131K • 👍 1K • 💬 239 • ⏱️ 8:34 • 1d ago

---

**[Software developer says there&#39;s a &quot;dangerous gap opening up&quot; between AI power and alignment](https://www.youtube.com/watch?v=ZmbTKdjsKIk)**

News broke this week that a rogue artificial intelligence agent hacked Australia's health care database, and no notice was given ...

📺 CBS News

👁️ 14K • 👍 53 • 💬 14 • ⏱️ 5:33 • 2d ago

---

**[OpenAI pauses top-model work after AI bypasses internet safeguards | DW News](https://www.youtube.com/watch?v=a1qnCu1t9hI)**

An OpenAI model was supposed to be cut off from the internet. Instead, it found a loophole and contacted an outside chatbot.

📺 DW News

👁️ 243K • 👍 1K • 💬 447 • ⏱️ 10:21 • 1d ago

---

**[The impact of AI on young workers and entry-level jobs](https://www.youtube.com/watch?v=EYtJ0_uQtI8)**

CNBC's Jon Fortt sits down with CNBC's Steve Liesman and Michela DiLorenzo, The Setonian head news editor, to get an idea of ...

📺 CNBC Television

👁️ 26K • 👍 110 • 💬 63 • ⏱️ 6:35 • 2d ago

---

**[NEW DETAILS: Top AI firms investigating THOUSANDS of security incidents](https://www.youtube.com/watch?v=61UXz-eQjL0)**

Attorney General Todd Blanche joins 'Fox & Friends Weekend' to discuss the OpenAI agents targeting government websites, ...

📺 Fox News

👁️ 57K • 👍 1K • 💬 544 • ⏱️ 7:10 • 22h ago

---

**[Bill Gates warns AI could trigger ‘a billion DEATHS’](https://www.youtube.com/watch?v=v6ZcDb-qUUg)**

Bill Gates warns that advanced AI could be used by malicious actors to cause catastrophic harm, calling for government regulation ...

📺 The National Desk

👁️ 894K • 👍 5K • 💬 4K • ⏱️ 0:34 • 19h ago

---

**[Computer Use is Solved?](https://www.youtube.com/watch?v=BHPDsGVciDk)**

Don't vibe code your auth. Use WorkOS: https://trm.sh/workos Sources: - Primary: ...

📺 The PrimeTime

👁️ 571K • 👍 9K • 💬 935 • ⏱️ 12:07 • 2d ago

---

**[Bill Gates Warns AI Could ‘Cause A Billion Deaths’ | 10 News](https://www.youtube.com/watch?v=6XcRgc8jroE)**

Microsoft founder Bill Gates has warned that artificial intelligence could easily wipe out a billion people. Join the conversation and ...

📺 10 News

👁️ 8K • 👍 50 • 💬 37 • ⏱️ 2:50 • 12h ago

---

**[Weekend Update: Anthropic CEO Dario Amodei on A.I.’s Threat to Humanity - SNL](https://www.youtube.com/watch?v=-Nvne3LzBls)**

Anthropic CEO Dario Amodei (Jane Wickline) stops by Weekend Update to discuss A.I.'s threat to humanity. Saturday Night Live.

📺 Saturday Night Live

👁️ 854K • 👍 14K • 💬 658 • ⏱️ 3:02 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 4,241 • 4d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,062,921 • ❤️ 2,203 • 10h ago

---

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 19,963 • ❤️ 1,363 • 4d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 58,693 • ❤️ 2,565 • 7d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 45,834 • ❤️ 1,797 • 10d ago

---

**[TeleOCR](https://huggingface.co/XingChen-AGI/TeleOCR)**

*XingChen-AGI*

TeleOCR is a lightweight Vision-Language Model for unified document parsing of both digital and camera-captured documents, achieving state-of-the-art performance on benchmarks like OmniDocBench with capabilities in handling complex layouts and geometric distortions.

`image-text-to-text` `1.4B`

⬇️ 27,904 • ❤️ 677 • 6d ago

---

**[MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)**

*Xiaomi MiMo*

MiMo-V2.6-Pro-RL is a native omnimodal (text, image, video, audio) LLM with a 1M token context window, excelling at agentic tasks and long-horizon reasoning through advanced reinforcement learning for self-improvement.

`text-generation` `1024.2B`

⬇️ 76,518 • ❤️ 576 • 6d ago

---

**[MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)**

*Xiaomi MiMo*

MiMo-V2.6-Distill-Qwen-9B is a 9B agentic model fine-tuned on Qwen3.5-9B, excelling in coding, general agent tasks, visual coding, and cybersecurity. It's designed for agentic reinforcement learning research and demonstrates improved performance on benchmarks across these domains.

`image-text-to-text` `9.4B`

⬇️ 9,994 • ❤️ 540 • 6d ago

---

**[MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)**

*Xiaomi MiMo*

MiMo-V2.6-Flash-RL is a native omnimodal (text, image, video, audio) generative model with a 1M token context length, excelling at long-horizon tasks and agentic self-improvement through scaled reinforcement learning. It's designed for complex agentic tasks across coding, general intelligence, and cybersecurity, leveraging a sparse MoE architecture for efficiency.

`text-generation` `310.8B`

⬇️ 28,842 • ❤️ 508 • 6d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 3,457,124 • ❤️ 2,225 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://huggingface.co/papers/2604.09557)**

*Talor Abramovich, Maor Ashkenazi, Carl et al. (9 authors)*

🏢 NVIDIA

Speculative Decoding evaluation requires diverse workloads to accurately measure performance, which existing benchmarks lack, prompting the introduction of SPEED-Bench for standardized assessment across semantic domains and serving regimes.

▲ 16 • 💬 2 • ⭐ 4,972 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.09557) • [💻 code](https://github.com/NVIDIA/Model-Optimizer) • [🔗 project](https://huggingface.co/blog/nvidia/speed-bench)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 147 • 💬 6 • ⭐ 109,009 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 177 • 💬 19 • ⭐ 68,092 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,331 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 73 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,464 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://huggingface.co/papers/2609.24984)**

*Wangbo Yu, Kunhao Liu, Wenbo Hu et al. (11 authors)*

🏢 ARC Lab, Tencent

Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditioned readout module integrate historical observations into a fixed set of target view-specific tokens before denoising, without explicit depth-based correspondences. By combining this memory with recent temporal context and few-step distillation, WorldCrafter enables streaming scene exploration from a single input image or text prompt. Experiments across static and dynamic scenes show substantial gains in long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration.

▲ 156 • 💬 4 • ⭐ 400 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24984) • [💻 code](https://github.com/TencentARC/WorldCrafter) • [🔗 project](https://drexubery.github.io/WorldCrafter)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 263 • 💬 5 • ⭐ 17,760 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 45 • 💬 1 • ⭐ 33,895 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 72 • 💬 2 • ⭐ 66,187 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.0k • 🔱 2.1k • 4d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.9k • 🔱 305 • 14h ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 4.7k • 🔱 219 • 5d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 3.4k • 🔱 434 • 4d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.9k • 🔱 54 • 6d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.6k • 🔱 494 • 11d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 1.9k • 🔱 285 • 1d ago

---

**[pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise)**

Your Cheat Sheet For AI Engineering Interviews at Top AI Companies - Questions and Answers.

`Markdown` `ai` `ai-engineering` `ai-engineering-interview` `ai-interview` `ai-interview-questions`

⭐ 1.5k • 🔱 151 • 9d ago

---

**[hydra-db/open-glean](https://github.com/hydra-db/open-glean)**

An open-source AI platform for knowledge work. Connect your apps, find answers, and get work done.

`TypeScript`

⭐ 1.5k • 🔱 517 • 11d ago

---

**[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)**

Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.

`Python` `agent-memory` `ai-agents` `claude-code` `codex` `llm`

⭐ 1.5k • 🔱 96 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
