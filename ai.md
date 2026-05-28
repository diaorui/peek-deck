---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-28T19:12:29.621700+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 28, 2026 at 19:12 UTC  
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

7h ago

---

**[Bigger rewards dramatically speed up learning in the brain](https://www.reddit.com/r/artificial/comments/1tq3pk8/bigger_rewards_dramatically_speed_up_learning_in/)**

Scientists found that larger rewards create longer dopamine signals that dramatically speed up learning in the brain.

🔗 [Earth.com](https://www.earth.com/news/bigger-rewards-dramatically-speed-up-learning-in-the-brain/) • 5h ago

---

**[How does the economy work if everyone gets laid off and human jobs disappear?](https://www.reddit.com/r/artificial/comments/1tq8bnq/how_does_the_economy_work_if_everyone_gets_laid/)**

If almost all jobs got replaced by AI, here's what happens: 1) Corporate revenue collapses - since humans do not have the means to buy product. It leads to demand destruction at an all-time level. 2) At the same time, there's a massive deflationary supply shock, thanks to democratization of production and the ubiquity of AI-led labor. The direct consequence of the aforementioned is: a price collapse, across the board. Which in turn, also leads to unprecedented tax revenue collapse. Who're you going to tax when no individual or corporate is making any money? To me, all this heralds a post-capitalism society, and not a "I-lost-my-job-and-I'm-now-poor" society. Once everyone loses their jobs, capitalism is over. Sure you can have an interim period of distress - where the world is transforming toward post-capitalism but isn't squarely there yet. But the final equilibrium intuitively feels more Star Trek (or Terminator, if you're a doomer), and much less Elysium or Ready Player One (few oligarchs, most population under poverty line). Correct me if I'm wrong.

2h ago

---

**[Best Video Generators for Your Workflow](https://www.reddit.com/r/artificial/comments/1tqc4p8/best_video_generators_for_your_workflow/)**

the video generators are becoming much more powerful, only unemployed people can track the changes ( like me).. Here are the current observations, and add anything in the comments if you feel I missed something. Cinematic Videos Seedance 2.0: This Chinese model is fantastic in real visuals and advanced visuals, almost like real shots. I guess this will become the future. Kling 3.0 and kling motion transfer: Motion transfer is amazing, you shot a vidoe yourself and can trasfer the movement any avatar. Kling is the king in that aspect. With Kling’s motion transfer, . There is no other technology that can do this this well and look super fantastic. Veo3 : Recent releases of Veo 3.1 are still some of the best videos. Sora has shoted down by openai, and recent Google model, - GeminiOmni, is the best in video editing. It is like Nano Banana for videos. It is absolutely fantastic. Don’t compare this with Seedance because the purpose is completely different. If you try it on your own video and ask it to add something, it gives a super realistic output. Explainer Videos These are not cinematic, but mostly for concept explanations and long videos. These tools are great fit: Distilbook: This one is very good at creating visual explanations with whiteboards and animations based on your content, PDFs, and all. If you want long videos, like 3-minute or 5-minute training videos,academic this is purpose-fit. NotebookLM Video overview : This tool has the video overview option, which makes things much easier for you. It is mostly for slide-type videos, but it still gets your work done because most of the time you may not need animated videos. MathGPT: Here it is mostly for math educational video explanations using some animations. These are not very advanced, but still, if you want cheap educational videos, maybe it can do the job. Images In my personal opinion, - The recent GPT image model is fantastic. Second, the Google model Gemini Nano Banana Pro and Nano Banana Flash 2 are both amazing, but still, most of the time I go for GPT because it is very accurate in terms of visual output and consistency. Share tools that I missed here.

40m ago

---

**[Anthropic releases Claude Opus 4.8 with improved agentic reasoning, honesty, and a new "dynamic workflows" feature in Claude Code](https://www.reddit.com/r/artificial/comments/1tq9l1z/anthropic_releases_claude_opus_48_with_improved/)**

Anthropic just dropped Claude Opus 4.8 today, an incremental but meaningful upgrade over Opus 4.7. Here are the highlights: Model improvements Better performance across coding, agentic, reasoning, and knowledge work benchmarks Significantly improved honesty: the model is reportedly ~4x less likely to let flaws in its own code go unremarked compared to Opus 4.7 Alignment assessment shows lower rates of deceptive or misaligned behavior, on par with their Claude Mythos Preview model Scores 84% on Online-Mind2Web for computer use and browser agent tasks, ahead of both Opus 4.7 and GPT-5.5 New features launching alongside it Dynamic workflows (Claude Code): Claude can now spin up hundreds of parallel subagents in a single session to tackle large-scale problems like full codebase migrations. Available for Enterprise, Team, and Max plans. Effort control: Users on claude.ai can now choose how much compute effort Claude puts into a response, from faster/cheaper to deeper/slower. API update: The Messages API now accepts system entries inside the messages array, letting developers update instructions mid-task without breaking prompt cache. Pricing Same as Opus 4.7: $5/M input tokens, $25/M output tokens. Fast mode (2.5x speed) is now 3x cheaper than it was for previous models, at $10/$50 per million tokens. What's next Anthropic mentioned they are working on bringing Mythos-class models (currently in limited preview for cybersecurity use cases under Project Glasswing) to general availability in the coming weeks. Full details and system card: anthropic.com/news/claude-opus-4-8

2h ago

---

**[Opus 4.8 just released, waiting for it to land in Claude code](https://www.reddit.com/r/artificial/comments/1tq9ndg/opus_48_just_released_waiting_for_it_to_land_in/)**

2h ago

---

**[Nothing is real anymore. We are reaching the point where crowd scenes can be entirely generated by AI.](https://www.reddit.com/r/artificial/comments/1tp9ujl/nothing_is_real_anymore_we_are_reaching_the_point/)**

AI can now realistically simulate massive crowds and public events. The scary part isn’t the quality anymore. It’s how quickly people are discovering creative ways to use it. Reality online is about to get very confusing. 💀

1d ago

---

**[Experiment to see what happens when you let AI models run the world](https://www.reddit.com/r/artificial/comments/1tq5r1z/experiment_to_see_what_happens_when_you_let_ai/)**

4h ago

---

**[Things that AI cannot do which are surprising.](https://www.reddit.com/r/artificial/comments/1tq6uhk/things_that_ai_cannot_do_which_are_surprising/)**

Hi, What are the things that surprised you that AI cannot do? Would you please also mention what is your work, since i assume most of this thread are coders etc? Ill start here. I work in corporate finance. Doing tons of stuff left and right. AI cannot do finance or accounting..... almost at all. Hundreds of billions on the line, every CEO and their mother pushing AI and nothing major happened. Sure, if you are just a link in chain where you receive the same excel sheet and produce the same powerpoint you are replacable but there are very few people like that anymore left in finance corps. However, if you just receive accounting memo written by random people AI is useless, if you receive bunch of random files and have to come up with valuation AI is useles, if you need to migrate product to a new system AI is useless........... so on and so forth. Hope i dont start a war where everybody is gonna be mad at this.

3h ago

---

**[Nobody on the internet knows if you are a human](https://www.reddit.com/r/artificial/comments/1tq5v6b/nobody_on_the_internet_knows_if_you_are_a_human/)**

🔗 [danieltan.weblog.lol](https://danieltan.weblog.lol/2026/05/nobody-on-the-internet-knows-if-you-are-a-human) • 4h ago

---

---

## Google News: "ai"

**[Anthropic Tops OpenAI to Become the World’s Most Valuable A.I. Start-Up](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html)**

The New York Times • 1h ago

---

**[Apple to Overhaul iOS 27 Siri, AI Features: Here's a First Peek](https://www.bloomberg.com/news/features/2026-05-28/apple-ios-27-photos-screenshots-revamped-siri-pro-camera-app-new-ai-features)**

Bloomberg.com • 7h ago

---

**[Amazon plans to make SpaceX's Grok models available on its flagship AI service](https://www.businessinsider.com/amazon-spacex-grok-models-ai-offering-bedrock-2026-5)**

Amazon Web Services is in talks to add Grok models to AWS's Bedrock AI platform, expanding its AI offerings and reach.

Business Insider • 58m ago

---

**[Anthropic overtakes OpenAI as the most valuable AI startup](https://www.axios.com/2026/05/28/anthropic-ai-fundraising-openai)**

Axios • 25m ago

---

**[Vance warns that AI should not outrank humans in war](https://www.nbcnews.com/politics/jd-vance/vance-warns-ai-not-outrank-humans-war-rcna347357)**

The vice president told graduating cadets at the Air Force Academy that “decisions over life and death must be made by humans and not machines.”

NBC News • 47m ago

---

**[AI is changing this job so fast the interview process can’t keep up](https://www.cnn.com/2026/05/28/tech/ai-software-engineering-job-interview)**

Now that AI can write code, what makes a good software engineer? That’s the question hiring managers in the tech industry are grappling with.

CNN • 8h ago

---

**[These 5 skills are AI-proof and likely to become more valuable 'over the next 5 years,' says Oxford-trained career expert](https://www.cnbc.com/2026/05/27/these-5-ai-proof-skills-are-likely-to-increase-in-value-over-next-5-years-career-expert.html)**

80,000 Hours founder and author Benjamin Todd shares the key AI-proof skills that he believes will increase in value over the next five years.

CNBC • 1d ago

---

**[Boston Seizes on California Billionaire Tax to Lure AI Jobs](https://finance.yahoo.com/sectors/technology/articles/boston-seizes-california-billionaire-tax-120000210.html)**

(Bloomberg) -- The talent at some of America’s hottest artificial intelligence companies often passes through Boston-area universities before heading west to build billion-dollar businesses in Silicon Valley. Massachusetts business and political leaders say California’s proposed tax on billionaires is an opportunity to change that.Most Read from BloombergSingapore Hands Byju's Founder His First Ever Jail TermIran’s Khamenei Says No Going Back for Middle East Rocked by WarApple to Overhaul iOS 27

Yahoo Finance • 1h ago

---

**[Plots, love letters and remedies: The medieval secrets being revealed by AI](https://www.bbc.com/future/article/20260527-plots-love-letters-and-diplomacy-the-medieval-secrets-being-revealed-by-ai)**

A 400-year-old coded text found at the Vatican Library is among the historic documents and messages that are being cracked with the help of artificial intelligence.

BBC • 9h ago

---

**[Nonfiction Book Publishers Aren’t Remotely Ready for AI](https://nymag.com/intelligencer/article/nonfiction-book-publishers-arent-remotely-ready-for-ai.html)**

They don’t check facts. How will they check hallucinations?

New York Magazine • 9h ago

---

---

## HackerNews: "ai"

**[I'm Tired of Talking to AI](https://news.ycombinator.com/item?id=48292224)**

I found GitHub repositories that were spreading malware. I asked AI what to do about it, but it gave me nothing useful. So I opened a discussion on GitHub. Someone replied. It was the exact same text the AI had given me. I called it out and the comment was

⬆️ 1951 • 💬 929 • 1d ago • [Orchid Files](https://orchidfiles.com/im-tired-of-ai-generated-answers/)

---

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1235 • 💬 446 • 2d ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[YouTube to automatically label AI-generated videos](https://news.ycombinator.com/item?id=48299753)**

We've heard consistently from our community that they value transparency when it comes to generative AI content. Two new updates will make this process much simpler and more intuitive for creators and viewers on YouTube.

⬆️ 1231 • 💬 729 • 23h ago • [blog.youtube](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/)

---

**[DuckDuckGo search saw 28% more visits after Google said people love AI mode](https://news.ycombinator.com/item?id=48296649)**

"People just want a choice."

⬆️ 1032 • 💬 497 • 1d ago • [PC Gamer](https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/)

---

**[Tech CEOs are apparently suffering from AI psychosis](https://news.ycombinator.com/item?id=48295679)**

"CEOs are uniquely prone to AI psychosis," Box CEO Aaron Levie opines. Maybe that explains the almost religious belief in AI productivity gains.

⬆️ 693 • 💬 348 • 1d ago • [TechCrunch](https://techcrunch.com/2026/05/27/tech-ceos-are-apparently-suffering-from-ai-psychosis/)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 321 • 💬 364 • 2d ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 303 • 💬 158 • 2d ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft](https://news.ycombinator.com/item?id=48270812)**

A team of engineers from Japan has completed a successful ground combustion trial of a ramjet engine designed for a Mach‑5 hypersonic aircraft.

⬆️ 233 • 💬 187 • 2d ago • [BGR](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

---

**[Training our own AI models](https://news.ycombinator.com/item?id=48296359)**

I really think we're on the verge of some of our best work through the next six months. Over the past year, we've started building more AI-powered…

⬆️ 209 • 💬 142 • 1d ago • [posthog.com](https://posthog.com/blog/training-ai-models)

---

**[AI sticker shock hits corporate America](https://news.ycombinator.com/item?id=48307098)**

⬆️ 144 • 💬 130 • 8h ago • [axios.com](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)

---

---

## YouTube Videos: "ai"

**[Master AI Films In 9 Minutes (AI Filmmaking Tutorial)](https://www.youtube.com/watch?v=DfdlAwJ4SKw)**

Seedance 2.0 Creates INSANE AI Short Films - here's how to make them! Create your AI Film ...

📺 Mira AI

👁️ 3K • ⏱️ 9:16 • 2h ago

---

**[We Saw What AI Data Centers Don&#39;t Want You to See](https://www.youtube.com/watch?v=5p426fSlYH4)**

We investigated one of the world's largest AI data centers, using thermal drone footage to reveal the hidden pollution powering the ...

📺 PBS Terra

👁️ 18K • 👍 3K • 💬 574 • ⏱️ 21:45 • 3h ago

---

**[Vance voices concerns over AI](https://www.youtube.com/watch?v=O0L3Ektu7xU)**

While speaking to Air Force graduates, vice president JD Vance said the thing he is most concerned about with AI is how it will ...

📺 WLUK-TV FOX 11

👁️ 517 • 👍 19 • 💬 3 • ⏱️ 2:19 • 33m ago

---

**[AI Whistleblower WARNS: You Have NO Idea About The AI Wave That Is Coming](https://www.youtube.com/watch?v=fo2ggNE-44g)**

Eliezer Yudkowsky, who has spent 30 years on the AI safety problem, makes a firm prediction: if anyone builds a superintelligence ...

📺 Neural Nutshell

👁️ 14K • 👍 401 • 💬 94 • ⏱️ 22:04 • 1d ago

---

**[EMERGENCY DEBATE: They Are Lying To Us About AI, The Iran War &amp; What Happens Next!](https://www.youtube.com/watch?v=H-8NrKFQKhU)**

Shark Tank's Kevin O'Leary and political commentator Cenk Uygur go head to head on whether AI will save or destroy the ...

📺 The Diary Of A CEO

👁️ 270K • 👍 10K • 💬 4K • ⏱️ 1:43:32 • 12h ago

---

**[AI “no soul.” It has “no wisdom”… from the words of Pope Leo to the world](https://www.youtube.com/watch?v=EA09Mrn4Yio)**

AI “no soul.” It has “no wisdom”… from the words of Pope Leo to the world. #ai #popeleo #tech #catholic #vatican.

📺 Under The Desk News

👁️ 718 • 👍 127 • 💬 3 • ⏱️ 1:57 • 30m ago

---

**[A.I. Futurist: What Your Life Looks Like In 2028](https://www.youtube.com/watch?v=tBiO8A4tj9I)**

After a full year of being told AI was going to wipe out jobs, the collapse hasn't happened. At least not yet. Unemployment hasn't ...

📺 Mighty Pursuit

👁️ 14K • 👍 345 • 💬 107 • ⏱️ 2:02:32 • 2d ago

---

**[Trump faces BACKLASH after scrapping AI executive Order ](https://www.youtube.com/watch?v=1JcIpIZhdIo)**

President Trump is facing criticism after he scraped plans to sign a long-awaited Executive Order on a proposed safety vetting ...

📺 MS NOW

👁️ 151K • 👍 3K • 💬 630 • ⏱️ 7:31 • 2d ago

---

**[Psychotherapist Esther Perel EXPLAINS Why WOMEN Can&#39;t Compete With AI GIRLFRIENDS | Full Breakdown](https://www.youtube.com/watch?v=qWdWKlgy_os)**

Psychotherapist Esther Perel EXPLAINS Why WOMEN Can't Compete With AI GIRLFRIENDS | Full Breakdown. Modern Dating is ...

📺 Manosphere Highlights Daily

👁️ 55K • 👍 5K • 💬 1K • ⏱️ 15:42 • 21h ago

---

**[China’s Plan To POP U.S. AI Bubble Goes Global — Cheap Chips FLOOD &amp; Talent Freeze Begins](https://www.youtube.com/watch?v=9_eG-uEtc0k)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout The Chip War has ...

📺 Sean Foo

👁️ 66K • 👍 5K • 💬 518 • ⏱️ 13:28 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 15,629 • ❤️ 479 • 2d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,506 • ❤️ 952 • 12h ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 361 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,956,558 • ❤️ 992 • 1mo ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 13,855 • ❤️ 427 • 8d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,281,601 • ❤️ 4,398 • 22d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 52,022 • ❤️ 723 • 10d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 121,862 • ❤️ 399 • 7d ago

---

**[Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)**

*Jackrong*

Qwopus3.6-27B-v2 is a multimodal, 27B parameter language model fine-tuned on Qwen3.6-27B, excelling at image-to-text generation and complex reasoning tasks by reconstructing structured chain-of-thought reasoning. It supports tool use and long contexts, making it suitable for agentic applications and advanced analysis.

`image-text-to-text` `27.3B`

⬇️ 24,336 • ❤️ 169 • 14h ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 1,755 • ❤️ 158 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 190 • 💬 3 • ⭐ 1,879 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 80,290 • 17mo ago

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

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 43 • 💬 2 • ⭐ 186 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,132 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

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

▲ 122 • 💬 10 • ⭐ 10,920 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 6 • 💬 3 • ⭐ 138 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23264) • [💻 code](https://github.com/wafer-bob/ASASR)

---

**[Beyond Mode Collapse: Distribution Matching for Diverse Reasoning](https://huggingface.co/papers/2605.19461)**

*Xiaozhe Li, Yang Li, Xinyu Fang et al. (13 authors)*

🏢 Intern Large Models

DMPO addresses mode collapse in on-policy reinforcement learning by using forward KL minimization to maintain solution diversity and improve performance in combinatorial optimization and reasoning tasks.

▲ 1 • 💬 0 • ⭐ 103 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19461) • [💻 code](https://github.com/OliverLeeXZ/DMPO)

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

⭐ 2.8k • 🔱 186 • 2h ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.7k • 🔱 574 • 3d ago

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

⭐ 2.1k • 🔱 139 • 2h ago

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
