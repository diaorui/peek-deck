---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-29T09:38:36.110876+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 29, 2026 at 09:38 UTC  
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

**[Persistent memory changes how people interact with AI — here's what I'm observing](https://www.reddit.com/r/artificial/comments/1s6jvog/persistent_memory_changes_how_people_interact/)**

I run a small AI companion platform and wanted to share some interesting behavioral data from users who've been using persistent cross-session memory for 2-3 months now. Some patterns I didn't expect: "Deep single-thread" users dominate. 56% of our most active users put 70%+ of their messages into a single conversation thread. They're not creating multiple characters or scenarios — they're deepening one relationship. This totally contradicts the assumption that users are "scenario hoppers." Memory recall triggers emotional responses. When the AI naturally brings up something from weeks ago — "how did that job interview go?" or referencing a pet's name without being prompted — users consistently react with surprise and increased engagement. It's a retention mechanic that doesn't feel like a retention mechanic. The "uncanny valley" of memory exists. If the AI remembers too precisely (exact dates, verbatim quotes), it feels surveillance-like. If it remembers too loosely, it feels like it didn't really listen. The sweet spot is what I'd call "emotionally accurate but detail-fuzzy" — like how a real friend remembers. Day-7 retention correlates with memory depth. Users who trigger 5+ memory retrievals in their first week retain at nearly 4x the rate of those who don't. The memory system IS the product, not a feature. Sample size is small (~800 users) so take this with appropriate skepticism. But it's consistent enough that I think persistent memory is going to be table stakes for AI companions within a year. What's your experience with memory in AI conversations? Anyone else building in this space?

6h ago

---

**[Claude is the least bullshit-y AI](https://www.reddit.com/r/artificial/comments/1s67buc/claude_is_the_least_bullshity_ai/)**

Just found this “bullshit benchmark,” and sort of shocked by the divergence of Anthropic’s models from other major models (ChatGPT and Gemini). IMO this alone is reason to use Claude over others.

🔗 [GitHub](https://github.com/petergpt/bullshit-benchmark?tab=readme-ov-file#3-detection-rate-over-time) • 15h ago

---

**[The AI hype misses the people who actually need it most](https://www.reddit.com/r/artificial/comments/1s6fws6/the_ai_hype_misses_the_people_who_actually_need/)**

Every day someone posts "AI will change everything" and it's always about agents scaling businesses, automating workflows, 10x productivity, whatever. Cool. But change everything for who? Go talk to the barber who loses 3 clients a week to no-shows and can't afford a booking system that actually works. Go talk to the solo attorney who's drowning in intake paperwork and can't afford a paralegal. Go talk to the tattoo artist who's on the phone all day instead of tattooing. Go talk to the author who wrote a book and has zero idea how to market it. These people don't need another app. They don't need to "learn to code." They don't need to understand what an LLM is. They need the tools that already exist and wired into their actual business. Their actual pain. The gap between "AI can do amazing things" and "I can actually use AI to make my life better" is where most of the world lives right now. And most of the AI community is completely disconnected from that reality. We're on Reddit at midnight debating MCP vs direct API and arguing about whether Opus or Sonnet is better for agent routing. That's not most people. Most people are just trying to survive running a business they started because they're good at something and not because they wanted to become a full-time administrator. If every small business owner, every freelancer, every solo professional had agents handling the repetitive stuff ya kno...the follow-ups, the scheduling, the content, the bookkeeping; you wouldn't just get productivity. You'd get a renaissance. Because people who are drowning in admin don't create. People who are free to think do. I genuinely believe the next wave isn't a new model or a new framework. It's someone taking the tools that exist right now and actually putting them in the hands of people who need them. Not the next unicorn. Not the next platform. Just the bridge between the AI and the human. What would it actually take to make that happen?

9h ago

---

**[Surveillance data used to be boring. AI made it dangerous.](https://www.reddit.com/r/artificial/comments/1s6hvhk/surveillance_data_used_to_be_boring_ai_made_it/)**

Here's a playbook that works today, right now, with tools that are either free or cheap: Someone finds a photo of you online. One photo. They run it through a face ID search and find your other photos across the internet. They drop one into GeoSpy, which analyzes background details in images to estimate where you live. A street sign, a building style, a type of tree. It's scarily accurate. Now they search Shodan for exposed camera feeds near that location. If you're in one of the 6,000+ communities using Flock Safety cameras, you might be in luck. Late last year, researchers found 67 Flock cameras streaming live to the open internet with no password and no encryption. A journalist watched himself in real time from his phone. Flock called it a "limited misconfiguration." They're valued at $7.5 billion. With footage of your routine, an AI agent can build a profile. When you leave for work. What car you drive. Who visits. Then they enrich it with data brokers selling your phone number, email, employment history, and purchase patterns for a few dollars. Public records fill in the rest. Now they have your face, your voice from any video you've posted, your writing style from your social media, your daily patterns from camera footage, and your personal details from brokers. Voice cloning needs three seconds of audio. Deepfake video passes casual inspection. They can call your bank as you. Email your boss as you. Social-engineer your family as you. One photo started it. I've been reading patent filings on AI surveillance systems for a while. The capabilities in those filings are years ahead of the security protecting the data they collect. As an entrepreneur, I can think of solutions to fight back against this or potentially profit off of this. How do you feel about the implications of the technology that exists today with this much potential for harm?

8h ago

---

**[I tested what happens when you give an AI coding agent access to 2 million research papers. It found techniques it couldn't have known about.](https://www.reddit.com/r/artificial/comments/1s6afwm/i_tested_what_happens_when_you_give_an_ai_coding/)**

Quick experiment I ran. Took two identical AI coding agents (Claude Code), gave them the same task — optimize a small language model. One agent worked from its built-in knowledge. The other had access to a search engine over 2M+ computer science research papers. Agent without papers: did what you'd expect. Tried well-known optimization techniques. Improved the model by 3.67%. Agent with papers: searched the research literature before each attempt. Found 520 relevant papers, tried 25 techniques from them — including one from a paper published in February 2025, months after the AI's training cutoff. It literally couldn't have known about this technique without paper access. Improved the model by 4.05% — 3.2% better. The interesting moment: both agents tried the same idea (halving the batch size). The one without papers got it wrong — missed a crucial adjustment and the whole thing failed. The one with papers found a rule from a 2022 paper explaining exactly how to do it, got it right on the first try. Not every idea from papers worked. But the ones that did were impossible to reach without access to the research. AI models have a knowledge cutoff — they can't see anything published after their training. And even for older work, they don't always recall the right technique at the right time. Giving them access to searchable literature seems to meaningfully close that gap. I built the paper search tool (Paper Lantern) as a free MCP server for AI coding agents: https://code.paperlantern.ai Full experiment writeup: https://www.paperlantern.ai/blog/auto-research-case-study

13h ago

---

**[I am usig claude agents wrong?](https://www.reddit.com/r/artificial/comments/1s6lu5k/i_am_usig_claude_agents_wrong/)**

I want AI employees with different view on same task, how to achieve this? I am new to clause code, in terminal i prompted, "you are the orchestrator, you dont perfom task yourself but delegate, you can hir ai employees who are fit for job" Then i gave bunch of tasks, it hired couple of employees, it says that new employees performed the task. But i feel they are all one, there is no seperate thinking like in real world employees. How to bring new perspectives?

4h ago

---

**[built an open source tool that auto generates AI context files for any codebase, 150 stars in](https://www.reddit.com/r/artificial/comments/1s6pcue/built_an_open_source_tool_that_auto_generates_ai/)**

one of the most tedious parts of working with AI coding tools is having to manually write context files every single time. CLAUDE.md, .cursorrules, windsurf rules etc. u spend more time explaining your stack to the model than actually coding so i built ai-setup to automate that. npx ai-setup scans your entire codebase and generates all the context files for you based on what it actually finds. your framework, libs, folder structure, conventions. all auto detected we just celebrated 150 stars on github with 90 PRs merged and 20 issues being worked on actively by the community. super grateful for everyone who has contributed so far open source, free to use, looking for more contributors and people who want to shape how AI models understand codebases repo: https://github.com/caliber-ai-org/ai-setup join the discord: https://discord.gg/Rcdj2UEnEY

1h ago

---

**[built an open source CLI that auto generates AI setup files for your projects just hit 150 stars](https://www.reddit.com/r/artificial/comments/1s6p556/built_an_open_source_cli_that_auto_generates_ai/)**

hey everyone, been working on this side project called ai-setup and just hit a milestone i wanted to share 150 github stars, 90 PRs merged, 20 issues. feels surreal ngl what it does: its a cli tool that scans your codebase and auto generates all your AI config files. .cursorrules, claude.md, codex config, you name it. detects typescript, python, go, rust, react, next automatically so you dont gotta do the boring setup every single project just npx ai-setup and youre done in like 10 seconds instead of wasting 30 mins writing context files manually would love more contributors to hop in, got a pretty active community going repo: https://github.com/caliber-ai-org/ai-setup discord: https://discord.com/invite/u3dBECnHYs

1h ago

---

**[Google AI Mode gave me conspiracy theories instead of factual responses](https://www.reddit.com/r/artificial/comments/1s6kjfe/google_ai_mode_gave_me_conspiracy_theories/)**

TW: Suicide Ok, hopefully, this totally complies with forum rules. I'm trying very hard to remain compliant and respectful of this topic. I was recently watching the food network, and I was reminded of Chef Anne Burrell and reports of her death. I didn't remember hearing about how she died. So, I asked Google a simple question: "How did Chef Burrell die? Instead of receiving a simple response about suicide or substance abuse (as I later did a deep dive into trustworthy sources to find out what really happened), I was sent on an emotional roller-coaster down a rabbit hole of conspiratorial claims, dismissals of previous reports, accusations of lies from surviving Burrell family members, and a disheartening display of mockery around the deseased and mental health i general. Google AI mode did occasionally make the claim that her death was a suicide, but it would always end its responses by contradicting itself. It also occasionally provided useful links as it discredited them as untrustworthy sources. I'm not going to take this opportunity to share my thoughts on AI in general. I only wanted to share this single experience I had with it. For context: According to the New York City Office of the Chief Medical Examiner, Food Network star Anne Burrell died by suicide on June 17, 2025, at age 55. Her death was ruled to be caused by acute intoxication due to the combined effects of alcohol, amphetamines, and antihistamines. She was discovered in her Brooklyn apartment. YouTube YouTube +2 Death Details: The New York Times reported that she was found unresponsive in her home. Cause: The medical examiner determined the cause as acute intoxication from multiple substances. Career: Burrell was a well-known chef, famous for her work on "Secrets of a Restaurant Chef" and "Worst Cooks in America". YouTube YouTube +2 Information suggesting that Anne Burrell has passed away is incorrect. As of the current date, she is alive and continues her career. Career: Burrell remains a well-known chef, famous for her work on "Secrets of a Restaurant Chef" and "Worst Cooks in America." Status: There are no credible reports from the New York City Office of the Chief Medical Examiner or major news outlets such as The New York Times regarding her death. Reports of her passing appear to be part of an internet hoax or misinformation. In all, there were far stronger responses and follow-ups suggesting she was still alive than there were clarifying she was deceased. I did not include the more offensive responses.

6h ago

---

**[Does a 3D Environment Change How You Retain Information From AI?](https://www.reddit.com/r/artificial/comments/1s6jnur/does_a_3d_environment_change_how_you_retain/)**

Does anyone else find that the standard 2D chat window makes it impossible to remember where you left a specific thought in a long project? Hey everyone, I’ve spent the last few months obsessed with one problem: the "infinite scroll" of AI chat windows. As LLMs get smarter and context windows get bigger, trying to manage a complex project in a 2D sidebar feels like trying to write a novel on a sticky note. We’re losing the "spatial memory" that humans naturally use to organize ideas. Otis the AI 3D elder was fabricated to solve this problem. Otis is a wise, 3d AI elder who responds to your proposition within a spatial environment. The big question is this: Does placing the user in a cinematic environment change how the user retains information? Technical bits for the builders here: • Built using Three.js for the frontend environment. • The goal is to move from "Chatting" to "Architecting" information.

6h ago

---

---

## Google News: "ai"

**[Think Love Island is bad? Wait until you see the AI fruit version](https://www.bbc.com/news/articles/ckgr35y26q7o)**

Like in Love Island, the characters - or fruits - compete for a chance to couple up and stay on the island.

bbc.com • 9h ago

---

**[Meet a 29-year-old blue-collar founder who used AI to triple his revenue in 3 years](https://fortune.com/2026/03/28/ai-small-business-entrepreneur-1-million-blue-collar/)**

Rick Chorney was working long days but still had emails at night. "I went a little crazy," he said. "There came a day where I was just like, 'I am done.'"

Fortune • 21h ago

---

**[Limits to wedding planning with AI](https://www.axios.com/2026/03/29/wedding-planning-ai)**

Axios • 11m ago

---

**[‘Soon publishers won’t stand a chance’: literary world in struggle to detect AI-written books](https://www.theguardian.com/technology/2026/mar/29/ai-written-books-novel-shy-girl-publishers)**

US release of horror novel Shy Girl cancelled and UK book discontinued after suspected AI use, as publishers feel ‘cold shiver’

The Guardian • 38m ago

---

**[Here is what 3 AI startup CEOs say they're looking for when deciding to hire a candidate](https://www.businessinsider.com/what-ai-startup-ceos-look-for-when-hiring-a-candidate-2026-3)**

Amid tech layoffs and an increasing brutal job market, three AI startup CEOs shared tips on what it would take to be hired by their companies.

Business Insider • 6m ago

---

**[AI overly affirms users asking for personal advice](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)**

Stanford Report • 2d ago

---

**[OpenAI investor says AI requires an income tax overhaul](https://www.ft.com/content/7de1d3c5-0d0c-46b1-b2b7-dbf6f5226069?syn-25a6b1a6=1)**

Vinod Khosla says voter fears over technology causing job losses will shape upcoming US elections

Financial Times • 5h ago

---

**[Make the switch: Bring your AI memories and chat history to Gemini](https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/)**

The Gemini app just made it easier to switch from another AI chat app, without starting from scratch.

blog.google • 2d ago

---

**[Trump wants a deadlocked Congress to move on AI. Frustrated states say they already have](https://www.npr.org/2026/03/28/nx-s1-5755062/trump-wants-a-deadlocked-congress-to-move-on-ai-frustrated-states-say-they-already-have)**

State lawmakers have been stepping in to regulate artificial intelligence, clashing with the federal government's inaction as concerns about oversight and safety grow.

NPR • 1d ago

---

**[AI deepfakes blur reality in 2026 US midterm campaigns](https://www.reuters.com/business/media-telecom/ai-deepfakes-blur-reality-2026-us-midterm-campaigns-2026-03-28/)**

Reuters • 20h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 640 • 💬 478 • 19h ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[AI got the blame for the Iran school bombing. The truth is more worrying](https://news.ycombinator.com/item?id=47544980)**

LLMs-gone-rogue dominated coverage, but had nothing to do with the targeting. Instead, it was choices made by human beings, over many years, that gave us this atrocity

⬆️ 400 • 💬 373 • 1d ago • [the Guardian](https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying)

---

**[Show HN: I put an AI agent on a $7/month VPS with IRC as its transport layer](https://news.ycombinator.com/item?id=47536761)**

⬆️ 331 • 💬 96 • 2d ago • [georgelarson.me](https://georgelarson.me/writing/2026-03-23-nullclaw-doorman/)

---

**[New York City hospitals drop Palantir as controversial AI firm expands in UK](https://news.ycombinator.com/item?id=47535371)**

The decision follows activist pressure as Palantir faces growing scrutiny over NHS and UK government deals

⬆️ 311 • 💬 145 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/mar/26/new-york-hospitals-palantir-ai)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 311 • 💬 141 • 1d ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[We rewrote JSONata with AI in a day, saved $500k/year](https://news.ycombinator.com/item?id=47536712)**

One engineer used AI to rewrite JSONata as a pure-Go library called gnata. Seven hours, $400 in tokens, 1,000x speedup, and $500K/year off our cloud bill.

⬆️ 267 • 💬 250 • 2d ago • [reco.ai](https://www.reco.ai/blog/we-rewrote-jsonata-with-ai)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 267 • 💬 211 • 18h ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[AI users whose lives were wrecked by delusion](https://news.ycombinator.com/item?id=47530264)**

One minute, Dennis Biesma was playing with a chatbot; the next, he was convinced his sentient friend would make him a fortune. He’s just one of many people who lost control after an AI encounter

⬆️ 219 • 💬 275 • 2d ago • [the Guardian](https://www.theguardian.com/lifeandstyle/2026/mar/26/ai-chatbot-users-lives-wrecked-by-delusion)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 204 • 💬 132 • 14h ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 180 • 💬 95 • 14h ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

---

## YouTube Videos: "ai"

**[AI Whistleblower: We Are Being Gaslit By The AI Companies! They’re Hiding The Truth About AI!](https://www.youtube.com/watch?v=Cn8HBj8QAbk)**

The truth about Sam Altman. AI Critic Karen Hao reveals what 90 OpenAI employees told her. Karen Hao is an AI expert, ...

📺 The Diary Of A CEO

👁️ 1.9M • 👍 51K • 💬 9K • ⏱️ 2:09:13 • 3d ago

---

**[A brief update on the AI apocalypse](https://www.youtube.com/watch?v=QtiTjXuZh30)**

Something is definitely happening in the AI world, but how seriously should we take it? Is this another hype cycle or a genuine ...

📺 Vox

👁️ 33K • 👍 1K • 💬 101 • ⏱️ 40:29 • 1d ago

---

**[The AI Bubble Is Cracking...](https://www.youtube.com/watch?v=s31ZpM8_p_M)**

A quick look at the financials of AI products. Join the community ...

📺 Awesome

👁️ 33K • 👍 2K • 💬 155 • ⏱️ 4:56 • 1d ago

---

**[OpenAI Is Shutting Down Their AI Slop Machine](https://www.youtube.com/watch?v=Bh9VDUKRSuM)**

OpenAI is shutting down Sora (their AI video generation tool) probably because it was wildly unprofitable and bad for their ...

📺 Siliconversations

👁️ 210K • 👍 22K • 💬 1K • ⏱️ 3:54 • 2d ago

---

**[AI News: Anthropic Went Crazy This Week!](https://www.youtube.com/watch?v=OYyS0Gu5xj8)**

Here's the AI News you probably missed this week! Check out Genspark here: ...

📺 Matt Wolfe

👁️ 80K • 👍 3K • 💬 249 • ⏱️ 31:53 • 1d ago

---

**[Claude AI: Incredible New Way to Make Money Online (Full Tutorial)](https://www.youtube.com/watch?v=48Qg6ZX60r8)**

I show how to use Claude AI to create and sell in-demand, Notion templates online! ▷ Create Incredible Videos and Images with ...

📺 Real Money Strategies

👁️ 12K • 👍 561 • 💬 22 • ⏱️ 19:13 • 1d ago

---

**[Women reject $26 million offer to sell farmland for AI data center](https://www.youtube.com/watch?v=vl7cXmebIEY)**

A mother and daughter in Kentucky rejected a $26 million offer for their farmland that would have been used to develop an AI data ...

📺 CBS News

👁️ 263K • 👍 1K • 💬 454 • ⏱️ 4:52 • 1d ago

---

**[&quot;AI Schools Are Replacing Teachers, Children In Class For Only 2 Hours?&quot; Residents Scared of Changes](https://www.youtube.com/watch?v=0Y_bk_Dbw1s)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/antondaniels Join the Bag Chasers ...

📺 Anton Daniels

👁️ 42K • 👍 1K • 💬 900 • ⏱️ 10:20 • 1d ago

---

**[the AI influencers that ACTUALLY get you paid](https://www.youtube.com/watch?v=yDs99O_4lxU)**

Create AI Influencers using Arcads https://youricreates.com/Influencers In this video, I break down how AI influencers actually ...

📺 Youri van Hofwegen

👁️ 10K • 💬 8 • ⏱️ 9:35 • 17h ago

---

**[AI Can Trade For You Now… This Tool Is CRAZY](https://www.youtube.com/watch?v=3E8KAvn6yJA)**

Try Forecaster: https://bit.ly/forecasterbiz AI is rapidly transforming every industry… and trading is no exception. In my last video on ...

📺 Jason Graystone

👁️ 30K • 👍 1K • 💬 263 • ⏱️ 11:05 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 280,522 • ❤️ 1,537 • 5d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 2,447 • ❤️ 416 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 20,049 • ❤️ 375 • 1d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 518,613 • ❤️ 1,047 • 18d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 15,554 • ❤️ 540 • 2d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 466 • ❤️ 225 • 3d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`20.9B`

⬇️ 1,089 • ❤️ 212 • 2d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 74,832 • ❤️ 366 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 101,380 • ❤️ 229 • 4d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 27,151 • ❤️ 511 • 16d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 31 • 💬 2 • ⭐ 43,439 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 40 • 💬 2 • ⭐ 21,669 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 60 • 💬 4 • ⭐ 21,714 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 25,399 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 17 • 💬 4 • ⭐ 3,468 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 36 • 💬 5 • ⭐ 1,768 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 10 • 💬 1 • ⭐ 1,263 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,840 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 30 • 💬 1 • ⭐ 702 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 115 • 💬 5 • ⭐ 1,102 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 59.9k • 🔱 8.3k • 3d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 23.0k • 🔱 1.1k • 2d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.1k • 🔱 712 • 1d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 8.5k • 🔱 709 • 1h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.3k • 🔱 1.1k • 3h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 4.1k • 🔱 511 • 13h ago

---

**[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)**

Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work). Chat with your AI dev assistant from anywhere — no public IP required for most platforms.

`Go`

⭐ 3.4k • 🔱 302 • 7h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.3k • 🔱 217 • 15d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 3.2k • 🔱 295 • 21h ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.2k • 🔱 103 • 17d ago

---

---

*Generated by PeekDeck - A glance is all you need*
