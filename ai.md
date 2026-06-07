---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-07T13:03:22.402512+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 07, 2026 at 13:03 UTC  
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

**[I got tired of Al making stuff up about my PDFs, so I built something that actually cites its sources](https://www.reddit.com/r/artificial/comments/1tzaylp/i_got_tired_of_al_making_stuff_up_about_my_pdfs/)**

so i kept using chatgpt to ask questions about my pdfs and notes, and half the time i couldn't tell if it actually read the doc or just made something up that sounded right. that bugged me enough to build my own thing over the last few weeks. you upload a pdf (or word, csv, image, or just paste a link), ask whatever you want, and it answers using only what's in your file - and it shows the exact page it pulled the answer from, so you can check. if the answer isn't in the doc, it just tells you instead of guessing. stuff i actually end up using: flip on web search when i want it to look something up online instead one click to turn a doc into a summary / key points / flashcards (this is clutch for studying) resume review + cover letter help you can talk to it and it reads the answer back it's completely free, i'm not selling anything. honestly just want people to break it and tell me what's missing. link: https://athena-wisdom.vercel.app (there's a short guide on the site too if you get stuck) solo project so be gentle lol - but real feedback is what i'm after, especially what you'd want it to do next.

28m ago

---

**[AI keeps getting blamed for tech layoffs, but the numbers don't really line up](https://www.reddit.com/r/artificial/comments/1tyq91e/ai_keeps_getting_blamed_for_tech_layoffs_but_the/)**

I keep seeing "AI took these jobs" every time a company does layoffs, and I'm not convinced it's the main driver. A few things I keep coming back to. The industry cut around 122,500 jobs in 2025, down from about 153,000 in 2024. AI was named as a direct reason in fewer than 8% of those announcements. So for the other 90 percent plus, something else was going on. Actual AI adoption inside companies is also lower than the marketing suggests. Full org-wide rollout is still in the single digits in the surveys I've seen. Plenty of teams have a ChatGPT subscription and call themselves "AI-driven", but that is not the same as AI doing real work in the pipeline. My read: AI usually isn't replacing people directly. Managers see devs shipping more code and assume they can cut headcount, and companies are moving tight budgets toward expensive AI infra and tooling. But coding is a small part of the job, so "more code per dev = fewer devs" rarely holds up. I don't think AI is taking most jobs. I think it's adding pressure to a market that was already rough for other reasons (economy, over-hiring in 2021-2022, investor expectations). For people who work in eng or hiring: when you've seen layoffs up close, how often was AI genuinely the reason versus the convenient public explanation?

17h ago

---

**[Benefits and Risks of AI at Harvard Class Day 2026](https://www.reddit.com/r/artificial/comments/1ty7pt5/benefits_and_risks_of_ai_at_harvard_class_day_2026/)**

1d ago

---

**[Does anyone else say please and thank you to AI? Or am I just wierd?](https://www.reddit.com/r/artificial/comments/1tylcl1/does_anyone_else_say_please_and_thank_you_to_ai/)**

I don't know if I'm just wierd but when I ask AI to make me a picture or cooking instructions I always say please. I can't be the only one..

20h ago

---

**[the more i use multiple models, the more i think "AI consensus" is a trap — the disagreement is the only part worth paying attention to](https://www.reddit.com/r/artificial/comments/1tymxz2/the_more_i_use_multiple_models_the_more_i_think/)**

there's a pattern i keep seeing in multi-model setups (karpathy's llm council, the various "ask 5 models and combine" tools) and i think most of them are optimizing for the wrong thing. they treat agreement as the goal. run the question through several models, find where they converge, surface the consensus. but in my experience the consensus is the least useful output. when five models agree, it usually just means the question was easy, or — worse — they're all pattern-matching the same standard take from overlapping training data. agreement can be a sign of shared blind spots, not correctness. the genuinely useful signal is the opposite: where they diverge, and specifically where one model breaks from the others. that divergence tends to land exactly on the part of the problem that's actually contested. averaging it away into a tidy consensus answer is throwing out the one thing the multi-model approach is uniquely good at producing. which makes me think the design goal for these systems is backwards. you don't want a machine that manufactures agreement. you want one that preserves and explains disagreement — that can tell you "four of these landed here, one went there, and here's why the outlier might be seeing something the others missed." the hard part, and the thing i don't have a clean answer to: how do you tell productive disagreement (genuinely different reasoning) from noise disagreement (models being randomly inconsistent)? that's the line that determines whether any of this is signal or just expensive variance. curious what people working on multi-agent or ensemble setups think. is consensus the wrong target? and how would you separate real divergence from noise?

19h ago

---

**[Best AI PowerPoint maker for people who already have content?](https://www.reddit.com/r/artificial/comments/1tz68q4/best_ai_powerpoint_maker_for_people_who_already/)**

Most recommendations I’m seeing are for generating presentations from a topic, but I already HAVE the content. Problem is it’s usually: messy notes meeting transcripts random docs giant walls of text Main thing I want is help turning all of that into slides that are actually readable. Does anything handle that well right now?

4h ago

---

**[this just isn't sustainable.](https://www.reddit.com/r/artificial/comments/1tzb82n/this_just_isnt_sustainable/)**

I had a work version of GPT do a very simple spreadsheet summary task for me yesterday. It took it 5 minutes to do it. I could probably have done it myself in 30 or so minutes. The heavily subsidised token cost of that task? 10 dollars. That's with a 10x subsidy. The actual compute cost was about 100 dollars. There's something seriously wrong there. It's going to crash and crash HARD. if people think i'm lying or are just interested. The spreadsheet had 45 sheets. Each sheet had roughly 500 x 50 populated cells. Formatting was not exactly standard across all sheets. The prompt was something like "there is labelled column in each sheet, give me a simple list of all the items from all the sheets in that column and ignore duplicates." We can chose which model to use. The model I chose was one of the newer ones, I honestly can't remember which one, possibly GPT 5.5. It took 5 minutes or more to so and the stated cost for the task was 10 dollars, possibly even more. I can't recall the token amount.

16m ago

---

**[How I built an AI email agent that processes 15,000 hotel guest emails per day. full architecture breakdown](https://www.reddit.com/r/artificial/comments/1tz8vm2/how_i_built_an_ai_email_agent_that_processes/)**

Just shipped this project and wanted to share the full technical breakdown because hotel/hospitality AI doesn't get much attention compared to the usual chatbot and SaaS use cases. The client manages 500 hotel properties. Their support team was manually handling around 15,000 guest emails per day. Same questions over and over across hundreds of hotels but each one still needed a human to read it, understand it, find the answer, and reply. Here's how the system works end to end: Layer 1: Email ingestion and question extraction This was the hardest part. Guest emails are messy. A typical one looks like: "Hi there, we're coming for our anniversary on the 20th and I was wondering if you have any room upgrades available. Also is the spa open to guests or do we need to book separately? We're driving so need to know about parking too. Last time we stayed the wifi was a bit slow in our room, has that been fixed? Thanks!" That's four separate questions plus a complaint wrapped in one email. If you just embed the whole thing and search the FAQ database you get a blended result that partially answers one or two questions and misses the rest. So I built an extraction layer that reads the full email and breaks it into individual questions. It handles directly stated questions ("is the spa open?"), implied questions ("we're driving" implies they need parking info), complaints that need acknowledgment but aren't FAQ-searchable ("wifi was slow"), and informational context that shouldn't be treated as a question at all ("coming on the 20th"). Getting this extraction reliable was probably 40% of the total development time. Layer 2: FAQ knowledge base with vector search All hotel FAQs get embedded and stored in a vector database. Different properties have different amenities, policies, and details so the search is scoped per hotel. When a guest emails the Berlin property asking about breakfast, it searches the Berlin FAQ, not the Munich one. Each extracted question from Layer 1 gets searched independently against the relevant hotel's FAQ. This is critical because searching each question separately gives way better retrieval quality than searching the entire email as one blob. Layer 3: Response assembly Takes the extracted questions plus their FAQ matches and generates a natural email response. The tone needs to sound like a helpful hotel staff member, not a chatbot. It addresses every question the guest asked in a logical order and flags anything it couldn't find an FAQ match for so the support team knows which emails need human follow-up. What I learned: The question extraction step is where most email AI projects would fail. It's tempting to skip it and just do whole-email retrieval. That works for short simple messages but completely breaks down on real customer emails that ramble across multiple topics. Investing the time in proper extraction made everything downstream work better. The per-hotel scoping was more important than I expected. Generic FAQ answers that don't match the specific property create confusion and erode trust. A guest asking about parking at a city center hotel needs a different answer than one asking about parking at a resort property. I made a full step-by-step video walking through the entire build process if anyone wants to see the actual implementation: link Happy to answer questions about the architecture.

2h ago

---

**[are AI coding tools just becoming the new cloud bill problem?](https://www.reddit.com/r/artificial/comments/1tz1mdu/are_ai_coding_tools_just_becoming_the_new_cloud/)**

idk maybe this is obvious to people already working in bigger teams, but the AI coding tool cost thing feels like early cloud all over again. Everyone keeps saying tokens are getting cheaper, which is true, but then somehow companies are still freaking out about AI bills. And I think the reason is pretty simple: people are treating these tools like normal SaaS seats when they are really more like metered infra. Like with a normal dev tool you kind of know the cost. X users, Y dollars per month, done. But with agentic coding tools one small request can quietly turn into a bunch of model calls, context loading, tool calls, retries, verification, more retries, etc. From the user side it looks like “fix this bug” or “write this function” but underneath it may have done a whole mini workflow. And then there is the other cost which I feel people don’t talk about enough: reviewing the generated code. Sometimes the code works but it adds weird duplication, misses existing abstractions, or creates stuff that someone has to clean up later. So the bill is not just tokens. It is also review time + maintenance + future tech debt. Not saying these tools are bad btw. I use them too and they are obviously useful. But it feels like the industry is moving from the fun phase of “look what this can do” to the boring phase of “who is paying for all these calls and did this actually ship anything useful?” Curious if teams are actually tracking this properly yet. Like cost per PR, cost per resolved ticket, cost per workflow etc. Or is it still mostly hidden under “AI productivity” and vibes.

9h ago

---

**[What happened in AI in the last 24 hours](https://www.reddit.com/r/artificial/comments/1tz997d/what_happened_in_ai_in_the_last_24_hours/)**

🚀 SpaceX signed a massive $920 million monthly deal with Google for 110,000 Nvidia chips — this is a huge infrastructure play ahead of their monster $1.7 trillion IPO. 🏛️ The Trump administration is discussing taking equity stakes in top AI firms — this would make the public official partners in the upside of AI-driven economic growth. 🔓 Meta's automated AI support was hacked to take over high-profile accounts — it proves that offloading critical security tasks to AI can create dangerous, easily exploited vulnerabilities. 🧠 Tech workers are trading hours of manual labor for high-level strategy thanks to AI — while tasks now take minutes, humans are still needed for crucial, complex decision-making.

1h ago

---

---

## Google News: "ai"

**[‘A driver of political violence’: how the breakneck AI boom is fueling anti-tech extremism](https://www.theguardian.com/technology/2026/jun/07/anti-ai-tech-extremism-violence)**

Backlash against AI is taking an extremist turn, following in the footsteps of earlier techno-pessimist militants

The Guardian • 14m ago

---

**[Trump: U.S. stake in AI giants "could be a beautiful thing"](https://www.axios.com/2026/06/06/trump-us-stake-ai-companies)**

Axios • 23h ago

---

**['A splash of cold water': Wall Street gauges pause in AI trade](https://finance.yahoo.com/markets/article/a-splash-of-cold-water-wall-street-gauges-pause-in-ai-trade-114012907.html)**

Wall Street analysts weighed in on tech's sell off this week as the blisterin AI trade took a breather.

Yahoo Finance • 1h ago

---

**[AI ‘content creators’ are getting harder to spot](https://www.theverge.com/ai-artificial-intelligence/943187/ai-content-creators)**

Social media platforms are baffled.

The Verge • 1h ago

---

**[AI Won’t Solve Your Talent Crisis, Better Leadership Will](https://www.forbes.com/sites/juliekratz/2026/06/07/ai-wont-solve-your-talent-crisis-better-leadership-will/)**

Explore why workplace culture, authentic allyship, and human trust remain your ultimate competitive advantages, even in the age of AI.

Forbes • 1h ago

---

**[AI CEOs from OpenAI, Anthropic, and Microsoft set aside their rivalry to warn Congress AI is making it too easy to design and create bioweapons](https://fortune.com/2026/06/05/openai-anthropic-microsoft-ceos-congress-bioweapon-safeguards/)**

The signatories want Congress to mandate screening for synthetic DNA sales as AI makes creating a bioweapon easier.

Fortune • 2d ago

---

**[Sorry, I’m Not Available. Talk to the A.I. Version of Me.](https://www.nytimes.com/2026/06/06/business/dealbook/ai-digital-twin.html)**

The New York Times • 1d ago

---

**[4 surprising ways AI is making your life more expensive](https://www.washingtonpost.com/technology/2026/06/06/inflation-is-being-driven-up-by-huge-investment-artificial-intelligence/)**

These goods and services are getting more expensive due to spillover from massive tech company investments in artificial intelligence.

The Washington Post • 21h ago

---

**[‘It’s a hurricane warning’: Guardrails around powerful AI models may be too late](https://www.politico.com/news/2026/06/07/frontier-ai-cybersecurity-china-race-00952786)**

Politico • 2h ago

---

**[Abel goes his own way with new Berkshire investments, including billions for AI](https://www.cnbc.com/2026/06/06/abel-goes-his-own-way-with-new-berkshire-investments-including-billions-for-ai.html)**

Warren Buffett tells CNBC's Becky Quick new Berkshire Hathaway CEO Greg Abel has "launched" with his first major deal.

CNBC • 1d ago

---

---

## HackerNews: "ai"

**[Meta confirms 1000s of Instagram accounts were hacked by abusing its AI chatbot](https://news.ycombinator.com/item?id=48427643)**

Meta fixed the bug that let anyone trick its Meta AI chatbot into resetting the password on Instagram accounts that didn't have two-factor authentication.

⬆️ 633 • 💬 230 • 18h ago • [~this week in security~](https://this.weekinsecurity.com/meta-confirms-thousands-of-instagram-accounts-were-hacked-by-abusing-its-ai-chatbot/)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 532 • 💬 141 • 2d ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 523 • 💬 692 • 2d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[Ask HN: Why is the HN crowd so anti-AI?](https://news.ycombinator.com/item?id=48420827)**

⬆️ 419 • 💬 700 • 1d ago

---

**[Astronauts told to return to ISS after sheltering over air leak repairs](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 417 • 💬 262 • 1d ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 277 • 💬 69 • 2d ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[South Korean forums will need to scan every images with AI censorship tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 268 • 💬 149 • 2d ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

**[The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy](https://news.ycombinator.com/item?id=48422993)**

⬆️ 211 • 💬 95 • 1d ago • [blog.includesecurity.com](https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/)

---

**[Hacker News, Sans AI](https://news.ycombinator.com/item?id=48417916)**

⬆️ 182 • 💬 100 • 1d ago • [elijahpotter.dev](https://elijahpotter.dev/articles/hacker-news-sans-AI)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 167 • 💬 104 • 2d ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

---

## YouTube Videos: "ai"

**[Google&#39;s New AI Architecture Changes Everything (Gemma 4 12B)](https://www.youtube.com/watch?v=WLtCHXdHTF0)**

Google DeepMind just released Gemma 4 12B, a new AI model that completely changes how LLMs process pictures and sound.

📺 Better Stack

👁️ 15K • 👍 682 • 💬 64 • ⏱️ 11:02 • 11h ago

---

**[Anthropic Just Warned Everyone About Claude (It’s Evolving)](https://www.youtube.com/watch?v=JlwwyNtHsCI)**

Anthropic just published a major warning about AI self-improvement, and the numbers behind it are hard to ignore. Claude is now ...

📺 AI Revolution

👁️ 64K • 👍 2K • 💬 294 • ⏱️ 17:13 • 1d ago

---

**[AI Tells Me to Drink Bleach](https://www.youtube.com/watch?v=Eky_eh-aSuM)**

📺 CodeMiko

👁️ 33K • 👍 2K • 💬 167 • ⏱️ 0:49 • 1d ago

---

**[The Limitless AI Lie. The Bubble Is Slowly BURSTING.](https://www.youtube.com/watch?v=o5jrjvi_w9Q)**

You've probably heard that the artificial intelligence revolution is running out of money, but the truth is much worse. It's running out ...

📺 The Infographics Show

👁️ 273K • 👍 6K • 💬 1K • ⏱️ 19:55 • 21h ago

---

**[Full body waifus, AI dreams, realtime AI music, open-source Gemini Omni: AI NEWS](https://www.youtube.com/watch?v=CzxqQJOswvo)**

HUGE AI NEWS: Minimax M3, Ideogram v4, Bernini, Gemma4, Nemotron 3 Ultra, & more #ai #ainews #aitools #agi #singularity ...

📺 AI Search

👁️ 36K • 👍 2K • 💬 197 • ⏱️ 49:09 • 9h ago

---

**[The AI obsession is backfiring](https://www.youtube.com/watch?v=apnIvQXMyz0)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 63K • 👍 4K • 💬 833 • ⏱️ 15:39 • 14h ago

---

**[Anthropic calls for global pause in AI development](https://www.youtube.com/watch?v=joZ4Esutu9w)**

The artificial intelligence company's warns that we need to pause development before AI can build itself and humans lose control ...

📺 ABC News

👁️ 84K • 👍 2K • 💬 607 • ⏱️ 4:00 • 1d ago

---

**[How to Build a $10M Business with AI (Zero Employees)](https://www.youtube.com/watch?v=b3yuAekDS4U)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4x5Fku6 Are you building an AI software ...

📺 Dan Martell

👁️ 76K • 👍 3K • 💬 142 • ⏱️ 14:11 • 3d ago

---

**[I Asked AI to Recreate This Image 100 Times To See What Would Happen](https://www.youtube.com/watch?v=imbF-igIJDM)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 622K • 👍 41K • 💬 976 • ⏱️ 0:45 • 19h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 4.0M • 👍 113K • 💬 1K • ⏱️ 0:29 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 115,556 • ❤️ 1,483 • 11d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 434,969 • ❤️ 648 • 3d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 568,158 • ❤️ 432 • 1d ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 99,655 • ❤️ 389 • 3d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 4,377 • ❤️ 325 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,923,564 • ❤️ 1,499 • 1mo ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 162,822 • ❤️ 715 • 17d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 16,924 • ❤️ 244 • 5d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 118,326 • ❤️ 535 • 1d ago

---

**[ideogram-4-nf4](https://huggingface.co/ideogram-ai/ideogram-4-nf4)**

*Ideogram*

Ideogram 4 is a state-of-the-art, open-weight text-to-image diffusion model trained from scratch. It excels at multilingual text rendering, layout control, and native 2k resolution image generation, positioning it at the forefront of design-oriented visual intelligence.

`text-to-image`

⬇️ 3,844 • ❤️ 219 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 14 • 💬 1 • ⭐ 81,097 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 87 • 💬 4 • ⭐ 83,696 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 91 • 💬 1 • ⭐ 9,597 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 5,220 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,496 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 39 • 💬 4 • ⭐ 28,821 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,705 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 7 • 💬 1 • ⭐ 208 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 59 • 💬 2 • ⭐ 57,907 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 79 • 💬 7 • ⭐ 76,075 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 60.1k • 🔱 7.3k • 2h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.2k • 🔱 610 • 5d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.6k • 🔱 745 • 3d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.1k • 🔱 312 • 2d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 317 • 2d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 407 • 16d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 1.9k • 🔱 208 • 9h ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 133 • 2d ago

---

**[XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI)**

AI agent workspace for DeepSeek models, with Code and Claw modes built into your application.

`TypeScript`

⭐ 1.8k • 🔱 154 • 6h ago

---

**[deeplethe/forkd](https://github.com/deeplethe/forkd)**

Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm parent; BRANCH a live VM in ~150ms. KVM-isolated, snapshot CoW.

`Rust` `ai-agents` `copy-on-write` `kvm` `microvm` `rust`

⭐ 1.8k • 🔱 134 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
