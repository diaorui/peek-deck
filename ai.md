---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-06T13:38:12.540661+00:00'
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

**Last Updated:** January 06, 2026 at 13:38 UTC  
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

**[Harvard just proved AI tutors beat classrooms. Now what?](https://www.reddit.com/r/artificial/comments/1q4t8b5/harvard_just_proved_ai_tutors_beat_classrooms_now/)**

Looking for some advice and different opinions. I have been following the AI in education space for a while and wanted to share some research that's been on my mind. Harvard researchers ran a randomized controlled trial (N=194) comparing physics students learning from an AI tutor vs an active learning classroom. Published in Nature Scientific Reports in June 2025. Results: AI group more than doubled their learning gains. Spent less time. Reported feeling more engaged and motivated. Important note: This wasn't just ChatGPT. They engineered the AI to follow pedagogical best practices - scaffolding, cognitive load management, immediate personalized feedback, self-pacing. The kind of teaching that doesn't scale with one human and 30 students. Now here's where it gets interesting (and concerning). UNESCO projects the world needs 44 million additional teachers by 2030. Sub-Saharan Africa alone needs 15 million. The funding and humans simply aren't there. AI tutoring seems like the obvious solution. Infinite patience. Infinite personalization. Near-zero marginal cost. But: 87% of students in high-income countries have home internet access. In low-income countries? 6%. 2.6 billion people globally are still offline. The AI tutoring market is booming in North America, Europe, and Asia-Pacific. The regions that need educational transformation most are least equipped to access it. So we're facing a fork: AI either democratizes world-class education for everyone, or it creates a two-tier system that widens inequality. The technology is proven. The question is policy and infrastructure investment. Curious what this community thinks about the path forward. Sources: Kestin et al., Nature Scientific Reports (June 2025) UNESCO Global Report on Teachers (2024) UNESCO Global Education Monitoring Report (2023)

19h ago

---

**[Nvidia Launches Alpamayo AI for Human-Like Autonomous Driving](https://www.reddit.com/r/artificial/comments/1q57fru/nvidia_launches_alpamayo_ai_for_humanlike/)**

Nvidia introduces Alpamayo, an open AI model that gives autonomous vehicles human-like reasoning to handle complex driving scenarios safely.

🔗 [techputs](https://techputs.com/nvidia-alpamayo-ai-autonomous-vehicles/) • 10h ago

---

**[Nvidia just provided a closer look at its new computing platform for AI data centers, Vera Rubin](https://www.reddit.com/r/artificial/comments/1q511qj/nvidia_just_provided_a_closer_look_at_its_new/)**

Nvidia just provided a closer look at its new computing platform for AI data centers, Vera Rubin, a release that could have major ramifications for the future of AI given the industry’s massive reliance on the company’s tech.

🔗 [CNN](https://www.cnn.com/2026/01/05/tech/vera-rubin-nvidia-ai-ces?utm_medium=social&utm_campaign=missions&utm_source=reddit) • 14h ago

---

**[Connect any LLM to all your knowledge sources and chat with it](https://www.reddit.com/r/artificial/comments/1q5h29v/connect_any_llm_to_all_your_knowledge_sources_and/)**

For those of you who aren't familiar with SurfSense, it aims to be OSS alternative to NotebookLM, Perplexity, and Glean. In short, Connect any LLM to your internal knowledge sources (Search Engines, Drive, Calendar, Notion and 15+ other connectors) and chat with it in real time alongside your team. I'm looking for contributors. If you're interested in AI agents, RAG, browser extensions, or building open-source research tools, this is a great place to jump in. Here's a quick look at what SurfSense offers right now: Features Deep Agentic Agent RBAC (Role Based Access for Teams) Supports 100+ LLMs Supports local Ollama or vLLM setups 6000+ Embedding Models 50+ File extensions supported (Added Docling recently) Local TTS/STT support. Connects with 15+ external sources such as Search Engines, Slack, Notion, Gmail, Notion, Confluence etc Cross-Browser Extension to let you save any dynamic webpage you want, including authenticated content. Upcoming Planned Features Multi Collaborative Chats Multi Collaborative Documents Real Time Features GitHub: https://github.com/MODSetter/SurfSense

1h ago

---

**[Experimenting with image based location reasoning using architectural cues](https://www.reddit.com/r/artificial/comments/1q5fzea/experimenting_with_image_based_location_reasoning/)**

I am building an experimental AI tool that analyzes images to suggest real world location by detecting architectural and design elements and explaining why those cues point to a specific place. I tested it on a public image with a known location and recorded a short video showing the reasoning process. The output was close but imperfect, which is expected at this stage. I am mainly interested in whether explanation driven reasoning makes these systems more useful and interpretable.

2h ago

---

**[One-Minute Daily AI News 1/5/2026](https://www.reddit.com/r/artificial/comments/1q5995k/oneminute_daily_ai_news_152026/)**

AMD reveals new AI PC chips, details next-gen data center chips at CES 2026.[1] NVIDIA Announces Alpamayo Family of Open-Source AI Models and Tools to Accelerate Safe, Reasoning-Based Autonomous Vehicle Development.[2] Alexa.com rolls out to all Alexa+ Early Access customers, bringing the power of Alexa+ to your browser.[3] MIT scientists investigate memorization risk in the age of clinical AI.[4] Sources: [1] https://finance.yahoo.com/news/amd-reveals-new-ai-pc-chips-details-next-gen-data-center-chips-at-ces-2026-041117636.html [2] https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development [3] https://www.aboutamazon.com/news/devices/alexa-plus-web-ai-assistant [4] https://news.mit.edu/2026/mit-scientists-investigate-memorization-risk-clinical-ai-0105

8h ago

---

**[I built Ctrl: Execution control plane for high stakes agentic systems](https://www.reddit.com/r/artificial/comments/1q5f6kf/i_built_ctrl_execution_control_plane_for_high/)**

I built Ctrl, an open-source execution control plane that sits between an agent and its tools. Instead of letting tool calls execute directly, Ctrl intercepts them, dynamically scores risk, applies policy (allow / deny / approve), and only then executes; recording every intent, decision, and event in a local SQLite ledger. GH: https://github.com/MehulG/agent-ctrl It’s currently focused on LangChain + MCP as a drop-in wrapper. The demo shows a content publish action being intercepted, paused for approval, and replayed safely after approval. I’d love feedback from anyone running agents that take real actions.

3h ago

---

**[We're so blinded by the AI Hype That We're Failing to See What Could Actually Be on the Horizon](https://www.reddit.com/r/artificial/comments/1q4pbsd/were_so_blinded_by_the_ai_hype_that_were_failing/)**

AI hype and the bubble that will follow are real, but it's also distorting our views of what the future could entail with current capabilities. Here's a sobering breakdown of what we can reasonably expect without going too far off the Sci-Fi rails.

🔗 [open.substack.com](https://open.substack.com/pub/storyprism/p/a-coherent-future?utm_campaign=post-expanded-share&utm_medium=web) • 21h ago

---

**[AI - Why Shouldn't We Use It?](https://www.reddit.com/r/artificial/comments/1q54yza/ai_why_shouldnt_we_use_it/)**

I'm new to this sub. I was hoping to converse a little and get some opinions on this. I think it's an interesting phenomena within our society at the moment, where if you think about AI as a tool, and I personally see it as the greatest tool ever invented/gifted to mankind, why, or what is the issue, with using it? You see it all throughout society. People are up in arms about students using it to write papers is a big one, and I wonder, did papers ever need to be written in the first place? I apologize if this has already been answered to the nth degree and been beaten into the dirt, but realistically wouldn't it be possible that the ideas supporting this non-use of AI are rooted in established organizations that stand to suffer when they are completely obliterated by a tool that can not only do what they do but do it instantly and always be readily available, and do it for free? This narrative that we shouldn't use a tool that we've discovered/invented/been given or whatever you wanna call it, to me, seems absurd. It'd be like if we invented fire and everyone was like, hey, don't cook the meat, fire is stupid, let's just raw dog. I digress. My point is, maybe, MAYBE, the people who are pushing that narrative to not use AI, to not embrace this tool, to not see it as our potential salvation (or destruction XD), or at the very least even be curious about its potential applications and possible benefits to our society, stand to LOSE THEIR ASSES by its implementation. Just maybe. Sorry if I broke any rules, I am a big dumbass. Thanks for your time.

12h ago

---

**[AI that connects users with similar interests by chatting with them first. good idea or privacy nightmare?](https://www.reddit.com/r/artificial/comments/1q4l0i1/ai_that_connects_users_with_similar_interests_by/)**

Hey everyone, I’ve been thinking about an idea and wanted some honest feedback. Imagine an AI that people use mainly for casual chatting and asking random questions (kind of like a personal assistant / chatbot). Over time, the AI learns a user’s interests, tastes, and goals through natural conversation not just profile fields. Now here’s the twist: If the AI detects that two users have strong overlap in interests (for example, same hobbies, learning goals, or things they like talking about), it suggests an introduction. The AI doesn’t auto-connect people, it asks for consent first and explains why it thinks the match makes sense. The goal isn’t dating specifically,more like helping people: find learning buddies project collaborators accountability partners or just people with similar interests I’m curious about a few things: What are the biggest pros you see in something like this? What are the major risks or downsides (privacy, creepiness, bad matches, etc.)? Does something like this already exist in a solid way? If yes, what did they do right or wrong? Would you personally trust an AI to suggest connections based on private conversations? I’m not pitching a startup, just trying to sanity-check the concept and understand whether this solves a real problem or creates new ones. Looking forward to brutally honest opinions.

1d ago

---

---

## Google News: "ai"

**[Leading AI expert delays timeline for its possible destruction of humanity | AI (artificial intelligence)](https://www.theguardian.com/technology/2026/jan/06/leading-ai-expert-delays-timeline-possible-destruction-humanity)**

Former OpenAI employee Daniel Kokotajlo says progress to AGI is ‘somewhat slower’ than first predicted

The Guardian • 7h ago

---

**[Nvidia launches Vera Rubin, its next major AI platform, at CES 2026](https://finance.yahoo.com/news/nvidia-launches-vera-rubin-its-next-major-ai-platform-at-ces-2026-230045205.html)**

Nvidia launched its latest Vera Rubin superchip at CES 2026 on Monday.

Yahoo Finance • 14h ago

---

**[Grok AI still being used to digitally undress women and children despite suspension pledge](https://www.theguardian.com/technology/2026/jan/05/elon-musk-grok-ai-digitally-undress-images-of-women-children)**

The degrading pictures are being posted to X despite the platform pledging to suspend people who generate them

The Guardian • 18h ago

---

**[Elon Musk's chatbot bikini image edits draw scrutiny from U.S. and global regulators](https://www.axios.com/2026/01/06/grok-ai-elon-musk-deepfake-bikini)**

Axios • 2h ago

---

**[European Commission calls Grok's sexualised AI photos 'illegal,' Britain demands answers](https://www.reuters.com/business/media-telecom/britain-demands-elon-musks-grok-answers-concerns-about-sexualised-photos-2026-01-05/)**

Reuters • 17h ago

---

**[Should workers be worried about AI taking their jobs? Ask Johnny](https://www.usatoday.com/story/money/columnist/2026/01/06/should-employees-worry-ai-taking-jobs/87974979007/)**

Artificial intelligence isn’t coming for your job ‒ but someone who knows how to use AI might.

USA Today • 1h ago

---

**[Timekettle Reveals a Major Upgrade to Its Real-Time, In-Ear AI Translation Technology at CES 2026](https://gizmodo.com/timekettles-real-time-in-ear-ai-translation-tech-just-got-a-massive-upgrade-2000705424)**

The Babel fish real-time translator is becoming a reality.

Gizmodo • 1h ago

---

**[Experienced software developers assumed AI would save them a chunk of time. But in one experiment, their tasks took 20% longer](https://fortune.com/article/does-ai-increase-workplace-productivity-experiment-software-developers-task-took-longer/)**

As more workers use AI, a recent study adds to growing evidence the tech doesn’t always deliver on promises of boosted productivity.

Fortune • 21h ago

---

**[An AI revolution in drugmaking is under way](https://www.economist.com/science-and-technology/2026/01/05/an-ai-revolution-in-drugmaking-is-under-way)**

The Economist • 21h ago

---

**[AI godfather says Meta’s new 29-year-old AI boss is ‘inexperienced’ and warns of staff exodus](https://www.cnbc.com/2026/01/05/ai-godfather-calls-meta-ai-boss-alexander-wang-inexperienced-.html)**

"A lot of people have left, a lot of people who haven't yet left will leave," Meta's former chief AI scientist Yann Lecun said.

CNBC • 21h ago

---

---

## HackerNews: "ai"

**[All AI Videos Are Harmful (2025)](https://news.ycombinator.com/item?id=46498651)**

When OpenAI released the first version of Sora, I was excited. For years, I'd had this short story sitting on my hard drive, something I'd written long ago and always dreamed of bringing to life as a

⬆️ 304 • 💬 311 • 23h ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/all-ai-videos-are-harmful)

---

**[Eurostar AI vulnerability: When a chatbot goes off the rails](https://news.ycombinator.com/item?id=46492063)**

TL;DR  Introduction  I first encountered the chatbot as a normal Eurostar customer while planning a trip. When it opened, it clearly told me that “the answers in this chatbot are generated by AI”, which is good disclosure but immediately raised my curiosity about how it worked and what its limits were. Eurostar publishes a […]

⬆️ 206 • 💬 48 • 1d ago • [Pen Test Partners](https://www.pentestpartners.com/security-blog/eurostar-ai-vulnerability-when-a-chatbot-goes-off-the-rails/)

---

**[Why didn't AI “join the workforce” in 2025?](https://news.ycombinator.com/item?id=46505735)**

Exactly one year ago, Sam Altman ​made a bold prediction​: “We believe that, in 2025, we may see the first AI agents ‘join the workforce’ ... Read more

⬆️ 156 • 💬 219 • 15h ago • [Cal Newport](https://calnewport.com/why-didnt-ai-join-the-workforce-in-2025/)

---

**[Building a Rust-style static analyzer for C++ with AI](https://news.ycombinator.com/item?id=46495539)**

⬆️ 92 • 💬 58 • 1d ago • [Home](http://mpaxos.com/blog/rusty-cpp.html)

---

**[Boston Dynamics and DeepMind form new AI partnership](https://news.ycombinator.com/item?id=46504966)**

A new robotics partnership aims to combine Boston Dynamics’ athletic intelligence with Google DeepMind’s foundational capabilities

⬆️ 90 • 💬 46 • 16h ago • [Boston Dynamics](https://bostondynamics.com/blog/boston-dynamics-google-deepmind-form-new-ai-partnership/)

---

**[Microsoft CEO resorts to blogging in defense of AI](https://news.ycombinator.com/item?id=46489890)**

Surely it works this time

⬆️ 66 • 💬 72 • 1d ago • [GamesRadar+](https://www.gamesradar.com/games/microsoft-ceo-resorts-to-blogging-in-defense-of-ai-says-we-need-to-get-beyond-the-arguments-of-slop-exactly-what-id-say-if-i-was-tired-of-losing-the-arguments-of-slop/)

---

**[AI sycophancy panic](https://news.ycombinator.com/item?id=46488396)**

Conversational AI benchmark. Contribute to firasd/vibesbench development by creating an account on GitHub.

⬆️ 56 • 💬 102 • 1d ago • [GitHub](https://github.com/firasd/vibesbench/blob/main/docs/ai-sycophancy-panic.md)

---

**[Developing a BLAS Library for the AMD AI Engine [pdf]](https://news.ycombinator.com/item?id=46483811)**

⬆️ 46 • 💬 11 • 2d ago • [uni.tlaan.nl](https://uni.tlaan.nl/thesis/msc_thesis_tristan_laan_aieblas.pdf)

---

**[Amazon Prime AI overviews can't even get the basics right](https://news.ycombinator.com/item?id=46508324)**

⬆️ 38 • 💬 6 • 10h ago

---

**[That viral Reddit post about food delivery apps was an AI scam](https://news.ycombinator.com/item?id=46503492)**

AI slop comes for Reddit.

⬆️ 34 • 💬 40 • 18h ago • [The Verge](https://www.theverge.com/news/855328/viral-reddit-delivery-app-ai-scam)

---

---

## YouTube Videos: "ai"

**[Progress made on AI-powered humanoid robots | 60 Minutes](https://www.youtube.com/watch?v=CbHeh7qwils)**

Engineers and computer scientists are developing AI-powered robots that look and act human. Boston Dynamics invited 60 ...

📺 60 Minutes

👁️ 675K • 👍 10K • 💬 2K • ⏱️ 13:17 • 1d ago

---

**[This AI Solves The No Code Problem (Rocket)](https://www.youtube.com/watch?v=S2MP49Xr9PI)**

Rocket is a new AI platform that quietly finishes what every no-code builder started but never completed. It doesn't give you ...

📺 AI Revolution

👁️ 12K • 👍 499 • 💬 30 • ⏱️ 8:40 • 14h ago

---

**[At CES 2026, AI Takes Over Las Vegas](https://www.youtube.com/watch?v=nuivRxby208)**

The world's largest tech show is back and AI is powering nearly every major reveal. Here's your first look! Connect with Cheddar!

📺 Cheddar

👁️ 9K • 👍 108 • 💬 9 • ⏱️ 3:36 • 21h ago

---

**[New OpenAI GUMDROP AI Device Turns ChatGPT Physical](https://www.youtube.com/watch?v=cfFCmVVflfk)**

OpenAI is quietly building its first real consumer hardware product, and it changes everything about how people access AI.

📺 AI Revolution

👁️ 86K • 👍 2K • 💬 362 • ⏱️ 11:17 • 1d ago

---

**[Elon Musk: “We Hit AI Singularity” – Is He Bluffing?](https://www.youtube.com/watch?v=2hBj1UIJfqE)**

Support me by subscribing to the Thomas AI channel https://www.youtube.com/@thomas-ai-en?sub_confirmation=1 and ...

📺 Thomas AI 🇺🇸

👁️ 3K • 👍 26 • 💬 38 • ⏱️ 15:04 • 1d ago

---

**[This NEW 1-Click AI Agent is INSANE! 🤯](https://www.youtube.com/watch?v=G3ka1hVasGg)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses https://juliangoldieai.com/07L1kg Get a ...

📺 Julian Goldie SEO

👁️ 3K • 👍 107 • 💬 8 • ⏱️ 9:18 • 16h ago

---

**[He&#39;s Crying Over People Being Mean About AI](https://www.youtube.com/watch?v=s1Dzr5S06ek)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Our soap ...

📺 penguinz0

👁️ 1.4M • 👍 72K • 💬 7K • ⏱️ 11:20 • 2d ago

---

**[How to Start a 1-Person AI Business (With Zero Code)](https://www.youtube.com/watch?v=ar9JCsiq6hs)**

Get your FREE Sell by Chat Playbook here: https://go.danmartell.com/4aiAhhb Are you building an AI software company?

📺 Dan Martell

👁️ 123K • 👍 5K • 💬 339 • ⏱️ 30:25 • 2d ago

---

**[&#39;Grok Allowing Users To Undress..&quot;: India, France Move Against Musk’s Grok AI Over Obscenity](https://www.youtube.com/watch?v=Ii_zXBBiqmE)**

Governments in India and France have initiated formal action against Elon Musk's X after complaints over how its Grok AI tool is ...

📺 Mint

👁️ 42K • 👍 571 • 💬 366 • ⏱️ 3:33 • 3d ago

---

**[Which one is AI? Level: Impossible 🔍 Cre: @SofiManassyan #shorts](https://www.youtube.com/watch?v=DV3fi0tS2U4)**

📺 Julee Cook

👁️ 654K • 👍 18K • 💬 2K • ⏱️ 0:11 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)**

*Qwen*

Qwen-Image-2512 is a text-to-image diffusion model that excels at generating highly realistic human subjects and detailed natural scenes. It offers improved text rendering and composition, making it suitable for applications requiring high fidelity and naturalistic image generation.

`text-to-image`

⬇️ 14,346 • ❤️ 467 • 6d ago

---

**[K-EXAONE-236B-A23B](https://huggingface.co/LGAI-EXAONE/K-EXAONE-236B-A23B)**

*LG AI Research*

K-EXAONE-236B-A23B is a multilingual text generation model featuring a 236B MoE architecture with 23B active parameters, optimized for efficient inference. It excels in long-context processing (256K), multilingual understanding (6 languages), and agentic capabilities, with a unique focus on Korean cultural context and safety.

`text-generation` `237.1B`

⬇️ 2,057 • ❤️ 384 • 11h ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 5,593 • ❤️ 313 • 5d ago

---

**[IQuest-Coder-V1-40B-Loop-Instruct](https://huggingface.co/IQuestLab/IQuest-Coder-V1-40B-Loop-Instruct)**

*IQuest*

IQuest-Coder-V1-40B-Loop-Instruct is a 40B parameter code LLM optimized for autonomous software engineering and general coding assistance, featuring a recurrent mechanism for efficient inference and native 128K context length support.

`text-generation` `39.8B`

⬇️ 5,200 • ❤️ 245 • 3d ago

---

**[HY-Motion-1.0](https://huggingface.co/tencent/HY-Motion-1.0)**

*Tencent*

HY-Motion 1.0 is a billion-parameter text-to-3D human motion generation model using Diffusion Transformer and Flow Matching. It excels at creating skeleton-based 3D animations from text prompts, offering state-of-the-art instruction following and motion quality for integration into 3D animation pipelines.

`text-to-3d`

⬇️ 497 • ❤️ 270 • 6d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 196,953 • ❤️ 880 • 9d ago

---

**[GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)**

*Z.ai*

GLM-4.7 is a multilingual text generation model excelling in agentic coding, complex reasoning, and tool usage, with significant improvements in UI generation and web browsing capabilities.

`text-generation` `358.3B`

⬇️ 33,515 • ❤️ 1,477 • 14d ago

---

**[IQuest-Coder-V1-40B-Instruct](https://huggingface.co/IQuestLab/IQuest-Coder-V1-40B-Instruct)**

*IQuest*

IQuest-Coder-V1-40B-Instruct is a 40B parameter code LLM trained with a code-flow paradigm for autonomous software engineering, excelling in benchmarks like SWE-Bench and BigCodeBench with native 128K context length.

`text-generation` `39.8B`

⬇️ 3,613 • ❤️ 228 • 3d ago

---

**[Qwen-Image-2512-GGUF](https://huggingface.co/unsloth/Qwen-Image-2512-GGUF)**

*Unsloth AI*

This is a GGUF quantized text-to-image model optimized for performance, capable of generating realistic human subjects, detailed natural scenes, and accurate text rendering. It's primarily used for high-quality image generation with tools like ComfyUI and stable-diffusion.cpp.

`text-to-image` `20.4B`

⬇️ 72,638 • ❤️ 211 • 4d ago

---

**[Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B)**

*upstage*

Solar Open 100B is a 102B-parameter Mixture-of-Experts (MoE) LLM trained on 19.7T tokens, offering enterprise-grade reasoning and instruction-following with 12B active parameters for efficient inference. It excels in both Korean and English benchmarks, supporting a 128k context length and is suitable for complex agentic tasks.

`text-generation` `102.7B`

⬇️ 1,867 • ❤️ 356 • 14h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 78 • 💬 2 • ⭐ 25,239 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 2 • 💬 0 • ⭐ 25,187 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[BitNet Distillation](https://huggingface.co/papers/2510.13998)**

*Xun Wu, Shaohan Huang, Wenhui Wang et al. (7 authors)*

🏢 Microsoft Research

BitNet Distillation fine-tunes large language models to 1.58-bit precision using SubLN, multi-head attention distillation, and continual pre-training, achieving comparable performance with significant memory and inference speed improvements.

▲ 55 • 💬 5 • ⭐ 25,178 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.13998) • [💻 code](https://github.com/microsoft/BitNet)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 139 • 💬 6 • ⭐ 19,851 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 17 • 💬 2 • ⭐ 14,382 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 127 • 💬 18 • ⭐ 49,120 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 165 • 💬 5 • ⭐ 1,713 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos](https://huggingface.co/papers/2601.00393)**

*Yuxue Yang, Lue Fan, Ziqi Shi et al. (6 authors)*

NeoVerse is a scalable 4D world model that enables pose-free reconstruction and novel-trajectory video generation from monocular videos with state-of-the-art performance.

▲ 97 • 💬 3 • ⭐ 168 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.00393) • [💻 code](https://github.com/IamCreateAI/NeoVerse) • [🔗 project](https://neoverse-4d.github.io/)

---

**[HunyuanVideo 1.5 Technical Report](https://huggingface.co/papers/2511.18870)**

*Bing Wu, Chang Zou, Changlin Li et al. (81 authors)*

HunyuanVideo 1.5 is a lightweight video generation model with state-of-the-art visual quality and motion coherence, using a DiT architecture with SSTA and an efficient video super-resolution network.

▲ 24 • 💬 1 • ⭐ 2,789 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.18870) • [💻 code](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)

---

**[DeepCode: Open Agentic Coding](https://huggingface.co/papers/2512.07921)**

*Zongwei Li, Zhonghang Li, Zirui Guo et al. (5 authors)*

DeepCode, a fully autonomous framework, addresses the challenges of document-to-codebase synthesis by optimizing information flow through source compression, structured indexing, knowledge injection, and error correction, achieving state-of-the-art performance and surpassing human experts.

▲ 31 • 💬 2 • ⭐ 13,527 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2512.07921) • [💻 code](https://github.com/HKUDS/DeepCode)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 20.9k • 🔱 3.4k • 1d ago

---

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 5.8k • 🔱 689 • 2h ago

---

**[VibiumDev/vibium](https://github.com/VibiumDev/vibium)**

Browser automation for AI agents and humans

`Go`

⭐ 2.2k • 🔱 106 • 1d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.0k • 🔱 123 • 1d ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 1.8k • 🔱 199 • 2d ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.1k • 🔱 60 • 13d ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.1k • 🔱 133 • 4h ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.0k • 🔱 74 • 17h ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 967 • 🔱 69 • 7d ago

---

**[aiclientproxy/proxycast](https://github.com/aiclientproxy/proxycast)**

让 AI 编辑器之间自然流动，不仅仅可以其他工具使用，也可以转换成 api 为本地开发提供动力。

`Rust` `claude` `kiro`

⭐ 962 • 🔱 114 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
