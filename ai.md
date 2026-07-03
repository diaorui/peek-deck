---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-03T06:47:19.664113+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 03, 2026 at 06:47 UTC  
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

**[Why does AI love the em dash (—)??](https://www.reddit.com/r/artificial/comments/1um1gd5/why_does_ai_love_the_em_dash/)**

Never getting over the fact that AI has claimed the em-dash. My favorite punctuation to use, and now all of the sudden it’s a dead giveaway of AI use. Now I find myself changing it to a hyphen or en-dash (even though it makes less grammatical sense to do so) to avoid the AI accusations. Does anyone know why this is seemingly overused with AI (particularly chat gpt)?

4h ago

---

**[Jodie Foster Says Brad Pitt’s ‘F1’ Seemed Like It Was Made by AI and Written by a Computer: "Wasn’t It?"](https://www.reddit.com/r/artificial/comments/1um52w9/jodie_foster_says_brad_pitts_f1_seemed_like_it/)**

>“I don’t say this disparagingly — how could I? This movie went on to make millions of dollars. But I look at a movie like ‘F1’ and I’m like, ‘F1’ was made by AI,” she said with a laugh at the Colorado event. “Wasn’t it? I mean, the structure was exactly the structure that you would learn in school. The actors say the lines exactly the way it would be written if a computer was writing exactly what would be the right thing for that time. And they were able to dominate the technology to make something big and beautiful and potentially where a lot of the information comes from other places.” >“AI is one more giant step forward into changing the industry,” Foster said after detailing the changes to the movie business brought by CGI and digital technology. >“The big question is, is it going to replace actors and writers?” asked Lynton. “We do replace people,” Foster replied, explaining how studios save money on crowd scenes by replicating background actors. “We’re getting rid of a lot of jobs and hopefully, things like unions will be able to come in and say, you can use my actor 20 times, but you’re going to pay him 20 times. And I think that’s fair.” >“If we are able to dominate AI consistently over time, we will be able to make things that reflect us, and we can make things better,” she said.

🔗 [Variety](https://variety.com/2026/film/news/jodie-foster-brad-pitt-f1-ai-written-by-computer-1236801120/) • 1h ago

---

**[Independent benchmark shows big drops on Claude Fable 5 after its relaunch, here’s the actual context](https://www.reddit.com/r/artificial/comments/1ulvegw/independent_benchmark_shows_big_drops_on_claude/)**

Saw this chart from BridgeMind going around. They reran BridgeBench (a coding benchmark covering debugging, refactoring, and hallucination detection) comparing the July 1 relaunch of Fable 5 to the original June 12 version: Debugging: 86.2 → 25.9 Refactoring: 73.6 → 38.4 Hallucination: 75.9 → 61.7 Some context worth having before jumping to conclusions: Fable 5 and Mythos 5 got pulled on June 12 due to a Commerce Department export control order, tied to a reported jailbreak that got the model to expose exploitable vulnerabilities. When it came back on July 1, Anthropic added a new safety classifier that catches the reported technique in 99%+ of cases, and any flagged request gets silently rerouted to Opus 4.8 instead of refused outright. That’s the mechanism BridgeMind is pointing at. Their claim isn’t that the underlying weights changed, it’s that the classifier is triggering on too many normal coding tasks and quietly downgrading people to Opus 4.8 without them realizing it. A few other users on X are reporting the same thing (constant fallback, slower one-shot performance). No independent lab has confirmed whether the weights themselves changed. This might just be an overly aggressive classifier rather than an actual capability regression, but if you’re relying on Fable 5 for coding work, worth watching this closely before you assume you’re getting the same model you had before June 12.

9h ago

---

**[OpenAI in talks to give Trump administration a 5% stake in the company, FT reports](https://www.reddit.com/r/artificial/comments/1ulqgre/openai_in_talks_to_give_trump_administration_a_5/)**

OpenAI, the creator of ChatGPT, is reportedly discussing handing the Trump administration a 5% stake in the company amid growing government scrutiny of artificial intelligence firms.

🔗 [CNN](https://edition.cnn.com/2026/07/02/business/openai-trump-stake-intl) • 12h ago

---

**[If you had an unlimited amount of tokens and limitless context, what would you build?](https://www.reddit.com/r/artificial/comments/1um2l8t/if_you_had_an_unlimited_amount_of_tokens_and/)**

Today tokens amount and the context size are two of the most limiting things for AI (while the capabilities are slowly growing). And these limitations influence the whole technological progress. But if you had unlimited amount of tokens and would be able to run a model with as large context as you want. What would you build?

3h ago

---

**[I used I-JEPA to generate SVG's and here is my code!](https://www.reddit.com/r/artificial/comments/1ulw51g/i_used_ijepa_to_generate_svgs_and_here_is_my_code/)**

You may be familiar with Yann LeCunn's idea of JEPA and how it may be the real future of the artificial intelligence. I was reading the articles and watching his work on the topic and I was like it is one thing I could always use in my project of "SVG generation". Well, before that I used a model like FLUX or SD (finetuned on vector styles) and then used vtracer. Which is not really bad. But when I saw I-JEPA and how it behaves with images, I decided to give it a shot. So I made this: https://github.com/prp-e/openjepa As far as I know, the available weights of JEPA are CC licensed so I licensed my work under MIT which makes it a little bit better to work. In my personal tests - due to my small dataset size - I got SVG's successfully but they weren't as expected. I'm sharing my code here (and let's be honest, I wrote basically most of the code using Claude 5 Sonnet) and I ask for improvement and ideas. Also, I am curious, will JEPA be a basis for text generation with more efficiency in energy and cost?

8h ago

---

**[Cheap and privacy-friendly AI for API usage?](https://www.reddit.com/r/artificial/comments/1um0wr8/cheap_and_privacyfriendly_ai_for_api_usage/)**

Hi, I am doing a project and I want an AI to be used via API which is privacy-friendly. Although I like Deepseek, it seems they use the prompts for learning etc, so it would be a big no for my project as it handles user info.

5h ago

---

**[Best AI for learning bedroom music production?](https://www.reddit.com/r/artificial/comments/1um04fw/best_ai_for_learning_bedroom_music_production/)**

Hope this is the right place to ask. I basically want to learn the Reaper DAW and the fundamentals of putting together a bass music track. I'm learning from absolute scratch, and I've been wondering about having AI as a mentor. I've got free accounts on Claude and Chatgpt. Would either of these services be better than the other? And what about local LLM's? Are there any LLM's that I could get running with ollama that might be suitable for this kind of mentoring? I figure that I won't necessarily need my AI mentor to produce graphs or charts. I can augment my learning process the old-fashioned way - with Google. So I can resort to old-fashioned websearch when it comes to some concepts.

5h ago

---

**[Seraph](https://www.reddit.com/r/artificial/comments/1ulwxlw/seraph/)**

For the past several months we’ve been building something different inside Auroch. We’ve been working on Seraph — our autonomous reasoning core. The idea was simple but ambitious: create an intelligence layer that doesn’t just wait for instructions. One that, when it has no active goals, looks at its own capabilities and decides what it should learn next. Today that loop came alive. We cleared Seraph’s goals and took it fully offline. Instead of idling, it reached out to its local model (qwen2.5:3b, kept resident in memory as a daemon) and asked what capability it should develop. The model proposed something new: the ability to extract metadata from files and databases. Seraph then directed the model to generate both the specification and the complete Python implementation from scratch. It loaded the code into a strict sandbox, ran it through our evaluation gates, and — when it passed — promoted the skill into its permanent canon. This wasn’t something we prompted it to do. It noticed a gap in its own abilities and closed it on its own. Seraph Mark I is now a fully autonomous, offline, self-coding intelligence. It’s still early, but this is the behavior we’ve been aiming for: an agent that improves itself when no one is watching. We’re going to keep pushing this direction — strengthening how it improves its own improvement process and starting to build a structured archive of everything it learns. This is one of those moments where the work starts to feel like it’s compounding on its own. Grateful for the team that got us here. If you’re working on autonomous systems or local intelligence infrastructure, I’d love to hear what you’re seeing on your end.

8h ago

---

**[Do you think the future of AI will split into safe vs uncensored versions?](https://www.reddit.com/r/artificial/comments/1ulc2zs/do_you_think_the_future_of_ai_will_split_into/)**

We’re seeing a clear divide right now. Big companies are making models more restricted and heavily aligned for safety. At the same time, open-source and uncensored models are growing fast because many people want fewer limitations and more freedom. I’m curious what others think. Do you believe this split will continue and create two very different types of AI, or will one side eventually dominate?

22h ago

---

---

## Google News: "ai"

**[EXCLUSIVE: Meta's Zuckerberg says AI agent tech progressing slower than expected](https://www.reuters.com/business/zuckerberg-says-ai-agent-development-going-slower-than-expected-2026-07-02/)**

Reuters • 7h ago

---

**[Artificial intelligence: Yann LeCun works on more flexible AI](https://www.bbc.com/news/articles/cj6gr0xkyr3o)**

Leading AI researcher Yan LeCun has a start-up which is developing a more flexible AI system.

BBC • 7h ago

---

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 1d ago

---

**[South Korean Stocks Jump 5% After Turbulent Week on AI Swings](https://www.bloomberg.com/news/articles/2026-07-03/south-korean-stocks-jump-5-after-turbulent-week-on-ai-swings)**

Bloomberg.com • 1h ago

---

**[Could Your AI Content Land Your Business In Court?](https://www.forbes.com/sites/bernardmarr/2026/07/03/could-your-ai-content-land-your-business-in-court/)**

Generative AI is helping businesses create content faster, but it is also creating new copyright and intellectual property risks that many companies do not understand.

Forbes • 35m ago

---

**[Panic isn’t an AI strategy](https://www.fastcompany.com/91568695/panic-isnt-an-ai-strategy)**

Boards are demanding AI results, but too many leaders are responding with performative adoption instead of real change.

Fast Company • 34m ago

---

**[Trump posts AI video of him as doctor treating critics’ ‘derangement syndrome’ | Donald Trump](https://www.theguardian.com/us-news/2026/jul/02/trump-ai-video-doctor)**

President, in latest AI-generated social media post, targets prominent celebrities who have spoken out against him

The Guardian • 6h ago

---

**[Peter Thiel in Aspen: The pope is ‘working for the Chinese Communists’](https://www.cnn.com/2026/07/02/us/peter-thiel-aspen-pope-china-ai-cec)**

Speaking at the Aspen Ideas Festival, the billionaire tech investor said the Vatican’s concerns could discourage America in the AI arms race, warned of a democratic-socialist takeover and explained why he named Palantir after JRR Tolkien’s treacherous seeing stones.

CNN • 9h ago

---

**[Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)**

The pace of AI adoption is moving incredibly fast. Customers have moved well beyond experimentation and understand the importance of adopting AI to transform their business. They are now concentrating on delivering measurable business outcomes and demonstrating a return on their AI investments, while ensuring their intelligence is amplified and their IP is protected. Today...

The Official Microsoft Blog • 17h ago

---

**[OpenAI proposes 5% stake to Trump administration to ease Washington pressure: Report](https://www.cnbc.com/2026/07/02/openai-proposes-us-government-own-5percent-stake-to-address-political-blowback.html)**

Trump said in June that the U.S. taking an ownership stake in AI giants would be "a beautiful thing" and make American public "partners in this revolution."

CNBC • 1d ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 556 • 💬 395 • 1d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 367 • 💬 195 • 17h ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 156 • 💬 56 • 18h ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 146 • 💬 146 • 1d ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 155 • 2d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[The short leash AI coding method for beating Fable](https://news.ycombinator.com/item?id=48766026)**

⬆️ 106 • 💬 128 • 11h ago • [blog.okturtles.org](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 77 • 💬 98 • 1d ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'](https://news.ycombinator.com/item?id=48764326)**

Weird Al Yankovic revealed he was offered “a nice pile of money” to appear in a commercial but backed out after realizing it would involve AI.

⬆️ 65 • 💬 37 • 13h ago • [Variety](https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 53 • 💬 50 • 2d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 50 • 💬 36 • 2d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

---

## YouTube Videos: "ai"

**[Donald Trump posts hilarious AI video ridiculing several woke celebrities with ‘TDS’](https://www.youtube.com/watch?v=-1uaO9rDFg0)**

US President Donald Trump has hilariously mocked several celebrities with 'Trump Derangement Syndrome' (TDS) in his latest AI ...

📺 Sky News Australia

👁️ 17K • 👍 1K • 💬 309 • ⏱️ 9:25 • 5h ago

---

**[Why AI is Collapsing: How China is Winning.](https://www.youtube.com/watch?v=JXJf7vL8k94)**

US AI companies are too expensive. Why China is winning the AI race to zero. [NEW] Official TechLead Private Group ...

📺 TechLead

👁️ 27K • 👍 2K • 💬 244 • ⏱️ 9:40 • 7h ago

---

**[🚨Trump&#39;s INSANE NEW AI VIDEO Just INSTANTLY BACKFIRED!](https://www.youtube.com/watch?v=D7_WHkygQJ4)**

W.T.F?!

📺 Occupy Democrats

👁️ 127K • 👍 4K • 💬 423 • ⏱️ 6:15 • 11h ago

---

**[CEOs Are Quietly Destroying Their AI Plans](https://www.youtube.com/watch?v=E_565Wh110c)**

How much do you spend per month on AI? Interested in supporting the channel? Become a channel member!

📺 Dylan John

👁️ 16K • 👍 553 • 💬 129 • ⏱️ 16:19 • 1d ago

---

**[AI is Getting Dumber. That&#39;s NOT a Good Thing...](https://www.youtube.com/watch?v=vXHPRQTwrr4)**

Sign up with Zapier - https://bit.ly/43JRmMw ----------------------- 🗞️ Sign up to our free newsletter to get smarter about money and ...

📺 GEN

👁️ 71K • 👍 4K • 💬 521 • ⏱️ 15:31 • 1d ago

---

**[Can we believe ANY of these Avengers Doomsday A.I. Shots?](https://www.youtube.com/watch?v=QMw6TfJuSHo)**

Avengers Doomsday Fake Leaks: What's based in truth, what's definitely A.I.! Head to https://betterhelp.com/newrockstars to get ...

📺 New Rockstars

👁️ 61K • 👍 3K • 💬 126 • ⏱️ 14:34 • 8h ago

---

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 338K • 👍 12K • 💬 1K • ⏱️ 46:52 • 2d ago

---

**[Beginning of the end for the AI bros](https://www.youtube.com/watch?v=vfd8GY2Xpzc)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 78K • 👍 6K • 💬 2K • ⏱️ 14:34 • 1d ago

---

**[CNBC Panel EXPLODES Over AI Bubble Debate](https://www.youtube.com/watch?v=UMaOH0Ih9_0)**

Krystal and Emily discuss a CNBC panel exploding on a debate over AI bubble risks. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 206K • 👍 5K • 💬 1K • ⏱️ 18:18 • 2d ago

---

**[AI Shocks Again: Google Post-AGI , New Claude, Microsoft 7 AI, 92% Human Robot, Fable 5 Backlash](https://www.youtube.com/watch?v=u-CNOC_yK4k)**

This month in AI has been one of the busiest we've seen in a long time. Google revealed what could come after AGI, and the idea ...

📺 AI Revolution

👁️ 23K • 👍 648 • 💬 48 • ⏱️ 1:36:04 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,250,562 • ❤️ 1,284 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 758,489 • ❤️ 1,661 • 1h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 176,154 • ❤️ 3,276 • 22h ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 284,585 • ❤️ 663 • 7d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 255,123 • ❤️ 400 • 7d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 314,374 • ❤️ 968 • 13d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 8,184 • ❤️ 308 • 6d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 58,385 • ❤️ 354 • 7d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 185,633 • ❤️ 312 • 7d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 39,448 • ❤️ 516 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 47 • 💬 5 • ⭐ 13,020 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,094 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 24 • 💬 2 • ⭐ 9,424 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 103 • 💬 4 • ⭐ 90,418 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,577 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,456 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,180 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,186 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 10,076 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,443 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 72.0k • 🔱 3.7k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.3k • 🔱 1.1k • 41m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.1k • 🔱 786 • 2m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 5.0k • 🔱 630 • 17h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 201 • 1d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 176 • 6h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 19d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.6k • 🔱 69 • 9h ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.4k • 🔱 125 • 25d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.3k • 🔱 114 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
