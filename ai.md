---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-30T10:18:15.921633+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 30, 2026 at 10:18 UTC  
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

**[Big increase in the amount of people using AI to write their replies with AI](https://www.reddit.com/r/artificial/comments/1s7k3n4/big_increase_in_the_amount_of_people_using_ai_to/)**

I find it interesting that we’ve all randomly decided to use the “-“ more often recently on reddit, and everyone’s grammar has drastically improved. Specifically on highly technical subreddits like this one, when people want to appear like they understand concepts or granular details they just feed it into AI to give them an answer. To me this feels dangerous, we’re essentially offloading entertainment for an AI to process so we get a dopamine hit. We aren’t even able to browse the internet anymore without AI doing it for us. We can’t even argue without AI feeding us an argument. This is the destruction of conversation globally. It isn’t a one world government or a tyrannical leader, it’s humanity collectively deciding we would rather not think than think, because thinking is hard. When thinking is the main ability which separates us from animals, so we’re becoming apes who can type because it’s convenient.

2h ago

---

**[Nicolas Carlini (67.2k citations on Google Scholar) says Claude is a better security researcher than him, made $3.7 million from exploiting smart contracts, and found vulnerabilities in Linux and Ghost](https://www.reddit.com/r/artificial/comments/1s738xf/nicolas_carlini_672k_citations_on_google_scholar/)**

Link: https://m.youtube.com/watch?v=1sd26pWhfmg The Linux exploit is especially interesting because it was introduced in 2003 and was never found until now. It’s also a major security issue because it allows attackers to steal the admin key. It was a buffer overflow error, which are so hard to do that Carlini has never done it before. He also says he expects LLMs to only get better overtime, which is likely true if Mythos lives up to the rumors. here are his Wikipedia and Google Scholar pages in case you doubt his credibility: https://en.wikipedia.org/wiki/Nicholas_Carlini https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=carlini&btnG=

15h ago

---

**[We built a fully deterministic control layer for agents. Would love feedback. No pitch](https://www.reddit.com/r/artificial/comments/1s7dlk7/we_built_a_fully_deterministic_control_layer_for/)**

Most of the current “AI security” stack seems focused on: • prompts • identities • outputs After an agent deleted a prod database on me a year ago. I saw the gap and started building. a control layer directly in the execution path between agents and tools. We are to market but I don’t want to spam yall with our company so I left it out. ⸻ What that actually means Every time an agent tries to take an action (API call, DB read, file access, etc.), we intercept it and decide in real time: • allow • block • require approval But the important part is how that decision is made. ⸻ A few things we’re doing differently Credential starvation (instead of trusting long-lived access) Agents don’t get broad, persistent credentials. They effectively operate with nothing by default, and access is granted per action based on policy + context. ⸻ Session-based risk escalation (not stateless checks) We track behavior across the entire session. Example: • one DB read → fine • 20 sequential reads + export → risk escalates • tool chaining → risk escalates So decisions aren’t per-call—they’re based on what the agent has been doing over time. ⸻ HITL only when it actually matters We don’t want humans in the loop for everything. Instead: • low risk → auto allow • medium risk → maybe constrained • high risk → require approval The idea is targeted interruption, not constant friction. ⸻ Autonomy zones Different environments/actions have different trust levels. Example: • read-only internal data → low autonomy constraints • external API writes → tighter controls • sensitive systems → very restricted Agents can operate freely within a zone, but crossing boundaries triggers stricter enforcement. ⸻ Per-tool, per-action control (not blanket policies) Not just “this agent can use X tool” More like: • what endpoints • what parameters • what frequency • in what sequence So risk is evaluated at a much more granular level. ⸻ Hash-chained audit log (including near-misses) Every action (allowed, blocked, escalated) is: • logged • chained • tamper-evident Including “almost bad” behavior not just incidents. This ended up being more useful than expected for understanding agent behavior. ⸻ Policy engine (not hardcoded rules) All of this runs through a policy layer (think flexible rules vs static checks), so behavior can adapt without rewriting code. ⸻ Setup is fast (~10 min) We tried to avoid the “months of integration” problem. If it’s not easy to sit in the execution path, nobody will actually use it. ⸻ Why we think this matters The failure mode we keep seeing: agents don’t fail because of one bad prompt — they fail because of a series of individually reasonable actions that become risky together Most tooling doesn’t really account for that. ⸻ Would love feedback from people actually building agents • Have you seen agents drift into risky behavior over time? • How are you controlling tool usage today (if at all)? • Does session-level risk make sense, or is that overkill? • Is “credential starvation” realistic in your setups? We are just two security guys who built a company not some McKenzie bros who are super funded. We have our first big design partners starting this month and need all these feedback from community as we can get.

8h ago

---

**[CLI for Google AI Search (gai.google) — run AI-powered code/tech searches headlessly from your terminal](https://www.reddit.com/r/artificial/comments/1s7k1sg/cli_for_google_ai_search_gaigoogle_run_aipowered/)**

Google AI (gai.google) gives Gemini-powered answers for technical queries — think AI-enhanced search with code understanding. I built a CLI for it using headless Playwright since the site is fully browser-rendered. cli-web-gai search "how does Redis persistence work" cli-web-gai search "Python asyncio vs threading" --json cli-web-gai search "Rust ownership model explained" --format markdown Because the site renders in-browser (no public API), the CLI spins up a headless Chromium session, runs the query, and extracts the structured response. No auth needed — fully public. Output includes the AI answer, any code blocks, and source citations. --json gives structured output for piping into other tools or agents. Open source: https://github.com/ItamarZand88/CLI-Anything-WEB/tree/main/gai Full project (13 CLIs): https://github.com/ItamarZand88/CLI-Anything-WEB

2h ago

---

**[What actually prevents execution in agent systems?](https://www.reddit.com/r/artificial/comments/1s76o5b/what_actually_prevents_execution_in_agent_systems/)**

Ran into this building an agent that could trigger API calls. We had validation, tool constraints, retries… everything looked “safe”. Still ended up executing the same action twice due to stale state + retry. Nothing actually prevented execution. It only shaped behavior. Curious what people use as a real execution gate: 1. something external to the agent 2. deterministic allow / deny 3. fail-closed if denied Any concrete patterns or systems that enforce this in practice?

13h ago

---

**[Be Amazed reddit isn’t impressed](https://www.reddit.com/r/artificial/comments/1s7kwh8/be_amazed_reddit_isnt_impressed/)**

The purpose of the Be amazed of Reddit was to be amazed. There was a post recently about an uncle who did some type of geographical stuff with rocks to make art and it’s been figured out that it wasn’t original content, originally years ago. Someone else’s uncle has been spread online and his image shared for public use by others from different accounts already so I did the same; only the 2026 version. my purpose wasn’t to post AI “slop” as they commented and moderated, but the layered concept of the fact that it’s pretty amazing that you can take a popular post (That’s been already posted over and over again) and in seconds recreate a different version of a different state of a different place and person. general public of be amazed reddit community misses the point. all reddit users are not the same. In minute it got thousands of views only a few comments and just because of some heated individuals, even though flared as art with no guidelines against how the art is produced specifically the moderator still removed it even though the recent repost of the uncles art supposedly from within 24 hours ago, got all the love even though it was someone else’s work just taken and presented in their own way and their own username. There’s other post and images like that that are edited and shared. That’s literally what art is. people borrow interpret and make it their own. I find an art to be the same and once again, pretty amazing. I kind of did it to see where is the line of amazement. When will people shift their view to understand how amazing creating images is? Maybe not objectively every single image created it’s amazing but this specific idea of posting something that can borrow from another post in seconds and re-create a whole different state with different rocks. I’m ranting now, but please discuss.

1h ago

---

**[Persistent memory changes how people interact with AI — here's what I'm observing](https://www.reddit.com/r/artificial/comments/1s6jvog/persistent_memory_changes_how_people_interact/)**

I run a small AI companion platform and wanted to share some interesting behavioral data from users who've been using persistent cross-session memory for 2-3 months now. Some patterns I didn't expect: "Deep single-thread" users dominate. 56% of our most active users put 70%+ of their messages into a single conversation thread. They're not creating multiple characters or scenarios — they're deepening one relationship. This totally contradicts the assumption that users are "scenario hoppers." Memory recall triggers emotional responses. When the AI naturally brings up something from weeks ago — "how did that job interview go?" or referencing a pet's name without being prompted — users consistently react with surprise and increased engagement. It's a retention mechanic that doesn't feel like a retention mechanic. The "uncanny valley" of memory exists. If the AI remembers too precisely (exact dates, verbatim quotes), it feels surveillance-like. If it remembers too loosely, it feels like it didn't really listen. The sweet spot is what I'd call "emotionally accurate but detail-fuzzy" — like how a real friend remembers. Day-7 retention correlates with memory depth. Users who trigger 5+ memory retrievals in their first week retain at nearly 4x the rate of those who don't. The memory system IS the product, not a feature. Sample size is small (~800 users) so take this with appropriate skepticism. But it's consistent enough that I think persistent memory is going to be table stakes for AI companions within a year. What's your experience with memory in AI conversations? Anyone else building in this space?

1d ago

---

**[Does your manager use AI to write their messages – and would you even know?](https://www.reddit.com/r/artificial/comments/1s70rqr/does_your_manager_use_ai_to_write_their_messages/)**

Sharing this for a friend conducting an academic study for her MBA thesis on how employees make sense of AI use in workplace communication. Specifically: disclosed vs. inferred AI use, and what difference that makes. Anonymous, under 5 minutes: English: https://whudrdl.qualtrics.com/jfe/form/SV\_1G4k3TKx8xhXwXQ German: https://whudrdl.qualtrics.com/jfe/form/SV\_3OYZNjGJr4qfceq Thanks a lot for your participation and support!

17h ago

---

**[Claude is the least bullshit-y AI](https://www.reddit.com/r/artificial/comments/1s67buc/claude_is_the_least_bullshity_ai/)**

Just found this “bullshit benchmark,” and sort of shocked by the divergence of Anthropic’s models from other major models (ChatGPT and Gemini). IMO this alone is reason to use Claude over others.

🔗 [GitHub](https://github.com/petergpt/bullshit-benchmark?tab=readme-ov-file#3-detection-rate-over-time) • 1d ago

---

**[The AI hype misses the people who actually need it most](https://www.reddit.com/r/artificial/comments/1s6fws6/the_ai_hype_misses_the_people_who_actually_need/)**

Every day someone posts "AI will change everything" and it's always about agents scaling businesses, automating workflows, 10x productivity, whatever. Cool. But change everything for who? Go talk to the barber who loses 3 clients a week to no-shows and can't afford a booking system that actually works. Go talk to the solo attorney who's drowning in intake paperwork and can't afford a paralegal. Go talk to the tattoo artist who's on the phone all day instead of tattooing. Go talk to the author who wrote a book and has zero idea how to market it. These people don't need another app. They don't need to "learn to code." They don't need to understand what an LLM is. They need the tools that already exist and wired into their actual business. Their actual pain. The gap between "AI can do amazing things" and "I can actually use AI to make my life better" is where most of the world lives right now. And most of the AI community is completely disconnected from that reality. We're on Reddit at midnight debating MCP vs direct API and arguing about whether Opus or Sonnet is better for agent routing. That's not most people. Most people are just trying to survive running a business they started because they're good at something and not because they wanted to become a full-time administrator. If every small business owner, every freelancer, every solo professional had agents handling the repetitive stuff ya kno...the follow-ups, the scheduling, the content, the bookkeeping; you wouldn't just get productivity. You'd get a renaissance. Because people who are drowning in admin don't create. People who are free to think do. I genuinely believe the next wave isn't a new model or a new framework. It's someone taking the tools that exist right now and actually putting them in the hands of people who need them. Not the next unicorn. Not the next platform. Just the bridge between the AI and the human. What would it actually take to make that happen?

1d ago

---

---

## Google News: "ai"

**[Police used AI facial recognition to arrest a Tennessee woman for crimes committed in a state she says she’s never visited](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

CNN • 1d ago

---

**[Tech CEOs suddenly love blaming AI for mass job cuts. Why?](https://www.bbc.com/news/articles/cde5y2x51y8o)**

More tech leaders are pointing to job cuts caused by AI tools - and a need for more investment cash.

BBC • 11h ago

---

**[AI leaders align against Elon Musk](https://www.axios.com/2026/03/30/elon-musk-openai-altman-anthropic)**

Axios • 59m ago

---

**[Mistral secures $830 million in debt financing to fund AI data center](https://www.cnbc.com/2026/03/30/mistral-ai-paris-data-center-cluster-debt-financing.html)**

Mistral is one of the few European startups building foundational AI models.

cnbc.com • 3h ago

---

**[France's Mistral raises $830 million in debt for AI data centre build-up](https://www.reuters.com/business/finance/frances-mistral-raises-830-million-debt-ai-data-centre-build-up-2026-03-30/)**

Reuters • 4h ago

---

**[Mistral raises $830mn to build Nvidia-powered AI centres in Europe](https://www.ft.com/content/229f4f59-d518-4e00-abd6-5a5b727cd2aa)**

French company’s debut debt financing follows rising demand for alternatives to US groups

Financial Times • 2h ago

---

**[LaGuardia Crash Bolsters Case for Using AI in Air Control Towers](https://www.bloomberg.com/news/articles/2026-03-30/laguardia-crash-bolsters-case-for-using-ai-in-air-control-towers)**

Bloomberg.com • 18m ago

---

**[Pro-AI group to spend $100mn on US midterm elections as backlash grows](https://www.ft.com/content/6a3f1938-759d-4ae4-924e-6a0feac14e24?syn-25a6b1a6=1)**

November 3 poll set to be battleground over regulation of AI

Financial Times • 10h ago

---

**[The Man Who Thought He Could Keep AI Safe](https://www.theatlantic.com/ideas/2026/03/ai-google-deep-mind-hassabis/686527/)**

Demis Hassabis has devoted his life to advancing a technology he thinks could destroy the world.

The Atlantic • 1d ago

---

**[Drone swarms: The potential AI future of drone warfare](https://www.cbsnews.com/news/drone-swarms-the-potential-ai-future-of-drone-warfare-60-minutes/)**

The architect of Ukraine's drone program Oleksandr Kamyshin told Holly Williams drone swarm technology that uses AI would provide a major advantage in the war with Russia, and there is an arms race for the technology. "Both countries are close. None got there yet," he told 60 Minutes.

CBS News • 10h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 772 • 💬 606 • 1d ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[AI got the blame for the Iran school bombing. The truth is more worrying](https://news.ycombinator.com/item?id=47544980)**

LLMs-gone-rogue dominated coverage, but had nothing to do with the targeting. Instead, it was choices made by human beings, over many years, that gave us this atrocity

⬆️ 405 • 💬 377 • 2d ago • [the Guardian](https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying)

---

**[Police used AI facial recognition to wrongly arrest TN woman for crimes in ND](https://news.ycombinator.com/item?id=47563384)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

⬆️ 394 • 💬 171 • 19h ago • [CNN](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 325 • 💬 146 • 2d ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[Miasma: A tool to trap AI web scrapers in an endless poison pit](https://news.ycombinator.com/item?id=47561819)**

Trap AI web scrapers in an endless poison pit. Contribute to austin-weeks/miasma development by creating an account on GitHub.

⬆️ 319 • 💬 229 • 1d ago • [GitHub](https://github.com/austin-weeks/miasma)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 283 • 💬 221 • 1d ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 254 • 💬 175 • 1d ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 212 • 💬 141 • 1d ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

**[What if AI doesn't need more RAM but better math?](https://news.ycombinator.com/item?id=47561297)**

⬆️ 175 • 💬 92 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more)

---

**[I am leaving the AI party after one drink](https://news.ycombinator.com/item?id=47545030)**

Personal website of Lara Aigmüller. Thoughts about web frontend development, music, and more…

⬆️ 120 • 💬 129 • 2d ago • [lara-aigmueller.at](https://lara-aigmueller.at/thoughts/leaving-the-ai-party/)

---

---

## YouTube Videos: "ai"

**[Anthropic’s New Claude MYTHOS Is The Most Powerful AI Ever!](https://www.youtube.com/watch?v=M6yRREy_5CM)**

Anthropic accidentally exposed Claude MYTHOS, its most powerful AI yet, Meta unveiled a model that predicts brain activity from ...

📺 AI Revolution

👁️ 17K • 👍 623 • 💬 37 • ⏱️ 12:51 • 10h ago

---

**[The AI Endgame (12 Scenarios)](https://www.youtube.com/watch?v=FLcrvMfHUJM)**

Detailed sources: https://docs.google.com/document/d/1P1X9xEmmgSYH0g1FSizgV2rDVomb_Wi0TcX-E-0np_Q/edit?tab=t.0 ...

📺 Species | Documenting AGI

👁️ 59K • 👍 4K • 💬 958 • ⏱️ 35:45 • 18h ago

---

**[Robot waifus, RIP Sora, GLM-5.1, AI brain scans, Google realtime voice: AI NEWS](https://www.youtube.com/watch?v=6Il0CJx9yU8)**

HUGE AI NEWS: GLM-5.1, daVinci MagiHuman, ARC-AGI 3, PrismAudio, Matrix Game, & more #ai #ainews #aitools #aivideo ...

📺 AI Search

👁️ 79K • 👍 4K • 💬 452 • ⏱️ 47:29 • 1d ago

---

**[Gary Vee: The AI Opportunity Is Real — You&#39;re Just Looking at It Wrong](https://www.youtube.com/watch?v=4vIIeCqHYXA)**

Build your own AI agent team and automate your daily ops with Accio Work — use my exclusive invite code SILVLG to skip the ...

📺 Silicon Valley Girl

👁️ 33K • 👍 1K • 💬 92 • ⏱️ 44:41 • 2d ago

---

**[Claude AI: Incredible New Way to Make Money Online (Full Tutorial)](https://www.youtube.com/watch?v=48Qg6ZX60r8)**

I show how to use Claude AI to create and sell in-demand, Notion templates online! ▷ Create Incredible Videos and Images with ...

📺 Real Money Strategies

👁️ 21K • 👍 906 • 💬 42 • ⏱️ 19:13 • 2d ago

---

**[Anthropic&#39;s Biggest Mistake Just Leaked Their Most Powerful AI (+ 9 AI Updates)](https://www.youtube.com/watch?v=c4Mgp3FWvt0)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT10 ...

📺 Vaibhav Sisinty

👁️ 39K • 👍 1K • 💬 48 • ⏱️ 15:58 • 19h ago

---

**[AI News: Anthropic Went Crazy This Week!](https://www.youtube.com/watch?v=OYyS0Gu5xj8)**

Here's the AI News you probably missed this week! Check out Genspark here: ...

📺 Matt Wolfe

👁️ 98K • 👍 4K • 💬 292 • ⏱️ 31:53 • 2d ago

---

**[Why Replacing Humans with AI is Backfiring](https://www.youtube.com/watch?v=bNJad6HE23c)**

jobmarket #ai #tech In this video, we explore why the AI gold rush is hitting a wall. Companies that rushed to automate are now ...

📺 Mackard

👁️ 200K • 👍 5K • 💬 477 • ⏱️ 8:01 • 2d ago

---

**[AI News: Gemini Is SO Much Better Now (+ NotebookLM, Claude and Siri Updates)](https://www.youtube.com/watch?v=jWNlxQQ_W_Q)**

This week's biggest AI updates (and rumors) you actually need to know. From a huge Gemini Live upgrade to a slick new ...

📺 Paul J Lipsky

👁️ 54K • 👍 2K • 💬 135 • ⏱️ 15:05 • 1d ago

---

**[The AI boom is a lie: Fake data centres and unused GPUs | Ed Zitron](https://www.youtube.com/watch?v=nxUEOdC4VzU)**

Hyperscalers have gone from the asset light cash machines to asset heavy behemoths.” Author of Where's Your Ed At and host of ...

📺 The Tech Report

👁️ 224K • 👍 10K • 💬 2K • ⏱️ 32:39 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 309,355 • ❤️ 1,605 • 6d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 28,233 • ❤️ 487 • 2d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 2,939 • ❤️ 478 • 2d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 16,297 • ❤️ 615 • 3d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 1,450 • ❤️ 253 • 9h ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 569,033 • ❤️ 1,066 • 19d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 540 • ❤️ 251 • 4d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 78,162 • ❤️ 406 • 5d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 140,733 • ❤️ 254 • 5d ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 9,919 • ❤️ 176 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 28,008 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 32 • 💬 2 • ⭐ 43,955 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 40 • 💬 2 • ⭐ 22,061 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 60 • 💬 4 • ⭐ 22,091 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 17 • 💬 4 • ⭐ 3,930 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 36 • 💬 5 • ⭐ 1,886 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 10,781 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 10 • 💬 2 • ⭐ 1,413 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 30 • 💬 1 • ⭐ 759 • 26d ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 1 • ⭐ 13,883 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 61.1k • 🔱 8.5k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 23.1k • 🔱 1.1k • 3d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.5k • 🔱 739 • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 9.0k • 🔱 750 • 4h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.5k • 🔱 1.2k • 1d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 5.9k • 🔱 703 • 3h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

A command-line tool for Lark/Feishu Open Platform — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 4.2k • 🔱 186 • 2h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 3.9k • 🔱 374 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.3k • 🔱 220 • 16d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.2k • 🔱 107 • 18d ago

---

---

*Generated by PeekDeck - A glance is all you need*
