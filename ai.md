---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-01T11:38:28.923402+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 01, 2026 at 11:38 UTC  
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

**[I have created a Chrome extension that fact checks YouTube videos as you watch](https://www.reddit.com/r/artificial/comments/1uk7t49/i_have_created_a_chrome_extension_that_fact/)**

Hi, I have been working on this for many months now and I'd really be happy for people to try it out. It is a Chrome extension called "PopUpFactCheck". It is an AI powered video fact checker. With it, you fact check any YouTube video that has captions. And you can use it, for free! You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. It's free, and you don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFact Check - Chrome Web Store PopUpFactCheck - Homepage

10h ago

---

**[Are Redditors influencing AI the most?](https://www.reddit.com/r/artificial/comments/1ujuckz/are_redditors_influencing_ai_the_most/)**

18h ago

---

**[Prompt injection broke every agent system I built so I designed a gateway that separates instructions from data](https://www.reddit.com/r/artificial/comments/1ukgppw/prompt_injection_broke_every_agent_system_i_built/)**

While building agent-based systems with LLM tool use, I kept running into the same failure mode: External content (webpages, files, API responses) would eventually influence agent behavior in unintended ways. Prompt injection isn’t just a “filtering problem” it’s an architectural one. So I built Sentinel Gateway, a middleware layer that sits between agents and tools and enforces a strict separation: Instruction channel (trusted, signed, runtime-issued only) Data channel (untrusted, never executable) Any action an agent takes must be backed by a signed, scoped runtime token, which means: external content cannot escalate into instructions tool calls cannot be influenced by injected payloads agent actions are constrained to explicit permissions It’s designed around the idea that: What it currently supports FastAPI-based agent gateway Streamlit UI for inspection and control Claude sessions + external agent integration Runtime-signed tool execution tokens Audit logging of all agent actions Scheduled tasks + memory tiers Local (SQLite) or Postgres deployment

2h ago

---

**[Why do we trust AI answers simply because they sound confident?](https://www.reddit.com/r/artificial/comments/1ukicm7/why_do_we_trust_ai_answers_simply_because_they/)**

Over the last few months, I've been thinking about one question: Why do we trust AI answers simply because they sound confident? In many domains, that confidence is harmless. But in finance, a single incorrect number can influence lending decisions, covenant monitoring, portfolio reviews, or risk assessments. The problem isn't that AI makes mistakes. Humans do too. The problem is that today's AI systems rarely show why a financial claim should be trusted. That realization led me to start building AutoFlow. We're not building another chatbot or AI wrapper. We're building a Credit Evidence Engine that verifies eligible financial claims against source evidence, calculation rules, and document consistency. Our first prototype is intentionally narrow. It focuses on credit packages, borrower financial statements, covenant calculations, and exception detection. If two documents report different EBITDA values, the system shouldn't silently choose one. It should expose the contradiction. If a leverage ratio is calculated, it should be traceable back to the covenant definition and supporting evidence. I'm sharing this journey in public because I believe trust is earned through transparent decisions, honest limitations, and continuous learning—not confident marketing. I'm still in the prototype stage, and I expect many assumptions to be challenged. That's exactly why I'm building in public. Question for other founders: When you're building trust before you have customers or production case studies, what has mattered most in your experience—clear scope, technical proof, transparent progress, or something else? I'd genuinely like to learn from your experience.

42m ago

---

**[When does using AI stop being collaboration and start being outsourcing your thinking?](https://www.reddit.com/r/artificial/comments/1ukdp8x/when_does_using_ai_stop_being_collaboration_and/)**

I've been thinking a lot lately about how I personally use AI tools in creative and professional work, and I'm genuinely curious where others draw the line. There's a real difference between using AI to brainstorm, get unstuck, or pressuretest ideas versus just outsourcing the thinking entirely. But in practice that line gets blurry fast. You start by asking for a rough outline, then you're editing its draft, then you're mostly just accepting suggestions, and somewhere in there you've lost the thread of your own voice. What I find interesting is that the most satisfying results I've had come when I treat the AI like a sparring partner rather than a ghostwriter. Push back on it, argue with it, use its output as a foil. That seems to produce something that still feels like mine. But I also wonder if that's just me rationalizing a comfort zone. Maybe the resistance to full AI collaboration is just ego, or maybe it's something worth protecting. For people who use AI regularly in creative or knowledge work, how do you think about this? Do you have explicit rules for yourself, or does it just depend on the task? Has your approach shifted over time as the models have gotten better? Curious whether others feel like the better the AI gets, the harder this question becomes.

5h ago

---

**[Netflix uses AI to recreate Gene Wilder's voice for new Willy Wonka competition show](https://www.reddit.com/r/artificial/comments/1ukfejv/netflix_uses_ai_to_recreate_gene_wilders_voice/)**

His wife has given her full support towards the series

🔗 [Reality Shrine](https://thetab.com/realityshrine/2026/07/01/netflix-has-used-ai-to-recreate-gene-wilders-voice-for-new-willy-wonka-show-and-its-cursed/) • 3h ago

---

**[Agentic AI for people that don’t need agentic AI?](https://www.reddit.com/r/artificial/comments/1uk7ffb/agentic_ai_for_people_that_dont_need_agentic_ai/)**

I work in the highly regulated finance industry in a non-engineering role. As a result, I don’t really have the ability to try building agents for work, but I want to build out my toolkit/personal knowledge in regards to AI. What are some feasible quality of life/personal agent building exercises that I could explore?

10h ago

---

**[which of this month's ai releases changed your actual workflow, not just your feed](https://www.reddit.com/r/artificial/comments/1ukecei/which_of_this_months_ai_releases_changed_your/)**

feels like every week this month theres a new model or a new robot demo and the feed just resets. sonnet 5, geminis video editing thing, the ubtech robots, whatever fable ends up being once its back. curious which of these actually changed something in your day to day versus which ones you watched a demo of once and moved on from.

4h ago

---

**[Anthropic Teams Up With Amazon, Microsoft, and Google on AI Jailbreak Framework](https://www.reddit.com/r/artificial/comments/1uki43w/anthropic_teams_up_with_amazon_microsoft_and/)**

Anthropic restored Claude Fable 5 after US export restrictions lifted & unveiled a new AI jailbreak framework with Amazon, Microsoft & Google.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/anthropic-ai-jailbreak-framework-fable-5/) • 55m ago

---

**[What is Google ai on about](https://www.reddit.com/r/artificial/comments/1uk6brc/what_is_google_ai_on_about/)**

They really like everything I do I do it for you

11h ago

---

---

## Google News: "ai"

**[Employers who laid off workers citing AI are already starting to regret it](https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html)**

Companies are realizing artificial intelligence can't do everything after all, prompting them to rehire employees to grow their businesses

CNBC • 7h ago

---

**[Connect Education To Jobs And Create An AI Workforce Transition Plan](https://www.forbes.com/sites/paulocarvao/2026/07/01/connect-education-to-jobs-and-create-an-ai-workforce-transition-system/)**

An AI workforce transition needs more than retraining. P-TECH shows how education, employers and credentials can connect workers to jobs reshaped by AI.

Forbes • 8m ago

---

**[Opinion | Why A.I. Won’t Steal All Our Jobs](https://www.nytimes.com/2026/06/30/opinion/ai-agents-steal-jobs-employment.html)**

The New York Times • 1d ago

---

**[US removes curbs on Anthropic's latest Fable and Mythos AI models](https://www.reuters.com/business/us-lift-export-controls-anthropics-fable-ai-model-tuesday-source-says-2026-06-30/)**

Reuters • 12h ago

---

**[Fable and Mythos: Anthropic says US lifts export ban on its advanced AI tools](https://www.bbc.com/news/articles/cdr42623e1do)**

Fable and Mythos were abruptly suspended in June over concerns that they could be used by hackers.

BBC • 7h ago

---

**[US ends ban on exports of Anthropic’s advanced AI](https://www.yahoo.com/news/politics/articles/us-ends-ban-exports-anthropic-110207094.html)**

The White House blocked foreign nationals from using the models last month, prompting Anthropic to suspend access to the two models altogether.

Yahoo • 36m ago

---

**[Cathie Wood Argues AI Cannot Replace Bitcoin As 'Insurance Policy' Protecting Wealth, Says 'Less Stable' Countries Will 'Light Another Fire' Under BTC](https://finance.yahoo.com/markets/crypto/articles/cathie-wood-argues-ai-cannot-094614293.html)**

Renowned investor Cathie Wood positioned Bitcoin as a “wealth insurance policy” on Saturday that AI-driven growth investments cannot provide. Wood Says AI Investments Can’t Compete With Bitcoin On This Front In an X post, Wood argued that capital outflows from...

Yahoo Finance • 1h ago

---

**[Jim Cramer says the AI trade has shifted — and these stocks are leading now](https://www.cnbc.com/2026/06/30/jim-cramer-ai-trade-shifted-stocks-leading-now.html)**

CNBC's Jim Cramer said Wall Street is rewarding the companies supplying the artificial intelligence boom rather than the technology giants funding it.

CNBC • 13h ago

---

**[Michael Burry says he's shorting Caterpillar for the first time after it nearly doubled in the AI-driven rally of 2026](https://www.cnbc.com/2026/06/30/burry-shorts-caterpillar-after-it-nearly-doubled-in-ai-rally-of-2026.html)**

"Caterpillar jumped out at me," Burry said. "I have never shorted Caterpillar. It has always done great for me on the long side in the past."

CNBC • 14h ago

---

**[Wall Street’s AI Race Is Fueling New Fears of Crowded Trading](https://www.bloomberg.com/news/articles/2026-07-01/wall-street-s-ai-race-is-fueling-new-fears-of-crowded-trading)**

Bloomberg.com • 1h ago

---

---

## HackerNews: "ai"

**[Professor denounces mass AI fraud on an exam at Brown](https://news.ycombinator.com/item?id=48708991)**

The renowned economist Roberto Serrano has ‘overwhelming evidence’ that his students cheated. He thinks the time has come for an in-depth debate so the technology does not signal the end of higher education

⬆️ 547 • 💬 719 • 2d ago • [EL PAÍS English](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html)

---

**[Librepods: AirPods liberated](https://news.ycombinator.com/item?id=48710232)**

AirPods liberated from Apple's ecosystem. Contribute to librepods-org/librepods development by creating an account on GitHub.

⬆️ 496 • 💬 181 • 2d ago • [GitHub](https://github.com/librepods-org/librepods)

---

**[Tidal AI Policy](https://news.ycombinator.com/item?id=48718840)**

⬆️ 307 • 💬 343 • 1d ago • [tidal.com](https://tidal.com/ai-policy)

---

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 232 • 💬 146 • 3h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Working With AI: A concrete example](https://news.ycombinator.com/item?id=48720064)**

In this essay, Carson Gross walks through a concrete bug fix in hyperscript to show where AI helped, where it fell short, and why keeping a knowledgeable human in the loop is what kept complexity in check.

⬆️ 190 • 💬 67 • 1d ago • [htmx.org](https://htmx.org/essays/working-with-ai/)

---

**[Google limits Meta's use of its Gemini AI models](https://news.ycombinator.com/item?id=48707103)**

Meta had sought more computing capacity than Google could provide, the Financial Times reports.

⬆️ 161 • 💬 72 • 2d ago • [CNBC](https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html)

---

**[AI boom risks global financial crash, warn central bankers](https://news.ycombinator.com/item?id=48713697)**

Reversal of ‘excessive’ tech investments could have serious economic consequences, report finds

⬆️ 157 • 💬 214 • 2d ago • [The Telegraph](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/)

---

**[We need tech news sources which exclude AI](https://news.ycombinator.com/item?id=48713041)**

⬆️ 139 • 💬 80 • 2d ago

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 135 • 💬 138 • 19h ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[Ford rehires 'gray beard' engineers after AI falls short](https://news.ycombinator.com/item?id=48710749)**

"Mistakenly we thought that by just introducing artificial intelligence ... that would produce a high-quality product.”

⬆️ 135 • 💬 3 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/)

---

---

## YouTube Videos: "ai"

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 83K • 👍 5K • 💬 472 • ⏱️ 9:43 • 18h ago

---

**[Congress Got a Private Look at AI. The Reaction Was Chilling.](https://www.youtube.com/watch?v=z9zqqsS7848)**

AI #Congress #OpenAI They saw the demo behind closed doors. They walked out shaken. Nobody will tell you what was in that ...

📺 Rod Miller

👁️ 8K • 👍 903 • 💬 216 • ⏱️ 28:59 • 1d ago

---

**[Anthropic Just Confirmed It: The 2028 AI Warning Is Real](https://www.youtube.com/watch?v=j1xcsDxSb_Y)**

Self-improving AI is starting to look real. Anthropic's Jack Clark put a 2028 timeline on recursive self-improvement, Google ...

📺 AI Revolution

👁️ 51K • 👍 1K • 💬 152 • ⏱️ 13:32 • 2d ago

---

**[The AI Bubble Has F*cked Us (Even If It NEVER Pops)](https://www.youtube.com/watch?v=dPVEha6oqfw)**

The AI Bubble Will Is MUCH Worse Than We Thought. Contact your representative to ENSURE AI is aligned with humanity: ...

📺 Damon Cassidy

👁️ 33K • 👍 2K • 💬 408 • ⏱️ 22:06 • 11h ago

---

**[3 REAL Ways To Make Money With Claude AI in 2026](https://www.youtube.com/watch?v=Zvnt4S3aFJk)**

Get started with FreshBooks free 30-day trial: https://partner.freshbooks.com/KimberlyMitchell The job market is rough right now ...

📺 Kimberly Mitchell

👁️ 5K • 👍 224 • 💬 17 • ⏱️ 16:21 • 21h ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 59K • 👍 3K • 💬 615 • ⏱️ 13:10 • 1d ago

---

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 81K • 👍 4K • 💬 407 • ⏱️ 46:52 • 20h ago

---

**[This New AI Model Changes Everything](https://www.youtube.com/watch?v=qks6dGQFd_c)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers GLM 5.2: https://z.ai/blog/glm-5.2 We would ...

📺 Two Minute Papers

👁️ 22K • 👍 1K • 💬 160 • ⏱️ 7:27 • 6h ago

---

**[Limiting access to top AI models in the U.S. could hand China an opening as capability gap narrows](https://www.youtube.com/watch?v=Jgmiy1tUjxI)**

CNBC's Deirdre Bosa reports on China's AI availability.

📺 CNBC Television

👁️ 24K • 👍 307 • 💬 280 • ⏱️ 3:30 • 1d ago

---

**[WTH? Trump Sends Cryptic Message! Now AI Says Trump Is DEAD!](https://www.youtube.com/watch?v=nWI15TNhKnU)**

President Trump is once again sparking a massive online reaction after posting a strange AI-style patriotic painting on Truth Social ...

📺 Lisa Haven

👁️ 8K • 👍 716 • 💬 87 • ⏱️ 8:27 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 630,246 • ❤️ 1,534 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,113,871 • ❤️ 1,102 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 159,967 • ❤️ 3,108 • 8d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 233,701 • ❤️ 576 • 5d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 34,371 • ❤️ 482 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 288,741 • ❤️ 902 • 12d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 191,409 • ❤️ 356 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 114,499 • ❤️ 603 • 2d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 46,677 • ❤️ 318 • 5d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 56,953 • ❤️ 431 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 44 • 💬 5 • ⭐ 12,690 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 72,669 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 8,993 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 90,031 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,209 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 9,890 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,296 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,026 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 84,946 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,888 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 69.9k • 🔱 3.6k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.2k • 🔱 1.1k • 1m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.9k • 🔱 742 • 29m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.6k • 🔱 584 • 39m ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.2k • 🔱 198 • 3d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 172 • 3d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 155 • 4d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.7k • 🔱 82 • 1h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 18d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.4k • 🔱 60 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
