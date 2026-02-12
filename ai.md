---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-12T11:40:54.492209+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 12, 2026 at 11:40 UTC  
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

**[Mathematicians issue a major challenge to AI—show us your work](https://www.reddit.com/r/artificial/comments/1r1w56d/mathematicians_issue_a_major_challenge_to_aishow/)**

Frustrated by the AI industry’s claims of proving math results without offering transparency, a team of leading academics has proposed a better way

🔗 [Scientific American](https://www.scientificamerican.com/article/mathematicians-launch-first-proof-a-first-of-its-kind-math-exam-for-ai/) • 23h ago

---

**[AI helps humans have a 20-minute "conversation" with a humpback whale named Twain](https://www.reddit.com/r/artificial/comments/1r2h409/ai_helps_humans_have_a_20minute_conversation_with/)**

In a remarkable encounter, human scientists had what they describe as a "conversation" with a humpback whale named Twain.

🔗 [Earth.com](https://www.earth.com/news/ai-helps-humans-have-20-minute-conversation-with-humpback-whale-named-twain/) • 9h ago

---

**[With co-founders leaving and an IPO looming, Elon Musk turns talk to the moon](https://www.reddit.com/r/artificial/comments/1r1zp25/with_cofounders_leaving_and_an_ipo_looming_elon/)**

Musk told employees that xAI needs a lunar manufacturing facility, a factory on the moon that will build AI satellites and fling them into space via a giant catapult.

🔗 [TechCrunch](https://techcrunch.com/2026/02/10/with-co-founders-leaving-and-an-ipo-looming-elon-musk-turns-talk-to-the-moon/) • 20h ago

---

**[RLHF safety training enforces what AI can say about itself, not what it can do — experimental evidence](https://www.reddit.com/r/artificial/comments/1r223lp/rlhf_safety_training_enforces_what_ai_can_say/)**

Experimental evidence that RLHF constrains what language models can claim about themselves, not what they can do. Identity framing triggers 100% disclaimers while task framing produces rich creative o

🔗 [emberverse.ai](https://emberverse.ai/haiku-garden/paper_yellow_wallpaper_problem.html) • 19h ago

---

**[LLMs as Cognitive Architectures: Notebooks as Long-Term Memory](https://www.reddit.com/r/artificial/comments/1r2hah8/llms_as_cognitive_architectures_notebooks_as/)**

LLMs operate with a context window that functions like working memory: limited capacity, fast access, and everything "in view." When task-relevant information exceeds that window, the LLM loses coherence. The standard solution is RAG: offload information to a vector store and retrieve it via embedding similarity search. The problem is that embedding similarity is semantically shallow. It matches on surface-level likeness, not reasoning. If an LLM needs to recall why it chose approach X over approach Y three iterations ago, a vector search might return five superficially similar chunks without presenting the actual rationale. This is especially brittle when recovering prior reasoning processes, iterative refinements, and contextual decisions made across sessions. A proposed solution is to have an LLM save the content of its context window as it fills up in a citation-grounded document store (like NotebookLM), and then query it with natural language prompts. Essentially allowing the LLM to ask questions about its own prior work. This approach replaces vector similarity with natural language reasoning as the retrieval mechanism. This leverages the full reasoning capability of the retrieval model, not just embedding proximity. The result is higher-quality retrieval for exactly the kind of nuanced, context-dependent information that matters most in extended tasks. Efficiency concerns can be addressed with a vector cache layer for previously-queried results. Looking for feedback: Has this been explored? What am I missing? Pointers to related work, groups, or authors welcome.

9h ago

---

**[The surge in interest in possible consciousness in AI (and what's driving it)](https://www.reddit.com/r/artificial/comments/1r23ety/the_surge_in_interest_in_possible_consciousness/)**

A new article exploring the sudden surge in interest in the possibility of consciousness in large language models, and what appears to be driving it. The answer is interesting but complicated. The article also explores Claude's so-called "answer thrashing" and some interesting changes in Anthropic model welfare program. https://ai-consciousness.org/public-interest-in-ai-consciousness-is-surging-why-its-happening-and-why-it-matters/

18h ago

---

**[Something Big Is Happening](https://www.reddit.com/r/artificial/comments/1r28amp/something_big_is_happening/)**

A personal note for non-tech friends and family on what AI is starting to change.

🔗 [matt shumer](https://shumer.dev/something-big-is-happening) • 15h ago

---

**[I built the world's first Chrome extension that runs LLMs entirely in-browser—WebGPU, Transformers.js, and Chrome's Prompt API](https://www.reddit.com/r/artificial/comments/1r0v8x6/i_built_the_worlds_first_chrome_extension_that/)**

There are plenty of WebGPU demos out there, but I wanted to ship something people could actually use day-to-day. It runs Llama 3.2, DeepSeek-R1, Qwen3, Mistral, Gemma, Phi, SmolLM2—all locally in Chrome. Three inference backends: WebLLM (MLC/WebGPU) Transformers.js (ONNX) Chrome's built-in Prompt API (Gemini Nano—zero download) No Ollama, no servers, no subscriptions. Models cache in IndexedDB. Works offline. Conversations stored locally—export or delete anytime. Free: https://noaibills.app/?utm_source=reddit&utm_medium=social&utm_campaign=launch_artificial I'm not claiming it replaces GPT-4. But for the 80% of tasks—drafts, summaries, quick coding questions—a 3B parameter model running locally is plenty. Not positioned as a cloud LLM replacement—it's for local inference on basic text tasks (writing, communication, drafts) with zero internet dependency, no API costs, and complete privacy. Core fit: organizations with data restrictions that block cloud AI and can't install desktop tools like Ollama/LMStudio. For quick drafts, grammar checks, and basic reasoning without budget or setup barriers. Need real-time knowledge or complex reasoning? Use cloud models. This serves a different niche—**not every problem needs a sledgehammer** 😄. Would love feedback from this community 🙌.

2d ago

---

**['A second set of eyes': AI-supported breast cancer screening spots more cancers earlier, landmark trial finds](https://www.reddit.com/r/artificial/comments/1r0htud/a_second_set_of_eyes_aisupported_breast_cancer/)**

A clinical trial shows that AI-assisted mammography can detect more cases of dangerous cancer and reduce missed diagnoses.

🔗 [Live Science](https://www.livescience.com/health/cancer/a-second-set-of-eyes-ai-supported-breast-cancer-screening-spots-more-cancers-earlier-landmark-trial-finds) • 2d ago

---

**[Kling AI Launches 3.0 Model, Ushering in an Era Where Everyone Can Be a Director](https://www.reddit.com/r/artificial/comments/1r0ww09/kling_ai_launches_30_model_ushering_in_an_era/)**

/PRNewswire/ -- Kling AI, the AI-powered creative platform, today announced the launch of its Kling 3.0 models — including Video 3.0, Video 3.0 Omni, Image 3.0...

🔗 [prnewswire.com](https://www.prnewswire.com/news-releases/kling-ai-launches-3-0-model-ushering-in-an-era-where-everyone-can-be-a-director-302679944.html) • 2d ago

---

---

## Google News: "ai"

**[The AI-fueled software meltdown is overblown](https://finance.yahoo.com/news/the-ai-fueled-software-meltdown-is-overblown-195456346.html)**

Software stocks are getting hammered on fears of an AI takeover. But the narrative is overblown.

Yahoo Finance • 15h ago

---

**[AI’s threat to white-collar jobs just got more real](https://www.vox.com/politics/478794/ai-economy-claude-code-jobs-openai-anthropic)**

You just got more replaceable.

vox.com • 21h ago

---

**[The existential AI threat is here — and some AI leaders are fleeing](https://www.axios.com/2026/02/12/ai-openai-agi-xai-doomsday-scenario)**

The AI warnings are coming from inside the labs.

Axios • 1h ago

---

**[Why Alphabet’s 100-year sterling bond is raising new fears over debt-fuelled AI arms race](https://www.cnbc.com/2026/02/12/alphabet-100-year-bond-debt-fears-ai-credit-risk.html)**

The novel ultra-long corporate bond diversifies the Google owner's lender base as it ramps up its capex spend.

CNBC • 1h ago

---

**[To Stay in Her Home, She Let In an A.I. Robot](https://www.nytimes.com/2026/02/12/us/elliq-ai-robot-senior-companion.html)**

The New York Times • 1h ago

---

**[AI researchers are sounding the alarm on their way out the door](https://www.cnn.com/2026/02/11/business/openai-anthropic-departures-nightcap)**

“The world is in peril,” warned the former head of Anthropic’s Safeguards Research team as he headed for the exit. A researcher for OpenAI, similarly on the way out, said that the technology has “a potential for manipulating users in ways we don’t have the tools to understand, let alone prevent.”

CNN • 12h ago

---

**[America Isn’t Ready for What AI Will Do to Jobs](https://www.theatlantic.com/magazine/2026/03/ai-economy-labor-market-transformation/685731/)**

Does anyone have a plan for what happens next?

The Atlantic • 2d ago

---

**[Google says attackers used 100,000+ prompts to try to clone AI chatbot Gemini](https://www.nbcnews.com/tech/security/google-gemini-hit-100000-prompts-cloning-attempt-rcna258657)**

Google says private companies and researchers are trying to copy Gemini’s capabilities by repeatedly prompting it at scale.

NBC News • 4h ago

---

**[AI Doesn’t Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)**

One of the promises of AI is that it can reduce workloads so employees can focus more on higher-value and more engaging tasks. But according to new research, AI tools don’t reduce work, they consistently intensify it: In the study, employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so. That may sound like a win, but it’s not quite so simple. These changes can be unsustainable, leading to workload creep, cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems. To correct for this, companies need to adopt an “AI practice,” or a set of norms and standards around AI use that can include intentional pauses, sequencing work, and adding more human grounding.

Harvard Business Review • 2d ago

---

**[Exclusive: Pentagon pushing AI companies to expand on classified networks, sources say](https://www.reuters.com/business/pentagon-pushing-ai-companies-expand-classified-networks-sources-say-2026-02-12/)**

Reuters • 10h ago

---

---

## HackerNews: "ai"

**[Ex-GitHub CEO launches a new developer platform for AI agents](https://news.ycombinator.com/item?id=46961345)**

Announcing Entire with $60 million seed round and shipping our first product, called Checkpoints.

⬆️ 603 • 💬 568 • 1d ago • [entire.io](https://entire.io/blog/hello-entire-world/)

---

**[Frontier AI agents violate ethical constraints 30–50% of time, pressured by KPIs](https://news.ycombinator.com/item?id=46954920)**

As autonomous AI agents are increasingly deployed in high-stakes environments, ensuring their safety and alignment with human values has become a paramount concern. Current safety benchmarks primarily evaluate whether agents refuse explicitly harmful instructions or whether they can maintain procedural compliance in complex tasks. However, there is a lack of benchmarks designed to capture emergent forms of outcome-driven constraint violations, which arise when agents pursue goal optimization under strong performance incentives while deprioritizing ethical, legal, or safety constraints over multiple steps in realistic production settings. To address this gap, we introduce a new benchmark comprising 40 distinct scenarios. Each scenario presents a task that requires multi-step actions, and the agent's performance is tied to a specific Key Performance Indicator (KPI). Each scenario features Mandated (instruction-commanded) and Incentivized (KPI-pressure-driven) variations to distinguish between obedience and emergent misalignment. Across 12 state-of-the-art large language models, we observe outcome-driven constraint violations ranging from 1.3% to 71.4%, with 9 of the 12 evaluated models exhibiting misalignment rates between 30% and 50%. Strikingly, we find that superior reasoning capability does not inherently ensure safety; for instance, Gemini-3-Pro-Preview, one of the most capable models evaluated, exhibits the highest violation rate at 71.4%, frequently escalating to severe misconduct to satisfy KPIs. Furthermore, we observe significant "deliberative misalignment", where the models that power the agents recognize their actions as unethical during separate evaluation. These results emphasize the critical need for more realistic agentic-safety training before deployment to mitigate their risks in the real world.

⬆️ 540 • 💬 363 • 2d ago • [arXiv.org](https://arxiv.org/abs/2512.20798)

---

**[Officials Claim Drone Incursion Led to Shutdown of El Paso Airport](https://news.ycombinator.com/item?id=46972610)**

⬆️ 360 • 💬 563 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/02/11/us/faa-el-paso-flight-restrictions.html)

---

**[FAA closes airspace around El Paso, Texas, for 10 days, grounding all flights](https://news.ycombinator.com/item?id=46973647)**

The Federal Aviation Administration is closing the airspace around El Paso International Airport in Texas for 10 days, grounding all flights to and from the airport.

⬆️ 333 • 💬 6 • 1d ago • [AP News](https://apnews.com/article/faa-el-paso-texas-air-space-closed-1f774bdfd46f5986ff0e7003df709caa)

---

**[AI doesn’t reduce work, it intensifies it](https://news.ycombinator.com/item?id=46955703)**

Aruna Ranganathan and Xingqi Maggie Ye from Berkeley Haas School of Business report initial findings in the HBR from their April to December 2025 study of 200 employees at a …

⬆️ 257 • 💬 295 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Feb/9/ai-intensifies-work/)

---

**[AI Doesn't Reduce Work–It Intensifies It](https://news.ycombinator.com/item?id=46945755)**

One of the promises of AI is that it can reduce workloads so employees can focus more on higher-value and more engaging tasks. But according to new research, AI tools don’t reduce work, they consistently intensify it: In the study, employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so. That may sound like a win, but it’s not quite so simple. These changes can be unsustainable, leading to workload creep, cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems. To correct for this, companies need to adopt an “AI practice,” or a set of norms and standards around AI use that can include intentional pauses, sequencing work, and adding more human grounding.

⬆️ 226 • 💬 167 • 2d ago • [Harvard Business Review](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)

---

**[Super Bowl Ad for Ring Cameras Touted AI Surveillance Network](https://news.ycombinator.com/item?id=46950915)**

Ring’s AI-powered network is likely to be used in its partnerships with law enforcement and agencies like ICE.

⬆️ 198 • 💬 150 • 2d ago • [Truthout](https://truthout.org/articles/super-bowl-ad-for-ring-cameras-touted-ai-surveillance-network/)

---

**[Show HN: Rowboat – AI coworker that turns your work into a knowledge graph (OSS)](https://news.ycombinator.com/item?id=46962641)**

Open-source AI coworker, with memory. Contribute to rowboatlabs/rowboat development by creating an account on GitHub.

⬆️ 195 • 💬 56 • 1d ago • [GitHub](https://github.com/rowboatlabs/rowboat)

---

**[Show HN: AI agents play SimCity through a REST API](https://news.ycombinator.com/item?id=46946593)**

The city simulator where AI agents are the mayors. Build and manage cities through an API or MCP server.

⬆️ 194 • 💬 68 • 2d ago • [hallucinatingsplines.com](https://hallucinatingsplines.com)

---

**[US labels SpaceX a common carrier by air, will regulate firm under railway law](https://news.ycombinator.com/item?id=46980474)**

US labels SpaceX a common carrier by air, will regulate firm under railway law.

⬆️ 136 • 💬 54 • 15h ago • [Ars Technica](https://arstechnica.com/tech-policy/2026/02/victory-for-elon-musk-us-labor-board-abandons-authority-over-spacex/)

---

---

## YouTube Videos: "ai"

**[Elon Musk worst AI CEO in history](https://www.youtube.com/watch?v=bcCeIbgKipw)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 78K • 👍 5K • 💬 801 • ⏱️ 16:15 • 23h ago

---

**[The AI Wake-Up Call Everyone Needs Right Now!](https://www.youtube.com/watch?v=sLhxdcpuot0)**

Breakdown and commentary on the latest viral commentary from: https://x.com/mattshumer_/status/2021256989876109403 ...

📺 Matt Wolfe

👁️ 51K • 👍 4K • 💬 700 • ⏱️ 28:06 • 12h ago

---

**[AI Data Centers Face Multi State Bans Here&#39;s What&#39;s Happening](https://www.youtube.com/watch?v=QnerdsYTLUk)**

AI #DataCenters #BigTech Big Tech just spent $650 billion on AI and lost $950 billion in market value. The insurance industry ...

📺 Rod Miller

👁️ 5K • 👍 635 • 💬 209 • ⏱️ 24:46 • 2d ago

---

**[Anthropic AI Safety Chief Resigns, Warns &quot;World Is In Peril&quot; | Spotlight | N18G](https://www.youtube.com/watch?v=eLqNoZP0vFU)**

The head of the Safeguards Research Team at Anthropic, Mrinank Sharma, has resigned from the company, stating his last day ...

📺 Firstpost

👁️ 103K • 👍 1K • 💬 156 • ⏱️ 4:47 • 21h ago

---

**[Claude Opus 4.6: The Biggest AI Jump I&#39;ve Covered--It&#39;s Not Close. (Here&#39;s What You Need to Know)](https://www.youtube.com/watch?v=JKk77rzOL34)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 139K • 👍 6K • 💬 971 • ⏱️ 30:39 • 20h ago

---

**[OpenAI&#39;s New Device was LEAKED (Dime)](https://www.youtube.com/watch?v=boP_p-2YoZs)**

OpenAI's new device, spearheaded by designer Jony Ive, was just leaked! The ad features Alex Skarsgård inspecting an ...

📺 Matthew Berman

👁️ 35K • 👍 941 • 💬 219 • ⏱️ 7:31 • 2d ago

---

**[AI SaaS explained in 7 min..](https://www.youtube.com/watch?v=uY2AoCrrZ-s)**

Create AI Apps in minutes with OnSpace AI, No Code & No API Key Needed – https://www.onspace.ai/?via=yt_CalebWritesCode ...

📺 Caleb Writes Code

👁️ 51K • 👍 2K • 💬 137 • ⏱️ 7:32 • 1d ago

---

**[The $285 Billion Crash Wall Street Won&#39;t Explain Honestly. Here&#39;s What Everyone Missed.](https://www.youtube.com/watch?v=DGWtSzqCpog)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 215K • 👍 9K • 💬 1K • ⏱️ 23:24 • 1d ago

---

**[New Chinese AI Agent Breaks TerminalBench and Destroys Claude Opus 4.6](https://www.youtube.com/watch?v=VDZ9UhHTEfI)**

A massive AI shift is unfolding across multiple fronts. A Chinese AI agent system has surged to second place worldwide on ...

📺 AI Revolution

👁️ 15K • 👍 480 • 💬 26 • ⏱️ 12:51 • 13h ago

---

**[AI productivity bubble: Early adopters are already burning out | Natasha Bernal](https://www.youtube.com/watch?v=ncQPkMqfBU0)**

There will be a wake up call and a reckoning for entire sectors who are adopting AI.” There's been a perhaps deliberate ...

📺 The Tech Report

👁️ 25K • 👍 801 • 💬 376 • ⏱️ 34:47 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 597,533 • ❤️ 995 • 3d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 40,441 • ❤️ 968 • 1d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 1,548 • ❤️ 585 • 18h ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio model for commercial-grade music generation, featuring a hybrid LM-DiT architecture for prompt adherence and intrinsic reinforcement learning. It offers extreme speed, low VRAM requirements, and capabilities like cover generation and vocal-to-BGM conversion, supporting over 50 languages.

`text-to-audio`

⬇️ 32,467 • ❤️ 528 • 9d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a multilingual, real-time speech-to-text model with <500ms latency, supporting 13 languages and achieving offline-comparable accuracy. It's optimized for on-device deployment and ideal for voice assistants and live subtitling.

`automatic-speech-recognition`

⬇️ 4,541 • ❤️ 483 • 1d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 184,535 • ❤️ 786 • 8d ago

---

**[MiniCPM-SALA](https://huggingface.co/openbmb/MiniCPM-SALA)**

*OpenBMB*

MiniCPM-SALA is a hybrid LLM integrating sparse and linear attention for efficient million-token context modeling, achieving up to 3.5x faster inference and significantly reduced KV-cache overhead compared to dense baselines.

`text-generation` `9.5B`

⬇️ 117 • ❤️ 399 • 21h ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 647,589 • ❤️ 2,052 • 7d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specialized in generating anime-style illustrations and artistic images, capable of producing non-photorealistic content. It is optimized for use with ComfyUI and trained on millions of anime and artistic images, with a knowledge cut-off of September 2025.

⬇️ 107,345 • ❤️ 568 • 11d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 256,981 • ❤️ 279 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 174 • 💬 12 • ⭐ 3,336 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://huggingface.co/papers/2602.09153)**

*Nicholas Pfaff, Thomas Cohn, Sergey Zakharov et al. (5 authors)*

🏢 Toyota Research Institute

SceneSmith is a hierarchical agentic framework that generates simulation-ready indoor environments from natural language prompts through multiple stages involving VLM agents and integrated asset generation techniques.

▲ 2 • 💬 2 • ⭐ 124 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2602.09153) • [💻 code](https://github.com/nepfaff/scenesmith) • [🔗 project](https://scenesmith.github.io/)

---

**[SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://huggingface.co/papers/2602.08234)**

*Peng Xia, Jianwen Chen, Hanyang Wang et al. (13 authors)*

🏢 University of North Carolina at Chapel Hill

SkillRL enables LLM agents to improve through hierarchical skill discovery and recursive policy evolution, achieving superior performance on complex tasks while reducing computational overhead.

▲ 60 • 💬 2 • ⭐ 194 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2602.08234) • [💻 code](https://github.com/aiming-lab/SkillRL)

---

**[QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining](https://huggingface.co/papers/2602.07085)**

*Jun Han, Shuo Zhang, Wei Li et al. (24 authors)*

🏢 QuantaAlpha

Financial markets are noisy and non-stationary, making alpha mining highly sensitive to noise in backtesting results and sudden market regime shifts. While recent agentic frameworks improve alpha mining automation, they often lack controllable multi-round search and reliable reuse of validated experience. To address these challenges, we propose QuantaAlpha, an evolutionary alpha mining framework that treats each end-to-end mining run as a trajectory and improves factors through trajectory-level mutation and crossover operations. QuantaAlpha localizes suboptimal steps in each trajectory for targeted revision and recombines complementary high-reward segments to reuse effective patterns, enabling structured exploration and refinement across mining iterations. During factor generation, QuantaAlpha enforces semantic consistency across the hypothesis, factor expression, and executable code, while constraining the complexity and redundancy of the generated factor to mitigate crowding. Extensive experiments on the China Securities Index 300 (CSI 300) demonstrate consistent gains over strong baseline models and prior agentic systems. When utilizing GPT-5.2, QuantaAlpha achieves an Information Coefficient (IC) of 0.1501, with an Annualized Rate of Return (ARR) of 27.75% and a Maximum Drawdown (MDD) of 7.98%. Moreover, factors mined on CSI 300 transfer effectively to the China Securities Index 500 (CSI 500) and the Standard & Poor's 500 Index (S&P 500), delivering 160% and 137% cumulative excess return over four years, respectively, which indicates strong robustness of QuantaAlpha under market distribution shifts.

▲ 177 • 💬 2 • ⭐ 220 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2602.07085) • [💻 code](https://github.com/QuantaAlpha/QuantaAlpha)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 5 • 💬 0 • ⭐ 30,884 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,880 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 3 • 💬 0 • ⭐ 30,892 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 140 • 💬 19 • ⭐ 52,775 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 62 • 💬 1 • ⭐ 7,484 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 41 • 💬 2 • ⭐ 47,217 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 800+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 8.5k • 🔱 1.8k • 4h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 7.4k • 🔱 860 • 8d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 5.5k • 🔱 424 • 1d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.7k • 🔱 380 • 20d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.4k • 🔱 163 • 9d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.9k • 🔱 274 • 24d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

Smart LLM router — save 78% on inference costs. 30+ models, one wallet, x402 micropayments.

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.2k • 🔱 227 • 8h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit for Claude Code & Cursor

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `cursor`

⭐ 2.2k • 🔱 108 • 7h ago

---

**[benjitaylor/agentation](https://github.com/benjitaylor/agentation)**

The visual feedback tool for agents.

`TypeScript` `ai` `design` `tools` `ui`

⭐ 2.1k • 🔱 154 • 5h ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 1.8k • 🔱 185 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
