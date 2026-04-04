---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-04T09:06:25.727205+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 04, 2026 at 09:06 UTC  
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

**[Elon Musk Requires Banks Behind SpaceX IPO To Buy Grok Subscriptions, Report Says](https://www.reddit.com/r/artificial/comments/1sbxms5/elon_musk_requires_banks_behind_spacex_ipo_to_buy/)**

The offering is expected to be the largest in history.

🔗 [Yahoo Finance](https://uk.finance.yahoo.com/news/elon-musk-requires-banks-behind-185412887.html) • 6h ago

---

**[People anxious about deviating from what AI tells them to do?](https://www.reddit.com/r/artificial/comments/1sc2lip/people_anxious_about_deviating_from_what_ai_tells/)**

My friend came over yesterday to dye her hair. She had asked ChatGPT for the 'correct' way to do it. Chat told her to dye the ends first, wait about 20 minutes, and then do the roots. Because of my own experience with dyeing my hair, that made me sceptical, so I read the instructions in the box dye package. It specifically said to mix it and apply everything all at once. That's how this particular formula is designed to work. I read the instructions on the package out loud and told her we should just follow what the manufacturer says. She got visibly stressed and told me that 'ChatGPT said to do it differently'. I pointed out that the company who made the dye probably knows how their own product is supposed to be applied. She still got visibly anxious about going against what ChatGPT told her to do. It was such a weird moment. She was genuinely stressed about ignoring the AI even though the real instructions were right there in her hands. Has anybody had similar experiences?

1h ago

---

**[OpenAI CEO Sam Altman accused of sexual abuse by family member](https://www.reddit.com/r/artificial/comments/1sc3kpj/openai_ceo_sam_altman_accused_of_sexual_abuse_by/)**

🔗 [The Independent](https://www.independent.co.uk/bulletin/news/sam-altman-lawsuit-abuse-sexual-assault-sister-annie-b2950929.html) • 54m ago

---

**[NHS staff resist using Palantir software. Staff reportedly cite ethics concerns, privacy worries, and doubt the platform adds much](https://www.reddit.com/r/artificial/comments/1sbuf2a/nhs_staff_resist_using_palantir_software_staff/)**

: Staff reportedly cite ethics concerns, privacy worries, and doubt the platform adds much

🔗 [theregister.com](https://www.theregister.com/2026/04/03/nhs_staff_against_palantir/) • 8h ago

---

**[China moves to regulate digital humans , issues draft rules](https://www.reddit.com/r/artificial/comments/1sc3hhu/china_moves_to_regulate_digital_humans_issues/)**

🔗 [thebroadpost.com](https://www.thebroadpost.com/blog/china-moves-to-regulate-digital-humans-issues-draft-rules) • 59m ago

---

**[MIT study challenges AI job apocalypse narrative](https://www.reddit.com/r/artificial/comments/1sb7qxc/mit_study_challenges_ai_job_apocalypse_narrative/)**

🔗 [axios.com](https://www.axios.com/2026/04/02/ai-jobs-mit-study-workforce-impact) • 1d ago

---

**[Your prompts aren’t the problem — something else is](https://www.reddit.com/r/artificial/comments/1sc1n6u/your_prompts_arent_the_problem_something_else_is/)**

I keep seeing people focus heavily on prompt optimization. But in practice, a lot of failures I’ve observed don’t come from the prompt itself. They show up at the transition point where: model output → real-world action Examples: - outputs that are correct in isolation but wrong in context - timing mismatches (right decision, wrong moment) - differences between environments (test vs live) - small context gaps that compound into bad outcomes The pattern seems consistent: improving prompt quality doesn’t solve these failures. Because the issue isn’t generation — it’s what happens when outputs are interpreted, trusted, and acted on. Curious how others here think about this layer, especially in deployed systems..

2h ago

---

**[Study: LLMs Able to De-Anonymize User Accounts on Reddit, Hacker News & Other "Pseudonymous" Platforms; Report Co-Author Expands, Advises](https://www.reddit.com/r/artificial/comments/1sbndrb/study_llms_able_to_deanonymize_user_accounts_on/)**

Advice from the study's co-author: "Be aware that it’s not any single post that identifies you, but the combination of small details across many posts. And consider never posting anything you truly don’t want shared with the world.”

🔗 [wjamesau.substack.com](https://wjamesau.substack.com/p/warning-llms-able-to-de-anonymize) • 13h ago

---

**[Anyone else feel like AI security is being figured out in production right now?](https://www.reddit.com/r/artificial/comments/1sbgw8y/anyone_else_feel_like_ai_security_is_being/)**

I’ve been digging into AI security incident data from 2025 into this year, and it feels like something isn’t being talked about enough outside security circles. A lot of the issues aren’t advanced attacks. It’s the same pattern we’ve seen with new tech before. Things like prompt injection through external data, agents with too many permissions, or employees using AI tools the company doesn’t even know about. One stat I saw said enterprises are averaging 300+ unsanctioned AI apps, which is kind of wild. The incident data reflects that. Prompt injection is showing up in a large percentage of production deployments. There’s also been a noticeable increase in attacks exploiting basic gaps, partly because AI is making it easier for attackers to find weaknesses faster. Even credential leaks tied to AI usage have been increasing. What stood out to me isn’t just the attacks, it’s the gap underneath it. Only a small portion of companies actually have dedicated AI security teams. In many cases, AI security isn’t even owned by security teams. The tricky part is that traditional security knowledge only gets you part of the way. Some concepts carry over, like input validation or trust boundaries, but the details are different enough that your usual instincts don’t fully apply. Prompt injection isn’t the same as SQL injection. Agent permissions don’t behave like typical API auth. There are frameworks trying to catch up. OWASP now has lists for LLMs and agent-based systems. MITRE ATLAS maps AI-specific attack techniques. NIST has an AI risk framework. The guidance exists, but the number of people who can actually apply it feels limited. I’ve been trying to build that knowledge myself and found that more hands-on learning helps a lot more than just reading docs. Curious how others here are approaching this. If you’re building or working with AI systems, are you thinking about security upfront or mostly dealing with it after things are already live? Sources for those interested: AI Agent Security 2026 Report IBM 2026 X-Force Threat Index Adversa AI Security Incidents Report 2025 Acuvity State of AI Security 2025 OWASP Top 10 for LLM Applications OWASP Top 10 for Agentic AI MITRE ATLAS Framework

17h ago

---

**[do you guys actually trust AI tools with your data?](https://www.reddit.com/r/artificial/comments/1sboyjf/do_you_guys_actually_trust_ai_tools_with_your_data/)**

idk if it’s just me but lately i’ve been thinking about how casually we use stuff like chatgpt and claude for everything like coding, random ideas, sometimes even personal things and i don’t think most of us really know what happens to that data after we send it we just kind of assume it’s fine because the tools are useful also saw some discussion recently about AI companies and governments asking for user data (not sure how accurate it was), but it kind of made me think more about this whole thing i’m not saying anything bad is happening, just feels like we’ve gotten comfortable really fast without thinking much about it do you guys filter what you share or just use it normally?

12h ago

---

---

## Google News: "ai"

**[Economists Are Drawing Stronger Connections Between A.I. and Jobs](https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html)**

nytimes.com • 18h ago

---

**[AI is rewiring the world’s most prolific film industry](https://www.reuters.com/technology/ai-is-rewiring-worlds-most-prolific-film-industry-2026-04-04/)**

reuters.com • 4h ago

---

**[The invisible risk: Can you really trust your ‘private’ AI assistant to keep your secrets?](https://www.jpost.com/business-and-innovation/tech-and-start-ups/article-892014)**

TECH AFFAIRS: Research by Israeli cybersecurity company Check Point found a weakness in ChatGPT’s system that could allow someone to extract data without triggering any alarms.

The Jerusalem Post • 1h ago

---

**[McKinsey has a leadership playbook for AI that says: It's time to cut ...](https://timesofindia.indiatimes.com/technology/tech-news/mckinsey-has-a-leadership-playbook-for-ai-that-says-its-time-to-cut-/articleshow/130015342.cms)**

Tech News News: McKinsey reportedly has a new leadership playbook for the AI era and its message is clear: It's time for companies to cut the extra layers in manageme.

timesofindia.indiatimes.com • 1h ago

---

**[Create, edit and share videos at no cost in Google Vids](https://blog.google/products-and-platforms/products/workspace/google-vids-updates-lyria-veo/)**

New AI capabilities are coming to Google Vids, powered by Lyria 3 and Veo 3.1, like high-quality video generation at no cost and more.

blog.google • 1d ago

---

**[Silicon Valley Is in a Frenzy Over Bots That Build Themselves](https://www.theatlantic.com/technology/2026/04/ai-industry-self-improving-bots/686686/)**

How close are we really to self-improving AI?

The Atlantic • 15h ago

---

**[Anthropic’s next model could be a ‘watershed moment’ for cybersecurity. Experts say that could also be a concern](https://www.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity)**

The next wave of AI-powered cybersecurity attacks will be like nothing we’ve seen before.

CNN • 23h ago

---

**[AI animation studio Toonstar will turn books into digital shows for HarperCollins](https://www.engadget.com/ai/ai-animation-studio-toonstar-will-turn-books-into-digital-shows-for-harpercollins-211419155.html)**

HarperCollins is tapping into AI to bring some of its book franchises to life.

Engadget • 11h ago

---

**[What’s the point of an AI novel?](https://www.ft.com/content/b83fbd97-e85d-4e67-90de-bfb7bf8c8cde)**

The danger is not that it will replace human-authored books — but that we stop caring about good writing at all

Financial Times • 5h ago

---

**[Is It Wrong to Write a Book with A.I.?](https://www.newyorker.com/culture/open-questions/is-it-wrong-to-write-a-book-with-ai)**

The horror novel “Shy Girl” was cancelled for being generated at least partly through artificial intelligence. Would we ever accept such a book as art?

The New Yorker • 23h ago

---

---

## HackerNews: "ai"

**[Show HN: Apfel – The free AI already on your Mac](https://news.ycombinator.com/item?id=47624645)**

Use Apple's built-in AI from the terminal. No API keys, no cloud, no subscriptions. The LLM is already on your Mac.

⬆️ 672 • 💬 140 • 23h ago • [apfel.franzai.com](https://apfel.franzai.com)

---

**[We replaced RAG with a virtual filesystem for our AI documentation assistant](https://news.ycombinator.com/item?id=47618223)**

We replaced expensive sandboxes with ChromaFs, a virtual filesystem over Chroma, to give our docs AI assistant the ability to explore documentation like a developer would.

⬆️ 297 • 💬 118 • 1d ago • [Mintlify](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)

---

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 223 • 💬 117 • 2d ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 106 • 💬 21 • 2d ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 76 • 💬 37 • 2d ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[A $20/month user costs OpenAI $65 in compute. AI video is a money furnace](https://news.ycombinator.com/item?id=47619322)**

⬆️ 75 • 💬 42 • 1d ago • [aedelon777.substack.com](https://aedelon777.substack.com/p/i-did-the-math-on-sora-ai-video-is)

---

**["Cognitive surrender" leads AI users to abandon logical thinking, research finds](https://news.ycombinator.com/item?id=47632504)**

Experiments show large majorities uncritically accepting "faulty" AI answers.

⬆️ 75 • 💬 30 • 11h ago • [Ars Technica](https://arstechnica.com/ai/2026/04/research-finds-ai-users-scarily-willing-to-surrender-their-cognition-to-llms/)

---

**[Show HN: Travel Hacking Toolkit – Points search and trip planning with AI](https://news.ycombinator.com/item?id=47635033)**

AI-powered travel hacking with points, miles, and award flights. Drop-in skills and MCP servers for OpenCode and Claude Code. - borski/travel-hacking-toolkit

⬆️ 69 • 💬 30 • 6h ago • [GitHub](https://github.com/borski/travel-hacking-toolkit)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 62 • 💬 53 • 2d ago • [Baton](https://getbaton.dev/)

---

**[AI has suddenly become more useful to open-source developers](https://news.ycombinator.com/item?id=47601107)**

More open-source developers are finding that, when used properly, AI can actually help current and long-neglected programs. However, legal and quality issues loom.

⬆️ 54 • 💬 46 • 2d ago • [ZDNET](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

---

---

## YouTube Videos: "ai"

**[AI News: Anthropic Leak is Bigger Than You Think](https://www.youtube.com/watch?v=BZ1hs2ZcnJc)**

Here's the AI News you probably missed this week. Try Recraft V4 now and experience an image generation model with ...

📺 Matt Wolfe

👁️ 47K • 👍 2K • 💬 175 • ⏱️ 31:05 • 18h ago

---

**[Grok AI Was Asked Why Aliens Haven&#39;t Contacted Us — Its Answer Shook Scientists](https://www.youtube.com/watch?v=DVHGhq73u_g)**

Discover the mind‑bending response Grok AI gave when asked one of humanity's biggest questions: Why haven't aliens ...

📺 Luminox

👁️ 60K • 👍 2K • 💬 306 • ⏱️ 21:36 • 2d ago

---

**[Anthropic&#39;s New Claude CONWAY Is Unlike Any AI Before](https://www.youtube.com/watch?v=x2l7W9aTc5k)**

Anthropic is testing Claude Conway, a strange new AI system that looks less like a chatbot and more like a persistent agent ...

📺 AI Revolution

👁️ 58K • 👍 1K • 💬 76 • ⏱️ 10:50 • 1d ago

---

**[Liquid River Cascade 🌊💧✨ (Part 1) AI ASMR | Endless Flow &amp; Pure Relax Energy 🌀💫](https://www.youtube.com/watch?v=uLEBB9HDoFI)**

Welcome to Part 1 of Liquid River Cascade ✨   This place doesn't follow nature. It flows… differently. No wind. No sound.

📺 Satisfyra ASMR

👁️ 58K • 👍 4K • 💬 320 • ⏱️ 8:15 • 1d ago

---

**[The AI crisis no one is talking about](https://www.youtube.com/watch?v=ZcH5C8Jlltc)**

Asking ChatGPT about pi was the worst mistake he ever made. Become a member on YouTube: ...

📺 Mo Bitar

👁️ 95K • 👍 7K • 💬 1K • ⏱️ 6:33 • 21h ago

---

**[Private AI on the go… a new trick ](https://www.youtube.com/watch?v=PqBrnip-ZLw)**

I put a tiny MacBook Air between me and some ridiculously large local AI models... and it worked. Power Your Spring Essentials ...

📺 Alex Ziskind

👁️ 85K • 👍 3K • 💬 262 • ⏱️ 9:09 • 2d ago

---

**[I Tested An AI Car](https://www.youtube.com/watch?v=K4kLiat84eE)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 637K • 👍 43K • 💬 405 • ⏱️ 0:53 • 15h ago

---

**[Are humans useless in the AI workspace? | BBC News](https://www.youtube.com/watch?v=6zAgTga9kZw)**

AI Decoded explores how artificial intelligence is reshaping the future of work — asking whether jobs will disappear or be ...

📺 BBC News

👁️ 21K • 👍 574 • 💬 122 • ⏱️ 26:12 • 20h ago

---

**[AI BUBBLE POP?: HALF Of Datacenters Delayed/Canceled](https://www.youtube.com/watch?v=pkomxsk5hpY)**

Krystal and Saagar discuss the AI bubble imploding. Sign up for a PREMIUM Breaking Points subscriptions for full early access to ...

📺 Breaking Points

👁️ 329K • 👍 10K • 💬 2K • ⏱️ 13:15 • 1d ago

---

**[SNOW RAVEN - Aan Alaxchyn | Bridal Ceremony | No AI (OFFICIAL MUSIC VIDEO)](https://www.youtube.com/watch?v=9p-FybtoUnk)**

This video showcases a symbolic fragment of the extensive traditional Sakha wedding ritual, which historically could span up to ...

📺 SNOW RAVEN 

👁️ 5K • 👍 634 • 💬 53 • ⏱️ 4:33 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 524,224 • ❤️ 2,249 • 11d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 287,440 • ❤️ 735 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 96,615 • ❤️ 769 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 36,635 • ❤️ 872 • 8d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 32,930 • ❤️ 370 • 4d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 133,224 • ❤️ 315 • 1d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 5,096 • ❤️ 653 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 241,087 • ❤️ 497 • 10d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 715,586 • ❤️ 956 • 1mo ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 108,261 • ❤️ 265 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 150 • 💬 7 • ⭐ 35,720 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 18 • 💬 1 • ⭐ 14,151 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 35 • 💬 2 • ⭐ 46,762 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 18 • 💬 3 • ⭐ 326 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,844 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 76 • 💬 3 • ⭐ 182 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 37 • 💬 2 • ⭐ 31,910 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 4,671 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 22,946 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 22,950 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 65.2k • 🔱 9.3k • 9d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 15.0k • 🔱 831 • 4d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 12.8k • 🔱 1.1k • 39m ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.4k • 🔱 1.3k • 16h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.4k • 🔱 975 • 5d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.6k • 🔱 375 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.0k • 🔱 1.5k • 45m ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.5k • 🔱 436 • 3d ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.7k • 🔱 646 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.5k • 🔱 229 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
