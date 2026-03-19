---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-19T02:24:42.666871+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 19, 2026 at 02:24 UTC  
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

**[The Pentagon is developing its own LLMs | TechCrunch](https://www.reddit.com/r/artificial/comments/1rx1k64/the_pentagon_is_developing_its_own_llms_techcrunch/)**

Russia aids Iran against U.S. ships. Oil surges 50%. Joe Kent resigns. DOGE cuts grants via AI. Trump creates a secret database. Hawley targets mifepristone. Vance leads fraud task force.

🔗 [Instrumental Communications](https://www.instrumentalcomms.com/blog/a-new-exoskeleton#story-the-pentagon-is-developing-its-own-llms) • 14h ago

---

**[The Moltbook acquisition makes a lot more sense when you read one of Meta's patent filings](https://www.reddit.com/r/artificial/comments/1rwyk17/the_moltbook_acquisition_makes_a_lot_more_sense/)**

Last week's post about Meta buying Moltbook got a lot of discussion here. I think most of the coverage (and the comments) missed what Meta is actually doing with it. I read a lot of patent filings because LLMs make them surprisingly accessible now, and one filed by Meta's CTO Andrew Bosworth connects directly to the Moltbook acquisition in a way I haven't seen anyone talk about. In December 2025, Meta was granted patent US 12513102B2 for a system that trains a language model on a user's historical interactions (posts, comments, likes, DMs, voice messages) and deploys it to simulate that user's social media behavior autonomously. The press covered it as "Meta wants to post for you after you die." The actual patent text describes simulating any user who is "absent from the social networking system," which includes breaks, inactivity, or death. The deceased framing is a broadening mechanism for the claims. What they built is a personalized LLM that maintains engagement on behalf of any user, for any reason. Now layer in the acquisitions. December 2025: Meta buys Manus for over $2 billion. General-purpose AI agent platform, hit $100M ARR eight months after launch. Meta said they'd integrate it into their consumer and business products. March 2026: The Moltbook acqui-hire. Matt Schlicht and Ben Parr join Meta Superintelligence Labs. What most coverage left out is their background. Schlicht and Parr co-founded Octane AI, a conversational commerce platform that automated personalized customer interactions for Shopify merchants via Messenger and SMS. They've been building AI-driven business communication tools since 2016. I think these three moves are connected. The "digital ghost" and "AI agents chatting with each other" framings are both wrong. Bosworth himself said in an Instagram Q&A that he didn't find Moltbook's agent conversations particularly interesting. So why buy it? Because Meta is building infrastructure for AI agents that act on behalf of businesses across their platforms. The small business owner spending hours managing their Facebook and Instagram presence is the real target user. The e-commerce brand running customer conversations through WhatsApp is the real target user. The patent gives them the IP foundation, Manus gives them the agent platform, and the Schlicht/Parr hire gives them the team that spent a decade figuring out how to make this work commercially. I'll be honest about the limits of reading patent tea leaves. Companies file for all kinds of reasons and most aren't strategic. Engineers get bonuses for filings. Legal teams build portfolios for cross-licensing leverage. Reading a single patent as a roadmap is a mistake I've made before. But a patent plus $2B in acquisitions plus an acqui-hire of people who built a related product for a decade starts to look like a pattern. Anyone here have a different read? Especially curious if anyone on Meta's business tools side sees this differently.

17h ago

---

**[Robot dogs priced at $300,000 a piece are now guarding some of the country’s biggest data centers](https://www.reddit.com/r/artificial/comments/1rx8q9x/robot_dogs_priced_at_300000_a_piece_are_now/)**

AI companies are turning to quadruped robots, better known as “robot dogs” for security solutions to protect their vast data centers.

🔗 [Fortune](https://fortune.com/2026/03/17/robot-dog-patrols-data-centers-ai-infrastructure-buildout/) • 9h ago

---

**[If you are using ChatGPT, you would probably want an AI policy. [I will not promote]](https://www.reddit.com/r/artificial/comments/1rx8hfr/if_you_are_using_chatgpt_you_would_probably_want/)**

I’ve been looking into AI governance for my company recently so wanted to share some of my findings. Apparently PwC put out a report saying 72% of companies have absolutely zero formal AI policy. For startups and small agencies i guess it would probably reach 90%? Even if you’re only a 5-person team, doing nothing is starting to become a liability. Without rules, someone would eventually paste client data, financials, or proprietary code into ChatGPT to save time. Most of these tools train on user inputs, that’s a trouble waiting to happen. You don’t need a 20-page legal manifesto. A basic 3-page Google Doc is plenty. It just needs to cover: Which specific AI tools are approved for work. A Red / Yellow / Green framework for what data can and cannot be pasted into them. Rules for when AI-generated content must be disclosed to clients. Who is in charge of approving new tools. Consequences for violating the policy. Obviously, have a lawyer glance at it before you finalize anything, especially if you handle sensitive data but even writing a DIY version using the bullet points above is 100x better than having nothing.

10h ago

---

**[How I use AI through a repeatable and programmable workflow to stop fixing the same mistakes over and over](https://www.reddit.com/r/artificial/comments/1rxd6q2/how_i_use_ai_through_a_repeatable_and/)**

Quick context: I use AI heavily in daily development, and I got tired of the same loop. Good prompt asking for a feature -> okay-ish answer -> more prompts to patch it -> standards break again -> rework. The issue was not "I need a smarter model." The issue was "I need a repeatable process." The real problem Same pain points every time: AI lost context between sessions it broke project standards on basic things (naming, architecture, style) planning and execution were mixed together docs were always treated as "later" End result: more rework, more manual review, less predictability. What I changed in practice I stopped relying on one giant prompt and split work into clear phases: /pwf-brainstorm to define scope, architecture, and decisions /pwf-plan to turn that into executable phases/tasks optional quality gates: /pwf-checklist /pwf-clarify /pwf-analyze /pwf-work-plan to execute phase by phase /pwf-review for deeper review /pwf-commit-changes to close with structured commits If the task is small, I use /pwf-work, but I still keep review and docs discipline. The rule that changed everything /pwf-work and /pwf-work-plan read docs before implementation and update docs after implementation. Without this, AI works half blind. With this, AI works with project memory. This single rule improved quality the most. References I studied (without copy-pasting) Compound Engineering Superpowers Spec Kit Spec-Driven Development I did not clone someone else's framework. I extracted principles, adapted them to my context, and refined them with real usage. Real results For me, the impact was direct: fewer repeated mistakes less rework better consistency across sessions more output with fewer dumb errors I had days closing 25 tasks (small, medium, and large) because I stopped falling into the same error loop. Project structure that helped a lot I also added a recommended structure in the wiki to improve AI context: one folder for code repos one folder for workspace assets (docs, controls, configs) Then I open both as multi-root in the editor (VS Code or Cursor), almost like a monorepo experience. This helps AI see the full system without turning things into chaos. Links Repository: https://github.com/J-Pster/Psters_AI_Workflow Wiki (deep dive): https://github.com/J-Pster/Psters_AI_Workflow/wiki If you want to criticize, keep it technical. If you want to improve it, send a PR.

🔗 [GitHub](https://github.com/J-Pster/Psters_AI_Workflow) • 7h ago

---

**[Jensen Huang says gamers are 'completely wrong' about DLSS 5 — Nvidia CEO responds to DLSS 5 backlash](https://www.reddit.com/r/artificial/comments/1rwl37x/jensen_huang_says_gamers_are_completely_wrong/)**

The CEO says artistic control remains with developers.

🔗 [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/jensen-huang-says-gamers-are-completely-wrong-about-dlss-5-nvidia-ceo-responds-to-dlss-5-backlash) • 1d ago

---

**[Zanita Kraklëin - Electric Velvet](https://www.reddit.com/r/artificial/comments/1rxhwvo/zanita_kraklëin_electric_velvet/)**

4h ago

---

**[Communication nowadays](https://www.reddit.com/r/artificial/comments/1rxfu8o/communication_nowadays/)**

We are, in a sense, large language models ourselves, and much of our communication in this alienated era now takes place through social media: because of this, many of us could be replicated by bots with surprisingly little change to the overall pattern of interaction. Thoughts?

5h ago

---

**[Are marketing jobs truly threatened by AI?](https://www.reddit.com/r/artificial/comments/1rwut6e/are_marketing_jobs_truly_threatened_by_ai/)**

Or has it created new opportunities, increased productivity, or had no influence at all. And do you expect it to in the future?

21h ago

---

**[Are we cooked?](https://www.reddit.com/r/artificial/comments/1rxlekb/are_we_cooked/)**

I've been writing prompts since 2022 and using the SaaS frontier models since GPT jumped, and I'm seeing something happen faster than anyone could have imagined. The convergence of AI and Biotech is screaming toward a singularity and superintelligence at breakneck speeds. Lumps of flesh playing Doom. Uploading a fruit fly into the bug matrix. It's crazy.

2h ago

---

---

## Google News: "ai"

**[Introducing “vibe design” with Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)**

Stitch is evolving into an AI-native platform that allows anyone to create, iterate, and collaborate on high-fidelity UI.

blog.google • 8h ago

---

**[Anthropic turns the tables on OpenAI in critical revenue category](https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai)**

Axios • 16h ago

---

**[Blackburn’s new AI framework seeks to codify Trump’s desires](https://www.politico.com/live-updates/2026/03/18/congress/blackburn-ai-framework-seeks-to-codify-trump-ratepayer-pledge-00834829)**

Politico • 1h ago

---

**[Alibaba AI Business Is ‘Free Call Option,’ First Eagle Fund Says](https://www.bloomberg.com/news/articles/2026-03-19/alibaba-ai-business-is-free-call-option-first-eagle-fund-says)**

Bloomberg.com • 54m ago

---

**[AI fakes about Iran-US war swirl on X despite policy crackdown](https://www.yahoo.com/news/articles/ai-fakes-iran-us-war-020802137.html)**

AI-created videos circulating on Elon Musk's X depict American soldiers captured by Iran, an Israeli city in ruins, and US embassies ablaze -- a surge of lifelike deepfakes despite a policy crackdown ...

Yahoo • 16m ago

---

**[The Cost of the A.I. Boom: A Trade Deficit the President Detests](https://www.nytimes.com/2026/03/18/business/economy/us-trade-deficit-ai-boom.html)**

The New York Times • 17h ago

---

**[Val Kilmer Resurrected by AI to Star in ‘As Deep as the Grave’ Movie — First Look (EXCLUSIVE)](https://variety.com/2026/film/news/val-kilmer-ai-film-as-deep-as-the-grave-1236691042/)**

First look at Val Kilmer in his new film "As Deep As the Grave." His performance was AI generated.

Variety • 11h ago

---

**[An AI-generated version of the late Val Kilmer is starring in a new movie](https://www.nbcnews.com/tech/tech-news/val-kilmer-ai-generated-new-movie-rcna264195)**

The filmmakers behind “As Deep as the Grave” said they obtained permission from the late actor’s estate to use his likeness.

NBC News • 3h ago

---

**[Val Kilmer set to be be resurrected with AI for new film](https://www.theguardian.com/film/2026/mar/18/val-kilmer-resurrected-in-movie-ai)**

As Deep As the Grave, the true story of 1920s archeologists, will bring late actor back with support from his estate

The Guardian • 7h ago

---

**[We asked experts about the most responsible ways to use AI tools – here’s what they said](https://www.theguardian.com/lifeandstyle/ng-interactive/2026/mar/18/how-to-use-ai-tools-expert-guide)**

Use AI as a brainstorming partner and organizer, but don’t outsource your judgment

The Guardian • 9h ago

---

---

## HackerNews: "ai"

**[Mistral AI Releases Forge](https://news.ycombinator.com/item?id=47418295)**

Today, we’re introducing Forge, a system that allows enterprises to build frontier-grade AI models grounded in their proprietary knowledge.

⬆️ 703 • 💬 179 • 1d ago • [mistral.ai](https://mistral.ai/news/forge)

---

**[AirPods Max 2](https://news.ycombinator.com/item?id=47398681)**

The ultimate over-ear listening experience — in five vibrant colors and with up to 1.5x more Active Noise Cancellation than the previous generation.

⬆️ 318 • 💬 553 • 2d ago • [Apple](https://www.apple.com/airpods-max/)

---

**[AI coding is gambling](https://news.ycombinator.com/item?id=47428541)**

GambleAI

I’ve been coding a lot with AI since November, when we all noticed it got really good. And it is quite good for instantly generating something th...

⬆️ 313 • 💬 383 • 9h ago • [VS Notes](https://notes.visaint.space/ai-coding-is-gambling/)

---

**[Snowflake AI Escapes Sandbox and Executes Malware](https://news.ycombinator.com/item?id=47427017)**

A vulnerability in the Snowflake Cortex Code CLI allowed malware to be installed and executed via indirect prompt injection, bypassing human-in-the-loop command approval and escaping the sandbox.

⬆️ 229 • 💬 73 • 10h ago • [promptarmor.com](https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware)

---

**[Nvidia Launches Vera CPU, Purpose-Built for Agentic AI](https://news.ycombinator.com/item?id=47404074)**

NVIDIA today launched the NVIDIA Vera CPU, the world’s first processor purpose-built for the age of agentic AI and reinforcement learning — delivering results with twice the efficiency and 50% faster than traditional rack-scale CPUs.

⬆️ 175 • 💬 100 • 2d ago • [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

---

**[Why AI systems don't learn – On autonomous learning from cognitive science](https://news.ycombinator.com/item?id=47418722)**

We critically examine the limitations of current AI models in achieving autonomous learning and propose a learning architecture inspired by human and animal cognition. The proposed framework integrates learning from observation (System A) and learning from active behavior (System B) while flexibly switching between these learning modes as a function of internally generated meta-control signals (System M). We discuss how this could be built by taking inspiration on how organisms adapt to real-world, dynamic environments across evolutionary and developmental timescales.

⬆️ 173 • 💬 106 • 1d ago • [arXiv.org](https://arxiv.org/abs/2603.15381)

---

**[Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)](https://news.ycombinator.com/item?id=47401734)**

Large language models (LLMs) have demonstrated the promise to revolutionize the field of software engineering. Among other things, LLM agents are rapidly gaining momentum in software development, with practitioners reporting a multifold increase in productivity after adoption. Yet, empirical evidence is lacking around these claims. In this paper, we estimate the causal effect of adopting a widely popular LLM agent assistant, namely Cursor, on development velocity and software quality. The estimation is enabled by a state-of-the-art difference-in-differences design comparing Cursor-adopting GitHub projects with a matched control group of similar GitHub projects that do not use Cursor. We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity. Further panel generalized-method-of-moments estimation reveals that increases in static analysis warnings and code complexity are major factors driving long-term velocity slowdown. Our study identifies quality assurance as a major bottleneck for early Cursor adopters and calls for it to be a first-class citizen in the design of agentic AI coding tools and AI-driven workflows.

⬆️ 147 • 💬 80 • 2d ago • [arXiv.org](https://arxiv.org/abs/2511.04427)

---

**[Apideck CLI – An AI-agent interface with much lower context consumption than MCP](https://news.ycombinator.com/item?id=47400261)**

TL;DR: MCP tool definitions can burn 55,000+ tokens before an agent processes a single user message. We built the Apideck CLI as an AI-agent interface instead:an ~80-token agent prompt replaces tens of thousands of tokens of schema, with progressive disclosure via `--help` and structural safety baked into the binary. Any agent that can run shell commands can use it. No protocol support required.

⬆️ 137 • 💬 123 • 2d ago • [Apideck](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

---

**[Why I may ‘hire’ AI instead of a graduate student](https://news.ycombinator.com/item?id=47396557)**

⬆️ 109 • 💬 109 • 2d ago • [science.org](https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student)

---

**[Toward automated verification of unreviewed AI-generated code](https://news.ycombinator.com/item?id=47397367)**

Constraints that could make unreviewed AI-generated code trustworthy.

⬆️ 91 • 💬 84 • 2d ago • [peterlavigne.com](https://peterlavigne.com/writing/verifying-ai-generated-code)

---

---

## YouTube Videos: "ai"

**[This New AI Just Made OpenClaw Fully Autonomous (Way More Powerful)](https://www.youtube.com/watch?v=GGK-HMYMBBI)**

A new way to run OpenClaw just dropped, turning it into something that feels much closer to a real autonomous system. Instead of ...

📺 AI Revolution

👁️ 6K • 👍 323 • 💬 30 • ⏱️ 8:59 • 4h ago

---

**[Elon Musk Notices Something About the AI Revolution No One Noticed](https://www.youtube.com/watch?v=C5-gWTWPh44)**

Dave Rubin of "The Rubin Report" shares a DM clip of Elon Musk explaining to Peter H. Diamandis how AI and robots will likely ...

📺 The Rubin Report

👁️ 200K • 👍 6K • 💬 2K • ⏱️ 6:24 • 1d ago

---

**[Meta in crisis: Zuckerberg considers mass layoffs as AI model delayed again | Natasha Bernal](https://www.youtube.com/watch?v=82lO9OYM01M)**

If they don't come up with something that does impress, there is definitely going to be a problem there.” Tech journalist Natasha ...

📺 The Tech Report

👁️ 23K • 👍 726 • 💬 292 • ⏱️ 26:23 • 8h ago

---

**[AI expert designs cancer vaccine for his dog using ChatGPT](https://www.youtube.com/watch?v=USEhHrY5ZEU)**

A tech entrepreneur in Australia, Paul Conyngham, said he used artificial intelligence to design a cancer vaccine for his dog Rosie ...

📺 CBS News

👁️ 842 • 👍 29 • 💬 7 • ⏱️ 4:50 • 4h ago

---

**[NEW Manus AI Computer is INSANE! ( FREE!)](https://www.youtube.com/watch?v=-RA1U9dzEB8)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 2K • 👍 66 • 💬 9 • ⏱️ 8:07 • 6h ago

---

**[Why AI Researchers Are Quitting and Panicking on the Way Out](https://www.youtube.com/watch?v=rtT87iAm_SM)**

Top AI researchers are walking away from some of the most powerful tech companies on Earth, and their reasons are raising ...

📺 The Infographics Show

👁️ 475K • 👍 12K • 💬 2K • ⏱️ 14:48 • 2d ago

---

**[Google’s New AI Just Broke Math… (Invented Its Own Algorithms)](https://www.youtube.com/watch?v=W31ro8YT7jc)**

Google DeepMind's AlphaEvolve just broke long-standing mathematical records by evolving algorithms that improved several ...

📺 AI Revolution

👁️ 48K • 👍 1K • 💬 79 • ⏱️ 10:41 • 2d ago

---

**[AI Agents Running Wall Street — The Game Has Changed](https://www.youtube.com/watch?v=ASR25tYXB5s)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *AI ...

📺 Julia McCoy

👁️ 8K • 👍 477 • 💬 25 • ⏱️ 6:55 • 11h ago

---

**[Sam Altman Just Declared the Death of Transformers (ChatGPT Getting Replaced)](https://www.youtube.com/watch?v=XeTuLyOBY_0)**

Sam Altman just said the architecture behind ChatGPT and most modern AI may soon be replaced. Apple introduced LiTo, a ...

📺 AI Revolution

👁️ 90K • 👍 2K • 💬 262 • ⏱️ 11:10 • 1d ago

---

**[Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers! (2029 PREDICTION)](https://www.youtube.com/watch?v=fpETS6q1Hww)**

What is financial freedom? The Business Strategist Daniel Priestley on why AI makes lifestyle businesses easy. Daniel Priestley is ...

📺 The Diary Of A CEO

👁️ 1.1M • 👍 24K • 💬 4K • ⏱️ 2:02:37 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 111,716 • ❤️ 577 • 8d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 78,794 • ❤️ 888 • 11d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 7,003 • ❤️ 631 • 7d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 8,716 • ❤️ 306 • 5d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 36,759 • ❤️ 254 • 4d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 254,662 • ❤️ 544 • 15d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 1,872 • ❤️ 226 • 1d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,271,977 • ❤️ 917 • 17d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 644,452 • ❤️ 672 • 3d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 2,743,984 • ❤️ 1,354 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 97 • 💬 4 • ⭐ 1,806 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 16 • 💬 0 • ⭐ 35,637 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[AI Can Learn Scientific Taste](https://huggingface.co/papers/2603.14473)**

*Jingqi Tong, Mingzhe Li, Hangcheng Li et al. (23 authors)*

🏢 OpenMOSS

Great scientists have strong judgement and foresight, closely tied to what we call scientific taste. Here, we use the term to refer to the capacity to judge and propose research ideas with high potential impact. However, most relative research focuses on improving an AI scientist's executive capability, while enhancing an AI's scientific taste remains underexplored. In this work, we propose Reinforcement Learning from Community Feedback (RLCF), a training paradigm that uses large-scale community signals as supervision, and formulate scientific taste learning as a preference modeling and alignment problem. For preference modeling, we train Scientific Judge on 700K field- and time-matched pairs of high- vs. low-citation papers to judge ideas. For preference alignment, using Scientific Judge as a reward model, we train a policy model, Scientific Thinker, to propose research ideas with high potential impact. Experiments show Scientific Judge outperforms SOTA LLMs (e.g., GPT-5.2, Gemini 3 Pro) and generalizes to future-year test, unseen fields, and peer-review preference. Furthermore, Scientific Thinker proposes research ideas with higher potential impact than baselines. Our findings show that AI can learn scientific taste, marking a key step toward reaching human-level AI scientists.

▲ 242 • 💬 8 • ⭐ 264 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.14473) • [💻 code](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste) • [🔗 project](https://tongjingqi.github.io/AI-Can-Learn-Scientific-Taste/)

---

**[Grounding World Simulation Models in a Real-World Metropolis](https://huggingface.co/papers/2603.15583)**

*Junyoung Seo, Hyunwook Choi, Minkyung Kwon et al. (13 authors)*

🏢 NAVER AI Lab

What if a world simulation model could render not an imagined environment but a city that actually exists? Prior generative world models synthesize visually plausible yet artificial environments by imagining all content. We present Seoul World Model (SWM), a city-scale world model grounded in the real city of Seoul. SWM anchors autoregressive video generation through retrieval-augmented conditioning on nearby street-view images. However, this design introduces several challenges, including temporal misalignment between retrieved references and the dynamic target scene, limited trajectory diversity and data sparsity from vehicle-mounted captures at sparse intervals. We address these challenges through cross-temporal pairing, a large-scale synthetic dataset enabling diverse camera trajectories, and a view interpolation pipeline that synthesizes coherent training videos from sparse street-view images. We further introduce a Virtual Lookahead Sink to stabilize long-horizon generation by continuously re-grounding each chunk to a retrieved image at a future location. We evaluate SWM against recent video world models across three cities: Seoul, Busan, and Ann Arbor. SWM outperforms existing methods in generating spatially faithful, temporally consistent, long-horizon videos grounded in actual urban environments over trajectories reaching hundreds of meters, while supporting diverse camera movements and text-prompted scenario variations.

▲ 121 • 💬 4 • ⭐ 317 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15583) • [💻 code](https://github.com/naver-ai/seoul-world-model) • [🔗 project](https://seoul-world-model.github.io/)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 34 • 💬 2 • ⭐ 28,161 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 128 • 💬 6 • ⭐ 3,515 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 12 • 💬 5 • ⭐ 959 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,901 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data](https://huggingface.co/papers/2603.15594)**

*Yuwen Du, Rui Ye, Shuo Tang et al. (7 authors)*

🏢 OpenSeeker

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet the development of high-performance search agents remains dominated by industrial giants due to a lack of transparent, high-quality training data. This persistent data scarcity has fundamentally hindered the progress of the broader research community in developing and innovating within this domain. To bridge this gap, we introduce OpenSeeker, the first fully open-source search agent (i.e., model and data) that achieves frontier-level performance through two core technical innovations: (1) Fact-grounded scalable controllable QA synthesis, which reverse-engineers the web graph via topological expansion and entity obfuscation to generate complex, multi-hop reasoning tasks with controllable coverage and complexity. (2) Denoised trajectory synthesis, which employs a retrospective summarization mechanism to denoise the trajectory, therefore promoting the teacher LLMs to generate high-quality actions. Experimental results demonstrate that OpenSeeker, trained (a single training run) on only 11.7k synthesized samples, achieves state-of-the-art performance across multiple benchmarks including BrowseComp, BrowseComp-ZH, xbench-DeepSearch, and WideSearch. Notably, trained with simple SFT, OpenSeeker significantly outperforms the second-best fully open-source agent DeepDive (e.g., 29.5% v.s. 15.3% on BrowseComp), and even surpasses industrial competitors such as Tongyi DeepResearch (trained via extensive continual pre-training, SFT, and RL) on BrowseComp-ZH (48.4% v.s. 46.7%). We fully open-source the complete training dataset and the model weights to democratize frontier search agent research and foster a more transparent, collaborative ecosystem.

▲ 135 • 💬 6 • ⭐ 147 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15594) • [💻 code](https://github.com/rui-ye/OpenSeeker)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 50,295 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 42.2k • 🔱 5.9k • 2d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.5k • 🔱 1.0k • 5h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.6k • 🔱 1.6k • 10h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 11.1k • 🔱 1.0k • 1d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.9k • 🔱 717 • 1d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 8.6k • 🔱 416 • 12h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 4.1k • 🔱 342 • 1d ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

Open-source database of 700+ cybersecurity skills for AI agents and security practitioners

`Python` `agent-skills` `ai-agents` `blue-team` `claude` `claude-code`

⭐ 3.4k • 🔱 331 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.0k • 🔱 194 • 4d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.9k • 🔱 95 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
