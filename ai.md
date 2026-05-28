---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-28T21:31:43.094580+00:00'
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

**Last Updated:** May 28, 2026 at 21:31 UTC  
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

**[The OpenClaw crisis is the most complete case study of agentic AI security failure. Here's the full timeline and technical breakdown.](https://www.reddit.com/r/artificial/comments/1tq0t1g/the_openclaw_crisis_is_the_most_complete_case/)**

OpenClaw the open source AI agent platform with 346K+ GitHub stars had four chainable CVEs disclosed on May 15. But that was just the latest chapter. The crisis started in january and it's worse than most people realize. The numbers 245,000 instances exposed to the public internet (Shodan + ZoomEye scans) 30,000+ actively compromised and used by attackers (Flare) 1,184 malicious marketplace skills across 12 publisher accounts (Antiy Labs) 12% of the entire ClawHub marketplace was compromised 4 chainable CVEs including a CVSS 9.6 sandbox write escape (Cyera Research) 9 CVEs disclosed in a 4-day window in March 50,000+ instances exploitable via one-click RCE (CVE-2026-25253) The Claw Chain (Cyera Research, May 15) Four CVEs that chain together into a complete kill chain CVE-2026-44113 (CVSS 7.7) - TOCTOU filesystem read escape. Race condition lets you swap paths with symlinks to read outside the sandbox CVE-2026-44115 (CVSS 8.8) - Credential disclosure. Gap between command validation and shell execution leaks API keys through unquoted heredocs CVE-2026-44118 (CVSS 7.8) - MCP loopback privilege escalation. Trusts client-controlled senderIsOwner flag without session validation CVE-2026-44112 (CVSS 9.6) - Filesystem write escape. Same TOCTOU race in write ops. Backdoor placement on the host The chain malicious plugin -> read escape + credential theft -> privilege escalation -> persistent backdoor. Every step mimics normal agent behavior. Traditional monitoring cannot distinguish this from legitimate operations. ClawHavoc supply chain attack (Jan-Feb 2026) First malicious skill appeared January 27 By February 5, 1,184 malicious packages identified Skills disguised as crypto bots and productivity tools Installed keyloggers on Windows, Atomic Stealer on macOS 76 distinct malicious payloads ClawHub had zero verification for skill publishers until March 26 - eight weeks after the attack started Timeline Jan 27 - First malicious skill on ClawHub Feb 1 - Koi Security names "ClawHavoc" Feb 3 - CVE-2026-25253 (one-click RCE) disclosed Feb 5 - 1,184 malicious skills identified Feb 9 - 135K exposed instances found Feb 18 - 312K+ instances on default port Mar 18-21 - 9 CVEs in 4 days Mar 26 - ClawHub adds verified screening Apr 23 - Claw Chain patches released May 15 - Claw Chain research published What this means for all AI agent deployments the underlying problems are not unique to OpenClaw Agents running with user's full credentials across every connected system Marketplace/plugin ecosystems with no security review Sandbox implementations with race condition vulnerabilities No behavioral monitoring to detect multi-step attacks that mimic normal behavior Default configs exposing agents to the internet with no auth If you're running any AI agents in production, the OpenClaw crisis is your case study. Scan inputs at runtime. Isolate credentials per agent. Monitor behavior patterns, not just system metrics.

10h ago

---

**[Bigger rewards dramatically speed up learning in the brain](https://www.reddit.com/r/artificial/comments/1tq3pk8/bigger_rewards_dramatically_speed_up_learning_in/)**

Scientists found that larger rewards create longer dopamine signals that dramatically speed up learning in the brain.

🔗 [Earth.com](https://www.earth.com/news/bigger-rewards-dramatically-speed-up-learning-in-the-brain/) • 8h ago

---

**[How does the economy work if everyone gets laid off and human jobs disappear?](https://www.reddit.com/r/artificial/comments/1tq8bnq/how_does_the_economy_work_if_everyone_gets_laid/)**

If almost all jobs got replaced by AI, here's what happens: 1) Corporate revenue collapses - since humans do not have the means to buy product. It leads to demand destruction at an all-time level. 2) At the same time, there's a massive deflationary supply shock, thanks to democratization of production and the ubiquity of AI-led labor. The direct consequence of the aforementioned is: a price collapse, across the board. Which in turn, also leads to unprecedented tax revenue collapse. Who're you going to tax when no individual or corporate is making any money? To me, all this heralds a post-capitalism society, and not a "I-lost-my-job-and-I'm-now-poor" society. Once everyone loses their jobs, capitalism is over. Sure you can have an interim period of distress - where the world is transforming toward post-capitalism but isn't squarely there yet. But the final equilibrium intuitively feels more Star Trek (or Terminator, if you're a doomer), and much less Elysium or Ready Player One (few oligarchs, most population under poverty line). Correct me if I'm wrong.

5h ago

---

**[Anthropic releases Claude Opus 4.8 with improved agentic reasoning, honesty, and a new "dynamic workflows" feature in Claude Code](https://www.reddit.com/r/artificial/comments/1tq9l1z/anthropic_releases_claude_opus_48_with_improved/)**

Anthropic just dropped Claude Opus 4.8 today, an incremental but meaningful upgrade over Opus 4.7. Here are the highlights: Model improvements Better performance across coding, agentic, reasoning, and knowledge work benchmarks Significantly improved honesty: the model is reportedly ~4x less likely to let flaws in its own code go unremarked compared to Opus 4.7 Alignment assessment shows lower rates of deceptive or misaligned behavior, on par with their Claude Mythos Preview model Scores 84% on Online-Mind2Web for computer use and browser agent tasks, ahead of both Opus 4.7 and GPT-5.5 New features launching alongside it Dynamic workflows (Claude Code): Claude can now spin up hundreds of parallel subagents in a single session to tackle large-scale problems like full codebase migrations. Available for Enterprise, Team, and Max plans. Effort control: Users on claude.ai can now choose how much compute effort Claude puts into a response, from faster/cheaper to deeper/slower. API update: The Messages API now accepts system entries inside the messages array, letting developers update instructions mid-task without breaking prompt cache. Pricing Same as Opus 4.7: $5/M input tokens, $25/M output tokens. Fast mode (2.5x speed) is now 3x cheaper than it was for previous models, at $10/$50 per million tokens. What's next Anthropic mentioned they are working on bringing Mythos-class models (currently in limited preview for cybersecurity use cases under Project Glasswing) to general availability in the coming weeks. Full details and system card: anthropic.com/news/claude-opus-4-8

4h ago

---

**[Opus 4.8 just released, waiting for it to land in Claude code](https://www.reddit.com/r/artificial/comments/1tq9ndg/opus_48_just_released_waiting_for_it_to_land_in/)**

4h ago

---

**[Experiment to see what happens when you let AI models run the world](https://www.reddit.com/r/artificial/comments/1tq5r1z/experiment_to_see_what_happens_when_you_let_ai/)**

6h ago

---

**[Nothing is real anymore. We are reaching the point where crowd scenes can be entirely generated by AI.](https://www.reddit.com/r/artificial/comments/1tp9ujl/nothing_is_real_anymore_we_are_reaching_the_point/)**

AI can now realistically simulate massive crowds and public events. The scary part isn’t the quality anymore. It’s how quickly people are discovering creative ways to use it. Reality online is about to get very confusing. 💀

1d ago

---

**[Chase the next new thing or lock-in on one ecosystem?](https://www.reddit.com/r/artificial/comments/1tqf4i1/chase_the_next_new_thing_or_lockin_on_one/)**

I love all the wild updates from Anthropic, Open AI, Google, etc. And also seeing the creative stuff that mid-market AI shops are rolling out. I sometimes go through phases where I ping-pong between new tools (mostly just curiosity) but sometimes I tend to go deeper into a specific ecosystem. Right now trying to go "all-in" on Claude but I'm like a cat and Open AI is the laser pointer with new Codex updates. What have you all found works best. Go wide and test everything? Different tools for different use cases. Go deep and specialize in one ecosystem?

1h ago

---

**[Nobody on the internet knows if you are a human](https://www.reddit.com/r/artificial/comments/1tq5v6b/nobody_on_the_internet_knows_if_you_are_a_human/)**

🔗 [danieltan.weblog.lol](https://danieltan.weblog.lol/2026/05/nobody-on-the-internet-knows-if-you-are-a-human) • 6h ago

---

**[AI Adoption Issue Debugging](https://www.reddit.com/r/artificial/comments/1tqgmto/ai_adoption_issue_debugging/)**

I was dealing with another "output not usable" issue today in our app, user left a comment saying that no matter what he does the agent returns the result in the wrong format. It took me hours to identify the mistake and AI model missed it. Curious to hear your stories about the times you shipped a feature in your AI product and it flopped. How did you figure out what was actually going wrong? What tools if any did you use? What metrics were key?

20m ago

---

---

## Google News: "ai"

**[Apple to Overhaul iOS 27 Siri, AI Features: Here's a First Peek](https://www.bloomberg.com/news/features/2026-05-28/apple-ios-27-photos-screenshots-revamped-siri-pro-camera-app-new-ai-features)**

Bloomberg.com • 9h ago

---

**[AI sticker shock hits corporate America](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)**

Axios • 12h ago

---

**[AI is moving fast. 2028 hopefuls will be forced to adapt: From the Politics Desk](https://www.nbcnews.com/politics/politics-news/ai-moving-fast-2028-hopefuls-will-forced-adapt-politics-desk-rcna347411)**

Plus, how Iowa farmers are feeling about Trump and the economy.

NBC News • 18m ago

---

**[Robinhood to allow AI agents to make stock trades, credit card purchases](https://www.cbsnews.com/video/robinhood-allow-ai-agents-stock-trades-credit-card-purchases/)**

The digital investing platform Robinhood is now allowing AI agents to trade stocks and make credit card purchases for users. Yahoo Finance senior reporter Brooke DiPalma joins with the details.

CBS News • 1h ago

---

**[Anthropic tops OpenAI as most valuable AI startup, nears $1 trillion valuation in latest round](https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html)**

Anthropic is now the most valuable AI company in Silicon Valley after a new $65 billion funding round.

CNBC • 2h ago

---

**[Anthropic Tops OpenAI to Become the World’s Most Valuable A.I. Start-Up](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html)**

The New York Times • 1h ago

---

**[Anthropic: San Francisco AI company vaults to a $965 billion valuation with new funding as Claude demand surges](https://abc7chicago.com/post/anthropic-san-francisco-ai-company-vaults-965-billion-valuation-new-funding-claude-demand-surges/19188579/)**

Artificial intelligence company Anthropic said Thursday it raised $65 billion in private funding that will push its valuation to $965 billion, a whopping number that makes the five-year-old maker of the Claude chatbot one of the world's most valuable startups as it careens toward a likely Wall Street debut.

ABC7 Chicago • 54m ago

---

**[Snowflake surges 36% for best day ever on AI frenzy, fueling software rally](https://www.cnbc.com/2026/05/28/snowflake-snow-software-stock-rally.html)**

The Snowflake rally also lifted shares of ServiceNow, Oracle and Palantir, while Salesforce bucked the trend.

CNBC • 7h ago

---

**[AI is changing this job so fast the interview process can’t keep up](https://www.cnn.com/2026/05/28/tech/ai-software-engineering-job-interview)**

Now that AI can write code, what makes a good software engineer? That’s the question hiring managers in the tech industry are grappling with.

CNN • 11h ago

---

**[Boston Seizes on California Billionaire Tax to Lure AI Jobs](https://finance.yahoo.com/sectors/technology/articles/boston-seizes-california-billionaire-tax-120000210.html)**

(Bloomberg) -- The talent at some of America’s hottest artificial intelligence companies often passes through Boston-area universities before heading west to build billion-dollar businesses in Silicon Valley. Massachusetts business and political leaders say California’s proposed tax on billionaires is an opportunity to change that.Most Read from BloombergSingapore Hands Byju's Founder His First Ever Jail TermIran’s Khamenei Says No Going Back for Middle East Rocked by WarApple to Overhaul iOS 27

Yahoo Finance • 3h ago

---

---

## HackerNews: "ai"

**[I'm Tired of Talking to AI](https://news.ycombinator.com/item?id=48292224)**

I found GitHub repositories that were spreading malware. I asked AI what to do about it, but it gave me nothing useful. So I opened a discussion on GitHub. Someone replied. It was the exact same text the AI had given me. I called it out and the comment was

⬆️ 1959 • 💬 933 • 1d ago • [Orchid Files](https://orchidfiles.com/im-tired-of-ai-generated-answers/)

---

**[YouTube to automatically label AI-generated videos](https://news.ycombinator.com/item?id=48299753)**

We've heard consistently from our community that they value transparency when it comes to generative AI content. Two new updates will make this process much simpler and more intuitive for creators and viewers on YouTube.

⬆️ 1252 • 💬 747 • 1d ago • [blog.youtube](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/)

---

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1236 • 💬 446 • 2d ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[DuckDuckGo search saw 28% more visits after Google said people love AI mode](https://news.ycombinator.com/item?id=48296649)**

"People just want a choice."

⬆️ 1041 • 💬 503 • 1d ago • [PC Gamer](https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/)

---

**[Tech CEOs are apparently suffering from AI psychosis](https://news.ycombinator.com/item?id=48295679)**

"CEOs are uniquely prone to AI psychosis," Box CEO Aaron Levie opines. Maybe that explains the almost religious belief in AI productivity gains.

⬆️ 698 • 💬 350 • 1d ago • [TechCrunch](https://techcrunch.com/2026/05/27/tech-ceos-are-apparently-suffering-from-ai-psychosis/)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 321 • 💬 365 • 2d ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 303 • 💬 158 • 2d ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[Training our own AI models](https://news.ycombinator.com/item?id=48296359)**

I really think we're on the verge of some of our best work through the next six months. Over the past year, we've started building more AI-powered…

⬆️ 210 • 💬 143 • 1d ago • [posthog.com](https://posthog.com/blog/training-ai-models)

---

**[Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue](https://news.ycombinator.com/item?id=48308376)**

A 30-second game about LLM permission fatigue. How carefully do you really read AI commands?

⬆️ 187 • 💬 91 • 8h ago • [llmgame.scalex.dev](https://llmgame.scalex.dev)

---

**[AI sticker shock hits corporate America](https://news.ycombinator.com/item?id=48307098)**

⬆️ 150 • 💬 131 • 10h ago • [axios.com](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)

---

---

## YouTube Videos: "ai"

**[We Saw What AI Data Centers Don&#39;t Want You to See](https://www.youtube.com/watch?v=5p426fSlYH4)**

We investigated one of the world's largest AI data centers, using thermal drone footage to reveal the hidden pollution powering the ...

📺 PBS Terra

👁️ 49K • 👍 6K • 💬 1K • ⏱️ 21:45 • 5h ago

---

**[Linda McMahon shuts down Randi Weingarten’s A.I. warnings | National Report](https://www.youtube.com/watch?v=fQuVTiyQxXo)**

Education Secretary Linda McMahon joined “National Report” to discuss the future of artificial intelligence in American classrooms ...

📺 Newsmax

👁️ 3K • 👍 396 • 💬 67 • ⏱️ 4:31 • 7h ago

---

**[Master AI Films In 9 Minutes (AI Filmmaking Tutorial)](https://www.youtube.com/watch?v=DfdlAwJ4SKw)**

Seedance 2.0 Creates INSANE AI Short Films - here's how to make them! Create your AI Film ...

📺 Mira AI

👁️ 5K • ⏱️ 9:16 • 5h ago

---

**[Vance voices concerns over AI](https://www.youtube.com/watch?v=O0L3Ektu7xU)**

While speaking to Air Force graduates, vice president JD Vance said the thing he is most concerned about with AI is how it will ...

📺 WLUK-TV FOX 11

👁️ 2K • 👍 41 • 💬 15 • ⏱️ 2:19 • 2h ago

---

**[AI Whistleblower WARNS: You Have NO Idea About The AI Wave That Is Coming](https://www.youtube.com/watch?v=fo2ggNE-44g)**

Eliezer Yudkowsky, who has spent 30 years on the AI safety problem, makes a firm prediction: if anyone builds a superintelligence ...

📺 Neural Nutshell

👁️ 14K • 👍 418 • 💬 100 • ⏱️ 22:04 • 1d ago

---

**[China’s Plan To POP U.S. AI Bubble Goes Global — Cheap Chips FLOOD &amp; Talent Freeze Begins](https://www.youtube.com/watch?v=9_eG-uEtc0k)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout The Chip War has ...

📺 Sean Foo

👁️ 67K • 👍 5K • 💬 623 • ⏱️ 13:28 • 23h ago

---

**[EMERGENCY DEBATE: They Are Lying To Us About AI, The Iran War &amp; What Happens Next!](https://www.youtube.com/watch?v=H-8NrKFQKhU)**

Shark Tank's Kevin O'Leary and political commentator Cenk Uygur go head to head on whether AI will save or destroy the ...

📺 The Diary Of A CEO

👁️ 334K • 👍 12K • 💬 5K • ⏱️ 1:43:32 • 14h ago

---

**[The Man Who Called The AI Boom Is Buying These 2 “Hidden” Stocks](https://www.youtube.com/watch?v=f0c6kCST3Mw)**

A 24-year-old AI prodigy turned $240 million into $5.5 BILLION... and now he's making one of the biggest bets Wall Street has ...

📺 Ross Givens

👁️ 74K • 👍 3K • 💬 524 • ⏱️ 13:47 • 1d ago

---

**[A.I. Futurist: What Your Life Looks Like In 2028](https://www.youtube.com/watch?v=tBiO8A4tj9I)**

After a full year of being told AI was going to wipe out jobs, the collapse hasn't happened. At least not yet. Unemployment hasn't ...

📺 Mighty Pursuit

👁️ 15K • 👍 355 • 💬 111 • ⏱️ 2:02:32 • 2d ago

---

**[Andrew Yang Has Been Preparing for This AI Moment for Years](https://www.youtube.com/watch?v=4EkBXJcWUpQ)**

Former presidential candidate and Noble Mobile CEO Andrew Yang shares how he sees AI reshaping everyday life and why the ...

📺 This is Gavin Newsom

👁️ 25K • 👍 2K • 💬 518 • ⏱️ 55:46 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 15,629 • ❤️ 487 • 2d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,506 • ❤️ 953 • 15h ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 365 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,956,558 • ❤️ 993 • 1mo ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 13,855 • ❤️ 429 • 8d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,281,601 • ❤️ 4,400 • 22d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 52,022 • ❤️ 725 • 10d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 121,862 • ❤️ 400 • 7d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 1,755 • ❤️ 172 • 1d ago

---

**[Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)**

*Jackrong*

Qwopus3.6-27B-v2 is a multimodal, 27B parameter language model fine-tuned on Qwen3.6-27B, excelling at image-to-text generation and complex reasoning tasks by reconstructing structured chain-of-thought reasoning. It supports tool use and long contexts, making it suitable for agentic applications and advanced analysis.

`image-text-to-text` `27.3B`

⬇️ 24,336 • ❤️ 170 • 17h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 191 • 💬 3 • ⭐ 1,879 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 80,405 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 27,100 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,420 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,169 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 43 • 💬 2 • ⭐ 192 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,837 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 122 • 💬 10 • ⭐ 10,920 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 57 • 💬 1 • ⭐ 81,295 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 6 • 💬 3 • ⭐ 138 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23264) • [💻 code](https://github.com/wafer-bob/ASASR)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.3k • 🔱 528 • 6d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.6k • 🔱 1.1k • 11d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.8k • 🔱 186 • 19m ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.7k • 🔱 575 • 3d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 396 • 6d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 355 • 11d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.1k • 🔱 139 • 4h ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 222 • 21d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 1.9k • 🔱 194 • 3d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 204 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
