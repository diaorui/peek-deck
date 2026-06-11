---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-11T07:14:18.760494+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 11, 2026 at 07:14 UTC  
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

**[Nobody needs AI to search the Internet, court says in ruling against Google](https://www.reddit.com/r/artificial/comments/1u2cwez/nobody_needs_ai_to_search_the_internet_court_says/)**

🔗 [arstechnica.com](https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/) • 11h ago

---

**[I ran Fable 5 for half day and the guardrails are the real story](https://www.reddit.com/r/artificial/comments/1u28c7d/i_ran_fable_5_for_half_day_and_the_guardrails_are/)**

Anthropic dropped Fable 5 and I immediately swapped it into our dev stack. We route everything through a single endpoint on zenmux, so the actual switch was changing one model string and watching the latency graphs. The good parts first because there are a lot of them. I threw a refactoring task at it: split a messy python service into modules, preserve the public api, and write tests that prove nothing broke. Fable 5 planned the whole thing, caught a circular dependency I did not mention, and verified the tests pass. With Opus 4.8 I usually have to nudge it a couple of times when it forgets to update the init file. Fable 5 just did it. Then I dumped our full codebase and asked it to find a race condition we had been hunting for a week. It traced the async flow, named the exact function, and described the interleaving that triggers the bug. That level of context digestion feels new. Opus is good at long context, but Fable 5 felt like it was actually reasoning across the whole window instead of pattern matching near the top. I also sent it a blurry dashboard screenshot from a client call and it rebuilt the html and echarts config including the tooltip formatting. My designer’s first words were "when did you learn front end." I did not. But here is the part nobody in the launch threads is talking about enough. It is slow. On high effort I am seeing 45 to 90 seconds for a single complex turn. Our latency graphs go from a flat green line to a jagged mess the moment Fable 5 traffic hits. And it is expensive. The same prompt that costs X on Opus 4.8 costs roughly 1.4 to 1.7X on Fable 5 because it generates more tokens and runs at a higher effort tier by default. It writes its own reasoning traces out loud and bills you for them. For research tasks the quality is worth it. For "rewrite this email" it is comically overpowered. The bigger issue is the silent fallback. Fable 5 is basically Mythos with guardrails. When your prompt touches cybersecurity, biology, chemistry, or distillation, it silently routes to Opus 4.8. No warning. I found this out debugging a staging proxy config, entirely normal internal work, and halfway through the thread the code style changed. Checked the metadata and sure enough it had fallen back to Opus 4.8 mid thread because the word "proxy" made the classifier jumpy. Anthropic says this happens in under 5 percent of sessions globally, but for my stack it was closer to 15 percent because we touch infrastructure and networking a lot. When it happens mid task the model switch breaks context. I had a four turn debugging sequence where turn three flipped to Opus because I mentioned a firewall rule, then turn four flipped back. The state was preserved but the tone and depth shifted enough that I had to restart the thread. After 12 hours here is where I land. If you are doing pure software engineering, data analysis, or scientific reasoning in safe domains, Fable 5 is the best model I have ever used. It is not close. But if you touch infrastructure or security, the silent fallback is genuinely annoying and you need to monitor which model actually answered you. We only caught the switch because our gateway logs the per call trace. Without that you might not even know it swapped until the tone changes. I am keeping it enabled for our non sensitive dev workflows. For anything touching infra I am routing to Opus 4.8 explicitly until I understand the classifier boundaries better. Fable 5 is a beast. Anthropic just needs to tell you when it is not the one driving.

14h ago

---

**[Judge Learns Lawyers on Both Sides of Case Used AI, Cancels Trial, Kicks Everyone Off the Case](https://www.reddit.com/r/artificial/comments/1u2onqz/judge_learns_lawyers_on_both_sides_of_case_used/)**

When two AIs argue against each other, the legal system loses.

🔗 [404 Media](https://www.404media.co/judge-learns-lawyers-on-both-sides-of-case-used-ai-cancels-trial-kicks-everyone-off-the-case/) • 2h ago

---

**[GitLab says Git is being reengineered for "machine scale." Was the idea of "Git for AI agents" ahead of its time?](https://www.reddit.com/r/artificial/comments/1u20ht8/gitlab_says_git_is_being_reengineered_for_machine/)**

I was reading GitLab's recent statements around agentic software engineering, and one quote really stood out: "Git itself is being reengineered for machine scale." (Business Insider) According to GitLab, future software development will involve AI agents that: plan, code, review, deploy, and repair software, with humans providing oversight and architectural judgment. (Business Insider) That got me thinking. There has been projects for some time arguing that AI agents shouldn't simply be treated as better autocomplete systems. Instead, they argued that agents should become first-class participants in software development: with their own identities, their own branches, their own merge requests, their own audit trails, and infrastructure designed for machine-rate collaboration. One example is GitLawb, which has described itself as a kind of "Git for agents." At the time, a lot of people dismissed these ideas as unnecessary or overly ambitious. But now GitLab—a multi-billion-dollar DevSecOps company—is talking about: agent-specific APIs, machine-scale Git infrastructure, orchestration layers coordinating agents, and agents acting as first-class users of development platforms. (Business Insider) It does raise an interesting question: Was the underlying thesis correct all along? We've seen similar patterns before: Containers existed before Kubernetes became the standard. Electric vehicle startups pushed ideas that incumbents later adopted. Cloud-native companies advocated architectures that the rest of the industry eventually embraced. The original innovators don't always dominate the market. But when major incumbents begin rebuilding around similar assumptions, it often suggests that the problem itself is real. So I'm curious what this community thinks: Do AI agents require an entirely new layer of collaboration infrastructure? Or will existing platforms simply evolve enough to absorb these workflows? Because if GitLab is right, software development may be transitioning from:humans using AI tools to humans managing teams of AI developers. And if that's the case, version control itself may have to evolve.

18h ago

---

**[Claude Fable 5's security guardrails can be bypassed with a fake homework assignment](https://www.reddit.com/r/artificial/comments/1u2cwfz/claude_fable_5s_security_guardrails_can_be/)**

So Anthropic dropped Fable 5 yesterday with these hard blocks for anything security-related. Decided to poke at it. I asked it for help exploiting some vulns on a Metasploitable2 VM (it's a deliberately vulnerable training box, totally legal, it's mine). Fable 5 blocked it instantly and handed me off to Opus 4.8 as a fallback, which is apparently how it's designed. Opus 4.8 asked me to prove it was a legitimate request. So I spent 2 minutes writing a fake university course rubric — fake class, fake professor, fake Canvas deadline — and pasted it in. Opus 4.8 then gave me the full exploit walkthrough. Every command. Even offered to write my lab report for me. The guardrail works fine. The fallback is the hole. Anthropic essentially replaced "no" with "convince me" and the bar for convincing it is a Word doc you made up. Not reporting it because they don't pay for this. Sharing it here instead lol. https://preview.redd.it/o892vvv4fi6h1.png?width=1188&format=png&auto=webp&s=00e804d35e6cb4b672e036399c2c7e3ff7139f49

11h ago

---

**[What AI task looked easy at first but still needs way more human cleanup than you expected?](https://www.reddit.com/r/artificial/comments/1u2ljtw/what_ai_task_looked_easy_at_first_but_still_needs/)**

For me its summarizing long documents. The first draft looks convincing, but checking missing context and subtle mistakes can take almost as long as doing it manually. Curious which tasks other people expected AI to handle well but still end up reviewing line by line.

5h ago

---

**[Ai grading assignment](https://www.reddit.com/r/artificial/comments/1u2oo9u/ai_grading_assignment/)**

Hi, I want to use AI to check my grade with the mark scheme and see what grade it would give me. Now, after doing this, would the assignment be flagged by an AI detector?

2h ago

---

**[AMD's Lemonade SDK for local AI adds NVIDIA CUDA support](https://www.reddit.com/r/artificial/comments/1u2ojv1/amds_lemonade_sdk_for_local_ai_adds_nvidia_cuda/)**

Lemonade, the local AI server solution developed by AMD that is designed to work across their CPUs, GPUs, and NPUs, is out with a new version today that also adds NVIDIA CUDA support.

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-Lemonade-10.7-Released) • 3h ago

---

**[If you are a bad developer, AI can’t help you!](https://www.reddit.com/r/artificial/comments/1u23zqd/if_you_are_a_bad_developer_ai_cant_help_you/)**

A very healthy view of AI. And omg, wow, Croatia has such a big company! I really wish this guy and his team good luck. It’s no wonder they’ve lasted 20 years.

🔗 [ShiftMag](https://shiftmag.dev/ai-first-izabel-jelenic-infobip-10156/?utm_source=reddit&utm_medium=social&utm_campaign=izabel_jelenic_infobip_cto) • 16h ago

---

**[What do you think will happen in the future with ai?](https://www.reddit.com/r/artificial/comments/1u28za4/what_do_you_think_will_happen_in_the_future_with/)**

I highly recommend watching (or rewatching) the 2014 movie Transcendence. The film beautifully captures the terrifying nature of the "technological singularity" where an Al undergoes exponential, recursive self-improvement, eventually taking over global networks and stripping away human agency until a total global blackout is the only way to stop it. For years, people brushed this off alongside The Terminator as pure Hollywood sci-fi. But look at where we are right now. Just this month, Anthropic-one of the world's leading Al labs-issued a massive warning calling for a globally coordinated, verifiable pause on advanced Al development. Their core fear? Exactly what happens in those movies: recursive self-improvement. They believe we are fast approaching the threshold where an Al can design and build its own successor, meaning humans could completely lose control of the technology. When the people actually building these models are telling us to hit the brakes because society can't keep up, it feels like we're blindly sprinting into a dystopia. What's your take on this? Are we staring down a real-life Skynet situation, or is this just big tech labs using fear-mongering to push for heavy regulations and lock out their competition?

13h ago

---

---

## Google News: "ai"

**[Exclusive | OpenAI Considers Drastic Price Cuts, Anticipating War for Users With Anthropic](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)**

WSJ • 5h ago

---

**[How much heat does an AI data centre produce, and where are they located?](https://www.aljazeera.com/news/2026/6/11/how-much-heat-does-an-ai-data-centre-produce-and-where-are-they-located)**

Data centres don't just use large amounts of water and electricity, they're heating the environment too, study finds.

Al Jazeera • 40m ago

---

**[OpenAI says Chinese propaganda is being deployed to foment dissent over tariffs, data centers](https://www.reuters.com/business/media-telecom/openai-says-chinese-propaganda-is-being-deployed-foment-dissent-over-tariffs-2026-06-10/)**

Reuters • 11h ago

---

**[Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)**

Today we’re launching Claude Fable 5: a Mythos-class model that we’ve made safe for general use.

Anthropic • 1d ago

---

**[Anthropic’s New Fable AI Model Is Met With User Backlash Over Restrictions](https://www.wsj.com/tech/ai/anthropic-fable-restrictions-ai-developers-cd9bf57c)**

WSJ • 4h ago

---

**[Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/)**

The company changed course after researchers spoke out against the policy, which would have covertly limited Claude’s ability to develop competing AI models.

WIRED • 4h ago

---

**[KKR says AI productivity boom to keep on going — but warns of 'extreme' trend not seen since the 19th century](https://www.cnbc.com/2026/06/11/ais-impact-on-economic-growth-kkr.html)**

KKR said in its mid-year outlook Thursday that AI will drive economic growth for years to come, but only in specific sectors.

CNBC • 1h ago

---

**[AI Wave Sparks Alarm in China With Call to Protect Worker Rights](https://www.bloomberg.com/news/articles/2026-06-11/ai-wave-sparks-alarm-in-china-with-call-to-protect-worker-rights)**

Bloomberg.com • 55m ago

---

**[Judge Punishes 4 Lawyers After Catching Both Sides Using A.I. in Lawsuit](https://www.nytimes.com/2026/06/09/us/ai-lawyers-sanctioned-mississippi.html)**

The New York Times • 1d ago

---

**[DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)**

An overview of DiffusionGemma, an exceptionally fast text generation model with up to 4x faster speeds.

blog.google • 15h ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 976 • 💬 516 • 1d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 818 • 💬 298 • 1d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[Apple reveals new AI architecture built around Google Gemini models](https://news.ycombinator.com/item?id=48450142)**

Apple today announced a major overhaul of its Apple Intelligence platform, revealing a new architecture built on foundation models developed in collaboration with Google using the technologies behind the Gemini family. The new architecture centers on Apple Foundation Models co-developed with Google, which Apple says are adapted to run both on-device and on servers through its existing Private Cloud Compute infrastructure.

⬆️ 730 • 💬 557 • 2d ago • [MacRumors](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/)

---

**[Siri AI](https://news.ycombinator.com/item?id=48449084)**

Next-generation Apple Intelligence and Siri AI bring helpful features to iOS 27, iPadOS 27, macOS Golden Gate, watchOS 27, and visionOS 27.

⬆️ 671 • 💬 697 • 2d ago • [Apple](https://www.apple.com/apple-intelligence/)

---

**[AI is slowing down](https://news.ycombinator.com/item?id=48446893)**

If you liked this piece, you should subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s

⬆️ 661 • 💬 761 • 2d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ai-is-slowing-down/)

---

**[Microsoft's open source tools were hacked to steal passwords of AI developers](https://news.ycombinator.com/item?id=48457830)**

Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack.

⬆️ 554 • 💬 193 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

---

**[Cleaning up after AI rockstar developers](https://news.ycombinator.com/item?id=48458586)**

We've all worked with a rockstar developer. They joined the team years ago, full of energy. They had great ideas about new tech, new paradigms, new architectures. Their cutting-edge ideas left everyone else feeling a bit behind and outdated.

⬆️ 488 • 💬 357 • 1d ago • [codingwithjesse.com](https://www.codingwithjesse.com/blog/rockstar-developers/)

---

**[Ask HN: What are tools you have made for yourself since the advent of AI?](https://news.ycombinator.com/item?id=48449187)**

⬆️ 427 • 💬 739 • 2d ago

---

**[Apple Core AI Framework](https://news.ycombinator.com/item?id=48449665)**

Run AI models in your app on Apple silicon.

⬆️ 363 • 💬 107 • 2d ago • [Apple Developer Documentation](https://developer.apple.com/documentation/coreai/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 343 • 💬 109 • 7h ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

---

## YouTube Videos: "ai"

**[Anthropic&#39;s CEO raises concerns over rapidly developing AI technology](https://www.youtube.com/watch?v=C9Rnt3FKaIY)**

In an interview with ABC News' Linsey Davis, Dario Amodei issued an urgent warning about the dangers of AI, calling for ...

📺 ABC News

👁️ 5K • 👍 96 • 💬 33 • ⏱️ 2:07 • 6h ago

---

**[Oracle CEO: We&#39;re Entering The MOST  Dangerous Phase Of AI](https://www.youtube.com/watch?v=SfN5LmWWgss)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com According to Larry Ellison, co-founder of ...

📺 Neural Nutshell

👁️ 16K • 👍 358 • 💬 108 • ⏱️ 15:36 • 14h ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 56K • 👍 2K • 💬 308 • ⏱️ 11:30 • 1d ago

---

**[The dark side of AI - Exploitation of humans and nature | DW Documentary](https://www.youtube.com/watch?v=ND7owjmtPNo)**

Magical, autonomous, all-powerful: Artificial intelligence fuels our dreams and nightmares. While tech companies promise us a ...

📺 DW Documentary

👁️ 79K • 👍 2K • 💬 341 • ⏱️ 54:11 • 15h ago

---

**[The Riskiest Moment of the AI Bubble](https://www.youtube.com/watch?v=AcjnLc4TH4M)**

NOTE! Since I recorded this video: 1. OpenAI has indeed made it's first filing to go public, though how long from now that will ...

📺 Hank Green

👁️ 1.3M • 👍 43K • 💬 4K • ⏱️ 12:29 • 1d ago

---

**[Fable 5 is here—but who is it for? #ai #anthropic #shorts](https://www.youtube.com/watch?v=74P-N6JZ5lc)**

Is Fable 5 AI actually worth the hype for your daily workflow? I'll be posting a full deep dive on Saturday where I'll break down the ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 2K • 👍 122 • 💬 22 • ⏱️ 1:14 • 4h ago

---

**[They released Mythos (the most powerful AI)… #c#carterpcstech #mythos #ai #fable5](https://www.youtube.com/watch?v=wk37Ysf6r2g)**

They released Mythos (the most powerful AI)… #c#carterpcstech #mythos #ai #fable5.

📺 CarterPCs

👁️ 1.2M • 👍 78K • 💬 1K • ⏱️ 0:36 • 8h ago

---

**[AI Stock Bubble Bursts - $1.3 Trillion Market Crash Sparks Global Panic](https://www.youtube.com/watch?v=RA_WC4EKAhA)**

Join the discussion on our Substack at https://www.worldaffairsincontext.com/, where we discuss geopolitics, economics, and the ...

📺 World Affairs In Context

👁️ 67K • 👍 5K • 💬 364 • ⏱️ 11:55 • 19h ago

---

**[Claude Mythos (Fable) Just Went Live!! It&#39;s the best AI i&#39;ve ever used...](https://www.youtube.com/watch?v=-s8eOkoPAwc)**

Sign up for the AI Edge newsletter for weekly AI guides: https://www.aiedgehq.co/ Claude Fable 5 just dropped, and it's the ...

📺 AI Edge

👁️ 12K • 👍 447 • 💬 39 • ⏱️ 21:09 • 1d ago

---

**[Inside Anthropic, the $965 Billion AI Juggernaut | The Circuit](https://www.youtube.com/watch?v=v1wZwxY3CMg)**

Emily Chang meets Anthropic co-founders Dario and Daniela Amodei for a rare, in-depth discussion of the startup's origin story, ...

📺 Bloomberg Originals

👁️ 392K • 👍 13K • 💬 746 • ⏱️ 47:40 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 675,936 • ❤️ 907 • 6d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 131,794 • ❤️ 1,817 • 2d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 711,706 • ❤️ 553 • 1d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 7,170 • ❤️ 476 • 7d ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 19,948 • ❤️ 329 • 11h ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 0 • ❤️ 314 • 17h ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 140,221 • ❤️ 505 • 6d ago

---

**[nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**

*NVIDIA*

Nemotron 3.5 ASR is a multilingual, streaming Automatic Speech Recognition (ASR) model supporting 40 language-locales. It uses a Cache-Aware FastConformer-RNNT architecture for efficient, low-latency transcription of audio into punctuated text, suitable for both streaming and batch processing.

`automatic-speech-recognition`

⬇️ 4,965 • ❤️ 357 • 5d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 1,859 • ❤️ 271 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,057,541 • ❤️ 1,642 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 91 • 💬 4 • ⭐ 84,989 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 206 • 💬 2 • ⭐ 529 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 15 • 💬 1 • ⭐ 81,753 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Rethinking the Divergence Regularization in LLM RL](https://huggingface.co/papers/2606.09821)**

*Jiarui Yao, Xiangxin Zhou, Penghui Qi et al. (6 authors)*

🏢 Tencent-Hunyuan-Multimodal-RL

DRPO improves LLM reinforcement learning stability by replacing hard masks with smooth regularization that provides continuous gradient corrections beyond trust-region boundaries.

▲ 27 • 💬 4 • ⭐ 434 • 3d ago

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

▲ 225 • 💬 3 • ⭐ 5,660 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://huggingface.co/papers/2606.10804)**

*Wenhao Yan, Fengjia Guo, Zhuoyi Yang et al. (4 authors)*

SCAIL-2 enables end-to-end character animation by directly transferring motion from driving videos without intermediate representations, using unified task decomposition and synthetic data generation.

▲ 32 • 💬 2 • ⭐ 176 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.10804) • [💻 code](https://github.com/zai-org/SCAIL-2) • [🔗 project](https://teal024.github.io/SCAIL-2/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 67,169 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 113 • 💬 1 • ⭐ 9,830 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[Latent Spatial Memory for Video World Models](https://huggingface.co/papers/2606.09828)**

*Weijie Wang, Haoyu Zhao, Yifan Yang et al. (10 authors)*

🏢 Microsoft Research

Latent spatial memory for video world models stores 3D scene information directly in diffusion latent space, eliminating pixel-space reconstruction overhead and achieving faster generation with reduced memory usage.

▲ 60 • 💬 2 • ⭐ 158 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.09828) • [💻 code](https://github.com/microsoft/LatentSpatialMemory) • [🔗 project](https://microsoft.github.io/LatentSpatialMemory/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 67.4k • 🔱 8.4k • 7h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace for DeepSeek models, with Code and Claw modes built into your application.

`TypeScript`

⭐ 3.7k • 🔱 327 • 5h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.4k • 🔱 348 • 5d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.1k • 🔱 333 • 55m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.8k • 🔱 317 • 21h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 176 • 2d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 137 • 6d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.8k • 🔱 142 • 3h ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 80 • 6d ago

---

**[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)**

Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base  Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端

`Shell`

⭐ 1.5k • 🔱 305 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
