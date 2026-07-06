---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-06T18:17:50.015990+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 06, 2026 at 18:17 UTC  
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

**[Can AI help with the emotional emptiness people feel in modern life?](https://www.reddit.com/r/artificial/comments/1up0k2f/can_ai_help_with_the_emotional_emptiness_people/)**

I’ve been thinking about something less technical about AI. In many ways, people’s living standards are getting better. We have better tools, more convenience, more entertainment, and access to more information than before. But at the same time, it feels like many people are still emotionally empty, confused, or lost. Even with better material conditions, people still seem to be searching for meaning, direction, connection, or some kind of inner stability. In some ways, the faster the world develops, the more confused people seem to become. So I’m curious: Can AI actually help with this kind of emotional emptiness or confusion? Not as a replacement for real relationships, therapy, or human connection, but maybe as a tool for reflection, journaling, self-understanding, or organizing thoughts. Or does AI only make people feel temporarily understood while the deeper problem remains? Have you ever used AI to deal with loneliness, confusion, lack of direction, or questions about meaning? Did it actually help?

2h ago

---

**[I built a Claude agent that runs Instagram DM ordering for a 7-location sushi chain](https://www.reddit.com/r/artificial/comments/1uorq6d/i_built_a_claude_agent_that_runs_instagram_dm/)**

I built an AI agent that took over order-taking for a sushi chain with 7 locations. About 90% of their orders come through Instagram DMs, and until now one person typed every reply by hand. How it works: code watches incoming messages through the Meta API and hands each one to Claude (Sonnet 4.6) over the API. The model has a knowledge base with the full menu, ingredients, calories, allergens, delivery zones, hours, prep times and promos for all 7 spots. It talks to the customer for real, helps them pick, explains what is in a roll, flags allergens, and upsells when it fits ("that set goes well with X sauce, want it?"). Once an order is confirmed it pushes straight to the kitchen and writes a record into the restaurant CRM and an admin panel where the owner watches how the agent is doing. Stack: SvelteKit for the site and admin panel, Meta API for the DMs, Claude Sonnet 4.6 for the conversations, pg-boss on Postgres for the job queue, and a CRM integration for the orders. One detail I am happy with: that whole menu-and-rules block has to go to the model on every message, which would normally be expensive. With prompt caching, about 97% of messages read that block from cache at a tenth of the input price, so running Sonnet on every DM ends up cheap enough that the owner never thinks about it. What it doesn't do, by choice: calls, voice notes and photos go to a human. A model guessing at a photo of a handwritten order is how you ship something embarrassing. Plain text handoffs almost never happen, basically just "let me talk to a human," and that is rare. The owner's panel keeps every chat plus the agent's reasoning chain per message, so if something breaks I can see exactly how and why. Still watching quality now that it is live. Happy to answer anything about the caching setup, the Meta API webhook flow, or how the kitchen handoff works.

9h ago

---

**[Benchmarks compare open models against closed products, not closed models. We might be missing what were actually paying for](https://www.reddit.com/r/artificial/comments/1uovy56/benchmarks_compare_open_models_against_closed/)**

So this has been on my mind for a while and it kinda bugs me. Every time someone benchmarks glm-5.2 or deepseek against claude or gpt, the closed one wins on some tasks and people just assume the underlying model is smarter. but thats not really what were measuring. We dont know what these closed providers actually do behind the api. they might be running rag over their own docs, injecting hidden system prompts based on your query, routing to specialized expert models depending on task type, doing prompt preprocessing we never see, hitting internal tool calls before the model even generates a response. anthropic already hides reasoning traces and doesnt show you the full pipeline. we get the polished output and we assume its just the model. Meanwhile when you benchmark an open model youre benchmarking raw inference. no scaffolding, no hidden tools, no preprocessing. its like comparing a cars engine on a dyno to another car actually driving on a road with traction control and abs and lane assist. the road one looks better but its not because the engine is stronger. Which makes me wonder if the actual model quality gap between the frontier closed stuff and something like glm-5.2 is way smaller than benchmarks suggest. What you are paying premium for might be the tooling and the harness wrapped around it, not the raw model. and if thats true this whole industry is heading somewhere weird, because tooling is way easier to replicate than model architecture, and open weights plus open source tooling starts to look really competitive really fast. There is a broader thing going on too. software engineering hasnt actually changed in principle, its still specs, architecture, tradeoffs, maintainability. what changed is the volume. line by line code review doesnt scale when agents produce diffs at this rate, so review has to move upstream to specs and downstream to tests, metrics, traces, observability. thats where the actual verification happens now, not in the middle where volume already broke it. So heres what i am stuck on. when we say model X is better than model Y based on benchmarks, are we actually comparing model to model, or are we comparing raw inference against everything the closed provider bolted onto it that we cant see, and does that distinction even matter to anyone anymore.

5h ago

---

**[What companies that you've actually called had a good AI voice customer support?](https://www.reddit.com/r/artificial/comments/1up056b/what_companies_that_youve_actually_called_had_a/)**

It feels like there's so much hype around AI for voice customer support these days, yet almost every time I call a company, I end up in the same old experience where I have to press 1, 2, or 3, repeat myself several times, or get stuck in a loop. It rarely feels like AI has actually made the experience better... I've been trying to find examples of companies that have actually built good AI phone support, but most articles just talk about the vendors behind the technology. I'm not looking for companies like ElevenLabs, or similar that provide technology. I'm looking for the actual brands you've called and where you thought: "That was helpful/good/etc." Any experience you could share?

3h ago

---

**[Nearly 90 Startups Hit Unicorn Status in Record First Half of 2026](https://www.reddit.com/r/artificial/comments/1uowx1s/nearly_90_startups_hit_unicorn_status_in_record/)**

Artificial intelligence startups are driving an unprecedented surge in venture capital activity, with nearly 90 new unicorns emerging in the first half of 2026 alone — a pace that far exceeds previ…

🔗 [Wealthari](https://wealthari.com/nearly-90-startups-hit-unicorn-status-in-record-first-half-of-2026/) • 5h ago

---

**[San Francisco court consolidates a dozen lawsuits alleging ChatGPT encouraged suicide and drug use](https://www.reddit.com/r/artificial/comments/1up0ou1/san_francisco_court_consolidates_a_dozen_lawsuits/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/openai-chatgpt-suicide-cases-22301936.php) • 2h ago

---

**[Should AI be able to prove what it knew at the time?](https://www.reddit.com/r/artificial/comments/1uowfa3/should_ai_be_able_to_prove_what_it_knew_at_the/)**

This might be a daft thought experiment, but I keep coming back to it. As AI gets more autonomous, should it be able to prove what it knew when it made a decision? Not just give a nice explanation afterwards, because we all know models can do that whether it’s true or not. I mean some kind of actual memory trail. Like version history, but for what the AI believed or had access to at that point. Would that be useful for trust and accountability, or is it overkill?

5h ago

---

**[after months of building, i shipped my first ever iOS app today!!](https://www.reddit.com/r/artificial/comments/1up4kww/after_months_of_building_i_shipped_my_first_ever/)**

kept using AI for actual decisions, not "write my email" but real ones like whether to take a contract or an idea worth building, and i realized the answer just depended on which model i happened to open. one says go, one says wait, one hedges. i wasn't getting an answer, i was getting one model's opinion in a confident voice and treating it like it settled things. so i built the opposite. you give it one hard decision and five different models (claude, gpt-5, gemini, grok, qwen) each argue it from a locked role across three rounds, then you get one verdict with the disagreements kept visible instead of smoothed into a safe average. the disagreement turned out to be the actual signal, the one model that broke from the pack was usually pointing at the thing i'd skipped. it went live on the App Store this morning, which still feels unreal. free to start: https://apps.apple.com/us/app/war-table-ai-council/id6780293764 genuinely curious what people here think though, do you trust the disagreement between models more than the consensus, or is that just reading signal into noise?

31m ago

---

**[Funny AI chatbot with customizable alcohol level](https://www.reddit.com/r/artificial/comments/1uowk5h/funny_ai_chatbot_with_customizable_alcohol_level/)**

I created an AI that answers in funny and poetic way. You can also setup the alcohol level, and get drunk-like answers. Also the voice (right-bottom speaker icon) gets drunk. Please give me feedback on that! https://aint.labs.seniqs.no/

5h ago

---

**[Revealed: landmark Scottish AI project has no prospect of meeting renewables promise | AI (artificial intelligence) | The Guardian](https://www.reddit.com/r/artificial/comments/1uotg15/revealed_landmark_scottish_ai_project_has_no/)**

Exclusive: Government and developers privately acknowledged Lanarkshire datacentre site had power provision ‘issue’

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jul/06/lanarkshire-scotland-ai-datacentre-project-renewable-energy) • 7h ago

---

---

## Google News: "ai"

**[Alibaba’s A.I. Is a Hit, but Hard to Turn Into a Moneymaker](https://www.nytimes.com/2026/07/06/business/alibaba-ai-qwen.html)**

The New York Times • 2h ago

---

**[Inside the secret AI war between Silicon Valley and China](https://www.washingtonpost.com/national-security/2026/07/06/why-anthropic-alleges-chinese-firms-are-distilling-knowledge-claude/)**

American tech firms say rivals are forcing their chatbots to act as tutors to make Chinese AI smarter.

The Washington Post • 2h ago

---

**[The Hollywood Bowl just got its biggest sound upgrade in a generation. AI is doing the heavy lifting](https://www.latimes.com/entertainment-arts/music/story/2026-07-06/hollywood-bowl-sound-upgrade-ai)**

A new speaker array, an immersive surround system and machine-learning vocal isolation technology are transforming the experience at one of the world's most beloved concert venues.

Los Angeles Times • 32m ago

---

**[Khan Academy CEO on AI's impact to labor, and how to use it effectively](https://www.cnbc.com/video/2026/07/06/khan-academy-ceo-on-ais-impact-to-labor-and-how-to-use-it-effectively.html)**

Sal Kahn, Kahn Academy CEO, joins 'The Exchange' to discuss AI's impact on labor, how using AI will help employees and much more.

CNBC • 11m ago

---

**[Researchers help close a critical security gap across AI platforms](https://techxplore.com/news/2026-07-critical-gap-ai-platforms.html)**

Tech Xplore • 37m ago

---

**[Shark Tank's Kevin O'Leary says if he were 25 today, he’d chase these two booming opportunities in the world of AI](https://fortune.com/article/kevin-oleary-ai-career-advice-small-business-implementation-data-centers-25-year-olds-get-rich/)**

O'Leary says young entrepreneurs shouldn't chase flashy AI, they should instead try to build its backbone.

Fortune • 1d ago

---

**[AI ‘Actor’ Tilly Norwood To Star In Feature Film ‘Misaligned’](https://deadline.com/2026/07/tilly-norwood-ai-actor-misaligned-1236974639/)**

Controversial AI actor Tilly Norwood will 'star' in Misaligned, marking the first time she has lead a feature film.

Deadline • 4h ago

---

**[Tilly Norwood, AI ‘actor’ denounced by actors union, to star in feature film](https://www.nbcnews.com/pop-culture/pop-culture-news/tilly-norwood-ai-actor-denounced-actors-union-star-feature-film-rcna353134)**

Tilly Norwood creator Particle6 Productions said the movie will be a comedy-drama called “Misaligned.”

NBC News • 3h ago

---

**[AI actor Tilly Norwood to star in first movie](https://www.latimes.com/entertainment-arts/business/story/2026-07-06/ai-actor-tilly-norwood-movie-hollywood-ai)**

AI actor Tilly Norwood will star in her first movie, a comedy drama called "Misaligned."

Los Angeles Times • 32m ago

---

**[Illinois Governor JB Pritzker signs AI bill into law](https://abc7chicago.com/post/illinois-governor-jb-pritzker-sign-ai-bill-law/19457902/)**

Governor JB Pritzker signed a bill into law on artificial intelligence Monday.

ABC7 Chicago • 3h ago

---

---

## HackerNews: "ai"

**[The bottleneck might be the air in the room](https://news.ycombinator.com/item?id=48783117)**

You gather your most expensive people into a room to make your most important decisions. Then, somewhere in the second hour, the room quietly gets worse at making them. Not the people. The room.

⬆️ 819 • 💬 464 • 2d ago • [Mike Bowler](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/)

---

**[New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://news.ycombinator.com/item?id=48796817)**

⬆️ 174 • 💬 108 • 23h ago • [intextbooks.science.uu.nl](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf)

---

**[Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://news.ycombinator.com/item?id=48799256)**

Instead, buy domestic product, and out in the open.

⬆️ 163 • 💬 72 • 18h ago • [readtheline.ca](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)

---

**[Delta flight hit by firework while landing at Midway Airport on Fourth of July](https://news.ycombinator.com/item?id=48797141)**

A Delta flight arriving at Chicago's Midway International Airport on the Fourth of July reportedly made contact with a firework, the airline said.

⬆️ 157 • 💬 363 • 22h ago • [NBC Chicago](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

---

**[AMD Ryzen AI Halo – $4k AI Dev Kit](https://news.ycombinator.com/item?id=48805624)**

Welcome to LTT Labs - your go-to destination for all things tech. Explore comprehensive test results, insightful commentary, and the latest analysis in hardware.

⬆️ 144 • 💬 120 • 3h ago • [LTT Labs](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

---

**[Mark Zuckerberg tells staff that AI agents haven't progressed enough](https://news.ycombinator.com/item?id=48795826)**

At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated.

⬆️ 133 • 💬 2 • 1d ago • [TechCrunch](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/)

---

**[When AI Costs More Than the Engineer](https://news.ycombinator.com/item?id=48801493)**

Anthropic spends 2.3x payroll on compute. Top software firms spend 0.4x. Three scenarios for where the rest of the market lands by 2029.

⬆️ 121 • 💬 105 • 11h ago • [Tomasz Tunguz](https://tomtunguz.com/ai-spend-breakeven-2029/)

---

**[AI has torched the market for junior programmers](https://news.ycombinator.com/item?id=48788361)**

Junior programmers are getting destroyed by AI — down 19%, while devs over 40 thrive. Meanwhile, millions of non-developers are shipping real software without the job title. The credential market collapsed; the activity exploded. The problem: nobody's building the next generation of senior engineers.

⬆️ 100 • 💬 194 • 1d ago • [seldo.com](https://seldo.com/posts/ai-has-torched-the-market-for-junior-programmers/)

---

**[Airplane Boneyards List and Map](https://news.ycombinator.com/item?id=48786284)**

⬆️ 93 • 💬 16 • 2d ago • [airplaneboneyards.com](https://airplaneboneyards.com/airplane-boneyards-list-and-map.htm)

---

**[President pardons 9 for Clean Air violations for 'fixing their car'](https://news.ycombinator.com/item?id=48791091)**

⬆️ 89 • 💬 60 • 1d ago • [msn.com](https://www.msn.com/en-us/news/crime/trump-pardons-9-for-clean-air-violations-for-fixing-their-car/ar-AA27cSkT)

---

---

## YouTube Videos: "ai"

**[Scott Galloway on Why Most AI Stocks Are About to Get Crushed](https://www.youtube.com/watch?v=6s_ytILF3GI)**

Scott Galloway breaks down why AI spending is soaring while ROI lags, weighs in on whether Cannes Lions is worth it for young ...

📺 The Prof G Pod – Scott Galloway

👁️ 5K • 👍 275 • 💬 22 • ⏱️ 19:56 • 2h ago

---

**[Trump HUMILIATED As July 4th AI Slopaganda Memes GO VIRAL!](https://www.youtube.com/watch?v=Kbqvi3rK73c)**

Really American Host Steve Harness Breaks Down Trump HUMILIATED By Viral July 4th AI Slopoganda meme's! Support the ...

📺 Really American

👁️ 445K • 👍 18K • 💬 865 • ⏱️ 9:00 • 2d ago

---

**[Why America Will Probably Nationalise AI](https://www.youtube.com/watch?v=77VXbHl5Zvo)**

Want to restore the planet's ecosystems and see your impact in monthly videos? The first 100 people to join Planet Wild with my ...

📺 TLDR News Global

👁️ 117K • 👍 5K • 💬 827 • ⏱️ 9:07 • 1d ago

---

**[Private Credit Just Burst The $25 Trillion AI Bubble](https://www.youtube.com/watch?v=ktLyXGRHNCk)**

The private credit bust is now starting to spread into AI and the AI buildout which up to now has been mostly financed by these ...

📺 Eurodollar University

👁️ 60K • 👍 3K • 💬 214 • ⏱️ 17:23 • 1d ago

---

**[Hightower&#39;s Stephanie Link: We&#39;re in the early stages of the AI boom](https://www.youtube.com/watch?v=5M_il-xgNlU)**

Stephanie Link, chief investment strategist at Hightower, joins 'Squawk Box' to discuss her market outlook for the second half of ...

📺 CNBC Television

👁️ 8K • 👍 158 • 💬 53 • ⏱️ 2:53 • 4h ago

---

**[Jackie DeAngelis: This is a &#39;MASSIVE GROIN PUNCH&#39; in US&#39; AI race against China](https://www.youtube.com/watch?v=EGAqQXVbqAc)**

'The Big Money Show' discusses China's AI advancements, highlighting the threat and implications to the United States' ...

📺 Fox Business

👁️ 102K • 👍 2K • 💬 589 • ⏱️ 15:20 • 2d ago

---

**[The SIMPLEST Claude AI Business Ideas For Beginners (Overlooked)](https://www.youtube.com/watch?v=RjKVB3MwdSw)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 In ...

📺 Max Max

👁️ 6K • 💬 7 • ⏱️ 40:06 • 4h ago

---

**[Qwen 3.6 + Pi Agent: Build Your Own AI Assistant (Full Setup)](https://www.youtube.com/watch?v=7KwoyDzxEuk)**

In this video I build an AI employee that runs my customer support inbox using Pi (pi.dev), the open source agent harness that ...

📺 Bart Slodyczka

👁️ 1K • 👍 47 • 💬 3 • ⏱️ 10:57 • 6h ago

---

**[Grok AI Was Asked Who Built the Pyramids - The Answer Shocked Everyone](https://www.youtube.com/watch?v=A4cY1bCgC_A)**

There is a structure standing in the desert outside Cairo that, by every measure of physics and mathematics, should not exist.

📺 New Discovery

👁️ 95K • 👍 1K • 💬 199 • ⏱️ 30:44 • 1d ago

---

**[Turn NotebookLM into Long AI Video Engine (FREE)](https://www.youtube.com/watch?v=7ufIdzIyYGA)**

This video was made using my Faceless YouTube Engine system. You can get the full guide here ...

📺 The AI Garage

👁️ 8K • 👍 447 • 💬 22 • ⏱️ 11:44 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,617,508 • ❤️ 1,620 • 8d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 231,218 • ❤️ 3,519 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,070,230 • ❤️ 1,785 • 3d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 8,766 • ❤️ 335 • 3d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 436,780 • ❤️ 751 • 11d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 2 • ❤️ 284 • 4h ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 430,676 • ❤️ 285 • 6d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 7,036 • ❤️ 250 • 2d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 370,884 • ❤️ 1,043 • 17d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 14,276 • ❤️ 407 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,451 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 105 • 💬 4 • ⭐ 91,306 • 18mo ago

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

▲ 251 • 💬 4 • ⭐ 11,056 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

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

▲ 8 • 💬 0 • ⭐ 5,271 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,631 • 23mo ago

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

**[OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation](https://huggingface.co/papers/2410.17799)**

*Qinglin Zhang, Luyao Cheng, Chong Deng et al. (9 authors)*

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.

▲ 16 • 💬 1 • ⭐ 60,825 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.17799) • [💻 code](https://github.com/karpathy/nanogpt)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,503 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 75.8k • 🔱 4.0k • 4d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.5k • 🔱 1.1k • 3h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.4k • 🔱 841 • 2h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 6.2k • 🔱 791 • 3h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.5k • 🔱 216 • 3d ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 2.5k • 🔱 590 • 1h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.4k • 🔱 184 • 3d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.0k • 🔱 72 • 12h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 90 • 23d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.4k • 🔱 133 • 29d ago

---

---

*Generated by PeekDeck - A glance is all you need*
