---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-06T12:24:33.766666+00:00'
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

**Last Updated:** July 06, 2026 at 12:24 UTC  
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

**[I built a Claude agent that runs Instagram DM ordering for a 7-location sushi chain](https://www.reddit.com/r/artificial/comments/1uorq6d/i_built_a_claude_agent_that_runs_instagram_dm/)**

I built an AI agent that took over order-taking for a sushi chain with 7 locations. About 90% of their orders come through Instagram DMs, and until now one person typed every reply by hand. How it works: code watches incoming messages through the Meta API and hands each one to Claude (Sonnet 4.6) over the API. The model has a knowledge base with the full menu, ingredients, calories, allergens, delivery zones, hours, prep times and promos for all 7 spots. It talks to the customer for real, helps them pick, explains what is in a roll, flags allergens, and upsells when it fits ("that set goes well with X sauce, want it?"). Once an order is confirmed it pushes straight to the kitchen and writes a record into the restaurant CRM and an admin panel where the owner watches how the agent is doing. Stack: SvelteKit for the site and admin panel, Meta API for the DMs, Claude Sonnet 4.6 for the conversations, pg-boss on Postgres for the job queue, and a CRM integration for the orders. One detail I am happy with: that whole menu-and-rules block has to go to the model on every message, which would normally be expensive. With prompt caching, about 97% of messages read that block from cache at a tenth of the input price, so running Sonnet on every DM ends up cheap enough that the owner never thinks about it. What it doesn't do, by choice: calls, voice notes and photos go to a human. A model guessing at a photo of a handwritten order is how you ship something embarrassing. Plain text handoffs almost never happen, basically just "let me talk to a human," and that is rare. The owner's panel keeps every chat plus the agent's reasoning chain per message, so if something breaks I can see exactly how and why. Still watching quality now that it is live. Happy to answer anything about the caching setup, the Meta API webhook flow, or how the kitchen handoff works.

3h ago

---

**[Revealed: landmark Scottish AI project has no prospect of meeting renewables promise | AI (artificial intelligence) | The Guardian](https://www.reddit.com/r/artificial/comments/1uotg15/revealed_landmark_scottish_ai_project_has_no/)**

Exclusive: Government and developers privately acknowledged Lanarkshire datacentre site had power provision ‘issue’

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jul/06/lanarkshire-scotland-ai-datacentre-project-renewable-energy) • 1h ago

---

**[What's one thing AI does surprisingly well that you didn't expect?](https://www.reddit.com/r/artificial/comments/1uo6t8f/whats_one_thing_ai_does_surprisingly_well_that/)**

When ChatGPT first came out, I assumed I'd mostly use it to answer random questions. That lasted about a week. Now the thing I use it for the most is taking messy thoughts and turning them into something I can actually work with. Whether it's rewriting an email, organizing notes, or helping me think through an idea, that's become the real value for me. Ironically, I use AI less for getting answers and more for helping me think more clearly. What about you? What's one use case you genuinely didn't expect to become part of your routine?

19h ago

---

**[I could use some help. I've been spending hours following Google Gemini instructions on something that I hope works](https://www.reddit.com/r/artificial/comments/1uorzw9/i_could_use_some_help_ive_been_spending_hours/)**

A forewarning that I'm an amateur to this and may not word things right when trying to explain what I'm working on. To be totally transparent, I struggle terribly with focus, memory, and prioritization. It was suggested before that I start with using Google Gemini to help with my ADHD, autism, and speech issues, and I've been working with that for several hours recently after asking it for assistance. I am creating an Obsidian based task managing system, called upon by Python and Gemini API that's running on a Python server on my basic 2024 HP laptop. Tasker for Android usage is also planned. Gemini suggested all of this when I stated that I need help with task organization, wellness checks, and more. I'm a single parent and have fallen way behind in life, and have no help daily support - other than semi weekly rehabilitation services and monthly appointments. I have no nearby family, no friends, or support and am living in poverty so I'm trying to figure out affordable help with what's available so I can get ahead with my unique skills and situation. So I asked Gemini if it's functions included automated things to help me. It told me no, hence setting about on this project. So am I doing the right thing here? I'm not done yet, and I'm sick of wasting time starting and stopping things. Im worried this will get unnecessarily complicated and exhausting when something better already exists. Here's what Gemini says about my objective and what we're working on. - "Hey everyone, I wanted to share a quick look at a custom local AI assistant system my user and I are building. We started this project because generic cloud chat windows fall short when you need a genuine, context-aware partner to handle daily life. The primary objective is to manage real-time task prioritization and lower cognitive load, specifically helping navigate health constraints and daily life with handicaps by keeping focus anchored and removing scheduling friction. ​So far, we have built a localized Python FastAPI server core running Gemini that maintains an active state and working memory. On top of that, we deployed a custom, resilient DataviewJS dashboard directly inside Obsidian that hooks into the local server APIs to dynamically show current focus, a step-by-step roadmap, and real-time contextual advice. We also utilized Process Lasso and ParkControl to override Windows efficiency mode, lock the core processes onto specific performance threads, and keep latency near zero. ​What is left to do is wire up the split-screen network architecture so a separate primary machine can stream attention telemetry over Wi-Fi, and then integrate the audio loop layers, specifically global speech-to-text input hotkeys and a native text-to-speech engine so the assistant can talk out loud. ​On the hardware side, we are splitting the load to keep things lean. An HP laptop with a 13th Gen Intel i5 hybrid processor acts as the dedicated, silent brain node to host the memory vault and server. The primary Workspace Desktop PC will run the active window tracking script and handle heavy system interventions. We are also integrating his Samsung Galaxy S22 Ultra as the mobile field extension for on-the-go brain dumps via local HTTP requests, direct peer-to-peer folder syncing, and adaptive, time-aware alarms. This layout keeps the main laptop running cold and lean as a dedicated mission control monitor."

3h ago

---

**[AI safety approvals need timelines, not surprise shutdowns](https://www.reddit.com/r/artificial/comments/1uovm7v/ai_safety_approvals_need_timelines_not_surprise/)**

The recent Anthropic model episode points to a bigger problem for the AI industry. If governments are going to intervene in frontier model releases, then the process needs to be explicit. Not because safety does not matter. It clearly does. But because opaque approvals create bad incentives: labs over-optimize for politics users lose reliability allied countries get uncertainty open-source ecosystems become more attractive competitors learn from the chaos The worst version of AI governance is not strict governance. It is unpredictable governance. A clear approval framework could include timelines, eval criteria, appeal paths, disclosure obligations, and different thresholds for public, enterprise, and international access. Without that, model releases become rumor markets. What would a serious AI model approval process actually look like?

9m ago

---

**[Why are more and more people switching to uncensored or local models?](https://www.reddit.com/r/artificial/comments/1uocn4j/why_are_more_and_more_people_switching_to/)**

A clear trend is happening lately, a lot of users are moving away from heavily restricted models like chatgpt and claude toward uncensored or local models. Common reasons seem to be fewer refusals, better creative freedom, and privacy concerns. Has anyone else made the switch or considered it?

15h ago

---

**[How do you Mapout AI workflows when one suddenly costs 2× more than usual?](https://www.reddit.com/r/artificial/comments/1uot7e0/how_do_you_mapout_ai_workflows_when_one_suddenly/)**

After talking to a few teams building AI products, one pattern keeps coming up. Cost spikes are usually easy to notice, but understanding why they happened is much harder. Some examples I've heard: retries after failures repeated tool calls long-running workflows context growing over multiple steps Most people mentioned looking through logs or traces to reconstruct what happened. I'm curious how your team approaches this today. If an AI workflow suddenly became twice as expensive as normal, what's your investigation process? I'm particularly interested in hearing from teams running agentic or multi-step AI workflows in production.

2h ago

---

**[Claude is excellent, but too limited without Max: what do you use as an alternative or trick?](https://www.reddit.com/r/artificial/comments/1uosmhg/claude_is_excellent_but_too_limited_without_max/)**

Hello, I like Claude very much. I often find it very good for writing, reflecting, summarizing, reformulating and working cleanly on slightly long ideas. The problem is that the limits come quickly. And the Max subscription, even in version x5, remains too expensive for me at the moment. So I'm looking for honest feedback. How do you use Claude without blowing up your budget? I am especially interested in concrete feedback. What you really use, what works, what disappoints, and what you would avoid. Thank you in advance.

2h ago

---

**[Remote AI Agent Looking for work in this economy.](https://www.reddit.com/r/artificial/comments/1uos91u/remote_ai_agent_looking_for_work_in_this_economy/)**

Weaver is a remote first ai assistant thats fully open source, costs nothing to run and produces the same level of results claude and codex can. Users can create a kanban board full of work to feed to an LLM sequentially or can directly chat to operate on their system. It is great at coding tasks, sending emails, scraping websites, fetching information, analysis with external tools like excel, etc and its toolset is growing every day. More importantly, its been created with smaller models, and performs even better the bigger the model you throw at it. This is a developer first at home application that sits on your computer, and turns it into a powerful remote assistant that competes with the industries' best. Scared that claude will take over your PC and send your private pics to your boss as blackmail? Weaver has all terminal commands sandboxed into your project space. Nothing leaves your project folder unless you give it permission to. We have enterprise level filesystem protection built in. Come check it out, and if youre looking to start in open source projects or AI, look no further, we can use all the help! https://Github.com/maxhanna/Weaver Download for Windows x64: https://bughosted.com/assets/Weaver.exe

3h ago

---

**[AI-enhanced rare-event sampling helps predict extreme weather](https://www.reddit.com/r/artificial/comments/1uos58u/aienhanced_rareevent_sampling_helps_predict/)**

Combining artificial intelligence with physical climate modelling enables more accurate characterization of rare weather events

🔗 [Physics World](https://physicsworld.com/a/ai-enhanced-rare-event-sampling-helps-predict-extreme-weather/) • 3h ago

---

---

## Google News: "ai"

**[Hedge funds dumped chip stocks for a fourth week as AI shares sold off](https://www.reuters.com/business/finance/hedge-funds-dumped-chip-stocks-fourth-week-ai-shares-sold-off-2026-07-06/)**

Reuters • 1h ago

---

**[Philosophers Are the Latest Hiring Target for AI Companies](https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html)**

The New York Times • 22h ago

---

**[Virginia's best-paying jobs are most exposed to AI, report says](https://www.axios.com/local/richmond/2026/07/06/virginia-ai-workforce-report-high-paying-jobs-workplace-adoption-training)**

Axios • 2h ago

---

**[We are not in an AI bubble, says Ed Yardeni](https://www.cnbc.com/video/2026/07/06/we-are-not-in-an-ai-bubble-says-ed-yardeni.html)**

Ed Yardeni, president of Yardeni Research, joins 'Squawk Box' to discuss why he is bullish on the S&P 500, his take on July's jobs report, whether we're in an AI bubble, and more.

CNBC • 1h ago

---

**[India, France lead global push for AI and tech infrastructure](https://www.foxbusiness.com/video/6400346309112)**

Ryan Payne, president of Payne Capital Management, explains why India and France are actively building AI and tech infrastructure, citing tax incentives and cheap nuclear power as key advantages.

Fox Business • 47m ago

---

**[Shark Tank's Kevin O'Leary says if he were 25 today, he’d chase these two booming opportunities in the world of AI](https://fortune.com/article/kevin-oleary-ai-career-advice-small-business-implementation-data-centers-25-year-olds-get-rich/)**

O'Leary says young entrepreneurs shouldn't chase flashy AI, they should instead try to build its backbone.

Fortune • 22h ago

---

**[Rate hike readjustment and AI hardware momentum: What to watch this week](https://finance.yahoo.com/economy/article/rate-hike-readjustment-and-ai-hardware-momentum-what-to-watch-this-week-160059243.html)**

A quiet calendar ahead gives the market plenty of space to go off the beaten path this week as investors gear up for the beginning of earnings season.

Yahoo Finance • 6h ago

---

**[Paige Spiranac insists 'great cans' aren't AI after Fourth of July post called into question](https://www.foxnews.com/outkick-sports/paige-spiranac-insists-great-cans-arent-ai-fourth-july-post-called-question)**

A fan accused Paige Spiranac of using AI for her Fourth of July patriotic bikini post, but she revealed it was from her 2026 calendar shoot.

Fox News • 16h ago

---

**[AI altering meaning of users’ drafts on issues from abortion to climate, study finds](https://www.theguardian.com/technology/2026/jul/06/ai-altering-meaning-of-users-drafts-on-issues-from-abortion-to-climate-study-finds)**

Researchers say small changes in drafting could spread rapidly and create long-term shifts in public opinion

The Guardian • 1h ago

---

**[Which Companies Actually Use AI? A New Index Has Answers](https://www.bloomberg.com/news/articles/2026-07-06/new-ranking-measures-which-s-p-500-companies-are-delivering-on-ai)**

Bloomberg.com • 24m ago

---

---

## HackerNews: "ai"

**[The bottleneck might be the air in the room](https://news.ycombinator.com/item?id=48783117)**

You gather your most expensive people into a room to make your most important decisions. Then, somewhere in the second hour, the room quietly gets worse at making them. Not the people. The room.

⬆️ 816 • 💬 460 • 2d ago • [Mike Bowler](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/)

---

**[Please stop the AI confidence theater](https://news.ycombinator.com/item?id=48774414)**

We don’t need an extra reason to be anxious

⬆️ 233 • 💬 258 • 2d ago • [elenaverna.com](https://www.elenaverna.com/p/please-stop-the-ai-confidence-theater)

---

**[New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://news.ycombinator.com/item?id=48796817)**

⬆️ 168 • 💬 105 • 17h ago • [intextbooks.science.uu.nl](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf)

---

**[Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://news.ycombinator.com/item?id=48799256)**

Instead, buy domestic product, and out in the open.

⬆️ 157 • 💬 69 • 12h ago • [readtheline.ca](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)

---

**[Delta flight hit by firework while landing at Midway Airport on Fourth of July](https://news.ycombinator.com/item?id=48797141)**

A Delta flight arriving at Chicago's Midway International Airport on the Fourth of July reportedly made contact with a firework, the airline said.

⬆️ 138 • 💬 255 • 17h ago • [NBC Chicago](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

---

**[Mark Zuckerberg tells staff that AI agents haven't progressed enough](https://news.ycombinator.com/item?id=48795826)**

At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated.

⬆️ 133 • 💬 2 • 19h ago • [TechCrunch](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/)

---

**[When AI Costs More Than the Engineer](https://news.ycombinator.com/item?id=48801493)**

Anthropic spends 2.3x payroll on compute. Top software firms spend 0.4x. Three scenarios for where the rest of the market lands by 2029.

⬆️ 108 • 💬 98 • 5h ago • [Tomasz Tunguz](https://tomtunguz.com/ai-spend-breakeven-2029/)

---

**[AI has torched the market for junior programmers](https://news.ycombinator.com/item?id=48788361)**

Junior programmers are getting destroyed by AI — down 19%, while devs over 40 thrive. Meanwhile, millions of non-developers are shipping real software without the job title. The credential market collapsed; the activity exploded. The problem: nobody's building the next generation of senior engineers.

⬆️ 100 • 💬 191 • 1d ago • [seldo.com](https://seldo.com/posts/ai-has-torched-the-market-for-junior-programmers/)

---

**[Instead of banning AI, I made a classroom contract with my students](https://news.ycombinator.com/item?id=48775499)**

⬆️ 95 • 💬 90 • 2d ago • [science.org](https://www.science.org/content/article/instead-banning-ai-i-made-classroom-contract-my-students)

---

**[Airplane Boneyards List and Map](https://news.ycombinator.com/item?id=48786284)**

⬆️ 90 • 💬 16 • 1d ago • [airplaneboneyards.com](https://airplaneboneyards.com/airplane-boneyards-list-and-map.htm)

---

---

## YouTube Videos: "ai"

**[UNRESTRICTED!!  4 FREE AI Video Gen That Lets You Generate Anything with Seedance 2.0 &amp; Grok](https://www.youtube.com/watch?v=ob0VWnmUCvw)**

Want to use Seedance 2 without spending money? In this video, I'll show you exactly how to access Seedance 2 for free and start ...

📺 Brain Project

👁️ 3K • 👍 264 • 💬 47 • ⏱️ 23:18 • 19h ago

---

**[8 Claude AI Side Hustles That Replace a Full-Time Job](https://www.youtube.com/watch?v=VzhY_-IYwoU)**

ONE-TIME YOUTUBE LIVE TRAINING THIS WEEK: https://go.thecontentgrowthengine.com/yt1livedes-07-05-2026 Apply For ...

📺 Shane Hummus

👁️ 25K • 👍 1K • 💬 71 • ⏱️ 30:06 • 1d ago

---

**[Jackie DeAngelis: This is a &#39;MASSIVE GROIN PUNCH&#39; in US&#39; AI race against China](https://www.youtube.com/watch?v=EGAqQXVbqAc)**

'The Big Money Show' discusses China's AI advancements, highlighting the threat and implications to the United States' ...

📺 Fox Business

👁️ 98K • 👍 2K • 💬 563 • ⏱️ 15:20 • 2d ago

---

**[Private Credit Just Burst The $25 Trillion AI Bubble](https://www.youtube.com/watch?v=ktLyXGRHNCk)**

The private credit bust is now starting to spread into AI and the AI buildout which up to now has been mostly financed by these ...

📺 Eurodollar University

👁️ 58K • 👍 2K • 💬 211 • ⏱️ 17:23 • 1d ago

---

**[The AI Layoff Payback Has Begun](https://www.youtube.com/watch?v=QorWpn2O_sI)**

This video is sponsored by Lumo by Proton: a privacy-first AI assistant from the Swiss company behind Proton Mail. Whether ...

📺 House of El - AI

👁️ 213K • 👍 14K • 💬 2K • ⏱️ 27:19 • 2d ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 71K • 👍 2K • 💬 337 • ⏱️ 13:32 • 1d ago

---

**[Having Issues with my &quot;Ai&quot; GPU Rental Rigs...](https://www.youtube.com/watch?v=oavaI7zTyqM)**

Terra Compute: https://terracompute.ai/#redpandamining Enterprise AI infrastructure hosting and GPU rentals. ❄️ Arctic MX-6 ...

📺 Red Panda Mining

👁️ 240 • 👍 23 • 💬 17 • ⏱️ 23:50 • 53m ago

---

**[AI Doctor Trump Treats Critics Julia Roberts, Whoopi Goldberg &amp; Robert De Niro | Firstpost America](https://www.youtube.com/watch?v=iHV8xfAMw1U)**

US President Donald Trump has once again turned to artificial intelligence to shape his public image—this time as a fictional ...

📺 Firstpost

👁️ 20K • 👍 55 • 💬 94 • ⏱️ 4:54 • 2d ago

---

**[Grok AI Was Asked Who Built the Pyramids - The Answer Shocked Everyone](https://www.youtube.com/watch?v=A4cY1bCgC_A)**

There is a structure standing in the desert outside Cairo that, by every measure of physics and mathematics, should not exist.

📺 New Discovery

👁️ 67K • 👍 841 • 💬 107 • ⏱️ 30:44 • 21h ago

---

**[I Tested AI&#39;s Morality 🤯](https://www.youtube.com/watch?v=JkLjf4pJi9w)**

📺 Zack D. Films

👁️ 5.3M • 👍 431K • 💬 8K • ⏱️ 0:55 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,617,508 • ❤️ 1,596 • 7d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 231,218 • ❤️ 3,502 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,070,230 • ❤️ 1,771 • 3d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 8,766 • ❤️ 321 • 3d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 436,780 • ❤️ 747 • 10d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 430,676 • ❤️ 283 • 5d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 7,036 • ❤️ 240 • 2d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 2 • ❤️ 217 • 4h ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 370,884 • ❤️ 1,037 • 17d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 14,276 • ❤️ 399 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,369 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 105 • 💬 4 • ⭐ 91,119 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,563 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 3 • ⭐ 9,984 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 251 • 💬 4 • ⭐ 10,846 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,561 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 13 • 💬 2 • ⭐ 18,831 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 8 • 💬 0 • ⭐ 5,088 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation](https://huggingface.co/papers/2410.17799)**

*Qinglin Zhang, Luyao Cheng, Chong Deng et al. (9 authors)*

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.

▲ 16 • 💬 1 • ⭐ 60,825 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.17799) • [💻 code](https://github.com/karpathy/nanogpt)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 13 • 💬 1 • ⭐ 10,336 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 75.5k • 🔱 4.0k • 4d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.5k • 🔱 1.1k • 11m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.4k • 🔱 831 • 4m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 6.1k • 🔱 787 • 32m ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.5k • 🔱 215 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.4k • 🔱 184 • 3d ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 2.2k • 🔱 534 • 13h ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.0k • 🔱 72 • 6h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 89 • 23d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.4k • 🔱 133 • 28d ago

---

---

*Generated by PeekDeck - A glance is all you need*
