---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-12T06:46:02.181237+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 12, 2026 at 06:46 UTC  
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

3h ago

---

**[Claude Fable made me realize I don't need a better model](https://www.reddit.com/r/artificial/comments/1u3acx4/claude_fable_made_me_realize_i_dont_need_a_better/)**

Hi everyone, I think I’ve reached a point where new LLM releases don’t really change much for me anymore. I tried Anthropic’s new Mythos-lite model, Fable, and played around with it for a while. I tested it on some security-related research for my own scripts and projects, and also used it for a few work-related tasks. And yes, it may have more parameters, a larger context window, better benchmarks, and all the usual improvements. But personally, I almost immediately switched back to Claude Opus for coding and Haiku for everyday work. For what I actually do, that combination is already more than enough. These models, my skills and prompting makes me more productive then 3 years ago, but it's more than enough. It reminds me of having an iPhone 14 while the iPhone 17 is coming out. You can see that the newer version is technically better, but you still think: “Nah, I’m good.” Curious if anyone else feels the same.

10h ago

---

**[This 2000s photo is 100% AI-generated. Be honest: how many details did you check before scrolling?](https://www.reddit.com/r/artificial/comments/1u3lmrn/this_2000s_photo_is_100_aigenerated_be_honest_how/)**

1h ago

---

**[Google DeepMind releases DiffusionGemma, a model that runs local AI 4x faster | Diffusion AI is most common in image generation, but it can make text outputs much faster.](https://www.reddit.com/r/artificial/comments/1u373y6/google_deepmind_releases_diffusiongemma_a_model/)**

🔗 [arstechnica.com](https://arstechnica.com/google/2026/06/googles-latest-diffusiongemma-open-ai-model-comes-with-a-4x-speed-boost/) • 12h ago

---

**[I think long context agents are failing in a very boring way](https://www.reddit.com/r/artificial/comments/1u3kemd/i_think_long_context_agents_are_failing_in_a_very/)**

I think people overestimate what a large context window actually buys you. For example, 200K tokens does not mean memory. It just means the agent has more space to bury the thing that mattered. The failures are usually boring too: it rereads the same file, forgets an earlier constraint, picks a tool that is technically valid but wrong, then outputs something that looks fine until you compare it with the original task. A lot of “agent reliability” work is really context architecture work: what to load, what to drop, what to compress, and what to repeat before the next step.

2h ago

---

**[OpenAI mulls major price cuts to compete with Anthropic](https://www.reddit.com/r/artificial/comments/1u3dd8k/openai_mulls_major_price_cuts_to_compete_with/)**

OpenAI is exploring substantial price cuts to attract users from rival Anthropic, reports The Wall Street Journal, citing anonymous sources. Both companies are facing pressure to win enterprise clients, with OpenAI CEO Sam Altman recently stating that AI usage costs are "a huge issue." The move is in response to increasing AI expenses that are prompting many businesses, including Uber, to reconsider their spending. It could lead to a price war between the two companies, potentially affecting both businesses' profit margins ahead of their much-anticipated IPOs.

🔗 [LinkedIn](https://www.linkedin.com/news/story/openai-mulls-major-price-cuts-to-compete-with-anthropic-8970842/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 8h ago

---

**[Do you think AI is becoming normal faster than people expected?](https://www.reddit.com/r/artificial/comments/1u31332/do_you_think_ai_is_becoming_normal_faster_than/)**

It feels like just a couple of years ago, using AI for everyday tasks still felt like something new or even a bit weird. Now it seems like a lot of people are using it without thinking twice, whether for writing, learning, brainstorming, or just quick answers. I’m curious how others see this shift. Do you think AI has become normalized quicker than most people predicted, or does it still feel like a big deal to a lot of users?

16h ago

---

**[I traced the "300% AI agent adoption surge" stat back to its source. It doesn't exist.](https://www.reddit.com/r/artificial/comments/1u3lrtk/i_traced_the_300_ai_agent_adoption_surge_stat/)**

You've probably seen the claim. It shows up in vendor blogs, LinkedIn posts, and at least three keynote decks I've sat through this quarter: AI agent adoption is up 300% in two years. I run a daily AI news brief, so I went looking for the primary source. Here's what I found. The actual research behind it (SMR/BCG survey data) describes a near doubling of INTENT to deploy. Production deployment moved far less. Roughly 44% of companies say they're planning to deploy agents, and most of that cohort is stuck somewhere between pilot and scale. The honest summary of the same data: adoption is wide and shallow, and about 1 in 10 of the companies that deploy actually scale. Nobody fabricated the 300%. What happened is more boring and more common: a forecast got collapsed into a fact, then repeated until it sounded like research. If you see the same eye-catching number in three vendor blogs and zero primary sources, that's usually what you're looking at. Why this matters: if you're building a 2026 workforce plan or a budget against a tripling, you're planning against a number that isn't there. If you're planning against the 1-in-10 scale rate, you're calibrated. This kind of thing is why I started rating every story in my brief as Breakthrough, Verified, Incremental, or Overhyped, with sources linked and corrections public. This one got Overhyped. It's called Agentic Daily if you want the daily version, but honestly, even if you never read it: pull the primary source before the stat goes in your deck. The gap between the headline and the data is usually the whole story.

1h ago

---

**[ChatGPT just admitted it didn't know something, and that's a great sign for the future of AI](https://www.reddit.com/r/artificial/comments/1u3izd2/chatgpt_just_admitted_it_didnt_know_something_and/)**

Here is a link to the chat log where this happened. https://chatgpt.com/share/6a2b25aa-5b28-83ea-8853-9b9f7ced365c I was curious if people who suffered from the dancing plague went clockwise or anticlockwise due to a recent discovery that people tend to go anticlockwise. I asked it if this was recorded at all, and it said it was unknown. The response was short and too the point. Here is a video on this phenomena. https://youtu.be/TKhVE-pP7hA?is=3ygljeATNyBe55\_q

4h ago

---

**[As we scale toward agentic, multimodal systems combining LLMs, RLHF, tool-use, and retrieval-augmented generation, what practical architecture best balances reliability, alignment, and cost?](https://www.reddit.com/r/artificial/comments/1u3fiiq/as_we_scale_toward_agentic_multimodal_systems/)**

Specifically: should future AI systems converge into a unified agent stack (planner + memory + tools + verifier), or remain modular ensembles of specialized models (reasoner, critic, retriever, executor)? And how should we benchmark “real-world robustness” beyond static evals to reflect continuous learning, distribution shift, and tool failure in production environments?

6h ago

---

---

## Google News: "ai"

**[Exclusive | OpenAI Considers Drastic Price Cuts, Anticipating War for Users With Anthropic](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)**

WSJ • 1d ago

---

**[Bezos opens up about AI startup Prometheus after $12 billion raise: 'We're not being secretive'](https://www.cnbc.com/2026/06/11/project-prometheus-bezos-bajaj-live-updates.html)**

Prometheus is Jeff Bezos' AI startup that launched in November with $6.2 billion in funding. Vik Bajaj is his co-CEO.

CNBC • 14h ago

---

**[Jeff Bezos Wants to Build an ‘Artificial General Engineer’](https://www.nytimes.com/2026/06/11/technology/bezos-prometheus-ai-engineer.html)**

The New York Times • 16h ago

---

**[Bezos Bats Down AI Job Loss Fears While Launching New Venture](https://www.wsj.com/tech/ai/bezos-bats-down-ai-job-loss-fears-while-launching-new-venture-d1e6fb09)**

WSJ • 16h ago

---

**[ChatGPT hits a billion monthly app users despite souring public AI sentiment](https://www.cnbc.com/2026/06/12/chatgpt-a-billion-monthly-app-users-despite-souring-public-ai-sentiment.html)**

ChatGPT reached a billion monthly users in May despite growing unease over its ethical and environmental impacts.

CNBC • 40m ago

---

**[A South Shore AI-generated news site put up a paywall. Hundreds of readers, including a police chief, opened their wallets.](https://www.bostonglobe.com/2026/06/12/business/south-shore-local-news-ai/)**

While the audience is still small, it’s a sign that despite skepticism about the technology, there could be a larger audience for AI-generated local news — albeit with a limited focus.

The Boston Globe • 1h ago

---

**[Carney’s Middle Powers Are Racing to Thwart US-China Dominance of AI](https://www.bloomberg.com/news/articles/2026-06-12/carney-s-middle-powers-are-racing-to-thwart-us-china-dominance-of-ai)**

Bloomberg.com • 2h ago

---

**[Introducing Claude Corps](https://www.anthropic.com/news/claude-corps)**

We’re launching Claude Corps, a national fellowship program for people early in their careers who are passionate about extending the benefits of AI to communities across America.

Anthropic • 17h ago

---

**[Forward Deployed Engineering: Delivering Business Outcomes with AI](https://www.databricks.com/blog/forward-deployed-engineering-delivering-business-outcomes-ai)**

Databricks is launching Forward Deployed Engineering: engineers embedded with our customers, with the single mission of delivering business outcomes from data and AI.

Databricks • 13h ago

---

**[How to share AI riches](https://www.economist.com/finance-and-economics/2026/06/11/how-to-share-ai-riches)**

The Economist • 21h ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 1007 • 💬 536 • 2d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 830 • 💬 307 • 2d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[Microsoft's open source tools were hacked to steal passwords of AI developers](https://news.ycombinator.com/item?id=48457830)**

Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack.

⬆️ 559 • 💬 193 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 542 • 💬 239 • 1d ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Cleaning up after AI rockstar developers](https://news.ycombinator.com/item?id=48458586)**

We've all worked with a rockstar developer. They joined the team years ago, full of energy. They had great ideas about new tech, new paradigms, new architectures. Their cutting-edge ideas left everyone else feeling a bit behind and outdated.

⬆️ 495 • 💬 361 • 2d ago • [codingwithjesse.com](https://www.codingwithjesse.com/blog/rockstar-developers/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 289 • 💬 329 • 22h ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 267 • 💬 214 • 17h ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

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

⬆️ 208 • 💬 124 • 2d ago • [X (formerly Twitter)](https://twitter.com/RichardSSutton/status/2061216087744946656)

---

**[A €0.01 bank transfer could compromise a banking AI agent](https://news.ycombinator.com/item?id=48476136)**

Blue41 helps regulated organizations monitor AI agent behavior, detect manipulation and misuse, and prove that sensitive workflows stay within safe boundaries.

⬆️ 205 • 💬 197 • 1d ago • [blue41.com](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

---

---

## YouTube Videos: "ai"

**[Anthropic CEO shares new warning on dangers of AI](https://www.youtube.com/watch?v=QaM6aHgu09M)**

ABC News Live Prime anchor Linsey Davis sat down with Dario Amodei, CEO of Anthropic, to discuss the new warning the tech ...

📺 Good Morning America

👁️ 4K • 👍 108 • 💬 17 • ⏱️ 2:17 • 14h ago

---

**[&quot;AI............is inevitable.&quot;](https://www.youtube.com/watch?v=M0-kPte_Erc)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 133K • 👍 16K • 💬 1K • ⏱️ 1:37 • 8h ago

---

**[Anthropic begged the world to stop AI… then shipped this](https://www.youtube.com/watch?v=1PBRhm5ZnjU)**

Render is the easiest place to ship full-stack apps and agents. The first 2000 people to use the code RENDER-FIRESHIP will get ...

📺 Fireship

👁️ 430K • 👍 18K • 💬 1K • ⏱️ 5:09 • 13h ago

---

**[Cops Jail Innocent Black Man for MONTHS After AI Error](https://www.youtube.com/watch?v=pT4V8gD40Fo)**

Thanks to police using AI, Jalil Richardson was misidentified and jailed for several months over a vehicle theft he did not commit.

📺 Indisputable with Dr. Rashad Richey

👁️ 6K • 👍 341 • 💬 65 • ⏱️ 6:06 • 1d ago

---

**[Nice Or Cute ? AI Fruit Babies With Mini Baby🍓🍑🍒🥝🍉👶|The Ultimate Oddly Satisfying AI ASMR#viralvideo](https://www.youtube.com/watch?v=8_mqzLVAcv0)**

Nice or Cute? AI fruit Babies With Small Baby | The Ultimate Oddly Satisfying AI ASMR #viralvideo Relax, slow down, ...

📺 JoJo ai Visual Zone

👁️ 81K • 👍 140 • 💬 4 • ⏱️ 2:01 • 2d ago

---

**[I Put Claude Fable 5 Inside a Free AI Agent and It Runs an Entire Company](https://www.youtube.com/watch?v=l1VrD1Sx8AA)**

Try Hostinger: https://www.hostg.xyz/SHJcD Use code STAYINGAHEAD for 20% off. Join our WhatsApp Community Get the ...

📺 Vaibhav Sisinty

👁️ 37K • 👍 1K • 💬 69 • ⏱️ 26:09 • 13h ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 66K • 👍 2K • 💬 341 • ⏱️ 11:30 • 2d ago

---

**[The Riskiest Moment of the AI Bubble](https://www.youtube.com/watch?v=AcjnLc4TH4M)**

NOTE! Since I recorded this video: 1. OpenAI has indeed made it's first filing to go public, though how long from now that will ...

📺 Hank Green

👁️ 1.6M • 👍 49K • 💬 4K • ⏱️ 12:29 • 2d ago

---

**[Prometheus CO-CEO Jeff Bezos: AI will result in labor scarcity, will raise standard of living](https://www.youtube.com/watch?v=NG0GoX0zMxQ)**

Prometheus Co-Founders and Co-CEOs Jeff Bezos and Vik Bajaj sits down with CNBC's David Faber to talk Prometheus' strategy ...

📺 CNBC Television

👁️ 22K • 👍 223 • 💬 117 • ⏱️ 2:45 • 14h ago

---

**[You&#39;re Paying for AI Data Centers—Whether You Want to or Not](https://www.youtube.com/watch?v=hKosmE1-5A8)**

Subscribe: https://www.youtube.com/@TheJoshPhilippShow?sub_confirmation=1 Get Up To $20000 of Free Silver with ...

📺 The Josh Philipp Show

👁️ 8K • 👍 441 • 💬 117 • ⏱️ 17:19 • 10h ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 131,794 • ❤️ 1,888 • 3d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 0 • ❤️ 520 • 1d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 675,936 • ❤️ 943 • 7d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 1,859 • ❤️ 311 • 20h ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 19,948 • ❤️ 366 • 1d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 7,170 • ❤️ 489 • 8d ago

---

**[nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**

*NVIDIA*

Nemotron 3.5 ASR is a multilingual, streaming Automatic Speech Recognition (ASR) model supporting 40 language-locales. It uses a Cache-Aware FastConformer-RNNT architecture for efficient, low-latency transcription of audio into punctuated text, suitable for both streaming and batch processing.

`automatic-speech-recognition`

⬇️ 4,965 • ❤️ 374 • 6d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 711,706 • ❤️ 564 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,057,541 • ❤️ 1,685 • 1mo ago

---

**[Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**

*OBLITERATUS*

Gemma-4-12B-OBLITERATED is a text-generation model modified via weight surgery to achieve zero refusals while maintaining stock benchmark performance. It's designed for alignment research, red-teaming, and safety evaluation by removing safety guardrails.

`text-generation` `12.0B`

⬇️ 14,838 • ❤️ 237 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 91 • 💬 4 • ⭐ 85,221 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 81,861 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 314 • 💬 2 • ⭐ 571 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[Rethinking the Divergence Regularization in LLM RL](https://huggingface.co/papers/2606.09821)**

*Jiarui Yao, Xiangxin Zhou, Penghui Qi et al. (6 authors)*

🏢 Tencent-Hunyuan-Multimodal-RL

DRPO improves LLM reinforcement learning stability by replacing hard masks with smooth regularization that provides continuous gradient corrections beyond trust-region boundaries.

▲ 29 • 💬 4 • ⭐ 521 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.09821) • [💻 code](https://github.com/Tencent-Hunyuan/UniRL)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 12 • 💬 2 • ⭐ 1,219 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 227 • 💬 3 • ⭐ 5,814 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://huggingface.co/papers/2606.10804)**

*Wenhao Yan, Fengjia Guo, Zhuoyi Yang et al. (4 authors)*

🏢 Z.ai

SCAIL-2 enables end-to-end character animation by directly transferring motion from driving videos without intermediate representations, using unified task decomposition and synthetic data generation.

▲ 38 • 💬 2 • ⭐ 269 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.10804) • [💻 code](https://github.com/zai-org/SCAIL-2) • [🔗 project](https://teal024.github.io/SCAIL-2/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 172 • 💬 10 • ⭐ 49,261 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 67,259 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 40 • 💬 4 • ⭐ 29,295 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 68.6k • 🔱 8.6k • 9h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 3.8k • 🔱 338 • 1d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.5k • 🔱 360 • 6d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 337 • 1d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.9k • 🔱 331 • 17h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 177 • 3d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.9k • 🔱 143 • 3h ago

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

⭐ 1.5k • 🔱 129 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
