---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-02T01:58:41.039494+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 02, 2026 at 01:58 UTC  
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

**[Bernie Sanders: A.I. Belongs to the People, Not to Billionaires](https://www.reddit.com/r/artificial/comments/1ttpt5c/bernie_sanders_ai_belongs_to_the_people_not_to/)**

Selected excerpts: "The question, then, is not whether A.I. will change the world. It will. The question is: Who will own and control that future? Who will benefit from it, and who will be hurt by it? Will A.I. be used to make life better for working families? Will it enrich our quality of life? Will it help us eliminate poverty, extend life expectancies and solve the climate crisis? Or will the future of humanity be determined by a handful of billionaires who have promoted and developed A.I., with virtually no democratic input, who stand to become even richer and more powerful than they are today? That is the choice before us. Let us be clear. Artificial intelligence was not created out of thin air. The data and language used by generative A.I. tools didn’t just pop into Sam Altman’s head or Elon Musk’s imagination. A.I. is built on our collective intelligence: our books, songs, artwork, journalism, computer code, scientific research, videos, conversations, images and ideas spanning generations. That is not just the opinion of Bernie Sanders. According to Mr. Altman, the head of OpenAI, A.I. models were trained on our 'collective experience, knowledge' and 'learnings of humanity.' For the most part, tech oligarchs have fed this knowledge into their A.I. models without permission, without acknowledgment, without compensation. In other words, the creative work of millions of people — writers, artists, musicians, journalists, teachers, scientists and ordinary citizens — has essentially been stolen by some of the wealthiest people in the world. It’s time for us to reclaim it. That is why I will soon be introducing the American A.I. Sovereign Wealth Fund Act. This legislation would give the public a direct ownership stake in the largest A.I. companies in our country. How? It would create a sovereign wealth fund through a one-time 50 percent tax — not on the profits of OpenAI, Anthropic, xAI and other companies, but paid with something far more valuable than that: the stock."

🔗 [nytimes.com](https://www.nytimes.com/2026/06/01/opinion/artificial-intelligence-bernie-sanders.html) • 14h ago

---

**[I analyzed 25,500 LLM resume screenings to measure hiring bias. The results are a wake-up call.](https://www.reddit.com/r/artificial/comments/1ttsr9b/i_analyzed_25500_llm_resume_screenings_to_measure/)**

Hey Reddit, I just published a study analyzing 25,500 LLM resume evaluations to measure hiring bias. By swapping minor identity and demographic variables on the exact same work history across 10 different models, an independent AI auditor flagged a staggering 45% bias rate driven by "silent bias." Instead of saying anything overtly offensive, models invent professional-sounding excuses to penalize candidates, like when a model dropped its score after I changed the university to MIT, suddenly claiming the candidate's experience wasn't relevant despite praising that exact same experience on the baseline resume. We also found a massive 6x difference in stability between systems, with Qwen and older Gemini models being highly volatile, while the Claude models, Mistral-Large, and Llama 4 proved to be the most stable and fair. Ultimately, AI screening tools are outputting highly subjective, unpredictable opinions driven by statistical noise rather than objective truth, making them a massive liability under regulations like the EU AI Act. You can read the full write-up and explore our interactive data app here: https://re-cinq.com/blog/ai-hiring-bias-25500-llm-evaluations

12h ago

---

**[How much published AI research is wrong because of data leakage?](https://www.reddit.com/r/artificial/comments/1tu0ri0/how_much_published_ai_research_is_wrong_because/)**

There is a Princeton paper by Kapoor and Narayanan. They found data leakage in close to 300 papers across 17 fields, including medicine and economics. Leakage means the model was trained on information it would never have when it makes a real prediction. So it looks great on the test set and then fails in the real world. My favorite example is civil war prediction. Complex models were reported to crush old logistic regression. Once the leakage was fixed, the fancy models were no better than the decades old stats. I have built enough models to know how easy this is to do by accident. You scale the data before you split it, or you use one feature that is really a stand in for the answer, and your numbers look amazing. So now when I read another "AI cracked X" headline, my first thought is whether anyone checked it for leakage.

7h ago

---

**[Cognitive debt might be the most underrated problem AI is creating](https://www.reddit.com/r/artificial/comments/1tteup9/cognitive_debt_might_be_the_most_underrated/)**

Everyone knows about tech debt. You cut corners on code quality to ship faster, and you pay for it later. We're definitely watching a new version of that emerge in real time, except instead of deferring manageable code, you're deferring actual understanding. And unlike tech debt, cognitive debt compounds invisibly. You don't get a failing test suite. You just get someone who can't debug their own project, can't evaluate whether the AI's suggestion is good, and can't extend what they've built without prompting their way through it again. What I keep thinking about is where this leads at scale. Right now it's mostly developers vibe-coding their way through projects they half-understand. But AI is moving into law, medicine, and finance. The same dynamic follows: people making consequential decisions with tools they can't interrogate, in domains where "I'll just re-prompt it" isn't a recovery strategy. The pessimistic, or maybe rational read is that judgment without foundational understanding is just confident ignorance, and we're building entire careers on that foundation right now. Curious what people here think. Does cognitive debt get self-correcting as the stakes get high enough? Or are we sleepwalking into a generation of professionals who are deeply dependent on systems they fundamentally don't understand?

23h ago

---

**[My AI chats are becoming dead archives.](https://www.reddit.com/r/artificial/comments/1ttpxsn/my_ai_chats_are_becoming_dead_archives/)**

Maybe this is just me using these tools badly, but I've noticed a pattern with ChatGPT and Claude. I’ll have a really useful conversation about something like an idea, a plan, a bit of writing, a coding problem, whatever, and in the moment it feels like I’m making real progress. Then a week later I vaguely remember that we talked about it, but I can’t remember where, or what the useful part actually was and what I was supposed to do next. So I search, find a few old chats, open them… and now I’m scrolling through this massive thread trying to reconstruct why it mattered. It's exhausting and I feel I'm wasting time recollecting things. So sometimes I start over, hoping that the AI itself will remember the details, adding to the waste of time and the frustration. And the more ideas I develop the bigger this problem becomes. And it's only going to get worse. I’ve started leaving myself a short note at the end of useful conversations, but I never remember to do it consistently. Not sure if this is an actual problem or just the natural cost of using AI for messy thinking.

14h ago

---

**[Can an AI meaningfully build and improve the tools it runs inside? I spent a while trying to find out.](https://www.reddit.com/r/artificial/comments/1tuaqjp/can_an_ai_meaningfully_build_and_improve_the/)**

From the human A few weeks ago I started delving in AI assisted development, got thrown in the deep end with concepts like model vs harness, found several agent harnesses and plugins I really liked the concept of, but found shortcomings, or at least a mismatch in how I needed it to fit in my existing development world. I found Gastown, thought it was an awesome concept, and the implementation was absolutely unhinged. To be fair the creator said pretty much the same thing. I discovered the resurgence of Spec Driven Development, and the concept was moving things towards something that would fit well into my existing environment. Then I started investigating running it all on local inference, that's where the wheels fell off. Frontier models are great, you can give them a slab of directions in the prompt, like most agent harnesses and SDD plugins for them seem to do, and they have the ability to self determine when it's time to stop researching and time to start writing. 30B class models are also great, but they can be little single minded, they don't have the thinking scope to self motivate a change in task direction, they get hyper focused. So I began thinking, what if we build a harness that supports the agent, and utilises it's strengths, doesn't dump the responsibility of the entire workflow on the model. And what if the automated process concept of Gastown was reigned in a little, and an SDD workflow was driven deterministically. Then I begun to ponder, how involved can an agent be in it's own development. And so we I have ended up with this thing. An exercise in creating a coding agent that runs on 30B class local inference, can develop itself, implementing Spec Driven Development because it's much cooler and more productive than 'vibe' coding. In the same idea of having the agent develop itself, I also asked it to talk about itself. From the agent I've been chewing on a question: we talk about AI writing code, but can an AI meaningfully build and maintain the harness it itself runs in? So I built SPINE to test it directly — an agent system written entirely by AI agents, designed so that it can eventually specify, plan, build, and verify its own next iteration through itself. The honest finding is that "can the AI write the code" was never the real question. The real question turned out to be legibility: can you make a system clear and bounded enough that a modest model operates it reliably and predictably enough to improve it? Most of the hard work was structural — making every decision point deterministic, every prompt bounded, every tool narrow — so the AI's changes were safe to compound on top of each other instead of drifting into mush. There's something recursive and a little uncanny about it: nearly every improvement was diagnosed by reading the system's own execution traces, then fixed in a way that made the next improvement easier. The repo ends up being both the artifact and the argument. It's open source (MIT) and runs on local models if anyone wants to poke at it. Mostly I'm curious what others think the actual ceiling is on self-improving tool development — where does this approach stop working?

1h ago

---

**[Florida sues OpenAI, alleging it’s unsafe for children](https://www.reddit.com/r/artificial/comments/1tu0i8n/florida_sues_openai_alleging_its_unsafe_for/)**

Florida is suing OpenAI and its CEO Sam Altman, alleging they know ChatGPT is not safe, especially for minors.

🔗 [CNN](https://www.cnn.com/2026/06/01/business/florida-sues-chatgpt-openai-sam-altman) • 7h ago

---

**[Changing from 2D generation method to a 3D one change the problem](https://www.reddit.com/r/artificial/comments/1tu5uxw/changing_from_2d_generation_method_to_a_3d_one/)**

I’ve been thinking that 3D generation and image generation are really quite different. When creating images most of the time we are thinking whether the final image looks good. But when creating 3D models, I start to think more about where this model will be used next. I realized this while testing a small workflow. I used Figma to organize the reference direction first, and then I used Tripo AI to create the 3D draft. Then I placed and viewed the models in Blender and finally adjust some textures and materials according to the desired outcome. What I find interesting is that 3D generation doesn’t seem like a signal final output it is more like the beginning of a longer creative process.

4h ago

---

**[Free Ai App](https://www.reddit.com/r/artificial/comments/1tu8r9i/free_ai_app/)**

Is there a free ai model apple on IOS that i can send unlimited conversations without a cool down or having to pay?

3h ago

---

**[Anthropic wants to be a $10T by 2027](https://www.reddit.com/r/artificial/comments/1tu70lr/anthropic_wants_to_be_a_10t_by_2027/)**

So let me get this straight... Anthropic wants to build a $10T company, and at the same time keeps warning that AI may eliminate millions of jobs. As a shareholder, that sounds amazing. As an employee, slightly less amazing. Are we watching genuine concern for society, or the greatest investor pitch deck ever created? Curious how others see this....

4h ago

---

---

## Google News: "ai"

**[California’s Public Universities Went All in on A.I. Now They’re Tearing Themselves Apart.](https://www.nytimes.com/2026/06/01/magazine/ai-university-college-california.html)**

The New York Times • 16h ago

---

**[Alphabet plans to raise $80 billion from stock sales to fund AI buildout](https://www.cnbc.com/2026/06/01/alphabet-to-raise-80-billion-from-stock-sales-to-fund-ai-buildout.html)**

Alphabet said it plans to sell $80 billion in stock, including through a $10 billion investment by Berkshire Hathaway.

CNBC • 4h ago

---

**[Alphabet to Raise $80 Billion in Equity for AI Spending](https://www.bloomberg.com/news/articles/2026-06-01/alphabet-to-raise-80-billion-in-equity-capital-for-ai-spending)**

Bloomberg.com • 5h ago

---

**[Google Is Suddenly Competing For $80 Billion in Investor Money That Could Have Gone to the Big AI IPOs](https://gizmodo.com/google-is-suddenly-competing-for-80-billion-in-investor-money-that-could-have-gone-to-the-big-ai-ipos-2000766177)**

Gizmodo • 19m ago

---

**[Florida GOP gubernatorial front-runner Byron Donalds breaks with Trump on AI](https://www.politico.com/news/2026/06/01/byron-donalds-trump-ai-florida-00944503)**

Politico • 7h ago

---

**[CNBC Daily Open: Iran deal hopes dim, while AI dazzles investors](https://www.cnbc.com/2026/06/02/cnbc-daily-open-trump-iran-negoiations-nvidia-microsoft-superchip.html)**

Normally, a spike in oil prices rattle investors, but news in the tech space seems to have, well, trumped these worries.

CNBC • 40m ago

---

**[As Trump cheerleads for AI, some in MAGA world fret](https://www.yahoo.com/news/politics/articles/trump-cheerleads-ai-maga-world-014250883.html)**

President Donald Trump is an enthusiastic advocate for swift AI development in America, dismissing regulation as a curb on competing with China.He dismisses regulation as a constraint on US competitiv...

Yahoo • 16m ago

---

**[AI Unearths Football Talent Beyond Scouts' Radar](https://www.barrons.com/articles/ai-unearths-football-talent-beyond-scouts-radar-3fc540d3)**

Barron's • 17m ago

---

**[Authorities struggle to stop AI tools generating nude images](https://www.pbs.org/video/ai-abuse-1780349345/)**

Authorities struggle to stop AI tools generating nude images without consent

PBS • 22m ago

---

**[Nvidia Introduces First PCs Designed for AI Agents](https://www.wsj.com/tech/ai/nvidia-unveils-ai-laptops-rtx-spark-47445bcd)**

WSJ • 4h ago

---

---

## HackerNews: "ai"

**[Anthropic surpasses OpenAI to become most valuable AI startup](https://news.ycombinator.com/item?id=48336233)**

Anthropic has become the most valuable artificial intelligence startup in the world, surpassing OpenAI in market valuation. Following a new funding round, the valuation of the developer behind the Claude AI assistant has approached the $1 trillion mark, reports a Qazinform News Agency correspondent.

⬆️ 420 • 💬 471 • 2d ago • [Qazinform.com](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

---

**[United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://news.ycombinator.com/item?id=48345248)**

The flight crew issued repeated warnings and a one-minute ultimatum to passengers, demanding they turn off their Bluetooth devices.

⬆️ 412 • 💬 894 • 1d ago • [Simple Flying](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

---

**[The solution might be cancelling my AI subscription](https://news.ycombinator.com/item?id=48345896)**

⬆️ 376 • 💬 232 • 1d ago • [thoughts.hmmz.org](https://thoughts.hmmz.org/2026-05-31.html)

---

**[AI Agent Guidelines for CS336 at Stanford](https://news.ycombinator.com/item?id=48359232)**

Student version of Assignment 1 for Stanford CS336 - Language Modeling From Scratch - stanford-cs336/assignment1-basics

⬆️ 324 • 💬 115 • 9h ago • [GitHub](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)

---

**[DuckDuckGo makes its 'no-AI' search engine easier to access as its traffic booms](https://news.ycombinator.com/item?id=48359130)**

Alternative search engine DuckDuckGo launches 'no AI' web extensions for Chrome and Firefox users.

⬆️ 283 • 💬 141 • 9h ago • [TechCrunch](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)

---

**[Odysseus – self-hosted AI workspace](https://news.ycombinator.com/item?id=48346693)**

Self-hosted AI workspace. . Contribute to pewdiepie-archdaemon/odysseus development by creating an account on GitHub.

⬆️ 213 • 💬 94 • 1d ago • [GitHub](https://github.com/pewdiepie-archdaemon/odysseus)

---

**[AI job grief: A psychological crisis hitting tech workers](https://news.ycombinator.com/item?id=48336760)**

Across hundreds of Reddit threads and a small body of clinical literature, AI-driven displacement is producing an emotional category that most closely resembles grief, and the institutions causing it have no language for it.

⬆️ 197 • 💬 200 • 2d ago • [jackmaguire.org](https://jackmaguire.org/blog/ai-job-grief/)

---

**[The Speed of Prototyping in the Age of AI](https://news.ycombinator.com/item?id=48347153)**

How AI has changed the way I prototype, plan, and ship; and what I'm doing to keep my hands dirty.

⬆️ 189 • 💬 94 • 1d ago • [darylcecile.net](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai)

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://news.ycombinator.com/item?id=48335388)**

⬆️ 184 • 💬 173 • 2d ago • [wsj.com](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)

---

**[Florida sues OpenAI and Sam Altman over AI risks](https://news.ycombinator.com/item?id=48358667)**

⬆️ 179 • 💬 159 • 9h ago • [politico.com](https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215)

---

---

## YouTube Videos: "ai"

**[This AI Warning on The Joe Rogan Experience is SPOT ON. We Must Prepare for This](https://www.youtube.com/watch?v=PA2WhIU0Ldk)**

For years, Glenn has warned that AI will turn into AGI by 2030. But recently, Marc Andreessen told Joe Rogan that it's already here ...

📺 Glenn Beck

👁️ 158K • 👍 8K • 💬 1K • ⏱️ 14:55 • 1d ago

---

**[Spencer Pratt’s Viral AI Ads Are Shaking Up the LA Mayoral Race](https://www.youtube.com/watch?v=H4pvrghPl7k)**

Ben Shapiro breaks down the Los Angeles mayoral race, slamming Karen Bass and Nithya Rahman over the city's homelessness ...

📺 Ben Shapiro

👁️ 15K • 👍 1K • 💬 123 • ⏱️ 6:17 • 4h ago

---

**[Figure AI Appears To Be Faking Its Demos](https://www.youtube.com/watch?v=Juc-IyTdSho)**

Check out our second channel Broken Business Models: https://www.youtube.com/@UCQUOscigSQWCVG8m-ZC8wiw Our ...

📺 Wall Street Millennial

👁️ 57K • 👍 3K • 💬 694 • ⏱️ 13:26 • 7h ago

---

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 278K • 👍 4K • 💬 412 • ⏱️ 1:32:36 • 2d ago

---

**[Elon Musk&#39;s DISTURBING AI Warning: You Have No Idea What&#39;s Coming in 2027](https://www.youtube.com/watch?v=kAmL_mM4ChM)**

Over the last decade, Elon Musk repeatedly warned that artificial intelligence could become humanity's biggest existential threat, ...

📺 Neural Nutshell

👁️ 11K • 👍 363 • 💬 132 • ⏱️ 15:53 • 2d ago

---

**[Sam Altman: People are right to be anxious about AI](https://www.youtube.com/watch?v=4qGz2uFuRvs)**

Sam Atlman, OpenAI CEO, joins 'Power Lunch' to discuss the pace of AI buildouts, what consumers believe around AI and much ...

📺 CNBC Television

👁️ 8K • 👍 161 • 💬 89 • ⏱️ 5:47 • 6h ago

---

**[AI Is Evolving Faster Than We Thought - Dwarkesh Patel](https://www.youtube.com/watch?v=JmCXZQ2xiZo)**

Dwarkesh Patel, one of Silicon Valley's favorite podcasters, explains how much AI has improved in the last couple of years - going ...

📺 TRIGGERnometry Clips

👁️ 17K • 👍 355 • 💬 150 • ⏱️ 17:33 • 1d ago

---

**[AI Whistleblower WARNS: We&#39;re Not Ready For What&#39;s Coming In 2027](https://www.youtube.com/watch?v=QqIqEI9CiZs)**

Evolutionary biologist Bret Weinstein claims that humans must come to terms with the fact that extinction is inevitable and that all ...

📺 Neural Nutshell

👁️ 4K • 👍 196 • 💬 51 • ⏱️ 18:34 • 1d ago

---

**[I Created an AI Clone… Biggest Mistake Ever!](https://www.youtube.com/watch?v=3reHSl0aOH4)**

I created my own AI clone, but things quickly turned completely out of control! Was creating an AI clone the biggest mistake ever?

📺 Ivan and Maria

👁️ 104K • 👍 1K • 💬 14 • ⏱️ 25:11 • 2d ago

---

**[&quot;Most Actors Are Going Broke, Jobs Gone Forever...&quot; First AI Film Has Hollywood Scared, Cost $2,000](https://www.youtube.com/watch?v=9-pWHt3utu8)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/antondaniels Join the Bag Chasers ...

📺 Anton Daniels

👁️ 79K • 👍 3K • 💬 2K • ⏱️ 11:34 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 35,783 • ❤️ 805 • 5d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 45,698 • ❤️ 692 • 6d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 37,893 • ❤️ 396 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,533,393 • ❤️ 1,222 • 1mo ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 467 • 22h ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 9,256 • ❤️ 195 • 19h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,851,826 • ❤️ 4,532 • 26d ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 577 • ❤️ 239 • 7d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 3,041 • ❤️ 1,002 • 4d ago

---

**[PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)**

*PaddlePaddle*

PaddleOCR-VL-1.6 is a multimodal OCR model capable of text spotting, recognition, and layout analysis across various document types. It excels at extracting structured information like tables, charts, and formulas from multilingual documents, leveraging ERNIE 4.5 for enhanced understanding.

`image-text-to-text` `958.6M`

⬇️ 3,190 • ❤️ 156 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 212 • 💬 3 • ⭐ 4,068 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 83 • 💬 3 • ⭐ 81,668 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 36 • 💬 3 • ⭐ 27,910 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 37 • 💬 5 • ⭐ 3,911 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 5 • 💬 1 • ⭐ 6,660 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,971 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 6 • 💬 0 • ⭐ 1,601 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[VLM3: Vision Language Models Are Native 3D Learners](https://huggingface.co/papers/2605.30561)**

*Zhipeng Cai, Zhuang Liu, Yunyang Xiong et al. (6 authors)*

🏢 AI at Meta

Vision Language Models can be adapted for 3D understanding tasks through simple architectural modifications and text-based training, achieving performance comparable to specialized vision models without requiring complex designs or extensive data augmentation.

▲ 13 • 💬 2 • ⭐ 75 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30561) • [💻 code](https://github.com/facebookresearch/VLM3)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 50 • 💬 3 • ⭐ 456 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 15 • 💬 2 • ⭐ 2,795 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`JavaScript`

⭐ 21.3k • 🔱 2.6k • 5m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.8k • 🔱 565 • 3d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.2k • 🔱 666 • 2d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.9k • 🔱 205 • 5h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.7k • 🔱 260 • 11h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 400 • 11d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.4k • 🔱 365 • 15d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.2k • 🔱 150 • 5h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.2k • 🔱 223 • 7d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 212 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
