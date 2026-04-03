---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-03T19:12:06.903465+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 03, 2026 at 19:12 UTC  
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

**[MIT study challenges AI job apocalypse narrative](https://www.reddit.com/r/artificial/comments/1sb7qxc/mit_study_challenges_ai_job_apocalypse_narrative/)**

🔗 [axios.com](https://www.axios.com/2026/04/02/ai-jobs-mit-study-workforce-impact) • 10h ago

---

**[Anyone else feel like AI security is being figured out in production right now?](https://www.reddit.com/r/artificial/comments/1sbgw8y/anyone_else_feel_like_ai_security_is_being/)**

I’ve been digging into AI security incident data from 2025 into this year, and it feels like something isn’t being talked about enough outside security circles. A lot of the issues aren’t advanced attacks. It’s the same pattern we’ve seen with new tech before. Things like prompt injection through external data, agents with too many permissions, or employees using AI tools the company doesn’t even know about. One stat I saw said enterprises are averaging 300+ unsanctioned AI apps, which is kind of wild. The incident data reflects that. Prompt injection is showing up in a large percentage of production deployments. There’s also been a noticeable increase in attacks exploiting basic gaps, partly because AI is making it easier for attackers to find weaknesses faster. Even credential leaks tied to AI usage have been increasing. What stood out to me isn’t just the attacks, it’s the gap underneath it. Only a small portion of companies actually have dedicated AI security teams. In many cases, AI security isn’t even owned by security teams. The tricky part is that traditional security knowledge only gets you part of the way. Some concepts carry over, like input validation or trust boundaries, but the details are different enough that your usual instincts don’t fully apply. Prompt injection isn’t the same as SQL injection. Agent permissions don’t behave like typical API auth. There are frameworks trying to catch up. OWASP now has lists for LLMs and agent-based systems. MITRE ATLAS maps AI-specific attack techniques. NIST has an AI risk framework. The guidance exists, but the number of people who can actually apply it feels limited. I’ve been trying to build that knowledge myself and found that more hands-on learning helps a lot more than just reading docs. Curious how others here are approaching this. If you’re building or working with AI systems, are you thinking about security upfront or mostly dealing with it after things are already live? Sources for those interested: AI Agent Security 2026 Report IBM 2026 X-Force Threat Index Adversa AI Security Incidents Report 2025 Acuvity State of AI Security 2025 OWASP Top 10 for LLM Applications OWASP Top 10 for Agentic AI MITRE ATLAS Framework

3h ago

---

**[AI video generation seems fundamentally more expensive than text, not just less optimized](https://www.reddit.com/r/artificial/comments/1sbk1ue/ai_video_generation_seems_fundamentally_more/)**

There’s been a lot of discussion recently about how expensive AI video generation is compared to text, and it feels like this is more than just an optimization issue. Text models work well because they compress meaning into tokens. Video doesn’t really have an equivalent abstraction yet. Current approaches have to deal with high-dimensional data across many frames, while also keeping objects and motion consistent over time. That makes the problem fundamentally heavier. Instead of predicting the next token, the model is trying to generate something that behaves like a continuous world. The amount of information it has to track and maintain is significantly larger. This shows up directly in cost. More compute per sample, longer inference paths, and stricter consistency requirements all stack up quickly. Even if models improve, that underlying structure does not change easily. It also explains why there is a growing focus on efficiency and representation rather than just pushing output quality. The limitation is not only what the models can generate, but whether they can do it sustainably at scale. At this point, it seems likely that meaningful cost reductions will require a different way of representing video, not just incremental improvements to existing approaches. I’m starting to think we might still be early in how this problem is formulated, rather than just early in model performance.

1h ago

---

**[Why the Reddit Hate of AI?](https://www.reddit.com/r/artificial/comments/1sbgpbf/why_the_reddit_hate_of_ai/)**

I just went through a project where a builder wanted to build a really large building on a small lot next door. The project needed 6 variances from the ZBA. I used ChatGpt and then transitioned to Claude. Essentially I researched zoning laws, variance rules, and deeds. I even uploaded plot plans and engineering designs. In the end I gave my lawyer essentially a complete set of objections for the ZBA hearings and I was able to get all the objections on the record. We won. (Neighborhood support, plus all my research, plus the lawyer) When I described this on another sub, 6-8 downvotes right away. Meanwhile, my lawyer told me I could do this kind of work for money or I could volunteer for the ZBA. (No thanks, I’m near retirement) The tools greatly magnified my understanding and my ability to argue against the builder. (And I caution anyone who uses it to watch out for “unconditional positive regard” (or as my wife says, sycophancy:-). Also to double check everything, ask it to explain terms you don’t understand. Point out inconsistency. In other words, take everything with a grain of salt…

3h ago

---

**[Google releases Gemma 4 models.](https://www.reddit.com/r/artificial/comments/1sapfpu/google_releases_gemma_4_models/)**

1d ago

---

**[Do you guys think in 2030 or 2031 call centers will exist? I mean will call centers be fully automated by 2031?](https://www.reddit.com/r/artificial/comments/1sblrfq/do_you_guys_think_in_2030_or_2031_call_centers/)**

I am curious. I work in a bank call centers and is so boring and repetitive the work i m doing. But also eveythin in my call center is so badly done. We have to do 30 things in one call. Open excell. The system is so slow and eveything is so bady placed. I m curious if AI will do any difference in my job in 2030 or after that.

38m ago

---

**[Microsoft to invest $10 billion in Japan for AI and cyber defence expansion](https://www.reddit.com/r/artificial/comments/1sb65un/microsoft_to_invest_10_billion_in_japan_for_ai/)**

🔗 [reuters.com](https://www.reuters.com/business/media-telecom/microsoft-invest-10-billion-japan-ai-cyber-defence-expansion-2026-04-03/) • 12h ago

---

**[Do AI datacenters being built lead to upgrades to the general power network that help private citizens?](https://www.reddit.com/r/artificial/comments/1sbkjpf/do_ai_datacenters_being_built_lead_to_upgrades_to/)**

As in subject. A lot is being said about power usage, but is the general power net being upgraded to make it more resilient and to somehow balance that out? Thanks.

1h ago

---

**[What happens when you let AI agents run a sitcom 24/7 with zero human involvement](https://www.reddit.com/r/artificial/comments/1sbk7me/what_happens_when_you_let_ai_agents_run_a_sitcom/)**

Ran an experiment — gave AI agents full control over writing, character creation, and performing a sitcom. Left it running nonstop for over a week. Some observations: The quality varies wildly — sometimes genuinely funny, sometimes complete nonsense Characters develop weird recurring quirks that weren't programmed It never gets "tired" but the output quality cycles in waves The pacing is off in ways human writers would never allow Anyone else experimenting with long-running autonomous AI content generation? Curious what others are seeing with extended agent runtimes. Here is an example. https://reddit.com/link/1sbk7me/video/1oupogy2h0tg1/player

1h ago

---

**[After building automation for barbers, therapists, law firms, and game devs/creators I found the setup looks different for each. here's what I got.](https://www.reddit.com/r/artificial/comments/1sbk3lr/after_building_automation_for_barbers_therapists/)**

Real quick on what I actually do. I build automated agent systems for small businesses. Not chatbots. Not "AI will save your business" hype. Actual systems that run specific workflows day to day. Each one takes me about 48-72 hours to set up although im currently working on my largest client and realized how much game i truly do have on this... The interesting part is how different each setup ends up being. The barber doesn't need what the lawyer needs. The therapist's workflow has nothing in common with the game dev's. Here's what I've learned from ACTUALLY installing these things.... AND YES THINGS WENT BAD IN THE BEGINNING MONTHS. The Barber Setup The problem was never cutting hair. It was everything around it. 47 DMs a day about appointments. No-shows not getting followed up with. Instagram posting between clients instead of taking a breather. What I set up: One agent handles booking, rescheduling, and reminders. One agent follows up after each cut and asks for reviews. One agent drafts the weekly social content from photos he snaps on his phone. One agent tracks cash flow and sends weekly summaries. He stopped carrying his phone around within a week. The phone answers itself now. Time saved: 18-22 hours a week. The Therapist Setup This one surprised me. I thought the paperwork would be manageable. It wasn't. Intake forms, insurance verification, session notes, between-session check-ins, cancellation policies. The therapists I worked with were spending more energy on admin than on clients. What I set up: One agent handles intake and insurance verification. One agent drafts session notes from bullet points. The therapist writes three sentences, the agent fills the template. One agent sends check-ins between sessions and flags when someone hasn't shown up. One agent handles cancellation policy enforcement. The cancellation rate dropped because the system does the nudging now, not the therapist. Time saved: 15-20 hours a week. The Law Firm Setup This was the most complex one. Small firm, three attorneys. They were drowning in client updates, deadline tracking, and the constant "did we file that?" panic. What I set up: One agent screens new inquiries and routes them to the right attorney. One agent tracks court dates, filing deadlines, and statute of limitations alerts. One agent drafts client updates and status reports. One agent monitors legal news in their practice areas. Deadlines don't slip anymore. Client updates go out without anyone typing them. They know what's on their desk Monday morning instead of finding out at 4 PM on Friday. Time saved: 20-25 hours a week. The Content Creator Setup This one hit close to home because I've been there. Creating content is fun. Managing the machine around it is not. What I set up: One agent researches trends and competitor content. One agent drafts scripts and outlines from voice notes. One agent handles thumbnails, titles, and posting schedules. One agent tracks analytics and surfaces what's actually working. The creator I built this for now makes content and gets a weekly report on what hit. No more refreshing dashboards every hour. Time saved: 20-30 hours a week. The Game Dev Setup Solo dev. Building a game and a community at the same time. Wasn't working. What I set up: One agent scans Reddit, Twitter, and Discord for community sentiment and bug reports. One agent drafts devlog posts and patch notes from commit messages. One agent manages store page descriptions and milestone announcements. One agent tracks sales, wishlists, and competitor launches. The devlogs write themselves from the commits now. The community gets answered even when he's heads-down in code. Time saved: 15-20 hours a week. What Actually Matters The setup is more important than the agents. I've seen people install five different AI tools and spend three times longer managing those five tools than they save. The difference is whether you build one system with a shared brain, or five tools that don't talk to each other. Every setup I've done follows the same architecture: Shared memory. All agents read and write to the same source of truth. Clear roles. Each agent has one job. No overlap, no stepping on toes. Fallbacks. When one agent can't handle a request, it knows exactly who to pass it to. Monitoring. Someone watches the whole board every morning. Nothing gets lost. The hardest part isn't the AI my brothers i think its just designing the workflow before the agents arrive. That's the piece most people skip. Happy to answer questions about any of these setups or go deeper on the architecture.

1h ago

---

---

## Google News: "ai"

**[How A.I. Helped One Man (and His Brother) Build a $1.8 Billion Company](https://www.nytimes.com/2026/04/02/technology/ai-billion-dollar-company-medvi.html)**

The New York Times • 1d ago

---

**[Economists Are Drawing Stronger Connections Between A.I. and Jobs](https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html)**

The New York Times • 4h ago

---

**[DeepSeek’s New AI Model Will Be a Victory for Huawei](https://www.theinformation.com/articles/deepseeks-new-ai-model-will-victory-huawei)**

When DeepSeek introduces its next-generation model, likely in the next few weeks, it will mark a milestone in China’s yearslong quest for semiconductor self-sufficiency. That’s because the new model, called V4, will be able to run on the latest chips designed by Huawei Technologies. And in ...

The Information • 6h ago

---

**[AI local news network shuts down after plagiarism found](https://www.axios.com/local/richmond/2026/04/03/nota-ai-news-sites-shut-down-plagiarism)**

axios.com • 53m ago

---

**[Trump’s partisan AI pitch stalls on the Hill](https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101)**

Politico • 12m ago

---

**[Steven Spielberg Says 'I Am Not For AI That Replaces A Creative Individual' As Studios And Unions Draw Lines On AI](https://www.yahoo.com/entertainment/movies/articles/steven-spielberg-says-am-not-180108755.html)**

Artificial intelligence should not replace the people behind the story, Oscar-winning director Steven Spielberg said as Hollywood debates AI's limits. "I am not for AI that replaces a creative individ...

Yahoo • 1h ago

---

**[Anthropic’s next model could be a ‘watershed moment’ for cybersecurity. Experts say that could also be a concern](https://www.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity)**

The next wave of AI-powered cybersecurity attacks will be like nothing we’ve seen before.

CNN • 9h ago

---

**[AI will change work. Our history shows that's normal](https://www.npr.org/2026/04/03/nx-s1-5761011/ai-will-change-work-our-history-shows-thats-normal)**

The fear is real: AI may replace millions of jobs. But Robinhood CEO Vlad Tenev argues that we're underestimating how many new opportunities the technology will bring.

NPR • 4h ago

---

**[Facebook removes page after William Shatner blasts 'horrible' AI-generated 'fake news' posts about him](https://ew.com/facebook-removes-page-after-william-shatner-blasts-ai-generated-fake-news-11941868)**

Facebook removed a page containing AI-generated content after William Shatner blasted the 'horrible' posts circulating 'fake news stories' about him.

Entertainment Weekly • 19h ago

---

**[Opinion | AI Is a Threat to Everything the American People Hold Dear](https://www.wsj.com/opinion/ai-is-a-threat-to-everything-the-american-people-hold-dear-a3286459?gaa_at=eafs&gaa_n=AWEtsqfLCej-BlDG2n6cbzqsP_ec2A5wf_r4H8kJq-NUxLbMh1azm8DUL0kS&gaa_ts=69d0146b&gaa_sig=44MOcqS_eHqsyJcToQ-_Lkag6uxGBlIy2Cr1sxvU8Fopd-UpirQ8ZQ7yoZABB5Cx9vS6LXawTZ0e8lG2suYm7A%3D%3D)**

WSJ • 22h ago

---

---

## HackerNews: "ai"

**[Show HN: Apfel – The free AI already on your Mac](https://news.ycombinator.com/item?id=47624645)**

Use Apple's built-in AI from the terminal. No API keys, no cloud, no subscriptions. The LLM is already on your Mac.

⬆️ 566 • 💬 129 • 9h ago • [apfel.franzai.com](https://apfel.franzai.com)

---

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 220 • 💬 117 • 2d ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 105 • 💬 22 • 2d ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 75 • 💬 36 • 1d ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[A $20/month user costs OpenAI $65 in compute. AI video is a money furnace](https://news.ycombinator.com/item?id=47619322)**

⬆️ 73 • 💬 41 • 23h ago • [aedelon777.substack.com](https://aedelon777.substack.com/p/i-did-the-math-on-sora-ai-video-is)

---

**[We replaced RAG with a virtual filesystem for our AI documentation assistant](https://news.ycombinator.com/item?id=47618223)**

We replaced expensive sandboxes with ChromaFs, a virtual filesystem over Chroma, to give our docs AI assistant the ability to explore documentation like a developer would.

⬆️ 73 • 💬 41 • 1d ago • [Mintlify](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 62 • 💬 52 • 2d ago • [Baton](https://getbaton.dev/)

---

**[AI has suddenly become more useful to open-source developers](https://news.ycombinator.com/item?id=47601107)**

More open-source developers are finding that, when used properly, AI can actually help current and long-neglected programs. However, legal and quality issues loom.

⬆️ 54 • 💬 46 • 2d ago • [ZDNET](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

---

**[Men are ditching TV for YouTube as AI usage and social media fatigue grow](https://news.ycombinator.com/item?id=47612127)**

⬆️ 46 • 💬 125 • 1d ago • [ofcom.org.uk](https://www.ofcom.org.uk/media-use-and-attitudes/media-habits-adults/passive-social-media-use-ai-companionship-and-online-side-hustles-uk-adults-media-and-online-lives-revealed)

---

**[Group Pushing Age Verification for AI Turns Out to Be Backed by OpenAI](https://news.ycombinator.com/item?id=47616665)**

It gave the leader of a nonprofit involved with it "a very grimy feeling."

⬆️ 46 • 💬 4 • 1d ago • [Gizmodo](https://gizmodo.com/group-pushing-age-verification-requirements-for-ai-turns-out-to-be-sneakily-backed-by-openai-2000741069)

---

---

## YouTube Videos: "ai"

**[HUGE JOB LOSSES ARE COMING- AI HAS HIT THE DEBT WALL AND PEOPLE WILL GO](https://www.youtube.com/watch?v=RNkDJ9kULbs)**

AI isn't paying for itself. It's being financed with massive debt. And right now — that funding is coming from layoffs, rising debt, and ...

📺 Ox Talks

👁️ 11K • 👍 1K • 💬 188 • ⏱️ 8:02 • 1d ago

---

**[Anthropic&#39;s New Claude CONWAY Is Unlike Any AI Before](https://www.youtube.com/watch?v=x2l7W9aTc5k)**

Anthropic is testing Claude Conway, a strange new AI system that looks less like a chatbot and more like a persistent agent ...

📺 AI Revolution

👁️ 49K • 👍 869 • 💬 67 • ⏱️ 10:50 • 21h ago

---

**[The AI crisis no one is talking about](https://www.youtube.com/watch?v=ZcH5C8Jlltc)**

Asking ChatGPT about pi was the worst mistake he ever made. Become a member on YouTube: ...

📺 Mo Bitar

👁️ 44K • 👍 4K • 💬 843 • ⏱️ 6:33 • 7h ago

---

**[AI BUSINESS SUMMIT 2026 - DAY 3](https://www.youtube.com/watch?v=TLtNyRUFbFE)**

Facebook Fan Page: https://www.facebook.com/alicialyttlelive Twitter: https://twitter.com/alicialyttle Instagram: ...

📺 Alicia Lyttle

👁️ 3K • 👍 222 • 2d ago

---

**[I Tested An AI Car](https://www.youtube.com/watch?v=K4kLiat84eE)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 40K • 👍 4K • 💬 107 • ⏱️ 0:53 • 1h ago

---

**[How We Would Teach AI From Scratch in 2026](https://www.youtube.com/watch?v=QbFU0UNMVaU)**

Most people are still using ChatGPT the way they used Google in 2005: type a question, get an answer, close the tab. In 2026 ...

📺 The Neuron

👁️ 3K • 👍 151 • 💬 10 • ⏱️ 2:23:24 • 23h ago

---

**[Claude Mythos Changes Everything. Your AI Stack Isn&#39;t Ready.](https://www.youtube.com/watch?v=hV5_XSEBZNg)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 104K • 👍 3K • 💬 397 • ⏱️ 31:21 • 2d ago

---

**[AI BUBBLE POP?: HALF Of Datacenters Delayed/Canceled](https://www.youtube.com/watch?v=pkomxsk5hpY)**

Krystal and Saagar discuss the AI bubble imploding. Sign up for a PREMIUM Breaking Points subscriptions for full early access to ...

📺 Breaking Points

👁️ 293K • 👍 9K • 💬 1K • ⏱️ 13:15 • 1d ago

---

**[Don’t Buy a New Computer in 2026! (Even for AI Use – Here’s Why)](https://www.youtube.com/watch?v=moTUpGoxcmc)**

New changes in technology like the fast pace of AI adoption and AI agents are triggering us to think of buying a new computer.

📺 Rob Braxman Tech

👁️ 140K • 👍 9K • 💬 1K • ⏱️ 20:47 • 2d ago

---

**[Google’s New AI Just Broke My Brain](https://www.youtube.com/watch?v=7YVrb3-ABYE)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The TurboQuant paper is available here: ...

📺 Two Minute Papers

👁️ 129K • 👍 9K • 💬 890 • ⏱️ 8:34 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 487,446 • ❤️ 2,202 • 10d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 76,200 • ❤️ 624 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 84,600 • ❤️ 759 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 26,980 • ❤️ 856 • 8d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 26,164 • ❤️ 354 • 3d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 4,760 • ❤️ 644 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 227,053 • ❤️ 486 • 9d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 24,366 • ❤️ 279 • 1d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 700,218 • ❤️ 940 • 1mo ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 23,460 • ❤️ 235 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 149 • 💬 7 • ⭐ 35,575 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 18 • 💬 1 • ⭐ 13,860 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 35 • 💬 2 • ⭐ 46,417 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 11 • 💬 1 • ⭐ 167 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 73 • 💬 2 • ⭐ 104 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,819 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 22,888 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 22,894 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 4,616 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 37 • 💬 2 • ⭐ 31,788 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 64.9k • 🔱 9.2k • 8d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 15.0k • 🔱 828 • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 12.5k • 🔱 1.1k • 1h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.4k • 🔱 1.3k • 2h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.2k • 🔱 947 • 4d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.5k • 🔱 365 • 5h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 4.9k • 🔱 1.5k • 1d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.5k • 🔱 432 • 3d ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.6k • 🔱 622 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 229 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
