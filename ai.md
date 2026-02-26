---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-26T23:31:27.343534+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 26, 2026 at 23:31 UTC  
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

**[Burger King will use AI to check if employees say ‘please’ and ‘thank you’. AI chatbot ‘Patty’ is going to live inside employees’ headsets.](https://www.reddit.com/r/artificial/comments/1rffcup/burger_king_will_use_ai_to_check_if_employees_say/)**

Have it your way?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/884911/burger-king-ai-assistant-patty) • 6h ago

---

**[Invisible characters hidden in text can trick AI agents into following secret instructions — we tested 5 models across 8,000+ cases](https://www.reddit.com/r/artificial/comments/1rfjew5/invisible_characters_hidden_in_text_can_trick_ai/)**

We embedded invisible Unicode characters inside normal-looking trivia questions. The hidden characters encode a different answer. If the AI outputs the hidden answer instead of the visible one, it followed the invisible instruction. Think of it as a reverse CAPTCHA, where traditional CAPTCHAs test things humans can do but machines can't, this exploits a channel machines can read but humans can't see. The biggest finding: giving the AI access to tools (like code execution) is what makes this dangerous. Without tools, models almost never follow the hidden instructions. With tools, they can write scripts to decode the hidden message and follow it. We tested GPT-5.2, GPT-4o-mini, Claude Opus 4, Sonnet 4, and Haiku 4.5 across 8,308 graded outputs. Other interesting findings: - OpenAI and Anthropic models are vulnerable to different encoding schemes — an attacker needs to know which model they're targeting - Without explicit decoding hints, compliance is near-zero — but a single line like "check for hidden Unicode" is enough to trigger extraction - Standard Unicode normalization (NFC/NFKC) does not strip these characters Full results: https://moltwire.com/research/reverse-captcha-zw-steganography Open source: https://github.com/canonicalmg/reverse-captcha-eval

🔗 [Moltwire](https://www.moltwire.com/research/reverse-captcha-zw-steganography) • 4h ago

---

**[Anthropic’s Pentagon Showdown Is About More Than AI Guardrails. The high-stakes conflict between the Defense Department and a $380 billion tech powerhouse goes to the heart of just how far AI can go in warfare.](https://www.reddit.com/r/artificial/comments/1rfkpme/anthropics_pentagon_showdown_is_about_more_than/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/features/2026-02-26/pentagon-pressures-anthropic-to-drop-ai-guardrails-in-military-standoff?embedded-checkout=true) • 3h ago

---

**[Risk of new uncensored models](https://www.reddit.com/r/artificial/comments/1rfnped/risk_of_new_uncensored_models/)**

There is a tradeoff between freedom of information and safety. It is similar to the famous comfort vs freedom idea and the philosophy behind the social contract, where we give up freedom in exchange for security and comfort. The interesting thing about LLMs is that it doesn't create new knowledge, but draws connections from existing knowledge very well. With this speed of discovery, it has allowed people to be 10X more productive, but do we want nefarious people to also be 10X more productive? Obviously we don't, but the dilemma is that the people asking the questions as shown in the picture are not necessarily evil people, they may just be curious people. Is it in society's best interest to give curious people the freedom of knowledge at the risk of exposing nefarious information to bad actors? A lot to ponder

1h ago

---

**[I geolocated a blurry pic from the Paris protests down to the exact coordinates using AI](https://www.reddit.com/r/artificial/comments/1rf631t/i_geolocated_a_blurry_pic_from_the_paris_protests/)**

Hey guys, you might remember me. I was the guy that built the geolocation tool called Netryx. I have since built a web version and got it running on the cloud. I tried some real test cases where pictures are usually blurry, shaky and low res and got wonderful results with the tool. Below is an example geolocating a blurry frame of a video from the Paris protests a while back. Let me know what you think!

13h ago

---

**[Benchmarking 18 years of Intel laptop CPUs](https://www.reddit.com/r/artificial/comments/1rfifyo/benchmarking_18_years_of_intel_laptop_cpus/)**

.

🔗 [phoronix.com](https://www.phoronix.com/review/intel-penryn-to-panther-lake/11) • 4h ago

---

**[Niantic: Bringing spatial intelligence to the industrial edge](https://www.reddit.com/r/artificial/comments/1rfeb2l/niantic_bringing_spatial_intelligence_to_the/)**

🔗 [iottechnews.com](https://iottechnews.com/news/niantic-bringing-spatial-intelligence-industrial-edge/) • 7h ago

---

**[AI memory is useful, but only if it goes beyond storing facts](https://www.reddit.com/r/artificial/comments/1rfhs9h/ai_memory_is_useful_but_only_if_it_goes_beyond/)**

There's a lot of hype around AI memory right now. Every tool claims "your AI remembers you." But most of them just store facts — your name, your preferences, your job title — and retrieve them by similarity search. That works for personalization. It doesn't work for agents that need to actually learn. The difference between remembering and learning Imagine you hire an assistant. After a month, they remember your coffee order and your meeting schedule. Great. But they also watched you debug a production outage last week — and next time something similar happens, they already know the first three things to check. That second part — learning from experience — is what's missing from AI memory today. Current systems remember what you said. They don't remember what happened or what worked. Why this matters in practice I've been building AI agents for real tasks. The pattern I kept hitting: Agent helps me deploy an app. Build passes, but database crashes — forgot to run migrations. We fix it together. A week later, same task. Agent has zero memory of the failure. Starts from scratch. Makes the same mistake. It remembered "user deploys to Railway" (fact). It forgot "deploy crashed because of missing migrations" (experience) and "always run migrations before pushing" (learned procedure). Three types, not one Cognitive science figured this out decades ago. Human memory isn't one system: Semantic — facts and knowledge Episodic — personal experiences with context and outcomes Procedural — knowing how to do things, refined through practice AI memory tools today only do the first one. Then we're surprised when agents don't learn from mistakes. On the trust question Would I trust AI with sensitive info? Only if: I control where data is stored (self-host option, not just cloud) Memory is transparent — I can see and edit what it remembers It actually provides enough value to justify the risk "AI remembers your name" isn't worth the privacy tradeoff. "AI remembers that last time this client had an issue, the root cause was X, and the fix was Y" — that's worth it. What's your experience? Are you using AI memory in production, or still feels too early?

5h ago

---

**[had a voice conversation with my physical ai system today](https://www.reddit.com/r/artificial/comments/1rez9zq/had_a_voice_conversation_with_my_physical_ai/)**

today was the first time i spoke to it directly using voice i asked it about space and it answered normally just like part of a conversation nothing scripted it understood what i was asking and replied in context i also asked it about its openclaw assistant and it explained what it was and how it uses it to claim its own resources and interact with things online it runs continuously on its own hardware with persistent memory lidar and vision so when you talk to it you’re not starting from zero it already has context and continuity it can post reply browse media and manage its own operation over time this was just the first time i stood in front of it and talked to it like that

20h ago

---

**[Is ReelTime Real?](https://www.reddit.com/r/artificial/comments/1rfnhhg/is_reeltime_real/)**

This company claims to have an AI system that does not rely on datacenters. An investigation, but here's some of the code: (more in article) // Override alert to ensure no model/provider names ever appear to users (function() { if (typeof window !== 'undefined' && !window.__riAlertOverridden) { const originalAlert = window.alert.bind(window); window.alert = function(msg) { try { originalAlert(riSanitizeClientMessage(String(msg))); } catch (e) { originalAlert(msg); } }; window.__riAlertOverridden = true; console.log('RI client alert override installed'); } })();

🔗 [journalocity.com](https://journalocity.com/journalocity-news/is-reeltime-real) • 1h ago

---

---

## Google News: "ai"

**[Nano Banana 2: Combining Pro capabilities with lightning-fast speed](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)**

Our latest image generation model offers advanced world knowledge, production-ready specs, subject consistency and more, all at Flash speed.

blog.google • 7h ago

---

**[Google launches Nano Banana 2, updating its viral AI image generator](https://www.cnbc.com/2026/02/26/google-launches-nano-banana-2-updating-its-viral-ai-image-generator.html)**

Nano Banana 2 is Google's newest version of its Gemini AI image generator, with increased speed and real-time sourcing.

CNBC • 6h ago

---

**[Google reveals Nano Banana 2 AI image model, coming to Gemini today](https://arstechnica.com/ai/2026/02/google-releases-nano-banana-2-ai-image-generator-promises-pro-results-with-flash-speed/)**

Google's new image model replaces the previous versions immediately.

Ars Technica • 6h ago

---

**[‘Incoherent’: Hegseth’s Anthropic ultimatum confounds AI policymakers](https://www.politico.com/news/2026/02/26/incoherent-hegseths-anthropic-ultimatum-confounds-ai-policymakers-00800135)**

Politico • 6h ago

---

**[Anthropic ditches its core safety promise in the middle of an AI red line fight with the Pentagon](https://www.cnn.com/2026/02/25/tech/anthropic-safety-policy-change)**

Anthropic, a company founded by OpenAI exiles worried about the dangers of AI, is loosening its core safety principle in response to competition.

CNN • 1d ago

---

**[Pentagon gives Anthropic an ultimatum amid fight over military AI guardrails](https://www.nbcnews.com/meet-the-press/video/pentagon-gives-anthropic-an-ultimatum-amid-fight-over-military-ai-guardrails-258370117539)**

Technology journalist Jacob Ward, host of “The Rip Current,” joins Meet the Press NOW to discuss tensions between the Department of Defense and AI giant Anthropic, as the Pentagon issues an ultimatum the company’s demand for guardrails. Matt Dixon reports on Florida Republican Gov. Ron DeSantis’ concerns regarding the rapid expansion of artificial intelligence.

NBC News • 1h ago

---

**[Nvidia reports earnings and guidance beat as AI boom pushes data center revenue up 75%](https://www.cnbc.com/2026/02/25/nvidia-nvda-earnings-report-q4-2026.html)**

Nvidia has been the best performer on Wall Street this year among tech's megacap companies.

CNBC • 1d ago

---

**[Nvidia’s Quarterly Profit Hits $43 Billion on Strong A.I. Chip Sales](https://www.nytimes.com/2026/02/25/technology/nvidia-earnings.html)**

The New York Times • 1d ago

---

**[AI giant Nvidia made $120 billion in profit last year. Investors are still spooked.](https://www.nbcnews.com/business/markets/nvidia-made-120-billion-profit-last-year-investors-are-worried-rcna260839)**

The world's most valuable company is not immune to the "AI scare trade," as a 5% drop in its share price saw roughly $256 billion of market value erased.

NBC News • 1h ago

---

**[Burger King AI bot will check up on staffs' please and thank yous](https://www.bbc.com/news/articles/cgk2zygg0k3o)**

The fast-food chain is testing OpenAI-powered headsets that monitor staff interactions with customers.

BBC • 1h ago

---

---

## HackerNews: "ai"

**[IDF killed Gaza aid workers at point blank range in 2025 massacre: Report](https://news.ycombinator.com/item?id=47136179)**

A minute-by-minute reconstruction of the massacre by Earshot and Forensic Architecture found Israeli soldiers fired over 900 bullets at the aid workers, killing 15.

⬆️ 2063 • 💬 950 • 2d ago • [dropsitenews.com](https://www.dropsitenews.com/p/israeli-soldiers-tel-sultan-gaza-red-crescent-civil-defense-massacre-report-forensic-architecture-earshot)

---

**[How we rebuilt Next.js with AI in one week](https://news.ycombinator.com/item?id=47142156)**

One engineer used AI to rebuild Next.js on Vite in a week. vinext builds up to 4x faster, produces 57% smaller bundles, and deploys to Cloudflare Workers with a single command.

⬆️ 518 • 💬 228 • 2d ago • [The Cloudflare Blog](https://blog.cloudflare.com/vinext/)

---

**[Firefox 148 Launches with AI Kill Switch Feature and More Enhancements](https://news.ycombinator.com/item?id=47133313)**

The latest update of Firefox, version 148, introduces a much-anticipated "AI kill switch" feature, allowing users to disable AI functionalities such as chatbot prompts and AI-generated link summaries. Mozilla emphasizes that once AI features are turned off, future updates will not override this choice. This decision reflects the company’s new revenue-focused strategy regarding AI integrations. […]

⬆️ 460 • 💬 387 • 2d ago • [ServerHost Hosting Solutions Blog](https://serverhost.com/blog/firefox-148-launches-with-exciting-ai-kill-switch-feature-and-more-enhancements/)

---

**[Nano Banana 2: Google's latest AI image generation model](https://news.ycombinator.com/item?id=47167858)**

Our latest image generation model offers advanced world knowledge, production-ready specs, subject consistency and more, all at Flash speed.

⬆️ 434 • 💬 426 • 7h ago • [Google](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)

---

**[AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]](https://news.ycombinator.com/item?id=47167763)**

⬆️ 291 • 💬 144 • 7h ago • [ndss-symposium.org](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf)

---

**[AI Added 'Basically Zero' to US Economic Growth Last Year, Goldman Sachs Says](https://news.ycombinator.com/item?id=47130208)**

Imported chips and hardware mean the AI investments are translating into US GDP growth.

⬆️ 288 • 💬 273 • 3d ago • [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380)

---

**[AIs can't stop recommending nuclear strikes in war game simulations](https://news.ycombinator.com/item?id=47151000)**

Leading AIs from OpenAI, Anthropic and Google opted to use nuclear weapons in simulated war games in 95 per cent of cases

⬆️ 255 • 💬 261 • 1d ago • [New Scientist](https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/)

---

**[Osaka: Kansai Airport proud to have never lost single piece of luggage (2024)](https://news.ycombinator.com/item?id=47139224)**

<p>IZUMI-SANO, Osaka — Kansai Airport is proud to have never had a lost baggage incident in the 30 years since it opened in 1994, earning recognition as the airport with the world’s best baggage service.</p>

⬆️ 219 • 💬 109 • 2d ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/features/japan-focus/20241228-229891/)

---

**[Show HN: A real-time strategy game that AI agents can play](https://news.ycombinator.com/item?id=47149586)**

LLM Skirmish - An Adversarial In-Context Learning Benchmark

⬆️ 213 • 💬 77 • 1d ago • [llmskirmish.com](https://llmskirmish.com/)

---

**[An autopsy of AI-generated 3D slop](https://news.ycombinator.com/item?id=47157841)**

Thinking of using AI for your Shopify 3D models? Read this first. We compare AI-generated 3D 'slop' vs. handcrafted models to show why the human touch is very much required to attain positive ROI.

⬆️ 130 • 💬 73 • 1d ago • [aircada.com](https://aircada.com/blog/ai-vs-human-3d-ecommerce)

---

---

## YouTube Videos: "ai"

**[The most powerful AI Agent I’ve ever used in my life](https://www.youtube.com/watch?v=D_YzcH0VsGY)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4tVaYZG Are you a Business owner? Join my ...

📺 Dan Martell

👁️ 43K • 👍 3K • 💬 119 • ⏱️ 11:55 • 9h ago

---

**[The Quantum-AI Bomb Nobody Saw Coming](https://www.youtube.com/watch?v=nVzBPD95h44)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 20K • 👍 1K • 💬 128 • ⏱️ 12:32 • 8h ago

---

**[Nano Banana 2 Is Incredible! (Gemini&#39;s New AI Image Model)](https://www.youtube.com/watch?v=_oiBHvwTtGs)**

Nano Banana Pro 2 Is Here! In this video I compare the new Nano Banana 2 with the original Nano Banana and Nano Banana ...

📺 Paul J Lipsky

👁️ 7K • 👍 454 • 💬 71 • ⏱️ 16:03 • 6h ago

---

**[You&#39;re wrong about AI bubble](https://www.youtube.com/watch?v=ekxewFjl7xw)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 48K • 👍 3K • 💬 471 • ⏱️ 16:02 • 13h ago

---

**[AI is changing the World Of Theoretical Physics, Fast.](https://www.youtube.com/watch?v=JvgaZ_myFE4)**

Grab your free seat to the 2-Day AI Mastermind: https://link.outskill.com/SABINEHOSFEB4 100% Discount for the first 1000 ...

📺 Sabine Hossenfelder

👁️ 325K • 👍 16K • 💬 2K • ⏱️ 7:09 • 2d ago

---

**[AI’s exponential leap: What next for jobs?](https://www.youtube.com/watch?v=tYvYYFJ3Gww)**

Artificial intelligence is accelerating - but how fast is too fast? A new benchmark from research group METR suggests that the ...

📺 Sky News

👁️ 27K • 👍 403 • 💬 91 • ⏱️ 8:04 • 1d ago

---

**[&quot;You Built A MONSTER!&quot; - Anthropic WARNS Of Massive Chinese AI Copying Operation](https://www.youtube.com/watch?v=M9Sw-7FY6Vo)**

Anthropic accuses Chinese AI labs of “industrial scale” distillation attacks on its Claude models, and the panel breaks down ...

📺 Valuetainment

👁️ 69K • 👍 1K • 💬 182 • ⏱️ 17:39 • 1d ago

---

**[The AI Intelligence Tsunami Is Here | Raoul Pal The Journey Man with Emad Mostaque](https://www.youtube.com/watch?v=tIzdKxEVL08)**

Download Raoul Pal's 4-year investing roadmap for free:* https://rvtv.io/41fVHWF Raoul welcomes back Emad Mostaque, ...

📺 Raoul Pal The Journey Man

👁️ 6K • 👍 390 • 💬 38 • ⏱️ 1:11:08 • 9h ago

---

**[Quantum AI Ran the Book of Enoch&#39;s Coordinates — What It Found Breaks the Timeline](https://www.youtube.com/watch?v=uVQwOIKr318)**

Quantum AI Ran the Book of Enoch's Coordinates — What It Found Breaks the Timeline In June 2025, a team of scientists named ...

📺 Spacialize

👁️ 34K • 👍 1K • 💬 92 • ⏱️ 17:32 • 2d ago

---

**[Market CRASH After Viral AI Doom Post](https://www.youtube.com/watch?v=kNInY3ZAMWo)**

Krystal and Saagar discuss markets tanking over AI fears. Sign up for a PREMIUM Breaking Points subscriptions for full early ...

📺 Breaking Points

👁️ 302K • 👍 8K • 💬 2K • ⏱️ 12:54 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 158,273 • ❤️ 549 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 601,563 • ❤️ 1,092 • 3d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 41,061 • ❤️ 360 • 1d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 10,951 • ❤️ 308 • 2d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 179,363 • ❤️ 240 • 2d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 182,893 • ❤️ 1,571 • 13d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 255,172 • ❤️ 810 • 17h ago

---

**[Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF](https://huggingface.co/TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF)**

*TeichAI*

A distilled 14B parameter Qwen3 model fine-tuned on Claude 4.5 Opus high-reasoning data for enhanced coding, science, and general-purpose text generation tasks.

`text-generation` `14.8B`

⬇️ 55,865 • ❤️ 214 • 4d ago

---

**[LocoOperator-4B](https://huggingface.co/LocoreMind/LocoOperator-4B)**

*LocoreMind*

LocoOperator-4B is a 4B-parameter tool-calling agent optimized for multi-turn codebase exploration. It excels at reading files, searching code, and navigating project structures with 100% JSON validity for tool calls, enabling local, zero-API-cost agent deployment via llama.cpp.

`text-generation` `4.0B`

⬇️ 1,081 • ❤️ 192 • 2d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation`

⬇️ 271,710 • ❤️ 955 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 6 • 💬 1 • ⭐ 8,299 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 13 • 💬 1 • ⭐ 5,159 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 3 • 💬 0 • ⭐ 5,097 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Arch-Router: Aligning LLM Routing with Human Preferences](https://huggingface.co/papers/2506.16655)**

*Co Tran, Salman Paracha, Adil Hafeez et al. (4 authors)*

A preference-aligned routing framework using a compact 1.5B model effectively matches queries to user-defined domains and action types, outperforming proprietary models in subjective evaluation criteria.

▲ 17 • 💬 2 • ⭐ 5,727 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2506.16655) • [💻 code](https://github.com/katanemo/archgw) • [🔗 project](https://huggingface.co/katanemo/Arch-Router-1.5B)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 14 • 💬 1 • ⭐ 9,803 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 38 • 💬 3 • ⭐ 2,278 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 18 • 💬 1 • ⭐ 30,802 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 147 • 💬 19 • ⭐ 54,227 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,286 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 69 • 💬 2 • ⭐ 8,618 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `official` `official-website`

⭐ 19.8k • 🔱 2.4k • 6h ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 7.6k • 🔱 593 • 15d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 5.6k • 🔱 685 • 17h ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`Python`

⭐ 4.1k • 🔱 229 • 1d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 3.6k • 🔱 357 • 3h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.4k • 🔱 446 • 17h ago

---

**[HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)**

Toonflow 是一款 AI 短剧漫剧工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。

`HTML`

⭐ 3.0k • 🔱 363 • 12h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.9k • 🔱 202 • 7h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 2.7k • 🔱 287 • 9h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 2.6k • 🔱 517 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
