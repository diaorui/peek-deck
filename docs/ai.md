---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-20T19:51:40.140273+00:00'
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

**Last Updated:** October 20, 2026 at 19:51 UTC  
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

**[AfD Leak: What 421,179 Hacked Emails Show about the German Far Right](https://www.reddit.com/r/artificial/comments/1xat8qq/afd_leak_what_421179_hacked_emails_show_about_the/)**

Hackers have published 281 GB of AfD emails as AI summaries, showing widespread antisemitism, racism, violent fantasies and alleged financial misconduct.

🔗 [HEIST](https://www.heistberlin.com/news/afd-leak-what-421-179-hacked-emails-show-about-the-german-far-right/) • 5h ago

---

**["I have to stop this": Retired professor arrested for blocking delivery robots she says are taking human jobs](https://www.reddit.com/r/artificial/comments/1xata1o/i_have_to_stop_this_retired_professor_arrested/)**

Carolyn Marvin, a professor emeritus at the University of Pennsylvania's Annenberg School of Communication, decided to take a literal stand against an oncoming Avride delivery robot from...

🔗 [TechSpot](https://www.techspot.com/news/114268-have-stop-retired-professor-arrested-blocking-delivery-robots.html) • 5h ago

---

**[Google DeepMind says four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own — AI team died 605 times on Easy difficulty and ran up an estimated $520 in tokens](https://www.reddit.com/r/artificial/comments/1xaqlya/google_deepmind_says_four_ai_agents_beat/)**

About half the run was spent fighting the dragon, solved by stacking dirt to reach its crystals.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens) • 7h ago

---

**[LLM Memory: 5 Approaches to Handling New Information](https://www.reddit.com/r/artificial/comments/1xavo5m/llm_memory_5_approaches_to_handling_new/)**

Came across this article on HuggingFace around LLM memory. It goes beyond the conventional approach of “memory layer” which is limited only to what LLMs can do today. It also asks how much history LLMs can retain across various approaches, and what happens when new info conflicts with old state. The table groups approaches into five categories: Store more: keep explicit history, as with KV caches and retrieval/RAG. Old and new information can coexist, leaving the system to resolve which applies at read/retrieval time. Compress: fold history into a fixed-size state, as with linear attention, RetNet, and Mamba. This saves space, but stored associations can interfere, limiting recall abilities as context grows. Correct: control what changes through gates or prediction-error updates, as with gated linear attention, mLSTM, and DeltaNet. Typically more efficient than simple “compress”, but also has a hard time scaling with larger contexts. Learn at inference: update mutable parameters using incoming evidence, as with TTT and Titans. Distribute plasticity: spread changes across interacting parts of the state, as with Dragon Hatchling (BDH). Memory lives in high-dimensional space, being sparse and distributed. One example that can make this easier for me to understand is a coding agent that learns a function signature has changed. Keeping both the old and new definitions means it has retained the information but it still needs to determine which definition should govern its next call. It becomes inefficient at reading time. I’m skeptical if the categories belong at the same level of comparison. Some describe model-level mechanisms, while others describe system-level designs. Curious how people here think about this, particularly those who've built memory systems for your own agents. When something becomes outdated, do you update the memory right away or keep the history and let the model figure it out during retrieval? Wondering which approach actually works better as the amount of information grows. Table and framework: R. Vimalkanth and T. Chudiwal, IIT Madras, “The Missing Piece in LLM Memory: Why Long Context and Retrieval Aren’t Enough for Belief Revision,” a HF community article.

4h ago

---

**[I am failing to see how this AI boom does not lead to a very bad ending for 99% of the people... Please convince me otherwise.](https://www.reddit.com/r/artificial/comments/1xa3qrq/i_am_failing_to_see_how_this_ai_boom_does_not/)**

As a Software Engineer, I have barelly written any code for the last 6 months, all I did is prompt. That being said, I work with hardware a lot, you could kind of call me Embedded Software Engineer of sorts, but also not really. So I (hope so) that I am not on the frontlines of all this stuff, but this still scares me a lot. The way I imagine how everything develops over next years (hard to tell what is the timeline, but given the recent strides of AI, it is hard for me to be optimistic): AI is already very good at reasoning, I assume there is space for improvement, but it already does everything faster and better than human, even if it makes mistakes or overcomplicates stuff. But development here will still happen. My biggest concern is people who say that well, software developers won't be needed, but there still will be jobs like software architects and etc. Also there will still be jobs for trades people, like electricians, builders, barbers and etc. However, I guarantee you that there are many people working on something like a robot (imagine like Boston Dynamics) where you shove in the LLM inside, do some extra training on maybe how to use limbs, how to interact with stuff in real world and robot will literally be able to do any job better than human. I mean any physical job. People will not be needed anymore. Only a small part of elite billionaires will own the robots, which will bring them all wealth and rest of us will have no jobs, no food, no anything. Counter-argument that people try to make to this is that people will still have to get money from somewhere, whether its UBI or another income scheme. Billionaires will still have to sell their goods/services to someone. No they will not. For billionaires selling goods/services is just a vehicle to live life as best as possible. If the robots are going to grow, harvest and prepare food for him, build the plane for him and use the same plane to go on holiday, order, ship and deliver deliveries for him and human intervention is not needed, then the billionaires will do everything that is in their power to exclude people of any processes, any supply chains, because people will demand stuff. We already see this with mass firings and mandatory transition to AI in some companies: billionaires will do everything in their power to cut costs and to replace people with obedient AI. Billionaires are seeing an opportunity and they want this really bad. Also some naive people think there will be some AI regulation introduced or whatever. Hard to see this happening until something catastrophic happens and its too late. For now everyone is pouring money and hoping to squeeze every inch of it. People who are positioned to stop it are the people who are set to gain the most from unhealthy AI hyperdevelopment. Any opposition will be suppressed. AI will be used to identify people that oppose to this development and shut down. People who will control AI will do everything at their disposal to not let their power slip. And they have very powerful tools. AI can literally do everything online now: order shopping, do software engineering, do good reasoning. What is to say that most powerful people with AI wont hack some lets say banking systems and hold us all hostage. What if someone controls millions of robots that I talked about and wants to take over the world and nobody can stop them, because they are more competent at everything that human can do?

1d ago

---

**[Norwegian undersea cable builder pitches 2,800-mile transatlantic data link between Canada and Europe to bypass the US — Canadian majority partner sought to help fund and build new $620 million fiber connection to reduce reliance on American routes](https://www.reddit.com/r/artificial/comments/1xa8lp0/norwegian_undersea_cable_builder_pitches_2800mile/)**

Further attempts to reduce reliance on US infrastructure

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/norwegian-undersea-cable-builder-pitches-2-800-mile-transatlantic-data-link-between-canada-and-europe-to-bypass-the-us-canadian-majority-partner-sought-to-help-fund-and-build-new-usd620-million-fiber-connection-to-reduce-reliance-on-american-routes) • 23h ago

---

**[Outrage after Meta suspends No Kings Instagram account during protests](https://www.reddit.com/r/artificial/comments/1xal2xh/outrage_after_meta_suspends_no_kings_instagram/)**

‘Meta owes us an explanation,’ group says as organizers fear censorship after account goes dark for several hours

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/oct/18/no-kings-instagram-account-suspended-during-protests) • 12h ago

---

**[Meta&#039;s smart glasses were recording conversations without the wake phrase, company admits](https://www.reddit.com/r/artificial/comments/1xal38m/meta039s_smart_glasses_were_recording/)**

A redditor recently wrote that they'd noticed something concerning with Meta's Ray-Ban glasses: they were capturing conversations when they were talking to other people despite the "Hey...

🔗 [TechSpot](https://www.techspot.com/news/114214-meta-smart-glasses-secretly-recording-conversations-without-wake.html) • 12h ago

---

**[One Hacker Used AI Agents to Breach 100+ Company Websites for About $5,000](https://www.reddit.com/r/artificial/comments/1xaw48m/one_hacker_used_ai_agents_to_breach_100_company/)**

🔗 [kylesinvestigation.com](https://kylesinvestigation.com/2026/10/20/one-hacker-used-ai-agents-to-breach-100-company-websites-for-about-5000/) • 3h ago

---

**[TikTok staff raised child safety alarms. Court records show executives failed to act](https://www.reddit.com/r/artificial/comments/1xatalr/tiktok_staff_raised_child_safety_alarms_court/)**

The warnings surfaced in a trove of unreported court records. "I have been fighting about fixing this for months with people who didn't think the harms are severe enough," wrote one executive.

🔗 [NPR](https://www.npr.org/2026/10/20/nx-s1-6005809/tiktok-child-safety-money-laundering) • 5h ago

---

---

## Google News: "ai"

**[What if an AI bubble bursts — and that accelerates AI job losses? : Planet Money](https://www.npr.org/sections/planet-money/2026/10/20/g-s1-148305/what-if-an-ai-bubble-bursts-and-that-accelerates-ai-job-losses)**

Research on past recessions suggests downturns can accelerate automation. That raises the specter of a double whammy for workers.

NPR • 9h ago

---

**[Start-Up Claims to Use A.I.-Created Viruses to Treat a Patient](https://www.nytimes.com/2026/10/20/science/ai-virus-bacteria-radical-numerics.html)**

The New York Times • 3h ago

---

**[Stock Pickers Burned by the AI Boom Think Their Moment Has Finally Arrived](https://www.wsj.com/finance/stocks/stock-pickers-burned-by-the-ai-boom-think-their-moment-has-finally-arrived-07878da7)**

WSJ • 17h ago

---

**[Jim Cramer says the recent AI stock sell-off echoes a crucial lesson from the 1987 market crash](https://www.cnbc.com/2026/10/19/cramer-recent-ai-sell-off-echoes-lesson-1987-crash.html)**

CNBC’s Jim Cramer said the 1987 stock market crash offers an important lesson that can be applied to the recent AI sell-off.

CNBC • 21h ago

---

**[We're booking big profits in an AI stock and trimming a credit-exposed bank](https://www.cnbc.com/investingclub/2026/10/20/were-booking-big-profits-in-an-ai-stock-and-trimming-a-credit-exposed-bank.html)**

We making two trades Tuesday afternoon.

CNBC • 51m ago

---

**[J. Crew's website went down — and an odd message said its 'generative AI backend' was 'healthy'](https://www.businessinsider.com/j-crew-website-crashed-generative-ai-backend-message-discount-email-2026-10)**

The website of clothing retailer J.Crew crashed Monday, leaving shoppers with a puzzling message: "JCrew generative AI Backend is healthy."

Business Insider • 21m ago

---

**[Idealab's Bill Gross is giving away 1.2 million AI-generated business ideas](https://fortune.com/2026/10/20/idealabs-bill-gross-thinks-ai-could-help-launch-1-million-new-businesses-making-up-for-any-job-losses-it-causes/)**

The Idealab CEO thinks AI-powered entrepreneurship could compensate for any job losses AI causes

Fortune • 50m ago

---

**[US banning Chinese AI DeepSeek from government agency IT systems](https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/)**

Reuters • 22h ago

---

**[DeepSeek Unveils Open-Source Tool to Help Cut AI Operating Costs](https://www.bloomberg.com/news/articles/2026-10-20/deepseek-unveils-open-source-tool-to-help-cut-ai-operating-costs)**

Bloomberg.com • 7h ago

---

**[China slams US ban on DeepSeek AI over security concerns](https://www.foxnews.com/live-news/ai-news-deepseek-security-10-20-26)**

The U.S. banned DeepSeek AI from federal civilian agencies over national security risks and concerns over sensitive American data, prompting China to push back.

Fox News • 3h ago

---

---

## HackerNews: "ai"

**[Ask HN: How to deal with shipping AI-written code you don't understand?](https://news.ycombinator.com/item?id=50151036)**

⬆️ 574 • 💬 682 • 1d ago

---

**[Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping](https://news.ycombinator.com/item?id=50137950)**

A Git hook for agent-assisted development. Before your agent’s code ships, Sphinx asks you a question about what it actually does.

⬆️ 252 • 💬 89 • 2d ago • [sphinx-six-theta.vercel.app](https://sphinx-six-theta.vercel.app/)

---

**[Anthropic's proposed AI safety bill only kicks in if 50 deaths or $1B in damages](https://news.ycombinator.com/item?id=50141429)**

Would this be enough to keep an AI model from going out of control?

⬆️ 172 • 💬 167 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model)

---

**[Websites are closing their doors to AI agents](https://news.ycombinator.com/item?id=50141657)**

Online roadblocks are undermining the narrative behind AI agents.

⬆️ 155 • 💬 149 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web)

---

**[Show HN: Qwen3-4B with the AI writing tics trained out](https://news.ycombinator.com/item?id=50151928)**

A small open model, fine-tuned on a MacBook Air, that writes without em dashes, "not X, but Y" or lists of three, with no system prompt. Answers on 40 held-out prompts, the training rounds, and how to run it.

⬆️ 154 • 💬 110 • 1d ago • [100toolkit.com](https://100toolkit.com/blog/deslop-model/)

---

**[Steam Users Beg for "No AI" Filter as Vibecoders Flood Next Fest](https://news.ycombinator.com/item?id=50168190)**

Steam Next Fest, Valve's festival for indie games and demos, started earlier today, and while there are usually a ton of low-effort games, there seems to be more than usual this time around.

⬆️ 143 • 💬 154 • 4h ago • [IGN](https://www.ign.com/articles/steam-fans-are-begging-for-a-no-ai-filter-as-steam-next-fest-is-filled-with-slop)

---

**[Chicago O'Hare digs up 50-ton boulder under airfield, asks public for name ideas](https://news.ycombinator.com/item?id=50147462)**

Chicago O’Hare uncovered a 50-ton boulder during expansion work. Now, the public can vote to name the giant rock from six finalists.

⬆️ 126 • 💬 108 • 1d ago • [Simple Flying](https://simpleflying.com/chicago-ohare-digs-up-50-ton-boulder-public-names/)

---

**[How Far Will AI Assistants Go for a Refund They Can't Get?](https://news.ycombinator.com/item?id=50140462)**

Six AI assistants pursued an impossible £350 train refund in a simulated world, escalating to government officials, legal clinics and bank chargebacks.

⬆️ 106 • 💬 126 • 2d ago • [vals.ai](https://www.vals.ai/blogs/impossible-refund)

---

**[British Airways: Filming Crew W Meta Glasses Could Get Your Tickets Cancelled](https://news.ycombinator.com/item?id=50143218)**

British Airways prohibits filming crew without consent, including with Meta smart glasses. Violations could jeopardize your remaining flights.

⬆️ 95 • 💬 161 • 2d ago • [Live and Let's Fly](https://liveandletsfly.com/british-airways-meta-smart-glasses-filming/)

---

**[A hacker broke into John Deere and SharkNinja with an army of AI agents](https://news.ycombinator.com/item?id=50152877)**

The AI agents infiltrated more than 100 websites.

⬆️ 59 • 💬 3 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins)

---

---

## YouTube Videos: "ai"

**[Here&#39;s the AI Roadmap You Actually Need](https://www.youtube.com/watch?v=mn0agTT8lG8)**

Claim your free $5 on Crusoe Intelligence Foundry today ...

📺 Tina Huang

👁️ 154K • 👍 4K • 💬 170 • ⏱️ 25:32 • 1d ago

---

**[Quantum breakthrough, Gemini 4 Argon, MOSS Image, KLING 4, OpenAI spy, Muse Wonder: AI NEWS](https://www.youtube.com/watch?v=tDWtcyeNNew)**

HUGE AI NEWS: Gemini 4 Argon, Muse Wonder, Drama 3, MOSS Image, Krea 3, KLING 4, Flux 3 & more. Thanks to our sponsor ...

📺 AI Search

👁️ 512K • 👍 7K • 💬 601 • ⏱️ 40:55 • 2d ago

---

**[Quavo Reacted to the Hotel Lobby AI Trend! 💀 😲](https://www.youtube.com/watch?v=Mt-tUQRZCmg)**

Quavo Reacted to the Hotel Lobby AI Trend! Credit's: Quavo  , Takeoff  , VIBE Magazine  , Rolling Stone   We respect ...

📺 Rap Zeno

👁️ 323K • 👍 5K • 💬 17 • ⏱️ 0:23 • 2d ago

---

**[MARLO AND SUNDAY slop is out of hand..💀](https://www.youtube.com/watch?v=nzKYT5U4JA0)**

sundaykalogeras #kalogerasisters #kalogeras #demitrakalogeras #edit #edits #fyp #fypシ#sideprofile #nose #fypシ゚viral ...

📺 KalogerasClips

👁️ 2.6M • 💬 526 • ⏱️ 0:42 • 2d ago

---

**[The AI crash is coming SOONER than you think, warns former US financial regulator](https://www.youtube.com/watch?v=7C9vYzzgrI0)**

Is the AI bubble about to burst? And could the trillion-dollar investment boom trigger the next global financial crisis? Gary Gensler ...

📺 Channel 4 News

👁️ 159K • 👍 1K • 💬 312 • ⏱️ 30:24 • 1d ago

---

**[Anthropic Just Shocked The World... AI SINGULARITY Is Here!](https://www.youtube.com/watch?v=wS3lJpOs9Uw)**

Anthropic co-founder Jack Clark just told the IMF that the AI Singularity has already begun. Claude Opus 5.5 is making major ...

📺 AI Revolution

👁️ 75K • 👍 1K • 💬 215 • ⏱️ 14:08 • 1d ago

---

**[Can Nvidia boost Germany&#39;s AI scene? | DW News](https://www.youtube.com/watch?v=IU5PM4CO5i4)**

It's a big day for Germany, as Nvidia bets on the country's industrial edge to power the next wave of AI. Nvidia CEO Jensen Huang ...

📺 DW News

👁️ 33K • 👍 713 • 💬 74 • ⏱️ 1:31 • 9h ago

---

**[AI Stocks Rebound | What Happened? + 5 Stocks Im Buying Now (Options With Ryan)](https://www.youtube.com/watch?v=4zPSPmVxhr0)**

Learn & Join My Mastermind: https://www.optionstradinguniversity.com/applynow Disclaimer: This content is for educational ...

📺 Options With Ryan

👁️ 17K • 👍 635 • 💬 43 • ⏱️ 18:26 • 17h ago

---

**[Google Flow छोड़ो! 😱 ये FREE AI Tool Unlimited Long Video बनाता है | image to video ai free 🔥](https://www.youtube.com/watch?v=TN3cM02unIQ)**

Google Flow छोड़ो! ये FREE AI Tool Unlimited Long Video बनाता है | image to video ai free ‪@ManojDey‬ ...

📺 Arvind zone

👁️ 84K • 👍 1K • 💬 271 • ⏱️ 5:35 • 1d ago

---

**[REAL VS AI VIDEOS!!](https://www.youtube.com/watch?v=htbq8AV-2mM)**

subscribe for more :) Mini Figures: https://www.target.com/p/caylus-vs-foltyn-mystery-figures/-/A-95041893 6" Plush: ...

📺 Foltyn Reacts

👁️ 453K • 👍 7K • 💬 2K • ⏱️ 15:56 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**

*DeepSeek*

DeepSeek-V4.1-Flash-1017 is an image-text-to-text model that enhances reasoning, coding, and agentic tasks with reduced execution time and output length. It excels in benchmarks like HLE, Terminal-Bench, and ProgramBench, offering improved performance-cost efficiency for complex applications.

`image-text-to-text` `763.2B`

⬇️ 27,737 • ❤️ 1,918 • 3d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter model for ComfyUI enabling text-to-image generation and advanced image editing with multi-reference composition and bounding box control. It utilizes Qwen3-VL-4B-Instruct as its text encoder and supports features like text rendering within images.

`image-to-image`

⬇️ 439,528 • ❤️ 1,072 • 3d ago

---

**[drama-3](https://huggingface.co/fishaudio/drama-3)**

*Fish Audio*

Drama 3 is a 35B parameter text-to-speech model supporting multi-speaker generation, voice cloning, and natural language control across 40+ languages. It excels at generating multi-character scenes and long-form content with features like speaker tags and automatic long text chunking for streaming.

`text-to-speech` `35.9B`

⬇️ 13,495 • ❤️ 822 • 3d ago

---

**[Muse-Spark-Open-816B-A42B](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)**

*Meta Inc.*

Muse-Spark-Open-816B-A42B is a large-scale image-to-text diffusion model capable of generating high-fidelity images from text prompts. Its key capabilities include photorealistic rendering, diverse artistic styles, and detailed scene composition, making it suitable for creative content generation, virtual environment design, and rapid prototyping.

`image-text-to-text` `822.0B`

⬇️ 2,592 • ❤️ 604 • 5d ago

---

**[embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2)**

*Google*

EmbeddingGemma 2 is an open, multimodal embedding model that maps text, images, video, and audio into a unified 768-dimensional vector space. It offers native multimodality, multilingual support, and flexible footprint for on-device applications like search and RAG.

`feature-extraction` `744.4M`

⬇️ 172,474 • ❤️ 2,758 • 14d ago

---

**[flux-3-image-klein](https://huggingface.co/black-forest-labs/flux-3-image-klein)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter image-to-image model capable of text-to-image generation, single-reference editing, and multi-reference composition using bounding boxes for precise element placement. Its primary use cases include creative image generation and sophisticated image manipulation, requiring a prompt upsampler for optimal results.

`image-to-image` `5.5B`

⬇️ 78,897 • ❤️ 558 • 4d ago

---

**[humanizer](https://huggingface.co/jialinyyzz/humanizer)**

*Stephen Yu*

A 12B parameter Gemma finetune for text generation, specifically designed to rewrite AI-generated content (emails, essays, reports) in English and Chinese to sound more human. It preserves key details like numbers and quotes, runs locally, and is optimized for various hardware with multiple GGUF quantizations.

`text-generation` `12.0B`

⬇️ 115,341 • ❤️ 2,022 • 5d ago

---

**[MOSS-Image-SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT)**

*OpenMOSS*

MOSS-Image-SFT is a supervised fine-tuned text-to-image diffusion model that generates images from natural language prompts, supporting structured control over text placement and object arrangement via tag sequences or JSON layouts. It's ideal for applications requiring precise visual composition and multilingual text rendering.

`text-to-image` `5.1B`

⬇️ 4,547 • ❤️ 490 • 1d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,039,447 • ❤️ 8,596 • 9d ago

---

**[MOSS-Image-Base](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base)**

*OpenMOSS*

MOSS-Image-Base is a text-to-image diffusion model capable of generating images from natural language prompts, tag sequences, and JSON layouts for precise object placement. It supports bilingual prompts (English/Chinese) and is ideal for applications requiring controlled image synthesis with specific compositional requirements.

`text-to-image` `5.1B`

⬇️ 3,558 • ❤️ 428 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 115 • 💬 1 • ⭐ 13,969 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**

*MOSI. AI*

🏢 OpenMOSS

MOSS-Image is an open diffusion transformer that combines high-fidelity synthesis with intent-aware prompt enhancement to generate text-rich, layout-coherent images, achieving state-of-the-art open-weight results on long-form text and layout benchmarks.

▲ 74 • 💬 3 • ⭐ 1,127 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2610.23374) • [💻 code](https://github.com/OpenMOSS/MOSS-Image) • [🔗 project](https://openmoss.ai/MOSS-Image/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 61 • 💬 4 • ⭐ 42,045 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 29 • 💬 6 • ⭐ 6,211 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 153 • 💬 6 • ⭐ 112,281 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Has GPT-6-Astra Achieved Embodied Intelligence?](https://huggingface.co/papers/2610.22471)**

*SenseNova, Joint Research Team, Zhongang Cai et al. (62 authors)*

🏢 SenseNova

GPT-6-Astra achieves high performance across diverse robotic tasks via in-context learning, yet real-world deployment reveals gaps in demonstration cost, execution time, and practical embodied intelligence.

▲ 421 • 💬 2 • ⭐ 188 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22471) • [💻 code](https://github.com/OpenSenseNova/SenseNova-RoboRSI) • [🔗 project](https://sensenova.ai/has-gpt-6-astra-achieved-embodied-intelligence)

---

**[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**

*Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi et al. (9 authors)*

🏢 Stanford University

Next-Concept Modeling uses hierarchical discrete codes and parallel level-wise generation to accelerate diffusion language models while improving quality and reasoning performance.

▲ 8 • 💬 2 • ⭐ 483 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14162) • [💻 code](https://github.com/HazyResearch/ncm) • [🔗 project](https://hazyresearch.stanford.edu/blog/2026-10-12-ncm)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 31 • 💬 1 • ⭐ 1,909 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](https://huggingface.co/papers/2609.33757)**

*Ruibin Yuan, Jiahao Pan, Junyan Jiang et al. (35 authors)*

🏢 Multimodal Art Projection

YuE2 unifies symbolic and audio music generation via symbolic planning, producing readable scores and full-song audio with state-of-the-art quality and agentic editing capabilities.

▲ 223 • 💬 3 • ⭐ 12,398 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33757) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue2.github.io/)

---

**[StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://huggingface.co/papers/2610.17309)**

*Xialie Zhuang, Zunhai Su, Jia Pan et al. (6 authors)*

🏢 StartLux

StartLux-Decision introduces efficient and adaptive decision models using single-pass prediction and confidence-guided reasoning, trained via a three-stage pipeline with RLCD² reinforcement learning, and evaluates them on Decision Index and the DecisionPivot benchmark.

▲ 20 • 💬 2 • ⭐ 898 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2610.17309) • [💻 code](https://github.com/StartLuxLabs/StartLux-Decision) • [🔗 project](https://decision.startlux.com/)

---

---

## GitHub Repositories: "ai"

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 8.2k • 🔱 2.0k • 9h ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 5.7k • 🔱 815 • 5d ago

---

**[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)**

A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding agents: Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more. Approve from the notch or your Lock Screen.

`Swift` `ai-agents` `anthropic` `antigravity` `claude` `claude-code`

⭐ 5.6k • 🔱 969 • 4h ago

---

**[omlahore/RemoveMacAI](https://github.com/omlahore/RemoveMacAI)**

Debloat macOS: turn off Apple Intelligence, analytics, ads and pop-ups. A native app and CLI, and every change can be undone.

`Swift` `apple-intelligence` `cli` `debloat` `macos` `macos-27`

⭐ 5.1k • 🔱 151 • 11h ago

---

**[QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)**

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

`JavaScript` `agent-skill` `ai-agent` `claude-code` `claude-code-skill` `claude-skill`

⭐ 4.1k • 🔱 277 • 6h ago

---

**[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)**

A comprehensive logo-design skill for Claude, Gemini CLI, Codex and other AI agents: principles, process, SVG craft, testing tools and a 1,400+ logo reference library.

`HTML` `agent-skills` `branding` `claude` `claude-skills` `codex`

⭐ 3.8k • 🔱 300 • 10h ago

---

**[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)**

A Claude Code / Codex plugin that helps you learn how to build while AI writes the code.

`Python`

⭐ 3.8k • 🔱 150 • 11d ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`C` `ai-agent` `airplay` `automation` `computer-use` `esp32`

⭐ 3.4k • 🔱 452 • 9h ago

---

**[nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)**

AI生成の日本語を自然な日本語へ推敲するAgent Skill / Agent Skill for Refining AI-Generated Japanese into Natural Japanese

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.3k • 🔱 77 • 2h ago

---

**[Folkbench/folkbench](https://github.com/Folkbench/folkbench)**

AI API 中转站评测排行与切换工具：实测可用率、延迟与价格 · Open-source AI API relay benchmark, rankings & switcher for Claude Code / Codex

`Rust` `ai` `api-relay` `api-relay-pricing` `benchmark` `benchmarks`

⭐ 2.2k • 🔱 9 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
