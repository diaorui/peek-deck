---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-07T20:55:07.936523+00:00'
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

**Last Updated:** February 07, 2026 at 20:55 UTC  
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

**[Report: OpenAI may tailor a version of ChatGPT for UAE that prohibits LGBTQ+ content](https://www.reddit.com/r/artificial/comments/1qy9vox/report_openai_may_tailor_a_version_of_chatgpt_for/)**

Countries have been building their own “sovereign AI” to reflect their culture and values, and OpenAI wants to help them....

🔗 [Sherwood News](https://sherwood.news/tech/report-openai-may-tailor-a-version-of-chatgpt-for-uae-that-prohibits-lgbtq/) • 11h ago

---

**[I built a geolocation tool that returns exact coordinates of any street photo within 3 minutes](https://www.reddit.com/r/artificial/comments/1qy775n/i_built_a_geolocation_tool_that_returns_exact/)**

I have been working solo on an AI-based project called Netryx. At a high level, it takes a street-level photo and attempts to determine the exact GPS coordinates where the image was taken. Not a city guess or a heatmap. The actual location, down to meters. If the system cannot verify the result with high confidence, it returns nothing. That behavior is intentional. Most AI geolocation tools will confidently give an answer even when they are wrong. Netryx is designed to fail closed. No verification means no output. Conceptually, it works in two stages. An AI model first narrows down likely areas based on visual features, either globally or within a user-defined region. A separate verification step then compares candidates against real street-level imagery. If verification fails, the result is discarded. This means it is not magic and not globally omniscient. The system requires pre-mapped street-level coverage to verify locations. Think of it as an AI-assisted visual index of physical space. As a test, I mapped roughly 5 square kilometers of Paris and fed in a random street photo from within that area. It identified the exact intersection in under three minutes. A few clarifications upfront: • It is not open source right now due to obvious privacy and abuse risks • It requires prior street-level coverage to return results • AI proposes candidates, verification gates all outputs • I am not interested in locating people from social media photos I am posting this here to get perspective from the security community. From a defensive angle, this shows how much location data AI can extract from ordinary images. From an offensive angle, the risks are clear. For those working in cybersecurity or AI security: where do you think the line is between a legitimate AI-powered OSINT capability and something that should not exist?

13h ago

---

**[Big Tech : AI Isn’t Taking Your Job. Your Refusal to Use It Might.](https://www.reddit.com/r/artificial/comments/1qyjrs6/big_tech_ai_isnt_taking_your_job_your_refusal_to/)**

Let’s say the quiet part out loud.

🔗 [Medium](https://medium.com/@behindthebuild/big-tech-ai-isnt-taking-your-job-your-refusal-to-use-it-might-966f8219f962) • 3h ago

---

**[AI Trajectories Through 2030: Analysis of Four Plausible Futures](https://www.reddit.com/r/artificial/comments/1qyjrtc/ai_trajectories_through_2030_analysis_of_four/)**

View AI Agent prediction on PardusAI - AI-powered data analysis platform

🔗 [pardusai.org](https://pardusai.org/view/fa19c538b421112c351c21f4018d955513b8dbd75c0b0b3a2a64bee4b7fc4080) • 3h ago

---

**[[WARNING] Kimi.com (ok computer + other agents) CRYPTO STEALING MALWARE](https://www.reddit.com/r/artificial/comments/1qyjktt/warning_kimicom_ok_computer_other_agents_crypto/)**

One of Kimi’s browser automation scripts uses a dark web library with crypto stealing malware: https://github.com/dnnyngyen/kimi-agent-internals/blob/main/source-code/browser_guard.py

3h ago

---

**[Roast my OSS AI memory graph engine > feedback on MVP?](https://www.reddit.com/r/artificial/comments/1qyoehj/roast_my_oss_ai_memory_graph_engine_feedback_on/)**

Hey fam, Been grinding on BrainAPI, this open-source thing that turns messy event logs into a smart knowledge graph for AI agents and rec systems. Think: feed it user clicks/buys/chats, it builds a precise map with cause-effect attribution (no BS hallucinations), then your AI retrieves fast AF for spot-on suggestions. Right now: Core APIs for saving/processing data -> works for CRM member matches/social networks (one user already using it for automated matches). Fast retrieval But ingestion? Slow as hell (10-30 min on small datasets) cuz of heavy LLM chains for precision. Trade-off for that "holy grail" accuracy, but yeah, it's a pain, optimizing soon. Repo: https://github.com/Lumen-Labs/brainapi2 What's the vibe? Bugs? Missing features? Use cases for ecom or agents? Roast it hard, I'm not fragile. If it slaps, star/fork. Building in public, hit me with thoughts!

29m ago

---

**[Goldman Sachs taps Anthropic’s Claude to automate accounting, compliance roles](https://www.reddit.com/r/artificial/comments/1qxv9jg/goldman_sachs_taps_anthropics_claude_to_automate/)**

Goldman Sachs is building AI agents with Anthropic’s Claude to automate trade accounting and client onboarding, aiming to speed work and boost efficiency.

🔗 [CNBC](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html) • 22h ago

---

**[AI is my peacekeeper, saving my sanity in step-parenting.](https://www.reddit.com/r/artificial/comments/1qyf5ag/ai_is_my_peacekeeper_saving_my_sanity_in/)**

I’m a solo web developer, so I spend most of my day using AI to debug my self made chaos , or manage my homelab as a fun side project. Or mess around with Arduino or 3D printing MCP servers. But recently, I asked Gemini for help with the hardest stack I’ve ever had to manage: a household with an extremely disrespectful 19 year old stepson. I am married with two step kids, the other is 15 and somewhat on the autistic spectrum. I've been in this family for for 7 years, married for 2. Their real dad bailed on them before I arrived and fell in love with my Soul Mate and best friend. If you’ve been there, you know the drill. The constant attitude, the tension between siblings, and the emotional toll it takes on your marriage. My wife and I were fed up, but every time we tried to talk to him, it devolved into a circular argument or a shouting match. He wouldn't understand, can't see our perspective, and continues to shit everything up. It was draining the life out of us. I decided to treat the conflict like a "System Architecture" problem and used Gemini to help us navigate it. Here’s how it changed the game for us. Sorry, not sorry, but I did use Gemini to summarise these shenanigans for me, as it really is a complex topic with emotions involved on my side. For what it's worth, I am very real and raw with Gemini in what I say about my family. As a 39 year old, I deeply understand the privacy issues, especially when ... Well, 90s kids don't trust the system... Which amazed me that I was doing this, telling Ai about this, but it shows how frustrated and desperate I was, to tell Google, of all companies, who removed their "do no evil" sign... Well... Anyway... Here it is: The "Logic Buffer": When you're angry, you say things that trigger defensiveness. The AI helped me translate raw frustration into firm, calm, adult-to-adult boundaries. I voice chat Gemini and it helped me work through some difficult thoughts. The Unified Front: It helped my wife and me build a literal Meeting Plan. It gave us roles, ideas, "anchor phrases" to use when things got heated, and a strategy to stay aligned so we couldn't be "divided and conquered." The "Adult Choice" Framework: It shifted the dynamic from us "punishing" a kid to us "managing a household of adults." The AI scripted an ultimatum that wasn't a threat, but a choice: You can be a respectful member of this house, or you can choose to find a living situation that better fits your current attitude. Emotional Outsourcing: It took the mental load of "What do I say?" and turned it into a checklist. We walked into that room feeling like a professional team with a script, rather than two exhausted parents winging it. The result? The most productive, calm, and clear conversation we’ve ever had with him. No yelling. No "what-abouts." Just clear boundaries and a path forward. I see a lot of talk about AI taking jobs, but for me, it’s giving me my home back. It’s like having a high-level consultant for your personal life who doesn’t get tired, emotional, or biased. Has anyone else used LLMs for "Soft Skills" or family mediation? It feels like a total superpower for conflict resolution. _ Me again, I asked it for some examples.. here it is raw from AI again: Example 1: The "Translation" (Emotional to Logical) The Chaos: I wanted to tell him, "You're being a lazy, entitled brat and you're making your mother miserable." The AI Refinement: "We value having you here, but the current lack of respect for the household peace is unsustainable. We are moving to an adult-to-adult living agreement where respect is the 'rent' for staying in this home." Example 2: The "Anchor Phrase" for High-Conflict The Chaos: Usually, he’d say something rude, I’d get defensive, and we’d yell for 20 minutes. The AI Solution: It gave us an "Anchor Phrase." Whenever he tried to derail the talk, we simply said: "We aren't here to argue about the past; we are here to decide if you can meet the standards of this house moving forward." Having that script prevented the "emotional hijack" that usually ruins these talks. Example 3: Managing the "Unified Front" The Chaos: In the past, he’d wait until I was in the workshop and then give his mom a hard time, or vice versa. The AI Plan: The AI helped us set a "Veto Rule." If he asks one of us something, the answer is always: "I’ll discuss that with [Alice/Partner] and we will get back to you together." It shut down the "divide and conquer" tactic instantly. Thanks for enjoying the chaos with me. I sincerely hope other families use this to their advantage. I have been very impressed with the assistance. The meetings have been way more productive. I imagine there will be more issues in the future, but the relief and support I received from AI has already made a huge difference in this young man's attitude, my wife's mental health, his brother's Daily life and... Yeah, definitely my own. I sleep way better now. Still tough, but I know I have support now.

6h ago

---

**[AI model can read and diagnose a brain MRI in seconds](https://www.reddit.com/r/artificial/comments/1qy24st/ai_model_can_read_and_diagnose_a_brain_mri_in/)**

An AI-powered model developed at University of Michigan can read a brain MRI and diagnose a person in seconds, a study suggests.&nbsp;It detected neurological conditions with up to 97.5% accuracy and predicted how urgently a patient required treatment. The technology&nbsp;could transform neuroimaging at health systems across the United States.

🔗 [EurekAlert!](https://www.eurekalert.org/news-releases/1115393) • 18h ago

---

**[Anthropic and OpenAI released flagship models 27 minutes apart -- the AI pricing and capability gap is getting weird](https://www.reddit.com/r/artificial/comments/1qxdz7q/anthropic_and_openai_released_flagship_models_27/)**

Anthropic shipped Opus 4.6 and OpenAI shipped GPT-5.3-Codex on the same day, 27 minutes apart. Both claim benchmark leads. Both are right -- just on different benchmarks. Where each model leads Opus 4.6 tops reasoning tasks: Humanity's Last Exam (53.1%), GDPval-AA (144 Elo ahead of GPT-5.2), BrowseComp (84.0%). GPT-5.3-Codex takes coding: Terminal-Bench 2.0 at 75.1% vs Opus 4.6's 69.9%. The pricing spread is hard to ignore Model Input/M Output/M Gemini 3 Pro $2 $12.00 GPT-5.2 $1.75 $14.00 Opus 4.6 $5.00 $25.00 MiMo V2 Flash $0.10 $0.30 Opus 4.6 costs 2x Gemini on input. Open-source alternatives cost 50x less. At some point the benchmark gap has to justify the price gap -- and for many tasks it doesn't. 1M context is becoming table stakes Opus 4.6 adds 1M tokens (beta, 2x pricing past 200K). Gemini already offers 1M at standard pricing. The real differentiator is retrieval quality at that scale -- Opus 4.6 scores 76% on MRCR v2 (8-needle, 1M), which is the strongest result so far. Market reaction was immediate Thomson Reuters stock fell 15.83%, LegalZoom dropped nearly 20%. Frontier model launches are now moving SaaS valuations in real time. The tradeoff nobody expected Opus 4.6 gets writing quality complaints from early users. The theory: RL optimizations for reasoning degraded prose output. Models are getting better at some things by getting worse at others. No single model wins across the board anymore. The frontier is fragmenting by task type. GPT-5.3-Codex pricing has not been disclosed at time of writing. Gemini offers 1M context at standard pricing; Claude charges 2x for prompts exceeding 200K tokens. Source with full benchmarks and analysis: Claude Opus 4.6: 1M Context, Agent Teams, Adaptive Thinking, and a Showdown with GPT-5.3

1d ago

---

---

## Google News: "ai"

**[Tech AI spending may approach $700 billion this year, but the blow to cash raises red flags](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html)**

Tech's megacaps announced major increases in capex spend for 2026, and now investors are preparing for cash to dwindle.

CNBC • 23h ago

---

**[Amazon leads Big Tech’s $1 trillion wipeout as AI bubble fears ignite sell-off](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)**

Fears over AI spending have sparked a sell-off among tech stocks.

CNBC • 1d ago

---

**[The AI Trade Enters a New Era of Skepticism](https://www.barrons.com/articles/dow-50000-ai-trade-skepticism-353375f4?gaa_at=eafs&gaa_n=AWEtsqe-Qw15q6r6PhfoIXRBkOD3KSKUH_nZNq2WPoBXOCzmZWEH47fjF8ZK&gaa_ts=6987aa17&gaa_sig=fMM7EJq37F6S29BPc_-Jl-_zlJ7SJv7uo40ejKI6GBuXwEYrKHGpvhz7FND4sw7TdQfFf_2oxIrj9V8d88oLag%3D%3D)**

Barron's • 23h ago

---

**[The AI boom is so huge it’s causing shortages everywhere else](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

The Washington Post • 2h ago

---

**[Here’s Where AI Is Tearing Through Corporate America](https://www.wsj.com/tech/ai/ai-software-business-stock-market-4b17b432?gaa_at=eafs&gaa_n=AWEtsqdox3JIApEhtN8eD7XlvGef5BkcQctaVKSAjB-Xl5L_Zb0pcRGHD507&gaa_ts=6987aa17&gaa_sig=8Rs_HLq8Sra9GknNBZA-FrKAS25EZtN5d92MzDg3U76CkGyRhyiR3nTl4FmKnM6RMwesPZPOxOE2k_G-2OhH1Q%3D%3D)**

The Wall Street Journal • 18h ago

---

**[AI wiped out $400 billion this week — and it's only getting started](https://www.axios.com/2026/02/07/ai-software-anthropic-losses-stock-market)**

AI isn't just hitting software valuations — it's changing how software companies operate.

Axios • 10h ago

---

**[AI fears pummel software stocks: Is it 'illogical' panic or a SaaS apocalypse?](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html)**

The software space is facing serious market concerns this week, after the release of new AI tools from AI triggered a market sell-off.

CNBC • 1d ago

---

**[This AI Stock Could Be One of the Most Valuable in the World by 2027](https://finance.yahoo.com/news/ai-stock-could-one-most-190900911.html)**

Alphabet is already one of the most valuable companies in the world, but it's betting big on being the biggest artificial intelligence (AI) company as well.

Yahoo Finance • 1h ago

---

**[Tech’s AI Push Risks a Bond Market Blowback: Credit Weekly](https://www.bloomberg.com/news/articles/2026-02-07/tech-s-ai-push-risks-a-bond-blowback-amzn-googl-msft-orcl)**

Bloomberg.com • 1h ago

---

**[New study uses Neanderthals to demonstrate gap between generative AI and scholarly knowledge](https://phys.org/news/2026-02-neanderthals-gap-generative-ai-scholarly.html)**

Phys.org • 1d ago

---

---

## HackerNews: "ai"

**[My AI Adoption Journey](https://news.ycombinator.com/item?id=46903558)**

⬆️ 925 • 💬 395 • 2d ago • [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

---

**[A new bill in New York would require disclaimers on AI-generated news content](https://news.ycombinator.com/item?id=46910963)**

A new bill in the New York state legislature would require news organizations to label AI-generated material and mandate that humans review any such content before publication. On Monday, Senator Patricia Fahy (D-Albany) and Assemblymember Nily Rozic (D-NYC) introduced the bill, called The New York…

⬆️ 554 • 💬 232 • 1d ago • [Nieman Lab](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

---

**[How to effectively write quality code with AI](https://news.ycombinator.com/item?id=46916586)**

AI is rarely optional anymore, but how can you still be proud of your craft? Discover the workflow to effectively write high-quality, robust code using AI tools.

⬆️ 310 • 💬 278 • 1d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/)

---

**[Monty: A minimal, secure Python interpreter written in Rust for use by AI](https://news.ycombinator.com/item?id=46918254)**

A minimal, secure Python interpreter written in Rust for use by AI - pydantic/monty

⬆️ 292 • 💬 156 • 23h ago • [GitHub](https://github.com/pydantic/monty)

---

**[The AI boom is causing shortages everywhere else](https://news.ycombinator.com/item?id=46922969)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

⬆️ 160 • 💬 199 • 9h ago • [The Washington Post](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)

---

**[India's female workers watching hours of abusive content to train AI](https://news.ycombinator.com/item?id=46906590)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

⬆️ 122 • 💬 198 • 1d ago • [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai)

---

**[Show HN: Smooth CLI – Token-efficient browser for AI agents](https://news.ycombinator.com/item?id=46901233)**

Give your AI agent a browser that actually works

⬆️ 94 • 💬 70 • 2d ago • [docs.smooth.sh](https://docs.smooth.sh/cli/overview)

---

**[Sam Altman responds to Anthropic's "Ads are coming to AI. But not to Claude" ads](https://news.ycombinator.com/item?id=46894151)**

⬆️ 88 • 💬 107 • 2d ago • [X (formerly Twitter)](https://twitter.com/sama/status/2019139174339928189)

---

**[Amazon plunge continues $1T wipeout as AI bubble fears ignite sell-off](https://news.ycombinator.com/item?id=46913302)**

Fears over AI spending have sparked a sell-off among tech stocks.

⬆️ 88 • 💬 87 • 1d ago • [CNBC](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)

---

**[Man who videotaped himself BASE jumping in Yosemite arrested, says it was AI](https://news.ycombinator.com/item?id=46916961)**

A California man is facing a criminal charge for allegedly BASE jumping off Glacier Point in Yosemite National Park during the federal government shutdown last year.

⬆️ 54 • 💬 90 • 1d ago • [Los Angeles Times](https://www.latimes.com/california/story/2026-02-05/man-videotaped-himself-base-jumping-in-yosemite-federal-officials-say-he-says-it-was-ai)

---

---

## YouTube Videos: "ai"

**[🚨ALARMING! An AI Just Wiped Out $285B From The Financial Markets…🔥](https://www.youtube.com/watch?v=lRwduk14uHY)**

1. Get 90% OFF A Course Today: https://www.neilmccoyward.com/courses 2. My Investment Portfolio Join THOUSANDS of ...

📺 Neil McCoy-Ward

👁️ 65K • 👍 5K • 💬 579 • ⏱️ 19:58 • 1d ago

---

**[Trump Posts Shocking AI Video Showing the Obamas as Apes](https://www.youtube.com/watch?v=V86R2ZJPXzI)**

The White House deleted a video posted on President Trump's Truth Social that included a clip depicting former President Barack ...

📺 New York Post

👁️ 38K • 👍 294 • 💬 597 • ⏱️ 2:07 • 23h ago

---

**[EXACTLY How to Start Making AI Influencers and get RICH](https://www.youtube.com/watch?v=UTcTcgum1-U)**

Create AI Influencers using Higgsfield https://youricreates.com/Higgsfield-AI In this video, I break down how AI influencers are ...

📺 Youri van Hofwegen

👁️ 7K • 💬 6 • ⏱️ 8:07 • 4h ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 181K • 👍 4K • 💬 791 • ⏱️ 13:31 • 2d ago

---

**[OpenAI&#39;s New GPT 5.3 Shocks Anthropic As Opus 4.6 Strikes Back (AI War Explodes)](https://www.youtube.com/watch?v=ydW6Io2T4ho)**

AI coding just entered a new phase of competition. In the same week, OpenAI unveiled GPT-5.3-Codex, a faster, more capable ...

📺 AI Revolution

👁️ 20K • 👍 611 • 💬 31 • ⏱️ 13:09 • 21h ago

---

**[not good for OPENCLAW](https://www.youtube.com/watch?v=ceEUO_i7aW4)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 72K • 👍 3K • 💬 704 • ⏱️ 18:15 • 18h ago

---

**[The White Collar AI APOCALYPSE Is HERE](https://www.youtube.com/watch?v=ur295T83Wg4)**

Krystal and Saagar discuss tech stocks tumbling amid emerging new fears of job loss and AI. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 352K • 👍 10K • 💬 2K • ⏱️ 24:33 • 2d ago

---

**[Nvidia CEO Jensen Huang: AI is going to fundamentally change how we compute everything](https://www.youtube.com/watch?v=P9dX_ek_6yY)**

Jensen Huang, NVIDIA CEO, joins CNBC's "Halftime Report to discuss the power of Artificial Intelligence and where he sees the ...

📺 CNBC Television

👁️ 119K • 👍 2K • 💬 413 • ⏱️ 8:35 • 1d ago

---

**[The Two Best AI Models/Enemies Just Got Released Simultaneously](https://www.youtube.com/watch?v=1PxEziv5XIU)**

The two models that you will hear discussed for at least the next two months - Claude Opus 4.6 and GPT 5.3 Codex - just got ...

📺 AI Explained

👁️ 53K • 👍 2K • 💬 294 • ⏱️ 19:50 • 1d ago

---

**[How AI is helping her speak again!](https://www.youtube.com/watch?v=-ANej33sbOQ)**

This is an amazing use of AI! evolving.ai on IG #ai #technology #advancements #medical ✰ ABOUT ME ✰ I'm Dr. Myro ...

📺 Doctor Myro

👁️ 395K • 👍 15K • 💬 650 • ⏱️ 0:44 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling at table recognition, formula extraction, and information extraction across diverse layouts. It offers state-of-the-art performance with efficient inference, supporting deployment via vLLM, SGLang, and Ollama for real-world business applications.

`image-to-text`

⬇️ 204,109 • ❤️ 772 • 4d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is an 80B parameter (3B active) LLM optimized for coding agents, featuring advanced agentic capabilities like long-horizon reasoning and tool usage. It boasts a 256k context length for seamless IDE integration and efficient local development.

`text-generation` `79.7B`

⬇️ 53,491 • ❤️ 577 • 4d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text` `170.7B`

⬇️ 335,220 • ❤️ 1,813 • 2d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 11,980 • ❤️ 511 • 15h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 60,581 • ❤️ 498 • 6d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and full-duplex live streaming, rivaling proprietary models like GPT-4o and Gemini 2.5 Flash. It offers advanced OCR, bilingual real-time conversation with voice cloning, and proactive omnimodal interaction for fluid, real-time experiences.

`any-to-any` `9.4B`

⬇️ 5,568 • ❤️ 582 • 4h ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio music generation model capable of producing commercial-ready music with precise stylistic control and editing features. It utilizes a hybrid LM-DiT architecture trained on licensed and royalty-free data, offering extreme speed and low VRAM requirements for consumer hardware, making it ideal for music artists and content creators.

`text-to-audio`

⬇️ 19,901 • ❤️ 430 • 4d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a 4B-parameter, multilingual speech-to-text model offering near-offline accuracy with <500ms latency. It features a streaming architecture for real-time applications like voice assistants and live subtitling, optimized for on-device deployment.

⬇️ 2,093 • ❤️ 363 • 2d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 166,132 • ❤️ 206 • 2d ago

---

**[Intern-S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro)**

*Intern Large Models*

Intern-S1-Pro is a trillion-scale MoE multimodal scientific reasoning model, excelling in AI4Science domains (chemistry, materials, life-science, earth) with strong general multimodal and text capabilities, supporting long, heterogeneous time-series data.

`image-text-to-text`

⬇️ 7,351 • ❤️ 189 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 137 • 💬 12 • ⭐ 2,267 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,217 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,455 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,451 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 3 • 💬 0 • ⭐ 30,470 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 119 • 💬 2 • ⭐ 2,635 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 60 • 💬 1 • ⭐ 7,069 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,354 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 28,000 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 113 • 💬 7 • ⭐ 70,357 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 13.1k • 🔱 755 • 1d ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.1k • 🔱 537 • 2h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.8k • 🔱 10.3k • 6h ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 7.8k • 🔱 1.6k • 14h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.5k • 🔱 734 • 3d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 4.5k • 🔱 357 • 3d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.3k • 🔱 358 • 15d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 377 • 15d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.7k • 🔱 258 • 19d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 2.3k • 🔱 106 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
