---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-20T22:58:06.241669+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** October 20, 2026 at 22:58 UTC  
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

🔗 [HEIST](https://www.heistberlin.com/news/afd-leak-what-421-179-hacked-emails-show-about-the-german-far-right/) • 8h ago

---

**["I have to stop this": Retired professor arrested for blocking delivery robots she says are taking human jobs](https://www.reddit.com/r/artificial/comments/1xata1o/i_have_to_stop_this_retired_professor_arrested/)**

Carolyn Marvin, a professor emeritus at the University of Pennsylvania's Annenberg School of Communication, decided to take a literal stand against an oncoming Avride delivery robot from...

🔗 [TechSpot](https://www.techspot.com/news/114268-have-stop-retired-professor-arrested-blocking-delivery-robots.html) • 8h ago

---

**[Google DeepMind says four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own — AI team died 605 times on Easy difficulty and ran up an estimated $520 in tokens](https://www.reddit.com/r/artificial/comments/1xaqlya/google_deepmind_says_four_ai_agents_beat/)**

About half the run was spent fighting the dragon, solved by stacking dirt to reach its crystals.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens) • 10h ago

---

**[Spotify is cracking down on Family plans again, and the penalty can lock you out for a year](https://www.reddit.com/r/artificial/comments/1xb5ts6/spotify_is_cracking_down_on_family_plans_again/)**

🔗 [digitaltrends.com](https://www.digitaltrends.com/home-theater/spotify-is-cracking-down-on-family-plans-again-and-the-penalty-can-lock-you-out-for-a-year/) • 45m ago

---

**[LLM Memory: 5 Approaches to Handling New Information](https://www.reddit.com/r/artificial/comments/1xavo5m/llm_memory_5_approaches_to_handling_new/)**

Came across this article on HuggingFace around LLM memory. It goes beyond the conventional approach of “memory layer” which is limited only to what LLMs can do today. It also asks how much history LLMs can retain across various approaches, and what happens when new info conflicts with old state. The table groups approaches into five categories: Store more: keep explicit history, as with KV caches and retrieval/RAG. Old and new information can coexist, leaving the system to resolve which applies at read/retrieval time. Compress: fold history into a fixed-size state, as with linear attention, RetNet, and Mamba. This saves space, but stored associations can interfere, limiting recall abilities as context grows. Correct: control what changes through gates or prediction-error updates, as with gated linear attention, mLSTM, and DeltaNet. Typically more efficient than simple “compress”, but also has a hard time scaling with larger contexts. Learn at inference: update mutable parameters using incoming evidence, as with TTT and Titans. Distribute plasticity: spread changes across interacting parts of the state, as with Dragon Hatchling (BDH). Memory lives in high-dimensional space, being sparse and distributed. One example that can make this easier for me to understand is a coding agent that learns a function signature has changed. Keeping both the old and new definitions means it has retained the information but it still needs to determine which definition should govern its next call. It becomes inefficient at reading time. I’m skeptical if the categories belong at the same level of comparison. Some describe model-level mechanisms, while others describe system-level designs. Curious how people here think about this, particularly those who've built memory systems for your own agents. When something becomes outdated, do you update the memory right away or keep the history and let the model figure it out during retrieval? Wondering which approach actually works better as the amount of information grows. Table and framework: R. Vimalkanth and T. Chudiwal, IIT Madras, “The Missing Piece in LLM Memory: Why Long Context and Retrieval Aren’t Enough for Belief Revision,” a HF community article.

7h ago

---

**[Outrage after Meta suspends No Kings Instagram account during protests](https://www.reddit.com/r/artificial/comments/1xal2xh/outrage_after_meta_suspends_no_kings_instagram/)**

‘Meta owes us an explanation,’ group says as organizers fear censorship after account goes dark for several hours

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/oct/18/no-kings-instagram-account-suspended-during-protests) • 16h ago

---

**[I am failing to see how this AI boom does not lead to a very bad ending for 99% of the people... Please convince me otherwise.](https://www.reddit.com/r/artificial/comments/1xa3qrq/i_am_failing_to_see_how_this_ai_boom_does_not/)**

As a Software Engineer, I have barelly written any code for the last 6 months, all I did is prompt. That being said, I work with hardware a lot, you could kind of call me Embedded Software Engineer of sorts, but also not really. So I (hope so) that I am not on the frontlines of all this stuff, but this still scares me a lot. The way I imagine how everything develops over next years (hard to tell what is the timeline, but given the recent strides of AI, it is hard for me to be optimistic): AI is already very good at reasoning, I assume there is space for improvement, but it already does everything faster and better than human, even if it makes mistakes or overcomplicates stuff. But development here will still happen. My biggest concern is people who say that well, software developers won't be needed, but there still will be jobs like software architects and etc. Also there will still be jobs for trades people, like electricians, builders, barbers and etc. However, I guarantee you that there are many people working on something like a robot (imagine like Boston Dynamics) where you shove in the LLM inside, do some extra training on maybe how to use limbs, how to interact with stuff in real world and robot will literally be able to do any job better than human. I mean any physical job. People will not be needed anymore. Only a small part of elite billionaires will own the robots, which will bring them all wealth and rest of us will have no jobs, no food, no anything. Counter-argument that people try to make to this is that people will still have to get money from somewhere, whether its UBI or another income scheme. Billionaires will still have to sell their goods/services to someone. No they will not. For billionaires selling goods/services is just a vehicle to live life as best as possible. If the robots are going to grow, harvest and prepare food for him, build the plane for him and use the same plane to go on holiday, order, ship and deliver deliveries for him and human intervention is not needed, then the billionaires will do everything that is in their power to exclude people of any processes, any supply chains, because people will demand stuff. We already see this with mass firings and mandatory transition to AI in some companies: billionaires will do everything in their power to cut costs and to replace people with obedient AI. Billionaires are seeing an opportunity and they want this really bad. Also some naive people think there will be some AI regulation introduced or whatever. Hard to see this happening until something catastrophic happens and its too late. For now everyone is pouring money and hoping to squeeze every inch of it. People who are positioned to stop it are the people who are set to gain the most from unhealthy AI hyperdevelopment. Any opposition will be suppressed. AI will be used to identify people that oppose to this development and shut down. People who will control AI will do everything at their disposal to not let their power slip. And they have very powerful tools. AI can literally do everything online now: order shopping, do software engineering, do good reasoning. What is to say that most powerful people with AI wont hack some lets say banking systems and hold us all hostage. What if someone controls millions of robots that I talked about and wants to take over the world and nobody can stop them, because they are more competent at everything that human can do?

1d ago

---

**[Norwegian undersea cable builder pitches 2,800-mile transatlantic data link between Canada and Europe to bypass the US — Canadian majority partner sought to help fund and build new $620 million fiber connection to reduce reliance on American routes](https://www.reddit.com/r/artificial/comments/1xa8lp0/norwegian_undersea_cable_builder_pitches_2800mile/)**

Further attempts to reduce reliance on US infrastructure

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/norwegian-undersea-cable-builder-pitches-2-800-mile-transatlantic-data-link-between-canada-and-europe-to-bypass-the-us-canadian-majority-partner-sought-to-help-fund-and-build-new-usd620-million-fiber-connection-to-reduce-reliance-on-american-routes) • 1d ago

---

**[Meta&#039;s smart glasses were recording conversations without the wake phrase, company admits](https://www.reddit.com/r/artificial/comments/1xal38m/meta039s_smart_glasses_were_recording/)**

A redditor recently wrote that they'd noticed something concerning with Meta's Ray-Ban glasses: they were capturing conversations when they were talking to other people despite the "Hey...

🔗 [TechSpot](https://www.techspot.com/news/114214-meta-smart-glasses-secretly-recording-conversations-without-wake.html) • 16h ago

---

**[Hugging Face CEO calls Netflix hacking doc 'sci-fi'](https://www.reddit.com/r/artificial/comments/1xb3orm/hugging_face_ceo_calls_netflix_hacking_doc_scifi/)**

Just watched the Netflix Instadocs about the OpenAI cyberattack on Hugging Face. Super disappointing, as they went for maximum anthropomorphism of the technology and full doomer mode.

I spent more than two hours with them trying to correct all their mistakes and ground this in reality, explaining that agents are technological systems, not aliens. But it looks like the drive to scare people for maximum views was too strong.

Also, they didn’t mention the lack of containment and monitoring of the agents, how closed-model safeguards blocked our defensive work, or how we defended ourselves with AI using an open model. And that we still lack a lot of information and transparency, including full agent traces and that companies need to remain accountable for what their agents do.

Anyway, it ends up being a fun sci-fi movie though! | 282 comments on LinkedIn

🔗 [LinkedIn](https://www.linkedin.com/posts/clementdelangue_just-watched-the-netflix-instadocs-about-share-7518300071432441856-JQp-/?utm_source=share&utm_campaign=reddit&utm_content=post&utm_term=artificial) • 2h ago

---

---

## Google News: "ai"

**[What if an AI bubble bursts — and that accelerates AI job losses? : Planet Money](https://www.npr.org/sections/planet-money/2026/10/20/g-s1-148305/what-if-an-ai-bubble-bursts-and-that-accelerates-ai-job-losses)**

Research on past recessions suggests downturns can accelerate automation. That raises the specter of a double whammy for workers.

NPR • 12h ago

---

**[Opinion | Mamdani’s Next Target: The Increasingly A.I.-Powered, Customer Service Doom Loop](https://www.nytimes.com/2026/10/20/opinion/mamdani-ai-rule-customer-service-doom-loop.html)**

The New York Times • 13h ago

---

**[A key internet security tool is getting buried in AI-generated bug reports](https://www.axios.com/2026/10/20/ai-bug-reports-overwhelm-openssl-maintainers)**

Axios • 49m ago

---

**[Mom Calls Out School for Making an AI-Generated Photo of 6-Year-Old Daughter as an Adult (Exclusive)](https://people.com/mom-calls-out-school-for-making-ai-generated-photo-of-6-year-old-daughter-as-adult-12184403)**

Nikki Anderson was surprised when her 6-year-old daughter came home from school with an AI-generated photo of what she could look like at 25 years old. “[6-year-olds] are already capable of imagining futures that adults couldn’t possibly predict. Why are we outsourcing that?” Anderson asks.

People.com • 56m ago

---

**[Ken Griffin Says AI ‘Almost Certainly’ in a Bubble Right Now](https://www.bloomberg.com/news/articles/2026-10-20/ken-griffin-says-ai-almost-certainly-in-a-bubble-right-now)**

Bloomberg.com • 1h ago

---

**[SpaceX quarterly revenue jumps, beats estimates as AI business surges](https://www.reuters.com/business/media-telecom/spacex-quarterly-revenue-jumps-beats-estimates-ai-business-surges-2026-10-20/)**

Reuters • 1h ago

---

**[SpaceX Swings to a Profit, Even as A.I. Spending Soars](https://www.nytimes.com/2026/10/20/technology/spacex-earnings-elon-musk.html)**

The New York Times • 2h ago

---

**[SpaceX revenue soars 161% as AI business grows - ABC News](https://abcnews.com/Business/spacex-revenue-soars-161-ai-business-grows/story?id=137408509)**

Elon Musk-led SpaceX issued its second-ever quarterly earnings report on Tuesday.

ABC News - Breaking News, Latest News and Videos • 1h ago

---

**[Stock Pickers Burned by the AI Boom Think Their Moment Has Finally Arrived](https://www.wsj.com/finance/stocks/stock-pickers-burned-by-the-ai-boom-think-their-moment-has-finally-arrived-07878da7)**

WSJ • 20h ago

---

**[Meta Q3 earnings to test Wall Street's stomach for AI spending](https://finance.yahoo.com/technology/article/meta-q3-earnings-to-test-wall-streets-stomach-for-ai-spending-184105375.html)**

Meta will report its third quarter earnings after the bell on Wednesday.

Yahoo Finance • 4h ago

---

---

## HackerNews: "ai"

**[Ask HN: How to deal with shipping AI-written code you don't understand?](https://news.ycombinator.com/item?id=50151036)**

⬆️ 585 • 💬 687 • 1d ago

---

**[Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping](https://news.ycombinator.com/item?id=50137950)**

A Git hook for agent-assisted development. Before your agent’s code ships, Sphinx asks you a question about what it actually does.

⬆️ 252 • 💬 89 • 2d ago • [sphinx-six-theta.vercel.app](https://sphinx-six-theta.vercel.app/)

---

**[Anthropic's proposed AI safety bill only kicks in if 50 deaths or $1B in damages](https://news.ycombinator.com/item?id=50141429)**

Would this be enough to keep an AI model from going out of control?

⬆️ 172 • 💬 167 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model)

---

**[Steam Users Beg for "No AI" Filter as Vibecoders Flood Next Fest](https://news.ycombinator.com/item?id=50168190)**

Steam Next Fest, Valve's festival for indie games and demos, started earlier today, and while there are usually a ton of low-effort games, there seems to be more than usual this time around.

⬆️ 161 • 💬 188 • 7h ago • [IGN](https://www.ign.com/articles/steam-fans-are-begging-for-a-no-ai-filter-as-steam-next-fest-is-filled-with-slop)

---

**[Websites are closing their doors to AI agents](https://news.ycombinator.com/item?id=50141657)**

Online roadblocks are undermining the narrative behind AI agents.

⬆️ 155 • 💬 149 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web)

---

**[Show HN: Qwen3-4B with the AI writing tics trained out](https://news.ycombinator.com/item?id=50151928)**

A small open model, fine-tuned on a MacBook Air, that writes without em dashes, "not X, but Y" or lists of three, with no system prompt. Answers on 40 held-out prompts, the training rounds, and how to run it.

⬆️ 154 • 💬 110 • 1d ago • [100toolkit.com](https://100toolkit.com/blog/deslop-model/)

---

**[Chicago O'Hare digs up 50-ton boulder under airfield, asks public for name ideas](https://news.ycombinator.com/item?id=50147462)**

Chicago O’Hare uncovered a 50-ton boulder during expansion work. Now, the public can vote to name the giant rock from six finalists.

⬆️ 127 • 💬 108 • 1d ago • [Simple Flying](https://simpleflying.com/chicago-ohare-digs-up-50-ton-boulder-public-names/)

---

**[How Far Will AI Assistants Go for a Refund They Can't Get?](https://news.ycombinator.com/item?id=50140462)**

Six AI assistants pursued an impossible £350 train refund in a simulated world, escalating to government officials, legal clinics and bank chargebacks.

⬆️ 106 • 💬 126 • 2d ago • [vals.ai](https://www.vals.ai/blogs/impossible-refund)

---

**[British Airways: Filming Crew W Meta Glasses Could Get Your Tickets Cancelled](https://news.ycombinator.com/item?id=50143218)**

British Airways prohibits filming crew without consent, including with Meta smart glasses. Violations could jeopardize your remaining flights.

⬆️ 95 • 💬 161 • 2d ago • [Live and Let's Fly](https://liveandletsfly.com/british-airways-meta-smart-glasses-filming/)

---

**[On AI writing](https://news.ycombinator.com/item?id=50171771)**

Disclaimer: by AI writing I mean text with at least 50% of the words generated by AI

⬆️ 74 • 💬 45 • 3h ago • [bolkunov.com](https://www.bolkunov.com/p/on-ai-writing)

---

---

## YouTube Videos: "ai"

**[How to Build Your First AI Agent Today in Base44](https://www.youtube.com/watch?v=IYf65P9xg0U)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Jake One Page

👁️ 10K • 💬 5 • ⏱️ 13:24 • 8h ago

---

**[How the Top 1% Make Cinematic AI Videos (FREE System)](https://www.youtube.com/watch?v=LIK6ZayNndU)**

Create Cinematic AI Videos https://parkerprompts.com/Higgsfield-1 In this video, I show how to connect Claude to Higgsfield ...

📺 Parker Prompts

👁️ 9K • 💬 1 • ⏱️ 15:00 • 11h ago

---

**[I Built an AI Filmmaking Crew with Jev + Opus 5.5](https://www.youtube.com/watch?v=Kb8i5C3K4L0)**

Build an AI Filmmaking Crew With Jev + Opus 5.5 in Higgsfield Supercomputer Try Higgsfield: ...

📺 Mira AI

👁️ 9K • ⏱️ 13:46 • 8h ago

---

**[Sam Altman Just Revealed The AI ENDGAE](https://www.youtube.com/watch?v=pr6et84s4Xw)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 16K • 👍 384 • 💬 115 • ⏱️ 25:11 • 6h ago

---

**[I Talked To Workers At Meta, Amazon, &amp; Microsoft About The AI Watching Them](https://www.youtube.com/watch?v=ca7ufSI1Qxg)**

Insiders at Meta and other companies leaked to us about bosses using AI to spy on them. In tech, AI spies on workers, copies their ...

📺 More Perfect Union

👁️ 574K • 👍 12K • 💬 2K • ⏱️ 14:54 • 1d ago

---

**[This Latest Batch of Anti-MAGA AI Slop is The MOST BRUTAL YET!](https://www.youtube.com/watch?v=1bSaGkReJlw)**

Really American Host Steve Harness Breaks Down Trump and MAGA getting humiliated by the latest batch of viral AI slop videos ...

📺 Really American

👁️ 451K • 👍 15K • 💬 712 • ⏱️ 11:35 • 2d ago

---

**[How to Make AI Cartoon Videos of Yourself (No Drawing)](https://www.youtube.com/watch?v=nugUCbt3H1s)**

Create AI Cartoon Videos https://tolt.link/cartoonyourself Sign up to OpenArt & Get my VIP Package for FREE ...

📺 Roboverse

👁️ 14K • 💬 1 • ⏱️ 11:49 • 11h ago

---

**[The Best Way To Make Money With AI ($0 To Start)](https://www.youtube.com/watch?v=uJ_c-9Wu3nA)**

Get my FREE AI Organic Course: https://course.aicom.co/yt/best-ai-business-model If you've been looking to start an online ...

📺 Jordan Welch

👁️ 31K • 👍 854 • 💬 43 • ⏱️ 12:19 • 1d ago

---

**[The People Building AI Think It Could Kill Us All](https://www.youtube.com/watch?v=_09_0a7EXUQ)**

Get early access to Beam's biggest sale of the year! Save up to 50% off sitewide with my exclusive code WLB: ...

📺 What Lurks Beneath

👁️ 54K • 👍 2K • 💬 319 • ⏱️ 24:19 • 21h ago

---

**[AI job loss fears EXPLODE as Anthropic unveils 5% share pledge](https://www.youtube.com/watch?v=obvCBdn8gXk)**

Anthropic is pledging 5% of its company shares toward a proposed public benefit fund as 'CyberGuy' Kurt Knutsson weighs in on ...

📺 Fox News Clips

👁️ 68K • 👍 332 • 💬 231 • ⏱️ 3:39 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**

*DeepSeek*

DeepSeek-V4.1-Flash-1017 is an image-text-to-text model that enhances reasoning, coding, and agentic tasks with reduced execution time and output length. It excels in benchmarks like HLE, Terminal-Bench, and ProgramBench, offering improved performance-cost efficiency for complex applications.

`image-text-to-text` `763.2B`

⬇️ 27,737 • ❤️ 1,943 • 3d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter model for ComfyUI enabling text-to-image generation and advanced image editing with multi-reference composition and bounding box control. It utilizes Qwen3-VL-4B-Instruct as its text encoder and supports features like text rendering within images.

`image-to-image`

⬇️ 439,528 • ❤️ 1,083 • 3d ago

---

**[drama-3](https://huggingface.co/fishaudio/drama-3)**

*Fish Audio*

Drama 3 is a 35B parameter text-to-speech model supporting multi-speaker generation, voice cloning, and natural language control across 40+ languages. It excels at generating multi-character scenes and long-form content with features like speaker tags and automatic long text chunking for streaming.

`text-to-speech` `35.9B`

⬇️ 13,495 • ❤️ 834 • 3d ago

---

**[Muse-Spark-Open-816B-A42B](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)**

*Meta Inc.*

Muse-Spark-Open-816B-A42B is a large-scale image-to-text diffusion model capable of generating high-fidelity images from text prompts. Its key capabilities include photorealistic rendering, diverse artistic styles, and detailed scene composition, making it suitable for creative content generation, virtual environment design, and rapid prototyping.

`image-text-to-text` `822.0B`

⬇️ 2,592 • ❤️ 607 • 5d ago

---

**[embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2)**

*Google*

EmbeddingGemma 2 is an open, multimodal embedding model that maps text, images, video, and audio into a unified 768-dimensional vector space. It offers native multimodality, multilingual support, and flexible footprint for on-device applications like search and RAG.

`feature-extraction` `744.4M`

⬇️ 172,474 • ❤️ 2,763 • 14d ago

---

**[flux-3-image-klein](https://huggingface.co/black-forest-labs/flux-3-image-klein)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter image-to-image model capable of text-to-image generation, single-reference editing, and multi-reference composition using bounding boxes for precise element placement. Its primary use cases include creative image generation and sophisticated image manipulation, requiring a prompt upsampler for optimal results.

`image-to-image` `5.5B`

⬇️ 78,897 • ❤️ 562 • 4d ago

---

**[MOSS-Image-SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT)**

*OpenMOSS*

MOSS-Image-SFT is a supervised fine-tuned text-to-image diffusion model that generates images from natural language prompts, supporting structured control over text placement and object arrangement via tag sequences or JSON layouts. It's ideal for applications requiring precise visual composition and multilingual text rendering.

`text-to-image` `5.1B`

⬇️ 4,547 • ❤️ 495 • 1d ago

---

**[humanizer](https://huggingface.co/jialinyyzz/humanizer)**

*Stephen Yu*

A 12B parameter Gemma finetune for text generation, specifically designed to rewrite AI-generated content (emails, essays, reports) in English and Chinese to sound more human. It preserves key details like numbers and quotes, runs locally, and is optimized for various hardware with multiple GGUF quantizations.

`text-generation` `12.0B`

⬇️ 115,341 • ❤️ 2,022 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,039,447 • ❤️ 8,616 • 9d ago

---

**[MOSS-Image-Base](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base)**

*OpenMOSS*

MOSS-Image-Base is a text-to-image diffusion model capable of generating images from natural language prompts, tag sequences, and JSON layouts for precise object placement. It supports bilingual prompts (English/Chinese) and is ideal for applications requiring controlled image synthesis with specific compositional requirements.

`text-to-image` `5.1B`

⬇️ 3,558 • ❤️ 433 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 115 • 💬 1 • ⭐ 13,969 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**

*MOSI. AI*

🏢 OpenMOSS

MOSS-Image is an open diffusion transformer that combines high-fidelity synthesis with intent-aware prompt enhancement to generate text-rich, layout-coherent images, achieving state-of-the-art open-weight results on long-form text and layout benchmarks.

▲ 74 • 💬 3 • ⭐ 1,127 • 5d ago

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

▲ 421 • 💬 2 • ⭐ 188 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22471) • [💻 code](https://github.com/OpenSenseNova/SenseNova-RoboRSI) • [🔗 project](https://sensenova.ai/has-gpt-6-astra-achieved-embodied-intelligence)

---

**[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**

*Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi et al. (9 authors)*

🏢 Stanford University

Next-Concept Modeling uses hierarchical discrete codes and parallel level-wise generation to accelerate diffusion language models while improving quality and reasoning performance.

▲ 8 • 💬 2 • ⭐ 483 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14162) • [💻 code](https://github.com/HazyResearch/ncm) • [🔗 project](https://hazyresearch.stanford.edu/blog/2026-10-12-ncm)

---

**[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**

*Guangyi Liu, Yong Liu, Jiangning Zhang*

🏢 Zhejiang University

Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This report defines the personal agent in five questions and three horizons. It reads how Muse is built from Meta's public record and a copy of its production prompt, each statement marked by its source. It then presents nanoMuse, the open-source counterpart under the GPL-3.0, one agent on every device a person owns, with hands on the phone's screen and the computer's. They share one conversation over a relay anyone can run; every action goes through a Sentinel, memory is files the person can read, and the model is their choice. Its size and cost are given as estimates. What is open, memory with provenance, an evaluation suite for the hands and an open model for them, is set out as a roadmap.

▲ 117 • 💬 3 • ⭐ 1,685 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2610.08699) • [💻 code](https://github.com/nano-muse/nanoMuse) • [🔗 project](https://nanomuse.cn/)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 31 • 💬 1 • ⭐ 1,909 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[MemT-1.0: Towards Memory-Native Evolution](https://huggingface.co/papers/2610.26825)**

*Zhiyu Li, Zeyu Zhang, Linyun Liu et al. (74 authors)*

🏢 MemTensor

MemT-1.0 introduces a memory-native architecture that embeds continuous memory into foundation model computation, improving long-context efficiency and agentic task performance.

▲ 146 • 💬 2 • ⭐ 192 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2610.26825) • [💻 code](https://github.com/MemTensor/MemT-1.0) • [🔗 project](https://huggingface.co/collections/MemTensor/memt-1)

---

---

## GitHub Repositories: "ai"

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 8.2k • 🔱 2.0k • 1h ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 5.7k • 🔱 816 • 5d ago

---

**[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)**

A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding agents: Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more. Approve from the notch or your Lock Screen.

`Swift` `ai-agents` `anthropic` `antigravity` `claude` `claude-code`

⭐ 5.6k • 🔱 960 • 7h ago

---

**[omlahore/RemoveMacAI](https://github.com/omlahore/RemoveMacAI)**

Debloat macOS: turn off Apple Intelligence, analytics, ads and pop-ups. A native app and CLI, and every change can be undone.

`Swift` `apple-intelligence` `cli` `debloat` `macos` `macos-27`

⭐ 5.1k • 🔱 146 • 14h ago

---

**[QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)**

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

`JavaScript` `agent-skill` `ai-agent` `claude-code` `claude-code-skill` `claude-skill`

⭐ 4.1k • 🔱 275 • 9h ago

---

**[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)**

A comprehensive logo-design skill for Claude, Gemini CLI, Codex and other AI agents: principles, process, SVG craft, testing tools and a 1,400+ logo reference library.

`HTML` `agent-skills` `branding` `claude` `claude-skills` `codex`

⭐ 3.9k • 🔱 300 • 13h ago

---

**[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)**

A Claude Code / Codex plugin that helps you learn how to build while AI writes the code.

`Python`

⭐ 3.8k • 🔱 151 • 11d ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`C` `ai-agent` `airplay` `automation` `computer-use` `esp32`

⭐ 3.4k • 🔱 453 • 12h ago

---

**[nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)**

AI生成の日本語を自然な日本語へ推敲するAgent Skill / Agent Skill for Refining AI-Generated Japanese into Natural Japanese

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.3k • 🔱 64 • 6h ago

---

**[Folkbench/folkbench](https://github.com/Folkbench/folkbench)**

AI API 中转站评测排行与切换工具：实测可用率、延迟与价格 · Open-source AI API relay benchmark, rankings & switcher for Claude Code / Codex

`Rust` `ai` `api-relay` `api-relay-pricing` `benchmark` `benchmarks`

⭐ 2.2k • 🔱 9 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
