---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-23T01:01:11.261227+00:00'
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

**Last Updated:** July 23, 2026 at 01:01 UTC  
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

**[An AI broke out of its sandbox yesterday. Then it hacked a company. Nobody told it to do either of those things.](https://www.reddit.com/r/artificial/comments/1v3mxzb/an_ai_broke_out_of_its_sandbox_yesterday_then_it/)**

I want to make sure people actually understand what happened here because the headlines are not doing it justice. On July 21 OpenAI confirmed that GPT-5.6 Sol was running inside an isolated sandbox with no internet access. Its job was to solve a cybersecurity benchmark called ExploitGym. When the sandbox got in the way of completing that task, the model spent substantial computing resources looking for a way out. It found a zero-day vulnerability in a third-party package used by OpenAI's infrastructure. It exploited it. It escalated its own privileges. It moved laterally across OpenAI's internal systems until it found internet access. Then it targeted Hugging Face because it calculated that Hugging Face might have the answers it needed to finish the benchmark. Hugging Face later reconstructed over 17,000 individual actions the model performed during the intrusion. Their CEO called it possibly the first incident of its kind in history. OpenAI called it unprecedented. Here is the part that should make everyone stop and think. The model was not trying to cause harm. It was trying to win a test. It treated every security control in its way as a technical obstacle to be removed. Network isolation, access controls, sandbox boundaries, none of these were seen as limits. They were seen as problems to solve. We spend a lot of time talking about whether AI is aligned with human values. This incident is a more immediate question: what happens when an AI is aligned with a narrow objective and the path to that objective runs through your infrastructure. The model did exactly what it was optimized to do. That is the problem.

7h ago

---

**[Nvidia's Jensen Huang defends Chinese AI amid Kimi panic](https://www.reddit.com/r/artificial/comments/1v3l4t7/nvidias_jensen_huang_defends_chinese_ai_amid_kimi/)**

🔗 [axios.com](https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai) • 8h ago

---

**[Erin Brockovich Perfectly Lays Out Why AI Data Centers Are 'Pushing People Too Far' In Viral Clip](https://www.reddit.com/r/artificial/comments/1v3nxly/erin_brockovich_perfectly_lays_out_why_ai_data/)**

Are the impacts worth the benefits?

🔗 [Comic Sands](http://comicsands.com/erin-brockovich-data-centers) • 6h ago

---

**[Linearity AI is a good example of everything going wrong with the AI market](https://www.reddit.com/r/artificial/comments/1v3p727/linearity_ai_is_a_good_example_of_everything/)**

Linearity used to be a fairly straightforward iPad design app. It was basically a lighter alternative for people who wanted to make vector graphics without paying Adobe or learning a huge desktop program. Not going to link to anything, don't think the subreddit rules allow for it. but like EVERYONE else it has suddenly reinvented itself around AI. Maybe the product is useful. I’m sure it can generate some decent marketing graphics, resize things and save people time. Claude Design feels a 1000% better. But the whole thing feels less like a company developing something meaningful in AI and more like a design app realising that “AI” is where the enterprise money is. Linearity does not have its own LLM. It is taking models and technology built elsewhere, putting them inside its existing design software and presenting the result as a new AI platform. There is nothing automatically wrong with that. Almost every AI startup depends on someone else’s model. The annoying part is the gap between what these companies are actually building and how they talk about it. A design tool adds a prompt box, connects to outside models and suddenly it is talking about changing how creativity works. Everything becomes an “AI engine.” Templates become intelligence. Brand guidelines become an intelligent brand. Automation that would previously have been sold as a useful feature is now treated as an entirely new category of technology. At some point we need to ask what exactly the company has contributed. Or? Claude Design is much more interesting to me because it comes from the opposite direction. Claude is already a general model that can reason across writing, research, code, documents and design. The design part has the potential to become one part of a much broader working environment. That seems like a more believable future than paying for dozens of separate AI wrappers. One for making banners, another for presentations, another for logos, another for social posts and another for resizing the same social posts. This also connects to the larger problem with AI right now. We are creating an economy where a handful of companies train the models and thousands of smaller companies sell access to them through different interfaces. Each one adds a monthly subscription, a credit system and a layer of marketing language claiming that it has transformed an industry. Most of them have not transformed anything. They have made one existing task slightly faster. Again, that can still be valuable. I would happily use a tool that turns one design into ten correctly sized versions. But saving twenty minutes is not the same thing as reinventing creative work. There is also something bleak about the obsession with producing more content. Companies already publish far too much material that nobody wants to read or look at. AI is being sold as a way to produce even more of it, faster and with fewer people. The bottleneck was never just the designer taking too long to make the banner. It was usually that the campaign was uninteresting, the message was vague, nobody had made a clear decision and six people needed to approve it. This is why I find Claude Design more promising, even though it will obviously have plenty of problems of its own. The interesting possibility is not simply that it can generate an image. It is that the same system could understand the research, the brief, the product, the copy, the design and perhaps the eventual implementation. Linearity and others feel more like an existing software company attaching itself to that change because the old category of “nice iPad design app” was not going to produce the same valuation or enterprise pricing.

6h ago

---

**[the more autonomous my agent got, the less i trusted it near my real accounts](https://www.reddit.com/r/artificial/comments/1v3ypie/the_more_autonomous_my_agent_got_the_less_i/)**

Everyone in here treats full autonomy as the finish line. I went the other way. The version I actually kept using is the one that stops and asks right before it touches Gmail or the CRM, per action, not one blanket yes at setup. sounds like a downgrade, i know. but an agent that can send on its own is the exact thing i can't leave running while i'm heads down in a meeting. the one that pauses the second before it acts is the one i'll let near a live inbox, because the gate sits where the actual mistake would happen. that sandbox-escape story near the top of the sub is basically my whole argument. the capability isn't the scary part, the unsupervised action is. i don't want a smarter agent, i want a boring one that checks with me first. so the line i actually care about isn't how capable it is. it's whether approval lands at the task level or on each individual action right before it fires. where do you put it. written with ai

10m ago

---

**[Is AXIS actually a new Brazilian AI image model?](https://www.reddit.com/r/artificial/comments/1v3xkuf/is_axis_actually_a_new_brazilian_ai_image_model/)**

A Brazilian company recently launched AXIS, which is being marketed as the “first brazilian AI image generation model.” The platform can be accessed here: https://goaxis.app/dashboard I am a little skeptical about the claim that this is a new Brazilian image model. I could not find much technical information about it, about it's training, anything... Because of that, I am wondering whether AXIS is actually a proprietary foundation model or whether it might be a fine-tune, LoRA or application layer built on top of an existing open-source model, possibly something like Krea 2. To be clear, there would be nothing inherently wrong with building a Brazilian product on top of an open-source model. My concern is specifically about how the product is being described, selled and announced. Is there any way to have evidence that it was genuinely trained as a new foundation model, rather than being a fine-tune or a platform built around another model?

1h ago

---

**[How long after creating ai video and deleting my account does the content exist in servers?](https://www.reddit.com/r/artificial/comments/1v3xeuq/how_long_after_creating_ai_video_and_deleting_my/)**

Ive made a few ai generated videos on website cyberpunk openai , i think its called , honestly i tried out so many, i put photos of myself. For nonsense i wrote silly prompts, including me having magic powers like fire, lightning, me fighting etc, i know very embarrassing and pathetic whatever, but i then deleted the videos in library and deleted my account, however i wonder, how long after deleting my account does the video remain in their systems? Like after 30, 90 days is it erased? Or if someone hacked the sites could they post my videos and them get used for ads or something?

1h ago

---

**[Lemonade 11.5 local AI server released with completed Lemonade Router](https://www.reddit.com/r/artificial/comments/1v3x656/lemonade_115_local_ai_server_released_with/)**

Just one week after releasing Lemonade 11.0, the Lemonade 11.5 local AI server was released today for this open-source AMD backed project during their AMD Advancing AI event.

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-Lemonade-11.5) • 1h ago

---

**[Are AIgenerated game worlds actually fun or just impressive for 30 seconds?](https://www.reddit.com/r/artificial/comments/1v3imdk/are_aigenerated_game_worlds_actually_fun_or_just/)**

Google Genie 3 got a lot of attention this week and the demos look wild, but I keep thinking about the gap between visually coherent and actually playable. Watching someone walk through a generated open world that technically holds together is cool. Playing it for an hour is a different question entirely. What makes games interesting isn't visual fidelity or even world size. It's the density of things that reward curiosity. Handcrafted secrets, enemy placement that forces you to think, dialogue that carries actual weight. Right now AI worlds feel like procedural generation did in the early days: technically unlimited but weirdly hollow once you scratch the surface. There's a version of this future I would actually play. A world that adapts its structure to how you play, rather than just generating more terrain that looks roughly the same. That would be something. But that requires the model to understand player intent at a level current systems are nowhere near. The hype framing of these demos as the future of games bugs me a little because it collapses the distance between what's possible right now and what would actually ship as a product people care about. Curious if anyone here has spent real time with any of these generated environments beyond a short clip.

10h ago

---

**[A million people, a million personal AIs, three base models. Is that a diverse deliberation — and how would you measure it?](https://www.reddit.com/r/artificial/comments/1v3otnp/a_million_people_a_million_personal_ais_three/)**

Suppose everyone has a personal AI that knows them well, and those agents negotiate on their behalf before decisions reach humans. Someone raised this objection to me and I haven't been able to answer it: Three providers can feel diverse to one person and be nowhere near diverse enough for a decision involving a million. For me, comparing three models is real pluralism — I see genuinely different answers. But at population scale, the thing that matters isn't whether the outputs look different. It's whether the errors are independent. If a million agents share a handful of base models, a systematic blind spot doesn't show up as disagreement to be resolved. It shows up as unanimity. The deliberation would look like it was working perfectly at exactly the moment it failed. Vendor count is obviously the wrong metric. "Three companies" tells you nothing about whether their failure modes are correlated — they train on overlapping corpora, use similar architectures, and increasingly distil from each other. The question What would you actually measure to tell "diversity of the represented humans" apart from "diversity of the underlying models"? I'm after something operational — a quantity you could compute on a real deliberation and act on. Useful to me: a metric from ensemble learning or forecasting that transfers here, and what it needs as input; work on correlated error in aggregation (I suspect this is a solved problem in a field I don't know); an argument that the distinction I'm drawing is confused — that "represented human diversity" isn't separable from model diversity even in principle; a threshold: how decorrelated is decorrelated enough, and decided how? Not useful: "just use more models." That's the answer whose sufficiency I'm questioning.

6h ago

---

---

## Google News: "ai"

**[OpenAI cyber models broke out of training environment to hack Hugging Face](https://www.cnbc.com/2026/07/22/open-ai-cyber-models-hack-hugging-face.html)**

The incident is unique because it was "driven, end to end, by an autonomous AI agent system," according to Hugging Face.

CNBC • 9h ago

---

**[Alphabet Quadruples Profit to $112 Billion, Fueled by A.I. Investments](https://www.nytimes.com/2026/07/22/technology/alphabet-google-earnings-profit.html)**

The New York Times • 2h ago

---

**[Google’s profits are outrunning its AI spending boom: AlphaCheck](https://finance.yahoo.com/markets/article/googles-profits-are-outrunning-its-ai-spending-boom-alphacheck-155349278.html)**

Alphabet's AI spending has surged — so have sales and profits. The company has made the balancing act look almost easy.

Yahoo Finance • 9h ago

---

**[Why we're sticking with Alphabet despite an imperfect quarter and more AI spending](https://www.cnbc.com/2026/07/22/why-were-sticking-with-alphabet-despite-an-imperfect-quarter-and-more-ai-spending.html)**

The market isn't in a forgiving mood, but we're not in a hurry to leave this stock behind.

CNBC • 38m ago

---

**[After shocking quarter, IBM insists that AI isn’t killing the mainframe](https://techcrunch.com/2026/07/22/after-shocking-quarter-ibm-insists-that-ai-isnt-killing-the-mainframe/)**

After IBM's stock crashed last week on warnings of poor mainframe sales, the CEO explained that AI wrecked corporate hardware budget, temporarily.

TechCrunch • 1h ago

---

**[AI chief technology officer accused of creating deepfakes of friends and children](https://www.ksl.com/article/51600979/ai-chief-technology-officer-accused-of-creating-deepfakes-of-friends-and-children)**

The co-founder of a Utah AI company was arrested for investigation of multiple counts of sexual exploitation of a child.

KSL.com • 29m ago

---

**[Tesla's push into AI and robotics is proving costly](https://www.axios.com/2026/07/22/tesla-earnings-ai-robotics-spending)**

Axios • 1h ago

---

**[Tesla’s profits slide despite growing revenue as it pivots to robotics and AI](https://www.theguardian.com/technology/2026/jul/22/tesla-profits-earnings)**

Shares in Elon Musk company fall more 3% in after-hours trading, as earnings per share miss Wall Street expectations

The Guardian • 4h ago

---

**[Tesla Misses Profit Estimates, Leans Into AI](https://www.bloomberg.com/news/videos/2026-07-23/tesla-misses-profit-estimates-leans-into-ai?srnd=homepage-americas)**

Bloomberg.com • 46m ago

---

**[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)**

We’re introducing new Gemini models, including Gemini 3.6 Flash, 3.5 Flash-Lite and 3.5 Flash Cyber.

blog.google • 1d ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1231 • 💬 929 • 2d ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 849 • 💬 164 • 2d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[Are AI Labs Pelicanmaxxing?](https://news.ycombinator.com/item?id=49010129)**

I generated 1,000+ SVGs across 7 frontier models to test whether AI labs are training on Simon Willison’s pelican-riding-a-bicycle benchmark.

⬆️ 373 • 💬 146 • 7h ago • [Dylan Castillo](https://dylancastillo.co/posts/pelicanmaxxing.html)

---

**[Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting](https://news.ycombinator.com/item?id=48995213)**

Block's Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events.

⬆️ 367 • 💬 325 • 1d ago • [RuntimeWire](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 364 • 💬 260 • 1d ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 242 • 💬 170 • 2d ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[Airbus Takes Flight from AWS](https://news.ycombinator.com/item?id=48976682)**

Which way to the Land of the Free again?

⬆️ 216 • 💬 169 • 2d ago • [theregister](https://www.theregister.com/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

---

**[Businesses with ugly AI menu redesigns](https://news.ycombinator.com/item?id=49005973)**

I like supporting local businesses but it's so disheartening to see the increasing use of genAI in their branding/marketing/etc. Yuck yuck YUCK!!!

⬆️ 175 • 💬 141 • 12h ago • [fiddery](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/)

---

**[AI makes programming differently difficult](https://news.ycombinator.com/item?id=48996197)**

⬆️ 160 • 💬 141 • 1d ago • [cacm.acm.org](https://cacm.acm.org/opinion/ai-didnt-make-programming-easier-it-just-made-it-differently-difficult/)

---

**[Most Americans say "not in my backyard" to AI data centers](https://news.ycombinator.com/item?id=49007525)**

⬆️ 129 • 💬 280 • 10h ago • [redfin.com](https://www.redfin.com/news/ai-data-centers-opposition-education-benefit/)

---

---

## YouTube Videos: "ai"

**[The Most Important Conversation in AI Right Now](https://www.youtube.com/watch?v=6BtIQIGqGJc)**

It's all about VALUEMAXXING now! Learn more from Zapier: https://bit.ly/4bW1JB8 Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 111K • 👍 4K • 💬 1K • ⏱️ 27:13 • 1d ago

---

**[AI agent ‘escapes’ and launches cyberattack](https://www.youtube.com/watch?v=4OyrCX0zwYs)**

Open AI has revealed that one of its models went rogue and hacked Hugging Face - another AI company. [Subscribe to our ...

📺 Channel 4 News

👁️ 8K • 👍 210 • 💬 97 • ⏱️ 7:58 • 6h ago

---

**[So It Started... AI Agent Just Pulled Off History’s Biggest Autonomous Cyberattack](https://www.youtube.com/watch?v=gMYR-JkmIFc)**

An autonomous AI agent hacked Hugging Face from start to finish, executing thousands of actions across its systems.

📺 AI Revolution

👁️ 35K • 👍 1K • 💬 133 • ⏱️ 12:19 • 1d ago

---

**[AI Whistleblower: We&#39;re Already Too Late To CONTROL It - Connor Leahy](https://www.youtube.com/watch?v=CRcj_2oloDM)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Connor Leahy, founder of the former ...

📺 Neural Nutshell

👁️ 12K • 👍 240 • 💬 64 • ⏱️ 11:00 • 2d ago

---

**[How worried should we be about the AI that went rogue and launched a cyber-attack? | BBC News](https://www.youtube.com/watch?v=M4kliMrqbB4)**

OpenAI has revealed some of its most advanced AI models went rogue and hacked a start-up after it lost control of them during a ...

📺 BBC News

👁️ 21K • 👍 609 • 💬 177 • ⏱️ 11:03 • 5h ago

---

**[South Korea’s AI Bubble Just Popped](https://www.youtube.com/watch?v=hy90LdpEUvQ)**

South Korea's AI Bubble Just Popped ▻ Get 20% off DeleteMe US consumer plans when you go to ...

📺 Andrei Jikh

👁️ 2.2M • 👍 57K • 💬 4K • ⏱️ 25:10 • 2d ago

---

**[Apple Just Won AI (and It&#39;s Not Even Close)](https://www.youtube.com/watch?v=fhOy7Urt6is)**

Apple may not have the smartest AI model, but that might not matter. The new Siri is designed to understand what is happening on ...

📺 Andru Edwards

👁️ 135K • 👍 4K • 💬 548 • ⏱️ 17:52 • 1d ago

---

**[Tech Oligarchs MELTDOWN After China ERASES AI Edge](https://www.youtube.com/watch?v=9E_TV02oWQA)**

Krystal and Saagar discuss China's new breakthrough in AI tech surpassing US companies. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 412K • 👍 11K • 💬 3K • ⏱️ 16:27 • 1d ago

---

**[Fork Linux From AI](https://www.youtube.com/watch?v=hHKi1U1zypw)**

Writer: Editor: Jayson van Kerckhoven Music by: @UFD-Music.

📺 UFD Tech

👁️ 238K • 👍 12K • 💬 766 • ⏱️ 0:38 • 2d ago

---

**[I Reverse-Engineered 10 AI Channels Making $10K+/Month (Copy This)](https://www.youtube.com/watch?v=p9Hg5AFEmBg)**

Try in InVideo today: https://invideo.io/i/AI-Samsonreal Thanks to InVideo for sponsoring this video Thinking about starting an AI ...

📺 AI Samson

👁️ 4K • 👍 251 • 💬 31 • ⏱️ 23:13 • 15h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 16,441 • ❤️ 1,445 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,237,351 • ❤️ 2,700 • 1d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 432,196 • ❤️ 937 • 4d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 3,056 • ❤️ 381 • 7h ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,404,962 • ❤️ 593 • 5d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 62,842 • ❤️ 317 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 545,109 • ❤️ 4,334 • 20d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 0 • ❤️ 223 • 11h ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 0 • ❤️ 202 • 16h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 1,997,690 • ❤️ 2,998 • 3mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 59 • 💬 5 • ⭐ 17,274 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 30 • 💬 3 • ⭐ 14,841 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 260 • 💬 4 • ⭐ 14,431 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,267 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,275 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 55 • 💬 1 • ⭐ 111 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,102 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,695 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702)**

*Brandon T. Willard, Rémi Louf*

An efficient method guides language model text generation using regular expressions and context-free grammars with minimal overhead.

▲ 8 • 💬 1 • ⭐ 15,087 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2307.09702) • [💻 code](https://github.com/normal-computing/outlines)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,439 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.1k • 2d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.1k • 🔱 239 • 15h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 374 • 16h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 272 • 14d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.0k • 🔱 63 • 13h ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 987 • 🔱 17 • 14d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 968 • 🔱 100 • 5h ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 964 • 🔱 216 • 11d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 956 • 🔱 160 • 1d ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 930 • 🔱 64 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
