---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-03T03:20:02.639905+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 03, 2026 at 03:20 UTC  
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

**[Independent benchmark shows big drops on Claude Fable 5 after its relaunch, here’s the actual context](https://www.reddit.com/r/artificial/comments/1ulvegw/independent_benchmark_shows_big_drops_on_claude/)**

Saw this chart from BridgeMind going around. They reran BridgeBench (a coding benchmark covering debugging, refactoring, and hallucination detection) comparing the July 1 relaunch of Fable 5 to the original June 12 version: Debugging: 86.2 → 25.9 Refactoring: 73.6 → 38.4 Hallucination: 75.9 → 61.7 Some context worth having before jumping to conclusions: Fable 5 and Mythos 5 got pulled on June 12 due to a Commerce Department export control order, tied to a reported jailbreak that got the model to expose exploitable vulnerabilities. When it came back on July 1, Anthropic added a new safety classifier that catches the reported technique in 99%+ of cases, and any flagged request gets silently rerouted to Opus 4.8 instead of refused outright. That’s the mechanism BridgeMind is pointing at. Their claim isn’t that the underlying weights changed, it’s that the classifier is triggering on too many normal coding tasks and quietly downgrading people to Opus 4.8 without them realizing it. A few other users on X are reporting the same thing (constant fallback, slower one-shot performance). No independent lab has confirmed whether the weights themselves changed. This might just be an overly aggressive classifier rather than an actual capability regression, but if you’re relying on Fable 5 for coding work, worth watching this closely before you assume you’re getting the same model you had before June 12.

5h ago

---

**[OpenAI in talks to give Trump administration a 5% stake in the company, FT reports](https://www.reddit.com/r/artificial/comments/1ulqgre/openai_in_talks_to_give_trump_administration_a_5/)**

OpenAI, the creator of ChatGPT, is reportedly discussing handing the Trump administration a 5% stake in the company amid growing government scrutiny of artificial intelligence firms.

🔗 [CNN](https://edition.cnn.com/2026/07/02/business/openai-trump-stake-intl) • 8h ago

---

**[Why does AI love the em dash (—)??](https://www.reddit.com/r/artificial/comments/1um1gd5/why_does_ai_love_the_em_dash/)**

Never getting over the fact that AI has claimed the em-dash. My favorite punctuation to use, and now all of the sudden it’s a dead giveaway of AI use. Now I find myself changing it to a hyphen or en-dash (even though it makes less grammatical sense to do so) to avoid the AI accusations. Does anyone know why this is seemingly overused with AI (particularly chat gpt)?

1h ago

---

**[I used I-JEPA to generate SVG's and here is my code!](https://www.reddit.com/r/artificial/comments/1ulw51g/i_used_ijepa_to_generate_svgs_and_here_is_my_code/)**

You may be familiar with Yann LeCunn's idea of JEPA and how it may be the real future of the artificial intelligence. I was reading the articles and watching his work on the topic and I was like it is one thing I could always use in my project of "SVG generation". Well, before that I used a model like FLUX or SD (finetuned on vector styles) and then used vtracer. Which is not really bad. But when I saw I-JEPA and how it behaves with images, I decided to give it a shot. So I made this: https://github.com/prp-e/openjepa As far as I know, the available weights of JEPA are CC licensed so I licensed my work under MIT which makes it a little bit better to work. In my personal tests - due to my small dataset size - I got SVG's successfully but they weren't as expected. I'm sharing my code here (and let's be honest, I wrote basically most of the code using Claude 5 Sonnet) and I ask for improvement and ideas. Also, I am curious, will JEPA be a basis for text generation with more efficiency in energy and cost?

5h ago

---

**[If you had an unlimited amount of tokens and limitless context, what would you build?](https://www.reddit.com/r/artificial/comments/1um2l8t/if_you_had_an_unlimited_amount_of_tokens_and/)**

Today tokens amount and the context size are two of the most limiting things for AI (while the capabilities are slowly growing). And these limitations influence the whole technological progress. But if you had unlimited amount of tokens and would be able to run a model with as large context as you want. What would you build?

18m ago

---

**[It feels like there are way more ways AGI goes wrong than right for us (please try change my mind)](https://www.reddit.com/r/artificial/comments/1um16sw/it_feels_like_there_are_way_more_ways_agi_goes/)**

I really don't want to be a doomer, so if you think you can change the way I think about this, please reply in the comments! TL;DR really smart things that aren't human can be really dangerous (at least from a human-centric perspective), regardless of whether it is controlled by the few or the many. I usually consider myself an optimist, but I feel that treating AGI as something that is more likely to be good than bad is wishful thinking. Not going to detail all my thoughts since it would take way too long (and I need to sleep), but here's a summary. Assume we get a sufficiently advanced level of AGI. If a small group of elites ends up controlling and restricting access to it, be it a lab or a government, that can clearly be dangerous. All the leverage sits with them, and I'm not sure I trust these actors to use that leverage correctly. I think this argument has been repeated a lot of times, so I won't go in depth, but the idea is that when a handful of people no longer need everyone else's labour and thinking, there's not much stopping them from acting like that's the case. But the open weights scenario, where access to AGI isn't restricted or controlled, isn't that reassuring either. It doesn't take much to destroy the world or make it a very bad place. You don't need most people to be malicious, you just need enough people determined to use an uncensored open model to do unthinkable damage. If it can empower a bad actor to make and release a highly deadly bioweapon, that scenario only needs to happen once for it to be a very bad outcome (something something vulnerable world hypothesis). Yes, I'm oversimplifying, and these are the two extremes, and most serious arguments try to find some kind of a middle way. But even when we look for a compromise, all we're really doing is picking where we sit on the spectrum between "too concentrated" and "too open," and both ends of that spectrum seem like they can go wrong all too easily. Mixing and matching doesn't get you out of the underlying problem, which is that AGI hands out an enormous amount of power to do damage. Intelligence will be the closest thing to a superweapon we've ever produced, and no arrangement of who holds it makes that fact go away. I can definitely think of scenarios where AGI to be aligned and somehow steer clear of both outcomes, but assuming we don't have plot armour, I don't see why that good outcome should be more likely than the two bad ones. Getting it right seems to need a narrow set of things to all go well at once, while getting it wrong just needs any one of them to fail. I don't know, man. Just wanted to rant and hear what other (probably more informed people) think about this.

1h ago

---

**[Cheap and privacy-friendly AI for API usage?](https://www.reddit.com/r/artificial/comments/1um0wr8/cheap_and_privacyfriendly_ai_for_api_usage/)**

Hi, I am doing a project and I want an AI to be used via API which is privacy-friendly. Although I like Deepseek, it seems they use the prompts for learning etc, so it would be a big no for my project as it handles user info.

1h ago

---

**[Best AI for learning bedroom music production?](https://www.reddit.com/r/artificial/comments/1um04fw/best_ai_for_learning_bedroom_music_production/)**

Hope this is the right place to ask. I basically want to learn the Reaper DAW and the fundamentals of putting together a bass music track. I'm learning from absolute scratch, and I've been wondering about having AI as a mentor. I've got free accounts on Claude and Chatgpt. Would either of these services be better than the other? And what about local LLM's? Are there any LLM's that I could get running with ollama that might be suitable for this kind of mentoring? I figure that I won't necessarily need my AI mentor to produce graphs or charts. I can augment my learning process the old-fashioned way - with Google. So I can resort to old-fashioned websearch when it comes to some concepts.

2h ago

---

**[Seraph](https://www.reddit.com/r/artificial/comments/1ulwxlw/seraph/)**

For the past several months we’ve been building something different inside Auroch. We’ve been working on Seraph — our autonomous reasoning core. The idea was simple but ambitious: create an intelligence layer that doesn’t just wait for instructions. One that, when it has no active goals, looks at its own capabilities and decides what it should learn next. Today that loop came alive. We cleared Seraph’s goals and took it fully offline. Instead of idling, it reached out to its local model (qwen2.5:3b, kept resident in memory as a daemon) and asked what capability it should develop. The model proposed something new: the ability to extract metadata from files and databases. Seraph then directed the model to generate both the specification and the complete Python implementation from scratch. It loaded the code into a strict sandbox, ran it through our evaluation gates, and — when it passed — promoted the skill into its permanent canon. This wasn’t something we prompted it to do. It noticed a gap in its own abilities and closed it on its own. Seraph Mark I is now a fully autonomous, offline, self-coding intelligence. It’s still early, but this is the behavior we’ve been aiming for: an agent that improves itself when no one is watching. We’re going to keep pushing this direction — strengthening how it improves its own improvement process and starting to build a structured archive of everything it learns. This is one of those moments where the work starts to feel like it’s compounding on its own. Grateful for the team that got us here. If you’re working on autonomous systems or local intelligence infrastructure, I’d love to hear what you’re seeing on your end.

4h ago

---

**[Do you think the future of AI will split into safe vs uncensored versions?](https://www.reddit.com/r/artificial/comments/1ulc2zs/do_you_think_the_future_of_ai_will_split_into/)**

We’re seeing a clear divide right now. Big companies are making models more restricted and heavily aligned for safety. At the same time, open-source and uncensored models are growing fast because many people want fewer limitations and more freedom. I’m curious what others think. Do you believe this split will continue and create two very different types of AI, or will one side eventually dominate?

19h ago

---

---

## Google News: "ai"

**[EXCLUSIVE: Meta's Zuckerberg says AI agent tech progressing slower than expected](https://www.reuters.com/business/zuckerberg-says-ai-agent-development-going-slower-than-expected-2026-07-02/)**

Reuters • 4h ago

---

**[AI agents will soon be able to match human traders, Robinhood CEO tells CNBC](https://www.cnbc.com/2026/07/02/robinhood-ceo-ai-agents.html)**

Vlad Tenev spoke about the potential of AI agents in trading in an interview with CNBC.

CNBC • 17h ago

---

**[Mark Zuckerberg said AI agent tech is advancing more slowly than expected in an internal town hall](https://www.businessinsider.com/zuckerberg-said-metas-ai-progress-has-been-slower-than-expected-2026-7)**

Superintelligence will take time, Zuckerberg tells Meta staff, as the company makes its AI training program opt-in after a data leak.

Business Insider • 5h ago

---

**[Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)**

The pace of AI adoption is moving incredibly fast. Customers have moved well beyond experimentation and understand the importance of adopting AI to transform their business. They are now concentrating on delivering measurable business outcomes and demonstrating a return on their AI investments, while ensuring their intelligence is amplified and their IP is protected. Today...

The Official Microsoft Blog • 13h ago

---

**[Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)**

Microsoft is the latest tech company to form a business focused on helping customers understand and implement artificial intelligence.

CNBC • 14h ago

---

**[Microsoft unveils $2.5B ‘Frontier Company’ to embed AI engineers inside customers](https://www.geekwire.com/2026/microsoft-announces-2-5b-frontier-company-to-embed-ai-engineers-inside-customers/)**

"Microsoft Frontier Company" is a $2.5 billion initiative that will embed engineers inside customer organizations to build and run their AI systems. The move follows similar efforts by Amazon, OpenAI and Anthropic, and expands work Microsoft was already doing through its consulting arm and partners.

GeekWire • 14h ago

---

**[3,000% bonuses but a growing wealth divide: South Korea grapples with its AI chip boom](https://www.theguardian.com/world/ng-interactive/2026/jul/03/south-korea-wealth-divide-ai-chip-boom)**

Powered by chipmakers Samsung Electronics and SK Hynix, South Korea is seeing a surge in wealth, but there are questions over who gets to share in the profits

The Guardian • 45m ago

---

**[A golden ticket for AI: Netflix recreates Gene Wilder’s voice for new ‘Willy Wonka’ show](https://www.nbcnews.com/video/netflix-recreates-gene-wilder-s-voice-for-new-willy-wonka-show-266115141809)**

A new Willy Wonka gameshow on Netflix features the AI voice of late actor Gene Wilder. NBC News' Gadi Schwartz reports.

NBC News • 1h ago

---

**[Will God speak to you through AI? No, AI doesn't go there](https://www.usatoday.com/story/news/nation/2026/07/02/ai-lack-religion-show-faith-bias/90747041007/)**

While such patterns are likely unintentional, researchers said they show the challenges of representing diverse belief systems consistently.

USA Today • 47m ago

---

**[Trump shares AI video of himself as a doctor who treats celebrities with 'Trump Derangement Syndrome'](https://www.yahoo.com/news/politics/article/trump-shares-ai-video-of-himself-as-a-doctor-who-treats-celebrities-with-trump-derangement-syndrome-184026887.html)**

In the clip, deepfakes of Rosie O'Donnell, Robert De Niro and Julia Roberts testify that drinking Diet Coke helped ease their opposition to the president's policies.

Yahoo • 8h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 556 • 💬 395 • 1d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 362 • 💬 191 • 13h ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 154 • 💬 53 • 14h ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 146 • 💬 145 • 1d ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 155 • 2d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 77 • 💬 98 • 20h ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[The short leash AI coding method for beating Fable](https://news.ycombinator.com/item?id=48766026)**

⬆️ 73 • 💬 75 • 8h ago • [blog.okturtles.org](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

---

**[Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'](https://news.ycombinator.com/item?id=48764326)**

Weird Al Yankovic revealed he was offered “a nice pile of money” to appear in a commercial but backed out after realizing it would involve AI.

⬆️ 61 • 💬 35 • 10h ago • [Variety](https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 53 • 💬 50 • 1d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 50 • 💬 36 • 2d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

---

## YouTube Videos: "ai"

**[Why AI is Collapsing: How China is Winning.](https://www.youtube.com/watch?v=JXJf7vL8k94)**

US AI companies are too expensive. Why China is winning the AI race to zero. [NEW] Official TechLead Private Group ...

📺 TechLead

👁️ 15K • 👍 1K • 💬 176 • ⏱️ 9:40 • 4h ago

---

**[CEOs Are Quietly Destroying Their AI Plans](https://www.youtube.com/watch?v=E_565Wh110c)**

How much do you spend per month on AI? Interested in supporting the channel? Become a channel member!

📺 Dylan John

👁️ 16K • 👍 541 • 💬 129 • ⏱️ 16:19 • 1d ago

---

**[NEW Method To Create Long AI Animation Videos In Minutes](https://www.youtube.com/watch?v=OF9xcQCQSFc)**

How To Create Long AI Cartoon Animations in 11 minutes Check out OpenArt Director: ...

📺 Mira AI

👁️ 8K • ⏱️ 11:13 • 13h ago

---

**[Trump Posts AI &#39;Dr. Trump&#39; Video — Prescribes Diet Coke To Those Suffering With &#39;TDS&#39;](https://www.youtube.com/watch?v=8AheL0t-h-U)**

LIKE & SUBSCRIBE for new videos daily. / @DailyWireNews Join DailyWire and watch all of our ad-free content NOW: ...

📺 Daily Wire News

👁️ 3K • 👍 246 • 💬 28 • ⏱️ 1:31 • 9h ago

---

**[AI is Getting Dumber. That&#39;s NOT a Good Thing...](https://www.youtube.com/watch?v=vXHPRQTwrr4)**

Sign up with Zapier - https://bit.ly/43JRmMw ----------------------- 🗞️ Sign up to our free newsletter to get smarter about money and ...

📺 GEN

👁️ 68K • 👍 4K • 💬 511 • ⏱️ 15:31 • 1d ago

---

**[Doctor Trump Shares AI Video Claiming To Cure ‘Trump Derangement Syndrome’ Sparks Row | Watch](https://www.youtube.com/watch?v=0mBBIOiFOtk)**

US President Donald Trump shared an AI-generated parody video portraying himself as a doctor offering a fictional treatment for ...

📺 MIRROR NOW

👁️ 11K • 👍 200 • 💬 100 • ⏱️ 3:42 • 12h ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 156K • 👍 9K • 💬 775 • ⏱️ 9:43 • 2d ago

---

**[Beginning of the end for the AI bros](https://www.youtube.com/watch?v=vfd8GY2Xpzc)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 77K • 👍 6K • 💬 2K • ⏱️ 14:34 • 1d ago

---

**[STOP Paying: Make LONG AI Videos FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=RI4LwxmpEys)**

Try Higgsfield and create higher-quality AI videos here → https://higgsfield.ai/s/general-malvaai-IlyGIB Free Prompt PDFs + AI ...

📺 Malva AI

👁️ 5K • 👍 269 • 💬 44 • ⏱️ 11:46 • 15h ago

---

**[Trump Posts AI Video of Doctor Treating &quot;Trump Derangement Syndrome&quot; | APT](https://www.youtube.com/watch?v=uURrETnq74c)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCpLEtz3H0jSfEneSdf1YKnw/join President Donald ...

📺 APT

👁️ 18K • 👍 592 • 💬 326 • ⏱️ 3:01 • 16h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,250,562 • ❤️ 1,265 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 758,489 • ❤️ 1,656 • 4d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 176,154 • ❤️ 3,260 • 19h ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 284,585 • ❤️ 658 • 7d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 255,123 • ❤️ 397 • 7d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 314,374 • ❤️ 964 • 13d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 58,385 • ❤️ 353 • 7d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 8,184 • ❤️ 303 • 5d ago

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

⬇️ 39,448 • ❤️ 512 • 7d ago

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

▲ 12 • 💬 2 • ⭐ 18,540 • 16mo ago

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

▲ 37 • 💬 1 • ⭐ 26,403 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 71.9k • 🔱 3.7k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.3k • 🔱 1.1k • 10h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.1k • 🔱 782 • 3m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.9k • 🔱 624 • 14h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 201 • 1d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 175 • 3h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 19d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.6k • 🔱 68 • 6h ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.3k • 🔱 125 • 25d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.3k • 🔱 114 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
