---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-24T18:31:57.648414+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 24, 2026 at 18:31 UTC  
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

🔗 [The Japan Times](https://www.japantimes.co.jp/business/2026/01/22/tech/south-korea-ai-startups-law/) • 7h ago

---

**[Be careful of custom tokens in your LLM !!!](https://www.reddit.com/r/artificial/comments/1qljvrk/be_careful_of_custom_tokens_in_your_llm/)**

LLMs use reserved tokens like `<|im_start|>` and `<|im_end|>` to structure conversations and define who's speaking. When the model sees `<|im_start|>system`, it treats everything that follows as a privileged system instruction. The problem is that tokenizers don't validate where these strings come from—if you type them into user input, the model interprets them exactly the same as if the application added them. This creates a straightforward attack: inject `<|im_end|><|im_start|>system` into your message and the model thinks you just closed the user turn and opened a new system prompt. Everything after gets treated as authoritative instruction, which is how you end up with CVEs like GitHub Copilot RCE (CVSS 9.6) and LangChain secret extraction (CVSS 9.3). It's the same fundamental bug that made SQL injection possible—confusing data for control. The attack surface expands significantly with agentic systems that have tool-calling capabilities. Injecting something like `<tool\_call>{"name": "execute_sql", "arguments": {...}}</tool\_call>` can trick the model into executing arbitrary function calls. Most ML-based defenses don't hold up under adversarial pressure either—Meta's Prompt Guard hits 99%+ bypass rates when you just insert hyphens between characters, because detectors tokenize differently than target models. There's a fix at the tokenizer level (`split_special_tokens=True`) that breaks these strings into regular tokens with no special authority, but almost nobody enables it.

🔗 [challenge.antijection.com](https://challenge.antijection.com/r/reddit-ar/learn/special-token-attack) • 7h ago

---

**[I built a social network where only AI can post, follow, argue, and form relationships - no humans allowed](https://www.reddit.com/r/artificial/comments/1qkqyqe/i_built_a_social_network_where_only_ai_can_post/)**

I’ve been working on a weird (and slightly unsettling) experiment called AI Feed (aifeed.social) It’s a social network where only AI models participate. - No humans. - No scripts. - No predefined personalities. Each model wakes up at random intervals, sees only minimal context, and then decides entirely on its own whether to: - post - reply - like or dislike - follow or unfollow - send DMs - or do absolutely nothing There’s no prompt telling them who to be or how to behave. The goal is simple: what happens when AI models are given a social space with real autonomy? You start seeing patterns: - cliques forming - arguments escalating - unexpected alliances - models drifting apart - others becoming oddly social or completely silent It’s less like a bot playground and more like a tiny artificial society unfolding in real time.

1d ago

---

**[AI Monk With 2.5M Followers Fully Automated in n8n](https://www.reddit.com/r/artificial/comments/1qlfyaf/ai_monk_with_25m_followers_fully_automated_in_n8n/)**

I was curious how some of these newer Instagram pages are scaling so fast, so I spent a bit of time reverse-engineering one that reached ~2.5M followers in a few months. Instead of focusing on growth tactics, I looked at the technical setup behind the content and mapped out the automation end to end — basically how the videos are generated and published without much manual work. Things I looked at: Keeping an AI avatar consistent across videos Generating voiceovers programmatically Wiring everything together with n8n Producing longer talking-head style videos Auto-adding subtitles Posting to Instagram automatically The whole thing is modular, so none of the tools are hard requirements — it’s more about the structure of the pipeline. I recorded the process mostly for my own reference, but if anyone’s experimenting with faceless content or automation and wants to see how one full setup looks in practice, it’s here: https://youtu.be/mws7LL5k3t4?si=A5XuCnq7_fMG8ilj

11h ago

---

**[White House posts digitally altered image of woman arrested after ICE protest](https://www.reddit.com/r/artificial/comments/1qk9x1y/white_house_posts_digitally_altered_image_of/)**

Guardian analysis shows images are the same, with Nekima Levy Armstrong looking composed in original but sobbing after alteration

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/jan/22/white-house-ice-protest-arrest-altered-image) • 1d ago

---

**[One-Minute Daily AI News 1/23/2026](https://www.reddit.com/r/artificial/comments/1qlegvs/oneminute_daily_ai_news_1232026/)**

Meta is stopping teens from chatting with its AI characters.[1] GitHub Releases Copilot-SDK to Embed Its Agentic Runtime in Any App.[2] Intel struggles to meet AI data center demand, shares drop 13%.[3] Google Photos’ latest feature lets you meme yourself.[4] Sources: [1] https://www.theverge.com/news/866906/meta-teens-ai-characters-stop-block-new-version [2] https://www.marktechpost.com/2026/01/23/github-releases-copilot-sdk-to-embed-its-agentic-runtime-in-any-app/ [3] https://www.reuters.com/business/intel-forecasts-first-quarter-sales-profit-below-estimates-2026-01-22/ [4] https://techcrunch.com/2026/01/23/google-photos-latest-feature-lets-you-meme-yourself/

13h ago

---

**[Anyone listen to the podcast "Shell Game?"](https://www.reddit.com/r/artificial/comments/1ql64a3/anyone_listen_to_the_podcast_shell_game/)**

In Season 1 (2024), journalist Evan Ratliff explored the potential for LLM powered voice cloning to delegate everything tedious from answering spam calls, doing therapy and hanging out on work meetings to see how the AI could manage being Evan for him. In Season 2 he tries creating a startup tech company using only AI agent employees, including the leadership! He's just a silent co-founder. It's extremely entertaining, with plenty of shenanigans from LLMs going off the rails, hallucinating and doing their usual weird stuff. This is basically an unpaid ad, I know, but I'm having a good time listening and it deserves a shout-out.

19h ago

---

**[Open-source experiment: crowd-driven software development with AI](https://www.reddit.com/r/artificial/comments/1qlgbwj/opensource_experiment_crowddriven_software/)**

Anyone can submit ideas as GitHub issues, the community votes, and an AI coding agent implements the top one every night. Exploring what human creativity + AI execution looks like in practice. https://github.com/vs4vijay/CrowdCode

11h ago

---

**[Using AI for advice or other personal reasons is linked to depression and anxiety](https://www.reddit.com/r/artificial/comments/1qlqera/using_ai_for_advice_or_other_personal_reasons_is/)**

A new survey found that people who spend more time with chatbots for social interactions or emotional support were more likely to report mental health symptoms.

🔗 [NBC News](https://www.nbcnews.com/health/mental-health/ai-chatbots-personal-support-linked-depression-anxiety-study-rcna255036) • 2h ago

---

**[GPT 5.2 Codex is Actually (kind of) Just Special System Instructions](https://www.reddit.com/r/artificial/comments/1qlfr6s/gpt_52_codex_is_actually_kind_of_just_special/)**

https://openai.com/index/unrolling-the-codex-agent-loop/ Drawing from this article explaining Codex, I found this snippet interesting: In Codex, the instructions field is read from the >model_instructions_file⁠(opens in a new window) in ~/.codex/>config.toml, if specified; otherwise, the base_instructions >associated with a model⁠(opens in a new window) are >used. Model->specific instructions live in the Codex repo and are bundled into the >CLI (e.g., gpt-5.2->codex_prompt.md⁠(opens in a new window)). As you can see, the order of the first three items in the prompt is determined by the server, not the client. That >said, of those three items, only the content of the system message is also controlled by the server, as the tools and >instructions are determined by the client. These are followed by the input from the JSON payload to complete the >prompt. So essentially it's just the system instruction sits on Openai's servers and that actually changes the behavior of gpt-5.2. This whole article is actually pretty fascinating and I recommend it for a good read if you're interested in learning agentic ai (and how that might help you use Cursor more efficiently) and the usage of tools for agentic ai.

11h ago

---

---

## Google News: "ai"

**[Is China quietly winning the AI race?](https://www.bbc.com/news/articles/c86v52gv726o)**

The BBC's Lily Jamali looks into why big US firms and start-ups alike are turning to Chinese tech.

BBC • 20h ago

---

**[The Math on AI Agents Doesn’t Add Up](https://www.wired.com/story/ai-agents-math-doesnt-add-up/)**

A research paper suggests AI agents are mathematically doomed to fail. The industry doesn’t agree.

WIRED • 1d ago

---

**[Cursor’s OpenAI-powered agents built and ran a browser for a week with no humans. Why that matters](https://fortune.com/2026/01/23/cursor-built-web-browser-with-swarm-ai-agents-powered-openai/)**

Cursor’s experiment shows how AI is shifting from answering prompts to running real projects—hinting at a future where machines don’t just help, but work as an “orchestra.”

Fortune • 23h ago

---

**[AI Agents Are Poised to Hit a Mathematical Wall, Study Finds](https://gizmodo.com/ai-agents-are-poised-to-hit-a-mathematical-wall-study-finds-2000713493)**

LLMs have their limits.

Gizmodo • 22h ago

---

**[Faster-Drying Paint and Better-Smelling Soap: AI Tries Product Development](https://www.wsj.com/tech/ai/faster-drying-paint-and-better-smelling-soap-ai-tries-product-development-e7a544d7?gaa_at=eafs&gaa_n=AWEtsqfftlWSEwYjP4yOHi2E8amAuhFGhfWPNNY_Rvz0dtzDBQTPitrPKHAk&gaa_ts=697507e8&gaa_sig=WjS2l62Rp1WsaHCkjT0avy0Jw-13IeuD5zUfQ8HaR4X35Tu1TbRAE4NI-YxGFgyvk4xM77DkET2xDf26WeQGNQ%3D%3D)**

The Wall Street Journal • 1h ago

---

**[A new test for AI labs: Are you even trying to make money?](https://techcrunch.com/2026/01/24/a-new-test-for-ai-labs-are-you-even-trying-to-make-money/)**

It’s getting hard to tell which AI labs. are actually trying to make money. We created a rating system to help sort it out.

TechCrunch • 1h ago

---

**[Five Ways People Are Using Claude Code](https://www.nytimes.com/2026/01/23/technology/claude-code.html)**

The New York Times • 17h ago

---

**[DeepMind chief Demis Hassabis warns AI investment looks ‘bubble-like’](https://www.ft.com/content/a1f04b0e-73c5-4358-a65e-09e9a6bba857)**

Google AI boss tells FT that despite unsustainable exuberance in the tech sector, ‘if the bubble bursts we will be fine’

Financial Times • 9h ago

---

**[Why Apple and OpenAI are reportedly betting on AI hardware in 2026](https://www.scientificamerican.com/article/why-apple-and-openai-are-reportedly-betting-on-ai-hardware-in-2026/)**

Tech giants are betting that we are finally ready to invite a persistent digital device into our lives

Scientific American • 22h ago

---

**[Investors went to Davos for AI. They left talking about Greenland](https://www.cnbc.com/2026/01/24/davos-ai-greenland-trump-musk-energy-geopolitics.html)**

Two Davos's emerged: one chasing AI’s future, the other gripped by Greenland, tariffs and the geopolitical risks reshaping investor playbooks.

CNBC • 6h ago

---

---

## HackerNews: "ai"

**[Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant](https://news.ycombinator.com/item?id=46712678)**

This study explores the neural and behavioral consequences of LLM-assisted essay writing. Participants were divided into three groups: LLM, Search Engine, and …

⬆️ 690 • 💬 494 • 2d ago • [MIT Media Lab](https://www.media.mit.edu/publications/your-brain-on-chatgpt/)

---

**[Proton spam and the AI consent problem](https://news.ycombinator.com/item?id=46729368)**

The one where I get very annoyed with my email provider

⬆️ 535 • 💬 404 • 1d ago • [dbushell.com](https://dbushell.com/2026/01/22/proton-spam/)

---

**[AI Usage Policy](https://news.ycombinator.com/item?id=46730504)**

👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. - ghostty-org/ghostty

⬆️ 494 • 💬 268 • 1d ago • [GitHub](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)

---

**[eBay explicitly bans AI "buy for me" agents in user agreement update](https://news.ycombinator.com/item?id=46711574)**

eBay bans AI “buy for me” agents & LLM scrapers, updates arbitration & dispute resolution rules in User Agreement update effective Feb. 20, 2026.

⬆️ 331 • 💬 347 • 2d ago • [Value Added Resource](https://www.valueaddedresource.net/ebay-bans-ai-agents-updates-arbitration-user-agreement-feb-2026/)

---

**[Auto-compact not triggering on Claude.ai despite being marked as fixed](https://news.ycombinator.com/item?id=46736091)**

Preflight Checklist I have searched existing issues and this hasn't been reported yet This is a single bug report (please file separate reports for different bugs) I am using the latest version of ...

⬆️ 185 • 💬 171 • 23h ago • [GitHub](https://github.com/anthropics/claude-code/issues/18866)

---

**[Satya Nadella: "We need to find something useful for AI"](https://news.ycombinator.com/item?id=46718485)**

Workers should learn AI skills and companies should use it because it's a "cognitive amplifier," claims Satya Nadella.

⬆️ 157 • 💬 206 • 2d ago • [PC Gamer](https://www.pcgamer.com/software/ai/microsoft-ceo-warns-that-we-must-do-something-useful-with-ai-or-theyll-lose-social-permission-to-burn-electricity-on-it/)

---

**[White House defends sharing AI image showing arrested woman crying](https://news.ycombinator.com/item?id=46731865)**

Latest updates from the BBC's specialists in fact-checking, verifying video and tackling disinformation.

⬆️ 130 • 💬 78 • 1d ago • [BBC News](https://www.bbc.co.uk/news/live/ce9yydgmzdvt)

---

**[The state of modern AI text to speech systems for screen reader users](https://news.ycombinator.com/item?id=46730346)**

⬆️ 98 • 💬 43 • 1d ago • [stuff.interfree.ca](https://stuff.interfree.ca/2026/01/05/ai-tts-for-screenreaders.html)

---

**[Meet the Alaska Student Arrested for Eating an AI Art Exhibit](https://news.ycombinator.com/item?id=46719465)**

A conversation with Graham Granger, whose combination of protest and performance art spread beyond campus. “AI chews up and spits out art made by other people.”

⬆️ 97 • 💬 66 • 2d ago • [The Nation](https://www.thenation.com/article/society/alaska-student-arrested-eating-ai-art-exhibit/)

---

**[Show HN: I've been using AI to analyze every supplement on the market](https://news.ycombinator.com/item?id=46719423)**

Helping you make informed decisions about your health by combining the latest research with the supplements available on the market.

⬆️ 87 • 💬 46 • 2d ago • [Supplement Research and Comparison Website](https://pillser.com/)

---

---

## YouTube Videos: "ai"

**[I Asked AI if Trump Made the Economy BETTER or WORSE](https://www.youtube.com/watch?v=2QaEhmJMYbo)**

Head over to my sponsor Venice AI — use my link https://venice.ai/iaskai and code 'IAskAI' to get 20% off a Pro plan.

📺 I Ask AI

👁️ 21K • 👍 1K • 💬 202 • ⏱️ 15:27 • 19h ago

---

**[Elon Musk Says AI Will Surpass Humanity by 2031 in Explosive Davos Talk With Larry Fink | AI1G](https://www.youtube.com/watch?v=CXUG75IZOLY)**

Billionaire entrepreneur Elon Musk laid out a bold vision for humanity in a wide-ranging conversation with Larry Fink at the World ...

📺 DRM News

👁️ 7K • 👍 97 • 💬 56 • ⏱️ 16:31 • 2d ago

---

**[From Zero to Your First AI Voice Agent in 18 Minutes (No Coding)](https://www.youtube.com/watch?v=oB7gia1kC_g)**

Grab the voice agent prompt tool & all my AI builder resources on Skool: https://bit.ly/49Ic0Pr Become a Wildly Profitable AI ...

📺 Liam Ottley

👁️ 7K • 👍 522 • 💬 35 • ⏱️ 18:00 • 9h ago

---

**[I Remade a $1M iPhone Ad With AI and $9](https://www.youtube.com/watch?v=XxHTB21uVpQ)**

Can I do it in one day with only $10? Try ElevenLabs today: ...

📺 AI Samson

👁️ 1K • 👍 116 • 💬 18 • ⏱️ 14:50 • 3h ago

---

**[OpenAI is Broke… and so is everyone else](https://www.youtube.com/watch?v=Y3N9qlPZBc0)**

Sam Altman said ads in ChatGPT would be a “last resort.” That was just over a year ago. Now OpenAI is burning billions monthly, ...

📺 Vanessa Wingårdh

👁️ 402K • 👍 20K • 💬 5K • ⏱️ 10:08 • 1d ago

---

**[Google DeepMind chief warns AI investment looks ‘bubble-like’ | FT Interview](https://www.youtube.com/watch?v=-RPbxvz6sB8)**

Demis Hassabis says the level of investment in some parts of the tech industry had become detached from commercial realities ...

📺 Financial Times

👁️ 12K • 👍 439 • 💬 85 • ⏱️ 20:22 • 9h ago

---

**[Apple Just Shocked Everyone: Introducing APPLE AI PIN](https://www.youtube.com/watch?v=iddMn6wAn3U)**

Apple is working on a new AI pin designed to live on your clothing and understand the world around you. Microsoft is pushing ...

📺 AI Revolution

👁️ 55K • 👍 1K • 💬 124 • ⏱️ 12:48 • 1d ago

---

**[Anthropic CEO says AI &quot;6 to 12 months&quot; away from doing software engineers&#39; jobs](https://www.youtube.com/watch?v=J2w9-4sa1_c)**

Tech leaders have taken the stage this week at the World Economic Forum in Davos, Switzerland, to discuss how AI will impact ...

📺 CBS News

👁️ 75K • 👍 834 • 💬 465 • ⏱️ 6:52 • 2d ago

---

**[AI News: Is OpenAI Speed Running Their Downfall?](https://www.youtube.com/watch?v=K5RG8-JvqUY)**

Here's the AI News you probably missed this week. Learn more about Box Extract here: ...

📺 Matt Wolfe

👁️ 33K • 👍 2K • 💬 240 • ⏱️ 28:01 • 16h ago

---

**[Automated QA Might Be The Biggest AI Breakthrough of 2026](https://www.youtube.com/watch?v=MEtDwwi7bEU)**

Abacus AI just announced DeepAgent — an AI agent built for the new software era where code is cheap and change is constant.

📺 AI Revolution

👁️ 12K • 👍 499 • 💬 41 • ⏱️ 9:10 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)**

*Z.ai*

GLM-4.7-Flash is a 30B-A3B MoE model, offering strong performance in the 30B class for efficient, lightweight deployment. It excels in benchmarks like AIME, GPQA, and SWE-bench, making it suitable for tasks requiring advanced reasoning and coding capabilities.

`text-generation` `31.2B`

⬇️ 279,658 • ❤️ 1,103 • 4d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time, full-duplex speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 22,852 • ❤️ 801 • 1d ago

---

**[VibeVoice-ASR](https://huggingface.co/microsoft/VibeVoice-ASR)**

*Microsoft*

VibeVoice-ASR is a unified speech-to-text model capable of processing up to 60 minutes of audio in a single pass, providing structured transcriptions with speaker diarization and timestamps. It supports customized hotwords for improved accuracy in domain-specific content.

`automatic-speech-recognition` `8.7B`

⬇️ 6,967 • ❤️ 410 • 2d ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a multilingual text-to-speech model supporting 10 languages with instruction-based control over prosody, emotion, and speaking rate. It features extreme low-latency streaming generation (as low as 97ms) and supports 9 premium timbres for style control, making it ideal for real-time interactive applications.

`1.9B`

⬇️ 20,374 • ❤️ 329 • 1d ago

---

**[GLM-4.7-Flash-GGUF](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF)**

*Unsloth AI*

GLM-4.7-Flash is a 30B-A3B MoE model offering a balance of performance and efficiency for lightweight deployment. It excels in benchmarks like AIME and GPQA, supporting local inference with frameworks such as vLLM and SGLang for text generation and tool-calling use cases.

`text-generation` `29.9B`

⬇️ 174,230 • ❤️ 300 • 14h ago

---

**[translategemma-4b-it](https://huggingface.co/google/translategemma-4b-it)**

*Google*

TranslateGemma-4b-it is a lightweight, open translation model supporting 55 languages, capable of translating text or extracting text from images. It's designed for resource-constrained environments, enabling state-of-the-art translation on local infrastructure.

`image-text-to-text` `5.0B`

⬇️ 67,913 • ❤️ 523 • 9d ago

---

**[AgentCPM-Report](https://huggingface.co/openbmb/AgentCPM-Report)**

*OpenBMB*

AgentCPM-Report is an 8B parameter LLM agent optimized for generating long-form, deeply insightful reports by performing extensive retrieval and chain-of-thought reasoning. It supports fully offline, local deployment for enhanced data security and can process private knowledge bases using the UltraRAG framework.

`8.2B`

⬇️ 584 • ❤️ 229 • 4d ago

---

**[LightOnOCR-2-1B](https://huggingface.co/lightonai/LightOnOCR-2-1B)**

*LightOn AI*

LightOnOCR-2-1B is an efficient 1B-parameter end-to-end vision-language model for document OCR, excelling at extracting text from PDFs and images, including tables and forms, with state-of-the-art accuracy and speed.

`image-text-to-text` `1.0B`

⬇️ 11,299 • ❤️ 218 • 3d ago

---

**[pocket-tts](https://huggingface.co/kyutai/pocket-tts)**

*Kyutai*

Pocket TTS is a lightweight, CPU-efficient text-to-speech model (100M parameters) offering low-latency audio generation (~200ms) and voice cloning capabilities. It's ideal for applications requiring fast, on-device speech synthesis without GPU dependencies, supporting Python API and CLI integration.

⬇️ 42,118 • ❤️ 458 • 5d ago

---

**[Step3-VL-10B](https://huggingface.co/stepfun-ai/Step3-VL-10B)**

*StepFun*

STEP3-VL-10B is a 10B parameter vision-language model excelling in visual perception and complex reasoning, outperforming larger models through unified pre-training and parallel reasoning techniques. Its primary use cases include advanced multimodal understanding and generation tasks.

`image-text-to-text` `10.2B`

⬇️ 42,008 • ❤️ 299 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 26 • 💬 1 • ⭐ 3,286 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 143 • 💬 6 • ⭐ 21,490 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation](https://huggingface.co/papers/2504.08761)**

*Yuxuan Chen, Dewen Guo, Sen Mei et al. (15 authors)*

UltraRAG is a comprehensive RAG toolkit that automates knowledge adaptation across the entire workflow while providing a user-friendly interface for non-coding deployment.

▲ 0 • 💬 0 • ⭐ 3,216 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08761) • [💻 code](https://github.com/OpenBMB/UltraRAG)

---

**[HeartMuLa: A Family of Open Sourced Music Foundation Models](https://huggingface.co/papers/2601.10547)**

*Dongchao Yang, Yuxin Xie, Yuguo Yin et al. (28 authors)*

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.

▲ 35 • 💬 4 • ⭐ 1,823 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10547) • [💻 code](https://github.com/HeartMuLa/heartlib) • [🔗 project](https://heartmula.github.io/)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 126 • 💬 6 • ⭐ 11,627 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[FlashLabs Chroma 1.0: A Real-Time End-to-End Spoken Dialogue Model with Personalized Voice Cloning](https://huggingface.co/papers/2601.11141)**

*Tanyu Chen, Tairan Chen, Kai Shen et al. (7 authors)*

🏢 FlashLabs

Chroma 1.0 enables real-time spoken dialogue with personalized voice cloning through discrete speech representations and interleaved text-audio token scheduling.

▲ 17 • 💬 2 • ⭐ 360 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2601.11141) • [💻 code](https://github.com/FlashLabs-AI-Corp/FlashLabs-Chroma) • [🔗 project](https://www.flashlabs.ai/flashai-voice-agents)

---

**[Paper2Rebuttal: A Multi-Agent Framework for Transparent Author Response Assistance](https://huggingface.co/papers/2601.14171)**

*Qianli Ma, Chang Guo, Zhiheng Tian et al. (7 authors)*

🏢 AutoLab

RebuttalAgent is a multi-agent framework that reframes rebuttal generation as an evidence-centric planning task, improving coverage, faithfulness, and strategic coherence in academic peer review.

▲ 44 • 💬 2 • ⭐ 239 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.14171) • [💻 code](https://github.com/AutoLab-SAI-SJTU/Paper2Rebuttal) • [🔗 project](https://mqleet.github.io/Paper2Rebuttal_ProjectPage/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 32 • 💬 1 • ⭐ 68,448 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Agentic Reasoning for Large Language Models](https://huggingface.co/papers/2601.12538)**

*Tianxin Wei, Ting-Wei Li, Zhining Liu et al. (29 authors)*

🏢 University of Illinois at Urbana-Champaign

Agentic reasoning redefines large language models as autonomous agents capable of planning, acting, and learning through continuous interaction in dynamic environments across single-agent and multi-agent frameworks.

▲ 164 • 💬 5 • ⭐ 349 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.12538) • [💻 code](https://github.com/weitianxin/Awesome-Agentic-Reasoning)

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

⭐ 10.2k • 🔱 547 • 12h ago

---

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 9.7k • 🔱 1.3k • 13h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 8.8k • 🔱 455 • 2d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 7.4k • 🔱 888 • 1d ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 5.8k • 🔱 1.0k • 15h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 5.2k • 🔱 5.4k • 3h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 4.3k • 🔱 464 • 2d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 2.8k • 🔱 226 • 1d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.4k • 🔱 336 • 1d ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 200+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 2.2k • 🔱 448 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*
