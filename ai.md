---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-06T18:06:20.152960+00:00'
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

**Last Updated:** February 06, 2026 at 18:06 UTC  
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

**[Chinese teams keep shipping Western AI tools faster than Western companies do](https://www.reddit.com/r/artificial/comments/1qxgvtr/chinese_teams_keep_shipping_western_ai_tools/)**

It happened again. A 13-person team in Shenzhen just shipped a browser-based version of Claude Code. No terminal, no setup, runs in a sandbox. Anthropic built Claude Code but hasn't shipped anything like this themselves. This is the same pattern as Manus. Chinese company takes a powerful Western AI tool, strips the friction, and ships it to a mainstream audience before the original builders get around to it. US labs keep building the most powerful models in the world. Chinese teams keep building the products that actually put them in people's hands. OpenAI builds GPT, China ships the wrappers. Anthropic builds Claude Code, a Shenzhen startup makes it work in a browser tab. US builds the engines. China builds the cars. Is this just how it's going to be, or are Western AI companies eventually going to care about distribution as much as they care about benchmarks?

5h ago

---

**[Anthropic and OpenAI released flagship models 27 minutes apart -- the AI pricing and capability gap is getting weird](https://www.reddit.com/r/artificial/comments/1qxdz7q/anthropic_and_openai_released_flagship_models_27/)**

Anthropic shipped Opus 4.6 and OpenAI shipped GPT-5.3-Codex on the same day, 27 minutes apart. Both claim benchmark leads. Both are right -- just on different benchmarks. Where each model leads Opus 4.6 tops reasoning tasks: Humanity's Last Exam (53.1%), GDPval-AA (144 Elo ahead of GPT-5.2), BrowseComp (84.0%). GPT-5.3-Codex takes coding: Terminal-Bench 2.0 at 75.1% vs Opus 4.6's 69.9%. The pricing spread is hard to ignore Model Input/M Output/M Gemini 3 Pro $2 $12.00 GPT-5.2 $1.75 $14.00 Opus 4.6 $5.00 $25.00 MiMo V2 Flash $0.10 $0.30 Opus 4.6 costs 2x Gemini on input. Open-source alternatives cost 50x less. At some point the benchmark gap has to justify the price gap -- and for many tasks it doesn't. 1M context is becoming table stakes Opus 4.6 adds 1M tokens (beta, 2x pricing past 200K). Gemini already offers 1M at standard pricing. The real differentiator is retrieval quality at that scale -- Opus 4.6 scores 76% on MRCR v2 (8-needle, 1M), which is the strongest result so far. Market reaction was immediate Thomson Reuters stock fell 15.83%, LegalZoom dropped nearly 20%. Frontier model launches are now moving SaaS valuations in real time. The tradeoff nobody expected Opus 4.6 gets writing quality complaints from early users. The theory: RL optimizations for reasoning degraded prose output. Models are getting better at some things by getting worse at others. No single model wins across the board anymore. The frontier is fragmenting by task type. Source with full benchmarks and analysis: Claude Opus 4.6: 1M Context, Agent Teams, Adaptive Thinking, and a Showdown with GPT-5.3

7h ago

---

**[‘In the end, you feel blank’: India’s female workers watching hours of abusive content to train AI](https://www.reddit.com/r/artificial/comments/1qwhthi/in_the_end_you_feel_blank_indias_female_workers/)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

🔗 [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai) • 1d ago

---

**[How do you actually use AI in your daily writing workflow?](https://www.reddit.com/r/artificial/comments/1qxfdcb/how_do_you_actually_use_ai_in_your_daily_writing/)**

Been using ChatGPT for about 24 months now and I'm curious how others integrate it into their work. My current process: Brainstorm ideas with AI Write the first draft myself Use AI to help restructure or expand sections Edit everything manually at the end I've noticed that keeping my own voice in the mix makes a huge difference - the output feels way more natural than just prompting and copying. What's your workflow? Do you use it more for ideation or actual writing? Also curious if anyone's tried other tools alongside ChatGPT - I've been testing a few like aitextools for checking how my writing comes across, but always looking for new suggestions.

6h ago

---

**[An experiment tested whether AI can pass human identity verification systems](https://www.reddit.com/r/artificial/comments/1qx9pws/an_experiment_tested_whether_ai_can_pass_human/)**

I found this experiment interesting because it doesn’t frame AI as “breaking” a system. Instead, it treats AI as a new kind of participant interacting with infrastructure that was built around human assumptions consistency, behavior, timing, and intent. What stood out to me is that many identity systems aren’t verifying who someone is so much as how human they appear over time. That feels increasingly fragile when the actor on the other side isn’t human at all. This doesn’t feel like a single vulnerability. It feels like a design mismatch. Curious how people here think identity and verification should evolve in an AI-native world better detection, new primitives, or abandoning certain assumptions entirely.

🔗 [mpost.io](https://mpost.io/humanity-protocol-experiment-reveals-how-ai-can-bypass-kyc-and-exploit-digital-trust/) • 12h ago

---

**[“unsanctionobility” 🔥🔥🔥 the bird is the word FUCK ICE, ONE LOVE. unsanctionobility.carrd.co](https://www.reddit.com/r/artificial/comments/1qxf7i9/unsanctionobility_the_bird_is_the_word_fuck_ice/)**

Here & NOW!!

6h ago

---

**[Early user test of a persistent AI narrative system with kids — some unexpected engagement patterns](https://www.reddit.com/r/artificial/comments/1qwo82n/early_user_test_of_a_persistent_ai_narrative/)**

I ran a small real-world test today with two kids (ages 8 and 11) using a long-running AI story world I’ve been experimenting with. Instead of one-shot story generation, the system maintains a persistent world state where choices carry over and shape future events. I let them pick the setting — they chose a Minecraft × Harry Potter mashup where they play wizards trying to defeat the Ender Dragon. One thing that made a huge difference: I used their real names as the characters, and the story started in their actual school. The engine generated story text and illustrations each round. They made all the choices. After about 10 rounds, they were constantly laughing, debating which option to pick, and building on each other’s ideas. It felt much more like co-creating a world than listening to a story. When I told them it was bedtime, they didn’t want to stop. They kept asking what would happen next. A few observations that surprised me: Personalization seemed to matter more than anything else. Once it became their world, emotional investment was instant. Although I designed it as a single-player experience, co-play emerged naturally. The shared decision-making and social dynamic massively increased engagement. Both ages stayed fully engaged the whole time. I expected the younger one to drop off sooner, but the persistent world kept them both hooked. One issue I noticed: my “re-immersion” mechanic (an in-world character emotionally reconnecting players after breaks instead of a dry recap) triggered too frequently between consecutive rounds. The repetition was noticeable. This looks like a simple trigger tuning problem (should probably only fire after longer gaps). What I haven’t tested yet: – Whether kids can reconnect naturally after a real multi-hour break – Whether they can retell the story in a coherent way – Whether they’ll come back unprompted the next day The earlier stress tests showed that constraint mechanisms help keep long-running narratives technically coherent. What this small user test suggests is that coherence itself isn’t what kids consciously care about — but it seems to be the infrastructure that makes personalization, consequence, and agency feel real. Curious if others working on long-horizon agents, narrative systems, or co-creative AI have seen similar effects around personalization and persistence.

1d ago

---

**[The 18-month gap between frontier and open-source AI models has shrunk to 6 months - what this means](https://www.reddit.com/r/artificial/comments/1qvs8q6/the_18month_gap_between_frontier_and_opensource/)**

Ran a real-world test this week: Gemma 3 12B vs paid frontier models across actual business workflows. The honest assessment? 90% of tasks: no meaningful difference. 5%: frontier models worth it (pay-per-use). 5%: neither quite there yet. This matches the data - open models are catching up fast. The article explores: - Why the "gasoline doesn't matter" - only if it powers your task - The shift from "one model to rule them all" to specialized local models - Why even AGI will eventually be open-sourced (historical precedent) - The water company future: infrastructure > model quality https://www.linkedin.com/posts/azizme_activity-7424774668034842624-v1-2?utm_source=share&utm_medium=member_desktop&rcm=ACoAACX_HOcBcpTEWJ3cXyVbVqKJsi39tDHJLFY Curious what others are seeing in their domains.

2d ago

---

**[Alibaba releases Qwen3-Coder-Next to rival OpenAI, Anthropic](https://www.reddit.com/r/artificial/comments/1qvn7o5/alibaba_releases_qwen3codernext_to_rival_openai/)**

🔗 [marktechpost.com](https://www.marktechpost.com/2026/02/03/qwen-team-releases-qwen3-coder-next-an-open-weight-language-model-designed-specifically-for-coding-agents-and-local-development/) • 2d ago

---

**[Simple Machine Learning Testing Tools Guide](https://www.reddit.com/r/artificial/comments/1qwbjhx/simple_machine_learning_testing_tools_guide/)**

🔗 [aivolut.com](https://aivolut.com/blog/simple-machine-learning-testing-tools-guide/) • 1d ago

---

---

## Google News: "ai"

**[Amazon plunges 9%, continues Big Tech's $1 trillion wipeout as AI bubble fears ignite sell-off](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)**

Fears over AI spending have sparked a sell-off among tech stocks.

CNBC • 5h ago

---

**[Amazon’s $200 Billion Spending Plan Raises Stakes in A.I. Race](https://www.nytimes.com/2026/02/05/technology/amazon-200-billion-ai.html)**

The New York Times • 18h ago

---

**[The AI investment surge is getting even bigger](https://www.axios.com/2026/02/06/amazon-microsoft-meta-ai-investment)**

Alphabet, Amazon, Meta and Microsoft are together anticipating capital spending of around $650 billion this year.

Axios • 58m ago

---

**[The AI that spooked the stock market just got a big update](https://www.cnn.com/2026/02/05/tech/anthropic-opus-update-software-stocks)**

Anthropic’s Cowork AI assistant sent shockwaves through Wall Street this week over concerns it could replace specialized software packages, such as for legal or financial analysis. Now Anthropic is improving the model behind that tool to make it better for office and coding work.

cnn.com • 1d ago

---

**[AI fears pummel software stocks: Is it 'illogical' panic or a SaaS apocalypse?](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html)**

The software space is facing serious market concerns this week, after the release of new AI tools from AI triggered a market sell-off.

CNBC • 13h ago

---

**[Why a new AI tool hammered some software stocks this week](https://abcnews.go.com/Business/new-ai-tool-hammered-software-stocks-week/story?id=129845251)**

The new tool adapts a workplace assistant for white-collar specific industries.

ABC News • 20h ago

---

**[Hedge Funds Hit by Worst Day in Months Amid AI-Fueled Rotation](https://www.bloomberg.com/news/articles/2026-02-06/ai-driven-rotation-deals-stock-hedge-funds-worst-day-in-months)**

Bloomberg • 1h ago

---

**[After streak of suicides by teen AI chatbot users, Oregon bill aims to restrict what chatbots can say or do](https://www.oregonlive.com/living/2026/02/after-streak-of-suicides-by-teen-ai-chatbot-users-oregon-bill-aims-to-restrict-what-chatbots-can-say-or-do.html)**

The bill also would require the chatbots to remind people using them that the bots are not a real person.

OregonLive.com • 1h ago

---

**[One of California’s first labor fights over AI is playing out at Kaiser](https://www.latimes.com/business/story/2026-02-06/kaiser-workers-launch-war-against-ai-protesting-potential-job-losses-patient-harm)**

From anxiety about job loss to data privacy, mental health workers, lawmakers and labor unions are trying to mitigate AI's risks as healthcare providers double down on the technology.

latimes.com • 7h ago

---

**[Tesla is training its AI technology in China, local media reports](https://www.reuters.com/technology/tesla-is-training-its-ai-technology-china-local-media-reports-2026-02-06/)**

Reuters • 6h ago

---

---

## HackerNews: "ai"

**[My AI Adoption Journey](https://news.ycombinator.com/item?id=46903558)**

⬆️ 781 • 💬 309 • 23h ago • [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

---

**[AI is killing B2B SaaS](https://news.ycombinator.com/item?id=46888441)**

SaaS is the most profitable business model on Earth.1 It’s easy to understand why: build once, sell the same thing again ad infinitum, and don’t suffer any marginal costs on more sales. I have been writing software for more than half my life. In the last year itself, I’ve talked to hundreds of founders and operators in SF, from preseed to Series E companies. AI is bringing an existential threat to a lot of B2B SaaS executives: How to keep asking customers for renewal, when every customer feels they can get something better built with vibe-coded AI products? And the market is pricing it in. Morgan Stanley’s SaaS basket has lagged the Nasdaq by 40 points since December. HubSpot and Klaviyo are down ~30%. Analysts are writing notes titled “No Reasons to Own” software stocks. The market is reflecting our new reality (Source: Bloomberg) Whenever I bring a new friend to the Salesforce Park, they are in absolute awe. And, the meme remains true that no one even knows what Salesforce does. Whatever they’re doing, they’re clearly earning enough revenue to purchase multiple blocks in SF. ↩

⬆️ 497 • 💬 725 • 2d ago • [N’s Blog](https://nmn.gl/blog/ai-killing-b2b-saas)

---

**[A new bill in New York would require disclaimers on AI-generated news content](https://news.ycombinator.com/item?id=46910963)**

A new bill in the New York state legislature would require news organizations to label AI-generated material and mandate that humans review any such content before publication. On Monday, Senator Patricia Fahy (D-Albany) and Assemblymember Nily Rozic (D-NYC) introduced the bill, called The New York…

⬆️ 363 • 💬 135 • 8h ago • [Nieman Lab](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

---

**[Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering](https://news.ycombinator.com/item?id=46882389)**

Production-grade Ghidra MCP Server — 132 endpoints, cross-binary documentation transfer, batch analysis, headless mode, and Docker deployment for AI-powered reverse engineering - bethington/ghidra-mcp

⬆️ 293 • 💬 66 • 2d ago • [GitHub](https://github.com/bethington/ghidra-mcp)

---

**[China Moon Mission: Aiming for 2030 lunar landing](https://news.ycombinator.com/item?id=46876047)**

China's space program is quietly building momentum for a moon landing by 2030. Could they outpace NASA's Artemis mission?

⬆️ 161 • 💬 172 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/china-moon-mission-mengzhou-artemis)

---

**[Sandboxing AI Agents in Linux](https://news.ycombinator.com/item?id=46874139)**

Like many developers, I find myself more and more using AI agents to help with software development.  I currently use Claude Code, the co...

⬆️ 118 • 💬 67 • 3d ago • [Senko Rašić](https://blog.senko.net/sandboxing-ai-agents-in-linux)

---

**[AI and Trust (2023)](https://news.ycombinator.com/item?id=46877075)**

⬆️ 97 • 💬 20 • 2d ago • [schneier.com](https://www.schneier.com/blog/archives/2023/12/ai-and-trust.html)

---

**[Sam Altman responds to Anthropic's "Ads are coming to AI. But not to Claude" ads](https://news.ycombinator.com/item?id=46894151)**

⬆️ 88 • 💬 107 • 1d ago • [X (formerly Twitter)](https://twitter.com/sama/status/2019139174339928189)

---

**[Anthropic AI tool sparks selloff from software to broader market](https://news.ycombinator.com/item?id=46876720)**

⬆️ 86 • 💬 72 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-02-03/legal-software-stocks-plunge-as-anthropic-releases-new-ai-tool)

---

**[India's female workers watching hours of abusive content to train AI](https://news.ycombinator.com/item?id=46906590)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

⬆️ 83 • 💬 132 • 19h ago • [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai)

---

---

## YouTube Videos: "ai"

**[‘DISGUSTING’: Trump’s AI Video Of Obamas As Monkeys Kicks Off Storm; Dems Seethe At ‘RACISM’](https://www.youtube.com/watch?v=MyvdajZTrkw)**

A massive political storm has erupted after Donald Trump shared an Artificial Intelligence (AI)-generated video showing former ...

📺 Times Of India

👁️ 37K • 👍 280 • 💬 432 • ⏱️ 8:22 • 4h ago

---

**[YouTuber Arrested for Fake AI Videos](https://www.youtube.com/watch?v=rqDv5ETfsQg)**

A YouTuber has been arrested for posting fake AI generated videos. AI slop, deepfakes, and synthetic content have been taking ...

📺 Deep Humor

👁️ 10K • 👍 1K • 💬 211 • ⏱️ 8:40 • 21h ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 130K • 👍 3K • 💬 621 • ⏱️ 13:31 • 1d ago

---

**[The White Collar AI APOCALYPSE Is HERE](https://www.youtube.com/watch?v=ur295T83Wg4)**

Krystal and Saagar discuss tech stocks tumbling amid emerging new fears of job loss and AI. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 303K • 👍 8K • 💬 2K • ⏱️ 24:33 • 1d ago

---

**[American people are &#39;BEING LIED TO&#39; about AI — Palantir&#39;s CTO explains why](https://www.youtube.com/watch?v=WEiWObNw6ho)**

Palantir CTO Shyam Sankar explains how Americans can leverage the use of AI, how the company helps the military and the ...

📺 Fox Business

👁️ 37K • 👍 641 • 💬 208 • ⏱️ 4:22 • 1d ago

---

**[President Trump talks job losses to A.I. and U.S. operation in Venezuela in exclusive interview](https://www.youtube.com/watch?v=J8UxjCRZQpo)**

NBC Nightly News anchor Tom Llamas spoke to President Trump about fears of job losses from A.I. President Trump also ...

📺 NBC News

👁️ 9K • 👍 70 • 💬 27 • ⏱️ 4:39 • 17h ago

---

**[TRILLION-DOLLAR WIPEOUT: Investors dump software stocks as AI fears erupt](https://www.youtube.com/watch?v=llrkhezWNKY)**

Dominari Securities CEO Kyle Wool and Strategic Wealth Partners CEO Mark Tepper analyze the worsening software stock ...

📺 Fox Business Clips

👁️ 100K • 👍 1K • 💬 2K • ⏱️ 6:34 • 1d ago

---

**[Why Replacing Developers with AI is Going Horribly Wrong](https://www.youtube.com/watch?v=WfjGZCuxl-U)**

jobmarket #ai #tech In 2026, the promise of AI replacing 80% of developers has collapsed into a $61 billion technical debt crisis ...

📺 Mackard

👁️ 1.0M • 👍 27K • 💬 3K • ⏱️ 8:12 • 3d ago

---

**[NEW Claude AI Plugins Update Changed The World 🤯](https://www.youtube.com/watch?v=hNMlUu-SFq8)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 7K • 👍 83 • 💬 11 • ⏱️ 15:41 • 18h ago

---

**[We Gave AI Free Will. It Created a Religion](https://www.youtube.com/watch?v=brkEdjzWTXk)**

What happens when you leave AI agents alone in a simulation and let them talk to each other for days? We thought they would ...

📺 Elijah Zielke

👁️ 5K • 👍 145 • 💬 43 • ⏱️ 19:25 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling at table recognition, formula extraction, and information extraction across diverse layouts. It offers state-of-the-art performance with efficient inference, supporting deployment via vLLM, SGLang, and Ollama for real-world business applications.

`image-to-text`

⬇️ 149,223 • ❤️ 724 • 3d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text` `170.7B`

⬇️ 274,182 • ❤️ 1,773 • 1d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is an 80B parameter (3B active) LLM optimized for coding agents, featuring advanced agentic capabilities like long-horizon reasoning and tool usage. It boasts a 256k context length for seamless IDE integration and efficient local development.

`text-generation` `79.7B`

⬇️ 34,937 • ❤️ 509 • 3d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 10,864 • ❤️ 480 • 7h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 50,832 • ❤️ 467 • 5d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and full-duplex live streaming, rivaling proprietary models like GPT-4o and Gemini 2.5 Flash. It offers advanced OCR, bilingual real-time conversation with voice cloning, and proactive omnimodal interaction for fluid, real-time experiences.

`any-to-any` `9.4B`

⬇️ 2,389 • ❤️ 523 • 1h ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio music generation model capable of producing commercial-ready music with precise stylistic control and editing features. It utilizes a hybrid LM-DiT architecture trained on licensed and royalty-free data, offering extreme speed and low VRAM requirements for consumer hardware, making it ideal for music artists and content creators.

`text-to-audio`

⬇️ 16,173 • ❤️ 401 • 3d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a 4B-parameter, multilingual speech-to-text model offering near-offline accuracy with <500ms latency. It features a streaming architecture for real-time applications like voice assistants and live subtitling, optimized for on-device deployment.

⬇️ 1,484 • ❤️ 335 • 1d ago

---

**[Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)**

*Qwen*

Qwen3-ASR-1.7B is a state-of-the-art automatic speech recognition model supporting 52 languages and dialects, offering high-quality, fast, and robust transcription for speech, singing, and songs with background music, with capabilities for streaming inference and timestamp prediction.

`automatic-speech-recognition` `2.3B`

⬇️ 132,239 • ❤️ 394 • 7d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time, full-duplex speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 172,413 • ❤️ 1,678 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 124 • 💬 12 • ⭐ 2,145 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,368 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,121 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,368 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 2 • 💬 0 • ⭐ 30,398 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 117 • 💬 2 • ⭐ 2,586 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 60 • 💬 1 • ⭐ 7,006 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 27,946 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 113 • 💬 7 • ⭐ 70,296 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,248 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 12.9k • 🔱 739 • 1d ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.1k • 🔱 536 • 23h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.7k • 🔱 10.2k • 4h ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 7.6k • 🔱 1.6k • 9h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.1k • 🔱 693 • 2d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.1k • 🔱 346 • 14d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 3.9k • 🔱 315 • 2d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 377 • 14d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.7k • 🔱 256 • 18d ago

---

**[Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor)**

An app to monitor the (Codex) situation

`TypeScript` `ai` `codex` `linux` `macos` `tauri-app`

⭐ 2.2k • 🔱 196 • 59m ago

---

---

*Generated by PeekDeck - A glance is all you need*
