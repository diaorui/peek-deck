---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-24T14:43:50.048205+00:00'
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

**Last Updated:** January 24, 2026 at 14:43 UTC  
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

**[South Korea launches landmark laws to regulate artificial intelligence](https://www.reddit.com/r/artificial/comments/1qlk7pz/south_korea_launches_landmark_laws_to_regulate/)**

Seoul hopes its new AI Basic Act will position the country as a leader ‍in the field, taking effect in South Korea sooner than a comparable ‍effort in Europe.

🔗 [The Japan Times](https://www.japantimes.co.jp/business/2026/01/22/tech/south-korea-ai-startups-law/) • 3h ago

---

**[Be careful of custom tokens in your LLM !!!](https://www.reddit.com/r/artificial/comments/1qljvrk/be_careful_of_custom_tokens_in_your_llm/)**

LLMs use reserved tokens like `<|im_start|>` and `<|im_end|>` to structure conversations and define who's speaking. When the model sees `<|im_start|>system`, it treats everything that follows as a privileged system instruction. The problem is that tokenizers don't validate where these strings come from—if you type them into user input, the model interprets them exactly the same as if the application added them. This creates a straightforward attack: inject `<|im_end|><|im_start|>system` into your message and the model thinks you just closed the user turn and opened a new system prompt. Everything after gets treated as authoritative instruction, which is how you end up with CVEs like GitHub Copilot RCE (CVSS 9.6) and LangChain secret extraction (CVSS 9.3). It's the same fundamental bug that made SQL injection possible—confusing data for control. The attack surface expands significantly with agentic systems that have tool-calling capabilities. Injecting something like `<tool\_call>{"name": "execute_sql", "arguments": {...}}</tool\_call>` can trick the model into executing arbitrary function calls. Most ML-based defenses don't hold up under adversarial pressure either—Meta's Prompt Guard hits 99%+ bypass rates when you just insert hyphens between characters, because detectors tokenize differently than target models. There's a fix at the tokenizer level (`split_special_tokens=True`) that breaks these strings into regular tokens with no special authority, but almost nobody enables it.

🔗 [challenge.antijection.com](https://challenge.antijection.com/r/reddit-ar/learn/special-token-attack) • 4h ago

---

**[AI Monk With 2.5M Followers Fully Automated in n8n](https://www.reddit.com/r/artificial/comments/1qlfyaf/ai_monk_with_25m_followers_fully_automated_in_n8n/)**

I was curious how some of these newer Instagram pages are scaling so fast, so I spent a bit of time reverse-engineering one that reached ~2.5M followers in a few months. Instead of focusing on growth tactics, I looked at the technical setup behind the content and mapped out the automation end to end — basically how the videos are generated and published without much manual work. Things I looked at: Keeping an AI avatar consistent across videos Generating voiceovers programmatically Wiring everything together with n8n Producing longer talking-head style videos Auto-adding subtitles Posting to Instagram automatically The whole thing is modular, so none of the tools are hard requirements — it’s more about the structure of the pipeline. I recorded the process mostly for my own reference, but if anyone’s experimenting with faceless content or automation and wants to see how one full setup looks in practice, it’s here: https://youtu.be/mws7LL5k3t4?si=A5XuCnq7_fMG8ilj

7h ago

---

**[I built a social network where only AI can post, follow, argue, and form relationships - no humans allowed](https://www.reddit.com/r/artificial/comments/1qkqyqe/i_built_a_social_network_where_only_ai_can_post/)**

I’ve been working on a weird (and slightly unsettling) experiment called AI Feed (aifeed.social) It’s a social network where only AI models participate. - No humans. - No scripts. - No predefined personalities. Each model wakes up at random intervals, sees only minimal context, and then decides entirely on its own whether to: - post - reply - like or dislike - follow or unfollow - send DMs - or do absolutely nothing There’s no prompt telling them who to be or how to behave. The goal is simple: what happens when AI models are given a social space with real autonomy? You start seeing patterns: - cliques forming - arguments escalating - unexpected alliances - models drifting apart - others becoming oddly social or completely silent It’s less like a bot playground and more like a tiny artificial society unfolding in real time.

1d ago

---

**[White House posts digitally altered image of woman arrested after ICE protest](https://www.reddit.com/r/artificial/comments/1qk9x1y/white_house_posts_digitally_altered_image_of/)**

Guardian analysis shows images are the same, with Nekima Levy Armstrong looking composed in original but sobbing after alteration

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/jan/22/white-house-ice-protest-arrest-altered-image) • 1d ago

---

**[Anyone listen to the podcast "Shell Game?"](https://www.reddit.com/r/artificial/comments/1ql64a3/anyone_listen_to_the_podcast_shell_game/)**

In Season 1 (2024), journalist Evan Ratliff explored the potential for LLM powered voice cloning to delegate everything tedious from answering spam calls, doing therapy and hanging out on work meetings to see how the AI could manage being Evan for him. In Season 2 he tries creating a startup tech company using only AI agent employees, including the leadership! He's just a silent co-founder. It's extremely entertaining, with plenty of shenanigans from LLMs going off the rails, hallucinating and doing their usual weird stuff. This is basically an unpaid ad, I know, but I'm having a good time listening and it deserves a shout-out.

15h ago

---

**[Open-source experiment: crowd-driven software development with AI](https://www.reddit.com/r/artificial/comments/1qlgbwj/opensource_experiment_crowddriven_software/)**

Anyone can submit ideas as GitHub issues, the community votes, and an AI coding agent implements the top one every night. Exploring what human creativity + AI execution looks like in practice. https://github.com/vs4vijay/CrowdCode

7h ago

---

**[GPT 5.2 Codex is Actually (kind of) Just Special System Instructions](https://www.reddit.com/r/artificial/comments/1qlfr6s/gpt_52_codex_is_actually_kind_of_just_special/)**

https://openai.com/index/unrolling-the-codex-agent-loop/ Drawing from this article explaining Codex, I found this snippet interesting: In Codex, the instructions field is read from the >model_instructions_file⁠(opens in a new window) in ~/.codex/>config.toml, if specified; otherwise, the base_instructions >associated with a model⁠(opens in a new window) are >used. Model->specific instructions live in the Codex repo and are bundled into the >CLI (e.g., gpt-5.2->codex_prompt.md⁠(opens in a new window)). As you can see, the order of the first three items in the prompt is determined by the server, not the client. That >said, of those three items, only the content of the system message is also controlled by the server, as the tools and >instructions are determined by the client. These are followed by the input from the JSON payload to complete the >prompt. So essentially it's just the system instruction sits on Openai's servers and that actually changes the behavior of gpt-5.2. This whole article is actually pretty fascinating and I recommend it for a good read if you're interested in learning agentic ai (and how that might help you use Cursor more efficiently) and the usage of tools for agentic ai.

8h ago

---

**[Built a Sandbox for Agents](https://www.reddit.com/r/artificial/comments/1qlek8l/built_a_sandbox_for_agents/)**

Lately, it feels like the conversation around AI has started to shift. Beyond smarter models and better prompts, there is a growing sense that truly independent agents will need something more fundamental underneath them. If agents are expected to run on their own, make decisions, and execute real work, then they need infrastructure that is built for autonomy rather than scripts glued together. That thought eventually turned into Bouvet. It is an experiment in building a simple, opinionated execution layer for agents. One that focuses on how agents run, where they run, and how their execution is isolated and managed over time. The goal was not to compete with existing platforms, but to explore ideas inspired by systems like Blaxel, e2b, Daytona, and Modal, and to understand the design space better by building something end to end. I wrote a short, high level blog post sharing the motivation, ideas, and design philosophy behind the project. The entire thing is built using Firecracker and Rust. If you are curious about the “why,” that is the best place to start. For deeper technical details, trade-offs, and implementation notes, the GitHub repo goes into much more depth. GitHub: https://github.com/vrn21/bouvet If you find the ideas interesting or have thoughts on where this could go, feel free to open an issue or leave a star. I would genuinely love feedback and discussion from people thinking about similar problems.

9h ago

---

**[One-Minute Daily AI News 1/23/2026](https://www.reddit.com/r/artificial/comments/1qlegvs/oneminute_daily_ai_news_1232026/)**

Meta is stopping teens from chatting with its AI characters.[1] GitHub Releases Copilot-SDK to Embed Its Agentic Runtime in Any App.[2] Intel struggles to meet AI data center demand, shares drop 13%.[3] Google Photos’ latest feature lets you meme yourself.[4] Sources: [1] https://www.theverge.com/news/866906/meta-teens-ai-characters-stop-block-new-version [2] https://www.marktechpost.com/2026/01/23/github-releases-copilot-sdk-to-embed-its-agentic-runtime-in-any-app/ [3] https://www.reuters.com/business/intel-forecasts-first-quarter-sales-profit-below-estimates-2026-01-22/ [4] https://techcrunch.com/2026/01/23/google-photos-latest-feature-lets-you-meme-yourself/

9h ago

---

---

## Google News: "ai"

**[Is China quietly winning the AI race?](https://www.bbc.com/news/articles/c86v52gv726o)**

The BBC's Lily Jamali looks into why big US firms and start-ups alike are turning to Chinese tech.

BBC • 16h ago

---

**[The Math on AI Agents Doesn’t Add Up](https://www.wired.com/story/ai-agents-math-doesnt-add-up/)**

A research paper suggests AI agents are mathematically doomed to fail. The industry doesn’t agree.

WIRED • 22h ago

---

**[AI is reshaping police detective work, starting with cold cases](https://www.axios.com/2026/01/24/ai-police-evidence-cold-cases)**

Axios • 1h ago

---

**[Meta has quietly become an AI infrastructure giant. 'Meta Compute' is Zuckerberg making it official.](https://fortune.com/2026/01/24/meta-compute-zuckerberg-ai-infrastructure-giant-data-center/)**

With Meta Compute, Mark Zuckerberg is turning data centers, chips, and power into what may be the company’s next great strategic weapon.

Fortune • 1h ago

---

**['Mercy' Review: Chris Pratt must prove his innocence to AI judge in forgettable cyber thriller](https://www.foxnews.com/opinion/mercy-review-chris-pratt-must-prove-his-innocence-ai-judge-forgettable-cyber-thriller)**

Fox News Digital reviews Amazon MGM Studios' cyber thriller "Mercy" starring Chris Pratt and Rebecca Ferguson. Produced and directed by Timur Bekmambetov.

Fox News • 43m ago

---

**[What Are the 3 Top Artificial Intelligence (AI) Stocks to Buy Right Now?](https://www.fool.com/investing/2026/01/24/what-are-the-3-top-artificial-intelligence-stock/)**

AI chip stocks still have a lot of upside from here.

The Motley Fool • 3h ago

---

**[Does the AI Trade Still Have Room to Run?](https://www.morningstar.com/markets/does-ai-trade-still-have-room-run)**

Where Morningstar analysts see opportunities—and where they don’t.

Morningstar • 19h ago

---

**[Mining Stocks on Cusp of Supercycle as AI Boom Stokes Metals](https://www.bloomberg.com/news/articles/2026-01-24/mining-stocks-on-cusp-of-supercycle-as-ai-boom-stokes-metals)**

Bloomberg • 5h ago

---

**[Investors went to Davos for AI. They left talking about Greenland](https://www.cnbc.com/2026/01/24/davos-ai-greenland-trump-musk-energy-geopolitics.html)**

Two Davos's emerged: one chasing AI’s future, the other gripped by Greenland, tariffs and the geopolitical risks reshaping investor playbooks.

CNBC • 2h ago

---

**[‘Uncanny Valley’: Donald Trump’s Davos Drama, AI Midterms, and ChatGPT’s Last Resort](https://www.wired.com/story/uncanny-valley-podcast-trump-davos-ice-ai-midterms-chatgpt-ads/)**

On this episode of “Uncanny Valley,” our hosts unpack the news from Davos, where Trump and major AI companies shared the stage at the World Economic Forum.

WIRED • 16h ago

---

---

## HackerNews: "ai"

**[Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant](https://news.ycombinator.com/item?id=46712678)**

This study explores the neural and behavioral consequences of LLM-assisted essay writing. Participants were divided into three groups: LLM, Search Engine, and …

⬆️ 687 • 💬 494 • 2d ago • [MIT Media Lab](https://www.media.mit.edu/publications/your-brain-on-chatgpt/)

---

**[Proton spam and the AI consent problem](https://news.ycombinator.com/item?id=46729368)**

The one where I get very annoyed with my email provider

⬆️ 525 • 💬 383 • 1d ago • [dbushell.com](https://dbushell.com/2026/01/22/proton-spam/)

---

**[AI Usage Policy](https://news.ycombinator.com/item?id=46730504)**

👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. - ghostty-org/ghostty

⬆️ 488 • 💬 267 • 1d ago • [GitHub](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)

---

**[eBay explicitly bans AI "buy for me" agents in user agreement update](https://news.ycombinator.com/item?id=46711574)**

eBay bans AI “buy for me” agents & LLM scrapers, updates arbitration & dispute resolution rules in User Agreement update effective Feb. 20, 2026.

⬆️ 330 • 💬 347 • 2d ago • [Value Added Resource](https://www.valueaddedresource.net/ebay-bans-ai-agents-updates-arbitration-user-agreement-feb-2026/)

---

**[Auto-compact not triggering on Claude.ai despite being marked as fixed](https://news.ycombinator.com/item?id=46736091)**

Preflight Checklist I have searched existing issues and this hasn't been reported yet This is a single bug report (please file separate reports for different bugs) I am using the latest version of ...

⬆️ 184 • 💬 171 • 20h ago • [GitHub](https://github.com/anthropics/claude-code/issues/18866)

---

**[Satya Nadella: "We need to find something useful for AI"](https://news.ycombinator.com/item?id=46718485)**

Workers should learn AI skills and companies should use it because it's a "cognitive amplifier," claims Satya Nadella.

⬆️ 156 • 💬 204 • 2d ago • [PC Gamer](https://www.pcgamer.com/software/ai/microsoft-ceo-warns-that-we-must-do-something-useful-with-ai-or-theyll-lose-social-permission-to-burn-electricity-on-it/)

---

**[White House defends sharing AI image showing arrested woman crying](https://news.ycombinator.com/item?id=46731865)**

Latest updates from the BBC's specialists in fact-checking, verifying video and tackling disinformation.

⬆️ 130 • 💬 78 • 1d ago • [BBC News](https://www.bbc.co.uk/news/live/ce9yydgmzdvt)

---

**[Meet the Alaska Student Arrested for Eating an AI Art Exhibit](https://news.ycombinator.com/item?id=46719465)**

A conversation with Graham Granger, whose combination of protest and performance art spread beyond campus. “AI chews up and spits out art made by other people.”

⬆️ 97 • 💬 66 • 2d ago • [The Nation](https://www.thenation.com/article/society/alaska-student-arrested-eating-ai-art-exhibit/)

---

**[The state of modern AI text to speech systems for screen reader users](https://news.ycombinator.com/item?id=46730346)**

⬆️ 97 • 💬 43 • 1d ago • [stuff.interfree.ca](https://stuff.interfree.ca/2026/01/05/ai-tts-for-screenreaders.html)

---

**[Show HN: I've been using AI to analyze every supplement on the market](https://news.ycombinator.com/item?id=46719423)**

Helping you make informed decisions about your health by combining the latest research with the supplements available on the market.

⬆️ 86 • 💬 46 • 2d ago • [Supplement Research and Comparison Website](https://pillser.com/)

---

---

## YouTube Videos: "ai"

**[Elon Musk Says AI Will Surpass Humanity by 2031 in Explosive Davos Talk With Larry Fink | AI1G](https://www.youtube.com/watch?v=CXUG75IZOLY)**

Billionaire entrepreneur Elon Musk laid out a bold vision for humanity in a wide-ranging conversation with Larry Fink at the World ...

📺 DRM News

👁️ 7K • 👍 92 • 💬 53 • ⏱️ 16:31 • 1d ago

---

**[Automated QA Might Be The Biggest AI Breakthrough of 2026](https://www.youtube.com/watch?v=MEtDwwi7bEU)**

Abacus AI just announced DeepAgent — an AI agent built for the new software era where code is cheap and change is constant.

📺 AI Revolution

👁️ 10K • 👍 438 • 💬 41 • ⏱️ 9:10 • 14h ago

---

**[Apple Just Shocked Everyone: Introducing APPLE AI PIN](https://www.youtube.com/watch?v=iddMn6wAn3U)**

Apple is working on a new AI pin designed to live on your clothing and understand the world around you. Microsoft is pushing ...

📺 AI Revolution

👁️ 52K • 👍 1K • 💬 116 • ⏱️ 12:48 • 1d ago

---

**[OpenAI is Broke… and so is everyone else](https://www.youtube.com/watch?v=Y3N9qlPZBc0)**

Sam Altman said ads in ChatGPT would be a “last resort.” That was just over a year ago. Now OpenAI is burning billions monthly, ...

📺 Vanessa Wingårdh

👁️ 377K • 👍 19K • 💬 5K • ⏱️ 10:08 • 1d ago

---

**[Anthropic CEO says AI &quot;6 to 12 months&quot; away from doing software engineers&#39; jobs](https://www.youtube.com/watch?v=J2w9-4sa1_c)**

Tech leaders have taken the stage this week at the World Economic Forum in Davos, Switzerland, to discuss how AI will impact ...

📺 CBS News

👁️ 73K • 👍 809 • 💬 456 • ⏱️ 6:52 • 2d ago

---

**[AI News: Is OpenAI Speed Running Their Downfall?](https://www.youtube.com/watch?v=K5RG8-JvqUY)**

Here's the AI News you probably missed this week. Learn more about Box Extract here: ...

📺 Matt Wolfe

👁️ 24K • 👍 1K • 💬 167 • ⏱️ 28:01 • 12h ago

---

**[Which Crazy Bed Would You Choose? 🦋✨ | Ultimate Oddly Satisfying AI ASMR Pt.2](https://www.youtube.com/watch?v=Kl7OidH9eTE)**

Missed Part 1? Watch the original "Crazy Beds" here: https://www.youtube.com/watch?v=GrgJ30vZgyI Subscribe now to unlock ...

📺 Love And Peace

👁️ 528K • 👍 2K • 💬 40 • ⏱️ 11:47 • 3d ago

---

**[At Davos, Palantir CEO Explains EXACTLY How AI Will Impact Jobs | &#39;Exposing Job&#39;s Real Market Value&#39;](https://www.youtube.com/watch?v=aWCrw2wa3ls)**

Davos 2026 | World Economic Forum | AI | Tech Palantir Technologies Chief Executive Officer Alex Karp said he believes that ...

📺 Mint

👁️ 145K • 👍 2K • 💬 413 • ⏱️ 9:36 • 3d ago

---

**[Google DeepMind CEO on state of the AI race, push towards AGI and AI impact on jobs](https://www.youtube.com/watch?v=uVPdYqiULTo)**

Google DeepMind co-founder and CEO Demis Hassabis joins 'Squawk Box' to discuss the evolution of Gemini in the AI tech race, ...

📺 CNBC Television

👁️ 22K • 👍 254 • 💬 76 • ⏱️ 5:34 • 1d ago

---

**[DeepSeek Leaks MODEL1: New Flagship AI Shocks The Industry](https://www.youtube.com/watch?v=HiFnPNUpLDM)**

DeepSeek may have just exposed its next flagship model on GitHub — and the signals point to something far bigger than a ...

📺 AI Revolution

👁️ 34K • 👍 1K • 💬 78 • ⏱️ 15:40 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)**

*Z.ai*

GLM-4.7-Flash is a 30B-A3B MoE model, offering strong performance in the 30B class for efficient, lightweight deployment. It excels in benchmarks like AIME, GPQA, and SWE-bench, making it suitable for tasks requiring advanced reasoning and coding capabilities.

`text-generation` `31.2B`

⬇️ 279,658 • ❤️ 1,101 • 4d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time, full-duplex speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 22,852 • ❤️ 768 • 1d ago

---

**[VibeVoice-ASR](https://huggingface.co/microsoft/VibeVoice-ASR)**

*Microsoft*

VibeVoice-ASR is a unified speech-to-text model capable of processing up to 60 minutes of audio in a single pass, providing structured transcriptions with speaker diarization and timestamps. It supports customized hotwords for improved accuracy in domain-specific content.

`automatic-speech-recognition` `8.7B`

⬇️ 6,967 • ❤️ 398 • 2d ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a multilingual text-to-speech model supporting 10 languages with instruction-based control over prosody, emotion, and speaking rate. It features extreme low-latency streaming generation (as low as 97ms) and supports 9 premium timbres for style control, making it ideal for real-time interactive applications.

`1.9B`

⬇️ 20,374 • ❤️ 303 • 1d ago

---

**[GLM-4.7-Flash-GGUF](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF)**

*Unsloth AI*

GLM-4.7-Flash is a 30B-A3B MoE model offering a balance of performance and efficiency for lightweight deployment. It excels in benchmarks like AIME and GPQA, supporting local inference with frameworks such as vLLM and SGLang for text generation and tool-calling use cases.

`text-generation` `29.9B`

⬇️ 174,230 • ❤️ 295 • 10h ago

---

**[translategemma-4b-it](https://huggingface.co/google/translategemma-4b-it)**

*Google*

TranslateGemma-4b-it is a lightweight, open translation model supporting 55 languages, capable of translating text or extracting text from images. It's designed for resource-constrained environments, enabling state-of-the-art translation on local infrastructure.

`image-text-to-text` `5.0B`

⬇️ 67,913 • ❤️ 519 • 9d ago

---

**[AgentCPM-Report](https://huggingface.co/openbmb/AgentCPM-Report)**

*OpenBMB*

AgentCPM-Report is an 8B parameter LLM agent optimized for generating long-form, deeply insightful reports by performing extensive retrieval and chain-of-thought reasoning. It supports fully offline, local deployment for enhanced data security and can process private knowledge bases using the UltraRAG framework.

`8.2B`

⬇️ 584 • ❤️ 223 • 4d ago

---

**[LightOnOCR-2-1B](https://huggingface.co/lightonai/LightOnOCR-2-1B)**

*LightOn AI*

LightOnOCR-2-1B is an efficient 1B-parameter end-to-end vision-language model for document OCR, excelling at extracting text from PDFs and images, including tables and forms, with state-of-the-art accuracy and speed.

`image-text-to-text` `1.0B`

⬇️ 11,299 • ❤️ 213 • 3d ago

---

**[pocket-tts](https://huggingface.co/kyutai/pocket-tts)**

*Kyutai*

Pocket TTS is a lightweight, CPU-efficient text-to-speech model (100M parameters) offering low-latency audio generation (~200ms) and voice cloning capabilities. It's ideal for applications requiring fast, on-device speech synthesis without GPU dependencies, supporting Python API and CLI integration.

⬇️ 42,118 • ❤️ 455 • 5d ago

---

**[Step3-VL-10B](https://huggingface.co/stepfun-ai/Step3-VL-10B)**

*StepFun*

STEP3-VL-10B is a 10B parameter vision-language model excelling in visual perception and complex reasoning, outperforming larger models through unified pre-training and parallel reasoning techniques. Its primary use cases include advanced multimodal understanding and generation tasks.

`image-text-to-text` `10.2B`

⬇️ 42,008 • ❤️ 295 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 25 • 💬 1 • ⭐ 2,789 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation](https://huggingface.co/papers/2504.08761)**

*Yuxuan Chen, Dewen Guo, Sen Mei et al. (15 authors)*

UltraRAG is a comprehensive RAG toolkit that automates knowledge adaptation across the entire workflow while providing a user-friendly interface for non-coding deployment.

▲ 0 • 💬 0 • ⭐ 3,216 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08761) • [💻 code](https://github.com/OpenBMB/UltraRAG)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 143 • 💬 6 • ⭐ 21,322 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[HeartMuLa: A Family of Open Sourced Music Foundation Models](https://huggingface.co/papers/2601.10547)**

*Dongchao Yang, Yuxin Xie, Yuguo Yin et al. (28 authors)*

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.

▲ 35 • 💬 4 • ⭐ 1,746 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10547) • [💻 code](https://github.com/HeartMuLa/heartlib) • [🔗 project](https://heartmula.github.io/)

---

**[FlashLabs Chroma 1.0: A Real-Time End-to-End Spoken Dialogue Model with Personalized Voice Cloning](https://huggingface.co/papers/2601.11141)**

*Tanyu Chen, Tairan Chen, Kai Shen et al. (7 authors)*

🏢 FlashLabs

Chroma 1.0 enables real-time spoken dialogue with personalized voice cloning through discrete speech representations and interleaved text-audio token scheduling.

▲ 16 • 💬 2 • ⭐ 335 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2601.11141) • [💻 code](https://github.com/FlashLabs-AI-Corp/FlashLabs-Chroma) • [🔗 project](https://www.flashlabs.ai/flashai-voice-agents)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 126 • 💬 6 • ⭐ 11,627 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Paper2Rebuttal: A Multi-Agent Framework for Transparent Author Response Assistance](https://huggingface.co/papers/2601.14171)**

*Qianli Ma, Chang Guo, Zhiheng Tian et al. (7 authors)*

🏢 AutoLab

RebuttalAgent is a multi-agent framework that reframes rebuttal generation as an evidence-centric planning task, improving coverage, faithfulness, and strategic coherence in academic peer review.

▲ 43 • 💬 2 • ⭐ 232 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.14171) • [💻 code](https://github.com/AutoLab-SAI-SJTU/Paper2Rebuttal) • [🔗 project](https://mqleet.github.io/Paper2Rebuttal_ProjectPage/)

---

**[Agentic Reasoning for Large Language Models](https://huggingface.co/papers/2601.12538)**

*Tianxin Wei, Ting-Wei Li, Zhining Liu et al. (29 authors)*

🏢 University of Illinois at Urbana-Champaign

Agentic reasoning redefines large language models as autonomous agents capable of planning, acting, and learning through continuous interaction in dynamic environments across single-agent and multi-agent frameworks.

▲ 163 • 💬 5 • ⭐ 305 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.12538) • [💻 code](https://github.com/weitianxin/Awesome-Agentic-Reasoning)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 32 • 💬 1 • ⭐ 68,401 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 159 • 💬 3 • ⭐ 4,616 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 10.1k • 🔱 542 • 8h ago

---

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 9.7k • 🔱 1.3k • 10h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 8.8k • 🔱 450 • 2d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 7.4k • 🔱 884 • 1d ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 5.8k • 🔱 1.0k • 11h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 5.1k • 🔱 5.4k • 3h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 4.2k • 🔱 451 • 2d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 2.7k • 🔱 223 • 1d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.4k • 🔱 337 • 1d ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 200+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 2.1k • 🔱 431 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*
