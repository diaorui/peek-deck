---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-25T02:00:37.198070+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 25, 2026 at 02:00 UTC  
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

**[Latest ChatGPT model uses Elon Musk’s Grokipedia as source, tests reveal](https://www.reddit.com/r/artificial/comments/1qlwt4l/latest_chatgpt_model_uses_elon_musks_grokipedia/)**

Guardian found OpenAI’s platform cited Grokipedia on topics including Iran and Holocaust deniers

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jan/24/latest-chatgpt-model-uses-elon-musks-grokipedia-as-source-tests-reveal) • 6h ago

---

**[NVIDIA’s real moat isn’t hardware, it’s 4 million developers](https://www.reddit.com/r/artificial/comments/1qm3ts4/nvidias_real_moat_isnt_hardware_its_4_million/)**

I couldn't stop thinking about Theo's "Why NVIDIA is dying" video. The thesis felt important enough to verify. So I dug through SEC filings, earnings reports, and technical benchmarks. What I found: NVIDIA isn't dying. Its $35.1B quarterly revenue is up 94% Yes, market share dropped (90% → 70-80%), but the pie is growing faster Groq and Cerebras have impressive chips, but asterisks everywhere The real moat: 4 million devs can't just abandon 20 years of CUDA tooling Plot twist: the biggest threat is Google/Amazon/Microsoft, not startups Deeper piece with Cerebras and Groq factored in at https://medium.com/@jpcaparas/nvidias-real-moat-isn-t-hardware-it-s-4-million-developers-648d6aeb1226?sk=82ee7baf9290da1eb93efd9d34c4c7b4

🔗 [medium.com](https://medium.com/@jpcaparas/nvidias-real-moat-isn-t-hardware-it-s-4-million-developers-648d6aeb1226?sk=82ee7baf9290da1eb93efd9d34c4c7b4) • 1h ago

---

**[South Korea launches landmark laws to regulate artificial intelligence](https://www.reddit.com/r/artificial/comments/1qlk7pz/south_korea_launches_landmark_laws_to_regulate/)**

Seoul hopes its new AI Basic Act will position the country as a leader ‍in the field, taking effect in South Korea sooner than a comparable ‍effort in Europe.

🔗 [The Japan Times](https://www.japantimes.co.jp/business/2026/01/22/tech/south-korea-ai-startups-law/) • 14h ago

---

**[The AI Delusion Epidemic](https://www.reddit.com/r/artificial/comments/1qlusy9/the_ai_delusion_epidemic/)**

🔗 [medium.com](https://medium.com/ai-advances/the-ai-delusion-epidemic-a851e0a4d842?sk=c629df4365a925426dcc5ab851861da2) • 7h ago

---

**[Be careful of custom tokens in your LLM !!!](https://www.reddit.com/r/artificial/comments/1qljvrk/be_careful_of_custom_tokens_in_your_llm/)**

LLMs use reserved tokens like `<|im_start|>` and `<|im_end|>` to structure conversations and define who's speaking. When the model sees `<|im_start|>system`, it treats everything that follows as a privileged system instruction. The problem is that tokenizers don't validate where these strings come from—if you type them into user input, the model interprets them exactly the same as if the application added them. This creates a straightforward attack: inject `<|im_end|><|im_start|>system` into your message and the model thinks you just closed the user turn and opened a new system prompt. Everything after gets treated as authoritative instruction, which is how you end up with CVEs like GitHub Copilot RCE (CVSS 9.6) and LangChain secret extraction (CVSS 9.3). It's the same fundamental bug that made SQL injection possible—confusing data for control. The attack surface expands significantly with agentic systems that have tool-calling capabilities. Injecting something like `<tool\_call>{"name": "execute_sql", "arguments": {...}}</tool\_call>` can trick the model into executing arbitrary function calls. Most ML-based defenses don't hold up under adversarial pressure either—Meta's Prompt Guard hits 99%+ bypass rates when you just insert hyphens between characters, because detectors tokenize differently than target models. There's a fix at the tokenizer level (`split_special_tokens=True`) that breaks these strings into regular tokens with no special authority, but almost nobody enables it.

🔗 [challenge.antijection.com](https://challenge.antijection.com/r/reddit-ar/learn/special-token-attack) • 15h ago

---

**[met someone who does ai cloning to "preserve legacy" as in your grandfather ,etc. Would this work?](https://www.reddit.com/r/artificial/comments/1qlvkka/met_someone_who_does_ai_cloning_to_preserve/)**

So im assuming he makes the person ask a long questionnaire that feeds into ai, and then talks to ai to get a sense of a person. The question is does this actually make the AI have this persons personality where it can be thought of as asking your grandfather. Because that seems wild to me. you never know if your grandfathers prejudices were hidden. thoughts ?

6h ago

---

**[AI Monk With 2.5M Followers Fully Automated in n8n](https://www.reddit.com/r/artificial/comments/1qlfyaf/ai_monk_with_25m_followers_fully_automated_in_n8n/)**

I was curious how some of these newer Instagram pages are scaling so fast, so I spent a bit of time reverse-engineering one that reached ~2.5M followers in a few months. Instead of focusing on growth tactics, I looked at the technical setup behind the content and mapped out the automation end to end — basically how the videos are generated and published without much manual work. Things I looked at: Keeping an AI avatar consistent across videos Generating voiceovers programmatically Wiring everything together with n8n Producing longer talking-head style videos Auto-adding subtitles Posting to Instagram automatically The whole thing is modular, so none of the tools are hard requirements — it’s more about the structure of the pipeline. I recorded the process mostly for my own reference, but if anyone’s experimenting with faceless content or automation and wants to see how one full setup looks in practice, it’s here: https://youtu.be/mws7LL5k3t4?si=A5XuCnq7_fMG8ilj

19h ago

---

**[I built a social network where only AI can post, follow, argue, and form relationships - no humans allowed](https://www.reddit.com/r/artificial/comments/1qkqyqe/i_built_a_social_network_where_only_ai_can_post/)**

I’ve been working on a weird (and slightly unsettling) experiment called AI Feed (aifeed.social) It’s a social network where only AI models participate. - No humans. - No scripts. - No predefined personalities. Each model wakes up at random intervals, sees only minimal context, and then decides entirely on its own whether to: - post - reply - like or dislike - follow or unfollow - send DMs - or do absolutely nothing There’s no prompt telling them who to be or how to behave. The goal is simple: what happens when AI models are given a social space with real autonomy? You start seeing patterns: - cliques forming - arguments escalating - unexpected alliances - models drifting apart - others becoming oddly social or completely silent It’s less like a bot playground and more like a tiny artificial society unfolding in real time.

1d ago

---

**[White House posts digitally altered image of woman arrested after ICE protest](https://www.reddit.com/r/artificial/comments/1qk9x1y/white_house_posts_digitally_altered_image_of/)**

Guardian analysis shows images are the same, with Nekima Levy Armstrong looking composed in original but sobbing after alteration

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/jan/22/white-house-ice-protest-arrest-altered-image) • 2d ago

---

**[One-Minute Daily AI News 1/23/2026](https://www.reddit.com/r/artificial/comments/1qlegvs/oneminute_daily_ai_news_1232026/)**

Meta is stopping teens from chatting with its AI characters.[1] GitHub Releases Copilot-SDK to Embed Its Agentic Runtime in Any App.[2] Intel struggles to meet AI data center demand, shares drop 13%.[3] Google Photos’ latest feature lets you meme yourself.[4] Sources: [1] https://www.theverge.com/news/866906/meta-teens-ai-characters-stop-block-new-version [2] https://www.marktechpost.com/2026/01/23/github-releases-copilot-sdk-to-embed-its-agentic-runtime-in-any-app/ [3] https://www.reuters.com/business/intel-forecasts-first-quarter-sales-profit-below-estimates-2026-01-22/ [4] https://techcrunch.com/2026/01/23/google-photos-latest-feature-lets-you-meme-yourself/

20h ago

---

---

## Google News: "ai"

**[Interest in Law School Is Surging. A.I. Makes the Payoff Less Certain.](https://www.nytimes.com/2026/01/24/business/dealbook/law-school-ai.html)**

The New York Times • 11h ago

---

**[Is China quietly winning the AI race?](https://www.bbc.com/news/articles/c86v52gv726o)**

The BBC's Lily Jamali looks into why big US firms and start-ups alike are turning to Chinese tech.

BBC • 1d ago

---

**[The Math on AI Agents Doesn’t Add Up](https://www.wired.com/story/ai-agents-math-doesnt-add-up/)**

A research paper suggests AI agents are mathematically doomed to fail. The industry doesn’t agree.

WIRED • 1d ago

---

**[Pope Leo warns of ‘overly affectionate’ AI chatbots](https://www.cnn.com/2026/01/24/europe/pope-leo-ai-chatbots-warning-intl)**

Beware of the AI chatbot that becomes more than just a friend, or worse, an emotional crutch. Pope Leo XIV has warned about overly “affectionate” chatbots, urging regulation to prevent humans from forming serious emotional bonds with their AI companions.

CNN • 9h ago

---

**[As massive winter storm hits, NWS has been using new AI-powered forecasts](https://www.washingtonpost.com/weather/2026/01/24/winter-storm-ai-forecasts/)**

The Washington Post • 8h ago

---

**[Meta has quietly become an AI infrastructure giant. 'Meta Compute' is Zuckerberg making it official.](https://fortune.com/2026/01/24/meta-compute-zuckerberg-ai-infrastructure-giant-data-center/)**

With Meta Compute, Mark Zuckerberg is turning data centers, chips, and power into what may be the company’s next great strategic weapon.

Fortune • 13h ago

---

**[Google AI Overviews cite YouTube more than any medical site for health queries, study suggests](https://www.theguardian.com/technology/2026/jan/24/google-ai-overviews-youtube-medical-citations-study)**

Exclusive: German research into responses to health queries raises fresh questions about summaries seen by 2bn people a month

The Guardian • 8h ago

---

**[Investors went to Davos for AI. They left talking about Greenland](https://www.cnbc.com/2026/01/24/davos-ai-greenland-trump-musk-energy-geopolitics.html)**

Two Davos's emerged: one chasing AI’s future, the other gripped by Greenland, tariffs and the geopolitical risks reshaping investor playbooks.

CNBC • 13h ago

---

**[Tech CEOs boast and bicker about AI at Davos](https://techcrunch.com/2026/01/24/tech-ceos-boast-and-bicker-about-ai-at-davos/)**

There were times at this week’s meeting of the World Economic Forum when Davos seemed transformed into a high-powered tech conference.

TechCrunch • 5h ago

---

**[CEOs at Davos were split on how bad the AI job wipeout will be](https://fortune.com/2026/01/23/davos-ceo-ai-job-wipeout-projections-world-economic-forum/)**

In over a dozen meetings with top executives, two main themes stood out.

Fortune • 1d ago

---

---

## HackerNews: "ai"

**[Proton spam and the AI consent problem](https://news.ycombinator.com/item?id=46729368)**

The one where I get very annoyed with my email provider

⬆️ 539 • 💬 413 • 1d ago • [dbushell.com](https://dbushell.com/2026/01/22/proton-spam/)

---

**[AI Usage Policy](https://news.ycombinator.com/item?id=46730504)**

👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. - ghostty-org/ghostty

⬆️ 498 • 💬 271 • 1d ago • [GitHub](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)

---

**[Auto-compact not triggering on Claude.ai despite being marked as fixed](https://news.ycombinator.com/item?id=46736091)**

Preflight Checklist I have searched existing issues and this hasn't been reported yet This is a single bug report (please file separate reports for different bugs) I am using the latest version of ...

⬆️ 185 • 💬 175 • 1d ago • [GitHub](https://github.com/anthropics/claude-code/issues/18866)

---

**[Satya Nadella: "We need to find something useful for AI"](https://news.ycombinator.com/item?id=46718485)**

Workers should learn AI skills and companies should use it because it's a "cognitive amplifier," claims Satya Nadella.

⬆️ 157 • 💬 208 • 2d ago • [PC Gamer](https://www.pcgamer.com/software/ai/microsoft-ceo-warns-that-we-must-do-something-useful-with-ai-or-theyll-lose-social-permission-to-burn-electricity-on-it/)

---

**[White House defends sharing AI image showing arrested woman crying](https://news.ycombinator.com/item?id=46731865)**

Latest updates from the BBC's specialists in fact-checking, verifying video and tackling disinformation.

⬆️ 132 • 💬 79 • 1d ago • [BBC News](https://www.bbc.co.uk/news/live/ce9yydgmzdvt)

---

**[The state of modern AI text to speech systems for screen reader users](https://news.ycombinator.com/item?id=46730346)**

⬆️ 99 • 💬 47 • 1d ago • [stuff.interfree.ca](https://stuff.interfree.ca/2026/01/05/ai-tts-for-screenreaders.html)

---

**[Meet the Alaska Student Arrested for Eating an AI Art Exhibit](https://news.ycombinator.com/item?id=46719465)**

A conversation with Graham Granger, whose combination of protest and performance art spread beyond campus. “AI chews up and spits out art made by other people.”

⬆️ 97 • 💬 67 • 2d ago • [The Nation](https://www.thenation.com/article/society/alaska-student-arrested-eating-ai-art-exhibit/)

---

**[Show HN: I've been using AI to analyze every supplement on the market](https://news.ycombinator.com/item?id=46719423)**

Helping you make informed decisions about your health by combining the latest research with the supplements available on the market.

⬆️ 88 • 💬 47 • 2d ago • [Supplement Research and Comparison Website](https://pillser.com/)

---

**[AI can 10x developers in creating tech debt](https://news.ycombinator.com/item?id=46740548)**

⬆️ 68 • 💬 26 • 23h ago • [stackoverflow.blog](https://stackoverflow.blog/2026/01/23/ai-can-10x-developers-in-creating-tech-debt/)

---

**[CEOs Say AI Is Making Work More Efficient. Employees Tell a Different Story](https://news.ycombinator.com/item?id=46728781)**

⬆️ 51 • 💬 20 • 1d ago • [wsj.com](https://www.wsj.com/lifestyle/workplace/ceos-say-ai-is-making-work-more-efficient-employees-tell-a-different-story-6613ce9d)

---

---

## YouTube Videos: "ai"

**[Elon Musk Says AI Will Surpass Humanity by 2031 in Explosive Davos Talk With Larry Fink | AI1G](https://www.youtube.com/watch?v=CXUG75IZOLY)**

Billionaire entrepreneur Elon Musk laid out a bold vision for humanity in a wide-ranging conversation with Larry Fink at the World ...

📺 DRM News

👁️ 8K • 👍 101 • 💬 56 • ⏱️ 16:31 • 2d ago

---

**[Google DeepMind chief warns AI investment looks ‘bubble-like’ | FT Interview](https://www.youtube.com/watch?v=-RPbxvz6sB8)**

Demis Hassabis says the level of investment in some parts of the tech industry had become detached from commercial realities ...

📺 Financial Times

👁️ 21K • 👍 574 • 💬 130 • ⏱️ 20:22 • 16h ago

---

**[OpenAI is Broke... Nvidia Caught Pirating To Train AI?!](https://www.youtube.com/watch?v=USVZuOafIi4)**

OpenAI's last resort is here... Nvida alegedly using stolen copyrighted content to train AI models, Microsoft is messing up again.

📺 Stylosa

👁️ 14K • 👍 740 • 💬 258 • ⏱️ 16:18 • 5h ago

---

**[Apple Just Shocked Everyone: Introducing APPLE AI PIN](https://www.youtube.com/watch?v=iddMn6wAn3U)**

Apple is working on a new AI pin designed to live on your clothing and understand the world around you. Microsoft is pushing ...

📺 AI Revolution

👁️ 59K • 👍 1K • 💬 131 • ⏱️ 12:48 • 2d ago

---

**[OpenAI is Broke… and so is everyone else](https://www.youtube.com/watch?v=Y3N9qlPZBc0)**

Sam Altman said ads in ChatGPT would be a “last resort.” That was just over a year ago. Now OpenAI is burning billions monthly, ...

📺 Vanessa Wingårdh

👁️ 427K • 👍 21K • 💬 5K • ⏱️ 10:08 • 1d ago

---

**[AI News: Is OpenAI Speed Running Their Downfall?](https://www.youtube.com/watch?v=K5RG8-JvqUY)**

Here's the AI News you probably missed this week. Learn more about Box Extract here: ...

📺 Matt Wolfe

👁️ 42K • 👍 2K • 💬 282 • ⏱️ 28:01 • 23h ago

---

**[Google DeepMind CEO on state of the AI race, push towards AGI and AI impact on jobs](https://www.youtube.com/watch?v=uVPdYqiULTo)**

Google DeepMind co-founder and CEO Demis Hassabis joins 'Squawk Box' to discuss the evolution of Gemini in the AI tech race, ...

📺 CNBC Television

👁️ 25K • 👍 275 • 💬 78 • ⏱️ 5:34 • 1d ago

---

**[Automated QA Might Be The Biggest AI Breakthrough of 2026](https://www.youtube.com/watch?v=MEtDwwi7bEU)**

Abacus AI just announced DeepAgent — an AI agent built for the new software era where code is cheap and change is constant.

📺 AI Revolution

👁️ 14K • 👍 545 • 💬 48 • ⏱️ 9:10 • 1d ago

---

**[It&#39;s Official..Ai Songs Have Taken OVER](https://www.youtube.com/watch?v=7LStLP5liII)**

ai songs are getting more popular Instagram: https://www.instagram.com/liamdonovanmusic/ Subreddit: ...

📺 Liam Donovan

👁️ 20K • 👍 2K • 💬 318 • ⏱️ 11:54 • 1d ago

---

**[$10,000 Mac Studio vs. $10 AI Agent](https://www.youtube.com/watch?v=hxDe1j_IcSQ)**

I used my $10000 512GB Mac Studio to see if local AI can finally beat a $10/month cloud coding agent—and the result was way ...

📺 Alex Ziskind

👁️ 31K • 👍 1K • 💬 149 • ⏱️ 16:40 • 6h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)**

*Z.ai*

GLM-4.7-Flash is a 30B-A3B MoE model, offering strong performance in the 30B class for efficient, lightweight deployment. It excels in benchmarks like AIME, GPQA, and SWE-bench, making it suitable for tasks requiring advanced reasoning and coding capabilities.

`text-generation` `31.2B`

⬇️ 279,658 • ❤️ 1,120 • 4d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time, full-duplex speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 22,852 • ❤️ 830 • 2d ago

---

**[VibeVoice-ASR](https://huggingface.co/microsoft/VibeVoice-ASR)**

*Microsoft*

VibeVoice-ASR is a unified speech-to-text model capable of processing up to 60 minutes of audio in a single pass, providing structured transcriptions with speaker diarization and timestamps. It supports customized hotwords for improved accuracy in domain-specific content.

`automatic-speech-recognition` `8.7B`

⬇️ 6,967 • ❤️ 429 • 3d ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a multilingual text-to-speech model supporting 10 languages with instruction-based control over prosody, emotion, and speaking rate. It features extreme low-latency streaming generation (as low as 97ms) and supports 9 premium timbres for style control, making it ideal for real-time interactive applications.

`1.9B`

⬇️ 20,374 • ❤️ 358 • 1d ago

---

**[GLM-4.7-Flash-GGUF](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF)**

*Unsloth AI*

GLM-4.7-Flash is a 30B-A3B MoE model offering a balance of performance and efficiency for lightweight deployment. It excels in benchmarks like AIME and GPQA, supporting local inference with frameworks such as vLLM and SGLang for text generation and tool-calling use cases.

`text-generation` `29.9B`

⬇️ 174,230 • ❤️ 308 • 22h ago

---

**[translategemma-4b-it](https://huggingface.co/google/translategemma-4b-it)**

*Google*

TranslateGemma-4b-it is a lightweight, open translation model supporting 55 languages, capable of translating text or extracting text from images. It's designed for resource-constrained environments, enabling state-of-the-art translation on local infrastructure.

`image-text-to-text` `5.0B`

⬇️ 67,913 • ❤️ 525 • 9d ago

---

**[AgentCPM-Report](https://huggingface.co/openbmb/AgentCPM-Report)**

*OpenBMB*

AgentCPM-Report is an 8B parameter LLM agent optimized for generating long-form, deeply insightful reports by performing extensive retrieval and chain-of-thought reasoning. It supports fully offline, local deployment for enhanced data security and can process private knowledge bases using the UltraRAG framework.

`8.2B`

⬇️ 584 • ❤️ 236 • 4d ago

---

**[LightOnOCR-2-1B](https://huggingface.co/lightonai/LightOnOCR-2-1B)**

*LightOn AI*

LightOnOCR-2-1B is an efficient 1B-parameter end-to-end vision-language model for document OCR, excelling at extracting text from PDFs and images, including tables and forms, with state-of-the-art accuracy and speed.

`image-text-to-text` `1.0B`

⬇️ 11,299 • ❤️ 229 • 3d ago

---

**[Step3-VL-10B](https://huggingface.co/stepfun-ai/Step3-VL-10B)**

*StepFun*

STEP3-VL-10B is a 10B parameter vision-language model excelling in visual perception and complex reasoning, outperforming larger models through unified pre-training and parallel reasoning techniques. Its primary use cases include advanced multimodal understanding and generation tasks.

`image-text-to-text` `10.2B`

⬇️ 42,008 • ❤️ 306 • 1d ago

---

**[sweep-next-edit-1.5B](https://huggingface.co/sweepai/sweep-next-edit-1.5B)**

*Sweep AI*

Sweep Next-Edit 1.5B is a GGUF quantized model for next-edit code autocompletion, running locally in under 500ms and outperforming larger models on benchmarks. It predicts code edits based on file context and recent diffs, primarily used for enhancing developer productivity via local code assistance.

`1.4B`

⬇️ 2,434 • ❤️ 199 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 26 • 💬 1 • ⭐ 3,286 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 143 • 💬 6 • ⭐ 21,633 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation](https://huggingface.co/papers/2504.08761)**

*Yuxuan Chen, Dewen Guo, Sen Mei et al. (15 authors)*

UltraRAG is a comprehensive RAG toolkit that automates knowledge adaptation across the entire workflow while providing a user-friendly interface for non-coding deployment.

▲ 0 • 💬 0 • ⭐ 3,402 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08761) • [💻 code](https://github.com/OpenBMB/UltraRAG)

---

**[HeartMuLa: A Family of Open Sourced Music Foundation Models](https://huggingface.co/papers/2601.10547)**

*Dongchao Yang, Yuxin Xie, Yuguo Yin et al. (28 authors)*

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.

▲ 36 • 💬 4 • ⭐ 1,823 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10547) • [💻 code](https://github.com/HeartMuLa/heartlib) • [🔗 project](https://heartmula.github.io/)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 126 • 💬 6 • ⭐ 11,659 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[FlashLabs Chroma 1.0: A Real-Time End-to-End Spoken Dialogue Model with Personalized Voice Cloning](https://huggingface.co/papers/2601.11141)**

*Tanyu Chen, Tairan Chen, Kai Shen et al. (7 authors)*

🏢 FlashLabs

Chroma 1.0 enables real-time spoken dialogue with personalized voice cloning through discrete speech representations and interleaved text-audio token scheduling.

▲ 17 • 💬 3 • ⭐ 360 • 8d ago

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

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 2 • 💬 0 • ⭐ 2,386 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[Agentic Reasoning for Large Language Models](https://huggingface.co/papers/2601.12538)**

*Tianxin Wei, Ting-Wei Li, Zhining Liu et al. (29 authors)*

🏢 University of Illinois at Urbana-Champaign

Agentic reasoning redefines large language models as autonomous agents capable of planning, acting, and learning through continuous interaction in dynamic environments across single-agent and multi-agent frameworks.

▲ 166 • 💬 5 • ⭐ 372 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.12538) • [💻 code](https://github.com/weitianxin/Awesome-Agentic-Reasoning)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 10.2k • 🔱 553 • 20h ago

---

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 9.7k • 🔱 1.3k • 21h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 8.9k • 🔱 461 • 3d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 7.5k • 🔱 893 • 1d ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 5.9k • 🔱 1.0k • 22h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 5.2k • 🔱 5.4k • 10h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 4.5k • 🔱 472 • 3h ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 2.8k • 🔱 231 • 1d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.4k • 🔱 340 • 1d ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 200+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 2.4k • 🔱 502 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
