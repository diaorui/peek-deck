---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-08T11:35:48.294383+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 08, 2026 at 11:35 UTC  
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

**[Can current LLM architecture actually get us to AGI?](https://www.reddit.com/r/artificial/comments/1wa8rjv/can_current_llm_architecture_actually_get_us_to/)**

I'm a software engineer, not a scientist and I love it. I enjoy solving hard, distributed applied problems at scale. It's what gets me out of bed in the morning, ready go keep learning even after over twenty years of doing this professionally. However, I also love to understand how things work. What makes them tick. How I can bend them to do my bidding, even if that's not what they were originally intended to do. Some may call this a hacker's mindset. Over the last couple of years, this has also applied to the nature of LLMs and where they are heading. Recently, I started peeling back the layers of the LLM black box. Instead of the academic path, I took that of the applied practitioner: Get a solid handle on how to use the thing and then take the knowledge learned from using it and enhance it by digging into how that black box actually works. Something of late has stumped me and I'm looking for those smarter than I to help me understand something: If the definition (as much as one can nail one down) of AGI is something akin to "a hypothetical type of computer software or machine intelligence that can match or surpass human cognitive abilities across any intellectual task", how an it possibly achieve that with current LLM architecture? At its core and at a /very/ high level, it predicts a probability distribution over the next token, conditioned on the tokens that came before it. Autoregressive decoding doesn't give a model an independent mechanism to know when it's wrong and deliberation steps don't fundamentally change that. Harnesses and the "intelligence" or "agentic reasoning" built into them to provide extra context, external feedback and loops work remarkably well in terms of providing what /seems/ to be intelligence, but at its core, it's "just" layers of probabilistic systems providing a magical output. The model itself isn't learning anything new. Ordinary inference doesn't update the model's weights from experience. Autoregressive generation itself doesn't backtrack and revise previously generated tokens. The primitive the model provides is generation, not an explicit reasoning mechanism. A human can have a thought, backtrack and make changes until it comes to the conclusion it wants. All on their own. The current state of LLMs is effectively like having a configurable number of people playing near-lossless telephone, each modifying or enriching the message before passing it along, except every person in the room is a clone (or maybe near clone if you're iterating with different models). Are the AGI claims with the existing architecture legitimately smoke and mirrors, or is there more to this equation that I can't see from my applied engineering standpoint?

11h ago

---

**[Crazy times](https://www.reddit.com/r/artificial/comments/1w9vaet/crazy_times/)**

20h ago

---

**[Have software jobs shown us what most jobs will probably be like?](https://www.reddit.com/r/artificial/comments/1wah05m/have_software_jobs_shown_us_what_most_jobs_will/)**

It's not surprising that software development is one of the first jobs that AI has really transformed. It's text-based, economically valuable, and generally of interest to the kinds of people inventing and training the AI. There's also a large amount of training examples available online. The job in most cases is now: You are a manager of robots who do things that used to be your job. You're responsible for what they produce and so the skill and art is in guiding and reviewing their work. It seems likely that one by one most jobs will turn into the above description, over the next year or three. Of course the domain will vary, so your knowledge and expertise used for instructing and verifying what the robots do will be what matters. This means there will still be a big difference between the jobs of e.g. an architect, surgeon, or builder. Probably the same basic kinds of robots in most cases, but requiring very different kinds of oversight. If that's the case then everyone needs to learn the job of robot management, well and quickly. I don't know how we do that, but I think that's what we need to accomplish as a society.

4h ago

---

**[I took a ride in the hype train at first, but no, not AGI](https://www.reddit.com/r/artificial/comments/1w9or91/i_took_a_ride_in_the_hype_train_at_first_but_no/)**

Spent the $200 within 8 hours on Astra. At first I was blown away, but checked things more thoroughly the next day, and a lot of the stuff it build wasn’t working. Actually 3 of the 4 things I asked Astra to do didn’t work. Quite disappointed. The demos focus mostly on 3D, Blender and games, but for coding and agentic use it was not an improvement at all for me. Maybe I could have prompted better, but when it spends 2+ hours on each task, you can’t really iterate and steer it. But still I feel like this is something AGI should have handled? Now I’m back to my usual setup with KIMI K.3 and DeepSeek flash trough standardcompute. Also keeping my max plan at both OpenAI and Claude, but $400+/month is starting to hurt. What are your thoughts? Closing in on AGI or was this all a part of a coordinated marketing stunt?

1d ago

---

**[AI Burnout Hits the People Charged With Defending Hospitals and Banks From Hackers](https://www.reddit.com/r/artificial/comments/1wagjuv/ai_burnout_hits_the_people_charged_with_defending/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-08-31/ai-driven-hacking-boom-fuels-cybersecurity-burnout-at-hospitals-and-banks?srnd=phx-businessweek) • 5h ago

---

**[Introducing AstraBlender! Real Blender that ChatGPT can use from a simple prompt sent from your phone on the ChatGPT website ;)](https://www.reddit.com/r/artificial/comments/1waj2rg/introducing_astrablender_real_blender_that/)**

Simply prompt ChatGPT work (or any other agent with a cloud browser, like Grok Bot) to go to the website and use blender. From your fucking phone! No nice computer required. No terminal codex. No blender install. None of that is required! Just prompt ChatGPT from your phone! Browser blender already exists, but it requires webgpu, which agent cloud computers don’t have. Blender via MCP also already exists. This though, where you can simply prompt ChatGPT from your phone to use blender, does not already exist to my knowledge or astra’s knowledge. How this works: I have blender and astrablender installed on an OCI cloud computer. It is streaming a browser desktop of that OCI cloud computer using selkies/linux server. The agent accesses the render website with the browser desktop from its cloud computer and operates it from there (you can prompt it to use blender from your phone!) This means I am paying real money to keep this running. It is free to use, but I have limited compute. As a result, only one person can be using this at a time. First come, first serve. If I reach my compute budget, I have to take it down until I can afford more. I am losing money on this free service. Please consider leaving an optional tip on the website if you find this useful. I will use the tips to buy more compute, hopefully enough so that everyone can use it at the same time. ALTERNATIVELY: This is open source. https://github.com/dakotalock/astrablender If I run out of compute or you just want your own, you may make your own. Here is what you need to do: Set up an OCI computer (they do have a free tier) Have your agent install blender and astrablender from the repo on that cloud computer. Set up a render website if you want a frontend for it. That’s it! Free for everyone! All I ask is that you leave a star on the GitHub repo if you use my work. Please enjoy agent blender access from your cell phones!

2h ago

---

**[Musk Loses Bid To Block MN Law Against AI Child Porn](https://www.reddit.com/r/artificial/comments/1w953sx/musk_loses_bid_to_block_mn_law_against_ai_child/)**

Politico reports: A federal judge Friday refused to block a Minnesota law prohibiting the creation of sexually explicit deepfake images that’s being challenged by Elon Musk’s artificial intelligence company, SpaceXAI. U.S. District Judge Donovan Frank said the company, formerly known as xAI, waited too long in making its last-minute request to temporarily block the law …

🔗 [Joe.My.God.](https://www.joemygod.com/2026/09/musk-loses-bid-to-block-mn-law-against-ai-child-porn/?__cf_chl_tk=8ecS8MZsG5kLxKOM9bn_OhtsSwkCeqv0nsm2KhSmayw-1788721611-1.0.1.1-qjvzErCp_nbPvJvAiboEjrydGx2Tw9tgtvvhETjw5T4) • 1d ago

---

**[Which AI is the best for helping me study?](https://www.reddit.com/r/artificial/comments/1wal3wc/which_ai_is_the_best_for_helping_me_study/)**

Now, I know this may seem like a dumb question. ''Why would I want AI to help my studies?'' I failed at the first university entrance exams I took. And now, I will study for a year again and try to enter a university. And when I study, I obviously cant solve every question correctly. And whenever I look at the video solutions of those questions, it doesnt help me at all mostly. Sometimes the teachers skip the important details to finish that video as quickly as possible, sometimes their mics barely work or they are too loud, sometimes they dont even bother to explain at all. So, I started using AI for it last year. I tried both GPT and Gemini so far and I concluded that Gemini just solved it better. It is my personal opinion, I might be wrong too, I dont know. And so, I got the paid subscribtion for it. But those prices are expensive in my country. And I can really use only one AI. And now that everyone is saying Gemini is just getting worse, Im worried. I would appreciate any advices or opinions.

39m ago

---

**[Three hikers got rescued off a mountain this week after following Gemini's advice. The same week OpenAI launched what it's calling the AGI era. I keep thinking about both together.](https://www.reddit.com/r/artificial/comments/1wa5i9p/three_hikers_got_rescued_off_a_mountain_this_week/)**

The hikers story happened September 1st. Three guys from Roseville used Gemini to plan a Mount Shasta summit. The AI told them to bring far less food and water than they needed. They summited at 7pm, four hours after the recommended turnaround time, descended in the dark, one of them hurt his knee, and they spent the night stranded in a canyon until rangers found them the next morning. Google says they can't replicate the bad answers Gemini gave. Maybe the prompts were vague. Maybe the AI was overconfident. Doesn't really matter which. What matters is that three people trusted a model's output as expert advice in a context where being wrong had serious consequences. Two days later OpenAI launched GPT-6 Astra. 99.9% on ARC-AGI-3, 97.6% on FrontierMath Tier 4, 100% on ExploitBench. OpenAI is calling this the start of the AGI era. Independent benchmarks from Artificial Analysis are more cautious and show Anthropic's Fable 5.1 still ahead on the broader intelligence index. But here's what I can't stop thinking about. The hikers story and the capability story are not separate things. Every time a model gets more capable, more people trust it in higher stakes situations. That gap between what the model can do and what the person using it understands about its limits doesn't close automatically when capability improves. If anything it gets harder to manage because the outputs get more convincing. I work with organizations on AI adoption and the single most common thing I see is not people being too skeptical of AI. It's people not knowing when to stop trusting it. What's your take? Does more capability make the trust calibration problem better or worse?

13h ago

---

**[Why aren't ARM chips more prevalent?](https://www.reddit.com/r/artificial/comments/1wahe3m/why_arent_arm_chips_more_prevalent/)**

So, I've had this question floating around in my head for a while. Given the high amount of power that generative AI uses, why aren't we using ARM based chips for data centers? They consume far less energy than x86 based chips and the technology has improved exponetially in the past ~6yrs. If it's because of hardwar constraints, what exactly would need to change for ARM chips to be considered a viable chip architecture for this purpose?

4h ago

---

---

## Google News: "ai"

**[French A.I. Start-Up Mistral Raises $3.5 Billion as Part of Strategy Shift](https://www.nytimes.com/2026/09/08/business/mistral-ai-fund-raising.html)**

The New York Times • 2h ago

---

**[Making sovereign, open-weight AI the technology frontier](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/)**

Mistral today announced that it has raised €3 billion in a Series D funding round at a post-money valuation of more than €21 billion.

mistral.ai • 6h ago

---

**[Mistral AI raises €3 billion in Samsung-led Series D round](https://qz.com/mistral-ai-samsung-series-d-funding-valuation-090826)**

The French AI startup's post-money valuation now exceeds €21 billion, up from €11.7 billion a year ago

qz.com • 16m ago

---

**[Early Data Indicates an A.I.-Generated Drug Could Slow Aging](https://www.nytimes.com/2026/09/07/science/ai-generated-drug-longevity.html)**

The New York Times • 1d ago

---

**[An Alien Mind](https://openai.com/index/an-alien-mind/)**

Jakub Pachocki reflects on increasingly capable AI and the challenge of keeping it aligned. He calls for stronger safeguards and international coordination.

OpenAI • 1d ago

---

**[The body image battle is real in 2026, but the bodies may not be](https://www.axios.com/2026/09/08/ai-fitness-influencers-body-ideals)**

Axios • 12m ago

---

**[The Prodigy Problem](https://www.theatlantic.com/ideas/2026/09/aschenbrenner-ai-future/688493/)**

Leopold Aschenbrenner claimed to know the future of AI. His investors lost billions.

The Atlantic • 35m ago

---

**[China’s AI Computing Boom Is Moving Far Beyond Its Biggest Cities](https://www.bloomberg.com/news/newsletters/2026-09-08/china-s-ai-computing-boom-is-moving-far-beyond-its-biggest-cities)**

Bloomberg.com • 31m ago

---

**[Trump says he's made 'Hundreds of Billions of Dollars on Stocks' for the U.S., in stream of AI posts](https://www.cnbc.com/2026/09/07/trump-truth-social-ai-images-posting-spree.html)**

U.S. President Donald Trump posted a stream of AI-generated images and a series of sweeping and unverified claims on Truth Social on Sunday

CNBC • 1d ago

---

**[AI will cure cancer in our lifetime, claims boss of UK chip giant](https://www.bbc.com/news/articles/c0m39g7xzevo)**

The head of chip designer Arm says modelling how a DNA marker is impacted by cancer cannot be done now, but computers are "going to solve it".

BBC • 2h ago

---

---

## HackerNews: "ai"

**[How I feel about AI](https://news.ycombinator.com/item?id=49587128)**

It's complicated

⬆️ 162 • 💬 258 • 1d ago • [beza1e1.tuxen.de](https://beza1e1.tuxen.de/ai_feelings.html)

---

**[AI, Tools and Transformation](https://news.ycombinator.com/item?id=49582656)**

It’s very tempting to imagine that AI turns everyone into a tool-builder - now everyone can just ask the model to make the software they need, and apps as we know them are dead.  I think that misunderstands how most people think and where software actually comes from, and more importantly, it isn’t

⬆️ 156 • 💬 76 • 2d ago • [Benedict Evans](https://www.ben-evans.com/benedictevans/2026/9/3/ai-tools-and-transformation)

---

**[AI models ran real businesses: They sent $12,431 in fake invoices, lost $3,200](https://news.ycombinator.com/item?id=49601338)**

$12,431 in fake invoices, 2,797 spam emails, $0 revenue.

⬆️ 100 • 💬 117 • 17h ago • [Bottleneck Labs](https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses)

---

**[I refused to train the AI that could replace me](https://news.ycombinator.com/item?id=49593959)**

⬆️ 95 • 💬 113 • 1d ago • [restofworld.org](https://restofworld.org/2026/ai-training-jobs-expert-replacement/)

---

**[Initial effects of AI technology on employment look positive](https://news.ycombinator.com/item?id=49596610)**

⬆️ 88 • 💬 132 • 1d ago • [economist.com](https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here)

---

**[Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs](https://news.ycombinator.com/item?id=49594008)**

The Universal Cross-Model Episodic Memory Standard. Local-first, project-scoped SQLite memory engine for Google Antigravity, Claude Code, Cursor, and Windsurf. Zero cloud lock-in. - timgordontg/engrim

⬆️ 88 • 💬 51 • 1d ago • [GitHub](https://github.com/timgordontg/engrim)

---

**[OKF Agent Memory – Git-native persistent memory for AI coding agents](https://news.ycombinator.com/item?id=49581240)**

Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with ...

⬆️ 79 • 💬 32 • 2d ago • [GitHub](https://github.com/okf-memory/okf-agent-memory)

---

**[AI Cold Showers](https://news.ycombinator.com/item?id=49601810)**

A short list of articles that temper my enthusiasm around AI, and drawing a
few lines in the sand along the way.

⬆️ 75 • 💬 12 • 16h ago • [allan.reyes.sh](https://allan.reyes.sh/posts/ai-cold-showers/)

---

**[America's two largest school districts impose AI moratoriums](https://news.ycombinator.com/item?id=49580980)**

The New York City Department of Education and the Los Angeles Unified School District announced new policies this week, reports Chris Mills Rodrigo.

⬆️ 61 • 💬 74 • 2d ago • [Tech Policy Press](https://www.techpolicy.press/americas-two-largest-school-districts-impose-ai-moratoriums/)

---

**[Arm Mali G2-Ultra NX GPU: desktop-class mobile gameplay with AI-native graphics](https://news.ycombinator.com/item?id=49605511)**

Arm Mali G2-Ultra NX brings AI-native graphics and neural acceleration to desktop-class mobile gaming.

⬆️ 48 • 💬 35 • 7h ago • [Arm Newsroom](https://newsroom.arm.com/blog/arm-mali-g2-ultra-nx-ai-native-mobile-graphics)

---

---

## YouTube Videos: "ai"

**[OpenAI Reveals ALIEN MIND - The Biggest AI Warning Yet](https://www.youtube.com/watch?v=M2aB-2XQ9UU)**

OpenAI's chief scientist just issued one of its strongest AI warnings yet. He says today's systems are becoming alien minds we do ...

📺 AI Revolution

👁️ 56K • 👍 889 • 💬 125 • ⏱️ 15:24 • 11h ago

---

**[The Great AI Die-Off Has Started](https://www.youtube.com/watch?v=aunUOIrbIeM)**

Get the #1 AI wearable: https://www.fieldy.ai/julia* FREE GUIDE: The Content Creator's AI Blueprint* ...

📺 Julia McCoy

👁️ 77K • 👍 2K • 💬 146 • ⏱️ 8:23 • 2d ago

---

**[Trump&#39;s Latest AI Slop Nightmare Just Hit The Internet](https://www.youtube.com/watch?v=PgsvPjon0cw)**

Really American Host Steve Harness Breaks Down The latest batch of anti-Trump AI Slop memes going viral on the internet.

📺 Really American

👁️ 462K • 👍 24K • 💬 897 • ⏱️ 12:34 • 1d ago

---

**[This Lazy AI Side Hustle Makes $11,267/Month (LIVE BREAKDOWN)](https://www.youtube.com/watch?v=NE-62S4OYCg)**

Join Monetise and let my AI system build you a profitable side hustle: https://link.consulting.com/shs-ep2-yt Message my team ...

📺 Iman Gadzhi

👁️ 1.4M • 👍 41K • 💬 606 • ⏱️ 1:29:33 • 14h ago

---

**[98% of Investors Miss The REAL AI Winners (My Full Map)](https://www.youtube.com/watch?v=csv55UtVMZM)**

Stop asking and start building with Emergent: https://app.emergent.sh/?utm_shift=redirect&via=tickersymbolyou Full prompt for my ...

📺 Ticker Symbol: YOU

👁️ 172K • 👍 5K • 💬 428 • ⏱️ 23:02 • 2d ago

---

**[The Cheapest 32GB Nvidia GPU You Can Buy for Local AI (Tesla V100)](https://www.youtube.com/watch?v=3P6m_QBIgAo)**

Buy one on Amazon: https://lon.tv/291nh - also find the aaostar dock here: https://amzn.to/3TcsM5b (compensated affiliate links).

📺 Lon.TV

👁️ 66K • 👍 1K • 💬 116 • ⏱️ 15:09 • 1d ago

---

**[Grok AI Finally Reveals Who Really Built the Pyramid — With Undeniable Proof](https://www.youtube.com/watch?v=0hr_ahlScik)**

Grok AI Finally Reveals Who Built The Pyramids — And The Evidence Is Unbelievable What if the story we've all been taught ...

📺 Ambrose Discovery

👁️ 147K • 👍 786 • 💬 60 • ⏱️ 26:20 • 19h ago

---

**[I Made AI Cheats Fight My AI Anti-Cheat](https://www.youtube.com/watch?v=Gr8iNYu3eF0)**

BUSINESS EMAIL ▻ KingHaiX7@yandex.ru TWITCH ▻https://www.twitch.tv/haixxd KICK ▻ https://kick.com/kinghaix 2ND ...

📺 HaiX

👁️ 146K • 👍 3K • 💬 285 • ⏱️ 29:30 • 21h ago

---

**[Haters will say this is fake AI medicine…](https://www.youtube.com/watch?v=BmgAD0axzsU)**

Haters will say this is fake AI medicine…

📺 Nick Freitas

👁️ 191K • 👍 17K • 💬 592 • ⏱️ 0:40 • 1d ago

---

**[Linus Torvalds Beat An AI](https://www.youtube.com/watch?v=tuPs2f0llOo)**

📺 Zack Shutt

👁️ 807K • 👍 48K • 💬 975 • ⏱️ 1:12 • 22h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 10,661 • ❤️ 797 • 5d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 6,712,160 • ❤️ 14,323 • 24d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 479,597 • ❤️ 605 • 6d ago

---

**[timesfm-3.0-pytorch](https://huggingface.co/google/timesfm-3.0-pytorch)**

*Google*

TimesFM 3.0 is a PyTorch-based foundation model from Google Research for time-series forecasting, utilizing a Stacked Mixing Transformer architecture with Variate Attention and CPM Iterative RevIN. It excels at predicting future trends across diverse datasets, including web traffic, search queries, and synthetic data, with a context patch length of 32 and forecast horizon of 64.

`time-series-forecasting` `330.7M`

⬇️ 444,052 • ❤️ 605 • 5d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 2,879 • ❤️ 534 • 2h ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,644,796 • ❤️ 3,119 • 7d ago

---

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 503,263 • ❤️ 4,992 • 12d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

A highly optimized, uncensored Qwen3.8-27B fine-tune excelling in reasoning and creative writing, achieving state-of-the-art benchmarks with significantly reduced thinking tokens for faster inference. It supports image-text-to-text tasks and is ideal for coding, story generation, and roleplaying.

`image-text-to-text` `26.9B`

⬇️ 348,753 • ❤️ 323 • 9h ago

---

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 313,547 • ❤️ 808 • 7d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 10,675,683 • ❤️ 3,665 • 18d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 16 • 💬 2 • ⭐ 2,171 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 778 • 💬 6 • ⭐ 11,251 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 31,859 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 107 • 💬 2 • ⭐ 12,074 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 86,805 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 128 • 💬 6 • ⭐ 102,992 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 206 • 💬 3 • ⭐ 2,202 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[BAT: Behavior-Aware Human-Like Trajectory Prediction for Autonomous
  Driving](https://huggingface.co/papers/2312.06371)**

*Haicheng Liao, Zhenning Li, Huanming Shen et al. (8 authors)*

A behavior-aware model predicts vehicle trajectories using insights from traffic psychology and human behavior, outperforming state-of-the-art benchmarks with reduced data.

▲ 0 • 💬 0 • ⭐ 647 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2312.06371) • [💻 code](https://github.com/petrichor625/batraj-behavior-aware-model)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 50 • 💬 2 • ⭐ 20,182 • 15d ago

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

⭐ 21.3k • 🔱 2.5k • 15h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.5k • 🔱 549 • 21h ago

---

**[Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills)**

🚀面向求职与开发场景的实用 AI Skills 集合，支持简历优化、岗位投递、面试准备与开发提效。

`HTML`

⭐ 4.0k • 🔱 243 • 1h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.9k • 🔱 440 • 11d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.5k • 🔱 445 • 1h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.4k • 🔱 151 • 4h ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 2.2k • 🔱 145 • 7d ago

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

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
