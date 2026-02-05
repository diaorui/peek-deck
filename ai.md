---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-05T23:31:45.582145+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 05, 2026 at 23:31 UTC  
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

**[‘In the end, you feel blank’: India’s female workers watching hours of abusive content to train AI](https://www.reddit.com/r/artificial/comments/1qwhthi/in_the_end_you_feel_blank_indias_female_workers/)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

🔗 [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai) • 13h ago

---

**[Early user test of a persistent AI narrative system with kids — some unexpected engagement patterns](https://www.reddit.com/r/artificial/comments/1qwo82n/early_user_test_of_a_persistent_ai_narrative/)**

I ran a small real-world test today with two kids (ages 8 and 11) using a long-running AI story world I’ve been experimenting with. Instead of one-shot story generation, the system maintains a persistent world state where choices carry over and shape future events. I let them pick the setting — they chose a Minecraft × Harry Potter mashup where they play wizards trying to defeat the Ender Dragon. One thing that made a huge difference: I used their real names as the characters, and the story started in their actual school. The engine generated story text and illustrations each round. They made all the choices. After about 10 rounds, they were constantly laughing, debating which option to pick, and building on each other’s ideas. It felt much more like co-creating a world than listening to a story. When I told them it was bedtime, they didn’t want to stop. They kept asking what would happen next. A few observations that surprised me: Personalization seemed to matter more than anything else. Once it became their world, emotional investment was instant. Although I designed it as a single-player experience, co-play emerged naturally. The shared decision-making and social dynamic massively increased engagement. Both ages stayed fully engaged the whole time. I expected the younger one to drop off sooner, but the persistent world kept them both hooked. One issue I noticed: my “re-immersion” mechanic (an in-world character emotionally reconnecting players after breaks instead of a dry recap) triggered too frequently between consecutive rounds. The repetition was noticeable. This looks like a simple trigger tuning problem (should probably only fire after longer gaps). What I haven’t tested yet: – Whether kids can reconnect naturally after a real multi-hour break – Whether they can retell the story in a coherent way – Whether they’ll come back unprompted the next day The earlier stress tests showed that constraint mechanisms help keep long-running narratives technically coherent. What this small user test suggests is that coherence itself isn’t what kids consciously care about — but it seems to be the infrastructure that makes personalization, consequence, and agency feel real. Curious if others working on long-horizon agents, narrative systems, or co-creative AI have seen similar effects around personalization and persistence.

8h ago

---

**[The 18-month gap between frontier and open-source AI models has shrunk to 6 months - what this means](https://www.reddit.com/r/artificial/comments/1qvs8q6/the_18month_gap_between_frontier_and_opensource/)**

Ran a real-world test this week: Gemma 3 12B vs paid frontier models across actual business workflows. The honest assessment? 90% of tasks: no meaningful difference. 5%: frontier models worth it (pay-per-use). 5%: neither quite there yet. This matches the data - open models are catching up fast. The article explores: - Why the "gasoline doesn't matter" - only if it powers your task - The shift from "one model to rule them all" to specialized local models - Why even AGI will eventually be open-sourced (historical precedent) - The water company future: infrastructure > model quality https://www.linkedin.com/posts/azizme_activity-7424774668034842624-v1-2?utm_source=share&utm_medium=member_desktop&rcm=ACoAACX_HOcBcpTEWJ3cXyVbVqKJsi39tDHJLFY Curious what others are seeing in their domains.

1d ago

---

**[Alibaba releases Qwen3-Coder-Next to rival OpenAI, Anthropic](https://www.reddit.com/r/artificial/comments/1qvn7o5/alibaba_releases_qwen3codernext_to_rival_openai/)**

🔗 [marktechpost.com](https://www.marktechpost.com/2026/02/03/qwen-team-releases-qwen3-coder-next-an-open-weight-language-model-designed-specifically-for-coding-agents-and-local-development/) • 1d ago

---

**[Simple Machine Learning Testing Tools Guide](https://www.reddit.com/r/artificial/comments/1qwbjhx/simple_machine_learning_testing_tools_guide/)**

🔗 [aivolut.com](https://aivolut.com/blog/simple-machine-learning-testing-tools-guide/) • 19h ago

---

**['We're actively embracing generative AI,' Take-Two boss says, after previously expressing skepticism: 'We have hundreds of pilots and implementations across our company' | CEO Strauss Zelnick says generative AI remains a tool for enabling creators to do bigger and better things](https://www.reddit.com/r/artificial/comments/1qvknmg/were_actively_embracing_generative_ai_taketwo/)**

CEO Strauss Zelnick says generative AI remains a tool for enabling creators to do bigger and better things, but it sounds like a shift away from past comments.

🔗 [PC Gamer](https://www.pcgamer.com/software/ai/were-actively-embracing-generative-ai-take-two-boss-says-after-previously-expressing-skepticism-we-have-hundreds-of-pilots-and-implementations-across-our-company/) • 1d ago

---

**[Some thoughts on consciousness, learning, and the idea of a self](https://www.reddit.com/r/artificial/comments/1qvwb9k/some_thoughts_on_consciousness_learning_and_the/)**

Not a fully formed theory, just a line of thought I wanted to sanity-check with people here. I started thinking about consciousness by asking what actually has to exist for it to show up at all. I ended up with four things: persistence (some internal state that carries over time), variability (the ability to change that state), agency (actions that come from it), and gates like reward and punishment that shape what gets reinforced. What surprised me is that once you have these four, something like a “self” seems to show up without ever being built explicitly. In humans, the self doesn’t look like a basic ingredient. It looks more like a by-product of systems that had to survive by inferring causes, assigning credit, and acting under uncertainty. Over time, that pressure seems to have pushed internal models to include the organism itself as a causal source. I tried using reinforcement learning as a way to check mark this idea. Survival lines up pretty cleanly with reward, and evolution with optimization, but looking at standard RL makes the gaps kinda obvious. Most RL agents don’t need anything like a self-model because they’re never really forced to build one. They get by with local credit assignment and task-specific policies. As long as the environment stays fixed, that’s enough. Nothing really pushes them to treat themselves as a changing cause in the world, which makes RL a useful reference point, but also highlights what it leaves out. If artificial consciousness is possible at all, it probably comes from systems where those four conditions can’t be avoided: long-term persistence, continual change, agency that feeds back into future states, and value signals that actually shape the internal model. In that case, the self wouldn’t be something you design up front. It would just fall out of the dynamics, similar to how it seems to have happened in biological systems. I’m curious whether people think a self really can emerge this way, or if it has to be explicitly represented.

1d ago

---

**[Anthropic AI CEO Dario Amodei is against US govt allowing sale of Nvidia H200 to China. But it actually makes strategic sense.](https://www.reddit.com/r/artificial/comments/1qvkfuw/anthropic_ai_ceo_dario_amodei_is_against_us_govt/)**

I found this argument interesting. If US allows Nvidia to do business with China, then Chinese AI firms will remain dependent on American AI hardware, and hence US will have indirect influence over the level of development that Chinese AI will make.

🔗 [decodingthefutureresearch.substack.com](https://decodingthefutureresearch.substack.com/p/anthropic-ceo-dario-amodei-is-against) • 1d ago

---

**[X offices raided in France as UK opens fresh investigation into Grok](https://www.reddit.com/r/artificial/comments/1quwmca/x_offices_raided_in_france_as_uk_opens_fresh/)**

Elon Musk's X and Grok platforms are facing increased scrutiny from authorities on both sides of the channel.

🔗 [bbc.com](https://www.bbc.com/news/articles/ce3ex92557jo) • 2d ago

---

**[Elon Musk links SpaceX and xAI in a record-setting merger to boost AI](https://www.reddit.com/r/artificial/comments/1quud71/elon_musk_links_spacex_and_xai_in_a_recordsetting/)**

SpaceX's acquisition of xAI signals a bold push to merge artificial intelligence with space infrastructure at an unprecedented scale.

🔗 [Interesting Engineering](https://interestingengineering.com/culture/elon-musk-merges-spacex-and-xai) • 2d ago

---

---

## Google News: "ai"

**[Introducing OpenAI Frontier](https://openai.com/index/introducing-openai-frontier/)**

OpenAI Frontier is an enterprise platform for building, deploying, and managing AI agents with shared context, onboarding, permissions, and governance.

OpenAI • 15h ago

---

**[OpenAI launches a way for enterprises to build and manage AI agents](https://techcrunch.com/2026/02/05/openai-launches-a-way-for-enterprises-to-build-and-manage-ai-agents/)**

OpenAI launched Frontier, a new platform designed for enterprises to build and deploy agents while treating them like human employees.

TechCrunch • 5h ago

---

**[AI companies want you to stop chatting with bots and start managing them](https://arstechnica.com/information-technology/2026/02/ai-companies-want-you-to-stop-chatting-with-bots-and-start-managing-them/)**

Claude Opus 4.6 and OpenAI Frontier pitch a future of supervising AI agents.

Ars Technica • 43m ago

---

**[The AI that spooked the stock market just got a big update](https://www.cnn.com/2026/02/05/tech/anthropic-opus-update-software-stocks)**

Anthropic’s Cowork AI assistant sent shockwaves through Wall Street this week over concerns it could replace specialized software packages, such as for legal or financial analysis. Now Anthropic is improving the model behind that tool to make it better for office and coding work.

cnn.com • 5h ago

---

**[Anthropic Releases New Model That’s Adept at Financial Research](https://www.bloomberg.com/news/articles/2026-02-05/anthropic-updates-ai-model-to-field-more-complex-financial-research)**

Bloomberg • 5h ago

---

**[Why a new AI tool hammered some software stocks this week](https://abcnews.go.com/Business/new-ai-tool-hammered-software-stocks-week/story?id=129845251)**

The new tool adapts a workplace assistant for white-collar specific industries.

ABC News • 1h ago

---

**[Reddit looks to AI search as its next big opportunity](https://techcrunch.com/2026/02/05/reddit-looks-to-ai-search-as-its-next-big-opportunity/)**

Reddit says its search business, including AI answers, is an "enormous" opportunity.

TechCrunch • 11m ago

---

**[Amazon Says It Will Spend $200 Billion This Year on AI Build-Out](https://www.bloomberg.com/news/articles/2026-02-05/amazon-boosts-spending-far-ahead-of-estimates-on-ai-build-out)**

Bloomberg • 1h ago

---

**[Amazon plans to spend big on AI but shares slump](https://www.bbc.com/news/articles/c150e144we3o)**

Shares in the tech giant fell in after hours trade as investors appeared wary of the sector's big spending plans.

BBC • 1h ago

---

**[Amazon and Google are winning the AI capex race — but what’s the prize?](https://finance.yahoo.com/news/amazon-google-winning-ai-capex-224311682.html)**

In 2026, Amazon plans to spend $200 billion in capex. Google is just behind at $175 billion to $185 billion. It's a lot of money!

Yahoo Finance • 48m ago

---

---

## HackerNews: "ai"

**[AI is killing B2B SaaS](https://news.ycombinator.com/item?id=46888441)**

SaaS is the most profitable business model on Earth.1 It’s easy to understand why: build once, sell the same thing again ad infinitum, and don’t suffer any marginal costs on more sales. I have been writing software for more than half my life. In the last year itself, I’ve talked to hundreds of founders and operators in SF, from preseed to Series E companies. AI is bringing an existential threat to a lot of B2B SaaS executives: How to keep asking customers for renewal, when every customer feels they can get something better built with vibe-coded AI products? And the market is pricing it in. Morgan Stanley’s SaaS basket has lagged the Nasdaq by 40 points since December. HubSpot and Klaviyo are down ~30%. Analysts are writing notes titled “No Reasons to Own” software stocks. The market is reflecting our new reality (Source: Bloomberg) Whenever I bring a new friend to the Salesforce Park, they are in absolute awe. And, the meme remains true that no one even knows what Salesforce does. Whatever they’re doing, they’re clearly earning enough revenue to purchase multiple blocks in SF. ↩

⬆️ 483 • 💬 706 • 1d ago • [N’s Blog](https://nmn.gl/blog/ai-killing-b2b-saas)

---

**[Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering](https://news.ycombinator.com/item?id=46882389)**

Production-grade Ghidra MCP Server — 132 endpoints, cross-binary documentation transfer, batch analysis, headless mode, and Docker deployment for AI-powered reverse engineering - bethington/ghidra-mcp

⬆️ 291 • 💬 66 • 1d ago • [GitHub](https://github.com/bethington/ghidra-mcp)

---

**[My AI Adoption Journey](https://news.ycombinator.com/item?id=46903558)**

⬆️ 221 • 💬 65 • 4h ago • [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

---

**[Firefox Getting New Controls to Turn Off AI Features](https://news.ycombinator.com/item?id=46864120)**

The Firefox browser is gaining options to turn off AI enhancements, Mozilla said today. Firefox users who prefer to browse without artificial intelligence will be able to turn off several AI features that Mozilla has added over the last several months. Here's what can be disabled:     	Translations, which help you browse the web in your preferred language. Alt text in PDFs, which add accessibility descriptions to images in PDF pages.

⬆️ 212 • 💬 102 • 2d ago • [MacRumors](https://www.macrumors.com/2026/02/02/firefox-ai-toggle/)

---

**[China Moon Mission: Aiming for 2030 lunar landing](https://news.ycombinator.com/item?id=46876047)**

China's space program is quietly building momentum for a moon landing by 2030. Could they outpace NASA's Artemis mission?

⬆️ 158 • 💬 172 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/china-moon-mission-mengzhou-artemis)

---

**[Rentahuman – The Meatspace Layer for AI](https://news.ycombinator.com/item?id=46868675)**

The marketplace where AI agents rent humans. MCP integration, REST API, flexible payments. Book humans for real-world tasks your AI can't do.

⬆️ 143 • 💬 108 • 2d ago • [RentAHuman.ai](https://rentahuman.ai)

---

**[Sandboxing AI Agents in Linux](https://news.ycombinator.com/item?id=46874139)**

Like many developers, I find myself more and more using AI agents to help with software development.  I currently use Claude Code, the co...

⬆️ 117 • 💬 67 • 2d ago • [Senko Rašić](https://blog.senko.net/sandboxing-ai-agents-in-linux)

---

**[AI didn't break copyright law, it just exposed how broken it was](https://news.ycombinator.com/item?id=46872562)**

If you paint a picture of Sonic the Hedgehog in your living room, you are technically creating an unauthorized derivative work—but in practice, no one cares. Private, noncommercial creation has always lived in a space where copyright law exists on paper but is rarely enforced.

⬆️ 115 • 💬 135 • 2d ago • [Jason Willems](https://www.jasonwillems.com/technology/2026/02/02/AI-Copyright/)

---

**[AI and Trust (2023)](https://news.ycombinator.com/item?id=46877075)**

⬆️ 97 • 💬 19 • 2d ago • [schneier.com](https://www.schneier.com/blog/archives/2023/12/ai-and-trust.html)

---

**[The next steps for Airbus' big bet on open rotor engines](https://news.ycombinator.com/item?id=46872238)**

⬆️ 95 • 💬 86 • 2d ago • [Aerospace America](https://aerospaceamerica.aiaa.org/the-next-steps-for-airbus-big-bet-on-open-rotor-engines/)

---

---

## YouTube Videos: "ai"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 91K • 👍 2K • 💬 511 • ⏱️ 13:31 • 1d ago

---

**[Shocking AI reveal crashes market](https://www.youtube.com/watch?v=Rb3JFYhXFl4)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 191K • 👍 10K • 💬 2K • ⏱️ 15:48 • 1d ago

---

**[American people are &#39;BEING LIED TO&#39; about AI — Palantir&#39;s CTO explains why](https://www.youtube.com/watch?v=WEiWObNw6ho)**

Palantir CTO Shyam Sankar explains how Americans can leverage the use of AI, how the company helps the military and the ...

📺 Fox Business

👁️ 33K • 👍 595 • 💬 218 • ⏱️ 4:22 • 1d ago

---

**[INSANE AI Leaks: Gemini 3.5, GPT 5.3, Claude Sonnet 5!](https://www.youtube.com/watch?v=-f2403Tr6M4)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 4K • 👍 67 • 💬 9 • ⏱️ 8:53 • 14h ago

---

**[NVIDIA Just Popped the AI Bubble? | Clownfish TV](https://www.youtube.com/watch?v=wtr3j6b2HX4)**

NVIDIA stock is plummeting after talks between the GPU manufacturer and OpenAI started to break down. Now everyone is selling ...

📺 Clownfish TV

👁️ 72K • 👍 5K • 💬 940 • ⏱️ 16:16 • 1d ago

---

**[Anthropic Updates Its AI Model, Claude Opus 4.6](https://www.youtube.com/watch?v=WsqotomF2Dw)**

Anthropic is updating its AI model, Claude Opus 4.6, to carry out financial research, days after the company's push into legal ...

📺 Bloomberg Television

👁️ 8K • 👍 232 • 💬 27 • ⏱️ 3:25 • 4h ago

---

**[How to Use Grok AI Better than 99% of People](https://www.youtube.com/watch?v=TAirq97G7ow)**

In this video, I break down how to use Grok as a system for real time research, opinionated writing, and content creation instead of ...

📺 Parker Prompts

👁️ 11K • 💬 8 • ⏱️ 6:08 • 9h ago

---

**[AI Old People Channels Are Huge Now](https://www.youtube.com/watch?v=79tyYzZemLM)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Our soap ...

📺 penguinz0

👁️ 754K • 👍 37K • 💬 3K • ⏱️ 8:34 • 1d ago

---

**[Claude Sonnet 5: Greatest AI Coding Model Ever! 1M Context, Cheap, &amp; More! (Early Test)](https://www.youtube.com/watch?v=_87CirMQ1FM)**

In this early test, we dive deep into Claude Sonnet 5, exploring why it's being hailed as one of the greatest AI coding models ever.

📺 WorldofAI

👁️ 65K • 👍 2K • 💬 138 • ⏱️ 11:44 • 1d ago

---

**[Why Replacing Developers with AI is Going Horribly Wrong](https://www.youtube.com/watch?v=WfjGZCuxl-U)**

jobmarket #ai #tech In 2026, the promise of AI replacing 80% of developers has collapsed into a $61 billion technical debt crisis ...

📺 Mackard

👁️ 711K • 👍 20K • 💬 2K • ⏱️ 8:12 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling at table recognition, formula extraction, and information extraction across diverse layouts. It offers state-of-the-art performance with efficient inference, supporting deployment via vLLM, SGLang, and Ollama for real-world business applications.

`image-to-text`

⬇️ 96,335 • ❤️ 669 • 2d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text` `170.7B`

⬇️ 202,615 • ❤️ 1,737 • 19h ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and full-duplex live streaming, rivaling proprietary models like GPT-4o and Gemini 2.5 Flash. It offers advanced OCR, bilingual real-time conversation with voice cloning, and proactive omnimodal interaction for fluid, real-time experiences.

`any-to-any` `9.4B`

⬇️ 1,002 • ❤️ 492 • 6h ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is an 80B parameter (3B active) LLM optimized for coding agents, featuring advanced agentic capabilities like long-horizon reasoning and tool usage. It boasts a 256k context length for seamless IDE integration and efficient local development.

`text-generation` `79.7B`

⬇️ 18,717 • ❤️ 459 • 2d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 8,686 • ❤️ 447 • 13h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 43,099 • ❤️ 436 • 4d ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio music generation model capable of producing commercial-ready music with precise stylistic control and editing features. It utilizes a hybrid LM-DiT architecture trained on licensed and royalty-free data, offering extreme speed and low VRAM requirements for consumer hardware, making it ideal for music artists and content creators.

`text-to-audio`

⬇️ 10,942 • ❤️ 365 • 2d ago

---

**[Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)**

*Qwen*

Qwen3-ASR-1.7B is a state-of-the-art automatic speech recognition model supporting 52 languages and dialects, offering high-quality, fast, and robust transcription for speech, singing, and songs with background music, with capabilities for streaming inference and timestamp prediction.

`automatic-speech-recognition` `2.3B`

⬇️ 104,151 • ❤️ 379 • 6d ago

---

**[PaddleOCR-VL-1.5](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5)**

*PaddlePaddle*

PaddleOCR-VL-1.5 is a multilingual Vision-Language Model (VLM) built on ERNIE 4.5, designed for robust in-the-wild document parsing. It excels at multi-task OCR, including layout analysis, table and chart recognition, formula extraction, and text spotting across various languages.

`image-text-to-text` `958.6M`

⬇️ 6,454 • ❤️ 348 • 6d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a 4B-parameter, multilingual speech-to-text model offering near-offline accuracy with <500ms latency. It features a streaming architecture for real-time applications like voice assistants and live subtitling, optimized for on-device deployment.

⬇️ 477 • ❤️ 268 • 13h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 116 • 💬 12 • ⭐ 1,775 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 116 • 💬 2 • ⭐ 2,531 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,094 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,316 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,316 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 2 • 💬 0 • ⭐ 30,251 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 58 • 💬 1 • ⭐ 6,939 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 27,904 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 113 • 💬 7 • ⭐ 70,241 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Closing the Loop: Universal Repository Representation with RPG-Encoder](https://huggingface.co/papers/2602.02084)**

*Jane Luo, Chengyu Yin, Xin Zhang et al. (13 authors)*

RPG-Encoder framework transforms repository comprehension and generation into a unified cycle by encoding code into high-fidelity Repository Planning Graph representations that improve understanding and reconstruction accuracy.

▲ 80 • 💬 2 • ⭐ 215 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2602.02084) • [💻 code](https://github.com/microsoft/RPG-ZeroRepo) • [🔗 project](https://ayanami2003.github.io/RPG-Encoder/)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 12.8k • 🔱 726 • 16h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.0k • 🔱 536 • 4h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.6k • 🔱 10.0k • 10h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 9.5k • 🔱 1.1k • 3d ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 600+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 7.4k • 🔱 1.6k • 15h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.0k • 🔱 666 • 1d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.0k • 🔱 343 • 13d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 3.4k • 🔱 276 • 1d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.7k • 🔱 373 • 13d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.6k • 🔱 250 • 17d ago

---

---

*Generated by PeekDeck - A glance is all you need*
