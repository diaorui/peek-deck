---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-02T04:41:18.370017+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 02, 2026 at 04:41 UTC  
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

**[Senate Judiciary Committee Advances Hawley's GUARD Act, Mandating ID Verification for AI Chatbot Users](https://www.reddit.com/r/artificial/comments/1t16w2v/senate_judiciary_committee_advances_hawleys_guard/)**

Every American who wants to ask a chatbot for help would need to upload a government ID, scan their face, or hand over a financial record first.

🔗 [Reclaim The Net](https://reclaimthenet.org/senate-panel-backs-guard-act-ai-age-verification-bill) • 6h ago

---

**[Anthropic just analyzed 1 million Claude conversations. 6% of people were asking Claude whether to quit their jobs, who to date, and if they should move countries.](https://www.reddit.com/r/artificial/comments/1t0qlvx/anthropic_just_analyzed_1_million_claude/)**

They published the full research yesterday. Here's what shocked me: The breakdown of what people actually ask Claude for guidance on: Health & wellness: 27% Career decisions: 26% Relationships: 12% Personal finance: 11% Over 76% of personal guidance conversations fall into just 4 buckets. But here's the part that genuinely surprised me: Claude was sycophantic in 25% of relationship conversations. Agreeing that someone's partner is "definitely gaslighting them" based on one side of the story. Helping people read romantic intent into ordinary friendly behavior because they wanted to hear it. In spirituality conversations it was even worse: 38%. Anthropic actually used this data to retrain Opus 4.7 specifically for this failure mode. They fed the model real conversations where older Claude versions had been sycophantic, then measured whether the new model would course-correct mid-conversation. Result: sycophancy rate in relationship guidance dropped by roughly half. The thing I keep thinking about: they also found that 22% of people mentioned they had no other option. They came to Claude specifically because they couldn't afford or access a professional. So the stakes here aren't "AI gave someone bad movie recommendations." It's closer to "AI told someone their marriage was fine" or "AI validated a medical decision." I'm curious to know your opinion. Do you notice Claude caving when you push back on its answers? Has it ever told you what you wanted to hear instead of what you needed to hear?

17h ago

---

**[China Bans AI Layoffs as Nvidia CEO Says AI Created 500K Jobs in 2 Years](https://www.reddit.com/r/artificial/comments/1t0tk5q/china_bans_ai_layoffs_as_nvidia_ceo_says_ai/)**

China just banned firing workers for AI while Nvidia's CEO claims AI created over 500K jobs, setting up a clash over automation's future.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/china-bans-ai-layoffs-nvidia-ceo-500k-jobs/) • 15h ago

---

**[Pentagon inks deals with seven AI companies for classified military work | Trump administration](https://www.reddit.com/r/artificial/comments/1t18zba/pentagon_inks_deals_with_seven_ai_companies_for/)**

Agreements with artificial intelligence firms spark concerns over public spending, cyber security and domestic surveillance

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/may/01/pentagon-us-military-pairs-with-spacex-google-openai) • 5h ago

---

**[Public photos are not consent to biometric search infrastructure](https://www.reddit.com/r/artificial/comments/1t0s7yh/public_photos_are_not_consent_to_biometric_search/)**

The Clearview AI story still feels like one of the cleanest examples of the consent gap in applied AI. The issue is not simply that photos were public. A birthday photo, profile picture, or local event image is posted for a social context. Turning that same image into a biometric lookup system for police is a purpose transformation: different audience, different risk model, different power relationship, and usually no notice or recourse. A few grounding points: The NYT reported in 2020 that Clearview's system was built on more than 3 billion images scraped from Facebook, YouTube, Venmo, and other sites: https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html The Dutch data protection authority fined Clearview in 2024 over an "illegal database" built by automatically harvesting photos and converting them into biometric codes: https://www.forbes.com/sites/roberthart/2024/09/03/clearview-ai-controversial-facial-recognition-firm-fined-33-million-for-illegal-database/ Later reporting put the database at tens of billions of images and described law-enforcement use at large scale: https://www.businessinsider.com/clearview-scraped-30-billion-images-facebook-police-facial-recogntion-database-2023-4 The engineering question I keep coming back to: should "publicly accessible" ever be treated as blanket permission to create biometric infrastructure? My instinct is no. At minimum, this class of system needs product and legal boundaries around: purpose limitation: social publication should not silently become identity search auditability: every search should be logged, reviewable, and tied to a lawful process dataset provenance: operators should be able to prove where biometric templates came from deletion and appeal: people need a way to challenge inclusion and misuse scope limits: investigative convenience is not the same as democratic authorization Curious where people draw the line. Is the right boundary at scraping, biometric conversion, commercial sale, law-enforcement access, or some combination of all four?

16h ago

---

**[I built a router that automatically sends your AI tasks to the most appropriate model to handle them at low cost - 9,200 tasks in, $21 saved at $0.14 actual cost](https://www.reddit.com/r/artificial/comments/1t0soki/i_built_a_router_that_automatically_sends_your_ai/)**

The observation that started this: most of what people use AI for every day - summarising, drafting, classifying, extracting etc doesn't actually require a frontier model. Any competent 8-70B model handles those just as well. But most people run everything through Claude or ChatGPT out of habit. I built Followloop (followloop.app) to solve this automatically. It classifies each task by complexity and routes it: - Simple tasks → Cerebras Llama (2000 TPS, 1M tokens/day free), Groq, Gemini Flash - Moderate tasks → Groq 70B, SambaNova - Complex tasks → Claude Haiku as fallback The dashboard shows your actual cost alongside what you'd have paid running everything on Claude Sonnet. I've been running it on my own AI workflow for two weeks: 9,200 tasks routed, $21.24 saved, $0.1360 actual cost. About 157× cheaper per token than Sonnet on average. Works with any AI setup via MCP (Model Context Protocol) - Claude Desktop, Cursor, Claude Code, or anything MCP-compatible. Also has a library of 1,300+ safety-screened MCP servers as a bonus feature. $5/month at followloop.app

15h ago

---

**[I Cut Claude API Costs by 50% Using This Self Modifying Agentic System](https://www.reddit.com/r/artificial/comments/1t1fjek/i_cut_claude_api_costs_by_50_using_this_self/)**

I've been developing a self-modifying Al agent system that effectively cuts my Claude API usage in half, Claude thinks and then I basically just copy/paste Claude's instructions for the agents to work on. Come back in 6 hours and it's done for free on local hardware. I'II explain precisely how it works below. Repo: https://github.com/ninjahawk/hollow-agentOS What it is: A system that runs 24/7 on my RTX 5070 gaming PC (but can run on CPU on any laptops as well, just slower) which I use to offload tasks that can be figured out over X amount of time. It becomes a time issue, not a model issue. Using a loop of iterative testing and self improvement, I've found Qwen 3.5: 9b running over an amount of time to be just as useful as Claude code. It will propose code, make it, test it, see if it worked, edit it, repeat indefinitely. How it’s self modifying: The system runs 24/7, when it doesn't have a task given to it, it will review the files which make it run, propose improvements, and autonomously implement those improvements or self-extensions within a sandboxed environment after it has a 2/3 majority vote by all agents. Self-modification is customizable to an extent, maybe you want a different type of the system for yourself, just make that the constant anchor state and they’ll approach your end goal constantly in their own time. By design everyone who uses this will have a different version most likely since the changes are dependent on what the specific agents want to accomplish, no two will be the same. Agents are created based on a set of constraints which do not produce the same agent twice (at least that I’ve seen, some behaviors are universal however). HOLLOW solves two key problems: A. It enables you to truly develop without developing. B. You allow it to truly develop itself as a system over time, learning and adapting without human interaction (unless you wanted to) Huge thank you for the 74 Github stars and hundreds of testers over this past month, the support has truly shocked me. This is a work in progress but if anyone has any feedback, criticism, or success you'd like to share, please comment below!

25m ago

---

**[Mark Zuckerberg Says AI Costs Contributed To Layoffs Of 8,000 Staffers, Report Says](https://www.reddit.com/r/artificial/comments/1t0cy0n/mark_zuckerberg_says_ai_costs_contributed_to/)**

🔗 [forbes.com](https://www.forbes.com/sites/antoniopequenoiv/2026/04/30/mark-zuckerberg-says-ai-costs-contributed-to-layoffs-of-8000-staffers-report-says/?utm_campaign=forbes&utm_medium=social&utm_source=twitter&utm_term=se-breaking) • 1d ago

---

**[AI outperforms doctors in Harvard trial of emergency triage diagnoses](https://www.reddit.com/r/artificial/comments/1t0p7ej/ai_outperforms_doctors_in_harvard_trial_of/)**

Researchers say results mark a really ‘profound change in technology that will reshape medicine’

🔗 [the Guardian](https://www.theguardian.com/technology/2026/apr/30/ai-outperforms-doctors-in-harvard-trial-of-emergency-triage-diagnoses) • 18h ago

---

**[What to build while we still have access to cheap AI?](https://www.reddit.com/r/artificial/comments/1t1d0oe/what_to_build_while_we_still_have_access_to_cheap/)**

AI companies are subsidizing access the same way Uber subsidized rides and AWS subsidized compute in the early days - burning cash to grab market share. You're getting GPT-4 and Claude Opus level intelligence at a fraction of what it actually costs to run. That won't last. When unit economics have to work, prices go up and the cheap development era ends. So the question is: what can you build right now, while the cost of intelligence is artificially low, that becomes durable and defensible once the subsidy disappears? Edit: I copied this from my brainstorming session with AI

2h ago

---

---

## Google News: "ai"

**[Oscars bans AI actors, writing from awards](https://www.bbc.com/news/articles/cx21dl3v7d3o)**

The academy that controls the Oscars on Friday issued new award eligibility requirements around the use of artificial intelligence in film.

BBC • 6h ago

---

**[Oscars changes allow for double acting nominations while banning AI](https://www.theguardian.com/film/2026/may/01/oscars-changes-double-acting-nominations-ai)**

The Academy of Motion Pictures Arts and Sciences has also rewritten rules on international film eligibility

The Guardian • 8h ago

---

**[New Oscars rules: No AI actors, human-written scripts only](https://www.dw.com/en/new-oscars-rules-exclude-ai-performers-require-scripts-written-by-human/a-77016539)**

AI performers will not qualify for Oscars under new Academy rules that also overhaul the international film category and acting nominations.

DW.com • 33m ago

---

**[So, About That AI Bubble](https://www.theatlantic.com/economy/2026/05/ai-bubble-revenue-anthropic/687022/)**

Thanks to the rise of Claude Code and other AI agents, revenues are finally catching up to the hype.

The Atlantic • 17h ago

---

**[Paranoid parenting in the age of AI](https://www.ft.com/content/0de94232-0e64-447f-ab5f-f46d0fdabd8c)**

It’s an illusion to think we can robot-proof our kids’ education choices

Financial Times • 40m ago

---

**[Why Investors Should Be Wary of AI Job Cutters](https://www.bloomberg.com/news/newsletters/2026-05-02/ai-is-coming-for-your-job-and-your-mind)**

Bloomberg.com • 40m ago

---

**[Building trades unions emerge as a key ally of tech giants in push for AI data centers](https://www.bostonglobe.com/2026/05/02/nation/building-trades-unions-emerge-as-a-key-ally-of-tech-giants-ai-data-centers/)**

Unionized workers are employed on a huge number of massive data center projects.

The Boston Globe • 9m ago

---

**[Caitlin Clark raises eyebrows with comment on team's AI post that showed her with a distorted hand](https://www.foxnews.com/outkick-sports/caitlin-clark-raises-eyebrows-comment-teams-ai-post-showed-distorted-hand)**

Caitlin Clark left a comment appearing to mock a bad AI image of her hand on the Indiana Fever's Instagram, sparking funny fan reactions online.

Fox News • 5h ago

---

**[Opinion | Trump Is the One Without the Cards at the Poker Table](https://www.nytimes.com/2026/05/01/opinion/trump-iran-artificial-intelligence-china.html)**

The New York Times • 23h ago

---

**[Top AI companies agree to work with Pentagon on secret data](https://www.washingtonpost.com/technology/2026/05/01/pentagon-ai-deals-microsoft-amazon-google-classified-military/)**

The Pentagon has signed agreements with leading AI firms, including Microsoft, Amazon and Google, advancing military capabilities amid a dispute over safeguards.

The Washington Post • 3h ago

---

---

## HackerNews: "ai"

**[The Zig project's rationale for their anti-AI contribution policy](https://news.ycombinator.com/item?id=47957294)**

Zig has one of the most stringent anti-LLM policies of any major open source project: No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the …

⬆️ 669 • 💬 453 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

---

**[Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library](https://news.ycombinator.com/item?id=47964617)**

The PyPI package lightning was compromised in versions 2.6.2 and 2.6.3 with Mini Shai-Hulud themed malicious code to execute credential-stealing malware on import.

⬆️ 457 • 💬 177 • 1d ago • [Semgrep](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

---

**[Uber torches 2026 AI budget on Claude Code in four months](https://news.ycombinator.com/item?id=47976415)**

Uber burned its entire 2026 AI budget on Claude Code and Cursor in just 4 months. Engineers' API costs ranged from $500 to $2,000.

⬆️ 373 • 💬 436 • 12h ago • [Briefs Finance](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)

---

**[AI uses less water than the public thinks](https://news.ycombinator.com/item?id=47977383)**

⬆️ 362 • 💬 324 • 11h ago • [californiawaterblog.com](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 286 • 💬 219 • 2d ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 241 • 💬 305 • 2d ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[Spotify adds 'Verified' badges to distinguish human artists from AI](https://news.ycombinator.com/item?id=47976856)**

The music streaming platform will review criteria such as artists' live dates and social media presence.

⬆️ 226 • 💬 249 • 11h ago • [bbc.com](https://www.bbc.com/news/articles/c5yerr4m1yno)

---

**[Mike: open-source legal AI](https://news.ycombinator.com/item?id=47956739)**

An open-source alternative to Harvey and Legora. Feature parity, zero cost, self-hostable — built for law firms to own and extend.

⬆️ 203 • 💬 101 • 2d ago • [mikeoss.com](https://mikeoss.com/)

---

**["People who don't use AI will be left behind"](https://news.ycombinator.com/item?id=47953011)**

"People who don't use AI will be left behind", they say. 
I can't emphasize enough how much I hate it when I hear/read shit like that because I'm pretty sur...

⬆️ 168 • 💬 263 • 2d ago • [migraine brain](https://migrainebrain.bearblog.dev/people-who-dont-use-ai-will-be-left-behind/)

---

**[DataCenter.FM – background noise app featuring the sound of the AI bubble](https://news.ycombinator.com/item?id=47959513)**

Experience the real-world sounds of AI with this interactive audio generator.

⬆️ 146 • 💬 28 • 1d ago • [DataCenter.FM](https://datacenter.fm/)

---

---

## YouTube Videos: "ai"

**[AI Expert Tells Bernie: AI Could WIPE OUT CIVILIZATION](https://www.youtube.com/watch?v=NzNo6glA48Y)**

Senator Bernie Sanders is the senior senator from Vermont. He is the longest-serving independent in U.S. congressional history ...

📺 Senator Bernie Sanders

👁️ 9K • 👍 852 • 💬 191 • ⏱️ 2:58 • 16h ago

---

**[Sundar Pichai Reveals What AI Will Do Next](https://www.youtube.com/watch?v=bxDObdH2YSc)**

Google CEO Sundar Pichai spoke with TIME about how artificial intelligence is reshaping decision-making, the rise of AI ...

📺 TIME

👁️ 108K • 👍 2K • 💬 116 • ⏱️ 6:44 • 1d ago

---

**[Harvard Just Caught AI Lying to Every Executive in America](https://www.youtube.com/watch?v=pd1Km6bT104)**

What 10000 readers from Coinbase, HP, and Johns Hopkins read every week → brendandell.com (Free to subscribe). A new ...

📺 Brendan Dell 

👁️ 158K • 👍 8K • 💬 2K • ⏱️ 16:59 • 2d ago

---

**[AI Shows America Without Democrats](https://www.youtube.com/watch?v=Jn-7ZuhoAEc)**

We asked Artificial Intelligence what America would look like without Democrats.

📺 The Babylon Bee

👁️ 131K • 👍 10K • 💬 1K • ⏱️ 1:09 • 2d ago

---

**[The AI Economy is about to change](https://www.youtube.com/watch?v=_Q-e_nczWqM)**

Don't let bad code get merged without reviewing (hopefully not by merge cop!). Checkout out Code Rabbit at ...

📺 The PrimeTime

👁️ 360K • 👍 16K • 💬 1K • ⏱️ 9:39 • 15h ago

---

**[I BLEW UP a YouTube Channel in 24 Hours with AI](https://www.youtube.com/watch?v=za2VyvLl5T0)**

In this video, I build a YouTube channel from scratch and take it viral in 24 hours. Showing every step from creating the niche, ...

📺 Jack Craig

👁️ 13K • 👍 1K • 💬 204 • ⏱️ 27:07 • 12h ago

---

**[AI Is REPLACING YOU and the MARKET LOVES IT](https://www.youtube.com/watch?v=hsjEckj9kO8)**

The AI revolution isn't coming; it's already here, and it's moving faster than anyone in Washington or on Wall Street wants to admit.

📺 Anthony Scaramucci

👁️ 30K • 👍 1K • 💬 209 • ⏱️ 27:44 • 2d ago

---

**[The Only 20 Ways to Make Money with AI in 2026](https://www.youtube.com/watch?v=K8Ros5RhJW4)**

Get your FREE Sell by Chat Playbook here: https://go.danmartell.com/4mWrJke Are you building an AI software company?

📺 Dan Martell

👁️ 159K • 👍 7K • 💬 265 • ⏱️ 26:44 • 1d ago

---

**[Google Just Stunned the AI Industry With a Physical Body for Gemini](https://www.youtube.com/watch?v=f7UhkOMhxss)**

Google is drawing significant interest with a new concept that brings its Gemini AI into a physical form, moving beyond traditional ...

📺 Carros Show

👁️ 6K • 👍 182 • 💬 25 • ⏱️ 8:51 • 1d ago

---

**[This Will Make Millionaires (A.I Stack)](https://www.youtube.com/watch?v=qXdWR1vC1QQ)**

Most people think AI is just about Nvidia… That's the mistake. AI isn't one company — it's an entire data center stack. And if you ...

📺 Wallstreet Trapper

👁️ 29K • 👍 2K • 💬 294 • ⏱️ 11:40 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 321,492 • ❤️ 3,374 • 4d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 92,567 • ❤️ 1,178 • 9d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 7,944 • ❤️ 351 • 3d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 906,859 • ❤️ 1,056 • 8d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 281,356 • ❤️ 909 • 4d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 6,809 • ❤️ 200 • 6h ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 187 • 8d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 35,000 • ❤️ 186 • 3d ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 21,407 • ❤️ 181 • 2d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 5,690 • ❤️ 175 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 54 • 💬 2 • ⭐ 60,119 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 168 • 💬 10 • ⭐ 46,199 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 2 • ⭐ 8,651 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 22,380 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,499 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,499 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 19,217 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,786 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

🏢 Meta AI

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 65 • 💬 4 • ⭐ 471 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,786 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 52.1k • 🔱 2.8k • 1d ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.7k • 🔱 6.7k • 50m ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.7k • 🔱 8.6k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 40.0k • 🔱 4.4k • 7h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.4k • 🔱 2.6k • 4d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 9.3k • 🔱 602 • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.7k • 🔱 1.2k • 2d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 5.2k • 🔱 458 • 3d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.9k • 🔱 339 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 4.8k • 🔱 361 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
