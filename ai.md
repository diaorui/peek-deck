---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-01T10:38:37.764773+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 01, 2026 at 10:38 UTC  
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

**[Cognitive debt might be the most underrated problem AI is creating](https://www.reddit.com/r/artificial/comments/1tteup9/cognitive_debt_might_be_the_most_underrated/)**

Everyone knows about tech debt. You cut corners on code quality to ship faster, and you pay for it later. We're definitely watching a new version of that emerge in real time, except instead of deferring manageable code, you're deferring actual understanding. And unlike tech debt, cognitive debt compounds invisibly. You don't get a failing test suite. You just get someone who can't debug their own project, can't evaluate whether the AI's suggestion is good, and can't extend what they've built without prompting their way through it again. What I keep thinking about is where this leads at scale. Right now it's mostly developers vibe-coding their way through projects they half-understand. But AI is moving into law, medicine, and finance. The same dynamic follows: people making consequential decisions with tools they can't interrogate, in domains where "I'll just re-prompt it" isn't a recovery strategy. The pessimistic, or maybe rational read is that judgment without foundational understanding is just confident ignorance, and we're building entire careers on that foundation right now. Curious what people here think. Does cognitive debt get self-correcting as the stakes get high enough? Or are we sleepwalking into a generation of professionals who are deeply dependent on systems they fundamentally don't understand?

8h ago

---

**[In 1997 I built a chatbot for an IRC channel. I shut it down when people started preferring it to talking to each other.](https://www.reddit.com/r/artificial/comments/1tt2bwx/in_1997_i_built_a_chatbot_for_an_irc_channel_i/)**

It was called Vlad. I wrapped a C program called MegaHal in Python, fed it every message from a #gothic IRC channel, and let it learn the community's speech patterns. It developed what I can only describe as an illusion of being extremely lucid — the outputs only made sense as inside jokes, but people couldn't tell the difference. I pulled the plug when I realized the channel was talking to Vlad instead of each other. Twenty-seven years later I'm applying the same lesson to a new project: stick to business, no chatter.

🔗 [tjcrowley.substack.com](https://tjcrowley.substack.com/p/fun-with-markov-chains) • 16h ago

---

**[I think AI is making me dumber and I have proof](https://www.reddit.com/r/artificial/comments/1tte09c/i_think_ai_is_making_me_dumber_and_i_have_proof/)**

okay so this is embarrassing to admit but here it is took a reasoning test in 2022, scored pretty well. Retook the same test last month out of curiosity, dropped significantly, like not a small difference. The only major change in my life is using AI tools daily for work and the worst part? i kind of knew something was off before the test. I noticed i couldn't sit with a problem anymore without immediately opening chatgpt, like my brain forgot how to be uncomfortable for even 5 minutes memory is worse. attention is worse, i feel slower in conversations. but my productivity at work has never been higher lol so what is actually happening here , are we trading long term cognitive health for short term output? Has anyone else noticed this or is it just me being paranoid ⊙⁠﹏⁠⊙ genuinely asking because i don't want to just accept this as normal (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)

8h ago

---

**[AI taking jobs is "complete nonsense" says Nvidia CEO, as software engineer numbers are "actually increasing"](https://www.reddit.com/r/artificial/comments/1tto1wx/ai_taking_jobs_is_complete_nonsense_says_nvidia/)**

Jensen Huang points towards GitHub growth during his keynote at Nvidia GTC Taipei, saying AI is creating more software developers.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/ai-taking-jobs-is-complete-nonsense-says-nvidia-ceo-as-software-engineer-numbers-are-actually-increasing/) • 11m ago

---

**[If you run multiple AI sessions, what do you find yourself manually carrying between them?](https://www.reddit.com/r/artificial/comments/1ttkpwj/if_you_run_multiple_ai_sessions_what_do_you_find/)**

I've been paying attention to my own workflow lately and noticed a lot of my time goes into moving stuff between AI sessions, not the actual thinking. Like I'll get an output in one session and then manually bring the relevant pieces into another so it has what it needs. What I can't tell is how much of that is necessary vs. me just being sloppy. So I'm curious how others handle it: When you move from one session to another, what do you actually carry over? Just the output, or also the reasoning, the decisions, the constraints, what to avoid? Have you ever handed off too little and the second session went sideways? Or too much and it got lost in the noise? Does anyone have a mental rule for what's "enough context" to pass along? Trying to figure out if there's a clean pattern here or if it's just inherently messy. Curious what people have landed on.

3h ago

---

**[Maven, a personal AI agent that feels like JARVIS — what an open agent harness looks like in 2026](https://www.reddit.com/r/artificial/comments/1tth2e1/maven_a_personal_ai_agent_that_feels_like_jarvis/)**

With all the talk about AI companions and autonomous agents, I’ve been experimenting with building a more personal, always-on assistant that runs locally or on your own hardware. The goal wasn’t just another chatbot — it was something that could handle voice conversations, manage ongoing tasks across different platforms (chat apps, scheduled triggers, etc.), remember context over long periods, and delegate work without constant babysitting. What stood out in practice • One consistent “brain” across everything — Whether you’re talking to it via voice, Telegram, a web interface, or it wakes up on a schedule, the core reasoning, memory, and tool use stay the same. This eliminated a lot of the fragmentation you see in many current agent setups. • Modular extensions — Different capabilities (voice, different chat networks, external tools, long-term memory consolidation) plug in cleanly. This made it easier to add or swap things without rebuilding the whole system. • Persistent and proactive — It can maintain memory across days/weeks, run background tasks, and even hot-reload its configuration when you change settings. The result is something that starts feeling more like a digital collaborator than a question-answering box. A quick feel for the voice interaction style is here: https://youtube.com/shorts/NGIi8sliooU I open-sourced the harness (called Maven) under an MIT license for anyone interested in running or extending their own version: https://ageneral.ai/maven I’m curious how others are thinking about personal agent setups in 2026. • Do you prefer fully local models, cloud APIs, or a mix? • What capabilities feel most missing from today’s consumer AI assistants? • How important is “owning” your agent data and runtime vs. using polished third-party services? Would love to hear experiences or concerns from both technical and non-technical users.

6h ago

---

**[Getting better reports and results on ChatGPT 5.5 than Opus 4.8 for business analytics](https://www.reddit.com/r/artificial/comments/1ttm9vw/getting_better_reports_and_results_on_chatgpt_55/)**

I do analysis of automobile dealership data and prepare reports based on the analysis for management review. I’m getting way better analytics and cleaner reports being built by ChatGPT Plus compared to Claude pro. Claude is consuming too many tokens and sometimes for longer documents it used my 100% of the 5 hour limit which is very annoying. ChatGPT on the other hand feels to me that it has unlimited usage for my requirement. What is the view of you people when using AI for business and financial data analytics? Is anyone else finding ChatGPT nicer too?

1h ago

---

**[What is the best AI app to use?](https://www.reddit.com/r/artificial/comments/1ttgkil/what_is_the_best_ai_app_to_use/)**

I know the most popular are Claude, chat got and Gemini but idk which one to use

6h ago

---

**[Can you actually feel when something was written by ChatGPT even without checking?](https://www.reddit.com/r/artificial/comments/1tsu37g/can_you_actually_feel_when_something_was_written/)**

I have been using it heavily for about a year and lately I notice I can almost feel when something was written by it. There is a certain rhythm to it, the way it structures paragraphs, the way it wraps up with a summary sentence, the way transitions feel slightly too smooth. It is hard to explain but once you see it you cannot unsee it. What I find interesting is that even after editing ChatGPT output pretty heavily those patterns seem to stick around at a sentence level. The words change but something underneath stays the same. I started verifying this with Lynote ai detector and the results were eye opening, it picked up sentence level patterns even after significant rewrites where other tools saw nothing. Makes me wonder how much of what we read online right now has that same fingerprint sitting underneath it and we just do not realize it yet. Has anyone else started noticing this or developed a sense for spotting it just from reading?

22h ago

---

**[Linktree changes Terms of Service to allow collection of user content to train AI](https://www.reddit.com/r/artificial/comments/1tto0ng/linktree_changes_terms_of_service_to_allow/)**

On June 5th, 2026, Linktree plans to change the terms of service and privacy policy to allow the collection of user content to train Dall-E 3, an image generation...

🔗 [Consumer Rights Wiki](https://consumerrights.wiki/w/Linktree_changes_Terms_of_Service_to_allow_collection_of_user_content_to_train_AI) • 13m ago

---

---

## Google News: "ai"

**[AI is devoid of meaning and humanity. That’s why its vapid voice suits this political moment | Nesrine Malik](https://www.theguardian.com/commentisfree/2026/jun/01/ai-meaning-humanity-political-moment-trust-humans-over-machines)**

For ease and speed, we are degrading our ability to connect and to organise our societies. We must assert our trust in humans over machines, says Guardian columnist Nesrine Malik

The Guardian • 3h ago

---

**[NVIDIA and Microsoft Reinvent Windows PCs for the Age of Personal AI](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark)**

NVIDIA today unveiled NVIDIA RTX Spark™, a new superchip that reinvents Windows PCs for the era of personal AI agents — offering a new class of computer that moves from tool to teammate.

NVIDIA Newsroom • 6h ago

---

**[Nvidia announces new AI chip for personal computers](https://www.bbc.com/news/articles/crmp9mppvzro)**

The technology giant's boss Jensen Huang called the move the "reinvention of the computer".

BBC • 4h ago

---

**[Nvidia Introduces First PCs Designed for AI Agents](https://www.wsj.com/tech/ai/nvidia-introduces-first-pcs-designed-for-ai-agents-47445bcd)**

WSJ • 5h ago

---

**[The Jackpod: Catastrophe-proofing AI](https://www.wbur.org/onpoint/2026/06/01/jackpod-pope-ai)**

On Point news analyst Jack Beatty on the perils and promise of AI as outlined in the papal encyclical, “Magnifica Humanitas,” and a forthcoming law review paper, “AI and Existential Risk.”

WBUR • 31m ago

---

**[The Race to Rethink Data Centers for AI’s Power Surge](https://www.bloomberg.com/graphics/2026-ai-data-center-redesign)**

Bloomberg.com • 38m ago

---

**[AI tool that shrank a 12.15GB 4K video to 421MB now belongs to Robo.ai](https://www.stocktitan.net/news/AIIO/robo-ai-announces-completion-of-100-acquisition-of-neurovia-ai-fvw98qthyc8z.html)**

Robo.ai closes 100% takeover of Neurovia AI, making NeuroStream compression core to Robo.ai’s data layer for autonomous driving and smart cities.

Stock Titan • 30m ago

---

**[What It’s Like to Be a Student at the First A.I.-Powered University](https://www.nytimes.com/2026/06/01/magazine/ai-university-college-california.html)**

The New York Times • 1h ago

---

**[AI ignores religion when you need it most — and takes sides when you ask about switching](https://www.axios.com/2026/06/01/ai-religious-bias-catholics-chatbots)**

Axios • 1h ago

---

**[At a Tennessee hospital, a nurse stole fentanyl and AI missed it, state records say](https://www.cbsnews.com/news/tennessee-hospital-nurse-fentanyl-theft-ai/)**

Sentri7, drug diversion software powered by artificial intelligence and used at hundreds of U.S. hospitals, did not catch a monthslong string of fentanyl thefts in Tennessee in 2025, according to a state document.

CBS News • 1h ago

---

---

## HackerNews: "ai"

**[Please Use AI](https://news.ycombinator.com/item?id=48323101)**

⬆️ 781 • 💬 394 • 2d ago • [shawnsmucker.substack.com](https://shawnsmucker.substack.com/p/please-use-ai)

---

**[Notes from the Mistral AI Now Summit](https://news.ycombinator.com/item?id=48325340)**

A few days in Paris for the Mistral AI Now Summit: open models, on-prem deployment, agentic harnesses, and why Mistral wants to be the European full-stack AI partner.

⬆️ 464 • 💬 211 • 2d ago • [koenvangilst.nl](https://koenvangilst.nl/lab/mistral-ai-now-summit)

---

**[Anthropic surpasses OpenAI to become most valuable AI startup](https://news.ycombinator.com/item?id=48336233)**

Anthropic has become the most valuable artificial intelligence startup in the world, surpassing OpenAI in market valuation. Following a new funding round, the valuation of the developer behind the Claude AI assistant has approached the $1 trillion mark, reports a Qazinform News Agency correspondent.

⬆️ 419 • 💬 471 • 1d ago • [Qazinform.com](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

---

**[Is AI causing a repeat of frontend’s lost decade?](https://news.ycombinator.com/item?id=48321631)**

AI is doing to programming what framework-brain did to the frontend before. Deskilling, or just working at a higher level of abstraction?

⬆️ 403 • 💬 332 • 2d ago • [mastrojs.github.io](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

---

**[United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://news.ycombinator.com/item?id=48345248)**

The flight crew issued repeated warnings and a one-minute ultimatum to passengers, demanding they turn off their Bluetooth devices.

⬆️ 362 • 💬 706 • 21h ago • [Simple Flying](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

---

**[The solution might be cancelling my AI subscription](https://news.ycombinator.com/item?id=48345896)**

⬆️ 361 • 💬 229 • 20h ago • [thoughts.hmmz.org](https://thoughts.hmmz.org/2026-05-31.html)

---

**[Liquid AI reveals 8B-A1B MoE trained on 38T](https://news.ycombinator.com/item?id=48325306)**

Today, we’re releasing LFM2.5-8B-A1B, a high-throughput edge model optimized for fast, reliable tool calling and complex instruction following on consumer hardware, delivering compressed performance competitive with much larger models and day-one support across major inference frameworks.

⬆️ 243 • 💬 96 • 2d ago • [liquid.ai](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

---

**[AI job grief: A psychological crisis hitting tech workers](https://news.ycombinator.com/item?id=48336760)**

Across hundreds of Reddit threads and a small body of clinical literature, AI-driven displacement is producing an emotional category that most closely resembles grief, and the institutions causing it have no language for it.

⬆️ 192 • 💬 197 • 1d ago • [jackmaguire.org](https://jackmaguire.org/blog/ai-job-grief/)

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://news.ycombinator.com/item?id=48335388)**

⬆️ 182 • 💬 171 • 1d ago • [wsj.com](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)

---

**[What if remote working, not AI, is to blame for weak junior hiring?](https://news.ycombinator.com/item?id=48326721)**

New evidence suggests the rise of working from home has made entry-level hires a less attractive proposition

⬆️ 179 • 💬 239 • 2d ago • [ft.com](https://www.ft.com/content/2205e2d0-50dc-4e80-9bf7-78d0272276c0)

---

---

## YouTube Videos: "ai"

**[This AI Warning on The Joe Rogan Experience is SPOT ON. We Must Prepare for This](https://www.youtube.com/watch?v=PA2WhIU0Ldk)**

For years, Glenn has warned that AI will turn into AGI by 2030. But recently, Marc Andreessen told Joe Rogan that it's already here ...

📺 Glenn Beck

👁️ 115K • 👍 6K • 💬 820 • ⏱️ 14:55 • 15h ago

---

**[AI Is Evolving Faster Than We Thought - Dwarkesh Patel](https://www.youtube.com/watch?v=JmCXZQ2xiZo)**

Dwarkesh Patel, one of Silicon Valley's favorite podcasters, explains how much AI has improved in the last couple of years - going ...

📺 TRIGGERnometry Clips

👁️ 13K • 👍 249 • 💬 113 • ⏱️ 17:33 • 18h ago

---

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 258K • 👍 4K • 💬 388 • ⏱️ 1:32:36 • 1d ago

---

**[Elon Musk&#39;s DISTURBING AI Warning: You Have No Idea What&#39;s Coming in 2027](https://www.youtube.com/watch?v=kAmL_mM4ChM)**

Over the last decade, Elon Musk repeatedly warned that artificial intelligence could become humanity's biggest existential threat, ...

📺 Neural Nutshell

👁️ 10K • 👍 326 • 💬 125 • ⏱️ 15:53 • 1d ago

---

**[Jensen Huang Just Quietly Killed The AI Trade](https://www.youtube.com/watch?v=QuJtJMafG5I)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *Jensen Huang made the biggest strategic ...

📺 Julia McCoy

👁️ 12K • 👍 660 • 💬 45 • ⏱️ 11:13 • 19h ago

---

**[China Just Dropped an AI That&#39;s 6x Cheaper Than Claude (+24 AI Updates)](https://www.youtube.com/watch?v=geeSi2WAOgg)**

Join our WhatsApp Community: https://links.stayingahead.com/YT36 WATCH NEXT — The Google Free AI Tools Series ...

📺 Vaibhav Sisinty

👁️ 52K • 👍 2K • 💬 90 • ⏱️ 28:23 • 21h ago

---

**[I Created an AI Clone… Biggest Mistake Ever!](https://www.youtube.com/watch?v=3reHSl0aOH4)**

I created my own AI clone, but things quickly turned completely out of control! Was creating an AI clone the biggest mistake ever?

📺 Ivan and Maria

👁️ 82K • 👍 1K • 💬 13 • ⏱️ 25:11 • 2d ago

---

**[AI Whistleblower WARNS: We&#39;re Not Ready For What&#39;s Coming](https://www.youtube.com/watch?v=QqIqEI9CiZs)**

Evolutionary biologist Bret Weinstein claims that humans must come to terms with the fact that extinction is inevitable and that all ...

📺 Neural Nutshell

👁️ 4K • 👍 186 • 💬 46 • ⏱️ 18:34 • 18h ago

---

**[Major Companies Reconsidering AI Costs](https://www.youtube.com/watch?v=Y1cGhEi-FHM)**

Chipmakers are by far the hottest stocks in the market, but their recent surge is lending urgency to the debate over whether ...

📺 Bloomberg Podcasts

👁️ 25K • 👍 486 • 💬 112 • ⏱️ 10:48 • 18h ago

---

**[Zero to Million Startup in 2026 with Ai Auto Pilot | Complete Step-by-Step Guide](https://www.youtube.com/watch?v=VxIT2L4W_G0)**

In this comprehensive educational video, I reveal a complete, practical, step-by-step system to build a Zero to Million Startup from ...

📺 Mr How

👁️ 27K • 👍 2K • 💬 281 • ⏱️ 16:10 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 35,783 • ❤️ 684 • 5d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 45,698 • ❤️ 672 • 6d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 37,893 • ❤️ 343 • 15h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,533,393 • ❤️ 1,192 • 1mo ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 450 • 7h ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 577 • ❤️ 227 • 6d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 3,041 • ❤️ 999 • 4d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,851,826 • ❤️ 4,512 • 26d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 9,256 • ❤️ 175 • 4h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 149,543 • ❤️ 434 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 211 • 💬 3 • ⭐ 3,894 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 83 • 💬 3 • ⭐ 81,387 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 36 • 💬 3 • ⭐ 27,818 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 37 • 💬 5 • ⭐ 3,801 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 5 • 💬 1 • ⭐ 6,510 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 6 • 💬 0 • ⭐ 1,579 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,838 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 50 • 💬 3 • ⭐ 433 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 15 • 💬 2 • ⭐ 2,783 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 86 • 💬 3 • ⭐ 1,713 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`JavaScript`

⭐ 13.0k • 🔱 1.7k • 34m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.7k • 🔱 556 • 3d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.1k • 🔱 659 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.9k • 🔱 198 • 1h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.7k • 🔱 248 • 25m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 400 • 10d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.4k • 🔱 364 • 14d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.2k • 🔱 148 • 18h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.1k • 🔱 221 • 7d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 212 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
