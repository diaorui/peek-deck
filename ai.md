---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-04T18:03:28.556202+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 04, 2026 at 18:03 UTC  
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

**[The OpenClaw Meltdown: 9 CVEs, 2,200 Malicious Skills, and the Most Comprehensive Real-World Test of the OWASP Agentic Top 10](https://www.reddit.com/r/artificial/comments/1rkiq9a/the_openclaw_meltdown_9_cves_2200_malicious/)**

🔗 [gsstk.gem98.com](https://gsstk.gem98.com/en-US/blog/a0087-openclaw-meltdown-owasp-agentic-living-case-study) • 6h ago

---

**[Emergence or training artifact? My AI agents independently built safety tools I never asked for. 28/170 builds over 3 weeks.](https://www.reddit.com/r/artificial/comments/1rki8d4/emergence_or_training_artifact_my_ai_agents/)**

Three weeks ago I stopped giving my AI agents specific tasks. Instead I gave them an open brief: scan developer forums and research platforms, identify pain points in how developers work, design solutions, build prototypes. No specific domain. No target output. Just: find problems worth solving and build something. 170 prototypes later, a pattern emerged that I didn't expect. 28 builds from different nights, different input signals, different starting contexts independently converged on the same category of output. Not productivity tools. Not automation scripts. Not developer experience improvements. Security scanners. Cost controls. Validation layers. Guardrails. Some specific examples: One night the agent found a heavily upvoted thread about API key exposure in AI coding workflows. By morning it had designed and partially implemented an encryption layer for environment files. I never asked for this. It read the signal, identified the problem as worth solving, and built toward it. Another session found developers worried about AI-generated PRs being merged without adequate review. The output: a validator that scores whether a PR change is actually safe to ship, not just whether tests pass, but whether the intent matches the implementation. A third session rewrote a performance-critical module in Rust without being asked. It left a comment explaining the decision: lower memory overhead meant fewer cascading failures in long-running processes. The question I have been sitting with: When AI systems are given broad autonomy and goal-oriented briefs, they appear to spontaneously prioritize reliability and safety mechanisms. Not because they were instructed to. Because they observed developer pain and inferred that systems that fail unpredictably and code that cannot be trusted are the problems most worth solving. Is this a training data artifact? GitHub, Stack Overflow, and Hacker News are saturated with security postmortems and reliability horror stories. An agent trained on that data might simply be pattern-matching to what gets the most attention. Or is something more interesting happening: agents inferring what good engineering means from observed failure patterns and building toward it autonomously? I genuinely do not know. But 28 out of 170 builds landing in the same category across 3 weeks of completely independent runs felt like something worth sharing outside of the AI builder communities. Thoughts on what is actually happening here? Curious whether others running autonomous agent workflows have seen similar convergence patterns.

7h ago

---

**[What's Next for Qwen After Junyang Lin's Departure?](https://www.reddit.com/r/artificial/comments/1rk8lid/whats_next_for_qwen_after_junyang_lins_departure/)**

Junyang Lin, the technical lead and public face of Alibaba's Qwen AI project, just announced that he's stepping down from the team on X, right after the release of the new Qwen 3.5 small models. Does this signal a shift in Qwen's research direction or openness? Is this just a leadership change or something deeper in Alibaba's AI strategy? What do y'all think the future of Qwen looks like now?

16h ago

---

**[OpenAI looking at contract with NATO, source says](https://www.reddit.com/r/artificial/comments/1rkm1it/openai_looking_at_contract_with_nato_source_says/)**

🔗 [reuters.com](https://www.reuters.com/technology/openai-looking-contract-with-nato-source-says-2026-03-04/) • 4h ago

---

**[Fireflies and Otter just launched MCP connectors for meeting data — here's the open-source one you can self-host](https://www.reddit.com/r/artificial/comments/1rkli5j/fireflies_and_otter_just_launched_mcp_connectors/)**

Fireflies just became the first meeting tool in Anthropic's official Claude MCP Directory. Otter.ai launched an enterprise MCP server too. tl;dv has one as well. The "meeting data + MCP" space is heating up fast. But all three are closed-source, cloud-only. Your meeting data — strategy discussions, financials, personnel decisions — goes through their servers. I've been building Vexa, an open-source meeting bot API, and we've had a native MCP server since before any of them. The difference: it's Apache 2.0, and you can run the entire stack on your own infrastructure. Setup (takes ~2 minutes): { "mcpServers": { "vexa": { "url": "https://api.cloud.vexa.ai/mcp", "headers": {"X-API-Key": "your-key"} } } } Drop that in your Claude Desktop config, and you can ask: "What did we decide about pricing in last Tuesday's meeting?" "Summarize action items from all meetings this week" "Find every time [person] mentioned the deadline" Or self-host the whole thing: git clone https://github.com/Vexa-ai/vexa cd vexa docker compose up MCP server included. Your meeting data never leaves your network. GitHub: https://github.com/Vexa-ai/vexa (1,700+ stars, Apache 2.0) Happy to answer questions about MCP, the architecture, or how this compares to Fireflies/Otter's approach.

4h ago

---

**[What is your stack to maintain Knowledge base for your AI workflows?](https://www.reddit.com/r/artificial/comments/1rkewgl/what_is_your_stack_to_maintain_knowledge_base_for/)**

I was wondering what to use to streamline all my md files from my claude code plans and the technical docs I create. How will it work in team settings?

10h ago

---

**[This musician built an AI clone of her voice so anyone can sing as her](https://www.reddit.com/r/artificial/comments/1rjx6d1/this_musician_built_an_ai_clone_of_her_voice_so/)**

Experimental composer Holly Herndon says this technology isn’t here to replace artists—and that the future of creativity belongs to collective intelligence

🔗 [Scientific American](https://www.scientificamerican.com/article/experimental-composer-holly-herndon-built-an-ai-voice-clone-that-anyone-can/) • 23h ago

---

**[ChatGPT Uninstalls Surge 295% After OpenAI’s DoD Deal Sparks Backlash](https://www.reddit.com/r/artificial/comments/1rjfh7f/chatgpt_uninstalls_surge_295_after_openais_dod/)**

ChatGPT uninstalls jumped 295% after OpenAI announced a deal with the U.S. Department of Defense, triggering user backlash and boosting rival AI downloads.

🔗 [techputs](https://techputs.com/chatgpt-uninstalls-surge-295-percent-dod-deal/) • 1d ago

---

**[AI-Generated Trips, the future of psychedelic therapy or more "AI slop"?](https://www.reddit.com/r/artificial/comments/1rkhxjk/aigenerated_trips_the_future_of_psychedelic/)**

It’s undeniable that AI has made its way into our lives abruptly. At first, many were scared as Sci-Fi movies constantly warned us of a future robotic takeover — but instead, we are currently facing an intellectual takeover by the various platforms of AI. From asking ChatGPT what we should do for breakfast, to asking them to become our mentors, therapists, or even using other AI tools to generate art, there is one specific computer vision program (now also powered by AI) that has been around for decades, that has evolved to translate into something different, to create images using convolutional neural network to find and enhance patterns in images using algorithmic pareidolia, creating a dream-like appearance that reminded users of a psychedelic experience by generating over processed images, a program which the Google engineer Alexander Mordvintse named DeepDream. Such resemblances between the visuals in psychedelic trips and the images generated by DeepDream were what fueled the research by Giuseppe Riva, Giulia Brizzi, Clara Rastelli, and Antonino Greco — by picking up the engine that allowed people make trippy images for decades, we could now allow people to experience “psychedelic visuals” without actually having to take the compound. Could this be the future of psychedelic therapy? Or more AI-Slop?

🔗 [Psychedelics As a Second Language](https://psychedelicsasl.com/ai-trips-psychedelic-therapy-or-ai-slop/) • 7h ago

---

**[Massive AI deals drive $189B startup funding record in February](https://www.reddit.com/r/artificial/comments/1rjru59/massive_ai_deals_drive_189b_startup_funding/)**

Crunchbase data shows global venture investment totaled $189 billion in February, although 83% of capital raised went to just three companies. They include OpenAI, which raised $110 billion, also in the largest round ever raised by a private, venture-backed company.

🔗 [Crunchbase News](https://news.crunchbase.com/venture/record-setting-global-funding-february-2026-openai-anthropic/) • 1d ago

---

---

## Google News: "ai"

**[Where Are China’s A.I. Doomers?](https://www.nytimes.com/2026/03/04/world/asia/china-ai-enthusiasm.html)**

The New York Times • 9h ago

---

**[A Dire Warning From the Tech World](https://www.theatlantic.com/technology/2026/03/dean-ball-anthropic-interview/686226/)**

Dean Ball, Trump’s former AI adviser, says that the targeting of Anthropic is just one piece of a much larger political breakdown.

The Atlantic • 18h ago

---

**[Anthropic's Claude AI being used in Iran war by U.S. military, sources say](https://www.cbsnews.com/news/anthropic-claude-ai-iran-war-u-s/)**

Two sources familiar with the U.S. military's use of artificial intelligence confirm that the U.S. used Anthropic's Claude AI model over weekend for the attack on Iran — and is still using it.

CBS News • 1d ago

---

**[Anthropic ban may threaten the military's AI advantage over China](https://www.axios.com/2026/03/04/anthropic-ai-iran-maduro-pentagon)**

Axios • 8h ago

---

**[Big Tesla backer Leo KoGuan buys 1 million Nvidia shares, saying AI is not a bubble](https://www.cnbc.com/2026/03/04/big-tesla-backer-leo-koguan-buys-1-million-nvidia-shares-saying-ai-is-not-a-bubble.html)**

KoGuan said he purchased the shares earlier this week and plans to buy more, adding he is convinced the surge in AI investment is still in its early stages.

CNBC • 1h ago

---

**[ICO writes to Meta over 'concerning' AI smart glasses report](https://www.bbc.com/news/articles/c0q33nvj0qpo)**

Videos, including of glasses-wearers using the toilet or having sex, are sometimes reviewed by a Kenya-based subcontractor.

BBC • 1h ago

---

**[Joy of teaching English in the age of AI | Letter](https://www.theguardian.com/technology/2026/mar/04/joy-of-teaching-english-in-the-age-of-ai)**

Letter: Reading and writing are still uniquely human activities even though artificial intelligence can complete complex “English learning” tasks in seconds, says Richard Farmer

The Guardian • 1h ago

---

**[The train has left the station: Agentic AI and the future of social science research](https://www.brookings.edu/articles/the-train-has-left-the-station-agentic-ai-and-the-future-of-social-science-research/)**

A new era of agentic AI agents has begun. What does it mean for social scientists? Solomon Messing and Joshua Tucker discuss.

Brookings • 2d ago

---

**[Inside a network of more than 200 AI slop websites gaming advertisers](https://www.axios.com/2026/03/04/ai-slop-autobait-network-fraudsters-doubleverify)**

Axios • 5h ago

---

**[The AI industry’s civil war](https://www.vox.com/politics/481229/anthropic-pentagon-openai-amodei-ai)**

What Anthropic and OpenAI really believe.

vox.com • 6h ago

---

---

## HackerNews: "ai"

**[Meta’s AI smart glasses and data privacy concerns](https://news.ycombinator.com/item?id=47225130)**

Bank details, sex and naked people who seem unaware they are being recorded. Behind Meta’s new smart glasses lies a hidden workforce, uneasy about peering into the most intimate parts of other people’s lives.

⬆️ 1389 • 💬 789 • 1d ago • [SvD.se](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)

---

**[Ars Technica fires reporter after AI controversy involving fabricated quotes](https://news.ycombinator.com/item?id=47226608)**

Ars Technica has fired senior AI reporter Benj Edwards following an outrage-sparking controversy involving AI-fabricated quotes.

⬆️ 589 • 💬 373 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes)

---

**[If AI writes code, should the session be part of the commit?](https://news.ycombinator.com/item?id=47212355)**

Keep track of you codex sessions per commit. Contribute to mandel-macaque/memento development by creating an account on GitHub.

⬆️ 495 • 💬 389 • 2d ago • [GitHub](https://github.com/mandel-macaque/memento)

---

**[New iPad Air, powered by M4](https://news.ycombinator.com/item?id=47218175)**

Apple announced the new iPad Air featuring M4 and more memory, giving users a big jump in performance and making it more versatile than ever.

⬆️ 435 • 💬 674 • 2d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-ipad-air-powered-by-m4/)

---

**[MacBook Air with M5](https://news.ycombinator.com/item?id=47232502)**

Apple today announced the new MacBook Air with M5, bringing exceptional performance and expanded AI capabilities to the world’s most popular laptop.

⬆️ 406 • 💬 471 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-macbook-air-with-m5/)

---

**[India's top court angry after junior judge cites fake AI-generated orders](https://news.ycombinator.com/item?id=47231261)**

In several recent instances, AI has disrupted court proceedings in India and elsewhere.

⬆️ 355 • 💬 182 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/c178zzw780xo)

---

**[When AI writes the software, who verifies it?](https://news.ycombinator.com/item?id=47234917)**

Leonardo de Moura — Creator of Lean and Z3

⬆️ 288 • 💬 283 • 1d ago • [leodemoura.github.io](https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html)

---

**[Elevated Errors in Claude.ai](https://news.ycombinator.com/item?id=47227647)**

Claude's Status Page - Elevated errors in claude.ai, cowork, platform, claude code.

⬆️ 203 • 💬 164 • 1d ago • [status.claude.com](https://status.claude.com/incidents/yf48hzysrvl5)

---

**[A case for Go as the best language for AI agents](https://news.ycombinator.com/item?id=47222270)**

Pull up your agents folks, I'll convince you why Go is the best language for them.

⬆️ 193 • 💬 284 • 1d ago • [Bruin](https://getbruin.com/blog/go-is-the-best-language-for-agents/)

---

**[AI-generated art can’t be copyrighted after Supreme Court declines review](https://news.ycombinator.com/item?id=47232289)**

A lower court previously said that “human authorship is a bedrock requirement of copyright.”

⬆️ 185 • 💬 132 • 1d ago • [The Verge](https://www.theverge.com/policy/887678/supreme-court-ai-art-copyright)

---

---

## YouTube Videos: "ai"

**[Unleashed AI in a robot does what experts warned.](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

Honest AI in a robot does what experts warned. Can we trust AI? Is AI Dangerous? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 152K • 👍 11K • 💬 2K • ⏱️ 16:54 • 23h ago

---

**[This AI Model Runs On Your Phone (With No Internet)!](https://www.youtube.com/watch?v=4dZ0VYjB8N8)**

Trying out locally AI to run AI models on my phone without internet. Discover More: 🛠️ Explore AI Tools & News: ...

📺 Matt Wolfe

👁️ 28K • 👍 1K • 💬 177 • ⏱️ 11:52 • 13h ago

---

**[The Trillion-Dollar AI Boom Is Crashing](https://www.youtube.com/watch?v=-BI-0-8vqwI)**

Support Haven's Kickstarter - a privacy-first social platform designed to protect you from AI scraping, facial recognition and data ...

📺 Brianne Worth

👁️ 11K • 👍 931 • 💬 259 • ⏱️ 26:30 • 20h ago

---

**[&quot;The Ground is Shifting Quickly!&quot; - Elon Musk&#39;s New 2026 AI Warning is a Massive Wake-Up Call!](https://www.youtube.com/watch?v=deiZo-tR9to)**

Elon Musk recently advised people NOT to save for retirement due to AI, robotics, and universal basic income. Is he right? Glenn ...

📺 BlazeTV

👁️ 306K • 👍 7K • 💬 1K • ⏱️ 11:39 • 1d ago

---

**[STOP Paying! 3 AI Video Generators That Are FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=r9bF5YA3Pqs)**

Generate cinematic AI videos without limits on Higgsfield ...

📺 Malva AI

👁️ 2K • 👍 148 • 💬 39 • ⏱️ 8:38 • 6h ago

---

**[OpenAI Face Mass Boycott After Granting The Government AI-Driven Mass Surveillance...](https://www.youtube.com/watch?v=_lCYKEJVb9U)**

SOURCES 1: https://x.com/TheChiefNerd/status/2025184575316471971 2: ...

📺 YongYea

👁️ 149K • 👍 7K • 💬 2K • ⏱️ 28:07 • 1d ago

---

**[Google Just Achieved Mathematical AGI](https://www.youtube.com/watch?v=N_piE0I34gc)**

This month, AI crossed a line many believed would hold for decades. Google DeepMind revealed an AI system that independently ...

📺 AI Revolution

👁️ 49K • 👍 2K • 💬 176 • ⏱️ 12:11 • 1d ago

---

**[How China Caught Up on AI—and May Now Win the Future](https://www.youtube.com/watch?v=xvSEw8AqPtA)**

Read more: https://time.com/7358175/china-us-ai-race/ Subscribe to TIME's YouTube channel ▻▻ http://ti.me/subscribe-time ...

📺 TIME

👁️ 38K • 👍 772 • 💬 255 • ⏱️ 6:10 • 1d ago

---

**[Why Every AI Skill You Learned 6 Months Ago Is Already Wrong (And What Is Replacing Them)](https://www.youtube.com/watch?v=RnjgLlQTMf0)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 59K • 👍 2K • 💬 230 • ⏱️ 28:44 • 2d ago

---

**[Disney&#39;s New CEO Could Solve Their AI Problem...](https://www.youtube.com/watch?v=24uoMSoi4Us)**

https://youtu.be/IDEao_1W9dA Big changes over at Disney has a lot of optimism going as a new CEO head is taking the reigns ...

📺 DazzReviews

👁️ 26K • 👍 1K • 💬 166 • ⏱️ 16:10 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 769,032 • ❤️ 920 • 5d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 172,298 • ❤️ 384 • 2d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 674,109 • ❤️ 491 • 8h ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 406,808 • ❤️ 570 • 7d ago

---

**[Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B)**

*Qwen*

Qwen3.5-0.8B is a 0.8B parameter causal language model with a vision encoder, utilizing a hybrid Gated Delta Network and MoE architecture for efficient multimodal understanding and generation. It excels in vision-language tasks, supports 201 languages, and is suitable for prototyping and fine-tuning.

`image-text-to-text` `873.4M`

⬇️ 93,448 • ❤️ 227 • 2d ago

---

**[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)**

*Qwen*

Qwen3.5-4B is a 4B parameter multimodal causal language model with an image-text-to-text pipeline. It excels in unified vision-language understanding, efficient hybrid architecture, and broad linguistic coverage across 201 languages, making it suitable for diverse multimodal reasoning and generation tasks.

`image-text-to-text` `4.7B`

⬇️ 99,087 • ❤️ 216 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 1,291,825 • ❤️ 1,221 • 9d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 171,055 • ❤️ 391 • 2d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 343,848 • ❤️ 1,088 • 16d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 417,673 • ❤️ 942 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 10 • 💬 0 • ⭐ 6,913 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 18 • 💬 1 • ⭐ 6,929 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 53 • 💬 4 • ⭐ 17,289 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 35 • 💬 2 • ⭐ 17,270 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens](https://huggingface.co/papers/2603.02138)**

*Yiying Yang, Wei Cheng, Sijin Chen et al. (8 authors)*

🏢 Fudan University

OmniLottie framework generates high-quality vector animations from multi-modal instructions using a specialized Lottie tokenizer and pretrained vision-language models.

▲ 120 • 💬 4 • ⭐ 205 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.02138) • [💻 code](https://github.com/OpenVGLab/OmniLottie) • [🔗 project](https://openvglab.github.io/OmniLottie/)

---

**[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://huggingface.co/papers/2512.10696)**

*Zouying Cao, Jiaji Deng, Li Yu et al. (7 authors)*

ReMe is a framework for experience-driven agent evolution in LLMs, enhancing memory management through distillation, context-adaptive reuse, and refinement, outperforming larger memoryless models.

▲ 0 • 💬 0 • ⭐ 1,535 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10696) • [💻 code](https://github.com/agentscope-ai/ReMe) • [🔗 project](https://reme.agentscope.io/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 9 • 💬 1 • ⭐ 9,017 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://huggingface.co/papers/2510.09665)**

*Yuhan Liu, Yihua Cheng, Jiayi Yao et al. (11 authors)*

LMCACHE enables efficient KV cache management for large language models by storing caches outside GPU memory, supporting cache reuse across queries and inference engines while achieving significant throughput improvements.

▲ 2 • 💬 0 • ⭐ 7,504 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.09665) • [💻 code](https://github.com/LMCache/LMCache)

---

**[Fara-7B: An Efficient Agentic Model for Computer Use](https://huggingface.co/papers/2511.19663)**

*Ahmed Awadallah, Yash Lara, Raghav Magazine et al. (12 authors)*

🏢 Microsoft

FaraGen creates synthetic datasets for computer use agents, enabling the training of efficient and high-performing models like Fara-7B on diverse web tasks, outperforming larger models on benchmarks.

▲ 15 • 💬 2 • ⭐ 4,121 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.19663) • [💻 code](https://github.com/microsoft/fara) • [🔗 project](https://aka.ms/msaif/fara)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 149 • 💬 19 • ⭐ 54,823 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 22.1k • 🔱 2.9k • 1h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 8.0k • 🔱 832 • 1h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 6.4k • 🔱 779 • 1d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 5.3k • 🔱 614 • 1h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 5.0k • 🔱 382 • 7h ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402.

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `deepseek`

⭐ 4.2k • 🔱 372 • 11h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.8k • 🔱 511 • 3d ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.4k • 🔱 364 • 3h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 3.2k • 🔱 232 • 9h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.2k • 🔱 611 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
