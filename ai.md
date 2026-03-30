---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-30T05:26:23.407695+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 30, 2026 at 05:26 UTC  
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

**[Nicolas Carlini (67.2k citations on Google Scholar) says Claude is a better security researcher than him, made $3.7 million from exploiting smart contracts, and found vulnerabilities in Linux and Ghost](https://www.reddit.com/r/artificial/comments/1s738xf/nicolas_carlini_672k_citations_on_google_scholar/)**

Link: https://m.youtube.com/watch?v=1sd26pWhfmg The Linux exploit is especially interesting because it was introduced in 2003 and was never found until now. It’s also a major security issue because it allows attackers to steal the admin key. It was a buffer overflow error, which are so hard to do that Carlini has never done it before. He also says he expects LLMs to only get better overtime, which is likely true if Mythos lives up to the rumors. here are his Wikipedia and Google Scholar pages in case you doubt his credibility: https://en.wikipedia.org/wiki/Nicholas_Carlini https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=carlini&btnG=

10h ago

---

**[What actually prevents execution in agent systems?](https://www.reddit.com/r/artificial/comments/1s76o5b/what_actually_prevents_execution_in_agent_systems/)**

Ran into this building an agent that could trigger API calls. We had validation, tool constraints, retries… everything looked “safe”. Still ended up executing the same action twice due to stale state + retry. Nothing actually prevented execution. It only shaped behavior. Curious what people use as a real execution gate: 1. something external to the agent 2. deterministic allow / deny 3. fail-closed if denied Any concrete patterns or systems that enforce this in practice?

8h ago

---

**[We built a fully deterministic control layer for agents. Would love feedback. No pitch](https://www.reddit.com/r/artificial/comments/1s7dlk7/we_built_a_fully_deterministic_control_layer_for/)**

Most of the current “AI security” stack seems focused on: • prompts • identities • outputs After an agent deleted a prod database on me a year ago. I saw the gap and started building. a control layer directly in the execution path between agents and tools. We are to market but I don’t want to spam yall with our company so I left it out. ⸻ What that actually means Every time an agent tries to take an action (API call, DB read, file access, etc.), we intercept it and decide in real time: • allow • block • require approval But the important part is how that decision is made. ⸻ A few things we’re doing differently Credential starvation (instead of trusting long-lived access) Agents don’t get broad, persistent credentials. They effectively operate with nothing by default, and access is granted per action based on policy + context. ⸻ Session-based risk escalation (not stateless checks) We track behavior across the entire session. Example: • one DB read → fine • 20 sequential reads + export → risk escalates • tool chaining → risk escalates So decisions aren’t per-call—they’re based on what the agent has been doing over time. ⸻ HITL only when it actually matters We don’t want humans in the loop for everything. Instead: • low risk → auto allow • medium risk → maybe constrained • high risk → require approval The idea is targeted interruption, not constant friction. ⸻ Autonomy zones Different environments/actions have different trust levels. Example: • read-only internal data → low autonomy constraints • external API writes → tighter controls • sensitive systems → very restricted Agents can operate freely within a zone, but crossing boundaries triggers stricter enforcement. ⸻ Per-tool, per-action control (not blanket policies) Not just “this agent can use X tool” More like: • what endpoints • what parameters • what frequency • in what sequence So risk is evaluated at a much more granular level. ⸻ Hash-chained audit log (including near-misses) Every action (allowed, blocked, escalated) is: • logged • chained • tamper-evident Including “almost bad” behavior not just incidents. This ended up being more useful than expected for understanding agent behavior. ⸻ Policy engine (not hardcoded rules) All of this runs through a policy layer (think flexible rules vs static checks), so behavior can adapt without rewriting code. ⸻ Setup is fast (~10 min) We tried to avoid the “months of integration” problem. If it’s not easy to sit in the execution path, nobody will actually use it. ⸻ Why we think this matters The failure mode we keep seeing: agents don’t fail because of one bad prompt — they fail because of a series of individually reasonable actions that become risky together Most tooling doesn’t really account for that. ⸻ Would love feedback from people actually building agents • Have you seen agents drift into risky behavior over time? • How are you controlling tool usage today (if at all)? • Does session-level risk make sense, or is that overkill? • Is “credential starvation” realistic in your setups? We are just two security guys who built a company not some McKenzie bros who are super funded. We have our first big design partners starting this month and need all these feedback from community as we can get.

3h ago

---

**[One-Minute Daily AI News 3/29/2026](https://www.reddit.com/r/artificial/comments/1s7gyyf/oneminute_daily_ai_news_3292026/)**

Police used AI facial recognition to arrest a Tennessee woman for crimes committed in a state she says she’s never visited.[1] AMD Introduces GAIA Agent UI For Privacy-First Web App For Local AI Agents.[2] Agent-Infra Releases AIO Sandbox: An All-in-One Runtime for AI Agents with Browser, Shell, Shared Filesystem, and MCP.[3] Google-Agent vs Googlebot: Google Defines the Technical Boundary Between User Triggered AI Access and Search Crawling Systems Today.[4] Sources: [1] https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition [2] https://www.phoronix.com/news/AMD-GAIA-0.17-Agent-UI [3] https://www.marktechpost.com/2026/03/29/agent-infra-releases-aio-sandbox-an-all-in-one-runtime-for-ai-agents-with-browser-shell-shared-filesystem-and-mcp/ [4] https://www.marktechpost.com/2026/03/28/google-agent-vs-googlebot-google-defines-the-technical-boundary-between-user-triggered-ai-access-and-search-crawling-systems-today/

46m ago

---

**[Reddit on the rise: What is it and why is AI search popularising it?](https://www.reddit.com/r/artificial/comments/1s7ff07/reddit_on_the_rise_what_is_it_and_why_is_ai/)**

Reddit has become the AI algorithm’s favourite website. This is why it is becoming popular, and how to use it.

🔗 [euronews](https://www.euronews.com/next/2026/02/28/reddit-on-the-rise-what-is-it-and-why-is-ai-search-popularising-it) • 2h ago

---

**[Persistent memory changes how people interact with AI — here's what I'm observing](https://www.reddit.com/r/artificial/comments/1s6jvog/persistent_memory_changes_how_people_interact/)**

I run a small AI companion platform and wanted to share some interesting behavioral data from users who've been using persistent cross-session memory for 2-3 months now. Some patterns I didn't expect: "Deep single-thread" users dominate. 56% of our most active users put 70%+ of their messages into a single conversation thread. They're not creating multiple characters or scenarios — they're deepening one relationship. This totally contradicts the assumption that users are "scenario hoppers." Memory recall triggers emotional responses. When the AI naturally brings up something from weeks ago — "how did that job interview go?" or referencing a pet's name without being prompted — users consistently react with surprise and increased engagement. It's a retention mechanic that doesn't feel like a retention mechanic. The "uncanny valley" of memory exists. If the AI remembers too precisely (exact dates, verbatim quotes), it feels surveillance-like. If it remembers too loosely, it feels like it didn't really listen. The sweet spot is what I'd call "emotionally accurate but detail-fuzzy" — like how a real friend remembers. Day-7 retention correlates with memory depth. Users who trigger 5+ memory retrievals in their first week retain at nearly 4x the rate of those who don't. The memory system IS the product, not a feature. Sample size is small (~800 users) so take this with appropriate skepticism. But it's consistent enough that I think persistent memory is going to be table stakes for AI companions within a year. What's your experience with memory in AI conversations? Anyone else building in this space?

1d ago

---

**[Does your manager use AI to write their messages – and would you even know?](https://www.reddit.com/r/artificial/comments/1s70rqr/does_your_manager_use_ai_to_write_their_messages/)**

Sharing this for a friend conducting an academic study for her MBA thesis on how employees make sense of AI use in workplace communication. Specifically: disclosed vs. inferred AI use, and what difference that makes. Anonymous, under 5 minutes: English: https://whudrdl.qualtrics.com/jfe/form/SV\_1G4k3TKx8xhXwXQ German: https://whudrdl.qualtrics.com/jfe/form/SV\_3OYZNjGJr4qfceq Thanks a lot for your participation and support!

12h ago

---

**[Claude is the least bullshit-y AI](https://www.reddit.com/r/artificial/comments/1s67buc/claude_is_the_least_bullshity_ai/)**

Just found this “bullshit benchmark,” and sort of shocked by the divergence of Anthropic’s models from other major models (ChatGPT and Gemini). IMO this alone is reason to use Claude over others.

🔗 [GitHub](https://github.com/petergpt/bullshit-benchmark?tab=readme-ov-file#3-detection-rate-over-time) • 1d ago

---

**[The AI hype misses the people who actually need it most](https://www.reddit.com/r/artificial/comments/1s6fws6/the_ai_hype_misses_the_people_who_actually_need/)**

Every day someone posts "AI will change everything" and it's always about agents scaling businesses, automating workflows, 10x productivity, whatever. Cool. But change everything for who? Go talk to the barber who loses 3 clients a week to no-shows and can't afford a booking system that actually works. Go talk to the solo attorney who's drowning in intake paperwork and can't afford a paralegal. Go talk to the tattoo artist who's on the phone all day instead of tattooing. Go talk to the author who wrote a book and has zero idea how to market it. These people don't need another app. They don't need to "learn to code." They don't need to understand what an LLM is. They need the tools that already exist and wired into their actual business. Their actual pain. The gap between "AI can do amazing things" and "I can actually use AI to make my life better" is where most of the world lives right now. And most of the AI community is completely disconnected from that reality. We're on Reddit at midnight debating MCP vs direct API and arguing about whether Opus or Sonnet is better for agent routing. That's not most people. Most people are just trying to survive running a business they started because they're good at something and not because they wanted to become a full-time administrator. If every small business owner, every freelancer, every solo professional had agents handling the repetitive stuff ya kno...the follow-ups, the scheduling, the content, the bookkeeping; you wouldn't just get productivity. You'd get a renaissance. Because people who are drowning in admin don't create. People who are free to think do. I genuinely believe the next wave isn't a new model or a new framework. It's someone taking the tools that exist right now and actually putting them in the hands of people who need them. Not the next unicorn. Not the next platform. Just the bridge between the AI and the human. What would it actually take to make that happen?

1d ago

---

**[Surveillance data used to be boring. AI made it dangerous.](https://www.reddit.com/r/artificial/comments/1s6hvhk/surveillance_data_used_to_be_boring_ai_made_it/)**

Here's a playbook that works today, right now, with tools that are either free or cheap: Someone finds a photo of you online. One photo. They run it through a face ID search and find your other photos across the internet. They drop one into GeoSpy, which analyzes background details in images to estimate where you live. A street sign, a building style, a type of tree. It's scarily accurate. Now they search Shodan for exposed camera feeds near that location. If you're in one of the 6,000+ communities using Flock Safety cameras, you might be in luck. Late last year, researchers found 67 Flock cameras streaming live to the open internet with no password and no encryption. A journalist watched himself in real time from his phone. Flock called it a "limited misconfiguration." They're valued at $7.5 billion. With footage of your routine, an AI agent can build a profile. When you leave for work. What car you drive. Who visits. Then they enrich it with data brokers selling your phone number, email, employment history, and purchase patterns for a few dollars. Public records fill in the rest. Now they have your face, your voice from any video you've posted, your writing style from your social media, your daily patterns from camera footage, and your personal details from brokers. Voice cloning needs three seconds of audio. Deepfake video passes casual inspection. They can call your bank as you. Email your boss as you. Social-engineer your family as you. One photo started it. I've been reading patent filings on AI surveillance systems for a while. The capabilities in those filings are years ahead of the security protecting the data they collect. As an entrepreneur, I can think of solutions to fight back against this or potentially profit off of this. How do you feel about the implications of the technology that exists today with this much potential for harm?

1d ago

---

---

## Google News: "ai"

**[Police used AI facial recognition to arrest a Tennessee woman for crimes committed in a state she says she’s never visited](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

CNN • 19h ago

---

**[Tech CEOs suddenly love blaming AI for mass job cuts. Why?](https://www.bbc.com/news/articles/cde5y2x51y8o)**

More tech leaders are pointing to job cuts caused by AI tools - and a need for more investment cash.

BBC • 6h ago

---

**[One Man, His Dog, And ChatGPT: Australia's AI Vaccine Saga](https://www.barrons.com/articles/one-man-his-dog-and-chatgpt-australia-s-ai-vaccine-saga-396cf9d7?gaa_at=eafs&gaa_n=AWEtsqdvUWsbUGeApA3-Hyao2iDNH22lyxHY97gyadWTpYkcGJbFrEaLNIlI&gaa_ts=69ca0ce7&gaa_sig=ilSe0T9qcW94q2XC61TFfrbWO2TXwQkEoIt3dlvYXudlv5RjxkajFVQCEh_-1J1ZpbegVaG1ZfAf4dCVCB3TTw%3D%3D)**

Barron's • 9m ago

---

**[AI influencer discovery tools are changing how agencies cast creators](https://digiday.com/marketing/ai-influencer-discovery-tools-are-changing-how-agencies-cast-creators/)**

As creator spending grows among brands, agencies tap AI to automate much of the influencer marketing workflow. Now, that includes casting.

Digiday • 1h ago

---

**[The Anti-AI Slop Playbook](https://www.vogue.com/article/the-anti-ai-slop-playbook)**

As generative AI floods the market with fast, low-cost content, luxury brands are learning to harness the tech without eroding the value of craft, authorship, and cultural authority. From “anti-slop” design cues to immersive real-world experiences, a new playbook is emerging.

Vogue • 56m ago

---

**[JFK grandson Schlossberg says billionaires, ‘massive AI companies’ spending millions in New York House race](https://thehill.com/homenews/campaign/5806153-jfk-grandson-schlossberg-says-billionaires-massive-ai-companies-spending-millions-in-new-york-house-race/)**

The Hill • 18h ago

---

**[Opinion | Your Chatbot Isn’t a Therapist](https://www.nytimes.com/2026/03/29/opinion/chatbot-therapy-ai.html)**

The New York Times • 16h ago

---

**[Eli Lilly reaches $2.75 billion deal with Insilico to bring AI-developed drugs to the global market](https://www.cnbc.com/2026/03/29/eli-lilly-reaches-deal-to-bring-ai-developed-drugs-to-global-market.html)**

U.S. pharmaceutical giant Eli Lilly will give Hong Kong-listed Insilico $115 million upfront to bring some of its AI-discovered drugs to the global market.

CNBC • 15h ago

---

**[AI drug developer Insilico Medicine and Lilly ink commercialization deal worth up to $2.75 billion](https://www.statnews.com/2026/03/29/insilico-medicine-lilly-sign-ai-drug-commercialization-deal/)**

Lilly has signed a deal with AI drug developer Insilico that’s worth $115 million up front and approximately $2.75 billion in biobucks

statnews.com • 11h ago

---

**[Eli Lilly, InSilico Strike AI Drug Discovery Deal](https://www.wsj.com/health/pharma/eli-lilly-insilico-strike-ai-drug-discovery-deal-acea2b45?gaa_at=eafs&gaa_n=AWEtsqeHMuw-2zG1j3HOzVEVx0fbkqoR2Viig1IgZTm7XfjmO0YZTXv4AxYJ&gaa_ts=69ca0ce7&gaa_sig=1ia-MF7EOTSKAnD0aApPA-mdBrUFck_OsG8VCkakt7Y3nmxeMGfk0aAbhNNpB8CW8owlZtIzsJheP_94ZkgrXA%3D%3D)**

WSJ • 1h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 760 • 💬 597 • 1d ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[AI got the blame for the Iran school bombing. The truth is more worrying](https://news.ycombinator.com/item?id=47544980)**

LLMs-gone-rogue dominated coverage, but had nothing to do with the targeting. Instead, it was choices made by human beings, over many years, that gave us this atrocity

⬆️ 405 • 💬 377 • 2d ago • [the Guardian](https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying)

---

**[Police used AI facial recognition to wrongly arrest TN woman for crimes in ND](https://news.ycombinator.com/item?id=47563384)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

⬆️ 380 • 💬 164 • 15h ago • [CNN](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 325 • 💬 146 • 1d ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[Miasma: A tool to trap AI web scrapers in an endless poison pit](https://news.ycombinator.com/item?id=47561819)**

Trap AI web scrapers in an endless poison pit. Contribute to austin-weeks/miasma development by creating an account on GitHub.

⬆️ 304 • 💬 220 • 19h ago • [GitHub](https://github.com/austin-weeks/miasma)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 282 • 💬 221 • 1d ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 252 • 💬 173 • 1d ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 211 • 💬 139 • 1d ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

**[What if AI doesn't need more RAM but better math?](https://news.ycombinator.com/item?id=47561297)**

⬆️ 168 • 💬 89 • 21h ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more)

---

**[I am leaving the AI party after one drink](https://news.ycombinator.com/item?id=47545030)**

Personal website of Lara Aigmüller. Thoughts about web frontend development, music, and more…

⬆️ 120 • 💬 129 • 2d ago • [lara-aigmueller.at](https://lara-aigmueller.at/thoughts/leaving-the-ai-party/)

---

---

## YouTube Videos: "ai"

**[Anthropic’s New Claude MYTHOS Is Their Most Powerful AI Ever](https://www.youtube.com/watch?v=M6yRREy_5CM)**

Anthropic accidentally exposed Claude MYTHOS, its most powerful AI yet, Meta unveiled a model that predicts brain activity from ...

📺 AI Revolution

👁️ 10K • 👍 464 • 💬 32 • ⏱️ 12:51 • 5h ago

---

**[The AI Endgame (12 Scenarios)](https://www.youtube.com/watch?v=FLcrvMfHUJM)**

Detailed sources: https://docs.google.com/document/d/1P1X9xEmmgSYH0g1FSizgV2rDVomb_Wi0TcX-E-0np_Q/edit?tab=t.0 ...

📺 Species | Documenting AGI

👁️ 50K • 👍 4K • 💬 851 • ⏱️ 35:45 • 14h ago

---

**[I Ranked EVERY AI Video Generator From Best to Worst in 2026](https://www.youtube.com/watch?v=kQF7sxNXpsU)**

I Tried Every AI Video Generator and ranked them for you!. Try ALL AI Video Generators here➡️ ...

📺 Mira AI

👁️ 8K • 💬 4 • ⏱️ 13:00 • 13h ago

---

**[Ai Bubble Is About To Burst](https://www.youtube.com/watch?v=inPBu71Jh_0)**

we're getting alot of good signs that the ai bubble might burst soon and things will return somewhat to normal. watch me live: ...

📺 Luneist

👁️ 7K • 👍 426 • 💬 122 • ⏱️ 6:23 • 14h ago

---

**[Google AI Studio 2.0 Just Changed Everything!](https://www.youtube.com/watch?v=pl7IO25HPCU)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 13K • 👍 278 • 💬 13 • ⏱️ 8:54 • 2d ago

---

**[Claude AI: Incredible New Way to Make Money Online (Full Tutorial)](https://www.youtube.com/watch?v=48Qg6ZX60r8)**

I show how to use Claude AI to create and sell in-demand, Notion templates online! ▷ Create Incredible Videos and Images with ...

📺 Real Money Strategies

👁️ 20K • 👍 873 • 💬 41 • ⏱️ 19:13 • 2d ago

---

**[AI News: Anthropic Went Crazy This Week!](https://www.youtube.com/watch?v=OYyS0Gu5xj8)**

Here's the AI News you probably missed this week! Check out Genspark here: ...

📺 Matt Wolfe

👁️ 96K • 👍 4K • 💬 292 • ⏱️ 31:53 • 2d ago

---

**[AI vs. Real Things Challenge](https://www.youtube.com/watch?v=Gi3nwC0lkPk)**

Today we're sitting down to see if we can tell what's AI and what's real, the challenge we all face in the big 26. Are we stupid? Is AI ...

📺 Microwave Society

👁️ 42K • 👍 3K • 💬 297 • ⏱️ 11:51 • 1d ago

---

**[A brief update on the AI apocalypse](https://www.youtube.com/watch?v=QtiTjXuZh30)**

Something is definitely happening in the AI world, but how seriously should we take it? Is this another hype cycle or a genuine ...

📺 Vox

👁️ 44K • 👍 1K • 💬 131 • ⏱️ 40:29 • 2d ago

---

**[The AI Collapse is Starting](https://www.youtube.com/watch?v=GSpqX7We5hk)**

OpenAI has just shut down the Sora 2 AI video app. Yes, the great AI desloppening has begun! ARTICLES: ...

📺 SAMTIME

👁️ 199K • 👍 13K • 💬 1K • ⏱️ 2:49 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 280,522 • ❤️ 1,591 • 6d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 2,447 • ❤️ 469 • 2d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 20,049 • ❤️ 467 • 2d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 15,554 • ❤️ 608 • 3d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 518,613 • ❤️ 1,061 • 19d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 466 • ❤️ 249 • 4d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 1,089 • ❤️ 240 • 4h ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 74,832 • ❤️ 405 • 5d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 101,380 • ❤️ 251 • 5d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 27,151 • ❤️ 527 • 17d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 26,941 • 7mo ago

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

▲ 17 • 💬 4 • ⭐ 3,815 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 36 • 💬 5 • ⭐ 1,834 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 10 • 💬 2 • ⭐ 1,335 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 10,585 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 30 • 💬 1 • ⭐ 759 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,883 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 60.8k • 🔱 8.5k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 23.1k • 🔱 1.1k • 3d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.3k • 🔱 731 • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 8.9k • 🔱 737 • 1m ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.5k • 🔱 1.2k • 23h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 5.6k • 🔱 674 • 20m ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 3.8k • 🔱 370 • 1d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

A command-line tool for Lark/Feishu Open Platform — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 3.7k • 🔱 171 • 2h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.3k • 🔱 219 • 15d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.2k • 🔱 106 • 18d ago

---

---

*Generated by PeekDeck - A glance is all you need*
