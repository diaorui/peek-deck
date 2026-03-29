---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-29T02:33:29.650315+00:00'
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

**Last Updated:** March 29, 2026 at 02:33 UTC  
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

**[Claude is the least bullshit-y AI](https://www.reddit.com/r/artificial/comments/1s67buc/claude_is_the_least_bullshity_ai/)**

Just found this “bullshit benchmark,” and sort of shocked by the divergence of Anthropic’s models from other major models (ChatGPT and Gemini). IMO this alone is reason to use Claude over others.

🔗 [GitHub](https://github.com/petergpt/bullshit-benchmark?tab=readme-ov-file#3-detection-rate-over-time) • 8h ago

---

**[The AI hype misses the people who actually need it most](https://www.reddit.com/r/artificial/comments/1s6fws6/the_ai_hype_misses_the_people_who_actually_need/)**

Every day someone posts "AI will change everything" and it's always about agents scaling businesses, automating workflows, 10x productivity, whatever. Cool. But change everything for who? Go talk to the barber who loses 3 clients a week to no-shows and can't afford a booking system that actually works. Go talk to the solo attorney who's drowning in intake paperwork and can't afford a paralegal. Go talk to the tattoo artist who's on the phone all day instead of tattooing. Go talk to the author who wrote a book and has zero idea how to market it. These people don't need another app. They don't need to "learn to code." They don't need to understand what an LLM is. They need the tools that already exist and wired into their actual business. Their actual pain. The gap between "AI can do amazing things" and "I can actually use AI to make my life better" is where most of the world lives right now. And most of the AI community is completely disconnected from that reality. We're on Reddit at midnight debating MCP vs direct API and arguing about whether Opus or Sonnet is better for agent routing. That's not most people. Most people are just trying to survive running a business they started because they're good at something and not because they wanted to become a full-time administrator. If every small business owner, every freelancer, every solo professional had agents handling the repetitive stuff ya kno...the follow-ups, the scheduling, the content, the bookkeeping; you wouldn't just get productivity. You'd get a renaissance. Because people who are drowning in admin don't create. People who are free to think do. I genuinely believe the next wave isn't a new model or a new framework. It's someone taking the tools that exist right now and actually putting them in the hands of people who need them. Not the next unicorn. Not the next platform. Just the bridge between the AI and the human. What would it actually take to make that happen?

2h ago

---

**[I tested what happens when you give an AI coding agent access to 2 million research papers. It found techniques it couldn't have known about.](https://www.reddit.com/r/artificial/comments/1s6afwm/i_tested_what_happens_when_you_give_an_ai_coding/)**

Quick experiment I ran. Took two identical AI coding agents (Claude Code), gave them the same task — optimize a small language model. One agent worked from its built-in knowledge. The other had access to a search engine over 2M+ computer science research papers. Agent without papers: did what you'd expect. Tried well-known optimization techniques. Improved the model by 3.67%. Agent with papers: searched the research literature before each attempt. Found 520 relevant papers, tried 25 techniques from them — including one from a paper published in February 2025, months after the AI's training cutoff. It literally couldn't have known about this technique without paper access. Improved the model by 4.05% — 3.2% better. The interesting moment: both agents tried the same idea (halving the batch size). The one without papers got it wrong — missed a crucial adjustment and the whole thing failed. The one with papers found a rule from a 2022 paper explaining exactly how to do it, got it right on the first try. Not every idea from papers worked. But the ones that did were impossible to reach without access to the research. AI models have a knowledge cutoff — they can't see anything published after their training. And even for older work, they don't always recall the right technique at the right time. Giving them access to searchable literature seems to meaningfully close that gap. I built the paper search tool (Paper Lantern) as a free MCP server for AI coding agents: https://code.paperlantern.ai Full experiment writeup: https://www.paperlantern.ai/blog/auto-research-case-study

6h ago

---

**[Surveillance data used to be boring. AI made it dangerous.](https://www.reddit.com/r/artificial/comments/1s6hvhk/surveillance_data_used_to_be_boring_ai_made_it/)**

Here's a playbook that works today, right now, with tools that are either free or cheap: Someone finds a photo of you online. One photo. They run it through a face ID search and find your other photos across the internet. They drop one into GeoSpy, which analyzes background details in images to estimate where you live. A street sign, a building style, a type of tree. It's scarily accurate. Now they search Shodan for exposed camera feeds near that location. If you're in one of the 6,000+ communities using Flock Safety cameras, you might be in luck. Late last year, researchers found 67 Flock cameras streaming live to the open internet with no password and no encryption. A journalist watched himself in real time from his phone. Flock called it a "limited misconfiguration." They're valued at $7.5 billion. With footage of your routine, an AI agent can build a profile. When you leave for work. What car you drive. Who visits. Then they enrich it with data brokers selling your phone number, email, employment history, and purchase patterns for a few dollars. Public records fill in the rest. Now they have your face, your voice from any video you've posted, your writing style from your social media, your daily patterns from camera footage, and your personal details from brokers. Voice cloning needs three seconds of audio. Deepfake video passes casual inspection. They can call your bank as you. Email your boss as you. Social-engineer your family as you. One photo started it. I've been reading patent filings on AI surveillance systems for a while. The capabilities in those filings are years ahead of the security protecting the data they collect. As an entrepreneur, I can think of solutions to fight back against this or potentially profit off of this. How do you feel about the implications of the technology that exists today with this much potential for harm?

1h ago

---

**[I cut Claude Code's token usage by 68.5% by giving agents their own OS](https://www.reddit.com/r/artificial/comments/1s66kt0/i_cut_claude_codes_token_usage_by_685_by_giving/)**

Al agents are running on infrastructure built for humans. Every state check runs 9 shell commands. Every cold start re-discovers context from scratch. It's wasteful by design. An agentic JSON-native OS fixes it. Benchmarks across 5 real scenarios: Semantic search vs grep + cat: 91% fewer tokens Agent pickup vs cold log parsing: 83% fewer tokens State polling vs shell commands: 57% fewer tokens Overall: 68.5% reduction Benchmark is fully reproducible: python3 tools/ bench_compare.py Plugs into Claude Code via MCP, runs local inference through Ollama, MIT licensed. Would love feedback from people actually running agentic workflows. https://github.com/ninjahawk/hollow-agentOS

9h ago

---

**[Say No to Congress using AI to mass surveil US Citizens and oppose the extension of the FISA Act](https://www.reddit.com/r/artificial/comments/1s5onmr/say_no_to_congress_using_ai_to_mass_surveil_us/)**

In April Congress is voting to extend the FISA Act on the 20th of April this year. The FISA Act allows the government to buy your emails, texts, and calls from corporations. With the newly established shady deal with Open AI surveillance has become even more accessible and applicable on a much more larger and invasive scale. It very important for the sake of maintaining our right of protest and the press in the future. Call/email your representatives in the US, protest, and speak in any way you can.

23h ago

---

**[👋Welcome to r/AiVIS - Let's build this right](https://www.reddit.com/r/artificial/comments/1s6i9in/welcome_to_raivis_lets_build_this_right/)**

Hey everyone! I’m u/Renomase, a founding moderator of r/AiVIS. This is the new spot for people watching how AI search is changing visibility in real time. We’re here for AI visibility, audits, citations, schema, structured content, trust signals, and why some sites get picked up while others stay buried. Good to have you here. What to Post: Drop anything useful, real, or worth unpacking. Audit results, questions, examples, experiments, wins, losses, weird search behavior, schema setups, citation problems, content structure ideas, or cases where a site looked good on the surface but still got overlooked by AI. Community Vibe: Keep it solid. Respectful, constructive, no fluff. This should be a place where builders, marketers, founders, and operators can compare notes and get sharper on what actually helps a site get understood and surfaced. How to Get Started: Introduce yourself below. Share what you’re building or testing. Ask a question or post a finding today. Invite somebody who’s tapped into SEO, AI search, or content visibility. Want to help mod and build this right from the ground floor? Reach out. Thanks for being part of the first run. Let’s make r/AiVIS a real signal spot, not just another dead page.

53m ago

---

**[AMD introduces GAIA agent UI for privacy-first web app for local AI agents](https://www.reddit.com/r/artificial/comments/1s67ajg/amd_introduces_gaia_agent_ui_for_privacyfirst_web/)**

AMD's GAIA AI agent framework (that previously stood for 'Generative AI Is Awesome' albeit they seemed to have dropped promoting it as that name) for Ryzen AI hardware is out with a new version

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-GAIA-0.17-Agent-UI) • 8h ago

---

**[👋Welcome to r/AiVIS - Let's build this right](https://www.reddit.com/r/artificial/comments/1s6e8r1/welcome_to_raivis_lets_build_this_right/)**

Hey everyone! I’m u/Renomase, a founding moderator of r/AiVIS. This is the new spot for people watching how AI search is changing visibility in real time. We’re here for AI visibility, audits, citations, schema, structured content, trust signals, and why some sites get picked up while others stay buried. Good to have you here. What to Post: Drop anything useful, real, or worth unpacking. Audit results, questions, examples, experiments, wins, losses, weird search behavior, schema setups, citation problems, content structure ideas, or cases where a site looked good on the surface but still got overlooked by AI. Community Vibe: Keep it solid. Respectful, constructive, no fluff. This should be a place where builders, marketers, founders, and operators can compare notes and get sharper on what actually helps a site get understood and surfaced. How to Get Started: Introduce yourself below. Share what you’re building or testing. Ask a question or post a finding today. Invite somebody who’s tapped into SEO, AI search, or content visibility. Want to help mod and build this right from the ground floor? Reach out. Thanks for being part of the first run. Let’s make r/AiVIS a real signal spot, not just another dead page.

3h ago

---

**[HALO - Hierarchical Autonomous Learning Organism](https://www.reddit.com/r/artificial/comments/1s63mtm/halo_hierarchical_autonomous_learning_organism/)**

The idea is called HALO - Hierarchical Autonomous Learning Organism. The core premise is simple: what if instead of just making LLMs bigger, we actually looked at how intelligence works in nature and built something that mirrors those principles? Not just the human brain either, evolution spent hundreds of millions of years solving different cognitive problems in different species. Why not take the best bits from all of them? Some of what ended up in the design: It has a nervous system. Not metaphorically, it’s literally wired to monitor its own hardware. GPU temps, memory pressure, all of it. When it’s running hot it conserves and gets cautious. When it’s idle and cool it explores and consolidates. Biological stress response, but for silicon. It learns the way animals learn. One strong negative experience permanently changes how it perceives that category of situation, like a kid touching a hot stove. Not just “add a rule” but actually changing the lens it sees similar situations through. Compare that to how current AI just… forgets everything between sessions. It has eight processing arms inspired by octopus neurology. Two thirds of an octopus’s neurons are in its arms, not its brain. Each arm is semi autonomous. Applied here that means memory retrieval, fact checking, simulation, tool staging, all running in parallel before the main model even needs them. No central bottleneck. It knows what it doesn’t know. There are three knowledge databases, what it’s verified, what it’s uncertain about, and a registry of confirmed gaps. That last one is the interesting one. It knows the shape of its own ignorance. That’s what drives the curiosity engine. That’s what makes it actually want to learn rather than just respond. It develops a personality over time. Starts with one seed temperament, curiosity, and everything else emerges from experience. There’s a developmental threshold, and once it crosses it, the system looks at what it’s actually become and that becomes its baseline. Not programmed personality. Accumulated identity. It can choose to ignore guidance and learn from the consequences. Bounded, transparent autonomy. It knows when advice is good and can still try something different. The outcome, good or bad, is the learning signal. That’s how real judgment develops. And everything is declared openly, nothing hidden. The whole thing is designed to run locally, on a gaming PC, with no cloud dependency. Private. Continuous. Gets smarter through use, not retraining. I put together a technical white paper with the complete architecture if anyone wants to go deep. 34+ subsystems, full brain region mapping, animal cognition mapping, causal reasoning engine, six-level memory tree, the works. I genuinely think the pieces are all there. Would love to get some feedback on the idea. The idea is fully open for use, so if anything from the architecture may benefit your project, you’re free to use it.

10h ago

---

---

## Google News: "ai"

**[Meet a 29-year-old blue-collar founder who used AI to triple his revenue in 3 years](https://fortune.com/2026/03/28/ai-small-business-entrepreneur-1-million-blue-collar/)**

Rick Chorney was working long days but still had emails at night. "I went a little crazy," he said. "There came a day where I was just like, 'I am done.'"

Fortune • 14h ago

---

**[Trump wants a deadlocked Congress to move on AI. Frustrated states say they already have](https://www.npr.org/2026/03/28/nx-s1-5755062/trump-wants-a-deadlocked-congress-to-move-on-ai-frustrated-states-say-they-already-have)**

State lawmakers have been stepping in to regulate artificial intelligence, clashing with the federal government's inaction as concerns about oversight and safety grow.

NPR • 17h ago

---

**[AI overly affirms users asking for personal advice](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)**

Stanford Report • 2d ago

---

**[‘Our assumptions are broken’: how fraudulent church data revealed AI’s threat to polling](https://www.theguardian.com/technology/2026/mar/28/how-fraudulent-church-data-revealed-ais-threat-to-polling)**

Experts say paid participants are using automated tools to generate unreliable survey responses at scale

The Guardian • 14h ago

---

**[Welcome to a Multidimensional Economic Disaster](https://www.theatlantic.com/technology/2026/03/ai-boom-polycrisis/686559/)**

The AI boom wasn’t built for the polycrisis.

The Atlantic • 2d ago

---

**[AI deepfakes blur reality in 2026 US midterm campaigns](https://www.reuters.com/business/media-telecom/ai-deepfakes-blur-reality-2026-us-midterm-campaigns-2026-03-28/)**

Reuters • 13h ago

---

**[Think Love Island is bad? Wait until you see the AI fruit version](https://www.bbc.com/news/articles/ckgr35y26q7o)**

Like in Love Island, the characters - or fruits - compete for a chance to couple up and stay on the island.

BBC • 2h ago

---

**[Make the switch: Bring your AI memories and chat history to Gemini](https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/)**

The Gemini app just made it easier to switch from another AI chat app, without starting from scratch.

blog.google • 2d ago

---

**[When AI turns software development inside-out: 170% throughput at 80% headcount](https://venturebeat.com/orchestration/when-ai-turns-software-development-inside-out-170-throughput-at-80-headcount)**

VentureBeat • 8h ago

---

**[What ‘The AI Doc’ Filmmakers Want Everyone to Know About AI: ‘There Probably Isn’t an Off Switch’](https://variety.com/2026/film/features/the-ai-doc-filmmakers-need-to-know-about-ai-1236701867/)**

The filmmakers behind 'The AI Doc: Or How I Became an Apocaloptimist' share what they learned from making the film and think everyone should know.

Variety • 9h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 533 • 💬 412 • 12h ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[AI got the blame for the Iran school bombing. The truth is more worrying](https://news.ycombinator.com/item?id=47544980)**

LLMs-gone-rogue dominated coverage, but had nothing to do with the targeting. Instead, it was choices made by human beings, over many years, that gave us this atrocity

⬆️ 398 • 💬 369 • 1d ago • [the Guardian](https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying)

---

**[Show HN: I put an AI agent on a $7/month VPS with IRC as its transport layer](https://news.ycombinator.com/item?id=47536761)**

⬆️ 331 • 💬 95 • 2d ago • [georgelarson.me](https://georgelarson.me/writing/2026-03-23-nullclaw-doorman/)

---

**[New York City hospitals drop Palantir as controversial AI firm expands in UK](https://news.ycombinator.com/item?id=47535371)**

The decision follows activist pressure as Palantir faces growing scrutiny over NHS and UK government deals

⬆️ 311 • 💬 144 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/mar/26/new-york-hospitals-palantir-ai)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 302 • 💬 132 • 18h ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[We rewrote JSONata with AI in a day, saved $500k/year](https://news.ycombinator.com/item?id=47536712)**

One engineer used AI to rewrite JSONata as a pure-Go library called gnata. Seven hours, $400 in tokens, 1,000x speedup, and $500K/year off our cloud bill.

⬆️ 267 • 💬 249 • 2d ago • [reco.ai](https://www.reco.ai/blog/we-rewrote-jsonata-with-ai)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 262 • 💬 206 • 11h ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[AI users whose lives were wrecked by delusion](https://news.ycombinator.com/item?id=47530264)**

One minute, Dennis Biesma was playing with a chatbot; the next, he was convinced his sentient friend would make him a fortune. He’s just one of many people who lost control after an AI encounter

⬆️ 219 • 💬 275 • 2d ago • [the Guardian](https://www.theguardian.com/lifeandstyle/2026/mar/26/ai-chatbot-users-lives-wrecked-by-delusion)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 153 • 💬 106 • 7h ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 125 • 💬 57 • 7h ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

---

## YouTube Videos: "ai"

**[&quot;AI Schools Are Replacing Teachers, Children In Class For Only 2 Hours?&quot; Residents Scared of Changes](https://www.youtube.com/watch?v=0Y_bk_Dbw1s)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/antondaniels Join the Bag Chasers ...

📺 Anton Daniels

👁️ 39K • 👍 1K • 💬 882 • ⏱️ 10:20 • 19h ago

---

**[Gary Vee: The AI Opportunity Is Real — You&#39;re Just Looking at It Wrong](https://www.youtube.com/watch?v=4vIIeCqHYXA)**

Build your own AI agent team and automate your daily ops with Accio Work — use my exclusive invite code SILVLG to skip the ...

📺 Silicon Valley Girl

👁️ 18K • 👍 685 • 💬 64 • ⏱️ 44:41 • 1d ago

---

**[AI Whistleblower: We Are Being Gaslit By The AI Companies! They’re Hiding The Truth About AI!](https://www.youtube.com/watch?v=Cn8HBj8QAbk)**

The truth about Sam Altman. AI Critic Karen Hao reveals what 90 OpenAI employees told her. Karen Hao is an AI expert, ...

📺 The Diary Of A CEO

👁️ 1.8M • 👍 50K • 💬 9K • ⏱️ 2:09:13 • 2d ago

---

**[Higgsfield AI Cinema Studio 2.5 SOLVED Consistent AI Characters!](https://www.youtube.com/watch?v=Q-vLiGjZTFA)**

Higgsfield AI Cinema Studio 2.5 SOLVED Consistent AI Characters! Try Cinema Studio now ...

📺 Mira AI

👁️ 6K • 💬 6 • ⏱️ 8:32 • 9h ago

---

**[How AI Made This Island Rich Overnight](https://www.youtube.com/watch?v=MiJJwCP4GZI)**

How AI Made This Island Rich Overnight keywords & hashtags: Anguilla AI domain story, .ai domain meaning, how Anguilla got ...

📺 Kalam Ghaseet

👁️ 2K • 💬 10 • ⏱️ 0:58 • 1d ago

---

**[The ONLY way To Create Realistic AI Avatars that look &amp; Sound like You](https://www.youtube.com/watch?v=s2HM4W1QCTw)**

Learn How To Make a Realistic AI Clone Avatar that sounds like you Try Higgsfield AI ...

📺 Dan Kieft

👁️ 29K • 💬 17 • ⏱️ 19:51 • 1d ago

---

**[the AI influencers that ACTUALLY get you paid](https://www.youtube.com/watch?v=yDs99O_4lxU)**

Create AI Influencers using Arcads https://youricreates.com/Influencers In this video, I break down how AI influencers actually ...

📺 Youri van Hofwegen

👁️ 9K • 💬 8 • ⏱️ 9:35 • 10h ago

---

**[A brief update on the AI apocalypse](https://www.youtube.com/watch?v=QtiTjXuZh30)**

Something is definitely happening in the AI world, but how seriously should we take it? Is this another hype cycle or a genuine ...

📺 Vox

👁️ 30K • 👍 968 • 💬 95 • ⏱️ 40:29 • 1d ago

---

**[Why Replacing Humans with AI is Backfiring](https://www.youtube.com/watch?v=bNJad6HE23c)**

jobmarket #ai #tech In this video, we explore why the AI gold rush is hitting a wall. Companies that rushed to automate are now ...

📺 Mackard

👁️ 54K • 👍 2K • 💬 164 • ⏱️ 8:01 • 1d ago

---

**[AI News: Anthropic Went Crazy This Week!](https://www.youtube.com/watch?v=OYyS0Gu5xj8)**

Here's the AI News you probably missed this week! Check out Genspark here: ...

📺 Matt Wolfe

👁️ 76K • 👍 3K • 💬 253 • ⏱️ 31:53 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 253,259 • ❤️ 1,526 • 5d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 1,802 • ❤️ 408 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 12,080 • ❤️ 361 • 1d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 478,934 • ❤️ 1,039 • 18d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 14,786 • ❤️ 519 • 2d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 418 • ❤️ 222 • 3d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 69,594 • ❤️ 366 • 4d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`20.9B`

⬇️ 451 • ❤️ 208 • 2d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 85,140 • ❤️ 218 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Claude 4.6 Opus Chain-of-Thought distillation. It excels at structured, step-by-step problem-solving within `<think>` tags, making it ideal for coding agents and complex task execution with improved autonomy and stability.

`image-text-to-text` `26.9B`

⬇️ 590,877 • ❤️ 467 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 30 • 💬 2 • ⭐ 43,223 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 21,488 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 59 • 💬 4 • ⭐ 21,522 • 7mo ago

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

▲ 16 • 💬 4 • ⭐ 3,468 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 35 • 💬 5 • ⭐ 1,768 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,823 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 30 • 💬 1 • ⭐ 690 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 9 • 💬 1 • ⭐ 1,263 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 115 • 💬 5 • ⭐ 1,070 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 59.7k • 🔱 8.3k • 3d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.9k • 🔱 1.1k • 2d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.1k • 🔱 707 • 1d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 8.4k • 🔱 692 • 10h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.2k • 🔱 1.1k • 3d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 3.7k • 🔱 475 • 5h ago

---

**[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)**

Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work). Chat with your AI dev assistant from anywhere — no public IP required for most platforms.

`Go`

⭐ 3.4k • 🔱 297 • 34m ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.3k • 🔱 216 • 14d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.2k • 🔱 104 • 17d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 3.1k • 🔱 278 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
