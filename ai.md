---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-07T05:38:30.607766+00:00'
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

**Last Updated:** July 07, 2026 at 05:38 UTC  
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

**[SpaceX burned up 260 of its own satellites in 6 months and this is just routine apparently](https://www.reddit.com/r/artificial/comments/1upbdoa/spacex_burned_up_260_of_its_own_satellites_in_6/)**

Saw this in an article and it's been on my mind since 260 satellites intentionally burned in the atmosphere in 6 months and another 349 queued. They're planning 42,000 total eventually. No debris which is fine but researchers are asking what happens when you're burning hundreds of massive metal objects in the upper atmosphere repeatedly over years. Aluminum particles, potential atmospheric chemistry changes. Science is still catching up and the FCC is now proposing to exempt satellites from environmental review entirely Idk,we're moving faster than we're studying this...anyone else find this a bit much?

7h ago

---

**[AI should be private and optional!](https://www.reddit.com/r/artificial/comments/1uplbps/ai_should_be_private_and_optional/)**

AI should be private and optional.

31m ago

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don’t Exist](https://www.reddit.com/r/artificial/comments/1upfz1n/scammers_sell_seeds_for_exotic_aigenerated/)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

🔗 [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/) • 4h ago

---

**[you can just watch a language model think now. i built a way to visualize the words AI doesn’t say](https://www.reddit.com/r/artificial/comments/1upejv3/you_can_just_watch_a_language_model_think_now_i/)**

anthropic published the J-space paper today. tl;dr: models have a small emergent set of internal “silent words” (~a few dozen concepts at a time, <10% of activations) that they can report on, control, and use for reasoning. the measurement tool is the jacobian lens and they open sourced it, and neuronpedia posted pre-fitted lenses for qwen. so the obvious next step was to wire it into a chat UI and just… look at it. subtext runs qwen3.5-4B in bf16 on a single 12GB GPU and reads the lens at 9 layers on every token — both while the model reads your message and while it replies. streams at full generation speed (the lens is just a matmul + unembed per layer, basically free). favorite moment: type “is this correct? 12 + 5 = 1” and incorrect lights up mid-network while it’s still reading the equation. zero reply tokens exist at this point. the verdict is just sitting there, internally, before the model says anything. repo: https://github.com/ninjahawk/Subtext no GPU: recorded session replays in the browser: https://ninjahawk.github.io/Subtext/ paper: https://www.anthropic.com/research/global-workspace the live readout path is verified against anthropic’s reference implementation — audit script in the repo, top-5 matches exactly at every layer/position tested, cosine 0.99998. that’s it. questions welcome.

5h ago

---

**[Can AI help with the emotional emptiness people feel in modern life?](https://www.reddit.com/r/artificial/comments/1up0k2f/can_ai_help_with_the_emotional_emptiness_people/)**

I’ve been thinking about something less technical about AI. In many ways, people’s living standards are getting better. We have better tools, more convenience, more entertainment, and access to more information than before. But at the same time, it feels like many people are still emotionally empty, confused, or lost. Even with better material conditions, people still seem to be searching for meaning, direction, connection, or some kind of inner stability. In some ways, the faster the world develops, the more confused people seem to become. So I’m curious: Can AI actually help with this kind of emotional emptiness or confusion? Not as a replacement for real relationships, therapy, or human connection, but maybe as a tool for reflection, journaling, self-understanding, or organizing thoughts. Or does AI only make people feel temporarily understood while the deeper problem remains? Have you ever used AI to deal with loneliness, confusion, lack of direction, or questions about meaning? Did it actually help?

14h ago

---

**[Please help - I saw a reel about how to better use Anthropic models in tandem with something on your local desktop. I thought it was very motivating and exciting, but now I cant find the reel again, and I don't even know the search terms to use to search for it](https://www.reddit.com/r/artificial/comments/1uphaxt/please_help_i_saw_a_reel_about_how_to_better_use/)**

I know part of it was about persistent memory, using files stored on your local machine, and part of it was about how to make your agents better and more useful by something saved on your local machine, and there were other cool sounding features, something about ways to save tokens, but I don't remember the rest. I see there is "no tool request" rule, so can someone without saying a product name, just say what the category name for this type of tool is? or what search terms to use find stuff on this topic? thanks

3h ago

---

**[Benchmarks compare open models against closed products, not closed models. We might be missing what were actually paying for](https://www.reddit.com/r/artificial/comments/1uovy56/benchmarks_compare_open_models_against_closed/)**

So this has been on my mind for a while and it kinda bugs me. Every time someone benchmarks glm-5.2 or deepseek against claude or gpt, the closed one wins on some tasks and people just assume the underlying model is smarter. but thats not really what were measuring. We dont know what these closed providers actually do behind the api. they might be running rag over their own docs, injecting hidden system prompts based on your query, routing to specialized expert models depending on task type, doing prompt preprocessing we never see, hitting internal tool calls before the model even generates a response. anthropic already hides reasoning traces and doesnt show you the full pipeline. we get the polished output and we assume its just the model. Meanwhile when you benchmark an open model youre benchmarking raw inference. no scaffolding, no hidden tools, no preprocessing. its like comparing a cars engine on a dyno to another car actually driving on a road with traction control and abs and lane assist. the road one looks better but its not because the engine is stronger. Which makes me wonder if the actual model quality gap between the frontier closed stuff and something like glm-5.2 is way smaller than benchmarks suggest. What you are paying premium for might be the tooling and the harness wrapped around it, not the raw model. and if thats true this whole industry is heading somewhere weird, because tooling is way easier to replicate than model architecture, and open weights plus open source tooling starts to look really competitive really fast. There is a broader thing going on too. software engineering hasnt actually changed in principle, its still specs, architecture, tradeoffs, maintainability. what changed is the volume. line by line code review doesnt scale when agents produce diffs at this rate, so review has to move upstream to specs and downstream to tests, metrics, traces, observability. thats where the actual verification happens now, not in the middle where volume already broke it. So heres what i am stuck on. when we say model X is better than model Y based on benchmarks, are we actually comparing model to model, or are we comparing raw inference against everything the closed provider bolted onto it that we cant see, and does that distinction even matter to anyone anymore.

17h ago

---

**[I built a Claude agent that runs Instagram DM ordering for a 7-location sushi chain](https://www.reddit.com/r/artificial/comments/1uorq6d/i_built_a_claude_agent_that_runs_instagram_dm/)**

I built an AI agent that took over order-taking for a sushi chain with 7 locations. About 90% of their orders come through Instagram DMs, and until now one person typed every reply by hand. How it works: code watches incoming messages through the Meta API and hands each one to Claude (Sonnet 4.6) over the API. The model has a knowledge base with the full menu, ingredients, calories, allergens, delivery zones, hours, prep times and promos for all 7 spots. It talks to the customer for real, helps them pick, explains what is in a roll, flags allergens, and upsells when it fits ("that set goes well with X sauce, want it?"). Once an order is confirmed it pushes straight to the kitchen and writes a record into the restaurant CRM and an admin panel where the owner watches how the agent is doing. Stack: SvelteKit for the site and admin panel, Meta API for the DMs, Claude Sonnet 4.6 for the conversations, pg-boss on Postgres for the job queue, and a CRM integration for the orders. One detail I am happy with: that whole menu-and-rules block has to go to the model on every message, which would normally be expensive. With prompt caching, about 97% of messages read that block from cache at a tenth of the input price, so running Sonnet on every DM ends up cheap enough that the owner never thinks about it. What it doesn't do, by choice: calls, voice notes and photos go to a human. A model guessing at a photo of a handwritten order is how you ship something embarrassing. Plain text handoffs almost never happen, basically just "let me talk to a human," and that is rare. The owner's panel keeps every chat plus the agent's reasoning chain per message, so if something breaks I can see exactly how and why. Still watching quality now that it is live. Happy to answer anything about the caching setup, the Meta API webhook flow, or how the kitchen handoff works.

20h ago

---

**[Are returns a fair way to judge the quality of Artificial Intelligence decision making when things are not certain?](https://www.reddit.com/r/artificial/comments/1upaw6u/are_returns_a_fair_way_to_judge_the_quality_of/)**

Artificial Intelligence systems are becoming more able to act on their own and make decisions that affect the world. We need to find ways to figure out if these decisions are good or not. Financial markets are a place to test this because they are very unpredictable and people are working against each other. There is also a lot of uncertainty. We do not always know right away if a decision was good or not. These are the kinds of conditions that Artificial Intelligence will have to deal with as it starts making complicated decisions. The problem is that most of the time we judge Artificial Intelligence systems by how money they make or lose.. In situations like this a good decision can still result in a loss because of things that the Artificial Intelligence system cannot control.. Sometimes a bad decision can work out just by luck. This makes me wonder about the picture of Artificial Intelligence and how we can make it even smarter. How can we really know if an Artificial Intelligence system is making decisions when things are not certain instead of just looking at the results? Are there any new ideas or tests being developed that can separate the quality of the decision making process from the actual results? I am especially interested, in ideas that work well in situations where we have to make decisions over a period of time and there is a lot of uncertainty. I would really like to hear what people think about this.

8h ago

---

**[The cheapest option for coding with AI](https://www.reddit.com/r/artificial/comments/1upafyz/the_cheapest_option_for_coding_with_ai/)**

I recently subscribed to OpenCode Go and wrote a post about my experience. I hope you find it useful: https://byandrev.dev/en/blog/the-cheapest-way-to-code-with-ai/

8h ago

---

---

## Google News: "ai"

**[AI Giants Are Handing Out Tons of Free Computing Power to Grab Startup Share](https://www.wsj.com/tech/ai/ai-giants-are-handing-out-tons-of-free-computing-power-to-grab-startup-share-c00a5c5c)**

WSJ • 4h ago

---

**[AI actor Tilly Norwood set to star in first feature film](https://www.cbsnews.com/news/tilly-norwood-ai-generated-actor-feature-film/)**

AI-generated actor Tilly Norwood is set to star in her first feature film, with her creator saying that "art will be imitating life."

CBS News • 11h ago

---

**[Tilly Norwood to Lead New Movie ‘Misaligned,’ Marking Feature Debut for AI ‘Actor’](https://variety.com/2026/film/global/ai-actor-tilly-norwood-movie-debut-misaligned-1236802325/)**

Tilly Norwood, the controversial AI actor, is to front her first feature film, the comedy-drama Misaligned from AI studio Particle6

Variety • 16h ago

---

**[Tilly Norwood, AI ‘actor’ denounced by actors union, to star in feature film](https://www.nbcnews.com/pop-culture/pop-culture-news/tilly-norwood-ai-actor-denounced-actors-union-star-feature-film-rcna353134)**

Tilly Norwood creator Particle6 Productions said the movie will be a comedy-drama called “Misaligned.”

NBC News • 8h ago

---

**[Chinese AI models are gaining ground with U.S. companies as OpenAI, Anthropic costs surge](https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html)**

Recent model releases from Chinese companies including DeepSeek and Z.ai are seen by many as highly competitive compared to leading U.S. frontier systems.

CNBC • 38m ago

---

**[Why A.I. Distillation Has Become a Hot Topic in the Race with China](https://www.nytimes.com/2026/07/06/technology/ai-distillation-china.html)**

The New York Times • 13h ago

---

**[Inside the secret AI war between Silicon Valley and China](https://www.washingtonpost.com/national-security/2026/07/06/why-anthropic-alleges-chinese-firms-are-distilling-knowledge-claude/)**

American tech firms say rivals are forcing their chatbots to act as tutors to make Chinese AI smarter.

The Washington Post • 13h ago

---

**[5 Ways To Build An AI-Positive Workplace Before Fear Takes Over](https://www.forbes.com/sites/bernardmarr/2026/07/07/5-ways-to-build-an-ai-positive-workplace-before-fear-takes-over/)**

Here are five practical steps business leaders can take to build an AI-positive corporate culture that encourages innovation while addressing risk, fear and uncertainty.

Forbes • 27m ago

---

**[Dollar Shave Club’s bet: AI makes agencies optional, not obsolete](https://digiday.com/marketing/dollar-shave-clubs-bet-ai-makes-agencies-optional-not-obsolete/)**

Dollar Shave Club already makes 90% of its advertising in-house. Its new brand boss wants AI to close the rest of the gap.

Digiday • 1h ago

---

**[Asian Markets Retreat After Rebounding AI Stocks Send the S&P 500 to Brink of a New Record](https://www.usnews.com/news/business/articles/2026-07-07/asian-markets-retreat-after-rebounding-ai-stocks-send-the-s-p-500-to-brink-of-a-new-record)**

Asian shares have retreated despite a rebound for AI stocks that lifted stocks on Wall Street

U.S. News & World Report • 36m ago

---

---

## HackerNews: "ai"

**[The bottleneck might be the air in the room](https://news.ycombinator.com/item?id=48783117)**

You gather your most expensive people into a room to make your most important decisions. Then, somewhere in the second hour, the room quietly gets worse at making them. Not the people. The room.

⬆️ 820 • 💬 465 • 2d ago • [Mike Bowler](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/)

---

**[AMD Ryzen AI Halo – $4k AI Dev Kit](https://news.ycombinator.com/item?id=48805624)**

Welcome to LTT Labs - your go-to destination for all things tech. Explore comprehensive test results, insightful commentary, and the latest analysis in hardware.

⬆️ 303 • 💬 218 • 14h ago • [LTT Labs](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

---

**[GLM 5.2 and the coming AI margin collapse](https://news.ycombinator.com/item?id=48809877)**

GLM 5.2 is the first open weights model I'd call a genuine competitor to Opus and GPT for agentic work - at ~15-20% of the price. Part one of why AI inference margins are about to collapse.

⬆️ 269 • 💬 182 • 9h ago • [Martin Alderson](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

---

**[New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://news.ycombinator.com/item?id=48796817)**

⬆️ 176 • 💬 111 • 1d ago • [intextbooks.science.uu.nl](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf)

---

**[Delta flight hit by firework while landing at Midway Airport on Fourth of July](https://news.ycombinator.com/item?id=48797141)**

A Delta flight arriving at Chicago's Midway International Airport on the Fourth of July reportedly made contact with a firework, the airline said.

⬆️ 168 • 💬 383 • 1d ago • [NBC Chicago](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

---

**[Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://news.ycombinator.com/item?id=48799256)**

Instead, buy domestic product, and out in the open.

⬆️ 163 • 💬 75 • 1d ago • [readtheline.ca](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)

---

**[OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files](https://news.ycombinator.com/item?id=48807225)**

OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation req...

⬆️ 152 • 💬 40 • 12h ago • [GitHub](https://github.com/iOfficeAI/OfficeCLI)

---

**[Mark Zuckerberg tells staff that AI agents haven't progressed enough](https://news.ycombinator.com/item?id=48795826)**

At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated.

⬆️ 133 • 💬 2 • 1d ago • [TechCrunch](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/)

---

**[When AI Costs More Than the Engineer](https://news.ycombinator.com/item?id=48801493)**

Anthropic spends 2.3x payroll on compute. Top software firms spend 0.4x. Three scenarios for where the rest of the market lands by 2029.

⬆️ 124 • 💬 109 • 22h ago • [Tomasz Tunguz](https://tomtunguz.com/ai-spend-breakeven-2029/)

---

**[AI has torched the market for junior programmers](https://news.ycombinator.com/item?id=48788361)**

Junior programmers are getting destroyed by AI — down 19%, while devs over 40 thrive. Meanwhile, millions of non-developers are shipping real software without the job title. The credential market collapsed; the activity exploded. The problem: nobody's building the next generation of senior engineers.

⬆️ 100 • 💬 194 • 2d ago • [seldo.com](https://seldo.com/posts/ai-has-torched-the-market-for-junior-programmers/)

---

---

## YouTube Videos: "ai"

**[The Dirty AI lie : How the GREATEST bet in human history started to crack in June 2026?](https://www.youtube.com/watch?v=WcckBmkauBQ)**

Check out Odoo: https://www.odoo.com/r/ChAT ⭐️ Think School's flagship Communication course with live doubt sessions ...

📺 Think School

👁️ 439K • 👍 17K • 💬 828 • ⏱️ 20:53 • 14h ago

---

**[Grok AI Was Asked Who Built the Pyramids - The Answer Shocked Everyone](https://www.youtube.com/watch?v=A4cY1bCgC_A)**

There is a structure standing in the desert outside Cairo that, by every measure of physics and mathematics, should not exist.

📺 New Discovery

👁️ 341K • 👍 4K • 💬 588 • ⏱️ 30:44 • 1d ago

---

**[AI expert worries about the risk of humans losing control | Four Corners](https://www.youtube.com/watch?v=gYORRh377Gw)**

Jeffrey Ladish consulted on security for AI giant Anthropic. Now as Executive Director at Palisade Research he tests AI agents and ...

📺 ABC News In-depth

👁️ 16K • 👍 484 • 💬 63 • ⏱️ 15:06 • 20h ago

---

**[Why America Will Probably Nationalise AI](https://www.youtube.com/watch?v=77VXbHl5Zvo)**

Want to restore the planet's ecosystems and see your impact in monthly videos? The first 100 people to join Planet Wild with my ...

📺 TLDR News Global

👁️ 130K • 👍 5K • 💬 889 • ⏱️ 9:07 • 1d ago

---

**[Jackie DeAngelis: This is a &#39;MASSIVE GROIN PUNCH&#39; in US&#39; AI race against China](https://www.youtube.com/watch?v=EGAqQXVbqAc)**

'The Big Money Show' discusses China's AI advancements, highlighting the threat and implications to the United States' ...

📺 Fox Business

👁️ 108K • 👍 2K • 💬 617 • ⏱️ 15:20 • 2d ago

---

**[Can a $125,000 robot really be your friend? #robotcompanions #humanoidrobot #aihumanoid #AI](https://www.youtube.com/watch?v=tkyxYDolA8I)**

Business Insider is a global newsroom covering business, technology, innovation, and the economy. Visit our homepage for the ...

📺 Business Insider

👁️ 2K • 👍 35 • 💬 8 • ⏱️ 2:32 • 10h ago

---

**[REAL or AI? 🤔](https://www.youtube.com/watch?v=8q9TFijshwE)**

📺 Liv Swearingen (LIV)

👁️ 372K • 👍 14K • 💬 3K • ⏱️ 0:14 • 14h ago

---

**[Trump HUMILIATED As July 4th AI Slopaganda Memes GO VIRAL!](https://www.youtube.com/watch?v=Kbqvi3rK73c)**

Really American Host Steve Harness Breaks Down Trump HUMILIATED By Viral July 4th AI Slopoganda meme's! Support the ...

📺 Really American

👁️ 491K • 👍 18K • 💬 903 • ⏱️ 9:00 • 2d ago

---

**[I Tested AI&#39;s Morality 🤯](https://www.youtube.com/watch?v=JkLjf4pJi9w)**

📺 Zack D. Films

👁️ 7.0M • 👍 530K • 💬 10K • ⏱️ 0:55 • 1d ago

---

**[#HumanoidRobot #RobotAttack #Indonesia #AI #ArtificialIntelligence #Robotics #RobotNews #ViralVideo](https://www.youtube.com/watch?v=f9nSkuew-8E)**

CSB IAS ACADEMY OFFICIAL Youtube Channel Link ...

📺 Bala Latha Madam

👁️ 6K • 👍 247 • 💬 1 • ⏱️ 0:55 • 13h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,617,508 • ❤️ 1,662 • 8d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 231,218 • ❤️ 3,543 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,070,230 • ❤️ 1,799 • 4d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 2 • ❤️ 362 • 15h ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 8,766 • ❤️ 349 • 3d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 430,676 • ❤️ 296 • 6d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 436,780 • ❤️ 760 • 11d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 7,036 • ❤️ 260 • 2d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 370,884 • ❤️ 1,055 • 17d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 2,903 • ❤️ 179 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 105 • 💬 4 • ⭐ 91,396 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,496 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 251 • 💬 4 • ⭐ 11,174 • 1mo ago

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

▲ 8 • 💬 0 • ⭐ 5,475 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 73,620 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 3 • ⭐ 10,052 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,673 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 13 • 💬 2 • ⭐ 18,878 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,548 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 13 • 💬 1 • ⭐ 10,422 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 76.1k • 🔱 4.0k • 3h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.6k • 🔱 1.1k • 19m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.5k • 🔱 859 • 2m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 6.3k • 🔱 803 • 14h ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 2.7k • 🔱 647 • 13h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.5k • 🔱 215 • 3d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.1k • 🔱 76 • 9h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 90 • 23d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.4k • 🔱 121 • 8d ago

---

**[apple/coreai-models](https://github.com/apple/coreai-models)**

Model export recipes, Python primitives, and Swift runtime utilities for on-device AI

`Swift`

⭐ 1.3k • 🔱 108 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
