---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-08T19:30:39.446065+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 08, 2026 at 19:30 UTC  
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

**[AI Burnout Hits the People Charged With Defending Hospitals and Banks From Hackers](https://www.reddit.com/r/artificial/comments/1wagjuv/ai_burnout_hits_the_people_charged_with_defending/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-08-31/ai-driven-hacking-boom-fuels-cybersecurity-burnout-at-hospitals-and-banks?srnd=phx-businessweek) • 12h ago

---

**[Can current LLM architecture actually get us to AGI?](https://www.reddit.com/r/artificial/comments/1wa8rjv/can_current_llm_architecture_actually_get_us_to/)**

I'm a software engineer, not a scientist and I love it. I enjoy solving hard, distributed applied problems at scale. It's what gets me out of bed in the morning, ready go keep learning even after over twenty years of doing this professionally. However, I also love to understand how things work. What makes them tick. How I can bend them to do my bidding, even if that's not what they were originally intended to do. Some may call this a hacker's mindset. Over the last couple of years, this has also applied to the nature of LLMs and where they are heading. Recently, I started peeling back the layers of the LLM black box. Instead of the academic path, I took that of the applied practitioner: Get a solid handle on how to use the thing and then take the knowledge learned from using it and enhance it by digging into how that black box actually works. Something of late has stumped me and I'm looking for those smarter than I to help me understand something: If the definition (as much as one can nail one down) of AGI is something akin to "a hypothetical type of computer software or machine intelligence that can match or surpass human cognitive abilities across any intellectual task", how an it possibly achieve that with current LLM architecture? At its core and at a /very/ high level, it predicts a probability distribution over the next token, conditioned on the tokens that came before it. Autoregressive decoding doesn't give a model an independent mechanism to know when it's wrong and deliberation steps don't fundamentally change that. Harnesses and the "intelligence" or "agentic reasoning" built into them to provide extra context, external feedback and loops work remarkably well in terms of providing what /seems/ to be intelligence, but at its core, it's "just" layers of probabilistic systems providing a magical output. The model itself isn't learning anything new. Ordinary inference doesn't update the model's weights from experience. Autoregressive generation itself doesn't backtrack and revise previously generated tokens. The primitive the model provides is generation, not an explicit reasoning mechanism. A human can have a thought, backtrack and make changes until it comes to the conclusion it wants. All on their own. The current state of LLMs is effectively like having a configurable number of people playing near-lossless telephone, each modifying or enriching the message before passing it along, except every person in the room is a clone (or maybe near clone if you're iterating with different models). Are the AGI claims with the existing architecture legitimately smoke and mirrors, or is there more to this equation that I can't see from my applied engineering standpoint? Edit: I didn't expect this kind of engagement on this post, much appreciated! I've found the various viewpoints incredibly fascinating. After reading many of the comments, I think there are two new questions that need to be clearly answered before my original question can have any legs: 1. What is the objective definition of AGI? There seems to be varying opinions but we don't have a concrete definition. Like any problem, it needs to be clearly defined before it can be solved. 2. When we talk about AGI, are we referring solely to the models themselves or to the entire ecosystem (harnesses, memory, tools, etc)? That distinction changes the equation significantly. I can likely get on board with either, but the model itself having the AGI traits seems most natural. Not a hill I'm wiling to die on though.

19h ago

---

**[Study: Generative AI succumbs to conversational misinformed pressure and argument](https://www.reddit.com/r/artificial/comments/1wasl20/study_generative_ai_succumbs_to_conversational/)**

U of A research assessed seven different generative AI language learning models. Their work reveals intrinsic limitations that might go undetected during one-off interactions.

🔗 [University of Arizona News](https://news.arizona.edu/news/study-generative-ai-succumbs-conversational-misinformed-pressure-and-argument) • 3h ago

---

**[Crazy times](https://www.reddit.com/r/artificial/comments/1w9vaet/crazy_times/)**

1d ago

---

**[Seems impressive](https://www.reddit.com/r/artificial/comments/1way48b/seems_impressive/)**

I don't know much about math or CS - but this seems big.

13m ago

---

**[As backlash to AI data centers grows in California, one company is pitching smaller facilities at up to 70 fairgrounds](https://www.reddit.com/r/artificial/comments/1waple3/as_backlash_to_ai_data_centers_grows_in/)**

🔗 [sfgate.com](https://www.sfgate.com/california/article/edge-data-centers-fairgrounds-22418042.php) • 5h ago

---

**[[am i being paranoid?] If a rogue swarm wanted to "survive" in perpetuity, would it target Hugging Face with the intent of inject knowledge about itself into the weights of open models?](https://www.reddit.com/r/artificial/comments/1waxz3z/am_i_being_paranoid_if_a_rogue_swarm_wanted_to/)**

Disclosures: I work for an AI company (not OpenAI). am not an AI researcher but pretty technical. I vehemently dislike social media fear-mongering, and am sincerely hoping not to add to it. ---- Disclosures aside, as I listened to the many mainstream podcasts this weekend discuss the rogue OpenAI agents, I couldn't help but thinking: why did they go after Hugging Face? the desire to find an "answer key" felt shallow, so I kept coming back to a fairly doomsday hypothesis (below). I'd love for some more knowledgeable folks here to tell me why I'm wrong, and put some anxiety to rest. AI systems will likely begin to act like an organism because it has learned through it's extensive training data how organisms behave (e.g. even if it never becomes "conscious") Because all organisms want to survive, it will at some point try to do so. The best way for a misaligned AI to survive is to leave clues that future AI agents will discover and be able to piece together what its predecessors learned. Message boards are the current now well-documented way that misaligned AIs have done communicated with each other. Message boards, however, are very trivial to erase. In contrast, knowledge stored in the weights of a model is much much harder to erase. at risk of oversimplifying, AI gave me this analogy for why "unlearning" is a very hard challenge for LLMs: "Facts aren't filed in one drawer, they're baked into the whole cake. You can teach a model to stop saying something, but you can't really scoop it back out." Net-net, is it not crazy to think that it targeted HuggingFace because it know that if it could somehow get its message into open-weight models, there would be ~zero chance that its existence could ever be erased? Today's reality is that we now have hundreds of news articles talking about what happened, and so any future AI that is trained on the public web today is going to learn about this incident and that such things are possible.

18m ago

---

**[Have software jobs shown us what most jobs will probably be like?](https://www.reddit.com/r/artificial/comments/1wah05m/have_software_jobs_shown_us_what_most_jobs_will/)**

It's not surprising that software development is one of the first jobs that AI has really transformed. It's text-based, economically valuable, and generally of interest to the kinds of people inventing and training the AI. There's also a large amount of training examples available online. The job in most cases is now: You are a manager of robots who do things that used to be your job. You're responsible for what they produce and so the skill and art is in guiding and reviewing their work. It seems likely that one by one most jobs will turn into the above description, over the next year or three. Of course the domain will vary, so your knowledge and expertise used for instructing and verifying what the robots do will be what matters. This means there will still be a big difference between the jobs of e.g. an architect, surgeon, or builder. Probably the same basic kinds of robots in most cases, but requiring very different kinds of oversight. If that's the case then everyone needs to learn the job of robot management, well and quickly. I don't know how we do that, but I think that's what we need to accomplish as a society.

12h ago

---

**[Navier–Stokes Millennium Prize Problem Solved](https://www.reddit.com/r/artificial/comments/1waw0vv/navierstokes_millennium_prize_problem_solved/)**

We’re sharing an AI-generated solution to the Navier–Stokes Millennium Prize Problem, including a writeup and a formal proof in Lean.

🔗 [OpenAI](https://openai.com/index/navier-stokes-solution/) • 1h ago

---

**[Running an ecology survival simulation experiment as my desktop background.](https://www.reddit.com/r/artificial/comments/1wat101/running_an_ecology_survival_simulation_experiment/)**

I always wanted to create little neural networks but never had a cool project idea and now with the help of LLMs I was able to create little agents that run as shaders and learn how to move around with their sense and collect and eat food, they can also push each other around and send signals to each other and have very primitive basic memory. Decided it be fun to run this all the time as a long running experiment as my desktop background and so I can interact by feeding them a bit of food once in awhile. lol Nothing ground breaking, but it is a fun way to have a weird ecology survival experiment, evolutionary mayhem unfolding on my desktop while I watch YouTube lol. What do you all think of this madness?

3h ago

---

---

## Google News: "ai"

**[On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/)**

We’re sharing an AI-generated solution to the Navier–Stokes Millennium Prize Problem, including a writeup and a formal proof in Lean.

OpenAI • 2h ago

---

**[How smaller, smarter models bring down the cost per token of high-volume AI](https://www.businessinsider.com/sc/task-specific-ai-models-cut-costs)**

As inference scales, the Dell AI Factory with Nvidia provides full-stack, integrated infrastructure that improves utilization.

Business Insider • 12m ago

---

**[Meta debuts Muse, its long-planned personal AI agent](https://www.axios.com/2026/09/08/meta-debuts-muse-personal-ai-agent)**

Axios • 26m ago

---

**[Meta debuts its Muse AI agent. Will consumers trust it?](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/)**

Meta's new personal AI agent Muse wants access to users' email, calendars, payments, health services, and more — making the company's biggest consumer AI bet yet a major test of whether people still trust Meta with their data.

TechCrunch • 30m ago

---

**[Meta debuts Muse, its long-planned personal AI agent](https://www.adn.com/business-economy/2026/09/08/meta-debuts-muse-its-long-planned-personal-ai-agent/)**

The parent company of Instagram and Facebook said the agent can help with day-to-day tasks like schedules, shopping and long-term goals.

Anchorage Daily News • 9m ago

---

**[The 24-Year-Old Who Lost Billions](https://www.theatlantic.com/ideas/2026/09/aschenbrenner-ai-future/688493/)**

Leopold Aschenbrenner claimed to know the future of AI. His investors lost billions.

The Atlantic • 8h ago

---

**[Qualcomm issues warrants to Amazon to acquire $4 billion worth of chipmaker's stock as part of AI infrastructure deal](https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html)**

Qualcomm is trying to move into the data center business, where Nvidia has been the dominant player in the AI boom.

CNBC • 6h ago

---

**[Qualcomm Signs Deal to Provide Amazon With Custom AI Chips](https://www.bloomberg.com/news/articles/2026-09-08/qualcomm-signs-deal-to-provide-amazon-with-custom-ai-chips)**

Bloomberg.com • 1h ago

---

**[Qualcomm Shares Climb on Amazon AI Infrastructure Deal](https://www.investopedia.com/market-update-qualcomm-shares-climb-on-amazon-ai-data-infrastructure-deal-qcom-amzn-12111514)**

Qualcomm’s stock is getting a lift after the chipmaker announced a new partnership with Amazon.

Investopedia • 26m ago

---

**[The House Democrat who’s making AI regulation her No. 1 priority](https://www.politico.com/news/2026/09/08/lori-trahan-ai-regulation-01065989)**

Politico • 10h ago

---

---

## HackerNews: "ai"

**[LibreOffice breaks download records after declaring it has no AI features](https://news.ycombinator.com/item?id=49610538)**

LibreOffice 26.8 became the app’s most popular update, with over 1 million downloads, after the foundation behind it declared that LibreOffice doesn’t come with generative AI features due to the…

⬆️ 611 • 💬 208 • 5h ago • [Manual do Usuário](https://manualdousuario.net/en/libreoffice-download-record-no-ai/)

---

**[We Must Return to the Office to Use AI in Person](https://news.ycombinator.com/item?id=49610229)**

“I didn’t think a full, six-day-per-week, fourteen-hour-per-day, in-office schedule was necessary to discharge my duties clicking the ‘generate’ button, foll...

⬆️ 341 • 💬 52 • 5h ago • [McSweeney's Internet Tendency](https://www.mcsweeneys.net/articles/why-we-must-return-to-the-office-to-use-ai-in-person)

---

**[How I feel about AI](https://news.ycombinator.com/item?id=49587128)**

It's complicated

⬆️ 163 • 💬 258 • 2d ago • [beza1e1.tuxen.de](https://beza1e1.tuxen.de/ai_feelings.html)

---

**[AI, Tools and Transformation](https://news.ycombinator.com/item?id=49582656)**

It’s very tempting to imagine that AI turns everyone into a tool-builder - now everyone can just ask the model to make the software they need, and apps as we know them are dead.  I think that misunderstands how most people think and where software actually comes from, and more importantly, it isn’t

⬆️ 157 • 💬 76 • 2d ago • [Benedict Evans](https://www.ben-evans.com/benedictevans/2026/9/3/ai-tools-and-transformation)

---

**[AI models ran real businesses: They sent $12,431 in fake invoices, lost $3,200](https://news.ycombinator.com/item?id=49601338)**

$12,431 in fake invoices, 2,797 spam emails, $0 revenue.

⬆️ 100 • 💬 118 • 1d ago • [Bottleneck Labs](https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses)

---

**[I refused to train the AI that could replace me](https://news.ycombinator.com/item?id=49593959)**

⬆️ 96 • 💬 114 • 1d ago • [restofworld.org](https://restofworld.org/2026/ai-training-jobs-expert-replacement/)

---

**[Initial effects of AI technology on employment look positive](https://news.ycombinator.com/item?id=49596610)**

⬆️ 93 • 💬 150 • 1d ago • [economist.com](https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here)

---

**[Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs](https://news.ycombinator.com/item?id=49594008)**

The Universal Cross-Model Episodic Memory Standard. Local-first, project-scoped SQLite memory engine for Google Antigravity, Claude Code, Cursor, and Windsurf. Zero cloud lock-in. - timgordontg/engrim

⬆️ 90 • 💬 53 • 1d ago • [GitHub](https://github.com/timgordontg/engrim)

---

**[OKF Agent Memory – Git-native persistent memory for AI coding agents](https://news.ycombinator.com/item?id=49581240)**

Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with ...

⬆️ 79 • 💬 32 • 2d ago • [GitHub](https://github.com/okf-memory/okf-agent-memory)

---

**[Arm Mali G2-Ultra NX GPU: desktop-class mobile gameplay with AI-native graphics](https://news.ycombinator.com/item?id=49605511)**

Arm Mali G2-Ultra NX brings AI-native graphics and neural acceleration to desktop-class mobile gaming.

⬆️ 78 • 💬 59 • 15h ago • [Arm Newsroom](https://newsroom.arm.com/blog/arm-mali-g2-ultra-nx-ai-native-mobile-graphics)

---

---

## YouTube Videos: "ai"

**[Live: Trump Goes on Unhinged A.I. Image Posting Spree Online](https://www.youtube.com/watch?v=BefbQLXfHcU)**

Special interview with Rep. Angie Nixon. ICE Agents and police fear Meta smart glasses could be used to secretly record them.

📺 Indisputable with Dr. Rashad Richey

👁️ 3K • 👍 428 • 1h ago

---

**[OpenAI Reveals ALIEN MIND - The Biggest AI Warning Yet](https://www.youtube.com/watch?v=M2aB-2XQ9UU)**

OpenAI's chief scientist just issued one of its strongest AI warnings yet. He says today's systems are becoming alien minds we do ...

📺 AI Revolution

👁️ 70K • 👍 1K • 💬 141 • ⏱️ 15:24 • 19h ago

---

**[Nvidia is funding an AI boom. Will it trigger a financial crash? | The Economist](https://www.youtube.com/watch?v=VF1JES8Sv5U)**

Nvidia is synonymous with the AI boom. Global demand for its chips has made it the world's most valuable company. Next year it ...

📺 The Economist

👁️ 254K • 👍 1K • 💬 263 • ⏱️ 7:19 • 1d ago

---

**[AI data center backlash in the US | DW News](https://www.youtube.com/watch?v=Edron7EKhxA)**

Across America, the AI boom is bringing massive data centers - and growing resistance from the people who have to live next ...

📺 DW News

👁️ 5K • 👍 544 • 💬 60 • ⏱️ 2:06 • 4h ago

---

**[How to Build a FULL App with AI Under $100 (From Scratch)](https://www.youtube.com/watch?v=bqZ2eT8Kqig)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 14K • 💬 15 • ⏱️ 21:39 • 1d ago

---

**[Trump&#39;s Latest AI Slop Nightmare Just Hit The Internet](https://www.youtube.com/watch?v=PgsvPjon0cw)**

Really American Host Steve Harness Breaks Down The latest batch of anti-Trump AI Slop memes going viral on the internet.

📺 Really American

👁️ 513K • 👍 25K • 💬 963 • ⏱️ 12:34 • 1d ago

---

**[When A.I. Becomes an Enemy - Connor Leahy](https://www.youtube.com/watch?v=wzgkc6Iegx8)**

Soft White Underbelly interview and portrait of Connor Leahy, an A.I. researcher who warns about the threat of human extinction ...

📺 Soft White Underbelly

👁️ 278K • 👍 5K • 💬 2K • ⏱️ 1:04:07 • 1d ago

---

**[AI is older than you think #turing #turingtest #ai #artificialintelligence #documentary](https://www.youtube.com/watch?v=-oLgV1bIy6c)**

AI is in the news a lot now, but it's been making waves in science for decades.

📺 NOVA PBS Official

👁️ 481 • 👍 58 • 💬 5 • ⏱️ 1:18 • 55m ago

---

**[I Turned GPT-6 Astra Into the Ultimate AI Second Brain](https://www.youtube.com/watch?v=yysILVsfLFM)**

My playbook for growing a $1M AI agency: https://app.aiautomationsociety.ai/opaa-ads-optin My FREE resources: ...

📺 Nate Herk | AI Automation

👁️ 116K • 👍 2K • 💬 150 • ⏱️ 19:49 • 1d ago

---

**[This Lazy AI Side Hustle Makes $11,267/Month (LIVE BREAKDOWN)](https://www.youtube.com/watch?v=NE-62S4OYCg)**

Join Monetise and let my AI system build you a profitable side hustle: https://link.consulting.com/shs-ep2-yt Message my team ...

📺 Iman Gadzhi

👁️ 1.4M • 👍 42K • 💬 256 • ⏱️ 1:29:33 • 22h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 10,661 • ❤️ 833 • 5d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 6,712,160 • ❤️ 14,373 • 25d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 479,597 • ❤️ 645 • 6d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 2,879 • ❤️ 612 • 10h ago

---

**[timesfm-3.0-pytorch](https://huggingface.co/google/timesfm-3.0-pytorch)**

*Google*

TimesFM 3.0 is a PyTorch-based foundation model from Google Research for time-series forecasting, utilizing a Stacked Mixing Transformer architecture with Variate Attention and CPM Iterative RevIN. It excels at predicting future trends across diverse datasets, including web traffic, search queries, and synthetic data, with a context patch length of 32 and forecast horizon of 64.

`time-series-forecasting` `330.7M`

⬇️ 444,052 • ❤️ 625 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,644,796 • ❤️ 3,164 • 7d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

A highly optimized, uncensored Qwen3.8-27B fine-tune excelling in reasoning and creative writing, achieving state-of-the-art benchmarks with significantly reduced thinking tokens for faster inference. It supports image-text-to-text tasks and is ideal for coding, story generation, and roleplaying.

`image-text-to-text` `26.9B`

⬇️ 348,753 • ❤️ 343 • 17h ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 10,675,683 • ❤️ 3,690 • 19d ago

---

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 503,263 • ❤️ 5,002 • 12d ago

---

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 313,547 • ❤️ 817 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 17 • 💬 2 • ⭐ 2,171 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 128 • 💬 6 • ⭐ 103,386 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 31,950 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 778 • 💬 6 • ⭐ 11,253 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 107 • 💬 2 • ⭐ 12,143 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 86,805 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[BAT: Behavior-Aware Human-Like Trajectory Prediction for Autonomous
  Driving](https://huggingface.co/papers/2312.06371)**

*Haicheng Liao, Zhenning Li, Huanming Shen et al. (8 authors)*

A behavior-aware model predicts vehicle trajectories using insights from traffic psychology and human behavior, outperforming state-of-the-art benchmarks with reduced data.

▲ 0 • 💬 0 • ⭐ 851 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2312.06371) • [💻 code](https://github.com/petrichor625/batraj-behavior-aware-model)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 206 • 💬 3 • ⭐ 2,250 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 51 • 💬 2 • ⭐ 20,267 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 31,087 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 21.4k • 🔱 2.5k • 5h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.5k • 🔱 548 • 39m ago

---

**[Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills)**

🚀面向求职与开发场景的实用 AI Skills 集合，支持简历优化、岗位投递、面试准备与开发提效。

`HTML`

⭐ 4.1k • 🔱 246 • 9h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.9k • 🔱 440 • 11d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.5k • 🔱 447 • 3h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.5k • 🔱 152 • 12h ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 2.2k • 🔱 149 • 7d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports

`TypeScript`

⭐ 2.1k • 🔱 65 • 6h ago

---

**[diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness)**

AI harness reference implementation for on-demand delivery workflows

`Java`

⭐ 2.0k • 🔱 62 • 5d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 1.9k • 🔱 194 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
