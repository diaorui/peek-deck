---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-01T20:56:16.631357+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 01, 2026 at 20:56 UTC  
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

🔗 [nytimes.com](https://www.nytimes.com/2026/06/01/opinion/artificial-intelligence-bernie-sanders.html) • 9h ago

---

**[I analyzed 25,500 LLM resume screenings to measure hiring bias. The results are a wake-up call.](https://www.reddit.com/r/artificial/comments/1ttsr9b/i_analyzed_25500_llm_resume_screenings_to_measure/)**

Hey Reddit, I just published a study analyzing 25,500 LLM resume evaluations to measure hiring bias. By swapping minor identity and demographic variables on the exact same work history across 10 different models, an independent AI auditor flagged a staggering 45% bias rate driven by "silent bias." Instead of saying anything overtly offensive, models invent professional-sounding excuses to penalize candidates, like when a model dropped its score after I changed the university to MIT, suddenly claiming the candidate's experience wasn't relevant despite praising that exact same experience on the baseline resume. We also found a massive 6x difference in stability between systems, with Qwen and older Gemini models being highly volatile, while the Claude models, Mistral-Large, and Llama 4 proved to be the most stable and fair. Ultimately, AI screening tools are outputting highly subjective, unpredictable opinions driven by statistical noise rather than objective truth, making them a massive liability under regulations like the EU AI Act. You can read the full write-up and explore our interactive data app here: https://re-cinq.com/blog/ai-hiring-bias-25500-llm-evaluations

7h ago

---

**[Cognitive debt might be the most underrated problem AI is creating](https://www.reddit.com/r/artificial/comments/1tteup9/cognitive_debt_might_be_the_most_underrated/)**

Everyone knows about tech debt. You cut corners on code quality to ship faster, and you pay for it later. We're definitely watching a new version of that emerge in real time, except instead of deferring manageable code, you're deferring actual understanding. And unlike tech debt, cognitive debt compounds invisibly. You don't get a failing test suite. You just get someone who can't debug their own project, can't evaluate whether the AI's suggestion is good, and can't extend what they've built without prompting their way through it again. What I keep thinking about is where this leads at scale. Right now it's mostly developers vibe-coding their way through projects they half-understand. But AI is moving into law, medicine, and finance. The same dynamic follows: people making consequential decisions with tools they can't interrogate, in domains where "I'll just re-prompt it" isn't a recovery strategy. The pessimistic, or maybe rational read is that judgment without foundational understanding is just confident ignorance, and we're building entire careers on that foundation right now. Curious what people here think. Does cognitive debt get self-correcting as the stakes get high enough? Or are we sleepwalking into a generation of professionals who are deeply dependent on systems they fundamentally don't understand?

18h ago

---

**[How much published AI research is wrong because of data leakage?](https://www.reddit.com/r/artificial/comments/1tu0ri0/how_much_published_ai_research_is_wrong_because/)**

There is a Princeton paper by Kapoor and Narayanan. They found data leakage in close to 300 papers across 17 fields, including medicine and economics. Leakage means the model was trained on information it would never have when it makes a real prediction. So it looks great on the test set and then fails in the real world. My favorite example is civil war prediction. Complex models were reported to crush old logistic regression. Once the leakage was fixed, the fancy models were no better than the decades old stats. I have built enough models to know how easy this is to do by accident. You scale the data before you split it, or you use one feature that is really a stand in for the answer, and your numbers look amazing. So now when I read another "AI cracked X" headline, my first thought is whether anyone checked it for leakage.

2h ago

---

**[My AI chats are becoming dead archives.](https://www.reddit.com/r/artificial/comments/1ttpxsn/my_ai_chats_are_becoming_dead_archives/)**

Maybe this is just me using these tools badly, but I've noticed a pattern with ChatGPT and Claude. I’ll have a really useful conversation about something like an idea, a plan, a bit of writing, a coding problem, whatever, and in the moment it feels like I’m making real progress. Then a week later I vaguely remember that we talked about it, but I can’t remember where, or what the useful part actually was and what I was supposed to do next. So I search, find a few old chats, open them… and now I’m scrolling through this massive thread trying to reconstruct why it mattered. It's exhausting and I feel I'm wasting time recollecting things. So sometimes I start over, hoping that the AI itself will remember the details, adding to the waste of time and the frustration. And the more ideas I develop the bigger this problem becomes. And it's only going to get worse. I’ve started leaving myself a short note at the end of useful conversations, but I never remember to do it consistently. Not sure if this is an actual problem or just the natural cost of using AI for messy thinking.

8h ago

---

**[Florida sues OpenAI, alleging it’s unsafe for children](https://www.reddit.com/r/artificial/comments/1tu0i8n/florida_sues_openai_alleging_its_unsafe_for/)**

Florida is suing OpenAI and its CEO Sam Altman, alleging they know ChatGPT is not safe, especially for minors.

🔗 [CNN](https://www.cnn.com/2026/06/01/business/florida-sues-chatgpt-openai-sam-altman) • 2h ago

---

**[Why do people hate/refuse to use anything with AI involved?](https://www.reddit.com/r/artificial/comments/1ttw89x/why_do_people_haterefuse_to_use_anything_with_ai/)**

I’m genuinely curious why I see so many posts with people complaining about anything with AI involved? It’s not just games, it’s everything. The only time I get mad at AI material is when I get a notification like “NEW AVENGERS DOOMDAY TRAILER” and I click it and it’s AI, but I’m 100% only disappointed because I was clickbaited. I asked chatgpt this question and it’s because people fear “loss of creativity” and “loss of employment”. Is that really the only reason? I’m 33 and I use chatgpt (AI) for day to day questions, which means it would be hypocritical if I were to disapprove of AI use in anything at all, in my opinion. There is nothing wrong with being a hypocrite, we’ve all been hypocritical at some point or another in our lives, but please tell me why you dislike AI if it applies to you. I really want to know.

5h ago

---

**[Recommended models for document data analysis?](https://www.reddit.com/r/artificial/comments/1ttyfal/recommended_models_for_document_data_analysis/)**

Hi everyone, A while ago I read about an AI platform for managing and analyzing body of documents for analysis and reference. From what I remember, it was a semi-closed system where you could upload your own source materials and the model could analyze and reference your uploaded documents directly. From what I recall, it wasn’t self-hosted. Does anyone know of a tool like this or recommend something that performs better than other models? Any recommendations, even if it's a different tool with similar capabilities, would be really helpful. Thanks in advance!

3h ago

---

**[NVIDIA just released a 32B open reasoning model for robotaxis](https://www.reddit.com/r/artificial/comments/1ttuhhd/nvidia_just_released_a_32b_open_reasoning_model/)**

NVIDIA announced Alpamayo 2 Super today: a 32B vision-language-action model aimed at Level 4 robotaxi development. The interesting part is not only the model size. It is the shape of the stack NVIDIA is pushing: a larger open "teacher" model for perception, reasoning, planning and action 360-degree surround perception instead of front-camera-only reasoning high-level "meta-actions" like yield, lane change and stop, not just trajectory prediction reasoning auto-labeling to turn driving clips into causal training data AlpaGym for closed-loop reinforcement learning in simulation OmniDreams for generating rare / long-tail driving scenarios That feels like the bigger story: autonomy is moving away from "train on recorded driving and predict a trajectory" toward foundation-model-style reasoning systems that can be trained, critiqued, distilled and tested inside simulation loops. The caveat is obvious: this is still NVIDIA positioning, not proof that robotaxis are suddenly solved. Model weights are expected this summer, and real-world validation is the hard part. But if open AV foundation models become normal, smaller autonomy teams may stop rebuilding the same perception/planning infrastructure from scratch and start competing on data, safety validation, deployment constraints and closed-loop testing. Source: NVIDIA press release https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Alpamayo-2-Super-Open-Reasoning-Model-for-Robotaxis/default.aspx

6h ago

---

**[Anthropic confidentially files to go public](https://www.reddit.com/r/artificial/comments/1tty3bm/anthropic_confidentially_files_to_go_public/)**

Anthropic on Monday said it filed plans for an initial public offering, setting it up for a share sale that could value the company in the trillion-dollar range as it races against rival OpenAI.

🔗 [CNN](https://www.cnn.com/2026/06/01/tech/anthropic-ipo-filing) • 4h ago

---

---

## Google News: "ai"

**[California’s Public Universities Went All in on A.I. Now They’re Tearing Themselves Apart.](https://www.nytimes.com/2026/06/01/magazine/ai-university-college-california.html)**

The New York Times • 11h ago

---

**[Nvidia Introduces First PCs Designed for AI Agents](https://www.wsj.com/tech/ai/nvidia-unveils-ai-laptops-rtx-spark-47445bcd)**

WSJ • 4h ago

---

**[Nvidia announces new AI chip for personal computers](https://www.bbc.com/news/articles/crmp9mppvzro)**

The technology giant's boss Jensen Huang called the move the "reinvention of the computer".

BBC • 9h ago

---

**[Has Micron replaced Nvidia as the 'It' stock for the AI trade? (MU:NASDAQ)](https://seekingalpha.com/news/4598510-has-micron-replaced-nvidia-as-the-it-stock-for-the-ai-trade)**

Micron (MU) is surging as the hottest AI trade, outpacing Nvidia (NVDA) on 1-year returns and Quant Ratings—see what’s driving it and act now.

Seeking Alpha • 1h ago

---

**[Stargate live updates: OpenAI's Altman says 'people are right to be anxious' about AI](https://www.cnbc.com/2026/06/01/stargate-project-michigan-live-updates.html)**

OpenAI, Oracle and Related Digital discuss the Stargate Michigan buildout, AI infrastructure, jobs and community plans.

CNBC • 43m ago

---

**[AI video depicts Washington arts center removing Trump's name](https://www.yahoo.com/news/politics/articles/ai-video-depicts-washington-arts-200718734.html)**

A US judge ruled May 29 that the famed Kennedy Center for the Performing Arts had been illegally renamed after Donald Trump and that his name would need to be removed from the facade. But a video spre...

Yahoo • 48m ago

---

**[The election that will shape the future of AI](https://www.politico.com/newsletters/forecast/2026/06/01/the-election-that-will-shape-the-future-of-ai-00944775)**

Politico • 26m ago

---

**[Remote work — not AI — has sidelined recent college graduates, research finds](https://www.npr.org/2026/06/01/nx-s1-5843076/remote-work-college-graduates-unemployment-ai)**

Research from the New York Fed finds that younger college graduates have been sidelined by remote work in recent years, as companies may be reluctant to hire those needing more training and mentoring.

NPR • 2h ago

---

**[GoPro Warns of Going-Concern Risk Amid AI-Fueled Memory Crunch](https://www.bloomberg.com/news/articles/2026-06-01/gopro-warns-of-going-concern-risk-amid-ai-fueled-memory-crunch)**

Bloomberg.com • 1h ago

---

**[Anthropic confidentially files IPO prospectus with SEC, prepping Wall Street for landmark AI deal](https://www.cnbc.com/2026/06/01/anthropic-ipo-s1-prospectus.html)**

Anthropic said it confidentially filed its IPO prospectus with the SEC, setting up a potentially historic share sale for investors ready to jump into AI.

CNBC • 4h ago

---

---

## HackerNews: "ai"

**[Anthropic surpasses OpenAI to become most valuable AI startup](https://news.ycombinator.com/item?id=48336233)**

Anthropic has become the most valuable artificial intelligence startup in the world, surpassing OpenAI in market valuation. Following a new funding round, the valuation of the developer behind the Claude AI assistant has approached the $1 trillion mark, reports a Qazinform News Agency correspondent.

⬆️ 420 • 💬 471 • 2d ago • [Qazinform.com](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

---

**[United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://news.ycombinator.com/item?id=48345248)**

The flight crew issued repeated warnings and a one-minute ultimatum to passengers, demanding they turn off their Bluetooth devices.

⬆️ 411 • 💬 865 • 1d ago • [Simple Flying](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

---

**[The solution might be cancelling my AI subscription](https://news.ycombinator.com/item?id=48345896)**

⬆️ 371 • 💬 232 • 1d ago • [thoughts.hmmz.org](https://thoughts.hmmz.org/2026-05-31.html)

---

**[DuckDuckGo makes its 'no-AI' search engine easier to access as its traffic booms](https://news.ycombinator.com/item?id=48359130)**

Alternative search engine DuckDuckGo launches 'no AI' web extensions for Chrome and Firefox users.

⬆️ 256 • 💬 130 • 4h ago • [TechCrunch](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)

---

**[Odysseus – self-hosted AI workspace](https://news.ycombinator.com/item?id=48346693)**

Self-hosted AI workspace. . Contribute to pewdiepie-archdaemon/odysseus development by creating an account on GitHub.

⬆️ 211 • 💬 93 • 1d ago • [GitHub](https://github.com/pewdiepie-archdaemon/odysseus)

---

**[AI Agent Guidelines for CS336 at Stanford](https://news.ycombinator.com/item?id=48359232)**

Student version of Assignment 1 for Stanford CS336 - Language Modeling From Scratch - stanford-cs336/assignment1-basics

⬆️ 205 • 💬 91 • 4h ago • [GitHub](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)

---

**[AI job grief: A psychological crisis hitting tech workers](https://news.ycombinator.com/item?id=48336760)**

Across hundreds of Reddit threads and a small body of clinical literature, AI-driven displacement is producing an emotional category that most closely resembles grief, and the institutions causing it have no language for it.

⬆️ 197 • 💬 200 • 2d ago • [jackmaguire.org](https://jackmaguire.org/blog/ai-job-grief/)

---

**[The Speed of Prototyping in the Age of AI](https://news.ycombinator.com/item?id=48347153)**

How AI has changed the way I prototype, plan, and ship; and what I'm doing to keep my hands dirty.

⬆️ 188 • 💬 94 • 1d ago • [darylcecile.net](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai)

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://news.ycombinator.com/item?id=48335388)**

⬆️ 183 • 💬 173 • 2d ago • [wsj.com](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)

---

**[To have a moral stance on AI is to be an outcast, and it sucks](https://news.ycombinator.com/item?id=48337676)**

I know the technology, I understand what it's doing and I know the impact, so I am vehemently anti-AI.  I do not believe any positive out...

⬆️ 146 • 💬 313 • 2d ago • [Martyn's random musings](https://musings.martyn.berlin/to-have-a-moral-stance-on-ai-is-to-be-an-outcast-and-it-sucks)

---

---

## YouTube Videos: "ai"

**[Best FREE AI Agent Tools That Actually Work in 2026 (I Tried All)](https://www.youtube.com/watch?v=2GOfWK5M3fg)**

Best Free AI Agent Tool is Base44 https://base44.pxf.io/c/6440076/3820726/25619?trafcat=agent&sharedid=agent5 ✓ Claim your ...

📺 Mikey No Code

👁️ 13K • 💬 7 • ⏱️ 20:44 • 6h ago

---

**[This AI Warning on The Joe Rogan Experience is SPOT ON. We Must Prepare for This](https://www.youtube.com/watch?v=PA2WhIU0Ldk)**

For years, Glenn has warned that AI will turn into AGI by 2030. But recently, Marc Andreessen told Joe Rogan that it's already here ...

📺 Glenn Beck

👁️ 146K • 👍 8K • 💬 987 • ⏱️ 14:55 • 1d ago

---

**[Sam Altman: People are right to be anxious about AI](https://www.youtube.com/watch?v=4qGz2uFuRvs)**

Sam Atlman, OpenAI CEO, joins 'Power Lunch' to discuss the pace of AI buildouts, what consumers believe around AI and much ...

📺 CNBC Television

👁️ 2K • 👍 52 • 💬 55 • ⏱️ 5:47 • 1h ago

---

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 277K • 👍 4K • 💬 408 • ⏱️ 1:32:36 • 2d ago

---

**[AI Is Evolving Faster Than We Thought - Dwarkesh Patel](https://www.youtube.com/watch?v=JmCXZQ2xiZo)**

Dwarkesh Patel, one of Silicon Valley's favorite podcasters, explains how much AI has improved in the last couple of years - going ...

📺 TRIGGERnometry Clips

👁️ 16K • 👍 338 • 💬 148 • ⏱️ 17:33 • 1d ago

---

**[Anthropic AI Buying Microsoft Maia Chips - NVIDIA is Dead](https://www.youtube.com/watch?v=ig4Sw4AwXng)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 8K • 👍 365 • 💬 71 • ⏱️ 12:45 • 8h ago

---

**[Elon Musk&#39;s DISTURBING AI Warning: You Have No Idea What&#39;s Coming in 2027](https://www.youtube.com/watch?v=kAmL_mM4ChM)**

Over the last decade, Elon Musk repeatedly warned that artificial intelligence could become humanity's biggest existential threat, ...

📺 Neural Nutshell

👁️ 11K • 👍 353 • 💬 128 • ⏱️ 15:53 • 2d ago

---

**[Jensen Huang Unveils NVIDIA&#39;s AI Laptop Revolution | The Future Of Computing Is Here Explained](https://www.youtube.com/watch?v=UgJKf49YUHY)**

NVIDIA CEO Jensen Huang has unveiled a bold vision for the future of computing — a world where laptops are built not just for ...

📺 NDTV Profit

👁️ 9K • 👍 58 • 💬 14 • ⏱️ 2:46 • 14h ago

---

**[EXACTLY How to Make an AI Short Film (Full Workflow)](https://www.youtube.com/watch?v=0v534yAyhwg)**

Make Your Own Short Film with Higgsfield https://youricreates.com/short-films In this video, I show my full workflow for making a ...

📺 Youri van Hofwegen

👁️ 9K • 💬 11 • ⏱️ 16:50 • 5h ago

---

**[AI Whistleblower WARNS: We&#39;re Not Ready For What&#39;s Coming In 2027](https://www.youtube.com/watch?v=QqIqEI9CiZs)**

Evolutionary biologist Bret Weinstein claims that humans must come to terms with the fact that extinction is inevitable and that all ...

📺 Neural Nutshell

👁️ 4K • 👍 191 • 💬 50 • ⏱️ 18:34 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 35,783 • ❤️ 775 • 5d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 45,698 • ❤️ 685 • 6d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 37,893 • ❤️ 375 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,533,393 • ❤️ 1,211 • 1mo ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 464 • 17h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,851,826 • ❤️ 4,528 • 26d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 9,256 • ❤️ 186 • 14h ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 577 • ❤️ 236 • 6d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 3,041 • ❤️ 1,002 • 4d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 149,543 • ❤️ 439 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 211 • 💬 3 • ⭐ 4,068 • 11d ago

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

▲ 5 • 💬 1 • ⭐ 6,624 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,940 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[VLM3: Vision Language Models Are Native 3D Learners](https://huggingface.co/papers/2605.30561)**

*Zhipeng Cai, Zhuang Liu, Yunyang Xiong et al. (6 authors)*

🏢 AI at Meta

Vision Language Models can be adapted for 3D understanding tasks through simple architectural modifications and text-based training, achieving performance comparable to specialized vision models without requiring complex designs or extensive data augmentation.

▲ 11 • 💬 1 • ⭐ 58 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30561) • [💻 code](https://github.com/facebookresearch/VLM3)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 6 • 💬 0 • ⭐ 1,601 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 15 • 💬 2 • ⭐ 2,783 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 50 • 💬 3 • ⭐ 456 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`JavaScript`

⭐ 19.5k • 🔱 2.4k • 1m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.8k • 🔱 563 • 3d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.2k • 🔱 665 • 2d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.9k • 🔱 205 • 22m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.7k • 🔱 257 • 6h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 399 • 10d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.4k • 🔱 365 • 15d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.2k • 🔱 148 • 19m ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.2k • 🔱 223 • 7d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 212 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
