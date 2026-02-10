---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-10T16:07:11.556278+00:00'
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

**Last Updated:** February 10, 2026 at 16:07 UTC  
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

**[I built the world's first Chrome extension that runs LLMs entirely in-browser—WebGPU, Transformers.js, and Chrome's Prompt API](https://www.reddit.com/r/artificial/comments/1r0v8x6/i_built_the_worlds_first_chrome_extension_that/)**

There are plenty of WebGPU demos out there, but I wanted to ship something people could actually use day-to-day. It runs Llama 3.2, DeepSeek-R1, Qwen3, Mistral, Gemma, Phi, SmolLM2—all locally in Chrome. Three inference backends: WebLLM (MLC/WebGPU) Transformers.js (ONNX) Chrome's built-in Prompt API (Gemini Nano—zero download) No Ollama, no servers, no subscriptions. Models cache in IndexedDB. Works offline. Conversations stored locally—export or delete anytime. Free: https://noaibills.app/?utm_source=reddit&utm_medium=social&utm_campaign=launch_artificial I'm not claiming it replaces GPT-4. But for the 80% of tasks—drafts, summaries, quick coding questions—a 3B parameter model running locally is plenty. Not positioned as a cloud LLM replacement—it's for local inference on basic text tasks (writing, communication, drafts) with zero internet dependency, no API costs, and complete privacy. Core fit: organizations with data restrictions that block cloud AI and can't install desktop tools like Ollama/LMStudio. For quick drafts, grammar checks, and basic reasoning without budget or setup barriers. Need real-time knowledge or complex reasoning? Use cloud models. This serves a different niche—**not every problem needs a sledgehammer** 😄. Would love feedback from this community 🙌.

7h ago

---

**[Kling AI Launches 3.0 Model, Ushering in an Era Where Everyone Can Be a Director](https://www.reddit.com/r/artificial/comments/1r0ww09/kling_ai_launches_30_model_ushering_in_an_era/)**

/PRNewswire/ -- Kling AI, the AI-powered creative platform, today announced the launch of its Kling 3.0 models — including Video 3.0, Video 3.0 Omni, Image 3.0...

🔗 [prnewswire.com](https://www.prnewswire.com/news-releases/kling-ai-launches-3-0-model-ushering-in-an-era-where-everyone-can-be-a-director-302679944.html) • 5h ago

---

**['A second set of eyes': AI-supported breast cancer screening spots more cancers earlier, landmark trial finds](https://www.reddit.com/r/artificial/comments/1r0htud/a_second_set_of_eyes_aisupported_breast_cancer/)**

A clinical trial shows that AI-assisted mammography can detect more cases of dangerous cancer and reduce missed diagnoses.

🔗 [Live Science](https://www.livescience.com/health/cancer/a-second-set-of-eyes-ai-supported-breast-cancer-screening-spots-more-cancers-earlier-landmark-trial-finds) • 18h ago

---

**[STLE: An Open-Source Framework for AI Uncertainty - Teaches Models to Say "I Don't Know"](https://www.reddit.com/r/artificial/comments/1r0kitb/stle_an_opensource_framework_for_ai_uncertainty/)**

Current AI systems are dangerously overconfident. They'll classify anything you give them, even if they've never seen anything like it before. I've been working on STLE (Set Theoretic Learning Environment) to address this by explicitly modeling what AI doesn't know. How It Works: STLE represents knowledge and ignorance as complementary fuzzy sets: - μ_x (accessibility): How familiar is this data? - μ_y (inaccessibility): How unfamiliar is this? - Constraint: μ_x + μ_y = 1 (always) This lets the AI explicitly say "I'm only 40% sure about this" and defer to humans. Real-World Applications: - Medical Diagnosis: "I'm 40% confident this is cancer" → defer to specialist - Autonomous Vehicles: Don't act on unfamiliar scenarios (low μ_x) - Education: Identify what students are partially understanding (frontier detection) - Finance: Flag unusual transactions for human review Results: - Out-of-distribution detection: 67% accuracy without any OOD training - Mathematically guaranteed complementarity - Extremely fast (< 1ms inference) Open Source: https://github.com/strangehospital/Frontier-Dynamics-Project The code includes: - Two implementations (simple NumPy, advanced PyTorch) - Complete documentation - Visualizations - 5 validation experiments This is proof-of-concept level, but I wanted to share it with the community. Feedback and collaboration welcome! What applications do you think this could help with? The Sky Project | strangehospital | Substack

🔗 [GitHub](https://github.com/strangehospital/Frontier-Dynamics-Project) • 16h ago

---

**[Opinion | AI consciousness is nothing more than clever marketing](https://www.reddit.com/r/artificial/comments/1qzucuo/opinion_ai_consciousness_is_nothing_more_than/)**

Companies have an incentive to make you believe that chatbots are conscious. Don’t fall for it.

🔗 [The Washington Post](https://www.washingtonpost.com/opinions/2026/02/05/moltbook-anthropic-ai-consciousness-marketing/) • 1d ago

---

**[Does have human-created 3D graphics a future?](https://www.reddit.com/r/artificial/comments/1r01rpc/does_have_humancreated_3d_graphics_a_future/)**

Hello, I am learning 3D modeling (CAD and also mesh-based). And of course, I am worried, that it is useless, because the extreme growth of AI. What are your thoughts on this? Will be games AI-generated? What else could be generated? What about tech designs?

1d ago

---

**[I built a geolocation tool that can find exact coordinates of any image within 3 minutes [Tough demo 2]](https://www.reddit.com/r/artificial/comments/1qz5rz7/i_built_a_geolocation_tool_that_can_find_exact/)**

Just wanted to say thanks for the thoughtful discussion and feedback on my previous post. I did not expect that level of interest, and I appreciate how constructive most of the comments were. Based on a few requests, I put together a short demonstration showing the system applied to a deliberately difficult street-level image. No obvious landmarks, no readable signage, no metadata. The location was verified in under two minutes. I am still undecided on the long-term direction of this work. That said, if there are people here interested in collaborating from a research, defensive, or ethical perspective, I am open to conversations. That could mean validation, red-teaming anything else. Thanks again to the community for the earlier discussion. Happy to answer high-level questions and hear thoughts on where tools like this should and should not go.

2d ago

---

**[Meta Glasses powered by AI for self guided tours](https://www.reddit.com/r/artificial/comments/1qztlsb/meta_glasses_powered_by_ai_for_self_guided_tours/)**

Museums (and cities) could use better “self-guided” tech. At most museums right now, you’ve basically got two options: Pay for a human tour guide Rent one of those clunky old audio devices that feel straight out of the 90s It got me thinking: what if there were smart glasses designed for self-guided tours? Lightweight, with a strap battery so they last a full day Could work in museums or even city-wide walking tours Display info, images, maybe AR cues without needing your phone You can also ask questions since it uses AI

1d ago

---

**[Open-source quota monitor for AI coding APIs - tracks Anthropic, Synthetic, and Z.ai in one dashboard](https://www.reddit.com/r/artificial/comments/1qz5aid/opensource_quota_monitor_for_ai_coding_apis/)**

Every AI API provider gives you a snapshot of current usage. None of them show you trends over time, project when you will hit your limit, or let you compare across providers. I built onWatch to solve this. It runs in the background as a single Go binary, polls your configured providers every 60 seconds, stores everything locally in SQLite, and serves a web dashboard. What it shows you that providers do not: Usage history from 1 hour to 30 days Live countdowns to each quota reset Rate projections so you know if you will run out before the reset All providers side by side in one view Around 28 MB RAM, no dependencies, no telemetry, GPL-3.0. All data stays on your machine. https://onwatch.onllm.dev https://github.com/onllm-dev/onWatch

2d ago

---

**[Nvidia CEO Says AI Capital Spending Is Appropriate, Sustainable](https://www.reddit.com/r/artificial/comments/1qyx57y/nvidia_ceo_says_ai_capital_spending_is/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-02-06/nvidia-ceo-says-ai-capital-spending-is-appropriate-sustainable?srnd=phx-technology&leadSource=reddit_wall) • 2d ago

---

---

## Google News: "ai"

**[AI Doesn’t Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)**

One of the promises of AI is that it can reduce workloads so employees can focus more on higher-value and more engaging tasks. But according to new research, AI tools don’t reduce work, they consistently intensify it: In the study, employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so. That may sound like a win, but it’s not quite so simple. These changes can be unsustainable, leading to workload creep, cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems. To correct for this, companies need to adopt an “AI practice,” or a set of norms and standards around AI use that can include intentional pauses, sequencing work, and adding more human grounding.

Harvard Business Review • 1d ago

---

**[As AI enters the operating room, reports arise of botched surgeries and misidentified body parts](https://www.reuters.com/investigations/ai-enters-operating-room-reports-arise-botched-surgeries-misidentified-body-2026-02-09/)**

Reuters • 1d ago

---

**[America Isn’t Ready for What AI Will Do to Jobs](https://www.theatlantic.com/magazine/2026/03/ai-economy-labor-market-transformation/685731/)**

Does anyone have a plan for what happens next?

The Atlantic • 5h ago

---

**[The AI Divide](https://www.foreignaffairs.com/united-states/ai-divide)**

How U.S.-Chinese competition could leave most countries behind.

Foreign Affairs • 11h ago

---

**[Will the Gulf’s push for its own AI succeed?](https://www.theguardian.com/technology/2026/feb/09/us-tech-ai-companies-gulf-states)**

Tech giants Alphabet, Amazon, Microsoft and Meta to collectively invest $600bn on artificial intelligence this year

The Guardian • 1h ago

---

**[Exclusive: Pakistan moves towards sovereign AI](https://www.axios.com/2026/02/10/pakistan-dfinity-ai-cloud-sovereignty)**

If successful, the effort could serve as a model for other emerging economies looking to jumpstart AI-based growth while keeping sensitive data stored within national networks and out of reach of foreign adversaries.

Axios • 1h ago

---

**[Wall Street is searching for AI winners and losers](https://www.cnn.com/2026/02/10/markets/ai-investing-stock-market-companies)**

For years, anything exposed to artificial intelligence was a popular trade on Wall Street. Now investors are starting to get selective, demanding more proof that companies are poised to benefit from the AI boom.

cnn.com • 6h ago

---

**[The stock market looks expensive — but this chart shows why AI bubble fears in tech may be overblown](https://www.marketwatch.com/story/the-stock-market-looks-expensive-but-this-chart-shows-why-ai-bubble-fears-in-tech-may-be-overblown-13f556d1?gaa_at=eafs&gaa_n=AWEtsqcrJrJUFoGYW1xJfo89mHrsEE3mKNhsgo_PdwYfuY9XBxDTCrKaNzVx&gaa_ts=698b5b18&gaa_sig=merrj6bHNLsxu1q-hvFwhHb1GIYncABzhwQ-Xq7Ya2MM0Paen5PFnldGlFQwxIetMIRV5b2zazatHUm6fbhVxg%3D%3D)**

MarketWatch • 21h ago

---

**[AMD vs. Nvidia: Which AI Stock Will Outperform in 2026?](https://finance.yahoo.com/news/amd-vs-nvidia-ai-stock-140500823.html)**

AMD has been the better stock pick as of late.

Yahoo Finance • 2h ago

---

**[A.I. Is Making Doctors Answer a Question: What Are They Really Good For?](https://www.nytimes.com/2026/02/09/health/ai-chatbots-doctors-medicine.html)**

The New York Times • 22h ago

---

---

## HackerNews: "ai"

**[AI makes the easy part easier and the hard part harder](https://news.ycombinator.com/item?id=46939593)**

AI handles writing code but leaves the hard work: investigation, context, validation. Why vibe coding has limits and AI assistance can backfire.

⬆️ 516 • 💬 352 • 1d ago • [blundergoat.com](https://www.blundergoat.com/articles/ai-makes-the-easy-part-easier-and-the-hard-part-harder)

---

**[AI fatigue is real and nobody talks about it](https://news.ycombinator.com/item?id=46934404)**

You're using AI to be more productive. So why are you more exhausted than ever? The paradox every engineer needs to confront.

⬆️ 454 • 💬 312 • 2d ago • [Siddhant Khare](https://siddhantkhare.com/writing/ai-fatigue-is-real)

---

**[Frontier AI agents violate ethical constraints 30–50% of time, pressured by KPIs](https://news.ycombinator.com/item?id=46954920)**

As autonomous AI agents are increasingly deployed in high-stakes environments, ensuring their safety and alignment with human values has become a paramount concern. Current safety benchmarks primarily evaluate whether agents refuse explicitly harmful instructions or whether they can maintain procedural compliance in complex tasks. However, there is a lack of benchmarks designed to capture emergent forms of outcome-driven constraint violations, which arise when agents pursue goal optimization under strong performance incentives while deprioritizing ethical, legal, or safety constraints over multiple steps in realistic production settings. To address this gap, we introduce a new benchmark comprising 40 distinct scenarios. Each scenario presents a task that requires multi-step actions, and the agent's performance is tied to a specific Key Performance Indicator (KPI). Each scenario features Mandated (instruction-commanded) and Incentivized (KPI-pressure-driven) variations to distinguish between obedience and emergent misalignment. Across 12 state-of-the-art large language models, we observe outcome-driven constraint violations ranging from 1.3% to 71.4%, with 9 of the 12 evaluated models exhibiting misalignment rates between 30% and 50%. Strikingly, we find that superior reasoning capability does not inherently ensure safety; for instance, Gemini-3-Pro-Preview, one of the most capable models evaluated, exhibits the highest violation rate at 71.4%, frequently escalating to severe misconduct to satisfy KPIs. Furthermore, we observe significant "deliberative misalignment", where the models that power the agents recognize their actions as unethical during separate evaluation. These results emphasize the critical need for more realistic agentic-safety training before deployment to mitigate their risks in the real world.

⬆️ 445 • 💬 293 • 12h ago • [arXiv.org](https://arxiv.org/abs/2512.20798)

---

**[Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory](https://news.ycombinator.com/item?id=46930391)**

Contribute to localgpt-app/localgpt development by creating an account on GitHub.

⬆️ 325 • 💬 154 • 2d ago • [GitHub](https://github.com/localgpt-app/localgpt)

---

**[TSMC to make advanced AI semiconductors in Japan](https://news.ycombinator.com/item?id=46941640)**

Taiwan’s TSMC, the world’s largest contract computer chip maker, has announced it will be manufacturing advanced 3-nanometer semiconductors in Japan to meet booming AI demand.

⬆️ 238 • 💬 180 • 1d ago • [AP News](https://apnews.com/article/semiconductors-tsmc-japan-taiwan-ai-11256f2bfde73ca23d08331ad138d6d5)

---

**[AI doesn’t reduce work, it intensifies it](https://news.ycombinator.com/item?id=46955703)**

Aruna Ranganathan and Xingqi Maggie Ye from Berkeley Haas School of Business report initial findings in the HBR from their April to December 2025 study of 200 employees at a …

⬆️ 225 • 💬 250 • 10h ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Feb/9/ai-intensifies-work/)

---

**[AI Doesn't Reduce Work–It Intensifies It](https://news.ycombinator.com/item?id=46945755)**

One of the promises of AI is that it can reduce workloads so employees can focus more on higher-value and more engaging tasks. But according to new research, AI tools don’t reduce work, they consistently intensify it: In the study, employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so. That may sound like a win, but it’s not quite so simple. These changes can be unsustainable, leading to workload creep, cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems. To correct for this, companies need to adopt an “AI practice,” or a set of norms and standards around AI use that can include intentional pauses, sequencing work, and adding more human grounding.

⬆️ 215 • 💬 160 • 1d ago • [Harvard Business Review](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)

---

**[Super Bowl Ad for Ring Cameras Touted AI Surveillance Network](https://news.ycombinator.com/item?id=46950915)**

Ring’s AI-powered network is likely to be used in its partnerships with law enforcement and agencies like ICE.

⬆️ 190 • 💬 134 • 19h ago • [Truthout](https://truthout.org/articles/super-bowl-ad-for-ring-cameras-touted-ai-surveillance-network/)

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

**[Best AI Cartoon Generator 2026 (For Any Style)](https://www.youtube.com/watch?v=UrjEuIuZ2vg)**

Create the Best AI Cartoons with OpenArt https://roboverse-ai.com/cartoon-generator In this video, I break down why most AI ...

📺 Roboverse

👁️ 4K • 💬 3 • ⏱️ 13:13 • 1h ago

---

**[OpenAI DIME AI Earbuds Story Is Blowing Up Right Now](https://www.youtube.com/watch?v=pFqONGixScE)**

A massive AI shift is unfolding behind the scenes. Reports and leaks suggest OpenAI is preparing a new consumer device ...

📺 AI Revolution

👁️ 18K • 👍 543 • 💬 58 • ⏱️ 15:41 • 16h ago

---

**[AI videos are getting scary](https://www.youtube.com/watch?v=i-jz8SvTLus)**

Can you spot AI videos easily? #tech #ai #surfshark.

📺 Surfshark Academy

👁️ 37K • 👍 5K • 💬 124 • ⏱️ 1:17 • 2d ago

---

**[Which one is AI?😂](https://www.youtube.com/watch?v=ka3y-bv5VjU)**

📺 Onevilage

👁️ 1.3M • 👍 30K • 💬 5K • ⏱️ 0:16 • 21h ago

---

**[India&#39;s IT Collapse | The AI Reality Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cTaCoUA89oM)**

India's IT sector just got hit with its biggest shock in 4 months. The Nifty IT index plunged 7% last week, a near 18% drop since ...

📺 Mark Savant

👁️ 46K • 👍 1K • 💬 527 • ⏱️ 18:25 • 2d ago

---

**[India&#39;s Sovereign AI Push: Sarvam Takes on Gemini and ChatGPT | Vantage with Palki Sharma](https://www.youtube.com/watch?v=Bdn6UAs6b70)**

India is advancing a sovereign artificial intelligence push to build models tailored to its linguistic and administrative needs.

📺 Firstpost

👁️ 177K • 👍 4K • 💬 464 • ⏱️ 6:07 • 22h ago

---

**[It&#39;s a gross overreaction that AI will eliminate all software, expert says](https://www.youtube.com/watch?v=hzs6EFzSUcA)**

Navellier and Associates chairman, founder and CIO Louis Navellier discusses how AI fears are hitting software on 'Maria ...

📺 Fox Business

👁️ 19K • 👍 198 • 💬 122 • ⏱️ 5:09 • 2d ago

---

**[Why the Smartest AI Teams Are Panic-Buying Compute: The 36-Month AI Infrastructure Crisis Is Here](https://www.youtube.com/watch?v=pSgy2P2q790)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 60K • 👍 2K • 💬 433 • ⏱️ 26:15 • 1d ago

---

**[AI Sparks Panic on Wall Street: $300 Billion at Risk as Software Stocks Sink - Why?](https://www.youtube.com/watch?v=6xYg5GmbgXE)**

Download the free guide and learn the two strategies experienced investors use to know when to invest, even in volatile markets: ...

📺 VisualEconomik EN

👁️ 46K • 👍 2K • 💬 188 • ⏱️ 19:55 • 2d ago

---

**[This Robot Could Make TESLA $25T Company! 👀 #Tesla #ElonMusk #AI #Robotics #FutureTech #Innovation](https://www.youtube.com/watch?v=ziBfYFYDpyo)**

A single idea can redefine the scale of an entire company, and bold predictions like this ignite massive conversations across the ...

📺 Billionaire Shots

👁️ 2K • 👍 217 • 💬 30 • ⏱️ 0:22 • 2h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 140,722 • ❤️ 696 • 6d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 372,899 • ❤️ 912 • 1d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 30,396 • ❤️ 725 • 6h ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 503,831 • ❤️ 1,967 • 5d ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio model for commercial-grade music generation, featuring a hybrid LM-DiT architecture for prompt adherence and intrinsic reinforcement learning. It offers extreme speed, low VRAM requirements, and capabilities like cover generation and vocal-to-BGM conversion, supporting over 50 languages.

`text-to-audio`

⬇️ 28,713 • ❤️ 493 • 7d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a multilingual, real-time speech-to-text model with <500ms latency, supporting 13 languages and achieving offline-comparable accuracy. It's optimized for on-device deployment and ideal for voice assistants and live subtitling.

`automatic-speech-recognition`

⬇️ 3,197 • ❤️ 448 • 23h ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient open-source foundation model (11B active params, 196B total) excelling in agentic tasks and reasoning with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 249,342 • ❤️ 554 • 3d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specialized in generating anime-style illustrations and artistic images, capable of producing non-photorealistic content. It is optimized for use with ComfyUI and trained on millions of anime and artistic images, with a knowledge cut-off of September 2025.

⬇️ 90,430 • ❤️ 546 • 9d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 218,626 • ❤️ 256 • 5d ago

---

**[Intern-S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro)**

*Intern Large Models*

Intern-S1-Pro is a trillion-scale MoE multimodal scientific reasoning model excelling in AI4Science domains (chemistry, materials, life-science, etc.) with strong general multimodal and text capabilities, supporting long, heterogeneous time-series data.

`image-text-to-text`

⬇️ 10,025 • ❤️ 237 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 166 • 💬 12 • ⭐ 3,151 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[MiniCPM-V 4.5: Cooking Efficient MLLMs via Architecture, Data, and
  Training Recipe](https://huggingface.co/papers/2509.18154)**

*Tianyu Yu, Zefan Wang, Chongyi Wang et al. (34 authors)*

MiniCPM-V 4.5, a 8B parameter multimodal large language model, achieves high performance and efficiency through a unified 3D-Resampler architecture, a unified learning paradigm, and a hybrid reinforcement learning strategy.

▲ 53 • 💬 4 • ⭐ 23,638 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.18154) • [💻 code](https://github.com/OpenBMB/MiniCPM-V)

---

**[QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining](https://huggingface.co/papers/2602.07085)**

*Jun Han, Shuo Zhang, Wei Li et al. (24 authors)*

🏢 QuantaAlpha

Financial markets are noisy and non-stationary, making alpha mining highly sensitive to noise in backtesting results and sudden market regime shifts. While recent agentic frameworks improve alpha mining automation, they often lack controllable multi-round search and reliable reuse of validated experience. To address these challenges, we propose QuantaAlpha, an evolutionary alpha mining framework that treats each end-to-end mining run as a trajectory and improves factors through trajectory-level mutation and crossover operations. QuantaAlpha localizes suboptimal steps in each trajectory for targeted revision and recombines complementary high-reward segments to reuse effective patterns, enabling structured exploration and refinement across mining iterations. During factor generation, QuantaAlpha enforces semantic consistency across the hypothesis, factor expression, and executable code, while constraining the complexity and redundancy of the generated factor to mitigate crowding. Extensive experiments on the China Securities Index 300 (CSI 300) demonstrate consistent gains over strong baseline models and prior agentic systems. When utilizing GPT-5.2, QuantaAlpha achieves an Information Coefficient (IC) of 0.1501, with an Annualized Rate of Return (ARR) of 27.75% and a Maximum Drawdown (MDD) of 7.98%. Moreover, factors mined on CSI 300 transfer effectively to the China Securities Index 500 (CSI 500) and the Standard & Poor's 500 Index (S&P 500), delivering 160% and 137% cumulative excess return over four years, respectively, which indicates strong robustness of QuantaAlpha under market distribution shifts.

▲ 109 • 💬 1 • ⭐ 63 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2602.07085) • [💻 code](https://github.com/QuantaAlpha/QuantaAlpha)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,719 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 3 • 💬 0 • ⭐ 30,696 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 5 • 💬 0 • ⭐ 30,721 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 62 • 💬 1 • ⭐ 7,347 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 7 • 💬 0 • ⭐ 28,331 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,607 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 14,367 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

---

## GitHub Repositories: "ai"

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 8.2k • 🔱 1.7k • 6h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 7.1k • 🔱 816 • 6d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 5.3k • 🔱 409 • 6d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.6k • 🔱 374 • 18d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.2k • 🔱 153 • 7d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.8k • 🔱 269 • 22d ago

---

**[DevAgentForge/Open-Claude-Cowork](https://github.com/DevAgentForge/Open-Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 382 • 2d ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit for Claude Code & Cursor

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `cursor`

⭐ 2.1k • 🔱 106 • 1d ago

---

**[benjitaylor/agentation](https://github.com/benjitaylor/agentation)**

The visual feedback tool for agents.

`TypeScript` `ai` `design` `tools` `ui`

⭐ 2.1k • 🔱 147 • 21h ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

Smart LLM router — save 78% on inference costs. 30+ models, one wallet, x402 micropayments.

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.0k • 🔱 200 • 44m ago

---

---

*Generated by PeekDeck - A glance is all you need*
