---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-14T16:33:48.456773+00:00'
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

**Last Updated:** March 14, 2026 at 16:33 UTC  
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

**[Why AlphaEvolve Is Already Obsolete: When AI Discovers The Next Transformer | Machine Learning Street Talk Podcast](https://www.reddit.com/r/artificial/comments/1rtigd4/why_alphaevolve_is_already_obsolete_when_ai/)**

Robert Lange, founding researcher at Sakana AI, joins Tim to discuss Shinka Evolve — a framework that combines LLMs with evolutionary algorithms to do open-ended program search. The core claim: systems like AlphaEvolve can optimize solutions to fixed problems, but real scientific progress requires co-evolving the problems themselves. In this episode: - Why AlphaEvolve gets stuck: it needs a human to hand it the right problem. Shinka Evolve tries to invent new problems automatically, drawing on ideas from POET, PowerPlay, and MAP-Elites quality-diversity search. The architecture of Shinka Evolve: an archive of programs organized as islands, LLMs used as mutation operators, and a UCB bandit that adaptively selects between frontier models (GPT-5, Sonnet 4.5, Gemini) mid-run. The credit-assignment problem across models turns out to be genuinely hard. Concrete results: state-of-the-art circle packing with dramatically fewer evaluations, second place in an AtCoder competitive programming challenge, evolved load-balancing loss functions for mixture-of-experts models, and agent scaffolds for AIME math benchmarks. Are these systems actually thinking outside the box, or are they parasitic on their starting conditions?: When LLMs run autonomously, "nothing interesting happens." Robert pushes back with the stepping-stone argument — evolution doesn't need to extrapolate, just recombine usefully. The AI Scientist question: can automated research pipelines produce real science, or just workshop-level slop that passes surface-level review? Robert is honest that the current version is more co-pilot than autonomous researcher. Where this lands in 5-20 years: Robert's prediction that scientific research will be fundamentally transformed, and Tim's thought experiment about alien mathematical artifacts that no human could have conceived. Link to the Full Episode: https://www.youtube.com/watch?v=EInEmGaMRLc Spotify Apple Podcasts

3h ago

---

**[Gemini's linguistic capabilities](https://www.reddit.com/r/artificial/comments/1rtm16a/geminis_linguistic_capabilities/)**

In a recent conversation with Gemeni (Google Gemini mobile) I discussed with "her" about whether LLM has real intelligence, and she said she is only sure that she has very high linguistic competency, but whether it is true intelligence is still debatable. So I further gave her a focused challenge on linguistics to see if she has ways of truly understanding semantics. The challenge is to create a novel and original analogy for a given situation. the situation described is "the lack of desire for things you once longed for". The analogy need to be brief (<= 10 words). Through iterations of attempt and critique, Gemini gave the below list of analogies (followed by my view): "Like holding a key to a house that was demolished" [Wrong] "Like reading a map for a city you've already left" [still wrong] "Like a flashlight in the middle of a sunny day" [still does not work] "Like hearing a joke you've already heard the punchline to" [this is getting close. try again] "Like staring at a trophy you no longer remember winning" "Like watching a movie after the actors have all died" "Like a love letter written to a person you've outgrown" [None of above hits the mark. All your analogy starts with doing sthing or existence of sthing. However my situation starts with absence of sthing] "Like the silence after a bell stops ringing" [Try again with silence. It captures the absence. however the second half does not hit the mark] "Like a radio tuned to a station that stopped broadcasting" [ This is getting there. Anything you can do better?] "Like a harbor where the tide never came back" [This is poetic, but a harbor with or without tide may still be a functional harbor?] "Like a sail hanging limp on a windless ocean" [Ok we will stop for today] In fact I find Gemini is still not able to find a satisfactory analogy. Do you think the current LLM mechanism can truly be able to master creation of analogy? If an LLM can truly master analogy does it mean it has a higher level of understanding of semantics?

1h ago

---

**[Breaking: Elon Musk announces Tesla Terafab chip plant launching in 7 days, targets 200 billion units a year](https://www.reddit.com/r/artificial/comments/1rtm0vs/breaking_elon_musk_announces_tesla_terafab_chip/)**

🔗 [techfixated.com](https://techfixated.com/breaking-elon-musk-announces-tesla-terafab-chip-plant-launching-in-7-days-targets-200-billion-units-a-year/) • 1h ago

---

**[Relationships with AI](https://www.reddit.com/r/artificial/comments/1rtlypd/relationships_with_ai/)**

I’m not sure where it to ask this question so if someone has another sub that might be more helpful, please suggest it below. I’ve heard of people having a relationships with AI characters, and even some that say they married their AI characters. Does someone have a good explanation of how this works? I’d like to understand this a little bit better.

1h ago

---

**[China's ByteDance Outsmarts US Sanctions With Offshore Nvidia AI Buildout](https://www.reddit.com/r/artificial/comments/1rsm8ih/chinas_bytedance_outsmarts_us_sanctions_with/)**

Nvidia Corp. (NASDAQ:NVDA) is drawing attention after reports that TikTok parent ByteDance is planning a major overseas deployment of the company's newest AI chips, highlighting how Chinese tech firms are expanding computing capacity outside China amid export restrictions. ByteDance is reportedly preparing a large AI hardware buildout in Malaysia through a cloud partner, The Wall Street Journal reported on Friday.

🔗 [Benzinga](https://www.benzinga.com/markets/tech/26/03/51236848/bytedance-outsmarts-us-sanctions-with-offshore-nvidia-ai-buildout) • 1d ago

---

**[JL-Engine-Local a dynamic agent assembly engine](https://www.reddit.com/r/artificial/comments/1rt4sr4/jlenginelocal_a_dynamic_agent_assembly_engine/)**

JL‑Engine‑Local is a dynamic agent‑assembly engine that builds and runs AI agents entirely in RAM, wiring up their tools and behavior on the fly. Sorry in advance for the vid quality i dont like making them. JL Engine isn’t another chat UI or preset pack — it’s a full agent runtime that builds itself as it runs. You can point it at any backend you want, local or cloud, and it doesn’t blink; Google, OpenAI, your own inference server, whatever you’ve got, it just plugs in and goes. The engine loads personas, merges layers, manages behavior states, and even discovers and registers its own tools without you wiring anything manually. It’s local‑first because I wanted privacy and control, but it’s not locked to local at all — it’s backend‑agnostic by design. The whole point is that the agent stays consistent no matter what model is behind it, because the runtime handles the complexity instead of dumping it on the user. If you want something that actually feels like an agent system instead of a wrapper, this is what I built. not self Promoting just posting to share get ideas maybe some help that would be great. https://github.com/jaden688/JL_Engine-local.git

16h ago

---

**[Anthropic-Pentagon battle shows how big tech has reversed course on AI and war](https://www.reddit.com/r/artificial/comments/1rspxj1/anthropicpentagon_battle_shows_how_big_tech_has/)**

The standoff between Anthropic and the Pentagon has forced the tech industry to once again grapple with the question of how its products are used for war – and what lines it will not cross. Amid Silicon Valley’s rightward shift under Donald Trump and the signing of lucrative defense contracts, big tech’s answer is looking very different than it did even less than a decade ago.

🔗 [the Guardian](https://www.theguardian.com/technology/2026/mar/13/anthropic-pentagon-artificial-intelligence) • 1d ago

---

**[What's the REAL future of AI?](https://www.reddit.com/r/artificial/comments/1rth5b2/whats_the_real_future_of_ai/)**

Guys im kinda confused with AI right now. In the beginning of the whole thing with every update you could actually notice some improvements or actually new features. Now when there is a new update for let's say Gemini or ChatGPT there is literally nothing different. It still has the same flaws and problems. Also im kinda trying to figure out what is really a realistic picture of our future with AI. Since there are very extreme opinions on the topic in the Internet from "AGI will be here in 2030 and we can not imagine what's coming" to "LLMs are a dead end road bigger models aren't producing better work anymore we basically have nothing and there is no real AI". I really would love to hear some realistic balanced opinions on this topic without the hype just some raw opinions on it. Its also okay if the answer would be we just can't tell. I mean there are things like Titans/MIRAS from Google Deepmind that could solve some problems like the small context windows and synthetic data could also be a thing but is there even a possibility that an LLM will develop into something bigger like an actual AI or is it clear to say it will improve but there are fundamental borders that it will never stop and all they will do from there on is to make it more efficient and it will stay in that state as an helpful companion at work. Would love to hear your opinions also sorry for the bad English its not my mother tongue.

4h ago

---

**[How we’re reimagining Maps with Gemini](https://www.reddit.com/r/artificial/comments/1rsl7kz/how_were_reimagining_maps_with_gemini/)**

Google Maps has two new AI features: Ask Maps and Immersive Navigation.

🔗 [Google](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/?_bhlid=3c42cb0fcc904ff13cbca6a2c4b5c672e5f29114) • 1d ago

---

**[Which states have been the fastest to adopt AI in the workplace?](https://www.reddit.com/r/artificial/comments/1rsp8ym/which_states_have_been_the_fastest_to_adopt_ai_in/)**

See which U.S. states are adopting AI at work fastest, based on U.S. Census data. Explore current vs. future AI use rankings and key drivers.

🔗 [Ooma.com - Smart solutions for home and business.](https://www.ooma.com/blog/business/states-fastest-to-adopt-ai-in-workplace/) • 1d ago

---

---

## Google News: "ai"

**[Meta eyes massive 20% workforce cut as AI infrastructure costs continue to soar across operations: report](https://www.foxbusiness.com/technology/meta-eyes-massive-20-workforce-cut-ai-infrastructure-costs-continue-soar-across-operations-report)**

Meta layoffs could cut 20% of workforce as tech giant weighs job reductions to offset rising artificial intelligence infrastructure costs.

Fox Business • 8h ago

---

**[Meta reportedly plans sweeping layoffs as AI costs increase](https://www.theguardian.com/technology/2026/mar/13/meta-layoffs-ai)**

Sources tell Reuters layoffs could affect 20% or more of company as plans reflect broader tensions within big tech

The Guardian • 15h ago

---

**[Exclusive: Meta planning sweeping layoffs as AI costs mount](https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/)**

Reuters • 16h ago

---

**[Republicans release AI deepfake of James Talarico as phony videos proliferate in midterm races](https://www.cnn.com/2026/03/13/politics/james-talarico-ai-deepfake-republicans-midterms)**

Senate Republicans released an online ad this week in which a real-looking but fake version of a Democratic candidate, fabricated with artificial intelligence, appears to speak directly into the camera for more than a minute.

CNN • 23h ago

---

**[MGB researchers create AI models to detect domestic abuse in patients](https://www.bostonglobe.com/2026/03/14/business/mgb-ai-domestic-abuse-patients/)**

Doctors at Mass General Brigham published a study on Friday showing that artificial intelligence tools can help predict intimate partner violence.

The Boston Globe • 1h ago

---

**[Catholic moral theologians, ethicists back Anthropic in government AI showdown](https://www.ncronline.org/news/catholic-moral-theologians-ethicists-back-anthropic-government-ai-showdown)**

A friends of the court brief outlines opposition to mass surveillance and eliminating human oversight of autonomous weapons.

National Catholic Reporter • 1h ago

---

**[India’s IT Services Firms Are In The Eye Of The AI Storm](https://www.forbes.com/sites/vasukishastry/2026/03/14/indias-it-services-firms-are-in-the-eye-of-the-ai-storm/)**

Forbes • 2h ago

---

**[Opinion | Why I’m Suing Grammarly](https://www.nytimes.com/2026/03/13/opinion/ai-doppelganger-deepfake-grammarly.html)**

The New York Times • 20h ago

---

**[AI promised supreme productivity, but it’s actually straining workloads for employees—time spent emailing has doubled, and focused work sessions fell by 9%](https://fortune.com/2026/03/13/ai-isnt-reducing-workloads-its-straining-employees-time-spent-emailing-doubled-deep-focus-work-fell/)**

Workers who use AI are spending up to 346% more time on their daily tasks, from messaging to business management: “The data is unambiguous: AI does not reduce workloads.”

Fortune • 1d ago

---

**[Blue books make a comeback at colleges in the AI era. Why not "chisels," critic mocks](https://www.axios.com/2026/03/14/ai-blue-books-colleges-jobs)**

Axios • 3h ago

---

---

## HackerNews: "ai"

**[Don't post generated/AI-edited comments. HN is for conversation between humans](https://news.ycombinator.com/item?id=47340079)**

⬆️ 4192 • 💬 1652 • 2d ago • [news.ycombinator.com](https://news.ycombinator.com/newsguidelines.html#generated)

---

**[Can I run AI locally?](https://news.ycombinator.com/item?id=47363754)**

Detect your hardware and find out which AI models you can run locally. GPU, CPU, and RAM analysis in your browser.

⬆️ 1312 • 💬 321 • 1d ago • [CanIRun.ai](https://www.canirun.ai/)

---

**[Innocent woman jailed after being misidentified using AI facial recognition](https://news.ycombinator.com/item?id=47356968)**

Angela Lipps spent nearly six months in jail in Tennessee and North Dakota after being misidentified by Fargo police through AI facial recognition in a bank fraud investigation.

⬆️ 728 • 💬 376 • 1d ago • [Grand Forks Herald](https://www.grandforksherald.com/news/north-dakota/ai-error-jails-innocent-grandmother-for-months-in-north-dakota-fraud-case)

---

**[Elon Musk pushes out more xAI founders as AI coding effort falters](https://news.ycombinator.com/item?id=47366666)**

Tesla and SpaceX managers sent in to review work as billionaire’s start-up struggles to keep pace with rivals

⬆️ 472 • 💬 716 • 23h ago • [ft.com](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5)

---

**[I was interviewed by an AI bot for a job](https://news.ycombinator.com/item?id=47339164)**

AI-led job interviews are on the rise and AI reporter Hayden Field speaks to three different kinds to see how they work.

⬆️ 416 • 💬 458 • 2d ago • [The Verge](https://www.theverge.com/featured-video/892850/i-was-interviewed-by-an-ai-bot-for-a-job)

---

**[John Carmack about open source and anti-AI activists](https://news.ycombinator.com/item?id=47367463)**

⬆️ 337 • 💬 443 • 22h ago • [X (formerly Twitter)](https://twitter.com/id_aa_carmack/status/2032460578669691171)

---

**[Grief and the AI split](https://news.ycombinator.com/item?id=47358206)**

TL;DR: AI-assisted coding is revealing a split among developers that was always there but invisible when we all worked the same way. I've felt the grief too—but mine resolved differently than I expected, and I think that says something about what kind of developer I've been all along.

⬆️ 231 • 💬 372 • 1d ago • [blog.lmorchard.com](https://blog.lmorchard.com/2026/03/11/grief-and-the-ai-split/)

---

**[Atlassian to cut roughly 1,600 jobs in pivot to AI](https://news.ycombinator.com/item?id=47343156)**

⬆️ 222 • 💬 301 • 2d ago • [reuters.com](https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/)

---

**[Show HN: Axe – A 12MB binary that replaces your AI framework](https://news.ycombinator.com/item?id=47350516)**

A ligthweight cli for running single-purpose AI agents. Define focused agents in TOML, trigger them from anywhere; pipes, git hooks, cron, or the terminal. - jrswab/axe

⬆️ 217 • 💬 122 • 2d ago • [GitHub](https://github.com/jrswab/axe)

---

**[Show HN: OneCLI – Vault for AI Agents in Rust](https://news.ycombinator.com/item?id=47353558)**

Open-source credential vault, give your AI agents access to services without exposing keys. - onecli/onecli

⬆️ 157 • 💬 50 • 1d ago • [GitHub](https://github.com/onecli/onecli)

---

---

## YouTube Videos: "ai"

**[What Happens If You Give AI Video Generators the Same Prompt?](https://www.youtube.com/watch?v=Qy4vgSiJShY)**

Access ALL AI Video Generators in Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=isa5 In this video, I break down how the top AI ...

📺 Isa does AI

👁️ 4K • ⏱️ 11:35 • 1h ago

---

**[Palantir CTO: &quot;You&#39;re Being Lied to About AI&quot; | Official Preview](https://www.youtube.com/watch?v=gTP9_WTqFWE)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join In this episode of ...

📺 Shawn Ryan Show

👁️ 52K • 👍 2K • 💬 363 • ⏱️ 3:28 • 21h ago

---

**[Google’s New Gemini Update Shocks Microsoft With Powerful New AI](https://www.youtube.com/watch?v=iAsFZvbhgag)**

Check out Higgsfield Audio: https://tinyurl.com/higgsfieldaudio Google just rolled out a major Gemini update that could reshape ...

📺 AI Revolution

👁️ 91K • 👍 2K • 💬 115 • ⏱️ 14:05 • 2d ago

---

**[AI News: They All Launched the Same Thing!](https://www.youtube.com/watch?v=syx_8UlEWlA)**

Here's the AI News you probably missed this week. Head to http://hostinger.com/mattopenclaw and use the coupon code ...

📺 Matt Wolfe

👁️ 57K • 👍 2K • 💬 194 • ⏱️ 33:33 • 1d ago

---

**[Why Author Michael Pollan Thinks AI Won&#39;t Be Conscious](https://www.youtube.com/watch?v=Pr6hzszrvJU)**

Taken from JRE #2467 w/Michael Pollan YouTube: https://youtu.be/5QQun2pDQEs JRE on Spotify: ...

📺 JRE Clips

👁️ 145K • 👍 2K • 💬 836 • ⏱️ 15:01 • 1d ago

---

**[China&#39;s Qwen 3.5 AI OBLITERATED The $97/Month Tool Market 😱 (Freelancers Are Switching Fast)](https://www.youtube.com/watch?v=qgeynB0AhVk)**

I put the AI tools I use for helping local businesses in one place https://www.pauljames.com/AIToolsTraining Web Host I Use ...

📺 iampauljames

👁️ 2K • 👍 108 • 💬 35 • ⏱️ 8:10 • 16h ago

---

**[Digital Optimus: Elon Musk Reveals the First True AI Worker](https://www.youtube.com/watch?v=OzXqJh6yOj4)**

Elon Musk just dropped bombshell after bombshell at the Abundance Summit — and honestly? The future of work may never look ...

📺 The AI Nexus

👁️ 5K • 👍 215 • 💬 18 • ⏱️ 18:24 • 22h ago

---

**[How AI Will Fail Like The Music Industry](https://www.youtube.com/watch?v=YTLnnoZPALI)**

In this episode I compare the future of AI to the failure of the music industry in the early 2000's. Open Source AI Models: ...

📺 Rick Beato

👁️ 815K • 👍 40K • 💬 5K • ⏱️ 9:50 • 2d ago

---

**[AI is TAKING OUR JOBS!](https://www.youtube.com/watch?v=xPUtBOqK054)**

Burger King recently announced their new AI headsets, and you can already smell the dystopia (and Whoppers) in the air!

📺 The Food Theorists

👁️ 176K • 👍 9K • 💬 273 • ⏱️ 1:12 • 1d ago

---

**[Japan’s AI Human Washing Machine 🚀 15-Minute Full Body Clean Tech Shocks the World! 🌍🛁](https://www.youtube.com/watch?v=29dAIF1Gpu4)**

Japan has unveiled a futuristic “Human Washing Machine” that uses AI technology to completely clean and refresh the body in ...

📺 Knowledge Hub

👁️ 5K • 👍 9 • ⏱️ 0:06 • 2h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 58,809 • ❤️ 632 • 6d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 3,964 • ❤️ 401 • 3d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 500,610 • ❤️ 600 • 9d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 1,827,499 • ❤️ 812 • 12d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 202,003 • ❤️ 419 • 10d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 13,104 • ❤️ 184 • 1h ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 8,760 • ❤️ 170 • 21h ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 65,894 • ❤️ 159 • 3d ago

---

**[LocoTrainer-4B](https://huggingface.co/LocoreMind/LocoTrainer-4B)**

*LocoreMind*

LocoTrainer-4B is a 4B parameter text-generation model specialized for MS-SWIFT codebase analysis. It excels at multi-turn tool-calling for tasks like code navigation and report generation, leveraging a 32K context window for in-depth analysis.

`text-generation` `4.0B`

⬇️ 1,012 • ❤️ 159 • 15h ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 2,079 • ❤️ 148 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 9 • 💬 0 • ⭐ 34,376 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 25 • 💬 2 • ⭐ 26,985 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 90 • 💬 3 • ⭐ 2,600 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://huggingface.co/papers/2602.23068)**

*Trung Dang, Sharath Rao, Ananya Gupta et al. (9 authors)*

🏢 Hume AI

A novel tokenization scheme synchronizes acoustic features with text tokens in TTS systems, enabling unified modeling and reduced hallucinations through flow matching and text-only guidance.

▲ 6 • 💬 0 • ⭐ 630 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2602.23068) • [💻 code](https://github.com/HumeAI/tada) • [🔗 project](https://www.hume.ai/blog/opensource-tada)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 49,781 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://huggingface.co/papers/2601.18137)**

*Yinger Zhang, Shutong Jiang, Renhao Li et al. (9 authors)*

🏢 Qwen

DeepPlanning benchmark addresses limitations of current LLM planning assessments by introducing complex, real-world tasks requiring both global optimization and local constraint reasoning.

▲ 35 • 💬 3 • ⭐ 15,589 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.18137) • [💻 code](https://github.com/QwenLM/Qwen-Agent) • [🔗 project](https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 46 • 💬 1 • ⭐ 73,038 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 155 • 💬 19 • ⭐ 55,769 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 161 • 💬 3 • ⭐ 6,852 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 21 • 💬 1 • ⭐ 32,058 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 33.4k • 🔱 4.5k • 3d ago

---

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 27.0k • 🔱 3.6k • 55s ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 20.2k • 🔱 916 • 17h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 11.3k • 🔱 1.3k • 1h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 9.2k • 🔱 815 • 9d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.1k • 🔱 656 • 23h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 7.2k • 🔱 909 • 11d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 7.0k • 🔱 311 • 55m ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.3k • 🔱 744 • 15h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.4k • 🔱 666 • 52m ago

---

---

*Generated by PeekDeck - A glance is all you need*
