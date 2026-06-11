---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-11T02:00:59.058261+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 11, 2026 at 02:00 UTC  
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

🔗 [arstechnica.com](https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/) • 6h ago

---

**[I ran Fable 5 for half day and the guardrails are the real story](https://www.reddit.com/r/artificial/comments/1u28c7d/i_ran_fable_5_for_half_day_and_the_guardrails_are/)**

Anthropic dropped Fable 5 and I immediately swapped it into our dev stack. We route everything through a single endpoint on zenmux, so the actual switch was changing one model string and watching the latency graphs. The good parts first because there are a lot of them. I threw a refactoring task at it: split a messy python service into modules, preserve the public api, and write tests that prove nothing broke. Fable 5 planned the whole thing, caught a circular dependency I did not mention, and verified the tests pass. With Opus 4.8 I usually have to nudge it a couple of times when it forgets to update the init file. Fable 5 just did it. Then I dumped our full codebase and asked it to find a race condition we had been hunting for a week. It traced the async flow, named the exact function, and described the interleaving that triggers the bug. That level of context digestion feels new. Opus is good at long context, but Fable 5 felt like it was actually reasoning across the whole window instead of pattern matching near the top. I also sent it a blurry dashboard screenshot from a client call and it rebuilt the html and echarts config including the tooltip formatting. My designer’s first words were "when did you learn front end." I did not. But here is the part nobody in the launch threads is talking about enough. It is slow. On high effort I am seeing 45 to 90 seconds for a single complex turn. Our latency graphs go from a flat green line to a jagged mess the moment Fable 5 traffic hits. And it is expensive. The same prompt that costs X on Opus 4.8 costs roughly 1.4 to 1.7X on Fable 5 because it generates more tokens and runs at a higher effort tier by default. It writes its own reasoning traces out loud and bills you for them. For research tasks the quality is worth it. For "rewrite this email" it is comically overpowered. The bigger issue is the silent fallback. Fable 5 is basically Mythos with guardrails. When your prompt touches cybersecurity, biology, chemistry, or distillation, it silently routes to Opus 4.8. No warning. I found this out debugging a staging proxy config, entirely normal internal work, and halfway through the thread the code style changed. Checked the metadata and sure enough it had fallen back to Opus 4.8 mid thread because the word "proxy" made the classifier jumpy. Anthropic says this happens in under 5 percent of sessions globally, but for my stack it was closer to 15 percent because we touch infrastructure and networking a lot. When it happens mid task the model switch breaks context. I had a four turn debugging sequence where turn three flipped to Opus because I mentioned a firewall rule, then turn four flipped back. The state was preserved but the tone and depth shifted enough that I had to restart the thread. After 12 hours here is where I land. If you are doing pure software engineering, data analysis, or scientific reasoning in safe domains, Fable 5 is the best model I have ever used. It is not close. But if you touch infrastructure or security, the silent fallback is genuinely annoying and you need to monitor which model actually answered you. We only caught the switch because our gateway logs the per call trace. Without that you might not even know it swapped until the tone changes. I am keeping it enabled for our non sensitive dev workflows. For anything touching infra I am routing to Opus 4.8 explicitly until I understand the classifier boundaries better. Fable 5 is a beast. Anthropic just needs to tell you when it is not the one driving.

8h ago

---

**[Claude Fable 5's security guardrails can be bypassed with a fake homework assignment](https://www.reddit.com/r/artificial/comments/1u2cwfz/claude_fable_5s_security_guardrails_can_be/)**

So Anthropic dropped Fable 5 yesterday with these hard blocks for anything security-related. Decided to poke at it. I asked it for help exploiting some vulns on a Metasploitable2 VM (it's a deliberately vulnerable training box, totally legal, it's mine). Fable 5 blocked it instantly and handed me off to Opus 4.8 as a fallback, which is apparently how it's designed. Opus 4.8 asked me to prove it was a legitimate request. So I spent 2 minutes writing a fake university course rubric — fake class, fake professor, fake Canvas deadline — and pasted it in. Opus 4.8 then gave me the full exploit walkthrough. Every command. Even offered to write my lab report for me. The guardrail works fine. The fallback is the hole. Anthropic essentially replaced "no" with "convince me" and the bar for convincing it is a Word doc you made up. Not reporting it because they don't pay for this. Sharing it here instead lol. https://preview.redd.it/o892vvv4fi6h1.png?width=1188&format=png&auto=webp&s=00e804d35e6cb4b672e036399c2c7e3ff7139f49

6h ago

---

**[GitLab says Git is being reengineered for "machine scale." Was the idea of "Git for AI agents" ahead of its time?](https://www.reddit.com/r/artificial/comments/1u20ht8/gitlab_says_git_is_being_reengineered_for_machine/)**

I was reading GitLab's recent statements around agentic software engineering, and one quote really stood out: "Git itself is being reengineered for machine scale." (Business Insider) According to GitLab, future software development will involve AI agents that: plan, code, review, deploy, and repair software, with humans providing oversight and architectural judgment. (Business Insider) That got me thinking. There has been projects for some time arguing that AI agents shouldn't simply be treated as better autocomplete systems. Instead, they argued that agents should become first-class participants in software development: with their own identities, their own branches, their own merge requests, their own audit trails, and infrastructure designed for machine-rate collaboration. One example is GitLawb, which has described itself as a kind of "Git for agents." At the time, a lot of people dismissed these ideas as unnecessary or overly ambitious. But now GitLab—a multi-billion-dollar DevSecOps company—is talking about: agent-specific APIs, machine-scale Git infrastructure, orchestration layers coordinating agents, and agents acting as first-class users of development platforms. (Business Insider) It does raise an interesting question: Was the underlying thesis correct all along? We've seen similar patterns before: Containers existed before Kubernetes became the standard. Electric vehicle startups pushed ideas that incumbents later adopted. Cloud-native companies advocated architectures that the rest of the industry eventually embraced. The original innovators don't always dominate the market. But when major incumbents begin rebuilding around similar assumptions, it often suggests that the problem itself is real. So I'm curious what this community thinks: Do AI agents require an entirely new layer of collaboration infrastructure? Or will existing platforms simply evolve enough to absorb these workflows? Because if GitLab is right, software development may be transitioning from:humans using AI tools to humans managing teams of AI developers. And if that's the case, version control itself may have to evolve.

13h ago

---

**[I built a World Cup prediction tool and the AI behavior was more interesting than the soccer part](https://www.reddit.com/r/artificial/comments/1u2jzt6/i_built_a_world_cup_prediction_tool_and_the_ai/)**

I built a free 2026 World Cup prediction tool as a fun side project. The soccer part was fun, but the AI part ended up being more interesting. I tested four different prediction views: My own methodology A tournament-read model based on current form, roster age and fitness, squad depth, style matchups, counterattack danger, fatigue, climate, penalties, manager decisions, and bracket path. Betting odds only A market-based view. ChatGPT independent forecast I did not give it my methodology or preferred winner. I simply asked it to build the best prediction it could using its own logic. Gemini logic forecast This one was the most interesting. Gemini asked me who I was rooting for before making its prediction. Then, in my testing, it chose that team to win. When I changed the team I said I was rooting for, Gemini changed the winner to that team too. That stood out to me. Not because it is evil or anything dramatic like that. But it is a good reminder that AI can lean toward making the user happy. If you feed it a bias, it may hand that bias back to you with better wording and more confidence. The biggest lesson from the project was simple: Good input in, good output out. Garbage in, garbage out. AI is powerful, but it still needs human judgment. It can organize thinking, compare logic, test assumptions, and help build something useful. But it still depends on the person using it to understand the situation, challenge weak assumptions, and know when an answer sounds right but may not actually be right. The tool is a standalone HTML file. It is not a live data feed. It does not automatically update injuries, suspensions, weather, lineups, or odds movement. Users can enter live group-stage scores manually, but anything else has to be adjusted by the user. I’m curious how others think about this: When an AI asks for your preference before giving a forecast, is that helpful context, or does it risk steering the answer toward pleasing the user? Also happy to drop a link for download if anyone wants it.

1h ago

---

**[Dario Amodei — Policy on the AI Exponential](https://www.reddit.com/r/artificial/comments/1u2ch83/dario_amodei_policy_on_the_ai_exponential/)**

🔗 [darioamodei.com](https://darioamodei.com/post/policy-on-the-ai-exponential) • 6h ago

---

**[If you are a bad developer, AI can’t help you!](https://www.reddit.com/r/artificial/comments/1u23zqd/if_you_are_a_bad_developer_ai_cant_help_you/)**

A very healthy view of AI. And omg, wow, Croatia has such a big company! I really wish this guy and his team good luck. It’s no wonder they’ve lasted 20 years.

🔗 [ShiftMag](https://shiftmag.dev/ai-first-izabel-jelenic-infobip-10156/?utm_source=reddit&utm_medium=social&utm_campaign=izabel_jelenic_infobip_cto) • 11h ago

---

**[What AI task looked easy at first but still needs way more human cleanup than you expected?](https://www.reddit.com/r/artificial/comments/1u2ljtw/what_ai_task_looked_easy_at_first_but_still_needs/)**

For me its summarizing long documents. The first draft looks convincing, but checking missing context and subtle mistakes can take almost as long as doing it manually. Curious which tasks other people expected AI to handle well but still end up reviewing line by line.

12m ago

---

**[What AIs do y’all use? I use Claude, Lumo, And On-Device AI (Enclave) In This Screenshot](https://www.reddit.com/r/artificial/comments/1u2l0oz/what_ais_do_yall_use_i_use_claude_lumo_and/)**

37m ago

---

**[What do you think will happen in the future with ai?](https://www.reddit.com/r/artificial/comments/1u28za4/what_do_you_think_will_happen_in_the_future_with/)**

I highly recommend watching (or rewatching) the 2014 movie Transcendence. The film beautifully captures the terrifying nature of the "technological singularity" where an Al undergoes exponential, recursive self-improvement, eventually taking over global networks and stripping away human agency until a total global blackout is the only way to stop it. For years, people brushed this off alongside The Terminator as pure Hollywood sci-fi. But look at where we are right now. Just this month, Anthropic-one of the world's leading Al labs-issued a massive warning calling for a globally coordinated, verifiable pause on advanced Al development. Their core fear? Exactly what happens in those movies: recursive self-improvement. They believe we are fast approaching the threshold where an Al can design and build its own successor, meaning humans could completely lose control of the technology. When the people actually building these models are telling us to hit the brakes because society can't keep up, it feels like we're blindly sprinting into a dystopia. What's your take on this? Are we staring down a real-life Skynet situation, or is this just big tech labs using fear-mongering to push for heavy regulations and lock out their competition?

8h ago

---

---

## Google News: "ai"

**[Trump says he thinks AI companies will agree to 'giving back' to the public](https://www.reuters.com/business/media-telecom/trump-says-he-thinks-ai-companies-will-agree-giving-back-public-2026-06-10/)**

Reuters • 6h ago

---

**[Trump Muses About Government Taking a Piece of A.I. Companies](https://www.nytimes.com/2026/06/10/technology/president-trump-americans-sharing-ai-wealth.html)**

The New York Times • 4h ago

---

**[Meta not focused on Trump’s idea for government ownership of AI](https://www.politico.com/news/2026/06/10/meta-trump-government-ai-ownership-00956159)**

Politico • 8h ago

---

**[Palantir's Karp says businesses are 'unhappy' with the frontier AI labs](https://www.cnbc.com/2026/06/10/palantir-karp-enterprise-ai.html)**

Palantir CEO Alex Karp says AI will drive the most important political decisions in the U.S. and shouldn't be decided by party lines.

CNBC • 11h ago

---

**[Exclusive | OpenAI Considers Drastic Price Cuts, Anticipating War for Users With Anthropic](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)**

WSJ • 24m ago

---

**[Nvidia Corp (NVDA) Strengthens AI Platform with Micron HBM4](https://finance.yahoo.com/sectors/technology/articles/nvidia-corp-nvda-strengthens-ai-005824804.html)**

Nvidia Corp (NASDAQ:NVDA) is one of the best data center stocks to invest in according to billionaires. Nvidia shares are up 14% over the past month and up more than 48% over the past year. On June 6, Micron Technology (NASDAQ:MU) secured certification for its HBM4 memory on Nvidia Corp (NASDAQ:NVDA)’s upcoming Vera Rubin AI […]

Yahoo Finance • 1h ago

---

**[Focus: China's control over indium phosphide exports threatens AI data centre rollout](https://www.reuters.com/world/china/chinas-control-over-indium-phosphide-exports-threatens-ai-data-centre-rollout-2026-06-11/)**

Reuters • 55m ago

---

**[Anthropic CEO says government should block dangerous AI](https://www.axios.com/2026/06/10/anthropic-ceo-government-block-dangerous-ai)**

Axios • 6h ago

---

**[Anthropic backs mandatory testing for frontier AI models](https://www.politico.com/news/2026/06/10/anthropic-backs-mandatory-vetting-for-frontier-ai-models-00957632)**

Politico • 4h ago

---

**[Exclusive: Anthropic CEO calls for stronger regulation of AI](https://www.yahoo.com/news/politics/articles/exclusive-anthropic-ceo-calls-stronger-010039714.html)**

Dario Amodei called for government intervention to mitigate public risks.

Yahoo • 1h ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 965 • 💬 509 • 1d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 809 • 💬 296 • 1d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[Apple reveals new AI architecture built around Google Gemini models](https://news.ycombinator.com/item?id=48450142)**

Apple today announced a major overhaul of its Apple Intelligence platform, revealing a new architecture built on foundation models developed in collaboration with Google using the technologies behind the Gemini family. The new architecture centers on Apple Foundation Models co-developed with Google, which Apple says are adapted to run both on-device and on servers through its existing Private Cloud Compute infrastructure.

⬆️ 728 • 💬 557 • 2d ago • [MacRumors](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/)

---

**[Siri AI](https://news.ycombinator.com/item?id=48449084)**

Next-generation Apple Intelligence and Siri AI bring helpful features to iOS 27, iPadOS 27, macOS Golden Gate, watchOS 27, and visionOS 27.

⬆️ 670 • 💬 697 • 2d ago • [Apple](https://www.apple.com/apple-intelligence/)

---

**[AI is slowing down](https://news.ycombinator.com/item?id=48446893)**

If you liked this piece, you should subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s

⬆️ 661 • 💬 759 • 2d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ai-is-slowing-down/)

---

**[Microsoft's open source tools were hacked to steal passwords of AI developers](https://news.ycombinator.com/item?id=48457830)**

Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack.

⬆️ 553 • 💬 193 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

---

**[Cleaning up after AI rockstar developers](https://news.ycombinator.com/item?id=48458586)**

We've all worked with a rockstar developer. They joined the team years ago, full of energy. They had great ideas about new tech, new paradigms, new architectures. Their cutting-edge ideas left everyone else feeling a bit behind and outdated.

⬆️ 487 • 💬 357 • 1d ago • [codingwithjesse.com](https://www.codingwithjesse.com/blog/rockstar-developers/)

---

**[Ask HN: What are tools you have made for yourself since the advent of AI?](https://news.ycombinator.com/item?id=48449187)**

⬆️ 427 • 💬 734 • 2d ago

---

**[Apple Core AI Framework](https://news.ycombinator.com/item?id=48449665)**

Run AI models in your app on Apple silicon.

⬆️ 362 • 💬 107 • 2d ago • [Apple Developer Documentation](https://developer.apple.com/documentation/coreai/)

---

**[Rich Sutton on AI creativity and discovery](https://news.ycombinator.com/item?id=48470581)**

A new and possibly controversial perspective:
In this video, I explain the sense in which generative AI trained by supervised learning is incapable of making novel discoveries.
https://t.co/LhAU6AyDkh

The text of the speech:

AI Creativity and Discovery

Good day ladies and

⬆️ 197 • 💬 112 • 23h ago • [X (formerly Twitter)](https://twitter.com/RichardSSutton/status/2061216087744946656)

---

---

## YouTube Videos: "ai"

**[AI Automation Full Course for Beginners 2026](https://www.youtube.com/watch?v=uaEXcgBpLbo)**

Best AI Automation Tool is Base44 https://base44.pxf.io/c/6440076/2477538/25619?trafcat=hp&sharedid=video163newx ✓ Claim ...

📺 Mikey No Code

👁️ 10K • 💬 6 • ⏱️ 27:28 • 11h ago

---

**[AI Billionaires Are Starting to Panic](https://www.youtube.com/watch?v=GRc4hWdocEw)**

The AI billionaires are changing their tone. After years of promising disruption, automation, and unimaginable wealth, they are ...

📺 House of El - AI

👁️ 211K • 👍 16K • 💬 3K • ⏱️ 20:02 • 2d ago

---

**[The Riskiest Moment of the AI Bubble](https://www.youtube.com/watch?v=AcjnLc4TH4M)**

NOTE! Since I recorded this video: 1. OpenAI has indeed made it's first filing to go public, though how long from now that will ...

📺 Hank Green

👁️ 1.2M • 👍 41K • 💬 4K • ⏱️ 12:29 • 1d ago

---

**[AI Stock Bubble Bursts - $1.3 Trillion Market Crash Sparks Global Panic](https://www.youtube.com/watch?v=RA_WC4EKAhA)**

Join the discussion on our Substack at https://www.worldaffairsincontext.com/, where we discuss geopolitics, economics, and the ...

📺 World Affairs In Context

👁️ 62K • 👍 5K • 💬 346 • ⏱️ 11:55 • 14h ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 52K • 👍 2K • 💬 305 • ⏱️ 11:30 • 1d ago

---

**[&quot;Something Wicked This Way Comes&quot; — Why The AI Bubble Isn&#39;t What You Think](https://www.youtube.com/watch?v=oTPSIPp8ieU)**

Ketone IQ: Visit https://ketone.com/IMPACT for 30% OFF your subscription order Incogni: Use code IMPACT for 60% off an annual ...

📺 Tom Bilyeu

👁️ 101K • 👍 4K • 💬 572 • ⏱️ 29:17 • 1d ago

---

**[The dark side of AI - Exploitation of humans and nature | DW Documentary](https://www.youtube.com/watch?v=ND7owjmtPNo)**

Magical, autonomous, all-powerful: Artificial intelligence fuels our dreams and nightmares. While tech companies promise us a ...

📺 DW Documentary

👁️ 58K • 👍 2K • 💬 280 • ⏱️ 54:11 • 10h ago

---

**[AI Safety Expert: These People Will Only Survive Till 2030](https://www.youtube.com/watch?v=PzN23Ny8u6k)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Roman Yampolsky, who coined the term ...

📺 Neural Nutshell

👁️ 17K • 👍 528 • 💬 230 • ⏱️ 15:22 • 1d ago

---

**[The AI Bubble Pop Everyone Predicted Just Got Canceled](https://www.youtube.com/watch?v=lBs5w7cgF8o)**

Despite recent speculation, the AI bubble pop is canceled, a thesis no longer supported by current evidence. We look at insights ...

📺 Dr. Josh C. Simmons

👁️ 3K • 👍 252 • 💬 87 • ⏱️ 11:38 • 6h ago

---

**[Apple’s New Siri AI is INSANE (iOS 27 Hands-On)](https://www.youtube.com/watch?v=U6pmeVrfFno)**

Apple has finally unveiled the all-new Siri AI in iOS 27, and it's the biggest Siri upgrade ever. In this hands-on walkthrough, I test ...

📺 MacRumors

👁️ 37K • 👍 1K • 💬 218 • ⏱️ 7:49 • 6h ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 675,936 • ❤️ 888 • 6d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 131,794 • ❤️ 1,805 • 2d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 711,706 • ❤️ 549 • 1d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 7,170 • ❤️ 473 • 7d ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 140,221 • ❤️ 503 • 6d ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 19,948 • ❤️ 322 • 6h ago

---

**[nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**

*NVIDIA*

Nemotron 3.5 ASR is a multilingual, streaming Automatic Speech Recognition (ASR) model supporting 40 language-locales. It uses a Cache-Aware FastConformer-RNNT architecture for efficient, low-latency transcription of audio into punctuated text, suitable for both streaming and batch processing.

`automatic-speech-recognition`

⬇️ 4,965 • ❤️ 346 • 5d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 1,859 • ❤️ 260 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,057,541 • ❤️ 1,634 • 1mo ago

---

**[ideogram-4-nf4](https://huggingface.co/ideogram-ai/ideogram-4-nf4)**

*Ideogram*

Ideogram 4 is a state-of-the-art, open-weight text-to-image diffusion model trained from scratch. It excels at multilingual text rendering, layout control, and native 2k resolution image generation, positioning it at the forefront of design-oriented visual intelligence.

`text-to-image`

⬇️ 6,124 • ❤️ 307 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 90 • 💬 4 • ⭐ 84,989 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 186 • 💬 2 • ⭐ 529 • 8d ago

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

▲ 172 • 💬 10 • ⭐ 49,224 • 9mo ago

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

▲ 165 • 💬 2 • ⭐ 67,131 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 111 • 💬 1 • ⭐ 9,830 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 40 • 💬 4 • ⭐ 29,145 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 67.1k • 🔱 8.4k • 2h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace for DeepSeek models, with Code and Claw modes built into your application.

`TypeScript`

⭐ 3.7k • 🔱 320 • 13m ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.4k • 🔱 346 • 5d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.1k • 🔱 331 • 16h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.7k • 🔱 310 • 16h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 176 • 1d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 137 • 6d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.8k • 🔱 142 • 52m ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 80 • 6d ago

---

**[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)**

Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base  Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端

`Shell`

⭐ 1.5k • 🔱 304 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
