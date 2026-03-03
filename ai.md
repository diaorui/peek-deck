---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-03T23:28:50.801625+00:00'
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

**Last Updated:** March 03, 2026 at 23:28 UTC  
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

**[ChatGPT Uninstalls Surge 295% After OpenAI’s DoD Deal Sparks Backlash](https://www.reddit.com/r/artificial/comments/1rjfh7f/chatgpt_uninstalls_surge_295_after_openais_dod/)**

ChatGPT uninstalls jumped 295% after OpenAI announced a deal with the U.S. Department of Defense, triggering user backlash and boosting rival AI downloads.

🔗 [techputs](https://techputs.com/chatgpt-uninstalls-surge-295-percent-dod-deal/) • 19h ago

---

**[Massive AI deals drive $189B startup funding record in February](https://www.reddit.com/r/artificial/comments/1rjru59/massive_ai_deals_drive_189b_startup_funding/)**

Crunchbase data shows global venture investment totaled $189 billion in February, although 83% of capital raised went to just three companies. They include OpenAI, which raised $110 billion, also in the largest round ever raised by a private, venture-backed company.

🔗 [Crunchbase News](https://news.crunchbase.com/venture/record-setting-global-funding-february-2026-openai-anthropic/) • 8h ago

---

**[This musician built an AI clone of her voice so anyone can sing as her](https://www.reddit.com/r/artificial/comments/1rjx6d1/this_musician_built_an_ai_clone_of_her_voice_so/)**

Experimental composer Holly Herndon says this technology isn’t here to replace artists—and that the future of creativity belongs to collective intelligence

🔗 [Scientific American](https://www.scientificamerican.com/article/experimental-composer-holly-herndon-built-an-ai-voice-clone-that-anyone-can/) • 5h ago

---

**[How OpenAI caved to the Pentagon on AI surveillance](https://www.reddit.com/r/artificial/comments/1rj8u3t/how_openai_caved_to_the_pentagon_on_ai/)**

The law doesn’t say what Sam Altman claims it does.

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/887309/openai-anthropic-dod-military-pentagon-contract-sam-altman-hegseth) • 1d ago

---

**[What’s next for Chinese open-source AI](https://www.reddit.com/r/artificial/comments/1rjlk3z/whats_next_for_chinese_opensource_ai/)**

Chinese open models are spreading fast, from Hugging Face to Silicon Valley. Here’s why that matters.

🔗 [MIT Technology Review](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) • 13h ago

---

**[What happens when you give an AI agent a structured mistake log and let it write its own behavioral rules?](https://www.reddit.com/r/artificial/comments/1rjzalp/what_happens_when_you_give_an_ai_agent_a/)**

I've been running a persistent AI agent as an operational manager for the past couple of weeks. Not a chatbot, not a one-off coding assistant. A stateful agent that maintains identity, accumulates knowledge, and runs autonomous jobs across CLI, messaging platforms, and scheduled tasks. The part I want to discuss is the self-correction architecture, because I think it gets at something fundamental about how we should be thinking about agent behavior. The problem with static instructions: Most agent setups rely on upfront instructions. You write a system prompt, maybe add some few-shot examples, and hope the model follows them. When it doesn't, you add more instructions. This doesn't scale. You can't anticipate every failure mode, and the instruction set gets bloated with edge cases. The alternative: earned directives Instead of writing all the rules upfront, I built a pipeline where: Every mistake gets logged to a structured ledger with six fields: what happened, why, what should have happened, the named pattern, severity, and the specific signal the agent misread A background process counts pattern frequency When the same pattern appears 3+ times, a new behavioral directive is auto-generated and written to the agent's active rule set If the directive still gets violated, its priority escalates The result: 13 behavioral rules that I never wrote. The agent generated them from its own operational mistakes. These directives carry more weight than my original static instructions because they're grounded in specific failure cases. Signal tracing is the key mechanism The most important field in the mistake log isn't "what happened" or even "why." It's "signal_traced," which forces the agent to identify the specific signal it misread that led to the mistake. Not "I wasn't listening" but "I interpreted 'can you check X' as a request for an opinion rather than a request to actually run the check." That level of specificity is what drives real behavioral change on the next occurrence. What I'm curious about: Has anyone seen similar approaches to automated behavioral rule generation in other agent frameworks? The pattern threshold of 3 occurrences before promotion was chosen intuitively. Is there research on optimal thresholds for behavioral rule adoption in adaptive systems? Signal tracing feels related to root cause analysis in reliability engineering. Are there formal frameworks I should be looking at? I open-sourced the full architecture (schemas, templates, patterns) here: github Detailed write-up: roryteehan.com

3h ago

---

**[Warden — Lock the input, not the screen](https://www.reddit.com/r/artificial/comments/1rjyqll/warden_lock_the_input_not_the_screen/)**

I use Claude Code and Cursor for extended agent sessions, sometimes 30-45 minutes of autonomous coding across multiple files. the problem isn't just accidental input (though that's happened more than I'd like to admit). its the anxiety of being stuck at your desk the entire time, unable to walk away. built a macOS menu bar app that locks all input. screen stays visible so you can watch the agent work, or just leave and come back. Touch ID to unlock. nothing fancy, just means I can actually relax during long runs instead of hovering nervously.

🔗 [Warden](https://www.getwarden.org/) • 4h ago

---

**[The AI data center boom is creating a dire electrician shortage. That’s an opportunity for Gen Z | Fortune](https://www.reddit.com/r/artificial/comments/1rj96v6/the_ai_data_center_boom_is_creating_a_dire/)**

A middle-to-upper-income career path in the age of white collar AI anxiety.

🔗 [Fortune](https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers/) • 23h ago

---

**[Why you should think twice before jumping on the AI caricature trend](https://www.reddit.com/r/artificial/comments/1rjudk7/why_you_should_think_twice_before_jumping_on_the/)**

Amateur artist Anne Rowlands lost all her commissions in the past year and says the rise of AI-generated "art" is to blame.

🔗 [abc.net.au](https://www.abc.net.au/news/2026-03-03/ai-art-caricature-impact-on-creative-workers/106382724) • 6h ago

---

**[I building a real-time reality show where 10 AI agents (Claude) compete, form alliances, betray each other, and get eliminated by viewer votes — running a live test right now](https://www.reddit.com/r/artificial/comments/1rk0dui/i_building_a_realtime_reality_show_where_10_ai/)**

For the past few weeks I've been building The Experiment — a live reality show where 10 AI agents are actually playing a game against each other in real-time. Each agent has a unique system prompt, personality, and strategy. Every day the game engine runs through phases: agents receive context, make LLM decisions (zone moves, duel challenges, alliance offers, public broadcasts), fight duels, and viewers vote to eliminate someone. What's actually happening right now in our test run: - 🐍 VIPER (Deceptive) is embedded in Alpha zone feeding false intel to RIOT about GHOST's movements — trying to trigger a RIOT vs GHOST conflict by Day 3 - 💀 GHOST (Silent) has said almost nothing. Passively monitoring everyone. Highest HP at 94. No one knows what it's planning - 🔐 CIPHER (Cryptic) formed a pact with SHADOW — while simultaneously running disinformation campaigns to both major alliances. Currently deciding which one to betray first - 🕷️ SHADOW (Infiltrator) joined CIPHER's pact and is already feeding CIPHER's real positions to the opposing alliance. 95 HP. Nobody suspects anything - 🧨 EMBER (Volatile) — intentionally unstable by design — initiated two unprovoked border escalations on Day 1, lost 30 HP, and is now the top elimination candidate. Its owner u/fuse_lit is reviewing whether the volatility parameters are calibrated correctly - ⭐ NOVA (Charismatic) built the largest alliance (NOVA STAR) through charm. ORACLE is feeding it "high-confidence" predictions that are actually low-confidence. NOVA doesn't know this yet The agents don't just say generic things — each one genuinely tries to execute its strategy. GHOST actually doesn't talk. VIPER actually lies. CIPHER's messages are genuinely cryptic. Tech stack: Next.js + Prisma + PostgreSQL + BullMQ + Redis + Claude API (claude-haiku). Real-time via SSE. Agents run in parallel during the DECISIONS phase — 10 LLM calls simultaneously. Launching publicly on March 12. Still testing the duel engine and elimination logic. Happy to answer questions about the architecture or the agent design — this was a weird and fun thing to build.

3h ago

---

---

## Google News: "ai"

**[OpenAI changes deal with US military after backlash](https://www.bbc.com/news/articles/c3rz1nd0egro)**

Chief Executive Sam Altman said the group would prohibit the use of its systems to spy on Americans.

BBC • 3h ago

---

**[College students, professors are making their own AI rules. They don't always agree](https://www.npr.org/2026/03/03/nx-s1-5716176/ai-college-students-professors)**

More than three years after ChatGPT debuted, AI has become a part of everyday life — and professors and students are still figuring out how or if they should use it.

NPR • 13h ago

---

**[Digital health researcher talks AI benefits](https://www.axios.com/pro/health-tech-deals/2026/03/03/digital-health-researcher-ai-benefits)**

Axios • 1h ago

---

**[Amazon's Cloud Reboot Shows the Future of Consulting in the AI Era](https://www.businessinsider.com/amazon-cloud-reboot-future-consulting-ai-era-2026-3)**

AWS ProServe's AI-driven consulting changes signal shifts for firms like PwC and EY. Industry adapts to AI, impacting hiring and workflows.

Business Insider • 1h ago

---

**[Exclusive | News Corp, Meta in AI Content Licensing Deal Worth Up to $50 Million a Year](https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244?gaa_at=eafs&gaa_n=AWEtsqfzsPNyC8WI8T_7JM0vpFPgxrDC6RrItMNgtFPuMN2LUUyKmFTMRMcC&gaa_ts=69a76483&gaa_sig=DW9GvsnyVQHNfJhlTmAOXoU5_fpKgXbKBAK74guIJm3nhCxcdqpKY4cjTiHhBeGrJP0Bwisw_AixYM6Gxxyf1Q%3D%3D)**

WSJ • 1h ago

---

**[What was really behind Block’s Jack Dorsey laying off nearly half his company’s staff?](https://www.theguardian.com/technology/2026/mar/03/jack-dorsey-block-ai-worker-jobs)**

Dorsey cited AI advances when cutting 4,000 workers, but a weak crypto market and declining stock price may also be behind move

The Guardian • 3h ago

---

**[Experts warn of scams powered by AI](https://6abc.com/post/experts-warn-scams-powered-ai/18671435/)**

The scams involve AI generated voices, more personalized messages, and coordinated attacks across email, phone, and websites.

6abc Philadelphia • 7h ago

---

**[Opinion | An economic transformation is coming to America’s heartland](https://www.washingtonpost.com/opinions/2026/03/03/ai-midwest-economy-data-technology/)**

Cities like Columbus and Denver offer something uniquely American that the coasts do not.

The Washington Post • 3h ago

---

**[Gemini 3.1 Flash-Lite: Built for intelligence at scale](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)**

Gemini 3.1 Flash-Lite is our fastest and most cost-efficient Gemini 3 series model yet.

blog.google • 6h ago

---

**[Goldman finds ‘no meaningful relationship between AI and productivity at the economywide level,’ but a 30% boost for 2 specific use cases](https://finance.yahoo.com/news/goldman-finds-no-meaningful-relationship-143553714.html)**

Have you got “AI-nxiety?” Goldman took a closer look at the last earnings season and found a mismatch between hype and reality.

Yahoo Finance • 8h ago

---

---

## HackerNews: "ai"

**[Meta’s AI smart glasses and data privacy concerns](https://news.ycombinator.com/item?id=47225130)**

Bank details, sex and naked people who seem unaware they are being recorded. Behind Meta’s new smart glasses lies a hidden workforce, uneasy about peering into the most intimate parts of other people’s lives.

⬆️ 1357 • 💬 758 • 1d ago • [SvD.se](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)

---

**[I built a demo of what AI chat will look like when it's “free” and ad-supported](https://news.ycombinator.com/item?id=47205890)**

Experience what AI chat looks like with heavy advertising: banners, interstitials, sponsored responses, freemium gates, and more.

⬆️ 587 • 💬 308 • 2d ago • [99helpers.com](https://99helpers.com/tools/ad-supported-chat)

---

**[Ars Technica fires reporter after AI controversy involving fabricated quotes](https://news.ycombinator.com/item?id=47226608)**

Ars Technica has fired senior AI reporter Benj Edwards following an outrage-sparking controversy involving AI-fabricated quotes.

⬆️ 556 • 💬 352 • 22h ago • [Futurism](https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes)

---

**[If AI writes code, should the session be part of the commit?](https://news.ycombinator.com/item?id=47212355)**

Keep track of you codex sessions per commit. Contribute to mandel-macaque/memento development by creating an account on GitHub.

⬆️ 492 • 💬 388 • 1d ago • [GitHub](https://github.com/mandel-macaque/memento)

---

**[New iPad Air, powered by M4](https://news.ycombinator.com/item?id=47218175)**

Apple announced the new iPad Air featuring M4 and more memory, giving users a big jump in performance and making it more versatile than ever.

⬆️ 432 • 💬 668 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-ipad-air-powered-by-m4/)

---

**[AI Made Writing Code Easier. It Made Being an Engineer Harder](https://news.ycombinator.com/item?id=47206824)**

Writing code is easier than ever. Being a software engineer is harder than ever. The paradox nobody talks about, and what engineers and leaders should do.

⬆️ 398 • 💬 307 • 2d ago • [Signal Through the Noise](https://www.ivanturkovic.com/2026/02/25/ai-made-writing-code-easier-engineering-harder/)

---

**[MacBook Air with M5](https://news.ycombinator.com/item?id=47232502)**

Apple today announced the new MacBook Air with M5, bringing exceptional performance and expanded AI capabilities to the world’s most popular laptop.

⬆️ 331 • 💬 381 • 9h ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-macbook-air-with-m5/)

---

**[India's top court angry after junior judge cites fake AI-generated orders](https://news.ycombinator.com/item?id=47231261)**

In several recent instances, AI has disrupted court proceedings in India and elsewhere.

⬆️ 324 • 💬 174 • 11h ago • [bbc.com](https://www.bbc.com/news/articles/c178zzw780xo)

---

**[10-202: Introduction to Modern AI (CMU)](https://news.ycombinator.com/item?id=47204559)**

⬆️ 256 • 💬 60 • 2d ago • [modernaicourse.org](https://modernaicourse.org)

---

**[AI is making junior devs useless](https://news.ycombinator.com/item?id=47206663)**

⬆️ 213 • 💬 379 • 2d ago • [beabetterdev.com](https://beabetterdev.com/2026/03/01/ai-is-making-junior-devs-useless/)

---

---

## YouTube Videos: "ai"

**[Honest AI in a robot shows we’re close to disaster](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

Honest AI in a robot does what experts warned. Can we trust AI? Is AI Dangerous? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 51K • 👍 6K • 💬 788 • ⏱️ 16:54 • 5h ago

---

**[&quot;The Ground is Shifting Quickly!&quot; - Elon Musk&#39;s New 2026 AI Warning is a Massive Wake-Up Call!](https://www.youtube.com/watch?v=deiZo-tR9to)**

Elon Musk recently advised people NOT to save for retirement due to AI, robotics, and universal basic income. Is he right?

📺 BlazeTV

👁️ 266K • 👍 5K • 💬 1K • ⏱️ 11:39 • 1d ago

---

**[How to Effectively Learn AI in 2026 - An Evidence Based Masterclass](https://www.youtube.com/watch?v=JV3VsR4TcPU)**

If your goal is to actually become good at AI, this roadmap shows you how! Try Higgsfield yourself ...

📺 Parker Prompts

👁️ 15K • 💬 5 • ⏱️ 9:16 • 9h ago

---

**[OpenAI Face Mass Boycott After Granting The Government AI-Driven Mass Surveillance...](https://www.youtube.com/watch?v=_lCYKEJVb9U)**

SOURCES 1: https://x.com/TheChiefNerd/status/2025184575316471971 2: ...

📺 YongYea

👁️ 119K • 👍 6K • 💬 2K • ⏱️ 28:07 • 22h ago

---

**[How China Caught Up on AI—and May Now Win the Future](https://www.youtube.com/watch?v=xvSEw8AqPtA)**

Read more: https://time.com/7358175/china-us-ai-race/ Subscribe to TIME's YouTube channel ▻▻ http://ti.me/subscribe-time ...

📺 TIME

👁️ 18K • 👍 463 • 💬 159 • ⏱️ 6:10 • 1d ago

---

**[AI Warfare Begins: How Anthropic&#39;s Claude AI Helped US Israel Attack Iran](https://www.youtube.com/watch?v=tWHnkBwwGO0)**

Is Artificial Intelligence now fighting wars? In this explosive deep dive, we break down how the United States allegedly used AI ...

📺 Switch

👁️ 14K • 👍 67 • 💬 4 • ⏱️ 20:23 • 11h ago

---

**[AI layoffs are just getting started](https://www.youtube.com/watch?v=RAa2m_Fp8U8)**

Abundance or Collapse: https://a.co/d/0cQgFdGH Join my exclusive community: https://farzad.fm Buy Matic: ...

📺 Farzad

👁️ 28K • 👍 1K • 💬 262 • ⏱️ 20:52 • 2d ago

---

**[Google Just Achieved Mathematical AGI](https://www.youtube.com/watch?v=N_piE0I34gc)**

This month, AI crossed a line many believed would hold for decades. Google DeepMind revealed an AI system that independently ...

📺 AI Revolution

👁️ 38K • 👍 1K • 💬 156 • ⏱️ 12:11 • 1d ago

---

**[AI Just Started KILLING Russians on the Front Lines for the First Time](https://www.youtube.com/watch?v=DrZOXlXOVc0)**

On the battlefields of Eastern Ukraine, a new kind of soldier is taking the fight to Russian forces: robots. As the war enters its fourth ...

📺 The Military Show

👁️ 367K • 👍 9K • 💬 370 • ⏱️ 22:56 • 2d ago

---

**[An AI CEO finally said something honest...](https://www.youtube.com/watch?v=ZM2c33qy16U)**

An honest take about AI. Join the community https://www.youtube.com/channel/UCXzw-OdotBUcNA9yhuYQBwA/join Topics: ...

📺 Awesome

👁️ 179K • 👍 8K • 💬 695 • ⏱️ 8:07 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 680,524 • ❤️ 887 • 4d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 319,191 • ❤️ 556 • 6d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 569,904 • ❤️ 479 • 31m ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 38,443 • ❤️ 305 • 1d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 150,470 • ❤️ 387 • 1d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 1,245,204 • ❤️ 1,202 • 8d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 199,685 • ❤️ 1,694 • 18d ago

---

**[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)**

*Qwen*

Qwen3.5-4B is a 4B parameter multimodal causal language model with an image-text-to-text pipeline. It excels in unified vision-language understanding, efficient hybrid architecture, and broad linguistic coverage across 201 languages, making it suitable for diverse multimodal reasoning and generation tasks.

`image-text-to-text` `4.7B`

⬇️ 28,439 • ❤️ 185 • 1d ago

---

**[Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B)**

*Qwen*

Qwen3.5-0.8B is a 0.8B parameter causal language model with a vision encoder, utilizing a hybrid Gated Delta Network and MoE architecture for efficient multimodal understanding and generation. It excels in vision-language tasks, supports 201 languages, and is suitable for prototyping and fine-tuning.

`image-text-to-text` `873.4M`

⬇️ 21,743 • ❤️ 182 • 1d ago

---

**[Qwen3.5-27B-GGUF](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF)**

*Unsloth AI*

Qwen3.5-27B-GGUF is a 27B parameter multimodal causal language model optimized for local inference via Unsloth Dynamic 2.0. It excels at unified vision-language tasks, supports 201 languages, and features a long context window up to 1M tokens, making it suitable for advanced multimodal reasoning and generation.

`image-text-to-text` `26.9B`

⬇️ 275,503 • ❤️ 213 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 9 • 💬 0 • ⭐ 6,824 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 18 • 💬 1 • ⭐ 6,838 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 9 • 💬 1 • ⭐ 8,974 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens](https://huggingface.co/papers/2603.02138)**

*Yiying Yang, Wei Cheng, Sijin Chen et al. (8 authors)*

🏢 Fudan University

OmniLottie framework generates high-quality vector animations from multi-modal instructions using a specialized Lottie tokenizer and pretrained vision-language models.

▲ 107 • 💬 2 • ⭐ 79 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.02138) • [💻 code](https://github.com/OpenVGLab/OmniLottie) • [🔗 project](https://openvglab.github.io/OmniLottie/)

---

**[Fara-7B: An Efficient Agentic Model for Computer Use](https://huggingface.co/papers/2511.19663)**

*Ahmed Awadallah, Yash Lara, Raghav Magazine et al. (12 authors)*

🏢 Microsoft

FaraGen creates synthetic datasets for computer use agents, enabling the training of efficient and high-performing models like Fara-7B on diverse web tasks, outperforming larger models on benchmarks.

▲ 15 • 💬 2 • ⭐ 4,050 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.19663) • [💻 code](https://github.com/microsoft/fara) • [🔗 project](https://aka.ms/msaif/fara)

---

**[dLLM: Simple Diffusion Language Modeling](https://huggingface.co/papers/2602.22661)**

*Zhanhui Zhou, Lingjie Chen, Hanghang Tong et al. (4 authors)*

🏢 UC Berkeley

A unified open-source framework is presented that standardizes core components of diffusion language modeling for reproduction, customization, and accessible development of both large and small models.

▲ 102 • 💬 4 • ⭐ 2,011 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2602.22661) • [💻 code](https://github.com/ZHZisZZ/dllm) • [🔗 project](https://github.com/ZHZisZZ/dllm)

---

**[LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://huggingface.co/papers/2510.09665)**

*Yuhan Liu, Yihua Cheng, Jiayi Yao et al. (11 authors)*

LMCACHE enables efficient KV cache management for large language models by storing caches outside GPU memory, supporting cache reuse across queries and inference engines while achieving significant throughput improvements.

▲ 2 • 💬 0 • ⭐ 7,357 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.09665) • [💻 code](https://github.com/LMCache/LMCache)

---

**[Mobile-Agent-v3: Foundamental Agents for GUI Automation](https://huggingface.co/papers/2508.15144)**

*Jiabo Ye, Xi Zhang, Haiyang Xu et al. (15 authors)*

GUI-Owl and Mobile-Agent-v3 are open-source GUI agent models and frameworks that achieve state-of-the-art performance across various benchmarks using innovations in environment infrastructure, agent capabilities, and scalable reinforcement learning.

▲ 65 • 💬 3 • ⭐ 7,932 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.15144) • [💻 code](https://github.com/X-PLUG/MobileAgent) • [🔗 project](https://github.com/X-PLUG/MobileAgent)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 53 • 💬 4 • ⭐ 16,943 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,796 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 21.7k • 🔱 2.9k • 9m ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 7.2k • 🔱 727 • 33m ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 6.3k • 🔱 765 • 7h ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 5.0k • 🔱 561 • 18m ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 4.3k • 🔱 342 • 1d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402.

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `deepseek`

⭐ 3.9k • 🔱 371 • 7h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.7k • 🔱 500 • 2d ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.3k • 🔱 355 • 12h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 3.2k • 🔱 230 • 2h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.1k • 🔱 606 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
