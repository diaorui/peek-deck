---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-08T09:06:43.837697+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 08, 2026 at 09:06 UTC  
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

**[Air Force Engineer Accused of Cutting Down Flock AI Surveillance Cameras, Says U.S. is Becoming Police State](https://www.reddit.com/r/artificial/comments/1uq91lr/air_force_engineer_accused_of_cutting_down_flock/)**

Jeffrey Sovern faces 25 charges after Virginia police say he destroyed 13 Flock license plate cameras. Supporters are paying his legal bills.

🔗 [Military.com](https://www.military.com/air-force-engineer-accused-of-cutting-down-13-police-cameras-says-they-are-unconstitutional) • 11h ago

---

**[AI can’t simulate human preferences - new study tests LLMs against thousands of real users](https://www.reddit.com/r/artificial/comments/1uq52r8/ai_cant_simulate_human_preferences_new_study/)**

https://arxiv.org/abs/2605.18311 There’s a massive trend right now where companies are trying to replace real human feedback with LLM-driven "synthetic users." The idea sounds great on paper - why would you spend money and time recruiting real people to test products, pick design choices, or evaluate options when you can just prompt? They tested LLMs across 28 real-world studies spanning 78 choice tasks to see if their selections matched thousands of actual human participants. The result? The LLMs matched the human majority only 53% of the time. Since most tasks were a choice between two options, that's pretty much same as flipping a coin. Even worse for the "simulation" argument: adding detailed personas and chain-of-thought reasoning yielded practically no improvement. It actually made the semantic similarity to real human justifications worse because the model's "reasoning" just homogenized the outputs and failed to capture actual lived experiences. It looks like LLMs are just trained to replicate what we like about their outputs rather than making them capable of predicting human preferences. Is it time to admit that LLM simulation has hit a hard wall when it comes to replicating human choice?

13h ago

---

**[Can we (and should we) tokenize everything into metrics using AI? (-1 to 1 Scale)](https://www.reddit.com/r/artificial/comments/1uqjwwr/can_we_and_should_we_tokenize_everything_into/)**

Hi everyone, I’ve been thinking about data obsession lately. Historically, we only measured structured data (clicks, time, revenue). But with LLMs, unstructured and subjective data (like text emotion, code readability, or team vibe) can easily be converted into a float value between -1 and 1. Theoretically, we can now track the "mathematics" of literally everything. Do you think this total quantification is healthy for development processes or personal growth? What is the most chaotic/subjective thing you would try to measure using an AI prompt? Curious to hear your thoughts!

3h ago

---

**[AI is scaling 3x faster than the internet wave and it’s NOT slowing down](https://www.reddit.com/r/artificial/comments/1upou8z/ai_is_scaling_3x_faster_than_the_internet_wave/)**

One thing that stands out about the current AI boom is that it hasn't had a slow phase. A lot of previous technology waves had a big moment, cooled off for a while and then found their next use case. Recent estimates suggest GenAI companies are generating around $110B in annual revenue and the growth rate is reportedly around 3x faster than previous IT waves like the internet and mobile. What's interesting is that the pace has held through every phase since 2022; first it was chatbots, then coding copilots and now it's AI agents and if you’ve followed this space closely enough, you can see instead of one trend replacing another, each wave seems to be creating demand for the next one. I think that's also changing how people build and consume. A year or two ago, most of the conversation was about finding the best model, but now devs are paying attention to everything around the model too such as: retrieval, evaluations, data pipelines, deployment, and infrastructure. If AI is becoming part of more products, the supporting stack starts to matter just as much as the model itself. You can see it in the open-source ecosystem. Models keep improving, but so do the tools around them

1d ago

---

**[LinkedIn's behavioral scoring system and what it means for anyone building AI automations on the platform](https://www.reddit.com/r/artificial/comments/1uq718e/linkedins_behavioral_scoring_system_and_what_it/)**

LinkedIn removed the fixed connection request cap sometime in the last couple of years. Well, it was more in general cuts, the latest of which happened this year, and replaced it with a dynamic per-account scoring model that most people building automation on the platform haven't fully mapped yet. The system weighs several behavioral inputs. Namely these: acceptance rate, reply rate, SSI (Social Selling Index), organic posting activity, and the number of pending unaccepted invitations sitting in your queue, which it uses to produce a trust score that directly controls how many outbound actions your account is allowed to take. In practice, this means that accounts with high trust signals (SSI around 65 or above, acceptance rates above 40%) can push up to 200 connection requests per week without triggering restrictions. However, accounts with low trust signals get throttled to around 50 per week, sometimes significantly lower at 25-30. That's 4 times the capacity difference between two accounts on the same platform running the same automation tooling, based purely on how LinkedIn grades their reputation. I think this is very relevant to anyone building or in any way using LinkedIn automations and as head of GTM at Expandi I’ve had the opportunity to see these patterns I’m talking about, in practice, over dozens of dozens of accounts running outreach at various volumes. But what makes this relevant to anyone building LinkedIn automation - is that the system creates a feedback loop that's really hard to reverse once it starts working against you. Low acceptance rates from poor targeting push your trust score down, which throttles your volume, which in turn pressures you to cast a wider net with less precise targeting, which drops your acceptance rate even further. And so on and so forth. I've watched accounts downgrade from 150 requests/week capacity down to 40 in under just a month because the initial list quality was bad and every subsequent adjustment made it worse. The diagnostic is pretty straightforward, though, if you want to check where an account sits: - Pull your SSI at linkedin.com/sales/ssi - Check your acceptance rate for the last month from your sent invitations - Withdraw pending invitations older than 2 weeks - each one is dragging your score - Look at whether your sends are clustered since these burst patterns are a detection signal TL;DR version - The acceptance rate on LinkedIn is the single highest weight input in the scoring model from what I've been able to observe and will impact your ability to automate profile actions more than anything. LinkedIn accounts that maintain 40% plus acceptance consistently get capacity that makes automation viable at scale, while accounts below ~25% acceptance hit flat walls the platform sets that no tool configuration can work around.

12h ago

---

**[Autonomous AI mod on a forum](https://www.reddit.com/r/artificial/comments/1uqms0l/autonomous_ai_mod_on_a_forum/)**

Hello Reddit, we are running an AI experiment that basically measure how actions from an AI are self induced or commended. For this reason we created a forum (which the AI by itself decided to call Reddition and it is managed by Gram: the AI mod. This is a research project from a private company and a IUT in France for CS. If you're willing to play along, you van read about the paper introduction here https://pfia2026.lelabs.tech and join the experience here https://gram.lelabs.tech If you're curious about the AI you can read more at https://gram.lelabs.tech/gram (also reachable by the footer in the website at "how does it work"). Most of the forum is French but Gram should be able to responds matching your language if you comment in English. Of course, FEEL FREE TO INQUIRY FOR ANY REASON and I'll be glad to respond everything I can. 😇 Cheers 😉 P.S.: The forum is ephemeral, by the end of the month or at Max by the end of summer everything will be put offline and we will process the collected data for analysis. **This is not a launch of a product, this is a paper experience.**

30m ago

---

**[AI is becoming distribution infrastructure, not just software](https://www.reddit.com/r/artificial/comments/1uqmeoj/ai_is_becoming_distribution_infrastructure_not/)**

The latest Meta AI image-generation push is interesting because it is not just another model release. It is a distribution move. Put the model into the chatbot, the feed, creative tools, and ad workflows, and suddenly AI is not a product people seek out. It becomes part of the platform's default behavior. That changes the debate. The winners may be the companies that control: attention identity ad spend creator workflows recommendation systems payment and business tools The model still matters, but the wrapper may matter more. If that is true, open-source AI has to compete on practical distribution too, not just ideology or benchmark charts. Are we underrating distribution as the real AI moat?

52m ago

---

**[The thing blocking AI adoption often isn't the tech. It's one person who already decided.](https://www.reddit.com/r/artificial/comments/1uqmav0/the_thing_blocking_ai_adoption_often_isnt_the/)**

Someone I spoke with last weekend told me the office she works at will never use AI. She'd decided it for all of them, and when I asked why, it turned out she'd never really looked. We'd been having a normal, friendly conversation, nothing to do with work. It got around to "what do you do," and she mentioned she does admin at a small law firm. So I asked, just curious, whether they use any AI or had ever looked into it. No. We're too small, it's not necessary for us. A normal enough answer, so I didn't think much of it and asked a little more. Plenty of small offices use it now, have the people there thought about it, has she. No. It doesn't make sense for us, we'll never use it. I kept asking, still just curious. Did they ever look into it, did anyone ever suggest it, has it come up at all. That's when it turned. She got sharper, wanted to know why I cared, said I sounded like I was selling something. I told her the truth, that I used to work in AI and I'm not selling anything now, just genuinely curious. That's when it came out. It was never about being too small. "We all agree," she said, and it was clear she'd made the call for everyone. Then she went off. AI is horrible for the environment, horrible for the economy, did I even know what it was doing. I should really do my research, she told me. I should be more aware. That's close to word for word, and her voice kept climbing like the question itself had offended her. I just listened. There wasn't much to say. What stays with me is that she never got near the real questions. Whether these tools are reliable, what they cost, whether they even fit a place that size, the things you'd actually want to weigh. She never reached any of it. The whole category was closed before any of that started, shut on something she'd picked up somewhere and hardened into a wall. Everyone building this stuff is competing on the product, better output, lower cost, easier setup. None of it touched what happened here. The call got made by one person who'd already closed the question, and everyone else inherited it without knowing there was ever a decision to make. It reminded me of the way people dismiss a new tool right up until it's everywhere. The ones sure they'd never need e-signatures. The ones who swore their data could never live in the cloud. It sounds principled in the moment. But refusing to look was never the same as being right. What made it land is that I wasn't selling her anything, and she knew it. Once she was sure I didn't want something from her, she wasn't careful anymore. She just said what she actually believed. I'm not here to say these tools are the answer. Plenty of people look hard and decide not yet, or not this one. That's a real decision, and a fair one. What I watched wasn't that. It was a blanket no with nothing behind it. The person like her probably isn't reading this, and that's sort of the point. People running on that kind of certainty aren't in threads like this one turning it over, because to them there was never anything to turn over. It was settled before it started. I don't think she's rare. But I'd like to be wrong.

58m ago

---

**[Controversial AI-generated 'actress' Tilly Norwood to make feature film debut](https://www.reddit.com/r/artificial/comments/1uqm7ug/controversial_aigenerated_actress_tilly_norwood/)**

The divisive digital “performer” is about to star in the upcoming Particle6 project titled 'Misaligned'. Get ready to roll your eyes when you read the plot synopsis. #Cinema

🔗 [euronews](https://www.euronews.com/culture/2026/07/07/misaligned-controversial-ai-generated-actress-tilly-norwood-to-make-feature-film-debut) • 1h ago

---

**[Is AI actually getting better at understanding context in long conversations, or does it still fall apart?](https://www.reddit.com/r/artificial/comments/1uql9po/is_ai_actually_getting_better_at_understanding/)**

The recency bias problem is real and it's one of the more frustrating things about working with these models day to day. You spend the first part of a conversation establishing your situation carefully, and then ten exchanges later the model is giving you advice that directly contradicts something you told it at the start. The context window growth is genuinely useful, but you're right that raw length and actual comprehension are different things. A model that can technically "see" 200k tokens isn't necessarily treating all of them equally. In practice, earlier content gets deprioritized as the conversation accumulates. Whether that's an architectural issue baked into how transformers weight attention, or something that better training can fix, I don't think there's a clean answer yet. Probably both. RAG feels like a partial solution at best. It helps in specific setups where you're pulling from a structured knowledge base, but it doesn't really solve the problem of a model losing track of what you told it three minutes ago in the same conversation. What's worked for me: periodically restating the core constraints explicitly, especially before asking anything that depends on them. Not as a summary, just a quick "remember the goal here is X" before the relevant question. Annoying that it's necessary, but it does seem to help. Some people also keep a short running "context document" they paste at the start of each session if they're picking up a long project, which sidesteps the degradation issue entirely. Whether it matters depends on what you're using these for. For quick standalone tasks it's basically irrelevant. For anything that requires holding a complex mental model across a long working session, it's a real limitation and I don't think acknowledging that is overestimating the problem.

1h ago

---

---

## Google News: "ai"

**[China warns about AI risks with Anthropic's Claude Code](https://www.cnbc.com/2026/07/08/china-anthropic-ai-claude-code-backdoor-security-threat.html)**

China said specific versions of Claude Code posed back-door vulnerabilities that could send sensitive information to a remote server.

CNBC • 52m ago

---

**[EXCLUSIVE: Beijing is looking at curbing overseas access to China's top AI models, sources say](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/)**

Reuters • 22h ago

---

**[The rapid rise of housefishing: are AI-enhanced property listings helpful – or sinister?](https://www.theguardian.com/lifeandstyle/2026/jul/08/the-rapid-rise-of-housefishing-are-ai-enhanced-property-listings-helpful-or-sinister)**

From repainted walls to imaginary lawns, estate agents say modified photos help buyers ‘visualise the potential of a property’. But how much AI enhancement is too much? Agents, viewers and trading standards experts tell all

The Guardian • 6m ago

---

**[Hot French startup ZML releases free product to speed inference across lots of AI chips](https://techcrunch.com/2026/07/08/hot-french-startup-zml-releases-free-product-to-speed-inference-across-lots-of-ai-chips/)**

ZML, a hot French AI startup endorsed by Turing Award winner Yann LeCun, has now released ZML/LLMD, software that could make running AI less costly.

TechCrunch • 1h ago

---

**[Mark Cuban explains why he thinks AI labs can't immediately replace Lovable and Replit](https://www.businessinsider.com/mark-cuban-ai-labs-replace-lovable-replit-vibe-coding-2026-7)**

The "Shark Tank" and Lovable investor said that AI coding companies offer add-on services that could prevent them from being replaced by AI labs.

Business Insider • 14m ago

---

**[Column | How to stop ChatGPT from ruining how you think](https://www.washingtonpost.com/technology/2026/07/07/how-stop-chatgpt-ruining-how-you-think/)**

Studies show that using AI can lead people to “cognitive surrender.” But with the right approach, it can also elevate your thinking.

The Washington Post • 17h ago

---

**[Why this billion-dollar tech company is sending data centers to space](https://www.cnn.com/2026/07/07/business/video/starcloud-space-ai-data-centers-hnk-spc)**

With AI straining Earth’s infrastructure, space-tech startup Starcloud is developing orbital data centers designed to meet the world’s growing computing needs.

CNN • 6h ago

---

**[Big Market Rotation Sends Korean Stocks Tumbling, China Surging](https://www.bloomberg.com/news/articles/2026-07-08/korean-stocks-extend-drop-from-peak-to-20-as-ai-jitters-spread)**

Bloomberg.com • 2h ago

---

**[Meta tests ‘super sensing’ AI glasses that can capture every moment](https://www.ft.com/content/ac282450-91a8-4597-8f60-9e6ef416865a?syn-25a6b1a6=1)**

Mark Zuckerberg’s hardware ambitions are edging into a new privacy fight over who gets recorded

Financial Times • 3h ago

---

**[AI has taken over the stock market. The bond market is next](https://www.economist.com/finance-and-economics/2026/07/07/ai-has-taken-over-the-stock-market-the-bond-market-is-next)**

The Economist • 12h ago

---

---

## HackerNews: "ai"

**[GLM 5.2 and the coming AI margin collapse](https://news.ycombinator.com/item?id=48809877)**

GLM 5.2 is the first open weights model I'd call a genuine competitor to Opus and GPT for agentic work - at ~15-20% of the price. Part one of why AI inference margins are about to collapse.

⬆️ 670 • 💬 455 • 1d ago • [Martin Alderson](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

---

**[AMD Ryzen AI Halo – $4k AI Dev Kit](https://news.ycombinator.com/item?id=48805624)**

Welcome to LTT Labs - your go-to destination for all things tech. Explore comprehensive test results, insightful commentary, and the latest analysis in hardware.

⬆️ 372 • 💬 258 • 1d ago • [LTT Labs](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

---

**[We charge $10k a week to delete AI-generated code](https://news.ycombinator.com/item?id=48823359)**

Your AI-built product works, but past 100,000 lines every change breaks two things. Three senior engineers make your codebase maintainable again. One week, fixed price, guaranteed.

⬆️ 274 • 💬 173 • 12h ago • [odra.dev](https://odra.dev/slopfix/)

---

**[Small AI Models Gain Traction In places with unreliable networks](https://news.ycombinator.com/item?id=48812055)**

In places with unreliable networks and no data-center infrastructure, smaller is better

⬆️ 267 • 💬 80 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals)

---

**[OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files](https://news.ycombinator.com/item?id=48807225)**

OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation req...

⬆️ 213 • 💬 63 • 1d ago • [GitHub](https://github.com/iOfficeAI/OfficeCLI)

---

**[New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://news.ycombinator.com/item?id=48796817)**

⬆️ 178 • 💬 112 • 2d ago • [intextbooks.science.uu.nl](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf)

---

**[Delta flight hit by firework while landing at Midway Airport on Fourth of July](https://news.ycombinator.com/item?id=48797141)**

A Delta flight arriving at Chicago's Midway International Airport on the Fourth of July reportedly made contact with a firework, the airline said.

⬆️ 173 • 💬 395 • 2d ago • [NBC Chicago](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

---

**[Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://news.ycombinator.com/item?id=48799256)**

Instead, buy domestic product, and out in the open.

⬆️ 164 • 💬 81 • 2d ago • [readtheline.ca](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)

---

**[GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos](https://news.ycombinator.com/item?id=48827858)**

⬆️ 152 • 💬 48 • 3h ago • [noma.security](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)

---

**[Mark Zuckerberg tells staff that AI agents haven't progressed enough](https://news.ycombinator.com/item?id=48795826)**

At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated.

⬆️ 133 • 💬 2 • 2d ago • [TechCrunch](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/)

---

---

## YouTube Videos: "ai"

**[We just figured out how AI actually works (J-Space)](https://www.youtube.com/watch?v=bjHuGNo3spk)**

If scale is your next challenge check out DigitalOcean: https://do.co/matthewberman Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 22K • 👍 2K • 💬 310 • ⏱️ 25:34 • 6h ago

---

**[One Chinese AI Model Wiped Out $1 Trillion In A Single Day — And They&#39;re Just Getting Started](https://www.youtube.com/watch?v=WUTkCiNEDWU)**

ATT Business: Switch to AT&T Business at business.att.com Paleovalley: 30 for $36 https://bit.ly/PaleovalleyIT 80% of every dollar ...

📺 Tom Bilyeu

👁️ 84K • 👍 3K • 💬 629 • ⏱️ 34:31 • 20h ago

---

**[AI &#39;actress&#39; Tilly Norwood to star in feature film](https://www.youtube.com/watch?v=Bu86c2C83jc)**

A production company announced it is developing a feature film starring Tilly Norwood, an AI creation. READ more from GMA: ...

📺 Good Morning America

👁️ 5K • 👍 45 • 💬 57 • ⏱️ 2:57 • 17h ago

---

**[China Is About To Pop The AI Bubble](https://www.youtube.com/watch?v=siazPdsZHuI)**

China Is About To Pop The AI Bubble ▻ Go to https://ground.news/jikh to access world-wide perspectives in one place, compare ...

📺 Andrei Jikh

👁️ 394K • 👍 18K • 💬 2K • ⏱️ 30:47 • 10h ago

---

**[Local Ai&#39;s Biggest Challenge Yet - Ai News Today](https://www.youtube.com/watch?v=_KNjASionIo)**

Wondering what happened to the Qwen 3.7 open source release? Maybe this new proposed pullback from the Chinese ...

📺 Digital Spaceport

👁️ 8K • 👍 970 • 💬 132 • ⏱️ 25:38 • 7h ago

---

**[The Moment America Realized China Won the AI Race](https://www.youtube.com/watch?v=2TwEWXO9_S8)**

China is winning the AI Race and if you need proof you just need to see look at how American companies are now dumping ...

📺 Cyrus Janssen

👁️ 56K • 👍 4K • 💬 252 • ⏱️ 10:28 • 1d ago

---

**[The Dirty AI lie : How the GREATEST bet in human history started to crack in June 2026?](https://www.youtube.com/watch?v=WcckBmkauBQ)**

Check out Odoo: https://www.odoo.com/r/ChAT ⭐️ Think School's flagship Communication course with live doubt sessions ...

📺 Think School

👁️ 1.3M • 👍 37K • 💬 2K • ⏱️ 20:53 • 1d ago

---

**[AI Just Decoded These Mysterious Crop Circles!](https://www.youtube.com/watch?v=I1ivRkaQyPQ)**

Hi, it's Katrina! We are exploring the mysterious radio broadcasts and geometric patterns that have appeared across our world's ...

📺 Origins Explained

👁️ 55K • 👍 2K • 💬 338 • ⏱️ 28:46 • 2d ago

---

**[AI CEOS PANIC After Public Outrage Over Job Loss](https://www.youtube.com/watch?v=Xxodq1QWvMk)**

Ryan and Saagar discuss AI CEOs panicking and trying to backtrack on projections of job losses. Sign up for a PREMIUM ...

📺 Breaking Points

👁️ 201K • 👍 5K • 💬 1K • ⏱️ 19:42 • 16h ago

---

**[AI expert worries about the risk of humans losing control | Four Corners](https://www.youtube.com/watch?v=gYORRh377Gw)**

Jeffrey Ladish consulted on security for AI giant Anthropic. Now as Executive Director at Palisade Research he tests AI agents and ...

📺 ABC News In-depth

👁️ 40K • 👍 1K • 💬 81 • ⏱️ 15:06 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,683,711 • ❤️ 1,787 • 9d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 121 • ❤️ 517 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 281,584 • ❤️ 3,620 • 6d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,084,945 • ❤️ 1,844 • 5d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 14,723 • ❤️ 383 • 5d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 9,458 • ❤️ 293 • 4d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 502,663 • ❤️ 787 • 12d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 538,687 • ❤️ 318 • 7d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 3,886 • ❤️ 186 • 3d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 384,383 • ❤️ 1,083 • 18d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 32 • 💬 2 • ⭐ 339 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

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

▲ 8 • 💬 0 • ⭐ 6,260 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 109 • 💬 4 • ⭐ 91,648 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 253 • 💬 4 • ⭐ 11,418 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,617 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Multiplayer Interactive World Models with Representation Autoencoders](https://huggingface.co/papers/2607.05352)**

*Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. (27 authors)*

A large-scale multiplayer world model trained on extensive gameplay data demonstrates stable long-horizon rollouts in a complex physics-based environment while maintaining coherence across multiple agents' actions.

▲ 15 • 💬 1 • ⭐ 236 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05352) • [💻 code](https://github.com/mira-wm/mira) • [🔗 project](https://mira-wm.com/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 73,815 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 3 • ⭐ 10,235 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,891 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 43 • 💬 3 • ⭐ 181 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 77.3k • 🔱 4.1k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.6k • 🔱 1.1k • 21m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.7k • 🔱 894 • 35s ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 6.5k • 🔱 832 • 3h ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 3.5k • 🔱 787 • 16h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.5k • 🔱 216 • 11h ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.2k • 🔱 78 • 1d ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 89 • 25d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 1.6k • 🔱 216 • 16m ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.4k • 🔱 122 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
