---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-06T14:49:11.396780+00:00'
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

**Last Updated:** April 06, 2026 at 14:49 UTC  
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

**[I have been coding for 11 years and I caught myself completely unable to debug a problem without AI assistance last month. That scared me more than anything I have seen in this industry.](https://www.reddit.com/r/artificial/comments/1sderg4/i_have_been_coding_for_11_years_and_i_caught/)**

I want to be honest about something that happened to me because I think it is more common than people admit. Last month I hit a bug in a service I wrote myself two years ago. Network timeout issue, intermittent, only in prod. The kind of thing I used to be able to sit with for an hour and work through methodically. I opened Claude, described the symptom, got a hypothesis, followed it, hit a dead end, fed that back, got another hypothesis. Forty minutes later I had not found the bug. I had just been following suggestions. At some point I closed the chat and tried to work through it myself. And I realized I had forgotten how to just sit with a problem. My instinct was to describe it to something else and wait for a direction. The internal monologue that used to generate hypotheses, that voice that says maybe check the connection pool, maybe it is a timeout on the load balancer side, maybe there is a retry storm. That voice was quieter than it used to be. I found the bug eventually. It took me longer without AI than it would have taken me three years ago without AI. I am not saying the tools are bad. I use them every day and they make me faster on most things. But there is something specific happening to the part of the brain that generates hypotheses under uncertainty. That muscle atrophies if you do not use it. The analogy I keep coming back to is GPS. You can navigate anywhere with GPS. But if you use it for five years and then lose signal, you do not just lack information. You lack the mental map that you would have built if you had been navigating manually. The skill and the mental model degrade together. I am 11 years into this career. I started noticing this in myself. I wonder how it looks for someone who started using AI tools in their first year. Has anyone else noticed this? Not the productivity gains, we all know those. The quieter thing underneath.

17h ago

---

**[AI machine sorts clothes faster than humans to boost textile recycling in China](https://www.reddit.com/r/artificial/comments/1sdwgvg/ai_machine_sorts_clothes_faster_than_humans_to/)**

A company in eastern China is using an artificial intelligence-powered machine to sort clothes and boost recycling.

🔗 [AP News](https://apnews.com/article/china-recycling-textiles-artificial-intelligence-863551cc54e88da6a7916894cb8980c4) • 3h ago

---

**[You can now give an AI agent its own email, phone number, wallet, computer, and voice. This is what the stack looks like](https://www.reddit.com/r/artificial/comments/1sdiugx/you_can_now_give_an_ai_agent_its_own_email_phone/)**

I’ve been tracking the companies building primitives specifically for agents rather than humans. The pattern is becoming obvious: every capability a human employee takes for granted is getting rebuilt as an API. Here are some of the companies building for AI agents: AgentMail — agents can have email accounts AgentPhone — agents can have phone numbers Kapso — agents can have WhatsApp numbers Daytona / E2B — agents can have their own computers monid.ai — agents can read social media (X, TikTok, Reddit, LinkedIn, Amazon, Facebook) Browserbase / Browser Use / Hyperbrowser — agents can use web browsers Firecrawl — agents can crawl the web without a browser Mem0 — agents can remember things Kite / Sponge — agents can pay for things Composio — agents can use your SaaS tools Orthogonal — agents can access APIs more easily ElevenLabs / Vapi — agents can have a voice Sixtyfour — agents can search for people and companies Exa — agents can search the web (Google isn’t built for agents) What’s interesting is how quickly this came together. Not long ago, none of this really existed in a usable form. Now you can piece together an agent with identity, memory, communication, and spending in a single afternoon. Feels less like “AI tools” and more like the early version of an agent-native infrastructure stack. Curious if anyone here is actually building on top of this. What are you using? Also probably missing a bunch - drop anything I should add and I’ll keep this updated.

15h ago

---

**[McKinsey's AI Lie Explains What's Happening to Work](https://www.reddit.com/r/artificial/comments/1sd90xu/mckinseys_ai_lie_explains_whats_happening_to_work/)**

Everyone thinks McKinsey just built 25,000 AI experts. They didn't. They took a 35-year-old internal database, put a natural language interface on top, and wrote a press release that every major business publication ran without asking a single follow-up question. This is the same play McKinsey has run for a hundred years. ERP in the 90s. Digital transformation in the 2000s. Big data in the 2010s. Each wave the same: new technology creates executive anxiety, McKinsey positions itself between that anxiety and the answer, and companies buy the trend to protect themselves when it fails. The future looks a lot like the past. And once you see it, you can't unsee it. https://www.youtube.com/watch?v=uTdKJaQkgJQ

21h ago

---

**[I built an AI content engine that turns one piece of content into posts for 9 platforms — fully automated with n8n](https://www.reddit.com/r/artificial/comments/1sdyvew/i_built_an_ai_content_engine_that_turns_one_piece/)**

What it does: You give it any input — a blog URL, a YouTube video, raw text, or just a topic — and it generates optimized posts for 9 platforms at once: Instagram, Twitter/X, LinkedIn, Facebook, TikTok, Reddit, Pinterest, Twitter threads, and email newsletters. Each output is tailored to the platform (hashtags for IG, hooks for TikTok, professional tone for LinkedIn, etc.). It also auto-generates images for visual platforms like Instagram, Facebook, and Pinterest,using AI. Other features: - Topic Research — scans Google, Reddit, YouTube, and news sources, then uses an LLM to identify trending subtopics before generating content - Auto-Discover — if you don't even have a topic, it searches what's trending right now (optionally filtered by niche) and picks the hottest one - Cinematic Ad — upload any photo, pick a style (cinematic, luxury, neon, retro, minimal, natural), and Gemini transforms it into a professional-looking ad - Multi-LLM support — works with Mistral, Groq, OpenAI, Anthropic, and Gemini - History — every generation is saved, exportable as CSV The n8n automation (this is where it gets fun): I connected the whole thing to an n8n workflow so it runs on autopilot: 1. Schedule Trigger — fires daily (or whatever frequency) 2. Google Sheets — reads a row with a topic (or "auto" to let AI pick a trending topic) 3. HTTP Request — hits my /api/auto-generate endpoint, which auto-detects the input type (URL, YouTube link, topic, or "auto") and generates everything 4. Code node — parses the response and extracts each platform's content 5. Google Drive — uploads generated images 6. Update Sheets — marks the row as done with status and links The API handles niche filtering too — so if my sheet says the topic is "auto" and the niche column says "AI", it'll specifically find trending AI topics instead of random viral stuff. Error handling: HTTP Request has retry on fail (2 retries), error outputs route to a separate branch that marks the sheet row as "failed" with the error message, and a global error workflow emails me if anything breaks. Tech stack: - FastAPI backend, vanilla JS frontend - Hosted on Railway - Google Gemini for image generation and cinematic ads - HuggingFace FLUX.1 for platform images - SerpAPI + Reddit + YouTube + NewsAPI for research - SQLite for history - n8n for workflow automation It's not perfect yet — rate limits on free tiers are real — but it's been saving me hours every week. Happy to answer questions. https://preview.redd.it/f8d3ogk3nktg1.png?width=888&format=png&auto=webp&s=dcd3d5e90facd54314f40e799b32cab979dae4bf https://preview.redd.it/j8zl07llmktg1.png?width=946&format=png&auto=webp&s=5c78c12a223d6357cccaed59371e97d5fe4787f5 https://preview.redd.it/5cjas6hkmktg1.png?width=891&format=png&auto=webp&s=288c6964061f531af63fb9717652bececfb63072 https://preview.redd.it/k7e89belmktg1.png?width=1057&format=png&auto=webp&s=8b6cb15cfa267d90a697ba03aed848166976d921 https://preview.redd.it/3w3l70tlmktg1.png?width=1794&format=png&auto=webp&s=6de10434f588b1bf16ae02f542afd770eaa23c3f https://preview.redd.it/a40rh1canktg1.png?width=1920&format=png&auto=webp&s=1d2414c7e653a5f01f12a21a43e69bd4fb4b99ed

1h ago

---

**[Opinions on Google’s search AI? Best practices?](https://www.reddit.com/r/artificial/comments/1sdt5jn/opinions_on_googles_search_ai_best_practices/)**

Hello! I tend to use it often and I find it to have valid information when it comes to linguistic or computer related summaries, though it does require a play of words at times. I’m wondering what this Google search AI is good at, what it’s bad at, your opinions on it (especially for learning various topics or getting information, any subject you think it’s good or bad at). What are your opinions for using it for political information? How are your best practices in verifying the validity of the information?? Literally, anything you have to say about it, yap about it in the comments. I use it all the time and it’s the only AI I use explicitly (usually after making a google search and it showing up at the top of my screen every time), besides some of the advanced (non image creation AI) AI parts of Photoshop, such as removing backgrounds. Or any better alternatives out there, or opinions on other AI platforms (free ones mostly), thanks!

6h ago

---

**[Last Call: Perplexity, Replit, & GitHub— The AI Student Discounts You're Cheerfully Paying the Tourist Price For](https://www.reddit.com/r/artificial/comments/1sdzcag/last_call_perplexity_replit_github_the_ai_student/)**

If you got a student edu email, these official promos will expire soon.

1h ago

---

**[Japan is adopting robotics and physical AI, with a model where startups innovate and corporations provide scale](https://www.reddit.com/r/artificial/comments/1sdx5ih/japan_is_adopting_robotics_and_physical_ai_with_a/)**

Physical AI is emerging as one of the next major industrial battlegrounds, with Japan’s push driven more by necessity than anything else. With workforces shrinking and pressure mounting to sustain productivity, companies are increasingly deploying AI-powered robots across factories, warehouses, and critical infrastructure.

🔗 [TechCrunch](https://techcrunch.com/2026/04/05/japan-is-proving-experimental-physical-ai-is-ready-for-the-real-world/) • 2h ago

---

**[mining hardware doing AI training - is the output actually useful](https://www.reddit.com/r/artificial/comments/1sdvygv/mining_hardware_doing_ai_training_is_the_output/)**

there's this network that launched recently routing crypto mining hardware toward AI training workloads. miners seem happy with the economics but that's not what i care about my question: is the AI output actually useful? running hardware is easy, producing valuable compute is hard. saw they had some audit confirming high throughput but throughput alone doesn't tell you about quality nobody independent has verified the training output yet afaik. that's the gap that matters. has anyone here looked at how you'd even verify something like that? seems like you'd need to compare against known benchmarks or something

3h ago

---

**[Rate My README.md](https://www.reddit.com/r/artificial/comments/1sdr3is/rate_my_readmemd/)**

Working on my README.md to make it more accessiable and understood without make it to long. still working through it. project is still under development also. getting closer every day. feedback is much appreciated, Its my first public repo. https://github.com/AIOSAI/AIPass/blob/main/README.md

8h ago

---

---

## Google News: "ai"

**[Brands Adopt ‘No AI’ Disclaimers to Stand Out Amid the Slop](https://www.wsj.com/cmo-today/brands-adopt-no-ai-disclaimers-to-stand-out-amid-the-slop-a92352af?gaa_at=eafs&gaa_n=AWEtsqf73YLP1YIQwow0eGXfZFs__pSGP_CyByS5GIY46m0oJnlqKVbtdWNb&gaa_ts=69d3bdec&gaa_sig=-VbdPnpjJMGkijg7aaW6cD7mDrFbh78moz4vEsH-AlDWkjB-QmojsY6nZi4ph-_v9d00EWE7_xNEDaTtt6Xy3g%3D%3D)**

WSJ • 4h ago

---

**[Chinese AI helping Iran target US forces with 'incredible precision'](https://www.abc.net.au/news/2026-04-06/chinese-satellite-intelligence-helping-iran-target-us-forces/106535420)**

Chinese satellite images enhanced by artificial intelligence could help Iran target US and allied forces to within a third of a square metre, military analysts say.

Australian Broadcasting Corporation • 6h ago

---

**[Datavault AI CEO Nathaniel T. Bradley to Deliver Flagship Keynotes on Breakthrough RWA Tokenization at CONV3RGENCE London and AssetRush × Zurich 2026](https://ir.datavaultsite.com/news-events/press-releases/detail/444/datavault-ai-ceo-nathaniel-t-bradley-to-deliver-flagship)**

Building Global Momentum Ahead of Upcoming XRP Tokyo Event PHILADELPHIA, PA / ACCESS Newswire / April 6, 2026 / Datavault AI Inc. ("Datavault AI"…...

Datavault AI • 1h ago

---

**[Regulators Propose Audit-Ready Controls to Govern AI](https://www.pymnts.com/artificial-intelligence-2/2026/regulators-propose-audit-ready-controls-to-govern-ai/)**

Banks and payments companies have spent the past few years embedding artificial intelligence into their core operations. They’ve been running fraud

PYMNTS.com • 1h ago

---

**[Teradyne's Easy Gains Behind Us - AI/Robotics Winner Expensive Here (NASDAQ:TER)](https://seekingalpha.com/article/4888628-teradynes-stock-easy-gains-behind-us-airobotics-winner-expensive-here)**

Teradyne’s robust growth is fueled by partnerships with TSM and exposure to AI networking, compute, and memory chips. Learn more on TER stock here.

Seeking Alpha • 1h ago

---

**[Forget the A.I. Apocalypse. Memes Have Already Nuked Our Culture.](https://www.nytimes.com/2026/04/06/magazine/ai-apocalypse-brain-rot-memes.html)**

The New York Times • 5h ago

---

**[Behind the Curtain: Sam's superintelligence New Deal](https://www.axios.com/2026/04/06/behind-the-curtain-sams-superintelligence-new-deal)**

Axios • 5h ago

---

**[OpenClaw: What China's frenzy says about its AI ambition](https://www.bbc.com/news/articles/cy41n17e23go)**

The AI agent sparked a frenzy of "raising lobsters" in March, with users training the tool to suit their needs.

BBC • 16h ago

---

**[JPMorgan CEO Jamie Dimon in annual letter cites risks in geopolitics, AI and private markets](https://www.cnbc.com/2026/04/06/jpmorgan-ceo-jamie-dimon-annual-letter-risks.html)**

JPMorgan CEO Jamie Dimon in his annual letter to shareholders noted the country's 250th anniversary and called for a broad recommitment to American ideals.

CNBC • 4h ago

---

**[Iran threat puts OpenAI’s $30B Stargate AI project in crosshairs (OPENAI:Private)](https://seekingalpha.com/news/4572585-iran-threat-puts-openais-30b-stargate-ai-project-in-crosshairs)**

Iran's Islamic Revolutionary Guard Corps spokesperson released a video on April 3 threatening "complete and utter annihilation" of U.S. and Israeli facilities, naming the planned $30B Stargate AI data center in Abu Dhabi as a potential target.

Seeking Alpha • 4h ago

---

---

## HackerNews: "ai"

**[Eight years of wanting, three months of building with AI](https://news.ycombinator.com/item?id=47648828)**

For eight years, I’ve wanted a high-quality set of devtools for working with SQLite. Given how important SQLite is to the industry1, I’ve long been puzzled that no one has invested in building a really good developer experience for it2.
A couple of weeks ago, after ~250 hours of effort over three months3 on evenings, weekends, and vacation days, I finally released syntaqlite (GitHub), fulfilling this long-held wish. And I believe the main reason this happened was because of AI coding agents4.
Of course, there’s no shortage of posts claiming that AI one-shot their project or pushing back and declaring that AI is all slop. I’m going to take a very different approach and, instead, systematically break down my experience building syntaqlite with AI, both where it helped and where it was detrimental.
I’ll do this while contextualizing the project and my background so you can independently assess how generalizable this experience was. And whenever I make a claim, I’ll try to back it up with evidence from my project journal, coding transcripts, or commit history5.

⬆️ 838 • 💬 262 • 1d ago • [Lalit Maganti](https://lalitm.com/post/building-syntaqlite-ai/)

---

**[Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B](https://news.ycombinator.com/item?id=47652007)**

On-device, real-time multimodal AI. Have natural voice and vision conversations with an AI that runs entirely on your machine. Powered by Gemma 4 E2B and Kokoro. - fikrikarim/parlor

⬆️ 161 • 💬 13 • 20h ago • [GitHub](https://github.com/fikrikarim/parlor)

---

**[12k AI-generated blog posts added in a single commit](https://news.ycombinator.com/item?id=47640722)**

…k/Ceph, and Dapr

Complete all topics from Todo.md including SQL functions, configuration guides,
troubleshooting runbooks, architecture comparisons, SDK tutorials, and operator
deployment pattern...

⬆️ 154 • 💬 147 • 1d ago • [GitHub](https://github.com/OneUptime/blog/commit/30cd2384794c897d95aca77d173db44af51ca849)

---

**[Musician says AI company is cloning her music, filing claims against her](https://news.ycombinator.com/item?id=47653471)**

⬆️ 114 • 💬 19 • 18h ago • [X (formerly Twitter)](https://twitter.com/unlimited_ls/status/2040577536136974444)

---

**[Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud](https://news.ycombinator.com/item?id=47655367)**

Gemma Gem runs Google's Gemma 4 model entirely on-device via WebGPU — no API keys, no cloud, no data leaving your machine. - kessler/gemma-gem

⬆️ 108 • 💬 17 • 14h ago • [GitHub](https://github.com/kessler/gemma-gem)

---

**["Cognitive surrender" leads AI users to abandon logical thinking, research finds](https://news.ycombinator.com/item?id=47632504)**

Experiments show large majorities uncritically accepting "faulty" AI answers.

⬆️ 98 • 💬 42 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/04/research-finds-ai-users-scarily-willing-to-surrender-their-cognition-to-llms/)

---

**[Show HN: Travel Hacking Toolkit – Points search and trip planning with AI](https://news.ycombinator.com/item?id=47635033)**

AI-powered travel hacking with points, miles, and award flights. Drop-in skills and MCP servers for OpenCode and Claude Code. - borski/travel-hacking-toolkit

⬆️ 95 • 💬 39 • 2d ago • [GitHub](https://github.com/borski/travel-hacking-toolkit)

---

**[Writing Lisp is AI resistant and I'm sad](https://news.ycombinator.com/item?id=47645468)**

⬆️ 93 • 💬 95 • 1d ago • [blog.djhaskin.com](https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/)

---

**[AI that copied musical artist files copyright claim against artist [updated]](https://news.ycombinator.com/item?id=47645976)**

⬆️ 64 • 💬 17 • 1d ago • [X (formerly Twitter)](https://twitter.com/VladTheInflator/status/2039577001531768906)

---

**[I used AI. It worked. I hated it](https://news.ycombinator.com/item?id=47646277)**

I used Claude Code to build a tool I needed. It worked great, but I was miserable. I need to reckon with what it means.

⬆️ 54 • 💬 120 • 1d ago • [taggart-tech.com](https://taggart-tech.com/reckoning/)

---

---

## YouTube Videos: "ai"

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 3K • 👍 147 • 💬 5 • ⏱️ 16:42 • 15h ago

---

**[AI just tried to take our jobs. It failed.](https://www.youtube.com/watch?v=p22QeLNHvlc)**

You're absolutely right, jail does sound pretty awful! https://x.com/atmoio/status/2040797533568434350 ...

📺 Mo Bitar

👁️ 15K • 👍 2K • 💬 384 • ⏱️ 5:39 • 3h ago

---

**[AI News: Anthropic Leak Shows Us The Future of AI](https://www.youtube.com/watch?v=BZ1hs2ZcnJc)**

Here's the AI News you probably missed this week. Try Recraft V4 now and experience an image generation model with ...

📺 Matt Wolfe

👁️ 81K • 👍 3K • 💬 246 • ⏱️ 31:05 • 2d ago

---

**[REPORT THIS VIDEO: AI is ruining youtube](https://www.youtube.com/watch?v=Ku3OMJsLzwU)**

garbage video: https://www.youtube.com/watch?v=huXOoaPWDQ0 https://youtu.be/6uKZ84zwJI0 https://youtu.be/iwc5HKnOmGg ...

📺 Louis Rossmann

👁️ 106K • 👍 12K • 💬 2K • ⏱️ 9:39 • 17h ago

---

**[The AI Bubble Is Getting Worse Faster Than Expected...](https://www.youtube.com/watch?v=HrfAHSUSMJA)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be serious pressure faced by the ...

📺 SomeOrdinaryGamers

👁️ 357K • 👍 15K • 💬 2K • ⏱️ 20:44 • 1d ago

---

**[Why do fascists love AI slop?](https://www.youtube.com/watch?v=QF2PYUPkvlo)**

Why do right-wing people love AI slop? AI is the perfect tool for a movement that needs you to stop thinking. // Ad-Free Videos ...

📺 Caelan Conrad

👁️ 74K • 👍 8K • 💬 1K • ⏱️ 37:34 • 1d ago

---

**[TIMMY Gets all the BADDIES 😂 (OMEGLE AI FACE TROLLING)](https://www.youtube.com/watch?v=I6EV7aw7cgY)**

Trolling & Rizzing The Cutest Girls ON OMEGLE. Live Stream: https://kick.com/jerqo ---Socials--- Instagram: ...

📺 JerqoBeats

👁️ 8K • 👍 521 • 💬 30 • ⏱️ 19:06 • 16h ago

---

**[ai se video kaise banaye | ai video kaise banaye | ai se cartoon video kaise banaye | ai video](https://www.youtube.com/watch?v=EoOGovixMIw)**

ai se video kaise banaye | ai video kaise banaye | ai se cartoon video kaise banaye | ai video Audiance Searching ai video kaise ...

📺 Arvind zone

👁️ 44K • 👍 1K • 💬 361 • ⏱️ 10:40 • 2d ago

---

**[Quantum AI](https://www.youtube.com/watch?v=JIkVDfOekB8)**

📺 Ben Goertzel

👁️ 9K • 👍 453 • 💬 153 • ⏱️ 9:35 • 1d ago

---

**[Gemma 4 on the iPhone (local AI, no internet required)](https://www.youtube.com/watch?v=d0gTthacB5c)**

Gemma 4 running on my iPhone works without internet, is blazing fast and can translate Japanese from a pill bottle. Local AI ...

📺 NetworkChuck

👁️ 172K • 👍 10K • 💬 307 • ⏱️ 2:03 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 678,740 • ❤️ 1,086 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 548,344 • ❤️ 2,377 • 12h ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 45,185 • ❤️ 450 • 7h ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 476,612 • ❤️ 434 • 4d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 425 • 3d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`text-generation` `6.4B`

⬇️ 13,727 • ❤️ 405 • 2d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 38,388 • ❤️ 1,014 • 11d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 321,152 • ❤️ 382 • 4d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 128,326 • ❤️ 811 • 3d ago

---

**[gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)**

*Google*

Gemma 4 E2B-it is an instruction-tuned, multimodal (text, image, audio) LLM from Google DeepMind, featuring a 128K context window and efficient Dense architecture. It excels at reasoning, coding, and agentic tasks, optimized for on-device deployment.

`any-to-any` `5.1B`

⬇️ 237,266 • ❤️ 271 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 153 • 💬 7 • ⭐ 36,530 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 20 • 💬 1 • ⭐ 15,006 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 36 • 💬 2 • ⭐ 47,672 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 33 • 💬 5 • ⭐ 657 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 32,322 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[DeepScientist: Advancing Frontier-Pushing Scientific Findings
  Progressively](https://huggingface.co/papers/2509.26603)**

*Yixuan Weng, Minjun Zhu, Qiujie Xie et al. (7 authors)*

🏢 Text Intelligence Lab of Westlake University

DeepScientist autonomously conducts scientific discovery through Bayesian Optimization, surpassing human state-of-the-art methods on multiple AI tasks.

▲ 18 • 💬 4 • ⭐ 1,540 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.26603) • [💻 code](https://github.com/ResearAI/DeepScientist) • [🔗 project](https://ai-researcher.net)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 5,001 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 88 • 💬 4 • ⭐ 373 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,939 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 50 • 💬 1 • ⭐ 75,421 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 15.2k • 🔱 853 • 6d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 13.6k • 🔱 1.2k • 7h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.5k • 🔱 1.3k • 2d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.9k • 🔱 1.0k • 7d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`Go` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 7.6k • 🔱 1.3k • 7h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.8k • 🔱 402 • 2h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.2k • 🔱 1.6k • 2d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.7k • 🔱 458 • 6d ago

---

**[Narcooo/inkos](https://github.com/Narcooo/inkos)**

Autonomous novel writing CLI AI Agent — agents write, audit, and revise novels with human review gates

`TypeScript` `agent` `ai` `ai-agent` `ai-novel` `ai-writing`

⭐ 3.6k • 🔱 654 • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 3.5k • 🔱 785 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*
