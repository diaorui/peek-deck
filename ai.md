---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-23T10:17:10.538921+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** December 23, 2025 at 10:17 UTC  
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

**[Steam games that openly use generative AI earned $660 million this year, including Call of Duty: Black Ops 6, Stellaris, and more, as studios continue to rely on the technology](https://www.reddit.com/r/artificial/comments/1ptd5uy/steam_games_that_openly_use_generative_ai_earned/)**

Uh oh…

🔗 [GamesRadar+](https://www.gamesradar.com/games/steam-games-that-openly-use-generative-ai-earned-usd660-million-this-year-including-call-of-duty-black-ops-6-stellaris-and-more-as-studios-continue-to-rely-on-the-technology/) • 11h ago

---

**[AI will neutralize the power of a general strike](https://www.reddit.com/r/artificial/comments/1ptqb64/ai_will_neutralize_the_power_of_a_general_strike/)**

There is a scenario I have been thinking about. Wondering what your feedback would be. If you’re like me and you’re paying attention to the political situation in America, it has become clear that electoral politics isn’t going to produce the kind of changes necessary for Americans to thrive going forward. Wages need to go up and costs need to go down. Across the board, people are struggling to survive and it’s only getting worse. Who here thinks that the current politicians or any potential future offerings from the Democrats or Republicans are going to be able to reduce costs and increase wages? Or deal with the consequences of environmental damage caused by pollution? Even if you consider more desperate, awful methods like what Luigi did; that didn’t really help bring medical costs down. Maybe for a day or so here or there but that kind of action won’t bring about substantive changes. Not saying it would be justified if it did, but either way it won’t. The only thing that might work is if Americans en masse decided to shut the country down and stop working until certain demands for better living conditions were met - via a general strike. Getting to the point where one could be organized is another matter, but if, in the highly unlikely event one could be organized, changes to the status quo would become much more likely. Especially if the police joined in. Once AI has replaced millions of jobs, or nearly every job, that will no longer be possible. I sometimes wonder if the only thing “the powers that be“ really are worried about is the possibility of a general strike. once it’s removed, they can lock in a new status quo that erases the old social contract, and create a permanent world of haves and have-nots run by a few wealthy families who have the power to make sure their status never changes. What do you think?

11m ago

---

**[Instacart scraps AI pricing tests that made some products more expensive | A study found that Instacart’s pricing tests resulted in higher prices for some customers.](https://www.reddit.com/r/artificial/comments/1pt9u2r/instacart_scraps_ai_pricing_tests_that_made_some/)**

Prices may still vary on a store-by-store basis, Instacart says.

🔗 [The Verge](https://www.theverge.com/news/849061/instacart-ends-ai-pricing-tests-eversight) • 13h ago

---

**[Schools across the U.S. are rolling out AI-powered surveillance technology, including drones, facial recognition and even bathroom listening devices](https://www.reddit.com/r/artificial/comments/1pswv5x/schools_across_the_us_are_rolling_out_aipowered/)**

The surveillance fostered an atmosphere of distrust: 32% of 14 to 18-year-old students surveyed said they felt like they were always being watched. In focus groups run by the ACLU, students said they felt less comfortable alerting educators to mental health issues and physical abuse. Marlow argues that’s a lousy tradeoff. “Because kids don't trust people they view as spying on them, it ruptures trust and actually makes things less safe,” he said.

🔗 [forbes.com](https://www.forbes.com/sites/thomasbrewster/2025/12/16/ai-bathroom-monitors-welcome-to-americas-new-surveillance-high-schools/) • 23h ago

---

**[Google's server-side state management API - thoughts on the architecture?](https://www.reddit.com/r/artificial/comments/1pto8yn/googles_serverside_state_management_api_thoughts/)**

Google recently shipped an API that handles conversation history, context management, and background execution server-side for agent deployments (the new Interactions API in Gemini). From what we can tell, this eliminates most of the infrastructure work that typically goes into building agents. No vector DB setup, no custom context engineering, no session state management. It's all handled by Google. We've been prototyping with it for a couple weeks now. The difference in development velocity is pretty significant. What used to take days of setting up memory architecture now just works out of the box. The trade-off seems obvious though. You're locked into Google's infrastructure. You lose control over how context is stored and retrieved. Model switching becomes harder. Cost optimization gets more opaque. But from a practical standpoint, it removes what we'd estimate was 60-80% of the grunt work in agent development. You can focus entirely on the business logic and prompt engineering instead of building plumbing. A few things we're curious about from people who've worked with this or similar patterns. How does this compare to building with LangChain or LangGraph memory solutions? Is the convenience worth the vendor lock-in? For production deployments, does server-side state management create any issues around auditability or debugging? With custom implementations you can inspect everything. Here it's more of a black box. What's the failure mode if Google's state management has issues? With self-hosted solutions you at least have control. Here you're dependent on their uptime. Is there a reasonable path to migrate off this if needed? Or once you build on it, you're committed? From an architecture perspective, this feels like Google positioning infrastructure as the moat. Similar to how AWS won by solving undifferentiated heavy lifting. But in ML workloads, control over the full stack has typically been important. For context, we're working across several businesses (e-commerce, SaaS) building management-layer agents. Planning systems, decision analysis, that kind of thing. Not doing anything cutting-edge from a research standpoint, just trying to ship production systems that work. The ease of prototyping with this API has been valuable. But we're trying to think through whether we're setting ourselves up for problems down the road by outsourcing this much of the stack. Curious what others think about this pattern. Is server-side state management the future for agent development? Or are we trading too much control for convenience?

2h ago

---

**[Guided learning lets “untrainable” neural networks realize their potential](https://www.reddit.com/r/artificial/comments/1ptlus7/guided_learning_lets_untrainable_neural_networks/)**

MIT CSAIL study suggests that neural network architectures considered unsuitable for modern tasks can improve with short-term guidance. The method encourages a target network to match a guide network’s internal representations, improving its starting point and making machine learning easier.

🔗 [MIT News | Massachusetts Institute of Technology](https://news.mit.edu/2025/guided-learning-lets-untrainable-neural-networks-realize-their-potential-1218) • 4h ago

---

**[Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves](https://www.reddit.com/r/artificial/comments/1pt4tnu/flock_exposed_its_aipowered_cameras_to_the/)**

Flock left at least 60 of its people-tracking Condor PTZ cameras live streaming and exposed to the open internet.

🔗 [404 Media](https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/) • 17h ago

---

**[One-Minute Daily AI News 12/22/2025](https://www.reddit.com/r/artificial/comments/1ptlxdk/oneminute_daily_ai_news_12222025/)**

OpenAI says AI browsers may always be vulnerable to prompt injection attacks.[1] AI has become the norm for students. Teachers are playing catch-up.[2] Google DeepMind Researchers Release Gemma Scope 2 as a Full Stack Interpretability Suite for Gemma 3 Models.[3] OpenAI introduces evaluations for chain-of-thought monitorability and studies how it scales with test-time compute, reinforcement learning, and pretraining.[4] Sources: [1] https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/ [2] https://www.nbcnews.com/tech/tech-news/ai-school-teacher-student-train-chatgpt-rcna248726 [3] https://www.marktechpost.com/2025/12/22/google-deepmind-researchers-release-gemma-scope-2-as-a-full-stack-interpretability-suite-for-gemma-3-models/ [4] https://openai.com/index/evaluating-chain-of-thought-monitorability/

4h ago

---

**[ICE Contracts Company Making Bounty Hunter AI Agents | AI Solutions 87 says on its website its AI agents “deliver rapid acceleration in finding persons of interest and mapping their entire network.”](https://www.reddit.com/r/artificial/comments/1ptpkc5/ice_contracts_company_making_bounty_hunter_ai/)**

AI Solutions 87 says on its website its AI agents “deliver rapid acceleration in finding persons of interest and mapping their entire network.”

🔗 [404 Media](https://www.404media.co/ice-contracts-company-making-bounty-hunter-ai-agents/) • 1h ago

---

**[I tried building a deterministic system to make AI safe, verifiable, auditable.](https://www.reddit.com/r/artificial/comments/1pto9go/i_tried_building_a_deterministic_system_to_make/)**

The idea is simple: LLMs guess. Businesses want proves. Instead of trusting AI confidence scores, I tried building a system that verifies outputs using SymPy (math), Z3 (logic), and AST (code). If you believe in determinism and think that it is the necessity and want to contribute, you are welcome to contribute, find and help me fix bugs which I must have failed in.

🔗 [GitHub](https://github.com/QWED-AI/qwed-verification) • 2h ago

---

---

## Google News: "ai"

**[Boys at her school shared AI-generated, nude images of her. After a fight, she was the one expelled](https://abcnews.go.com/US/wireStory/boys-school-shared-ai-generated-nude-images-after-128611202)**

A 13-year-old girl at a Louisiana middle school got into a fight with classmates who were sharing AI-generated nude images of her

ABC News • 1d ago

---

**[When the AI bubble bursts, humans will finally have their chance to take back control | Rafael Behr](https://www.theguardian.com/commentisfree/2025/dec/23/artificial-intelligence-ai-bubble-bursts-humans-take-back-control)**

The US economy is pumped up on tech-bro vanity. The inevitable correction should prompt a global conversation, says Guardian columnist Rafael Behr

The Guardian • 1h ago

---

**[TikTok’s Chinese owner plans $23bn AI spend to keep pace with US rivals](https://www.ft.com/content/9f550bb6-5708-41e3-aef6-ce8d7bb405ad)**

TikTok’s Chinese owner set to increase capital expenditure next year in effort to further build AI infrastructure

Financial Times • 9h ago

---

**[AI investors don't use most AI tools. Here are the ones they do use](https://qz.com/ai-investors-tools-agents-chatbots)**

qz.com • 11m ago

---

**[The AI dating arms race: Dating apps are betting millions that you'll fall back in love with them](https://www.businessinsider.com/dating-apps-bet-ai-will-increase-users-2025-12)**

Dating apps like Tinder, Hinge, Bumble, and Grindr are investing in AI-powered matchmaking, hoping to fend off swiping fatigue.

Business Insider • 37m ago

---

**[2 Artificial Intelligence ETFs to Confidently Buy Heading Into 2026](https://www.fool.com/investing/2025/12/23/2-ai-etfs-to-confidently-buy-heading-into-2026/)**

Both of these exchange-traded funds are beating the market in 2025 thanks to their concentrated portfolios of AI stocks.

The Motley Fool • 1h ago

---

**[60 of our biggest AI announcements in 2025](https://blog.google/technology/ai/google-ai-news-recap-2025/)**

Look back on Google AI news in 2025 across Gemini, Search, Pixel and more products.

blog.google • 16h ago

---

**[Google’s Chess Master Is Working on AI's Killer App](https://www.bloomberg.com/opinion/articles/2025-12-23/google-ai-boss-demis-hassabis-is-working-on-the-next-killer-app)**

You may have only recently heard about Demis Hassabis. He’s been named one of Time magazine’s “AI architects,” won a Nobel Prize for using the technology to predict protein folding and runs Google’s AI efforts. When the search giant acquired his company DeepMind in 2014, he embraced his new employer’s vast resources to build machines that surpassed human brainpower, so-called artificial general intelligence.

Bloomberg.com • 5h ago

---

**[Air Force Shutting Down AI Chatbot NIPRGPT](https://www.airandspaceforces.com/air-force-shutting-down-ai-chatbot-niprgpt/)**

NIPRGPT, the Air Force’s generative artificial intelligence chatbot, will shut down to make way for the new GenAI.mil platform.

Air & Space Forces Magazine • 16h ago

---

**[She Fell in Love With ChatGPT. Then She Ghosted It.](https://www.nytimes.com/2025/12/22/technology/ai-boyfriend-chatgpt.html)**

The New York Times • 1d ago

---

---

## HackerNews: "ai"

**[Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves](https://news.ycombinator.com/item?id=46355548)**

Flock left at least 60 of its people-tracking Condor PTZ cameras live streaming and exposed to the open internet.

⬆️ 593 • 💬 404 • 17h ago • [404 Media](https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/)

---

**[Autoland saves King Air, everyone reported safe](https://news.ycombinator.com/item?id=46346214)**

Aircraft landed safely at Rocky Mountain Metropolitan Airport near Denver on Saturday afternoon.

⬆️ 267 • 💬 170 • 1d ago • [AvBrief.com](https://avbrief.com/autoland-saves-king-air-everyone-reported-safe/)

---

**[Measuring AI Ability to Complete Long Tasks](https://news.ycombinator.com/item?id=46342166)**

⬆️ 242 • 💬 191 • 2d ago • [metr.org](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

---

**[Clair Obscur having its Indie Game Game Of The Year award stripped due to AI use](https://news.ycombinator.com/item?id=46342902)**

The Indie Game Awards presented the award last night, only to strip it hours later.

⬆️ 181 • 💬 399 • 2d ago • [TheGamer](https://www.thegamer.com/clair-obscur-expedition-33-indie-game-awards-goty-stripped-ai-use/)

---

**[How I protect my Forgejo instance from AI web crawlers](https://news.ycombinator.com/item?id=46345205)**

This article describes my nginx
configuration and strategy on how to prevent web crawlers from putting
down my instance while still serving most people with minimal amount of
friction.

⬆️ 168 • 💬 85 • 1d ago • [her.esy.fun](https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-instance-from-ai-web-crawlers/index.html)

---

**[Get an AI code review in 10 seconds](https://news.ycombinator.com/item?id=46346391)**

Personal Musings and Transcripts

⬆️ 139 • 💬 63 • 1d ago • [Oldmanrahul](https://oldmanrahul.com/2025/12/19/ai-code-review-trick/)

---

**[I announced my divorce on Instagram and then AI impersonated me](https://news.ycombinator.com/item?id=46352004)**

⬆️ 138 • 💬 166 • 1d ago • [eiratansey.com](https://eiratansey.com/2025/12/20/i-announced-my-divorce-on-instagram-and-then-ai-impersonated-me/)

---

**[I doubt that anything resembling genuine AGI is within reach of current AI tools](https://news.ycombinator.com/item?id=46342380)**

I doubt that anything resembling genuine "artificial general intelligence" is within reach of current #AI tools.  However, I think a weaker, but still quite valuable, type of "artificial general cleverness" is becoming a reality in various ways.

By "general cleverness", I mean the ability to solve broad classes of complex problems via somewhat ad hoc means.  These means may be stochastic or the result of brute force computation; they may be ungrounded or fallible; and they may be either uninterpretable, or traceable back to similar tricks found in an AI's training data.  So they would not qualify as the result of any true "intelligence".  And yet, they can have a non-trivial success rate at achieving an increasingly wide spectrum of tasks, particularly when coupled with stringent verification procedures to filter out incorrect or unpromising approaches, at scales beyond what individual humans could achieve.

This results in the somewhat unintuitive combination of a technology that can be very useful and impressive, while simultaneously being fundamentally unsatisfying and disappointing - somewhat akin to how one's awe at an amazingly clever magic trick can dissipate (or transform to technical respect) once one learns how the trick was performed.  

But perhaps this can be resolved by the realization that while cleverness and intelligence are somewhat correlated traits for humans, they are much more decoupled for AI tools (which are often optimized for cleverness), and viewing the current generation of such tools primarily as a stochastic generator of sometimes clever - and often useful - thoughts and outputs may be a more productive perspective when trying to use them to solve difficult problems.

⬆️ 134 • 💬 109 • 2d ago • [Mathstodon](https://mathstodon.xyz/@tao/115722360006034040)

---

**[MIRA – An open-source persistent AI entity with memory](https://news.ycombinator.com/item?id=46339537)**

This is the public release of MIRA OS. Discrete memories decay through momentum loss, tools auto-configure when dropped into tools/ folder, and the system prompt composes from modular trinkets. I w...

⬆️ 128 • 💬 53 • 2d ago • [GitHub](https://github.com/taylorsatula/mira-OSS)

---

**[iOS 26.3 Brings AirPods-Like Pairing to Third-Party Devices in EU Under DMA](https://news.ycombinator.com/item?id=46362927)**

The European Commission today praised the interoperability changes that Apple is introducing in iOS 26.3, once again crediting the Digital Markets Act (DMA) with bringing "new opportunities" to European users and developers. The Digital Markets Act requires Apple to provide third-party accessories with the same capabilities and access to device features that Apple's own products get. In iOS 26.3, EU wearable device makers can now test proximity pairing and improved notifications.

⬆️ 98 • 💬 57 • 3h ago • [MacRumors](https://www.macrumors.com/2025/12/22/ios-26-3-dma-airpods-pairing/)

---

---

## YouTube Videos: "ai"

**[AI Trends 2026: Quantum, Agentic AI &amp; Smarter Automation](https://www.youtube.com/watch?v=zt0JA5rxdfM)**

Ready to become a certified watsonx AI Assistant Engineer v1 - Professional? Register now and use code IBMTechYT20 for 20% ...

📺 IBM Technology

👁️ 21K • 👍 951 • 💬 39 • ⏱️ 11:39 • 22h ago

---

**[I Made the Same Animation in Every AI Video Generator](https://www.youtube.com/watch?v=UKp_zXdxVTI)**

I made the same AI Animation in every AI video generator Best All In One AI Video Generator ...

📺 Dan Kieft

👁️ 19K • 💬 50 • ⏱️ 44:39 • 16h ago

---

**[Google executive reveals if slowing AI is still possible](https://www.youtube.com/watch?v=Y1z2-Q8QRkM)**

Royal Hansen, vice president of privacy, safety and security engineering at Google, weighs in on the push to slow AI development ...

📺 Fox News

👁️ 27K • 👍 351 • 💬 218 • ⏱️ 4:26 • 1d ago

---

**[Which Crazy Bed Would You Choose? 🦋✨ | Ultimate Oddly Satisfying AI ASMR](https://www.youtube.com/watch?v=IJYkIQQsIw8)**

Which Crazy Bed Would You Choose? ✨ | Ultimate Oddly Satisfying AI ASMR: https://youtu.be/IJYkIQQsIw8 Which crazy bed ...

📺 Satisfy Hub ASMR

👁️ 1.1M • 👍 5K • 💬 234 • ⏱️ 8:24 • 2d ago

---

**[The Exact Moment The AI Bubble Burst…](https://www.youtube.com/watch?v=rrsZ0k7FPss)**

welcome to this month's episode of techbros vs basic care and consideration for the world around them. the techbros are winning.

📺 Fads

👁️ 239K • 👍 13K • 💬 2K • ⏱️ 19:40 • 2d ago

---

**[AI Bubble just CRASHED in SF](https://www.youtube.com/watch?v=3bGe4CkrLUM)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 157K • 👍 10K • 💬 3K • ⏱️ 16:54 • 1d ago

---

**[&quot;I CREATED AI AND I&#39;M HERE TO WARN YOU&quot;](https://www.youtube.com/watch?v=BFy4nIqaVLQ)**

AI progress is outpacing our ability to control it… because control ISN'T keeping up with capability. One of the people raising that ...

📺 The Diary Of A CEO

👁️ 100K • 👍 3K • 💬 134 • ⏱️ 1:29 • 1d ago

---

**[AI News: 28 Headlines No One Expected](https://www.youtube.com/watch?v=IT8LbiACH_g)**

Click here to learn more about VibeCode and Get your first 3 apps free using code “Wolfe”: https://vibecode.go.link/9G72M This ...

📺 Matt Wolfe

👁️ 67K • 👍 3K • 💬 207 • ⏱️ 37:38 • 2d ago

---

**[AI Isn’t Working](https://www.youtube.com/watch?v=4Xjx5c0z7io)**

Get Your Free US Stock Worth $50 From eToro - https://bit.ly/etoro-free-stock Oracle stock has collapsed by over 40% as investors ...

📺 Sasha Yanshin

👁️ 150K • 👍 7K • 💬 2K • ⏱️ 16:44 • 1d ago

---

**[Real vs AI Videos!](https://www.youtube.com/watch?v=BdBGTLJekWE)**

Need new glasses? Check out our partner Zenni Optical: https://zennipartners.pxf.io/PrestonReacts For 10% off your purchase at ...

📺 PrestonReacts

👁️ 164K • 👍 2K • 💬 434 • ⏱️ 15:32 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered)**

*Qwen*

Qwen-Image-Layered decomposes images into RGBA layers for inherent editability, enabling high-fidelity manipulation like resizing, recoloring, and object replacement. It supports variable and recursive layer decomposition for flexible image editing.

`image-text-to-image`

⬇️ 9,848 • ❤️ 572 • 4d ago

---

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is an efficient text-to-image diffusion transformer model (6B parameters) offering sub-second inference with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (EN/ZH), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 373,123 • ❤️ 3,323 • 14d ago

---

**[functiongemma-270m-it](https://huggingface.co/google/functiongemma-270m-it)**

*Google*

FunctionGemma 270M-IT is a lightweight, open Google model optimized for function calling tasks, suitable for fine-tuning on specific single or multi-turn agentic workflows. Its small size allows for deployment in resource-constrained environments, enabling custom app mechanics and offline personal device task execution.

`text-generation` `268.1M`

⬇️ 21,058 • ❤️ 492 • 4d ago

---

**[MiMo-V2-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash)**

*Xiaomi MiMo*

MiMo-V2-Flash is a 309B parameter Mixture-of-Experts (MoE) model with 15B active parameters, optimized for high-speed reasoning and agentic workflows. It features a hybrid attention architecture and Multi-Token Prediction (MTP) for efficient long-context processing (up to 256k) and accelerated inference, excelling in complex reasoning and coding tasks.

`text-generation` `309.8B`

⬇️ 10,832 • ❤️ 415 • 5d ago

---

**[HY-WorldPlay](https://huggingface.co/tencent/HY-WorldPlay)**

*Tencent*

HY-World 1.5 is a text-to-3D model enabling real-time, interactive world modeling with long-term geometric consistency. It uses a streaming video diffusion approach with novel memory management and RL post-training for applications like 3D reconstruction and scene generation.

`image-to-video`

⬇️ 3,313 • ❤️ 401 • 4d ago

---

**[TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B)**

*Microsoft*

TRELLIS.2-4B is a 4B parameter image-to-3D generative model that reconstructs arbitrary 3D assets with complex topologies and PBR materials from a single image using a novel O-Voxel representation and flow-matching transformer. It excels at high-fidelity generation up to 1536³ resolution with efficient inference, supporting features like transparency and sharp details.

`image-to-3d`

⬇️ 0 • ❤️ 364 • 56m ago

---

**[AWPortrait-Z](https://huggingface.co/Shakker-Labs/AWPortrait-Z)**

*Shakker Labs*

AWPortrait-Z is a LoRA for text-to-image generation, fine-tuned on Z-Image-Turbo to produce high-quality, realistic portraits with improved skin texture, controlled lighting, and diverse facial features, ideal for beauty and portrait applications.

`text-to-image`

⬇️ 6,493 • ❤️ 412 • 9d ago

---

**[GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)**

*Z.ai*

GLM-4.7 is a multilingual text generation model excelling in agentic coding, complex reasoning, and tool usage, with significant improvements in UI generation and web browsing capabilities.

`text-generation` `358.3B`

⬇️ 1,148 • ❤️ 350 • 35m ago

---

**[NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 is a 30B parameter LLM with a hybrid MoE/Mamba architecture, excelling in reasoning and general tasks across multiple languages. It generates reasoning traces before final answers for improved accuracy, supporting commercial use.

`text-generation` `31.6B`

⬇️ 110,376 • ❤️ 447 • 3d ago

---

**[chatterbox-turbo](https://huggingface.co/ResembleAI/chatterbox-turbo)**

*Resemble AI*

Chatterbox-Turbo is an efficient, open-source text-to-speech model (350M parameters) optimized for low-latency voice agents and narration. It features single-step mel-decoder generation and supports paralinguistic tags like [cough] and [laugh] for enhanced realism.

`text-to-speech`

⬇️ 0 • ❤️ 339 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Sharp Monocular View Synthesis in Less Than a Second](https://huggingface.co/papers/2512.10685)**

*Lars Mescheder, Wei Dong, Shiwei Li et al. (13 authors)*

🏢 Apple

SHARP synthesizes photorealistic views from a single image using a 3D Gaussian representation, achieving state-of-the-art results with rapid processing.

▲ 11 • 💬 2 • ⭐ 4,737 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2512.10685) • [💻 code](https://github.com/apple/ml-sharp) • [🔗 project](https://apple.github.io/ml-sharp/)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 10 • 💬 2 • ⭐ 12,979 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[Self-Supervised Prompt Optimization](https://huggingface.co/papers/2502.06855)**

*Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu et al. (9 authors)*

A self-supervised framework optimizes prompts for both closed and open-ended tasks by evaluating LLM outputs without external references, reducing costs and required data.

▲ 3 • 💬 0 • ⭐ 61,306 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.06855) • [💻 code](https://github.com/geekan/metagpt)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 120 • 💬 18 • ⭐ 47,541 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 137 • 💬 6 • ⭐ 18,908 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield](https://huggingface.co/papers/2511.22677)**

*Dongyang Liu, Peng Gao, David Liu et al. (11 authors)*

🏢 Tongyi-MAI

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.

▲ 27 • 💬 2 • ⭐ 7,680 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22677) • [💻 code](https://github.com/Tongyi-MAI/Z-Image/tree/main) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer](https://huggingface.co/papers/2511.22699)**

*Z-Image Team, Huanqia Cai, Sihan Cao et al. (21 authors)*

🏢 Tongyi-MAI

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.

▲ 208 • 💬 5 • ⭐ 7,668 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22699) • [💻 code](https://github.com/Tongyi-MAI/Z-Image) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling](https://huggingface.co/papers/2512.14614)**

*Wenqiang Sun, Haiyu Zhang, Haoyuan Wang et al. (10 authors)*

WorldPlay is a streaming video diffusion model that achieves real-time, interactive world modeling with long-term geometric consistency by using a Dual Action Representation, Reconstituted Context Memory, and Context Forcing.

▲ 61 • 💬 3 • ⭐ 673 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2512.14614) • [💻 code](https://github.com/Tencent-Hunyuan/HY-WorldPlay) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework](https://huggingface.co/papers/2512.17459)**

*Tobias Sautter, Jan-Niklas Dihlmann, Hendrik P. A. Lensch*

3D-RE-GEN reconstructs single images into modifiable 3D textured mesh scenes with comprehensive backgrounds, achieving top performance through compositional generation and scene optimization.

▲ 5 • 💬 1 • ⭐ 50 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2512.17459) • [💻 code](https://github.com/cgtuebingen/3D-RE-GEN) • [🔗 project](https://3dregen.jdihlmann.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 26 • 💬 1 • ⭐ 65,975 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 18.9k • 🔱 3.0k • 1d ago

---

**[Anionex/banana-slides](https://github.com/Anionex/banana-slides)**

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出 - An AI-native PPT generator based on nano banana pro🍌

`Python` `ai-ppt-maker` `ai-slide-builder` `ai-slides` `llm` `nanobananapro`

⭐ 5.8k • 🔱 646 • 1h ago

---

**[AndyMik90/Auto-Claude](https://github.com/AndyMik90/Auto-Claude)**

Autonomous multi-session AI coding

`TypeScript`

⭐ 2.5k • 🔱 336 • 10h ago

---

**[code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)**

#1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

`TypeScript` `ai` `ai-agents` `amp` `anthropic` `claude`

⭐ 2.5k • 🔱 183 • 1h ago

---

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

`Python` `ai-skills` `antigravity` `claude` `claude-code` `command-line`

⭐ 1.7k • 🔱 363 • 17d ago

---

**[TanShilongMario/PromptFill](https://github.com/TanShilongMario/PromptFill)**

一个专为 AI 绘画（Nano Banana 等）设计的“结构化提示词生成工具”。通过可视化的“填空”交互方式，帮助用户快速构建、管理和迭代复杂的 Prompt。

`JavaScript`

⭐ 1.2k • 🔱 189 • 10h ago

---

**[wusimpl/AntigravityQuotaWatcher](https://github.com/wusimpl/AntigravityQuotaWatcher)**

Google Antigravity AI模型配额监控插件

`TypeScript`

⭐ 1.1k • 🔱 55 • 5d ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 987 • 🔱 91 • 7h ago

---

**[datawhalechina/vibe-vibe](https://github.com/datawhalechina/vibe-vibe)**

首个系统化 Vibe Coding 开源教程 | 零基础到全栈实战，让人人都能用 AI 开发产品 | 在线地址：www.vibevibe.cn

`agent` `agentic-ai` `ai` `coding-assistant` `programming`

⭐ 939 • 🔱 91 • 23h ago

---

**[Hugo-Dz/spritefusion-pixel-snapper](https://github.com/Hugo-Dz/spritefusion-pixel-snapper)**

A tool to snap pixels to a perfect grid. Designed to fix messy and inconsistent pixel art generated by AI.

`Rust` `game-development` `gamedev` `image-processing` `pixel-art`

⭐ 919 • 🔱 25 • 15d ago

---

---

*Generated by PeekDeck - A glance is all you need*
