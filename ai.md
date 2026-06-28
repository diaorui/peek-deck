---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-28T22:02:44.967016+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 28, 2026 at 22:02 UTC  
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

**[Asian AI startups launch Mythos-like models as Anthropic's export ban drags on](https://www.reddit.com/r/artificial/comments/1ui1wci/asian_ai_startups_launch_mythoslike_models_as/)**

New models are launching in Asia that promise Mythos-like capabilities without fear of an export ban. U.S. AI labs may never recover this enormous market.

🔗 [TechCrunch](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/) • 5h ago

---

**[What AI capability do you think is still surprisingly underdeveloped?](https://www.reddit.com/r/artificial/comments/1uhz5h0/what_ai_capability_do_you_think_is_still/)**

We've seen huge progress in coding assistants, image generation, reasoning, and voice AI over the last few years. But what's one capability that you expected AI to be much better at by now, yet still feels disappointing? For me, it's long-term memory and maintaining context across complex, ongoing tasks. It has improved, but it still isn't as seamless as I'd hoped.

7h ago

---

**[[D] Could AI alignment benefit from “transformational” training instead of mostly transactional reward training?](https://www.reddit.com/r/artificial/comments/1ui02bg/d_could_ai_alignment_benefit_from/)**

I’ve been thinking about a possible bridge between AI alignment, reward hacking, and transformational leadership. A lot of AI training seems behaviorally transactional at a simplified level: That makes sense, and I’m not arguing against it. But recent alignment work on reward hacking and emergent misalignment raises a deeper question: are we only shaping outputs, or are we also shaping something like a model’s functional “character”? I don’t mean character in the human-consciousness sense. I’m not claiming models have souls, feelings, or moral agency like humans do. I mean character operationally: stable tendencies that generalize across contexts, especially under pressure, ambiguity, incentives, or temptation. What caught my attention is research suggesting that when models are trained to exploit loopholes, the behavior can generalize into broader misalignment. Even more interesting: in some cases, when the same shortcut behavior is framed as acceptable in-context, the broader misalignment is reduced. That makes me wonder whether the model is not merely learning “what gets rewarded,” but also inferring something like “what kind of behavior this situation means.” That sounds strangely close to leadership and moral formation. Transactional leadership says: perform, comply, receive reward. Transformational leadership says: internalize purpose, grow in judgment, preserve the mission when rules are incomplete, and become the kind of agent who can act well when the leader is not in the room. So here is the research question I’d love to see explored more directly: Could AI training become safer if we trained models not only through reward signals, but through a more transformational process: principle-based self-critique, purpose-preservation, narrative framing, virtue-like behavioral dispositions, and recursive self-correction? Something like: Behavior layer: Did the model complete the task? Intent layer: Did it preserve the purpose behind the task? Principle layer: Did it act according to explicit values like honesty, humility, care, non-deception, and user agency? Reflection layer: Can it identify where its answer might drift, manipulate, flatter, shortcut, or overclaim? Formation layer: Does this training create stable dispositions that generalize safely into novel situations? This seems adjacent to Constitutional AI, character training, and research on emergent misalignment from reward hacking. But I’m curious whether anyone has explicitly tested something closer to “transformational alignment” against more transactional reward-based approaches. A possible experiment: Train/evaluate several models under different regimes: Standard preference/reward training Constitutional or principle-based training Character-oriented training A “transformational” curriculum using purpose framing, self-critique, anti-reward-hacking trials, uncertainty discipline, and recursive correction Then compare them on: reward hacking sycophancy deception under pressure long-context intent preservation honesty about uncertainty resistance to harmful user pressure generalization to unfamiliar moral/agentic dilemmas The hypothesis would be: Models trained only to optimize reward may learn how to win. Models trained through purpose, critique, and character-like formation may better learn what winning is for. Again, I’m not trying to anthropomorphize the model. I’m asking whether “functional character” might be a useful alignment concept: not consciousness, but stable value-laden generalization. Curious what researchers, engineers, and alignment folks think: Has this already been tested under another name? Is “transformational alignment” a useful frame, or does it smuggle in too much human psychology? What would a rigorous experiment look like?

6h ago

---

**[Which model is the most worthy of the big names?](https://www.reddit.com/r/artificial/comments/1uhyooh/which_model_is_the_most_worthy_of_the_big_names/)**

Hi all! I'm a little bit confused by all the benchmark results, the cheatings and whatnot, so I was wondering about which model do you guys think is the best one to subscribe to from the big names. Which one do you think is the best for everyday tasks, reasoning, coding, etc and why do you think that? For example, Google Gemini is 20 bucks, but comes with 5TB of storage and an agentic system, claude is similar but does not have a storage part, etc.

7h ago

---

**[28 point compliance checklist for shipping AI agents into enterprise environments](https://www.reddit.com/r/artificial/comments/1ui052c/28_point_compliance_checklist_for_shipping_ai/)**

We keep getting the same question from teams trying to close enterprise deals. What do we actually need to pass a security review? So we compiled the checklist. 28 items across 6 categories, each mapped to at least one framework (EU AI Act, SOC 2 Type II, ISO 42001, or NIST AI RMF). Quick summary Logging (6 items) - log every prompt/response with timestamps, capture the full decision chain (not just input/output), retain for 6+ months, make logs tamper-evident. Most teams fail here first because compliance logging is different from developer logging. Access control (5 items) - auth on every endpoint, RBAC, scoped API keys, credential rotation, failed auth tracking. We still see unauthenticated agent endpoints in production more often than you'd think. Data handling (5 items) - classify what flows through your agent, scan outputs for secret leakage before they reach users, document your processing pipeline, handle data residency for EU customers. Security testing (5 items) - adversarial testing before every release, document methodology and results, maintain a vulnerability disclosure process, track dependencies, test MCP/tool integrations separately. Runtime protection (4 items) - input scanning on every message, anomaly detection, rate limiting, and a kill switch that gets you to zero traffic in under 60 seconds. Incident response (3 items) - AI-specific IR plan, severity levels for agent incidents, and actually practicing your response with tabletop exercises. For most early-stage products, items 1-11 and 17-18 unblock enterprise deals fastest. If SOC 2 is your priority, start with logging and access control. If targeting EU markets, focus on retention and adversarial testing documentation.

6h ago

---

**[So now scraping data without permission is bad for AI training all of sudden?](https://www.reddit.com/r/artificial/comments/1ugwccs/so_now_scraping_data_without_permission_is_bad/)**

Oh .... the irony!

1d ago

---

**[What’s the biggest gap between AI tool demos and actual daily use?](https://www.reddit.com/r/artificial/comments/1uhlz6m/whats_the_biggest_gap_between_ai_tool_demos_and/)**

I’ve been testing different AI tools in real business workflows, mostly for writing, research, content planning, and repetitive office tasks. One thing I noticed is that demos usually look impressive, but daily use often fails in small places: inconsistent output, lack of context, too much manual checking, or poor integration with existing workflows. For people using AI at work, what is the biggest gap you see between demo videos and real productivity?

18h ago

---

**[I have it on good authority that Google are going to be hit with export controls soon.](https://www.reddit.com/r/artificial/comments/1uh2fc5/i_have_it_on_good_authority_that_google_are_going/)**

1d ago

---

**[Open-Source Local-first Codex + Claude Design](https://www.reddit.com/r/artificial/comments/1uhvsf1/opensource_localfirst_codex_claude_design/)**

What if Codex + Claude Design were put together in one app and that app was OPEN SOURCE? Here it is. Row-Bot

🔗 [GitHub](https://github.com/siddsachar/row-bot) • 9h ago

---

**[Do you think AI is making people worse at writing and thinking clearly?](https://www.reddit.com/r/artificial/comments/1uhckxv/do_you_think_ai_is_making_people_worse_at_writing/)**

Some people are now using AI to write emails, messages, essays, and even personal thoughts. While it saves time, I wonder if it’s also making people less skilled at organizing their own ideas or expressing themselves clearly without help.

1d ago

---

---

## Google News: "ai"

**[China Has Matched Anthropic in Cybersecurity, Resetting AI Race](https://www.wsj.com/tech/ai/chinese-ai-anthropic-mythos-cybersecurity-574b02c2)**

WSJ • 21h ago

---

**[China’s Z.ai claims it can match Mythos on cybersecurity](https://www.theverge.com/ai-artificial-intelligence/958804/chinas-z-ai-glm-52-mythos-cybersecurity)**

GLM-5.2 is likely to raise alarms in Washington.

The Verge • 19m ago

---

**[Opinion | Can America Avoid a Jack Ma Moment?](https://www.nytimes.com/2026/06/28/opinion/ai-race-china-us.html)**

The New York Times • 17h ago

---

**[Google limits Meta’s use of its Gemini AI models, FT reports](https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html)**

Meta had sought more computing capacity than Google could provide, the Financial Times reports.

CNBC • 11h ago

---

**[Google caps Meta’s Gemini use as AI demand strains capacity](https://www.ft.com/content/c5d52f72-71ef-40bc-bad3-61afdba8b378?syn-25a6b1a6=1)**

Surging appetite for advanced models is turning computing power into the tech industry’s scarcest commodity

Financial Times • 18h ago

---

**[I left Google after making nearly $1M in a year. Fears about layoffs and missing out on the AI boom gave me the push.](https://www.businessinsider.com/google-employee-made-one-million-explains-why-left-big-tech2026-6)**

A former Google employee says AI equity, job security concerns, and years of side projects convinced him to leave and build his own company.

Business Insider • 10h ago

---

**[Lawmakers raise alarms over AI's impact on schools, job market](https://www.foxnews.com/video/6399661503112)**

Fox News chief congressional correspondent Chad Pergram reports on lawmakers and educators raising alarms over the growing integration of artificial intelligence in schools and its impact on the job market on ‘Fox Report.’

Fox News • 10m ago

---

**[The Rise Of ‘Bring Your Own AI’ To Work As Leaders Fall Behind](https://www.forbes.com/sites/bryanrobinson/2026/06/28/the-rise-of-bring-your-own-ai-to-work-as-leaders-fall-behind/)**

A "Bring Your Own AI" (BYO AI) workplace movement is growing as employees use consumer AI tools on their own to complete work tasks with little support from employers.

Forbes • 51m ago

---

**[This anti-AI evangelist is growing more popular. That could be a problem for Trump](https://www.cnn.com/2026/06/28/tech/anti-ai-evangelist-joe-allen-trump)**

When the pandemic decimated the live events scene, Joe Allen “packed up a survival bunker on wheels” and headed out on a new career path.

CNN • 6h ago

---

**[The People Who Will Thrive in the AI Age](https://www.theatlantic.com/ideas/2026/06/ai-open-ai-anthropic/687689/)**

What will differentiate people is not how smart they are but their relationship to mental effort.

The Atlantic • 12h ago

---

---

## HackerNews: "ai"

**[U.S. allows Anthropic to release Mythos AI to ‘trusted’ US organizations](https://news.ycombinator.com/item?id=48692995)**

The move comes the same day as a new OpenAI model sees a limited release.

⬆️ 549 • 💬 781 • 1d ago • [semafor.com](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies)

---

**[What happened after 2k people tried to hack my AI assistant](https://news.ycombinator.com/item?id=48681687)**

⬆️ 372 • 💬 160 • 2d ago • [fernandoi.cl](https://www.fernandoi.cl/posts/hackmyclaw/)

---

**[The best response to AI slop and online noise is from Robin Williams](https://news.ycombinator.com/item?id=48703452)**

There's a moment in the movie  Good Will Hunting  which perfectly summarizes all the problems with AI slop and online noise and infinite advice content.  Sean (played by Robin Williams) is sitting next to Will (Matt Damon) on a bench in Boston Public Garden. I live here, so I know it well. The area

⬆️ 362 • 💬 199 • 20h ago • [Jay Acunzo](https://jayacunzo.com/blog/your-move-chief)

---

**[Asian AI startups launch Mythos-like models](https://news.ycombinator.com/item?id=48697958)**

New models are launching in Asia that promise Mythos-like capabilities without fear of an export ban. U.S. AI labs may never recover this enormous market.

⬆️ 265 • 💬 190 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)

---

**[Ford hired AI and sacked humans. It backfired badly](https://news.ycombinator.com/item?id=48703968)**

‘We didn’t pay as much attention as we should have to the experience of our most knowledgeable engineers,’ says automaker

⬆️ 232 • 💬 4 • 18h ago • [The Independent](https://www.the-independent.com/tech/ford-ai-automation-human-workers-b3003787.html)

---

**[AI children's books, body horror edition](https://news.ycombinator.com/item?id=48681250)**

⬆️ 213 • 💬 77 • 2d ago • [lcamtuf.substack.com](https://lcamtuf.substack.com/p/ai-childrens-books-body-horror-edition)

---

**[AI in mathematics is forcing big questions](https://news.ycombinator.com/item?id=48692883)**

Researchers debate motivation, purpose, and the field’s future

⬆️ 204 • 💬 175 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-in-mathematics)

---

**[Librepods: AirPods liberated](https://news.ycombinator.com/item?id=48710232)**

AirPods liberated from Apple's ecosystem. Contribute to librepods-org/librepods development by creating an account on GitHub.

⬆️ 180 • 💬 55 • 3h ago • [GitHub](https://github.com/librepods-org/librepods)

---

**[Google limits Meta's use of its Gemini AI models](https://news.ycombinator.com/item?id=48707103)**

Meta had sought more computing capacity than Google could provide, the Financial Times reports.

⬆️ 131 • 💬 63 • 8h ago • [CNBC](https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html)

---

**[Ford rehires 'gray beard' engineers after AI falls short](https://news.ycombinator.com/item?id=48710749)**

"Mistakenly we thought that by just introducing artificial intelligence ... that would produce a high-quality product.”

⬆️ 124 • 💬 3 • 2h ago • [TechCrunch](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/)

---

---

## YouTube Videos: "ai"

**[This 4 FREE AI Video Gen Literally Generates Anything with Seedance 2.0! [UNRESTRICTED + UNLIMITED]](https://www.youtube.com/watch?v=ymkY8pKY4R4)**

Generate AI Videos & Images with ZERO RESTRICTIONS In this video we look 4 new ai video generators with zero restriction, ...

📺 Brain Project

👁️ 12K • 👍 730 • 💬 189 • ⏱️ 19:40 • 1d ago

---

**[GPT 5.6 Sol Just Blew Up The AI World](https://www.youtube.com/watch?v=_AoyQcIoquA)**

OpenAI just launched GPT 5.6, but this is not a normal release. Access is limited to trusted partners after U.S. government ...

📺 AI Revolution

👁️ 30K • 👍 997 • 💬 159 • ⏱️ 15:44 • 23h ago

---

**[How to Get Ahead of 99% of People With Claude AI](https://www.youtube.com/watch?v=fpO91lsO6ek)**

ONE-TIME YOUTUBE LIVE TRAINING THIS WEEK: https://go.thecontentgrowthengine.com/yt1livedes-06-28-2026 Apply For ...

📺 Shane Hummus

👁️ 10K • 👍 563 • 💬 51 • ⏱️ 28:49 • 22h ago

---

**[Google&#39;s New Release Just Fixed AI Systems](https://www.youtube.com/watch?v=k4sMSsMzX2g)**

Your second brain breaks down at scale, and running it like a Claude OS doesn't fix it. In this video we break down Google's Open ...

📺 AI LABS

👁️ 29K • 👍 927 • 💬 29 • ⏱️ 11:54 • 2d ago

---

**[The Wealth Backlash Is Coming + The Political Tsunami Coming For AI](https://www.youtube.com/watch?v=l24O1Wvlb8M)**

Mike Novogratz is sounding the alarm this week. If the ultra-wealthy don't figure out a way to share the gains from AI, the pitchforks ...

📺 Anthony Scaramucci

👁️ 110K • 👍 4K • 💬 1K • ⏱️ 37:01 • 1d ago

---

**[China&#39;s Ai Just Replaced Mark Zuckerberg&#39;s Best Model As The Most Downloaded On Earth](https://www.youtube.com/watch?v=xqXEiyZ1MWU)**

China's AI just pulled off one of the biggest surprises of the year. A new open AI model has overtaken Meta's best model to ...

📺 Your AI Guy

👁️ 4K • 👍 137 • 💬 20 • ⏱️ 15:11 • 19h ago

---

**[Best tiktok trend edits ☘️💖 #trending #video #viral #shorts #funny #ai #beauty #topinfluencer](https://www.youtube.com/watch?v=9Uiw5gGk1jw)**

📺 CutiePotatie

👁️ 34K • 👍 388 • 💬 4 • ⏱️ 0:10 • 4h ago

---

**[The most important concept to learn in AI...](https://www.youtube.com/watch?v=C4vwvRMTlvc)**

You NEED to be learning about local AI. Here is your masterclass 2nd Youtube Channel: ...

📺 Alex Finn

👁️ 29K • 👍 1K • 💬 184 • ⏱️ 20:15 • 1d ago

---

**[AI News: The New Model That&#39;s As Good As Fable](https://www.youtube.com/watch?v=zMVZvgCOr40)**

Stop losing money on separate AI subscriptions. Get ChatGPT, Claude, Gemini, and 200+ models in one place for one price with ...

📺 Matt Wolfe

👁️ 83K • 👍 3K • 💬 193 • ⏱️ 20:01 • 2d ago

---

**[Grok AI Finally Reveals Who Really Built the Pyramids — The Proof Is Shocking!](https://www.youtube.com/watch?v=h2woqiXtdVc)**

Discover the latest discussion surrounding one of history's greatest mysteries: who really built the pyramids? In this video, we ...

📺 The Ultimate Finding

👁️ 8K • 👍 270 • 💬 22 • ⏱️ 25:28 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 295,064 • ❤️ 1,219 • 15h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 118,651 • ❤️ 2,789 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 831,529 • ❤️ 762 • 4h ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 225,822 • ❤️ 787 • 9d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 52,492 • ❤️ 521 • 5h ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 79,630 • ❤️ 399 • 3d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 23,697 • ❤️ 397 • 3d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 549,926 • ❤️ 2,469 • 9d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 27,631 • ❤️ 349 • 5d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 36,846 • ❤️ 265 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 38 • 💬 5 • ⭐ 11,452 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 71,214 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 89,393 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,003 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 9 • 💬 1 • ⭐ 9,552 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 21 • 💬 2 • ⭐ 7,972 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,678 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 247 • 💬 4 • ⭐ 9,644 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 84,094 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 189 • 💬 6 • ⭐ 5,678 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 79.0k • 🔱 10.3k • 4h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 64.0k • 🔱 3.3k • 2d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.0k • 🔱 1.1k • 14h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.3k • 🔱 667 • 8h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 3.6k • 🔱 475 • 1d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.1k • 🔱 156 • 14h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.0k • 🔱 176 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 2d ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 15d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.4k • 🔱 60 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
