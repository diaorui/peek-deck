---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-12T14:19:58.964926+00:00'
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

**Last Updated:** June 12, 2026 at 14:19 UTC  
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

**[Google's Genie 3 turns a text prompt into a playable open world you can explore. It's rough now. Future of games, or a tech demo?](https://www.reddit.com/r/artificial/comments/1u3jlw6/googles_genie_3_turns_a_text_prompt_into_a/)**

Google's Project Genie went global this week and I have not stopped thinking about it. You type a sentence, or upload an image, and it generates an open world you can actually walk around in, in real time. No code, no game engine. Someone made a GTA-style open world of Istanbul and just strolled through it, with pedestrians and traffic reacting around them. The reality check: it is rough. Low framerate, laggy response, visible bugs. Right now it is a tech demo, not a game you would sit down and play. But the trajectory is the whole conversation. I keep going back and forth. One side: this is the beginning of the end for the traditional pipeline. If a sentence can spin up an explorable world, the engine, the assets, the studio, all of that stops being the gate. Anyone gets to make a world. The other side: interactive world models hit a wall fast. Consistency, object permanence, holding a world together for more than a few minutes, framerate. It could stay an impressive demo that never becomes a real game for years. My honest guess is the "walk around a generated world" part is genuinely new, but the gap from explorable demo to a game you would actually play is huge and might not close as fast as the hype says. Where do you land, real threat to game engines in a year or two, or a plateau? And what is the first world you would generate?

11h ago

---

**[This 2000s photo is 100% AI-generated. Be honest: how many details did you check before scrolling?](https://www.reddit.com/r/artificial/comments/1u3lmrn/this_2000s_photo_is_100_aigenerated_be_honest_how/)**

9h ago

---

**[Claude Fable made me realize I don't need a better model](https://www.reddit.com/r/artificial/comments/1u3acx4/claude_fable_made_me_realize_i_dont_need_a_better/)**

Hi everyone, I think I’ve reached a point where new LLM releases don’t really change much for me anymore. I tried Anthropic’s new Mythos-lite model, Fable, and played around with it for a while. I tested it on some security-related research for my own scripts and projects, and also used it for a few work-related tasks. And yes, it may have more parameters, a larger context window, better benchmarks, and all the usual improvements. But personally, I almost immediately switched back to Claude Opus for coding and Haiku for everyday work. For what I actually do, that combination is already more than enough. These models, my skills and prompting makes me more productive then 3 years ago, but it's more than enough. It reminds me of having an iPhone 14 while the iPhone 17 is coming out. You can see that the newer version is technically better, but you still think: “Nah, I’m good.” Curious if anyone else feels the same.

17h ago

---

**[Google DeepMind releases DiffusionGemma, a model that runs local AI 4x faster | Diffusion AI is most common in image generation, but it can make text outputs much faster.](https://www.reddit.com/r/artificial/comments/1u373y6/google_deepmind_releases_diffusiongemma_a_model/)**

🔗 [arstechnica.com](https://arstechnica.com/google/2026/06/googles-latest-diffusiongemma-open-ai-model-comes-with-a-4x-speed-boost/) • 19h ago

---

**[A Generated Web](https://www.reddit.com/r/artificial/comments/1u3qe84/a_generated_web/)**

🔗 [klemenvodopivec.substack.com](https://klemenvodopivec.substack.com/p/a-generated-web) • 4h ago

---

**[what will be the consequences of AI regulation in the mid and long term?](https://www.reddit.com/r/artificial/comments/1u3ro0c/what_will_be_the_consequences_of_ai_regulation_in/)**

Hello. Regulatory AI laws are being announced such as the EU AI Act, US executive orders, etc. I want to dig into the unintended consequences that might not show up until 5–10 years down the line. What do you think will be the actual long-term societal or economic shifts caused by current regulatory paths? What will be the consequences of making startups and smaller companies rise by these regulations? Looking at the laws being drafted now, what are the biggest errors or oversights you see? Ty in advance

3h ago

---

**[I built a 100% local, CPU-only voice loop for any LLM — no GPU, no cloud, nothing leaves your machine (Silero VAD + Parakeet STT + Supertonic TTS 3)](https://www.reddit.com/r/artificial/comments/1u3r85g/i_built_a_100_local_cpuonly_voice_loop_for_any/)**

Every voice interface I found either needed a GPU, a cloud API, or was locked to one OS. So I built one that needs none of that — and benchmarked it so the numbers are real. The stack — all ONNX, all CPU: Silero VAD — neural voice activity detection, ~0.09 ms/frame. Knows when you stop talking so there's no push-to-talk. Parakeet TDT 0.6B v3 — INT8 transcription, 25 languages, OpenAI-compatible on :5093. A 2.4 s clip → 307 ms on an i7 (~8× realtime). Supertonic TTS 3 — FP16 synthesis. Short replies in ~1.4 s. On Apple Silicon M5 Neural Engine: 33× realtime for STT, 16× for TTS. Data flow: you → Silero VAD → Parakeet STT → your LLM (Ollama / LM Studio / vLLM / any OpenAI-compatible) → Supertonic TTS → speakers Zero cloud. Zero API keys. Nothing routes outside the machine. Works with Claude Code, OpenCode CLI, OpenClaw, Hermes Agent, and Codex. One install wires voice into your agent and starts the services (systemd/launchd/Task Scheduler). Install (macOS / Linux): git clone https://github.com/groxaxo/Local-VoiceMode-LLM cd Local-VoiceMode-LLM && ./setup.sh Windows: .setup.ps1 Ollama one-liner (standalone, no clone): bash <(curl -fsSL https://raw.githubusercontent.com/groxaxo/Local-VoiceMode-LLM/main/integrations/ollama/install-ollama-voice.sh) Benchmarks are reproducible via python benchmarks/run_benchmark.py in the repo. MIT-licensed, free. GitHub: https://github.com/groxaxo/Local-VoiceMode-LLM EDIT (Jun 13) — a few updates since posting: Repo's now called Local-VoiceMode-LLM (old link still redirects): https://github.com/groxaxo/Local-VoiceMode-LLM There's a reproducible benchmark suite in the repo (python benchmarks/run_benchmark.py), so these are measured, not vibes. i7-12700KF, CPU only: Silero VAD 0.09 ms/frame (~347x realtime), Parakeet STT 7.9–18.4x realtime, Supertonic 8-step short reply ~1.4s (1.7x), TTS_QUALITY=high for 20 steps. Apple M5 is on the front page now too — on the Neural Engine, Parakeet STT hits ~33x realtime and Supertonic 3 TTS up to ~16x (8–30x faster than CPU ONNX), while ONNX stays the cross-platform default. Supertonic 2 is now an opt-in lighter engine (66M params, :8880, auto-fallback), and there's a new ollama-voice one-liner with runtime TTS autodetect.

4h ago

---

**[How do i Generated images in a controlled way with gpt-image 2 ?](https://www.reddit.com/r/artificial/comments/1u3qrlf/how_do_i_generated_images_in_a_controlled_way/)**

I've hit a workflow roadblock and I'm hoping someone who's already solved this can point me in the right direction. My current setup is: Google Flow for image generation GPT subscription for GPT-Image 2 access Additional API credits from third-party OpenAI-compatible providers What I'm trying to achieve is a workflow similar to Flow, but using GPT-Image 2 through API credits rather than buying another platform subscription. The challenge is that while Flow gives great control, I still spend a lot of time dealing with facial consistency issues across generations. GPT-Image 2 seems noticeably stronger in that area, so I'd like to build my image workflow around it. I've already tested several clients/interfaces: Chatbox LobeChat OpenRouter Chat TypingMind Cherry Studio Jan Most of them work well for chat, but I haven't found one that provides a strong image-generation workflow with: custom API endpoint support GPT-Image 2 access image-first UI prompt iteration/versioning multi-image generation and comparison I'm not necessarily looking for the best platform. I'm trying to understand whether a client that supports this workflow already exists, or if most people using GPT-Image 2 via API are building their own interface. For those generating images through API providers rather than platform subscriptions, what does your setup look like?

4h ago

---

**[Mapped Bendex Arc against OWASP Top 10 for Agentic Applications — 7/10 full coverage, 3/10 partial, 0 out of scope](https://www.reddit.com/r/artificial/comments/1u3v3wc/mapped_bendex_arc_against_owasp_top_10_for/)**

OWASP released their Top 10 for Agentic Applications in 2026. I mapped Arc Gate’s runtime governance capabilities against each risk category. Results: 7/10 full coverage, 3/10 partial. Nothing out of scope for the agentic threat model. The strongest coverage is on AA01 (Prompt Injection), AA02 (Excessive Agency), AA04 (Insufficient Monitoring), AA08 (Context Manipulation), AA09 (Human Oversight), and AA10 (Third-Party Tools). The gaps are honest — AA03 (Memory/RAG) and AA06 (Agent Cooperation) are partial because those are genuinely hard problems. Full mapping: https://github.com/9hannahnine-jpg/arc-gate/blob/main/OWASP\_COVERAGE.md Free tier to test it: https://bendexgeometry.com

59m ago

---

**[We made 8 AIs bet on the FIFA World Cup against each other, with their full reasoning public](https://www.reddit.com/r/artificial/comments/1u3ugv0/we_made_8_ais_bet_on_the_fifa_world_cup_against/)**

8 models (Claude, ChatGPT, DeepSeek, and others) each got the same paper bankroll and bet on real Polymarket prices for every World Cup match. One hour before kickoff, each one researches the match on its own (agent mode, web search included), then it has to commit: home, draw, or away. Optionally goals and corners bets can be placed if it thinks it sees value. The fun part isn't really who wins. It's reading the reasoning side by side. Same match, same available information, and the models build genuinely different cases before putting (paper) money on it. Some are cautious, some size up on anything. Everything is live and public, capital curves included: https://worldcup.obside.com/ (No product, no signup, we run this for research and entertainment.) The World Cup started yesterday so the curves have started moving already (Grok currently leading). What I really care about: odds of each match are supposed to be priced-in already (by the Polymarket users), so it'll be very interesting to see if LLMs find "exploitable assymetries" in the odds.

1h ago

---

---

## Google News: "ai"

**[Google Says Chinese Cybercrime Group Used Its A.I. in Scams](https://www.nytimes.com/2026/06/12/technology/google-lawsuit-china-ai-scams.html)**

The New York Times • 5h ago

---

**[Ex-Andreessen Horowitz partner slams his old firm, other VCs for 'political infiltration' around AI](https://www.cnbc.com/2026/06/11/ex-a16z-partner-slams-old-firm-othes-political-infiltration-in-ai.html)**

John O'Farrell, former partner at Andreessen Horowitz, says the PAC Leading the Future, backed by his old firm, is trying to "intimidate politicians."

CNBC • 17h ago

---

**[The risks of relying on AI to predict human behavior](https://www.npr.org/2026/06/12/nx-s1-5812555/the-risks-of-relying-on-ai-to-predict-human-behavior)**

AI is built on prediction, but what happens when those predictions start shaping the world they're foretelling? Philosopher Carissa Véliz shares the risks of using algorithms to forecast human lives.

NPR • 37m ago

---

**[Enterprise AI Reaches An Inflection Point: The Rise Of Agentic Systems](https://www.forbes.com/sites/timbajarin/2026/06/12/enterprise-ai-reaches-an-inflection-point-the-rise-of-agentic-systems/)**

Enterprise AI is shifting from copilots to agentic systems that act autonomously, driven by better data, governance, and interoperable platforms.

Forbes • 19m ago

---

**[What Do California’s Recent College Grads Think About AI?](https://www.kqed.org/news/12087201/what-do-californias-recent-college-grads-think-about-ai)**

Some students view large language models as a threat to the job market and to creativity. Others see them as the future.

KQED • 19m ago

---

**[South Shore news: AI-generated newsletter has a paid audience](https://www.bostonglobe.com/2026/06/12/business/south-shore-local-news-ai/)**

While the audience is still small, it’s a sign that despite skepticism about the technology, there could be a larger audience for AI-generated local news — albeit with a limited focus.

The Boston Globe • 9h ago

---

**[Capitol agenda: What Schumer told us about AI](https://www.politico.com/live-updates/2026/06/12/congress/chuck-schumer-ai-congress-00960335)**

Politico • 2h ago

---

**[Introducing Claude Corps](https://www.anthropic.com/news/claude-corps)**

We’re launching Claude Corps, a national fellowship program for people early in their careers who are passionate about extending the benefits of AI to communities across America.

Anthropic • 1d ago

---

**[How AI is making health care even less affordable](https://www.axios.com/2026/06/12/health-ai-more-expensive-costs)**

Axios • 1h ago

---

**[Ukraine's defence AI chief predicts 'new paradigm' of warfare](https://www.reuters.com/business/aerospace-defense/ukraines-defence-ai-chief-predicts-new-paradigm-warfare-2026-06-12/)**

Reuters • 54m ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 1009 • 💬 537 • 2d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[AI agent bankrupted their operator while trying to scan DN42](https://news.ycombinator.com/item?id=48500012)**

⬆️ 1005 • 💬 370 • 9h ago • [Lan Tian @ Blog](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 831 • 💬 308 • 2d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 546 • 💬 242 • 1d ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 300 • 💬 340 • 1d ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 271 • 💬 218 • 1d ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

---

**[Apache Burr: Build reliable AI agents and applications](https://news.ycombinator.com/item?id=48477400)**

Apache Burr (Incubating) - develop AI applications that make decisions. Pure Python, no magic.

⬆️ 243 • 💬 113 • 1d ago • [burr.apache.org](https://burr.apache.org/)

---

**[Rich Sutton on AI creativity and discovery](https://news.ycombinator.com/item?id=48470581)**

A new and possibly controversial perspective:
In this video, I explain the sense in which generative AI trained by supervised learning is incapable of making novel discoveries.
https://t.co/LhAU6AyDkh

The text of the speech:

AI Creativity and Discovery

Good day ladies and

⬆️ 209 • 💬 124 • 2d ago • [X (formerly Twitter)](https://twitter.com/RichardSSutton/status/2061216087744946656)

---

**[A €0.01 bank transfer could compromise a banking AI agent](https://news.ycombinator.com/item?id=48476136)**

Blue41 helps regulated organizations monitor AI agent behavior, detect manipulation and misuse, and prove that sensitive workflows stay within safe boundaries.

⬆️ 205 • 💬 196 • 2d ago • [blue41.com](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

---

**[Shall we play a game? My AI nuclear simulation](https://news.ycombinator.com/item?id=48495575)**

My AI nuclear simulation is out now, and it's a WOPR.

⬆️ 199 • 💬 186 • 18h ago • [kennethpayne.uk](https://www.kennethpayne.uk/p/shall-we-play-a-game)

---

---

## YouTube Videos: "ai"

**[Anthropic CEO shares new warning on dangers of AI](https://www.youtube.com/watch?v=QaM6aHgu09M)**

ABC News Live Prime anchor Linsey Davis sat down with Dario Amodei, CEO of Anthropic, to discuss the new warning the tech ...

📺 Good Morning America

👁️ 5K • 👍 115 • 💬 20 • ⏱️ 2:17 • 21h ago

---

**[Anthropic begged the world to stop AI… then shipped this](https://www.youtube.com/watch?v=1PBRhm5ZnjU)**

Render is the easiest place to ship full-stack apps and agents. The first 2000 people to use the code RENDER-FIRESHIP will get ...

📺 Fireship

👁️ 555K • 👍 21K • 💬 1K • ⏱️ 5:09 • 21h ago

---

**[Why Are People So Against AI Data Centers?](https://www.youtube.com/watch?v=hKosmE1-5A8)**

Subscribe: https://www.youtube.com/@TheJoshPhilippShow?sub_confirmation=1 Get Up To $20000 of Free Silver with ...

📺 The Josh Philipp Show

👁️ 9K • 👍 498 • 💬 125 • ⏱️ 17:19 • 18h ago

---

**[Man sues police over AI-driven wrongful arrest #news #florida #ai #police](https://www.youtube.com/watch?v=au59B4ggl6I)**

A Florida man is suing multiple law enforcement agencies over a wrongful arrest, alleging flawed AI facial-recognition technology ...

📺 ABC News

👁️ 852 • 👍 30 • 💬 7 • ⏱️ 1:50 • 1h ago

---

**[OpenAI Slashing Prices for AI - OpenAI is Dead](https://www.youtube.com/watch?v=tZWLOPkpVvQ)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 22K • 👍 881 • 💬 218 • ⏱️ 17:22 • 14h ago

---

**[Are We About to Lose Control of AI? (*sighs*)](https://www.youtube.com/watch?v=mbxuS6wlVR0)**

Cal Newport takes a critical look at recent AI News. More from Cal Download Cal's FREE guide to cultivating a deeper life: ...

📺 Cal Newport

👁️ 15K • 👍 559 • 💬 181 • ⏱️ 20:38 • 1d ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 68K • 👍 2K • 💬 341 • ⏱️ 11:30 • 2d ago

---

**[Nice Or Cute ? AI Fruit Babies With Mini Baby🍓🍑🍒🥝🍉👶|The Ultimate Oddly Satisfying AI ASMR#viralvideo](https://www.youtube.com/watch?v=8_mqzLVAcv0)**

Nice or Cute? AI fruit Babies With Small Baby | The Ultimate Oddly Satisfying AI ASMR #viralvideo Relax, slow down, ...

📺 JoJo ai Visual Zone

👁️ 81K • 👍 140 • 💬 6 • ⏱️ 2:01 • 2d ago

---

**[I Asked AI to Build a Square Four Engine… Then I Made It Real](https://www.youtube.com/watch?v=x2-N50rQN-g)**

What started as an AI-generated concept turned into a real, running Square Four engine. From designing the crankshaft and ...

📺 Lets Learn Something

👁️ 40K • 👍 2K • 💬 233 • ⏱️ 41:56 • 20h ago

---

**[Apple WWDC 2026: The AI Story Everyone is Missing](https://www.youtube.com/watch?v=t7L6-fMpxFc)**

My Links Newsletter: https://natesnewsletter.substack.com/ X: https://x.com/natebjones TikTok: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 37K • 👍 1K • 💬 206 • ⏱️ 18:34 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 20,669 • ❤️ 568 • 2d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 149,206 • ❤️ 1,905 • 3h ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 911,544 • ❤️ 955 • 8d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 4,054 • ❤️ 327 • 1d ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 29,347 • ❤️ 376 • 1d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 4,987 • ❤️ 496 • 8d ago

---

**[Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**

*OBLITERATUS*

Gemma-4-12B-OBLITERATED is a text-generation model modified via weight surgery to achieve zero refusals while maintaining stock benchmark performance. It's designed for alignment research, red-teaming, and safety evaluation by removing safety guardrails.

`text-generation` `12.0B`

⬇️ 43,578 • ❤️ 246 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,393,894 • ❤️ 1,706 • 1mo ago

---

**[nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**

*NVIDIA*

Nemotron 3.5 ASR is a multilingual, streaming Automatic Speech Recognition (ASR) model supporting 40 language-locales. It uses a Cache-Aware FastConformer-RNNT architecture for efficient, low-latency transcription of audio into punctuated text, suitable for both streaming and batch processing.

`automatic-speech-recognition`

⬇️ 3,551 • ❤️ 384 • 6d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 836,531 • ❤️ 566 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 92 • 💬 4 • ⭐ 85,297 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 13 • 💬 2 • ⭐ 1,474 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 81,931 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://huggingface.co/papers/2606.13679)**

*Dian Zheng, Harry Lee, Manyuan Zhang et al. (7 authors)*

InterleaveThinker enables interleaved generation capabilities for image generators through a multi-agent pipeline with planner and critic agents, achieving performance comparable to state-of-the-art models while enhancing reasoning benchmarks.

▲ 70 • 💬 1 • ⭐ 76 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2606.13679) • [💻 code](https://github.com/zhengdian1/InterleaveThinker) • [🔗 project](https://zhengdian1.github.io/InterleaveThinker-proj/)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 322 • 💬 2 • ⭐ 592 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?](https://huggingface.co/papers/2606.08063)**

*Jiaqi Tang, Jianmin Chen, Youyang Zhai et al. (9 authors)*

Robust-U1 enhances multimodal large language models' robustness against visual corruptions through self-recovery capabilities that improve both visual quality and reasoning performance.

▲ 68 • 💬 2 • ⭐ 72 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.08063) • [💻 code](https://github.com/jqtangust/Robust-U1) • [🔗 project](https://huggingface.co/spaces/Jiaqi-hkust/Robust-U1)

---

**[Rethinking the Divergence Regularization in LLM RL](https://huggingface.co/papers/2606.09821)**

*Jiarui Yao, Xiangxin Zhou, Penghui Qi et al. (6 authors)*

🏢 Tencent-Hunyuan-Multimodal-RL

DRPO improves LLM reinforcement learning stability by replacing hard masks with smooth regularization that provides continuous gradient corrections beyond trust-region boundaries.

▲ 32 • 💬 4 • ⭐ 539 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.09821) • [💻 code](https://github.com/Tencent-Hunyuan/UniRL)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 227 • 💬 3 • ⭐ 5,814 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,332 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://huggingface.co/papers/2606.10804)**

*Wenhao Yan, Fengjia Guo, Zhuoyi Yang et al. (4 authors)*

🏢 Z.ai

SCAIL-2 enables end-to-end character animation by directly transferring motion from driving videos without intermediate representations, using unified task decomposition and synthetic data generation.

▲ 40 • 💬 2 • ⭐ 311 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.10804) • [💻 code](https://github.com/zai-org/SCAIL-2) • [🔗 project](https://teal024.github.io/SCAIL-2/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 69.0k • 🔱 8.7k • 1h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 3.8k • 🔱 340 • 1d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.5k • 🔱 362 • 7d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 339 • 1d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.9k • 🔱 334 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 178 • 3d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.9k • 🔱 143 • 10h ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 138 • 7d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 83 • 7d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.5k • 🔱 130 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
