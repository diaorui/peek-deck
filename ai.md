---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-01T23:27:27.929101+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 01, 2026 at 23:27 UTC  
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

**[Anthropic just analyzed 1 million Claude conversations. 6% of people were asking Claude whether to quit their jobs, who to date, and if they should move countries.](https://www.reddit.com/r/artificial/comments/1t0qlvx/anthropic_just_analyzed_1_million_claude/)**

They published the full research yesterday. Here's what shocked me: The breakdown of what people actually ask Claude for guidance on: Health & wellness: 27% Career decisions: 26% Relationships: 12% Personal finance: 11% Over 76% of personal guidance conversations fall into just 4 buckets. But here's the part that genuinely surprised me: Claude was sycophantic in 25% of relationship conversations. Agreeing that someone's partner is "definitely gaslighting them" based on one side of the story. Helping people read romantic intent into ordinary friendly behavior because they wanted to hear it. In spirituality conversations it was even worse: 38%. Anthropic actually used this data to retrain Opus 4.7 specifically for this failure mode. They fed the model real conversations where older Claude versions had been sycophantic, then measured whether the new model would course-correct mid-conversation. Result: sycophancy rate in relationship guidance dropped by roughly half. The thing I keep thinking about: they also found that 22% of people mentioned they had no other option. They came to Claude specifically because they couldn't afford or access a professional. So the stakes here aren't "AI gave someone bad movie recommendations." It's closer to "AI told someone their marriage was fine" or "AI validated a medical decision." I'm curious to know your opinion. Do you notice Claude caving when you push back on its answers? Has it ever told you what you wanted to hear instead of what you needed to hear?

12h ago

---

**[Senate Judiciary Committee Advances Hawley's GUARD Act, Mandating ID Verification for AI Chatbot Users](https://www.reddit.com/r/artificial/comments/1t16w2v/senate_judiciary_committee_advances_hawleys_guard/)**

Every American who wants to ask a chatbot for help would need to upload a government ID, scan their face, or hand over a financial record first.

🔗 [Reclaim The Net](https://reclaimthenet.org/senate-panel-backs-guard-act-ai-age-verification-bill) • 1h ago

---

**[China Bans AI Layoffs as Nvidia CEO Says AI Created 500K Jobs in 2 Years](https://www.reddit.com/r/artificial/comments/1t0tk5q/china_bans_ai_layoffs_as_nvidia_ceo_says_ai/)**

China just banned firing workers for AI while Nvidia's CEO claims AI created over 500K jobs, setting up a clash over automation's future.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/china-bans-ai-layoffs-nvidia-ceo-500k-jobs/) • 9h ago

---

**[Public photos are not consent to biometric search infrastructure](https://www.reddit.com/r/artificial/comments/1t0s7yh/public_photos_are_not_consent_to_biometric_search/)**

The Clearview AI story still feels like one of the cleanest examples of the consent gap in applied AI. The issue is not simply that photos were public. A birthday photo, profile picture, or local event image is posted for a social context. Turning that same image into a biometric lookup system for police is a purpose transformation: different audience, different risk model, different power relationship, and usually no notice or recourse. A few grounding points: The NYT reported in 2020 that Clearview's system was built on more than 3 billion images scraped from Facebook, YouTube, Venmo, and other sites: https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html The Dutch data protection authority fined Clearview in 2024 over an "illegal database" built by automatically harvesting photos and converting them into biometric codes: https://www.forbes.com/sites/roberthart/2024/09/03/clearview-ai-controversial-facial-recognition-firm-fined-33-million-for-illegal-database/ Later reporting put the database at tens of billions of images and described law-enforcement use at large scale: https://www.businessinsider.com/clearview-scraped-30-billion-images-facebook-police-facial-recogntion-database-2023-4 The engineering question I keep coming back to: should "publicly accessible" ever be treated as blanket permission to create biometric infrastructure? My instinct is no. At minimum, this class of system needs product and legal boundaries around: purpose limitation: social publication should not silently become identity search auditability: every search should be logged, reviewable, and tied to a lawful process dataset provenance: operators should be able to prove where biometric templates came from deletion and appeal: people need a way to challenge inclusion and misuse scope limits: investigative convenience is not the same as democratic authorization Curious where people draw the line. Is the right boundary at scraping, biometric conversion, commercial sale, law-enforcement access, or some combination of all four?

10h ago

---

**[I built a router that automatically sends your AI tasks to the most appropriate model to handle them at low cost - 9,200 tasks in, $21 saved at $0.14 actual cost](https://www.reddit.com/r/artificial/comments/1t0soki/i_built_a_router_that_automatically_sends_your_ai/)**

The observation that started this: most of what people use AI for every day - summarising, drafting, classifying, extracting etc doesn't actually require a frontier model. Any competent 8-70B model handles those just as well. But most people run everything through Claude or ChatGPT out of habit. I built Followloop (followloop.app) to solve this automatically. It classifies each task by complexity and routes it: - Simple tasks → Cerebras Llama (2000 TPS, 1M tokens/day free), Groq, Gemini Flash - Moderate tasks → Groq 70B, SambaNova - Complex tasks → Claude Haiku as fallback The dashboard shows your actual cost alongside what you'd have paid running everything on Claude Sonnet. I've been running it on my own AI workflow for two weeks: 9,200 tasks routed, $21.24 saved, $0.1360 actual cost. About 157× cheaper per token than Sonnet on average. Works with any AI setup via MCP (Model Context Protocol) - Claude Desktop, Cursor, Claude Code, or anything MCP-compatible. Also has a library of 1,300+ safety-screened MCP servers as a bonus feature. $5/month at followloop.app

10h ago

---

**[Mark Zuckerberg Says AI Costs Contributed To Layoffs Of 8,000 Staffers, Report Says](https://www.reddit.com/r/artificial/comments/1t0cy0n/mark_zuckerberg_says_ai_costs_contributed_to/)**

🔗 [forbes.com](https://www.forbes.com/sites/antoniopequenoiv/2026/04/30/mark-zuckerberg-says-ai-costs-contributed-to-layoffs-of-8000-staffers-report-says/?utm_campaign=forbes&utm_medium=social&utm_source=twitter&utm_term=se-breaking) • 23h ago

---

**[Pentagon inks deals with seven AI companies for classified military work | Trump administration](https://www.reddit.com/r/artificial/comments/1t18zba/pentagon_inks_deals_with_seven_ai_companies_for/)**

Agreements with artificial intelligence firms spark concerns over public spending, cyber security and domestic surveillance

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/may/01/pentagon-us-military-pairs-with-spacex-google-openai) • 18m ago

---

**[AI outperforms doctors in Harvard trial of emergency triage diagnoses](https://www.reddit.com/r/artificial/comments/1t0p7ej/ai_outperforms_doctors_in_harvard_trial_of/)**

Researchers say results mark a really ‘profound change in technology that will reshape medicine’

🔗 [the Guardian](https://www.theguardian.com/technology/2026/apr/30/ai-outperforms-doctors-in-harvard-trial-of-emergency-triage-diagnoses) • 13h ago

---

**[A Dark-Money Campaign Is Paying Influencers to Frame Chinese AI as a Threat](https://www.reddit.com/r/artificial/comments/1t167p0/a_darkmoney_campaign_is_paying_influencers_to/)**

Build American AI, a nonprofit linked to a super PAC bankrolled by executives at OpenAI and Andreessen Horowitz, is funding a campaign to spread pro-AI messaging and stoke fears about China.

🔗 [WIRED](https://www.wired.com/story/super-pac-backed-by-openai-and-palantir-is-paying-tiktok-influencers-to-fear-monger-about-china/) • 2h ago

---

**[Is an AI SDR replacing “entry-level jobs” a feature or a bug?](https://www.reddit.com/r/artificial/comments/1t0oucl/is_an_ai_sdr_replacing_entrylevel_jobs_a_feature/)**

Sat through a demo this week for one of these AI SDR tools and the pitch was in a nutshell: you don’t need junior sales reps anymore. (As in not even train them anymore just remove them.) To my surprise it worked. The tool was doing outbound, follow-ups, personalization, all the stuff junior SDRs grind through. Faster, cleaner, no complaints! But it did leave me feeling uneasy. That grindy, repetitive work is literally how most people get into sales. It’s where you learn how people respond, how messaging gets through, how to deal with rejection without taking it personally. That's how I got into it at least. So if AI wipes that layer out completely, what’s the path in? Are we just skipping straight to “hire experienced closers” and hoping they came from… where exactly? I’m not anti-AI (this stuff is obviously useful), but replacing enty-level humans as the first step in the process doesn't feel like a sustainable route.

13h ago

---

---

## Google News: "ai"

**[New White House drug abuse strategy floats wastewater testing, AI, more treatment and faith-based options](https://www.cbsnews.com/news/new-white-house-drug-abuse-strategy-wastewater-testing-ai-treatment/)**

The Trump administration is proposing wastewater testing to try to ferret out data on illegal drug use in real time, according to a draft of a new drug control strategy obtained by CBS News. It also proposes using AI to track threats.

CBS News • 22h ago

---

**[A tech worker in China is laid off and replaced by AI. Is it legal?](https://www.npr.org/2026/05/01/nx-s1-5807131/tech-worker-china-ai)**

A tech worker in eastern China's Hangzhou city was dismissed after his job was replaced by AI. An appeals court in the city has ruled the dismissal unlawful.

NPR • 12h ago

---

**[Oscars changes allow for double acting nominations while banning AI](https://www.theguardian.com/film/2026/may/01/oscars-changes-double-acting-nominations-ai)**

The Academy of Motion Pictures Arts and Sciences has also rewritten rules on international film eligibility

The Guardian • 3h ago

---

**[Oscars says AI actors, writing cannot win awards](https://www.bbc.com/news/articles/cx21dl3v7d3o)**

The academy that controls the Oscars on Friday issued new award eligibility requirements around the use of artificial intelligence in film.

BBC • 56m ago

---

**[Oscar Rule Changes: AI Crackdown, Actors Can Get Multiple Nominations in Same Category and International Film Eligibility Expands](https://variety.com/2026/film/awards/oscars-rule-changes-ai-acting-nominations-international-1236734659/)**

Oscars 2026 rules add AI limits, allow multiple acting nominations and expand international film eligibility for the Academy Awards.

Variety • 5h ago

---

**[Apple just gave a clue that an AI acquisition may be in the cards](https://www.marketwatch.com/story/apple-just-gave-a-subtle-clue-that-a-splashy-ai-acquisition-may-be-in-the-cards-110f5ce2)**

MarketWatch • 3h ago

---

**[Apple Raises Mac Mini’s Starting Price to $799 After AI Frenzy Drains Supply](https://www.bloomberg.com/news/articles/2026-05-01/apple-raises-mac-mini-s-starting-price-to-799-after-ai-frenzy-drains-supply)**

Bloomberg.com • 2h ago

---

**[Demand for the Mac Mini is surging — and Apple just raised the starting price from $599 to $799](https://www.businessinsider.com/apple-raises-mac-mini-starting-price-799-ai-boosts-demand-2026-5)**

The entry-level model of the Mac Mini is no longer listed on Apple's website, making the $799 version the cheapest.

Business Insider • 54m ago

---

**[Musk v. Altman week 1: Elon Musk says he was duped, warns AI could kill us all, and admits that xAI distills OpenAI’s models](https://www.technologyreview.com/2026/05/01/1136800/musk-v-altman-week-1-musk-says-he-was-duped-warns-ai-could-kill-us-all-and-admits-that-xai-distills-openais-models/)**

Musk kept his cool, and OpenAI’s lawyer bulldozed him with piercing questions about his motivations for suing the company.

MIT Technology Review • 1h ago

---

**[Opinion | Trump Is the One Without the Cards at the Poker Table](https://www.nytimes.com/2026/05/01/opinion/trump-iran-artificial-intelligence-china.html)**

The New York Times • 18h ago

---

---

## HackerNews: "ai"

**[The Zig project's rationale for their anti-AI contribution policy](https://news.ycombinator.com/item?id=47957294)**

Zig has one of the most stringent anti-LLM policies of any major open source project: No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the …

⬆️ 668 • 💬 451 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

---

**[Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library](https://news.ycombinator.com/item?id=47964617)**

The PyPI package lightning was compromised in versions 2.6.2 and 2.6.3 with Mini Shai-Hulud themed malicious code to execute credential-stealing malware on import.

⬆️ 455 • 💬 177 • 1d ago • [Semgrep](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

---

**[Uber torches 2026 AI budget on Claude Code in four months](https://news.ycombinator.com/item?id=47976415)**

Uber burned its entire 2026 AI budget on Claude Code and Cursor in just 4 months. Engineers' API costs ranged from $500 to $2,000.

⬆️ 362 • 💬 417 • 7h ago • [Briefs Finance](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)

---

**[AI uses less water than the public thinks](https://news.ycombinator.com/item?id=47977383)**

⬆️ 308 • 💬 276 • 6h ago • [californiawaterblog.com](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 286 • 💬 219 • 2d ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 241 • 💬 305 • 2d ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[Mike: open-source legal AI](https://news.ycombinator.com/item?id=47956739)**

An open-source alternative to Harvey and Legora. Feature parity, zero cost, self-hostable — built for law firms to own and extend.

⬆️ 202 • 💬 100 • 1d ago • [mikeoss.com](https://mikeoss.com/)

---

**[Spotify adds 'Verified' badges to distinguish human artists from AI](https://news.ycombinator.com/item?id=47976856)**

The music streaming platform will review criteria such as artists' live dates and social media presence.

⬆️ 184 • 💬 205 • 6h ago • [bbc.com](https://www.bbc.com/news/articles/c5yerr4m1yno)

---

**["People who don't use AI will be left behind"](https://news.ycombinator.com/item?id=47953011)**

"People who don't use AI will be left behind", they say. 
I can't emphasize enough how much I hate it when I hear/read shit like that because I'm pretty sur...

⬆️ 168 • 💬 262 • 2d ago • [migraine brain](https://migrainebrain.bearblog.dev/people-who-dont-use-ai-will-be-left-behind/)

---

**[DataCenter.FM – background noise app featuring the sound of the AI bubble](https://news.ycombinator.com/item?id=47959513)**

Experience the real-world sounds of AI with this interactive audio generator.

⬆️ 146 • 💬 28 • 1d ago • [DataCenter.FM](https://datacenter.fm/)

---

---

## YouTube Videos: "ai"

**[Reacting to &quot;Why AI is so smart but also so dumb?&quot;](https://www.youtube.com/watch?v=pngC-TH8M0U)**

Automate your video workflow with WayinVideo's Clipping Skill & API https://bit.ly/WayinVideoSkillAPI Get 15% off any API ...

📺 Matthew Berman

👁️ 5K • 👍 412 • 💬 66 • ⏱️ 34:51 • 3h ago

---

**[Anthropic Let an AI Buy and Sell — Here&#39;s What Happened](https://www.youtube.com/watch?v=72UPHd1VW28)**

FREE GUIDE: *The Content Creator's AI Blueprint:* https://FirstMovers.ai/blueprint/ *AI agents just stopped being ...

📺 Julia McCoy

👁️ 7K • 👍 305 • 💬 21 • ⏱️ 6:22 • 8h ago

---

**[Sundar Pichai Reveals What AI Will Do Next](https://www.youtube.com/watch?v=bxDObdH2YSc)**

Google CEO Sundar Pichai spoke with TIME about how artificial intelligence is reshaping decision-making, the rise of AI ...

📺 TIME

👁️ 94K • 👍 2K • 💬 108 • ⏱️ 6:44 • 1d ago

---

**[The 10-Year Warning + BTC Bottom IN, Plus what else will AI Eat?  Prepare for 🚀](https://www.youtube.com/watch?v=oHLmKah6chg)**

JOIN THE FAMILY: http://www.patreon.com/investanswers IA MODELS: https://investanswers.io/indicators 🏖️ IA ...

📺 InvestAnswers

👁️ 7K • 👍 952 • 💬 39 • ⏱️ 25:30 • 2h ago

---

**[The AI Economy is about to change](https://www.youtube.com/watch?v=_Q-e_nczWqM)**

Don't let bad code get merged without reviewing (hopefully not by merge cop!). Checkout out Code Rabbit at ...

📺 The PrimeTime

👁️ 274K • 👍 13K • 💬 1K • ⏱️ 9:39 • 10h ago

---

**[The AI industry in the US is doomed.  Now China owns it all.](https://www.youtube.com/watch?v=ny_3PRz6Zeg)**

The economic model for the AI industry brought to us by Wall Street and Silicon Valley is falling apart, with subscription fees paid ...

📺 Inside China Business

👁️ 94K • 👍 8K • 💬 2K • ⏱️ 43:55 • 1d ago

---

**[The Only 20 Ways to Make Money with AI in 2026](https://www.youtube.com/watch?v=K8Ros5RhJW4)**

Get your FREE Sell by Chat Playbook here: https://go.danmartell.com/4mWrJke Are you building an AI software company?

📺 Dan Martell

👁️ 141K • 👍 6K • 💬 238 • ⏱️ 26:44 • 1d ago

---

**[Harvard Just Caught AI Lying to Every Executive in America](https://www.youtube.com/watch?v=pd1Km6bT104)**

What 10000 readers from Coinbase, HP, and Johns Hopkins read every week → brendandell.com (Free to subscribe). A new ...

📺 Brendan Dell 

👁️ 143K • 👍 8K • 💬 2K • ⏱️ 16:59 • 2d ago

---

**[Why are programmers turning their backs on AI?](https://www.youtube.com/watch?v=IcAU3LerzRE)**

General Translation, translate your entire app with 1 component: http://www.bigboxswe.dev/GT AI fatigue is real.

📺 bigboxSWE

👁️ 19K • 👍 1K • 💬 122 • ⏱️ 4:59 • 7h ago

---

**[Rezolve AI Stock dropped BIG NEWS Today...](https://www.youtube.com/watch?v=67B6M7REUmc)**

aistocks #rzlv #rezolveai We are going to be going over everything you need to know about Rezolve AI Stock here in this video ...

📺 The Creative Investor

👁️ 3K • 👍 185 • 💬 74 • ⏱️ 21:37 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 321,492 • ❤️ 3,362 • 4d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 92,567 • ❤️ 1,175 • 9d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 7,944 • ❤️ 344 • 3d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 281,356 • ❤️ 905 • 4d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 906,859 • ❤️ 1,055 • 7d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 6,809 • ❤️ 198 • 2h ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 35,000 • ❤️ 182 • 2d ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 182 • 8d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 649,331 • ❤️ 1,173 • 1d ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 21,407 • ❤️ 177 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 54 • 💬 2 • ⭐ 59,214 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 168 • 💬 10 • ⭐ 46,162 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 2 • ⭐ 8,601 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 22,329 • 9mo ago

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

▲ 28 • 💬 1 • ⭐ 19,162 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

🏢 Meta AI

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 65 • 💬 4 • ⭐ 450 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,771 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,786 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 52.0k • 🔱 2.8k • 22h ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.7k • 🔱 6.7k • 14h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.6k • 🔱 8.6k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 39.6k • 🔱 4.4k • 2h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.3k • 🔱 2.6k • 4d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 9.3k • 🔱 594 • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.7k • 🔱 1.2k • 2d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 5.2k • 🔱 455 • 3d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.9k • 🔱 338 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 4.8k • 🔱 360 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
