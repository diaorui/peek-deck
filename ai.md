---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-11T19:18:47.856186+00:00'
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

**Last Updated:** June 11, 2026 at 19:18 UTC  
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

**[Do you think AI is becoming normal faster than people expected?](https://www.reddit.com/r/artificial/comments/1u31332/do_you_think_ai_is_becoming_normal_faster_than/)**

It feels like just a couple of years ago, using AI for everyday tasks still felt like something new or even a bit weird. Now it seems like a lot of people are using it without thinking twice, whether for writing, learning, brainstorming, or just quick answers. I’m curious how others see this shift. Do you think AI has become normalized quicker than most people predicted, or does it still feel like a big deal to a lot of users?

4h ago

---

**[Nobody needs AI to search the Internet, court says in ruling against Google](https://www.reddit.com/r/artificial/comments/1u2cwez/nobody_needs_ai_to_search_the_internet_court_says/)**

🔗 [arstechnica.com](https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/) • 23h ago

---

**[Google DeepMind releases DiffusionGemma, a model that runs local AI 4x faster | Diffusion AI is most common in image generation, but it can make text outputs much faster.](https://www.reddit.com/r/artificial/comments/1u373y6/google_deepmind_releases_diffusiongemma_a_model/)**

🔗 [arstechnica.com](https://arstechnica.com/google/2026/06/googles-latest-diffusiongemma-open-ai-model-comes-with-a-4x-speed-boost/) • 54m ago

---

**[Which AI agent are you?](https://www.reddit.com/r/artificial/comments/1u31cep/which_ai_agent_are_you/)**

Seven questions, five personas: Orchestrator, Architect, Explorer, Closer, or Guardian? Find your AI agent persona and your ideal starter team. No signup.

🔗 [What Is Agentic AI](https://whatisagenticai.net/quiz/) • 4h ago

---

**[Judge Learns Lawyers on Both Sides of Case Used AI, Cancels Trial, Kicks Everyone Off the Case](https://www.reddit.com/r/artificial/comments/1u2onqz/judge_learns_lawyers_on_both_sides_of_case_used/)**

When two AIs argue against each other, the legal system loses.

🔗 [404 Media](https://www.404media.co/judge-learns-lawyers-on-both-sides-of-case-used-ai-cancels-trial-kicks-everyone-off-the-case/) • 15h ago

---

**[The gap between decision and exécution](https://www.reddit.com/r/artificial/comments/1u30wjh/the_gap_between_decision_and_exécution/)**

I’ve been thinking about a support automation story I read recently. A team replaced a simple rules engine with an LLM classifier. The model was around 92% accurate. Sounds good. Until you realize that at 100 tickets a day, that’s roughly 8 mistakes every day. The interesting part wasn’t the accuracy though. It was what happened when the model was wrong. Nobody could explain why a ticket was classified a certain way. Nobody could point to a specific rule. Nobody could quickly fix the behavior. The team eventually started reviewing every classification manually. The automation was still running, but the trust was gone. That got me thinking. A lot of discussion around AI agents focuses on making decisions better. Better prompts. Better models. Better reasoning. But I rarely see people discussing what happens after the decision. How is the decision verified? How is it audited? How do you know an action should actually be executed? Maybe the biggest challenge for AI agents isn’t getting from 92% to 96%. Maybe it’s building systems that people can trust when things go wrong. Curious how others are thinking about this.

4h ago

---

**[I ran Fable 5 for half day and the guardrails are the real story](https://www.reddit.com/r/artificial/comments/1u28c7d/i_ran_fable_5_for_half_day_and_the_guardrails_are/)**

Anthropic dropped Fable 5 and I immediately swapped it into our dev stack. We route everything through a single endpoint on zenmux, so the actual switch was changing one model string and watching the latency graphs. The good parts first because there are a lot of them. I threw a refactoring task at it: split a messy python service into modules, preserve the public api, and write tests that prove nothing broke. Fable 5 planned the whole thing, caught a circular dependency I did not mention, and verified the tests pass. With Opus 4.8 I usually have to nudge it a couple of times when it forgets to update the init file. Fable 5 just did it. Then I dumped our full codebase and asked it to find a race condition we had been hunting for a week. It traced the async flow, named the exact function, and described the interleaving that triggers the bug. That level of context digestion feels new. Opus is good at long context, but Fable 5 felt like it was actually reasoning across the whole window instead of pattern matching near the top. I also sent it a blurry dashboard screenshot from a client call and it rebuilt the html and echarts config including the tooltip formatting. My designer’s first words were "when did you learn front end." I did not. But here is the part nobody in the launch threads is talking about enough. It is slow. On high effort I am seeing 45 to 90 seconds for a single complex turn. Our latency graphs go from a flat green line to a jagged mess the moment Fable 5 traffic hits. And it is expensive. The same prompt that costs X on Opus 4.8 costs roughly 1.4 to 1.7X on Fable 5 because it generates more tokens and runs at a higher effort tier by default. It writes its own reasoning traces out loud and bills you for them. For research tasks the quality is worth it. For "rewrite this email" it is comically overpowered. The bigger issue is the silent fallback. Fable 5 is basically Mythos with guardrails. When your prompt touches cybersecurity, biology, chemistry, or distillation, it silently routes to Opus 4.8. No warning. I found this out debugging a staging proxy config, entirely normal internal work, and halfway through the thread the code style changed. Checked the metadata and sure enough it had fallen back to Opus 4.8 mid thread because the word "proxy" made the classifier jumpy. Anthropic says this happens in under 5 percent of sessions globally, but for my stack it was closer to 15 percent because we touch infrastructure and networking a lot. When it happens mid task the model switch breaks context. I had a four turn debugging sequence where turn three flipped to Opus because I mentioned a firewall rule, then turn four flipped back. The state was preserved but the tone and depth shifted enough that I had to restart the thread. After 12 hours here is where I land. If you are doing pure software engineering, data analysis, or scientific reasoning in safe domains, Fable 5 is the best model I have ever used. It is not close. But if you touch infrastructure or security, the silent fallback is genuinely annoying and you need to monitor which model actually answered you. We only caught the switch because our gateway logs the per call trace. Without that you might not even know it swapped until the tone changes. I am keeping it enabled for our non sensitive dev workflows. For anything touching infra I am routing to Opus 4.8 explicitly until I understand the classifier boundaries better. Fable 5 is a beast. Anthropic just needs to tell you when it is not the one driving.

1d ago

---

**[Anthropic: “AI is too dangerous” also Anthropic: releases the most dangerous AI model ever](https://www.reddit.com/r/artificial/comments/1u38fk3/anthropic_ai_is_too_dangerous_also_anthropic/)**

They literally published a blog this week calling for a global pause on AI and warning that humans might lose control of their own creations. Same week they started testing Mythos, a model they describe as so powerful it could cause widespread disruption if released publicly. They also dropped their flagship safety pledge earlier this year, saying they won’t hold back dangerous AI if rivals are getting close. ￼ The valuation? $965 billion. The safety message and the growth machine are running on the exact same calendar. ￼ Nobody is actually slowing down. They’re just the ones with the best PR about it.

7m ago

---

**[Crazy Sensitive infos generated by AI chat bots](https://www.reddit.com/r/artificial/comments/1u3861e/crazy_sensitive_infos_generated_by_ai_chat_bots/)**

So this chat bot (which is pretty famous like gemini and other ones) some of you might know understand which chat bot it is by looking at the font and styling, it apparently generates very sensitive things, like literal codes for ransomeware and other things pretty crazy, these things have no restriction, ofcourse these might be pretty much non working things as they are plausible and hallucinated stuff but still it's crazy, most AI chat bots seem to be getting strong at moderation day by day but still some find a way through it

16m ago

---

**[I gave your agent access to Firefox - meet Firefox CLI](https://www.reddit.com/r/artificial/comments/1u37gjn/i_gave_your_agent_access_to_firefox_meet_firefox/)**

Firefox CLI is a CLI interface that lets your agent control your real Firefox session. It's a full equivalent of Agent Browser with the same capabilities, but for Firefox - and with a number of improvements. Why it's better First, you install the extension once and for all. The extension ships right alongside the CLI: install it, grant access, forget about it. Unlike Chrome, where you have to grant connection permissions every half hour and manage debugging sessions - here it's one button and full control. Second, your agents can now create their own separate windows and request your permission to connect on their own. In everything else, Firefox CLI mirrors Agent Browser: token-efficient operation via short IDs, running arbitrary scripts, keypresses, input emulation, form filling, and full tab and window management of your real session - where you're already logged in. Why I built it I used the Comet browser for a long time (on my promo subscription to Perplexity), but it started to let me down. More unnecessary features and ads crept in, it got slower. But the main thing - using Comet as an actual browser during development is extremely inconvenient: there's music you can't turn off, a broken onboarding that was never fixed after months of back-and-forth with support, and a poorly functioning CDP. I switched back to Firefox as my main browser, but losing the ability for agents to control my browser was a huge blow to my workflow. No automation for filling out boring freelance forms, no proper web app testing. I went looking for alternatives, but nothing like Agent Browser for Firefox simply existed. And here's the result :) Installation 1. Install the CLI: bash npm install -g firefox-cli 2. Install the Firefox extension: bash firefox-cli setup 3. Install the skill for agents: Claude Code text /plugin marketplace add respawn-llc/claude-plugin-marketplace /plugin install firefox-cli@respawn-tools Codex text $skill-installer install https://github.com/respawn-llc/firefox-cli/tree/main/skills/firefox-cli General bash npx skills@latest add respawn-llc/firefox-cli The project was built by Builder autonomously over 62 hours of continuous work.

41m ago

---

---

## Google News: "ai"

**[Exclusive | OpenAI Considers Drastic Price Cuts, Anticipating War for Users With Anthropic](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)**

WSJ • 17h ago

---

**[Why the Real A.I. Threat Is in the Back Office](https://www.nytimes.com/2026/06/10/business/economy/back-office-workers-ai.html)**

The New York Times • 1d ago

---

**[Three Ways to Think About AI and Jobs](https://www.theatlantic.com/economy/2026/06/ai-job-displacement-questions/687503/)**

Whether automation will make human workers obsolete depends on more than just how smart the AI is.

The Atlantic • 3h ago

---

**[AI is sparking a jobs boom — just not for newbies](https://www.cnn.com/2026/06/11/business/ai-jobs-work)**

As Corporate America scrambles to fill artificial intelligence jobs, junior workers are getting left behind.

CNN • 9h ago

---

**[AI Learned How the Universe Works—and That Created an Unexpected Problem for Physicists](https://gizmodo.com/ai-learned-how-the-universe-works-and-that-created-an-unexpected-problem-for-physicists-2000770643)**

Gizmodo • 13m ago

---

**[The workers Meta and Google are scrambling to find](https://www.businessinsider.com/google-meta-invest-trades-training-ai-data-center-boom-2026-6)**

As AI drives a data center boom, tech giants are backing trade programs to help fill a growing construction labor shortage.

Business Insider • 31m ago

---

**[Single snapshot unlocks 3D depth with coded aperture and AI](https://techxplore.com/news/2026-06-snapshot-3d-depth-coded-aperture.html)**

Tech Xplore • 18m ago

---

**[Introducing Claude Corps](https://www.anthropic.com/news/claude-corps)**

We’re launching Claude Corps, a national fellowship program for people early in their careers who are passionate about extending the benefits of AI to communities across America.

Anthropic • 6h ago

---

**[AI wealth boom sending San Francisco home prices surging: ‘It’s ridiculous’](https://www.theguardian.com/us-news/2026/jun/11/ai-wealth-boom-san-francisco-home-prices)**

Employees at artificial intelligence companies are coming into gargantuan sums of money amid boom in IPOs

The Guardian • 5h ago

---

**[How to share AI riches](https://www.economist.com/finance-and-economics/2026/06/11/how-to-share-ai-riches)**

The Economist • 9h ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 997 • 💬 530 • 1d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 827 • 💬 305 • 2d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[Microsoft's open source tools were hacked to steal passwords of AI developers](https://news.ycombinator.com/item?id=48457830)**

Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack.

⬆️ 558 • 💬 193 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 532 • 💬 239 • 19h ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Cleaning up after AI rockstar developers](https://news.ycombinator.com/item?id=48458586)**

We've all worked with a rockstar developer. They joined the team years ago, full of energy. They had great ideas about new tech, new paradigms, new architectures. Their cutting-edge ideas left everyone else feeling a bit behind and outdated.

⬆️ 492 • 💬 360 • 2d ago • [codingwithjesse.com](https://www.codingwithjesse.com/blog/rockstar-developers/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 250 • 💬 300 • 11h ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 238 • 💬 196 • 5h ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

---

**[Apache Burr: Build reliable AI agents and applications](https://news.ycombinator.com/item?id=48477400)**

Apache Burr (Incubating) - develop AI applications that make decisions. Pure Python, no magic.

⬆️ 238 • 💬 112 • 1d ago • [burr.apache.org](https://burr.apache.org/)

---

**[Rich Sutton on AI creativity and discovery](https://news.ycombinator.com/item?id=48470581)**

A new and possibly controversial perspective:
In this video, I explain the sense in which generative AI trained by supervised learning is incapable of making novel discoveries.
https://t.co/LhAU6AyDkh

The text of the speech:

AI Creativity and Discovery

Good day ladies and

⬆️ 205 • 💬 121 • 1d ago • [X (formerly Twitter)](https://twitter.com/RichardSSutton/status/2061216087744946656)

---

**[A €0.01 bank transfer could compromise a banking AI agent](https://news.ycombinator.com/item?id=48476136)**

Blue41 helps regulated organizations monitor AI agent behavior, detect manipulation and misuse, and prove that sensitive workflows stay within safe boundaries.

⬆️ 199 • 💬 192 • 1d ago • [blue41.com](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

---

---

## YouTube Videos: "ai"

**[The AI cash burn is about to pop](https://www.youtube.com/watch?v=ZswT_E0zW-Q)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 42K • 👍 3K • 💬 540 • ⏱️ 14:47 • 5h ago

---

**[Something Is Going Wrong with AI in China—and Now Xi Jinping Is Trying to Slow It Down](https://www.youtube.com/watch?v=F3PZFrzajVc)**

Go to https://surfshark.com/economik or use code ECONOMIK at checkout to get 4 extra months of Surfshark VPN! Check out our ...

📺 VisualEconomik EN

👁️ 28K • 👍 1K • 💬 236 • ⏱️ 16:06 • 1d ago

---

**[Claude vs ChatGPT vs Gemini Make An AI Film From Scratch](https://www.youtube.com/watch?v=FBHCeGb-1zU)**

I Made An AI Film With 1 Prompt - ChatGPT vs Claude vs Gemini Make your Ai Films ...

📺 Skai Generated

👁️ 4K • ⏱️ 14:01 • 2h ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 61K • 👍 2K • 💬 326 • ⏱️ 11:30 • 1d ago

---

**[The Riskiest Moment of the AI Bubble](https://www.youtube.com/watch?v=AcjnLc4TH4M)**

NOTE! Since I recorded this video: 1. OpenAI has indeed made it's first filing to go public, though how long from now that will ...

📺 Hank Green

👁️ 1.5M • 👍 47K • 💬 4K • ⏱️ 12:29 • 2d ago

---

**[Anthropic&#39;s CEO raises concerns over rapidly developing AI technology](https://www.youtube.com/watch?v=C9Rnt3FKaIY)**

In an interview with ABC News' Linsey Davis, Dario Amodei issued an urgent warning about the dangers of AI, calling for ...

📺 ABC News

👁️ 12K • 👍 151 • 💬 68 • ⏱️ 2:07 • 19h ago

---

**[Trump’s Ai ‘Public Stake’ Plan Is Just 2008 All Over Again](https://www.youtube.com/watch?v=C7Fc_w39bzU)**

Trump #AI #TrumpAI Trump says he's meeting with the top 12-15 AI executives "very shortly" to discuss giving the public a stake in ...

📺 curious@bitcoin

👁️ 783 • 👍 10 • 💬 3 • ⏱️ 0:46 • 1h ago

---

**[Cops Jail Innocent Black Man for MONTHS After AI Error](https://www.youtube.com/watch?v=pT4V8gD40Fo)**

Thanks to police using AI, Jalil Richardson was misidentified and jailed for several months over a vehicle theft he did not commit.

📺 Indisputable with Dr. Rashad Richey

👁️ 6K • 👍 318 • 💬 55 • ⏱️ 6:06 • 20h ago

---

**[The dark side of AI - Exploitation of humans and nature | DW Documentary](https://www.youtube.com/watch?v=ND7owjmtPNo)**

Magical, autonomous, all-powerful: Artificial intelligence fuels our dreams and nightmares. While tech companies promise us a ...

📺 DW Documentary

👁️ 114K • 👍 3K • 💬 471 • ⏱️ 54:11 • 1d ago

---

**[Prometheus CO-CEO Jeff Bezos: AI will result in labor scarcity, will raise standard of living](https://www.youtube.com/watch?v=NG0GoX0zMxQ)**

Prometheus Co-Founders and Co-CEOs Jeff Bezos and Vik Bajaj sits down with CNBC's David Faber to talk Prometheus' strategy ...

📺 CNBC Television

👁️ 4K • 👍 92 • 💬 52 • ⏱️ 2:45 • 2h ago

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

⬇️ 19,948 • ❤️ 344 • 23h ago

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

⬇️ 1,859 • ❤️ 299 • 9h ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 7,170 • ❤️ 481 • 8d ago

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

⭐ 68.2k • 🔱 8.5k • 11m ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace for DeepSeek models, with Code and Claw modes built into your application.

`TypeScript`

⭐ 3.8k • 🔱 333 • 17h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.5k • 🔱 353 • 6d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 335 • 12h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.8k • 🔱 322 • 6h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 176 • 2d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.9k • 🔱 143 • 3h ago

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
