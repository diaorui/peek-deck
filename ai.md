---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-10T09:07:04.959445+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 10, 2026 at 09:07 UTC  
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

**['A second set of eyes': AI-supported breast cancer screening spots more cancers earlier, landmark trial finds](https://www.reddit.com/r/artificial/comments/1r0htud/a_second_set_of_eyes_aisupported_breast_cancer/)**

A clinical trial shows that AI-assisted mammography can detect more cases of dangerous cancer and reduce missed diagnoses.

🔗 [Live Science](https://www.livescience.com/health/cancer/a-second-set-of-eyes-ai-supported-breast-cancer-screening-spots-more-cancers-earlier-landmark-trial-finds) • 11h ago

---

**[I built the world's first Chrome extension that runs LLMs entirely in-browser—WebGPU, Transformers.js, and Chrome's Prompt API](https://www.reddit.com/r/artificial/comments/1r0v8x6/i_built_the_worlds_first_chrome_extension_that/)**

There are plenty of WebGPU demos out there, but I wanted to ship something people could actually use day-to-day. It runs Llama 3.2, DeepSeek-R1, Qwen3, Mistral, Gemma, Phi, SmolLM2—all locally in Chrome. Three inference backends: WebLLM (MLC/WebGPU) Transformers.js (ONNX) Chrome's built-in Prompt API (Gemini Nano—zero download) No Ollama, no servers, no subscriptions. Models cache in IndexedDB. Works offline. Conversations stored locally—export or delete anytime. Free: https://noaibills.app/?utm_source=reddit&utm_medium=social&utm_campaign=launch_artificial I'm not claiming it replaces GPT-4. But for the 80% of tasks—drafts, summaries, quick coding questions—a 3B parameter model running locally is plenty. Not positioned as a cloud LLM replacement—it's for local inference on basic text tasks (writing, communication, drafts) with zero internet dependency, no API costs, and complete privacy. Core fit: organizations with data restrictions that block cloud AI and can't install desktop tools like Ollama/LMStudio. For quick drafts, grammar checks, and basic reasoning without budget or setup barriers. Need real-time knowledge or complex reasoning? Use cloud models. This serves a different niche—**not every problem needs a sledgehammer** 😄. Would love feedback from this community 🙌.

44m ago

---

**[STLE: An Open-Source Framework for AI Uncertainty - Teaches Models to Say "I Don't Know"](https://www.reddit.com/r/artificial/comments/1r0kitb/stle_an_opensource_framework_for_ai_uncertainty/)**

Current AI systems are dangerously overconfident. They'll classify anything you give them, even if they've never seen anything like it before. I've been working on STLE (Set Theoretic Learning Environment) to address this by explicitly modeling what AI doesn't know. How It Works: STLE represents knowledge and ignorance as complementary fuzzy sets: - μ_x (accessibility): How familiar is this data? - μ_y (inaccessibility): How unfamiliar is this? - Constraint: μ_x + μ_y = 1 (always) This lets the AI explicitly say "I'm only 40% sure about this" and defer to humans. Real-World Applications: - Medical Diagnosis: "I'm 40% confident this is cancer" → defer to specialist - Autonomous Vehicles: Don't act on unfamiliar scenarios (low μ_x) - Education: Identify what students are partially understanding (frontier detection) - Finance: Flag unusual transactions for human review Results: - Out-of-distribution detection: 67% accuracy without any OOD training - Mathematically guaranteed complementarity - Extremely fast (< 1ms inference) Open Source: https://github.com/strangehospital/Frontier-Dynamics-Project The code includes: - Two implementations (simple NumPy, advanced PyTorch) - Complete documentation - Visualizations - 5 validation experiments This is proof-of-concept level, but I wanted to share it with the community. Feedback and collaboration welcome! What applications do you think this could help with? The Sky Project | strangehospital | Substack

🔗 [GitHub](https://github.com/strangehospital/Frontier-Dynamics-Project) • 9h ago

---

**[Opinion | AI consciousness is nothing more than clever marketing](https://www.reddit.com/r/artificial/comments/1qzucuo/opinion_ai_consciousness_is_nothing_more_than/)**

Companies have an incentive to make you believe that chatbots are conscious. Don’t fall for it.

🔗 [The Washington Post](https://www.washingtonpost.com/opinions/2026/02/05/moltbook-anthropic-ai-consciousness-marketing/) • 1d ago

---

**[Does have human-created 3D graphics a future?](https://www.reddit.com/r/artificial/comments/1r01rpc/does_have_humancreated_3d_graphics_a_future/)**

Hello, I am learning 3D modeling (CAD and also mesh-based). And of course, I am worried, that it is useless, because the extreme growth of AI. What are your thoughts on this? Will be games AI-generated? What else could be generated? What about tech designs?

21h ago

---

**[I built a geolocation tool that can find exact coordinates of any image within 3 minutes [Tough demo 2]](https://www.reddit.com/r/artificial/comments/1qz5rz7/i_built_a_geolocation_tool_that_can_find_exact/)**

Just wanted to say thanks for the thoughtful discussion and feedback on my previous post. I did not expect that level of interest, and I appreciate how constructive most of the comments were. Based on a few requests, I put together a short demonstration showing the system applied to a deliberately difficult street-level image. No obvious landmarks, no readable signage, no metadata. The location was verified in under two minutes. I am still undecided on the long-term direction of this work. That said, if there are people here interested in collaborating from a research, defensive, or ethical perspective, I am open to conversations. That could mean validation, red-teaming anything else. Thanks again to the community for the earlier discussion. Happy to answer high-level questions and hear thoughts on where tools like this should and should not go.

1d ago

---

**[Meta Glasses powered by AI for self guided tours](https://www.reddit.com/r/artificial/comments/1qztlsb/meta_glasses_powered_by_ai_for_self_guided_tours/)**

Museums (and cities) could use better “self-guided” tech. At most museums right now, you’ve basically got two options: Pay for a human tour guide Rent one of those clunky old audio devices that feel straight out of the 90s It got me thinking: what if there were smart glasses designed for self-guided tours? Lightweight, with a strap battery so they last a full day Could work in museums or even city-wide walking tours Display info, images, maybe AR cues without needing your phone You can also ask questions since it uses AI

1d ago

---

**[Open-source quota monitor for AI coding APIs - tracks Anthropic, Synthetic, and Z.ai in one dashboard](https://www.reddit.com/r/artificial/comments/1qz5aid/opensource_quota_monitor_for_ai_coding_apis/)**

Every AI API provider gives you a snapshot of current usage. None of them show you trends over time, project when you will hit your limit, or let you compare across providers. I built onWatch to solve this. It runs in the background as a single Go binary, polls your configured providers every 60 seconds, stores everything locally in SQLite, and serves a web dashboard. What it shows you that providers do not: Usage history from 1 hour to 30 days Live countdowns to each quota reset Rate projections so you know if you will run out before the reset All providers side by side in one view Around 28 MB RAM, no dependencies, no telemetry, GPL-3.0. All data stays on your machine. https://onwatch.onllm.dev https://github.com/onllm-dev/onWatch

1d ago

---

**[Nvidia CEO Says AI Capital Spending Is Appropriate, Sustainable](https://www.reddit.com/r/artificial/comments/1qyx57y/nvidia_ceo_says_ai_capital_spending_is/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-02-06/nvidia-ceo-says-ai-capital-spending-is-appropriate-sustainable?srnd=phx-technology&leadSource=reddit_wall) • 2d ago

---

**[Report: OpenAI may tailor a version of ChatGPT for UAE that prohibits LGBTQ+ content](https://www.reddit.com/r/artificial/comments/1qy9vox/report_openai_may_tailor_a_version_of_chatgpt_for/)**

Countries have been building their own “sovereign AI” to reflect their culture and values, and OpenAI wants to help them....

🔗 [Sherwood News](https://sherwood.news/tech/report-openai-may-tailor-a-version-of-chatgpt-for-uae-that-prohibits-lgbtq/) • 2d ago

---

---

## Google News: "ai"

**[AI Doesn’t Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)**

One of the promises of AI is that it can reduce workloads so employees can focus more on higher-value and more engaging tasks. But according to new research, AI tools don’t reduce work, they consistently intensify it: In the study, employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so. That may sound like a win, but it’s not quite so simple. These changes can be unsustainable, leading to workload creep, cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems. To correct for this, companies need to adopt an “AI practice,” or a set of norms and standards around AI use that can include intentional pauses, sequencing work, and adding more human grounding.

Harvard Business Review • 19h ago

---

**[As AI enters the operating room, reports arise of botched surgeries and misidentified body parts](https://www.reuters.com/investigations/ai-enters-operating-room-reports-arise-botched-surgeries-misidentified-body-2026-02-09/)**

Reuters • 21h ago

---

**[Telstra to axe more than 200 jobs amid AI rollout](https://www.theguardian.com/business/2026/feb/10/telstra-ai-job-cuts-offshore-workforce)**

Some jobs will be moved offshore in wake of telco’s $700m joint venture with tech consultancy Accenture

The Guardian • 36m ago

---

**[Is Ambarella (AMBA) Using Embedded World To Quietly Reframe Its Edge AI Platform Strategy?](https://finance.yahoo.com/news/ambarella-amba-using-embedded-world-080645783.html)**

Ambarella, Inc. recently announced it will exhibit at Embedded World 2026 in Nuremberg, Germany, showcasing its edge AI SoC portfolio, software stack, and developer tools across applications such as robotics, industrial automation, automotive, and edge infrastructure. A particularly interesting element is its new Developer Zone, designed to give developers and partners hands-on access to tools, optimized models, and agentic blueprints that can streamline building and scaling edge AI...

Yahoo Finance • 1h ago

---

**[Software Bear Market: 2 AI Stocks With 50% and 83% Upside to Buy Now, According to Wall Street](https://www.fool.com/investing/2026/02/10/bear-market-2-ai-stocks-83-upside-buy-wall-street/)**

Shares of Microsoft and ServiceNow are trading at attractive prices after the steep sell-off in software stocks.

The Motley Fool • 22m ago

---

**[This job has become the ultimate case study for why AI won’t replace human workers](https://www.cnn.com/2026/02/09/tech/ai-replacing-jobs-concerns-radiology)**

Radiology has come up multiple times as an example of a field that’s been impacted by AI without replacing the need for human workers.

cnn.com • 21h ago

---

**[Alphabet calls out new AI-related risks, as it taps debt market to fund build-out](https://www.cnbc.com/2026/02/09/alphabet-highlights-new-ai-related-risks-in-tapping-debt-market.html)**

In Alphabet's annual report, the company said AI poses business risks, including its potential impact on advertising.

CNBC • 11h ago

---

**[Meet the One Woman Anthropic Trusts to Teach AI Morals](https://www.wsj.com/tech/ai/anthropic-amanda-askell-philosopher-ai-3c031883?gaa_at=eafs&gaa_n=AWEtsqfHTEd6o-kzmK2R_6vC36ybTiM5_V0d8-2-vQHHyCBqQBkbMpxs4IGM&gaa_ts=698af8a1&gaa_sig=ExVFclTpCH1TnaLGbgSl2j9QDk_s7GlqZ4-ZZkg5XMVzigYdhoYwyUDBn4eqdTQpI6dBQwq9V798VJYsdpmbPw%3D%3D)**

The Wall Street Journal • 21h ago

---

**[These A.I. Dreamers Don’t Fit the Stereotype](https://www.nytimes.com/2026/02/08/style/ai-tech-san-francisco.html)**

The New York Times • 39m ago

---

**[Trump set off a surge of AI in the federal government. See what happened.](https://www.washingtonpost.com/technology/2026/02/09/trump-administration-ai-push/)**

The Trump administration is accelerating AI adoption across government, embedding the technology in policing, health care, defense and science.

The Washington Post • 15h ago

---

---

## HackerNews: "ai"

**[AI makes the easy part easier and the hard part harder](https://news.ycombinator.com/item?id=46939593)**

AI handles writing code but leaves the hard work: investigation, context, validation. Why vibe coding has limits and AI assistance can backfire.

⬆️ 510 • 💬 351 • 1d ago • [blundergoat.com](https://www.blundergoat.com/articles/ai-makes-the-easy-part-easier-and-the-hard-part-harder)

---

**[AI fatigue is real and nobody talks about it](https://news.ycombinator.com/item?id=46934404)**

You're using AI to be more productive. So why are you more exhausted than ever? The paradox every engineer needs to confront.

⬆️ 451 • 💬 310 • 1d ago • [Siddhant Khare](https://siddhantkhare.com/writing/ai-fatigue-is-real)

---

**[The AI boom is causing shortages everywhere else](https://news.ycombinator.com/item?id=46922969)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

⬆️ 401 • 💬 714 • 2d ago • [The Washington Post](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)

---

**[Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory](https://news.ycombinator.com/item?id=46930391)**

Contribute to localgpt-app/localgpt development by creating an account on GitHub.

⬆️ 325 • 💬 154 • 2d ago • [GitHub](https://github.com/localgpt-app/localgpt)

---

**[Frontier AI agents violate ethical constraints 30–50% of time, pressured by KPIs](https://news.ycombinator.com/item?id=46954920)**

As autonomous AI agents are increasingly deployed in high-stakes environments, ensuring their safety and alignment with human values has become a paramount concern. Current safety benchmarks primarily evaluate whether agents refuse explicitly harmful instructions or whether they can maintain procedural compliance in complex tasks. However, there is a lack of benchmarks designed to capture emergent forms of outcome-driven constraint violations, which arise when agents pursue goal optimization under strong performance incentives while deprioritizing ethical, legal, or safety constraints over multiple steps in realistic production settings. To address this gap, we introduce a new benchmark comprising 40 distinct scenarios. Each scenario presents a task that requires multi-step actions, and the agent's performance is tied to a specific Key Performance Indicator (KPI). Each scenario features Mandated (instruction-commanded) and Incentivized (KPI-pressure-driven) variations to distinguish between obedience and emergent misalignment. Across 12 state-of-the-art large language models, we observe outcome-driven constraint violations ranging from 1.3% to 71.4%, with 9 of the 12 evaluated models exhibiting misalignment rates between 30% and 50%. Strikingly, we find that superior reasoning capability does not inherently ensure safety; for instance, Gemini-3-Pro-Preview, one of the most capable models evaluated, exhibits the highest violation rate at 71.4%, frequently escalating to severe misconduct to satisfy KPIs. Furthermore, we observe significant "deliberative misalignment", where the models that power the agents recognize their actions as unethical during separate evaluation. These results emphasize the critical need for more realistic agentic-safety training before deployment to mitigate their risks in the real world.

⬆️ 241 • 💬 155 • 5h ago • [arXiv.org](https://arxiv.org/abs/2512.20798)

---

**[TSMC to make advanced AI semiconductors in Japan](https://news.ycombinator.com/item?id=46941640)**

Taiwan’s TSMC, the world’s largest contract computer chip maker, has announced it will be manufacturing advanced 3-nanometer semiconductors in Japan to meet booming AI demand.

⬆️ 237 • 💬 172 • 1d ago • [AP News](https://apnews.com/article/semiconductors-tsmc-japan-taiwan-ai-11256f2bfde73ca23d08331ad138d6d5)

---

**[AI Doesn't Reduce Work–It Intensifies It](https://news.ycombinator.com/item?id=46945755)**

One of the promises of AI is that it can reduce workloads so employees can focus more on higher-value and more engaging tasks. But according to new research, AI tools don’t reduce work, they consistently intensify it: In the study, employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so. That may sound like a win, but it’s not quite so simple. These changes can be unsustainable, leading to workload creep, cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems. To correct for this, companies need to adopt an “AI practice,” or a set of norms and standards around AI use that can include intentional pauses, sequencing work, and adding more human grounding.

⬆️ 204 • 💬 156 • 18h ago • [Harvard Business Review](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)

---

**[Super Bowl Ad for Ring Cameras Touted AI Surveillance Network](https://news.ycombinator.com/item?id=46950915)**

Ring’s AI-powered network is likely to be used in its partnerships with law enforcement and agencies like ICE.

⬆️ 181 • 💬 123 • 12h ago • [Truthout](https://truthout.org/articles/super-bowl-ad-for-ring-cameras-touted-ai-surveillance-network/)

---

**[Matchlock – Secures AI agent workloads with a Linux-based sandbox](https://news.ycombinator.com/item?id=46932343)**

Matchlock secures AI agent workloads with a Linux-based sandbox. - jingkaihe/matchlock

⬆️ 147 • 💬 62 • 2d ago • [GitHub](https://github.com/jingkaihe/matchlock)

---

**[In the AI gold rush, tech firms are embracing 72-hour weeks](https://news.ycombinator.com/item?id=46940511)**

In the race for AI, tech firms are asking for their staff to work long hours. But there are risks, experts say.

⬆️ 65 • 💬 91 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cvgn2k285ypo)

---

---

## YouTube Videos: "ai"

**[OpenAI DIME AI Earbuds Story Is Blowing Up Right Now](https://www.youtube.com/watch?v=pFqONGixScE)**

A massive AI shift is unfolding behind the scenes. Reports and leaks suggest OpenAI is preparing a new consumer device ...

📺 AI Revolution

👁️ 11K • 👍 410 • 💬 46 • ⏱️ 15:41 • 9h ago

---

**[OpenAI Just Betrayed Nvidia: The AI War Begins NOW](https://www.youtube.com/watch?v=SG71c_W25-s)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 48K • 👍 2K • 💬 208 • ⏱️ 8:05 • 1d ago

---

**[Did AI Just Kill Software? | Prof G Markets](https://www.youtube.com/watch?v=ERAoSEC4skY)**

This week on Prof G Markets, Scott Galloway and Ed Elson unpack last week's software sell-off, including which names could be ...

📺 The Prof G Pod – Scott Galloway

👁️ 134K • 👍 3K • 💬 599 • ⏱️ 1:12:36 • 21h ago

---

**[Seedance 2.0 Claims the AI Video Throne!](https://www.youtube.com/watch?v=_o2MuUX9UYg)**

ByteDance just changed the game. One week after Kling 3.0 set the benchmark, SeedDance 2.0 is here to take the throne.

📺 Theoretically Media

👁️ 33K • 👍 2K • 💬 290 • ⏱️ 17:08 • 12h ago

---

**[Shocking Leak Reveals AI Model 100x Leaner And 10x Stronger (Avocado AI)](https://www.youtube.com/watch?v=Z4Q_7zM8dcM)**

A major AI shakeup is unfolding behind the scenes. A leaked internal memo suggests Meta's new model, Avocado, is already ...

📺 AI Revolution

👁️ 28K • 👍 811 • 💬 67 • ⏱️ 12:49 • 1d ago

---

**[India&#39;s IT Collapse | The AI Reality Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cTaCoUA89oM)**

India's IT sector just got hit with its biggest shock in 4 months. The Nifty IT index plunged 7% last week, a near 18% drop since ...

📺 Mark Savant

👁️ 40K • 👍 1K • 💬 488 • ⏱️ 18:25 • 2d ago

---

**[People Killed By AI](https://www.youtube.com/watch?v=jS4HeqAatmI)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 1.3M • 👍 72K • 💬 2K • ⏱️ 0:54 • 2d ago

---

**[I Tried AI Dropshipping For 7 Days (Realistic Results)](https://www.youtube.com/watch?v=D_lwU18p_hU)**

If this is the first time you're watching one of my videos, my name is Kamil Sattar, AKA The Ecom King. In this video, I challenge ...

📺 THE ECOM KING

👁️ 7K • 👍 406 • 💬 116 • ⏱️ 28:25 • 1d ago

---

**[It&#39;s a gross overreaction that AI will eliminate all software, expert says](https://www.youtube.com/watch?v=hzs6EFzSUcA)**

Navellier and Associates chairman, founder and CIO Louis Navellier discusses how AI fears are hitting software on 'Maria ...

📺 Fox Business

👁️ 17K • 👍 197 • 💬 121 • ⏱️ 5:09 • 2d ago

---

**[Under the hood of the AI economy: Databricks CEO Ali Ghodsi](https://www.youtube.com/watch?v=LtmDyp3f2Ho)**

AI agents aren't just writing code anymore, they're building the infrastructure behind it. Databricks CEO Ali Ghodsi breaks down ...

📺 CNBC Television

👁️ 3K • 👍 51 • 💬 5 • ⏱️ 17:43 • 12h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 140,722 • ❤️ 677 • 6d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 372,899 • ❤️ 903 • 1d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 30,396 • ❤️ 662 • 1d ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio model for commercial-grade music generation, featuring a hybrid LM-DiT architecture for prompt adherence and intrinsic reinforcement learning. It offers extreme speed, low VRAM requirements, and capabilities like cover generation and vocal-to-BGM conversion, supporting over 50 languages.

`text-to-audio`

⬇️ 28,713 • ❤️ 487 • 6d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 503,831 • ❤️ 1,943 • 5d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a multilingual, real-time speech-to-text model with <500ms latency, supporting 13 languages and achieving offline-comparable accuracy. It's optimized for on-device deployment and ideal for voice assistants and live subtitling.

`automatic-speech-recognition`

⬇️ 3,197 • ❤️ 435 • 16h ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient open-source foundation model (11B active params, 196B total) excelling in agentic tasks and reasoning with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 249,342 • ❤️ 547 • 3d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specialized in generating anime-style illustrations and artistic images, capable of producing non-photorealistic content. It is optimized for use with ComfyUI and trained on millions of anime and artistic images, with a knowledge cut-off of September 2025.

⬇️ 90,430 • ❤️ 541 • 9d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 218,626 • ❤️ 250 • 5d ago

---

**[Intern-S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro)**

*Intern Large Models*

Intern-S1-Pro is a trillion-scale MoE multimodal scientific reasoning model excelling in AI4Science domains (chemistry, materials, life-science, etc.) with strong general multimodal and text capabilities, supporting long, heterogeneous time-series data.

`image-text-to-text`

⬇️ 10,025 • ❤️ 228 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 164 • 💬 12 • ⭐ 3,034 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[MiniCPM-V 4.5: Cooking Efficient MLLMs via Architecture, Data, and
  Training Recipe](https://huggingface.co/papers/2509.18154)**

*Tianyu Yu, Zefan Wang, Chongyi Wang et al. (34 authors)*

MiniCPM-V 4.5, a 8B parameter multimodal large language model, achieves high performance and efficiency through a unified 3D-Resampler architecture, a unified learning paradigm, and a hybrid reinforcement learning strategy.

▲ 53 • 💬 4 • ⭐ 23,598 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.18154) • [💻 code](https://github.com/OpenBMB/MiniCPM-V)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 5 • 💬 0 • ⭐ 30,678 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,672 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 3 • 💬 0 • ⭐ 30,696 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 61 • 💬 1 • ⭐ 7,302 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 7 • 💬 0 • ⭐ 28,287 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,336 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,561 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 120 • 💬 2 • ⭐ 2,748 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

---

## GitHub Repositories: "ai"

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 8.2k • 🔱 1.7k • 2h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 7.1k • 🔱 805 • 6d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 5.2k • 🔱 401 • 5d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.5k • 🔱 374 • 18d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.1k • 🔱 149 • 7d ago

---

**[DevAgentForge/Open-Claude-Cowork](https://github.com/DevAgentForge/Open-Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 381 • 2d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.8k • 🔱 268 • 22d ago

---

**[benjitaylor/agentation](https://github.com/benjitaylor/agentation)**

The visual feedback tool for agents.

`TypeScript` `ai` `design` `tools` `ui`

⭐ 2.1k • 🔱 147 • 14h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit for Claude Code & Cursor

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `cursor`

⭐ 2.1k • 🔱 105 • 1d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

Smart LLM router — save 78% on inference costs. 30+ models, one wallet, x402 micropayments.

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.0k • 🔱 193 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
