---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-21T13:41:30.378774+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 21, 2026 at 13:41 UTC  
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

**[This is really the entire plan.](https://www.reddit.com/r/artificial/comments/1wlze5f/this_is_really_the_entire_plan/)**

11h ago

---

**[These Were NOT Rogue AI Escapes. Just SLOPPY Firewall Failures.](https://www.reddit.com/r/artificial/comments/1wm9aua/these_were_not_rogue_ai_escapes_just_sloppy/)**

The headlines right now are full of stories about AI models "escaping their sandboxes" and literally killing all humans, lol. I've even heard several commentators and writers say that AI escaped an "Air gap". But that is SO WRONG. It's actually TOTALLY WRONG. *To be clear, not a single one of these sandboxes was actually air-gapped.* That's a crucial computer science fact. An air gapped sandbox would require *ZERO* cables and network interfaces. It would also require absolute physical isolation. What these labs actually built were soft software barriers. And then they left the doors unlocked. With some of the smartest AI on the planet. Lol. Of COURSE it escaped. 1. The OpenAI / Hugging Face "Escape": The sandbox was connected to OpenAI’s internal network through a package proxy. The model didn't perform magic. It found a basic flaw in the proxy and walked right through the open door. 2. The Google Gemini "Hack": Testers left the model connected to the live internet during offensive tests. They then used a test domain name that overlapped with real companies. These were classic IT security failures. I'm talking about bad network segmentation, permissive egress rules, and relying on soft software barriers instead of true physical isolation. When you leave an active network interface open on a test bed, a model finding its way out is just sloppy cybersecurity. Your nerdy friend, Mike D

2h ago

---

**[Professor: A “messy” job is the defense against AI unemployment](https://www.reddit.com/r/artificial/comments/1wm3ok9/professor_a_messy_job_is_the_defense_against_ai/)**

An excerpt: "Fundamentally, Garicano says there are two factors that determine whether a job is messy. The first is whether the tasks that make up the job are difficult to separate from one another. He cites sales as an example. There is a significant cognitive component involving understanding the customer and what product they are looking for. The salesperson can use AI to help with this, but it’s still something they will also have to do themselves. “In order to meet the potential customer for dinner, I need to be able to think ‘Oh, he wants this other thing’, and then remember that we have this other product.” The second factor that makes a job messy is whether it involves managing a complex network of human relationships. The book gives the example of a chief engineer at a factory who, among other things, has to hire new employees, negotiate with executives about implementing proposals, communicate with the municipality about obtaining building permits, and so on. By contrast, your job is vulnerable if it consists of a single isolated task where it is possible to objectively verify whether it has been completed correctly. Examples might include technical translation, drafting standard contracts, or simple bookkeeping tasks where the numbers have to add up."

🔗 [excitech.media](https://excitech.media/p/professor-a-messy-job-is-the-defense) • 8h ago

---

**[Most ai productivity advice comes from people who don't have much actual work to do](https://www.reddit.com/r/artificial/comments/1wmbbu9/most_ai_productivity_advice_comes_from_people_who/)**

If you already have a real workflow, ai speeds it up. if you don't, no tool hands you one. that's the whole thing and nobody says it. the people posting "15 ai tools you NEED" are mostly just doing tools as a hobby. which is fine but that's shopping, not productivity. i've done it too, spent weeks trying stuff instead of doing the thing i was avoiding. pick two. learn them properly. don't switch until one actually fails you!

1h ago

---

**[FBI Director Kash Patel says that AI use at the FBI has "increased by 605%" since he became director — claims that every major tech player is "embedded" in the agency](https://www.reddit.com/r/artificial/comments/1wm2996/fbi_director_kash_patel_says_that_ai_use_at_the/)**

A seemingly unsupported figure that nevertheless may be grounded in truth.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/kash-patel-says-that-ai-use-at-the-fbi-has-increased-by-605-percent-since-he-became-director-claims-that-every-major-tech-player-is-embedded-in-the-agency) • 9h ago

---

**[A $40M model is being sold on calibrated confidence, and no calibration data has been published](https://www.reddit.com/r/artificial/comments/1wm8btm/a_40m_model_is_being_sold_on_calibrated/)**

TypeSafe AI came out of stealth on September 15 with $40M led by DCVC, reportedly at a $200M valuation, founded by Diogo Almeida, an ex-OpenAI researcher who worked on InstructGPT, ChatGPT and GPT-4. Their model, Jev, does not generate text. It takes program state plus typed questions and returns typed answers with a probability on each. The framing is Kahneman's System One: fast intuitive judgment rather than deliberation. The product claim is that those probabilities are calibrated, meaning 70% should be right about 70% of the time. TypeSafe calls the training method Reinforcement Learning for Calibrated Decisions. Here is what bothers me about the coverage so far. Calibration is the whole product and there is no public measurement of it No expected calibration error. No reliability diagrams. No results on any standard public benchmark. No architecture paper. For a company whose pitch is fixing AI overconfidence, the overconfidence-fixing property is the one thing with nothing published behind it. What has been published is a company-designed eval over four workflow tasks where the correct answer is defined as the average of GPT-6 Astra and Claude Fable 5.1 at high thinking. That measures agreement with two competitor models, not correctness. A model could match the reference on every case and be wrong on every case. Competing models in the same harness run at default reasoning settings, so the 193.6x speed and 444.6x cost multipliers are measured against reasoning-off configurations while the accuracy target comes from reasoning-on ones. "Cannot hallucinate" is true in a narrow sense The output space is fixed before decoding, so it cannot emit an option that is not on the list. That eliminates fabricated output. It does not make the chosen option correct. The Register made the same point: absence of hallucination does not preclude being incorrect. Constrained decoding is also not new, OpenAI has guaranteed JSON Schema conformance since August 2024. Where I think the skepticism should stop The adoption number is third-party and it is striking. Vercel reported Jev as the fastest-adopted model in AI Gateway history: a tenth of paid teams within 18 hours, nearly 13% by hour 24, roughly six times Fable 5.1's first-day share. And TypeSafe's own documentation is unusually honest. It publishes a model jaggedness page stating that Jev does not count reliably, underperforms on hex and RGB values, cannot judge whether two values are near each other, and reads dates as text. It also states there is no guaranteed mathematical relationship between semantically related outputs, so the probability of a statement and its negation need not sum to 1. That is a genuinely awkward admission to sit next to a calibration pitch, and they published it anyway. So: real product, real adoption, and a headline property nobody outside the company has measured. What would you want to see before trusting the confidence numbers in production?

3h ago

---

**[AI CAN be incredible for learning](https://www.reddit.com/r/artificial/comments/1wlzydy/ai_can_be_incredible_for_learning/)**

I've seen a lot of hate that LLMs will always reduce people's ability to for themselves, which I think isn't true. You can use LLMs to learn extremely effectively, but the hard part is avoiding the thousands of ways to learn extremely ineffectively. I've been using LLMs to find gaps in my knowledge by asking me questions about my notes, and it's been working very well. It's not something a YouTube video can emulate because it's completely personalized to what YOU know. A teacher will always be better, but sometimes you want to learn something on your own, or don't want to pester the teacher for whatever reason. You can ask as many stupid questions as many times as you want. That's the power, personalization. Now, if used incorrectly, it can be very hurtful for your cognitive development, no doubting that. You just have to have self-control and use it as a tutor, not an answer machine. What are your thoughts on this?

11h ago

---

**[What’s an AI capability people underestimate because they’re using it for the wrong things?](https://www.reddit.com/r/artificial/comments/1wlunqx/whats_an_ai_capability_people_underestimate/)**

Everyone talks about generating text, images, and code. What’s a less obvious use case where you think AI is genuinely much more useful than people realize?

15h ago

---

**[Joint Chiefs chairman says U.S. forces must prepare to be ‘hunted’ by autonomous systems](https://www.reddit.com/r/artificial/comments/1wlpbbq/joint_chiefs_chairman_says_us_forces_must_prepare/)**

“We have to assume from now on that our formations will be hunted by autonomous systems, jammed across the spectrum, and tracked in real time," Gen. Dan Caine said.

🔗 [DefenseScoop](https://defensescoop.com/2026/09/16/gen-dan-caine-drones-autonomous-systems-ai-enabled-warfare/) • 18h ago

---

**[“I have a really, really strong legal team.” Inside the AI party boom.](https://www.reddit.com/r/artificial/comments/1wlre82/i_have_a_really_really_strong_legal_team_inside/)**

They’re skipping caviar for fire-breathing lessons.

🔗 [The San Francisco Standard](https://sfstandard.com/2026/09/19/ai-party-boom/) • 17h ago

---

---

## Google News: "ai"

**[Nvidia's Jensen Huang rejects AI extinction warnings as "doomsday narratives"](https://www.cbsnews.com/news/jensen-huang-nvidia-rejects-ai-extinction-warnings/)**

Predictions that AI could destroy humanity in a few years are irresponsible and not based on science, Nvidia's co-founder told CBS News.

CBS News • 1d ago

---

**[Nvidia boss says there is ‘0% chance’ AI destroys the world by 2030 | AI (artificial intelligence)](https://www.theguardian.com/technology/2026/sep/21/nvidia-boss-jensen-huang-dismisses-warnings-ai-destroys-world-anthropic)**

Jensen Huang dismisses warnings from former Anthropic researcher and others as ‘doomsday narratives’

theguardian.com • 6h ago

---

**[Capitol agenda: Nvidia’s clout tested as AI debate shifts](https://www.politico.com/live-updates/2026/09/21/congress/what-were-watching-01085964)**

Politico • 4h ago

---

**[U.S. and China Discuss System to Warn of A.I. National Security Issues](https://www.nytimes.com/2026/09/20/business/us-china-ai-warning-system-national-security.html)**

The New York Times • 12h ago

---

**[M6 Mac mini Review: A Better Tiny Desktop, With or Without AI](https://gizmodo.com/m6-mac-mini-review-a-better-tiny-desktop-with-or-without-ai-2000813947)**

Gizmodo • 41m ago

---

**[‘Energy-Guzzling’ AI Must Rein in Its Emissions, Says UN Climate Chief](https://www.bloomberg.com/news/articles/2026-09-21/-energy-guzzling-ai-must-rein-in-its-emissions-says-un-climate-chief)**

Bloomberg.com • 30m ago

---

**[Scott Wiener and Connie Chan both want to rein in AI. They disagree on how to do that.](https://missionlocal.org/2026/09/ai-nancy-pelosi-scott-wiener-connie-chan/)**

missionlocal.org • 41m ago

---

**[Trump admin won't give AI leaders a 'liability shield,' Bessent tells CNBC](https://www.cnbc.com/2026/09/21/treasury-bessent-cnbc-squawk-trump-bond-affordabilty.html)**

Bessent spoke with CNBC's "Squawk Box" about AI safety concerns and this week's summit between Chinese President Xi Jinping and President Donald Trump.

CNBC • 2h ago

---

**[Trump and Xi dine with AI titans and Meta takes the stage: What to watch this week](https://finance.yahoo.com/markets/article/trump-and-xi-dine-with-ai-titans-and-meta-takes-the-stage-what-to-watch-this-week-100000383.html)**

A state visit from Chinese leader Xi Jinping, conferences from Meta and Qualcomm, and a lot of FedSpeak form the last full week of September.

Yahoo Finance • 3h ago

---

**[Is this how the world ends? Extinction scenarios are taking over the AI debate.](https://www.washingtonpost.com/technology/2026/09/21/is-this-how-world-ends-extinction-scenarios-are-taking-over-ai-debate/)**

As nightmare thought experiments shape the fight over how to govern a multitrillion-dollar industry, some experts say the parables may lead decision-makers astray.

washingtonpost.com • 8m ago

---

---

## HackerNews: "ai"

**[AI-generated posters don’t have to be horrible](https://news.ycombinator.com/item?id=49764791)**

The problem

⬆️ 1834 • 💬 931 • 2d ago • [‘ERE I AM - JH!](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

---

**[US Military had close call after using AI for hallucinated intelligence report](https://news.ycombinator.com/item?id=49757520)**

The episode shows the risks of using this new, relatively poorly understood technology in the middle of the Iran war

⬆️ 513 • 💬 388 • 2d ago • [CNN](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship)

---

**[I think you should almost never use AI to write](https://news.ycombinator.com/item?id=49767937)**

⬆️ 354 • 💬 168 • 1d ago • [erichgrunewald.substack.com](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai)

---

**[AI and the Destruction of the Creative Commons](https://news.ycombinator.com/item?id=49774329)**

⬆️ 231 • 💬 275 • 1d ago • [chesterwisniewski.com](https://www.chesterwisniewski.com/post/2026-09-13-ai-is-destroying-the-creative-commons/)

---

**[Microsoft director: AI scraping 'the largest theft of labor in human history'](https://news.ycombinator.com/item?id=49768921)**

The NYT argues that OpenAI and Microsoft infringed upon its copyright over thousands of news articles.

⬆️ 186 • 💬 49 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit)

---

**[Alibaba open-sources AI model that can detect cancer and nearly 150 conditions](https://news.ycombinator.com/item?id=49761840)**

⬆️ 151 • 💬 25 • 2d ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions)

---

**[AI chatbots give wrong answers to financial queries 'most of the time'](https://news.ycombinator.com/item?id=49783062)**

Report finds some chatbots ignored upcoming tax changes and hallucinated rules

⬆️ 130 • 💬 62 • 9h ago • [ft.com](https://www.ft.com/content/c0cd359d-df84-4208-a789-ffa864b43666)

---

**[AI is an elite crime spree](https://news.ycombinator.com/item?id=49755590)**

⬆️ 124 • 💬 42 • 2d ago • [thebignewsletter.com](https://www.thebignewsletter.com/p/ai-is-an-elite-crime-spree)

---

**[Can you tell which images are AI-generated?](https://news.ycombinator.com/item?id=49770847)**

Trust your eyes, build a streak, and beat your score in 60 seconds.

⬆️ 109 • 💬 85 • 1d ago • [Slop Sense](https://slop-sense.labtoagi.com/games/is-this-image-ai/)

---

**[If AI coding is lowering your code quality, you're not managing quality right](https://news.ycombinator.com/item?id=49774795)**

One common take on the coding agents that I see goes something like this: “Sure, AI helps you output more code, but won’t the quality suffer?”

⬆️ 104 • 💬 149 • 1d ago • [i-kh.net](https://www.i-kh.net/p/if-ai-coding-is-lowering-your-code)

---

---

## YouTube Videos: "ai"

**[Comedians roast AI CEOs for warning AI could kill us all | Have I Got News For You](https://www.youtube.com/watch?v=hopgSsqnHZ0)**

Have I Got News For You” host Roy Wood Jr. talks to his panel of comedians about AI CEO's warnings that, yes, the tech they're ...

📺 CNN

👁️ 100K • 👍 886 • 💬 167 • ⏱️ 11:24 • 18h ago

---

**[AI experts on doomsday fears: It&#39;s too late to stop the AI threat](https://www.youtube.com/watch?v=rvxfcmloDhU)**

The New York Times columnist Thomas Friedman tells CNN why it's already too late to stop the AI threat. Geoffrey Hinton, the ...

📺 CNN

👁️ 274K • 👍 1K • 💬 767 • ⏱️ 11:45 • 1d ago

---

**[Something Just Snapped In The AI Industry...](https://www.youtube.com/watch?v=JMvHSNT1xyQ)**

The AI industry has raised serious concerns lately. A number of researchers, insiders, and even CEOs are now about the rapid ...

📺 Alex Wei

👁️ 41K • 👍 1K • 💬 473 • ⏱️ 21:13 • 2d ago

---

**[Fable 5.2 Just Embarrassed GPT-6 Astra](https://www.youtube.com/watch?v=a30jl5ZXlsM)**

Anthropic's leaked Fable 5.2 is already reaching Claude users, with early testers claiming it beats GPT-6 Astra while Opus 5.2 ...

📺 AI Revolution

👁️ 59K • 👍 785 • 💬 82 • ⏱️ 14:43 • 12h ago

---

**[How to Make Long AI Videos With Consistent Characters](https://www.youtube.com/watch?v=NBS98oN5zs0)**

Create Long AI Videos https://higgsfield.ai?fpr=ai&fp_sid=conor In this video, I show how I keep two characters consistent ...

📺 Creating with Conor

👁️ 11K • 💬 1 • ⏱️ 8:04 • 1d ago

---

**[AI Is Outrunning Everyone’s Predictions - Noam Brown](https://www.youtube.com/watch?v=-OIQs3xe9-I)**

📺 Dwarkesh Patel

👁️ 68K • 👍 836 • 💬 107 • ⏱️ 0:39 • 2d ago

---

**[Extended interview: Nvidia CEO Jensen Huang on fears about AI](https://www.youtube.com/watch?v=xCUala5j7aQ)**

In this web exclusive, Nvidia CEO Jensen Huang talks with CBS News' Jo Ling Kent about the exponential growth of AI, industry ...

📺 CBS Sunday Morning

👁️ 236K • 👍 2K • 💬 876 • ⏱️ 46:19 • 1d ago

---

**[The CHILLING Reason AI Researchers Are Quitting Their Jobs](https://www.youtube.com/watch?v=JYIkGljjnWY)**

Nate Soares, president of the Machine Intelligence Research Institute, joins the show to discuss the potential life-threatening ...

📺 The Young Turks

👁️ 158K • 👍 3K • 💬 1K • ⏱️ 24:35 • 21h ago

---

**[How to Run Local AI on ANY Computer (in 1 click)](https://www.youtube.com/watch?v=MZ2YVMkdjTI)**

It's never been easier to use local AI with Hermes agent Sign up for my free newsletter: https://www.shipitweekly.com/ FULL local ...

📺 Alex Finn

👁️ 51K • 👍 1K • 💬 79 • ⏱️ 12:10 • 2d ago

---

**[Garbage Truck AI](https://www.youtube.com/watch?v=NGvlIY4W_KQ)**

Writer: Kyler Himes Editor: Catlin Stevenson Music by: @UFD-Music Great, ANOTHER public surveillance camera to worry about.

📺 UFD Tech

👁️ 254K • 👍 10K • 💬 932 • ⏱️ 0:43 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 2,227,879 • ❤️ 1,650 • 3d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 1,486 • 1d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 6,523 • ❤️ 1,197 • 8h ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 18,394 • ❤️ 1,020 • 3d ago

---

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 512,120 • ❤️ 3,486 • 11d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,153,238 • ❤️ 15,923 • 1mo ago

---

**[Qwen-2.5-1B-RLCD](https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD)**

*Harsha Gundala*

Qwen-2.5-1B-RLCD is a text-generation model optimized for high-throughput structured information extraction on Apple Silicon using MLX. It achieves 5.6x-7.0x latency reductions with 100% schema validity by evaluating multi-field JSON schemas in parallel, ideal for tasks like fraud routing, code auditing, and support triage.

`text-generation`

⬇️ 0 • ❤️ 494 • 5d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 1,292,471 • ❤️ 1,510 • 19d ago

---

**[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)**

*Multimodal Art Projection*

YuE2-3B is a text-to-audio model capable of generating high-quality music with vocals and accompaniment from lyrics and style prompts. It features editable score generation, agentic editing for iterative refinement, and can run locally on a 24GB GPU.

`text-to-audio` `3.6B`

⬇️ 18,759 • ❤️ 936 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,626,742 • ❤️ 4,614 • 20d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 144 • 💬 6 • ⭐ 107,870 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 176 • 💬 19 • ⭐ 67,491 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 209 • 💬 3 • ⭐ 4,231 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 9,971 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://huggingface.co/papers/2609.20519)**

*Haozhe Liu, Tian Ye, Sensen Gao et al. (14 authors)*

🏢 NVIDIA

As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \8.75-13.50 relative to native Codex and Claude Code harnesses, and \4.36-5.71 relative to Pi.

▲ 96 • 💬 3 • ⭐ 2,762 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.20519) • [💻 code](https://github.com/NVlabs/SoL-Pi) • [🔗 project](https://nvlabs.github.io/SoL-Pi/)

---

**[Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://huggingface.co/papers/2609.14858)**

*Tong Zheng, Xidong Wu, Zheng Zhang et al. (17 authors)*

🏢 Google

Dream-RSI enables scalable recursive self-improvement by using historical discovery replay to evaluate exploration policies offline, reducing costly online evaluations.

▲ 239 • 💬 3 • ⭐ 1,012 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.14858) • [💻 code](https://github.com/zhengkid/Dream-RSI) • [🔗 project](https://dream-rsi.com/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 45 • 💬 1 • ⭐ 33,353 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 88 • 💬 7 • ⭐ 88,702 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI
  Agents](https://huggingface.co/papers/2509.06917)**

*Jiacheng Miao, Joe R. Davis, Jonathan K. Pritchard et al. (4 authors)*

Paper2Agent converts research papers into interactive AI agents to facilitate knowledge dissemination and enable complex scientific queries through natural language.

▲ 46 • 💬 7 • ⭐ 3,214 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06917) • [💻 code](https://github.com/jmiao24/Paper2Agent) • [🔗 project](https://huggingface.co/spaces/Paper2Agent/alphagenome_agent)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 111 • 💬 2 • ⭐ 13,371 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 5.1k • 🔱 1.4k • 13h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.3k • 🔱 206 • 2h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.7k • 🔱 183 • 15h ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.3k • 🔱 42 • 2h ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 2.2k • 🔱 228 • 26d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 1.8k • 🔱 192 • 9h ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 1.7k • 🔱 324 • 4d ago

---

**[jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)**

Professional agent skills for screenwriting, television writing and dramaturgy

`Python` `ai` `skills`

⭐ 1.3k • 🔱 150 • 5d ago

---

**[adtexterry-lgtm/unigit-ecosystem](https://github.com/adtexterry-lgtm/unigit-ecosystem)**

UNIGIT public brand and ecosystem hub — AI should work for everyone.

`JavaScript` `agentic-ai` `ai-tools` `ai-workbench` `ecosystem` `mcp`

⭐ 1.3k • 🔱 45 • 19d ago

---

**[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)**

An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔哩哔哩等平台。

`Python` `agent` `agent-skill` `content-automation` `content-creation` `content-generation`

⭐ 1.3k • 🔱 185 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
