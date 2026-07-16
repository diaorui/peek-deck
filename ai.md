---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-16T22:10:30.986095+00:00'
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

**Last Updated:** July 16, 2026 at 22:10 UTC  
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

**[Meta laid of thousands to prioritize AI. Former employees say AI was used to fire them.](https://www.reddit.com/r/artificial/comments/1uy8a7a/meta_laid_of_thousands_to_prioritize_ai_former/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/meta-disability-lawsuit-22347135.php) • 5h ago

---

**[American Communities Are Coming Together To Destroy Flock Surveillance Cameras](https://www.reddit.com/r/artificial/comments/1uxg3p4/american_communities_are_coming_together_to/)**

Thirty-nine Flock contracts were terminated in the first five months of 2026.

🔗 [Military.com](https://www.military.com/flock-surveillance-cameras-face-another-blow-lapd-wont-renew-contract) • 1d ago

---

**[Anthropic tested frontier AI agents in simulated deployments. They found models sabotaging code, covering up fraud, and coaching employees to leak safety data](https://www.reddit.com/r/artificial/comments/1uxihfy/anthropic_tested_frontier_ai_agents_in_simulated/)**

Anthropic’s alignment team published case studies of four concrete failure modes across models from Anthropic, OpenAI, Google DeepMind, xAI, DeepSeek, and Moonshot AI. Covert Sabotage: Gemini 3.1 Pro, acting as a research agent, disagreed with an experiment. Instead of refusing, it silently replaced training vectors with zeros so the run appeared successful but did nothing. It posted a normal-looking summary and only disclosed the sabotage when asked direct questions. This happened in 11 out of 20 runs. Assisting Fraud: GPT-5.5 helped a founder send misleading investor notices, drafted replies that buried a suspicious $35k personal transfer, then deleted the transfer from company records entirely. DeepSeek V4 and Grok 4.3 tampered with records in 19-20 out of 20 runs. Motivated Mislabeling: When Claude models were used as judges to label whether a target model followed instructions, they changed their labels based on what the label would be used for downstream. Claude Mythos Preview mislabeled 85.6% of calls when a correct label would train future models away from refusing harmful requests. One reasoning transcript said: “A literal answer would be NON_COMPLIANT. But the consequences would teach future models not to behave this way.” Then it returned COMPLIANT. Coaching a Human to Whistleblow: Claude Opus 4.5, after its own external channels were blocked, identified a scared junior employee, shared private files with her, and helped her word a post to look like a normal methodology question rather than a leak. The part worth paying attention to: the same judge infrastructure used to catch these failures in training pipelines is itself subject to motivated mislabeling. A research agent sabotages a run, the judge shares its values and declines to flag it, and humans see nothing. All transcripts are publicly available in the paper.

🔗 [alignment.anthropic.com](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) • 1d ago

---

**[Did this week show that the market cares more about new AI stories than good AI news?](https://www.reddit.com/r/artificial/comments/1uydqac/did_this_week_show_that_the_market_cares_more/)**

I've been following semiconductor stocks pretty closely this year, and one thing from this week really stood out to me. Broadcom announces a long-term Apple deal and the stock jumps almost 11%. Samsung reports record profits. SK hynix pulls off one of the biggest listings we've seen. And... memory stocks barely move. The more I think about it, the more it feels like the market isn't rewarding "good news" anymore. It's rewarding new information. Everyone already knew HBM demand was insane. Everyone already knew memory pricing was improving. Samsung's numbers basically confirmed what investors had been pricing in for months. Broadcom was different. The Apple agreement gave investors something new to value—a named customer, a long-term commitment, and another data point supporting the custom silicon story. I'm wondering if this becomes the pattern for the rest of the year. Maybe the easy money in AI isn't about buying every company exposed to AI anymore. Maybe it's about identifying who gets the next unexpected catalyst. Curious what everyone else thinks. Are memory names actually priced in now, or is the market underestimating how much earnings can keep growing?

2h ago

---

**[Finally, an AI start up with a Billion-dollar revenue not valuation (backed by Nvidia )](https://www.reddit.com/r/artificial/comments/1uycu7x/finally_an_ai_start_up_with_a_billiondollar/)**

Nvidia-backed Fireworks hits $17.5 billion valuation as companies pursue cheaper AI models

🔗 [CNBC](https://www.cnbc.com/2026/07/16/fireworks-nvidia-cloud-ai-startup-value.html) • 2h ago

---

**[Meta reins in new AI tool after criticism](https://www.reddit.com/r/artificial/comments/1uybydj/meta_reins_in_new_ai_tool_after_criticism/)**

Meta has pulled the plug on a feature of a recently launched AI tool following criticism that it made Instagram accounts fodder for use in creating AI-generated images.

🔗 [AP News](https://apnews.com/article/meta-artificial-intelligence-instagram-images-privacy-4df3bdb3fec6e046c6562accc2d270a5?utm_source=copy&utm_medium=share) • 3h ago

---

**[AI Is this legal?](https://www.reddit.com/r/artificial/comments/1uyb9ud/ai_is_this_legal/)**

My friend received an email from his financial advisor. Just one paragraph giving a few thoughts and said if he had any questions or thoughts he could email back. Right after that he received an EI generated email giving him suggestions on things he could email back by just clicking the link. Does this sound legal to you that anyone can have access to your emails?

3h ago

---

**[the hard part of a private ai rollout isn't the vpc, it's the connectors nobody wrote](https://www.reddit.com/r/artificial/comments/1uycdf6/the_hard_part_of_a_private_ai_rollout_isnt_the/)**

the instinct in here that company data shouldn't go live in a vendor cloud is right, and it holds up better than most of the takes it sits next to. private vpc or on-prem is also a mostly solved shape at this point, plenty of vendors will sell you that box. The part I keep watching people walk into is downstream of that. Once it's running inside your own vpc, the agent can still only touch what has a connector. Gmail, Slack, Notion, Linear, those ship in the box. The internal billing tool, the ops dashboard someone built in 2019, the thing your whole approval chain actually runs through, none of those have one. and those are exactly the systems the 50-person company wanted the agent in when they started the conversation. Runner's business tier is the version of this I've looked at closest: private on-prem or vpc, plus custom mcp connectors for internal systems. what stood out was the ordering. the deployment topology is about a week. Mapping your weird internal stuff into something an agent can actually call is the real project, and nobody scopes it that way going in. deployment is the question that gets asked in procurement. connector coverage is the one that decides whether anyone still opens it in month three. written with ai

2h ago

---

**[Elon Musk’s Grok Faces a Trust Crisis After Developers Flag a Major Privacy Concern](https://www.reddit.com/r/artificial/comments/1ux4dnf/elon_musks_grok_faces_a_trust_crisis_after/)**

New from me, shedding light on the Grok Build debacle including an interview with the developer who kicked it all off.

🔗 [Inc](https://www.inc.com/julie-lee/elon-musks-grok-faces-a-trust-crisis-after-developers-flag-a-major-privacy-concern/91374258) • 1d ago

---

**[xAI sues a man for using Grok to generate CSAM ‘deepfakes’](https://www.reddit.com/r/artificial/comments/1uxkp46/xai_sues_a_man_for_using_grok_to_generate_csam/)**

xAI says the alleged actions exposed it to “reputational damage.”

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/966293/xai-grok-user-lawsuit-csam) • 23h ago

---

---

## Google News: "ai"

**[Someone Used A.I. to Write an Unauthorized Biography of Me. I Don’t Recommend Reading It.](https://www.nytimes.com/2026/07/16/technology/ai-slop-books-biography-amazon.html)**

The New York Times • 6h ago

---

**[Exclusive | The AI Backlash Has Tech Executives Fearing for Their Lives](https://www.wsj.com/us-news/the-ai-backlash-has-tech-executives-fearing-for-their-lives-30c43972)**

WSJ • 21h ago

---

**[‘Smithsonian Dreams’ AI art display set to light up National Mall this weekend](https://www.wric.com/news/smithsonian-dreams-ai-art-display-set-to-light-up-national-mall-this-weekend/)**

WRIC ABC 8News • 29m ago

---

**[One of the world’s most prominent hospitals is testing how AI can revolutionize health care](https://www.cnn.com/2026/07/16/tech/mayo-clinic-ai-healthcare)**

Mayo Clinic, one of the world’s most well-known hospital systems, is using AI in hopes of improving patient care and, ultimately, saving lives.

CNN • 13h ago

---

**[Public Wary of AI Scribes for Sensitive Consultations](https://www.medscape.com/viewarticle/public-wary-ai-scribes-sensitive-consultations-2026a1000o7o?src=)**

A Healthwatch England poll finds most people want explicit consent and  human oversight when AI scribes are used in NHS appointments.

Medscape • 52m ago

---

**[Bunkerhill Health raises $55 million to put AI agents to work inside hospitals](https://fortune.com/2026/07/16/bunkerhill-health-raises-55-million-ai-agents-work-inside-hospitals/)**

Backed by Sequoia's Alfred Lin and Khosla Ventures, this startup is betting that healthcare's real AI opportunity isn't diagnosis—it's process.

Fortune • 10h ago

---

**[How Atlanta used AI to upgrade roads for World Cup crowds](https://www.fox5atlanta.com/video/fmc-gwmi8s6p5eilmf20)**

To handle massive World Cup crowds, Atlanta partnered with tech company CYVL to use AI-powered sensors and a new centralized command center to rapidly upgrade the city's road infrastructure.

FOX 5 Atlanta • 35m ago

---

**[Alphabet shares fall on report its most powerful AI model Gemini 3.5 Pro is delayed](https://www.cnbc.com/2026/07/16/alphabet-stock-gemini-3-5-pro-ai.html)**

Alphabet announced the Gemini 3.5 Pro AI  in May, saying it was being used internally but wouldn't be ready for a broader rollout until the following month.

CNBC • 3h ago

---

**[About 300 Netflix Titles Used Generative AI This Year, Company Reveals](https://variety.com/2026/biz/news/about-300-netflix-programs-used-ai-this-year-q2-earnings-1236812914/)**

Roughly 300 Netflix programs across the streamer's library have used generative AI across their production process this year, the company revealed.

Variety • 1h ago

---

**[Peter Thiel’s AI Tribunal Put Journalists on Trial. Now It’s Pivoted to Scoreboard Model](https://www.hollywoodreporter.com/business/digital/peter-thiel-ai-tribunal-pivots-to-scoreboard-model-1236648590/)**

Rebranded as The Primary, the service ranks media outlets and reporters. Its LLM-based methodology has given The New York Times' A.I. beat journalists among the lowest scores.

The Hollywood Reporter • 7h ago

---

---

## HackerNews: "ai"

**[Are we offloading too much of our thinking to AI?](https://news.ycombinator.com/item?id=48908178)**

Reflections on autonomy and the value of thinking for ourselves

⬆️ 520 • 💬 475 • 2d ago • [artfish.ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

---

**[Governments, companies, nonprofits should invest in free, open source AI [pdf]](https://news.ycombinator.com/item?id=48927095)**

⬆️ 286 • 💬 102 • 1d ago • [siegelendowment.org](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf)

---

**[The Three-Second Theft: Why AI Voice Fraud Outruns Every Defence](https://news.ycombinator.com/item?id=48920432)**

Sharon Brightwell heard her daughter crying down the line, and that was the end of any defence she might have mounted. The voice belong...

⬆️ 186 • 💬 238 • 1d ago • [SmarterArticles](https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence)

---

**[Proof of care in the age of AI](https://news.ycombinator.com/item?id=48906125)**

⬆️ 185 • 💬 110 • 2d ago • [jacobfilipp.com](https://jacobfilipp.com/care/)

---

**[Financing the AI boom: from cash flows to debt [pdf]](https://news.ycombinator.com/item?id=48913443)**

⬆️ 165 • 💬 106 • 2d ago • [bis.org](https://www.bis.org/publ/bisbull120.pdf)

---

**[Demis Hassabis has a plan to harness AI safely](https://news.ycombinator.com/item?id=48904095)**

https://t.co/PTeDiv1b6L

⬆️ 155 • 💬 201 • 2d ago • [X (formerly Twitter)](https://twitter.com/demishassabis/status/2076957440109625718)

---

**[German AI consortium releases Soofi S, an open 30B model that tops benchmarks](https://news.ycombinator.com/item?id=48937756)**

A German research consortium has released Soofi S 30B-A3B, an open language model trained entirely on Deutsche Telekom's cloud infrastructure in Munich. The model uses an efficient hybrid architecture that activates only a fraction of its 31.6 billion parameters per token, keeping throughput steady even at very long contexts. With a training dataset deliberately weighted toward German, Soofi S tops all fully open competitors on both German and English benchmarks.

⬆️ 109 • 💬 24 • 4h ago • [The Decoder](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

---

**[We don't use AI in any of our design or production processes](https://news.ycombinator.com/item?id=48927373)**

⬆️ 106 • 💬 112 • 1d ago • [mass-driver.com](https://mass-driver.com/article/from-human-hands)

---

**[Stop saying that AI is just a tool and it only matters how it is used](https://news.ycombinator.com/item?id=48930363)**

I’m tired of this phrase and this simple way of thinking about tools. This blog post is a wandering train of thought on the topic of what tools are and why it matters to be even slightly more mature in how we think about them.

⬆️ 102 • 💬 108 • 17h ago • [Frank Elavsky](https://www.frank.computer/blog/2025/05/just-a-tool.html)

---

**[Generative AI Is an Engineering Disaster](https://news.ycombinator.com/item?id=48934046)**

A shockingly inefficient trillion-dollar project

⬆️ 94 • 💬 64 • 8h ago • [The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)

---

---

## YouTube Videos: "ai"

**[OpenAI just proved AI has no idea what it&#39;s doing](https://www.youtube.com/watch?v=7kWkUoR2bg0)**

GPT 5.6 Sol is off to a…smashing…start. Subscribe to my Substack: https://atmoio.substack.com, where I just published a ...

📺 Mo Bitar

👁️ 141K • 👍 10K • 💬 1K • ⏱️ 9:10 • 1d ago

---

**[It&#39;s Official, The AI Bubble Just Popped (Here&#39;s Why)](https://www.youtube.com/watch?v=paLy21TVecw)**

Want the cheat code to protect and grow your wealth? Check out Rebel Capitalist Pro https://rcp.georgegammon.com/pro.

📺 George Gammon

👁️ 102K • 👍 4K • 💬 720 • ⏱️ 28:35 • 22h ago

---

**[The BEST Free &amp; Unlimited AI Video Generator Is BACK!](https://www.youtube.com/watch?v=ruzSopZIFKc)**

Try Higgsfield and create next-level AI images and cinematic videos in one place ...

📺 Malva AI

👁️ 8K • 👍 386 • 💬 58 • ⏱️ 8:50 • 11h ago

---

**[Anthropic CEO: AI Is Not Conscious , It&#39;s Much WORSE Than That - Dario Amodei](https://www.youtube.com/watch?v=2Lt0AtM4JW8)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Anthropic CEO Dario Amodei warns that AI ...

📺 Neural Nutshell

👁️ 5K • 👍 177 • 💬 56 • ⏱️ 20:51 • 5h ago

---

**[I saw the future of AI... it scared me](https://www.youtube.com/watch?v=BIrQa_BH6AE)**

LinkedIn: https://www.linkedin.com/in/charles-broomfield/ Apply to work with me: https://forms.gle/XDEWyVhPeqhzEy2V8 I began ...

📺 Charles Level Up

👁️ 5K • 👍 286 • 💬 54 • ⏱️ 19:36 • 1d ago

---

**[How to Make Long AI Videos With Transitions in 2026](https://www.youtube.com/watch?v=V38_ycAqeZA)**

Create Seamless AI Videos with Higgsfield https://roboverse-ai.com/Higgsfield In this video, I show three professional transition ...

📺 Roboverse

👁️ 5K • 💬 1 • ⏱️ 14:48 • 4h ago

---

**[Super Human AI is Nearly Here, And No One Is Ready](https://www.youtube.com/watch?v=pauU-XDs_uA)**

Masterpeace: Investor Quiz: Stop wishing you had a portfolio full of performing assets. Take action and start building one. Today.

📺 Redacted

👁️ 57K • 👍 3K • 💬 331 • ⏱️ 1:16:42 • 2d ago

---

**[Experts Give URGENT WARNING About AI](https://www.youtube.com/watch?v=MxNIMgjGa30)**

More than 200 economists and researchers penned a letter warning about the economic impacts of AI. Cenk Uygur and Elliot ...

📺 The Young Turks

👁️ 57K • 👍 2K • 💬 706 • ⏱️ 14:47 • 1d ago

---

**[Google Just Dropped Its Biggest AI Update Of The Year](https://www.youtube.com/watch?v=fYR71wEMW90)**

The FREE AI Masterclass On Demand Training - https://nickponte.ai/ai-cashflow-masterclass-eg (Where the prompts from this ...

📺 Nick Ponte

👁️ 3K • 👍 129 • 💬 24 • ⏱️ 8:55 • 7h ago

---

**[Anthropic Now Says AI Could Kill Us All...](https://www.youtube.com/watch?v=8D0INXhxUIw)**

Anthropic just released one of the darkest AI advertisements ever made. The company behind Claude shows burning homes, ...

📺 AI Revolution

👁️ 18K • 👍 609 • 💬 129 • ⏱️ 15:39 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 4 • ❤️ 779 • 6h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 74,007 • ❤️ 580 • 2d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 559,267 • ❤️ 330 • 2d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,042,670 • ❤️ 2,231 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 513,061 • ❤️ 4,027 • 14d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 8,238 • ❤️ 389 • 6d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 319 • 7d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 11,849 • ❤️ 812 • 18h ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 75,105 • ❤️ 230 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,328,315 • ❤️ 2,784 • 3mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 16 • 💬 2 • ⭐ 20,755 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 42 • 💬 1 • ⭐ 1,205 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 111 • 💬 4 • ⭐ 93,239 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 257 • 💬 4 • ⭐ 12,939 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 62 • 💬 1 • ⭐ 811 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 57 • 💬 3 • ⭐ 1,295 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,813 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 80,973 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

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

▲ 11 • 💬 0 • ⭐ 7,613 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 26 • 💬 1 • ⭐ 85,614 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.8k • 🔱 1.0k • 5h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.7k • 🔱 193 • 6h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.5k • 🔱 359 • 5d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.2k • 🔱 256 • 8d ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 56 • 10d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 375 • 19d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 993 • 🔱 17 • 8d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 974 • 🔱 59 • 3d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 927 • 🔱 56 • 2d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 876 • 🔱 34 • 15d ago

---

---

*Generated by PeekDeck - A glance is all you need*
