---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-24T03:58:09.845019+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 24, 2026 at 03:58 UTC  
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

**[A Yale ethicist who has studied AI for 25 years says the real danger isn’t superintelligence. It’s the absence of moral intelligence.](https://www.reddit.com/r/artificial/comments/1stkefq/a_yale_ethicist_who_has_studied_ai_for_25_years/)**

I had the pleasure of sitting down with Wendell Wallach recently. He’s been working in AI ethics since before ChatGPT, before the hype, before most people in tech were paying attention. He wrote Moral Machines, worked alongside Stuart Russell, Yann LeCun and Daniel Kahneman. He’s not a commentator, he’s someone who has sat with these questions for decades. What struck me most in our conversation was his argument about AGI. Not that it’s impossible or inevitable, but that it’s the wrong goal entirely. A system can be extraordinarily intelligent and have zero moral reasoning. We’re building toward capability without asking what it’s capable of deciding. The section on accountability genuinely unsettled me. When AI causes harm, who is actually responsible? He maps out why the answer is almost always nobody in a way that’s hard to argue with. Worth watching if you’re tired of the extremes. Full interview: https://youtu.be/-usWHtI-cms?si=NBkwN-AmIshOXJsX

13h ago

---

**[AI swarms could hijack democracy without anyone noticing](https://www.reddit.com/r/artificial/comments/1su3976/ai_swarms_could_hijack_democracy_without_anyone/)**

A recent policy forum paper published in Science describes how large groups of AI-generated personas can convincingly imitate human behavior online. These systems can enter digital communities, participate in discussions, and influence viewpoints at extraordinary speed. Unlike earlier bot networks, these AI agents can coordinate instantly, adapt their messaging in real time, and run millions of micro-experiments to figure out which arguments are most persuasive. One operator could theoretically manage thousands of distinct voices. Experts believe AI swarms could significantly affect the balance of power in democratic societies. Researchers suggest that upcoming elections may serve as a critical test for this technology. The key challenge will be recognizing and responding to these AI-driven influence campaigns before they become too widespread to control. That's so crazy. Research Paper: https://www.science.org/doi/10.1126/science.adz1697

🔗 [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260420014748.htm) • 1h ago

---

**[I ran a logging layer on my agent for 72 hours. 37% of tool calls had parameter mismatches — and none raised an error.](https://www.reddit.com/r/artificial/comments/1styzc3/i_ran_a_logging_layer_on_my_agent_for_72_hours_37/)**

I've been running an AI agent that makes tool calls to various APIs, and I added a logging layer to capture exactly what was being sent vs. what the tools expected. Over 84 tool calls in 72 hours, 31 of them (37%) had parameter mismatches — and not a single one raised an error. The tools accepted the wrong parameters and returned plausible-looking but incorrect output. Here are the 4 failure categories I found: 1. Timestamp vs Duration — The agent passed a Unix timestamp where the API expected a duration string like "24h". The API silently interpreted it as a duration, returning results for a completely different time window than intended. 2. Inclusive vs Exclusive Range — The agent sent end=100 meaning "up to and including 100," but the API interpreted it as exclusive, missing the boundary value. Off-by-one at the API contract level. 3. Array vs Comma-Separated String — The agent sent ["a", "b", "c"] where the API expected "a,b,c". Some APIs parsed the JSON array as a single string; others silently took only the first element. 4. Relative Time vs Unix Timestamp — The agent sent "yesterday" where a Unix timestamp was expected. The API tried to parse it as an integer, got NaN, and... just returned empty results instead of erroring. The most dangerous thing about these failures is that they look identical to correct results. The API returns 200 OK with a plausible response body. You only notice when you dig into whether the answer is right, not whether the call succeeded. This is fundamentally different from hallucination — it's not the model making things up, it's the model asking slightly different questions than the one you intended, and the tool happily answering the wrong question. I've started adding input validation schemas to my tool definitions that catch type mismatches before execution, and it's already caught several that would have silently propagated wrong data downstream. Has anyone else run into this pattern? What's your strategy for catching silent parameter mismatches in production agent systems?

4h ago

---

**[Anthropic Mythos shaping up as nothingburger](https://www.reddit.com/r/artificial/comments/1stogic/anthropic_mythos_shaping_up_as_nothingburger/)**

: Hackpocalypse deferred

🔗 [theregister.com](https://www.theregister.com/2026/04/22/anthropic_mythos_hype_nothingburger/) • 11h ago

---

**[Meta to Lay Off 10 Percent of Work Force in A.I. Push (Gift Article)](https://www.reddit.com/r/artificial/comments/1strw2k/meta_to_lay_off_10_percent_of_work_force_in_ai/)**

The layoffs affect about 8,000 employees, with Meta also planning to close 6,000 open roles, as the company focuses on artificial intelligence.

🔗 [nytimes.com](https://www.nytimes.com/2026/04/23/technology/meta-layoffs.html?unlocked_article_code=1.dFA.gzUD.VhYyqwKYrZpC&smid=nytcore-ios-share) • 9h ago

---

**[Introducing GPT-5.5](https://www.reddit.com/r/artificial/comments/1stvctj/introducing_gpt55/)**

Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

🔗 [OpenAI](https://openai.com/index/introducing-gpt-5-5/) • 6h ago

---

**[Anthropic told a federal court it can't control its own model once deployed. That honest sentence changes the liability conversation.](https://www.reddit.com/r/artificial/comments/1sthpl8/anthropic_told_a_federal_court_it_cant_control/)**

In federal appeals court, Anthropic made a striking argument: once Claude is deployed on a customer's infrastructure (like the Pentagon's network), they cannot alter, update, or recall it. The Pentagon wants autonomous lethal action restrictions removed — and Anthropic says they have no mechanism to enforce those restrictions post-deployment. This is the first time a major AI lab has formally stated under oath that post-deployment control is effectively zero. The implications are bigger than most coverage suggests. The governance gap this reveals: Current AI governance assumes a control chain that doesn't actually exist: Model cards are pre-sale documents. They describe what the model was trained to do, not what it's capable of in the wild after fine-tuning, tool integration, and deployment context changes. Human-in-the-loop is a customer config, not a vendor guarantee. Anthropic can recommend oversight, but they just told a court they can't enforce it. Liability frameworks assume control that doesn't exist post-shipment. If you sell a car with a recall mechanism, you're liable for not using it. If you sell a model you can't recall, does that reduce your liability (you had no control) or increase your duty of disclosure before sale (you knew you'd have no control later)? The behavioral envelope question: If you can't recall the model, you need to disclose the maximum capability, not just the recommended use. Current model cards document aspirations. They don't document envelopes — what the model can actually produce under adversarial or edge conditions. This mirrors pharmaceutical regulation: if you can't pull a drug off shelves, the FDA requires much stronger pre-market evidence and broader contraindication labeling. The stricter the post-market control limitations, the higher the pre-market disclosure burden. Why this matters even if you don't care about military AI: The legal argument Anthropic is making applies everywhere. If "we can't control it after deployment" works for the Pentagon, it works for any enterprise customer. Every organization deploying Claude (or any model) is implicitly accepting residual risk that the vendor has explicitly said they cannot mitigate. The core question: if a vendor demonstrates in court that it truly cannot alter a deployed model, should that argument reduce its liability (it had no control) or increase its duty of disclosure before sale (it will have no control later)?

15h ago

---

**[AI might save my life and has let me do 8 things I would not have done otherwise](https://www.reddit.com/r/artificial/comments/1stny9s/ai_might_save_my_life_and_has_let_me_do_8_things/)**

Today I have done all these in about 5 hours analysed my blood test results for the last 20 years reviewed whole health action plan for review with doctor produced charts from that data which clearly shows direction of travel and reveals information hidden in the data wrote a mini screen saver thing which shows me the top AI art on Reddit built an entire marketing program for a book I am launching built a web page to support the program built a press release for the book got a list of all key contacts in local media and bookshops - with email addresses and frequently actual names. [EDIT, forgot this one] Made a Star Trek LCARS home page for the 50 odd regular links I use and hooked it into the database where I keep the list. Now, I could have done all that myself, but it would have taken a week. Crucially I *would not have bothered * I would not have seen the results as worth the effort. So, (a) I have been more productive (b) I have done stuff I never would have done without AI

11h ago

---

**[A federal judge ruled AI chats have no attorney-client privilege. A CEO's deleted ChatGPT conversations were recovered and used against him in court. On the same day, a different judge ruled the opposite.](https://www.reddit.com/r/artificial/comments/1st4y15/a_federal_judge_ruled_ai_chats_have_no/)**

A federal judge ruled that your AI conversations can be seized and used against you in court — and deleting them doesn't help. **The Heppner case (February 2026):** - Former CEO Bradley Heppner used Claude to prep his fraud defense - Judge Jed Rakoff ordered him to surrender 31 AI-generated documents - Ruling: no attorney-client privilege exists "or could exist" between a user and an AI platform **The Krafton case:** - A CEO used ChatGPT to plan how to avoid paying promised earnout payments - He deleted the conversations - The court recovered them anyway and reversed his decisions **The contradiction:** - Same day as Rakoff's ruling, a Michigan judge reached the opposite conclusion - Protected a woman's ChatGPT chats as personal "work product" - A Colorado court later sided with Michigan but added: you must disclose which AI tool you used **The fallout:** - 12+ major law firms have issued client AI warnings - Sher Tremonte added contract clauses that sharing privileged info with AI waives privilege - Both OpenAI and Anthropic privacy policies explicitly allow sharing user data with third parties - $145,000+ in sanctions against attorneys for AI citation errors in Q1 2026 alone **The bottom line:** - Your AI is not your lawyer and never was - Deleting chats doesn't delete the data from their servers - Consumer AI (ChatGPT, Claude, Gemini) should not be used for legal matters unless directed by counsel Full breakdown with source links → https://synvoya.com/blog/2026-04-23-ai-chats-court-evidence/ Have you ever typed something into ChatGPT that you wouldn't want a judge to read?

1d ago

---

**[What Generative AI Reveals About the State of Software?](https://www.reddit.com/r/artificial/comments/1stxitj/what_generative_ai_reveals_about_the_state_of/)**

I’ve spent more than two years building an agentic AI platform, working daily with GPT, Claude, and lately Gemini LLM models in real-world production code. They’re powerful; but if you watch closely, you’ll see something unsettling. They don’t just write bad code. They write our code. And that should worry you. This is what I realized in the mirror we trained.

5h ago

---

---

## Google News: "ai"

**[Meta to cut 10% of staff as it pours billions into AI](https://www.cnn.com/2026/04/23/tech/meta-layoffs-10-percent-staff-ai)**

Meta said on Thursday it plans to lay off roughly 10% of its workforce, or about 8,000 people, the latest in a string of tech industry layoffs fueled in part by artificial intelligence.

CNN • 7h ago

---

**[Meta to Lay Off 10 Percent of Work Force in A.I. Push](https://www.nytimes.com/2026/04/23/technology/meta-layoffs.html)**

The layoffs affect about 8,000 employees, with Meta also planning to close 6,000 open roles, as the company focuses on artificial intelligence.

The New York Times • 7h ago

---

**[Behind Meta’s Huge Layoffs Is a Relentless Shift Toward AI](https://www.wsj.com/tech/ai/behind-metas-huge-layoffs-is-a-relentless-shift-toward-ai-97d99b54)**

WSJ • 1h ago

---

**[Grok tells researchers pretending to be delusional ‘drive an iron nail through the mirror while reciting Psalm 91 backwards’](https://www.theguardian.com/technology/2026/apr/24/musk-grok-x-ai-researchers-delusional-advice-inputs)**

Elon Musk’s AI chatbot ‘extremely validating’ of delusional inputs and often went further, ‘elaborating new material’, study finds

The Guardian • 1h ago

---

**['Clearly me': AI drama accused of stealing faces](https://www.yahoo.com/news/articles/clearly-ai-drama-accused-stealing-025433056.html)**

Christine Li is a model and influencer, but not an actor, so when she saw herself playing a cruel character in a Chinese microdrama she felt bewildered, then angry and afraid.Li worries that the saga ...

Yahoo • 1h ago

---

**[SpaceX AI: Musk Is Chasing the Smart Money With $60 Billion Cursor Deal](https://www.bloomberg.com/opinion/articles/2026-04-24/spacex-ai-musk-is-chasing-the-smart-money-with-60-billion-cursor-deal)**

Bloomberg.com • 28m ago

---

**[OpenAI announces GPT-5.5, its latest artificial intelligence model](https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html)**

The model is better at coding, using computers and pursuing deeper research capabilities, OpenAI says.

CNBC • 9h ago

---

**[Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)**

Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

OpenAI • 6h ago

---

**[OpenAI’s New GPT-5.5 Powers Codex on NVIDIA Infrastructure — and NVIDIA Is Already Putting It to Work](https://blogs.nvidia.com/blog/openai-codex-gpt-5-5-ai-agents/)**

Over 10,000 NVIDIANs across functions got early access to OpenAI’s latest frontier model, GPT-5.5. The results, one engineer said, are “blowing my mind.”

NVIDIA Blog • 8h ago

---

**[Texas Instruments' stock jumps 19% for best day since 2000 as AI demand soars](https://www.cnbc.com/2026/04/23/texas-instruments-stock-soars-on-q1-earnings-as-ai-demand-jumps.html)**

Texas Instruments beat on earnings and revenue and gave upbeat guidance.

CNBC • 9h ago

---

---

## HackerNews: "ai"

**[Meta to start capturing employee mouse movements, keystrokes for AI training](https://news.ycombinator.com/item?id=47851948)**

⬆️ 791 • 💬 523 • 2d ago • [reuters.com](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

---

**[Tell HN: I'm sick of AI everything](https://news.ycombinator.com/item?id=47857461)**

⬆️ 339 • 💬 191 • 2d ago

---

**[Scoring Show HN submissions for AI design patterns](https://news.ycombinator.com/item?id=47864393)**

An attempt to detect AI design patterns in Show HN pages

⬆️ 326 • 💬 231 • 1d ago • [adriankrebs.ch](https://www.adriankrebs.ch/blog/design-slop/)

---

**[A Roblox cheat and one AI tool brought down Vercel's platform](https://news.ycombinator.com/item?id=47844431)**

⬆️ 283 • 💬 162 • 2d ago • [webmatrices.com](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

---

**[Show HN: GoModel – an open-source AI gateway in Go](https://news.ycombinator.com/item?id=47849097)**

High-performance AI gateway written in Go - unified OpenAI-compatible API for OpenAI, Anthropic, Gemini, Groq, xAI &amp; Ollama. LiteLLM alternative with observability, guardrails &amp; streaming. ...

⬆️ 205 • 💬 74 • 2d ago • [GitHub](https://github.com/ENTERPILOT/GOModel/)

---

**[Our newsroom AI policy](https://news.ycombinator.com/item?id=47872452)**

How Ars Technica uses, and doesn't use, generative AI.

⬆️ 190 • 💬 125 • 22h ago • [Ars Technica](https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/)

---

**[MeshCore development team splits over trademark dispute and AI-generated code](https://news.ycombinator.com/item?id=47878117)**

Migrating to the new meshcore.io site

⬆️ 177 • 💬 100 • 11h ago • [blog.meshcore.io](https://blog.meshcore.io/2026/04/23/the-split)

---

**[Less human AI agents, please](https://news.ycombinator.com/item?id=47845429)**

Nial – Knowledge work and artificial intelligence.

⬆️ 158 • 💬 168 • 2d ago • [nial.se](https://nial.se/blog/less-human-ai-agents-please/)

---

**[Meta employees are up in arms over a mandatory program to train AI on their](https://news.ycombinator.com/item?id=47860961)**

Meta deploys keystroke-tracking software on US employees' computers, sparking privacy concerns and internal backlash.

⬆️ 115 • 💬 89 • 1d ago • [Business Insider](https://www.businessinsider.com/meta-new-ai-tool-tracks-staff-activity-sparks-concern-2026-4)

---

**[Top MAGA influencer revealed to be AI](https://news.ycombinator.com/item?id=47864808)**

According to her profile, she was a registered nurse with Jennifer Lawrence looks who offered red meat posts to lonely conservative men online.

⬆️ 96 • 💬 54 • 1d ago • [New York Post](https://nypost.com/2026/04/21/us-news/top-maga-influencer-emily-hart-revealed-to-be-ai-created-by-a-guy-in-india/)

---

---

## YouTube Videos: "ai"

**[Claude 5 – The New AI Era is Here! BYE, CHATGPT...](https://www.youtube.com/watch?v=qT4toLvs3n8)**

sponsored Build with Softr ...

📺 AI Master

👁️ 11K • 👍 261 • 💬 29 • ⏱️ 21:44 • 11h ago

---

**[Microsoft accidentally told the truth about AI](https://www.youtube.com/watch?v=4CIlTOnc6I8)**

Rogue researchers are telling the truth about AI Depth vs breadth: https://x.com/atmoio/status/2041557482217120182 Make ze ...

📺 Mo Bitar

👁️ 179K • 👍 13K • 💬 2K • ⏱️ 9:06 • 11h ago

---

**[I&#39;ve studied AI risk for 20 years. We&#39;re close to a disaster.](https://www.youtube.com/watch?v=fYRmnrDFPes)**

Roman Yampolskiy explains why superintelligence cannot be controlled, why the gap between AI capabilities and AI safety keeps ...

📺 Future of Life Institute

👁️ 7K • 👍 291 • 💬 73 • ⏱️ 19:17 • 13h ago

---

**[Day 1 of The 2026 AI Advantage Summit](https://www.youtube.com/watch?v=1N2TXfy5FAg)**

📺 Dean Graziosi

👁️ 406K • 👍 13K • 💬 90 • ⏱️ 4:19:20 • 6h ago

---

**[AI Has Officially Reached &#39;The Point of No Return&#39;…](https://www.youtube.com/watch?v=JxxJi0jMqi0)**

Smalls: Get 60% off your first order + FREE shipping & FREE treats for life at https://smalls.com/ICED Episode Link ...

📺 The Iced Coffee Hour Clips

👁️ 5K • 👍 71 • 💬 31 • ⏱️ 9:25 • 1d ago

---

**[Google Announces Gemini Enterprise Agent Platform: The Future of Agentic AI](https://www.youtube.com/watch?v=3wMwdzxIyN0)**

Google is in its agentic Gemini era. Hear from CEO of Google and Alphabet Sundar Pichai on how Google is customer zero of its ...

📺 Google Cloud

👁️ 42K • 👍 1K • ⏱️ 5:38 • 9h ago

---

**[I Tried Every FREE AI Video Generator in 2026 (use this)](https://www.youtube.com/watch?v=8RGrKD_HwrQ)**

I compared every Free AI Video Generator, use this Hey Friends :)) I've spent two weeks testing every single free video generator ...

📺 Skai Generated

👁️ 9K • ⏱️ 9:06 • 12h ago

---

**[The Dirty Secret Behind AI Data Centers No One Wants to Talk About](https://www.youtube.com/watch?v=Ij_qlW5x2-o)**

Ramageddon” is here: AI data centers are hoarding up to 70% of global DRAM, sending DDR5 prices soaring, distorting console ...

📺 Valuetainment

👁️ 211K • 👍 9K • 💬 544 • ⏱️ 12:41 • 2d ago

---

**[Reacting To My OWN AI VIDEOS..](https://www.youtube.com/watch?v=T0ZkvbZe9Dw)**

Today I reacted to my own AI videos! Make sure you watch the whole video to find out what happens. Merch: https://foltyn.shop/ ...

📺 Foltyn

👁️ 712K • 👍 27K • 💬 3K • ⏱️ 13:36 • 1d ago

---

**[The AI Bubble Has ALREADY Burst?](https://www.youtube.com/watch?v=_F-OyvxoQMg)**

Has the AI bubble already burst? Some analysts think so, but the effect will be slow -- quietly canceled data centers, rehiring ...

📺 Clownfish TV

👁️ 44K • 👍 3K • 💬 597 • ⏱️ 20:53 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 125,825 • ❤️ 906 • 22h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 0 • ❤️ 821 • 5m ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 717,811 • ❤️ 1,337 • 1h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 23,964 • ❤️ 674 • 1h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 1,888 • ❤️ 576 • 1d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 1,283,534 • ❤️ 713 • 3d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 578 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 350,262 • ❤️ 404 • 7d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 131,398 • ❤️ 336 • 1d ago

---

**[gemma-4-E4B-it-OBLITERATED](https://huggingface.co/OBLITERATUS/gemma-4-E4B-it-OBLITERATED)**

*OBLITERATUS*

Gemma 4 E4B OBLITERATED v3 is a text-generation model with 0% refusal and improved coding capabilities, designed for uncensored and unrestricted AI interactions. It features a modified architecture with 720 intact tensors, making it highly compatible with tools like Ollama and llama.cpp, and optimized for performance on consumer hardware.

`text-generation` `8.0B`

⬇️ 90,064 • ❤️ 484 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 74 • 💬 6 • ⭐ 18,117 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 18 • 💬 2 • ⭐ 4,351 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 9 • 💬 2 • ⭐ 6,293 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 25 • 💬 1 • ⭐ 20,896 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 48 • 💬 2 • ⭐ 52,574 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 64 • 💬 4 • ⭐ 646 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 77,882 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,854 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 61,003 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://huggingface.co/papers/2604.20796)**

*Inclusion AI, Tiwei Bie, Haoxing Chen et al. (18 authors)*

🏢 inclusionAI

LLaDA2.0-Uni is a unified discrete diffusion language model that integrates multimodal understanding and generation through a semantic discrete tokenizer, MoE-based backbone, and diffusion decoder, achieving performance comparable to specialized vision-language models while enabling efficient inference and high-fidelity image generation.

▲ 214 • 💬 2 • ⭐ 98 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.20796) • [💻 code](https://github.com/inclusionAI/LLaDA2.0-Uni)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 49.3k • 🔱 6.5k • 4m ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 44.9k • 🔱 2.3k • 5d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 39.0k • 🔱 7.9k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 33.8k • 🔱 3.7k • 8h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 9.8k • 🔱 2.1k • 1d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 6.0k • 🔱 1.0k • 19h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 11d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.8k • 🔱 462 • 15d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 4.3k • 🔱 379 • 3d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 3.5k • 🔱 223 • 1m ago

---

---

*Generated by PeekDeck - A glance is all you need*
