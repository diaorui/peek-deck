---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-11T16:03:07.674210+00:00'
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

**Last Updated:** June 11, 2026 at 16:03 UTC  
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

**[Which AI agent are you?](https://www.reddit.com/r/artificial/comments/1u31cep/which_ai_agent_are_you/)**

Seven questions, five personas: Orchestrator, Architect, Explorer, Closer, or Guardian? Find your AI agent persona and your ideal starter team. No signup.

🔗 [What Is Agentic AI](https://whatisagenticai.net/quiz/) • 1h ago

---

**[Nobody needs AI to search the Internet, court says in ruling against Google](https://www.reddit.com/r/artificial/comments/1u2cwez/nobody_needs_ai_to_search_the_internet_court_says/)**

🔗 [arstechnica.com](https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/) • 20h ago

---

**[Do you think AI is becoming normal faster than people expected?](https://www.reddit.com/r/artificial/comments/1u31332/do_you_think_ai_is_becoming_normal_faster_than/)**

It feels like just a couple of years ago, using AI for everyday tasks still felt like something new or even a bit weird. Now it seems like a lot of people are using it without thinking twice, whether for writing, learning, brainstorming, or just quick answers. I’m curious how others see this shift. Do you think AI has become normalized quicker than most people predicted, or does it still feel like a big deal to a lot of users?

1h ago

---

**[What if AI's biggest limitation isn't reasoning, but the inability to accumulate experience?](https://www.reddit.com/r/artificial/comments/1u2z66y/what_if_ais_biggest_limitation_isnt_reasoning_but/)**

Everyone talks about reasoning, agents, and larger models. But the more I learn about AI systems, the more I think we're missing something fundamental: AI doesn't accumulate experience the way humans do. A senior engineer isn't valuable only because of raw intelligence. They're valuable because years of experience have shaped how they think. They're valuable because they've spent years building mental models, learning from failures, recognizing patterns, updating beliefs, and connecting knowledge across thousands of experiences. That accumulated experience becomes a competitive advantage. Modern AI systems are different. They can solve difficult problems, write code, and explain complex concepts, yet most of what they "know" remains largely fixed after training. New information is often handled through context windows, retrieval systems, databases, or retraining pipelines rather than being integrated into a continuously evolving understanding of the world. This creates an interesting question: Can intelligence continue to scale if experience doesn't? Humans become more useful over time because experience compounds. An AI that could reliably learn from interactions, update its worldview, resolve contradictions, remember what matters, forget what doesn't, and improve without catastrophic forgetting might represent a larger leap than another increase in parameter count. Maybe the next frontier isn't making AI smarter. Maybe it's making AI capable of growth. Do you think future breakthroughs will come primarily from better reasoning models, or from systems that can continuously learn from experience?

2h ago

---

**[Judge Learns Lawyers on Both Sides of Case Used AI, Cancels Trial, Kicks Everyone Off the Case](https://www.reddit.com/r/artificial/comments/1u2onqz/judge_learns_lawyers_on_both_sides_of_case_used/)**

When two AIs argue against each other, the legal system loses.

🔗 [404 Media](https://www.404media.co/judge-learns-lawyers-on-both-sides-of-case-used-ai-cancels-trial-kicks-everyone-off-the-case/) • 11h ago

---

**[I ran Fable 5 for half day and the guardrails are the real story](https://www.reddit.com/r/artificial/comments/1u28c7d/i_ran_fable_5_for_half_day_and_the_guardrails_are/)**

Anthropic dropped Fable 5 and I immediately swapped it into our dev stack. We route everything through a single endpoint on zenmux, so the actual switch was changing one model string and watching the latency graphs. The good parts first because there are a lot of them. I threw a refactoring task at it: split a messy python service into modules, preserve the public api, and write tests that prove nothing broke. Fable 5 planned the whole thing, caught a circular dependency I did not mention, and verified the tests pass. With Opus 4.8 I usually have to nudge it a couple of times when it forgets to update the init file. Fable 5 just did it. Then I dumped our full codebase and asked it to find a race condition we had been hunting for a week. It traced the async flow, named the exact function, and described the interleaving that triggers the bug. That level of context digestion feels new. Opus is good at long context, but Fable 5 felt like it was actually reasoning across the whole window instead of pattern matching near the top. I also sent it a blurry dashboard screenshot from a client call and it rebuilt the html and echarts config including the tooltip formatting. My designer’s first words were "when did you learn front end." I did not. But here is the part nobody in the launch threads is talking about enough. It is slow. On high effort I am seeing 45 to 90 seconds for a single complex turn. Our latency graphs go from a flat green line to a jagged mess the moment Fable 5 traffic hits. And it is expensive. The same prompt that costs X on Opus 4.8 costs roughly 1.4 to 1.7X on Fable 5 because it generates more tokens and runs at a higher effort tier by default. It writes its own reasoning traces out loud and bills you for them. For research tasks the quality is worth it. For "rewrite this email" it is comically overpowered. The bigger issue is the silent fallback. Fable 5 is basically Mythos with guardrails. When your prompt touches cybersecurity, biology, chemistry, or distillation, it silently routes to Opus 4.8. No warning. I found this out debugging a staging proxy config, entirely normal internal work, and halfway through the thread the code style changed. Checked the metadata and sure enough it had fallen back to Opus 4.8 mid thread because the word "proxy" made the classifier jumpy. Anthropic says this happens in under 5 percent of sessions globally, but for my stack it was closer to 15 percent because we touch infrastructure and networking a lot. When it happens mid task the model switch breaks context. I had a four turn debugging sequence where turn three flipped to Opus because I mentioned a firewall rule, then turn four flipped back. The state was preserved but the tone and depth shifted enough that I had to restart the thread. After 12 hours here is where I land. If you are doing pure software engineering, data analysis, or scientific reasoning in safe domains, Fable 5 is the best model I have ever used. It is not close. But if you touch infrastructure or security, the silent fallback is genuinely annoying and you need to monitor which model actually answered you. We only caught the switch because our gateway logs the per call trace. Without that you might not even know it swapped until the tone changes. I am keeping it enabled for our non sensitive dev workflows. For anything touching infra I am routing to Opus 4.8 explicitly until I understand the classifier boundaries better. Fable 5 is a beast. Anthropic just needs to tell you when it is not the one driving.

22h ago

---

**[The gap between decision and exécution](https://www.reddit.com/r/artificial/comments/1u30wjh/the_gap_between_decision_and_exécution/)**

I’ve been thinking about a support automation story I read recently. A team replaced a simple rules engine with an LLM classifier. The model was around 92% accurate. Sounds good. Until you realize that at 100 tickets a day, that’s roughly 8 mistakes every day. The interesting part wasn’t the accuracy though. It was what happened when the model was wrong. Nobody could explain why a ticket was classified a certain way. Nobody could point to a specific rule. Nobody could quickly fix the behavior. The team eventually started reviewing every classification manually. The automation was still running, but the trust was gone. That got me thinking. A lot of discussion around AI agents focuses on making decisions better. Better prompts. Better models. Better reasoning. But I rarely see people discussing what happens after the decision. How is the decision verified? How is it audited? How do you know an action should actually be executed? Maybe the biggest challenge for AI agents isn’t getting from 92% to 96%. Maybe it’s building systems that people can trust when things go wrong. Curious how others are thinking about this.

1h ago

---

**[We captured the network traffic of ChatGPT, Gemini and DeepSeek to see how each defines a "source" — they're three completely different mechanisms](https://www.reddit.com/r/artificial/comments/1u2xdmg/we_captured_the_network_traffic_of_chatgpt_gemini/)**

Disclosure upfront: I'm the founder of an AI-visibility company, so this research scratches our own itch. Our domain was excluded from all counts before analysis. Not linking anything in the post. We wanted to answer a simple question: when an AI assistant shows you "sources," what is that, technically? So we opened devtools on the web clients of ChatGPT, Gemini, and DeepSeek, and ran the same 4 queries 10 times through each system. What we found: ChatGPT streams the answer over SSE and attaches citations as url_citation objects with start_ix/end_ix — character offsets into the generated text (UTF-16 code units, so emoji and CJK break your parsing if you count bytes). A citation is bound to a specific fragment of the answer, not the answer as a whole. Gemini runs on Google's batchexecute/JSPB transport — protobuf-as-JSON-arrays where fields have positions, not names. Next to each cited URL there's a family of short obfuscated fields. Our working hypotheses (not confirmed by Google docs): rs ≈ reliability score for the domain, ls ≈ last-seen date, GK ≈ character range (functional analog of ChatGPT's offsets). The interesting part isn't the exact decoding — it's that Gemini ships internal per-domain trust signals alongside every source. DeepSeek is the most transparent: a plain search_results[] array attached to the sub-queries it decomposes your question into. No offsets, no hidden fields. And what they actually cite is just as different: ChatGPT favored arXiv + Wikipedia (one arXiv paper got cited in 10/10 runs), Gemini favors big SaaS/marketing domains and — fun detail — never cited a single Google property in our runs, DeepSeek lives on press-release wires and news aggregators, including Chinese-language sources the other two never touched. Bonus finding: we compared all of this against Google/Bing top-10 for the same queries. URL-level overlap: 3.3% (4 matches out of 120 SERP positions). All four matches were Bing-side. Google: zero. Caveats: 4 queries from one B2B category, N=10 per system (±15–20 pp), single-day snapshot, field decodings are hypotheses from traffic analysis. Happy to answer anything about the methodology. If anyone has captured different field names in their own sessions, I'd love to compare.

3h ago

---

**[OpenAI Filed for IPO at $852B as Anthropic Beats It to Market and Price Cuts Loom](https://www.reddit.com/r/artificial/comments/1u302rd/openai_filed_for_ipo_at_852b_as_anthropic_beats/)**

OpenAI filed a confidential S-1 on June 8 targeting a $852B valuation and September listing. It is considering major token price cuts as Anthropic filed at $965B one week earlier.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/openai-ipo-852-billion-confidential-s1-anthropic-token-price-cuts/) • 1h ago

---

**[Microsoft continues global rollout of Copilot's smiley AI companion Mico, now available in 40 countries](https://www.reddit.com/r/artificial/comments/1u2uzmm/microsoft_continues_global_rollout_of_copilots/)**

Mico for Copilot was introduced at the tail end of last year, exclusive to the United States. Now it's available around the world.

🔗 [PC Guide](https://www.pcguide.com/news/microsoft-continues-global-rollout-of-copilots-smiley-ai-companion-mico-now-available-in-40-countries/) • 5h ago

---

---

## Google News: "ai"

**[Exclusive | OpenAI Considers Drastic Price Cuts, Anticipating War for Users With Anthropic](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)**

WSJ • 14h ago

---

**[Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/)**

The company changed course after researchers spoke out against the policy, which would have covertly limited Claude’s ability to develop competing AI models.

WIRED • 12h ago

---

**[Anthropic CEO: Government should have power to block dangerous AI deployments](https://thehill.com/policy/technology/5919784-ai-regulation-anthropic-ceo/)**

The Hill • 1h ago

---

**[Why the Real A.I. Threat Is in the Back Office](https://www.nytimes.com/2026/06/10/business/economy/back-office-workers-ai.html)**

The New York Times • 1d ago

---

**[Bezos opens up about AI startup Prometheus after $12 billion raise: 'We're not being secretive'](https://www.cnbc.com/2026/06/11/project-prometheus-bezos-bajaj-live-updates.html)**

Prometheus is Jeff Bezos' AI startup that launched in November with $6.2 billion in funding. Vik Bajaj is his co-CEO.

CNBC • 15m ago

---

**[Bezos Bats Down AI Job Loss Fears While Launching New Venture](https://www.wsj.com/tech/ai/bezos-bats-down-ai-job-loss-fears-while-launching-new-venture-d1e6fb09)**

WSJ • 2h ago

---

**[Jeff Bezos Prometheus AI startup raises $12 billion Series B](https://qz.com/jeff-bezos-prometheus-ai-startup-raises-12-billion-061126)**

The industrial AI company, which Bezos co-leads with Vik Bajaj, has hired about 150 people and is building AI systems for engineering and manufacturing

qz.com • 30m ago

---

**[The YC Benchmark: Building A Company From Scratch For The AI Era](https://www.forbes.com/sites/keithferrazzi/2026/06/11/the-yc-benchmark-building-a-company-from-scratch-for-the-ai-era/)**

The YC Benchmark shows why leaders must learn from AI-native founders designing companies, work, and human-agent systems from scratch.

Forbes • 7m ago

---

**[How NEC's AI and oral delivery system are redefining personalized cancer therapy](https://www.fiercebiotech.com/sponsored/how-necs-ai-and-oral-delivery-system-are-redefining-personalized-cancer-therapy)**

Fierce Biotech • 8m ago

---

**[AI is sparking a jobs boom — just not for newbies](https://www.cnn.com/2026/06/11/business/ai-jobs-work)**

As Corporate America scrambles to fill artificial intelligence jobs, junior workers are getting left behind.

CNN • 6h ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 994 • 💬 527 • 1d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 826 • 💬 301 • 1d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[Apple reveals new AI architecture built around Google Gemini models](https://news.ycombinator.com/item?id=48450142)**

Apple today announced a major overhaul of its Apple Intelligence platform, revealing a new architecture built on foundation models developed in collaboration with Google using the technologies behind the Gemini family. The new architecture centers on Apple Foundation Models co-developed with Google, which Apple says are adapted to run both on-device and on servers through its existing Private Cloud Compute infrastructure.

⬆️ 730 • 💬 559 • 2d ago • [MacRumors](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/)

---

**[Siri AI](https://news.ycombinator.com/item?id=48449084)**

Next-generation Apple Intelligence and Siri AI bring helpful features to iOS 27, iPadOS 27, macOS Golden Gate, watchOS 27, and visionOS 27.

⬆️ 672 • 💬 698 • 2d ago • [Apple](https://www.apple.com/apple-intelligence/)

---

**[Microsoft's open source tools were hacked to steal passwords of AI developers](https://news.ycombinator.com/item?id=48457830)**

Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack.

⬆️ 558 • 💬 193 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 522 • 💬 230 • 15h ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Cleaning up after AI rockstar developers](https://news.ycombinator.com/item?id=48458586)**

We've all worked with a rockstar developer. They joined the team years ago, full of energy. They had great ideas about new tech, new paradigms, new architectures. Their cutting-edge ideas left everyone else feeling a bit behind and outdated.

⬆️ 492 • 💬 360 • 2d ago • [codingwithjesse.com](https://www.codingwithjesse.com/blog/rockstar-developers/)

---

**[Ask HN: What are tools you have made for yourself since the advent of AI?](https://news.ycombinator.com/item?id=48449187)**

⬆️ 431 • 💬 750 • 2d ago

---

**[Apple Core AI Framework](https://news.ycombinator.com/item?id=48449665)**

Run AI models in your app on Apple silicon.

⬆️ 363 • 💬 107 • 2d ago • [Apple Developer Documentation](https://developer.apple.com/documentation/coreai/)

---

**[Apache Burr: Build reliable AI agents and applications](https://news.ycombinator.com/item?id=48477400)**

Apache Burr (Incubating) - develop AI applications that make decisions. Pure Python, no magic.

⬆️ 234 • 💬 111 • 1d ago • [burr.apache.org](https://burr.apache.org/)

---

---

## YouTube Videos: "ai"

**[How to Make Your First AI Movie (Full Guide)](https://www.youtube.com/watch?v=fs5S867VQzg)**

Create Your First AI Movie with Higgsfield https://youricreates.com/first-movie ✓ Generate top tier AI video prompts for free: ...

📺 Youri van Hofwegen

👁️ 4K • ⏱️ 17:03 • 1h ago

---

**[Something Is Going Wrong with AI in China—and Now Xi Jinping Is Trying to Slow It Down](https://www.youtube.com/watch?v=F3PZFrzajVc)**

Go to https://surfshark.com/economik or use code ECONOMIK at checkout to get 4 extra months of Surfshark VPN! Check out our ...

📺 VisualEconomik EN

👁️ 27K • 👍 1K • 💬 229 • ⏱️ 16:06 • 1d ago

---

**[AI That’s Too Dangerous For You? What we learned from S.A.T.A.N](https://www.youtube.com/watch?v=UE_vuadQrJ0)**

Learn more about Zero-Day Exploit here → https://ibm.biz/~2lAtr9uM2 AI is uncovering vulnerabilities faster than ever before.

📺 IBM Technology

👁️ 3K • 👍 205 • 💬 36 • ⏱️ 12:59 • 5h ago

---

**[The Riskiest Moment of the AI Bubble](https://www.youtube.com/watch?v=AcjnLc4TH4M)**

NOTE! Since I recorded this video: 1. OpenAI has indeed made it's first filing to go public, though how long from now that will ...

📺 Hank Green

👁️ 1.4M • 👍 46K • 💬 4K • ⏱️ 12:29 • 2d ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 59K • 👍 2K • 💬 318 • ⏱️ 11:30 • 1d ago

---

**[Anthropic&#39;s CEO raises concerns over rapidly developing AI technology](https://www.youtube.com/watch?v=C9Rnt3FKaIY)**

In an interview with ABC News' Linsey Davis, Dario Amodei issued an urgent warning about the dangers of AI, calling for ...

📺 ABC News

👁️ 9K • 👍 136 • 💬 60 • ⏱️ 2:07 • 15h ago

---

**[The dark side of AI - Exploitation of humans and nature | DW Documentary](https://www.youtube.com/watch?v=ND7owjmtPNo)**

Magical, autonomous, all-powerful: Artificial intelligence fuels our dreams and nightmares. While tech companies promise us a ...

📺 DW Documentary

👁️ 106K • 👍 3K • 💬 433 • ⏱️ 54:11 • 1d ago

---

**[Claude Mythos (Fable) Just Went Live!! It&#39;s the best AI i&#39;ve ever used...](https://www.youtube.com/watch?v=-s8eOkoPAwc)**

Sign up for the AI Edge newsletter for weekly AI guides: https://www.aiedgehq.co/ Claude Fable 5 just dropped, and it's the ...

📺 AI Edge

👁️ 13K • 👍 474 • 💬 43 • ⏱️ 21:09 • 1d ago

---

**[Grok AI Finally Reveals How Ancient Egyptians Cut Granite — The Proof Is Shocking!](https://www.youtube.com/watch?v=-AiFyHr0jPc)**

Discover the fascinating claims surrounding Grok AI's analysis of ancient granite cutting techniques in Egypt's Aswan Quarry.

📺 The Ultimate Finding

👁️ 372K • 👍 3K • 💬 203 • ⏱️ 29:08 • 2d ago

---

**[Honest Trailers | A.I. Artificial Intelligence (2001)](https://www.youtube.com/watch?v=Oovq_p-WFuQ)**

Steven Spielberg's got a new original sci-fi movie coming out with Disclosure Day, so we took a look back at his films and one ...

📺 Screen Junkies

👁️ 264K • 👍 12K • 💬 1K • ⏱️ 8:26 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 131,794 • ❤️ 1,852 • 2d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 675,936 • ❤️ 930 • 7d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 0 • ❤️ 421 • 1d ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 19,948 • ❤️ 344 • 20h ago

---

**[nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**

*NVIDIA*

Nemotron 3.5 ASR is a multilingual, streaming Automatic Speech Recognition (ASR) model supporting 40 language-locales. It uses a Cache-Aware FastConformer-RNNT architecture for efficient, low-latency transcription of audio into punctuated text, suitable for both streaming and batch processing.

`automatic-speech-recognition`

⬇️ 4,965 • ❤️ 365 • 5d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 711,706 • ❤️ 558 • 2d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 1,859 • ❤️ 299 • 6h ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 7,170 • ❤️ 481 • 7d ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 140,221 • ❤️ 513 • 7d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,057,541 • ❤️ 1,663 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 91 • 💬 4 • ⭐ 85,117 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 243 • 💬 2 • ⭐ 551 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 15 • 💬 1 • ⭐ 81,823 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Rethinking the Divergence Regularization in LLM RL](https://huggingface.co/papers/2606.09821)**

*Jiarui Yao, Xiangxin Zhou, Penghui Qi et al. (6 authors)*

🏢 Tencent-Hunyuan-Multimodal-RL

DRPO improves LLM reinforcement learning stability by replacing hard masks with smooth regularization that provides continuous gradient corrections beyond trust-region boundaries.

▲ 28 • 💬 4 • ⭐ 498 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.09821) • [💻 code](https://github.com/Tencent-Hunyuan/UniRL)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 172 • 💬 10 • ⭐ 49,239 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 225 • 💬 3 • ⭐ 5,702 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://huggingface.co/papers/2606.10804)**

*Wenhao Yan, Fengjia Guo, Zhuoyi Yang et al. (4 authors)*

🏢 Z.ai

SCAIL-2 enables end-to-end character animation by directly transferring motion from driving videos without intermediate representations, using unified task decomposition and synthetic data generation.

▲ 34 • 💬 2 • ⭐ 220 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.10804) • [💻 code](https://github.com/zai-org/SCAIL-2) • [🔗 project](https://teal024.github.io/SCAIL-2/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 67,228 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Toward Generalist Autonomous Research via Hypothesis-Tree Refinement](https://huggingface.co/papers/2606.11926)**

*Jiajie Jin, Yuyang Hu, Kai Qiu et al. (18 authors)*

🏢 NLPIR Lab @ RUC

An AI framework called Arbor enables autonomous scientific research by combining strategic coordination, isolated hypothesis testing, and a persistent knowledge tree to iteratively improve research outcomes across multiple domains.

▲ 63 • 💬 3 • ⭐ 63 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2606.11926) • [💻 code](https://github.com/RUC-NLPIR/Arbor) • [🔗 project](https://ruc-nlpir.github.io/Arbor/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 115 • 💬 1 • ⭐ 9,854 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 68.0k • 🔱 8.5k • 4m ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace for DeepSeek models, with Code and Claw modes built into your application.

`TypeScript`

⭐ 3.8k • 🔱 332 • 14h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.5k • 🔱 353 • 6d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 334 • 9h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.8k • 🔱 322 • 2h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 176 • 2d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.9k • 🔱 143 • 28m ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 138 • 6d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 81 • 6d ago

---

**[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)**

Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base  Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端

`Shell`

⭐ 1.5k • 🔱 310 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
