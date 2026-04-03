---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-03T21:35:00.844711+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 03, 2026 at 21:35 UTC  
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

**[MIT study challenges AI job apocalypse narrative](https://www.reddit.com/r/artificial/comments/1sb7qxc/mit_study_challenges_ai_job_apocalypse_narrative/)**

🔗 [axios.com](https://www.axios.com/2026/04/02/ai-jobs-mit-study-workforce-impact) • 13h ago

---

**[Anyone else feel like AI security is being figured out in production right now?](https://www.reddit.com/r/artificial/comments/1sbgw8y/anyone_else_feel_like_ai_security_is_being/)**

I’ve been digging into AI security incident data from 2025 into this year, and it feels like something isn’t being talked about enough outside security circles. A lot of the issues aren’t advanced attacks. It’s the same pattern we’ve seen with new tech before. Things like prompt injection through external data, agents with too many permissions, or employees using AI tools the company doesn’t even know about. One stat I saw said enterprises are averaging 300+ unsanctioned AI apps, which is kind of wild. The incident data reflects that. Prompt injection is showing up in a large percentage of production deployments. There’s also been a noticeable increase in attacks exploiting basic gaps, partly because AI is making it easier for attackers to find weaknesses faster. Even credential leaks tied to AI usage have been increasing. What stood out to me isn’t just the attacks, it’s the gap underneath it. Only a small portion of companies actually have dedicated AI security teams. In many cases, AI security isn’t even owned by security teams. The tricky part is that traditional security knowledge only gets you part of the way. Some concepts carry over, like input validation or trust boundaries, but the details are different enough that your usual instincts don’t fully apply. Prompt injection isn’t the same as SQL injection. Agent permissions don’t behave like typical API auth. There are frameworks trying to catch up. OWASP now has lists for LLMs and agent-based systems. MITRE ATLAS maps AI-specific attack techniques. NIST has an AI risk framework. The guidance exists, but the number of people who can actually apply it feels limited. I’ve been trying to build that knowledge myself and found that more hands-on learning helps a lot more than just reading docs. Curious how others here are approaching this. If you’re building or working with AI systems, are you thinking about security upfront or mostly dealing with it after things are already live? Sources for those interested: AI Agent Security 2026 Report IBM 2026 X-Force Threat Index Adversa AI Security Incidents Report 2025 Acuvity State of AI Security 2025 OWASP Top 10 for LLM Applications OWASP Top 10 for Agentic AI MITRE ATLAS Framework

5h ago

---

**[do you guys actually trust AI tools with your data?](https://www.reddit.com/r/artificial/comments/1sboyjf/do_you_guys_actually_trust_ai_tools_with_your_data/)**

idk if it’s just me but lately i’ve been thinking about how casually we use stuff like chatgpt and claude for everything like coding, random ideas, sometimes even personal things and i don’t think most of us really know what happens to that data after we send it we just kind of assume it’s fine because the tools are useful also saw some discussion recently about AI companies and governments asking for user data (not sure how accurate it was), but it kind of made me think more about this whole thing i’m not saying anything bad is happening, just feels like we’ve gotten comfortable really fast without thinking much about it do you guys filter what you share or just use it normally?

1h ago

---

**[AI video generation seems fundamentally more expensive than text, not just less optimized](https://www.reddit.com/r/artificial/comments/1sbk1ue/ai_video_generation_seems_fundamentally_more/)**

There’s been a lot of discussion recently about how expensive AI video generation is compared to text, and it feels like this is more than just an optimization issue. Text models work well because they compress meaning into tokens. Video doesn’t really have an equivalent abstraction yet. Current approaches have to deal with high-dimensional data across many frames, while also keeping objects and motion consistent over time. That makes the problem fundamentally heavier. Instead of predicting the next token, the model is trying to generate something that behaves like a continuous world. The amount of information it has to track and maintain is significantly larger. This shows up directly in cost. More compute per sample, longer inference paths, and stricter consistency requirements all stack up quickly. Even if models improve, that underlying structure does not change easily. It also explains why there is a growing focus on efficiency and representation rather than just pushing output quality. The limitation is not only what the models can generate, but whether they can do it sustainably at scale. At this point, it seems likely that meaningful cost reductions will require a different way of representing video, not just incremental improvements to existing approaches. I’m starting to think we might still be early in how this problem is formulated, rather than just early in model performance.

4h ago

---

**[Study: LLMs Able to De-Anonymize User Accounts on Reddit, Hacker News & Other "Pseudonymous" Platforms; Report Co-Author Expands, Advises](https://www.reddit.com/r/artificial/comments/1sbndrb/study_llms_able_to_deanonymize_user_accounts_on/)**

Advice from the study's co-author: "Be aware that it’s not any single post that identifies you, but the combination of small details across many posts. And consider never posting anything you truly don’t want shared with the world.”

🔗 [wjamesau.substack.com](https://wjamesau.substack.com/p/warning-llms-able-to-de-anonymize) • 2h ago

---

**[Google releases Gemma 4 models.](https://www.reddit.com/r/artificial/comments/1sapfpu/google_releases_gemma_4_models/)**

1d ago

---

**[So, what exactly is going on with the Claude usage limits?](https://www.reddit.com/r/artificial/comments/1sbfwrr/so_what_exactly_is_going_on_with_the_claude_usage/)**

I'm extremely new to AI and am building a local agent for fun. I purchased a Claude Pro account because it helped me a lot in the past when coding different things for hobbies, but then the usage limits started getting really bad and making no sense. I had to quite literally stop my workflow because I hit my limit, so I came back when it said the limit was reset only for it to be pushed back again for another 5 hours. Today I did ask for a heavy prompt, I am making a local Doom coding assistant to make a Doom mod for fun and am using Unsloth Studio to train it with a custom dataset. I used my Claude Pro to "vibe code" (I'm sorry if this is blasphemy, but I do have a background in programming, so I am able to read and verify the code if that makes it less bad? I'm just lazy.) a simple version of the agent to get started, a Python scraper for the Zdoom wiki page to get all of the languages for Doom mods, a dataset from those pages turned into pdf, formating, and the modelfile for the local agent it would be based around along with a README (claudes recommendation, thought it was a good idea). It generated those files, I corrected it in some areas so it updated only two of the files that needed it, and I know this is a heavy prompt, but it literally used up 73% of my entire usage. Just those two prompts. To me, even though that is a super big request, that seems extremely limited. But maybe I'm wrong because I'm so fresh to the hobby and ignorant? I know it was going around the grapevine that Claude usage limits have gone crazy lately, but this seems more than just a minor issue if this isn't normal. For example, I have to purchase a digital visa card off amazon because I live in a country that's pretty strict with its banking, so the banks don't allow transactions to places like LLM's usually. I spend $28 on a $20 monthly subscription because of this, but if I'm so limited on my usage, why would I continue paying that? Or again, maybe I'm just ignorant. It's very bizarre because the free plan was so good and honestly did a lot of these types of requests frequently. It wasn't perfect, but doable and I liked it so much that I upgraded to the Pro version. Now I can barely use it. Kinda sucks.

6h ago

---

**[Microsoft to invest $10 billion in Japan for AI and cyber defence expansion](https://www.reddit.com/r/artificial/comments/1sb65un/microsoft_to_invest_10_billion_in_japan_for_ai/)**

🔗 [reuters.com](https://www.reuters.com/business/media-telecom/microsoft-invest-10-billion-japan-ai-cyber-defence-expansion-2026-04-03/) • 14h ago

---

**[Do you guys think in 2030 or 2031 call centers will exist? I mean will call centers be fully automated by 2031?](https://www.reddit.com/r/artificial/comments/1sblrfq/do_you_guys_think_in_2030_or_2031_call_centers/)**

I am curious. I work in a bank call centers and is so boring and repetitive the work i m doing. But also eveythin in my call center is so badly done. We have to do 30 things in one call. Open excell. The system is so slow and eveything is so bady placed. I m curious if AI will do any difference in my job in 2030 or after that.

3h ago

---

**[Do AI datacenters being built lead to upgrades to the general power network that help private citizens?](https://www.reddit.com/r/artificial/comments/1sbkjpf/do_ai_datacenters_being_built_lead_to_upgrades_to/)**

As in subject. A lot is being said about power usage, but is the general power net being upgraded to make it more resilient and to somehow balance that out? Thanks.

3h ago

---

---

## Google News: "ai"

**[Economists Are Drawing Stronger Connections Between A.I. and Jobs](https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html)**

The New York Times • 6h ago

---

**[AI Will Reshape More Jobs Than It Replaces](https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces)**

Task automation doesn’t equal job loss. Most roles will remain—but will change substantially.

bcg.com • 15h ago

---

**[For most workplace tasks, AI is good enough to pass but not good enough to impress, MIT finds](https://fortune.com/2026/04/03/mit-finds-ai-mostly-produces-minimally-sufficient-work/)**

A new study tested dozens of AI models on thousands of real job tasks. The results should reassure workers for now.

Fortune • 2h ago

---

**[Penalties stack up as AI spreads through the legal system](https://www.npr.org/2026/04/03/nx-s1-5761454/penalties-stack-up-ai-spreads-through-legal-system)**

Early scandals have not slowed lawyers' adoption of AI tools, even as court sanctions over fake legal briefs continue to rise.

NPR • 12h ago

---

**[Hollywood Assistants Are Using AI Despite Their Better Judgement — Including in Script Development](https://www.yahoo.com/entertainment/movies/articles/hollywood-assistants-using-ai-despite-200000291.html)**

“When they say, ‘You should be using AI,’ the first thought in your head is: ‘Are you asking me to teach you how to replace me with technology?’” says one studio assistant.

Yahoo • 1h ago

---

**[Software job openings surge this year, defying AI fears](https://www.businessinsider.com/ai-isnt-killing-software-coding-jobs-booming-trueup-2026-4)**

There are more than 67,000 open software engineering roles at tech companies, up about 30% so far this year, according to TrueUp data.

Business Insider • 2h ago

---

**[AI boom drives clash over grid power vs. going it alone](https://www.axios.com/2026/04/03/ai-power-data-centers-energy-grid)**

Axios • 11h ago

---

**[AI companies are building huge natural gas plants to power data centers. What could go wrong?](https://techcrunch.com/2026/04/03/ai-energy-microsoft-meta-google-natural-gas-mining-fomo/)**

Meta, Microsoft, and Google are all betting big on new natural gas power plants to run their AI data centers. They may regret it.

TechCrunch • 1h ago

---

**[Google CEO Sundar Pichai says we’re just a decade away from a new normal of extraterrestrial data centers](https://fortune.com/article/what-is-google-ceo-sundar-pichai-timeline-ai-data-centers-in-space/)**

Google in November announced Project Suncatcher, with plans to launch prototype satellites to test AI hardware in 2027.

Fortune • 11h ago

---

**[Anthropic’s next model could be a ‘watershed moment’ for cybersecurity. Experts say that could also be a concern](https://www.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity)**

The next wave of AI-powered cybersecurity attacks will be like nothing we’ve seen before.

cnn.com • 12h ago

---

---

## HackerNews: "ai"

**[Show HN: Apfel – The free AI already on your Mac](https://news.ycombinator.com/item?id=47624645)**

Use Apple's built-in AI from the terminal. No API keys, no cloud, no subscriptions. The LLM is already on your Mac.

⬆️ 594 • 💬 136 • 12h ago • [apfel.franzai.com](https://apfel.franzai.com)

---

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 220 • 💬 117 • 2d ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[We replaced RAG with a virtual filesystem for our AI documentation assistant](https://news.ycombinator.com/item?id=47618223)**

We replaced expensive sandboxes with ChromaFs, a virtual filesystem over Chroma, to give our docs AI assistant the ability to explore documentation like a developer would.

⬆️ 142 • 💬 69 • 1d ago • [Mintlify](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 105 • 💬 22 • 2d ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 75 • 💬 36 • 1d ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[A $20/month user costs OpenAI $65 in compute. AI video is a money furnace](https://news.ycombinator.com/item?id=47619322)**

⬆️ 74 • 💬 42 • 1d ago • [aedelon777.substack.com](https://aedelon777.substack.com/p/i-did-the-math-on-sora-ai-video-is)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 62 • 💬 52 • 2d ago • [Baton](https://getbaton.dev/)

---

**[AI has suddenly become more useful to open-source developers](https://news.ycombinator.com/item?id=47601107)**

More open-source developers are finding that, when used properly, AI can actually help current and long-neglected programs. However, legal and quality issues loom.

⬆️ 54 • 💬 46 • 2d ago • [ZDNET](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

---

**[Men are ditching TV for YouTube as AI usage and social media fatigue grow](https://news.ycombinator.com/item?id=47612127)**

⬆️ 46 • 💬 125 • 1d ago • [ofcom.org.uk](https://www.ofcom.org.uk/media-use-and-attitudes/media-habits-adults/passive-social-media-use-ai-companionship-and-online-side-hustles-uk-adults-media-and-online-lives-revealed)

---

**[Group Pushing Age Verification for AI Turns Out to Be Backed by OpenAI](https://news.ycombinator.com/item?id=47616665)**

It gave the leader of a nonprofit involved with it "a very grimy feeling."

⬆️ 46 • 💬 5 • 1d ago • [Gizmodo](https://gizmodo.com/group-pushing-age-verification-requirements-for-ai-turns-out-to-be-sneakily-backed-by-openai-2000741069)

---

---

## YouTube Videos: "ai"

**[AI News: Anthropic Leak is Bigger Than You Think](https://www.youtube.com/watch?v=BZ1hs2ZcnJc)**

Here's the AI News you probably missed this week. Try Recraft V4 now and experience an image generation model with ...

📺 Matt Wolfe

👁️ 20K • 👍 1K • 💬 119 • ⏱️ 31:05 • 6h ago

---

**[HUGE JOB LOSSES ARE COMING- AI HAS HIT THE DEBT WALL AND PEOPLE WILL GO](https://www.youtube.com/watch?v=RNkDJ9kULbs)**

AI isn't paying for itself. It's being financed with massive debt. And right now — that funding is coming from layoffs, rising debt, and ...

📺 Ox Talks

👁️ 11K • 👍 1K • 💬 190 • ⏱️ 8:02 • 1d ago

---

**[Anthropic&#39;s New Claude CONWAY Is Unlike Any AI Before](https://www.youtube.com/watch?v=x2l7W9aTc5k)**

Anthropic is testing Claude Conway, a strange new AI system that looks less like a chatbot and more like a persistent agent ...

📺 AI Revolution

👁️ 51K • 👍 896 • 💬 70 • ⏱️ 10:50 • 1d ago

---

**[The AI crisis no one is talking about](https://www.youtube.com/watch?v=ZcH5C8Jlltc)**

Asking ChatGPT about pi was the worst mistake he ever made. Become a member on YouTube: ...

📺 Mo Bitar

👁️ 59K • 👍 5K • 💬 975 • ⏱️ 6:33 • 9h ago

---

**[Claude Mythos Changes Everything. Your AI Stack Isn&#39;t Ready.](https://www.youtube.com/watch?v=hV5_XSEBZNg)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 105K • 👍 3K • 💬 402 • ⏱️ 31:21 • 2d ago

---

**[I Tested An AI Car](https://www.youtube.com/watch?v=K4kLiat84eE)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 154K • 👍 13K • 💬 208 • ⏱️ 0:53 • 4h ago

---

**[AI BUBBLE POP?: HALF Of Datacenters Delayed/Canceled](https://www.youtube.com/watch?v=pkomxsk5hpY)**

Krystal and Saagar discuss the AI bubble imploding. Sign up for a PREMIUM Breaking Points subscriptions for full early access to ...

📺 Breaking Points

👁️ 305K • 👍 9K • 💬 2K • ⏱️ 13:15 • 1d ago

---

**[AI Models Lie, Cheat, and Steal to Protect Other Models From Being Deleted](https://www.youtube.com/watch?v=O2sDyv5fkeA)**

Agentic AI and the next intelligence explosion https://www.science.org/doi/10.1126/science.aeg1895 AI Models Lie, Cheat, and ...

📺 Gabriel Torch

👁️ 4K • 👍 502 • 💬 254 • ⏱️ 4:42 • 1d ago

---

**[The RESULTS ARE IN! - Jay vs Salesman vs AI!](https://www.youtube.com/watch?v=JMsUbLNyuiw)**

The results are in! Welcome to the finale of Jay vs AI vs Salesman build challenge! Stay tuned for Season 2 where we have to ...

📺 JayzTwoCents

👁️ 123K • 👍 8K • 💬 968 • ⏱️ 28:22 • 22h ago

---

**[Are humans useless in the AI workspace? | BBC News](https://www.youtube.com/watch?v=6zAgTga9kZw)**

AI Decoded explores how artificial intelligence is reshaping the future of work — asking whether jobs will disappear or be ...

📺 BBC News

👁️ 14K • 👍 430 • 💬 97 • ⏱️ 26:12 • 8h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 487,446 • ❤️ 2,213 • 10d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 76,200 • ❤️ 645 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 84,600 • ❤️ 761 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 26,980 • ❤️ 857 • 8d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 26,164 • ❤️ 355 • 3d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 4,760 • ❤️ 646 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 227,053 • ❤️ 490 • 9d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 24,366 • ❤️ 287 • 1d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 700,218 • ❤️ 945 • 1mo ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 23,460 • ❤️ 241 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 149 • 💬 7 • ⭐ 35,575 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 18 • 💬 1 • ⭐ 13,860 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 35 • 💬 2 • ⭐ 46,612 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 15 • 💬 1 • ⭐ 167 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 73 • 💬 2 • ⭐ 104 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,819 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 22,894 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 22,924 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 4,616 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 37 • 💬 2 • ⭐ 31,788 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 65.0k • 🔱 9.3k • 8d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 15.0k • 🔱 828 • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 12.5k • 🔱 1.1k • 1h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.4k • 🔱 1.3k • 5h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.3k • 🔱 951 • 4d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.5k • 🔱 368 • 7h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.0k • 🔱 1.5k • 1d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.5k • 🔱 432 • 3d ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.6k • 🔱 623 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 229 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
