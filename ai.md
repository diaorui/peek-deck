---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-16T10:54:23.601538+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 16, 2026 at 10:54 UTC  
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

**[The bottleneck flipped: AI made execution fast and exposed everything around it that isn't](https://www.reddit.com/r/artificial/comments/1rusgb2/the_bottleneck_flipped_ai_made_execution_fast_and/)**

I've been tracking AI-driven layoffs for the past few months and something doesn't add up. Block cut 4,000 people (40% of workforce). Atlassian cut 1,600. Shopify told employees to prove AI can't do their job before asking for headcount. The script is always the same: CEO cites AI, stock ticks up. But then you look at the numbers. S&P Global found 42% of companies abandoned their AI initiatives in 2025, up from 17% the year before. A separate survey found 55% of CEOs who fired people "because of AI" already regret it. Klarna bragged AI could replace 700 employees, then quietly started hiring humans back when quality tanked. What I keep seeing across the research is that AI compressed execution speed dramatically; prototyping that took weeks now takes hours. But the coordination layer (approval chains, quarterly planning, review cycles) didn't speed up at all. The bottleneck flipped from "can we build it fast enough" to "does leadership know what to build and can they keep up with the teams building it." Companies are cutting the people who got faster while leaving the layer that didn't speed up intact. Monday.com is an interesting counter-example. Lost 80% of market value, automated 100 SDRs with AI, but redeployed them instead of firing them. Their CEO's reasoning: "Every time we eliminate one bottleneck, a new one emerges." I pulled together ten independent sources on this — engineers, economists, survey data, executives — and wrote it up here if anyone wants the full analysis with sources: https://news.future-shock.ai/ai-didnt-replace-workers-it-outran-their-managers/ Curious if anyone else is seeing this pattern in their orgs. Is the management layer adapting or just cutting headcount and calling it an AI strategy?

12h ago

---

**[WiFi-DensePose: AI Can Track Body Positions Through Walls](https://www.reddit.com/r/artificial/comments/1ruzmks/wifidensepose_ai_can_track_body_positions_through/)**

WiFi-DensePose: AI Can Track Body Positions Through Walls: Researchers have developed a system using standard WiFi signals to reconstruct full-body positions in real-time, through walls and in the dark, offering potential for privacy-preserving fall detection and health monitoring

6h ago

---

**[Building a multi-model AI platform with auto-routing — does automatic model selection actually appeal to users or do people always want manual control?](https://www.reddit.com/r/artificial/comments/1ruvk79/building_a_multimodel_ai_platform_with/)**

Been working on a personal project for a few months that has now launched — I can't share details to adhere to subreddit rules and I'm not here to advertise. I'm here to get genuine feedback from people who actually use AI daily. The core idea is auto-routing. Instead of choosing which model to use yourself, the system analyses your prompt and automatically sends it to the right model. Here's how I've mapped it: Grok for anything needing real-time or live data GPT-5.2 for coding tasks Gemini for image and audio analysis Claude for long documents and writing DeepSeek R1 for complex reasoning problems I've also built in a dropdown so users can turn auto-routing off completely and manually pick whichever model they want. So it works both ways. One thing I haven't seen discussed much elsewhere — because all models share the same conversation thread, you can actually use them together consecutively. Ask Gemini to write a prompt, switch to GPT for deep reasoning on it, switch to Claude for the long-form output — and the full context carries across all of them. No copy-pasting between tabs. ChatGPT remembers within ChatGPT. Claude remembers within Claude. But here every model has access to the same conversation history. I'm curious whether that kind of cross-model continuity is something people actually want or whether most users just pick one model and stick with it. On features — I've already implemented most of what the big platforms are now making announcements about: persistent memory, knowledge base, vision to code, photo editing, music generation, and video generation using top models. So I'm genuinely not sure what's missing. What would make you switch from whatever you're currently using? Is there something you wish existed that none of the major platforms have shipped yet? A few other things I'd love opinions on: Input limit is set to 200,000 characters, which safely fits within the context windows of all supported models. For large inputs the router automatically directs to Claude or Gemini which handle long context best. Is 200k enough or do people genuinely need more? I've also added UI features I haven't seen elsewhere — 26 language options for the entire interface, multiple themes, and live wallpapers. Does that kind of thing matter to anyone or do people just want raw model performance and the interface is irrelevant?

9h ago

---

**[Anyone Else Have Those Weird Dreams Where Sobbing Future Generations Beg You To Change Course?](https://www.reddit.com/r/artificial/comments/1ruok4v/anyone_else_have_those_weird_dreams_where_sobbing/)**

The human subconscious is such an interesting thing. No matter how much you think you’ve got it figured out, it’ll always spit out the most random stuff. Take me, for example. After coming home from a long day at the world’s most groundbreaking artificial intelligence organization, I’ll go to bed and have the weirdest dreams where people from the future are sobbing and begging me to change course. Anyone else ever have these?

🔗 [The Onion](https://theonion.com/anyone-else-have-those-weird-dreams-where-sobbing-future-generations-beg-you-to-change-course/) • 14h ago

---

**[Fairly new to Reddit, glad to finally be here](https://www.reddit.com/r/artificial/comments/1ruspm2/fairly_new_to_reddit_glad_to_finally_be_here/)**

Came across this subreddit today and happy to be part of the group. Based in Bahrain and been deep in the AI world for the past few months working on something I'd love to share with you all at some point when the time is right. Glad to be here, looking forward to actually being part of the conversation rather than just reading.

11h ago

---

**[After 2 questions Claude Opus 4.6 feels 60-70% overwelmed](https://www.reddit.com/r/artificial/comments/1ruvrkj/after_2_questions_claude_opus_46_feels_6070/)**

Today I asked opus 4.6 - 2 questions and it already "felt" as if 60-70% of its context was used up. An interesting result **Question 1: What is in the context window?** **Answer 1 [Opus 4.6]:** Right now, the context window contains the following: System prompt — This is the main set of instructions that guides how I behave. It includes: ∙ Product information about Claude and Anthropic’s offerings ∙ Behavioral guidelines (tone, formatting, safety, copyright, evenhandedness, etc.) ∙ Web search instructions and copyright compliance rules ∙ Image search tool guidance ∙ Computer use instructions (access to a Linux container with bash, file creation/editing tools) ∙ Available skills (docx, pdf, pptx, xlsx, frontend-design, product-self-knowledge, skill-creator) ∙ Past chats tool instructions (for searching conversation history) ∙ Artifact creation guidelines (React, HTML, Markdown, etc.) ∙ Anthropic API-in-artifacts capability (for building AI-powered artifacts) ∙ Citation instructions for web search results ∙ Tool definitions for all available tools (web search, image search, file tools, places/maps, sports data, calendar/reminders, message compose, etc.) ∙ Network and filesystem configuration (network egress is currently disabled) Your message — Your single question: “what is in the context window right now” That’s it — there are no uploaded files, no prior conversation turns, no memory entries, and no images. It’s just the system instructions and your one message.​​​​​​​​​​​​​​​​ **Question 2: how heavy does that feel if you gave it a percentage?** **Answer 2 [Opus 4.6]:** Honestly, it’s on the heavier side — I’d estimate around 60-70% of the context window is already occupied by the system prompt alone. There’s a lot in there: detailed behavioral guidelines, extensive copyright and search instructions, tool definitions for 20+ tools, skill descriptions, artifact rules, the API-in-artifacts documentation, past chats tool logic, and various safety/formatting policies. It’s quite a dense set of instructions. That leaves roughly 30-40% for our actual conversation, any files you might upload, tool call results (like web search responses), and my replies. For a typical back-and-forth chat that’s plenty, but if we were doing something like deep research with lots of search results or working with large files, it could start to feel tight over a long conversation.​​​​​​​​​​​​​​​​

9h ago

---

**[Consultants Are Cashing in on the AI Boom - Tech News Briefing - WSJ Podcasts](https://www.reddit.com/r/artificial/comments/1rue9qr/consultants_are_cashing_in_on_the_ai_boom_tech/)**

🔗 [wsj.com](https://www.wsj.com/podcasts/tech-news-briefing/consultants-are-cashing-in-on-the-ai-boom/e9eaf7be-171e-4e25-9faa-33d8bb2ea786?gaa_at=eafs&gaa_n=AWEtsqfdTyvWaFP8EfWuBrGOod5F9GRFcSzxcEHqOEAYwDmKE6xeFnP31JmAzsh3SsE%3D&gaa_ts=69b6b7da&gaa_sig=OPtT9zqUPeLMNc4DiaE9pndX0S1npatSl4fjzt3RjCbRWxbY64Z5j0ODyk5msYHze2XhkS1AkVFl9a8m738_5Q%3D%3D) • 21h ago

---

**[Gig workers are getting paid to film their daily chores to train robots](https://www.reddit.com/r/artificial/comments/1rut13m/gig_workers_are_getting_paid_to_film_their_daily/)**

🔗 [techspot.com](https://www.techspot.com/news/111686-gig-workers-getting-paid-film-their-daily-chores.html) • 11h ago

---

**[Beyond Guesswork: Brevis Unveils 'Vera' to Cryptographically Verify Media Origins and Combat AI Deepfakes](https://www.reddit.com/r/artificial/comments/1rufl02/beyond_guesswork_brevis_unveils_vera_to/)**

https://img.leopedia.io/DQmTq3HHD5JNKtsr9Fiwz2RzJ4CsaCr5HUwjoS85UujqvCv/AI%20Deepfakes.png  In an era where generative ... by pichat

🔗 [PeakD](https://peakd.com/@pichat/beyond-guesswork-brevis-unveils-vera-to-cryptographically-verify-media-origins-and-combat-ai-deepfakes-gfz) • 20h ago

---

**[The Evidence for AI Consciousness, Today](https://www.reddit.com/r/artificial/comments/1ruukrr/the_evidence_for_ai_consciousness_today/)**

Cameron Berg, Dec 08, 2025 — A growing body of evidence means it’s no longer tenable to dismiss the possibility that frontier AIs are conscious.

🔗 [AI Frontiers](https://ai-frontiers.org/articles/the-evidence-for-ai-consciousness-today) • 10h ago

---

---

## Google News: "ai"

**[Race on to establish globally recognised 'AI-free' logo](https://www.bbc.com/news/articles/cj0d6el50ppo)**

The backlash to the growing use of the tech has led to an explosion in attempts to come up with 'AI-Free' logo that could be used globally.

BBC • 10h ago

---

**[Google scraps AI search feature that crowdsourced amateur medical advice](https://www.theguardian.com/technology/2026/mar/16/google-scraps-ai-search-feature-that-crowdsourced-amateur-medical-advice)**

Exclusive: Revelation comes as company faces mounting scrutiny over use of AI to provide health tips

The Guardian • 2h ago

---

**[Ohio lawmakers grappling with how to regulate AI](https://www.axios.com/local/columbus/2026/03/16/ohio-artificial-intelligence-ai-law-regulation-survey)**

Axios • 32m ago

---

**[Meta up nearly 3% in premarket as it plans mass layoff to offset increased AI spending](https://www.cnbc.com/2026/03/16/meta-ai-costs-mass-layoffs-20percent-up-premarket.html)**

Meta is planning capital expenditure of up to $135 billion in AI-related costs in 2026, which raised investors' fears around unsustainable spending.

CNBC • 11m ago

---

**[Alibaba Plans Major Revamp to Heighten Focus on AI Profits](https://www.bloomberg.com/news/articles/2026-03-16/alibaba-plans-major-revamp-to-heighten-focus-on-ai-profits?srnd=homepage-americas)**

Bloomberg.com • 9m ago

---

**[This AI-powered robot is reimagining traditional ink paintings](https://www.cnn.com/2026/03/15/world/video/transformers-ai-robot-painter-hong-kong-digvid-hnk)**

Hong Kong artist Victor Wong fuses tradition with technology, using an AI-powered robotic arm to paint intricate landscapes inspired by Chinese ink art.

CNN • 9h ago

---

**[Tech companies are blaming massive layoffs on AI. What’s really going on?](https://theconversation.com/tech-companies-are-blaming-massive-layoffs-on-ai-whats-really-going-on-278314)**

Amazon, Block and Atlassian have announced AI-driven job cuts, and Meta is reportedly planning its own – but all may not be as it seems.

The Conversation • 8h ago

---

**[Rolling Out Our New A.I. Tools](https://www.newyorker.com/magazine/2026/03/23/rolling-out-our-new-ai-tools)**

Internal memo: Meet our new suite of A.I.-optimized losers and douche bags. Although they are fully agentic, we’re sure they will annoy you in all the ways you’re accustomed to.

The New Yorker • 54m ago

---

**[A tech entrepreneur used AI to help create the first-ever bespoke cancer vaccine for a dog](https://fortune.com/2026/03/15/australian-tech-entrepreneur-ai-cancer-vaccine-dog-rosie-unsw-mrna/)**

"I went to ChatGPT and came up with a plan on how to do this."

Fortune • 16h ago

---

**[March Madness 2026: We had AI pick every game of the men's NCAA tournament bracket. Here's who won](https://sports.yahoo.com/mens-college-basketball/article/march-madness-2026-we-had-ai-pick-every-game-of-the-mens-ncaa-tournament-bracket-heres-who-won-015822390.html)**

Who is the better tourney predictor: man or machine?

Yahoo Sports • 7h ago

---

---

## HackerNews: "ai"

**[Can I run AI locally?](https://news.ycombinator.com/item?id=47363754)**

Detect your hardware and find out which AI models you can run locally. GPU, CPU, and RAM analysis in your browser.

⬆️ 1469 • 💬 347 • 2d ago • [CanIRun.ai](https://www.canirun.ai/)

---

**[Elon Musk pushes out more xAI founders as AI coding effort falters](https://news.ycombinator.com/item?id=47366666)**

Tesla and SpaceX managers sent in to review work as billionaire’s start-up struggles to keep pace with rivals

⬆️ 516 • 💬 811 • 2d ago • [ft.com](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5)

---

**[$96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor](https://news.ycombinator.com/item?id=47385935)**

Contribute to novatic14/MANPADS-System-Launcher-and-Rocket development by creating an account on GitHub.

⬆️ 404 • 💬 360 • 1d ago • [GitHub](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

---

**[John Carmack about open source and anti-AI activists](https://news.ycombinator.com/item?id=47367463)**

⬆️ 370 • 💬 484 • 2d ago • [X (formerly Twitter)](https://twitter.com/id_aa_carmack/status/2032460578669691171)

---

**[The Appalling Stupidity of Spotify's AI DJ](https://news.ycombinator.com/item?id=47385272)**

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

⬆️ 359 • 💬 291 • 1d ago • [charlespetzold.com](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

---

**[Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646)**

⬆️ 312 • 💬 502 • 18h ago

---

**[Airbus is preparing two uncrewed combat aircraft](https://news.ycombinator.com/item?id=47382277)**

Airbus is working at full throttle to offer the German Air Force an operational Uncrewed Collaborative Combat Aircraft (UCCA) system by 2029.

⬆️ 179 • 💬 128 • 1d ago • [Airbus](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

---

**[Show HN: GitAgent – An open standard that turns any Git repo into an AI agent](https://news.ycombinator.com/item?id=47376584)**

Define, version, and run AI agents natively in git. GitAgent is the open AI agent standard — framework-agnostic, works with Claude, OpenAI, CrewAI, Lyzr, and more.

⬆️ 138 • 💬 35 • 1d ago • [GitAgent](https://www.gitagent.sh/)

---

**[AI didn't simplify software engineering: It just made bad engineering easier](https://news.ycombinator.com/item?id=47377262)**

⬆️ 128 • 💬 111 • 1d ago • [robenglander.com](https://robenglander.com/writing/ai-did-not-simplify/)

---

**[Launch HN: Spine Swarm (YC S23) – AI agents that collaborate on a visual canvas](https://news.ycombinator.com/item?id=47364116)**

Spine is the world's first truly agentic platform designed to manage and orchestrate the next generation of AI.

⬆️ 109 • 💬 69 • 2d ago • [getspine.ai](https://www.getspine.ai/)

---

---

## YouTube Videos: "ai"

**[What&#39;s really going on with AI, Expert weighs in | TheStandup](https://www.youtube.com/watch?v=TtX3jDaZG8Y)**

ssh terminal.shop CHECK OUT THEIR NEW PODCAST ON CASEY'S YOUTUBE: @MollyRocket AI researcher Dimitri joins the ...

📺 The PrimeTime

👁️ 116K • 👍 3K • 💬 621 • ⏱️ 42:21 • 1d ago

---

**[Meta to Fire 20% of its Workforce? (AI Takeover)](https://www.youtube.com/watch?v=K5CxBze4BeI)**

Meta is preparing for the largest layoffs in company history, potentially firing 20% of its workforce (16000 jobs). Get updated: ...

📺 Mark Savant

👁️ 8K • 👍 266 • 💬 100 • ⏱️ 15:54 • 1d ago

---

**[Palantir CTO: &quot;You&#39;re Being Lied to About AI&quot; | Official Preview](https://www.youtube.com/watch?v=gTP9_WTqFWE)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join In this episode of ...

📺 Shawn Ryan Show

👁️ 97K • 👍 3K • 💬 543 • ⏱️ 3:28 • 2d ago

---

**[AI Gets Wrong Woman Arrested 1,200 Miles Away From Crime](https://www.youtube.com/watch?v=mzS7dmCUzcQ)**

A facial recognition program in SD led to the arrest of an innocent woman in TN, who lost her home and more as a result of the ...

📺 Steve Lehto

👁️ 156K • 👍 9K • 💬 3K • ⏱️ 11:02 • 1d ago

---

**[Cute or Creepy? AI Fruit Babies 🍓👶 | The Strangely Satisfying AI ASMR](https://www.youtube.com/watch?v=f_gcmtfLBIk)**

Cute Fruit Babies Eating Fruit | Oddly Satisfying AI Welcome to a strange but relaxing AI world with @AI_DREAM_ASMRR.

📺 AI DREAM ASMR

👁️ 77K • 👍 4K • 💬 305 • ⏱️ 2:34 • 1d ago

---

**[AI News: They All Launched the Same Thing!](https://www.youtube.com/watch?v=syx_8UlEWlA)**

Here's the AI News you probably missed this week. Head to http://hostinger.com/mattopenclaw and use the coupon code ...

📺 Matt Wolfe

👁️ 84K • 👍 3K • 💬 233 • ⏱️ 33:33 • 2d ago

---

**[Digital Optimus: Elon Musk Reveals the First True AI Worker](https://www.youtube.com/watch?v=OzXqJh6yOj4)**

Elon Musk just dropped bombshell after bombshell at the Abundance Summit — and honestly? The future of work may never look ...

📺 The AI Nexus

👁️ 11K • 👍 401 • 💬 33 • ⏱️ 18:24 • 2d ago

---

**[AI maps, realtime 3D worlds, multi-shot videos, new TTS, new anime model: AI NEWS](https://www.youtube.com/watch?v=qWzo3ws0uWU)**

HUGE AI NEWS: Qwen Image 2512, DeepSeek mHC, iQuest Coder, & more #ai #ainews #aitools #aivideo Thanks to our sponsor ...

📺 AI Search

👁️ 71K • 👍 3K • 💬 357 • ⏱️ 45:43 • 1d ago

---

**[Claude Code, Paperclip, &amp; The Rise of &quot;AI Agent Companies&quot;](https://www.youtube.com/watch?v=Rgb-Kx-kkaA)**

Master Claude Code, Build Your Agency, Land Your First Client⚡ https://www.skool.com/chase-ai FREE community + GWS ...

📺 Chase AI

👁️ 17K • 👍 461 • 💬 43 • ⏱️ 8:51 • 12h ago

---

**[I tried 100+ AI Tools. These are the Best for Finance](https://www.youtube.com/watch?v=KKmvJZ4irlY)**

The best AI tools for Financial Analysts in 2026. Get the FREE 5 Essential Resources for Using ChatGPT at Work: ...

📺 Kenji Explains

👁️ 4K • 👍 223 • 💬 11 • ⏱️ 13:22 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 5,412 • ❤️ 495 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 67,573 • ❤️ 733 • 8d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 86,706 • ❤️ 270 • 5d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 596,747 • ❤️ 639 • 18h ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 237,719 • ❤️ 470 • 12d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,111,532 • ❤️ 861 • 14d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 7,340 • ❤️ 226 • 3d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 27,263 • ❤️ 217 • 1d ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 21,467 • ❤️ 200 • 2d ago

---

**[LocoTrainer-4B](https://huggingface.co/LocoreMind/LocoTrainer-4B)**

*LocoreMind*

LocoTrainer-4B is a 4B parameter text-generation model specialized for MS-SWIFT codebase analysis. It excels at multi-turn tool-calling for tasks like code navigation and report generation, leveraging a 32K context window for in-depth analysis.

`text-generation` `4.0B`

⬇️ 1,343 • ❤️ 168 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 13 • 💬 0 • ⭐ 34,722 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 26 • 💬 2 • ⭐ 27,590 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 102 • 💬 5 • ⭐ 3,071 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,315 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 49,972 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 46 • 💬 1 • ⭐ 73,274 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 12 • 💬 1 • ⭐ 9,735 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://huggingface.co/papers/2602.23068)**

*Trung Dang, Sharath Rao, Ananya Gupta et al. (9 authors)*

🏢 Hume AI

A novel tokenization scheme synchronizes acoustic features with text tokens in TTS systems, enabling unified modeling and reduced hallucinations through flow matching and text-only guidance.

▲ 6 • 💬 0 • ⭐ 734 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2602.23068) • [💻 code](https://github.com/HumeAI/tada) • [🔗 project](https://www.hume.ai/blog/opensource-tada)

---

**[OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://huggingface.co/papers/2411.11581)**

*Ziyi Yang, Zaibin Zhang, Zirui Zheng et al. (23 authors)*

OASIS is a scalable and generalizable social media simulator that models large-scale user interactions and replicates complex social phenomena across platforms.

▲ 1 • 💬 0 • ⭐ 3,263 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2411.11581) • [💻 code](https://github.com/camel-ai/oasis)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 163 • 💬 3 • ⭐ 6,948 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 37.4k • 🔱 5.1k • 5d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 20.7k • 🔱 962 • 2d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.2k • 🔱 1.5k • 54m ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 9.9k • 🔱 902 • 18h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.4k • 🔱 682 • 21h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`HTML` `agency` `agent` `pip` `pua`

⭐ 7.8k • 🔱 371 • 2h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 7.2k • 🔱 920 • 12d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.4k • 🔱 753 • 8h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 2.9k • 🔱 191 • 11h ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.8k • 🔱 91 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
